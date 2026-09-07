---
id: 08-logic-set-theory/bi-interpretability-of-turing-degrees
title: "Bi Interpretability of Turing Degrees"
topic: 08-logic-set-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Bi-Interpretability of the Turing Degrees

> **Topic:** Mathematical Logic & Set Theory · **ID:** `08-logic-set-theory/bi-interpretability-of-turing-degrees` · **Status:** open

## 1. Problem Statement / Conjecture

Let $\mathcal{D} = (2^\omega/\equiv_T, \leq_T, \vee)$ be the upper semilattice of Turing degrees. Simpson (1977) showed that the first-order theory of $\mathcal{D}$ is recursively isomorphic to true second-order arithmetic $\mathrm{Th}(Z_2)$. That is an *interpretation in one direction*: a copy of second-order arithmetic can be read off inside $\mathcal{D}$. The open problem asks for the converse half, making the two structures mutually interpretable in a coherent way.

**Bi-Interpretability Conjecture (Slaman–Woodin).** $\mathcal{D}$ is bi-interpretable with second-order arithmetic, with parameters. Explicitly: there is a formula scheme producing, from parameters $\bar p$, an interpretation of a standard model $\mathcal{M}_{\bar p} \cong (\omega, +, \times, 0, 1, \in, 2^\omega)$ inside $\mathcal{D}$, together with a formula $\Phi(\bar p, x, y)$ such that
$$\mathcal{D} \models \Phi(\bar p, R, \mathbf{a}) \iff R \text{ codes (in } \mathcal{M}_{\bar p}) \text{ a real } A \text{ with } \deg_T(A) = \mathbf{a}.$$
Informally: the map sending a degree to a code for one of its members is itself definable in $\mathcal{D}$.

A complete solution is a proof of this scheme, or a refutation. The standard route to refutation is exhibiting a nontrivial automorphism of $\mathcal{D}$, since bi-interpretability implies:

1. **Rigidity.** $\mathrm{Aut}(\mathcal{D}) = \{\mathrm{id}\}$.
2. **Maximal definability.** A relation on $\mathcal{D}$ is first-order definable in $\mathcal{D}$ **iff** it is definable in second-order arithmetic and invariant under Turing equivalence.

Item 2 is the real payload: it would say the degree order remembers everything about relative computability that is expressible at all.

## 2. Mathematical Foundations

**Degrees.** For $A, B \subseteq \omega$, $A \leq_T B$ iff $A$ is computable from an oracle for $B$; $\equiv_T$ is the induced equivalence and $\mathbf{a} = \deg_T(A)$. Then $\mathcal{D}$ is an upper semilattice of size $2^{\aleph_0}$ with least element $\mathbf{0}$, join $\mathbf{a}\vee\mathbf{b} = \deg_T(A \oplus B)$, and jump operator $\mathbf{a}' = \deg_T(A')$ where $A' = \{e : \Phi_e^A(e){\downarrow}\}$.

**Interpretation.** A structure $\mathcal{M}$ is *interpretable with parameters* in $\mathcal{D}$ if there are formulas $\delta(\bar p, x)$, $\varepsilon(\bar p, x, y)$, and $\varphi_R(\bar p, \bar x)$ for each relation $R$ of $\mathcal{M}$, such that $\delta^{\mathcal{D}}/\varepsilon^{\mathcal{D}}$ with the induced relations is isomorphic to $\mathcal{M}$.

**Bi-interpretability.** $\mathcal{D}$ and $Z_2$ are bi-interpretable if each interprets the other and the composite isomorphisms
$$\mathcal{D} \;\longrightarrow\; \mathcal{D}^{\,\mathcal{M}^{\mathcal{D}}}, \qquad \mathcal{M} \;\longrightarrow\; \mathcal{M}^{\,\mathcal{D}^{\mathcal{M}}}$$
are definable in the respective structures. For $\mathcal{D}$ the second map is automatic; the first is exactly the formula $\Phi$ of §1.

**Key classical theorems used.**

- *Spector exact pair* (1956). For any countable ideal $I \subseteq \mathcal{D}$ there exist $\mathbf{b}_0,\mathbf{b}_1$ with
$$\mathbf{x} \leq \mathbf{b}_0 \wedge \mathbf{x} \leq \mathbf{b}_1 \iff \mathbf{x} \in I.$$
So every countable ideal is definable from two parameters.
- *Slaman–Woodin coding* (1986). Every countable relation on $\mathcal{D}$ is uniformly definable from finitely many parameters: there is a fixed formula $\psi(\bar p, \bar x)$ such that for each countable $R \subseteq \mathcal{D}^n$ some $\bar p$ gives $R = \{\bar x : \mathcal{D}\models\psi(\bar p,\bar x)\}$.
- *Simpson* (1977). $\mathrm{Th}(\mathcal{D}) \equiv_1 \mathrm{Th}(Z_2)$, both of degree $\deg_T(Z_2)$.
- *Shore–Slaman* (1999). The relation $\mathbf{y} = \mathbf{x}'$ is first-order definable in $\mathcal{D}$, via definability of "$\mathbf{x}$ is arithmetic in $\mathbf{y}$" using Kumabe–Slaman forcing.

**Homogeneity fails.** $\mathcal{D} \not\cong \mathcal{D}(\ge \mathbf{a})$ in general (Feiner, Shore), so the conjecture cannot be attacked by pushing everything to a cone by homogeneity.

## 3. History & State of the Art (SOTA)

- **1944–1956.** Post, Kleene–Post, and Spector establish the basic structure: density failures, minimal covers, exact pairs.
- **1977.** Simpson: $\mathrm{Th}(\mathcal{D})$ is as complex as $Z_2$. Interpretation of arithmetic into $\mathcal{D}$ from parameters.
- **1980.** Nerode–Shore: definability results and automorphism bases; every automorphism of $\mathcal{D}$ is determined by its action on a cone.
- **1986.** Slaman–Woodin, *Definability in the Turing degrees*: the coding theorem; $\mathrm{Aut}(\mathcal{D})$ is countable; every automorphism is fixed on a cone. The bi-interpretability conjecture is formulated here and refined in their later monograph.
- **1990s.** Slaman–Woodin push the fixed cone down to $\mathbf{0}''$ and prove the *relativized* form of the conjecture: bi-interpretability holds for the cone $\mathcal{D}(\ge \mathbf{0}'')$. Consequences: $|\mathrm{Aut}(\mathcal{D})| \le \aleph_0$ and each automorphism is arithmetically definable.
- **1998–1999.** Nies–Shore–Slaman prove bi-interpretability up to double jump for the c.e. degrees $\mathcal{R}$; Shore–Slaman define the jump in $\mathcal{D}$.
- **2014.** Shore: bi-interpretability up to double jump for $\mathcal{D}(\le \mathbf{0}')$.
- **Status 2026.** The global conjecture is open. No credible nontrivial automorphism exists; Cooper's announced construction of one (late 1990s) was never verified by the community and is not accepted.

## 4. Partial Results / Verified Cases

| Setting | Result | Source |
|---|---|---|
| $\mathcal{D}(\ge \mathbf{0}'')$ | Full bi-interpretability with $Z_2$; the cone is rigid | Slaman–Woodin |
| $\mathcal{D}$, global | Every automorphism is the identity on $\{\mathbf{x} : \mathbf{x} \ge \mathbf{0}''\}$ | Slaman–Woodin |
| $\mathcal{D}$, global | $\mathrm{Aut}(\mathcal{D})$ countable; each automorphism induced by a map arithmetic in its restriction to a cone | Slaman–Woodin 1986 |
| $\mathcal{D}$, global | Jump $\mathbf{x}\mapsto\mathbf{x}'$, the relation $\mathbf{x}\in \mathrm{Arith}(\mathbf{y})$, and $\mathbf{0}^{(n)}$ for each $n$ are definable | Shore–Slaman 1999 |
| $\mathcal{R}$ (c.e. degrees) | Bi-interpretability *up to double jump*: any automorphism preserves double jump; $\mathrm{Aut}(\mathcal{R})$ countable | Nies–Shore–Slaman 1998 |
| $\mathcal{D}(\le\mathbf{0}')$ | Bi-interpretability up to double jump | Shore 2014 |
| Countable relations | Uniform parameter-definability (coding theorem) | Slaman–Woodin 1986 |
| $\mathcal{D}_e$ (enumeration degrees) | Rigid: $\mathrm{Aut}(\mathcal{D}_e)$ trivial | Soskova 2016 |

Thus the conjecture is *theorem* on every cone above $\mathbf{0}''$ and *open only below it* — but "below it" carries all of the difficulty, because a putative automorphism has $2^{\aleph_0}$ degrees of freedom in the region $\mathcal{D}(\not\ge\mathbf{0}'')$.

## 5. Principal Obstacles

- **Coding needs parameters that sit high.** The Slaman–Woodin coding of a countable relation requires parameters computing enough to run an exact-pair/minimal-pair construction with the coded objects. Recovering the code of an *arbitrary* degree $\mathbf{a}$ with $\mathbf{a} \not\ge \mathbf{0}''$ demands parameters below or incomparable with $\mathbf{a}$, and no forcing is known that makes the coding uniform in that regime.
- **The double jump barrier is intrinsic to the forcing.** Kumabe–Slaman forcing with use-monotone partial functionals produces generics whose definable properties are controlled only two jumps up: the relevant genericity/decidability facts are $\Sigma^0_2$ in the parameters. Every known argument that a degree's code is recoverable loses exactly two jumps, which is why "up to double jump" recurs in $\mathcal{R}$, in $\mathcal{D}(\le\mathbf{0}')$, and globally.
- **Non-homogeneity.** Since $\mathcal{D} \not\cong \mathcal{D}(\ge \mathbf{a})$ for suitable $\mathbf{a}$, the cone result cannot be transported downward by an isomorphism. There is no known "local-to-global" transfer.
- **No structure theory below $\mathbf{0}''$.** The initial segments of $\mathcal{D}$ realize all countable upper semilattices with least element (Lachlan–Lebeuf), so low degrees are combinatorially wild; there is no invariant to attach to a general $\mathbf{a}$ that a hypothetical automorphism must preserve.
- **Failure of standard model theory.** $\mathcal{D}$ is not $\omega$-saturated in any usable way, has no stability-theoretic tameness, and its theory is as complex as $Z_2$; classification-theoretic tools give nothing.

## 6. The Gap

Proven: for $\mathbf{a} \ge \mathbf{0}''$, the relation "$R$ codes a real of degree $\mathbf{a}$" is definable from parameters. Conjectured: the same for **all** $\mathbf{a} \in \mathcal{D}$.

The precise missing step is a *parameter-uniform decoding below the double jump*: a formula $\Phi(\bar p, x, y)$, with parameters not required to compute $\mathbf{a}''$, that identifies the code of an arbitrary degree. Equivalently, one must show that a hypothetical automorphism $\pi$ with $\pi \restriction \mathcal{D}(\ge \mathbf{0}'') = \mathrm{id}$ is the identity everywhere. Currently $\pi$ is known to be arithmetically definable and to fix the arithmetic degrees; nothing forces $\pi(\mathbf{a}) = \mathbf{a}$ for a single 1-generic or minimal $\mathbf{a}$.

## 7. Current Research (as of June 2026)

- **Berkeley school (Slaman, Woodin, students).** Continued work on the unpublished monograph *Definability in Degree Structures* and on lowering the fixed cone from $\mathbf{0}''$ toward $\mathbf{0}'$. *(frontier — verify)*
- **Cornell (Shore) and collaborators.** Extending bi-interpretability-up-to-double-jump techniques to further local structures ($\mathcal{D}(\le\mathbf{0}^{(n)})$, degrees of $n$-c.e. sets).
- **Wisconsin / Sofia (M. Soskova, Ganchev, Kent).** Definability and rigidity in $\mathcal{D}_e$ and in the $\Sigma^0_2$ enumeration degrees, where full rigidity was obtained; transfer of those methods back to $\mathcal{D}$ is an active question.
- **Martin's conjecture program (Marks, Montalbán, Slaman, Steel, Lutz, Siskind).** Determinacy-based classification of degree-invariant functions. Under $\mathrm{AD}$, Martin's conjecture would classify all such functions on a cone, closely related to the rigidity half of bi-interpretability. *(frontier — verify)*
- **Reverse-mathematical calibration.** Measuring which fragments of $Z_2$ suffice to formalize the coding theorems, so that the conjecture's consequences can be separated by strength.

## 8. Future Work

- Reduce the fixed cone from $\mathbf{0}''$ to $\mathbf{0}'$, then to a cone above an arbitrary non-computable degree. Each reduction has historically required a new forcing.
- Develop a forcing whose genericity is decided one jump up rather than two — this is the single technical device that would collapse the "double jump" losses across $\mathcal{R}$, $\mathcal{D}(\le\mathbf{0}')$ and $\mathcal{D}$ simultaneously.
- Prove rigidity directly: show that any automorphism fixing the arithmetic degrees fixes all 1-generic degrees, then use minimal covers to propagate.
- Settle whether a relative version holds for $\mathcal{D}(\le \mathbf{a})$ for all $\mathbf{a}$, giving a uniform local theory.
- Determine whether bi-interpretability is provable in $\mathrm{ZFC}$ at all, or whether some form of independence is possible; no forcing extension is known to add an automorphism of $\mathcal{D}$.

## 9. Key References

- **[Foundational]** C. Spector. *On degrees of recursive unsolvability.* Annals of Mathematics 64 (1956), 581–592.
- **[Foundational]** S. G. Simpson. *First-order theory of the degrees of recursive unsolvability.* Annals of Mathematics 105 (1977), 121–139.
- **[Foundational]** A. Nerode, R. A. Shore. *Reducibility orderings: theories, definability and automorphisms.* Annals of Mathematical Logic 18 (1980), 61–89.
- **[Foundational]** T. A. Slaman, W. H. Woodin. *Definability in the Turing degrees.* Illinois Journal of Mathematics 30 (1986), 320–334.
- **[SOTA]** R. A. Shore, T. A. Slaman. *Defining the Turing jump.* Mathematical Research Letters 6 (1999), 711–722.
- **[SOTA]** A. Nies, R. A. Shore, T. A. Slaman. *Interpretability and definability in the recursively enumerable degrees.* Proceedings of the London Mathematical Society (3) 77 (1998), 241–291.
- **[SOTA]** R. A. Shore. *Biinterpretability up to double jump in the degrees below $\mathbf{0}'$.* Proceedings of the American Mathematical Society 142 (2014), 351–360.
- **[SOTA]** M. I. Soskova. *The automorphism group of the enumeration degrees.* Annals of Pure and Applied Logic 167 (2016), 982–999.
- **[Survey]** T. A. Slaman. *Global properties of the Turing degrees and the Turing jump.* In *Computational Prospects of Infinity, Part I: Tutorials*, IMS Lecture Notes Series vol. 14, World Scientific, 2008, 83–101.
- **[Survey]** R. A. Shore. *The Turing degrees: an introduction.* In *Forcing, Iterated Ultrapowers, and Turing Degrees*, IMS Lecture Notes Series vol. 29, World Scientific, 2016, 39–121.
- **[Book]** M. Lerman. *Degrees of Unsolvability: Local and Global Theory.* Springer, 1983.
- **[Book]** A. Montalbán. *Computable Structure Theory: Within the Arithmetic.* Cambridge University Press, 2021.

## 10. Worked Example / Concrete Special Case

**Goal.** Show concretely how a countable, canonically-given set of degrees becomes first-order definable from two parameters, and where the same move stalls for an arbitrary degree.

**Step 1 — the ideal.** Take the arithmetic degrees
$$I = \{\mathbf{x} \in \mathcal{D} : \exists n\; \mathbf{x} \le \mathbf{0}^{(n)}\}.$$
$I$ is a countable ideal: closed downward, and closed under join since $\mathbf{0}^{(m)}\vee\mathbf{0}^{(n)} = \mathbf{0}^{(\max(m,n))}$.

**Step 2 — Spector exact pair.** Spector's theorem applied to the ascending sequence $\mathbf{0} < \mathbf{0}' < \mathbf{0}'' < \cdots$ yields degrees $\mathbf{b}_0, \mathbf{b}_1$ with
$$\mathbf{x} \le \mathbf{b}_0 \ \wedge\ \mathbf{x}\le \mathbf{b}_1 \iff \mathbf{x}\in I.$$
Construction sketch: build $B_0, B_1 \subseteq \omega\times\omega$ by finite conditions so that column $n$ of each $B_i$ is $\emptyset^{(n)}$ (giving $\supseteq$), while diagonalizing against all pairs $(\Phi_e,\Phi_j)$ with $\Phi_e^{B_0} = \Phi_j^{B_1} = X$ total, forcing $X \le_T \emptyset^{(n)}$ for the $n$ current at that stage (giving $\subseteq$).

**Step 3 — a definition with parameters.** With $\bar p = (\mathbf{b}_0,\mathbf{b}_1)$,
$$\mathrm{Arith}(\mathbf{x}) \;\equiv\; \mathbf{x}\le \mathbf{b}_0 \wedge \mathbf{x}\le\mathbf{b}_1$$
defines the arithmetic degrees from parameters. Shore–Slaman upgrade this to a *parameter-free* definition of the relation "$\mathbf{x}$ is arithmetic in $\mathbf{y}$", and then define the jump: $\mathbf{y} = \mathbf{x}'$ is the least degree that is $\Sigma_1$-complete relative to $\mathbf{x}$ inside the definable arithmetic hierarchy over $\mathbf{x}$.

**Step 4 — the interpretation of arithmetic.** Inside $\mathcal{D}$, pick parameters coding a countable independent set $\{\mathbf{c}_n\}_{n\in\omega}$ together with coded relations $S = \{(\mathbf{c}_n,\mathbf{c}_{n+1})\}$, $P = \{(\mathbf{c}_m,\mathbf{c}_n,\mathbf{c}_{m+n})\}$, $T = \{(\mathbf{c}_m,\mathbf{c}_n,\mathbf{c}_{mn})\}$. By the coding theorem, all three are definable from a fixed finite parameter tuple with a single formula, so $(\omega,+,\times)$ is interpreted. Adding coded sets of the $\mathbf{c}_n$ interprets full $Z_2$ — this is Simpson's direction.

**Step 5 — where it breaks.** Bi-interpretability needs the *reverse* dictionary: given an arbitrary $\mathbf{a}$, a definable way to point at a code $R \subseteq \{\mathbf{c}_n\}$ for some $A \in \mathbf{a}$. If $\mathbf{a} \ge \mathbf{0}''$, one can choose the parameters $\bar p$ recursively in $\mathbf{a}''$ and run the Slaman–Woodin decoding: $\Phi(\bar p,R,\mathbf{a})$ holds iff the ideal generated by $R$'s exact pair meets $\mathcal{D}(\le\mathbf{a})$ in exactly $\{\mathbf{x} : \mathbf{x}\le\mathbf{a}\}$. If instead $\mathbf{a}$ is, say, a minimal degree below $\mathbf{0}'$, then $\mathbf{a}$ computes no exact pair for any infinite ideal it does not already bound, the parameters must come from outside $\mathcal{D}(\le\mathbf{a})$, and no uniform choice is known. That single failure — decoding without two jumps of overhead — is the whole open problem.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*