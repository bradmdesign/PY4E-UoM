while True:
    myname = input("What's your name, slick?")
    charactercount = (len(myname))
    if charactercount > 10:
        print("Your name is too long. Please fix this.")
    elif charactercount <= 10:
        print("Registered.")