---
id: 05-analysis/shafarevich-holomorphic-convexity
title: "Shafarevich Holomorphic Convexity"
topic: 05-analysis
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Shafarevich Holomorphic Convexity Conjecture

> **Topic:** Real & Complex Analysis · **ID:** `05-analysis/shafarevich-holomorphic-convexity` · **Status:** partially-solved (open in general)

## 1. Problem Statement / Conjecture

**Conjecture (Shafarevich).** Let $X$ be a smooth connected complex projective variety and let $\widetilde X \to X$ be its universal covering, equipped with the induced complex structure. Then $\widetilde X$ is **holomorphically convex**: for every compact $K \subset \widetilde X$, the holomorphic hull
$$\widehat K \;=\; \bigl\{\, y \in \widetilde X \;:\; |f(y)| \le \sup_K |f| \ \ \forall f \in \mathcal O(\widetilde X) \,\bigr\}$$
is compact.

Two standard variants are usually treated together:

* **Kähler version.** The same statement with $X$ a compact Kähler manifold.
* **Galois version.** For every normal subgroup $N \trianglelefteq \pi_1(X)$, the covering $X_N = \widetilde X / N$ is holomorphically convex. (The universal cover is the case $N = 1$; the conjecture is *not* known to be equivalent to the general case.)

A proof must produce, for each compact $K$, a plurisubharmonic exhaustion controlling $\widehat K$ — equivalently (Remmert), a proper surjective holomorphic map $\widetilde X \to S$ onto a Stein space. A disproof must exhibit a projective $X$ whose universal cover carries so few global holomorphic functions that some hull is non-compact — e.g. an infinite nested chain of compact analytic subsets, or a cover on which $\mathcal O(\widetilde X) = \mathbb C$ while $\widetilde X$ is non-compact.

Status: proved for all coverings attached to **linear** representations of $\pi_1(X)$ (Eyssidieux–Katzarkov–Pantev–Ramachandran, 2012); open for general $\pi_1$, in particular for non-residually-finite and non-linear Kähler groups.

## 2. Mathematical Foundations

**Holomorphic convexity and Remmert reduction.** A complex space $Y$ is holomorphically convex iff there exists a proper surjective holomorphic map with connected fibres $r : Y \to S$ onto a normal Stein space $S$ with $r_*\mathcal O_Y = \mathcal O_S$ (the *Cartan–Remmert reduction*). $Y$ is Stein iff it is holomorphically convex and holomorphically separable. Holomorphic convexity forces the set of positive-dimensional compact analytic subsets of $Y$ to be "finite-dimensionally organised": each is contained in a fibre of $r$.

**Shafarevich / $\Gamma$-reduction.** Kollár and Campana constructed independently, for $X$ smooth projective, an almost-holomorphic dominant rational map
$$\operatorname{sh}_X : X \dashrightarrow \mathrm{Sh}(X)$$
onto a normal projective variety, unique up to birational equivalence, characterised by: for a very general irreducible subvariety $Z \subset X$ with normalisation $\widetilde Z$,
$$\operatorname{sh}_X(Z) = \text{point} \iff \operatorname{im}\bigl(\pi_1(\widetilde Z) \to \pi_1(X)\bigr) \ \text{is finite.}$$
The number $\gamma(X) = \dim \mathrm{Sh}(X)$ is the *$\Gamma$-dimension*. $X$ has **generically large fundamental group** iff $\gamma(X) = \dim X$. If $\widetilde X$ is holomorphically convex, its Remmert reduction $\widetilde X \to \mathrm{Sh}(\widetilde X)$ is the lift of $\operatorname{sh}_X$; conversely the conjecture asserts that this rational, purely topological construction is realised by an honest proper holomorphic map upstairs.

**Analytic machinery.**
* $L^2$ theory on covers: for $(X,\omega)$ projective with $L$ ample, Hörmander/Andreotti–Vesentini estimates on $\widetilde X$ give $L^2$ holomorphic sections of $\pi^*L^{\otimes m}$, and Atiyah's $L^2$-index theorem gives $\chi_{(2)}$ and von Neumann dimensions $\dim_{\pi_1(X)} H^0_{(2)}$.
* Non-abelian Hodge theory: for reductive $\rho : \pi_1(X) \to GL_n(\mathbb C)$, Corlette–Simpson attach a harmonic metric and a Higgs bundle $(E,\theta)$ with $\theta \wedge \theta = 0$; the *spectral cover* / Higgs foliation produces multivalued psh functions $\int |\theta|$ that descend to exhaustions.
* Harmonic maps to buildings (Gromov–Schoen) handle representations into $GL_n(K)$ for $K$ non-archimedean, giving the "unbounded / non-rigid" directions.

**Key equivalence used throughout.** A connected complex manifold $Y$ with a psh exhaustion $\varphi$ that is strictly psh outside a compact-fibred proper map is holomorphically convex; conversely, holomorphic convexity of a Galois cover $X_N$ implies that $N$ contains no "non-residually-detectable" loops shrinking along an infinite chain of subvarieties.

## 3. History & State of the Art

* **1972.** I. R. Shafarevich raises the question in *Basic Algebraic Geometry*, asking whether $\widetilde X$ is always holomorphically convex, motivated by uniformisation in dimension $1$ and by the hope of a "Stein-fication" of covers.
* **1990.** T. Napier (*Math. Ann.* 286) develops convexity criteria for coverings of projective varieties via psh exhaustions and $L^2$ methods; establishes the first non-trivial families.
* **1993–95.** Kollár and Campana construct the Shafarevich map / $\Gamma$-reduction, giving the conjecture its precise structural target. Kollár's book *Shafarevich Maps and Automorphic Forms* (1995) is the standard reference.
* **1993.** Toledo constructs smooth projective varieties with **non-residually finite** $\pi_1$, killing the naive strategy "approximate $\widetilde X$ by finite covers".
* **1995–98.** Napier–Ramachandran ($L^2$ $\bar\partial$-methods, weak Lefschetz); Katzarkov–Ramachandran settle large classes of surfaces; Bogomolov–Katzarkov propose candidate counterexamples built from Lefschetz pencils with prescribed monodromy.
* **1997–2004.** Katzarkov (rank-one and "large" representations), then Eyssidieux (*Invent. Math.* 156, 2004): the covering attached to a **reductive** linear representation is holomorphically convex.
* **2012.** Eyssidieux, Katzarkov, Pantev, Ramachandran, *Linear Shafarevich conjecture* (*Ann. of Math.* 176): the full linear case, including non-reductive representations, via mixed Hodge / Katzarkov–Zuo theory and Gromov–Schoen buildings.
* **2013–2026.** Extensions to quasi-projective and orbifold settings, positive-characteristic representation groups, and hyperbolicity consequences (Campana–Claudon–Eyssidieux; Brunebarbe; Deng–Yamanoi).

## 4. Partial Results / Verified Cases

| Case | Result |
|---|---|
| $\dim_{\mathbb C} X = 1$ | Trivial: uniformisation gives $\widetilde X \in \{\mathbb P^1, \mathbb C, \mathbb D\}$, all holomorphically convex. |
| $\pi_1(X)$ finite | $\widetilde X$ compact, hence trivially holomorphically convex. |
| $\pi_1(X)$ abelian / virtually nilpotent | Follows from linearity (Mal'cev: f.g. nilpotent groups embed in $GL_n(\mathbb Z)$) plus EKPR; for abelian varieties directly, $\widetilde X = \mathbb C^g$ is Stein. |
| $\rho : \pi_1(X) \to GL_n(\mathbb C)$ **reductive** | Eyssidieux (2004): $X_{\ker\rho}$ is holomorphically convex. |
| $\rho : \pi_1(X) \to GL_n(\mathbb C)$ **arbitrary** | EKPR (*Annals*, 2012): $X_{\ker\rho}$ is holomorphically convex. Hence the full conjecture holds whenever $\pi_1(X)$ is **linear** (admits a faithful finite-dimensional representation over $\mathbb C$), e.g. lattices in semisimple Lie groups, surface groups, f.g. nilpotent and polycyclic groups. |
| $\gamma(X) = 0$ | $\pi_1(X)$ is finite for very general subvarieties; $\widetilde X$ compact-modulo-nothing, conjecture reduces to the finite case. |
| $\gamma(X) = 1$ | Known: the Shafarevich map is a fibration onto a curve and $\widetilde X \to \widetilde{\mathrm{Sh}}$ is proper (Kollár; Campana). |
| Surfaces ($\dim X = 2$) with $\pi_1(X)$ surjecting onto a genus-$\ge 2$ curve group | Katzarkov–Ramachandran (*Ann. Sci. ÉNS* 31, 1998). |
| $X$ with $\pi_1(X)$ residually finite and generically large, in dimension $\le 2$ | Established by combining Napier's exhaustions with the $\Gamma$-reduction. |
| $\widetilde X$ quasi-projective | Claudon–Höring–Kollár (*Crelle* 679, 2013) classify such $X$: up to finite étale cover, $X$ is a fibration in abelian-variety-like factors over a variety with Stein cover. |

## 5. Principal Obstacles

* **Non-linear Kähler groups.** All complete results route through a representation $\rho$ into $GL_n$ of some field. A group with no infinite linear quotient (or none detecting the relevant subvarieties) leaves the machinery with nothing to act on. No general construction of "enough" representations from a Kähler group is known.
* **Failure of residual finiteness.** Toledo's examples mean $\widetilde X$ cannot be approximated by finite covers; $L^2$ sections that separate points on all finite covers need not separate on $\widetilde X$.
* **Positivity is only asymptotic.** $L^2$ estimates on $\widetilde X$ produce sections of $\pi^*L^{\otimes m}$, but $\pi^* L$ has *no* curvature-positivity relative to the ends of $\widetilde X$; the Andreotti–Vesentini argument yields $L^2$ functions with no control on where hulls escape. Non-vanishing of $\dim_{\pi_1} H^0_{(2)}$ does not imply base-point freeness on the cover.
* **Infinite chains of compact subvarieties.** The only known obstruction mechanism: an infinite strictly-increasing chain of compact analytic subsets of $\widetilde X$ would break convexity. Ruling this out requires bounding the "size" of $\pi_1$-images of subvarieties — precisely what the Shafarevich map is designed to record, but the map is only *birational* and almost-holomorphic, so its lift is a priori non-proper over the indeterminacy locus.
* **Non-Kähler transfer fails.** $\partial\bar\partial$-lemma and harmonic-map rigidity inputs (Siu, Corlette, Gromov–Schoen) are Kähler-specific, so no analogue exists to test the conjecture in a larger class.

## 6. The Gap

Proven: for any $\rho : \pi_1(X) \to GL_n(K)$, the covering $X_{\ker\rho}$ is holomorphically convex, and its Remmert reduction realises the $\rho$-Shafarevich map. The general conjecture is the case $N = 1$, i.e. the intersection $\bigcap_\rho \ker \rho$ over all linear $\rho$ must be trivial — the **linear residual finiteness** of $\pi_1(X)$. The exact step to cross:

> Given $X$ projective with $\Gamma = \pi_1(X)$ and $\Gamma^{\mathrm{lin}} = \bigcap_{\rho \text{ linear}} \ker\rho \ne 1$, show that the intermediate cover $\widetilde X \to X_{\Gamma^{\mathrm{lin}}}$ is proper, or produce independently a psh exhaustion on $\widetilde X$.

Equivalently: prove that no smooth projective $X$ admits an infinite chain $Z_1 \subsetneq Z_2 \subsetneq \cdots$ of compact analytic subsets of $\widetilde X$ with $\bigcup Z_i$ non-compact and unbounded hull. Every known technique gives *some* linear invariant; none gives the whole of $\Gamma$.

## 7. Current Research (as of June 2026)

* **Positive-characteristic and non-archimedean representations.** Deng–Yamanoi, *Linear Shafarevich conjecture in positive characteristic, hyperbolicity and applications* (arXiv, 2024) extends EKPR to $\rho : \pi_1(X) \to GL_n(K)$ for $K$ of arbitrary characteristic and derives hyperbolicity: varieties with generically large linear $\pi_1$ are of general type and Brody hyperbolic modulo a divisor *(frontier — verify)*.
* **Quasi-projective / orbifold Shafarevich.** Brunebarbe, Campana–Claudon–Eyssidieux: convexity of covers of quasi-projective varieties with linear monodromy; the correct statement requires the Cartan–Remmert reduction to be Stein *modulo* the boundary orbifold structure *(frontier — verify)*.
* **Hodge-theoretic school (Green–Griffiths–Katzarkov).** Realising the Shafarevich map by period maps of variations of Hodge structure and their degenerations.
* **Group-theoretic side.** Structural results on Kähler groups (Delzant–Gromov cuts, Py, Llosa Isenrich) narrow the class of possible non-linear Kähler groups; a Kähler group with trivial linear quotient would be the natural counterexample source.
* **Candidate counterexamples.** The Bogomolov–Katzarkov surfaces remain unresolved: no proof of convexity, no proof of failure.

Active groups: Grenoble (Eyssidieux), Miami/Katzarkov, CNRS-Nancy (Deng), Nantes (Claudon), Osaka (Yamanoi), Chicago/Princeton (Kollár's circle).

## 8. Future Work

* Prove convexity for coverings attached to representations into infinite-dimensional groups or into $\mathrm{Homeo}^+(S^1)$ / mapping class groups, where non-linear Kähler groups first appear.
* Develop an $L^2$-theory of holomorphic functions on covers with von Neumann dimension bookkeeping strong enough to separate points without residual finiteness.
* Decide the Bogomolov–Katzarkov candidates: compute the $\Gamma$-reduction of their Lefschetz-pencil surfaces explicitly.
* Settle the Kähler (non-projective) case, where even the linear result is not fully documented.
* Prove or refute: every Kähler group is *linear-residually-finite*. A counterexample here would not disprove the conjecture but would remove the only known route to it.

## 9. Key References

- **[Foundational]** I. R. Shafarevich. *Basic Algebraic Geometry.* Springer, 1974 (Russian original 1972) — statement of the problem.
- **[Foundational]** T. Napier. *Convexity properties of coverings of smooth projective varieties.* Mathematische Annalen 286 (1990), 433–479. [DOI](https://doi.org/10.1007/bf01453583)
- **[Foundational]** J. Kollár. *Shafarevich Maps and Automorphic Forms.* Princeton University Press, 1995.
- **[Foundational]** F. Campana. *Remarques sur le revêtement universel des variétés kählériennes compactes.* Bulletin de la SMF 122 (1994), 255–284. [DOI](https://doi.org/10.24033/bsmf.2232)
- **[Foundational]** D. Toledo. *Projective varieties with non-residually finite fundamental group.* Publications Mathématiques de l'IHÉS 77 (1993), 103–119. [DOI](https://doi.org/10.1007/bf02699189)
- **[SOTA]** P. Eyssidieux, L. Katzarkov, T. Pantev, M. Ramachandran. *Linear Shafarevich conjecture.* Annals of Mathematics 176 (2012), 1545–1581. [DOI](https://doi.org/10.4007/annals.2012.176.3.4)
- **[SOTA]** P. Eyssidieux. *Sur la convexité holomorphe des revêtements linéaires réductifs d'une variété projective algébrique complexe.* Inventiones Mathematicae 156 (2004), 503–564. [DOI](https://doi.org/10.1007/s00222-003-0345-0)
- **[SOTA]** B. Claudon, A. Höring, J. Kollár. *Algebraic varieties with quasi-projective universal cover.* Journal für die reine und angewandte Mathematik 679 (2013), 207–221. [DOI](https://doi.org/10.1515/crelle.2012.017)
- **[Recent]** F. Campana, B. Claudon, P. Eyssidieux. *Représentations linéaires des groupes kählériens: factorisations et applications.* American Journal of Mathematics 137 (2015), 1091–1130.
- **[Partial results]** L. Katzarkov, M. Ramachandran. *On the universal coverings of algebraic surfaces.* Annales Scientifiques de l'ÉNS 31 (1998), 525–535. [DOI](https://doi.org/10.1016/s0012-9593(98)80105-5)
- **[Partial results]** T. Napier, M. Ramachandran. *Structure theorems for complete Kähler manifolds and applications to Lefschetz type theorems.* GAFA 5 (1995), 809–851. [DOI](https://doi.org/10.1007/bf01897052)
- **[Candidate counterexamples]** F. Bogomolov, L. Katzarkov. *Complex projective surfaces and infinite groups.* GAFA 8 (1998), 243–272. [DOI](https://doi.org/10.1007/s000390050055)
- **[Technique]** M. Gromov, R. Schoen. *Harmonic maps into singular spaces and $p$-adic superrigidity for lattices in groups of rank one.* Publ. IHÉS 76 (1992), 165–246.
- **[Survey]** P. Eyssidieux. *Lectures on the Shafarevich conjecture on uniformization.* In: Complex Manifolds, Foliations and Uniformization, Panoramas et Synthèses 34/35, SMF, 2011.

## 10. Worked Example / Concrete Special Case

Take $X = C \times \mathbb P^1$ with $C$ a smooth projective curve of genus $g = 2$. This is the smallest instance where the universal cover is **neither compact nor Stein**, so the Remmert reduction is genuinely non-trivial.

**Step 1 — the cover.** $\pi_1(X) = \pi_1(C) \times \pi_1(\mathbb P^1) = \Gamma_2$, the genus-2 surface group. By uniformisation $\widetilde C = \mathbb D$, so
$$\widetilde X \;=\; \mathbb D \times \mathbb P^1, \qquad \Gamma_2 \curvearrowright \mathbb D \ \text{by Möbius transformations, trivially on } \mathbb P^1 .$$

**Step 2 — the function algebra.** Since $\mathbb P^1$ is compact and connected, $\mathcal O(\mathbb D \times \mathbb P^1) = \mathcal O(\mathbb D) \otimes \mathcal O(\mathbb P^1) = \mathcal O(\mathbb D)$: every global holomorphic function is $f(z,w) = f(z)$. So $\widetilde X$ is **not** holomorphically separable (points on a fibre $\{z\}\times\mathbb P^1$ are indistinguishable) and hence not Stein.

**Step 3 — convexity check.** Let $K \subset \mathbb D\times \mathbb P^1$ be compact and $p = \mathrm{pr}_1(K) \subset \mathbb D$, compact. For $(z,w) \in \widehat K$ and any $f \in \mathcal O(\mathbb D)$ we need $|f(z)| \le \sup_p |f|$, i.e. $z \in \widehat p^{\,\mathcal O(\mathbb D)} = \widehat p$. Because $\mathbb D$ is Stein, $\widehat p$ is compact. Hence
$$\widehat K \subseteq \widehat p \times \mathbb P^1,$$
a compact set, and $\widehat K$ is closed, so compact. **$\widetilde X$ is holomorphically convex.**

**Step 4 — explicit exhaustion.** $\varphi(z,w) = -\log(1-|z|^2)$ is psh on $\widetilde X$, exhausts modulo the $\mathbb P^1$-fibres, and is strictly psh in the $z$-direction: $\partial\bar\partial \varphi = \frac{dz\wedge d\bar z}{(1-|z|^2)^2} \ge 0$, the Poincaré metric pulled back.

**Step 5 — Remmert reduction = lifted Shafarevich map.** The reduction is $r = \mathrm{pr}_1 : \mathbb D \times \mathbb P^1 \to \mathbb D$: proper, surjective, connected fibres $\cong \mathbb P^1$, target Stein. Downstairs, $\operatorname{sh}_X : X \to C$ is the first projection: a very general subvariety $Z \subset X$ has finite $\pi_1$-image in $\Gamma_2$ exactly when $Z$ lies in a fibre $\{c\}\times\mathbb P^1$ (whose $\pi_1$ is trivial). So $\gamma(X) = 1$, matching $\dim \mathbb D = 1$, and $r$ is the lift of $\operatorname{sh}_X$ — exactly the structure the conjecture predicts in general.

**Why the general case is harder.** Here the fibres of $\operatorname{sh}_X$ are a genuine holomorphic fibration and $\pi_1(X)$ is linear (surface groups embed in $SL_2(\mathbb R)$), so EKPR applies. In the open case, $\operatorname{sh}_X$ is only *almost*-holomorphic, its indeterminacy locus can meet the non-compact directions of $\widetilde X$, and there is no representation to build $\varphi$ from.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*