---
id: 07-combinatorics/masons-conjectures
title: "Mason's Conjectures"
topic: 07-combinatorics
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Mason's Conjectures

> **Topic:** Combinatorics & Graph Theory · **ID:** `07-combinatorics/masons-conjectures` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

Let $M$ be a matroid on a finite ground set $E$ with $|E| = n$ and rank $r$. Let
$$I_k = I_k(M) = \\#\{S \subseteq E : S \text{ independent in } M,\ |S| = k\},$$
so $I_0 = 1$, $I_1 = n$ minus the number of loops, and $I_k = 0$ for $k > r$. The sequence $(I_0, I_1, \dots, I_r)$ is the $f$-vector of the independence complex of $M$.

In 1972 John H. Mason proposed three successively stronger inequalities, for all $1 \le k \le r-1$:

- **(M1) Log-concavity.** $\;I_k^2 \ge I_{k-1} I_{k+1}$.
- **(M2) Strong log-concavity.** $\;I_k^2 \ge \dfrac{k+1}{k}\, I_{k-1} I_{k+1}$.
- **(M3) Ultra log-concavity.** $\;I_k^2 \ge \dfrac{k+1}{k}\cdot\dfrac{n-k+1}{n-k}\, I_{k-1} I_{k+1}$.

Since $\frac{k+1}{k} > 1$ and $\frac{n-k+1}{n-k} > 1$, one has (M3) $\Rightarrow$ (M2) $\Rightarrow$ (M1). Statement (M3) is equivalent to saying that the normalized sequence $\bigl(I_k / \binom{n}{k}\bigr)_{k=0}^{n}$ is log-concave — the "ultra" terminology of Pemantle and Liggett.

A complete resolution requires proof (or a counterexample) for **all** matroids, including non-representable ones such as the Vámos matroid $V_8$ and the $2^{2^{\Theta(n)}}$ matroids that are representable over no field. All three statements are now **theorems**; the page is retained because the surrounding program (equality cases, matroid intersection, Stanley's $h$-vector conjecture) remains open.

## 2. Mathematical Foundations

**Matroid.** A pair $M = (E, \mathcal{I})$ with $\mathcal{I} \subseteq 2^E$ nonempty, downward closed, and satisfying the exchange axiom: if $A, B \in \mathcal{I}$ with $|A| < |B|$ then $A \cup \{b\} \in \mathcal{I}$ for some $b \in B \setminus A$. The rank function is $\mathrm{rk}(S) = \max\{|A| : A \subseteq S,\ A \in \mathcal{I}\}$ and $r = \mathrm{rk}(E)$.

**Independence generating polynomials.** Two objects carry the conjectures:
$$g_M(x_1,\dots,x_n) \;=\; \sum_{S \in \mathcal{I}} \prod_{i \in S} x_i, \qquad
h_M(x,y) \;=\; \sum_{k=0}^{r} I_k\, x^k y^{\,r-k}.$$

**Log-concavity notions.** A sequence $(a_k)_{k\ge0}$ of nonnegative reals with no internal zeros is *log-concave* if $a_k^2 \ge a_{k-1}a_{k+1}$, and *ultra log-concave of order $n$* (written $\mathrm{ULC}(n)$) if $\bigl(a_k/\binom{n}{k}\bigr)_k$ is log-concave. Expanding the binomials, $\mathrm{ULC}(n)$ is exactly (M3).

**Complete log-concavity (Anari–Liu–Oveis Gharan–Vinzant).** A polynomial $p \in \mathbb{R}_{\ge 0}[x_1,\dots,x_n]$ is *completely log-concave* if for every $m \ge 0$ and every matrix $A \in \mathbb{R}_{\ge0}^{m \times n}$, the polynomial $\bigl(\prod_{i=1}^m \sum_j A_{ij}\partial_{x_j}\bigr) p$ is identically zero or log-concave as a function on $\mathbb{R}_{>0}^n$.

**Lorentzian polynomials (Brändén–Huh).** A homogeneous $f$ of degree $d$ with nonnegative coefficients is *Lorentzian* if its support is $M$-convex (the set of exponent vectors is the set of bases of a discrete polymatroid) and every $(d-2)$-fold partial derivative $\partial^\alpha f$, $|\alpha| = d-2$, is a quadratic form whose Hessian has at most one positive eigenvalue — i.e. signature $(+,-,\dots,-)$ or degenerate. Two facts drive the proofs:

1. **Bivariate criterion.** $f(x,y) = \sum_{k=0}^{d} c_k \binom{d}{k} x^k y^{d-k}$ is Lorentzian if and only if $(c_k)$ is log-concave with no internal zeros.
2. **Closure.** The Lorentzian class is closed under $\partial_{x_i}$, under linear maps with nonnegative coefficients, and under the normalization operator $N\bigl(\sum c_\alpha x^\alpha\bigr) = \sum c_\alpha x^\alpha/\alpha!$ relating multiaffine and homogeneous pictures.

**Theorem (Brändén–Huh 2020; ALOV 2018/2024).** For every matroid $M$, the homogenization of $g_M$ is Lorentzian / $g_M$ is completely log-concave. Consequently $(I_k)_{k}$ is $\mathrm{ULC}(n)$, proving (M3), hence (M2) and (M1).

The earlier, weaker chain runs through the **Heron–Rota–Welsh conjecture**: if $\chi_M(q) = \sum_{i=0}^{r}(-1)^i w_i q^{r-i}$ is the characteristic polynomial, the $|w_i|$ are log-concave — proved by Adiprasito–Huh–Katz via a Hodge theory (hard Lefschetz + Hodge–Riemann relations) for the Chow ring $A^\bullet(M)$ of the Bergman fan.

## 3. History & State of the Art (SOTA)

- **1972.** Mason states the three conjectures in *Matroids: unimodal conjectures and Motzkin's problem* (Combinatorics, Oxford conference proceedings). Welsh's *Matroid Theory* (1976) records them alongside Rota's and Heron's log-concavity conjectures for Whitney numbers.
- **1980s.** Only fragmentary progress: Mahoney (1985) verifies unimodality for a class of matroids arising from outerplanar graphs; Hamidoune and Salaün (1989) prove unimodality of $(I_k)$ for all matroids of rank $\le 7$.
- **2012–2015.** Huh and Katz prove log-concavity of $|w_i|$ for realizable matroids using intersection theory on the Chow variety; Lenz (2013) shows this implies **(M1) for representable matroids** through a purely combinatorial deduction from the $h$-vector.
- **2018.** Adiprasito, Huh and Katz prove Heron–Rota–Welsh for **all** matroids (Annals of Math. 188). Combined with Lenz's argument this settles **(M1) unconditionally**.
- **2018–2020.** ALOV prove (M3) via completely log-concave polynomials; independently Brändén and Huh prove (M3) via Lorentzian polynomials (Annals of Math. 192, 2020). Huh, Schröter and Wang (JEMS 2022) give a separate proof of **(M2)** through correlation bounds ($\mathrm{Cov}$-type inequalities for matroids and fields).
- **2022–2024.** Chan and Pak's "combinatorial atlas" supplies an elementary linear-algebraic proof of Heron–Rota–Welsh, removing Hodge theory from that half of the story. Berget, Eur, Spink and Tseng (Invent. Math. 2023) rederive the independent-set inequalities from tautological Chern classes of matroids.

**SOTA:** all three conjectures are theorems. The frontier has moved to equality characterizations, multivariate/correlation strengthenings, and analogues for matroid intersection and for $h$-vectors.

## 4. Partial Results / Verified Cases

Historically established special cases, now subsumed but still the sharpest elementary arguments:

- **Rank $r \le 2$:** (M3) is provable by hand (Section 10).
- **Rank $r \le 7$:** unimodality of $(I_k)$ — Hamidoune–Salaün (1989).
- **Uniform matroids $U_{r,n}$:** $I_k = \binom{n}{k}$ for $k \le r$, so $I_k/\binom{n}{k} = 1$ for $k \le r$ and $0$ after; (M3) holds with **equality** for $1 \le k \le r-1$. This shows the constant $\frac{k+1}{k}\cdot\frac{n-k+1}{n-k}$ cannot be improved.
- **Representable matroids over any field:** (M1) by Lenz (2013) building on Huh–Katz; the $h$-vector log-concavity of Huh (2015) covers the same class.
- **Graphic matroids:** covered by representability over every field; $I_k$ counts spanning forests with $k$ edges, so (M3) is a statement about forest counts in any graph.
- **Transversal / cotransversal matroids:** independently accessible via Stanley-type results on $h$-vectors.
- **All matroids, $n$ arbitrary:** (M1) since 2018, (M2) since 2019 (Huh–Schröter–Wang), (M3) since 2020 (Brändén–Huh; ALOV).
- **Still open sub-cases:** the analogue of (M1) for the common independent sets of **two** matroids, and Stanley's conjecture that the $h$-vector of a matroid complex is a pure $O$-sequence (proved for cotransversal and for rank $\le 3$ classes only).

## 5. Principal Obstacles

- **No representability to lean on.** Almost all matroids are non-representable (Nelson, 2018), so algebraic-geometry arguments that produce a variety with an ample class — Huh–Katz's original route — cover a vanishing fraction of instances. The obstruction is not technical: there is no scheme whose intersection numbers are the $I_k$ of the Vámos matroid.
- **Failure of injections.** Log-concavity $I_k^2 \ge I_{k-1}I_{k+1}$ asks for an injection $\mathcal{I}_{k-1}\times\mathcal{I}_{k+1} \hookrightarrow \mathcal{I}_k \times \mathcal{I}_k$. Exchange gives local moves but no canonical global matching; no such injection is known even now, and (M3)'s extra factor is not an integer ratio, so no injective proof can be direct.
- **Real-rootedness is false.** The natural strengthening — that $\sum_k I_k x^k$ has only real roots — fails; the Fano matroid and small rank-3 examples give complex roots. So Newton's inequalities are unavailable and one must work with the strictly weaker Lorentzian/Hodge-theoretic condition.
- **Hodge theory had to be built, not borrowed.** AHK could not import hard Lefschetz from Kähler geometry; they proved it for $A^\bullet(M)$ by an induction on matroid flips, with the Hodge–Riemann relations of signature $(+,-,\dots,-)$ as the load-bearing statement. Standard algebraic topology gives no Poincaré duality for the Bergman fan a priori.
- **Two-matroid intersection breaks the method.** The polynomial $\sum_{S \in \mathcal{I}_1 \cap \mathcal{I}_2} \prod_{i\in S} x_i$ is generally **not** Lorentzian, since its support is not $M$-convex. Every current technique consumes $M$-convexity as an input.

## 6. The Gap

For Mason's three inequalities the gap is closed: Sections 4 and 1 coincide. The residual boundary is threefold.

1. **Equality classification.** (M3) is tight for $U_{r,n}$ and for Boolean matroids. A full description of the matroids attaining equality at some $k$ — conjecturally exactly those whose truncation is uniform — is not written down in complete generality.
2. **Intersection analogue.** Prove or refute: for matroids $M_1, M_2$ on $E$, the numbers $J_k = \\#\{S : |S| = k,\ S \in \mathcal{I}(M_1)\cap\mathcal{I}(M_2)\}$ are log-concave. The missing step is a substitute for $M$-convexity of the support, which is exactly what intersection destroys.
3. **Stanley's $h$-vector conjecture.** Log-concavity of the $h$-vector of a matroid complex is implied by the above machinery; purity as an $O$-sequence is not, because it is a monomial-ideal statement with no known polynomial-positivity certificate.

## 7. Current Research (as of June 2026)

- **Lorentzian/negative-dependence school** (Brändén, Huh, Leake, and the Berkeley–Princeton–IAS orbit): classifying Lorentzian polynomials beyond matroids, and extending to polymatroids and valuated matroids.
- **Markov-chain consequences** (Anari, Oveis Gharan, Vinzant, Liu, Cryan–Guo–Mousa): complete log-concavity yields a mixing-time bound of $O(r \log n)$ for the bases-exchange walk, giving an FPRAS for counting bases of a matroid. This application, not the inequality, drives most current activity.
- **Combinatorial atlas** (Chan, Pak): elementary hyperbolic-matrix framework reproving Heron–Rota–Welsh and giving equality conditions; extension to independence numbers and to poset inequalities is active *(frontier — verify)*.
- **Tautological matroid classes** (Berget, Eur, Spink, Tseng; Eur, Huh, Larson): $K$-theoretic and Chow-theoretic invariants that recover Mason's inequalities and predict new ones, e.g. for the Tutte polynomial and Merino–Welsh.
- **Intersection and correlation** (Huh, Schröter, Wang; Bérczi–Schwartz): correlation bounds for two matroids as an approach to item 2 of Section 6 *(frontier — verify)*.

## 8. Future Work

- Prove or disprove log-concavity of $(J_k)$ for two-matroid intersection; a counterexample is plausible and would sharpen the role of $M$-convexity.
- Give a fully bijective/injective proof of (M1) for graphic matroids — a forest-counting injection would be the first combinatorial certificate.
- Settle Stanley's $h$-vector conjecture, and the Merino–Welsh conjecture $\max\{T_M(2,0), T_M(0,2)\} \ge T_M(1,1)$ for graphic matroids, using Lorentzian methods.
- Extract effective *strict* forms: quantify the gap in (M3) in terms of connectivity or the number of parallel classes.
- Develop a Hodge theory for the intersection lattice of two matroids, or prove that none can exist.

## 9. Key References

- **[Foundational]** J. H. Mason. *Matroids: unimodal conjectures and Motzkin's problem.* In: Combinatorics (Proc. Conf. Combinatorial Mathematics, Math. Inst., Oxford, 1972), pp. 207–220. Institute of Mathematics and its Applications, 1972.
- **[Foundational]** D. J. A. Welsh. *Matroid Theory.* Academic Press, London, 1976.
- **[Foundational]** J. Oxley. *Matroid Theory*, 2nd ed. Oxford University Press, 2011.
- **[Historical]** C. Mahoney. *On the unimodality of the independent set numbers of a class of matroids.* Journal of Combinatorial Theory, Series B, 39 (1985), 77–85.
- **[Historical]** Y. O. Hamidoune, I. Salaün. *On the independence numbers of a matroid.* Journal of Combinatorial Theory, Series B, 47 (1989), 146–152.
- **[Partial]** M. Lenz. *The f-vector of a representable-matroid complex is log-concave.* Advances in Applied Mathematics, 51 (2013), 543–545.
- **[Partial]** J. Huh. *h-vectors of matroids and logarithmic concavity.* Advances in Mathematics, 270 (2015), 49–59.
- **[SOTA]** K. Adiprasito, J. Huh, E. Katz. *Hodge theory for combinatorial geometries.* Annals of Mathematics, 188 (2018), 381–452.
- **[SOTA]** P. Brändén, J. Huh. *Lorentzian polynomials.* Annals of Mathematics, 192 (2020), 821–891.
- **[SOTA]** N. Anari, K. Liu, S. Oveis Gharan, C. Vinzant. *Log-concave polynomials III: Mason's ultra-log-concavity conjecture for independent sets of matroids.* Proceedings of the American Mathematical Society, 152 (2024), 1969–1981.
- **[SOTA]** J. Huh, B. Schröter, B. Wang. *Correlation bounds for fields and matroids.* Journal of the European Mathematical Society, 24 (2022), 1335–1351.
- **[Recent]** A. Berget, C. Eur, H. Spink, D. Tseng. *Tautological classes of matroids.* Inventiones Mathematicae, 233 (2023), 951–1039.
- **[Survey]** M. Baker. *Hodge theory in combinatorics.* Bulletin of the American Mathematical Society, 55 (2018), 57–80.
- **[Survey]** S. H. Chan, I. Pak. *Introduction to the combinatorial atlas.* Expositiones Mathematicae, 40 (2022), 1014–1048.
- **[Context]** R. P. Stanley. *Cohen–Macaulay complexes.* In: Higher Combinatorics (M. Aigner, ed.), Reidel, 1977, 51–62.

## 10. Worked Example / Concrete Special Case

**(a) Rank 2, proved by hand.** Let $M$ be a loopless rank-2 matroid on $n$ elements whose parallel classes have sizes $a_1,\dots,a_m$, $\sum a_i = n$. Then
$$I_0 = 1, \qquad I_1 = n, \qquad I_2 = \binom{n}{2} - \sum_{i=1}^m \binom{a_i}{2}.$$
The only instance of (M3) is $k=1$, which in normalized form reads
$$\left(\frac{I_1}{\binom{n}{1}}\right)^2 \;\ge\; \frac{I_0}{\binom{n}{0}}\cdot\frac{I_2}{\binom{n}{2}} \quad\Longleftrightarrow\quad 1 \ge \frac{I_2}{\binom{n}{2}},$$
which holds because independent pairs are a subset of all pairs. Equality occurs exactly when every $a_i = 1$, i.e. $M = U_{2,n}$. The same computation in Mason's original form is $I_1^2 \ge \frac{2}{1}\cdot\frac{n}{n-1} I_0 I_2$, i.e. $n^2 \ge \frac{2n}{n-1}\bigl(\binom n2 - \sum\binom{a_i}{2}\bigr) = n^2 - \frac{2n}{n-1}\sum\binom{a_i}{2}$. ✔

**(b) The graphic matroid $M(K_4)$.** Ground set = the $6$ edges of $K_4$; rank $r = 3$; independent sets = forests.
$$I_0 = 1,\quad I_1 = 6,\quad I_2 = \binom{6}{2} = 15,\quad I_3 = \binom{6}{3} - \\#\{\text{triangles}\} = 20 - 4 = 16.$$
(No two edges form a circuit since $K_4$ is simple, so $I_2 = \binom62$; the only 3-edge dependent sets are the four triangles.)

Normalized sequence: $\;I_k/\binom{6}{k} = (1,\ 1,\ 1,\ 0.8)$, log-concave. Checking (M3) directly:

| $k$ | LHS $I_k^2$ | factor $\frac{k+1}{k}\cdot\frac{n-k+1}{n-k}$ | RHS |
|---|---|---|---|
| $1$ | $36$ | $2 \cdot \tfrac{6}{5} = 2.4$ | $2.4 \cdot 1 \cdot 15 = 36$ |
| $2$ | $225$ | $\tfrac32 \cdot \tfrac54 = 1.875$ | $1.875 \cdot 6 \cdot 16 = 180$ |

At $k=1$ the inequality is **tight** ($36 = 36$), reflecting simplicity of $K_4$; at $k=2$ there is slack $225 > 180$, and the weaker (M1) reads $225 \ge 96$. This single example shows both that (M3)'s constant is unimprovable and that (M1) and (M2) are strictly weaker.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*