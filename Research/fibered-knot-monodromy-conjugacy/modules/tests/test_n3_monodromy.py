"""Regression tests for n3_monodromy.

Run with:
    sage -python test_n3_monodromy.py

The tests intentionally use plain ``assert`` statements, following the style
of the previous test suite.  No external test framework is required.
"""

from sage.all import (
    FreeGroup,
    QQ,
    ZZ,
    block_matrix,
    identity_matrix,
    matrix,
    vector,
    zero_matrix,
)

from n3_monodromy import *


def assert_raises(exception_types, function, *args, **kwargs):
    """Assert that function(*args, **kwargs) raises an expected exception."""
    try:
        function(*args, **kwargs)
    except exception_types:
        return
    raise AssertionError(
        f"Expected {exception_types!r} from {function!r}"
    )


def test_free_group_conjugation_method():
    assert fg.x.conj(fg.y) == fg.y * fg.x * (~fg.y)

    u = fg.x * fg.Y * fg.z
    v = fg.w * fg.x
    assert u.conj(v) == v * u * (~v)

    other_group = FreeGroup(1, "q")
    assert_raises(TypeError, fg.x.conj, other_group.gen(0))


def test_mapping_class_validation_reduction_and_equality():
    identity = MC("")

    assert_raises(TypeError, MC, 1)
    assert_raises(ValueError, MC, "ag")

    # 同じ簡約語の比較
    phi = MC("Db")
    psi = MC("Ca")
    assert phi * psi == MC("DbCa")
    assert MC("DbCa") != MC("CaDb")

    # 隣接する逆元対
    for letter in "abcdef":
        inverse = letter.swapcase()
        assert MC(letter + inverse) == identity
        assert MC(inverse + letter) == identity

    # 簡約後に新たな逆元対が隣接する場合
    assert MC("abBA") == identity
    assert MC("DaAd") == identity

    # 積の境界をまたぐ簡約
    assert MC("DbA") * MC("aCa") == MC("DbCa")

    theta = MC("DbCaEf")
    assert theta * theta.inv() == identity
    assert theta.inv() * theta == identity

    # 隣接する逆元でない部分は簡約しない
    assert MC("abAB").loops == "abAB"
    assert MC("a") != "a"


def test_homology_modules_and_basis():
    assert H_Z.rank() == 4
    assert H_Q.rank() == 4
    assert H_Z.base_ring() == ZZ
    assert H_Q.base_ring() == QQ

    expected = identity_matrix(ZZ, 4)
    for i, generator in enumerate(fg.BASIS):
        assert homology(generator) == expected.column(i)
        assert homology(~generator) == -expected.column(i)
        assert homology(generator).parent() == H_Z


def test_homology_is_a_homomorphism():
    u = fg.x * fg.y * fg.Z
    v = fg.z * fg.w * fg.X
    assert homology(u * v) == homology(u) + homology(v)
    assert homology(~u) == -homology(u)

    zero = H_Z.zero()
    assert homology(fg.comm(fg.x, fg.y)) == zero
    assert homology(fg.comm(fg.z, fg.w)) == zero
    assert homology(fg.bnd) == zero


def test_dehn_twist_validation_boundary_and_inverses_on_pi():
    assert_raises(ValueError, DT, "g")

    for lower, upper in zip("abcdef", "ABCDEF"):
        twist = DT(lower)
        twist_inverse = DT(upper)
        assert twist.twist(fg.bnd) == fg.bnd
        assert twist_inverse.twist(fg.bnd) == fg.bnd
        for generator in fg.BASIS:
            assert twist_inverse.twist(twist.twist(generator)) == generator
            assert twist.twist(twist_inverse.twist(generator)) == generator

    other_group = FreeGroup(1, "q")
    assert_raises(TypeError, DT("a").twist, other_group.gen(0))


def test_dehn_twist_is_a_homomorphism_on_words():
    twist = DT("b")
    u = fg.x * fg.Y * fg.z
    v = fg.w * fg.x
    assert twist.twist(u * v) == twist.twist(u) * twist.twist(v)
    assert twist.twist(~u) == ~twist.twist(u)


def test_homology_action_matrices():
    expected = {
        "a": [
            [1, 1, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1],
        ],
        "b": [
            [1, 0, 0, 0],
            [-1, 1, 1, 0],
            [0, 0, 1, 0],
            [1, 0, -1, 1],
        ],
        "c": [
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 1],
            [0, 0, 0, 1],
        ],
        "d": [
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, -1, 1],
        ],
        "e": [
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, -1, 1],
        ],
        "f": [
            [1, 0, 0, 0],
            [-1, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1],
        ],
    }

    for letter, rows in expected.items():
        action = homology_action_matrix(MC(letter))
        action_inverse = homology_action_matrix(MC(letter.upper()))
        assert action == matrix(ZZ, rows)
        assert action * action_inverse == identity_matrix(ZZ, 4)
        assert action_inverse * action == identity_matrix(ZZ, 4)


def test_all_generators_are_symplectic():
    assert Sp4_Z.invariant_form() == J
    for letter in "abcdefABCDEF":
        action = homology_action_matrix(MC(letter))
        assert action in Sp4_Z
        assert action.change_ring(QQ) in Sp4_Q
        assert action.transpose() * J * action == J


def test_mapping_class_composition_inverse_and_conjugation():
    mc1 = MC("Db")
    mc2 = MC("Ca")
    assert homology_action_matrix(mc1 * mc2) == (
        homology_action_matrix(mc1) * homology_action_matrix(mc2)
    )

    phi = MC("DbCa")
    assert (phi * phi.inv()).act_on_basis() == list(fg.BASIS)
    assert (phi.inv() * phi).act_on_basis() == list(fg.BASIS)

    a = MC("a")
    b = MC("b")
    assert a.conj(b).act_on_basis() == (b * a * b.inv()).act_on_basis()


def test_DbCa_regression_on_pi_and_H():
    phi = MC("DbCa")
    expected_images = [
        fg.x * fg.Y * fg.z * fg.w * fg.Z,
        fg.z
        * fg.W
        * fg.Z
        * fg.y
        * fg.z
        * fg.w
        * fg.Z
        * fg.x
        * fg.Y
        * fg.z
        * fg.w
        * fg.Z,
        fg.z * fg.W * fg.Z * fg.y * fg.z * fg.w,
        fg.Z * fg.Y * fg.z * fg.w * fg.Z,
    ]
    expected_action = matrix(
        ZZ,
        [
            [1, 1, 0, 0],
            [-1, 0, 1, -1],
            [0, 0, 1, -1],
            [1, 1, 0, 1],
        ],
    )

    assert phi.act_on_basis() == expected_images
    assert homology_action_matrix(phi) == expected_action
    assert expected_action in Sp4_Z


def test_matrix_from_columns_uses_column_convention():
    columns = [identity_matrix(ZZ, 4).column(i) for i in range(4)]
    assert matrix_from_columns(columns, ZZ) == identity_matrix(ZZ, 4)
    assert_raises(ValueError, matrix_from_columns, [])


def test_L2_modules_coordinates_and_arithmetic():
    assert L2_Z.rank() == 6
    assert L2_Q.rank() == 6
    assert L2_Z.base_ring() == ZZ
    assert L2_Q.base_ring() == QQ

    half = QQ(1) / 2
    eta = L2Element([half, 0, -1, 0, QQ(3) / 2, 0])
    nu = L2Element([half, 0, 1, 0, -QQ(3) / 2, 0])

    assert eta.coordinates.parent() == L2_Q
    assert eta.coordinates.is_immutable()
    assert len(eta) == 6
    assert tuple(eta) == tuple(eta.coordinates)
    assert eta[2] == -1
    assert eta + nu == L2Element([1, 0, 0, 0, 0, 0])
    assert eta - eta == L2Element.zero()
    assert eta.is_zero() is False
    assert L2Element.zero().is_zero() is True
    assert 2 * L2Element([half, 0, 0, 0, 0, 0]) == L2Element(
        [1, 0, 0, 0, 0, 0]
    )
    assert repr(eta) == "1/2 X∧Y - X∧W + 3/2 Y∧W"
    assert eta._repr_latex_() == "$\\frac{1}{2} X\\wedge Y - X\\wedge W + \\frac{3}{2} Y\\wedge W$"

    mutable_copy = eta.as_vector()
    assert mutable_copy.parent() == L2_Q
    assert not mutable_copy.is_immutable()
    assert_raises((TypeError, ValueError), L2Element, [0] * 5)


def test_wedge_bilinearity_antisymmetry_and_basis_order():
    X, Y, Z, W = H_Q.basis()
    expected_basis = (
        L2Element([1, 0, 0, 0, 0, 0]),
        L2Element([0, 1, 0, 0, 0, 0]),
        L2Element([0, 0, 1, 0, 0, 0]),
        L2Element([0, 0, 0, 1, 0, 0]),
        L2Element([0, 0, 0, 0, 1, 0]),
        L2Element([0, 0, 0, 0, 0, 1]),
    )
    actual_basis = (
        wedge(X, Y),
        wedge(X, Z),
        wedge(X, W),
        wedge(Y, Z),
        wedge(Y, W),
        wedge(Z, W),
    )
    assert actual_basis == expected_basis

    U = X + 2 * Y - Z
    V = -X + Z + W
    assert wedge(U, V) == -wedge(V, U)
    assert wedge(U, U).is_zero()
    assert wedge(U + X, V) == wedge(U, V) + wedge(X, V)
    assert wedge(3 * U, V) == 3 * wedge(U, V)


def test_ell2_generators_inverse_and_product_formula():
    half = QQ(1) / 2
    expected = (
        L2Element([half, 0, 0, 0, 0, 0]),
        L2Element([-half, 0, 0, 0, 0, 0]),
        L2Element([0, 0, 0, 0, 0, half]),
        L2Element([0, 0, 0, 0, 0, -half]),
    )
    assert tuple(ELL2_GENERATOR_VALUES[i] for i in range(1, 5)) == expected

    for generator, expected_value in zip(fg.BASIS, expected):
        assert ell2_theta(generator) == expected_value
        assert ell2_theta(~generator) == -expected_value

    g = fg.x * fg.Y * fg.z * fg.w * fg.X
    assert ell2_theta(~g) == -ell2_theta(g)

    u = fg.x * fg.Y * fg.z
    v = fg.w * fg.x * fg.Z
    assert ell2_theta(u * v) == (
        ell2_theta(u)
        + ell2_theta(v)
        + half * wedge(homology(u), homology(v))
    )


def test_boundary_ell2_is_omega():
    assert ell2_theta(fg.bnd) == L2Element([1, 0, 0, 0, 0, 1])


def _sample_hom_matrix():
    return matrix(
        QQ,
        [
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ],
    )


def test_HomHL2_modules_and_column_matrix_convention():
    assert HomHL2_Z.domain() == H_Z
    assert HomHL2_Z.codomain() == L2_Z
    assert HomHL2_Q.domain() == H_Q
    assert HomHL2_Q.codomain() == L2_Q

    column_matrix = _sample_hom_matrix()
    tau = HomHL2Element(column_matrix)

    assert tau.morphism.parent() == HomHL2_Q
    assert tau.morphism.matrix() == column_matrix.transpose()
    assert tau.as_matrix() == column_matrix

    reconstructed = HomHL2Element.from_morphism(tau.morphism)
    assert reconstructed == tau
    assert reconstructed.as_matrix() == column_matrix

    assert_raises(
        (TypeError, ValueError),
        HomHL2Element,
        zero_matrix(QQ, 5, 4),
    )


def test_HomHL2_evaluation_basis_arithmetic_and_display():
    column_matrix = _sample_hom_matrix()
    tau = HomHL2Element(column_matrix)
    element = H_Q([1, 2, 3, 4])

    assert tau(element) == L2Element([1, 2, 3, 4, 0, 0])
    assert tau + (-tau) == HomHL2Element.zero()
    assert tau - tau == HomHL2Element.zero()
    assert HomHL2Element.zero().is_zero()
    assert not tau.is_zero()
    assert 2 * tau == HomHL2Element(2 * column_matrix)
    assert tau * 2 == 2 * tau

    expected_basis_images = tuple(
        L2Element(column_matrix.column(i)) for i in range(H_Q.rank())
    )
    assert tau.on_basis() == expected_basis_images
    assert all(isinstance(image, L2Element) for image in tau.on_basis())
    assert repr(tau).startswith("HomHL2Element(X -> X∧Y")
    assert tau._latex_() == column_matrix._latex_()


def test_HomHL2_transport_action():
    tau = HomHL2Element(_sample_hom_matrix())
    A = homology_action_matrix(MC("Db")).change_ring(QQ)
    B = homology_action_matrix(MC("Ca")).change_ring(QQ)

    expected = HomHL2Element(
        wedge_action_matrix(A) * tau.as_matrix() * A.inverse()
    )
    assert tau.transported_by(A) == expected
    assert tau.transported_by(identity_matrix(QQ, 4)) == tau
    assert tau.transported_by(B).transported_by(A) == (
        tau.transported_by(A * B)
    )

    assert_raises(
        ValueError,
        tau.transported_by,
        zero_matrix(QQ, 4, 4),
    )
    assert_raises(
        ValueError,
        tau.transported_by,
        identity_matrix(QQ, 3),
    )


def test_L3_modules_coordinates_and_display():
    assert L3_Z.rank() == 4
    assert L3_Q.rank() == 4
    assert L3_Z.base_ring() == ZZ
    assert L3_Q.base_ring() == QQ

    half = QQ(1) / 2
    eta = L3Element([half, -1, 0, QQ(3) / 2])

    assert eta.coordinates.parent() == L3_Q
    assert eta.coordinates.is_immutable()
    assert eta.as_vector() == L3_Q([half, -1, 0, QQ(3) / 2])

    # Basis order: X∧Y∧Z, X∧Y∧W, X∧Z∧W, Y∧Z∧W.
    assert repr(L3Element(L3_Q.basis()[0])) == "X∧Y∧Z"
    assert repr(L3Element(L3_Q.basis()[1])) == "X∧Y∧W"
    assert repr(L3Element(L3_Q.basis()[2])) == "X∧Z∧W"
    assert repr(L3Element(L3_Q.basis()[3])) == "Y∧Z∧W"
    assert "X∧Y∧Z" in repr(eta)
    assert "Y∧Z∧W" in repr(eta)
    assert_raises((TypeError, ValueError), L3Element, [0] * 3)


def test_L3_and_HomHL2_conversion():
    # The two public conversions are inverse on Lambda^3 H_Q.
    samples = [
        L3Element([0, 0, 0, 0]),
        *(L3Element(v) for v in L3_Q.basis()),
        L3Element([QQ(1) / 2, -1, QQ(3) / 2, 2]),
    ]

    for value in samples:
        tau = value.to_HomHL2()
        assert isinstance(tau, HomHL2Element)
        assert tau.as_L3() == value
        assert tau.as_L3().to_HomHL2() == tau

    # A general element of Hom(H_Q, Lambda^2 H_Q) need not come from L3_Q.
    assert_raises(
        ValueError,
        HomHL2Element(_sample_hom_matrix()).as_L3,
    )

    # Boundary-preserving mapping classes do give Lambda^3-valued tau.
    for loops in [*"aAbBcCdDeEfF", "DbCa", "Abcd", "abdD"]:
        tau = tau1_theta(MC(loops))
        value = tau.as_L3()
        assert isinstance(value, L3Element)
        assert value.to_HomHL2() == tau


def test_N3_coordinate_space_and_accessors():
    assert N3_Q.rank() == L2_Q.rank() + H_Q.rank() == 10
    assert N3_Q.base_ring() == QQ

    xi = L2Element([1, 2, 3, 4, 5, 6])
    X = H_Q([7, 8, 9, 10])
    element = N3Element(xi, X)

    assert element.coordinates.parent() == N3_Q
    assert element.coordinates.is_immutable()
    assert element.xi == xi
    assert element.X == X
    assert element.X.parent() == H_Q
    assert element.X.is_immutable()
    assert element.as_pair() == (xi, X)
    assert isinstance(element.as_pair()[0], L2Element)
    assert repr(element.as_pair()[0]) == repr(xi)
    assert tuple(element) == (xi, X)
    assert not element.is_identity()
    assert N3Element.identity().is_identity()


def test_N3_group_law_and_word_coordinates():
    identity = N3Element.identity()
    assert N3Element.from_word(fg.F.one()) == identity

    u_word = fg.x * fg.Y * fg.z
    v_word = fg.w * fg.x * fg.Z * fg.y
    u = N3Element.from_word(u_word)
    v = N3Element.from_word(v_word)
    assert u * v == N3Element.from_word(u_word * v_word)
    assert identity * u == u
    assert u * identity == u

    g = N3Element.from_word(fg.x * fg.Y * fg.z * fg.w * fg.X * fg.y)
    assert ~g == g.inverse()
    assert g * ~g == identity
    assert ~g * g == identity

    a = N3Element.from_word(fg.x * fg.y)
    b = N3Element.from_word(fg.Z * fg.w * fg.x)
    c = N3Element.from_word(fg.y * fg.W)
    assert (a * b) * c == a * (b * c)


def test_N3_commutator_is_central_and_given_by_wedge():
    xi = L2Element([1, 0, 0, 0, 0, 0])
    eta = L2Element([0, 1, 0, 0, 0, 0])
    X = H_Q([1, 2, 0, -1])
    Y = H_Q([0, 1, 1, 0])
    u = N3Element(xi, X)
    v = N3Element(eta, Y)

    commutator = u * v * (~u) * (~v)
    assert commutator == N3Element(wedge(X, Y), H_Q.zero())

    central = N3Element(L2Element([0, 0, 1, 0, 0, 0]), H_Q.zero())
    assert central * u == u * central


def test_wedge_action_matrix_and_functoriality():
    identity = identity_matrix(QQ, 4)
    assert wedge_action_matrix(identity) == identity_matrix(QQ, 6)

    A = homology_action_matrix(MC("DbCa")).change_ring(QQ)
    B = homology_action_matrix(MC("aB")).change_ring(QQ)
    A2 = wedge_action_matrix(A)
    U = H_Q([1, 2, -1, 1])
    V = H_Q([-1, 1, 2, 0])
    assert L2Element(A2 * wedge(U, V).as_vector()) == wedge(A * U, A * V)
    assert wedge_action_matrix(A * B) == wedge_action_matrix(A) * wedge_action_matrix(B)


def test_tau_defining_relation():
    phi = MC("DbCa")
    A = homology_action_matrix(phi).change_ring(QQ)
    A2 = wedge_action_matrix(A)
    tau = tau1_theta(phi)

    assert isinstance(tau, HomHL2Element)
    assert tau.morphism.parent() == HomHL2_Q
    for generator, image in zip(fg.BASIS, phi.act_on_basis()):
        assert ell2_theta(image) == (
            tau(A * homology(generator))
            + L2Element(A2 * ell2_theta(generator).as_vector())
        )


def test_tau_generators_regression():
    zero = HomHL2Element.zero()
    assert tau1_theta(MC("")) == zero

    for letter in "aAcCdDfF":
        assert tau1_theta(MC(letter)) == zero

    expected_b = matrix(
        QQ,
        [
            [0, 0, -QQ(1) / 2, 0],
            [0, 0, 0, 0],
            [QQ(1) / 2, 0, 0, 0],
            [0, 0, QQ(1) / 2, 0],
            [0, QQ(1) / 2, 0, QQ(1) / 2],
            [QQ(1) / 2, 0, 0, 0],
        ],
    )
    assert tau1_theta(MC("b")) == HomHL2Element(expected_b)
    assert tau1_theta(MC("e")) != zero


def test_tau_cocycle_formula():
    phi = MC("Db")
    psi = MC("Ca")
    A_phi = homology_action_matrix(phi).change_ring(QQ)

    assert tau1_theta(phi * psi) == (
        tau1_theta(phi)
        + tau1_theta(psi).transported_by(A_phi)
    )


def test_AutN3_structure_matrix_and_action_formula():
    tau = HomHL2Element(_sample_hom_matrix())
    A = homology_action_matrix(MC("Db")).change_ring(QQ)
    automorphism = AutN3Element(tau, A)

    expected_matrix = block_matrix(
        QQ,
        [
            [wedge_action_matrix(A), tau.as_matrix() * A],
            [zero_matrix(QQ, 4, 6), A],
        ],
    )
    assert automorphism.morphism.parent() == EndN3_Q
    assert automorphism.as_matrix() == expected_matrix
    assert automorphism.morphism.matrix() == expected_matrix.transpose()

    element = N3Element(
        L2Element([1, -1, 0, 2, 0, 1]),
        H_Q([1, 0, -1, 2]),
    )
    expected_image = N3Element(
        L2Element(
            wedge_action_matrix(A) * element.xi.as_vector()
        )
        + tau(A * element.X),
        A * element.X,
    )
    assert automorphism(element) == expected_image
    assert_raises(TypeError, automorphism, element.coordinates)


def test_AutN3_validation_identity_composition_and_inverse():
    assert_raises(
        ValueError,
        AutN3Element,
        HomHL2Element.zero(),
        zero_matrix(QQ, 4, 4),
    )
    assert_raises(
        ValueError,
        AutN3Element,
        HomHL2Element.zero(),
        identity_matrix(QQ, 3),
    )

    R1 = rho3(MC("Db"))
    R2 = rho3(MC("Ca"))
    R12 = rho3(MC("DbCa"))

    assert isinstance(R1, AutN3Element)
    assert R1 * R2 == R12
    assert (R1 * R2).as_matrix() == R1.as_matrix() * R2.as_matrix()
    assert R1 * ~R1 == AutN3Element.identity()
    assert ~R1 * R1 == AutN3Element.identity()
    assert AutN3Element.identity().is_identity()
    assert not R1.is_identity()

    tau_as_L3, A = R1.as_L3_pair()
    assert isinstance(tau_as_L3, L3Element)
    assert tau_as_L3 == R1.tau.as_L3()
    assert A == R1.A

    general_automorphism = AutN3Element(
        HomHL2Element(_sample_hom_matrix()),
        identity_matrix(QQ, 4),
    )
    assert_raises(ValueError, general_automorphism.as_L3_pair)

    u = N3Element.from_word(fg.x * fg.Y * fg.z)
    assert (R1 * R2)(u) == R1(R2(u))


def test_AutN3_preserves_the_BCH_group_law():
    automorphism = rho3(MC("DbCa"))
    u = N3Element(
        L2Element([1, 0, -1, 2, 0, 0]),
        H_Q([1, 2, 0, -1]),
    )
    v = N3Element(
        L2Element([0, 1, 0, 0, -2, 1]),
        H_Q([-1, 0, 1, 1]),
    )

    assert automorphism(u * v) == automorphism(u) * automorphism(v)
    assert automorphism(~u) == ~automorphism(u)


def test_rho3_identity_and_DbCa_regression():
    identity = rho3(MC(""))
    assert identity == AutN3Element.identity()

    R = rho3(MC("DbCa"))
    expected_A = matrix(
        ZZ,
        [
            [1, 1, 0, 0],
            [-1, 0, 1, -1],
            [0, 0, 1, -1],
            [1, 1, 0, 1],
        ],
    )
    expected_tau = matrix(
        QQ,
        [
            [0, 0, -QQ(1) / 2, 0],
            [0, 0, 0, 0],
            [QQ(1) / 2, 0, 0, 0],
            [0, 0, QQ(1) / 2, 0],
            [0, QQ(1) / 2, 0, QQ(1) / 2],
            [QQ(1) / 2, 0, 0, 0],
        ],
    )
    assert R.A == expected_A
    assert R.A.base_ring() == QQ
    assert R.A.is_immutable()
    assert R.A2 == wedge_action_matrix(expected_A)
    assert R.A2.is_immutable()
    assert R.tau == HomHL2Element(expected_tau)


def test_rho3_on_words_and_boundary():
    sample_words = [
        fg.F.one(),
        *fg.BASIS,
        fg.x * fg.Y * fg.z,
        fg.w * fg.X * fg.y * fg.Z,
        fg.bnd,
    ]
    for loops in [*"aAbBcCdDeEfF", "DbCa", "Abcd", "abdD"]:
        phi = MC(loops)
        R = rho3(phi)
        images = phi.act_on_basis()

        for generator, image in zip(fg.BASIS, images):
            assert R(N3Element.from_word(generator)) == N3Element.from_word(image)

        # 自由群上の作用と N3 上の作用が一般の標本語でも一致する。
        twists = [DT(letter) for letter in phi.loops[::-1]]
        for word in sample_words:
            image = word
            for twist in twists:
                image = twist.twist(image)
            assert R(N3Element.from_word(word)) == N3Element.from_word(image)

        boundary = N3Element.from_word(fg.bnd)
        assert R(boundary) == boundary


def test_all_generator_tau_relations_and_rho_homomorphism():
    generators = "aAbBcCdDeEfF"

    for letter in generators:
        phi = MC(letter)
        A = homology_action_matrix(phi).change_ring(QQ)
        A2 = wedge_action_matrix(A)
        tau = tau1_theta(phi)

        for generator, image in zip(fg.BASIS, phi.act_on_basis()):
            assert ell2_theta(image) == (
                tau(A * homology(generator))
                + L2Element(A2 * ell2_theta(generator).as_vector())
            )

    # 全12生成元の順序つき二文字積で rho_3(phi psi)=rho_3(phi)rho_3(psi)。
    for left in generators:
        for right in generators:
            assert rho3(MC(left + right)) == rho3(MC(left)) * rho3(MC(right))


TESTS = [
    test_free_group_conjugation_method,
    test_mapping_class_validation_reduction_and_equality,
    test_homology_modules_and_basis,
    test_homology_is_a_homomorphism,
    test_dehn_twist_validation_boundary_and_inverses_on_pi,
    test_dehn_twist_is_a_homomorphism_on_words,
    test_homology_action_matrices,
    test_all_generators_are_symplectic,
    test_mapping_class_composition_inverse_and_conjugation,
    test_DbCa_regression_on_pi_and_H,
    test_matrix_from_columns_uses_column_convention,
    test_L2_modules_coordinates_and_arithmetic,
    test_wedge_bilinearity_antisymmetry_and_basis_order,
    test_ell2_generators_inverse_and_product_formula,
    test_boundary_ell2_is_omega,
    test_HomHL2_modules_and_column_matrix_convention,
    test_HomHL2_evaluation_basis_arithmetic_and_display,
    test_HomHL2_transport_action,
    test_L3_modules_coordinates_and_display,
    test_L3_and_HomHL2_conversion,
    test_N3_coordinate_space_and_accessors,
    test_N3_group_law_and_word_coordinates,
    test_N3_commutator_is_central_and_given_by_wedge,
    test_wedge_action_matrix_and_functoriality,
    test_tau_defining_relation,
    test_tau_generators_regression,
    test_tau_cocycle_formula,
    test_AutN3_structure_matrix_and_action_formula,
    test_AutN3_validation_identity_composition_and_inverse,
    test_AutN3_preserves_the_BCH_group_law,
    test_rho3_identity_and_DbCa_regression,
    test_rho3_on_words_and_boundary,
    test_all_generator_tau_relations_and_rho_homomorphism,
]


def run_all_tests():
    for test in TESTS:
        test()
        print(f"✓ {test.__name__}")
    print(f"\nAll {len(TESTS)} test groups passed.")


if __name__ == "__main__":
    run_all_tests()
