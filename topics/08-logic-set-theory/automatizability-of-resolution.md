---
id: 08-logic-set-theory/automatizability-of-resolution
title: "Automatizability of Resolution Proof Search"
topic: 08-logic-set-theory
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Automatizability of Resolution Proof Search

> **Topic:** Mathematical Logic & Set Theory · **ID:** `08-logic-set-theory/automatizability-of-resolution` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Resolution is the propositional proof system underlying essentially every CNF-SAT solver. **Automatizability** asks whether short refutations can be *found* as efficiently as they can be *verified*.

A proof system $P$ is **automatizable in time $t$** if there is a deterministic algorithm that, given an unsatisfiable CNF $F$, outputs a $P$-refutation of $F$ in time $t\bigl(|F| + S_P(F)\bigr)$, where $S_P(F)$ is the size of the shortest $P$-refutation of $F$.

- **Settled (negative):** Resolution is *not* automatizable in polynomial time unless $\mathrm{P} = \mathrm{NP}$ (Atserias–Müller, 2019/2020).
- **Open (the live question):** Is Resolution automatizable in **quasipolynomial** time $N^{O(\log N)}$? Equivalently, is there an algorithm producing a refutation of size $\mathrm{poly}(S)$ — or any $2^{\mathrm{polylog}}$ overhead — for every $F$ with a size-$S$ refutation?
- **Open (weak form):** Is Resolution **weakly automatizable**, i.e. is there a polynomial-time algorithm that on input $(F, 1^s)$, with $F$ having a Resolution refutation of size $\le s$, outputs *some* certificate of unsatisfiability (possibly in a stronger system)?

A resolution requires either an algorithm with the stated running time and a correctness proof, or a hardness reduction from a standard-assumption problem ruling it out.

## 2. Mathematical Foundations

Let $F = C_1 \wedge \cdots \wedge C_m$ be a CNF over variables $x_1,\dots,x_n$, each $C_i$ a clause (disjunction of literals). The **resolution rule** is
$$\frac{A \vee x \qquad B \vee \neg x}{A \vee B}.$$
A **refutation** is a sequence of clauses ending in $\bot$, each an axiom of $F$ or a resolvent of two earlier clauses. Define
$$S(F) = \text{minimum number of clauses in a refutation}, \qquad w(F) = \min_{\pi} \max_{C \in \pi} |C|,$$
the minimum **size** and minimum **width**. Write $w(F \vdash \bot)$ for width and $w(F)$ for the initial clause width. Tree-like resolution ($S_T$) requires each derived clause be used once.

**Theorem (Ben-Sasson–Wigderson, 2001).** For CNF $F$ on $n$ variables,
$$w(F \vdash \bot) \;\le\; w(F) + O\!\left(\sqrt{n \ln S(F)}\right), \qquad w(F \vdash \bot) \le w(F) + \log_2 S_T(F).$$

Since all clauses of width $\le w$ can be enumerated by a fixpoint (dynamic-programming) procedure in time $n^{O(w)}$, this gives the standard search algorithms
$$\text{general: } n^{O\left(\sqrt{n\log S}\right)}, \qquad \text{tree-like: } n^{O(\log S)} = N^{O(\log N)}.$$

**Feasible interpolation.** If $A(\bar p,\bar q) \wedge B(\bar p,\bar r)$ has a resolution refutation of size $S$, there is a Boolean circuit of size $\mathrm{poly}(S)$ that on input $\bar p$ outputs $0$ if $A(\bar p,\cdot)$ is unsatisfiable and $1$ if $B(\bar p,\cdot)$ is (Krajíček 1997; Pudlák 1997). This is the main structural tool linking automatizability to complexity assumptions.

**Canonical pair.** The disjoint NP-pair of Resolution is
$$(\mathrm{SAT}^*, \mathrm{REF}) = \bigl\{(F,1^s) : F \text{ satisfiable}\bigr\},\ \bigl\{(F,1^s) : S(F) \le s\bigr\}.$$
Resolution is weakly automatizable iff this pair is separable in polynomial time (Pudlák 2003).

## 3. History & State of the Art (SOTA)

- **1996.** Bonet, Pitassi and Raz introduce "automatizability" as the formalization of proof search; Beame–Pitassi give the $n^{O(\log S)}$ tree-like algorithm.
- **1997–1998.** Krajíček's interpolation theorem for Resolution; Krajíček–Pudlák show Extended Frege is not automatizable if RSA is secure. Bonet–Pitassi–Raz (SICOMP 2000) extend to bounded-depth Frege under Diffie–Hellman.
- **2001.** Ben-Sasson–Wigderson's size–width relation yields the $n^{O(\sqrt{n\log S})}$ upper bound — still the best known for general Resolution.
- **2004–2008.** Alekhnovich–Razborov prove Resolution and tree-like Resolution are not automatizable unless $\mathrm{FPT} = \mathrm{W}[\mathrm{P}]$ (SICOMP 2008); the randomized-reduction caveat is removed by Eickmeyer–Grohe–Grüber (2008).
- **2004.** Atserias–Bonet connect (weak) automatizability of Resolution to feasible interpolation and to the clique–coloring pairs.
- **2019/2020.** **Atserias–Müller**: automating Resolution is NP-hard — the central breakthrough. Their reduction maps a CNF $F$ to a formula $\mathrm{Ref}(F,s)$ ("$F$ has a refutation with $s$ lines"), which has polynomial-size refutations when $F$ is unsatisfiable and requires refutations of size $2^{N^{\Omega(1)}}$ when $F$ is satisfiable.
- **2020–2021.** The technique propagates: Cutting Planes (Göös–Koroth–Mertz–Pitassi), Nullstellensatz/Polynomial Calculus/Sherali–Adams (de Rezende–Göös–Nordström–Pitassi–Robere–Sokolov), $\mathrm{Res}(k)$ (Garlík). de Rezende shows tree-like Resolution is not automatizable in time $n^{o(\log n)}$ under ETH, matching Beame–Pitassi exactly.

## 4. Partial Results / Verified Cases

| Regime | Result |
|---|---|
| Tree-like Resolution | Automatizable in $N^{O(\log N)}$; optimal — no $n^{o(\log n)}$ algorithm under ETH (de Rezende 2021) |
| Width-$w$ refutations | Found in $n^{O(w)}$; polynomial for constant $w$ |
| General Resolution, size $S$ | Found in $n^{O(\sqrt{n\log S})}$; beats brute force $2^{O(n)}$ whenever $\log S = o(n/\log^2 n)$ |
| Regular Resolution | Not automatizable in polynomial time unless $\mathrm{P}=\mathrm{NP}$ (Atserias–Müller); tree-like case NP-hard already by Alekhnovich–Razborov |
| Horn / 2-CNF / renamable-Horn | Unsatisfiability decidable in linear time; refutations of size $O(|F|)$ constructible directly |
| Bounded treewidth / bounded clique-width incidence graphs | Resolution refutation of size $2^{O(\mathrm{tw})}\mathrm{poly}(n)$ constructible in FPT time |
| Tseitin formulas over bounded-degree graphs | Width, hence proof search, controlled by a cops-and-robber game; refutations found in $n^{O(\text{tw}(G))}$ (Galesi–Talebanfard–Torán) |
| Frege, Extended Frege | Not automatizable under cryptographic assumptions (Krajíček–Pudlák 1998; Bonet–Pitassi–Raz 2000) |

## 5. Principal Obstacles

- **The width method saturates.** Ben-Sasson–Wigderson's $\sqrt{n\log S}$ term is tight: there are formulas with polynomial-size refutations but width $\Omega(\sqrt{n})$ (Bonet–Galesi 2001). So *no* width-based algorithm can do better than $n^{\Theta(\sqrt n)}$ for general Resolution, and the technique gives nothing quasipolynomial.
- **No known structural handle beyond width.** Every known upper-bound method extracts a refutation from a *small-measure* certificate (width, space, degree). Short general resolution refutations need not be narrow, shallow, or regular, and no combinatorial parameter is known that is simultaneously (a) bounded when $S$ is small and (b) searchable.
- **Feasible interpolation is only a barrier, not an algorithm.** Interpolation converts short refutations into small circuits, but *finding* the circuit is exactly the hard step; monotone-interpolation lower bounds constrain what proof search could look like without suggesting one.
- **The hardness reductions themselves have quasipolynomial slack.** The $\mathrm{Ref}(F,s)$ construction blows up the instance size, so it rules out $\mathrm{poly}$ but does not straightforwardly close the quasipolynomial window from the tree-like algorithm.
- **Weak automatizability resists both directions.** It is not known to follow from any standard algorithmic assumption, and refuting it would separate the canonical pair — which by Atserias–Maneva would imply mean-payoff games are not in $\mathrm{P}$, contradicting nothing but requiring genuinely new lower-bound technology for disjoint NP-pairs.

## 6. The Gap

The proven statement is: *no polynomial-time automating algorithm exists unless $\mathrm{P}=\mathrm{NP}$*, and *no $n^{o(\log n)}$ tree-like algorithm exists under ETH*. The general statement asks about the interval
$$n^{\omega(1)} \;\;\text{---}\;\; n^{O(\sqrt{n \log S})},$$
whose most natural target is $N^{O(\log N)}$. Two concrete steps would close it:

1. **Upward (algorithm):** a proof-search procedure whose complexity depends on a parameter bounded by $O(\log S)$ rather than $O(\sqrt{n\log S})$ for *general* (non-tree-like) refutations. No candidate parameter is currently known.
2. **Downward (hardness):** an amplified $\mathrm{Ref}(F,s)$ construction with only polylogarithmic blow-up, converting NP-hardness into ETH-hardness of $N^{o(\log N)}$ automation for general Resolution — the analogue of what de Rezende achieved in the tree-like case.

For weak automatizability the gap is total: neither a separation algorithm for $(\mathrm{SAT}^*,\mathrm{REF})$ nor a hardness result under a standard assumption is known.

## 7. Current Research (as of June 2026)

- **Lifting-based hardness.** The Atserias–Müller reduction combined with query-to-communication lifting is the dominant tool; groups at Charles University (Pudlák, Garlík), Lund/Copenhagen (Nordström, de Rezende), UPC Barcelona (Atserias), and Columbia/Simons (Pitassi, Robere, Göös at EPFL) drive it. Current targets: automating Frege systems and $\mathrm{AC}^0[p]$-Frege without cryptographic assumptions.
- **Fine-grained automatizability.** Sharpening ETH-hardness to pin the exact exponent for general Resolution and for $\mathrm{Res}(k)$ *(frontier — verify)*.
- **Weak automatizability and games.** Following Atserias–Maneva and Huang–Pitassi, work relates weak automatizability of Resolution to the complexity of mean-payoff/parity games and to the provability of game-determinacy in bounded arithmetic.
- **Practice-facing.** Empirical study of CDCL as an approximate automating algorithm: CDCL with restarts polynomially simulates general Resolution (Pipatsrisawat–Darwiche 2011), so heuristic automatization is exactly the branching-heuristic question.

## 8. Future Work

- Identify a "second parameter" beyond width — candidates include clause-space, depth-restricted decision DAGs, or communication-complexity measures of the refutation DAG — provably $O(\mathrm{polylog}\,S)$ for general Resolution.
- Build a low-blow-up variant of $\mathrm{Ref}(F,s)$ (Pudlák's programme) to obtain quasipolynomial hardness.
- Settle weak automatizability under a cryptographic assumption, or derive a surprising algorithmic consequence (games in $\mathrm{P}$) from its truth.
- Transfer the results to $\mathrm{Res}(\log)$ and to Cutting Planes with unbounded coefficients, where automatizability status is still incomplete.

## 9. Key References

- **[Foundational]** M. L. Bonet, T. Pitassi, R. Raz. *On Interpolation and Automatization for Frege Systems.* SIAM Journal on Computing 29(6):1939–1967, 2000.
- **[Foundational]** J. Krajíček. *Interpolation Theorems, Lower Bounds for Proof Systems, and Independence Results for Bounded Arithmetic.* Journal of Symbolic Logic 62(2):457–486, 1997.
- **[Foundational]** J. Krajíček, P. Pudlák. *Some Consequences of Cryptographical Conjectures for $S^1_2$ and EF.* Information and Computation 140(1):82–94, 1998.
- **[Foundational]** E. Ben-Sasson, A. Wigderson. *Short Proofs Are Narrow — Resolution Made Simple.* Journal of the ACM 48(2):149–169, 2001.
- **[Foundational]** M. Alekhnovich, A. A. Razborov. *Resolution Is Not Automatizable Unless W[P] Is Tractable.* SIAM Journal on Computing 38(4):1347–1363, 2008.
- **[SOTA]** A. Atserias, M. Müller. *Automating Resolution Is NP-Hard.* Journal of the ACM 67(5), Article 31, 2020 (conference version FOCS 2019).
- **[SOTA]** M. Göös, S. Koroth, I. Mertz, T. Pitassi. *Automating Cutting Planes Is NP-Hard.* STOC 2020, pp. 68–77.
- **[SOTA]** S. F. de Rezende, M. Göös, J. Nordström, T. Pitassi, R. Robere, D. Sokolov. *Automating Algebraic Proof Systems Is NP-Hard.* STOC 2021, pp. 209–222.
- **[SOTA]** S. F. de Rezende. *Automating Tree-Like Resolution in Time $n^{o(\log n)}$ Is ETH-Hard.* Procedia Computer Science 195:152–162, 2021.
- **[Related]** A. Atserias, M. L. Bonet. *On the Automatizability of Resolution and Related Propositional Proof Systems.* Information and Computation 189(2):182–201, 2004.
- **[Related]** P. Pudlák. *On Reducibility and Symmetry of Disjoint NP-Pairs.* Theoretical Computer Science 295(1–3):323–339, 2003.
- **[Related]** A. Atserias, E. Maneva. *Mean-Payoff Games and Propositional Proofs.* Information and Computation 209(4):664–691, 2011.
- **[Survey]** J. Krajíček. *Proof Complexity.* Cambridge University Press, Encyclopedia of Mathematics and its Applications 170, 2019.
- **[Survey]** P. Beame, T. Pitassi. *Propositional Proof Complexity: Past, Present, and Future.* Bulletin of the EATCS 65:66–89, 1998.

## 10. Worked Example / Concrete Special Case

**(a) What the width algorithm buys, numerically.** Take $n = 10^6$ variables, a 3-CNF, and suppose $S(F) = n^3 = 10^{18}$, so $\ln S \approx 41$. Ben-Sasson–Wigderson gives
$$w(F\vdash\bot) \le 3 + O\!\left(\sqrt{n\ln S}\right) = 3 + O\!\left(\sqrt{4.1\times 10^7}\right) \approx 6.4\times 10^3 \ \ (\text{suppressed constant}).$$
The width-$w$ saturation loop costs $n^{O(w)} = 2^{O(w\log n)} \approx 2^{1.3\times 10^{5}}$, versus brute force $2^{10^6}$. It wins — but by an exponential, not a quasipolynomial, margin: the exponent is $n^{1/2+o(1)}$, and this is *unimprovable* by width alone, because Bonet–Galesi exhibit families with $S = \mathrm{poly}(n)$ and $w(F\vdash\bot) = \Omega(\sqrt n)$.

**(b) Why automating is NP-hard, in miniature.** The Atserias–Müller map sends a CNF $F$ to the CNF $\mathrm{Ref}(F,s)$ whose variables encode an $s$-line resolution refutation of $F$ (which clause sits at each line, and which two earlier lines resolve into it), with clauses asserting local correctness and that line $s$ is $\bot$.

- If $F$ is **unsatisfiable**, $\mathrm{Ref}(F,s)$ is unsatisfiable for $s$ below the true refutation size, and — the technical heart — it has a resolution refutation of size $\mathrm{poly}(|F|,s)$, obtained by simulating the natural "inductive" argument that no correct $s$-line refutation exists.
- If $F$ is **satisfiable**, fix a satisfying assignment $\alpha$. Every clause in any purported refutation must be falsified by $\alpha$ at the top and satisfied at $\bot$ — a contradiction — so $\mathrm{Ref}(F,s)$ is again unsatisfiable, but now proving it requires reconstructing $\alpha$, and the formula inherits an exponential $2^{N^{\Omega(1)}}$ resolution lower bound.

Concretely, with $F = (x) \wedge (\neg x)$ (unsatisfiable, $S(F)=3$) and $s = 2$: $\mathrm{Ref}(F,2)$ says "there is a 2-line refutation", refuted by a handful of resolution steps checking that neither $(x)$ nor $(\neg x)$ resolves to $\bot$ in one step. With $F = (x)$ (satisfiable), the same schema at large $s$ becomes exponentially hard. An automating algorithm running in time $\mathrm{poly}(|F| + S)$ would separate the two cases by its own running time, hence decide SAT in polynomial time. Therefore $\mathrm{P} = \mathrm{NP}$.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*