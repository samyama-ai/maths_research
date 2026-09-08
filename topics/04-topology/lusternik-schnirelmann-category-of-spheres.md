---
id: 04-topology/lusternik-schnirelmann-category-of-spheres
title: "Lusternik-Schnirelmann Category of Spheres"
topic: 04-topology
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Lusternik-Schnirelmann Category of Spheres

> **Topic:** Topology & Knot Theory · **ID:** `04-topology/lusternik-schnirelmann-category-of-spheres` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

The Lusternik–Schnirelmann (LS) category of a sphere is elementary: $\mathrm{cat}(S^n) = 1$ for every $n \ge 1$ in the normalized convention. The research problem carrying this name is not that computation but the question of how spheres act on category under products — **Ganea's conjecture**, posed by Tudor Ganea in 1971:

> For every finite CW complex $X$ and every $n \ge 1$,
> $$\mathrm{cat}(X \times S^n) = \mathrm{cat}(X) + 1 .$$

The inequality $\le$ is a special case of the classical product bound $\mathrm{cat}(X\times Y)\le \mathrm{cat}(X)+\mathrm{cat}(Y)$. The content is the lower bound: multiplying by a sphere — the simplest possible non-contractible factor, of category exactly $1$ — should never fail to raise category.

**Status.** The conjecture is **false**. Norio Iwase (1998) constructed finite complexes $X$ with $\mathrm{cat}(X)=2$ and $\mathrm{cat}(X\times S^n)=2$. What remains open is the residual classification problem: characterize the pairs $(X,n)$ for which equality holds, and settle the low-dimensional and manifold cases — in particular the case $n=1$, for which no counterexample is known. A complete resolution would give a checkable criterion, in terms of the attaching data of $X$, deciding whether $\mathrm{cat}(X\times S^n)$ is $\mathrm{cat}(X)$ or $\mathrm{cat}(X)+1$.

## 2. Mathematical Foundations

**Definition (normalized LS category).** For a topological space $X$, $\mathrm{cat}(X)$ is the least integer $k$ such that $X$ admits an open cover $X = U_0\cup\cdots\cup U_k$ with each $U_i$ contractible in $X$ (each inclusion $U_i\hookrightarrow X$ null-homotopic). Thus $\mathrm{cat}(X)=0$ iff $X$ is contractible. It is a homotopy invariant (Fox, 1941).

**Ganea fibration.** Let $G_0(X)=PX \to X$ be the path fibration with fiber $\Omega X$, and define inductively $G_{k}(X) \to X$ by taking the fiberwise join of $G_{k-1}(X)$ with $\Omega X$. Then
$$\mathrm{cat}(X)\le k \iff G_k(X)\to X \text{ admits a section.}$$
This converts category into a lifting/obstruction problem.

**Lower bounds.**
- *Cup-length.* If there are $x_1,\dots,x_k \in \widetilde H^*(X;R)$ with $x_1\smile\cdots\smile x_k \neq 0$, then $\mathrm{cat}(X)\ge k$.
- *Category weight* (Fadell–Husseini; Rudyak; Strom): a refinement $\mathrm{wgt}(u)$ assigned to $u\in \widetilde H^*(X)$ with $\mathrm{cat}(X)\ge \mathrm{wgt}(u)$ and $\mathrm{wgt}(u\smile v)\ge \mathrm{wgt}(u)+\mathrm{wgt}(v)$.

**Upper bounds.** $\mathrm{cat}(X)\le \dim X$ for connected CW complexes; $\mathrm{cat}(X)\le \mathrm{cl}(X)$, the cone length; and for $(q-1)$-connected $X$, $\mathrm{cat}(X)\le \dim X / q$ (Grossman–Whitehead type bound).

**Spheres.** $S^n$ is covered by two open sets, each an enlarged hemisphere, hence contractible in $S^n$; and $S^n$ is not contractible. So
$$\mathrm{cat}(S^n)=1,\qquad n\ge 1 .$$

**Ganea's problem in cell form.** Write $X=A\cup_\alpha e^{m+1}$ with $\alpha: S^m\to A$. Berstein–Hilton (1960) attached to $\alpha$ a **Hopf invariant** $H(\alpha)\in [S^m,\, \Omega(\ast^{k+1}\Omega A)]$-type group, with
$$\mathrm{cat}(A\cup_\alpha e^{m+1}) = \mathrm{cat}(A) \iff H(\alpha)=0 \quad(\text{when }\mathrm{cat}(A)=k).$$
Ganea's conjecture is equivalent to the assertion that such Hopf invariants never die after smashing with a sphere. Iwase's counterexamples are exactly complexes where they do.

**Morse-theoretic motivation.** Lusternik and Schnirelmann (1934): for a closed manifold $M$, every smooth function $f:M\to\mathbb{R}$ has at least $\mathrm{cat}(M)+1$ critical points. Product behaviour of $\mathrm{cat}$ therefore controls critical-point counts on $M\times S^n$.

## 3. History & State of the Art (SOTA)

- **1934.** Lusternik and Schnirelmann introduce the invariant to prove that every Riemannian metric on $S^2$ carries three simple closed geodesics.
- **1941.** Fox proves homotopy invariance and the product inequality $\mathrm{cat}(X\times Y)\le\mathrm{cat}(X)+\mathrm{cat}(Y)$.
- **1960.** Berstein and Hilton introduce generalized Hopf invariants detecting category of two-cones.
- **1971.** Ganea, in *Some problems on numerical homotopy invariants*, poses the product-with-a-sphere problem as Problem 4.
- **1990–91.** Jessup, then Hess, settle the rational case: Hess proves Ganea's conjecture for simply connected rational spaces, via the Quillen/Sullivan model characterization $\mathrm{cat}_0 = \mathrm{Mcat}$.
- **1998.** Iwase disproves the conjecture: a finite complex $X$ with $\mathrm{cat}(X)=2=\mathrm{cat}(X\times S^n)$, built $p$-locally at an odd prime from a cell attached to a sphere along a map whose Hopf invariant is killed by the sphere factor.
- **2002.** Iwase's $A_\infty$-method paper sharpens this to low-dimensional, small-cell counterexamples, including complexes with only two cells, and gives a general criterion for $\mathrm{cat}(X\times S^n)$ in terms of $A_\infty$-structures on $\Omega X$.
- **1999–2003.** Rudyak, Strom, Vandembroucq and Stanley isolate large positive classes (manifolds under connectivity/dimension constraints; spaces where cone length equals category).
- **2003.** Iwase computes $\mathrm{cat}$ of every sphere bundle over a sphere, giving a complete answer in the first family where spheres and category interact nontrivially.
- **2003.** Cornea–Lupton–Oprea–Tanré publish the standard monograph, which is still the reference account.

## 4. Partial Results / Verified Cases

Ganea's equality $\mathrm{cat}(X\times S^n)=\mathrm{cat}(X)+1$ is **proved** in the following cases.

| Class | Result |
|---|---|
| $\mathrm{cat}(X)\le 1$ (co-H-spaces, suspensions $\Sigma Y$) | Holds; $\mathrm{cat}(\Sigma Y\times S^n)=2$ |
| Simply connected rational spaces | Hess (1991): $\mathrm{cat}_0(X\times S^n)=\mathrm{cat}_0(X)+1$ |
| $X$ with $\mathrm{cat}(X)=\mathrm{cl}(X)$ (cone length) | Holds, since cone length is additive over the sphere factor |
| $X$ with $\mathrm{cat}(X)$ realized by cup-length over some ring $R$ | Holds: $x_1\cdots x_k\otimes u_n \neq 0$ in $H^*(X\times S^n)$ |
| Tori, real/complex projective spaces, closed surfaces | $\mathrm{cat}(T^k)=k$, $\mathrm{cat}(\mathbb{RP}^k)=\mathrm{cat}(\mathbb{CP}^k)=k$; all cup-length-sharp |
| Closed manifolds $M$, $(s-1)$-connected, with $\dim M$ small relative to $s\cdot(\mathrm{cat}(M)+1)$ | Rudyak (1999), extended by Strom via category weight |
| Sphere bundles over spheres | Iwase (2003) computes $\mathrm{cat}$ outright; equality determined by clutching-function Hopf invariants |
| $n=1$, i.e. $X\times S^1$ | No counterexample known; open in general *(frontier — verify)* |

**Counterexamples.** Iwase (1998, 2002): finite complexes $X$ with $\mathrm{cat}(X)=2$ and $\mathrm{cat}(X\times S^n)=2$ for suitable $n$, constructed $p$-locally. So the conjecture already fails at the smallest nontrivial value $\mathrm{cat}(X)=2$, and the failure is not a large-category or infinite-dimensional pathology.

## 5. Principal Obstacles

- **No sharp lower bound.** Every computable lower bound — cup-length, category weight, Toda-bracket length, rational invariants — is a *homology-level* shadow of category. The counterexamples live exactly where all of them are strictly smaller than $\mathrm{cat}(X)$, so no cohomological method can detect the difference.
- **Category is not stable.** $\mathrm{cat}$ is not determined by the stable homotopy type, and the Berstein–Hilton Hopf invariant that controls it can be nonzero yet become null after smashing with $S^n$. Suspension and stabilization arguments therefore cannot transport the lower bound across the product.
- **Obstruction theory does not terminate.** Deciding whether $G_k(X\times S^n)\to X\times S^n$ has a section is an infinite tower of obstructions in homotopy groups of iterated joins of $\Omega X$; these groups are unknown for all but the simplest $X$.
- **Rational methods lose the counterexamples.** Hess's proof works because rational homotopy theory linearizes the problem into a Sullivan/Quillen model, where the relevant Hopf invariant is a Whitehead-product expression. The failures are $p$-torsion phenomena, invisible rationally.
- **No algorithm.** There is no known decision procedure computing $\mathrm{cat}(X)$ from a finite CW presentation, even for $2$-cell complexes at a fixed prime; the invariant is not finitely determined by any known finite data set.

## 6. The Gap

Proven: equality holds whenever the category of $X$ is *detected* by an additive invariant (cup-length, category weight, cone length, rational model) — i.e. whenever the lower bound $\mathrm{cat}(X)\ge k$ comes from a source that automatically upgrades to $\mathrm{cat}(X\times S^n)\ge k+1$. Refuted: equality fails when $\mathrm{cat}(X)$ exceeds all such detectors and the excess is carried by an unstable Hopf invariant that the sphere factor annihilates.

The gap is the missing *invariant*: a functor $W$ with $\mathrm{cat}(X)\ge W(X)$, $W(X\times S^n)\ge W(X)+1$, and $W(X)=\mathrm{cat}(X)$ on a class strictly larger than the current one — or, dually, a structural criterion on the $A_\infty$-structure of $\Omega X$ that decides the dichotomy. Concretely, the unresolved boundary is: (i) the case $n=1$ for all finite complexes; (ii) closed manifolds without connectivity hypotheses; (iii) a classification of counterexamples at the prime $2$.

## 7. Current Research (as of June 2026)

- **$A_\infty$ and higher-structure methods.** Iwase's school (Kyushu) continues to refine the $A_\infty$-criterion, relating $\mathrm{cat}$, the *module* category $\mathrm{Mcat}$, and topological complexity $\mathrm{TC}$; the same machinery decides Ganea-type questions for $\mathrm{TC}$.
- **Manifold cases.** Work descending from Rudyak and Strom on closed manifolds, using category weight and cohomology of the Ganea fibration, aims to prove Ganea's equality unconditionally for closed manifolds; no counterexample is known to be a manifold *(frontier — verify)*.
- **Rational and $p$-local models.** Groups around Félix, Halperin, Lupton, Oprea, Tanré and Vandembroucq (Lille, Louvain, Cleveland State) study $\mathrm{cat}_0$, $\mathrm{Mcat}$ and fibrewise constructions, where the product formula is exactly understood.
- **Sectional/ topological-complexity analogues.** The analogous "does $\times S^n$ raise it by one" question for $\mathrm{TC}$ and for sectional category is an active source of new counterexample techniques.
- **Motivic and equivariant category.** Recent work transporting LS category to motivic homotopy theory and to $G$-spaces raises the product question afresh in settings where the Ganea fibration behaves differently *(frontier — verify)*.

## 8. Future Work

- Settle $n=1$: is $\mathrm{cat}(X\times S^1)=\mathrm{cat}(X)+1$ for all finite complexes? A counterexample would need a Hopf invariant killed by a single suspension coordinate.
- Prove or refute Ganea's equality for all closed smooth manifolds; Rudyak has repeatedly proposed this as the right surviving form of the conjecture.
- Produce a $2$-primary counterexample of minimal dimension, and determine the minimal dimension over all primes.
- Develop an invariant intermediate between category weight and $\mathrm{cat}$ that is additive on products with spheres and sharp on two-cones.
- Extend Iwase's sphere-bundle computation to bundles with non-spherical fiber, and to iterated products $X\times S^{n_1}\times\cdots\times S^{n_r}$.

## 9. Key References

- **[Foundational]** L. Lusternik and L. Schnirelmann. *Méthodes topologiques dans les problèmes variationnels.* Hermann, Paris, 1934.
- **[Foundational]** R. H. Fox. *On the Lusternik–Schnirelmann category.* Annals of Mathematics 42 (1941), 333–370.
- **[Foundational]** I. Berstein and P. J. Hilton. *Category and generalized Hopf invariants.* Illinois Journal of Mathematics 4 (1960), 437–451. [DOI](https://doi.org/10.1215/ijm/1255456060)
- **[Foundational]** T. Ganea. *Some problems on numerical homotopy invariants.* In: Symposium on Algebraic Topology, Lecture Notes in Mathematics 249, Springer, 1971, 13–22. [DOI](https://doi.org/10.1007/bfb0060892)
- **[SOTA]** N. Iwase. *Ganea's conjecture on Lusternik–Schnirelmann category.* Bulletin of the London Mathematical Society 30 (1998), 623–634.
- **[SOTA]** N. Iwase. *$A_\infty$-method in Lusternik–Schnirelmann category.* Topology 41 (2002), 695–723. [DOI](https://doi.org/10.1016/s0040-9383(00)00045-8)
- **[SOTA]** N. Iwase. *Lusternik–Schnirelmann category of a sphere-bundle over a sphere.* Topology 42 (2003), 701–713. [DOI](https://doi.org/10.1016/s0040-9383(02)00026-5)
- **[Partial results]** K. Hess. *A proof of Ganea's conjecture for rational spaces.* Topology 30 (1991), 205–214. [DOI](https://doi.org/10.1016/0040-9383(91)90006-p)
- **[Partial results]** B. Jessup. *Rational L-S category and a conjecture of Ganea.* Journal of Pure and Applied Algebra 65 (1990), 57–67. [DOI](https://doi.org/10.1016/0022-4049(90)90100-v)
- **[Partial results]** Yu. B. Rudyak. *On category weight and its applications.* Topology 38 (1999), 37–55. [DOI](https://doi.org/10.1016/s0040-9383(97)00101-8)
- **[Partial results]** D. Stanley. *Spaces of Lusternik–Schnirelmann category $n$ and cone length $n+1$.* Topology 39 (2000), 985–1019. [DOI](https://doi.org/10.1016/s0040-9383(99)00047-6)
- **[Survey / Book]** O. Cornea, G. Lupton, J. Oprea, D. Tanré. *Lusternik–Schnirelmann Category.* Mathematical Surveys and Monographs 103, American Mathematical Society, 2003.
- **[Survey]** I. M. James. *On category, in the sense of Lusternik–Schnirelmann.* Topology 17 (1978), 331–348. [DOI](https://doi.org/10.1016/0040-9383(78)90002-2)

## 10. Worked Example / Concrete Special Case

**Step 1: $\mathrm{cat}(S^n)=1$.** Let $N=(0,\dots,0,1)$ and $S=-N$. Put $U_0=S^n\setminus\{N\}$ and $U_1=S^n\setminus\{S\}$. Each is homeomorphic to $\mathbb{R}^n$ by stereographic projection, hence contractible in itself and a fortiori in $S^n$, and $U_0\cup U_1=S^n$. So $\mathrm{cat}(S^n)\le 1$. Since $S^n$ is not contractible ($H_n(S^n)=\mathbb{Z}\ne 0$), $\mathrm{cat}(S^n)\ne 0$. Hence $\mathrm{cat}(S^n)=1$. Corollary (Lusternik–Schnirelmann): every smooth $f:S^n\to\mathbb{R}$ has at least $2$ critical points — sharp, by the height function.

**Step 2: Ganea's equality for $X=S^m$.** Upper bound: $\mathrm{cat}(S^m\times S^n)\le \mathrm{cat}(S^m)+\mathrm{cat}(S^n)=2$. Lower bound by cup-length: with $a\in H^m(S^m\times S^n;\mathbb{Z})$ and $b\in H^n(S^m\times S^n;\mathbb{Z})$ the pullbacks of the fundamental classes, the Künneth theorem gives
$$H^*(S^m\times S^n;\mathbb{Z}) \cong \mathbb{Z}[a,b]/(a^2,b^2),\qquad a\smile b \neq 0 .$$
A nonzero product of two positive-degree classes forces $\mathrm{cat}\ge 2$. Therefore
$$\mathrm{cat}(S^m\times S^n)=2=\mathrm{cat}(S^m)+1 .$$
Iterating, $\mathrm{cat}(S^{n_1}\times\cdots\times S^{n_k})=k$, and $\mathrm{cat}(T^k)=k$.

**Step 3: where the argument breaks.** The lower bound above used only cup-length. Take instead a two-cone $X=S^q\cup_\alpha e^{r+1}$ with $\alpha$ having trivial Hurewicz image, so that all cup products in $\widetilde H^*(X)$ vanish and cup-length gives only $\mathrm{cat}(X)\ge 1$. Berstein–Hilton theory can still force $\mathrm{cat}(X)=2$, because the Hopf invariant $H(\alpha)$ is nonzero. In $X\times S^n$ there is still no nonzero triple cup product, so cohomology gives nothing beyond $\mathrm{cat}\ge 2$; and Iwase's computation shows that for suitable $\alpha$ (localized at an odd prime $p$) the relevant Hopf invariant is annihilated by the sphere factor, yielding an explicit section of $G_2(X\times S^n)$ and hence
$$\mathrm{cat}(X\times S^n)=2=\mathrm{cat}(X),$$
contradicting Ganea's conjecture. The example isolates the mechanism precisely: the extra unit of category in $X$ is unstable data, and multiplying by $S^n$ destroys it rather than adding to it.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*