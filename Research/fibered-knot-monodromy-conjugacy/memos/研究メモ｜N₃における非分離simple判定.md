# 研究メモ｜(N_3) における非分離 simple 判定

更新日: 2026-10-19

## 0. このメモの位置づけ

`simpleness.pdf` と `kiyoh.pdf` に書かれた (N_3) 上の simpleness 条件を再検討した結果、次の点が重要だと分かった。

1. 「simple」を自由ホモトピーで定義する限り、separating simple curve と nonseparating simple curve を分ける必要がある。
2. (N_3) の nonseparating-simple 判定では、(langle l(x),|x|angleinmathbb Q|x|) だけでは足りず、少なくとも (|x|) の primitive 性が必要である。
3. primitive 性を加えると、(langle l(x),|x|angleinmathbb Q|x|) から逆向きも証明できる見通しが立った。
4. その証明では、**共役による補正**と **Torelli / Johnson による補正**を二段階で使う。

以下では nonseparating sector に限定して整理する。separating case (|x|=0) は別問題として残す。

---

## 1. 定義と Fact 2.1 / 2.2 の注意点

`simpleness.pdf` の Definition 2.1 では、(xinpi) が simple であるとは、その自由ホモトピー類が simple closed curve を含むことと定義している。

この定義では separating simple curve も含まれる。たとえば

[
[x_1,y_1]
]

は separating simple closed curve を表すが、その homology class は (0) であり、自由群の primitive element ではない。

したがって、

[
x	ext{ simple}Longrightarrow x	ext{ primitive}
]

を無条件で使うことはできない。

以後、主線では **nonseparating simple** を扱う。

### based element と free homotopy のずれ

さらに、自由ホモトピーで simple を定義すると、based element (x) 自身は standard simple element の像そのものとは限らず、その共役である可能性がある。

したがって、現行の定義から自然に得られる形は

[
oxed{
x	ext{ nonseparating-simple}
iff
exists finoperatorname{Aut}_{partial}(pi), exists winpi
	ext{ such that }
x=w f(x_1)w^{-1}.
}
]

`kiyoh.pdf` の Proposition 3.2 の証明では、内部自己同型によって (x) を共役な based simple representative に取り替えてから (f(x_1)=x) としているが、元の (x) に戻す共役が (operatorname{Aut}_{partial}(pi)) に属することは示されていない。

したがって、free-homotopy の定義を維持するなら、Fact 2.1(ii) と Fact 2.2 は「共役まで含めた orbit」として書き直すのが安全である。

(N_k) では対応して

[
oxed{
[x]_k	ext{ nonseparating-simple}
iff
exists finoperatorname{Aut}_{partial}(pi), exists winpi
	ext{ such that }
[x]_k=[w f(x_1)w^{-1}]_k.
}
]

---

## 2. (N_3) の座標と extended Johnson 項

symplectic expansion によって

[
[z]_3longmapsto (l(z),|z|)
]

と座標化する。

一般の (finoperatorname{Aut}_{partial}(pi)) に対して

[
A=|f|in Sp(H_{mathbb Z})
]

とすると、

[
oxed{
l(f(z))
=
A,l(z)
+
leftlangle	au_1^	heta(f),A|z|ightangle.
}
]

ここで (	au_1^	heta(f)) は一般の (f) に対する extended Johnson 成分である。

Torelli 元 (hinmathcal I_{g,1}) では (A=mathrm{id}) なので、

[
oxed{
l(h(z))
=
l(z)+langle	au_1(h),|z|angle.
}
]

また (	auinLambda^3H) に対して

[
leftlanglelangle	au,Xangle,Xightangle=0.
]

したがって

[
oxed{
langle l(f(z)),|f(z)|angle
=
Alangle l(z),|z|angle.
}
]

---

## 3. standard simple element の contraction

規約

[
l(x_1)=rac12X_1wedge Y_1
]

および

[
langle Xwedge Y,Zangle
=
(Zcdot X)Y-(Zcdot Y)X
]

より、

[
oxed{
langle l(x_1),X_1angle
=
-rac12X_1.
}
]

したがって (y_0=f(x_1)), (v=|y_0|=A(X_1)) なら

[
oxed{
langle l(y_0),vangle
=
-rac12v.
}
]

---

## 4. 共役による (l)-成分の変化

(y=w y_0 w^{-1}) とし、

[
a=|w|,qquad v=|y_0|=|y|
]

と置く。

(l) の積公式から

[
oxed{
l(wy_0w^{-1})
=
l(y_0)+awedge v.
}
]

したがって

[
egin{aligned}
langle l(y),vangle
&=
-rac12v+langle awedge v,vangle\
&=
left(-rac12+vcdot aight)v.
end{aligned}
]

ここで (vcdot ainmathbb Z) なので、nonseparating simple element については

[
oxed{
langle l(y),|y|angle
in
left(mathbb Z-rac12ight)|y|.
}
]

したがって (mathbb Q|y|) に入るという条件より強い離散的条件が成り立つ。

---

## 5. primitive 条件は不可欠

`simpleness.pdf` の Theorem 2.4 は

[
[x]_3	ext{ simple}
iff
langle l(x),|x|angleinmathbb Q|x|
]

としているが、nonseparating simpleness を考えるなら primitive 条件が必要である。

反例は

[
x=x_1^2.
]

このとき

[
|x|=2X_1
]

は primitive ではない。一方

[
l(x_1^2)=X_1wedge Y_1
]

なので

[
langle l(x),|x|angle
=
-2X_1
=
-|x|
inmathbb Q|x|.
]

よって contraction 条件だけでは ([x]_3) の nonseparating simpleness は従わない。

---

## 6. 修正版の候補定理

nonseparating sector では、正しい候補は次である。

[
oxed{
[x]_3	ext{ is nonseparating-simple}
iff
egin{cases}
|x|	ext{ is primitive in }H_{mathbb Z},\[1mm]
langle l(x),|x|angleinmathbb Q|x|.
end{cases}
}
]

only-if は上の議論から従う。

以下、if part を示す。

---

## 7. if part の証明

[
v:=|x|
]

とし、

[
v	ext{ primitive},qquad
langle l(x),vangle=qv,quad qinmathbb Q
]

を仮定する。

### Step 1. homology class を合わせる

(v) が primitive なので、

[
exists Ain Sp(H_{mathbb Z})
quad	ext{such that}quad
A(X_1)=v.
]

(ho_2(operatorname{Aut}_{partial}pi)=Sp(H_{mathbb Z})) を使って (A) を lift し、

[
f_0inoperatorname{Aut}_{partial}(pi),qquad |f_0|=A
]

を取る。

[
y_0:=f_0(x_1).
]

すると

[
|y_0|=v,qquad
langle l(y_0),vangle=-rac12v.
]

### Step 2. (q) は自動的に half-odd-integer になる

(|x|=|y_0|=v) なので

[
xy_0^{-1}inGamma_2.
]

したがって

[
delta_0:=l(x)-l(y_0)inLambda^2H_{mathbb Z}.
]

よって

[
langledelta_0,vangle
=
left(q+rac12ight)v
in H_{mathbb Z}.
]

(v) は primitive なので

[
oxed{
q+rac12=ninmathbb Z.
}
]

すなわち

[
qinmathbb Z-rac12.
]

したがって、「(mathbb Q v) に入る」という条件は primitive 性と組み合わせると自動的に正しい half-integral parity を含んでいる。

### Step 3. 共役で scalar part を合わせる

symplectic lattice の unimodularity と (v) の primitive 性から、

[
vcdot a=n
]

となる (ain H_{mathbb Z}) を取れる。

(|w|=a) となる (winpi) を取り、

[
y_1:=w y_0 w^{-1}
]

と置く。

すると (y_1) は nonseparating-simple のままで、

[
|y_1|=v,
]

かつ

[
l(y_1)=l(y_0)+awedge v.
]

したがって

[
langle l(y_1),vangle
=
left(-rac12+night)v
=
qv
=
langle l(x),vangle.
]

そこで

[
delta:=l(x)-l(y_1)
]

と置けば、

[
oxed{
deltainLambda^2H_{mathbb Z},
qquad
langledelta,vangle=0.
}
]

### Step 4. 残りの差を Johnson 項として表す

(v) が primitive なので、

[
vcdot b=1
]

となる (bin H_{mathbb Z}) を取れる。

[
	au:=bwedgedeltainLambda^3H_{mathbb Z}
]

と置くと、

[
egin{aligned}
langle	au,vangle
&=
langle bwedgedelta,vangle\
&=
(vcdot b)delta-bwedgelangledelta,vangle\
&=
delta.
end{aligned}
]

よって

[
oxed{
delta=langle	au,vangle
quad
(	auinLambda^3H_{mathbb Z}).
}
]

Johnson の全射性

[
	au_1(mathcal I_{g,1})
=
Lambda^3H_{mathbb Z}
]

より、

[
exists hinmathcal I_{g,1}
quad	ext{such that}quad
	au_1(h)=	au.
]

Torelli 元なので (|h|=mathrm{id})。したがって

[
|h(y_1)|=v
]

かつ

[
egin{aligned}
l(h(y_1))
&=
l(y_1)+langle	au_1(h),vangle\
&=
l(y_1)+delta\
&=
l(x).
end{aligned}
]

よって (N_3) の座標が一致し、

[
[h(y_1)]_3=[x]_3.
]

(h(y_1)) は nonseparating-simple なので、

[
oxed{
[x]_3	ext{ is nonseparating-simple}.
}
]

これで if part が得られる。

---

## 8. 証明の構造

逆向きの補正は二段階に分かれる。

### (A) 共役による補正

[
l(y_0)longmapsto l(y_0)+awedge v
]

により、

[
langle l(,cdot,),vangle
]

の (v)-方向の係数を整数だけ動かす。

これにより

[
langle l(y_1),vangle
=
langle l(x),vangle
]

まで合わせる。

### (B) Torelli / Johnson による補正

残差

[
delta=l(x)-l(y_1)
]

は

[
langledelta,vangle=0
]

を満たす。

このとき

[
delta=langle bwedgedelta,vangle
]

なので、Johnson の全射性を使って Torelli 元で残差を完全に消せる。

要するに

[
oxed{
	ext{共役で scalar part を合わせる}
quadLongrightarrowquad
	ext{Torelli で kernel part を合わせる}.
}
]

---

## 9. 現時点での結論

nonseparating sector では、次の修正版が有力であり、上記の議論で proof sketch まで得られた。

[
oxed{
[x]_3	ext{ nonseparating-simple}
iff
|x|	ext{ primitive}
	ext{ and }
langle l(x),|x|angleinmathbb Q|x|.
}
]

重要な点は以下。

- `simpleness.pdf` の Theorem 2.4 は **primitive 条件が抜けている**。
- (x_1^2) がそのまま反例になる。
- 一方、primitive 条件を加えれば、(mathbb Q|x|) という条件は弱すぎず、half-odd-integral condition を自動的に含む。
- free-homotopy の simple を扱うなら、Fact 2.1 / 2.2 では based representative の **共役の自由度**を落としてはいけない。
- if part では、この共役自由度が実際に必要であり、その後の残差を Johnson surjectivity で消す。

---

## 10. separating case は別問題

(|x|=0) では

[
langle l(x),|x|angle=0
]

が自動的に成り立つため、contraction 条件は何も検出しない。

したがって separating simple elements の (N_3)-simpleness は、nonseparating sector と分離して別の不変量・orbit 記述を考える必要がある。

---

## 11. 次に確認する事項

1. Fact 2.1 / 2.2 を free-homotopy の定義に合わせて、共役込みで正式に書き直す。
2. (l(Gamma_2)=Lambda^2H_{mathbb Z}) の符号・格子規約を現在の (l) の定義と照合する。
3. 上記 if-part を lemma ごとに分解し、完全な証明として整える。
4. genus (g=1) の場合の Johnson surjectivity の扱いを別途確認する。
5. separating sector (|x|=0) の (N_3)-simpleness 判定を独立に考える。

---

## 参照した手元資料

- `simpleness.pdf`
- `kiyoh.pdf`
- Johnson の第一 Johnson 準同型の全射性
- Morita / Kawazumi–Kuno による extended Johnson / symplectic expansion の枠組み
