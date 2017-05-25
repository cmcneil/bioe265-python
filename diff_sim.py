import numpy as np
import matplotlib.pyplot as plt
from bloch import bloch



N = 500
M = 300
D = 0.0
#P = 512
    
mx = np.ones((1, N))
my = np.zeros((1, N))
mz = np.zeros((1, N))
    
dp = np.random.normal(loc=0.0, scale=1.8, size=(2, N))
dt = 4.0*10**(-6)
G = np.array([[4.0], [0.0]])
S = np.zeros((M+3, 1))
df = np.zeros((1, N))
    
for n in range(1, int(M/2)):
    mx, my, mz = bloch.bloch(0, G, dt, 800, 800, 0, dp, 2, mx, my, mz)
    print(np.shape(mx))
    dp = dp + np.random.normal(loc=0.0, scale=D, size=(2, N))
    S[n, 0] = np.absolute(np.mean(mx + 1j*my))
    print(np.shape(S))
    print(np.shape(dp))
    plt.quiver(dp[0, :], dp[1, :], mx, my)
    plt.show()
for n in range(1, int(M/2)):
    mx, my, mz = bloch.bloch(0, -G, dt, 800, 800, 0, dp, 2, mx, my, mz)
    print(np.shape(mx))
    dp = dp + np.random.normal(loc=0.0, scale=D, size=(2, N))
    S[int(n+M/2), 0] = np.absolute(np.mean(mx + 1j*my))
    print(np.shape(S))
    print(np.shape(dp))
    
plt.plot(S)
plt.show()
