---
id: 08-logic-set-theory/martin-conjecture-on-turing-degrees
title: "Martin Conjecture on Turing Degrees"
topic: 08-logic-set-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Martin Conjecture on Turing Degrees

> **Topic:** Mathematical Logic & Set Theory · **ID:** `08-logic-set-theory/martin-conjecture-on-turing-degrees` · **Status:** open

## 1. Problem Statement / Conjecture

Martin's Conjecture asserts that the only definable functions on the Turing degrees are the "obvious" ones: constants, the identity, and transfinite iterates of the Turing jump. Work in $\mathsf{ZF} + \mathsf{DC} + \mathsf{AD}$ (the Axiom of Determinacy), where every function on reals is well behaved; equivalently, work in $\mathsf{ZFC}$ and restrict attention to a definable class of functions (Borel, projective, or $\infty$-Borel).

Let $f : 2^\omega \to 2^\omega$ be **Turing-invariant**: $x \equiv_T y \implies f(x) \equiv_T f(y)$. Then:

- **Part I (dichotomy).** Either $f$ is constant on a cone, i.e. there is $z$ with $f(x) \equiv_T f(z)$ for all $x \geq_T z$; or $f$ is increasing on a cone, i.e. $f(x) \geq_T x$ for all $x$ in some cone.
- **Part II (classification).** The Turing-invariant functions that are increasing on a cone are pre-well-ordered by the relation
$$f \leq_M g \iff f(x) \leq_T g(x) \text{ for all } x \text{ in some cone},$$
and the successor in this pre-well-order is the Turing jump: if $f$ has $\leq_M$-rank $\alpha$, then $x \mapsto f(x)'$ has rank $\alpha + 1$.

A complete solution proves both parts under $\mathsf{AD}$ (or refutes one). A partial solution proves them for a wider definability class or drops a uniformity hypothesis. Both parts are known to **fail** in $\mathsf{ZFC}$ for arbitrary (non-definable) $f$ — see §10 — so the determinacy or definability hypothesis is essential, not cosmetic.

## 2. Mathematical Foundations

**Turing reducibility.** For $x, y \in 2^\omega$, $x \leq_T y$ iff $x = \Phi_e^y$ for some index $e$, where $\{\Phi_e\}_{e\in\omega}$ enumerates the oracle Turing functionals. $\equiv_T$ is the induced equivalence relation; $\mathcal{D} = 2^\omega/\!\equiv_T$ is the upper semilattice of Turing degrees with join $\deg(x) \vee \deg(y) = \deg(x \oplus y)$ and least element $\mathbf{0}$.

**Cones.** For $z \in 2^\omega$, the cone above $z$ is $C_z = \{x : x \geq_T z\}$; $z$ is its base. The **Martin filter** is
$$\mathcal{F} = \{ A \subseteq \mathcal{D} : \exists z\, C_z \subseteq A \}.$$
Since $C_{z_0} \cap C_{z_1} = C_{z_0 \oplus z_1}$ and $\bigcap_n C_{z_n} \supseteq C_{\bigoplus_n z_n}$, $\mathcal{F}$ is a countably complete filter in $\mathsf{ZF}+\mathsf{DC}$.

**Martin's cone theorem** (1968). Assume $\mathsf{AD}$. If $A \subseteq \mathcal{D}$ is a set of degrees, then $A$ or $\mathcal{D}\setminus A$ contains a cone. Hence $\mathcal{F}$ is a countably complete ultrafilter on $\mathcal{D}$ — "Martin measure". Statements true on a cone are said to hold *$\mathcal{F}$-almost everywhere*.

**Jump.** $x' = \{e : \Phi_e^x(e)\!\downarrow\}$, with $x <_T x'$ and $x \leq_T y \implies x' \leq_T y'$. Iterates: $x^{(n+1)} = (x^{(n)})'$, and $x^{(\alpha)}$ for $x$-computable ordinal notations of $\alpha$.

**Uniform invariance.** $f$ is *uniformly degree-invariant* if there is $u : \omega^2 \to \omega^2$ such that whenever $x = \Phi_i^y$ and $y = \Phi_j^x$, writing $u(i,j) = (i^*, j^*)$, we have $f(x) = \Phi_{i^*}^{f(y)}$ and $f(y) = \Phi_{j^*}^{f(x)}$. Reductions between values are computed from the reductions between arguments.

**Order-preserving.** $f$ is order-preserving if $x \leq_T y \implies f(x) \leq_T f(y)$. Every order-preserving $f$ is Turing-invariant; the converse fails.

**Jump operators (Steel).** A *jump operator* is a uniformly degree-invariant, order-preserving $f$ with $f(x) \geq_T x$ on a cone. Part II restricted to this class is Steel's classification theorem.

**Pointed perfect sets.** $P \subseteq 2^\omega$ is pointed if every $x \in P$ computes (a code for) $P$. Pointed perfect trees are the standard tool for producing cones inside definable sets and give $\mathsf{ZFC}$ substitutes for determinacy at the Borel level.

## 3. History & State of the Art (SOTA)

- **1968.** D. A. Martin proves the cone theorem from $\mathsf{AD}$ (Bull. AMS 74). The Martin measure becomes the basic "almost everywhere" notion in the degrees, and Martin formulates the conjecture in the 1970s in the Cabal seminar circle.
- **Background question.** Sacks (1963) asks whether Post's problem has a degree-invariant solution: is there invariant $f$ with $x <_T f(x) <_T x'$ on a cone? Part I + Part II forbid it; Lachlan (1975) rules out uniform enumeration-operator solutions.
- **1982.** J. R. Steel, *A classification of jump operators* (JSL 47): under $\mathsf{AD}$, the uniformly invariant order-preserving functions increasing on a cone are pre-well-ordered by $\leq_M$ with jump as successor — Part II for jump operators.
- **1988.** Slaman–Steel, *Definable functions on degrees* (Cabal Seminar 81–85, LNM 1333): Part I for uniformly invariant functions under $\mathsf{AD}$, and Part I for Borel order-preserving functions in $\mathsf{ZFC}$ (via Borel determinacy). Also: no uniformly invariant solution to Post's problem.
- **1988.** Becker, *A characterization of jump operators* (JSL 53): jump operators coincide with $\Sigma^1_1$-style canonical operators on a cone, sharpening Steel's picture.
- **2016.** Marks–Slaman–Steel (Cabal Seminar vol. III): Part II implies Turing equivalence $E_T$ is not a universal countable Borel equivalence relation, and yields non-embedding results in the Borel-reducibility hierarchy. This turned MC into a load-bearing conjecture for descriptive set theory.
- **2018.** Kihara–Montalbán prove the uniform Martin conjecture for many-one degrees (Trans. AMS 370), a full analogue in a coarser degree structure.
- **2021–2023.** Lutz–Siskind prove Part I for *all* order-preserving functions (no uniformity), and for measure-preserving functions — the first removal of a uniformity hypothesis.

Status: **open**. Neither part is known for arbitrary Borel Turing-invariant functions.

## 4. Partial Results / Verified Cases

| Class of $f$ | Part I | Part II | Source |
|---|---|---|---|
| Uniformly degree-invariant | ✔ ($\mathsf{AD}$) | ✔ for order-preserving | Slaman–Steel 1988; Steel 1982 |
| Order-preserving (no uniformity) | ✔ ($\mathsf{AD}$) | open | Lutz–Siskind 2021 |
| Measure-preserving | ✔ ($\mathsf{AD}$) | open | Lutz–Siskind |
| Borel, order-preserving | ✔ ($\mathsf{ZFC}$) | open | Slaman–Steel 1988 |
| Many-one degrees, uniform | ✔ | ✔ | Kihara–Montalbán 2018 |
| Arbitrary invariant $f$ | open | open | — |

Concrete verified instances: constants $f(x)=c$ (rank: constant branch); identity (rank $0$); $x \mapsto x^{(n)}$ (rank $n$); $x \mapsto x^{(\omega)}$ (rank $\omega$); $x \mapsto \mathcal{O}^x$ (hyperjump, rank a large countable ordinal); "least degree of a nonstandard model of PA relative to $x$" is $\equiv_M$ the identity on a cone. Bard (Proc. AMS, 2020) verified a local form of the uniform conjecture within intervals $[\mathbf{a}, \mathbf{a}']$. No invariant function has ever been produced whose $\leq_M$-behaviour lies outside the conjectured list.

## 5. Principal Obstacles

- **Uniformity is the whole difficulty.** Every proof of Part I from Steel onward extracts, from a winning strategy $\sigma$ in a Martin game, a *reduction index* computing $f(x)$ from $f(y)$. Without uniformity, the strategy tells you a reduction exists but gives no way to find it computably in the play, and the game-theoretic argument fails to close.
- **Determinacy games are the only known engine.** Martin-style games decide statements about a cone but produce no *structure*; there is no known combinatorial invariant of a degree-invariant function analogous to a derivative or a measure.
- **Coding failure.** Constructing a counterexample would require coding a global choice function into the degrees, but under $\mathsf{AD}$ every such choice is $\mathcal{F}$-measurable — the constructions that succeed in $\mathsf{ZFC}$ (§10) use a well-ordering of $2^\omega$ and die immediately.
- **Part II needs an ordinal analysis.** Proving $\leq_M$ is a pre-well-order requires ruling out infinite $\leq_M$-descending sequences $f_0 >_M f_1 >_M \cdots$; countable completeness of $\mathcal{F}$ gives a single cone on which all comparisons hold, but there is no known well-foundedness principle to contradict — one needs a rank function, and only the uniform case supplies one (via Steel's coding of $f$ by a $\Sigma^1_1$ operator).
- **No "intermediate operator" argument.** The jump-successor claim requires showing nothing sits strictly between $f$ and $f'$ on a cone. Priority-method constructions from classical recursion theory produce intermediate degrees pointwise but destroy invariance.

## 6. The Gap

The proven region is: *(order-preserving or uniformly invariant)* $\Rightarrow$ Part I. The conjecture asks for: *(Turing-invariant, definable)* $\Rightarrow$ Part I and Part II.

Two precise crossings are needed.

1. **From order-preserving to invariant.** Given invariant $f$, produce, on a cone, either an order-preserving $g$ with $g \equiv_M f$, or a direct game argument. The obstacle: invariance constrains $f$ only along $\equiv_T$-classes and says nothing about $f$'s behaviour across the partial order.
2. **From Part I to Part II without uniformity.** Even granting Part I in full, the pre-well-ordering is open: one must define an ordinal rank $\rho(f)$ for non-uniform $f$, show $\rho(f') = \rho(f)+1$, and show $\rho$ is total. Currently $\rho$ exists only as Steel's rank on jump operators.

## 7. Current Research (as of June 2026)

- **Berkeley/UCLA school** (Slaman, Steel, Marks, Lutz, Siskind). The Lutz–Siskind method — "basis" arguments producing pointed perfect sets on which an arbitrary function acquires uniformity — is the main new tool since 1988. Active target: extend it from order-preserving to all Borel invariant functions. *(frontier — verify)*
- **Countable Borel equivalence relations.** Kechris–Marks and collaborators use MC as a source of rigidity: MC Part II $\Rightarrow$ $E_T$ is not universal, $\Rightarrow$ no Borel embedding of $E_\infty$ into $E_T$. Progress on either side is traded back and forth.
- **Analogue structures.** Kihara–Montalbán's many-one result and ongoing analogues for enumeration degrees, Weihrauch degrees, and arithmetic/hyperarithmetic equivalence test whether the phenomenon is specific to $\leq_T$. *(frontier — verify)*
- **Choiceless set theory.** Work in the Larson–Zapletal "geometric set theory" framework studies the Martin filter in symmetric $\mathsf{ZF}$ models, isolating exactly how much choice kills the conjecture.
- **Measure- and category-preserving variants.** Lutz–Siskind's measure-preserving theorem suggests a program of proving Part I under any "regularity" side condition, then removing them one at a time.

## 8. Future Work

- Prove Part I for all Borel Turing-invariant functions in $\mathsf{ZFC}$; this is regarded as the cleanest next milestone and would already answer Sacks' degree-invariant Post problem for Borel operators.
- Develop a rank theory for non-uniform functions: find an ordinal assignment $\rho$ on $\leq_M$-classes definable from a cone base, not from a uniformity function.
- Settle whether Part I implies Part II, an implication conjectured but unproven.
- Establish (or refute) MC-style classification for enumeration degrees and for $\equiv_A$ (arithmetic equivalence), where Marks–Slaman–Steel already have partial classification.
- Extract consequences in the other direction: use failures of universality for $E_T$ to constrain what a counterexample to MC could look like.

## 9. Key References

- **[Foundational]** D. A. Martin. *The axiom of determinateness and reduction principles in the analytical hierarchy.* Bulletin of the American Mathematical Society 74 (1968), 687–689.
- **[Foundational]** J. R. Steel. *A classification of jump operators.* The Journal of Symbolic Logic 47 (1982), 347–358.
- **[Foundational]** T. A. Slaman and J. R. Steel. *Definable functions on degrees.* In *Cabal Seminar 81–85*, Lecture Notes in Mathematics 1333, Springer, 1988, pp. 37–55.
- **[Foundational]** H. Becker. *A characterization of jump operators.* The Journal of Symbolic Logic 53 (1988), 708–728.
- **[Foundational]** G. E. Sacks. *Degrees of Unsolvability.* Annals of Mathematics Studies 55, Princeton University Press, 1963.
- **[Classical]** A. H. Lachlan. *Uniform enumeration operations.* The Journal of Symbolic Logic 40 (1975), 401–409.
- **[SOTA / Recent]** A. Marks, T. A. Slaman, J. R. Steel. *Martin's conjecture, arithmetic equivalence, and countable Borel equivalence relations.* In *Ordinal Definability and Recursion Theory: The Cabal Seminar, Volume III*, ASL Lecture Notes in Logic 43, Cambridge University Press, 2016.
- **[SOTA / Recent]** T. Kihara and A. Montalbán. *The uniform Martin's conjecture for many-one degrees.* Transactions of the American Mathematical Society 370 (2018).
- **[SOTA / Recent]** P. Lutz and B. Siskind. *Part 1 of Martin's conjecture for order-preserving and measure-preserving functions.* arXiv preprint, 2021.
- **[SOTA / Recent]** V. Bard. *Uniform Martin's conjecture, locally.* Proceedings of the American Mathematical Society 148 (2020).
- **[Thesis]** P. Lutz. *Results on Martin's Conjecture.* Ph.D. thesis, University of California, Berkeley, 2021.
- **[Survey]** T. A. Slaman. *Aspects of the Turing jump.* In *Logic Colloquium 2000*, ASL Lecture Notes in Logic 19, 2005.
- **[Background]** R. I. Soare. *Recursively Enumerable Sets and Degrees.* Perspectives in Mathematical Logic, Springer, 1987.
- **[Background]** A. S. Kechris. *Classical Descriptive Set Theory.* Graduate Texts in Mathematics 156, Springer, 1995.
- **[Background]** P. B. Larson and J. Zapletal. *Geometric Set Theory.* Mathematical Surveys and Monographs 248, American Mathematical Society, 2020.

## 10. Worked Example / Concrete Special Case

**(a) Why the cone theorem gives an ultrafilter.** Let $A \subseteq \mathcal{D}$ be invariant. Consider the game where players alternate bits producing $x \in 2^\omega$; Player II wins iff $\deg(x) \in A$. Under $\mathsf{AD}$ one player has a winning strategy $\sigma$. If II wins, take any $z \geq_T \sigma$. Then $z$ can be played by I against $\sigma$ (I plays $z$'s bits), producing an output $x$ with $z \leq_T x \leq_T z \oplus \sigma \equiv_T z$, so $\deg(z) = \deg(x) \in A$. Hence $C_\sigma \subseteq A$. Symmetrically if I wins, $C_\sigma \subseteq \mathcal{D}\setminus A$.

**(b) A verified instance of both parts.** Take $f(x) = x'$.
- *Invariance:* if $x = \Phi_i^y$ and $y = \Phi_j^x$ then $x' \leq_T y'$ and $y' \leq_T x'$, so $x' \equiv_T y'$.
- *Uniform invariance:* the index $i^*$ with $x' = \Phi_{i^*}^{y'}$ is computed primitively recursively from $i$ by the $s$-$m$-$n$ theorem; so $u(i,j)$ exists and $f$ is a jump operator.
- *Part I:* $x <_T x'$ everywhere, so $f$ is increasing on the cone above $\mathbf{0}$ — the second alternative, and $f$ is constant on no cone since $x' \not\equiv_T y'$ for suitable $x <_T y$.
- *Part II:* $\mathrm{id}$ has rank $0$; $f = \mathrm{id}'$ has rank $1$; $x \mapsto x''$ has rank $2$. Steel's theorem says no jump operator $g$ satisfies $x <_T g(x) <_T x'$ on a cone — the degree-invariant Post problem has no uniform solution.

**(c) Why choice must be excluded.** In $\mathsf{ZFC}$, $|\mathcal{D}| = 2^{\aleph_0} = \kappa$ and there are exactly $\kappa$ cones, each of size $\kappa$. Enumerate the cones as $\langle C_\alpha : \alpha < \kappa\rangle$ and recursively choose distinct degrees $\mathbf{a}_\alpha \neq \mathbf{b}_\alpha$ in $C_\alpha$ avoiding all earlier choices (possible since fewer than $\kappa$ degrees are used at stage $\alpha$). Put $A = \{\mathbf{a}_\alpha\}$. Then neither $A$ nor $\mathcal{D}\setminus A$ contains a cone. Define
$$f(x) = \begin{cases} 0' & \deg(x) \in A,\\ 0'' & \deg(x) \notin A.\end{cases}$$
$f$ is Turing-invariant by construction. It is not constant on any cone (every cone meets $A$ and its complement) and not increasing on any cone (for $x \geq_T 0''$, $f(x) \leq_T 0'' \leq_T x$ with $f(x)\not\geq_T x$ whenever $x >_T 0''$). So Part I fails outright under $\mathsf{AC}$ — confirming that the conjecture is a statement about *definable* functions, and that any proof must use determinacy or Borel-level regularity in an essential way.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*