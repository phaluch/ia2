"""
Rotina para criação de população inicial aleatória
"""

import random

# Function to convert decimal number
# to binary using recursion
def DecimalToBinary(num):
    """
    Converte inteiros base 10 em strings representando valores base 2, com o mínimo possível de bits.
    @param num : Número Inteiro
    @return : string de 0's e 1's
    """
    if num == 1:
        return str(num % 2)
    return DecimalToBinary(num // 2) + str(num % 2)

def BinaryToDecimal(num):
    """
    Converte strings representando valores base 2 em inteiros base 10.
    @param num : string de 0's e 1's
    @return : Número Inteiro
    """
    ans = 0
    tam = len(num)
    for i in range(tam):
        if num[i] == '1':
            exponent = tam-i - 1
            ans+= 2**exponent
    return ans
    
def newpop(Nind, CromLim):
    """
    Cria a população
    @param Nind : Número de indivíduos na população
    @param CromLim : Range de valores possíveis para cada cromossomo
    @return : Lista de dicionários, onde cada dicionário é um indivíduo
    """

    Ncrom = len(CromLim)

    Populacao = []

    for i in range(Nind):
        individuo = {}
        for j in range(Ncrom):
            inf = CromLim[j][0]
            sup = CromLim[j][1]
            individuo[j] = inf + round(random()*(sup-inf))
        Populacao.append(individuo)

    return Populacao





def cod(pop, Lbits):
    """
    Rotina para codificação binária dos invivíduos
    pop: população a ser codificada
    Ncrom: número de cromossomos em cada indivíduo
    CromLim: Matriz Ncrom x 2 contendo os limites inferior e superior para os cromossomos
    Lbits: vetor Ncrom contendo o número de bits para cada cromossomo
    """
    Nind = len(pop)
    Ncrom = len(pop[0])
    coded = {}
    temp = '' # Variável que vai receber o indivíduo
    for i in range(Nind):
        for j in range(Ncrom):
            aux = pop[i][j]
            baux = DecimalToBinary(int(aux))
            if Lbits[j]-len(baux) < 0:
                raise Exception(f'{Lbits[j]} bits não são suficientes para escrever {aux} em binário ({baux})')
            padding = '0' * (Lbits[j]-len(baux))
            
            baux = padding + baux
            if j == 0:
                temp = baux
            else:
                temp = temp + baux
        coded[i] = temp
    return coded



def decod(pop, Lbits):
    """
    Rotina para decodificação binária dos invivíduos
    pop: população a ser decodificada
    Ncrom: número de cromossomos em cada indivíduo
    Lbits: vetor Ncrom contendo o número de bits para cada cromossomo
    """
    decoded = []
    for ind in pop:
        startIndex = endIndex = 0
        tempInd = {}
        for i in range(len(Lbits)):
            endIndex += Lbits[i] 
            curCrom = pop[ind][startIndex:endIndex]
            tempInd[i] = BinaryToDecimal(curCrom)
            startIndex = endIndex
        decoded.append(tempInd)
    return decoded
        

def fit(pop, func):
    """
    Função que aplica uma função fit específica para uma população
    @param pop : lista de dicionários, onde cada dicionário é um indivíduo
    @param func : Função que aceita um indivíduo no formato dicionário.
    @return : list contendo os valores de fit para cada indivíduo de pop, em ordem
    """

    return [func(pop[ind]) for ind in pop]


def roulette(pop, fitValues):
    """
    Cria nova população, selecionando indivíduos de pop baseado nos pesos dos valores de fit.
    @param : lista de indivíduos
    @param fitValues : list(int) ou list(float), que será convertida em list(int)
    @return : lista de individuos selecionados
    """
    fitValues = [int(x) for x in fitValues]
    tempPop = []
    for i in range(len(pop)):
        tempPop += [pop[i] for _ in range(fitValues[i])]
    # Etapa de seleção
    newPop = [random.choice(tempPop) for _ in range(len(pop))]
    return newPop

def cruzamentoSimples(x, y, Lbits, cut=None):
    """
    Recebe dois indivíduos, e retorna dois filhos executando cruzamento simples

    @param x: primeiro indivíduo
    @param y: segundo indivíduo
    @param Lbits: lista com número de bits de cada gene, em sequência
    @param cut: índice no qual executar o corte. A primeira metade incluirá até o cut-ésimo gene, inclusive. Se None, seleciona cut aleatoriamente.
    @return: tupla (x', y') com os filhos do cruzamento
    """

    if cut is None:
        cut = random.randint(1, len(Lbits))

    startIndex = sum([Lbits[x] for x in range(cut)]) # Índice do começo da segunda metade
    x1, x2 = x[:startIndex], x[startIndex:]
    y1, y2 = y[:startIndex], y[startIndex:]

    return x1+y2, y1+x2
    
def mutacaoIndividuo(x):
    """
    Esta função troca um dos caracteres, escolhido aleatoriamente, na string pelo seu oposto.

    @param x: str de 0's e 1's
    @return: str de 0's e 1's
    """
    mpoint = random.randint(0,len(x)-1)
    metade1, metade2 = x[:mpoint], x[mpoint+1:] # +1 no final para 'pular' o elemento que vamos trocar
    novoValor = '0' if x[mpoint] == '1' else '1'
    return metade1+novoValor+metade2


def mutacaoPop(pop, pmut):
    """
    Aplica a mutação individual à população na proporção pmut.

    @param pop: lista de strings de 0's e 1's
    @param pmut: Probabilidade de mutação. 0 <= pmut <= 1
    @return: lista de strings de 0's e 1's
    """

    return [mutacaoIndividuo(pop[ind]) if random.random() < pmut else ind for ind in pop]


