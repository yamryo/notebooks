# 研究メモ｜Q(c)によるYang・S-pair共役判定の整理

## 位置づけ

研究進捗ツリーの `2｜Sp₄(Z) での共役判定` に属する研究メモ。

既存の Yang・S-pair による共役判定手順を、候補共役子

$$
Q(c)=M_BT(c)M_A^{-1}
$$

を中心に据えて整理し直す。

ここで重要なのは、任意の $c\in F^\times$ に対して $Q(c)$ はすでに $\mathbb Q$ 上の共役子であり、問題は

$$
Q(c)\in Sp(2g,\mathbb Z)
$$

となる $c$ を見つけることだ、という見方である。

---

## 1. 設定

$A,B\in Sp(2g,\mathbb Z)$ が同じ既約 reciprocal polynomial $f(t)$ を特性多項式にもつとする。

$f$ の根を $\alpha$ とし、

$$
F=\mathbb Q(\alpha),\qquad R=\mathbb Z[\alpha]
$$

とおく。また involution を

$$
\widetilde\alpha=\alpha^{-1}
$$

で定める。

power basis を

$$
e=(1,\alpha,\ldots,\alpha^{2g-1})^T
$$

とする。$A,B$ の $\alpha$-固有ベクトルをそれぞれ

$$
v_A=M_Ae,\qquad v_B=M_Be
$$

と書く。

$c\in F^\times$ に対し、$T(c)$ を power basis に関する multiplication by $c$ の行列とする：

$$
T(c)e=ce.
$$

したがって

$$
T(c_1)T(c_2)=T(c_1c_2),
$$

特に $T(c)$ と $T(\alpha)$ は可換する。

Yang の S-pair を

$$
S_A=(\mathfrak a_A,a_A),\qquad
S_B=(\mathfrak a_B,a_B)
$$

とする。ここで $\mathfrak a_A,\mathfrak a_B$ は、それぞれ $v_A,v_B$ の座標が生成する $R$-ideal である。

---

## 2. 候補共役子 $Q(c)$ と全 $\mathbb Q$-共役子

$c\in F^\times$ に対して

$$
\boxed{Q(c):=M_BT(c)M_A^{-1}}
$$

と定める。

$Av_A=\alpha v_A$ より

$$
M_A^{-1}AM_Ae=\alpha e=T(\alpha)e.
$$

$e$ は $F$ の $\mathbb Q$-basis なので

$$
M_A^{-1}AM_A=T(\alpha).
$$

同様に

$$
M_B^{-1}BM_B=T(\alpha).
$$

したがって

$$
A=M_AT(\alpha)M_A^{-1},
\qquad
B=M_BT(\alpha)M_B^{-1}.
$$

さらに $T(c)$ は $T(\alpha)$ と可換するので、任意の $c\in F^\times$ に対して

$$
\boxed{B=Q(c)AQ(c)^{-1}}
$$

が $\mathbb Q$ 上で成立する。同値な形では

$$
A=Q(c)^{-1}BQ(c)
$$

である。

### 補題：$Q(c)$ は全ての $\mathbb Q$-共役子を尽くす

$$
\boxed{
\{Q\in GL_{2g}(\mathbb Q)\mid B=QAQ^{-1}\}
=
\{Q(c)\mid c\in F^\times\}.
}
$$

実際、$B=QAQ^{-1}$ を満たす $Q\in GL_{2g}(\mathbb Q)$ を任意に取って

$$
X:=M_B^{-1}QM_A
$$

とおく。このとき $QA=BQ$ と

$$
M_A^{-1}AM_A=M_B^{-1}BM_B=T(\alpha)
$$

から

$$
XT(\alpha)=T(\alpha)X
$$

を得る。

一方、$\alpha$ の最小多項式は次数 $2g$ の既約多項式 $f$ であるから、$T(\alpha)$ の $M_{2g}(\mathbb Q)$ における中心化環は

$$
C_{M_{2g}(\mathbb Q)}(T(\alpha))
=
\mathbb Q[T(\alpha)]
=
T(F)
$$

である。したがって、ある一意な $c\in F$ に対して

$$
X=T(c)
$$

となる。$X$ は可逆なので $c\ne0$、すなわち $c\in F^\times$ であり、

$$
Q=M_BXM_A^{-1}=M_BT(c)M_A^{-1}=Q(c)
$$

を得る。逆 inclusion は上で確認済みである。

よって

$$
Q(c)\in Sp(2g,\mathbb Z)
$$

となる $c$ を探すことは、単なる候補族の探索ではなく、$A$ を $B$ へ移す $Sp$-共役子の全探索になっている。

---

## 3. $Q(c)\in Sp(2g,\mathbb Z)$ の二条件

Yang の S-pair 条件は

$$
\boxed{\mathfrak a_A=c\mathfrak a_B}
\tag{I}
$$

および

$$
\boxed{a_A=c\widetilde c\,a_B}
\tag{II}
$$

である。

### 3.1 条件 (I)：整数格子条件

$Q(c)v_A=M_BT(c)e=cv_B$ なので、$Q(c)$ は $v_A$ の座標格子を $cv_B$ の座標格子へ移す。

したがって

$$
\mathfrak a_A=c\mathfrak a_B
$$

は

$$
\operatorname{row}_{\mathbb Z}(M_A)
=
\operatorname{row}_{\mathbb Z}(M_BT(c))
$$

と同値である。

これは、ある $U\in GL(2g,\mathbb Z)$ が存在して

$$
M_BT(c)=UM_A
$$

となることと同値であり、その $U$ は

$$
U=M_BT(c)M_A^{-1}=Q(c)
$$

である。

よって

$$
\boxed{
\mathfrak a_A=c\mathfrak a_B
\iff
Q(c)\in GL(2g,\mathbb Z)
}
$$

となる。

すなわち条件 (I) は、$Q(c)$ の整数性・unimodularity を表す条件である。

### 3.2 条件 (II)：symplectic 条件

条件 (I) が成立して $Q(c)\in GL(2g,\mathbb Z)$ となっているとき、

$$
a_A=c\widetilde c\,a_B
$$

が $Q(c)$ を symplectic にする条件である。

したがって

$$
\boxed{
Q(c)\in Sp(2g,\mathbb Z)
\iff
\begin{cases}
\mathfrak a_A=c\mathfrak a_B,\\
a_A=c\widetilde c\,a_B.
\end{cases}
}
$$

この形にすると、S-pair の二条件はそれぞれ

- $\mathfrak a_A=c\mathfrak a_B$：$Q(c)$ を整数 unimodular 行列にする条件
- $a_A=c\widetilde c\,a_B$：$Q(c)$ を symplectic にする条件

と明確に分離される。

---

## 4. $R=\mathcal O_F$ の場合

まず最大 order の場合を整理する。

### Step 1. ideal 条件を解く

$$
\mathfrak a_A=c_0\mathfrak a_B
$$

となる $c_0\in F^\times$ を求める。

この時点で

$$
Q(c_0)\in GL(2g,\mathbb Z)
$$

である。

### Step 2. symplectic 条件を unit で補う

$$
r:=\frac{a_A}{c_0\widetilde{c_0}\,a_B}
$$

とおく。

次に

$$
r=u\widetilde u
$$

を満たす $u\in\mathcal O_F^\times$ を探す。すなわち

$$
r\in C_{\mathcal O}
:=
\{u\widetilde u:u\in\mathcal O_F^\times\}
$$

を判定し、成立する場合には明示的な witness $u$ を保持する。

### Step 3. 共役子を作る

$$
c=c_0u
$$

とおけば

$$
\mathfrak a_A=c\mathfrak a_B,
$$

かつ

$$
a_A=c\widetilde c\,a_B.
$$

したがって

$$
\boxed{Q(c)=M_BT(c)M_A^{-1}\in Sp(2g,\mathbb Z)}.
$$

特に $r=1$ の場合は $u=1$ としてよい。

---

## 5. $R\ne\mathcal O_F$ の場合：$\mathcal O_F$ への拡張

$R$ が maximal order でない場合、元の ideal 条件

$$
\mathfrak a_A=c\mathfrak a_B
$$

を直接解く前に、まず $\mathcal O_F$ 上へ拡張して粗く解く。

$$
I_A:=\mathfrak a_A\mathcal O_F,\qquad
I_B:=\mathfrak a_B\mathcal O_F.
$$

### Step 1. 最大 order 上で ideal 部分を合わせる

$$
\boxed{I_A=c_0I_B}
$$

となる $c_0\in F^\times$ を探す。

特に $h_F=1$ なら $I_AI_B^{-1}$ は principal なので、その generator を一つ求めればよい。

ただし、これは元の条件

$$
\mathfrak a_A=c\mathfrak a_B
$$

より弱い。ここでは $R$ と $\mathcal O_F$ の差をいったん忘れている。

### Step 2. norm 条件を unit で補う

$$
r:=\frac{a_A}{c_0\widetilde{c_0}\,a_B}
$$

とおく。

次に

$$
\boxed{r=u\widetilde u}
$$

を満たす

$$
u\in\mathcal O_F^\times
$$

を探す。

一つ witness $u$ が見つかれば

$$
c_1:=c_0u
$$

とおくことで

$$
I_A=c_1I_B,
$$

かつ

$$
a_A=c_1\widetilde{c_1}\,a_B
$$

となる。

したがって $\mathcal O_F$ 上では二条件がそろう。

### Step 3. 元の $R$-ideal 条件へ戻る

最後に

$$
\boxed{\mathfrak a_A\stackrel{?}{=}c_1\mathfrak a_B}
$$

を調べる。

行列の言葉では

$$
\boxed{
Q(c_1)=M_BT(c_1)M_A^{-1}
\stackrel{?}{\in}GL(2g,\mathbb Z)
}
$$

を調べることと同じである。

これが成立すれば、Step 2 により symplectic 条件もすでに成立しているので

$$
\boxed{Q(c_1)\in Sp(2g,\mathbb Z)}
$$

となり、共役子が一つ得られる。

---

## 6. 最初の unit で $R$-ideal 条件が通らない場合

$r=u\widetilde u$ を満たす $u$ は一般に一意ではない。

一つの解 $u_0\in\mathcal O_F^\times$ があれば、他の解は

$$
u=u_0v
$$

で、

$$
v\widetilde v=1
$$

を満たす。

そこで

$$
\mathcal O_F^{\times,1}
:=
\{v\in\mathcal O_F^\times:v\widetilde v=1\}
$$

とおく。

最初の $u_0$ で

$$
\mathfrak a_A\ne c_0u_0\mathfrak a_B
$$

となっても、直ちに非共役とは結論できない。

調べるべき条件は

$$
\boxed{
\exists v\in\mathcal O_F^{\times,1}
\quad
\mathfrak a_A=c_0u_0v\,\mathfrak a_B
}
$$

である。

行列では

$$
\boxed{
\exists v\in\mathcal O_F^{\times,1}
\quad
Q(c_0u_0v)\in GL(2g,\mathbb Z)
}
$$

となる。

norm-one 条件は保たれているので、この $GL(2g,\mathbb Z)$ 条件が通れば自動的に

$$
Q(c_0u_0v)\in Sp(2g,\mathbb Z).
$$

この最後の探索が、$R\ne\mathcal O_F$ の場合の主要な難所となる。

---

## 7. 判定過程で現れる unit 群

判定手順では、unit の自由度が段階的に狭くなる。

まず norm 条件を解く段階では

$$
\boxed{\mathcal O_F^\times}
$$

の中から

$$
r=u\widetilde u
$$

を満たす $u$ を探す。

一つ $u_0$ が見つかった後は、norm 条件を保つ自由度だけが残るので

$$
\boxed{
\mathcal O_F^{\times,1}
=
\{v\in\mathcal O_F^\times:v\widetilde v=1\}
}
$$

の中を探索する。

したがって存在判定では

$$
\boxed{
\mathcal O_F^\times
\supset
\mathcal O_F^{\times,1}
}
$$

という絞り込みが起こる。

---

## 8. 一つ共役子が見つかった後：全共役子と中心化群

一つ

$$
c_*\in F^\times,
\qquad
Q(c_*)\in Sp(2g,\mathbb Z)
$$

が見つかったとする。

別の解を

$$
c=c_*s
$$

と書く。

ideal 条件

$$
\mathfrak a_A=c\mathfrak a_B
$$

と

$$
\mathfrak a_A=c_*\mathfrak a_B
$$

を比較すると

$$
s\mathfrak a_B=\mathfrak a_B.
$$

そこで $\mathfrak a_B$ の multiplier ring を

$$
S:=(\mathfrak a_B:\mathfrak a_B)
=
\{x\in F:x\mathfrak a_B\subseteq\mathfrak a_B\}
$$

とおくと、

$$
s\in S^\times.
$$

さらに第2 S-pair 条件を比較すると

$$
s\widetilde s=1.
$$

したがって

$$
S^{\times,1}
:=
\{s\in S^\times:s\widetilde s=1\}
$$

として、

$$
\boxed{
\{c\in F^\times:Q(c)\in Sp(2g,\mathbb Z)\}
=
c_*S^{\times,1}
}
$$

となる。

また $S\subseteq\mathcal O_F$ の場合には

$$
\boxed{
S^{\times,1}
\subseteq
\mathcal O_F^{\times,1}
\subseteq
\mathcal O_F^\times
}
$$

である。

したがって、判定から全共役子・中心化群の決定までを通して見ると、調べる unit の自由度は

$$
\boxed{
\mathcal O_F^\times
\supset
\mathcal O_F^{\times,1}
\supset
S^{\times,1}
}
$$

と段階的に狭まっていく。

行列側では、一つの共役子

$$
Q_*:=Q(c_*)
$$

が見つかれば、全共役子は $A,B$ の symplectic centralizer を用いて

$$
\boxed{
Z_{Sp(2g,\mathbb Z)}(B)\,Q_*
=
Q_*\,Z_{Sp(2g,\mathbb Z)}(A)
}
$$

と書ける。

さらに $s\in S^{\times,1}$ に対して

$$
M_BT(s)M_B^{-1}
$$

は $B$ を centralize し、

$$
Q(c_*s)
=
\bigl(M_BT(s)M_B^{-1}\bigr)Q_*
$$

となる。これにより $S^{\times,1}$ が中心化群の自由度を記述する。

---

## 9. 全体の判定フロー

$R\ne\mathcal O_F$ の場合の判定手順を、$Q(c)$ の言葉だけでまとめる。

1. S-pair
   $$
   (\mathfrak a_A,a_A),\qquad
   (\mathfrak a_B,a_B)
   $$
   を計算する。

2. 
   $$
   I_A=\mathfrak a_A\mathcal O_F,
   \qquad
   I_B=\mathfrak a_B\mathcal O_F
   $$
   とし、
   $$
   I_A=c_0I_B
   $$
   となる $c_0\in F^\times$ を求める。

3. 
   $$
   r=\frac{a_A}{c_0\widetilde{c_0}a_B}
   $$
   を計算し、
   $$
   r=u_0\widetilde{u_0},
   \qquad
   u_0\in\mathcal O_F^\times
   $$
   を満たす $u_0$ を探す。存在しなければ非共役。

4. 
   $$
   c_1=c_0u_0
   $$
   とし、
   $$
   Q(c_1)=M_BT(c_1)M_A^{-1}
   $$
   が $GL(2g,\mathbb Z)$ に入るかを調べる。

5. 入れば
   $$
   Q(c_1)\in Sp(2g,\mathbb Z)
   $$
   であり、共役子を一つ得る。

6. 入らなければ
   $$
   v\in\mathcal O_F^{\times,1}
   $$
   を動かし、
   $$
   Q(c_0u_0v)\in GL(2g,\mathbb Z)
   $$
   となる $v$ を探す。存在しなければ非共役。

7. 一つ $c_*$ が見つかった後、全ての共役子を求めるなら
   $$
   S=(\mathfrak a_B:\mathfrak a_B)
   $$
   を計算し、$S^{\times,1}$ を決定する。全解は
   $$
   c_*S^{\times,1}
   $$
   で与えられる。

---

## 10. この整理の要点

Yang の S-pair 判定を

$$
\boxed{
\text{候補 }Q(c)=M_BT(c)M_A^{-1}
\text{ を }Sp(2g,\mathbb Z)\text{ に落とす問題}
}
$$

とみなす。

その際、

$$
\boxed{\mathfrak a_A=c\mathfrak a_B}
$$

は $Q(c)$ を $GL(2g,\mathbb Z)$ に落とす条件、

$$
\boxed{a_A=c\widetilde c\,a_B}
$$

はさらに symplectic にする条件である。

$R\ne\mathcal O_F$ の場合、$\mathcal O_F$ への拡張は、まず maximal order 上で $c$ の ideal 部分を合わせ、その後

$$
\mathcal O_F^\times
\supset
\mathcal O_F^{\times,1}
\supset
S^{\times,1}
$$

と unit の自由度を順に絞りながら、最終的に

$$
Q(c)\in Sp(2g,\mathbb Z)
$$

を実現する $c$ を求める操作として理解できる。
