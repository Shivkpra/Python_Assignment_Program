#Write a function to compute 5/0 and use try/except to catch the exceptions.
def div(n):
    return n/0

try:
    n=int(input("Enter the number: "))
    div(n)
except ZeroDivisionError:
    print ("the number should not divided  by zero!")
except Exception:
    print ('Caught an exception')
finally:
    print ('In finally block for cleanup')
