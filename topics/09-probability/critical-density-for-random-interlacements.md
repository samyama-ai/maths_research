---
id: 09-probability/critical-density-for-random-interlacements
title: "Critical Density for Random Interlacements"
topic: 09-probability
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Critical Density for Random Interlacements

> **Topic:** Probability & Stochastic Processes · **ID:** `09-probability/critical-density-for-random-interlacements` · **Status:** open

## 1. Problem Statement / Conjecture

Random interlacements at level $u>0$ is a Poissonian soup $\mathcal{I}^u$ of doubly-infinite simple random walk trajectories on $\mathbb{Z}^d$, $d\ge 3$. Its complement $\mathcal{V}^u = \mathbb{Z}^d\setminus\mathcal{I}^u$, the **vacant set**, undergoes a percolation phase transition at a critical density $u_*(d)$.

Two critical parameters are defined:

$$u_*(d) \;=\; \inf\{u\ge 0:\ \mathbb{P}[0 \leftrightarrow \infty \text{ in } \mathcal{V}^u]=0\},$$

$$u_{**}(d) \;=\; \inf\Big\{u\ge 0:\ \lim_{L\to\infty}\mathbb{P}\big[B_L \leftrightarrow \partial B_{2L} \text{ in } \mathcal{V}^u\big]=0\Big\}.$$

Trivially $u_*\le u_{**}$. The central open problems are:

1. **(Sharpness)** Prove $u_*(d)=u_{**}(d)$ for every $d\ge 3$ — i.e. the transition has no intermediate phase in which the vacant set has no infinite cluster but crossing probabilities of annuli do not vanish.
2. **(Value / asymptotics)** Determine $u_*(d)$, or sharp non-asymptotic bounds. Only $u_*(d)/\log d \to 1$ as $d\to\infty$ is known.
3. **(Behaviour at $u_*$)** Show $\theta(u_*)=\mathbb{P}[0\leftrightarrow\infty\ \text{in}\ \mathcal{V}^{u_*}]=0$ (no percolation at criticality) and identify the critical exponents.

A complete solution to (1) means a proof (or a counterexample construction) valid for all $d\ge 3$ on $\mathbb{Z}^d$; partial results on trees or on $G\times\mathbb{Z}$ do not suffice.

## 2. Mathematical Foundations

Let $d\ge 3$ and let $(X_n)$ be simple random walk on $\mathbb{Z}^d$ with Green function

$$g(x,y)=\sum_{n\ge 0}P_x[X_n=y],\qquad g(x,y)\sim c_d|x-y|^{2-d},\quad c_d=\tfrac{d}{2}\Gamma(\tfrac d2-1)\pi^{-d/2}.$$

For finite $K\subset\mathbb{Z}^d$, the **equilibrium measure** and **capacity** are

$$e_K(x)=P_x[\widetilde H_K=\infty]\,\mathbf 1_{x\in K},\qquad \mathrm{cap}(K)=\sum_{x\in K}e_K(x),$$

with $\widetilde H_K$ the hitting time of $K$ after time $1$.

Let $W^*$ be the space of doubly-infinite transient trajectories modulo time-shift, carrying the $\sigma$-finite intensity measure $\nu$ of Sznitman. Random interlacements is the Poisson point process $\omega=\sum_i\delta_{(w_i^*,u_i)}$ on $W^*\times\mathbb{R}_+$ with intensity $\nu\otimes du$, and

$$\mathcal I^u(\omega)=\bigcup_{u_i\le u}\mathrm{range}(w_i^*),\qquad \mathcal V^u=\mathbb{Z}^d\setminus\mathcal I^u.$$

The defining identity — which characterizes the law uniquely — is

$$\boxed{\ \mathbb{P}\big[\mathcal I^u\cap K=\emptyset\big]=e^{-u\,\mathrm{cap}(K)}\ }\qquad\text{for all finite }K\subset\mathbb{Z}^d.$$

Special cases: $\mathrm{cap}(\{0\})=1/g(0,0)$, so the **vacant density** is $\mathbb{P}[0\in\mathcal V^u]=e^{-u/g(0,0)}$; and $\mathrm{cap}(\{x,y\})=2/\big(g(0,0)+g(x,y)\big)$, giving

$$\mathrm{Cov}\big(\mathbf 1_{x\in\mathcal V^u},\mathbf 1_{y\in\mathcal V^u}\big)\;\asymp\; u\,|x-y|^{-(d-2)}\,e^{-2u/g(0,0)}\quad (|x-y|\to\infty).$$

The family $(\mathcal V^u)_{u>0}$ is decreasing in $u$, ergodic under lattice translations, and satisfies the FKG inequality (Teixeira, 2009). The **isomorphism theorem** (Sznitman, 2012; Lupu, 2016) couples $\mathcal I^u$ with the discrete Gaussian free field $\varphi$: for the field $\ell_{x,u}$ of interlacement local times,

$$\big(\ell_{x,u}+\tfrac12\varphi_x^2\big)_{x}\ \stackrel{d}{=}\ \big(\tfrac12(\varphi_x+\sqrt{2u})^2\big)_{x},$$

linking $u_*$ to the GFF level-set critical parameters $h_*, h_{**}$.

## 3. History & State of the Art (SOTA)

- **2007–2010, origin.** Sznitman introduced random interlacements to describe the local picture left by random walk on the discrete torus $(\mathbb{Z}/N\mathbb{Z})^d$ and on the cylinder $(\mathbb{Z}/N\mathbb{Z})^d\times\mathbb{Z}$ at times of order $uN^d$ (*Vacant set of random interlacements and percolation*, Ann. of Math. 171, 2010). He proved $u_*(d)<\infty$ for all $d\ge3$ and $u_*(d)>0$ for $d\ge7$.
- **2009, non-degeneracy in all dimensions.** Sidoravicius–Sznitman (CPAM 62) proved $u_*(d)>0$ for every $d\ge3$, via a multi-scale renormalization on the interlacement trajectories.
- **2009, uniqueness.** Teixeira (Ann. Appl. Probab. 19) proved that the infinite vacant cluster, when it exists, is a.s. unique — the Burton–Keane argument survives the long-range correlations.
- **2011, high dimensions.** Sznitman (Ann. Probab. 39) proved $u_*(d)=\log d\,(1+o(1))$ as $d\to\infty$, the only sharp asymptotic known.
- **2011–2015, decoupling technology.** Sznitman's decoupling inequalities on $G\times\mathbb{Z}$ (Invent. Math. 187, 2012) and Popov–Teixeira's **soft local times** (JEMS 17, 2015) gave the flexible tools that drive nearly all subsequent renormalization arguments.
- **2020–2023, sharpness for the GFF.** Duminil-Copin, Goswami, Rodriguez, Severo proved $h_*=h_{**}$ for GFF level sets on $\mathbb{Z}^d$, $d\ge3$ (Duke Math. J. 172, 2023), the closest analogue of the interlacement conjecture; the transfer to $u_*=u_{**}$ via isomorphism remains incomplete.
- **Status.** $u_*=u_{**}$ on $\mathbb{Z}^d$ is open for every $d\ge3$. No dimension has a proven numerical value of $u_*$.

## 4. Partial Results / Verified Cases

- **Non-degeneracy, all $d\ge3$:** $0<u_*(d)\le u_{**}(d)<\infty$ (Sznitman 2010; Sidoravicius–Sznitman 2009).
- **Regular trees:** on the $(d+1)$-regular tree, the vacant set is a branching process and $u_*$ is explicit,
  $$u_*(\mathbb T_d)=\frac{d(d-1)\log(d-1)}{(d-2)^2},$$
  with $u_*=u_{**}$ (Teixeira, *Interlacement percolation on transient weighted graphs*, EJP 14, 2009). On trees $\theta(u_*)=0$ and mean-field exponents hold.
- **Transient graphs with mean-field geometry:** Drewitz, Prévost, Rodriguez (Invent. Math. 232, 2023) established equality of critical parameters and critical exponents ($\theta(u)\asymp (u_*-u)$, one-arm exponent $2$) for interlacements and GFF level sets on a class of transient graphs including trees times $\mathbb{Z}$-like structures and graphs with sufficiently spread-out Green function.
- **Product graphs $G\times\mathbb{Z}$:** $0<u_*<\infty$ whenever $G$ is a suitable transient weighted graph (Sznitman, Invent. Math. 187, 2012).
- **High dimension:** $u_*(d)/\log d\to1$; furthermore $u_{**}(d)/\log d\to 1$, so the two parameters agree *asymptotically* in $d$ (Sznitman 2011).
- **Supercritical regime $u<u_*$:** local uniqueness, chemical-distance and shape theorems for the vacant cluster hold for $u$ small (Drewitz–Ráth–Sapozhnikov, J. Math. Phys. 53, 2012; AIHP 2014).
- **Subcritical regime $u>u_{**}$:** stretched-exponential decay $\mathbb{P}[0\leftrightarrow\partial B_L]\le e^{-cL^{\varepsilon}}$ (Sznitman 2012; Popov–Teixeira 2015).
- **Torus:** for random walk on $(\mathbb{Z}/N\mathbb{Z})^d$ run for $uN^d$ steps, the vacant set undergoes a transition at the same $u_*$ up to the $u_*$ vs. $u_{**}$ gap (Teixeira–Windisch, CPAM 64, 2011).

## 5. Principal Obstacles

- **Correlations are not summable.** $\mathrm{Cov}\asymp|x-y|^{-(d-2)}$ and $\sum_{x}|x|^{-(d-2)}=\infty$ in every dimension. The Liggett–Schonmann–Stacey domination theorem, which converts finite-range or summably-correlated fields into independent Bernoulli percolation, does not apply. Every comparison with Bernoulli site percolation on $\mathbb{Z}^d$ fails at the first step.
- **No BK inequality, no Russo formula in usable form.** The interlacement measure is not a product measure; the van den Berg–Kesten inequality is unavailable, and the differential inequalities of Menshikov / Aizenman–Barsky / Duminil-Copin–Tassion (which give sharpness in Bernoulli percolation) have no direct analogue because $u$ does not act as an independent-resampling parameter site by site.
- **Renormalization loses a window.** Multi-scale schemes (Sznitman's decoupling, Popov–Teixeira soft local times) require a **sprinkling** $u\to u(1+\varepsilon_k)$ at each scale $k$, with $\sum_k\varepsilon_k>0$. The total sprinkling cost is bounded below by a strictly positive constant, so renormalization proves statements for $u<(1-\delta)u_{**}$ but never up to $u_{**}$ itself — precisely the gap the conjecture asks to close.
- **Isomorphism transfer is one-directional.** The Sznitman–Lupu isomorphism relates $\{\varphi>h\}$ to $\mathcal V^u$ only after integrating over an independent field; monotone events do not transfer cleanly, so the GFF sharpness proof (which uses the field's Gaussian structure, Markov property and continuity in $h$) does not port to interlacements, where $u$ enters through capacity rather than a Gaussian tilt.
- **No exact solvability, no explicit $u_*$.** Unlike Bernoulli percolation in $d=2$, there is no duality, no conformal-invariance input, and $\mathbb{Z}^d$ interlacements are genuinely $d\ge3$ objects, so two-dimensional exact methods are simply absent.

## 6. The Gap

Proven: $0<u_*\le u_{**}<\infty$, stretched-exponential decay strictly above $u_{**}$, and strong supercritical structure strictly below $u_*$. Unproven: that the interval $[u_*,u_{**}]$ is a single point.

The exact missing step is a **sprinkling-free renormalization**, or equivalently: show that for $u<u_{**}$ the annulus-crossing probability $\mathbb{P}[B_L\leftrightarrow\partial B_{2L}\ \text{in}\ \mathcal V^u]$ staying bounded away from $0$ forces an infinite cluster at the *same* level $u$, without paying $\varepsilon>0$ of intensity. In Bernoulli percolation this is the content of sharpness (Menshikov 1986); here it requires either (a) a differential inequality in $u$ for $\theta(u)$ valid for the correlated field, or (b) a monotone coupling absorbing the sprinkling cost, e.g. by exploiting the exact exponential–capacity formula.

## 7. Current Research (as of June 2026)

- **Sharpness transfer from the GFF.** The Geneva/IHES school (Duminil-Copin, Severo) and collaborators (Goswami, Rodriguez) continue to push the $h_*=h_{**}$ machinery — interpolation schemes and the "OSSS/randomized-algorithm" toolbox for Gaussian fields — toward interlacements. A direct interlacement analogue is the most-cited target. *(frontier — verify)*
- **Critical exponents on transient graphs.** Drewitz (Cologne), Prévost (Geneva/Luxembourg), Rodriguez (Warwick) extend the Invent. Math. 2023 framework to broader Green-function regimes, aiming at an upper critical dimension statement for interlacements. *(frontier — verify)*
- **Disconnection and large deviations.** Sznitman and Nitzschner (ETH/HKUST) study the cost of disconnecting a macroscopic body by $\mathcal I^u$; the large-deviation rate functions are governed by $u_{**}$-type parameters and give indirect information on the gap (Nitzschner–Sznitman, JEMS 22, 2020).
- **Late points and cover times.** Prévost, Rodriguez, Sousi relate the set of late points of random walk on the torus to $\mathcal V^u$, transporting any resolution of the gap into cover-time asymptotics.
- **Numerics.** Simulation estimates in $d=3$ place $u_*$ near $3$; no rigorous numeric bracket exists, and published estimates are not of certified accuracy. *(frontier — verify)*

## 8. Future Work

- Develop a **Duminil-Copin–Tassion-style** two-parameter argument adapted to capacity: find a functional $\varphi_u(S)$ over finite sets $S$ whose positivity forces $\theta(u)>0$, replacing the product-measure Russo derivative by the derivative of $e^{-u\,\mathrm{cap}(\cdot)}$ in $u$.
- Establish a **monotone coupling** of $\mathcal V^{u(1+\varepsilon)}$ inside $\mathcal V^u$ with cost vanishing as the renormalization scale grows — the direct route to eliminating sprinkling.
- Prove **continuity at criticality**, $\theta(u_*)=0$, for $d\ge3$; this is unknown even given $u_*=u_{**}$.
- Determine the **upper critical dimension** $d_c$ above which interlacement percolation has mean-field exponents; the tree results suggest $d_c=6$ by analogy with Bernoulli percolation, but no lace expansion exists for interlacements.
- Settle **monotonicity of $u_*(d)$ in $d$**, and improve the $\log d$ asymptotics to second order.

## 9. Key References

- **[Foundational]** A.-S. Sznitman. *Vacant set of random interlacements and percolation.* Annals of Mathematics, 171(2):2039–2087, 2010.
- **[Foundational]** V. Sidoravicius, A.-S. Sznitman. *Percolation for the vacant set of random interlacements.* Communications on Pure and Applied Mathematics, 62(6):831–858, 2009.
- **[Foundational]** A. Teixeira. *Interlacement percolation on transient weighted graphs.* Electronic Journal of Probability, 14:1604–1628, 2009.
- **[Foundational]** A. Teixeira. *On the uniqueness of the infinite cluster of the vacant set of random interlacements.* Annals of Applied Probability, 19(1):454–466, 2009.
- **[SOTA]** A.-S. Sznitman. *On the critical parameter of interlacement percolation in high dimension.* Annals of Probability, 39(1):70–103, 2011.
- **[SOTA]** A.-S. Sznitman. *Decoupling inequalities and interlacement percolation on $G\times\mathbb{Z}$.* Inventiones Mathematicae, 187(3):645–706, 2012.
- **[SOTA]** S. Popov, A. Teixeira. *Soft local times and decoupling of random interlacements.* Journal of the European Mathematical Society, 17(10):2545–2593, 2015.
- **[SOTA / Recent]** H. Duminil-Copin, S. Goswami, P.-F. Rodriguez, F. Severo. *Equality of critical parameters for percolation of Gaussian free field level sets.* Duke Mathematical Journal, 172(5):839–913, 2023.
- **[SOTA / Recent]** A. Drewitz, A. Prévost, P.-F. Rodriguez. *Critical exponents for a percolation model on transient graphs.* Inventiones Mathematicae, 232:229–299, 2023.
- **[Isomorphism]** A.-S. Sznitman. *Random interlacements and the Gaussian free field.* Annals of Probability, 40(6):2400–2438, 2012. — T. Lupu. *From loop clusters and random interlacements to the free field.* Annals of Probability, 44(3):2117–2146, 2016.
- **[Survey / Book]** A. Drewitz, B. Ráth, A. Sapozhnikov. *An Introduction to Random Interlacements.* SpringerBriefs in Mathematics, Springer, 2014.
- **[Survey]** J. Černý, A. Teixeira. *From Random Walk Trajectories to Random Interlacements.* Ensaios Matemáticos, vol. 23, Sociedade Brasileira de Matemática, 2011.

## 10. Worked Example / Concrete Special Case

**Setting: $d=3$.** The return probability of SRW on $\mathbb{Z}^3$ is $p_{\mathrm{ret}}=0.340537\ldots$ (Watson's integral), so

$$g(0,0)=\frac{1}{1-p_{\mathrm{ret}}}=1.516386\ldots,\qquad \mathrm{cap}(\{0\})=\frac{1}{g(0,0)}=0.659463\ldots$$

**Vacant density.** $\ \mathbb{P}[0\in\mathcal V^u]=e^{-0.659463\,u}$. Numerically:

| $u$ | vacant density |
|---|---|
| $1$ | $0.5172$ |
| $2$ | $0.2675$ |
| $3$ | $0.1383$ |

Bernoulli site percolation on $\mathbb{Z}^3$ has $p_c^{\mathrm{site}}\approx0.3116$. If $\mathcal V^u$ were an i.i.d. field, percolation would stop at density $0.3116$, i.e. at $u\approx 1.767$. Simulations put $u_*(3)$ near $3$, i.e. at density $\approx0.138$ — less than half of $p_c^{\mathrm{site}}$. The long-range positive correlations of $\mathcal V^u$ therefore *help* percolation substantially, which is exactly why no comparison argument with independent percolation can locate $u_*$.

**Why correlations block the standard proof.** Using $\mathrm{cap}(\{0,x\})=2/(g(0,0)+g(0,x))$ and $g(0,x)\simeq \tfrac{3}{2\pi|x|}$ in $d=3$:

$$\mathbb{P}[0,x\in\mathcal V^u]=\exp\!\Big(\!-\frac{2u}{g(0,0)+g(0,x)}\Big),\qquad \mathrm{Cov}\simeq \frac{2u\,g(0,x)}{g(0,0)^2}\,e^{-2u/g(0,0)}.$$

At $u=1$, $|x|=10$: $g(0,x)\approx0.0477$, $\mathrm{Cov}\approx 0.0111$. Summing over the sphere of radius $r$ ($\asymp r^2$ sites, covariance $\asymp r^{-1}$) gives a contribution $\asymp r$ — divergent. The correlation field is not summable, so Liggett–Schonmann–Stacey domination is unavailable and one is forced into multi-scale renormalization with sprinkling.

**Where the gap appears.** A renormalization at scales $L_k=\ell_0^k$ proves: if the crossing probability at scale $L_0$ is small enough, then for $u'=u\prod_k(1+\varepsilon_k)$ crossings die out at all scales. Since $\prod_k(1+\varepsilon_k)=1+\delta$ with $\delta>0$ fixed, this yields $u_{**}\le (1+\delta)u_*$ — a *bounded ratio*, never equality. Closing the factor $(1+\delta)$ is the whole problem.

**Contrast: the tree, where it is solved.** On the $4$-regular tree ($d=3$ in the formula of Section 4), $u_*=\frac{3\cdot2\log 2}{1}=6\log 2\approx4.159$, and $u_*=u_{**}$ with $\theta(u_*)=0$, because the vacant set there is an explicit subcritical/supercritical branching process with mean offspring $ (d-1)e^{-u(d-2)^2/(d(d-1))}$, crossing $1$ exactly at $u_*$. The Euclidean lattice has no such exact recursion.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*