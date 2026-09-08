---
id: 03-geometry/deligne-conjecture-local-systems
title: "Deligne's Conjecture on the Semisimplicity of Local Systems"
topic: 03-geometry
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Deligne's Conjecture on the Semisimplicity of Local Systems

> **Topic:** Algebraic & Differential Geometry · **ID:** `03-geometry/deligne-conjecture-local-systems` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

The name attaches to a cluster of statements asserting that local systems arising in algebraic geometry are *semisimple* — direct sums of irreducibles — and that irreducible ones are automatically as rigid, pure and motivic as if they came from a family of varieties. Two are designated here.

**(A) Arithmetic form (Deligne, *Weil II* 1.2.10).** Let $X$ be a normal connected scheme of finite type over $\mathbb{F}_q$, $\ell \nmid q$, and let $\mathcal{F}$ be an irreducible lisse $\overline{\mathbb{Q}}_\ell$-sheaf on $X$ of rank $r$ with finite determinant. Then:

1. $\mathcal{F}$ is $\iota$-pure of weight $0$;
2. the coefficients of the local factors $\det(1 - F_x t \mid \mathcal{F})^{-1}$ are algebraic over $\mathbb{Q}$;
3. they lie in a single number field $E$ independent of $x$;
4. their $\lambda$-adic valuations are bounded ($\ell'$-integrality for all $\ell' \neq p$);
5. for every place $\lambda' \nmid p$ of $E$ there is an $\lambda'$-companion $\mathcal{F}_{\lambda'}$ with matching characteristic polynomials, and likewise a *crystalline* (p-adic) companion.

Part (1) combined with *Weil II* Thm. 3.4.1(iii) forces $\mathcal{F}|_{X \otimes \overline{\mathbb{F}}_q}$ to be **semisimple**: arithmetic irreducibility propagates to geometric semisimplicity.

**(B) Complex/motivic form.** Every irreducible rigid local system on a smooth quasi-projective complex variety $X$ is *of geometric origin* — a subquotient of $R^i f_* \mathbb{C}$ for some smooth family $f: Y \to U \subseteq X$ — hence underlies a polarizable variation of Hodge structure and is semisimple with quasi-unipotent, integral monodromy.

A complete proof must supply (A)(1)–(5) for arbitrary normal $X$ over $\mathbb{F}_q$, including non-smooth $X$ and $p$-adic companions, and (B) beyond the cohomologically rigid, $\mathrm{SL}_2$, and one-dimensional-base cases. A disproof would exhibit an irreducible lisse sheaf with finite determinant that is not pure, or a rigid local system with non-integral traces.

## 2. Mathematical Foundations

**Local systems.** For $X$ a connected scheme, a lisse $\overline{\mathbb{Q}}_\ell$-sheaf of rank $r$ is a continuous representation
$$\rho: \pi_1(X, \bar{x}) \longrightarrow \mathrm{GL}_r(\overline{\mathbb{Q}}_\ell).$$
When $X/\mathbb{F}_q$ there is the exact sequence
$$1 \to \pi_1(X \otimes \overline{\mathbb{F}}_q, \bar{x}) \to \pi_1(X,\bar{x}) \to \mathrm{Gal}(\overline{\mathbb{F}}_q/\mathbb{F}_q) = \widehat{\mathbb{Z}} \to 1,$$
so "arithmetically irreducible" ($\rho$ irreducible) is weaker than "geometrically semisimple" ($\rho|_{\pi_1^{\mathrm{geom}}}$ semisimple). The gap is exactly what purity closes.

**Weights.** Fix $\iota: \overline{\mathbb{Q}}_\ell \hookrightarrow \mathbb{C}$. $\mathcal{F}$ is $\iota$-pure of weight $w$ if for every closed point $x \in |X|$ with residue field $\mathbb{F}_{q_x}$, every eigenvalue $\alpha$ of the geometric Frobenius $F_x$ on $\mathcal{F}_{\bar{x}}$ satisfies
$$|\iota(\alpha)| = q_x^{w/2}.$$

**Semisimplicity from purity (Deligne, *Weil II* 3.4.1(iii)).** If $\mathcal{F}$ is lisse and $\iota$-pure on $X$ smooth over $\mathbb{F}_q$, then $\mathcal{F}|_{X\otimes\overline{\mathbb{F}}_q}$ is semisimple. Proof mechanism: $\mathrm{End}(\mathcal{F})$ is pure of weight $0$, and any $\pi_1^{\mathrm{geom}}$-subobject would produce a Frobenius-invariant idempotent in $H^0(X\otimes\overline{\mathbb{F}}_q, \mathcal{E}nd(\mathcal{F}))$, which the weight-monodromy bookkeeping supplies.

**Companions.** Two lisse sheaves $\mathcal{F}_\lambda, \mathcal{F}_{\lambda'}$ over $E$ are companions if for all $x \in |X|$,
$$\det(1 - F_x t \mid \mathcal{F}_\lambda) = \det(1 - F_x t \mid \mathcal{F}_{\lambda'}) \in E[t].$$
The $p$-adic slot is filled not by an étale sheaf but by an **overconvergent $F$-isocrystal** on $X/W(\mathbb{F}_q)$, with $L$-function matching.

**Complex side.** Over $\mathbb{C}$, the Riemann–Hilbert correspondence identifies local systems with regular singular flat connections $(\mathcal{E}, \nabla)$, $\nabla^2 = 0$. Corlette–Simpson nonabelian Hodge theory gives, for $X$ smooth projective, a homeomorphism
$$M_{\mathrm{B}}(X, r) \;\cong\; M_{\mathrm{Dol}}(X, r), \qquad (E,\theta),\ \theta\wedge\theta = 0,$$
between the character variety of semisimple rank-$r$ representations and moduli of semistable Higgs bundles with vanishing Chern classes. A local system is **rigid** if it is an isolated point of $M_{\mathrm{B}}$; **cohomologically rigid** if $H^1(X, \mathcal{E}nd(\mathcal{E})) = 0$.

**Deligne's theorem (1968/1971).** For $f: Y \to X$ smooth projective over $\mathbb{C}$, $R^i f_* \mathbb{Q}$ is a semisimple local system and the Leray spectral sequence degenerates at $E_2$. This is the model case the conjectures generalize.

## 3. History & State of the Art (SOTA)

- **1968–1971.** Deligne proves $E_2$-degeneration and semisimplicity of $R^i f_*\mathbb{Q}$ for smooth projective families (*Publ. IHÉS* 35, 40), using hard Lefschetz and the Hodge-theoretic decomposition.
- **1980.** *La conjecture de Weil II* (*Publ. IHÉS* 52). Theorem 3.4.1 establishes purity-implies-semisimplicity; Conjecture 1.2.10 states (A)(1)–(5).
- **1982.** Beĭlinson–Bernstein–Deligne–Gabber, *Faisceaux pervers*: the decomposition theorem, semisimplicity for pure perverse sheaves.
- **1987.** Deligne, *Un théorème de finitude pour la monodromie*: finiteness of local systems with bounded ramification and given rank — the structural finiteness underlying (3).
- **1988–1992.** Corlette and Simpson build nonabelian Hodge theory; Simpson conjectures that rigid local systems are motivic.
- **1996.** Katz, *Rigid Local Systems*: complete classification and middle-convolution algorithm for rigid local systems on $\mathbb{P}^1 \setminus S$; all are motivic there.
- **2002.** L. Lafforgue proves the Langlands correspondence for $\mathrm{GL}_r$ over function fields (*Invent. Math.* 147), settling (A)(1)–(5) for **smooth curves** over $\mathbb{F}_q$.
- **2012.** Deligne (*Moscow Math. J.* 12, 497–514) proves (2),(3),(4) for arbitrary normal $X$ over $\mathbb{F}_q$; Drinfeld (same issue, 515–542) deduces existence of $\ell'$-companions for **smooth** $X$ of any dimension by a curve-gluing argument.
- **2018–2022.** Abe (*JAMS* 31) proves the $p$-adic Langlands correspondence for curves, giving crystalline companions on curves; Abe–Esnault (*Ann. Sci. ÉNS* 52, 2019) and Kedlaya (*EPIGA*, 2022/2024) extend to smooth varieties.

**SOTA summary.** (A) is a theorem for $X$ smooth over $\mathbb{F}_q$, in all dimensions and for all companion places including $p$. It remains open for general normal (non-smooth) $X$, and the $p$-adic case leans on resolution-type inputs. (B) is open in general.

## 4. Partial Results / Verified Cases

| Case | Status | Source |
|---|---|---|
| $X$ smooth curve over $\mathbb{F}_q$, any rank $r$ | (1)–(5) proven | L. Lafforgue 2002; Abe 2018 ($p$-adic) |
| $X$ smooth over $\mathbb{F}_q$, $\dim \geq 2$, $\ell' \neq p$ | companions exist | Drinfeld 2012 |
| $X$ smooth over $\mathbb{F}_q$, crystalline companion | proven | Abe–Esnault 2019; Kedlaya 2022 |
| $X$ normal, non-smooth | (2),(3),(4) proven; (5) open | Deligne 2012 |
| Rank $1$ (any $X$) | classical, via class field theory | — |
| $f$ smooth projective over $\mathbb{C}$: $R^if_*\mathbb{Q}$ | semisimple | Deligne 1968, 1971 |
| Rigid local systems on $\mathbb{P}^1 \setminus \{s_1,\dots,s_n\}$ | all motivic | Katz 1996 |
| Cohomologically rigid, $X$ smooth projective$/\mathbb{C}$ | integral (traces are algebraic integers) | Esnault–Groechenig, *Selecta Math.* 24 (2018) |
| Cohomologically rigid with finite determinant | underlie $F$-isocrystals in char $p$ reduction | Esnault–Groechenig, *Acta Math.* 225 (2020) |
| Rank $2$, quasi-unipotent, $X$ a curve | motivic in many families | Katz; Corlette–Simpson, *Compositio* 144 (2008) |
| $\mathrm{SL}_2(\mathbb{C})$ rank-2 rigid, any smooth quasi-proj. $X$ | motivic (of geometric origin) | Corlette–Simpson 2008 |

## 5. Principal Obstacles

- **No Langlands correspondence above dimension 1.** Every proof of purity for higher-dimensional $X$ routes through curves. That works for pointwise statements (weights, traces), but any statement genuinely about $\pi_1(X)$ — e.g. semisimplicity of a *non-pure* sheaf, or companions on a singular $X$ — cannot be assembled from curve data without a gluing theorem. Drinfeld's gluing needs $X$ smooth to control ramification along a normal crossings boundary; on a singular normal $X$ there is no such boundary model.
- **Wild ramification.** Over $\mathbb{C}$ regular singularities are automatic in the relevant category; in characteristic $p$, Swan conductors are unbounded, and finiteness statements (Deligne 1987) require an a priori ramification bound. Removing that bound is not a technical nuisance: rank is not enough to bound wildness.
- **The $p$-adic slot is not a sheaf category.** Overconvergent $F$-isocrystals lack a $\pi_1$-description; there is no étale descent, and extending an isocrystal from an open subset to a compactification is a genuinely open problem (semistable reduction for isocrystals, Kedlaya). Statements provable by "restrict to a curve, glue" for $\ell \neq p$ have no direct analogue.
- **Nonabelian Hodge theory is analytic, not motivic.** Corlette–Simpson produces a variation of Hodge structure on a rigid local system, hence a Hodge filtration and semisimplicity — but a VHS is not a family of varieties. Bridging VHS $\Rightarrow$ geometric origin needs an unproved Hodge-theoretic converse (essentially the Hodge conjecture-level input of constructing algebraic cycles/families from Hodge data).
- **Rigid $\neq$ cohomologically rigid.** All current integrality proofs use $H^1(X,\mathcal{E}nd) = 0$ to run a Frobenius-fixed-point argument on the moduli space. Rigid-but-not-cohomologically-rigid points (non-reduced isolated points of $M_{\mathrm{B}}$) are not known to exist, and are not covered.

## 6. The Gap

Two precise boundaries.

**Arithmetic.** Proven: $X$ smooth over $\mathbb{F}_q$ $\Rightarrow$ (1)–(5). Missing: for $X$ normal but singular, the existence of $\ell'$- and crystalline companions, i.e. Drinfeld's descent without smoothness. The obstruction is that the gluing argument needs, for each pair of curves meeting in $X$, a compatible tame/wild structure at the boundary; on a singular $X$ the local fundamental groups at singular points are not controlled by any known finiteness theorem.

**Complex.** Proven: cohomologically rigid $\Rightarrow$ integral traces, $\Rightarrow$ $F$-isocrystal structure mod $p$. Missing: the implication
$$\text{integral} + \text{VHS} \;\Longrightarrow\; \text{subquotient of } R^i f_*\mathbb{C}.$$
No mechanism currently converts a $\mathbb{Z}$-structure plus Hodge filtration into an algebraic family. This is the same wall as the Hodge conjecture in the absolute case.

## 7. Current Research (as of June 2026)

- **Esnault (Copenhagen/Berlin) and Groechenig (Toronto)**: companions and integrality; extending the $F$-isocrystal method to non-cohomologically-rigid systems and to the "arithmetic" $\pi_1$ constraints (density of geometric points in character varieties). Esnault's 2023 Springer lecture notes *Local Systems in Algebraic-Arithmetic Geometry* is the standard synthesis.
- **Kedlaya (UCSD)**: *Étale and crystalline companions II* and the semistable-reduction program for overconvergent isocrystals; the current bottleneck for removing smoothness hypotheses.
- **Abe (Tokyo IPMU)**: $p$-adic cohomological Langlands, arithmetic $\mathcal{D}$-modules, six-functor formalism for isocrystals.
- **Drinfeld (Chicago)** and de Jong's conjecture circle: finiteness of representations of arithmetic fundamental groups, $\pi_1$ of varieties over $\overline{\mathbb{F}}_p$.
- **Landesman–Litt (Stanford/Brown)**: canonical representations and non-abelian Hodge theory for local systems on surfaces; results bounding low-rank local systems on curves with finite mapping-class-group orbits, tightly connected to rigidity conjectures. *(frontier — verify current preprint status)*
- **Klevdal–Patrikis**: motivicity of Shimura-variety local systems; arithmetic descent of companions. *(frontier — verify)*

## 8. Future Work

- Prove semistable reduction for overconvergent $F$-isocrystals in dimension $\geq 3$; this is the identified single input that would extend crystalline companions to normal singular $X$.
- Develop a companion formalism intrinsic to $\pi_1(X)$ rather than to $|X|$, so that statements survive without curve-by-curve reduction.
- Attack rigid $\Rightarrow$ cohomologically rigid, or produce a counterexample; either resolves a clean structural question in $M_{\mathrm{B}}(X,r)$.
- Use the $p$-adic companion of a rigid complex local system to construct the conjectural motive by $p$-adic interpolation over varying $p$ (Esnault–Groechenig's stated strategy).
- Extend integrality from cohomologically rigid to *arithmetic* local systems: those whose $\mathrm{Gal}(\overline{\mathbb{Q}}/\mathbb{Q})$-orbit is finite.

## 9. Key References

- **[Foundational]** P. Deligne. *Théorème de Lefschetz et critères de dégénérescence de suites spectrales.* Publ. Math. IHÉS 35 (1968), 259–278.
- **[Foundational]** P. Deligne. *Théorie de Hodge II.* Publ. Math. IHÉS 40 (1971), 5–57.
- **[Foundational]** P. Deligne. *La conjecture de Weil II.* Publ. Math. IHÉS 52 (1980), 137–252. (Conjecture 1.2.10; Théorème 3.4.1.)
- **[Foundational]** P. Deligne. *Un théorème de finitude pour la monodromie.* In *Discrete Groups in Geometry and Analysis*, Progr. Math. 67, Birkhäuser, 1987, 1–19.
- **[Foundational]** A. Beĭlinson, J. Bernstein, P. Deligne. *Faisceaux pervers.* Astérisque 100, Soc. Math. France, 1982.
- **[SOTA]** L. Lafforgue. *Chtoucas de Drinfeld et correspondance de Langlands.* Invent. Math. 147 (2002), 1–241.
- **[SOTA]** P. Deligne. *Finitude de l'extension de $\mathbb{Q}$ engendrée par des traces de Frobenius, en caractéristique finie.* Moscow Math. J. 12 (2012), 497–514.
- **[SOTA]** V. Drinfeld. *On a conjecture of Deligne.* Moscow Math. J. 12 (2012), 515–542.
- **[SOTA]** T. Abe. *Langlands correspondence for isocrystals and the existence of crystalline companions for curves.* J. Amer. Math. Soc. 31 (2018), 921–1057.
- **[SOTA]** T. Abe, H. Esnault. *A Lefschetz theorem for overconvergent isocrystals with Frobenius structure.* Ann. Sci. Éc. Norm. Supér. 52 (2019), 1243–1264.
- **[SOTA]** K. S. Kedlaya. *Étale and crystalline companions, I.* Épijournal de Géométrie Algébrique 6 (2022), Article 20.
- **[SOTA]** H. Esnault, M. Groechenig. *Cohomologically rigid local systems and integrality.* Selecta Math. (N.S.) 24 (2018), 4279–4292.
- **[SOTA]** H. Esnault, M. Groechenig. *Rigid connections and $F$-isocrystals.* Acta Math. 225 (2020), 103–158.
- **[Foundational]** C. Simpson. *Higgs bundles and local systems.* Publ. Math. IHÉS 75 (1992), 5–95.
- **[Foundational]** K. Corlette. *Flat $G$-bundles with canonical metrics.* J. Differential Geom. 28 (1988), 361–382.
- **[Survey]** N. Katz. *Rigid Local Systems.* Annals of Mathematics Studies 139, Princeton Univ. Press, 1996.
- **[Survey]** H. Esnault. *Local Systems in Algebraic-Arithmetic Geometry.* Lecture Notes in Mathematics 2337, Springer, 2023.
- **[Related]** K. Corlette, C. Simpson. *On the classification of rank-two representations of quasiprojective fundamental groups.* Compositio Math. 144 (2008), 1271–1331.

## 10. Worked Example / Concrete Special Case

**The Legendre family over $\mathbb{P}^1_{\mathbb{F}_q} \setminus \{0,1,\infty\}$, $p > 2$.**

Let $U = \mathbb{P}^1 \setminus \{0,1,\infty\}$ over $\mathbb{F}_q$ and let $f: \mathcal{E} \to U$ be the Legendre elliptic curve
$$E_\lambda: \; y^2 = x(x-1)(x-\lambda).$$
Set $\mathcal{F} = R^1 f_* \overline{\mathbb{Q}}_\ell$, a lisse sheaf of rank $2$.

**Step 1 — traces.** For a closed point $\lambda \in |U|$ with residue field $\mathbb{F}_{q_\lambda}$,
$$\mathrm{tr}(F_\lambda \mid \mathcal{F}) = a_\lambda = q_\lambda + 1 - \\#E_\lambda(\mathbb{F}_{q_\lambda}).$$
Concretely over $\mathbb{F}_5$, $\lambda = 2$: counting affine points of $y^2 = x(x-1)(x-2)$ gives $4$ affine points plus the point at infinity, so $\\#E_2(\mathbb{F}_5) = 5$ and $a_2 = 5 + 1 - 5 = 1$.

**Step 2 — purity, verified.** Hasse's bound gives $|a_\lambda| \le 2\sqrt{q_\lambda}$; here $|1| \le 2\sqrt5 \approx 4.47$. Since $\det \mathcal{F} = \overline{\mathbb{Q}}_\ell(-1)$ has Frobenius eigenvalue $q_\lambda$, the two eigenvalues $\alpha,\bar\alpha$ satisfy $\alpha\bar\alpha = q_\lambda$ and $|\alpha| \le 2\sqrt{q_\lambda}$, forcing
$$|\iota(\alpha)| = q_\lambda^{1/2}.$$
So $\mathcal{F}$ is pure of weight $1$. After the Tate twist $\mathcal{F}(1/2)$ (or passing to $\mathcal{F} \otimes \overline{\mathbb{Q}}_\ell(1/2)$) the determinant is finite and the weight is $0$: exactly the hypotheses of (A).

**Step 3 — geometric semisimplicity, verified directly.** The local monodromy at $\lambda = 0$ and $\lambda = 1$ is unipotent nontrivial ($\begin{psmallmatrix}1&1\\0&1\end{psmallmatrix}$ in a suitable basis), and at $\infty$ it is $-\begin{psmallmatrix}1&2\\0&1\end{psmallmatrix}$ up to conjugacy. A rank-$2$ representation with a nontrivial unipotent has at most one invariant line; two unipotents at $0$ and $1$ with distinct fixed lines leave no common invariant line, so $\mathcal{F}|_{U \otimes \overline{\mathbb{F}}_q}$ is irreducible, hence semisimple. Igusa's theorem identifies the geometric monodromy image as all of $\mathrm{SL}_2(\mathbb{Z}_\ell)$. This is the conclusion *Weil II* 3.4.1(iii) predicts from Step 2 — here obtained independently, which is why the example is a check rather than an application.

**Step 4 — companions, made explicit.** The trace field is $E = \mathbb{Q}$: every $a_\lambda \in \mathbb{Z}$, confirming (2),(3),(4) with $\lambda$-integrality from $|a_\lambda| \le 2\sqrt{q_\lambda}$. For each $\ell' \neq p$ the companion is $R^1f_*\overline{\mathbb{Q}}_{\ell'}$ — same $L$-factors by the Weil conjectures for curves. The crystalline companion is $R^1 f_{*,\mathrm{rig}} \mathcal{O}$, the relative rigid cohomology $F$-isocrystal, with unit-root part of rank $1$ over the ordinary locus and slopes $\{0,1\}$ there, slopes $\{1/2,1/2\}$ at supersingular $\lambda$ (e.g. $\lambda$ a root of the Hasse polynomial $H_p(\lambda)$; for $p=5$, $H_5(\lambda) = \lambda^2 - \lambda + \tfrac{1}{4}$-type, giving $\lambda = 3$ in $\mathbb{F}_5$ where $a_\lambda = 0$).

**What the example does not settle.** Here geometric origin is given by construction. The conjecture asserts the converse for an *arbitrary* irreducible lisse rank-$2$ sheaf on $U$ with finite determinant — one handed over as a representation of $\pi_1(U)$ with no family attached. Purity, and hence semisimplicity, must then be extracted from automorphic input (Lafforgue) rather than from Hasse's bound.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*