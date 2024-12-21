# Setup & Usage
*Please read this document carefully. Missing even one step may result in errors.*

## Prerequisities

1. An Android phone/device (tested on Adnroid 15, however should also work on devices supported by the Automate app)
2. Python installed on your local machine (tested with 3.12, should work with 3.11 as well, no guarantees with older versions)
3. If you want to use Ollama, make sure Ollama is installed on the host machine.

## Automate
1. First, install the [Automate](https://llamalab.com/automate/) app on your Android device. This app allows you to create flows that can interact with Android APIs.
2. Then, import the flow linked in the releases page of Github here, into the Automate app.
3. In the flow, define the **BACKEND_HOST** variable to the IP address of the server running the Flask backend. If you use ollama, this will be the IP address of the computer running the Ollama server as well. If you wanat to use OpenAI instead of Ollama, set USEOPENAI to 1, indicating True. The default port of the backend is 4445.

**If you want to use OpenAI's api instead of Ollama, then you must set the OPENAI_API_KEY variable in the Automate flow to your OpenAI API key, AND enable OpenAI by setting USEOPENAI to 1 in the flow**

### The Automate flow setup is complete! Now, you can run the flask backend, and if you are using ollama, start your ollama server.

**Note:** The default model for Ollama in the Automate flow is llama3.1, as that has been the most tested for this project and the best performing. If you want to use a different model, you can manually change the model in the Automate flow. 

## Flask Backend (no setup needed, just run the server)

You need to run the Flask backend on the machine with the IP set in the BACKEND_HOST located in the Automate flow.

**Flask backend info:**

This project provides a Flask backend and an Automate flow for an Android SMS AI Assistant. The backend processes incoming SMS messages and determines whether the AI Assistant should respond based on various criteria. We use a backend to handle the core logic of validating senders, so that the Automate flow is more maintainable and the overall logic is more readable.

The Flask backend accepts POST requests with the following data:
1. `black_listed_numbers`: List of numbers that are blacklisted.
2. `sender_number`: The number from which the SMS was received.
3. `chat_log`: Log of the conversation including both sender numbers and assistant responses.
4. `allow_list`: List of numbers that are allowed to send messages, overriding the blacklist.
5. `phone_contacts`: List of phone contacts to avoid triggering the assistant for spam messages.
6. `block_spam`: Boolean value to block messages from numbers not in the phone contacts list. This won't affect anything if the phone contacts list is empty.
7. `max_messages_per_hour`: Maximum number of messages the assistant can respond to from a number per hour.

**These parameters are set via the automate workflow for convenience.**

The backend returns whether the assistant should respond to the message, and even returns the chat_log (and the sender_chat_log if the number passes). We send the chat_log because Automate updates it, in case the Flask backend updates it by removing messages of a blocked number that has sent the max amount of messages per hour.

> [!NOTE] 
> In case you are wondering why the Flask backend doesn't handle everything, including the request to the LLM provider, I still need to decide whether or not the Flask backend and the Automate flow should have such a relationship. As of now, the Automate flow contributes to handling the chat_log in addition to the LLM response, which may be more convenient for some, as when the flow is stopped, the chat_log is not saved on the backend but rather reset. If this is a problem, the relationship will be changed so that the Flask backend does more of the work than it does now, thus leading to a simpler Automate flow.

> [!CAUTION] 
> If the Automate flow is terminated, but then restarted while the backend is still running, chat logs will be reset. This is for convenience, as if you want to change something on the Automate workflow, you can do it quickly without having to access the backend. Also, it is assumed that once you enter the phone, you are actually available to respond to your messages.

## Optional tmux launch script
Optionally, you can run the provided script to run the servers in a tmux session, side-by-side. This is for convenience, and you can also run the servers separately if you wish.
Use the `tmux_server_launcher.sh` script to start the Flask server and Ollama server in a tmux session (must have tmux installed, of course Ollama as well). Of course, you can also do these separately if you wish, and the script is only there for convenience.
**Note**: If using this tmux launcher script, you must define the FLASK_BACKEND_PATH to the absolute path of the flask_backend.py file.

## Customization Instructions

### Variables in Automate Flow

> [!NOTE] 
> All of the variables that you can set are located on top of the Automate flow, separated from the rest of the logic. However, here they are listed as well:

Important Variables (these should NOT be optional, so please fill them out when setting up the flow)

1. `NAME`: Your name to give to the LLM for reference, so that it has context to who it is serving.
2. `OUTREASON`: Message explaining why you're unavailable **If not provided, assistant may make things up!**
3. `ASSISTANTNAME`: The name of your assistant.
4. `BACKEND_HOST`: IP address of the machine running the Flask backend
5. `OPENAI_API_KEY`: Your OpenAI API key **(ONLY required if USEOPENAI=1)**

**Optional Variables**

1. `MAXMESSAGESPERHOURPERUSER`: Maximum messages a number can send per hour (default: 3)
2. `USEOPENAI`: 0 for false, 1 for true. If this is enabled, make sure that you have provided an OpenAI API key!
3. `BLOCKSPAM`: Set to 1 to block numbers not in your contacts
4. `ALLOWLIST`: These are the numbers that are **only allowed** for the assistant to respond. Allow list overrides everything, except for the max messages per hour per person limit. If you want other things such as block spam or the blacklist to work, then make sure your allow list is empty.
5. `BLACKLISTNUMBERS`: These are the numbers that you do not want the assistant to respond to. However, if a number in the blacklist is in the allow list, it will be allowed.

> [!NOTE] 
> For the block spam feature to work, you must provide contact permissions for Automate. Otherwise, it will not be able to find who isn't or who is a contact.

### Number List Formatting
When entering numbers in the Automate flow variables:
- For `BLACKLISTNUMBERS` and `ALLOWLIST`, separate numbers with a single space
- Example format: "+1234567890 +0987654321 +1122334455"
- Do not use commas or other separators
- Include the country code with + symbol

### Chat Log Format
The chat log alternates between sender messages and assistant responses:
- Even indices: Sender messages (format: "sendernumber: message")
- Odd indices: Assistant responses

### Important Notes
- If you are completely new to Automate, starting the flow can be easily done by pressing the Start button in the app. Very convenient!
- If you restart the Automate flow, the chat log resets even if the backend is still running
- The backend runs on port 4445 by default
- When using Ollama, ensure your machine has sufficient RAM for the chosen model
- The Flask backend must be running with the Automate flow for this to work correctly.

> [!CAUTION] 
> Please be responsible with this tool. I take no responsibility with what you do. Be cautious when using things such as OpenAI or setting the max messages per hour per user, as they may be subject to costing money when using OpenAI. This project is for educational purposes only!

If you find any errors regarding the setup process, please feel free to open an issue!