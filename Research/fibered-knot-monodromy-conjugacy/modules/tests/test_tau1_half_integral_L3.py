"""Theoretical verification of the half-integral Lambda^3 target.

This file verifies

    tau_1^theta(MC word) in (1/2) Lambda^3 H_Z

by a finite generator-and-lattice-closure argument:

the argument applies to every MappingClass word by the cocycle formula.

Run with:
    sage -python test_tau1_half_integral_L3.py
"""

from sage.all import QQ, ZZ

from n3_monodromy import *


GENERATORS = "aAbBcCdDeEfF"


def _is_in_half_integral_L3(value):
    r"""Return whether value belongs to (1/2) Lambda^3 H_Z."""
    return (
        isinstance(value, L3Element)
        and all(QQ(2 * coefficient) in ZZ for coefficient in value)
    )


def _as_half_integral_L3(tau, context):
    """Convert tau to L3 and assert half-integrality with context."""
    try:
        value = tau.as_L3()
    except ValueError as error:
        raise AssertionError(
            f"tau_1^theta({context}) does not lie in Lambda^3 H_Q"
        ) from error

    assert _is_in_half_integral_L3(value), (
        f"tau_1^theta({context}) is not in "
        "(1/2) Lambda^3 H_Z: "
        f"{value}"
    )
    return value


def test_all_MC_words_by_generators_and_lattice_closure():
    r"""Verify the finite data implying the claim for every MC word.

    Let L = (1/2) Lambda^3 H_Z.  The cocycle formula is

        tau(phi psi) = tau(phi) + phi . tau(psi).

    The test checks:

    - tau(g) lies in L for every positive and negative generator g;
    - every generator action preserves L, checked on a basis of L.

    Since the twelve generators generate every MC word and L is additive,
    induction on word length gives tau(phi) in L for every MC word phi.
    """
    half = QQ(1) / 2
    half_lattice_basis = tuple(
        L3Element(half * basis_vector)
        for basis_vector in L3_Q.basis()
    )

    for letter in GENERATORS:
        _as_half_integral_L3(
            tau1_theta(MC(letter)),
            repr(letter),
        )

        A = homology_action_matrix(MC(letter)).change_ring(QQ)

        for basis_element in half_lattice_basis:
            transported = (
                basis_element
                .to_HomHL2()
                .transported_by(A)
                .as_L3()
            )
            assert _is_in_half_integral_L3(transported), (
                f"Generator {letter!r} does not preserve "
                "(1/2) Lambda^3 H_Z"
            )


TESTS = [
    test_all_MC_words_by_generators_and_lattice_closure,
]


def run_all_tests():
    for test in TESTS:
        test()
        print(f"✓ {test.__name__}")
    print(f"\nAll {len(TESTS)} half-integral L3 test groups passed.")


if __name__ == "__main__":
    run_all_tests()
