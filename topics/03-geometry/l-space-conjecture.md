---
id: 03-geometry/l-space-conjecture
title: "L-space Conjecture"
topic: 03-geometry
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# L-space Conjecture

> **Topic:** Algebraic & Differential Geometry · **ID:** `03-geometry/l-space-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Let $Y$ be a closed, connected, orientable, **irreducible** rational homology $3$-sphere (a QHS$^3$: $b_1(Y)=0$, so $H_1(Y;\mathbb{Z})$ is finite). The conjecture asserts the equivalence of three conditions drawn from three different areas of $3$-manifold theory:

1. **(Floer-theoretic)** $Y$ is **not** an L-space, i.e. $\operatorname{rk}_{\mathbb{F}}\widehat{HF}(Y) > |H_1(Y;\mathbb{Z})|$, where $\mathbb{F}=\mathbb{Z}/2\mathbb{Z}$.
2. **(Algebraic)** $\pi_1(Y)$ is **left-orderable**: it admits a strict total order $<$ with $g<h \Rightarrow fg<fh$ for all $f$.
3. **(Foliation-theoretic)** $Y$ admits a **coorientable taut foliation** (CTF): a codimension-one $C^\infty$ foliation $\mathcal{F}$, transversely orientable, such that every leaf meets a closed transverse loop.

A complete proof requires establishing all six implications (three are known or reduce to known ones; see §4). A disproof requires a single irreducible QHS$^3$ satisfying one condition and failing another — e.g. a non-L-space with non-left-orderable $\pi_1$, or a left-orderable non-L-space carrying no taut foliation.

Irreducibility is essential: $Y=\Sigma(2,3,5)\,\\#\,\Sigma(2,3,5)$-type reducible examples and reducible connected sums break (3) trivially. For $b_1(Y)\ge 1$ the trichotomy holds for soft reasons: Gabai produces a taut foliation, $\pi_1$ surjects onto $\mathbb{Z}$ hence is left-orderable, and $Y$ is not a QHS$^3$.

## 2. Mathematical Foundations

**Heegaard Floer homology.** Ozsváth–Szabó associate to a closed oriented $3$-manifold $Y$ with $\mathrm{Spin}^c$ structure $\mathfrak{s}$ groups $\widehat{HF}(Y,\mathfrak{s})$, $HF^+$, $HF^-$, $HF^\infty$. For a QHS$^3$,
$$\chi\big(\widehat{HF}(Y,\mathfrak{s})\big)=1,\qquad \operatorname{rk}_{\mathbb{F}}\widehat{HF}(Y)=\sum_{\mathfrak{s}\in \mathrm{Spin}^c(Y)}\operatorname{rk}\widehat{HF}(Y,\mathfrak{s})\ \ge\ |\mathrm{Spin}^c(Y)|=|H_1(Y;\mathbb{Z})|.$$
$Y$ is an **L-space** when equality holds, equivalently $HF_{\mathrm{red}}(Y)=0$, equivalently $HF^+(Y,\mathfrak{s})\cong \mathcal{T}^+=\mathbb{F}[U,U^{-1}]/U\mathbb{F}[U]$ for every $\mathfrak{s}$. Lens spaces and all spherical space forms are L-spaces; the name records that $L(p,q)$ is the model case.

**Left-orderability.** For a countable group $G$, $G$ is left-orderable iff $G$ is torsion-free and admits a faithful action by orientation-preserving homeomorphisms of $\mathbb{R}$; equivalently there is a positive cone $P\subset G$ with $P\cdot P\subseteq P$ and $G = P\sqcup P^{-1}\sqcup\{1\}$. Left-orderability of $\pi_1(Y)$ for $Y$ irreducible is thus a statement about $1$-dimensional dynamics of $\pi_1(Y)$.

**Taut foliations and contact geometry.** By Eliashberg–Thurston, a $C^2$ CTF on $Y\neq S^1\times S^2$ is $C^0$-approximated by weakly symplectically fillable, hence tight, contact structures $\xi_\pm$. Ozsváth–Szabó's contact invariant $c(\xi)\in\widehat{HF}(-Y)$ is nonzero for such $\xi$ and obstructs $Y$ being an L-space; combined with the adjunction/genus bounds of *Holomorphic disks and genus bounds*, one gets
$$Y \text{ admits a CTF} \ \Longrightarrow\ Y \text{ is not an L-space.}$$
Bowden and Kazez–Roberts extended this to $C^0$ foliations, so the regularity in (3) is immaterial.

**Slope detection (the relative theory).** For $M$ compact irreducible with $\partial M=T^2$, one studies sets of boundary slopes $\alpha\in \mathrm{Sl}(M)\cong\mathbb{Q}\cup\{\infty\}$:
$$\mathcal{L}(M)=\{\alpha: M(\alpha)\text{ is an L-space}\},\quad \mathcal{NLS},\ \mathcal{LO}(M),\ \mathcal{CTF}(M)$$
of L-space, left-order-detected and foliation-detected slopes. Hanselman–Rasmussen–Watson encode $\widehat{CFD}(M)$ as a collection of immersed curves with local systems in $\partial M\setminus\{pt\}$, giving the **L-space gluing theorem**: for boundary-incompressible $M_1,M_2$ glued along $\varphi:\partial M_1\to\partial M_2$,
$$M_1\cup_\varphi M_2 \text{ is an L-space}\iff \varphi\big(\mathcal{L}^\circ(M_1)\big)\cup \mathcal{L}^\circ(M_2)=\mathrm{Sl}(\partial M_2).$$
The conjecture is then predicted to hold "slope-wise": $\mathcal{L}^{\circ}(M)$, the complement of the $\mathcal{LO}$-detected slopes, and the complement of the $\mathcal{CTF}$-detected slopes should coincide.

## 3. History & State of the Art (SOTA)

- **2004.** Ozsváth–Szabó prove taut foliation $\Rightarrow$ non-L-space (*Holomorphic disks and genus bounds*), the first bridge between the analytic and foliation sides.
- **2005.** Boyer–Rolfsen–Wiest, *Orderable 3-manifold groups*, systematize left-orderability of $3$-manifold groups and settle the Seifert fibered case in terms of horizontal foliations.
- **2013.** Boyer–Gordon–Watson (*Math. Ann.*) formulate the conjecture "$Y$ irreducible QHS$^3$ is a non-L-space $\iff$ $\pi_1(Y)$ is LO", after verifying it for all geometric non-hyperbolic $Y$ and for many branched covers.
- **2015.** Juhász's survey adds the taut-foliation clause explicitly, giving the now-standard tripartite form.
- **2016–2020.** Boyer–Clay develop slope detection for graph manifolds; Rasmussen–Rasmussen compute L-space interval structure for graph manifolds and cables; Hanselman–J. Rasmussen–S. Rasmussen–Watson complete the **graph manifold case** of the full conjecture.
- **2018–2020.** Culler–Dunfield give practical certificates for left-orderability via $\widetilde{PSL_2\mathbb{R}}$ representations; Dunfield verifies the conjecture computationally for $307{,}301$ hyperbolic QHS$^3$s from the census, finding no counterexample and confirming all three properties agree in every case decided.

Status as of 2026: no counterexample and no proof of any implication in the hyperbolic setting. The consensus view treats the LO $\Leftrightarrow$ CTF equivalence as the most tractable pair, with the Floer side coupled to it via bordered invariants.

## 4. Partial Results / Verified Cases

- **All non-hyperbolic geometries.** The conjecture holds for $Y$ modelled on $S^3$, $S^2\times\mathbb{R}$, $\mathbb{E}^3$, $\mathrm{Nil}$, $\mathrm{Sol}$, $\mathbb{H}^2\times\mathbb{R}$, $\widetilde{PSL_2\mathbb{R}}$ (Boyer–Gordon–Watson, building on Eisenbud–Hirsch–Neumann, Jankins–Neumann, Naimi, Lisca–Stipsicz). For Seifert fibered QHS$^3$s with Euler number $e\neq 0$ the three conditions are each equivalent to the existence of a **horizontal** foliation, decided by an explicit arithmetic condition on the Seifert invariants.
- **Graph manifolds.** Fully proved (Hanselman–Rasmussen–Rasmussen–Watson, *Compositio Math.* 156 (2020)): a closed graph manifold QHS$^3$ is a non-L-space $\iff$ LO $\iff$ carries a CTF.
- **Manifolds with $b_1\ge 1$.** All three conditions hold automatically (Gabai; Boyer–Rolfsen–Wiest).
- **Surgeries and cables.** For $K\subset S^3$, $S^3_{p/q}(K)$ is an L-space for some slope only if $K$ is fibered and strongly quasipositive; the L-space slopes form an interval $[2g(K)-1,\infty]$ (Ozsváth–Szabó, Hedden, Hom, Rasmussen–Rasmussen). Cables and satellites: the conjecture is verified for all cable-of-graph-manifold and many satellite constructions via immersed-curve calculus.
- **Branched covers.** Boyer–Gordon–Watson and Gordon–Lidman verify the LO/L-space equivalence for large families of cyclic branched covers of alternating and quasipositive links; Boileau–Boyer–Gordon handle branched covers of quasipositive links.
- **Census verification.** Dunfield (2020): $307{,}301$ hyperbolic QHS$^3$s tested; L-space status vs. LO vs. CTF agreed in every case where all three could be computed.
- **One-way implication, all $Y$.** CTF $\Rightarrow$ non-L-space (Ozsváth–Szabó; $C^0$ case Bowden, Kazez–Roberts).

## 5. Principal Obstacles

- **No functor connects the sides.** Left-orderability is a property of a discrete group with no known chain complex; Heegaard Floer homology is defined by counting pseudoholomorphic curves. There is no construction turning a nontrivial class in $HF_{\mathrm{red}}(Y)$ into an action of $\pi_1(Y)$ on $\mathbb{R}$, nor conversely.
- **The missing direction is a *construction* problem.** Proving non-L-space $\Rightarrow$ CTF requires building a foliation from the vanishing of an obstruction. Gabai's sutured hierarchy builds taut foliations from nontrivial $H_2$, which QHS$^3$s lack by definition; there is no substitute existence theorem in the rational homology sphere setting.
- **Left-orderability is not local.** LO of $\pi_1(Y)$ can fail for reasons invisible to any finite quotient or homology: it is equivalent to a $\widetilde{PSL_2\mathbb{R}}$-type action existing, and the space of such actions is not deformation-connected. Culler–Dunfield's certificates only prove LO; there is no general method to certify **non**-LO for hyperbolic $Y$ other than exhibiting torsion or using explicit finite presentations.
- **Bordered gluing degenerates.** The immersed-curve machinery converts the closed problem to a slope-detection problem, but for hyperbolic pieces the loci $\mathcal{L}^\circ(M)$, $\mathcal{LO}(M)$, $\mathcal{CTF}(M)$ are computed by three unrelated methods; agreement is only known when at least one piece is Seifert or graph.
- **Taut foliations are unstable under Dehn filling.** A CTF on $M$ need not extend over a filling torus with a given slope, and the set of slopes for which it does is not known to be closed or an interval in the hyperbolic case.

## 6. The Gap

Proved: CTF $\Rightarrow$ non-L-space (all $Y$); the full trichotomy for non-hyperbolic geometries and graph manifolds; large but non-generic families of surgeries and branched covers.

Missing: **every implication for hyperbolic $Y$**. Concretely, the three open steps are

1. non-L-space $\Rightarrow$ CTF — an existence theorem for foliations from Floer-theoretic non-vanishing;
2. non-L-space $\Rightarrow$ LO — an existence theorem for $\pi_1$-actions on $\mathbb{R}$;
3. LO $\Rightarrow$ CTF (or $\Rightarrow$ non-L-space) — turning a $1$-dimensional dynamical structure into a $2$-plane field.

The sharpest formulation of the barrier: for a hyperbolic $M$ with torus boundary, prove $\mathcal{L}^\circ(M)=\mathrm{Sl}(\partial M)\setminus\mathcal{CTF}(M)$. All known proofs of this identity use a Seifert or graph structure to enumerate slopes; no argument survives when the JSJ decomposition is trivial and the piece is hyperbolic.

## 7. Current Research (as of June 2026)

- **Immersed-curve program** (Hanselman, J. Rasmussen, Watson; Princeton/Cambridge/Sherbrooke–Glasgow): extend the L-space gluing theorem to a "foliation gluing theorem" and a "LO gluing theorem", making all three slope sets computable from curve data.
- **Foliation construction from Heegaard splittings** — building CTFs on manifolds of Heegaard genus $2$ and on branched covers, e.g. work of Krishna and collaborators on taut foliations of surgeries on knots. *(frontier — verify)*
- **Instanton/SU(2) route** (Kronheimer–Mrowka circle, Baldwin–Sivek, Zentner): $SU(2)$-abelian and $\widetilde{PSL_2\mathbb{R}}$ representation varieties as a bridge, using $I^\natural$ and the conjectural $\widehat{HF}\cong I^\\#$ isomorphism.
- **Computational frontier**: extending Dunfield-style census verification into the $\ge 10$-tetrahedron range and to non-census surgeries; ongoing SnapPy/Regina work. *(frontier — verify)*
- **Skepticism**: several researchers publicly regard the LO clause as the likeliest to fail, and search programs targeting non-LO non-L-spaces among $2$-bridge and branched-cover families are active. *(frontier — verify)*

## 8. Future Work

- Prove the conjecture for **all Seifert-glued unions with one hyperbolic piece**, the first case beyond graph manifolds.
- Develop a Floer-theoretic invariant valued in group actions — e.g. a $\pi_1$-equivariant refinement of $\widehat{HF}$ from which a positive cone can be extracted.
- Establish that $\mathcal{CTF}(M)$ is a closed interval for hyperbolic $M$ (known for graph manifolds), which alone would import the Floer-side interval structure.
- Settle the conjecture for **cyclic branched covers of alternating knots**, where L-space status is combinatorially decidable but LO is not.
- Either prove a general non-LO criterion for hyperbolic $3$-manifold groups, or produce the expected counterexample.

## 9. Key References

- **[Foundational]** P. Ozsváth, Z. Szabó. *Holomorphic disks and topological invariants for closed three-manifolds.* Annals of Mathematics 159 (2004), 1027–1158.
- **[Foundational]** P. Ozsváth, Z. Szabó. *Holomorphic disks and genus bounds.* Geometry & Topology 8 (2004), 311–334.
- **[Foundational]** S. Boyer, D. Rolfsen, B. Wiest. *Orderable 3-manifold groups.* Annales de l'Institut Fourier 55 (2005), 243–288.
- **[Foundational / Conjecture]** S. Boyer, C. McA. Gordon, L. Watson. *On L-spaces and left-orderable fundamental groups.* Mathematische Annalen 356 (2013), 1213–1245.
- **[Foundational]** Y. Eliashberg, W. Thurston. *Confoliations.* University Lecture Series 13, American Mathematical Society, 1998.
- **[SOTA]** J. Hanselman, J. Rasmussen, S. D. Rasmussen, L. Watson. *L-spaces, taut foliations, and graph manifolds.* Compositio Mathematica 156 (2020), 604–612.
- **[SOTA]** S. Boyer, A. Clay. *Foliations, orders, representations, L-spaces and graph manifolds.* Advances in Mathematics 310 (2017), 159–234.
- **[SOTA]** J. Hanselman, J. Rasmussen, L. Watson. *Bordered Floer homology for manifolds with torus boundary via immersed curves.* arXiv:1604.03466.
- **[SOTA]** J. Rasmussen, S. D. Rasmussen. *L-space intervals for graph manifolds and cables.* Compositio Mathematica 153 (2017), 1008–1049.
- **[Computational]** N. Dunfield. *Floer homology, group orderability, and taut foliations of hyperbolic 3-manifolds.* Algebraic & Geometric Topology 20 (2020), 3001–3030.
- **[Computational]** M. Culler, N. Dunfield. *Orderability and Dehn filling.* Geometry & Topology 22 (2018), 1405–1457.
- **[Regularity]** J. Bowden. *Approximating $C^0$-foliations by contact structures.* Geometric and Functional Analysis 26 (2016), 1255–1296.
- **[Regularity]** W. Kazez, R. Roberts. *$C^0$ approximations of foliations.* Geometry & Topology 21 (2017), 3601–3657.
- **[Survey]** A. Juhász. *A survey of Heegaard Floer homology.* In *New Ideas in Low Dimensional Topology*, World Scientific, 2015, 237–296.
- **[Survey]** A. Clay, D. Rolfsen. *Ordered Groups and Topology.* Graduate Studies in Mathematics 176, American Mathematical Society, 2016.

## 10. Worked Example / Concrete Special Case

Compare two Brieskorn integer homology spheres, both Seifert fibered over $S^2$ with three exceptional fibers, both irreducible, both with $|H_1|=1$.

**(a) $Y_1=\Sigma(2,3,5)$, the Poincaré sphere.** Seifert Euler number $e=-\tfrac{1}{30}$; $\pi_1(Y_1)$ is the binary icosahedral group $2I$, of order $120$.

- *Floer side.* $Y_1$ bounds the negative-definite $E_8$-plumbing, so it is a lens-space surgery ($+1$-surgery on the left trefoil) and $\operatorname{rk}\widehat{HF}(Y_1)=1=|H_1(Y_1;\mathbb{Z})|$. **L-space.**
- *Order side.* $\pi_1$ has torsion (elements of order $10$, $6$, $4$), and left-orderable groups are torsion-free. **Not left-orderable.**
- *Foliation side.* By Eisenbud–Hirsch–Neumann/Jankins–Neumann/Naimi, a Seifert QHS$^3$ with $e\neq0$ has a CTF iff it has a horizontal one, iff its Seifert invariants are realized by a triple $\left(\tfrac{\beta_1}{\alpha_1},\tfrac{\beta_2}{\alpha_2},\tfrac{\beta_3}{\alpha_3}\right)$ admitting $0<a<m$ with $\tfrac{a}{m}<\tfrac{\beta_i}{\alpha_i}<\tfrac{a+1}{m}$ up to the standard normalisation. For $(2,3,5)$ the required rational interval is empty. **No CTF.**

All three conditions fail together: consistent with the conjecture.

**(b) $Y_2=\Sigma(2,3,7)$, i.e. $-1$-surgery on the right trefoil.** Here $e=-\tfrac{1}{42}$.

- *Floer side.* Ozsváth–Szabó's surgery formula for the trefoil gives $HF^+_{\mathrm{red}}(Y_2)\cong\mathbb{F}$, hence
$$\operatorname{rk}_{\mathbb{F}}\widehat{HF}(\Sigma(2,3,7))=1+2\cdot 1=3>1=|H_1|.$$
**Not an L-space.** (Contrast: $+n$-surgery on the trefoil is an L-space exactly for slopes $\ge 2g(K)-1=1$, so $\Sigma(2,3,5)=S^3_{+1}$ is one and $\Sigma(2,3,7)=S^3_{-1}$ is not.)
- *Order side.* $\pi_1(Y_2)$ is a central extension $1\to\mathbb{Z}\to\pi_1(Y_2)\to \Delta(2,3,7)\to 1$ with $\Delta(2,3,7)$ the hyperbolic triangle group. The central $\mathbb{Z}$ is generated by the regular fiber $h$, and $\pi_1(Y_2)$ embeds in $\widetilde{PSL_2\mathbb{R}}$, which acts faithfully on $\mathbb{R}$ by orientation-preserving homeomorphisms. **Left-orderable.**
- *Foliation side.* The Jankins–Neumann/Naimi realization condition is satisfied for $(2,3,7)$: taking $m=7$, $a=1$ one finds a rational $\tfrac{a}{m}$ separating the normalized Seifert data, so $Y_2$ carries a horizontal, hence taut and coorientable, foliation. **CTF exists.**

All three hold together. Note the consistency check with the general theorem: the CTF on $\Sigma(2,3,7)$ forces $HF_{\mathrm{red}}\ne 0$, matching the rank-$3$ computation. The family $\Sigma(2,3,6n\pm 1)$ interpolates: $\Sigma(2,3,6n-1)=S^3_{-1/n}(\text{trefoil})$ is never an L-space for $n\ge1$ and is always LO with a horizontal foliation, while $\Sigma(2,3,5)$ is the unique L-space in the Brieskorn homology sphere family. What no argument of this type reaches is the hyperbolic case, where neither the Seifert arithmetic nor the surgery formula is available.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*