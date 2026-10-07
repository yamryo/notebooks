# 研究メモ｜標準原点 $(R,1)$ と S-pair 共役類の階層的不変量

更新日: 2026-10-07

## 位置づけ

研究進捗ツリーの

- `2｜Sp₄(Z) での共役判定`
- とくに `2.1｜Q(c) による Yang・S-pair 共役判定の整理`
- および `2.2｜unit 群と全共役子の整理`

に接続する研究メモ。

固定した既約 reciprocal polynomial $f(t)$ に対する Yang の S-pair 分類の中で、標準 S-pair

$$
(R,1)
$$

を「原点」として共役類のずれを階層的に記述する、という見方を整理する。

ここでいう「距離」は数値距離や metric を意味しない。現段階では、

$$
\text{基準点からの階層的変位 invariant}
$$

という意味で用いるのが安全である。

---

## 1. 設定

$f(t)$ を次数 $2g$ の separable, irreducible, palindromic monic polynomial とする。

$f$ の根を $\alpha$ とし、

$$
F=\mathbb Q(\alpha),\qquad R=\mathbb Z[\alpha]
$$

とおく。reciprocal involution を

$$
\widetilde{\alpha}=\alpha^{-1}
$$

で定める。

Yang の理論では、$f$ を特性多項式にもつ

$$
A\in Sp_{2g}(\mathbb Z)
$$

の $Sp_{2g}(\mathbb Z)$-共役類は S-pair

$$
(\mathfrak a_A,a_A)
$$

の同値類に対応する。

$\mathfrak a_A$ は $\alpha$-固有ベクトルの座標が生成する fractional $R$-ideal であり、$a_A$ は symplectic form の情報を記録する第2成分である。

---

## 2. 標準 S-pair $(R,1)$

Yang の定義では

$$
\boxed{(R,1)\in P_f}
$$

が常に成り立つ。

したがって、固定した $f$ に対する $Sp_{2g}(\mathbb Z)$-共役類の集合には、S-pair $(R,1)$ に対応する distinguished class が必ず存在する。

これを

$$
\boxed{\mathcal O_f:=[R,1]}
$$

と書き、標準原点とみなす。

重要なのは、「第1成分が $R$ である共役類」が一つとは限らないことと、「原点が一意に選べないこと」は別問題だという点である。

第1成分が $R$ である S-pair は一般に

$$
(R,s)
$$

という形で複数存在するが、その中に $(R,1)$ という canonical な一つがある。

したがって原点は

$$
\boxed{[R,1]}
$$

と一意に指定できる。

---

## 3. $R$ 上にある共役類の複数性

$$
U:=R^\times
$$

とし、

$$
U^+:=\{u\in U:\widetilde u=u\},
$$

$$
N(U):=\{u\widetilde u:u\in U\}
$$

とおく。

第1成分を $R$ に固定した S-pair $(R,s)$ の同値類は

$$
\boxed{U^+/N(U)}
$$

で parametrized される。

したがって $[R,1]$ 以外にも $[R,s]$ が存在しうる。

ここで $R$ が maximal order でない場合には、

$$
U^+=(R^\times)^{\widetilde{\phantom{x}}}
=(R\cap F^+)^\times
$$

であり、一般に $\mathcal O_{F^+}^\times$ と同一視してはいけない。

---

## 4. 「原点集合」と「標準原点」

二つの見方を区別する。

### 4.1 原点集合として見る場合

第1成分が $R$ である共役類全体

$$
\mathcal Z_R
:=
\{[R,s]:s\in U^+\}
$$

を原点集合とみなすことができる。

このとき $\mathcal Z_R$ 内部の違い $U^+/N(U)$ を無視し、ideal class のずれだけを見ることになる。

これは $GL_{\mathbb Z}$ 的な粗い不変量として自然である。

### 4.2 一点を原点として見る場合

より細かい $Sp_{\mathbb Z}$ 情報まで保持するなら、

$$
\boxed{\mathcal O_f=[R,1]}
$$

だけを原点とする。

この方が、本研究で考えたい「原点からの階層的変位」という発想には適している。

---

## 5. 第1段階：ideal のずれ

S-pair

$$
S_A=(\mathfrak a_A,a_A)
$$

に対して、まず

$$
\boxed{
\delta_{\mathrm{ideal}}(A):=[\mathfrak a_A]
}
$$

を考える。

これは $R$-ideal の同値類であり、原点では

$$
\delta_{\mathrm{ideal}}(\mathcal O_f)=[R].
$$

この第1段階は、Alexander module / Latimer–MacDuffee の言葉では $GL_{\mathbb Z}$-共役情報に対応する。

すなわち、同じ $f$ をもつ $A,B$ について

$$
[\mathfrak a_A]=[\mathfrak a_B]
$$

であることは、

$$
A\sim_{GL_{2g}(\mathbb Z)}B
$$

に対応する。

---

## 6. 第2段階：principal stratum 上の symplectic なずれ

$$
[\mathfrak a_A]=[R]
$$

とする。

このとき、ある $c\in F^\times$ を用いて

$$
\mathfrak a_A=cR
$$

と書ける。

そこで

$$
\boxed{
\sigma_A:=\frac{a_A}{c\widetilde c}
}
$$

とおく。

S-pair 条件から $\sigma_A$ は $U^+$ に入り、$c$ の取り方を

$$
c'=cu,\qquad u\in R^\times
$$

と変えると

$$
\sigma_A'
=
\frac{\sigma_A}{u\widetilde u}.
$$

したがって

$$
\boxed{
\delta_{\mathrm{Sp}}(A)
:=
[\sigma_A]\in U^+/N(U)
}
$$

は well-defined である。

原点 $(R,1)$ では

$$
\delta_{\mathrm{Sp}}(\mathcal O_f)=1.
$$

従って principal stratum では

$$
\boxed{
A\sim_{Sp_{2g}(\mathbb Z)}\mathcal O_f
\iff
\delta_{\mathrm{ideal}}(A)=[R]
\ \text{かつ}\
\delta_{\mathrm{Sp}}(A)=1.
}
$$

---

## 7. 階層的変位 invariant

以上をまとめると、原点 $(R,1)$ からのずれは

$$
\boxed{
\text{ideal のずれ}
\quad\longrightarrow\quad
\text{symplectic/unit のずれ}
}
$$

という二段階で見ることができる。

記号的には

$$
\delta(A)
=
\bigl(
\delta_{\mathrm{ideal}}(A),
\delta_{\mathrm{Sp}}(A)
\bigr)
$$

と書きたいが、$\delta_{\mathrm{Sp}}$ は $\delta_{\mathrm{ideal}}=[R]$ の stratum 上で定義される量である。

したがって、現段階では直積値の invariant とみなすより、

$$
\boxed{
\text{pointed, stratified invariant}
}
$$

と理解するのが正確である。

これは数値的な metric ではない。

---

## 8. Yang の完全系列との関係

$R$ が integrally closed の場合、Yang の分類には

$$
1
\longrightarrow
U^+/N(U)
\longrightarrow
P_f
\longrightarrow
C_0
\longrightarrow
1
$$

という完全系列が現れる。

ここで

- $C_0$ は許される ideal class の部分群、
- kernel $U^+/N(U)$ は第1成分が $R$ である S-pair の違い、

を記述する。

したがって

$$
\boxed{
\text{ideal-class direction}
+
\text{unit/norm direction}
}
$$

という上の階層は、Yang の完全系列そのものに内在している。

さらに Yang は、$R$ が integrally closed でない場合でも、対応する set-level の分解が成立することを述べている。

---

## 9. $Q(c)$ による共役判定との対応

既存メモ

`研究メモ｜Q(c)によるYang・S-pair共役判定の整理.md`

では、

$$
Q(c)=M_BT(c)M_A^{-1}
$$

に対して

$$
Q(c)\in Sp_{2g}(\mathbb Z)
$$

となる条件を

$$
\mathfrak a_A=c\mathfrak a_B
$$

と

$$
a_A=c\widetilde c\,a_B
$$

の二段階に分けた。

これは本メモの言葉では、

1. ideal のずれを消す、
2. norm/unit のずれを消す、

という操作に対応する。

従って $(R,1)$ を原点とする見方は、既存の $Q(c)$ 判定を別の理論に置き換えるものではなく、その構造を「基準点からの変位」として読み直すものである。

---

## 10. $R\neq\mathcal O_F$ の場合の三段階化

$R$ が maximal order でない場合には、さらに粗い第0段階として

$$
\boxed{
\delta_{\max}(A)
:=
[\mathfrak a_A\mathcal O_F]
}
$$

を置くことができる。

すると

$$
\boxed{
[\mathfrak a_A\mathcal O_F]
\quad\longrightarrow\quad
[\mathfrak a_A]
\quad\longrightarrow\quad
[\sigma_A]
}
$$

という三段階になる。

それぞれ

1. maximal order 上での coarse ideal information,
2. 元の order $R$ 上の lattice/ideal information,
3. symplectic unit/norm information,

を表す。

これは既存の「最大整環への延長による二段階 Sp 共役判定」と自然に接続する。

---

## 11. fibered knot の集合内での原点という問題

代数的には $(R,1)$ は常に存在する。

一方、

$$
[R,1]
$$

に対応する $Sp_{2g}(\mathbb Z)$-共役類が、実際に $S^3$ の fibered knot の homological monodromy として実現されるかは別問題である。

最近の整理では、Alexander module と Blanchfield pairing を用いることでこの問題を knot-theoretic に翻訳できる可能性が見えている。

とくに cyclic Alexander module

$$
\Lambda/(f)\cong R
$$

をもつ fibered knot の Blanchfield pairing を Yang の第2成分へ翻訳できれば、

$$
(R,1)
$$

の realizability を Blanchfield pairing の numerator / norm class の問題として記述できる。

ただし、現時点では符号・mirror・$\alpha\leftrightarrow\alpha^{-1}$ の convention を完全に固定した厳密な翻訳を別途確認する必要がある。

したがって、

$$
\boxed{
(R,1)\text{ は代数的には canonical origin}
}
$$

は確定事項であり、

$$
\boxed{
(R,1)\text{ が常に fibered-knot realizable か}
}
$$

は検証課題として分離する。

---

## 12. 本流への還元

本研究における使い方を次のように整理する。

- 固定した既約 $f$ に対する標準基準点は $(R,1)$ とする。
- $[\mathfrak a]$ を第1の変位 invariant とする。
- principal stratum では $U^+/N(U)$ の class を第2の変位 invariant とする。
- $R\neq\mathcal O_F$ では maximal-order extension を第0段階として追加できる。
- 「距離」という語を使う場合も、当面は metric ではなく階層的変位を意味する。
- knot-realizable subset の中にも標準原点を取れるかどうかは、Blanchfield pairing との翻訳を通して別途確認する。

この見方により、Yang の S-pair 分類は

$$
\boxed{
\text{原点 }(R,1)\text{ をもつ階層的な共役不変量}
}
$$

として解釈できる。

---

## 参考

- Q. Yang, *Conjugacy classes in integral symplectic groups*, Linear Algebra Appl. **418** (2006), 614–624.
- `研究メモ｜Yang・S-pairと固有ベクトル.md`
- `研究メモ｜Q(c)によるYang・S-pair共役判定の整理.md`
- `研究メモ｜最大整環への延長による二段階Sp共役判定.md`
