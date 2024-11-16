# AndroidSecretary 

## **Note:** 
This project uses [Automate](https://llamalab.com/automate/) to easily access Android API's and create a flow for an AI Assistant. The backend is written in Python using Flask and assistant responses are made with Ollama or OpenAI. Thank you Automate for making this process easier!

Checkout out the [setup & usage process](SETUP.md) to get started!

## Features
1. Ollama & OpenAI Support (with ollama, an external computer more powerful than the phone is likely needed to run more context-wise LLM's)
2. Context-based assistant responses to messages received.
3. Cutomization - Name your assistant, limit the max amount of messages per hour per user, blacklist and allowlist features, block spam feature (provided you give your list of phone contacts to Automate), and an optional reason why you are not available, to let senders know what you are doing.

## Can I run this project on my phone without an external computer?
1. **Yes**, you can run the servers locally using Termux! Just clone the repo to Termux, install Flask if you havn't in Termux, and you can run the flask_backend.py file.
2. **Yes**, you can run this project fully on your phone without an external computer. However, the Ollama server may be slow on a phone, and you may need to use OpenAI for better context handling.


## Project Structure

- `tmux_server_launcher.sh`: Script to launch the Flask server and Ollama server in a tmux session. **Note:** You must have tmux installed, AND you must define the FLASK_BACKEND_PATH to the absolute path of the flask_backend.py file.
- `src/flask_backend.py`: Flask backend implementation that processes SMS messages.
 
## Resources used:
- [Automate](https://llamalab.com/automate/)
- [Flask](https://flask.palletsprojects.com/en/2.0.x/)
- [Ollama](https://ollama.ai/)
- [OpenAI](https://openai.com/)

If you like AndroidSecretary, make sure to give it a star! ⭐️

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing
If you would like to contribute to this project, feel free to fork the project and make a pull request. I will review the pull request and merge it if it fits the project. If you have any questions, feel free to open an issue.


[^ Back To Top ^](#androidsecretary)