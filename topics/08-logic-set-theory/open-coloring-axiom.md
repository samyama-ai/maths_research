---
id: 08-logic-set-theory/open-coloring-axiom
title: "Open Coloring Axiom"
topic: 08-logic-set-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Open Coloring Axiom

> **Topic:** Mathematical Logic & Set Theory · **ID:** `08-logic-set-theory/open-coloring-axiom` · **Status:** open

## 1. Problem Statement / Conjecture

The Open Coloring Axiom (OCA, in Todorcevic's form $\mathrm{OCA}_{[T]}$) is a Ramsey-type dichotomy for open graphs on separable metric spaces. It is consistent relative to ZFC (Todorcevic, 1989) and follows from PFA.

The catalogued open problem is the central structural question about it:

> **Problem.** Does $\mathrm{OCA}$ imply $2^{\aleph_0}=\aleph_2$?

Equivalently: is $\mathrm{OCA} + 2^{\aleph_0} > \aleph_2$ consistent with ZFC? No model of $\mathrm{OCA}$ with continuum above $\aleph_2$ is known, and no ZFC proof that $\mathrm{OCA}\Rightarrow \mathfrak c=\aleph_2$ is known. A complete resolution is either (a) a ZFC proof that $\mathrm{OCA}$ decides $\mathfrak c=\aleph_2$, or (b) a forcing construction (necessarily not a countable-support proper iteration of length $\omega_2$) producing a model of $\mathrm{OCA}+\mathfrak c\ge\aleph_3$.

Two subsidiary open questions travel with it: does $\mathrm{OCA}_{[T]}$ imply the Abraham–Rubin–Shelah axiom $\mathrm{OCA}_{[ARS]}$, and does $\mathrm{OCA}$ imply $\mathrm{MA}_{\aleph_1}$ (or any of its fragments beyond those already known to follow)?

## 2. Mathematical Foundations

Let $X$ be a separable metrizable space. Write $[X]^2=\{\{x,y\}: x\neq y\in X\}$, topologised as the quotient of $X^2\setminus\Delta$ by the flip map. A partition
$$[X]^2 = K_0 \,\dot\cup\, K_1$$
is an **open colouring** if $K_0$ is open in $[X]^2$; equivalently $K_0$ is the edge set of a graph $G$ on $X$ that is open as a symmetric subset of $X^2\setminus\Delta$. A set $Y\subseteq X$ is **$K_i$-homogeneous** if $[Y]^2\subseteq K_i$ ($K_0$-homogeneous $=$ clique, $K_1$-homogeneous $=$ independent set).

**Axiom ($\mathrm{OCA}_{[T]}$, Todorcevic 1989).** For every separable metrizable $X$ and every open colouring $[X]^2=K_0\cup K_1$:
$$\exists\, Y\subseteq X \text{ uncountable, } [Y]^2\subseteq K_0 \qquad\text{or}\qquad X=\bigcup_{n<\omega}X_n \text{ with } [X_n]^2\subseteq K_1 \ \forall n .$$

In graph language: every open graph on a separable metric space either has an uncountable clique or has countable chromatic number. The two alternatives are not exclusive; the axiom asserts at least one holds. For $|X|\le\aleph_0$ it is trivial, so the content is at $|X|\ge\aleph_1$.

**Related axioms.**
- $\mathrm{OCA}_{[ARS]}$ (Abraham–Rubin–Shelah 1985): a partition axiom for *continuous* colourings of pairs of reals, formulated in their study of $\aleph_1$-dense real order types; in the normalisation used by Moore (2002) it is a "rectangular" strengthening asserting uncountable $X_0,X_1\subseteq X$ with $[X_0,X_1]\subseteq K_0$. It is not known to follow from $\mathrm{OCA}_{[T]}$.
- $\mathrm{OCA}_\infty$ (Farah 2011): the analogous dichotomy for decreasing $\omega$-sequences of open colourings, used in operator-algebra applications.

**Cardinal characteristics used below.** $f<^*g$ iff $f(n)<g(n)$ for all but finitely many $n$; $\mathfrak b$ is the least size of a $<^*$-unbounded family in $\omega^\omega$, $\mathfrak d$ the least size of a dominating family, and $\mathfrak c=2^{\aleph_0}$. Always $\aleph_1\le\mathfrak b\le\mathfrak d\le\mathfrak c$.

**Anchor theorems.**
1. (Todorcevic) $\mathrm{Con}(\mathrm{ZFC})\Rightarrow\mathrm{Con}(\mathrm{ZFC}+\mathrm{OCA})$, via a countable-support iteration of proper forcings of length $\omega_2$ over a model of CH. Consistency strength is exactly ZFC.
2. (Todorcevic) $\mathrm{OCA}\Rightarrow \mathfrak b=\aleph_2$. Hence $\mathrm{OCA}\Rightarrow\neg\mathrm{CH}$ and $\mathfrak c\ge\aleph_2$.
3. (Todorcevic) $\mathrm{PFA}\Rightarrow\mathrm{OCA}$; and $\mathrm{PFA}\Rightarrow\mathfrak c=\aleph_2$ (Todorcevic–Veličković).

## 3. History & State of the Art (SOTA)

- **1985.** Abraham, Rubin and Shelah isolate partition axioms for continuous colourings (SOCA, $\mathrm{OCA}_{[ARS]}$) while classifying $\aleph_1$-dense real order types, and prove their consistency with $\mathrm{MA}_{\aleph_1}+\mathfrak c=\aleph_2$.
- **1989.** Todorcevic, *Partition Problems in Topology*, states the axiom in its now-standard form, proves consistency by proper forcing over a model of CH, and derives $\mathfrak b=\aleph_2$ plus a battery of consequences on gaps in $\mathcal P(\omega)/\mathrm{fin}$ and on chain conditions.
- **1993.** Feng Qi proves the definable half in ZFC: the dichotomy holds for all $\boldsymbol\Sigma^1_1$ (analytic) sets, and calibrates $\mathrm{OCA}(\boldsymbol\Sigma^1_2)$ and projective/$L(\mathbb R)$ versions against large-cardinal hypotheses.
- **1993–2000.** Veličković shows $\mathrm{OCA}\Rightarrow$ every automorphism of $\mathcal P(\omega)/\mathrm{fin}$ is trivial; Farah's memoir *Analytic quotients* extends the rigidity programme to quotients by analytic ideals, making OCA the standard rigidity axiom.
- **2002.** Moore proves $\mathrm{OCA}_{[ARS]}+\mathrm{OCA}_{[T]}\Rightarrow\mathfrak c=\aleph_2$ — the strongest published approximation to the catalogued problem.
- **2011.** Farah proves in $\mathrm{ZFC}+\mathrm{OCA}$ that all automorphisms of the Calkin algebra $\mathcal B(H)/\mathcal K(H)$ are inner, contradicting the CH construction of Phillips–Weaver.
- **Status 2026.** Whether $\mathrm{OCA}$ alone decides the continuum remains open; every known consistency proof of OCA yields $\mathfrak c=\aleph_2$.

## 4. Partial Results / Verified Cases

- **Definable classes (ZFC, no extra axioms).** The dichotomy holds outright for every analytic $X\subseteq\mathbb R$ and every open colouring; the $K_0$-homogeneous set can be taken perfect, of size $\mathfrak c$ (Feng 1993). Under $\mathrm{AD}^{L(\mathbb R)}$ or a proper class of Woodin cardinals it holds for all sets in $L(\mathbb R)$.
- **Cardinality $\aleph_1$ under $\mathrm{MA}_{\aleph_1}$.** The restriction of OCA to $|X|=\aleph_1$ already implies $\mathfrak b>\aleph_1$; conversely $\mathrm{MA}_{\aleph_1}$ alone does not imply OCA (ARS 1985).
- **Upper bounds forced by OCA.** $\mathfrak b=\aleph_2$; every $(\omega_1,\omega_1)$-gap in $\mathcal P(\omega)/\mathrm{fin}$ is Hausdorff; there are no $(\mathfrak b,\omega_1)$-gaps of the "Luzin" type. Under $\mathrm{OCA}+\mathrm{MA}_{\aleph_1}$ the gap spectrum of $\mathcal P(\omega)/\mathrm{fin}$ is completely determined.
- **Conditional resolution of the catalogued problem.** $\mathrm{OCA}_{[ARS]}+\mathrm{OCA}_{[T]}\Rightarrow \mathfrak c=\aleph_2$ (Moore 2002). Also $\mathrm{PFA}\Rightarrow\mathrm{OCA}+\mathfrak c=\aleph_2$.
- **Rigidity consequences (theorems, not conjectures).** All automorphisms of $\mathcal P(\omega)/\mathrm{fin}$ are trivial; all automorphisms of the Calkin algebra are inner; all isomorphisms between quotients over analytic P-ideals have continuous liftings.

## 5. Principal Obstacles

- **One-sided forcing technology.** OCA is proved consistent by iterating, for each open colouring, a proper poset that adds either an uncountable clique or a countable colouring. Countable-support iterations of proper forcings over a model of CH are $\aleph_2$-c.c. and collapse cardinals above $\aleph_2$ if lengthened naively; so the only known construction *forces* $\mathfrak c=\aleph_2$. This is a limitation of the method, not a proof.
- **Finite-support alternatives fail.** Finite-support iterations of ccc forcings can push $\mathfrak c$ above $\aleph_2$, but the natural OCA-forcings are not ccc in general (their ccc-ness for arbitrary colourings is exactly what fails without extra hypotheses), and cofinally added Cohen reals reinstate open colourings with neither alternative.
- **No known reflection for $\mathfrak c$.** The derivation $\mathrm{OCA}\Rightarrow\mathfrak b=\aleph_2$ uses a specific colouring built from an unbounded $<^*$-increasing family. No colouring is known whose homogeneity analysis reads off $\mathfrak c$ itself; a set of size $\aleph_3$ has no canonical "one-dimensional" combinatorial skeleton to colour.
- **The $\aleph_1$-vs-$\aleph_2$ asymmetry.** OCA's conclusion produces *uncountable* cliques, never cliques of size $\aleph_2$; iterating the axiom at higher cardinals ($\mathrm{OCA}_{\aleph_2}$) is outright inconsistent in the direct generalisation, so no upward induction is available.
- **Definable methods stop at $\boldsymbol\Sigma^1_1$.** Feng's proof uses Baire-category/derivative arguments on analytic sets; sets of size $\aleph_1$ in a model with $\mathfrak c>\aleph_1$ are non-definable and admit no perfect-set machinery.

## 6. The Gap

Proven: $\mathrm{OCA}\Rightarrow\mathfrak b=\aleph_2$ (so $\aleph_2\le\mathfrak c$), and $\mathrm{OCA}_{[T]}+\mathrm{OCA}_{[ARS]}\Rightarrow\mathfrak c=\aleph_2$. Unproven: an upper bound $\mathfrak c\le\aleph_2$ from $\mathrm{OCA}_{[T]}$ alone.

The exact missing step is one of:

1. **Derivation.** Produce, in $\mathrm{ZFC}+\mathrm{OCA}_{[T]}$, an open colouring on a space coded by an arbitrary family of $\aleph_2$ reals whose $K_0$/$K_1$ dichotomy forces a cofinal map $\omega_2\to\mathfrak c$ — i.e. show $\mathrm{OCA}_{[T]}\Rightarrow\mathrm{OCA}_{[ARS]}$ and invoke Moore; or
2. **Separation.** Build an iteration (side-condition, or matrix/template-style, or a $\sigma$-closed$\ast$ccc factorisation) of length $\ge\omega_3$ that generically resolves every open colouring while adding $\aleph_3$ reals and preserving $\aleph_1,\aleph_2$. The obstruction is preserving "no uncountable clique appears later that destroys an earlier countable colouring" over long iterations.

## 7. Current Research (as of June 2026)

- **Toronto/York and Belgrade–Paris schools** (Farah, Todorcevic and collaborators) continue the OCA-rigidity programme: automorphisms of corona algebras, reduced products of matrix algebras, and Borel-reducibility consequences. These use $\mathrm{OCA}_\infty$ and OCA$+\mathrm{MA}_{\aleph_1}$ rather than resolving the continuum question.
- **Cornell (Moore) and descendants** pursue the $\mathrm{OCA}_{[T]}\Rightarrow\mathrm{OCA}_{[ARS]}$ implication and OCA's relation to fragments of MA, and to the basis problem for uncountable linear orders.
- **Iteration technology.** Attempts to combine side-condition forcing with template iterations to obtain $\mathrm{OCA}+\mathfrak c>\aleph_2$ are periodically announced; none has been verified. *(frontier — verify)*
- **Higher-dimensional and derived-limit interactions.** Work relating OCA and $\mathrm{MA}_{\aleph_1}$ to vanishing of $\lim^n$ over $\omega^\omega$ (Bergfalk, Lambie-Hanson, and coauthors) has produced new OCA-consequences at $\aleph_n$; whether these constrain $\mathfrak c$ is under active study. *(frontier — verify)*

## 8. Future Work

- Isolate a *rectangular* form of the dichotomy provable from $\mathrm{OCA}_{[T]}$; this is the direct route to Moore's hypothesis and hence to $\mathfrak c=\aleph_2$.
- Analyse OCA-forcing in the presence of a fixed $\aleph_3$-sized set of reals: determine whether "no uncountable clique" is preserved by $\sigma$-closed forcing, the standard preservation failure point.
- Determine the exact relationship between OCA, $\mathfrak b=\aleph_2$, and $\mathrm{MA}_{\aleph_1}(\sigma\text{-centered})$; a proof that OCA implies $\mathfrak p>\aleph_1$ would be a major step.
- Push Feng's definable results: is $\mathrm{OCA}(\boldsymbol\Sigma^1_2)$ equiconsistent with an inaccessible, and does the projective hierarchy version give bounds on $\mathfrak c$ in inner models?

## 9. Key References

- **[Foundational]** U. Abraham, M. Rubin, S. Shelah. *On the consistency of some partition theorems for continuous colorings, and the structure of $\aleph_1$-dense real order types.* Annals of Pure and Applied Logic 29 (1985), 123–206.
- **[Foundational]** S. Todorcevic. *Partition Problems in Topology.* Contemporary Mathematics 84, American Mathematical Society, 1989.
- **[SOTA]** J. T. Moore. *Open colorings, the continuum and the second uncountable cardinal.* Proceedings of the AMS 130 (2002), 2753–2759.
- **[SOTA]** Q. Feng. *Homogeneity for open partitions of pairs of reals.* Transactions of the AMS 339 (1993), 659–684.
- **[SOTA]** B. Veličković. *OCA and automorphisms of $\mathcal P(\omega)/\mathrm{fin}$.* Topology and its Applications 49 (1993), 1–13.
- **[SOTA]** I. Farah. *All automorphisms of the Calkin algebra are inner.* Annals of Mathematics 173 (2011), 619–661.
- **[SOTA]** I. Farah. *Analytic Quotients: Theory of Liftings for Quotients over Analytic Ideals on the Integers.* Memoirs of the AMS 148, no. 702, 2000.
- **[Survey]** M. Bekkali. *Topics in Set Theory* (Lebesgue measurability, large cardinals, forcing axioms, rho-functions; notes on lectures by S. Todorcevic). Lecture Notes in Mathematics 1476, Springer, 1991.
- **[Survey]** M. Scheepers. *Gaps in $\omega^\omega$.* Israel Mathematical Conference Proceedings 6 (1993), 439–561.
- **[Survey]** J. T. Moore. *The proper forcing axiom.* Proceedings of the ICM, Hyderabad, 2010, Vol. II, 3–29.
- **[Context]** S. Todorcevic, I. Farah. *Some Applications of the Method of Forcing.* Yenisei, Moscow, 1995.
- **[Context]** A. S. Kechris, S. Solecki, S. Todorcevic. *Borel chromatic numbers.* Advances in Mathematics 141 (1999), 1–44.

## 10. Worked Example / Concrete Special Case

**The product-order colouring on Baire space.** Work in $X\subseteq\mathbb N^\omega$ with the product topology. For $f\ne g$ put
$$\{f,g\}\in K_0 \iff \exists m,n\ \big(f(m)<g(m)\ \wedge\ f(n)>g(n)\big),$$
"$f$ and $g$ cross"; $K_1$ is its complement, i.e. $f\le g$ everywhere or $g\le f$ everywhere.

*$K_0$ is open.* Membership is witnessed by two coordinates $m,n$; the set of pairs with $f(m)<g(m)$ and $f(n)>g(n)$ is a basic open box in $X^2\setminus\Delta$, and $K_0$ is the union of these over $m,n$.

*$K_1$-homogeneous sets are countable.* Let $C\subseteq\mathbb N^\omega$ satisfy $[C]^2\subseteq K_1$, so $(C,\le)$ is linearly ordered by everywhere-domination. Fix $n$. The map $f\mapsto f(n)$ is monotone from the linear order $C$ into $\mathbb N$, hence takes countably many values and partitions $C$ into at most countably many convex blocks $\mathcal B_n$. Let $\mathcal B=\bigwedge_{n<\omega}\mathcal B_n$ be the common refinement; since a common refinement of countably many countable convex partitions of a linear order has countably many blocks (the set of cut points is a countable union of countable sets), $|\mathcal B|\le\aleph_0$. Two elements of $C$ in the same block agree at every coordinate, hence are equal. So $|C|=|\mathcal B|\le\aleph_0$.

*Consequence.* For uncountable $X$, the second alternative of OCA is impossible: a countable union of $K_1$-homogeneous sets is countable. Therefore
$$\mathrm{OCA}\ \Longrightarrow\ \text{every uncountable }X\subseteq\mathbb N^\omega\text{ contains an uncountable pairwise-crossing family,}$$
i.e. an uncountable antichain in the product order.

*Where the axiom is doing work.* If $X$ is analytic, this is a ZFC theorem by Feng's result, and the antichain can be taken perfect. Concretely, for $X=\mathbb N^\omega$ itself the family $\{f_r\}_{r\in 2^\omega}$ with $f_r(2k)=r(k)$, $f_r(2k+1)=1-r(k)$ is a size-$\mathfrak c$ antichain: for $r\ne s$ with $r(k)=0,s(k)=1$ we get $f_r(2k)<f_s(2k)$ and $f_r(2k+1)>f_s(2k+1)$, so every pair crosses. For a *general* $X$ of size $\aleph_1$ — a set with no definable structure, such as one added by an $\omega_1$-length recursion under CH — no ZFC argument produces the antichain, and the conclusion is exactly the OCA instance. This is the smallest visible case of the gap in §6: OCA constrains sets of size $\aleph_1$ inside $\mathbb N^\omega$, and the open problem is whether that constraint propagates far enough up to cap $\mathfrak c$ at $\aleph_2$.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*