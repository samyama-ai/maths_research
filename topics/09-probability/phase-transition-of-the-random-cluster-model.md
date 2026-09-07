---
id: 09-probability/phase-transition-of-the-random-cluster-model
title: "Phase Transition of the Random-Cluster Model"
topic: 09-probability
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Phase Transition of the Random-Cluster Model

> **Topic:** Probability & Stochastic Processes · **ID:** `09-probability/phase-transition-of-the-random-cluster-model` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

The random-cluster (Fortuin–Kasteleyn, FK) model on $\mathbb{Z}^d$ with cluster weight $q \ge 1$ and edge parameter $p \in [0,1]$ has a critical point $p_c(q,d)$ separating a phase with no infinite cluster from one with an infinite cluster. Two questions are open in general:

1. **Nature of the transition.** Is the transition *continuous* (the infinite-cluster density $\theta(p) = \phi_p^1[0 \leftrightarrow \infty]$ satisfies $\theta(p_c)=0$) or *discontinuous* ($\theta(p_c) > 0$)? The conjecture is that for each $d \ge 2$ there is a threshold $q_c(d) \in (1,\infty)$ with the transition continuous for $q < q_c(d)$ and discontinuous for $q > q_c(d)$, and that $q_c(2)=4$, $q_c(3) \approx 2.2$, $q_c(d)=2$ for $d \ge 4$ *(the last is the mean-field prediction; the Potts transition for $q\ge3$ is expected discontinuous in $d\ge3$)*.
2. **Location of $p_c$.** For $d=2$ the answer $p_c(q) = \frac{\sqrt q}{1+\sqrt q}$ is a theorem; for $d\ge3$ no closed form exists or is expected, and even continuity/monotonicity of $q \mapsto p_c(q,d)$ is only partly known.

A complete resolution means: for every $d \ge 3$ and every $q \ge 1$, decide whether $\theta(p_c)=0$, and prove uniqueness of the infinite-volume Gibbs measure at $p_c$ in the continuous case.

## 2. Mathematical Foundations

Let $G=(V,E)$ be a finite graph. A configuration is $\omega \in \{0,1\}^E$; $k(\omega)$ is its number of connected components (isolated vertices counted). The **random-cluster measure** with parameters $p\in[0,1]$, $q>0$ is

$$
\phi_{G,p,q}(\omega) \;=\; \frac{1}{Z_{G,p,q}} \left(\prod_{e\in E} p^{\omega(e)}(1-p)^{1-\omega(e)}\right) q^{k(\omega)},
\qquad
Z_{G,p,q}=\sum_{\omega} p^{|\omega|}(1-p)^{|E|-|\omega|} q^{k(\omega)} .
$$

**Boundary conditions.** On a box $\Lambda_n=[-n,n]^d\cap\mathbb{Z}^d$, *free* ($\xi=0$) counts clusters inside $\Lambda_n$; *wired* ($\xi=1$) identifies all of $\partial\Lambda_n$ into one vertex. For $q\ge1$ the measures satisfy the FKG lattice condition, so the weak limits
$$\phi^0_{p,q}=\lim_{n\to\infty}\phi^0_{\Lambda_n,p,q},\qquad \phi^1_{p,q}=\lim_{n\to\infty}\phi^1_{\Lambda_n,p,q}$$
exist and are extremal: $\phi^0_{p,q}\le_{\rm st}\phi\le_{\rm st}\phi^1_{p,q}$ for every infinite-volume random-cluster measure $\phi$.

**Critical point.** $\theta^\xi(p)=\phi^\xi_{p,q}[0\leftrightarrow\infty]$ is non-decreasing in $p$; set
$$p_c(q,d)=\inf\{p:\theta^1(p)>0\}.$$
The transition is **continuous** if $\theta^1(p_c)=0$, **discontinuous** otherwise. Equivalently (for $q\ge1$), continuity is equivalent to $\phi^0_{p_c,q}=\phi^1_{p_c,q}$, i.e. uniqueness at criticality; the set of $p$ where $\phi^0\ne\phi^1$ is at most countable.

**Edwards–Sokal coupling.** For integer $q\ge2$ and $p=1-e^{-\beta}$, sampling $\omega\sim\phi_{G,p,q}$ and colouring each cluster with a uniform colour from $\{1,\dots,q\}$ yields the $q$-state Potts model at inverse temperature $\beta$:
$$\mu^{\rm Potts}_{\beta,q}(\sigma)\propto \exp\Big(\beta\sum_{\{x,y\}\in E}\mathbf 1_{\sigma_x=\sigma_y}\Big),\qquad
\mu_{\beta,q}[\sigma_x=\sigma_y]-\tfrac1q=\big(1-\tfrac1q\big)\phi_{p,q}[x\leftrightarrow y].$$
So spin-spin correlations equal connection probabilities, and a discontinuous FK transition equals a first-order Potts transition (latent heat, jump in magnetisation). $q=1$ is Bernoulli percolation; $q=2$ is Ising.

**Sharpness (Duminil-Copin–Raoufi–Tassion 2019).** For all $q\ge1$, $d\ge2$ and $p<p_c$ there is $c=c(p)>0$ with
$$\phi^0_{p,q}[0\leftrightarrow \partial\Lambda_n]\le e^{-cn},$$
and for $p>p_c$, $\theta^1(p)\ge c\,(p-p_c)$. Hence no intermediate regime of polynomial decay.

**Planar duality.** For a planar graph $G$ with dual $G^*$, $\phi_{G,p,q}(\omega)=\phi_{G^*,p^*,q}(\omega^*)$ where
$$\frac{p^*}{1-p^*}=\frac{q(1-p)}{p}.$$
The self-dual point is $p_{\rm sd}(q)=\frac{\sqrt q}{1+\sqrt q}$.

## 3. History & State of the Art (SOTA)

- **1969–1972.** Fortuin and Kasteleyn introduce the model, unifying percolation, Ising, Potts and electrical networks (*Physica* 57, 1972).
- **1980s.** Aizenman, Chayes, Chayes, Newman and others develop the graphical/random-current toolkit; Burton–Keane (1989) give uniqueness of the infinite cluster for translation-invariant measures with finite energy.
- **1991.** Laanait–Messager–Miracle-Solé–Ruiz–Shlosman prove a discontinuous transition for $q$ large in every $d\ge2$ via Pirogov–Sinai theory applied to the FK representation.
- **2006.** Grimmett's monograph *The Random-Cluster Model* consolidates the theory; the continuity question is stated as the central open problem.
- **2012.** Beffara–Duminil-Copin prove $p_c(q,2)=\sqrt q/(1+\sqrt q)$ for all $q\ge1$, with exponential decay in the subcritical phase.
- **2015–2021.** Full resolution in $d=2$: continuity for $1\le q\le 4$ (Duminil-Copin–Sidoravicius–Tassion), discontinuity for $q>4$ (Duminil-Copin–Gagnebin–Harel–Manolescu–Tassion; short proof by Ray–Spinka).
- **Present.** $d\ge3$ with $q\ge3$ (not large) remains open; the physics prediction $q_c(3)\approx 2.2$ has no rigorous counterpart in either direction.

## 4. Partial Results / Verified Cases

| Regime | Result | Source |
|---|---|---|
| $d=2$, $q\ge1$ | $p_c=\sqrt q/(1+\sqrt q)$ | Beffara–Duminil-Copin 2012 |
| $d=2$, $1\le q\le4$ | Continuous; $\phi^0_{p_c}=\phi^1_{p_c}$, polynomial decay of $\phi_{p_c}[0\leftrightarrow\partial\Lambda_n]$ | Duminil-Copin–Sidoravicius–Tassion 2017 |
| $d=2$, $q>4$ | Discontinuous; correlation length $\xi(p_c)<\infty$, exact conjectured $\xi$ asymptotics | DGHMT 2021; Ray–Spinka 2020 |
| $q=1$, all $d$ | Continuity known for $d=2$ (Kesten 1980, $p_c=1/2$) and $d\ge11$ (lace expansion: Hara–Slade 1990; Fitzner–van der Hofstad 2017); **open for $3\le d\le10$** | — |
| $q=2$, all $d\ge2$ | Continuous (Ising has no spontaneous magnetisation at $\beta_c$) | Aizenman–Duminil-Copin–Sidoravicius 2015 |
| $q>q_0(d)$, all $d\ge2$ | Discontinuous, $q_0(2)=4$ but $q_0(d)$ non-explicit and large for $d\ge3$ | Laanait et al. 1991 |
| All $q\ge1$, $d\ge2$ | Sharpness of the transition; exponential decay below $p_c$ | Duminil-Copin–Raoufi–Tassion 2019 |
| Supercritical $q\ge1$ | Slab percolation / Grimmett–Marstrand-type results ($q=1$: 1990; Ising $q=2$: Bodineau 2005) | — |
| $d=2$, $q=2$ | Conformal invariance of the critical FK-Ising interface (SLE$_{16/3}$) | Smirnov 2010; Chelkak–Duminil-Copin–Hongler–Kemppainen–Smirnov 2014 |

## 5. Principal Obstacles

- **No planar duality in $d\ge3$.** The self-dual point argument, parafermionic observables, and the crossing/RSW machinery that drive every sharp $d=2$ result rely on duality between primal and dual *edges*. In $d=3$ the dual object is a surface (plaquette percolation); RSW-type crossing estimates for surfaces are not available.
- **Loss of positive association across representations.** For $q\ge3$ the Potts model has no random-current representation, so the switching lemma that yields Ising continuity in all $d$ (ADS 2015) has no analogue. This is the single sharpest technical wall: $q=2$ is solved in every dimension precisely because currents exist.
- **Non-perturbative $q$ range.** Pirogov–Sinai works only when $q$ is large enough that ordered and disordered phases are separated by a large surface tension; it says nothing at $q=3$. Conversely, mean-field/lace-expansion methods need $q$ near $1$ *and* $d$ large. The physically interesting window $q\in\{3,4,\dots\}$, $d=3$ sits between the two perturbative regimes.
- **Discontinuity is not monotone-friendly.** $\theta^1(p_c)>0$ is not a monotone event in any parameter, so FKG/coupling arguments cannot transfer discontinuity from large $q$ down to small $q$, nor from $d=2$ to $d=3$. Even monotonicity of $q\mapsto q_c(d)$ is unproven.
- **Criticality in $3\le d\le 10$ for percolation.** Even $q=1$ resists: the lace expansion requires $d>10$, and no non-perturbative substitute exists.

## 6. The Gap

Proven: $d=2$ completely; $q\in\{1,2\}$ partially or completely in higher dimensions; $q$ large in all $d$. Missing: any statement at fixed small integer $q\ge3$ in $d=3$. Concretely, the gap is a proof of **either**

- a dichotomy theorem in $d\ge3$ — "either $\phi^0_{p_c}=\phi^1_{p_c}$ or the correlation length is finite at $p_c$" — with a criterion computable at $q=3$; **or**
- a monotonicity statement "if the transition is discontinuous for $(q,d)$ then it is discontinuous for $(q',d)$ for all $q'>q$", which would define $q_c(d)$ and reduce the problem to locating one number.

Neither is known. Even the existence of a threshold $q_c(d)$ separating the two behaviours is a conjecture, not a theorem, for $d \ge 3$.

## 7. Current Research (as of June 2026)

- **Geneva / IHES school (Duminil-Copin and collaborators).** Continued development of crossing-probability technology beyond planarity; the "Bethe-ansatz-free" route to $q_c$ and quantitative RSW. Rotational invariance of critical planar FK models for $1\le q\le4$ (Duminil-Copin, Kozlowski, Krachun, Manolescu, Oulamara) upgrades scaling-limit control in $d=2$ *(frontier — verify final journal version)*.
- **Random-current substitutes for $q\ge3$.** Attempts to build a signed or loop-based representation supporting a switching lemma for Potts. No working analogue yet *(frontier — verify)*.
- **Discrete holomorphicity and integrability.** Parafermionic observables at the self-dual point, and transfer-matrix/Bethe-ansatz input, give the conjectured correlation length $\xi(p_{\rm sd}(q))$ for $q>4$ in $d=2$; extending any of this off the plane is the stated aim.
- **$d=3$ numerics.** Monte Carlo with FK cluster algorithms consistently place $q_c(3)$ between $2$ and $3$ (estimates cluster near $2.2$), and show the $q=3$ Potts transition in $d=3$ is weakly first order.
- **Long-range and hierarchical models.** One-dimensional $1/|x-y|^2$ Potts/FK models where discontinuity is provable (ACCN 1988) are used as testbeds for mechanisms that might transfer.

## 8. Future Work

- Prove $\theta(p_c)=0$ for Bernoulli percolation ($q=1$) in $d=3$ — the cleanest sub-target, and a prerequisite for any general method.
- Establish monotonicity in $q$ of the discontinuity property; this alone would legitimise the definition of $q_c(d)$.
- Sharpen Pirogov–Sinai so that the required $q_0(d)$ becomes explicit and small; a bound $q_0(3)\le 3$ would settle the $3$-state Potts transition in $d=3$.
- Develop a surface/plaquette-duality theory in $d=3$ with usable crossing estimates for the dual random surfaces.
- Prove continuity for $q\in[1,2]$ (non-integer) in all $d$ by interpolating between the percolation and Ising methods.

## 9. Key References

- **[Foundational]** C. M. Fortuin, P. W. Kasteleyn. *On the random-cluster model I. Introduction and relation to other models.* Physica **57**, 536–564, 1972.
- **[Foundational / Survey]** G. Grimmett. *The Random-Cluster Model.* Grundlehren der mathematischen Wissenschaften **333**, Springer, 2006.
- **[SOTA]** V. Beffara, H. Duminil-Copin. *The self-dual point of the two-dimensional random-cluster model is critical for $q\ge1$.* Probability Theory and Related Fields **153**, 511–542, 2012.
- **[SOTA]** H. Duminil-Copin, V. Sidoravicius, V. Tassion. *Continuity of the phase transition for planar random-cluster and Potts models with $1\le q\le 4$.* Communications in Mathematical Physics **349**, 47–107, 2017.
- **[SOTA]** H. Duminil-Copin, M. Gagnebin, M. Harel, I. Manolescu, V. Tassion. *Discontinuity of the phase transition for the planar random-cluster and Potts models with $q>4$.* Annales Scientifiques de l'École Normale Supérieure **54**, 1363–1413, 2021.
- **[SOTA]** G. Ray, Y. Spinka. *A short proof of the discontinuity of phase transition in the planar random-cluster model with $q>4$.* Communications in Mathematical Physics **378**, 1977–1988, 2020.
- **[SOTA]** H. Duminil-Copin, A. Raoufi, V. Tassion. *Sharp phase transition for the random-cluster and Potts models via decision trees.* Annals of Mathematics **189**, 75–99, 2019.
- **[SOTA]** M. Aizenman, H. Duminil-Copin, V. Sidoravicius. *Random currents and continuity of Ising model spontaneous magnetization.* Communications in Mathematical Physics **334**, 719–742, 2015.
- **[Foundational]** L. Laanait, A. Messager, S. Miracle-Solé, J. Ruiz, S. Shlosman. *Interfaces in the Potts model I: Pirogov–Sinai theory of the Fortuin–Kasteleyn representation.* Communications in Mathematical Physics **140**, 81–91, 1991.
- **[Foundational]** G. Grimmett, J. Marstrand. *The supercritical phase of percolation is well behaved.* Proceedings of the Royal Society A **430**, 439–457, 1990.
- **[Related]** T. Bodineau. *Slab percolation for the Ising model.* Probability Theory and Related Fields **132**, 83–118, 2005.
- **[Related]** S. Smirnov. *Conformal invariance in random cluster models. I. Holomorphic fermions in the Ising model.* Annals of Mathematics **172**, 1435–1467, 2010.
- **[Related]** R. Fitzner, R. van der Hofstad. *Mean-field behavior for nearest-neighbor percolation in $d>10$.* Electronic Journal of Probability **22**, paper 43, 2017.
- **[Survey]** H. Duminil-Copin. *Lectures on the Ising and Potts models on the hypercubic lattice.* In *Random Graphs, Phase Transitions, and the Gaussian Free Field*, PIMS-CRM Summer School Proceedings, Springer, 2020.

## 10. Worked Example / Concrete Special Case

**(a) One edge, from the definition.** Take $G$ = two vertices joined by one edge. Then $k(1)=1$, $k(0)=2$, so
$$Z=p\,q^1+(1-p)\,q^2=q\big(p+q(1-p)\big),\qquad
\phi(\omega=1)=\frac{p}{p+q(1-p)} .
$$
For $q>1$ the cluster weight *penalises* connection: at $p=1/2$, $q=3$ we get $\phi(1)=\tfrac{1/2}{1/2+3/2}=1/4$ rather than $1/2$. This is exactly the bias that makes $p_c(q)$ increase with $q$.

**(b) Deriving the self-dual point.** Let $G$ be a finite planar graph with $V$ vertices, $E$ edges, $F$ faces, and let $\omega^*$ be the dual configuration ($e^*$ open iff $e$ closed), so $|\omega^*|=|E|-|\omega|$. Euler's formula gives
$$k(\omega)=|V|-|\omega|+f(\omega)-1,\qquad f(\omega)=k(\omega^*)-1 \ \ \text{(loops of }\omega = \text{clusters of }\omega^*\text{)}.$$
Substituting into the weight,
$$
p^{|\omega|}(1-p)^{|E|-|\omega|}q^{k(\omega)}
\;\propto\;
\Big(\frac{p}{q(1-p)}\Big)^{|\omega|} q^{k(\omega^*)}
\;\propto\;
\Big(\frac{q(1-p)}{p}\Big)^{|\omega^*|} q^{k(\omega^*)} .
$$
Matching against the random-cluster form on $G^*$ with parameter $p^*$, whose odds ratio is $p^*/(1-p^*)$, yields the duality relation
$$\frac{p^*}{1-p^*}=\frac{q(1-p)}{p}.$$
Self-duality $p^*=p$ gives $p^2 = q(1-p)^2$, i.e. $\frac{p}{1-p}=\sqrt q$, hence
$$p_{\rm sd}(q)=\frac{\sqrt q}{1+\sqrt q}.$$

**(c) Numerical check at $q=2$.** $p_{\rm sd}(2)=\frac{\sqrt2}{1+\sqrt2}=0.585786\ldots$. Onsager's Ising critical temperature is $\beta_c=\tfrac12\ln(1+\sqrt2)=0.440687$, and the Edwards–Sokal map $p=1-e^{-2\beta}$ (factor $2$ from the $\pm1$ spin normalisation) gives $p=1-e^{-0.881374}=1-0.414214=0.585786$. The two agree, confirming $p_c(2,2)=p_{\rm sd}(2)$.

**(d) What is open.** On $\mathbb{Z}^2$ with $q=3$, part (b) plus Beffara–Duminil-Copin gives $p_c=\frac{\sqrt3}{1+\sqrt3}=0.633975\ldots$ and DSST gives $\theta(p_c)=0$. On $\mathbb{Z}^3$ with $q=3$: no formula for $p_c$, and whether $\theta(p_c)=0$ is unknown — steps (b) and (c) both fail because the dual of an edge in $\mathbb{Z}^3$ is a plaquette, not an edge, so the odds-ratio matching above has no analogue.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*