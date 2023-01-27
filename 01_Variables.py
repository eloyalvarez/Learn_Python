# Variables 

my__string_variable = "My String Variable"
print(my__string_variable)

my_int_variable = 5
print(my_int_variable)

#Transformación de un tipo a otro
my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))


my_bool_variable = False
print(my_bool_variable)


# Concatenación de variables en un print
print(my__string_variable, my_int_to_str_variable, my_bool_variable)
print("Este es el valor de:",my_bool_variable) #"Este es el valor de: False"

# Funciones del sistema 
print(len(my__string_variable)) # (18) cuenta carácteres con espacios

# Variables en una sola línea ()
name, surname, alias, age = "Eloy", "Alvarez", "Malon", 24
print("Me llamo:", name, surname, ". Mi edad es:", age, ". Y mi alias es:", alias)

# name = input('Cual es tu nombre? ')
# age = input('Cuantos años tienes? ')
# print(name)
# print(age) 

name = 24
age = "Eloy"

#Cambiamos su tipo
print(name)
print(age)

# ¿Forzamos el tipo? 
address: str = "Mi direccion"
address = 32

print(type(address))
