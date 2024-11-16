import 數學計算.operations
from 工具計算 import operations


if __name__ == "__main__":
    op = input("歡迎來到Derrick工具包，請選擇您要的功能:1.溫度轉換 2.電費計算 3.兩數相加 4.吃什麼:")
    if op =="1":
        operations.temperature()
    elif op == "2":
        operations.eBill()
    elif op == "3":
        print(數學計算.operations.add(3,8))
    elif op == "4":
        print(operations.lunch())