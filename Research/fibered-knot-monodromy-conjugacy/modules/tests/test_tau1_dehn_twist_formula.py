"""Theoretical Route A tests for tau_1^theta.

These tests compare the production implementation ``tau1_theta`` with the
independent Dehn twist formula

    tau_1^theta(t_c) = -|c| wedge ell_2^theta(c).

Run with:
    sage -python test_tau1_dehn_twist_formula.py
"""

from itertools import combinations

from sage.all import QQ, identity_matrix, vector
from n3_monodromy import *


# Basis orders:
#   H:        X, Y, Z, W
#   Lambda^2: XY, XZ, XW, YZ, YW, ZW
#   Lambda^3: XYZ, XYW, XZW, YZW
_L2_PAIRS = tuple(combinations(range(H_Q.rank()), 2))
_L2_PAIR_INDEX = {
    pair: index for index, pair in enumerate(_L2_PAIRS)
}
_L3_TRIPLES = tuple(combinations(range(H_Q.rank()), 3))


def _wedge_H_L2(u, eta):
    r"""Return u wedge eta in Lambda^3 H_Q coordinates."""
    u = H_Q(u)
    if not isinstance(eta, L2Element):
        eta = L2Element(eta)

    def eta_coefficient(i, j):
        return eta[_L2_PAIR_INDEX[(i, j)]]

    return vector(
        QQ,
        [
            (
                u[i] * eta_coefficient(j, k)
                - u[j] * eta_coefficient(i, k)
                + u[k] * eta_coefficient(i, j)
            )
            for i, j, k in _L3_TRIPLES
        ],
    )


def _lambda3_to_HomHL2(trivector):
    r"""Use the symplectic form to embed Lambda^3 H_Q in Hom(H_Q,L2_Q)."""
    trivector = vector(QQ, trivector)
    if len(trivector) != len(_L3_TRIPLES):
        raise ValueError("trivector must have four coordinates")

    columns = []
    for h in H_Q.basis():
        # pairing[s] = <h,e_s> = h^T J e_s
        pairing = [
            sum(h[r] * J[r, s] for r in range(H_Q.rank()))
            for s in range(H_Q.rank())
        ]
        image = vector(QQ, L2_Q.rank())

        for coefficient, (i, j, k) in zip(
            trivector,
            _L3_TRIPLES,
        ):
            image[_L2_PAIR_INDEX[(j, k)]] += (
                coefficient * pairing[i]
            )
            image[_L2_PAIR_INDEX[(i, k)]] -= (
                coefficient * pairing[j]
            )
            image[_L2_PAIR_INDEX[(i, j)]] += (
                coefficient * pairing[k]
            )

        columns.append(image)

    return HomHL2Element(
        matrix_from_columns(columns, QQ)
    )


def _positive_twist_curves():
    r"""Return explicit curve words, independently of DehnTwist.ACTION."""
    return {
        "a": fg.x,
        "b": fg.Y * fg.w.conj(fg.z),
        "c": fg.z,
        "d": fg.w,
        "e": fg.bnd * fg.w,
        "f": fg.y,
    }


def _positive_twist_tau_from_formula(letter):
    r"""Compute tau_1^theta(t_c) = -|c| wedge ell_2^theta(c)."""
    curve = _positive_twist_curves()[letter]
    trivector = -_wedge_H_L2(
        homology(curve),
        ell2_theta(curve),
    )
    return _lambda3_to_HomHL2(trivector)


def _twist_tau_from_formula(letter):
    """Return the theoretical value for one positive or negative twist."""
    lower = letter.lower()
    positive_tau = _positive_twist_tau_from_formula(lower)

    if letter.islower():
        return positive_tau

    A = homology_action_matrix(MC(lower)).change_ring(QQ)
    return HomHL2Element(
        -(
            wedge_action_matrix(A).inverse()
            * positive_tau.as_matrix()
            * A
        )
    )


def _tau_from_formula(loops):
    """Compose theoretical generator values using the cocycle formula."""
    tau = HomHL2Element.zero()
    A = identity_matrix(QQ, H_Q.rank())

    for letter in loops:
        tau = tau + _twist_tau_from_formula(letter).transported_by(A)
        A = A * homology_action_matrix(MC(letter)).change_ring(QQ)

    return tau


def test_tau_positive_twists_from_Dehn_twist_formula():
    r"""Compare all six positive twists with -|c| wedge ell_2^theta(c)."""
    expected_homology = {
        "a": H_Q([1, 0, 0, 0]),
        "b": H_Q([0, -1, 0, 1]),
        "c": H_Q([0, 0, 1, 0]),
        "d": H_Q([0, 0, 0, 1]),
        "e": H_Q([0, 0, 0, 1]),
        "f": H_Q([0, 1, 0, 0]),
    }

    for letter, curve in _positive_twist_curves().items():
        assert H_Q(homology(curve)) == expected_homology[letter]
        assert _positive_twist_tau_from_formula(letter) == tau1_theta(
            MC(letter)
        )


def test_tau_formula_route_for_inverses_and_composites():
    r"""Compare Route A with tau1_theta after inverse and cocycle formulas."""
    generators = "aAbBcCdDeEfF"

    for letter in generators:
        assert _tau_from_formula(letter) == tau1_theta(MC(letter))

    for left in generators:
        for right in generators:
            loops = left + right
            assert _tau_from_formula(loops) == tau1_theta(MC(loops))

    for loops in ["DbCa", "Abcd", "abdD"]:
        assert _tau_from_formula(loops) == tau1_theta(MC(loops))


TESTS = [
    test_tau_positive_twists_from_Dehn_twist_formula,
    test_tau_formula_route_for_inverses_and_composites,
]


def run_all_tests():
    for test in TESTS:
        test()
        print(f"✓ {test.__name__}")
    print(f"\nAll {len(TESTS)} theoretical test groups passed.")


if __name__ == "__main__":
    run_all_tests()
