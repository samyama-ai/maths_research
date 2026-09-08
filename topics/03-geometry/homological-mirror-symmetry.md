---
id: 03-geometry/homological-mirror-symmetry
title: "Homological Mirror Symmetry"
topic: 03-geometry
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Homological Mirror Symmetry

> **Topic:** Algebraic & Differential Geometry · **ID:** `03-geometry/homological-mirror-symmetry` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Kontsevich's conjecture (ICM 1994): for a mirror pair of Calabi–Yau manifolds $(X, \check{X})$ there is an equivalence of triangulated categories

$$D^b\mathrm{Coh}(\check{X}) \;\simeq\; D^\pi \mathcal{F}(X,\omega),$$

where the left side is the bounded derived category of coherent sheaves on the complex manifold $\check{X}$ and the right side is the split-closed derived Fukaya category of the symplectic manifold $(X,\omega)$, built from Lagrangian submanifolds and pseudoholomorphic discs.

A complete solution requires, for a class of mirror pairs specified independently (by Batyrev–Borisov polytope duality, Greene–Plesser quotients, or the Gross–Siebert degeneration data):

1. a construction of the mirror $\check{X}$ from $(X,\omega)$ that is not case-by-case;
2. an $A_\infty$-quasi-equivalence, not merely an isomorphism of Hochschild invariants or of Euler characteristics;
3. compatibility with the enumerative statement — the equivalence must intertwine the Gauss–Manin connection on $\check{X}$'s periods with quantum cohomology of $X$, recovering genus-0 Gromov–Witten invariants.

The conjecture is open in general; it is a theorem in the large families listed in §4. Disproof would require a mirror pair (in the above sense) with non-equivalent categories — e.g. distinguishable Hochschild cohomology.

## 2. Mathematical Foundations

**Fukaya category.** For $(X,\omega)$ compact symplectic with $c_1(X)=0$, objects are closed Lagrangians $L\subset X$ with $[\omega]|_L=0$, equipped with a grading (lift of the phase $L \to \mathbb{R}$ under $\det^2_{\mathbb{C}}$), a spin structure, and a flat unitary local system. Morphism spaces are Floer cochains, over the Novikov field
$$\Lambda = \Big\{ \sum_{i\ge 0} a_i T^{\lambda_i} : a_i \in \mathbb{C},\ \lambda_i \in \mathbb{R},\ \lambda_i \to \infty \Big\},$$
with $CF^*(L_0,L_1) = \bigoplus_{p \in L_0 \pitchfork L_1} \Lambda \cdot p$. The $A_\infty$-structure maps
$$\mu^d : CF^*(L_{d-1},L_d)\otimes\cdots\otimes CF^*(L_0,L_1) \to CF^*(L_0,L_d)[2-d]$$
count rigid pseudoholomorphic discs $u:(D,\partial D)\to (X,\bigcup L_i)$ with $d+1$ boundary punctures, weighted by $T^{\omega(u)}$, and satisfy
$$\sum_{m,n} (-1)^{\dagger}\,\mu^{d-m+1}(x_d,\dots,\mu^m(x_{n+m},\dots,x_{n+1}),\dots,x_1)=0 .$$
Obstruction is governed by $\mu^0 \in CF^*(L,L)$; for unobstructed $L$ one has $\mu^1\circ\mu^1=0$ and $HF^*(L,L)\cong H^*(L;\Lambda)$ when $L$ is "wide". Fukaya–Oh–Ohta–Ono construct the curved $A_\infty$-structure via Kuranishi structures and virtual perturbation.

**Derived side.** $D^b\mathrm{Coh}(\check X)$ is enhanced to the dg category of perfect complexes; by Bondal–Kapranov/Lunts–Orlov the dg enhancement is unique for smooth projective $\check X$.

**Invariants that must match.** Hochschild cohomology
$$HH^*(D^b\mathrm{Coh}\,\check X) \cong \bigoplus_{p+q=*} H^q(\check X,\Lambda^p T_{\check X}),\qquad HH^*(\mathcal{F}(X)) \cong QH^*(X;\Lambda)\ \text{(conjecturally, via the closed–open map)}.$$
Hodge-number mirror symmetry $h^{p,q}(X)=h^{n-p,q}(\check X)$ is a corollary.

**Fano / Landau–Ginzburg version.** For $X$ Fano the mirror is a pair $(\check X, W)$, $W:\check X\to\mathbb{C}$, and the conjecture reads $D^b\mathrm{Coh}(X)\simeq D^b\mathrm{Sing}(W^{-1}(0))=\mathrm{MF}(\check X,W)$ (matrix factorisations: $\mathbb{Z}/2$-graded pairs $(P_0\xrightarrow{d_0}P_1\xrightarrow{d_1}P_0)$ with $d_1d_0=W\cdot\mathrm{id}$), and dually $\mathcal{F}(\check X,W)\simeq D^b\mathrm{Coh}(X)$ using Lefschetz thimbles.

**Open version.** For $X$ noncompact/Weinstein one uses the wrapped Fukaya category $\mathcal{W}(X)$, with $CW^*(L_0,L_1)=\varinjlim_{w} CF^*(\phi^w_H(L_0),L_1)$ for a quadratic Hamiltonian $H$.

**SYZ mechanism.** Strominger–Yau–Zaslow: near a large complex structure limit, $X$ admits a special Lagrangian $T^n$-fibration $f:X\to B$, and $\check X$ is the dual fibration $\check f:\check X \to B$, i.e. $\check X = \bigcup_{b} H^1(f^{-1}(b);\mathbb{R}/\mathbb{Z})$ corrected by disc instantons. HMS should then follow from a family Floer / real-analytic Fourier–Mukai transform.

## 3. History & State of the Art (SOTA)

- **1990–91.** Candelas–de la Ossa–Green–Parkes predict rational curve counts on the quintic threefold from periods of the mirror; Greene–Plesser construct the mirror as an orbifold quotient of a Fermat pencil.
- **1994.** Kontsevich states HMS at the ICM in Zürich, replacing the enumerative statement with a categorical one.
- **1996.** Strominger–Yau–Zaslow propose the torus-fibration mechanism; Kontsevich–Soibelman later formalise it via non-archimedean analytic geometry and affine structures with singularities.
- **1998.** Polishchuk–Zaslow prove HMS for the elliptic curve — the first complete case.
- **2000s.** Seidel develops Picard–Lefschetz theory for Fukaya categories (exceptional collections of thimbles); Abouzaid proves a generation criterion (2010) making "these Lagrangians split-generate" checkable.
- **2003–11.** Gross–Siebert build the toric-degeneration program, producing mirror pairs algebraically from tropical/affine data and removing the case-by-case input.
- **2010s.** Seidel (quartic K3), Sheridan (Calabi–Yau hypersurfaces in $\mathbb{P}^n$), Abouzaid–Smith (4-torus), and Ganatra–Pardon–Shende (sectorial descent for wrapped categories) turn HMS from a family of examples into a structural theory.

## 4. Partial Results / Verified Cases

| Case | Result | Reference |
|---|---|---|
| Elliptic curve $E_\tau$, all $\tau$ | Full equivalence | Polishchuk–Zaslow 1998 |
| Abelian varieties, generic complexified symplectic form | Equivalence for the 4-torus; large classes of abelian varieties | Abouzaid–Smith 2010; Fukaya (family Floer) |
| Quartic K3 surface $\{z_0^4+\cdots+z_3^4=0\}\subset\mathbb{P}^3$ | $D^\pi\mathcal{F}(X)\simeq D^b\mathrm{Coh}(\check X)$ | Seidel, *Memoirs AMS* 2015 |
| Smooth CY hypersurface $X_n\subset\mathbb{P}^{n+1}$, all $n\ge 2$ (includes the quintic 3-fold) | $D^\pi\mathcal{F}(X_n)$ embeds in / is equivalent to $D^b\mathrm{Coh}$ of the Greene–Plesser mirror | Sheridan, *Invent. Math.* 2015 |
| Generalized Greene–Plesser mirrors (Calabi–Yau hypersurfaces in toric orbifolds, generic Kähler parameter) | HMS proved | Sheridan–Smith, *Invent. Math.* 2021 |
| Curves of genus $g\ge 2$ | HMS for the mirror LG model | Efimov, *Adv. Math.* 2012; Seidel (genus 2) 2011 |
| Punctured spheres, pair-of-pants, punctured Riemann surfaces | Wrapped HMS, both directions | Abouzaid–Auroux–Efimov–Katzarkov–Orlov, *JAMS* 2013; H. Lee 2016 |
| Toric varieties, del Pezzo surfaces, weighted projective planes | LG mirror symmetry | Abouzaid 2009; Auroux–Katzarkov–Orlov 2006, 2008; Fang–Liu–Treumann–Zaslow 2011 |
| Cotangent bundles $T^*M$ | $\mathcal{W}(T^*M)\simeq$ chains on $\Omega M$; $\mathcal{F}(T^*M)\simeq$ constructible sheaves | Abbondandolo–Schwarz; Nadler–Zaslow, *JAMS* 2009; Abouzaid 2012 |
| Cluster varieties, log CY surfaces | Mirror algebra from scattering diagrams; HMS in many cases | Gross–Hacking–Keel 2015; Gross–Hacking–Keel–Kontsevich 2018 |

## 5. Principal Obstacles

- **Foundations of the Fukaya category.** Transversality for multiply-covered discs fails; one needs virtual perturbation (Kuranishi structures, polyfolds, or Pardon's implicit atlases). Comparing constructions across schools is still laborious, so "the" Fukaya category is not a single black box.
- **Generation.** Even with Abouzaid's criterion, exhibiting a finite set of Lagrangians that split-generates a *compact* Fukaya category requires deep geometric input (Seidel's quartic argument uses a specific degeneration and a large computation).
- **Computability of $\mu^d$.** Structure constants are Novikov power series counting discs; convergence and closed-form evaluation are only available in near-toric or torus-fibered settings.
- **Instanton corrections in SYZ.** Special Lagrangian fibrations have singular fibers; the discriminant locus has codimension 2 with wall-crossing, and the naive dual fibration must be corrected by disc counts. Constructing the corrected mirror analytically (rather than tropically) is unsolved in dimension $\ge 3$.
- **Failure of standard toolkits.** Sheaf-theoretic methods (Fourier–Mukai kernels) require an algebraic correspondence; the symplectic side has none. Classical algebraic topology sees only $K$-theory/Hodge numbers and cannot detect $A_\infty$-structure. Perturbative/deformation arguments compare formal neighbourhoods of the large-volume limit but do not extend over the whole Kähler moduli space, where $\Pi_1$ monodromy acts by autoequivalences.

## 6. The Gap

Proved: HMS for specific families where (i) the mirror is given by an explicit combinatorial recipe, and (ii) an explicit generating collection of Lagrangians exists (Fermat-type hypersurfaces, abelian varieties, curves, toric and Weinstein settings).

Missing: a *construction*, not a verification. One wants a functor
$$\Phi:\mathcal{F}(X,\omega)\longrightarrow D^b\mathrm{Coh}(\check X),\qquad \check X:=\text{family Floer / Gross–Siebert mirror of }(X,\omega),$$
defined for every Calabi–Yau $X$ with a suitable degeneration, together with a proof that $\Phi$ is an equivalence by a general argument (deformation to the normal cone of the large-volume limit, plus a formality/rigidity statement). The concrete step is: prove that the family Floer mirror of Fukaya (rigid analytic, no corrections proved to converge in general) coincides with the Gross–Siebert mirror, and that Lagrangian sections generate. Also missing: HMS for non-generic Kähler parameters (Sheridan–Smith need genericity), and for singular / non-simply-connected degenerations.

## 7. Current Research (as of June 2026)

- **Sectorial / descent methods.** Ganatra–Pardon–Shende's sectorial covers reduce wrapped HMS to local models; ongoing work extends descent to *compact* Fukaya categories via Lagrangian skeleta. Groups: Stanford, Berkeley/IMJ (Shende, Nadler).
- **Gross–Siebert intrinsic mirror symmetry.** Mirror algebras from punctured log Gromov–Witten invariants; the current program aims to lift the ring isomorphism to a categorical equivalence *(frontier — verify)*.
- **Family Floer.** Abouzaid's rigid-analytic mirror functor is being pushed past the torus-fibration-without-singularities case; the singular-fiber wall-crossing is the live obstruction.
- **Homological mirror symmetry for symplectic manifolds without CY structure**: monotone/Fano settings, quantum cohomology and Bogomolov–Tian–Todorov-type unobstructedness (Sheridan; Ganatra–Perutz–Sheridan on the categorical enumerative invariants program, which derives Gromov–Witten invariants from a Calabi–Yau $A_\infty$-category).
- **Institutions.** IHES, Columbia (Abouzaid), Cambridge/Edinburgh (Smith, Sheridan), Stanford, Miami (Katzarkov), IBS-CGP Pohang, Kavli IPMU.

## 8. Future Work

- Prove *homological mirror symmetry implies enumerative mirror symmetry* in full generality — Ganatra–Perutz–Sheridan reduce this to showing the Fukaya category is a smooth Calabi–Yau $A_\infty$-category with a specified "$n$-dimensional" splitting of the Hodge filtration.
- Establish convergence of Novikov-series structure constants (Kontsevich–Soibelman's analytic HMS), moving from $\Lambda$ to $\mathbb{C}$ and making periods honest functions.
- Extend HMS to singular / non-commutative spaces: Landau–Ginzburg models with non-isolated singularities, Fano threefolds, and the Katzarkov–Kontsevich–Pantev framework of noncommutative Hodge structures for birational invariants.
- Use HMS to prove symplectic rigidity statements (nonexistence of Lagrangian tori, Nadler-type results), i.e. run the arrow backwards.

## 9. Key References

- **[Foundational]** M. Kontsevich. *Homological Algebra of Mirror Symmetry.* Proceedings of the International Congress of Mathematicians (Zürich, 1994), Birkhäuser, 1995, 120–139. [DOI](https://doi.org/10.1007/978-3-0348-9078-6_11)
- **[Foundational]** A. Strominger, S.-T. Yau, E. Zaslow. *Mirror Symmetry is T-Duality.* Nuclear Physics B 479 (1996), 243–259.
- **[Foundational]** A. Polishchuk, E. Zaslow. *Categorical Mirror Symmetry: the Elliptic Curve.* Advances in Theoretical and Mathematical Physics 2 (1998), 443–470. [DOI](https://doi.org/10.4310/atmp.1998.v2.n2.a9)
- **[Foundational]** K. Fukaya, Y.-G. Oh, H. Ohta, K. Ono. *Lagrangian Intersection Floer Theory: Anomaly and Obstruction, I & II.* AMS/IP Studies in Advanced Mathematics 46, 2009.
- **[Foundational]** P. Seidel. *Fukaya Categories and Picard–Lefschetz Theory.* Zurich Lectures in Advanced Mathematics, EMS, 2008. [DOI](https://doi.org/10.4171/063)
- **[SOTA]** P. Seidel. *Homological Mirror Symmetry for the Quartic Surface.* Memoirs of the American Mathematical Society 236 (1116), 2015. [DOI](https://doi.org/10.1090/memo/1116)
- **[SOTA]** N. Sheridan. *Homological Mirror Symmetry for Calabi–Yau Hypersurfaces in Projective Space.* Inventiones Mathematicae 199 (2015), 1–186. [DOI](https://doi.org/10.1007/s00222-014-0507-2)
- **[SOTA]** N. Sheridan, I. Smith. *Homological Mirror Symmetry for Generalized Greene–Plesser Mirrors.* Inventiones Mathematicae 224 (2021), 627–682. [DOI](https://doi.org/10.1007/s00222-020-01018-w)
- **[SOTA]** M. Abouzaid, I. Smith. *Homological Mirror Symmetry for the 4-Torus.* Duke Mathematical Journal 152 (2010), 373–440. [DOI](https://doi.org/10.1215/00127094-2010-015)
- **[SOTA]** M. Abouzaid, D. Auroux, A. Efimov, L. Katzarkov, D. Orlov. *Homological Mirror Symmetry for Punctured Spheres.* Journal of the AMS 26 (2013), 1051–1083. [DOI](https://doi.org/10.1090/s0894-0347-2013-00770-5)
- **[SOTA]** S. Ganatra, J. Pardon, V. Shende. *Sectorial Descent for Wrapped Fukaya Categories.* Journal of the AMS 37 (2024), 499–635. [DOI](https://doi.org/10.1090/jams/1035)
- **[SOTA]** M. Abouzaid. *A Geometric Criterion for Generating the Fukaya Category.* Publications Mathématiques de l'IHÉS 112 (2010), 191–240. [DOI](https://doi.org/10.1007/s10240-010-0028-5)
- **[SOTA]** M. Gross, B. Siebert. *From Real Affine Geometry to Complex Geometry.* Annals of Mathematics 174 (2011), 1301–1428. [DOI](https://doi.org/10.4007/annals.2011.174.3.1)
- **[Survey]** K. Hori, S. Katz, A. Klemm, R. Pandharipande, R. Thomas, C. Vafa, R. Vakil, E. Zaslow. *Mirror Symmetry.* Clay Mathematics Monographs 1, AMS, 2003.
- **[Survey]** D. Auroux. *A Beginner's Introduction to Fukaya Categories.* In: Contact and Symplectic Topology, Bolyai Society Mathematical Studies 26, Springer, 2014, 85–136. [DOI](https://doi.org/10.1007/978-3-319-02036-5_3)
- **[Survey]** M. Gross. *Tropical Geometry and Mirror Symmetry.* CBMS Regional Conference Series in Mathematics 114, AMS, 2011. [DOI](https://doi.org/10.1090/cbms/114)

## 10. Worked Example / Concrete Special Case

**HMS for the elliptic curve (Polishchuk–Zaslow).**

Symplectic side: $X = T^2 = \mathbb{R}^2/\mathbb{Z}^2$ with area form $\omega$ of total area $A$, complexified by a $B$-field: $q = e^{2\pi i(B+iA)}$. Mirror complex side: $\check X = E_\tau = \mathbb{C}^*/q^{\mathbb{Z}}$ with $\tau = B + iA$.

Lagrangians are straight lines. Take
$$L_0 = \{y=0\},\qquad L_1=\{y=x\},\qquad L_2=\{y=2x\}$$
of slopes $0,1,2$, each with trivial local system. Intersections:
$$\\#(L_0\cap L_1)=1,\quad \\#(L_1\cap L_2)=1,\quad \\#(L_0\cap L_2)=|2-0|=2 .$$
So $HF^0(L_0,L_1)=\Lambda\langle a\rangle$, $HF^0(L_1,L_2)=\Lambda\langle b\rangle$, $HF^0(L_0,L_2)=\Lambda\langle c_0,c_1\rangle$.

The product $\mu^2(b,a)=\sum_{k} n_k\, c_k$ counts holomorphic triangles in $T^2$ with vertices at $a,b,c_k$ and sides on $L_0,L_1,L_2$. Lifting to the universal cover $\mathbb{R}^2$, triangles are honest affine triangles; those with vertex $c_k$ form a family indexed by $\mathbb{Z}$, with areas an arithmetic-progression-of-squares. Weighting by $T^{\mathrm{area}}$ (equivalently by $q$) gives
$$\mu^2(b,a) \;=\; \sum_{k=0}^{1}\Big(\sum_{n\in\mathbb{Z}} q^{\frac{1}{2}\left(n+\frac{k}{2}\right)^2\cdot 2}\Big) c_k \;=\; \sum_{k=0}^{1}\theta\!\begin{bmatrix} k/2 \\ 0\end{bmatrix}\!(0,2\tau)\, c_k,$$
i.e. the structure constants are theta functions with characteristics.

Mirror side: under the correspondence $L_{\text{slope }m} \leftrightarrow$ a degree-$m$ line bundle (with $L_0 \mapsto \mathcal{O}_{E}$, $L_1\mapsto \mathcal{L}$, $L_2\mapsto \mathcal{L}^{\otimes 2}$), Floer cohomology matches sheaf cohomology:
$$\dim H^0(E,\mathcal{L}^{\otimes d}) = d = \\#(L_0\cap L_d),$$
and the composition $H^0(\mathcal{L})\otimes H^0(\mathcal{L})\to H^0(\mathcal{L}^{\otimes 2})$ is exactly multiplication of theta functions, governed by the classical addition formula
$$\theta(z_1,\tau)\,\theta(z_2,\tau)=\sum_{k=0}^{1}\theta\!\begin{bmatrix}k/2\\0\end{bmatrix}\!(z_1+z_2,2\tau)\;\theta\!\begin{bmatrix}k/2\\0\end{bmatrix}\!(z_1-z_2,2\tau).$$
The disc-count identity and the theta identity agree term by term. Vertical lines $\{x=c\}$ (with local systems) correspond to skyscraper sheaves $\mathcal{O}_p$, and line bundles plus skyscrapers split-generate both sides — giving the full equivalence $D^\pi\mathcal{F}(T^2,\omega)\simeq D^b\mathrm{Coh}(E_\tau)$.

This example shows the general shape and the general difficulty: the equivalence is a statement that *disc counts equal structure constants of an algebraic multiplication*. In dimension 1 the discs are triangles and the counts are theta series; in dimension 3 they are unknown transcendental series, which is precisely the gap of §6.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*