
def forca(erros,nome,vit,der) :

    if erros == 0 :

        #print ()
        print ("|----- ")
        print ("|    | ")
        print ("|      ")
        print ("|      ")
        print ("|      ")
        print ("|      ")
        print ("_      ")
        print ()

    elif erros == 1 :

      #  print ()
        print ("|----- ")
        print ("|    | ")
        print ("|    O ")
        print ("|      ")
        print ("|      ")
        print ("|      ")
        print ("_      ")
        print ()

    elif erros == 2 :

      #  print ()
        print ("|----- ")
        print ("|    | ")
        print ("|    O ")
        print ("|    | ")
        print ("|    |  ")
        print ("|      ")
        print ("_      ")
        print ()

    elif erros == 3:

      #  print ()
        print ("|----- ")
        print ("|    | ")
        print ("|    O ")
        print ("|   /| ")
        print ("|    |  ")
        print ("|      ")
        print ("_      ")
        print ()

    elif erros == 4:

      #  print ()
        print ("|----- ")
        print ("|    | ")
        print ("|    O ")
        print ("|   /|\ ")
        print ("|    |  ")
        print ("|      ")
        print ("_      ")
        print ()

    elif erros == 5:

      #  print ()
        print ("|----- ")
        print ("|    | ")
        print ("|    O ")
        print ("|   /|\ ")
        print ("|    |  ")
        print ("|   /   ")
        print ("_      ")
        print ()

    elif erros == 6 :

      #  print ()
        print ("|----- ")
        print ("|    | ")
        print ("|    O ")
        print ("|   /|\ ")
        print ("|    | ")
        print ("|   / \ ")
        print ("_      ")
        print ('Não foi dessa vez :(')
        print ()

def inicio():
    x = 'FORCA'
    print ('-=-' * 10)
    print ('{:^30}'.format (x))
    print ('-=-' * 10)
