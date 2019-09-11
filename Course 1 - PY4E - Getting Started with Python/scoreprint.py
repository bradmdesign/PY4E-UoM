score = float(input("Give us a score between 0.0 and 1.0: "))
try:
    if score < 0.0:
        print("Error, too low")
    elif score > 1.0:
        print("Error, too high.")
    elif score >=0.9:
            print ("A")
    elif score >= 0.8:
            print ("B")
    elif score >= 0.7:
            print ("C")
    elif score >= 0.6:
            print ("D")
    elif score < 0.6:
            print ("F")
except:
    print("Out of range.")
    quit()
