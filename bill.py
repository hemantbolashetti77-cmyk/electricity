import sys
Rate=5
if len(sys.argv) == 2:
    units = float(sys.argv[1])
else:
    print("No input given - using default units")
    units = 100  

bill_amount = units * Rate  # Ch

print("Units Consumed:", units)
print("Rate per Unit:", Rate)
print("Total Bill Amount: ₹", bill_amount)
