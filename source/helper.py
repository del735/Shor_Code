from qiskit_aer import AerSimulator
from qiskit import transpile
import qiskit.quantum_info as qi
import matplotlib.pyplot as plt


def visualize(quantumCircuit):
    simulator = AerSimulator()
    compiledCircuit = transpile(quantumCircuit, simulator)
    result = simulator.run(compiledCircuit).result()

    # Get the statevector of output.
    statevector = result.get_statevector()

    # Statevector with qubit labels formatted as Qiskit does for statevectors.
    qubitLabels = [
        f"{register.name}_{i}"
        for register in quantumCircuit.qregs
        for i in reversed(range(register.size))
    ]
    statevectorLabeled = "|" + "".join(qubitLabels[::-1]) + "\\rangle"

    # Visualize the statevector in LaTeX.
    latexStatevector = qi.Statevector(statevector).draw(output="latex_source")
    figure, axes = plt.subplots(figsize=(10, 0.5))
    axes.text(
        0.5,
        0.5,
        f"Vector labels: ${statevectorLabeled}$. Output: ${latexStatevector}$.",
        fontsize=12,
        va="center",
        ha="center",
    )
    axes.axis("off")

    # Draw the quantum circuit.
    quantumCircuit.draw(output="mpl")

    # Show all figures.
    plt.show()
