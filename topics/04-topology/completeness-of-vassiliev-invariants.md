---
id: 04-topology/completeness-of-vassiliev-invariants
title: "Completeness of Vassiliev Invariants"
topic: 04-topology
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Completeness of Vassiliev Invariants

> **Topic:** Topology & Knot Theory · **ID:** `04-topology/completeness-of-vassiliev-invariants` · **Status:** open

## 1. Problem Statement / Conjecture

Let $\mathcal{K}$ be the set of isotopy classes of oriented knots in $S^3$. A rational-valued knot invariant $v:\mathcal{K}\to\mathbb{Q}$ is of **finite type (Vassiliev) of degree $\le n$** if its $(n+1)$-st iterated difference along crossing changes vanishes identically.

**Conjecture (completeness / separation).** Finite type invariants separate knots: if $K_1,K_2\in\mathcal{K}$ satisfy $v(K_1)=v(K_2)$ for every finite type invariant $v$, then $K_1=K_2$.

Equivalent formulation: the Kontsevich integral $Z:\mathcal{K}\to\widehat{\mathcal{A}}$ — the universal rational finite type invariant — is injective.

Weaker, also open, sub-problems:

- **Unknot detection.** Does $Z(K)=Z(\text{unknot})$ imply $K$ is unknotted?
- **Invertibility.** Is there a finite type invariant $v$ and a knot $K$ with $v(K)\ne v(\bar K)$, where $\bar K$ is $K$ with reversed orientation?

A proof requires showing injectivity of $Z$ (or of the full system of $\mathbb{Z}$-valued finite type invariants); a disproof requires an explicit pair $K_1\ne K_2$ with all finite type invariants equal, or a non-constructive argument producing such a pair.

## 2. Mathematical Foundations

**Singular knots and the Vassiliev skein relation.** Extend $v$ to knots with $m$ transverse double points by
$$v(K_{\times}) \;=\; v(K_{+}) - v(K_{-}),$$
where $K_\pm$ are the two resolutions of the double point. Then $v$ has degree $\le n$ iff $v$ vanishes on all knots with $n+1$ double points. Write $\mathcal{V}_n$ for the $\mathbb{Q}$-vector space of such invariants; $\mathcal{V}_0\subset\mathcal{V}_1\subset\cdots$, $\mathcal{V}=\bigcup_n\mathcal{V}_n$.

**Chord diagrams.** A chord diagram of order $n$ is an oriented circle with $n$ chords, up to orientation-preserving homeomorphism. Let $\mathcal{A}_n$ be the span of order-$n$ diagrams modulo the **one-term (framing independence)** relation — any diagram with an isolated chord is $0$ — and the **four-term relation**
$$D_1 - D_2 - D_3 + D_4 = 0,$$
where the $D_i$ agree outside a disc and differ by moving one chord endpoint past a neighbouring endpoint. A **weight system** is a linear functional $w\in\mathcal{A}_n^{*}$.

**Fundamental theorem (Vassiliev–Kontsevich).** The symbol map $v\mapsto \operatorname{symb}(v)$, sending $v\in\mathcal{V}_n$ to its value on $n$-singular knots, induces an isomorphism
$$\mathcal{V}_n/\mathcal{V}_{n-1}\;\xrightarrow{\ \cong\ }\;\mathcal{A}_n^{*}\qquad(\text{over }\mathbb{Q}).$$
Surjectivity is Kontsevich's theorem, proved by constructing the **Kontsevich integral**
$$Z(K)\;=\;\sum_{m\ge 0}\frac{1}{(2\pi i)^m}\int_{t_1<\cdots<t_m}\ \sum_{P=\{(z_j,z_j')\}}(-1)^{\downarrow P}\, D_P\ \bigwedge_{j=1}^{m}\frac{dz_j-dz_j'}{z_j-z_j'}\ \in\ \widehat{\mathcal{A}}=\prod_n\mathcal{A}_n,$$
for a Morse representative of $K$, corrected by the value on the hump. $Z$ is universal: for any $v\in\mathcal{V}_n$ there is $w\in\mathcal{A}_n^{*}$ with $v=w\circ Z$ modulo lower degree. Hence completeness $\iff$ $Z$ injective.

$\mathcal{A}=\bigoplus_n\mathcal{A}_n$ is a graded commutative Hopf algebra under connected sum, so $\mathcal{A}\cong S(\mathcal{P})$ with $\mathcal{P}$ the primitives; $\dim\mathcal{P}_n$ counts "multiplicatively independent" invariants.

**Sources of weight systems.** Every finite-dimensional metrized Lie algebra $(\mathfrak{g},\langle,\rangle)$ with a representation $R$ gives $w_{\mathfrak{g},R}:\mathcal{A}_n\to\mathbb{Q}$; $\mathfrak{sl}_2$ with the standard representation recovers the Jones polynomial coefficients. Birman–Lin: substituting $q=e^{h}$ into the Jones, HOMFLY or Kauffman polynomial and expanding in $h$ yields coefficients that are finite type. The Alexander–Conway coefficients $a_n$ in $\nabla_K(z)=\sum a_n z^n$ are finite type of degree $n$.

## 3. History & State of the Art (SOTA)

- **1990.** V. A. Vassiliev introduces the invariants via the spectral sequence of the discriminant in the space of maps $S^1\to\mathbb{R}^3$ (*Cohomology of knot spaces*).
- **1991–93.** M. Goussarov independently develops the theory combinatorially, via $n$-triviality.
- **1993.** Birman–Lin show quantum invariants expand into finite type invariants; the theory is at least as strong as the Jones, HOMFLY and Kauffman polynomials.
- **1993.** Kontsevich constructs $Z$, proving $\mathcal{V}_n/\mathcal{V}_{n-1}\cong\mathcal{A}_n^*$ over $\mathbb{Q}$.
- **1995.** Bar-Natan's *On the Vassiliev knot invariants* systematizes chord diagrams, 4T, Lie-algebraic weight systems, and computes $\dim\mathcal{A}_n$ for $n\le 9$.
- **1997–2000.** Le–Murakami and Bar-Natan–Garoufalidis relate $Z$ to quantum invariants; Kneissler pushes dimension computations to $n=12$.
- **2000.** Habiro's clasper calculus and Goussarov's parallel theory give a *topological* characterization of finite type equivalence.

**Dimension table** ($\dim\mathcal{A}_n$, $n=0,\dots,12$): $1,1,1,2,3,5,8,12,18,27,39,55,80$ for primitives $\mathcal{P}_n$ ($n\ge1$), and $\dim\mathcal{A}_n = 1,1,2,3,6,10,19,33,60,104,184,316,548$.

**Growth bounds.** Lower: $\dim\mathcal{A}_n \ge e^{c\sqrt{n}}$ (Chmutov–Duzhin; Dasbach for primitives). Upper: Chmutov–Duzhin gave $\dim\mathcal{A}_n\le (n-1)!$, improved by Stoimenow and then by Zagier to
$$\dim\mathcal{A}_n \;<\; \frac{n!}{2\,(\ln 2)^{n+1}}\quad\text{asymptotically}.$$
The gap between $e^{c\sqrt n}$ and factorial growth is itself wide open.

## 4. Partial Results / Verified Cases

- **Braids.** Finite type invariants classify braids completely: $Z$ is injective on $B_n$ (Kohno; Bar-Natan; via the Magnus/Milnor filtration of the pure braid group $P_n$, which is residually torsion-free nilpotent).
- **String links up to homotopy.** Milnor's $\bar\mu$-invariants are finite type (Bar-Natan, Lin), and by Habegger–Lin they classify string links up to link homotopy — so finite type invariants are complete there.
- **Knots modulo $n$-equivalence.** Goussarov and Habiro: two knots have the same $\mathbb{Z}$-valued invariants of degree $<n$ **iff** they are $C_n$-equivalent (related by a finite sequence of $C_n$-moves / clasper surgeries). This converts the algebraic filtration into a topological one and is the strongest structural theorem available.
- **Small crossing number.** $Z$ truncated at low degree already separates all prime knots of $\le 10$ crossings (composite Vassiliev data from Jones/HOMFLY/Kauffman coefficients suffices); no failure of separation is known for any tabulated knot pair.
- **Mutation.** Every finite type invariant of degree $\le 10$ takes equal values on mutant knots (Chmutov–Duzhin, via the Kontsevich integral and the $\mathcal{A}$-algebra structure). Conversely, Morton–Cromwell showed the HOMFLY polynomial of the $3$-cable distinguishes the Conway and Kinoshita–Terasaka knots, yielding a degree-$11$ finite type invariant that separates that mutant pair — so mutation is not an obstruction in general.
- **Non-separation phenomena that do occur.** Stanford: inserting a pure braid from the $n$-th lower central series $P_k^{(n)}$ into a knot preserves all invariants of degree $<n$. This produces, for each $n$, infinitely many distinct knots agreeing to degree $<n$ — but not agreeing in *all* degrees.
- **Failure in adjacent settings.** For 3-manifolds and for some quantum settings the analogous "finite type separates" statements are false or unavailable; also, finite type invariants of *links* do not detect all link-homotopy data beyond string links.

## 5. Principal Obstacles

1. **No topological control on $Z$.** $Z$ is defined by iterated integrals on a Morse representative; there is no known geometric reconstruction of $K$ from $Z(K)$. Injectivity proofs elsewhere (braids) rely on residual nilpotence of a group; knots form a monoid, not a group, so the classical Magnus-expansion argument has no direct analogue.
2. **Orientation blindness.** No finite type invariant is known to distinguish a knot from its reverse. Kuperberg showed that completeness forces finite type invariants to detect knot orientation; every known weight system source ($\mathfrak{g}$-weight systems, quantum invariants, Alexander) is reversal-invariant, and non-invertible knots (e.g. $8_{17}$) are undetected by all computed invariants. This is the sharpest concrete threat to the conjecture.
3. **Dimension deficit.** $\dim\mathcal{A}_n$ grows subexponentially in a sense far slower than the number of knots of bounded complexity is believed to grow. Counting arguments are inconclusive, because the filtration is infinite and each degree can carry unbounded information, but no positive counting argument exists either.
4. **Lie algebras do not exhaust $\mathcal{A}^*$.** Vogel constructed weight systems not coming from any semisimple Lie superalgebra, and showed the "universal Lie algebra" $\Lambda$ has zero divisors. So even the classification of weight systems — the linear-algebraic shadow of the problem — is unfinished.
5. **Mutation-type degeneracies.** The Kontsevich integral is insensitive to mutation up to degree 10 and behaves tamely under many satellite/cabling operations; each such invariance is a place where separation could fail, and controlling all of them simultaneously is beyond current technique.
6. **Gauge-theoretic tools do not interface.** Khovanov homology detects the unknot (Kronheimer–Mrowka) and knot Floer homology detects genus and fiberedness, but neither is known to be a limit of finite type invariants, so these detection theorems transfer no information to $\mathcal{V}$.

## 6. The Gap

Proven: $Z$ is injective on braids and on string links up to homotopy; degree-$<n$ agreement is exactly $C_n$-equivalence; no counterexample pair is known among tabulated knots. The general statement asserts injectivity of $Z$ on all of $\mathcal{K}$.

The precise barrier: $C_n$-equivalence classes of knots are computable and finite-index-like objects, but nothing prevents
$$\bigcap_{n\ge 1}\ \{K' : K' \text{ is } C_n\text{-equivalent to } K\}$$
from containing more than $K$. Completeness is exactly the statement that this intersection is a singleton for every $K$ — i.e. that the Goussarov–Habiro filtration of the knot monoid is *separating*, the analogue of residual nilpotence. Proving that requires either (a) a geometric inverse to $Z$, or (b) a residual-nilpotence theorem for a group-like object whose "abelianized layers" are $\mathcal{A}_n$. Neither exists. A single non-invertible knot proven indistinguishable from its reverse by all finite type invariants would settle the problem negatively.

## 7. Current Research (as of June 2026)

- **Clasper/claspers-and-quantum-groups school** (Habiro and successors, Kyoto; Massuyeau, Strasbourg): unified functorial and universal invariants of bottom tangles, refining $Z$ integrally and studying torsion in the Goussarov–Habiro groups.
- **Weight-system computation via combinatorics and machine assistance**: Chmutov, Kazarian, Lando and collaborators have pushed $\mathfrak{gl}_N$ and $\mathfrak{sl}_2$ weight-system evaluation to previously intractable diagram families through recursion relations on chord diagrams. *(frontier — verify)* Reported extensions of $\dim\mathcal{A}_n$ tables beyond $n=12$ remain unconfirmed.
- **Orientation-detection programme**: renewed attempts to build a weight system sensitive to reversal, typically via non-Lie sources (Vogel's $\Lambda$, planar-algebra methods) or via cabling of the Kontsevich integral.
- **Homological knot theory bridge**: attempts to relate perturbative expansions of Khovanov/HOMFLY homology or knot Floer to finite type data; a positive link would import the unknot-detection theorem into $\mathcal{V}$.
- **Configuration-space integrals** (Bott–Taubes, Volić, Koytcheff): the Goodwillie–Weiss embedding calculus tower for $\mathrm{Emb}(S^1,\mathbb{R}^3)$ is conjecturally the finite type filtration; convergence of that tower for $1$-dimensional knots would be a form of completeness. *(frontier — verify)*

## 8. Future Work

- Prove or disprove orientation detection — the cleanest decidable-looking sub-question.
- Settle unknot detection by $Z$ (weaker than full completeness, likely more tractable, and comparable to the still-open Jones unknot-detection problem).
- Establish convergence of the Goodwillie–Weiss tower for classical knots, which would identify the finite type filtration with a homotopy-theoretic limit that separates by construction.
- Develop an integral/torsion refinement: determine whether $\mathbb{Z}$-valued or finite-group-valued finite type invariants (Goussarov–Habiro, Willerton) are strictly stronger than rational ones.
- Complete the classification of weight systems, in particular decide whether Vogel's $\Lambda$-module structure exhausts $\mathcal{A}^*$.
- Search computationally for candidate counterexample pairs among knots with large crossing number and identical HOMFLY, Kauffman and cabled invariants.

## 9. Key References

- **[Foundational]** V. A. Vassiliev. *Cohomology of knot spaces.* In *Theory of Singularities and its Applications* (V. I. Arnold, ed.), Advances in Soviet Mathematics 1, AMS, 1990, 23–69.
- **[Foundational]** M. Kontsevich. *Vassiliev's knot invariants.* Advances in Soviet Mathematics 16 (Part 2), AMS, 1993, 137–150.
- **[Foundational]** D. Bar-Natan. *On the Vassiliev knot invariants.* Topology 34 (1995), 423–472.
- **[Foundational]** J. S. Birman, X.-S. Lin. *Knot polynomials and Vassiliev's invariants.* Inventiones Mathematicae 111 (1993), 225–270.
- **[Structural]** K. Habiro. *Claspers and finite type invariants of links.* Geometry & Topology 4 (2000), 1–83.
- **[Structural]** M. Goussarov. *Finite type invariants and n-equivalence of 3-manifolds.* C. R. Acad. Sci. Paris Sér. I Math. 329 (1999), 517–522.
- **[SOTA / Recent]** P. Vogel. *Algebraic structures on modules of diagrams.* Journal of Pure and Applied Algebra 215 (2011), 1292–1339.
- **[SOTA / Recent]** D. Zagier. *Vassiliev invariants and a strange identity related to the Dedekind eta-function.* Topology 40 (2001), 945–960.
- **[Related]** G. Kuperberg. *Detecting knot invertibility.* Journal of Knot Theory and Its Ramifications 5 (1996), 173–181.
- **[Related]** T. Stanford. *Braid commutators and Vassiliev invariants.* Pacific Journal of Mathematics 174 (1996), 269–276.
- **[Related]** H. R. Morton, P. R. Cromwell. *Distinguishing mutants by knot polynomials.* Journal of Knot Theory and Its Ramifications 5 (1996), 225–238.
- **[Related]** N. Habegger, X.-S. Lin. *The classification of links up to link-homotopy.* Journal of the AMS 3 (1990), 389–419.
- **[Survey]** S. Chmutov, S. Duzhin, J. Mostovoy. *Introduction to Vassiliev Knot Invariants.* Cambridge University Press, 2012.
- **[Survey]** S. Chmutov, S. Duzhin. *The Kontsevich integral.* Acta Applicandae Mathematicae 66 (2001), 155–190.
- **[Survey]** P. M. Kronheimer, T. S. Mrowka. *Khovanov homology is an unknot-detector.* Publications Mathématiques de l'IHÉS 113 (2011), 97–208.

## 10. Worked Example / Concrete Special Case

**Degree 2.** There are exactly two chord diagrams of order 2: two parallel chords $D_{\parallel}$ and two crossing chords $D_{\times}$. The one-term relation kills $D_{\parallel}$ (each chord is isolated), and the 4T relation is vacuous here, so
$$\dim\mathcal{A}_2 = 1,\qquad \mathcal{A}_2=\langle D_\times\rangle .$$
Hence $\dim(\mathcal{V}_2/\mathcal{V}_1)=1$: up to lower degree there is exactly one degree-2 invariant, $v_2$, normalized by $v_2(\text{unknot})=0$ and $\operatorname{symb}(v_2)(D_\times)=1$.

**Realization.** $v_2 = a_2$, the $z^2$-coefficient of the Conway polynomial $\nabla_K(z)$. Compute via the Conway skein $\nabla_{K_+}-\nabla_{K_-}=z\,\nabla_{K_0}$:

- Unknot: $\nabla = 1$, so $v_2 = 0$.
- Trefoil $3_1$: $\nabla = z^2+1$, so $v_2 = 1$.
- Figure-eight $4_1$: $\nabla = 1-z^2$, so $v_2 = -1$.

So a single degree-2 invariant already separates $\{0_1, 3_1, 4_1\}$. Note $v_2(3_1)=v_2(\overline{3_1}^{\,\text{mirror}})=1$: $v_2$ is even, so chirality needs degree 3 ($v_3(3_1)=-1$ vs $+1$ on the mirror, from the $z^0$-normalized Jones expansion).

**Where separation gets hard.** Take the Conway knot $C$ ($11n34$) and the Kinoshita–Terasaka knot $KT$ ($11n42$), a mutant pair. Both have $\nabla = 1$, so all Conway-coefficient invariants agree; in fact
$$v(C) = v(KT)\quad\text{for every finite type }v\text{ with }\deg v \le 10$$
(Chmutov–Duzhin). Separation first occurs at degree 11, using the HOMFLY polynomial of the $3$-parallel (Morton–Cromwell): $P_{C^{(3)}}\ne P_{KT^{(3)}}$, and its $h^{11}$-coefficient is a finite type invariant of degree 11 taking distinct values. This is the conjecture's typical shape — every known "hard" pair eventually separates, but only after climbing many degrees, and no argument bounds that climb uniformly.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*