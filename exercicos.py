'''num1 = int(input("Insira um número"))
num2 = int(input("Insira um número"))
def media (num1, num2):
    return (num1 + num2)/2

resultado = media(num1, num2)
print("Resultado", resultado)'''

#ex4.1

'''def saudar(nome ):
    mensage= f"Bom dia,{nome}!"
    return mensage

resultado = saudar("Fulano")
print(resultado)'''

#ex4.2
'''num1 = int(input("Insira uma número"))
num2 = int(input("Insira uma número"))
def calcular(num1,num2):
    return num1 / num2

resultado = calcular(num1,num2)
print("resultado",resultado)'''


#ex 4.3
'''
Email = input("insira o email")

 
def validar_email(Email):
    ponto = False 
    arroba = False
    for leter in Email:
        print ( "Leter atual:",leter,",Válido ponto:", leter == '.' ,",Válido @:", leter == '@')
        if leter == ".":
            ponto = True  
        if leter == "@":
            arroba = True

    if arroba and ponto:
       return True 
    else:
       return False  



resposta = validar_email(Email)
print("Resposta:", resposta)'''
    
#ex 4.7


