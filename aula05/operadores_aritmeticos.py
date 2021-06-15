"""
+ = soma
- = subtração
* = multiplicação
/ = divisão
// = divisão inteira
** = exponenciação ou potenciação
% = resto da divisão
() = parenteses
"""

print('Soma entre 10 + 10 =', 10 + 10)
print('Subtracao entre 10 - 10 =', 10 - 10)
print('Multiplicacao entre 10 * 10 =', 10 * 10)
print('Divisao entre 10 / 10 =', 10 / 10)
print('Divisao inteira 10 // 10 =', 10 // 10)
print('Exponenciacao entre 10 ** 10 =', 10 ** 10)
print('Resto da divisao entre 10 % 10 =', 10 % 10)
print('Parenteses entre 10 + (10 / 10 * 10) =', 10 + (10 / 10 * 10))
print('Precedencia entre 5 + 2 * 10 =', 5 + 2 * 10) # resolve primeiro 2 * 10 e depois soma com o numero 5
print('Precedencia entre (5 + 2) * 10 =', (5 + 2) * 10) # resolve primeiro (5 + 2) e depois multiplica com o numero 10
print('Leandro' + ' ' + 'Mello' + ' ' + 'ele tem' + ' ' + str(35) + ' ' + 'anos', end='.') # sinal de + faz concatenação