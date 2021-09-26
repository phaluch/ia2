"""
Rotina para criação de população inicial aleatória
"""

from random import random

# Function to convert decimal number
# to binary using recursion
def DecimalToBinary(num):
    if num == 1:
        return str(num % 2)
    return DecimalToBinary(num // 2) + str(num % 2)

def BinaryToDecimal(num):
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



"""
Rotina para codificação binária dos invivíduos
pop: população a ser codificada
Ncrom: número de cromossomos em cada indivíduo
CromLim: Matriz Ncrom x 2 contendo os limites inferior e superior para os cromossomos
Lbits: vetor Ncrom contendo o número de bits para cada cromossomo
"""

def cod(pop, CromLim, Lbits):
    Nind = len(pop)
    Ncrom = len(CromLim)
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

"""
Rotina para decodificação binária dos invivíduos
pop: população a ser decodificada
Ncrom: número de cromossomos em cada indivíduo
Lbits: vetor Ncrom contendo o número de bits para cada cromossomo
"""

def decod(pop, Lbits):
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
        


Nind = 6
CromLim = [(1,2),(3,4),(5,6),(7,8),(1,2),(3,4)]
CromLim = [(10*x[0],10*x[1]) for x in CromLim]

pop = newpop(Nind, CromLim)
k = 2
Lbits = [k*i+5 for i in range(Nind)]
print(Lbits)
print(pop)
codpop = cod(pop, CromLim, Lbits)
print(codpop)
decpop = decod(codpop, Lbits)
print(decpop)