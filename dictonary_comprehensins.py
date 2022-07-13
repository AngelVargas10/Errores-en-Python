def run():

    my_dici = {i:i**3 for i in range(1,100) if i % 3 !=0}
    my_dic = {i:i**0.5 for i in range(1,1000)}

    #todo esto se puede hacer en una linea
    # dictonary = {}
    # for i in  range(1,100):
    #     if i % 3 != 0 :
    #       dictonary[i] =i ** 3

    for key, i in my_dic.items():
        print(key,"--",i)
    
    for key, i in my_dici.items():
        print(key,"--",i)


if __name__ == "__main__":
    run()