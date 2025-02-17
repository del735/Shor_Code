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
edit `self.quantumCircuit.z(self.dataQubits[0])` to change where and what  
type of error occurs. The Shor code corrects single-qubit X, Y, and Z errors.  
The index ranges from 0 to 8, corresponding to data qubits q_0 to q_8, respectively.  

Note that single-qubit Y errors introduce a -i global phase. Since global  
phases do not affect measurement probabilities, the logical information is  
still recovered as intended.

