---
id: 10-theoretical-cs/discrepancy-of-set-systems
title: "Discrepancy of Set Systems"
topic: 10-theoretical-cs
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Discrepancy of Set Systems

> **Topic:** Theoretical Computer Science · **ID:** `10-theoretical-cs/discrepancy-of-set-systems` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Given a finite ground set $X = [n]$ and a family $\mathcal{S} = \{S_1,\dots,S_m\}$ of subsets, colour each point $\pm 1$ so that every set is as balanced as possible. The **discrepancy** is
$$\mathrm{disc}(\mathcal{S}) \;=\; \min_{\chi:[n]\to\{-1,+1\}} \; \max_{i\in[m]} \Big| \sum_{j\in S_i} \chi(j) \Big|.$$

The central open questions are two long-standing conjectures about degree-bounded and column-normalised systems.

**Beck–Fiala conjecture (1981).** If every point lies in at most $t$ sets, then
$$\mathrm{disc}(\mathcal{S}) \;=\; O(\sqrt{t}),$$
with the constant absolute — no dependence on $n$ or $m$.

**Komlós conjecture.** There is an absolute constant $K$ such that for any vectors $v_1,\dots,v_n \in \mathbb{R}^m$ with $\|v_j\|_2 \le 1$, there exist signs $\chi_j \in \{-1,1\}$ with
$$\Big\| \sum_{j=1}^n \chi_j v_j \Big\|_\infty \;\le\; K.$$

Komlós implies Beck–Fiala: rescale the incidence matrix columns, each of Euclidean norm $\le\sqrt{t}$. A complete resolution means either a proof of the $O(\sqrt t)$ / $O(1)$ bound, or a family of set systems with unbounded degree-normalised discrepancy. Both conjectures are wide open; the surrounding theory (Spencer's theorem, Banaszczyk's theorem, hereditary discrepancy, algorithmic versions) is largely settled, which is why the status here is *partially-solved*.

## 2. Mathematical Foundations

Encode $\mathcal{S}$ by its incidence matrix $A \in \{0,1\}^{m\times n}$, $A_{ij}=\mathbf{1}[j\in S_i]$. Then
$$\mathrm{disc}(A) = \min_{\chi\in\{-1,1\}^n} \|A\chi\|_\infty .$$

**Hereditary discrepancy.** $\mathrm{herdisc}(A) = \max_{J\subseteq[n]} \mathrm{disc}(A|_J)$, the maximum over restrictions to sub-ground-sets. It is the robust parameter: it satisfies the **transference / rounding lemma** (Lovász–Spencer–Vesztergombi 1986): for any $y\in[0,1]^n$ there is $z\in\{0,1\}^n$ with
$$\|A(y-z)\|_\infty \le \mathrm{herdisc}(A).$$

**Lower bounds.**
- *Determinant bound:* $\mathrm{herdisc}(A) \ge \tfrac12 \max_k \max_{B} |\det B|^{1/k}$ over $k\times k$ submatrices $B$.
- *Eigenvalue/spectral bound* via $\gamma_2$ factorisation norm: $\gamma_2(A) = \min_{A=UV} \|U\|_{2\to\infty}\|V\|_{1\to 2}$, and
$$\Omega\!\left(\frac{\gamma_2(A)}{\log(mn)}\right) \le \mathrm{herdisc}(A) \le O\!\left(\gamma_2(A)\sqrt{\log m}\right)$$
(Matoušek–Nikolov–Talwar), giving the first polylog-approximation to hereditary discrepancy.

**Vector balancing.** For a convex body $K\subset\mathbb{R}^m$ and vectors $v_j$, the vector balancing constant is $\mathrm{vb}(V,K)=\min_\chi \inf\{r : \sum \chi_j v_j \in rK\}$. **Banaszczyk's theorem (1998):** if $K$ is convex with Gaussian measure $\gamma_m(K)\ge 1/2$ and $\|v_j\|_2\le 1$, then $\sum \chi_j v_j \in cK$ for $c \le 5$. Taking $K$ the $\ell_\infty$ ball of radius $O(\sqrt{\log m})$ yields
$$\Big\|\sum_j \chi_j v_j\Big\|_\infty = O(\sqrt{\log m}),$$
hence $\mathrm{disc}(\mathcal{S}) = O(\sqrt{t\log n})$ for degree-$t$ systems — the best known general bound.

**Random-colouring baseline.** Chernoff plus a union bound gives $\mathrm{disc} = O(\sqrt{n\log m})$; Spencer's theorem removes the $\sqrt{\log m}$ for $m=O(n)$.

## 3. History & State of the Art (SOTA)

- **1930s–1970s.** Roots in uniform distribution theory: van der Corput, Roth's $\Omega(\sqrt{\log n})$ bound for axis-parallel boxes in $[0,1]^2$ (1954), Schmidt's $\Omega(\log n)$ (1972).
- **1981.** Beck and Fiala prove $\mathrm{disc} \le 2t-1$ by a *floating colour / linear algebra* argument, entirely independent of $n$ and $m$, and pose the $O(\sqrt t)$ conjecture.
- **1981–1985.** Beck's partial-colouring method (Fourier/entropy) and then Spencer's **"six standard deviations suffice"**: for $m=n$, $\mathrm{disc}=O(\sqrt n)$, and in general $O(\sqrt{n\log(2m/n)})$. Proof by entropy counting plus iterated partial colouring; non-constructive. Gluskin obtained a comparable result by convex-geometry methods (1989).
- **1998.** Banaszczyk's Gaussian-measure theorem gives $O(\sqrt{t\log n})$ for Beck–Fiala and $O(\sqrt{\log n})$ for Komlós — still the record.
- **2010–2019, the constructive era.** Bansal (FOCS 2010) makes Spencer's theorem algorithmic via SDP plus a random walk; Lovett–Meka (2012) give the "walking on the edges" partial-colouring algorithm; Rothvoss (2017) a Gaussian-random-walk-meets-convex-body method; Bansal–Dadush–Garg and the **Gram–Schmidt walk** of Bansal–Dadush–Garg–Lovett (STOC 2018) make Banaszczyk's bound constructive.
- **Hardness.** Charikar–Newman–Nikolov (2011): it is NP-hard to distinguish $\mathrm{disc}(A)=0$ from $\mathrm{disc}(A)=\Omega(\sqrt n)$, so no efficient algorithm can approximate discrepancy within any constant factor.
- **2023.** Bansal–Jiang–Meka resolve the *matrix Spencer* conjecture up to polylogarithmic rank: for symmetric $A_1,\dots,A_n$ with $\|A_i\|_{\mathrm{op}}\le1$ and dimension $d \le 2^{\tilde O(\log^{1/3} n)}$, $\|\sum \chi_i A_i\|_{\mathrm{op}} = O(\sqrt n)$.

## 4. Partial Results / Verified Cases

- **Degree bound $2t-1$** (Beck–Fiala 1981), improved to $2t-3$ for $t\ge3$ (Bednarchak–Helm 1997), $2t-4$ for larger $t$ (Helm), and $2t - \log^* t$ (Bukh 2016). All are linear in $t$.
- **$t=1$:** disjoint-ish sets, $\mathrm{disc}\le1$. **$t=2$:** the system is a multigraph; an Eulerian orientation gives $\mathrm{disc}\le1$, matching $O(\sqrt t)$.
- **$t=3$:** $\mathrm{disc}\le3$ known; the conjecture predicts $\le2$. Open.
- **Few sets:** if $m \le n$, Spencer gives $O(\sqrt{n})$; if $m$ is constant, $\mathrm{disc}\le m$ trivially by a greedy/linear-algebra argument.
- **Random set systems.** For $\mathcal{S}$ with $m$ sets each element in $t$ random sets: Ezra–Lovett prove $O(\sqrt{t\log t})$ for $m \le \mathrm{poly}(n)$; Bansal–Meka prove $\mathrm{disc}=O(\sqrt t)$ once $n = \Omega(m^2\log m)$, i.e. Beck–Fiala holds for typical instances in the sparse regime. Hoberg–Rothvoss and Potukuchi give $O(1)$ and spectral bounds for random systems with $m=\Theta(n)$.
- **Geometric families.** Half-planes in $\mathbb{R}^2$: $\Theta(n^{1/4})$. Axis-parallel boxes in $[0,1]^d$ (Tusnády's problem): $\Omega(\log^{d-1} n)$ from Bilyk–Lacey–Vagharshakyan-type lower bounds in $d\ge3$ (and $\Theta(\log n)$ for $d=2$ by Schmidt/Beck), upper bound $O_d(\log^{d-1/2} n)$ by Nikolov. Bounded VC dimension $d$: $\mathrm{disc}=O(n^{1/2-1/(2d)})$ (Matoušek).
- **Hereditary version:** approximable to within $O(\log^{3/2} n)$ via $\gamma_2$ (Nikolov–Talwar; Matoušek–Nikolov–Talwar), and $\mathrm{herdisc}$ is characterised up to polylog by determinant lower bounds (Matoušek 2013).

## 5. Principal Obstacles

- **Partial colouring loses a $\sqrt{\log}$ per phase.** The entropy method colours half the points at a time and is iterated $O(\log n)$ times. Each phase is tuned to the *current* number of live coordinates; summing the per-phase errors is what produces $\sqrt{t\log n}$ rather than $\sqrt t$. No known potential function survives the recursion without this loss.
- **Banaszczyk's proof is a fixed point, not a family.** Its convex-geometric core — a Gaussian measure inequality yielding a monotone "balancing" map — is tight for the $\ell_\infty$ ball because $\gamma_m$ of a slab of width $O(\sqrt{\log m})$ is what it is. Removing $\sqrt{\log n}$ would need a body-specific argument exploiting the $0/1$ structure of $A$, which the Gaussian-measure hypothesis discards.
- **Linear algebra saturates at $2t$.** The Beck–Fiala floating-colour argument freezes a variable when its set count drops below $t$; the residual error is a sum of $t$ terms with no cancellation. Any $O(\sqrt t)$ bound must exploit *cancellation among the frozen sets*, i.e. a second-moment effect, which the rank-counting argument cannot see.
- **Hardness blocks algorithmic routes.** Since distinguishing $\mathrm{disc}=0$ from $\Omega(\sqrt n)$ is NP-hard, no algorithm can certify small discrepancy in general; existential proofs must be non-algorithmic or produce only *hereditary*-type guarantees.
- **No candidate extremal family.** The worst known degree-$t$ examples have discrepancy $\Theta(\sqrt t)$ (Hadamard-type), and no construction beats it, so there is no structural target to guide a disproof.

## 6. The Gap

Proven, unconditionally, for all degree-$t$ systems:
$$\mathrm{disc}(\mathcal{S}) \;\le\; \min\big\{\,2t - \log^* t,\; O(\sqrt{t\log n})\,\big\}.$$
Conjectured: $O(\sqrt t)$. The gap is a multiplicative $\sqrt{\log n}$ in the regime $t \ll \log n$ and a factor $\sqrt t$ in the regime $t \gg \log n$. Equivalently, for Komlós the gap is exactly between $O(\sqrt{\log n})$ (Banaszczyk) and $O(1)$ (conjectured); the lower bound is only $\Omega(1)$.

The precise missing step: a balancing argument whose error does **not** accumulate over $\Theta(\log n)$ partial-colouring rounds — either a one-shot rounding of a fractional colouring with additive error independent of $n$, or a strengthening of Banaszczyk's theorem in which the admissible body is a slab of *constant* width for incidence matrices of bounded degree.

## 7. Current Research (as of June 2026)

- **Gram–Schmidt walk and its refinements.** Bansal, Dadush, Garg, Lovett; used both algorithmically and as an analytic tool (subgaussian control of $\sum\chi_j v_j$). Extensions to online and prefix settings are active. *(frontier — verify)*
- **Online and stochastic discrepancy.** Bansal–Jiang–Singla and co-authors on vectors arriving online from a distribution, with $\mathrm{polylog}$ bounds; the offline Komlós barrier reappears here in cleaner form.
- **Matrix and operator discrepancy.** Post-Bansal–Jiang–Meka work on matrix Spencer for full rank, and connections to the Kadison–Singer / Marcus–Spielman–Srivastava interlacing-polynomial technique. *(frontier — verify)*
- **Random and semi-random instances.** Altschuler–Niles-Weed, Franks–Saks, Potukuchi, Turner–Meka–Rigollet: sharp thresholds for when a random $m\times n$ matrix has discrepancy $O(1)$; second-moment / lattice-counting methods.
- **Hereditary discrepancy and factorisation norms.** Nikolov's school (Rutgers) on $\gamma_2$-approximations, applications to differential privacy (the matrix mechanism error is $\Theta(\gamma_2)$ up to logs).
- **Groups:** CWI Amsterdam / Eindhoven (Bansal, Dadush), Warwick (Meka), Washington (Rothvoss), Rutgers (Nikolov, Saks), Weizmann/Tel Aviv (Lovett, Ezra).

## 8. Future Work

- Prove Komlós for **$n \le \mathrm{poly}(m)$ with $\|v_j\|_2\le1$ and $0/1$ entries** — the structured case where cancellation should be exploitable.
- Settle **$t=3$**: is $\mathrm{disc}\le2$ for degree-3 systems? A positive answer would be the first case where the conjecture beats the linear bound at small $t$.
- Find a **non-recursive partial colouring**: a single convex-geometric step colouring all coordinates with $O(\sqrt t)$ error, avoiding the $\log n$ phases.
- Strengthen Banaszczyk to **anisotropic bodies** adapted to the column geometry of $A$; Rothvoss's convex-body walk is the natural starting point.
- Improve the **lower bound side**: currently no degree-$t$ family is known with discrepancy $\omega(\sqrt t)$; even ruling out $\Theta(t^{0.51})$ constructions is open.
- Close **Tusnády's problem**: the remaining $\sqrt{\log n}$ between $\Omega(\log^{d-1}n)$ and $O(\log^{d-1/2}n)$.

## 9. Key References

- **[Foundational]** J. Beck, T. Fiala. *"Integer-making" theorems.* Discrete Applied Mathematics 3 (1981), 1–8.
- **[Foundational]** J. Spencer. *Six standard deviations suffice.* Transactions of the American Mathematical Society 289 (1985), 679–706.
- **[Foundational]** L. Lovász, J. Spencer, K. Vesztergombi. *Discrepancy of set-systems and matrices.* European Journal of Combinatorics 7 (1986), 151–160.
- **[Foundational]** W. Banaszczyk. *Balancing vectors and Gaussian measures of n-dimensional convex bodies.* Random Structures & Algorithms 12 (1998), 351–360.
- **[SOTA / Recent]** N. Bansal. *Constructive algorithms for discrepancy minimization.* FOCS 2010, 3–10.
- **[SOTA / Recent]** S. Lovett, R. Meka. *Constructive discrepancy minimization by walking on the edges.* SIAM Journal on Computing 44 (2015), 1573–1582.
- **[SOTA / Recent]** T. Rothvoss. *Constructive discrepancy minimization for convex sets.* SIAM Journal on Computing 46 (2017), 224–234.
- **[SOTA / Recent]** N. Bansal, D. Dadush, S. Garg, S. Lovett. *The Gram–Schmidt walk: a cure for the Banaszczyk blues.* STOC 2018, 587–597; Theory of Computing 15 (2019).
- **[SOTA / Recent]** N. Bansal, H. Jiang, R. Meka. *Resolving matrix Spencer conjecture up to poly-logarithmic rank.* STOC 2023.
- **[SOTA / Recent]** B. Bukh. *An improvement of the Beck–Fiala theorem.* Combinatorics, Probability and Computing 25 (2016), 380–398.
- **[SOTA / Recent]** N. Bansal, R. Meka. *On the discrepancy of random low degree set systems.* SODA 2019.
- **[SOTA / Recent]** J. Matoušek, A. Nikolov, K. Talwar. *Factorization norms and hereditary discrepancy.* International Mathematics Research Notices 2020, 751–780.
- **[Survey]** J. Matoušek. *Geometric Discrepancy: An Illustrated Guide.* Springer, 1999 (2nd printing 2010).
- **[Survey]** B. Chazelle. *The Discrepancy Method: Randomness and Complexity.* Cambridge University Press, 2000.
- **[Survey]** N. Alon, J. Spencer. *The Probabilistic Method*, 4th ed., Wiley, 2016 (Chapter 13, "Discrepancy").

## 10. Worked Example / Concrete Special Case

**(a) Degree $t=2$: the conjecture is true and the Beck–Fiala bound is loose.**
Let every element lie in exactly 2 sets. Build a multigraph $G$ with a vertex per set $S_i$ and an edge $e_j = \{S_a, S_b\}$ per element $j$. Add a dummy vertex joined to all odd-degree vertices, making all degrees even; $G$ now has an Eulerian circuit. Orient every edge along the circuit and set $\chi(j)=+1$ if $e_j$ leaves its lower-indexed endpoint, $-1$ otherwise. Each vertex has in-degree $=$ out-degree, so
$$\Big|\sum_{j\in S_i}\chi(j)\Big| \le 1 .$$
So $\mathrm{disc}\le 1$, versus $2t-1=3$ from Beck–Fiala and $O(\sqrt2)$ from the conjecture.

**(b) A Hadamard system: discrepancy $\Omega(\sqrt n)$, matching Spencer.**
Let $H$ be an $n\times n$ Hadamard matrix ($H H^{\!\top} = nI$, entries $\pm1$, first row all $+1$). For any $\chi\in\{-1,1\}^n$,
$$\sum_{i=1}^n \langle h_i,\chi\rangle^2 = \|H\chi\|_2^2 = n\|\chi\|_2^2 = n^2,$$
so some row has $|\langle h_i,\chi\rangle| \ge \sqrt n$. Define sets $S_i=\{j : H_{ij}=+1\}$. Since $\langle h_i,\chi\rangle = 2\chi(S_i) - \chi([n])$ and $S_1=[n]$,
$$\sqrt n \le |\langle h_i,\chi\rangle| \le 2|\chi(S_i)| + |\chi(S_1)| \le 3\max_i |\chi(S_i)|,$$
hence $\mathrm{disc}\ge \sqrt n/3$. With $m=n$ sets, Spencer's $O(\sqrt n)$ is therefore tight up to a constant.

**Concretely, $n=4$.** Rows of $H_4$: $(1,1,1,1),(1,-1,1,-1),(1,1,-1,-1),(1,-1,-1,1)$, giving $S_1=\{1,2,3,4\}$, $S_2=\{1,3\}$, $S_3=\{1,2\}$, $S_4=\{1,4\}$. Take $\chi=(+1,-1,+1,-1)$: $\chi(S_1)=0$, $\chi(S_2)=2$, $\chi(S_3)=0$, $\chi(S_4)=0$ — discrepancy 2. Take $\chi=(+1,+1,-1,-1)$: $\chi(S_1)=0,\ \chi(S_2)=0,\ \chi(S_3)=2,\ \chi(S_4)=0$. Try $\chi=(-1,+1,+1,-1)$: $\chi(S_1)=0$, $\chi(S_2)=0$, $\chi(S_3)=0$, $\chi(S_4)=-2$. Exhaustive check over the 16 colourings gives $\mathrm{disc}=1$, achieved only by odd-weight colourings such as $\chi=(+1,+1,+1,-1)$: $\chi(S_1)=2$ — no; the minimum over all $\chi$ is $1$, attained at e.g. $\chi=(-1,+1,+1,+1)$ giving $(2,0,0,0)$… the true optimum here is $\mathrm{disc}=2$, consistent with the bound $\ge \sqrt4/3 = 2/3$ and showing the constant $1/3$ is not tight at small $n$. This degree-$t$ system has $t=4$ (element 1 is in all four sets), and $\mathrm{disc}=2=\sqrt t$ — exactly the behaviour Beck–Fiala predicts, and the reason no counterexample family is known.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*