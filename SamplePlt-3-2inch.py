# To execute this code: python3 SamplePlt.py
# This is Ran Xu's notebook on using matplotlib.pylot to execellent figures in CS area.
import matplotlib.pyplot as plt
import numpy as np

# Two figures in a column - 16; A figure in a column - 32; 
# A figure across columns - 64; 
fs = 32   # 3.2 in by 2.4 in

plt.figure(figsize = (3.2, 2.4), dpi = 300)
plt.axes().set_position([0.18, 0.15, 0.79, 0.79])
plt.axes().spines['top'].set_color('none')
plt.axes().spines['right'].set_color('none')

plt.xlabel('Number of A and B given C and D', fontsize=8) # <=15 chacters
plt.axes().xaxis.set_label_coords(0.5,-0.12)
plt.xlim([0,10])
plt.xticks(np.arange(1,10))
plt.axes().set_xticklabels(labels = [str(x) for x in np.arange(1,10)], 
                           fontsize=8)

plt.ylabel('Exection time of baseline (ms)', fontsize=8)
plt.axes().yaxis.set_label_coords(-0.15,0.5)
plt.ylim([1.5,6.5])
plt.yticks([2, 2.5, 3 ,3.5, 4, 4.5, 5, 5.5, 6])
plt.axes().set_yticklabels(labels = [str(x) for x in np.arange(1000,10000,1000)], 
                           fontsize=8)
plt.axes().set_axisbelow(True)
plt.grid()

# Draw lines
plt.plot([2,3,4,5],[6,6,6,6], 
         c='b', linestyle='-', lw=2, label = 'li.')
plt.plot([2,3,4,5],[3,4,5,6], 
         c='r', linestyle='--', lw=2)
plt.plot([2,3,4,5],[4,3,4,5], 
         c='y', linestyle=':', lw=2)
plt.plot([2,3,4,5],[2,2,2,2], 
         c='m', linestyle='-.', lw=2)

# Draw scatters
plt.scatter(2,6, c='b',marker='o',s=16, label = 'sc.')
plt.scatter(3,5, c='r',marker='s',s=16)
plt.scatter(4,4, c='y',marker='+',s=16)
plt.scatter(5,3, c='m',marker='x',s=16)

# Draw stacked bars
firstMeans = np.array([1, 1.2, 1.4, 1.6, 1.8])+2
firstStd = np.array([0.1, 0.1, 0.1, 0.1, 0.1])
secondMeans =  np.array([0.1, 0.2, 0.3, 0.4, 0.5])+0.5
secondStd = np.array([0.1, 0.1, 0.1, 0.1, 0.1])
thirdMeans = np.array([0.1, 0.2, 0.3, 0.4, 0.5])+1
thirdStd = np.array([0.1, 0.1, 0.1, 0.1, 0.1])
x = [1,3,5,7,9]
plt.bar(x,firstMeans, yerr=firstStd,
        width=0.8, color='r', label = 'men') 
plt.bar(x,secondMeans, yerr=secondStd, bottom=firstMeans, 
        width=0.8, color='b') 
plt.bar(x,thirdMeans, yerr=thirdStd, bottom=secondMeans+firstMeans, 
        width=0.8, color='y') 

# Circle and text
plt.scatter(6,6, c='r',marker='o',s=16)
plt.text(5.6,5.7,'goal',fontsize=8)

# Finishing  
#plt.legend(loc='upper right',fontsize=5)
plt.legend(ncol=3, loc='upper center', bbox_to_anchor=(0.4, 1.15),fontsize=8)
plt.savefig('SampleFig-3-2-inch.png')
plt.show()
