import random

def celsius_to_fahrenheit(celsius):
    """將攝氏溫度轉換為華氏溫度"""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """將華氏溫度轉換為攝氏溫度"""
    return (fahrenheit - 32) * 5/9

def electricity_to_money(a):
    """計算用電量對應的電費"""
    if a == 0:
        return "用電量為零，無需計費"
    elif a <= 200:
        return a * 3.2  # 用電量小於或等於 200 度
    elif 200 < a <= 300:
        return 200 * 3.2 + (a - 200) * 3.4  # 用電量在 200 到 300 度之間
    elif a > 300:
        return 200 * 3.2 + 100 * 3.4 + (a - 300) * 3.6  # 用電量大於 300 度

def eat():
    """隨機抽取餐廳"""
    foods = []
    try:
        with open('food.txt', 'r', encoding='utf-8') as file:
            for line in file:
                foods.append(line.strip())
        # 隨機選擇餐廳
        result = random.choice(foods) if foods else "食物清單是空的，請檢查 food.txt 文件。"
    except FileNotFoundError:
        result = "找不到 'food.txt' 文件，請確認文件存在。"
    return result