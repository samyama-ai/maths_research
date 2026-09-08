---
id: 04-topology/crossing-number-additivity-general
title: "Additivity of Crossing Number Under Connected Sum"
topic: 04-topology
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Additivity of Crossing Number Under Connected Sum

> **Topic:** Topology & Knot Theory · **ID:** `04-topology/crossing-number-additivity-general` · **Status:** open

## 1. Problem Statement / Conjecture

Let $c(K)$ denote the crossing number of a knot $K \subset S^3$: the minimum number of double points over all regular planar diagrams of $K$. Let $K_1 \\# K_2$ denote the connected sum (oriented, hence well defined).

**Conjecture (crossing number additivity).** For all knots $K_1, K_2$,
$$c(K_1 \\# K_2) = c(K_1) + c(K_2).$$

The inequality $c(K_1 \\# K_2) \le c(K_1) + c(K_2)$ is immediate: juxtapose minimal diagrams and splice. The open content is the lower bound
$$c(K_1 \\# K_2) \ \ge\ c(K_1) + c(K_2).$$

A proof must handle arbitrary summands, including non-alternating, non-adequate, non-fibered knots. A disproof requires an explicit pair $K_1, K_2$ together with a diagram $D$ of $K_1 \\# K_2$ having $c(D) < c(K_1) + c(K_2)$ and a certified computation of $c(K_1), c(K_2)$ — the hard half, since crossing number has no known algorithm of practical reach beyond tabulated ranges.

The same statement is conjectured for links, and extends to $n$ summands: $c(K_1 \\# \cdots \\# K_n) = \sum_i c(K_i)$.

## 2. Mathematical Foundations

**Diagrams.** A diagram $D$ of $K$ is the image of a generic projection $S^3 \setminus \{\ast\} \to \mathbb{R}^2$, a 4-valent plane graph with over/under decoration at each vertex. $c(D) = |V(D)|$ and $c(K) = \min_D c(D)$.

**Connected sum.** Given $K_1, K_2$ with chosen orientations, $K_1 \\# K_2$ is obtained by removing a trivial arc from each and gluing along a sphere $S$ meeting the knot in two points. Schubert's theorem: every knot factors uniquely (up to order) into primes under $\\#$.

**Additive invariants for comparison.** Several classical invariants *are* known to be additive:
- Seifert genus: $g(K_1 \\# K_2) = g(K_1) + g(K_2)$ (Schubert 1949).
- Bridge number: $b(K_1 \\# K_2) = b(K_1) + b(K_2) - 1$ (Schubert 1954).
- Braid index: $\mathrm{braid}(K_1 \\# K_2) = \mathrm{braid}(K_1) + \mathrm{braid}(K_2) - 1$ (Birman–Menasco 1990).
- Polynomial invariants are multiplicative: $V(K_1\\#K_2) = V(K_1)V(K_2)$, $P(K_1\\#K_2)=P(K_1)P(K_2)$, so their **spans are additive**.

**The Kauffman bracket bound.** For any diagram $D$ of a link $L$, the Kauffman–Murasugi–Thistlethwaite theorem gives
$$\operatorname{span} V(L) \ \le\ c(L),$$
with equality when $L$ admits a reduced alternating diagram, and more generally when $L$ is adequate. Here $\operatorname{span}$ is the difference between top and bottom degrees in $q$ (or $t$), normalized so that $\operatorname{span} V$ of the reduced alternating $n$-crossing diagram is $n$.

Define the class
$$\mathcal{S} = \{\, K : \operatorname{span} V(K) = c(K) \,\} \quad (\text{"span-tight" knots}).$$
Additivity of $\operatorname{span}$ plus the KMT bound immediately gives additivity on $\mathcal{S}$ (Section 10).

**Positive braids.** If $K$ is the closure of a positive braid on $b$ strands with $\ell$ letters, then $\ell = 2g(K) + b - 1$ by Bennequin, and the Morton–Franks–Williams inequality is sharp; for torus knots this pins $c(K)$ exactly, and both $g$ and $b-1$ are additive.

**Best general lower bound (Lackenby 2009).** There is a universal constant such that
$$c(K_1 \\# \cdots \\# K_n) \ \ge\ \frac{1}{152}\sum_{i=1}^{n} c(K_i).$$

## 3. History & State of the Art (SOTA)

- **1877–1885.** P. G. Tait tabulates knots by crossing number and treats minimal crossing number as the organizing complexity measure. Additivity is folklore from this era; no proof is offered.
- **1949–1954.** Schubert establishes unique prime factorization and additivity of genus and bridge number — the template additivity results, both proved by *3-manifold* (essential surface) arguments, not diagrammatic ones.
- **1987.** Kauffman, Murasugi, and Thistlethwaite independently prove the Tait conjecture that reduced alternating diagrams are minimal, via the bracket-span bound. This settles additivity for alternating summands.
- **1988.** Lickorish and Thistlethwaite extend minimality to *adequate* diagrams, enlarging the class.
- **2003–2004.** Gruber gives crossing-number estimates for connected sums via polynomial breadths; Diao proves exact additivity for connected sums of torus knots (and more generally sums whose summands have crossing number determined by braid-theoretic data).
- **2009.** Lackenby proves the first universal linear lower bound with constant $1/152$, using normal-surface / essential-sphere arguments applied to the complement of a minimal diagram rather than diagrammatic combinatorics alone. This remains the SOTA for arbitrary summands.
- **2014.** Lackenby proves the analogous satellite statement, $c(\text{satellite}) \ge c(\text{companion})/10^{13}$, showing the method is general but the constants are far from tight.
- **2020.** Malyutin shows the additivity conjecture is *not* logically independent of tabulation heuristics: it is incompatible with the widely believed statement that the proportion of alternating knots among prime knots with at most $n$ crossings tends to $0$. At least one of the two must fail.

The conjecture appears in Kirby's problem list and in Adams' *The Knot Book* as one of the oldest unresolved statements in knot theory.

## 4. Partial Results / Verified Cases

Additivity $c(K_1 \\# K_2) = c(K_1)+c(K_2)$ is **proved** when:

1. **Both summands are alternating** (Kauffman–Murasugi–Thistlethwaite 1987). Extends to $n$ alternating summands.
2. **Both summands are adequate** — in particular $+$adequate and $-$adequate diagrams, covering all Montesinos knots with suitable parameters and most tabulated knots through 12 crossings (Lickorish–Thistlethwaite 1988).
3. **Both summands lie in $\mathcal{S}$** (span-tight), a class containing (1) and (2) and closed under $\\#$.
4. **Both summands are torus knots** (Diao 2004); more generally, positive braid closures where MFW is sharp and $c = 2g + b - 1$.
5. **Mixed sums** where each summand independently lies in $\mathcal S$ — the classes need not match.

**Weaker general facts.** For arbitrary knots: $c(K_1\\#K_2) \ge \tfrac{1}{152}(c(K_1)+c(K_2))$ (Lackenby 2009); $c(K_1\\#K_2) \ge 2g(K_1)+2g(K_2)+1$ from genus additivity and $2g(D) \le c(D)-1$; and $c(K_1 \\# K_2) \ge 3(\mathrm{braid}(K_1)+\mathrm{braid}(K_2)-2)$ from braid-index additivity.

**Computational range.** Prime knot tables are complete to 16 crossings (Hoste–Thistlethwaite–Weeks, 1.7 million knots) and to 19 crossings (Burton 2020, ~350 million). No composite knot in any exhaustive diagram enumeration performed to date has a diagram beating $c(K_1)+c(K_2)$.

**Not known.** Even $c(K_1 \\# K_2) \ge \max\{c(K_1), c(K_2)\}$ is open in general — the $1/152$ bound does not imply it.

## 5. Principal Obstacles

- **No lower-bound machinery for crossing number.** Genus, bridge number, and braid index are defined by minimizing over *surfaces or braid axes*, objects that a decomposing sphere can be made transverse to, enabling innermost-disk induction. Crossing number minimizes over *projections*; a minimal diagram of $K_1\\#K_2$ carries no canonical surface to cut along, so the standard 3-manifold argument has nothing to grip.
- **The decomposing sphere need not be visible.** In a minimal diagram $D$ of $K_1\\#K_2$ there is no reason the factorizing sphere intersects the projection plane in a single circle meeting $D$ in two points. Lackenby's proof controls this only up to a bounded multiplicative loss — hence the constant $152$.
- **Polynomial bounds are class-limited.** $\operatorname{span} V \le c$ is additive and clean, but the gap $c(K) - \operatorname{span} V(K)$ is unbounded (torus knots: $c(T_{2,n})=n$ versus span growth for larger $T_{p,q}$ is far off). Once a summand leaves $\mathcal{S}$, the argument gives nothing. HOMFLY and Khovanov-homology width bounds fail for the same reason: they too are additive-but-slack.
- **Crossing number is not computable in practice.** No algorithm certifies $c(K)$ for an arbitrary large knot; verifying a putative counterexample is as hard as the conjecture.
- **Non-monotonicity elsewhere.** Unknotting number additivity is likewise open, tunnel number is provably *sub*-additive with degeneration, and crossing number is known to be non-additive for *spatial graphs* and for knots in general 3-manifolds — so no soft reason forces additivity here.

## 6. The Gap

Proven: additivity whenever both summands belong to a class on which some additive lower bound $\lambda$ (with $\lambda \le c$ always) is *sharp*: $\lambda(K_i)=c(K_i)$. All of $\mathcal S$, torus knots, adequate knots arise this way.

Conjectured: additivity with no sharpness hypothesis.

The precise gap is the existence of a lower bound for $c$ that is (i) additive under $\\#$ and (ii) sharp for *every* knot — or, avoiding that, a purely topological argument showing that a minimal diagram of a composite knot can always be isotoped so that a factorizing sphere meets it in exactly two points, without the bounded-loss step. Closing the constant from $1/152$ to $1$ is the whole problem: every intermediate constant $\kappa < 1$ is a quantitative improvement, not a resolution, though $\kappa = 1$ for $n=2$ suffices for all $n$ by induction.

## 7. Current Research (as of June 2026)

- **Lackenby's program (Oxford).** Continued refinement of normal-surface and thin-position arguments in diagram complements, aiming to reduce the $152$ constant; incremental improvements to small constants have been circulated, none reaching $1$. *(frontier — verify)*
- **Malyutin's incompatibility line (St. Petersburg / PDMI).** The 2020 IMRN result reframes additivity as a statement about the asymptotic census of knots. Follow-up work studies whether the density of alternating knots can be estimated directly, which would decide additivity by contradiction *(frontier — verify)*.
- **Large-scale enumeration.** Burton's *Regina*-based tabulation to 19 crossings and successor projects give a search space in which a composite counterexample would be detectable; ongoing work extends certified diagram enumeration and invariant separation.
- **Machine-assisted diagram minimization.** Reinforcement-learning agents searching Reidemeister sequences (following the DeepMind knot-theory line and successors) have been applied to composite diagrams as a counterexample hunt; no reduction below $c_1+c_2$ has been reported *(frontier — verify)*.
- **Khovanov and HOMFLY width.** Attempts to replace $\operatorname{span} V$ by categorified additive quantities with smaller slack.

## 8. Future Work

- Identify an additive lower bound sharp on a class strictly larger than adequate knots — e.g. all knots with a "semi-adequate up to a bounded defect" diagram.
- Prove $c(K_1\\#K_2)\ge \max\{c(K_1),c(K_2)\}$, currently unknown, as a first structural step.
- Push Lackenby's constant to $\kappa > 1/2$; a constant above $1/2$ already rules out large classes of hypothetical counterexamples.
- Settle the alternating-density question of Malyutin, which decides additivity or the census conjecture.
- Test additivity on connected sums of the least tractable known knots — non-adequate, non-fibered, low-volume hyperbolic knots at 15–19 crossings — with certified minimality.

## 9. Key References

- **[Foundational]** Schubert, H. *Die eindeutige Zerlegbarkeit eines Knotens in Primknoten.* Sitzungsberichte der Heidelberger Akademie der Wissenschaften, 1949.
- **[Foundational]** Schubert, H. *Über eine numerische Knoteninvariante.* Mathematische Zeitschrift 61 (1954), 245–288.
- **[Foundational]** Kauffman, L. H. *State models and the Jones polynomial.* Topology 26 (1987), 395–407.
- **[Foundational]** Murasugi, K. *Jones polynomials and classical conjectures in knot theory.* Topology 26 (1987), 187–194.
- **[Foundational]** Thistlethwaite, M. B. *A spanning tree expansion of the Jones polynomial.* Topology 26 (1987), 297–309.
- **[Foundational]** Lickorish, W. B. R.; Thistlethwaite, M. B. *Some links with non-trivial polynomials and their crossing-numbers.* Commentarii Mathematici Helvetici 63 (1988), 527–539.
- **[Foundational]** Birman, J. S.; Menasco, W. W. *Studying links via closed braids IV: composite links and split links.* Inventiones Mathematicae 102 (1990), 115–139.
- **[SOTA / Recent]** Lackenby, M. *The crossing number of composite knots.* Journal of Topology 2 (2009), 747–768.
- **[SOTA / Recent]** Lackenby, M. *The crossing number of satellite knots.* Algebraic & Geometric Topology 14 (2014), 2379–2409.
- **[SOTA / Recent]** Diao, Y. *The additivity of crossing numbers.* Journal of Knot Theory and Its Ramifications 13 (2004), 857–866.
- **[SOTA / Recent]** Malyutin, A. V. *On the question of genericity of hyperbolic knots.* International Mathematics Research Notices, 2020, no. 21, 7792–7828.
- **[SOTA / Recent]** Burton, B. A. *The next 350 million knots.* Proceedings of the 36th International Symposium on Computational Geometry (SoCG 2020), LIPIcs vol. 164.
- **[Survey]** Adams, C. C. *The Knot Book: An Elementary Introduction to the Mathematical Theory of Knots.* W. H. Freeman, 1994; reprinted AMS, 2004.
- **[Survey]** Lickorish, W. B. R. *An Introduction to Knot Theory.* Graduate Texts in Mathematics 175, Springer, 1997.
- **[Survey]** Cromwell, P. R. *Knots and Links.* Cambridge University Press, 2004.
- **[Survey]** Hoste, J.; Thistlethwaite, M.; Weeks, J. *The first 1,701,936 knots.* The Mathematical Intelligencer 20 (1998), 33–48.

## 10. Worked Example / Concrete Special Case

**Claim.** For the granny knot $G = 3_1 \\# 3_1$ (two right trefoils), $c(G) = 6$.

*Step 1 — upper bound.* Splicing two standard 3-crossing trefoil diagrams gives a 6-crossing diagram, so $c(G) \le 6$.

*Step 2 — the Jones polynomial.* For the right-handed trefoil,
$$V(3_1) = -t^{-4} + t^{-3} + t^{-1},$$
so top degree $-1$, bottom degree $-4$, and $\operatorname{span} V(3_1) = 3$.

*Step 3 — multiplicativity.* $V(K_1\\#K_2) = V(K_1)\,V(K_2)$, hence
$$V(G) = \left(-t^{-4}+t^{-3}+t^{-1}\right)^2 = t^{-8} - 2t^{-7} + t^{-6} - 2t^{-5} + 2t^{-4} + t^{-2},$$
with top degree $-2$, bottom degree $-8$, so $\operatorname{span} V(G) = 6$.

*Step 4 — the KMT bound.* For any link, $\operatorname{span} V(L) \le c(L)$. Therefore $c(G) \ge 6$.

*Conclusion.* $6 \le c(G) \le 6$, so $c(G) = 6 = c(3_1) + c(3_1)$. The same computation gives $c(\\#^n 3_1) = 3n$ for all $n$, and the identical argument applies verbatim to the square knot $3_1 \\# \overline{3_1}$.

**Why this does not generalize.** The argument used only that $\operatorname{span} V(3_1) = c(3_1) = 3$. Take instead a summand $K$ with $\operatorname{span} V(K) = c(K) - d$ for some defect $d > 0$ (any non-adequate knot; defects grow without bound over the tabulated 15- and 16-crossing non-alternating knots). Then for $K_1, K_2$ with defects $d_1, d_2$ the method yields only
$$c(K_1\\#K_2) \ \ge\ c(K_1)+c(K_2) - (d_1+d_2),$$
which is vacuous as soon as $d_1 + d_2$ is comparable to $\min\{c(K_1), c(K_2)\}$. Replacing $V$ by HOMFLY or Khovanov width shrinks $d$ on some families but never to $0$ on all knots — that residual defect is exactly The Gap of Section 6.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*