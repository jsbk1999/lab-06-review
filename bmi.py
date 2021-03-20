import sys
W = float (input("Enter your weight (in pounds): "))
H = float (input("Ok, also enter your height (in inches): "))
BMI = (W * 703) / (H ** 2)
print("Your body mass index (BMI) is " + str(BMI) + "%")
