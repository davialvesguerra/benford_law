#import pacotes

import pandas as pd
import numpy as np
from random import sample
import matplotlib.pyplot as plt

#cria uma lista onde se pega apenas o primeiro digito
lista = [x[0] for x in sample([str(x) for x in range(100000)],10000)]

#cria uma função para calcular a probabilidade ideal
def probab_ideal(lista):
  dic = {}

  for i in range(1,10):
    dic[i] = lista.count(str(i))

  dic = pd.Series(dic)

  plt.bar(range(1,10),dic.values)
  plt.show()

probab_ideal(lista)

#######################################################################

#essa lista simula as probabilidades de cada digito
benford = [float(np.log10(1+1/x)) for x in range(1,10)]

#plota um gráfico de linhas
plt.plot(range(1,10), benford)
plt.show()
