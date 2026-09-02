# 研究メモ｜N₃共役判定と primitive Johnson obstruction

更新日: 2026-09-02

## 位置づけ

研究進捗ツリーの

`3｜N₃ 共役判定` → `3.1｜Johnson obstruction の適用方法の整理`

に対応する研究メモ。

目的は、$H=N_2$ 上で共役である二つのモノドロミー $\phi,\psi$ が $N_3$ 上でも共役かどうかを、$H$ 上の共役子を与える Yang・S-pair の算術データと Johnson 成分から判定する形に整理することである。

---

## 1. 基本設定

$H=N_2$ とし、

$$
R_\phi:=\rho_2(\phi),\qquad R_\psi:=\rho_2(\psi).
$$

$H$ 上で $\phi,\psi$ が共役であると仮定する。

Yang・S-pair の計算によって、まず一つ

$$
\mathfrak a_A=(cu_0)\mathfrak a_B,
\qquad u_0\in S^{\times,1}
$$

を満たす $u_0$ を取り、対応する $Sp(H_\mathbb Z)$-共役子を

$$
Q_0:=Q(cu_0)
$$

とする。したがって

$$
R_\psi=Q_0R_\phi Q_0^{-1}.
$$

$R_\phi$ の $Sp$-中心化群は、仮定のもとで $S^{\times,1}$ により

$$
v\longmapsto C(v)
$$

とパラメータ化される。

したがって、$H$ 上の全共役子は

$$
Q_0C(v),\qquad v\in S^{\times,1}
$$

と書ける。

ここで、$H$ 共役判定で最初に選んだ $u_0$ と、$N_3$ 共役判定で中心化群方向に動かす $v$ は役割が異なる。最終的には $u=u_0v$ とまとめて $Q(cu)$ と書くこともできるが、階層的判定では $u_0$ と $v$ を分けておく方が論理構造が明確である。

---

## 2. $N_3$ と Johnson 成分

$N_3$ に対して

$$
1\to \Lambda^3H_\mathbb Z
\to \operatorname{Aut}_{\partial}(N_3)
\to Sp(H_\mathbb Z)
\to 1
$$

を用いる。

固定した symplectic expansion に関する extended Johnson 成分を

$$
u_\phi,\qquad u_\psi
$$

と書く。

座標的には

$$
\rho_3(\phi)=(u_\phi,R_\phi),
\qquad
\rho_3(\psi)=(u_\psi,R_\psi)
$$

と考える。

---

## 3. fixed-$Q$ obstruction

まず $H$ 上の共役子 $Q$ を一つ固定する。

$Q$ の $N_3$-lift を一つ $\widetilde Q\in\operatorname{Aut}_{\partial}(N_3)$ とすると、

$$
\Delta_Q
:=
\widetilde Q^{-1}\rho_3(\psi)\widetilde Q\rho_3(\phi)^{-1}
\in \Lambda^3H_\mathbb Z.
$$

$\widetilde Q$ を同じ $Q$ の別の lift に変えると、$\Delta_Q$ は

$$
(1-R_\phi\cdot)w,
\qquad w\in\Lambda^3H_\mathbb Z
$$

だけ変化する。

したがって

$$
[\Delta_Q]
\in
\operatorname{Coker}(1-R_\phi\cdot)
$$

は lift の選択によらない。

重要なのは、cokernel class だけを見ると $\widetilde Q$ 自身の Johnson 成分は不要になることである。

実際、

$$
\boxed{
[\Delta_Q]
=
[Q^{-1}\cdot u_\psi-u_\phi]
}
$$

となる。

すなわち、$Q$ の $N_3$-lift を具体的に構成する必要はない。

---

## 4. primitive quotient

symplectic form を $\omega$ とし、

$$
P_\mathbb Z
:=
\Lambda^3H_\mathbb Z/(H_\mathbb Z\wedge\omega)
$$

を integral primitive quotient とする。

fibered knot の場合に用いている条件 $|f(1)|=1$ のもとでは、$H\wedge\omega$ 成分における $1-R_\phi$ は unimodular であるため、Johnson obstruction は primitive quotient に完全に落とせる。

そこで

$$
K_{\mathrm{prim}}(\phi)
:=
\operatorname{Coker}
\left(
1-R_\phi\cdot:
P_\mathbb Z\to P_\mathbb Z
\right)
$$

と置く。

$\psi$ 側にも同様に $K_{\mathrm{prim}}(\psi)$ を定める。

$Q$ が

$$
R_\psi=QR_\phi Q^{-1}
$$

を満たすので、$Q$ は自然な同型

$$
Q:\ K_{\mathrm{prim}}(\phi)
\xrightarrow{\sim}
K_{\mathrm{prim}}(\psi)
$$

を誘導する。

したがって fixed-$Q$ obstruction は

$$
\boxed{
[Q^{-1}\cdot u_\psi-u_\phi]_{\mathrm{prim}}
}
$$

で表される。

---

## 5. 中心化群方向に共役子を動かす

基準の $H$-共役子を $Q_0=Q(cu_0)$ とする。

$H$ 上の他の共役子は

$$
Q_0C(v),\qquad v\in S^{\times,1}
$$

である。

一見すると、$C(v)$ の $N_3$-lift $\widetilde C(v)$ の Johnson 成分も新たに計算する必要があるように見える。

しかし、ここでも cokernel に落とすと lift の Johnson 成分は消える。

$\widetilde C(v)$ を任意の lift とすると、中心化群 lift に由来する障害は

$$
\widetilde C(v)^{-1}
\rho_3(\phi)
\widetilde C(v)
\rho_3(\phi)^{-1}
$$

であるが、その primitive cokernel class は

$$
\boxed{
[C(v)^{-1}\cdot u_\phi-u_\phi]_{\mathrm{prim}}
}
$$

となる。

したがって $\widetilde C(v)$ の Johnson 成分も具体的には不要である。

---

## 6. 二つの障害の相殺

基準共役子 $Q_0$ による障害と、中心化群方向 $C(v)$ による障害を合わせると、

$$
[\Delta_v]_{\mathrm{prim}}
=
C(v)^{-1}\cdot
[Q_0^{-1}\cdot u_\psi-u_\phi]_{\mathrm{prim}}
+
[C(v)^{-1}\cdot u_\phi-u_\phi]_{\mathrm{prim}}.
$$

両項をまとめると

$$
\boxed{
[\Delta_v]_{\mathrm{prim}}
=
[C(v)^{-1}Q_0^{-1}\cdot u_\psi-u_\phi]_{\mathrm{prim}}.
}
$$

したがって $N_3$ 共役子が存在するための条件は

$$
\exists v\in S^{\times,1}
\quad\text{such that}\quad
[C(v)^{-1}Q_0^{-1}\cdot u_\psi-u_\phi]_{\mathrm{prim}}=0.
$$

これに $Q_0C(v)$ を作用させると、より対称な形

$$
\boxed{
[u_\psi]_{\mathrm{prim},\psi}
=
Q_0C(v)\cdot
[u_\phi]_{\mathrm{prim},\phi}
}
$$

を得る。

これが実用上の最終判定式である。

---

## 7. 最終判定

### 段階的な形

まず $H$ 共役判定で一つ $u_0\in S^{\times,1}$ を見つけ、

$$
\mathfrak a_A=(cu_0)\mathfrak a_B
$$

および

$$
Q_0=Q(cu_0)
$$

を得る。

その後、$N_3$ 共役判定では

$$
\boxed{
\phi,\psi\text{ が }N_3\text{-共役}
\iff
\exists v\in S^{\times,1}:
[u_\psi]_{\mathrm{prim},\psi}
=
Q_0C(v)\cdot[u_\phi]_{\mathrm{prim},\phi}.
}
$$

### パラメータをまとめた形

$u=u_0v$ と置けば

$$
Q_0C(v)=Q(cu_0)C(v)=Q(cu),
$$

したがって

$$
\boxed{
\phi,\psi\text{ が }N_3\text{-共役}
\iff
\exists u\in S^{\times,1}:
[u_\psi]_{\mathrm{prim},\psi}
=
Q(cu)\cdot[u_\phi]_{\mathrm{prim},\phi}.
}
$$

ただし、研究の論理構造としては $H$ 共役判定と $N_3$ 共役判定を区別するため、$u_0$ と $v$ を分けた「段階的な形」を基本とする方がよい。

---

## 8. 重要な帰結

### 8.1 探索空間は増えない

$N_3$ に上がると kernel $\Lambda^3H_\mathbb Z$ の自由度が現れるが、その自由度は cokernel class に落とすことで吸収される。

したがって、$N_3$ 共役判定で新しい探索変数を導入する必要はない。

$H$ 共役判定と同じく、探索するのは

$$
S^{\times,1}
$$

の中だけである。

階層を上げることで探索空間が大きくなるのではなく、同じ算術的パラメータ空間に対して、より強い条件

$$
[u_\psi]_{\mathrm{prim},\psi}
=
Q_0C(v)\cdot[u_\phi]_{\mathrm{prim},\phi}
$$

が追加される。

### 8.2 lift の Johnson 成分は不要

最終判定に必要なのは

- $u_\phi,u_\psi$
- $H$ 上の共役子 $Q_0$
- 中心化群作用 $C(v)$
- primitive cokernel

である。

一方、以下は最終的には不要である。

- $Q_0$ の $N_3$-lift の Johnson 成分
- $C(v)$ の $N_3$-lift の Johnson 成分

これらはすべて $(1-R_\phi\cdot)$ の像に入り、cokernel で消える。

### 8.3 $H$ 共役だが $N_3$ 非共役は起こり得る

$H$ 共役判定を通る $u_0$ が存在しても、

$$
[u_\psi]_{\mathrm{prim},\psi}
=
Q_0C(v)\cdot[u_\phi]_{\mathrm{prim},\phi}
$$

を満たす $v\in S^{\times,1}$ が存在するとは限らない。

この不成立が $N_3$ で新たに現れる obstruction である。

---

## 9. genus $2$ の場合

$g=2$ では

$$
\Lambda^3H_\mathbb Z\cong H_\mathbb Z
$$

が $Sp$-equivariant に成り立つ。

fibered knot の条件 $|f(1)|=1$ のもとでは

$$
1-R_\phi\cdot
$$

は unimodular となり、対応する cokernel は $0$ である。

したがって genus $2$ では

$$
\boxed{
H=N_2\text{ 上で共役なら、自動的に }N_3\text{ 上でも共役する。}
}
$$

よって genus $2$ では $N_3$ obstruction の具体的検査は不要である。

---

## 10. 現時点での判定フロー

$$
\text{Yang・S-pair により }H\text{-共役判定}
$$

$$
\Downarrow
$$

$$
\mathfrak a_A=(cu_0)\mathfrak a_B,
\qquad Q_0=Q(cu_0)
$$

$$
\Downarrow
$$

$$
[u_\phi]_{\mathrm{prim},\phi},
\quad
[u_\psi]_{\mathrm{prim},\psi}
\text{ を計算}
$$

$$
\Downarrow
$$

$$
\exists v\in S^{\times,1}:
[u_\psi]_{\mathrm{prim},\psi}
=
Q_0C(v)\cdot[u_\phi]_{\mathrm{prim},\phi}
\ ?
$$

$$
\Downarrow
$$

$$
\begin{cases}
\text{Yes} &\Rightarrow N_3\text{-共役},\\
\text{No} &\Rightarrow N_3\text{-非共役}.
\end{cases}
$$

この形では、$N_2\to N_3$ に上がっても探索範囲そのものは $S^{\times,1}$ のままであり、Johnson obstruction は同じ探索空間上の追加条件として現れる。
