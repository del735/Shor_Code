"""
This module provides instructions and gates as abstract components for use
in other circuits.
"""

from qiskit import QuantumCircuit, QuantumRegister, AncillaRegister, ClassicalRegister


def shorStabilizers():
    """
    Implements stabilizer operators of the Shor code.
    """

    dataQubits = QuantumRegister(9, "q")
    ancillaQubits = AncillaRegister(8, "a")
    classicalBits = ClassicalRegister(8, "c")
    quantumCircuit = QuantumCircuit(dataQubits, ancillaQubits, classicalBits)

    # X-stabilizer operators for Z-error detection.
    quantumCircuit.h(dataQubits)

    for i in range(6):
        quantumCircuit.cx(dataQubits[i], ancillaQubits[0])
        quantumCircuit.cx(dataQubits[i + 3], ancillaQubits[1])

    quantumCircuit.h(dataQubits)

    # Z-stabilizer operators for X-error detection. Hard-coded for clarity.
    quantumCircuit.cx(dataQubits[0], ancillaQubits[2])
    quantumCircuit.cx(dataQubits[1], ancillaQubits[2])

    quantumCircuit.cx(dataQubits[1], ancillaQubits[3])
    quantumCircuit.cx(dataQubits[2], ancillaQubits[3])

    quantumCircuit.cx(dataQubits[3], ancillaQubits[4])
    quantumCircuit.cx(dataQubits[4], ancillaQubits[4])

    quantumCircuit.cx(dataQubits[4], ancillaQubits[5])
    quantumCircuit.cx(dataQubits[5], ancillaQubits[5])

    quantumCircuit.cx(dataQubits[6], ancillaQubits[6])
    quantumCircuit.cx(dataQubits[7], ancillaQubits[6])

    quantumCircuit.cx(dataQubits[7], ancillaQubits[7])
    quantumCircuit.cx(dataQubits[8], ancillaQubits[7])

    # Instruction label contains spaces because the current Qiskit version
    # has width-crowding issues with instructions in larger circuits.
    return quantumCircuit.to_instruction(label="                Stabs             ")


def shorCorrection():
    """
    Implements correction for the Shor code.
    """

    dataQubits = QuantumRegister(9, "q")
    ancillaQubits = AncillaRegister(8, "a")
    classicalBits = ClassicalRegister(8, "c")
    quantumCircuit = QuantumCircuit(dataQubits, ancillaQubits, classicalBits)

    # Z-error correction.
    with quantumCircuit.switch(classicalBits[0]) as case:
        with case(1):
            quantumCircuit.z(dataQubits[3]).c_if(classicalBits[1], 1)
            quantumCircuit.z(dataQubits[0]).c_if(classicalBits[1], 0)
        with case(0):
            quantumCircuit.z(dataQubits[6]).c_if(classicalBits[1], 1)

    # X-error correction.
    with quantumCircuit.switch(classicalBits[2]) as case:
        with case(1):
            quantumCircuit.x(dataQubits[1]).c_if(classicalBits[3], 1)
            quantumCircuit.x(dataQubits[0]).c_if(classicalBits[3], 0)
        with case(0):
            quantumCircuit.x(dataQubits[2]).c_if(classicalBits[3], 1)

    with quantumCircuit.switch(classicalBits[4]) as case:
        with case(1):
            quantumCircuit.x(dataQubits[4]).c_if(classicalBits[5], 1)
            quantumCircuit.x(dataQubits[3]).c_if(classicalBits[5], 0)
        with case(0):
            quantumCircuit.x(dataQubits[5]).c_if(classicalBits[5], 1)

    with quantumCircuit.switch(classicalBits[6]) as case:
        with case(1):
            quantumCircuit.x(dataQubits[7]).c_if(classicalBits[7], 1)
            quantumCircuit.x(dataQubits[6]).c_if(classicalBits[7], 0)
        with case(0):
            quantumCircuit.x(dataQubits[8]).c_if(classicalBits[7], 1)

    # Instruction label contains spaces because the current Qiskit version
    # has width-crowding issues with instructions in larger circuits.
    return quantumCircuit.to_instruction(label="                Corr              ")
