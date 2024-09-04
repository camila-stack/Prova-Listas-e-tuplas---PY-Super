lista = []
pares = []
impares = []

for i in range (10):
    numero = int(input("Digite um número: "))
    lista.append(numero)

    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

tupla_impares = tuple(impares)

quantidade_pares = len(pares)
quantidade_impares = len(impares)

soma_pares = sum(pares)
soma_impares = sum(impares)

print("Informações")
print()
print(f"Números pares: {pares}")
print(f"Números ímpares: {tupla_impares}")
print(f"Quantidade de números pares: {quantidade_pares}")
print(f"Quantidade de números ímpares: {quantidade_impares}")
print(f"Soma dos números pares: {soma_pares}")
print(f"Soma dos números ímpares: {soma_impares}")
