custo_carro_dia = 60
custo_km_rodado = 0.15


dias_alugado = int(input("Por quantos dias você alugou o carro? "))
kms_rodados = float(input("Quantos Kms você rodou? "))

total_a_pagar = (dias_alugado * custo_carro_dia) + (kms_rodados * custo_km_rodado)

print(f"Você deve pagar R$ {total_a_pagar}")