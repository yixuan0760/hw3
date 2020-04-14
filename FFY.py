import matplotlib.pyplot as plt

import numpy as np

import serial

import time


Fs = 10.0;  # sampling rate

Ts = 1.0/Fs; # sampling interval

t = np.arange(0,10,Ts) # time vector; create Fs samples between 0 and 1.0 sec.
x = np.arange(0,10,Ts)
y = np.arange(0,10,Ts) # signal vector; create Fs samples
z = np.arange(0,10,Ts)
tilt=np.arange(0,10,Ts)

n = len(y) # length of the signal

k = np.arange(n)

T = n/Fs

frq = k/T # a vector of frequencies; two sides frequency range

frq = frq[range(int(n/2))] # one side frequency range


serdev = '/dev/ttyACM0'

s = serial.Serial(serdev,115200)

for a in range(0,100):
    line=s.readline()
    line=line.strip() # Read an echo string from K66F terminated with '\n'

    # print line

    tilt[a] = float(line)
for a in range(100,200):
    line=s.readline()
    line=line.strip() # Read an echo string from K66F terminated with '\n'

    # print line

    x[a-100] = float(line)
for a in range(200,300):
    line=s.readline()
    line=line.strip() # Read an echo string from K66F terminated with '\n'

    # print line

    y[a-200] = float(line)
for a in range(300,400):
    line=s.readline()
    line=line.strip() # Read an echo string from K66F terminated with '\n'

    # print line

    z[a-300] = float(line)


fig, ax = plt.subplots(2, 1)
ax[0].plot(t,x)
ax[0].plot(t,y)
ax[0].plot(t,z)
ax[0].set_xlabel('Time')

ax[0].set_ylabel('Acc Vector' )

ax[1].stem(t,tilt) # plotting the spectrum

ax[1].set_xlabel('Time')

ax[1].set_ylabel('Tilt')

plt.show()

s.close()