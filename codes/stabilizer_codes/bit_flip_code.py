from codes.stabilizer_codes.stabilizer_code import StabilizerCode


class BitFlipCode(StabilizerCode):
    def __init__(self):
        super().__init__(numDataQubits=3, numAncillaQubits=2, numClassicalBits=2)

        # Example input: |+>.
        self.quantumCircuit.h(self.dataQubits[0])

        self.encode()
        self.error()
        self.measureSyndrome()
        self.decode()

        # Grab statevector at output. May be used at other points of circuit.
        self.quantumCircuit.save_statevector()

    def encode(self):
        self.quantumCircuit.cx(self.dataQubits[0], self.dataQubits[1])
        self.quantumCircuit.cx(self.dataQubits[0], self.dataQubits[2])

    def error(self):
        self.quantumCircuit.x(self.dataQubits[0])

    def measureSyndrome(self):
        self.quantumCircuit.cx(self.dataQubits[0], self.ancillaQubits[0])
        self.quantumCircuit.cx(self.dataQubits[1], self.ancillaQubits[0])
        self.quantumCircuit.cx(self.dataQubits[0], self.ancillaQubits[1])
        self.quantumCircuit.cx(self.dataQubits[2], self.ancillaQubits[1])
        self.quantumCircuit.measure(self.ancillaQubits, self.classicalBits)

    def decode(self):
        self.quantumCircuit.x(self.dataQubits[0]).c_if(self.classicalBits, 1)
        self.quantumCircuit.x(self.dataQubits[1]).c_if(self.classicalBits[0], 1)
        self.quantumCircuit.x(self.dataQubits[2]).c_if(self.classicalBits[1], 1)
