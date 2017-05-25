import numpy as np
import scipy.special as sp

fft2c = lambda f: np.ifftshift(np.fft.fftshift(np.fft.fft2(f)))
ifft2c = lambda F: np.fft.fftshift(np.fft.ifft2(np.fft.ifftshift(F)))

def mysincd(x):
    eps = 10**-12
    if np.abs(x) < eps:
        return 1.0
    return np.sin(np.pi * x) / (np.pi * x)
mysinc = np.vectorize(mysincd)

def myjincd(x):
    eps = 10**-12
    if np.abs(x) < eps:
        return np.pi / 4
    return sp.jn(1, np.pi*x) / (2 * x)
myjinc = np.vectorize(myjincd)
