import warnings
warnings.filterwarnings("ignore")

import cmath
import matplotlib.pyplot as plt
import define

#a=1/cmath.sqrt(2)
#b=-1j/cmath.sqrt(2)

#a=0
#b=-1j

#a=0
#b=1

a=1/cmath.sqrt(2)
b=1/cmath.sqrt(2)
c=1/cmath.sqrt(2)
d=-1/cmath.sqrt(2)

print("a, b:")
print(a, b)

define.plot_bloch_vector_by_ab(a, b)
define.plot_bloch_vector_by_ab(c, d)
plt.show()
plt.legend()