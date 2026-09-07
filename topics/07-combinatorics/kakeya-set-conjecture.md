---
id: 07-combinatorics/kakeya-set-conjecture
title: "Kakeya Set Conjecture"
topic: 07-combinatorics
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Kakeya Set Conjecture

> **Topic:** Combinatorics & Graph Theory · **ID:** `07-combinatorics/kakeya-set-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

A **Kakeya set** (Besicovitch set) in $\mathbb{R}^n$ is a compact set containing a unit line segment in every direction. Besicovitch showed such sets can have Lebesgue measure zero. The conjecture asserts they cannot be small in a dimensional sense.

**Conjecture (Kakeya set conjecture).** Every Kakeya set $K \subset \mathbb{R}^n$, $n \ge 2$, satisfies
$$\dim_H(K) = \dim_M(K) = n,$$
where $\dim_H$ is Hausdorff dimension and $\dim_M$ is (upper) Minkowski dimension.

A complete proof must handle arbitrary compact $K$ containing a segment in *every* direction of $S^{n-1}$; a disproof requires an explicit Kakeya set with $\dim_H(K) = n - \delta$ for some $\delta > 0$. The Minkowski version is formally weaker ($\dim_H \le \dim_M$), so the Hausdorff statement is the target. The case $n = 2$ (Davies, 1971) and $n = 3$ (Wang–Zahl, 2025) are settled; $n \ge 4$ is open.

## 2. Mathematical Foundations

**Hausdorff dimension.** For $s \ge 0$ and $E \subset \mathbb{R}^n$,
$$\mathcal{H}^s(E) = \lim_{\delta \to 0}\ \inf\Big\{ \sum_i (\operatorname{diam} U_i)^s : E \subset \bigcup_i U_i,\ \operatorname{diam} U_i < \delta \Big\},\qquad \dim_H(E) = \inf\{ s : \mathcal{H}^s(E) = 0\}.$$
**Minkowski dimension.** With $N(E,\delta)$ the minimal number of $\delta$-balls covering $E$,
$$\overline{\dim}_M(E) = \limsup_{\delta \to 0} \frac{\log N(E,\delta)}{\log(1/\delta)}.$$

**Kakeya maximal function.** For $\delta > 0$, let $T^\delta_e(a)$ be the $\delta$-neighbourhood of the unit segment in direction $e \in S^{n-1}$ centred at $a$ — a $\delta \times \cdots \times \delta \times 1$ tube. Define
$$f^*_\delta(e) = \sup_{a \in \mathbb{R}^n} \frac{1}{|T^\delta_e(a)|}\int_{T^\delta_e(a)} |f|.$$
**Kakeya maximal conjecture.** For all $\varepsilon > 0$,
$$\|f^*_\delta\|_{L^n(S^{n-1})} \le C_\varepsilon\, \delta^{-\varepsilon}\, \|f\|_{L^n(\mathbb{R}^n)}.$$
This implies the set conjecture; it is strictly stronger, and both follow from the **restriction** and **Bochner–Riesz** conjectures (Fefferman 1971; Bourgain 1991).

**Discretized form.** A collection of $\delta$-separated directions $\{e_j\}_{j=1}^{\sim \delta^{1-n}}$ with tubes $T_j = T^\delta_{e_j}(a_j)$ satisfies, conjecturally,
$$\Big| \bigcup_j T_j \Big| \ \ge\ c_\varepsilon\, \delta^{\varepsilon}.$$
Equivalently, in $L^{n/(n-1)}$ dual form: $\big\|\sum_j \chi_{T_j}\big\|_{n/(n-1)} \lesssim_\varepsilon \delta^{-\varepsilon}\big(\sum_j |T_j|\big)^{(n-1)/n}$.

**Finite-field model.** For $\mathbb{F}_q^n$, a Kakeya set $K$ contains a line in every direction $b \in \mathbb{F}_q^n \setminus \{0\}$: for each $b$ there is $a$ with $\{a + tb : t \in \mathbb{F}_q\} \subset K$. Here the conjecture reads $|K| \ge c_n q^n$.

## 3. History & State of the Art (SOTA)

- **1917/1919 — Kakeya, Besicovitch.** Sōichi Kakeya asked for the minimal area needed to rotate a needle continuously by $180^\circ$. Abram Besicovitch, working on Riemann integration, constructed a compact set of measure zero containing a segment in every direction, and deduced (Besicovitch 1928) that the needle can be turned in arbitrarily small area. The **Perron tree** construction (Perron 1928; Schoenberg) gives an elementary version.
- **1971 — Davies.** $\dim_H(K) = 2$ for every Kakeya set in $\mathbb{R}^2$. The plane is settled.
- **1971 — Fefferman.** Disproof of the ball multiplier conjecture using Besicovitch sets, establishing the link between Kakeya geometry and Fourier summation.
- **1991 — Bourgain.** "Bush" and bilinear ideas give $\dim_H \ge (n+1)/2 + \epsilon_n$; also the formal Kakeya $\Rightarrow$ restriction chain.
- **1995 — Wolff.** The **hairbrush** argument: $\dim_H(K) \ge (n+2)/2$ for all $n$. Still the best general bound at $n=3,4$ until the 2019–2025 work.
- **1999–2002 — Bourgain; Katz–Tao.** Arithmetic-combinatorial methods (sum-difference inequalities, Gowers-type counting) give $\dim_H \ge 13n/25 + 12/25$ (Bourgain 1999) and $\dim_H \ge (2-\sqrt2)(n-4)+3 \approx 0.5858n + 0.6$ (Katz–Tao 2002), which beats Wolff for $n \ge 5$.
- **2000 — Katz–Łaba–Tao.** Upper Minkowski dimension $\ge 5/2 + 10^{-10}$ in $\mathbb{R}^3$: the first break past Wolff's exponent, via a three-way structure trichotomy (plany/sticky/graininess).
- **2009 — Dvir.** The **polynomial method** resolves the finite-field Kakeya conjecture completely: $|K| \ge c_n q^n$.
- **2019 — Katz–Zahl.** $\dim_H \ge 5/2 + \varepsilon_0$ in $\mathbb{R}^3$ with $\varepsilon_0 = 10^{-10}$, for Hausdorff dimension.
- **2025 — Wang–Zahl.** Proof that every Kakeya set in $\mathbb{R}^3$ has Hausdorff and Minkowski dimension $3$, via sticky-Kakeya structure and a volume estimate for unions of convex sets. Widely regarded as settling $n = 3$ *(frontier — verify: published version pending as of 2026-06)*.

## 4. Partial Results / Verified Cases

| Setting | Result | Source |
|---|---|---|
| $n = 2$, $\mathbb{R}^2$ | $\dim_H = 2$ (full conjecture) | Davies 1971 |
| $n = 3$, $\mathbb{R}^3$ | $\dim_H = \dim_M = 3$ (full conjecture) | Wang–Zahl 2025 |
| All $n$ | $\dim_H \ge (n+2)/2$ | Wolff 1995 |
| $n \ge 5$ | $\dim_H \ge (2-\sqrt2)(n-4)+3$ | Katz–Tao 2002 |
| $n = 4$ | $\dim_H \ge 3.059$ | Zahl 2021 (Gromov algebraic lemma) |
| Minkowski, all $n$ | $\dim_M \ge (4n+3)/7$ | Katz–Tao 2001 |
| $\mathbb{F}_q^n$, all $n$, all $q$ | $|K| \ge q^n / 2^n$ | Dvir 2009; Dvir–Kopparty–Saraf–Sudan 2013 |
| Kakeya maximal, $n=2$ | $\|f^*_\delta\|_{L^2(S^1)} \lesssim \log(1/\delta)^{1/2}\|f\|_2$, sharp | Córdoba 1977 |
| Structured families | Full dimension for sets of lines with algebraic/analytic parametrization, e.g. Nikodym and "sticky" cases | Katz–Zahl 2019; Wang–Zahl 2025 |
| Curved/nilpotent models | Kakeya for the Heisenberg group and $SL_2$ line families | Katz–Tao 2002; Zahl 2023 |

Under Assouad and packing dimension the conjecture is also known in weaker regularity classes; the measure-zero constructions of Besicovitch show no measure-theoretic improvement is possible.

## 5. Principal Obstacles

- **No non-trivial upper-bound examples to guide the proof.** All known Besicovitch sets have full dimension, so the extremal configuration is unknown; one cannot reverse-engineer a proof from a near-counterexample.
- **The Heisenberg / $SL_2$ obstruction.** Katz and Tao exhibited line families in $\mathbb{R}^n$ (over $\mathbb{C}$-like or nilpotent structures) satisfying *all* the two-slice and three-slice combinatorial axioms used by arithmetic methods, but with dimension $< n$. Any purely incidence-combinatorial argument that does not use the ordered-field structure of $\mathbb{R}$ is therefore doomed above the Katz–Tao exponent.
- **The polynomial method does not transfer.** Dvir's proof interpolates a polynomial of degree $< q$ vanishing on $K$ and uses that a polynomial vanishing on a full line vanishes at its point at infinity. Over $\mathbb{R}$ the corresponding statement is quantitative and scale-dependent: a low-degree polynomial can vanish on a $\delta$-neighbourhood of many lines while the union has small volume at scale $\delta$. Guth's polynomial partitioning recovers some of this but loses the crucial "degree $\le q$" rigidity.
- **Multi-scale non-self-similarity.** Real Kakeya sets can behave differently at different scales (the "sticky vs. plany vs. grainy" trichotomy). Wolff's hairbrush is a single-scale argument and saturates exactly at $(n+2)/2$; breaking it requires induction on scales with tube families whose direction sets are themselves fractal.
- **Dimensional inflation of the case analysis.** The $n=3$ proof (Wang–Zahl) rests on a classification of $3$-parameter line families and a convex-set volume estimate whose combinatorics grow rapidly with $n$; there is no known $n$-uniform analogue of the grains/graininess structure theorem.
- **Loss in $\varepsilon$-bookkeeping.** Induction-on-scale arguments accumulate $\delta^{-\varepsilon}$ factors; controlling them for arbitrary $n$ requires uniform constants that current arguments do not supply.

## 6. The Gap

Known: $\dim_H(K) \ge \max\{(n+2)/2,\ (2-\sqrt2)(n-4)+3\}$ for $n \ge 4$. Conjectured: $n$. The gap is asymptotically **linear**: current bounds give roughly $0.5858n$, so a constant fraction $\approx 0.414n$ of the dimension is missing, and it *widens* with $n$. Even the qualitative statement "$\dim_H(K) \ge (1/2 + c)n$ for an absolute $c > 0$ and all large $n$" is open beyond $c = 0.086$.

The precise barrier: propagate the $n = 3$ mechanism — a structure theorem forcing a Kakeya set that is not full-dimensional to be *sticky* (its line family is Lipschitz-parametrized over scales), followed by a volume lower bound for unions of the resulting convex "grains" — to $n \ge 4$. In $\mathbb{R}^3$ grains are $\delta \times \rho \times 1$ slabs classified by planar incidence geometry; in $\mathbb{R}^4$ the intermediate-dimensional grains form a two-parameter family with no available Szemerédi–Trotter-type incidence bound at every intermediate scale. Supplying such multi-scale incidence estimates in $\mathbb{R}^n$ is the exact missing step.

## 7. Current Research (as of June 2026)

- **Verification and dissemination of Wang–Zahl.** The $\mathbb{R}^3$ proof (arXiv 2502.17655) is under peer review and being reworked into modular form; several groups are extracting the "sticky reduction" and the convex-union volume estimate as standalone tools *(frontier — verify)*.
- **Push to $\mathbb{R}^4$.** Joshua Zahl (UBC), Hong Wang (NYU Courant / IAS), Nets Katz (Rice) and collaborators are testing whether the sticky-Kakeya structure theorem admits a $4$-dimensional analogue; partial announcements target improving $3.059$ toward $7/2$ *(frontier — verify)*.
- **Furstenberg-set methods.** Ren–Wang's resolution of the planar Furstenberg set problem (2023) supplies sharp $(s,t)$ exceptional-projection estimates now feeding into higher-dimensional Kakeya arguments.
- **Restriction/decoupling transfer.** Guth, Hickman, Iliopoulou, Bourgain–Demeter-style decoupling and polynomial partitioning continue to improve restriction exponents, which conditionally strengthen Kakeya-type maximal bounds.
- **Algebraic and $p$-adic models.** Kakeya over $\mathbb{Z}/p^k$, function fields, and for curved line families ($SL_2$, Heisenberg) probes which parts of the real problem are genuinely metric rather than combinatorial.
- **Institutions.** NYU Courant, IAS Princeton, UBC, Caltech/Rice, Bonn (Hausdorff Center), Edinburgh, Hebrew University.

## 8. Future Work

- Formulate a **dimension-uniform structure theorem**: any Kakeya set with $\dim_H < n$ must be sticky at all scales, for every $n$. This is the strategy Katz and Tao proposed in 2002 and which succeeded at $n = 3$.
- Develop **multi-scale incidence geometry for convex bodies** ("grains") in $\mathbb{R}^n$, generalizing the $\delta$-slab counting used in three dimensions.
- Prove the **maximal-function version** in $\mathbb{R}^3$, which does not follow formally from the set statement, then the $L^p$ endpoints.
- Seek a **real analogue of the polynomial method** with degree control at every scale — Guth's polynomial partitioning plus algebraic-geometric degree bounds (Gromov, Solymosi–Tao) is the leading candidate.
- Settle **intermediate conjectures**: Nikodym, Furstenberg, and $SL_2$-Kakeya in $\mathbb{R}^4$, each of which is implied by, or implies pieces of, the general case.
- Determine whether Kakeya in all dimensions implies **restriction/Bochner–Riesz**, which is known to be false in the naive direction; identify the additional geometric input needed.

## 9. Key References

- **[Foundational]** A. S. Besicovitch. *On Kakeya's problem and a similar one.* Mathematische Zeitschrift 27 (1928), 312–320.
- **[Foundational]** R. O. Davies. *Some remarks on the Kakeya problem.* Proc. Cambridge Philos. Soc. 69 (1971), 417–421.
- **[Foundational]** C. Fefferman. *The multiplier problem for the ball.* Annals of Mathematics 94 (1971), 330–336.
- **[Foundational]** J. Bourgain. *Besicovitch type maximal operators and applications to Fourier analysis.* Geometric and Functional Analysis 1 (1991), 147–187.
- **[Foundational]** T. Wolff. *An improved bound for Kakeya type maximal functions.* Revista Matemática Iberoamericana 11 (1995), 651–674.
- **[SOTA]** N. H. Katz, I. Łaba, T. Tao. *An improved bound on the Minkowski dimension of Besicovitch sets in $\mathbb{R}^3$.* Annals of Mathematics 152 (2000), 383–446.
- **[SOTA]** N. H. Katz, T. Tao. *New bounds for Kakeya problems.* Journal d'Analyse Mathématique 87 (2002), 231–263.
- **[SOTA]** Z. Dvir. *On the size of Kakeya sets in finite fields.* Journal of the AMS 22 (2009), 1093–1097.
- **[SOTA]** Z. Dvir, S. Kopparty, S. Saraf, M. Sudan. *Extensions to the method of multiplicities, with applications to Kakeya sets and mergers.* SIAM Journal on Computing 42 (2013), 2305–2328.
- **[SOTA]** N. H. Katz, J. Zahl. *An improved bound on the Hausdorff dimension of Besicovitch sets in $\mathbb{R}^3$.* Journal of the AMS 32 (2019), 195–259.
- **[SOTA / Recent]** H. Wang, J. Zahl. *Volume estimates for unions of convex sets, and the Kakeya set conjecture in three dimensions.* arXiv:2502.17655, 2025.
- **[Survey]** T. Wolff. *Recent work connected with the Kakeya problem.* In *Prospects in Mathematics* (H. Rossi, ed.), American Mathematical Society, 1999, 129–162.
- **[Survey]** L. Guth. *Polynomial Methods in Combinatorics.* University Lecture Series 64, American Mathematical Society, 2016.
- **[Survey]** T. Tao. *From rotating needles to stability of waves: emerging connections between combinatorics, analysis, and PDE.* Notices of the AMS 48 (2001), 294–303.

## 10. Worked Example / Concrete Special Case

**Dvir's polynomial method in $\mathbb{F}_q^2$.** Claim: any Kakeya set $K \subset \mathbb{F}_q^2$ has $|K| \ge \binom{q+1}{2}$.

*Setup.* $K$ contains, for each direction $b \in \mathbb{F}_q^2\setminus\{0\}$ (up to scaling, $q+1$ directions), a full line $\ell_b = \{a_b + tb\}$.

*Step 1 — interpolation.* The space of polynomials in $\mathbb{F}_q[x_1,x_2]$ of degree $\le d$ has dimension $\binom{d+2}{2}$. Suppose for contradiction $|K| < \binom{d+2}{2}$ with $d = q-1$, i.e. $|K| < \binom{q+1}{2}$. Vanishing at each point of $K$ is one linear condition, so there is a nonzero $P$ with $\deg P \le d = q-1$ and $P|_K = 0$.

*Step 2 — restriction to a line.* Fix a direction $b$. The map $t \mapsto P(a_b + tb)$ is a univariate polynomial of degree $\le q-1$ vanishing at all $q$ values $t \in \mathbb{F}_q$, hence it is identically zero as a polynomial.

*Step 3 — top-degree form.* Write $P = P_d + (\text{lower order})$ with $P_d$ homogeneous of degree $d$. The coefficient of $t^{d}$ in $P(a_b + tb)$ is exactly $P_d(b)$. By Step 2 that coefficient is $0$, so $P_d(b) = 0$ for every direction $b$.

*Step 4 — contradiction.* $P_d$ is homogeneous, so $P_d(\lambda b) = \lambda^d P_d(b) = 0$ for all $\lambda$: $P_d$ vanishes on all of $\mathbb{F}_q^2$. A nonzero polynomial of degree $d \le q-1$ cannot vanish everywhere on $\mathbb{F}_q^2$ (Schwartz–Zippel: it vanishes on at most $d q < q^2$ points). Hence $P_d \equiv 0$ as a polynomial, contradicting $\deg P = d$. Therefore $|K| \ge \binom{q+1}{2} = \tfrac12 q^2 + \tfrac12 q$. $\blacksquare$

*Why this does not settle $\mathbb{R}^2$.* Take $q \sim \delta^{-1}$ and think of $\mathbb{F}_q^2$ as a discretization at scale $\delta$. The argument used two facts with no Euclidean counterpart: (i) a line contains exactly $q$ points, so degree $q-1$ forces exact vanishing — over $\mathbb{R}$ a tube $T^\delta_e$ contains a continuum of points but a polynomial need only be *small*, not zero, on it; (ii) the direction set is the projective line, an algebraic variety, whereas real Kakeya sets may use a fractal, non-algebraic set of directions with different behaviour across scales. The real case at $n=2$ instead needs Davies' measure-theoretic argument (dually, Córdoba's $L^2$ bound $\|f^*_\delta\|_{L^2(S^1)} \lesssim \log(1/\delta)^{1/2}\|f\|_2$, obtained by summing the tube-overlap estimate $|T_i \cap T_j| \lesssim \delta^2/(\delta + \angle(e_i,e_j))$).

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*