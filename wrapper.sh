
#!/bin/bash

# Start the virtual display
Xvfb :100 -screen 0 1024x768x16 &

# Wait a moment to ensure Xvfb is fully started
sleep 2

# Set the DISPLAY variable
export DISPLAY=:100

# Run your pyautogui script
/home/brianmina17/workspace/github.com/brianmina/my_message/python_script_for_testing.py

