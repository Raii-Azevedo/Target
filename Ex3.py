import json

def main():
    with open('dados.json') as file:
        dados = json.load(file)

    print(dados)

    for dia, valor in dados:
        menor = sum(dados.valor.items())
        print(f'O menor valor faturado foi: R${menor:.2f}')

if __name__ == '__main__':
    main()