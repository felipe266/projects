#EXERCÍCIO 6: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada
num = float(input('Digite um número: ').strip())

dobro = (num*2)
triplo = (num*3)
raiz = (num**(1/2))

print(f'o número {num} tem o dobro {dobro} o triplo {triplo} e raiz {raiz:.3f}')

print('*~~'*20)

#EXERCÍCIO 7: Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média
notas = 0
media = 0
nota = []
while notas <= 1:
    nota.append(float(input(f'digite a {(notas+1)}º nota: ')))
    media += (nota[notas]/2)
    notas += 1
print(f'a 1º nota é {nota[0]} 2º nota é {nota[1]} a média é {media:.3f}')