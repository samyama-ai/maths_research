---
id: 09-probability/capacity-of-the-brownian-motion-path-in-3d
title: "Capacity of the Brownian Motion Path in 3D"
topic: 09-probability
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Capacity of the Brownian Motion Path in 3D

> **Topic:** Probability & Stochastic Processes · **ID:** `09-probability/capacity-of-the-brownian-motion-path-in-3d` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

Let $(W_t)_{t\ge 0}$ be standard Brownian motion in $\mathbb{R}^3$ started at the origin, and let
$$\mathcal{W}[0,1]=\{W_t : 0\le t\le 1\}$$
be its (compact, random) trace. Let $\mathrm{cap}$ denote Newtonian capacity with respect to the kernel $k(x,y)=|x-y|^{-1}$, normalised so that $\mathrm{cap}(\bar B(0,r))=r$. Set
$$\mathcal{C}_3 := \mathrm{cap}\big(\mathcal{W}[0,1]\big).$$

$\mathcal{C}_3$ is a.s. finite and a.s. strictly positive (the path has Hausdorff dimension $2>1$). Brownian scaling gives the exact identity $\mathrm{cap}(\mathcal{W}[0,t]) = \sqrt{t}\,\mathcal{C}_3$ in law, so all the content is in the **law of the single random variable $\mathcal{C}_3$**.

**The problem.** Determine $\mathcal{C}_3$ quantitatively:

1. Compute $\mathbb{E}[\mathcal{C}_3]$ in closed form (or prove no closed form exists). No value is known — only two-sided bounds.
2. Determine the law of $\mathcal{C}_3$: does it have a smooth density? What are its upper and lower tails, $\mathbb{P}(\mathcal{C}_3>\lambda)$ and $\mathbb{P}(\mathcal{C}_3<\varepsilon)$?
3. Give the sharp small-radius expansion of the capacity of the Wiener sausage $\mathcal{W}^{a}[0,1]=\{x:\mathrm{dist}(x,\mathcal{W}[0,1])\le a\}$ as $a\downarrow 0$, i.e. the rate at which $\mathrm{cap}(\mathcal{W}^a[0,1])\downarrow \mathcal{C}_3$.

A complete solution to (1) means an exact evaluation with proof; to (2), identification of the tail exponents with matching constants; to (3), a theorem with an explicit correction term.

The **recently solved** part is the structural/asymptotic layer: order of magnitude, capacity-equivalence to a square, and the law-of-large-numbers and fluctuation theory for the lattice analogue (capacity of the range of simple random walk) in every dimension. The exact constants for $d=3$ remain open.

## 2. Mathematical Foundations

**Energy and capacity.** For a compact $A\subset\mathbb{R}^3$ and a probability measure $\mu$ on $A$, the Newtonian energy is
$$I(\mu)=\iint \frac{\mu(dx)\,\mu(dy)}{|x-y|},\qquad \mathrm{cap}(A)=\Big(\inf_{\mu\in\mathcal{P}(A)} I(\mu)\Big)^{-1}.$$
Equivalently, in probabilistic form (Port–Stone), for $|x|$ large,
$$\mathbb{P}_x\big(\exists t\ge 0:\ B_t\in A\big)\sim \frac{\mathrm{cap}(A)}{|x|},$$
and for a discrete set $A\subset\mathbb{Z}^3$ the lattice capacity is $\mathrm{cap}_{\mathbb{Z}^3}(A)=\sum_{x\in A}\mathbb{P}_x(\text{SRW never returns to }A)$.

**Kernel normalisations.** For simple random walk on $\mathbb{Z}^3$ the Green function satisfies $G(0,x)\sim \frac{3}{2\pi|x|}$, so lattice and continuum capacities differ by the factor $2\pi/3$.

**Dimension and gauges.** $\dim_H \mathcal{W}[0,1]=2$ a.s.; the exact gauge is $\varphi(r)=r^2\log\log(1/r)$ (Ciesielski–Taylor / Lévy). A set of dimension $2$ in $\mathbb{R}^3$ has positive $\alpha$-capacity for all $\alpha<2$, in particular $\alpha=1$ (Newtonian), so $\mathcal{C}_3>0$; finiteness is immediate from $\mathrm{cap}(A)\le \mathrm{diam}(A)$.

**Capacity-equivalence (Pemantle–Peres–Shapiro, 1996).** There exist universal $c_1,c_2>0$ such that for *every* gauge function $f$,
$$c_1\,\mathrm{Cap}_f([0,1]^2)\ \le\ \mathbb{E}\big[\mathrm{Cap}_f(\mathcal{W}[0,1])\big]\ \le\ c_2\,\mathrm{Cap}_f([0,1]^2),$$
i.e. the spatial Brownian trace is *capacity-equivalent to the unit square*. This pins the path down up to constants for all potential-theoretic questions — but only up to constants.

**Second-moment (energy) bound.** With $\mu$ the normalised occupation measure of $\mathcal{W}[0,1]$,
$$\mathcal{C}_3 \ \ge\ \frac{1}{I(\mu)},\qquad I(\mu)=\int_0^1\!\!\int_0^1 \frac{ds\,dt}{|W_s-W_t|}.$$

**Lattice link.** If $R_n=\{S_0,\dots,S_n\}$ is the range of SRW on $\mathbb{Z}^3$, then since $S_n\approx W_{n/3}$,
$$\mathrm{cap}_{\mathbb{Z}^3}(R_n)\ \approx\ \frac{2\pi}{3}\sqrt{\tfrac{n}{3}}\;\mathcal{C}_3\ =\ \frac{2\pi}{3\sqrt3}\,\sqrt{n}\,\mathcal{C}_3 .$$

## 3. History & State of the Art (SOTA)

- **1940s–60s.** Kakutani, Dvoretzky–Erdős and Itô–McKean establish transience, dimension $2$, and polarity of points in $d\ge 3$; the path is "large enough" to be non-polar for the Newtonian kernel.
- **Spitzer (1964).** *Electrostatic capacity, heat flow, and Brownian motion*: exact and asymptotic formulas for the expected volume and capacity of the Wiener sausage in $\mathbb{R}^3$, e.g. $\mathbb{E}|\mathcal{W}^a[0,t]|=2\pi a t + 4a^2\sqrt{2\pi t}+\tfrac{4}{3}\pi a^3$. Capacity of the sausage is the natural regularisation of $\mathcal{C}_3$.
- **Le Gall (1988).** Second-order asymptotics and fluctuations of the Wiener sausage volume in $d=3$ ("Sur une conjecture de M. Kac"), fixing the technology (intersection local times) later used for capacity.
- **Pemantle–Peres–Shapiro (1996).** Capacity-equivalence to $[0,1]^2$; Peres (1996) gives the matching intersection-equivalence with a branching random walk / percolation-on-tree model.
- **van den Berg–Bolthausen–den Hollander (2001).** Moderate deviations for the Wiener sausage volume — the template for large-deviation statements about path functionals.
- **Asselah–Schapira–Sousi (2018–2019).** A complete programme for $\mathrm{cap}(R_n)$ on $\mathbb{Z}^d$: LLN and CLT for $d\ge 6$ (Trans. AMS, 2018); the critical dimension $d=4$, where $\mathrm{cap}(R_n)\sim \frac{\pi^2}{8}\,\frac{n}{\log n}$ (Ann. Probab., 2019), with the Wiener-sausage analogue in PTRF (2019); dimension $5$ treated separately with non-Gaussian corrections.
- **$d=3$.** Here $\mathrm{cap}(R_n)\asymp \sqrt n$ and the correct statement is *convergence in law*, not an LLN: $n^{-1/2}\mathrm{cap}(R_n)\Rightarrow \frac{2\pi}{3\sqrt3}\mathcal{C}_3$. The limit is genuinely random, which is exactly why no constant is available.

## 4. Partial Results / Verified Cases

- **$d\ge 5$ (lattice).** $\mathrm{cap}(R_n)/n\to \gamma_d>0$ a.s., with $\gamma_d$ an explicit escape probability; CLT with Gaussian limit for $d\ge 6$, and non-Gaussian correction terms in $d=5$ (Asselah–Schapira–Sousi).
- **$d=4$ (critical).** $\frac{\log n}{n}\mathrm{cap}(R_n)\to \frac{\pi^2}{8}$ a.s.; the same constant appears for the Wiener sausage $\mathrm{cap}(\mathcal{W}^a[0,t])\sim 8\pi^2 t/\log t$ up to normalisation.
- **$d=3$, order of magnitude.** $\mathrm{cap}(\mathcal{W}[0,t])=\sqrt t\,\mathcal{C}_3$ exactly (scaling), and $0<\mathcal{C}_3<\infty$ a.s.
- **$d=3$, two-sided constants.** Capacity-equivalence to $[0,1]^2$ gives $c_1\le \mathbb{E}[\mathcal{C}_3]\le c_2$ with explicit but far-apart $c_1,c_2$; the energy bound of §10 gives the clean rigorous $\mathbb{E}[\mathcal{C}_3]\ge \tfrac38\sqrt{\pi/2}\approx 0.4700$.
- **Moments and tails, qualitative.** $\mathcal{C}_3\le \sup_{t\le 1}|W_t|$ gives all moments finite and a Gaussian-type upper tail $\mathbb{P}(\mathcal{C}_3>\lambda)\le e^{-c\lambda^2}$; the lower tail is controlled by small-ball estimates, $\mathbb{P}(\mathcal{C}_3<\varepsilon)\le \exp(-c/\varepsilon^{2})$ up to constants.
- **Related exactly-solved functional.** For the Wiener sausage in $d=3$, $\mathbb{E}[\text{volume}]$ is known exactly (Spitzer); no analogous exact formula is known for $\mathbb{E}[\mathrm{cap}]$.

## 5. Principal Obstacles

- **No additivity.** Volume and occupation measures are additive: $\mathbb{E}|\mathcal{W}^a[0,t]|$ splits over time increments. Capacity is only sub-additive, $\mathrm{cap}(A\cup B)\le \mathrm{cap}(A)+\mathrm{cap}(B)$, with a defect governed by the mutual energy. Every exact computation in the field (Spitzer, Kac, Le Gall) uses additivity; it is unavailable here.
- **The equilibrium measure is not explicit.** $\mathcal{C}_3$ is the total mass of the equilibrium measure of a fractal, self-intersecting set. There is no Markovian description of that measure along the path: the harmonic measure at time $s$ depends on the whole path, both past and future.
- **Variational bounds are loose in both directions.** The energy lower bound uses the occupation measure, which is a poor approximation to equilibrium (it charges the deep interior, which carries almost no charge). Upper bounds via covering or via the enclosing ball throw away the two-dimensional structure. The two families do not converge to each other.
- **Critical logarithms are absent.** In $d=4$ the answer is driven by a single divergent sum $\sum_m 1/m$, and the constant $\pi^2/8$ is a mean-field computation. In $d=3$ the corresponding sum $\sum_m m^{-1/2}$ is dominated by the *macroscopic* scale, so the answer is a genuine functional of the whole Brownian path — mean-field is not asymptotically exact.
- **Non-self-averaging.** Because $\mathcal{C}_3$ is random and not concentrated, there is no LLN to extract a constant from; one must compute the law of a nonlinear functional of a path, a problem class where exact answers (Lévy's arcsine law, Kac's formulas) exist only when a PDE representation is available. No PDE for capacity is known.

## 6. The Gap

Proven: $\mathrm{cap}(\mathcal{W}[0,t])=\sqrt{t}\,\mathcal{C}_3$ with $\mathcal{C}_3\in(0,\infty)$, plus two-sided constants and a full lattice theory in $d\ge 4$.

Wanted: the distribution of $\mathcal{C}_3$, or at minimum $\mathbb{E}[\mathcal{C}_3]$.

The precise missing step is a **tractable representation of the equilibrium measure of the Brownian trace**. In $d\ge 5$ one writes $\mathrm{cap}(R_n)=\sum_x \mathbb{P}_x(\text{no return})$ and the summands decorrelate; in $d=4$ the correlations produce exactly one logarithm and mean-field is exact. In $d=3$ the escape probability from a point of the path is an $O(1)$-order functional of the entire path, so the sum does not factorise at any order. Crossing the gap requires either (a) a stochastic-calculus identity expressing $\mathcal{C}_3$ as an additive functional plus a controllable remainder, or (b) an exactly solvable branching/tree model that is *equal* to — not merely equivalent up to constants with — the Brownian trace.

## 7. Current Research (as of June 2026)

- **Asselah–Schapira–Sousi school (Paris-Est Créteil, Aix-Marseille, Cambridge).** Deviation theory for the capacity of the range: moderate and large deviations, and the "swelling/folding" phase transition (the shape of the range conditioned on atypically small capacity). Techniques: last-exit decompositions and a Lyapunov-type sub-additivity.
- **Precise fluctuation theory in $d=3$.** Identifying the limit law of $n^{-1/2}\mathrm{cap}(R_n)$ with $\frac{2\pi}{3\sqrt3}\mathcal{C}_3$ including the invariance-principle error rate, and the small-$a$ expansion $\mathrm{cap}(\mathcal{W}^a[0,1])=\mathcal{C}_3 + \kappa\,(\log(1/a))^{-1}+o((\log(1/a))^{-1})$ *(frontier — verify)*.
- **Random interlacements (Sznitman school, ETH/Zurich, Technion, Cologne).** Capacity of the range is the basic input to interlacement local-set decompositions and to disconnection/cover-time large deviations; sharper $d=3$ constants would sharpen those results.
- **Numerics.** High-precision Monte-Carlo of $\mathrm{cap}_{\mathbb{Z}^3}(R_n)$ with Richardson extrapolation in $n^{-1/2}$ gives $\mathbb{E}[\mathcal{C}_3]$ to a few digits; no published value has been independently reproduced at high precision *(frontier — verify)*.
- **Multifractal / thick-point angle (Dembo–Peres–Rosen–Zeitouni lineage).** Localising where the equilibrium measure lives on the path — conjecturally on the "thin" (few-visit) points — as a route to a representation formula.

## 8. Future Work

- Look for an **Itô-type decomposition** of $t\mapsto \mathrm{cap}(\mathcal{W}[0,t])$: it is increasing and $\sqrt{t}$-scaling, so $d\,\mathrm{cap}$ should be a positive additive functional supported on the boundary of the path. Identifying this functional (an analogue of local time on the "outer boundary") is the most direct route to $\mathbb{E}[\mathcal{C}_3]$.
- **Sharpen capacity-equivalence to capacity-asymptotics**: find the constant $\theta$ with $\mathcal{C}_3 \stackrel{?}{=} \theta\cdot(\text{explicit functional of a branching random walk})$, upgrading Peres's intersection-equivalence from $\asymp$ to $\sim$.
- **Transfer the $d=4$ mean-field method downward** by working with the capacity of the range restricted to a dyadic scale and summing scales — a multi-scale renormalisation whose fixed point would encode $\mathcal{C}_3$.
- **Rigorous numerics**: certified upper and lower bounds via finite-element solution of the exterior Dirichlet problem on sampled polygonal approximations, with proven discretisation error, to bracket $\mathbb{E}[\mathcal{C}_3]$ to two digits.
- Determine whether $\mathcal{C}_3$ is **absolutely continuous** and whether its law satisfies a distributional fixed-point (smoothing) equation coming from the Brownian scaling/decomposition at an independent split time.

## 9. Key References

- **[Foundational]** F. Spitzer. *Electrostatic capacity, heat flow, and Brownian motion.* Zeitschrift für Wahrscheinlichkeitstheorie und verwandte Gebiete, 3:110–121, 1964.
- **[Foundational]** S. C. Port and C. J. Stone. *Brownian Motion and Classical Potential Theory.* Academic Press, 1978.
- **[Foundational]** J.-F. Le Gall. *Sur une conjecture de M. Kac.* Probability Theory and Related Fields, 78:389–402, 1988.
- **[Key structural]** R. Pemantle, Y. Peres, and J. W. Shapiro. *The trace of spatial Brownian motion is capacity-equivalent to the unit square.* Probability Theory and Related Fields, 106:379–399, 1996.
- **[Key structural]** Y. Peres. *Intersection-equivalence of Brownian paths and certain branching processes.* Communications in Mathematical Physics, 177:417–434, 1996.
- **[SOTA]** A. Asselah, B. Schapira, and P. Sousi. *Capacity of the range of random walk on $\mathbb{Z}^d$.* Transactions of the American Mathematical Society, 370, 2018.
- **[SOTA]** A. Asselah, B. Schapira, and P. Sousi. *Capacity of the range of random walk on $\mathbb{Z}^4$.* Annals of Probability, 47, 2019.
- **[SOTA]** A. Asselah, B. Schapira, and P. Sousi. *Strong law of large numbers for the capacity of the Wiener sausage in dimension four.* Probability Theory and Related Fields, 173, 2019.
- **[Related]** M. van den Berg, E. Bolthausen, and F. den Hollander. *Moderate deviations for the volume of the Wiener sausage.* Annals of Mathematics, 153:355–406, 2001.
- **[Survey / Book]** P. Mörters and Y. Peres. *Brownian Motion.* Cambridge University Press, 2010 (Chapters 8–10: capacity, dimension, intersections).
- **[Survey / Book]** G. F. Lawler. *Intersections of Random Walks.* Birkhäuser, 1991.
- **[Related]** A.-S. Sznitman. *Brownian Motion, Obstacles and Random Media.* Springer, 1998.

## 10. Worked Example / Concrete Special Case

**A rigorous numerical lower bound for $\mathbb{E}[\mathcal{C}_3]$.**

Take $\mu$ = normalised occupation measure of $\mathcal{W}[0,1]$, i.e. $\mu(f)=\int_0^1 f(W_t)\,dt$. It is a probability measure supported on the trace, so $\mathcal{C}_3\ge 1/I(\mu)$ with
$$I(\mu)=\int_0^1\!\!\int_0^1\frac{ds\,dt}{|W_s-W_t|}.$$

Compute $\mathbb{E}[I(\mu)]$. For $u>0$, $W_u\stackrel{d}{=}\sqrt u\,Z$ with $Z$ standard Gaussian in $\mathbb{R}^3$, and
$$\mathbb{E}\Big[\frac{1}{|Z|}\Big]=\int_{\mathbb{R}^3}\frac{1}{|z|}\frac{e^{-|z|^2/2}}{(2\pi)^{3/2}}dz=\frac{4\pi}{(2\pi)^{3/2}}\int_0^\infty r e^{-r^2/2}dr=\sqrt{\tfrac{2}{\pi}} .$$
Hence $\mathbb{E}\big[|W_s-W_t|^{-1}\big]=\sqrt{2/\pi}\;|t-s|^{-1/2}$, and
$$\mathbb{E}[I(\mu)]=\sqrt{\tfrac{2}{\pi}}\int_0^1\!\!\int_0^1|t-s|^{-1/2}ds\,dt=\sqrt{\tfrac{2}{\pi}}\cdot 2\int_0^1 (1-u)u^{-1/2}du=\sqrt{\tfrac{2}{\pi}}\cdot 2\Big(2-\tfrac23\Big)=\frac{8}{3}\sqrt{\tfrac{2}{\pi}} .$$
Numerically $\mathbb{E}[I(\mu)]=2.1277\ldots$. By Jensen ($x\mapsto 1/x$ convex),
$$\mathbb{E}[\mathcal{C}_3]\ \ge\ \mathbb{E}\Big[\frac{1}{I(\mu)}\Big]\ \ge\ \frac{1}{\mathbb{E}[I(\mu)]}=\frac{3}{8}\sqrt{\frac{\pi}{2}}=0.46997\ldots$$

**Upper bound.** $\mathcal{W}[0,1]\subset \bar B(0,R)$ with $R=\sup_{t\le 1}|W_t|$, and capacity is monotone with $\mathrm{cap}(\bar B(0,R))=R$, so $\mathbb{E}[\mathcal{C}_3]\le \mathbb{E}[R]<\infty$ (numerically $\mathbb{E}[R]\approx 1.6$).

So $0.470 \le \mathbb{E}[\mathcal{C}_3]\lesssim 1.6$: a factor of roughly $3.4$ separates the best elementary bounds. Sharper versions of both sides exist, but no argument has closed the interval to a point in sixty years — that gap **is** the open problem.

**Consequence for the lattice.** Using $\mathrm{cap}_{\mathbb{Z}^3}(R_n)\approx \frac{2\pi}{3\sqrt3}\sqrt n\,\mathcal{C}_3$ with $\frac{2\pi}{3\sqrt3}=1.2092$, the bound above predicts $\mathbb{E}[\mathrm{cap}_{\mathbb{Z}^3}(R_n)]\ge 0.568\sqrt n$ asymptotically — e.g. at $n=10^6$, at least $568$ units of capacity out of the $\approx 10^6$ visited sites, showing how severely screening reduces the naive count. Contrast $d=4$, where the same computation is asymptotically *exact* and yields $\mathbb{E}[\mathrm{cap}(R_n)]\sim \frac{\pi^2}{8}\frac{n}{\log n}$.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*