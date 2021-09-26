from ag import *
Nind = 6
CromLim = [(1,2),(3,4),(5,6),(7,8),(1,2),(3,4)]
CromLim = [(10*x[0],10*x[1]) for x in CromLim]





pop = newpop(Nind, CromLim)
k = 2
Lbits = [k*i+3 for i in range(Nind)]
print(Lbits)
print(pop)
codpop = cod(pop, CromLim, Lbits)
print(codpop)
decpop = decod(codpop, Lbits)
print(decpop)