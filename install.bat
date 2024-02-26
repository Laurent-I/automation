@echo off
echo Checking for necessary Python packages...
python -c "import os, sys, time, shutil, tkinter, watchdog, colorama" 2>NUL
if %errorlevel% neq 0 (
    echo Installing necessary Python packages...
    pip install watchdog colorama
    echo Python packages installed successfully.
) else (
    echo All necessary Python packages are already installed.
)

@echo off
setlocal EnableDelayedExpansion

rem Get the current working directory
set "CURRENT_DIR=%CD%"

rem Add the current directory to the system PATH
setx PATH "%CURRENT_DIR%;%PATH%"

rem Notify the user
echo Current directory has been added to the PATH.
echo Please restart the command prompt for changes to take effect.
