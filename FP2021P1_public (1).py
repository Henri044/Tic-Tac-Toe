"""
FP2020/2021 @ IST - Projeto 1 - Jogo do Galo


Este primeiro projecto de Fundamentos da Programacao consiste em implelmentar as
funcoes que permitem a um jogador humano jogar o Jogo do Galo contra o computador de acordo com o enunciado.

Alberto Abad
alberto.abad@tecnico.ulisboa.pt
"""


def eh_tabuleiro(tab):
    """Reconhece tabuleiro.

    :param tab: universal
    :return: bool

    Recebe um argumento de qualquer tipo e devolve True se o seu argumento
    corresponde a um tabuleiro e False caso contrario. Exemplo de uso:

    >>> tab = ((1,0,0),(-1,1,0),(1,-1,-1))
    >>> eh_tabuleiro(tab)
    True
    >>> tab = ((1,0,0),('O',1,0),(1,-1,-1))
    >>> eh_tabuleiro(tab)
    False
    >>> tab = ((1,0,0),(-1,1,0),(1,-1))
    >>> eh_tabuleiro(tab)
    False
    """
    return isinstance(tab, tuple) and \
           len(tab) == 3 and \
           all(isinstance(row, tuple) and len(row) == 3 for row in tab) and \
           all(type(p) == int for row in tab for p in row) and \
           all(p in (1, 0, -1) for row in tab for p in row)


def eh_posicao(p):
    """Reconhece posicao.

    :param p: universal
    :return: bool

    Recebe um argumento de qualquer tipo e devolve True se o seu argumento corresponde a uma posicao
    e False caso contrario. Exemplo:

    >>> eh_posicao(9)
    True
    >>> eh_posicao(-2)
    False
    >>> eh_posicao((1,))
    False
    """
    return (type(p) == int) and (1 <= p <= 9)


def eh_jogador(jog):
    """Reconhece jogador.

    :param jog: univeral
    :return: bool

    Recebe um argumento de qualquer tipo e devolve True se o seu argumento
    corresponde a um jogador 1 ou -1 e False caso contrario.
    """
    return type(jog) == int and jog in (1, -1)


def eh_estrategia(estrategia):
    """Reconhece estrategia.

    :param estrategia: univeral
    :return: bool

    Recebe um argumento de qualquer tipo e devolve True se o seu argumento
    corresponde a uma estrategia de jogo valida e False caso contrario.
    """

    return estrategia in ('basico', 'normal', 'perfeito')


def pos_to_coord(p):
    """
    Converte posicao para coordenada.

    :param p: posicao
    :return:  tuple

    Funcao auxiliar que recebe uma posicao e converte para coordenada

    """
    return (p - 1) // 3, (p - 1) % 3


def obter_coluna(tab, n):
    """
    Devolve coluna.

    :param tab: tabuleiro
    :param n: int
    :return:  tuple

    Recebe um tabuleiro e um inteiro com valor de 1 a 3 que representa o numero da coluna,
    e devolve um vector com os valores dessa coluna. Se algum dos argumentos dados forem invalidos,
    a funcao gera um erro. Exemplo:


    >>> tab = ((1,-1,0),(1,0,-1),(1,-1,0))
    >>> obter_coluna(tab, 2)
    (-1, 0, -1)
    >>> obter_coluna(tab, 1)
    (1, 1, 1)
    >>> obter_coluna(tab, 4)
    Traceback (most recent call last):
    ...
    ValueError: obter_coluna: algum dos argumentos e invalido
    """
    if eh_tabuleiro(tab) and (type(n) == int and 1 <= n <= 3):
        return tuple(tab[row][n - 1] for row in range(3))
    raise ValueError('obter_coluna: algum dos argumentos e invalido')


def obter_linha(tab, n):
    """
    Devolve linha.

    :param tab: tabuleiro
    :param n: int
    :return:  tuple

    Recebe um tabuleiro e um inteiro com valor de 1 a 3 que representa o numero da linha,
    e devolve um vector com os valores dessa linha. Se algum dos argumentos dados forem invalidos,
    a funcao gera um erro. Exemplo:

    >>> tab = ((1,-1,0),(1,0,-1),(1,-1,0))
    >>> obter_linha(tab, 2)
    (1, 0, -1)
    >>> obter_linha(tab, 1)
    (1, -1, 0)
    >>> obter_linha(tab, 4)
    Traceback (most recent call last):
    ...
    ValueError: obter_linha: algum dos argumentos e invalido
    """
    if eh_tabuleiro(tab) and (type(n) == int and 1 <= n <= 3):
        return tab[n - 1]
    raise ValueError('obter_linha: algum dos argumentos e invalido')


def obter_diagonal(tab, n):
    """
    Devolve diagonal.

    :param tab: tabuleiro
    :param n: int
    :return:  tuple

    Recebe um tabuleiro e um inteiro que representa a direcao da diagonal, 1 para descendente da esquerda
    para a direita e 2 para ascendente da esquerda para a direita, e devolve um vector com os valores dessa diagonal.
    Se algum dos argumentos dados forem invalidos, a funcao gera um erro. Exemplo:

    >>> tab = ((1,-1,-1),(1,0,-1),(1,-1,0))
    >>> obter_diagonal(tab, 1)
    (1, 0, 0)
    >>> obter_diagonal(tab, 2)
    (1, 0, -1)
    >>> obter_diagonal(tab, 3)
    Traceback (most recent call last):
    ...
    ValueError: obter_diagonal: algum dos argumentos e invalido
    """

    if eh_tabuleiro(tab) and (type(n) == int and n in (1, 2)):
        if n == 1:
            return tuple(tab[i][i] for i in range(3))
        else:
            return tuple(tab[2 - i][i] for i in range(3))

    raise ValueError('obter_diagonal: algum dos argumentos e invalido')


def tabuleiro_str(tab):
    """
    Representacao externa do tabuleiro.

    :param tab: tabuleiro
    :return: str

    Recebe um tabuleiro e devolve a cadeia de caracteres que o representa. Se o argumento dado for invalido,
    a funcao gera um erro. Exemplo:

    >>> tab = ((1,-1,0),(1,0,-1),(1,-1,0))
    >>> tabuleiro_str(tab)
    ' X | O |   \\n-----------\\n X |   | O \\n-----------\\n X | O |   '
    >>> tabuleiro_str((('X','O',' '),('X',' ')))
    Traceback (most recent call last):
        ...
    ValueError: tabuleiro_str: o argumento e invalido
    """
    if eh_tabuleiro(tab):
        n2c = {1: 'X', -1: 'O', 0: ' '}
        string = [n2c[val] for row in tab for val in row]
        return ' {} | {} | {} \n-----------\n {} | {} | {} \n-----------\n {} | {} | {} '.format(*string)
    raise ValueError('tabuleiro_str: o argumento e invalido')


def eh_posicao_livre(tab, p):
    """
    Testa posicao livre.

    :param tab: tabuleiro
    :param p: posicao
    :return:  tuple

    Recebe um tabuleiro e uma posicao, e devolve True se a posicao corresponde a uma posicao livre do tabuleiro
    e False caso contrario.  Se algum dos argumentos dados forem invalidos, a funcao gera um erro. Exemplo:

    >>> tab = ((1,-1,0),(1,-1,0),(1,-1,0))
    >>> eh_posicao_livre(tab, 9)
    True
    >>> eh_posicao_livre(tab, 7)
    False
    >>> eh_posicao_livre(tab, (-1,))
    Traceback (most recent call last):
        ...
    ValueError: eh_posicao_livre: algum dos argumentos e invalido
    """

    if eh_tabuleiro(tab) and eh_posicao(p):
        return tab[pos_to_coord(p)[0]][pos_to_coord(p)[1]] == 0
    raise ValueError('eh_posicao_livre: algum dos argumentos e invalido')


def obter_posicoes_livres(tab):
    """
    Devolve posicoes livres.

    :param tab: tabuleiro
    :return: tuple

    Recebe um tabuleiro, e devolve o vector ordenado com todas as posicoes  livres do tabuleiro. Se o argumento
    dado for invalido, a funcao gera um erro. Exemplo:

    >>> tab = ((1,-1,0),(1,-1,0),(1,-1,0))
    >>> obter_posicoes_livres(tab)
    (3, 6, 9)
    >>> tab = ((1,-1,0),(1,-1,0),(1,-1))
    >>> obter_posicoes_livres(tab)
    Traceback (most recent call last):
        ...
    ValueError: obter_posicoes_livres: o argumento e invalido
    """
    if eh_tabuleiro(tab):
        return tuple(p for p in range(1, 10) if eh_posicao_livre(tab, p))
    raise ValueError("obter_posicoes_livres: o argumento e invalido")


def jogador_ganhador(tab):
    """
    Devolve o jogador ganhador.

    :param tab: tabuleiro
    :return: bool


    Recebe um tabuleiro, e devolve um valor inteiro a indicar o jogador que ganhou a partidao, sendo o valor
    igual a 1 se ganhou o jogador que joga com ’X’, -1 se ganhou o jogador que joga com ’O’, ou 0 se nao
    ganhou nenhum jogador. Se o argumento dado for invalido, a funcao gera um erro. Exemplo:

    >>> tab = ((1,-1,0),(1,0,-1),(0,-1,0))
    >>> jogador_ganhador(tab)
    0
    >>> tab = ((1,-1,0),(1,0,-1),(1,-1,0))
    >>> jogador_ganhador(tab)
    1
    >>> tab = ((1,1,-1),(-1,-1,1),(1,-1,1))
    >>> jogador_ganhador(tab)
    0
    >>> tab = ((1,1,-1),(-1,-1,1),(1,-1))
    >>> jogador_ganhador(tab)
    Traceback (most recent call last):
        ...
    ValueError: jogador_ganhador: o argumento e invalido
    """
    if eh_tabuleiro(tab):
        for jog in (1, -1):
            if any(all(val == jog for val in obter_linha(tab, n)) for n in range(1, 4)) or \
                    any(all(val == jog for val in obter_coluna(tab, n)) for n in range(1, 4)) or \
                    all(val == jog for val in obter_diagonal(tab, 1)) or \
                    all(val == jog for val in obter_diagonal(tab, 2)):
                return jog
        return 0

    raise ValueError('jogador_ganhador: o argumento e invalido')


def eh_fim_jogo(tab):
    """
    Verifica se e fim de jogo.

    :param tab: tabuleiro
    :return: bool


    Recebe um tabuleiro, e verifica se o jogo terminou. Exemplo:

    >>> tab = ((1,-1,0),(1,0,-1),(0,-1,0))
    >>> eh_fim_jogo(tab)
    False
    >>> tab = ((1,-1,0),(1,0,-1),(1,-1,0))
    >>> eh_fim_jogo(tab)
    True
    >>> tab = ((1,1,-1),(-1,-1,1),(1,-1,1))
    >>> eh_fim_jogo(tab)
    True
    >>> eh_fim_jogo(((1,1,-1),(-1,-1,1)))
    Traceback (most recent call last):
    ...
    ValueError: eh_fim_jogo: o argumento e invalido
    """
    if eh_tabuleiro(tab):
        return jogador_ganhador(tab) in (1, -1) or not obter_posicoes_livres(tab)

    raise ValueError('eh_fim_jogo: o argumento e invalido')


def marcar_posicao(tab, jog, p):
    """
    Marca uma posicao no tabuleiro.

    :param tab: tabuleiro
    :param jog: jogador
    :param p: posicao
    :return:  tabuleiro

    Devolve um  tabuleiro modificado com uma nova marca do jogador na posicao argumento. Se algum dos argumentos
    dados forem invalidos, a funcao gera um erro. Exemplo:

    >>> tab = ((1,-1,0),(1,0,-1),(1,-1,0))
    >>> marcar_posicao(tab, -1, 5)
    ((1, -1, 0), (1, -1, -1), (1, -1, 0))
    >>> marcar_posicao(tab, 1, 3)
    ((1, -1, 1), (1, 0, -1), (1, -1, 0))
    >>> marcar_posicao(tab, 1, 1)
    Traceback (most recent call last):
    ...
    ValueError: marcar_posicao: algum dos argumentos e invalido
    """

    if eh_tabuleiro(tab) and eh_posicao(p) and eh_posicao_livre(tab, p) and eh_jogador(jog):
        return tuple(tuple(jog if (i, j) == pos_to_coord(p) else tab[i][j] for j in range(3)) for i in range(3))
    raise ValueError('marcar_posicao: algum dos argumentos e invalido')


def escolher_posicao_manual(tab):
    """
    Leitura da posicao escolhida pelo jogador.

    :param tab: tabuleiro
    :return: posicao

    Esta funcao realiza a leitura de uma posicao introduzida manualmente por um jogador e devolve
    esta posicao escolhida.  Se o argumento dado for invalido, a funcao gera um erro.
    """
    if eh_tabuleiro(tab):
        p = eval(input('Turno do jogador. Escolha uma posicao livre: '))
        if eh_posicao(p) and eh_posicao_livre(tab, p):
            return p
        raise ValueError('escolher_posicao_manual: a posicao introduzida e invalida')

    raise ValueError('escolher_posicao_manual: o argumento e invalido')


def escolher_posicao_auto(table, player, estrategia):
    """
    Seleciona uma posicao de forma automatica.

    :param table: tabuleiro
    :param player: int
    :param estrategia: str
    :return: posicao

    Devolve a posicao escolhida automaticamente de acordo com a estrategia seleccionada. Se algum dos argumentos
    dados forem invalidos, a funcao  gera um erro. Exemplo:

    >>> tab = ((0,0,0),(0,1,0),(-1,0,0))
    >>> escolher_posicao_auto(tab, 1, 'basico')
    1
    >>> tab = ((0,0,0),(0,1,0),(-1,0,0))
    >>> escolher_posicao_auto(tab, 1, 'normal')
    3
    >>> tab = ((0,0,-1),(-1,1,0),(1,0,0))
    >>> escolher_posicao_auto(tab, 1, 'normal')
    1
    >>> tab = ((0,0,-1),(-1,1,0),(1,0,0))
    >>> escolher_posicao_auto(tab, 1, 'perfeito')
    8
    >>> tab = ((0,0,-1),(-1,1,0),(1,0,0))
    >>> escolher_posicao_auto(tab, 'X', 'basico')
    Traceback (most recent call last):
    ...
    ValueError: escolher_posicao_auto: algum dos argumentos e invalido
    """
    def get_win_moves(tab, jog):
        livre = obter_posicoes_livres(tab)
        return tuple(pos for pos in livre if jogador_ganhador(marcar_posicao(tab, jog, pos)) == jog)

    def get_fork_moves(tab, jog):
        livre = obter_posicoes_livres(tab)
        res = ()
        for pos in livre:
            newtab = marcar_posicao(tab, jog, pos)
            if len(get_win_moves(newtab, jog)) > 1:
                res += (pos,)
        return res

    def force_defense_in_fork(tab, jog):
        def two_in_a_row(ntab):
            look = (jog, jog, 0), (jog, 0, jog), (0, jog, jog)
            return any(obter_linha(ntab, n) in look for n in range(1, 4)) \
                   or any(obter_coluna(ntab, n) in look for n in range(1, 4)) \
                   or any(obter_diagonal(ntab, n) in look for n in range(1, 3))
        res = ()
        for pos in obter_posicoes_livres(tab):
            newtab = marcar_posicao(tab, jog, pos)
            if two_in_a_row(newtab) and \
                    get_win_moves(newtab, jog)[0] not in get_fork_moves(newtab, -jog):
                res += (pos,)
        return res

    def rule1(tab, jog):  # win rule
        return get_win_moves(tab, jog)

    def rule2(tab, jog):  # block rule
        return get_win_moves(tab, -jog)

    def rule3(tab, jog):  # fork rule
        return get_fork_moves(tab, jog)

    def rule4(tab, jog):  # block fork rule
        p = get_fork_moves(tab, -jog)
        return p if len(p) <= 1 else force_defense_in_fork(tab, jog)

    def rule5(tab, jog):  # center rule
        return (5,) if eh_posicao_livre(tab, 5) else ()

    def rule6(tab, jog):  # opposite corner rule
        other = -jog
        corner_pairs = ((1, 9), (3, 7), (7, 3), (9, 1))
        res = ()
        for c in corner_pairs:
            x, y = pos_to_coord(c[0])
            if tab[x][y] == other and eh_posicao_livre(tab, c[1]):
                res += (c[1],)

        return tuple(sorted(res))

    def rule7(tab, jog):  # corner rule
        corners = (1, 3, 7, 9)
        return tuple(pos for pos in corners if eh_posicao_livre(tab, pos))

    def rule8(tab, jog):  # side rule
        sides = (2, 4, 6, 8)
        return tuple(pos for pos in sides if eh_posicao_livre(tab, pos))

    if eh_tabuleiro(table) and eh_jogador(player) and eh_estrategia(estrategia):

        rules = {'basico': (rule5, rule7, rule8),
                 'normal': (rule1, rule2, rule5, rule6, rule7, rule8),
                 'perfeito': (rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8)}

        for rule in rules[estrategia]:
            candidate = rule(table, player)
            if candidate:
                return candidate[0]

    raise ValueError('escolher_posicao_auto: algum dos argumentos e invalido')


def jogo_do_galo(human, estrategia):
    """
    Funcao principal do jogo do galo

    :param human: str
    :param estrategia: str
    :return: str

    Funcao principal que permite jogar um jogo completo de Jogo do Galo de um jogador contra o computador.
    Recebe duas cadeias de caracteres e devolve o identificador do jogador ganhador ('X' ou 'O').
    Em caso de empate, devolve a cadeia de caracteres 'EMPATE'.
    O primeiro argumento corresponde a marca (’X’ ou ’O’) que deseja utilizar o jogador humano,
    e o segundo argumento selecciona a estrategia de jogo utilizada pela maquina. Se algum dos argumentos forem
    invalidos, a gera um erro.
    """
    if (human in ('X', 'O')) and eh_estrategia(estrategia):

        tab = ((0, 0, 0), (0, 0, 0), (0, 0, 0))
        current_player = 1
        print('Bem-vindo ao JOGO DO GALO.\nO jogador joga com \'{}\'.'.format(human))
        human = 1 if human == 'X' else -1

        while not eh_fim_jogo(tab):
            if human == current_player:
                p = escolher_posicao_manual(tab)
            else:
                print('Turno do computador (', estrategia, '):', sep='')
                p = escolher_posicao_auto(tab, current_player, estrategia)

            tab = marcar_posicao(tab, current_player, p)
            print(tabuleiro_str(tab))
            current_player = -current_player

        if jogador_ganhador(tab) == 1:
            return 'X'
        elif jogador_ganhador(tab) == -1:
            return 'O'
        else:
            return 'EMPATE'

    raise ValueError('jogodogalo:  algum dos argumentos e invalido')
