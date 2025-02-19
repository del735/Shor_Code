"""
Module containing an abstract class representing general stabilizer codes.
"""

from abc import ABC, abstractmethod
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, AncillaRegister


class StabilizerCode(ABC):
    def __init__(self, numphysQubits, numAncillaQubits, numClassicalBits):
        self.physQubits = QuantumRegister(numphysQubits, "q")
        self.ancillaQubits = AncillaRegister(numAncillaQubits, "a")
        self.classicalBits = ClassicalRegister(numClassicalBits, "c")
        self.quantumCircuit = QuantumCircuit(
            self.physQubits, self.ancillaQubits, self.classicalBits
        )

    @abstractmethod
    def generateCircuit(self):
        raise NotImplementedError()

    @abstractmethod
    def encode(self):
        raise NotImplementedError()

    @abstractmethod
    def error(self):
        raise NotImplementedError()

    @abstractmethod
    def measureSyndrome(self):
        raise NotImplementedError()

    @abstractmethod
    def correct(self):
        raise NotImplementedError()

    @abstractmethod
    def decode(self):
        raise NotImplementedError()
