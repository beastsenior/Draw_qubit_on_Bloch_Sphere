import warnings
warnings.filterwarnings("ignore")

import cmath
import matplotlib.pyplot as plt
import define as d

a=1/cmath.sqrt(2)
b=-1j/cmath.sqrt(2)
#a=0
#b=-1j
#a=1
#b=0

print("a, b:")
print(a, b)

d.plot_bloch_vector_by_ab(a, b)
plt.show()
plt.legend()