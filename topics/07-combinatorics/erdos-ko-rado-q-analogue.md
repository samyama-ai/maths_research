---
id: 07-combinatorics/erdos-ko-rado-q-analogue
title: "Erdős-Ko-Rado Theorem q-analogue"
topic: 07-combinatorics
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Erdős-Ko-Rado Theorem q-analogue

> **Topic:** Combinatorics & Graph Theory · **ID:** `07-combinatorics/erdos-ko-rado-q-analogue` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

Replace "$k$-subset of an $n$-set" by "$k$-dimensional subspace of $\mathbb{F}_q^n$" and ask for the largest family of subspaces that pairwise intersect nontrivially.

**Core statement (proved).** Let $q$ be a prime power, $n \ge 2k$, and let $\mathcal{F}$ be a family of $k$-subspaces of $V = \mathbb{F}_q^n$ with $\dim(A \cap B) \ge 1$ for all $A, B \in \mathcal{F}$. Then
$$|\mathcal{F}| \;\le\; \begin{bmatrix} n-1 \\ k-1 \end{bmatrix}_q ,$$
with equality (for $n > 2k$) only for the *point-pencil* $\{A : p \subseteq A\}$ for a fixed $1$-space $p$. For $n = 2k$ the dual family $\{A : A \subseteq H\}$, $H$ a fixed $(n-1)$-space, is equally large.

**$t$-intersecting version (proved).** For $\dim(A\cap B)\ge t$ and $n \ge 2k-t$,
$$|\mathcal{F}| \;\le\; \max\left\{ \begin{bmatrix} n-t \\ k-t \end{bmatrix}_q, \; \begin{bmatrix} 2k-t \\ k \end{bmatrix}_q \right\}.$$

The theorem itself is settled (Hsieh 1975; Frankl–Wilson 1986). What remains open is the surrounding programme: which *other* intersection theorems for sets admit $q$-analogues, and at what parameters. The live open cases are (i) the $q$-analogue of the Erdős matching conjecture (families with no $s+1$ pairwise trivially-intersecting members), (ii) exact chromatic numbers and Hilton–Milner-type stability for small $k$ relative to $q$, (iii) EKR for all finite classical polar spaces, and (iv) forbidden-intersection ($q$-Frankl–Rödl) problems. A resolution means exact extremal numbers plus classification of extremal families, valid for all prime powers $q$, not merely $q$ large.

## 2. Mathematical Foundations

**Gaussian binomial coefficient.** The number of $k$-subspaces of $\mathbb{F}_q^n$ is
$$\begin{bmatrix} n \\ k \end{bmatrix}_q = \prod_{i=0}^{k-1} \frac{q^{n-i}-1}{q^{k-i}-1}, \qquad \lim_{q\to 1}\begin{bmatrix} n \\ k \end{bmatrix}_q = \binom{n}{k}.$$
The subspace lattice thus $q$-deforms the Boolean lattice; the $q \to 1$ limit recovers the classical EKR statement.

**$q$-Kneser graph.** $qK_{n:k}$ has as vertices the $k$-subspaces of $\mathbb{F}_q^n$, adjacent when they meet trivially. It is regular of degree
$$d = q^{k^2}\begin{bmatrix} n-k \\ k \end{bmatrix}_q,$$
and an intersecting family is exactly an independent set, so the EKR problem is the computation of $\alpha(qK_{n:k})$.

**Grassmann scheme.** The $k$-subspaces of $\mathbb{F}_q^n$ carry the association scheme $J_q(n,k)$ with relations $R_i = \{(A,B) : \dim(A\cap B) = k-i\}$, $0 \le i \le k$. Its eigenvalues are $q$-Eberlein polynomials; for $n\ge 2k$ the least eigenvalue of $qK_{n:k}$ is
$$\lambda_{\min} = -\,q^{k^2-k}\begin{bmatrix} n-k-1 \\ k-1 \end{bmatrix}_q .$$

**Delsarte–Hoffman ratio bound.** For a $d$-regular graph $G$ on $N$ vertices with least eigenvalue $\lambda_{\min} < 0$,
$$\alpha(G) \le N\,\frac{-\lambda_{\min}}{d - \lambda_{\min}},$$
with equality forcing the characteristic vector of a maximum independent set to lie in the span of the trivial and $\lambda_{\min}$-eigenspaces. Substituting the values above yields exactly $\begin{bmatrix} n-1 \\ k-1 \end{bmatrix}_q$ — the algebraic proof of the $q$-EKR theorem.

**Hilton–Milner $q$-analogue.** For $n \ge 2k+1$, $k \ge 3$, a maximal intersecting family with $\bigcap_{A\in\mathcal{F}} A = 0$ satisfies
$$|\mathcal{F}| \le \begin{bmatrix} n-1 \\ k-1 \end{bmatrix}_q - q^{k(k-1)}\begin{bmatrix} n-k-1 \\ k-1 \end{bmatrix}_q + q^k .$$
For $k = 2$ the extremal nontrivial family is instead all lines of a fixed plane, of size $q^2+q+1$.

## 3. History & State of the Art (SOTA)

- **1961** — Erdős, Ko and Rado publish the set version (written 1938), giving $\binom{n-1}{k-1}$ for $n \ge 2k$.
- **1975** — W. N. Hsieh proves the $q$-analogue for $n \ge 2k+1$ (and $t$-intersecting cases for $n$ large), by a $q$-shifting/compression argument.
- **1986** — Frankl and Wilson give the complete $t$-intersecting theorem for all $n \ge 2k-t$, including the delicate boundary case $n = 2k$. Crucially, the $q$-world has only **two** candidate optima; the intermediate Frankl families that make the set problem require the Ahlswede–Khachatrian complete intersection theorem (1997) are never optimal for $q \ge 2$.
- **2006** — Godsil–Newman give the clean ratio-bound proof and the $n=2k$ uniqueness; Tanaka classifies all extremal families via width/dual-width in the Grassmann scheme, obtaining uniqueness for the $t$-intersecting case.
- **2010** — Blokhuis, Brouwer, Chowdhury, Frankl, Mussche, Patkós and Szőnyi prove the Hilton–Milner $q$-analogue.
- **2011–2013** — Pepe–Storme–Vanhove and Blokhuis–Brouwer–Szőnyi extend to polar spaces and settle $\chi(qK_{n:k})$ for $n \ge 2k$ (value $q^{n-k+1}-1$ over $q-1$ scale; for $n=2k$ the answer is $q^k + q^{k-1}$).
- **2017–2024** — hypercontractivity for global functions (Keller–Lifshitz–Minzer; Ellis–Kindler–Lifshitz) yields junta approximation and forbidden-intersection results in the linear-algebraic setting, replacing shifting entirely.

## 4. Partial Results / Verified Cases

| Regime | Status |
|---|---|
| $t=1$, $n \ge 2k$, all $q$ | **Solved** (Hsieh; Frankl–Wilson; Godsil–Newman). Extremal families classified. |
| $t \ge 2$, $n \ge 2k-t$, all $q$ | **Solved** (Frankl–Wilson); uniqueness by Tanaka (2006). |
| $n < 2k-t$ | Trivial: any two $k$-spaces meet in dimension $\ge 2k-n > t$. |
| Nontrivial intersecting, $n\ge 2k+1$, $k\ge3$ | **Solved** (Blokhuis et al. 2010). $k=2$ handled separately. |
| Chromatic number $\chi(qK_{n:k})$, $n \ge 2k$ | **Solved** for $n>2k$ and, after Blokhuis–Brouwer–Szőnyi (2013), for $n=2k$. |
| Polar spaces: $Q^+(4n+1,q)$, $H(2d+1,q^2)$, $W(2d-1,q)$ generators | Solved in most types (Pepe–Storme–Vanhove 2011; Ihringer–Metsch 2014); a few small-rank/characteristic cases remain. |
| $q$-Erdős matching conjecture ($s\ge2$) | Known only for $n$ large relative to $k,s$; exact threshold open. |
| Forbidden intersections ($\dim(A\cap B)\ne t$) | Solved for $n \ge Ck$ with $C$ absolute (junta method); small $n/k$ open. |

Computationally, $\alpha(qK_{n:k})$ has been confirmed by exhaustive/clique search for $q\le 4$ and $n\le 8$, $k \le 3$, matching the formula in every case.

## 5. Principal Obstacles

- **Shifting has no $q$-analogue.** The compression operator $S_{ij}$ that drives most set-system proofs replaces element $j$ by $i$; there is no subspace analogue because the subspace lattice is not a product of chains and its automorphism group $\mathrm{P\Gamma L}(n,q)$ is far smaller and $2$-transitive only on points. Every $q$-proof must be spectral, geometric, or analytic.
- **No topological method.** Lovász's proof of Kneser's conjecture uses the Borsuk–Ulam theorem on $S^{n}$; the $q$-Kneser graph has no comparable topological model, so its chromatic number required hard finite-geometry input (blocking sets, Beutelspacher-type results on maximal partial spreads).
- **Ratio bound is tight only at the extreme.** The Delsarte–Hoffman bound is exact for $t=1$, $n\ge 2k$, but for $t\ge 2$ and small $n-2k$ the relevant eigenvalue interlacing loses a constant factor; refined semidefinite (Terwilliger algebra) relaxations are needed and are not yet exactly solvable in general.
- **Uniform-in-$q$ statements.** Many modern analytic tools (junta approximation, global hypercontractivity) carry error terms that blow up as $q \to \infty$ or require $n \ge Ck$ with $C$ non-explicit, so they cannot reach the sharp thresholds $n = 2k$ or $n=2k-t$.
- **Matchings resist eigenvalues.** For the $q$-Erdős matching conjecture there is no single graph whose independence number encodes the problem; the corresponding hypergraph relaxation has an integrality gap.

## 6. The Gap

The classical EKR $q$-analogue is closed. The gap now lies one level up: for every intersection theorem beyond the basic and $t$-intersecting cases, the proven range is $n \ge C(k,s)$ with $C$ either non-explicit or far above the conjectured threshold, while the conjectured statement holds down to $n \approx (s+1)k$ or $n = 2k$. Concretely, for the $q$-Erdős matching conjecture one wants: a family of $k$-spaces in $\mathbb{F}_q^n$ with no $s+1$ pairwise trivially-intersecting members has size at most
$$\max\left\{ \begin{bmatrix} (s+1)k-1 \\ k \end{bmatrix}_q,\; \begin{bmatrix} n \\ k \end{bmatrix}_q - \begin{bmatrix} n-s \\ k \end{bmatrix}_q \right\},$$
and the exact step to be crossed is a stability/junta argument whose error term is uniform in $q$ and valid at $n = (s+1)k$ rather than $n \gg k$.

## 7. Current Research (as of June 2026)

- **Global hypercontractivity school** (Keller, Lifshitz, Minzer, Ellis, Kindler; Bar-Ilan, Hebrew University, Cambridge). Replaces shifting by junta approximation for "global" functions on $\mathrm{Gr}_q(n,k)$ and on spaces of linear maps; has already delivered $q$-analogues of Frankl–Rödl forbidden intersections and simplex-type theorems. *(frontier — verify: extension of the method down to $n = 2k+O(1)$ uniformly in $q$.)*
- **Finite-geometry school** (Storme, Metsch, Ihringer, Blokhuis, Szőnyi; Ghent, Giessen, Budapest). Pushes EKR into polar and dual polar spaces, attenuated spaces, and $q$-analogues of designs; the remaining polar-space cases are small rank with $q$ even.
- **Algebraic combinatorics / association schemes** (Godsil, Meagher, Tanaka; Waterloo, Regina, Tohoku). Terwilliger-algebra SDP hierarchies to sharpen the ratio bound for $t\ge2$ and for non-uniform (Boolean-lattice-analogue) versions.
- **Spread and matching problems.** Ongoing work on $q$-analogues of the Erdős matching conjecture and of Kneser hypergraph colourings, driven by progress in subspace designs and $q$-Steiner systems.

## 8. Future Work

1. Prove the $q$-Erdős matching conjecture at the natural threshold $n=(s+1)k$, at least for $s=2$.
2. Obtain a *uniform-in-$q$* junta theorem: every intersecting family of $k$-spaces is contained in a union of $O(1)$ point-pencils up to $\varepsilon\binom{n-1}{k-1}_q$ error, with $\varepsilon$ independent of $q$.
3. Close the remaining EKR cases for finite classical polar spaces of small rank.
4. Determine sharp Hilton–Milner-type stability for $n=2k$, where two extremal families coexist and the standard stability machinery degenerates.
5. Develop a genuine $q$-analogue of the Borsuk–Ulam argument, or prove that none exists, for $q$-Kneser hypergraph chromatic numbers.

## 9. Key References

- **[Foundational]** P. Erdős, C. Ko, R. Rado. *Intersection theorems for systems of finite sets.* Quarterly Journal of Mathematics (Oxford), 12 (1961), 313–320.
- **[Foundational]** W. N. Hsieh. *Intersection theorems for systems of finite vector spaces.* Discrete Mathematics, 12 (1975), 1–16.
- **[Foundational]** P. Frankl, R. M. Wilson. *The Erdős–Ko–Rado theorem for vector spaces.* Journal of Combinatorial Theory Series A, 43 (1986), 228–236.
- **[SOTA]** C. Godsil, M. Newman. *Independent sets in association schemes.* Combinatorica, 26 (2006), 431–443.
- **[SOTA]** H. Tanaka. *Classification of subsets with minimal width and dual width in Grassmann, bilinear forms and dual polar graphs.* Journal of Combinatorial Theory Series A, 113 (2006), 903–910.
- **[SOTA]** A. Blokhuis, A. E. Brouwer, A. Chowdhury, P. Frankl, T. Mussche, B. Patkós, T. Szőnyi. *A Hilton–Milner theorem for vector spaces.* Electronic Journal of Combinatorics, 17 (2010), \#R71.
- **[SOTA]** A. Blokhuis, A. E. Brouwer, T. Szőnyi. *On the chromatic number of $q$-Kneser graphs.* Designs, Codes and Cryptography, 65 (2013), 187–197.
- **[SOTA]** V. Pepe, L. Storme, F. Vanhove. *Theorems of Erdős–Ko–Rado type in polar spaces.* Journal of Combinatorial Theory Series A, 118 (2011), 1291–1312.
- **[SOTA]** F. Ihringer, K. Metsch. *On the maximum size of Erdős–Ko–Rado sets in $H(2d+1,q^2)$.* Designs, Codes and Cryptography, 72 (2014), 311–316.
- **[SOTA]** N. Keller, N. Lifshitz. *The junta method for hypergraphs and the Erdős–Chvátal simplex conjecture.* Advances in Mathematics, 392 (2021), 107991.
- **[Related]** R. Ahlswede, L. H. Khachatrian. *The complete intersection theorem for systems of finite sets.* European Journal of Combinatorics, 18 (1997), 125–136.
- **[Survey]** C. Godsil, K. Meagher. *Erdős–Ko–Rado Theorems: Algebraic Approaches.* Cambridge University Press, 2016.
- **[Survey]** P. Frankl, N. Tokushige. *Invitation to intersection problems for finite sets.* Journal of Combinatorial Theory Series A, 144 (2016), 157–211.

## 10. Worked Example / Concrete Special Case

Take $q=2$, $n=4$, $k=2$: lines of $\mathrm{PG}(3,2)$, i.e. $2$-subspaces of $\mathbb{F}_2^4$.

**Count the ground set.**
$$\begin{bmatrix}4\\2\end{bmatrix}_2 = \frac{(2^4-1)(2^3-1)}{(2^2-1)(2^1-1)} = \frac{15\cdot 7}{3\cdot 1} = 35 .$$

**Degree of $2K_{4:2}$.** The number of $2$-spaces meeting a fixed $2$-space $A$ trivially is
$$q^{k^2}\begin{bmatrix}n-k\\k\end{bmatrix}_q = 2^{4}\begin{bmatrix}2\\2\end{bmatrix}_2 = 16\cdot 1 = 16 .$$
So $2K_{4:2}$ is a $16$-regular graph on $35$ vertices (each line of $\mathrm{PG}(3,2)$ has exactly $16$ skew partners).

**Least eigenvalue.**
$$\lambda_{\min} = -q^{k^2-k}\begin{bmatrix}n-k-1\\k-1\end{bmatrix}_q = -2^{2}\begin{bmatrix}1\\1\end{bmatrix}_2 = -4 .$$

**Ratio bound.**
$$\alpha(2K_{4:2}) \le 35\cdot\frac{4}{16+4} = \frac{140}{20} = 7 .$$

**Matching construction.** Two families attain $7$:
- Point-pencil: fix a $1$-space $p$; the $2$-spaces containing $p$ number $\begin{bmatrix}3\\1\end{bmatrix}_2 = 7$. Any two share $p$.
- Dual (plane) family: fix a $3$-space $H$; the $2$-spaces inside $H$ number $\begin{bmatrix}3\\2\end{bmatrix}_2 = 7$, and two $2$-spaces in a $3$-space meet in dimension $\ge 2+2-3 = 1$.

So $\alpha(2K_{4:2}) = 7 = \begin{bmatrix}3\\1\end{bmatrix}_2$, the bound is tight, and because $n = 2k$ the extremal family is **not** unique — exactly the phenomenon Godsil–Newman and Tanaka had to classify. Compare $q\to1$: $\binom{4-1}{2-1} = 3$, the classical answer for $2$-subsets of a $4$-set, likewise attained by both a star and the triangle $\{12,13,23\}$.

For contrast, at $n=5$, $k=2$, $q=2$ the point-pencil has $\begin{bmatrix}4\\1\end{bmatrix}_2 = 15$ members, while the best nontrivial family — all lines of a fixed plane — has only $q^2+q+1 = 7$, matching the $k=2$ Hilton–Milner exception.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*