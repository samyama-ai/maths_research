---
id: 03-geometry/demailly-conjecture
title: "Demailly Conjecture"
topic: 03-geometry
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Demailly Conjecture

> **Topic:** Algebraic & Differential Geometry · **ID:** `03-geometry/demailly-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

The Demailly Conjecture proposes a fundamental bridge between the realms of algebraic geometry and complex analytic geometry. It asserts that for a complex projective variety, the purely polynomial, global notion of *algebraic hyperbolicity* is completely equivalent to the analytic, local notion of *Kobayashi hyperbolicity*. 

Because it is a proven theorem (established by Jean-Pierre Demailly) that Kobayashi hyperbolicity always implies algebraic hyperbolicity for smooth projective varieties, the central open conjecture is the converse:

**Conjecture:** *If $X$ is a complex projective variety that is algebraically hyperbolic, then $X$ is Kobayashi hyperbolic.*

A complete proof of this conjecture requires demonstrating that if a variety forces the geometric genus of all its closed algebraic curves to grow at least linearly with respect to their degree, then it mathematically prohibits the existence of any non-constant entire holomorphic curve $f: \mathbb{C} \to X$. Because entire curves are generally transcendental, non-algebraic limits of finite maps, proving the conjecture demands a method to translate asymptotic algebraic constraints onto infinite analytic maps. Conversely, a disproof would require constructing an algebraically hyperbolic projective variety that still admits a dense, transcendental entire holomorphic curve.

## 2. Mathematical Foundations

The conjecture relies on the rigorous definitions of two highly distinct flavors of hyperbolicity.

**Analytic Setup: Kobayashi Hyperbolicity**
Let $X$ be a complex manifold. The *Kobayashi pseudometric* $d_X(p, q)$ between two points $p, q \in X$ is defined as the infimum of the sum of Poincaré distances $\sum_{i=1}^k \rho(a_i, b_i)$ over all possible finite chains of points $p = x_0, x_1, \dots, x_k = q$ and holomorphic maps $f_i: \Delta \to X$ from the unit disk $\Delta \subset \mathbb{C}$ such that $f_i(a_i) = x_{i-1}$ and $f_i(b_i) = x_i$. 

$X$ is defined to be **Kobayashi hyperbolic** if $d_X$ is a true metric (i.e., $d_X(x, y) > 0$ for all $x \neq y$). For compact complex manifolds, this reduces via **Brody's Lemma** (1978) to *Brody hyperbolicity*: $X$ is Kobayashi hyperbolic if and only if there exists no non-constant entire holomorphic map $f: \mathbb{C} \to X$.

**Algebraic Setup: Algebraic Hyperbolicity**
Let $X$ be a complex projective variety equipped with an ample line bundle $H$. $X$ is defined as **algebraically hyperbolic** if there exists a strictly positive real constant $\epsilon > 0$ such that for every integral algebraic curve $C \subset X$, the geometric genus $g(C)$ and the degree $\deg_H(C)$ satisfy the strict linear inequality:
$$ 2g(C) - 2 \ge \epsilon \deg_H(C) $$
Here, the degree is given by the intersection number $\deg_H(C) = \int_C c_1(H)$, and $g(C)$ is the geometric genus (the genus of the smooth normalization $\tilde{C} \to C$). The definition is robust and independent of the choice of the ample line bundle $H$, up to a change in the constant $\epsilon$.

The conjecture essentially posits that the purely algebraic inequality bounding the topological complexity of closed 1-dimensional subvarieties ($2g-2 \ge \epsilon \deg$) is universally sufficient to obstruct the existence of complex analytic maps from $\mathbb{C}$.

## 3. History & State of the Art (SOTA)

The history of the conjecture is heavily tied to the development of higher-dimensional complex analysis in the late 20th century. Jean-Pierre Demailly formalized the notion of algebraic hyperbolicity during his lecture series at the 1995 AMS Summer Institute on Algebraic Geometry in Santa Cruz, subsequently publishing it in his seminal 1997 paper, *"Algebraic criteria for Kobayashi hyperbolic projective varieties and jet differentials."*

In this paper, Demailly utilized the Ahlfors-Schwarz lemma to decisively prove that Kobayashi hyperbolicity implies algebraic hyperbolicity for any compact complex manifold equipped with a Hermitian metric. By introducing the algebraic counterpart, Demailly provided algebraic geometers with a polynomial proxy to test Kobayashi hyperbolicity, immediately conjecturing their equivalence.

The Demailly Conjecture is intimately bound to the **Green-Griffiths-Lang (GGL) conjecture**. A variety $X$ that is algebraically hyperbolic cannot contain any rational curves ($g=0$) or elliptic curves ($g=1$), because for these curves $2g - 2 \le 0$, which would force $\epsilon \deg_H(C) \le 0$, a contradiction since degree is positive. The absence of such curves strongly aligns with varieties of general type. The GGL conjecture predicts that for any variety of general type, the locus of all entire curves $f: \mathbb{C} \to X$ is algebraically degenerate (contained in a proper algebraic subvariety $Y \subsetneq X$). 

As of 2026, the SOTA treats Demailly's Conjecture as wide open in general dimension, though firmly proven in dimension 1, partially in dimension 2, and for specific rigid geometric spaces. Major theoretical advances have been heavily focused on constructing global sections of jet bundles to constrain entire curves, pushing the bounds on the degrees required for generic hypersurfaces to satisfy these hyperbolicity properties.

## 4. Partial Results / Verified Cases

Despite the broad difficulty of the general conjecture, the mathematical community has achieved absolute verification in several vital, highly structured settings:

- **Subvarieties of Abelian Varieties:** The equivalence is fully proven here. A closed subvariety of an abelian variety is Kobayashi hyperbolic if and only if it is algebraically hyperbolic. By Bloch's theorem, the Zariski closure of any entire curve $f: \mathbb{C} \to A$ in an abelian variety is a translate of an abelian subvariety. Since abelian subvarieties contain elliptic curves (which explicitly violate algebraic hyperbolicity), the algebraic absence of elliptic curves absolutely guarantees Kobayashi hyperbolicity.
- **Very General Surfaces of High Degree:** For very general surfaces in $\mathbb{P}^3$, algebraic hyperbolicity implies Kobayashi hyperbolicity. Following the breakthrough work of McQuillan (1998) on Diophantine approximations and foliations, and Demailly-El Goul (2000), a very general surface $X \subset \mathbb{P}^3$ of degree $d \ge 21$ is rigorously proven to be Kobayashi hyperbolic. These surfaces trivially satisfy algebraic hyperbolicity.
- **Projective Curves (Dimension 1):** The theorem holds trivially for all projective curves (Riemann surfaces). A curve is algebraically hyperbolic if and only if $g \ge 2$, which coincides precisely with the condition for Kobayashi hyperbolicity under the Uniformization Theorem.
- **Fibrations and Campana's Orbifolds:** The equivalence has been established for specific dimensional fibrations within Campana's "geometric orbifolds" framework, where logarithmic bounds on algebraic curve complements map cleanly to Brody hyperbolicity on the open variety.

## 5. Principal Obstacles

The central bottleneck preventing a general proof lies in the profound structural mismatch between **algebraic cycles** and **transcendental analytic currents**.

Algebraic hyperbolicity only restricts the topological behavior of *closed algebraic curves*, which are defined by polynomial equations and represent compact homology classes. In contrast, an entire curve $f: \mathbb{C} \to X$ is a transcendental, non-compact object. The image $f(\mathbb{C})$ is almost never closed in the Zariski topology, and its Euclidean closure can be a highly irregular fractal set with no meaningful algebraic structure.

To bridge this, modern theory relies on Nevanlinna theory. Given an entire curve $f: \mathbb{C} \to X$, one considers the restriction of $f$ to expanding disks $\Delta_r \subset \mathbb{C}$ of radius $r$. By normalizing the currents of integration over $f(\Delta_r)$ by the Nevanlinna order function $T_f(r)$, one extracts a weak limit as $r \to \infty$. This limit is a strictly positive closed $(1,1)$-current $T$, known as an **Ahlfors current**.

If the Demailly conjecture is true, the existence of this Ahlfors current $T$ should inherently violate the algebraic bound $2g - 2 \ge \epsilon \deg_H$. The principal obstacle is that $T$ is merely a measure-like object. Mathematicians currently have no generalized "Riemann-Hurwitz formula" or intersection theory for arbitrary positive closed currents that can algebraically quantify the "genus" of $T$. Because $T$ cannot be rigorously approximated by a sequence of actual algebraic curves $C_n$ while preserving the crucial genus-to-degree ratio, standard perturbation and limiting techniques fail instantly.

## 6. The Gap

The exact boundary between what is verified and the general proof is the transition from **closed positive analytic currents** to **effective algebraic cycles**. 

Assume $X$ is algebraically hyperbolic. Suppose for contradiction it is not Kobayashi hyperbolic. By Brody's Lemma, there exists a non-constant entire curve $f: \mathbb{C} \to X$, yielding a non-zero, positive closed Ahlfors current $T$. 
The mathematical gap requires proving a theorem of the form: *If $X$ satisfies $2g(C) - 2 \ge \epsilon \int_C c_1(H)$ for all algebraic cycles $C$, then any Ahlfors current $T$ generated by an entire curve must evaluate negatively against a specific intersection product, contradicting $T \ge 0$.* Until functional analysis and algebraic intersection theory can cohesively define topological genus for diffuse analytic currents, the gap remains uncrossed.

## 7. Current Research (as of June 2026)

Active research primarily operates through the lens of differential equations, specifically leveraging **Jet Differentials**.
- **Green-Griffiths Jet Bundles:** Schools of thought led by Demailly, Siu, Păun, and Rousseau attempt to bypass the Ahlfors current gap entirely by constructing global sections of jet bundles $E_{k, m}^{GG} \Omega_X$ (polynomials in the derivatives of entire curves). If $X$ is algebraically hyperbolic, researchers aim to prove it possesses enough global jet differentials to force any entire curve to satisfy a rigid differential equation, thereby forcing $f(\mathbb{C})$ into a proper algebraic subvariety.
- **Effective Algebraic Degeneracy:** Following landmark papers like Diverio-Merker-Rousseau (2010), research focuses on pushing the effective degree bounds for which generic hypersurfaces are proven hyperbolic. Current computational geometry algorithms are deployed to calculate Euler characteristics of these highly complex vector bundles.
- *(frontier — verify)* **Non-Archimedean and Berkovich Approaches:** Recent preprints have begun deploying non-Archimedean geometry to study the boundary of the moduli spaces of entire curves. By translating the Nevanlinna limits into Berkovich spaces, researchers hope to attach a rigorous, non-trivial algebraic genus invariant to the asymptotic ends of the transcendental curves.

## 8. Future Work

Prominent algebraic geometers have outlined several critical pathways to resolve the conjecture:
1. **Resolution of the Green-Griffiths-Lang Conjecture:** This is the most viable path. If GGL is proven (that entire curves on general type varieties must be algebraically degenerate), one can prove Demailly's conjecture by induction on the dimension. Since any proper subvariety of an algebraically hyperbolic variety is itself algebraically hyperbolic, the existence of an entire curve would eventually be squeezed into a 1-dimensional algebraically hyperbolic curve—yielding an immediate contradiction via the Uniformization Theorem.
2. **Current Regularization Theory:** Developing a robust "smoothing" technique in pluripotential theory that allows an Ahlfors current to be approximated by genuine algebraic curves $C_n$ such that the geometric genus of $C_n$ can be bounded uniformly.
3. **The Optimal Kobayashi Degree Bound:** Proving that a generic hypersurface $X \subset \mathbb{P}^{n+1}$ of optimal degree $d = 2n + 1$ is Kobayashi hyperbolic. Such hypersurfaces are already known to be algebraically hyperbolic (by Clemens, Ein, Voisin). Closing this gap would provide the largest continuous family of varieties verifying the Demailly conjecture, severely constraining potential counterexamples.

## 9. Key References

- **[Foundational]** Demailly, J.-P. *Algebraic criteria for Kobayashi hyperbolic projective varieties and jet differentials.* Proceedings of Symposia in Pure Mathematics, Vol. 62, Part 2, AMS, 1997. [DOI](https://doi.org/10.1090/pspum/062.2/1492539)
- **[SOTA / Recent]** Diverio, S., Merker, J., & Rousseau, E. *Effective algebraic degeneracy.* Inventiones Mathematicae, 2010. [DOI](https://doi.org/10.1007/s00222-010-0232-4)
- **[Survey]** Demailly, J.-P. *Recent progress towards the Kobayashi and Green-Griffiths-Lang conjectures.* Fourteenth Marcel Grossmann Meeting, 2017.
- **[Foundational]** Brody, R. *Compact manifolds and hyperbolicity.* Transactions of the American Mathematical Society, 1978. [DOI](https://doi.org/10.2307/1998216)

## 10. Worked Example / Concrete Special Case

To ground the conjecture, we can analyze the simplest concrete case: 1-dimensional varieties. Let $X$ be a smooth, compact complex projective curve (a Riemann surface) over $\mathbb{C}$. We will test if the Demailly conjecture holds.

**Step 1: Assessing Algebraic Hyperbolicity**
For a 1-dimensional curve $X$, the only integral algebraic curve $C \subset X$ is the variety $X$ itself. Let the ample line bundle $H$ be the canonical bundle $K_X$ (assuming $X$ is not rational). 
The algebraic hyperbolicity condition requires finding an $\epsilon > 0$ such that:
$$ 2g(X) - 2 \ge \epsilon \deg_H(X) $$
For this inequality to hold with a strictly positive $\epsilon$ and positive degree, the left side must be strictly positive. 
If $g(X) = 0$ ($X \cong \mathbb{P}^1$) or $g(X) = 1$ (an elliptic curve), we have $2g(X) - 2 \le 0$, making algebraic hyperbolicity impossible. Therefore, algebraic hyperbolicity structurally forces $g(X) \ge 2$.

**Step 2: Assessing Kobayashi Hyperbolicity**
Kobayashi hyperbolicity requires $X$ to admit no non-constant entire holomorphic maps $f: \mathbb{C} \to X$. We utilize the Uniformization Theorem, which categorizes the universal cover $\tilde{X}$ of the curve $X$:
- If $g = 0$, $\tilde{X} = \mathbb{P}^1$
- If $g = 1$, $\tilde{X} = \mathbb{C}$
- If $g \ge 2$, $\tilde{X} = \Delta$ (the Poincaré unit disk)

Assume $X$ is algebraically hyperbolic (so $g(X) \ge 2$). Any entire map $f: \mathbb{C} \to X$ must lift to a holomorphic map $\tilde{f}: \mathbb{C} \to \Delta$ because the domain $\mathbb{C}$ is simply connected. 
However, $\tilde{f}$ is now a bounded entire function on the complex plane. By **Liouville's Theorem**, any bounded entire holomorphic function must be a constant. Consequently, the lifted map $\tilde{f}$ is constant, meaning the original map $f$ is also constant. 
Because all maps from $\mathbb{C}$ are constant, $X$ is inherently Brody hyperbolic, and thus Kobayashi hyperbolic.

**Conclusion:**
For 1-dimensional varieties, $X$ is algebraically hyperbolic $\iff g(X) \ge 2 \iff X$ is Kobayashi hyperbolic. The Demailly Conjecture holds absolutely in dimension 1, elegantly demonstrating how algebraic bounds (genus) effortlessly obstruct analytic freedom (Liouville's theorem) in low dimensions. The open frontier exists entirely because Liouville-style rigidity breaks down for transcendental curves diffusing through dimensions 2 and higher.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*