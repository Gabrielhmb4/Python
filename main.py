def analisar_lista(numeros):
    
    if not numeros:
        return "A lista está vazia."

    maior = max(numeros)
    media = sum(numeros) / len(numeros)
    pares = sum(1 for numero in numeros if numero % 2 == 0)
    menor = min(numeros)

    return maior, media, pares, menor
