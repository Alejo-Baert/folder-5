# print("Hola")
# print("ALOJA SOY ALEJOX AJJAX")
for n in range(1, 11):
    d= 0
    for c in range(1, n + 1):
        if n % c == 0:
            d+=1   
    if d <= 2:
        print(n, end=" ")      

                 