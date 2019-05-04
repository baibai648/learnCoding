'''
Auther: Qbm

Description: 
    - add this file to ipython config path, startup folder
    - file name starts w/ a number, which specifies start-up load sequence
'''

#import numpy and set the printed precision to human readable 
print ('STARTUP modules IMPORTing ...')
import numpy as np
np_precision=3
np.set_printoptions(precision=np_precision,suppress=True)
print ('np imported, precision sets to %d'%np_precision)
import scipy as scipy
print ('scipy imported')
import matplotlib.pyplot as plt
#print plt.style.available           #checks avialable plot style
plt_style='ggplot'
plt.style.use('%s'%plt_style)
plt.ion()
print ('plt imported, style set to %s'%plt_style)
#%config InlineBackend.figure_format='retina'
import pandas as pd
print ('pd imported')
print ('STARTUP modules IMPORTends ...')
