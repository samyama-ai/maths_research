---
id: 04-topology/bounded-homeomorphism-conjecture
title: "Bounded Homeomorphism Conjecture for Open Manifolds"
topic: 04-topology
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Bounded Homeomorphism Conjecture for Open Manifolds

> **Topic:** Topology & Knot Theory · **ID:** `04-topology/bounded-homeomorphism-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Ordinary surgery classifies closed manifolds up to homeomorphism within a homotopy type. For open (non-compact, boundaryless) manifolds the homotopy type carries almost no information — every contractible open manifold is homotopy equivalent to $\mathbb{R}^n$, yet the Whitehead manifold $\mathrm{Wh}^3$ is not homeomorphic to $\mathbb{R}^3$. **Bounded (coarse) control** is the replacement invariant: one measures homotopies not by whether they exist but by how far they move points in a reference metric space.

**Bounded Homeomorphism Conjecture (bounded Borel conjecture, Ferry–Weinberger form).** Let $X$ be a uniformly contractible open $n$-manifold of bounded geometry, $n \ge 5$. Then every bounded homotopy equivalence $f : M \to X$ from an open $n$-manifold $M$ is boundedly homotopic to a homeomorphism. Equivalently, the bounded structure set vanishes:
$$\mathcal{S}^{b}(X) = 0 .$$

A complete proof must produce, for each such $f$, a homeomorphism $h : M \to X$ and a homotopy $f \simeq h$ whose tracks have uniformly bounded diameter. A disproof must exhibit a single uniformly contractible bounded-geometry $X$ and a bounded homotopy equivalence with non-trivial bounded structure invariant. **Both hypotheses are essential:** dropping bounded geometry makes the statement false (Section 4).

## 2. Mathematical Foundations

Let $(Z,d)$ be a proper metric space (closed balls compact), the *control space*. A **control map** on a space $M$ is a proper continuous $p_M : M \to Z$.

**Bounded maps.** $g : M \to N$ over $Z$ is *$C$-bounded* if
$$\sup_{x \in M} d\big(p_N(g(x)),\, p_M(x)\big) \le C < \infty .$$
A homotopy $H : M \times I \to N$ is $C$-bounded if $\operatorname{diam} p_N H(\{x\} \times I) \le C$ for all $x$. A **bounded homotopy equivalence** is a bounded $f : M \to N$ admitting bounded $g$ with $gf \simeq \mathrm{id}$, $fg \simeq \mathrm{id}$ through bounded homotopies. A **bounded homeomorphism** is a homeomorphism that is bounded, with bounded inverse.

**Uniform contractibility.** $X$ is uniformly contractible if for every $R > 0$ there is $S(R) \ge R$ such that every ball $B(x,R)$ contracts to a point inside $B(x,S(R))$. This is the coarse substitute for asphericity: for a closed aspherical $M$, the universal cover $\widetilde M$ with the pulled-back metric is uniformly contractible.

**Bounded geometry.** A metric space has bounded geometry if it is quasi-isometric to a uniformly discrete space $\Gamma$ with $\sup_{\gamma} \\#\big(B(\gamma,R) \cap \Gamma\big) < \infty$ for all $R$. For Riemannian manifolds: injectivity radius bounded below, curvature bounded above.

**Bounded algebra (Pedersen–Weibel).** For a ring $R$ let $\mathcal{C}_Z(R)$ be the additive category of $Z$-graded free $R$-modules $A = \bigoplus_{z \in Z} A_z$ (locally finite) with morphisms $\phi = (\phi_{z',z})$ satisfying $\phi_{z',z} = 0$ whenever $d(z,z') > C_\phi$. The central computation is
$$K_i\big(\mathcal{C}_{\mathbb{R}^k}(R)\big) \;\cong\; K_{i-k}(R), \qquad L^{b}_{n}\big(\mathbb{R}^k;\mathbb{Z}\big) \;\cong\; L_{n-k}(\mathbb{Z}),$$
the algebraic-topology form of "bounded control over $\mathbb{R}^k$ = $k$-fold delooping".

**Bounded surgery exact sequence (Ferry–Pedersen).** For $M^n$ with control map to $Z$, $n \ge 5$:
$$\cdots \to H^{lf}_{n+1}\big(Z;\mathbb{L}\big) \xrightarrow{\ A_Z\ } L^{b}_{n+1}(Z) \to \mathcal{S}^{b}(M) \to H^{lf}_{n}\big(Z;\mathbb{L}\big) \xrightarrow{\ A_Z\ } L^{b}_{n}(Z),$$
where $H^{lf}_*(-;\mathbb{L})$ is locally finite homology with coefficients in the periodic surgery spectrum and $A_Z$ is the **coarse assembly map**. The conjecture is therefore equivalent to:

$$\textbf{(BHC)}\qquad A_X : H^{lf}_*\big(X;\mathbb{L}\big) \longrightarrow L^{b}_{*}(X) \ \text{ is an isomorphism for } X \text{ uniformly contractible, bounded geometry.}$$

This is the $L$-theoretic mirror of the **coarse Baum–Connes conjecture** $KX_*(X) \to K_*(C^*X)$ and, restricted to $X = \widetilde M$ for closed aspherical $M$ with $\pi_1 = \Gamma$, it implies the Novikov and Borel conjectures for $\Gamma$.

## 3. History & State of the Art (SOTA)

- **1965.** Siebenmann's thesis isolates the end obstruction $\sigma(\varepsilon) \in \widetilde K_0(\mathbb{Z}[\pi_1 \varepsilon])$ to completing an open manifold ($n \ge 6$) by a boundary — the first proof that geometry at infinity, not homotopy type, controls open manifolds.
- **1979–1985.** Chapman–Siebenmann's controlled Hilbert-cube-manifold theory; Quinn's *Ends of maps* I–II establish the controlled surgery machine and the local obstruction in $H^0(X;\mathbb{Z})$.
- **1985.** Pedersen–Weibel construct the non-connective delooping $K(\mathcal{C}_{\mathbb{R}^k}(R)) \simeq \Omega^{-k}K(R)$, making bounded algebra computable.
- **1990s.** Ferry–Pedersen's *Epsilon surgery theory* (1995) gives the bounded surgery exact sequence above and the bounded $\pi$–$\pi$ theorem. Ferry–Weinberger and Roe recast Novikov coarsely; Roe's CBMS lectures (1996) fix the coarse-geometric language. Dranishnikov–Ferry–Weinberger's étale approach (CPAM 1997) proves integral Novikov for finite-dimensional classifying spaces with suitable compactifications.
- **1998.** Yu: Novikov holds for groups with finite asymptotic dimension (and finite $B\Gamma$) — via coarse Baum–Connes.
- **2003.** Dranishnikov–Ferry–Weinberger, *Large Riemannian manifolds which are flexible* (Annals): the conjecture is **false without bounded geometry**. Simultaneously Dranishnikov proves finite asymptotic dimension $\Rightarrow$ integrally hyperspherical, confirming the conjecture in that class.
- **2012.** Guentner–Tessera–Yu prove stable topological rigidity for groups of finite decomposition complexity — the strongest general positive result. Bartels–Lück prove Borel for hyperbolic and CAT(0) groups.
- **2020.** Dranishnikov–Ferry–Weinberger, *An infinite-dimensional phenomenon in finite-dimensional metric topology* (Camb. J. Math.), sharpens the flexible examples using cohomological-dimension pathologies.

**Status:** open in the bounded-geometry case; false in general; proved for large explicit classes.

## 4. Partial Results / Verified Cases

| Class of $X$ | Result | Source |
|---|---|---|
| $X = \mathbb{R}^n$, $n \ge 5$ | $\mathcal{S}^b(\mathbb{R}^n) = 0$; bounded rigidity holds | Ferry–Pedersen 1995 |
| $X = \widetilde M$, $M$ closed nonpositively curved | Bounded/foliated rigidity; Borel holds | Farrell–Jones 1993 |
| $\Gamma$ hyperbolic or CAT(0), $X = E\Gamma$ | Farrell–Jones isomorphism $\Rightarrow$ (BHC) for $X$ | Bartels–Lück 2012 |
| $\operatorname{asdim} X < \infty$ | Integral coarse Novikov; injectivity of $A_X$; $X$ hyperspherical | Yu 1998; Dranishnikov 2003; Bartels 2003 |
| Finite decomposition complexity | Stable rigidity: $M \times \mathbb{R}^k \cong X \times \mathbb{R}^k$ | Guentner–Tessera–Yu 2012 |
| $X$ with $\overline{X}$ a $Z$-set compactification (contractible, finite-dim.) | Integral assembly injective | Dranishnikov–Ferry–Weinberger 1997 |
| Dimension $n \le 4$ | Open; surgery machinery unavailable ($n=3,4$) | — |
| **Not** bounded geometry, $n \ge 8$ | **Counterexample**: uniformly contractible $X$, $\mathcal{S}^b(X) \ne 0$ | DFW, Annals 2003 |

The DFW counterexamples are built from Dranishnikov's infinite-dimensional compacta of finite integral cohomological dimension; the resulting $X$ is uniformly contractible but has wildly non-uniform local topology — exactly what bounded geometry forbids.

## 5. Principal Obstacles

- **No group to induct on.** Ordinary Borel-type theorems exploit $\pi_1$ and Farrell–Jones-style induction over virtually cyclic subgroups. A general uniformly contractible bounded-geometry $X$ has no group action; the coarse category has no analogue of transfer, induction, or a Cayley-graph model.
- **Assembly is not a homology comparison.** $L^b_*(X)$ is not a homology theory in $X$ — it fails excision. Standard Mayer–Vietoris/descent arguments (the engine of Yu's and Bartels' proofs) need a *coarse decomposition*: finite asymptotic dimension or finite decomposition complexity. No known geometric hypothesis short of these produces the decomposition, and bounded geometry alone does not.
- **Expanders break the analytic route.** The coarse Baum–Connes conjecture — the $C^*$-analogue used as evidence — is **false** for bounded-geometry spaces built from expander graphs (Higson–Lafforgue–Skandalis 2002). So the analytic method cannot be pushed to the general bounded-geometry case, and its failure removes the main heuristic support for (BHC).
- **Uniform contractibility is not coarsely stable.** Being uniformly contractible is not a quasi-isometry invariant of the underlying discrete space, so one cannot replace $X$ by a combinatorially simpler quasi-isometric model without destroying the hypothesis.
- **Squeezing has a dimension-dependent radius.** Bartels' squeezing theorem converts small-controlled to bounded data only over spaces with controlled covering dimension at all scales; the constants blow up when $\operatorname{asdim} = \infty$.

## 6. The Gap

Proved: injectivity/isomorphism of $A_X$ when $X$ admits a *coarse decomposition* (finite asdim, FDC, or a $Z$-set compactification), plus geometric rigidity for universal covers of nonpositively curved manifolds. Conjectured: the same for **all** uniformly contractible bounded-geometry $X$.

The gap is one implication:
$$\text{bounded geometry} + \text{uniform contractibility} \ \Longrightarrow\ ?\ \text{a coarse decomposition sufficient for descent.}$$
There is no candidate proof of this implication, and no counterexample. Concretely: a uniformly contractible bounded-geometry manifold whose underlying discrete model coarsely contains an expander would be the natural test case — it is not known whether one exists, since expanders are not coarsely embeddable in Hilbert space but might still fail to be uniformly contractible in any thickening. Resolving that existence question would likely settle (BHC) one way or the other.

## 7. Current Research (as of June 2026)

- **Decomposition complexity.** Extending Guentner–Tessera–Yu from *stable* rigidity ($\times \mathbb{R}^k$) to genuine bounded rigidity; the obstruction lives in a $\varprojlim^1$-type term and is the focus of work in the Vanderbilt/Texas A&M coarse-geometry school. *(frontier — verify)*
- **Coarse assembly beyond expanders.** Isolating which failures of coarse Baum–Connes transfer to $L$-theory. $L$-theory has 4-periodicity and no analogue of the Kazhdan-property obstruction, so (BHC) may survive where coarse Baum–Connes dies. Several groups treat this as the most likely route to a positive answer for bounded geometry. *(frontier — verify)*
- **Farrell–Jones-driven inputs.** Bartels–Lück–Reich-style controlled algebra continues to feed new group classes (mapping class groups, $\mathrm{GL}_n(\mathbb{Z})$, lattices) into the $X = E\Gamma$ case.
- **Low dimensions.** $n = 4$ remains untouched: no bounded surgery, and Freedman-style disc embedding does not exist in the controlled setting.
- **Refined DFW examples.** Follow-ups to the 2020 Cambridge J. Math. paper aim to quantify how badly bounded geometry must fail — how much local dimension growth is needed for flexibility.

## 8. Future Work

1. **Decide the expander question.** Construct, or rule out, a uniformly contractible bounded-geometry manifold coarsely containing an expander sequence.
2. **A purely $L$-theoretic descent principle** requiring only bounded geometry, sidestepping Hilbert-space embeddability.
3. **Quantitative bounded geometry.** Introduce a numerical invariant interpolating between finite asdim and bounded geometry, and prove (BHC) as its value grows.
4. **Non-simply-connected-at-infinity examples.** Systematically test candidate counterexamples of Whitehead-manifold type equipped with bounded-geometry metrics.
5. **Dimension 4** via controlled Freedman theory over $\mathbb{R}^k$ for good coarse fundamental groups.

## 9. Key References

- **[Foundational]** L. C. Siebenmann. *The Obstruction to Finding a Boundary for an Open Manifold of Dimension Greater than Five.* Ph.D. thesis, Princeton University, 1965.
- **[Foundational]** E. K. Pedersen, C. Weibel. *A nonconnective delooping of algebraic K-theory.* In *Algebraic and Geometric Topology*, Springer Lecture Notes in Mathematics 1126, 1985.
- **[Foundational]** S. Ferry, E. K. Pedersen. *Epsilon surgery theory.* In *Novikov Conjectures, Index Theorems and Rigidity*, Vol. 2, LMS Lecture Note Series 227, Cambridge Univ. Press, 1995.
- **[Foundational]** F. Quinn. *Ends of maps, I.* Annals of Mathematics 110 (1979), 275–331.
- **[Survey]** J. Roe. *Index Theory, Coarse Geometry, and Topology of Manifolds.* CBMS Regional Conference Series 90, AMS, 1996.
- **[Survey]** S. Ferry, S. Weinberger. *A coarse approach to the Novikov conjecture.* In *Novikov Conjectures, Index Theorems and Rigidity*, Vol. 1, LMS Lecture Note Series 226, 1995.
- **[Counterexample]** A. N. Dranishnikov, S. Ferry, S. Weinberger. *Large Riemannian manifolds which are flexible.* Annals of Mathematics 157 (2003), 919–938.
- **[Counterexample]** A. N. Dranishnikov, S. Ferry, S. Weinberger. *An infinite-dimensional phenomenon in finite-dimensional metric topology.* Cambridge Journal of Mathematics 8 (2020), 95–147.
- **[SOTA]** G. Yu. *The Novikov conjecture for groups with finite asymptotic dimension.* Annals of Mathematics 147 (1998), 325–355.
- **[SOTA]** E. Guentner, R. Tessera, G. Yu. *A notion of geometric complexity and its application to topological rigidity.* Inventiones Mathematicae 189 (2012), 315–357.
- **[SOTA]** A. Bartels, W. Lück. *The Borel conjecture for hyperbolic and CAT(0)-groups.* Annals of Mathematics 175 (2012), 631–689.
- **[Related]** N. Higson, V. Lafforgue, G. Skandalis. *Counterexamples to the Baum–Connes conjecture.* GAFA 12 (2002), 330–354.
- **[Related]** A. Bartels. *Squeezing and higher algebraic K-theory.* K-Theory 28 (2003), 19–37.
- **[Related]** A. N. Dranishnikov. *On hypersphericity of manifolds with finite asymptotic dimension.* Transactions of the AMS 355 (2003), 155–167.
- **[Textbook]** S. Chang, S. Weinberger. *A Course on Surgery Theory.* Annals of Mathematics Studies 211, Princeton University Press, 2021.

## 10. Worked Example / Concrete Special Case

**Case $X = \mathbb{R}^n$, $n \ge 5$, control space $Z = \mathbb{R}^n$ (identity control map).**

$\mathbb{R}^n$ is uniformly contractible ($S(R) = R$) and of bounded geometry. Compute $\mathcal{S}^b(\mathbb{R}^n)$ from the bounded surgery sequence.

*Step 1 — the $L$-groups.* By Ferry–Pedersen's bounded $L$-theory over Euclidean space,
$$L^{b}_{m}(\mathbb{R}^n;\mathbb{Z}) \;\cong\; L_{m-n}(\mathbb{Z}), \qquad L_{j}(\mathbb{Z}) = \mathbb{Z},\, \mathbb{Z}/2,\, 0,\, 0 \ \text{ for } j \equiv 0,1,2,3 \ (\mathrm{mod}\ 4)$$
(with $L_0 = \mathbb{Z}$ via the signature/8, $L_2 = \mathbb{Z}/2$ via Arf; the indexing convention places $\mathbb{Z}$ in degree $0$). So $L^b_n(\mathbb{R}^n) \cong L_0(\mathbb{Z}) = \mathbb{Z}$ and $L^b_{n+1}(\mathbb{R}^n) \cong L_1(\mathbb{Z}) = 0$.

*Step 2 — the homology.* $\mathbb{R}^n$ is a locally finite $\mathbb{L}$-homology "point at infinity": $H^{lf}_m(\mathbb{R}^n;\mathbb{L}) \cong \pi_{m-n}(\mathbb{L}) \cong L_{m-n}(\mathbb{Z})$ by locally finite Poincaré duality $H^{lf}_m(\mathbb{R}^n;\mathbb{L}) \cong H^{n-m}(\mathrm{pt};\mathbb{L})$.

*Step 3 — assembly.* Under these identifications $A_{\mathbb{R}^n}$ is the identity of $L_{m-n}(\mathbb{Z})$ in every degree — the $n$-fold delooping of the assembly map over a point, which is trivially an isomorphism. The sequence
$$0 = L^b_{n+1} \to \mathcal{S}^{b}(\mathbb{R}^n) \to H^{lf}_n(\mathbb{R}^n;\mathbb{L}) = \mathbb{Z} \xrightarrow{\ \cong\ } L^b_n(\mathbb{R}^n) = \mathbb{Z}$$
forces $\mathcal{S}^{b}(\mathbb{R}^n) = 0$.

*Conclusion.* Any open $n$-manifold $M$ ($n \ge 5$) admitting a bounded homotopy equivalence to $\mathbb{R}^n$ over $\mathbb{R}^n$ is boundedly homeomorphic to $\mathbb{R}^n$.

**Contrast: why the metric hypotheses do the work.** The Whitehead manifold $\mathrm{Wh}^3$ is contractible, hence homotopy equivalent to $\mathbb{R}^3$, but not homeomorphic to it (it is not simply connected at infinity). It even satisfies $\mathrm{Wh}^3 \times \mathbb{R} \cong \mathbb{R}^4$. The homotopy equivalence $\mathrm{Wh}^3 \times \mathbb{R}^2 \to \mathbb{R}^5$ can be made proper but *not* bounded with respect to any bounded-geometry uniformly contractible metric: the Whitehead continuum's infinitely nested tori force the contraction radius $S(R)$ to grow without bound relative to $R$. The conjecture asserts that this failure mode — non-uniform contraction — is the *only* obstruction. The DFW flexible manifolds show that once bounded geometry is dropped, a second, genuinely different obstruction appears, living in the discrepancy between integral and rational cohomological dimension at infinity.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*