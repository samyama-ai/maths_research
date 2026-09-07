---
id: 09-probability/integrability-of-the-stochastic-six-vertex-model
title: "Integrability of the Stochastic Six-Vertex Model"
topic: 09-probability
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Integrability of the Stochastic Six-Vertex Model

> **Topic:** Probability & Stochastic Processes · **ID:** `09-probability/integrability-of-the-stochastic-six-vertex-model` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

The stochastic six-vertex model (S6V) is a Markovian specialization of Baxter's six-vertex model in which the vertex weights are chosen so that each vertex acts as a transition kernel: given the arrows entering from the left and below, the pair of outgoing arrows is sampled from a probability distribution. The central question:

**Is the S6V exactly solvable in a sense strong enough to determine its full large-scale behaviour?** Concretely, does the Yang–Baxter equation yield (i) closed formulas for the distribution of the height function $\mathfrak{h}(x,y)$, (ii) KPZ-class limit theorems — $t^{1/3}$ fluctuations with Tracy–Widom limits, and convergence of the whole field to the KPZ fixed point — and (iii) does this survive under the natural deformations: colored (multi-species), inhomogeneous, half-space, open-boundary, and stationary versions?

**Resolved core.** Parts (i) and (ii) at the level of one-point distributions with step or step-Bernoulli initial data are theorems (Borodin–Corwin–Gorin 2016; Aggarwal–Borodin 2019), as is the weak-asymmetry limit to the KPZ SPDE (Corwin–Ghosal–Shen–Tsai 2020), the limit-shape/local-statistics picture (Aggarwal 2020), and the colored spectral theory (Borodin–Wheeler 2022).

**Residual open kernel.** Full multi-point convergence to the KPZ fixed point from *general* (non-integrable) initial data; complete classification of stationary measures for open/half-space S6V for all boundary parameters; sharp control in the ferroelectric ordered phase and at the phase boundary; and a proof of universality showing the exact formulas are not an artifact of the integrable weights. A complete resolution means: theorems covering arbitrary initial data and all parameter regimes, with matching lower bounds, not merely new determinantal identities.

## 2. Mathematical Foundations

**Configurations.** On the quadrant $\mathbb{Z}_{\ge1}^2$, each vertex has incoming arrows $(i_1,j_1)\in\{0,1\}^2$ (left, bottom) and outgoing $(i_2,j_2)$ (right, top), subject to arrow conservation $i_1+j_1=i_2+j_2$. Six configurations are admissible.

**Stochastic weights.** Fix $b_1,b_2\in(0,1)$ and set
$$
L\!\begin{pmatrix}0,0\to0,0\end{pmatrix}=1,\quad
L\!\begin{pmatrix}1,1\to1,1\end{pmatrix}=1,
$$
$$
L\!\begin{pmatrix}0,1\to0,1\end{pmatrix}=b_1,\quad
L\!\begin{pmatrix}0,1\to1,0\end{pmatrix}=1-b_1,\quad
L\!\begin{pmatrix}1,0\to1,0\end{pmatrix}=b_2,\quad
L\!\begin{pmatrix}1,0\to0,1\end{pmatrix}=1-b_2 .
$$
Weights are non-negative and sum to $1$ for each fixed input, so the vertex is a Markov kernel and the model defines a probability measure on up-right path ensembles.

**Anisotropy parameter.** In Baxter's normalization $a_1=a_2=1$, $c_1=1-b_1$, $c_2=1-b_2$,
$$
\Delta=\frac{a_1a_2+b_1b_2-c_1c_2}{2\sqrt{a_1a_2b_1b_2}}=\frac{b_1+b_2}{2\sqrt{b_1b_2}}\ \ge 1,
$$
so stochastic weights always sit in the **ferroelectric** regime. Writing $\Delta=\tfrac12(q^{1/2}+q^{-1/2})$ gives exactly
$$
q=b_1/b_2 .
$$

**Yang–Baxter equation.** $L$ is a stochastic gauge of the $U_q(\widehat{\mathfrak{sl}_2})$ $R$-matrix and satisfies
$$
R_{12}(u/v)\,L_{13}(u)\,L_{23}(v)=L_{23}(v)\,L_{13}(u)\,R_{12}(u/v),
$$
which is the single algebraic input behind every exact formula below.

**Height function.** For step initial data (a path entering from below at every column $x\ge1$, none from the left), let $\mathfrak{h}(x,y)$ be the number of paths passing weakly to the right of $(x,y)$ in row $y$. $\mathfrak{h}$ is monotone, and the S6V is the $y$-time evolution of an interacting particle system with *parallel* (not sequential) update.

**Duality and $q$-moments.** The model is self-dual: $\mathbb{E}[q^{k\mathfrak h}]$-type observables satisfy a closed, Bethe-solvable system, giving nested contour-integral formulas
$$
\mathbb{E}\Big[\prod_{i=1}^{k} q^{\mathfrak h(x,y)}\Big]\ \text{expressible as}\ \oint\cdots\oint \prod_{i<j}\frac{z_i-z_j}{z_i-qz_j}\,\prod_{i=1}^k F(z_i)\,\frac{dz_i}{z_i},
$$
which resum into Fredholm determinants $\det(I+K)_{L^2(\mathcal C)}$.

**Degenerations.** With $b_1=\varepsilon$, $b_2=\varepsilon/q$ (fixed ratio $q$) and time sped up by $\varepsilon^{-1}$, $\mathfrak h$ converges to the ASEP height function with asymmetry $q$ (Aggarwal 2017). Under weak asymmetry $q=e^{-\sqrt\varepsilon}$ and the $1{:}2{:}3$ scaling $\varepsilon^{1/2}\mathfrak h(\varepsilon^{-1}x,\varepsilon^{-2}t)$ minus a drift, the Hopf–Cole solution of
$$
\partial_t \mathcal H=\tfrac12\partial_x^2\mathcal H+\tfrac12(\partial_x\mathcal H)^2+\xi
$$
is recovered (Corwin–Ghosal–Shen–Tsai 2020).

## 3. History & State of the Art (SOTA)

- **1967.** Lieb solves the six-vertex model by Bethe ansatz (residual entropy of square ice); Baxter's 1982 monograph systematizes the transfer-matrix theory.
- **1992.** Gwa and Spohn identify the dynamical exponent $z=3/2$ for the asymmetric six-vertex/ASEP Hamiltonian — the first KPZ signature in this family.
- **2016.** Borodin, Corwin and Gorin write down the S6V as a Markov process on the quadrant, prove a law of large numbers for $\mathfrak h$, and obtain GUE Tracy–Widom $t^{1/3}$ fluctuations in the rarefaction fan for step and step-Bernoulli data. This is the founding integrability theorem.
- **2016–2018.** Corwin–Petrov build stochastic higher-spin vertex models on the line; Borodin–Petrov connect them to symmetric rational (spin Hall–Littlewood) functions, placing S6V inside a one-parameter hierarchy that degenerates to $q$-TASEP, $q$-Hahn TASEP, ASEP and the KPZ equation.
- **2018–2019.** Half-quadrant S6V and half-line open ASEP are solved by Barraquand–Borodin–Corwin–Wheeler (GOE/GSE-type crossover). Aggarwal–Borodin establish the phase transition between the "fan" and "shock" behaviours, including Gaussian fluctuations off the fan.
- **2020–2022.** Aggarwal proves limit shapes and identifies local statistics as translation-invariant Gibbs measures. Borodin–Wheeler develop the colored (multi-species) spectral theory in *Astérisque*; Borodin–Gorin–Wheeler prove shift-invariance identities linking distinct observables.
- **2021–2023.** Matetski–Quastel–Remenik construct the KPZ fixed point; Quastel–Sarkar prove ASEP converges to it for general initial data — the template that S6V must follow.

## 4. Partial Results / Verified Cases

- **Step and step-Bernoulli initial data, $b_1<b_2$ (i.e. $q<1$):** exact Fredholm determinant for $\mathfrak h$, LLN limit shape, and GUE Tracy–Widom $t^{1/3}$ fluctuations for ratios $\kappa=x/y$ strictly inside the explicitly determined rarefaction interval (BCG 2016).
- **Outside the fan / shock regime:** Gaussian fluctuations of order $t^{1/2}$ and a full phase diagram in the initial-density parameter (Aggarwal–Borodin 2019).
- **Weak asymmetry ($q=e^{-\sqrt\varepsilon}$, near-stationary and narrow-wedge data):** convergence to the KPZ SPDE (CGST 2020).
- **Vanishing-weight limit ($b_1,b_2\to0$, ratio fixed):** convergence to ASEP with asymmetry $q$ (Aggarwal 2017).
- **Half-quadrant with one boundary parameter:** Fredholm Pfaffian formulas, GOE Tracy–Widom at the critical boundary (BBCW 2018).
- **Colored/multi-species S6V:** commuting transfer matrices, Cauchy identities and a complete spectral decomposition in terms of colored functions (Borodin–Wheeler 2022); shift-invariance for joint distributions (Borodin–Gorin–Wheeler 2022).
- **Free-fermion point ($\Delta=1$, i.e. $b_1=b_2$, $q=1$):** the model is determinantal and everything is computable in closed form; fluctuations degenerate to Gaussian.
- **Stationary/translation-invariant measures on $\mathbb Z$:** product Bernoulli measures are stationary for the parallel update in the homogeneous case; ring stationary measures for colored systems constructed from the Yang–Baxter equation *(frontier — verify)*.

## 5. Principal Obstacles

- **Formulas are initial-data specific.** The nested contour integrals require the initial condition to be a specialization of a symmetric-function argument (step, step-Bernoulli, geometric/Bernoulli-product). Flat, general deterministic, or half-flat data destroy the factorized $q$-moment structure, and no analogue of the biorthogonalization used for TASEP is known in full generality for parallel-update S6V.
- **$q$-moments do not determine the law.** $\mathbb{E}[q^{k\mathfrak h}]$ grows like $q^{-k^2/2}$, so the moment problem is indeterminate. Every asymptotic argument must go through a resummation into a Fredholm determinant, which is available only for special data.
- **Parallel update breaks standard couplings.** Unlike ASEP, S6V updates a whole row at once; basic coupling and attractiveness arguments used for hydrodynamics are available but the multi-species couplings needed for the KPZ-fixed-point route are far more delicate.
- **Steep-descent analysis is fragile.** In the shock/ordered phase the saddle points collide with poles of the kernel; uniform control across the fan–shock boundary requires case-by-case contour deformation rather than a single argument.
- **No non-integrable perturbation theory.** There is no proof that generic (non-Yang–Baxter) stochastic vertex weights lie in the same universality class; standard perturbative and renormalization tools do not reach $t^{1/3}$ scales.
- **Boundary integrability is constrained.** Half-space and open-boundary versions require the reflection (Sklyanin) equation, which is solvable only along special surfaces in boundary-parameter space; most boundary parameters remain analytically inaccessible.

## 6. The Gap

Proven: one-point (and, via shift-invariance, some multi-point) distributions for a measure-zero family of initial conditions, plus SPDE and ASEP limits. Sought: a statement of the form — for *any* initial height profile converging to $\mathfrak h_0$ after $1{:}2{:}3$ scaling, the rescaled S6V height field converges to the KPZ fixed point started from $\mathfrak h_0$, uniformly on compacts, for all $b_1,b_2\in(0,1)$.

The precise barrier is the passage from *algebraic* solvability (exact formulas for special data) to *dynamical* solvability (a transition-probability kernel for the limit that can be composed). For TASEP this was crossed by Matetski–Quastel–Remenik's biorthogonal-ensemble kernel and for ASEP by Quastel–Sarkar's coupling plus one-point universality. S6V has neither an established biorthogonal representation for arbitrary data nor a coupling to a solved model uniform in $(b_1,b_2)$ away from the $b_i\to0$ corner.

## 7. Current Research (as of June 2026)

- **MIT / Columbia / Caltech / Institute for Advanced Study.** Borodin, Corwin, Aggarwal, Petrov and collaborators continue the colored-vertex-model program: colored $q$-Whittaker and spin $q$-Whittaker functions, shift-invariance, and Gibbs-property characterizations.
- **KPZ fixed point route.** Extending Quastel–Sarkar-style arguments from ASEP to parallel-update S6V for general initial data is the main announced target *(frontier — verify)*.
- **Stationary measures.** Yang–Baxter-based constructions of stationary measures for colored systems on the ring and on the segment (Aggarwal–Nicoletti–Petrov and successors), aiming at open-boundary S6V analogues of the matrix-product ansatz *(frontier — verify)*.
- **Half-space and Pfaffian structures.** Barraquand, Le Doussal and collaborators push half-space S6V toward general boundary parameters and toward the half-space KPZ fixed point *(frontier — verify)*.
- **Local statistics and arctic curves.** Aggarwal's classification of translation-invariant Gibbs states is being combined with variational methods to describe the frozen/liquid boundary for non-step boundary conditions.

## 8. Future Work

1. Construct a biorthogonalization or transition-kernel representation valid for arbitrary initial data under parallel update.
2. Prove tightness plus finite-dimensional convergence to the KPZ fixed point directly, using colored couplings rather than one-point formulas.
3. Classify stationary measures for open-boundary S6V across the full boundary phase diagram, matching the three-phase picture known for open ASEP.
4. Establish universality: show that non-integrable stochastic vertex weights in a neighbourhood of the integrable surface have the same $t^{1/3}$ and Tracy–Widom asymptotics.
5. Handle the deep ferroelectric regime $\Delta\gg1$ and the fan–shock boundary with a single uniform asymptotic method.
6. Develop higher-rank ($U_q(\widehat{\mathfrak{sl}_n})$) and elliptic stochastic vertex models with comparable asymptotic control.

## 9. Key References

- **[Foundational]** R. J. Baxter. *Exactly Solved Models in Statistical Mechanics.* Academic Press, 1982.
- **[Foundational]** L.-H. Gwa, H. Spohn. *Six-vertex model, roughened surfaces, and an asymmetric spin Hamiltonian.* Physical Review Letters 68 (1992), 725–728.
- **[Foundational]** A. Borodin, I. Corwin, V. Gorin. *Stochastic six-vertex model.* Duke Mathematical Journal 165 (2016), no. 3, 563–624.
- **[Foundational]** I. Corwin, L. Petrov. *Stochastic higher spin vertex models on the line.* Communications in Mathematical Physics 343 (2016), 651–700.
- **[SOTA / Recent]** A. Borodin, L. Petrov. *Higher spin six vertex model and symmetric rational functions.* Selecta Mathematica 24 (2018), 751–874.
- **[SOTA / Recent]** A. Aggarwal. *Convergence of the stochastic six-vertex model to the ASEP.* Mathematical Physics, Analysis and Geometry 20 (2017), no. 2.
- **[SOTA / Recent]** G. Barraquand, A. Borodin, I. Corwin, M. Wheeler. *Stochastic six-vertex model in a half-quadrant and half-line open ASEP.* Duke Mathematical Journal 167 (2018), 2457–2529.
- **[SOTA / Recent]** A. Aggarwal, A. Borodin. *Phase transitions in the ASEP and stochastic six-vertex model.* Annals of Probability 47 (2019), 613–689.
- **[SOTA / Recent]** A. Aggarwal. *Limit shapes and local statistics for the stochastic six-vertex model.* Communications in Mathematical Physics 376 (2020), 681–746.
- **[SOTA / Recent]** I. Corwin, P. Ghosal, H. Shen, L.-C. Tsai. *Stochastic PDE limit of the six vertex model.* Communications in Mathematical Physics 375 (2020), 1945–2038.
- **[SOTA / Recent]** A. Borodin, M. Wheeler. *Coloured stochastic vertex models and their spectral theory.* Astérisque 437, Société Mathématique de France, 2022.
- **[SOTA / Recent]** A. Borodin, V. Gorin, M. Wheeler. *Shift-invariance for vertex models and polymers.* Proceedings of the London Mathematical Society 124 (2022), 182–299.
- **[SOTA / Recent]** K. Matetski, J. Quastel, D. Remenik. *The KPZ fixed point.* Acta Mathematica 227 (2021), 115–203.
- **[SOTA / Recent]** J. Quastel, S. Sarkar. *Convergence of exclusion processes and the KPZ equation to the KPZ fixed point.* Journal of the American Mathematical Society 36 (2023), 251–289.
- **[Survey]** I. Corwin. *The Kardar–Parisi–Zhang equation and universality class.* Random Matrices: Theory and Applications 1 (2012), 1130001.
- **[Survey]** A. Borodin, V. Gorin. *Lectures on integrable probability.* In *Probability and Statistical Physics in St. Petersburg*, Proc. Sympos. Pure Math. 91, AMS, 2016.

## 10. Worked Example / Concrete Special Case

**The leftmost path, exactly.** Take $b_1=\tfrac12$, $b_2=\tfrac34$, so $q=b_1/b_2=\tfrac23$ and $\Delta=\frac{b_1+b_2}{2\sqrt{b_1b_2}}=\frac{5/4}{2\sqrt{3/8}}\approx1.021>1$ (ferroelectric, as required).

With step initial data, the path entering at column $1$ never meets another path from its left, so its trajectory is exactly a Markov chain with the single-arrow weights:

- moving vertically (input $(0,1)$): continue vertically with probability $b_1=\tfrac12$, turn right with probability $1-b_1=\tfrac12$;
- moving horizontally (input $(1,0)$): continue horizontally with probability $b_2=\tfrac34$, turn up with probability $1-b_2=\tfrac14$.

Hence vertical runs are $\mathrm{Geom}(1-b_1)$ with mean $\frac{1}{1-b_1}=2$ and variance $\frac{b_1}{(1-b_1)^2}=2$; horizontal runs are $\mathrm{Geom}(1-b_2)$ with mean $\frac{1}{1-b_2}=4$ and variance $\frac{b_2}{(1-b_2)^2}=12$.

After $n$ turns, the vertical displacement $Y_n$ has mean $2n$, variance $2n$, and the horizontal displacement $X_n$ has mean $4n$, variance $12n$. So the leftmost path travels with asymptotic slope
$$
\frac{\Delta y}{\Delta x}=\frac{1-b_2}{1-b_1}=\frac{1/4}{1/2}=\frac12,
$$
and by the CLT its transversal fluctuation around that ray is Gaussian of order $\sqrt{n}$. Explicitly, $X_n-2Y_n$ has variance $12n+4\cdot2n=20n$ (independent runs), so fluctuations are $\sqrt{20n}$.

**The point.** This edge computation is elementary because a single path is a random walk — no interaction, exponent $1/2$. Move one ray inward, into the rarefaction fan where $\Theta(t)$ paths compete for space, and the exclusion constraint takes over: BCG's theorem says the fluctuations of $\mathfrak h(\lfloor\kappa t\rfloor,t)$ there are of order $t^{1/3}$ with a GUE Tracy–Widom limit, not $t^{1/2}$ Gaussian. The entire integrability question is how to compute past the free edge into that interacting bulk — and the answer, for step data, is the Yang–Baxter equation via $q$-moments and a Fredholm determinant. What is still missing (Section 6) is the same computation when the initial arrows are placed arbitrarily rather than at every column.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*