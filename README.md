AI-Enhanced Quantum Computing Simulator
Overview

This project is an interactive Python-based simulator that allows users to build, simulate, and optimize quantum circuits. It integrates classical AI techniques to automatically optimize quantum gates for target quantum states, providing rich visualizations and quantum metrics.
Features

    Interactive Circuit Builder: Construct quantum circuits with standard gates (H, X, RX, RY, RZ, CNOT).

    Quantum Simulation: Compute exact statevectors and simulate measurement outcomes.

    Visualization: Display circuit diagrams, state probabilities, measurement histograms, Bloch sphere, and metrics such as entanglement entropy, fidelity, and coherence.

    AI Optimization: Use a neural network to find optimal gate parameters for variational quantum circuits, maximizing fidelity with target states.

    Quantum ML and Error Correction Demos: Explore quantum machine learning and quantum error correction algorithms.

Technologies Used

    Qiskit: For quantum circuit modeling and simulation.

    PennyLane: For variational circuits and hybrid quantum-classical optimization.

    PyTorch: To implement and train neural networks for circuit parameter optimization.

    NumPy & Matplotlib: Numerical computation and visualizations.

    ipywidgets: Interactive user interface.

How To Use

    Run the interactive_circuit_builder() to open the UI.

    Add gates to qubits using dropdowns and sliders.

    Run the circuit to simulate and visualize quantum state and measurements.

    Use AI Optimize to let the system find optimal parameters for your circuit.

    Explore advanced demos or extend with custom gates.

Quantum Concepts

    Qubits, quantum gates, statevector, measurement, entanglement, fidelity, coherence.

    Variational quantum circuits with tunable parameters.

    Neural network-based quantum circuit optimization.

Installation Requirements

    Python 3.8+

    Qiskit

    PennyLane

    PyTorch

    NumPy

    Matplotlib

    ipywidgets

Potential Applications

    Quantum algorithm research and prototyping.

    Educational tool for understanding quantum computation and AI.

    Benchmarking and optimizing quantum circuits.
