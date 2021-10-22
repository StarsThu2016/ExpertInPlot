'''
Plot a scientific figure, in 3.2 inch width, and polish it for the CS conferences.
Usage:
$ python3 plot_3_2_inch.py

Author: Ran Xu
'''

import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(3.2, 2.4), dpi=300)
plt.gca().set_position([0.15, 0.15, 0.81, 0.77])
plt.gca().spines['top'].set_color('none')
plt.gca().spines['right'].set_color('none')
plt.gca().set_xlabel('Number of A and B', fontsize=8)  # <=15 chacters
plt.gca().xaxis.set_label_coords(0.5, -0.12)
plt.gca().set_xlim([0, 10])
plt.gca().set_xticks(np.arange(1, 10))
plt.gca().set_xticklabels(labels=[str(x) for x in np.arange(1, 10)], fontsize=8)

plt.gca().set_ylabel('Exection time of baseline (ms)', fontsize=8)
plt.gca().yaxis.set_label_coords(-0.12, 0.5)
plt.gca().set_ylim([1.5, 6.5])
plt.gca().set_yticks(np.arange(2, 6.1, 0.5))
plt.gca().set_yticklabels(labels=[str(x) for x in np.arange(2, 6.1, 0.5)], fontsize=8)
plt.gca().set_axisbelow(True)
plt.grid()

# Draw lines
plt.plot([2, 3, 4, 5], [6, 6, 6, 6], c='b', linestyle='-', lw=2, label='li.')
plt.plot([2, 3, 4, 5], [3, 4, 5, 6], c='r', linestyle='--', lw=2)
plt.plot([2, 3, 4, 5], [4, 3, 4, 5], c ='y', linestyle=':', lw=2)
plt.plot([2, 3, 4, 5], [2, 2, 2, 2], c ='m', linestyle='-.', lw=2)

# Draw scatters
plt.scatter(2, 6, c='b', marker='o', s=16, label='sc.')
plt.scatter(3, 5, c='r', marker='s', s=16)
plt.scatter(4, 4, c='y', marker='+', s=16)
plt.scatter(5, 3, c='m', marker='x', s=16)

# Draw stacked bars
firstMeans = np.array([1, 1.2, 1.4, 1.6, 1.8]) + 2
firstStd = np.array([0.1, 0.1, 0.1, 0.1, 0.1])
secondMeans =  np.array([0.1, 0.2, 0.3, 0.4, 0.5]) + 0.5
secondStd = np.array([0.1, 0.1, 0.1, 0.1, 0.1])
thirdMeans = np.array([0.1, 0.2, 0.3, 0.4, 0.5]) + 1
thirdStd = np.array([0.1, 0.1, 0.1, 0.1, 0.1])
x = [1, 3, 5, 7, 9]
plt.bar(x, firstMeans, yerr=firstStd, width=0.8, color='r', label='men')
plt.bar(x, secondMeans, yerr=secondStd, bottom=firstMeans, width=0.8, color='b')
plt.bar(x, thirdMeans, yerr=thirdStd, bottom=secondMeans+firstMeans, width=0.8, color='y')

# Circle and text
plt.scatter(6, 6, c='r', marker='o', s=16)
plt.text(5.6, 5.7, 'goal', fontsize=8)

#plt.legend(loc='upper right', fontsize=8)
plt.legend(ncol=3, loc='upper center', bbox_to_anchor=(0.5, 1.10), fontsize=8)
plt.savefig('figure_3_2_inch.png')
#plt.show()
