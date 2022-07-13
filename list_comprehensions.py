def run():
    # squares =[i**2 for i in range(1,101) if i % 3 != 0]
    # print(squares)

    mul = [i for i in range(1,10000) if i%6==0 and i%9==0 and i%4==0]
    print(mul)
    #con esa misma linea podemos hacer lo mismo que en la de abajo
    # for i in range(1,101):
    #     if i % 3 != 0:
    #      print(i**2)

    # limite = 100 
    # contador = 0

    # while limite > contador:
    #     contador += 1
    #     if i % 3 != 0:
    #      print(contador**2)

    # squares = []
    # for i in range(1,101):
    #     if i % 3 != 0:
    #      squares.append(i**2)
    
    # print(squares)
    

if __name__ == "__main__":
    run()
