"""
This module provides instructions and gates as abstract components for use
in other circuits.
"""

from qiskit import QuantumCircuit, QuantumRegister, AncillaRegister, ClassicalRegister


def shorStabilizers():
    """
    Implements stabilizer operators of the Shor code.
    """

    physQubits = QuantumRegister(9, "q")
    ancillaQubits = AncillaRegister(8, "a")
    classicalBits = ClassicalRegister(8, "c")
    quantumCircuit = QuantumCircuit(physQubits, ancillaQubits, classicalBits)

    # X-stabilizer operators for Z-error detection.
    quantumCircuit.h(physQubits)

    for i in range(6):
        quantumCircuit.cx(physQubits[i], ancillaQubits[0])
        quantumCircuit.cx(physQubits[i + 3], ancillaQubits[1])

    quantumCircuit.h(physQubits)

    # Z-stabilizer operators for X-error detection. Hard-coded for clarity.
    quantumCircuit.cx(physQubits[0], ancillaQubits[2])
    quantumCircuit.cx(physQubits[1], ancillaQubits[2])

    quantumCircuit.cx(physQubits[1], ancillaQubits[3])
    quantumCircuit.cx(physQubits[2], ancillaQubits[3])

    quantumCircuit.cx(physQubits[3], ancillaQubits[4])
    quantumCircuit.cx(physQubits[4], ancillaQubits[4])

    quantumCircuit.cx(physQubits[4], ancillaQubits[5])
    quantumCircuit.cx(physQubits[5], ancillaQubits[5])

    quantumCircuit.cx(physQubits[6], ancillaQubits[6])
    quantumCircuit.cx(physQubits[7], ancillaQubits[6])

    quantumCircuit.cx(physQubits[7], ancillaQubits[7])
    quantumCircuit.cx(physQubits[8], ancillaQubits[7])

    # Instruction label contains spaces because the current Qiskit version
    # has width-crowding issues with instructions in larger circuits.
    return quantumCircuit.to_instruction(label="                Stabs             ")


def shorCorrection():
    """
    Implements correction for the Shor code.
    """

    physQubits = QuantumRegister(9, "q")
    ancillaQubits = AncillaRegister(8, "a")
    classicalBits = ClassicalRegister(8, "c")
    quantumCircuit = QuantumCircuit(physQubits, ancillaQubits, classicalBits)

    # SwitchCaseOp does not support cases with multiple-bit conditions,
    # such as 'case: a = 1 and b = 0 -> do...' As a workaround, 'c_if' is used
    # in combination with a switch statement.
    # Z-error correction.
    with quantumCircuit.switch(classicalBits[0]) as case:
        with case(1):
            quantumCircuit.z(physQubits[3]).c_if(classicalBits[1], 1)
            quantumCircuit.z(physQubits[0]).c_if(classicalBits[1], 0)
        with case(0):
            quantumCircuit.z(physQubits[6]).c_if(classicalBits[1], 1)

    # X-error correction.
    with quantumCircuit.switch(classicalBits[2]) as case:
        with case(1):
            quantumCircuit.x(physQubits[1]).c_if(classicalBits[3], 1)
            quantumCircuit.x(physQubits[0]).c_if(classicalBits[3], 0)
        with case(0):
            quantumCircuit.x(physQubits[2]).c_if(classicalBits[3], 1)

    with quantumCircuit.switch(classicalBits[4]) as case:
        with case(1):
            quantumCircuit.x(physQubits[4]).c_if(classicalBits[5], 1)
            quantumCircuit.x(physQubits[3]).c_if(classicalBits[5], 0)
        with case(0):
            quantumCircuit.x(physQubits[5]).c_if(classicalBits[5], 1)

    with quantumCircuit.switch(classicalBits[6]) as case:
        with case(1):
            quantumCircuit.x(physQubits[7]).c_if(classicalBits[7], 1)
            quantumCircuit.x(physQubits[6]).c_if(classicalBits[7], 0)
        with case(0):
            quantumCircuit.x(physQubits[8]).c_if(classicalBits[7], 1)

    # Instruction label contains spaces because the current Qiskit version
    # has width-crowding issues with instructions in larger circuits.
    return quantumCircuit.to_instruction(label="                Corr              ")
