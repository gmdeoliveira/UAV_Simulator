import matplotlib.pyplot as plt
import numpy as np

## List of variables ##
m = 1 # Quadcopter mass (kg)
g = 9.81 # Gravity aceleration (m/s^2)
# Gains definition
Kd = 1
Kp = .5

## Initial conditions ##
z0 = 0 # Initial height
w0 = 0 # Initial velocity
u0 = m*g # Initial vertical force
z_des = 0 # Initial desired state condition
w_des = 0 # Initial desired velocity

## ODE definition ##
dt = 0.1 # Time step
tspan = 40 # Duration of the simulation
#t = 0 # Variable to indicate the time during the simulation
n = int(tspan/dt) # Array size
# Creating the time and states arrays
z = np.zeros(n)
w = np.zeros(n)
t = np.zeros(n)

i = 0 # Count variable
z[i] = z0
w[i] = w0

## Loop using Euler integration
for i in range(n-1):
    # Step in the desired height
    if (t[i] >= 5):
        z_des = 1
        
    e = z_des - z[i] # Error
    edot = w_des - w[i] # Error derivative

    u = u0 + Kd * edot + Kp * e # Controller equation

    z_ddot = u/m - g # Z acceleration

    # Updating the states and the time
    w[i+1] = w[i] + z_ddot * dt
    z[i+1] = z[i] + w[i+1] * dt
    t[i+1] = t[i] + dt

plt.plot(t,z,t,w)
plt.show()

