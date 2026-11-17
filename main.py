salario = float(input("salario atual: R$"))

if salario > 1250:
    aumento = salario * 0.10
else:
    aumento = salario * 0.15

    novo_salario = salario + aumento
    print(f"Novo salario: R${novo_salario:.2f}")