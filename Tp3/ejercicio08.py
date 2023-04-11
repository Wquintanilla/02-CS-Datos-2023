'''
• pedir al usuario que ingrese una palabra.
• utiliza user_word = user_word.upper() 
para convertir la palabra ingresada por el usuario a mayúsculas.
• utiliza la ejecución condicional y la instrucción continue para "devorar" 
las siguientes vocales A,E, I, O, U de la palabra ingresada.
• imprime las letras no consumidas en la pantalla, cada una de ellas en una línea separada'''
user_word=input("Ingrese una palabra")
user_word = user_word.upper()
for i in range(len(user_word)):
    if user_word[i] in "AEIOU":
        continue
    print(user_word[i])