---
id: 09-probability/large-deviations-for-the-asymmetric-simple-exclusion-process
title: "Large Deviations for the Asymmetric Simple Exclusion Process"
topic: 09-probability
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Large Deviations for the Asymmetric Simple Exclusion Process

> **Topic:** Probability & Stochastic Processes · **ID:** `09-probability/large-deviations-for-the-asymmetric-simple-exclusion-process` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

The asymmetric simple exclusion process (ASEP) is the canonical non-reversible interacting particle system. Its hydrodynamic limit is the entropy solution of the inviscid Burgers equation. The problem is to establish a full large deviation principle (LDP) for the empirical density around that limit, and to identify the rate function.

**Jensen–Varadhan conjecture.** For the totally asymmetric process (TASEP, $p=1$), the empirical measure $\pi^N$ satisfies an LDP on $D([0,T];\mathcal{M})$ at speed $N$ (not $N^2$, the diffusive speed) with rate function equal to the total *entropy production* of the candidate trajectory: a weak solution $\rho$ of Burgers' equation costs exactly the mass of the negative part of the entropy-production measure, and any non-weak-solution trajectory costs $+\infty$.

Two components must be proved:

- **Upper bound:** $\limsup_N \frac{1}{N}\log \mathbb{P}(\pi^N \in C) \le -\inf_C I$ for closed $C$. *Proved* (Jensen 2000; Varadhan 2004).
- **Lower bound:** $\liminf_N \frac{1}{N}\log \mathbb{P}(\pi^N \in O) \ge -\inf_O I$ for open $O$. *Open in general.* Known only for restricted classes of trajectories (notably single non-entropic shocks).

A complete resolution must also (a) show $I$ is the correct rate function — lower semicontinuous, with compact sub-level sets, and (b) reconcile the hydrodynamic LDP with the exactly-solvable *current* large deviations of Derrida–Lebowitz, including the asymmetric $3/2$ and $5/2$ tail exponents and the $N^2$-speed upper-tail regime.

## 2. Mathematical Foundations

**The process.** State space $\{0,1\}^{\mathbb{Z}}$ (or $\{0,1\}^{\mathbb{Z}/L\mathbb{Z}}$). A particle at $x$ jumps to $x+1$ at rate $p$ and to $x-1$ at rate $q=1-p$, each jump suppressed if the target is occupied. Generator:

$$(\mathcal{L}f)(\eta)=\sum_{x}\Big[p\,\eta(x)(1-\eta(x+1))+q\,\eta(x+1)(1-\eta(x))\Big]\big(f(\eta^{x,x+1})-f(\eta)\big).$$

Set the asymmetry $\gamma=p-q>0$. Bernoulli product measures $\nu_\rho$, $\rho\in[0,1]$, are the extremal translation-invariant stationary measures. The stationary flux is

$$j(\rho)=\gamma\,\rho(1-\rho),$$

strictly concave — the source of shocks.

**Hydrodynamics.** Under Euler scaling $\pi^N(t)=\frac1N\sum_x \eta_{Nt}(x)\delta_{x/N}$, Rezakhanlou's theorem gives $\pi^N(t,du)\to\rho(t,u)\,du$ where $\rho$ is the unique entropy solution of

$$\partial_t\rho+\partial_u\big(\gamma\rho(1-\rho)\big)=0,\qquad \rho(0,\cdot)=\rho_0.$$

**Entropy production.** For a convex entropy–flux pair $(h,g)$ with $g'=h'j'$, define for a bounded weak solution $\rho$ the distribution

$$\mu_{h}[\rho]:=\partial_t h(\rho)+\partial_u g(\rho)\ \in\ \mathcal{D}'((0,T)\times\mathbb{R}).$$

Entropy solutions are exactly those with $\mu_h[\rho]\le 0$ for all convex $h$. The conjectured rate function is

$$I(\rho)=\sup_{(h,g)}\ \mu_h[\rho]^{+}\big((0,T)\times\mathbb{R}\big)\quad\text{for weak solutions},\qquad I(\rho)=+\infty\ \text{otherwise},$$

normalised so that for a single shock joining $\rho_-$ to $\rho_+$ travelling at the Rankine–Hugoniot speed $v=\gamma(1-\rho_--\rho_+)$, the cost per unit time is the *anti-entropic* jump cost. For TASEP the local cost density of an up-shock (an "anti-shock", $\rho_-<\rho_+$) is

$$\Phi(\rho_-,\rho_+)=\tfrac{\gamma}{6}\,\big|\rho_+-\rho_-\big|^{3}\ \ \text{(per unit length of shock trajectory, in the } h(\rho)=\rho^2 \text{ normalisation)} .$$

The cubic $|\Delta\rho|^3$ scaling is the signature of the Euler-scale ($N$-speed) mechanism: an anti-shock is created by an atypical *rarefaction-blocking* fluctuation.

**Current LDP.** Let $Y_t$ be the total number of jumps across the bond $(0,1)$ up to time $t$. On the ring of $L$ sites with $N$ particles the scaled cumulant generating function

$$\lambda_L(\alpha)=\lim_{t\to\infty}\frac1t\log \mathbb{E}\big[e^{\alpha Y_t}\big]$$

is the Perron eigenvalue of the tilted generator and is exactly computable by Bethe ansatz (Derrida–Lebowitz 1998). In the joint limit $L\to\infty$, $N/L\to\rho$, $\lambda$ has the universal parametric form

$$\lambda \;\sim\; -\sum_{k\ge1}\frac{C^k}{k^{5/2}},\qquad \alpha \;\sim\; -\sum_{k\ge1}\frac{C^k}{k^{3/2}},$$

giving tail exponents $\frac32$ (lower tail of the current) and $\frac52$ (upper tail) — the KPZ-class signature.

## 3. History & State of the Art (SOTA)

- **1970:** Spitzer introduces the exclusion process.
- **1989:** Kipnis, Olla and Varadhan prove the dynamical LDP for the *symmetric* and weakly asymmetric case at diffusive speed $N^{d}$ ($=N$ in $d=1$ under $N^2$ time scaling), rate function of Hamilton–Jacobi type.
- **1991:** Rezakhanlou proves hydrodynamics for attractive asymmetric systems in $d=1$ — entropy solution of Burgers.
- **1998:** Derrida and Lebowitz obtain the exact large deviation function of the current for ASEP on a ring via Bethe ansatz; universal scaling function with $3/2$–$5/2$ tails.
- **2000–2004:** Jensen's NYU thesis and Varadhan's paper establish the **upper bound** at speed $N$ with the entropy-production rate function for TASEP.
- **2001–2015:** Bertini, De Sole, Gabrielli, Jona-Lasinio, Landim develop Macroscopic Fluctuation Theory, giving a variational (formal) description of the rate functional for driven diffusive systems.
- **2004–2005:** Bodineau and Derrida propose the additivity principle and identify dynamical phase transitions in current large deviations.
- **2008–2009:** Tracy and Widom derive exact formulas for ASEP with step initial data; GUE Tracy–Widom fluctuations, and tail estimates.
- **2011:** Amir, Corwin and Quastel connect weakly asymmetric exclusion to the KPZ equation and the exact Fredholm-determinant distribution.
- **2019:** Olla and Tsai identify "exceedingly large" deviations of TASEP: the upper tail of the current occurs at speed $N^2$, not $N$, with an explicit rate.
- **2020–2022:** Corwin–Ghosal, Tsai, Das–Tsai and Lin–Tsai settle KPZ-equation tail exponents ($\frac52$ lower, $\frac32$ upper) rigorously.

The **lower bound** in the Jensen–Varadhan program remains the open core.

## 4. Partial Results / Verified Cases

- **Symmetric / weakly asymmetric ($\gamma=O(1/N)$):** full LDP proven, Kipnis–Olla–Varadhan (1989); boundary-driven WASEP by Bertini–Landim–Mourragui (2009).
- **TASEP upper bound:** proven for all $T$, all bounded initial profiles, speed $N$, entropy-production rate function (Jensen 2000; Varadhan 2004). Extends to ASEP with fixed $\gamma>0$.
- **Lower bound, single shock:** proven for trajectories consisting of one non-entropic shock of constant left/right densities (Vilensky, NYU thesis 2008); matching cost $\frac{\gamma}{6}|\Delta\rho|^3$.
- **One-sided (super-exponential) bounds:** for one-sided deviations of the current in TASEP, matching upper and lower bounds at speed $N$ for the lower tail and $N^2$ for the upper tail (Olla–Tsai 2019).
- **Ring, exact:** for the ring of $L$ sites and any $N$ particles, $\lambda_L(\alpha)$ is exactly known (Derrida–Lebowitz 1998); the $L\to\infty$ universal function is rigorously confirmed in the stationary case.
- **KPZ scaling limits:** the lower-tail rate function of the KPZ equation is explicit (Tsai 2022; Corwin–Ghosal 2020), upper tail exponent $\frac32$ with exact constant (Das–Tsai 2021; Lin–Tsai 2021). These transfer to weakly asymmetric ASEP height functions.
- **Stationary TASEP current, all densities $\rho\in(0,1)$:** the $\frac52$/$\frac32$ tails are established via the Tracy–Widom formulas and via last-passage percolation (Baik–Deift–Johansson-type analysis) in the step and stationary cases.

## 5. Principal Obstacles

- **No reversibility, no Dirichlet form.** The Kipnis–Olla–Varadhan machinery hinges on a variational (Dirichlet-form) representation of the entropy cost. ASEP is not reversible w.r.t. $\nu_\rho$; the antisymmetric part of the generator dominates at Euler scale, so the standard $H_{-1}$ variational bound gives no useful lower bound.
- **Speed mismatch.** The hydrodynamic deviations occur at speed $N$, but the *microscopic* perturbation needed to realize an anti-shock is not a smooth tilt of the measure — a Girsanov change of measure that produces an anti-shock has relative entropy of a different order. There is no known tilted dynamics whose typical behaviour is the desired non-entropic solution.
- **Rate function non-convexity.** $I$ is not convex and not a Legendre transform of anything computable; the Gärtner–Ellis route is closed.
- **Loss of regularity.** Entropy solutions develop shocks in finite time. Compactness for the upper bound comes from Young measures / compensated compactness (Tartar–DiPerna), which are one-directional tools: they certify that limits are weak solutions, but give no construction of atypical trajectories.
- **Non-uniqueness of the perturbation.** Multiple microscopic mechanisms (blocking a site, seeding a second-class particle cloud) produce the same macroscopic anti-shock; identifying the *cheapest* is a control problem with no known solvable structure.
- **Integrability is fragile.** Bethe-ansatz and Fredholm-determinant tools give sharp answers only for step, flat, stationary or ring geometries with $p+q=1$ nearest-neighbour rates; they do not see general trajectory-level deviations.

## 6. The Gap

Proven: for every closed set of trajectories, $\limsup \frac1N\log\mathbb{P}\le -\inf I$. Missing: for an open neighbourhood $O$ of a non-entropic weak solution $\rho^\ast$ with $I(\rho^\ast)<\infty$, a construction giving $\liminf \frac1N\log\mathbb{P}(\pi^N\in O)\ge -I(\rho^\ast)$.

The precise barrier is a **change-of-measure with matching entropy cost**. One needs a family of perturbed dynamics $\mathbb{P}^N_{\rho^\ast}$ (or a coupling/blocking construction) such that (i) $\pi^N\to\rho^\ast$ in $\mathbb{P}^N_{\rho^\ast}$-probability, and (ii) $H(\mathbb{P}^N_{\rho^\ast}\mid\mathbb{P}^N)=N\,I(\rho^\ast)+o(N)$. Vilensky's single-shock case achieves this by explicitly blocking the bond at the shock location for a time of order $1$, paying $\frac{\gamma}{6}|\Delta\rho|^3$ per unit shock length. Extending this to (a) shocks with curved trajectories, (b) countably many interacting shocks, and (c) rate-function-continuous approximation of a general finite-cost weak solution by such configurations is the open step. Sub-problem: prove that finite-$I$ weak solutions admit BV-type structure so that the entropy production is concentrated on a countably rectifiable shock set.

## 7. Current Research (as of June 2026)

- **NYU / Courant lineage** (Varadhan's students and collaborators): pushing the lower bound past single shocks using second-class-particle couplings and blocking constructions.
- **Integrable-probability groups** (Columbia, Michigan, MIT, KTH): Corwin, Ghosal, Tsai, Baik, Liu — exact tail asymptotics for KPZ and ASEP; transfer of Fredholm-determinant asymptotics to trajectory-level statements.
- **Macroscopic Fluctuation Theory school** (Rome/IMPA/ENS: Bertini, Jona-Lasinio, Landim, Bodineau, Derrida, Gabrielli): variational characterisation, dynamical phase transitions, and the "$N$ vs $N^2$" crossover.
- **Hydrodynamic-limit-meets-PDE work:** using DiPerna–Lions and BV structure theory of scalar conservation laws to give the rate function a rectifiable-shock representation. *(frontier — verify)*
- **Open-boundary ASEP:** exact phase diagram of current large deviations via matrix product ansatz (Lazarescu–Mallick line of work); dynamical transitions in the open geometry are being matched to MFT predictions. *(frontier — verify)*
- **KPZ fixed point route:** after Quastel–Sarkar's convergence theorem, one asks whether deviations of the ASEP height function at speed $N$ can be read off from a large deviation principle for the KPZ fixed point / directed landscape. *(frontier — verify)*

## 8. Future Work

- Prove the lower bound for finitely many non-interacting shocks, then handle shock collisions — the natural inductive route sketched by Varadhan.
- Establish a structure theorem: every weak solution with $I(\rho)<\infty$ is BV in space-time with entropy production supported on a rectifiable set.
- Find a genuine tilted dynamics (not a blocking construction) realising anti-shocks; candidates include ASEP with slow bonds moving along the shock trajectory or with a time-dependent second-class-particle source.
- Reconcile the Euler-scale ($N$) rate function with the Olla–Tsai $N^2$-speed upper tail: a unified moderate-deviation interpolation.
- Extend from TASEP to general attractive systems (zero-range, misanthrope) with concave flux; and to $d\ge2$ asymmetric exclusion, where even hydrodynamics is only partially understood.
- Derive the rate function directly from the Bethe-ansatz spectrum in a trajectory-level (not stationary) formulation.

## 9. Key References

- **[Foundational]** C. Kipnis, S. Olla, S. R. S. Varadhan. *Hydrodynamics and large deviation for simple exclusion processes.* Communications on Pure and Applied Mathematics 42 (1989), 115–137.
- **[Foundational]** F. Rezakhanlou. *Hydrodynamic limit for attractive particle systems on $\mathbb{Z}^d$.* Communications in Mathematical Physics 140 (1991), 417–448.
- **[Foundational]** B. Derrida, J. L. Lebowitz. *Exact large deviation function in the asymmetric exclusion process.* Physical Review Letters 80 (1998), 209–213.
- **[Foundational]** S. R. S. Varadhan. *Large deviations for the asymmetric simple exclusion process.* In *Stochastic Analysis on Large Scale Interacting Systems*, Advanced Studies in Pure Mathematics 39, Mathematical Society of Japan, 2004, 1–27.
- **[Foundational]** L. Jensen. *Large deviations of the asymmetric simple exclusion process in one dimension.* Ph.D. thesis, Courant Institute, New York University, 2000.
- **[SOTA / Recent]** S. Olla, L.-C. Tsai. *Exceedingly large deviations of the totally asymmetric exclusion process.* Electronic Journal of Probability 24 (2019), paper 12.
- **[SOTA / Recent]** C. A. Tracy, H. Widom. *Asymptotics in ASEP with step initial condition.* Communications in Mathematical Physics 290 (2009), 129–154.
- **[SOTA / Recent]** G. Amir, I. Corwin, J. Quastel. *Probability distribution of the free energy of the continuum directed random polymer in 1+1 dimensions.* Communications on Pure and Applied Mathematics 64 (2011), 466–537.
- **[SOTA / Recent]** L.-C. Tsai. *Exact lower-tail large deviations of the KPZ equation.* Duke Mathematical Journal 171 (2022), 1879–1922.
- **[SOTA / Recent]** I. Corwin, P. Ghosal. *Lower tail of the KPZ equation.* Duke Mathematical Journal 169 (2020), 1329–1395.
- **[SOTA / Recent]** J. Quastel, S. Sarkar. *Convergence of exclusion processes and the KPZ equation to the KPZ fixed point.* Journal of the American Mathematical Society 36 (2023), 251–289.
- **[Survey]** L. Bertini, A. De Sole, D. Gabrielli, G. Jona-Lasinio, C. Landim. *Macroscopic fluctuation theory.* Reviews of Modern Physics 87 (2015), 593–636.
- **[Survey]** C. Kipnis, C. Landim. *Scaling Limits of Interacting Particle Systems.* Springer, Grundlehren 320, 1999.
- **[Survey]** T. M. Liggett. *Stochastic Interacting Systems: Contact, Voter and Exclusion Processes.* Springer, 1999.
- **[Survey]** I. Corwin. *The Kardar–Parisi–Zhang equation and universality class.* Random Matrices: Theory and Applications 1 (2012), 1130001.

## 10. Worked Example / Concrete Special Case

**Current LDP on the smallest ring.** Take TASEP ($p=1,q=0$) on $\mathbb{Z}/2\mathbb{Z}$ with one particle. Whichever site the particle occupies, the site ahead is empty, so jumps occur at rate $1$ regardless of state. The cumulative current through a fixed bond is $Y_t\sim\mathrm{Poisson}(t/2)$ (half the jumps cross the tagged bond in the stationary sense; count all jumps for simplicity, $Y_t\sim\mathrm{Poisson}(t)$). Then

$$\lambda(\alpha)=\lim_{t\to\infty}\frac1t\log\mathbb{E}[e^{\alpha Y_t}]=e^{\alpha}-1,$$

and by Legendre duality the current $Y_t/t$ satisfies an LDP with rate

$$I(j)=\sup_\alpha\{\alpha j-e^\alpha+1\}=j\log j-j+1,\qquad j\ge0.$$

Tails: $I(j)\sim j\log j$ as $j\to\infty$ and $I(0)=1$. Both are *exponential-type*, with no $3/2$ or $5/2$ exponents — exclusion never binds when there is a single particle, so the system is a free Poisson clock.

**What changes at large $L$.** Put $N=\rho L$ particles on the ring of $L$ sites and let $L\to\infty$. The Derrida–Lebowitz diagonalisation gives, in the scaling regime $\alpha\sim L^{-3/2}$, $\lambda-\gamma\rho(1-\rho)\alpha \sim L^{-3/2}$, the universal parametric pair

$$\lambda_{\mathrm{scaled}}=-\sum_{k\ge1}\frac{C^k}{k^{5/2}},\qquad \alpha_{\mathrm{scaled}}=-\sum_{k\ge1}\frac{C^k}{k^{3/2}},$$

whose Legendre transform has asymmetric tails $\exp(-c\,y^{3/2})$ for $y\to+\infty$ (current above the mean) and $\exp(-c'\,|y|^{5/2})$ for $y\to-\infty$. The $L=2$ computation is the degenerate corner of this family: the $5/2$ exponent comes from the collective cost of slowing $\Theta(L)$ particles at once, which a single particle cannot exhibit.

**Anti-shock cost.** For the hydrodynamic problem, take $\gamma=1$ and the initial profile $\rho_0=\mathbf{1}_{\{u<0\}}\cdot a + \mathbf{1}_{\{u>0\}}\cdot b$ with $a<b$. The entropy solution is a rarefaction fan (the flux $\rho(1-\rho)$ is concave and $a<b$). The non-entropic weak solution is the standing anti-shock moving at speed $v=1-a-b$. Its cost over time $T$ is

$$I=\frac{T}{6}\,(b-a)^3 .$$

For $a=0$, $b=1$: $I=T/6$, so $\mathbb{P}(\text{anti-shock persists to time }T)\approx e^{-NT/6}$. Vilensky's construction realises exactly this by blocking the bond at the shock, and the upper bound of Jensen–Varadhan matches — this single case is the complete, verified instance of the conjecture.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*