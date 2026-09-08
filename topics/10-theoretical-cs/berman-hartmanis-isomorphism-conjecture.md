---
id: 10-theoretical-cs/berman-hartmanis-isomorphism-conjecture
title: "Sparse Set Completeness and Berman-Hartmanis Isomorphism Conjecture"
topic: 10-theoretical-cs
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Sparse Set Completeness and the Berman–Hartmanis Isomorphism Conjecture

> **Topic:** Theoretical Computer Science · **ID:** `10-theoretical-cs/berman-hartmanis-isomorphism-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

**Isomorphism Conjecture (Berman–Hartmanis, 1977).** All sets complete for $\mathrm{NP}$ under polynomial-time many-one ($\le_m^p$) reductions are polynomial-time isomorphic: for any two $\mathrm{NP}$-complete $A, B \subseteq \{0,1\}^*$ there is a bijection $f:\{0,1\}^*\to\{0,1\}^*$ such that $f$ and $f^{-1}$ are computable in polynomial time and $x \in A \iff f(x) \in B$.

Two immediate consequences frame the problem:

1. The conjecture implies $\mathrm{P} \neq \mathrm{NP}$. If $\mathrm{P}=\mathrm{NP}$ then every non-trivial set in $\mathrm{P}$ (e.g. $\{0\}$ and $\{0\}^*$) is $\mathrm{NP}$-complete, and finite/co-finite-density sets cannot be p-isomorphic to $\mathrm{SAT}$ because p-isomorphisms are length-bounded by a polynomial in both directions and hence preserve density up to a polynomial.
2. The conjecture implies the **sparse-set conjecture**: no sparse set is $\mathrm{NP}$-complete under $\le_m^p$, since $\mathrm{SAT}$ has density $2^{\Omega(n)}$.

The companion question is the converse-flavoured programme: *how weak a reduction to a sparse set still forces $\mathrm{P}=\mathrm{NP}$?* A complete resolution means either exhibiting two $\mathrm{NP}$-complete sets provably not p-isomorphic (under no unproven hypothesis), or proving p-isomorphism of the whole $\le_m^p$-complete degree of $\mathrm{NP}$ — which would in particular settle $\mathrm{P}\neq\mathrm{NP}$.

## 2. Mathematical Foundations

**Reductions.** $A \le_m^p B$ iff there is $f \in \mathrm{FP}$ with $x\in A \iff f(x)\in B$. $A \le_{btt}^p B$ ($k$-truth-table) iff a polynomial-time machine produces $k$ queries $q_1,\dots,q_k$ and a Boolean predicate $\alpha$ with $x \in A \iff \alpha(\chi_B(q_1),\dots,\chi_B(q_k))$. $A \le_T^p B$ is Cook reducibility.

**Density.** For $S\subseteq\{0,1\}^*$ write $S^{\le n} = \{x\in S : |x| \le n\}$. $S$ is **sparse** iff $\exists$ polynomial $p$ with $|S^{\le n}| \le p(n)$; $S$ is a **tally** set iff $S \subseteq 0^*$.

**Paddability.** $A$ is **paddable** iff there is $p_A \in \mathrm{FP}$, injective, with polynomial-time invertible range, such that
$$\forall x,y:\quad p_A(x,y)\in A \iff x \in A .$$
$\mathrm{SAT}$, $\mathrm{CLIQUE}$, $\mathrm{3\text{-}COL}$, $\mathrm{SUBSET\text{-}SUM}$, $\mathrm{VC}$, and every problem in Garey–Johnson are paddable.

**Berman–Hartmanis criterion (effective Cantor–Schröder–Bernstein).** If $A \le_m^p B$ and $B \le_m^p A$ via reductions that are (i) injective, (ii) length-increasing, and (iii) polynomial-time invertible, then $A \cong_p B$. The isomorphism is built by the back-and-forth chain construction: for $f: A\to B$, $g: B\to A$ with those properties,
$$
h(x) = \begin{cases} f(x) & \text{if the } g\text{-chain from } x \text{ terminates in } \mathrm{range}(g)^c \text{ after an even number of steps},\\ g^{-1}(x) & \text{otherwise},\end{cases}
$$
where chains are traced by alternately inverting $g$ and $f$; length-increase bounds the chain length by $|x|$, and invertibility makes each step polynomial.

**Corollary.** All paddable $\mathrm{NP}$-complete sets are p-isomorphic. Hence the conjecture is equivalent to: *every $\mathrm{NP}$-complete set is paddable* (equivalently, is $\le_m^p$-complete via length-increasing invertible reductions).

**Mahaney's theorem (1982).** There is a sparse $\mathrm{NP}$-complete set under $\le_m^p$ iff $\mathrm{P}=\mathrm{NP}$.

**Karp–Lipton (1980).** If $\mathrm{NP}$ has a sparse $\le_T^p$-hard set (equivalently $\mathrm{NP}\subseteq\mathrm{P/poly}$) then $\mathrm{PH}=\Sigma_2^p$; strengthened to $\mathrm{PH}=\mathrm{ZPP}^{\mathrm{NP}}$ (Köbler–Watanabe 1998) and to $\mathrm{PH}=\mathrm{S}_2^p$ (Cai 2007).

## 3. History & State of the Art (SOTA)

- **1977.** Leonard Berman and Juris Hartmanis, *On isomorphisms and density of NP and other complete sets* (SIAM J. Comput. 6(2)), observe that all then-known $\mathrm{NP}$-complete sets are p-isomorphic via padding, conjecture this for all of them, and conjecture that no sparse set is $\mathrm{NP}$-complete. They prove the isomorphism criterion above (a polynomial-time analogue of Myhill's 1955 theorem that all $\Sigma_1$-complete sets are recursively isomorphic).
- **1979.** Steve Fortune: a sparse $\le_m^p$-complete set for $\mathrm{coNP}$ implies $\mathrm{P}=\mathrm{NP}$.
- **1982.** Stephen Mahaney resolves the sparse many-one case for $\mathrm{NP}$ by a census/left-set pruning argument.
- **1988–1991.** Ogihara (Ogiwara) and Watanabe extend to bounded truth-table: a sparse $\le_{btt}^p$-hard set for $\mathrm{NP}$ implies $\mathrm{P}=\mathrm{NP}$.
- **1989–1995.** Kurtz, Mahaney and Royer show the conjecture **fails relative to a generic oracle** and construct oracles collapsing/separating degrees; Fenner, Fortnow and Kurtz (1996) show it **holds relative to an oracle**. Relativization is therefore useless.
- **1998.** Agrawal, Allender and Rudich prove an unconditional isomorphism theorem at low complexity: all sets complete for $\mathrm{NP}$ under $\mathrm{AC}^0$ (indeed first-order) reductions are isomorphic under $\mathrm{P}$-uniform $\mathrm{AC}^0$-computable isomorphisms.
- **1999.** Cai and Sivakumar settle Hartmanis's analogous conjecture for $\mathrm{P}$: a sparse $\le_m^{\log}$-hard set for $\mathrm{P}$ implies $\mathrm{P}=\mathrm{L}$ (using Reed–Solomon list decoding / the isolation lemma).
- **2008.** Buhrman and Hitchcock: $\mathrm{NP}$-hard sets under $\le_T^p$ have density at least $2^{n^\varepsilon}$ unless $\mathrm{coNP} \subseteq \mathrm{NP}/\mathrm{poly}$.
- **2009.** Agrawal and Watanabe: regular one-way functions imply all $\mathrm{NP}$-complete sets are complete under *length-increasing* reductions computed by non-uniform linear-size circuits — evidence *for* the conjecture from a hypothesis once thought to refute it.

SOTA: the conjecture is open, provably non-relativizing, unconditionally **true at the $\mathrm{AC}^0$ level**, and both supported and contradicted by natural but incompatible hypotheses.

## 4. Partial Results / Verified Cases

- **All natural $\mathrm{NP}$-complete problems.** Every one of the ~300 problems in Garey–Johnson is paddable, hence all are p-isomorphic to $\mathrm{SAT}$ — a "verified case" over the entire catalog of known complete problems.
- **$\mathrm{AC}^0$/first-order degree.** Sets complete for $\mathrm{NP}$ under $\mathrm{AC}^0$ many-one reductions are all $\mathrm{AC}^0$-isomorphic (Agrawal–Allender–Rudich 1998; Agrawal–Allender–Impagliazzo–Pitassi–Rudich 2001 for $\mathrm{NC}^0$/first-order variants). The same holds for the complete degrees of $\mathrm{P}$, $\mathrm{PSPACE}$, $\mathrm{NEXP}$, $\mathrm{DET}$ and every level of $\mathrm{NC}$ under these reductions.
- **Sparse sets, many-one:** fully solved. $\mathrm{P}=\mathrm{NP}$ iff a sparse $\mathrm{NP}$-complete set exists (Mahaney). Tally case is earlier and easier (Berman 1978).
- **Sparse sets, $k$-tt for constant $k$:** solved (Ogihara–Watanabe 1991); extended to $\le_{btt}^{\mathrm{SN}}$ and to $\mathrm{NP}$-hard sets of density $2^{n^{o(1)}}$ under nondeterministic reductions (Arvind et al. 1995; Cai–Naik–Sivakumar).
- **Sparse hard sets for $\mathrm{P}$ and $\mathrm{NL}$ under logspace/$\mathrm{NC}^1$ reductions:** solved (Cai–Sivakumar 1999; Cai–Ogihara).
- **Conditional isomorphism:** under the hypothesis that $\mathrm{NP}$ contains sets requiring exponential-size circuits ("$\mathrm{NP}$ is hard on average / pseudorandom generator" hypotheses), Agrawal (2002) shows all $\mathrm{NP}$-complete sets are complete under *$\mathrm{P}$-computable, length-increasing, invertible* reductions in restricted models, giving isomorphism within those models.

## 5. Principal Obstacles

- **It implies $\mathrm{P}\neq\mathrm{NP}$.** Any proof is at least as hard as the central open problem of the field; hence relativization (Baker–Gill–Solovay), natural proofs (Razborov–Rudich) and algebrization barriers all apply.
- **Oracles point both ways.** Kurtz–Mahaney–Royer (generic oracle: conjecture false, and $\mathrm{P}\neq\mathrm{NP}$) versus Fenner–Fortnow–Kurtz (oracle: conjecture true). No relativizing argument can decide it. Rogers (1997) even gives an oracle where the conjecture *and* one-way functions both hold, killing the simplest intuition that one-way functions refute it.
- **Padding is the whole difficulty.** Given paddability, the Cantor–Schröder–Bernstein construction is routine. Proving every complete set is paddable requires reasoning about *arbitrary* reductions, and no technique constructs an invertible length-increasing reduction from a generic many-one reduction $f$ — $f$ may be many-to-one and length-decreasing, and inverting it is an $\mathrm{NP}$ search problem.
- **Counter-evidence from cryptography.** Joseph–Young (1985) construct $k$-creative sets $K_f$ from strong one-way functions $f$; if $f$ is not p-invertible, $K_f$ appears to be $\mathrm{NP}$-complete yet not paddable, suggesting the conjecture is false. But "appears" is not a theorem: nobody can prove $K_f \not\cong_p \mathrm{SAT}$.
- **Measure-theoretic counter-evidence.** Under the measure hypothesis ($\mathrm{NP}$ does not have p-measure zero), Lutz–Mayordomo (1996) separate $\le_{3\text{-}tt}^p$-completeness from $\le_m^p$-completeness for $\mathrm{NP}$, and the same hypothesis yields $\mathrm{NP}$-complete sets that are not p-isomorphic. So plausible hypotheses contradict each other on this question.
- **Sparse Turing case is stuck at $\mathrm{P/poly}$.** A sparse $\le_T^p$-hard set for $\mathrm{NP}$ is *exactly* $\mathrm{NP}\subseteq\mathrm{P/poly}$; ruling it out is the circuit lower bound problem. Karp–Lipton-style collapses are the best available and only collapse $\mathrm{PH}$, not $\mathrm{NP}$ to $\mathrm{P}$.

## 6. The Gap

Proven: (a) paddable complete sets are all p-isomorphic; (b) $\mathrm{AC}^0$-complete degrees are unconditionally isomorphic; (c) the sparse-set conjecture holds for $\le_m^p$ and $\le_{btt}^p$.

Unproven: that **every** $\le_m^p$-complete set for $\mathrm{NP}$ is complete under *length-increasing, injective, polynomial-time invertible* reductions. The missing step is a uniform procedure that, given an arbitrary $f$ witnessing $\mathrm{SAT} \le_m^p A$, manufactures an invertible length-increasing $f'$ witnessing the same. Agrawal–Watanabe do this *non-uniformly* assuming regular one-way functions; removing non-uniformity, or removing the hypothesis, is the exact frontier. The secondary gap is between $\le_{btt}^p$ and $\le_T^p$ for sparse hard sets: closing it collapses to proving $\mathrm{NP}\not\subseteq\mathrm{P/poly}$.

## 7. Current Research (as of June 2026)

- **Length-increasing completeness.** Continuing work of Hitchcock, Pavan, Buhrman, Agrawal and Watanabe on hypotheses (measure, genericity, one-way functions) forcing $\mathrm{NP}$-completeness under length-increasing reductions; established for $\mathrm{PSPACE}$ and $\mathrm{NEXP}$-complete degrees under weaker assumptions than for $\mathrm{NP}$.
- **The $\mathrm{AC}^0$-isomorphism programme (Agrawal's conjecture):** *all $\mathrm{NP}$-complete sets under $\le_m^p$ are $\mathrm{AC}^0$-isomorphic after a suitable padding*. Groups at IIT Kanpur, Rutgers (Allender) and Tokyo Tech pursue this; it would imply the classical conjecture. *(frontier — verify)*
- **Nonuniform and randomized completeness notions** (Hitchcock–Shafei): whether $\mathrm{NP}$-complete sets under $\mathrm{P/poly}$ many-one reductions are complete under uniform ones. *(frontier — verify)*
- **Sparse hardness for other classes:** sparse hard sets for $\mathrm{NL}$, $\mathrm{\oplus P}$, and for the Minimum Circuit Size Problem's reduction degree; MCSP is the most-studied candidate for a "non-paddable-looking" natural complete-ish set. *(frontier — verify)*
- **Derandomization links:** Buhrman–Hitchcock-style density lower bounds refined under $\mathrm{NP}\not\subseteq\mathrm{coNP}/\mathrm{poly}$.

## 8. Future Work

- Prove or refute: every $\mathrm{NP}$-complete set is complete under length-increasing reductions, *unconditionally* — the cleanest sub-goal, and it does not obviously imply $\mathrm{P}\neq\mathrm{NP}$.
- Derandomize the Agrawal–Watanabe non-uniform construction under a standard hardness assumption.
- Settle the Joseph–Young programme: prove that some $k$-creative set built from a candidate one-way function is $\mathrm{NP}$-complete and *not* paddable, or prove all $k$-creative sets are paddable.
- Extend Cai–Sivakumar's coding-theoretic machinery upward from $\mathrm{P}$/$\mathrm{NL}$ to unbounded truth-table reductions for $\mathrm{NP}$.
- Identify a non-relativizing, non-naturalizing technique; the $\mathrm{AC}^0$ isomorphism theorem is the one existing example and its algebraic core (switching lemma + Sipser functions) may extend.

## 9. Key References

- **[Foundational]** L. Berman, J. Hartmanis. *On Isomorphisms and Density of NP and Other Complete Sets.* SIAM Journal on Computing 6(2):305–322, 1977.
- **[Foundational]** S. R. Mahaney. *Sparse Complete Sets for NP: Solution of a Conjecture of Berman and Hartmanis.* Journal of Computer and System Sciences 25(2):130–143, 1982.
- **[Foundational]** R. M. Karp, R. J. Lipton. *Turing Machines That Take Advice.* L'Enseignement Mathématique 28:191–209, 1982 (STOC 1980).
- **[Foundational]** M. Ogiwara, O. Watanabe. *On Polynomial-Time Bounded Truth-Table Reducibility of NP Sets to Sparse Sets.* SIAM Journal on Computing 20(3):471–483, 1991.
- **[SOTA]** M. Agrawal, E. Allender, S. Rudich. *Reductions in Circuit Complexity: An Isomorphism Theorem and a Gap Theorem.* Journal of Computer and System Sciences 57(2):127–143, 1998.
- **[SOTA]** M. Agrawal, E. Allender, R. Impagliazzo, T. Pitassi, S. Rudich. *Reducing the Complexity of Reductions.* Computational Complexity 10(2):117–138, 2001.
- **[SOTA]** J.-Y. Cai, D. Sivakumar. *Sparse Hard Sets for P: Resolution of a Conjecture of Hartmanis.* Journal of Computer and System Sciences 58(2):280–296, 1999.
- **[SOTA]** M. Agrawal, O. Watanabe. *One-Way Functions and the Berman–Hartmanis Conjecture.* IEEE Conference on Computational Complexity (CCC), 2009.
- **[SOTA]** H. Buhrman, J. M. Hitchcock. *NP-Hard Sets Are Exponentially Dense Unless coNP ⊆ NP/poly.* IEEE Conference on Computational Complexity (CCC), 2008.
- **[Structural]** S. Kurtz, S. Mahaney, J. Royer. *The Isomorphism Conjecture Fails Relative to a Random Oracle.* Journal of the ACM 42(2):401–420, 1995.
- **[Structural]** S. Fenner, L. Fortnow, S. Kurtz. *The Isomorphism Conjecture Holds Relative to an Oracle.* SIAM Journal on Computing 25(1):193–206, 1996.
- **[Structural]** D. Joseph, P. Young. *Some Remarks on Witness Functions for Nonpolynomial and Noncomplete Sets in NP.* Theoretical Computer Science 39:225–237, 1985.
- **[Structural]** J. H. Lutz, E. Mayordomo. *Cook Versus Karp–Levin: Separating Completeness Notions if NP Is Not Small.* Theoretical Computer Science 164(1–2):141–163, 1996.
- **[Survey]** S. Kurtz, S. Mahaney, J. Royer. *The Structure of Complete Degrees.* In: Complexity Theory Retrospective (A. Selman, ed.), Springer, 1990.
- **[Survey]** M. Agrawal. *The Isomorphism Conjecture for NP.* In: Computability in Context, Imperial College Press, 2011.
- **[Textbook]** S. Homer, A. L. Selman. *Computability and Complexity Theory*, 2nd ed., Springer, 2011 (Ch. on sparse sets and isomorphism).

## 10. Worked Example / Concrete Special Case

**Goal: exhibit a p-isomorphism $\mathrm{SAT} \cong_p \mathrm{CLIQUE}$ in the Berman–Hartmanis style.**

*Step 1: padding for $\mathrm{SAT}$.* Let $\varphi$ be a CNF formula over variables $x_1,\dots,x_n$ and $y = y_1\cdots y_k \in\{0,1\}^k$. Define
$$
p_{\mathrm{SAT}}(\varphi,y) \;=\; \varphi \;\wedge\; \bigwedge_{i=1}^{k}\bigl(z_i \vee \bar z_i\bigr)^{(y_i)},
$$
where the $i$-th conjunct is the tautological clause $(z_i \vee \bar z_i)$ if $y_i=1$ and $(z_i \vee \bar z_i \vee w)\wedge(z_i\vee\bar z_i\vee \bar w)$ if $y_i=0$, with $z_i,w$ fresh variables. Every added conjunct is a tautology, so satisfiability is unchanged: $p_{\mathrm{SAT}}(\varphi,y)\in \mathrm{SAT} \iff \varphi \in \mathrm{SAT}$. The encoding is injective, computable in time $O(|\varphi| + k)$, length-increasing, and decodable: scan the suffix of tautological conjuncts, read off $y_i \in \{1,0\}$ by clause width, and strip them to recover $\varphi$.

*Step 2: reductions.* Cook–Levin/Karp give $f:\mathrm{SAT}\le_m^p\mathrm{CLIQUE}$ (formula $\to$ graph with a vertex per literal-occurrence, target $k=$ number of clauses) and $g:\mathrm{CLIQUE}\le_m^p\mathrm{SAT}$ (Cook's tableau encoding). Neither is invertible as stated.

*Step 3: make them invertible via padding.* Define
$$
f'(\varphi) = p_{\mathrm{CLIQUE}}\bigl(f(\varphi),\,\varphi\bigr),\qquad g'(\langle G,k\rangle) = p_{\mathrm{SAT}}\bigl(g(\langle G,k\rangle),\,\langle G,k\rangle\bigr).
$$
$f'$ carries its own input in the pad, so $f'$ is injective and $f'^{-1}$ is polynomial (decode the pad, output $\varphi$); it preserves membership because padding does; and it is length-increasing because $|f'(\varphi)| \ge |\varphi| + 1$. Same for $g'$. Here $p_{\mathrm{CLIQUE}}(\langle G,k\rangle, y)$ adds $|y|$ isolated vertices plus a self-delimiting gadget encoding $y$ as a path of length $2$ or $3$ per bit, leaving the maximum clique size fixed.

*Step 4: Cantor–Schröder–Bernstein.* For $x \in \{0,1\}^*$ trace the chain $x, g'^{-1}(x), f'^{-1}(g'^{-1}(x)), \dots$ Each inversion strictly decreases length, so at most $|x|$ steps occur before some step is undefined. Set $h(x)=f'(x)$ if the chain has even length, $h(x)=g'^{-1}(x)$ if odd. Then $h$ is a polynomial-time bijection, $h^{-1}$ is polynomial-time by the symmetric construction, and $\varphi\in\mathrm{SAT}\iff h(\varphi)\in\mathrm{CLIQUE}$.

*What breaks in general.* Step 3 used only that $\mathrm{SAT}$ and $\mathrm{CLIQUE}$ are paddable. For a hypothetical $\mathrm{NP}$-complete set $A$ built as a Joseph–Young $k$-creative set from a one-way function, no $p_A$ is known; the reduction $f:\mathrm{SAT}\le_m^p A$ exists but its range is sparse-looking inside $A$, and computing $f^{-1}$ is exactly inverting the one-way function. That single missing padding function is the entire open problem.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*