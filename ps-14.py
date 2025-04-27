# Python Program to Check Prime Number(প্রাইম+মৌলিক সংখ্যা+নম্বর চেক করার জন্য পাইথন প্রোগ্রাম)

num = 37

if num <= 1:
    print("it's not Prime Number")
elif num <= 3:
    print("it's Prime Number")
elif num % 2 == 0 or num % 3 == 0:
    print("it's not Prime Number")
else:
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i+2) == 0:
            print("it's not Prime Number")

        i += 6
    else:
        print("it's Prime Number")

