import init     # Import init and shell modules for shell and global vars support
import shell

def su(suuser,perm):    # Define su function with user to switch to and permission check
    if init.database.get(suuser)==None: # If given user not exists, print that out
        print(f"User {suuser} not found.")
        
    elif perm==True:    # If permission check successes, substitute user immediatelly
        shell.shell(suuser)
        
    else:               # Else check if account isn't locked, if so print that out
        password = init.database.get(suuser)[0]
        if password=="!":
            print(f"Account {suuser} is locked.")
            
        else:           # Ask for a password, if correct substitute user, if not print that out
            loginpassword=input(f"Password for {suuser}: ")
            if loginpassword==password:
                shell.sh(suuser)
            else:
                print("Login incorrect.")

def useradd(newuser,perm):  # Define useradd function with new username and permission check
    global database         # Declare needed global
    
    if perm==False:         # If permission check fails, print that out
        print("You do not have permission.")
        
    else:
        if init.database.get(newuser) != None:  # If an user actually exists, print that out
            print("This user actually exists!")
        else:
            y = []  # Set a temporary list
            for x in init.database: # Get all UUIDs in database
                y.append(init.database.get(x)[1])
            newuuid=max(y)+1 # Generate new UUID
            
            init.database.update({newuser:["!",newuuid]}) # Create the user
            print(f"New user named {newuser} created.")   # Print out the confirmation
            
def userdel(deluser,perm):  # Define userdel function with user to delete and permission check
    global database         # Declare needed global
    
    if perm==False:         # If permission check fails, print that out
        print("You do not have permission.")
        
    elif deluser=="root":   # If trying to delete root, print that out
        print("You can't delete root user!")
        
    elif init.database.get(deluser)==None:      # If user not exists, print that out
        print(f'User {deluser} not exists!')
    
    else:
        while True: # loop until answer given
            sel=input(f'Are you sure to delete user {deluser}? (Y/n): ') # ask for confirmation
            sel.lower() # lower the selection
            if sel=="y":    # if selection is yes, pop the user from database
                init.database.pop(deluser)
                return 0
            elif sel=="n":  # if it is no simply exit the function
                return 0
            else:           # if the selection is incorrect, print that out
                print('Please enter "y" or "n".')

            
def passwd(moduser,user):   # Define userdel function with user to change password and user doing it
    global database         # Declare needed global
    
    if init.database.get(moduser)==None:    # If user not exists, print that out
        print(f"User {moduser} not found.")
        
    else:
        if moduser != user and user != "root": # If user isn't root or isn't changing his own password, print out the denial
            print("You do not have permission.")
            
        else:
            print(f"Changing password for {moduser}:")  # Print header
            if user != "root":                          # If current user isn't root, ask for current password
                curr=input("Current password: ")
                if curr!=init.database.get(moduser)[0]: # If password is incorrect, print that out
                    print("Incorrect password!")
                    return 0
            while True:     # loop
                pass1=input("New password: ")        # Ask for new password
                pass2=input("Retype new password: ") # Ask for retype
                
                if pass1==pass2:                     # If passwords match, save it to the database, confirm and exit function
                    data=init.database.get(moduser)
                    data[0]=pass1
                    init.database.update({moduser:data})
                    print("Password successfully changed.")
                    return 0
                else:
                    print("Passwords do not match! Please try again.") # If passwords do not match, print that out
