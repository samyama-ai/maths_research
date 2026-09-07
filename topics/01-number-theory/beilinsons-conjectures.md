---
id: 01-number-theory/beilinsons-conjectures
title: "Beilinson's Conjectures"
topic: 01-number-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Beilinson's Conjectures

> **Topic:** Number Theory · **ID:** `01-number-theory/beilinsons-conjectures` · **Status:** open

## 1. Problem Statement / Conjecture

Beilinson's conjectures form a sweeping generalization of several classical theorems and open problems in algebraic number theory and arithmetic geometry, including Dirichlet's analytic class number formula and the Birch and Swinnerton-Dyer conjecture. 

The conjecture predicts that the leading non-zero coefficient in the Taylor expansion of the L-function $L(M, s)$ of an arithmetic motive $M$ (typically the $i$-th cohomology of a smooth projective variety $X$ over a number field $F$) at integer points $s=n$ can be expressed exactly (up to a non-zero rational number) as the determinant of a canonical "regulator map." This regulator map evaluates elements of the algebraic $K$-theory (or motivic cohomology) of $X$ into its Deligne cohomology.

A complete proof of the conjecture requires:
1. Proving that the motivic cohomology groups have the finite ranks predicted by the conjecture.
2. Showing that the Beilinson regulator map induces an isomorphism of real vector spaces after tensoring the motivic cohomology modulo torsion with $\mathbb{R}$.
3. Demonstrating that the determinant of this regulator map, calculated with respect to a rational basis of motivic cohomology and a rational basis of the Betti/de Rham cohomology, equals the leading Taylor coefficient of the L-function at $s=n$.

## 2. Mathematical Foundations

Let $X$ be a smooth projective variety of dimension $d$ over a number field $F$. Let $H^i(X)$ denote the $i$-th étale cohomology group $H^i_{\text{ét}}(X_{\overline{F}}, \mathbb{Q}_\ell)$, which forms a Galois representation. The L-function associated to this cohomology is defined by an Euler product over the finite places $v$ of $F$:

$$ L(H^i(X), s) = \prod_{v \nmid \infty} P_v(N(v)^{-s})^{-1} $$

where $P_v(T) = \det(1 - \text{Frob}_v \cdot T \mid H^i(X)^{I_v})$, and $\text{Frob}_v$ is the geometric Frobenius, $I_v$ is the inertia group, and $N(v)$ is the norm of the place.

Beilinson relates the value of $L(H^i(X), s)$ at an integer $s=n \ge i/2 + 1$ to the **motivic cohomology** of $X$, denoted $H^j_{\mathcal{M}}(X, \mathbb{Q}(n))$. Motivic cohomology is isomorphic to pieces of the algebraic $K$-theory of $X$ under the Adams operations:

$$ H^j_{\mathcal{M}}(X, \mathbb{Q}(n)) \cong K_{2n-j}(X)^{(n)} \otimes \mathbb{Q} $$

For $X$ viewed as a complex manifold via embeddings $\sigma: F \hookrightarrow \mathbb{C}$, there is the **Deligne cohomology** $H^j_{\mathcal{D}}(X_{/\mathbb{R}}, \mathbb{R}(n))$. 

Beilinson defined the **regulator map**:

$$ r_{\mathcal{D}}: H^j_{\mathcal{M}}(X, \mathbb{Q}(n)) \longrightarrow H^j_{\mathcal{D}}(X_{/\mathbb{R}}, \mathbb{R}(n)) $$

For the critical case where $j = i+1$, the conjecture states that $r_{\mathcal{D}} \otimes \mathbb{R}$ is an isomorphism, and that the determinant of $r_{\mathcal{D}}$ with respect to natural $\mathbb{Q}$-structures on both sides coincides, up to a factor in $\mathbb{Q}^{\times}$, with the leading coefficient of $L(H^i(X), s)$ at $s=n$.

## 3. History & State of the Art (SOTA)

Alexander Beilinson proposed these conjectures in his landmark 1984 paper *"Higher regulators and values of L-functions"*. His work was heavily inspired by Spencer Bloch's late-1970s investigations into algebraic $K_2$ of elliptic curves and the values of their L-functions at $s=2$. Beilinson generalized Bloch's observations into a vast cohesive framework, incorporating Deligne cohomology and higher $K$-theory (recently formulated by Quillen).

Historically, the evaluation of L-functions at integers has been a central pillar of number theory:
- $s=1$ for the Dedekind zeta function $\zeta_F(s)$ yields Dirichlet’s Class Number Formula.
- Borel (1974) calculated the higher ranks of $K$-groups of number fields and linked them to $\zeta_F(n)$ for $n \ge 2$, paving the way for Beilinson's general formulation.
- The Birch and Swinnerton-Dyer conjecture deals with $H^1$ of an elliptic curve at $s=1$.

The State of the Art (SOTA) remains that the conjecture is wide open for general varieties. Progress is typically made on a case-by-case basis for specific varieties (mostly of dimensions 0, 1, and some surfaces) where the L-functions and $K$-theory can be described via modular forms and polylogarithms.

## 4. Partial Results / Verified Cases

The conjectures have been verified only in very specific, highly structured scenarios:

1. **Number Fields (Dimension 0):** By A. Borel's theorem, Beilinson's conjecture holds for $X = \text{Spec}(F)$ for any number field $F$ and any integer $n \ge 2$. Here, the regulator maps from $K_{2n-1}(\mathcal{O}_F)$ to $\mathbb{R}^{d_n}$, and its determinant gives the leading term of the Dedekind zeta function $\zeta_F(n)$.
2. **Modular Curves:** Beilinson proved his own conjecture for the value of the L-function of modular curves $X_0(N)$ at $s=2$. He explicitly constructed elements in $K_2(X_0(N))$ using modular units.
3. **Elliptic Curves over $\mathbb{Q}$:** For modular elliptic curves over $\mathbb{Q}$, the conjecture at $s=2$ was proven through the combined efforts of Bloch, Beilinson, Flach, and Kato, leveraging the theorem that all elliptic curves over $\mathbb{Q}$ are modular (Modularity Theorem).
4. **Artin Motives:** Beilinson proved the conjecture for Artin motives (motives of dimension 0 varieties over number fields) across all integer values.
5. **Certain K3 Surfaces:** The conjecture has been shown to hold for particular classes of K3 surfaces (e.g., product of two modular elliptic curves), heavily relying on Scholl's theory of motives of modular forms.

## 5. Principal Obstacles

The main barriers to proving Beilinson's conjectures broadly are both geometric and analytic:

- **Constructing Motivic Elements:** To even define the regulator determinant, one must produce a full-rank set of independent elements in the algebraic $K$-theory of the variety $X$. Unlike divisors (which live in $K_0$ and $K_1$), higher $K$-groups ($K_2, K_3, \dots$) are defined via highly abstract machinery (like Quillen's Q-construction) making explicit calculation exceptionally difficult.
- **Transcendental Regulators:** Calculating the image of the regulator map requires evaluating complicated integrals of differential forms (often requiring generalized polylogarithms). For arbitrary varieties without a connection to modular forms or symmetric spaces, there is no known toolkit to compute these integrals.
- **Analytic Continuation of L-functions:** The Beilinson conjectures implicitly assume that $L(H^i(X), s)$ possesses a meromorphic continuation to the entire complex plane. For general varieties, this continuation itself is unproven and constitutes a massive open problem (related to the Langlands program).

## 6. The Gap

The exact boundary between verified cases and the general statement is the reliance on **modularity**. Almost all known cases of the Beilinson conjectures rely on the fact that the variety in question is governed by modular forms, automorphic representations, or symmetric spaces. This allows mathematicians to construct the required $K$-theoretic elements (so-called "Beilinson-Flach elements" or "Euler systems") explicitly using the geometry of modular curves or Shimura varieties. For a general smooth projective variety (e.g., a generic Calabi-Yau threefold or a high-degree hypersurface), we completely lack the geometric machinery to explicitly construct the required higher $K$-theory classes.

## 7. Current Research (as of June 2026)

Active research directions currently focus on:

- **$p$-adic Analogues:** Formulations of the $p$-adic Beilinson conjectures (using $p$-adic L-functions and syntomic or $p$-adic regulators) are highly active. Researchers like Colmez, Besser, and Nekovář have laid frameworks, and recent constructions of Euler systems via the Gan-Gross-Prasad conjectures provide new pathways.
- **Bloch-Kato Conjectures (Tamagawa Number Conjecture):** Beilinson’s conjectures predict the exact value of the L-function up to a rational number. The Bloch-Kato Tamagawa Number conjecture goes further, predicting the exact arithmetic significance of that rational factor (in terms of Tate-Shafarevich groups and Galois cohomology). 
- **Polylogarithmic Motivic Complexes:** Goncharov's program attempts to build explicit complexes of higher polylogarithms to compute the real regulators of mixed Tate motives, making the abstract K-theory geometrically tangible.
- *(frontier — verify)*: New results applying relative trace formulas to construct Euler systems for higher-rank Shimura varieties, verifying $p$-adic Beilinson conjectures for certain unitary groups.

## 8. Future Work

Leading experts suggest a few key strategies for the future:
1. **Higher Euler Systems:** Developing a robust, unified theory for constructing Euler systems for arbitrary Galois representations beyond those appearing in $\text{GL}(2)$ or $\text{GL}(2) \times \text{GL}(2)$.
2. **Zagier's Conjecture:** Proving Zagier’s polylogarithm conjecture, which gives a concrete model for the algebraic $K$-theory of fields in terms of higher polylogarithms, would vastly simplify the computation of regulators for number fields and their arithmetic schemes.
3. **Motivic Cohomology Formalism:** Resolving the standard conjectures on motives to unconditionally establish the exact sequences and spectral sequences of motivic cohomology that are currently often assumed via Voevodsky’s triangulated categories.

## 9. Key References

- **[Foundational]** Beilinson, A. A. *Higher regulators and values of L-functions*. Current Problems in Mathematics, Vol. 24, 181–238, Itogi Nauki i Tekhniki, Akad. Nauk SSSR, Moscow, 1984.
- **[Foundational]** Bloch, S. *Higher regulators, algebraic $K$-theory, and zeta functions of elliptic curves*. CRM Monograph Series, Vol. 11, American Mathematical Society, 2000.
- **[Survey]** Rapoport, M., Schappacher, N., Schneider, P. (Eds.). *Beilinson's Conjectures on Special Values of L-Functions*. Perspectives in Mathematics, Vol. 4, Academic Press, 1988.
- **[SOTA / Recent]** Goncharov, A. B. *Multiple polylogarithms and mixed Tate motives*. Annals of Mathematics, 154(2), 397-440, 2001.
- **[SOTA / Recent]** Kings, G. *The Tamagawa number conjecture for CM elliptic curves*. Inventiones Mathematicae, 139, 103-142, 1999.

## 10. Worked Example / Concrete Special Case

Consider the simplest non-trivial setting that goes beyond Dirichlet's class number formula: the value of the Dedekind zeta function $\zeta_F(2)$ for an imaginary quadratic field $F = \mathbb{Q}(\sqrt{-d})$.

For $s=2$, Beilinson's conjecture relates $\zeta_F(2)$ to the regulator on the K-group $K_3(F)$.
By Borel's rank theorem, for a number field $F$ with $r_1$ real embeddings and $r_2$ complex conjugate pairs of embeddings, the dimension of $K_{2m-1}(F) \otimes \mathbb{Q}$ is $r_2$ if $m$ is even, and $r_1 + r_2$ if $m$ is odd.
For $m=2$, the rank is $r_2$. For an imaginary quadratic field, $r_1 = 0$ and $r_2 = 1$. Thus, $K_3(F) \otimes \mathbb{Q}$ is a 1-dimensional $\mathbb{Q}$-vector space.

The Beilinson regulator in this dimension reduces to a map evaluated via the **Bloch-Wigner dilogarithm** $D(z)$, defined as:
$$ D(z) = \text{Im}(\text{Li}_2(z)) + \arg(1-z)\log|z| $$
where $\text{Li}_2(z) = \sum_{n=1}^\infty \frac{z^n}{n^2}$ is the classical dilogarithm.

Bloch explicitly showed that one can construct a generator of $K_3(F) \otimes \mathbb{Q}$ using the algebraic geometry of $F$. Specifically, for $F = \mathbb{Q}(\sqrt{-3})$, let $\omega = e^{2\pi i/6}$ be a root of unity in $F$. 
The regulator $r_{\mathcal{D}}$ applied to a specifically constructed algebraic symbol in $K_3(\mathbb{Q}(\sqrt{-3}))$ involving $\omega$ yields a value proportional to $D(\omega)$.

The analytic side yields:
$$ \zeta_{\mathbb{Q}(\sqrt{-3})}(2) = \frac{\pi^2}{3\sqrt{3}} D(e^{2\pi i/6}) $$

Here, $\zeta_F(2)$ is exactly expressed as a determinant (a $1 \times 1$ determinant, hence just the value) of the regulator map applied to a basis of $K_3(F)$, up to a rational factor. This establishes a perfect concrete instance of Beilinson's abstract framework.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*