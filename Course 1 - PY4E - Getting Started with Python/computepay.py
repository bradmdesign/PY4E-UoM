

hrs = float(input("Enter Hours:"))
pay = float(input("Enter your pay:"))

def computepay(h,r):
    if hrs > 40:
        return ((hrs - 40)*1.5*pay)+(40*pay)
    else:
        return (hrs*pay)


p = computepay(10,20)
print("Pay",p)
