def fatorial(n, show=False):
    """
    -> Calcula o Fatorial de um Número:
    :para n: O número a ser calculado
    :para show: mostra ou não a conta
    :return: O valor fatorial de um número n.
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


print(fatorial(5, show=True))


