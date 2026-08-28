# `n3_monodromy.py` 使用ガイド

## 1. このモジュールでできること

`n3_monodromy.py` は、種数 $2$ の曲面の基本群

$$
\pi=\langle x,y,z,w\rangle
$$

と、その $2$ 段冪零商 $N_3$ に対するモノドロミーの作用を計算するための SageMath モジュールである。

主に次の計算を行える。

- 自由群の語と境界語の生成
- Humphries 型 Dehn twist の自由群上の作用
- Dehn twist の語で表された mapping class の合成・逆元・共役
- $H=\pi/[\pi,\pi]\cong\mathbb Z^4$ 上の作用行列
- $\Lambda^2H$ 上の誘導作用
- $\ell_2^\theta$ の計算
- $N_3\cong\Lambda^2H\rtimes H$ の座標と群演算
- $\tau_1^\theta(\phi)$ の計算
- $\rho_3(\phi)$ の構成と $N_3$ の元への作用

現段階では、$\operatorname{Sp}_4(\mathbb Z)$ での共役判定や Johnson obstruction の最終判定は含まれていない。

## 2. 必要な環境と配置

このファイルは通常の `.py` 形式だが、内部で `sage.all` を使うため、**SageMath の Python 環境**から読み込む必要がある。

最も簡単なのは、次の3ファイルを同じフォルダに置く方法である。

```text
作業フォルダ/
├── n3_monodromy.py
├── test_n3_monodromy.py
└── research_notebook.ipynb
```

SageMath カーネルの notebook では次のように読み込む。

```python
import n3_monodromy as n3
```

このガイドでは、名前の衝突を避けるためにこの形式を使う。公開名をすべて直接読み込む場合は次でもよい。

```python
from n3_monodromy import *
```

別のフォルダに置く場合は、そのフォルダを検索パスへ追加する。

```python
import sys
sys.path.append("/Users/ユーザー名/path/to/modules")

import n3_monodromy as n3
```

モジュールの編集後、カーネルを再起動せずに読み直すには次を使う。

```python
import importlib
importlib.reload(n3)
```

## 3. クイックスタート

例としてモノドロミー

$$
\phi=t_Dt_bt_Ct_a
$$

を `DbCa` と表す。

```python
import n3_monodromy as n3

phi = n3.MC("DbCa")

# 自由群の基底 x,y,z,w の像
images = phi.act_on_basis()

# H 上の作用行列
A = n3.homology_action_matrix(phi)

# tau_1^theta(phi)
tau = n3.tau1_theta(phi)

# rho_3(phi) の全データ
data = n3.rho3(phi)
```

`data` は次の4項目を持つ辞書である。

| キー | 内容 | サイズ・型 |
|---|---|---|
| `A` | $H$ 上の作用 | $4\times4$ 整数行列 |
| `A2` | $\Lambda^2A$ | $6\times6$ 有理数行列 |
| `tau` | $\tau_1^\theta(\phi):H\to\Lambda^2H$ | $6\times4$ 有理数行列 |
| `images` | $x,y,z,w$ の自由群上の像 | 自由群の元4個のリスト |

## 4. 記法と合成規約

### 4.1 自由群の生成元

自由群と生成元は `fg` にまとめられている。

```python
n3.fg.F                    # 自由群
n3.fg.x, n3.fg.y           # x, y
n3.fg.z, n3.fg.w           # z, w
n3.fg.X, n3.fg.Y           # x^{-1}, y^{-1}
n3.fg.Z, n3.fg.W           # z^{-1}, w^{-1}
n3.fg.BASIS                # (x, y, z, w)
```

自由群の語は `*` で掛ける。

```python
g = n3.fg.x * n3.fg.Y * n3.fg.z * n3.fg.w
g_inv = ~g
one = n3.fg.F.one()
```

### 4.2 交換子・共役・境界語

交換子の規約は

$$
[u,v]=uvu^{-1}v^{-1}
$$

である。

```python
comm = n3.fg.comm(n3.fg.x, n3.fg.y)
```

`fg.u.conj(v)` の規約は

$$
\operatorname{fg.u.conj}(v)=vuv^{-1}
$$

である。

```python
conjugate = n3.fg.x.conj(n3.fg.y)
# y*x*y^{-1}
```

境界語

$$
\partial=[x,y][z,w]
$$

は `n3.fg.bnd` として準備されている。

### 4.3 Dehn twist の文字

使用できる文字は次の12個である。

```text
a A b B c C d D e E f F
```

小文字が twist、大文字がその逆 twist を表す。

### 4.4 mapping class の合成順序

`MC("uv")` では、**右端の twist が先に作用する**。

```python
phi = n3.MC("a") * n3.MC("b")
```

これは写像として $t_a\circ t_b$ を表す。したがって、

$$
A(\phi\psi)=A(\phi)A(\psi)
$$

という行列積の順序と一致する。

## 5. Dehn twist の使い方

一つの twist を自由群の語へ作用させる。

```python
T = n3.DT("b")
g = n3.fg.x * n3.fg.Y * n3.fg.z
Tg = T.twist(g)
```

基底すべての像を見るには `MC` が便利である。

```python
n3.MC("b").act_on_basis()
```

twist が境界語を固定することも直接確認できる。

```python
assert T.twist(n3.fg.bnd) == n3.fg.bnd
```

## 6. MappingClass の使い方

### 6.1 生成と積

```python
phi = n3.MC("Db")
psi = n3.MC("Ca")

product = phi * psi
# MappingClass('DbCa')
```

空文字列は恒等写像を表す。

```python
identity = n3.MC("")
```

### 6.2 逆元

```python
phi = n3.MC("DbCa")
phi_inv = phi.inv()

print(phi_inv)
# MappingClass('AcBd')

assert (phi * phi_inv).act_on_basis() == list(n3.fg.BASIS)
```

### 6.3 共役

```python
phi = n3.MC("a")
h = n3.MC("b")
conjugate = phi.conj(h)
```

規約は

$$
\phi.\mathrm{conj}(h)=h\phi h^{-1}
$$

である。

```python
assert conjugate.act_on_basis() == (h * phi * h.inv()).act_on_basis()
```

## 7. $H$ 上の計算

### 7.1 自由群の語の可換化

`homology(g)` は自由群の語を基底 $(X,Y,Z,W)$ の列ベクトルへ送る。

```python
g = n3.fg.x * n3.fg.Y * n3.fg.z
n3.homology(g)
# (1, -1, 1, 0)
```

### 7.2 作用行列

```python
phi = n3.MC("DbCa")
A = n3.homology_action_matrix(phi)
```

行列は**基底の像を列に並べる規約**である。第 $j$ 列が第 $j$ 基底ベクトルの像になる。

```python
columns = [n3.homology(g) for g in phi.act_on_basis()]
A_again = n3.matrix_from_columns(columns)
assert A == A_again
```

### 7.3 symplectic 条件

```python
assert n3.is_symplectic(A)
```

使用する交叉形式は

$$
J=
\begin{pmatrix}
0&1&0&0\\
-1&0&0&0\\
0&0&0&1\\
0&0&-1&0
\end{pmatrix}
$$

である。

## 8. $\Lambda^2H$ 上の計算

### 8.1 基底順序

$\Lambda^2H$ の基底順序は

$$
X\wedge Y,\;
X\wedge Z,\;
X\wedge W,\;
Y\wedge Z,\;
Y\wedge W,\;
Z\wedge W
$$

である。

```python
n3.WEDGE_BASIS
```

### 8.2 外積

```python
from sage.all import QQ, vector

u = vector(QQ, [1, 0, 1, 0])
v = vector(QQ, [0, 1, 0, 1])
uv = n3.wedge(u, v)
```

戻り値は上記の基底順序による6次元ベクトルである。

### 8.3 誘導作用

```python
A = n3.homology_action_matrix(n3.MC("DbCa"))
A2 = n3.wedge_action_matrix(A)
```

`A2` は $6\times6$ 行列で、

$$
(\Lambda^2A)(U\wedge V)=AU\wedge AV
$$

を満たす。

## 9. $\ell_2^\theta$ の計算

生成元での値は `ELL` に保存されている。

```python
n3.ELL
```

任意の自由群の語に対しては `ell2` を使う。

```python
g = n3.fg.x * n3.fg.Y * n3.fg.z
ell_g = n3.ell2(g)
```

内部では

$$
\ell_2(uv)
=
\ell_2(u)+\ell_2(v)
+\frac12|u|\wedge|v|
$$

を使って一文字ずつ計算する。境界語については

$$
\ell_2(\partial)=X\wedge Y+Z\wedge W
$$

となる。

```python
from sage.all import QQ, vector

omega = vector(QQ, [1, 0, 0, 0, 0, 1])
assert n3.ell2(n3.fg.bnd) == omega
```

## 10. $N_3$ の座標と群演算

このモジュールでは

$$
[g]_3
\longleftrightarrow
(\ell_2^\theta(g),|g|)
\in\Lambda^2H\times H
$$

と表す。

### 10.1 座標への変換

```python
g = n3.fg.x * n3.fg.Y * n3.fg.z
g_N3 = n3.N3_coordinate(g)

xi, X = g_N3
```

- `xi` は6次元の $\Lambda^2H$ 成分
- `X` は4次元の $H$ 成分

### 10.2 積

```python
u = n3.N3_coordinate(n3.fg.x * n3.fg.y)
v = n3.N3_coordinate(n3.fg.Z * n3.fg.w)
uv = n3.N3_multiply(u, v)
```

群法則は

$$
(\xi,X)(\nu,Y)
=
\left(
\xi+\nu+\frac12X\wedge Y,\;
X+Y
\right)
$$

である。

### 10.3 逆元

```python
u_inv = n3.N3_inverse(u)
```

この座標では $(\xi,X)^{-1}=(-\xi,-X)$ となる。

## 11. $\tau_1^\theta$ の計算

```python
phi = n3.MC("DbCa")
tau = n3.tau1_theta(phi)
```

`tau` は

$$
\tau_1^\theta(\phi):H\longrightarrow\Lambda^2H
$$

を表す $6\times4$ 行列である。

- 列の順序：$X,Y,Z,W$
- 行の順序：$X\wedge Y,X\wedge Z,X\wedge W,Y\wedge Z,Y\wedge W,Z\wedge W$

twist 単体については、例えば次を確認できる。

```python
from sage.all import QQ, zero_matrix

zero_tau = zero_matrix(QQ, 6, 4)

assert n3.tau1_theta(n3.MC("a")) == zero_tau
assert n3.tau1_theta(n3.MC("b")) != zero_tau
assert n3.tau1_theta(n3.MC("e")) != zero_tau
```

## 12. $\rho_3$ の計算と作用

### 12.1 $\rho_3(\phi)$ の構成

```python
phi = n3.MC("DbCa")
R = n3.rho3(phi)

A = R["A"]
A2 = R["A2"]
tau = R["tau"]
images = R["images"]
```

このデータが

$$
\rho_3(\phi)=(\tau_1^\theta(\phi),A)
$$

を表す。

### 12.2 $N_3$ の元へ作用

```python
g = n3.fg.x * n3.fg.Y * n3.fg.z
g_N3 = n3.N3_coordinate(g)
image_N3 = n3.rho3_apply(R, g_N3)
```

自由群上の直接計算との一致は次のように確認できる。

```python
for generator, image in zip(n3.fg.BASIS, phi.act_on_basis()):
    lhs = n3.rho3_apply(R, n3.N3_coordinate(generator))
    rhs = n3.N3_coordinate(image)
    assert lhs == rhs
```

## 13. 任意のモノドロミーを調べる基本形

```python
import n3_monodromy as n3

MONODROMY = "DbCa"
phi = n3.MC(MONODROMY)

print("mapping class:", phi)

print("\nimages on pi:")
for name, image in zip(("x", "y", "z", "w"), phi.act_on_basis()):
    print(f"{name} -> {image}")

A = n3.homology_action_matrix(phi)
print("\nA =")
show(A)

print("symplectic:", n3.is_symplectic(A))

tau = n3.tau1_theta(phi)
print("\ntau_1^theta =")
show(tau)

R = n3.rho3(phi)

for generator, image in zip(n3.fg.BASIS, phi.act_on_basis()):
    assert n3.rho3_apply(R, n3.N3_coordinate(generator)) == (
        n3.N3_coordinate(image)
    )

print("rho_3 agrees with the direct action on the four generators")
```

`show` は SageMath notebook で行列を数式表示するための関数である。

## 14. テストの実行

テストは `test_n3_monodromy.py` に分離されている。

### 14.1 ターミナルから

2つの `.py` ファイルがあるフォルダへ移動して実行する。

```bash
sage -python test_n3_monodromy.py
```

すべて成功すれば最後に次が表示される。

```text
All 18 test groups passed.
```

### 14.2 notebook から

```python
from test_n3_monodromy import run_all_tests
run_all_tests()
```

### 14.3 pytest を使う場合

```bash
sage -python -m pytest test_n3_monodromy.py
```

## 15. 主な公開名

| 名前 | 用途 |
|---|---|
| `fg` | 自由群、生成元、逆元、境界語 |
| `DT(letter)` | Dehn twist 一つを生成 |
| `MC(word)` | twist の語から mapping class を生成 |
| `homology(g)` | 自由群の語を $H$ へ射影 |
| `homology_action_matrix(phi)` | $H$ 上の $4\times4$ 作用行列 |
| `is_symplectic(A)` | $A^TJA=J$ の確認 |
| `wedge(u,v)` | $u\wedge v\in\Lambda^2H$ |
| `wedge_action_matrix(A)` | $\Lambda^2A$ の $6\times6$ 行列 |
| `ELL` | $\ell_2^\theta$ の生成元での値 |
| `ell2(g)` | 自由群の語の $\ell_2^\theta$ |
| `N3_coordinate(g)` | 自由群の語を $N_3$ 座標へ変換 |
| `N3_multiply(u,v)` | $N_3$ 座標の積 |
| `N3_inverse(u)` | $N_3$ 座標の逆元 |
| `tau1_theta(phi)` | $\tau_1^\theta(\phi)$ の $6\times4$ 行列 |
| `rho3(phi)` | $\rho_3(\phi)$ の計算データ |
| `rho3_apply(R,u)` | $\rho_3(\phi)$ を $N_3$ の元へ作用 |

完全な一覧は次でも確認できる。

```python
n3.__all__
```

## 16. 注意点

1. **SageMath カーネルを使う。** 通常の Python カーネルでは `sage.all` を読み込めない。
2. mapping class の語には `aAbBcCdDeEfF` の文字だけを使う。
3. **合成は右から作用する。** `MC("DbCa")` では `a`、`C`、`b`、`D` の順に作用する。
4. **行列は列 convention である。** 基底ベクトルの像が各列に入る。
5. $H$ の基底順序は $X,Y,Z,W$、$\Lambda^2H$ は `WEDGE_BASIS` の順である。
6. `fg.conj(u,v)` は $vuv^{-1}$、`phi.conj(h)` は $h\phi h^{-1}$ である。
7. モジュールを編集した後は `importlib.reload` を行うか、カーネルを再起動する。

