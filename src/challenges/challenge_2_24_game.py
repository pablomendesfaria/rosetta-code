from itertools import permutations, product


def solve24(num_str: str) -> str:
    """
    O Jogo 24 testa a aritmética mental de uma pessoa.
    O objetivo do jogo é organizar quatro números de forma que, quando avaliados, o resultado seja 24.
    Exemplo: solve24("4878") deve retornar (7-8/8)*4, 4*(7-8/8) ou uma string válida semelhante.
    
    Args:
        num_str (str): Números a serem avaliados.

    Returns:
        str: String com a expressão que resulta em 24 ou "Sem solução" caso não haja solução.
    """
    if len(num_str) != 4:
        return "Sem solução"

    all_num_combinations = permutations([int(i) for i in num_str])
    all_op_combinations = list(product(["+", "-", "*", "/"], repeat=3))
    templates = [
        "(({}{}{}){}{}){}{}",
        "({}{}{}){}({}{}{})",
        "({}{}({}{}{})){}{}",
        "{}{}({}{}({}{}{}))",
        "{}{}(({}{}{}){}{})"
    ]

    for num_comb in all_num_combinations:
        for op_comb in all_op_combinations:
            for template in templates:
                expression = template.format(num_comb[0], op_comb[0], num_comb[1], op_comb[1], num_comb[2], op_comb[2], num_comb[3])
                try:
                    if eval(expression) == 24:
                        return expression
                except ZeroDivisionError:
                    pass
    return "Sem solução"


print(solve24("4878"))  # (7-8/8)*4 ou 4*(7-8/8) ou qualquer outra string válida
print(solve24("1234"))  # 1*2*3*4
print(solve24("6789"))  # (6*8)/(9-7), (8*6)/(9-7) ou qualquer outra string válida
print(solve24("1127"))  # (1+7)*(1+2) ou qualquer outra string válida
