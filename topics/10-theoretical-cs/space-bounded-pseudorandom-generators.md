---
id: 10-theoretical-cs/space-bounded-pseudorandom-generators
title: "Space Bounded Pseudorandom Generators"
topic: 10-theoretical-cs
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Space Bounded Pseudorandom Generators

> **Topic:** Theoretical Computer Science · **ID:** `10-theoretical-cs/space-bounded-pseudorandom-generators` · **Status:** open

## 1. Problem Statement / Conjecture

Construct an explicit pseudorandom generator (PRG) with seed length $O(\log n)$ that fools polynomial-width, length-$n$ read-once branching programs (ROBPs) with constant error.

**Main conjecture.** For every constant $c$ there is a function $G:\{0,1\}^{O(\log n)}\to\{0,1\}^n$, computable in space $O(\log n)$, such that for every ROBP $B$ of length $n$ and width $w=n^c$,
$$\Big|\ \Pr_{s\sim U_{O(\log n)}}[B(G(s))=1]\ -\ \Pr_{x\sim U_n}[B(x)=1]\ \Big|\ \le\ 1/10 .$$

Such a $G$ implies $\mathbf{BPL}=\mathbf{L}$ (and $\mathbf{BPSPACE}(S)=\mathbf{DSPACE}(S)$ for $S\ge\log n$) by enumerating all $\mathrm{poly}(n)$ seeds. A complete resolution is either (i) an explicit construction meeting the $O(\log n)$ bound, or (ii) a proof that no logspace-computable generator with seed $o(\log^2 n)$ can fool this class — an unconditional lower bound against all explicit constructions, which no current technique can supply. The counting argument shows non-explicit generators with seed $O(\log(nw/\varepsilon))$ exist, so the entire difficulty is explicitness.

Nisan's 1992 generator, with seed $O(\log^2 n)$, remains the best known for the full class after 34 years.

## 2. Mathematical Foundations

**Read-once branching program.** A $(n,w)$-ROBP is a layered DAG with layers $V_0,\dots,V_n$, $|V_i|\le w$, a start vertex $v_0\in V_0$, an accepting set $V_n^{acc}\subseteq V_n$, and edge maps $\delta_i:V_{i-1}\times\{0,1\}\to V_i$. On input $x\in\{0,1\}^n$ it walks $v_i=\delta_i(v_{i-1},x_i)$ and accepts iff $v_n\in V_n^{acc}$. Equivalently, layer $i$ is a pair of $w\times w$ stochastic transition matrices $M_i^0,M_i^1$, and
$$\Pr_{x\sim U_n}[B(x)=1]=e_{v_0}^{\top}\Big(\prod_{i=1}^{n}\tfrac{1}{2}(M_i^{0}+M_i^{1})\Big)\mathbf{1}_{V_n^{acc}} .$$
A space-$S$ randomized machine reading $2^{O(S)}$ random bits once is exactly an ROBP of width $w=2^{O(S)}$; $S=O(\log n)$ gives $w=\mathrm{poly}(n)$.

**Fooling.** $G$ $\varepsilon$-fools a class $\mathcal{C}$ if $|\mathbb{E}[B(G(U_d))]-\mathbb{E}[B(U_n)]|\le\varepsilon$ for all $B\in\mathcal{C}$. A *hitting set generator* (HSG) only guarantees: if $\Pr[B(U_n)=1]>\varepsilon$ then $B(G(s))=1$ for some $s$. A *weighted PRG* (WPRG, or pseudorandom pseudodistribution) is a pair $(G,\rho)$ with $\rho:\{0,1\}^d\to\mathbb{R}$ such that
$$\Big|\ \mathbb{E}_{s}\big[\rho(s)\,B(G(s))\big]-\mathbb{E}[B(U_n)]\Big|\le\varepsilon ,$$
which still suffices for derandomization but escapes some PRG lower bounds.

**Special subclasses.** $B$ is *regular* if every vertex in $V_i$ ($i\ge1$) has in-degree exactly $2$; it is a *permutation* program if each $M_i^b$ is a permutation matrix. Width $2$, width $3$, regular, permutation, and unknown-order variants are the standard stratification.

**Nisan's generator.** With $k=\log n$ levels, pairwise-independent hash families $h_1,\dots,h_k:\{0,1\}^m\to\{0,1\}^m$,
$$G_0(x)=x,\qquad G_j(x,h_1,\dots,h_j)=\big(G_{j-1}(x,h_{<j}),\,G_{j-1}(h_j(x),h_{<j})\big),$$
giving seed $m+k\cdot O(m)=O(\log n\log(nw/\varepsilon))=O(\log^2 n)$. The INW variant replaces hashes by expander walks: if $H$ is a $\lambda$-spectral-expander of degree $2^d$, the recursion costs $d=O(\log(w/\varepsilon'))$ extra bits per level.

## 3. History & State of the Art (SOTA)

- **1990–92.** Babai–Nisan–Szegedy and then Nisan (*Combinatorica*, 1992) gave the $O(\log^2 n)$-seed generator for $\mathrm{poly}(n)$-width ROBPs — still SOTA for the general class.
- **1994.** Impagliazzo–Nisan–Wigderson (STOC) reproved it via expander/extractor recursion (INW), the form used in almost all later work.
- **1996.** Nisan–Zuckerman (*JCSS*): "randomness is linear in space" — space-$S$ machines running in time $\mathrm{poly}(S)$ need only $O(S)$ random bits; i.e. seed $O(\log n)$ when $n=\mathrm{polylog}$.
- **1999.** Saks–Zhou (*JCSS*): $\mathbf{BPSPACE}(S)\subseteq\mathbf{DSPACE}(S^{3/2})$, hence $\mathbf{BPL}\subseteq\mathbf{DSPACE}(\log^{1.5}n)$, by a shift-and-truncate recycling of Nisan's generator. Not improved for 22 years.
- **2008.** Reingold (*JACM*): undirected $s$–$t$ connectivity in logspace, $\mathbf{SL}=\mathbf{L}$ — a full derandomization of the flagship $\mathbf{RL}$ problem without a PRG.
- **2010s.** Structural restrictions fall: regular programs (Braverman–Rao–Raz–Yehudayoff), permutation programs (Koucký–Nimbhorkar–Pudlák; Steinke), width 2 (Bogdanov–Dvir–Verbin–Yehudayoff), width 3 (Meka–Reingold–Tal, 2019), arbitrary-order ROBPs of small width (Forbes–Kelley, 2018).
- **2018–2021.** The WPRG era: Braverman–Cohen–Garg achieve seed $\tilde{O}(\log^2 n+\log(1/\varepsilon))$ — breaking Nisan's $\log n\cdot\log(1/\varepsilon)$ error dependence — refined by Chattopadhyay–Liao to $O(\log^2 n+\log(1/\varepsilon)\log\log(1/\varepsilon))$. Hoza (2021) turns this into $\mathbf{BPL}\subseteq\mathbf{DSPACE}\big(\log^{3/2}n/\sqrt{\log\log n}\big)$, the first improvement on Saks–Zhou.
- **2020.** Ahmadinejad–Kelner–Murtagh–Peebles–Sidford–Vadhan: high-precision random-walk estimation for Eulerian digraphs in space $\tilde O(\log n)$, importing spectral sparsification and Laplacian solvers into the space-bounded toolkit.

## 4. Partial Results / Verified Cases

| Class | Seed length | Source |
|---|---|---|
| Width $w=2$, length $n$, error $\varepsilon$ | $O(\log(n/\varepsilon))$ — optimal | Bogdanov–Dvir–Verbin–Yehudayoff, 2013 |
| Width $w=3$ | $\tilde O(\log n)$ for constant $\varepsilon$ | Meka–Reingold–Tal, 2019 |
| Regular, width $w$ | $O(\log n\,(\log\log n+\log(w/\varepsilon)))$ | Braverman–Rao–Raz–Yehudayoff, 2014 |
| Permutation / group products, constant width | $O(\log n\log(1/\varepsilon))$ | Koucký–Nimbhorkar–Pudlák, 2011 |
| Unknown-order ROBP, width $w$ | $\tilde O(\log^3 n)$ (poly width), $O(\log^2 n)$ for $w=O(1)$ | Forbes–Kelley, 2018 |
| Time-$\mathrm{poly}(S)$ space-$S$ machines ($n=S^{O(1)}$) | $O(S)$ — optimal | Nisan–Zuckerman, 1996 |
| Poly-width, general, WPRG | $\tilde O(\log^2 n+\log(1/\varepsilon))$ | Braverman–Cohen–Garg, 2020 |
| Poly-width HSG, small threshold $\varepsilon$ | $O(\log n)$ as $\varepsilon\to$ exponentially small | Hoza–Zuckerman, 2020 |
| Undirected / Eulerian connectivity | space $O(\log n)$, $\tilde O(\log n)$ | Reingold 2008; Ahmadinejad et al. 2020 |

Also verified: $\mathbf{RL}\subseteq\mathbf{SC}$ (Nisan, 1994); Cheng–Hoza (2020) show an optimal HSG for poly-width ROBPs *implies* $\mathbf{BPL}=\mathbf{L}$, so one-sided and two-sided derandomization are equivalent at this granularity.

## 5. Principal Obstacles

- **Hybrid/error accumulation.** Every recursive construction (Nisan, INW) pays $\varepsilon'$ error per level over $\log n$ levels against $w$ states, forcing $\varepsilon'\approx\varepsilon/(nw)$, hence $\Omega(\log(nw/\varepsilon))$ bits *per level* and $\Theta(\log^2 n)$ total. No known analysis makes the per-level cost $o(\log n)$ amortized.
- **Fourier methods cap out.** Polynomial-approximation and small-bias arguments that fool $\mathbf{AC}^0$ or low-degree $\mathbb{F}_2$ polynomials do not apply: poly-width ROBPs compute functions with large high-order Fourier mass (e.g. inner product mod 2 is width $2$ but $\mathrm{IP}$-like tests on general programs need full spectral control), so bounded independence provably fails — $O(1)$-wise, even $n^{0.99}$-wise independence does not fool width-$4$ programs in general.
- **Loss of regularity.** The successful subclass results exploit *structure*: regularity gives a doubly stochastic transition operator with a spectral gap argument (weight per vertex is preserved); general programs have "sink-heavy" layers where a single vertex absorbs mass and the potential-function/expander mixing analysis collapses.
- **Width 3 is already the wall.** MRT's width-$3$ proof is a delicate case analysis of Markov chains with three states; even width $4$ resists, showing the difficulty is not asymptotic but combinatorial.
- **No hardness-to-randomness engine.** In the time-bounded setting Nisan–Wigderson converts circuit lower bounds into PRGs. For space, a comparable engine needs a hard function *computable in small space* fooling small-space distinguishers, and $\mathbf{L}$-vs-$\mathbf{P}$-style lower bounds of that strength are unknown; recent "certified hardness vs. randomness" (Pyne–Raz–Zhan, 2023) gets conditional statements only.
- **Barriers to lower bounds.** No unconditional $\omega(\log n)$ seed lower bound is known for any explicit-generator model, so one cannot even rule out that Nisan's generator itself has a $O(\log n)$-seed variant.

## 6. The Gap

Proven: $O(\log^2 n)$ seed for the full class (Nisan/INW), and $O(\log n)$-type seeds only under structural hypotheses (width $\le3$, regularity, permutation) or in relaxed models (WPRGs, hitting sets at tiny thresholds, $\tilde O(\log^2 n)$ error dependence). Conjectured: $O(\log n)$ for width $\mathrm{poly}(n)$, constant error.

The precise gap is a factor of $\log n$ arising from the hybrid argument: one must show that a *single* seed can be reused across all $\log n$ recursion levels, or that the accumulated error over $n$ layers is $O(\varepsilon)$ rather than $n\varepsilon'$. Concretely: eliminate the per-level $\Omega(\log(w/\varepsilon))$ expander-degree charge in the INW recursion for *irregular* programs. Equivalently (Cheng–Hoza), build an explicit hitting set of size $\mathrm{poly}(n)$ for poly-width ROBPs at threshold $1/2$.

## 7. Current Research (as of June 2026)

- **WPRG and inverse-Laplacian analysis.** Richardson-iteration and shortcutting techniques (Chen–Hoza–Lyu–Tal–Wu, FOCS 2023) push weighted generators toward $\tilde{O}(\log^{1.5}n)$-type parameters for restricted widths *(frontier — verify)*. Groups: UT Austin (Zuckerman, Hoza's lineage), Harvard (Vadhan, Pyne), Stanford (Sidford), Weizmann (Raz, Tal).
- **Spectral / Laplacian toolkit.** Derandomized square, spectral sparsification in small space, and Eulerian Laplacian solvers extend the AKMPSV line to broader digraph classes and to estimating stationary distributions to inverse-polynomial precision.
- **Hardness vs. randomness for $\mathbf{BPL}$.** Doron–Pyne–Tell (STOC 2024) "open up the distinguisher", using structural properties of $\mathbf{BPL}$ rather than black-box hardness; direction: unconditional $\mathbf{BPL}=\mathbf{L}$ from lower bounds far weaker than the classical NW requirement.
- **Catalytic and shared-memory models.** Pyne and collaborators derandomize logspace given a small full "hard drive" — a model-theoretic route that has already produced new $\mathbf{BPL}$ simulations *(frontier — verify)*.
- **Fourier growth.** Bounding $L_1$ Fourier growth of ROBPs at each level (Chattopadhyay–Hatami–Hosseini–Lovett polarizing random walks; Tal's line) is the leading candidate for a unified constant-width analysis.

## 8. Future Work

1. **Width 4 and beyond.** Extend the MRT width-$3$ analysis to width $4$ with seed $\tilde O(\log n)$; a technique that survives one unit of width increase likely survives all constant widths.
2. **Reduce general to regular.** Find an explicit, seed-efficient transformation from arbitrary ROBPs to regular ones (currently costs a $w$-fold blowup that destroys the parameter gain).
3. **Optimal hitting sets.** By Cheng–Hoza, a $\mathrm{poly}(n)$-size explicit hitting set at threshold $1/2$ settles $\mathbf{BPL}=\mathbf{L}$; this one-sided target is strictly easier to attack.
4. **Break $\log^{3/2}$.** Improve Saks–Zhou–Hoza to $\mathbf{BPL}\subseteq\mathbf{DSPACE}(\log^{1+\delta}n)$ for some $\delta<1/2$ via better pseudodistributions.
5. **Lower bounds.** Prove any $\omega(\log n)$ seed lower bound for INW-style or "black-box recursive" generators, to delimit the search space.

## 9. Key References

- **[Foundational]** N. Nisan. *Pseudorandom generators for space-bounded computation.* Combinatorica 12(4):449–461, 1992.
- **[Foundational]** R. Impagliazzo, N. Nisan, A. Wigderson. *Pseudorandomness for network algorithms.* STOC 1994, 356–364.
- **[Foundational]** N. Nisan, D. Zuckerman. *Randomness is linear in space.* Journal of Computer and System Sciences 52(1):43–52, 1996.
- **[Foundational]** M. Saks, S. Zhou. *$\mathrm{BP}_H\mathrm{SPACE}(S)\subseteq \mathrm{DSPACE}(S^{3/2})$.* JCSS 58(2):376–403, 1999.
- **[Foundational]** O. Reingold. *Undirected connectivity in log-space.* Journal of the ACM 55(4), Article 17, 2008.
- **[Structural]** M. Braverman, A. Rao, R. Raz, A. Yehudayoff. *Pseudorandom generators for regular branching programs.* SIAM Journal on Computing 43(3):973–986, 2014.
- **[Structural]** M. Koucký, P. Nimbhorkar, P. Pudlák. *Pseudorandom generators for group products.* STOC 2011, 263–272.
- **[Structural]** A. Bogdanov, Z. Dvir, E. Verbin, A. Yehudayoff. *Pseudorandomness for width-2 branching programs.* Theory of Computing 9:283–293, 2013.
- **[SOTA / Recent]** R. Meka, O. Reingold, A. Tal. *Pseudorandom generators for width-3 branching programs.* STOC 2019, 626–637.
- **[SOTA / Recent]** M. Forbes, Z. Kelley. *Pseudorandom generators for read-once branching programs, in any order.* FOCS 2018, 946–955.
- **[SOTA / Recent]** M. Braverman, G. Cohen, S. Garg. *Pseudorandom pseudo-distributions with near-optimal error for read-once branching programs.* SIAM Journal on Computing 49(5):STOC18-242–299, 2020.
- **[SOTA / Recent]** E. Chattopadhyay, J.-J. Liao. *Optimal error pseudodistributions for read-once branching programs.* CCC 2020, 25:1–25:27.
- **[SOTA / Recent]** W. M. Hoza, D. Zuckerman. *Simple optimal hitting sets for small-success RL.* SIAM Journal on Computing 49(4):811–820, 2020.
- **[SOTA / Recent]** K. Cheng, W. M. Hoza. *Hitting sets give two-sided derandomization of small space.* CCC 2020, 10:1–10:25.
- **[SOTA / Recent]** W. M. Hoza. *Better pseudodistributions and derandomization for space-bounded computation.* RANDOM 2021, 28:1–28:23.
- **[SOTA / Recent]** A. Ahmadinejad, J. Kelner, J. Murtagh, J. Peebles, A. Sidford, S. Vadhan. *High-precision estimation of random walks in small space.* FOCS 2020, 1295–1306.
- **[SOTA / Recent]** E. Pyne, R. Raz, W. Zhan. *Certified hardness vs. randomness for log-space.* FOCS 2023.
- **[Survey]** W. M. Hoza. *Recent progress on derandomizing space-bounded computation.* Bulletin of the EATCS 138, 2022.
- **[Survey]** S. P. Vadhan. *Pseudorandomness.* Foundations and Trends in Theoretical Computer Science 7(1–3):1–336, 2012.

## 10. Worked Example / Concrete Special Case

**Setting.** $n=2^{10}=1024$, width $w=2^{10}$, target error $\varepsilon=1/10$. Take the INW recursion with expander graphs.

*Step 1 — level structure.* $G_j$ outputs $2^j$ bits, $j=0,\dots,10$; $G_0$ outputs one block of $m$ bits.

*Step 2 — per-level cost.* At level $j$, INW glues two halves using a walk on a $2^d$-regular $\lambda$-expander. The mixing lemma bounds the error introduced by
$$\Delta_j \le w\cdot\lambda,\qquad \lambda = 2^{-\Theta(d)} .$$
The hybrid argument sums over the $n$ layer-boundaries at which gluing occurs, so total error $\le n\cdot w\cdot\lambda$. Requiring $n w \lambda\le\varepsilon$ gives
$$\lambda\le \frac{\varepsilon}{nw}=\frac{1/10}{2^{20}}\approx 9.5\times10^{-8},\qquad d=\Theta\!\left(\log\frac{nw}{\varepsilon}\right)\approx 24\ \text{bits}.$$

*Step 3 — total seed.* $|s| = m + \sum_{j=1}^{10} d = m + 10\cdot 24 \approx 241$ bits, i.e. $\Theta(\log n\log(nw/\varepsilon))=\Theta(\log^2 n)$.

*Step 4 — the target.* A non-explicit generator exists with seed $O(\log(nw/\varepsilon)) \approx 24$ bits (probabilistic method: a random multiset of $O(nw/\varepsilon^2)$ strings fools all $2^{O(nw\log w)}$ programs by Chernoff plus union bound). The gap is $241$ vs $24$ — exactly the factor $\log n = 10$.

*Where the slack is.* If the program is *regular*, each $M_i^b$ is doubly stochastic, so total "weight" is conserved and one can charge error to a decreasing potential $\Phi_i=\sum_v |p_i(v)-1/w|$; BRRY show the per-level cost drops to $O(\log\log n+\log(w/\varepsilon))$ *amortized*, not $O(\log(nw/\varepsilon))$ per level, saving the $\log n$. For a general program with a sink vertex $t$ absorbing all mass after layer $n/2$, the potential does not decrease, the mixing lemma must be reapplied at full strength at every boundary, and the $\log n$ factor returns. Removing that reapplication for irregular programs is the whole problem.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*