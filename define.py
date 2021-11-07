import numpy as np
import cmath
import sys
from qiskit.visualization import plot_bloch_vector

#用量子态a|0>+b|1>中的a和b计算出cos(theta)|0>+e^i(phi)*sin(theta)|1>形式的theta和phi
def ab2sph(a, b):
    theta = 2 * cmath.acos(a)
    phi = cmath.log(sys.float_info.min+b/(sys.float_info.min+cmath.sin(theta/2)))/1j  #为了让除数不为0，还有让ln x的x不为0，添加了sys.float_info.min，即最小浮点数
    print("theta, phi:")
    print(theta.real, phi.real)
    return theta.real, phi.real

#用量子态cos(theta)|0>+e^i(phi)*sin(theta)|1>中的的theta和phi（球坐标）计算出bloch sphere中的x，y，z（直角坐标）
def sph2cart(theta, phi):
    x = np.sin(theta)*np.cos(phi)
    y = np.sin(theta)*np.sin(phi)
    z = np.cos(theta)
    print("x, y, z:")
    print(x, y, z)
    return x, y, z

#通过cos(theta)|0>+e^i(phi)*sin(theta)|1>中的的theta和phi（球坐标）在bloch sphere中画量子态
def plot_bloch_vector_by_sph(theta, phi):
    plot_bloch_vector(sph2cart(theta, phi))

#通过a|0>+b|1>中的a和b在bloch sphere中画量子态
def plot_bloch_vector_by_ab(a, b):
    theta, phi = ab2sph(a, b)
    plot_bloch_vector_by_sph(theta, phi)

