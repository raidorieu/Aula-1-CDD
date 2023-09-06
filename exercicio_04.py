nome=input("qual é o seu nome? ")
idade=input("qual a sua idade? ")
sal=float(input("quanto você recebe? "))

print(f"CONFIRMAÇÃO DE DADOS - seu nome é:  {nome} você tem {idade} e o seu salário é de: {sal}")

#aumento
aumento=float(input("seu aumento quantos porcento? "))
novosal=(sal*aumento/100)+sal
print(f"logo, seu acréscimo de {aumento} faria seu novo salário vai ser de {novosal} reais")

#filhos
filhos=float(input("quantos filhos? "))
abono=novosal+(filhos*150)
print(f"com o abono seu salário fica"
      f" {abono}")

#férias
ferias=(sal*30/100)
print(f"seu bonus de férias é de {ferias}. ")

#imposto de renda
imposto=novosal-(novosal*15/100)
inss=imposto-(novosal*8/100)
print(f"retirando o imposto de renda, seu sal fica: {imposto}, depois retiranso o inss também, fica {inss}")

#tudo
tudo=novosal+ferias+abono-imposto-inss
print(f"salário total, com o aumento, abono, férias e retirando o imposto de renda fica {tudo}")