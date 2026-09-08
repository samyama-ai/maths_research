---
id: 04-topology/3d-3d-correspondence
title: "3D-3D Correspondence"
topic: 04-topology
status: empirically-supported
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# 3D-3D Correspondence

> **Topic:** Topology & Knot Theory · **ID:** `04-topology/3d-3d-correspondence` · **Status:** empirically-supported

## 1. Problem Statement / Conjecture

The 3d-3d correspondence asserts a functorial dictionary between three-manifold topology and three-dimensional supersymmetric gauge theory. Compactifying the six-dimensional $(2,0)$ superconformal theory $\mathcal{T}[\mathfrak{g}]$ of ADE type $\mathfrak{g}$ on a 3-manifold $M$ (with a partial topological twist) is conjectured to produce a 3d $\mathcal{N}=2$ theory $T[M;\mathfrak{g}]$ whose infrared physics is a topological invariant of $M$. Concretely:

1. **(Invariance)** $T[M;\mathfrak{g}]$ depends only on the homeomorphism type of $M$ (plus a framing/flavor-symmetry decoration), not on the triangulation or Heegaard/surgery presentation used to build it.
2. **(Moduli = character variety)** The moduli space of supersymmetric vacua of $T[M;\mathfrak{g}]$ on $\mathbb{R}^2\times S^1$ is isomorphic to the $G_{\mathbb{C}}$-character variety of $\pi_1(M)$, $G_\mathbb{C} = $ complexification of the compact group with Lie algebra $\mathfrak{g}$.
3. **(Partition functions = quantum invariants)** Supersymmetric partition functions of $T[M;\mathfrak{g}]$ on curved backgrounds compute quantum invariants of $M$: the squashed sphere $S^3_b$ partition function equals the partition function of complex Chern–Simons theory at level $k=1$ (equivalently, the Andersen–Kashaev Teichmüller TQFT invariant); the superconformal index equals the 3d index of $M$; half-index/$D^2\times_q S^1$ partition functions produce the $\hat{Z}$ (homological block) invariants.
4. **(Gluing)** Cutting $M$ along a surface $\Sigma$ corresponds to gauging the flavor symmetry associated to $\Sigma$; disjoint union corresponds to tensor product.

A complete resolution requires: (a) an intrinsic mathematical definition of $T[M;\mathfrak{g}]$ independent of the physics of the (2,0) theory (which itself has no rigorous construction), and (b) proofs of the equalities in (2)-(4) for all $M$ and all $\mathfrak{g}$, including non-hyperbolic $M$, reducible flat connections, and higher rank.

**Status:** empirically supported — verified in a large but structurally restricted family of cases (Section 4), with known failures of the naive algorithmic construction (Section 5).

## 2. Mathematical Foundations

**Character variety.** For $M$ compact oriented 3-manifold with torus boundary and $G_\mathbb{C}=SL(2,\mathbb{C})$,
$$\mathcal{X}(M)=\mathrm{Hom}(\pi_1(M),SL(2,\mathbb{C}))/\!\!/ SL(2,\mathbb{C}),$$
and restriction to $\partial M$ gives a Lagrangian $\mathcal{L}_M\subset \mathcal{X}(T^2)=(\mathbb{C}^\times\times\mathbb{C}^\times)/\mathbb{Z}_2$ with coordinates $(\ell,m)$ (eigenvalues of longitude and meridian holonomy), with respect to $\omega = \frac{d\ell}{\ell}\wedge\frac{dm}{m}$. The defining polynomial of the top-dimensional component is the **A-polynomial** $A_M(\ell,m)$ (Cooper–Culler–Gillet–Long–Shalen, 1994).

**Ideal triangulation and gluing equations.** Let $M = \bigcup_{i=1}^{N}\Delta_i$ be an ideal triangulation. Each tetrahedron carries a shape $z_i\in\mathbb{C}\setminus\{0,1\}$ with
$$z_i' = \frac{1}{1-z_i},\qquad z_i''=1-\frac{1}{z_i},\qquad z_iz_i'z_i''=-1 .$$
Thurston's gluing equations, one per edge $e$,
$$\prod_i z_i^{a_{ei}}(z_i')^{b_{ei}}(z_i'')^{c_{ei}}=1,$$
together with cusp equations cut out the **deformation variety**; solutions with $\operatorname{Im}z_i>0$ give the hyperbolic structure and
$$\mathrm{Vol}(M)=\sum_{i=1}^N D(z_i),\qquad D(z)=\operatorname{Im}\mathrm{Li}_2(z)+\arg(1-z)\log|z| .$$

**The tetrahedron theory.** $T_\Delta$ is a free chiral multiplet of charge $+1$ under $U(1)$ with a background Chern–Simons term at level $-\tfrac12$; its $S^3_b$ partition function is the non-compact quantum dilogarithm
$$Z_\Delta(x)=\Phi_b(x)=\prod_{r=0}^{\infty}\frac{1-e^{2\pi b(x+ i b(r+\frac12))}}{1-e^{2\pi b^{-1}(x - i b^{-1}(r+\frac12))}},\qquad Q=b+b^{-1}.$$
Dimofte–Gaiotto–Gukov build $T[M]$ by taking $\bigotimes_i T_{\Delta_i}$, acting by an $Sp(2N,\mathbb{Z})$ symplectic change of polarization encoding the gluing, and adding superpotential terms for internal edges.

**Partition function identities (conjectural).**
$$Z_{S^3_b}\big[T[M]\big](\mu)\;=\;Z^{CS}_{SL(2,\mathbb{C}),\,k=1}[M](\mu)\;\sim_{b\to0}\;\exp\!\Big(\tfrac{1}{2\pi b^2}\big(\mathrm{Vol}(M)+i\,\mathrm{CS}(M)\big)\Big),$$
$$\mathcal{I}\big[T[M]\big](m,\zeta;q)=\mathcal{I}_M(m,\zeta;q)\ \ \text{(3d index of Dimofte–Gaiotto–Gukov)},$$
$$Z_{D^2\times_qS^1}\big[T[M]\big]\;\rightsquigarrow\;\hat{Z}_a(q)\in q^{\Delta_a}\mathbb{Z}[[q]],\quad Z_{CS}^{SU(2)}[M]\ \text{recovered as}\ q\to\ \text{root of unity}.$$
Quantization of $\mathcal{L}_M$ gives the operator $\hat{A}_M(\hat\ell,\hat m;q)$ annihilating the colored Jones polynomials (the AJ conjecture), which appears as the Ward identity of $T[M]$ with a Wilson line.

## 3. History & State of the Art

- **2009–2010.** Alday–Gaiotto–Tachikawa establish the 4d analogue (AGT); Gaiotto's theory of class $\mathcal{S}$ makes the "compactify the (2,0) theory on a manifold" paradigm systematic.
- **2011.** Terashima–Yamazaki construct $T[M]$ for mapping tori of once-punctured torus, matching $SL(2,\mathbb{R})$ Chern–Simons/Teichmüller TQFT. Dimofte–Gaiotto–Gukov, *Gauge Theories Labelled by Three-Manifolds* (CMP 2014), give the general tetrahedron-gluing algorithm and the name.
- **2013.** Dimofte–Gaiotto–Gukov define the **3d index** $\mathcal{I}_M$ purely combinatorially from a triangulation and prove (with Garoufalidis) invariance results; Garoufalidis–Hodgson–Rubinstein–Segerman relate its convergence to 1-efficient triangulations.
- **2013–2016.** Cordova–Jafferis derive $SL(2,\mathbb{C})$ Chern–Simons at level $k$ from M5-branes on the squashed $S^3_b$, giving the first "first-principles" derivation of the $k=1$ statement. Andersen–Kashaev's Teichmüller TQFT gives a rigorous state-integral model matching $Z_{S^3_b}$.
- **2017–2021.** Gukov–Putrov–Vafa and Gukov–Pei–Putrov–Vafa introduce $\hat{Z}_a(q)$ for negative-definite plumbed 3-manifolds; Gukov–Manolescu define the two-variable series $F_K(x,q)$ for knot complements. Ekholm–Gruen–Gukov–Kucharski–Park–Sułkowski extend to large $N$.
- **2020–2025.** Higher-rank $\hat{Z}$ (Park), $\hat{Z}$ for non-plumbed and Dehn-surgered manifolds, and false/mock modularity of $\hat{Z}$; rigorous convergence results for state integrals (Garoufalidis–Gu–Mariño).

## 4. Partial Results / Verified Cases

- **Hyperbolic knot complements with small triangulations.** $T[M]$ constructed and checked for $4_1$, $5_2$, $6_1$, $6_2$, $6_3$, and all census manifolds with $N\le 5$ ideal tetrahedra; $S^3_b$ partition functions match Andersen–Kashaev invariants and reproduce $\mathrm{Vol}+i\,\mathrm{CS}$ in the $b\to0$ limit to $>30$ decimal digits numerically.
- **3d index.** Garoufalidis–Hodgson–Rubinstein–Segerman: $\mathcal{I}_M(m,\zeta;q)$ converges and is a topological invariant for all 1-efficient ideal triangulations of hyperbolic $M$ with $\ge 1$ cusp; verified over the SnapPy census (thousands of manifolds, $N\le 8$).
- **Mapping tori.** For once-punctured-torus bundles with monodromy $\varphi\in SL(2,\mathbb{Z})$ written in $L,R$ generators, Terashima–Yamazaki and Dimofte give $T[M]$ explicitly and prove mapping-class-group consistency of the $Sp(2,\mathbb{Z})$ representation.
- **Seifert-fibered and plumbed manifolds.** For negative-definite plumbing trees, $\hat{Z}_a(q)$ is defined by an explicit contour integral and proven to be a topological invariant under Neumann moves (Gukov–Pei–Putrov–Vafa); the $q\to e^{2\pi i/k}$ radial limit reproduces $SU(2)_k$ WRT invariants in verified cases including Brieskorn spheres $\Sigma(2,3,5)$, $\Sigma(2,3,7)$.
- **$\mathfrak{g}=\mathfrak{su}(2)$ only, plus partial $\mathfrak{su}(N)$.** Higher-rank gluing rules exist for $\mathfrak{su}(N)$ via $N$-triangulations (Fock–Goncharov coordinates); verified for $\mathfrak{su}(3)$ on $4_1$.
- **Lens spaces and $S^3$:** $T[L(p,1)]$ and $T[S^3]$ identified with explicit abelian theories; closed-manifold cases match Chern–Simons at level 1.

## 5. Principal Obstacles

- **No mathematical definition of the (2,0) theory.** The correspondence's source is a 6d superconformal field theory with no Lagrangian and no rigorous construction; every statement is derived from string-theory dualities rather than axioms.
- **Triangulation dependence and missing branches.** The DGG algorithm only sees flat connections visible in the deformation variety. Abelian/reducible flat connections and components of $\mathcal{X}(M)$ not detected by a given triangulation are lost, so $T[M]$ can depend on the triangulation. Known failures: triangulations that are not 1-efficient give non-invariant indices; some manifolds admit no triangulation with a positively oriented solution.
- **Closed 3-manifolds.** The construction is intrinsically cusped: gluing along tori requires flavor symmetries, and closing off requires an infrared-singular gauging. $T[M]$ for closed $M$ is often "bad" (non-isolated vacua, unbounded operators), so partition functions diverge.
- **Non-hyperbolic geometry.** For Seifert-fibered or graph manifolds the character variety is positive-dimensional and non-reduced; saddle-point matching with $\mathrm{Vol}+i\mathrm{CS}$ degenerates.
- **Analytic control.** State integrals are not absolutely convergent in general; proving the $b\to0$ asymptotics rigorously requires resurgence-level control of transseries whose Stokes data is only conjectural.
- **Higher rank.** Fock–Goncharov coordinates for $SL(N,\mathbb{C})$, $N\ge3$, involve non-generic configurations; the symplectic gluing rules lack a proof of $Sp(2M,\mathbb{Z})$-covariance.

## 6. The Gap

Proven: for a *fixed 1-efficient ideal triangulation* of a *cusped hyperbolic* $M$, combinatorial objects ($\mathcal{I}_M$, Andersen–Kashaev state integral) are well defined, and in verified cases they agree with the gauge-theoretic quantities and with $\mathrm{Vol}(M)$.

Claimed: a *functor* $M\mapsto T[M;\mathfrak{g}]$ from a bordism-like category of 3-manifolds to a category of 3d $\mathcal{N}=2$ theories (modulo infrared equivalence), for all $M$ and all $\mathfrak{g}$, whose invariants reconstruct *all* of $\mathcal{X}(M)$.

The gap is precisely: (i) an axiomatic target category — infrared equivalence of 3d $\mathcal{N}=2$ theories is itself undefined mathematically; (ii) capturing flat connections invisible to triangulations, so that the assignment is genuinely triangulation-independent; (iii) extending from cusped to closed $M$.

## 7. Current Research (as of June 2026)

- **$\hat{Z}$ program.** Extension of $\hat{Z}_a(q)$ beyond negative-definite plumbings — Dehn surgery formulas from $F_K(x,q)$, higher-rank $\hat{Z}$, and the conjectural quantum-modularity of $\hat{Z}$ (Caltech: Gukov, Park; Bonn/MPIM: Zagier-adjacent circle). *(frontier — verify)*
- **Resurgence and Stokes data.** Garoufalidis–Gu–Mariño's work on resurgence of the Kashaev invariant and matrices of state integrals; conjectural identification of Stokes constants with counts of BPS states / $\hat{Z}$ coefficients.
- **Rigorous Teichmüller TQFT.** Andersen–Kashaev's volume conjecture proven for further knot families; Andersen–Malusà on the AJ/quantization side.
- **Higher rank and Fock–Goncharov.** $SL(N)$ 3d-3d dictionaries and cluster-algebraic mapping class group representations (Kyoto: Yamazaki; Seoul/KIAS: Gang).
- **Closed manifolds.** Gang–Yamazaki and collaborators propose rank-0 $\mathcal{N}=4$ theories $T[M]$ for closed hyperbolic $M$ whose topologically twisted indices reproduce log-CFT / non-semisimple TQFT invariants. *(frontier — verify)*

## 8. Future Work

- Axiomatize the target: define a category whose objects are "3d $\mathcal{N}=2$ theories up to IR duality" via, e.g., their Coulomb-branch algebras or their category of line operators — then state 3d-3d as a genuine functor.
- Prove triangulation-independence of $\mathcal{I}_M$ and of the state integral for all 1-efficient triangulations of all cusped $M$ (partially done; the general statement is open).
- Build the abelian/reducible sector into the construction, so that $\hat{Z}_a$ and $Z_{S^3_b}$ decompose over *all* components of $\mathcal{X}(M)$.
- Prove convergence and asymptotic expansion of state integrals via resurgent analysis, converting the volume conjecture into a theorem for infinite families.
- Develop the $SL(N)$ and exceptional-$\mathfrak{g}$ dictionaries with proofs of symplectic covariance.

## 9. Key References

- **[Foundational]** T. Dimofte, D. Gaiotto, S. Gukov. *Gauge Theories Labelled by Three-Manifolds.* Communications in Mathematical Physics 325 (2014) 367–419. [DOI](https://doi.org/10.1007/s00220-013-1863-2)
- **[Foundational]** T. Dimofte, D. Gaiotto, S. Gukov. *3-Manifolds and 3d Indices.* Advances in Theoretical and Mathematical Physics 17 (2013) 975–1076. [DOI](https://doi.org/10.4310/atmp.2013.v17.n5.a3)
- **[Foundational]** Y. Terashima, M. Yamazaki. *SL(2,R) Chern–Simons, Liouville, and Gauge Theory on Duality Walls.* JHEP 08 (2011) 135.
- **[Foundational]** D. Cooper, M. Culler, H. Gillet, D. Long, P. Shalen. *Plane curves associated to character varieties of 3-manifolds.* Inventiones Mathematicae 118 (1994) 47–84. [DOI](https://doi.org/10.1007/bf01231526)
- **[Foundational]** J. E. Andersen, R. Kashaev. *A TQFT from Quantum Teichmüller Theory.* Communications in Mathematical Physics 330 (2014) 887–934. [DOI](https://doi.org/10.1007/s00220-014-2073-2)
- **[SOTA / Recent]** S. Gukov, P. Putrov, C. Vafa. *Fivebranes and 3-manifold homology.* JHEP 07 (2017) 071. [DOI](https://doi.org/10.1007/jhep07(2017)071)
- **[SOTA / Recent]** S. Gukov, D. Pei, P. Putrov, C. Vafa. *BPS spectra and 3-manifold invariants.* Journal of Knot Theory and Its Ramifications 29 (2020) 2040003. [DOI](https://doi.org/10.1142/s0218216520400039)
- **[SOTA / Recent]** S. Gukov, C. Manolescu. *A two-variable series for knot complements.* Quantum Topology 12 (2021) 1–109. [DOI](https://doi.org/10.4171/qt/145)
- **[SOTA / Recent]** C. Córdova, D. Jafferis. *Complex Chern–Simons from M5-branes on the Squashed Three-Sphere.* JHEP 11 (2017) 119. [DOI](https://doi.org/10.1007/jhep11(2017)119)
- **[SOTA / Recent]** S. Garoufalidis, C. Hodgson, H. Rubinstein, H. Segerman. *1-efficient triangulations and the index of a cusped hyperbolic 3-manifold.* Geometry & Topology 19 (2015) 2619–2689. [DOI](https://doi.org/10.2140/gt.2015.19.2619)
- **[SOTA / Recent]** S. Garoufalidis, J. Gu, M. Mariño. *The resurgent structure of quantum knot invariants.* Communications in Mathematical Physics 386 (2021) 469–493. [DOI](https://doi.org/10.1007/s00220-021-04076-0)
- **[Survey]** T. Dimofte. *Perturbative and nonperturbative aspects of complex Chern–Simons theory.* Journal of Physics A 50 (2017) 443009. [DOI](https://doi.org/10.1088/1751-8121/aa6a5b)
- **[Survey]** S. Gukov, M. Mariño, P. Putrov. *Resurgence in complex Chern–Simons theory.* arXiv (2016).

## 10. Worked Example: the figure-eight knot complement $M=S^3\setminus 4_1$

**Topology.** $M$ has an ideal triangulation with $N=2$ tetrahedra, shapes $z,w$, and two edge equations that reduce to the single relation
$$z(1-z)\,w(1-w)=1 .$$
Setting $z=w$ gives $z^2-z+1=0$, so $z=e^{i\pi/3}$ — the complete hyperbolic structure. Then
$$\mathrm{Vol}(M)=2D(e^{i\pi/3})=2\times 1.0149416064\ldots=2.0298832128\ldots,$$
matching SnapPy's value for $4_1$. The A-polynomial is
$$A_{4_1}(\ell,m)=-\ell^{-1}+m^{4}+\ell\,(\,\cdots)\ \Longleftrightarrow\ \ell+\ell^{-1}=m^{4}-m^{2}-2-m^{-2}+m^{-4}.$$

**Gauge theory.** The DGG recipe gives $T[4_1]$ = two chiral multiplets of charges $+1,-1$ under a $U(1)$ gauge symmetry, with vanishing effective CS level, one flavor $U(1)_m$ (the meridian), and a superpotential enforcing the internal edge. Its Coulomb/Higgs branch equations reproduce exactly $A_{4_1}(\ell,m)=0$: the vacuum equation of the $U(1)$ theory with FI-type parameter $m$ is the classical limit of the $\hat A$-operator annihilating the colored Jones polynomials $J_n(4_1;q)$,
$$J_{n+1}+J_{n-1}=\big(q^{2n}+q^{-2n}-q^{n}-q^{-n}-\ldots\big)J_n .$$

**Partition function.** Localization gives, up to a prefactor,
$$Z_{S^3_b}\big[T[4_1]\big](\mu)=\int_{\mathcal{C}}dx\;\frac{\Phi_b\!\big(x+\tfrac{\mu}{2}\big)}{\Phi_b\!\big(-x+\tfrac{\mu}{2}\big)}\,e^{2\pi i x^2},$$
which is precisely the Andersen–Kashaev state integral for $4_1$. Saddle point as $b\to0$: the critical point of the exponent is $x_\ast$ with $e^{2\pi b x_\ast}\to z=e^{i\pi/3}$, and
$$\log Z \;\sim\; \frac{1}{2\pi b^{2}}\Big(2\,\mathrm{Li}_2(e^{-i\pi/3})\text{-terms}\Big)\;=\;\frac{1}{2\pi b^{2}}\big(\mathrm{Vol}(4_1)+i\,\mathrm{CS}\big),\qquad \mathrm{Vol}=2.02988\ldots$$
Numerically the integral evaluated at $b=1$ and $\mu=0$ agrees with the Kashaev invariant asymptotics to the digits tested. The 3d index of $T[4_1]$ likewise equals
$$\mathcal{I}_{4_1}(0,\zeta;q)=1-2q+ \ldots,$$
independent of which of the two 1-efficient triangulations of $4_1$ is used. This single example instantiates every clause of Section 1 — and equally illustrates the gap: the abelian flat connections of $\pi_1(4_1)$, i.e. the line $\ell=1$ of $A_{4_1}$, are invisible to this triangulation-based $T[M]$.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*