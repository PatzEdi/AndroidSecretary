# Python file to test sending requests without having to send curl via the terminal.
import requests

def post_sms_allow(
    black_listed_numbers=[],
    allow_list=[],
    phone_contacts=[],
    block_spam=False,
    sender_number='',
    chat_log='',
    max_messages_per_hour=5,
    url='http://localhost:4445/sms_allow'
):
    """
    Sends a POST request to the Flask endpoint '/sms_allow' with the specified data.

    Args:
        black_listed_numbers (list): List of blacklisted phone numbers.
        allow_list (list): List of allowed phone numbers.
        phone_contacts (list): List of phone contacts.
        block_spam (bool): Boolean indicating whether to block spam messages.
        sender_number (str): The sender's phone number.
        chat_log (str): The chat log content.
        max_messages_per_hour (int): Maximum number of messages allowed per hour.
        url (str): The URL of the Flask endpoint.

    Returns:
        dict: The JSON response from the server.
    """

    # Construct the data payload matching the expected format by the Flask endpoint
    data = {
        'black_listed_numbers': ' '.join(black_listed_numbers),
        'allow_list': ' '.join(allow_list),
        'phone_contacts': ' '.join(phone_contacts),
        'block_spam': block_spam,
        'sender_number': sender_number,
        'chat_log': chat_log,
        'max_messages_per_hour': max_messages_per_hour
    }

    # Send the POST request with JSON payload
    try:
        response = requests.post(url, json=data)
        response.raise_for_status()  # Raise an error for bad status codes
        return response.json()
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    # Example data
    black_listed_numbers = ['+19494126173']
    allow_list = ['+19494126173']
    phone_contacts = []
    block_spam = False 
    sender_number = '+19494126173'
    chat_log = ["+19494126173\nHello, how are you?\n","Example assistant response"] # continue if necessary: "+19494126173\nYes that is fine, thanks."]
    max_messages_per_hour = 1

    # Send the POST request
    response = post_sms_allow(
        black_listed_numbers,
        allow_list,
        phone_contacts,
        block_spam,
        sender_number,
        chat_log,
        max_messages_per_hour
    )

    # Handle the response
    if response:
        print("Server Response:", response)