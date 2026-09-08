---
id: 02-algebra-group-theory/kapovich-kleiner-conjecture
title: "Kapovich-Kleiner Conjecture"
topic: 02-algebra-group-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Kapovich-Kleiner Conjecture

> **Topic:** Algebra & Group Theory · **ID:** `02-algebra-group-theory/kapovich-kleiner-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

**Conjecture (Kapovich–Kleiner, 2000).** Let $G$ be a word-hyperbolic group whose Gromov boundary $\partial_\infty G$ is homeomorphic to the Sierpiński carpet. Then $G$ acts geometrically (properly discontinuously, cocompactly, by isometries) on a convex subset $Y \subseteq \mathbb{H}^3$ with nonempty totally geodesic boundary.

Equivalently: $G$ is virtually the fundamental group of a compact hyperbolic $3$-manifold with nonempty totally geodesic boundary; equivalently $G$ is a convex-cocompact Kleinian group whose limit set is a Sierpiński carpet, up to finite index and finite kernel.

A complete proof must produce, from purely coarse/topological data (the homeomorphism type of $\partial_\infty G$), a discrete faithful representation $\rho\colon G_0 \to \mathrm{PSL}_2(\mathbb{C})$ on a finite-index subgroup $G_0 \le G$ with convex-cocompact image and totally geodesic convex-core boundary. A disproof requires a hyperbolic group with carpet boundary admitting no such action — e.g. one whose boundary carries no quasi-Möbius round-carpet structure.

This is the "surface-with-boundary" companion of **Cannon's conjecture** ($\partial_\infty G \cong S^2 \Rightarrow G$ is virtually Kleinian cocompact), and sits inside the Kapovich–Kleiner program on hyperbolic groups with low-dimensional boundary.

## 2. Mathematical Foundations

**Gromov boundary.** For $G$ hyperbolic with Cayley graph $\Gamma$, $\partial_\infty G$ is the set of equivalence classes of geodesic rays, metrized by visual metrics $d_\epsilon$ with
$$d_\epsilon(\xi,\eta) \asymp e^{-\epsilon\,(\xi\mid\eta)_{e}},\qquad (\xi\mid\eta)_e = \tfrac12\big(|\xi| + |\eta| - d(\xi,\eta)\big),$$
for $\epsilon>0$ small. Quasi-isometries of $G$ induce **quasi-Möbius** (equivalently, for uniformly perfect spaces, quasisymmetric) homeomorphisms of $(\partial_\infty G, d_\epsilon)$; the quasi-Möbius class — the *conformal gauge* — is the quasi-isometry invariant.

**Sierpiński carpet.** The standard carpet $\mathcal{S}$ is $[0,1]^2$ minus the middle open ninth, iterated. Whyburn's theorem: a metrizable continuum is homeomorphic to $\mathcal{S}$ iff it is planar, $1$-dimensional, connected, locally connected, has no local cut points, and its complementary components have disjoint closures with diameters $\to 0$. Embedded in $S^2$,
$$\mathcal{S} \;=\; S^2 \setminus \bigsqcup_{i\in\mathbb{N}} D_i,$$
with $D_i$ open Jordan domains; $\partial D_i$ are the **peripheral circles**, a topological invariant of $\mathcal{S}$ (they are exactly the non-separating simple closed curves).

**Round carpet.** A carpet is *round* if all $D_i$ are open round disks. Conjecturally, $\partial_\infty G$ carpet $\Rightarrow$ $\partial_\infty G$ is quasi-Möbius equivalent to a round carpet in $\hat{\mathbb{C}}$; combined with rigidity, that gives the group action.

**Kapovich–Kleiner trichotomy.** If $G$ is hyperbolic, one-ended, $\dim \partial_\infty G = 1$, and $G$ admits no essential splitting over a virtually cyclic subgroup (so $\partial_\infty G$ has no local cut points, by Bowditch), then
$$\partial_\infty G \;\cong\; S^1,\quad \text{Sierpiński carpet},\quad\text{or the Menger curve }\mu^1 .$$
The circle case is settled (Tukia–Casson–Jungreis–Gabai: $G$ is virtually Fuchsian). The Menger case is generic and expected to be wild. The carpet case is this conjecture.

**Conformal dimension.** The Ahlfors-regular conformal dimension is
$$\operatorname{confdim}_{AR}(\partial_\infty G)=\inf\{Q>0:\ \exists\ \text{Ahlfors } Q\text{-regular } d'\in \text{gauge}(\partial_\infty G)\}.$$
For a carpet boundary $1<\operatorname{confdim}_{AR}\le 2$. If $G$ is convex cocompact Kleinian with limit set $\Lambda(G)$, then $\operatorname{confdim}_{AR}=\dim_H \Lambda(G)=\delta(G)$, the critical exponent, and the infimum is **attained**.

**Target conclusion, restated.** There is $Y\subseteq\mathbb{H}^3$ closed convex with $\partial Y$ a disjoint union of totally geodesic planes, and a geometric $G$-action on $Y$; then $\partial_\infty Y=\Lambda(G)$ is a round carpet whose peripheral circles are the boundary circles of the removed half-space disks, and the peripheral subgroups $\mathrm{Stab}_G(\partial D_i)$ are virtual surface groups.

## 3. History & State of the Art (SOTA)

- **1980s.** Thurston's geometrization and Cannon's combinatorial Riemann mapping program set the pattern: recognize a group's negative curvature from the conformal geometry of its boundary. Cannon–Swenson (Trans. AMS, 1998) gave a combinatorial criterion for the $S^2$ case.
- **2000.** Kapovich and Kleiner, *Hyperbolic groups with low-dimensional boundary* (Ann. Sci. ÉNS), prove the trichotomy above and formulate the carpet conjecture. They also prove structural results: peripheral circles are permuted by $G$ with finitely many orbits, and their stabilizers are quasiconvex.
- **2002–2011.** Bonk–Kleiner solve the *sphere* uniformization problem (Ahlfors $2$-regular linearly locally connected sphere $\Rightarrow$ quasisymmetric to $S^2$), and Bonk (Invent. Math. 2011) proves the **carpet uniformization theorem**: a carpet in $S^2$ whose peripheral circles are uniform quasicircles, uniformly relatively separated, is quasisymmetric to a round carpet. This makes "round carpet" reachable *if* one first embeds the boundary in $S^2$ well.
- **2005.** Kapovich–Kleiner, *Coarse Alexander duality and duality groups* (JDG), supply the coarse $PD(3)$-pair machinery: a hyperbolic group with carpet boundary behaves like a $PD(3)$ pair relative to its peripheral subgroups.
- **2013.** Bonk–Merenkov prove quasisymmetric rigidity of the standard square carpets $S_p$ (their quasisymmetry groups are finite, of order $\le 8$ for $p\ge 3$) — evidence that carpets in the conformal gauge are extremely rigid.
- **2015.** Haïssinsky, *Hyperbolic groups with planar boundaries* (Invent. Math.), gives the strongest general theorem to date (Section 4).
- **2013.** Markovic's criterion for Cannon's conjecture via abundance of quasiconvex surface subgroups, built on Kahn–Markovic; the analogous relative statement for carpets is the natural target.

**SOTA summary:** the conjecture is open in general; it is a theorem under an attained-conformal-dimension hypothesis, and it is known to follow from Cannon's conjecture via a doubling reduction.

## 4. Partial Results / Verified Cases

- **Conformal dimension attained (Haïssinsky, 2015).** If $G$ is hyperbolic with planar boundary $\partial_\infty G$ (in particular a Sierpiński carpet) and $\operatorname{confdim}_{AR}(\partial_\infty G)$ is attained by some Ahlfors-regular metric in the gauge, then $G$ is virtually a convex-cocompact Kleinian group. This settles the conjecture for all such groups and is the exact analogue of Bonk–Kleiner's conditional solution of Cannon's conjecture.
- **Reduction to Cannon's conjecture (Kapovich–Kleiner).** For $G$ with carpet boundary and virtual-surface peripheral subgroups, the double $D(G)$ along the peripheral subgroups is hyperbolic with $\partial_\infty D(G)\cong S^2$; Cannon's conjecture for $D(G)$ plus equivariant Mostow-type rigidity returns the totally geodesic structure for $G$. So Cannon $\Rightarrow$ Kapovich–Kleiner.
- **Circle case, $\dim=1$.** Trichotomy branch $\partial_\infty G\cong S^1$: fully solved (Tukia 1988; Casson–Jungreis 1994; Gabai 1992) — $G$ is virtually a surface group.
- **Kleinian input.** If $G$ is *already known* to be a discrete subgroup of $\mathrm{Isom}(\mathbb{H}^3)$ that is convex cocompact with $\Lambda(G)$ a carpet, the conclusion holds by Thurston/Mostow; so the conjecture holds trivially on the class of $3$-manifold groups. Combined with Agol–Wise, every one-ended hyperbolic $3$-manifold group with incompressible boundary is covered.
- **Coxeter groups.** For hyperbolic Coxeter groups whose nerve is a planar $1$-complex, the boundary is a carpet and explicit geometric realizations by truncated hyperbolic polyhedra exist in many families (see Section 10); Bourdon–Kleiner verify the combinatorial Loewner property for large classes of such boundaries, and CLP $\Rightarrow$ attainment is expected but unproven.
- **Rigidity results.** Bonk–Kleiner–Merenkov: quasisymmetries of Schottky sets of measure zero in $S^n$, $n\ge 3$, are restrictions of Möbius maps; Bonk–Merenkov: square carpets $S_p$ are quasisymmetrically rigid. These confirm the conjecture's rigidity prediction on model carpets.

## 5. Principal Obstacles

- **No a priori metric control.** The visual metric is only defined up to quasi-Möbius equivalence. Bonk's uniformization theorem needs peripheral circles to be *uniform quasicircles, uniformly relatively separated* — quantitative conditions with no known derivation from hyperbolicity alone.
- **The boundary is not given inside $S^2$.** Whyburn's characterization gives an abstract carpet; the group-equivariant embedding into $\hat{\mathbb{C}}$ with controlled geometry is precisely what must be constructed. Topological planarity carries no metric information.
- **Conformal dimension need not be attained.** This is the same wall as in Cannon's conjecture. For a general hyperbolic group, $\operatorname{confdim}_{AR}$ can fail to be attained (Bourdon's examples in other settings), and no criterion decides attainment from a presentation. Combinatorial modulus estimates (Bourdon–Kleiner, Carrasco Piaggio) give the exponent as a limit of discrete moduli but not attainment.
- **Peripheral structure is not known to be surface-like.** To run the doubling argument one needs $\mathrm{Stab}_G(\partial D_i)$ to be virtually a surface group. Coarse Alexander duality shows these subgroups are coarse $PD(2)$ groups; "coarse $PD(2)$ $\Rightarrow$ virtual surface group" is itself the Cannon-type $\partial\cong S^1$ statement, available only once quasiconvexity plus one-endedness are established — the hardest inputs come with the same circularity risk.
- **Failure of soft topology.** Algebraic topology (Čech cohomology, duality) determines the homeomorphism type of the boundary but not the gauge; two hyperbolic groups can have homeomorphic boundaries with non-quasi-Möbius gauges. Analytic tools (Loewner property, Poincaré inequalities) are unavailable because carpets have measure zero and no obvious rectifiable curve families of positive modulus.
- **No random/probabilistic surface subgroup construction relative to boundary.** Kahn–Markovic's method builds closed surfaces via exponential mixing on a *closed* hyperbolic $3$-manifold; there is no known analogue producing relative surfaces starting from a group only.

## 6. The Gap

Proven: carpet boundary + *attained* Ahlfors-regular conformal dimension $\Rightarrow$ virtually Kleinian (Haïssinsky). Conjectured: carpet boundary $\Rightarrow$ virtually Kleinian.

The gap is the single implication
$$\partial_\infty G \cong \text{Sierpiński carpet}\ \Longrightarrow\ \operatorname{confdim}_{AR}(\partial_\infty G)\ \text{is attained},$$
or a route that bypasses it: producing a $G$-equivariant quasi-Möbius embedding $\partial_\infty G \hookrightarrow \hat{\mathbb{C}}$ with uniformly quasicircle, uniformly separated peripheral circles, so Bonk's uniformization applies and Sullivan-type rigidity upgrades the resulting round-carpet action to a Kleinian one. Equivalently, one must show that a hyperbolic group with carpet boundary contains "enough" quasiconvex virtual surface subgroups — the relative form of Markovic's criterion — where "enough" means their limit sets separate points of $\partial_\infty G$ in the required uniform way.

## 7. Current Research (as of June 2026)

- **Analysis on metric spaces / conformal dimension.** Groups around Bonk, Kleiner, Merenkov, Haïssinsky, Bourdon, and Carrasco Piaggio continue to push combinatorial modulus and the combinatorial Loewner property (CLP) as a substitute for attainment. Verifying CLP for boundaries of hyperbolic Coxeter groups with planar nerve, and proving **CLP $\Rightarrow$ attainment**, is the most-cited concrete goal. *(frontier — verify)*
- **Cubulation and surface subgroups.** Post-Agol–Wise techniques are used to search for quasiconvex surface subgroups in hyperbolic groups with carpet boundary, aiming at a relative Markovic criterion. Progress is reported for groups acting properly cocompactly on CAT(0) cube complexes. *(frontier — verify)*
- **Coarse $PD$-pairs.** Continuation of Kapovich–Kleiner's coarse Alexander duality to prove that peripheral subgroups of carpet groups are virtual surface groups unconditionally; related work on Bowditch boundaries of relatively hyperbolic groups (Tshishiku–Walsh and successors) treats the $S^2$ analogue in the relatively hyperbolic setting.
- **Quasisymmetric rigidity of carpets.** Extending Bonk–Merenkov rigidity beyond square carpets to slit carpets and Julia-set carpets, mapping out which carpets can be group boundaries.
- **Computational/experimental.** Numerical estimation of $\operatorname{confdim}_{AR}$ via discrete $Q$-modulus on Cayley-graph annuli for small Coxeter examples; used as a sanity check on attainment conjectures. *(frontier — verify)*

## 8. Future Work

- Prove **CLP $\Rightarrow$ attained conformal dimension** for boundaries of hyperbolic groups; this would finish both Cannon and Kapovich–Kleiner for CLP boundaries.
- Prove unconditionally that peripheral-circle stabilizers in a carpet group are virtually surface groups, closing the doubling reduction and making Kapovich–Kleiner a strict corollary of Cannon.
- Develop a relative Kahn–Markovic surface-subgroup machine producing quasiconvex surface subgroups with prescribed peripheral behaviour.
- Settle the Menger-curve branch of the trichotomy: show that hyperbolic groups with Menger boundary admit no analogous uniformization, isolating carpets as the exceptional planar case.
- Classify, up to quasisymmetry, all carpets that arise as $\partial_\infty G$ — expected answer: exactly the round carpets of convex-cocompact Kleinian groups.

## 9. Key References

- **[Foundational]** M. Kapovich, B. Kleiner. *Hyperbolic groups with low-dimensional boundary.* Annales scientifiques de l'École Normale Supérieure (4) **33** (2000), 647–669.
- **[Foundational]** B. H. Bowditch. *Cut points and canonical splittings of hyperbolic groups.* Acta Mathematica **180** (1998), 145–186. [DOI](https://doi.org/10.1007/bf02392898)
- **[Foundational]** M. Kapovich, B. Kleiner. *Coarse Alexander duality and duality groups.* Journal of Differential Geometry **69** (2005), 279–352.
- **[SOTA / Recent]** P. Haïssinsky. *Hyperbolic groups with planar boundaries.* Inventiones Mathematicae **201** (2015), 61–98. [DOI](https://doi.org/10.1007/s00222-014-0552-x)
- **[SOTA / Recent]** M. Bonk. *Uniformization of Sierpiński carpets in the plane.* Inventiones Mathematicae **186** (2011), 559–665. [DOI](https://doi.org/10.1007/s00222-011-0325-8)
- **[SOTA / Recent]** M. Bonk, B. Kleiner. *Quasisymmetric parametrizations of two-dimensional metric spheres.* Inventiones Mathematicae **150** (2002), 127–183. [DOI](https://doi.org/10.1007/s00222-002-0233-z)
- **[SOTA / Recent]** M. Bonk, S. Merenkov. *Quasisymmetric rigidity of square Sierpiński carpets.* Annals of Mathematics (2) **177** (2013), 591–643. [DOI](https://doi.org/10.4007/annals.2013.177.2.5)
- **[SOTA / Recent]** M. Bonk, B. Kleiner, S. Merenkov. *Rigidity of Schottky sets.* American Journal of Mathematics **131** (2009), 409–443. [DOI](https://doi.org/10.1353/ajm.0.0045)
- **[SOTA / Recent]** M. Bourdon, B. Kleiner. *Combinatorial modulus, the combinatorial Loewner property, and Coxeter groups.* Groups, Geometry, and Dynamics **7** (2013), 39–107. [DOI](https://doi.org/10.4171/ggd/177)
- **[SOTA / Recent]** V. Markovic. *Criterion for Cannon's conjecture.* Geometric and Functional Analysis **23** (2013), 1035–1061.
- **[SOTA / Recent]** J. Kahn, V. Markovic. *Immersing almost geodesic surfaces in a closed hyperbolic three manifold.* Annals of Mathematics **175** (2012), 1127–1190. [DOI](https://doi.org/10.4007/annals.2012.175.3.4)
- **[Survey]** M. Bonk. *Quasiconformal geometry of fractals.* Proceedings of the International Congress of Mathematicians, Madrid 2006, Vol. II, EMS, 1349–1373. [DOI](https://doi.org/10.4171/022-2/64)
- **[Survey]** B. Kleiner. *The asymptotic geometry of negatively curved spaces: uniformization, geometrization and rigidity.* Proceedings of the ICM, Madrid 2006, Vol. II, EMS, 743–768. [DOI](https://doi.org/10.4171/022-2/36)
- **[Survey]** J. W. Cannon, E. L. Swenson. *Recognizing constant curvature discrete groups in dimension 3.* Transactions of the AMS **350** (1998), 809–849. [DOI](https://doi.org/10.1090/s0002-9947-98-02107-2)
- **[Survey]** M. Kapovich. *Hyperbolic Manifolds and Discrete Groups.* Birkhäuser, 2001.

## 10. Worked Example / Concrete Special Case

**A Coxeter group with carpet boundary, and its geometric realization.**

Let
$$W \;=\; \big\langle\, r_1,r_2,r_3,r_4 \;\big|\; r_i^2=1,\ (r_ir_j)^4=1\ (i\neq j) \,\big\rangle,$$
the Coxeter group whose diagram is the complete graph $K_4$ with every edge labelled $4$.

*Step 1 — hyperbolicity.* By Moussong's criterion, $W$ is word-hyperbolic iff no special subgroup is virtually $\mathbb{Z}^2$ (Euclidean). The rank-$2$ specials $\langle r_i,r_j\rangle$ are finite dihedral of order $8$. The rank-$3$ specials are $(4,4,4)$-triangle groups with
$$\tfrac14+\tfrac14+\tfrac14=\tfrac34<1,$$
hence hyperbolic, not Euclidean. So $W$ is hyperbolic.

*Step 2 — the nerve.* The nerve $L$ has a simplex for each spherical (finite) subset. Singletons and all six pairs are spherical; no triple is. Hence $L=K_4$: a $1$-dimensional, connected, $3$-connected, **planar** graph.

*Step 3 — the boundary.* $\dim\partial_\infty W=\dim L=1$. Since $L$ is connected with no separating simplex, $W$ is one-ended; $3$-connectivity of $L$ rules out local cut points, so $W$ admits no essential virtually-cyclic splitting (Bowditch). The Kapovich–Kleiner trichotomy leaves $S^1$, carpet, or Menger curve. $W$ is not virtually a surface group (it contains $(4,4,4)$-triangle groups of infinite index and has too many ends of pairs for $S^1$), and $L$ is planar, so
$$\partial_\infty W \;\cong\; \text{Sierpiński carpet}.$$

*Step 4 — the conjectured conclusion, realized.* Take the hyperideal (all four vertices outside $\mathbb{H}^3$) tetrahedron with all six dihedral angles $\pi/4$, truncated by the four polar planes of its vertices. Truncation faces meet the four "hexagonal" faces orthogonally, and each truncation triangle has angles $(\pi/4,\pi/4,\pi/4)$, sum $3\pi/4<\pi$: a genuine hyperbolic triangle, with area $\pi-3\pi/4=\pi/4$ by Gauss–Bonnet. Reflecting in the four hexagonal faces only gives a discrete group isomorphic to $W$, acting geometrically on the convex set
$$Y=\bigcup_{w\in W} w\cdot P \subseteq \mathbb{H}^3,$$
whose boundary is the disjoint union of the $W$-orbit of the four truncation planes — totally geodesic. The limit set is
$$\Lambda(W)=\hat{\mathbb{C}}\setminus \bigsqcup_{w\in W,\,k\le 4} w(D_k),$$
a **round** carpet whose peripheral circles are the boundaries of the orbit disks $w(D_k)$; the peripheral subgroups are the $(4,4,4)$-triangle groups, i.e. virtual surface groups, exactly as the conjecture predicts. Here $\operatorname{confdim}_{AR}(\partial_\infty W)=\dim_H\Lambda(W)=\delta(W)\in(1,2)$ and is attained.

*Step 5 — what is actually open.* Everything above used the *external* input of an explicit polyhedron. The conjecture asks for the reverse arrow: given only the presentation of $W$ (or of any hyperbolic group) plus the topological fact "$\partial_\infty W$ is a carpet", construct $Y$. Changing $K_4$ to $K_5$ with all labels $4$ keeps the group hyperbolic but makes the nerve nonplanar, so the boundary becomes the Menger curve $\mu^1$ and no such action exists — showing that planarity of the boundary is the sole hypothesis carrying the geometric conclusion, and that no purely combinatorial invariant currently extracts it.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*