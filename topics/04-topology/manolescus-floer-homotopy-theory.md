---
id: 04-topology/manolescus-floer-homotopy-theory
title: "Manolescu's Floer Homotopy Theory"
topic: 04-topology
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Manolescu's Floer Homotopy Theory

> **Topic:** Topology & Knot Theory · **ID:** `04-topology/manolescus-floer-homotopy-theory` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Floer homology assigns a graded abelian group to a 3-manifold (or a Lagrangian pair, or a symplectomorphism) as the Morse homology of an infinite-dimensional functional. The **Floer homotopy problem**, posed by Cohen–Jones–Segal (1995), asks whether such a group is the homology of a genuine object of stable homotopy theory:

> Given a Floer-type functional $\mathcal{L}$ on a space $\mathcal{C}$ with a compact moduli of flow lines, does there exist a spectrum $\mathbf{X}(\mathcal{L})$, natural in the geometric data, with $H_*(\mathbf{X}(\mathcal{L})) \cong HF_*(\mathcal{L})$, and does the assignment extend to a functor sending cobordisms to maps of spectra?

**Manolescu's programme** is the Seiberg–Witten realization of this question, together with its consequences. Concretely, the open problem has four coupled components:

1. **Construction.** For every closed 3-manifold $Y$ and $\mathrm{spin}^c$ structure $\mathfrak{s}$, produce an $S^1$-equivariant (and, for self-conjugate $\mathfrak{s}$, $\mathrm{Pin}(2)$-equivariant) spectrum $SWF(Y,\mathfrak{s})$, well defined up to canonical stable equivalence.
2. **Functoriality.** Show that a spin$^c$ cobordism $W: Y_0 \to Y_1$ induces a map $\mathrm{BF}(W): \Sigma^{a}SWF(Y_0,\mathfrak{s}_0) \to \Sigma^{b} SWF(Y_1,\mathfrak{s}_1)$, with gluing $\mathrm{BF}(W_1 \cup_Y W_0) \simeq \mathrm{BF}(W_1)\circ \mathrm{BF}(W_0)$, giving a spectrum-valued $(3{+}1)$-TQFT.
3. **Comparison.** Prove that the equivariant homology of $SWF$ recovers Kronheimer–Mrowka monopole Floer homology, and that its $\mathrm{Pin}(2)$-refinement recovers the invariants used in applications.
4. **Extraction.** Use generalized cohomology theories ($ko$, $KO$, $K(n)$, $MU$) applied to $\mathbf{X}$ to obtain invariants strictly stronger than those visible in ordinary homology.

A complete resolution means: (i) a construction valid for all $Y$ with no restriction on $b_1(Y)$, natural and functorial in the above sense; (ii) an analogous construction for instanton and Lagrangian Floer theory; (iii) identification of the resulting stable homotopy invariants. Components (1) and (4) are settled in significant ranges; (2) and the $b_1>0$ naturality are not.

## 2. Mathematical Foundations

Let $Y$ be a closed oriented 3-manifold with Riemannian metric $g$ and $\mathrm{spin}^c$ structure $\mathfrak{s}$, spinor bundle $S$, Dirac operator $D_a$. The **Chern–Simons–Dirac functional** on connections-plus-spinors $(a,\phi) \in \Omega^1(Y;i\mathbb{R}) \oplus \Gamma(S)$ is

$$\mathcal{L}(a,\phi) \;=\; -\tfrac{1}{2}\int_Y (a - 2\hat a_0)\wedge da \;+\; \tfrac{1}{2}\int_Y \langle \phi, D_a \phi\rangle \, \mathrm{dvol}.$$

Its critical points are the Seiberg–Witten solutions; the downward gradient flow $\frac{d}{dt}(a,\phi) = -\nabla \mathcal{L}(a,\phi)$ is the 4-dimensional Seiberg–Witten equation on $\mathbb{R}\times Y$.

**Global Coulomb slice and finite-dimensional approximation.** Assume $b_1(Y)=0$. Fixing the global Coulomb gauge $d^*a=0$ leaves a residual $S^1$ (constant gauge transformations). Write the flow as $\frac{d}{dt}x = -(l + c)(x)$, where $l = (*d, D)$ is linear self-adjoint Fredholm and $c$ is compact-quadratic. Let $V_\lambda^\mu$ be the span of eigenvectors of $l$ with eigenvalues in $(\lambda,\mu]$, and let $\varphi_\lambda^\mu$ be the flow of $-(l + p^\mu_\lambda c)$ on $V^\mu_\lambda$. For $-\lambda,\mu \gg 0$ all trajectories bounded in $\mathcal{L}$ lie in a compact isolated invariant set $S^\mu_\lambda$, with **Conley index** $I^\mu_\lambda = I(S^\mu_\lambda)$, a pointed $S^1$-space.

**Definition (Manolescu 2003).** The Seiberg–Witten Floer stable homotopy type is the formal desuspension

$$SWF(Y,\mathfrak{s}) \;=\; \Sigma^{-n(Y,\mathfrak{s},g)\,\mathbb{C}}\,\Sigma^{-\dim V^0_\lambda(\mathbb{R})\,\mathbb{R}}\; I^\mu_\lambda,$$

an object of a category whose objects are triples $(A,m,n)$ with $A$ a pointed $S^1$-space, $m \in \mathbb{Z}$, $n \in \mathbb{Q}$, denoting $\Sigma^{-m\mathbb{C}}\Sigma^{-n\mathbb{R}}A$. The rational shift $n(Y,\mathfrak{s},g)$ is the index-theoretic correction

$$n(Y,\mathfrak{s},g)\;=\;\mathrm{ind}_{\mathbb C}\, D^+(W) - \frac{c_1(\mathfrak{s}_W)^2 - \sigma(W)}{8},$$

computed on any compact spin$^c$ 4-manifold $W$ bounding $(Y,\mathfrak{s})$; it makes $SWF$ metric-independent.

**$\mathrm{Pin}(2)$-symmetry.** Let $\mathrm{Pin}(2)=S^1\cup jS^1 \subset \mathbb{H}^\times$. When $\mathfrak{s}$ is self-conjugate (a spin structure), the charge-conjugation symmetry $j$ preserves the flow, so $SWF(Y,\mathfrak{s})$ is $\mathrm{Pin}(2)$-equivariant. With $\mathbb{F}_2$ coefficients,

$$H^*(B\mathrm{Pin}(2);\mathbb{F}_2)=\mathbb{F}_2[q,v]/(q^3), \qquad \deg q = 1,\ \deg v = 4 .$$

Borel homology $\widetilde{H}^{\mathrm{Pin}(2)}_*(SWF(Y,\mathfrak{s}))$ is a module over this ring; localizing at $v$ and reading off the minimal degrees of elements in the image of $\mathbb{F}_2[v]$, $q\mathbb{F}_2[v]$, $q^2\mathbb{F}_2[v]$ gives three homology-cobordism invariants

$$\alpha(Y,\mathfrak{s}) \;\ge\; \beta(Y,\mathfrak{s}) \;\ge\; \gamma(Y,\mathfrak{s}), \qquad \alpha \equiv \beta \equiv \gamma \equiv \mu(Y,\mathfrak{s}) \bmod 2,$$

with $\mu$ the Rokhlin invariant, and duality $\alpha(-Y)=-\gamma(Y)$, $\beta(-Y)=-\beta(Y)$.

**Galewski–Stern/Matumoto criterion.** A topological $n$-manifold, $n\ge 5$, is triangulable iff the obstruction $\delta(M)\in H^5(M;\ker\mu)$ — the Bockstein of the Kirby–Siebenmann class for $0\to\ker\mu\to\Theta^H_3\xrightarrow{\mu}\mathbb{Z}/2\to 0$ — vanishes. All such manifolds are triangulable iff this sequence splits, i.e. iff $\Theta^H_3$ contains an element of order 2 with $\mu = 1$.

## 3. History & State of the Art (SOTA)

- **1988–1995.** Floer's instanton and symplectic homologies; Cohen–Jones–Segal propose framed flow categories and the realization problem (*Floer Memorial Volume*, 1995).
- **2001–2004.** Bauer–Furuta refine the 4-dimensional Seiberg–Witten invariant to a stable cohomotopy class, proving connected-sum results invisible to numerical SW invariants.
- **2003.** Manolescu constructs $SWF(Y,\mathfrak{s})$ for $b_1(Y)=0$ (*Geom. Topol.* 7).
- **2007.** Manolescu proves a gluing theorem for relative Bauer–Furuta invariants along rational homology spheres.
- **2013/2016.** Manolescu introduces $\mathrm{Pin}(2)$-equivariant Seiberg–Witten Floer homology, defines $\alpha,\beta,\gamma$, and **disproves the triangulation conjecture in all dimensions $\ge 5$** (*J. Amer. Math. Soc.* 29).
- **2015–2018.** Khandhawit's new gauge slice; Khandhawit–Lin–Sasahira construct unfolded spectra for $b_1>0$; Lin gives a Morse–Bott monopole-Floer proof of the triangulation result; Lidman–Manolescu prove the two Seiberg–Witten Floer homologies agree.
- **2018–present.** $\mathrm{Pin}(2)$-methods yield the **10/8+4 theorem** (Hopkins–Lin–Shi–Xu) and equivariant-$KO$ bounds (J. Lin). In symplectic topology, Abouzaid–Blumberg use Morava $K$-theory to prove the Arnold conjecture over $\mathbb{F}_p$, and Abouzaid–McLean–Smith build global Kuranishi charts giving complex-cobordism-valued invariants.

## 4. Partial Results / Verified Cases

| Setting | Status |
|---|---|
| $b_1(Y)=0$, any $\mathfrak{s}$ | $SWF$ constructed, $S^1$-equivariant, metric-independent (Manolescu 2003) |
| $\mathfrak{s}$ self-conjugate, $b_1=0$ | $\mathrm{Pin}(2)$-equivariant refinement; $\alpha,\beta,\gamma$ defined (Manolescu 2016) |
| $b_1(Y)>0$ | Unfolded spectra $\underline{swf}^A,\underline{swf}^R$ constructed (Khandhawit–Lin–Sasahira 2018); further developed by Sasahira–Stoffregen |
| Cobordism maps | Relative Bauer–Furuta invariant defined; gluing proven along $b_1=0$ boundaries (Manolescu 2007), extended by Khandhawit–Lin–Sasahira |
| Comparison with $\widehat{HM}$ | Isomorphism $\widetilde{H}^{S^1}_*(SWF) \cong \widehat{HM}_*$ for rational homology spheres (Lidman–Manolescu, *Astérisque* 399, 2018) |
| Explicit computations | Seifert fibered spaces: $\alpha,\beta,\gamma$ computed (Stoffregen, *Compositio Math.* 156, 2020); connected sums of Seifert spaces |
| Dimension $\ge 5$ triangulation | Resolved negatively (Manolescu 2016) |
| 4-manifold spin bounds | Furuta $b_2 \ge \frac{10}{8}|\sigma| + 2$; strengthened to $+4$ for $|\sigma|>0$ under hypotheses (Hopkins–Lin–Shi–Xu) |
| Symplectic side | Arnold conjecture over $\mathbb{F}_p$ via Morava $K$-theory (Abouzaid–Blumberg 2021); flow-category foundations (Abouzaid–Blumberg 2024) |

## 5. Principal Obstacles

- **Non-compactness with $b_1>0$.** For $b_1(Y)>0$ the Chern–Simons–Dirac functional has a non-compact critical set (a torus of flat connections) and the harmonic 1-form directions carry no natural finite-dimensional approximation. The unfolded construction produces a pro-/ind-spectrum rather than a single spectrum, and the two versions $\underline{swf}^A$, $\underline{swf}^R$ are not known to be canonically identified.
- **Gauge fixing is not natural.** The Coulomb slice depends on the metric; comparing slices requires the correction $n(Y,\mathfrak{s},g)$, which is rational. Equivariant desuspension by fractional spheres has no honest model, forcing the auxiliary category of triples $(A,m,n)$ and blocking a straightforward $\infty$-categorical functor.
- **Reducibles.** The unique reducible solution is a fixed point of the $S^1$-action; standard transversality perturbations destroy $\mathrm{Pin}(2)$-equivariance, so ordinary Morse-theoretic model constructions do not apply and Conley index theory must be used instead.
- **Coherent orientations vs. framings.** Realizing a chain complex by a spectrum requires *smooth framings* of the flow category, not merely coherent orientations. Obstructions live in stable homotopy groups of spheres and are computable only in low degrees.
- **Analytic foundations in symplectic Floer theory.** Kuranishi/polyfold perturbation schemes yield virtual chains over $\mathbb{Q}$; extracting a spectrum needs integral, framed geometric data, which multivalued perturbations destroy.

## 6. The Gap

Section 4 delivers a spectrum for $b_1=0$ and an unfolded object for $b_1>0$; Section 1 demands a naturally defined, functorial spectrum-valued invariant for all $Y$. The precise missing steps:

1. **Naturality.** Existing constructions give equivalences, not *canonical* equivalences: there is no proof that the identifications between two finite-dimensional approximations form a coherent system (an $\infty$-functor from the space of metrics to spectra).
2. **Full gluing.** The composition law $\mathrm{BF}(W_1\cup_Y W_0)\simeq \mathrm{BF}(W_1)\circ\mathrm{BF}(W_0)$ is unproven when $b_1(Y)>0$ in general.
3. **Rational shifts.** No construction avoids the $\mathbb{Q}$-valued desuspension; a genuine spectrum requires a canonical model (e.g. via $\mathrm{Pin}(2)$-equivariant Thom spectra of index bundles).
4. **Beyond Seiberg–Witten.** No instanton Floer spectrum exists at all; the $SU(2)$ setting has no analogue of finite-dimensional approximation.

## 7. Current Research (as of June 2026)

- **Abouzaid–Blumberg (Stanford/Columbia, Northwestern)** — *Foundations of Floer homotopy theory* series: flow categories as objects of a stable $\infty$-category, bordism-theoretic framings, module structures over $MU$ and $K(n)$. *(frontier — verify)*
- **Manolescu, Lin, Stoffregen, Hendricks (Stanford, Tsinghua, Michigan State, Rutgers)** — interplay of $\mathrm{Pin}(2)$-spectra with involutive Heegaard Floer homology and the structure of $\Theta^H_3$; the group is known to contain a $\mathbb{Z}^\infty$ summand (Dai–Hom–Stoffregen–Truong).
- **Sasahira–Stoffregen** — Seiberg–Witten Floer spectra for $b_1>0$ and their gluing theory. *(frontier — verify)*
- **Homotopy theorists (Hopkins, Xu, Shi, Behrens)** — equivariant Mahowald invariants and $\mathrm{Pin}(2)$-$KO$ constraints on spin 4-manifold intersection forms; the $\frac{11}{8}$-conjecture remains the target.
- **Global Kuranishi charts (Abouzaid–McLean–Smith, Rezchikov, Bai–Xu)** — making symplectic Floer theory carry genuine stable-homotopy data.

## 8. Future Work

- Reformulate $SWF$ as a functor $\mathrm{Man}_3^{\mathrm{spin}^c}\to \mathrm{Sp}^{\mathrm{Pin}(2)}$ using an $\infty$-categorical Conley index, removing the auxiliary triple category.
- Prove an unrestricted gluing theorem for relative Bauer–Furuta invariants; this would give the first spectrum-level $(3{+}1)$-TQFT.
- Apply $ko$, $tmf$ and $K(n)$ to $SWF$ to extract invariants beyond $\alpha,\beta,\gamma$; target: the $\frac{11}{8}$-conjecture $b_2\ge \frac{11}{8}|\sigma|$.
- Determine whether $\Theta^H_3$ has *any* torsion; Manolescu's result only excludes 2-torsion with $\mu=1$.
- Construct an instanton Floer homotopy type, or prove an obstruction to its existence.

## 9. Key References

- **[Foundational]** R. L. Cohen, J. D. S. Jones, G. B. Segal. *Floer's infinite-dimensional Morse theory and homotopy theory.* In: The Floer Memorial Volume, Progress in Mathematics 133, Birkhäuser, 1995.
- **[Foundational]** C. Manolescu. *Seiberg–Witten–Floer stable homotopy type of three-manifolds with $b_1=0$.* Geometry & Topology 7 (2003), 889–932.
- **[Foundational]** S. Bauer, M. Furuta. *A stable cohomotopy refinement of Seiberg–Witten invariants: I.* Inventiones Mathematicae 155 (2004), 1–19; S. Bauer, *II*, ibid., 21–40.
- **[SOTA]** C. Manolescu. *Pin(2)-equivariant Seiberg–Witten Floer homology and the triangulation conjecture.* Journal of the AMS 29 (2016), 147–176.
- **[SOTA]** T. Khandhawit, J. Lin, H. Sasahira. *Unfolded Seiberg–Witten Floer spectra, I: Definition and invariance.* Geometry & Topology 22 (2018), 2027–2114.
- **[SOTA]** T. Lidman, C. Manolescu. *The equivalence of two Seiberg–Witten Floer homologies.* Astérisque 399 (2018).
- **[SOTA]** F. Lin. *A Morse–Bott approach to monopole Floer homology and the triangulation conjecture.* Memoirs of the AMS 255 (2018), no. 1221.
- **[SOTA]** M. Stoffregen. *Pin(2)-equivariant Seiberg–Witten Floer homology of Seifert fibrations.* Compositio Mathematica 156 (2020), 199–250.
- **[SOTA]** M. J. Hopkins, J. Lin, X. D. Shi, Z. Xu. *Intersection forms of spin 4-manifolds and the Pin(2)-equivariant Mahowald invariant.* arXiv:1812.04052 (2018).
- **[SOTA]** M. Abouzaid, A. J. Blumberg. *Arnold conjecture and Morava K-theory.* arXiv:2103.01507 (2021).
- **[Classical]** D. E. Galewski, R. J. Stern. *Classification of simplicial triangulations of topological manifolds.* Annals of Mathematics 111 (1980), 1–34.
- **[Survey]** C. Manolescu. *Homology cobordism and triangulations.* Proceedings of the ICM 2018, Rio de Janeiro, Vol. II, 1175–1191.
- **[Survey]** R. L. Cohen. *Floer homotopy theory, realizing chain complexes by module spectra.* Contemporary Mathematics 519, AMS, 2010.

## 10. Worked Example / Concrete Special Case

**(a) $Y = S^3$.** With the round metric and the unique $\mathrm{spin}^c$ structure, the only solution to the Seiberg–Witten equations in the Coulomb slice is the reducible $(0,0)$: $S^3$ has positive scalar curvature $s>0$, and the Weitzenböck formula $D_a^2 = \nabla^*\nabla + \frac{s}{4} + \frac{1}{2}\rho(F_{a})$ forces $\phi = 0$. Hence the isolated invariant set is $S^\mu_\lambda = \{0\}$, its Conley index is the one-point compactification $(V^\mu_\lambda)^+$, and the correction term $n(S^3,\mathfrak{s},g)=0$ (take $W = D^4$: $\mathrm{ind}_{\mathbb C}D^+=0$, $\sigma=0$). Desuspending,

$$SWF(S^3) \;\simeq\; S^0 .$$

Its reduced $\mathrm{Pin}(2)$-Borel homology is $\widetilde{H}^{\mathrm{Pin}(2)}_*(S^0;\mathbb{F}_2)= H_*(B\mathrm{Pin}(2);\mathbb{F}_2)$, on which $v$ acts freely in degrees $0,1,2$ modulo $q^3=0$. The three towers begin in degree $0$, so

$$\alpha(S^3)=\beta(S^3)=\gamma(S^3)=0, \qquad \mu(S^3)=0 \ \checkmark$$

consistent with $\alpha\equiv\beta\equiv\gamma\equiv\mu \pmod 2$.

**(b) Disproof of the triangulation conjecture.** Suppose $[Y]\in\Theta^H_3$ has order 2, i.e. $Y \\# Y$ bounds a homology $\mathbb{Z}$-cobordism to $S^3$. Then $[Y]=[-Y]$, and since $\beta$ is a homology cobordism invariant,

$$\beta(Y) = \beta(-Y) = -\beta(Y) \;\Longrightarrow\; 2\beta(Y)=0 \;\Longrightarrow\; \beta(Y)=0 .$$

By the congruence $\beta \equiv \mu \pmod 2$, $\mu(Y)=0$. So **no** element of order 2 in $\Theta^H_3$ has Rokhlin invariant 1, the Galewski–Stern sequence does not split, and non-triangulable topological manifolds exist in every dimension $\ge 5$.

**(c) A nontrivial value.** For the Poincaré sphere $\Sigma(2,3,5)$, bounding the negative-definite $E_8$-manifold gives $\mu = \sigma/8 \equiv 1 \pmod 2$; the Seifert-fibered computations give $\beta(\Sigma(2,3,5)) = 1 \neq 0$. By (b) this immediately shows $[\Sigma(2,3,5)]$ is not 2-torsion in $\Theta^H_3$ — a conclusion invisible to the Frøyshov invariant alone, which is the concrete payoff of passing from homology to the $\mathrm{Pin}(2)$-equivariant homotopy type.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*