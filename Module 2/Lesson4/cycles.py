#Цикла for:

#Цикл for это итерируемый цикл
#Оператор цикла
#V    V условие для итератора

def main():

    a = [1,2,3,4,5,6,7,8]
    b = 0
    for i in a:
        if i == 5:
            continue
        b +=i
        a = [1,2,3,4,5,6,7,8]



        
    b = 0
    while b<len(a):
        
        print(a[b])
        b+=1
    else:
        print("Finished on "+str(b))
    
    print(b)
if __name__ == "__main__":
    main()

    