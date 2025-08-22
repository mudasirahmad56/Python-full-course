a = int(input("Enter your age :"))

if (a >= 20):
    print("your are eligible to apply")

elif (a < 0):
    print("Invalid negative age")

elif (a==0):
    print("not a valid age")

else:
    print("you are not eligible to apply")

print("thank you for checking your eligibility")
