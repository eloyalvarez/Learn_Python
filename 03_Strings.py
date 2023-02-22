### Operadores Aritmeticos ###

my_string = "Mi string"
my_other_string = "Mi otro string"

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string)

my_new_line_string = "Este es un String\ncon salto de línea"
print(my_new_line_string)

my_tab_string = "\tEste es un String con tabulacion"
print(my_tab_string)

my_scape_string = "\\tEste es un String \\n con escapado"
print(my_scape_string)

###FORMATEO###

name, surname, age = "Eloy", "Alvarez", 24


print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print("Mi nombre es %s %s y mi edad es %d" %(name, surname, age))
print(f"Mi nombre es {name} {surname} y mi edad es {age}")


### desempaquetado de caracteres ###
language = "123456"
a, b, c, d, e, f = language

print(a)
print(b)
