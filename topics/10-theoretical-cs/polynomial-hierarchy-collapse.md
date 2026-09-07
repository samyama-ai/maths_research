---
id: 10-theoretical-cs/polynomial-hierarchy-collapse
title: "Polynomial Hierarchy Collapse"
topic: 10-theoretical-cs
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Polynomial Hierarchy Collapse

> **Topic:** Theoretical Computer Science · **ID:** `10-theoretical-cs/polynomial-hierarchy-collapse` · **Status:** open

## 1. Problem Statement / Conjecture

The polynomial hierarchy $\mathrm{PH}=\bigcup_{k\ge 0}\Sigma^p_k$ is the tower of complexity classes obtained by alternating existential and universal polynomially-bounded quantifiers over a polynomial-time predicate. The **collapse problem** asks:

> Is the polynomial hierarchy **proper** (infinite), i.e. is $\Sigma^p_k \subsetneq \Sigma^p_{k+1}$ for every $k \ge 0$? Or does there exist a finite $k$ with $\mathrm{PH} = \Sigma^p_k$?

The standard conjecture is that **PH is infinite**: no collapse occurs at any level. A complete resolution requires either

1. a proof that $\Sigma^p_k \ne \Sigma^p_{k+1}$ for all $k$ (which implies $\mathrm{P}\ne\mathrm{NP}$ as the case $k=0$, and is therefore at least as hard), or
2. an explicit $k$ and a proof that $\Sigma^p_{k+1}\subseteq\Sigma^p_k$.

Neither direction is known for a single value of $k$. Even $\Sigma^p_1 \ne \Sigma^p_2$ (i.e. $\mathrm{NP}\ne\Sigma^p_2$) is open, and is strictly stronger than $\mathrm{P}\ne\mathrm{NP}$ is known to be — in fact all separations $\Sigma^p_k \neq \Sigma^p_{k+1}$ for $k\ge 1$ imply $\mathrm{P} \neq \mathrm{NP}$, while no converse implication is known.

## 2. Mathematical Foundations

**Quantifier definition.** Set $\Sigma^p_0=\Pi^p_0=\mathrm{P}$. For $k\ge 1$, a language $L\subseteq\{0,1\}^*$ is in $\Sigma^p_k$ iff there is a polynomial $q$ and a polynomial-time decidable relation $R$ with

$$x\in L \iff \exists y_1\in\{0,1\}^{q(|x|)}\ \forall y_2 \ \exists y_3\cdots Q_k y_k : R(x,y_1,\dots,y_k)=1,$$

where $Q_k=\exists$ if $k$ is odd and $\forall$ if $k$ is even. Dually $\Pi^p_k=\mathrm{co}\Sigma^p_k$, starting with $\forall$.

**Oracle definition.** Equivalently $\Sigma^p_{k+1}=\mathrm{NP}^{\Sigma^p_k}$, $\Pi^p_{k+1}=\mathrm{coNP}^{\Sigma^p_k}$, $\Delta^p_{k+1}=\mathrm{P}^{\Sigma^p_k}$, giving

$$\mathrm{P}\subseteq\mathrm{NP}\subseteq\Sigma^p_2\subseteq\cdots\subseteq \mathrm{PH}=\bigcup_k\Sigma^p_k\subseteq\mathrm{PSPACE}.$$

**Complete problems.** $\Sigma_k\mathrm{SAT}$ — deciding whether $\exists \bar y_1\forall \bar y_2\cdots Q_k\bar y_k\,\varphi(\bar y_1,\dots,\bar y_k)$ holds for a Boolean formula $\varphi$ — is $\Sigma^p_k$-complete under Karp reductions (Wrathall 1976; Stockmeyer 1976). $\mathrm{PH}$ itself has a complete problem **iff** it collapses.

**Upward collapse (the key structural lemma).** For every $k\ge 1$,

$$\Sigma^p_k=\Pi^p_k \ \Longrightarrow\ \mathrm{PH}=\Sigma^p_k, \qquad \Sigma^p_k=\Sigma^p_{k+1}\ \Longrightarrow\ \mathrm{PH}=\Sigma^p_k.$$

So the hierarchy is either strictly infinite or collapses at the first level where two consecutive classes coincide; there is no "partial" collapse.

**Non-uniform hypotheses.** $\mathrm{P/poly}$ is the class of languages decided by polynomial-size circuit families. The Karp–Lipton theorem states

$$\mathrm{NP}\subseteq\mathrm{P/poly}\ \Longrightarrow\ \mathrm{PH}=\Sigma^p_2,$$

sharpened to $\mathrm{PH}=\mathrm{ZPP}^{\mathrm{NP}}$ (Köbler–Watanabe) and to $\mathrm{PH}=\mathrm{S}^p_2$ (Cai; Sengupta), with $\mathrm{S}^p_2\subseteq\mathrm{ZPP}^{\mathrm{NP}}\subseteq\Sigma^p_2\cap\Pi^p_2$.

**Containments used constantly.** $\mathrm{BPP}\subseteq\Sigma^p_2\cap\Pi^p_2$ (Sipser–Gács–Lautemann); $\mathrm{PH}\subseteq\mathrm{P}^{\\#\mathrm{P}}$ (Toda 1991); $\mathrm{AM}\subseteq\Pi^p_2$.

## 3. History & State of the Art (SOTA)

- **1972–1976.** Meyer and Stockmeyer introduce the hierarchy while studying the space complexity of regular expressions with squaring; Stockmeyer's *The polynomial-time hierarchy* (TCS, 1976) and Wrathall's companion paper fix the definitions, completeness results and the upward-collapse lemma.
- **1975.** Baker–Gill–Solovay show $\mathrm{P}$ vs $\mathrm{NP}$ relativizes both ways, immediately implying no relativizing proof can settle collapse.
- **1980.** Karp–Lipton link non-uniform circuit upper bounds to collapse.
- **1983–1986.** Sipser, Yao and finally Håstad prove that constant-depth circuits require size $2^{\Omega(n^{1/(d-1)})}$ for parity and, more relevantly, that the depth-$d$ $\mathrm{AC}^0$ hierarchy is strict — yielding an oracle $A$ with $\mathrm{PH}^A$ infinite.
- **1989.** Ko constructs, for each $k$, an oracle relative to which $\mathrm{PH}$ has exactly $k$ levels.
- **1991.** Toda: $\mathrm{PH}\subseteq\mathrm{P}^{\\#\mathrm{P}}$ — the entire hierarchy sits inside one counting oracle.
- **2015.** Rossman–Servedio–Tan prove an *average-case* depth hierarchy theorem for $\mathrm{AC}^0$, implying $\mathrm{PH}^A$ is infinite relative to a **random** oracle $A$ with probability 1 — the strongest evidence for non-collapse.
- **2019.** Raz–Tal give an oracle separating $\mathrm{BQP}$ from $\mathrm{PH}$, resolving Aaronson's forrelation program.
- **2024.** Chen–Hirahara–Ren and, independently, Li prove $\mathrm{S}_2\mathrm{E}/_1$ (and hence $\Sigma_2\mathrm{E}$) requires circuits of size $2^n/n$ — the first near-maximum lower bound at that level, obtained by "range avoidance" / single-valued-$\mathrm{FS}_2\mathrm{P}$ techniques.

## 4. Partial Results / Verified Cases

- **Relativized worlds, all levels.** Håstad (1986) plus Rossman–Servedio–Tan (2015): for a random oracle $A$, $\Sigma^{p,A}_k\subsetneq\Sigma^{p,A}_{k+1}$ for **every** $k$, almost surely. Conversely Ko (1989) gives oracles collapsing at each prescribed level $k$, and $A=\mathrm{TQBF}$ gives $\mathrm{PH}^A=\mathrm{PSPACE}^A$.
- **Bounded-depth circuit analogue — fully solved.** The $\mathrm{AC}^0$ "hierarchy" is unconditionally strict: depth $d+1$, size $O(n)$ circuits compute functions requiring size $\exp(\Omega(n^{1/d}))$ at depth $d$ (Håstad; RST for the average-case version).
- **Query/decision-tree complexity — fully solved.** The analogue of $\Sigma^{dt}_k$ vs $\Sigma^{dt}_{k+1}$ separates unconditionally by explicit AND-OR tree functions.
- **Communication complexity — levels 1–2 solved.** $\Sigma^{cc}_2 \ne \Pi^{cc}_2$ and related separations in the Babai–Frankl–Simon hierarchy are known (Göös–Pitassi–Watson, 2015 onward); higher levels remain partially open.
- **Conditional collapses that are theorems.** $\mathrm{P}=\mathrm{NP}\Rightarrow\mathrm{PH}=\mathrm{P}$; $\mathrm{NP}\subseteq\mathrm{P/poly}\Rightarrow\mathrm{PH}=\mathrm{S}^p_2$; $\mathrm{coNP}\subseteq\mathrm{NP/poly}\Rightarrow\mathrm{PH}=\Sigma^p_3$ (Yap 1983); $\mathrm{NP}$ has a sparse Turing-hard set $\Rightarrow \mathrm{PH}=\Sigma^p_2$; graph isomorphism $\mathrm{NP}$-complete $\Rightarrow\mathrm{PH}=\Sigma^p_2$ (Boppana–Håstad–Zachos 1987); $\mathrm{PH}=\mathrm{PSPACE}\Rightarrow$ collapse.
- **Lower bounds at level 2.** Kannan (1982): $\Sigma^p_2\cap\Pi^p_2$ contains languages of circuit complexity $\omega(n^k)$ for each fixed $k$ — so $\Sigma^p_2 \not\subseteq \mathrm{SIZE}(n^k)$.

## 5. Principal Obstacles

- **Relativization (Baker–Gill–Solovay 1975; Ko 1989).** Oracles exist making $\mathrm{PH}$ infinite and making it collapse at any chosen level. Any proof technique that stays valid under oracle access — diagonalization, simulation, standard reductions — cannot decide the question.
- **Natural proofs (Razborov–Rudich 1997).** Separating levels via circuit lower bounds runs into the barrier that any "large" and "constructive" combinatorial property distinguishing hard functions would break pseudorandom generators, contradicting standard hardness assumptions. The $\mathrm{AC}^0$ methods (switching lemma, random restrictions) that *do* separate the bounded-depth analogue are natural in exactly this sense and provably do not scale past $\mathrm{AC}^0[p]$.
- **Algebrization (Aaronson–Wigderson 2009).** Arithmetization — the technique behind $\mathrm{IP}=\mathrm{PSPACE}$ and Toda's theorem — also fails: there are algebraic oracle extensions consistent with both collapse and non-collapse.
- **No "hardest" object.** If $\mathrm{PH}$ were infinite it has no complete problem, so one cannot pin the question to a single language and attack it directly; and the candidate hard instances at level $k$ ($\Sigma_k\mathrm{SAT}$) look structurally identical to SAT under all known measures.
- **Self-reducibility of the collapse.** Because collapse propagates upward, proving *any* separation $\Sigma^p_k\neq\Pi^p_k$ implies $\mathrm{P}\neq\mathrm{NP}$. Every level is therefore at least as hard as the flagship open problem.

## 6. The Gap

Section 4 establishes the separations only in **restricted computational models** — constant-depth circuits, decision trees, two-party communication, and relativized Turing machines — where the adversary's access to the input is information-theoretically limited and random restrictions apply. Section 1 asks about **uniform polynomial-time computation with unrestricted access**.

Precisely: the switching lemma proves that a depth-$(k+1)$ alternating circuit family cannot be simulated at depth $k$ without exponential size blow-up. Translating that into $\Sigma^p_k \ne \Sigma^p_{k+1}$ would require showing that a $\Sigma^p_{k+1}$ machine's *polynomially many* alternations cannot be traded for polynomial-time preprocessing — but polynomial-time preprocessing is precisely what random restrictions cannot control, since a poly-time predicate can encode global structure (parity, arithmetic, PRG outputs) that survives any restriction. **The gap is the step from non-uniform, depth-bounded, restriction-vulnerable circuits to uniform, unbounded-fan-in, poly-time-computable predicates.** No known technique crosses it, and the three barriers above say that no *relativizing*, *naturalizing*, or *algebrizing* technique ever will.

## 7. Current Research (as of June 2026)

- **Meta-complexity and MCSP.** The dominant program: Hirahara, Ren, Chen, Santhanam and collaborators (NII Tokyo, Oxford, Berkeley, IAS) study the Minimum Circuit Size Problem and $\mathrm{K^{poly}}$-complexity as a route to non-relativizing lower bounds. Hardness of MCSP under randomized reductions would place strong constraints on level-2 collapse.
- **Range avoidance and $\mathrm{S}_2\mathrm{E}$.** Following Chen–Hirahara–Ren (STOC 2024) and Li (STOC 2024), the $2^n/n$ circuit lower bound for $\mathrm{S}_2\mathrm{E}$ is being pushed toward lower classes; a $\mathrm{P^{NP}}$-level analogue would be a genuine advance on Kannan's theorem. *(frontier — verify)*
- **Hardness vs. randomness at level 2.** Whether $\mathrm{BPP}\subseteq\Sigma^p_2$ can be improved to $\mathrm{BPP}=\mathrm{P}$ under weaker assumptions bears directly on the $\mathrm{S}^p_2$ vs $\mathrm{ZPP^{NP}}$ refinement of Karp–Lipton.
- **Proof complexity.** Lower bounds for constant-depth Frege with counting axioms are read as the propositional shadow of $\mathrm{PH}$ separations (Pitassi, Krajíček, Beame).
- **Quantum-adjacent.** Post-Raz–Tal work on forrelation and $\mathrm{QMA}$ vs $\mathrm{PH}$ oracle separations continues (Aaronson's group, UT Austin). *(frontier — verify)*

## 8. Future Work

- Find a lower-bound technique that is simultaneously **non-relativizing and non-naturalizing**; meta-complexity currently offers the only credible candidate.
- Prove $\mathrm{NEXP}\not\subseteq \mathrm{P/poly}$, which by Impagliazzo–Kabanets–Wigderson (2002) and the Karp–Lipton family would sharply constrain collapse scenarios.
- Extend the average-case depth hierarchy theorem of Rossman–Servedio–Tan to $\mathrm{AC}^0[\oplus]$, the first model where natural proofs bite.
- Settle whether $\mathrm{S}^p_2 = \Sigma^p_2\cap\Pi^p_2$, cleaning up the exact collapse level in Karp–Lipton.
- Determine whether $\mathrm{PH}$ has a complete *promise* problem — a structural question equivalent in spirit to collapse.

## 9. Key References

- **[Foundational]** Stockmeyer, L. *The polynomial-time hierarchy.* Theoretical Computer Science 3(1):1–22, 1976.
- **[Foundational]** Wrathall, C. *Complete sets and the polynomial-time hierarchy.* Theoretical Computer Science 3(1):23–33, 1976.
- **[Foundational]** Meyer, A. R., Stockmeyer, L. *The equivalence problem for regular expressions with squaring requires exponential space.* 13th IEEE SWAT (FOCS), 125–129, 1972.
- **[Foundational]** Baker, T., Gill, J., Solovay, R. *Relativizations of the P =? NP question.* SIAM J. Computing 4(4):431–442, 1975.
- **[Foundational]** Karp, R. M., Lipton, R. J. *Some connections between nonuniform and uniform complexity classes.* STOC 1980, 302–309.
- **[Foundational]** Håstad, J. *Almost optimal lower bounds for small depth circuits.* STOC 1986, 6–20.
- **[Foundational]** Yao, A. C.-C. *Separating the polynomial-time hierarchy by oracles.* FOCS 1985, 1–10.
- **[Foundational]** Toda, S. *PP is as hard as the polynomial-time hierarchy.* SIAM J. Computing 20(5):865–877, 1991.
- **[SOTA / Recent]** Rossman, B., Servedio, R., Tan, L.-Y. *An average-case depth hierarchy theorem for Boolean circuits.* FOCS 2015, 1030–1048.
- **[SOTA / Recent]** Chen, L., Hirahara, S., Ren, H. *Symmetric exponential time requires near-maximum circuit complexity.* STOC 2024.
- **[SOTA / Recent]** Li, Z. *Symmetric exponential time requires near-maximum circuit complexity: simplified, truly uniform.* STOC 2024.
- **[SOTA / Recent]** Raz, R., Tal, A. *Oracle separation of BQP and PH.* STOC 2019, 13–23.
- **[SOTA / Recent]** Cai, J.-Y. *$S_2^p \subseteq ZPP^{NP}$.* Journal of Computer and System Sciences 73(1):25–35, 2007.
- **[Related]** Ko, K.-I. *Relativized polynomial time hierarchies having exactly $k$ levels.* SIAM J. Computing 18(2):392–408, 1989.
- **[Related]** Yap, C. K. *Some consequences of non-uniform conditions on uniform classes.* Theoretical Computer Science 26(3):287–300, 1983.
- **[Related]** Boppana, R., Håstad, J., Zachos, S. *Does co-NP have short interactive proofs?* Information Processing Letters 25(2):127–132, 1987.
- **[Related]** Kannan, R. *Circuit-size lower bounds and non-reducibility to sparse sets.* Information and Control 55(1–3):40–56, 1982.
- **[Barrier]** Razborov, A., Rudich, S. *Natural proofs.* Journal of Computer and System Sciences 55(1):24–35, 1997.
- **[Barrier]** Aaronson, S., Wigderson, A. *Algebrization: a new barrier in complexity theory.* ACM Transactions on Computation Theory 1(1), 2009.
- **[Survey]** Arora, S., Barak, B. *Computational Complexity: A Modern Approach.* Cambridge University Press, 2009 (Chapter 5).
- **[Survey]** Fortnow, L. *The status of the P versus NP problem.* Communications of the ACM 52(9):78–86, 2009.

## 10. Worked Example / Concrete Special Case

**Claim (upward collapse at level 2).** If $\Sigma^p_2=\Pi^p_2$ then $\Sigma^p_3=\Sigma^p_2$, and hence $\mathrm{PH}=\Sigma^p_2$.

*Proof.* Let $L\in\Sigma^p_3$. By definition there is a polynomial $q$ and a poly-time relation $R$ with

$$x\in L \iff \exists y_1\,\forall y_2\,\exists y_3 \; R(x,y_1,y_2,y_3),\qquad |y_i|\le q(|x|).$$

Define $B=\{\langle x,y_1\rangle : \forall y_2\,\exists y_3\, R(x,y_1,y_2,y_3)\}$. The inner two quantifiers start with $\forall$, so $B\in\Pi^p_2$. By hypothesis $\Pi^p_2=\Sigma^p_2$, so there are a polynomial $r$ and a poly-time relation $S$ with

$$\langle x,y_1\rangle\in B \iff \exists z_1\,\forall z_2\; S(x,y_1,z_1,z_2),\qquad |z_i|\le r(|x|+|y_1|).$$

Substituting,

$$x\in L \iff \exists y_1\,\exists z_1\,\forall z_2\; S(x,y_1,z_1,z_2) \iff \exists \langle y_1,z_1\rangle\,\forall z_2\; S'(x,\langle y_1,z_1\rangle,z_2),$$

where $S'$ just unpacks the pair. Adjacent like quantifiers merge into one of polynomially bounded length ($|\langle y_1,z_1\rangle| \le q(|x|)+r(|x|+q(|x|))+O(\log)$, still polynomial), and $S'$ is poly-time. Hence $L\in\Sigma^p_2$, giving $\Sigma^p_3\subseteq\Sigma^p_2$. Induction on $k$ extends this to $\Sigma^p_k = \Sigma^p_2$ for all $k \ge 2$. $\square$

**Concrete instantiation.** $\Sigma_2\mathrm{SAT}$ — is $\exists \bar y \forall \bar z\, \varphi(\bar y,\bar z)$ true? — is $\Sigma^p_2$-complete; the natural problem *Minimum Equivalent DNF* (given a DNF $\phi$ and integer $s$, is there an equivalent DNF with at most $s$ terms?) is also $\Sigma^p_2$-complete (Umans, JCSS 2001). Take $\varphi(y_1,y_2,z)=(y_1\vee z)\wedge(y_2\vee\neg z)$: the assignment $y_1=y_2=1$ satisfies it for both $z=0$ and $z=1$, so the instance is a yes-instance, checkable by $2^2\cdot 2 = 8$ evaluations. The collapse question asks whether the extra $\forall z$ block ever buys real power over $\mathrm{NP}$ — and the theorem above says that if it does not at level 2, it never does at any level.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*