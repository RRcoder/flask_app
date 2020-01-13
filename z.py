import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

data = {
        'peli 1': 1,
        'peli 2': 1,
        'peli 3': 1,
        'peli 4': 2,
        'peli 5': 4,
        'peli 6': 1,
        'peli 7': 5,
        'peli 8 asdfasd fasd asdf asdf asdfad asdf asdf': 2,
        'peli 9': 1,
        'peli 10': 1,
        'peli 11': 1,
        'peli 12': 2,
        'peli 13': 4,
        'peli 14': 1,
        'peli 15': 5,
        'peli 16 asdfasd fasd asdf asdf asdfad asdf asdf': 2,
        'peli 17': 1,
        'peli 18': 1,
        'peli 19': 1,
        'peli 20': 2,
        'peli 21': 4,
        'peli 22': 1,
        'peli 23': 5,
        'peli 24 asdfasd fasd asdf asdf asdfad asdf asdf': 2,
        'peli 25': 1,
        'peli 26': 1,
        'peli 27': 1,
        'peli 28': 2,
        'peli 29': 4,
        'peli 30': 1,
        'peli 31': 5,
        'peli 32 asdfasd fasd asdf asdf asdfad asdf asdf': 2,
        'peli 33': 1,
        'peli 34': 1,
        'peli 35': 1,
        'peli 36': 2,
        'peli 37': 4,
        'peli 38': 1,
        'peli 39': 5,
        'peli 40 asdfasd fasd asdf asdf asdfad asdf asdf': 2,
        'peli 41': 1,
        'peli 42': 1,
        'peli 43': 1,
        'peli 44': 2,
        'peli 45': 4,
        'peli 46': 1,
        'peli 47': 5,
        'peli 48 asdfasd fasd asdf asdf asdfad asdf asdf': 7

        }


datos = list(data.values())
etiq = list(data.keys())

y_pos = np.arange(len(datos))


fig, ax = plt.subplots()

ax.barh(y_pos, datos, align='center')
ax.set_yticks(y_pos)
ax.set_yticklabels(etiq)
#plt.xlim(0, 100)
plt.tight_layout()

ax.set_xticks([1,2,3,4,5,6,7,8])
print y_pos
print data

plt.show()
