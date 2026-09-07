---
id: 09-probability/directed-polymer-infinite-volume-limit-2d
title: "Infinite Volume Limit for 2D Directed Polymers"
topic: 09-probability
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Infinite Volume Limit for 2D Directed Polymers

> **Topic:** Probability & Stochastic Processes · **ID:** `09-probability/directed-polymer-infinite-volume-limit-2d` · **Status:** open

## 1. Problem Statement / Conjecture

The central open problem concerning $1+1$ dimensional (often referred to as 2D) directed polymers in a random environment is to rigorously construct and prove the uniqueness of the extremal infinite-volume Gibbs measure for an arbitrary i.i.d. environment and for every fixed asymptotic direction. 

Specifically, consider a polymer path modeled as a directed random walk on $\mathbb{Z}^2$. For a general, non-integrable random environment (e.g., i.i.d. weights with finite exponential moments), the conjecture asserts:
1. **Existence:** For any macroscopic angle/velocity $\theta \in [0, 1]$ parameterizing the asymptotic boundary condition, there exists an infinite-volume limit of the polymer path distribution (an infinite-volume Gibbs measure supported on semi-infinite paths).
2. **Uniqueness:** For each fixed direction $\theta$, there is exactly one extremal, shift-invariant infinite-volume Gibbs measure. 
3. **Busemann Limit:** This unique measure is constructed via the almost-sure limits of Busemann functions (ratios of point-to-point partition functions), which are conjectured to exist and satisfy the cocycle property globally for any typical environment.

A complete proof requires demonstrating that the limiting free energy (or shape function) is strictly concave/convex and differentiable for general noise distributions, thereby preventing the existence of "flat edges" that would cause non-uniqueness or instability in the infinite-volume limit.

## 2. Mathematical Foundations

Let the state space be the planar lattice $\mathbb{Z}^2$. A directed path $\pi$ from $x \in \mathbb{Z}^2$ to $y \in \mathbb{Z}^2$ is a sequence of vertices $x = \pi_0, \pi_1, \dots, \pi_n = y$ such that $\pi_{k} - \pi_{k-1} \in \{e_1, e_2\}$ where $e_1 = (1,0)$ and $e_2 = (0,1)$. The length of the path is $n = (y_1 - x_1) + (y_2 - x_2)$. 

The **random environment** is a family of i.i.d. random variables $\omega = \{\omega_v\}_{v \in \mathbb{Z}^2}$ satisfying the moment condition $\mathbb{E}[e^{\beta \omega_v}] < \infty$ for inverse temperature $\beta > 0$. 

The **point-to-point partition function** from $x$ to $y$ is:
$$ Z_{x,y}^\beta = \sum_{\pi : x \to y} \exp\left( \beta \sum_{v \in \pi} \omega_v \right) $$

If there is no directed path from $x$ to $y$, $Z_{x,y}^\beta = 0$. The finite-volume Gibbs measure on paths from $x$ to $y$ is:
$$ \mu_{x,y}^\beta(\pi) = \frac{1}{Z_{x,y}^\beta} \exp\left( \beta \sum_{v \in \pi} \omega_v \right) $$

An **infinite-volume Gibbs measure** on semi-infinite directed paths $\pi = (\pi_0, \pi_1, \dots)$ starting at $x$ is a probability measure $\mu^\beta$ on the space of paths such that the DLR (Dobrushin-Lanford-Ruelle) condition holds: conditioned on the path passing through a distant vertex $y$, the restriction of the measure to paths from $x$ to $y$ coincides with the finite-volume measure $\mu_{x,y}^\beta$.

The primary mechanism to construct such measures is the **Busemann function**:
$$ B^\theta(x,y) = \lim_{n \to \infty} \left[ \log Z_{x, v_n}^\beta - \log Z_{y, v_n}^\beta \right] $$
where $v_n = (n, \lfloor n\theta \rfloor) \in \mathbb{Z}^2$. If $B^\theta(x,y)$ converges almost surely, it forms an additive cocycle, and the infinite-volume Gibbs measure directed toward $\theta$ can be characterized by transition probabilities proportional to $\exp(B^\theta(x, x+e_i))$.

The **limiting free energy** (or shape function) is defined by Kingman's Subadditive Ergodic Theorem:
$$ g(\theta) = \lim_{n \to \infty} \frac{1}{n} \mathbb{E}\left[ \log Z_{0, v_n}^\beta \right] $$

## 3. History & State of the Art (SOTA)

The problem traces back to the physics literature with Huse and Henley (1985), who studied the pinning of domain walls in 2D Ising systems. The rigorous mathematical framework was established by Imbrie and Spencer (1988) and Bolthausen (1989), who proved that for spatial dimensions $d \ge 3$ (so $1+d$ spacetime), a weak disorder phase exists where the polymer behaves diffusively and the martingale $W_n = Z_n / \mathbb{E}[Z_n]$ converges to a strictly positive limit. 

In $1+1$ dimensions, Comets and Yoshida (1989) proved the environment is always in **strong disorder**: $W_n \to 0$ almost surely, implying the polymer path is heavily localized and exhibits anomalous KPZ fluctuations. 

For general models, Hoffman (2007) made a breakthrough at zero temperature ($\beta = \infty$, First-Passage Percolation), constructing infinite geodesics using Busemann functions. Georgiou, Rassoul-Agha, and Seppäläinen (2017) extended Busemann cocycle theory to positive temperature directed polymers, achieving the SOTA by fully resolving the existence and uniqueness for exactly solvable integrable models (like the Log-Gamma polymer).

The SOTA regarding the macroscopic limit of the $1+1$ D polymer is the construction of the **Directed Landscape** by Dauvergne, Ortmann, and Virág (2018), which acts as the universal scaling limit for integrable models. However, proving general microscopic uniqueness of the Gibbs measure for non-integrable lattice models remains completely open.

## 4. Partial Results / Verified Cases

The conjecture is resolved in the affirmative strictly for **integrable models** and special boundary regimes:

1. **The Log-Gamma Polymer:** Solved by Seppäläinen (2012) and Georgiou et al. (2015). When the weights $e^{\beta \omega_v}$ are distributed according to an inverse gamma distribution, the exact formulas related to the Robinson-Schensted-Knuth (RSK) correspondence and Burke's theorem allow explicit computation of $g(\theta)$. The Busemann functions are proven to exist almost surely for all $\theta$, and the infinite-volume measure is unique.
2. **Strictly Weak / O'Connell-Yor Polymers:** Semi-discrete and strictly weak topologies also exhibit Burke-type properties. Busemann functions and uniqueness are established (Corwin, Seppäläinen, et al.).
3. **Zero-Temperature Limits (First-Passage Percolation):** For continuous weight distributions, Licea and Newman (1996) and Hoffman (2007) proved the existence of semi-infinite geodesics for an uncountable dense set of directions $\theta$, but uniqueness and existence for *every* specific direction remains unresolved for general weights.

## 5. Principal Obstacles

The fundamental bottleneck is the **lack of integrability** for general i.i.d. environments. 

1. **Transversal Fluctuations and KPZ Exponents:** In $1+1$ dimensions, the polymer path fluctuates transversally by $n^{2/3}$ and the free energy fluctuates by $n^{1/3}$. Because the model is heavily localized (strong disorder), classical perturbation theory, functional limit CLTs, and martingale limits fail catastrophically. The limit object is governed by the non-Gaussian KPZ fixed point.
2. **Shape Function Strict Concavity:** Uniqueness of the infinite-volume Gibbs measure is equivalent to proving that the limiting free energy $g(\theta)$ is strictly concave (or strictly convex, depending on sign conventions) and continuously differentiable everywhere. For general environments, we currently lack the geometric or analytic tools to rule out "flat edges" in $g(\theta)$. If $g(\theta)$ had a flat segment, multiple distinct extremal Gibbs measures could share the same macroscopic velocity $\theta$.
3. **Absence of Exact Distributional Identities:** In the Log-Gamma polymer, the Busemann increments along the boundary axes remain independent Gamma variables (stationary measure). No such stationary, shift-invariant measure is explicitly known or writable for a general weight distribution, completely blocking algebraic approaches.

## 6. The Gap

The precise gap is between the **asymptotic scaling regime** (where the Directed Landscape provides the continuum limits via integrable approximation) and the **discrete microscopic lattice** for general distributions. 

To cross this gap, mathematicians must formulate a purely probabilistic robustness argument that does not require determinantal point processes or exact Schur polynomial identities. Specifically, one must prove a generalized version of the Busemann cocycle convergence:
$$ \mathbb{P} \left( \forall x,y, \lim_{n \to \infty} \left[ \log Z_{x, v_n} - \log Z_{y, v_n} \right] \text{ exists and forms a curl-free field} \right) = 1 $$
without relying on exact stationary representations of the field.

## 7. Current Research (as of June 2026)

Active research follows several tracks, mostly anchored by the Busemann process framework developed heavily at the University of Utah (Seppäläinen, Rassoul-Agha) and Wisconsin-Madison. 

1. **Coalescence of Paths:** Bates and Chatterjee have explored the coalescence of polymer paths. Current methodologies attempt to show that for general bounded environments, two semi-infinite polymer paths with the same asymptotic direction $\theta$ must intersect and coalesce almost surely in finite time.
2. **Coupling to the Directed Landscape:** The Virág school is attempting to show that macroscopic geometric features of the general discrete model couple tightly enough to the Directed Landscape to inherit its strict concavity.
3. **Uniform Strict Concavity:** * (frontier — verify) * Recent preprints suggest techniques leveraging chaotic expansion and concentration of measure to bound the curvature of $g(\theta)$ away from zero for specific classes of compactly supported, bounded continuous environments.

## 8. Future Work

Leading mathematicians suggest the following open pathways:
- **Geometric Ergodic Theory:** Generalizing the subadditive ergodic theorems to directly mandate strict concavity for lattice models with super-diffusive transversal fluctuation bounds.
- **Shear Invariance:** Exploiting the statistical shear invariance of the random environment to construct a localized limit mapping from general distributions to the known invariant measures of the KPZ fixed point.
- **Zero-Temperature Reductions:** Resolving the directed First-Passage Percolation uniqueness problem first, then scaling $\beta < \infty$ via low-temperature expansions.

## 9. Key References

- **[Foundational]** Huse, D. A., & Henley, C. L. *Pinning and roughening of domain walls in Ising systems due to random impurities*. Physical Review Letters, 1985.
- **[Foundational]** Imbrie, J. Z., & Spencer, T. *Directed polymers in a random environment*. Journal of Statistical Physics, 1988.
- **[SOTA / Recent]** Dauvergne, C., Ortmann, J., & Virág, B. *The directed landscape*. Acta Mathematica, 2022.
- **[SOTA / Recent]** Janjigian, C., Rassoul-Agha, F., & Seppäläinen, T. *Busemann functions and joint distributions for directed polymers*. Annals of Probability, 2019.
- **[Survey]** Comets, F. *Directed Polymers in Random Environments*. Springer Lecture Notes in Mathematics 2175, 2017.

## 10. Worked Example / Concrete Special Case

To understand how Busemann functions induce an infinite-volume measure, we examine the zero-temperature limit ($\beta \to \infty$), which reduces the point-to-point partition function to the First-Passage Percolation (FPP) longest path (maximum weight path). Here $Z_{x,y}^\infty = \max_{\pi : x \to y} \sum_{v \in \pi} \omega_v$, defined as $L(x,y)$.

Consider a minimal $2 \times 2$ grid on $\mathbb{Z}^2_{\ge 0}$ with vertices from $(0,0)$ to $(2,2)$. We assign deterministic weights to illustrate the Busemann mechanism:
- $\omega(0,0)=1$
- $\omega(1,0)=2, \omega(0,1)=1$
- $\omega(2,0)=1, \omega(1,1)=5, \omega(0,2)=1$
- $\omega(2,1)=2, \omega(1,2)=2$
- $\omega(2,2)=10$

We want to calculate the Busemann increment at the origin in the direction of the target $v = (2,2)$. The increment is $\Delta B(e_1) = L((0,0), v) - L((1,0), v)$. 

1. **Calculate $L((0,0), (2,2))$:**
   The optimal path starting at $(0,0)$ must go through the heavy weights at $(1,1)$ and $(2,2)$. 
   Path 1: $(0,0) \to (1,0) \to (1,1) \to (2,1) \to (2,2)$. 
   Weights: $1 + 2 + 5 + 2 + 10 = 20$.
   Path 2: $(0,0) \to (0,1) \to (1,1) \to (1,2) \to (2,2)$.
   Weights: $1 + 1 + 5 + 2 + 10 = 19$.
   Maximum $L((0,0), (2,2)) = 20$.

2. **Calculate $L((1,0), (2,2))$:**
   Starting at $e_1 = (1,0)$, the path avoids $\omega(0,0)$. 
   Path: $(1,0) \to (1,1) \to (2,1) \to (2,2)$.
   Weights: $2 + 5 + 2 + 10 = 19$.

3. **Calculate the Busemann Function:**
   $B^{(2,2)}((0,0), (1,0)) = 20 - 19 = 1$.
   Similarly for $e_2 = (0,1)$: $L((0,1), (2,2))$ max path is $(0,1) \to (1,1) \to (1,2) \to (2,2)$ yielding $1 + 5 + 2 + 10 = 18$.
   $B^{(2,2)}((0,0), (0,1)) = 20 - 18 = 2$.

At zero temperature, the infinite volume measure is completely localized onto the geodesic. A local walker at $(0,0)$ queries the Busemann gradients to decide its step: since $B((0,0), (1,0)) < B((0,0), (0,1))$ (meaning the "cost to go" from $(1,0)$ is less than from $(0,1)$), the geodesic deterministically steps from $(0,0)$ to $(1,0)$. 

The open problem conjectures that as the target vertex $v_n$ goes to infinity at angle $\theta$, these finite Busemann differences $\log Z(x, v_n) - \log Z(x+e_i, v_n)$ strictly converge almost surely for a random environment, locking in a unique random transition probability for the infinite-volume Gibbs measure at any finite temperature $\beta$.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*