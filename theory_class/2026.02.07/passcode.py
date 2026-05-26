def check_passcode(attempts=3):
    correct_pass = 1234
    access_granted = False
    for _ in range(attempts):
        passcode = int(input("Enter the passcode: "))
        if passcode == correct_pass:
            print("Access Granted")
            access_granted = True
            break
    if not access_granted:
        print("System Locked")


check_passcode()
