def fibonacci(v):
    fibo = [0, 1] 
    while fibo[-1] < v:  
        fibo.append(fibo[-1] + fibo[-2])
    return fibo


def main():
    print('SEQUENCIA FIBONACCI\n')
    valor = int(input('Informe o valor: '))

    F = fibonacci(valor)

    if valor in F:
        print(f"O {valor} pertence à sequência de Fibonacci.")
    else:
        print(f"O {valor} NÃO pertence à sequência de Fibonacci.")


if __name__ == '__main__':
    main()