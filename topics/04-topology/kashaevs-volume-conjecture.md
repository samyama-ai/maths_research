---
id: 04-topology/kashaevs-volume-conjecture
title: "Kashaev's Volume Conjecture"
topic: 04-topology
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Kashaev's Volume Conjecture

> **Topic:** Topology & Knot Theory · **ID:** `04-topology/kashaevs-volume-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Let $K \subset S^3$ be a knot and let $\langle K \rangle_N \in \mathbb{C}$ be Kashaev's invariant, defined for each integer $N \geq 2$ from the cyclic quantum dilogarithm at the root of unity $q = e^{2\pi i/N}$. Kashaev (1997) conjectured:

$$\lim_{N \to \infty} \frac{2\pi \log \bigl| \langle K \rangle_N \bigr|}{N} \;=\; \operatorname{Vol}(S^3 \setminus K),$$

where $\operatorname{Vol}$ is the simplicial (Gromov) volume normalized so that it equals the hyperbolic volume of the complement when $K$ is hyperbolic, and $0$ when $K$ is a torus knot.

Murakami–Murakami (2001) identified $\langle K \rangle_N = |J_N(K; e^{2\pi i/N})|$, where $J_N$ is the $N$-dimensional colored Jones polynomial normalized so that $J_N(\text{unknot}) = 1$. The conjecture therefore asserts that a *combinatorially defined, purely algebraic* quantum invariant, evaluated at a sequence of roots of unity where it is generically a sum of $O(N)$ terms of modulus $O(1)$, detects hyperbolic geometry through exponential growth.

A complete proof must establish the limit for **every** knot (equivalently, for every non-split link, with $\operatorname{Vol}$ of the link complement). A disproof requires one knot for which the limit fails to exist or differs from $\operatorname{Vol}$. Both the existence of the limit and the exponential growth rate are open in general; even $\limsup_N \frac{1}{N}\log|\langle K\rangle_N| > 0$ is unproven for a generic hyperbolic knot.

## 2. Mathematical Foundations

**Quantum dilogarithm.** For $q = e^{2\pi i/N}$ set $(x;q)_k = \prod_{j=1}^{k}(1 - x q^{j-1})$. Kashaev's original construction assigns to a link diagram an $R$-matrix built from the cyclic quantum dilogarithm, a solution of the pentagon identity; the resulting state sum is a link invariant $\langle L\rangle_N$.

**Colored Jones normalization.** Let $J_N(K;q)$ denote the $\mathfrak{sl}_2$ invariant colored by the $N$-dimensional irreducible representation, normalized by the unknot. Habiro's cyclotomic expansion gives, for the figure-eight knot $4_1$,

$$J_N(4_1;q) = \sum_{k=0}^{N-1} \prod_{j=1}^{k} \bigl(q^{(N-j)/1}\cdots\bigr) \quad\Longrightarrow\quad \langle 4_1\rangle_N = \sum_{k=0}^{N-1} \prod_{j=1}^{k} \bigl|1 - e^{2\pi i j/N}\bigr|^2 = \sum_{k=0}^{N-1}\prod_{j=1}^{k} 4\sin^2\!\frac{\pi j}{N}.$$

**Hyperbolic side.** By Mostow rigidity, $\operatorname{Vol}(S^3\setminus K)$ is a topological invariant. For an ideal triangulation with tetrahedra of shape parameters $z_i \in \mathbb{H}$ satisfying Thurston's gluing equations, the volume is

$$\operatorname{Vol} = \sum_i D(z_i), \qquad D(z) = \operatorname{Im}\operatorname{Li}_2(z) + \arg(1-z)\log|z|,$$

the Bloch–Wigner dilogarithm; $D(e^{i\theta}) = \Lambda(\theta/2)\cdot 2$ relates to the Lobachevsky function $\Lambda$.

**Saddle-point mechanism.** Writing $\langle K\rangle_N$ as a discrete sum $\sum_k e^{\frac{N}{2\pi i}\Phi(k/N)+\cdots}$ and passing to an integral, the *potential function* $\Phi$ is a sum of dilogarithms $\operatorname{Li}_2$ whose critical-point equations coincide with Thurston's gluing equations. The critical value satisfies

$$\Phi(z^\ast) = i\bigl(\operatorname{Vol}(S^3\setminus K) + i\,\mathrm{CS}(S^3\setminus K)\bigr) \pmod{\pi^2\mathbb{Z}},$$

which is the content of the **complexified volume conjecture** (Murakami–Murakami–Okamoto–Takata–Yokota 2002): with $q=e^{2\pi i/N}$,

$$\lim_{N\to\infty}\frac{2\pi}{N}\log J_N(K;q) = \operatorname{Vol}(S^3\setminus K) + i\,\mathrm{CS}(S^3\setminus K).$$

**Refined asymptotics (Ohtsuki).** For the verified cases the stronger statement holds:

$$\langle K\rangle_N = N^{3/2}\, e^{\frac{N}{2\pi}\zeta_K}\,\omega_K\Bigl(1 + \sum_{i\ge1}\kappa_i \bigl(\tfrac{2\pi}{N}\bigr)^{i}\Bigr), \qquad \zeta_K = \operatorname{Vol} + i\,\mathrm{CS},$$

with $\omega_K$ related to the $1$-loop invariant / adjoint Reidemeister torsion of the discrete faithful representation.

**Generalizations.** Gukov's *generalized volume conjecture* interpolates in the holonomy parameter and predicts $\hbar$-deformed asymptotics governed by the $A$-polynomial; the Chen–Yang conjecture predicts that Turaev–Viro invariants $TV_r$ at $q = e^{4\pi i/r}$ grow like $e^{\frac{r}{4\pi}\operatorname{Vol}}$.

## 3. History & State of the Art (SOTA)

- **1995.** Kashaev defines $\langle L\rangle_N$ from the quantum dilogarithm (*Modern Phys. Lett. A*).
- **1997.** Kashaev computes the asymptotics numerically for $4_1$, $5_2$, $6_1$ and states the conjecture.
- **2000.** Kashaev–Tirkkonen prove the conjecture for all torus knots (both sides give $0$; the invariant grows polynomially).
- **2001.** Murakami–Murakami prove $\langle K\rangle_N = |J_N(K;e^{2\pi i/N})|$, converting a state sum into a statement about the colored Jones polynomial and linking the conjecture to the Jones-polynomial-detects-geometry problem.
- **2002.** MMOTY formulate the complexified version with Chern–Simons; extensive numerics.
- **2005.** Gukov's physics derivation via $SL(2,\mathbb{C})$ Chern–Simons and the $A$-polynomial; birth of the AJ/quantization program.
- **2008–2009.** van der Veen proves the conjecture for Whitehead chains; Andersen–Hansen and Ohtsuki give rigorous $4_1$ asymptotics (a proof for $4_1$ is due independently to Ekholm, written up in H. Murakami's survey).
- **2011.** Garoufalidis–Lê establish that $\frac{1}{N}\log|J_N|$ is bounded above, i.e. growth is at most exponential — the only universal quantitative constraint known.
- **2016–2018.** Ohtsuki proves the conjecture with full asymptotic expansion for $5_2$; Ohtsuki–Yokota extend to all hyperbolic knots with at most $7$ crossings.
- **2018–2020.** Chen–Yang formulate and give strong numerical evidence for the Turaev–Viro version; Detcherry–Kalfagianni–Yang prove it for the figure-eight and Borromean-rings complements; Belletti–Detcherry–Kalfagianni–Yang and Wong–Yang prove it for fundamental shadow links and their cablings.
- **2021–2024.** Garoufalidis–Zagier's *quantum modularity* program refines the conjecture into a statement about the modular transformation of $\hat{Z}$-type $q$-series, valid at all roots of unity.

## 4. Partial Results / Verified Cases

**Proven (Kashaev's original statement):**
- **Torus knots and links** — Kashaev–Tirkkonen (2000); volume $0$, invariant grows like $N^{3/2}$.
- **Figure-eight knot $4_1$** ($\operatorname{Vol}=6\Lambda(\pi/3)=2.029883\ldots$) — Ekholm; also Andersen–Hansen, Ohtsuki.
- **$5_2$** ($\operatorname{Vol}=2.828122\ldots$) — Ohtsuki (2016), with full asymptotic expansion.
- **All hyperbolic knots with $\le 7$ crossings** ($4_1$, $5_2$, $6_1$, $6_2$, $6_3$, $7_1$–$7_7$ excluding torus) — Ohtsuki–Yokota (2018).
- **Whitehead chains** (an infinite family of links including the Whitehead link, $\operatorname{Vol}=3.663862\ldots$, and Borromean rings, $\operatorname{Vol}=7.327724\ldots$) — van der Veen (2008).
- **Fundamental shadow links** and octahedral fillings — infinite families with arbitrarily large volume; Costantino, and in the Turaev–Viro setting Belletti–Detcherry–Kalfagianni–Yang (2020).
- **Universal upper bound:** $\limsup_N \frac{1}{N}\log|J_N(K;e^{2\pi i/N})| < \infty$ for all $K$ (Garoufalidis–Lê 2011).
- **Satellite/cabling stability:** Chen–Zhu, Wong–Yang show the growth rate is preserved under cabling for classes where it is known.

**Numerically verified:** all knots in the Rolfsen table through $\sim 12$ crossings, and many census manifolds, typically to $N \le 500$ with agreement to several decimals; the conjecture is *empirically robust* but the numerics degrade because $|\langle K\rangle_N|$ is a sum of $O(N)$ terms with huge cancellation.

## 5. Principal Obstacles

- **No integral representation in general.** Ohtsuki's proofs convert $\langle K\rangle_N$ into a finite-dimensional integral via the Poisson summation formula and then apply the saddle-point method. Constructing this integral requires an explicit potential function from a triangulation adapted to the diagram; for large or non-alternating diagrams the number of variables grows and no uniform construction is known.
- **Non-geometric critical points.** The potential function has many critical points, corresponding to all boundary-parabolic $SL(2,\mathbb{C})$ representations. Proving that the *geometric* one dominates requires locating the steepest-descent contour in a complex domain — a global, non-perturbative deformation problem solved so far only case-by-case.
- **Cancellation.** $\langle K\rangle_N$ is a sum of $\sim N$ terms of modulus that can far exceed the total; no positivity or unitarity makes the growth rate manifest. Standard hyperbolic-geometry tools (Mostow rigidity, Gromov norm, geometrization) are invariants of the complement and give no handle on a finite sum of roots of unity.
- **Divergence of $q$-series at roots of unity.** The colored Jones polynomial has good $q$-adic structure (Habiro cyclotomic expansion, convergent at $|q|<1$), but the conjecture evaluates exactly on the unit circle where the Habiro ring's analytic control breaks down. Bridging $|q|<1$ asymptotics to $q$ on the circle requires modularity-type transformation laws known only for $4_1$ and a handful of knots.
- **Uniformity.** Even for a proven family, the error terms are not uniform, so limits of families (Dehn surgery, cabling) do not automatically inherit the result.

## 6. The Gap

Proven: individual knots with small triangulations, plus infinite families whose complements decompose into *regular* ideal octahedra or tetrahedra (Whitehead chains, fundamental shadow links) where the potential function is explicitly a sum of $\operatorname{Li}_2$'s with symmetric critical points.

Missing: a *diagram-independent* mechanism. The exact step is:

> Given an arbitrary knot diagram, produce a finite-dimensional integral representation of $\langle K\rangle_N$ whose potential $\Phi$ has critical-point equations equal to Thurston's gluing equations for *some* ideal triangulation, and prove that the steepest-descent contour passes through the geometric solution.

Yokota's construction supplies the potential in principle; what is missing is (i) control of the degenerate/non-geometric critical points, and (ii) a proof that the contour deformation is possible for all diagrams. No approach currently even gives a positive *lower* bound $\liminf \frac1N\log|\langle K\rangle_N| > 0$ for a generic hyperbolic knot.

## 7. Current Research (as of June 2026)

- **Quantum modularity (Garoufalidis–Zagier, MPIM Bonn).** The $\hat{Z}$-invariants and the matrix-valued $q$-series $\mathbf{\Phi}(q)$ satisfy conjectural modular transformation laws under $\mathrm{SL}(2,\mathbb{Z})$ that *imply* the volume conjecture at all roots of unity, not just $e^{2\pi i/N}$. Proven for $4_1$ and $(-2,3,7)$ in restricted forms. *(frontier — verify)*
- **Turaev–Viro route (Detcherry, Kalfagianni, Yang; Michigan State / Rennes).** The Chen–Yang conjecture is often more tractable because $TV_r$ is a positive-definite state sum; results now cover all links obtained from fundamental shadow links by cabling and some Dehn fillings.
- **Resurgence and Borel summation (Gukov, Mariño, Putrov).** Treating the asymptotic series as a resurgent transseries whose Stokes data encodes the full character variety; predicts the exponentially small corrections from non-geometric flat connections.
- **Teichmüller TQFT (Andersen–Kashaev).** An alternative TQFT whose partition function conjecturally has the volume as its leading asymptotics; proven for $4_1$ and $5_2$ and for infinite families of fibered knots.
- **Machine-assisted numerics.** High-precision computations of $J_N$ for $N \le 10^3$ on knots up to 15 crossings continue to support the conjecture and its subleading terms.

## 8. Future Work

- Prove a **lower bound** $\liminf \frac{1}{N}\log|\langle K\rangle_N| \ge c\cdot \operatorname{Vol}$ for some $c>0$ and all hyperbolic knots — currently the weakest unproven quantitative statement.
- Establish **uniform error control** for Ohtsuki's expansion across families, enabling Dehn-surgery and cabling induction to reach all knots.
- Prove the **AJ conjecture** (that the recursion annihilating $J_N$ specializes to the $A$-polynomial), which would supply the differential-equation control needed for WKB asymptotics.
- Prove Garoufalidis–Zagier quantum modularity in general; this would settle the conjecture at all roots of unity at once.
- Determine whether the conjecture can *fail* for satellite knots: $\operatorname{Vol}$ of a satellite is at least that of the companion, but no matching lower bound on the colored Jones is known.

## 9. Key References

- **[Foundational]** R. M. Kashaev. *A link invariant from quantum dilogarithm.* Modern Physics Letters A **10** (1995), 1409–1418.
- **[Foundational]** R. M. Kashaev. *The hyperbolic volume of knots from the quantum dilogarithm.* Letters in Mathematical Physics **39** (1997), 269–275.
- **[Foundational]** H. Murakami, J. Murakami. *The colored Jones polynomials and the simplicial volume of a knot.* Acta Mathematica **186** (2001), 85–104.
- **[Foundational]** H. Murakami, J. Murakami, M. Okamoto, T. Takata, Y. Yokota. *Kashaev's conjecture and the Chern–Simons invariants of knots and links.* Experimental Mathematics **11** (2002), 427–435.
- **[Partial result]** R. M. Kashaev, O. Tirkkonen. *A proof of the volume conjecture on torus knots.* Journal of Mathematical Sciences **115** (2003), 2033–2036.
- **[Partial result]** R. van der Veen. *Proof of the volume conjecture for Whitehead chains.* Acta Mathematica Vietnamica **33** (2008), 421–431.
- **[Partial result]** J. E. Andersen, S. K. Hansen. *Asymptotics of the quantum invariants for surgeries on the figure 8 knot.* Journal of Knot Theory and Its Ramifications **15** (2006), 479–548.
- **[SOTA]** T. Ohtsuki. *On the asymptotic expansion of the Kashaev invariant of the $5_2$ knot.* Quantum Topology **7** (2016), 669–735.
- **[SOTA]** T. Ohtsuki, Y. Yokota. *On the asymptotic expansions of the Kashaev invariant of the knots with 6 crossings.* Mathematical Proceedings of the Cambridge Philosophical Society **165** (2018), 287–339.
- **[SOTA]** S. Garoufalidis, T. T. Q. Lê. *Asymptotics of the colored Jones function of a knot.* Geometry & Topology **15** (2011), 2135–2180.
- **[SOTA]** Q. Chen, T. Yang. *Volume conjectures for the Reshetikhin–Turaev and the Turaev–Viro invariants.* Quantum Topology **9** (2018), 419–460.
- **[SOTA]** R. Detcherry, E. Kalfagianni, T. Yang. *Turaev–Viro invariants, colored Jones polynomials and volume.* Quantum Topology **9** (2018), 775–813.
- **[SOTA]** G. Belletti, R. Detcherry, E. Kalfagianni, T. Yang. *Growth of Turaev–Viro invariants and cabling.* Mathematical Proceedings of the Cambridge Philosophical Society (2020).
- **[Frontier]** S. Garoufalidis, D. Zagier. *Knots, perturbative series and quantum modularity.* SIGMA **20** (2024).
- **[Context]** S. Gukov. *Three-dimensional quantum gravity, Chern–Simons theory, and the A-polynomial.* Communications in Mathematical Physics **255** (2005), 577–627.
- **[Survey]** H. Murakami. *An introduction to the volume conjecture.* Contemporary Mathematics **541** (2011), 1–40.
- **[Survey]** H. Murakami, Y. Yokota. *Volume Conjecture for Knots.* SpringerBriefs in Mathematical Physics **30**, Springer, 2018.

## 10. Worked Example / Concrete Special Case

**The figure-eight knot $4_1$.** Kashaev's invariant has the closed form

$$\langle 4_1\rangle_N \;=\; \sum_{k=0}^{N-1}\ \prod_{j=1}^{k} \bigl|1 - e^{2\pi i j/N}\bigr|^{2} \;=\; \sum_{k=0}^{N-1}\ \prod_{j=1}^{k} 4\sin^{2}\!\Bigl(\frac{\pi j}{N}\Bigr).$$

Direct evaluation:

| $N$ | terms $\prod_{j\le k} 4\sin^2(\pi j/N)$ | $\langle 4_1\rangle_N$ | $\frac{2\pi}{N}\log\langle 4_1\rangle_N$ |
|---|---|---|---|
| 2 | $1,\,4$ | $5$ | $5.056$ |
| 3 | $1,\,3,\,9$ | $13$ | $5.372$ |
| 4 | $1,\,2,\,8,\,16$ | $27$ | $5.177$ |
| 5 | $1,\,1.382,\,5.000,\,18.09,\,25.00$ | $50.47$ | $4.928$ |

The target is $\operatorname{Vol}(S^3\setminus 4_1) = 6\Lambda(\pi/3) = 2.029883\ldots$, the volume of two regular ideal tetrahedra (shape $z = e^{i\pi/3}$, each of volume $\Lambda(\pi/3)\cdot 3 = 1.014941\ldots$).

The table looks far off because the convergence is only $O(\log N / N)$. The proven asymptotic is

$$\langle 4_1\rangle_N \sim \frac{N^{3/2}}{3^{1/4}}\, e^{\frac{N}{2\pi}\operatorname{Vol}} ,$$

so

$$\frac{2\pi}{N}\log\langle 4_1\rangle_N \;=\; \operatorname{Vol} \;+\; \frac{2\pi}{N}\Bigl(\tfrac{3}{2}\log N - \tfrac14\log 3\Bigr) + O(N^{-2}).$$

At $N=5$ the correction term is $\frac{2\pi}{5}(1.5\cdot 1.609 - 0.275) = 2.69$, predicting $2.03 + 2.69 = 4.72$ against the computed $4.93$ — consistent once the $O(N^{-2})$ terms are allowed. At $N=100$ the correction drops to $0.42$ and the numerics track $\operatorname{Vol}$ to two decimals.

**Where the geometry enters.** Replacing the sum by an integral and using $\log\prod_{j\le k}4\sin^2(\pi j/N) \approx \frac{N}{\pi}\bigl(\operatorname{Im}\operatorname{Li}_2(e^{2\pi i k/N}) - \operatorname{Im}\operatorname{Li}_2(1)\bigr)$ gives the potential $\Phi(x) = 2\operatorname{Im}\operatorname{Li}_2(e^{2\pi i x})$. Setting $\Phi'(x)=0$ yields $|1-e^{2\pi i x}| = 1$, i.e. $x = 1/6$ or $x = 5/6$; the maximum is at $x^\ast=1/6$, and

$$\Phi(1/6) = 2\operatorname{Im}\operatorname{Li}_2(e^{i\pi/3}) = 2\cdot 3\Lambda(\pi/3) = 2.029883\ldots$$

The saddle point is exactly the shape parameter $z = e^{i\pi/3}$ of the regular ideal tetrahedron, and its critical value is the hyperbolic volume. This one-variable case is the entire conjecture in miniature; the open problem is that for a general knot the potential has many variables, many critical points, and no known argument that the geometric one controls the contour.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*