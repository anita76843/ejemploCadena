#string concatenar
text1 ="fundamentos con "
text2 = "Python"
#test3 = 5
result = text1 + text2
print (result)

name = "ana"
lastName =" lopez"
fullName = name + "" +lastName
print(fullName)

#format strimg
price = 97
text3 =f"the price is {price:.2f} dollars"
print(text3)

#math operation
text4 = f"la multiplicacion es {20*59}"
print(text4)

#string capitalize
text5 = "python es un lenguaje de alto nivel de programacion"
result1 =text5.capitalize()
print(result1)

#string casefold()
title ="Cien Años De Soledad"
titleConvert = title.casefold()
print(titleConvert)

#string center()
fruit ="banana"
textCenter = fruit.center(20, "-")
print(textCenter)

#string count()
title1 = "i love apple, apple are my favorite fruit"
result2 = title1.count("apple")
print(result2)

#string endswith()
text6 ="Curso, fundamentos con python."
result3 = text6.endswith(".")
print(result3)

#string expandtabs()
letter ="F\tU\tP"
letterSpace = letter.expandtabs(2)
print(letterSpace)

#string find}
text7 = "Hola, bienvenidos a colombia"
result4 =text7.find("bienvenidos")
print(result4)

#funcion title
text8 = "welcome  to my word"
result5 = text8.title()
print(result5)

#funcion isalnum
alphanumeric ="python312"
result6 = alphanumeric.isalnum()
print(result6)

#funcion isalpha
letters = "Space X"
result7= letters.isalpha()
print(result7)