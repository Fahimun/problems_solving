# Python Program to Check Leap Year(লিপ ইয়ার পরীক্ষা করার জন্য পাইথন প্রোগ্রাম)
year1 = 2024
year2 = 2025
check_opction = 100,400,4

if year1 % 400 == 0:
 print(f"{year1}: leap year")

elif year1 % 100 == 0:
  print(f"{year1}: not leap year")
elif year1 % 4 == 0:
  print(f"{year1}: leap year")
else:
  print("not leap year")  

