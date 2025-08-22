marks1 = int(input("Enter marks 1:"))
marks2 = int(input("Enter marks 2:"))   
marks3 = int(input("Enter marks 3:"))

total_percentage = (100)*(marks1 + marks2 + marks3) / 300

if (total_percentage >= 40):
    print("You have passed the exam.", total_percentage)
else:
    print("You have failed the exam try next year", total_percentage)

