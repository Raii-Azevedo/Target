def reverso(frase):
    inverso = frase[::-1] # Percorrer :: do começo ao final começando da posição [-1 = Última]

    return inverso


def main():
    frase = input('Digite uma frase para ver seu inverso: ')

    print(f'A frase "{frase.upper()}" ao inverso fica: "{reverso(frase).upper()}"') # Upper()  -> Função mmaiúsculo


if __name__ == '__main__':
    main()