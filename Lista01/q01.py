velocidade = int(input("Digite a velocidade de download em Mbps: "))

if velocidade < 10:
    print("Velocidade Lenta")
if velocidade >= 10 and velocidade <= 100:
    print("Velocidade normal")
if velocidade > 100:
    print("Velocidade rápida")      
    
print("Velocidade de download:", velocidade, "Mbps")    
