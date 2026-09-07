---
id: 09-probability/convergence-of-the-on-model-loop-soup
title: "Convergence of the On Model Loop Soup"
topic: 09-probability
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Convergence of the O(n) Model Loop Soup

> **Topic:** Probability & Stochastic Processes · **ID:** `09-probability/convergence-of-the-on-model-loop-soup` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

The loop $O(n)$ model on the hexagonal lattice assigns to each collection of vertex-disjoint simple loops a weight proportional to $n^{\\#\text{loops}} x^{\\#\text{edges}}$. Nienhuis predicted that for $n \in [0,2]$ the model is critical at
$$x_c(n) = \frac{1}{\sqrt{2+\sqrt{2-n}}}.$$

**Conjecture (Nienhuis; Kager–Nienhuis; Smirnov).** For $n \in [0,2]$ and $x = x_c(n)$, the collection of all loops (the *loop soup*) in a simply connected domain $\Omega$ converges, as the mesh $\delta \to 0$ and in the Hausdorff-type topology on closed sets of loops, to the conformal loop ensemble $\mathrm{CLE}_\kappa$ with
$$\kappa = \frac{4\pi}{\pi + \arccos(n/2)} \in \left(\tfrac{8}{3}, 4\right] \quad (\text{dilute phase}),$$
and for every $x > x_c(n)$ to $\mathrm{CLE}_{\kappa'}$ with $\kappa' = \frac{4\pi}{\pi - \arccos(n/2)} \in [4,8)$ (dense phase). For $x < x_c(n)$, and for $n > 2$ at every $x$, loop lengths should decay exponentially and the soup should converge to the empty (trivial) ensemble.

A complete resolution requires: (i) tightness of the loop family; (ii) identification of every subsequential limit as $\mathrm{CLE}_\kappa$; (iii) conformal invariance of the limit, in particular invariance under all Möbius maps of the domain, not merely under lattice symmetries.

## 2. Mathematical Foundations

Let $\mathbb{H}$ be the hexagonal lattice and $\Omega_\delta \subset \delta\mathbb{H}$ a discrete domain. A *loop configuration* $\omega$ is a subset of edges in which every vertex has even degree $0$ or $2$; its connected components are loops. The measure is
$$\mathbb{P}_{n,x}(\omega) \;=\; \frac{n^{\ell(\omega)} x^{|\omega|}}{Z_{n,x}(\Omega_\delta)},\qquad Z_{n,x}=\sum_{\omega} n^{\ell(\omega)} x^{|\omega|},$$
with $\ell(\omega)$ the number of loops and $|\omega|$ the number of edges. For $n=1$ this is the high-temperature expansion of the Ising model with $x=\tanh\beta$; $n=0$ (with a single open path) is the self-avoiding walk; $n=2$ is the *height-function* / integer-valued Lipschitz model on the triangular lattice.

**Parafermionic observable.** For a boundary mid-edge $a$ and mid-edge $z$, set
$$F_{\sigma}(z)\;=\;\sum_{\gamma:\,a\to z} e^{-i\sigma W(\gamma)}\; x^{|\gamma|} n^{\ell(\omega)},$$
summing over configurations with one open path $\gamma$ from $a$ to $z$, where $W(\gamma)$ is the total turning (winding) of $\gamma$. Smirnov's *discrete contour relation* — for every vertex $v$ with incident mid-edges $p,q,r$,
$$(p-v)F_\sigma(p)+(q-v)F_\sigma(q)+(r-v)F_\sigma(r)=0$$
— holds **exactly** when
$$\sigma = \sigma(n) = \frac14 + \frac{3}{4\pi}\arccos\!\Big(\frac n2\Big) \in \left[\tfrac14,\tfrac58\right], \qquad x=\frac{1}{2\cos\!\big(\tfrac{\pi(1-\sigma)}{3}\big)} = x_c(n),$$
the second root of the same local equation being $\tilde x_c(n)=\big(2-\sqrt{2-n}\big)^{-1/2}$ with spin $\tilde\sigma = \tfrac14-\tfrac{3}{4\pi}\arccos(n/2)$. Special values: $\sigma(0)=5/8$, $\sigma(1)=1/2$, $\sigma(2)=1/4$.

**Target object.** $\mathrm{CLE}_\kappa$, $\kappa\in(8/3,8)$, is the unique conformally invariant loop ensemble satisfying the conformal restriction/Markov property (Sheffield–Werner). For $\kappa\in(8/3,4]$ it coincides with the collection of outer boundaries of clusters of a Brownian loop soup of intensity
$$c=\frac{(3\kappa-8)(6-\kappa)}{2\kappa}\in(0,1],$$
so the dilute range $n\in[0,2]$ matches exactly the loop-soup range $c\in(0,1]$ — the reason "$O(n)$ loop soup" and "Brownian loop soup" are expected to be two descriptions of one scaling limit.

## 3. History & State of the Art (SOTA)

- **1982.** Nienhuis derives $x_c(n)$ and the exponent set by Coulomb-gas methods (PRL 49, 1062), predicting the dilute/dense dichotomy.
- **2000–2004.** Schramm's SLE and Kager–Nienhuis' survey translate the Coulomb-gas exponents into the $\kappa \leftrightarrow n$ dictionary above.
- **2006.** Smirnov's ICM address states the parafermionic programme: prove discrete holomorphicity of $F_\sigma$, pass to the limit, identify SLE/CLE.
- **2006.** Camia–Newman construct the full scaling limit of critical percolation — the first proven $O(n)$ loop-soup limit ($n=1$, $x=1$, dense phase, $\mathrm{CLE}_6$).
- **2012.** Duminil-Copin–Smirnov prove $\mu(\mathbb{H})=\sqrt{2+\sqrt2}$, confirming $x_c(0)$ — the first rigorous confirmation of the Nienhuis point.
- **2017–2021.** Duminil-Copin–Peled–Samotij–Spinka (large $n$ exponential decay); Duminil-Copin–Glazman–Peled–Spinka (macroscopic loops for $n\in[1,2]$ at $x_c$); Glazman–Manolescu (delocalization at $n=2$, $x=1$).
- **2019.** Benoist–Hongler identify critical Ising loops with $\mathrm{CLE}_3$ — the only proven *dilute* case.
- **2020–2024.** Duminil-Copin–Kozlowski–Krachun–Manolescu–Oulamara establish rotational invariance for a family of related models, removing one of the three obstacles for those models.

## 4. Partial Results / Verified Cases

| Parameters | Result | Reference |
|---|---|---|
| $n=1$, $x=x_c(1)=1/\sqrt3$ (Ising, $\cosh 2\beta_c=2$) | Full convergence to $\mathrm{CLE}_3$; interfaces to $\mathrm{SLE}_3$ | Chelkak–Smirnov 2012; Benoist–Hongler 2019 |
| $n=1$, $x=1$ (uniform even subgraphs $=$ critical site percolation on triangular lattice) | Full convergence to $\mathrm{CLE}_6$ | Smirnov 2001; Camia–Newman 2006 |
| $n=0$, $x=x_c(0)=1/\sqrt{2+\sqrt2}$ | Critical point identified ($\mu=\sqrt{2+\sqrt2}$); walk is sub-ballistic; endpoint density vanishes | Duminil-Copin–Smirnov 2012; Duminil-Copin–Hammond 2013; Duminil-Copin–Glazman–Hammond–Manolescu 2016 |
| $n\in[1,2]$, $x=x_c(n)$ | Macroscopic loops exist: crossing probabilities of annuli bounded below uniformly in $\delta$ | Duminil-Copin–Glazman–Peled–Spinka 2021 |
| $n=2$, $x=1$ | Logarithmic delocalization of the associated Lipschitz height function; macroscopic loops (BKT-type behaviour) | Glazman–Manolescu 2021 |
| $n\ge n_0$ (large), all $x$ | Exponential decay of loop lengths — no macroscopic loops | Duminil-Copin–Peled–Samotij–Spinka 2017 |
| $x$ small, any $n>0$ | Exponential decay by Peierls/cluster expansion | classical |

Beyond these: the parafermionic observable is proved to satisfy the exact contour relation for *every* $n\in[0,2]$ at $x_c(n)$ — an exact discrete identity, verified case-free.

## 5. Principal Obstacles

- **From one relation to a full boundary value problem.** Discrete holomorphicity of $F_\sigma$ gives one linear relation per vertex, but $F_\sigma$ is complex-valued with a *fractional* spin $\sigma\notin\{0,\tfrac12,1\}$, so there is no discrete Cauchy–Riemann pair, no discrete integration by parts, and no maximum principle. Only at $\sigma=1/2$ ($n=1$) does the relation upgrade to genuine s-holomorphicity with an integrable primitive $\int \mathrm{Im}\,F^2$ — the single reason Ising is solved.
- **No positive association.** For $n<1$ the loop model has no FKG inequality; for $n>1$ the natural spin representation loses positivity. RSW-type crossing estimates, the workhorse behind percolation and random-cluster scaling limits, therefore have no general proof here.
- **Tightness.** Aizenman–Burchard tightness needs polynomial bounds on the probability of $k$ crossings of an annulus; these are unavailable without RSW.
- **Rotational invariance.** Subsequential limits can be shown to be invariant under lattice symmetries only. Upgrading to full conformal invariance requires either an exact-integrability input (Yang–Baxter, as in the Duminil-Copin et al. rotational-invariance programme) or a discrete stress-energy tensor with the right Ward identities.
- **Identification.** Even granted a conformally invariant limit, matching it to $\mathrm{CLE}_\kappa$ requires the conformal Markov property for the *whole* ensemble, not just one interface; Sheffield–Werner's characterization is the only route and needs the limit to be simple and non-nested-degenerate.

## 6. The Gap

Proven: existence of macroscopic loops for $n\in[1,2]$ at $x_c$; exact discrete holomorphicity for all $n\in[0,2]$; full CLE identification only at $n=1$.

Missing, in order of increasing difficulty:
1. **Uniform crossing (RSW) estimates** at $x_c(n)$ for $n\in[0,2]$, in particular for $n<1$ where no macroscopic-loop result exists at all.
2. **A discrete primitive.** For $\sigma\ne 1/2$ there is no known discrete function whose "derivative" is $F_\sigma^2$, so the observable cannot be shown to converge to a conformal map — the sharp technical step separating $n=1$ from every other $n$.
3. **Rotational invariance** of subsequential limits for the loop $O(n)$ model itself (currently proved only for random-cluster-type models with an integrable structure).

## 7. Current Research (as of June 2026)

- **Geneva/IHES school (Duminil-Copin and collaborators).** Extending the rotational-invariance machinery, built from the Yang–Baxter-integrable random-cluster and six-vertex models, toward the loop $O(n)$ family; a transfer to $n\in(1,2)$ via the associated six-vertex representation is the stated goal *(frontier — verify)*.
- **Discrete stress-energy tensor.** Chelkak–Glazman–Smirnov's construction of a discrete stress-energy tensor in the loop $O(n)$ model aims to supply the Ward identities that replace the missing primitive; the outstanding step is a convergence theorem for this tensor at $n\ne 1$ *(frontier — verify)*.
- **s-embeddings (Chelkak).** The perturbed-Ising / s-embedding technology has universalized the $n=1$ case to non-isoradial and random geometries; whether an analogue exists for fractional spin remains open.
- **Loop-soup side (Camia, Werner, Lupu, van de Brug–Camia–Lis).** Coupling arguments between Brownian loop soups, Markovian loop soups on graphs, and CLE nesting continue to sharpen the target: any proven limit must be reconcilable with the $c=(3\kappa-8)(6-\kappa)/2\kappa$ parametrization.
- **Non-critical regimes (Peled, Spinka, Glazman, Taggi).** Refinements of the exponential-decay region for $n>2$ and quantitative macroscopic-loop bounds at $n=2$.

## 8. Future Work

- Prove RSW/crossing estimates at $n\in[0,1)$, most urgently $n=0$: a positive-probability macroscopic-loop statement for critical SAW would be the first crossing result without positive association.
- Construct a substitute primitive: candidates include a two-parameter family of observables (several spins simultaneously), or a "massive" deformation whose derivative recovers $F_\sigma$.
- Import integrability: realize the loop $O(n)$ model as a specialization of a solvable six-vertex/Temperley–Lieb transfer matrix and run the rotational-invariance argument there.
- Attack the dense phase first ($x>x_c$), where extra monotonicity is expected and where $\mathrm{CLE}_6$ ($n=1$, $x=1$) already provides a solved anchor.
- Establish uniqueness/characterization results for loop ensembles under weaker hypotheses than Sheffield–Werner's, so that identification does not require full conformal invariance up front.

## 9. Key References

- **[Foundational]** B. Nienhuis. *Exact Critical Point and Critical Exponents of $O(n)$ Models in Two Dimensions.* Physical Review Letters 49 (1982), 1062–1065.
- **[Foundational]** W. Kager, B. Nienhuis. *A Guide to Stochastic Löwner Evolution and Its Applications.* Journal of Statistical Physics 115 (2004), 1149–1229.
- **[Foundational]** S. Smirnov. *Towards conformal invariance of 2D lattice models.* Proceedings of the ICM Madrid, Vol. II (2006), 1421–1451.
- **[SOTA]** H. Duminil-Copin, S. Smirnov. *The connective constant of the honeycomb lattice equals $\sqrt{2+\sqrt2}$.* Annals of Mathematics 175 (2012), 1653–1665.
- **[SOTA]** D. Chelkak, S. Smirnov. *Universality in the 2D Ising model and conformal invariance of fermionic observables.* Inventiones Mathematicae 189 (2012), 515–580.
- **[SOTA]** S. Benoist, C. Hongler. *The scaling limit of critical Ising interfaces is $\mathrm{CLE}_3$.* Annals of Probability 47 (2019), 2049–2086.
- **[SOTA]** H. Duminil-Copin, A. Glazman, R. Peled, Y. Spinka. *Macroscopic loops in the loop $O(n)$ model at Nienhuis' critical point.* Journal of the European Mathematical Society 23 (2021), 315–347.
- **[SOTA]** H. Duminil-Copin, R. Peled, W. Samotij, Y. Spinka. *Exponential decay of loop lengths in the loop $O(n)$ model with large $n$.* Communications in Mathematical Physics 349 (2017), 777–817.
- **[SOTA]** A. Glazman, I. Manolescu. *Uniform Lipschitz functions on the triangular lattice have logarithmic variations.* Communications in Mathematical Physics 381 (2021), 1153–1221.
- **[SOTA]** S. Sheffield, W. Werner. *Conformal loop ensembles: the Markovian characterization and the loop-soup construction.* Annals of Mathematics 176 (2012), 1827–1917.
- **[SOTA]** F. Camia, C. M. Newman. *Two-dimensional critical percolation: the full scaling limit.* Communications in Mathematical Physics 268 (2006), 1–38.
- **[Frontier]** H. Duminil-Copin, K. K. Kozlowski, D. Krachun, I. Manolescu, M. Oulamara. *Rotational invariance in critical planar lattice models.* arXiv:2012.11672 (2020).
- **[Frontier]** D. Chelkak, A. Glazman, S. Smirnov. *Discrete stress-energy tensor in the loop $O(n)$ model.* arXiv:1604.06339 (2016).
- **[Survey]** R. Peled, Y. Spinka. *Lectures on the spin and loop $O(n)$ models.* In: Sojourns in Probability Theory and Statistical Physics I, Springer PROMS 298 (2019), 246–320.
- **[Survey]** H. Duminil-Copin, S. Smirnov. *Conformal invariance of lattice models.* Clay Mathematics Proceedings 15 (2012), 213–276.

## 10. Worked Example / Concrete Special Case

**Deriving the Nienhuis point from the parafermionic relation.** Fix $n\in[0,2]$ and write $a=\arccos(n/2)\in[0,\pi]$. At a vertex $v$ of $\mathbb{H}$ the three incident mid-edges $p,q,r$ sit at angles $120^\circ$ apart. Grouping configurations by how the path $\gamma$ enters and leaves $v$, each pairing contributes a phase $e^{\mp i\pi\sigma/3}$ (a turn by $\pm\pi/3$) and a factor $x$ per extra edge; the "loop-closing" pairings contribute the weight $n$. The relation $(p-v)F_\sigma(p)+(q-v)F_\sigma(q)+(r-v)F_\sigma(r)=0$ then reduces to the two scalar conditions
$$2\cos\!\Big(\frac{\pi(1-\sigma)}{3}\Big)\,x = 1, \qquad n = 2\cos\!\Big(\frac{\pi(4\sigma-1)}{3}\Big).$$
Solving the second for $\sigma$ gives $\sigma=\frac14+\frac{3a}{4\pi}$, hence $\frac{\pi(1-\sigma)}{3}=\frac{\pi}{4}-\frac a4$, and
$$x^{-2}=4\cos^2\!\Big(\frac{\pi}{4}-\frac a4\Big)=2+2\cos\!\Big(\frac{\pi}{2}-\frac a2\Big)=2+2\sin\frac a2=2+\sqrt{2-2\cos a}=2+\sqrt{2-n}.$$
So $x_c(n)=1/\sqrt{2+\sqrt{2-n}}$ — Nienhuis' point recovered as the *unique* weight making the observable discretely holomorphic. Taking instead $\cos(\pi/4+a/4)$ gives the dense-phase root $\tilde x_c(n)=1/\sqrt{2-\sqrt{2-n}}$.

**Check at $n=1$.** Here $a=\pi/3$, $\sigma=1/2$, and $x_c=1/(2\cos(\pi/6))=1/\sqrt3$. Independently, the loop $O(1)$ model is the high-temperature expansion of the honeycomb Ising model with $x=\tanh\beta$; criticality is $\cosh 2\beta_c=2$, i.e.
$$\tanh^2\beta_c=\frac{\cosh 2\beta_c-1}{\cosh 2\beta_c+1}=\frac13 \implies x_c=\tfrac{1}{\sqrt3}. \checkmark$$
Because $\sigma=1/2$, $F_{1/2}$ is s-holomorphic: $\mathrm{Im}\,F_{1/2}^2$ has a discrete primitive, which converges to the solution of a Dirichlet problem — and this single extra structure is what carries the argument all the way to $\mathrm{SLE}_3$ and $\mathrm{CLE}_3$ (Chelkak–Smirnov; Benoist–Hongler), with $\kappa = 4\pi/(\pi+\pi/3)=3$ as predicted. For $n=1$, $x=1$ the same dictionary gives $\kappa'=4\pi/(\pi-\pi/3)=6$, matching the percolation full scaling limit. For every other $n$ the two displayed scalar conditions still hold exactly, yet $\sigma\ne 1/2$ and the primitive vanishes from the toolbox — the whole of the gap in Section 6, in one line.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*