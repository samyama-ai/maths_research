---
id: 02-algebra-group-theory/foulkes-conjecture
title: "Foulkes' Conjecture"
topic: 02-algebra-group-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Foulkes' Conjecture

> **Topic:** Algebra & Group Theory · **ID:** `02-algebra-group-theory/foulkes-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Let $1 \le m \le n$ be integers and let $S_{mn}$ act on the set of partitions of $\{1,\dots,mn\}$ into $m$ unordered blocks of size $n$. Write $H^{(m,n)}$ for the resulting complex permutation module; its stabiliser is the wreath product $S_n \wr S_m \le S_{mn}$, so
$$H^{(m,n)} \;=\; \mathrm{Ind}_{S_n \wr S_m}^{S_{mn}} \mathbf{1}.$$

**Foulkes' Conjecture (1950).** For all $m \le n$, $H^{(m,n)}$ embeds in $H^{(n,m)}$ as a $\mathbb{C}S_{mn}$-module: every irreducible $S^\lambda$ ($\lambda \vdash mn$) satisfies
$$\big\langle H^{(m,n)},\, S^\lambda \big\rangle \;\le\; \big\langle H^{(n,m)},\, S^\lambda \big\rangle .$$

Equivalently, in the ring of symmetric functions, $h_n \circ h_m - h_m \circ h_n$ is **Schur-positive** for $m \le n$; equivalently, for every vector space $V$, the $GL(V)$-module $\mathrm{Sym}^m(\mathrm{Sym}^n V)$ is isomorphic to a submodule of $\mathrm{Sym}^n(\mathrm{Sym}^m V)$.

A proof must establish the inequality for **all** pairs $(m,n)$ with $m \le n$ and all $\lambda$; a disproof requires one explicit pair and one partition $\lambda$ with strictly larger multiplicity on the left. Note that no *natural* (i.e. $GL$-equivariant, canonically defined) embedding is required — and indeed none is available (§5).

## 2. Mathematical Foundations

**Plethysm.** For symmetric functions $f,g$ with $g$ a sum of monomials $\sum_i u_i$, the plethysm $f \circ g$ is $f$ evaluated at the alphabet $\{u_i\}$. On complete homogeneous functions, $h_m \circ h_n$ is the Frobenius characteristic of $H^{(m,n)}$:
$$\mathrm{ch}\, H^{(m,n)} = h_m \circ h_n = \sum_{\lambda \vdash mn} a_\lambda(m,n)\, s_\lambda ,\qquad a_\lambda(m,n) := \langle h_m\circ h_n, s_\lambda\rangle \in \mathbb{Z}_{\ge 0}.$$
The $a_\lambda(m,n)$ are the **plethysm coefficients**; equivalently $\mathrm{Sym}^m(\mathrm{Sym}^n V) \cong \bigoplus_\lambda \mathbb{S}_\lambda(V)^{\oplus a_\lambda(m,n)}$ where $\mathbb{S}_\lambda$ is the Schur functor. The conjecture reads
$$a_\lambda(m,n) \le a_\lambda(n,m) \quad \text{for all } m \le n,\ \lambda \vdash mn. \tag{F}$$

**Dimensions.** $\dim H^{(m,n)} = \dfrac{(mn)!}{m!\,(n!)^m}$, and $m \le n \Rightarrow n!\,(m!)^n \le m!\,(n!)^m$, so (F) is consistent on dimensions — the numerical shadow of the conjecture is elementary.

**Foulkes–Howe map.** Howe (1987) constructed a canonical $GL(V)$-equivariant map
$$\varphi_{m,n} : \mathrm{Sym}^m(\mathrm{Sym}^n V) \longrightarrow \mathrm{Sym}^n(\mathrm{Sym}^m V),$$
obtained by polarising a product of $m$ degree-$n$ forms and re-grouping; combinatorially it sends an $m \times n$ "block" tableau to the sum over its row/column transversals. Injectivity of $\varphi_{m,n}$ for $m \le n$ implies (F).

**Hermite reciprocity.** For $\dim V = 2$,
$$\mathrm{Sym}^m(\mathrm{Sym}^n \mathbb{C}^2) \cong \mathrm{Sym}^n(\mathrm{Sym}^m \mathbb{C}^2),$$
so (F) holds with equality for all $\lambda$ with at most two rows. This is the classical invariant-theoretic origin of the problem: $H^{(m,n)}$ counts covariants/concomitants of binary and ternary forms.

**Thrall's formulas** (the $m=2$ and $n$-fold-$h_2$ cases):
$$h_2 \circ h_n = \sum_{k=0}^{\lfloor n/2 \rfloor} s_{(2n-2k,\,2k)}, \qquad h_n \circ h_2 = \sum_{\substack{\lambda \vdash 2n \\ \text{all parts even}}} s_\lambda .$$

## 3. History & State of the Art (SOTA)

- **1942** — R. M. Thrall computes $h_n\circ h_2$ and $h_2 \circ h_n$ explicitly, settling the $m=2$ case.
- **1950** — H. O. Foulkes, studying concomitants of the quintic and sextic, states the conjecture in *J. London Math. Soc.* **25**, together with a stronger monotonicity statement.
- **1987** — R. Howe introduces $\varphi_{m,n}$ in the $(GL_n,GL_m)$-duality framework, giving the conjecture a map-theoretic form.
- **1993** — M. Brion proves the **asymptotic** version: for fixed $m$, (F) holds for all $n \gg 0$. The proof uses Hilbert-series/degeneration arguments on Grassmannian cones and is non-effective.
- **2000–2017** — the "small $m$" ladder is climbed: $m=3$ (Dent–Siemons), $m=4$ (Vessenes), $m=5$ (Cheung–Ikenmeyer–Mkrtchyan).
- **2005** — Müller and Neunhöffer show computationally that $\varphi_{5,5}$ is **not injective**, killing the most natural proof strategy.
- **2008** — T. McKay proves related plethysm conjectures of Stanley and gives effective stable ranges.
- **2010s–2020s** — the problem is absorbed into geometric complexity theory (GCT) and into the general study of plethysm positivity (Ikenmeyer, Panova, Bürgisser; Paget–Wildon; Bowman–de Visscher–Orellana).

**SOTA summary:** proved for $m \le 5$ (all $n$); proved for $\ell(\lambda) \le 2$; proved asymptotically in $n$ for fixed $m$; open in general, with $m = n = 6$ (a question about $S_{36}$) the first fully unresolved symmetric instance.

## 4. Partial Results / Verified Cases

| Case | Result | Source |
|---|---|---|
| $m = 1$ | Trivial ($h_1 \circ h_n = h_n$) | — |
| $m = 2$, all $n$ | True; explicit decompositions | Thrall (1942) |
| $m = 3$, all $n$ | True | Dent–Siemons (2000) |
| $m = 4$, all $n$ | True | Vessenes (2004) |
| $m = 5$, all $n$ | True ("the 5th case") | Cheung–Ikenmeyer–Mkrtchyan (2017) |
| $\ell(\lambda) \le 2$ | Equality of multiplicities | Hermite reciprocity |
| Fixed $m$, $n \ge N(m)$ | True, $N(m)$ non-effective | Brion (1993) |
| $m=n=5$ ($S_{25}$) | Verified by machine computation | Müller–Neunhöffer (2005) |
| Extremal $\lambda$ | Maximal/minimal constituents of $h_m\circ h_n$ determined and shown to obey (F) | Paget–Wildon (2016, 2019) |
| $\varphi_{m,n}$ injective | $m \le 4$ (all $n$); **fails** at $(5,5)$ | Brion; Müller–Neunhöffer |

Small verified instance: $(m,n)=(2,3)$, difference $s_{(2,2,2)}$ (worked in §10).

## 5. Principal Obstacles

- **No positive combinatorial rule for plethysm.** Unlike Littlewood–Richardson coefficients, $a_\lambda(m,n)$ has no known manifestly nonnegative combinatorial formula; Stanley lists this as a central open positivity problem. Without such a rule, (F) cannot be reduced to an injection of combinatorial sets.
- **Complexity barrier.** Deciding positivity of plethysm coefficients is NP-hard (Fischer–Ikenmeyer, 2020), and the coefficients are not known to lie in $\\#P$. A uniformly checkable certificate for (F) is therefore unlikely to be cheap.
- **The natural map fails.** The single most attractive route — prove $\varphi_{m,n}$ injective — is dead: $\varphi_{5,5}$ has a kernel. Any proof must produce a non-canonical embedding, or work purely numerically on multiplicities.
- **Ineffective asymptotics.** Brion's argument yields existence of $N(m)$ from finiteness/flatness statements about Hilbert functions, not a bound; the gap between "large $n$" and the finitely many remaining $n$ per $m$ is not bridged by his method.
- **Induction on $m$ degrades.** The proofs for $m \le 5$ build explicit tableau-symmetrisation matrices whose size grows super-exponentially; the $m=5$ proof already requires computer-assisted rank certificates. There is no visible inductive step from $m$ to $m+1$.
- **Brute force is out of reach.** $H^{(6,6)}$ sits inside $S_{36}$ with $\dim = 36!/(6!\,(6!)^6) \approx 2.7\times10^{18}$; character-theoretic evaluation over all $\lambda \vdash 36$ is feasible only in restricted ranges, not as a decomposition of modules.

## 6. The Gap

The proven region is $\{m \le 5\} \cup \{\ell(\lambda)\le 2\} \cup \{n \ge N(m)\}$. The general statement quantifies over the *two-dimensional* family $(m,n)$ with both parameters large — precisely the region where neither the tableau-symmetrisation machinery (needs small $m$) nor Brion's stability (needs $n$ enormous relative to $m$) applies. Concretely, the missing step is one of:

1. an **effective** bound $N(m)$ in Brion's theorem, small enough that the residual finitely many $(m,n)$ per $m$ are computable; or
2. a uniform-in-$m$ construction of an injection $H^{(m,n)} \hookrightarrow H^{(n,m)}$, necessarily *not* equal to $\varphi_{m,n}$ (which fails at $(5,5)$); or
3. a positive combinatorial rule, or a positivity-preserving operator, that expresses $a_\lambda(n,m) - a_\lambda(m,n)$ as a cardinality.

The first genuinely open symmetric case is $m=n=6$.

## 7. Current Research (as of June 2026)

- **GCT-driven plethysm study** (Ikenmeyer, Panova, Bürgisser, and collaborators; Saarbrücken / USC / TU Berlin lineage): rectangular Kronecker and plethysm coefficients, vanishing behaviour, and the demonstration that occurrence obstructions alone cannot separate $\mathbf{VP}_{ws}$ from $\mathbf{VNP}$. Foulkes' conjecture is the model positivity question in this program.
- **Representation-theoretic school around Foulkes modules** (Paget, Wildon, Bowman, de Visscher, Orellana; Royal Holloway / Kent / City St George's): twisted Foulkes modules $H^{(m,n)} \otimes \mathrm{sgn}$, maximal and minimal constituents of $s_\nu \circ s_\mu$, and partition-algebra models for plethysm.
- **Polyhedral / commutative-algebra methods** (Kahle, Michałek, Manivel): plethysm coefficients as lattice-point counts of parametric polytopes, quasi-polynomiality in $n$, and effective versions of stability. *(frontier — verify)* Progress on explicit stability thresholds for $s_\lambda$-multiplicities in $h_m\circ h_n$ continues to be reported in preprints; no published effective $N(m)$ resolving §6(1) is known to the editor.
- **Computational verification** using modular character theory and Chevie/GAP/Magma at $m=n=6$ restricted to families of $\lambda$. *(frontier — verify)* No claimed full resolution of $(6,6)$ has been confirmed.

No credible claim of a proof or counterexample to the general conjecture is currently in circulation.

## 8. Future Work

- **Make Brion effective.** Extract a bound $N(m)$ from the Hilbert-function/degeneration argument, ideally polynomial in $m$, then close the residual window computationally.
- **Search for a repaired map.** Study $\ker \varphi_{m,n}$ structurally: is the kernel confined to $\lambda$ with many rows, and can $\varphi_{m,n}$ be corrected by a lower-order term to restore injectivity for $m\le n$?
- **Stability in $\lambda$.** Prove monotonicity of $a_\lambda(m,n)$ under adding columns/rows, which would let one reduce (F) to boundary partitions.
- **Character-free proofs.** Construct the embedding at the level of $\mathbb{Z}$-forms or of $S_{mn}$-sets with multiplicity, e.g. via a poset/injection between combinatorial models of $m\times n$ set partitions.
- **Prove the $m=6$ case.** Even one further rung would test whether the tableau-symmetrisation method has an intrinsic ceiling.

## 9. Key References

- **[Foundational]** H. O. Foulkes. *Concomitants of the quintic and sextic up to degree four in the coefficients of the ground form.* Journal of the London Mathematical Society **25** (1950), 205–209.
- **[Foundational]** R. M. Thrall. *On symmetrized Kronecker powers and the structure of the free Lie ring.* American Journal of Mathematics **64** (1942), 371–388.
- **[Foundational]** R. Howe. *$(GL_n, GL_m)$-duality and symmetric plethysm.* Proceedings of the Indian Academy of Sciences (Mathematical Sciences) **97** (1987), 85–109.
- **[Structural]** M. Brion. *Stable properties of plethysm: on two conjectures of Foulkes.* Manuscripta Mathematica **80** (1993), 347–371.
- **[Partial result]** S. C. Dent and J. Siemons. *On a conjecture of Foulkes.* Journal of Algebra **226** (2000), 236–249.
- **[Partial result]** R. Vessenes. *Generalized Foulkes' conjecture and tableaux construction.* Journal of Algebra **277** (2004), 579–614.
- **[Computational]** J. Müller and M. Neunhöffer. *Some computations regarding Foulkes' conjecture.* Experimental Mathematics **14** (2005), 277–283.
- **[Partial result]** T. McKay. *On plethysm conjectures of Stanley and Foulkes.* Journal of Algebra **319** (2008), 2050–2071.
- **[SOTA / Recent]** W. Cheung, C. Ikenmeyer and S. Mkrtchyan. *Symmetrizing tableaux and the 5th case of the Foulkes conjecture.* Journal of Symbolic Computation **80** (2017), 833–843.
- **[SOTA / Recent]** C. Ikenmeyer and G. Panova. *Rectangular Kronecker coefficients and plethysms in geometric complexity theory.* Advances in Mathematics **319** (2017), 40–66.
- **[SOTA / Recent]** N. Fischer and C. Ikenmeyer. *The computational complexity of plethysm coefficients.* Computational Complexity **29** (2020), article 8.
- **[SOTA / Recent]** R. Paget and M. Wildon. *Generalized Foulkes modules and maximal and minimal constituents of plethysms of Schur functions.* Proceedings of the London Mathematical Society **118** (2019), 1153–1187.
- **[Survey]** R. P. Stanley. *Positivity problems and conjectures in algebraic combinatorics.* In *Mathematics: Frontiers and Perspectives*, American Mathematical Society, 2000, 295–319.
- **[Survey / Textbook]** I. G. Macdonald. *Symmetric Functions and Hall Polynomials*, 2nd edition. Oxford University Press, 1995. (Chapter I.8 and Appendix A: plethysm.)

## 10. Worked Example / Concrete Special Case

Take $m=2$, $n=3$, so $mn = 6$ and the claim is $h_3 \circ h_2 - h_2 \circ h_3 \succeq 0$.

**Left module $H^{(3,2)}$:** partitions of $\{1,\dots,6\}$ into three blocks of size $2$. Count: $6!/(3!\,2!^3) = 15$. By Thrall,
$$h_3 \circ h_2 = \sum_{\substack{\lambda \vdash 6 \\ \text{all parts even}}} s_\lambda = s_{(6)} + s_{(4,2)} + s_{(2,2,2)} .$$

**Right module $H^{(2,3)}$:** partitions into two blocks of size $3$. Count: $6!/(2!\,3!^2) = 10$. By Thrall,
$$h_2 \circ h_3 = s_{(6)} + s_{(4,2)} .$$

**Dimension check.** $\dim S^{(6)} = 1$, $\dim S^{(4,2)} = 9$, $\dim S^{(2,2,2)} = 5$ (hook-length formula). Then $1+9 = 10 = \dim H^{(2,3)}$ and $1+9+5 = 15 = \dim H^{(3,2)}$. Consistent.

**Conclusion.** With $m=2 \le n=3$,
$$h_3\circ h_2 - h_2 \circ h_3 = s_{(2,2,2)} \succeq 0,$$
so $H^{(2,3)} \hookrightarrow H^{(3,2)}$, with cokernel the $5$-dimensional irreducible $S^{(2,2,2)}$. Concretely: the map sending a $3{+}3$ split $\{A, A^c\}$ to the sum of all $2{+}2{+}2$ partitions refining it is injective here, and its cokernel is exactly $S^{(2,2,2)}$.

**Why this is not the general picture.** The same "refinement" map is the combinatorial shadow of $\varphi_{m,n}$. It is injective for $m\le 4$ but acquires a kernel at $m=n=5$ (Müller–Neunhöffer), so the clean cokernel computation above has no known analogue for large $m$ — the multiplicity inequality must then be argued without exhibiting a canonical embedding.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*