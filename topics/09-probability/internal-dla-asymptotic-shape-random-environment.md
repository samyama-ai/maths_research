---
id: 09-probability/internal-dla-asymptotic-shape-random-environment
title: "Asymptotic Shape of IDLA in Random Environments"
topic: 09-probability
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Asymptotic Shape of IDLA in Random Environments

> **Topic:** Probability & Stochastic Processes · **ID:** `09-probability/internal-dla-asymptotic-shape-random-environment` · **Status:** open

## 1. Problem Statement / Conjecture

Internal diffusion-limited aggregation (IDLA) grows a random set by releasing particles one at a time from the origin; each performs a random walk until it reaches a site not yet occupied, where it stops. On $\mathbb{Z}^d$ with simple random walk, Lawler–Bramson–Griffeath (1992) proved the occupied set of $n$ particles, rescaled by $n^{-1/d}$, converges a.s. to a Euclidean ball.

**The problem.** Let $\omega$ be a random environment on $\mathbb{Z}^d$ — i.i.d. or ergodic edge conductances, a supercritical percolation cluster, or a random walk in random environment (RWRE) — sampled once and then frozen. Run IDLA using the environment's walk.

- **(A) Quenched shape theorem.** For $\mathbb{P}$-a.e. $\omega$, does $n^{-1/d} A_n(\omega) \to \mathcal{S}$ a.s., and is $\mathcal{S}$ the ellipsoid $\{x : x^{\mathsf T}\Sigma^{-1}x \le r^2\}$ determined by the homogenized diffusion matrix $\Sigma$ of the environment's walk (a ball when $\Sigma = \sigma^2 I$)?
- **(B) Fluctuations.** Are the inner/outer error radii $O(\mathrm{polylog}\, n)$ as in the homogeneous case, or does frozen environmental noise force a polynomial correction $n^{\alpha}$ with $\alpha>0$ in some dimensions?

A complete solution proves (A) for a general class of ergodic, uniformly elliptic or degenerate-but-integrable environments, identifies $\mathcal{S}$ from $\Sigma$, and settles the fluctuation exponent in (B). A disproof would exhibit an ergodic environment with a non-ellipsoidal or non-deterministic limit shape.

## 2. Mathematical Foundations

**IDLA (Diaconis–Fulton).** Set $A_1 = \{0\}$. Given $A_n$, run an independent walk $(S^{n+1}_k)$ from $0$, let $\tau_{n+1} = \min\{k : S^{n+1}_k \notin A_n\}$, and set
$$A_{n+1} = A_n \cup \{S^{n+1}_{\tau_{n+1}}\},\qquad |A_n| = n .$$
The law of $A_n$ is independent of the order of particle release (abelian property).

**Random conductance model (RCM).** Let $\omega = (\omega_e)_{e \in E(\mathbb{Z}^d)}$ be i.i.d. (or stationary ergodic) positive weights. The walk has generator
$$(\mathcal{L}^\omega f)(x) = \frac{1}{\mu^\omega(x)}\sum_{y \sim x}\omega_{xy}\big(f(y)-f(x)\big),\qquad \mu^\omega(x)=\sum_{y\sim x}\omega_{xy},$$
reversible w.r.t. $\mu^\omega$. Supercritical bond percolation is the degenerate case $\omega_e \in \{0,1\}$, $\mathbb{P}(\omega_e=1)=p>p_c(d)$, restricted to the infinite cluster $\mathcal{C}_\infty$ of density $\theta(p)$.

**Quenched invariance principle (QIP).** Under uniform ellipticity, or $\mathbb{E}[\omega_e]<\infty$ and $\mathbb{E}[\omega_e^{-1}]<\infty$, for a.e. $\omega$ the rescaled walk $\varepsilon S^\omega_{\lfloor t\varepsilon^{-2}\rfloor}$ converges to Brownian motion with nondegenerate covariance $\Sigma = \sigma^2 I$ (isotropy from lattice symmetry of the i.i.d. law). This is the homogenization input: Sidoravicius–Sznitman (2004), Berger–Biskup (2007), Mathieu–Piatnitski (2007), Barlow–Deuschel (2010), Andres–Barlow–Deuschel–Hambly (2013).

**Divisible-sandpile / obstacle-problem heuristic.** The continuum limit of IDLA is the quenched obstacle problem: the odometer $u_n(x)$ (expected number of visits to $x$ by all particles before stopping) satisfies, in the homogenized limit,
$$\tfrac{\sigma^2}{2}\Delta u = \theta(p)^{-1}\mathbf{1}_{A} - n\,\delta_0,\qquad u \ge 0,\ u=0 \text{ off } A,$$
whose noncoincidence set is a ball of volume $n/\theta(p)$ (density correction on percolation clusters, where only cluster sites can be occupied).

**Key martingale.** For $h$ harmonic for $\mathcal{L}^\omega$ on a region and $N^h_n = \sum_{i\le n} h(S^i_{\tau_i}) - n\,h(0)$, $N^h_n$ is a martingale — the Lawler–Bramson–Griffeath mechanism for both inner and outer bounds, now with $\omega$-dependent harmonic functions.

**Fluctuation benchmark (homogeneous case).** With $B_r$ the ball of volume $n$,
$$B_{r-\delta_n^{\mathrm{in}}} \cap \mathbb{Z}^d \subset A_n \subset B_{r+\delta_n^{\mathrm{out}}},\qquad \delta_n^{\mathrm{in}},\delta_n^{\mathrm{out}} = O(\log r)\ (d=2),\ O(\sqrt{\log r})\ (d\ge3),$$
by Jerison–Levine–Sheffield (2012, 2013) and Asselah–Gaudillière (2013), and these orders are sharp.

## 3. History & State of the Art (SOTA)

- **1991.** Diaconis and Fulton introduce the growth model and prove the abelian property.
- **1992.** Lawler, Bramson, Griffeath prove the shape theorem on $\mathbb{Z}^d$, $d\ge 2$: $n^{-1/d}A_n \to$ Euclidean ball a.s., with errors $o(r)$.
- **1995.** Lawler sharpens the errors to $O(r^{1/3}\log^2 r)$ (subdiffusive).
- **2007.** Blachère–Brofferio establish shape theorems on groups of exponential growth, with the limit shape given by balls in the *Green metric*, not the Euclidean one — the first clear signal that the ambient geometry, not the lattice, dictates $\mathcal{S}$.
- **2010.** Shellef obtains the first result in a genuinely random environment: on the supercritical percolation cluster, $A_n$ is "not too spread out" and contains a ball of the right order up to a density of holes.
- **2012–2014.** Jerison–Levine–Sheffield prove logarithmic (and $\sqrt{\log}$ in $d\ge3$) fluctuations and identify the limiting fluctuation field as a variant of the Gaussian free field; Asselah–Gaudillière obtain matching bounds by independent methods.
- **2013.** Duminil-Copin, Lucas, Yadin, Yehudayoff prove the complementary containment on supercritical percolation clusters: for a.e. $\omega$ and every $\varepsilon>0$, $A_n \subset B_{(1+\varepsilon)r_n}$ eventually. Together with Shellef's inner bound this gives the **shape theorem on percolation clusters: the limit is a Euclidean ball of volume $n/\theta(p)$**, with only $o(r)$ error control.
- **2012–2014.** Lucas treats drifted IDLA on $\mathbb{Z}^d$, where the limit shape is a "true heat ball" rather than a Euclidean ball.
- **2017.** Levine–Peres survey the Laplacian-growth family and list quenched fluctuation bounds in random media as open.

**SOTA summary:** shape known (Euclidean, $o(r)$ error) for supercritical percolation; expected but unproven in general ergodic RCM with heavy tails or degenerate conductances; fluctuation order unknown in *every* random environment.

## 4. Partial Results / Verified Cases

| Setting | Result | Reference |
|---|---|---|
| $\mathbb{Z}^d$, $d\ge 2$, SRW | Ball, $o(r)$ error | Lawler–Bramson–Griffeath 1992 |
| $\mathbb{Z}^d$, $d\ge2$ | $\delta_n = O(\log r)$ ($d=2$), $O(\sqrt{\log r})$ ($d\ge3$); sharp | JLS 2012/2013; Asselah–Gaudillière 2013 |
| Supercritical percolation, $p>p_c$, $d\ge2$ | Inner bound (full density) | Shellef 2010 |
| Supercritical percolation, $d\ge2$ | Outer containment $A_n\subset B_{(1+\varepsilon)r}$; shape theorem complete | Duminil-Copin–Lucas–Yadin–Yehudayoff 2013 |
| Uniformly elliptic i.i.d. conductances $0<c_-\le\omega_e\le c_+$ | Shape theorem follows by the same route (QIP + Barlow-type heat-kernel bounds); errors still $o(r)$ | folklore consequence |
| Groups of exponential growth | Green-metric balls | Blachère–Brofferio 2007 |
| Comb lattice, Sierpiński gasket graphs | Explicit non-Euclidean shapes | Huss–Sava 2011, 2013 |
| $\mathbb{Z}^d$ with constant drift | "True heat ball" | Lucas 2014 |

Unproven even at the level of a shape theorem: i.i.d. conductances with $\mathbb{E}[\omega_e^{-1}]=\infty$ (trapping), non-reversible RWRE in $d\ge2$, and environments with only ergodic (non-i.i.d.) laws lacking lattice symmetry, where $\Sigma$ is anisotropic and the predicted shape is an ellipsoid.

## 5. Principal Obstacles

- **Quenched harmonic functions are not explicit.** The LBG proof rests on exact estimates for the SRW Green function $G(x,y)\asymp|x-y|^{2-d}$ and on martingales built from lattice harmonic polynomials. In a random environment, $\mathcal{L}^\omega$-harmonic functions exist only through correctors $\chi(\omega,x)$ with $x \mapsto x-\chi$ harmonic; the corrector is sublinear but not quantitatively so in general.
- **Corrector sublinearity is qualitative.** For percolation and degenerate RCM, $\max_{|x|\le r}|\chi(x)| = o(r)$ is all that is known in general; polynomial or logarithmic rates are available only under strong moment/ellipticity assumptions. Any error term smaller than $o(r)$ needs a quantitative homogenization rate, which is exactly what the shape-theorem error inherits.
- **Traps.** Percolation clusters and heavy-tailed conductances contain dead-ends and low-conductance bottlenecks on all scales. A particle can be delayed for $r^{2+\epsilon}$ steps, breaking uniform-in-$\omega$ hitting-time control; Barlow's Gaussian heat-kernel bounds hold only above a random scale $\mathcal{N}_x(\omega)$ with stretched-exponential tails, so union bounds over $\sim r^d$ sites lose the sharp constants.
- **Two noise sources.** The homogeneous-case log fluctuation is a delicate cancellation of walk noise against the mean curvature of the obstacle problem. Adding a *frozen* noise field changes the variance structure entirely: the environment contributes a correlated, non-refreshing perturbation to the odometer that the JLS martingale/GFF machinery is not designed to absorb.
- **No abelian shortcut.** The abelian property survives, but the divisible-sandpile comparison of Levine–Peres, which gives $O(1)$ smoothness in the homogeneous case, requires an exact discrete mean-value property that a random $\mathcal{L}^\omega$ does not have.

## 6. The Gap

Two distinct gaps.

1. **Class gap.** Proven: percolation and uniformly elliptic i.i.d. weights, with isotropic $\Sigma$ by symmetry. Conjectured: every stationary ergodic environment satisfying a QIP, with the limit shape the $\Sigma$-ellipsoid. The missing step is a shape theorem *derived from a QIP as a black box* — currently every proof also needs quenched Green-function and heat-kernel bounds, which fail for degenerate/heavy-tailed weights.
2. **Precision gap.** Proven: $o(r)$. Conjectured: $\mathrm{polylog}(r)$. Closing this requires transporting a quantitative homogenization rate — e.g. $\|\chi\|_{L^\infty(B_r)} \lesssim r^{\epsilon}$ or $\log r$ — into the LBG martingale argument, and then showing that the frozen environmental fluctuation of the effective conductivity over a ball of radius $r$, of relative size $r^{-d/2}$, displaces the boundary by only $r^{1-d/2}$. Heuristically this is $O(1)$ in $d=2$ and vanishing in $d \ge 3$, so log fluctuations should persist; nobody has made this rigorous *(heuristic — not a theorem)*.

## 7. Current Research (as of June 2026)

- **Quantitative stochastic homogenization applied to growth models.** The Armstrong–Kuusi–Mourrat renormalization framework gives algebraic corrector rates for uniformly elliptic i.i.d. coefficients; several groups are attempting to plug these into the LBG/JLS scheme to upgrade $o(r)$ to $r^{\epsilon}$ in RCM IDLA *(frontier — verify)*.
- **Degenerate conductances.** Andres–Deuschel–Slowik-type moment conditions ($\mathbb{E}[\omega^p]+\mathbb{E}[\omega^{-q}]<\infty$, $1/p+1/q<2/d$) are the natural hypothesis under which a shape theorem is expected; establishing it there is an active target *(frontier — verify)*.
- **Non-reversible RWRE.** IDLA driven by ballistic RWRE in $d\ge 3$ (Sznitman-type conditions), where the limit shape should be a translated ellipsoid; no shape theorem is known.
- **Fluctuation field.** Extending the JLS "IDLA and the Gaussian free field" identification to random media: whether the scaling limit of the boundary fluctuation is still an (augmented) GFF, or acquires an independent environmental component.
- **Related media models.** Random-environment versions of rotor-router aggregation and the divisible sandpile, which are more rigid and may yield the ellipsoid statement first.

## 8. Future Work

- Prove a **black-box theorem**: QIP + volume regularity $\Rightarrow$ shape theorem with limit the $\Sigma$-ellipsoid. This would immediately cover all currently known QIP settings.
- Obtain the first **polynomial-in-$r$ error bound** on the percolation cluster, improving $o(r)$ to $r^{1-\epsilon}$, by combining Barlow's heat kernel bounds with a quantitative corrector estimate.
- Decide whether **environment-induced fluctuations are subdominant** in $d\ge3$ and marginal in $d=2$; a matching lower bound (showing fluctuations are *not* $o(\log r)$ in $d=2$) would be equally informative.
- Construct a **counterexample**: an ergodic (necessarily non-i.i.d., e.g. layered or long-range correlated) environment with anisotropic $\Sigma$, and verify the limit shape is a genuine ellipsoid rather than a ball — confirming that isotropy is an artifact of the i.i.d. lattice symmetry, not of IDLA.
- Study **critical and near-critical** environments (incipient infinite cluster, fractal media), where the walk is subdiffusive with spectral dimension $d_s \ne d$ and the shape should follow the intrinsic/Green metric, as in Blachère–Brofferio.

## 9. Key References

- **[Foundational]** P. Diaconis, W. Fulton. *A growth model, a game, an algebra of Lagrange inversion, and characteristic classes.* Rend. Sem. Mat. Univ. Politec. Torino, 49 (1991), 95–119.
- **[Foundational]** G. Lawler, M. Bramson, D. Griffeath. *Internal diffusion limited aggregation.* Annals of Probability 20 (1992), 2117–2140.
- **[Foundational]** G. Lawler. *Subdiffusive fluctuations for internal diffusion limited aggregation.* Annals of Probability 23 (1995), 71–86.
- **[SOTA]** E. Shellef. *IDLA on the supercritical percolation cluster.* Electronic Journal of Probability 15 (2010), 723–740.
- **[SOTA]** H. Duminil-Copin, C. Lucas, A. Yadin, A. Yehudayoff. *Containing internal diffusion limited aggregation.* Electronic Communications in Probability 18 (2013), paper 50.
- **[SOTA]** D. Jerison, L. Levine, S. Sheffield. *Logarithmic fluctuations for internal DLA.* Journal of the AMS 25 (2012), 271–301.
- **[SOTA]** D. Jerison, L. Levine, S. Sheffield. *Internal DLA in higher dimensions.* Electronic Journal of Probability 18 (2013), paper 98.
- **[SOTA]** D. Jerison, L. Levine, S. Sheffield. *Internal DLA and the Gaussian free field.* Duke Mathematical Journal 163 (2014), 267–308.
- **[SOTA]** A. Asselah, A. Gaudillière. *From logarithmic to subdiffusive polynomial fluctuations for internal DLA and related growth models.* Annals of Probability 41 (2013), 1115–1159.
- **[SOTA]** A. Asselah, A. Gaudillière. *Sublogarithmic fluctuations for internal DLA.* Annals of Probability 41 (2013), 1160–1179.
- **[Structure]** S. Blachère, S. Brofferio. *Internal diffusion limited aggregation on discrete groups having exponential growth.* Probability Theory and Related Fields 137 (2007), 323–343.
- **[Structure]** C. Lucas. *The limiting shape for drifted internal diffusion limited aggregation is a true heat ball.* Probability Theory and Related Fields, 2014.
- **[Structure]** W. Huss, E. Sava. *Internal aggregation models on comb lattices.* Electronic Journal of Probability 16 (2011), 1188–1216.
- **[Tools]** M. Barlow. *Random walks on supercritical percolation clusters.* Annals of Probability 32 (2004), 3024–3084.
- **[Tools]** V. Sidoravicius, A.-S. Sznitman. *Quenched invariance principles for walks on clusters of percolation or among random conductances.* PTRF 129 (2004), 219–244.
- **[Tools]** N. Berger, M. Biskup. *Quenched invariance principle for simple random walk on percolation clusters.* PTRF 137 (2007), 83–120.
- **[Tools]** S. Andres, M. Barlow, J.-D. Deuschel, B. Hambly. *Invariance principle for the random conductance model.* PTRF 156 (2013), 535–580.
- **[Tools]** M. Barlow, J.-D. Deuschel. *Invariance principle for the random conductance model with unbounded conductances.* Annals of Probability 38 (2010), 234–276.
- **[Survey]** L. Levine, Y. Peres. *Laplacian growth, sandpiles, and scaling limits.* Bulletin of the AMS 54 (2017), 355–382.

## 10. Worked Example / Concrete Special Case

**IDLA on $\mathbb{Z}$ with i.i.d. conductances.** Let $\omega_{x,x+1}$ be i.i.d., bounded above and below, with $\rho_x := 1/\omega_{x,x+1}$ (edge resistance), $m = \mathbb{E}[\rho]$, $\mathrm{Var}(\rho)=s^2$. After $n$ particles, $A_n = [-L_n, R_n]\cap\mathbb{Z}$ with $L_n + R_n + 1 = n$.

Each new particle starts at $0$ and, by the electrical-network formula for a reversible walk on an interval, exits at the right end $R_n+1$ with probability
$$p_n = \frac{\mathcal{R}_-}{\mathcal{R}_-+\mathcal{R}_+},\qquad \mathcal{R}_-=\sum_{x=-L_n-1}^{-1}\rho_x,\quad \mathcal{R}_+=\sum_{x=0}^{R_n}\rho_x .$$

*Law of large numbers.* $\mathcal{R}_\pm = m\cdot(\text{length}) + O(\sqrt{n})$ a.s. The dynamics is self-correcting: if $R_n > L_n$ then $\mathcal{R}_+>\mathcal{R}_-$, so $p_n<1/2$ and growth favours the left. Hence $R_n/n \to 1/2$ a.s. and $n^{-1}A_n \to [-\tfrac12,\tfrac12]$ — the shape theorem, with the *same* limit shape as the homogeneous case. The conductances cancel from the shape because the resistance LLN constant $m$ is the same on both sides.

*Where the environment shows up.* The interval stabilizes near the resistance-balance point $R^\ast$ with $\mathcal{R}_-(R^\ast)=\mathcal{R}_+(R^\ast)$. Writing $R^\ast = n/2 + \delta$, a CLT for the partial sums gives $\mathcal{R}_+-\mathcal{R}_- \approx 2m\delta - s\sqrt{n}\,Z$ with $Z$ standard normal, so
$$\delta \approx \frac{s}{2m}\sqrt{n}\,Z .$$
This is a **quenched, frozen** displacement of order $\sqrt{n}$ determined by the environment alone — on top of the $\Theta(\sqrt n)$ walk noise present when $\omega\equiv1$. In $d=1$ both are order $\sqrt n$, so the environment merely inflates the variance constant from the homogeneous value to (walk term) $+\,s^2/4m^2$.

*Scaling up.* Repeating the computation in $d\ge2$: the effective conductivity of a ball of radius $r$ fluctuates by a relative $r^{-d/2}$, and the obstacle problem converts this into a boundary displacement of order $r\cdot r^{-d/2} = r^{1-d/2}$ — $O(1)$ at $d=2$, decaying for $d\ge3$. Compared with the proven homogeneous fluctuations $\Theta(\log r)$ ($d=2$) and $\Theta(\sqrt{\log r})$ ($d\ge3$), this predicts that environmental noise is subdominant and the polylog order survives. Turning this scaling computation into a theorem is precisely the open problem of Section 6(2).

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*