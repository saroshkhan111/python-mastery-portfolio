while True:    

    user_input = input("Enter command for s/w: (start/stop/pause)")

    match user_input:
        case "start":
            print("S/w is starting.....")
        case "stop":
            print("S/w is stopping.....")
        case "pause":
            print("S/w is pausing.....")
        case _:
            print("Invalid command,Please Enter Valid Command")
            
    software_stop = input("Do you want to stop the software? (yes/no)")
    if software_stop.lower() == "yes":
        break
       