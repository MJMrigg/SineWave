# This code is a modified version of a code from pythonic
# Original code here: https://pythontic.com/visualization/charts/sinewave
import numpy as np
import matplotlib.pyplot as plot

# Create the x value, time
time = np.arange(0, 10, 0.01)
# The computer will start at 0.
# At every 0.01 place on the x-axis, it will plug in that points into the sine equation.
# This will go on until 10 is reached, which is the maximum x-value

# Create the y value, amplitude, using the sine equation
# A = sine(F * t), A = Amplitude, F = Frequency, t = time
amplitude = np.sin(time)


# Plot the amplitude and time. A color can also be added, in this case, b=blue
plot.plot(time, amplitude, color='b')

# Give the graph a title
plot.title('Sine Wave')

# Label the x and y axis
plot.xlabel('Time')
plot.ylabel('Amplitude')

# Create the grid.
# The true/false displays the grid. True displays it. False does not
plot.grid(True)
# This line of code draws a horizontal line at y=0 that is black to separate the positive and negative amplitudes
plot.axhline(y=0, color='k')

# Plot the sine wave
plot.show()
