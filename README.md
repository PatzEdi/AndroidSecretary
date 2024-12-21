<!-- omit in toc -->
# AndroidSecretary 

<p align="center">
  <img src="assets/ASLogo.png" alt="ASLogo">
</p>

<p align="center">
  <i>Your personal, context-aware AI SMS secretary for Android</i>
</p>

<!-- omit in toc -->
# Table of Contents
- [DEMO](#demo)
- [Setup \& Usage](#setup--usage)
- [Features](#features)
- [Can I run this project on my phone without an external computer?](#can-i-run-this-project-on-my-phone-without-an-external-computer)
- [Project Structure](#project-structure)
- [Known Limitations](#known-limitations)
- [Tested LLM Models](#tested-llm-models)
- [Resources](#resources)
- [Contributing](#contributing)
- [License](#license)

<!-- omit in toc -->
> [!NOTE]
> This project uses [Automate](https://llamalab.com/automate/) to easily access Android APIs and create a flow for an AI Assistant. The backend is written in Python using Flask and assistant responses are made with Ollama or OpenAI. Thank you Automate for making this process easier!

**ALSO** this project is still in its early stages. I plan to develop it further, but not at the fastest pace as I am working on bigger projects right now. I take no responsibility for any damage conducted by this tool. It is strictly for educational purposes only.

## DEMO

https://github.com/user-attachments/assets/5fc198e6-d253-4e33-b1c7-203c4fba1a2b

*The responses in the demo were gathered using Ollama and llama3.1 on an M1 Macbook Air. It works very well even with the 8b model!*

Sorry for the small backend text, I wanted to make the two videos synchronized so I put them together.

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
As of now, there are only a few known limitations to how this works. The biggest one (first one below) may be added as a feature later on (although, I will quickly state here that it would require some restructuring of the project, as the Flask backend would do more of the work than it does now, as explained in the [setup & usage process](SETUP.md)).

1. **AndroidSecretary can't process more than one response at a time.** In other words, if one message is still being processed, and another message comes in at the same time, then it will not register the second message. Each process of the message must finish for the Automate flow to detect a second incoming message, but since the chat_log is handled by the Automate app in conjunction with the Flask backend, simply duplicating or having various instances of the Automate flow would not work, as the chat_logs would be disjoint/unrelated between the two flows, leading to improper handling of message validation.
2. No RCS support. So far, only SMS messages work. With some modifying of the Automate flow, however, MMS messages may also be supported, although that hasn't been tested. Until Automate will release RCS support, only SMS is indeed supported.

## Tested LLM Models
1. Llama3.1 with Ollama has been tested. The 8B parameter works just fine, so higher parameter models would work as well.
2. For OpenAI usage, GPT-4 is unfortunately better than gpt-3.5-turbo for this, which is costly. I have tried gpt-3.5-turbo, but it does not give reliable responses and sometimes misses important context. Perhaps there are other OpenAI models that are cheaper than GPT-4 that work well. If there are, feel free to create an issue!

## Resources
- [Automate](https://llamalab.com/automate/)
- [Flask](https://flask.palletsprojects.com/en/2.0.x/)
- [Ollama](https://ollama.ai/)
- [OpenAI](https://openai.com/)

If you like AndroidSecretary, make sure to give it a star! ⭐️

## Contributing
If you would like to contribute to this project, feel free to fork the project and make a pull request. I will review the pull request and merge it if it fits the project. If you have any questions, feel free to open an issue.

Also, to make sure everything works fine, run the unittests :)

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

[^ Back To Top ^](#table-of-contents)
