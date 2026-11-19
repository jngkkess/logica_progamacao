custo_carro = 50
custo_km = 0.15

custo_carro = int(input("Quantos dias o carro foi alugado? "))
custo_km = int(input("Quantos km rodou? "))

total_a_pagar = (custo_carro * 50) + (custo_km * 0.15)

print(f"Total a pagar:  {total_a_pagar:.2f} R$")