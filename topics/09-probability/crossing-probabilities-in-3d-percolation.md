---
id: 09-probability/crossing-probabilities-in-3d-percolation
title: "Crossing Probabilities in 3D Percolation"
topic: 09-probability
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Crossing Probabilities in 3D Percolation

> **Topic:** Probability & Stochastic Processes · **ID:** `09-probability/crossing-probabilities-in-3d-percolation` · **Status:** open

## 1. Problem Statement / Conjecture

The central open problem in three-dimensional percolation theory is to establish a rigorous uniform bound for the probability that a macroscopic domain is crossed by a connected path of open edges at the critical probability $p_c$, as the scale of the domain tends to infinity. This is the 3D analogue of the celebrated Russo-Seymour-Welsh (RSW) theorem.

Conjecture: Let $\mathbb{P}_{p_c}$ denote the probability measure for critical bond (or site) percolation on the three-dimensional cubic lattice $\mathbb{Z}^3$. For any aspect ratios $\rho_1, \rho_2 > 0$, let $B_R = [0, R] \times [0, \rho_1 R] \times [0, \rho_2 R]$ be a rectangular cuboid. Let $\mathcal{C}(B_R)$ be the event that there exists a continuous path of open edges inside $B_R$ connecting the left face $\{0\} \times [0, \rho_1 R] \times [0, \rho_2 R]$ to the right face $\{R\} \times [0, \rho_1 R] \times [0, \rho_2 R]$. Then, there exist strictly positive constants $c, C \in (0, 1)$, dependent only on $\rho_1, \rho_2$ and not on $R$, such that:

$$ 0 < c \le \mathbb{P}_{p_c}(\mathcal{C}(B_R)) \le C < 1 $$

for all sufficiently large $R$. 

A complete proof requires establishing these uniform bounds, proving that macroscopic crossing probabilities neither vanish to zero nor jump to one at criticality. A complete disproof would require showing that macroscopic scale-invariance breaks down in three dimensions, which would contradict extensive numerical evidence and physical universality.

## 2. Mathematical Foundations

Bernoulli bond percolation is defined on the cubic lattice $\mathbb{L} = (\mathbb{V}, \mathbb{E})$ where $\mathbb{V} = \mathbb{Z}^3$ and $\mathbb{E}$ is the set of nearest-neighbor edges. The state space is $\Omega = \{0, 1\}^{\mathbb{E}}$. The probability measure $\mathbb{P}_p$ is the product measure where each edge $e \in \mathbb{E}$ is assigned state $\omega(e) = 1$ (open) with probability $p$ and $\omega(e) = 0$ (closed) with probability $1 - p$, independently.

The percolation probability, representing the chance that the origin is connected to an infinite open cluster, is defined as:

$$ \theta(p) = \mathbb{P}_p(|C_0| = \infty) $$

where $C_0$ is the connected component of open edges containing the origin. The critical probability $p_c$ is uniquely defined as the threshold of the infinite volume phase transition:

$$ p_c = \sup \{ p \in [0, 1] : \theta(p) = 0 \} $$

In two dimensions, scale invariance is formalized via the Russo-Seymour-Welsh (RSW) theory. Let $A_R(k)$ be the event that an open path crosses a $[0, kR] \times [0, R]$ rectangle in the long direction. The 2D RSW theorem states that if the probability of crossing a square is bounded away from 0, then the probability of crossing an arbitrary rectangle is also bounded away from 0:

$$ \mathbb{P}_{p} (A_R(1)) \ge \delta > 0 \implies \mathbb{P}_{p} (A_R(k)) \ge f_k(\delta) > 0 $$

where $f_k(\delta)$ depends only on $k$ and $\delta$. Because self-duality on the square lattice forces $\mathbb{P}_{p_c}(A_R(1)) = 1/2$, the RSW theorem instantly yields uniform upper and lower bounds for all rectangles at $p_c$. 

In three dimensions, the critical point $p_c(\mathbb{Z}^3) \approx 0.24881$ is strictly less than the threshold for a 2D slice, and lacks exact self-duality. Consequently, the uniform bounding of the macroscopic observable $\mathbb{P}_{p_c}(\mathcal{C}(B_R))$ remains an unresolved foundation for defining a rigorous continuum scaling limit.

## 3. History & State of the Art (SOTA)

The mathematical theory of percolation was introduced by Broadbent and Hammersley in 1957 to model the flow of fluids through porous media. While the model is easily stated, its behavior depends profoundly on the spatial dimension $d$.

For $d=2$, the geometry of critical percolation is deeply understood. Kesten's breakthrough in 1980 proved that $p_c = 1/2$ for bond percolation on $\mathbb{Z}^2$. The RSW theorem (Russo 1978, Seymour and Welsh 1978) established scale-invariance. This culminated in 2001 when Smirnov proved that the scaling limit of site percolation on the triangular lattice is conformally invariant and described by Schramm-Loewner Evolution ($\text{SLE}_6$).

At the other extreme, for high dimensions, the geometry is completely governed by mean-field theory. In 1990, Hara and Slade introduced the lace expansion technique to percolation, proving that for $d \ge 19$, critical percolation behaves like a branching process. This critical dimension threshold was sequentially lowered to $d \ge 11$ for nearest-neighbor models by Fitzner and van der Hofstad in 2017. The theoretical upper critical dimension is known to be $d_c = 6$.

The dimensions $d \in \{3, 4, 5, 6\}$ represent a massive gap in modern probability. 3D percolation, being the most physically relevant dimension, has been isolated as a foundational problem. Grimmett (1999) highlighted the 3D RSW theorem as the fundamental bottleneck for studying the phase transition. Currently, the state of the art for 3D relies heavily on computational Monte Carlo simulations (such as those by Ziff and Grassberger), which strongly support the existence of scale-invariant crossing probabilities, yet rigorous mathematical bounds remain elusive.

## 4. Partial Results / Verified Cases

While the general conjecture for $\mathbb{Z}^3$ remains open, the behavior of crossing probabilities has been verified in several specific limiting cases and geometries:

1. **Two-Dimensional Lattices ($d=2$):** As noted, the conjecture is fully solved for $\mathbb{Z}^2$ and the triangular lattice. Crossing probabilities are conformally invariant, uniquely given by Cardy's Formula.
2. **High Dimensions ($d \ge 11$):** Using lace expansion, it is proven that crossing probabilities exhibit mean-field scaling. Depending on boundary conditions, macroscopic crossing probabilities either vanish asymptotically (scaling as $R^{6-d}$) or jump to 1, as the paths behave like highly separated random walks.
3. **Thick Slabs:** The Grimmett-Marstrand Theorem (1990) proves that critical percolation on a slab $\mathbb{S}_k = \mathbb{Z}^2 \times \{0, \dots, k\}$ for any finite thickness $k$ undergoes a phase transition analogous to 2D percolation, with $p_c(\mathbb{S}_k) < p_c(\mathbb{Z}^2)$. The RSW bounds hold for any finite $k$, but the bounding constants degrade drastically as $k \to \infty$, failing to generalize to the full $\mathbb{Z}^3$ lattice.
4. **Spread-out Models ($d > 6$):** If the model is generalized to allow edges between vertices at distance $L$, the lace expansion successfully resolves crossing bounds for dimensions strictly above the upper critical dimension $d_c = 6$, provided $L$ is sufficiently large.

## 5. Principal Obstacles

The intractability of the 3D percolation problem stems from the simultaneous failure of the two primary mathematical engines used in spatial probability:

**1. Topological Planarity and Lack of Self-Duality:**
In 2D, the dual of a planar graph is another planar graph (e.g., the dual of $\mathbb{Z}^2$ is a shifted $\mathbb{Z}^2$). Crucially, a left-to-right open path in a square completely blocks any top-to-bottom closed path in the dual lattice. This binary topological barrier (an application of the Jordan Curve Theorem) allows contour arguments to forcefully link crossing probabilities in different directions. In $\mathbb{Z}^3$, this duality collapses. The dual of a 1D path is a 2D surface of plaquettes. To block a 1D path of open edges crossing a 3D box, one must construct a 2D surface of closed edges. The geometric and entropic asymmetry between 1D curves and 2D surfaces destroys the symmetric contour arguments that make 2D RSW possible.

**2. The Absence of the Virasoro Algebra:**
In 2D, the assumption of local scale and rotation invariance at criticality promotes to full conformal invariance because the local conformal group is infinite-dimensional (described by the Virasoro algebra). In 3D, Liouville's Theorem restricts the conformal group to the finite-dimensional Möbius group. Consequently, there is no infinite-dimensional symmetry to uniquely constrain the macroscopic crossing probabilities, meaning an exact analytic solution akin to Cardy's Formula is highly unlikely to exist.

**3. Breakdown of Mean-Field Perturbation:**
Lace expansion relies heavily on paths avoiding each other (low intersection probabilities). In $d=3$, simple random walks are transient but highly entangled; their intersection probability is highly relevant. Perturbative expansions around a mean-field (tree-like) cluster geometry diverge in 3D, rendering high-dimensional techniques useless.

## 6. The Gap

The exact boundary between what is mathematically proven and the general statement lies at establishing a scale-free geometric observable. Currently, if one considers a sequence of cubes $B_R = [0, R]^3$, it is not rigorously known whether $\mathbb{P}_{p_c}(\mathcal{C}(B_R))$ converges to a constant strictly between 0 and 1, oscillates indefinitely, decays to zero, or converges to one. 

To bridge this gap, a completely novel topological linkage must be discovered that relates the probability of 1D path crossings to the geometry of 3D domains without relying on planar duality or mean-field limits. Proving that $0 < c \le \mathbb{P}_{p_c}(\mathcal{C}(B_R)) \le C < 1$ is the singular step required to prove that a non-trivial universal scaling limit exists for 3D continuous percolation.

## 7. Current Research (as of June 2026)

Active mathematical and physical research is divided into three major camps:

- **The Conformal Bootstrap:** Drawing from theoretical physics (e.g., El-Showk, Simmons-Duffin), researchers are applying the conformal bootstrap to $O(N)$ models. Because percolation can be formulated as the $q \to 1$ limit of the $q$-state Potts model (which is mathematically linked to $O(N \to 0)$ models), bootstrap numerical constraints on CFT operator dimensions provide the most precise estimates of 3D critical exponents (e.g., $\nu \approx 0.876$). Translating these algebraic CFT constraints into rigorous probability bounds remains a major frontier.
- **Entropic and Isoperimetric Bounds:** Groups in geometric probability (including researchers at IHES and Geneva) are attempting to replace exact topological duality with probabilistic entropic inequalities, seeking modified logarithmic Sobolev inequalities or BKS (Benjamini-Kalai-Schramm) noise sensitivity theorems tailored to 3D surfaces.
- **Probabilistic Cellular Automata:** Attempting to build an analogue of the SLE by studying the Markovian evolution of 2D surfaces (the boundaries of 3D clusters) rather than 1D curves. *(frontier — verify)*

## 8. Future Work

Leading probabilists suggest several strategic pathways forward:
- **Discovering a 3D Parafermionic Observable:** In 2D, Smirnov's proof relied on an exactly solvable discrete holomorphic observable on the triangular lattice. A major open challenge is to construct a lattice-level vector or tensor field in 3D that satisfies a discrete analogue of a conformal conservation law, providing a local martingale for the phase transition.
- **Coarse-Graining and Renormalization:** Formulating a rigorous, non-perturbative real-space renormalization group map for $\mathbb{Z}^3$ percolation that possesses a non-trivial fixed point. 
- **Surface Duality:** Developing a rigorous probabilistic framework for the scaling limit of random 2D surfaces (plaquette percolation) and proving a "surface-RSW" theorem, which could indirectly yield bounds on 1D path crossings.

## 9. Key References

- **[Foundational]** Broadbent, S. R., & Hammersley, J. M. *Percolation processes: I. Crystals and mazes.* Mathematical Proceedings of the Cambridge Philosophical Society, Vol. 53, No. 3. Cambridge University Press, 1957. 
- **[Foundational]** Grimmett, G. *Percolation.* (2nd ed.). Grundlehren der mathematischen Wissenschaften, Springer, 1999.
- **[SOTA / Recent]** Fitzner, R., & van der Hofstad, R. *Mean-field behavior for nearest-neighbor percolation in $d \ge 11$.* Electronic Journal of Probability, 22(43), 1-65, 2017.
- **[SOTA / Recent]** El-Showk, S., Paulos, M. F., Poland, D., Rychkov, S., Simmons-Duffin, D., & Vichi, A. *Solving the 3D Ising model with the conformal bootstrap.* Physical Review D, 86(2), 2012.
- **[Survey]** Duminil-Copin, H. *Sixty years of percolation.* arXiv preprint arXiv:1712.00898 (Bonn Mathematical Society lecture), 2017.

## 10. Worked Example / Concrete Special Case

To clearly illustrate the crossing probability mechanics and the lack of planar containment, consider the absolute smallest 3D domain: a single $1 \times 1 \times 1$ cubic cell on the $\mathbb{Z}^3$ lattice.

Let the set of vertices be $\mathbb{V} = \{0, 1\}^3$. The edges $\mathbb{E}$ consist of the 12 segments of unit length forming the cube. Let the bond percolation probability be $p$. We wish to find the probability of the crossing event $\mathcal{C}(B_1)$, defined as the existence of an open path from the left face $F_0$ (where $x = 0$) to the right face $F_1$ (where $x = 1$).

The left face $F_0$ contains 4 vertices: $(0,0,0), (0,0,1), (0,1,0), (0,1,1)$. 
The right face $F_1$ contains 4 vertices: $(1,0,0), (1,0,1), (1,1,0), (1,1,1)$.

A crossing exists if any vertex in $F_0$ can reach any vertex in $F_1$ via open edges. Notice that any path originating in $F_0$ and terminating in $F_1$ must, by definition, traverse at least one edge that strictly connects $F_0$ to $F_1$. In a $1 \times 1 \times 1$ cube, the only edges spanning the gap between these two faces are the 4 direct edges parallel to the $x$-axis (e.g., the edge connecting $(0,0,0)$ to $(1,0,0)$). The other 8 edges lie entirely within $F_0$ or entirely within $F_1$. 

Therefore, a path from $F_0$ to $F_1$ exists if and only if at least one of these 4 transverse edges is open. The states of the 8 facial edges are irrelevant to this specific definition of face-to-face crossing in a single unit cell. Because the edges are independent Bernoulli trials, the exact polynomial for the crossing probability is simply:

$$ \mathbb{P}_p(\mathcal{C}(B_1)) = 1 - \mathbb{P}_p(\text{all 4 transverse edges are closed}) = 1 - (1 - p)^4 $$

For 3D critical bond percolation, numerical results place $p_c \approx 0.2488$. Plugging this in yields:

$$ \mathbb{P}_{p_c}(\mathcal{C}(B_1)) = 1 - (1 - 0.2488)^4 \approx 1 - 0.3184 = 0.6816 $$

In 2D on a $1 \times 1$ square at critical probability $p_c = 0.5$, the equivalent calculation for crossing from the left edge (2 vertices) to the right edge (2 vertices) using 2 transverse edges is $1 - (1 - 0.5)^2 = 0.75$. 

While this $1 \times 1 \times 1$ exact calculation is trivial, it highlights the core geometric reality: at scale $R=1$, the crossing probability is bounded firmly between 0 and 1. As $R$ expands to $R=2$ and beyond, paths can detour through the dense, highly-connected interior volume of the box in ways that cannot be contained by dual curves. Evaluating whether this polynomial cascade stabilizes to a constant $C \in (0,1)$ as $R \to \infty$, rather than decaying to $0$, is the essence of the unsolved 3D RSW conjecture.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*