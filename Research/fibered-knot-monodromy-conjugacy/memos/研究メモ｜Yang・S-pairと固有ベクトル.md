# 研究メモ｜Yang・S-pairと固有ベクトル

## 1. 位置づけ

Qingjie Yang, *Conjugacy classes in integral symplectic groups* は、与えられた separable, irreducible, palindromic monic polynomial を特性多項式にもつ整数シンプレクティック行列の共役分類を扱う。

分類の中心は、固有ベクトルから得られるイデアルと交代形式の情報を組にした S-pair である。

## 2. 固有ベクトルと分数イデアル

\(X\) の固有値を \(\alpha\) とし、固有ベクトルを

\[
v=(a_1,a_2,a_3,a_4)^{\mathsf T}
\]

とする。

このとき

\[
I(v)=\mathbb Za_1+\mathbb Za_2+\mathbb Za_3+\mathbb Za_4
\]

は \(\mathbb Z[\alpha]\) の分数イデアルとして解釈できる。

Latimer–MacDuffee 型の対応により、イデアル類は \(\operatorname{GL}_4(\mathbb Z)\) 共役を理解するための基本データとなる。

## 3. φₙ 族での整理

今回の計算では

\[
F=\mathbb Q(\alpha),\qquad \mathcal O_F=\mathbb Z[\alpha]
\]

で、\(F\) の類数は 1。

このため、\(\operatorname{GL}_4(\mathbb Z)\) 共役子の存在はイデアル類の側から説明しやすい。

SageMath の固有ベクトルに共通分母 7 が現れたのは、固有ベクトルのある成分を 1 に正規化する際に、ノルム 7 の代数的整数で割ったことに由来すると整理した。

## 4. GL 共役と Sp 共役の違い

類数1だけで説明できるのは基本的に \(\operatorname{GL}\) 共役であり、\(\operatorname{Sp}\) 共役には追加の交代形式データが必要。

Yang の S-pair は、この追加情報を保持する。

したがって、

> イデアル類が一致する → GL 共役の候補  
> S-pair まで一致する → symplectic 共役

という役割分担で理解する。

## 5. 注意

Yang の論文は \(\operatorname{Sp}_{2n}(\mathbb Z)\) の共役分類を扱うものであり、\(N_3\), \(N_4\), Johnson obstruction は扱っていない。

したがって、高次冪零商に関する主張を Yang の結果として引用しない。

## 関連ソース

- `Conjugacy classes in integral symplectic groups.pdf`
