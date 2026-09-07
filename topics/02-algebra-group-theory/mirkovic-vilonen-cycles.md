---
id: 02-algebra-group-theory/mirkovic-vilonen-cycles
title: "Mirkovic-Vilonen Cycles"
topic: 02-algebra-group-theory
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Mirkovic-Vilonen Cycles

> **Topic:** Algebra & Group Theory · **ID:** `02-algebra-group-theory/mirkovic-vilonen-cycles` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

Mirković–Vilonen (MV) cycles are the irreducible components of intersections of Schubert cells with semi-infinite orbits in the affine Grassmannian. Under geometric Satake they index bases of every weight space of every irreducible representation of the Langlands dual group, and — passing to the stable limit — a basis $\{b_Z\}$ of the coordinate ring $\mathbb{C}[N]$ of a maximal unipotent subgroup, the **MV basis**.

The central conjecture, due to Anderson and to Kamnitzer, was:

> **(MV = canonical)** The MV basis of $\mathbb{C}[N]$ coincides with Lusztig's dual canonical basis, and with Lusztig's dual semicanonical basis.

**Status.** Resolved **negatively** by Baumann, Kamnitzer and Knutson (*Acta Mathematica* 227, 2021): in type $A_5$ the MV basis differs from the dual semicanonical basis. The proof introduces a strictly finer invariant of an MV cycle than its polytope — the Duistermaat–Heckman (DH) measure — and exhibits two cycles which the polytope cannot separate but the measure can.

What remains open, and is the live form of the problem:

1. Is the MV basis independent of the choices made to define it (the pinning, the point $0 \in \mathbb{P}^1$, the identification of $\mathbb{C}[N]$ with the stable limit)? Partial dependence results are known; the general answer is not.
2. Classify MV cycles with a fixed polytope, i.e. describe the fibres of $Z \mapsto P(Z)$ as moduli.
3. Do the structure constants of the MV basis lie in $\mathbb{Z}_{\ge 0}$?

A complete resolution of (1) means either a canonical construction free of choices, or an explicit pair of choices producing different bases.

## 2. Mathematical Foundations

Let $G$ be a connected reductive group over $\mathbb{C}$ with maximal torus $T$, Borel $B = TN$, opposite $B^- = TN^-$, coweight lattice $X_*(T)$, and Langlands dual $G^\vee$. Put $\mathcal{K} = \mathbb{C}((t))$, $\mathcal{O} = \mathbb{C}[[t]]$ and

$$\mathrm{Gr} \;=\; G(\mathcal{K})/G(\mathcal{O}), \qquad \mathrm{Gr} \;=\; \bigsqcup_{\lambda \in X_*(T)^+} \mathrm{Gr}^\lambda, \quad \mathrm{Gr}^\lambda = G(\mathcal{O})\cdot t^\lambda ,$$

with $\dim \mathrm{Gr}^\lambda = \langle 2\rho, \lambda\rangle$. The **semi-infinite orbits** are

$$S_\mu = N(\mathcal{K})\cdot t^\mu, \qquad S^-_\mu = N^-(\mathcal{K})\cdot t^\mu, \qquad \mu \in X_*(T).$$

**Dimension formula (Mirković–Vilonen).** For $\mu \le \lambda$,

$$\dim\left( \mathrm{Gr}^\lambda \cap S_\mu \right) \;=\; \langle \rho, \lambda + \mu \rangle .$$

**Definition.** An **MV cycle of coweight $(\lambda,\mu)$** is an irreducible component of $\overline{\mathrm{Gr}^\lambda} \cap S_\mu$; write $\mathcal{Z}(\lambda)_\mu$ for this set. A **stable MV cycle** is an irreducible component of $\overline{S_\nu} \cap S^-_\mu$, obtained as $\lambda \to \infty$.

**Geometric Satake (Lusztig, Ginzburg, Beilinson–Drinfeld, Mirković–Vilonen).** The category $\mathrm{Perv}_{G(\mathcal{O})}(\mathrm{Gr})$ with convolution is tensor-equivalent to $\mathrm{Rep}(G^\vee)$, the fibre functor being $F = \bigoplus_\mu H^{\langle 2\rho,\mu\rangle}_c(S_\mu, -)$. Applying this to $\mathrm{IC}_\lambda$:

$$V(\lambda)_\mu \;\cong\; H^{\langle 2\rho, \mu\rangle}_c\!\left( S_\mu \cap \overline{\mathrm{Gr}^\lambda}, \mathbb{C} \right),$$

which has as basis the fundamental classes $[Z]$, $Z \in \mathcal{Z}(\lambda)_\mu$. In particular $\dim V(\lambda)_\mu = \\#\mathcal{Z}(\lambda)_\mu$.

**MV polytopes.** Intersect with all $N^-_w$-orbits: the GGMS stratum data of $Z$ gives, via the moment map for the $T$-action,

$$P(Z) \;=\; \mathrm{Conv}\left\{ \mu_w(Z) : w \in W \right\} \subset X_*(T)\otimes\mathbb{R}, \qquad \mu_w(Z) = \text{the } w\text{-extreme coweight of } Z .$$

Kamnitzer showed the collection $M_\bullet = (M_\gamma)_\gamma$ of support numbers of $P(Z)$ satisfies the **tropical Plücker relations**

$$M_{w\gamma} + M_{ws_i\gamma} \;=\; \max\left( M_{w\gamma'} + M_{ws_i\gamma''},\; M_{w\gamma''} + M_{ws_i\gamma'} \right),$$

and that polytopes so defined ("MV polytopes", equivalently BZ data) carry a crystal structure isomorphic to $B(\infty)$; edge lengths along a reduced word $\underline{w_0}$ recover Lusztig data.

**MV basis.** Stable MV cycles $\mathcal{Z}$ are indexed by $B(\infty)$; the classes $b_Z \in \mathbb{C}[N]$ obtained from $\mathbb{C}[N] = \varinjlim_\lambda V(\lambda)^*$ form the MV basis.

**DH measure.** For a $T$-stable cycle $Z$ of dimension $d$, the equivariant multiplicity / DH measure $\mathrm{DH}(Z)$ is a piecewise-polynomial measure on $X_*(T)\otimes \mathbb{R}$ with $\mathrm{supp}\,\mathrm{DH}(Z) = P(Z)$ and total mass $\deg Z$. It is a strictly finer invariant than $P(Z)$.

## 3. History & State of the Art (SOTA)

- **1983.** Lusztig computes IC stalks on $\mathrm{Gr}$ and relates them to $q$-analogues of weight multiplicities (Kostka–Foulkes), the first appearance of the geometry.
- **1995–2001.** Ginzburg, and Beilinson–Drinfeld, formulate the Satake equivalence; Mirković–Vilonen supply the semi-infinite orbits and the dimension estimate that makes the fibre functor weight-graded.
- **2003.** Anderson introduces MV polytopes and the "polytope calculus", conjecturing MV cycles are governed by their moment polytopes and asking whether the resulting basis is canonical.
- **2005.** Gaussent–Littelmann give a gallery model for MV cycles, linking them to Littelmann paths.
- **2007.** Mirković–Vilonen publish the equivalence over arbitrary commutative rings (*Annals* 166), the definitive reference.
- **2007–2010.** Kamnitzer classifies MV polytopes by tropical Plücker relations, puts a $B(\infty)$-crystal structure on them, and shows every MV cycle is the closure of a single GGMS stratum.
- **2012–2014.** Baumann–Kamnitzer identify MV polytopes with Harder–Narasimhan polytopes of preprojective algebra modules; Baumann–Kamnitzer–Tingley extend the theory to affine type via KLR algebras.
- **2021 (SOTA).** Baumann–Kamnitzer–Knutson, *The Mirković–Vilonen basis and Duistermaat–Heckman measures* (*Acta Math.* 227), with an appendix by Dranowski, Kamnitzer, Morton-Ferguson: DH measures are constructed as a basis-independent invariant, a "measure" refinement of the polytope crystal is built, and **MV $\ne$ dual semicanonical in type $A_5$** is proved.

## 4. Partial Results / Verified Cases

- **Rank 1 ($SL_2$, $PGL_2$).** All MV cycles are Schubert-type; $Z \mapsto P(Z)$ is a bijection onto segments; MV = canonical = semicanonical basis (divided powers).
- **Rank 2 ($A_2$, $B_2$, $G_2$).** Polytopes are complete invariants; the MV basis agrees with the dual canonical basis. In $A_2$ the $6$ MV polytopes of weight $\alpha_1+\alpha_2$ reproduce the two-dimensional space $\mathbb{C}[N]_{\alpha_1+\alpha_2}$.
- **Types $A_n$, $n \le 4$, and $D_4$.** The MV basis coincides with the dual semicanonical basis (BKK 2021); no separation of cycles by DH measure occurs below rank 5.
- **Type $A_5$.** The first discrepancy: the Kashiwara–Saito singular point in Lusztig's nilpotent variety produces two objects with equal MV polytope but distinct DH measures; the MV and dual semicanonical bases differ there.
- **Cominuscule / minuscule $\lambda$.** $\overline{\mathrm{Gr}^\lambda}$ is smooth, all MV cycles are torus-fixed-point closures of Schubert cells, and everything is combinatorially explicit.
- **Affine type $A_1^{(1)}$ and symmetric affine types.** Baumann–Kamnitzer–Tingley construct affine MV polytopes and prove the crystal isomorphism $B(\infty)$, including imaginary-root decorations.

## 5. Principal Obstacles

- **The polytope loses information.** $P(Z)$ records only the moment image. Two MV cycles can have identical polytopes yet different degrees, singularities, and DH measures. All combinatorial models (BZ data, Lusztig data, galleries, preprojective modules) factor through the polytope, so they cannot, on their own, distinguish such cycles.
- **Fibres of $Z \mapsto P(Z)$ are moduli, not finite sets.** Beyond low rank, cycles with a fixed polytope form positive-dimensional families. There is no known parameter space with a modular interpretation, so counting arguments fail.
- **Non-transversality.** $\overline{\mathrm{Gr}^\lambda} \cap S_\mu$ is not a transverse intersection of smooth things; its components are typically singular and not normal, so intersection-theoretic and equivariant-localisation formulas require case-by-case resolutions.
- **No cluster or bar-involution characterisation.** The dual canonical basis is pinned down by a bar involution plus a triangularity condition; the MV basis has no known analogue. Consequently there is no axiomatic uniqueness statement to compare against.
- **Choice-dependence is invisible to the combinatorics.** The construction fixes a pinning and a point on the curve; the crystal structure is insensitive to these, so combinatorial evidence cannot certify independence.
- **Fusion is hard to compute.** Multiplication in $\mathbb{C}[N]$ corresponds to degeneration in the Beilinson–Drinfeld Grassmannian; flat limits of products of cycles are computable only in small examples.

## 6. The Gap

Section 4 settles comparison of bases in ranks $\le 4$ and refutes it at rank 5. The residual gap is structural: **there is no invariant known to be complete for MV cycles.** DH measures separate strictly more cycles than polytopes but are not proved to be a complete invariant; the exact statement "$\mathrm{DH}(Z) = \mathrm{DH}(Z') \Rightarrow Z = Z'$" is open even in type $A_5$. Crossing the gap requires either (i) a moduli-theoretic description of $\{Z : P(Z) = P\}$ for arbitrary $P$, or (ii) a characterisation of the MV basis by intrinsic axioms (positivity, integrality, a bar-type involution) strong enough to prove or disprove independence of the pinning.

## 7. Current Research (as of June 2026)

- **Measure-theoretic refinements.** Extending BKK's DH-measure crystal to affine and Kac–Moody types; computing measures via equivariant multiplicities of quiver-variety components. Groups at Toronto/Perimeter, IMJ-PRG (Paris), and Cornell.
- **Computation of fusion.** Dranowski–Kamnitzer–Morton-Ferguson compute products of MV cycles by degeneration in the Beilinson–Drinfeld Grassmannian, giving structure constants in low rank; positivity holds in every computed case. *(frontier — verify: no general positivity proof.)*
- **Symplectic duality.** MV cycles as components of Lagrangians in Coulomb-branch/BFN presentations, aiming at a categorification where cycles with equal polytopes become distinguishable objects. *(frontier — verify.)*
- **Cluster comparison.** Relating the MV basis to the theta / generic bases of $\mathbb{C}[N]$ arising from cluster structures (Gross–Hacking–Keel–Kontsevich, Geiß–Leclerc–Schröer); the $A_5$ discrepancy suggests MV sits with the generic basis rather than the dual canonical one. *(frontier — verify.)*
- **$p$-adic and integral aspects.** MV cycles over $\mathbb{Z}$ and mod-$p$ Satake, where the polytope-to-cycle failure interacts with torsion in IC stalks.

## 8. Future Work

- Prove or refute that DH measures separate MV cycles; if not, find the next invariant (e.g. full equivariant cohomology class, or the cycle's IC stalk data).
- Give a modular description of the fibres of the polytope map, presumably as quiver-variety strata.
- Settle positivity of MV structure constants; a geometric proof would come from a flat family with reduced special fibre.
- Determine whether the MV basis depends on the pinning — the most explicit remaining question, and one that a single rank-5 or rank-6 computation could decide.
- Extend the affine MV polytope theory (BKT) to non-symmetric affine types and to double affine settings.

## 9. Key References

- **[Foundational]** I. Mirković, K. Vilonen. *Geometric Langlands duality and representations of algebraic groups over commutative rings.* Annals of Mathematics **166** (2007), 95–143.
- **[Foundational]** G. Lusztig. *Singularities, character formulas, and a $q$-analog of weight multiplicities.* Astérisque **101–102** (1983), 208–229.
- **[Foundational]** V. Ginzburg. *Perverse sheaves on a loop group and Langlands' duality.* Preprint, alg-geom/9511007, 1995.
- **[Foundational]** J. Anderson. *A polytope calculus for semisimple groups.* Duke Mathematical Journal **116** (2003), 567–588.
- **[Structural]** J. Kamnitzer. *Mirković–Vilonen cycles and polytopes.* Annals of Mathematics **171** (2010), 245–294.
- **[Structural]** J. Kamnitzer. *The crystal structure on the set of Mirković–Vilonen polytopes.* Advances in Mathematics **215** (2007), 66–93.
- **[Structural]** A. Braverman, D. Gaitsgory. *Crystals via the affine Grassmannian.* Duke Mathematical Journal **107** (2001), 561–575.
- **[Structural]** S. Gaussent, P. Littelmann. *LS galleries, the path model, and MV cycles.* Duke Mathematical Journal **127** (2005), 35–88.
- **[Structural]** P. Baumann, J. Kamnitzer. *Preprojective algebras and MV polytopes.* Representation Theory **16** (2012), 152–188.
- **[SOTA / Recent]** P. Baumann, J. Kamnitzer, A. Knutson. *The Mirković–Vilonen basis and Duistermaat–Heckman measures.* Acta Mathematica **227** (2021), 1–101. (With an appendix by A. Dranowski, J. Kamnitzer, C. Morton-Ferguson.)
- **[SOTA / Recent]** P. Baumann, J. Kamnitzer, P. Tingley. *Affine Mirković–Vilonen polytopes.* Publications mathématiques de l'IHÉS **120** (2014), 113–205.
- **[Related]** M. Kashiwara, Y. Saito. *Geometric construction of crystal bases.* Duke Mathematical Journal **89** (1997), 9–36.
- **[Survey]** X. Zhu. *An introduction to affine Grassmannians and the geometric Satake equivalence.* In *Geometry of Moduli Spaces and Representation Theory*, IAS/Park City Mathematics Series 24, AMS, 2017.

## 10. Worked Example / Concrete Special Case

Take $G = SL_2$, so $G^\vee = PGL_2$. Write $\alpha^\vee$ for the simple coroot, $\rho$ the fundamental weight, $\langle \rho, \alpha^\vee\rangle = 1$. Choose $\lambda = \alpha^\vee$.

**The Schubert variety.** $\dim \mathrm{Gr}^{\alpha^\vee} = \langle 2\rho, \alpha^\vee\rangle = 2$, and $\overline{\mathrm{Gr}^{\alpha^\vee}} = \mathrm{Gr}^{\alpha^\vee} \sqcup \{t^0\}$ is the affine quadric cone $\{xy = z^2\} \cong \mathbb{C}^2/\{\pm 1\}$, singular exactly at $t^0$.

**Intersections with $S_\mu$.** The relevant $\mu$ are $\alpha^\vee, 0, -\alpha^\vee$, and

$$\dim\left(\mathrm{Gr}^{\alpha^\vee} \cap S_\mu\right) = \langle \rho, \alpha^\vee + \mu \rangle = \begin{cases} 2, & \mu = \alpha^\vee,\\ 1, & \mu = 0,\\ 0, & \mu = -\alpha^\vee. \end{cases}$$

Each intersection is irreducible, so there is exactly one MV cycle for each $\mu$: $Z_{\alpha^\vee} = \overline{\mathrm{Gr}^{\alpha^\vee}}$, $Z_0$ a line (the closure of a $1$-dimensional $N(\mathcal{K})$-orbit through $t^0$), $Z_{-\alpha^\vee} = \{t^{-\alpha^\vee}\}$.

**Satake check.** $\\#\mathcal{Z}(\alpha^\vee)_\mu = 1$ for each of the three weights, and $V(\alpha^\vee)$ for $PGL_2$ is the $3$-dimensional adjoint representation with weights $\{\alpha, 0, -\alpha\}$, each of multiplicity $1$. The counts match:

$$\dim V(\alpha^\vee) = \sum_\mu \\#\mathcal{Z}(\alpha^\vee)_\mu = 1+1+1 = 3 .$$

**Polytopes.** $P(Z_{\alpha^\vee}) = [-\alpha^\vee, \alpha^\vee]$, $P(Z_0) = [-\alpha^\vee, 0]$, $P(Z_{-\alpha^\vee}) = \{-\alpha^\vee\}$ — three distinct segments in $\mathbb{R}\alpha^\vee$. The map $Z \mapsto P(Z)$ is injective here, so the polytope is a complete invariant.

**DH measures.** $\mathrm{DH}(Z_{-\alpha^\vee}) = \delta_{-\alpha^\vee}$; $\mathrm{DH}(Z_0)$ is Lebesgue measure on $[-\alpha^\vee, 0]$; $\mathrm{DH}(Z_{\alpha^\vee})$ is Lebesgue measure on $[-\alpha^\vee,\alpha^\vee]$ with total mass $2 = \deg \overline{\mathrm{Gr}^{\alpha^\vee}}$ (degree of the quadric cone). No two agree, consistent with injectivity of the polytope map.

**Stable limit.** Here $N \cong \mathbb{G}_a$ with coordinate $x$, and the stable MV cycles produce $b_n = x^n/n!$, exactly the dual canonical basis of $\mathbb{C}[N] = \mathbb{C}[x]$. Structure constants $b_m b_n = \binom{m+n}{m} b_{m+n}$ are positive integers.

**What breaks at rank 5.** In type $A_5$ one finds two stable MV cycles $Z \ne Z'$ with $P(Z) = P(Z')$; the segment-style argument above has no analogue, and the polytope crystal cannot see the difference. BKK compute $\mathrm{DH}(Z) \ne \mathrm{DH}(Z')$ and use this to conclude $b_Z$ is not the corresponding dual semicanonical vector — the counterexample that changed the status of this problem from *open* to *solved-recently*.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*