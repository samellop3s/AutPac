from datetime import datetime, timedelta

def ajustar_fim_semana(data):
    if data.weekday() == 5: #sabado
        data += timedelta(days=2)
    elif data.weekday() == 6: #domingo
        data += timedelta(days=2)
    return data

def calcular(parcelas, base="hoje"):

    if base == "ontem":
        data_base = datetime.now() - timedelta(days=1)
    else:
        data_base = datetime.now()
    resultados = []

    for dias in parcelas:
        data = data_base + timedelta(days=dias)
        data = ajustar_fim_semana(data)
        resultados.append(f"{dias} dias -> {data.strftime('%d/%m/%Y')}")
    return resultados
    
entrada = input("Digite os prazos do parcelamento: ")
prazos = [int(x) for x in entrada.split("/")]

for r in calcular(prazos):
        print(r)

