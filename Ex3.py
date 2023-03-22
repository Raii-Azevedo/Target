import json

def main():
    with open('dados.json') as file:
        dados = json.load(file)

    print(dados)
if __name__ == '__main__':
    main()