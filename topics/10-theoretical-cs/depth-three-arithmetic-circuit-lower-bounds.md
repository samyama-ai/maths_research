---
id: 10-theoretical-cs/depth-three-arithmetic-circuit-lower-bounds
title: "Depth-Three Arithmetic Circuit Lower Bounds over Infinite Fields"
topic: 10-theoretical-cs
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Depth-Three Arithmetic Circuit Lower Bounds over Infinite Fields

> **Topic:** Theoretical Computer Science · **ID:** `10-theoretical-cs/depth-three-arithmetic-circuit-lower-bounds` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

A **$\Sigma\Pi\Sigma$ circuit** (depth-three, unbounded fan-in, over a field $\mathbb{F}$) computes a polynomial as a sum of products of affine forms:
$$C(x_1,\dots,x_n) \;=\; \sum_{i=1}^{s} \prod_{j=1}^{d_i} \ell_{i,j}(x_1,\dots,x_n), \qquad \ell_{i,j} \in \mathbb{F}[x_1,\dots,x_n]_{\le 1}.$$
Its size is $\sum_i d_i$ (equivalently, the number of affine forms, up to a factor $n$ for writing them down).

**The problem.** Exhibit an explicit family $\{f_n\}$ of $n$-variate polynomials of degree $d = d(n)$, computable in $\mathrm{VNP}$ (e.g. the permanent, the determinant, or iterated matrix multiplication), together with a proof that over an infinite field $\mathbb{F}$ of characteristic $0$ every $\Sigma\Pi\Sigma$ circuit computing $f_n$ has size $2^{\omega(\sqrt{d}\,\log n)}$.

**Why that threshold.** By the *chasm at depth three* (Gupta–Kamath–Kayal–Saptharishi 2016), any $n$-variate degree-$d$ polynomial computed by a poly-size arithmetic circuit over a characteristic-zero field is computed by a $\Sigma\Pi\Sigma$ circuit of size $2^{O(\sqrt{d\log d\log n})}$. Hence a lower bound of $2^{\omega(\sqrt{d}\log n)}$ for an explicit $f$ **implies $\mathrm{VP}\neq\mathrm{VNP}$** — Valiant's algebraic analogue of $\mathrm{P}\neq\mathrm{NP}$. A complete solution is a proof (or a proof that the threshold is unattainable, i.e. a matching $2^{O(\sqrt d \log n)}$ depth-3 upper bound for the permanent).

The status is *partially solved*: the analogous question over **fixed finite fields** is settled (exponential bounds, Grigoriev–Karpinski 1998), and superpolynomial bounds over infinite fields exist in restricted degree regimes (Limaye–Srinivasan–Tavenas 2021), but no bound of the strength above is known.

## 2. Mathematical Foundations

Let $\mathbb{F}$ be a field, $\mathbb{F}[\mathbf{x}] = \mathbb{F}[x_1,\dots,x_n]$.

**Circuit classes.** $\Sigma\Pi\Sigma$ is as above; $\Sigma\Pi\Sigma\Pi^{[t]}$ denotes depth four with bottom fan-in (degree of bottom products) at most $t$. A circuit is *homogeneous* if every gate computes a homogeneous polynomial; $\Sigma\Pi\Sigma$ circuits over infinite fields are typically **non**-homogeneous, and this is exactly where their power lies.

**Complexity classes.** $\mathrm{VP}$ = families $(f_n)$ with $\deg f_n, n$ polynomially related and circuit size $\mathrm{poly}(n)$. $\mathrm{VNP}$ = families with $f_n(\mathbf{x}) = \sum_{\mathbf{e}\in\{0,1\}^m} g(\mathbf{x},\mathbf{e})$ for $g\in\mathrm{VP}$. $\mathrm{perm}_n=\sum_{\sigma\in S_n}\prod_i x_{i\sigma(i)}$ is $\mathrm{VNP}$-complete (Valiant 1979).

**Partial-derivative measures.** For $f$ and $k\ge 0$ let $\partial^{=k}(f)$ be the $\mathbb{F}$-span of all order-$k$ partial derivatives, and
$$\mathrm{SP}_{k,\ell}(f) \;=\; \dim_{\mathbb{F}} \big\langle\, \mathbf{x}^{\alpha}\cdot g \;:\; |\alpha|=\ell,\ g\in\partial^{=k}(f) \,\big\rangle$$
the *shifted partial derivative* measure (Kayal; GKKS 2014). Both are subadditive over $+$ and controlled on products of affine forms:
$$\dim \partial^{=k}\Big(\prod_{j=1}^{d}\ell_j\Big) \;\le\; \binom{d}{k}, \qquad \mathrm{SP}_{k,\ell}\Big(\prod_{j=1}^{d}\ell_j\Big)\;\le\;\binom{d}{k}\binom{n+\ell}{n}.$$

**Set-multilinear rank.** If $\mathbf{x}$ is partitioned into $X_1\sqcup\dots\sqcup X_d$ and $f$ is set-multilinear, then for $S\subseteq[d]$ the coefficient matrix $M_S(f)$ has rows indexed by monomials in $\bigcup_{i\in S}X_i$ and columns by monomials in the complement. $\mathrm{rank}(M_S(\cdot))$ is subadditive and multiplicative-friendly; for $\mathrm{IMM}_{n,d}$ (the $(1,1)$ entry of a product of $d$ matrices of size $n\times n$ with distinct variables) one has $\mathrm{rank}(M_S) = n^{\min(|S|,d-|S|)}$ up to the boundary, which is full.

**The depth reductions.** Agrawal–Vinay (2008), Koiran (2012) and Tavenas (2015): a size-$s$ circuit for a degree-$d$, $n$-variate $f$ yields $\Sigma\Pi\Sigma\Pi^{[\sqrt d]}$ of size $2^{O(\sqrt{d}\log(ns))}$. GKKS (2016) push one level further over $\mathbb{F}$ of characteristic $0$:
$$\mathrm{size}_{\Sigma\Pi\Sigma}(f) \;=\; 2^{O\left(\sqrt{d\log d\,\log n}\,\right)} \quad\text{whenever } f\in\mathrm{VP},$$
and $\mathrm{perm}_n$ has $\Sigma\Pi\Sigma$ size $2^{O(\sqrt n\log n)}$ — a genuinely subexponential depth-3 upper bound that has **no analogue over $\mathbb{F}_q$**.

## 3. History & State of the Art (SOTA)

- **1979** Valiant frames $\mathrm{VP}$ vs $\mathrm{VNP}$.
- **1997** Nisan–Wigderson introduce the partial-derivative method; exponential lower bounds for *homogeneous* $\Sigma\Pi\Sigma$ ($2^{\Omega(d)}$ for degree-$d$ polynomials such as $\mathrm{IMM}$) and $n^{\Omega(d)}$ for set-multilinear depth three.
- **1998–2000** Grigoriev–Karpinski, then Grigoriev–Razborov: $2^{\Omega(n)}$ lower bounds for $\det_n$ / $\mathrm{perm}_n$ over any *fixed finite* field, via a rank measure that exploits the fact that a product of affine forms over $\mathbb{F}_q$ vanishes on a constant fraction of $\mathbb{F}_q^n$.
- **2001** Shpilka–Wigderson: over characteristic zero, an $\Omega(n^2)$ lower bound for $\Sigma\Pi\Sigma$ computing the elementary symmetric polynomial $e_d$ (and quadratic bounds for other explicit families) — matching Ben-Or's $O(n^2)$ construction. **This quadratic barrier for general depth-3 over infinite fields has never been broken for constant degree.**
- **2013–2014** GKKS: chasm at depth three; $2^{\Omega(\sqrt d)}$ for $\Sigma\Pi\Sigma\Pi^{[\sqrt d]}$ computing $\mathrm{perm}$, via shifted partial derivatives.
- **2016–2017** Kayal–Saha: $n^{\Omega(\sqrt d)}$-type bounds for $\Sigma\Pi\Sigma$ with **bottom fan-in $\le \sqrt d$** over characteristic zero. Kayal–Limaye–Saha–Srinivasan: $2^{\Omega(\sqrt{d}\log n)}$ for homogeneous depth-four formulas.
- **2021** Limaye–Srinivasan–Tavenas (FOCS): first superpolynomial lower bounds for **general constant-depth** circuits over characteristic-zero fields — for product-depth $\Delta$, computing $\mathrm{IMM}_{n,d}$ requires size $n^{d^{\exp(-\Delta)}}$ in the low-degree regime $d=O(\log n/\log\log n)$.
- **2023–2024** Amireddy–Garg–Kayal–Saha–Thankey sharpen constant-depth bounds without set-multilinearisation; Forbes extends the LST program to fields of arbitrary characteristic.

## 4. Partial Results / Verified Cases

| Restriction | Bound | Source |
|---|---|---|
| $\mathbb{F}$ fixed finite ($\mathbb{F}_q$), general $\Sigma\Pi\Sigma$ | $2^{\Omega(n)}$ for $\det_n$ | Grigoriev–Karpinski 1998 |
| $\mathbb{F}$ arbitrary, **homogeneous** $\Sigma\Pi\Sigma$, degree $d$ | $2^{\Omega(d)}$; $n^{\Omega(d)}$ for $\mathrm{IMM}_{n,d}$ | Nisan–Wigderson 1997 |
| **Set-multilinear** $\Sigma\Pi\Sigma$, $d$ parts | $n^{\Omega(d)}$ | Nisan–Wigderson 1997 |
| $\Sigma\Pi\Sigma$ with **bottom fan-in $\le t \approx \sqrt d$**, char $0$ | $n^{\Omega(\sqrt d)}$ | Kayal–Saha 2016 |
| $\Sigma\Pi\Sigma\Pi^{[\sqrt d]}$, char $0$ | $2^{\Omega(\sqrt d)}$ for $\mathrm{perm}$ | GKKS 2014 |
| General $\Sigma\Pi\Sigma$, char $0$, **constant degree $d$** | $\Omega(n^2)$ for $e_d$, $n^{\Omega(1)}$ only | Shpilka–Wigderson 2001 |
| General constant-depth, char $0$, $d = O(\log n/\log\log n)$ | $n^{\omega(1)}$, namely $n^{d^{\exp(-\Delta)}}$ | LST 2021 |
| Constant-depth, any field | superpolynomial, same regime | Forbes 2024 |

So: exponential over finite fields; exponential over infinite fields once homogeneity, set-multilinearity, or a bottom-fan-in cap is imposed; only superpolynomial (and only for $d\lesssim\log n$) in the unrestricted characteristic-zero case.

## 5. Principal Obstacles

- **Non-homogeneity is a real resource, not a technicality.** Ben-Or's interpolation (Section 10) computes $e_d$ in $\Sigma\Pi\Sigma$ size $O(n^2)$ using massive cancellation among high-degree products of affine forms; homogeneous depth-3 requires $2^{\Omega(d)}$. Every measure that is well behaved on homogeneous components loses to this cancellation.
- **Partial-derivative measures saturate.** $\dim\partial^{=k}(\prod_{j\le d}\ell_j)\le\binom dk$, and *any* $n$-variate polynomial has $\dim\partial^{=k}\le\binom{n+d-k}{n}$. When $d=\Theta(n)$ the two are comparable, so the ratio bounds the circuit size only by a polynomial. Shifted partials fix this only in the low-bottom-fan-in regime, which is precisely where the results of Section 4 stop.
- **Finite-field techniques do not transfer.** Grigoriev–Karpinski count common zeros of affine forms in $\mathbb{F}_q^n$; over $\mathbb{C}$ a hyperplane has measure zero, so no "many roots" argument exists.
- **Set-multilinearisation is lossy.** LST convert general low-depth circuits to set-multilinear ones at a cost of $d^{O(d)}$ or $2^{O(d)}$, forcing $d=O(\log n/\log\log n)$; at $d=n^{\Omega(1)}$ — the regime relevant to $\mathrm{perm}_n$ — the conversion is vacuous.
- **Rank-method barrier.** Efremenko–Garg–Oliveira–Wigderson (2018) show that "rank methods" — lower-bounding via the rank of a linear operator applied to the polynomial, which covers partial derivatives, shifted partials and their relatives — cannot certify tensor/circuit lower bounds beyond roughly the square of the trivial bound.
- **The chasm cuts both ways.** Any depth-3 lower bound above $2^{c\sqrt{d\log d\log n}}$ automatically resolves $\mathrm{VP}\ne\mathrm{VNP}$, so the problem inherits the full difficulty of algebraic complexity.

## 6. The Gap

Proven (char $0$, explicit $f$, general $\Sigma\Pi\Sigma$): size $\ge n^{d^{\exp(-\Delta)}}$ for $d\le O(\log n/\log\log n)$, and $\Omega(n^2)$ for constant $d$.
Required: size $\ge 2^{\omega(\sqrt d\,\log n)}$ at $d=n^{\Omega(1)}$.

Two concrete steps separate them:

1. **Degree barrier.** Push the LST-type lower bound from $d=O(\log n/\log\log n)$ to $d=n^{\varepsilon}$, i.e. find a complexity measure that survives non-set-multilinear, non-homogeneous circuits without the $d^{O(d)}$ conversion loss.
2. **Strength barrier.** Even at high degree, the bound must exceed $2^{\sqrt{d}\log n}$, which is *above* what any known subadditive rank measure can certify against products of $d$ affine forms (their measures are bounded by $\binom{d}{k}\cdot\text{shift}$, capping the achievable ratio).

Crossing step 1 alone would already be a landmark; crossing both is equivalent to $\mathrm{VP}\ne\mathrm{VNP}$.

## 7. Current Research (as of June 2026)

- **Post-LST program** (Limaye, Srinivasan, Tavenas; Forbes; Andrews): extend set-multilinear lower bounds to arbitrary characteristic (Forbes, CCC 2024) and to larger degree by replacing set-multilinearisation with direct decompositions.
- **Bypassing set-multilinearisation** (Amireddy, Garg, Kayal, Saha, Thankey, ICALP 2023): measures applied directly to non-homogeneous low-depth circuits, giving cleaner and in places stronger constant-depth bounds *(frontier — verify the exact depth-3 exponent claimed in the latest version)*.
- **Ideal-theoretic and border complexity methods** (Andrews–Forbes, STOC 2022): lower bounds for polynomial ideals and for *border* $\Sigma\Pi\Sigma$ complexity, where degeneration can only help the circuit.
- **Geometric complexity theory** (Bürgisser, Ikenmeyer, Panova): occurrence obstructions were ruled out for the $\det$ vs $\mathrm{perm}$ setting (2019), redirecting effort towards multiplicity obstructions; depth-3 remains a testbed.
- Active groups: IISc/TIFR/CMI (Kayal, Saha, Limaye, Srinivasan, Saptharishi), UIUC (Forbes), Rutgers/IAS (Saraf, Wigderson), Tel Aviv (Shpilka), Paderborn/Saarbrücken (Ikenmeyer, Bläser).

## 8. Future Work

- Design a measure that is **non-monotone under homogenisation** — sensitive to cancellation between components of different degrees — since every current measure factors through homogeneous parts.
- Prove lower bounds for $\Sigma\Pi\Sigma$ circuits with **bottom fan-in $d^{1/2+\varepsilon}$**, the immediate next case beyond Kayal–Saha, which would already break past the shifted-partials regime.
- Attack **$\Sigma\Pi\Sigma$ over $\mathbb{Q}$ with bounded coefficient bit-length**, where number-theoretic arguments may substitute for the finite-field root-counting.
- Prove **border** lower bounds $\underline{\mathrm{size}}_{\Sigma\Pi\Sigma}$, which are conjecturally no harder and connect to GCT.
- Determine whether the GKKS $2^{O(\sqrt{d\log d\log n})}$ upper bound is tight for $\mathrm{perm}$: a matching depth-3 *upper* bound improvement to $2^{O(\sqrt d)}$ would show the depth-3 route to $\mathrm{VP}\ne\mathrm{VNP}$ is essentially optimal, and any improvement of the reduction narrows the target window.

## 9. Key References

- **[Foundational]** L. G. Valiant. *Completeness classes in algebra.* STOC 1979, 249–261.
- **[Foundational]** N. Nisan, A. Wigderson. *Lower bounds on arithmetic circuits via partial derivatives.* Computational Complexity 6(3):217–234, 1997.
- **[Foundational]** D. Grigoriev, M. Karpinski. *An exponential lower bound for depth 3 arithmetic circuits.* STOC 1998, 577–582.
- **[Foundational]** D. Grigoriev, A. Razborov. *Exponential lower bounds for depth 3 arithmetic circuits in algebras of functions over finite fields.* Applicable Algebra in Engineering, Communication and Computing 10(6):465–487, 2000.
- **[Foundational]** A. Shpilka, A. Wigderson. *Depth-3 arithmetic circuits over fields of characteristic zero.* Computational Complexity 10(1):1–27, 2001.
- **[Depth reduction]** M. Agrawal, V. Vinay. *Arithmetic circuits: A chasm at depth four.* FOCS 2008, 67–75.
- **[Depth reduction]** P. Koiran. *Arithmetic circuits: The chasm at depth four gets wider.* Theoretical Computer Science 448:56–65, 2012.
- **[Depth reduction]** S. Tavenas. *Improved bounds for reduction to depth 4 and depth 3.* Information and Computation 240:2–11, 2015.
- **[Key]** A. Gupta, P. Kamath, N. Kayal, R. Saptharishi. *Arithmetic circuits: A chasm at depth 3.* SIAM Journal on Computing 45(3):1064–1079, 2016 (FOCS 2013).
- **[Key]** A. Gupta, P. Kamath, N. Kayal, R. Saptharishi. *Approaching the chasm at depth four.* Journal of the ACM 61(6):33, 2014.
- **[SOTA]** N. Kayal, C. Saha. *Lower bounds for depth-three arithmetic circuits with small bottom fanin.* Computational Complexity 25(2):419–454, 2016.
- **[SOTA]** N. Kayal, N. Limaye, C. Saha, S. Srinivasan. *An exponential lower bound for homogeneous depth four arithmetic formulas.* SIAM Journal on Computing 46(1):307–335, 2017.
- **[SOTA / Recent]** N. Limaye, S. Srinivasan, S. Tavenas. *Superpolynomial lower bounds against low-depth algebraic circuits.* FOCS 2021, 804–814.
- **[SOTA / Recent]** M. A. Forbes. *Low-depth algebraic circuit lower bounds over any field.* CCC 2024.
- **[SOTA / Recent]** P. Amireddy, A. Garg, N. Kayal, C. Saha, B. Thankey. *Low-depth arithmetic circuit lower bounds: bypassing set-multilinearization.* ICALP 2023.
- **[Barrier]** K. Efremenko, A. Garg, R. Oliveira, A. Wigderson. *Barriers for rank methods in arithmetic complexity.* ITCS 2018.
- **[Survey]** A. Shpilka, A. Yehudayoff. *Arithmetic circuits: A survey of recent results and open questions.* Foundations and Trends in Theoretical Computer Science 5(3–4):207–388, 2010.
- **[Survey]** R. Saptharishi. *A survey of lower bounds in arithmetic circuit complexity.* Living survey, 2015–present.

## 10. Worked Example / Concrete Special Case

**Ben-Or's depth-3 circuit for elementary symmetric polynomials** — the construction that makes the infinite-field case hard.

Let $e_k(x_1,\dots,x_n)=\sum_{|S|=k}\prod_{i\in S}x_i$. Over any field with at least $n+1$ distinct elements $\alpha_0,\dots,\alpha_n$, consider
$$P(y)\;=\;\prod_{i=1}^{n}(y+x_i)\;=\;\sum_{k=0}^{n} e_k(\mathbf{x})\, y^{\,n-k}.$$
Each $P(\alpha_j)=\prod_{i=1}^n(\alpha_j+x_i)$ is a single product of $n$ affine forms. The $(n+1)\times(n+1)$ Vandermonde matrix $V=(\alpha_j^{\,n-k})_{j,k}$ is invertible, so with $(c_0,\dots,c_n)$ the $k$-th row of $V^{-1}$,
$$e_k(\mathbf{x})\;=\;\sum_{j=0}^{n} c_j \prod_{i=1}^{n}(\alpha_j+x_i).$$
This is a $\Sigma\Pi\Sigma$ circuit with $n+1$ product gates, each of fan-in $n$: size $O(n^2)$.

**Take $n=3$, $k=2$, $\alpha_j\in\{0,1,-1\}$.** With $P(y)=y^3+e_1y^2+e_2y+e_3$:
$P(0)=e_3$, $P(1)=1+e_1+e_2+e_3$, $P(-1)=-1+e_1-e_2+e_3$. Hence
$$e_2=\tfrac12\big(P(1)-P(-1)\big)-1 = \tfrac12\prod_{i=1}^3(1+x_i)-\tfrac12\prod_{i=1}^3(-1+x_i)-1,$$
and indeed $\tfrac12[(1+x_1)(1+x_2)(1+x_3)-(x_1-1)(x_2-1)(x_3-1)]-1 = x_1x_2+x_1x_3+x_2x_3$.

**What this shows.** Each summand has degree $3$, but the target $e_2$ has degree $2$: the degree-$3$ and degree-$0$ parts cancel exactly. Consequently $\dim\partial^{=1}$ of each summand is $3$, while $\dim\partial^{=1}(e_2)=3$ as well — the measure certifies nothing. Any measure that first splits a circuit into homogeneous components would see a $2^{\Omega(d)}$-sized homogeneous circuit and give a strong bound, which is *false* for the actual non-homogeneous circuit. Over $\mathbb{F}_2$ the interpolation fails for lack of field elements, and $e_k$ genuinely requires exponential-size depth-3 circuits (Grigoriev–Karpinski). This single example isolates why the infinite-field case is open: the cancellation is real, it is unbounded in the number of degrees involved, and no known subadditive measure survives it.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*