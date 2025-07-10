def divide(a,b):
    try:
        print(a//b)
    except ZeroDivisionError:
        print("you can't divide by zero")
a,b=map(int,input().split())
divide(a,b)