---
id: 08-logic-set-theory/baumgartner-axiom-higher-cardinals
title: "Baumgartner's Problem on Isomorphism of Aleph-One Dense Sets"
topic: 08-logic-set-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Baumgartner's Problem on Isomorphism of Aleph-One Dense Sets

> **Topic:** Mathematical Logic & Set Theory · **ID:** `08-logic-set-theory/baumgartner-axiom-higher-cardinals` · **Status:** open

## 1. Problem Statement / Conjecture

A set $A \subseteq \mathbb{R}$ is **$\kappa$-dense** if $|A \cap (a,b)| = \kappa$ for every pair of reals $a < b$. Baumgartner's axiom $\mathrm{BA}(\kappa)$ is the statement:

$$\mathrm{BA}(\kappa):\quad \text{any two } \kappa\text{-dense sets } A, B \subseteq \mathbb{R} \text{ are order-isomorphic.}$$

Baumgartner (1973) proved $\mathrm{Con}(\mathrm{ZFC}) \Rightarrow \mathrm{Con}(\mathrm{ZFC} + \mathrm{BA}(\aleph_1))$. The open problem is the higher-cardinal case:

> **Problem.** Is $\mathrm{BA}(\aleph_2)$ consistent with $\mathrm{ZFC}$ (relative to large cardinals)? More generally, is $\mathrm{BA}(\aleph_n)$ consistent for some $n \ge 2$?

Two secondary questions, both attributed to Baumgartner, are also open:

- Does $\mathrm{BA}(\aleph_1)$ imply $2^{\aleph_0} = \aleph_2$?
- Is $\mathrm{BA}(\aleph_1) \wedge \mathrm{BA}(\aleph_2)$ consistent?

A complete solution is either a forcing construction (with whatever large-cardinal hypotheses are needed) producing a model of $\mathrm{ZFC} + \mathrm{BA}(\aleph_2)$, or a $\mathrm{ZFC}$ proof that $\mathrm{BA}(\aleph_2)$ is false. Note $\mathrm{BA}(\aleph_2)$ already forces $2^{\aleph_0} \ge \aleph_3$ (Section 4), so any consistency proof must produce a model with large continuum, which is the crux of the difficulty.

## 2. Mathematical Foundations

**Order types.** For $A \subseteq \mathbb{R}$ write $\mathrm{tp}(A)$ for its order type under the inherited $<$. Cantor's theorem gives $\mathrm{tp}(A) = \eta$ (the type of $\mathbb{Q}$) for every countable dense $A$, i.e. $\mathrm{BA}(\aleph_0)$ is a $\mathrm{ZFC}$ theorem by back-and-forth. $\mathrm{BA}(\kappa)$ asks whether Cantor's uniqueness survives at $\kappa > \aleph_0$.

**Determination by a countable subset.** If $A$ is dense in $\mathbb{R}$, $D \subseteq A$ is countable and dense in $A$, and $f, g : A \to \mathbb{R}$ are strictly increasing with $f\restriction D = g\restriction D$, then $f = g$: for $x \in A$, both $f(x)$ and $g(x)$ lie in $\bigcap \{ (f(d), f(d')) : d < x < d',\ d,d' \in D\}$, and density of $f[D]$ forces this intersection to be a single point. Hence

$$\bigl|\{\, f : f \text{ an order-isomorphism between } \kappa\text{-dense subsets of } \mathbb{R} \,\}\bigr| \;\le\; \mathfrak{c}^{\aleph_0} = 2^{\aleph_0}. \tag{2.1}$$

**Forcing $\mathrm{BA}(\aleph_1)$.** Given $\aleph_1$-dense $A,B$, Baumgartner's poset is
$$\mathbb{P}_{A,B} = \{\, p : p \text{ a finite order-preserving partial injection } A \to B \,\},$$
ordered by $\supseteq$, iterated with countable support over a model of $\mathrm{CH}$ along an $\omega_2$-length iteration. The key lemma is that $\mathbb{P}_{A,B}$ is **proper** — indeed it has the $\aleph_1$-properness needed so countable support iteration does not collapse $\omega_1$ — and adds a generic isomorphism $\bigcup G : A \to B$. The same poset is a witness that $\mathrm{PFA} \Rightarrow \mathrm{BA}(\aleph_1)$.

**Combinatorial obstructions.** Under $\mathrm{CH}$ there are $2^{\aleph_1}$ pairwise non-isomorphic $\aleph_1$-dense sets, and rigid ones exist in $\mathrm{ZFC}$ at the continuum (Dushnik–Miller). Abraham–Rubin–Shelah isolated the relevant combinatorics as **increasing sets** and the partition principles $\mathrm{PFA}^{-}$-style axioms for continuous colorings $c : [A]^2 \to 2$; the open colouring axiom $\mathrm{OCA}_{\mathrm{ARS}}$ from that paper is precisely the tool that makes finite approximations amalgamate.

**Cardinal arithmetic constraint.** From (2.1): if $\kappa = 2^{\aleph_0}$ then there are only $\kappa$ candidate isomorphisms, and a recursion of length $\kappa$ defeats them all, so
$$\mathrm{BA}(\kappa) \Rightarrow \kappa < 2^{\aleph_0}. \tag{2.2}$$

## 3. History & State of the Art (SOTA)

- **1940.** Dushnik and Miller construct in $\mathrm{ZFC}$ a rigid dense subset of $\mathbb{R}$ of size $\mathfrak{c}$, showing Cantor's theorem fails badly at the continuum.
- **1973.** James Baumgartner, *All $\aleph_1$-dense sets of reals can be isomorphic* (Fund. Math. 79), proves $\mathrm{Con}(\mathrm{BA}(\aleph_1))$ by an $\omega_2$-length countable-support iteration over a model of $\mathrm{CH}$, yielding $\mathrm{BA}(\aleph_1) + 2^{\aleph_0} = \aleph_2$. This is one of the first genuine applications of what became the theory of proper forcing.
- **1981.** Abraham and Shelah show $\mathrm{MA}_{\aleph_1}$ does not imply $\mathrm{BA}(\aleph_1)$: there is a model of $\mathrm{MA} + 2^{\aleph_0} = \aleph_2$ with two non-isomorphic $\aleph_1$-dense sets. So ccc forcing axioms are strictly too weak.
- **1984.** Baumgartner's Handbook chapter derives $\mathrm{BA}(\aleph_1)$ from $\mathrm{PFA}$ and raises the higher-cardinal question explicitly.
- **1985.** Abraham–Rubin–Shelah give a fine structure theory of $\aleph_1$-dense real order types, separating $\mathrm{BA}(\aleph_1)$ from neighbouring axioms and producing models with prescribed numbers of $\aleph_1$-dense types.
- **2006–2010.** Moore's five-element basis theorem for uncountable linear orders (Annals, 2006) is the deepest structural result in the $\aleph_1$ regime; $\mathrm{PFA}$-style methods do not extend to $\aleph_2$-dense sets.
- **2014–2017.** Neeman's forcing with sequences of models of two types gives finite side-condition iterations at $\omega_2$ — currently the most promising machinery for the higher case, but it has not been made to yield $\mathrm{BA}(\aleph_2)$.

## 4. Partial Results / Verified Cases

| Case | Status |
|---|---|
| $\kappa = \aleph_0$ | **True in ZFC** (Cantor 1895, back-and-forth). |
| $\kappa = \aleph_1$, under $\mathrm{CH}$ | **False in ZFC + CH**; $2^{\aleph_1}$ non-isomorphic types. |
| $\kappa = \aleph_1$ | **Consistent** (Baumgartner 1973); follows from $\mathrm{PFA}$; independent of $\mathrm{MA}_{\aleph_1}$ (Abraham–Shelah 1981). |
| $\kappa = 2^{\aleph_0}$ | **False in ZFC** by (2.2); rigid examples: Dushnik–Miller 1940. |
| $\kappa = \aleph_2$, with $2^{\aleph_0} = \aleph_2$ | **False in ZFC** — immediate from (2.2). |
| $\kappa = \aleph_2$, $2^{\aleph_0} \ge \aleph_3$ | **Open.** This is the problem. |
| $\kappa$ of cofinality $\omega$, e.g. $\aleph_\omega < 2^{\aleph_0}$ | Open; no consistency proof known for any $\kappa \ge \aleph_2$. |
| Restricted classes | $\mathrm{BA}(\aleph_1)$ restricted to sets of a fixed "type" (increasing sets, sets with prescribed colouring behaviour) is fully analysed by Abraham–Rubin–Shelah. |

So the verified positive territory is exactly $\kappa \in \{\aleph_0\}$ in $\mathrm{ZFC}$ and $\kappa = \aleph_1$ consistently; everything at and above $\aleph_2$ is open except the arithmetic exclusion $\kappa < 2^{\aleph_0}$.

## 5. Principal Obstacles

- **Iteration theory stops at $\omega_1$.** Baumgartner's proof needs countable support iteration and properness, whose preservation theorem is tied to countable elementary submodels and $\omega_1$. The analogue — "$\aleph_2$-properness", preservation of $\omega_2$ under $\omega_2$-support iterations — conflicts with adding reals: a forcing that is $\ ^{\omega}\!\mathrm{closed}$-like enough to iterate at $\omega_2$ adds no reals, but the isomorphism poset $\mathbb{P}_{A,B}$ for $\aleph_2$-dense sets must be handled without collapsing $\aleph_2$ while $2^{\aleph_0} \ge \aleph_3$.
- **Large continuum breaks the bookkeeping.** By (2.2) a model of $\mathrm{BA}(\aleph_2)$ has $\mathfrak{c} \ge \aleph_3$. Standard forcing axioms ($\mathrm{PFA}$, $\mathrm{MM}$) imply $\mathfrak{c} = \aleph_2$, so none of them can be the source of $\mathrm{BA}(\aleph_2)$; the entire forcing-axiom toolkit is disqualified as-is.
- **No back-and-forth at $\aleph_2$.** The finite-condition poset $\mathbb{P}_{A,B}$ is still ccc-like combinatorially, but the genericity needed to make $\bigcup G$ total on an $\aleph_2$-sized set requires meeting $\aleph_2$ dense sets — i.e. $\mathrm{MA}_{\aleph_2}$-strength for a poset class where even $\mathrm{MA}_{\aleph_1}$ is known insufficient (Abraham–Shelah).
- **Colouring obstructions at $\aleph_2$.** Todorcevic's $\mathrm{ZFC}$ walks on ordinals give strong negative partition relations $\aleph_2 \not\to [\aleph_2]^2_{\aleph_2}$ that survive all known forcings; whether such a colouring can be converted into a $\mathrm{ZFC}$ pair of non-isomorphic $\aleph_2$-dense sets is unresolved but is the natural route to a negative answer.
- **Side conditions do not yet reach $\mathfrak{c} > \aleph_2$.** Neeman's two-type side conditions handle $\omega_2$ but the resulting models satisfy $\mathfrak{c} = \aleph_2$, exactly the excluded case.

## 6. The Gap

Everything positive is a proper-forcing theorem at $\omega_1$; the problem lives at $\omega_2$ with $\mathfrak{c} \ge \aleph_3$. The exact missing step:

> Produce an iterable class $\mathcal{K}$ of forcings containing $\mathbb{P}_{A,B}$ for all $\aleph_2$-dense $A,B$, closed under an iteration of length $\ge \aleph_3$ that preserves $\aleph_1$ and $\aleph_2$ and adds reals cofinally, with a preservation theorem for $\mathcal{K}$.

Alternatively, on the negative side: convert a $\mathrm{ZFC}$ colouring $c : [\omega_2]^2 \to 2$ with no large monochromatic set into a $\mathrm{ZFC}$ construction of two $\aleph_2$-dense sets $A, B$ with $\mathrm{tp}(A) \ne \mathrm{tp}(B)$, without assuming $\mathfrak{c} = \aleph_2$. No known argument survives the hypothesis $\mathfrak{c} \ge \aleph_3$, because the counting bound (2.1) becomes vacuous once $2^{\aleph_0} > \aleph_2$.

## 7. Current Research (as of June 2026)

- **Side-condition forcing at $\omega_2$** (Neeman, UCLA; Veličković, Paris; Krueger, North Texas): mixed finite/countable and finite/two-type side conditions are the only technology producing genuinely new $\omega_2$-forcing axioms. Adapting them to models with $\mathfrak{c} > \aleph_2$ is active. *(frontier — verify)*
- **Higher forcing axioms with large continuum** (Cummings, Friedman, Honzík, Shelah school): axioms of the form $\mathrm{MA}^{+}_{\aleph_2}(\mathcal{K})$ compatible with $\mathfrak{c} \ge \aleph_3$; no instance yet decides $\mathrm{BA}(\aleph_2)$.
- **Structure of uncountable linear orders** (Moore, Cornell; Todorcevic, Toronto/Paris): basis problems for orders of size $\aleph_2$; a five-element-basis analogue at $\aleph_2$ is itself open and would be a strong prerequisite.
- **The secondary question "does $\mathrm{BA}(\aleph_1)$ imply $\mathfrak{c} = \aleph_2$?"** is periodically revisited; partial results give $\mathrm{BA}(\aleph_1)$ plus fragments of $\mathrm{OCA}$ implying $\mathfrak{c} = \aleph_2$, but the bare implication remains open. *(frontier — verify)*

## 8. Future Work

1. **Isolate $\aleph_2$-properness.** Find a preservation theorem for iterations of length $>\aleph_2$ with supports of size $\le \aleph_1$ that preserves both $\aleph_1$ and $\aleph_2$; Shelah's $(<\!\kappa)$-properness fails to cover posets adding reals.
2. **Prove or refute $\mathrm{BA}(\aleph_2) \Rightarrow$ some known-false statement**, e.g. derive a violation of $\square_{\omega_1}$-type principles or a strong colouring contradiction, giving an outright $\mathrm{ZFC}$ refutation.
3. **Weak versions first.** Consistency of "any two $\aleph_2$-dense sets have isomorphic $\aleph_2$-dense subsets" — a strictly weaker and probably more tractable statement.
4. **Determine the exact continuum constraint.** Does $\mathrm{BA}(\aleph_2)$ imply $\mathfrak{c} = \aleph_3$, or is it compatible with $\mathfrak{c}$ arbitrarily large?
5. **Large-cardinal calibration.** No lower bound in consistency strength above $\mathrm{ZFC}$ is known for $\mathrm{BA}(\aleph_2)$; establishing any would be informative.

## 9. Key References

- **[Foundational]** J. E. Baumgartner. *All $\aleph_1$-dense sets of reals can be isomorphic.* Fundamenta Mathematicae 79 (1973), 101–106.
- **[Foundational]** B. Dushnik, E. W. Miller. *Concerning similarity transformations of linearly ordered sets.* Bulletin of the American Mathematical Society 46 (1940), 322–326.
- **[Foundational]** J. E. Baumgartner. *Applications of the Proper Forcing Axiom.* In: Handbook of Set-Theoretic Topology (K. Kunen, J. E. Vaughan, eds.), North-Holland, 1984, 913–959.
- **[Independence]** U. Abraham, S. Shelah. *Martin's axiom does not imply that every two $\aleph_1$-dense sets of reals are isomorphic.* Israel Journal of Mathematics 38 (1981), 161–176.
- **[Structure]** U. Abraham, M. Rubin, S. Shelah. *On the consistency of some partition theorems for continuous colorings, and the structure of $\aleph_1$-dense real order types.* Annals of Pure and Applied Logic 29 (1985), 123–206.
- **[SOTA / Recent]** I. Neeman. *Forcing with sequences of models of two types.* Notre Dame Journal of Formal Logic 55 (2014), 265–298.
- **[SOTA / Recent]** I. Neeman. *Two applications of finite side conditions at $\omega_2$.* Archive for Mathematical Logic 56 (2017), 983–1036.
- **[SOTA / Recent]** J. T. Moore. *A five element basis for the uncountable linear orders.* Annals of Mathematics 163 (2006), 669–688.
- **[Survey]** J. T. Moore. *The proper forcing axiom.* Proceedings of the International Congress of Mathematicians, Hyderabad 2010, Vol. II, 3–29.
- **[Survey]** S. Todorcevic. *Partition Problems in Topology.* Contemporary Mathematics 84, American Mathematical Society, 1989.
- **[Reference]** S. Shelah. *Proper and Improper Forcing*, 2nd ed. Perspectives in Mathematical Logic, Springer, 1998.

## 10. Worked Example / Concrete Special Case

**Claim.** If $2^{\aleph_0} = \kappa$ then $\mathrm{BA}(\kappa)$ fails. Taking $\kappa = \aleph_1$ this is the $\mathrm{CH}$ case; taking $\kappa = \aleph_2$ it is the reason the target problem must be attacked with $\mathfrak{c} \ge \aleph_3$.

*Construction.* Assume $2^{\aleph_0} = \kappa$ (so $\kappa^{\aleph_0} = \kappa$). By (2.1) there are at most $\kappa$ strictly increasing maps between dense subsets of $\mathbb{R}$; enumerate them as $\langle f_\alpha : \alpha < \kappa\rangle$. Fix disjoint copies of $\mathbb{Q}$: let $Q_0 = \mathbb{Q}$, $Q_1 = \mathbb{Q} + \sqrt{2}$.

Build increasing chains $\langle A_\alpha\rangle_{\alpha<\kappa}$, $\langle B_\alpha\rangle_{\alpha<\kappa}$ of sets of size $<\kappa$ with $A_0 = Q_0$, $B_0 = Q_1$, $A_\alpha \cap B_\alpha = \emptyset$, taking unions at limits. At stage $\alpha+1$:

1. If $f_\alpha$ maps a subset of $\mathbb{R}$ onto a subset of $\mathbb{R}$ and $A_\alpha \subseteq \mathrm{dom}(f_\alpha)$ is not yet defeated, choose $x \in \mathbb{R} \setminus (A_\alpha \cup B_\alpha \cup f_\alpha^{-1}[B_\alpha])$ with $f_\alpha(x)$ defined; put $x \in A_{\alpha+1}$ and $f_\alpha(x) \notin B_{\alpha+1}$. This is possible because $|A_\alpha|,|B_\alpha| < \kappa = \mathfrak{c}$ and every interval has $\mathfrak{c}$ reals.
2. Add $\kappa$-many further points to keep the eventual sets $\kappa$-dense: for each rational interval, ensure the number of points placed in it grows cofinally in $\kappa$.

Set $A = \bigcup_\alpha A_\alpha$, $B = \bigcup_\alpha B_\alpha$. Then $A, B$ are $\kappa$-dense and disjoint. If $f : A \to B$ were an order-isomorphism, pick a countable dense $D \subseteq A$; by the determination lemma $f$ agrees with some $f_\alpha$ (namely the unique increasing extension of $f\restriction D$), and stage $\alpha+1$ put a point $x \in A$ with $f_\alpha(x) \notin B$ — contradiction.

**Numerically, under $\mathrm{CH}$:** the candidate isomorphisms number $\mathfrak{c}^{\aleph_0} = \aleph_1^{\aleph_0} = \aleph_1$, the recursion has length $\omega_1$, and each step kills one candidate using a single new real — the bookkeeping closes exactly. Under $\mathfrak{c} = \aleph_2$ the same count gives $\aleph_2^{\aleph_0} = \aleph_2$ candidates against an $\omega_2$-length recursion, killing $\mathrm{BA}(\aleph_2)$. The argument collapses only when $\mathfrak{c} > \kappa$: then there are $\mathfrak{c} > \kappa$ candidate isomorphisms but only $\kappa$ stages available, and no diagonalization is possible — which is precisely the open region.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*