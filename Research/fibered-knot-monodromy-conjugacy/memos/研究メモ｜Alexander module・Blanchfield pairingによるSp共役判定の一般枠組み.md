# 研究メモ｜Alexander module・Blanchfield pairing による Sp 共役判定の一般枠組み

更新日: 2026-10-07

## 位置づけ

研究進捗ツリーの

`2.3｜reducible 固有多項式の場合の Sp 共役判定`

を、本流の言葉で整理し直すための研究メモ。

結論を先に言うと、fibered-knot monodromy の $Sp_{mathbb Z}$-共役問題の一般言語としては

$$
oxed{
(	ext{Alexander module}, 	ext{Blanchfield pairing})
}
$$

を採用するのが自然である。

Yang の S-pair は、この一般理論のうち $f(t)$ が既約な場合に、Alexander module と pairing を数体・ideal・norm の言葉に圧縮した算術的座標表示とみなす。

したがって、

$$
oxed{
	ext{一般理論は module + pairing、既約の場合の実計算は Yang}
}
$$

という役割分担を採用する。

---

## 1. 基本設定

$$
Lambda:=mathbb Z[t,t^{-1}]
$$

とする。

$$
Ain Sp_{2g}(mathbb Z)
$$

に対し、$mathbb Z^{2g}$ に

$$
tcdot x:=Ax
$$

と作用させて $Lambda$-module

$$
oxed{
mathcal A_A:=(mathbb Z^{2g},tcdot x=Ax)
}
$$

を定める。

presentation では

$$
oxed{
mathcal A_A
cong
operatorname{coker}(tI-A)
}
$$

である。

$A$ が $S^3$ の fibered knot $K$ の homological monodromy なら、

$$
mathcal A_A
$$

は $K$ の Alexander module

$$
H_1(widetilde X_K;mathbb Z)
$$

そのものである。

任意の symplectic matrix に対しては、必要に応じて「monodromy module」と呼び、実際に knot が存在する場合に Alexander module と同一視する。

---

## 2. characteristic polynomial は module の order にすぎない

$$
f_A(t):=det(tI-A)
$$

とする。

$mathcal A_A$ は $tI-A$ で presentation されるので、

$$
f_A(t)
$$

は $mathcal A_A$ の order / 0-th Fitting invariant を与える。

したがって

$$
oxed{
mathcal A_A
quadLongrightarrowquad
f_A(t)
}
$$

であるが、逆に $f_A(t)$ だけから $mathcal A_A$ は一般には決まらない。

module theory の典型例として、

$$
Lambda/(p(t)^2)
$$

と

$$
Lambda/(p(t))oplusLambda/(p(t))
$$

は同じ order $p(t)^2$ をもつが、module としては異なる。

従って

$$
oxed{
	ext{Alexander polynomial}
<
	ext{Alexander module}
}
$$

という情報量の差がある。

---

## 3. Alexander module と $GL_{mathbb Z}$-共役

$A,Bin GL_n(mathbb Z)$ に対して、

$$
oxed{
mathcal A_Acong_Lambdamathcal A_B
iff
Asim_{GL_n(mathbb Z)}B
}
$$

が成り立つ。

### 証明

$Lambda$-module 同型

$$
P:mathcal A_Alongrightarrowmathcal A_B
$$

は underlying $mathbb Z$-module の同型なので

$$
Pin GL_n(mathbb Z)
$$

である。

$Lambda$-linearity は

$$
P(Ax)=B(Px)
$$

を意味するから

$$
PA=BP.
$$

従って

$$
B=PAP^{-1}.
$$

逆向きは明らかである。

よって Alexander module は、行列の $GL_{mathbb Z}$-共役類そのものを記録する。

---

## 4. knot-admissible symplectic matrix と Seifert matrix

fibered knot の場合には

$$
det(I-A)=pm1
$$

が成り立つ。

以下ではこの条件を満たす

$$
Ain Sp_{2g}(mathbb Z)
$$

を考える。

standard symplectic matrixを $J$ とし、

$$
oxed{
V_A:=J(I-A)^{-1}
}
$$

とおく。

$det(I-A)=pm1$ なので

$$
V_Ain M_{2g}(mathbb Z).
$$

さらに symplectic 条件

$$
A^TJA=J
$$

から

$$
oxed{
V_A-V_A^T=J
}
$$

が成り立つ。

また

$$
det V_A=pm1
$$

なので $V_A$ は unimodular である。

そして

$$
V_A(I-A)=J=V_A-V_A^T
$$

より

$$
V_AA=V_A^T,
$$

従って

$$
oxed{
A=V_A^{-1}V_A^T.
}
$$

これは規約をこの形に固定したときの monodromy–Seifert matrix 関係である。

$t$ を deck transformation と monodromy のどちら向きに対応させるかによって、文献では $tleftrightarrow t^{-1}$ や $Aleftrightarrow A^{-1}$ の規約差がある。

---

## 5. Blanchfield pairing

classical knot $K$ の Alexander moduleには非退化 hermitian pairing

$$
oxed{
operatorname{Bl}_K:
mathcal A_K	imesmathcal A_K
longrightarrow
mathbb Q(t)/Lambda
}
$$

が定まる。

幾何的には infinite cyclic cover における equivariant linking form である。

Seifert matrix $V$ から Blanchfield pairing は標準公式で構成できる。したがって、上の $V_A$ を用いれば、少なくとも

$$
Ain Sp_{2g}(mathbb Z),
qquad
det(I-A)=pm1
$$

の範囲では、knot の実現可能性とは独立に algebraic Blanchfield pairing

$$
operatorname{Bl}_A
$$

を定義できる。

presentation の規約差を除けば、

$$
operatorname{coker}(V_A-tV_A^T)
$$

は

$$
operatorname{coker}(tI-A)
$$

と同じ Alexander module を与える。

---

## 6. Blanchfield pairing と $Sp_{mathbb Z}$-共役

Trotter の定理により、Seifert matrices が与える Blanchfield pairings が isometric であることと、Seifert matrices が $S$-equivalent であることは同値である。

さらに unimodular Seifert matrices については、$S$-equivalent であることと integral congruent であることが同値である。

従って、$V_A,V_B$ が unimodular なら

$$
(mathcal A_A,operatorname{Bl}_A)
cong
(mathcal A_B,operatorname{Bl}_B)
$$

であることは、ある

$$
Pin GL_{2g}(mathbb Z)
$$

によって

$$
V_B=P^TV_AP
$$

となることと同値である。

一方、

$$
V_A-V_A^T=V_B-V_B^T=J
$$

なので、

$$
J
=
P^TJP.
$$

従って

$$
Pin Sp_{2g}(mathbb Z).
$$

さらに

$$
A=V_A^{-1}V_A^T,qquad
B=V_B^{-1}V_B^T
$$

から

$$
B=P^{-1}AP.
$$

逆に $B=P^{-1}AP$ かつ $Pin Sp_{2g}(mathbb Z)$ なら、

$$
V_B
=
J(I-B)^{-1}
=
P^TV_AP,
$$

よって Blanchfield pairings は isometric である。

以上より、$det(I-A)=det(I-B)=pm1$ の範囲では

$$
oxed{
(mathcal A_A,operatorname{Bl}_A)
cong
(mathcal A_B,operatorname{Bl}_B)
iff
Asim_{Sp_{2g}(mathbb Z)}B.
}
$$

この記述には $f_A(t)$ の既約性を必要としない。

---

## 7. 共役判定の三階層

以上により、fibered-knot monodromy の範囲では

$$
oxed{
f_A(t)
quadlongleftarrowquad
mathcal A_A
quadlongleftarrowquad
(mathcal A_A,operatorname{Bl}_A)
}
$$

という階層を得る。

対応する共役情報は

$$
oxed{
egin{array}{ccl}
f_A=f_B
&:&
	ext{characteristic / Alexander polynomial が一致},
\[1mm]
mathcal A_Acongmathcal A_B
&iff&
Asim_{GL_{2g}(mathbb Z)}B,
\[1mm]
(mathcal A_A,operatorname{Bl}_A)
cong
(mathcal A_B,operatorname{Bl}_B)
&iff&
Asim_{Sp_{2g}(mathbb Z)}B.
end{array}
}
$$

従って、本研究における「階層的共役判定」の $Sp$ 段階を、Yang の既約理論に依存せず定式化できる。

---

## 8. $f(t)$ が既約の場合：Yang への還元

$f(t)$ が既約 reciprocal polynomial の場合、

$$
F=mathbb Q(alpha),qquad
R=mathbb Z[alpha]
$$

とおける。

このとき

$$
mathcal A_A
$$

は rank-one torsion-free $R$-module であり、fractional $R$-ideal

$$
mathfrak a_Asubset F
$$

として記述できる。

従って

$$
oxed{
mathcal A_A
longleftrightarrow
mathfrak a_A
}
$$

である。

さらに involution

$$
widetildealpha=alpha^{-1}
$$

を用いると、rank-one lattice 上の Blanchfield / symplectic pairing の情報は一つの scalar datum に圧縮できる。

Yang の第2成分

$$
a_A
$$

がこの scalar datum を記録し、S-pair

$$
oxed{
(mathfrak a_A,a_A)
}
$$

が $Sp_{mathbb Z}$-共役類を完全に分類する。

したがって概念的には

$$
oxed{
egin{array}{ccc}
	ext{general language}&&	ext{irreducible arithmetic language}
\[1mm]
mathcal A_A&&mathfrak a_A
\
operatorname{Bl}_A&&a_A
\
(mathcal A_A,operatorname{Bl}_A)
&&
(mathfrak a_A,a_A)
end{array}
}
$$

と理解する。

ここで $operatorname{Bl}_A$ と $a_A$ は文字通り同じ対象ではなく、Blanchfield pairing を rank-one $R$-lattice 上で数体的に座標表示したものが $a_A$ である、という意味である。

---

## 9. 既約の場合に既存の計算はそのまま残る

一般理論を Alexander module + Blanchfield pairing に移しても、既約 $f$ の場合にこれまで行ってきた計算は不要にならない。

むしろ

- fractional ideal $mathfrak a_A$,
- ideal class,
- maximal order $mathcal O_F$ への延長,
- multiplier ring,
- unit group,
- norm equation,
- norm-one units $S^{	imes,1}$,
- $Q(c)=M_BT(c)M_A^{-1}$,

はすべて

$$
(mathcal A_A,operatorname{Bl}_A)
$$

の isometry problem を rank-one arithmetic に落とした具体的な計算方法と理解できる。

従って

$$
oxed{
	ext{Yang を捨てるのではなく、Yang の位置づけを一般理論の既約 case に変更する}
}
$$

のが本整理の要点である。

---

## 10. square-free reducible case

次に

$$
f=f_1f_2cdots f_r
$$

を $mathbb Q$ 上相異なる既約因子の積とする。

このとき

$$
E
:=
mathbb Q[t,t^{-1}]/(f)
$$

は field ではないが、Chinese remainder theorem により

$$
oxed{
Econg K_1	imescdots	imes K_r,
qquad
K_i=mathbb Q[t,t^{-1}]/(f_i)
}
$$

という finite étale $mathbb Q$-algebra になる。

integral level では

$$
R:=mathbb Z[t,t^{-1}]/(f)
$$

は $E$ の order である。

この場合、Alexander module は一つの数体中の fractional ideal ではなく、

$$
oxed{
E	ext{ 内の }R	ext{-lattice}
}
$$

として扱うのが自然である。

rationally は各 $K_i$ 成分へ分解するが、integrally には一般に

$$
R
eq R_1	imescdots	imes R_r
$$

であり、各成分をどう貼り合わせるかという gluing data が残る。

この integral gluing は、とくに resultants

$$
operatorname{Res}(f_i,f_j)
$$

を割る素数で問題になると予想される。

---

## 11. reciprocal involution と factor の組

involution

$$
tlongmapsto t^{-1}
$$

は $E$ 上に作用する。

既約因子 $p(t)$ に対し reciprocal polynomial を $p^*(t)$ とすると、factor は概念的に

1. self-reciprocal factor
   $$
   p=p^*,
   $$

2. reciprocal pair
   $$
   p
eq p^*,qquad (p,p^*)
   $$

に分かれる。

self-reciprocal factor 上では、対応する number field に involution が入り、Blanchfield pairing は hermitian lattice の問題になる。

reciprocal pair の場合には、$p$-part と $p^*$-part が pairing によって dual に結ばれる。

従って square-free reducible case は

$$
oxed{
	ext{各 number-field 成分の算術}
+
	ext{integral gluing}
+
	ext{hermitian pairing}
}
$$

として理解するのが自然である。

これは Yang の ideal theory から大きく離れるというより、

$$
oxed{
	ext{一つの number field}
longrightarrow
	ext{finite étale algebra}
}
$$

への拡張とみなせる。

---

## 12. repeated factor をもつ場合

$f$ が

$$
f=p(t)^2q(t)
$$

のように repeated factor をもつ場合、

$$
mathbb Q[t,t^{-1}]/(f)
$$

は non-reduced algebra になりうる。

この場合には、数体の積だけでは記述できず、

- nilpotent structure,
- generalized eigenspaces,
- extension data,
- Jordan-type information,

が module に現れうる。

典型的には

$$
Lambda/(p^2)
$$

と

$$
Lambda/(p)oplusLambda/(p)
$$

の違いのような情報である。

従って repeated-factor case は

$$
oxed{
	ext{modules over non-reduced orders}
+
	ext{Blanchfield/hermitian pairing}
}
$$

の問題になる。

---

## 13. 一般化の三段階

以上から、$f$ の型によって理論を次の三段階に分ける。

$$
oxed{
egin{array}{ccl}
f	ext{ irreducible}
&Rightarrow&
	ext{number field + fractional ideal + norm}
\[1mm]
f	ext{ square-free reducible}
&Rightarrow&
	ext{étale algebra + lattice + gluing + hermitian form}
\[1mm]
f	ext{ non-square-free}
&Rightarrow&
	ext{non-reduced order + module extension data + pairing}
end{array}
}
$$

一般言語

$$
(mathcal A,operatorname{Bl})
$$

はこの三段階すべてで共通して使える。

---

## 14. 本流における研究方針

今後の本流では、次の役割分担を採用する。

### General layer

$$
oxed{
(mathcal A_A,operatorname{Bl}_A)
}
$$

を $Sp_{mathbb Z}$-共役問題の基本対象とする。

### Irreducible layer

$f$ が既約なら Yang の S-pair

$$
(mathfrak a_A,a_A)
$$

へ変換し、既存の ideal / unit / norm / multiplier-ring のアルゴリズムを使う。

### Square-free reducible layer

Yang を無理に「一つの数体の ideal theory」として拡張するのではなく、

$$
Rsubset E=prod K_i
$$

上の lattice と pairing の isometry problem として定式化する。

### Repeated-factor layer

non-reduced order 上の module classification と pairing の isometry を別段階として扱う。

---

## 15. 次に確認・実装すべき事項

本メモは conceptual framework の整理であり、2.3 の計算アルゴリズム完成を意味しない。

次の課題を残す。

1. **Blanchfield convention の固定**
   - $t$ と monodromy の向き
   - $A$ と $A^{-1}$
   - Seifert matrix formula の符号
   をプロジェクト全体で統一する。

2. **Yang 第2成分との翻訳公式**
   - $operatorname{Bl}$ の cyclic generator の self-pairing と
   - $a_A=arepsilon^{-1}v_A^TJwidetilde v_A$
   の厳密な対応を、符号を含めて証明する。

3. **square-free reducible case の具体的算法**
   - factor decomposition
   - local gluing
   - involution による factor pairing
   - integral hermitian lattice isometry
   を計算可能な形にする。

4. **repeated-factor case の切り分け**
   - minimal polynomial と characteristic polynomial の差
   - primary module structure
   - extension data
   を整理する。

5. **既存データへの適用**
   - reducible Alexander polynomial をもつ fibered knots を、従来の Yang 対象外から新しい module + pairing 判定へ戻す。

---

## 16. 本整理の要点

従来は

$$
oxed{
	ext{Yang の理論を reducible }f	ext{ にどう拡張するか}
}
$$

を問題としていた。

今後はむしろ

$$
oxed{
	ext{一般理論は Alexander module + Blanchfield pairing であり、}
}
$$

$$
oxed{
	ext{Yang はその irreducible rank-one case の算術的実装である}
}
$$

と位置づける。

これにより、

- 既約 $f$ については既存の Yang 計算をそのまま利用できる。
- reducible $f$ を理論上排除する必要がなくなる。
- square-free reducible と repeated-factor case を別の難易度として整理できる。
- 「階層的共役判定」の本流を
  $$
  f
  longrightarrow
  mathcal A
  longrightarrow
  (mathcal A,operatorname{Bl})
  $$
  と統一できる。

---

## 参考文献・関連メモ

- Q. Yang, *Conjugacy classes in integral symplectic groups*, Linear Algebra Appl. **418** (2006), 614–624.
- H. F. Trotter, *On S-equivalence of Seifert matrices*, Invent. Math. **20** (1973), 173–207.
- C. Kearton, *Blanchfield Duality and Simple Knots*, Trans. Amer. Math. Soc. **202** (1975), 141–160.
- `研究メモ｜Yang・S-pairと固有ベクトル.md`
- `研究メモ｜Q(c)によるYang・S-pair共役判定の整理.md`
- `研究メモ｜標準原点(R,1)とS-pair共役類の階層的不変量.md`
