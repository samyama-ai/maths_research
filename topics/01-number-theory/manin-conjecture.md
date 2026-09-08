---
id: 01-number-theory/manin-conjecture
title: "Manin Conjecture"
topic: 01-number-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Manin Conjecture

> **Topic:** 01-number-theory · **ID:** `01-number-theory/manin-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

The Manin Conjecture (formulated by J. Franke, Y. Manin, and Y. Tschinkel in 1989) describes the asymptotic distribution of rational points of bounded height on Fano varieties. 

Let $V$ be a smooth projective Fano variety defined over a number field $K$. Let $H: V(K) \to \mathbb{R}_{\ge 0}$ be an exponential Weil height function associated to a metrization of the anticanonical divisor $-K_V$. Because rational points can accumulate on subvarieties of lower degree, we must restrict our counting to a well-behaved subset. The modern formulation of the conjecture states that there exists a *thin set* $Z \subset V(K)$ (in the sense of Serre) such that the counting function of rational points outside $Z$, defined as:

$$ N_{V \setminus Z, H}(B) = \left| \{ x \in V(K) \setminus Z : H(x) \le B \} \right| $$

satisfies the asymptotic formula as $B \to \infty$:

$$ N_{V \setminus Z, H}(B) \sim c(V, K) B (\log B)^{\rho(V) - 1} $$

where:
1. $\rho(V) = \operatorname{rank} \operatorname{Pic}(V)$ is the Picard rank of $V$.
2. $c(V, K) > 0$ is a specific positive constant introduced by E. Peyre (1995), dependent on the geometry of $V$, the choice of height metrics, and the Tamagawa measure on the adelic space $V(\mathbb{A}_K)$. 

A complete proof requires establishing this asymptotic formula for all smooth Fano varieties over any number field, along with a formalized geometric characterization of the exceptional thin set $Z$.

## 2. Mathematical Foundations

The conjecture bridges algebraic geometry and analytic number theory.

**Fano Varieties:** A smooth projective variety $V$ over a field $K$ is *Fano* if its anticanonical divisor $-K_V$ (or equivalently, the determinant of the tangent bundle $\det T_V$) is ample.

**Height Functions:** Let $L$ be a very ample line bundle on $V$. It embeds $V \hookrightarrow \mathbb{P}^N$. For a rational point $x = [x_0 : \dots : x_N] \in \mathbb{P}^N(K)$, the standard Weil height is $H_L(x) = \prod_{v \in M_K} \max_{i} \{ |x_i|_v \}$, where $M_K$ are the places of $K$. For the Manin Conjecture, the primary line bundle of interest is $L = -K_V$.

**Peyre's Constant:** The leading constant $c(V, K)$ takes the form:
$$ c(V, K) = \alpha(V) \cdot \beta(V) \cdot \omega_H(V(\mathbb{A}_K)) $$
- $\alpha(V)$ is a rational volume related to the effective cone of divisors $\Lambda_{\mathrm{eff}}(V) \subset \operatorname{Pic}(V) \otimes \mathbb{R}$.
- $\beta(V) = |H^1(K, \operatorname{Pic}(\overline{V}))|$ is a cohomological factor related to the Brauer group.
- $\omega_H$ is the Tamagawa measure on the adelic points $V(\mathbb{A}_K)$, intrinsically tied to the local heights, ensuring the constant behaves correctly under local-global principles.

**Thin Sets:** A subset $Z \subset V(K)$ is *thin* if it is a finite union of subsets that are either non-dense Zariski closed sets, or images of $Y(K)$ under a generically finite morphism $f: Y \to V$ of degree $\ge 2$. Originally, Manin conjectured the removal of a proper Zariski closed subset, but Batyrev and Tschinkel constructed examples where points accumulate on infinite families of curves, necessitating the removal of a thin set.

## 3. History & State of the Art (SOTA)

- **1989 (Origins):** Proposed by Franke, Manin, and Tschinkel. They proved the conjecture for flag varieties $P \backslash G$ using the theory of Langlands Eisenstein series.
- **1995 (Peyre's Constant):** Emmanuel Peyre identified the precise cohomological and measure-theoretic structure of the constant $c(V, K)$, elevating the conjecture to a rigid testable statement.
- **1996-1998 (Toric Varieties & Counterexamples):** Batyrev and Tschinkel proved the conjecture for all smooth projective toric varieties over arbitrary number fields using Fourier analysis on adele groups. Concurrently, they discovered Fano varieties (bundles over $\mathbb{P}^1$) where the count on any Zariski open set grows faster than predicted, forcing the modification to exclude *thin sets*.
- **2010s (Minimal Model Program):** Lehmann and Tanimoto utilized the Minimal Model Program (MMP) to study the geometric origin of accumulating subvarieties, defining the "a-constant" $a(L)$ for arbitrary subvarieties to predict exactly which sets must be placed in $Z$.
- **SOTA:** The conjecture is proven for highly symmetric spaces (equivariant compactifications of linear algebraic groups, toric varieties, flag varieties) and Fano varieties of large dimension relative to their degree (via the Hardy-Littlewood circle method). Low-dimensional, non-symmetric Fano varieties (like general cubic surfaces) remain widely open.

## 4. Partial Results / Verified Cases

The conjecture (with Peyre's constant) has been strictly proven for:
1. **Projective Spaces:** $\mathbb{P}^n$ (Schanuel’s Theorem, 1979).
2. **Homogeneous Spaces:** Flag varieties $G/P$, generalized by Shalika, Takano, and Tschinkel (2007).
3. **Toric Varieties:** All smooth projective toric varieties (Batyrev and Tschinkel, 1998).
4. **Group Compactifications:** Equivariant compactifications of connected linear algebraic groups (Chambert-Loir and Tschinkel, 2012).
5. **Del Pezzo Surfaces (Dimension 2):** 
   - Degree $d \ge 6$: Proven (toric or closely related).
   - Degree $d = 5$: Proven (de la Bretèche, 2001).
   - Degree $d = 4$: Proven (intersection of two quadrics in $\mathbb{P}^4$, Salberger, de la Bretèche, Browning, Derenthal).
6. **Specific Cubic Surfaces (Degree 3):** E.g., the singular cubic surface $x_1 x_2 x_3 = x_4^3$ (de la Bretèche, 1998), and select smooth ones containing lines (Heath-Brown).
7. **Complete Intersections:** Fano complete intersections in $\mathbb{P}^n$ provided the dimension $n$ is sufficiently large compared to the degree (using the Circle Method, e.g., Birch's Theorem, and recent improvements by Browning and Vishe).

## 5. Principal Obstacles

The central difficulty is the lack of a universal technique to count points on varieties without large symmetry groups or high dimensions.

1. **Failure of Harmonic Analysis:** For toric or flag varieties, the dense orbit of a group action allows counting to be translated into harmonic analysis on adelic groups (using Poisson summation or Eisenstein series). General Fano varieties (like general cubic surfaces) have trivial automorphism groups, rendering harmonic analysis inapplicable.
2. **Failure of the Circle Method:** The Hardy-Littlewood circle method provides exact asymptotics for counting solutions to Diophantine equations, but only when the number of variables $n$ is large compared to the degree $d$. For a cubic surface ($d=3, n=4$), the circle method fundamentally fails because the "minor arcs" bound exceeds the expected main term.
3. **Complex Accumulation (Thin Sets):** Identifying and removing the thin set $Z$ analytically is highly non-trivial. When counting, one cannot easily filter out points that algebraically lie on a dense network of rational curves.

## 6. The Gap

The boundary of current mathematics lies at low-dimensional spaces lacking symmetry—most famously, **del Pezzo surfaces of degrees 1, 2, and 3** (smooth cubic surfaces in $\mathbb{P}^3$). The exact mathematical barrier to cross is finding an analytic or geometric counting mechanism that operates efficiently beyond the density thresholds of the Circle Method and does not rely on a dense group orbit. Proving the conjecture for a general smooth cubic surface over $\mathbb{Q}$ is the most prominent immediate gap in the field.

## 7. Current Research (as of June 2026)

- **Geometric Manin's Conjecture:** Groups led by Brian Lehmann, Sho Tanimoto, and Sengupta are actively mapping the arithmetic of the Manin conjecture entirely into the geometry of the Minimal Model Program. They aim to characterize the exceptional thin set $Z$ purely unconditionally through the "a-invariants" of subvarieties.
- **The Delta Method:** The $p$-adic and structural Delta method (developed by Heath-Brown) is being heavily pushed by T. Browning, P. Vishe, and S. Marmon to handle hypersurfaces of lower dimensions than classically possible.
- **Function Field Analogues & Topology:** *(frontier — verify)* Recent breakthroughs count points over $\mathbb{F}_q(t)$ (the function field analogue) by transforming the count into computing the Betti numbers of moduli spaces of rational curves, applying tools from étale cohomology and the Weil conjectures (Browning, Sawin, Ellenberg, Venkatesh). These homological stability theorems are currently driving the most rapid advancements.

## 8. Future Work

Leading mathematicians suggest the following pathways:
1. **General Cubic Surfaces:** Solving the conjecture for a generic smooth cubic surface is the holy grail of this domain.
2. **Uniform Upper Bounds:** While asymptotics are hard, proving uniform upper bounds of the form $N_U(B) = O_\epsilon(B^{1+\epsilon})$ for *all* Fano varieties is seen as a highly tractable intermediate step (often approached via Salberger's global determinant method).
3. **Movable Curves:** Formalizing the connection between the base loci of movable curves and the exceptional thin sets, proving that MMP invariants dictate arithmetic accumulation in all dimensions.

## 9. Key References

- **[Foundational]** Franke, J., Manin, Y. I., and Tschinkel, Y. *Rational points of bounded height on Fano varieties*. Inventiones Mathematicae, 1989. [DOI](https://doi.org/10.1007/bf01233436)
- **[Foundational]** Peyre, E. *Hauteurs et mesures de Tamagawa sur les variétés de Fano*. Duke Mathematical Journal, 1995. [DOI](https://doi.org/10.1215/s0012-7094-95-07904-6)
- **[SOTA / Recent]** Lehmann, B., and Tanimoto, S. *On the geometry of thin exceptional sets in Manin's conjecture*. Duke Mathematical Journal, 2017. [DOI](https://doi.org/10.1215/00127094-2017-0011)
- **[SOTA / Recent]** Batyrev, V. V., and Tschinkel, Y. *Manin's conjecture for toric varieties*. Journal of Algebraic Geometry, 1998.
- **[Survey]** Browning, T. D. *Quantitative Arithmetic of Projective Varieties*. Progress in Mathematics, Birkhäuser, 2009. [DOI](https://doi.org/10.1007/978-3-0346-0129-0)

## 10. Worked Example / Concrete Special Case

The simplest Fano variety is the projective line $V = \mathbb{P}^1$ over $K = \mathbb{Q}$. Let's verify the conjecture here (this is Schanuel's theorem for $n=1$).

The standard Weil height of a point $x = [u:v] \in \mathbb{P}^1(\mathbb{Q})$ where $u, v \in \mathbb{Z}$ and $\gcd(u,v)=1$ is given by $H_{std}(x) = \max(|u|, |v|)$. 

The canonical divisor is $K_{\mathbb{P}^1} = \mathcal{O}(-2)$, so the anticanonical bundle is $\mathcal{O}(2)$. Therefore, the anticanonical height is $H_{-K}(x) = (H_{std}(x))^2 = \max(|u|, |v|)^2$.

We wish to count the number of rational points $N(B)$ with $H_{-K}(x) \le B$, which is equivalent to counting pairs $(u, v)$ such that:
1. $\gcd(u,v) = 1$
2. $\max(|u|, |v|) \le B^{1/2}$
3. $(u, v)$ and $(-u, -v)$ represent the same point.

The number of integer points in the box $[-B^{1/2}, B^{1/2}] \times [-B^{1/2}, B^{1/2}]$ is approximately $(2B^{1/2})^2 = 4B$.
The probability that two random integers are coprime is well-known to be $\frac{1}{\zeta(2)} = \frac{6}{\pi^2}$.
Since $[u:v]$ and $[-u:-v]$ are the same point, we divide the count by 2.

Thus, as $B \to \infty$, the number of rational points is:
$$ N_{\mathbb{P}^1, -K}(B) \sim \frac{1}{2} \cdot \frac{6}{\pi^2} \cdot 4B = \frac{12}{\pi^2} B $$

Now, let's match this against Manin's prediction:
$$ N_{V, -K}(B) \sim c(\mathbb{P}^1, \mathbb{Q}) B (\log B)^{\rho(\mathbb{P}^1) - 1} $$
Since $\operatorname{Pic}(\mathbb{P}^1) \cong \mathbb{Z}$, the Picard rank is $\rho = 1$. The $(\log B)^{1-1} = 1$ term disappears, leaving a linear growth $c B$. Peyre's constant $c(\mathbb{P}^1, \mathbb{Q})$ calculates precisely to $\frac{12}{\pi^2}$, confirming the conjecture for $\mathbb{P}^1$.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*