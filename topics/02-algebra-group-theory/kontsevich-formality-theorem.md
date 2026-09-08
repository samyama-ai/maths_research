---
id: 02-algebra-group-theory/kontsevich-formality-theorem
title: "Kontsevich Formality Theorem"
topic: 02-algebra-group-theory
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Kontsevich Formality Theorem

> **Topic:** Algebra & Group Theory · **ID:** `02-algebra-group-theory/kontsevich-formality-theorem` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

Let $M$ be a smooth manifold, $A = C^\infty(M)$. Two differential graded Lie algebras (DGLAs) are attached to $A$:

- $T_{\mathrm{poly}}(M) = \Gamma(M, \Lambda^{\bullet+1} TM)$, polyvector fields with the Schouten–Nijenhuis bracket and zero differential;
- $D_{\mathrm{poly}}(M) \subset C^{\bullet+1}(A,A)$, the multidifferential Hochschild cochains with the Gerstenhaber bracket and Hochschild differential.

**Formality theorem (Kontsevich, 1997).** There is an $L_\infty$-quasi-isomorphism
$$\mathcal{U} : T_{\mathrm{poly}}(M) \longrightarrow D_{\mathrm{poly}}(M),\qquad \mathcal{U}_1 = \text{Hochschild–Kostant–Rosenberg map},$$
i.e. a collection of graded-antisymmetric maps $\mathcal{U}_n : \Lambda^n T_{\mathrm{poly}} \to D_{\mathrm{poly}}[1-n]$ satisfying the $L_\infty$-relations, whose first component induces the HKR isomorphism on cohomology. Hence $D_{\mathrm{poly}}(M)$ is *formal*: quasi-isomorphic to its own cohomology as an $L_\infty$-algebra.

**Corollary (deformation quantization).** Poisson structures on $M$ modulo formal diffeomorphism are in bijection with star products on $C^\infty(M)[[\hbar]]$ modulo gauge equivalence.

A complete proof requires: (i) construction of all $\mathcal{U}_n$, (ii) verification of the infinite family of $L_\infty$ relations, (iii) globalization from $\mathbb{R}^d$ to arbitrary $M$. All three were achieved. What remains open are the *refinements*: the cyclic/Tsygan formality in full generality, the classification of the homotopy classes of formality morphisms, and the arithmetic nature of Kontsevich's integral weights.

## 2. Mathematical Foundations

**Schouten bracket.** On $T_{\mathrm{poly}}$, for decomposables,
$$[\xi_0\wedge\cdots\wedge\xi_k,\ \eta_0\wedge\cdots\wedge\eta_l] = \sum_{i,j}(-1)^{i+j}[\xi_i,\eta_j]\wedge \xi_0\wedge\cdots\widehat{\xi_i}\cdots\wedge\eta_0\cdots\widehat{\eta_j}\cdots .$$
A bivector $\pi$ is Poisson iff $[\pi,\pi]=0$.

**Gerstenhaber bracket.** For $\Phi\in C^{k+1}$, $\Psi\in C^{l+1}$, $\Phi\circ\Psi=\sum_i(-1)^{il}\Phi(a_1,\dots,\Psi(a_{i+1},\dots),\dots)$ and $[\Phi,\Psi]=\Phi\circ\Psi-(-1)^{kl}\Psi\circ\Phi$; $d_H = [\mu,-]$ with $\mu$ the product. Star products $\star = \mu + \sum_{n\ge1}\hbar^n B_n$ correspond to $\Pi=\sum\hbar^nB_n$ with $d_H\Pi + \tfrac12[\Pi,\Pi]=0$.

**$L_\infty$-morphism.** Maps $\mathcal{U}_n:\Lambda^n\mathfrak{g}\to\mathfrak{h}[1-n]$ with
$$d\,\mathcal{U}_n(\xi_1,\dots,\xi_n) + \tfrac12\!\!\sum_{I\sqcup J=\{1..n\}}\!\!\pm[\mathcal{U}_{|I|}(\xi_I),\mathcal{U}_{|J|}(\xi_J)] = \sum_{i<j}\pm\,\mathcal{U}_{n-1}([\xi_i,\xi_j],\xi_1,\dots,\widehat{\xi_i},\dots,\widehat{\xi_j},\dots).$$
Such a morphism maps Maurer–Cartan elements to Maurer–Cartan elements: $\Pi = \sum_{n\ge1}\frac{\hbar^n}{n!}\mathcal{U}_n(\pi,\dots,\pi)$.

**Kontsevich's construction on $\mathbb{R}^d$.** Let $\mathrm{Conf}_{n,m}$ be configurations of $n$ points in the open upper half-plane $\mathcal{H}$ and $m$ ordered points on $\mathbb{R}$, modulo $z\mapsto az+b$; $C_{n,m}$ its Fulton–MacPherson compactification, $\dim = 2n+m-2$. The hyperbolic angle
$$\phi^h(p,q) = \arg\frac{q-p}{q-\bar p}$$
gives, for each admissible graph $\Gamma$ (a labelled directed graph on $n$ aerial and $m$ ground vertices, each aerial vertex of out-degree $2$, no loops or double edges), the weight
$$w_\Gamma = \frac{1}{(2\pi)^{2n}}\int_{C_{n,m}^+}\bigwedge_{e\in E(\Gamma)} d\phi^h_e .$$
Then
$$\mathcal{U}_n(\pi_1,\dots,\pi_n) = \sum_{\Gamma\in G_{n,m}} w_\Gamma\, B_{\Gamma}(\pi_1,\dots,\pi_n),$$
$B_\Gamma$ being the multidifferential operator obtained by contracting tensor indices along edges. The $L_\infty$ relations follow from Stokes' theorem on $C_{n,m}$: $\int_{\partial C}\omega=0$, with boundary strata reproducing exactly the terms of the relation.

## 3. History & State of the Art (SOTA)

- **1978.** Bayen–Flato–Fronsdal–Lichnerowicz–Sternheimer pose deformation quantization and the existence question for star products.
- **1983.** De Wilde–Lecomte prove existence on symplectic manifolds; **1994** Fedosov gives a geometric construction and classification by $\frac{[\omega]}{\hbar}+H^2_{dR}(M)[[\hbar]]$.
- **1997.** Kontsevich, *Deformation quantization of Poisson manifolds* (arXiv:q-alg/9709040) proves the local formality theorem via the graph/weight expansion, and sketches globalization; published in Lett. Math. Phys. **66** (2003).
- **1998.** Tamarkin gives a second, operadic proof: formality of the little discs operad $\Rightarrow$ Deligne conjecture $\Rightarrow$ formality, at the price of a choice of Drinfeld associator.
- **1999–2000.** Cattaneo–Felder derive the star product as the perturbative expansion of the Poisson sigma model path integral, explaining the weights as Feynman amplitudes.
- **2002.** Cattaneo–Felder–Tomassini give a clean globalization (formal geometry / Gelfand–Fuks); Dolgushev (2005) proves covariant and equivariant versions using Fedosov resolutions, valid for any smooth manifold with a torsion-free connection.
- **2003–2005.** Shoikhet proves Tsygan's formality for Hochschild *chains* on $\mathbb{R}^d$; Dolgushev globalizes it.
- **2015.** Willwacher identifies $H^0$ of Kontsevich's graph complex with the Grothendieck–Teichmüller Lie algebra $\mathfrak{grt}_1$, giving a transitive $\mathfrak{grt}_1$-action on the homotopy classes of formality morphisms.
- **2020.** Banks–Panzer–Pym prove all Kontsevich weights are $\mathbb{Q}$-linear combinations of multiple zeta values, and give an algorithm computing them.

## 4. Partial Results / Verified Cases

- **Symplectic $M$ ($\pi$ nondegenerate, $\dim M = 2n$):** existence (De Wilde–Lecomte 1983) and full classification (Fedosov 1994, Nest–Tsygan 1995) predate Kontsevich; equivalence classes $\leftrightarrow \frac{[\omega]}{\hbar}+ \hbar H^2_{\mathrm{dR}}(M)[[\hbar]]$.
- **$M=\mathbb{R}^d$ with any Poisson $\pi$:** Kontsevich 1997, explicit graph formula; weights computable to all orders (Banks–Panzer–Pym 2020 compute through order 7 in practice).
- **Linear Poisson structures $\pi = \frac12 f^{ij}_k x^k\partial_i\wedge\partial_j$ on $\mathfrak{g}^*$:** the star product is gauge-equivalent to the Gutt product on $U(\mathfrak{g})$; the induced isomorphism $S(\mathfrak{g})^{\mathfrak{g}}\cong Z(U(\mathfrak{g}))$ recovers the **Duflo isomorphism** (Kontsevich §8; Alekseev–Torossian 2012 relates the underlying identities to the Kashiwara–Vergne conjecture and Drinfeld associators).
- **General smooth $M$, any $\pi$:** globalized formality (CFT 2002; Dolgushev 2005), including $G$-equivariant versions for compact $G$.
- **Chains / Tsygan formality:** proved for $\mathbb{R}^d$ (Shoikhet 2003) and for arbitrary smooth $M$ (Dolgushev 2005/2006).
- **Algebraic/holomorphic settings:** formality for smooth affine varieties over a field of characteristic $0$ (Kontsevich, *Operads and motives*, 1999; Yekutieli for schemes over $\mathbb{Q}$); complex-analytic version via Kontsevich's "deformation quantization of algebraic varieties".
- **Rationality:** all weights lie in the $\mathbb{Q}$-algebra of MZVs (2020); Felder–Willwacher (2010) show individual weights of certain graphs are *not* forced to be rational by the axioms alone, while the full star product can be chosen with MZV coefficients.

## 5. Principal Obstacles

The theorem itself is proved; the obstacles concern its refinements and the transparency of the proof.

- **The weights are transcendental integrals.** $w_\Gamma$ is a period of a configuration-space integral; no closed formula exists. Establishing rationality of individual weights (e.g. the conjecture $w_\Gamma\in\mathbb{Q}$ for the "wheel" graphs beyond low order) resists because the integrals are only expressible after blow-up and iterated-integral regularization; the MZV result gives $\zeta(3),\zeta(5),\dots$ in general.
- **Cyclic formality.** For a *cyclic* (unimodular / with volume form) refinement one needs a quasi-isomorphism compatible with Connes' $B$-operator; Kontsevich's graph integrals do not obviously respect the cyclic structure, and Stokes-theorem cancellations fail on the boundary strata where aerial points collide with the whole real line. Shoikhet's cyclic formality conjecture was proved only in the $\mathbb{R}^d$/unimodular setting; the general statement remains partly open *(frontier — verify)*.
- **Non-smooth and characteristic $p$.** Both proofs use $\mathbb{Q}\subset k$ (operads, $L_\infty$, associators, $1/n!$) and smoothness (HKR). For singular schemes, $\mathrm{Ext}^\bullet_{X\times X}(\mathcal{O},\mathcal{O})$ is not polyvector fields, and formality fails; in characteristic $p$ HKR itself fails beyond degree $<p$.
- **Uniqueness.** Kontsevich's and Tamarkin's morphisms are not known to be homotopic in general; the $\mathfrak{grt}_1$-action is transitive on homotopy classes (Willwacher), but the stabilizer / faithfulness questions reduce to the still-open structure of $\mathfrak{grt}_1$ (Deligne–Drinfeld conjecture that $\mathfrak{grt}_1$ is free on $\sigma_3,\sigma_5,\dots$).

## 6. The Gap

Proven: existence of $\mathcal{U}$ over $\mathbb{R}$ (and $\mathbb{Q}$-algebras with associators), globally, with chain-level analogue, and MZV weights. Not proven:

1. **Arithmetic gap.** Are all $w_\Gamma$ rational, or does $\zeta(3)$ genuinely appear in *every* formality morphism? The MZV theorem bounds the field; it does not decide minimality.
2. **Homotopy-classification gap.** Classify $\pi_0$ of the space of formality morphisms as a $\mathrm{GRT}_1$-torsor — known to be a torsor; identifying a canonical base point requires resolving $\mathfrak{grt}_1$.
3. **Cyclic gap.** A globally defined cyclic/unimodular formality on an arbitrary Poisson manifold with volume form, compatible with the divergence operator.
4. **Beyond smooth/char 0.** Any formality statement for singular or positive-characteristic targets.

## 7. Current Research (as of June 2026)

- **Graph complexes and $\mathfrak{grt}$.** Willwacher (Zurich/ETH), Turchin, Fresse and collaborators continue the program linking $GC_2$, $\mathfrak{grt}_1$, and embedding-space homotopy; the Deligne–Drinfeld freeness conjecture remains the bottleneck.
- **Period computations.** Panzer, Pym and coauthors extend the algorithmic evaluation of Kontsevich weights and study which MZVs are unavoidable *(frontier — verify)*.
- **Shifted/derived formality.** Calaque, Pantev, Toën, Vezzosi, Vaquié's shifted Poisson geometry gives derived-stack analogues; formality statements there are proved case by case.
- **Quantization of Courant algebroids and higher structures.** Formality for $L_\infty$-algebroids and for the Deligne conjecture in higher operadic degrees.
- **Kashiwara–Vergne.** Following Alekseev–Torossian (Ann. of Math. 2012) and Alekseev–Enriquez–Torossian, links between formality, KV solutions, and associators are further tightened.

## 8. Future Work

- Determine whether a formality morphism with all-rational weights exists (a "$\mathbb{Q}$-formality" theorem); Kontsevich conjectured a motivic/Galois-theoretic explanation for the appearance of MZVs.
- Prove or disprove the freeness of $\mathfrak{grt}_1$, which would classify formality morphisms.
- Complete cyclic formality on general manifolds and derive Batalin–Vilkovisky-compatible quantizations.
- Extend to derived/shifted settings and to Poisson structures on stacks with singular support.
- Give a purely combinatorial (weight-free) proof of the local theorem to make it available over $\mathbb{Q}$ without associators.

## 9. Key References

- **[Foundational]** M. Kontsevich. *Deformation quantization of Poisson manifolds.* Letters in Mathematical Physics **66** (2003), 157–216. (arXiv:q-alg/9709040, 1997). [DOI](https://doi.org/10.1023/b:math.0000027508.00421.bf)
- **[Foundational]** F. Bayen, M. Flato, C. Fronsdal, A. Lichnerowicz, D. Sternheimer. *Deformation theory and quantization I, II.* Annals of Physics **111** (1978), 61–110, 111–151.
- **[Foundational]** B. Fedosov. *A simple geometrical construction of deformation quantization.* Journal of Differential Geometry **40** (1994), 213–238. [DOI](https://doi.org/10.4310/jdg/1214455536)
- **[Alternative proof]** D. Tamarkin. *Another proof of M. Kontsevich formality theorem.* arXiv:math/9803025 (1998); and *Formality of chain operad of little discs*, Lett. Math. Phys. **66** (2003), 65–72.
- **[Physics interpretation]** A. S. Cattaneo, G. Felder. *A path integral approach to the Kontsevich quantization formula.* Communications in Mathematical Physics **212** (2000), 591–611. [DOI](https://doi.org/10.1007/s002200000229)
- **[Globalization]** A. S. Cattaneo, G. Felder, L. Tomassini. *From local to global deformation quantization of Poisson manifolds.* Duke Mathematical Journal **115** (2002), 329–352. [DOI](https://doi.org/10.1215/s0012-7094-02-11524-5)
- **[Globalization / equivariance]** V. Dolgushev. *Covariant and equivariant formality theorems.* Advances in Mathematics **191** (2005), 147–177. [DOI](https://doi.org/10.1016/s0001-8708(04)00076-3)
- **[Chains]** B. Shoikhet. *A proof of the Tsygan formality conjecture for chains.* Advances in Mathematics **179** (2003), 7–37. [DOI](https://doi.org/10.1016/s0001-8708(02)00023-3)
- **[SOTA]** T. Willwacher. *M. Kontsevich's graph complex and the Grothendieck–Teichmüller Lie algebra.* Inventiones Mathematicae **200** (2015), 671–760. [DOI](https://doi.org/10.1007/s00222-014-0528-x)
- **[SOTA]** P. Banks, E. Panzer, B. Pym. *Multiple zeta values in deformation quantization.* Inventiones Mathematicae **222** (2020), 79–159. [DOI](https://doi.org/10.1007/s00222-020-00970-x)
- **[SOTA]** A. Alekseev, C. Torossian. *The Kashiwara–Vergne conjecture and Drinfeld's associators.* Annals of Mathematics **175** (2012), 415–463. [DOI](https://doi.org/10.4007/annals.2012.175.2.1)
- **[Survey]** S. Gutt. *Deformation quantisation of Poisson manifolds.* Geometry & Topology Monographs **17** (2011), 171–220.
- **[Survey]** A. Cattaneo, D. Indelicato. *Formality and star products.* In *Poisson Geometry, Deformation Quantisation and Group Representations*, LMS Lecture Note Series 323, CUP, 2005. [DOI](https://doi.org/10.1017/cbo9780511734878.008)

## 10. Worked Example / Concrete Special Case

**Order-2 expansion.** On $\mathbb{R}^d$ with Poisson bivector $\pi^{ij}$, summing the admissible graphs with $n\le2$ gives
$$f\star g = fg + \hbar\,\pi^{ij}\partial_if\,\partial_jg + \frac{\hbar^2}{2}\pi^{ij}\pi^{kl}\partial_i\partial_kf\,\partial_j\partial_lg + \frac{\hbar^2}{3}\pi^{ij}\big(\partial_j\pi^{kl}\big)\big(\partial_i\partial_kf\,\partial_lg-\partial_kf\,\partial_i\partial_lg\big)+O(\hbar^3).$$
The coefficient $1$ at order $\hbar$ is $2w_{\Gamma_1}$ where $\Gamma_1$ has a single aerial vertex with edges to both ground points; $C_{1,2}$ is a point after the $az+b$ quotient is used, and $w_{\Gamma_1}=\frac{1}{(2\pi)^2}\int_{C^+_{1,2}}d\phi^h_1\wedge d\phi^h_2 = \tfrac12$.

**Constant $\pi$.** If $\pi^{ij}$ is constant all $\partial\pi$ terms drop and the series resums to the Moyal product $f\star g = f\exp(\hbar\,\overleftarrow{\partial_i}\pi^{ij}\overrightarrow{\partial_j})g$.

**Linear case: $\mathfrak{aff}(1)$.** Take $M=\mathbb{R}^2$ with coordinates $(x,y)$ and $\pi = x\,\partial_x\wedge\partial_y$, i.e. $\pi^{xy}=-\pi^{yx}=x$. This is the linear Poisson structure on $\mathfrak{g}^*$ for $\mathfrak{g}=\mathfrak{aff}(1)$, $[X,Y]=X$. Apply the formula to $f=x$, $g=y$:

- order $0$: $xy$;
- order $1$: $\hbar\,\pi^{ij}\partial_i x\,\partial_j y = \hbar\,\pi^{xy} = \hbar x$;
- order $2$: every surviving term contains a second derivative $\partial_i\partial_k f$ or $\partial_i\partial_k g$, and $x,y$ are linear, so all vanish. The same holds at every higher order, since each aerial vertex beyond the first must send an edge into an already-differentiated argument.

Hence $x\star y = xy+\hbar x$, $y\star x = xy-\hbar x$, and
$$[x,y]_\star = x\star y - y\star x = 2\hbar\,x .$$
Setting $\hbar=\tfrac12$ recovers the defining relation $[X,Y]=X$ of $\mathfrak{aff}(1)$: the Kontsevich star product on $\mathfrak{g}^*$ reproduces the universal enveloping algebra $U(\mathfrak{g})$, with the symmetrization map $S(\mathfrak{g})\to U(\mathfrak{g})$ as the identification of underlying vector spaces. Restricting to invariants and correcting by the Duflo factor $\det\!\big(\frac{\sinh(\mathrm{ad}/2)}{\mathrm{ad}/2}\big)^{1/2}$ makes the map $S(\mathfrak{g})^{\mathfrak{g}}\to Z(U(\mathfrak{g}))$ an algebra isomorphism — Kontsevich's derivation of the Duflo theorem from formality.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*