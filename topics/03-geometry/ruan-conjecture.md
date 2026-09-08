---
id: 03-geometry/ruan-conjecture
title: "Ruan Conjecture"
topic: 03-geometry
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Ruan Conjecture (Crepant Resolution / Crepant Transformation Conjecture)

> **Topic:** Algebraic & Differential Geometry · **ID:** `03-geometry/ruan-conjecture` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Let $\mathcal{X}$ be a Gorenstein orbifold (smooth Deligne–Mumford stack with trivial generic stabiliser and Gorenstein coarse space $X$), and let $\pi\colon Y \to X$ be a crepant resolution, i.e. $\pi^{*}K_X = K_Y$. **Ruan's conjecture** asserts that the quantum cohomology ring of $Y$ and the Chen–Ruan orbifold quantum cohomology ring of $\mathcal{X}$ are isomorphic after analytic continuation in the quantum parameters and a specialisation of the parameters dual to exceptional/twisted classes:

$$QH^{*}_{\mathrm{CR}}(\mathcal{X})\ \cong\ QH^{*}(Y)\qquad\text{over }\mathbb{C}\text{, after analytic continuation.}$$

In its original and strongest form (Ruan 1999) the statement is birational rather than orbifold-theoretic: **if $X_1$ and $X_2$ are $K$-equivalent smooth projective varieties (there is a common resolution $\phi_i\colon Z\to X_i$ with $\phi_1^{*}K_{X_1}=\phi_2^{*}K_{X_2}$), then their quantum cohomology rings are isomorphic after analytic continuation.** This is the *quantum minimal model conjecture*: the quantum ring, unlike the classical ring, is a birational invariant within a $K$-equivalence class. The crepant resolution case is the specialisation where one side is an orbifold.

A complete proof must supply, for each such pair, (i) a linear isomorphism $\mathcal{L}\colon H^{*}_{\mathrm{CR}}(\mathcal{X};\mathbb{C})\to H^{*}(Y;\mathbb{C})$, (ii) a proof that the genus-0 Gromov–Witten generating functions of $Y$, a priori formal power series in Novikov variables, are the Taylor expansions of functions analytic on a common domain, and (iii) that $\mathcal{L}$ intertwines the two quantum products after continuation along a specified path. A disproof requires a $K$-equivalent pair (or crepant resolution) whose quantum products are provably non-isomorphic — for instance non-convergent invariants, or monodromy-invariant ring data that differ.

## 2. Mathematical Foundations

**Chen–Ruan cohomology.** For $\mathcal{X}$ with inertia stack $I\mathcal{X}=\coprod_{i\in I}\mathcal{X}_i$ (components indexed by conjugacy classes of stabiliser elements $g$), set

$$H^{d}_{\mathrm{CR}}(\mathcal{X})\ :=\ \bigoplus_{i\in I} H^{\,d-2\,\mathrm{age}(\mathcal{X}_i)}(\mathcal{X}_i;\mathbb{Q}),\qquad \mathrm{age}(g)=\sum_{j=1}^{n}\frac{a_j}{r},$$

where $g$ acts on the tangent space with eigenvalues $e^{2\pi i a_j/r}$, $0\le a_j<r$. The grading is rational in general and integral exactly when $\mathcal{X}$ is Gorenstein. The Chen–Ruan cup product is defined by three-point orbifold invariants and involves the obstruction bundle over the double inertia stack.

**Genus-0 Gromov–Witten theory.** For $Y$ smooth projective, with $\{\phi_a\}$ a basis of $H^{*}(Y)$ and Novikov variables $q^{\beta}$,

$$\langle \phi_a * \phi_b,\phi_c\rangle \;=\; \sum_{\beta\in H_2(Y;\mathbb{Z})} q^{\beta}\, \langle \phi_a,\phi_b,\phi_c\rangle_{0,3,\beta},\qquad \langle\cdots\rangle_{0,3,\beta}=\int_{[\overline{\mathcal{M}}_{0,3}(Y,\beta)]^{\mathrm{vir}}}\prod \mathrm{ev}_i^{*}\phi_i .$$

The same formula with $\overline{\mathcal{M}}_{0,3}(\mathcal{X},\beta)$ (Abramovich–Graber–Vistoli twisted stable maps) defines $QH^{*}_{\mathrm{CR}}(\mathcal{X})$; here the quantum parameters include variables $u_i$ dual to twisted sectors of age $1$, which have no Novikov counterpart.

**Shape of the identification.** In the $A_1$/local model the exceptional parameter $q$ and the twisted parameter $u$ are matched by

$$q \;=\; -\,e^{\,i u},$$

so that $u=0$ (the orbifold point) corresponds to $q=-1$, a point *outside* the formal Novikov disc $|q|<\varepsilon$. Convergence and analytic continuation are therefore intrinsic to the statement, not technical fine print.

**Modern reformulation (Coates–Ruan).** Genus-0 theory is encoded by the Givental Lagrangian cone $\mathcal{L}_{\mathcal{X}}\subset \mathcal{H}_{\mathcal{X}} = H^{*}_{\mathrm{CR}}(\mathcal{X})\otimes\mathbb{C}((z^{-1}))$, a cone ruled by $z\,T_{f}\mathcal{L}$. The **crepant transformation conjecture** asserts the existence of a $\mathbb{C}((z^{-1}))$-linear symplectic transformation $\mathbb{U}\colon \mathcal{H}_{\mathcal{X}}\to\mathcal{H}_{Y}$ with

$$\mathbb{U}\big(\mathcal{L}_{\mathcal{X}}\big) = \mathcal{L}_{Y}$$

after analytic continuation, equivalently an isomorphism of quantum $D$-modules matching the integral structures $K^0(\mathcal{X})\to K^0(Y)$ given by the Fourier–Mukai transform $\mathbb{F}=R\pi_{*}\circ$ (Bridgeland–King–Reid / derived McKay equivalence). This form is stronger than the ring statement and is the one now standardly proved.

## 3. History & State of the Art (SOTA)

- **1999.** Y. Ruan, *Surgery, quantum cohomology and birational geometry*, conjectures invariance of quantum cohomology under $K$-equivalence, motivated by symplectic surgery and the physics of Calabi–Yau moduli (Aspinwall–Greene–Morrison flop transitions).
- **2001.** A.-M. Li and Y. Ruan prove the conjecture for simple (ordinary) flops of Calabi–Yau 3-folds using symplectic degeneration and the relative GW formalism.
- **2004.** Chen–Ruan orbifold cohomology is published; Ruan (2006) formulates the *cohomological crepant resolution conjecture*: $H^{*}_{\mathrm{CR}}(\mathcal{X})\cong H^{*}(Y)$ as the $q\to$ specialised limit of the quantum ring.
- **2007–2009.** Bryan–Graber isolate the **Hard Lefschetz condition** (age$(g)=$ age$(g^{-1})$ on all sectors) under which the conjecture takes a clean form, and verify it for $[\mathbb{C}^2/G]$, $\mathrm{Sym}^n(\mathbb{C}^2)$ and $A_n$ cases; Bryan–Gholampour prove the quantum McKay correspondence for polyhedral (ADE) singularities.
- **2009–2013.** Coates–Iritani–Tseng and Coates–Ruan reformulate everything in terms of Givental cones and Iritani's integral structure, replacing "specialisation of variables" by a symplectic transformation; the resulting statement is birationally symmetric and applies without the Hard Lefschetz hypothesis.
- **2010.** Lee–Lin–Wang prove invariance of quantum cohomology under **ordinary flops of arbitrary splitting type**, the deepest general result on the $K$-equivalence version.
- **2018.** Coates–Iritani–Jiang prove the crepant transformation conjecture for **all toric complete intersections** related by variation of GIT — the largest verified class to date.
- **2019–present.** Higher-genus and holomorphic-anomaly versions (Lho–Pandharipande for $[\mathbb{C}^3/\mathbb{Z}_3]$); extensions to quasimap and LG/CY wall-crossing.

## 4. Partial Results / Verified Cases

| Class | Result | Source |
|---|---|---|
| CY 3-fold simple flops | Full quantum ring invariance | Li–Ruan (2001) |
| $[\mathbb{C}^2/\mathbb{Z}_n]$, $A_n$ resolutions | Explicit ring isomorphism, $q=-e^{iu}$ | Bryan–Graber (2009) |
| $[\mathbb{C}^2/G]$, $G\subset SU(2)$ polyhedral | Quantum McKay: $q$-deformed root-system product | Bryan–Gholampour (2009) |
| $\mathrm{Sym}^n(\mathbb{C}^2)\ \leftrightarrow\ \mathrm{Hilb}^n(\mathbb{C}^2)$ | Full genus-0 equality | Bryan–Graber; Cheong–Gholampour |
| $[\mathbb{C}^3/\mathbb{Z}_3]\ \leftrightarrow\ K_{\mathbb{P}^2}$ | Genus 0 (Coates–Corti–Iritani–Tseng); all genus (Lho–Pandharipande, 2019) | — |
| Toric orbifolds / toric complete intersections related by VGIT | Crepant transformation conjecture for quantum $D$-modules and integral structures | Coates–Iritani–Jiang (2018) |
| Ordinary flops of splitting type, any dimension | Quantum rings isomorphic after continuation | Lee–Lin–Wang (2010, 2016) |
| Hard Lefschetz orbifolds, cohomological version | $H^*_{\mathrm{CR}}(\mathcal{X})\cong H^*(Y)$ in many families | Perroni, Fantechi–Göttsche, Uribe |

The Hard Lefschetz condition holds exactly when all twisted sectors have age concentrated so that $\dim H^{*}_{\mathrm{CR}}$ pairs symmetrically; e.g. $\mathcal{X}=[\mathbb{C}^{2}/G]$ satisfies it, $[\mathbb{C}^{3}/\mathbb{Z}_3]$ does not.

## 5. Principal Obstacles

- **Convergence.** Gromov–Witten potentials are only formal power series. The conjecture asserts continuation to $q=-1$; there is no general theorem that genus-0 GW potentials of a Calabi–Yau converge on any disc, so the statement is not even well-posed in general without an unproved analyticity input. This is the single largest gap.
- **Failure of deformation invariance.** Crepant resolutions and flops change $H^{*}$ and $H_2$; the standard toolkit (deformation invariance of GW invariants, symplectic cobordism) does not apply because the two spaces are not deformation equivalent — they are only $K$-equivalent.
- **Degeneration methods do not scale.** Li–Ruan's symplectic cutting works because a CY 3-fold flop is modelled on a single $(-1,-1)$-curve. For higher-dimensional or non-split flops the relative GW theory of the local model is itself unknown; Lee–Lin–Wang needed a quantum Leray–Hirsch theorem and a splitting principle to bypass it.
- **Non-Hard-Lefschetz cases break the grading.** When ages are not symmetric, $\mathcal{L}$ cannot preserve the cohomological grading, so no degree-based rigidity is available; only the $z$-graded cone/$D$-module formulation survives, and there the transformation $\mathbb{U}$ must be produced by hand from mirror data.
- **Mirror-theoretic input is method-bound.** Nearly every proof beyond dimension 2 uses an $I$-function from toric mirror symmetry or VGIT quasimap wall-crossing. No such $I$-function exists for a general Gorenstein orbifold, so all current techniques stop at (quotients by) torus-linearised data.
- **Higher genus.** Givental's quantisation formalism predicts a higher-genus statement only for semisimple quantum cohomology; Calabi–Yau cases are non-semisimple, so the transition from genus 0 to all genus requires holomorphic anomaly equations that are themselves conjectural.

## 6. The Gap

Proven: the conjecture for pairs where **one side admits a computable $I$-function** (toric, toric complete intersection, GIT quotients with torus actions) or where the geometry reduces to a **local model of dimension $\le 3$ with a split normal bundle**. In these cases analyticity is proved by explicit resummation (hypergeometric functions with finitely many singular points, or rational functions of $q$).

Unproven: the conjecture for a general Gorenstein orbifold or a general $K$-equivalent pair. The exact missing step is a *geometric* (as opposed to computational) construction of the symplectic transformation $\mathbb{U}$ — one derived from the derived-equivalence $D^{b}(\mathcal{X})\simeq D^{b}(Y)$ (Bridgeland–King–Reid) rather than from mirror hypergeometrics — together with an a priori analyticity theorem for the quantum connection of $Y$ near the wall separating the two large-radius limits. Concretely: prove that the quantum connection of a $K$-equivalent pair extends to a flat connection on a punctured domain containing both limit points, with monodromy matching the Fourier–Mukai action on $K^{0}$.

## 7. Current Research (as of June 2026)

- **Integral structures and $\Gamma$-conjecture programme** (Iritani, Kyoto; Coates, Imperial College London): showing $\mathbb{U}$ is the map induced by $\mathbb{F}=$ Fourier–Mukai on $K$-theory with $\hat\Gamma$-class framing. Verified for all toric cases; extension to non-abelian GIT quotients is active. *(frontier — verify)*
- **Quasimap and $\epsilon$-wall-crossing** (Ciocan-Fontanine, Kim; Cheong; Zhou): deriving crepant transformations as limits of stability wall-crossings, which sidesteps mirror theorems for some non-toric targets.
- **Non-abelian and Grassmannian flops** (Lee–Lin–Wang school in Taipei; Halpern-Leistner's magic windows via derived categories): the "window" subcategory formalism produces derived equivalences for many non-toric VGIT flops, and matching them with quantum $D$-modules is the current frontier. *(frontier — verify)*
- **Higher genus / holomorphic anomaly** (Lho, Pandharipande, Guo, Ross–Ruan): all-genus crepant resolution for local $\mathbb{P}^2$-type geometries, with modularity of the resummed potentials as the mechanism enforcing continuation.
- **Analyticity** (Iritani; Coates–Iritani "Fock sheaf" line): reducing convergence to conjectural bounds on GW invariants; no unconditional theorem for general CY targets. *(frontier — verify)*

## 8. Future Work

1. **Prove convergence** of genus-0 GW potentials for at least one non-toric CY class; this would make the general conjecture well-posed.
2. **Derived-categorical proof:** upgrade the Bridgeland–King–Reid equivalence to an equivalence of quantum $D$-modules directly, without mirror input — the strategy Ruan and Iritani both single out as the "correct" proof.
3. **Non-Gorenstein / discrepancy $>0$ analogues:** relate $QH$ of birational pairs with $K$-inequality, expecting a semi-orthogonal (not full) match, as in Kawamata's D-K conjecture.
4. **Symplectic-geometric formulation:** extend Li–Ruan's surgery framework to general symplectic birational cobordisms in dimension $\ge 8$.
5. **Higher genus without semisimplicity:** develop a Givental-type quantisation valid for CY quantum cohomology, giving all-genus statements beyond case-by-case modularity.

## 9. Key References

- **[Foundational]** Y. Ruan. *Surgery, quantum cohomology and birational geometry.* In: Northern California Symplectic Geometry Seminar, AMS Translations Ser. 2, vol. 196, 1999, 183–198. [DOI](https://doi.org/10.1090/trans2/196/09)
- **[Foundational]** W. Chen and Y. Ruan. *A new cohomology theory of orbifold.* Communications in Mathematical Physics 248 (2004), 1–31. [DOI](https://doi.org/10.1007/s00220-004-1089-4)
- **[Foundational]** Y. Ruan. *The cohomology ring of crepant resolutions of orbifolds.* In: Gromov–Witten Theory of Spin Curves and Orbifolds, Contemporary Mathematics 403, AMS, 2006, 117–126. [DOI](https://doi.org/10.1090/conm/403/07597)
- **[Foundational]** A.-M. Li and Y. Ruan. *Symplectic surgery and Gromov–Witten invariants of Calabi–Yau 3-folds.* Inventiones Mathematicae 145 (2001), 151–218. [DOI](https://doi.org/10.1007/s002220100146)
- **[SOTA]** J. Bryan and T. Graber. *The crepant resolution conjecture.* Proceedings of Symposia in Pure Mathematics 80.1 (2009), 23–42.
- **[SOTA]** T. Coates and Y. Ruan. *Quantum cohomology and crepant resolutions: a conjecture.* Annales de l'Institut Fourier 63 (2013), 431–478. [DOI](https://doi.org/10.5802/aif.2766)
- **[SOTA]** T. Coates, H. Iritani and H.-H. Tseng. *Wall-crossings in toric Gromov–Witten theory I: crepant examples.* Geometry & Topology 13 (2009), 2675–2744. [DOI](https://doi.org/10.2140/gt.2009.13.2675)
- **[SOTA]** T. Coates, H. Iritani and Y. Jiang. *The crepant transformation conjecture for toric complete intersections.* Advances in Mathematics 329 (2018), 1002–1087. [DOI](https://doi.org/10.1016/j.aim.2017.11.017)
- **[SOTA]** Y.-P. Lee, H.-W. Lin and C.-L. Wang. *Flops, motives, and invariance of quantum rings.* Annals of Mathematics 172 (2010), 243–290. [DOI](https://doi.org/10.4007/annals.2010.172.243)
- **[SOTA]** Y.-P. Lee, H.-W. Lin and C.-L. Wang. *Invariance of quantum rings under ordinary flops I, II.* Algebraic Geometry 3 (2016).
- **[SOTA]** H. Iritani. *An integral structure in quantum cohomology and mirror symmetry for toric orbifolds.* Advances in Mathematics 222 (2009), 1016–1079. [DOI](https://doi.org/10.1016/j.aim.2009.05.016)
- **[SOTA]** J. Bryan and A. Gholampour. *The quantum McKay correspondence for polyhedral singularities.* Inventiones Mathematicae 178 (2009), 655–681. [DOI](https://doi.org/10.1007/s00222-009-0212-8)
- **[SOTA]** H. Lho and R. Pandharipande. *Crepant resolution and the holomorphic anomaly equation for $[\mathbb{C}^3/\mathbb{Z}_3]$.* Proceedings of the London Mathematical Society 119 (2019), 781–813.
- **[Survey]** T. Coates, A. Corti, H. Iritani and H.-H. Tseng. *Hodge-theoretic mirror symmetry for toric stacks.* Journal of Differential Geometry 114 (2020), 41–115. [DOI](https://doi.org/10.4310/jdg/1577502022)
- **[Survey]** C.-L. Wang. *K-equivalence in birational geometry and characterizations of complex elliptic genera.* Journal of Algebraic Geometry 12 (2003), 285–306. [DOI](https://doi.org/10.1090/s1056-3911-02-00312-0)

## 10. Worked Example / Concrete Special Case

Take $\mathcal{X}=[\mathbb{C}^2/\mathbb{Z}_2]$ with $\mathbb{Z}_2$ acting by $(x,y)\mapsto(-x,-y)$, and $Y=T^{*}\mathbb{P}^1$, the minimal ($A_1$) resolution of the quadric cone $X=\mathbb{C}^2/\mathbb{Z}_2$. This is crepant: the exceptional curve $C\cong\mathbb{P}^1$ has $C\cdot C=-2$ and $K_Y=\pi^{*}K_X$.

**Resolution side.** $H^{2}(Y)$ is spanned by $\gamma$ with $\int_{C}\gamma=1$; since $[C]$ has self-intersection $-2$, $\gamma = -\tfrac12[C]$ and the classical product is $\gamma\cup\gamma=-\tfrac12\,[\mathrm{pt}]$. The only curve classes are $d[C]$, $d\ge 1$, and the degree-$d$ genus-0 invariant of the local $(-2)$-curve is the Aspinwall–Morrison multiple-cover contribution $N_d = 1/d^{3}$. The divisor axiom gives $\langle\gamma,\gamma,\gamma\rangle_{0,3,d[C]} = (\textstyle\int_{d[C]}\gamma)^{3}N_d = d^{3}\cdot d^{-3}=1$. Hence

$$\gamma * \gamma \;=\; \Big(-\tfrac12 + \sum_{d\ge1} q^{d}\Big)[\mathrm{pt}] \;=\; \Big(-\tfrac12 + \frac{q}{1-q}\Big)[\mathrm{pt}],$$

a rational function of $q$ with its only pole at $q=1$. It is therefore analytic at $q=-1$.

**Orbifold side.** $I\mathcal{X}$ has two components: the untwisted sector $\mathcal{X}$ and the sector fixed by $g=-1$, a point with $\mathrm{age}(g)=\tfrac12+\tfrac12=1$. So $H^{*}_{\mathrm{CR}}$ has a generator $\mathfrak{1}_{1/2}$ in degree $2$ — matching $\dim H^{2}(Y)=1$, as the McKay correspondence predicts. The orbifold Poincaré pairing gives $\langle\mathfrak{1}_{1/2},\mathfrak{1}_{1/2}\rangle=\tfrac12$, and the Chen–Ruan product is $\mathfrak{1}_{1/2}\cup\mathfrak{1}_{1/2}=\tfrac12[\mathrm{pt}]$ (the obstruction bundle is trivial for $[\mathbb{C}^2/\mathbb{Z}_2]$).

**Matching.** Substitute Ruan's change of variable $q=-e^{iu}$:

$$-\tfrac12+\frac{q}{1-q}\;=\;-\tfrac12-\frac{e^{iu}}{1+e^{iu}}\;=\;-1-\tfrac{i}{2}\tan\!\big(\tfrac{u}{2}\big),$$

which is analytic at $u=0$ and takes the value $-1$ there. Setting $u=0$ recovers the *classical* Chen–Ruan product, so the linear map $\mathcal{L}$ must satisfy $\mathcal{L}(\mathfrak{1}_{1/2})=c\,\gamma$ with $c^{2}\cdot\tfrac12 \cdot(\text{sign}) = $ the value $-1$, i.e. $c = i\sqrt{2}$. The isomorphism exists over $\mathbb{C}$ but **not** over $\mathbb{R}$ or $\mathbb{Q}$ — the factor $\sqrt{-1}$ is forced. This is the phenomenon Bryan and Graber highlight, and it is why the conjecture is stated with complex coefficients and analytic continuation rather than as a naive isomorphism of graded rings. The full $u$-dependence, $-1-\tfrac{i}{2}\tan(u/2)$, is exactly the generating function of the odd-insertion orbifold invariants $\langle\mathfrak{1}_{1/2}^{\,2k+1}\rangle$, so the two theories agree not just at a point but as analytic families — the local $A_1$ case of the conjecture in full.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*