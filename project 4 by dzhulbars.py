#task1
def arifmetic(a,b,operation):
    if operation == '+':
        return a+b
    elif operation == '-':
        return a-b
    elif operation == '*':
        return a*b
    elif operation == '**':
        return a**b
    elif operation == '/':
        return a/b
    else:
        return 'Invalid operation'
a=int(input("Enter a digit: "))
b=int(input("Enter a second digit: "))
operation=input("Enter a symbol(+,-,*,**,/): ")
result=arifmetic(a,b,operation)
print(f"The result: {result}")
#task2
year=int(input("Enter a year: "))
if year%4==0:
    print("It is a leap year")
else:
    print("It is not a leap yar ")
#task3
import math
def square(x):
    perimetr=x*4
    area=x**2
    diagonal=x*math.sqrt(2)
    return perimetr,area,diagonal
perimetr,area,diagonal=square(17)
print(f"The perimetr: {perimetr}")
print(f"The area: {area}")
print(f"Diagonal: {diagonal}")
#task4
def season():
    season=int(input("enter a month: "))
    if season==12 or season==1 or season==2:
        print("winter")
    elif season==3 or season==4 or season==5:
        print("spring")
    elif season==6 or season==7 or season==8:
        print("summer")
    elif season==9 or season==10 or season==11:
        print("autumn")
    else:
        print("incorrect month")
month=season()
print(month)
#task5
def bank():
  n=float(input("Enter the deposit amount: "))
  years=int(input("Enter the deposit period: "))
  for a in range(years):
    n+=n*0.10
  return n
print(f"The invested amount that will be received: {bank()}")
#task6
def is_prime():
    x=int(input("Enter a digit: "))
    if x<2:
        return False
    elif x==2:
        return True
    for a in range(2,x):
        if x%a==0:
            return False
        return True
result=is_prime()
print(f"The result: {result}")
#task 7
import datetime
def date():
    today=datetime.datetime.now().date()
    year=int(input("Enter a year: "))
    month=int(input("Enter a month: "))
    day=int(input("Enter a day: "))
    date=datetime.date(year,month,day)
    if date==datetime.datetime.now().date():
        return f"Correct: {today}"
    else:
        return f"Incorrect...Correct date is: {today}"
print(date())
#task8
def count_uc_lc(word):
    upper_count=0
    lower_count=0
    for word in word:
        if word.isupper():
            upper_count+=1
        elif word.islower():
            lower_count+=1
    return {"Upper":upper_count,"Lower":lower_count}
word=input("Enter a word: ")
result=count_uc_lc(word)
print(f"The result: {result}")
#task9
import math
a=int(input("Enter a digit to count factorial: "))
n=math.factorial(a)
print(f"The Factorial: {n}")
#task11
import math
a=int(input("Enter a digit: "))
b=int(input("Enter a digit: "))
ab=math.gcd(a,b)
print(f"Mutual divider: {ab}")