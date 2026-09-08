---
id: 04-topology/montesinos-conjecture
title: "Montesinos Conjecture"
topic: 04-topology
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Montesinos Conjecture

> **Topic:** Topology & Knot Theory · **ID:** `04-topology/montesinos-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

A link $L \subset S^3$ is **universal** if *every* closed orientable 3-manifold $M$ is a branched covering space of $S^3$ with branch set contained in $L$. The conjecture attributed to Montesinos (with Hilden and Lozano) is:

> **Conjecture (Hilden–Lozano–Montesinos, 1985).** Every knot $K \subset S^3$ that is not a torus knot is universal.

The complementary half is a theorem: no torus knot $T_{p,q}$ is universal. So the conjecture asserts that the torus knots are the *only* obstruction, i.e. universality is detected by a single classical property of the knot complement (Seifert fibration).

A proof requires, for each non-torus knot $K$ and each closed orientable 3-manifold $M$, the construction of a transitive representation $\omega:\pi_1(S^3\setminus K)\to S_n$ whose Fox completion is homeomorphic to $M$. A disproof requires exhibiting one non-torus knot $K$ and one closed orientable 3-manifold $M$ that is not a branched cover of $S^3$ over $K$ — for instance by producing a geometric or homological invariant obstructing all such $\omega$.

*Nomenclature.* Several statements carry Montesinos' name. The **Montesinos–Nakanishi 3-move conjecture** (every link reduces to a trivial link by 3-moves) was **disproved** by Dąbkowski–Przytycki (2002). The Hilden–Montesinos 3-fold branched covering statement is a **theorem** (1974). The universality statement above is the one that remains open.

## 2. Mathematical Foundations

**Branched coverings.** Let $L\subset S^3$ be a link. A map $p:M\to S^3$ is an $n$-fold branched covering with branch set $L$ if
$$p|_{p^{-1}(S^3\setminus L)}:\;p^{-1}(S^3\setminus L)\longrightarrow S^3\setminus L$$
is an ordinary $n$-fold covering and $p$ is the *Fox completion* of it over $L$. Such coverings are classified by transitive representations
$$\omega:\pi_1(S^3\setminus L)\longrightarrow S_n,$$
taken up to conjugation in $S_n$. If a meridian $\mu_i$ of a component of $L$ satisfies $\omega(\mu_i)=\sigma$ with cycle decomposition of lengths $(k_1,\dots,k_r)$, then $p^{-1}(L)$ has $r$ components lying over that component, with local branching indices $k_1,\dots,k_r$. The covering is **simple** if every $\omega(\mu_i)$ is a transposition, **regular** if $\omega$ has image acting freely-transitively, i.e. $\ker\omega$ is normal of index $n$.

**Universality.**
$$L \text{ universal} \iff \forall\, M^3 \text{ closed, orientable, connected } \exists\, n,\ \omega:\pi_1(S^3\setminus L)\to S_n \text{ with } \widehat{M_\omega}\cong M.$$
Note that $\omega$ is *not* required to be simple, and branching indices may differ along $p^{-1}(L)$; this flexibility is what makes single-knot universality plausible.

**Orbifold reformulation.** For $n\ge 2$ let $\mathcal{O}(L,n)$ denote the orbifold with underlying space $S^3$ and singular locus $L$ of cone order $n$. If $\mathcal{O}(L,n)$ is hyperbolic, its orbifold group embeds as a Kleinian group $\Gamma \subset \mathrm{Isom}^+(\mathbb{H}^3)=\mathrm{PSL}_2(\mathbb{C})$. A group $\Gamma$ is a **universal group** if every closed orientable 3-manifold is $\mathbb{H}^3/G$ for some finite-index torsion-free $G\le\Gamma$. Universality of $L$ follows if some $\mathcal{O}(L,n)$ has a universal group, since manifold covers of $\mathcal{O}(L,n)$ are branched covers of $S^3$ over $L$.

**Background theorems relied on.**
- *Alexander (1920):* every closed orientable PL $n$-manifold is a branched cover of $S^n$.
- *Hilden (1974), Montesinos (1974):* every closed orientable 3-manifold is a **3-fold simple** branched cover of $S^3$ branched over a **knot**. Here the knot depends on $M$; universality demands one knot for all $M$.
- *Thurston (1982):* universal links exist; the Borromean rings and the Whitehead link are universal.
- *Composition principle:* if $q:S^3\to S^3$ is a branched covering with branch set $K$ and $q^{-1}(K)\supseteq L$ with $L$ universal, then $K$ is universal (compose $M\to S^3 \to S^3$ and apply Fox completion).

## 3. History & State of the Art (SOTA)

- **1920.** Alexander proves every closed orientable PL 3-manifold is a branched cover of $S^3$; the branch set is an arbitrary graph.
- **1974.** Hilden and Montesinos independently reduce the branch set to a knot and the degree to $3$. This is the structural precursor: 3-manifolds are "knots plus permutation data".
- **1982.** Thurston introduces the term *universal link* and gives the first examples, using hyperbolic geometry and the fact that $\mathbb{H}^3/\Gamma$ for the Borromean-rings orbifold group has enough finite-index subgroups. He asks whether a universal **knot** exists.
- **1983.** Hilden, Lozano and Montesinos answer affirmatively (announcement in *Bull. AMS*): universal knots exist. Their method: start from a universal link, take branched covers of $S^3$ over a candidate knot, and arrange the preimage to contain a universal link.
- **1985.** In *Topology*, the same authors prove the **figure-eight knot $4_1$ is universal** and that **no torus knot is universal**. The conjecture in Section 1 is stated there.
- **1987–1992.** Montesinos' book *Classical Tessellations and Three-Manifolds* systematises the tessellation/orbifold viewpoint; the Borromean-orbifold papers identify the relevant universal groups as **arithmetic** Kleinian groups.
- **2003 onward.** Geometrization (Perelman) removes any need for topological case analysis in the "target" manifold $M$, but supplies no new construction of coverings; the conjecture is untouched by it.

State of the art: universality is proved for scattered explicit knots and infinite families produced by the composition principle; it is disproved only for torus knots. There is no general criterion, and no algorithm that decides universality of a given knot.

## 4. Partial Results / Verified Cases

- **Universal links.** Borromean rings; the Whitehead link; the $(2,2,2,\dots)$ chain links of $\ge 3$ components (Thurston, 1982). Every link containing a universal sublink is universal.
- **Universal knots.** The figure-eight knot $4_1$ (Hilden–Lozano–Montesinos, *Topology* 24, 1985). Infinitely many further knots, including rational (2-bridge) knots and knots constructed as branch sets whose preimage under a low-degree branched self-covering of $S^3$ contains the Borromean rings (HLM, *Universal Knots*, LNM 1144, 1985).
- **Negative case (complete).** For all coprime $p,q\ge 2$, the torus knot $T_{p,q}$ is **not** universal: $3_1=T_{2,3}$, $5_1=T_{2,5}$, $7_1$, $8_{19}=T_{3,4}$, etc. This is the only known family of non-universal knots.
- **Degree bounds.** Universality gives no uniform degree: for a fixed universal knot $K$, the minimal $n$ with $M$ an $n$-fold cover grows with the complexity of $M$ (Gromov norm of $M$ is bounded above by $n$ times that of the orbifold, giving $n \gtrsim \|M\|/\|\mathcal{O}\|$).
- **Orbifold-group level.** Certain arithmetic Kleinian groups, obtained from Borromean-rings orbifolds with small cone orders, are proved universal (HLM, *On the Borromean orbifolds: geometry and arithmetic*, 1992).

## 5. Principal Obstacles

- **No invariant detects universality.** Universality is a $\forall M \exists \omega$ statement over an infinite, unbounded family. Classical knot invariants (Alexander polynomial, genus, signature, Jones polynomial) are covering-insensitive in the required direction; none is known to obstruct any non-torus knot.
- **The only known proof technique is constructive.** Every positive result proceeds by exhibiting an explicit branched covering $S^3\to S^3$ whose upstairs branch set contains a known universal link. This is a finite hand computation per knot; it does not parameterise over knot types. Hyperbolic knots have wildly varying symmetry groups, and the composition trick needs a covering $S^3\to S^3$ branched over $K$, which typically requires $K$ to have a periodic or strongly invertible symmetry — most knots have trivial symmetry group.
- **The torus-knot obstruction is geometric, not algebraic.** It uses the Seifert fibration of the complement; there is no analogue for hyperbolic or satellite complements, so the negative side of the dichotomy has no candidate generalisation to test against.
- **Subgroup separability is insufficient.** Even with Agol–Wise (virtual specialness, LERF for hyperbolic 3-manifold groups), one gets *many* finite-index subgroups of $\pi_1(S^3\setminus K)$, but no control over which closed 3-manifold the Fox completion produces. The passage from a cover of the complement to a *prescribed* closed manifold is the uncontrolled step.
- **Satellites.** For a satellite knot, branched covers decompose along the companion torus, which suggests a JSJ obstruction; yet no satellite knot has been proved non-universal, so it is unclear whether the conjecture is even correctly stated for satellites.

## 6. The Gap

Proven: $T_{p,q}$ not universal (all $p,q$); $4_1$ and an explicit infinite family universal. Conjectured: universality for **all** non-torus knots.

The gap is a *uniformity* gap. Every known positive proof supplies, for a specific $K$, a specific branched covering $q:S^3\to S^3$ with $q^{-1}(K)\supset$ (universal link). The missing step is either

1. a construction of such a $q$ for an arbitrary hyperbolic or satellite knot — currently blocked because $q$ must be branched over $K$ itself, and such coverings exist only under symmetry hypotheses; or
2. a symmetry-free criterion, e.g. "$\mathcal{O}(K,n)$ hyperbolic for some $n$ $\Rightarrow$ its orbifold group is universal", which would follow from a strengthening of the arithmetic universal-group results to all hyperbolic knot orbifolds.

Equivalently: prove that the class of universal knots is closed under the operations that generate all non-torus knots from $4_1$, or find the first non-universal hyperbolic knot.

## 7. Current Research (as of June 2026)

- **Orbifold/arithmetic school (Madrid — UCM/UNED, continuing the Hilden–Lozano–Montesinos programme).** Classification of arithmetic 2-bridge knot and link orbifolds, and identification of which orbifold groups are universal. The working hypothesis is that universality of $\Gamma$ is generic among cocompact-by-cusped arithmetic Kleinian groups. *(frontier — verify)*
- **Computational branched-cover search.** SnapPy/Regina-based enumeration of low-degree transitive representations $\pi_1(S^3\setminus K)\to S_n$ for $n\le 8$ and census manifolds, testing which census 3-manifolds arise over a fixed candidate knot. No systematic published census exists yet. *(frontier — verify)*
- **Special-cube-complex methods.** Attempts to leverage virtual specialness to produce covers of $S^3\setminus K$ with prescribed peripheral behaviour, so that Fox completion realises a prescribed Dehn filling. The obstruction is control of the induced slopes. *(frontier — verify)*
- **Quantitative universality.** Bounds relating the minimal covering degree $n(M,K)$ to $\|M\|$ (Gromov norm) and to the volume of $\mathcal{O}(K,n)$; universality with a computable degree function would be strictly stronger than the conjecture.

## 8. Future Work

- Prove universality for all **hyperbolic 2-bridge knots** $b(p,q)$, extending the figure-eight case; these have dihedral symmetry, so the composition principle is available in principle.
- Settle the **satellite case** separately: decide whether a satellite knot with a torus-knot companion can be universal.
- Find an invariant that vanishes for torus knots and is nonzero for universal knots — a genuine *certificate* of universality rather than a construction.
- Determine whether universality is **decidable** for a given diagram.
- Establish or refute: *if $\mathcal{O}(K,n)$ is hyperbolic for some $n\ge 3$, then $K$ is universal.* This single implication, combined with orbifold geometrization, would prove the conjecture for all knots whose complements are not Seifert fibered.

## 9. Key References

- **[Foundational]** J. W. Alexander. *Note on Riemann spaces.* Bulletin of the American Mathematical Society 26 (1920), 370–372. [DOI](https://doi.org/10.1090/s0002-9904-1920-03319-7)
- **[Foundational]** H. M. Hilden. *Every closed orientable 3-manifold is a 3-fold branched covering space of $S^3$.* Bulletin of the American Mathematical Society 80 (1974), 1243–1244. [DOI](https://doi.org/10.1090/s0002-9904-1974-13699-2)
- **[Foundational]** J. M. Montesinos. *A representation of closed orientable 3-manifolds as 3-fold branched coverings of $S^3$.* Bulletin of the American Mathematical Society 80 (1974), 845–846. [DOI](https://doi.org/10.1090/s0002-9904-1974-13535-4)
- **[Foundational]** W. P. Thurston. *Universal links.* Preprint, Princeton University, 1982.
- **[SOTA]** H. M. Hilden, M. T. Lozano, J. M. Montesinos. *Universal knots.* Bulletin of the American Mathematical Society (N.S.) 8 (1983), 449–450.
- **[SOTA]** H. M. Hilden, M. T. Lozano, J. M. Montesinos. *On knots that are universal.* Topology 24 (1985), 499–504.
- **[SOTA]** H. M. Hilden, M. T. Lozano, J. M. Montesinos. *Universal knots.* In *Knot Theory and Manifolds* (D. Rolfsen, ed.), Lecture Notes in Mathematics 1144, Springer, 1985, 25–59.
- **[SOTA]** H. M. Hilden, M. T. Lozano, J. M. Montesinos. *On the Borromean orbifolds: geometry and arithmetic.* In *Topology '90*, de Gruyter, 1992, 133–167. [DOI](https://doi.org/10.1515/9783110857726.133)
- **[Survey / Book]** J. M. Montesinos. *Classical Tessellations and Three-Manifolds.* Universitext, Springer-Verlag, 1987. [DOI](https://doi.org/10.1007/978-3-642-61572-6)
- **[Survey]** J. M. Montesinos. *Representing 3-manifolds by a universal branching set.* Mathematical Proceedings of the Cambridge Philosophical Society 94 (1983), 109–123. [DOI](https://doi.org/10.1017/s0305004100060941)
- **[Related, resolved]** M. K. Dąbkowski, J. H. Przytycki. *Burnside obstructions to the Montesinos–Nakanishi 3-move conjecture.* Geometry & Topology 6 (2002), 355–360. [DOI](https://doi.org/10.2140/gt.2002.6.355)
- **[Context]** R. H. Fox. *Covering spaces with singularities.* In *Algebraic Geometry and Topology: A Symposium in Honor of S. Lefschetz*, Princeton University Press, 1957, 243–257. [DOI](https://doi.org/10.1515/9781400879915-019)

## 10. Worked Example / Concrete Special Case

**Claim.** The trefoil $3_1 = T_{2,3}$ is not universal — a complete, self-contained instance of the negative half.

Let $E = S^3\setminus \mathring{N}(3_1)$. The trefoil complement is Seifert fibered over the disk with two exceptional fibers of orders $2$ and $3$:
$$\pi_1(E) = \langle x,y \mid x^2 = y^3\rangle,$$
and $h=x^2=y^3$ generates the infinite cyclic centre, realised by a regular fiber. On $\partial E$, with meridian $\mu$ and Seifert longitude $\lambda$, the regular fiber has slope
$$f = pq = 2\cdot 3 = 6, \qquad \text{i.e. } f = 6\mu + \lambda \text{ in } H_1(\partial E).$$

Now take any branched covering $p:M\to S^3$ with branch set $3_1$, given by a transitive $\omega:\pi_1(E)\to S_n$. Then:

1. $p^{-1}(E)\to E$ is an honest $n$-fold covering, so $p^{-1}(E)$ inherits a Seifert fibration (Seifert fibrations lift to finite covers).
2. $M$ is recovered by filling each boundary torus $T_i \subset \partial p^{-1}(E)$ along the slope $\tilde\mu_i$ covering $\mu$ with degree $k_i$ (the length of the $i$-th cycle of $\omega(\mu)$).
3. Computing the intersection number of the lifted filling slope with the lifted fiber: $\Delta(\tilde\mu_i,\tilde f_i) = k_i\cdot\Delta(\mu,f)/1 = k_i \neq 0$, since $\Delta(\mu, 6\mu+\lambda)=|\,\mu\cdot\lambda\,|=1$. So the filling slope is never the fiber slope.
4. Filling a Seifert fibered space along non-fiber slopes yields a Seifert fibered space. Hence $M$ is Seifert fibered.

Consequently every branched cover of $S^3$ over the trefoil is Seifert fibered, so has Gromov norm $\|M\|=0$. But the Weeks manifold $W$ (closed hyperbolic, volume $\approx 0.9427$) has $\|W\| = \mathrm{vol}(W)/v_3 > 0$, so $W$ is not such a cover. Therefore $3_1$ is not universal; replacing $(2,3)$ by $(p,q)$ gives the general torus-knot statement.

**Contrast.** For the figure-eight knot, $\mathcal{O}(4_1,n)$ is hyperbolic for $n\ge 4$ (the complement is hyperbolic with volume $2V_{\mathrm{oct}} \approx 2.0299$), so no such fibration obstruction exists; Hilden–Lozano–Montesinos exploit a $2$-fold branched covering $S^3\to S^3$ over $4_1$ whose upstairs branch set contains a universal link, and conclude universality by composition. The conjecture asserts that this dichotomy — Seifert fibered complement blocks, everything else permits — is exhaustive.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*