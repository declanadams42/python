# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
# The BMI is a measure of some's weight taking into account their height. e.g.
#  If a tall person and a short person both weigh the same amount, the short person is usually more overweight.
# The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):





weight = int(input("enter your weight in kg:\n"))
height = float(input("enter your height in m:\n"))

result = (weight / height ** 2 )
bmi = int(result)

print("your BMI is " + str(bmi))



