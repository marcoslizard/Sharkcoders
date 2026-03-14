from matplotlib import pyplot as plt
import numpy as np

x =  np.arange(-20,21)

y = np.where(x < 0, np.abs(x)**2 ,
     np.where(x == 0 ,0, x**3))
