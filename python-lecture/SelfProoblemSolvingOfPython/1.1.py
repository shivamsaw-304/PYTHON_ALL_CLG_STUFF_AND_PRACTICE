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


# Take the principal, annual interest rate, and tenure in years. Calculate the EMI using EMI = P*r*(1+r)^n / ((1+r)^n - 1), where r is the monthly rate and n is the number of months. Display the result rounded to 2 decimals. Also print the data type of each input.

principleAmt = float(input("enter princi[le amount : "))
intrestRate = float(input("interest rate : "))
tenure = int(input("Added tenure of intrest in years : "))

intrestRate = intrestRate / 12 / 100

mont = tenure *  12 


emi = principleAmt*intrestRate*(1+intrestRate)**mont / ((1+intrestRate)**mont - 1)

print(f"emi : {emi}")

print(f"data type of amount : {type(principleAmt)}")

print(f"data type of intrest : {type(intrestRate) }")

print(f"data type of intrest :  {type(tenure) }")










