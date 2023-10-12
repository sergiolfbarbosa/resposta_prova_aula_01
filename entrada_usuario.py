#CÓDIGO PARA COLETAR DADOS DO USUÁRIO E EXIBIR NA TELA DE FORMA PERSONALIZADA
nome = str(input("Digite seu primeiro nome: "))
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura usando ponto: "))
peso = float(input("Digite seu peso usando ponto: "))
sexo = str(input("Informe seu sexo: Digite Feminio ou Masculino ")).lower()

print(f'Voçê se chama {nome}, do sexo {sexo}, tem {idade} anos de idade, possui {altura} de altura e pesa {peso}Kg.')