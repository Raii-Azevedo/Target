def fibonacci(v):
    fibo = [0, 1] # Lista começando com 0 e 1 para a sequência fibonacci.
    while fibo[-1] < v:  # Enquanto a últma posição for menor que V
        fibo.append(fibo[-1] + fibo[-2]) #Adicionar a última posição somado a penúltima.
    return fibo


def main():
    print('SEQUENCIA FIBONACCI\n')
    valor = int(input('Informe o valor: '))

    F = fibonacci(valor)

    if valor in F: # Percorrer F que retorna a lista fibo
        print(f"O {valor} pertence à sequência de Fibonacci.")
    else:
        print(f"O {valor} NÃO pertence à sequência de Fibonacci.")


if __name__ == '__main__':
    main()