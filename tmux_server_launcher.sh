
tmux has-session -t android_sms_servers 2>/dev/null
if [ $? -eq 0 ]; then
  tmux kill-session -t android_sms_servers
fi

# Create a new tmux session named "servers" and start it detached
tmux new-session -d -s android_sms_servers

# Split the window vertically
tmux split-window -h

# In the left pane (Flask server), run the Flask server
tmux send-keys -t android_sms_servers:0.0 'python3 /Users/edwardferrari/VIM_tests/android_sms_assistant_flask_backend/src/flask_backend.py' C-m


# In the right pane (Ollama server), run the Ollama server
tmux send-keys -t android_sms_servers:0.1 'ollama serve' C-m

# Attach to the session to view both panes
tmux attach-session -t android_sms_servers
