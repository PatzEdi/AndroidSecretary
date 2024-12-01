<!-- omit in toc -->
# Table of Contents
- [Setup \& Usage](#setup--usage)
- [Features](#features)
- [Can I run this project on my phone without an external computer?](#can-i-run-this-project-on-my-phone-without-an-external-computer)
- [Project Structure](#project-structure)
- [Known Limitations](#known-limitations)
- [Resources](#resources)
- [License](#license)
- [Contributing](#contributing)

<!-- omit in toc -->
# AndroidSecretary 

![ASLogo](assets/ASLogo.png)
<!-- omit in toc -->
## **Note:** 
This project uses [Automate](https://llamalab.com/automate/) to easily access Android API's and create a flow for an AI Assistant. The backend is written in Python using Flask and assistant responses are made with Ollama or OpenAI. Thank you Automate for making this process easier!

**ALSO** this project is still in its early stages. I plan to develop it further, but not at the fastest pace as I am working on bigger projects right now. I take no responsibility for any damage conducted by this tool. It is strictly for education purposes only.

## Setup & Usage
Checkout out the [setup & usage process](SETUP.md) to get started!

## Features
1. Ollama & OpenAI Support (with ollama, an external computer more powerful than the phone is likely needed to run more context-wise LLM's, unless you have a phone at least 12 GB of RAM)
2. Context-based assistant responses to messages received.
3. **Customization**:
   1.  Name your assistant
   2.  Limit the max amount of messages per hour per user 
   3.  Blacklist and allowlist features (allowlist overrides blacklist)
   4.  Block spam feature (provided you give your list of phone contacts to Automate) 
   5.  Optional reason why you are not available, to let senders briefly know what you are doing.
   6.  Possibility of doing much more as well!

## Can I run this project on my phone without an external computer?
1. **Yes**, you can run the servers (both Flask and Ollama) locally using Termux. Just clone the repo to Termux, install Flask if you havn't in Termux, and you can run the flask_backend.py file. However, the Ollama server may be slow on a phone, and you may need to use OpenAI for better context handling.


## Project Structure

- `src/flask_backend.py`: Flask backend implementation that processes SMS messages.
- `tmux_server_launcher.sh`: Script to launch the Flask server and Ollama server in a tmux session. **Note:** This is strictly optional. If you want to use it, you must have tmux installed, AND you must define the FLASK_BACKEND_PATH to the absolute path of the flask_backend.py file.

## Known Limitations
As of now, there is only one know limitation to how this works, which may be added as a feature later on (although, I will quickly state here that it would require some restructuring of the project, as the Flask backend would do more of the work than it does now, as explained in the [setup & usage process](SETUP.md)).
1. **AndroidSecretary can't process more than one response at a time.** In other words, if one message is still being processed, and another message comes in at the same time, then it will not register the second message. Each process of the message must finish for the Automate flow to detect a second incoming message, but since the chat_log is handled by the Automate app in conjunction with the Flask backend, simply duplicating or having various instances of the Automate flow would not work, as the chat_logs would be disjoint/unrelated between the two flows, leading to improper handling of message validation.

## Resources
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