from codes.stabilizer_codes.stabilizer_code import StabilizerCode


class BitFlipCode(StabilizerCode):
    def __init__(self):
        super().__init__(numDataQubits=3, numAncillaQubits=2, numClassicalBits=2)

        # Example input: |+>.
        self.quantumCircuit.h(self.dataQubits[0])

        self.encode()
        self.error()
        self.measureSyndrome()
        self.correct()
        self.decode()

        # Grab statevector at output. May be used at other points of circuit.
        self.quantumCircuit.save_statevector()

    def encode(self):
        self.quantumCircuit.cx(self.dataQubits[0], self.dataQubits[1])
        self.quantumCircuit.cx(self.dataQubits[0], self.dataQubits[2])

    def error(self):
        """
        Bit-flip error on one of the data qubits.
        TODO: Look into implementing this more creatively.
        """
        # self.quantumCircuit.x(self.dataQubits[0])
        self.quantumCircuit.x(self.dataQubits[1])
        # self.quantumCircuit.x(self.dataQubits[2])

    def measureSyndrome(self):
        self.quantumCircuit.cx(self.dataQubits[0], self.ancillaQubits[0])
        self.quantumCircuit.cx(self.dataQubits[1], self.ancillaQubits[0])
        self.quantumCircuit.cx(self.dataQubits[0], self.ancillaQubits[1])
        self.quantumCircuit.cx(self.dataQubits[2], self.ancillaQubits[1])
        self.quantumCircuit.measure(self.ancillaQubits, self.classicalBits)

    def correct(self):
        """
        TODO: Implement more cleanly.
        """
        with self.quantumCircuit.if_test((self.classicalBits[0], 1)):
            with self.quantumCircuit.if_test((self.classicalBits[1], 1)):
                self.quantumCircuit.x(self.dataQubits[0])
        
        with self.quantumCircuit.if_test((self.classicalBits[0], 1)):
            with self.quantumCircuit.if_test((self.classicalBits[1], 0)):
                self.quantumCircuit.x(self.dataQubits[1])

        with self.quantumCircuit.if_test((self.classicalBits[0], 0)):
            with self.quantumCircuit.if_test((self.classicalBits[1], 1)):
                self.quantumCircuit.x(self.dataQubits[2])

    def decode(self):
        """
        TODO: Implement. Not difficult, but make the state-vector representation nicer.
        """
        pass
