from datetime import datetime, timedelta

print("\nAutPac v1")
print("===========================")
print()


def ajustar_fim_semana(data):
    while data.weekday() >= 5:
        data += timedelta(days=1)
    return data


def calcular(parcelas, base="hoje"):
    if base == "ontem":
        data_base = datetime.now().date() - timedelta(days=1)
    else:
        data_base = datetime.now().date()

    resultados = []

    for dias in parcelas:
        if dias <= 0:
            print(f"⚠ Prazo inválido ignorado: {dias}")
            continue
        data = data_base + timedelta(days=dias)
        data = ajustar_fim_semana(data)
        resultados.append(f"{dias} dias -> {data.strftime('%d/%m/%Y')}")

    return resultados


def main():
    try:
        entrada = input("Digite os prazos (ex: 28/35/42): ").strip()

        if not entrada:
            print("⚠ Nenhum valor digitado.")
            return

        prazos = [int(x.strip()) for x in entrada.split("/")]

        for r in calcular(prazos):
            print(r)

    except ValueError:
        print("⚠ Digite apenas números separados por /")


if __name__ == "__main__":

    while True:
        main()
        opcao = input("\nDeseja calcular novamente? (s/n): ").lower()

        if opcao != "s":
            print("Encerrando programa...")
            break