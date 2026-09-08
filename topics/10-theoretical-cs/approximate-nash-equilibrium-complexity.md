---
id: 10-theoretical-cs/approximate-nash-equilibrium-complexity
title: "Nash Equilibrium Approximation Complexity"
topic: 10-theoretical-cs
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Nash Equilibrium Approximation Complexity

> **Topic:** Theoretical Computer Science · **ID:** `10-theoretical-cs/approximate-nash-equilibrium-complexity` · **Status:** open

## 1. Problem Statement / Conjecture

For a two-player game given by payoff matrices $R, C \in [0,1]^{n \times n}$, an **$\varepsilon$-approximate Nash equilibrium** ($\varepsilon$-NE) is a pair of mixed strategies in which neither player can gain more than $\varepsilon$ by deviating. Exact equilibria exist (Nash, 1951) but computing one is PPAD-complete (Daskalakis–Goldberg–Papadimitriou 2009; Chen–Deng–Teng 2009). The open question concerns the *approximate* problem:

**Central question.** For a fixed constant $\varepsilon \in (0,1)$, what is the exact complexity of finding an $\varepsilon$-NE of an $n \times n$ bimatrix game?

Two concrete open problems:

1. **(No-PTAS conjecture / algorithmic side.)** Does a PTAS exist — an algorithm running in time $\mathrm{poly}(n)$ for every fixed $\varepsilon$? The best known upper bound is the quasi-polynomial $n^{O(\log n/\varepsilon^2)}$ of Lipton–Markakis–Mehta (2003). Conjecturally no PTAS exists; a proof requires either a new hardness route or an unconditional lower bound.
2. **(Constant threshold.)** What is $\varepsilon^\star = \inf\{\varepsilon : \varepsilon\text{-NE is computable in polynomial time}\}$? Currently $\varepsilon^\star \le 1/3$ (Deligkas–Fasoulakis–Markakis 2022) and no unconditional lower bound $\varepsilon^\star > 0$ is known.

A complete resolution means either (a) a polynomial-time algorithm for all constant $\varepsilon$, or (b) a hardness proof under a standard complexity assumption (or unconditionally) ruling one out. The currently strongest hardness — Rubinstein (2016) — is conditional on the **Exponential Time Hypothesis for PPAD**, itself an unproven assumption.

## 2. Mathematical Foundations

**Game.** A bimatrix game $(R,C)$, $R,C\in[0,1]^{n\times n}$. Mixed strategies are $x,y \in \Delta_n = \{z \in \mathbb{R}^n_{\ge0} : \sum_i z_i = 1\}$. Payoffs are $x^\top R y$ (row) and $x^\top C y$ (column).

**$\varepsilon$-approximate Nash equilibrium.** $(x,y)$ is an $\varepsilon$-NE if
$$x^\top R y \;\ge\; \max_{x' \in \Delta_n} x'^\top R y - \varepsilon, \qquad x^\top C y \;\ge\; \max_{y' \in \Delta_n} x^\top C y' - \varepsilon .$$
Equivalently, with regret $f(x,y) = \max_i (Ry)_i - x^\top R y$ and $g(x,y) = \max_j (x^\top C)_j - x^\top C y$, the condition is $\max\{f,g\} \le \varepsilon$. Exact NE is $\varepsilon = 0$.

**$\varepsilon$-well-supported NE ($\varepsilon$-WSNE).** A stronger notion: every pure strategy in the support is an $\varepsilon$-best response,
$$\forall i \in \mathrm{supp}(x):\ (Ry)_i \ge \max_k (Ry)_k - \varepsilon, \qquad \forall j \in \mathrm{supp}(y):\ (x^\top C)_j \ge \max_k (x^\top C)_k - \varepsilon .$$
Every $\varepsilon$-WSNE is an $\varepsilon$-NE; the converse fails, and the known conversion loses a square root: an $\varepsilon^2/8$-NE yields an $\varepsilon$-WSNE.

**Complexity class.** $\mathrm{PPAD}$ (Papadimitriou 1994) is the class of total search problems reducible to `END-OF-LINE`: given circuits $S,P:\{0,1\}^m\to\{0,1\}^m$ with $P(S(0^m))=0^m \ne S(0^m)$, find $v$ with $P(S(v)) \ne v$ or $S(P(v)) \ne v \ne 0^m$. Totality comes from a parity argument on a directed graph of in/out-degree $\le 1$; the class sits inside $\mathrm{TFNP}$, and $\mathrm{PPAD}$-hardness of an $\mathrm{NP}$-total problem does not imply $\mathrm{NP}$-hardness.

**Sampling lemma (Althöfer / LMM).** If $(x,y)$ is a NE and $k = \lceil 12\ln n/\varepsilon^2\rceil$, then sampling $k$ pure strategies i.i.d. from $x$ and from $y$ and taking empirical distributions $(\hat x,\hat y)$ gives an $\varepsilon$-NE with positive probability. Hence there always exists an $\varepsilon$-NE with support size $O(\log n/\varepsilon^2)$, and exhaustive search over such supports (each support fixes an LP) runs in $n^{O(\log n/\varepsilon^2)}$.

**ETH for PPAD.** The hypothesis that `END-OF-LINE` on $m$-bit inputs requires $2^{\tilde\Omega(m)}$ time. Under it, no $n^{\tilde{o}(\log n)}$ algorithm computes an $\varepsilon$-NE for some constant $\varepsilon>0$, matching LMM up to the $\tilde{o}$.

## 3. History & State of the Art (SOTA)

- **1951.** Nash proves existence via Brouwer's fixed-point theorem; no algorithm.
- **1964.** Lemke–Howson give a pivoting algorithm; Savani–von Stengel (2004) construct games forcing exponentially many pivots.
- **1994.** Papadimitriou defines PPAD and conjectures NASH is complete for it.
- **2003.** Lipton, Markakis, Mehta: $n^{O(\log n/\varepsilon^2)}$ via logarithmic-support sampling — still the best upper bound after 23 years.
- **2006.** Daskalakis–Goldberg–Papadimitriou: 4-player, then 3-player NASH is PPAD-complete. Chen–Deng: 2-player NASH is PPAD-complete; Chen–Deng–Teng extend to $\varepsilon = n^{-\Theta(1)}$, ruling out an FPTAS unless $\mathrm{PPAD}=\mathrm{FP}$.
- **2006–2008.** Constant-factor race: $3/4$ (Kontogiannis–Panagopoulou–Spirakis), $1/2$ (Daskalakis–Mehta–Papadimitriou), $0.38$ (Bosse–Byrka–Markakis), $0.3393$ (Tsaknakis–Spirakis) — the latter stood for 15 years.
- **2015.** Braverman–Ko–Weinstein: under ETH, finding an $\varepsilon$-NE with near-optimal social welfare needs $n^{\tilde\Omega(\log n)}$ time.
- **2016.** Rubinstein: under ETH-for-PPAD, no $n^{\log^{1-o(1)} n}$ algorithm for $\varepsilon$-NE at some constant $\varepsilon$. Babichenko: $2^{\Omega(n)}$ payoff-query lower bound for $n$-player binary-action games.
- **2017.** Babichenko–Rubinstein: $2^{\Omega(n)}$ randomized communication lower bound for $\varepsilon$-NE in two-player $N\times N$ games ($N = 2^n$).
- **2018.** Kothari–Mehta: degree-$\Omega(\log n)$ sum-of-squares lower bound and a matching enumerative-algorithm lower bound.
- **2022–2023.** Deligkas–Fasoulakis–Markakis: polynomial-time $(1/3+\delta)$-NE for every $\delta>0$, the current record.

**SOTA summary.**

| Quantity | Best known |
|---|---|
| Upper bound, constant $\varepsilon$ | $n^{O(\log n/\varepsilon^2)}$ (LMM 2003) |
| Poly-time constant $\varepsilon$-NE | $1/3 + \delta$ (DFM 2022) |
| Poly-time constant $\varepsilon$-WSNE | $0.6528$ (Czumaj et al. 2019) |
| Unconditional lower bound | none (only $\varepsilon = n^{-\Theta(1)}$ PPAD-hardness) |
| Conditional lower bound | $n^{\log^{1-o(1)}n}$ under ETH-for-PPAD (Rubinstein 2016) |

## 4. Partial Results / Verified Cases

- **Inverse-polynomial $\varepsilon$.** For $\varepsilon = n^{-c}$ with $c$ a sufficiently large constant, finding an $\varepsilon$-NE is PPAD-complete (Chen–Deng–Teng 2009). Settled.
- **Zero-sum games** ($C = -R$). Exact equilibria via linear programming in polynomial time (von Neumann/Dantzig). Settled.
- **Constant rank.** If $\mathrm{rank}(R+C) = k$ is constant, an exact NE is computable in polynomial time (Lipton–Markakis–Mehta for $k=0$; Adsul–Garg–Mehta–Sohoni 2011 for $k=1$); an $\varepsilon$-NE for fixed rank in $\mathrm{poly}(n)\cdot(1/\varepsilon)^{O(k)}$ (Kannan–Theobald).
- **Sparse / low-support games.** Games where each row and column has $O(1)$ nonzero entries, and win-lose games with bounded degree, admit PTASes in restricted regimes.
- **Anonymous / symmetric multiplayer games.** Two-strategy anonymous games with $n$ players admit a PTAS (Daskalakis–Papadimitriou 2008), running in $\mathrm{poly}(n)\cdot(1/\varepsilon)^{O(1/\varepsilon^2)}$.
- **Support-size lower bound.** Feder–Nazerzadeh–Saberi (2007): for $\varepsilon < 1/2$, some games need $\varepsilon$-NE support $\Omega(\log n)$ — the LMM support bound is tight, so the quasi-polynomial enumeration cannot be improved *by that route*.
- **Constant thresholds achieved.** $\varepsilon$-NE: $3/4 \to 1/2 \to 0.38 \to 0.3393 \to 1/3+\delta$. $\varepsilon$-WSNE: $2/3 \to 0.6608 \to 0.6528$.

## 5. Principal Obstacles

- **PPAD-hardness does not scale with $\varepsilon$.** The reduction from `END-OF-LINE` to NASH embeds a Brouwer function on a grid; the "error" per gadget is inverse-polynomial in the circuit size. Amplifying to constant $\varepsilon$ requires a PCP-like theorem for PPAD, and no such theorem is known. Rubinstein's work builds a *bespoke* birthday-repetition argument that yields quasi-polynomial, not polynomial, hardness — and only under ETH.
- **Totality blocks NP-hardness.** NASH is total: a solution always exists. If $\varepsilon$-NASH were NP-hard, $\mathrm{NP} = \mathrm{coNP}$ would follow. So every standard NP-hardness technique is off the table by fiat.
- **Sum-of-squares fails.** Kothari–Mehta (2018) show that degree-$d$ SoS relaxations of the NE feasibility system cannot certify approximate equilibria for $d = o(\log n)$, and enumerative/support-based algorithms need $n^{\Omega(\log n)}$ — the two most natural algorithmic paradigms both hit the LMM barrier at the same place.
- **Descent gets stuck at 1/3.** Tsaknakis–Spirakis minimize the maximum regret $\max\{f,g\}$ by gradient descent on $\Delta_n\times\Delta_n$; the objective is non-convex and its stationary points genuinely attain regret near $0.3393$. DFM's improvement to $1/3$ escapes only some stationary points, via a careful case analysis; the analysis provably cannot go below $1/3$ without new structure.
- **Information-theoretic barriers only in the black-box model.** Babichenko's $2^{\Omega(n)}$ query bound and Babichenko–Rubinstein's communication bound are unconditional but apply to games given by an oracle or split between parties — they say nothing about explicitly-given $n\times n$ matrices, where the input already has $n^2$ bits.

## 6. The Gap

Proven: hardness at $\varepsilon = n^{-\Theta(1)}$ (unconditional modulo $\mathrm{PPAD}\ne\mathrm{FP}$), and quasi-polynomial hardness at some constant $\varepsilon$ *conditional on ETH-for-PPAD*. Algorithms: polynomial time for $\varepsilon \ge 1/3$, quasi-polynomial for all constant $\varepsilon$.

The gap is the entire interval $\varepsilon \in (0, 1/3)$ under standard assumptions, and it is a gap in two directions:

1. **Assumption gap.** ETH-for-PPAD is not implied by ETH or by $\mathrm{P}\ne\mathrm{NP}$. Deriving Rubinstein's conclusion from ETH alone requires a *quasi-polynomial PCP for PPAD* — a reduction that amplifies inverse-polynomial equilibrium error to constant error while blowing up size only polynomially. No such amplification is known for any total search problem.
2. **Exponent gap.** Even granting ETH-for-PPAD, the lower bound $n^{\log^{1-o(1)}n}$ and the upper bound $n^{O(\log n/\varepsilon^2)}$ differ in the $\varepsilon$-dependence of the exponent; the true rate as $\varepsilon \to 0$ is unknown.

## 7. Current Research (as of June 2026)

- **PCP for PPAD.** The central program: build error amplification for `END-OF-LINE`. Rubinstein's birthday-repetition and its refinements (Rubinstein, Deng, Babichenko) remain the only amplification technique; making it lossless would upgrade quasi-polynomial hardness to polynomial-time hardness under ETH. No breakthrough reported. *(frontier — verify)*
- **Constant-factor algorithms below 1/3.** Groups at Warwick (Savani, Fearnley, Deligkas at Royal Holloway) and AUEB (Markakis, Fasoulakis) continue refining the descent/LP-hybrid framework. Reported attempts to break $1/3$ rely on richer strategy mixtures over three or more supports. *(frontier — verify)*
- **WSNE below 0.6528.** Believed easier to move than the $\varepsilon$-NE record, since the $\varepsilon^2/8$ conversion loss suggests the two thresholds are not tightly coupled.
- **Structured classes.** Polymatrix, graphical, and constant-rank games; PTASes for network games with bounded treewidth. Also constrained/optimal $\varepsilon$-NE, where hardness is much better understood (Braverman–Ko–Weinstein).
- **Beyond worst case.** Smoothed analysis of Lemke–Howson, and average-case complexity of PPAD via cryptographic hardness (Choudhuri–Hubáček–Kamath–Pietrzak–Rosen–Rothblum: PPAD-hardness from `\#SAT`-based assumptions / iterated squaring), aiming to base ETH-for-PPAD on a cryptographic assumption.

## 8. Future Work

- Prove or refute a **PCP theorem for PPAD**: a size-$\mathrm{poly}(m)$ reduction from `END-OF-LINE` to constant-$\varepsilon$ NASH. This single step closes the assumption gap.
- **Base ETH-for-PPAD on standard cryptography.** Hardness of PPAD from indistinguishability obfuscation or from repeated squaring is known; an *exponential-time* version would make Rubinstein's theorem rest on a widely believed assumption.
- **Break the $1/3$ barrier**, or prove that the regret-descent framework cannot: a matching lower bound for the class of "polynomial-time convex-programming-based" algorithms would be the first evidence that $\varepsilon^\star > 0$ within a natural algorithmic model.
- **Extend SoS lower bounds** from degree $\Omega(\log n)$ to degree $n^{\Omega(1)}$, which would rule out a broad family of semidefinite relaxations outright.
- Determine the **exact $\varepsilon$-dependence** of the quasi-polynomial exponent, i.e. whether $n^{\Theta(\log n/\varepsilon^2)}$ is optimal or $n^{\Theta(\log n / \varepsilon)}$ suffices.

## 9. Key References

- **[Foundational]** John F. Nash. *Non-Cooperative Games.* Annals of Mathematics 54(2):286–295, 1951.
- **[Foundational]** Christos H. Papadimitriou. *On the Complexity of the Parity Argument and Other Inefficient Proofs of Existence.* Journal of Computer and System Sciences 48(3):498–532, 1994.
- **[Foundational]** Constantinos Daskalakis, Paul W. Goldberg, Christos H. Papadimitriou. *The Complexity of Computing a Nash Equilibrium.* SIAM Journal on Computing 39(1):195–259, 2009.
- **[Foundational]** Xi Chen, Xiaotie Deng, Shang-Hua Teng. *Settling the Complexity of Computing Two-Player Nash Equilibria.* Journal of the ACM 56(3), Article 14, 2009.
- **[Foundational]** Richard J. Lipton, Evangelos Markakis, Aranyak Mehta. *Playing Large Games Using Simple Strategies.* ACM Conference on Electronic Commerce (EC), pp. 36–41, 2003.
- **[SOTA / Recent]** Aviad Rubinstein. *Settling the Complexity of Computing Approximate Two-Player Nash Equilibria.* IEEE Symposium on Foundations of Computer Science (FOCS), pp. 258–265, 2016.
- **[SOTA / Recent]** Argyrios Deligkas, Michail Fasoulakis, Evangelos Markakis. *A Polynomial-Time Algorithm for 1/3-Approximate Nash Equilibria in Bimatrix Games.* European Symposium on Algorithms (ESA), 2022; journal version, ACM Transactions on Algorithms, 2023.
- **[SOTA / Recent]** Pravesh K. Kothari, Ruta Mehta. *Sum-of-Squares Meets Nash: Lower Bounds for Finding Any Equilibrium.* ACM Symposium on Theory of Computing (STOC), pp. 1241–1248, 2018.
- **[SOTA / Recent]** Yakov Babichenko. *Query Complexity of Approximate Nash Equilibria.* Journal of the ACM 63(4), Article 36, 2016.
- **[SOTA / Recent]** Yakov Babichenko, Aviad Rubinstein. *Communication Complexity of Approximate Nash Equilibria.* ACM Symposium on Theory of Computing (STOC), pp. 878–889, 2017.
- **[SOTA / Recent]** Mark Braverman, Young Kun Ko, Omri Weinstein. *Approximating the Best Nash Equilibrium in $n^{o(\log n)}$-Time Breaks the Exponential Time Hypothesis.* ACM–SIAM Symposium on Discrete Algorithms (SODA), pp. 970–982, 2015.
- **[SOTA / Recent]** Haralampos Tsaknakis, Paul G. Spirakis. *An Optimization Approach for Approximate Nash Equilibria.* Internet Mathematics 5(4):365–382, 2008.
- **[SOTA / Recent]** Constantinos Daskalakis, Aranyak Mehta, Christos H. Papadimitriou. *A Note on Approximate Nash Equilibria.* Theoretical Computer Science 410(17):1581–1588, 2009.
- **[SOTA / Recent]** Artur Czumaj, Argyrios Deligkas, Michail Fasoulakis, John Fearnley, Marcin Jurdziński, Rahul Savani. *Distributed Methods for Computing Approximate Equilibria.* Algorithmica 81(3):1205–1231, 2019.
- **[SOTA / Recent]** Tomás Feder, Hamid Nazerzadeh, Amin Saberi. *Approximating Nash Equilibria Using Small-Support Strategies.* ACM Conference on Electronic Commerce (EC), pp. 352–354, 2007.
- **[Survey]** Constantinos Daskalakis, Paul W. Goldberg, Christos H. Papadimitriou. *The Complexity of Computing a Nash Equilibrium.* Communications of the ACM 52(2):89–97, 2009.
- **[Survey]** Noam Nisan, Tim Roughgarden, Éva Tardos, Vijay V. Vazirani (eds.). *Algorithmic Game Theory.* Cambridge University Press, 2007 (Ch. 2 and Ch. 29).
- **[Survey]** Paul W. Goldberg. *A Survey of PPAD-Completeness for Computing Nash Equilibria.* In Surveys in Combinatorics 2011, London Mathematical Society Lecture Note Series 392, Cambridge University Press, 2011.

## 10. Worked Example / Concrete Special Case

**The Daskalakis–Mehta–Papadimitriou $1/2$-algorithm, run on a $3\times3$ game.**

Take $R, C \in [0,1]^{3\times3}$:
$$R = \begin{pmatrix} 1 & 0 & 0.2 \\ 0 & 1 & 0.4 \\ 0.3 & 0.3 & 0.9 \end{pmatrix}, \qquad C = \begin{pmatrix} 0 & 1 & 0.5 \\ 1 & 0 & 0.5 \\ 0.6 & 0.6 & 0.1 \end{pmatrix}.$$

The algorithm: pick any row $i$; let $j$ be the column player's best response to $i$; let $k$ be the row player's best response to $j$; output $x = \tfrac12 e_i + \tfrac12 e_k$, $y = e_j$.

- Pick $i = 1$. Column payoffs against row 1 are $C_{1\cdot} = (0, 1, 0.5)$, so $j = 2$.
- Row payoffs against column 2 are $R_{\cdot 2} = (0, 1, 0.3)$, so $k = 2$.
- Output $x = (\tfrac12, \tfrac12, 0)$, $y = (0,1,0)$.

**Verify the $1/2$ guarantee.**

Row player: $x^\top R y = \tfrac12 R_{12} + \tfrac12 R_{22} = \tfrac12(0) + \tfrac12(1) = 0.5$. Best response value is $\max_i (Ry)_i = \max(0,1,0.3) = 1$. Row regret $= 1 - 0.5 = 0.5$.

Column player: $x^\top C = \tfrac12(0,1,0.5) + \tfrac12(1,0,0.5) = (0.5, 0.5, 0.5)$. So $x^\top C y = 0.5$ and $\max_j (x^\top C)_j = 0.5$. Column regret $= 0$.

Hence $\max\{f,g\} = 0.5$: a $1/2$-NE, and the bound is tight here on the row side.

**Why the general proof gives exactly $1/2$.** Column regret is $0$ by construction: column $j$ is a best response to $e_i$, and against $e_k$ the column player's loss is at most $1$, so mixing halves it — formally, $(x^\top C)_j = \tfrac12 C_{ij} + \tfrac12 C_{kj} \ge \tfrac12 C_{ij'} + 0$ and $\max_{j'}(x^\top C)_{j'} \le \tfrac12 C_{ij'} + \tfrac12 \le (x^\top C)_j + \tfrac12$. Row regret: $x^\top R y = \tfrac12 R_{ij} + \tfrac12 R_{kj} \ge \tfrac12 R_{kj} = \tfrac12\max_l (Ry)_l$, and since $\max_l(Ry)_l \le 1$, the loss is at most $1/2$. Both bounds use only $R,C \in [0,1]$.

**What the record algorithm adds.** Tsaknakis–Spirakis instead minimize $\Phi(x,y) = \max\{f(x,y), g(x,y)\}$ by descent; at a stationary point where descent stalls, a case analysis shows $\Phi \le 0.3393$. DFM (2022) show that at the worst stalling configurations one can re-solve a small LP over the two-player supports and push the value to $1/3+\delta$. The example above has an exact NE at $x=y=(\tfrac12,\tfrac12,0)$-style symmetric mixtures; the hardness is not in any single game but in the fact that no known method controls $\Phi$ below $1/3$ *uniformly* over all $n\times n$ inputs — and by Feder–Nazerzadeh–Saberi, any method that searches over small supports must look at supports of size $\Omega(\log n)$, i.e. $n^{\Omega(\log n)}$ candidates.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*