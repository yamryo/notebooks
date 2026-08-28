# 研究メモ｜Residual nilpotenceと共役判別

## 1. Residual nilpotence

今回の曲面基本群は自由群なので residually nilpotent であり、

\[
\bigcap_{k\ge1}\Gamma_k\pi=\{1\}
\]

が成り立つ。

したがって、自然な写像

\[
\pi\longrightarrow\varprojlim_k N_k
\]

は単射である。

## 2. 自己同型の一致は検出できる

\(\phi,\psi\in\operatorname{Aut}(\pi)\) がすべての \(N_k\) 上で同じ作用をするなら、任意の \(x\in\pi\) について

\[
\phi(x)\psi(x)^{-1}\in\Gamma_k\pi
\]

がすべての \(k\) について成立する。

residual nilpotence により \(\phi(x)=\psi(x)\) となり、\(\phi=\psi\)。

したがって、異なる二つの自己同型は、どこかの \(N_k\) 上で作用が異なる。

## 3. 共役は別問題

今回必要なのは

\[
\rho_k(\phi_i)\sim\rho_k(\phi_j)
\]

かどうかである。

各 \(k\) で共役子 \(Q_k\) が存在しても、\(Q_k\) が \(k\) に関して compatible に選べるとは限らない。

したがって、

\[
\phi_i\not\sim\phi_j
\]

ならば、必ずどこかの \(k\) で

\[
\rho_k(\phi_i)\not\sim\rho_k(\phi_j)
\]

となる、とは residual nilpotence だけからは言えない。

## 4. さらに必要になる問題

- 降中心列商 \(N_k\) が定める位相に関する共役分離性。
- compatible な pro-nilpotent conjugator の存在。
- その共役子が離散群 \(\operatorname{Aut}(\pi)\) から来るか。
- さらに境界を保存する写像類から実現されるか。

## 5. この研究への意味

\(N_3\) で共役だったからといって \(N_4\) で必ず非共役になる保証はない。

また、すべての有限段階で共役となる可能性も、現段階では一般論だけでは排除できない。

## 関連ソース

- `residual-nilpotence-and-conjugacy.md`
