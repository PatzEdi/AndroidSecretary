# AndroidSecretary 

![ASLogo](assets/ASLogo.png)
## **Note:** 
This project uses [Automate](https://llamalab.com/automate/) to easily access Android API's and create a flow for an AI Assistant. The backend is written in Python using Flask and assistant responses are made with Ollama or OpenAI. Thank you Automate for making this process easier!

# Setup & Usage
Checkout out the [setup & usage process](SETUP.md) to get started!

## Features
1. Ollama & OpenAI Support (with ollama, an external computer more powerful than the phone is likely needed to run more context-wise LLM's, unless you have at least 12 GB of RAM)
2. Context-based assistant responses to messages received.
3. **Customization**:
   1.  Name your assistant
   2.  Limit the max amount of messages per hour per user 
   3.  Blacklist and allowlist features (allowlist overrides blacklist)
   4.  Block spam feature (provided you give your list of phone contacts to Automate) 
   5.  Optional reason why you are not available, to let senders briefly know what you are doing.
   6.  Possibility of doing much more as well!

## Can I run this project on my phone without an external computer?
1. **Yes**, you can run the servers locally using Termux. Just clone the repo to Termux, install Flask if you havn't in Termux, and you can run the flask_backend.py file. However, the Ollama server may be slow on a phone, and you may need to use OpenAI for better context handling.


## Project Structure

- `src/flask_backend.py`: Flask backend implementation that processes SMS messages.
- `tmux_server_launcher.sh`: Script to launch the Flask server and Ollama server in a tmux session. **Note:** This is strictly optional. If you want to use it, you must have tmux installed, AND you must define the FLASK_BACKEND_PATH to the absolute path of the flask_backend.py file.
 
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