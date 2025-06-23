nome = str(input("Digite seu Nome: "))
idade = int(input("Digite a idade: "))
print(nome)
print(idade)

if idade > 17:
    print("Você pode entrar na festa!")
else:
    print("Você nao pode entrar na festa")

with open("base_dados.csv", "a") as arquivo:
    arquivo.write(f"Seja bem vindo(a) {nome}.\n")