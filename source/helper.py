"""
This module provides visualization for quantum circuits and their 
resulting statevectors.
"""

from qiskit_aer import AerSimulator
from qiskit import transpile
import qiskit.quantum_info as qi
import matplotlib.pyplot as plt

circuitStyle = {
    # Changes custom instruction colors.
    "displaycolor": {
        "                Stabs             ": ("#EFBF04", "#000000"),
        "                Corr              ": ("#305CDE", "#000000"),
    },
    # Changes classical wire style.
    "creglinestyle": "--",
}


def visualize(quantumCircuit):
    """
    Simulates a quantum circuit, extracts its statevector, and visualizes both
    the statevector and the circuit using Matplotlib.
    """

    simulator = AerSimulator()
    compiledCircuit = transpile(quantumCircuit, simulator)
    result = simulator.run(compiledCircuit).result()

    # Get the statevector of output.
    statevector = result.get_statevector()

    # Statevector string with qubit labels formatted as Qiskit does for statevectors.
    qubitLabels = [
        f"{register.name}_{i}"
        for register in quantumCircuit.qregs
        for i in range(register.size)
    ]
    statevectorLabeled = "|" + "".join(qubitLabels[::-1]) + "\\rangle"

    # For visualizing the statevector in LaTeX using Matplotlib.
    latexStatevector = qi.Statevector(statevector).draw(output="latex_source")
    plt.figure(figsize=(12, 0.8))
    plt.figtext(
        0.5,
        0.5,
        f"Vector labels: ${statevectorLabeled}$.\nOutput: ${latexStatevector}$.\nSyndrome: $(a_0, ..., a_7)$ with decoded qubit: $|q_0\\rangle$.",
        fontsize=12,
        va="center",
        ha="center",
    )
    plt.axis("off")

    # For visualizing the circuit.
    quantumCircuit.draw(output="mpl", style=circuitStyle, cregbundle=False, fold=-1)

    plt.show()
