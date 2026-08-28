"""Genus-two monodromy calculations on H and N_3.

Value classes:
    L2      -- an element of Lambda^2 H;
    HomHL2  -- an element of Hom(H, Lambda^2 H);
    N3      -- an element of Lambda^2 H semidirect H;
    AutN3   -- an automorphism represented by (tau, A).

The maps ell_2^theta, tau_1^theta, and rho_3 remain module-level functions.
Basis conventions:
    H: (X, Y, Z, W);
    Lambda^2 H: (X^Y, X^Z, X^W, Y^Z, Y^W, Z^W).

MC("uv") acts as u o v, so the rightmost twist acts first.
This module must be imported in a SageMath Python environment.
"""

from functools import reduce
from itertools import combinations

from sage.all import (
    FreeGroup,
    FreeModule,
    Hom,
    QQ,
    ZZ,
    Sp,
    identity_matrix,
    latex,
    matrix,
    vector,
    zero_matrix,
    block_matrix,
)


# ---------------------------------------------------------------------------
# Fundamental group and mapping classes
# ---------------------------------------------------------------------------

class fundamentalGroup:
    """The rank-four free group and its distinguished words."""

    F = FreeGroup(4, "x,y,z,w")
    x, y, z, w = F.generators()
    X, Y, Z, W = ~x, ~y, ~z, ~w
    BASIS = (x, y, z, w)

    @classmethod
    def comm(cls, u, v):
        """Return the commutator u v u^-1 v^-1."""
        if u.parent() != cls.F or v.parent() != cls.F:
            raise TypeError("u and v must be elements of fg.F")
        return u * v * (~u) * (~v)

fg = fundamentalGroup
fg.bnd = fg.comm(fg.x, fg.y) * fg.comm(fg.z, fg.w)

def conj(self, v):
    """Return v self v^-1."""
    if v.parent() != self.parent():
        raise TypeError("v must be elements of fg.F")
    return v * self * (~v)
FreeGroupElement = type(fg.x)    
FreeGroupElement.conj = conj    


class DehnTwist(fg):
    """One of the twelve Humphries twist generators aAbBcCdDeEfF."""

    GEN_NAMES = {1: "x", 2: "y", 3: "z", 4: "w"}

    x, y, z, w = fg.x, fg.y, fg.z, fg.w
    X, Y, Z, W = fg.X, fg.Y, fg.Z, fg.W
    bnd = fg.bnd

    a_w = x
    b_w = Y * fg.w.conj(z)
    c_w = z
    d_w = w
    e_w = bnd * w
    f_w = y

    ACTION = {
        "a": {"y": y * a_w},
        "A": {"y": y * ~a_w},
        "b": {
            "x": x * b_w,
            "y": fg.y.conj(~b_w),
            "z": ~b_w * z,
        },
        "B": {
            "x": x * ~b_w,
            "y": fg.y.conj(b_w),
            "z": b_w * z,
        },
        "c": {"w": w * c_w},
        "C": {"w": w * ~c_w},
        "d": {"z": z * ~d_w},
        "D": {"z": z * d_w},
        "e": {
            "x": fg.x.conj(~e_w),
            "y": fg.y.conj(~e_w),
            "z": ~e_w * z,
        },
        "E": {
            "x": fg.x.conj(e_w),
            "y": fg.y.conj(e_w),
            "z": e_w * z,
        },
        "f": {"x": x * ~f_w},
        "F": {"x": x * f_w},
    }

    def __init__(self, twisting_loop: str):
        if twisting_loop not in self.ACTION:
            raise ValueError(
                f"Unknown Dehn twist generator: {twisting_loop!r}"
            )
        self.loop = twisting_loop
        self.act = self.ACTION[twisting_loop]

    def twist(self, element):
        """Apply the twist automorphism to a free-group word."""
        if element.parent() != self.F:
            raise TypeError("element must be an element of fg.F")

        result = self.F.one()
        for idx in element.Tietze():
            generator_name = self.GEN_NAMES[abs(idx)]
            image = self.act.get(
                generator_name,
                self.F.gen(abs(idx) - 1),
            )
            result *= image if idx > 0 else ~image
        return result


DT = DehnTwist


class MappingClass:
    """A word in the twelve Dehn-twist generators."""

    GENERATORS = frozenset(DehnTwist.ACTION)

    def __init__(self, loops: str):
        if not isinstance(loops, str):
            raise TypeError("loops must be a string")
        unknown = sorted(set(loops) - self.GENERATORS)
        if unknown:
            raise ValueError(f"Unknown Dehn twist generators: {unknown}")
        self.loops = self._reduce_word(loops)

    def __repr__(self):
        return f"MappingClass({self.loops!r})"

    def __eq__(self, other):
        if not isinstance(other, MappingClass):
            return NotImplemented
        return self.loops == other.loops    
    
    def __mul__(self, other):
        if not isinstance(other, MappingClass):
            return NotImplemented
        return type(self)(self.loops + other.loops)

    def inv(self):
        return type(self)(self.loops[::-1].swapcase())

    def conj(self, other):
        """Return other * self * other^-1."""
        if not isinstance(other, MappingClass):
            raise TypeError("other must be a MappingClass")
        return other * self * other.inv()

    def act_on_basis(self):
        twists = [DehnTwist(letter) for letter in self.loops[::-1]]
        return [
            reduce(lambda word, twist: twist.twist(word), twists, generator)
            for generator in fg.BASIS
        ]
        
    @staticmethod
    def _reduce_word(loops):
        """Cancel adjacent inverse pairs such as aA and Aa."""
        stack = []
        for letter in loops:
            if (stack and stack[-1] == letter.swapcase()):
                stack.pop()
            else:
                stack.append(letter)
        return "".join(stack)

MC = MappingClass


# ---------------------------------------------------------------------------
# H = pi/[pi,pi] and Sp(4,ZZ)
# ---------------------------------------------------------------------------


H_Z = FreeModule(ZZ, 4)
H_Q = FreeModule(QQ, 4)

# Basis: 
# H_Z.basis() = [(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1)]
# _H_BASIS_LABEL: (1,0,0,0) |--> X, (0,1,0,0) |--> Y, (0,0,1,0) |--> Z, (0,0,0,1) |--> W
_H_BASIS_LABEL = dict( zip(H_Z.basis(), ("X", "Y", "Z", "W")) )

J = matrix(ZZ, [
    [0, 1, 0, 0],
    [-1, 0, 0, 0],
    [0, 0, 0, 1],
    [0, 0, -1, 0],
    ],
          )
J.set_immutable()

Sp4_Z = Sp(4, ZZ, invariant_form=J)
Sp4_Q = Sp(4, QQ, invariant_form=J.change_ring(QQ))

def homology(element):
    """Abelianize a free-group word in the basis (X,Y,Z,W)."""
    coordinates = H_Z.zero_vector()
    for idx in element.Tietze():
        coordinates[abs(idx) - 1] += 1 if idx > 0 else -1
    return coordinates


def matrix_from_columns(columns, ring=ZZ):
    """Construct a matrix whose columns are the supplied vectors."""
    if not columns:
        raise ValueError("columns must be nonempty")
    return matrix(
        ring,
        len(columns[0]),
        len(columns),
        lambda i, j: columns[j][i],
    )


def homology_action_matrix(mc):
    return matrix_from_columns(
        [homology(image) for image in mc.act_on_basis()],
        ZZ,
    )


def _format_linear_combination(coordinates, basis, coefficient_formatter=str):
    terms = []

    for coefficient, basis_element in zip(coordinates, basis):
        if coefficient == 0:
            continue

        absolute = abs(coefficient)
        body = (
            basis_element
            if absolute == 1
            else f"{coefficient_formatter(absolute)} {basis_element}"
        )

        if not terms:
            prefix = "- " if coefficient < 0 else ""
        else:
            prefix = " - " if coefficient < 0 else " + "
        terms.append(prefix + body)

    return "".join(terms) if terms else "0"


def _immutable_vector(ring, data, dimension, name):
    value = vector(ring, data)
    if len(value) != dimension:
        raise ValueError(f"{name} must have {dimension} coordinates")
    value.set_immutable()
    return value


# ---------------------------------------------------------------------------
# L2 = Lambda^2 H
# ---------------------------------------------------------------------------

_L2_BASIS = tuple(
    combinations(H_Z.basis(), 2)
)
_L2_PAIRS = tuple(
    combinations(range(H_Z.rank()), 2)
)
L2_Z = FreeModule(ZZ, len(_L2_BASIS))
L2_Q = FreeModule(QQ, len(_L2_BASIS))


class L2Element:
    """An element of L2_Q = Lambda^2(H_Q)."""

    def __init__(self, coordinates):
        value = L2_Q(coordinates)
        value.set_immutable()
        self.coordinates = value

    @classmethod
    def zero(cls):
        return cls(L2_Q.zero())

    def as_vector(self):
        """Return a mutable coordinate vector in L2_Q."""
        return L2_Q(list(self.coordinates))

    def is_zero(self):
        return self.coordinates == L2_Q.zero()

    def __len__(self):
        return L2_Q.rank()

    def __iter__(self):
        return iter(self.coordinates)

    def __getitem__(self, index):
        return self.coordinates[index]

    def __eq__(self, other):
        return (
            isinstance(other, L2Element)
            and self.coordinates == other.coordinates
        )

    def __add__(self, other):
        if not isinstance(other, L2Element):
            return NotImplemented

        return type(self)(
            self.coordinates + other.coordinates
        )

    def __neg__(self):
        return type(self)(-self.coordinates)

    def __sub__(self, other):
        if not isinstance(other, L2Element):
            return NotImplemented

        return self + (-other)

    def __rmul__(self, scalar):
        try:
            scalar = QQ(scalar)
        except (TypeError, ValueError):
            return NotImplemented

        return type(self)(
            scalar * self.coordinates
        )

    def __mul__(self, scalar):
        return self.__rmul__(scalar)

    @staticmethod
    def _basis_labels(latex_mode=False):
        wedge_symbol = r"\wedge " if latex_mode else "∧"

        return tuple(
            (
                _H_BASIS_LABEL[u]
                + wedge_symbol
                + _H_BASIS_LABEL[v]
            )
            for u, v in _L2_BASIS
        )

    def __repr__(self):
        return _format_linear_combination(
            self.coordinates,
            self._basis_labels(),
        )

    def _latex_(self):
        return _format_linear_combination(
            self.coordinates,
            self._basis_labels(latex_mode=True),
            coefficient_formatter=latex,
        )

    def _repr_latex_(self):
        return "$" + self._latex_() + "$"
        

def wedge(u, v):
    """Return u wedge v as an element of L2_Q."""
    u, v = H_Q(u), H_Q(v)
    return L2Element( [u[i] * v[j] - u[j] * v[i] for i, j in _L2_PAIRS] )


def wedge_action_matrix(A):
    A = A.change_ring(QQ)
    return matrix_from_columns( [wedge(A.column(i), A.column(j)).as_vector() for i, j in _L2_PAIRS], QQ, )


# ---------------------------------------------------------------------------
# L3 = Lambda^3 H
# ---------------------------------------------------------------------------

_L3_BASIS = tuple(
    combinations(H_Z.basis(), 3)
)
_L3_TRIPLES = tuple(
    combinations(range(H_Z.rank()), 3)
)

L3_Z = FreeModule(ZZ, len(_L3_BASIS))
L3_Q = FreeModule(QQ, len(_L3_BASIS))


class L3Element:
    """An element of L3_Q = Lambda^3(H_Q)."""

    def __init__(self, coordinates):
        value = L3_Q(coordinates)
        value.set_immutable()
        self.coordinates = value

    def as_vector(self):
        return L3_Q(list(self.coordinates))

    def __iter__(self):
        return iter(self.coordinates)

    def __getitem__(self, index):
        return self.coordinates[index]

    def __eq__(self, other):
        return (
            isinstance(other, L3Element)
            and self.coordinates == other.coordinates
        )

    @staticmethod
    def _basis_labels(latex_mode=False):
        wedge_symbol = r"\wedge " if latex_mode else "∧"

        return tuple(
            wedge_symbol.join(
                _H_BASIS_LABEL[u]
                for u in basis_element
            )
            for basis_element in _L3_BASIS
        )

    def __repr__(self):
        return _format_linear_combination(
            self.coordinates,
            self._basis_labels(),
        )

    def _latex_(self):
        return _format_linear_combination(
            self.coordinates,
            self._basis_labels(latex_mode=True),
            coefficient_formatter=latex,
        )

    def _repr_latex_(self):
        return "$" + self._latex_() + "$"

    def to_HomHL2(self):
        """Return the corresponding HomHL2Element."""
        return _L3_to_HomHL2(self)

        
# ---------------------------------------------------------------------------
# ell_2^theta : pi -> L2
# ---------------------------------------------------------------------------

def _make_ell2_generator_values():
    half = QQ(1) / 2
    return {
        1: L2Element([half, 0, 0, 0, 0, 0]),
        2: L2Element([-half, 0, 0, 0, 0, 0]),
        3: L2Element([0, 0, 0, 0, 0, half]),
        4: L2Element([0, 0, 0, 0, 0, -half]),
    }


ELL2_GENERATOR_VALUES = _make_ell2_generator_values()


def _ell2_on_letter(idx):
    """Internal value of ell_2^theta on one signed Tietze letter."""
    if idx == 0 or abs(idx) not in ELL2_GENERATOR_VALUES:
        raise ValueError(f"Invalid Tietze letter: {idx}")
    value = ELL2_GENERATOR_VALUES[abs(idx)]
    return value if idx > 0 else -value


def ell2_theta(element):
    r"""Compute ell_2^theta(element) as an L2 element.

    Product rule:
        ell_2(uv) = ell_2(u) + ell_2(v) + (1/2)|u| wedge |v|.
    """
    h = H_Q.zero_vector()
    result = L2Element.zero()

    for idx in element.Tietze():
        letter_homology = H_Q.zero_vector()
        letter_homology[abs(idx) - 1] = 1 if idx > 0 else -1
        result += (
            _ell2_on_letter(idx)
            + QQ(1) / 2 * wedge(h, letter_homology)
        )
        h += letter_homology

    return result


# ---------------------------------------------------------------------------
# Hom(H, L2)
# ---------------------------------------------------------------------------

HomHL2_Z = Hom(H_Z, L2_Z)
HomHL2_Q = Hom(H_Q, L2_Q)


class HomHL2Element:
    """An element of HomHL2_Q = Hom(H_Q, L2_Q)."""

    def __init__(self, coordinate_matrix):
        """
        Construct from a 6-by-4 matrix acting on column vectors.

        The transpose required by Sage's matrix convention is handled
        internally.
        """
        coordinate_matrix = matrix(QQ, coordinate_matrix)

        self.morphism = HomHL2_Q(
            coordinate_matrix.transpose()
        )

    @classmethod
    def from_morphism(cls, morphism):
        """Construct from an element of HomHL2_Q."""
        morphism = HomHL2_Q(morphism)

        instance = cls.__new__(cls)
        instance.morphism = morphism
        return instance

    @classmethod
    def zero(cls):
        return cls.from_morphism(
            HomHL2_Q.zero()
        )

    def is_zero(self):
        return self.morphism == HomHL2_Q.zero()

    def as_matrix(self):
        """
        Return the 6-by-4 coordinate matrix acting on column vectors.

        The Sage-internal transpose convention is hidden here.
        """
        return matrix(
            QQ,
            self.morphism.matrix().transpose(),
        )

    def __call__(self, X):
        """Evaluate this homomorphism at X in H_Q."""
        return L2Element(
            self.morphism(H_Q(X))
        )

    def on_basis(self):
        """Return the images of the basis of H_Q as L2Element objects."""
        return tuple(
            self(X)
            for X in H_Q.basis()
        )
    

    def transported_by(self, A):
        r"""
        Return (Lambda^2 A) self A^{-1}.
        """
        A = matrix(QQ, A)

        if (
            A.nrows() != H_Q.rank()
            or A.ncols() != H_Q.rank()
            or not A.is_invertible()
        ):
            raise ValueError(
                "A must be an invertible 4-by-4 matrix"
            )

        return type(self)(
            wedge_action_matrix(A)
            * self.as_matrix()
            * A.inverse()
        )

    def as_L3(self):
        r"""
        Return this homomorphism as an element of Lambda^3 H_Q.
        
        Raise ValueError if it is not a symplectic degree-one
        derivation, hence does not lie in Lambda^3 H_Q.
        """
        return _HomHL2_to_L3(self)

    
    def __eq__(self, other):
        return (
            isinstance(other, HomHL2Element)
            and self.morphism == other.morphism
        )

    def __add__(self, other):
        if not isinstance(other, HomHL2Element):
            return NotImplemented

        return type(self).from_morphism(
            self.morphism + other.morphism
        )

    def __neg__(self):
        return type(self).from_morphism(
            -self.morphism
        )

    def __sub__(self, other):
        if not isinstance(other, HomHL2Element):
            return NotImplemented

        return type(self).from_morphism(
            self.morphism - other.morphism
        )

    def __rmul__(self, scalar):
        try:
            scalar = QQ(scalar)
        except (TypeError, ValueError):
            return NotImplemented

        return type(self).from_morphism(
            HomHL2_Q(
                scalar * self.morphism.matrix()
            )
        )

    def __mul__(self, scalar):
        return self.__rmul__(scalar)

    def __repr__(self):
        images = ", ".join(
            f"{_H_BASIS_LABEL[X]} -> {image}"
            for X, image in zip(
                H_Z.basis(),
                self.on_basis(),
            )
        )
        return f"HomHL2Element({images})"

    def _latex_(self):
        return latex(self.as_matrix())

    def _repr_latex_(self):
        return "$" + self._latex_() + "$"


def _L3_to_HomHL2(trivector):
    r"""
    Embed Lambda^3 H_Q into Hom(H_Q, Lambda^2 H_Q)
    using the symplectic form J.
    """
    if not isinstance(trivector, L3Element):
        trivector = L3Element(trivector)

    pair_index = {
        pair: index
        for index, pair in enumerate(_L2_PAIRS)
    }

    columns = []

    for h in H_Q.basis():
        # pairing[s] = <h, e_s> = h^T J e_s
        pairing = [
            sum(
                h[r] * J[r, s]
                for r in range(H_Q.rank())
            )
            for s in range(H_Q.rank())
        ]

        image = vector(QQ, L2_Q.rank())

        for coefficient, (i, j, k) in zip(
            trivector,
            _L3_TRIPLES,
        ):
            image[pair_index[(j, k)]] += (
                coefficient * pairing[i]
            )
            image[pair_index[(i, k)]] -= (
                coefficient * pairing[j]
            )
            image[pair_index[(i, j)]] += (
                coefficient * pairing[k]
            )

        columns.append(image)

    return HomHL2Element(
        matrix_from_columns(columns, QQ)
    )


def _flatten_HomHL2(tau):
    """Flatten a 6-by-4 column-action matrix column by column."""
    matrix_value = tau.as_matrix()

    return vector(
        QQ,
        [
            matrix_value[row, column]
            for column in range(matrix_value.ncols())
            for row in range(matrix_value.nrows())
        ],
    )


def _L3_embedding_matrix():
    r"""
    Return the 24-by-4 matrix of

        Lambda^3 H_Q -> Hom(H_Q, Lambda^2 H_Q).
    """
    columns = []

    for basis_vector in L3_Q.basis():
        image = _L3_to_HomHL2(
            L3Element(basis_vector)
        )
        columns.append(
            _flatten_HomHL2(image)
        )

    return matrix_from_columns(columns, QQ)


def _HomHL2_to_L3(tau):
    r"""
    Convert tau to L3Element.

    Raise ValueError if tau does not lie in the image of Lambda^3 H_Q.
    """
    if not isinstance(tau, HomHL2Element):
        raise TypeError(
            "tau must be a HomHL2Element"
        )

    embedding = _L3_embedding_matrix()
    target = _flatten_HomHL2(tau)

    try:
        coordinates = embedding.solve_right(target)
    except ValueError as error:
        raise ValueError(
            "HomHL2Element does not lie in Lambda^3 H_Q"
        ) from error

    # 念のため、厳密に像に入っていることを再確認する。
    if embedding * coordinates != target:
        raise ValueError(
            "HomHL2Element does not lie in Lambda^3 H_Q"
        )

    return L3Element(coordinates)


# ---------------------------------------------------------------------------
# N3_Q = L2_Q x H_Q with the BCH group law
# ---------------------------------------------------------------------------

N3_Q = L2_Q.direct_sum(H_Q)


class N3Element:
    r"""
    An element of N3_Q in BCH coordinates.

    The underlying coordinate space is L2_Q direct_sum H_Q, while
    multiplication is

        (xi, X)(eta, Y)
        = (xi + eta + (1/2) X wedge Y, X + Y).
    """

    def __init__(self, xi, X):
        if not isinstance(xi, L2Element):
            xi = L2Element(xi)

        X = H_Q(X)

        coordinates = N3_Q(
            tuple(xi.coordinates) + tuple(X)
        )
        coordinates.set_immutable()

        self.coordinates = coordinates

    @classmethod
    def identity(cls):
        return cls(
            L2Element.zero(),
            H_Q.zero(),
        )

    @classmethod
    def from_word(cls, word):
        return cls(
            ell2_theta(word),
            homology(word),
        )

    @property
    def xi(self):
        """Return the L2_Q component as an L2Element."""
        return L2Element(
            self.coordinates[:L2_Q.rank()]
        )

    @property
    def X(self):
        """Return the H_Q component."""
        value = H_Q(
            self.coordinates[L2_Q.rank():]
        )
        value.set_immutable()
        return value

    def as_pair(self):
        """Return the pair (xi, X)."""
        return self.xi, self.X

    def is_identity(self):
        return self == type(self).identity()

    def __iter__(self):
        return iter(self.as_pair())

    def __eq__(self, other):
        return (
            isinstance(other, N3Element)
            and self.coordinates == other.coordinates
        )

    def __mul__(self, other):
        if not isinstance(other, N3Element):
            return NotImplemented

        return type(self)(
            self.xi
            + other.xi
            + QQ(1) / 2 * wedge(self.X, other.X),
            self.X + other.X,
        )

    def inverse(self):
        return type(self)(
            -self.xi,
            -self.X,
        )

    def __invert__(self):
        return self.inverse()

    def __repr__(self):
        h_repr = _format_linear_combination(
            self.X,
            tuple(
                _H_BASIS_LABEL[u]
                for u in H_Z.basis()
            ),
        )
        return f"({self.xi}, {h_repr})"

    def _latex_(self):
        h_latex = _format_linear_combination(
            self.X,
            tuple(
                _H_BASIS_LABEL[u]
                for u in H_Z.basis()
            ),
        )
        return (
            r"\left("
            + self.xi._latex_()
            + r",\;"
            + h_latex
            + r"\right)"
        )

    def _repr_latex_(self):
        return "$" + self._latex_() + "$"
        

# ---------------------------------------------------------------------------
# Aut(N3) represented by (tau, A)
# ---------------------------------------------------------------------------

EndN3_Q = Hom(N3_Q, N3_Q)


class AutN3Element:
    r"""
    An automorphism of N3_Q represented by (tau, A).

    The action is

        (xi, X) |-> (tau(A X) + (Lambda^2 A)xi, A X).
    """

    def __init__(self, tau, A):
        if not isinstance(tau, HomHL2Element):
            tau = HomHL2Element(tau)

        A = matrix(QQ, A)

        if (
            A.nrows() != H_Q.rank()
            or A.ncols() != H_Q.rank()
            or not A.is_invertible()
        ):
            raise ValueError(
                "A must be an invertible 4-by-4 matrix"
            )

        A.set_immutable()

        A2 = wedge_action_matrix(A)
        A2.set_immutable()

        # Column-action matrix on N3_Q = L2_Q direct_sum H_Q:
        #
        #     [ Lambda^2 A    tau A ]
        #     [      0           A  ]
        #
        column_matrix = block_matrix(QQ, [
            [
                A2,
                tau.as_matrix() * A,
            ],
            [
                zero_matrix(
                    QQ,
                    H_Q.rank(),
                    L2_Q.rank(),
                ),
                A,
            ],
        ])

        # Sage's Hom convention requires the transpose.
        morphism = EndN3_Q(
            column_matrix.transpose()
        )

        self.tau = tau
        self.A = A
        self.A2 = A2
        self.morphism = morphism

    @classmethod
    def identity(cls):
        return cls(
            HomHL2Element.zero(),
            identity_matrix(QQ, H_Q.rank()),
        )

    def is_identity(self):
        return self == type(self).identity()

    def as_matrix(self):
        """
        Return the 10-by-10 matrix acting on column coordinates.

        The Sage-internal transpose convention is hidden here.
        """
        return matrix(
            QQ,
            self.morphism.matrix().transpose(),
        )

    def as_L3_pair(self):
        """Return (tau, A), with tau represented as an L3Element."""
        return self.tau.as_L3(), self.A
    
    def __call__(self, element):
        """Apply this automorphism to an N3Element."""
        if not isinstance(element, N3Element):
            raise TypeError(
                "AutN3Element acts on N3Element objects"
            )

        image = self.morphism(
            element.coordinates
        )

        return N3Element(
            L2Element(
                image[:L2_Q.rank()]
            ),
            H_Q(
                image[L2_Q.rank():]
            ),
        )

    def __eq__(self, other):
        return (
            isinstance(other, AutN3Element)
            and self.morphism == other.morphism
        )

    def __mul__(self, other):
        """
        Return the composition self o other.
        """
        if not isinstance(other, AutN3Element):
            return NotImplemented

        return type(self)(
            self.tau
            + other.tau.transported_by(self.A),
            self.A * other.A,
        )

    def inverse(self):
        A_inverse = self.A.inverse()

        inverse_tau = HomHL2Element(
            -(
                self.A2.inverse()
                * self.tau.as_matrix()
                * self.A
            )
        )

        return type(self)(
            inverse_tau,
            A_inverse,
        )

    def __invert__(self):
        return self.inverse()

    def __repr__(self):
        return (
            "AutN3Element("
            f"tau={self.tau!r}, "
            f"A={self.A!r}"
            ")"
        )

    def _latex_(self):
        return (
            r"\left("
            + self.tau._latex_()
            + r",\;"
            + latex(self.A)
            + r"\right)"
        )

    def _repr_latex_(self):
        return "$" + self._latex_() + "$"


# ---------------------------------------------------------------------------
# tau_1^theta and rho_3
# ---------------------------------------------------------------------------


def tau1_theta(mc):
    r"""
    Return tau_1^theta(mc) as a HomHL2Element.

    For each basis generator x_i,

        delta_i
        = ell_2^theta(mc(x_i))
          - (Lambda^2 A) ell_2^theta(x_i)

        = tau_1^theta(mc)(A e_i),

    where A is the induced action on H_Q. Therefore,

        tau_1^theta(mc) = D A^{-1},

    where the columns of D are the delta_i.
    """
    images = mc.act_on_basis()

    A = homology_action_matrix(mc).change_ring(QQ)
    A2 = wedge_action_matrix(A)

    delta_columns = []

    for index, image in enumerate(images, start=1):
        generator_value = ELL2_GENERATOR_VALUES[index]

        transported_generator_value = L2Element(
            A2 * generator_value.as_vector()
        )

        delta = (
            ell2_theta(image)
            - transported_generator_value
        )

        delta_columns.append(
            delta.as_vector()
        )

    D = matrix_from_columns(
        delta_columns,
        QQ,
    )

    return HomHL2Element(
        D * A.inverse()
    )


def rho3(mc):
    """Return rho_3(mc) as an AutN3Element."""
    return AutN3Element(
        tau=tau1_theta(mc),
        A=homology_action_matrix(mc),
    )



__all__ = [
    "fundamentalGroup",
    "fg",
    "DehnTwist",
    "DT",
    "MappingClass",
    "MC",
    "H_Z",
    "H_Q",
    "J",
    "Sp4_Z",
    "Sp4_Q",
    "homology",
    "matrix_from_columns",
    "homology_action_matrix",
    "L2_Z",
    "L2_Q",
    "L2Element",
    "L3_Z",
    "L3_Q",
    "L3Element",
    "wedge",
    "wedge_action_matrix",
    "ELL2_GENERATOR_VALUES",
    "ell2_theta",
    "HomHL2_Z",
    "HomHL2_Q",
    "HomHL2Element",
    "N3_Q",
    "N3Element",
    "EndN3_Q",
    "AutN3Element",
    "tau1_theta",
    "rho3",
]