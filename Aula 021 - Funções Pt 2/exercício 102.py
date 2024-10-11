def fatorial(n, show = False):
    """
    -> Calcular Fatorial do número:
        n = o número a ter o fatorial calculado
        show = True mostra o calculo e False mostra apenas o resultado final
    """
    f = 1
    for c in range(n, 0, -1):
        if show == True:
            if c > 1:
                print(f'{c} x ', end="")
            else:
                print(f'{c} = ', end="")
        f *= c         
    return f

print(fatorial(5, show=False))

help(fatorial)