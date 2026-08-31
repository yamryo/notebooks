# 類数 1 の場合の primitive 固有ベクトルと \(s\)-class による Sp-共役判定

## 1. 設定

\(A\in \mathrm{Sp}_{2n}(\mathbb Z)\) の特性多項式を

\[
f(t)\in \mathbb Z[t]
\]

とし、\(\alpha\) をその根とする。以下、

\[
F=\mathbb Q(\alpha),\qquad
R=\mathbb Z[\alpha],\qquad
\mathcal O_F=\text{the ring of integers of }F
\]

とする。

\(f\) は reciprocal なので、\(F\) 上に

\[
\widetilde{\alpha}=\alpha^{-1}
\]

で定まる involution がある。

Yang の記号に合わせて

\[
\varepsilon=\alpha^{1-n}f'(\alpha)
\]

とおく。

---

## 2. Yang の S-pair

\(\alpha\)-固有ベクトル

\[
v=(v_1,\dots,v_{2n})^T\in R^{2n},
\qquad
Av=\alpha v
\]

を取る。

座標から

\[
\mathfrak a_v
=
\mathbb Z v_1+\cdots+\mathbb Z v_{2n}
\]

を作る。これは \(R\) の integral ideal になる。

さらに

\[
s_v
=
\varepsilon^{-1}v^TJ\widetilde v
\]

とおく。

Yang の S-pair は

\[
(\mathfrak a_v,s_v)
\]

であり、その同値類が Sp-共役類を記述する。

---

## 3. \(\mathcal O_F\) への拡張と primitive 化

\(\mathfrak a_v\) を \(\mathcal O_F\) に拡張すると

\[
\mathfrak a_v\mathcal O_F
=
\mathcal O_Fv_1+\cdots+\mathcal O_Fv_{2n}.
\]

ここで

\[
h_F=1
\]

と仮定する。すると \(\mathcal O_F\) は PID なので、

\[
\mathfrak a_v\mathcal O_F=(g)
\]

と書ける。

この \(g\) を使って

\[
w=g^{-1}v
\]

とおくと

\[
w\in\mathcal O_F^{2n}
\]

かつ

\[
\mathcal O_Fw_1+\cdots+\mathcal O_Fw_{2n}
=
\mathcal O_F.
\]

このような \(w\) を primitive と呼ぶ。

したがって、

\[
\boxed{
w=g^{-1}v
}
\]

は \(v\) の primitive 化である。

### 注意

primitive であることは、ある成分が \(1\) であることを意味しない。

必要なのは

\[
(w_1,\dots,w_{2n})=\mathcal O_F
\]

であり、これは整数の場合の

\[
(2,3)=\mathbb Z
\]

と同じ意味である。

---

## 4. primitive 固有ベクトルから直接 \(s\) を作る

primitive \(\alpha\)-固有ベクトル

\[
w\in\mathcal O_F^{2n}
\]

を取れば、ideal 成分は最初から

\[
\mathfrak a_w=\mathcal O_F
\]

である。

したがって、類数 \(1\) の場合には pair を前面に出さず、

\[
\boxed{
s_w
=
\varepsilon^{-1}w^TJ\widetilde w
}
\]

という一つの量だけに注目できる。

実際、

\[
w=g^{-1}v
\]

なら

\[
\begin{aligned}
s_w
&=
\varepsilon^{-1}
(g^{-1}v)^T
J
\widetilde{(g^{-1}v)}
\\
&=
\frac{1}{g\widetilde g}
\varepsilon^{-1}v^TJ\widetilde v
\\
&=
\boxed{
\frac{s_v}{g\widetilde g}
}.
\end{aligned}
\]

したがって、以前の記号 \(u\) を使えば

\[
\boxed{
u=s_w.
}
\]

つまり理論上は primitive 固有ベクトル \(w\) から直接 \(s_w\) を定義し、実際の計算では

\[
v\longrightarrow g\longrightarrow w=g^{-1}v\longrightarrow s_w
\]

という手順を使えばよい。

---

## 5. \(s_w\) の選択依存性と \(C_O\)

primitive 固有ベクトル \(w\) は一意ではない。

別の primitive 固有ベクトルは

\[
w'=e\,w,
\qquad
e\in\mathcal O_F^\times
\]

と書ける。

このとき

\[
\begin{aligned}
s_{w'}
&=
\varepsilon^{-1}(ew)^TJ\widetilde{(ew)}
\\
&=
e\widetilde e\,
\varepsilon^{-1}w^TJ\widetilde w
\\
&=
e\widetilde e\,s_w.
\end{aligned}
\]

そこで

\[
\boxed{
C_O
=
\{e\widetilde e\mid e\in\mathcal O_F^\times\}
}
\]

とおく。

すると \(s_w\) 自体は \(w\) の選び方に依存するが、

\[
\boxed{
[s_A]\pmod{C_O}
}
\]

は選び方に依存しない。

したがって、行列 \(A\) に対して本質的に対応させる量は

\[
\boxed{
A\longmapsto [s_A].
}
\]

---

## 6. 2つの行列の比較

同じ特性多項式をもつ \(A,B\) に対して primitive \(\alpha\)-固有ベクトル

\[
w_A,\qquad w_B
\]

を取り、

\[
s_A
=
\varepsilon^{-1}w_A^TJ\widetilde w_A,
\qquad
s_B
=
\varepsilon^{-1}w_B^TJ\widetilde w_B
\]

とする。

それぞれの class の代表元 \(s_A,s_B\) を取り、

\[
\boxed{
r=\frac{s_A}{s_B}
}
\]

とおく。

すると

\[
\boxed{
[s_A]=[s_B]
\iff
\frac{s_A}{s_B}\in C_O.
}
\]

したがって

\[
\boxed{
[s_A]=[s_B]
\iff
r\in C_O.
}
\]

この判定は primitive 固有ベクトルの選び方に依存しない。

実際、

\[
w_A'=e_Aw_A,\qquad
w_B'=e_Bw_B
\]

と取り直すと

\[
r'
=
\frac{s_A'}{s_B'}
=
\frac{e_A\widetilde e_A}
     {e_B\widetilde e_B}
r
=
\left(\frac{e_A}{e_B}\right)
\widetilde{\left(\frac{e_A}{e_B}\right)}
r.
\]

前の係数は \(C_O\) に属するので、

\[
r\in C_O
\iff
r'\in C_O.
\]

---

## 7. Sp-共役との関係

一般には、\(R\) から \(\mathcal O_F\) へ拡張する過程で情報を失う可能性がある。

したがって一般には

\[
A\sim_{\mathrm{Sp}}B
\Longrightarrow
[s_A]=[s_B]
\Longleftrightarrow
\frac{s_A}{s_B}\in C_O
\]

という必要条件として使う。

特に、

\[
\boxed{
\frac{s_A}{s_B}\notin C_O
\Longrightarrow
A\not\sim_{\mathrm{Sp}}B.
}
\]

一方、

\[
\boxed{
R=\mathcal O_F
}
\]

かつ

\[
\boxed{
h_F=1
}
\]

なら、ideal 成分は primitive 化によって完全に自明化され、Yang の S-pair の情報は \(s\)-class に集約される。

この場合は

\[
\boxed{
A\sim_{\mathrm{Sp}}B
\iff
[s_A]=[s_B]
\iff
\frac{s_A}{s_B}\in C_O.
}
\]

したがって \([s_A]\) は Sp-共役類の完全不変量になる。

---

## 8. \(r\in C_O\) の実際の確認手順

実際の計算では、次の順序で確認する。

### Step 1. \(r\) を計算する

\[
r=\frac{s_A}{s_B}
\]

を \(F\) の power basis

\[
1,\alpha,\dots,\alpha^{2n-1}
\]

で表示する。

### Step 2. \(r\) が involution で固定されることを確認する

\[
\widetilde r=r
\]

を確認する。

これは \(r=e\widetilde e\) となるための必要条件である。

### Step 3. relative norm equation を解く

次の方程式を満たす

\[
z\in\mathcal O_F^\times
\]

を探す：

\[
\boxed{
z\widetilde z=r.
}
\]

すなわち

\[
N_{F/F^+}(z)=r
\]

という relative norm equation を解く。

ここで

\[
F^+=F^{\widetilde{\phantom{x}}}
\]

は involution の固定体である。

### Step 4. 候補 \(z\) が単数であることを確認する

候補 \(z\) が見つかったら、

\[
z^{-1}\in\mathcal O_F
\]

を直接示すか、

\[
N_{F/\mathbb Q}(z)=\pm1
\]

を確認する。

### Step 5. \(z\widetilde z=r\) を直接検算する

\(f(\alpha)=0\) を用いて

\[
z\widetilde z-r
\]

を power basis に還元し、

\[
z\widetilde z-r=0
\]

を確認する。

これにより

\[
\boxed{
r\in C_O
}
\]

が確定する。

逆に、この norm equation が \(\mathcal O_F^\times\) 内で解をもたないことを示せれば

\[
r\notin C_O
\]

であり、したがって \(A,B\) は Sp-共役ではない。

---

## 9. 例：\(6_3\) と \(11n_{12}\) での \(r\in C_O\) の確認

この例では

\[
f(t)=t^4-3t^3+5t^2-3t+1
\]

で、

\[
r
=
-\alpha^3+3\alpha^2-4\alpha+2.
\]

候補として

\[
\boxed{
z=\alpha^2-2\alpha+3
}
\]

を取る。

まず、

\[
\boxed{
z^{-1}=\alpha-\alpha^2
}
\]

であり、実際 \(f(\alpha)=0\) を使うと

\[
(\alpha^2-2\alpha+3)(\alpha-\alpha^2)=1.
\]

したがって

\[
z\in\mathcal O_F^\times.
\]

また

\[
\widetilde\alpha=\alpha^{-1}
\]

なので

\[
\widetilde z
=
\alpha^{-2}-2\alpha^{-1}+3.
\]

計算すると

\[
z\widetilde z
=
-\alpha^3+3\alpha^2-4\alpha+2
=
r.
\]

したがって

\[
\boxed{
r=z\widetilde z\in C_O.
}
\]

このように、最後の判定は「\(r\) が unit の relative norm として書けるか」という問題に帰着する。

---

## 10. まとめ

類数 \(1\) の場合、理論上は最初から primitive \(\alpha\)-固有ベクトル

\[
w_A\in\mathcal O_F^{2n}
\]

を取り、

\[
\boxed{
s_A=\varepsilon^{-1}w_A^TJ\widetilde w_A
}
\]

だけを見ることができる。

実際の計算では、取りやすい

\[
v_A\in R^{2n}
\]

から始め、

\[
\mathfrak a_v\mathcal O_F=(g),
\qquad
w_A=g^{-1}v_A
\]

として primitive 化すればよい。

比較量は

\[
\boxed{
[s_A]\pmod{C_O}
}
\]

であり、2つの行列 \(A,B\) の比較は

\[
\boxed{
r=\frac{s_A}{s_B}
}
\]

を用いて

\[
\boxed{
r\in C_O\ ?
}
\]

を調べることに帰着する。

特に

\[
\boxed{
R=\mathcal O_F,\quad h_F=1
}
\]

なら

\[
\boxed{
A\sim_{\mathrm{Sp}}B
\iff
[s_A]=[s_B]
\iff
s_A/s_B\in C_O.
}
\]

---

## 参考

Qingjie Yang, *Conjugacy classes in integral symplectic groups*, Linear Algebra and its Applications 418 (2006), 614–624.
