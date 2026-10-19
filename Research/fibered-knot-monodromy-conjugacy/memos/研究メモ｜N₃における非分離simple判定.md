# 研究メモ｜$N_3$ における非分離 simple 判定

更新日: 2026-10-19

## 0. このメモの位置づけ

`simpleness.pdf` と `kiyoh.pdf` に書かれた $N_3$ 上の simpleness 条件を再検討した結果、次の点が重要だと分かった。

1. 「simple」を自由ホモトピーで定義する限り、separating simple curve と nonseparating simple curve を分ける必要がある。
2. $N_3$ の nonseparating-simple 判定では、$\langle l(x),|x|\rangle\in\mathbb Q|x|$ だけでは足りず、少なくとも $|x|$ の primitive 性が必要である。
3. primitive 性を加えると、$\langle l(x),|x|\rangle\in\mathbb Q|x|$ から逆向きも証明できる見通しが立った。
4. その証明では、**共役による補正**と **Torelli / Johnson による補正**を二段階で使う。

以下では nonseparating sector に限定して整理する。separating case $|x|=0$ は別問題として残す。

---

## 1. 定義と Fact 2.1 / 2.2 の注意点

`simpleness.pdf` の Definition 2.1 では、$x\in\pi$ が simple であるとは、その自由ホモトピー類が simple closed curve を含むことと定義している。

この定義では separating simple curve も含まれる。たとえば

$$
[x_1,y_1]
$$

は separating simple closed curve を表すが、その homology class は $0$ であり、自由群の primitive element ではない。

したがって、

$$
x\text{ simple}\Longrightarrow x\text{ primitive}
$$

を無条件で使うことはできない。

以後、主線では **nonseparating simple** を扱う。

### based element と free homotopy のずれ

さらに、自由ホモトピーで simple を定義すると、based element $x$ 自身は standard simple element の像そのものとは限らず、その共役である可能性がある。

したがって、現行の定義から自然に得られる形は

$$
\boxed{
x\text{ nonseparating-simple}
\iff
\exists f\in\operatorname{Aut}_{\partial}(\pi),\ \exists w\in\pi
\text{ such that }
x=w f(x_1)w^{-1}.
}
$$

`kiyoh.pdf` の Proposition 3.2 の証明では、内部自己同型によって $x$ を共役な based simple representative に取り替えてから $f(x_1)=x$ としているが、元の $x$ に戻す共役が $\operatorname{Aut}_{\partial}(\pi)$ に属することは示されていない。

したがって、free-homotopy の定義を維持するなら、Fact 2.1(ii) と Fact 2.2 は「共役まで含めた orbit」として書き直すのが安全である。

$N_k$ では対応して

$$
\boxed{
[x]_k\text{ nonseparating-simple}
\iff
\exists f\in\operatorname{Aut}_{\partial}(\pi),\ \exists w\in\pi
\text{ such that }
[x]_k=[w f(x_1)w^{-1}]_k.
}
$$

---

## 2. $N_3$ の座標と extended Johnson 項

symplectic expansion によって

$$
[z]_3\longmapsto (l(z),|z|)
$$

と座標化する。

一般の $f\in\operatorname{Aut}_{\partial}(\pi)$ に対して

$$
A=|f|\in Sp(H_{\mathbb Z})
$$

とすると、

$$
\boxed{
l(f(z))
=
A\,l(z)
+
\left\langle\tau_1^\theta(f),A|z|\right\rangle.
}
$$

ここで $\tau_1^\theta(f)$ は一般の $f$ に対する extended Johnson 成分である。

Torelli 元 $h\in\mathcal I_{g,1}$ では $A=\mathrm{id}$ なので、

$$
\boxed{
l(h(z))
=
l(z)+\langle\tau_1(h),|z|\rangle.
}
$$

また $\tau\in\Lambda^3H$ に対して

$$
\left\langle\langle\tau,X\rangle,X\right\rangle=0.
$$

したがって

$$
\boxed{
\langle l(f(z)),|f(z)|\rangle
=
A\langle l(z),|z|\rangle.
}
$$

---

## 3. standard simple element の contraction

規約

$$
l(x_1)=\frac12X_1\wedge Y_1
$$

および

$$
\langle X\wedge Y,Z\rangle
=
(Z\cdot X)Y-(Z\cdot Y)X
$$

より、

$$
\boxed{
\langle l(x_1),X_1\rangle
=
-\frac12X_1.
}
$$

したがって $y_0=f(x_1)$, $v=|y_0|=A(X_1)$ なら

$$
\boxed{
\langle l(y_0),v\rangle
=
-\frac12v.
}
$$

---

## 4. 共役による $l$-成分の変化

$y=w y_0 w^{-1}$ とし、

$$
a=|w|,\qquad v=|y_0|=|y|
$$

と置く。

$l$ の積公式から

$$
\boxed{
l(wy_0w^{-1})
=
l(y_0)+a\wedge v.
}
$$

したがって

$$
\begin{aligned}
\langle l(y),v\rangle
&=
-\frac12v+\langle a\wedge v,v\rangle\\
&=
\left(-\frac12+v\cdot a\right)v.
\end{aligned}
$$

ここで $v\cdot a\in\mathbb Z$ なので、nonseparating simple element については

$$
\boxed{
\langle l(y),|y|\rangle
\in
\left(\mathbb Z-\frac12\right)|y|.
}
$$

したがって $\mathbb Q|y|$ に入るという条件より強い離散的条件が成り立つ。

---

## 5. primitive 条件は不可欠

`simpleness.pdf` の Theorem 2.4 は

$$
[x]_3\text{ simple}
\iff
\langle l(x),|x|\rangle\in\mathbb Q|x|
$$

としているが、nonseparating simpleness を考えるなら primitive 条件が必要である。

反例は

$$
x=x_1^2.
$$

このとき

$$
|x|=2X_1
$$

は primitive ではない。一方

$$
l(x_1^2)=X_1\wedge Y_1
$$

なので

$$
\langle l(x),|x|\rangle
=
-2X_1
=
-|x|
\in\mathbb Q|x|.
$$

よって contraction 条件だけでは $[x]_3$ の nonseparating simpleness は従わない。

---

## 6. 修正版の候補定理

nonseparating sector では、正しい候補は次である。

$$
\boxed{
[x]_3\text{ is nonseparating-simple}
\iff
\begin{cases}
|x|\text{ is primitive in }H_{\mathbb Z},\\[1mm]
\langle l(x),|x|\rangle\in\mathbb Q|x|.
\end{cases}
}
$$

only-if は上の議論から従う。

以下、if part を示す。

---

## 7. if part の証明

$$
v:=|x|
$$

とし、

$$
v\text{ primitive},\qquad
\langle l(x),v\rangle=qv,\quad q\in\mathbb Q
$$

を仮定する。

### Step 1. homology class を合わせる

$v$ が primitive なので、

$$
\exists A\in Sp(H_{\mathbb Z})
\quad\text{such that}\quad
A(X_1)=v.
$$

$\rho_2(\operatorname{Aut}_{\partial}\pi)=Sp(H_{\mathbb Z})$ を使って $A$ を lift し、

$$
f_0\in\operatorname{Aut}_{\partial}(\pi),\qquad |f_0|=A
$$

を取る。

$$
y_0:=f_0(x_1).
$$

すると

$$
|y_0|=v,\qquad
\langle l(y_0),v\rangle=-\frac12v.
$$

### Step 2. $q$ は自動的に half-odd-integer になる

$|x|=|y_0|=v$ なので

$$
xy_0^{-1}\in\Gamma_2.
$$

したがって

$$
\delta_0:=l(x)-l(y_0)\in\Lambda^2H_{\mathbb Z}.
$$

よって

$$
\langle\delta_0,v\rangle
=
\left(q+\frac12\right)v
\in H_{\mathbb Z}.
$$

$v$ は primitive なので

$$
\boxed{
q+\frac12=n\in\mathbb Z.
}
$$

すなわち

$$
q\in\mathbb Z-\frac12.
$$

したがって、「$\mathbb Q v$ に入る」という条件は primitive 性と組み合わせると自動的に正しい half-integral parity を含んでいる。

### Step 3. 共役で scalar part を合わせる

symplectic lattice の unimodularity と $v$ の primitive 性から、

$$
v\cdot a=n
$$

となる $a\in H_{\mathbb Z}$ を取れる。

$|w|=a$ となる $w\in\pi$ を取り、

$$
y_1:=w y_0 w^{-1}
$$

と置く。

すると $y_1$ は nonseparating-simple のままで、

$$
|y_1|=v,
$$

かつ

$$
l(y_1)=l(y_0)+a\wedge v.
$$

したがって

$$
\langle l(y_1),v\rangle
=
\left(-\frac12+n\right)v
=
qv
=
\langle l(x),v\rangle.
$$

そこで

$$
\delta:=l(x)-l(y_1)
$$

と置けば、

$$
\boxed{
\delta\in\Lambda^2H_{\mathbb Z},
\qquad
\langle\delta,v\rangle=0.
}
$$

### Step 4. 残りの差を Johnson 項として表す

$v$ が primitive なので、

$$
v\cdot b=1
$$

となる $b\in H_{\mathbb Z}$ を取れる。

$$
\tau:=b\wedge\delta\in\Lambda^3H_{\mathbb Z}
$$

と置くと、

$$
\begin{aligned}
\langle\tau,v\rangle
&=
\langle b\wedge\delta,v\rangle\\
&=
(v\cdot b)\delta-b\wedge\langle\delta,v\rangle\\
&=
\delta.
\end{aligned}
$$

よって

$$
\boxed{
\delta=\langle\tau,v\rangle
\quad
(\tau\in\Lambda^3H_{\mathbb Z}).
}
$$

Johnson の全射性

$$
\tau_1(\mathcal I_{g,1})
=
\Lambda^3H_{\mathbb Z}
$$

より、

$$
\exists h\in\mathcal I_{g,1}
\quad\text{such that}\quad
\tau_1(h)=\tau.
$$

Torelli 元なので $|h|=\mathrm{id}$。したがって

$$
|h(y_1)|=v
$$

かつ

$$
\begin{aligned}
l(h(y_1))
&=
l(y_1)+\langle\tau_1(h),v\rangle\\
&=
l(y_1)+\delta\\
&=
l(x).
\end{aligned}
$$

よって $N_3$ の座標が一致し、

$$
[h(y_1)]_3=[x]_3.
$$

$h(y_1)$ は nonseparating-simple なので、

$$
\boxed{
[x]_3\text{ is nonseparating-simple}.
}
$$

これで if part が得られる。

---

## 8. 証明の構造

逆向きの補正は二段階に分かれる。

### (A) 共役による補正

$$
l(y_0)\longmapsto l(y_0)+a\wedge v
$$

により、

$$
\langle l(\,\cdot\,),v\rangle
$$

の $v$-方向の係数を整数だけ動かす。

これにより

$$
\langle l(y_1),v\rangle
=
\langle l(x),v\rangle
$$

まで合わせる。

### (B) Torelli / Johnson による補正

残差

$$
\delta=l(x)-l(y_1)
$$

は

$$
\langle\delta,v\rangle=0
$$

を満たす。

このとき

$$
\delta=\langle b\wedge\delta,v\rangle
$$

なので、Johnson の全射性を使って Torelli 元で残差を完全に消せる。

要するに

$$
\boxed{
\text{共役で scalar part を合わせる}
\quad\Longrightarrow\quad
\text{Torelli で kernel part を合わせる}.
}
$$

---

## 9. 現時点での結論

nonseparating sector では、次の修正版が有力であり、上記の議論で proof sketch まで得られた。

$$
\boxed{
[x]_3\text{ nonseparating-simple}
\iff
|x|\text{ primitive}
\text{ and }
\langle l(x),|x|\rangle\in\mathbb Q|x|.
}
$$

重要な点は以下。

- `simpleness.pdf` の Theorem 2.4 は **primitive 条件が抜けている**。
- $x_1^2$ がそのまま反例になる。
- 一方、primitive 条件を加えれば、$\mathbb Q|x|$ という条件は弱すぎず、half-odd-integral condition を自動的に含む。
- free-homotopy の simple を扱うなら、Fact 2.1 / 2.2 では based representative の **共役の自由度**を落としてはいけない。
- if part では、この共役自由度が実際に必要であり、その後の残差を Johnson surjectivity で消す。

---

## 10. separating case は別問題

$|x|=0$ では

$$
\langle l(x),|x|\rangle=0
$$

が自動的に成り立つため、contraction 条件は何も検出しない。

したがって separating simple elements の $N_3$-simpleness は、nonseparating sector と分離して別の不変量・orbit 記述を考える必要がある。

---

## 11. 次に確認する事項

1. Fact 2.1 / 2.2 を free-homotopy の定義に合わせて、共役込みで正式に書き直す。
2. $l(\Gamma_2)=\Lambda^2H_{\mathbb Z}$ の符号・格子規約を現在の $l$ の定義と照合する。
3. 上記 if-part を lemma ごとに分解し、完全な証明として整える。
4. genus $g=1$ の場合の Johnson surjectivity の扱いを別途確認する。
5. separating sector $|x|=0$ の $N_3$-simpleness 判定を独立に考える。

---

## 参照した手元資料

- `simpleness.pdf`
- `kiyoh.pdf`
- Johnson の第一 Johnson 準同型の全射性
- Morita / Kawazumi–Kuno による extended Johnson / symplectic expansion の枠組み
