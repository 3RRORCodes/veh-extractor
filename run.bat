@echo off
setlocal enabledelayedexpansion
mode con: cols=80 lines=25
color 0b

:: Batch file to run the Python script for categorizing vehicles
title Vehicle Names Extraction Tool by 3RROR

:check_python
:: Check if Python is installed
where python >nul 2>&1
if errorlevel 1 (
    color 0c
    echo +===========================================================+
    echo ^|                         ERROR                             ^|
    echo ^|                                                           ^|
    echo ^|         Python is not installed or not in PATH            ^|
    echo ^|            Please install Python to proceed.              ^|
    echo +===========================================================+
    echo.
    choice /c YN /n /m "Would you like to install Python now? [Y/N]: "
    if errorlevel 2 (
        echo.
        echo Exiting. Please install Python and try again.
        pause
        exit /b 1
    )
    if errorlevel 1 (
        echo.
        echo Redirecting to Python download page...
        start https://www.python.org/downloads/
        pause
        exit /b 1
    )
)

:menu
cls
echo +===========================================================+
echo ^|           Vehicle Names Extraction Tool by 3RROR           ^|
echo +===========================================================+
echo ^|                                                           ^|
echo ^|                  [1] Drag and Drop Folder                 ^|
echo ^|                  [2] Enter Path Manually                  ^|
echo ^|                  [3] Exit                                 ^|
echo ^|                                                           ^|
echo +===========================================================+
echo.
choice /c 123 /n /m "Select an option [1-3]: "

if errorlevel 3 goto exit
if errorlevel 2 goto manual_input
if errorlevel 1 goto drag_drop

:drag_drop
cls
echo +===========================================================+
echo ^|     Drag and drop the folder containing vehicle           ^|
echo ^|     subfolders here and press Enter:                     ^|
echo +===========================================================+
echo.
set /p "directory="
if "!directory!"=="" (
    echo Invalid input. Please try again.
    pause
    goto menu
)
goto process_directory

:manual_input
cls
echo +===========================================================+
echo ^|            Enter the full path to the folder:             ^|
echo +===========================================================+
echo.
set /p "directory="
if "!directory!"=="" (
    echo Invalid input. Please try again.
    pause
    goto menu
)
goto process_directory

:process_directory
if not exist "!directory!" (
    color 0c
    echo.
    echo +===========================================================+
    echo ^|    Error: Directory does not exist.                       ^|
    echo ^|    Please check the path and try again.                   ^|
    echo +===========================================================+
    pause
    goto menu
)

:: Call the Python script with the directory as an argument
python vehicle_extractor.py "!directory!"

:: Check if the Python script executed successfully
if errorlevel 1 (
    color 0c
    echo.
    echo +===========================================================+
    echo ^|    Error: The Python script encountered an error.         ^|
    echo +===========================================================+
    pause
    goto menu
)

:: Success message
color 0a
echo.
echo +===========================================================+
echo ^|           Processing completed successfully!               ^|
echo +===========================================================+
pause
goto menu

:exit
echo.
echo Exiting...
pause
exit /b 0

:error
color 0c
echo.
echo +===========================================================+
echo ^|    An error occurred. Please check your input and try     ^|
echo ^|    again.                                                 ^|
echo +===========================================================+
pause
color 0b
goto menu