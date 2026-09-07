---
id: 05-analysis/halmos-invariant-subspace
title: "Halmos Invariant Subspace"
topic: 05-analysis
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Halmos Invariant Subspace Problem

> **Topic:** Real & Complex Analysis · **ID:** `05-analysis/halmos-invariant-subspace` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Let $H$ be a separable infinite-dimensional complex Hilbert space and let $T \in \mathcal{B}(H)$ be a bounded linear operator.

**Problem.** Does every such $T$ admit a closed subspace $M \subseteq H$ with $M \neq \{0\}$, $M \neq H$, and $T(M) \subseteq M$?

The qualifiers are essential:

- **Closed.** Every non-scalar operator has a non-trivial invariant *linear manifold* (take the span of the orbit of a single vector); the question is whether one can be closed.
- **Separable and infinite-dimensional.** In finite dimension $\ge 2$ over $\mathbb{C}$, eigenvectors give invariant lines. In a non-separable space, the closed span $\overline{\operatorname{span}}\{x, Tx, T^2x, \dots\}$ of a single orbit is separable, hence proper and invariant.
- **Complex scalars.** Over $\mathbb{R}$, rotation by $\pi/2$ in $\mathbb{R}^2$ already fails; the Hilbert-space question is normally posed over $\mathbb{C}$.

A resolution is either (a) a proof that every $T \in \mathcal{B}(H)$ has such an $M$, or (b) an explicit or existential construction of a *transitive* operator — one for which $\overline{\operatorname{span}}\{T^n x : n \ge 0\} = H$ for every $x \neq 0$. The Banach-space version is **solved negatively** (Enflo, Read); the Hilbert-space version is the open case, popularized as Problem 3 in Halmos's "Ten problems in Hilbert space" (1970).

## 2. Mathematical Foundations

**Lattice of invariant subspaces.** For $T \in \mathcal{B}(H)$ put
$$\operatorname{Lat}(T) = \{ M \subseteq H \text{ closed subspace} : TM \subseteq M \}.$$
$\operatorname{Lat}(T)$ is a complete lattice under $\wedge = \cap$, $\vee = \overline{\text{span}}$, always containing $\{0\}$ and $H$. The problem asks whether $|\operatorname{Lat}(T)| \ge 3$ always.

**Cyclic vectors.** $x \in H$ is cyclic for $T$ if
$$M_x := \overline{\operatorname{span}}\{ p(T)x : p \in \mathbb{C}[z] \} = H.$$
Since $M_x \in \operatorname{Lat}(T)$, $T$ is a counterexample iff **every** nonzero $x$ is cyclic. Thus counterexamples are exactly the operators for which the orbit map $x \mapsto \{T^nx\}$ is maximally spreading.

**Hyperinvariant subspaces.** $M$ is hyperinvariant if $SM \subseteq M$ for every $S$ in the commutant $\{T\}' = \{S : ST = TS\}$. Hyperinvariance is strictly stronger; most positive results produce hyperinvariant subspaces.

**Spectral reductions.** Let $\sigma(T)$ be the spectrum. If $\sigma(T)$ is disconnected, the Riesz idempotent
$$P_\Gamma = \frac{1}{2\pi i}\oint_\Gamma (\lambda I - T)^{-1}\, d\lambda$$
for a contour $\Gamma$ separating $\sigma(T)$ is a nontrivial projection commuting with $T$, so $\operatorname{ran} P_\Gamma$ is hyperinvariant. Hence one may assume $\sigma(T)$ is connected; further, if $\sigma_p(T) \neq \emptyset$ eigenvectors suffice, and if $T$ is not injective or has non-dense range those give invariant subspaces. So a putative counterexample satisfies: $T$ injective, dense range, $\sigma(T)$ connected, no eigenvalues, and (after scaling/translating) one may take $\sigma(T) = \overline{\mathbb{D}}$ or a quasinilpotent normalization.

**Model operator.** By Beurling's theorem the unilateral shift $S$ on the Hardy space
$$H^2(\mathbb{D}) = \Big\{ f = \sum_{n\ge0} a_n z^n : \|f\|^2 = \sum |a_n|^2 < \infty \Big\}, \qquad (Sf)(z) = z f(z),$$
has $\operatorname{Lat}(S) = \{\theta H^2 : \theta \text{ inner}\}$, where $\theta$ inner means $\theta \in H^\infty$, $|\theta^*| = 1$ a.e. on $\mathbb{T}$. Sz.-Nagy–Foiaş theory represents every completely non-unitary contraction as a compression of a shift to $H(\Theta) = H^2 \ominus \Theta H^2$, so the problem localizes to functional models.

**Key positive theorem (Lomonosov, 1973).** If $T \in \mathcal{B}(H)$ is non-scalar and commutes with a nonzero compact operator $K$, then $T$ has a nontrivial hyperinvariant subspace. Proof (Hilden's argument) uses Schauder's fixed point theorem applied to $x \mapsto$ suitable $A_i K x$ on a ball not containing $0$.

## 3. History & State of the Art (SOTA)

- **1935.** von Neumann proves (unpublished) that compact operators on Hilbert space have nontrivial invariant subspaces.
- **1949.** Beurling classifies $\operatorname{Lat}(S)$ for the shift — the first complete lattice computation.
- **1954.** Aronszajn and Smith publish the compact case for Banach spaces (*Ann. of Math.*).
- **1966.** Bernstein and Robinson, using nonstandard analysis, prove the polynomially compact case ($p(T)$ compact for some nonzero polynomial $p$); Halmos immediately gives a standard-analysis translation in the same issue of *Pacific J. Math.*
- **1970.** Halmos lists the problem as Problem 3 of "Ten problems in Hilbert space" (*Bull. AMS*), fixing it as a central open question.
- **1973.** Lomonosov's theorem: commuting with a nonzero compact operator suffices. This subsumed nearly all prior results and briefly raised hope of a general proof — until Hadwin, Nordgren, Radjavi and Rosenthal (1980) produced an operator not satisfying Lomonosov's hypothesis.
- **1978.** S. Brown: every subnormal operator has a nontrivial invariant subspace, via a dual-algebra / analytic-functional technique.
- **1984–1988.** Enflo (circulated 1975/1981, published *Acta Math.* 1987) and Read (*Bull. LMS* 1984) construct operators on Banach spaces with no nontrivial closed invariant subspace; Read (1985) does it on $\ell^1$, and (1997) exhibits a **quasinilpotent** such operator on $\ell^1$.
- **1988.** Brown, Chevreau and Pearcy: every contraction whose spectrum contains the unit circle has a nontrivial invariant subspace.
- **2011.** Argyros and Haydon construct a Banach space on which *every* operator is scalar-plus-compact, hence every operator has an invariant subspace — showing the Banach answer depends heavily on the space.
- **2023–2026.** Enflo posts a claimed positive solution for separable Hilbert space (arXiv:2305.15442); as of this review it is not accepted by the community as verified. *(frontier — verify)*

## 4. Partial Results / Verified Cases

Nontrivial invariant subspaces are **known to exist** for:

1. $\dim H < \infty$, $\dim H \ge 2$, complex scalars (eigenvectors).
2. Normal operators, and more generally any $T$ with $\sigma(T)$ disconnected or $\sigma_p(T) \neq \emptyset$ (spectral projections).
3. Compact operators (von Neumann 1935; Aronszajn–Smith 1954) and polynomially compact operators (Bernstein–Robinson 1966).
4. Any non-scalar $T$ commuting with a nonzero compact operator (Lomonosov 1973) — this covers all $T$ with $\{T\}' \cap \mathcal{K}(H) \neq \{0\}$.
5. Subnormal operators (S. Brown 1978) and hyponormal operators with "thick" spectrum (Brown 1987).
6. Contractions $\|T\| \le 1$ with $\sigma(T) \supseteq \mathbb{T}$ (Brown–Chevreau–Pearcy 1988), and $C_{00}$-contractions of class $A_{\aleph_0}$.
7. Operators with a nontrivial "quasi-triangular"/Bishop-property functional calculus; operators $T$ with $T$ or $T^*$ decomposable, and $2$-isometries.
8. Every $T$ on the Argyros–Haydon Banach space $X_{AH}$ (2011).
9. Positive/quasi-nilpotent-dominated operators on $L^p$ lattices, via Abramovich–Aliprantis–Burkinshaw positivity results.

Counterexamples exist on Banach spaces: Enflo's space (1987), $\ell^1$ (Read 1985), a quasinilpotent operator on $\ell^1$ (Read 1997), and $c_0$. No counterexample is known on any reflexive Banach space, in particular none on $\ell^2$.

## 5. Principal Obstacles

- **Lomonosov barrier.** Compactness-driven fixed-point arguments require a nonzero compact operator in the commutant. The commutant of a hypothetical counterexample contains only operators with no compact part, so Schauder-type arguments have nothing to compress with. Hadwin–Nordgren–Radjavi–Rosenthal (1980) showed the hypothesis genuinely restricts.
- **Read's constructions are not Hilbertian.** They rely on carefully tuned basis-dependent norms with wildly non-Euclidean geometry (long "quasi-nilpotent" blocks with controlled overlaps). The parallelogram law forces uniform two-dimensional rigidity, and every attempt to port Read's inductive weight scheme to $\ell^2$ has broken down when orthogonality forces the block norms to grow.
- **No classification of $\mathcal{B}(H)$.** Positive results are class-by-class (normal, subnormal, contraction with fat spectrum). There is no structure theorem covering the residual class: injective, dense range, connected spectrum, no eigenvalues, non-quasitriangular in neither $T$ nor $T^*$.
- **Dual-algebra methods stall on thin spectrum.** Brown-type methods solve $\langle f, \cdot\rangle$-moment problems in $L^1/H^1_0$; they need enough of $\sigma(T)$ to touch $\mathbb{T}$ or enough analytic structure. When $\sigma(T) = \{0\}$ (quasinilpotent), the functional calculus degenerates and the predual $Q_T$ carries no information.
- **Quasinilpotent case is the hardest.** Read's 1997 counterexample is quasinilpotent, so any Hilbert-space proof must succeed exactly where the Banach case fails — it cannot be a soft argument that ignores geometry.

## 6. The Gap

Everything proven in §4 attaches to some *extra structure*: a compact operator in the commutant, a normality-type relation between $T$ and $T^*$, or spectrum large enough to run a functional calculus. The open residue is the set
$$\mathcal{R} = \{T \in \mathcal{B}(\ell^2) : \{T\}' \cap \mathcal{K} = \{0\},\ \sigma(T) \text{ connected},\ \sigma_p(T) = \sigma_p(T^*) = \emptyset\},$$
of which the quasinilpotent stratum $\sigma(T) = \{0\}$ is the sharpest instance. The required step is one of:

1. a uniform mechanism producing a non-cyclic vector for every $T \in \mathcal{R}$ — e.g. a quantitative lower bound showing $\inf_{p} \|p(T)x - y\|$ cannot vanish for all $y$; or
2. an $\ell^2$-realizable analogue of Read's inductive construction, which requires controlling orthogonality losses that Read's $\ell^1$ estimates absorb into the norm.

Equivalently: does Hilbert-space geometry (parallelogram law, unconditionality of orthogonal decompositions) *by itself* prevent transitivity? Nobody has isolated a Hilbert-specific invariant that Read's construction must violate.

## 7. Current Research (as of June 2026)

- **Enflo's claimed proof** (arXiv:2305.15442, 2023) asserts every bounded operator on a separable Hilbert space has a nontrivial closed invariant subspace, via approximation of "minimal vectors" for cyclic orbits. Independent verification is still incomplete; the community has not accepted it. *(frontier — verify)*
- **Neville–Tao style adversarial reading** of the above and of related preprints; several expositions and seminar notes (Lyon, Leeds, Lund) have produced partial rewrites without confirming the key convergence step. *(frontier — verify)*
- **Minimal-vector methods** (Ansari–Enflo 1998; Androulakis, Chalendar, Partington) give constructive proofs of the compact and quasinilpotent-dominated cases without Schauder's theorem, and remain the main constructive engine.
- **Functional models and de Branges–Rovnyak spaces**: groups at Laval, Leeds and Lille study $\operatorname{Lat}$ of compressed shifts $S_\Theta$ and truncated Toeplitz operators.
- **Positivity/lattice methods** on $L^p$ (Abramovich–Aliprantis–Burkinshaw programme) continue to widen the class of positive operators with invariant closed ideals.
- **Read-style constructions in reflexive spaces**: the standing question of whether any reflexive Banach space carries a transitive operator remains open and is treated as a strict weakening of the Hilbert problem.

## 8. Future Work

- Settle the **reflexive** case first: constructing a transitive operator on some reflexive $X$ would show reflexivity is not the obstruction and sharply focus attention on Hilbert geometry.
- Push minimal-vector estimates: quantify $\operatorname{dist}(y, \overline{\{p(T)x\}})$ against $\|T^n\|^{1/n}$ to see whether quasinilpotency forces non-cyclicity in $\ell^2$.
- Decide whether every **quasinilpotent** operator on $\ell^2$ has a nontrivial invariant subspace — Read's 1997 example makes this the decisive test case.
- Extend Brown-type dual-algebra techniques to operators with $\sigma(T)$ of empty interior, currently outside the reach of the $A_{\aleph_0}$ machinery.
- Use $C^*$/von Neumann algebra invariants (Voiculescu's quasidiagonality, Brown–Douglas–Fillmore $\mathrm{Ext}$) to detect obstructions to transitivity.

## 9. Key References

- **[Foundational]** A. Beurling. *On two problems concerning linear transformations in Hilbert space.* Acta Mathematica 81 (1949), 239–255.
- **[Foundational]** N. Aronszajn and K. T. Smith. *Invariant subspaces of completely continuous operators.* Annals of Mathematics 60 (1954), 345–350.
- **[Foundational]** A. R. Bernstein and A. Robinson. *Solution of an invariant subspace problem of K. T. Smith and P. R. Halmos.* Pacific Journal of Mathematics 16 (1966), 421–431.
- **[Foundational]** P. R. Halmos. *Invariant subspaces of polynomially compact operators.* Pacific Journal of Mathematics 16 (1966), 433–437.
- **[Foundational]** P. R. Halmos. *Ten problems in Hilbert space.* Bulletin of the AMS 76 (1970), 887–933.
- **[Foundational]** V. I. Lomonosov. *Invariant subspaces of the family of operators that commute with a completely continuous operator.* Functional Analysis and Its Applications 7 (1973), 213–214.
- **[SOTA]** S. W. Brown. *Some invariant subspaces for subnormal operators.* Integral Equations and Operator Theory 1 (1978), 310–333.
- **[SOTA]** P. Enflo. *On the invariant subspace problem for Banach spaces.* Acta Mathematica 158 (1987), 213–313.
- **[SOTA]** C. J. Read. *A solution to the invariant subspace problem.* Bulletin of the London Mathematical Society 16 (1984), 337–401.
- **[SOTA]** C. J. Read. *A solution to the invariant subspace problem on the space $\ell_1$.* Bulletin of the London Mathematical Society 17 (1985), 305–317.
- **[SOTA]** C. J. Read. *Quasinilpotent operators and the invariant subspace problem.* Journal of the London Mathematical Society 56 (1997), 595–606.
- **[SOTA]** S. Brown, B. Chevreau and C. Pearcy. *On the structure of contraction operators II.* Journal of Functional Analysis 76 (1988), 30–55.
- **[SOTA]** S. A. Argyros and R. G. Haydon. *A hereditarily indecomposable $\mathcal{L}_\infty$-space that solves the scalar-plus-compact problem.* Acta Mathematica 206 (2011), 1–54.
- **[Survey]** H. Radjavi and P. Rosenthal. *Invariant Subspaces.* Springer, 1973; 2nd ed. Dover, 2003.
- **[Survey]** I. Chalendar and J. R. Partington. *Modern Approaches to the Invariant Subspace Problem.* Cambridge University Press, 2011.
- **[Survey]** B. Sz.-Nagy, C. Foiaş, H. Bercovici and L. Kérchy. *Harmonic Analysis of Operators on Hilbert Space.* 2nd ed., Springer, 2010.

## 10. Worked Example / Concrete Special Case

**The unilateral shift on $H^2$ — a case where the lattice is fully computed.**

Take $H = H^2(\mathbb{D})$ with orthonormal basis $\{z^n\}_{n\ge0}$, and $S f = zf$. Then $\|S\|=1$, $\sigma(S) = \overline{\mathbb{D}}$, and $S$ has no eigenvalues: $zf(z) = \lambda f(z)$ forces $f \equiv 0$.

*A visible invariant subspace.* $M_1 = \overline{\operatorname{span}}\{z, z^2, \dots\} = zH^2$ is closed, proper, nonzero, and $S(zH^2) = z^2H^2 \subseteq zH^2$. So $S$ is not a counterexample — trivially.

*The full lattice.* Beurling's theorem says every $M \in \operatorname{Lat}(S)$ with $M \neq \{0\}$ equals $\theta H^2$ for an inner $\theta$, unique up to a unimodular constant. Sketch: $zM \subseteq M$ and $zM \neq M$ (else $M = z^nM$ for all $n$ gives $M=\{0\}$), so pick a unit $\theta \in M \ominus zM$. Orthogonality of $\theta$ to $z^n\theta$ for all $n \ge 1$ gives
$$\int_{\mathbb{T}} |\theta|^2 e^{-in t}\,dm = 0 \quad (n \ge 1),$$
and taking conjugates, for all $n \neq 0$; hence $|\theta|^2$ has constant Fourier transform, so $|\theta| = 1$ a.e.: $\theta$ is inner. One then shows $M = \theta H^2$.

*Concrete instance.* Take $\theta(z) = \dfrac{z - 1/2}{1 - z/2}$, a Blaschke factor. Then
$$\theta H^2 = \{ f \in H^2 : f(1/2) = 0 \},$$
a codimension-one invariant subspace. Its orthogonal complement is spanned by the Szegő kernel $k_{1/2}(z) = (1 - z/2)^{-1}$, and $S^* k_{1/2} = \tfrac12 k_{1/2}$ — the adjoint has eigenvalue $1/2$, which is exactly the mechanism producing the invariant subspace for $S$.

*Why this does not settle the problem.* Every step used $\sigma_p(S^*) = \mathbb{D} \neq \emptyset$ plus an explicit analytic model. A hypothetical counterexample $T$ satisfies $\sigma_p(T) = \sigma_p(T^*) = \emptyset$, so no reproducing kernel is an eigenvector and no Beurling-type factorization is available. The gap of §6 is precisely the absence of any model for that residual class.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*