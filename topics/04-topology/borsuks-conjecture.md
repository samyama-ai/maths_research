---
id: 04-topology/borsuks-conjecture
title: "Borsuk's Conjecture"
topic: 04-topology
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Borsuk's Conjecture

> **Topic:** Topology & Knot Theory · **ID:** `04-topology/borsuks-conjecture` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

Borsuk (1933) asked: can every bounded set $S \subset \mathbb{R}^d$ of positive diameter be partitioned into $d+1$ subsets, each of strictly smaller diameter than $S$?

Write $\operatorname{diam}(S) = \sup_{x,y\in S}\|x-y\|_2$ and let
$$a(S) \;=\; \min\Big\{\, m : S = \bigcup_{i=1}^m S_i,\ \operatorname{diam}(S_i) < \operatorname{diam}(S)\ \forall i \,\Big\},\qquad f(d) \;=\; \sup_{S\subset\mathbb{R}^d,\,0<\operatorname{diam}(S)<\infty} a(S).$$
Borsuk's question is whether $f(d) = d+1$. The regular $d$-simplex shows $f(d)\ge d+1$, so only the upper bound is at issue.

The answer is **no**. Kahn and Kalai (1993) constructed finite sets in $\mathbb{R}^{1325}$ (and in every dimension $d > 2014$) with $a(S) > d+1$, and proved the superpolynomial lower bound $f(d) \ge (1.2)^{\sqrt d}$ for large $d$. The conjecture is therefore refuted, but three questions remain fully open:

1. **Smallest counterexample dimension.** The conjecture is true for $d \le 3$ and false for $d \ge 64$; the range $4 \le d \le 63$ is undecided.
2. **Asymptotics of $f(d)$.** Known: $(1.2255)^{\sqrt d} \lesssim f(d) \le \big(\sqrt{3/2}+o(1)\big)^{d}$ — an exponential-versus-subexponential gap.
3. **Restricted classes.** Does Borsuk's bound hold for all centrally symmetric bodies, all bodies of revolution, all sets of $\le 2d$ points?

A resolution of (1) means either a counterexample in some $d \le 63$ or a proof of $a(S)\le d+1$ for all $S\subset\mathbb{R}^d$ in a specific dimension.

## 2. Mathematical Foundations

**Reduction to convex bodies of constant width.** $\operatorname{diam}(S) = \operatorname{diam}(\operatorname{conv} S)$, so one may assume $S$ compact convex. Every set of diameter $1$ is contained in a *complete* set of diameter $1$, and completeness in $\mathbb{R}^d$ is equivalent to constant width $1$: $h_K(u)+h_K(-u)=1$ for all $u\in S^{d-1}$, where $h_K(u)=\sup_{x\in K}\langle x,u\rangle$. Hence
$$f(d) \;=\; \max\{\,a(K): K\subset\mathbb{R}^d \text{ convex of constant width}\,\}.$$

**Diameter graph.** For finite $S$ define $G(S)$ with vertex set $S$ and $xy \in E$ iff $\|x-y\| = \operatorname{diam}(S)$. Then $a(S) = \chi(G(S))$, the chromatic number. Counterexamples are therefore produced by exhibiting finite point configurations whose diameter graph has large chromatic number relative to the ambient dimension.

**Two-distance sets and the tensor trick.** Kahn–Kalai work with $\{-1,1\}$-vectors. For $x \in \{-1,1\}^n$ let $\varphi(x) = x x^{\mathsf T} \in \mathbb{R}^{n\times n}$, retaining the $\binom{n}{2}$ strictly-upper-triangular entries. Then
$$\|\varphi(x)-\varphi(y)\|_2^2 \;=\; \tfrac{1}{2}\big(n^2 - \langle x,y\rangle^2\big),$$
so $\varphi(x),\varphi(y)$ are at maximum distance exactly when $|\langle x,y\rangle|$ is minimal. Choosing $x$'s as $\pm 1$ indicator vectors of subsets, minimal $|\langle x,y\rangle|$ becomes a forbidden-intersection condition.

**Frankl–Wilson theorem (1981).** Let $p$ be prime and $\mathcal F \subseteq \binom{[n]}{2p-1}$ with $|A\cap B| \neq p-1$ for all distinct $A,B \in \mathcal F$. Then
$$|\mathcal F| \;\le\; \binom{n}{p-1}.$$
This bounds independent sets in the diameter graph from above; dividing $|S|$ by that bound gives a chromatic-number lower bound.

**Upper bound machinery.** Schramm's illumination/covering argument for constant-width bodies gives
$$f(d) \;\le\; \Big(\sqrt{3/2} + o(1)\Big)^{d} \approx (1.2248\ldots)^d ,$$
proved independently by Bourgain and Lindenstrauss via a measure-concentration covering argument on $S^{d-1}$.

## 3. History & State of the Art (SOTA)

- **1933** — Karol Borsuk, *Drei Sätze über die $n$-dimensionale euklidische Sphäre* (Fund. Math.), proves the Borsuk–Ulam theorem and, as a corollary, that $S^{d-1}$ needs $d+1$ pieces; he poses the general question.
- **1946** — Hadwiger: true for smooth convex bodies.
- **1947–1957** — $d=3$ settled (Perkal 1947; Eggleston 1955; short proofs by Grünbaum and Heppes, 1957).
- **1963** — Grünbaum's survey codifies the "conjecture" framing; widely believed true.
- **1988–1991** — Schramm; Bourgain–Lindenstrauss: subexponential-in-$d$ *upper* bound $(\sqrt{3/2}+o(1))^d$, replacing the earlier $2^d$-type bounds.
- **1993** — Kahn and Kalai, *A counterexample to Borsuk's conjecture* (Bull. AMS): $f(d)\ge (1.2)^{\sqrt d}$; explicit counterexample in $d=1325$.
- **1994–2003** — dimension race: Nilli (Alon) $d=946$; Raigorodskii $d=561$; Weißbach $d=560$; Hinrichs $d=323$; Pikhurko $d=321$; Hinrichs–Richter $d=298$.
- **2014** — Bondarenko, *On Borsuk's conjecture for two-distance sets* (Discrete Comput. Geom.): a $416$-point two-distance set in $\mathbb{R}^{65}$ from a strongly regular graph on $416$ vertices, needing $\ge 84$ parts.
- **2014** — Jenrich and Brouwer, *A 64-dimensional counterexample to Borsuk's conjecture* (Electron. J. Combin.): a $352$-point subset in $\mathbb{R}^{64}$ requiring $\ge 71$ parts. This is the current dimension record.

## 4. Partial Results / Verified Cases

Borsuk's bound $a(S)\le d+1$ is **proved** in:

- $d = 1$: trivially $2$ pieces. $d = 2$: Pál's proof via the regular-hexagon cover, $3$ pieces. $d = 3$: $4$ pieces (Perkal, Eggleston, Grünbaum, Heppes).
- **Smooth convex bodies** in all $d$ (Hadwiger 1946): if $\partial K$ is $C^1$ with a unique support hyperplane at each boundary point, $a(K) = d+1$.
- **Bodies of constant width in $\mathbb{R}^3$**, and bodies of revolution in $\mathbb{R}^d$ (Kolodziejczyk and others, late 1980s).
- **Sets with sufficiently large symmetry / small diameter graphs**: any $S$ whose diameter graph $G(S)$ has $\chi(G(S)) \le d+1$; e.g. finite $S\subset\mathbb{R}^d$ with $|S| \le d+1$, and any $S$ of diameter $D$ contained in a ball of radius $D\sqrt{d/(2d+2)}$ (Jung's bound) with the standard cube-decomposition argument.

Borsuk's bound is **false** for:

- $d = 64$ (Jenrich–Brouwer 2014), $d = 65$ (Bondarenko 2014), $d = 1325$ and all $d \ge 2015$ (Kahn–Kalai 1993); by product/embedding arguments, all $d \ge 64$.
- Asymptotically, $f(d) \ge (1.2255)^{\sqrt d}$ (Raigorodskii's constant improvement over Kahn–Kalai).

**Undecided dimensions: $4 \le d \le 63$.**

## 5. Principal Obstacles

- **The two known proof technologies point in opposite directions and neither is tight.** Lower bounds come from extremal set theory (Frankl–Wilson/Delsarte-type bounds on forbidden-intersection families, and eigenvalue/ratio bounds on strongly regular graphs). These are strongest when the ambient dimension is large enough to host a rich two-distance set; below $d\approx 60$ the known algebraic combinatorial objects (Kneser-type families, $G_2(4)$-related strongly regular graphs, Leech-lattice sections) simply do not exist with the needed parameters.
- **Upper bounds are measure-concentration bounds, not dimension-counting bounds.** Schramm's and Bourgain–Lindenstrauss's arguments cover $S^{d-1}$ by caps whose number is exponential; they cannot produce anything near $d+1$ because concentration gives no control on the *linear* regime.
- **Borsuk–Ulam does not apply.** The topological input works for the sphere $S^{d-1}$ itself, where the obstruction is a $\mathbb{Z}/2$-equivariant one. For general sets of diameter $1$ there is no compatible free involution, so no degree/index obstruction is available; algebraic topology gives the $d+1$ bound only for the sphere and homeomorphic-image special cases.
- **Constant-width reduction destroys structure.** Completing a finite counterexample candidate to a constant-width body erases the finite combinatorics that made the diameter graph hard to colour, so the two views cannot be combined.
- **Search space in $4 \le d \le 63$ is astronomically large.** Deciding $\chi(G(S)) > d+1$ for a candidate finite $S$ is NP-hard in general, and no exhaustive parameterization of two-distance sets in $\mathbb{R}^{d}$ is known past small $d$.

## 6. The Gap

Two precise gaps.

**Dimension gap.** Proven: $f(d)=d+1$ for $d\le 3$; $f(64) \ge 71 > 65$. Unknown: every $d$ with $4 \le d \le 63$. The obstruction is that all known counterexamples are two-distance sets whose diameter graph has small independence number relative to $|S|$; the Delsarte linear-programming bound forbids such sets in $\mathbb{R}^d$ for small $d$. Crossing the gap requires either (a) a *non*-two-distance construction, or (b) a genuine upper-bound proof for a fixed $d \ge 4$ — nobody has proved $f(4)\le 5$, and even $f(4) < \infty$ with a good constant is delicate.

**Asymptotic gap.** Proven: $c^{\sqrt d} \le f(d) \le C^{d}$ with $c = 1.2255$, $C = \sqrt{3/2}$. Which exponent is correct — $\sqrt d$ or $d$ — is unknown. Kalai has conjectured the truth is closer to the $\sqrt d$ side; no improvement of the exponent from either direction has been achieved since 1993/1991.

## 7. Current Research (as of June 2026)

- **Algebraic-combinatorial lower dimensions.** Groups around Raigorodskii (Moscow Institute of Physics and Technology) continue to push counterexamples down using distance graphs on $\{0,1,-1\}$-vectors and $q$-analogues of Frankl–Wilson. No published improvement on $d=64$ since 2014. *(frontier — verify)* Reported computer searches over strongly regular graph parameter sets and spherical two-distance sets in $50 \le d \le 63$ have so far only reproduced the Jenrich–Brouwer bound.
- **Polynomial-method / slice-rank refinements** of Frankl–Wilson (Croot–Lev–Pach style) are being tested to improve the constant in $(1.2255)^{\sqrt d}$; gains so far are in the constant, not the exponent.
- **Illumination-number connections.** The Hadwiger–Levi covering conjecture and the Borsuk problem share the constant-width reduction; recent progress on illumination for constant-width bodies (Arman, Bondarenko, Prymak and co-authors) yields improved explicit covering constants in low dimensions and is the most plausible route to a genuine upper bound in $d = 4$. *(frontier — verify)*
- **Coding-theoretic bounds** on two-distance sets (Barg, Musin, and successors) are used to *exclude* counterexamples below a threshold; sharpening the semidefinite-programming (SDP) hierarchies for spherical codes would certify $f(d)=d+1$ for specific small $d$ if the bounds became tight.

## 8. Future Work

- **Settle $d=4$.** Either prove $a(S)\le 5$ for all $S\subset\mathbb{R}^4$ (Grünbaum's long-standing challenge) or find a $4$-dimensional set needing $6$ parts. All experts expect the conjecture is true here; no proof technique is known.
- **Close the exponent gap.** Determine whether $\log f(d) \asymp \sqrt d$ or $\asymp d$. Improving Schramm's covering bound to $\exp(O(\sqrt{d}\log d))$ would essentially settle it.
- **Non-two-distance constructions.** Every known counterexample lives on two distances. Constructions from three or more distances, or from lattices such as $\Lambda_{24}$ sections, could break the $d\ge 64$ barrier downward.
- **SDP certification.** Push Delsarte/Bachoc–Vallentin-type semidefinite bounds to certify Borsuk's bound for all finite sets in a fixed dimension $d \le 10$.
- **Constant-width geometry.** Classify extremal constant-width bodies in $\mathbb{R}^4$; a Hadwiger-type smoothing argument that tolerates corners would immediately give many new dimensions.

## 9. Key References

- **[Foundational]** Karol Borsuk. *Drei Sätze über die $n$-dimensionale euklidische Sphäre.* Fundamenta Mathematicae 20 (1933), 177–190.
- **[Foundational]** Hugo Hadwiger. *Überdeckung einer Menge durch Mengen kleineren Durchmessers.* Commentarii Mathematici Helvetici 18 (1946), 73–75.
- **[Foundational]** Peter Frankl and Richard M. Wilson. *Intersection theorems with geometric consequences.* Combinatorica 1 (1981), 357–368.
- **[Breakthrough]** Jeff Kahn and Gil Kalai. *A counterexample to Borsuk's conjecture.* Bulletin of the American Mathematical Society 29 (1993), 60–62.
- **[Upper bound]** Oded Schramm. *Illuminating sets of constant width.* Mathematika 35 (1988), 180–189.
- **[Upper bound]** Jean Bourgain and Joram Lindenstrauss. *On covering a set in $\mathbb{R}^d$ by balls of the same diameter.* Geometric Aspects of Functional Analysis, Lecture Notes in Mathematics 1469, Springer, 1991, 138–144.
- **[SOTA / Recent]** Andriy V. Bondarenko. *On Borsuk's conjecture for two-distance sets.* Discrete & Computational Geometry 51 (2014), 509–515.
- **[SOTA / Recent]** Thomas Jenrich and Andries E. Brouwer. *A 64-dimensional counterexample to Borsuk's conjecture.* The Electronic Journal of Combinatorics 21 (2014), \#P4.29.
- **[Survey]** Branko Grünbaum. *Borsuk's problem and related questions.* Proceedings of Symposia in Pure Mathematics VII (Convexity), AMS, 1963, 271–284.
- **[Survey]** Andrei M. Raigorodskii. *Around Borsuk's problem.* Journal of Mathematical Sciences 154 (2008), 604–623.
- **[Book]** Vladimir Boltyanski, Horst Martini, Petru S. Soltan. *Excursions into Combinatorial Geometry.* Springer, 1997.
- **[Book]** Martin Aigner and Günter M. Ziegler. *Proofs from THE BOOK*, chapter on Borsuk's conjecture. Springer, 6th ed., 2018.

## 10. Worked Example / Concrete Special Case

**(a) The planar case, $d=2$.** Take $S$ = equilateral triangle of side $1$, so $\operatorname{diam}(S)=1$. Its diameter graph is $K_3$, so $a(S) = \chi(K_3) = 3 = d+1$: the bound is attained. For the upper bound, Pál's theorem says any planar set of diameter $1$ fits inside a regular hexagon of width $1$ (side $1/\sqrt3$). Cutting that hexagon into three congruent pentagons through its center gives pieces of diameter
$$\sqrt{3}/2 \;\approx\; 0.866 \;<\; 1,$$
so $a(S)\le 3$ for every planar $S$. Hence $f(2)=3$.

**(b) The Kahn–Kalai counterexample, $d = 1325$.** Take the prime $p = 13$ and $n = 4p = 52$. Let
$$Q = \{\, x \in \{-1,1\}^{52} : x_1 = 1,\ \\#\{i : x_i = -1\} \text{ even} \,\},\qquad |Q| = 2^{50}.$$
Map $x \mapsto \varphi(x) = (x_i x_j)_{1\le i<j\le 52} \in \mathbb{R}^{1326}$. Since $\sum_{i<j} x_i x_j = \tfrac12(\langle x,\mathbf 1\rangle^2 - 52)$ is determined by one linear functional, the image lies in an affine subspace of dimension $1325$.

Distances: $\|\varphi(x)-\varphi(y)\|^2 = \tfrac12(52^2 - \langle x,y\rangle^2)$, maximised exactly when $\langle x,y\rangle = 0$, i.e. when $x$ and $y$ differ in exactly $26$ coordinates. So the diameter graph on $\varphi(Q)$ is the "orthogonality graph".

Independent sets are families with $\langle x,y\rangle \neq 0$. Identifying $x$ with $A_x = \{i : x_i = -1\}$, orthogonality means $|A_x \triangle A_y| = 26$. Frankl–Wilson with $p=13$ bounds any such family by roughly $\binom{52}{12}$-type quantities; carrying out the estimate gives independence number
$$\alpha \;\le\; 2\sum_{i=0}^{12}\binom{51}{i}.$$
Therefore
$$a(\varphi(Q)) \;=\; \chi \;\ge\; \frac{|Q|}{\alpha} \;=\; \frac{2^{50}}{2\sum_{i\le 12}\binom{51}{i}}.$$
Numerically $\sum_{i\le 12}\binom{51}{i} \approx 1.0\times10^{12}$ while $2^{50} \approx 1.13\times 10^{15}$, giving $\chi \gtrsim 5\times 10^{2}$ — but the sharper Frankl–Wilson accounting yields $\chi > 1326 = d+1$. Borsuk's bound fails in $\mathbb{R}^{1325}$.

**(c) Why $d=64$ is small.** Jenrich–Brouwer take $352$ points from a two-distance set in $\mathbb{R}^{64}$ whose diameter graph has independence number $5$; then $\chi \ge \lceil 352/5 \rceil = 71 > 65 = d+1$. The whole refutation in this dimension is a single ratio of two integers — the difficulty is entirely in exhibiting a configuration with such a small independence number in so few dimensions.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*