---
id: 09-probability/phase-transition-of-the-random-k-sat-problem
title: "Phase Transition of the Random k-SAT Problem"
topic: 09-probability
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Phase Transition of the Random k-SAT Problem

> **Topic:** Probability & Stochastic Processes · **ID:** `09-probability/phase-transition-of-the-random-k-sat-problem` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Let $\Phi_k(n,m)$ be a Boolean formula in conjunctive normal form on $n$ variables $x_1,\dots,x_n$, built by drawing $m$ clauses independently and uniformly from the $2^k\binom{n}{k}$ possible clauses of exactly $k$ distinct literals. Write $m=\lfloor rn\rfloor$, so $r$ is the **clause density**.

**Satisfiability Conjecture.** For every $k\ge 3$ there is a constant $r_k\in(0,\infty)$ such that for all $\varepsilon>0$,
$$\lim_{n\to\infty}\Pr\big[\Phi_k(n,\lfloor rn\rfloor)\ \text{is satisfiable}\big]=\begin{cases}1,& r<r_k-\varepsilon,\\[2pt] 0,& r>r_k+\varepsilon.\end{cases}$$

A complete resolution requires: (i) existence of the limit $r_k$ for every $k\ge 3$ (open for $k=3,4$ and all $k$ below an unspecified large constant $k_0$); (ii) identification of $r_k$ with the one-step replica symmetry breaking (1RSB) variational formula predicted by statistical physics; and (iii) a description of the associated phase diagram (clustering, condensation, freezing) and of the finite-size scaling window around $r_k$. Disproof would consist of showing the satisfiability probability does *not* have a sharp threshold at a fixed density for some $k\ge3$, or that the limiting value differs from the 1RSB prediction.

## 2. Mathematical Foundations

**Probability space.** $\Omega_{n,m}=(\mathcal{C}_{k,n})^m$ with the uniform product measure, $\mathcal{C}_{k,n}$ the set of $k$-clauses. The *Poissonized* model $\Phi_k(n,\mathrm{Poi}(rn))$ is contiguous for threshold purposes.

**Partition function.** Let $Z(\Phi)=\\#\{\sigma\in\{0,1\}^n:\ \Phi(\sigma)=1\}$. Then
$$\mathbb{E}\,Z=2^n\left(1-2^{-k}\right)^{m},\qquad \tfrac1n\log\mathbb{E}Z \to \log 2 + r\log\!\left(1-2^{-k}\right),$$
which vanishes at the **first-moment bound**
$$r_k\ \le\ r_k^{\mathrm{fm}}=-\frac{\log 2}{\log(1-2^{-k})}=2^k\log 2-\tfrac{\log 2}{2}+O(2^{-k}).$$

**Second moment.** With $\sigma,\tau$ at overlap $\rho=\frac1n|\{i:\sigma_i=\tau_i\}|$,
$$\mathbb{E}\,Z^2=\sum_{\rho}\binom{n}{\rho n}\Big(1-2^{1-k}+2^{-k}\big(\rho^k+(1-\rho)^k\big)\Big)^{m},$$
and $\mathbb{E}Z^2 = O\big((\mathbb{E}Z)^2\big)$ iff the exponent is maximized at $\rho=1/2$. Paley–Zygmund then gives $\Pr[Z>0]=\Omega(1)$, upgraded to $1-o(1)$ by Friedgut's sharp-threshold theorem.

**Sharp threshold (Friedgut 1999).** There exists a sequence $r_k(n)$ with
$$\Pr[\Phi_k(n,(r_k(n)\pm\varepsilon)n)\ \text{SAT}]\to 1\ \text{resp.}\ 0 .$$
Monotone, symmetric graph properties without a "local" cause have coarse-to-sharp dichotomies; $k$-SAT for $k\ge 3$ has no local obstruction, so the threshold is sharp *as a sequence*. Convergence of $r_k(n)$ is precisely what remains open for small $k$.

**Belief propagation / 1RSB.** The physics prediction encodes solutions as fixed points of the survey-propagation recursion on the factor graph. Let $\mu$ be a distribution over messages in $[0,1]$; the Bethe free energy is
$$\mathcal{F}(\mu)=\mathbb{E}\log\Big(\text{var-term}\Big)-r(k-1)\,\mathbb{E}\log\Big(\text{edge-term}\Big)+r\,\mathbb{E}\log\Big(\text{clause-term}\Big),$$
and $r_k$ is conjectured to be the density at which the *condensation* free energy $\sup_\mu\mathcal{F}(\mu)$ drops below $0$. Mézard–Parisi–Zecchina (2002) computed this numerically; Ding–Sly–Sun (2022) proved it rigorously for large $k$.

**Interpolation.** Guerra-type interpolation (Franz–Leone 2003) shows $\frac1n\mathbb{E}\log Z$ converges and that 1RSB expressions are valid *bounds*; subadditivity gives existence of $\lim_n \frac1n\mathbb{E}\log Z$ but not of $r_k(n)$, since $\log Z=-\infty$ on the UNSAT event.

## 3. History & State of the Art (SOTA)

- **1992.** Chvátal–Reed, and independently Goerdt, prove $r_2=1$ exactly.
- **1994.** Kirkpatrick–Selman report numerics for $k=3$: threshold near $4.2$, with critical-exponent behaviour resembling a physical phase transition; "easy–hard–easy" algorithmic profile.
- **1999.** Friedgut proves sharpness of the (possibly non-convergent) threshold sequence, the single most-used structural theorem in the area.
- **2001.** Bollobás–Borgs–Chayes–Kim–Wilson determine the 2-SAT scaling window: width $\Theta(n^{-1/3})$ around $r=1$.
- **2002.** Mézard–Parisi–Zecchina apply the cavity method: $r_3\approx 4.267$, $r_4\approx 9.93$, $r_5\approx 21.12$, $r_7\approx 87.79$; introduce survey propagation, which solves $n=10^6$ instances near threshold.
- **2004.** Achlioptas–Peres: weighted second moment gives $r_k\ge 2^k\log2-\tfrac{(k+1)\log 2}{2}-1-o_k(1)$, matching the first-moment upper bound to within $O(k)$.
- **2014–2016.** Coja-Oghlan–Panagiotou pin the asymptotics: $r_k=2^k\log 2-\tfrac{1+\log 2}{2}+\varepsilon_k$, $\varepsilon_k\to0$.
- **2015/2022.** Ding–Sly–Sun prove the Satisfiability Conjecture for all $k\ge k_0$, with $r_k$ given by an explicit 1RSB formula. This is the SOTA.
- **2021–2022.** Bresler–Huang establish the algorithmic barrier at $(1+o_k(1))\,2^k\log k/k$ for low-degree polynomial algorithms, matching Coja-Oghlan's Fix algorithm.

## 4. Partial Results / Verified Cases

| Case | Result |
|---|---|
| $k=2$ | Threshold $r_2=1$ proven (Chvátal–Reed 1992; Goerdt 1996; Fernandez de la Vega). Scaling window $n^{-1/3}$ (BBCKW 2001). |
| $k=3$ | Not proven. Best rigorous interval $3.52\le r_3(n)\le 4.4898$ for large $n$. Lower bound: Hajiaghayi–Sorkin (2003) and Kaporis–Kirousis–Lalas (2006), via analysis of greedy/myopic algorithms. Upper bound: Díaz–Kirousis–Mitsche–Pérez-Giménez (2009), first-moment over "locally maximal" assignments. Predicted $r_3\approx 4.26675$. |
| $k=4$ | $\approx 7.91 \le r_4 \le 10.217$; predicted $\approx 9.931$. |
| $k\ge k_0$ (large, unspecified, certainly $>3$) | **Fully solved.** Ding–Sly–Sun (Annals of Math., 2022): $r_k$ exists and equals the explicit 1RSB condensation formula. |
| All $k\ge3$ | Threshold *sequence* $r_k(n)$ is sharp (Friedgut 1999). Asymptotic value known to $o_k(1)$: $r_k=2^k\log2-\frac{1+\log 2}{2}+o_k(1)$ (Coja-Oghlan–Panagiotou 2016). |
| Clustering / shattering | For $k\ge 8$, the solution space shatters into exponentially many clusters for $r\ge (1+o_k(1))2^k\log k/k$ (Achlioptas–Coja-Oghlan 2008; Mézard–Mora–Zecchina 2005). |
| Regular NAE-SAT | Threshold proven exactly for large $k$ (Ding–Sly–Sun, *Comm. Math. Phys.* 2016). |
| Algorithms | Poly-time algorithms succeed up to $(1-o_k(1))2^k\log k/k$ (Coja-Oghlan's Fix, 2010) — a factor $\Theta(k/\log k)$ below $r_k$. |

## 5. Principal Obstacles

- **Second-moment failure.** For $k=3,4$ the overlap profile of $\mathbb{E}Z^2$ is maximized away from $\rho=1/2$ at densities well below the conjectured threshold, so $\mathbb{E}Z^2/(\mathbb{E}Z)^2$ is exponentially large. The obstruction is real, not technical: **condensation** means $Z$ is dominated by $O(1)$ clusters and is not concentrated, so $Z$ is genuinely non-Gaussian near $r_k$. Reweighting fixes this only when $k$ is large enough that the entropy term dominates the fluctuation term.
- **No monotone coupling in $k$.** Nothing transfers a proof for large $k$ down to $k=3$; the $k$-dependence enters through $2^{-k}$ corrections that are $O(1)$ when $k=3$.
- **Friedgut's theorem gives no location.** Sharpness is proven by a Bourgain-type "no local booster" argument that is entirely non-constructive about the value of $r_k(n)$, and does not preclude oscillation of $r_k(n)$ in $n$.
- **Free energy is $-\infty$ in the UNSAT phase.** Standard interpolation and subadditivity arguments control $\frac1n\mathbb{E}\log Z$ only where $Z>0$ whp; the threshold is exactly where those tools break.
- **Small-graph conditioning is delicate.** Cycle counts on the factor graph contribute $\Theta(1)$ multiplicative corrections; conditioning on them is required and the resulting product over cycle lengths converges only under fine estimates that degrade for small $k$.
- **Algorithmic barrier.** The overlap gap property (Gamarnik–Sudan) shows that stable/local algorithms cannot reach $r_k$, so no algorithmic lower-bound technique will close the gap by itself.

## 6. The Gap

Proven: existence and exact value of $r_k$ for $k\ge k_0$; sharpness of $r_k(n)$ for all $k\ge3$; $r_2=1$. Conjectured: existence of $\lim_n r_k(n)$ for $3\le k<k_0$, and its identification with the 1RSB formula (e.g. $r_3=4.26675\ldots$).

The precise missing step is a **non-asymptotic control of the condensation regime at small $k$**: one must show that the number of clusters, and the free energy of the dominant cluster, concentrate well enough that a truncated/weighted second-moment computation on cluster representatives succeeds when $2^{-k}$ is not small. Ding–Sly–Sun's proof needs $k$ large in two places — the contraction of the survey-propagation recursion in a suitable metric, and the error control in the small-subgraph conditioning — and both are quantitatively far from $k=3$. Equivalently: an explicit, effective $k_0$ has never been extracted, and even an effective $k_0=10^{6}$ would leave $k\in\{3,\dots,k_0\}$ untouched by any current method.

## 7. Current Research (as of June 2026)

- **Small-$k$ program.** Groups around Coja-Oghlan (Dortmund/TU Wien), Sly (Princeton), Sun (Columbia/CUHK) pursue effective versions of the 1RSB analysis, aiming to extract a concrete $k_0$. Reported progress is on regular and NAE variants first. *(frontier — verify)*
- **Sharp thresholds via spatial coupling and Nishimori-type symmetry**, extending Coja-Oghlan–Krzakala–Perkins–Zdeborová's "information-theoretic thresholds from the cavity method" (STOC 2017) to non-symmetric models.
- **Algorithmic phase transition.** Post-Bresler–Huang work extends low-degree and OGP lower bounds to stochastic local search and to random $k$-XORSAT/$k$-NAE-SAT; hardness for Glauber-type dynamics above the clustering threshold.
- **Scaling window and finite-size corrections.** No rigorous window is known for $k\ge3$; numerics suggest width $n^{-1/\nu}$ with $\nu$ near $1.5$–$2$, inconsistent with the 2-SAT exponent. *(frontier — verify)*
- **Proof-complexity crossover.** Resolution lower bounds for random $k$-SAT slightly above $r_k$ (Feige–Kim–Ofek style refutation) and the "refutation gap" at density $n^{k/2-1}$ remain active.

## 8. Future Work

1. Extract an explicit $k_0$ from Ding–Sly–Sun; even $k_0$ astronomically large would convert a qualitative theorem into a quantitative one.
2. Develop a "cluster second moment": apply the second moment to a partition function over *cluster representatives* (frozen-variable configurations) rather than assignments, removing the condensation obstruction at its source.
3. Prove convergence of $r_k(n)$ without identifying its value — a genuinely weaker statement that is still open for $k=3$ and might yield to a subadditivity/interpolation argument on a smoothed model.
4. Establish the scaling window for $k=3$ and determine whether the transition is discontinuous in the order parameter (overlap) while continuous in the SAT probability.
5. Close the algorithmic gap in the negative direction: prove NP-hardness-type or unconditional lower bounds for all polynomial algorithms in $(2^k\log k/k,\,2^k\log 2)$.

## 9. Key References

- **[Foundational]** V. Chvátal, B. Reed. *Mick gets some (the odds are on his side).* Proc. 33rd IEEE FOCS, 1992, 620–627.
- **[Foundational]** E. Friedgut (appendix by J. Bourgain). *Sharp thresholds of graph properties, and the $k$-SAT problem.* Journal of the AMS 12(4), 1999, 1017–1054.
- **[Foundational]** M. Mézard, G. Parisi, R. Zecchina. *Analytic and algorithmic solution of random satisfiability problems.* Science 297, 2002, 812–815.
- **[SOTA]** J. Ding, A. Sly, N. Sun. *Proof of the satisfiability conjecture for large $k$.* Annals of Mathematics 196(1), 2022, 1–388. (Extended abstract: STOC 2015.)
- **[SOTA]** A. Coja-Oghlan, K. Panagiotou. *The asymptotic $k$-SAT threshold.* Advances in Mathematics 288, 2016, 985–1068.
- **[SOTA]** D. Achlioptas, Y. Peres. *The threshold for random $k$-SAT is $2^k\log 2 - O(k)$.* Journal of the AMS 17(4), 2004, 947–973.
- **[SOTA]** G. Bresler, B. Huang. *The algorithmic phase transition of random $k$-SAT for low degree polynomials.* Proc. 62nd IEEE FOCS, 2021, 298–309.
- **[Bounds]** J. Díaz, L. Kirousis, D. Mitsche, X. Pérez-Giménez. *On the satisfiability threshold of formulas with three literals per clause.* Theoretical Computer Science 410(30–32), 2009, 2920–2934.
- **[Bounds]** A. Kaporis, L. Kirousis, E. Lalas. *The probabilistic analysis of a greedy satisfiability algorithm.* Random Structures & Algorithms 28(4), 2006, 444–480.
- **[Structure]** D. Achlioptas, A. Coja-Oghlan. *Algorithmic barriers from phase transitions.* Proc. 49th IEEE FOCS, 2008, 793–802.
- **[Structure]** B. Bollobás, C. Borgs, J. T. Chayes, J. H. Kim, D. B. Wilson. *The scaling window of the 2-SAT transition.* Random Structures & Algorithms 18(3), 2001, 201–256.
- **[Survey]** M. Mézard, A. Montanari. *Information, Physics, and Computation.* Oxford University Press, 2009.
- **[Survey]** A. Coja-Oghlan. *Phase transitions in discrete structures.* Proceedings of the European Congress of Mathematics, 2016.
- **[Survey]** D. Gamarnik. *The overlap gap property: a topological barrier to optimizing over random structures.* PNAS 118(41), 2021.

## 10. Worked Example / Concrete Special Case

**First-moment upper bound for $k=3$.** A uniform random 3-clause is falsified by a fixed $\sigma$ with probability $2^{-3}=1/8$, so it is satisfied with probability $7/8$, independently across clauses. Hence
$$\mathbb{E}Z=2^{n}\left(\tfrac78\right)^{rn}=\exp\!\Big(n\big[\log 2+r\log\tfrac78\big]\Big).$$
Markov's inequality gives $\Pr[Z\ge1]\le\mathbb{E}Z$, so the formula is unsatisfiable whp once $\log 2 + r\log(7/8)<0$, i.e.
$$r>\frac{\log 2}{\log(8/7)}=\frac{0.693147}{0.133531}=5.1910\ldots$$
So $r_3\le 5.191$ — already within $22\%$ of the predicted $4.2667$, from two lines.

**Why this is loose, and how it is tightened.** $Z$ is inflated by clusters of near-identical solutions. Díaz et al. count only *locally maximal* assignments: $\sigma$ such that flipping any single variable $0\to1$ breaks a clause. Each satisfying $\sigma$ has at least one such representative, so the count $Z^{\mathrm{lm}}\ge \mathbf{1}[Z>0]$, while $\mathbb{E}Z^{\mathrm{lm}}$ is exponentially smaller than $\mathbb{E}Z$ because each variable set to $0$ must occur as the unique true literal of some clause. Optimizing the resulting large-deviations rate function gives $r_3\le 4.4898$.

**The other side.** Take $r=3.52$. Run a myopic greedy rule that repeatedly picks a variable of maximum degree in the remaining clauses and sets it to satisfy the majority of its occurrences, simplifying after each step. Tracking the clause-length profile $(C_1(t),C_2(t),C_3(t))$ by Wormald's differential-equation method shows the unit-clause density $C_1(t)/n$ stays below the critical value that would trigger a contradiction, so the algorithm outputs a satisfying assignment whp. This yields $r_3\ge 3.52$. The interval $[3.52,\,4.4898]$ is where the conjecture $r_3=4.26675$ lives, and no current technique enters it.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*