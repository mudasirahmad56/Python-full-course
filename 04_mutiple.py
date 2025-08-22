a = int(input("Enter your age :"))

#if statement 01
if(a%2==0):
    print("Even age")

#if statement 02
if (a >= 20):
    print("your are eligible to apply")

elif (a < 0):
    print("Invalid negative age")

elif (a==0):
    print("not a valid age")

else:
    print("you are not eligible to apply")

print("thank you for checking your eligibility")

