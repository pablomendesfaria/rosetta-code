def get_final_opened_doors(num_doors):
    """
    Calcula as portas que estarão abertas ao final do processo.
    Matematicamente falando, as portas que estarão abertas são as portas que possuem um número ímpar de divisores.
    E sabemos que um número tem um número ímpar de divisores se ele for um quadrado perfeito.
    Portanto, as portas que estarão abertas são as portas que são quadrados perfeitos.
    Para calcular os quadrados perfeitos, basta calcular o quadrado de todos os números de 1 até a raiz quadrada do número de portas.

    Args:
        num_doors (int): Número de portas.

    Returns:
        list: Lista com as portas que estarão abertas.
    """
    return [i * i for i in range(1, int(num_doors ** 0.5) + 1)]


print(get_final_opened_doors(100))
