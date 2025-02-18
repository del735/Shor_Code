# Nine-Qubit Shor Code
Implementation of the nine-qubit Shor quantum error correction code.

This program uses Qiskit to construct and execute quantum circuits.
Additionally, Qiskit-Aer is required to simulate quantum circuits and
retrieve the statevector with explicit state saving. LaTeX is needed to
represent mathematical expressions in circuits and Matplotlib figures.

## Required Dependencies
- **Qiskit** - For building and running quantum circuits.
- **Qiskit-Aer** - For statevector simulation and measurement processing.
- **Matplotlib** - For visualizing circuits and statevectors.
## Further Requirement
- **LaTeX** - Needed for rendering mathematical expressions.
## Usage
Execute `run.py` to start the program.

In `nine_qubit_code_v2.py` (or `nine_qubit_code_v1.py`, depending on use),  
edit `self.quantumCircuit.z(self.dataQubits[0])` in the `error()` function 
to modify the location and type of error. The Shor code corrects single-qubit 
X, Y, and Z errors. The `dataQubits` indices range from 0 to 8, corresponding 
to data qubits q_0 to q_8, respectively.

Note that single-qubit Y errors introduce a global phase (i or -i). Since global 
phases do not affect measurement probabilities, the logical information is  
still recovered as intended.

To change the input state, which is set to |1⟩ by default, modify 
`self.quantumCircuit.x(self.dataQubits[0])` in the `__init__` method. 
