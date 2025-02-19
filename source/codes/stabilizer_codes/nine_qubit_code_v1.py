"""
Module containing the 9-qubit Shor code. 
Here, self.quantumCircuit.barrier() is included to improve circuit 
visualization. However, barriers may increase runtime. If faster 
execution is preferred, comment out barriers by changing all occurences 
within this module. It is recommended to run 'nine_qubit_code_v2' (see 
explanation in run.py docstring).
"""

from codes.stabilizer_codes.stabilizer_code import StabilizerCode


class ShorCode(StabilizerCode):
    def __init__(self):
        """
        Class initialization. Walks through error-correction steps
        to generate the Shor code circuit and output state.
        """

        super().__init__(numphysQubits=9, numAncillaQubits=8, numClassicalBits=8)
        self.generateCircuit()

    def generateCircuit(self):
        """
        Creates the Shor code circuit with error and stores the resultant
        output state vector.
        """

        # Example input: |1>.
        self.quantumCircuit.x(self.physQubits[0])

        self.encode()
        self.error()
        self.measureSyndrome()
        self.correct()
        self.decode()

        # Store output statevector.
        self.quantumCircuit.save_statevector()

    def encode(self):
        """Encoding process of the 9-qubit Shor code."""

        # Encoding for phase-flip code.
        self.quantumCircuit.cx(self.physQubits[0], self.physQubits[3])
        self.quantumCircuit.cx(self.physQubits[0], self.physQubits[6])

        self.quantumCircuit.h(self.physQubits[0])
        self.quantumCircuit.h(self.physQubits[3])
        self.quantumCircuit.h(self.physQubits[6])

        # Encoding for bit-flip code blocks.
        self.quantumCircuit.cx(self.physQubits[0], self.physQubits[1])
        self.quantumCircuit.cx(self.physQubits[0], self.physQubits[2])

        self.quantumCircuit.cx(self.physQubits[3], self.physQubits[4])
        self.quantumCircuit.cx(self.physQubits[3], self.physQubits[5])

        self.quantumCircuit.cx(self.physQubits[6], self.physQubits[7])
        self.quantumCircuit.cx(self.physQubits[6], self.physQubits[8])

    def error(self):
        """
        Represents the error. The Shor code supports correction of
        single-qubit x, y, and z errors.
        """

        self.quantumCircuit.z(self.physQubits[0])

    def measureSyndrome(self):
        """Measurement of stabilizers to generate the error syndrome."""

        self.quantumCircuit.barrier()

        # Stabilizer operators.
        # X-stabilizer operators for Z-error detection.
        self.quantumCircuit.h(self.physQubits)

        # Two loops for visual representation of stabilizer operators
        # consistent with thesis.
        for i in range(6):
            self.quantumCircuit.cx(self.physQubits[i], self.ancillaQubits[0])

        self.quantumCircuit.barrier()

        for i in range(6):
            self.quantumCircuit.cx(self.physQubits[i + 3], self.ancillaQubits[1])

        self.quantumCircuit.barrier()

        self.quantumCircuit.h(self.physQubits)

        # Z-stabilizer operators for X-error detection. Hard-coded for clarity.
        self.quantumCircuit.cx(self.physQubits[0], self.ancillaQubits[2])
        self.quantumCircuit.cx(self.physQubits[1], self.ancillaQubits[2])

        self.quantumCircuit.cx(self.physQubits[1], self.ancillaQubits[3])
        self.quantumCircuit.cx(self.physQubits[2], self.ancillaQubits[3])

        self.quantumCircuit.barrier()

        self.quantumCircuit.cx(self.physQubits[3], self.ancillaQubits[4])
        self.quantumCircuit.cx(self.physQubits[4], self.ancillaQubits[4])

        self.quantumCircuit.cx(self.physQubits[4], self.ancillaQubits[5])
        self.quantumCircuit.cx(self.physQubits[5], self.ancillaQubits[5])

        self.quantumCircuit.barrier()

        self.quantumCircuit.cx(self.physQubits[6], self.ancillaQubits[6])
        self.quantumCircuit.cx(self.physQubits[7], self.ancillaQubits[6])

        self.quantumCircuit.cx(self.physQubits[7], self.ancillaQubits[7])
        self.quantumCircuit.cx(self.physQubits[8], self.ancillaQubits[7])

        self.quantumCircuit.barrier()

        # Measurement.
        self.quantumCircuit.measure(self.ancillaQubits, self.classicalBits)

    def correct(self):
        """Correction of the error after acquiring the syndrome."""

        # Current SwitchCaseOp does not support cases with multiple-bit conditions,
        # such as 'case: a = 1 and b = 0 -> do...' Used 'if_test' instead.
        # Z-error correction.
        with self.quantumCircuit.if_test((self.classicalBits[0], 1)):
            with self.quantumCircuit.if_test((self.classicalBits[1], 0)):
                self.quantumCircuit.z(self.physQubits[0])

        with self.quantumCircuit.if_test((self.classicalBits[0], 1)):
            with self.quantumCircuit.if_test((self.classicalBits[1], 1)):
                self.quantumCircuit.z(self.physQubits[3])

        with self.quantumCircuit.if_test((self.classicalBits[0], 0)):
            with self.quantumCircuit.if_test((self.classicalBits[1], 1)):
                self.quantumCircuit.z(self.physQubits[6])

        self.quantumCircuit.barrier()

        # X-error correction.
        # Block 1.
        with self.quantumCircuit.if_test((self.classicalBits[2], 1)):
            with self.quantumCircuit.if_test((self.classicalBits[3], 0)):
                self.quantumCircuit.x(self.physQubits[0])

        with self.quantumCircuit.if_test((self.classicalBits[2], 1)):
            with self.quantumCircuit.if_test((self.classicalBits[3], 1)):
                self.quantumCircuit.x(self.physQubits[1])

        with self.quantumCircuit.if_test((self.classicalBits[2], 0)):
            with self.quantumCircuit.if_test((self.classicalBits[3], 1)):
                self.quantumCircuit.x(self.physQubits[2])

        self.quantumCircuit.barrier()

        # Block 2.
        with self.quantumCircuit.if_test((self.classicalBits[4], 1)):
            with self.quantumCircuit.if_test((self.classicalBits[5], 0)):
                self.quantumCircuit.x(self.physQubits[3])

        with self.quantumCircuit.if_test((self.classicalBits[4], 1)):
            with self.quantumCircuit.if_test((self.classicalBits[5], 1)):
                self.quantumCircuit.x(self.physQubits[4])

        with self.quantumCircuit.if_test((self.classicalBits[4], 0)):
            with self.quantumCircuit.if_test((self.classicalBits[5], 1)):
                self.quantumCircuit.x(self.physQubits[5])

        self.quantumCircuit.barrier()

        # Block 3.
        with self.quantumCircuit.if_test((self.classicalBits[6], 1)):
            with self.quantumCircuit.if_test((self.classicalBits[7], 0)):
                self.quantumCircuit.x(self.physQubits[6])

        with self.quantumCircuit.if_test((self.classicalBits[6], 1)):
            with self.quantumCircuit.if_test((self.classicalBits[7], 1)):
                self.quantumCircuit.x(self.physQubits[7])

        with self.quantumCircuit.if_test((self.classicalBits[6], 0)):
            with self.quantumCircuit.if_test((self.classicalBits[7], 1)):
                self.quantumCircuit.x(self.physQubits[8])

    def decode(self):
        """Decoding process of the 9-qubit Shor code."""

        self.quantumCircuit.barrier()

        # Decoding for phase-flip code.
        self.quantumCircuit.cx(self.physQubits[6], self.physQubits[8])
        self.quantumCircuit.cx(self.physQubits[6], self.physQubits[7])

        self.quantumCircuit.cx(self.physQubits[3], self.physQubits[5])
        self.quantumCircuit.cx(self.physQubits[3], self.physQubits[4])

        self.quantumCircuit.cx(self.physQubits[0], self.physQubits[2])
        self.quantumCircuit.cx(self.physQubits[0], self.physQubits[1])

        # Decoding for bit-flip code blocks.
        self.quantumCircuit.h(self.physQubits[6])
        self.quantumCircuit.h(self.physQubits[3])
        self.quantumCircuit.h(self.physQubits[0])

        self.quantumCircuit.cx(self.physQubits[0], self.physQubits[6])
        self.quantumCircuit.cx(self.physQubits[0], self.physQubits[3])
