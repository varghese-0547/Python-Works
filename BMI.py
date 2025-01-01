while True:
    W=float(input("Enter your weight in kilogram : "))
    H=float(input("Enter your height in centi meter : "))
    H/=100
    BMI=W/(H**2)
    print(" ")
    if BMI<18.5:
        print("Your BMI is",BMI,"\nCategory : Underweight")
        print('''\nUnderweight = <18.5
Normal weight = 18.5–24.9
Overweight = 25–29.9
Obesity = BMI of 30 or greater''')
        break
    elif 18.5 <= BMI < 25.0:
        print("Your BMI is",BMI,"\nCategory : Normal")
        print('''\nUnderweight = <18.5
Normal weight = 18.5–24.9
Overweight = 25–29.9
Obesity = BMI of 30 or greater''')
        break
    elif 25.0 <= BMI < 30:
        print("Your BMI is",BMI,"\nCategory : Overweight")
        print('''\nUnderweight = <18.5
Normal weight = 18.5–24.9
Overweight = 25–29.9
Obesity = BMI of 30 or greater''')
        break
    elif 41>BMI >= 30:
        print("Your BMI is",BMI,"\nCategory : Obesity")
        print('''\nUnderweight = <18.5
Normal weight = 18.5–24.9
Overweight = 25–29.9
Obesity = BMI of 30 or greater''')
        break
    else:
        print("\nSorry, there is an error.\nEnter one more time\n")
        continue
