---
id: 04-topology/turaev-viro-invariants-asymptotics
title: "Turaev-Viro Invariants Asymptotics"
topic: 04-topology
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Turaev-Viro Invariants Asymptotics

> **Topic:** Topology & Knot Theory · **ID:** `04-topology/turaev-viro-invariants-asymptotics` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Let $M$ be a compact orientable $3$-manifold with empty or toroidal boundary, and let $TV_r(M;q)$ denote the $SO(3)$ Turaev–Viro invariant at odd level $r \ge 3$. Evaluate it at the **root of unity $q = A^2 = e^{2\pi i/r}$** — not at the "standard" $q=e^{i\pi/r}$ used in the original construction.

**Chen–Yang volume conjecture (2015).** For every hyperbolic $M$,
$$\lim_{\substack{r\to\infty \\ r\ \text{odd}}} \frac{4\pi}{r}\,\log TV_r\!\left(M; e^{2\pi i/r}\right) \;=\; \mathrm{Vol}(M),$$
where $\mathrm{Vol}$ is the hyperbolic volume of the interior of $M$ (for manifolds with non-hyperbolic pieces, the conjectured limit is the Gromov norm scaled by $v_3$, the volume of the regular ideal tetrahedron).

Write $l_{TV}(M)$ for the $\limsup$ on the left, the **exponential growth rate**. A complete proof requires (i) existence of the limit, (ii) the lower bound $l_{TV}(M)\ge \mathrm{Vol}(M)$, and (iii) the matching upper bound, for *all* hyperbolic $M$, closed and cusped. A disproof would exhibit one hyperbolic $M$ whose growth rate is provably $\ne \mathrm{Vol}(M)$ (e.g. sub-exponential growth, which was the expected behaviour at the classical root of unity).

Two features make the statement striking: $TV_r$ is a *sum of positive terms*, so there is no cancellation to explain sub-exponential behaviour; and the classical Witten asymptotic expansion conjecture predicts *polynomial* growth of the same invariants at $q=e^{i\pi/r}$. The conjecture asserts that changing the root of unity converts a polynomially bounded topological invariant into an exponentially growing one that reads off geometry.

## 2. Mathematical Foundations

**State sum.** Fix an odd integer $r\ge 3$, set $m=(r-3)/2$, $q=A^2$ with $A$ a primitive $2r$-th root of unity, and let
$$[n] = \frac{A^{2n}-A^{-2n}}{A^2-A^{-2}}, \qquad \eta_r = \frac{A^2-A^{-2}}{\sqrt{-r}} \quad\text{so that}\quad |\eta_r|^2=\frac{4\sin^2(2\pi/r)}{r}\ \ \text{at}\ q=e^{2\pi i/r}.$$
Let $\mathcal T$ be a triangulation of $M$ with vertex set $V$, edge set $E$, tetrahedra $T$. An **$r$-admissible colouring** is $c:E\to I_r=\{0,2,4,\dots,r-3\}$ (even colours, $SO(3)$ theory) such that each triangle's triple $(a,b,c)$ satisfies $a+b+c$ even, the triangle inequalities, and $a+b+c\le 2(r-2)$. Then
$$TV_r(M;q) \;=\; \eta_r^{\,2|V|}\sum_{c\ \text{admissible}} \ \prod_{e\in E} |e|_{c(e)} \ \prod_{T} \left|\begin{matrix} c_1 & c_2 & c_3\\ c_4 & c_5 & c_6\end{matrix}\right|,$$
where $|e|_a = (-1)^a[a+1]$ is a quantum dimension and the tetrahedral weight is the **quantum $6j$-symbol**, a ratio of quantum factorials (Masbaum–Vogel / Kauffman–Lins normalisation). Turaev–Viro proved the sum is independent of $\mathcal T$ (Pachner moves), giving a topological invariant.

**Relation to Reshetikhin–Turaev.** Roberts and Benedetti–Petronio proved the Turaev–Walker theorem
$$TV_r(M) = \left|RT_r(M)\right|^2,$$
for closed $M$, i.e. $TV$ is the modulus-squared of the $SU(2)$ Chern–Simons partition function, hence *manifestly positive*.

**Link complements.** Detcherry–Kalfagianni–Yang (2018) proved, for $L\subset S^3$ with $n$ components and $r=2m+1$ odd,
$$TV_r\!\left(S^3\setminus L; e^{2\pi i/r}\right) \;=\; \eta_r^2 \sum_{1\le i_1,\dots,i_n\le m} \left|J_L(i_1,\dots,i_n)\right|^2,$$
where $J_L$ are unnormalised coloured Jones polynomials evaluated at $t=q^2=e^{4\pi i/r}$. This converts the $3$-dimensional state sum into a finite sum of squared knot polynomials and links the conjecture to the Kashaev–Murakami–Murakami volume conjecture — but at the *unusual* root $e^{4\pi i/r}$ rather than $e^{2\pi i/N}$.

**Geometric mechanism.** The asymptotics of a single $6j$-symbol at $q=e^{2\pi i/r}$ are governed, by a saddle-point/Poisson-summation analysis, by the volume of a *hyperbolic* (rather than spherical, as in Ponzano–Regge) truncated tetrahedron whose dihedral angles are determined by the colours; summing over colourings should select the complete hyperbolic structure of $M$.

## 3. History & State of the Art (SOTA)

- **1992.** Turaev and Viro define $TV_r$ from quantum $6j$-symbols (*Topology* 31); Barrett–Westbury give the general spherical-category framework.
- **1995–96.** Roberts, and Benedetti–Petronio, prove $TV_r=|RT_r|^2$.
- **1997–2001.** Kashaev's volume conjecture and its reformulation by H. Murakami–J. Murakami set the template: quantum invariants at roots of unity detecting volume.
- **2015–2018.** Q. Chen and T. Yang observe numerically that at $q=e^{2\pi i/r}$ the invariants grow exponentially with rate $\mathrm{Vol}/4\pi$, checked for the figure-eight and $5_2$ complements, many census manifolds and closed surgeries; published in *Quantum Topology* 9 (2018).
- **2018.** Detcherry–Kalfagianni–Yang prove the coloured-Jones formula above and give the first rigorous cases: the figure-eight complement $S^3\setminus 4_1$ and the Borromean rings complement.
- **2018.** Ohtsuki proves an asymptotic expansion for closed hyperbolic manifolds obtained by integral surgery along $4_1$.
- **2020–2021.** Belletti–Detcherry–Kalfagianni–Yang prove the conjecture for **fundamental shadow links** — an infinite family with arbitrarily large volume — and show stability under cabling; Detcherry–Kalfagianni relate $l_{TV}$ to the Gromov norm; Belletti's theorem on maximal volumes of hyperbolic polyhedra supplies the sharp exponential bound on $6j$-symbols.
- **2020–2023.** Wong–Yang extend to Dehn fillings of fundamental shadow links and obtain full asymptotic expansions with $1$-loop terms; Belletti–Yang develop a discrete-Fourier-transform method for "deeply truncated" tetrahedra.

## 4. Partial Results / Verified Cases

Proved (limit exists and equals $\mathrm{Vol}$):

- **$S^3\setminus 4_1$** (figure-eight, $\mathrm{Vol}=2.029883\ldots$) and the **Borromean rings complement** ($\mathrm{Vol}=2v_8=7.327\ldots$) — Detcherry–Kalfagianni–Yang 2018.
- **Fundamental shadow link complements**: complements of links in $\\#_k(S^1\times S^2)$ obtained by gluing $2k$ ideal regular octahedra in pairs; volume $2k\,v_8$, $v_8=3.66386\ldots$ — Belletti–Detcherry–Kalfagianni–Yang 2021. Every $3$-manifold is a Dehn filling of such a complement, so this family is "universal" but the filled cases are not covered.
- **Closed manifolds by integral surgery on $4_1$** with surgery coefficient $|p|\ge 5$ — Ohtsuki 2018, via full asymptotic expansion of $RT$.
- **Cablings**: if the conjecture holds for $S^3\setminus L$ it holds for its $(p,q)$-cables (BDKY 2021); also stable under connected sum and split union.
- **Dehn fillings of fundamental shadow links** with sufficiently large filling coefficients — Wong–Yang.

General structural results: $l_{TV}$ is additive under connected sums and gluings along tori; $l_{TV}(M)=0$ for manifolds with vanishing Gromov norm; and there is an upper bound of the form $l_{TV}(M)\le C\,\|M\|$ with an explicit universal constant $C$ (Detcherry–Kalfagianni 2020, using Belletti's polyhedral volume bound), so exponential growth already detects positive simplicial volume. Numerically, the conjecture has been checked for hundreds of census manifolds up to $r\approx 100$–$300$; convergence is slow, consistent with a $\tfrac{3}{2}\cdot\frac{\log r}{r}$ correction.

## 5. Principal Obstacles

- **Exponentially many terms, no cancellation control from above.** Positivity gives the lower bound cheaply *for a single dominant colouring*, but proving the upper bound requires uniform control over $\sim r^{|E|}$ summands; naive term-by-term bounds overshoot by a factor exponential in the number of tetrahedra.
- **Non-uniform saddle-point analysis.** The Poisson summation/steepest-descent argument that works for octahedral (fundamental shadow) decompositions requires an explicit potential function with a *non-degenerate* critical point in a controlled domain. For a general triangulation the potential is the sum of Neumann–Zagier-type dilogarithms, and no method guarantees that the relevant critical point is the geometric one, or that it lies on a deformable contour.
- **Degenerate and non-geometric colourings.** Colourings near the boundary of the admissibility polytope correspond to degenerate hyperbolic polyhedra where the $6j$ asymptotics change form; these contributions are hard to bound.
- **Positivity of the leading coefficient.** Even where an asymptotic expansion is obtained, one must show the $1$-loop invariant (a torsion-type quantity) is non-zero — an unresolved arithmetic issue also blocking the classical volume conjecture.
- **No topological proof of exponential growth.** Standard tools of algebraic topology and TQFT (functoriality, surgery formulas, Kauffman bracket skein theory) are *finite-dimensional linear algebra over cyclotomic fields*; they carry no analytic information about the size of matrix entries as $r\to\infty$.

## 6. The Gap

Every proven case comes with a *preferred geometric decomposition* — into ideal regular octahedra or into a single explicitly analysable surgery — for which the state sum degenerates to a one- or two-variable oscillating integral. The general conjecture asks for the same conclusion from an *arbitrary* triangulation, where the potential has as many variables as edges. The precise missing step: a uniform saddle-point theorem for the multivariable quantum $6j$ potential showing that (a) the maximum of the real part of the potential over the admissibility polytope equals $\mathrm{Vol}(M)/2$, and (b) it is attained at the colouring corresponding to the complete hyperbolic structure, with a non-degenerate Hessian. Equivalently: a "geometric convergence" statement that the discrete variational problem defined by $6j$-symbol volumes converges to the Rivin/Casson volume functional on hyperbolic structures.

## 7. Current Research (as of June 2026)

- **Asymptotic expansions with $1$-loop terms.** Wong–Yang and Ohtsuki push beyond the leading exponential to the conjectured refined form $TV_r(M)\sim C\,r^{a}e^{\,r\mathrm{Vol}/4\pi}$, identifying $C$ with adjoint Reidemeister torsion. *(frontier — verify)*
- **Discrete Fourier transform / deeply truncated tetrahedra** (Belletti–Yang, Bordeaux–Texas A&M): a uniform integral representation of $6j$-symbols valid across colouring regimes, aimed at removing the octahedral restriction.
- **Resurgence and state-integral models** (Garoufalidis–Gu–Mariño; Andersen–Kashaev's TQFT from the quantum dilogarithm): transseries for Chern–Simons partition functions that would encode all $r$-asymptotics at once.
- **Gromov-norm program** (Detcherry, Dijon; Kalfagianni, Michigan State): proving $l_{TV}(M)=v_3\|M\|$ for all $M$ — a weaker but structurally robust statement invariant under JSJ decomposition.
- **Skein-theoretic positivity** (Frohman–Kania-Bartoszyńska–Lê): unicity of skein-algebra representations at roots of unity, giving representation-theoretic sources for the exponential terms.
- **Physics input**: the $3d$–$3d$ correspondence identifies the growth rate with the $S^3_b$ partition function of $T[M]$; Gang–Yamazaki-type computations agree numerically. *(frontier — verify)*

## 8. Future Work

1. Prove the conjecture for all Dehn fillings of fundamental shadow links with *arbitrary* (not just large) coefficients — this would cover all closed hyperbolic $3$-manifolds by universality.
2. Establish the upper bound $l_{TV}(M)\le \mathrm{Vol}(M)$ in general; currently only $l_{TV}(M)\le C\|M\|$ with non-sharp $C$ is known.
3. Prove non-vanishing of the $1$-loop/torsion coefficient, giving unconditional lower bounds.
4. Extend to invariants at other roots $q=e^{2\pi i k/r}$, testing the conjectural dependence of the growth rate on $k$.
5. Develop a "quantum Mostow rigidity": show the maximiser of the discrete volume functional is unique, mirroring uniqueness of the complete structure.

## 9. Key References

- **[Foundational]** V. G. Turaev, O. Y. Viro. *State sum invariants of $3$-manifolds and quantum $6j$-symbols.* Topology 31 (1992), 865–902. [DOI](https://doi.org/10.1016/0040-9383(92)90015-a)
- **[Foundational]** J. W. Barrett, B. W. Westbury. *Invariants of piecewise-linear $3$-manifolds.* Transactions of the AMS 348 (1996), 3997–4022. [DOI](https://doi.org/10.1090/s0002-9947-96-01660-1)
- **[Foundational]** J. Roberts. *Skein theory and Turaev–Viro invariants.* Topology 34 (1995), 771–787. [DOI](https://doi.org/10.1016/0040-9383(94)00053-0)
- **[Foundational]** R. Kashaev. *The hyperbolic volume of knots from quantum dilogarithm.* Letters in Mathematical Physics 39 (1997), 269–275. [DOI](https://doi.org/10.1023/a:1007364912784)
- **[Foundational]** H. Murakami, J. Murakami. *The colored Jones polynomials and the simplicial volume of a knot.* Acta Mathematica 186 (2001), 85–104. [DOI](https://doi.org/10.1007/bf02392716)
- **[SOTA]** Q. Chen, T. Yang. *Volume conjectures for the Reshetikhin–Turaev and the Turaev–Viro invariants.* Quantum Topology 9 (2018), 419–460. [DOI](https://doi.org/10.4171/qt/111)
- **[SOTA]** R. Detcherry, E. Kalfagianni, T. Yang. *Turaev–Viro invariants, colored Jones polynomials and volume.* Quantum Topology 9 (2018), 775–813. [DOI](https://doi.org/10.4171/qt/120)
- **[SOTA]** R. Detcherry, E. Kalfagianni. *Gromov norm and Turaev–Viro invariants of $3$-manifolds.* Annales Scientifiques de l'École Normale Supérieure 53 (2020), 1363–1391. [DOI](https://doi.org/10.24033/asens.2449)
- **[SOTA]** T. Ohtsuki. *On the asymptotic expansion of the quantum $SU(2)$ invariant at $q=\exp(4\pi\sqrt{-1}/N)$ for closed hyperbolic $3$-manifolds obtained by integral surgery along the figure-eight knot.* Algebraic & Geometric Topology 18 (2018), 4187–4274. [DOI](https://doi.org/10.2140/agt.2018.18.4187)
- **[SOTA]** G. Belletti, R. Detcherry, E. Kalfagianni, T. Yang. *Growth of Turaev–Viro invariants and cabling.* Mathematical Proceedings of the Cambridge Philosophical Society 170 (2021), 625–650.
- **[SOTA]** G. Belletti. *The maximum volume of hyperbolic polyhedra.* Transactions of the AMS 374 (2021), 1125–1153. [DOI](https://doi.org/10.1090/tran/8215)
- **[Survey]** H. Murakami. *An introduction to the volume conjecture.* In *Interactions between Hyperbolic Geometry, Quantum Topology and Number Theory*, Contemporary Mathematics 541, AMS, 2011, 1–40.
- **[Survey]** T. Ohtsuki (ed.). *Problems on invariants of knots and $3$-manifolds.* Geometry & Topology Monographs 4, 2002.
- **[Background]** L. Kauffman, S. Lins. *Temperley–Lieb Recoupling Theory and Invariants of $3$-Manifolds.* Annals of Mathematics Studies 134, Princeton University Press, 1994.

## 10. Worked Example / Concrete Special Case

**Figure-eight complement at $r=5$.** Here $m=(r-1)/2=2$ and $q=e^{4\pi i/5}$ (i.e. $t=q^2$ in the coloured-Jones variable), with
$$|\eta_5|^2=\frac{4\sin^2(2\pi/5)}{5}=\frac{4(0.904508)}{5}=0.723607 .$$
Habiro's formula for the normalised coloured Jones polynomial of $4_1$:
$$J'_N(4_1;q)=\sum_{k=0}^{N-1}\prod_{j=1}^{k}\left(q^{\frac{N-j}{2}}-q^{-\frac{N-j}{2}}\right)\left(q^{\frac{N+j}{2}}-q^{-\frac{N+j}{2}}\right).$$
For $N=1$: $J'_1=1$. For $N=2$ with $q^{1/2}=e^{2\pi i/5}$, the $k=1$ term is
$$\left(e^{2\pi i/5}-e^{-2\pi i/5}\right)\left(e^{6\pi i/5}-e^{-6\pi i/5}\right)=(2i\sin\tfrac{2\pi}{5})(2i\sin\tfrac{6\pi}{5})=(1.902113i)(-1.175570i)=2.236068=\sqrt5 .$$
So $J'_2=1+\sqrt5=3.236068$. Using the Detcherry–Kalfagianni–Yang formula (unnormalised invariants differ from $J'_N$ by the quantum integer $[N]$, which is $1$ for $N=1$ and cancels in this normalisation for the leading estimate):
$$TV_5\!\left(S^3\setminus 4_1\right)\;\approx\;0.723607\left(1^2+3.236068^2\right)=0.723607\times 11.4721=8.3014 .$$
The corresponding volume estimate is
$$\frac{4\pi}{5}\log(8.3014)=2.513274\times 2.11646=5.319,$$
against $\mathrm{Vol}(S^3\setminus 4_1)=2.029883$. The estimate at $r=5$ overshoots by a factor $2.6$ — the shortfall is the $\frac{4\pi}{r}\log(\text{polynomial prefactor})$ term, which decays only like $\log r/r$. Larger $r$ improves it slowly: Chen–Yang's numerics reach agreement to two decimals only around $r\approx 150$. This is exactly the difficulty the general conjecture faces: the exponential rate is correct but is masked at every finite $r$ by sub-exponential factors, and rigorous proofs must control them uniformly over all colourings, not just the two terms visible here.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*