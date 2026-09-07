# 研究メモ｜BBB整数格子による N₃ 共役判定手順

更新日: 2026-09-07

## 位置づけ

研究進捗ツリーの

`3｜N₃ 共役判定` → `3.1｜Johnson obstruction の適用方法の整理`

に対応する研究メモ。

このメモでは、Birman–Brendle–Broaddus (BBB) の「$N_3$ の正しい整数格子を保存する条件から Johnson–Morita representation の像を記述する」という考え方を採用し、

- $N_2=H$ 上の共役子 $Q$ を、$ho_3(\operatorname{Aut}_{\partial}\pi)$ 内の **正しい $N_3$-lift** に持ち上げること
- その後の残りの自由度を Johnson の定理により $\Lambda^3H_\mathbb Z$ に限定すること
- 最後に primitive cokernel obstruction として $N_3$ 共役判定を行うこと

を一つの手順として整理する。

旧メモ

- `OLD/研究メモ｜N₃共役方程式と整数格子.md`
- `OLD/研究メモ｜N₃共役判定とprimitive Johnson obstruction.md`

は、このメモにより置き換える。

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

と書く。以下では記号を簡単にするため

$$
u_\phi=u_\phi,\qquad u_\psi=u_\psi
$$

と書き、

$$
\rho_3(\phi)=(u_\phi,R_\phi),\qquad
\rho_3(\psi)=(u_\psi,R_\psi)
$$

と表す。

Morita の extended Johnson 成分は一般に

$$
u_\phi,u_\psi\in \frac12\Lambda^3H_\mathbb Z
$$

に入る。

一方、$N_3$ 上で実際に許される自己同型の像は

$$
\operatorname{Aut}_{\partial}(N_3)
:=
\rho_3(\operatorname{Aut}_{\partial}\pi)
\subset
\frac12\Lambda^3H_\mathbb Z\rtimes Sp(H_\mathbb Z)
$$

であり、ambient space 全体ではない。

以下

$$
L:=\Lambda^3H_\mathbb Z
$$

と置く。

---

## 2. BBB の役割：$N_3$ の「正しい整数格子」を使う

symplectic expansion により $N_3$ は

$$
N_3\hookrightarrow L_{2,\mathbb Q}\times H_\mathbb Z
$$

と座標化され、積は

$$
(\xi,X)(\eta,Y)
=
\left(
\xi+\eta+\frac12X\wedge Y,\,
X+Y
\right)
$$

で与えられる。

重要なのは、$L_{2,\mathbb Q}\times H_\mathbb Z$ 全体が $N_3$ なのではなく、その中に $N_3$ の像として特定の整数格子

$$
\mathcal N_\theta
\subset
L_{2,\mathbb Q}\times H_\mathbb Z
$$

があることである。

BBB の方法の本質は、

$$
(\nu,A)\in \frac12L\rtimes Sp(H_\mathbb Z)
$$

が mapping class / $\operatorname{Aut}_{\partial}\pi$ から来るためには、この正しい整数格子 $\mathcal N_\theta$ を保存しなければならない、という条件を明示的に使うことである。

この格子保存条件から、固定した

$$
A\in Sp(H_\mathbb Z)
$$

に対して、許される Johnson part の半整数型

$$
\nu_A\bmod L
\in
\frac{\frac12L}{L}
\cong
L/2L
$$

が $A$ の行列成分だけから決まる。

したがって、BBB の像記述、またはそれを現在の $\theta$-座標へ移した同値な整数格子保存条件を使えば、各 $A$ に対して一つ

$$
\boxed{
(\nu_A,A)
\in
\operatorname{Aut}_{\partial}(N_3)
}
$$

を正しく選べる。

ここで「正しく」とは、単に

$$
\nu_A\in\frac12L
$$

という意味ではなく、実際に

$$
(\nu_A,A)\in\rho_3(\operatorname{Aut}_{\partial}\pi)
$$

であるという意味である。

---

## 3. Johnson の定理が与える残りの自由度

固定した $A\in Sp(H_\mathbb Z)$ に対して正しい lift を一つ

$$
(\nu_A,A)
\in
\operatorname{Aut}_{\partial}(N_3)
$$

取ったとする。

同じ $A$ を $H$-部分にもつ二つの正しい lift の差は Torelli 群から来る。

Johnson の定理

$$
\tau_1(\mathcal I_{g,1})=\Lambda^3H_\mathbb Z=L
$$

により、同じ $A$ の上にある正しい lift はちょうど

$$
\boxed{
(\nu_A+w,A),\qquad w\in L
}
$$

を走る。

したがって、正しい基準 lift を一つ確保した後には、残りの自由度は ambient space の $\frac12L$ ではなく、**exactly $L$** である。

この事実が、後で整数 cokernel obstruction を作れる理由である。

---

## 4. fixed-$Q$ の $N_3$ 共役判定

$Q\in Sp(H_\mathbb Z)$ が $N_2$-共役子、すなわち

$$
R_\psi=QR_\phi Q^{-1}
$$

を満たすとする。

BBB 型の整数格子保存条件から、$Q$ の正しい $N_3$-lift を一つ

$$
(\nu_Q,Q)
\in
\operatorname{Aut}_{\partial}(N_3)
$$

取る。

同じ $Q$ を $H$-部分にもつ全ての正しい lift は

$$
(\nu_Q+w,Q),\qquad w\in L
$$

である。

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

したがって

$$
(\nu_Q+w,Q)
$$

が $N_3$-共役子になる条件は

$$
 u_\psi
=
Q\cdot u_\phi
+(1-R_\psi\cdot)(\nu_Q+w).
$$

よって

$$
D_Q
:=
u_\psi
-Q\cdot u_\phi
-(1-R_\psi\cdot)\nu_Q
$$

と置けば、必要十分条件は

$$
\boxed{
D_Q\in
\operatorname{Im}
\left(
1-R_\psi\cdot:L\to L
\right).
}
$$

### 重要：$D_Q$ は整数格子に入る

$\nu_Q$ を「正しい lift」として選んでいるため、

$$
D_Q\in L
$$

が自動的に保証される。

実際、

$$
(\nu_Q,Q)\rho_3(\phi)(\nu_Q,Q)^{-1}
$$

と $\rho_3(\psi)$ は共に $\operatorname{Aut}_{\partial}(N_3)$ に属し、$H$ 上では同じ $R_\psi$ を持つ。したがって両者の差は kernel $L$ に入る。

ここが、$\nu_Q$ を単に $\frac12L$ から適当に選んだ場合との決定的な違いである。

---

## 5. fixed-$Q$ obstruction の cokernel class

正しい lift を

$$
\nu_Q\longmapsto\nu_Q+w_0,
\qquad w_0\in L
$$

と変えると、

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

そして

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

fibered knot の場合に用いている

$$
|f(1)|=1
$$

の条件のもとでは、$H_\mathbb Z\wedge\omega$ 成分で $1-R_\psi\cdot$ は unimodular となるため、full Johnson cokernel と primitive cokernel は同型になる。

そこで

$$
K_{\mathrm{prim}}(\psi)
:=
\operatorname{Coker}
\left(
1-R_\psi\cdot:
P_\mathbb Z\to P_\mathbb Z
\right)
$$

と置けば、fixed-$Q$ 判定は

$$
\boxed{
[D_Q]_{\mathrm{prim}}=0
}
$$

と書ける。

ここで重要なのは、$u_\phi,u_\psi,\nu_Q$ は個別には半整数であり得るため、

$$
[u_\psi]_{\mathrm{prim}},
\qquad
[Q\cdot u_\phi]_{\mathrm{prim}}
$$

のように各項を別々に整数 cokernel class にしてはいけないことである。

まず正しい lift $\nu_Q$ を用いて

$$
D_Q
=
u_\psi-Q\cdot u_\phi-(1-R_\psi\cdot)\nu_Q
\in L
$$

という整数元を作り、その後で primitive cokernel class を取る。

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

$Q_0$ と $C(u)$ について、それぞれ BBB 型の条件から正しい lift

$$
(\nu_{Q_0},Q_0),
\qquad
(\nu_{C(u)},C(u))
$$

を選ぶ。

積を取れば

$$
\boxed{
\nu_{Q(u)}
=
\nu_{Q_0}+Q_0\cdot\nu_{C(u)}
}
$$

を $Q(u)$ の正しい lift の Johnson part として選べる。

---

## 8. $u\in S^{\times,1}$ を動かしたときの obstruction の変化

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

$C(u)$ は $R_\phi$ と可換し、$(\nu_{C(u)},C(u))$ は正しい lift なので、

$$
\boxed{
E_\phi(u)\in L.
}
$$

これは

$$
(\nu_{C(u)},C(u))
\rho_3(\phi)
(\nu_{C(u)},C(u))^{-1}
\rho_3(\phi)^{-1}
$$

の Johnson 成分に一致する。

$Q(u)=Q_0C(u)$ に対する obstruction を $D(u)$ とすると、

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

ここで

$$
Q_0:
K_{\mathrm{prim}}(\phi)
\xrightarrow{\sim}
K_{\mathrm{prim}}(\psi)
$$

が誘導する同型を用いている。

---

## 9. 最終的な $N_3$ 共役判定

### 9.1 直接形

$Q(u)=Q_0C(u)$ に対して正しい lift $\nu_{Q(u)}$ を BBB 型の整数格子保存条件から選び、

$$
D(u)
=
u_\psi
-Q(u)\cdot u_\phi
-(1-R_\psi\cdot)\nu_{Q(u)}
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

### 9.2 基準障害と中心化方向の相殺として書く形

上の式は

$$
\boxed{
\exists u\in S^{\times,1}
\quad\text{such that}\quad
[D(1)]_{\mathrm{prim}}
=
Q_0\cdot[E_\phi(u)]_{\mathrm{prim}}.
}
$$

と同値である。

つまり、

- $[D(1)]_{\mathrm{prim}}$ は固定された基準 $N_2$-共役子 $Q_0$ の $N_3$ obstruction
- $[E_\phi(u)]_{\mathrm{prim}}$ は中心化群方向 $C(u)$ が生む補正

であり、この二つが一致する $u$ を探せばよい。

---

## 10. 実際の判定作業

### Step 1. $N_2$ 共役判定

Yang・S-pair により $N_2=H$ 上での共役を確認し、一つ基準共役子

$$
Q_0
$$

を得る。

同時に中心化群を

$$
C(u),\qquad u\in S^{\times,1}
$$

として記述する。

### Step 2. extended Johnson 成分を計算

$$
 u_\phi=\tau_1^\theta(\phi),
\qquad
u_\psi=\tau_1^\theta(\psi)
$$

を計算する。

### Step 3. BBB 型の整数格子条件で正しい lift を作る

$Q_0$ および必要な $C(u)$ に対して、$N_3$ の正しい整数格子 $\mathcal N_\theta$ の保存条件から

$$
(\nu_{Q_0},Q_0),
\qquad
(\nu_{C(u)},C(u))
$$

を正しく選ぶ。

または $Q(u)=Q_0C(u)$ に対して直接 $\nu_{Q(u)}$ を計算してもよい。

### Step 4. 整数 obstruction を作る

$$
D(u)
=
u_\psi
-Q(u)\cdot u_\phi
-(1-R_\psi\cdot)\nu_{Q(u)}
\in L
$$

を計算する。

### Step 5. primitive quotient に落とす

$$
P_\mathbb Z
=
L/(H_\mathbb Z\wedge\omega)
$$

へ射影し、

$$
[D(u)]_{\mathrm{prim}}
\in K_{\mathrm{prim}}(\psi)
$$

を求める。

実装上は $1-R_\psi\cdot$ の Smith normal form などで cokernel class を判定できる。

### Step 6. $S^{\times,1}$ 内を探索

$$
[D(u)]_{\mathrm{prim}}=0
$$

となる $u\in S^{\times,1}$ が存在するかを調べる。

存在すれば $N_3$-共役、存在しなければ $N_3$-非共役である。

---

## 11. 「正しい lift」を最初に作る恩恵

ambient space

$$
\frac12L\rtimes Sp(H_\mathbb Z)
$$

の中で共役方程式を解くだけなら、Johnson part は $\frac12L$ を自由に動けてしまう。

しかし、その解が

$$
\rho_3(\operatorname{Aut}_{\partial}\pi)
$$

から来る保証はない。

BBB 型の整数格子条件で正しい lift

$$
(\nu_Q,Q)
\in\rho_3(\operatorname{Aut}_{\partial}\pi)
$$

を一つ選ぶと、残りの許される自由度が

$$
\boxed{\nu_Q+L}
$$

に正確に限定される。

その結果、

$$
D_Q\in L
$$

が保証され、さらに lift の変更は

$$
D_Q\mapsto D_Q-(1-R_\psi\cdot)w,
\qquad w\in L
$$

だけになる。

したがって初めて、整数 primitive cokernel class

$$
[D_Q]_{\mathrm{prim}}
$$

が自然かつ well-defined に定義できる。

要約すると、

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

を作ってから

$$
[D_Q]_{\mathrm{prim}}
$$

を取ることである。

---

## 13. genus 2 の特別な場合

$g=2$ では

$$
\Lambda^3H_\mathbb Z
\cong
H_\mathbb Z
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
N_2\text{-共役}
\Longrightarrow
N_3\text{-共役}.
}
$$

本格的な $N_3$ obstruction 検査が必要になるのは genus $3$ 以上である。

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

を直接計算する公式を確定することである。

これができれば、$N_3$ 共役判定は

1. Yang・S-pair による $N_2$ 共役子と中心化群の計算
2. extended Johnson 成分の計算
3. BBB 型の正しい lift の計算
4. 整数 primitive cokernel class の計算
5. $S^{\times,1}$ 内の探索

という完全に機械的な手順になる。

---

## 参考

- J. S. Birman, T. E. Brendle, N. Broaddus, *Calculating the image of the second Johnson–Morita representation*.
- D. Johnson, Torelli 群の第一 Johnson 準同型と $\tau_1(\mathcal I_{g,1})=\Lambda^3H_\mathbb Z$.
- S. Morita, Johnson 準同型の mapping class group への拡張.
- `kiyoh.pdf`
- `simpleness.pdf`
- `研究メモ｜Q(c)によるYang・S-pair共役判定の整理.md`
