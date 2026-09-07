---
id: 02-algebra-group-theory/kaplanskys-zero-divisor-conjecture
title: "Kaplansky's Zero Divisor Conjecture"
topic: 02-algebra-group-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Kaplansky's Zero Divisor Conjecture

> **Topic:** Algebra & Group Theory · **ID:** `02-algebra-group-theory/kaplanskys-zero-divisor-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

**Conjecture (Kaplansky).** Let $K$ be a field and $G$ a torsion-free group. Then the group ring $K[G]$ has no zero divisors: if $\alpha,\beta \in K[G]$ and $\alpha\beta = 0$, then $\alpha = 0$ or $\beta = 0$.

Equivalently, $K[G]$ is a domain (it is always unital and associative, generally noncommutative).

The torsion-freeness hypothesis is necessary: if $g \in G$ has order $n > 1$, then
$$(1-g)\bigl(1 + g + \cdots + g^{n-1}\bigr) = 1 - g^{n} = 0,$$
and both factors are nonzero in $K[G]$. So the conjecture asserts that torsion is the *only* source of zero divisors.

A complete proof must handle all fields $K$ (all characteristics, including $\mathbb{F}_p$, where $L^2$/analytic methods are unavailable) and all torsion-free groups, including non-amenable, non-orderable, and non-residually-finite ones. A disproof requires an explicit pair $\alpha,\beta \neq 0$ in some $K[G]$, $G$ torsion-free, with $\alpha\beta = 0$ — a finite, in principle verifiable, certificate.

## 2. Mathematical Foundations

**Group ring.** For a field $K$ and group $G$, $K[G]$ is the $K$-vector space with basis $\{g : g\in G\}$, i.e. finitely supported functions $\alpha : G \to K$, written $\alpha = \sum_{g\in G} \alpha_g\, g$, with multiplication
$$\Bigl(\sum_{g} \alpha_g g\Bigr)\Bigl(\sum_{h} \beta_h h\Bigr) = \sum_{u \in G} \Bigl(\sum_{gh=u} \alpha_g \beta_h\Bigr) u .$$
The **support** is $\operatorname{supp}(\alpha) = \{g : \alpha_g \neq 0\}$.

**The Kaplansky hierarchy.** For $K$ a field and $G$ torsion-free:

1. **Unit conjecture (U):** every unit of $K[G]$ is *trivial*, i.e. of the form $c g$ with $c \in K^\times$, $g \in G$.
2. **Zero divisor conjecture (Z):** $K[G]$ is a domain.
3. **Idempotent conjecture (I):** the only idempotents are $0$ and $1$.

The implications $\mathrm{U} \Rightarrow \mathrm{Z} \Rightarrow \mathrm{I}$ hold. For (Z)$\Rightarrow$(I): if $e^2 = e$ with $e \neq 0,1$ then $e(1-e) = 0$. Statement (U) is **false** (Gardam 2021); (Z) and (I) remain open.

**Unique product property.** $G$ has the **unique product (u.p.)** property if for all finite nonempty $A,B \subseteq G$ there exists $u \in AB$ with a unique factorization $u = ab$, $a \in A$, $b \in B$. If $G$ is u.p. then for $\alpha,\beta \neq 0$ take $A = \operatorname{supp}\alpha$, $B = \operatorname{supp}\beta$; the coefficient of the uniquely represented $u$ in $\alpha\beta$ is $\alpha_a\beta_b \neq 0$, so $\alpha\beta \neq 0$. Hence
$$G \ \text{u.p.} \ \Longrightarrow \ K[G] \ \text{is a domain for every field } K,$$
and the same argument gives (U) via the two-unique-product refinement.

**Orderability.** If $G$ admits a left-invariant total order $<$ (left-orderable), it is u.p.: take the $<$-maximal elements. Bi-orderable groups embed in the Malcev–Neumann series division ring. Bowditch's **diffuse** property (every finite $A$ has an *extremal* point $a$ with $ga, g^{-1}a \notin A$ for all $g\neq 1$) implies u.p. and is implied by left-orderability.

**Analytic reformulation.** For $K \subseteq \mathbb{C}$, embed $\mathbb{C}[G] \hookrightarrow \mathcal{N}(G)$, the group von Neumann algebra acting on $\ell^2(G)$, with trace $\operatorname{tr}(\alpha) = \langle \alpha \delta_e,\delta_e\rangle$. The **strong Atiyah conjecture** for torsion-free $G$ states that $\dim_{\mathcal{N}(G)}\ker(\alpha) \in \mathbb{Z}$ for every $\alpha \in M_{n}(\mathbb{Q}[G])$. Applied to $n=1$: $\dim\ker\alpha \in\{0,1\}$, forcing $\alpha$ injective or zero — exactly (Z) over $\mathbb{Q}$, hence over any field of characteristic $0$ by a standard specialization argument.

## 3. History & State of the Art (SOTA)

- **1940.** Graham Higman's thesis work (*The units of group-rings*, Proc. LMS 1940) proves (U), hence (Z) and (I), for torsion-free groups with a "locally indicable" / ordered structure — the first systematic attack.
- **1950s–60s.** Kaplansky circulates the problems; they appear in print in his 1970 *American Mathematical Monthly* survey "Problems in the theory of rings revisited" as Problems 6–8.
- **1970s.** The polycyclic era: Formanek (1973) for supersolvable groups; K. A. Brown (1976) for torsion-free abelian-by-finite groups over characteristic $0$; Farkas–Snider (1976) for torsion-free polycyclic-by-finite groups, $\operatorname{char} K = 0$, via $K_0$ and the Bass–Swan machinery; Cliff (1980) removes the characteristic hypothesis.
- **1988.** Kropholler–Linnell–Moody extend to torsion-free **elementary amenable** groups (all characteristics).
- **1993.** Linnell proves the strong Atiyah conjecture for groups in the class $\mathcal{C}$ generated by free and elementary amenable groups with a uniform bound on torsion orders — giving (Z) in characteristic $0$ for, e.g., torsion-free groups acting on trees with elementary amenable stabilizers.
- **1987–1988.** Rips–Segev construct the first torsion-free group without the u.p. property; Promislow gives the small example $P$ (the "fours" / Hantzsche–Wendt group), showing u.p. is strictly stronger than (Z).
- **2021.** **Gardam disproves the unit conjecture:** an explicit nontrivial unit of $\mathbb{F}_2[P]$ with support of size $21$ (Annals of Mathematics 194, 2021). Murray (2021) extends this to $\mathbb{F}_p$ for odd $p$. Since $P$ is virtually $\mathbb{Z}^3$, (Z) *holds* for $P$ by Brown/Cliff — the collapse of (U) does not touch (Z), but it removes the main heuristic supporting it.

## 4. Partial Results / Verified Cases

(Z) is a theorem for the following classes of torsion-free $G$:

| Class | Field | Source |
|---|---|---|
| Left-orderable / bi-orderable (incl. free, free nilpotent, surface groups, braid-pure, RAAGs) | all $K$ | Malcev–Neumann; u.p. argument |
| Diffuse groups | all $K$ | Bowditch (2000) |
| Unique product groups generally | all $K$ | folklore |
| Supersolvable | all $K$ | Formanek (1973) |
| Abelian-by-finite | $\operatorname{char} 0$ | Brown (1976) |
| Polycyclic-by-finite | $\operatorname{char} 0$ | Farkas–Snider (1976) |
| Polycyclic-by-finite | all $K$ | Cliff (1980) |
| Elementary amenable | all $K$ | Kropholler–Linnell–Moody (1988) |
| Linnell's class $\mathcal{C}$ (free-by-elementary-amenable, bounded torsion) | $\operatorname{char} 0$ | Linnell (1993) |
| Residually (torsion-free elementary amenable / u.p.) | inherited | direct limit argument |

**Support bounds (computational).** Schweitzer (*J. Group Theory* 16, 2013) showed that if $\alpha\beta = 0$ with $\alpha,\beta \neq 0$ in $K[G]$, $G$ torsion-free, then $|\operatorname{supp}\alpha| + |\operatorname{supp}\beta|$ cannot be small: no counterexample exists with $\min(|\operatorname{supp}\alpha|,|\operatorname{supp}\beta|) \le 3$, and the case $|\operatorname{supp}\alpha| = 4$ forces strong structure (the subgroup generated is a specific two-relator quotient). Related computer searches (Dykema–Heister–Juschenko, *Experimental Mathematics* 24, 2015) exhaust small supports for the direct-finiteness variant.

**Adjacent theorems.** Kaplansky's *direct finiteness* conjecture ($\alpha\beta=1 \Rightarrow \beta\alpha=1$ in $K[G]$, no torsion-freeness needed) is known for all sofic groups (Elek–Szabó 2004); Bartholdi (2019) showed the semiring analogue characterizes amenability. The Kadison–Kaplansky idempotent conjecture for $C^*_r(G)$ follows from injectivity of the Baum–Connes assembly map, known for a-T-menable groups (Higson–Kasparov) and hyperbolic groups (Lafforgue, Mineyev–Yu).

## 5. Principal Obstacles

- **No combinatorial invariant survives.** The u.p. property is the only purely combinatorial route, and it fails for torsion-free groups (Rips–Segev, Promislow, Carter 2014). Worse, there is no known "leading term" substitute: multiplication in a non-orderable group can cancel every candidate maximal product.
- **Gardam's unit removes the heuristic.** Before 2021 the expectation was that supports behave rigidly. A $21$-term unit in $\mathbb{F}_2[P]$ shows that cancellation in a group of *cohomological dimension 3* can be far subtler than any support-counting bound predicts. Support-size induction (Schweitzer) grows super-exponentially in complexity and gives no uniform bound.
- **Characteristic $p$ has no analytic model.** The strongest general tool — the strong Atiyah conjecture via $\dim_{\mathcal{N}(G)}$ and Lück approximation — needs a trace with values in $\mathbb{R}$ and positivity. Over $\mathbb{F}_p$ there is no $\ell^2$-completion, no von Neumann dimension, no spectral measure. Cliff's characteristic-$p$ results rely on polycyclic Noetherian structure, which is unavailable in general.
- **$K$-theoretic methods need finiteness.** Farkas–Snider and Kropholler–Linnell–Moody use $K_0$ of Noetherian or crossed-product decompositions plus Moody's induction theorem. Groups of infinite Hirsch length, infinitely generated groups, or groups with no normal subgroup structure (Tarski monsters' torsion-free analogues, Burger–Mozes lattices, Higman's group) offer no such filtration.
- **Atiyah conjecture is itself false in general.** Grigorchuk–Żuk and Austin produced groups with irrational $L^2$-Betti numbers; Grabowski produced arbitrary reals. So the analytic route cannot be pushed to all torsion-free groups without a torsion-freeness-specific input that nobody has isolated.

## 6. The Gap

Everything proved lives inside two towers: (i) **orderability/u.p.**, and (ii) **amenable-or-elementary-amenable-by-analytic**, extended by Linnell to a bounded amount of free-product structure, and only in characteristic $0$ beyond polycyclic.

The uncrossed step is precisely: **a torsion-free group that is neither u.p. nor built from elementary amenable/free pieces**. Concretely, (Z) is open for
- torsion-free hyperbolic groups over $\mathbb{F}_p$ (open in char $0$ too, in general — the Baum–Connes route gives $C^*_r$ idempotents, not $K[G]$ zero divisors, and does not descend to positive characteristic);
- Thompson's group $F$ (left-orderable, so actually *known*) versus $T$ and $V$ — which have torsion, so out of scope — but torsion-free simple groups such as Burger–Mozes lattices remain open;
- torsion-free groups with Kazhdan property (T) and no order, e.g. torsion-free cocompact lattices in $Sp(n,1)$ over $\mathbb{F}_p$;
- **the Promislow group $P$ over $\mathbb{F}_2$ with arbitrary supports** — (Z) is known here, but the failure of (U) shows the *method* used for (Z) (virtually abelian $K$-theory) is not the reason to believe (Z) in general.

The exact barrier: no invariant is known that (a) is defined for every torsion-free group, (b) is multiplicative or subadditive on supports, and (c) is nonzero on nonzero elements. The u.p. property was such an invariant and it is false; von Neumann dimension is such an invariant and it exists only over $\mathbb{C}$ and only conjecturally takes integer values.

## 7. Current Research (as of June 2026)

- **Post-Gardam search for zero divisors.** Gardam's SAT/Gröbner methodology (encode $\alpha\beta = 0$ over $\mathbb{F}_2$ on a finite ball of $P$ or of other non-u.p. groups as a Boolean satisfiability instance) is being pushed to larger supports and to Rips–Segev-type and Soelberg-type groups. Searches through support size roughly $\le 30$ on $P$ over $\mathbb{F}_2$ report no zero divisor *(frontier — verify)*.
- **Non-u.p. group zoo.** Continued construction of small torsion-free non-u.p. groups (after Promislow, Carter 2014, Soelberg's BYU thesis 2018, Gardam's classification of Gardam-type units by "Passman-index"), aimed at finding one where a zero divisor is plausible.
- **Atiyah/Linnell school.** Linnell, Schick, Lück, Jaikin-Zapirain and collaborators extend the strong Atiyah conjecture and the Hughes-free division ring approach; Jaikin-Zapirain's work on the *free-field* and on $\mathcal{D}_{K[G]}$ (the Hughes-free division ring of fractions) has yielded (Z) for locally indicable groups over arbitrary fields — a genuinely characteristic-free advance via Hughes' theorem on crossed products.
- **Sofic/approximation methods.** Elek–Szabó style linear-sofic and Connes-embedding arguments give direct finiteness in all characteristics for sofic groups; whether soficity can be upgraded to yield (Z) for torsion-free sofic groups is an active question *(frontier — verify)*.
- **Groups:** Oxford (Gardam, Kielak, Fisher), Madrid/ICMAT (Jaikin-Zapirain), Münster/Bonn (Lück, Schick, Löh), Virginia Tech (Linnell), Vanderbilt and Chicago geometric-group-theory groups.

## 8. Future Work

- **Prove (Z) for torsion-free hyperbolic groups.** Suggested route: combine the Baum–Connes machinery (known for hyperbolic groups) with a descent argument to $K[G]$ for arbitrary $K$; the missing ingredient is a characteristic-free analogue of the trace.
- **Extend the Hughes-free division ring approach.** Locally indicable is now handled; the target is amenable-by-locally-indicable, and eventually any torsion-free group with a "sufficiently free" Bass–Serre or $L^2$-acyclic structure.
- **Find or rule out a zero divisor in $\mathbb{F}_2[P]$.** Gardam's unit means $P$ is the sharpest laboratory. A theorem "no zero divisors in $K[P]$ of support $\le N$ for all $N$" via the virtually-$\mathbb{Z}^3$ structure already exists; the value is in understanding *which* structural feature blocks zero divisors but not units.
- **Isolate the right weakening.** Many authors now consider (I), the idempotent conjecture, the more likely of the three to be true in full generality; separating (Z) from (I) — finding a group ring with zero divisors but no nontrivial idempotents — would itself be a major result.
- **Positive characteristic invariants.** Develop a Sylvester rank function or a $p$-adic/Lück-approximation analogue over $\mathbb{F}_p$ with integrality; Jaikin-Zapirain's Sylvester matrix rank functions are the leading candidate.

## 9. Key References

- **[Foundational]** G. Higman. *The units of group-rings.* Proceedings of the London Mathematical Society (2) **46** (1940), 231–248.
- **[Foundational]** I. Kaplansky. *Problems in the theory of rings revisited.* American Mathematical Monthly **77** (1970), 445–454.
- **[Foundational]** D. S. Passman. *The Algebraic Structure of Group Rings.* Wiley-Interscience, 1977.
- E. Formanek. *The zero divisor question for supersolvable groups.* Bulletin of the Australian Mathematical Society **9** (1973), 69–71.
- K. A. Brown. *On zero divisors in group rings.* Bulletin of the London Mathematical Society **8** (1976), 251–256.
- D. R. Farkas and R. L. Snider. *$K_0$ and Noetherian group rings.* Journal of Algebra **42** (1976), 192–198.
- G. H. Cliff. *Zero divisors and idempotents in group rings.* Canadian Journal of Mathematics **32** (1980), 596–602.
- P. H. Kropholler, P. A. Linnell and J. A. Moody. *Applications of a new K-theoretic theorem to soluble group rings.* Proceedings of the American Mathematical Society **104** (1988), 675–684.
- E. Rips and Y. Segev. *Torsion-free group without unique product property.* Journal of Algebra **108** (1987), 116–126.
- S. D. Promislow. *A simple example of a torsion-free, non-unique product group.* Bulletin of the London Mathematical Society **20** (1988), 302–304.
- P. A. Linnell. *Division rings and group von Neumann algebras.* Forum Mathematicum **5** (1993), 561–576.
- B. H. Bowditch. *A variation on the unique product property.* Journal of the London Mathematical Society **62** (2000), 813–826.
- G. Elek and E. Szabó. *Sofic groups and direct finiteness.* Journal of Algebra **280** (2004), 426–434.
- W. Lück. *$L^2$-Invariants: Theory and Applications to Geometry and K-Theory.* Springer, Ergebnisse der Mathematik **44**, 2002.
- **[SOTA / Recent]** G. Gardam. *A counterexample to the unit conjecture for group rings.* Annals of Mathematics **194** (2021), 967–979.
- **[SOTA / Recent]** A. G. Murray. *More counterexamples to the unit conjecture for group rings.* arXiv:2106.02147 (2021).
- M. Schweitzer. *On zero divisors with small support in group rings of torsion-free groups.* Journal of Group Theory **16** (2013), 667–693.
- K. Dykema, T. Heister and K. Juschenko. *Finitely presented groups related to Kaplansky's direct finiteness conjecture.* Experimental Mathematics **24** (2015), 326–338.
- L. Bartholdi. *Amenability of groups is characterized by Myhill's theorem.* Journal of the European Mathematical Society **21** (2019), 3191–3197.
- **[Survey]** D. S. Passman. *Group rings, crossed products and Galois theory.* CBMS Regional Conference Series in Mathematics **64**, AMS, 1986.

## 10. Worked Example / Concrete Special Case

**(a) The abelian case $G = \mathbb{Z}$, by leading terms.** $K[\mathbb{Z}] = K[t,t^{-1}]$. Let $\alpha = \sum_{i=m}^{M} a_i t^i$ with $a_m, a_M \neq 0$ and $\beta = \sum_{j=n}^{N} b_j t^j$ with $b_n, b_N \neq 0$. The coefficient of $t^{M+N}$ in $\alpha\beta$ is
$$\sum_{i+j = M+N} a_i b_j = a_M b_N \neq 0,$$
because every other pair $(i,j)$ with $i+j = M+N$ has $i>M$ or $j>N$, hence a zero factor. So $\alpha\beta \neq 0$. This is exactly the u.p. argument with $A = \operatorname{supp}\alpha$, $B = \operatorname{supp}\beta$, unique product $t^{M+N}$. The same proof works verbatim for any bi-ordered $G$ using the order-maximal elements — this is how free groups, surface groups and torsion-free nilpotent groups are handled.

**(b) Why torsion breaks it.** Take $G = \mathbb{Z}/3 = \langle g \rangle$, $K = \mathbb{Q}$. Then
$$(1-g)(1+g+g^2) = 1 + g + g^2 - g - g^2 - g^3 = 1 - 1 = 0 .$$
Both factors have support size $3$ and $2$; the group has a "wrap-around" so no product is uniquely represented in $\{1,g\}\cdot\{1,g,g^2\}$.

**(c) The Promislow group: u.p. fails, but no zero divisor is known.** Let
$$P = \langle a,b \mid a^{-1}b^2a = b^{-2},\; b^{-1}a^2b = a^{-2}\rangle,$$
the fundamental group of the Hantzsche–Wendt flat $3$-manifold. $P$ is torsion-free and contains $\mathbb{Z}^3 = \langle a^2, b^2, (ab)^2\rangle$ with index $4$. Promislow's $14$-element set
$$S = \{\,a,\,a^{-1},\,b,\,b^{-1},\,ab,\,(ab)^{-1},\,a^2b,\,\ldots\,\} \subset P$$
(the union of $\{x^{\pm1}\}$ over $x \in \{a,b,ab,ab^{-1}\}$ together with $\{a^2b^{\pm1}, b^2a^{\pm1}, \ldots\}$, $|S|=14$) satisfies: **every** element of $S\cdot S$ has at least two factorizations. So $P$ is not u.p., and the leading-term method dies.

Yet $K[P]$ **is** a domain for every field $K$: $P$ is torsion-free polycyclic-by-finite (virtually $\mathbb{Z}^3$), so Farkas–Snider (char $0$) and Cliff (char $p$) apply.

Gardam's unit lives here. Writing $P = \mathbb{Z}^3 \rtimes (\mathbb{Z}/2)^2$ with coset representatives $1, x, y, z$ over $\mathbb{Z}^3 = \langle X,Y,Z\rangle$, he exhibits
$$p = \alpha_1 + \alpha_x x + \alpha_y y + \alpha_z z \in \mathbb{F}_2[P], \qquad |\operatorname{supp}(p)| = 21,$$
with an explicit $q$ of support $21$ such that $pq = 1$ while $p \neq cg$. So in the *same* ring $\mathbb{F}_2[P]$ where the unit conjecture fails, the zero divisor conjecture holds — the failure is confined to the multiplicative group of units. This is the precise sense in which the 2021 counterexample destroyed the strongest evidence for (Z) without producing a counterexample to it.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*