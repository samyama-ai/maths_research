---
id: 05-analysis/invariant-subspace-problem
title: "Invariant Subspace Problem"
topic: 05-analysis
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Invariant Subspace Problem

> **Topic:** Real & Complex Analysis · **ID:** `05-analysis/invariant-subspace-problem` · **Status:** open

## 1. Problem Statement / Conjecture

Let $H$ be a separable, infinite-dimensional complex Hilbert space and let $T \in \mathcal{B}(H)$ be a bounded linear operator. A closed subspace $M \subseteq H$ is **invariant** for $T$ if $T M \subseteq M$; it is **trivial** if $M = \{0\}$ or $M = H$.

> **Invariant Subspace Problem (ISP).** Does every $T \in \mathcal{B}(H)$ admit a nontrivial closed invariant subspace?

A positive resolution requires a proof valid for all $T$; a negative resolution requires exhibiting a single $T \in \mathcal{B}(H)$ for which every nonzero vector $x$ is **cyclic**, i.e.
$$\overline{\operatorname{span}}\{x, Tx, T^2x, \dots\} = H \qquad \text{for all } x \neq 0 .$$

Three conventions matter. (i) *Closed* is essential: every operator has non-closed invariant linear manifolds. (ii) *Separable* is essential: if $H$ is non-separable, $\overline{\operatorname{span}}\{T^n x\}_{n \ge 0}$ is a separable, hence proper, invariant subspace. (iii) *Complex* is essential: on real $\mathbb{R}^2$ a rotation by $\pi/2$ has no invariant line, so the finite-dimensional statement already fails over $\mathbb{R}$.

The Banach-space version — "does every operator on every infinite-dimensional separable Banach space have a nontrivial closed invariant subspace?" — is **false** (Enflo, Read). The Hilbert-space case is open.

## 2. Mathematical Foundations

**Setting.** $\mathcal{B}(H)$ is the C\*-algebra of bounded operators with operator norm $\|T\| = \sup_{\|x\|=1}\|Tx\|$. The spectrum is
$$\sigma(T) = \{\lambda \in \mathbb{C} : T - \lambda I \text{ is not invertible}\},$$
a nonempty compact set with spectral radius $r(T) = \lim_n \|T^n\|^{1/n} = \max\{|\lambda| : \lambda \in \sigma(T)\}$.

**Reduction to cyclic operators.** For $x \neq 0$ put $K_x = \overline{\operatorname{span}}\{T^n x : n \ge 0\}$. Then $T K_x \subseteq K_x$, so a counterexample must have $K_x = H$ for every $x \neq 0$. Equivalently, ISP asks whether every $T$ has a non-cyclic nonzero vector.

**Spectral reductions.** If $\sigma(T)$ is disconnected, the Riesz idempotent
$$P = \frac{1}{2\pi i}\oint_{\Gamma} (\lambda I - T)^{-1}\, d\lambda$$
for $\Gamma$ separating $\sigma(T)$ gives a nontrivial invariant range $PH$. If $T$ has an eigenvalue, its eigenspace is invariant. If $T$ is not injective or not surjective, $\ker T$ or $\overline{\operatorname{ran}} T$ works. Hence a counterexample $T$ may be assumed to have connected spectrum, no eigenvalues, and to be injective with dense range; after scaling and translation one may take $\sigma(T)$ to be a connected compact set, and the hardest model case is $\sigma(T) = \{0\}$ (**quasinilpotent**: $\|T^n\|^{1/n}\to 0$).

**Hyperinvariance.** $M$ is *hyperinvariant* for $T$ if $SM\subseteq M$ for every $S$ in the commutant $\{T\}' = \{S : ST = TS\}$. Hyperinvariant subspaces are invariant; several classical theorems produce the stronger version.

**Normality and the spectral theorem.** $T$ is normal if $T^*T = TT^*$; then $T = \int_{\sigma(T)} \lambda \, dE(\lambda)$ for a projection-valued measure $E$, and $E(\omega)H$ is invariant (indeed reducing) for any Borel $\omega$ with $0 \neq E(\omega) \neq I$. $T$ is **subnormal** if it is the restriction of a normal operator to an invariant subspace, and **hyponormal** if $T^*T \ge TT^*$; subnormal $\Rightarrow$ hyponormal.

**Model theory.** For a completely non-unitary contraction ($\|T\|\le 1$), the Sz.-Nagy–Foiaş functional calculus $f \mapsto f(T)$, $f \in H^\infty(\mathbb{D})$, is contractive, and the ranges of $f(T)$ are invariant. Beurling's theorem describes all invariant subspaces of the unilateral shift $S$ on $H^2(\mathbb{D})$: they are exactly $\theta H^2$ with $\theta$ inner ($|\theta| = 1$ a.e. on $\partial\mathbb{D}$).

## 3. History & State of the Art (SOTA)

- **1930s–40s.** Von Neumann proves (unpublished) that a compact operator on Hilbert space has a nontrivial invariant subspace. Beurling (1949) classifies the shift's lattice.
- **1954.** Aronszajn and Smith publish the compact case for Banach spaces.
- **1966.** Bernstein and Robinson, using nonstandard analysis, settle Halmos's question: $T$ with $p(T)$ compact for some nonzero polynomial $p$ has an invariant subspace. Halmos immediately gives a standard translation.
- **1973.** Lomonosov's theorem: if $T$ commutes with a nonzero compact operator $K$ and $T \neq \lambda I$, then $T$ has a nontrivial *hyperinvariant* subspace. The Hilden–Michaels proof (1977) reduces it to Schauder's fixed-point theorem. This subsumed nearly all prior results and briefly raised hopes that every operator commutes with a compact one — refuted by Hadwin, Nordgren, Radjavi and Rosenthal (1980).
- **1975–87.** Enflo constructs a Banach space and an operator on it with no nontrivial closed invariant subspace (announced 1975/76; published in *Acta Mathematica* 1987 after long refereeing).
- **1984–85.** Read gives an independent, more elementary counterexample, then one on the classical space $\ell^1$.
- **1978–88.** Scott Brown's dual-algebra technique settles subnormal operators (1978) and, with Chevreau and Pearcy, contractions whose spectrum contains the unit circle (1988).
- **1997.** Read produces a *quasinilpotent* operator on a Banach space with no invariant subspace, killing the hope that small spectrum forces invariant subspaces.
- **2011.** Argyros and Haydon build a Banach space $X_{AH}$ on which every operator is $\lambda I + \text{compact}$; by Lomonosov every operator on $X_{AH}$ has a nontrivial invariant subspace.
- **2023–present.** Enflo posts a preprint claiming a positive solution on Hilbert space. It has not been accepted by the community. *(frontier — verify)*

## 4. Partial Results / Verified Cases

Classes for which a nontrivial invariant subspace is known to exist:

| Class | Result |
|---|---|
| $\dim H = n < \infty$, $n \ge 2$, over $\mathbb{C}$ | Eigenvector exists (fundamental theorem of algebra) |
| Non-separable $H$ | Cyclic subspace of any $x\ne0$ is separable, hence proper |
| Compact $T$ | Von Neumann; Aronszajn–Smith (1954) |
| $p(T)$ compact, $p \ne 0$ polynomial | Bernstein–Robinson (1966) |
| $T$ commutes with nonzero compact, $T \ne \lambda I$ | Lomonosov (1973); hyperinvariant |
| Normal, self-adjoint, unitary | Spectral theorem |
| Subnormal | S. Brown (1978) |
| Hyponormal with $\sigma(T)$ of nonempty interior, and other "thick spectrum" cases | Brown-technique refinements |
| Contractions with $\partial\mathbb{D}\subseteq\sigma(T)$ | Brown–Chevreau–Pearcy (1988) |
| $\sigma(T)$ disconnected; $T$ non-injective or non-surjective; $T$ has an eigenvalue | Riesz functional calculus |
| Certain positive operators on $\ell^p$, $1\le p<\infty$, and on Banach lattices | Abramovich–Aliprantis–Burkinshaw (1993 onward) |
| Every operator on the Argyros–Haydon space | Argyros–Haydon (2011) + Lomonosov |
| Polynomially bounded / algebraic / normaloid-with-structure special families | Various |

Negative results (Banach setting): counterexamples exist on Enflo's constructed space, on $\ell^1$ (Read 1985), on $c_0$, and among quasinilpotent operators (Read 1997). No counterexample is known on any **reflexive** Banach space; that case is open too and is regarded as intermediate in difficulty.

## 5. Principal Obstacles

- **No decomposition principle.** Read's counterexamples show the statement is *not* a soft consequence of Banach-space geometry, functional calculus or spectral smallness. Any positive proof must use a Hilbert-space-specific ingredient (inner product, unitary dilation, $C^*$-structure) that the counterexamples violate.
- **Failure of the compactness lever.** Lomonosov's theorem is the strongest general tool, but Hadwin–Nordgren–Radjavi–Rosenthal exhibited operators commuting with no nonzero compact operator, so the whole Schauder-fixed-point route is bounded away from the general case.
- **The quasinilpotent wall.** For $\sigma(T)=\{0\}$ every holomorphic functional calculus collapses: $f(T)$ depends only on the germ at $0$, Riesz idempotents are trivial, and $H^\infty$-calculus arguments have nothing to grip. Read's 1997 quasinilpotent counterexample proves the wall is real in Banach spaces.
- **Scott Brown technique needs spectral bulk.** Dual-algebra methods solve $\langle f, x\otimes y\rangle$-type factorization problems in $L^1/H^1_0$; they require the spectrum to carry enough of $\partial\mathbb{D}$ or planar area. Operators with thin spectrum are exactly the untouched ones.
- **Genericity of the hard case.** Reductions leave a residual class — injective, dense-range, no eigenvalues, connected thin spectrum, not commuting with any compact — for which no structural model theory exists.
- **Construction side is equally blocked.** Read-type constructions build the operator on a space designed with a basis adapted to the orbit combinatorics; the rigidity of the Hilbert norm (all orthonormal bases are unitarily equivalent, $\|\cdot\|$ is unconditional and Euclidean) obstructs transplanting the argument to $\ell^2$.

## 6. The Gap

Everything proven is of the form: *if $T$ carries extra structure — compactness, normality-like positivity, a rich spectrum, an $H^\infty$ calculus, or a compact operator in its commutant — then an invariant subspace exists.* The general statement claims the conclusion with **no** hypothesis beyond boundedness.

The precise gap is a single residual class:
$$\mathcal{R} = \{T \in \mathcal{B}(H) : T \text{ injective, dense range, } \sigma_p(T)=\sigma_p(T^*)=\emptyset,\ \sigma(T) \text{ connected and thin},\ \{T\}' \cap \mathcal{K}(H) = \{0\}\},$$
with the quasinilpotent subfamily $\sigma(T)=\{0\}$ as its hard core. Crossing the gap means either (a) producing a Hilbert-space mechanism that manufactures a non-cyclic vector from boundedness alone — no such mechanism is known, and it must fail on $\ell^1$ — or (b) porting a Read-type orbit construction into $\ell^2$, which requires simultaneously controlling $\|T^n\|$ and the mutual angles of orbit vectors under a Euclidean norm.

## 7. Current Research (as of June 2026)

- **Enflo's 2023 preprint** *On the invariant subspace problem in Hilbert spaces* (arXiv:2305.15442) claims every bounded operator on a separable Hilbert space has a nontrivial closed invariant subspace, via a minimal-vector / approximation argument. It remains unrefereed and unverified by the community; specialists have not endorsed it. *(frontier — verify)*
- **Minimal / extremal vectors.** Ansari–Enflo (1998) introduced backward minimal vectors; Chalendar, Partington and collaborators (Lyon, Leeds) continue to develop them as a constructive route to invariant subspaces for classes of operators.
- **Read-type machinery.** Grivaux and Roginskaya gave a unified framework for Read's constructions (*Proc. LMS*, 2013), clarifying exactly which Banach-space features they consume — a template for testing what fails in $\ell^2$.
- **Hyperinvariant subspaces and free probability.** Haagerup–Schultz subspaces for operators in a $\mathrm{II}_1$ factor give invariant subspaces for every operator affiliated to a finite von Neumann algebra with non-degenerate Brown measure — a positive answer in a tracial, non-$\mathcal{B}(H)$ setting.
- **Reflexive Banach spaces.** Whether a counterexample exists on a reflexive space (e.g. $\ell^p$, $1<p<\infty$) is actively pursued and widely considered strictly easier than the Hilbert case.
- **Composition and Toeplitz operators.** Concrete classes on $H^2(\mathbb{D})$ (composition operators, Toeplitz operators with continuous symbol) continue to yield complete lattice descriptions, feeding intuition.

## 8. Future Work

- Settle the reflexive Banach case; a counterexample on $\ell^p$ would strongly suggest a Hilbert counterexample, and a positive proof would isolate what reflexivity buys.
- Determine whether every quasinilpotent operator on $\ell^2$ has an invariant subspace — the recognized crux.
- Extend Scott Brown/dual-algebra methods below the current spectral thickness threshold, e.g. to hyponormal operators with spectrum of empty interior.
- Push the Haagerup–Schultz tracial results toward $\mathcal{B}(H)$, or prove a formal obstruction to doing so.
- Adjudicate Enflo's 2023 argument: independent verification or a located error would itself be a substantive contribution.

## 9. Key References

- **[Foundational]** Beurling, A. *On two problems concerning linear transformations in Hilbert space.* Acta Mathematica 81 (1949), 239–255. [DOI](https://doi.org/10.1007/bf02395019)
- **[Foundational]** Aronszajn, N., Smith, K. T. *Invariant subspaces of completely continuous operators.* Annals of Mathematics 60 (1954), 345–350. [DOI](https://doi.org/10.2307/1969637)
- **[Foundational]** Bernstein, A. R., Robinson, A. *Solution of an invariant subspace problem of K. T. Smith and P. R. Halmos.* Pacific Journal of Mathematics 16 (1966), 421–431. [DOI](https://doi.org/10.2140/pjm.1966.16.421)
- **[Foundational]** Lomonosov, V. I. *Invariant subspaces of the family of operators that commute with a completely continuous operator.* Funktsional. Analiz i Prilozhen. 7 (1973), 55–56.
- **[Foundational]** Michaels, A. J. *Hilden's simple proof of Lomonosov's invariant subspace theorem.* Advances in Mathematics 25 (1977), 56–58. [DOI](https://doi.org/10.1016/0001-8708(77)90089-5)
- **[Foundational]** Brown, S. W. *Some invariant subspaces for subnormal operators.* Integral Equations and Operator Theory 1 (1978), 310–333. [DOI](https://doi.org/10.1007/bf01682842)
- **[Counterexample]** Enflo, P. *On the invariant subspace problem for Banach spaces.* Acta Mathematica 158 (1987), 213–313. [DOI](https://doi.org/10.1007/bf02392260)
- **[Counterexample]** Read, C. J. *A solution to the invariant subspace problem.* Bulletin of the London Mathematical Society 16 (1984), 337–401.
- **[Counterexample]** Read, C. J. *A solution to the invariant subspace problem on the space $l_1$.* Bulletin of the London Mathematical Society 17 (1985), 305–317. [DOI](https://doi.org/10.1112/blms/17.4.305)
- **[Counterexample]** Read, C. J. *Quasinilpotent operators and the invariant subspace problem.* Journal of the London Mathematical Society 56 (1997), 595–606. [DOI](https://doi.org/10.1112/s0024610797005486)
- **[SOTA]** Brown, S., Chevreau, B., Pearcy, C. *On the structure of contraction operators. I.* Journal of Functional Analysis 76 (1988), 30–55. [DOI](https://doi.org/10.1016/0022-1236(88)90046-8)
- **[SOTA]** Argyros, S. A., Haydon, R. G. *A hereditarily indecomposable $\mathcal{L}_\infty$-space that solves the scalar-plus-compact problem.* Acta Mathematica 206 (2011), 1–54. [DOI](https://doi.org/10.1007/s11511-011-0058-y)
- **[SOTA]** Ansari, S., Enflo, P. *Extremal vectors and invariant subspaces.* Transactions of the American Mathematical Society 350 (1998), 539–558. [DOI](https://doi.org/10.1090/s0002-9947-98-01865-0)
- **[SOTA]** Grivaux, S., Roginskaya, M. *A general approach to Read's type constructions of operators without non-trivial invariant subspaces.* Proceedings of the London Mathematical Society 109 (2014), 596–652. [DOI](https://doi.org/10.1112/plms/pdu012)
- **[Survey / Book]** Radjavi, H., Rosenthal, P. *Invariant Subspaces.* Springer-Verlag, 1973; 2nd ed. Dover, 2003.
- **[Survey / Book]** Beauzamy, B. *Introduction to Operator Theory and Invariant Subspaces.* North-Holland, 1988. [DOI](https://doi.org/10.1016/s0924-6509(08)x7031-x)
- **[Survey / Book]** Chalendar, I., Partington, J. R. *Modern Approaches to the Invariant-Subspace Problem.* Cambridge University Press, 2011.
- **[Frontier — verify]** Enflo, P. *On the invariant subspace problem in Hilbert spaces.* arXiv:2305.15442 (2023). Unrefereed.

## 10. Worked Example / Concrete Special Case

**The unilateral shift on $H^2(\mathbb{D})$.** Identify $\ell^2(\mathbb{N}_0)$ with the Hardy space $H^2 = \{f(z)=\sum_{n\ge0} a_n z^n : \sum |a_n|^2 < \infty\}$, and let
$$S: (a_0,a_1,a_2,\dots) \mapsto (0,a_0,a_1,\dots), \qquad (Sf)(z) = z f(z).$$

*Step 1 — spectrum.* $\|S\|=1$ and $S$ is an isometry, so $\sigma(S)\subseteq \overline{\mathbb{D}}$. For $|\lambda|<1$ the vector $k_\lambda(z)=(1-\bar\lambda z)^{-1}$ satisfies $S^*k_\lambda = \bar\lambda k_\lambda$, so $\overline{\mathbb{D}}\subseteq\sigma(S)$ and $\sigma(S)=\overline{\mathbb{D}}$, connected with nonempty interior. $S$ itself has **no** eigenvalues: $zf(z)=\lambda f(z)$ forces $f\equiv 0$.

*Step 2 — an invariant subspace by hand.* $M_1 = zH^2 = \{f : f(0)=0\} = \overline{\operatorname{span}}\{S^n e_0 : n\ge 1\}$ is closed, $S M_1 \subseteq M_1$, and $M_1 \ne \{0\}, H^2$ since $1 \notin M_1$. So $e_0$ is not cyclic for... in fact $e_0$ *is* cyclic; the non-cyclic vector is $e_1 = z$, whose orbit closure is $M_1$.

*Step 3 — the full lattice (Beurling).* Every nonzero closed $M$ with $SM\subseteq M$ is $M = \theta H^2$ for an inner function $\theta$, unique up to unimodular constant. Proof sketch: $M \ominus zM$ is one-dimensional (else two orthogonal $\theta_1,\theta_2$ would give $\int_{\partial\mathbb D} \theta_1\overline{\theta_2}\, z^n\,dm = 0$ for all $n\in\mathbb{Z}$, forcing $\theta_1\overline{\theta_2}=0$); pick a unit $\theta$ spanning it. Then $\{z^n\theta\}$ is orthonormal, $|\theta|^2$ has all nonzero Fourier coefficients vanishing, hence $|\theta|=1$ a.e. on $\partial\mathbb{D}$, and $M=\theta H^2$.

*Step 4 — concrete instance.* Take $\theta(z) = \dfrac{z-1/2}{1-z/2}$, a Blaschke factor. Then
$$\theta H^2 = \{f \in H^2 : f(1/2) = 0\},$$
a codimension-one invariant subspace: it is the orthogonal complement of the reproducing kernel $k_{1/2}(z) = (1-z/2)^{-1}$, and $\langle zf, k_{1/2}\rangle = \tfrac12 f(1/2) = 0$ for $f \in \theta H^2$, confirming invariance.

*Why this does not solve ISP.* $S$ is a subnormal isometry with $\sigma(S)=\overline{\mathbb{D}}$ — the spectrum is as thick as possible, and the $H^\infty(\mathbb D)$ functional calculus $f\mapsto f(S)$ is isometric, so ranges $\overline{f(S)H^2}$ manufacture invariant subspaces for free. Every tool used above (inner functions, reproducing kernels, boundary values) is a consequence of that spectral richness. Strip it away — take $T$ quasinilpotent, $\sigma(T)=\{0\}$, with no compact operator in its commutant — and each of Steps 1–4 evaporates: there are no eigenvalues of $T^*$ to build kernels from, the functional calculus is trivial, and no analogue of Beurling's theorem is known. That residual class is exactly the open problem.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*