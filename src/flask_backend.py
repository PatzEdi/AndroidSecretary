from flask import Flask, request, jsonify

# NOTES: 
# This file will be runnable both on Android and on a PC. You will be able to choose which one via the Automate workflow.

# Our flask backend will accept a request for each SMS recieved. The request will contain: 1. black listed numbers 2. Sender's number 3. Chat Log (contains both sender numbers and assistant responses) 4. "Allow only" overrides blacklist & only allows sms messages from numbers in this list, if there are any 5. Phone contacts list- optional but useful to avoid triggering the assistant when spam arrives to the phone - blacklist can override this 6. Block spam - a boolean value that ignores numbers that aren't in the phone contacts list. If the phone contacts list is empty, then block_spam won't affect anything, as it will be set the False (can't check for spam without a contacts list). Based on this information, we return whether or not a number can proceed to recieving a message from the assitant. We will handle that in the Automate app.

# The point of the Flask backend is that not all of our logic will be in the Automate app workflow, but rather be made in Python. For now, this python backend will receive a request from the Automate app as soon as an SMS message is detected, and return True or False on whether or not the AI Assistant should respond to the message.

# We will use the Flask library to create a simple web server that will accept POST requests. We will then use the requests library to send a POST request to the server. We will also use the json library to parse the JSON data that we receive.

class FlaskBackend:
    def __init__(self):
        self.app = Flask(__name__)
        self.set_app_routes()
    def start(self, port=5000, debug=False, host='0.0.0.0'):
        self.app.run(host=host, port=port, debug=debug)

    # Define app routes:
    def set_app_routes(self):

        @self.app.route('/sms_allow', methods=['POST'])
        def sms_allow(self):
            data = request.get_json()
            black_listed_numbers = data['black_listed_numbers'].split(' ')
            allow_list = data['allow_list'].split(' ')
            phone_contacts = data['phone_contacts'].split(' ') # if empty, wwe process whether or not the number is in the allow list or black list for all numbers. If not empty, we only process the numbers in the phone contacts list IF block_spam is set to True. 
            block_spam = data['block_spam']
            sender_number = data['sender_number']
            chat_log = data['chat_log']

            # Our logic will go here
            # We will return a response based on our logic
            return jsonify({'response': 'ok'})

if __name__ == '__main__':
    app = FlaskBackend()
    # Start the app:
    app.start(port=4445)

