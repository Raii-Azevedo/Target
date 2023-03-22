import json
# PS. Para informar o menor valor faturado, ignorei os dias com valores zerados.


def main():
    with open('dados.json') as file:
        dados = json.load(file)
    #A = analise(dados)

    menor = min(dados['valor'])
    print(f"Menor valor de faturamento: R${menor:.2f}")


if __name__ == '__main__':
    main()