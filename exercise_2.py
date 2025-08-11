import time
timestamp = time.strftime('%H:%M:%S')
print(time.strftime('%A'), time.strftime('%d/%B/%Y'), "Current Time: ",timestamp, "IST")
# print(time.strftime('%B'))

if ("00:00:00" <= timestamp <= "12:00:00"):
    print("Good Morning Sir")


elif("12:00:00" <= timestamp <= "16:00:00"):
        print("Good Afternoon Sir")
    
    
elif("16:00:00" <= timestamp <= "20:00:00"):
        print("Good Evening Sir")
    
    
else:
    print("Good Night Sir")
    


    