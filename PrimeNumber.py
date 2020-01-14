a = 10000
while(1):
    i = 2
    while(a%i != 0):
        if a//2 == i:
            print(a)
            break   
        i += 1
    a += 1
