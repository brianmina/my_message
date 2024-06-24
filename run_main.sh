#!/bin/bash
export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv init -)"
xvfb-run -a /home/brianmina17/.pyenv/shims/python /home/brianmina17/workspace/github.com/brianmina/my_message/main.py >> /home/brianmina17/workspace/github.com/brianmina/my_message/main.log 2>&1
