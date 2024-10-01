# Solicite ao usuário que insira o nome de até 7 convidados.
# Armazene os nomes em uma lista.
# Permita ao usuário remover um convidado da lista, caso necessário.
# Exiba a lista final de convidados.
from time import sleep
convidados = []

for i in range(1, 8):
    nomes = str(input(f"escreva o nome do convidado {i}: ")).strip()
    convidados.append(nomes)

remover = str(input("deseja remover um nome da lista? (sim/não): ")).strip()

if remover.upper() == "SIM":
    nomeRemovido = input('Digite o nome que desejas remover: ')
    convidados.remove(nomeRemovido)
else:
    print("Tudo certo!")
    sleep(0.5)
print(f"A lista de convidados está finalizada:\n{convidados}")
