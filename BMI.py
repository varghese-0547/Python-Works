W=float(input("Enter your wiaght in kilogram : "))
H=float(input("Enter your height in meter : "))
H/=100
BMI=W/(H**2)
if BMI<18.5:
    print("Your BMI is",BMI,"\nCategory : Underweight")
elif 18.5 <= BMI < 24.9:
    print("Your BMI is",BMI,"\nCategory : Normal")
elif 24.9 <= BMI < 30:
    print("Your BMI is",BMI,"\nCategory : Overweight")
elif BMI > 30:
    print("Your BMI is",BMI,"\nCategory : Obesity")
