import operations
import random

if __name__ == "__main__":
    a = input('請輸入要哪個專案:(1)溫度 (2)電度(3)抽取餐廳: ')

    if a == "1":
        
        celsius = float(input("請輸入攝氏溫度: "))  
        print(operations.celsius_to_fahrenheit(celsius))  

    elif a == "2":

        electricity = float(input("請輸入用電量 (度): "))  
        print(operations.electricity_to_money(electricity)) 

    elif a == "3":
        print(operations.eat()) 

    else:
        print("無效選項，請選擇 1 或 2 或 3")
