---
id: 01-number-theory/beilinson-bloch-conjecture
title: "Beilinson-Bloch Conjecture on Heights"
topic: 01-number-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Beilinson-Bloch Conjecture on Heights

> **Topic:** Number Theory · **ID:** `01-number-theory/beilinson-bloch-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Let $X$ be a smooth projective geometrically connected variety of dimension $d$ over a number field $k$. Let $\mathrm{CH}^i(X)_0$ denote the group of codimension-$i$ algebraic cycles homologically trivial modulo rational equivalence. The Beilinson–Bloch conjecture asserts:

1. **(Rank conjecture)** The $\mathbb{Q}$-vector space $\mathrm{CH}^i(X)_0 \otimes \mathbb{Q}$ is finite-dimensional and
$$\operatorname{ord}_{s=i} L\big(H^{2i-1}(X), s\big) \;=\; \dim_{\mathbb{Q}} \mathrm{CH}^i(X)_0 \otimes \mathbb{Q}.$$
2. **(Height conjecture)** The Beilinson–Bloch height pairing
$$\langle\,\cdot\,,\,\cdot\,\rangle_{\mathrm{BB}} : \mathrm{CH}^i(X)_0 \otimes \mathbb{Q} \;\times\; \mathrm{CH}^{d+1-i}(X)_0 \otimes \mathbb{Q} \longrightarrow \mathbb{R}$$
is well defined and **non-degenerate**; for $2i = d+1$ it is $(-1)^i$-definite (a conjectural arithmetic Hodge index property).
3. **(Refined / Bloch–Kato form)** The leading Taylor coefficient of $L(H^{2i-1}(X),s)$ at $s=i$ equals, up to periods, the regulator $\det\langle\,\cdot,\cdot\,\rangle_{\mathrm{BB}}$ times a Tamagawa-type factor involving the (conjecturally finite) Selmer-theoretic analogue of Ш.

A complete proof must (i) supply meromorphic continuation of $L(H^{2i-1}(X),s)$ to $s=i$, (ii) construct the height pairing unconditionally, and (iii) prove the rank identity. A disproof would exhibit one $X$, $i$, and $k$ where the two integers differ, or where the pairing is degenerate.

For $i=1$ and $X$ an abelian variety, $\mathrm{CH}^1(X)_0 = \hat X(k)$ and the statement is exactly the Birch–Swinnerton-Dyer rank conjecture. Beilinson–Bloch is the codimension-$\geq 2$ generalization.

## 2. Mathematical Foundations

**The motive and its $L$-function.** Fix a prime $\ell$. The Galois representation $V_\ell = H^{2i-1}_{\mathrm{ét}}(X_{\bar k},\mathbb{Q}_\ell(i))$ is pure of weight $-1$. Its $L$-function is the Euler product
$$L(H^{2i-1}(X),s) \;=\; \prod_{v} \det\!\Big(1 - \mathrm{Frob}_v\, N v^{-s} \,\Big|\, H^{2i-1}_{\mathrm{ét}}(X_{\bar k},\mathbb{Q}_\ell)^{I_v}\Big)^{-1},$$
convergent for $\Re(s) > i + \tfrac12$ by Deligne's Weil I/II bounds $|\alpha_{v,j}| = Nv^{(2i-1)/2}$. The point $s=i$ is the **centre** of the functional equation $s \leftrightarrow 2i - s$. Continuation past $\Re(s)>i+\frac12$ is itself conjectural (known only in automorphic cases).

**Cycle class and Abel–Jacobi.** The $\ell$-adic cycle class map $\mathrm{cl}: \mathrm{CH}^i(X) \to H^{2i}_{\mathrm{ét}}(X_{\bar k},\mathbb{Q}_\ell(i))$ has kernel $\mathrm{CH}^i(X)_0$ (after $\otimes\mathbb{Q}$), and Bloch's $\ell$-adic Abel–Jacobi map
$$\mathrm{AJ}_\ell : \mathrm{CH}^i(X)_0 \otimes \mathbb{Q}_\ell \longrightarrow H^1\big(k, H^{2i-1}_{\mathrm{ét}}(X_{\bar k},\mathbb{Q}_\ell(i))\big)$$
lands in the Bloch–Kato Selmer group $H^1_f(k,V_\ell)$.

**The height pairing.** For $Z \in \mathrm{CH}^i(X)_0$ and $W \in \mathrm{CH}^{d+1-i}(X)_0$ with disjoint supports,
$$\langle Z, W\rangle_{\mathrm{BB}} \;=\; \sum_{v \nmid \infty} \langle Z,W\rangle_v \log Nv \;+\; \sum_{v \mid \infty} \langle Z,W\rangle_v .$$
At $v\mid\infty$, $\langle Z,W\rangle_v = \int_{X(\mathbb{C}_v)} g_Z \wedge \delta_W$ using a Green current $g_Z$ with $dd^c g_Z + \delta_Z = 0$ (harmonic projection zero since $Z$ is homologically trivial). At a finite $v$, one picks a regular proper model $\mathcal{X}/\mathcal{O}_v$ and sets $\langle Z,W\rangle_v = (\bar{\mathcal{Z}}\cdot\bar{\mathcal{W}})_v$, where $\bar{\mathcal{Z}}$ is a $\mathbb{Q}$-extension of $Z$ chosen **orthogonal to all vertical cycles** in the special fibre. Existence of such a correction is guaranteed for $i=1$ by the negative semidefiniteness of the intersection form on the special fibre; in general it requires the cycle class of $\mathcal{Z}$ to vanish in $H^{2i}$ of the special fibre — a consequence of the standard conjectures, not a theorem. The whole framework sits inside Gillet–Soulé arithmetic intersection theory on $\widehat{\mathrm{CH}}^\bullet(\mathcal{X})$.

**Conjectural inputs used.** Grothendieck's standard conjectures (for well-definedness at bad primes), the Bloch–Beilinson filtration $F^\bullet \mathrm{CH}^i(X)_\mathbb{Q}$ with $\mathrm{gr}^\nu$ controlled by $\mathrm{Ext}^\nu$ in a category of mixed motives, and finiteness of the Tate–Shafarevich analogue $\mathrm{Ш}(V_\ell)$.

## 3. History & State of the Art (SOTA)

- **1965–1974.** Birch and Swinnerton-Dyer formulate the $i=1$ case numerically; Tate reformulates it and states the function-field analogue via the Tate conjecture on surfaces.
- **1969.** Griffiths shows homological and algebraic equivalence differ (quintic threefold), so $\mathrm{CH}^2(X)_0$ genuinely exceeds the "obvious" part.
- **1983.** Clemens proves the Griffiths group of the quintic threefold over $\mathbb{C}$ has infinite rank — showing the finiteness in Conjecture 1 is *arithmetic*, false over $\mathbb{C}$.
- **1984.** Bloch, *Height pairings for algebraic cycles* (J. Pure Appl. Algebra 34), constructs the pairing conditionally.
- **1986–87.** Beilinson states the rank conjecture and the height pairing in general form (*Height pairing between algebraic cycles*, LNM 1289), fitting it into his conjectures on special values.
- **1986.** Gross–Zagier prove the height formula for Heegner points: the $i=1$, modular-curve case in analytic rank 1.
- **1992, 1997.** Nekovář extends Kolyvagin's Euler system to Chow groups of Kuga–Sato varieties; S. Zhang proves the Gross–Zagier formula for **Heegner cycles** in codimension $i=k$ on Kuga–Sato varieties of weight-$2k$ forms — the first genuine codimension-$\geq2$ evidence.
- **2013–2022.** Yuan–Zhang–Zhang give the Gross–Zagier formula on Shimura curves and, for Gross–Kudla–Schoen cycles, relate heights to $L'(1/2)$ of triple-product $L$-functions. The arithmetic Gan–Gross–Prasad programme (Wei Zhang's arithmetic fundamental lemma, Rapoport–Smithling–Zhang, Chao Li–Yifeng Liu) proves rank-one lower bounds for unitary Shimura varieties in arbitrary dimension.
- **2017.** Yun–Zhang prove a *higher* Gross–Zagier formula over function fields, giving cycle-theoretic meaning to all Taylor coefficients — the strongest structural evidence for the conjecture in any setting.

## 4. Partial Results / Verified Cases

- **$i=1$, abelian varieties over $\mathbb{Q}$, analytic rank $\le 1$:** proved (Gross–Zagier + Kolyvagin, with modularity for elliptic curves); this is the BSD rank statement.
- **Trivial-Chow-group cases:** if $H^{2i-1}(X)=0$ (so $L \equiv 1$) and $\mathrm{CH}^i(X)_0\otimes\mathbb{Q}=0$ — e.g. cellular varieties, Grassmannians, toric varieties, and varieties with $\mathrm{CH}_0$ supported on a subvariety via Bloch–Srinivas — the conjecture holds trivially in that codimension.
- **Heegner cycles, $i=k$, on the Kuga–Sato variety $W_{2k-2} \to X_0(N)$ of dimension $2k-1$:** for weight-$2k$ newforms with $L(f,k)=0$ and $L'(f,k)\neq 0$, S. Zhang (1997) computes $\langle y_f, y_f\rangle_{\mathrm{BB}} \doteq L'(f,k)$; Nekovář (1992) proves $\dim \mathrm{CH}^k(W)_{0,f} \le 1$ when $L'(f,k)\ne0$. Combined: the rank conjecture holds in analytic rank $\le 1$ for these motives.
- **Gross–Kudla–Schoen cycles $\Delta_{GKS} \subset X^3$, $i=2$, $d=3$:** Yuan–Zhang–Zhang relate $\langle \Delta_{GKS},\Delta_{GKS}\rangle$ to $L'(1/2,\pi_1\times\pi_2\times\pi_3)$ for triple products of modular curves.
- **Unitary Shimura varieties $\mathrm{Sh}(U(n-1,1))$, $i=n/2$-type middle cycles:** Chao Li–Yifeng Liu (*Ann. of Math.* 194, 2021; *Forum Math. Pi* 10, 2022) prove, for cuspidal automorphic $\Pi$ of $U(n)\times U(n+1)$ satisfying local conditions at ramified/inert places, that $L'(1/2,\Pi)\neq 0 \Rightarrow \dim \mathrm{CH}^{\ast}(\ )_{0,\Pi}\otimes\mathbb{Q} \ge 1$, in **all** dimensions $n$, plus the reverse Euler-system bound giving $\le 1$ under hypotheses.
- **Function fields:** Yun–Zhang (2017) prove, for $\mathrm{PGL}_2$ over $\mathbb{F}_q(t)$ with everywhere-unramified everything, an identity between $\frac{1}{r!}L^{(r)}(\pi,1/2)$ and intersection numbers of Heegner–Drinfeld cycles on moduli of shtukas — the rank conjecture's analogue in arbitrary order $r$.
- **Non-degeneracy:** proved for $i=1$ (Néron–Tate positivity), and for abelian varieties in some codimensions by Künnemann (2001) under semistability hypotheses.

## 5. Principal Obstacles

- **The height pairing is not unconditionally defined.** At primes of bad reduction, subtracting the vertical component of $\bar{\mathcal Z}$ needs an orthogonality statement equivalent to a case of the standard conjectures. For $i=1$ the Zariski/Hodge-index argument on the special fibre supplies it; in higher codimension no substitute exists.
- **No finite-generation theorem.** $\mathrm{CH}^i(X)_0\otimes\mathbb{Q}$ is not known to be finite-dimensional for a *single* variety with $i\ge2$ and nontrivial cycles. Mordell–Weil's proof (heights + weak Mordell–Weil via Kummer theory on $A(k)/mA(k)$) has no analogue: there is no group scheme whose points are codimension-2 cycles, hence no descent.
- **No continuation of $L$.** Outside automorphic motives, $L(H^{2i-1}(X),s)$ is not known to reach $s=i$, so "$\operatorname{ord}_{s=i}$" is meaningless in general. This makes the conjecture unfalsifiable numerically for generic $X$.
- **Euler systems stop at rank 1.** Kolyvagin/Nekovář-type arguments bound Selmer ranks by $1$ only; and even the upper bound $\dim\mathrm{CH}^i_0 \le \dim H^1_f$ requires injectivity of $\mathrm{AJ}_\ell$ modulo torsion, itself open (a Bloch–Beilinson consequence).
- **Cycle construction is sporadic.** When $\operatorname{ord}\ge 2$, no mechanism produces independent cycles. Special cycles (Heegner, Kudla–Rapoport, diagonal) come from embeddings of smaller Shimura varieties and are structurally one-dimensional families.
- **Archimedean analysis.** Green currents for higher-codimension cycles are only defined up to $\partial,\bar\partial$-exact terms; explicit star-product computations (Gillet–Soulé) become intractable beyond codimension 2.

## 6. The Gap

Proven: analytic rank $0$ and $1$, for motives that are (a) automorphic, so $L$ continues, and (b) equipped with a geometric family of special cycles supplying the generator. Conjectured: an unconditional statement for arbitrary $X/k$, arbitrary $i$, arbitrary order of vanishing.

The gap has three sharply separable components:

1. **Definedness.** Prove the local height at bad $v$ exists for $i \ge 2$ without assuming standard conjectures (or prove enough of the standard conjectures).
2. **Finiteness / descent.** Prove $\dim_\mathbb{Q}\mathrm{CH}^2(X)_0\otimes\mathbb{Q} < \infty$ for even one surface over $\mathbb{Q}$ with $p_g>0$. This is the higher Mordell–Weil problem and no strategy is known.
3. **Order $\ge 2$.** Construct cycles from higher derivatives. Yun–Zhang show this is possible over $\mathbb{F}_q(t)$ using moduli of shtukas with $r$ legs; the number-field side has no object playing the role of "$r$ legs".

## 7. Current Research (as of June 2026)

- **Arithmetic Gan–Gross–Prasad / Kudla programme** (Columbia, MIT, Bonn, Tsinghua/BICMR): Chao Li, Wei Zhang, Yifeng Liu, Rapoport, Smithling. Extending arithmetic Siegel–Weil and the Kudla–Rapoport conjecture to ramified and archimedean places, removing hypotheses from the Li–Liu theorems.
- **Higher Gross–Zagier over number fields:** attempts to import Yun–Zhang's shtuka argument, e.g. via derived Hecke actions and derived special cycles in derived algebraic geometry (Feng–Yun–W. Zhang's "higher theta series" and modularity of derived special cycle classes). *(frontier — verify)*
- **$p$-adic and Iwasawa-theoretic surrogates:** $p$-adic height pairings on Selmer complexes (Nekovář), plectic and Bloch–Kato refinements; these are defined unconditionally more often than the archimedean pairing.
- **Beilinson–Bloch for Rankin–Selberg and $\mathrm{GSp}_4$ motives** via Euler systems (Loeffler–Skinner–Zerbes) giving rank-0 and rank-1 results for codimension-2 cycles on Siegel threefolds. *(frontier — verify)*
- **Unconditional height pairings** via Yuan–Zhang's adelic line bundles and arithmetic Hodge index, extending definedness beyond divisors.

## 8. Future Work

- Prove the **Hodge standard conjecture** in the codimensions needed to make the local height well defined; this is the cleanest route to unconditional definedness.
- Develop a **descent theory for higher Chow groups**: a $K$-theoretic weak Mordell–Weil statement bounding $\mathrm{CH}^i(X)_0/m$ by a Selmer group. Beilinson–Soulé vanishing is a prerequisite.
- Transport the **shtuka/legs mechanism** to number fields, or find a "derived" Gross–Zagier producing $r$ independent cycles from $L^{(r)}$.
- Systematic **numerical verification**: compute Abel–Jacobi images and heights of Gross–Kudla–Schoen cycles on triple products of small modular curves and compare with triple-product $L$-derivatives.
- Settle **non-degeneracy for abelian varieties** in all codimensions, where Künnemann's Fourier-transform methods are strongest.

## 9. Key References

- **[Foundational]** S. Bloch. *Height pairings for algebraic cycles.* Journal of Pure and Applied Algebra 34 (1984), 119–145.
- **[Foundational]** A. Beilinson. *Height pairing between algebraic cycles.* In *K-theory, Arithmetic and Geometry*, Lecture Notes in Math. 1289, Springer, 1987, 1–25.
- **[Foundational]** A. Beilinson. *Higher regulators and values of $L$-functions.* Journal of Soviet Mathematics 30 (1985), 2036–2070.
- **[Foundational]** B. Gross and D. Zagier. *Heegner points and derivatives of $L$-series.* Inventiones Mathematicae 84 (1986), 225–320.
- **[Foundational]** H. Gillet and C. Soulé. *Arithmetic intersection theory.* Publications Mathématiques de l'IHÉS 72 (1990), 93–174.
- **[Partial results]** J. Nekovář. *Kolyvagin's method for Chow groups of Kuga–Sato varieties.* Inventiones Mathematicae 107 (1992), 99–125.
- **[Partial results]** S.-W. Zhang. *Heights of Heegner cycles and derivatives of $L$-series.* Inventiones Mathematicae 130 (1997), 99–152.
- **[Partial results]** B. Gross and C. Schoen. *The modified diagonal cycle on the triple product of a pointed curve.* Annales de l'Institut Fourier 45 (1995), 649–679.
- **[Partial results]** H. Clemens. *Homological equivalence, modulo algebraic equivalence, is not finitely generated.* Publications Mathématiques de l'IHÉS 58 (1983), 19–38.
- **[SOTA / Recent]** X. Yuan, S.-W. Zhang, W. Zhang. *The Gross–Zagier Formula on Shimura Curves.* Annals of Mathematics Studies 184, Princeton University Press, 2013.
- **[SOTA / Recent]** Z. Yun and W. Zhang. *Shtukas and the Taylor expansion of $L$-functions.* Annals of Mathematics 186 (2017), 767–911.
- **[SOTA / Recent]** W. Zhang. *Weil representation and arithmetic fundamental lemma.* Annals of Mathematics 193 (2021), 863–978.
- **[SOTA / Recent]** C. Li and Y. Liu. *Chow groups and $L$-derivatives of automorphic motives for unitary groups.* Annals of Mathematics 194 (2021), 817–901; part II, Forum of Mathematics Pi 10 (2022), e5.
- **[SOTA / Recent]** M. Rapoport, B. Smithling, W. Zhang. *Arithmetic diagonal cycles on unitary Shimura varieties.* Compositio Mathematica 156 (2020), 1745–1824.
- **[SOTA / Recent]** C. Li and W. Zhang. *Kudla–Rapoport cycles and derivatives of local densities.* Journal of the American Mathematical Society 35 (2022), 705–797.
- **[SOTA / Recent]** X. Yuan and S.-W. Zhang. *The arithmetic Hodge index theorem for adelic line bundles.* Mathematische Annalen 367 (2017), 1123–1171.
- **[Survey]** U. Jannsen. *Motivic sheaves and filtrations on Chow groups.* In *Motives*, Proceedings of Symposia in Pure Mathematics 55, AMS, 1994, 245–302.
- **[Survey]** S. Bloch. *Lectures on Algebraic Cycles*, 2nd edition. Cambridge University Press, 2010.
- **[Survey]** C. Soulé, D. Abramovich, J.-F. Burnol, J. Kramer. *Lectures on Arakelov Geometry.* Cambridge University Press, 1992.

## 10. Worked Example / Concrete Special Case

**(a) The codimension-1 case: $X = E$, the elliptic curve 37a1 over $\mathbb{Q}$.**

$E: y^2 + y = x^3 - x$, conductor $37$, $d = 1$, $i = 1$. Here $H^{2i-1}(X) = H^1(E)$ and $L(H^1(E),s)$ is the Hasse–Weil $L$-function; the centre is $s=1$. Since $37$ is prime and $E$ is modular, $L(E,s)$ continues entirely, and the sign of the functional equation is $-1$, forcing $L(E,1)=0$.

$\mathrm{CH}^1(E)_0 = \mathrm{Pic}^0(E) = E(\mathbb{Q})$, which is infinite cyclic generated by $P=(0,0)$, with $E(\mathbb{Q})_{\mathrm{tors}}=0$. So the right-hand side of the rank conjecture is $1$. Numerically $L'(E,1) = 0.30599\ldots \neq 0$, so $\operatorname{ord}_{s=1}L = 1$ and the identity holds.

The height pairing $\langle\,,\rangle_{\mathrm{BB}}$ on $\mathrm{CH}^1(E)_0 \times \mathrm{CH}^1(E)_0$ is exactly twice the Néron–Tate height, and
$$\hat h(P) = 0.0511114082\ldots, \qquad \Omega_E = 5.98691729\ldots$$
The BSD leading-coefficient formula, with $c_{37}=1$, $|Ш|=1$, $|E(\mathbb{Q})_{\mathrm{tors}}|=1$, predicts
$$L'(E,1) \;=\; \frac{\Omega_E \cdot \mathrm{Reg}(E) \cdot \prod_p c_p \cdot |Ш|}{|E(\mathbb{Q})_{\mathrm{tors}}|^2} \;=\; 5.98691729 \times 0.0511114082 \;=\; 0.30599\ldots,$$
matching the analytic value. This is a fully verified instance of Beilinson–Bloch with $i=1$, and shows the height pairing is non-degenerate here ($\hat h(P)>0$ by Néron–Tate positivity).

**(b) Why $i=2$ is different: the Gross–Kudla–Schoen cycle.**

Take $C/\mathbb{Q}$ a smooth projective curve with a rational base point $e$, and $X = C^3$, so $d=3$, $i=2$, $2i = d+1$: the middle codimension. Write $\Delta_{123} \subset C^3$ for the small diagonal and $\Delta_{12} = \{(x,x,e)\}$, etc. The modified diagonal is
$$\Delta_{GKS} \;=\; \Delta_{123} - \Delta_{12} - \Delta_{13} - \Delta_{23} + \Delta_1 + \Delta_2 + \Delta_3 \;\in\; \mathrm{CH}^2(C^3),$$
with $\Delta_1 = \{e\}\times\{e\}\times C$ and cyclic variants. A direct Künneth computation shows $\mathrm{cl}(\Delta_{GKS}) = 0$ in $H^4(C^3_{\bar{\mathbb{Q}}},\mathbb{Q}_\ell(2))$: each correction term cancels the corresponding Künneth component of $\Delta_{123}$. So $\Delta_{GKS} \in \mathrm{CH}^2(C^3)_0$.

If $C$ has genus $0$ or $1$, $\Delta_{GKS}$ is rationally trivial, and correspondingly $H^3(C^3)$ contributes no interesting motive. For $g \ge 2$, the relevant motive is $\bigotimes_{j=1}^3 H^1(C)$, whose $L$-function is a triple-product $L$-function $L(s,\pi_1\times\pi_2\times\pi_3)$ when $C$ is modular. Beilinson–Bloch predicts
$$\operatorname{ord}_{s=2} L\big(H^1(C)^{\otimes 3},s\big) \;=\; \dim_{\mathbb{Q}} \mathrm{CH}^2(C^3)_0\otimes\mathbb{Q},$$
and the Yuan–Zhang–Zhang height formula supplies the rank-one half: $\langle \Delta_{GKS},\Delta_{GKS}\rangle_{\mathrm{BB}} \doteq L'(1/2,\pi_1\times\pi_2\times\pi_3)$ up to explicit local factors. Note the contrast with part (a): here the finite-dimensionality of $\mathrm{CH}^2(C^3)_0\otimes\mathbb{Q}$ is *not known*, and the local height at a prime of bad reduction of $C$ requires the orthogonality correction discussed in Section 5. The example therefore isolates exactly the gap: the analytic side is fully understood, the cycle side is not even known to be finite-dimensional.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*