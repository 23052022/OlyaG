x = int(input("Kids 1 group: "))
result  = x // 2 + x %2
b= result
print("First group beds: ", result)

y = int(input("Kids 2 group: "))
result  = y // 2 + y %2
a=result
print("Second group beds: ", result)

result = (a+b)
print ("Total beds ", result)