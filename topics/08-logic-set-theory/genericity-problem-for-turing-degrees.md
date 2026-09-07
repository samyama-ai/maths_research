---
id: 08-logic-set-theory/genericity-problem-for-turing-degrees
title: "Genericity Problem for Turing Degrees"
topic: 08-logic-set-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Genericity Problem for Turing Degrees

> **Topic:** Mathematical Logic & Set Theory · **ID:** `08-logic-set-theory/genericity-problem-for-turing-degrees` · **Status:** open

## 1. Problem Statement / Conjecture

Cohen forcing over the space $2^{\omega}$ yields a hierarchy of "typical" reals: $1$-generic, $2$-generic, $\dots$, $n$-generic, and arithmetically generic sets. Each level induces a class of Turing degrees. The **genericity problem** asks for a structural theory of these classes and, in its sharpest form, whether the hierarchy *stabilizes*:

> **Conjecture (stabilization).** For every property $P$ of Turing degrees expressible in the first-order language $\langle \mathbf{D}; \le_T \rangle$ (optionally with the jump), there is an $n < \omega$ such that either every $n$-generic degree satisfies $P$ or no $n$-generic degree satisfies $P$; and the least such $n$ is computable from the syntactic complexity of $P$.

Two concrete instances, both open, carry the problem:

1. **Exact level problem.** For each classical degree-theoretic property (bounding a minimal degree, having a strong minimal cover, being the top of a diamond, being a branching degree), determine the exact $n$ at which the $n$-generic degrees switch behaviour. Known: bounding a minimal degree is *possible* at level $1$ and *impossible* at level $2$; almost all other properties have no known threshold.
2. **Initial-segment problem.** Is the first-order theory of the degrees $\le \mathbf{g}$ independent of the choice of the $2$-generic $\mathbf{g}$? Equivalently, do all $2$-generic degrees have isomorphic — or at least elementarily equivalent — lower cones?

A complete solution requires either a uniform forcing-theoretic proof that sufficiently generic degrees are elementarily indistinguishable, or an explicit property $P$ and two $n$-generic degrees for arbitrarily large $n$ disagreeing on $P$.

## 2. Mathematical Foundations

Work in $2^{<\omega}$, finite binary strings, ordered by extension $\sigma \preceq \tau$. A set $S \subseteq 2^{<\omega}$ is **dense along** $A \in 2^{\omega}$ if some initial segment of $A$ lies in $S$ or some initial segment has no extension in $S$. Write $A \in [\![S]\!]$ if $A$ **meets** $S$, i.e. $\exists n\, (A\restriction n \in S)$.

**Definition ($n$-genericity).** $G \in 2^{\omega}$ is **$n$-generic** if for every $\Sigma^0_n$ set $S \subseteq 2^{<\omega}$,
$$\exists n_0\ \big(\, G\restriction n_0 \in S \ \ \vee\ \ \forall \tau \succeq G\restriction n_0\ \ \tau \notin S \,\big).$$
$G$ is **weakly $n$-generic** if it meets every dense $\Sigma^0_n$ set. Then
$$\text{$(n{+}1)$-generic} \Rightarrow \text{weakly $(n{+}1)$-generic} \Rightarrow \text{$n$-generic},$$
and both implications are strict. $G$ is **arithmetically generic** if it is $n$-generic for all $n$. A degree $\mathbf{g}$ is $n$-generic if it contains an $n$-generic set.

**Relativization.** $G$ is $n$-generic **relative to** $X$ if the condition holds for all $\Sigma^0_n(X)$ sets $S$. Genericity is preserved downward along the forcing partial order: if $G$ is $n$-generic and $\sigma \prec G$, then $\sigma \ast G'$ is $n$-generic for suitable tails, which is the source of all homogeneity arguments.

**Basic facts used throughout.**

- *(Jockusch, 1980)* Every $1$-generic set $G$ is **generalized low**: $G' \equiv_T G \oplus \emptyset'$, so $\deg(G)$ is $\mathrm{GL}_1$.
- Every $1$-generic $G$ is of **hyperimmune-free-free** type in the sense that $G$ computes a function not dominated by any computable function; hence $\deg(G) \not\le \mathbf{0}$ and $\deg(G)$ is not minimal.
- $1$-generic degrees are **downward dense in themselves**: $G_{\mathrm{even}} = \{n : 2n \in G\}$ and $G_{\mathrm{odd}}$ are each $1$-generic and $G \equiv_T G_{\mathrm{even}} \oplus G_{\mathrm{odd}}$, so every $1$-generic degree splits.
- The $n$-generic degrees are **comeager** in $2^{\omega}$ but of measure zero; the measure-theoretic analogue (random degrees) has an incompatible structure theory (Barmpalias–Day–Lewis-Pye, 2014).

A **minimal degree** is $\mathbf{a} > \mathbf{0}$ with no $\mathbf{b}$ satisfying $\mathbf{0} < \mathbf{b} < \mathbf{a}$; $\mathbf{a}$ is a **strong minimal cover** of $\mathbf{b}$ if $\{\mathbf{c} : \mathbf{c} < \mathbf{a}\} = \{\mathbf{c} : \mathbf{c} \le \mathbf{b}\}$.

## 3. History & State of the Art (SOTA)

- **1970s.** Cohen forcing enters computability theory through Feferman's work on arithmetic forcing and Sacks' forcing constructions. Martin and Jockusch identify $n$-genericity as the computability-theoretic analogue of Cohen genericity.
- **1980.** Jockusch's *Degrees of generic sets* (LMS Lecture Notes 45) is the founding paper: generalized lowness, non-minimality, splitting, and the theorem that **no $2$-generic degree bounds a minimal degree**. He asks whether a $1$-generic degree can bound one.
- **1986.** Haught proves that every nonzero degree $\le$ a $1$-generic degree below $\mathbf{0}'$ is itself $1$-generic — a strong homogeneity result *below $\mathbf{0}'$*.
- **1990.** Kumabe answers Jockusch: there **is** a $1$-generic degree bounding a minimal degree. Level $1$ and level $2$ therefore differ on a $\Sigma$-simple property; Haught's homogeneity fails above $\mathbf{0}'$.
- **1991–2000.** Kumabe develops the fine structure: relative recursive enumerability of generic degrees; a $1$-generic degree with a **strong minimal cover** (JSL, 2000), again impossible at level $2$.
- **2010s.** Barmpalias, Day and Lewis-Pye (*The typical Turing degree*, Proc. LMS, 2014) systematically contrast genericity-typical and randomness-typical degrees, establishing e.g. that a $2$-generic degree is not the top of a diamond formed with its own predecessors, while a random degree can be.
- **Distinct usage.** Jockusch and Schupp's *generic computability* (density-based, JLMS 2012) is a different notion of genericity; the two literatures share vocabulary but not theorems.

## 4. Partial Results / Verified Cases

| Level | Result | Source |
|---|---|---|
| $n=1$ | $G' \equiv_T G \oplus \emptyset'$; $\deg(G)$ splits; $\deg(G)$ not minimal | Jockusch 1980 |
| $n=1$, below $\mathbf{0}'$ | Every nonzero $\mathbf{b} \le \mathbf{g}$ is $1$-generic — full homogeneity | Haught 1986 |
| $n=1$, above $\mathbf{0}'$ | Some $1$-generic $\mathbf{g}$ bounds a minimal degree | Kumabe 1990 |
| $n=1$ | Some $1$-generic degree has a strong minimal cover | Kumabe 2000 |
| $n=2$ | No $2$-generic degree bounds a minimal degree | Jockusch 1980 |
| $n=2$ | No $2$-generic degree has a strong minimal cover; $\mathbf{g}$ is not a minimal cover of anything | Jockusch 1980; Kumabe 1996 |
| all $n$ | $n$-generic degrees are comeager, measure $0$; closed under join with $\mathbf{0}'$ | folklore/Odifreddi 1999 |
| arithmetic | Arithmetically generic degrees satisfy every $\Sigma^0_\omega$-forceable sentence; theory of the arithmetically generic cone is stable | forcing-theoretic, folklore |

So the stabilization conjecture is **verified for the specific properties above at $n \le 2$**, and for all properties on the arithmetically generic (fully generic) side by a Cohen-forcing absoluteness argument. What is missing is any *uniform* statement in the range $2 \le n < \omega$.

## 5. Principal Obstacles

- **Non-uniformity of the jump.** The forcing relation for $\Sigma^0_n$ formulas is $\Sigma^0_n$-complete, so a construction diagonalizing against level-$n$ requirements needs $\emptyset^{(n)}$ as an oracle. Priority arguments become $n$-fold nested (a "$\emptyset^{(n)}$-tree" argument) and no known bookkeeping keeps them finitary as $n \to \omega$.
- **Failure of Haught homogeneity above $\mathbf{0}'$.** Kumabe's minimal degree below a $1$-generic is built inside a tree of *non-generic* branches; hence lower cones of generic degrees are not generated by generic degrees. Any proof of elementary equivalence of lower cones cannot proceed by identifying the cone with the generic degrees inside it.
- **Coding versus genericity are in tension.** The Slaman–Woodin style coding of arbitrary countable structures into $\mathbf{D}$ requires arranging exact pairs, which needs *definable rigidity*; genericity actively destroys the parameters used, so the standard interpretation machinery for $\mathrm{Th}(\mathbf{D})$ does not descend to $\mathbf{D}(\le \mathbf{g})$.
- **No measure-like invariant.** For randomness, Lebesgue measure gives a $0$–$1$ law that forces stabilization of almost-all behaviour. Category has no analogous countably-additive $0$–$1$ law at fixed arithmetic level: the class of $n$-generics is comeager but the *degree* class is not Borel-simple, so a category-theoretic $0$–$1$ law cannot be invoked at finite $n$.
- **Non-absoluteness.** Statements about lower cones of generics quantify over all reals below $\mathbf{g}$; these are not $\Sigma^1_1$ and therefore not settled by Shoenfield absoluteness, which is exactly why the arithmetic-genericity case is easy and the finite-level case is not.

## 6. The Gap

Proven: a complete answer at levels $1$ and $2$ for **bounding minimality**, **strong minimal covers** and **lowness**, plus full stabilization for arithmetically generic degrees. Open: everything strictly between. The precise barrier is a **level-transfer lemma** of the form
$$\text{$G$ is $(n{+}1)$-generic} \ \wedge\ \mathbf{b} \le \deg(G) \ \Longrightarrow\ \mathbf{b} \text{ is $n$-generic relative to some } \sigma \prec G,$$
which is *true* for $n=0$ below $\mathbf{0}'$ (Haught) and *false* in general above $\mathbf{0}'$ (Kumabe). Resolving the genericity problem means finding the correct weakening of this lemma — one strong enough to yield elementary equivalence of cones, weak enough to survive Kumabe's counterexample.

## 7. Current Research (as of June 2026)

- **Fine hierarchy of pointed genericity.** Work descending from Downey–Jockusch–Stob array-nonrecursiveness and pb-genericity, asking which genericity notions are *degree-invariant* — a notion $N$ with "$\deg(G)$ contains an $N$-generic $\Rightarrow$ every set in $\deg(G)$ has an $N$-generic property" would give the missing homogeneity. *(frontier — verify)*
- **Genericity vs randomness comparison programme.** Continuation of Barmpalias–Day–Lewis-Pye: for each classical structural property, tabulate its truth value on the comeager and on the measure-one side. Active at Victoria University of Wellington, Nanjing/Fudan (Yu Liang's group), and the Chinese Academy of Sciences.
- **Higher genericity.** Transfer of the problem to $\Pi^1_1$ and higher-recursion-theoretic forcing (Greenberg, Monin, Yu), where the definable determinacy available may deliver a $0$–$1$ law that finite levels lack. *(frontier — verify)*
- **Reverse-mathematical calibration.** Locating the strength of "there is a $2$-generic set bounding no minimal degree" in the $\mathsf{ACA}_0$/$\mathsf{ATR}_0$ range as a way of measuring how much induction the level-transfer lemma needs. *(frontier — verify)*

## 8. Future Work

1. **Prove or refute stabilization for $\Sigma_1$ sentences** of $\langle \mathbf{D}; \le_T \rangle$ with parameters below $\mathbf{g}$. This is the smallest fragment where the arithmetically generic proof and the finite-level proofs diverge.
2. **Kumabe's programme:** extend the $1$-generic-bounds-a-minimal-degree method to construct, for each $n$, two $n$-generic degrees with non-isomorphic lower cones. Success refutes stabilization outright.
3. **Build a "generic jump inversion":** show every degree $\ge \mathbf{0}'$ that is $\mathrm{GL}_1$ is the jump of a $1$-generic, sharpening Jockusch's lowness theorem into a characterization.
4. **Definability:** decide whether the class of $1$-generic degrees is first-order definable in $\mathbf{D}$ (or in $\mathbf{D}(\le \mathbf{0}')$). A positive answer would import Slaman–Woodin coding machinery wholesale.

## 9. Key References

- **[Foundational]** C. G. Jockusch, Jr. *Degrees of generic sets.* In *Recursion Theory: its Generalisations and Applications*, LMS Lecture Note Series 45, Cambridge University Press, 1980, pp. 110–139.
- **[Foundational]** C. A. Haught. *The degrees below a 1-generic degree $< \mathbf{0}'$.* Journal of Symbolic Logic 51 (1986), 770–777.
- **[Key result]** M. Kumabe. *A 1-generic degree which bounds a minimal degree.* Journal of Symbolic Logic 55 (1990), 733–743.
- **[Key result]** M. Kumabe. *A 1-generic degree with a strong minimal cover.* Journal of Symbolic Logic 65 (2000), 1395–1442.
- **[Survey]** M. Kumabe. *Degrees of generic sets.* In *Computability, Enumerability, Unsolvability: Directions in Recursion Theory*, LMS Lecture Note Series 224, Cambridge University Press, 1996, pp. 167–183.
- **[SOTA / Recent]** G. Barmpalias, A. R. Day, A. E. M. Lewis-Pye. *The typical Turing degree.* Proceedings of the London Mathematical Society 109 (2014), 1–39.
- **[Related notion]** C. G. Jockusch, Jr., P. E. Schupp. *Generic computability, Turing degrees, and asymptotic density.* Journal of the London Mathematical Society 85 (2012), 472–490.
- **[Textbook]** M. Lerman. *Degrees of Unsolvability: Local and Global Theory.* Perspectives in Mathematical Logic, Springer, 1983.
- **[Textbook]** P. Odifreddi. *Classical Recursion Theory, Volume II.* Studies in Logic 143, North-Holland, 1999 (Chapter on forcing and genericity).
- **[Textbook]** R. I. Soare. *Recursively Enumerable Sets and Degrees.* Perspectives in Mathematical Logic, Springer, 1987.
- **[Context]** R. Downey, D. Hirschfeldt. *Algorithmic Randomness and Complexity.* Springer, 2010 (Chapter 8: genericity and weak genericity).

## 10. Worked Example / Concrete Special Case

**Claim.** Every $1$-generic $G$ has non-minimal degree — verified by an explicit split.

*Step 1: build $G$.* Enumerate the $\Sigma^0_1$ sets $S_0, S_1, \dots$ of strings. Set $\sigma_0 = \langle\rangle$. Given $\sigma_e$:
$$\sigma_{e+1} = \begin{cases}\tau & \text{if some } \tau \succeq \sigma_e \text{ has } \tau \in S_e \text{ (least such found)},\\ \sigma_e 0 & \text{otherwise.}\end{cases}$$
Let $G = \bigcup_e \sigma_e$. If no extension of $\sigma_e$ enters $S_e$, then $\sigma_{e+1} \prec G$ witnesses avoidance; otherwise $G$ meets $S_e$. So $G$ is $1$-generic. (The construction is $\emptyset'$-computable, so one may take $G \le_T \emptyset'$.)

*Step 2: $G_{\mathrm{even}} = \{n : 2n \in G\}$ is not computable.* Fix a computable $f = \varphi_e$ total $0$–$1$ valued and consider
$$S = \{\sigma : \exists n\ (|\sigma| > 2n \ \wedge\ \sigma(2n) \ne f(n))\},$$
a $\Sigma^0_1$ set. $S$ is dense: any $\sigma$ extends to $\sigma \ast b$ at an even position with $b \ne f(|\sigma|/2)$. Density means the avoidance option is unavailable, so $G$ meets $S$, giving $n$ with $G_{\mathrm{even}}(n) \ne f(n)$. Hence $G_{\mathrm{even}} \not\le_T \emptyset$, so $\mathbf{0} < \deg(G_{\mathrm{even}})$.

*Step 3: $G \not\le_T G_{\mathrm{even}}$.* For each $e$ the set
$$S_e^{\ast} = \{\sigma : \exists n\ \varphi_e^{\,\sigma_{\mathrm{even}}}(n)\!\downarrow \ \wedge\ \varphi_e^{\,\sigma_{\mathrm{even}}}(n) \ne \sigma(2n{+}1)\}$$
is $\Sigma^0_1$ and dense along any string: extend $\sigma$ until the computation converges, then set the *odd* bit $2n+1$ opposite to the output — legal because odd bits do not affect $\sigma_{\mathrm{even}}$. Genericity gives either a witness (so $\varphi_e^{G_{\mathrm{even}}} \ne G$) or a string beyond which $\varphi_e^{G_{\mathrm{even}}}$ diverges. Either way $G \not\le_T G_{\mathrm{even}}$.

*Conclusion.* $\mathbf{0} < \deg(G_{\mathrm{even}}) < \deg(G)$, so $\deg(G)$ is not minimal.

**Where the problem bites.** Step 3 used only $\Sigma^0_1$ density, i.e. level $1$. Jockusch's theorem that no $2$-generic degree *bounds* a minimal degree needs $\Sigma^0_2$ density to defeat an arbitrary tree of partial computable functionals, and the analogous argument at level $3$ gains nothing new — no known property separates level $2$ from level $3$. That silence, not any single counterexample, is the genericity problem.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*