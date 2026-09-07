---
id: 03-geometry/crepant-resolution-conjecture
title: "Crepant Resolution Conjecture"
topic: 03-geometry
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Crepant Resolution Conjecture

> **Topic:** Algebraic & Differential Geometry · **ID:** `03-geometry/crepant-resolution-conjecture` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

The Crepant Resolution Conjecture (CRC) asserts a profound mathematical equivalence between the enumerative geometry of a complex orbifold and the enumerative geometry of its crepant resolution. 

Formally, let $\mathcal{X}$ be a complex Gorenstein orbifold (or a smooth Deligne-Mumford stack) such that its coarse moduli space $X$ admits a crepant resolution of singularities $\pi: Y \to X$. The conjecture postulates that the Gromov-Witten (GW) theory of the orbifold $\mathcal{X}$ and the Gromov-Witten theory of the smooth manifold $Y$ are equivalent. This equivalence is not a simple isomorphism of invariants; rather, it states that after an appropriate analytic continuation of the Gromov-Witten potentials—formal power series generating these invariants—and a highly non-trivial change of variables mapping the quantum parameters (Kähler moduli) of $Y$ to the twisted sector parameters of $\mathcal{X}$, the quantum structures of $\mathcal{X}$ and $Y$ are canonically isomorphic. 

At the genus-zero level, a complete proof of the conjecture requires demonstrating an isomorphism of the underlying Frobenius manifolds (or equivalently, an equivalence of their Givental Lagrangian cones). At higher genera, the conjecture demands that the higher-genus Gromov-Witten potentials of $\mathcal{X}$ map exactly to those of $Y$ under the quantization of this symplectic transformation.

## 2. Mathematical Foundations

The formulation of the CRC relies heavily on algebraic geometry, intersection theory on moduli spaces, and symplectic geometry.

**Orbifolds and Crepant Resolutions:**
Let $\mathcal{X}$ be a smooth Deligne-Mumford stack over $\mathbb{C}$. Its coarse moduli space $X$ typically possesses quotient singularities. A resolution of singularities $\pi: Y \to X$, where $Y$ is a smooth variety, is called *crepant* if it preserves the canonical class:
$$ \pi^* K_X = K_Y $$
This condition ensures that both $\mathcal{X}$ and $Y$ share the same Calabi-Yau geometry (e.g., if one has trivial canonical bundle, so does the other).

**Chen-Ruan Orbifold Cohomology:**
The state space for the Gromov-Witten theory of $\mathcal{X}$ is the Chen-Ruan orbifold cohomology ring, $H_{CR}^*(\mathcal{X}, \mathbb{C})$. This space is additively defined as the ordinary singular cohomology of the inertia stack $I\mathcal{X}$:
$$ I\mathcal{X} = \mathcal{X} \times_{\mathcal{X} \times \mathcal{X}} \mathcal{X} \cong \coprod_{(g)} \mathcal{X}_{(g)} $$
where $\mathcal{X}_{(g)}$ represent the twisted sectors (components corresponding to conjugacy classes of local stabilizer groups). The degree of a class in a twisted sector is shifted by a rational number called the *age* (or degree shift), which measures the action of the stabilizer on the tangent space. 

**Gromov-Witten Invariants:**
For $Y$, Gromov-Witten invariants are defined as intersection numbers on the moduli space of stable maps $\overline{M}_{g,n}(Y, \beta)$, where $\beta \in H_2(Y, \mathbb{Z})$. For $\mathcal{X}$, one utilizes the moduli space of *twisted* stable maps (or orbifold stable maps) $\overline{M}_{g,n}(\mathcal{X}, \beta)$. The invariants are denoted:
$$ \langle \gamma_1, \dots, \gamma_n \rangle_{g, n, \beta}^{\mathcal{X}} \quad \text{and} \quad \langle \alpha_1, \dots, \alpha_n \rangle_{g, n, \beta'}^Y $$
where $\gamma_i \in H_{CR}^*(\mathcal{X})$ and $\alpha_i \in H^*(Y)$. 

**Givental's Symplectic Formalism:**
To state the genus-zero CRC rigorously, one uses Givental's symplectic vector space $\mathcal{H} = H \otimes \mathbb{C}(\!(z^{-1})\!)$, where $H$ is the respective state space ($H_{CR}^*(\mathcal{X})$ or $H^*(Y)$) and $z$ is a formal parameter representing the equivariant parameter of the circle action on loop spaces. The space is equipped with a symplectic form:
$$ \Omega(f, g) = \text{Res}_{z=0} (f(-z), g(z)) dz $$
The genus-zero Gromov-Witten theory defines a Lagrangian cone $\mathcal{L} \subset \mathcal{H}$. The CRC states that there is a linear symplectic isomorphism $\mathbb{U}: \mathcal{H}_{\mathcal{X}} \to \mathcal{H}_Y$ and a change of variables (analytic continuation) such that $\mathbb{U}(\mathcal{L}_{\mathcal{X}}) = \mathcal{L}_Y$.

## 3. History & State of the Art (SOTA)

The genesis of the Crepant Resolution Conjecture traces back to physics, specifically string theory on orbifolds. In 1985, Dixon, Harvey, Vafa, and Witten realized that the Hilbert space of closed strings on an orbifold requires the inclusion of "twisted sectors" (strings closing only up to a group element) to maintain modular invariance. Vafa and Zaslow (1993) later provided topological calculations supporting this geometry.

The rigorous mathematical formulation began with Chen and Ruan's definition of orbifold cohomology (2001, 2004). Shortly after, Ruan formulated the *Cohomological Crepant Resolution Conjecture*, stating that $H_{CR}^*(\mathcal{X}, \mathbb{C})$ and $H^*(Y, \mathbb{C})$ are isomorphic as graded rings (after extending scalars to account for quantum corrections in the classical limit).

In 2009, Bryan and Graber formulated the quantum (genus-zero) CRC for Hard Lefschetz targets, explicitly introducing the necessary analytic continuation and the change of variables mapping orbifold variables to the Novikov variables $Q$. Simultaneously, Coates, Corti, Iritani, and Tseng (CCIT) utilized Givental's symplectic formalism to state a universally applicable genus-zero CRC, which they proved for all toric orbifolds.

Currently, the state of the art focuses on higher-genus formulations and categorical GW theory. Milanov and Tseng, alongside Coates and Iritani, have developed higher-genus CRC frameworks relying on Givental's quantization of quadratic Hamiltonians. Furthermore, Gauged Linear Sigma Models (GLSMs) have become the preeminent tool for analyzing the wall-crossing phenomena between the orbifold and resolution phases.

## 4. Partial Results / Verified Cases

The Crepant Resolution Conjecture is a highly active area of research and has been definitively verified in several substantial geometric domains:

- **Toric Orbifolds (Genus Zero):** Coates, Corti, Iritani, and Tseng (2009) established the conjecture for all toric orbifolds $\mathcal{X}$ that admit a projective toric crepant resolution $Y$. Their proof uses mirror symmetry to relate the GW invariants of both spaces to oscillating integrals of a common Landau-Ginzburg model.
- **Surface Singularities:** For ADE (Kleinian) surface singularities $\mathbb{C}^2/\Gamma$ where $\Gamma \subset SL(2, \mathbb{C})$ is finite, Bryan and Graber, and later CCIT, proved the conjecture.
- **Symmetric Products and Hilbert Schemes:** A monumental achievement was verifying the CRC for the orbifold $\mathcal{X} = [S^n / \Sigma_n]$ (the symmetric product stack of a smooth algebraic surface $S$) and its crepant resolution $Y = \text{Hilb}^{[n]}(S)$, the Hilbert scheme of points. This builds heavily on the Nakajima oscillator algebra and the work of Lehn, Li, Qin, and Wang.
- **Higher Genus for Specific Targets:** The higher-genus CRC has been proven for specific classes, such as one-dimensional quotients (e.g., $[\mathbb{C}/\mathbb{Z}_r]$) and localized invariants of toric Calabi-Yau threefolds, using techniques from topological recursion (Chekhov-Eynard-Orantin).
- **Flops:** A variant of the conjecture comparing two different crepant resolutions (a flop) has been established in broad settings (e.g., by Iritani, and Lee-Lin-Wang for ordinary flops).

## 5. Principal Obstacles

The persistence of the CRC as an open problem is due to several formidable technical obstacles that prevent standard topological or algebraic methodologies from yielding a general proof:

1. **The Analytic Continuation Bottleneck:** Gromov-Witten potentials are defined inherently as formal power series in the Novikov ring variables $Q^\beta$ (tracking the degrees of the curves). To relate the potential of $Y$ to that of $\mathcal{X}$, one must prove that these highly transcendental series actually converge in some non-empty domain, define a multi-valued analytic function on the stringy Kähler moduli space, and analytically continue this function from the large-volume limit of $Y$ to the orbifold point of $\mathcal{X}$. Convergence of GW potentials is a notoriously difficult problem and is generally unknown outside of specific homogeneous or toric varieties.
2. **Lack of Functoriality:** There is no direct morphism between the moduli spaces $\overline{M}_{g,n}(\mathcal{X}, \beta)$ and $\overline{M}_{g,n}(Y, \beta')$. Standard intersection theory techniques (like pullback/pushforward formulas) fail because a stable map to $Y$ does not naturally induce a twisted stable map to $\mathcal{X}$.
3. **Higher Genus Complexity:** At higher genera ($g \ge 1$), the invariants involve integrals of Hodge classes over the boundary strata of the moduli space. The Givental quantization action, which is hypothesized to relate the higher-genus potentials, is combinatorially explosive and highly non-linear, making explicit computational checks impossible for arbitrary geometries.

## 6. The Gap

The exact mathematical barrier separating the verified cases from the general statement lies in lifting derived categorical equivalences to non-linear enumerative geometry. 

We possess robust theorems (such as the Bridgeland-King-Reid theorem) which state that the bounded derived categories of coherent sheaves are equivalent: $D^b(Y) \simeq D^b(\mathcal{X})$. However, Gromov-Witten invariants are not directly extracted from the derived category (unlike Donaldson-Thomas invariants). The gap is the absence of a "Gromov-Witten Mirror Theorem" for general Calabi-Yau threefolds that systematically maps Fourier-Mukai transforms in derived geometry to symplectic transformations in Givental's Lagrangian cone. Until we can algebraically bypass the need for analytic continuation—perhaps via a fully developed theory of Categorical Enumerative Invariants—the conjecture will remain stubbornly open for non-toric compact Calabi-Yau manifolds.

## 7. Current Research (as of June 2026)

Active research on the CRC is converging on several sophisticated frameworks:

- **Gauged Linear Sigma Models (GLSM):** Led by researchers like Ciocan-Fontanine, Kim, and Sabbah, GLSMs construct a master moduli space of "phases". Here, both $Y$ and $\mathcal{X}$ appear as different stability conditions (GIT quotients) of a single gauge theory. Researchers are using quasimap invariants to track wall-crossing formulas precisely as one varies the stability parameter from the geometric phase ($Y$) to the orbifold phase ($\mathcal{X}$).
- **Categorical and K-Theoretic GW Theory:** Efforts are shifting from singular cohomology to K-theory (Givental, Tonita) to bridge the gap with derived categories. 
- ***(frontier — verify)* Complete Intersections in Toric Varieties:** Recent preprints attempt to generalize the CCIT toric proofs to non-toric compact targets by embedding them as complete intersections inside toric varieties and utilizing the Quantum Lefschetz hyperplane theorem combined with GLSM wall-crossing.

## 8. Future Work

Leading mathematicians have outlined clear strategic pathways to finally conquer the CRC:
- **Algebraic Reductions:** Developing a purely algebraic definition of the analytic continuation using strictly local data of the moduli spaces, completely circumventing convergence issues.
- **The Higher-Genus Matrix Model:** Utilizing topological recursion to prove that if the genus-zero CRC holds, the structural properties of the recursion automatically enforce the higher-genus CRC.
- **Integration with the Minimal Model Program (MMP):** Expanding the CRC framework to understand how quantum cohomology mutates under general flips and flops in the MMP, mapping the full global structure of the stringy Kähler moduli space.

## 9. Key References

- **[Foundational]** Y. Ruan. *Stringy Geometry and Topology of Orbifolds.* Contemporary Mathematics, 2001.
- **[Foundational]** J. Bryan, T. Graber. *The Crepant Resolution Conjecture.* Algebraic Geometry—Seattle 2005, Proceedings of Symposia in Pure Mathematics, 2009.
- **[SOTA / Recent]** T. Coates, A. Corti, H. Iritani, H.-H. Tseng. *The Crepant Resolution Conjecture for Type A Surface Singularities.* Inventiones mathematicae, 2009.
- **[Survey]** T. Coates, Y. Ruan. *Quantum Cohomology and Crepant Resolutions: A Conjecture.* Annales de l'Institut Fourier, 2013.

## 10. Worked Example / Concrete Special Case

Consider the simplest non-trivial example: the $A_1$ surface singularity and its resolution. Let $\mathbb{Z}_2$ act on $\mathbb{C}^2$ by the involution $(x, y) \mapsto (-x, -y)$. 

**The Orbifold:**
The stack is $\mathcal{X} = [\mathbb{C}^2 / \mathbb{Z}_2]$. The underlying coarse moduli space is the quadric cone $X = \{uv = w^2\} \subset \mathbb{C}^3$. The inertia stack $I\mathcal{X}$ consists of two components: the untwisted sector (the origin acting as identity) and the twisted sector corresponding to the non-trivial element in $\mathbb{Z}_2$, which is localized at the origin.
Thus, the Chen-Ruan cohomology is:
$$ H_{CR}^*(\mathcal{X}, \mathbb{C}) = \mathbb{C}\langle 1 \rangle \oplus \mathbb{C}\langle 1_t \rangle $$
where $1$ is the fundamental class (degree 0) and $1_t$ is the fundamental class of the twisted sector (shifted to degree 1). In ordinary cohomology, the cup product gives $1_t \cup 1_t = 0$. In orbifold quantum cohomology, taking into account 3-point orbifold invariants, the product deforms with a parameter $u$: $1_t * 1_t = u \cdot 1$.

**The Crepant Resolution:**
The crepant resolution is $Y = T^* \mathbb{P}^1 \to X$, which blows up the origin to an exceptional divisor $E \cong \mathbb{P}^1$.
The ordinary cohomology is:
$$ H^*(Y, \mathbb{C}) = \mathbb{C}\langle 1 \rangle \oplus \mathbb{C}\langle E \rangle $$
In the quantum cohomology of $Y$, the product of the exceptional divisor with itself incorporates genus-zero curves covering $E$. The relation is deformed by the quantum parameter $q = e^{2\pi i \int_E \omega}$, giving $E * E = f(q) \cdot 1$.

**The Equivalence:**
The Cohomological CRC states $H_{CR}^*(\mathcal{X}) \cong H^*(Y)$ as vector spaces. 
The Quantum CRC dictates that the two Frobenius algebras are isomorphic after a change of variables. Bryan and Graber demonstrated that by substituting:
$$ q = -e^{iu} $$
(which represents an analytic continuation from the coordinate $q=0$ at the large volume limit of $Y$ to the coordinate $u=0$ at the orbifold point of $\mathcal{X}$), the structural constants of the quantum cohomology ring of $Y$ identically match the structural constants of the Chen-Ruan quantum cohomology ring of $\mathcal{X}$. This exact parameter matching encapsulates the essence of the Crepant Resolution Conjecture.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*