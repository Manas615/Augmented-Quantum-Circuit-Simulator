from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Function to draw a Bloch sphere
def plot_bloch_sphere(ax):
    # Draw sphere
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)
    x = np.outer(np.cos(u), np.sin(v))
    y = np.outer(np.sin(u), np.sin(v))
    z = np.outer(np.ones(np.size(u)), np.cos(v))
    ax.plot_surface(x, y, z, color='#ADD8E6', alpha=0.2)

    # Draw axes
    ax.plot([-1.5, 1.5], [0, 0], [0, 0], 'k--', alpha=0.5)
    ax.plot([0, 0], [-1.5, 1.5], [0, 0], 'k--', alpha=0.5)
    ax.plot([0, 0], [0, 0], [-1.5, 1.5], 'k--', alpha=0.5)

    # Labels
    ax.text(0, 0, 1.6, '|0>', color='k')
    ax.text(0, 0, -1.6, '|1>', color='k')
    ax.text(1.6, 0, 0, '|+>', color='k')
    ax.text(-1.6, 0, 0, '|->', color='k')
    ax.text(0, 1.6, 0, '|i+>', color='k')
    ax.text(0, -1.6, 0, '|i->', color='k')

    ax.set_xlim([-1.5, 1.5])
    ax.set_ylim([-1.5, 1.5])
    ax.set_zlim([-1.5, 1.5])
    ax.set_axis_off()

# Create a figure and an axes for the Bloch sphere
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')
plot_bloch_sphere(ax)

plt.ion() # Turn on interactive mode

# Initialize the vector plot
line, = ax.plot([0, 0], [0, 0], [0, 1], 'r-', linewidth=3)

for frame in range(200):
    # Create a quantum circuit for a single qubit
    qc = QuantumCircuit(1)
    # Apply a rotation around the Y-axis, varying with the frame
    qc.ry(frame * 2 * np.pi / 200, 0) # Rotate 2pi over 200 frames

    # Get the statevector
    state = Statevector.from_instruction(qc)

    alpha = state[0]
    beta = state[1]
    x = 2 * (alpha * beta.conjugate()).real
    y = 2 * (alpha * beta.conjugate()).imag
    z = (abs(alpha)**2) - (abs(beta)**2)
    bloch_vec = [x, y, z]

    line.set_data([0, bloch_vec[0]], [0, bloch_vec[1]])
    line.set_3d_properties([0, bloch_vec[2]])

    fig.canvas.draw_idle()
    fig.canvas.flush_events()
    plt.pause(0.05)

plt.ioff() # Turn off interactive mode
plt.show() # Keep the final plot open