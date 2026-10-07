"""
Problem Statement
The alarm triggers if the system is "Armed".
If armed, check if "Motion Detected" is True. If motion is detected, check if the
time is "Night". If Night, print "Call Police Immediately". If "Day", print
"Send Alert to Owner". If not armed, print "System Idle".
"""

# st 1: Print the header Security System Checker
print()
print("=" * 50)
print("            Security System Checker Program: ")
print("=" * 50)

# st 2: Get Armed status from the system
system_armed = input("Enter the Armed Status (Armed/Not Armed): ").strip().lower()

# check the status of System Armed or not
is_armed = (system_armed == "armed")

# st 3: Get Motion detector from the system
motion_detector = input("Enter the status of Motion Detector (Detected/Not Detected): ").strip().lower()

# check the motion status from the system
is_motion = (motion_detector == "detected")

# st 4: check the night status
time_status = input("Enter time status (Day/Night): ").strip().lower()

# check is night or not
is_night = (time_status == "night")

print()

# apply the Nested if/else for checking status
if is_armed: # check the outer condition

    # check motion is detected
    if is_motion:

        # check the night status
        if is_night:
            print("Call Police Immediately")
        else:
            print("Send Alert to Owner")    
    else:
        print("Motion is not detected")
else:
    print("System Idle")

print()