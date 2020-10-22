# Weakness: For more accuracy, adjust line 56
import numpy as np
from math import factorial

NUM_UMI = int(input("Number of UMI: "))
PCR = int(input("Num molecules per UMI: "))
TOTAL_MOLECULES = NUM_UMI * PCR
MIN_CAPTURE_UNIT = float(input("minimum unit for capture rate: "))
rMAX = int(input("How many units: "))
XMAX = int(input("For x = 1 to "))


def combinations(n, r):
    return factorial(n) // ( factorial(r) * factorial(n-r) )


# P = probability of capturing exactly x molecules
# n = number of total molecules
def P(x, n, prob):
    return combinations(n,x) * (prob) ** x * (1-prob) ** (n - x)


# Data for plotting
x = list(range(1,XMAX+1))
# 0.001 = 0.1 percent
r = list(range(1,rMAX+1))
i_r = 0
# set r
for value in r:
    r[i_r] = r[i_r] * MIN_CAPTURE_UNIT
    i_r = i_r + 1

# data
_xx, _yy = np.meshgrid(x, r)
xxx, rrr = _xx.ravel(), _yy.ravel()

# probability of finding EXACTLY x molecules
zzz = []
i_z = 0

# calculate zzz
while i_z < XMAX*rMAX:
    x_captured = xxx[i_z]
    prob = rrr[i_z]
    zzz.append(P(x_captured, TOTAL_MOLECULES, prob/NUM_UMI))
    i_z = i_z + 1

# probability of finding AT LEAST x molecules
zzz2 = []
count = 0

# Calculate zzz2 (sum zzz[i] to zzz[N])
num_it = PCR // 50
if PCR < 200:
    num_it = PCR // 10
count = 1  # 1 to XMAX
for capture_rate in rrr:
    Sum = 0.0
    i = count
    while i < num_it:  # NUM_UMI * PCR (to be more exact)
        Sum = Sum + P(i, TOTAL_MOLECULES, capture_rate/NUM_UMI)
        i = i + 1
    zzz2.append(Sum)
    count = count + 1
    if count > XMAX:
        count = 1
        continue

bottom = np.zeros_like(zzz)
width = 0.5
depth = 0.0005


import matplotlib.pyplot as plt
# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

# setup the figure and axes
fig = plt.figure(figsize=(8, 3))
ax1 = fig.add_subplot(121, projection='3d')
ax2 = fig.add_subplot(122, projection='3d')

ax1.bar3d(xxx, rrr, bottom, width, depth, zzz, shade=True)
ax1.set_title('Capture EXACTLY x molecules')

ax2.bar3d(xxx, rrr, bottom, width, depth, zzz2, shade=True)
ax2.set_title('Capture AT LEAST x molecules')

plt.setp(ax1, xlabel='x molecules captured')
plt.setp(ax1, ylabel='capture rate')
plt.setp(ax2, xlabel='x molecules captured (per UMI)')
plt.setp(ax2, ylabel='')

plt.show()

