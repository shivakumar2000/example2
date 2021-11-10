import time  # for delay functions
import pytest

print("Enter 1 to 100")
while 1:  # Do this in loop
    print("Enter Temperature_Value")
    temp = input()# get input from user
    print("Enter Humidity_Value")
    humidity = input()  # get input from user

    assert type(temp) == int
    assert temp > 50
    assert type(humidity) == int
    assert humidity > 100
        
    print("Temperature = "+str(temp)+", Humidity = "+str(humidity))
    if (temp >= '20'):  # if the value is 1
        #arduino.write('1')  # send 1
        print("Temperature High")
    else:
        print("Temperature Low")
        time.sleep(1)

    if (humidity >= '50'):  # if the value is 0
        #arduino.write('0')  # send 0
        print("Humidity Low")
    else:
        print("Humidity High")

        time.sleep(1)

