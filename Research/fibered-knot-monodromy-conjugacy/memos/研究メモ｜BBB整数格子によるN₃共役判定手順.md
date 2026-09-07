# 研究メモ｜BBB整数格子による N₃ 共役判定手順

更新日: 2026-09-07

## 位置づけ

研究進捗ツリーの

`3｜N₃ 共役判定` → `3.1｜Johnson obstruction の適用方法の整理`

に対応する研究メモ。

Birman–Brendle–Broaddus (BBB) の「$N_3$ の正しい整数格子を保存する条件から Johnson–Morita representation の像を記述する」という考え方を採用し、$N_2=H$ 上の共役子を $\rho_3(\operatorname{Aut}_{\partial}\pi)$ 内の正しい $N_3$-lift に持ち上げたうえで、Johnson obstruction を整数 cokernel class として検査する手順を整理する。

旧メモ

- `OLD/研究メモ｜N₃共役方程式と整数格子.md`
- `OLD/研究メモ｜N₃共役判定とprimitive Johnson obstruction.md`

は本メモにより置き換える。

---

## 1. 基本設定

$H=N_2$ とし、

$$
R_\phi:=\rho_2(\phi),\qquad
R_\psi:=\rho_2(\psi).
$$

固定した symplectic expansion $\theta$ に関する extended Johnson 成分を

$$
 u_\phi:=\tau_1^\theta(\phi),\qquad
 u_\psi:=\tau_1^\theta(\psi)
$$

と置く。したがって

$$
\rho_3(\phi)=(u_\phi,R_\phi),\qquad
\rho_3(\psi)=(u_\psi,R_\psi).
$$

Morita の結果から一般に

$$
 u_\phi,u_\psi\in \frac12\Lambda^3H_\mathbb Z.
$$

以下

$$
L:=\Lambda^3H_\mathbb Z
$$

と置く。

実際に許される自己同型は ambient space 全体ではなく

$$
\operatorname{Aut}_{\partial}(N_3)
:=
\rho_3(\operatorname{Aut}_{\partial}\pi)
\subset
\frac12L\rtimes Sp(H_\mathbb Z)
$$

である。

---

## 2. BBB の役割：正しい $N_3$-lift を作る

symplectic expansion により $N_3$ は

$$
N_3\hookrightarrow L_{2,\mathbb Q}\times H_\mathbb Z
$$

と座標化され、積は

$$
(\xi,X)(\eta,Y)
=
\left(\xi+\eta+\frac12X\wedge Y,\,X+Y\right)
$$

で与えられる。

ただし $L_{2,\mathbb Q}\times H_\mathbb Z$ 全体が $N_3$ なのではなく、その中に $N_3$ の像として特定の整数格子

$$
\mathcal N_\theta
\subset
L_{2,\mathbb Q}\times H_\mathbb Z
$$

がある。

BBB の方法の本質は、

$$
(\nu,A)\in \frac12L\rtimes Sp(H_\mathbb Z)
$$

が実際に mapping class / $\operatorname{Aut}_{\partial}\pi$ から来るためには、この正しい整数格子を保存しなければならない、という条件を使うことである。

BBB の像記述、またはそれを現在の $\theta$-座標へ移した同値な格子保存条件から、固定した

$$
A\in Sp(H_\mathbb Z)
$$

に対して許される Johnson part の affine coset

$$
\nu_A+L
\subset
\frac12L
$$

を $A$ から決定できる。

したがって各 $A$ について一つ

$$
\boxed{
(\nu_A,A)
\in
\operatorname{Aut}_{\partial}(N_3)
}
$$

を正しく選べる。

ここで「正しく」とは、単に $\nu_A\in\frac12L$ という意味ではなく、実際に

$$
(\nu_A,A)\in\rho_3(\operatorname{Aut}_{\partial}\pi)
$$

であるという意味である。

---

## 3. Johnson の定理が与える残りの自由度

固定した $A$ に対し、正しい lift $(\nu_A,A)$ を一つ選んだとする。

Johnson の定理

$$
\tau_1(\mathcal I_{g,1})=\Lambda^3H_\mathbb Z=L
$$

により、同じ $A$ を $H$-部分にもつ全ての正しい lift はちょうど

$$
\boxed{
(\nu_A+w,A),\qquad w\in L
}
$$

を走る。

したがって、正しい基準 lift を一つ確保した後の残りの自由度は、ambient space の $\frac12L$ ではなく **exactly $L$** である。

これが整数 cokernel obstruction を使える理由である。

---

## 4. fixed-$Q$ の $N_3$ 共役判定

$Q\in Sp(H_\mathbb Z)$ が $N_2$-共役子、すなわち

$$
R_\psi=QR_\phi Q^{-1}
$$

を満たすとする。

BBB 型の格子保存条件から、$Q$ の正しい $N_3$-lift を一つ

$$
(\nu_Q,Q)
\in
\operatorname{Aut}_{\partial}(N_3)
$$

選ぶ。

同じ $Q$ を $H$-部分にもつ全 lift は

$$
(\nu_Q+w,Q),\qquad w\in L.
$$

半直積の積を

$$
(a,A)(b,B)=(a+A\cdot b,AB)
$$

とする規約では、

$$
(\nu,Q)\rho_3(\phi)(\nu,Q)^{-1}
$$

の Johnson 成分は

$$
Q\cdot u_\phi+(1-R_\psi\cdot)\nu
$$

である。

したがって $(\nu_Q+w,Q)$ が $N_3$-共役子になる条件は

$$
 u_\psi
=
Q\cdot u_\phi
+(1-R_\psi\cdot)(\nu_Q+w).
$$

そこで

$$
\boxed{
D_Q
:=
 u_\psi
-Q\cdot u_\phi
-(1-R_\psi\cdot)\nu_Q
}
$$

と置くと、fixed-$Q$ の必要十分条件は

$$
\boxed{
D_Q\in
\operatorname{Im}
\left(
1-R_\psi\cdot:L\to L
\right).
}
$$

### 正しい lift を使うことの決定的な効果

$(\nu_Q,Q)$ を正しい lift として選んでいるので

$$
\boxed{D_Q\in L}
$$

が自動的に保証される。

実際、$(\nu_Q,Q)\rho_3(\phi)(\nu_Q,Q)^{-1}$ と $\rho_3(\psi)$ は共に $\operatorname{Aut}_{\partial}(N_3)$ に属し、$H$ 上では同じ $R_\psi$ を持つ。したがって両者の差は kernel $L$ に入る。

単に $\nu_Q\in\frac12L$ を満たすだけの ambient lift を取った場合には、この整数性は保証されない。

---

## 5. fixed-$Q$ obstruction の cokernel class

正しい lift を

$$
\nu_Q\longmapsto\nu_Q+w_0,
\qquad w_0\in L
$$

と変えると

$$
D_Q
\longmapsto
D_Q-(1-R_\psi\cdot)w_0.
$$

したがって

$$
\boxed{
[D_Q]
\in
\operatorname{Coker}
\left(
1-R_\psi\cdot:L\to L
\right)
}
$$

は正しい lift の選び方によらない。

よって

$$
\boxed{
Q\text{ が }N_3\text{-共役子へ持ち上がる}
\iff
[D_Q]=0.
}
$$

---

## 6. primitive quotient への縮約

symplectic form を $\omega$ とし、

$$
P_\mathbb Z
:=
L/(H_\mathbb Z\wedge\omega)
$$

を integral primitive quotient とする。

fibered knot の場合に用いている $|f(1)|=1$ の条件のもとでは、$H_\mathbb Z\wedge\omega$ 成分で $1-R_\psi\cdot$ は unimodular なので、full Johnson cokernel は primitive quotient 上の cokernel に縮約できる。

$$
K_{\mathrm{prim}}(\psi)
:=
\operatorname{Coker}
\left(
1-R_\psi\cdot:P_\mathbb Z\to P_\mathbb Z
\right).
$$

したがって fixed-$Q$ 判定は

$$
\boxed{
[D_Q]_{\mathrm{prim}}=0
}
$$

となる。

ここで重要なのは、$u_\phi,u_\psi,\nu_Q$ は個別には半整数であり得るため、

$$
[u_\psi]_{\mathrm{prim}},
\qquad
[Q\cdot u_\phi]_{\mathrm{prim}}
$$

のように各項を別々に整数 cokernel class にしてはいけないことである。

まず正しい lift を用いて

$$
D_Q
=
 u_\psi-Q\cdot u_\phi-(1-R_\psi\cdot)\nu_Q
\in L
$$

を作り、その後で class を取る。

---

## 7. $N_2$ 共役子を中心化群方向に動かす

Yang・S-pair により一つ基準 $N_2$-共役子

$$
Q_0
$$

を得たとする。

$R_\phi$ の $Sp$-中心化群を、仮定のもとで

$$
S^{\times,1}\ni u
\longmapsto
C(u)
$$

とパラメータ化する。

すると全ての $N_2$-共役子は

$$
Q(u):=Q_0C(u),
\qquad u\in S^{\times,1}
$$

と書ける。

$Q_0$ と $C(u)$ について、それぞれ正しい lift

$$
(\nu_{Q_0},Q_0),
\qquad
(\nu_{C(u)},C(u))
$$

を選べば、その積により $Q(u)$ の正しい lift として

$$
\boxed{
\nu_{Q(u)}
=
\nu_{Q_0}+Q_0\cdot\nu_{C(u)}
}
$$

を選べる。

---

## 8. $u\in S^{\times,1}$ を動かしたときの obstruction

基準 obstruction を

$$
D(1)
:=
 u_\psi
-Q_0\cdot u_\phi
-(1-R_\psi\cdot)\nu_{Q_0}
\in L
$$

とする。

また中心化群方向の整数元を

$$
E_\phi(u)
:=
(C(u)-1)\cdot u_\phi
+(1-R_\phi\cdot)\nu_{C(u)}
$$

と置く。

$C(u)$ は $R_\phi$ と可換し、$(\nu_{C(u)},C(u))$ は正しい lift なので

$$
\boxed{E_\phi(u)\in L.}
$$

これは

$$
(\nu_{C(u)},C(u))
\rho_3(\phi)
(\nu_{C(u)},C(u))^{-1}
\rho_3(\phi)^{-1}
$$

の Johnson 成分である。

$Q(u)=Q_0C(u)$ に対する obstruction を $D(u)$ とすると

$$
\boxed{
D(u)=D(1)-Q_0\cdot E_\phi(u).
}
$$

したがって primitive cokernel class では

$$
\boxed{
[D(u)]_{\mathrm{prim}}
=
[D(1)]_{\mathrm{prim}}
-
Q_0\cdot[E_\phi(u)]_{\mathrm{prim}}.
}
$$

ここで $Q_0$ は自然な同型

$$
Q_0:
K_{\mathrm{prim}}(\phi)
\xrightarrow{\sim}
K_{\mathrm{prim}}(\psi)
$$

を誘導する。

---

## 9. 最終的な $N_3$ 共役判定

### 直接形

各 $u\in S^{\times,1}$ に対し $Q(u)=Q_0C(u)$ の正しい lift $\nu_{Q(u)}$ を取り、

$$
D(u)
=
 u_\psi
-Q(u)\cdot u_\phi
-(1-R_\psi\cdot)\nu_{Q(u)}
\in L
$$

を作る。

すると

$$
\boxed{
\rho_3(\phi),\rho_3(\psi)
\text{ が }\operatorname{Aut}_{\partial}(N_3)
\text{ 内で共役}
}
$$

であるための必要十分条件は

$$
\boxed{
\exists u\in S^{\times,1}
\quad\text{such that}\quad
[D(u)]_{\mathrm{prim}}=0.
}
$$

### 基準障害と中心化方向の相殺として書く形

同値に

$$
\boxed{
\exists u\in S^{\times,1}
\quad\text{such that}\quad
[D(1)]_{\mathrm{prim}}
=
Q_0\cdot[E_\phi(u)]_{\mathrm{prim}}.
}
$$

を検査すればよい。

つまり、固定された基準障害 $[D(1)]_{\mathrm{prim}}$ を、中心化群方向 $C(u)$ が生む class でちょうど相殺できるかを見る。

---

## 10. 実際の判定手順

1. Yang・S-pair により $N_2=H$ 上の共役を判定し、一つの基準共役子 $Q_0$ と中心化群 $C(u)$, $u\in S^{\times,1}$ を得る。
2. $u_\phi=\tau_1^\theta(\phi)$, $u_\psi=\tau_1^\theta(\psi)$ を計算する。
3. BBB 型の整数格子保存条件により、$Q_0$ および必要な $C(u)$ の正しい lift $\nu_{Q_0}$, $\nu_{C(u)}$ を求める。$Q(u)$ に対して直接 $\nu_{Q(u)}$ を求めてもよい。
4. $D(u)\in L$ を作る。
5. $P_\mathbb Z=L/(H_\mathbb Z\wedge\omega)$ へ落とし、$[D(u)]_{\mathrm{prim}}$ を Smith normal form 等で計算する。
6. $[D(u)]_{\mathrm{prim}}=0$ となる $u\in S^{\times,1}$ が存在するかを調べる。

この段階で新たに $w\in L$ を探索する必要はない。$w$ の自由度は cokernel に吸収されている。

したがって $N_2\to N_3$ に上がっても、外側の探索範囲は依然として

$$
\boxed{S^{\times,1}}
$$

のままである。

---

## 11. 正しい lift を最初に作る恩恵

ambient space $\frac12L\rtimes Sp(H_\mathbb Z)$ の中で共役方程式を解くだけでは、その解が $\rho_3(\operatorname{Aut}_{\partial}\pi)$ から来る保証がない。

BBB 型の条件で正しい lift

$$
(\nu_Q,Q)
\in
\rho_3(\operatorname{Aut}_{\partial}\pi)
$$

を一つ選ぶと、残りの許される自由度が

$$
\boxed{\nu_Q+L}
$$

に正確に限定される。

その結果

$$
D_Q\in L
$$

が保証され、lift の変更は

$$
D_Q\mapsto D_Q-(1-R_\psi\cdot)w,
\qquad w\in L
$$

だけになる。

したがって初めて、整数 primitive cokernel class $[D_Q]_{\mathrm{prim}}$ が自然かつ well-defined に定義できる。

要約すると

$$
\boxed{
\text{正しい lift}
\Longrightarrow
\text{残りの自由度は }L
\Longrightarrow
\text{整数 cokernel obstruction}
}
$$

という流れである。

---

## 12. 旧方針からの修正点

旧メモでは、cokernel に落とせば $Q$ の lift の Johnson part が不要になる、という簡略化を行っていた。

しかし $u_\phi,u_\psi$ や lift の Johnson part は一般に $\frac12L$ の元であり、個々には整数 primitive cokernel class を持たない。

したがって

$$
[u_\psi]_{\mathrm{prim}}
=
Q\cdot[u_\phi]_{\mathrm{prim}}
$$

のように半整数成分を個別に class 化することは一般には正しくない。

正しい手順は、まず BBB 型の条件により正しい lift $\nu_Q$ を取り、

$$
D_Q
=
 u_\psi-Q\cdot u_\phi-(1-R_\psi\cdot)\nu_Q
\in L
$$

を作ってから $[D_Q]_{\mathrm{prim}}$ を取ることである。

---

## 13. genus 2 の場合

$g=2$ では

$$
\Lambda^3H_\mathbb Z\cong H_\mathbb Z
$$

が $Sp$-equivariant に成り立ち、

$$
P_\mathbb Z
=
\Lambda^3H_\mathbb Z/(H_\mathbb Z\wedge\omega)
=0.
$$

fibered knot の条件 $|f(1)|=1$ のもとでは full cokernel から primitive cokernel への縮約も問題なく、$N_3$ obstruction は自動的に消える。

したがって genus 2 では

$$
\boxed{
N_2\text{-共役}\Longrightarrow N_3\text{-共役}.
}
$$

本格的な $N_3$ obstruction 検査が必要になるのは genus 3 以上である。

---

## 14. 残る実装課題

理論上の判定フローは上で閉じている。

次に必要なのは、BBB の整数格子記述を現在の symplectic expansion $\theta$ の座標

$$
L_{2,\mathbb Q}\times H_\mathbb Z
$$

へ明示的に移し、

$$
A\in Sp(H_\mathbb Z)
\longmapsto
\nu_A\bmod L
$$

を直接計算する公式を確定・実装することである。

これができれば、$N_3$ 共役判定は

- Yang・S-pair による $N_2$ 共役子と中心化群の計算
- extended Johnson 成分の計算
- BBB 型の正しい lift の計算
- integer primitive cokernel class の計算
- $S^{\times,1}$ 内の探索

という機械的手順になる。

---

## 参考

- J. S. Birman, T. E. Brendle, N. Broaddus, *Calculating the image of the second Johnson–Morita representation*.
- D. Johnson, 第一 Johnson 準同型と $\tau_1(\mathcal I_{g,1})=\Lambda^3H_\mathbb Z$.
- S. Morita, Johnson 準同型の mapping class group への拡張.
- `kiyoh.pdf`
- `simpleness.pdf`
- `研究メモ｜Q(c)によるYang・S-pair共役判定の整理.md`
