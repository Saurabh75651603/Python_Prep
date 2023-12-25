height = float(input("Enter your height in foot and inches: "))
weight = float(input("Enter your height in kilograms and grams:"))

bmi = weight /(height ** 2)

if bmi < 18.5:
    print("You are underweight and need to gain some.")
    print()
elif 18.5 <= bmi < 25:
    print("You are healthy and fit, need to be stuck with these routines")
    print()
elif 25 <= bmi < 30:
    print("You are overweight and need to focus on the healthy diet and excercise.")
    print()
else:
    print("You are Obese and need to strictly follow the healthy diet and excercise and routine.")