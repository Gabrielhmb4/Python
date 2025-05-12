from main import analisar_lista

numeros = [10, 23, 5, 8, 12, 33, 42, 7, 19, 28, 3, 16, 9, 50, 21]
maior, media, pares, menor = analisar_lista(numeros)

print(f"Maior número: {maior}")
print(f"Média: {media}")
print(f"Quantidade de números pares: {pares}")
print(f"Menor número: {menor}")
