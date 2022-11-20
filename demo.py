# WAP to Convert distance into feet to inches and inches into feet
#take two user input
num1 = int(input("enter the distance in feet:-"))
num2 = int(input("enter the distance in inch:-"))
inch = num1 * 12
feet = num2/12
print("The distance in inches is %i inches." % inch)
print(f"There are {round(feet,4)} feet in {inch} inch(es)")