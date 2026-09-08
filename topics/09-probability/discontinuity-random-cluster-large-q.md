---
id: 09-probability/discontinuity-random-cluster-large-q
title: "Dimerization and Delocalization in the Random-Cluster Model with q>4"
topic: 09-probability
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Dimerization and Delocalization in the Random-Cluster Model with q>4

> **Topic:** Probability & Stochastic Processes · **ID:** `09-probability/discontinuity-random-cluster-large-q` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

The planar random-cluster model with cluster weight $q$ is conjectured to undergo a **continuous** phase transition for $1 \le q \le 4$ and a **discontinuous** (first-order) one for $q > 4$. The $q>4$ half was proved on $\mathbb{Z}^2$ in 2016–2021. What remains open is the finer structure that the transition mechanism predicts:

1. **Dimerization / antiferroelectric order.** In the equivalent six-vertex representation at anisotropy $\Delta = -\sqrt{q}/2 < -1$, the height function should be localized and the Gibbs measure should spontaneously break the period-1 translation symmetry down to period 2, with exactly two extremal, exponentially mixing Gibbs states. Full classification of the Gibbs states — including the general $a \ne b$ (non-symmetric) six-vertex regime and free/mixed boundary conditions — is open.
2. **Correlation-length asymptotics at $q \downarrow 4$.** Rigorous proof of the Bethe-ansatz prediction that the correlation length at criticality blows up as $\xi(q) = \exp\!\big(\Theta((q-4)^{-1/2})\big)$, with the conjectured constant $\pi^2/\sqrt{q-4}$ in the exponent, and of the matching essential singularity in the free energy.
3. **Dimensions $d \ge 3$.** Whether the transition is discontinuous for *every* $q > q_c(d)$, with the physically expected $q_c(3) \in (2,3)$ — in particular whether the $3$-state Potts model on $\mathbb{Z}^3$ has a first-order transition.

A complete resolution means: a proof (or disproof) of two-state dimerization in the $\Delta<-1$ six-vertex model on $\mathbb{Z}^2$ with a classification of extremal Gibbs states; sharp two-sided bounds on $\xi(q)$ as $q\downarrow 4$; and a $d$-independent criterion separating continuous from discontinuous behaviour.

## 2. Mathematical Foundations

Let $G=(V,E)$ be a finite subgraph of $\mathbb{Z}^2$. For $\omega \in \{0,1\}^{E}$, the **random-cluster (FK) measure** with parameters $p\in[0,1]$, $q>0$ and boundary condition $\xi$ is
$$\phi^{\xi}_{G,p,q}[\omega] \;=\; \frac{1}{Z^{\xi}_{G,p,q}}\; p^{|\omega|}(1-p)^{|E|-|\omega|}\, q^{\,k^{\xi}(\omega)},$$
where $|\omega|$ is the number of open edges and $k^{\xi}(\omega)$ the number of clusters after identifying vertices wired by $\xi$. For $q \ge 1$ the measure is positively associated (FKG), and the infinite-volume limits $\phi^0_{p,q}$ (free) and $\phi^1_{p,q}$ (wired) exist and are extremal.

**Self-duality and criticality.** The planar dual of $\phi^{\xi}_{G,p,q}$ is a random-cluster model with $p^*$ satisfying $\frac{p p^*}{(1-p)(1-p^*)} = q$; the fixed point is
$$p_{sd}(q) = \frac{\sqrt q}{1+\sqrt q}, \qquad p_c(q) = p_{sd}(q) \quad (q \ge 1),$$
the second equality being the Beffara–Duminil-Copin theorem (2012).

**Order parameter and the dichotomy.** Set $\theta(p) = \phi^1_{p,q}[0 \leftrightarrow \infty]$. The transition is *continuous* if $\theta(p_c)=0$ and *discontinuous* if $\theta(p_c)>0$, equivalently if $\phi^0_{p_c,q} \ne \phi^1_{p_c,q}$.

**Six-vertex correspondence.** At $p=p_{sd}$ the FK model on $\mathbb{Z}^2$ maps to the six-vertex model with weights $a=b=1$, $c=\sqrt q$, whose anisotropy is
$$\Delta \;=\; \frac{a^2+b^2-c^2}{2ab} \;=\; 1-\frac{q}{2} \quad\text{(loop/FK normalisation: } \Delta=-\tfrac{\sqrt q}{2}\text{)},$$
so $q=4$ corresponds exactly to $\Delta=-1$, the boundary of the antiferroelectric regime. Writing $\sqrt q = 2\cosh\lambda$ with $\lambda>0$ for $q>4$ (and $\sqrt q = 2\cos\gamma$ for $q<4$) makes the change of regime a change from trigonometric to hyperbolic Bethe kernels.

**Height function.** For the six-vertex configuration, orient edges and define $h:\;(\mathbb{Z}^2)^* \to \mathbb{Z}$ by incrementing $h$ by $\pm1$ across each edge according to its orientation. *Delocalization* means $\operatorname{Var}(h_x) \to \infty$ as $x\to\infty$ (no infinite-volume Gibbs measure with translation-invariant gradient and bounded variance); *localization* means uniformly bounded variance, with tails $\phi[|h_x - h_y|>t] \le C e^{-ct}$.

**Dimerization.** The $\Delta<-1$ model is expected to admit exactly two extremal Gibbs states $\mu_{\text{even}},\mu_{\text{odd}}$, exchanged by a unit translation, in which the "$c$-type" vertices (equivalently, the doubly-covered edges of the associated loop model) occupy one of the two sublattices with density bounded away from $1/2$. In the loop $O(n)$/quantum spin-chain language with $n=\sqrt q = 2S+1$, this is precisely dimerization of the ground state of the spin-$S$ antiferromagnetic chain.

## 3. History & State of the Art (SOTA)

- **1972.** Fortuin and Kasteleyn introduce the random-cluster model, unifying Bernoulli percolation ($q=1$), Ising ($q=2$) and $q$-state Potts.
- **1973.** Baxter computes the critical free energy of the Potts model and predicts, from the six-vertex solution, that the transition is first order exactly when $q>4$, with spontaneous magnetization and correlation length given by explicit infinite products in $\lambda$.
- **1982.** Kotecký and Shlosman prove first-order behaviour for $q$ large in all dimensions $d\ge2$ via chessboard estimates and reflection positivity.
- **1991.** Laanait, Messager, Miracle-Solé, Ruiz and Shlosman, using Pirogov–Sinai theory applied directly to the FK representation, prove discontinuity in $d=2$ for $q > 25.72$ (later pushed down by refinements, but never to $4$).
- **2012.** Beffara and Duminil-Copin: $p_c = p_{sd}$ for all $q \ge 1$.
- **2017.** Duminil-Copin, Sidoravicius and Tassion prove continuity for $1 \le q \le 4$ (parafermionic observables plus a dichotomy for crossing probabilities).
- **2016/2021.** Duminil-Copin, Gagnebin, Harel, Manolescu and Tassion prove discontinuity for **all** $q>4$ in $d=2$, by a rigorous Bethe-ansatz analysis of the transfer matrix of the six-vertex model at $\Delta<-1$, showing a spectral gap and hence exponential decay of the free-measure connectivity at $p_c$.
- **2020.** Ray and Spinka give a short, Bethe-ansatz-free proof of the same statement using a coupling/counting argument in the loop representation.
- **2020.** Aizenman, Duminil-Copin and Warzel convert the $q>4$ discontinuity into **dimerization** of quantum spin-$S$ chains ($S\ge1$, i.e. $q=(2S+1)^2\ge9$) and Néel order for XXZ at $\Delta>1$.
- **2022–2024.** Duminil-Copin–Kozlowski–Krachun–Manolescu–Tikhonovskaia give a rigorous derivation of the six-vertex free energy; Glazman–Peled establish localization of the height function on the antiferroelectric side; Glazman–Lammers give a unified delocalization/continuity proof for $q\le4$.

## 4. Partial Results / Verified Cases

| Regime | Result | Source |
|---|---|---|
| $1\le q\le4$, $d=2$ | Transition continuous; height function delocalized ($\Delta\in[-1,1]$) | Duminil-Copin–Sidoravicius–Tassion 2017; Duminil-Copin–Karrila–Manolescu–Oulamara 2020; Glazman–Lammers 2024 |
| $q>4$, $d=2$, $a=b$ | $\theta(p_c)>0$; $\phi^0_{p_c}\ne\phi^1_{p_c}$; exponential decay of free connectivities at $p_c$ | Duminil-Copin–Gagnebin–Harel–Manolescu–Tassion 2021; Ray–Spinka 2020 |
| $q>4$, $d=2$ | Height function localized with exponential tails; strictly positive antiferroelectric order parameter | Glazman–Peled 2023 |
| $q=(2S+1)^2$, $S\ge1$ | Dimerization of the spin-$S$ AF chain ground state; Néel order for XXZ | Aizenman–Duminil-Copin–Warzel 2020 |
| $q\ge25.73$, $d=2$; $q$ large, any $d$ | First order via Pirogov–Sinai / chessboard estimates, with quantitative surface tension | Laanait et al. 1991; Kotecký–Shlosman 1982 |
| Complete graph $K_n$ (mean field) | Discontinuous iff $q>2$; explicit $\lambda_c(q)$ and jump | Bollobás–Grimmett–Janson 1996 |
| $q\ge1$, $d\ge3$, $q$ large | First order, coexistence of ordered/disordered states at $\beta_c$ | Kotecký–Shlosman 1982 |

## 5. Principal Obstacles

- **Loss of integrability off the symmetric line.** The Bethe-ansatz proof of DGHMT requires $a=b$ (the FK self-dual line). For general $a\ne b$ the transfer matrices still commute, but the rigorous control of the Bethe roots — the "condensation" of roots on a contour and the completeness of the ansatz — has only been established in the symmetric case. Nothing in the argument yields the *structure* of the infinite-volume states, only a spectral gap.
- **No monotonicity in $q$ for the fine observables.** FKG and comparison inequalities control connection probabilities, but neither the antiferroelectric order parameter nor the height-function variance is monotone in the parameters, so the standard toolbox (sharp thresholds, OSSS, randomized algorithms) does not transfer.
- **Discontinuity destroys conformal-invariance tools.** Parafermionic observables, which drive every result for $q\le4$, are exactly discrete-holomorphic only at $\Delta \in [-1,1]$; for $q>4$ the corresponding spin becomes imaginary and the observable no longer satisfies a usable Cauchy–Riemann relation.
- **Pirogov–Sinai needs a large parameter.** Contour expansions converge only when the surface tension is large, i.e. $q \gg 4$; near $q=4^+$ the correlation length diverges super-polynomially and the "small parameter" $e^{-\sigma}$ is not small.
- **Non-perturbative essential singularity.** The predicted $\xi \sim \exp(c/\sqrt{q-4})$ is invisible to any expansion in $q-4$: every derivative of the free energy is expected to be finite at $q=4$, so no analytic perturbation scheme can detect it.
- **Reflection positivity fails in $d=2$ at moderate $q$.** Chessboard estimates require the entropy gap of Kotecký–Shlosman, again a large-$q$ condition, and they give coexistence but not uniqueness of the two states.

## 6. The Gap

Proven: at $q>4$, $d=2$, $a=b$, the wired and free measures differ at $p_c$, and the height function is localized. Conjectured: the localized phase consists of *exactly two* extremal Gibbs states related by a lattice translation, all Gibbs states are convex combinations of them, and correlations decay exponentially at a rate $\xi(q)^{-1}$ with
$$\lim_{q \downarrow 4}\; \sqrt{q-4}\,\log \xi(q) \;=\; \pi^2 \quad \text{(Baxter's prediction; the rigorous statement is only } \log\xi(q) \asymp (q-4)^{-1/2}\text{ up to constants).}$$
The missing step is a *structural* theorem: converting a spectral gap for the transfer matrix into a classification of translation-non-invariant Gibbs states, and converting Baxter's formal Bethe-root density into two-sided bounds on the second eigenvalue uniformly as $\lambda \downarrow 0$ ($q \downarrow 4$). In $d\ge3$ the gap is wider still: there is no dual model, no six-vertex representation, and the location of $q_c(d)$ is not even conjecturally pinned down beyond numerics.

## 7. Current Research (as of June 2026)

- **Geneva / IHES (Duminil-Copin and collaborators).** Rigorous transfer-matrix spectral theory for the six-vertex model beyond the symmetric line; extraction of correlation-length asymptotics from the free-energy computation of Duminil-Copin–Kozlowski–Krachun–Manolescu–Tikhonovskaia. *(frontier — verify)*
- **Innsbruck / Bonn (Glazman, Lammers).** The "dichotomy theory" for height functions: a general framework in which delocalization for $|\Delta|\le1$ and localization for $\Delta<-1$ are two sides of one percolation-type criterion; extension to loop $O(n)$ with $n>2$.
- **Tel Aviv (Peled and collaborators).** Quantitative antiferroelectric order for $c>2$, including the mixed regime $a\ne b$ and free boundary conditions. *(frontier — verify)*
- **Princeton / Geneva (Aizenman, Warzel, Nachtergaele school).** Consequences for quantum spin chains: dimerization for $S \ge 1$ is settled; the open target is the spin-$1/2$ and the two-dimensional quantum analogues, where the loop weight leaves the $q>4$ window.
- **Numerics.** Tensor-network and Monte Carlo studies confirm $\xi(4.5) \approx 10^{5}$–$10^{6}$, consistent with the $\exp(\pi^2/\sqrt{q-4})$ law, and put $q_c(3) \approx 2.2$.

## 8. Future Work

- Prove uniqueness of the two dimerized states via a *disagreement percolation* or Burton–Keane style argument adapted to non-translation-invariant measures.
- Push the Ray–Spinka combinatorial coupling to give quantitative bounds in $q-4$, bypassing the Bethe ansatz entirely.
- Develop a rigorous Riemann–Hilbert analysis of the Bethe equations at $\lambda \to 0$ to obtain the sharp constant $\pi^2$.
- Extend to the $d\ge3$ Potts model by combining the $d=2$ discontinuity with a dimensional-reduction / rigidity argument for interfaces; prove that $q\mapsto$ (discontinuity) is monotone in $q$ for fixed $d$ — currently unknown even in $d=2$.
- Identify the scaling limit of the $q>4$ critical model: conjecturally a trivial (deterministic-density) limit, with the interface between the two dimerized states converging to a Brownian-type object.

## 9. Key References

- **[Foundational]** C. M. Fortuin, P. W. Kasteleyn. *On the random-cluster model I. Introduction and relation to other models.* Physica 57 (1972), 536–564.
- **[Foundational]** R. J. Baxter. *Potts model at the critical temperature.* J. Phys. C: Solid State Phys. 6 (1973), L445–L448.
- **[Foundational]** R. J. Baxter. *Exactly Solved Models in Statistical Mechanics.* Academic Press, 1982.
- **[Foundational]** R. Kotecký, S. Shlosman. *First-order phase transitions in large entropy lattice models.* Comm. Math. Phys. 83 (1982), 493–515.
- **[Foundational]** L. Laanait, A. Messager, S. Miracle-Solé, J. Ruiz, S. Shlosman. *Interfaces in the Potts model I: Pirogov–Sinai theory of the Fortuin–Kasteleyn representation.* Comm. Math. Phys. 140 (1991), 81–91.
- **[Foundational]** B. Bollobás, G. Grimmett, S. Janson. *The random-cluster model on the complete graph.* Probab. Theory Related Fields 104 (1996), 283–317.
- **[Survey]** G. Grimmett. *The Random-Cluster Model.* Grundlehren der mathematischen Wissenschaften 333, Springer, 2006.
- **[SOTA]** V. Beffara, H. Duminil-Copin. *The self-dual point of the two-dimensional random-cluster model is critical for $q\ge1$.* Probab. Theory Related Fields 153 (2012), 511–542.
- **[SOTA]** H. Duminil-Copin, V. Sidoravicius, V. Tassion. *Continuity of the phase transition for planar random-cluster and Potts models with $1\le q\le4$.* Comm. Math. Phys. 349 (2017), 47–107.
- **[SOTA]** H. Duminil-Copin, M. Gagnebin, M. Harel, I. Manolescu, V. Tassion. *Discontinuity of the phase transition for the planar random-cluster and Potts models with $q>4$.* Annales Scientifiques de l'ENS 54 (2021), 1363–1413.
- **[SOTA]** H. Duminil-Copin, M. Gagnebin, M. Harel, I. Manolescu, V. Tassion. *The Bethe ansatz for the six-vertex and XXZ models: an exposition.* Probability Surveys 15 (2018), 102–130.
- **[SOTA]** G. Ray, Y. Spinka. *A short proof of the discontinuity of phase transition in the planar random-cluster model with $q>4$.* Comm. Math. Phys. 378 (2020), 1977–1988.
- **[SOTA]** M. Aizenman, H. Duminil-Copin, S. Warzel. *Dimerization and Néel order in different quantum spin chains through a shared loop representation.* Annales Henri Poincaré 21 (2020), 2737–2774.
- **[SOTA]** H. Duminil-Copin, K. K. Kozlowski, D. Krachun, I. Manolescu, T. Tikhonovskaia. *On the six-vertex model's free energy.* Comm. Math. Phys. 395 (2022), 1383–1430.
- **[Recent]** A. Glazman, R. Peled. *On the transition between the disordered and antiferroelectric phases of the 6-vertex model.* Electronic Journal of Probability 28 (2023), paper no. 82.
- **[Recent]** A. Glazman, P. Lammers. *Delocalisation and continuity in 2D: loop $O(2)$, six-vertex, and random-cluster models.* Comm. Math. Phys. 405 (2024), article 53.
- **[Recent]** H. Duminil-Copin, A. Karrila, I. Manolescu, M. Oulamara. *Delocalization of the height function of the six-vertex model.* arXiv:2012.13750 (2020).

## 10. Worked Example / Concrete Special Case

**Mean-field random-cluster on $K_n$: the transition threshold is $q=2$, computed exactly.**

Take $G=K_n$ with $p=\lambda/n$, $\lambda>0$ fixed. Bollobás–Grimmett–Janson (1996) show the largest cluster has size $\theta(\lambda,q)\,n + o(n)$, where $\theta$ maximizes an explicit variational functional; $\theta$ is the largest root of
$$e^{-\lambda\theta} \;=\; \frac{1-\theta}{1+(q-1)\theta}.$$

*Case $q=1$ (Erdős–Rényi).* The equation becomes $e^{-\lambda\theta}=1-\theta$, whose positive root appears continuously at $\lambda_c=1$. Continuous transition.

*Case $q=2$ (Ising).* $e^{-\lambda\theta} = (1-\theta)/(1+\theta)$. Expanding both sides for small $\theta$: LHS $=1-\lambda\theta+\tfrac{\lambda^2\theta^2}{2}$, RHS $=1-2\theta+2\theta^2$. The linear terms match at $\lambda=2$; the $\theta^2$ coefficients then give $2 - 2 = 0$, so the bifurcation is degenerate at exactly the borderline. Still continuous, $\lambda_c = q = 2$.

*Case $q=3$.* Now the root appears by a saddle-node bifurcation *before* $\lambda$ reaches $3$. The explicit answer is
$$\lambda_c(q) \;=\; \frac{2(q-1)}{q-2}\,\log(q-1), \qquad \theta_c(q) \;=\; \frac{q-2}{q-1} \quad (q>2).$$
For $q=3$: $\lambda_c = \frac{4}{1}\log 2 = 4\log 2 \approx 2.7726$ and $\theta_c = \tfrac12$. Check: with $\theta=\tfrac12$, $e^{-\lambda_c/2} = e^{-2\log 2} = \tfrac14$, while $(1-\theta)/(1+2\theta) = (1/2)/2 = \tfrac14$. ✓

So at $\lambda_c(3)$ the order parameter jumps from $0$ to $1/2$: the transition is **discontinuous**, and one checks $\theta_c(q) \to 0$ as $q \downarrow 2$, recovering continuity exactly at $q=2$ (indeed $\lambda_c(q) \to 2$).

**What this illustrates.** The mean-field model exhibits the same dichotomy — continuous below a threshold, first order above, with the jump vanishing continuously at the threshold — but with $q_{\text{crit}}=2$ instead of $4$. The planar threshold $q=4$ is not a mean-field effect: it comes from $\Delta = -\sqrt q/2 = -1$, the point where the six-vertex Bethe roots stop being trigonometric. The open problems in Section 1 are exactly the statements that, in $d=2$, one cannot compute the analogue of $\theta_c(q)$ and $\lambda_c(q)$ in closed form, and cannot yet see the two coexisting states directly — only their difference.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*