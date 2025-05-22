# Python Program to Print the Fibonacci sequence
# (ফিবোনাচ্চি সিকোয়েন্স প্রিন্ট করার জন্য পাইথন প্রোগ্রাম)

num = 5

a, b = 0, 1
count = 0
print("Fibonacci sequence:")
while count < num:
    print(a, end="")
    a, b = b, a+b

    count += 1

