---
id: 09-probability/critical-percolation-intermediate-dimensions
title: "Scaling Limit of Critical Percolation in Dimensions Between Six and Seven"
topic: 09-probability
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Scaling Limit of Critical Percolation in Dimensions Between Six and Seven

> **Topic:** Probability & Stochastic Processes · **ID:** `09-probability/critical-percolation-intermediate-dimensions` · **Status:** open

## 1. Problem Statement / Conjecture

Bernoulli bond percolation on $\mathbb{Z}^d$ is believed to have upper critical dimension $d_c = 6$: for every $d > 6$ the critical cluster should behave as it does on a tree, and its scaling limit should be **integrated super-Brownian excursion (ISE)**, the canonical measure of super-Brownian motion conditioned on total mass one.

**Conjecture.** For every $d > 6$, nearest-neighbour critical percolation on $\mathbb{Z}^d$ satisfies mean-field behaviour: $\beta=1$, $\gamma=1$, $\delta=2$, $\eta=0$, $\nu=1/2$, the triangle diagram is finite at $p_c$, the incipient infinite cluster (IIC) has almost-sure Hausdorff dimension $4$ and spectral dimension $4/3$, and the finite critical clusters, rescaled by volume $n$ and space $n^{1/4}$, converge to ISE.

Proofs currently exist only for $d \ge 11$. The **open regime is $6 < d \le 10$**, and the sharpest form of the question concerns the immediate neighbourhood of $d_c$ — dimensions "between six and seven". Since $\mathbb{Z}^d$ has no non-integer members, the regime $d \in (6,7)$ is made precise through models with a continuously tunable effective dimension: long-range percolation on $\mathbb{Z}^d$ with connection exponent $d+\alpha$ (effective dimension $2d/\alpha$), and hierarchical lattices. A complete resolution must either (i) prove the triangle condition and ISE convergence for all $d>6$ on $\mathbb{Z}^d$, or (ii) exhibit a $d\in(6,10]$ where mean-field behaviour fails; and, in the tunable setting, determine the scaling limit uniformly as the effective dimension decreases to $6^+$, including the conjectured logarithmic corrections at $d_c$ exactly.

## 2. Mathematical Foundations

Let $p\in[0,1]$ and let each edge of $\mathbb{Z}^d$ be open independently with probability $p$. Write $C(x)$ for the open cluster of $x$, and
$$\theta(p)=\mathbb{P}_p(|C(0)|=\infty),\qquad \chi(p)=\mathbb{E}_p|C(0)|,\qquad \tau_p(x)=\mathbb{P}_p(0\leftrightarrow x).$$
The critical point is $p_c=\sup\{p:\theta(p)=0\}$. Critical exponents are defined by
$$\theta(p)\asymp (p-p_c)^{\beta},\quad \chi(p)\asymp (p_c-p)^{-\gamma},\quad \mathbb{P}_{p_c}(|C(0)|\ge n)\asymp n^{-1/\delta},\quad \tau_{p_c}(x)\asymp |x|^{-(d-2+\eta)}.$$

**Triangle diagram.**
$$\nabla(p) \;=\; \sum_{x,y\in\mathbb{Z}^d} \tau_p(0,x)\,\tau_p(x,y)\,\tau_p(y,0) \;=\; \int_{[-\pi,\pi]^d} \hat\tau_p(k)^3 \,\frac{d^dk}{(2\pi)^d}.$$
The **triangle condition** is $\nabla(p_c)<\infty$. If $\tau_{p_c}(x)\asymp|x|^{-(d-2)}$ then $\hat\tau_{p_c}(k)\asymp |k|^{-2}$ and the integral converges iff $d>6$ — this is the analytic origin of $d_c=6$.

**Hyperscaling and its breakdown.** Below $d_c$ one expects $d\nu = 2-\alpha_{\rm heat} = \gamma+2\beta$; mean-field values give $d\nu=d/2$, which equals $\gamma+2\beta=3$ only at $d=6$. Above six, hyperscaling fails and is replaced by $d_c\nu$.

**Scaling limit.** For a finite cluster of volume $n$, let $\mu_n$ be the uniform probability measure on $\{x/(An^{1/4}): x \in C(0)\}$ conditioned on $|C(0)|=n$. ISE convergence asserts $\mu_n \Rightarrow \mathcal{N}_{\rm ISE}$ weakly, where ISE is the occupation measure of the Brownian snake driven by a normalized Brownian excursion. Equivalently, in Fourier space the $r$-point functions converge to the moment measures of ISE:
$$\hat\tau^{(r)}_{p_c}(k_1,\dots,k_{r-1})\; \sim\; \text{(tree sums over binary trees with propagators } |k|^{-2}).$$

**Long-range formalization of non-integer dimension.** On $\mathbb{Z}^d$ let $\{x,y\}$ be open with probability $\approx \beta|x-y|^{-(d+\alpha)}$, $\alpha\in(0,2)$. Then $\hat\tau_{p_c}(k)\asymp|k|^{-\alpha}$, so $\eta=2-\alpha$ and $\nabla(p_c)<\infty$ iff $d>3\alpha$. Matching $\nabla$-convergence thresholds identifies the **effective dimension**
$$d_{\rm eff} \;=\; \frac{2d}{\alpha},$$
which takes every real value; $d_{\rm eff}>6 \iff d>3\alpha$. The conjectured limit is then the $\alpha$-stable analogue of ISE (integrated super-$\alpha$-stable excursion), with volume-to-space exponent $1/\alpha$ in place of $1/2$.

## 3. History & State of the Art (SOTA)

- **1974–1978.** Toulouse identified $d_c=6$ for percolation from hyperscaling; the $6-\epsilon$ expansion of the $q\to1$ Potts model / $\phi^3$ field theory gave the first exponent series. Essam, Gaunt and Guttmann analysed the critical dimension itself and predicted logarithmic corrections at $d=6$.
- **1984.** Aizenman and Newman introduced the triangle condition and proved it implies $\gamma=1$ and $\mathbb{E}|C|<\infty$ control.
- **1987–1991.** Nguyen; Barsky and Aizenman derived $\beta=1$ and $\delta=2$ from the triangle condition; Aizenman–Barsky gave sharpness of the phase transition.
- **1990.** Hara and Slade verified the triangle condition by the **lace expansion** for nearest-neighbour percolation with $d\ge19$, and for spread-out models with $d>6$ and large range $L$.
- **2000.** Hara–Slade proved the ISE scaling limit for spread-out critical percolation with $d>6$, in the sense of convergence of rescaled $r$-point functions.
- **2008–2015.** Heydenreich, van der Hofstad and Sakai extended the lace expansion to long-range models with $d>3(\alpha\wedge2)$; Chen and Sakai obtained sharp $x$-space asymptotics $\tau_{p_c}(x)\asymp|x|^{-(d-\alpha)}$.
- **2009–2011.** Kozma and Nachmias proved the Alexander–Orbach conjecture (spectral dimension $4/3$) and the one-arm exponent $\mathbb{P}(0\leftrightarrow \partial B_r)\asymp r^{-2}$ in high dimensions.
- **2017.** Fitzner and van der Hofstad reduced the nearest-neighbour threshold from $d\ge19$ to $d\ge11$ using the **non-backtracking lace expansion (NoBLE)**. This is still the record.
- **2021–2022.** Hutchcroft gave a largely expansion-free derivation of the mean-field exponents from the triangle condition, and developed hierarchical-lattice methods reaching $d_c$ itself.

## 4. Partial Results / Verified Cases

| Setting | Result | Reference |
|---|---|---|
| $\mathbb{Z}^d$, nearest-neighbour, $d\ge19$ | triangle condition, $\gamma=\beta=1$, $\delta=2$, $\eta=0$ | Hara–Slade 1990 |
| $\mathbb{Z}^d$, nearest-neighbour, $d\ge11$ | same, current record | Fitzner–van der Hofstad 2017 |
| Spread-out, $d>6$, range $L\ge L_0(d)$ | triangle condition, ISE $r$-point convergence, IIC exists | Hara–Slade 2000; van der Hofstad–Járai 2004 |
| Spread-out, $d>6$ | $\tau_{p_c}(x)\sim A|x|^{-(d-2)}$ in $x$-space | Hara 2008 |
| $d\ge11$ (or triangle condition) | spectral dimension $4/3$; one-arm exponent $2$ | Kozma–Nachmias 2009, 2011 |
| Long-range, $\alpha<2$, $d>3\alpha$ (large $\beta$) | mean-field exponents, $\eta=2-\alpha$; covers $d_{\rm eff}\in(6,\infty)$ | Heydenreich–van der Hofstad–Sakai 2008; Chen–Sakai 2015 |
| $d=2$, site percolation on triangular lattice | full conformal scaling limit, $\mathrm{SLE}_6$; exponents $\beta=5/36$, $\eta=5/24$ | Smirnov 2001; Camia–Newman 2006 |
| Infinite regular tree / complete graph | mean-field exact; ISE limit of critical Galton–Watson trees | Aldous 1993 |
| Hierarchical lattice, $d_{\rm eff}>6$ and $=6$ | mean-field exponents; logarithmic corrections at $d_c$ | Hutchcroft 2022 *(frontier — verify)* |

Nothing is proven for $d\in\{3,4,5\}$, and for $d\in\{7,8,9,10\}$ on the nearest-neighbour lattice no mean-field exponent is known.

## 5. Principal Obstacles

- **Lace expansion needs a small parameter.** Convergence requires the one-step "bubble" $\sum_x \tau(x)^2$-type quantity to be small. On $\mathbb{Z}^d$ the only small parameters available are $1/d$ (from the simple-random-walk Green function $G_d(0)-1 = O(1/d)$) or the inverse range $1/L$. Neither is small at $d=7$: the random-walk return probability is still of order $1/4$, so the expansion's remainder terms do not close. Reducing $19\to11$ needed the non-backtracking reformulation plus large rigorous computer-assisted numerics; the arithmetic degrades sharply below $11$.
- **No perturbative access to $d_c$.** Near $d=6$ the physical expansion parameter is $\epsilon=6-d$, and the correct object is a renormalization-group flow of a $\phi^3$ theory with an imaginary coupling. There is no rigorous RG construction for percolation on $\mathbb{Z}^d$ in dimensions just above six; the rigorous RG successes (Brydges–Slade for weakly self-avoiding walk at $d=4$) rely on a Gaussian reference measure that percolation lacks.
- **Non-integer dimension is not intrinsic.** $\mathbb{Z}^d$ exists only for integer $d$. Interpolating models (long-range, hierarchical) have different microscopic structure, and transferring a theorem about $d_{\rm eff}=6.5$ back to a statement about $\mathbb{Z}^7$ is not a theorem — it is a universality assumption that is itself open.
- **Marginal-dimension logarithms.** At $d_{\rm eff}=6$ exactly, exponents acquire logarithmic corrections (e.g. $\mathbb{P}(|C|\ge n)\approx n^{-1/2}(\log n)^{c}$). Any method proving results *uniformly* down to $6^+$ must survive the divergence of the correction as $d\downarrow 6$; the triangle diagram diverges logarithmically and all triangle-based arguments lose quantitative control.
- **Non-monotonicity in $d$.** There is no known coupling making mean-field behaviour monotone in dimension, so "true for $d\ge11$" gives no information at $d=7$.

## 6. The Gap

Proven: $\nabla(p_c)<\infty$ and ISE-type limits for $d\ge11$ (nearest-neighbour) or $d>6$ with large range/small $\alpha$-coupling. Conjectured: the same for all $d>6$ with range $1$, and uniformly as $d_{\rm eff}\downarrow 6$.

The single missing step is a **non-perturbative proof of the triangle condition**. Every known route to $\nabla(p_c)<\infty$ passes through an expansion whose error terms are controlled by a small parameter. What is needed is either:

1. a self-consistent bootstrap showing $\hat\tau_{p_c}(k)\le C|k|^{-2}$ from a hypothesis of the same form, with $C$ independent of $d>6$ (an "$L^2$-boundedness" argument in the sense of Hutchcroft's nonamenable work, adapted to amenable $\mathbb{Z}^d$); or
2. a rigorous RG construction of the $\phi^3$-type effective theory at $d=6-\epsilon$ giving the tricritical/mean-field crossover directly; or
3. a universality theorem transporting hierarchical results at $d_{\rm eff}\in(6,7)$ to Euclidean lattices.

Everything else — exponents, IIC geometry, ISE convergence, Alexander–Orbach — follows from the triangle condition by results now largely expansion-free (Hutchcroft 2022; Kozma–Nachmias 2009).

## 7. Current Research (as of June 2026)

- **Hierarchical and long-range RG** (Hutchcroft, Cambridge/Caltech; Bäumler, Berger, Munich; Sakai, Hokkaido). Hierarchical lattices allow $d_{\rm eff}$ to be tuned continuously through $6$; results there include mean-field exponents for $d_{\rm eff}>6$ and logarithmic corrections at $d_{\rm eff}=6$ *(frontier — verify)*.
- **NoBLE improvements** (Fitzner, van der Hofstad, Heydenreich). Pushing the nearest-neighbour threshold below $11$ via sharper diagrammatic bounds and interval arithmetic; incremental gains, not a route to $d=7$.
- **Expansion-free derivations** (Hutchcroft). Deriving $\beta,\gamma,\delta,\Delta$ and IIC geometry from the triangle condition alone, isolating the triangle condition as the unique open input.
- **High-precision numerics** (Deng, Ziff, Grassberger, Mertens–Moore). Monte Carlo in $d=5,6,7$ confirms mean-field exponents in $d=7$ and detects $\log$ corrections in $d=6$ consistent with theory.
- **Field-theoretic resummation** (Borinsky, Gracey, Kompaniets, Schnetz). Five-loop $\phi^3$ in $6-\epsilon$ with Borel resummation gives $\eta,\nu,\beta$ for $d=3,4,5$ agreeing with simulation to $\sim10^{-3}$ — evidence for, but not a proof of, the $d_c=6$ picture.

## 8. Future Work

- Prove $\hat\tau_{p_c}(k)\asymp|k|^{-2}$ on $\mathbb{Z}^7$ by any means; this alone closes four integer dimensions.
- Establish universality between hierarchical/long-range models at $d_{\rm eff}=d$ and nearest-neighbour $\mathbb{Z}^d$ — a stated goal of the high-dimensional percolation programme.
- Construct a rigorous RG for the percolation $\phi^3$ theory in $6-\epsilon$, in the spirit of Brydges–Slade at $d=4$.
- Upgrade ISE convergence from $r$-point functions to convergence of the full measure-valued object, and to convergence of the IIC to the *integrated super-Brownian tree*.
- Prove the conjectured logarithmic corrections at $d=6$ on $\mathbb{Z}^6$: $\theta(p)\asymp (p-p_c)\,|\log(p-p_c)|^{2/7}$ *(frontier — verify exponent)*.

## 9. Key References

- **[Foundational]** M. Aizenman, C. M. Newman. *Tree graph inequalities and critical behavior in percolation models.* Journal of Statistical Physics 36, 107–143, 1984.
- **[Foundational]** D. J. Barsky, M. Aizenman. *Percolation critical exponents under the triangle condition.* Annals of Probability 19, 1520–1536, 1991.
- **[Foundational]** T. Hara, G. Slade. *Mean-field critical behaviour for percolation in high dimensions.* Communications in Mathematical Physics 128, 333–391, 1990.
- **[Foundational]** T. Hara, G. Slade. *The scaling limit of the incipient infinite cluster in high-dimensional percolation. II. Integrated super-Brownian excursion.* Journal of Mathematical Physics 41, 1244–1293, 2000.
- **[SOTA]** R. Fitzner, R. van der Hofstad. *Mean-field behavior for nearest-neighbor percolation in $d>10$.* Electronic Journal of Probability 22, paper 43, 2017.
- **[SOTA]** T. Hutchcroft. *On the derivation of mean-field percolation critical exponents from the triangle condition.* Journal of Statistical Physics 189, article 6, 2022.
- **[SOTA]** G. Kozma, A. Nachmias. *The Alexander–Orbach conjecture holds in high dimensions.* Inventiones Mathematicae 178, 635–654, 2009.
- **[SOTA]** M. Heydenreich, R. van der Hofstad, A. Sakai. *Mean-field behavior for long- and finite-range Ising model, percolation and self-avoiding walk.* Journal of Statistical Physics 132, 1001–1049, 2008.
- **[SOTA]** L.-C. Chen, A. Sakai. *Critical two-point functions for long-range statistical-mechanical models in high dimensions.* Annals of Probability 43, 639–681, 2015.
- **[SOTA]** T. Hara. *Decay of correlations in nearest-neighbor self-avoiding walk, percolation, lattice trees and animals.* Annals of Probability 36, 530–593, 2008.
- **[Numerics]** M. Borinsky, J. A. Gracey, M. V. Kompaniets, O. Schnetz. *Five-loop renormalization of $\phi^3$ theory with applications to the Lee–Yang edge singularity and percolation theory.* Physical Review D 103, 116024, 2021.
- **[Numerics]** S. Mertens, C. Moore. *Percolation thresholds and Fisher exponents in hypercubic lattices.* Physical Review E 98, 022120, 2018.
- **[Numerics]** P. Grassberger. *Critical percolation in high dimensions.* Physical Review E 67, 036101, 2003.
- **[Survey]** M. Heydenreich, R. van der Hofstad. *Progress in High-Dimensional Percolation and Random Graphs.* Springer (CRM Short Courses), 2017.
- **[Survey]** G. Slade. *The Lace Expansion and its Applications.* Lecture Notes in Mathematics 1879, Springer, 2006.
- **[Survey]** G. Grimmett. *Percolation.* 2nd edition, Springer, 1999.
- **[Low dimension]** S. Smirnov. *Critical percolation in the plane: conformal invariance, Cardy's formula, scaling limits.* Comptes Rendus de l'Académie des Sciences Paris 333, 239–244, 2001.
- **[Low dimension]** F. Camia, C. M. Newman. *Two-dimensional critical percolation: the full scaling limit.* Communications in Mathematical Physics 268, 1–38, 2006.

## 10. Worked Example / Concrete Special Case

**A percolation model in effective dimension $6.\overline{6}$.**

Take $d=1$ and long-range percolation on $\mathbb{Z}$: each pair $\{x,y\}$ is open independently with probability
$$p_{xy} \;=\; 1-\exp\!\big(-\beta|x-y|^{-(1+\alpha)}\big), \qquad \alpha = \tfrac{3}{10}.$$
Then $d_{\rm eff} = 2d/\alpha = 2/0.3 = 6.\overline{6} \in (6,7)$.

*Step 1 — where is $d_c$?* Assume the mean-field two-point behaviour $\hat\tau_{p_c}(k)\asymp |k|^{-\alpha}$ for small $k$ (proved in this regime by Chen–Sakai). Then
$$\nabla(p_c)\;\asymp\;\int_{|k|\le 1} |k|^{-3\alpha}\,dk \;=\;\int_0^1 k^{-3\alpha}\,dk,$$
which converges iff $3\alpha < d = 1$, i.e. $\alpha < 1/3$. With $\alpha=0.3$: $3\alpha=0.9<1$, so $\nabla(p_c)<\infty$ — the triangle condition holds and mean-field exponents follow. The threshold $\alpha=1/3$ is exactly $d_{\rm eff}=6$.

*Step 2 — exponents.* Mean-field values apply: $\beta=\gamma=1$, $\delta=2$, and $\eta = 2-\alpha = 1.7$, so
$$\tau_{p_c}(x)\;\asymp\;|x|^{-(d-\alpha)} \;=\; |x|^{-0.7}.$$
Check consistency: $\sum_{|x|\le R}\tau_{p_c}(x) \asymp R^{0.3}$, so the expected cluster mass in a box of radius $R$ grows like $R^{\alpha}$ — the cluster has fractal dimension $\alpha=0.3$ inside $\mathbb{Z}$, matching $d_{\rm eff}/{\rm (mass\ exponent)}$: rescaling volume $n$ against space $n^{1/\alpha}$ is the analogue of $n^{1/2}$ in the Euclidean case, and $4 = d_{\rm eff}\cdot \alpha/2 \cdot (2/\alpha)$ recovers the "dimension 4" of the Euclidean IIC.

*Step 3 — the scaling limit.* A critical cluster conditioned to have $n$ vertices, rescaled by $n^{1/\alpha}=n^{10/3}$ in space, is conjectured to converge to **integrated super-$\alpha$-stable excursion**: the occupation measure of the $\alpha$-stable snake driven by a normalized Brownian excursion. Convergence of the $r$-point functions in this regime follows the Hara–Slade template with propagator $|k|^{-2}$ replaced by $|k|^{-\alpha}$.

*Step 4 — the open part.* Push $\alpha\uparrow 1/3$, i.e. $d_{\rm eff}\downarrow 6$. The integral in Step 1 behaves like $(1-3\alpha)^{-1}$, so $\nabla(p_c)\to\infty$ and every constant in the lace-expansion bootstrap blows up. No current argument gives estimates uniform in $\alpha$ up to $1/3$, and at $\alpha=1/3$ exactly one expects $\mathbb{P}(|C|\ge n)\asymp n^{-1/2}(\log n)^{c}$ rather than pure power law. Reproducing Steps 1–3 with constants uniform as $d_{\rm eff}\downarrow 6$ — and transporting them to the nearest-neighbour lattice $\mathbb{Z}^7$ — is precisely the open problem.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*