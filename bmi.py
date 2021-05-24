# Asks for height and weight

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

# Calculates BMI

bmi = round(weight / height ** 2)

if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")

elif bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")

elif bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")

elif bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")

else:
    print(f"Your BMI is {bmi}, you are clinically obese.")

""" 
Under 18.5 is underweight
Over 18.5 but below 25 is a normal weight
Over 25 but below 30 is slightly overweight
Over 30 but below 35 is obese
Above 35 is clinically obese. 
"""
