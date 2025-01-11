"""
TODO: Add docstrings.
"""

from codes.stabilizer_codes import bit_flip_code
import helper


def main():
    bitFlipCode = bit_flip_code.BitFlipCode()
    helper.visualize(bitFlipCode.quantumCircuit)


if __name__ == "__main__":
    main()
