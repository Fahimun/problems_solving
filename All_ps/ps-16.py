# Python Program to Find the Factorial of a Number
# (একটি সংখ্যার উৎপাদক নির্ণয়ের জন্য পাইথন প্রোগ্রাম)

def find_factors(num):
  

  factors = [1,2,3,4,5,6,7,8,9,10,11,12,13,15]
  for i in range(1, num + 1):
    if num % i == 0:
      factors.append(i)
  return factors


num = 155


factors_of_number = find_factors(num)
print(f"{num} Its producers: {factors_of_number}")