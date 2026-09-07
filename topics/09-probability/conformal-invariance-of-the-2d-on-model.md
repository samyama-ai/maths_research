---
id: 09-probability/conformal-invariance-of-the-2d-on-model
title: "Conformal Invariance of the 2D On Model"
topic: 09-probability
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Conformal Invariance of the 2D O(n) Model

> **Topic:** Probability & Stochastic Processes · **ID:** `09-probability/conformal-invariance-of-the-2d-on-model` · **Status:** open

## 1. Problem Statement / Conjecture

The loop $O(n)$ model on the hexagonal lattice assigns to each collection of disjoint simple loops a weight $x^{\\#\text{edges}} n^{\\#\text{loops}}$. Nienhuis (1982) predicted that for $n \in [0,2]$ the model is critical at
$$x_c(n) = \frac{1}{\sqrt{2+\sqrt{2-n}}},$$
critical (dense) for all $x > x_c(n)$, and subcritical for $x < x_c(n)$.

**Conjecture.** For $n \in [0,2]$ and $x \ge x_c(n)$, the collection of loops, viewed in a simply connected domain $\Omega$ with lattice mesh $\delta \to 0$, converges in law to the **conformal loop ensemble** $\mathrm{CLE}_\kappa$ in $\Omega$, where
$$n = -2\cos\!\left(\frac{4\pi}{\kappa}\right), \qquad \kappa \in \left(\tfrac83, 4\right] \text{ if } x = x_c(n) \text{ (dilute)}, \qquad \kappa \in [4,8) \text{ if } x > x_c(n) \text{ (dense)}.$$
In particular the limit is invariant under conformal maps: if $\varphi:\Omega \to \Omega'$ is conformal, the image of the limit law under $\varphi$ is the limit law in $\Omega'$.

A complete proof must supply, for a fixed $n$ and $x$: (i) existence of subsequential scaling limits, (ii) rotational and full conformal invariance of every limit, (iii) identification of the limit with $\mathrm{CLE}_\kappa$ at the stated $\kappa$, and (iv) universality — independence from the underlying lattice. Disproof would mean exhibiting $n \in [0,2]$ for which limits exist but are not conformally invariant, or for which $\kappa(n)$ differs from the Coulomb-gas prediction.

## 2. Mathematical Foundations

**Configuration space.** Let $\mathbb{H}$ be the hexagonal lattice. A loop configuration $\omega \subset E(\mathbb{H})$ is a subgraph in which every vertex has degree $0$ or $2$; its connected components are simple loops. On a finite domain $\Omega_\delta$,
$$\mathbb{P}_{n,x}[\omega] = \frac{x^{|\omega|}\, n^{\ell(\omega)}}{Z_{n,x}(\Omega_\delta)}, \qquad Z_{n,x} = \sum_{\omega} x^{|\omega|} n^{\ell(\omega)},$$
with $|\omega|$ the edge count and $\ell(\omega)$ the loop count. The measure is positive for $n>0$; $n=0$ is interpreted as the single-loop (self-avoiding polygon) limit.

**Special cases.** $n=0$: self-avoiding walk/polygon. $n=1$: Ising model on the triangular lattice — loops are domain walls between $\pm$ clusters, $x = e^{-2\beta}$. $n=\sqrt{q}$ in the dense phase: FK-percolation cluster boundaries for $q\in[0,4]$ (Baxter–Kelland–Wu). $n=2$: the $\mathbb{Z}$-valued height function / six-vertex-like regime, expected $\kappa=4$ (Gaussian free field).

**Spin model.** The loop model arises from the $O(n)$ spin model with spins $\sigma_v \in \mathbb{S}^{n-1}$ and formal weight $\prod_{uv} (1 + x\, n\, \sigma_u \cdot \sigma_v)$ expanded graphically; the loop representation extends this to non-integer $n$.

**Parafermionic observable.** For a domain $\Omega_\delta$ with boundary edge-midpoint $a$ and mid-edge $z$, set
$$F_{\sigma}(z) = \sum_{\gamma:\, a \to z} e^{-i\sigma W(\gamma)}\, x^{|\gamma|}\, n^{\ell(\gamma)},$$
where $\gamma$ runs over configurations containing a single open path from $a$ to $z$ plus loops, and $W(\gamma)$ is the total turning (winding) of the path in radians. Setting
$$n = 2\cos\!\big(\pi(1-\sigma)\big) \cdot \text{(Nienhuis parametrisation)}, \qquad \sigma = 1 - \frac{3}{2}\cdot\frac{ \kappa - 4}{ \kappa}\ \ \text{(spin)},$$
one finds for the critical dilute weight $x = x_c(n)$ the **discrete contour relation**: for every vertex $v$ with neighbouring mid-edges $p,q,r$,
$$(p-v)F_\sigma(p) + (q-v)F_\sigma(q) + (r-v)F_\sigma(r) = 0,$$
i.e. $\oint F_\sigma(z)\,dz = 0$ around each face — the discrete analogue of holomorphicity of $F_\sigma$, which in the continuum should behave as $F(z) \sim \varphi'(z)^{\sigma}$ under conformal change of coordinates.

**Target object.** $\mathrm{CLE}_\kappa$, $\kappa \in (8/3,8)$, is the unique family of random countable collections of non-crossing loops satisfying conformal invariance and the domain Markov property (Sheffield 2009; Sheffield–Werner 2012); loops are locally $\mathrm{SLE}_\kappa$-type, with Hausdorff dimension $1 + \kappa/8$ and central charge
$$c = \frac{(6-\kappa)(3\kappa-8)}{2\kappa}.$$

## 3. History & State of the Art (SOTA)

- **1976** — Baxter, Kelland, Wu give the loop representation of the random-cluster model, linking $n=\sqrt q$ to Potts.
- **1982** — Nienhuis predicts $x_c(n)=1/\sqrt{2+\sqrt{2-n}}$ and the exponents via Coulomb-gas/Bethe-ansatz arguments; the honeycomb connective constant $\mu = \sqrt{2+\sqrt2}$ is the $n=0$ case.
- **1999–2001** — Schramm introduces SLE; Lawler–Schramm–Werner compute LERW/UST limits; Smirnov proves Cardy's formula and conformal invariance of critical site percolation on the triangular lattice ($n=1$, dense, $\kappa=6$).
- **2007–2010** — Smirnov's fermionic observable gives conformal invariance of the critical Ising and FK-Ising models on $\mathbb{Z}^2$ ($n=1$ dilute, $\kappa=3$; $n=\sqrt2$ dense, $\kappa=16/3$).
- **2012** — Duminil-Copin and Smirnov prove $\mu(\mathbb{H})=\sqrt{2+\sqrt2}$, confirming Nienhuis's critical point at $n=0$ using the $\sigma=5/8$ parafermionic observable.
- **2017–2021** — Duminil-Copin, Peled, Samotij, Spinka prove exponential decay for large $n$; Duminil-Copin, Glazman, Peled, Spinka prove macroscopic loops at $(n,x)=(n,x_c(n))$ for $n\in[1,2]$.
- **2020–** — Duminil-Copin, Kozlowski, Krachun, Manolescu, Oulamara establish **rotational invariance** of the scaling limit for the random-cluster model with $q \in [1,4]$ using Bethe-ansatz-driven Yang–Baxter deformations *(frontier — verify final venue)*.

## 4. Partial Results / Verified Cases

| Case | Result | Reference |
|---|---|---|
| $n=1$, dense ($\kappa=6$) | Full conformal invariance of critical site percolation on the triangular lattice; scaling limit is $\mathrm{CLE}_6$ | Smirnov 2001; Camia–Newman 2006 |
| $n=1$, dilute ($\kappa=3$) | Ising interfaces converge to $\mathrm{SLE}_3$; loop ensemble to $\mathrm{CLE}_3$ | Chelkak–Duminil-Copin–Hongler–Kemppainen–Smirnov 2014; Benoist–Hongler 2019 |
| $n=\sqrt2$, dense ($\kappa=16/3$) | FK-Ising conformal invariance; $\mathrm{CLE}_{16/3}$ | Smirnov 2010; Chelkak–Smirnov 2012 (universality on isoradial graphs) |
| $n=2$, $x=x_c(2)=1/\sqrt2$ | Delocalisation of the associated height function; logarithmic variance | Glazman–Manolescu 2021 |
| $n=0$ | Critical point $x_c=1/\sqrt{2+\sqrt2}$ proved (connective constant) | Duminil-Copin–Smirnov 2012 |
| $n \in [1,2]$, $x=x_c(n)$ | Macroscopic loops exist; no exponential decay | Duminil-Copin–Glazman–Peled–Spinka 2021 |
| $n \in [1,2]$, $x > x_c(n)$ | Macroscopic loops in the dense regime | Duminil-Copin–Glazman–Peled–Spinka 2021 |
| $n$ large, all $x$ | Exponential decay of loop lengths (no critical behaviour) | Duminil-Copin–Peled–Samotij–Spinka 2017 |
| $q \in [1,4]$ random-cluster | Rotational invariance of the limit | Duminil-Copin–Kozlowski–Krachun–Manolescu–Oulamara 2020 |

Only $n \in \{1, \sqrt2\}$ (via Ising/percolation/FK-Ising) have full conformal invariance. Nowhere is $\kappa(n)$ identified for generic $n$.

## 5. Principal Obstacles

- **Only two integrable spins.** The parafermionic observable is exactly discrete-holomorphic (all three complex relations at each vertex) only for $\sigma \in \{1/2\}$ (Ising-type), where the relation closes into a genuine Riemann–Hilbert boundary value problem. For $\sigma = 5/8$ ($n=0$) and generic $n$, the vertex relation gives only the *divergence* condition $\oint F\,dz=0$, not the full Cauchy–Riemann pair; the curl condition is missing, so $F$ is not determined by its boundary data.
- **No positive association.** For $n>1$ the loop model has no known FKG inequality in a usable form, and for $n<1$ the measure is not even positive on cluster events. Standard RSW-type crossing machinery, which drives the percolation and FK proofs, has no analogue.
- **Tightness.** Kemppainen–Smirnov's criterion for convergence of interfaces requires uniform bounds on the probability of annulus crossings ("no bottlenecks"). These follow from RSW, which is unavailable for generic $n$.
- **Non-locality of the loop weight.** $n^{\ell(\omega)}$ is a global functional; the model is not a Gibbs field with finite-range local specification in the spin variables when $n \notin \mathbb{Z}$, blocking transfer-matrix-free probabilistic arguments.
- **Continuum uniqueness.** Even granting conformal invariance, identifying $\kappa$ requires computing one exponent exactly (e.g. the one-arm or loop-fractal dimension) — a quantity currently accessible only by non-rigorous Coulomb gas.

## 6. The Gap

Proven: the critical point at $n=0$; existence of macroscopic loops for $n\in[1,2]$; conformal invariance at $n \in \{1,\sqrt 2\}$; rotational invariance in the random-cluster family $q\in[1,4]$.

Missing: (a) tightness of the loop collection for generic $n$, i.e. uniform annulus-crossing bounds; (b) upgrading the single scalar identity $\oint F_\sigma\,dz = 0$ to a full discrete-holomorphicity statement with solvable boundary conditions; (c) passage from rotational invariance (a one-parameter symmetry) to the infinite-dimensional conformal group — the Yang–Baxter deformation method yields rotations but no known route to general Möbius/Riemann maps; (d) determination of $\kappa(n)$ from a proved exponent rather than from the Coulomb-gas ansatz.

The single sharpest step: prove RSW-type crossing estimates uniform in scale for the loop $O(n)$ model at $n \in (0,2)$, $x \ge x_c(n)$.

## 7. Current Research (as of June 2026)

- **Geneva / IHÉS (Duminil-Copin and collaborators).** Extending the Bethe-ansatz/Yang–Baxter deformation programme from random-cluster to loop $O(n)$; the aim is rotational invariance for $n\in[1,2]$ as a stepping stone *(frontier — verify)*.
- **Tel Aviv / Weizmann (Peled, Spinka, Glazman).** Height-function delocalisation techniques (Ginzburg–Landau comparison, Lipschitz-function arguments) to extend the $n \in [1,2]$ macroscopic-loop result to $n<1$.
- **Chelkak school (s-embeddings).** Chelkak's s-embeddings give universality for Ising-type ($\sigma=1/2$) observables on arbitrary weighted planar graphs; the open question is whether a comparable geometric embedding exists for $\sigma \neq 1/2$.
- **Discrete complex analysis on quantum surfaces (LQG route).** Miller–Sheffield–Werner-style constructions realise $\mathrm{CLE}_\kappa$ on Liouville quantum gravity; mating-of-trees exponents give predicted values that match Nienhuis, but transfer to the Euclidean lattice model remains conditional.
- **Numerics.** High-precision Monte Carlo continues to match $\kappa(n) = 4\pi/(2\pi - \arccos(-n/2))$ for the dilute branch to several digits.

## 8. Future Work

1. Prove RSW/crossing estimates for loop $O(n)$ at $n\in(0,2)$ — the consensus prerequisite.
2. Find a second exactly-solvable spin beyond $\sigma=1/2$, e.g. by identifying a lattice embedding making the $\sigma = 5/8$ observable genuinely discrete-holomorphic.
3. Complete rotational $\Rightarrow$ conformal invariance: show that a rotationally and scale-invariant, domain-Markov loop ensemble is automatically $\mathrm{CLE}_\kappa$.
4. Prove Nienhuis's formula $x_c(n) = 1/\sqrt{2+\sqrt{2-n}}$ for all $n\in(0,2)$, currently known only at $n=0$ and (partially) $n \in [1,2]$.
5. Determine the critical behaviour at $n=2$, where $\kappa=4$ and logarithmic corrections are expected (a BKT-type transition).

## 9. Key References

- **[Foundational]** B. Nienhuis. *Exact critical point and critical exponents of $O(n)$ models in two dimensions.* Physical Review Letters 49, 1062–1065, 1982.
- **[Foundational]** R. J. Baxter, S. B. Kelland, F. Y. Wu. *Equivalence of the Potts model or Whitney polynomial with an ice-type model.* Journal of Physics A 9, 397–406, 1976.
- **[Foundational]** O. Schramm. *Scaling limits of loop-erased random walks and uniform spanning trees.* Israel Journal of Mathematics 118, 221–288, 2000.
- **[Foundational]** S. Smirnov. *Critical percolation in the plane: conformal invariance, Cardy's formula, scaling limits.* Comptes Rendus de l'Académie des Sciences Paris 333, 239–244, 2001.
- **[SOTA]** S. Smirnov. *Conformal invariance in random cluster models. I. Holomorphic fermions in the Ising model.* Annals of Mathematics 172, 1435–1467, 2010.
- **[SOTA]** H. Duminil-Copin, S. Smirnov. *The connective constant of the honeycomb lattice equals $\sqrt{2+\sqrt2}$.* Annals of Mathematics 175, 1653–1665, 2012.
- **[SOTA]** D. Chelkak, S. Smirnov. *Universality in the 2D Ising model and conformal invariance of fermionic observables.* Inventiones Mathematicae 189, 515–580, 2012.
- **[SOTA]** D. Chelkak, H. Duminil-Copin, C. Hongler, A. Kemppainen, S. Smirnov. *Convergence of Ising interfaces to Schramm's SLE curves.* Comptes Rendus Mathematique 352, 157–161, 2014.
- **[SOTA]** H. Duminil-Copin, R. Peled, W. Samotij, Y. Spinka. *Exponential decay of loop lengths in the loop $O(n)$ model with large $n$.* Communications in Mathematical Physics 349, 777–817, 2017.
- **[SOTA]** H. Duminil-Copin, A. Glazman, R. Peled, Y. Spinka. *Macroscopic loops in the loop $O(n)$ model at Nienhuis' critical point.* Journal of the European Mathematical Society 23, 315–347, 2021.
- **[SOTA]** A. Glazman, I. Manolescu. *Uniform Lipschitz functions on the triangular lattice have logarithmic variations.* Communications in Mathematical Physics 381, 1153–1221, 2021.
- **[SOTA]** H. Duminil-Copin, K. K. Kozlowski, D. Krachun, I. Manolescu, M. Oulamara. *Rotational invariance in critical planar lattice models.* arXiv:2012.11672, 2020.
- **[Structural]** S. Sheffield. *Exploration trees and conformal loop ensembles.* Duke Mathematical Journal 147, 79–129, 2009.
- **[Structural]** S. Sheffield, W. Werner. *Conformal loop ensembles: the Markovian characterization and the loop-soup construction.* Annals of Mathematics 176, 1827–1917, 2012.
- **[Survey]** R. Peled, Y. Spinka. *Lectures on the spin and loop $O(n)$ models.* In *Sojourns in Probability Theory and Statistical Physics – I*, Springer PROMS 298, 246–320, 2019.
- **[Survey]** W. Kager, B. Nienhuis. *A guide to stochastic Löwner evolution and its applications.* Journal of Statistical Physics 115, 1149–1229, 2004.

## 10. Worked Example / Concrete Special Case

**The case $n=0$: proving $x_c(0)=1/\sqrt{2+\sqrt2}$.**

At $n=0$ the model is the self-avoiding walk on $\mathbb{H}$: $Z(x) = \sum_{\gamma} x^{|\gamma|}$ over self-avoiding walks from a fixed mid-edge $a$. The connective constant $\mu = \lim_N c_N^{1/N}$ ($c_N$ = number of walks of length $N$) satisfies $x_c = 1/\mu$.

Take $\sigma = 5/8$ and define $F(z) = \sum_{\gamma: a \to z} e^{-i\frac58 W(\gamma)} x^{|\gamma|}$. Fix a vertex $v$ with the three adjacent mid-edges $p,q,r$. Walks arriving at $v$ are grouped into triples related by the two ways of leaving $v$; each turn contributes winding $\pm \pi/3$, giving phase $e^{\mp i 5\pi/24}$. Summing, one gets
$$(p-v)F(p) + (q-v)F(q) + (r-v)F(r) = 0 \quad \text{exactly when } x = x_c := \frac{1}{\sqrt{2+\sqrt2}},$$
because the required cancellation reduces to $x^{-1} = 2\cos(\pi/8) = \sqrt{2+\sqrt2}$.

Now sum this relation over all vertices of a trapezoidal domain $S_{T,L}$ (height $T$, width $L$) cut from $\mathbb{H}$. Interior contributions telescope, leaving a boundary identity. Writing $A_{T,L}$, $B_{T,L}$, $E_{T,L}$ for the generating functions of walks ending on the left/right, bottom, and top boundaries, one obtains
$$c_\alpha A_{T,L} + B_{T,L} + c_\beta E_{T,L} = 1, \qquad c_\alpha = \cos\tfrac{3\pi}{8},\ \ c_\beta = \cos\tfrac{\pi}{4}.$$
All three terms are non-negative, so $B_{T,L} \le 1$ uniformly. Taking $L\to\infty$ then $T\to\infty$ shows $\sum_\gamma x_c^{|\gamma|} < \infty$ for walks in a half-plane strip, hence $\mu \le \sqrt{2+\sqrt2}$; a complementary bridge-decomposition argument (Hammersley–Welsh) applied to the same identity gives $\mu \ge \sqrt{2+\sqrt2}$.

**What this does and does not give.** The identity pins the critical point exactly, confirming Nienhuis at $n=0$. It gives no control of the *shape* of the walk: proving that the critical self-avoiding walk converges to $\mathrm{SLE}_{8/3}$ ($\kappa = 8/3$, $n = -2\cos(3\pi/2) = 0$) would additionally require showing $F$ converges to $\varphi'(z)^{5/8}$ for the conformal map $\varphi$ onto a strip — which needs tightness plus a second, currently missing, discrete relation. This is exactly the gap of Section 6, visible in the simplest possible instance.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*