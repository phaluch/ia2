"""
Rotina para criação de população inicial aleatória
"""

from random import random

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
            individuo[j] = inf + random()*(sup-inf)
        Populacao.append(individuo)

    return Populacao