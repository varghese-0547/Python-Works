s=''
hi=["HI","Hai","hai","hello","Hello","Hey there","hi",
    "Hi","hey there","hello there","Hello there"]
if s in hi:
    print ("Hi I'm Swen")
print ("How can I help you")
print('1. Calculate BMI')
print('2. Encode Ph. no.')
print('3. Decode Ph. no.')
print('4. Encode to morse')
print('5. Decode from morse')
c = input('\nEnter Choice : ')
print()
if c=='1':
    print('BMI  \n')
    import BMI
    print()
elif c=='2':
    print('Encode no.  \n')
    from Code_language import Encd_no
    print()
elif c=='3':
    print('Decode no.  \n')
    from Code_language import Dcod_no
    print() 
elif c=='4':
    print('Encode morse  \n')
    from Code_language import Encd_morse
    print() 
elif c=='5':
    print('Decode morse  \n')
    from Code_language import Dcod_morse
    print() 


'''

# *_________*_________* Name Sequence *__________*_________*


N = input("Name : ")
print ("Hello there",N ,"nice to meet you. May I know your age")


#*__________*__________* Age Sequence *_________*__________*


Age = eval(input("Age : "))
if Age < 25:
    print ("Oh you'r younger than me. I'm 25")

elif Age == 25:
    print ("Oh you'r my same age. I'm also 25")

elif Age > 25:
    print ("Oh you'r older than me. I'm only 25")

'''
#*__________*__________* Shutdown Sequence *__________*__________*


print("Do your selection wisely.\n\n")
c=input("Do yo whish to close ? : ")
l=['No','no','NO','Nah','nah','NAH','N','n']
if c in l:
    print ("Okay")

else :
    import os
    print("Danger")

    os.system("shutdown /s /t 1")
'''
#*__________*__________* Date Sequence *__________*__________*

var = input ("Do you want to know date : ")  
l=['Yes','yes,'YES',yah,'Yah','YAH','ok','OK','Ok','Okay','okay,'OKAY']
def Date():
    from datetime import datetime as dt
    print(dt.now()) # 2020-03-29 01:43:03.170480
if var in l:
    from datetime import date

    today = date.today()
    # DD/MM/YYYY
    d1 = today.strftime("%d/%m/%Y")
    print("Today's date is", today)


else :
    print("Sorry, I am not well trained")
'''
