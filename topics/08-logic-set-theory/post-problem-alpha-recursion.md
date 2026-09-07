---
id: 08-logic-set-theory/post-problem-alpha-recursion
title: "Post's Problem for Alpha Recursion Theory"
topic: 08-logic-set-theory
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Post's Problem for Alpha Recursion Theory

> **Topic:** Mathematical Logic & Set Theory · **ID:** `08-logic-set-theory/post-problem-alpha-recursion` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

Post's problem asks for a recursively enumerable set that is neither decidable nor complete. Its generalization to $\alpha$-recursion theory, where computation is measured by an admissible ordinal $\alpha$ in place of $\omega$, is:

> **Question (Post's problem for $\alpha$).** For every admissible ordinal $\alpha$, do there exist $\alpha$-recursively enumerable sets $A, B \subseteq \alpha$ with
> $$A \not\le_\alpha B \quad\text{and}\quad B \not\le_\alpha A\,?$$
> Equivalently, is there an $\alpha$-r.e. set $C$ with $\emptyset <_\alpha C <_\alpha K_\alpha$, where $K_\alpha$ is the complete $\alpha$-r.e. set?

A complete solution must produce such sets **for every** admissible $\alpha$, uniformly enough to survive the pathologies that arise when $\alpha$ is not regular in the ambient universe, when the $\Sigma_1$-projectum $\alpha^*$ is far below $\alpha$, or when the sets constructed fail to be regular. The answer is **yes**: Sacks and Simpson (1972) proved it for all admissible $\alpha$. What remains open — and is the live content of this entry — is the analogous question one level up: for non-admissible $\beta$ in the residual cases, for $E$-recursion, and for the machine models (ordinal Turing/register machines, infinite time machines) that generalize $\alpha$-recursion in incompatible directions.

## 2. Mathematical Foundations

Fix an admissible ordinal $\alpha$, i.e. $L_\alpha \models \mathrm{KP}$ ($\Sigma_1$-collection plus $\Delta_0$-separation). Write:

- **$\alpha$-finite:** $K \subseteq \alpha$ with $K \in L_\alpha$.
- **$\alpha$-r.e.:** $A \subseteq \alpha$ that is $\Sigma_1$-definable over $L_\alpha$ with parameters.
- **$\alpha$-recursive:** $\Delta_1(L_\alpha)$, equivalently $A \in L_\alpha$ when $A \subseteq \alpha$ is bounded.

**Reducibilities.** $A \le_{w\alpha} B$ (weak reducibility) if there is an $\alpha$-r.e. set $W$ of triples such that for all $\alpha$-finite $K, K'$,
$$K \subseteq A \ \wedge\ K' \subseteq \alpha\setminus A \iff \exists\, H, H'\ \big(\langle K,K',H,H'\rangle \in W \wedge H \subseteq B \wedge H' \subseteq \alpha\setminus B\big).$$
$A \le_\alpha B$ (**Sacks reducibility**) additionally requires the neighbourhood condition to be *$\alpha$-finitely* witnessed: the reduction must map $\alpha$-finite queries to $\alpha$-finite answers uniformly, so that $\le_\alpha$ is transitive. For $\alpha = \omega$ both collapse to Turing reducibility.

**Regularity.** $A \subseteq \alpha$ is **regular** if $A \cap \gamma \in L_\alpha$ for all $\gamma < \alpha$. Irregular $\alpha$-r.e. sets exist for many $\alpha$ and break naive priority bookkeeping; hence solutions are demanded in regular form.

**Projectum and cofinality.** The **$\Sigma_1$-projectum** is
$$\alpha^* = \mu\,\gamma \le \alpha\ \big[\exists\, f\ \Sigma_1(L_\alpha)\text{-partial injection } f:\alpha \to \gamma\big],$$
equivalently the least $\gamma$ such that some $\alpha$-r.e. $R \subseteq \gamma$ is not $\alpha$-finite. The **$\Sigma_2$-cofinality** $\sigma\mathrm{cf}_2(\alpha)$ is the least $\gamma$ with a $\Sigma_2(L_\alpha)$ map from $\gamma$ cofinally into $\alpha$. Admissibility gives $\Sigma_1$-cofinality $=\alpha$, but $\alpha^*$ may be as small as $\omega$ (e.g. $\alpha = \aleph_1^L$-like ordinals, or any $\alpha$ with a $\Sigma_1$ map of $\omega$ onto $\alpha$).

**Theorem (Sacks–Simpson, 1972).** For every admissible $\alpha$ there are regular $\alpha$-r.e. sets $A, B$ with $A \not\le_\alpha B$ and $B \not\le_\alpha A$.

The proof replaces the $\omega$-indexed requirement list of Friedberg–Muchnik by **blocks**: requirements are grouped into $\alpha^*$-many blocks each of $\alpha$-finite size, and each block is treated as a single unit of priority. $\Sigma_1$-collection over $L_\alpha$ bounds the injury to each block, so injury sets remain $\alpha$-finite even when $\alpha^* < \alpha$.

## 3. History & State of the Art (SOTA)

- **1944.** Post poses the problem for $\omega$ (Bull. AMS 50).
- **1956–57.** Friedberg and Muchnik independently solve it by the finite injury priority method.
- **1966.** Kreisel–Sacks metarecursion ($\alpha = \omega_1^{\mathrm{CK}}$) and Sacks' work on hyperdegrees give the first ordinal generalization; the metarecursive case is settled there, where $\alpha^* = \alpha$ makes the classical argument nearly literal.
- **1971–72.** Sacks and Simpson, *The $\alpha$-finite injury method*, solve the general admissible case by the blocking technique. This is the theorem the page is titled after.
- **1974–76.** Simpson develops $\alpha$-degree theory; Shore proves the **density theorem** for $\alpha$-r.e. degrees (1976), an infinite-injury argument, and isolates the irregular / non-hyperregular degrees (1975). Lerman constructs maximal $\alpha$-r.e. sets (1974).
- **1978–81.** Maass analyzes inadmissibility and the "admissible collapse"; Sy Friedman develops $\beta$-recursion theory and solves Post's problem without admissibility for a large class of $\beta$, with companion negative results in the relativized setting.
- **1985–90.** Slaman and Sacks push into $E$-recursion; Sacks' *Higher Recursion Theory* (1990) becomes the standard reference.
- **1989–2000s.** Reverse-mathematical calibration: Mytilinaios shows the Friedberg–Muchnik theorem is provable from $\Sigma_1$-induction; Chong–Yang and coauthors analyze priority arguments over models of fragments of $\mathrm{PA}$, where cuts play the role of projecta.
- **2008–2019.** Ordinal computability (Koepke and school) re-derives admissible recursion from machine models; Hamkins–Lewis show Post's problem for infinite time Turing machines has *both* positive and negative solutions depending on the degree notion.

## 4. Partial Results / Verified Cases

| Class of $\alpha$ / setting | Status |
|---|---|
| $\alpha = \omega$ | Solved (Friedberg 1957, Muchnik 1956) |
| $\alpha = \omega_1^{\mathrm{CK}}$ (metarecursion, $\alpha^* = \alpha$) | Solved; classical argument lifts with only bookkeeping changes |
| $\alpha$ admissible with $\alpha^* = \alpha$ ("$\alpha$-regular") | Solved directly by $\alpha$-finite injury |
| $\alpha$ admissible with $\omega \le \alpha^* < \alpha$ | Solved by Sacks–Simpson blocking (1972) — the general theorem |
| $\alpha = \aleph_1^L$, $\alpha$ a cardinal of $L$ | Solved; sets are regular |
| Density of $\alpha$-r.e. degrees, all admissible $\alpha$ | Solved (Shore 1976) |
| Non-admissible $\beta$ with $\beta$ "tame" / suitable projectum data | Solved (S. Friedman 1980, and $\beta$-recursion theory 1979) |
| Models of $\mathrm{I}\Sigma_1$ (fragments of PA) | Solved (Mytilinaios 1989); $\Sigma_1$-induction suffices |
| Infinite time Turing machines | Both a positive and a negative answer, depending on which degree notion (Hamkins–Lewis 2002) |
| $E$-recursion (Kleene recursion in type-3 / set recursion) | **Open in $\mathrm{ZFC}$**; partial positive results under $V=L$ and under reflection hypotheses |
| Residual non-admissible $\beta$ outside Friedman's hypotheses | **Open** |

## 5. Principal Obstacles

- **Failure of $\Sigma_2$-collection.** Priority arguments need to bound the total injury to a requirement. At $\omega$, $\Sigma_2$-induction is free. Over $L_\alpha$ only $\Sigma_1$-collection holds; a $\Sigma_2$ list of injuries can be cofinal in $\alpha$, so "the requirement is injured finitely often" has no analogue. Blocking repairs this only because blocks are $\alpha$-finite and their injury is $\Sigma_1$-bounded — a repair that does not survive into settings where the natural requirement list is itself $\Sigma_2$-cofinal.
- **Projectum collapse.** When $\alpha^* = \omega$, there is a $\Sigma_1$ map of $\omega$ onto $\alpha$: an $\alpha$-r.e. set can be built whose "stages" are indexed by $\omega$ while its content is unbounded in $\alpha$. Enumeration order and ordinal order decouple, so "the state at stage $\sigma$" is no longer $\alpha$-finite.
- **Irregularity.** Non-regular $\alpha$-r.e. sets have $A \cap \gamma \notin L_\alpha$ for some $\gamma < \alpha$, so partial computations cannot be finitely approximated; every construction must additionally *prove* regularity of its output, which is not automatic.
- **Non-admissibility.** For non-admissible $\beta$, $\Sigma_1$-collection fails outright: a $\beta$-finite set can have $\Sigma_1$-image cofinal in $\beta$. Friedman's machinery substitutes "tameness" and admissible collapse, but the arguments are case-split on the structure of $\beta$ rather than uniform.
- **$E$-recursion divergence.** In $E$-recursion, computations may diverge for reasons unrelated to unbounded search; the "$\Sigma_1$ on a divergence-closed structure" analogy breaks, and forcing over the relevant structures (Slaman) requires reflection hypotheses that are not theorems of $\mathrm{ZFC}$.

## 6. The Gap

The admissible case is closed. The gap is between:

1. **Proved:** for every admissible $\alpha$, regular incomparable $\alpha$-r.e. degrees exist, and the $\alpha$-r.e. degrees are dense.
2. **Not proved:** an analogue for $E$-recursion valid in $\mathrm{ZFC}$, and a *uniform* (non-case-split) solution across all non-admissible $\beta$.

Concretely: Slaman's forcing solution for $E$-recursion needs a reflection property of the least $E$-closed ordinal $\kappa^{\mathrm{r}}(V)$ that follows from $V = L$ but is not known to follow from $\mathrm{ZFC}$. The exact step to cross is: replace the reflection hypothesis by an absoluteness argument, or produce a model of $\mathrm{ZFC}$ where every $E$-r.e. degree is $0$ or complete.

## 7. Current Research (as of June 2026)

- **Ordinal computability.** Koepke's school (Bonn) and Carl (Konstanz) re-prove and refine admissible degree theory via ordinal register and Turing machines; the machine formulation gives finer stage structure and has produced new proofs of the Sacks–Simpson theorem with explicit resource bounds. *(frontier — verify)*
- **Reverse recursion theory.** Chong (NUS), Yang (NUS), Slaman (Berkeley) continue calibrating priority arguments against fragments of $\mathrm{PA}$: which degree-theoretic theorems are equivalent to $\mathrm{I}\Sigma_1$, $\mathrm{B}\Sigma_2$, or $\mathrm{I}\Sigma_2$ over cuts. The projectum/cut dictionary is the working tool.
- **$E$-recursion and set recursion.** Sporadic activity; the $\mathrm{ZFC}$ status of Post's problem there is the standing open question flagged in Sacks' monograph and unchanged since.
- **Higher analogues.** $\Pi^1_1$-recursion, $\Sigma_1$-definability over admissible sets with urelements, and infinite-time degree structures remain active for the *structure* of the degrees (embeddings, definability), with Post's problem itself already settled in most of these.

## 8. Future Work

- Eliminate $V = L$ from the $E$-recursion solution, or force a negative answer.
- Give a single uniform construction covering all $\beta$, admissible or not, replacing the current case analysis by projectum and cofinality type.
- Determine whether the Sacks–Simpson sets can always be chosen **hyperregular** (i.e. $\alpha$-recursion in them does not collapse cofinality) simultaneously with incomparability, for all $\alpha$.
- Transfer $\alpha$-degree techniques to computable structure theory over admissible sets, where the analogues of Post's problem for automorphism and isomorphism problems are open.
- Extract explicit complexity bounds from the blocking argument in the ordinal-machine model.

## 9. Key References

- **[Foundational]** E. L. Post. *Recursively enumerable sets of positive integers and their decision problems.* Bulletin of the American Mathematical Society **50** (1944), 284–316.
- **[Foundational]** R. M. Friedberg. *Two recursively enumerable sets of incomparable degrees of unsolvability (solution of Post's problem, 1944).* Proceedings of the National Academy of Sciences USA **43** (1957), 236–238.
- **[Foundational]** G. E. Sacks and S. G. Simpson. *The $\alpha$-finite injury method.* Annals of Mathematical Logic **4** (1972), 343–367.
- **[SOTA]** R. A. Shore. *The recursively enumerable $\alpha$-degrees are dense.* Annals of Mathematical Logic **9** (1976), 123–155.
- **[SOTA]** R. A. Shore. *The irregular and non-hyperregular $\alpha$-r.e. degrees.* Israel Journal of Mathematics **22** (1975), 28–41.
- **[SOTA]** S. D. Friedman. *Post's problem without admissibility.* Advances in Mathematics **35** (1980), 30–49.
- **[SOTA]** S. D. Friedman. *$\beta$-recursion theory.* Transactions of the American Mathematical Society **255** (1979), 173–200.
- **[SOTA]** W. Maass. *Inadmissibility, tame R.E. sets and the admissible collapse.* Annals of Mathematical Logic **13** (1978), 149–170.
- **[SOTA]** T. A. Slaman. *Reflection and forcing in $E$-recursion theory.* Annals of Pure and Applied Logic **29** (1985), 79–106.
- **[SOTA]** J. D. Hamkins and A. Lewis. *Post's problem for supertasks has both positive and negative solutions.* Archive for Mathematical Logic **41** (2002), 507–523.
- **[SOTA]** M. Mytilinaios. *Finite injury and $\Sigma_1$-induction.* Journal of Symbolic Logic **54** (1989), 38–49.
- **[SOTA]** P. Koepke and B. Seyfferth. *Ordinal machines and admissible recursion theory.* Annals of Pure and Applied Logic **160** (2009), 310–318.
- **[Survey]** G. E. Sacks. *Higher Recursion Theory.* Perspectives in Mathematical Logic, Springer, 1990.
- **[Survey]** S. G. Simpson. *Degree theory on admissible ordinals.* In: J. E. Fenstad and P. G. Hinman (eds.), *Generalized Recursion Theory*, North-Holland, 1974, 165–193.
- **[Survey]** M. Carl. *Ordinal Computability: An Introduction to Infinitary Machines.* De Gruyter, 2019.

## 10. Worked Example / Concrete Special Case

**Case $\alpha = \omega_1^{\mathrm{CK}}$ (metarecursion), where $\alpha^* = \alpha$.**

Build $A, B \subseteq \alpha$ meeting, for each $e < \alpha$,
$$R_{2e}: \ A \ne \{e\}^B, \qquad R_{2e+1}: \ B \ne \{e\}^A,$$
where $\{e\}^X$ is the $e$-th $\alpha$-r.e. reduction procedure relative to $X$.

*Construction.* At stage $\sigma < \alpha$ maintain $A_\sigma, B_\sigma \in L_\alpha$ (so both are $\alpha$-finite). Requirement $R_{2e}$ picks a fresh witness $x_e < \alpha$ larger than every number so far mentioned by requirements of higher priority; such $x_e$ exists because the set of mentioned ordinals at stage $\sigma$ is $\alpha$-finite, hence bounded in $\alpha$ by admissibility. If at some stage $\{e\}^{B_\sigma}(x_e)\!\downarrow = 0$ with $\alpha$-finite use $H \subseteq B_\sigma$, put $x_e$ into $A$ and **restrain** $B$ on $\sup(H)+1$. Then $x_e \in A$ but $\{e\}^B(x_e) = 0$, so $R_{2e}$ is met, provided the restraint holds.

*Why it works here.* Injury to $R_{2e}$ comes only from the $<2e$-many higher-priority requirements acting, each at most once. The map
$$\sigma \mapsto (\text{stage at which requirement } \sigma \text{ last acts})$$
is $\Sigma_1$ over $L_\alpha$ with domain the $\alpha$-finite set $2e$, so by $\Sigma_1$-collection its range is **bounded** below $\alpha$. Past that bound, $R_{2e}$ is never injured again. Regularity: $A \cap \gamma$ is decided by stage $\gamma' > \gamma$ for a suitable $\gamma'$, and $A \cap \gamma = A_{\gamma'} \cap \gamma \in L_\alpha$.

**Where this breaks and blocking is needed.** Take $\alpha$ admissible with $\alpha^* = \omega$ — say the least $\alpha$ admitting a $\Sigma_1(L_\alpha)$ surjection $f: \omega \to \alpha$. Now the requirement list $\{R_i : i < \alpha\}$ can be re-indexed by $\omega$ via $f$, and "the requirements of higher priority than $R_{2e}$" is a set of order type $\alpha$ in the $\Sigma_1$ enumeration. The map "last stage of action" now has domain of size $\alpha$, and $\Sigma_1$-collection gives nothing. Sacks–Simpson instead partition the requirements into blocks
$$\mathcal{B}_\xi = \{ R_i : i \in I_\xi \}, \qquad \xi < \alpha^* = \omega, \quad I_\xi \in L_\alpha,$$
so each $I_\xi$ is $\alpha$-finite and there are only $\alpha^*$-many blocks. A block acts as one unit: the restraint imposed by $\mathcal{B}_\xi$ is $\sup$ of the $\alpha$-finitely many individual restraints, which is $<\alpha$ by admissibility, and $\mathcal{B}_\xi$ is injured only by the $\xi$-many earlier blocks. Collection is applied to the **block** index set (of size $<\alpha^*+1$, an $\alpha$-finite object), not to the requirement index set — and the bound reappears. That single move, from per-requirement to per-block bookkeeping, is the whole content of the $\alpha$-finite injury method.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*