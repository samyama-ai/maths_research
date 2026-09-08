---
id: 09-probability/beta-coalescent-tree-height-asymptotics
title: "Coalescent Processes with Multiple Mergers and Beta Coalescent Tree Heights"
topic: 09-probability
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Coalescent Processes with Multiple Mergers and Beta Coalescent Tree Heights

> **Topic:** Probability & Stochastic Processes · **ID:** `09-probability/beta-coalescent-tree-height-asymptotics` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Let $(\Pi^{(n)}_t)_{t\ge0}$ be the $\Lambda$-coalescent started from the partition of $\{1,\dots,n\}$ into singletons, with $\Lambda = \mathrm{Beta}(2-\alpha,\alpha)$, $\alpha\in(0,2)$. Let

$$T_n \;=\; \inf\{t\ge 0:\ |\Pi^{(n)}_t| = 1\}$$

be the **absorption time**, equal to the height of the associated coalescent tree (the time to the most recent common ancestor of the $n$ samples).

**Problem.** Determine, for every $\alpha \in (0,2)$, the complete first- and second-order asymptotics of $T_n$: centering sequences $b_n(\alpha)$, scaling sequences $a_n(\alpha)$, and the limit law $\mathcal{L}_\alpha$ with

$$\frac{T_n - b_n(\alpha)}{a_n(\alpha)} \;\xrightarrow{d}\; \mathcal{L}_\alpha ,$$

with $\mathcal{L}_\alpha$ non-degenerate, and establish that the map $\alpha \mapsto (a_n, b_n, \mathcal{L}_\alpha)$ is described uniformly across the three regimes $\alpha\in(0,1)$ (dust), $\alpha=1$ (Bolthausen–Sznitman), $\alpha\in(1,2)$ (comes down from infinity), including the boundary transitions $\alpha\uparrow 1$, $\alpha\downarrow 1$, $\alpha\uparrow 2$.

A complete solution requires: (i) a proof of a fluctuation limit theorem for $T_n$ for all $\alpha\in(1,2)$, where $T_n \uparrow T_\infty < \infty$ and the object of interest is the *residual* $T_\infty - T_n$; (ii) identification of the constant and limit law in the dust regime $\alpha\in(0,1)$; (iii) matching expansions at the three critical values. The status is **partially-solved**: (ii)-type first-order results and the $\alpha=1$ and $\alpha=2$ cases are settled; the fluctuation law for $1<\alpha<2$ is not.

## 2. Mathematical Foundations

**$\Lambda$-coalescents.** Let $\Lambda$ be a finite measure on $[0,1]$. The $\Lambda$-coalescent (Pitman 1999; Sagitov 1999) is the Markov process on partitions of $\mathbb{N}$ whose restriction to $\{1,\dots,n\}$ jumps, when there are $b$ blocks, by merging any given $k$ of them ($2\le k\le b$) at rate

$$\lambda_{b,k} \;=\; \int_0^1 x^{k-2}(1-x)^{b-k}\,\Lambda(dx).$$

Consistency under restriction holds because $\lambda_{b,k} = \lambda_{b+1,k} + \lambda_{b+1,k+1}$. The total merger rate from $b$ blocks is $\lambda_b = \sum_{k=2}^b \binom{b}{k}\lambda_{b,k}$, and the block-counting process $N^{(n)}_t = |\Pi^{(n)}_t|$ is a Markov chain on $\{1,\dots,n\}$ decreasing by $k-1$ at rate $\binom{b}{k}\lambda_{b,k}$.

**Beta family.** Take $\Lambda(dx) = \frac{x^{1-\alpha}(1-x)^{\alpha-1}}{B(2-\alpha,\alpha)}dx$, so $\Lambda([0,1])=1$. Then

$$\lambda_{b,k} \;=\; \frac{B(k-\alpha,\ b-k+\alpha)}{B(2-\alpha,\alpha)} .$$

$\alpha=2$ is the weak limit $\Lambda=\delta_0$, the **Kingman coalescent** (pairwise mergers at rate $1$); $\alpha=1$ gives $\Lambda=\mathrm{Unif}[0,1]$, the **Bolthausen–Sznitman coalescent** (Bolthausen–Sznitman 1998). Beta coalescents with $\alpha\in(1,2)$ arise as genealogies of supercritical Galton–Watson processes with offspring tail index $\alpha$ (Schweinsberg 2003) and as time-changed genealogies of $\alpha$-stable continuous-state branching processes.

**Coming down from infinity (CDI).** Schweinsberg's criterion (2000): the $\Lambda$-coalescent comes down from infinity iff $\sum_{b\ge2}\gamma_b^{-1}<\infty$ where $\gamma_b=\sum_{k=2}^b (k-1)\binom{b}{k}\lambda_{b,k}$. For Beta, CDI holds iff $\alpha\in(1,2)$. Dust (a positive fraction of singletons persists) occurs iff $\int_0^1 x^{-1}\Lambda(dx)<\infty$, i.e. $\alpha\in(0,1)$.

**Speed of CDI.** For $1<\alpha<2$, Berestycki–Berestycki–Limic (2010) proved $N_t \sim v(t)$ a.s. as $t\downarrow 0$ with

$$v(t) \;=\; \bigl(\alpha\Gamma(\alpha)\,t\bigr)^{-1/(\alpha-1)} .$$

Hence, with $T_\infty$ the absorption time from infinitely many blocks,

$$T_\infty - T_n \;\approx\; v^{-1}(n) \;=\; \frac{n^{1-\alpha}}{\alpha\Gamma(\alpha)} .$$

**Total length.** $L_n=\int_0^{T_n} N^{(n)}_t\,dt$ satisfies $n^{\alpha-2}L_n \to \frac{\alpha(\alpha-1)\Gamma(\alpha)}{2-\alpha}$ in probability for $1<\alpha<2$ (Berestycki–Berestycki–Schweinsberg 2007).

## 3. History & State of the Art (SOTA)

- **1982.** Kingman's coalescent; $\mathbb{E}[T_n]=2(1-1/n)$, $T_n\to T_\infty$ a.s.
- **1998–1999.** Bolthausen–Sznitman coalescent from Ruelle cascades; Pitman and Sagitov independently characterise all exchangeable multiple-merger coalescents by $\Lambda$.
- **2000.** Schweinsberg's necessary and sufficient CDI condition, splitting the Beta family at $\alpha=1$.
- **2003.** Schweinsberg derives Beta$(2-\alpha,\alpha)$ coalescents from heavy-tailed Galton–Watson genealogies, making $1<\alpha<2$ the biologically relevant window (sweepstakes reproduction).
- **2005.** Goldschmidt–Martin: the Bolthausen–Sznitman coalescent is the cutting of a random recursive tree; $T_n-\log\log n \Rightarrow$ Gumbel.
- **2007–2010.** Beta-coalescents linked to $\alpha$-stable continuous random trees (BBS 2007); exact CDI speed $v(t)$ (BBL 2010).
- **2008–2012.** Delmas–Dhersin–Siri-Jégousse compute length and $T_n$ asymptotics; Kersting obtains the $\alpha$-stable fluctuation law for $L_n$.
- **2015.** Limic–Talarczyk prove second-order (fluctuation) limits for the block-counting process $N_t$ in regularly varying $\Lambda$-coalescents — the closest existing tool for the height problem.
- **2014–2021.** Evolving/fixation-line viewpoints (Kersting–Schweinsberg–Wakolbinger; Hénard), external branch lengths (Diehl–Kersting), and the Kersting–Wakolbinger survey consolidate the field.

## 4. Partial Results / Verified Cases

| Regime | Result | Source |
|---|---|---|
| $\alpha=2$ (Kingman) | $T_n\to T_\infty$ a.s., $\mathbb{E}T_n=2(1-1/n)$; $n(T_\infty-T_n)\to2$ in $L^2$ and $n^{3/2}(T_\infty-T_n-2/n)\Rightarrow \mathcal{N}(0,4/3)$ | classical, direct sum of exponentials |
| $\alpha=1$ (Bolthausen–Sznitman) | $T_n-\log\log n \xrightarrow{d}$ standard Gumbel; number of collisions $\sim n/\log n$ | Goldschmidt–Martin 2005 |
| $1<\alpha<2$ | $T_n\uparrow T_\infty<\infty$ a.s.; $T_\infty-T_n \sim \frac{n^{1-\alpha}}{\alpha\Gamma(\alpha)}$ in probability (first order only) | BBL 2010; Delmas–Dhersin–Siri-Jégousse 2008 |
| $1<\alpha<2$, block counts | $N_t/v(t)\to1$ a.s.; second-order fluctuations of $N_t$ around $v(t)$ are $\alpha$-stable | Limic–Talarczyk 2015 |
| $1<\alpha<2$, length | $n^{\alpha-2}L_n\to \frac{\alpha(\alpha-1)\Gamma(\alpha)}{2-\alpha}$; fluctuations of $L_n$ are $(\alpha)$-stable after $n^{1/\alpha}$-type scaling | BBS 2007; Kersting 2012 |
| $0<\alpha<1$ (dust) | $T_n\to\infty$; no CDI; log-order growth established for classes of dust coalescents via the associated subordinator / Markov chain in the frequency of singletons | Möhle 2010 |
| $\alpha=1$ boundary | Block counting process of BS coalescent has Mittag-Leffler scaling limit, linking $\alpha\uparrow1$ and $\alpha\downarrow1$ regimes | Möhle 2010 and successors |

## 5. Principal Obstacles

- **The residual is a boundary functional, not a bulk one.** For $1<\alpha<2$, $T_\infty-T_n$ is determined by the coalescent's behaviour at the *very small time scale* $t\asymp n^{1-\alpha}$, where $N_t$ is large. Martingale CLTs that work for $L_n$ (an integral over the whole tree, dominated by many independent-ish small increments) do not apply: $T_\infty - T_n = \sum_{b>n}\text{(holding times)}$, and the holding times have heavy dependence through the jump chain of $N$.
- **Non-Markovian jump sizes.** The jump chain of $N^{(n)}$ has jumps $b\mapsto b-(k-1)$ with $\binom{b}{k}\lambda_{b,k}$ decaying like $k^{-1-\alpha}$, so jump sizes have infinite variance for $\alpha<2$. Renewal/regenerative arguments used at $\alpha=1$ (the recursive-tree cutting bijection) have no analogue for $\alpha\ne1$: the Bolthausen–Sznitman case is exactly solvable because of a combinatorial coincidence, not by a method that deforms in $\alpha$.
- **Failure of the flow-of-bridges linearisation.** The $\alpha$-stable CSBP time-change representation gives $T_\infty$ exactly, but the map from CSBP extinction to the *discrete* $n$-sample MRCA involves the sampling coupling, whose error is of the same order $n^{1-\alpha}$ as the quantity being estimated.
- **Non-uniformity at $\alpha\to2$.** The centering $n^{1-\alpha}/(\alpha\Gamma(\alpha))$ tends to $2/n$ as $\alpha\to2$ correctly, but the fluctuation scale changes from $n^{-3/2}$ (Gaussian, $\alpha=2$) to a stable regime; no known argument is uniform in $\alpha$ near $2$, because the fluctuation exponent and the limit family both degenerate.
- **Dust regime lacks a coupling.** For $\alpha<1$, $T_n$ is governed by a sequence of near-independent "almost-fixation" attempts; the natural subordinator representation gives moments but not tightness of the centered height.

## 6. The Gap

Proven: first-order law of large numbers for $T_n$ in every regime, plus an exact limit law only at $\alpha\in\{1,2\}$. Missing: for each fixed $\alpha\in(1,2)$, a sequence $a_n$ and a non-degenerate law $\mathcal{L}_\alpha$ with

$$a_n^{-1}\Bigl(T_\infty - T_n - \tfrac{n^{1-\alpha}}{\alpha\Gamma(\alpha)}\Bigr) \;\xrightarrow{d}\; \mathcal{L}_\alpha .$$

Heuristics from Limic–Talarczyk's stable fluctuations of $N_t$ suggest $a_n \asymp n^{1-\alpha}\cdot n^{-(\alpha-1)/\alpha}$ with $\mathcal{L}_\alpha$ an $\alpha$-stable law, but the required step — transferring a fluctuation theorem for the *state* $N_t$ at fixed $t$ into one for the *inverse* (hitting time of level $n$), uniformly over the whole descent from $\infty$ — has not been carried out. Formally: one needs a functional invariance principle for $(v(t)^{-1}N_t - 1)$ on the time interval $(0,\epsilon]$ strong enough to invert, plus control of the accumulated error from the $O(1)$ blocks at the end of the descent, where the diffusion approximation fails.

## 7. Current Research (as of June 2026)

- **Frankfurt / Munich school (Kersting, Wakolbinger and collaborators):** branch-length spectra of $\Lambda$-coalescents without dust; the natural next target is the internal-branch/height spectrum. Their survey (2021) explicitly lists the height fluctuation problem as open.
- **UCSD (Schweinsberg) and Oxford (Goldschmidt):** evolving coalescents and the process $n\mapsto T_n$ viewed as a stochastic process indexed by sample size; the evolving-beta-coalescent framework (2014) gives the correct topology for a functional limit.
- **Zagreb / Warsaw (Limic, Talarczyk):** extension of second-order block-counting asymptotics to the inverse process; *(frontier — verify)* preprints extending the 2015 result to hitting times of low levels are circulating.
- **Statistical genetics groups (Freund, Birkner, Blath):** simulation-based estimation of $\alpha$ from site-frequency spectra of Atlantic cod and Pacific oyster data depends on the constants in the height and length asymptotics; sharper second-order terms directly improve estimator bias. *(frontier — verify)*
- **CSBP/CRT route (Duquesne–Le Gall lineage):** encoding the Beta-coalescent tree by the height process of the $\alpha$-stable CRT, aiming to read $T_\infty-T_n$ off excursion theory.

## 8. Future Work

1. Prove a functional limit theorem for $\{(N_t - v(t))/\sigma(t)\}$ on shrinking time windows and invert it to obtain $\mathcal{L}_\alpha$.
2. Handle the boundary $\alpha\uparrow2$ by a triangular-array scheme in which $\alpha=\alpha_n\to2$, producing a crossover family interpolating $\alpha$-stable and Gaussian limits.
3. Settle the dust regime: identify $c(\alpha)$ with $T_n/\log n\to c(\alpha)$ for $0<\alpha<1$ and prove a Gumbel-type fluctuation theorem matching Goldschmidt–Martin at $\alpha=1$.
4. Compute joint limits of $(T_n, L_n)$ — currently even the correlation structure is unknown for $\alpha\in(1,2)$.
5. Extend beyond the Beta family to all regularly varying $\Lambda$ with $\Lambda(dx)\sim x^{1-\alpha}dx$ near $0$, and determine which asymptotics are universal in $\alpha$ alone.

## 9. Key References

- **[Foundational]** J. Pitman. *Coalescents with multiple collisions.* Annals of Probability 27(4), 1870–1902, 1999.
- **[Foundational]** S. Sagitov. *The general coalescent with asynchronous mergers of ancestral lines.* Journal of Applied Probability 36(4), 1116–1125, 1999.
- **[Foundational]** E. Bolthausen, A.-S. Sznitman. *On Ruelle's probability cascades and an abstract cavity method.* Communications in Mathematical Physics 197, 247–276, 1998.
- **[Foundational]** J. Schweinsberg. *A necessary and sufficient condition for the Λ-coalescent to come down from infinity.* Electronic Communications in Probability 5, 1–11, 2000.
- **[Foundational]** J. Schweinsberg. *Coalescent processes obtained from supercritical Galton–Watson processes.* Stochastic Processes and their Applications 106(1), 107–139, 2003.
- **[SOTA]** C. Goldschmidt, J. B. Martin. *Random recursive trees and the Bolthausen–Sznitman coalescent.* Electronic Journal of Probability 10, 718–745, 2005.
- **[SOTA]** J. Berestycki, N. Berestycki, J. Schweinsberg. *Beta-coalescents and continuous stable random trees.* Annals of Probability 35(5), 1835–1887, 2007.
- **[SOTA]** J.-F. Delmas, J.-S. Dhersin, A. Siri-Jégousse. *Asymptotic results on the length of coalescent trees.* Annals of Applied Probability 18(2), 997–1025, 2008.
- **[SOTA]** J. Berestycki, N. Berestycki, V. Limic. *The Λ-coalescent speed of coming down from infinity.* Annals of Probability 38(1), 207–233, 2010.
- **[SOTA]** M. Möhle. *Asymptotic results for coalescent processes without proper frequencies and applications to the two-parameter Poisson–Dirichlet coalescent.* Stochastic Processes and their Applications 120(11), 2159–2173, 2010.
- **[SOTA]** G. Kersting. *The asymptotic distribution of the length of Beta-coalescent trees.* Annals of Applied Probability 22(5), 2086–2107, 2012.
- **[SOTA]** G. Kersting, J. Schweinsberg, A. Wakolbinger. *The evolving beta coalescent.* Electronic Journal of Probability 19, paper 64, 2014.
- **[SOTA]** V. Limic, A. Talarczyk. *Second-order asymptotics for the block counting process in a class of regularly varying Λ-coalescents.* Annals of Probability 43(3), 1419–1455, 2015.
- **[SOTA]** O. Hénard. *The fixation line in the Λ-coalescent.* Annals of Applied Probability 25(5), 3007–3032, 2015.
- **[Recent]** J. Diehl, G. Kersting. *External branch lengths of Λ-coalescents without a dust component.* Electronic Journal of Probability 24, paper 134, 2019.
- **[Survey]** N. Berestycki. *Recent progress in coalescent theory.* Ensaios Matemáticos 16, 1–193, 2009.
- **[Survey]** G. Kersting, A. Wakolbinger. *Probabilistic aspects of Λ-coalescents in equilibrium and in evolution.* In *Probabilistic Structures in Evolution*, EMS Press, 2021.

## 10. Worked Example / Concrete Special Case

**(a) $\alpha=3/2$, $n=3$: exact height.** Here $B(2-\alpha,\alpha)=B(\tfrac12,\tfrac32)=\pi/2$. Since $\lambda_{b,b}=\int_0^1 x^{b-2}\Lambda(dx)$, we get for $b=3$:

$$\lambda_{3,3}=\mathbb{E}[X]=\frac{2-\alpha}{2}=\frac14,\qquad \lambda_{3,2}=\int_0^1(1-x)\Lambda(dx)=1-\frac14=\frac34,\qquad \lambda_{2,2}=\Lambda([0,1])=1.$$

Total rate out of $3$ blocks: $\binom32\lambda_{3,2}+\binom33\lambda_{3,3}=3\cdot\tfrac34+\tfrac14=\tfrac52$. The triple merger takes probability $\tfrac{1/4}{5/2}=\tfrac1{10}$. Hence

$$\mathbb{E}[T_3]=\frac{1}{5/2}+\frac{9}{10}\cdot\frac{1}{1}=0.4+0.9=1.3 .$$

Compare Kingman ($\alpha=2$): $\mathbb{E}[T_3]=\tfrac13+1=\tfrac43\approx1.333$. Multiple mergers shorten the tree even at $n=3$.

**(b) $\alpha=2$: the fluctuation computation the problem asks for.** With Kingman rates, the time to descend from $\infty$ to $n$ blocks is $R_n=T_\infty-T_n=\sum_{k>n}E_k$, $E_k\sim\mathrm{Exp}\bigl(\binom k2\bigr)$ independent. Then

$$\mathbb{E}[R_n]=\sum_{k>n}\frac{2}{k(k-1)}=\frac2n,\qquad \mathrm{Var}(R_n)=\sum_{k>n}\frac{4}{k^2(k-1)^2}\sim\frac{4}{3n^3}.$$

Lindeberg applies (the summands are uniformly small relative to $n^{-3/2}$), giving

$$n^{3/2}\Bigl(R_n-\frac2n\Bigr)\;\xrightarrow{d}\;\mathcal{N}\!\left(0,\tfrac43\right).$$

**(c) What breaks for $1<\alpha<2$.** The same decomposition gives $R_n=\sum_{j\ge1}\mathcal{E}_j/\lambda_{B_j}$ where $B_1=\infty>B_2>\dots$ is the jump chain. Now the descent is not by unit steps: from $b$ blocks the chain jumps down by $k-1$ with $\binom{b}{k}\lambda_{b,k}\propto b\,k^{-1-\alpha}$ for $k\ll b$, so the step distribution is in the domain of attraction of an $\alpha$-stable law and $\mathrm{Var}$ is infinite. The mean of $R_n$ still gives $\frac{n^{1-\alpha}}{\alpha\Gamma(\alpha)}$, matching $2/n$ at $\alpha=2$, but the variance computation above has no analogue: the centred sum is conjecturally $\alpha$-stable at scale $n^{1-\alpha-\frac{\alpha-1}{\alpha}}$, and proving this — including the randomness of the levels $B_j$ actually visited — is exactly the open step of Section 6.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*