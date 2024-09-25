#!/usr/bin/env python3

def admin_login(username, password):
    # your code here
    # username=("ADMIN","admin")
    # password="12345"
    # return "Access granted" if username="true" and password="true" else "Access denied"
    if(username =="admin" and password =="12345"):
        return "Access granted"
    elif(username =="ADMIN" and password =="12345"):
        return "Access granted"
    else:
        return "Access denied"

def hows_the_weather(temperature):
    # your code here
    # temperature== <40
    # dict_map={
    #     >40 and <65 : "It's a little chilly out there!",
    #     >85 : "It's too dang hot out there!",}
    # weather =dict_map.get(temperature,"It's perfect out there!")
    # return weather
    if(temperature  < 40):
        return "It's brisk out there!"
    elif(temperature  >= 40 and temperature <= 65):
        return "It's a little chilly out there!"
    elif(temperature  > 85):
        return "It's too dang hot out there!"
    else:
        return "It's perfect out there!"


def fizzbuzz(num):
    if(num % 3 == 0 and num % 5 == 0):
        return "FizzBuzz"
    elif(num % 5 == 0):
        return "Buzz"
    elif(num % 3 == 0):
        return "Fizz"
    else:
        return num
    # your code here

def calculator(operation, num1, num2):
    # your code here
    # operation=["+","-","*","/"]
    # if(operation[i] == "true"):
    #     return (num1 operation[i] num2)
    # else:
    #     print("Invalid operation!")
    #     return None
    if(operation == "+"):
        return num1 + num2
    elif(operation == "-"):
        return num1 - num2
    elif(operation == "*"):
        return num1 * num2
    elif(operation == "/"):
        return num1 / num2
    else:
        print("Invalid operation!")
        return None
               
