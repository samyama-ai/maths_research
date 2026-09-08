---
id: 04-topology/characterizing-slopes-conjecture
title: "Dehn Surgery Characterizing Slopes Conjecture"
topic: 04-topology
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Dehn Surgery Characterizing Slopes Conjecture

> **Topic:** Topology & Knot Theory · **ID:** `04-topology/characterizing-slopes-conjecture` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Let $K \subset S^3$ be a knot and $p/q \in \mathbb{Q} \cup \{1/0\}$ a slope. Write $S^3_{p/q}(K)$ for the closed oriented $3$-manifold obtained by $p/q$-Dehn surgery on $K$. The slope $p/q$ is **characterizing** for $K$ if
$$S^3_{p/q}(K) \cong S^3_{p/q}(K') \ \text{(orientation-preserving homeomorphism)} \implies K' = K \ \text{(isotopy in } S^3).$$

The problem cluster known as the *characterizing slopes conjecture* asks how large the set of non-characterizing slopes can be. The current working form:

> **Conjecture.** For every knot $K \subset S^3$ there is a constant $C(K)$ such that every slope $p/q$ with $|q| \ge C(K)$ is characterizing for $K$. Conjecturally one may take $C(K) = 3$ — i.e. **every slope $p/q$ with $|q| \ge 3$ is characterizing for every knot.**

Two historically prior statements bracket this. (i) *Every* slope is characterizing for the unknot (Gordon, Kirby Problem 1.81) — now a theorem. (ii) *All but finitely many* slopes are characterizing for every knot — now **false** (Baker–Motegi 2018). A complete resolution means either proving the $|q| \ge C(K)$ statement for all knots (open for satellites in general), or exhibiting a knot with non-characterizing slopes of arbitrarily large $q$.

## 2. Mathematical Foundations

**Dehn surgery.** For $K \subset S^3$ with tubular neighbourhood $N(K)$, the exterior is $E_K = S^3 \setminus \mathrm{int}\,N(K)$. Fix the standard meridian–longitude basis $(\mu,\lambda)$ of $H_1(\partial E_K) \cong \mathbb{Z}^2$ with $\lambda$ the Seifert-framed longitude. The slope $p/q$ is the isotopy class of the essential simple closed curve $p\mu + q\lambda$, $\gcd(p,q)=1$. Then
$$S^3_{p/q}(K) = E_K \cup_\varphi (S^1 \times D^2), \qquad \varphi(\partial D^2) = p\mu + q\lambda .$$
Homology: $H_1(S^3_{p/q}(K)) \cong \mathbb{Z}/p\mathbb{Z}$, independent of $K$; so $|p|$ is not itself an invariant separating knots.

**Why the question is nontrivial.** Gordon–Luecke (1989) proved knots are determined by their *complements*: $E_K \cong E_{K'}$ implies $K = K'$. Characterizing slopes ask the strictly harder question after the complement has been filled in, where the filling can forget the surgery torus.

**Heegaard Floer input.** For $p/q > 0$ the rational surgery formula of Ozsváth–Szabó computes $\widehat{HF}(S^3_{p/q}(K))$ from the knot Floer complex $CFK^\infty(K)$, with
$$\operatorname{rk} \widehat{HF}\big(S^3_{p/q}(K)\big) \; \ge \; |p| ,$$
equality defining an **L-space**. The correction terms satisfy
$$d\big(S^3_{p/q}(K), i\big) \;=\; d\big(S^3_{p/q}(U), i\big) \;-\; 2\max\{V_{\lfloor i/q \rfloor},\, V_{\lceil (p-i)/q \rceil}\},$$
where $V_j \in \mathbb{Z}_{\ge 0}$ is the non-increasing sequence of local $h$-invariants of $K$, with $V_j = 0$ for $j \ge g(K)$ and $V_0 \ge \lceil \tau(K)/2 \rceil$-type lower bounds. Knot Floer homology detects genus ($\max\{i : \widehat{HFK}(K,i) \ne 0\} = g(K)$) and fiberedness (Ni), which is what converts Floer coincidences into knot-theoretic conclusions.

**Geometric input.** By Thurston's hyperbolic Dehn surgery theorem, for hyperbolic $E_K$ all but finitely many fillings are hyperbolic, and $\mathrm{vol}(S^3_{p/q}(K)) \nearrow \mathrm{vol}(E_K)$ as $|p|+|q| \to \infty$, with geodesic core length $\ell(p/q) \to 0$ at rate $O(1/(p^2+q^2))$. Filling with large $q$ forces the core curve to be the *unique* shortest geodesic, which is what makes the surgery torus recoverable.

## 3. History & State of the Art (SOTA)

- **1976–1980.** Lickorish and Brakes give the first examples of distinct knots with homeomorphic surgeries, showing not all slopes are characterizing.
- **1990.** Gordon's Problem 1.81 in Kirby's list asks which manifolds arise from surgery on more than one knot; the unknot case ("is every slope characterizing for $U$?") becomes the benchmark.
- **2007.** Kronheimer–Mrowka–Ozsváth–Szabó, *Monopoles and lens space surgeries*: if $S^3_{p}(K) \cong L(p,1)$ for integral $p$, then $K = U$. Every integral slope is characterizing for the unknot.
- **2007–2008.** Ni's fiberedness detection and Ghiggini's genus-one fibred detection theorem supply the tools for the trefoils and figure-eight.
- **2011.** Ozsváth–Szabó's rational surgery formula extends the unknot result to all rational slopes, and yields that **every** slope is characterizing for $U$, $T_{2,3}$, $T_{2,-3}$ and $4_1$.
- **2014.** Ni–Zhang and McCoy give the first infinite families of non-integral characterizing slopes for torus knots.
- **2018.** Baker–Motegi construct hyperbolic knots with **infinitely many** non-characterizing integral slopes, refuting the "all but finitely many" form and forcing the conjecture to be stated in terms of $q$.
- **2019.** Lackenby, *Every knot has characterising slopes*: for any $K$, $p/q$ is characterizing whenever $q \ge 3$ and $|p| + q$ is sufficiently large. This is the structural SOTA for general knots.
- **2022–2025.** Sorya proves the full $|q| \ge C(K)$ statement for hyperbolic knots and torus knots, and extends to large classes of satellites; the general satellite case remains the live frontier.

## 4. Partial Results / Verified Cases

| Class | Result |
|---|---|
| Unknot $U$ | **All** slopes $p/q$ characterizing (KMOS 2007 integral; Ozsváth–Szabó 2011 rational). |
| $T_{2,3}$, $T_{2,-3}$, $4_1$ | **All** slopes characterizing (Ozsváth–Szabó 2011, with Ghiggini/Ni detection). |
| Torus knots $T_{r,s}$ | All $p/q$ with $q \ge 2$ and $p/q$ above an explicit genus-linear bound; for $T_{5,2}$ every $p/q$ with $q \ge 2$, $p/q \ge 43/2$ (Ni–Zhang 2014). Non-integral slopes with $q \ge 3$ handled broadly by McCoy. |
| Arbitrary $K$ | $p/q$ characterizing if $q \ge 3$ and $|p|+q \gg 0$ (Lackenby 2019); effective versions in terms of genus and hyperbolic volume by McCoy. |
| Hyperbolic and torus knots | $\exists\, C(K)$ with all $p/q$, $|q| \ge C(K)$, characterizing (Sorya). |
| Small knots ($\le 5$ crossings) | Case-by-case Floer verification, including $5_2$; slope $0$ characterizing for many genus-one knots. |
| Counterexamples | Slope $0$ non-characterizing for infinitely many knots (Osoinach's annulus twists, Abe–Jong–Omae–Takeuchi); infinitely many non-characterizing **integers** for some hyperbolic knots (Baker–Motegi 2018). Every known non-characterizing slope has $|q| \le 2$. |

## 5. Principal Obstacles

- **Gauge-theoretic invariants are $q$-blind in the wrong way.** The surgery formulas determine $\widehat{HF}(S^3_{p/q}(K))$ from $CFK^\infty(K)$, but $CFK^\infty$ does not determine $K$. Floer coincidences pin down $g(K)$, $\tau(K)$, fiberedness and $\Delta_K(t)$ — not the isotopy class — so Floer alone can never close the conjecture beyond classes where these invariants are complete (unknot, trefoils, $4_1$, some L-space knots).
- **Non-effective geometry.** Lackenby's argument uses a geometric limiting/compactness step (thin position, Gromov–Hausdorff-type convergence of filled manifolds): it yields "sufficiently large $|p|+q$" without a computable threshold for a given $K$, so no finite check reduces a specific knot to a finite verification.
- **Annulus twisting defeats slope-by-slope arguments.** Osoinach–Baker–Motegi families produce infinitely many knots sharing one filled manifold by twisting along an annulus whose boundary slope is the surgery slope. The construction is intrinsically $q \in \{0,1,2\}$; there is no known mechanism to push it to $q \ge 3$, but also no proof that none exists.
- **Satellites break both toolkits.** For a satellite $K$ the exterior is not hyperbolic, so Thurston's rigidity/volume control fails; and the JSJ pieces of $S^3_{p/q}(K)$ can be reassembled in ways that hide the surgery torus. Floer invariants of satellites are governed by the companion and pattern in a way that loses the pattern's embedding data.
- **Cosmetic-surgery-type degeneracies.** Distinguishing $S^3_{p/q}(K)$ from $S^3_{p/q}(K')$ up to *orientation-preserving* homeomorphism requires invariants sensitive to orientation ($d$-invariants, Casson–Walker); unoriented invariants systematically fail.

## 6. The Gap

Proven: for hyperbolic and torus knots, and for all knots once $q \ge 3$ *and* $|p|$ is large in a non-effective sense. Conjectured: $|q| \ge 3$ alone suffices, for every knot.

Two precise gaps remain.

1. **The satellite gap.** Establish $C(K) < \infty$ for every satellite knot. This needs a JSJ-level uniqueness statement: if $S^3_{p/q}(K) \cong S^3_{p/q}(K')$ with $q$ large, the two surgery solid tori must be isotopic inside a common JSJ piece. No analogue of Thurston's rigidity is available for the Seifert-fibred and graph pieces.
2. **The effectivity gap.** Replace Lackenby's "$|p|+q$ sufficiently large" by a bound $f(g(K), \mathrm{vol}(E_K))$, and then remove the $|p|$ condition entirely, so that $q \ge 3$ suffices with no constraint on $p$. Equivalently: rule out a knot admitting non-characterizing slopes $p_n/q_n$ with $q_n \ge 3$ and $|p_n| \to \infty$.

## 7. Current Research (as of June 2026)

- **Sorya's programme (UQAM/McGill, Montreal).** Slope-uniform statements: a constant $C(K)$ depending only on coarse geometric data, with current work extending from hyperbolic and torus knots to satellites via JSJ induction on the companion tree. *(frontier — verify)*
- **Instanton and Khovanov detection (Baldwin–Sivek, Boston College/Princeton).** Using $SU(2)$ representation-theoretic detection theorems to settle characterizing-slope statements for individual small knots such as $5_2$, where Heegaard Floer is insufficient. *(frontier — verify)*
- **Effective Lackenby bounds (McCoy, Toronto/UQAM).** Converting the compactness step into explicit genus- and volume-dependent thresholds, aiming at "$q \ge 3$ and $p/q \ge \lambda g(K)$".
- **Constructions of non-characterizing slopes (Baker, Motegi, Miami/Nihon).** Systematic search for twisting operations realizing $q \ge 3$; a single example would refute the $C(K)=3$ form.
- **Census computation.** SnapPy/Regina verification of characterizing behaviour for knots up to 15 crossings against surgery-census manifolds, used to test whether $|q| \le 2$ really bounds all counterexamples.

## 8. Future Work

- Prove a **JSJ rigidity lemma**: for $q \ge 3$, the surgery solid torus in $S^3_{p/q}(K)$ is determined up to isotopy by the manifold, for satellite $K$.
- Make Lackenby's theorem effective and drop the dependence on $|p|$; a stated target is "every $p/q$ with $q \ge 3$ is characterizing for every hyperbolic knot".
- Determine whether $C(K) = 3$ can fail: search for annulus- or Seifert-fibred-based constructions with $q \ge 3$.
- Settle slope $0$ for genus-one knots and for fibred knots, where Floer detection is strongest.
- Extend detection theorems (instanton, Khovanov, $\mathrm{SL}(2,\mathbb{C})$ character varieties) to more knots, converting "every slope is characterizing" from a class statement into a per-knot certificate.

## 9. Key References

- **[Foundational]** C. McA. Gordon and J. Luecke. *Knots are determined by their complements.* Journal of the American Mathematical Society 2 (1989), 371–415.
- **[Foundational]** R. Kirby (ed.). *Problems in low-dimensional topology.* In: Geometric Topology (AMS/IP Stud. Adv. Math. 2.2), American Mathematical Society, 1997. (Problem 1.81.)
- **[Foundational]** P. Kronheimer, T. Mrowka, P. Ozsváth and Z. Szabó. *Monopoles and lens space surgeries.* Annals of Mathematics 165 (2007), 457–546.
- **[Foundational]** P. Ozsváth and Z. Szabó. *Knot Floer homology and rational surgeries.* Algebraic & Geometric Topology 11 (2011), 1–68.
- **[Foundational]** Y. Ni. *Knot Floer homology detects fibred knots.* Inventiones Mathematicae 170 (2007), 577–608.
- **[Foundational]** P. Ghiggini. *Knot Floer homology detects genus-one fibred knots.* American Journal of Mathematics 130 (2008), 1151–1169.
- **[SOTA]** M. Lackenby. *Every knot has characterising slopes.* Mathematische Annalen 374 (2019), 429–446.
- **[SOTA]** K. L. Baker and K. Motegi. *Noncharacterizing slopes for hyperbolic knots.* Algebraic & Geometric Topology 18 (2018), 1461–1480.
- **[SOTA]** Y. Ni and X. Zhang. *Characterizing slopes for torus knots.* Algebraic & Geometric Topology 14 (2014), 1249–1274.
- **[SOTA]** D. McCoy. *Non-integer characterizing slopes for torus knots.* Communications in Analysis and Geometry, 2020.
- **[SOTA]** F. Gainullin. *Heegaard Floer homology and knots determined by their complements.* Algebraic & Geometric Topology 18 (2018), 69–109.
- **[Foundational]** J. K. Osoinach. *Manifolds obtained by surgery on an infinite number of knots in $S^3$.* Topology 45 (2006), 725–733.
- **[Survey]** J. Hom. *A survey on Heegaard Floer homology and concordance.* Journal of Knot Theory and Its Ramifications 26 (2017), 1740015.
- **[Survey]** S. Boyer. *Dehn surgery on knots.* In: Handbook of Geometric Topology, North-Holland, 2002.

## 10. Worked Example / Concrete Special Case

**Claim:** slope $5$ is characterizing for the unknot $U$; the right-handed trefoil $T_{2,3}$ is the sharpest near-miss.

$S^3_5(U) = L(5,1)$. By Moser's classification of torus-knot surgeries, $S^3_{rs\pm1}(T_{r,s})$ is a lens space; for $T_{2,3}$ and slope $5 = 2\cdot3 - 1$,
$$S^3_5(T_{2,3}) \;\cong\; L(5,4) \;\cong\; -L(5,1).$$
So $T_{2,3}$ produces the *orientation-reversed* copy: not a counterexample, but it shows the orientation convention in §1 is essential — drop it and slope $5$ would already fail.

**Why no knot other than $U$ gives $L(5,1)$.** Suppose $S^3_5(K) \cong L(5,1)$.

1. $|H_1| = 5$ is automatic, so homology gives nothing.
2. $L(5,1)$ is an L-space: $\operatorname{rk}\widehat{HF} = 5 = |p|$. By the surgery formula this forces $K$ to be an **L-space knot**, so $\Delta_K(t) = \sum_{k=0}^{2n}(-1)^k t^{a_k}$ with strictly decreasing exponents, and $CFK^\infty(K)$ is a staircase complex determined by $\Delta_K$.
3. Lens space surgery requires $p \ge 2g(K)-1$, so $g(K) \le 3$.
4. Compare correction terms. With $q=1$ the formula reads $d(S^3_5(K),i) = d(L(5,1),i) - 2V_{\min\{i,\,5-i\}}$. Since $S^3_5(K) \cong L(5,1)$ orientation-preservingly, the $\mathrm{Spin}^c$-graded $d$-invariants agree, hence $V_i = 0$ for all $i \ge 0$, in particular $V_0 = 0$.
5. For an L-space knot $V_0 = 0$ forces $g(K) = 0$: L-space knots have $V_0 \ge \lceil g(K)/2 \rceil > 0$ when $g(K) > 0$. Since knot Floer homology detects genus, $g(K)=0$ gives $K = U$. $\square$

**Contrast — a non-characterizing slope.** Take $q = 0$. Osoinach's annulus twist takes a knot $K$ bounding a Seifert surface meeting a suitable annulus $A$ with $\partial A$ of slope $0$; twisting along $A$ produces knots $K_n$, pairwise distinct, with
$$S^3_0(K_n) \cong S^3_0(K_0) \quad \text{for all } n \in \mathbb{Z}.$$
The twist changes the knot in $S^3$ but is realized by a homeomorphism of the $0$-filled manifold. Baker–Motegi upgrade this to integral slopes on a hyperbolic knot. Every such construction has $|q| \le 2$ — exactly the gap the conjecture asserts is real.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*