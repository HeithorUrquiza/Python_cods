"""
    - import this -> Zen do Python
    - Camel Case para nome de classes
    - letras minúsculas e underline para nomes de variáveis e funções
    
    _________________________________________________________________________________________________________________________________
    
    DIR -> Apresenta todos os atributos e funções/métodos disponíveis para determinado tipo de dado ou variável
    
    - dir(tipo de dados/variável)
    
    HELP -> Apresenta a documentação/como utilizar os atributos/propriedades e funções/métodos deisponíveis para determinado tipo de dado ou variável
    
    - help(tipo de dado/variável.propriedade)
    
    _________________________________________________________________________________________________________________________________
    
    RECEBENDO DADOS DO USUÁRIO
    
    nome = input(str("Qual o seu nome? "))  #Entrada de dados
    print(f"Seja Bem-vindo(a) {nome}") #Saída de dados
    
    - Exemplos de PRINT
    print('Seja bem-vindo %s' % nome)    
    print('Seja bem-vindo {0}'.fromat(nome))    
    print(f'Seja bem-vindo {nome}')
    
    * CAST -> conversão de um tipo de dado para outro    
    
    _________________________________________________________________________________________________________________________________
    
    TIPOS DE DADOS
    
    > type() => mostra qual é o tipo do dado
    
    - Numérico: 1, 100, 1_000_000
    - Float/Real/Decimal: 1.2, 3.99, 1_000.00 
    - Complex: basta adicionar j ao final (ex: 5j)
    - Booleano: True ou False | NOT: not + variável => inverte o valor lógico da variável
    - String: Todo dado envolvido por aspas simples('') ou duplas("") | Slice de String -- ex: print(nome[0:5]) | [::-1] -> Comece do primeiro elemtno, vá até o último e inverta
    
    _________________________________________________________________________________________________________________________________
    
    ESCOPO DE VARIÁVEIS
    
    --> Python é um liguagem de tipagem dinâmica, isto é, o seu tipo é atribuido quando declarada  EX: num = 3 (inteiro)
    
    -- Variáveis Globais
        São reconhecidas, ou seja, seu escopo compreende todo o programa
        
    -- Variáveis locais
        São reconhecidas apenas no bloco onde foram declaradas, ou seja, seu escopo é limitado
        
    _________________________________________________________________________________________________________________________________
    
    ESTRUTURAS CONDICIONAIS E LÓGICAS
    
    -- if/else/elif
    idade = 20
    if idade < 18:
        print('\nMenor de idade')
    elif idade == 18:
        print('\nJá atingiu 18 anos')
    else:
        print('\nMaior de idade')    
    print('')
    
    -- and/or/not/is
    not => são operadores unários
    and, or & is => são operadores binários
    
    ativo = True
    logado = not False #Inverte os valores Flase -> True
    if ativo and logado:
        print('\nBem-vindo usuário')
    else:
        print('\nVocê precisa ativar sua conta !!')
    print()

    logado = None
    if logado is None:
        print('Vázio')
        
    _________________________________________________________________________________________________________________________________
    
    ESTRUTURAS DE REPETIÇÃO 
    
    --> Utilizadas para iterar sobre sequências ou sobre valores iteráveis
    
    -- Loop for
    nome = 'Robertão'
    lista = [1, 2, 3, 4, 5]
    
    for num in lista:
        print(num)
    print()
    
    for letra in nome:
        print(letra)
    print()
    
    for i in range(5): #Similar a um array [0, 1, 2, 3, 4]
        print(i)

    nome = 'Heithor'
    for i, v in enumerate(nome): #Podemos usar o '_' para ocultar valores que não vamos usar
        print(f'{i} = {v}') #end = '' para não saltar linha no loop
        
    
    -- Ranges
    > Utilizados para gerar sequências númericas de forma especificada
    
    * Forma 1
    for i in range(11): #Vai de 0 a 10
        print(i)
        
    * Forma 2
    for i in range(1, 11): #Inicio especificado, mas o final permanece uma a casa a menos
        print(i)
        
    * Forma 3
    for i in range(1, 10, 2): #Especificando o paço (no exemplo de 2 em 2)
        print(i)
        
    * Forma 4 (Inverso)
    for i in range(10, 0, -1):
        print(i) 
        
    
    -- Loop While    
    > Cuidado com as condições de parada (loop infinito)

    * Exempo 1
    num = 1
    while(num < 10):
        print(num)
        num += 1    
        
    * Exemplo 2
    resp = ''
    while resp != 'Sim':
        resp = input('Deseja parar? ').title()
        
        
    -- Break
    > Responsável por encerrar os loops em alguns casos
    for num in range(1, 10):
    if num == 6:
        break
    print(num)
    
    while(True):
    resp = input('Sair? ').title()   
    if resp == 'Sim':
        break  
"""

  


