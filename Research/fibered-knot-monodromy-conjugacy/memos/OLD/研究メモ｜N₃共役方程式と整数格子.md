# 研究メモ｜N₃共役方程式と整数格子

## 1. Aut(N₃) の座標表示

symplectic expansion により

\[
N_3 \hookrightarrow \Lambda^2 H \rtimes H
\]

と表し、自己同型を

\[
(\tau,A)\in \operatorname{Hom}(H,\Lambda^2H)\rtimes \operatorname{GL}(H)
\]

として扱う。

mapping class の像では \(A\in\operatorname{Sp}(H)\)。

## 2. 共役方程式

\[
\rho_3(\phi_0)=(u_0,A_0),\qquad
\rho_3(\phi_n)=(u_n,A_n)
\]

とし、\(H\) 上の共役子 \(P_n\) が

\[
A_n=P_nA_0P_n^{-1}
\]

を満たすとする。

\(N_3\) 上の共役子を

\[
Q_n=(h_n,P_n)
\]

とおくと、共役条件は

\[
(1-A_n\cdot)h_n=u_n-P_n\cdot u_0
\]

という線形方程式になる。

\(\operatorname{Hom}(H,\Lambda^2H)\) は種数2では 24 次元なので、24変数の有理一次方程式として解ける。

## 3. φₙ 族での状況

再構成計算では

\[
\det(1-A_n\cdot)=256
\]

となり、選んだ \(P_n\) に対する \(h_n\) は \(\mathbb Q\) 上で一意に決まった。

したがって、この \(P_n\) を固定した場合には

\[
P_n \longmapsto h_n \longmapsto Q_n
\]

という流れになる。

ただし、別の \(H\) 上の共役子 \(P_n'\) を選べば、対応する \(h_n'\) も一般には変わる。

## 4. 整数格子保存

\(P_n\in\operatorname{Sp}_4(\mathbb Z)\) であり、共役方程式が \(\mathbb Q\) 上で解けても、

\[
Q_n=(h_n,P_n)
\]

が \(N_3\) の整数格子を保存することは自動ではない。

実際、候補 \(h_n\) には半整数成分が現れる。

これまでの再構成計算では \(\theta\)-座標における格子条件を満たしたが、その概念的理由はまだ説明できていない。

現時点の位置づけは：

> 格子 obstruction は計算上消えているが、その概念的理由は未解明。

## 5. 今後確認すること

- 最新版 `n3_monodromy.py` で \(u_n=\tau_1^\theta(\phi_n)\) を再計算する。
- \(h_n\) の一般式と照合する。
- \(Q_n\rho_3(\phi_0)Q_n^{-1}=\rho_3(\phi_n)\) を確認する。
- \(Q_n\) の整数格子保存を確認する。
- 有限個の \(n\) の数値検算ではなく、一般 \(n\) の恒等式として検証する。

## 関連ソース

- `kiyoh.pdf`
- `n3_monodromy.py`
- `計算結果｜モノドロミー族φₙ.md`
