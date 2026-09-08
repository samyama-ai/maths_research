---
id: 09-probability/critical-window-universality-random-graphs
title: "Erdos–Renyi Critical Window Universality for Inhomogeneous Random Graphs"
topic: 09-probability
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Erdős–Rényi Critical Window Universality for Inhomogeneous Random Graphs

> **Topic:** Probability & Stochastic Processes · **ID:** `09-probability/critical-window-universality-random-graphs` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

At criticality the Erdős–Rényi graph $G(n,p)$ with $p = n^{-1}(1+\lambda n^{-1/3})$ has largest components of order $n^{2/3}$, intrinsic diameters of order $n^{1/3}$, and rescaled component sizes converging to the excursion lengths of a Brownian motion with parabolic drift (Aldous, 1997). The **critical window universality problem** asks:

> For which inhomogeneous random graph models — general kernels $\kappa$, rank-1 models, configuration models, preferential-attachment-type graphs — do the critical scaling exponents, the limiting size vector, *and* the limiting metric space (the scaling limit of the components viewed as measured metric spaces) coincide with those of $G(n,p)$ up to deterministic constants? And what is the exact analytic criterion on the model that separates this Erdős–Rényi class from other classes?

The working conjecture is a **moment dichotomy**: if the limiting degree/weight distribution $W$ has $\mathbb{E}[W^3]<\infty$ then the model lies in the Erdős–Rényi (Brownian) universality class; if $W$ has a power-law tail with exponent $\tau\in(3,4)$ then it lies in a distinct one-parameter family of classes governed by thinned Lévy processes. A complete resolution requires (i) a proof valid for *general* kernels, not only rank-1 or degree-prescribed models, (ii) convergence in the Gromov–Hausdorff–Prokhorov (GHP) topology, not only of component sizes, and (iii) an identification of the boundary case $\mathbb{E}[W^3]=\infty$ with $\tau=4$, including slowly varying corrections.

## 2. Mathematical Foundations

**Inhomogeneous random graph (IRG).** Let $(\mathcal{S},\mu)$ be a ground space, $\kappa:\mathcal{S}^2\to[0,\infty)$ a symmetric kernel, and $x_1,\dots,x_n\in\mathcal{S}$ vertex types with empirical measure $\to\mu$. Edges appear independently with
$$\mathbb{P}(i\sim j) = \min\!\Big(\tfrac{\kappa(x_i,x_j)}{n},\,1\Big).$$
The associated integral operator is
$$(T_\kappa f)(x) = \int_{\mathcal S}\kappa(x,y)f(y)\,\mu(dy),\qquad \|T_\kappa\| = \sup\{\|T_\kappa f\|_2 : \|f\|_2\le 1\}.$$
Bollobás–Janson–Riordan: a giant component exists iff $\|T_\kappa\|>1$; criticality is $\|T_\kappa\|=1$.

**Rank-1 case.** $\kappa(x,y)=xy$ with weights $w_1,\dots,w_n$ i.i.d. copies of $W>0$. The Norros–Reittu model sets $\mathbb{P}(i\sim j)=1-e^{-w_iw_j/\ell_n}$, $\ell_n=\sum_k w_k$. Write
$$\eta_r = \frac{\mathbb{E}[W^r]}{\mathbb{E}[W]},\qquad \nu = \eta_2 .$$
The exploration is dominated by a two-stage branching process with size-biased offspring mean $\nu$; criticality is $\nu=1$, and the critical window is $\nu_n = 1+\lambda n^{-1/3}$.

**Aldous's limit.** For $G(n,n^{-1}(1+\lambda n^{-1/3}))$, let $|C_{(1)}|\ge|C_{(2)}|\ge\cdots$. Then
$$n^{-2/3}\big(|C_{(i)}|\big)_{i\ge1} \;\xrightarrow{d}\; \big(|\gamma_i(\lambda)|\big)_{i\ge1}\quad\text{in }\ell^2_{\downarrow},$$
where $\gamma_i(\lambda)$ are the ordered excursion lengths above past minima of
$$W^\lambda(s) = B(s) + \lambda s - \tfrac{1}{2}s^2 .$$
The process $(\lambda\mapsto$ limit$)$ is the standard multiplicative coalescent, whose entrance boundary was classified by Aldous–Limic.

**Metric limit.** Rescaling the graph distance by $n^{-1/3}$ and the counting measure by $n^{-2/3}$, the critical components converge in GHP to random $\mathbb{R}$-trees with finitely many extra identifications, built from tilted Brownian excursions (Addario-Berry–Broutin–Goldschmidt).

**Finite third moment (ER class).** If $\nu=1$ and $\eta_3<\infty$, there exist constants $a,b>0$ depending only on $\eta_1,\eta_2,\eta_3$ such that
$$n^{-2/3}\big(|C_{(i)}|\big)_{i\ge1}\xrightarrow{d} a\cdot\big(|\gamma_i(b\lambda)|\big)_{i\ge1}.$$

**Heavy tail $\tau\in(3,4)$.** If $\mathbb{P}(W>x)=x^{-(\tau-1)}L(x)$ with $\tau\in(3,4)$, the exponents change:
$$\text{sizes}\;\asymp\;n^{\frac{\tau-2}{\tau-1}},\qquad \text{window width}\;\asymp\;n^{-\frac{\tau-3}{\tau-1}},\qquad \text{distances}\;\asymp\;n^{\frac{\tau-3}{\tau-1}},$$
and the size limit is the excursion vector of a thinned Lévy process
$$V^\lambda(s)=\sum_{i\ge1}c_i\big(\mathbf 1_{\{\xi_i\le s\}}-c_i s\big)+\lambda s ,$$
an Aldous–Limic entrance-boundary point with infinitely many "big-jump" parameters $c_i\propto i^{-1/(\tau-1)}$.

## 3. History & State of the Art (SOTA)

- **1960.** Erdős–Rényi identify the phase transition at $p=1/n$.
- **1984–1990.** Bollobás locates the critical window at width $n^{-4/3}$; Łuczak analyses component structure inside it.
- **1993.** Janson–Knuth–Łuczak–Pittel, *The birth of the giant component*, give exact generating-function asymptotics for excess and multicyclic components.
- **1997.** Aldous proves the $\ell^2_\downarrow$ scaling limit and identifies the multiplicative coalescent; Aldous–Limic (1998) classify its entrance boundary — the source of every known critical universality class.
- **2007.** Bollobás–Janson–Riordan give the general IRG phase-transition theory ($\|T_\kappa\|$ criterion), but leave the critical window open.
- **2010–2013.** Turova, and Bhamidi–van der Hofstad–van Leeuwaarden, establish the ER window for rank-1 models with $\eta_3<\infty$; the latter also prove the *new* $\tau\in(3,4)$ classes.
- **2012.** Addario-Berry–Broutin–Goldschmidt give the GHP metric limit for $G(n,p)$.
- **2017–2020.** Dhara–van der Hofstad–van Leeuwaarden–Sen prove the window for the configuration model, first for finite third moment, then for $\tau\in(3,4)$; Bhamidi–Dhara–van der Hofstad–Sen obtain the metric structure in the heavy-tailed case.

## 4. Partial Results / Verified Cases

| Model class | Condition | Result | Reference |
|---|---|---|---|
| $G(n,p)$, $G(n,m)$ | — | size + GHP limit, all $\lambda\in\mathbb{R}$ | Aldous 1997; ABG 2012 |
| Rank-1 IRG (Norros–Reittu, Chung–Lu, Poissonian) | $\nu=1$, $\eta_3<\infty$ | ER class, sizes $n^{2/3}$, surplus limits | BHvL 2010 |
| Rank-1 IRG | $\tau\in(3,4)$ | new class, sizes $n^{(\tau-2)/(\tau-1)}$ | BHvL 2012 |
| Configuration model, given degrees | $\mathbb{E}[D^3]<\infty$, $\nu_n=1+\lambda n^{-1/3}$ | ER class in $\ell^2_\downarrow$ | Dhara–van der Hofstad–van Leeuwaarden–Sen 2017 |
| Configuration model | $\tau\in(3,4)$ | Lévy class, sizes + surplus | DHLS 2020 |
| Bounded-size rules, Bohman–Frieze, quantum random graphs | third-moment analogue | ER class (basin of attraction) | Bhamidi–Broutin–Sen–Wang |
| Heavy-tailed models | $\tau\in(3,4)$ | GHP metric limit exists | Bhamidi–Dhara–van der Hofstad–Sen 2020 |
| General finite-type kernels | $\|T_\kappa\|=1$, $\mathcal S$ finite, irreducible | ER class | reducible to rank-1 / multi-type CLT arguments |

Numerically, ER window behaviour is confirmed for $n$ up to $10^9$ by direct simulation of component-size histograms; the $n^{2/3}$ and $n^{1/3}$ exponents are visible already at $n\approx10^5$.

## 5. Principal Obstacles

- **Exploration walks are not martingales off rank-1.** For rank-1 models the breadth-first walk has increments that are (size-biased) i.i.d.-like, so a martingale FCLT applies. For a general kernel $\kappa$ the type of the explored vertex is a non-reversible Markov-modulated process; the natural martingale requires the Perron eigenfunction of $T_\kappa$, which for non-compact or non-$L^2$ kernels may not exist.
- **Spectral degeneracy.** $\|T_\kappa\|=1$ can be attained with a continuous spectrum, or with eigenvalue $1$ of infinite multiplicity. The window width $n^{-1/3}$ is derived from a *spectral gap* between the top eigenvalue and the rest; without a gap the correct window scale is unknown.
- **Third moment is not intrinsic.** $\eta_3<\infty$ is a rank-1 statement. The kernel analogue — finiteness of $\int\!\!\int\!\!\int \kappa(x,y)\kappa(y,z)\kappa(z,x)$-type triple integrals — is sufficient in known proofs but not proven necessary.
- **Metric convergence needs more than size convergence.** GHP limits require control of the surplus edges *and* the height process; tightness in GHP has been obtained only via explicit tree encodings (Poisson-tilted $p$-trees, inhomogeneous continuum random trees), which exist for rank-1 and configuration models but not for general kernels.
- **The boundary $\tau=4$.** Slowly varying corrections make both the Brownian and Lévy encodings degenerate; no proof technique currently interpolates.

## 6. The Gap

Proven: rank-1, configuration-model, and several bounded-size-rule models, under a clean moment split ($\mathbb{E}[W^3]<\infty$ vs. $\tau\in(3,4)$), with metric limits in both regimes.

Not proven: (a) a **general-kernel theorem** — an if-and-only-if analytic condition on $(\kappa,\mu)$ placing the model in the ER class; (b) the **critical case $\tau=4$** with regularly varying corrections, including whether the window width is $n^{-1/3}$ up to slowly varying factors; (c) universality for models with **genuine dependence** between edges (preferential attachment, uniform graphs with prescribed degrees beyond configuration-model contiguity, spatial/geometric kernels), where no multiplicative-coalescent structure is available; (d) whether every critical scaling limit must be an Aldous–Limic entrance-boundary point — i.e. whether the classification is *exhaustive* for natural graph models.

The precise step to be crossed: replace "the exploration walk of the model converges to a Lévy-type process by a martingale FCLT" with a spectral-theoretic statement about $T_\kappa$ near $\|T_\kappa\|=1$ that forces the same convergence without an i.i.d. weight representation.

## 7. Current Research (as of June 2026)

- **Eindhoven / Amsterdam (van der Hofstad and collaborators).** Programme extending the moment dichotomy to spatial and geometric IRGs; volume 2 of *Random Graphs and Complex Networks* consolidates the critical-window machinery.
- **UNC Chapel Hill (Bhamidi) and collaborators (Sen, Wang, Broutin).** "Basin of attraction" programme: identifying which dynamic graph processes converge to the standard multiplicative coalescent, and computing the corresponding continuum limits.
- **Oxford / Paris (Goldschmidt, Broutin, Marzouk).** Continuum-limit side: GHP compactness criteria for critical graphs with surplus, and the scaling limit of critical graphs with prescribed degrees. *(frontier — verify)* Recent preprints aim at a unified "critical graph $\Rightarrow$ inhomogeneous continuum random tree with identifications" statement covering all $\tau>3$.
- **Percolation-on-graphs route.** Critical percolation on high-dimensional tori and on expanders shows ER-window behaviour; transferring these triangle-condition arguments to IRGs is an active line. *(frontier — verify)*

## 8. Future Work

1. Formulate and prove a kernel-intrinsic third-moment condition, likely as finiteness of $\|T_\kappa\|_{L^3\to L^3}$-type norms or of a triangle-condition integral.
2. Resolve $\tau=4$: expect window $n^{-1/3}\ell(n)$ and a Brownian limit with slowly varying variance.
3. Prove GHP tightness directly from surplus-edge counts, removing the dependence on explicit tree encodings.
4. Extend to dependent-edge models: preferential attachment at criticality, and critical uniform graphs with heavy-tailed degrees.
5. Establish exhaustiveness: show every scaling limit of a natural critical graph model is an Aldous–Limic extreme point.

## 9. Key References

- **[Foundational]** P. Erdős, A. Rényi. *On the evolution of random graphs.* Publ. Math. Inst. Hungar. Acad. Sci., 1960.
- **[Foundational]** B. Bollobás. *The evolution of random graphs.* Transactions of the AMS 286, 1984.
- **[Foundational]** S. Janson, D. E. Knuth, T. Łuczak, B. Pittel. *The birth of the giant component.* Random Structures & Algorithms 4, 1993.
- **[Foundational]** D. Aldous. *Brownian excursions, critical random graphs and the multiplicative coalescent.* Annals of Probability 25(2), 1997.
- **[Foundational]** D. Aldous, V. Limic. *The entrance boundary of the multiplicative coalescent.* Electronic Journal of Probability 3, 1998.
- **[Foundational]** B. Bollobás, S. Janson, O. Riordan. *The phase transition in inhomogeneous random graphs.* Random Structures & Algorithms 31(1), 2007.
- **[SOTA]** S. Bhamidi, R. van der Hofstad, J. van Leeuwaarden. *Scaling limits for critical inhomogeneous random graphs with finite third moments.* Electronic Journal of Probability 15, 2010.
- **[SOTA]** S. Bhamidi, R. van der Hofstad, J. van Leeuwaarden. *Novel scaling limits for critical inhomogeneous random graphs.* Annals of Probability 40(6), 2012.
- **[SOTA]** L. Addario-Berry, N. Broutin, C. Goldschmidt. *The continuum limit of critical random graphs.* Probability Theory and Related Fields 152, 2012.
- **[SOTA]** S. Dhara, R. van der Hofstad, J. van Leeuwaarden, S. Sen. *Critical window for the configuration model: finite third moment degrees.* Electronic Journal of Probability 22, 2017.
- **[SOTA]** S. Dhara, R. van der Hofstad, J. van Leeuwaarden, S. Sen. *Heavy-tailed configuration models at criticality.* Annales de l'IHP Probabilités et Statistiques 56(3), 2020.
- **[SOTA]** S. Bhamidi, R. van der Hofstad, S. Sen. *The multiplicative coalescent, inhomogeneous continuum random trees, and new universality classes.* Probability Theory and Related Fields 170, 2018.
- **[Recent]** S. Bhamidi, S. Dhara, R. van der Hofstad, S. Sen. *Universality for critical heavy-tailed network models: metric structure of maximal components.* Electronic Journal of Probability 25, 2020.
- **[Survey]** R. van der Hofstad. *Random Graphs and Complex Networks, Vol. 1.* Cambridge University Press, 2017.
- **[Survey]** S. Janson, T. Łuczak, A. Ruciński. *Random Graphs.* Wiley, 2000.
- **[Related]** T. Turova. *Diffusion approximation for the components in critical inhomogeneous random graphs of rank 1.* Random Structures & Algorithms 43, 2013.

## 10. Worked Example / Concrete Special Case

**A two-point-weight rank-1 model in the ER class.**

Let $W$ take value $2$ with probability $q$ and $1/2$ with probability $1-q$. Build the Norros–Reittu graph on $n$ vertices with i.i.d. weights $w_i\sim W$.

*Criticality.* $\nu=\eta_2=\mathbb{E}[W^2]/\mathbb{E}[W]=1$ requires $\mathbb{E}[W^2]=\mathbb{E}[W]$:
$$4q+\tfrac14(1-q)=2q+\tfrac12(1-q)\;\Longrightarrow\; \tfrac94 q=\tfrac14\;\Longrightarrow\; q=\tfrac19 .$$
Check: $\mathbb{E}[W]=\tfrac29+\tfrac89\cdot\tfrac12=\tfrac23$, $\mathbb{E}[W^2]=\tfrac49+\tfrac89\cdot\tfrac14=\tfrac23$. So $\nu=1$ exactly.

*Third moment.* $\mathbb{E}[W^3]=\tfrac89\cdot 1+\tfrac89\cdot\tfrac18\cdot\;$ — explicitly $\tfrac19\cdot 8+\tfrac89\cdot\tfrac18=\tfrac89+\tfrac19=1$, hence
$$\eta_3=\frac{\mathbb{E}[W^3]}{\mathbb{E}[W]}=\frac{1}{2/3}=\frac32<\infty .$$

*Conclusion.* The model satisfies $\nu=1$, $\eta_3<\infty$, so BHvL 2010 applies: perturbing to $\nu_n=1+\lambda n^{-1/3}$ (e.g. by multiplying all weights by $1+\tfrac{\lambda}{2}n^{-1/3}$),
$$n^{-2/3}\big(|C_{(i)}|\big)_{i\ge1}\xrightarrow{d} a\big(|\gamma_i(b\lambda)|\big)_{i\ge1},$$
with $a,b$ explicit in $\eta_1,\eta_2,\eta_3$ only. The exponent $2/3$, the window exponent $1/3$, and the parabolic-drift Brownian limit are *identical* to $G(n,p)$; only the two constants differ, and they depend on the weight law solely through its first three moments. Numerically at $n=10^6$, $\lambda=0$: $n^{2/3}=10^4$, so the largest component has size of order $10^4$ vertices and intrinsic diameter of order $n^{1/3}=100$ — the same orders as $G(10^6,10^{-6})$.

*Contrast.* Replace $W$ by a Pareto weight with tail exponent $\tau-1=2.5$ (so $\tau=3.5$, $\mathbb{E}[W^3]=\infty$), rescaled to $\nu=1$. Then $\eta_3=\infty$ and the exponents move:
$$\frac{\tau-2}{\tau-1}=\frac{1.5}{2.5}=0.6,\qquad \frac{\tau-3}{\tau-1}=\frac{0.5}{2.5}=0.2 .$$
Largest components are of order $n^{0.6}$ (at $n=10^6$: $\approx 4\times10^3$), the window has width $n^{-0.2}$, and the limit is a thinned Lévy excursion process, not Brownian. The gap in Section 6 is exactly the statement that this dichotomy — $0.6$ versus $2/3$ driven by a single moment condition — persists for arbitrary kernels $\kappa$, including the boundary $\tau=4$.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*