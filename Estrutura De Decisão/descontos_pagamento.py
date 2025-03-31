valor_hora = float(input("Informe o valor da sua hora de trabalho: "))
horas_trabalhadas = float(input("Informe a quantidade de horas trabalhadas no mês: "))

salario_bruto = valor_hora * horas_trabalhadas

if salario_bruto <= 900:
    ir = 0
elif salario_bruto <= 1500:
    ir = salario_bruto * 0.05
elif salario_bruto <= 2500:
    ir = salario_bruto * 0.10
else:
    ir = salario_bruto * 0.20

sindicato = salario_bruto * 0.03

fgts = salario_bruto * 0.11

descontos = ir + sindicato
salario_liquido = salario_bruto - descontos

if ir == 0:
    ir_percentual = "Isento"
else:
    ir_percentual = f"{(ir / salario_bruto) * 100:.0f}%"

print(f"Salário Bruto:\t\t\t: R$ {salario_bruto:.2f}")
print(f"(-) IR ({ir_percentual}):\t\t\t: R$ {ir:.2f}")
print(f"(-) Sindicato (3%)\t\t: R$ {sindicato:.2f}")
print(f"FGTS (11%)\t\t\t: R$ {fgts:.2f}")
print(f"Total de descontos\t\t: R$ {descontos:.2f}")
print(f"Salário Líquido\t\t\t: R$ {salario_liquido:.2f}")
