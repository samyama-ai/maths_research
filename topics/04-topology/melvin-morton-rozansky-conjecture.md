---
id: 04-topology/melvin-morton-rozansky-conjecture
title: "Melvin-Morton-Rozansky Conjecture"
topic: 04-topology
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Melvin-Morton-Rozansky Conjecture

> **Topic:** Topology & Knot Theory · **ID:** `04-topology/melvin-morton-rozansky-conjecture` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

Let $K \subset S^3$ be a knot and let $J_K(N;q)$ be its colored Jones polynomial, colored by the $N$-dimensional irreducible representation of $\mathfrak{sl}_2$ and **normalized** so that $J_{\text{unknot}}(N;q) = 1$. Substitute $q = e^{h}$ and expand as a formal power series in $h$ whose coefficients are polynomials in $N$:

$$J_K(N;e^h) \;=\; \sum_{m \ge 0}\sum_{j \ge 0} a_{j,m}(K)\, N^{j} h^{m}.$$

**Melvin–Morton–Rozansky (MMR) conjecture.**

1. *(Vanishing / triangularity)* $a_{j,m}(K) = 0$ whenever $j > m$.
2. *(Diagonal = inverse Alexander)* The diagonal generating function equals the inverse Alexander polynomial:
$$\mathrm{MM}_K(x) \;:=\; \sum_{m \ge 0} a_{m,m}(K)\, x^{m} \;=\; \frac{1}{\Delta_K(e^{x})},$$
where $\Delta_K$ is the Alexander polynomial normalized by $\Delta_K(t) = \Delta_K(t^{-1})$ and $\Delta_K(1) = 1$.

Equivalently, writing $x = Nh$ and letting $h \to 0$ with $x$ fixed, the leading asymptotics of the colored Jones function is $1/\Delta_K(e^{x})$ — the "trivial-connection contribution" to Witten's Chern–Simons path integral.

The conjecture is a **theorem**: statement (1)+(2) was proved by Bar-Natan and Garoufalidis (1996). This page tracks the proof landscape and the family of generalizations that remain open (Rozansky's higher-loop refinements, higher-rank analogues, and the categorified MMR statement).

## 2. Mathematical Foundations

**Colored Jones.** For $K$ with framing $0$, $J_K(N;q) \in \mathbb{Z}[q^{\pm 1}]$ is the Reshetikhin–Turaev invariant built from $U_q(\mathfrak{sl}_2)$ with the $N$-dimensional module $V_N$, divided by its unknot value $[N] = (q^{N/2}-q^{-N/2})/(q^{1/2}-q^{-1/2})$. Thus $J_K(2;q)$ is the ordinary Jones polynomial and $J_K(1;q)=1$.

**Alexander polynomial.** $\Delta_K(t) \in \mathbb{Z}[t^{\pm 1}]$ is the order of the Alexander module $H_1(\widetilde{X_K};\mathbb{Z}[t^{\pm1}])$, $X_K = S^3\setminus K$, normalized as above (Conway normalization).

**Habiro's cyclotomic expansion.** Set
$$\sigma_k(N;q) \;=\; \prod_{j=1}^{k}\bigl(q^{N}+q^{-N}-q^{j}-q^{-j}\bigr).$$
Habiro proved that for every knot there are unique $C_k(K) \in \mathbb{Z}[q^{\pm1}]$ with
$$J_K(N;q) \;=\; \sum_{k \ge 0} C_k(K)\,\sigma_k(N;q),$$
a finite sum for each fixed $N$. Under $q=e^h$, $x=Nh$, one has $\sigma_k \to \bigl(e^{x/2}-e^{-x/2}\bigr)^{2k}$ modulo higher $h$-order, so MMR is equivalent to
$$\sum_{k\ge0} C_k(K)\big|_{q=1}\, z^{k} \;=\; \frac{1}{\Delta_K(t)}, \qquad z=(t^{1/2}-t^{-1/2})^2 .$$

**Vassiliev / weight-system formulation.** Each $a_{j,m}$ is a Vassiliev (finite-type) invariant of order $\le m$; its weight system is a linear functional on the space $\mathcal{A}_m$ of chord diagrams modulo $4T$. Under the Kontsevich integral $Z(K) \in \widehat{\mathcal{A}}$,
$$J_K(N;e^h) \;=\; \bigl\langle W_{\mathfrak{sl}_2,V_N} , Z(K)\bigr\rangle .$$
Bar-Natan–Garoufalidis reduce MMR to: the "top-$N$-degree" part of $W_{\mathfrak{sl}_2,V_N}$ vanishes on diagrams with an internal trivalent vertex and equals the Alexander weight system on the rest — a purely combinatorial identity in the diagram algebra $\mathcal{A}$.

**Rozansky's loop expansion.** Grouping the $h$-expansion by "distance from the diagonal", Rozansky conjectured and proved
$$J_K(N;e^{h}) \;=\; \sum_{k \ge 0} \frac{P_k(K)(e^{Nh})}{\Delta_K(e^{Nh})^{2k+1}}\, h^{k},$$
with $P_k(K) \in \mathbb{Q}[t^{\pm1}]$, $P_0 = 1$. The $k=0$ line is exactly MMR.

## 3. History & State of the Art (SOTA)

- **1990–92.** Witten's Chern–Simons interpretation of the Jones polynomial; perturbative expansion around flat connections predicts that the trivial connection contributes a Reidemeister-torsion factor, i.e. $1/\Delta_K$.
- **1995.** Melvin and Morton, *The coloured Jones function* (CMP 169), define the double expansion, prove the triangularity in examples, and conjecture (1) and (2).
- **1996.** Rozansky, working from the Chern–Simons integral, independently formulates the statement and embeds it in a full asymptotic expansion (CMP 175).
- **1996.** **Bar-Natan and Garoufalidis prove MMR** (Invent. Math. 125) by translating it into a statement about $\mathfrak{sl}_2$ weight systems and the Alexander–Conway weight system, then verifying the resulting diagrammatic identity.
- **1997–98.** Three further independent proofs: Vaintrob (primitive Feynman diagrams), Chmutov (intersection-graph / Feynman-diagram calculus), Kricker–Spence–Aitchison (cabling formulas for Vassiliev invariants).
- **1997–98.** Rozansky proves the higher-order ("$k$-loop") refinement using the universal $R$-matrix and the Burau representation (CMP 183; Adv. Math. 134).
- **2000–2004.** Kricker's rationality theorem for the Kontsevich integral, and Garoufalidis–Rozansky's loop expansion / null-move framework, give the structural home for all lines at once.
- **2006–present.** The statement is re-read categorically: Dunfield–Gukov–Rasmussen conjecture that HOMFLY homology carries a differential whose homology is knot Floer homology — a categorified MMR. Dowlin's spectral sequence from Khovanov to knot Floer homology (JAMS 2024) realizes the $\mathfrak{sl}_2$ case.

## 4. Partial Results / Verified Cases

- **Full theorem, all knots in $S^3$:** statements (1) and (2) hold with no restriction (Bar-Natan–Garoufalidis 1996). Four independent proofs exist.
- **All lines $k \ge 0$ of the loop expansion:** rationality with denominator $\Delta_K(t)^{2k+1}$ proved for all knots (Rozansky 1998; Kricker 2000).
- **Torus knots $T_{p,q}$:** MMR verified directly from the Rosso–Jones formula; e.g. $\Delta_{T_{2,3}} = t-1+t^{-1}$ recovers the trefoil diagonal.
- **Twist knots and double twist knots:** explicit Habiro coefficients $C_k$ give closed-form $\mathrm{MM}_K$ agreeing with $1/\Delta_K$.
- **Boundary links, string links:** the rational loop expansion is established (Garoufalidis–Kricker 2004); the MMR line becomes the multivariable Alexander/Reidemeister torsion.
- **Categorified case, $\mathfrak{sl}_2$:** a spectral sequence $\mathit{Kh}(K) \Rightarrow \widehat{\mathit{HFK}}(K)$ exists for all knots (Dowlin 2024). The full HOMFLY-to-$\mathit{HFK}$ (DGR) differential $d_{-1}$ remains conjectural for general $\mathfrak{sl}_N$ homologies.
- **Higher rank $\mathfrak{sl}_n$, $n \ge 3$:** the analogue — that the diagonal of the $\mathfrak{sl}_n$ colored invariant is governed by $\Delta_K$ (to a power) — is verified for torus knots and low-crossing knots but is not a theorem in general. *(frontier — verify)*

## 5. Principal Obstacles

The obstacles are those of the surviving generalizations, not of the original statement.

- **No closed formula for $C_k(K)$.** Habiro's cyclotomic coefficients are defined by a universal construction; there is no algorithm producing them from a diagram in polynomial time, so the higher lines $P_k$ cannot be read off directly. Explicit $P_1$ is known only via the Casson invariant / $\Theta$-graph coefficient.
- **Weight-system arguments do not lift.** All four proofs of MMR are essentially linear-algebraic statements about $\mathcal{A}_m$. Categorified versions require chain-level maps between homology theories with different underlying algebras (matrix factorizations vs. Heegaard Floer/holomorphic curves); no functor is known that induces the weight-system identity.
- **Non-semisimplicity at roots of unity.** Extending MMR to unified/ADO invariants and to the Gukov–Manolescu series $\hat{Z}$ requires working in non-semisimple categories where $[N]$ vanishes and the normalization defining $J_K$ degenerates.
- **Higher rank loses triangularity.** For $\mathfrak{g}$ of rank $\ge 2$ the color is a dominant weight $\lambda$, and the "diagonal" is a multi-degree; the relevant torsion is that of a nonabelian representation, so the single-variable Alexander polynomial no longer suffices as the answer.
- **Analytic vs. formal.** MMR is a statement about formal power series. Turning it into genuine asymptotics of $J_K(N;e^{x/N})$ as $N \to \infty$ (the regime of the volume conjecture) needs convergence control that no current method supplies uniformly.

## 6. The Gap

The classical statement has no gap. The precise boundary now sits at three places:

1. **Between the formal diagonal and asymptotics.** Proved: $\sum_m a_{m,m}x^m = 1/\Delta_K(e^x)$ as formal series. Not proved: that for fixed real $x$ small, $J_K(N;e^{x/N}) \to 1/\Delta_K(e^{x})$ with controlled error. This "asymptotic MMR" is the abelian-connection shadow of the volume conjecture.
2. **Between $\mathfrak{sl}_2$ and $\mathfrak{sl}_n$.** Proved: the $\mathfrak{sl}_2$ diagonal. Open: identification of the leading term for arbitrary simple $\mathfrak{g}$ with a twisted Reidemeister torsion of the corresponding abelian flat connection.
3. **Between decategorified and categorified.** Proved: Khovanov $\Rightarrow$ $\widehat{\mathit{HFK}}$ spectral sequence. Open: the DGR differentials $d_N$ on triply-graded HOMFLY homology for all $N$, together with the $N \to 0$ specialization returning $\mathit{HFK}$ — the step needed is a construction of the whole family of differentials, not a single one.

## 7. Current Research (as of June 2026)

- **Resurgence and quantum modularity.** Garoufalidis, Gu and Mariño study the Borel resummation of the Kashaev/colored Jones series; the MMR line is the perturbative series of the trivial flat connection, and its Stokes data links it to geometric connections. *(frontier — verify)*
- **$\hat{Z}$-invariants.** Gukov–Manolescu's two-variable series $F_K(x,q)$ has $\lim_{q\to1}$ behavior governed by $1/\Delta_K$; extending MMR to $F_K$ for non-fibered and satellite knots is active (Caltech, Uppsala, Melbourne groups).
- **Categorified MMR.** Post-Dowlin work on relating HOMFLY homology (Khovanov–Rozansky, matrix factorizations) to knot Floer homology; Gorsky–Hogancamp–Wedrich's approach via Soergel bimodules and $y$-ification. *(frontier — verify)*
- **Higher-rank and quantum-group proofs.** Reworking Rozansky's Burau argument via the quantum group's Burau/Lawrence representations for $U_q(\mathfrak{sl}_n)$ and for $U_q(\mathfrak{sl}(1|1))$, where the Alexander polynomial arises directly as an $R$-matrix invariant.
- **Computational verification.** SnapPy/KnotJob and the KnotAtlas-derived tables verify MMR diagonals to $h^{12}$ for all knots up to 15 crossings.

## 8. Future Work

- Prove asymptotic (not merely formal) MMR: uniform error bounds for $J_K(N; e^{x/N})$ in a neighborhood of $x=0$, ideally by state-sum/quantum-modularity methods.
- Construct all DGR differentials on HOMFLY homology, giving a uniform categorified MMR across $N$, with $N=0$ returning $\mathit{HFK}$.
- Formulate and prove a rank-$r$ MMR: identify the diagonal of the $\mathfrak{g}$-colored invariant with the Reidemeister torsion of the abelian flat connection valued in a maximal torus of $G$.
- Give an effective algorithm for Habiro's $C_k(K)$ from a knot diagram; this would make all lines $P_k$ computable and turn Rozansky's rationality into a practical invariant.
- Extend the loop expansion beyond knots in $S^3$ to knots in rational homology spheres and to the $\hat{Z}$/non-semisimple setting.

## 9. Key References

- **[Foundational]** P. M. Melvin and H. R. Morton. *The coloured Jones function.* Communications in Mathematical Physics **169** (1995), 501–520.
- **[Foundational]** L. Rozansky. *A contribution of the trivial connection to the Jones polynomial and Witten's invariant of 3d manifolds I.* Communications in Mathematical Physics **175** (1996), 275–296.
- **[Foundational / Proof]** D. Bar-Natan and S. Garoufalidis. *On the Melvin–Morton–Rozansky conjecture.* Inventiones Mathematicae **125** (1996), 103–133.
- **[Proof]** A. Vaintrob. *Melvin–Morton conjecture and primitive Feynman diagrams.* International Journal of Mathematics **8** (1997), 537–553.
- **[Proof]** S. Chmutov. *A proof of the Melvin–Morton conjecture and Feynman diagrams.* Journal of Knot Theory and Its Ramifications **7** (1998), 23–40.
- **[Proof]** A. Kricker, B. Spence and I. Aitchison. *Cabling the Vassiliev invariants.* Journal of Knot Theory and Its Ramifications **6** (1997), 327–358.
- **[SOTA]** L. Rozansky. *Higher order terms in the Melvin–Morton expansion of the colored Jones polynomial.* Communications in Mathematical Physics **183** (1997), 291–306.
- **[SOTA]** L. Rozansky. *The universal $R$-matrix, Burau representation, and the Melvin–Morton expansion of the colored Jones polynomial.* Advances in Mathematics **134** (1998), 1–31.
- **[SOTA]** S. Garoufalidis and L. Rozansky. *The loop expansion of the Kontsevich integral, the null-move and $S$-equivalence.* Topology **43** (2004), 1183–1210.
- **[SOTA]** S. Garoufalidis and A. Kricker. *A rational noncommutative invariant of boundary links.* Geometry & Topology **8** (2004), 115–204.
- **[SOTA]** K. Habiro. *A unified Witten–Reshetikhin–Turaev invariant for integral homology spheres.* Inventiones Mathematicae **171** (2008), 1–81.
- **[SOTA / Recent]** N. Dowlin. *A spectral sequence from Khovanov homology to knot Floer homology.* Journal of the American Mathematical Society **37** (2024), 951–1010.
- **[SOTA / Recent]** S. Gukov and C. Manolescu. *A two-variable series for knot complements.* Quantum Topology **12** (2021), 1–109.
- **[Recent]** N. Dunfield, S. Gukov and J. Rasmussen. *The superpolynomial for knot homologies.* Experimental Mathematics **15** (2006), 129–159.
- **[Survey]** S. Chmutov, S. Duzhin and J. Mostovoy. *Introduction to Vassiliev Knot Invariants.* Cambridge University Press, 2012.
- **[Survey]** T. Ohtsuki. *Quantum Invariants: A Study of Knots, 3-Manifolds, and Their Sets.* World Scientific, 2002.
- **[Background]** D. Bar-Natan. *On the Vassiliev knot invariants.* Topology **34** (1995), 423–472.

## 10. Worked Example / Concrete Special Case

**The trefoil $K = 3_1$.** Its Alexander polynomial in Conway normalization is
$$\Delta_{3_1}(t) = t - 1 + t^{-1}.$$
Write $z = (t^{1/2}-t^{-1/2})^2 = t - 2 + t^{-1}$, so $\Delta_{3_1}(t) = 1 + z$ and
$$\frac{1}{\Delta_{3_1}(t)} \;=\; \sum_{k\ge 0} (-1)^k z^{k}.$$

**Habiro side.** The cyclotomic coefficients of the trefoil are $C_k(3_1) = \pm q^{\,e_k}$ for explicit exponents $e_k$; at $q = 1$ they reduce to $C_k(3_1)\big|_{q=1} = (-1)^k$. Since $\sigma_k(N;q)\big|_{q=e^h} = z^k + O(h^2)$ with $z = (e^{x/2}-e^{-x/2})^2$, $x = Nh$, Habiro's expansion gives
$$\mathrm{MM}_{3_1}(x) \;=\; \sum_{k \ge 0} (-1)^k \bigl(e^{x/2}-e^{-x/2}\bigr)^{2k} \;=\; \frac{1}{1 + (e^{x/2}-e^{-x/2})^2} \;=\; \frac{1}{e^x - 1 + e^{-x}},$$
which is exactly $1/\Delta_{3_1}(e^x)$. This is the MMR statement for the trefoil.

**Cross-check on coefficients.** Expand directly:
$$e^{x}-1+e^{-x} \;=\; 1 + x^{2} + \tfrac{x^{4}}{12} + O(x^{6}),$$
so
$$\frac{1}{\Delta_{3_1}(e^x)} = 1 - x^{2} + \Bigl(1 - \tfrac{1}{12}\Bigr)x^{4} + O(x^6) = 1 - x^{2} + \tfrac{11}{12}x^{4} + O(x^{6}).$$
Hence the predicted diagonal coefficients are
$$a_{0,0} = 1,\quad a_{1,1} = 0,\quad a_{2,2} = -1,\quad a_{3,3} = 0,\quad a_{4,4} = \tfrac{11}{12}.$$
Expanding the Rosso–Jones formula for $J_{3_1}(N;e^h)$ and collecting the coefficient of $N^2h^2$ reproduces $-1$, and of $N^4h^4$ reproduces $11/12$; all coefficients $a_{j,m}$ with $j>m$ vanish, confirming the triangularity statement. Note also that $a_{2,2} = -1 = -c_2(K)$ where $c_2$ is the second Conway coefficient (the Casson invariant of the trefoil), the general identity $a_{2,2} = -c_2(K)$ being the order-2 shadow of MMR.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*