# sudo apt-get install python-matplotlib
# sudo pip install numpy
# sudo apt-get install python-numpy python-scipy 

import matplotlib.pyplot as plt
import csv
import pylab
from pylab import xticks
x = []
y = []

with open('Hist.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(float(row[0]))
        #y.append(float(row[1]))
bins = 1000

plt.hist(x,bins, label='Secondary Particles')
#xticks(range(0,50000))
#pylab.xticks(fontsize=15)
plt.xlabel('Energy[MeV]')
plt.ylabel('Number of particles')
plt.title('Particle Kinetic Energy')
plt.grid(True)
plt.legend()
plt.show()


