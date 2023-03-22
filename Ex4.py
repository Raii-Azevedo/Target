def main():
    faturamentoUF = {
        'SP': 67836.43,
        'RJ': 36678.66,
        'MG': 29229.88,
        'ES': 27165.48,
        'Outros': 19849.53
    } # Dicionário com chave UF e Valores.

    total = sum(faturamentoUF.values()) # Soma de todos os valores do DICT faturamento UF
    
    print(f'Total de todos os faturamentos: R${total:.2f}\n')
    
    print('A porcentagem de cada estado é: ')

    for UF, faturamento in faturamentoUF.items():
        percentual = faturamento / total * 100
        print(f'{UF}: {percentual:.2f}%')

if __name__ == '__main__':
    main()