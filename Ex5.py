def reverso(frase):
    inverso = frase[::-1]

    return inverso


def main():
    frase = input('Digite uma frase para ver seu reverso: ')

    print(f'A frase "{frase.upper()}" ao inverso fica: "{reverso(frase).upper()}"')


if __name__ == '__main__':
    main()