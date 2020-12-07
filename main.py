#!/bin/python3

import subprocess # To support rebooting
import sys # To support args from command line

def firmware(): # Definition of firmware
    
    global systemcode   # Declaring needed global vars
    global args
    
    if args.count("--firmware") > 0:        # If firmware was loaded with argument,
        args.pop(args.index("--firmware"))  # remove it to not be used anymore

    print("PyUnix Firmware not supported yet.") # Print out information that firmware is not ready yet
    systemcode = 6 # Set systemcode to 6 (normal boot)
    
args = sys.argv.copy() # Copy args to modify them safely

if args.count("--firmware") > 0: # If there is "--firmware" in args,
    systemcode = 5               # set systemcode to 5 (enter firmware),
else:                            # else set it to 6 (normal boot)
    systemcode = 6

while True:                     # Main loop
    if systemcode == 0:         # If systemcode is 0 (exit), break from the loop
        break
    
    elif systemcode == 5:       # If systemcode is 5 (enter firmware), call firmware
        firmware()
        
    elif systemcode == 6:       # If systemcode is 6 (normal boot):
        command = ['./boot.py'] + args  # Set up the script adding args
        systemcode = subprocess.call(command)   # Run the boot subprocess with args and set the systemcode to the returned value
        args = []               # Clear the args out
