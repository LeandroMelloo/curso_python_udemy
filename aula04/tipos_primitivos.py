"""
Tipos de dados
str = string = 'Assim' ou "Assim"
int = inteiro = 1234 ou -12 ou 10 ou 333
float = real/ponto flutuante = -89.10 ou 12.99 ou 0.0
bool = booleano/lógico = True ou False => 10 == 10 => True
type = retorna o tipo do dado
"""
print("Leandro")
print(type("Leandro"))
print(123456)
print(type(123456))
print(23.99)
print(type(23.99))
print(10 == 10)
print(10 == 12)
print('L' == 'L')
print('L' == 'l')
print(bool(''))
print(bool([]))
print(bool(0))
print(bool('1'))
print(bool([1]))
print(bool(1))
print(type(True))
print('10', type('10'), type(int('10')))
print('10.99', type('10.99'), float('10.99'), type(float('10.99')))