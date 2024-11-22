a = int(input("введимт число odin "))
b = int(input("введимт число dva "))

result = a if a > b else (b if b > a else "числа равны")
print(result)