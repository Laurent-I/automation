#!/bin/bash
python -c "import os, sys, time, shutil, tkinter, watchdog, colorama" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "Installing necessary Python packages..."
    pip install watchdog colorama
fi

# Get the current working directory
CURRENT_DIR=$(pwd)

# Add the current directory to the PATH temporarily for this session
export PATH="$CURRENT_DIR:$PATH"

# Notify the user
echo "Current directory has been added to the PATH."
echo "To permanently add it, consider adding the export command to your .bashrc or .bash_profile file."
