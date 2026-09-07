---
id: 08-logic-set-theory/invertibility-turing-jump
title: "Invertibility of the Turing Jump Operator"
topic: 08-logic-set-theory
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Invertibility of the Turing Jump Operator

> **Topic:** Mathematical Logic & Set Theory · **ID:** `08-logic-set-theory/invertibility-turing-jump` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

The Turing jump $\mathbf{a} \mapsto \mathbf{a}'$ maps the degrees of unsolvability $\mathcal{D}$ into $\mathcal{D}$, is strictly increasing ($\mathbf{a} < \mathbf{a}'$) and monotone ($\mathbf{a} \le \mathbf{b} \Rightarrow \mathbf{a}' \le \mathbf{b}'$). Its range lies in the upper cone $\{\mathbf{a} : \mathbf{a} \ge \mathbf{0}'\}$. **Invertibility** asks, in increasing strength:

1. **(Surjectivity / jump inversion.)** Is every $\mathbf{a} \ge \mathbf{0}'$ of the form $\mathbf{b}'$? — **Yes**, Friedberg's Completeness Criterion (1957).
2. **(Local inversion.)** For a prescribed complexity class $\Gamma$ of degrees $\mathbf{a} \ge \mathbf{0}'$, can the preimage $\mathbf{b}$ be found inside a prescribed substructure (below $\mathbf{0}'$, c.e., minimal, of prescribed jump class)?
3. **(Structural inversion.)** Is there a *degree-invariant, order-preserving* map $J^{-}$ with $(J^{-}(\mathbf{a}))' = \mathbf{a}$ on a cone — i.e. is the jump invertible *as an operator on the degree structure*, not merely pointwise?
4. **(Definability.)** Is the graph $\{(\mathbf{a},\mathbf{b}) : \mathbf{b} = \mathbf{a}'\}$ first-order definable in $(\mathcal{D}, \le)$? — **Yes**, Shore–Slaman (1999).

Items 1 and 4 are theorems; item 2 is a rich, largely mapped landscape; item 3 is the live core, and is equivalent on a cone to **Part 2 of Martin's Conjecture**. A complete resolution of the remaining question means either constructing a degree-invariant order-preserving jump inverse on a cone, or proving (in ZF + AD, or ZFC + large cardinals for Borel/definable maps) that none exists.

## 2. Mathematical Foundations

Fix a standard enumeration $\{\Phi_e\}_{e\in\omega}$ of oracle Turing functionals. For $A \subseteq \omega$,
$$A' \;=\; \{\, e \in \omega \;:\; \Phi_e^{A}(e)\!\downarrow \,\}.$$
$A'$ is $\Sigma^0_1(A)$-complete under $\le_m$; $A <_T A'$ (**Turing 1939 / Kleene–Post 1954**); $A \le_T B \Rightarrow A' \le_T B'$. Degrees are $\deg(A) = \{B : B \equiv_T A\}$, $\mathcal{D} = 2^\omega/\!\equiv_T$ with join $\mathbf{a}\cup\mathbf{b} = \deg(A\oplus B)$. Iterates: $A^{(0)}=A$, $A^{(n+1)} = (A^{(n)})'$; the **Post hierarchy** gives $X \in \Sigma^0_{n+1} \iff X$ is c.e. in $\emptyset^{(n)}$.

**Relativized arithmetic.** $X \le_T A^{(n)} \iff X$ is $\Delta^0_{n+1}(A)$ (Post). The **Shoenfield limit lemma**: $X \le_T \emptyset' \iff X = \lim_s f(s,\cdot)$ for computable $f$.

**Jump classes.** For $\mathbf{a}\le\mathbf{0}'$: $\mathbf{a}$ is **low$_n$** if $\mathbf{a}^{(n)} = \mathbf{0}^{(n)}$, **high$_n$** if $\mathbf{a}^{(n)} = \mathbf{0}^{(n+1)}$.

**Degree-invariant functions.** $f : 2^\omega \to 2^\omega$ is *degree-invariant* if $A \equiv_T B \Rightarrow f(A)\equiv_T f(B)$; it induces $\hat f:\mathcal{D}\to\mathcal{D}$. A set $C\subseteq\mathcal D$ is a **cone** if $C = \{\mathbf{x} : \mathbf{x}\ge\mathbf{d}\}$. Under $\mathsf{AD}$, Martin's measure ($C$ measure one iff $C$ contains a cone) is a countably complete ultrafilter on $\mathcal D$.

**Martin's Conjecture** (for degree-invariant $f$, on a cone):
- *Part 1:* either $\hat f$ is constant on a cone, or $\hat f(\mathbf{x}) \ge \mathbf{x}$ on a cone.
- *Part 2:* the degree-invariant $f$ with $\hat f(\mathbf x)\ge \mathbf x$ on a cone are prewellordered by "$\le$ on a cone", with successor given by the jump: rank $\alpha$ corresponds to $\mathbf{x}\mapsto \mathbf{x}^{(\alpha)}$.

Part 2 forbids a degree-invariant $J^-$ with $(J^-\mathbf x)'=\mathbf x$ on a cone, since $J^-$ would sit strictly between rank $0$ (identity) and rank $1$ (jump).

## 3. History & State of the Art (SOTA)

- **1936–1944.** Turing introduces relative computability; Post (1944) formulates the theory of degrees and the jump.
- **1954.** Kleene and Post establish the basic order-theoretic facts about $\mathcal{D}$ below $\mathbf{0}'$.
- **1957.** **Friedberg** proves the Completeness Criterion: $\mathbf{a} \ge \mathbf{0}' \Rightarrow \exists \mathbf{b}\,(\mathbf{b}' = \mathbf{a}\ \text{and}\ \mathbf{b}\cup\mathbf{0}' = \mathbf{a})$. The jump is surjective onto its evident range — question 1 closed, by a one-page finite-extension argument.
- **1959.** **Shoenfield** shows every $\mathbf{a}$ that is c.e. in and above $\mathbf{0}'$ is $\mathbf{b}'$ for some $\mathbf{b}\le\mathbf{0}'$.
- **1963.** **Sacks** strengthens this: $\mathbf b$ may be taken **c.e.**, and jump inversion can preserve order above a fixed parameter.
- **1982.** **Steel**, *A classification of jump operators*, isolates uniformly-defined jump operators and proves rigidity results under determinacy.
- **1988.** **Slaman–Steel** prove Martin's Conjecture Part 1 for *uniformly* degree-invariant functions and Part 2 for uniformly invariant order-preserving functions.
- **1997.** **Downey–Shore**: there is no degree-invariant "half jump" — no order-preserving degree-invariant $f$ with $f(f(\mathbf x)) \equiv \mathbf x'$ for all $\mathbf x$ in a suitable sense. The first hard negative on structural invertibility.
- **1999.** **Shore–Slaman**, *Defining the Turing jump*: the jump relation is first-order definable in $(\mathcal{D},\le)$, via Slaman–Woodin coding plus the Posner–Robinson join theorem.
- **2021–2024.** **Lutz–Siskind** prove Part 1 of Martin's Conjecture for all *order-preserving* functions (dropping uniformity), the strongest advance in three decades; Lutz's thesis extends the toolkit to measure-preserving maps. This is the "solved-recently" component: the invariance side of jump invertibility is now settled for order-preserving maps.

## 4. Partial Results / Verified Cases

| Setting | Result | Source |
|---|---|---|
| All $\mathbf a\ge\mathbf 0'$ | $\exists\mathbf b:\mathbf b'=\mathbf b\cup\mathbf 0'=\mathbf a$ | Friedberg 1957 |
| $\mathbf a$ c.e. in and $\ge \mathbf 0'$ (i.e. $\Sigma^0_2$-presentable) | $\mathbf b \le \mathbf 0'$ exists | Shoenfield 1959 |
| Same $\mathbf a$ | $\mathbf b$ can be chosen **c.e.** | Sacks 1963 |
| $\mathbf a \ge \mathbf 0'$, $\mathbf c$ given with $\mathbf c'\le\mathbf a$ | $\mathbf b\ge\mathbf c$ can be arranged (order-preserving pointwise inversion) | Sacks 1963 |
| $\mathbf a \ge \mathbf 0'$ | $\mathbf b$ can be taken **minimal** ($\mathbf 0 < \mathbf b$, no degree strictly between) | Cooper 1973; Jockusch–Posner |
| Any $\mathbf a \ge \mathbf 0'$, any noncomputable $\mathbf c$ | Posner–Robinson: $\exists \mathbf g$ with $\mathbf c\cup\mathbf g=\mathbf g'=\mathbf a$ (for $\mathbf a=\mathbf 0'$) | Posner–Robinson 1981 |
| $n$-th jump, all $n\ge 1$ | $\mathbf a \ge \mathbf 0^{(n)} \Rightarrow \exists\mathbf b\,\mathbf b^{(n)}=\mathbf a$ | iterate Friedberg |
| Enumeration degrees | Full jump inversion for the enumeration jump above $\mathbf 0_e'$ | Soskov 2000 |
| Pseudo-jump operators $V^X$ | Inversion $V^B \equiv_T \emptyset'$ for c.e. operators (analogue of Friedberg) | Jockusch–Shore 1983/84 |
| Uniformly degree-invariant order-preserving maps | Martin's Conjecture Part 2 holds ⇒ **no** invariant jump inverse | Slaman–Steel 1988 |
| Order-preserving (not nec. uniform) maps | Martin's Conjecture Part 1 holds | Lutz–Siskind 2021 |
| "Half jumps" | No degree-invariant order-preserving square root of the jump | Downey–Shore 1997 |

Failures that delimit the picture: no $\mathbf b$ with $\mathbf b' = \mathbf a$ can be found below $\mathbf 0'$ when $\mathbf a$ is not $\Sigma^0_2$; and inversion is never *uniform* in $\mathbf a$ (Section 5).

## 5. Principal Obstacles

- **Non-uniformity is intrinsic.** Friedberg's construction consults an $A$-oracle to answer $\Sigma^0_1$ extension questions; different $A$'s in the same degree give non-$\equiv_T$ outputs unless extra care is taken, and no single functional $\Psi$ satisfies $(\Psi^A)' \equiv_T A$ for all $A\ge_T\emptyset'$. Finite-extension forcing produces *a* preimage but destroys invariance — exactly the property question 3 demands.
- **Priority arguments do not see cones.** The finite-injury/infinite-injury machinery that proves every local inversion theorem (Sacks, Shoenfield) is a stage-by-stage combinatorial method with no mechanism for asserting "on a cone". The remaining question is a statement about *all* degree-invariant functions, a set-theoretic quantifier the priority method cannot reach.
- **Determinacy is load-bearing and expensive.** Martin's measure requires $\mathsf{AD}$ (or Borel determinacy for Borel $f$, which by Friedman is not provable in ZFC minus replacement). Any negative answer to structural invertibility must be proved from determinacy, and Part 2 has resisted because the Slaman–Steel technique needs *uniformity* to build a Martin-style game whose winning strategy computes the inverse.
- **The uniformity gap.** Lutz–Siskind removed uniformity for Part 1 by a "sliding" / Borel-selection argument; the analogous move for Part 2 fails because Part 2 asserts a *global prewellordering*, requiring one to compare two arbitrary invariant functions, not just compare $f$ to the identity.
- **Coding limits.** Shore–Slaman definability shows the jump is intrinsic to $(\mathcal D,\le)$, so any inverse operator is also definable — which means a positive answer would have to be definable, and definable maps are precisely those most constrained by determinacy. The two horns pinch.

## 6. The Gap

Proven (Section 4): **pointwise** inversion, everywhere on the cone above $\mathbf 0'$, with control of complexity, order, and minimality; and non-existence of invariant inverses in the *uniform* category.

Wanted (Section 1, item 3): a dichotomy for *arbitrary* degree-invariant $f$. The precise open step is **Part 2 of Martin's Conjecture without a uniformity hypothesis**: show that any degree-invariant $f$ with $\mathbf x \le \hat f(\mathbf x) \le \mathbf x'$ on a cone satisfies $\hat f(\mathbf x)\equiv\mathbf x$ or $\hat f(\mathbf x)\equiv\mathbf x'$ on a cone. Equivalently: **the jump has no degree-invariant inverse and no degree-invariant fractional iterate.** Lutz–Siskind closed the order-preserving case of Part 1; the gap is (i) Part 1 for functions that are invariant but not order-preserving, and (ii) all of Part 2 beyond uniform maps.

## 7. Current Research (as of June 2026)

- **Berkeley / UCLA (Slaman, Marks, Siskind, Lutz).** Extending the Lutz–Siskind technique from Part 1 to the "no intermediate operator between $\mathrm{id}$ and $'$" instance of Part 2. *(frontier — verify)*
- **Descriptive set theory link.** Marks–Slaman–Steel connect Martin's Conjecture to the theory of countable Borel equivalence relations: Part 2 implies $\equiv_T$ has no Borel "half-way" reduction, and progress flows in both directions.
- **Wisconsin / Notre Dame (Goh, Shore, Lempp).** Jump inversion in weaker structures: $\alpha$-jump inversion for computable ordinals, hyperjump inversion, and inversion of pseudo-jump operators along transfinite iterations.
- **Weihrauch / uniform computability (Brattka, Pauly, Valenti).** The Weihrauch jump $f \mapsto f'$ is a genuinely different operator: it is *not* surjective onto its evident range, so the uniform analogue of Friedberg's theorem **fails**, sharpening the diagnosis that Friedberg's success is a non-uniform accident.
- **Enumeration and Muchnik degrees (Sofia school, after Soskov).** Jump inversion transfers to $\mathcal D_e$ but the invariance question there is untouched.

## 8. Future Work

- Prove Part 2 of Martin's Conjecture for order-preserving functions, matching the Lutz–Siskind Part 1 result; the "no jump inverse" corollary follows immediately.
- Find a game-theoretic characterization of degree-invariance that survives without uniformity — Slaman and Steel have repeatedly flagged this as the missing tool.
- Settle whether ZFC alone refutes a *Borel* degree-invariant jump inverse (currently only determinacy arguments apply).
- Push jump inversion into $\alpha$-recursion and the hyperdegrees: for which admissible $\alpha$ does Friedberg's criterion hold verbatim?
- Classify which substructures of $\mathcal D$ (minimal covers, $\mathrm{GH}_1$, the c.e. degrees) admit *simultaneous* inversion of all jumps in a uniform family.

## 9. Key References

- **[Foundational]** R. M. Friedberg. *A criterion for completeness of degrees of unsolvability.* Journal of Symbolic Logic, 22(2):159–160, 1957.
- **[Foundational]** J. R. Shoenfield. *On degrees of unsolvability.* Annals of Mathematics, 69(3):644–653, 1959.
- **[Foundational]** G. E. Sacks. *Recursive enumerability and the jump operator.* Transactions of the AMS, 108:223–239, 1963.
- **[Foundational]** G. E. Sacks. *Degrees of Unsolvability.* Annals of Mathematics Studies 55, Princeton University Press, 1963 (2nd ed. 1966).
- **[Structural]** J. R. Steel. *A classification of jump operators.* Journal of Symbolic Logic, 47(2):347–358, 1982.
- **[Structural]** T. A. Slaman and J. R. Steel. *Definable functions on degrees.* In: Cabal Seminar 81–85, Lecture Notes in Mathematics 1333, Springer, 37–55, 1988.
- **[Structural]** R. Downey and R. A. Shore. *There is no degree invariant half-jump.* Proceedings of the AMS, 125(10):3033–3037, 1997.
- **[Definability]** R. A. Shore and T. A. Slaman. *Defining the Turing jump.* Mathematical Research Letters, 6:711–722, 1999.
- **[SOTA / Recent]** P. Lutz and B. Siskind. *Part 1 of Martin's Conjecture for order-preserving and measure-preserving functions.* arXiv:2111.02024, 2021.
- **[SOTA / Recent]** A. Marks, T. A. Slaman and J. R. Steel. *Martin's conjecture, arithmetic equivalence, and countable Borel equivalence relations.* In: Ordinal Definability and Recursion Theory (Cabal Seminar Vol. III), Cambridge University Press, 2016.
- **[Related]** C. G. Jockusch and R. A. Shore. *Pseudo-jump operators I: The r.e. case.* Transactions of the AMS, 275:599–609, 1983.
- **[Related]** I. N. Soskov. *A jump inversion theorem for the enumeration jump.* Archive for Mathematical Logic, 39:417–437, 2000.
- **[Related]** V. Brattka, G. Gherardi and A. Marcone. *The Bolzano–Weierstrass theorem is the jump of weak Kőnig's lemma.* Annals of Pure and Applied Logic, 163(6):623–655, 2012.
- **[Survey]** R. I. Soare. *Turing Computability: Theory and Applications.* Springer, 2016.
- **[Survey]** R. I. Soare. *Recursively Enumerable Sets and Degrees.* Perspectives in Mathematical Logic, Springer, 1987.

## 10. Worked Example / Concrete Special Case

**Friedberg inversion, executed on $A = \emptyset''$.** We build $B$ with $B' \equiv_T \emptyset''$ and $B \oplus \emptyset' \equiv_T \emptyset''$, so $\deg(B)$ is a preimage of $\mathbf 0''$ that does **not** itself compute $\mathbf 0'$ in general.

Construct finite binary strings $\sigma_0 \subset \sigma_1 \subset \cdots$, $\sigma_0 = \langle\rangle$, and set $B = \bigcup_s \sigma_s$.

*Stage $2e$ (jump control).* Ask
$$Q_e:\quad \exists \tau \supseteq \sigma_{2e}\ \ \Phi_e^{\tau}(e)\!\downarrow.$$
$Q_e$ is $\Sigma^0_1$ in the (finite) parameter $\sigma_{2e}$, hence decidable by $\emptyset' \le_T A$.
- If **yes**: let $\tau$ be the least such string in the standard ordering and put $\sigma_{2e+1} = \tau$. Since $\tau \subset B$ and use is finite, $\Phi_e^{B}(e)\!\downarrow$, so $e \in B'$.
- If **no**: put $\sigma_{2e+1} = \sigma_{2e}{}^\frown 0$. No extension ever converges, so $\Phi_e^{B}(e)\!\uparrow$ and $e \notin B'$.

*Stage $2e+1$ (coding).* Put $\sigma_{2e+2} = \sigma_{2e+1}{}^\frown A(e)$, appending the $e$-th bit of $\emptyset''$.

**$B' \le_T A$.** The whole sequence $\langle \sigma_s\rangle$ is computable from $A$: the $Q_e$ queries need only $\emptyset'\le_T A$, and the coding bits are read off $A$. By the case analysis, $e \in B' \iff Q_e$ answered yes. So $B' \le_T A = \emptyset''$.

**$A \le_T B'$.** Recover the construction from $B'$ by induction. Given $\sigma_{2e}$, ask the oracle $B'$ whether $e \in B'$. If yes, search effectively for the least $\tau\supseteq\sigma_{2e}$ with $\Phi_e^\tau(e)\!\downarrow$ — the search halts because such a $\tau$ exists — and set $\sigma_{2e+1}=\tau$. If no, $\sigma_{2e+1} = \sigma_{2e}{}^\frown 0$. Either way we know $n_e := |\sigma_{2e+1}|$ exactly, and $A(e) = B(n_e)$. Since $B \le_T B'$, we get $A \le_T B'$.

Hence $B' \equiv_T \emptyset''$, i.e. $\deg(B)' = \mathbf 0''$.

**Where invariance breaks.** Replace $A=\emptyset''$ by any $\tilde A \equiv_T \emptyset''$ with a different bit sequence. Stage $2e+1$ codes $\tilde A(e)$ instead of $A(e)$, so a different $\tilde B$ is produced; $\tilde B' \equiv_T \emptyset''$ still, but nothing forces $\tilde B \equiv_T B$ — the two outputs are built by incomparable finite-extension paths. This is exactly the failure of degree-invariance: the map $A \mapsto B$ is a legitimate function on *sets* but induces no function on *degrees*. Martin's Conjecture Part 2 predicts that this failure is unavoidable — no repair of the construction can yield a degree-invariant inverse on a cone.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*