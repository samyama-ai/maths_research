---
id: 02-algebra-group-theory/littelmann-path-model
title: "Littelmann Path Model"
topic: 02-algebra-group-theory
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Littelmann Path Model

> **Topic:** Algebra & Group Theory · **ID:** `02-algebra-group-theory/littelmann-path-model` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

The problem: **find a uniform, type-independent combinatorial model that computes characters, tensor product decompositions, branching rules and Demazure characters for the irreducible integrable highest-weight modules of an arbitrary symmetrizable Kac–Moody algebra.**

Before 1994 the available combinatorics was type-by-type: Young tableaux and the Littlewood–Richardson rule in type $A$, Kashiwara–Nakashima tableaux in types $B,C,D$, Littelmann's own patterns for $G_2$, nothing systematic outside finite type. The demand is a single combinatorial set $\mathbb{B}(\lambda)$, defined for every symmetrizable Kac–Moody root datum and every dominant integral $\lambda$, with an explicit weight map and explicit operators, such that

$$\operatorname{ch} V(\lambda)=\sum_{\pi\in\mathbb{B}(\lambda)} e^{\pi(1)},\qquad \mathbb{B}(\lambda)\otimes\mathbb{B}(\mu)\cong\bigsqcup_{\nu} \mathbb{B}(\nu)^{\oplus c^{\nu}_{\lambda\mu}} .$$

Littelmann (1994, 1995) constructed such a model out of **piecewise-linear paths in $\mathfrak{h}^*_{\mathbb{R}}$** together with **root operators** $e_\alpha,f_\alpha$, and proved the required properties. The core problem is therefore **solved**. What remains open, and what this page tracks, is the boundary of the method: non-symmetrizable Kac–Moody algebras, Borcherds and super algebras, positive characteristic, and the geometric/quantum-affine refinements where uniform path models are still conjectural.

## 2. Mathematical Foundations

Let $A=(a_{ij})_{i,j\in I}$ be a symmetrizable generalized Cartan matrix, $\mathfrak{g}=\mathfrak{g}(A)$ the Kac–Moody algebra, $\mathfrak{h}$ its Cartan subalgebra, $\Pi=\{\alpha_i\}$ simple roots, $\Pi^\vee=\{\alpha_i^\vee\}$ simple coroots, $P$ the weight lattice, $P^+$ the dominant integral weights, $W$ the Weyl group.

**Paths.** Let $\Pi_{\mathrm{paths}}$ be the set of piecewise-linear maps $\pi:[0,1]\to\mathfrak{h}^*_{\mathbb{R}}$ with $\pi(0)=0$ and $\pi(1)\in P$, taken modulo reparametrization. Weight: $\mathrm{wt}(\pi)=\pi(1)$. Concatenation:

$$(\pi_1*\pi_2)(t)=\begin{cases}\pi_1(2t), & 0\le t\le \tfrac12,\\[2pt] \pi_1(1)+\pi_2(2t-1), & \tfrac12\le t\le 1.\end{cases}$$

**Root operators.** Fix a simple root $\alpha$ and set $h(t)=\langle \pi(t),\alpha^\vee\rangle$, $m=\min_{t\in[0,1]}h(t)$ (an integer for the paths in play).

- $f_\alpha\pi$ is defined iff $h(1)-m\ge 1$. Put $t_0=\min\{t:h(t)=m\}$ and $t_1=\min\{t\ge t_0: h(t)=m+1\}$. Then
$$f_\alpha\pi(t)=\begin{cases}\pi(t), & t\le t_0,\\ \pi(t_0)+s_\alpha\big(\pi(t)-\pi(t_0)\big), & t_0\le t\le t_1,\\ \pi(t)-\alpha, & t\ge t_1.\end{cases}$$
- $e_\alpha\pi$ is defined iff $m\le -1$; put $t_1=\max\{t:h(t)=m\}$, $t_0=\max\{t\le t_1:h(t)=m+1\}$, reflect on $[t_0,t_1]$ and translate by $+\alpha$ afterwards. Otherwise $e_\alpha\pi=\mathbf{0}$.

Here $s_\alpha(\mu)=\mu-\langle\mu,\alpha^\vee\rangle\alpha$. Set $\varepsilon_\alpha(\pi)=\max\{n:e_\alpha^n\pi\ne\mathbf 0\}=-m$ and $\varphi_\alpha(\pi)=h(1)-m$, so $\varphi_\alpha-\varepsilon_\alpha=\langle\mathrm{wt}(\pi),\alpha^\vee\rangle$: the axioms of a **crystal** in Kashiwara's sense.

**Main theorem (Littelmann).** Let $\pi_\lambda$ be any path from $0$ to $\lambda\in P^+$ contained in the dominant chamber, and let
$$\mathbb{B}(\lambda)=\{f_{i_1}\cdots f_{i_k}\pi_\lambda\ :\ k\ge 0,\ i_j\in I\}\setminus\{\mathbf 0\}.$$
Then (i) $\mathbb{B}(\lambda)$ is independent of the choice of $\pi_\lambda$ up to weight-preserving bijection; (ii) $\operatorname{ch}V(\lambda)=\sum_{\pi\in\mathbb{B}(\lambda)}e^{\pi(1)}$; (iii) $\mathbb{B}(\lambda)*\mathbb{B}(\mu)\cong\bigsqcup_{\eta}\mathbb{B}(\lambda+\eta(1))$, the union over $\eta\in\mathbb{B}(\mu)$ with $\pi_\lambda*\eta$ entirely dominant — the **generalized Littlewood–Richardson rule**; (iv) for $w\in W$, the subset of paths of the form $f_{i_1}\cdots f_{i_k}\pi_\lambda$ with $\pi(1)\le w\lambda$-admissible initial direction gives the **Demazure character** $\operatorname{ch}V_w(\lambda)$ (Demazure character formula, including for Kac–Moody $w$).

**LS paths.** The canonical representative model: for $\lambda\in P^+$, an *LS path of shape $\lambda$* is a pair $(\underline{\sigma};\underline{a})$ with $\sigma_1>\sigma_2>\cdots>\sigma_r$ in $W/W_\lambda$ (Bruhat order) and $0=a_0<a_1<\cdots<a_r=1$ rational, satisfying the **$a_i$-chain condition** of Lakshmibai–Seshadri; the associated path is $\pi(t)=\sum_{j<i}(a_j-a_{j-1})\sigma_j\lambda+(t-a_{i-1})\sigma_i\lambda$ for $t\in[a_{i-1},a_i]$.

## 3. History & State of the Art

- **1986** — Lakshmibai–Seshadri, *Geometry of $G/P$ V*, introduce LS paths (as "standard monomials") for finite-type $G/P$, conjecturally basing Demazure modules.
- **1990–91** — Kashiwara constructs crystal bases at $q\to0$ for $U_q(\mathfrak{g})$, $\mathfrak{g}$ symmetrizable Kac–Moody; Lusztig constructs canonical bases in the simply-laced case. Existence is proved, but the combinatorics is not explicit outside classical types.
- **1994** — Littelmann, *A Littlewood–Richardson rule for symmetrizable Kac–Moody algebras* (Invent. Math. **116**): LS paths and the tensor rule.
- **1995** — Littelmann, *Paths and root operators in representation theory* (Ann. of Math. **142**): the general path model with arbitrary dominant initial path; independence of the choice; Demazure character formula; branching to Levi subalgebras.
- **1996–98** — Kashiwara (*Similarity of crystal bases*) and Joseph (*Quantum Groups and Their Primitive Ideals*) prove $\mathbb{B}(\lambda)$ is isomorphic to Kashiwara's crystal $B(\lambda)$ as a crystal, closing the loop with quantum groups. Littelmann, *Cones, crystals, and patterns* (Transform. Groups **3**, 1998) gives the polyhedral (string-cone) form.
- **1999–2008** — Geometrization. Gaussent–Littelmann (*LS galleries, the path model, and MV cycles*, Duke Math. J. **127**, 2005) realize LS galleries in the affine building and relate them to Mirković–Vilonen cycles; Baumann–Gaussent (Represent. Theory **12**, 2008) make the MV-cycle/crystal comparison precise. Kapovich–Millson (Groups Geom. Dyn. **2**, 2008) give a metric-geometry path model in Euclidean buildings.
- **2008–2020** — Uniform alternatives and extensions: Lenart–Postnikov's **alcove model** (Trans. AMS **360**, 2008); Naito–Sagaki's level-zero LS paths for quantum affine algebras; Lenart–Naito–Sagaki–Schilling–Shimozono's quantum/semi-infinite LS paths for Kirillov–Reshetikhin crystals.

## 4. Partial Results / Verified Cases

- **Fully proved:** all symmetrizable Kac–Moody $\mathfrak{g}$, all $\lambda\in P^+$, over $\mathbb{C}$ (or any field of characteristic $0$) — character formula, tensor decomposition, restriction to Levi subalgebras, Demazure characters (Littelmann 1994, 1995).
- **Finite types $A_n$–$G_2$:** the model specializes to classical combinatorics. In type $A_n$, LS paths of shape $\lambda$ are in bijection with semistandard Young tableaux of shape $\lambda$, and the concatenation rule reproduces the classical Littlewood–Richardson coefficients $c^\nu_{\lambda\mu}$. In types $B_n,C_n,D_n$ it matches Kashiwara–Nakashima tableaux; in $G_2$, Littelmann's earlier pattern model.
- **Affine types $X^{(r)}_N$:** level-$\ell$ integrable modules are covered; the level-zero extremal-weight modules of $U_q(\widehat{\mathfrak{g}})$ are handled by Naito–Sagaki (IMRN 2003; Proc. LMS 2008) for arbitrary level-zero shape.
- **Geometric verification:** for $G$ reductive over $\mathbb{C}$ and its affine Grassmannian, LS galleries index MV cycles for all types (Gaussent–Littelmann 2005; Baumann–Gaussent 2008) — bijection, not merely equinumerosity.
- **Applications proved via the model:** PRV-type components; the Kac–Moody Demazure character formula independent of Kumar–Mathieu's positive-characteristic geometry; Littelmann's standard monomial theory for symmetrizable Kac–Moody $G/B$.
- **Not covered:** non-symmetrizable $A$; Borcherds algebras with imaginary simple roots; Kac–Moody superalgebras with isotropic odd simple roots; modular ($\operatorname{char} k=p$) simple characters.

## 5. Principal Obstacles

- **Symmetrizability is used, not incidental.** The proofs of the tensor and independence theorems ultimately rest on the existence of a $W$-invariant nondegenerate form $(\ ,\ )$ on $\mathfrak{h}^*$ and on the Kac–Kazhdan/Shapovalov machinery behind integrable highest-weight theory. Without it, $\langle\ ,\alpha^\vee\rangle$-height functions lose the reflection symmetry that makes $f_\alpha$ well defined on concatenations, and $\operatorname{ch}V(\lambda)$ has no Weyl–Kac product form to match against.
- **Non-symmetrizable case: no crystal to model.** Kashiwara's crystal-base existence proof needs the grand-loop induction driven by the symmetrizable Shapovalov form; for non-symmetrizable $A$ it is not known that $B(\lambda)$ exists at all. A path model here would have to *construct* the invariant, not merely encode it.
- **Positive characteristic.** $\mathbb{B}(\lambda)$ computes $\operatorname{ch}V(\lambda)$ = Weyl module character in char $p$, but simple modules $L(\lambda)$ have characters governed by $p$-Kazhdan–Lusztig / Lusztig character-formula phenomena (and Williamson's counterexamples to expected bounds). Root operators are characteristic-free and cannot see $p$-torsion in the Frobenius kernel cohomology, so no naive path model computes $\operatorname{ch}L(\lambda)$.
- **Isotropic odd roots.** For superalgebras with $\langle\alpha,\alpha^\vee\rangle=0$ on an odd simple root, the height function $h(t)$ is constant along $\alpha$ and $s_\alpha$ is not a reflection; the operator definitions degenerate.
- **Positivity and geometry.** Identifying paths with *canonical* basis elements (rather than with a crystal isomorphic to $B(\lambda)$) requires geometry; the MV-cycle dictionary is type-uniform but the resulting bases depend on choices (Baumann–Gaussent show the MV basis and the semicanonical basis differ in general).

## 6. The Gap

Section 4's theorems hold exactly on the symmetrizable, characteristic-zero, integrable-highest-weight locus. The precise gaps:

1. **Non-symmetrizable Kac–Moody.** Needed step: a construction of $\mathbb{B}(\lambda)$ with the crystal axioms whose character equals $\operatorname{ch}V(\lambda)$, without invoking a symmetric bilinear form. Equivalent difficulty: proving existence of crystal bases for non-symmetrizable $U_q(\mathfrak g)$.
2. **Canonical vs. crystal.** The path model gives the crystal $B(\lambda)$; lifting it to an explicit basis of $V(\lambda)$ with positive structure constants (Lusztig positivity) is open outside symmetric type.
3. **Level zero / semi-infinite.** For quantum affine $U_q'(\widehat{\mathfrak g})$, uniform path models for *all* Kirillov–Reshetikhin crystals $B^{r,s}$ exist only conditional on the existence of $B^{r,s}$ itself, which is open for several non-simply-laced/twisted $(r,s)$ *(frontier — verify)*.

## 7. Current Research (as of June 2026)

- **Quantum and semi-infinite LS paths.** Lenart, Naito, Sagaki, Schilling, Shimozono continue the program identifying quantum LS paths with semi-infinite Lakshmibai–Seshadri paths and with specializations of Macdonald polynomials at $t=0$; connections to Chevalley formulas in the $K$-theory of semi-infinite flag manifolds (Kato, Naito, Sagaki) are the most active front *(frontier — verify)*.
- **Buildings and galleries.** Gaussent, Littelmann (Köln), Ciubotaru/Schwer, and Hitzelberger's school study Hecke-path and gallery models over local fields, including affine Deligne–Lusztig varieties.
- **Categorification.** Khovanov–Lauda–Rouquier algebra module categories give a second uniform "model"; comparing crystal structures on simple KLR modules with LS paths for arbitrary symmetrizable type is ongoing (Kleshchev, Lauda, Tingley).
- **Beyond Kac–Moody.** Path/gallery combinatorics for Borcherds–Kac–Moody algebras and for hyperbolic types with imaginary root data; also Kashiwara–Kim–Oh–Park style crystal combinatorics for quiver Hecke superalgebras.

## 8. Future Work

- Construct or obstruct crystal bases for non-symmetrizable $U_q(\mathfrak g)$; a path model would be the natural vehicle.
- Extend LS galleries to mixed characteristic (Witt vector affine Grassmannians) to obtain MV-type bases for $p$-adic geometric Satake.
- Give an intrinsic, non-recursive description of the set $\mathbb{B}(\lambda)$ for arbitrary dominant initial path (currently the description is intrinsic only for LS paths).
- Uniform path models for the $p$-canonical basis, matching Williamson's $p$-cells.
- Path models for Kac–Moody superalgebras with isotropic simple roots, e.g. via odd reflections combined with concatenation.

## 9. Key References

- **[Foundational]** P. Littelmann. *A Littlewood–Richardson rule for symmetrizable Kac–Moody algebras.* Inventiones Mathematicae **116** (1994), 329–346.
- **[Foundational]** P. Littelmann. *Paths and root operators in representation theory.* Annals of Mathematics (2) **142** (1995), 499–525.
- **[Foundational]** M. Kashiwara. *On crystal bases of the $q$-analogue of universal enveloping algebras.* Duke Mathematical Journal **63** (1991), 465–516.
- **[Foundational]** V. Lakshmibai, C. S. Seshadri. *Geometry of $G/P$ – V.* Journal of Algebra **100** (1986), 462–557.
- **[Structural]** A. Joseph. *Quantum Groups and Their Primitive Ideals.* Ergebnisse der Mathematik 29, Springer, 1995.
- **[Structural]** P. Littelmann. *Cones, crystals, and patterns.* Transformation Groups **3** (1998), 145–179.
- **[Geometric]** S. Gaussent, P. Littelmann. *LS galleries, the path model, and MV cycles.* Duke Mathematical Journal **127** (2005), 35–88.
- **[SOTA / Recent]** P. Baumann, S. Gaussent. *On Mirković–Vilonen cycles and crystal combinatorics.* Representation Theory **12** (2008), 83–130.
- **[SOTA / Recent]** C. Lenart, A. Postnikov. *A combinatorial model for crystals of Kac–Moody algebras.* Transactions of the AMS **360** (2008), 4349–4381.
- **[SOTA / Recent]** S. Naito, D. Sagaki. *Path model for a level-zero extremal weight module over a quantum affine algebra.* International Mathematics Research Notices **2003**, no. 32, 1731–1754.
- **[SOTA / Recent]** M. Kapovich, J. J. Millson. *A path model for geodesics in Euclidean buildings and its applications to representation theory.* Groups, Geometry, and Dynamics **2** (2008), 405–480.
- **[Survey]** D. Bump, A. Schilling. *Crystal Bases: Representations and Combinatorics.* World Scientific, 2017.
- **[Survey]** S. Kumar. *Kac–Moody Groups, their Flag Varieties and Representation Theory.* Progress in Mathematics 204, Birkhäuser, 2002.

## 10. Worked Example / Concrete Special Case

Take $\mathfrak g=\mathfrak{sl}_3$, $I=\{1,2\}$, fundamental weights $\omega_1,\omega_2$. Write the three weights of $V(\omega_1)$ as
$$\varepsilon_1=\omega_1,\qquad \varepsilon_2=\omega_1-\alpha_1,\qquad \varepsilon_3=\omega_1-\alpha_1-\alpha_2=-\omega_2,$$
and let $\pi_i(t)=t\,\varepsilon_i$ be the straight-line paths. Then $\mathbb{B}(\omega_1)=\{\pi_1,\pi_2,\pi_3\}$.

*Check one root operator.* For $\pi_1$ and $\alpha=\alpha_1$: $h(t)=\langle t\omega_1,\alpha_1^\vee\rangle=t$, so $m=0$ and $h(1)-m=1\ge1$, hence $f_1$ is defined with $t_0=0$, $t_1=1$. The whole path is reflected: $f_1\pi_1(t)=s_{\alpha_1}(t\omega_1)=t(\omega_1-\alpha_1)=\pi_2(t)$. Similarly $f_2\pi_2=\pi_3$, and $f_1\pi_2=\mathbf 0$ because $h(t)=-t$ gives $m=-1$, $h(1)-m=0$.

*Tensor product $V(\omega_1)^{\otimes 2}$.* By the concatenation rule, the irreducible constituents correspond to $\eta\in\mathbb{B}(\omega_1)$ with $\pi_1*\eta$ contained in the dominant chamber:

| $\eta$ | endpoint of $\pi_1*\eta$ | $\langle\cdot,\alpha_1^\vee\rangle$ along second leg | $\langle\cdot,\alpha_2^\vee\rangle$ | dominant? |
|---|---|---|---|---|
| $\pi_1$ | $2\omega_1$ | $1+t\ge0$ | $0$ | yes |
| $\pi_2$ | $2\omega_1-\alpha_1=\omega_2$ | $1-t\ge0$ | $t\ge0$ | yes |
| $\pi_3$ | $\omega_1-\omega_2$ | $1-t\ge 0$ | $-t<0$ | no |

Hence
$$V(\omega_1)\otimes V(\omega_1)\;\cong\;V(2\omega_1)\oplus V(\omega_2),\qquad 3\times3=6+3 .$$

*A Kac–Moody instance where tableaux do not exist.* Let $A=\begin{pmatrix}2&-3\\-3&2\end{pmatrix}$ (rank-2 hyperbolic, symmetrizable) and $\lambda=\omega_1$. Starting from $\pi_{\omega_1}(t)=t\omega_1$, applying $f_1$ then $f_2$ then $f_1$ produces paths with endpoints $\omega_1,\ \omega_1-\alpha_1,\ \omega_1-\alpha_1-3\alpha_2$ (since $\langle\omega_1-\alpha_1,\alpha_2^\vee\rangle=3$, so $f_2$ may be applied three times), and the process never terminates: $\mathbb{B}(\omega_1)$ is infinite, matching $\dim V(\omega_1)=\infty$. No tableau model is available here, while the path recursion runs verbatim — the point of the uniform construction.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*