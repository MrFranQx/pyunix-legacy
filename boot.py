#!/bin/python3

import init # Import init control module
import sys # To support given args

def boot(args=[]): # Define boot function
    if "--init" in args:                        # If runlevel was declared with --init argument,
        level = args[args.index("--init") + 1]  # set it to given value,
    else:                                       # else set it to 2
        level = 2
        
    exit(init.init(level)) # Execute init with given runlevel, after that exit with returned systemcode

print("PyUnix Development Test\n") # Print out the MOTD

args = sys.argv.copy() # Copy the args to modify them safely
args.pop(0)            # Pop the useless filename argument
boot(args)             # Execute boot function
