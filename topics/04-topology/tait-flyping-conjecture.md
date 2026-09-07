---
id: 04-topology/tait-flyping-conjecture
title: "Tait Flyping Conjecture"
topic: 04-topology
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Tait Flyping Conjecture

> **Topic:** Topology & Knot Theory · **ID:** `04-topology/tait-flyping-conjecture` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

**Conjecture (Tait, c. 1877–1885).** Let $L$ be a prime link in $S^3$ that admits an alternating diagram, and let $D_1, D_2 \subset S^2$ be two reduced alternating diagrams of $L$. Then $D_1$ and $D_2$ are related by a finite sequence of *flypes* (together with isotopy of $S^2$).

Here a diagram is *alternating* if, travelling along each component, crossings alternate over–under–over–under; *reduced* if it has no nugatory crossing (a crossing separated by a simple closed curve in $S^2$ meeting the diagram only at that crossing).

A complete proof must show that the flype move alone generates the equivalence relation "same link" on the set of reduced alternating diagrams of a fixed prime alternating link. A disproof would exhibit two reduced alternating diagrams of one prime link lying in distinct flype orbits.

**Status.** Proved by W. Menasco and M. Thistlethwaite (announcement 1991, full proof *Annals of Mathematics* 1993). It is listed as `solved-recently` in the sense of the modern era of the subject: it closed the last of the three Tait conjectures and remains the structural theorem on which every alternating-link classification algorithm and knot table is built. Its natural generalisations (beyond prime, beyond alternating, beyond $S^3$) are still open.

## 2. Mathematical Foundations

**Diagrams.** A link diagram is a 4-valent graph $D \subset S^2$ with over/under decoration at each vertex. Write $c(D)$ for the number of crossings and $c(L) = \min_D c(D)$ for the crossing number. The writhe of an oriented diagram is $w(D)=\sum_{x}\varepsilon(x)$, $\varepsilon(x)\in\{\pm 1\}$.

**Tangles and flypes.** A *2-tangle* $T$ is a pair $(B, T\cap B)$ with $B\subset S^2$ a disc meeting $D$ transversally in exactly $4$ points $\{\mathrm{NW},\mathrm{NE},\mathrm{SW},\mathrm{SE}\}$. Suppose $D$ decomposes as a crossing $c$ adjacent to a tangle $T$:
$$D \;=\; \big(\,c \;\ast\; T\,\big).$$
The **flype** is the move
$$c \ast T \;\longmapsto\; T^{\rho} \ast c ,$$
where $T^{\rho}$ is $T$ rotated by $\pi$ about the horizontal axis of $B$ in the projection plane, and the crossing $c$ is transported to the opposite side of $T$. A flype preserves $c(D)$, the writhe $w(D)$, the alternating property, and the link type.

**Kauffman bracket.** With $\langle \,\cdot\, \rangle \in \mathbb{Z}[A^{\pm1}]$ defined by
$$\big\langle \,\overcrossing\, \big\rangle = A\big\langle \,)(\, \big\rangle + A^{-1}\big\langle \,\smile\!\!\frown\, \big\rangle, \qquad \langle D \sqcup \bigcirc\rangle = (-A^2-A^{-2})\langle D\rangle, \qquad \langle \bigcirc \rangle = 1,$$
the Jones polynomial is $V_L(t) = \big((-A)^{-3w(D)}\langle D\rangle\big)_{A = t^{-1/4}}$. For a connected diagram, $\operatorname{spread}\langle D\rangle \le 4c(D)+4$, with equality iff $D$ is *adequate*; reduced alternating diagrams are adequate. This inequality is the engine of the first two Tait conjectures.

**Theorem (Kauffman 1987, Murasugi 1987, Thistlethwaite 1987).** A reduced alternating diagram of a link $L$ has minimal crossing number, and any two reduced alternating diagrams of $L$ have the same writhe.

**Theorem (Menasco–Thistlethwaite 1993 — the flyping theorem).** The conjecture of §1 holds.

**Corollary (rigidity).** For a prime alternating link $L$, $c(L)$, $w(D)$, the Conway/Gauss structure of $D$, and the flype orbit of $D$ are complete diagrammatic invariants; consequently the equivalence problem for alternating links is decidable in time polynomial in $c(L)$ after a canonical-form computation.

## 3. History & State of the Art (SOTA)

- **1877–1885.** Peter Guthrie Tait, tabulating knots up to 10 crossings with Kirkman and Little, formulated three empirical principles: minimality of reduced alternating diagrams, writhe invariance (equivalently, no amphichiral alternating knot has odd crossing number), and the flyping principle. Tait had no invariant capable of proving any of them.
- **1928–1984.** The Alexander polynomial cannot see crossing number; Tait's conjectures survive untouched for a century. Menasco (1984) proves alternating links are prime iff their diagrams are, and that alternating link complements contain no closed essential tori unless the link is a satellite — the geometric toolkit later needed.
- **1985–1987.** Jones' polynomial arrives; Kauffman, Murasugi and Thistlethwaite independently settle Tait I and II via the bracket span.
- **1991–1993.** Menasco and Thistlethwaite prove the flyping conjecture, combining (i) Menasco's incompressible-surface / crossing-ball geometry in the complement of an alternating link, applied to a sphere realising a second diagram, with (ii) polynomial obstructions controlling the combinatorics of the resulting tangle decompositions.
- **1998–present.** Consequences dominate tabulation: Hoste–Thistlethwaite–Weeks enumerate all $1{,}701{,}936$ knots to 16 crossings; Sundberg–Thistlethwaite compute the exact exponential growth rate of prime alternating links; Burton (2020) extends tables to 19 crossings. Greene (2017) and Howie (2017) give intrinsic, diagram-free characterisations of alternating links, reproving Tait-type rigidity from the topology of the exterior.

## 4. Partial Results / Verified Cases

- **Rational (2-bridge) links.** Fully classified by Schubert (1956): $S(p,q)\cong S(p,q')$ iff $q'\equiv q^{\pm1}\ (\mathrm{mod}\ p)$. The flyping theorem here reduces to reversal of the continued fraction $[a_1,\dots,a_n]$, verified independently of Menasco–Thistlethwaite.
- **Montesinos and pretzel links.** Bonahon–Siebenmann's classification of Seifert-fibred/Montesinos pairs confirms the flype orbits (cyclic permutation and reversal of the rational tangles) for all alternating Montesinos links.
- **Small crossing number.** Verified exhaustively by computer for all prime alternating knots and links with $c \le 16$ (Hoste–Thistlethwaite–Weeks), and for knots to $c \le 19$ (Burton, 2020): $1$ knot at $c=3$, $123$ at $c=10$, $1288$ at $c=12$, $379{,}799$ at $c=16$, and $1{,}769{,}979$ prime alternating knots at $c=19$.
- **Counting consequence.** Sundberg–Thistlethwaite (1998): the number $A_n$ of prime alternating links with $n$ crossings satisfies
$$\limsup_n A_n^{1/n} \;=\; \frac{101+\sqrt{21001}}{40}\;\approx\;6.1479,$$
a computation that is only meaningful because flypes give the exact redundancy in diagram counting.
- **Beyond $S^3$.** Boden–Karimi (2022) prove the Tait minimality and writhe statements, and flyping-type rigidity, for alternating links in thickened surfaces $\Sigma\times I$ via the Jones–Krushkal polynomial.
- **Still unverified generalisations.** No flype-like generating theorem is known for adequate but non-alternating links, for non-prime alternating diagrams beyond the obvious connected-sum bookkeeping, or for alternating virtual links in full generality.

## 5. Principal Obstacles

The obstacles that made the conjecture hard for 110 years — and that still block its generalisations — are:

- **Polynomial invariants are blind to diagram moves.** The bracket span bounds $c(D)$ from below and pins the writhe, but a polynomial is a single element of $\mathbb{Z}[A^{\pm1}]$: it cannot distinguish flype orbits, since flypes preserve every known invariant. Tait III is a *statement about moves*, not about numbers, so no invariant-theoretic argument can close it.
- **Reidemeister calculus is unbounded.** Two diagrams of the same link are related by Reidemeister moves, but no a priori bound on their number or on intermediate crossing count follows from Reidemeister's theorem; Coward (2006) showed the moves cannot generally be ordered to avoid crossing increase. So one cannot enumerate paths between $D_1$ and $D_2$.
- **Two spheres, one complement.** The real content is: given a link $L$ and two projection spheres $S_1, S_2$ realising alternating diagrams, isotope $S_2$ to $S_1$. This is a normal-surface problem in a 3-manifold where the surfaces are not incompressible in the usual sense, and standard minimal-surface or hierarchy machinery does not directly apply. Menasco's crossing-ball technique had to be extended to control intersection curves that are neither trivial nor essential.
- **Failure outside the alternating class.** Menasco's geometry uses the "black/white checkerboard bands are essential" property that is specific to reduced alternating diagrams. For a general link, minimal diagrams need not have equal writhe (e.g. non-alternating knots with distinct-writhe minimal diagrams exist), so no move set can exist that preserves writhe *and* connects all minimal diagrams. There is no candidate generalised flype.
- **Hyperbolic geometry is not sharp enough.** Mostow rigidity classifies alternating link complements up to isometry, but recovering the *diagram* — a combinatorial object living on an unmarked $S^2$ — from the geometry needs an extra step; Greene's and Howie's characterisations supply that only for existence of some alternating diagram, not for the move structure relating two of them.

## 6. The Gap

For the original statement there is no remaining gap: primeness plus alternation plus reducedness plus the flype move is exactly the right package, and Menasco–Thistlethwaite closed it. The live boundary is one level out:

1. **From alternating to adequate.** Adequate diagrams also realise the bracket-span equality and have invariant writhe. *No* move set is known that connects all minimal adequate diagrams of an adequate link. This is the closest genuine open analogue of Tait III.
2. **From $S^3$ to $\Sigma\times I$ and virtual links.** Boden–Karimi handle checkerboard-colourable alternating surface links; the non-checkerboard-colourable and non-cellularly-embedded cases lack a flyping theorem.
3. **From existence to effectiveness.** Menasco–Thistlethwaite gives decidability but the number of flypes needed, and hence the size of the flype orbit, is bounded only by the (exponentially large) count of tangle decompositions. A polynomial bound on the flype distance between two reduced alternating diagrams of the same link is not proved.

## 7. Current Research (as of June 2026)

- **Intrinsic characterisations.** Greene's *definite spanning surface* criterion and Howie's *two-sided essential surface* criterion (both 2017) are being pushed toward a purely topological re-derivation of the flyping theorem, which would replace the crossing-ball combinatorics by surface-theoretic uniqueness. Groups at Boston College, Auckland and MPIM Bonn are active here. *(frontier — verify)*
- **Surface and virtual links.** Boden, Karimi and Sikora continue the thickened-surface programme; the open target is a flype theorem for alternating links in $\Sigma\times I$ without checkerboard colourability.
- **Enumeration and physics.** The Zinn-Justin–Zuber matrix-model approach to counting alternating tangles is being revisited with modern random-map techniques to obtain subexponential corrections to $A_n \sim C\,\mu^n n^{-\alpha}$; flype quotienting is the combinatorial heart of the computation.
- **Computation.** Burton's `Regina`-based 19-crossing census and successor efforts to 20+ crossings rely on flype-orbit canonical forms; the practical bottleneck is isomorphism testing of flype orbits, not diagram generation. *(frontier — verify)*
- **Quantum-invariant reformulations.** Attempts to see the flype orbit as a groupoid acting on a categorified invariant (Khovanov homology of alternating links is thin, hence carries no extra data) have so far confirmed that categorification adds nothing here — a negative result that sharpens the case for geometric methods.

## 8. Future Work

- Prove or refute a **flype-type theorem for adequate links**: identify a finite move set generating all minimal adequate diagrams.
- Obtain a **quantitative flyping theorem**: a polynomial upper bound $f(c(L))$ on the number of flypes relating any two reduced alternating diagrams, which would immediately give a clean polynomial-time equivalence algorithm.
- Re-prove Menasco–Thistlethwaite **without diagram combinatorics**, using only Greene/Howie-style essential-surface uniqueness; this is the route most likely to generalise to $\Sigma\times I$.
- Extend the theorem to **alternating links in general 3-manifolds** (Howie–Purcell's alternating links on surfaces in 3-manifolds) where minimality results already exist but move-generation does not.
- Settle the **flype orbit growth** question: asymptotics for the average orbit size among prime alternating diagrams of $n$ crossings.

## 9. Key References

- **[Foundational]** P. G. Tait. *On Knots I, II, III.* In: Scientific Papers, Vol. 1, Cambridge University Press, 1898 (papers originally 1877–1885).
- **[Foundational]** H. Schubert. *Knoten mit zwei Brücken.* Mathematische Zeitschrift 65 (1956), 133–170.
- **[Foundational]** W. Menasco. *Closed incompressible surfaces in alternating knot and link complements.* Topology 23 (1984), 37–44.
- **[Foundational]** L. H. Kauffman. *State models and the Jones polynomial.* Topology 26 (1987), 395–407.
- **[Foundational]** K. Murasugi. *Jones polynomials and classical conjectures in knot theory.* Topology 26 (1987), 187–194.
- **[Foundational]** M. B. Thistlethwaite. *A spanning tree expansion of the Jones polynomial.* Topology 26 (1987), 297–309.
- **[Resolution]** W. Menasco and M. Thistlethwaite. *The Tait flyping conjecture.* Bulletin of the American Mathematical Society 25 (1991), 403–412.
- **[Resolution]** W. Menasco and M. Thistlethwaite. *The classification of alternating links.* Annals of Mathematics 138 (1993), 113–171.
- **[SOTA / Recent]** J. Greene. *Alternating links and definite surfaces.* Duke Mathematical Journal 166 (2017), 2133–2151.
- **[SOTA / Recent]** J. Howie. *A characterisation of alternating knot exteriors.* Geometry & Topology 21 (2017), 2353–2371.
- **[SOTA / Recent]** H. U. Boden and H. Karimi. *The Jones–Krushkal polynomial and minimal diagrams of surface links.* Annales de l'Institut Fourier 72 (2022), 1437–1475.
- **[Computational]** C. Sundberg and M. Thistlethwaite. *The rate of growth of the number of prime alternating links and tangles.* Pacific Journal of Mathematics 182 (1998), 329–358.
- **[Computational]** J. Hoste, M. Thistlethwaite and J. Weeks. *The first 1,701,936 knots.* The Mathematical Intelligencer 20 (1998), 33–48.
- **[Computational]** B. A. Burton. *The next 350 million knots.* Proceedings of the 36th International Symposium on Computational Geometry (SoCG 2020), LIPIcs 164.
- **[Survey]** W. B. R. Lickorish. *An Introduction to Knot Theory.* Springer GTM 175, 1997 (Chapters 5–6 for the Tait conjectures).
- **[Survey]** P. Zinn-Justin and J.-B. Zuber. *Matrix integrals and the counting of tangles and links.* Discrete Mathematics 246 (2002), 343–360.

## 10. Worked Example / Concrete Special Case

**Two reduced alternating diagrams of $6_2$ related by one flype.**

Take Conway's rational tangle notation $C(a_1,a_2,a_3)$, built by alternately adding $a_i$ horizontal or vertical twists. The associated fraction is the continued fraction
$$\frac{p}{q} \;=\; a_3 + \cfrac{1}{a_2 + \cfrac{1}{a_1}}.$$

*Diagram $D_1$:* $C(3,1,2)$. Fraction $= 2 + \cfrac{1}{1 + \tfrac{1}{3}} = 2 + \tfrac{3}{4} = \tfrac{11}{4}$, so $D_1$ is a diagram of the 2-bridge link $S(11,4)$, with $c(D_1) = 3+1+2 = 6$.

*Diagram $D_2$:* $C(2,1,3)$. Fraction $= 3 + \cfrac{1}{1 + \tfrac{1}{2}} = 3 + \tfrac{2}{3} = \tfrac{11}{3}$, so $D_2$ is a diagram of $S(11,3)$, with $c(D_2)=6$.

*They are the same knot.* Schubert's criterion says $S(p,q)\cong S(p,q')$ iff $q'\equiv q^{\pm1}\pmod p$. Here $3\cdot 4 = 12 \equiv 1 \pmod{11}$, so $4 \equiv 3^{-1}$ and $S(11,4)\cong S(11,3)$. In tables this is the knot $6_2$, with
$$V_{6_2}(t) \;=\; -t^{-4}+2t^{-3}-2t^{-2}+2t^{-1}-2+2t-t^{2}.$$

*The flype.* Isolate the 2-tangle $T$ consisting of the $a_1$-twist region together with the single $a_2$ crossing, with the outermost crossing $c$ of the $a_3$ region sitting to its left. Rotating $T$ by $\pi$ about the horizontal axis and transporting $c$ to the right-hand side of $T$ is exactly the move $c\ast T \mapsto T^{\rho}\ast c$; the result is the diagram $C(2,1,3)$. One flype therefore carries $D_1$ to $D_2$.

*Checks the theorem predicts.* Both diagrams are reduced (no nugatory crossings: each of the three twist regions has $a_i\ge 1$ and the tangle is not a connected sum) and alternating; both have $6$ crossings, matching $c(6_2)=6$ from the bracket-span bound $\operatorname{spread}\langle D\rangle = 4\cdot 6 + 4 = 28$; both have writhe $w = -2$ for the standard orientation, as Tait II requires. The flyping theorem asserts that these are the *only* reduced alternating 6-crossing diagrams of $6_2$ up to flypes and sphere isotopy — which is precisely what the exhaustive $c\le 16$ census confirms, and what makes the entry "$6_2$" in a knot table well defined.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*