# 実装メモ｜n3_monodromy.py

## 1. 目的

種数2のモノドロミーについて、\(H\) および \(N_3\) 上の計算を notebook から独立した再利用可能な SageMath モジュールとしてまとめる。

## 2. ファイル

- `n3_monodromy.py`
- `test_n3_monodromy.py`
- `n3_monodromy_guide.md`

notebook と同じ階層の `modules/` に置き、

```python
import sys
sys.path.insert(0, "./modules")

from n3_monodromy import *
```

で利用する。

## 3. 値クラス

### L2

\[
L_2=\Lambda^2H
\]

の元。6次元座標を保持する。

基底順序：

\[
X\wedge Y,\ X\wedge Z,\ X\wedge W,\ 
Y\wedge Z,\ Y\wedge W,\ Z\wedge W.
\]

### HomHL2

\[
\operatorname{Hom}(H,\Lambda^2H)
\]

の元を \(6\times4\) 行列として保持する。

### N3

\[
N_3=\Lambda^2H\rtimes H
\]

の元 \((\xi,X)\)。

### AutN3

\[
(\tau,A)\in
\operatorname{Hom}(H,\Lambda^2H)\rtimes\operatorname{GL}(H)
\]

で表した \(N_3\) の自己同型。

mapping class の像では \(A\in\operatorname{Sp}(H)\)。

## 4. 基本関数

```python
ell2_theta(g)       # pi -> L2
tau1_theta(phi)     # MappingClass -> HomHL2
rho3(phi)           # MappingClass -> AutN3
```

## 5. MappingClass の convention

`MC("uv")` は

\[
u\circ v
\]

として作用し、右側の twist が先に作用する。

## 6. 基本使用例

```python
phi = MC("DbCa")

tau = tau1_theta(phi)
R = rho3(phi)

g = fg.x * fg.Y * fg.z
u = N3.from_word(g)

Ru = R(u)
```

## 7. テスト

`run_all_tests()` により全20テスト群が成功。

主な確認項目：

- 自由群と Dehn twist の作用
- mapping class の合成・逆元・共役
- \(H\) 上の作用と symplectic 条件
- \(L_2\) の演算
- \(\ell_2^\theta\) の積公式・境界値
- `HomHL2`
- \(N_3\) の群法則
- \(\Lambda^2A\) の作用
- \(\tau_1^\theta\)
- `AutN3`
- \(\rho_3\)
- 自由群上の作用と \(N_3\) 上の作用の一致
- 境界元の固定

最終出力：

```text
All 20 test groups passed.
```

## 8. 現在の役割

1.4｜Aut(N₃) 共役判定 — モノドロミー族 \(\phi_n\) の正式検証では、この最新版モジュールを基準実装とする。
