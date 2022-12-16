import time

def count_down(t):
    while t > 0:
        print(t)
        t -= 1
        time.sleep(1)



x = int(input("enter a number: "))
count_down(x)