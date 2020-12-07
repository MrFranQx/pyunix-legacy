import shell # Import shell module to be able to run it

def init(level=2):      # Define init function with runlevel defaulting to 2
    global runlevel     # Set runlevel
    runlevel=str(level)
    
    global database     # Set user database
    database = {"root":["passwd",0],"user":["qwerty",1000]}
    
    global shellterminate # Set shellterminate variable which tells if shell should terminate or not
    shellterminate = False
    while True:           # Main loop
        
        if runlevel=="0":           # If runlevel is 0, return systemcode 0 (exit)
            return 0
        
        elif runlevel=="s":         # If runlevel is s (single user), ask for root password and run shell
            shell.sh(login("root"))
            shellterminate=False

        elif runlevel=="1":         # If runlevel is 1 (alias for s), ask for root password and run shell
            shell.sh(login("root"))
            shellterminate=False

        elif runlevel=="2":         # If runlevel is 2 (normal mode), display login prompt and run shell
            shell.sh(login())
            shellterminate=False

        elif runlevel=="5":         # If runlevel is 5, return systemcode 5 (enter firmware)
            return 5

        elif runlevel=="6":         # If runlevel is 6, return systemcode 6 (reboot)
            return 6

                                    # If runlevel is not valid, display a message and set runlevel to 2
        elif not runlevel in ["0", "1", "2", "3", "4", "5", "6", "s"]:
            print("Only runlevels 0-6 and s are valid.")
            runlevel="2"

        else:                       # If runlevel is not supported (levels 3 and 4), display a message and set runlevel to 2
            print("Runlevel not supported yet.")
            runlevel="2"

def login(user=None):               # Define login function, default with no initial username
    while True:                     # Main loop
        if user == None:                # If no initial username provided,
            loginuser=input("Login: ")  # display login prompt and save username,
        else:                           # else save initial username
            loginuser=user
        password = database.get(loginuser)[0]   # Get the given user's password
        
        if password==None:                      # If there is no such user, display a message
            print(f"User {loginuser} not found.")
            
        elif password=="!":                     # If account is locked, display a message
            print(f"Account {loginuser} is locked.")
            
        else:                                                   # Prompt for a password,
            loginpassword=input(f"Password for {loginuser}: ")  # if correct return the username,
            if loginpassword==password:                         # else display a message and loop
                return loginuser
            else:
                print("Login incorrect.")

def telinit(level,perm):    # Define telinit function to change runlevels with wanted level and permission check
    global runlevel         # Declare needed global vars
    global shellterminate
    
    if perm == False:        # If permission check fails, print a message
        print("You do not have permission.")
    elif level != runlevel: # If current runlevel is not the same as given runlevel, terminate the shell and change current runlevel
        shellterminate = True
        runlevel = level

def shutdown(action,perm):  # Define shutdown function to change the system state and permission check
    global runlevel         # Declare needed global vars
    global shellterminate
    
    if perm==False:         # If permission check fails, print a message
        print("You do not have permission.")
                            
                            # Else terminate the shell and run given action
    elif action=="-i0":     # (shutdown)
        shellterminate = True
        runlevel = "0"
        
    elif action=="-is":     # (single user)
        shellterminate = True
        runlevel = "s"
        
    elif action=="-i5":     # (enter firmware)
        shellterminate = True
        runlevel = "5"
        
    elif action=="-i6":     # (reboot)
        shellterminate = True
        runlevel = "6"
