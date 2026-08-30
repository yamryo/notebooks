# 研究メモ｜最大整環への延長による Sp 共役の必要条件

## 1. 目的

Yang の S-pair による共役判定では、通常

\[
R=\mathbb Z[\alpha]
\]

上のイデアルと単数を扱う。ところが、非極大整環

\[
R\subsetneq\mathcal O_F,
\qquad F=\mathbb Q(\alpha)
\]

の場合、`F.unit_group()` が与える最大整環の単数群を、そのまま

\[
R^\times
\]

として使うことはできない。

本メモでは、最大整環の類数が1であるという仮定だけを用いて、最大整環へのイデアル延長から得られる **Sp 共役の必要条件** を整理する。この条件は一般には十分条件ではないが、非共役を検出する obstruction として利用できる。

## 2. 設定

共通の既約相反多項式をもつ二つの symplectic 行列を

\[
X_1,X_2\in\operatorname{Sp}_{2n}(\mathbb Z)
\]

とし、それぞれに対応する S-pair を

\[
(\mathfrak a_1,s_1),
\qquad
(\mathfrak a_2,s_2)
\]

とする。ここで

\[
\mathfrak a_i\subset R
\]

は固有ベクトルの成分が生成する integral $R$-ideal であり、$s_i\in R$ は S-pair の第二成分である。

相反性から、$F$ には

\[
\widetilde\alpha=\alpha^{-1}
\]

で定まる対合がある。この対合は代数的整数を代数的整数へ移すため、最大整環

\[
\mathcal O_F
\]

を保つ。

以下では

\[
h(\mathcal O_F)=1
\]

を仮定する。ただし

\[
R=\mathcal O_F
\]

は仮定しない。

## 3. 最大整環へのイデアル延長

各 $R$-ideal を最大整環へ延長して

\[
\mathfrak A_i
:=
\mathfrak a_i\mathcal O_F
\]

とする。

最大整環の類数が1なので、各 $\mathfrak A_i$ は単項であり、ある $g_i\in F^\times$ を用いて

\[
\mathfrak A_i=g_i\mathcal O_F
\]

と書ける。

そこで

\[
u_i
:=
\frac{s_i}{g_i\widetilde g_i}
\in F^\times
\]

および

\[
r
:=
\frac{u_1}{u_2}
=
\frac{s_1}{s_2}
\frac{g_2\widetilde g_2}{g_1\widetilde g_1}
\]

を定める。

この段階では、個々の $u_i$ が最大整環の単数であるとは仮定しない。以下で示すのは、Sp 共役ならば比 $r$ が最大整環の単数ノルムになる、という主張である。

## 4. 必要条件

最大整環の単数群と、その対合ノルムの像を

\[
U_{\mathcal O}
:=
\mathcal O_F^\times,
\]

\[
U_{\mathcal O}^+
:=
\{u\in U_{\mathcal O}\mid \widetilde u=u\},
\]

\[
C_{\mathcal O}
:=
\{\varepsilon\widetilde\varepsilon
\mid \varepsilon\in U_{\mathcal O}\}
\]

とする。

主張は

\[
\boxed{
X_1\sim_{\operatorname{Sp}_{2n}(\mathbb Z)}X_2
\quad\Longrightarrow\quad
r\in C_{\mathcal O}
}
\]

である。

したがって、その対偶として

\[
\boxed{
r\notin C_{\mathcal O}
\quad\Longrightarrow\quad
X_1\not\sim_{\operatorname{Sp}_{2n}(\mathbb Z)}X_2
}
\]

が得られる。

## 5. 導出

二つの行列が Sp 共役であると仮定する。Yang の S-pair の同値性により、ある非零元

\[
\lambda,\mu\in R
\]

が存在して

\[
\lambda\mathfrak a_1
=
\mu\mathfrak a_2
\]

および

\[
\lambda\widetilde\lambda s_1
=
\mu\widetilde\mu s_2
\]

が成り立つ。

最初の等式を最大整環へ延長すると

\[
\lambda g_1\mathcal O_F
=
\mu g_2\mathcal O_F.
\]

従って

\[
\varepsilon
:=
\frac{\mu g_2}{\lambda g_1}
\]

は最大整環の単数である。

第二の等式から

\[
\frac{s_1}{s_2}
=
\frac{\mu\widetilde\mu}
     {\lambda\widetilde\lambda}
\]

を得る。よって

\[
\begin{aligned}
r
&=
\frac{s_1}{s_2}
\frac{g_2\widetilde g_2}
     {g_1\widetilde g_1}\\
&=
\frac{\mu g_2}{\lambda g_1}
\frac{\widetilde\mu\widetilde g_2}
     {\widetilde\lambda\widetilde g_1}\\
&=
\varepsilon\widetilde\varepsilon.
\end{aligned}
\]

従って

\[
r\in C_{\mathcal O}.
\]

特に Sp 共役ならば、自動的に

\[
r\in\mathcal O_F^\times,
\qquad
\widetilde r=r
\]

も成り立つ。ただし、これら二条件だけでは $r\in C_{\mathcal O}$ より弱い。

## 6. 生成元の選択からの独立性

単項イデアルの生成元は一意ではない。別の生成元を

\[
g_i'=\eta_i g_i,
\qquad
\eta_i\in\mathcal O_F^\times
\]

とすると

\[
u_i'
=
\frac{u_i}{\eta_i\widetilde\eta_i}
\]

となる。そのため

\[
r'
=
r
\frac{\eta_2\widetilde\eta_2}
     {\eta_1\widetilde\eta_1}.
\]

従って $r$ 自体は生成元の選択で変化するが、その剰余類

\[
[r]
\in
U_{\mathcal O}^+/C_{\mathcal O}
\]

は変化しない。特に

\[
r\in C_{\mathcal O}
\]

かどうかは、$g_1,g_2$ の選択に依存しない。

## 7. 実際の判定手順

1. 固有ベクトルから S-pair

   \[
   (\mathfrak a_i,s_i)
   \]

   を構成する。

2. 最大整環を計算する。

   \[
   \mathcal O_F
   \]

3. 最大整環の類数が1であることを確認する。

4. 延長イデアルを計算する。

   \[
   \mathfrak A_i=\mathfrak a_i\mathcal O_F
   \]

5. 生成元 $g_i$ を求める。

   \[
   \mathfrak A_i=g_i\mathcal O_F
   \]

6. 比を計算する。

   \[
   r
   =
   \frac{s_1}{s_2}
   \frac{g_2\widetilde g_2}
        {g_1\widetilde g_1}
   \]

7. 次を確認する。

   \[
   r\in\mathcal O_F^\times,
   \qquad
   \widetilde r=r.
   \]

   どちらかが不成立なら Sp 非共役である。

8. 最大整環の単数群を計算し、ノルム方程式

   \[
   r=\varepsilon\widetilde\varepsilon,
   \qquad
   \varepsilon\in\mathcal O_F^\times
   \]

   を解く。

9. 解が存在しなければ Sp 非共役である。解が存在する場合は、この必要条件だけでは共役・非共役を決定できない。

## 8. 単数群による計算

Dirichlet の単数定理により

\[
\mathcal O_F^\times
\cong
\mu_F\times\mathbb Z^{r_1+r_2-1}.
\]

ねじれ生成元と基本単数を

\[
\xi,\varepsilon_1,\ldots,\varepsilon_m
\]

とすれば

\[
C_{\mathcal O}
=
\left\langle
\xi\widetilde\xi,
\varepsilon_1\widetilde{\varepsilon}_1,
\ldots,
\varepsilon_m\widetilde{\varepsilon}_m
\right\rangle.
\]

従って $r\in C_{\mathcal O}$ の判定は、単数群の指数ベクトル上の整数格子問題になる。自由部分は Smith 標準形で処理でき、ねじれ部分は有限合同条件として処理できる。

SageMath では最大整環の単数群を概念的に次のように取得する。

```sage
U = F.unit_group(proof=True)
U.rank()
U.zeta_order()
U.gens_values()
U.fundamental_units()
```

単数 $v$ の指数ベクトルは

```sage
U.log(v)
```

で取得できる。各生成元 $\varepsilon_j$ に対して

```sage
eps_j * tilde(eps_j)
```

を計算し、その指数ベクトルが生成する部分格子に `U.log(r)` が属するかを調べる。

## 9. なぜ十分条件ではないか

最大整環への延長は、元の $R$-加群としての情報を忘れる。特に

\[
R^\times\subseteq\mathcal O_F^\times
\]

であり、従って

\[
\{\eta\widetilde\eta\mid\eta\in R^\times\}
\subseteq
C_{\mathcal O}.
\]

最大整環上でノルム方程式が解けても、次のことは自動的には従わない。

- $\mathfrak a_1$ と $\mathfrak a_2$ が $R$-ideal として同値であること。
- 得られた最大整環の単数が元の $R$-格子を保つこと。
- 第二成分の比が $R^\times$ からの対合ノルムとして実現されること。

従って

\[
r\in C_{\mathcal O}
\]

は Sp 共役の必要条件ではあるが、一般には十分条件ではない。

## 10. 判定結果の意味

| 最大整環での判定 | 結論 |
|---|---|
| $r\notin\mathcal O_F^\times$ | Sp 非共役 |
| $\widetilde r\neq r$ | Sp 非共役 |
| $r\in U_{\mathcal O}^+$ だが $r\notin C_{\mathcal O}$ | Sp 非共役 |
| $r\in C_{\mathcal O}$ | この必要条件では判定不能 |

最後の場合には、元の非極大整環 $R$ に戻り、$R$-ideal の同値性と $R^\times$ のノルム像を直接調べる必要がある。

## 11. 補足

最大整環の類数1という仮定は、各延長イデアルを

\[
\mathfrak A_i=g_i\mathcal O_F
\]

と大域的に単項化するために用いた。類数1を仮定しない場合には、まず

\[
[\mathfrak A_1]=[\mathfrak A_2]
\]

が最大整環のイデアル類群で成り立つことが、別の必要条件になる。

## 12. 参考文献

- Q. Yang, *Conjugacy classes in integral symplectic groups*, Linear Algebra and its Applications 418 (2006), 614–624.
- Yang, Lemma 6：symplectic 共役と S-pair の同値性。
- Yang, Lemmas 8–10：S-pair のスカラー変換、同一イデアル部分での第二成分の比較、イデアル類が一致する場合の比較。
