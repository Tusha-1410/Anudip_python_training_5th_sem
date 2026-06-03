second = int(input("enter time in seconds"))

if(second < 0):
    exit("time cannot be negative ....exited")

    print("---------------------")

elif(second >= 3600):
        hour = second // 3600
        second = second % 3600

elif( second >= 60):
        minute = second // 60
        second = second % 60
else:
        hour = 0
        minute = 0

print("time in hours is" , hour)
print("time in minutes is" , minute)
print("time in seconds is" , second)