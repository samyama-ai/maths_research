---
id: 10-theoretical-cs/randomized-exponential-time-hypothesis
title: "Randomized Exponential Time Hypothesis"
topic: 10-theoretical-cs
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Randomized Exponential Time Hypothesis

> **Topic:** Theoretical Computer Science · **ID:** `10-theoretical-cs/randomized-exponential-time-hypothesis` · **Status:** open

## 1. Problem Statement / Conjecture

The **Randomized Exponential Time Hypothesis (rETH)** asserts that $3$-SAT cannot be solved in subexponential time even by randomized algorithms with bounded two-sided error:

$$3\text{-SAT} \notin \mathsf{BPTIME}\!\left(2^{o(n)}\right),$$

where $n$ is the number of variables. Equivalently: there is a constant $\delta > 0$ such that no randomized algorithm decides satisfiability of $3$-CNF formulas on $n$ variables in time $O(2^{\delta n})$ with error probability at most $1/3$.

rETH is the probabilistic strengthening of the Exponential Time Hypothesis (ETH) of Impagliazzo and Paturi. It is strictly stronger as a formal statement ($\text{rETH} \Rightarrow \text{ETH}$, since deterministic algorithms are randomized algorithms), and it is the hypothesis actually required whenever a fine-grained hardness reduction is itself randomized — for instance any reduction routed through the Valiant–Vazirani isolation lemma.

A **proof** of rETH would imply $\mathsf{NP} \not\subseteq \mathsf{BPP}$, hence $\mathsf{P} \neq \mathsf{NP}$; it is therefore at least as hard as the $\mathsf{P}$ vs $\mathsf{NP}$ problem and no proof is expected with current techniques. A **disproof** would be a randomized $2^{o(n)}$ algorithm for $3$-SAT, collapsing the entire fine-grained lower-bound program built on ETH-style assumptions. The realistic open questions are (a) whether $\text{ETH} \Rightarrow \text{rETH}$ unconditionally, and (b) whether rETH can be based on a weaker or more structurally understood assumption.

## 2. Mathematical Foundations

**$k$-SAT complexity exponents.** For $k \ge 3$ define

$$s_k \;=\; \inf\big\{\, \delta \ge 0 \;:\; k\text{-SAT} \in \mathsf{DTIME}(2^{\delta n})\,\big\}, \qquad
s_k^{\mathrm{BP}} \;=\; \inf\big\{\, \delta \ge 0 \;:\; k\text{-SAT} \in \mathsf{BPTIME}(2^{\delta n})\,\big\}.$$

Then $s_k^{\mathrm{BP}} \le s_k$, and:

- **ETH:** $s_3 > 0$.
- **rETH:** $s_3^{\mathrm{BP}} > 0$.
- **SETH:** $\lim_{k\to\infty} s_k = 1$; **rSETH:** $\lim_{k\to\infty} s_k^{\mathrm{BP}} = 1$.

**Complexity class.** $L \in \mathsf{BPTIME}(t(n))$ iff there is a probabilistic Turing machine $M$ running in time $O(t(n))$ with
$$x \in L \Rightarrow \Pr[M(x)=1] \ge 2/3, \qquad x \notin L \Rightarrow \Pr[M(x)=1] \le 1/3 .$$
By Chernoff amplification, repeating $M$ $\;r$ times reduces error to $2^{-\Omega(r)}$ at cost $O(r\,t(n))$; taking $r = \Theta(n)$ keeps a $2^{o(n)}$ algorithm inside $2^{o(n)}$, so the error constant $1/3$ is immaterial to rETH.

**Sparsification Lemma** (Impagliazzo–Paturi–Zane, 2001). For every $\varepsilon>0$ and $k$ there is $C = C(k,\varepsilon)$ and an algorithm running in time $2^{\varepsilon n}\,\mathrm{poly}(n)$ that maps a $k$-CNF $F$ on $n$ variables to $k$-CNFs $F_1,\dots,F_t$ with $t \le 2^{\varepsilon n}$, each having at most $Cn$ clauses, such that
$$F \text{ satisfiable} \iff \bigvee_{i=1}^{t} F_i \text{ satisfiable}.$$
Consequently rETH is equivalent to its "$m$-version": no randomized $2^{o(n+m)}$ algorithm for $3$-SAT.

**Monotonicity and the width–density duality.** $s_3 \le s_4 \le \cdots$, and Calabro–Impagliazzo–Paturi show $s_\infty = \lim_k s_k$ exists and equals the exponent for CNF-SAT with $m = O(n)$ clauses; the same monotone structure holds for $s_k^{\mathrm{BP}}$. In particular $s_3^{\mathrm{BP}}>0 \iff s_k^{\mathrm{BP}}>0$ for every fixed $k \ge 3$.

**Hardness-vs-randomness bridge.** Impagliazzo–Wigderson: if $\mathsf{E} = \mathsf{DTIME}(2^{O(n)})$ requires Boolean circuits of size $2^{\Omega(n)}$, then $\mathsf{BPP} = \mathsf{P}$, via a pseudorandom generator with seed length $O(\log s)$ fooling size-$s$ circuits. Applied at exponential scale, this converts a randomized $2^{\varepsilon n}$ algorithm into a deterministic $2^{O(\varepsilon n)}$ one, so
$$\text{ETH} \;\wedge\; \big(\mathsf{E} \not\subseteq \mathsf{SIZE}(2^{o(n)})\big) \;\Longrightarrow\; \text{rETH}.$$

## 3. History & State of the Art (SOTA)

- **1999.** Impagliazzo and Paturi introduce $s_k$ and ETH in *On the Complexity of $k$-SAT*, proving $s_k \le s_{k+1}$ and $s_k \ge (1 - d/k)s_\infty$ for a constant $d$ — so ETH $\Rightarrow$ $s_\infty > 0$.
- **2001.** Impagliazzo–Paturi–Zane prove the Sparsification Lemma, making ETH robust and giving the standard "$2^{o(n+m)}$" formulation. Both proofs are algorithmic and transfer verbatim to the randomized exponents $s_k^{\mathrm{BP}}$.
- **1998–2005.** Randomized upper bounds: Schöning's random-walk algorithm runs in $O^*\big((2-2/k)^n\big)$; PPSZ (Paturi–Pudlák–Saks–Zane) gives $s_k^{\mathrm{BP}} \le 1 - \mu_k/k$ with $\mu_k \to \pi^2/6$, i.e. $2^{n(1-\Theta(1/k))}$.
- **2008.** Calabro–Impagliazzo–Kabanets–Paturi prove an isolation lemma for $k$-CNFs: $k$-SAT reduces to Unique-$k$-SAT by a *randomized* reduction with only a $2^{\varepsilon n}$ overhead, giving $s_k - \sigma_k \to 0$ where $\sigma_k$ is the Unique-$k$-SAT exponent. The conclusion is naturally a statement about randomized time — the canonical place where rETH rather than ETH is the right hypothesis.
- **2011–2021.** Hertli shows PPSZ's unique-SAT bound holds in general, giving $3$-SAT in $O(1.308^n)$ randomized time; Hansen–Kaplan–Zamir–Zwick (biased PPSZ) reach $O(1.307^n)$; Scheder's *PPSZ is better than you think* improves the general-$k$ analysis. These are the SOTA upper bounds, all randomized, all still $2^{\Theta(n)}$.
- **2016–2017.** Gap-ETH (Dinur; Manurangsi–Raghavendra) is stated in randomized form for exactly this reason: the gap-amplification route uses randomized sub-exponential reductions.

**Status.** rETH is open, unproven and unrefuted; no unconditional separation of $s_3^{\mathrm{BP}}$ from $0$ exists, and no unconditional implication $\text{ETH} \Rightarrow \text{rETH}$ is known.

## 4. Partial Results / Verified Cases

- **Conditional derivation.** rETH follows from ETH together with $\mathsf{E} \not\subseteq \mathsf{i.o.\text{-}SIZE}(2^{o(n)})$ (Impagliazzo–Wigderson / Nisan–Wigderson). Since the latter is widely believed, ETH and rETH are believed equivalent; the equivalence is *proved* only relative to that circuit lower bound.
- **Equivalence across $k$.** rETH for $3$-SAT $\iff$ rETH for $k$-SAT for every fixed $k \ge 3$ $\iff$ rETH for CNF-SAT with $m = O(n)$ clauses (sparsification). Verified unconditionally.
- **Restricted algorithm models.** Exponential lower bounds are unconditional for randomized algorithms confined to specific proof systems: randomized resolution-based DPLL solvers inherit the $2^{\Omega(n)}$ resolution-width lower bounds of Ben-Sasson–Wigderson on random $3$-CNFs; myopic and greedy DPLL variants have unconditional exponential lower bounds (Alekhnovich–Hirsch–Itsykson). These cover *all current practical solvers*, but not general $\mathsf{BPTIME}$.
- **Tightness of the SOTA upper bound.** Scheder–Steinberger show the PPSZ analysis is essentially tight for its own algorithm, so no improvement of $s_3^{\mathrm{BP}}$ below roughly $\log_2 1.307 \approx 0.386$ comes from PPSZ alone.
- **Downstream verified consequences.** Under rETH: no randomized $2^{o(n)}$ algorithm for Independent Set, Vertex Cover, $3$-Coloring, Hamiltonicity on $n$-vertex graphs; no randomized $f(k)\,n^{o(k)}$ algorithm for $k$-Clique; permanent and Tutte-polynomial exponential lower bounds (Dell–Husfeldt–Marx–Taslaman–Wahlén) hold in randomized form under the counting analogue $\\#$rETH.
- **Parameter ranges settled algorithmically.** For $k$-SAT with clause density below the satisfiability threshold and for $2$-SAT ($k=2$, polynomial time), the hypothesis is vacuous or false; rETH concerns only $k \ge 3$ with $m = \Theta(n)$.

## 5. Principal Obstacles

- **It implies $\mathsf{P} \neq \mathsf{NP}$.** Any proof must beat relativization, natural proofs (Razborov–Rudich), and algebrization. No known technique proves superpolynomial, let alone $2^{\Omega(n)}$, lower bounds for general (even deterministic) Turing machines on an $\mathsf{NP}$ problem.
- **Derandomization is the missing ingredient for ETH $\Rightarrow$ rETH.** Removing randomness generically needs a hard function in $\mathsf{E}$; proving such a circuit lower bound is itself a decades-open problem. There is no known "randomness-free" argument that a randomized subexponential $3$-SAT algorithm can be simulated deterministically at the same exponential scale.
- **Diagonalization gives nothing at this granularity.** The time hierarchy theorems separate $\mathsf{BPTIME}(2^{\delta n})$ from $\mathsf{BPTIME}(2^{n})$ only for artificial languages, and hierarchy theorems for $\mathsf{BPTIME}$ require advice (Barak; Fortnow–Santhanam). None places a *specific* natural problem like $3$-SAT outside a subexponential randomized class.
- **Algebraic and Fourier-analytic tools plateau.** Polynomial-method lower bounds and communication-complexity reductions produce $n^{1+\Omega(1)}$-type bounds, not $2^{\Omega(n)}$; the polynomial method has instead produced faster algorithms (e.g. for $\mathsf{ACC}$-SAT), pushing in the opposite direction.
- **Randomized reductions break the "for-free" transfer.** Many fine-grained reductions preserve deterministic time, but isolation- and hashing-based ones (Valiant–Vazirani, Gap-ETH amplification) do not; there is no known way to derandomize the $k$-CNF isolation lemma while keeping the $2^{\varepsilon n}$ overhead.

## 6. The Gap

Proven: (i) rETH $\Rightarrow$ ETH; (ii) ETH $+$ exponential circuit lower bound for $\mathsf{E}$ $\Rightarrow$ rETH; (iii) rETH is invariant across $k \ge 3$ and across $n$ vs $n+m$ parameterizations.

Not proven, and this is the precise boundary:

1. **ETH $\Rightarrow$ rETH unconditionally.** The gap is exactly the missing unconditional derandomization of $\mathsf{BPTIME}(2^{\delta n})$ into $\mathsf{DTIME}(2^{O(\delta) n})$. Nothing rules out a world where $3$-SAT has a randomized $2^{o(n)}$ algorithm but no deterministic one — such a world would need $\mathsf{E}$ to have $2^{o(n)}$-size circuits, which no one can currently exclude.
2. **Any unconditional lower bound $s_3^{\mathrm{BP}} > 0$.** The gap between the best proved randomized lower bound for $3$-SAT (essentially $\Omega(n)$ time, trivial) and the conjectured $2^{\Omega(n)}$ is the full $\mathsf{P}$ vs $\mathsf{NP}$ chasm.

## 7. Current Research (as of June 2026)

- **Hardness-vs-randomness at exponential scale.** Work on "algorithms from hardness" and on non-black-box derandomization (Chen–Tell style *hardness-to-randomness for uniform computation*) aims to reduce the circuit-lower-bound premise needed for $\text{ETH} \Rightarrow \text{rETH}$ to a uniform hardness assumption. Groups at UC Berkeley/Simons, Tel Aviv, and IAS are active here. *(frontier — verify)*
- **Improved randomized $k$-SAT algorithms.** Post-Scheder refinements of PPSZ and of Schöning-style local search continue to shave the base of $s_k^{\mathrm{BP}}$; the target of interest is whether $s_k^{\mathrm{BP}} \le 1 - \omega(1/k)\cdot k^{-1}$ is achievable, which would refute rSETH without touching rETH. *(frontier — verify)*
- **Derandomizing the $k$-CNF isolation lemma.** A deterministic isolation with $2^{\varepsilon n}$ overhead would let many Unique-SAT-based lower bounds be stated under ETH rather than rETH. Partial derandomizations for structured formula classes exist. *(frontier — verify)*
- **Fine-grained hypothesis cartography.** Nondeterministic and Merlin–Arthur variants (NSETH, MAETH; Carmosino–Gao–Impagliazzo–Mihajlin–Paturi–Schneider) are used to show which reductions *cannot* exist; the randomized analogues are being mapped by the same community (UCSD, MIT, Copenhagen/BARC, Saarbrücken).
- **Gap-ETH.** Whether the randomized Gap-ETH can be replaced by a deterministic version remains a headline question for parameterized inapproximability.

## 8. Future Work

- Prove ETH $\Rightarrow$ rETH from a *uniform* assumption (e.g. $\mathsf{E} \not\subseteq \mathsf{BPP}$-uniform circuits) rather than a non-uniform circuit lower bound.
- Derandomize the Calabro–Impagliazzo–Kabanets–Paturi isolation lemma; equivalently, find a deterministic $2^{\varepsilon n}$-overhead reduction $k$-SAT $\to$ Unique-$k$-SAT.
- Establish unconditional $2^{\Omega(n)}$ randomized lower bounds in stronger proof systems (Res($k$), Cutting Planes, Sum-of-Squares) to extend the "verified restricted models" frontier of Section 4.
- Determine whether rETH and rSETH separate: is $s_3^{\mathrm{BP}} > 0$ compatible with $\lim_k s_k^{\mathrm{BP}} < 1$? A randomized CNF-SAT algorithm in $2^{n(1-\varepsilon)}$ would settle this.
- Catalogue systematically which of the hundreds of ETH-based lower bounds genuinely require rETH because their reductions are randomized.

## 9. Key References

- **[Foundational]** Russell Impagliazzo, Ramamohan Paturi. *On the Complexity of $k$-SAT.* Journal of Computer and System Sciences 62(2):367–375, 2001.
- **[Foundational]** Russell Impagliazzo, Ramamohan Paturi, Francis Zane. *Which Problems Have Strongly Exponential Complexity?* Journal of Computer and System Sciences 63(4):512–530, 2001.
- **[Foundational]** Russell Impagliazzo, Avi Wigderson. *P = BPP if E Requires Exponential Circuits: Derandomizing the XOR Lemma.* STOC 1997, pp. 220–229.
- **[Foundational]** Noam Nisan, Avi Wigderson. *Hardness vs. Randomness.* Journal of Computer and System Sciences 49(2):149–167, 1994.
- **[Foundational]** Leslie G. Valiant, Vijay V. Vazirani. *NP is as Easy as Detecting Unique Solutions.* Theoretical Computer Science 47:85–93, 1986.
- **[SOTA / Recent]** Chris Calabro, Russell Impagliazzo, Valentine Kabanets, Ramamohan Paturi. *The Complexity of Unique $k$-SAT: An Isolation Lemma for $k$-CNFs.* Journal of Computer and System Sciences 74(3):386–393, 2008.
- **[SOTA / Recent]** Ramamohan Paturi, Pavel Pudlák, Michael E. Saks, Francis Zane. *An Improved Exponential-Time Algorithm for $k$-SAT.* Journal of the ACM 52(3):337–364, 2005.
- **[SOTA / Recent]** Timon Hertli. *3-SAT Faster and Simpler — Unique-SAT Bounds for PPSZ Hold in General.* SIAM Journal on Computing 43(2):718–729, 2014.
- **[SOTA / Recent]** Thomas Dueholm Hansen, Haim Kaplan, Or Zamir, Uri Zwick. *Faster $k$-SAT Algorithms Using Biased-PPSZ.* STOC 2019, pp. 578–589.
- **[SOTA / Recent]** Dominik Scheder. *PPSZ is Better Than You Think.* FOCS 2021, pp. 205–216.
- **[SOTA / Recent]** Uwe Schöning. *A Probabilistic Algorithm for $k$-SAT and Constraint Satisfaction Problems.* FOCS 1999, pp. 410–414.
- **[SOTA / Recent]** Holger Dell, Thore Husfeldt, Dániel Marx, Nina Taslaman, Martin Wahlén. *Exponential Time Complexity of the Permanent and the Tutte Polynomial.* ACM Transactions on Algorithms 10(4):21, 2014.
- **[SOTA / Recent]** Marco L. Carmosino, Jiawei Gao, Russell Impagliazzo, Ivan Mihajlin, Ramamohan Paturi, Stefan Schneider. *Nondeterministic Extensions of the Strong Exponential Time Hypothesis and Consequences for Non-reducibility.* ITCS 2016, pp. 261–270.
- **[SOTA / Recent]** Pasin Manurangsi, Prasad Raghavendra. *A Birthday Repetition Theorem and Complexity of Approximating Dense CSPs.* ICALP 2017.
- **[Survey]** Daniel Lokshtanov, Dániel Marx, Saket Saurabh. *Lower Bounds Based on the Exponential Time Hypothesis.* Bulletin of the EATCS 105:41–72, 2011.
- **[Survey]** Marek Cygan, Fedor V. Fomin, Łukasz Kowalik, Daniel Lokshtanov, Dániel Marx, Marcin Pilipczuk, Michał Pilipczuk, Saket Saurabh. *Parameterized Algorithms.* Springer, 2015 (Chapter 14).
- **[Survey]** Ryan Williams. *Some Estimated Likelihoods for Computational Complexity.* In *Computing and Software Science: State of the Art and Perspectives*, LNCS 10000, Springer, 2019.

## 10. Worked Example / Concrete Special Case

**Claim.** Under rETH, Maximum Independent Set on an $N$-vertex graph admits no randomized $2^{o(N)}$-time algorithm.

*Step 1 — sparsify.* Fix $\varepsilon = 0.01$. Given a $3$-CNF $F$ on $n$ variables with arbitrarily many clauses, the Sparsification Lemma produces, in time $2^{0.01n}\mathrm{poly}(n)$, at most $t \le 2^{0.01n}$ formulas $F_1,\dots,F_t$, each with $m_i \le Cn$ clauses, $C = C(3,0.01)$, and $F$ satisfiable iff some $F_i$ is.

*Step 2 — reduce.* Apply the textbook $3$-SAT $\to$ Independent Set reduction to each $F_i$: one triangle per clause (a vertex per literal occurrence), plus an edge between every pair of complementary literals in different triangles. The graph $G_i$ has $N_i = 3m_i \le 3Cn$ vertices, and $F_i$ is satisfiable iff $G_i$ has an independent set of size $m_i$.

*Step 3 — plug in the hypothetical algorithm.* Suppose $\mathcal{A}$ decides Independent Set in randomized time $2^{o(N)}$ with error $\le 1/3$. Run $\mathcal{A}$ on each $G_i$, amplifying to error $\le 2^{-2n}$ by $O(n)$ independent repetitions. Total time:
$$t \cdot O(n) \cdot 2^{o(N_i)} \;\le\; 2^{0.01n}\cdot O(n)\cdot 2^{o(3Cn)} \;=\; 2^{0.01n + o(n)} .$$
By a union bound over $t \le 2^{0.01n}$ calls, the probability that any call errs is at most $2^{0.01n}\cdot 2^{-2n} \ll 1/3$. So $3$-SAT is decided in randomized time $2^{0.02n}$ for large $n$ — and since $\varepsilon$ was arbitrary, in randomized time $2^{\delta n}$ for every $\delta > 0$, contradicting rETH. $\square$

**Why rETH and not ETH.** Replace Step 2 with the Valiant–Vazirani-style isolation of Calabro–Impagliazzo–Kabanets–Paturi: hash the variable space with a random subcube restriction so that, with probability $2^{-\varepsilon n}$-boundedly close to constant, a satisfiable $F_i$ has exactly one satisfying assignment. The composed reduction is now genuinely randomized: even if the downstream algorithm for Unique-$3$-SAT were *deterministic* and ran in $2^{o(n)}$, the composition only yields a *randomized* $2^{o(n)}$ algorithm for $3$-SAT. That contradicts rETH but not ETH. This is the exact sense in which rETH is the operative hypothesis for isolation-based, gap-amplification-based, and hashing-based fine-grained lower bounds.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*