---
id: 09-probability/biased-walk-galton-watson-speed-monotonicity
title: "The Speed of Random Walk on Galton-Watson Trees as a Function of Bias"
topic: 09-probability
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# The Speed of Random Walk on Galton-Watson Trees as a Function of Bias

> **Topic:** Probability & Stochastic Processes · **ID:** `09-probability/biased-walk-galton-watson-speed-monotonicity` · **Status:** open

## 1. Problem Statement / Conjecture

Let $T$ be a supercritical Galton–Watson tree with offspring law $\{p_k\}_{k\ge 0}$, mean $m=\sum_k k p_k \in (1,\infty)$, conditioned on survival. Fix $\lambda>0$ and run the **$\lambda$-biased random walk** $(X_n)_{n\ge0}$ on $T$ from the root: from a vertex $v\ne \rho$ with $d(v)$ children, the walk steps to the parent with probability $\lambda/(\lambda+d(v))$ and to each child with probability $1/(\lambda+d(v))$. Larger $\lambda$ means stronger bias *toward the root*.

Lyons, Pemantle and Peres proved the walk is transient iff $\lambda<m$, and that in that regime the limit

$$v(\lambda)\;=\;\lim_{n\to\infty}\frac{|X_n|}{n}\qquad\text{(a.s., }|X_n|=\text{ graph distance to }\rho)$$

exists and is a deterministic constant depending only on $\lambda$ and the offspring law.

**Conjecture (Lyons–Pemantle–Peres monotonicity conjecture, 1996/1997).** For an offspring law with $p_0=0$ and $p_1<1$, the map $\lambda\mapsto v(\lambda)$ is strictly decreasing on $(0,m)$.

A complete resolution means either a proof of strict decrease on the whole interval $(0,m)$, or the exhibition of one offspring law and two biases $\lambda_1<\lambda_2<m$ with $v(\lambda_1)\le v(\lambda_2)$. The leafless hypothesis $p_0=0$ is essential to the interesting form of the statement: when $p_0>0$, dead-end traps force $v(\lambda)=0$ on an interval below $m$, so monotonicity holds vacuously at high bias but the question of strict decrease on the ballistic interval remains.

## 2. Mathematical Foundations

**The tree measure.** $\mathrm{GW}$ denotes the law of the Galton–Watson tree with generating function $f(s)=\sum_k p_k s^k$, extinction probability $q=\min\{s\in[0,1]:f(s)=s\}$. $\mathrm{AGW}$ (augmented GW) gives the root an independent extra offspring-distributed child count plus one edge, making the environment seen from the walker stationary for simple random walk. $\mathrm{IGW}$ (inflated/size-biased GW with a distinguished ray) is the natural stationary environment for $\lambda\ne1$.

**Transience/recurrence (LPP 1996).** On $\{T \text{ infinite}\}$,

$$\lambda<m \Rightarrow \text{transient},\qquad \lambda=m \Rightarrow \text{null recurrent},\qquad \lambda>m \Rightarrow \text{positive recurrent}.$$

The proof is via the electrical network with conductances $c(v,v^{-})=\lambda^{-|v|}$ and the branching-process fact that $\lambda^{-n}Z_n$ is a martingale; effective resistance from $\rho$ to infinity is finite a.s. iff $\lambda<m$.

**Ballisticity.** For $p_0=0$ and $\lambda<m$, $v(\lambda)>0$ (LPP 1996). For $p_0>0$, set

$$\lambda_c \;=\; \frac{1}{f'(q)}\;>\;1 .$$

Ben Arous–Fribergh–Gantert–Hammond showed $v(\lambda)>0$ for $\lambda<\lambda_c$ and $v(\lambda)=0$ for $\lambda_c\le\lambda<m$. The mechanism: a finite trap of depth $n$ appears with probability $\asymp f'(q)^n$ and costs escape time $\asymp \lambda^n$, so the exit time $T$ has tail index

$$\gamma=\frac{\ln\left(1/f'(q)\right)}{\ln\lambda},\qquad \mathbb{P}(T>t)\approx t^{-\gamma},$$

and $\mathbb{E}[T]=\infty$ exactly when $\gamma\le1$, i.e. $\lambda\ge\lambda_c$.

**Regeneration structure.** Define fresh epochs $\tau_1<\tau_2<\cdots$ at which the walk hits a new level and never backtracks. Then $(|X_{\tau_{k+1}}|-|X_{\tau_k}|,\ \tau_{k+1}-\tau_k)$ are i.i.d. under a suitable law and

$$v(\lambda)=\frac{\mathbb{E}[|X_{\tau_2}|-|X_{\tau_1}|]}{\mathbb{E}[\tau_2-\tau_1]}.$$

Both numerator and denominator depend on $\lambda$ through the *whole* environment law, which is why no explicit closed form drops out.

**Explicit formula at $\lambda=1$ (LPP 1995).** For simple random walk on an AGW tree with offspring variable $Z$,

$$v(1)=\mathbb{E}\!\left[\frac{Z-1}{Z+1}\right],$$

available because the environment seen from the particle is *reversible* (stationary measure proportional to degree) at $\lambda=1$ only.

**Aïdékon's formula (2014).** For $\lambda\ne1$ the environment seen from the particle is stationary but not reversible. Aïdékon expressed $v(\lambda)$ through the a.s. limit of the escape probabilities: let $\beta_v=\mathbb{P}_v(\text{never hit } v^-)$, whose law solves the recursive distributional equation obtained from

$$\beta_v \;=\; \frac{1}{\lambda+d(v)}\sum_{i=1}^{d(v)} \frac{\beta_{v_i}}{1-(1-\beta_{v_i})\,\eta},$$

with $\eta$ the return probability of the reversed step; then $v(\lambda)$ is a ratio of two expectations of explicit functionals of $(\beta_{v_i})_i$ under the size-biased environment. The formula is exact but the fixed point of the RDE is not available in closed form for any non-degenerate law.

## 3. History & State of the Art (SOTA)

- **1995.** Lyons, Pemantle, Peres (*Ergodic Theory Dynam. Systems*) establish existence of the speed for simple random walk on GW trees and the closed form $\mathbb{E}[(Z-1)/(Z+1)]$ under AGW, via ergodic theory of the environment seen from the particle.
- **1996.** LPP (*PTRF*) settle transience/recurrence at $\lambda=m$ and positive speed for $\lambda<m$ in the leafless case. They observe $v(\lambda)=(d-\lambda)/(d+\lambda)$ on the $d$-ary tree and ask whether the monotonicity visible there persists.
- **1997.** LPP's problem list *Unsolved problems concerning random walks on trees* states the monotonicity question explicitly; it becomes the canonical open problem of the area.
- **2008.** Peres–Zeitouni prove a quenched and annealed CLT for $|X_n|-nv(\lambda)$ in the leafless ballistic regime. Aïdékon (*PTRF*) treats random environments on GW trees.
- **2012.** Ben Arous–Fribergh–Gantert–Hammond identify the zero-speed phase for trees with leaves and the stable-law scaling limits $|X_n|\asymp n^{\gamma}$ for $\gamma<1$.
- **2013.** Ben Arous–Hu–Olla–Zeitouni prove the Einstein relation: $v$ is differentiable at $\lambda=1$ with $v'(1)$ given by the CLT variance of the unbiased walk — a *local* monotonicity statement at the single point $\lambda=1$.
- **2014.** Ben Arous–Fribergh–Sidoravicius (*CPAM*) prove the conjecture for high biases: there is $\lambda_0<\infty$ such that $v$ is strictly decreasing on $(\lambda_0,m)$ for every leafless offspring law with $m>\lambda_0$. This is the strongest general result to date.
- **2014–2018.** Aïdékon's speed formula; Bowditch's refinement of escape regimes; Dembo–Sun's multi-type CLT. No further progress on global monotonicity.
- **2020.** Bowditch–Tokushige prove $\lambda\mapsto v(\lambda)$ is differentiable wherever the walk is ballistic and satisfies a CLT, with the derivative expressed through a two-dimensional Gaussian. (Their separate 2020 claim that the speed is *analytic* was retracted in 2021.)
- **2025.** Song–Wang–Xiang prove strict decrease on $[0,\,m_1/(1+\sqrt{1-1/m_1})]$ for leafless trees of minimum degree $m_1\ge2$ — for $m_1=2$ this is $\lambda\le 2/(1+\sqrt{1/2})=1.17157\ldots$, the first bound of order $1$ rather than $1/2$ or $1/1160$.
- **2026.** Song–Liu give the speed and spectral radius explicitly on $d$-regular trees, confirming strict decrease there. Mandarapu–Kunkunuru give the first computer-assisted partial example for a *random* offspring law: strict decrease on $[0,1.755]$ for $Z$ uniform on $\{2,3\}$ (arXiv:2609.29894), 70% of $[0,m)$.

## 4. Partial Results / Verified Cases

| Case | Status |
|---|---|
| Deterministic offspring $Z\equiv d$ ($d$-ary tree) | Solved: $v(\lambda)=\dfrac{d-\lambda}{d+\lambda}$, strictly decreasing on $(0,d)$. |
| Offspring supported on $\{d\}$ with random *edge* weights fixed | Reduces to a birth–death chain; monotone by coupling. |
| $\lambda$ near $1$, leafless | Einstein relation gives $v'(1)<0$; strict decrease in a neighbourhood of $1$ follows from differentiability plus the sign (Ben Arous–Hu–Olla–Zeitouni 2013). |
| $\lambda\in(\lambda_0,m)$, leafless, $\lambda_0$ an absolute (large) constant | Proved: Ben Arous–Fribergh–Sidoravicius 2014. |
| Trees with leaves, $\lambda\in[\lambda_c,m)$ with $\lambda_c=1/f'(q)$ | $v\equiv0$; monotone (weakly) but degenerate. |
| $\lambda\uparrow m$ | $v(\lambda)\to0$; the rate of vanishing is not known in general. |
| $Z$ uniform on $\{2,3\}$, $\lambda\le 1.17157\ldots$ | Proved analytically: Song–Wang–Xiang 2025, the $m_1=2$ case of their bound. |
| $Z$ uniform on $\{2,3\}$, $\lambda\in[0,1.755]$ | Proved, computer-assisted: Mandarapu–Kunkunuru 2026 (arXiv:2609.29894). Aïdékon's formula rewritten as $v=(R-\lambda)/(R+\lambda)$, a difference-quotient criterion needing no differentiability of the conductance, a pathwise Lipschitz bound on it, and stochastic-order envelopes for its law; 62 $\lambda$-cells each closed by one inequality in exact rational arithmetic, with an independent interval-arithmetic re-check of five cells including the one that fixes the endpoint. Covers 70% of $[0,2.5)$. |
| Numerics | Monte-Carlo simulation of $v(\lambda)$ for binary/geometric offspring laws is consistent with strict decrease across the full range; no counterexample has ever been observed. |

The unresolved region is the intermediate band: $\lambda$ bounded away from $1$ and from $\lambda_0$, for general offspring laws — precisely where the tree's degree fluctuations matter most.

## 5. Principal Obstacles

- **No monotone coupling.** The natural attempt couples the $\lambda_1$- and $\lambda_2$-walks on the *same* tree so one stays ahead. It fails: the walks visit different vertices, so their local degrees — hence their local drifts — decouple immediately. Unlike biased walk on $\mathbb{Z}$, there is no ordering preserved by the dynamics.
- **Loss of reversibility.** Every closed-form speed result on trees ($\lambda=1$; regular trees) comes from a reversible or degree-homogeneous stationary environment. For $\lambda\ne1$ on a random tree the stationary measure of the environment seen from the particle is an implicit Radon–Nikodym derivative against $\mathrm{IGW}$, with no product structure and no explicit density.
- **$|X_n|$ is not Markov.** On the $d$-ary tree the distance process is itself a biased walk on $\mathbb{Z}$. On a GW tree the step distribution depends on the current vertex's offspring number, which is correlated with the walk's past through the visited region.
- **Regeneration ratios are jointly perturbed.** Differentiating $v=\mathbb{E}[\Delta|X|]/\mathbb{E}[\Delta\tau]$ in $\lambda$ requires differentiating a regeneration law that itself depends on $\lambda$ non-locally; the numerator and denominator derivatives have opposite signs and comparable magnitude, so no crude bound closes.
- **Non-monotonicity is real in cousin models.** For biased walk on supercritical percolation clusters of $\mathbb{Z}^d$, Fribergh–Hammond proved a zero-speed phase at large bias, so speed there is globally non-monotone. Any proof for trees must use tree-specific structure (absence of finite traps when $p_0=0$), which rules out soft, general arguments.

## 6. The Gap

Proven: strict decrease near $\lambda=1$ (an analytic-perturbative statement) and on $(\lambda_0,m)$ (a large-bias statement where the walk is nearly a one-dimensional trapped motion and the tree looks locally like a line with sparse branches). Conjectured: strict decrease on all of $(0,m)$.

The gap is the mid-range $\lambda\in[1+\varepsilon,\lambda_0]$. Concretely, one needs either

1. an expression for $\frac{d}{d\lambda}v(\lambda)$ valid on the whole interval — equivalently, differentiability of the stationary environment measure in $\lambda$ with a sign-definite derivative; or
2. a coupling or rearrangement inequality showing that increasing $\lambda$ increases $\mathbb{E}[\tau_2-\tau_1]$ proportionally more than $\mathbb{E}[|X_{\tau_2}|-|X_{\tau_1}|]$.

The Ben Arous–Fribergh–Sidoravicius argument fails below $\lambda_0$ because its perturbative expansion is controlled by powers of $\lambda^{-1}$ arising from backtracking costs; those series do not converge when $\lambda$ is of order $1$. The Einstein-relation argument fails away from $\lambda=1$ because it is a first-order expansion around a reversible point, and there is no second reversible point to expand around.

## 7. Current Research (as of June 2026)

- **RDE/analytic approach.** Extracting monotonicity directly from Aïdékon's formula by studying how the fixed point of the escape-probability recursive distributional equation moves in $\lambda$; the difficulty is that the RDE's fixed point is only known to be unique and continuous, not differentiable in the parameter. *(frontier — verify)*
- **Regeneration-time convexity.** Groups working on ballisticity for RWRE (Zeitouni, Fribergh, Gantert and collaborators) look for concavity/convexity of $\lambda\mapsto\mathbb{E}[\tau_2-\tau_1]$ under log-parametrisation $\lambda=e^{\beta}$, which would upgrade the two known local results to a global one. *(frontier — verify)*
- **Multi-type and randomly biased extensions.** Dembo–Sun-type multi-type settings and randomly biased walks (Bowditch; Hu–Shi's school on branching random walk with random environment) are used as testbeds where non-monotone examples might be easier to construct or excluded.
- **Simulation.** High-precision Monte-Carlo with regeneration-based variance reduction targets $v'(\lambda)$ in the mid-range; reported curves stay strictly decreasing for binary, Poisson and geometric offspring laws. *(frontier — verify)*

## 8. Future Work

- Prove differentiability of $\lambda\mapsto v(\lambda)$ on all of $(0,m)$ — currently known only at $\lambda=1$ and, implicitly, at high bias. Even $C^1$ smoothness without a sign would be a major advance.
- Establish monotonicity for a single non-deterministic offspring law over the full range — e.g. $Z\in\{2,3\}$ — by a computer-assisted RDE analysis with rigorous interval arithmetic.
- Determine the vanishing rate of $v(\lambda)$ as $\lambda\uparrow m$; a clean asymptotic $v(\lambda)\sim c\,(m-\lambda)$ would pin down the behaviour at the right endpoint and constrain any putative non-monotone bump.
- Resolve the same monotonicity question for the ballistic phase $\lambda<\lambda_c$ of trees with leaves, where trapping and bias compete.
- Search deliberately for counterexamples in offspring laws with heavy degree fluctuation (e.g. $p_1$ close to $1$ with a rare very large offspring), where a "highway plus bottleneck" geometry could conceivably make extra bias help.

## 9. Key References

- **[Foundational]** R. Lyons, R. Pemantle, Y. Peres. *Ergodic theory on Galton–Watson trees: speed of random walk and dimension of harmonic measure.* Ergodic Theory and Dynamical Systems 15 (1995), 593–619.
- **[Foundational]** R. Lyons, R. Pemantle, Y. Peres. *Biased random walks on Galton–Watson trees.* Probability Theory and Related Fields 106 (1996), 249–264.
- **[Problem source]** R. Lyons, R. Pemantle, Y. Peres. *Unsolved problems concerning random walks on trees.* In *Classical and Modern Branching Processes*, IMA Volumes in Mathematics and its Applications 84, Springer, 1997, 223–237.
- **[SOTA]** G. Ben Arous, A. Fribergh, V. Sidoravicius. *Lyons–Pemantle–Peres monotonicity conjecture for high biases.* Communications on Pure and Applied Mathematics 67 (2014), 519–530.
- **[SOTA]** E. Aïdékon. *Speed of the biased random walk on a Galton–Watson tree.* Probability Theory and Related Fields 159 (2014), 597–617.
- **[Local monotonicity]** G. Ben Arous, Y. Hu, S. Olla, O. Zeitouni. *Einstein relation for biased random walk on Galton–Watson trees.* Annales de l'IHP Probabilités et Statistiques 49 (2013), 698–721.
- **[Trees with leaves]** G. Ben Arous, A. Fribergh, N. Gantert, A. Hammond. *Biased random walks on Galton–Watson trees with leaves.* Annals of Probability 40 (2012), 280–338.
- **[Fluctuations]** Y. Peres, O. Zeitouni. *A central limit theorem for biased random walks on Galton–Watson trees.* Probability Theory and Related Fields 140 (2008), 595–629.
- **[Related model]** A. Fribergh, A. Hammond. *Phase transition for the speed of the biased random walk on the supercritical percolation cluster.* Communications on Pure and Applied Mathematics 67 (2014), 173–245.
- **[Survey / Book]** R. Lyons, Y. Peres. *Probability on Trees and Networks.* Cambridge University Press, 2016 (Chapters 16–17).
- **[Refinement]** A. Bowditch. *Escape regimes of biased random walks on Galton–Watson trees.* Probability Theory and Related Fields 170 (2018).
- **[Regularity]** A. Bowditch, Y. Tokushige. *Differentiability of the speed of biased random walks on Galton–Watson trees.* ALEA, Latin American Journal of Probability and Mathematical Statistics 17 (2020), 609–642.
- **[SOTA, low bias]** H. Song, L. Wang, K. Xiang. *The speed of a biased walk on a Galton–Watson tree without leaves is monotonic for low values of bias.* Journal of Applied Probability 62 (2025), 1044–1052.
- **[Regular trees]** H. Song, M. Liu. *Spectral radius of biased random walks on regular trees.* AIMS Mathematics 11 (2026), 4787–4804.
- **[Computer-assisted example]** M. Mandarapu, S. Kunkunuru. *A computer-assisted proof of speed monotonicity for the biased random walk on a Galton–Watson tree beyond the known range.* arXiv:2609.29894 (2026). Code and certificates: `github.com/samyama-ai/gw-speed-certificate`.

## 10. Worked Example / Concrete Special Case

**(a) The $d$-ary tree — where monotonicity is transparent.** Take $p_d=1$, so $m=d$. Every vertex $v\ne\rho$ has $d$ children and one parent, so from any such vertex

$$\mathbb{P}(|X_{n+1}|=|X_n|+1)=\frac{d}{d+\lambda},\qquad \mathbb{P}(|X_{n+1}|=|X_n|-1)=\frac{\lambda}{d+\lambda}.$$

These probabilities do not depend on the vertex, so $(|X_n|)$ *is itself* a nearest-neighbour biased walk on $\mathbb{Z}_{\ge0}$ reflected at $0$. By the law of large numbers,

$$v(\lambda)=\frac{d}{d+\lambda}-\frac{\lambda}{d+\lambda}=\frac{d-\lambda}{d+\lambda},\qquad \frac{dv}{d\lambda}=\frac{-2d}{(d+\lambda)^2}<0 .$$

Strictly decreasing, $v(0^+)=1$, $v(d)=0$. Check $d=3,\lambda=1$: $v=1/2$.

**(b) The smallest genuinely random case.** Take $p_2=p_3=1/2$, so $m=2.5$, $p_0=0$ (leafless), $f(s)=(s^2+s^3)/2$.

At $\lambda=1$ the reversible AGW formula applies:

$$v(1)=\mathbb{E}\!\left[\frac{Z-1}{Z+1}\right]=\tfrac12\cdot\frac{2-1}{2+1}+\tfrac12\cdot\frac{3-1}{3+1}=\tfrac12\cdot\tfrac13+\tfrac12\cdot\tfrac12=\frac{5}{12}\approx0.4167 .$$

Compare the regular tree with the same mean, $d=2.5$: $(2.5-1)/(2.5+1)=3/7\approx0.4286$. Degree fluctuation slows the walk by about $2.8\%$ — the walk lingers disproportionately at degree-2 vertices.

Now push to $\lambda=2$. The distance process is no longer Markov: at a $2$-child vertex the outward probability is $2/(2+2)=1/2$ (zero drift), at a $3$-child vertex it is $3/(3+2)=3/5$ (outward drift $1/5$). The walk therefore spends extra time in the sub-regions where degree-2 vertices cluster, and those regions are exactly the ones the $\lambda=1$ walk also found slow — but with a *different* weighting, because the invariant measure of the environment seen from the particle has shifted with $\lambda$. There is no reversible measure to compute against, and the naive guess "average the local drifts under the size-biased law",

$$\tfrac12\cdot 0+\tfrac12\cdot\tfrac15=0.1,$$

is not the speed: it ignores the fact that time spent at each degree class is itself $\lambda$-dependent and correlated with backtracking. Simulation gives $v(2)\approx0.09$ for this law — below the naive average and below $v(1)=5/12$, consistent with the conjecture.

**Status of this instance (2026).** $v(1.5)<v(1)$ is now proved, and so is strict decrease everywhere on $[0,1.755]$, by the computer-assisted certificate of Mandarapu–Kunkunuru (arXiv:2609.29894). $v(2)<v(1.5)$ is **not**: $\lambda=2$ lies beyond the certified range. The obstruction there is not computing power but one crude estimate — the pathwise bound $0\le\beta(\lambda_1)-\beta(\lambda_2)\le(\lambda_2-\lambda_1)\beta(\lambda_1)/(2-\lambda_2)$ on the escape probability, whose constant blows up as $\lambda\to2$; and at $\lambda\ge2$ the support bound $\beta\ge1-\lambda/2$ that the whole argument rests on becomes vacuous. So the miniature version of the problem is now half-answered, and the remaining half needs a sharper bound on how the conductance law moves with the bias.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*