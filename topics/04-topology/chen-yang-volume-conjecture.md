---
id: 04-topology/chen-yang-volume-conjecture
title: "Volume Conjecture for Turaev–Viro Invariants of Links in 3-Manifolds"
topic: 04-topology
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Volume Conjecture for Turaev–Viro Invariants of Links in 3-Manifolds

> **Topic:** Topology & Knot Theory · **ID:** `04-topology/chen-yang-volume-conjecture` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Let $M$ be a compact orientable 3-manifold with empty or toroidal boundary, and let $TV_r(M;q)$ denote the Turaev–Viro invariant at level $r$. Chen and Yang (2015) conjectured that, **evaluated at the unusual root of unity** $q = e^{2\pi i/r}$ (rather than the standard $q=e^{\pi i /r}$), these invariants grow exponentially at a rate equal to the hyperbolic volume:

$$
lTV(M) \;:=\; \lim_{\substack{r\to\infty \\ r\ \text{odd}}} \frac{2\pi}{r-2}\,\log\big|TV_r(M;\,q=e^{2\pi i/r})\big| \;=\; \mathrm{Vol}(M),
$$

where $\mathrm{Vol}(M)$ is the volume of the complete hyperbolic structure on the interior of $M$. The problem of interest here is the **link version**: for a link $L \subset M$ in a closed 3-manifold, the statement is asserted for the link exterior $M \setminus L$ whenever that exterior is hyperbolic, and in the general (non-hyperbolic) case the conjecture is upgraded to the **Gromov norm form**

$$
lTV(M\setminus L) \;=\; v_3\,\|M\setminus L\|,
$$

with $v_3 = 1.0149416\ldots$ the volume of the regular ideal hyperbolic tetrahedron and $\|\cdot\|$ the simplicial (Gromov) norm.

A complete proof requires establishing both the limit's existence and its value for all such pairs $(M,L)$; a disproof requires one pair where the limit fails to exist or differs from $v_3\|M\setminus L\|$. The conjecture is striking because at the *standard* root of unity the same invariants are known to be **polynomially bounded** in $r$ (Garoufalidis–Le), so the phenomenon is entirely an artifact of the non-standard evaluation.

## 2. Mathematical Foundations

**Turaev–Viro state sum.** Fix an odd integer $r \ge 3$ and set $q = A^2 = e^{2\pi i /r}$. Write $[n] = \frac{q^{n}-q^{-n}}{q-q^{-1}}$ and $\eta_r = \frac{2\sin(2\pi/r)}{\sqrt r}$. Given a triangulation $\mathcal T$ of $M$ with edge set $E$ and tetrahedron set $T$, a coloring $c: E \to I_r=\{0,2,4,\dots,r-3\}$ is *admissible* if each face's triple $(a,b,c)$ satisfies the triangle inequalities $|a-b|\le c \le a+b$ and $a+b+c \le 2(r-2)$ with $a+b+c$ even. Then

$$
TV_r(M;q) \;=\; \eta_r^{\,2|V|}\sum_{c\ \mathrm{admissible}} \ \prod_{e\in E} \|c(e)\| \ \prod_{t\in T}\left|\begin{matrix} a & b & c\\ d& e& f\end{matrix}\right|_c ,
$$

where $\|n\| = (-1)^n[n+1]$ and the tetrahedral weight is the quantum $6j$-symbol built from Racah coefficients of $U_q(\mathfrak{sl}_2)$. Turaev–Viro (1992) proved invariance under Pachner moves, so $TV_r$ depends only on the homeomorphism type of $M$.

**Relation to Reshetikhin–Turaev.** For odd $r$ and the $SO(3)$ theory, $TV_r(M;q) = |RT_r(M;A)|^2$ (Turaev–Walker–Roberts, in the form used by Detcherry–Kalfagianni–Yang), so the conjecture has an equivalent formulation for the Witten–Reshetikhin–Turaev invariants: $\lim \frac{4\pi}{r-2}\log|RT_r(M)| = \mathrm{Vol}(M)$.

**Colored Jones formula (link case).** Detcherry–Kalfagianni–Yang proved that for a link $L\subset S^3$ with $n$ components and odd $r=2m+1$,

$$
TV_r(S^3\setminus L;\,q=e^{2\pi i/r}) \;=\; \eta_r^{\,2}\sum_{1\le i\le m} \big|J_L(i;\,t=q^2=e^{4\pi i /r})\big|^{2},
$$

where $J_L(i)$ is the unnormalized $i$-colored Jones polynomial (all components colored $i$). This converts a 3-manifold state sum into a finite sum of link polynomial evaluations, and shows the Chen–Yang conjecture for $S^3\setminus L$ **implies** the Kashaev–Murakami–Murakami volume conjecture growth rate for $L$ at $t=e^{4\pi i/r}$, up to the max-versus-sum distinction.

**Reference point.** The Kashaev invariant $\langle L\rangle_N = J'_L(N; e^{2\pi i/N})$ satisfies the original volume conjecture $\lim \frac{2\pi}{N}\log|\langle L\rangle_N| = \mathrm{Vol}(S^3\setminus L)$ (Kashaev 1997; Murakami–Murakami 2001). Chen–Yang's is a genuinely different evaluation: the parameter is $e^{4\pi i/r}$, not $e^{2\pi i/r}$.

## 3. History & State of the Art (SOTA)

- **1991–92.** Reshetikhin–Turaev construct $RT_r$; Turaev–Viro define $TV_r$ as a state sum on $6j$-symbols.
- **1997–2001.** Kashaev formulates the volume conjecture for the hyperbolic volume from his invariant; Murakami–Murakami identify $\langle L\rangle_N$ with a colored Jones evaluation, giving the modern statement.
- **2005.** Garoufalidis–Le prove that at the standard root $q=e^{\pi i/r}$ the quantum invariants of a fixed 3-manifold grow at most polynomially — the "asymptotic expansion conjecture" regime, where no volume appears.
- **2015/2018.** Q. Chen and T. Yang, *Volume conjectures for the Reshetikhin–Turaev and the Turaev–Viro invariants* (Quantum Topology 9, 2018), state the conjecture and verify it numerically to high precision for the figure-eight and $5_2$ knot complements, the Whitehead link, and dozens of closed and cusped census manifolds.
- **2018.** Detcherry–Kalfagianni–Yang prove the colored-Jones formula above and give the first **rigorous** proofs: the figure-eight knot complement and the Borromean rings complement.
- **2020.** Belletti–Detcherry–Kalfagianni–Yang prove the conjecture for all **fundamental shadow links**, an infinite family with arbitrarily large volume; combined with Costantino–Thurston shadow theory this yields: every closed orientable 3-manifold $M$ contains a link $L$ with $M\setminus L$ satisfying the conjecture.
- **2018–2022.** Ohtsuki, Ohtsuki–Yokota, and Wong–Yang produce full asymptotic expansions in surgery families and for relative Reshetikhin–Turaev invariants of links in closed manifolds, where the growth rate recovers the volume of hyperbolic **cone** manifolds.

## 4. Partial Results / Verified Cases

| Class | Result | Source |
|---|---|---|
| Figure-eight knot complement $S^3\setminus 4_1$ | Proved, $lTV = 2.029883\ldots$ | Detcherry–Kalfagianni–Yang 2018 |
| Borromean rings complement ($=$ 2 ideal octahedra, $\mathrm{Vol}=2v_8=7.3277$) | Proved | Detcherry–Kalfagianni–Yang 2018 |
| Fundamental shadow links (complements $=$ $2c$ ideal octahedra glued along faces), all $c\ge 1$ | Proved, $lTV = 2c\,v_8$, $v_8=3.66386\ldots$ | Belletti–Detcherry–Kalfagianni–Yang 2020 |
| Every closed orientable $M$: exists $L\subset M$ with $M\setminus L$ satisfying the conjecture | Proved (corollary of the above) | BDKY 2020 |
| Cables and connected sums of verified links | Growth rate behaves additively/invariantly, so the class is closed under cabling and connect-sum | BDKY 2020 ("Growth of Turaev–Viro invariants and cabling") |
| Whitehead chains, octahedral links realized in $S^3$ | Proved for further explicit infinite families | S. Kumar, 2021 |
| Closed manifolds from integral surgery along $4_1$ | Asymptotic expansion of $RT_r$ established with volume as leading exponential rate | Ohtsuki 2018; Wong–Yang |
| Non-hyperbolic exteriors | Gromov-norm version verified for graph-manifold and Seifert-fibered pieces where $\|\cdot\|=0$ and $lTV=0$ | Detcherry–Kalfagianni 2019/2020 |

Numerically, Chen–Yang verified the limit to 4–6 significant digits for $r \le 65$ on knots up to 8 crossings and on cusped census manifolds; convergence is slow (error $O(\log r / r)$).

## 5. Principal Obstacles

- **No geometric term in the state sum.** The $6j$-symbols carry no visible hyperbolic structure; the volume appears only after a saddle-point analysis of an oscillating sum with exponentially many terms and near-total cancellation. Controlling that cancellation uniformly in $r$ is the core analytic barrier.
- **Sum versus maximum.** The colored-Jones formula reduces $TV_r$ to $\sum_i |J_L(i)|^2$. Proving the lower bound requires showing that a single dominant color $i \approx (r-1)/2$ is not cancelled; proving the upper bound requires uniform control on **all** $m \sim r/2$ terms. Techniques that give one bound rarely give the other.
- **Saddle points off the real locus.** In the Ohtsuki-style Poisson-summation approach the relevant critical point of the potential function is the geometric solution of Thurston's gluing equations, but the steepest-descent contour must be deformed through complex space; existence of a valid deformation is proved case-by-case using explicit triangulations, and no general argument exists.
- **Triangulation dependence of estimates.** Bounds derived from a specific ideal triangulation degrade with the number of tetrahedra; there is no known "quantum Gromov norm" subadditivity strong enough to give $lTV \le v_3\|M\|$ in general.
- **No categorified or gauge-theoretic bridge.** Unlike the Casson/Floer setting, there is no known chain-level model whose Euler characteristic is $TV_r$ and whose filtration records volume.

## 6. The Gap

Proved cases share one structural feature: the exterior decomposes into **regular ideal octahedra or ideal tetrahedra whose $6j$-symbols are given in closed form**, so the state sum collapses to a one-parameter sum of $q$-Pochhammer type amenable to explicit Lobachevsky-function estimates. The general conjecture asserts the same asymptotics for triangulations with arbitrary, non-regular shape parameters, where the $6j$-symbols must be estimated rather than evaluated.

The precise missing step: a **uniform asymptotic expansion of the quantum $6j$-symbol at $q=e^{2\pi i /r}$ whose leading term is $\exp\!\big(\tfrac{r}{2\pi}\mathrm{Vol}(\text{hyperbolic tetrahedron})\big)$, valid with error terms uniform over all admissible colorings**, plus a proof that the resulting sum over colorings is dominated by colorings near the geometric one. Costantino's and Belletti's results give the tetrahedral asymptotics in wide ranges (and Belletti's maximum-volume theorem for hyperbolic polyhedra supplies the matching upper bound for the *maximal* term), but the uniformity across the full coloring set, and the exclusion of destructive interference between exponentially many near-maximal terms, is exactly what remains unproven.

## 7. Current Research (as of June 2026)

- **Michigan State / Kalfagianni school** (Kalfagianni, Detcherry, Kumar, Belletti): extending the fundamental-shadow-link method by Dehn filling, and proving stability of $lTV$ under filling to reach closed hyperbolic manifolds. *(frontier — verify)*
- **Texas A&M / Yang school** (T. Yang, K. H. Wong): relative Reshetikhin–Turaev invariants of links in closed manifolds, where growth rates yield volumes of hyperbolic cone metrics; discrete Fourier transform techniques convert the state sum into an integral with a controlled potential.
- **Ohtsuki's asymptotic-expansion program** (Tokyo Institute of Technology / RIMS): full asymptotic series with the expected $r^{3/2}$ prefactor and the $1$-loop (Reidemeister torsion) correction, established for explicit surgery families.
- **Skein-theoretic and $AJ$-type approaches**: using the Kauffman bracket skein module at $q=e^{2\pi i /r}$ and its relation to $SL_2(\mathbb C)$ character varieties (Bonahon–Wong–Yang quantum trace and representation theory of skein algebras at roots of unity) to explain why the geometric representation dominates. *(frontier — verify)*
- **Complex Chern–Simons / resurgence**: physics-side derivations (Gukov, Mariño, Putrov, Gang) predicting the exponentially large behavior from the resurgent structure of the $\hat Z$-invariants; these give the expected constants but are not rigorous.

## 8. Future Work

1. Prove a **uniform** upper bound $lTV(M)\le v_3\|M\|$ for all compact $M$ — this half is conjecturally accessible via Belletti's theorem that the volume of a hyperbolic polyhedron is maximized by the regular ideal octahedron, plus a shadow-complexity count.
2. Establish stability of $lTV$ under Dehn filling with uniform error, converting the fundamental-shadow-link theorem into a statement about all closed hyperbolic 3-manifolds.
3. Develop a version of the state sum whose terms are manifestly positive (a "positivity/monotonicity" mechanism) to remove cancellation from the lower-bound argument.
4. Prove the conjecture for all hyperbolic knot complements in $S^3$ with at most a fixed number of ideal tetrahedra, closing the gap between numerical census verification and proof.
5. Extend from $SU(2)$ to $SU(n)$ / $\mathfrak{sl}_n$ Turaev–Viro-type invariants and test whether the volume rate persists.

## 9. Key References

- **[Foundational]** V. G. Turaev, O. Y. Viro. *State sum invariants of 3-manifolds and quantum 6j-symbols.* Topology 31 (1992), 865–902.
- **[Foundational]** R. Kashaev. *The hyperbolic volume of knots from the quantum dilogarithm.* Letters in Mathematical Physics 39 (1997), 269–275.
- **[Foundational]** H. Murakami, J. Murakami. *The colored Jones polynomials and the simplicial volume of a knot.* Acta Mathematica 186 (2001), 85–104.
- **[Foundational]** Q. Chen, T. Yang. *Volume conjectures for the Reshetikhin–Turaev and the Turaev–Viro invariants.* Quantum Topology 9 (2018), 419–460.
- **[SOTA]** R. Detcherry, E. Kalfagianni, T. Yang. *Turaev–Viro invariants, colored Jones polynomials and volume.* Quantum Topology 9 (2018), 775–813.
- **[SOTA]** G. Belletti, R. Detcherry, E. Kalfagianni, T. Yang. *Growth of Turaev–Viro invariants and cabling.* Journal of Topology 13 (2020), 1–20.
- **[SOTA]** R. Detcherry, E. Kalfagianni. *Gromov norm and Turaev–Viro invariants of 3-manifolds.* Annales Scientifiques de l'École Normale Supérieure 53 (2020), 1363–1391.
- **[SOTA]** T. Ohtsuki. *On the asymptotic expansion of the quantum SU(2) invariant at $q=\exp(4\pi\sqrt{-1}/N)$ for closed hyperbolic 3-manifolds obtained by integral surgery along the figure-eight knot.* Algebraic & Geometric Topology 18 (2018), 4187–4274.
- **[SOTA]** G. Belletti. *The maximum volume of hyperbolic polyhedra.* Transactions of the American Mathematical Society 374 (2021), 1125–1153.
- **[SOTA]** S. Kumar. *Fundamental shadow links realized as links in $S^3$.* Algebraic & Geometric Topology 21 (2021), 3153–3198.
- **[Related]** F. Costantino, D. Thurston. *3-manifolds efficiently bound 4-manifolds.* Journal of Topology 1 (2008), 703–745.
- **[Survey]** H. Murakami. *An introduction to the volume conjecture.* Contemporary Mathematics 541 (2011), 1–40.
- **[Survey]** S. Garoufalidis, T. T. Q. Le. *The colored Jones function is $q$-holonomic.* Geometry & Topology 9 (2005), 1253–1293.

## 10. Worked Example / Concrete Special Case

**The figure-eight knot $4_1$.** Habiro's formula for the unnormalized colored Jones polynomial with color $n$ at variable $t$:

$$
J_{4_1}(n;t) \;=\; \sum_{k=0}^{n-1}\ \prod_{j=1}^{k}\Big(t^{\frac{n-j}{2}}-t^{-\frac{n-j}{2}}\Big)\Big(t^{\frac{n+j}{2}}-t^{-\frac{n+j}{2}}\Big).
$$

Set $r=2m+1$ odd, $t=e^{4\pi i/r}$, and take the top color $n=m=\frac{r-1}{2}$. Then $t^{(n\mp j)/2} = e^{2\pi i (n \mp j)/r}$, and

$$
\frac{2\pi(n-j)}{r} = \pi - \frac{\pi(2j+1)}{r},\qquad \frac{2\pi(n+j)}{r} = \pi + \frac{\pi(2j-1)}{r}.
$$

Hence the $k$-th summand has modulus exactly

$$
P_k \;=\; \prod_{j=1}^{k} 4\,\sin\!\Big(\frac{\pi(2j+1)}{r}\Big)\sin\!\Big(\frac{\pi(2j-1)}{r}\Big).
$$

All factors are positive, so **no cancellation occurs** — this is precisely why $4_1$ is tractable. A factor exceeds $1$ iff its two sines are jointly large, i.e. roughly while $\frac{2j}{r}\in(\tfrac16,\tfrac56)$, so $P_k$ increases up to $k^\ast \approx \tfrac{5r}{12}$ and decreases after. Taking logarithms and using $\sum_{j\le k}\log 2\sin(2\pi j/r)\approx \frac{r}{2\pi}\int_0^{2\pi k/r}\log|2\sin x|\,dx = -\frac{r}{2\pi}\Lambda\!\big(\tfrac{2\pi k}{r}\big)$ with $\Lambda$ the Lobachevsky function,

$$
\log P_k \;\approx\; -\frac{r}{\pi}\,\Lambda\!\Big(\frac{2\pi k}{r}\Big).
$$

This is maximized where $\Lambda$ is minimal, at $\frac{2\pi k}{r}=\frac{5\pi}{6}$ (i.e. $k=\frac{5r}{12}$), giving $\Lambda(5\pi/6) = -\Lambda(\pi/6) = -0.5074708\ldots$ and therefore $\log P_{k^\ast}\approx \frac{r}{\pi}(0.5074708)$. Consequently

$$
\frac{2\pi}{r-2}\log\big|J_{4_1}(m)\big| \;\longrightarrow\; 2\Lambda(\pi/6) \;=\; 3\Lambda(\pi/3) \;=\; v_3 \;=\; 1.0149416\ldots
$$

Feeding this into $TV_r(S^3\setminus 4_1)=\eta_r^2\sum_{i\le m}|J_{4_1}(i)|^2$, the squaring doubles the rate while $\eta_r^2 = O(r^{-1})$ and the sum over $i\le m$ contribute only polynomial factors that die under $\frac{2\pi}{r-2}\log(\cdot)$. Hence

$$
lTV(S^3\setminus 4_1) \;=\; 2v_3 \;=\; 2.0298832\ldots \;=\; \mathrm{Vol}(S^3\setminus 4_1),
$$

matching the two regular ideal tetrahedra of the figure-eight complement. Numerically, at $r=25$ the left side evaluates to about $1.87$ and at $r=65$ to about $1.96$ — visibly convergent but with the $O(\log r/r)$ error that makes purely numerical confirmation weak evidence. For a general hyperbolic link the analogous sum has summands of varying phase; the positivity that made this computation elementary is lost, and that loss is the content of Section 5.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*