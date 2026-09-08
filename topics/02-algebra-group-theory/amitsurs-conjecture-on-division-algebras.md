---
id: 02-algebra-group-theory/amitsurs-conjecture-on-division-algebras
title: "Amitsur's Conjecture on Rational Identities of Division Rings"
topic: 02-algebra-group-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Amitsur's Conjecture on Rational Identities of Division Rings

> **Topic:** Algebra & Group Theory · **ID:** `02-algebra-group-theory/amitsurs-conjecture-on-division-algebras` · **Status:** open

## 1. Problem Statement / Conjecture

A *rational identity* of a division ring $D$ is a rational expression in noncommuting variables that vanishes at every point of $D^n$ where it is defined (its domain being nonempty). Amitsur (1966) proved that the rational identities of a division ring are governed by one integer — its degree over the center — **provided the center is infinite**:

> **Theorem (Amitsur).** Let $D$ be a division ring with center $C$, $|C| = \infty$. If $\dim_C D = \infty$, then every rational identity of $D$ holds in *every* division ring. If $\dim_C D = n^2 < \infty$, the rational identities of $D$ are exactly the rational identities of $M_n(F)$ for any infinite field $F$.

The conjecture is that this dichotomy is the whole truth, in the two directions where Amitsur's proof does not reach:

- **(A) Finite-center case.** If $D$ is a division ring whose center $C$ is finite (so $\dim_C D = \infty$, by Wedderburn's little theorem), does $D$ satisfy only the trivial rational identities — those valid in the free field?
- **(B) Generalized identities.** Characterize the division rings satisfying a nontrivial *generalized* rational identity, i.e. one whose coefficients are allowed to lie in $D$ rather than in $C$. Bergman (1976) showed that the naive extension of Amitsur's theorem is false here; no classification replaces it.

A complete solution of (A) is: a proof that $\dim_C D = \infty$ forces triviality with no cardinality hypothesis on $C$, or an explicit division ring with finite center together with a rational expression that is defined somewhere on it, vanishes identically there, and fails on some other division ring. A solution of (B) is a structural criterion on $D$ (in the style of Amitsur's GPI theorem for *polynomial* generalized identities) equivalent to the existence of a nontrivial generalized rational identity.

## 2. Mathematical Foundations

Let $k$ be a commutative field and $X = \{x_1,\dots,x_m\}$. The set of **rational expressions** over $k$ in $X$ is defined recursively: every $x_i$ and every $\alpha \in k$ is a rational expression; if $r,s$ are, so are $r+s$, $rs$, and $r^{-1}$.

For a $k$-algebra division ring $D$, the **domain of definition** $\operatorname{dom}_D(r) \subseteq D^m$ is defined recursively by
$$\operatorname{dom}_D(r+s)=\operatorname{dom}_D(r)\cap\operatorname{dom}_D(s),\qquad
\operatorname{dom}_D(r^{-1})=\{a\in\operatorname{dom}_D(r): r(a)\neq 0\}.$$
$r$ is a **rational identity of $D$** if $\operatorname{dom}_D(r)\neq\varnothing$ and $r(a)=0$ for all $a\in\operatorname{dom}_D(r)$. It is a **generalized** rational identity if coefficients from $D$ are permitted in the construction.

**Free field.** Amitsur constructed, and P. M. Cohn identified functorially, the **universal skew field of fractions** $k\!\left(\!\left<X\right>\!\right)$ of the free algebra $k\langle X\rangle$: every full matrix over $k\langle X\rangle$ becomes invertible there, and every homomorphism of $k\langle X\rangle$ into a division ring that is *honest* factors through it. Cohn's criterion: a square matrix $A$ over $k\langle X\rangle$ is invertible in the free field iff $A$ is **full**, i.e. $A \neq BC$ with $B \in k\langle X\rangle^{n\times r}$, $C\in k\langle X\rangle^{r\times n}$, $r<n$. A rational expression is a **trivial identity** exactly when it maps to $0$ in $k\!\left(\!\left<X\right>\!\right)$.

**Linearization / realization.** Every rational expression $r$ admits a linear representation
$$r(x) = c^{\top} L(x)^{-1} b, \qquad L(x) = A_0 + \sum_{i=1}^m A_i x_i,\quad A_i \in k^{d\times d},$$
with $b,c \in k^d$ (Cohn; Hrubeš–Wigderson). Hence $r$ is a nontrivial rational function iff the pencil $L$ is *full* over the free field, which reduces identity testing to computing the **noncommutative rank**
$$\operatorname{ncrank}(L) = \max_{s\ge 1} \tfrac{1}{s}\operatorname{rank}\bigl(A_0\otimes I_s + \textstyle\sum_i A_i \otimes Y_i\bigr),\quad Y_i \in k^{s\times s} \text{ generic}.$$

**Degree filtration.** For $\dim_C D = n^2$, evaluation on $D$ factors through $M_n$ after scalar extension $D\otimes_C \bar C \cong M_n(\bar C)$, so the identities of $D$ are the *$n\times n$ rational identities*: expressions vanishing on a Zariski-dense open subset of $M_n(\bar C)^m$. These form a strictly decreasing chain as $n$ grows, with intersection the trivial identities. The infinite-center hypothesis enters precisely here: Amitsur's argument is a Zariski-density/specialization argument on the affine variety $M_n(\bar C)^m$, which needs infinitely many scalars.

## 3. History & State of the Art (SOTA)

- **1953–1965.** Amitsur's GPI theorem: a primitive ring satisfies a nontrivial generalized polynomial identity iff it has a minimal one-sided ideal whose endomorphism division ring is finite-dimensional over the center (Amitsur, *Generalized polynomial identities and pivotal monomials*, 1965). This is the polynomial shadow of the rational problem.
- **1966.** Amitsur, *Rational identities and applications to algebra and geometry*, J. Algebra **3**, 304–359: the free field of rational expressions is built, the dichotomy above is proved for infinite center, and the corollary is drawn that two division rings with infinite centers satisfy the same rational identities iff they have equal (possibly infinite) degree.
- **1971–1985.** Cohn's theory of free ideal rings and universal fields of fractions gives the fullness criterion and the canonical model for the trivial identities (*Free Rings and their Relations*, 1971/1985; *Skew Fields*, 1995).
- **1976.** Bergman, *Rational relations and rational identities in division rings I, II*, J. Algebra **43**: systematic study of relations valid on a division ring, including coefficients from $D$; shows that the clean degree-classification collapses for generalized rational identities, and that domains of definition behave far worse than in the central-coefficient case.
- **2015–2018.** The computational face: Hrubeš–Wigderson formalize noncommutative circuits with division and reduce rational identity testing (RIT) to fullness of a linear pencil; Garg–Gurvits–Oliveira–Wigderson give a deterministic polynomial-time algorithm for RIT in characteristic $0$ (operator scaling); Ivanyos–Qiao–Subrahmanyam and Derksen–Makam give alternative algorithms and degree bounds.

Current state: the infinite-center theorem is definitive and unimproved; the finite-center case (A) and generalized case (B) are exactly where the subject has stood since 1976.

## 4. Partial Results / Verified Cases

- **Infinite center, any degree** — completely solved (Amitsur 1966). Covers all division algebras over $\mathbb{Q}, \mathbb{R}, \mathbb{C}$, number fields, $p$-adic fields, and all fields of characteristic $0$.
- **Degree $n=1$**: $D$ commutative; the identity $xy-yx=0$ is the generating nontrivial identity.
- **Degree $n=2$** (quaternion algebras): identities generated by $[(xy-yx)^2, z]=0$ (the $2\times2$ trace-zero-square phenomenon), plus $\mathrm{S}_4(x_1,\dots,x_4)=0$ (Amitsur–Levitzki for $M_2$).
- **Finite-dimensional case, all $n$**: identities of $D$ with $\dim_C D=n^2$ are computable in principle from the invariant theory of $M_n$; every nontrivial polynomial identity of $M_n$ (degree $\ge 2n$, Amitsur–Levitzki bound $S_{2n}=0$) is a rational identity.
- **Trivial identities, effective version**: whether a rational expression is a trivial identity is decidable — and in deterministic polynomial time over $\mathbb{Q}$ (GGOW 2016), with singly-exponential-free bounds via Derksen–Makam's $O(n^2)$ degree bound for matrix semi-invariants.
- **Finite center, restricted shapes**: rational expressions of "inverse height" $1$ (i.e. $p(x)q(x)^{-1}$ with $p,q$ polynomial) satisfy the dichotomy over any center, since a nonzero polynomial in $k\langle X\rangle$ with $k$ finite still fails to vanish on any infinite-dimensional $D$ by Amitsur's GPI theorem. The obstruction begins at height $\ge 2$.

## 5. Principal Obstacles

- **Loss of Zariski density.** Amitsur's proof specializes $x_i$ to generic matrices and uses that a rational function vanishing on a dense open subset of $M_n(\bar C)^m$ vanishes identically. Over a finite center, $C^m$ has finitely many points, "generic" is meaningless, and the algebraic-geometry engine simply has no input. This is not a technical annoyance: over $\mathbb{F}_q$, nonzero polynomials can vanish on the whole space.
- **Domains are not open sets.** For a rational expression of inverse height $h$, $\operatorname{dom}_D(r)$ is an $h$-fold nested complement of zero sets. Klep–Volčič showed such *free loci* are determinantal hypersurfaces of linear pencils; over a finite center these need not be "small" in any usable sense, so "vanishes on its domain" can be a vacuous-looking but nonempty condition.
- **No transfer to a larger center.** The obvious fix — replace $D$ by $D\otimes_C C(t)$, which has infinite center and the same degree — only transports identities *downward*. An identity of $D$ need not survive to $D(t)$, so Amitsur's theorem gives no information about $D$ itself.
- **Generalized coefficients break fullness.** With coefficients in $D$, the linear pencil $L(x)=A_0+\sum A_i x_i$ has entries in $D$, and $\operatorname{ncrank}$ over a noncommutative coefficient ring has no known Cohn-style fullness criterion. Bergman's counterexamples show that the answer genuinely depends on finer invariants of $D$ (e.g. subfields, valuations) than the degree.
- **Positive characteristic in the algorithmic route.** Operator scaling proofs use the characteristic-$0$ Lie-algebraic invariant $\log\det$; deterministic RIT in characteristic $p$ remains open, so even the "trivial identity" side of the finite-center problem lacks an effective handle in the relevant characteristic.

## 6. The Gap

Proven: for $|C|=\infty$, $\dim_C D=\infty \Rightarrow$ only trivial identities. Conjectured: the same implication with the hypothesis $|C|=\infty$ deleted.

The single step to be crossed is a **substitution principle over finite fields**: given a nonfull linear pencil-free rational expression $r$ (nonzero in the free field) and an infinite-dimensional division ring $D$ with $|Z(D)| = q < \infty$, produce a point $a\in \operatorname{dom}_D(r)$ with $r(a)\neq 0$. Amitsur produces $a$ by a density argument; what is needed is a *constructive* or *counting* argument, e.g. a noncommutative Schwartz–Zippel lemma valid over $\mathbb{F}_q$ where the "sample set" is a set of matrices of large enough size rather than scalars. Since $\operatorname{ncrank}$ is computed by a *matrix* substitution of size $s$, and $M_s(\mathbb{F}_q)$ is large even though $\mathbb{F}_q$ is not, the plausible route is to trade scalar genericity for dimension genericity — but the embedding of a suitable $M_s$ into an arbitrary infinite-dimensional $D$ is exactly what is not available.

For (B), the gap is the absence of any candidate statement: no invariant of $D$ is currently known to be equivalent to "satisfies a nontrivial generalized rational identity".

## 7. Current Research (as of June 2026)

- **Free real algebraic geometry / free analysis** (Klep, Volčič, Pascoe, Helton): domains of noncommutative rational functions, free loci, and realization theory. Volčič's minimal-realization results give canonical linear representations, and Pascoe's inverse function theorems constrain how a rational function can vanish on a matrix domain — the most promising modern source of substitution principles. *(frontier — verify: claims that free-locus techniques settle the finite-center case are not established.)*
- **Invariant-theoretic complexity** (Derksen, Makam, Ivanyos, Qiao, Subrahmanyam): degree bounds for matrix semi-invariants and the null-cone problem; the char-$p$ RIT question is the headline open problem in this line.
- **Generalized identities in skew fields** (Chiba and coauthors, and the Vietnamese school around Bien and Hai on subnormal subgroups of division rings): rational and generalized rational identities imposed on multiplicative subgroups, with the recurring theme that a nontrivial identity on a large subgroup forces finite dimensionality.
- **PI and central simple algebra structure** (Saltman, Rowen, Reichstein): degree-$n$ generic division algebras and their identity theory, connected to the separate, also-open Amitsur rationality question for $Z(UD(n))$, $n\ge 5$ (known rational for $n\le 4$, Formanek; stably rational for $n=5,7$, Bessenrodt–Le Bruyn).

## 8. Future Work

1. **A finite-field substitution lemma.** Prove: if $L(x)$ is a full linear pencil over $\mathbb{F}_q\langle X\rangle$ of size $d$, then $L$ is invertible at some point of $D^m$ for every division $\mathbb{F}_q$-algebra $D$ with $\dim_{Z(D)}D=\infty$. This alone implies (A).
2. **Char-$p$ operator scaling.** Replace $\log\det$ by a characteristic-free potential (or use the Ivanyos–Qiao–Subrahmanyam second Wong sequence) to get deterministic RIT over $\mathbb{F}_q$; this would give effective control of the trivial-identity side in the finite-center regime.
3. **Classify Bergman's counterexamples.** Extract from Bergman's constructions the precise feature of $D$ (maximal subfield, valuation, crossed-product structure) responsible for nontrivial generalized rational identities, and conjecture a criterion.
4. **Involutions and orderings.** Extend the dichotomy to $*$-rational identities on division rings with involution, where even the infinite-center case is only partially understood.
5. **Group-theoretic transfer.** Determine whether a rational identity holding on a subnormal subgroup of $D^\times$ propagates to $D$ over an arbitrary center.

## 9. Key References

- **[Foundational]** S. A. Amitsur. *Rational identities and applications to algebra and geometry.* Journal of Algebra **3** (1966), 304–359.
- **[Foundational]** S. A. Amitsur. *Generalized polynomial identities and pivotal monomials.* Transactions of the American Mathematical Society **114** (1965), 210–226.
- **[Foundational]** G. M. Bergman. *Rational relations and rational identities in division rings, I and II.* Journal of Algebra **43** (1976), 252–266 and 267–297.
- **[Survey / Book]** P. M. Cohn. *Skew Fields: Theory of General Division Rings.* Encyclopedia of Mathematics and its Applications 57, Cambridge University Press, 1995.
- **[Survey / Book]** P. M. Cohn. *Free Rings and their Relations*, 2nd ed. Academic Press, 1985.
- **[Survey / Book]** L. H. Rowen. *Polynomial Identities in Ring Theory.* Academic Press, 1980.
- **[SOTA / Recent]** P. Hrubeš, A. Wigderson. *Non-commutative arithmetic circuits with division.* Theory of Computing **11** (2015), 357–393.
- **[SOTA / Recent]** A. Garg, L. Gurvits, R. Oliveira, A. Wigderson. *A deterministic polynomial time algorithm for non-commutative rational identity testing.* Proc. IEEE FOCS 2016, 109–117.
- **[SOTA / Recent]** G. Ivanyos, Y. Qiao, K. V. Subrahmanyam. *Constructive non-commutative rank computation is in deterministic polynomial time.* Computational Complexity **27** (2018), 561–593.
- **[SOTA / Recent]** H. Derksen, V. Makam. *Polynomial degree bounds for matrix semi-invariants.* Advances in Mathematics **310** (2017), 44–63.
- **[SOTA / Recent]** I. Klep, J. Volčič. *Free loci of matrix pencils and domains of noncommutative rational functions.* Commentarii Mathematici Helvetici **92** (2017), 105–130.
- **[Context]** E. Formanek. *The center of the ring of $3\times3$ generic matrices.* Linear and Multilinear Algebra **7** (1979), 203–212.

## 10. Worked Example / Concrete Special Case

**(a) A trivial identity: Hua's identity.** For all $a,b$ in any division ring with $a\neq0$, $b\neq0$, $b^{-1}-a \neq 0$:
$$a - \bigl(a^{-1} + (b^{-1}-a)^{-1}\bigr)^{-1} = aba.$$
Check the inner term: $a^{-1}+(b^{-1}-a)^{-1}$. Write $u=b^{-1}-a$, so $b^{-1}=u+a$. Then
$$a^{-1}+u^{-1}=a^{-1}(u+a)u^{-1}=a^{-1}b^{-1}u^{-1},$$
hence $\bigl(a^{-1}+u^{-1}\bigr)^{-1}=u\,b\,a$, and
$$a-uba = a-(b^{-1}-a)ba = a - a + aba = aba.$$
So the expression $r(a,b) = a-(a^{-1}+(b^{-1}-a)^{-1})^{-1}-aba$ is a rational identity of *every* division ring — it is $0$ in the free field. It carries no information about $\dim_C D$, and its domain is a nonempty subset of $D^2$ cut out by three inverse conditions (inverse height $3$).

**(b) A nontrivial identity detecting degree $2$.** Let $D=\mathbb{H}$, the real quaternions, $C=\mathbb{R}$, $\dim_C D = 4 = 2^2$. Consider
$$f(x,y,z)=\bigl[(xy-yx)^2,\;z\bigr].$$
Take $x=i$, $y=j$: $ij-ji = k-(-k) = 2k$, and $(2k)^2 = 4k^2 = -4 \in \mathbb{R}$, so $[(ij-ji)^2,z]=0$. In general, for any $u,v \in \mathbb{H}$, $uv-vu$ is a pure quaternion, and every pure quaternion $w$ satisfies $w^2 = -|w|^2 \in \mathbb{R}$; hence $f\equiv 0$ on $\mathbb{H}^3$. The same holds in $M_2$: $xy-yx$ has trace $0$, so by Cayley–Hamilton $(xy-yx)^2 = -\det(xy-yx)\,I$ is scalar. This is the generating $2\times2$ identity.

**(c) It fails in infinite dimension.** Let $F=\mathbb{Q}\!\left(\!\left<x,y,z\right>\!\right)$ be the free field, or concretely the Weyl field $D_1 = \operatorname{Frac}(A_1(\mathbb{Q}))$, $A_1 = \mathbb{Q}\langle p,q\rangle/(pq-qp-1)$, which is infinite-dimensional over its center $\mathbb{Q}$. Put $x=p$, $y=q$: $xy-yx = 1$, so $(xy-yx)^2 = 1$ and $f=0$ — a bad choice. Instead put $x=p$, $y=q^2$: then $pq^2-q^2p = 2q$, so $(xy-yx)^2 = 4q^2$, which is *not* central ($[4q^2,p] = -8q \neq 0$). Hence $f(p,q^2,p)\neq0$ and $\mathbb{H}$'s identity fails on $D_1$, as Amitsur's theorem requires. Note the center $\mathbb{Q}$ here is infinite — the open case (A) is precisely the analogue where the base field is replaced by $\mathbb{F}_q$ (e.g. $D = \operatorname{Frac}$ of a skew polynomial ring $\mathbb{F}_q(t)[\sigma]$ with $\sigma$ of infinite order, whose center is finite), and where no argument of this type is available to produce the witnessing point.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*