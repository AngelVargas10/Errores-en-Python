def run ():

    my_list = [1 , "mi lista","hola",True,False,4.5]
    my_dic = {"hola me la pelan ":1,
    "me la pelan ":2,
    }

    firt_list = [
    {"hola me la pelan ":17, "me la pelan ":2, },
    {"hola me la pelan ":12, "me la  ":4, },
    {"hola me la pelan ":13, "me pelan ":5, },
    {"hola me la pelan ":15, "la pelan ":6, },
    {"hola me la pelan ":14, "me la cd fire pelan ":8, },
    {"hola me la pelan ":13, "me la pelan garcia  ":9, },
    {"hola me la pelan ":31, "me la pelan jasna":7, },
    {"hola me la pelan ":14, "me la pelan  hola":34, },

    ] 

    super_dic = {
        "primera lista " :[1 , "mi listfasea","hola",True,False,4.532423234234],
         "segunda lista":[1 , "mi listadfdsaf","hola",True,False,4.55324],
        "tercera lista":[1 , "mi lisdsfasta","hola",True,False,4.55432],
         "cuarta lista ":[1 , "mi lisvvasddta","hola",True,False,4.4325],
        "quinta lista ":[1 , "mi lista","hola",True,False,4.543245234],


    }

    for key, i in super_dic.items():
        print(key, "-" , i)

#i es el iterador : el cual se va remplazar por los que se vaya imprimir 
#key es igual a laforma en la cual los podemos envocar es como su indice es lo primero del dic
#super_dic.items() es la forma de acededer a lo que hay dentro de los diccionarios 

    for i in firt_list:
        print(i)

if __name__ == "__main__":
    run()