---
id: 04-topology/borel-conjecture
title: "Borel Conjecture"
topic: 04-topology
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Borel Conjecture

> **Topic:** Topology & Knot Theory · **ID:** `04-topology/borel-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

**Conjecture (Borel, c. 1953).** Let $M$ and $N$ be closed aspherical topological manifolds and let $f\colon M \to N$ be a homotopy equivalence. Then $f$ is homotopic to a homeomorphism. In particular $M$ and $N$ are homeomorphic, and a closed aspherical manifold is determined up to homeomorphism by its fundamental group.

Equivalent formulation: for every closed aspherical manifold $M$, the topological structure set is a single point,
$$\mathcal{S}^{\mathrm{TOP}}(M) = \{*\}.$$

Constraints that matter:
- **Aspherical** means $\pi_i(M) = 0$ for $i \ge 2$, i.e. the universal cover $\widetilde M$ is contractible and $M \simeq B\pi_1(M)$.
- **Topological**, not smooth or PL. The smooth and PL analogues are *false* (Section 3), so any proof strategy must use tools unavailable in those categories.
- No curvature, geometry, or finiteness hypothesis beyond closed + aspherical is allowed.

A complete proof must produce the homeomorphism for all closed aspherical manifolds in all dimensions; a disproof needs one pair $M \not\cong N$ with $M \simeq N$ aspherical, or a single $M$ with $|\mathcal{S}^{\mathrm{TOP}}(M)| > 1$.

## 2. Mathematical Foundations

**Structure set.** For a closed topological $n$-manifold $M$, $\mathcal{S}^{\mathrm{TOP}}(M)$ is the set of equivalence classes of pairs $(N, f)$ with $N$ a closed manifold and $f\colon N \to M$ a homotopy equivalence, where $(N,f)\sim(N',f')$ iff there is a homeomorphism $h$ with $f' h \simeq f$. The base point is $(M,\mathrm{id})$.

**Surgery exact sequence** (Browder–Novikov–Sullivan–Wall; topological category, $n \ge 5$, $\pi = \pi_1(M)$):
$$\cdots \to L_{n+1}(\mathbb{Z}\pi) \xrightarrow{\ \partial\ } \mathcal{S}^{\mathrm{TOP}}(M) \xrightarrow{\ \eta\ } [M, G/\mathrm{TOP}] \xrightarrow{\ \sigma\ } L_n(\mathbb{Z}\pi),$$
where $L_*$ are Wall's quadratic $L$-groups and $G/\mathrm{TOP}$ classifies normal invariants. Localized away from $2$, $G/\mathrm{TOP} \simeq \mathbb{L}\langle 1\rangle_0$, the $0$-space of the $1$-connective quadratic $L$-theory spectrum.

**Assembly.** Ranicki's algebraic surgery exact sequence identifies the sequence above with
$$\cdots \to H_n(M; \mathbb{L}\langle 1\rangle) \xrightarrow{\ A\ } L_n(\mathbb{Z}\pi) \to \mathcal{S}^{\mathrm{TOP}}(M) \to H_{n-1}(M;\mathbb{L}\langle 1\rangle) \to \cdots$$
For $M$ aspherical, $M = B\pi$, so the Borel Conjecture in dimensions $\ge 5$ follows from:
1. $A\colon H_n(B\pi; \mathbb{L}\langle 1\rangle) \to L_n(\mathbb{Z}\pi)$ is an isomorphism for all $n$ ($L$-theoretic Farrell–Jones), and
2. $\mathrm{Wh}(\pi) = \widetilde K_0(\mathbb{Z}\pi) = K_{-i}(\mathbb{Z}\pi) = 0$ for $i \ge 1$ ($K$-theoretic Farrell–Jones), which via the $s$-cobordism theorem upgrades $h$-cobordisms to products.

**Farrell–Jones Conjecture (FJC).** For a group $G$ and $R = \mathbb{Z}$, the assembly maps
$$H_n^G(\underline{\underline{E}}G; \mathbf{K}_R) \to K_n(RG), \qquad H_n^G(\underline{\underline{E}}G; \mathbf{L}^{\langle -\infty\rangle}_R) \to L_n^{\langle -\infty\rangle}(RG)$$
induced by projection to a point are isomorphisms, where $\underline{\underline{E}}G$ is the classifying space for the family of virtually cyclic subgroups.

**Theorem (Farrell–Jones + Ranicki + Freedman–Quinn machinery).** If $G$ satisfies FJC in $K$- and $L$-theory and $M$ is a closed aspherical manifold of dimension $n \ge 5$ with $\pi_1(M) \cong G$, then $\mathcal{S}^{\mathrm{TOP}}(M) = \{*\}$.

Two facts constrain the fundamental groups involved: $\pi = \pi_1(M)$ is torsion-free (a finite-order element acting freely on contractible $\widetilde M \simeq \mathbb{R}^n$ contradicts Smith theory), and $\pi$ is a Poincaré duality group of formal dimension $n$.

## 3. History & State of the Art

- **c. 1953.** Armand Borel poses the question in correspondence with Serre, prompted by Mostow's rigidity for solvmanifolds. First circulated in print in Borel's 1953 note and reproduced in the appendix to Farrell–Jones' 1993 lecture notes.
- **1968–69.** Wall's *Surgery on Compact Manifolds* provides the exact sequence; Kirby–Siebenmann establish topological transversality and the topological $s$-cobordism theorem in dimension $\ge 5$, making the topological surgery machine available.
- **1969–70.** Hsiang–Shaneson and Wall classify PL structures on the torus $T^n$, $n \ge 5$: **fake tori** exist, so the PL Borel Conjecture is false. Kirby–Siebenmann then deduce that $T^n$ is topologically rigid.
- **1978–89.** Farrell–Hsiang prove rigidity for flat and infranil manifolds. Farrell–Jones (*A topological analogue of Mostow's rigidity theorem*, JAMS 1989) prove the Borel Conjecture for closed nonpositively curved Riemannian manifolds of dimension $\ge 5$, using their "asymptotic transfer" / foliated control theory.
- **1989–90.** Farrell–Jones show the **smooth** Borel Conjecture fails: for many nonpositively curved $M^n$ and exotic spheres $\Sigma$, $M \\# \Sigma$ is homeomorphic but not diffeomorphic to $M$.
- **1993.** Farrell–Jones formulate the Isomorphism Conjecture (JAMS), reorganizing the whole subject around assembly maps.
- **2008–2012.** Bartels–Lück–Reich prove the $K$-theoretic FJC for hyperbolic groups (Invent. Math. 2008); **Bartels–Lück** prove full FJC and hence the Borel Conjecture for Gromov-hyperbolic and CAT(0) groups (*Annals of Mathematics* 176 (2012), 631–689). This is the current headline theorem.
- **2012–2016.** Wegner (CAT(0), then virtually solvable), Bartels (relatively hyperbolic), Rüping ($\mathrm{GL}_n(\mathbb{Z})$ and $S$-arithmetic groups), Kammeyer–Lück–Rüping (lattices in almost connected Lie groups), Bartels–Lück–Reich–Rüping — a steady widening of the class $\mathcal{FJ}$ of groups satisfying FJC, closed under subgroups, finite products, free products, and directed colimits.

## 4. Partial Results / Verified Cases

**By dimension.**
- $n \le 2$: classical (surface classification).
- $n = 3$: true, by Waldhausen's rigidity for Haken manifolds (1968) plus Perelman's geometrization; every closed aspherical $3$-manifold is determined by $\pi_1$.
- $n = 4$: true whenever $\pi_1$ is *good* in Freedman's sense (subexponential growth, and more generally elementary amenable), since the disc embedding theorem then makes surgery and the $s$-cobordism theorem work. Covers $T^4$ and closed flat $4$-manifolds. Open for general $\pi_1$, e.g. hyperbolic $4$-manifolds.
- $n \ge 5$: reduced to FJC for $\pi_1(M)$.

**By fundamental group** (all give Borel in dim $\ne 4$; dim $\ge 5$ via FJC):
- Hyperbolic groups and CAT(0) groups (Bartels–Lück 2012) — includes all closed nonpositively curved manifolds, hence all closed hyperbolic manifolds of any dimension $\ge 5$.
- Virtually solvable groups, including virtually poly-$\mathbb{Z}$ (Wegner 2015); covers all infranilmanifolds and infrasolvmanifolds.
- Free abelian $\mathbb{Z}^n$: the $n$-torus is topologically rigid for every $n$.
- Lattices in virtually connected Lie groups (Bartels–Farrell–Lück for cocompact lattices in almost connected Lie groups, 2014; Kammeyer–Lück–Rüping, *Geom. Topol.* 2016).
- Relatively hyperbolic groups with FJC peripherals (Bartels 2017); mapping class groups (Bartels–Bestvina 2019) — the latter yields FJC but not Borel directly, as mapping class groups are not torsion-free.
- Fundamental groups of closed $3$-manifolds (Roushon; Bartels–Lück–Reich techniques).

**Known counterexamples in other categories.** PL: fake tori, $\mathcal{S}^{\mathrm{PL}}(T^n) \ne *$ for $n \ge 5$. Smooth: $M \\# \Sigma$ for nonpositively curved $M$. Also, the "Borel Conjecture with boundary" and the Poincaré-duality-group version (every torsion-free PD$_n$ group is the fundamental group of a closed aspherical manifold) are separate open problems.

## 5. Principal Obstacles

- **No global structure on aspherical manifolds.** Davis's reflection-group construction produces closed aspherical manifolds whose universal covers are *not* homeomorphic to $\mathbb{R}^n$ (non-simply-connected at infinity). These carry no nonpositively curved metric and no coarse geometry that current control theory can exploit.
- **Control theory needs a flow.** All FJC proofs — Farrell–Jones' foliated control, Bartels–Lück's transfer with $\mathcal{N}$-dominated covers — rely on a geodesic-type flow space and on finite asymptotic dimension / finite-dimensional models for $\underline{\underline{E}}G$. Exotic aspherical manifolds may have $\pi_1$ with infinite asymptotic dimension.
- **FJC is not known to be inherited by extensions or amalgams in general.** The class $\mathcal{FJ}$ is closed under subgroups, colimits, and (conditionally) extensions with FJC quotients having suitable actions — but there is no closure under arbitrary extensions, and no method for a group given only by a presentation.
- **Nonpositively curved $\ne$ aspherical.** Gromov's random groups and the Osajda/Gromov monster groups embed expanders; such groups are counterexamples to the Baum–Connes conjecture with coefficients, and FJC for groups built from them is unavailable. Whether they arise as $\pi_1$ of closed aspherical manifolds is itself open.
- **Dimension 4 lacks surgery.** Without the disc embedding theorem for arbitrary $\pi_1$, the surgery exact sequence and the $s$-cobordism theorem both fail as tools; the hyperbolic $4$-manifold case is genuinely inaccessible.
- **$K$-theory vanishing is fragile.** Borel needs $\mathrm{Wh}(\pi)=0$; this is unknown for general torsion-free $\pi$ and is not implied by $L$-theoretic statements such as Novikov.

## 6. The Gap

Proven: Borel holds for $M^n$, $n \ge 5$, whenever $\pi_1(M) \in \mathcal{FJ}$ — a class built from hyperbolic, CAT(0), virtually solvable, and lattice groups by explicit closure operations. Also proven in $n \le 3$ unconditionally, and $n=4$ for good groups.

Missing: a proof of FJC for a *general* torsion-free Poincaré duality group, with no geometric input. The exact step is producing, for arbitrary such $G$, the geometric data that transfer arguments consume: a finite-dimensional $G$-space with a flow, covers of controlled dimension and long thin sets in the flow direction, or an equivalent "$\mathcal{N}$-dominated" family. There is currently no candidate construction for a group known only to act freely cocompactly on a contractible manifold. Secondarily, dimension $4$ requires either the disc embedding theorem for all groups (unlikely — Freedman–Quinn suggest it fails) or a route around it.

## 7. Current Research (as of June 2026)

- **Munich / Bonn / Münster school (Bartels, Lück, Wegner, Rüping, Kasprowski, Winges).** Extending $\mathcal{FJ}$: FJC for $\mathrm{Out}(F_n)$ remains the flagship open target *(frontier — verify)*; FJC with coefficients in higher categories and for Hecke algebras of reductive $p$-adic groups (Bartels–Lück, 2023) is an active line. Recent work uses "Dress induction" and homotopy-coherent transfer.
- **Coarse geometry.** Finite decomposition complexity (Guentner–Tessera–Yu) and finite asymptotic dimension give $K$- and $L$-theoretic vanishing/injectivity results and continue to yield Novikov-type theorems for classes broader than $\mathcal{FJ}$.
- **Davis-style constructions.** Ongoing attempts to produce a closed aspherical manifold whose fundamental group is a counterexample to FJC or has infinite asymptotic dimension — via hyperbolization applied to exotic complexes *(frontier — verify)*.
- **Dimension 4.** Interaction between the disc embedding theorem (the 2021 Behrens–Kalmár–Kim–Powell–Ray book) and topological rigidity of aspherical $4$-manifolds with free or surface fundamental groups.
- **Equivariant / stratified analogues.** Farrell–Jones for $L$-theory with $\mathbb{Z}[1/2]$-coefficients, and the Borel Conjecture for orbifolds and for manifolds with boundary.

## 8. Future Work

- Prove FJC for $\mathrm{Out}(F_n)$ and for groups acting properly on finite-dimensional CAT(0) cube complexes without cocompactness.
- Find a purely homotopy-theoretic proof of the assembly isomorphism for PD$_n$ groups, bypassing the flow-space transfer entirely — Lück has repeatedly flagged this as the structural need.
- Determine whether every torsion-free PD$_n$ group ($n \ge 4$) is the fundamental group of a closed aspherical manifold (Wall's problem); a negative answer would reshape Borel.
- Settle whether $\mathrm{Wh}(\pi) = 0$ for all torsion-free $\pi$ independently of FJC.
- Resolve dimension $4$ for hyperbolic $4$-manifold groups.
- Investigate whether Gromov monster groups can be fundamental groups of closed aspherical manifolds; a positive answer plus a failure of FJC there would be the most likely route to a counterexample.

## 9. Key References

- **[Foundational]** C. T. C. Wall. *Surgery on Compact Manifolds.* Academic Press, 1970; 2nd ed., AMS Mathematical Surveys and Monographs 69, 1999.
- **[Foundational]** R. C. Kirby and L. C. Siebenmann. *Foundational Essays on Topological Manifolds, Smoothings, and Triangulations.* Annals of Mathematics Studies 88, Princeton University Press, 1977.
- **[Foundational]** F. T. Farrell and L. E. Jones. *A topological analogue of Mostow's rigidity theorem.* Journal of the American Mathematical Society 2 (1989), 257–370.
- **[Foundational]** F. T. Farrell and L. E. Jones. *Isomorphism conjectures in algebraic $K$-theory.* Journal of the American Mathematical Society 6 (1993), 249–297. [DOI](https://doi.org/10.2307/2152801)
- **[Foundational]** A. Ranicki. *Algebraic $L$-theory and Topological Manifolds.* Cambridge Tracts in Mathematics 102, Cambridge University Press, 1992.
- **[SOTA / Recent]** A. Bartels and W. Lück. *The Borel conjecture for hyperbolic and CAT(0)-groups.* Annals of Mathematics 175 (2012), 631–689. [DOI](https://doi.org/10.4007/annals.2012.175.2.5)
- **[SOTA / Recent]** A. Bartels, W. Lück and H. Reich. *The $K$-theoretic Farrell–Jones conjecture for hyperbolic groups.* Inventiones Mathematicae 172 (2008), 29–70. [DOI](https://doi.org/10.1007/s00222-007-0093-7)
- **[SOTA / Recent]** C. Wegner. *The Farrell–Jones conjecture for virtually solvable groups.* Journal of Topology 8 (2015), 975–1016. [DOI](https://doi.org/10.1112/jtopol/jtv026)
- **[SOTA / Recent]** H. Kammeyer, W. Lück and H. Rüping. *The Farrell–Jones conjecture for arbitrary lattices in virtually connected Lie groups.* Geometry & Topology 20 (2016), 1275–1287. [DOI](https://doi.org/10.2140/gt.2016.20.1275)
- **[Survey]** W. Lück. *Survey on aspherical manifolds.* In: Proceedings of the 5th European Congress of Mathematics, EMS, 2010, 53–82.
- **[Survey]** W. Lück and H. Reich. *The Baum–Connes and the Farrell–Jones conjectures in $K$- and $L$-theory.* In: Handbook of $K$-theory, Springer, 2005, 703–842. [DOI](https://doi.org/10.1007/978-3-540-27855-9_15)
- **[Survey]** M. W. Davis. *The Geometry and Topology of Coxeter Groups.* London Mathematical Society Monographs 32, Princeton University Press, 2008.
- **[Reference]** M. Freedman and F. Quinn. *Topology of 4-Manifolds.* Princeton University Press, 1990.

## 10. Worked Example: the $n$-Torus

Take $M = T^n = \mathbb{R}^n/\mathbb{Z}^n$, $n \ge 5$. It is closed and aspherical with $\pi = \mathbb{Z}^n$.

**Step 1 — $K$-theory.** By Bass–Heller–Swan, $K_i(\mathbb{Z}[\mathbb{Z}^n])$ decomposes with no Nil terms since $\mathbb{Z}$ is regular. Iterating,
$$\mathrm{Wh}(\mathbb{Z}^n) = 0, \qquad \widetilde K_0(\mathbb{Z}[\mathbb{Z}^n]) = 0, \qquad K_{-i}(\mathbb{Z}[\mathbb{Z}^n]) = 0\ (i \ge 1).$$
So every $h$-cobordism on $T^n$ is a product, and homotopy equivalences may be taken simple.

**Step 2 — $L$-theory.** Shaneson splitting gives, for each added $\mathbb{Z}$ factor,
$$L_k^s(\mathbb{Z}[\pi \times \mathbb{Z}]) \cong L_k^s(\mathbb{Z}\pi) \oplus L_{k-1}^h(\mathbb{Z}\pi).$$
Since $\mathrm{Wh}=\widetilde K_0=0$ the decorations agree, and iterating $n$ times from $L_*(\mathbb{Z})$ gives
$$L_k(\mathbb{Z}[\mathbb{Z}^n]) \cong \bigoplus_{j=0}^{n} \binom{n}{j} L_{k-j}(\mathbb{Z}).$$
This is exactly $H_k(T^n; \mathbb{L})$, and the isomorphism is the assembly map: FJC holds for $\mathbb{Z}^n$.

**Step 3 — structure set.** Surgery exactness with $A$ an isomorphism in degrees $n$ and $n+1$ forces
$$\mathcal{S}^{\mathrm{TOP}}(T^n) = \{*\}.$$
So any closed manifold homotopy equivalent to $T^n$ is homeomorphic to it — the Borel Conjecture for $T^n$.

**Step 4 — why "topological" is essential.** The PL surgery sequence is not the same: $G/\mathrm{PL}$ differs from $G/\mathrm{TOP}$ at the prime $2$, with $\pi_4(G/\mathrm{PL}) = \mathbb{Z}$ mapping to $\pi_4(G/\mathrm{TOP}) = \mathbb{Z}$ by multiplication by $2$ (the Kervaire–Milnor obstruction), and $\pi_3(\mathrm{TOP}/\mathrm{PL}) = \mathbb{Z}/2$. The residual $\mathbb{Z}/2$ produces the Hsiang–Shaneson–Wall **fake tori**: PL manifolds PL-homotopy-equivalent but not PL-homeomorphic to $T^n$, classified by
$$H^3(T^n; \mathbb{Z}/2) \cong (\mathbb{Z}/2)^{\binom{n}{3}}.$$
For $n=5$ that is $(\mathbb{Z}/2)^{10}$: at least $1024$ PL structures, all homeomorphic to $T^5$. Smoothly, $M \\# \Sigma$ for $\Sigma$ an exotic sphere gives further non-diffeomorphic models. The single point in Step 3 is a phenomenon of the topological category alone.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*