---
id: 06-pdes/ericksen-leslie-liquid-crystals
title: "Ericksen Leslie Liquid Crystals"
topic: 06-pdes
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Ericksen-Leslie Equations for Nematic Liquid Crystals

> **Topic:** Partial Differential Equations · **ID:** `06-pdes/ericksen-leslie-liquid-crystals` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

The Ericksen-Leslie equations describe the macroscopic hydrodynamics of nematic liquid crystals, bridging complex non-Newtonian fluid mechanics with the topological dynamics of directional order. The system mathematically couples the incompressible Navier-Stokes equations for the fluid flow with a harmonic map heat flow into the sphere $\mathbb{S}^2$ for the molecular director field.

The primary open mathematical question (often referred to as the global regularity problem for liquid crystal flows) is whether smooth, finite-energy initial data yields a globally existing smooth solution in three spatial dimensions ($\mathbb{R}^3$), or if solutions can develop finite-time singularities (blow-up). Furthermore, establishing the uniqueness and full partial regularity of global weak solutions in $\mathbb{R}^3$ for the complete, multi-constant physical model remains a profound mathematical challenge. A complete proof must either provide a unified mechanism that bounds the geometric energy concentration to prevent blow-up, or rigorously construct a finite-time singularity directly driven by topological defect formation interacting with the fluid velocity.

## 2. Mathematical Foundations

Let $\Omega \subset \mathbb{R}^n$ (where $n=2$ or $3$) be a smooth domain. The macroscopic state of an incompressible nematic liquid crystal is characterized by the fluid velocity vector field $v: \Omega \times [0, T) \to \mathbb{R}^n$, the scalar hydrostatic pressure $P: \Omega \times [0, T) \to \mathbb{R}$, and the molecular director field $d: \Omega \times [0, T) \to \mathbb{S}^2$, representing the averaged local alignment of rod-like molecules. 

The full hydrodynamic system is governed by the conservation of linear momentum, the incompressibility constraint, and the balance of angular momentum (the director equation):

$$ \rho (\partial_t v + (v \cdot \nabla) v) = - \nabla P + \nabla \cdot (\sigma^E + \sigma^L) $$
$$ \nabla \cdot v = 0 $$
$$ \partial_t d + (v \cdot \nabla) d = \omega d + \gamma (h - (h \cdot d)d) $$

Here, $\rho$ is the fluid density, $\omega = \frac{1}{2}(\nabla v - (\nabla v)^T)$ is the vorticity tensor, and $A = \frac{1}{2}(\nabla v + (\nabla v)^T)$ is the strain rate tensor. The internal molecular field $h$ is defined via the variational derivative of the Oseen-Frank free energy density $W(d, \nabla d)$:

$$ W(d, \nabla d) = \frac{K_1}{2} (\nabla \cdot d)^2 + \frac{K_2}{2} (d \cdot (\nabla \times d))^2 + \frac{K_3}{2} |d \times (\nabla \times d)|^2 $$

The Ericksen stress tensor $\sigma^E$, derived from elastic distortions, is given by $\sigma^E_{ij} = - \frac{\partial W}{\partial (\partial_j d_k)} \partial_i d_k$. The Leslie stress tensor $\sigma^L$ models viscous dissipation and anisotropic coupling:

$$ \sigma^L_{ij} = \alpha_1 (d_k A_{kp} d_p) d_i d_j + \alpha_2 N_i d_j + \alpha_3 d_i N_j + \alpha_4 A_{ij} + \alpha_5 A_{ik} d_k d_j + \alpha_6 d_i A_{jk} d_k $$

where $N = \partial_t d + (v \cdot \nabla) d - \omega d$ is the co-rotational time derivative of the director. To satisfy thermodynamic laws of energy dissipation, the Leslie viscosity coefficients $\alpha_1, \dots, \alpha_6$ must satisfy Parodi's relation: $\alpha_2 + \alpha_3 = \alpha_6 - \alpha_5$.

In the standard mathematical literature, the system is simplified using the one-constant approximation ($K_1=K_2=K_3=1$), leading to $W = \frac{1}{2}|\nabla d|^2$ and $h = \Delta d$. Neglecting complex viscous couplings ($\alpha_1=\alpha_2=\alpha_3=\alpha_5=\alpha_6=0$ and $\alpha_4 = 2\mu$), the system reduces to the simplified Lin-Liu model:

$$ \partial_t v + (v \cdot \nabla) v + \nabla P = \mu \Delta v - \nabla \cdot \left( \nabla d \odot \nabla d \right) $$
$$ \nabla \cdot v = 0 $$
$$ \partial_t d + (v \cdot \nabla) d = \Delta d + |\nabla d|^2 d $$

where $(\nabla d \odot \nabla d)_{ij} = \sum_k \partial_i d_k \partial_j d_k$. This system obeys the fundamental energy dissipation law:

$$ \frac{1}{2} \frac{d}{dt} \int_\Omega \left( |v|^2 + |\nabla d|^2 \right) dx + \int_\Omega \left( \mu |\nabla v|^2 + \left| \Delta d + |\nabla d|^2 d \right|^2 \right) dx = 0 $$

## 3. History & State of the Art (SOTA)

The continuum theory was first formulated physically by J. L. Ericksen (1961) for the statics of nematics, and extended to hydrodynamics by F. M. Leslie (1968). The rigorous partial differential equation analysis of these models commenced decades later.

In 1989, F.-H. Lin initiated the deep mathematical study of both the static Oseen-Frank equations and dynamic simplifications. To circumvent the severe non-linear constraint $d \in \mathbb{S}^2$, Lin and Liu (1995) introduced a penalized Ginzburg-Landau functional $E_\varepsilon(d) = \frac{1}{2}\int |\nabla d|^2 + \frac{1}{4\varepsilon^2}\int (1-|d|^2)^2$, successfully proving the global existence of classical solutions in 2D and weak solutions in 3D for the penalized system.

The constraint $|d|=1$ poses extreme challenges because it forces energy to concentrate at points or curves, leading to topological defects. In 2010, Lin, Lin, and Wang achieved a major breakthrough by proving the existence of global weak solutions for the exact-sphere model in 2D, demonstrating that solutions are smooth except at finitely many times where point singularities form.

By 2016, Lin and Wang proved the global existence of weak solutions in 3D for the simplified system, requiring a highly intricate compactness framework based on defect measures. 

**State of the Art:** The existence of global smooth solutions in 3D for arbitrary large initial data remains completely unsolved. For the full, unsimplified Ericksen-Leslie system, even global weak existence in 3D is only partially understood under strict structural assumptions on the Leslie coefficients. Uniqueness of weak solutions in 3D is similarly unresolved.

## 4. Partial Results / Verified Cases

- **2D Global Existence:** For bounded 2D domains, global weak solutions exist. Furthermore, they are smooth everywhere except at at most finitely many singular times $0 < t_1 < t_2 < \dots < t_L < \infty$ where harmonic map "bubbles" separate, causing a finite jump in the energy.
- **3D Local Well-Posedness:** For smooth initial data $(v_0, d_0) \in H^s \times H^{s+1}$ ($s > \frac{3}{2}$), a unique strong solution exists on a local time interval $[0,T)$. 
- **Small Data Global Existence in 3D:** If the initial perturbations are sufficiently small—specifically, if $\|v_0\|_{L^3(\mathbb{R}^3)} + \|\nabla d_0\|_{L^3(\mathbb{R}^3)}$ or norms in suitable Besov/BMO spaces are bounded by a small $\epsilon_0$—the unique smooth solution exists globally in time.
- **Global Weak Solutions (Simplified 3D Model):** A pair $(v,d)$ is established as a global weak solution with $v \in L^\infty(0,T; L^2) \cap L^2(0,T; H^1)$ and $d \in L^\infty(0,T; H^1) \cap L^2(0,T; H^2)$. 
- **Partial Regularity:** Drawing on the Caffarelli-Kohn-Nirenberg theory for Navier-Stokes, it is proven that for suitable weak solutions of the 3D simplified model, the singular set $\Sigma \subset \mathbb{R}^3 \times (0, \infty)$ where the solution is not smooth has one-dimensional parabolic Hausdorff measure zero ($\mathcal{P}\text{-}\mathcal{H}^1(\Sigma) = 0$).

## 5. Principal Obstacles

**Supercriticality of the Harmonic Map Heat Flow:** The director equation $\partial_t d = \Delta d + |\nabla d|^2 d$ is energy-supercritical in three dimensions. The natural energy bound provides $\nabla d \in L^\infty(L^2)$. Consequently, the non-linear term $|\nabla d|^2 d$ belongs merely to $L^1$, which is insufficiently regular for standard parabolic bootstrapping, violating the required conditions to leverage standard Sobolev embeddings.

**Defect Dynamics and Bubbling:** Nematic liquid crystals inherently form topological defects to minimize energy across boundary constraints. Mathematically, these defects represent singular points where the director field maps non-trivially onto $\mathbb{S}^2$. As a defect forms dynamically, energy concentrates, and the gradient $|\nabla d|$ blows up locally. This produces a highly singular forcing term $-\nabla \cdot (\nabla d \odot \nabla d)$ that is injected directly into the momentum equation of the Navier-Stokes flow. It is unknown if this force is capable of destroying the regularity of the fluid velocity $v$.

**Tensor Nonlinearities and Loss of Maximum Principle:** In the full Ericksen-Leslie model, the complex viscosity terms in the Leslie stress tensor $\sigma^L$ couple the fluid strain $A$ and vorticity $\omega$ strongly to the director derivative $N$. When relying on approximation schemes (like the Ginzburg-Landau penalty), this cross-coupling disrupts maximum principles. It becomes extraordinarily difficult to prove that the approximate director length $|d^\varepsilon|$ remains bounded by 1, breaking the foundation of weak compactness arguments.

## 6. The Gap

The central mathematical gap lies between weak existence (characterized by bounded energy but potential singularities of low Hausdorff dimension) and classical global existence. Mathematics currently lacks a unified theory of "defect-fluid interaction". Specifically, we do not have the analytical tools to determine whether the fluid transport $(v \cdot \nabla) d$ acts to regularize and disperse concentrating energy (suppressing blow-up), or if the topological stress $-\nabla \cdot (\nabla d \odot \nabla d)$ inevitably overpowers fluid viscosity, leading to simultaneous finite-time singular ruptures in both the director field and the fluid velocity field. Bridging this gap requires either a fundamentally new monotonicity formula that couples geometry with fluid mechanics, or a rigorous numerical-analytical blow-up construction.

## 7. Current Research (as of June 2026)

- **Finite-Time Blow-Up Constructions:** A major priority is attempting to construct rigorous finite-time blow-up solutions for the 3D simplified system. Researchers are adapting known blow-up profiles from the isolated harmonic map heat flow (building on works by Raphael, Schweyer, and others) and coupling them to fluid flows to force a singularity. *(frontier — verify)*
- **Weak-Strong Uniqueness:** Establishing weak-strong uniqueness principles; proving that if a strong solution exists on an interval, any suitable weak solution must coincide identically with it.
- **Active Nematics:** A booming area of research extends these equations to biological fluids (e.g., microtubule networks driven by kinesin). This involves adding an active stress term $\sigma^{active} = \zeta d \otimes d$ to the Navier-Stokes equation. The activity parameter $\zeta$ acts as an internal energy source, breaking the fundamental dissipative energy equality and leading to "active turbulence"—spontaneous chaotic flows driven by constant creation and annihilation of $\pm 1/2$ defects.
- **Stochastic Formulations:** Introducing stochastic forcing to the Navier-Stokes component to study whether noise regularizes the defect formation, mirroring similar efforts in standard fluid dynamics.

## 8. Future Work

- **Resolution of the 3D Global Regularity Problem:** Definitively construct a counterexample (finite-time blow-up for smooth initial data) or prove global regularity for the simplified Ericksen-Leslie system in $\mathbb{R}^3$.
- **Full Ericksen-Leslie Framework:** Establish global weak existence and partial regularity for the non-isothermal, fully coupled Ericksen-Leslie system without imposing unphysical symmetry constraints on the Leslie coefficients or simplifying the Oseen-Frank energy.
- **Defect Tracking:** Develop a rigorous measure-valued or varifold weak formulation capable of explicitly tracking the trajectories and collisions of line and point defects dynamically through the 3D fluid field after they form.

## 9. Key References

- **[Foundational]** Ericksen, J. L. *Conservation laws for liquid crystals.* Transactions of the Society of Rheology, 1961.
- **[Foundational]** Leslie, F. M. *Some constitutive equations for liquid crystals.* Archive for Rational Mechanics and Analysis, 1968.
- **[Foundational]** Lin, F.-H., & Liu, C. *Nonparabolic dissipative systems modeling the flow of liquid crystals.* Communications on Pure and Applied Mathematics, 1995.
- **[SOTA / Recent]** Lin, F.-H., Lin, J., & Wang, C. *Liquid crystal flows in two dimensions.* Archive for Rational Mechanics and Analysis, 2010.
- **[SOTA / Recent]** Lin, F.-H., & Wang, C. *Global existence of weak solutions of the nematic liquid crystal flow in dimension three.* Communications on Pure and Applied Mathematics, 2016.
- **[Survey]** Lin, F.-H., & Wang, C. *Recent developments of analysis for hydrodynamic flow of nematic liquid crystals.* Philosophical Transactions of the Royal Society A, 2014.

## 10. Worked Example / Concrete Special Case

To ground the abstract equations, consider a static, steady-state configuration where the fluid is strictly at rest ($v = 0$) in $\mathbb{R}^3$. Under this condition, the coupled Ericksen-Leslie system reduces entirely to the harmonic map equation for the director field:

$$ \Delta d + |\nabla d|^2 d = 0 $$

A classic topological defect solution is the radial "hedgehog" configuration, where liquid crystal molecules point directly radially outward from the origin. For a position vector $x = (x_1, x_2, x_3)$ and radius $r = \sqrt{x_1^2 + x_2^2 + x_3^2}$, the director is:

$$ d(x) = \frac{x}{r}, \quad \text{for } x \neq 0 $$

We can rigorously verify this is a steady-state solution. First, we compute the spatial derivatives. Using the quotient rule, $\partial_j d_i = \partial_j \left( \frac{x_i}{r} \right) = \frac{\delta_{ij}}{r} - \frac{x_i x_j}{r^3}$. 

Next, we evaluate the gradient magnitude squared, $|\nabla d|^2$. Summing over all components:
$$ |\nabla d|^2 = \sum_{i,j=1}^3 \left( \frac{\delta_{ij}}{r} - \frac{x_i x_j}{r^3} \right)^2 = \sum_{i,j=1}^3 \left( \frac{\delta_{ij}}{r^2} - \frac{2\delta_{ij} x_i x_j}{r^4} + \frac{x_i^2 x_j^2}{r^6} \right) $$
Using the identities $\sum_i x_i^2 = r^2$ and $\sum_i \delta_{ii} = 3$, we find:
$$ |\nabla d|^2 = \frac{3}{r^2} - \frac{2r^2}{r^4} + \frac{r^4}{r^6} = \frac{2}{r^2} $$

Now, we compute the Laplacian $\Delta d_i$:
$$ \Delta d_i = \sum_{j=1}^3 \partial_j \left( \frac{\delta_{ij}}{r} - \frac{x_i x_j}{r^3} \right) = \sum_{j=1}^3 \left( -\frac{\delta_{ij} x_j}{r^3} - \frac{\delta_{ij} x_j + \delta_{jj} x_i}{r^3} + \frac{3 x_i x_j^2}{r^5} \right) $$
$$ \Delta d_i = -\frac{x_i}{r^3} - \frac{x_i + 3x_i}{r^3} + \frac{3x_i r^2}{r^5} = -\frac{2x_i}{r^3} $$

Substituting these directly into the PDE gives:
$$ \Delta d_i + |\nabla d|^2 d_i = -\frac{2x_i}{r^3} + \left(\frac{2}{r^2}\right) \frac{x_i}{r} = 0 $$

This holds everywhere for $x \neq 0$. At the origin ($x=0$), the director is mathematically undefined, representing a point defect with concentrated energy density $\frac{1}{2}|\nabla d|^2 = \frac{1}{r^2}$. 

While the hedgehog is a static solution, its dynamic implications are severe. If such a topological defect attempts to form dynamically during an active flow, the localized geometric stress tensor $-\nabla \cdot (\nabla d \odot \nabla d)$ injects an intense, concentrated force into the Navier-Stokes equations precisely at the defect center. This mechanism perfectly illustrates how topology impacts hydrodynamics, and it remains the exact mathematical barrier preventing proofs of global smooth existence.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*