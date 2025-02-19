# **Nine-Qubit Shor Code**  
An implementation of the nine-qubit Shor quantum error correction code using Qiskit.

---

## **Required Dependencies**  

The following packages are required to run this program:  
### **Quantum Computing & Simulation**  
- **[Qiskit](https://github.com/Qiskit/qiskit)** – For building and running quantum circuits.  
- **[Qiskit-Aer](https://github.com/Qiskit/qiskit-aer)** – To retrieve the statevector of circuits that include measurement operations.
### **Visualization & LaTeX Support**  
- **[Matplotlib](https://github.com/matplotlib/matplotlib)** – Used for visualizing circuits and quantum states.  
- **[pylatexenc](https://github.com/phfaist/pylatexenc)** – Required for rendering mathematical expressions in Matplotlib.  

The required dependencies can be installed through `pip`:  

```bash
pip install qiskit 
pip install qiskit-aer 
pip install matplotlib 
pip install pylatexenc
```

It is [recommended](https://docs.quantum.ibm.com/guides/install-qiskit) to use a Python virtual environment to prevent problems between Qiskit and other applications.

---

## Usage
Execute `run.py` to start the program.

In `nine_qubit_code_v2.py` (or `nine_qubit_code_v1.py`, depending on use),
edit `self.quantumCircuit.z(self.physQubits[0])` in the `error` function
to modify the location and type of error. The Shor code corrects single-qubit
$X, Y$, and $Z$ errors. The `physQubits` indices range from 0 to 8, corresponding
to data qubits $q_0$ to $q_8$, respectively.

Note that single-qubit $Y$ errors introduce a global phase ($i$ or $-i$). Since global
phases do not affect measurement probabilities, the logical information is
still recovered as intended.

To change the input $q_0$, which is set to $|1\rangle$ by default, modify
`self.quantumCircuit.x(self.physQubits[0])` in the `generateCircuit` method. The decoded
qubit $q_0$ will match its input despite single-qubit error. Measurement behavior 
remains consistent as well.

---

## Output Example
For input $H|0\rangle$, and a single-qubit $Y$-error on $q_4$, the output below illustrates successful error correction:

![Screenshot from 2025-02-19 20-46-20](https://github.com/user-attachments/assets/76b32e9a-ae1a-4f6b-870d-c31b4bcfc513)

