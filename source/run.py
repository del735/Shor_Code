"""
TODO: Add docstrings.
"""

from codes.stabilizer_codes import bit_flip_code, nine_qubit_code
import helper


def main():
    # bitFlipCode = bit_flip_code.BitFlipCode()
    # helper.visualize(bitFlipCode.quantumCircuit)

    shorCode = nine_qubit_code.ShorCode()
    helper.visualize(shorCode.quantumCircuit)

if __name__ == "__main__":
    main()
