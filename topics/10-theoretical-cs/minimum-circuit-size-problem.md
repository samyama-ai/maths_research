---
id: 10-theoretical-cs/minimum-circuit-size-problem
title: "Minimum Circuit Size Problem"
topic: 10-theoretical-cs
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Minimum Circuit Size Problem

> **Topic:** Theoretical Computer Science · **ID:** `10-theoretical-cs/minimum-circuit-size-problem` · **Status:** open

## 1. Problem Statement / Conjecture

**MCSP** is the decision problem: given the full truth table of a Boolean function and a size bound, does the function have a circuit of at most that size?

$$\mathrm{MCSP} = \{\,(T, s) \;:\; T \in \{0,1\}^{N},\; N = 2^{n},\; s \in \mathbb{N},\; \mathrm{CC}(f_T) \le s \,\}$$

where $f_T : \{0,1\}^n \to \{0,1\}$ is the function whose truth table is $T$, and $\mathrm{CC}(\cdot)$ is minimum circuit size over the basis of all $2$-input gates.

**The open question.** Determine the complexity of MCSP. It lies in $\mathsf{NP}$, and it is not known to be in $\mathsf{P}$ nor $\mathsf{NP}$-complete. Concretely:

1. Is $\mathrm{MCSP} \in \mathsf{P}$? (Equivalently — up to known implications — can circuit minimization be done efficiently?)
2. Is MCSP $\mathsf{NP}$-complete under polynomial-time many–one reductions?
3. If neither, is MCSP $\mathsf{NP}$-intermediate, and can that be proved from a standard hypothesis?

A complete resolution is a proof of $\mathsf{NP}$-hardness under $\le_m^p$, a polynomial-time algorithm, or an unconditional proof that neither holds (which would settle $\mathsf{P}$ vs $\mathsf{NP}$).

## 2. Mathematical Foundations

**Circuits.** A Boolean circuit $C$ over inputs $x_1,\dots,x_n$ is a finite directed acyclic graph whose sources are labelled by variables or constants and whose internal nodes (gates) have fan-in $2$ and are labelled by a function in $B_2 = \{g : \{0,1\}^2 \to \{0,1\}\}$, $|B_2| = 16$. Size $|C|$ is the number of gates. Then

$$\mathrm{CC}(f) = \min\{\,|C| : C \text{ computes } f\,\}.$$

**Counting bounds (Shannon, Lupanov).** For all but a vanishing fraction of $f$ on $n$ variables,

$$\mathrm{CC}(f) = (1 + o(1)) \cdot \frac{2^n}{n} = (1+o(1))\cdot\frac{N}{\log N},$$

with the upper bound holding for *every* $f$ (Lupanov, 1958). So the interesting parameter range is $s \in [1, N/\log N]$.

**Input length.** The instance has length $N + O(\log s)$, i.e. the input is *exponentially long* in the number of variables $n$. This is the source of nearly all difficulty: reductions must produce truth tables, and hardness proofs must control $\mathrm{CC}$ of an object of size $2^n$.

**Membership in NP.** A witness is a circuit $C$ with $|C| \le s \le N$, describable in $O(s\log s) = \tilde O(N)$ bits; verification evaluates $C$ on all $2^n = N$ inputs in time $\mathrm{poly}(N)$. Hence $\mathrm{MCSP} \in \mathsf{NP}$.

**Brute force.** The number of circuits of size $\le s$ on $n$ inputs is at most $\big(16\,(n+s)^2\big)^{s} = 2^{O(s\log(n+s))}$, so MCSP is decidable in time $2^{O(s \log s)}\cdot \mathrm{poly}(N)$ — polynomial in $N$ only when $s = O(\log N / \log\log N)$, and $2^{\Theta(N)}$ in the worst case.

**Kolmogorov-style variants.** $\mathrm{KT}(x) = \min\{|d| + t\}$ over programs $d$ that, given $i$, output $x_i$ in $t$ steps; $\mathrm{MKTP} = \{(x,s) : \mathrm{KT}(x) \le s\}$. $\mathrm{KT}$ and $\mathrm{CC}$ agree up to polynomial factors, so MKTP is the "Kolmogorov twin" of MCSP and most results transfer, but not all — no reduction between MCSP and MKTP is known in either direction.

**Gap and partial variants.**
- $\mathrm{Gap}_{\alpha}\text{-MCSP}$: distinguish $\mathrm{CC}(f)\le s$ from $\mathrm{CC}(f) > \alpha s$.
- $\mathrm{Partial}\text{-MCSP}$: input $T \in \{0,1,\ast\}^N$; is there a size-$s$ circuit consistent with $T$ on non-$\ast$ positions?
- $\mathrm{MCSP}^A$: circuits with oracle gates for $A$.
- Restricted-class versions: $\mathrm{DNF}\text{-MCSP}$, $\mathrm{Formula}\text{-MCSP}$, $\mathrm{AC}^0_d\text{-MCSP}$.

## 3. History & State of the Art (SOTA)

- **1950s–60s (USSR).** Circuit minimization is the archetypal *perebor* ("brute-force search") problem. Trakhtenbrot's history (1984) records that Levin delayed publishing his $\mathsf{NP}$-completeness paper partly because he could not settle the status of circuit minimization.
- **1979.** Masek shows minimizing a DNF given a DNF is $\mathsf{NP}$-hard (unpublished manuscript, widely cited).
- **1998.** Umans proves the Minimum Equivalent DNF problem is $\Sigma_2^p$-complete — the *succinct-input* version is provably harder than $\mathsf{NP}$ under standard assumptions.
- **2000.** Kabanets and Cai (STOC) name MCSP, place it in $\mathsf{NP}$, and prove the first structural consequences: $\mathrm{MCSP}\in\mathsf{P}$ implies there are no cryptographic pseudorandom generators (hence no one-way functions); and $\mathsf{NP}$-hardness under "natural" (locally computable, parameter-controlled) reductions would imply $\mathsf{EXP}\not\subseteq \mathsf{P/poly}$.
- **2006.** Allender, Buhrman, Koucký, van Melkebeek, Ronneburger (SICOMP) prove $\mathsf{PSPACE}\subseteq \mathsf{P}^{R_{KT}}$ and $\mathsf{NEXP}\subseteq \mathsf{NP}^{R_{KT}}$ using random strings; the techniques give $\mathsf{BPP}\subseteq \mathsf{ZPP}^{\mathrm{MCSP}}$.
- **2017.** Murray and Williams (CCC) show MCSP is not $\mathsf{NP}$-hard under *local* (sublinear-time-computable) reductions unless $\mathsf{EXP} \ne \mathsf{ZPP}$ — i.e. the easy route is blocked. Allender and Das show $\mathsf{SZK}\subseteq \mathsf{BPP}^{\mathrm{MCSP}}$.
- **2018–2020.** Hirahara's non-black-box worst-case-to-average-case reduction (FOCS 2018) shows $\mathsf{NP}$-hardness of $\mathrm{Gap}$-MCSP would imply average-case hardness of $\mathsf{NP}$ — an "excluded middle" that makes hardness both desirable and expensive.
- **2020–2023.** Restricted versions fall: multi-output MCSP (Ilango–Loff–Oliveira), constant-depth-formula MCSP and Partial-MCSP for formulas (Ilango), and finally Partial-MCSP is $\mathsf{NP}$-hard under randomized reductions (Hirahara, FOCS 2022). The general (total-function, general-circuit) case remains open.

## 4. Partial Results / Verified Cases

| Variant / regime | Status |
|---|---|
| $s = O(\log N/\log\log N)$ | In $\mathsf{P}$ by brute force over $2^{O(s\log s)}$ circuits |
| Minimum equivalent DNF (input: a formula) | $\Sigma_2^p$-complete (Umans 1998) |
| DNF minimization from a truth table | $\mathsf{NP}$-complete (Allender–Hellerstein–McCabe–Pitassi–Saks 2008; approximation hardness within $N^{\gamma}$) |
| Multi-output MCSP (MOCSP) | $\mathsf{NP}$-complete (Ilango–Loff–Oliveira 2020) |
| Constant-depth formula MCSP, $d\ge 2$ fixed | $\mathsf{NP}$-hard (Ilango 2020) |
| Partial-MCSP (general circuits, $\{0,1,\ast\}$ inputs) | $\mathsf{NP}$-hard under randomized poly-time reductions (Hirahara 2022) |
| $\mathrm{MCSP}^{\mathrm{QBF}}$ | Hard for $\mathsf{PSPACE}$ under $\mathsf{ZPP}$ reductions (Allender–Holden–Kabanets 2017) |
| Lower bounds for MCSP itself | $N^{3-o(1)}$ de Morgan formula, $N^{2-o(1)}$ full-basis formula and branching-program bounds — matching the best known for *any* explicit function (Cheraghchi–Kabanets–Lu–Myrisiotis 2019) |
| Oracle separations | Relativized worlds where MCSP is not $\mathsf{NP}$-complete and where it is not in $\mathsf{P}$ |

Negative/limiting results are equally "verified": MCSP is not $\mathsf{NP}$-hard under logtime-uniform $\mathsf{AC}^0$ or other local reductions unless standard separations follow (Murray–Williams 2017), and Turing-reduction $\mathsf{NP}$-hardness would give circuit lower bounds (Saks–Santhanam 2020).

## 5. Principal Obstacles

- **Exponentially long instances.** A reduction from SAT on $m$ variables must output a truth table of length $N$, and to argue correctness it must compute or bound $\mathrm{CC}$ of that table. Computing $\mathrm{CC}$ is exactly the problem being reduced to; bounding it from *below* is a circuit lower bound. So the standard gadget-reduction toolkit is inapplicable: any reduction is implicitly proving lower bounds.
- **The Kabanets–Cai barrier.** Reductions with mild uniformity/locality provably cannot exist unless one first proves separations like $\mathsf{EXP}\not\subseteq\mathsf{P/poly}$ or $\mathsf{EXP}\ne\mathsf{ZPP}$. Every known $\mathsf{NP}$-hardness technique produces exactly such reductions.
- **Natural proofs, reversed.** By Razborov–Rudich, $\mathrm{MCSP}\in\mathsf{P}$ yields a natural property useful against $\mathsf{P/poly}$, breaking all pseudorandom function candidates. So proving $\mathrm{MCSP}\in\mathsf{P}$ is at least as hard as breaking cryptography; proving $\mathrm{MCSP}\notin\mathsf{P}$ implies $\mathsf{P}\ne\mathsf{NP}$. Both directions are locked behind major separations.
- **Hardness has a price.** Hirahara's reductions mean $\mathsf{NP}$-hardness of $\mathrm{Gap}$-MCSP implies average-case $\mathsf{NP}$-hardness ($\mathsf{DistNP}\not\subseteq\mathsf{AvgP}$), a statement nobody knows how to prove.
- **Total vs partial.** The $\mathsf{NP}$-hardness proofs for Partial-MCSP crucially use $\ast$ entries to encode combinatorial constraints. Filling in the $\ast$s changes $\mathrm{CC}$ in an uncontrolled way, and no "completion" lemma is known.
- **Relativization and algebrization.** Contradictory oracle results show the answer is not decidable by relativizing arguments.

## 6. The Gap

Proved: hardness for *multi-output*, *partial*, and *restricted-class* versions; membership in $\mathsf{NP}$; the search-to-decision and reduction-locality barriers; matching-frontier lower bounds against weak models.

Missing: a reduction $f$ from an $\mathsf{NP}$-complete language $L$ such that $x\in L \Rightarrow \mathrm{CC}(f(x)) \le s$ and $x\notin L \Rightarrow \mathrm{CC}(f(x)) > s$, where the *soundness* direction is a genuine circuit lower bound on an explicitly constructed truth table, and $f$ is *not* local (to evade Murray–Williams). The single crossing step is: **produce, in polynomial time from an $\mathsf{NP}$ instance, a total Boolean function whose circuit complexity is provably large in the "no" case.** Every current technique that certifies large $\mathrm{CC}$ does so either by counting (non-explicit) or by restriction/approximation methods that stall at $\mathsf{AC}^0[p]$.

## 7. Current Research (as of June 2026)

- **Meta-complexity school** (Hirahara, NII/Tokyo; Santhanam, Oxford; Oliveira, Warwick; Ilango, MIT/IAS; Ren, Berkeley). Central programme: derive $\mathsf{NP}$-hardness of gap versions and convert it into average-case hardness of $\mathsf{NP}$ and into cryptographic characterisations.
- **Cryptography from meta-complexity.** Liu–Pass (FOCS 2020) show one-way functions exist iff time-bounded Kolmogorov complexity $K^t$ is mildly hard on average; Hirahara's "Capturing one-way functions via NP-hardness of meta-complexity" (STOC 2023) pushes this toward MCSP-style measures. Active work seeks an unconditional equivalence between OWF existence and average-case MCSP hardness. *(frontier — verify)*
- **Learning connections.** Carmosino–Impagliazzo–Kabanets–Kolokolova give PAC learning from natural properties; MCSP algorithms would yield learners, and conversely hardness of learning is being used to constrain MCSP.
- **Closing the total/partial gap.** Attempts to derandomize Hirahara's randomized reduction and to eliminate $\ast$ entries, e.g. via "robust" or error-tolerant circuit complexity measures. *(frontier — verify)*
- **Oracle and proof-complexity barriers.** Systematic mapping of which relativizing or black-box techniques are ruled out (Hirahara–Watanabe).

## 8. Future Work

- Prove $\mathsf{NP}$-hardness of $\mathrm{Gap}_{\alpha}$-MCSP for some $\alpha > 1$, accepting the consequence $\mathsf{DistNP}\not\subseteq\mathsf{AvgP}$.
- Derandomize the Partial-MCSP hardness reduction, then attack the $\ast$-completion problem.
- Settle MCSP vs MKTP: exhibit a reduction in either direction, or an oracle separating them.
- Push unconditional lower bounds for MCSP beyond formulas into $\mathsf{AC}^0[p]$ or $\mathsf{TC}^0$ — Allender has argued this is the most tractable near-term target.
- Determine whether MCSP is hard for $\mathsf{NP}$ under *non-uniform* or randomized Turing reductions, and extract circuit lower bounds from that (Saks–Santhanam programme).

## 9. Key References

- **[Foundational]** B. A. Trakhtenbrot. *A Survey of Russian Approaches to Perebor (Brute-Force Searches) Algorithms.* Annals of the History of Computing, 6(4):384–400, 1984.
- **[Foundational]** V. Kabanets, J.-Y. Cai. *Circuit Minimization Problem.* Proc. 32nd ACM Symposium on Theory of Computing (STOC), 2000.
- **[Foundational]** A. Razborov, S. Rudich. *Natural Proofs.* Journal of Computer and System Sciences, 55(1):24–35, 1997.
- **[Foundational]** E. Allender, H. Buhrman, M. Koucký, D. van Melkebeek, D. Ronneburger. *Power from Random Strings.* SIAM Journal on Computing, 35(6):1467–1493, 2006.
- **[Foundational]** C. Umans. *The Minimum Equivalent DNF Problem and Shortest Implicants.* Proc. 39th IEEE Symposium on Foundations of Computer Science (FOCS), 1998.
- **[SOTA / Recent]** C. Murray, R. R. Williams. *On the (Non) NP-Hardness of Computing Circuit Complexity.* Theory of Computing, 13(4):1–22, 2017.
- **[SOTA / Recent]** S. Hirahara. *Non-Black-Box Worst-Case to Average-Case Reductions within NP.* Proc. 59th IEEE Symposium on Foundations of Computer Science (FOCS), 2018.
- **[SOTA / Recent]** R. Ilango, B. Loff, I. C. Oliveira. *NP-Hardness of Circuit Minimization for Multi-Output Functions.* Proc. 35th Computational Complexity Conference (CCC), 2020.
- **[SOTA / Recent]** R. Ilango. *Constant Depth Formula and Partial Function Versions of MCSP are Hard.* Proc. 61st IEEE Symposium on Foundations of Computer Science (FOCS), 2020.
- **[SOTA / Recent]** S. Hirahara. *NP-Hardness of Learning Programs and Partial MCSP.* Proc. 63rd IEEE Symposium on Foundations of Computer Science (FOCS), 2022.
- **[SOTA / Recent]** Y. Liu, R. Pass. *On One-Way Functions and Kolmogorov Complexity.* Proc. 61st IEEE Symposium on Foundations of Computer Science (FOCS), 2020.
- **[SOTA / Recent]** M. Cheraghchi, V. Kabanets, Z. Lu, D. Myrisiotis. *Circuit Lower Bounds for MCSP from Local Pseudorandom Generators.* Proc. 46th International Colloquium on Automata, Languages, and Programming (ICALP), 2019.
- **[SOTA / Recent]** M. Saks, R. Santhanam. *Circuit Lower Bounds from NP-Hardness of MCSP under Turing Reductions.* Proc. 35th Computational Complexity Conference (CCC), 2020.
- **[Survey]** E. Allender. *The New Complexity Landscape Around Circuit Minimization.* Proc. 14th International Conference on Language and Automata Theory and Applications (LATA), Springer LNCS, 2020.
- **[Survey]** E. Allender, S. Hirahara. *New Insights on the (Non-)Hardness of Circuit Minimization and Related Problems.* ACM Transactions on Computation Theory, 11(4), 2019.

## 10. Worked Example / Concrete Special Case

Take $n = 2$, so $N = 4$. Consider the truth table $T = 0110$ read in the order $(x_1x_2) = 00, 01, 10, 11$; this is $f = x_1 \oplus x_2$.

**Is $(T, 1) \in \mathrm{MCSP}$?** Over the basis $B_2$ of all $16$ binary gates, $\oplus \in B_2$, so a single gate suffices: $\mathrm{CC}(f) = 1$ and the answer is **yes**.

**Change the basis to de Morgan** ($\wedge, \vee$ with free negations). Then $\mathrm{CC}_{\text{DM}}(x_1\oplus x_2) = 3$, realized by

$$x_1 \oplus x_2 = (x_1 \vee x_2) \wedge \neg(x_1 \wedge x_2).$$

*Lower bound by exhaustion.* With $\le 2$ gates and negations free, every circuit output is one of the following forms: a literal $\ell_1$; $\ell_1 \circ \ell_2$; or $(\ell_1 \circ \ell_2) \circ \ell_3$ with $\circ \in \{\wedge,\vee\}$, where each $\ell_i \in \{x_1,\neg x_1, x_2, \neg x_2\}$. Every such function is monotone in each variable after fixing polarities — i.e. it is a "unate" function. But $\oplus$ is not unate: setting $x_2 = 0$ makes $f = x_1$ (increasing in $x_1$), while setting $x_2 = 1$ makes $f = \neg x_1$ (decreasing in $x_1$). No unate function has this behaviour, so no $2$-gate de Morgan circuit computes $\oplus$. Hence $\mathrm{CC}_{\text{DM}}(f) = 3$ and $(T,2)\notin \mathrm{DM\text{-}MCSP}$.

**What this exhibits.** The hard direction was the *lower* bound, and we proved it by enumerating all $O(1)$ circuits of size $\le 2$ — feasible only because $n = 2$. For $n = 20$ the input is $N = 2^{20} \approx 10^6$ bits and the interesting bound is $s \approx N/\log N \approx 52{,}000$; enumeration touches $2^{\Theta(s\log s)}$ circuits, astronomically more than $\mathrm{poly}(N)$. Meanwhile a "no" certificate would be a lower bound of $52{,}000$ gates on an explicit function — and the best unconditional lower bound known for any explicit function is $(3+\tfrac{1}{86})n$ gates (Find–Golovnev–Hirsch–Kulikov, 2016). That gap between the trivial upper bound and the state of the art in explicit lower bounds is exactly the gap of Section 6.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*