def teste_eh_tabuleiro():
    total_score = 125
    fun_name = eh_tabuleiro

    tab = ((0,0,0),(0,0,0),(0,0,0))
    eh_tabuleiro(tab)
    # True

    tab = ((1,1,1),(1,1,1),(1,1,1))
    eh_tabuleiro(tab)
    # True

    tab = ((-1,-1,-1),(0,0,0),(1,1,1))
    eh_tabuleiro(tab)
    # True

    tab = True
    eh_tabuleiro(tab)
    # False

    tab = [(1,0,0),(1,1,0),(1,-1,-1)]
    eh_tabuleiro(tab)
    # False

    tab = ((1,0,0),(-1,1,0),[1,-1,-1])
    eh_tabuleiro(tab)
    # False

    tab = ([1,0,0],[-1,1,0],[1,-1,-1])
    eh_tabuleiro(tab)
    # False

    tab = (1, 0, -1)
    eh_tabuleiro(tab)
    # False

    tab = ((1,0,0),(1,1,0),(1,-1,-1), (1,-1,-1))
    eh_tabuleiro(tab)
    # False

    tab = ((1,0,0,0),(1,1,0,0),(1,-1,-1,0))
    eh_tabuleiro(tab)
    # False

    tab = ((1,False,False),(0,True,False),(-1,True,False))
    eh_tabuleiro(tab)
    # False

    tab = ((1,0,0),(1,1,0),(1,-1,-2))
    eh_tabuleiro(tab)
    # False

    tab = ((1,0,0),(1,1,2),(1,-1,-1))
    eh_tabuleiro(tab)
    # False

    tab = ((1,0,0),(1,1,0),(1,-1,0.0))
    eh_tabuleiro(tab)
    # False

    tab = (('X',' ',' '),('X','X',' '),('X',' ',' '))
    eh_tabuleiro(tab)
    # False

    return


def teste_eh_posicao():
    total_score = 50
    fun_name = eh_posicao

    eh_posicao(5)
    # True

    eh_posicao(5.0)
    # False

    eh_posicao(14)
    # False

    eh_posicao(0)
    # False

    eh_posicao(True)
    # False

    eh_posicao(False)
    # False

    eh_posicao(())
    # False

    eh_posicao([4])
    # False

    return



def teste_obter_coluna():
    total_score = 75
    fun_name = obter_coluna

    tab = ((1,0,-1),(0,0,0),(1,1,1))
    obter_coluna(tab, 1)
    # (1, 0, 1)

    tab = ((1,0,-1),(0,0,0),(-1,1,1))
    obter_coluna(tab, 2)
    # (0, 0, 1)

    tab = ((1,0,-1),(0,0,0),(-1,1,1))
    obter_coluna(tab,3)
    # (-1, 0, 1)

    tab = ((1,-1,0),(1,0,-1),(1,-1,0))
    obter_coluna(tab, 0)
    # obter_coluna: algum dos argumentos e invalido

    tab = ((1,-1,0),(1,0,-1),(1,-1,0))
    obter_coluna(tab, False)
    # obter_coluna: algum dos argumentos e invalido

    obter_coluna((1,1,1), 2)
    # obter_coluna: algum dos argumentos e invalido

    return


def teste_obter_linha():
    total_score = 50
    fun_name = obter_linha

    tab = ((1,0,-1),(0,0,0),(1,1,1))
    obter_linha(tab, 1)
    # (1, 0, -1)

    tab = ((1,0,-1),(0,0,0),(-1,1,1))
    obter_linha(tab, 2)
    # (0, 0, 0)

    tab = ((1,0,-1),(0,0,0),(-1,1,1))
    obter_linha(tab,3)
    # (-1, 1, 1)

    tab = ((1,-1,0),(1,0,-1),(1,-1,0))
    obter_linha(tab, 0)
    # obter_linha: algum dos argumentos e invalido

    tab = ((1,-1,0),(1,0,-1),(1,-1,0))
    obter_linha(tab, True)
    # obter_linha: algum dos argumentos e invalido

    obter_linha([1,1,1], 2)
    # obter_linha: algum dos argumentos e invalido


    return



def teste_obter_diagonal():
    total_score = 75
    fun_name = obter_diagonal

    
    tab = ((1,0,-1),(0,0,0),(-1,1,1))
    obter_diagonal(tab, 1)
    # (1, 0, 1)

    tab = ((1,0,-1),(0,0,0),(-1,1,1))
    obter_diagonal(tab, 2)
    # (-1, 0, -1)

    tab = ((1,-1,-1),(1,0,-1),(1,-1,0))
    obter_diagonal(tab, 0)
    # obter_diagonal: algum dos argumentos e invalido

    tab = ((1,-1,-1),(1,0,-1),(1,-1,0))
    obter_diagonal(tab, True)
    # obter_diagonal: algum dos argumentos e invalido

    tab = ((1,-1,-1),(1,0,-1),(1,-1,0))
    obter_diagonal(tab, False)
    # obter_diagonal: algum dos argumentos e invalido

    obter_diagonal(1, 1)
    # obter_diagonal: algum dos argumentos e invalido

    return



def teste_tabuleiro_str():
    total_score = 125
    fun_name = tabuleiro_str

    tab = ((0,0,0),(0,0,0),(0,0,0))
    tabuleiro_str(tab)
    #    |   |   \\n-----------\\n   |   |   \\n-----------\\n   |   |   
    
    tab = ((1,1,1),(0,0,0),(-1,-1,-1))
    tabuleiro_str(tab)
    #  X | X | X \\n-----------\\n   |   |   \\n-----------\\n O | O | O 


    tab = ((1,0,-1),(1,0,-1),(1,0,-1))
    tabuleiro_str(tab)
    #  X |   | O \\n-----------\\n X |   | O \\n-----------\\n X |   | O 

    tabuleiro_str(False)
    # tabuleiro_str: o argumento e invalido

    tabuleiro_str((1, 0, -1))
    # tabuleiro_str: o argumento e invalido


    return



def teste_eh_posicao_livre():
    total_score =75
    fun_name = eh_posicao_livre

    tab = ((1,1,-1),(1,-1,-1),(1,0,1))
    eh_posicao_livre(tab, 8)
    # True

    tab = ((0,0,0),(1,0,0),(0,0,0))
    eh_posicao_livre(tab, 4)
    # False

    tab = ((1,-1,0),(1,-1,0),(1,-1,0))
    eh_posicao_livre(tab, 0)
    # eh_posicao_livre: algum dos argumentos e invalido

    tab = [(1,-1,0),(1,-1,0),(1,-1,0)]
    eh_posicao_livre(tab, 1)
    # eh_posicao_livre: algum dos argumentos e invalido

    tab = ((1,-1,0),(1,-1,0),(1,-1,0))
    eh_posicao_livre(9, tab)
    # eh_posicao_livre: algum dos argumentos e invalido


    return



def teste_obter_posicoes_livres():
    total_score = 75
    fun_name = obter_posicoes_livres

    tab = ((1, 0, -1), (1, 0, -1), (1, 0, -1))
    obter_posicoes_livres(tab)
    # (2, 5, 8)

    tab = ((1,-1,-1),(1,1,-1),(1,0,-1))
    obter_posicoes_livres(tab)
    # (8,)

    tab = ((1,-1,-1),(1,1,-1),(1,1,-1))
    obter_posicoes_livres(tab)
    # ()

    tab = ((0,0,0),(0,0,0),(0,0,0))
    obter_posicoes_livres(tab)
    # (1, 2, 3, 4, 5, 6, 7, 8, 9)
    
    tab = ((1,-1,0),(1,-1,0),(1,-1, 'O'))
    obter_posicoes_livres(tab)
    # obter_posicoes_livres: o argumento e invalido

    return



def teste_jogador_ganhador():
    total_score = 200
    fun_name = jogador_ganhador

    tab = ((-1,-1,1),(1,1,-1),(1,-1,1))
    jogador_ganhador(tab)
    # 1
    
    tab = ((1,1,1),(-1,-1,1),(0,0,0))
    jogador_ganhador(tab)
    # 1
    
    tab = ((1,-1,1),(-1,-1,1),(0,-1,0))
    jogador_ganhador(tab)
    # -1

    tab = ((1,-1,-1),(1,-1,-1),(-1,1,1))
    jogador_ganhador(tab)
    # -1

    tab = ((1,-1,1),(1,-1,-1),(-1,1,1))
    jogador_ganhador(tab)
    # 0    

    tab = ((0,0,0),(0,0,0),(0,0,0))
    jogador_ganhador(tab)
    # 0

    tab = ((1,1,-1),(-1,-1,1),(1,-1, 1, 1))
    jogador_ganhador(tab)
    # jogador_ganhador: o argumento e invalido

    return


def teste_marcar_posicao():
    total_score = 100
    fun_name = marcar_posicao

    tab = ((0,0,0),(0,0,0),(0,0,0))
    marcar_posicao(tab, -1, 4)
    # ((0, 0, 0), (-1, 0, 0), (0, 0, 0))

    tab = ((0,0,0),(0,0,0),(0,0,0))
    marcar_posicao(tab, 1, 8)
    # ((0, 0, 0), (0, 0, 0), (0, 1, 0))
    
    marcar_posicao((0,0,0), 1, 8)
    # marcar_posicao: algum dos argumentos e invalido

    tab = ((0,0,0),(0,0,0),(0,0,0))
    marcar_posicao(tab, 0, 8)
    # marcar_posicao: algum dos argumentos e invalido

    tab = ((0,0,0),(0,0,0),(0,0,0))
    marcar_posicao(tab, False, 8)
    # marcar_posicao: algum dos argumentos e invalido

    tab = ((0,0,0),(0,0,0),(0,0,0))
    marcar_posicao(tab, True, 8)
    # marcar_posicao: algum dos argumentos e invalido

    tab = ((0,0,0),(0,0,0),(0,0,0))
    marcar_posicao(tab, 1, -5)
    # marcar_posicao: algum dos argumentos e invalido

    tab = ((0,0,0),(0,1,0),(0,0,0))
    marcar_posicao(tab, 1, 5)
    # marcar_posicao: algum dos argumentos e invalido

    return


def teste_escolher_posicao_manual():
    total_score = 50
    fun_name = escolher_posicao_manual


    tab = ((0,1,-1),(1,-1,1),(1,-1,1))
    escolher_posicao_manual_mooshak(tab,'1')
    # Turno do jogador. Escolha uma posicao livre: 1

    tab = ((-1,1,-1),(1,-1,1),(1,-1,0))
    escolher_posicao_manual_mooshak(tab,'9')
    # Turno do jogador. Escolha uma posicao livre: 9

    tab = ((0,0,0),(0,0,0),(0,0,0))
    escolher_posicao_manual_mooshak(tab,'0')
    # Turno do jogador. Escolha uma posicao livre: escolher_posicao_manual: a posicao introduzida e invalida

    tab = ((0,0,0),(0,0,1),(0,0,0))
    escolher_posicao_manual_mooshak(tab,'6')
    # Turno do jogador. Escolha uma posicao livre: escolher_posicao_manual: a posicao introduzida e invalida

    tab = ((0,0,0),(0,0,1))
    escolher_posicao_manual(tab)
    # escolher_posicao_manual: o argumento e invalido

    return


def teste_escolher_posicao_auto():
    total_score = 75
    fun_name = escolher_posicao_auto

    tab = ((0,0,0),(0,0,0),(0,0))
    escolher_posicao_auto(tab, 1, 'basico')
    # escolher_posicao_auto: algum dos argumentos e invalido

    tab = ((0,0,0),(0,0,0),(0,0,0))
    escolher_posicao_auto(tab, 0, 'basico')
    # escolher_posicao_auto: algum dos argumentos e invalido

    tab = ((0,0,0),(0,0,0),(0,0,0))
    escolher_posicao_auto(tab, True, 'basico')
    # escolher_posicao_auto: algum dos argumentos e invalido

    tab = ((0,0,0),(0,0,0),(0,0,0))
    escolher_posicao_auto(tab, -1, 'basic')
    # escolher_posicao_auto: algum dos argumentos e invalido

    tab = ((0,0,0),(0,0,0),(0,0,0))
    escolher_posicao_auto(tab, 'normal', 1)
    # escolher_posicao_auto: algum dos argumentos e invalido

    return


def teste_escolher_posicao_auto_basic():
    total_score = 75
    fun_name = escolher_posicao_auto_basic

    tab = ((0,0,0),(0,0,0),(0,0,0))
    escolher_posicao_auto(tab, 1, 'basico')
    # 5

    tab = ((1,0,0),(0,0,0),(0,0,0))
    escolher_posicao_auto(tab, -1, 'basico')
    # 5

    tab = ((0,0,0),(0,1,0),(0,0,0))
    escolher_posicao_auto(tab, -1, 'basico')
    # 1

    tab = ((1,0,0),(0,-1,0),(0,0,0))
    escolher_posicao_auto(tab, 1, 'basico')
    # 3
    
    tab = ((1,0,1),(0,-1,0),(-1,0,0))
    escolher_posicao_auto(tab, 1, 'basico')
    # 9

    tab = ((1,0,1),(0,1,0),(-1,0,-1))
    escolher_posicao_auto(tab, -1, 'basico')
    # 2

    tab = ((1,-1,1),(0,-1,0),(-1,0,1))
    escolher_posicao_auto(tab, 1, 'basico')
    # 4

    tab = ((1,-1,1),(1,-1,-1),(-1,0,1))
    escolher_posicao_auto(tab, 1, 'basico')
    # 8

    tab = ((0,0,0),(0,-1,1),(1,0,0))
    escolher_posicao_auto(tab, -1, 'basico')
    # 1

    return


def teste_escolher_posicao_auto_normal():
    total_score = 125
    fun_name = escolher_posicao_auto_normal

    tab = ((0,0,0),(0,0,0),(0,0,0))
    escolher_posicao_auto(tab, 1, 'normal')
    # 5

    tab = ((0,1,0),(0,0,0),(0,0,0))
    escolher_posicao_auto(tab, -1, 'normal')
    # 5

    tab = ((0,0,0),(0,1,0),(0,0,0))
    escolher_posicao_auto(tab, -1, 'normal')
    # 1

    tab = ((1,0,0),(0,-1,0),(0,0,0))
    escolher_posicao_auto(tab, 1, 'normal')
    # 3

    tab = ((-1,0,0),(0,1,0),(0,0,0))
    escolher_posicao_auto(tab, 1, 'normal')
    # 9
    
    tab = ((0,0,-1),(0,1,0),(0,0,0))
    escolher_posicao_auto(tab, 1, 'normal')
    # 7

    tab = ((1,0,1),(0,-1,0),(-1,0,0))
    escolher_posicao_auto(tab, 1, 'normal')
    # 2

    tab = ((0,0,1),(0,-1,0),(-1,0,1))
    escolher_posicao_auto(tab, 1, 'normal')
    # 6

    tab = ((1,0,0),(0,1,0),(-1,-1,0))
    escolher_posicao_auto(tab, 1, 'normal')
    # 9

    tab = ((1,0,0),(1,0,0),(0,-1,0))
    escolher_posicao_auto(tab, -1, 'normal')
    # 7

    tab = ((1,0,1),(0,0,0),(0,-1,0))
    escolher_posicao_auto(tab, -1, 'normal')
    # 2

    tab = ((1,-1,1),(0,-1,0),(0,0,0))
    escolher_posicao_auto(tab, 1, 'normal')
    # 8

    tab = ((1,0,1),(0,1,0),(-1,0,-1))
    escolher_posicao_auto(tab, -1, 'normal')
    # 8

    tab = ((1,-1,1),(0,-1,0),(-1,0,1))
    escolher_posicao_auto(tab, 1, 'normal')
    # 6

    tab = ((0,0,0),(0,-1,1),(1,0,0))
    escolher_posicao_auto(tab, -1, 'normal')
    # 3

    tab = ((0,0,0),(0,-1,1),(0,1,0))
    escolher_posicao_auto(tab, -1, 'normal')
    # 1

    return


def teste_escolher_posicao_auto_perfeito():
    total_score = 125
    fun_name = escolher_posicao_auto_perfeito

    tab = ((0,0,0),(0,0,0),(0,1,0))
    escolher_posicao_auto(tab, -1, 'perfeito')
    # 5

    tab = ((1,-1,0),(0,0,0),(0,0,0))
    escolher_posicao_auto(tab, 1, 'perfeito')
    # 5

    tab = ((0,0,0),(0,-1,0),(1,0,0))
    escolher_posicao_auto(tab, 1, 'perfeito')
    # 1


    tab = ((1,0,-1),(0,-1,0),(1,0,0))
    escolher_posicao_auto(tab, 1, 'perfeito')
    # 4


    tab = ((0,0,1),(0,1,0),(0,-1,-1))
    escolher_posicao_auto(tab, 1, 'perfeito')
    # 7

    tab = ((0,-1,0),(0,0,0),(1,0,1))
    escolher_posicao_auto(tab, 1, 'perfeito')
    # 8

    
    tab = ((1,0,0),(-1,-1,0),(1,0,0))
    escolher_posicao_auto(tab, 1, 'perfeito')
    # 6

    tab = ((-1,0,-1),(0,1,0),(1,0,1))
    escolher_posicao_auto(tab, -1, 'perfeito')
    # 2

    tab = ((1,-1,0),(0,1,0),(0,0,-1))
    escolher_posicao_auto(tab, 1, 'perfeito')
    # 4

    tab = ((-1,1,0),(0,-1,0),(0,0,1))
    escolher_posicao_auto(tab, 1, 'perfeito')
    # 3

    tab = ((0,0,0),(0,-1,1),(1,0,0))
    escolher_posicao_auto(tab, -1, 'perfeito')
    # 9

    tab = ((0,0,1),(0,-1,0),(1,0,0))
    escolher_posicao_auto(tab, -1, 'perfeito')
    # 2

    tab = ((0,0,0),(1,-1,-1),(0,0,1))
    escolher_posicao_auto(tab, 1, 'perfeito')
    # 7

    tab = ((0,0,0),(-1,1,1),(0,0,-1))
    escolher_posicao_auto(tab, 1, 'perfeito')
    # 7

    tab = ((0,0,0),(0,-1,1),(0,1,0))
    escolher_posicao_auto(tab, -1, 'perfeito')
    # 9 

    tab = ((1,0,0),(0,1,0),(0,0,-1))
    escolher_posicao_auto(tab, -1, 'perfeito')
    # 3 


    tab = ((-1,0,0),(0,1,-1),(0,0,1))
    escolher_posicao_auto(tab, 1, 'perfeito')
    # 7

    tab = ((1,0,0),(0,-1,1),(0,0,-1)) 
    escolher_posicao_auto(tab, 1, 'perfeito')
    # 2

    return



def teste_jogo_do_galo():
    total_score = 200
    fun_name = jogo_do_galo


    jogo_do_galo_mooshak('X', 'basico', '3\\n1\\n2')
    # Bem-vindo ao JOGO DO GALO.\nO jogador joga com 'X'.\nTurno do jogador. Escolha uma posicao livre:    |   | X \n-----------\n   |   |   \n-----------\n   |   |   \nTurno do computador (basico):\n   |   | X \n-----------\n   | O |   \n-----------\n   |   |   \nTurno do jogador. Escolha uma posicao livre:  X |   | X \n-----------\n   | O |   \n-----------\n   |   |   \nTurno do computador (basico):\n X |   | X \n-----------\n   | O |   \n-----------\n O |   |   \nTurno do jogador. Escolha uma posicao livre:  X | X | X \n-----------\n   | O |   \n-----------\n O |   |   \nX


    jogo_do_galo_mooshak('O', 'basico', '9\\n3\\n4\\n8')
    # Bem-vindo ao JOGO DO GALO.\nO jogador joga com 'O'.\nTurno do computador (basico):\n   |   |   \n-----------\n   | X |   \n-----------\n   |   |   \nTurno do jogador. Escolha uma posicao livre:    |   |   \n-----------\n   | X |   \n-----------\n   |   | O \nTurno do computador (basico):\n X |   |   \n-----------\n   | X |   \n-----------\n   |   | O \nTurno do jogador. Escolha uma posicao livre:  X |   | O \n-----------\n   | X |   \n-----------\n   |   | O \nTurno do computador (basico):\n X |   | O \n-----------\n   | X |   \n-----------\n X |   | O \nTurno do jogador. Escolha uma posicao livre:  X |   | O \n-----------\n O | X |   \n-----------\n X |   | O \nTurno do computador (basico):\n X | X | O \n-----------\n O | X |   \n-----------\n X |   | O \nTurno do jogador. Escolha uma posicao livre:  X | X | O \n-----------\n O | X |   \n-----------\n X | O | O \nTurno do computador (basico):\n X | X | O \n-----------\n O | X | X \n-----------\n X | O | O \nEMPATE


    jogo_do_galo_mooshak('X', 'basico', '1\\n2\\n4')
    # Bem-vindo ao JOGO DO GALO.\nO jogador joga com 'X'.\nTurno do jogador. Escolha uma posicao livre:  X |   |   \n-----------\n   |   |   \n-----------\n   |   |   \nTurno do computador (basico):\n X |   |   \n-----------\n   | O |   \n-----------\n   |   |   \nTurno do jogador. Escolha uma posicao livre:  X | X |   \n-----------\n   | O |   \n-----------\n   |   |   \nTurno do computador (basico):\n X | X | O \n-----------\n   | O |   \n-----------\n   |   |   \nTurno do jogador. Escolha uma posicao livre:  X | X | O \n-----------\n X | O |   \n-----------\n   |   |   \nTurno do computador (basico):\n X | X | O \n-----------\n X | O |   \n-----------\n O |   |   \nO


    jogo_do_galo_mooshak('O', 'basico', '9\\n6\\n7')
    # Bem-vindo ao JOGO DO GALO.\nO jogador joga com 'O'.\nTurno do computador (basico):\n   |   |   \n-----------\n   | X |   \n-----------\n   |   |   \nTurno do jogador. Escolha uma posicao livre:    |   |   \n-----------\n   | X |   \n-----------\n   |   | O \nTurno do computador (basico):\n X |   |   \n-----------\n   | X |   \n-----------\n   |   | O \nTurno do jogador. Escolha uma posicao livre:  X |   |   \n-----------\n   | X | O \n-----------\n   |   | O \nTurno do computador (basico):\n X |   | X \n-----------\n   | X | O \n-----------\n   |   | O \nTurno do jogador. Escolha uma posicao livre:  X |   | X \n-----------\n   | X | O \n-----------\n O |   | O \nTurno do computador (basico):\n X | X | X \n-----------\n   | X | O \n-----------\n O |   | O \nX


    jogo_do_galo_mooshak('X', 'basico', '5\\n9\\n2\\n4\\n8')
    # Bem-vindo ao JOGO DO GALO.\nO jogador joga com 'X'.\nTurno do jogador. Escolha uma posicao livre:    |   |   \n-----------\n   | X |   \n-----------\n   |   |   \nTurno do computador (basico):\n O |   |   \n-----------\n   | X |   \n-----------\n   |   |   \nTurno do jogador. Escolha uma posicao livre:  O |   |   \n-----------\n   | X |   \n-----------\n   |   | X \nTurno do computador (basico):\n O |   | O \n-----------\n   | X |   \n-----------\n   |   | X \nTurno do jogador. Escolha uma posicao livre:  O | X | O \n-----------\n   | X |   \n-----------\n   |   | X \nTurno do computador (basico):\n O | X | O \n-----------\n   | X |   \n-----------\n O |   | X \nTurno do jogador. Escolha uma posicao livre:  O | X | O \n-----------\n X | X |   \n-----------\n O |   | X \nTurno do computador (basico):\n O | X | O \n-----------\n X | X | O \n-----------\n O |   | X \nTurno do jogador. Escolha uma posicao livre:  O | X | O \n-----------\n X | X | O \n-----------\n O | X | X \nX


    return
