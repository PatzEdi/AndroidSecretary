# Setup & Usage
## Automate
1. First, install the [Automate](https://llamalab.com/automate/) app on your Android device. This app allows you to create flows that can interact with Android API's.
2. Then, import the flow linked in the releases page of the github here, into the Automate app.
3. In the flow, define the **BACKENDHOST** variable to the IP address of the server running the Flask backend. If you use ollama, this will be the IP address of the computer running the Ollama server as well. If you are using OpenAI, set USEOPENAI to 1, indicating 1.

**If you want to use OpenAI's api instead of Ollama, then you must set the OPENAI_API_KEY variable in the Automate flow to your OpenAI API key.**

The Automate flow setup is complete! Now, you can run the flask backend, and if you are using ollama, start your ollama server.

**Note:** The default model for ollama is llama3.1, as that has been the most tested for this project and the best performing. If you want to use a different model, you can manually change the model in the Automate flow. 

Optionally, you can run the provided script to run the servers in a tmux session, side-by-side. This is for convenience, and you can also run the servers separately if you wish.
Use the `tmux_server_launcher.sh` script to start the Flask server and Ollama server in a tmux session (must have tmux installed, of course ollama as well) Of course, you can also do these separately if you wish, and the script is only there for convenience.
**Note**: You must define the FLASK_BACKEND_PATH to the absolute path of the flask_backend.py file.

## Flask Backend (no setup needed, just run the server)

Flask backend info:

This project provides a Flask backend and an Automate flow for an Android SMS AI Assistant. The backend processes incoming SMS messages and determines whether the AI Assistant should respond based on various criteria. We use a backend to handle the core logic of allowing senders, so that the Auomate flow is more maintainable and the overall logic is more readable.

The Flask backend accepts POST requests with the following data:
1. `black_listed_numbers`: List of numbers that are blacklisted.
2. `sender_number`: The number from which the SMS was received.
3. `chat_log`: Log of the conversation including both sender numbers and assistant responses.
4. `allow_list`: List of numbers that are allowed to send messages, overriding the blacklist.
5. `phone_contacts`: List of phone contacts to avoid triggering the assistant for spam messages.
6. `block_spam`: Boolean value to block messages from numbers not in the phone contacts list. This won't affect anything if the phone contacts list is empty.
7. `max_messages_per_hour`: Maximum number of messages the assistant can respond to from a number per hour.

**These parameters are set via the automate workflow for convenience.**

The backend returns whether the assistant should respond to the message, and even returns the chat_log (and the sender_chat_log if the number pases). We send the chat_log because Automate updates it, in case the Flask backend updates it by removing messages of a blocked number that has send the max amount of messages per hour.

**Note:** If the Automate flow is terminated, but then restarted while the backend is still running, chat logs will be reset. This is for convenience, as if you want to change something on the Automate workflow, you can do it quickly without having to access the backend. Also, it is assumed that once you enter the phone, you are actually available to respond to your messages.
