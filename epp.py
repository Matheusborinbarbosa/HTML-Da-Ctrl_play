nome = "Pedro "
idade = 17
carteira = True

if idade >= 18 and carteira == True:
    print("você pode dirigir!")
elif idade < 18 and carteira == True:
    print ("você e menor de idade não tem como ter carteira")
elif idade < 18 :
    print("você e menor de idade")
    
elif idade <= 18 and carteira == False:
    print("você precisa tirar a sua carteira")
else :
    print("você não pode dirigir!")