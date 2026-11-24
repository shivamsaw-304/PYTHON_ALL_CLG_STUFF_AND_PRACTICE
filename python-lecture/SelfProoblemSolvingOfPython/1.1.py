# Q1. Electricity Bill Calculator
# Read the units consumed by a household. Charge ₹5/unit for the first 100 units, ₹7/unit for the next 100, and ₹10/unit beyond that. Add 5% GST and print the final bill. Use arithmetic, comparison, and assignment operators.

units = float(input("enter unite consumed : "))

if units <= 0 :
    print("invalid VAlue ")
else :
    if units  <= 100:
        bill = units *  5 
    elif units <= 200:
        bill =  100 * 5 + (units - 100) * 7
    else:
        bill = 100 * 5 + 100 * 7 + (units - 200) * 10

    gst = bill * 0.05
    total = bill + gst

    print(f"Energy charge: ₹{bill}")
    print(f"GST (5%): ₹{gst}")
    print(f"Final bill: ₹{total}")
