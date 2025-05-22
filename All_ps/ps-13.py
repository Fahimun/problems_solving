# Python Program to Find the Largest Among Three Numbers
# (তিনটি সংখ্যার মধ্যে বৃহত্তম সংখ্যা খুঁজে বের করার জন্য পাইথন প্রোগ্রাম)

number1 = 55
number2 = 45
number3 = 33

if number1 >=number2 and number1 >=number3:
    print(f"{number1}: Largest number")

elif number2 >= number1 and number2 >=number3:
    print(f"{number2}: Largest number")

elif number3 >= number1 and number3 >= number2:
    print(f"{number3}: Largest number")

else:
    print("Not Largest number")    
