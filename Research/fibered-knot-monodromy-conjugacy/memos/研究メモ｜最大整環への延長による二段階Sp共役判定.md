# 研究メモ｜最大整環への延長による二段階 Sp 共役判定

## 1. 設定

共通の既約相反多項式をもつ

$$
A,B\in \operatorname{Sp}(2g,\mathbb Z)
$$

を考える。多項式の根を $\alpha$ とし、

$$
F=\mathbb Q(\alpha),\qquad R=\mathbb Z[\alpha],\qquad \mathcal O_F=\text{the ring of integers of }F
$$

とする。また、$\widetilde{\alpha}=\alpha^{-1}$ で定まる対合を $\widetilde{\phantom{x}}$ と書く。

Yang の対応により、$A,B$ からそれぞれ S-pair

$$
(\mathfrak a_A,s_A),\qquad (\mathfrak a_B,s_B)
$$

を得る。

ここで

$$
\mathfrak A_A:=\mathfrak a_A\mathcal O_F,\qquad
\mathfrak A_B:=\mathfrak a_B\mathcal O_F
$$

と、S-pair のイデアル成分を最大整環へ延長する。

Yang の定理より、Sp 共役なら S-pair は同値である。したがって以下の二段階の obstruction が得られる。

---

## 2. Obstruction (1)：延長イデアルのイデアル類

$$
I:=\mathfrak A_A\mathfrak A_B^{-1}
$$

とおく。

もし $A$ と $B$ が Sp 共役なら、Yang の S-pair 同値性より、ある非零元

$$
\lambda,\mu\in R
$$

が存在して

$$
\lambda\mathfrak a_A=\mu\mathfrak a_B
$$

となる。これを $\mathcal O_F$ へ延長すると

$$
\lambda\mathfrak A_A=\mu\mathfrak A_B,
$$

したがって

$$
I=\mathfrak A_A\mathfrak A_B^{-1}
=\left(\frac{\mu}{\lambda}\right)
$$

は主イデアルである。

従って、

$$
\boxed{
I\text{ が非主イデアル}
\quad\Longrightarrow\quad
A\not\sim_{\mathrm{Sp}}B
}
$$

を得る。

これは

$$
[\mathfrak A_A]\neq [\mathfrak A_B]
\in \operatorname{Cl}(\mathcal O_F)
$$

なら Sp 非共役、という必要条件である。

---

## 3. Obstruction (2)：第二成分の norm-unit class

Obstruction (1) を通過し、

$$
I=(c),\qquad c\in F^\times
$$

とする。すなわち

$$
\mathfrak A_A=c\,\mathfrak A_B.
$$

このとき

$$
\boxed{
r:=\frac{1}{c\widetilde c}\frac{s_A}{s_B}}
$$

と定める。

また

$$
C_{\mathcal O}
:=
\{u\widetilde u\mid u\in\mathcal O_F^\times\}
$$

とする。

もし $A$ と $B$ が Sp 共役なら、Yang の S-pair 同値性より

$$
\lambda\widetilde\lambda\,s_A
=
\mu\widetilde\mu\,s_B
$$

も成立する。

一方、

$$
\lambda\mathfrak A_A=\mu\mathfrak A_B
$$

と $\mathfrak A_A=c\mathfrak A_B$ から

$$
\frac{\lambda c}{\mu}\in\mathcal O_F^\times
$$

である。そこで

$$
u:=\frac{\lambda c}{\mu}\in\mathcal O_F^\times
$$

とおけば、

$$
\frac{s_A}{s_B}
=
\frac{\mu\widetilde\mu}{\lambda\widetilde\lambda}
$$

より

$$
\begin{aligned}
r
&=
\frac{1}{c\widetilde c}
\frac{s_A}{s_B}\\
&=
\frac{1}{c\widetilde c}
\frac{\mu\widetilde\mu}{\lambda\widetilde\lambda}\\
&=
\frac{1}{u\widetilde u}.
\end{aligned}
$$

$u^{-1}\in\mathcal O_F^\times$ なので

$$
r\in C_{\mathcal O}.
$$

従って、

$$
\boxed{
r\notin C_{\mathcal O}
\quad\Longrightarrow\quad
A\not\sim_{\mathrm{Sp}}B}
$$

を得る。

---

## 4. $R=\mathcal O_F$ の場合

もし

$$
R=\mathbb Z[\alpha]=\mathcal O_F
$$

なら、最大整環への延長による情報損失はない。

この場合、Obstruction (1) を通過して $I=(c)$ となり、さらに

$$
r\in C_{\mathcal O}
$$

が成立すれば、二つの S-pair は Yang の意味で同値である。

したがって

$$
\boxed{
R=\mathcal O_F
\quad\Longrightarrow\quad
r\in C_{\mathcal O}
\iff
A\sim_{\mathrm{Sp}}B
}
$$

ただし、もちろん Obstruction (1) を通過していることを前提とする。

---

## 5. $R\subsetneq\mathcal O_F$ の場合

$$
R\subsetneq\mathcal O_F
$$

の場合には、

$$
\mathfrak a\longmapsto\mathfrak a\mathcal O_F
$$

によって元の $R$-ideal の情報が失われる可能性がある。

したがって、

$$
I=(c),
\qquad
r\in C_{\mathcal O}
$$

まで成立しても、元の S-pair が $R$ 上で同値であるとは限らない。

従って

$$
\boxed{
R\subsetneq\mathcal O_F
\quad\Longrightarrow\quad
I=(c),\ r\in C_{\mathcal O}
\text{ だけでは共役かどうか不明}
}
$$

である。

---

## 6. 類数 $h_F=1$ の場合

$$
h_F=1
$$

なら $\mathcal O_F$ は PID なので、Obstruction (1) は自動的に通過する。

$\alpha$-固有ベクトルを

$$
v_A=(v_{A,1},\ldots,v_{A,2g}),
\qquad
v_B=(v_{B,1},\ldots,v_{B,2g})
$$

とし、

$$
g_A:=\gcd_{\mathcal O_F}(v_{A,1},\ldots,v_{A,2g}),
$$

$$
g_B:=\gcd_{\mathcal O_F}(v_{B,1},\ldots,v_{B,2g})
$$

とする。このとき

$$
\mathfrak A_A=(g_A),
\qquad
\mathfrak A_B=(g_B),
$$

したがって

$$
I
=
\mathfrak A_A\mathfrak A_B^{-1}
=
\left(\frac{g_A}{g_B}\right).
$$

よって

$$
\boxed{c=\frac{g_A}{g_B}}
$$

と簡単に取れる。

さらに

$$
u_A:=\frac{s_A}{g_A\widetilde g_A},
\qquad
u_B:=\frac{s_B}{g_B\widetilde g_B}
$$

とおけば、

$$
\boxed{
r=\frac{u_A}{u_B}}
$$

となる。

したがって $h_F=1$ の場合には、一般の二段階判定が、以前の $u$-class の比較にそのまま帰着する。

---

## 7. 判定フロー

$$
(\mathfrak a_A,s_A),\ (\mathfrak a_B,s_B)
$$

から

$$
\mathfrak A_A=\mathfrak a_A\mathcal O_F,
\qquad
\mathfrak A_B=\mathfrak a_B\mathcal O_F
$$

を作る。

### Step 1

$$
I=\mathfrak A_A\mathfrak A_B^{-1}
$$

を調べる。

- $I$ が非主イデアル：

  $$
  \boxed{A\not\sim_{\mathrm{Sp}}B}
  $$

- $I=(c)$：Step 2 へ。

### Step 2

$$
r=\frac{1}{c\widetilde c}\frac{s_A}{s_B}
$$

を計算し、

$$
r\stackrel{?}{\in}C_{\mathcal O}
$$

を調べる。

- $r\notin C_{\mathcal O}$：

  $$
  \boxed{A\not\sim_{\mathrm{Sp}}B}
  $$

- $r\in C_{\mathcal O}$：

  $$
  \boxed{
  \begin{cases}
  A\sim_{\mathrm{Sp}}B, & R=\mathcal O_F,\\
  \text{不明}, & R\subsetneq\mathcal O_F.
  \end{cases}}
  $$

---

## 8. 位置づけ

この判定法は、Yang の S-pair を最大整環へ粗視化して

$$
\boxed{
\text{ideal-class obstruction}
\longrightarrow
\text{norm-unit obstruction}
}
$$

の二段階で利用するものである。

類数 $h_F=1$ は理論上の必須仮定ではない。$h_F=1$ の役割は、第一段階を自動的に通過させ、さらに

$$
c=\frac{\gcd_{\mathcal O_F}(v_A)}{\gcd_{\mathcal O_F}(v_B)}
$$

と明示的に取れるようにすることである。

一方、$R=\mathcal O_F$ は、この粗視化判定が必要条件だけでなく完全な共役判定になるための条件である。

## 9. 参考

Q. Yang, *Conjugacy classes in integral symplectic groups*, Linear Algebra and its Applications **418** (2006), 614–624.

- Lemma 6：Sp 共役と S-pair 同値性。
- Lemmas 8–10：S-pair のスカラー変換および同一 ideal class 上での第二成分の比較。
- Theorem 1.2：整閉の場合の ideal-class part と unit-norm part の構造。
