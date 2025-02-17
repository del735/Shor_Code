"""
Module for running the 9-qubit Shor error correction code.

There are two implementations:
- v2: Uses gate/instruction abstractions for cleaner circuit visualization
  but relies on the `c_if` function, which is deprecated (though it will work
  in all versions until the release of Qiskit 2). The current non-deprecated
  `IfElseOp` is not supported in instructions.
- v1: Compatible with future Qiskit releases, but circuit visualization
  is not prioritized. Adding barriers improves visualization but introduces
  runtime overhead.

Current recommendation: Use v2, but migrate to v1 when Qiskit 2 removes
`c_if` support. Alternatively, continue using Qiskit 1 to run v2.
"""

from codes.stabilizer_codes import nine_qubit_code_v1, nine_qubit_code_v2
import helper


def main():
    """Start the error-correction process."""

    # shorCode = nine_qubit_code_v1.ShorCode()
    # helper.visualize(shorCode.quantumCircuit)

    shorCode = nine_qubit_code_v2.ShorCode()
    helper.visualize(shorCode.quantumCircuit)


if __name__ == "__main__":
    main()
