hrs = input("Enter Hours:")
h = float(hrs)
pay = input("Enter Pay rate:")
if float(hrs) >= 40 :
    overtime = float(hrs) - 40
    hrs = float(hrs) - float(overtime)
totalpay = (float(overtime)*float(pay)*1.5) + (float(pay) * hrs)
print(totalpay)
