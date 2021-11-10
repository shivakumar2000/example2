import time  # for delay functions
temp = 0
humidity = 0

def get_temperature():
    global temp
    print("Enter Temperature : ")
    temp = input()
    return temp
def get_humidity():
    global humidity
    print("Enter Humidity : ")
    humidity = input()
    return humidity

print("The Temperature is : ", temp)
print("The humidity is : ", humidity)
