import random

def celsius_to_fahrenheit(celsius):
    """
    將攝氏溫度轉換為華氏溫度
    """
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# 華氏轉攝氏
def fahrenheit_to_celsius(fahrenheit):
    """
    將華氏溫度轉換為攝氏溫度
    """
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def temperature():
    kind = input("請輸入使用的類型1.攝氏 2.華式")
    if kind == "1":
      num = int(input("請輸入攝氏溫度:"))
      print(f"{num}°C 對應的華氏溫度是 {celsius_to_fahrenheit(num):.2f}°F")
    else:
      num = int(input("請輸入華氏溫度:"))
      print(f"{num}°F 對應的攝氏溫度是 {fahrenheit_to_celsius(num):.2f}°C")

def eBill():
   while True:
    try:
        num = float(input('請輸入用電度數（輸入負數結束程式）：'))

        # 如果輸入負數，結束程式
        if num < 0:
            print("程式結束，再見！")
            break

        output = 0
        if num <= 200:
            output = num * 3.2
        elif num <= 300:
            output = 200 * 3.2 + (num - 200) * 3.4
        else:
            output = 200 * 3.2 + 100 * 3.4 + (num - 300) * 3.6

        print(f'用電 {num} 度共 {output:.2f} 元')
    except ValueError:
        # 捕捉非數值輸入的錯誤
        print("輸入錯誤！請輸入正確的數字。")

def lunch():

    foods = []
    
    with open("lunch.txt","r",encoding="utf-8") as file:
       for line in file:
          foods.append(line.strip())

    result = random.choice(foods)

    return result