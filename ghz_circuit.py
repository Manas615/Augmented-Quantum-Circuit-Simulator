from qiskit import QuantumCircuit, Aer, transpile
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# Cell 8: GHZ State Circuit
qc_ghz = QuantumCircuit(3, 3)
qc_ghz.h(0)
qc_ghz.cx(0,1)
qc_ghz.cx(1,2)
qc_ghz.measure([0,1,2],[0,1,2])

qc_ghz.draw('mpl')
plt.show()
simulator = Aer.get_backend('qasm_simulator')
compiled_circuit = transpile(qc_ghz, simulator)
result = simulator.run(compiled_circuit, shots=1024).result()
counts = result.get_counts(qc_ghz)
plot_histogram(counts)
plt.title("GHZ State (3-qubit entanglement)")
plt.show()
