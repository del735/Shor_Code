"""
Module containing the 9-qubit Shor code using abstract 
gates/instructions.
"""

from codes.stabilizer_codes.stabilizer_code import StabilizerCode
from custom_gates import shorStabilizers, shorCorrection


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

        # Encodig for bit-flip code blocks.
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

        # Stabilizer operators displayed as a single instruction.
        self.quantumCircuit.append(shorStabilizers(), range(17), range(8))

        # Measurement.
        self.quantumCircuit.measure(self.ancillaQubits, self.classicalBits)

    def correct(self):
        """Correction of the error after acquiring the syndrome."""

        # Correction process displayed as a single instruction.
        self.quantumCircuit.append(shorCorrection(), range(17), range(8))

    def decode(self):
        """Decoding process of the 9-qubit Shor code."""

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
