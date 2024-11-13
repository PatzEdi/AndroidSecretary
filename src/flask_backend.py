from flask import Flask, request, jsonify
import time # To keep track of blocked numbers
"""
NOTES:
This file will be runnable both on Android and on a PC. You will be able to choose which one via the Automate workflow.

Our flask backend will accept a request for each SMS received. The request will contain:
1. Black listed numbers
2. Sender's number
3. Chat Log (contains both sender numbers and assistant responses)
4. "Allow only" overrides blacklist & only allows SMS messages from numbers in this list, if there are any
5. Phone contacts list - optional but useful to avoid triggering the assistant when spam arrives to the phone - blacklist can override this
6. Block spam - a boolean value that ignores numbers that aren't in the phone contacts list
7. Max messages per number per hour - determines the max amount of messages the assistant can respond to a number each hour. If the phone contacts list is empty, then block_spam won't affect anything, as it will be set to False (can't check for spam without a contacts list).

Based on this information, we return whether or not a number can proceed to receiving a message from the assistant. We will handle that in the Automate app.

The point of the Flask backend is that not all of our logic will be in the Automate app workflow, but rather be made in Python. For now, this Python backend will receive a request from the Automate app as soon as an SMS message is detected, and return True or False on whether or not the AI Assistant should respond to the message.

We will use the Flask library to create a simple web server that will accept POST requests. We will then use the requests library to send a POST request to the server. We will also use the json library to parse the JSON data that we receive.
"""

class FlaskBackend:
    
    blocked_numbers : dict
    
    def __init__(self):
        self.app = Flask(__name__)
        self.set_app_routes()
        self.blocked_numbers  = {}
    def start(self, port=5000, debug=False, host='0.0.0.0'):
        self.app.run(host=host, port=port, debug=debug)

    # Define app routes:
    def set_app_routes(self):

        @self.app.route('/sms_allow', methods=['POST'])
        def sms_allow():
            data = request.get_json()
            print(data)
            black_listed_numbers = data['black_listed_numbers'].split(' ')
            allow_list = data['allow_list'].split(' ') if len(data['allow_list'].strip()) > 0 else [] # Make sure to split the string into a list, only if it's not empty
            phone_contacts = data['phone_contacts'].split(' ') if len(data['phone_contacts'].strip()) > 0 else [] # if empty, wwe process whether or not the number is in the allow list or black list for all numbers. If not empty, we only process the numbers in the phone contacts list IF block_spam is set to True. 
            block_spam = data['block_spam']
            sender_number = data['sender_number']
            sender_message = data['sender_message']
            chat_log = data['chat_log'] if data['chat_log'] else []
            max_messages_per_hour = data['max_messages_per_hour']
            
            validity = self.check_number(sender_number, sender_message, black_listed_numbers, allow_list, phone_contacts, block_spam, max_messages_per_hour, chat_log)
            print(validity)
            # Our logic will go here
            if validity:
                # We then get the sender_chat_log, which is just the messages of that sender, and the corresponding assistant message, in the chat_log.
                sender_chat_log = self.get_sender_chat_log(sender_number, chat_log)
                print("\nCHAT LOG:")
                print(chat_log)
                print("\n\nSENDER CHAT LOG:")
                print(sender_chat_log)

                return jsonify({'response': 'valid', 'chat_log': chat_log, 'sender_chat_log': sender_chat_log})
            
            # We will return a response based on our logic
            return jsonify({'response': 'invalid', 'chat_log': chat_log}) # We may have removed the sender's messages from the chat log, so we will return the chat log back to Automate, so that it can update the chat log. 
    
    
    def check_number(self, sender_number, sender_message, black_listed_numbers, allow_list, phone_contacts, block_spam, max_messages_per_hour, chat_log):
        # First thing to check is if the number is blocked because it has in the past reached its max messages per hour:
        if sender_number in list(self.blocked_numbers.keys()):
            if time.time() < self.blocked_numbers[sender_number] + 3600: # 3600 seconds in an hour
                return False # If the number is still blocked, we return False.
            # If 1 hour has passed, we remove the number from the blocked numbers list:
            del self.blocked_numbers[sender_number] # Remove the number from the blocked numbers list, as it has been an hour since it was blocked.
                
        # We first need to check if the max_messages_per_hour has been reached for the sender_number. This overrides all other checks, including allow list and black list. 
        if self.get_num_messages(sender_number, chat_log) == max_messages_per_hour: # Will never be above the max_messages per hour, as we will block the number after it reaches the limit.
            # WIP: Add logic here that will block the number from sending more messages for the next hour. We can do this by creating a dictionary with the key as the number and the value as the time the number was blocked. We will then check if the current time is greater than the time the number was blocked + 1 hour. If it is, we will unblock the number.
            self.blocked_numbers[sender_number] = time.time()
            # We then delete the messages that the number has sent from the chat log, so that the number can start fresh after the hour is up. We will pass the chat log back to Automate, so that it can update the chat log.
            self.remove_messages(sender_number, chat_log)
            return False
        # Allow list has the highest priority. If a number is in the allow list and the allow list is not empty, it will be allowed to proceed.
        if (allow_list) and (sender_number in allow_list):
            return True 
        elif (allow_list) and (sender_number not in allow_list):
            return False
        # Black list has the second highest priority. If a number is in the black list, it will be blocked, unless it is in the allow list.
        if sender_number in black_listed_numbers:
            return False
        # If the phone contacts list is not empty, we will only allow numbers in the phone contacts list to proceed, if block_spam is set to True, unless they are in the allow list or black list.
        if block_spam and phone_contacts and sender_number not in phone_contacts:
            return False
            
        return True
    
    
    def get_num_messages(self, sender_number, chat_log):
        count = 0
        # We search how many times the string number occurs in the list chat_log:
        for i in range(len(chat_log)):
            if i % 2 == 0: # We only want the sender's messages, which are at even indices in the list. 
                # If the message is a sender message, then we process it below:
                count += 1 if chat_log[i].find(sender_number) == 0 else 0 # We use find, as the number may be in the message, but not at the start of the message. Otherwise, there would be the vulnerability of a number being in the message, but not being the sender's number.
            
        return count
    
    # Removes both the sender number's message, and the assistant's message from the chat log, which is right after the sender's message.
    def remove_messages(self, sender_number, chat_log):
        i = 0
        while i < len(chat_log):
            if chat_log[i].find(sender_number) == 0: 
                chat_log.pop(i)
                chat_log.pop(i)
                continue # We skip the increment of i, as we have removed two elements from the list.
            i += 2
        return chat_log
        

    def get_sender_chat_log(self, sender_number, chat_log):
        sender_chat_log = []
        i = 0
        while i < len(chat_log)-1:
            if chat_log[i].find(sender_number) == 0: # Again, we can't just uses the "in" keyword, as the number may be in the message, but not at the start of the message.
                sender_chat_log.append(chat_log[i])
                sender_chat_log.append(chat_log[i+1])
            i += 2
        return sender_chat_log

if __name__ == '__main__':
    app = FlaskBackend()
    # Start the app:
    app.start(port=4445)

