vt = float (input(print("Valor total: ")))
dc = float (input(print("Desconto: ")))

dc = dc / 100
vtcdc = vt - (dc * vt)

print(f"Valor com desconto: {vtcdc}")