from datetime import datetime, timedelta

def ajustar_fim_semana(data): #aq vai ser feito a analise dos dias para deixar retrito aos fins de semana
    if data.weekday() == 5: #sabado
        data += timedelta(days=2)
    elif data.weekday() == 6: #domingo
        data += timedelta(days=2)
    return data

def calcular(parcelas, base="hoje"): #aqui sera feito o calculo com a base do dia solicitado pelo usuario

    if base == "ontem":
        data_base = datetime.now() - timedelta(days=1)
    else:
        data_base = datetime.now()
    resultados = []

    for dias in parcelas:
        data = data_base + timedelta(days=dias) #e por fim, mostra o resultado com um print no console
        data = ajustar_fim_semana(data)
        resultados.append(f"{dias} dias -> {data.strftime('%d/%m/%Y')}")
    return resultados

def main():
    try:
        entrada = input("Digite os prazos do parcelamento (ex: 28/35/42): ").strip()

        if not entrada:
            print("⚠ Nenhum valor digitado.")
            return

        prazos = [int(x) for x in entrada.split("/")]

        for r in calcular(prazos):
            print(r)

    except ValueError:
        print("⚠ Digite apenas números separados por /")