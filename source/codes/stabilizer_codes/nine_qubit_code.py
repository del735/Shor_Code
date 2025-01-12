from qiskit import QuantumCircuit
from codes.stabilizer_codes.stabilizer_code import StabilizerCode
from custom_gates import shorStabilizers

class ShorCode(StabilizerCode):
    def __init__(self):
        super().__init__(numDataQubits=9, numAncillaQubits=8, numClassicalBits=8)

        # Example input: |+>.
        # self.quantumCircuit.h(self.dataQubits[0])

        self.encode()
        self.error()
        self.measureSyndrome()
        self.correct()
        self.decode()

        # Grab statevector at output. May be used at other points of circuit.
        self.quantumCircuit.save_statevector()

    def encode(self):
        # Encoding phase-flip code.
        self.quantumCircuit.cx(self.dataQubits[0], self.dataQubits[3])
        self.quantumCircuit.cx(self.dataQubits[0], self.dataQubits[6])
        
        self.quantumCircuit.h(self.dataQubits[0])
        self.quantumCircuit.h(self.dataQubits[3])
        self.quantumCircuit.h(self.dataQubits[6])

        # Bit-flip code blocks.
        self.quantumCircuit.cx(self.dataQubits[0], self.dataQubits[1])
        self.quantumCircuit.cx(self.dataQubits[0], self.dataQubits[2])

        self.quantumCircuit.cx(self.dataQubits[3], self.dataQubits[4])
        self.quantumCircuit.cx(self.dataQubits[3], self.dataQubits[5])

        self.quantumCircuit.cx(self.dataQubits[6], self.dataQubits[7])
        self.quantumCircuit.cx(self.dataQubits[6], self.dataQubits[8])

    def error(self):
        self.quantumCircuit.x(self.dataQubits[8])
        self.quantumCircuit.barrier()

    def measureSyndrome(self):
        
        # X-stabilizer operators for Z-error detection.
        self.quantumCircuit.h(self.dataQubits)

        for i in range(6):
            self.quantumCircuit.cx(self.dataQubits[i], self.ancillaQubits[0])
        
        self.quantumCircuit.barrier()

        for i in range(6):
            self.quantumCircuit.cx(self.dataQubits[i+3], self.ancillaQubits[1])
        
        self.quantumCircuit.barrier()
        
        self.quantumCircuit.h(self.dataQubits)

        self.quantumCircuit.barrier()

        # Z-stabilizer operators for X-error detection.
        self.quantumCircuit.cx(self.dataQubits[0], self.ancillaQubits[2])
        self.quantumCircuit.cx(self.dataQubits[1], self.ancillaQubits[2])

        self.quantumCircuit.cx(self.dataQubits[1], self.ancillaQubits[3])
        self.quantumCircuit.cx(self.dataQubits[2], self.ancillaQubits[3])

        self.quantumCircuit.cx(self.dataQubits[3], self.ancillaQubits[4])
        self.quantumCircuit.cx(self.dataQubits[4], self.ancillaQubits[4])

        self.quantumCircuit.cx(self.dataQubits[4], self.ancillaQubits[5])
        self.quantumCircuit.cx(self.dataQubits[5], self.ancillaQubits[5])

        self.quantumCircuit.cx(self.dataQubits[6], self.ancillaQubits[6])
        self.quantumCircuit.cx(self.dataQubits[7], self.ancillaQubits[6])

        self.quantumCircuit.cx(self.dataQubits[7], self.ancillaQubits[7])
        self.quantumCircuit.cx(self.dataQubits[8], self.ancillaQubits[7])

        self.quantumCircuit.barrier()

        # Measurement.
        self.quantumCircuit.measure(self.ancillaQubits, self.classicalBits)

    def correct(self):
        self.quantumCircuit.barrier()
        
        # Z-Correction.
        with self.quantumCircuit.if_test((self.classicalBits[0], 1)):
            with self.quantumCircuit.if_test((self.classicalBits[1], 0)):
                self.quantumCircuit.z(self.dataQubits[0])
        
        with self.quantumCircuit.if_test((self.classicalBits[0], 1)):
            with self.quantumCircuit.if_test((self.classicalBits[1], 1)):
                self.quantumCircuit.z(self.dataQubits[3])

        with self.quantumCircuit.if_test((self.classicalBits[0], 0)):
            with self.quantumCircuit.if_test((self.classicalBits[1], 1)):
                self.quantumCircuit.z(self.dataQubits[6])

        self.quantumCircuit.barrier()

        # X-Correction.
        # Block 1.
        with self.quantumCircuit.if_test((self.classicalBits[2], 1)):
            with self.quantumCircuit.if_test((self.classicalBits[3], 0)):
                self.quantumCircuit.x(self.dataQubits[0])

        with self.quantumCircuit.if_test((self.classicalBits[2], 1)):
            with self.quantumCircuit.if_test((self.classicalBits[3], 1)):
                self.quantumCircuit.x(self.dataQubits[1])

        with self.quantumCircuit.if_test((self.classicalBits[2], 0)):
            with self.quantumCircuit.if_test((self.classicalBits[3], 1)):
                self.quantumCircuit.x(self.dataQubits[2])

        self.quantumCircuit.barrier()

        # Block 2.
        with self.quantumCircuit.if_test((self.classicalBits[4], 1)):
            with self.quantumCircuit.if_test((self.classicalBits[5], 0)):
                self.quantumCircuit.x(self.dataQubits[3])

        with self.quantumCircuit.if_test((self.classicalBits[4], 1)):
            with self.quantumCircuit.if_test((self.classicalBits[5], 1)):
                self.quantumCircuit.x(self.dataQubits[4])

        with self.quantumCircuit.if_test((self.classicalBits[4], 0)):
            with self.quantumCircuit.if_test((self.classicalBits[5], 1)):
                self.quantumCircuit.x(self.dataQubits[5])
        
        self.quantumCircuit.barrier()

        # Block 3.
        with self.quantumCircuit.if_test((self.classicalBits[6], 1)):
            with self.quantumCircuit.if_test((self.classicalBits[7], 0)):
                self.quantumCircuit.x(self.dataQubits[6])

        with self.quantumCircuit.if_test((self.classicalBits[6], 1)):
            with self.quantumCircuit.if_test((self.classicalBits[7], 1)):
                self.quantumCircuit.x(self.dataQubits[7])

        with self.quantumCircuit.if_test((self.classicalBits[6], 0)):
            with self.quantumCircuit.if_test((self.classicalBits[7], 1)):
                self.quantumCircuit.x(self.dataQubits[8])

    def decode(self):
        pass
