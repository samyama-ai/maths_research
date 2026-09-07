---
id: 06-pdes/fokker-planck-convergence
title: "Fokker Planck Convergence"
topic: 06-pdes
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Convergence to Equilibrium for the Fokker-Planck Equation

> **Topic:** Partial Differential Equations · **ID:** `06-pdes/fokker-planck-convergence` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

The central problem of Fokker-Planck convergence asks for the precise, optimal, and constructive rates at which solutions $\rho(t, x)$ of the Fokker-Planck Equation (FPE) converge to their stationary probability measure $\rho_\infty(x)$ as $t \to \infty$. 

In its classical, overdamped form on $\mathbb{R}^d$, the equation is given by:
$$ \partial_t \rho = \nabla \cdot (\rho \nabla V) + \nabla \cdot (D \nabla \rho) $$
where $V: \mathbb{R}^d \to \mathbb{R}$ is a confining potential and $D$ is a diffusion matrix (often the identity $I$). When a unique invariant measure $\rho_\infty \propto \exp(-V)$ exists, the problem is to establish bounds of the form:
$$ \mathbf{d}(\rho(t), \rho_\infty) \le C \exp(-\lambda t) \quad \text{or} \quad \mathbf{d}(\rho(t), \rho_\infty) \le C t^{-\alpha} $$
for a suitable distance or divergence $\mathbf{d}$ (e.g., $L^2$, relative entropy, or Wasserstein distance), identifying explicit constants $C$ and $\lambda > 0$ independent of the initial data's dimension.

The problem remains aggressively open or partially solved in three domains:
1. **Degenerate/Kinetic Models:** Where diffusion only acts on a subset of variables (e.g., velocity but not position), requiring *hypocoercivity* to prove convergence.
2. **Non-convex Potentials:** Where $V$ exhibits multiple local minima, inducing metastability and exponentially small spectral gaps (Kramers' rate).
3. **Non-linear/McKean-Vlasov FPEs:** Where the drift depends on the density itself via an interaction potential $W(x,y)$, meaning the energy functional is non-convex with respect to the geometry of optimal transport, and phase transitions can destroy the uniqueness of the stationary state.

A complete resolution entails classifying the exact geometric and algebraic conditions on $V$, $D$, and interaction kernels $W$ under which spectral gaps or modified logarithmic Sobolev inequalities persist, particularly in high-dimensional or infinite-dimensional mean-field limits.

## 2. Mathematical Foundations

The overdamped Fokker-Planck equation describes the evolution of the probability density function $\rho(t,x)$ of a particle subject to a gradient flow and stochastic noise (Langevin dynamics). Setting $D = I$, we write:
$$ \partial_t \rho = \nabla \cdot (\rho \nabla V + \nabla \rho) $$

The stationary solution, assuming $Z = \int_{\mathbb{R}^d} e^{-V(x)} \,dx < \infty$, is the Gibbs measure $\rho_\infty(x) = Z^{-1} e^{-V(x)}$. 

Convergence is naturally studied using the **Relative Entropy** (Kullback-Leibler divergence):
$$ \mathcal{H}(\rho | \rho_\infty) = \int_{\mathbb{R}^d} \rho(x) \log\left(\frac{\rho(x)}{\rho_\infty(x)}\right) dx $$
The time derivative of the relative entropy along the flow of the FPE yields the **Fisher Information** (entropy production rate):
$$ \frac{d}{dt} \mathcal{H}(\rho | \rho_\infty) = - \int_{\mathbb{R}^d} \rho \left| \nabla \log \frac{\rho}{\rho_\infty} \right|^2 dx =: - \mathcal{I}(\rho | \rho_\infty) $$

To deduce exponential convergence $\mathcal{H}(\rho(t) | \rho_\infty) \le e^{-2\lambda t}\mathcal{H}(\rho(0) | \rho_\infty)$, one must establish a **Logarithmic Sobolev Inequality (LSI)** for the measure $\rho_\infty dx$:
$$ \mathcal{H}(\rho | \rho_\infty) \le \frac{1}{2\lambda} \mathcal{I}(\rho | \rho_\infty) $$
By the Bakry-Émery $\Gamma_2$-criterion, an LSI holds with constant $\lambda$ if the potential $V$ is uniformly convex, i.e., the Hessian satisfies $\nabla^2 V(x) \ge \lambda I$ for some $\lambda > 0$.

In the **Kinetic (Underdamped) Fokker-Planck Equation**, the state space is the phase space $(x, v) \in \mathbb{R}^d \times \mathbb{R}^d$:
$$ \partial_t f + v \cdot \nabla_x f - \nabla_x V \cdot \nabla_v f = \gamma \nabla_v \cdot (v f + \nabla_v f) $$
Here, the operator is degenerate because the Laplacian $\Delta_v$ acts only on velocities. The generator $L = \mathcal{T} + \mathcal{S}$ is composed of a skew-symmetric transport operator $\mathcal{T} = -v \cdot \nabla_x + \nabla_x V \cdot \nabla_v$ and a symmetric diffusion operator $\mathcal{S} = \gamma \nabla_v \cdot (v \cdot + \nabla_v \cdot)$. Since $[\mathcal{T}, \mathcal{S}] \neq 0$, Hörmander's condition is satisfied, and the system is *hypoelliptic*, leading to *hypocoercive* convergence rather than standard coercivity.

## 3. History & State of the Art (SOTA)

The FPE traces back to Kolmogorov (1931), Fokker, and Planck in statistical mechanics. The modern analytical theory of its convergence is anchored in three major paradigm shifts:

1. **The $\Gamma_2$ Calculus (1985):** Bakry and Émery revolutionized the study of Markov semigroup convergence by introducing the $\Gamma$ and $\Gamma_2$ operators, tying the convergence rate of the FPE to the Ricci curvature of the underlying manifold (or the convexity of the potential $V$).
2. **The JKO Scheme / Wasserstein Gradient Flows (1998):** Jordan, Kinderlehrer, and Otto (JKO) proved that the overdamped FPE is precisely the gradient flow of the free energy $\mathcal{F}(\rho) = \int V\rho + \int \rho \log \rho$ in the space of probability measures equipped with the 2-Wasserstein metric $\mathcal{W}_2$. This geometrized the field, showing that uniform convexity of $V$ corresponds to geodesic convexity of $\mathcal{F}$ in $\mathcal{W}_2$.
3. **Hypocoercivity (2000s):** For kinetic equations where Bakry-Émery fails due to zero coercivity in the spatial direction, Villani (2009) formalized the theory of *hypocoercivity*. By constructing modified entropy functionals involving commutator terms (e.g., $\nabla_x + \nabla_v$), researchers successfully captured the hidden dissipation mechanism.

**SOTA:** Recent breakthroughs have focused on quantitative hypocoercivity (Dolbeault, Mouhot, Schmeiser) avoiding complex commutator bounds via modified $L^2$ norms, and the treatment of non-local McKean-Vlasov equations (Carrillo, McCann, Villani) where the energy functional relies on displacement convexity of interaction kernels.

## 4. Partial Results / Verified Cases

The convergence problem is considered strictly solved in the following configurations:
- **Strictly Convex Potentials:** If $\nabla^2 V \ge \lambda I > 0$, standard LSI and Poincaré inequalities hold. Convergence is exponential with rate $2\lambda$ in relative entropy and $\lambda$ in $\mathcal{W}_2$.
- **Bounded Perturbations of Convexity:** If $V(x) = U(x) + B(x)$ where $U$ is strictly convex and $B$ is bounded ($\|B\|_\infty < \infty$), the Holley-Stroock perturbation lemma guarantees an LSI, though the constant scales exponentially poorly with the oscillation of $B$.
- **Kinetic FPE with Smooth Confining $V$:** Via hypocoercivity, exponential convergence has been proven for kinetic systems with polynomial growth potentials, provided one measures distance in suitably weighted Sobolev spaces or modified entropies.
- **1D Potentials:** By Muckenhoupt criteria, the exact necessary and sufficient conditions on $V(x)$ for spectral gap and LSI in $\mathbb{R}^1$ are completely classified.

## 5. Principal Obstacles

The generic Fokker-Planck convergence problem stalls against three formidable mathematical barriers:

**1. Metastability in Non-Convex Landscapes:** 
When $V(x)$ has multiple deep local minima, the solution density rapidly thermalizes within local wells but transitions between wells very slowly. The time scale for probability mass to cross a saddle point barrier $\Delta E$ is governed by the Eyring-Kramers law: $\tau \sim \exp(\Delta E / kT)$. Consequently, while an LSI may technically exist, the constant degenerates exponentially with barrier height. Standard gradient flow theory provides no constructive insight into the pre-factor of this rate.

**2. Non-Self-Adjointness in Kinetic Equations:**
The kinetic FPE generator is non-symmetric. Its spectrum lies in the complex plane, and standard spectral gap arguments (which rely on the spectral theorem for self-adjoint operators) fail. The generator is highly non-normal, leading to transient growth (pseudospectral effects) where the distance to equilibrium can temporarily increase before exponentially decaying.

**3. Loss of Displacement Convexity in Interactions:**
For non-linear FPEs governed by interaction potentials $W(x,y)$, McCann's condition for displacement convexity requires $W$ to be strictly convex. If $W$ is attractive-repulsive (e.g., Keller-Segel models of chemotaxis or granular media), the free energy functional loses convexity. This leads to phase transitions where the equation no longer possesses a unique stationary state, and solutions may blow up in finite time rather than converging.

## 6. The Gap

The specific theoretical gap dividing the solved from the open lies in bridging **microscopic functional inequalities with singular macroscopic structures**.
1. **The Spectral Gap for Singular Interactions:** Constructing a verifiable criterion for the LSI of the invariant measure associated with McKean-Vlasov equations where $W$ has a singularity at the origin (e.g., Coulombic or Biot-Savart interactions). 
2. **Dimension-Free Bounds for Weakly Convex Geometries:** Establishing dimension-free convergence rates for potentials that are strictly convex at infinity but possess a flat or degenerate region near the origin. Current methods yield rates that vanish as the dimension $d \to \infty$.
3. **Constructive Hypocoercivity with Rough Coefficients:** Extending Villani's commutator calculus to cases where the potential $V(x)$ or the friction coefficient $\gamma(x)$ are only Lipschitz or spatially dependent, breaking the regularity required for iterated Lie brackets $[\mathcal{T}, \mathcal{S}]$.

## 7. Current Research (as of June 2026)

Active schools of thought and contemporary techniques include:

- **Entropic Optimal Transport:** Leveraging Sinkhorn algorithms and Schrödinger bridges to discrete FPEs on graphs. Researchers at MIT and ENS Paris are mapping continuous FPE convergence bounds onto discrete Markov chains using optimal transport geometries.
- **Quantitative Propagation of Chaos:** Linking the convergence of $N$-particle Langevin systems to the macroscopic nonlinear FPE. The frontier lies in achieving bounds that are uniform in both time $t$ and particle number $N$ for mildly singular potentials.
- **Neural Operator Approximations *(frontier — verify)*:** Using deep generative models (like Score-Based Diffusion, which is fundamentally a reverse-time FPE) to empirically approximate the LSI constants of non-convex potentials in high dimensions. The mathematical community is currently attempting to formalize these empirical convergence bounds.
- **Hypocoercivity via $L^2$ Space Splitting:** Following the Dolbeault-Mouhot-Schmeiser framework, simplifying the functional framework of hypocoercivity to require only micro-macro decomposition instead of high-order elliptic regularity, effectively porting kinetic FPE techniques to fractional and non-local operators.

## 8. Future Work

Leading figures such as Cedric Villani, Felix Otto, and José Carrillo have highlighted several strategic directions:
- **Fractional/Lévy Fokker-Planck:** Establishing the equivalent of the JKO scheme and robust functional inequalities for FPEs driven by fractional Laplacians $(-\Delta)^s$, representing anomalous diffusion. The geometric structure of such nonlocal gradient flows is heavily under-explored.
- **Geometry of Non-Equilibrium Steady States (NESS):** Analyzing FPEs with non-conservative drift vectors $b(x) \neq \nabla V(x)$. These systems converge to a NESS with persistent probability currents. Since the detailed balance is broken, the standard Wasserstein gradient flow structure is destroyed, necessitating novel Finsler geometries.
- **Mean-Field Games:** Solving coupled forward-backward FPE systems where convergence to equilibrium must be analyzed simultaneously with a Hamilton-Jacobi-Bellman equation.

## 9. Key References

- **[Foundational]** Bakry, D., & Émery, M. *Diffusions hypercontractives*. Séminaire de Probabilités XIX 1983/84. Springer, 1985.
- **[Foundational]** Jordan, R., Kinderlehrer, D., & Otto, F. *The variational formulation of the Fokker-Planck equation*. SIAM Journal on Mathematical Analysis, 1998.
- **[Survey]** Villani, C. *Hypocoercivity*. Memoirs of the American Mathematical Society, 2009.
- **[SOTA / Recent]** Carrillo, J. A., McCann, R. J., & Villani, C. *Kinetic equilibration rates for granular media and related equations: entropy dissipation and mass transportation estimates*. Revista Matemática Iberoamericana, 2003.
- **[SOTA / Recent]** Dolbeault, J., Mouhot, C., & Schmeiser, C. *Hypocoercivity for linear kinetic equations conserving mass*. Transactions of the American Mathematical Society, 2015.

## 10. Worked Example / Concrete Special Case

The most fundamental concrete instance of FPE convergence is the **Ornstein-Uhlenbeck (OU) process**. 

Let the potential be the strictly quadratic harmonic oscillator: $V(x) = \frac{\lambda}{2} x^2$ for some $\lambda > 0$. The associated overdamped Fokker-Planck equation on $\mathbb{R}$ is:
$$ \partial_t \rho = \partial_x (\lambda x \rho) + \partial_{xx} \rho $$

**1. Identify the Stationary State:**
Set $\partial_t \rho = 0$. We solve $\partial_x (\lambda x \rho + \partial_x \rho) = 0$. Assuming zero flux at infinity, $\partial_x \rho = -\lambda x \rho$. Integrating yields the Gaussian distribution:
$$ \rho_\infty(x) = \sqrt{\frac{\lambda}{2\pi}} \exp\left(-\frac{\lambda}{2} x^2\right) $$

**2. Entropy Dissipation:**
Define the relative entropy $\mathcal{H}(t) = \int \rho(t) \log(\rho(t)/\rho_\infty) dx$. Differentiating with respect to $t$ gives the negative Fisher Information:
$$ \frac{d}{dt} \mathcal{H}(t) = - \int \rho \left( \partial_x \log \frac{\rho}{\rho_\infty} \right)^2 dx =: -\mathcal{I}(\rho | \rho_\infty) $$

**3. Applying the Log-Sobolev Inequality:**
Because $V(x) = \frac{\lambda}{2}x^2$, the Hessian is uniformly bounded below: $\partial_{xx} V = \lambda$. By the Bakry-Émery criterion, the Gaussian measure $\rho_\infty dx$ satisfies an exact LSI:
$$ \mathcal{H}(\rho | \rho_\infty) \le \frac{1}{2\lambda} \mathcal{I}(\rho | \rho_\infty) $$

**4. Exponential Convergence:**
Substitute the LSI into the dissipation equation:
$$ \frac{d}{dt} \mathcal{H}(t) \le -2\lambda \mathcal{H}(t) $$
By Grönwall's inequality, we obtain strict, constructive exponential convergence to the invariant measure without needing spectral analysis of the differential operator:
$$ \mathcal{H}(\rho(t) | \rho_\infty) \le \mathcal{H}(\rho(0) | \rho_\infty) e^{-2\lambda t} $$
This concrete case clearly demonstrates how convexity of the potential directly dictates the rate of convergence via functional inequalities, setting the baseline that researchers attempt to recover in degenerate or non-convex regimes.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*