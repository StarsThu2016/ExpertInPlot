# To execute this code: python3 SamplePlt.py
# This is Ran Xu's notebook on using matplotlib.pylot to execellent figures in CS area.
import matplotlib.pyplot as plt
import numpy as np

# Two figures in a column - 16; A figure in a column - 32; 
plt.figure(figsize = (6.4, 3.2), dpi = 300)
fontsize = 12

# Left figure
plt.subplot(121)
plt.plot([2,3,4,5],[6,6,6,6], c='b', linestyle='-', lw=2, label = 'y1')
plt.plot([2,3,4,5],[3,4,5,6], c='r', linestyle='--', lw=2, label = 'y2')
# Fine tuning left figure 
ax1 = plt.gca()
ax1.set_position([0.1, 0.15, 0.35, 0.7]) # W0, H0, W, H
# -- xs
plt.xlabel('X-axis', fontsize=fontsize) # <=15 chacters
ax1.xaxis.set_label_coords(0.5,-0.12)
plt.xlim([0,10])
plt.xticks(np.arange(1,10))
ax1.set_xticklabels(labels = [str(x) for x in np.arange(1,10)], fontsize=fontsize)
# -- ys
plt.ylabel('Y-axis', fontsize=fontsize) # <=15 chacters
ax1.yaxis.set_label_coords(-0.12, 0.5)
plt.ylim([0,10])
plt.yticks(np.arange(1,10))
ax1.set_yticklabels(labels = [str(x) for x in np.arange(1,10)], fontsize=fontsize)
# -- figure
ax1.set_axisbelow(True)
plt.grid()

# Right figure
plt.subplot(122)
plt.plot([2,3,4,5],[6,6,6,6], c='b', linestyle='-', lw=2, label = 'y1')
plt.plot([2,3,4,5],[3,4,5,6], c='r', linestyle='--', lw=2, label = 'y2')
# Right tuning left figure 
ax2 = plt.gca()
ax2.set_position([0.6, 0.15, 0.35, 0.7]) # W0, H0, W, H
# -- xs
plt.xlabel('X-axis', fontsize=fontsize) # <=15 chacters
ax2.xaxis.set_label_coords(0.5,-0.12)
plt.xlim([0,10])
plt.xticks(np.arange(1,10))
ax2.set_xticklabels(labels = [str(x) for x in np.arange(1,10)], fontsize=fontsize)
# -- ys
plt.ylabel('Y-axis', fontsize=fontsize) # <=15 chacters
ax2.yaxis.set_label_coords(-0.12, 0.5)
plt.ylim([0,10])
plt.yticks(np.arange(1,10))
ax2.set_yticklabels(labels = [str(x) for x in np.arange(1,10)], fontsize=fontsize)
# -- figure
ax2.set_axisbelow(True)
plt.grid()

# Finishing  
plt.legend(ncol=3, loc='upper center', bbox_to_anchor=(-0.3, 1.2),fontsize=fontsize)
plt.savefig('SampleFig-3-2-inch-ShareLegend.png')
