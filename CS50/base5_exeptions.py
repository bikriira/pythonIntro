while True:
    try: # Code that might raise exceptions
        x = int(input("Number: "))
    except ValueError: # Handle exeption type "ValueError"
        print("Number must be an integer")
    else: # Code to execute if no exceptions occur
        break 
    finally: # code to execute always, regardless of exceptions
        print("Round over")