---
id: 05-analysis/garnett-problem
title: "Garnett's Problem"
topic: 05-analysis
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Garnett's Problem on Blaschke Products

> **Topic:** Real & Complex Analysis · **ID:** `05-analysis/garnett-problem` · **Status:** open

## 1. Problem Statement / Conjecture

Garnett's Problem (also commonly referred to as the Garnett-Jones Approximation Problem) is a fundamental open question in the theory of bounded analytic functions regarding the rigid geometric structure of inner functions. It asks whether the set of interpolating Blaschke products is dense in the set of all Blaschke products with respect to the uniform norm (the $H^\infty$ norm).

Formally, let $\mathbb{D}$ denote the open unit disk in the complex plane, and let $H^\infty(\mathbb{D})$ be the Banach algebra of bounded analytic functions equipped with the supremum norm $\|f\|_\infty = \sup_{z \in \mathbb{D}} |f(z)|$. Let $\mathcal{B} \subset H^\infty(\mathbb{D})$ denote the set of all Blaschke products, and let $\mathcal{I} \subset \mathcal{B}$ denote the subset of interpolating Blaschke products. 

**Conjecture:** For every Blaschke product $B \in \mathcal{B}$ and every $\epsilon > 0$, there exists an interpolating Blaschke product $b \in \mathcal{I}$ such that 
$$ \| B - b \|_\infty < \epsilon. $$
Equivalently, the conjecture posits that the norm closure of the interpolating Blaschke products in $H^\infty(\mathbb{D})$ contains all Blaschke products, meaning $\overline{\mathcal{I}} \supset \mathcal{B}$. Because it is known via Frostman's Theorem that the set of all Blaschke products is uniformly dense in the set of all inner functions, an affirmative answer to Garnett's Problem would immediately imply that every inner function can be uniformly approximated by interpolating Blaschke products.

## 2. Mathematical Foundations

The problem is rooted in the structure of the Hardy space $H^\infty(\mathbb{D})$ and the boundary behavior of analytic functions. A function $f \in H^\infty(\mathbb{D})$ is called an *inner function* if its radial limits $f(e^{i\theta}) = \lim_{r \to 1^-} f(re^{i\theta})$ exist and satisfy $|f(e^{i\theta})| = 1$ for almost every $\theta \in [0, 2\pi)$ with respect to Lebesgue measure. 

A sequence of points $\{z_n\}_{n=1}^\infty \subset \mathbb{D}$ is called a *Blaschke sequence* if it satisfies the Blaschke condition:
$$ \sum_{n=1}^\infty (1 - |z_n|) < \infty. $$
Given a Blaschke sequence, the corresponding *Blaschke product* is defined as:
$$ B(z) = z^m \prod_{z_n \neq 0} \frac{|z_n|}{z_n} \frac{z_n - z}{1 - \overline{z_n}z}, $$
where $m \geq 0$ is the order of the zero at the origin. The Blaschke condition guarantees that the infinite product converges absolutely and uniformly on compact subsets of $\mathbb{D}$, defining an inner function.

The geometry of $\mathbb{D}$ is governed by the pseudohyperbolic metric, defined for $z, w \in \mathbb{D}$ as:
$$ \rho(z, w) = \left| \frac{z - w}{1 - \bar{w}z} \right|. $$
A sequence $\{z_n\}$ is called an *interpolating sequence* for $H^\infty(\mathbb{D})$ if the trace space $H^\infty|_{\{z_n\}} = \ell^\infty$. By Carleson's Interpolation Theorem (1958), a sequence is interpolating if and only if it satisfies the Carleson separation condition:
$$ \inf_{k} \prod_{j \neq k} \rho(z_j, z_k) \geq \delta > 0. $$
A Blaschke product formed from an interpolating sequence is called an *interpolating Blaschke product*. The condition implies that the zeros are strictly separated in the pseudohyperbolic metric (i.e., $\inf_{j \neq k} \rho(z_j, z_k) \geq \delta$) and that the measure $\sum (1 - |z_n|) \delta_{z_n}$ is a Carleson measure on $\mathbb{D}$.

## 3. History & State of the Art (SOTA)

The study of the relationship between $\mathcal{B}$ and $\mathcal{I}$ has been a central theme in harmonic analysis since Carleson’s resolution of the Corona Problem in 1962. The uniform approximation question was prominently highlighted by John B. Garnett in the 1970s and subsequently featured in his classic 1981 text, *Bounded Analytic Functions*.

Historically, mathematical intuition shifted dramatically with Donald Marshall’s 1976 theorem, which proved that the closed convex hull of the interpolating Blaschke products is exactly the closed unit ball of $H^\infty(\mathbb{D})$. This revealed that $\mathcal{I}$ is linearly dense. In 1996, Garnett and Artur Nicolau pushed this further, proving that the closed linear span of the interpolating Blaschke products is the entire space $H^\infty(\mathbb{D})$. 

Despite these massive linear approximation results, multiplicative or direct uniform approximation by a *single* interpolating Blaschke product remains unsolved. The state of the art largely relies on the Garnett-Jones Theorem on angular derivatives. Garnett and Peter Jones demonstrated that boundary regularities are rigidly preserved under uniform approximation: if an inner function $B$ has an infinite angular derivative at a point $\xi \in \partial\mathbb{D}$, and if $b$ is an interpolating Blaschke product such that $\|B - b\|_\infty < 1$, then $b$ must also have an infinite angular derivative at $\xi$. This rigidity suggests that finding an approximant requires an incredibly precise matching of boundary behaviors, leading many modern analysts to suspect the conjecture might actually be false, though no explicit counterexample has been successfully constructed.

## 4. Partial Results / Verified Cases

While the general conjecture remains open, several critical subclasses of Blaschke products have been verified to admit uniform approximation by interpolating Blaschke products:

1. **Finite Blaschke Products:** Every finite Blaschke product with distinct zeros is trivially interpolating. If a finite Blaschke product has multiple roots at the same point, it can be uniformly approximated by perturbing the roots slightly apart in the pseudohyperbolic metric, instantly making it interpolating.
2. **Thin Sequences:** If the zero sequence of $B(z)$ lies on a finite union of Stolz angles (non-tangential approach regions) and satisfies a weak separation property, constructive surgery on the zeros allows for uniform approximation.
3. **Approximation in Weaker Topologies:** It is a verified, elementary fact that $\mathcal{I}$ is dense in $\mathcal{B}$ under the topology of uniform convergence on compact subsets of $\mathbb{D}$. One simply truncates the infinite product to a finite one, which is trivially interpolating. The bottleneck is strictly at the boundary $\partial\mathbb{D}$.
4. **Frostman Shifts:** Frostman's Theorem guarantees that for any inner function $\theta(z)$, the fractional linear shift $\theta_\alpha(z) = \frac{\theta(z) - \alpha}{1 - \bar{\alpha}\theta(z)}$ is a Blaschke product for all $\alpha \in \mathbb{D}$ outside a set of logarithmic capacity zero. Kenneth Hoffman proved that if $\theta$ is an interpolating Blaschke product, its Frostman shifts $\theta_\alpha$ remain interpolating for all $\alpha \in \mathbb{D}$. Consequently, Frostman shifts cannot be used to generate non-interpolating Blaschke products from interpolating ones, trapping the known constructive methods inside $\mathcal{I}$.

## 5. Principal Obstacles

The fundamental bottleneck lies in the topological structure of the maximal ideal space of the algebra $H^\infty(\mathbb{D})$, denoted $\mathcal{M}(H^\infty)$. By the Corona Theorem, $\mathbb{D}$ is dense in $\mathcal{M}(H^\infty)$, and the boundary $\mathcal{M}(H^\infty) \setminus \mathbb{D}$ is known as the Corona.

Hoffman completely classified the Gleason parts of $\mathcal{M}(H^\infty)$. A point $m$ in the Corona belongs to a non-trivial Gleason part (a component analytically homeomorphic to $\mathbb{D}$) if and only if $m$ lies in the closure of an interpolating sequence. Interpolating Blaschke products have the rigid geometric property that their zero sets, when extended to the maximal ideal space, intersect the Corona *only* at non-trivial Gleason parts. 

However, an arbitrary Blaschke product $B \in \mathcal{B}$ can vanish on *trivial* Gleason parts—points in the Corona that are entirely isolated in the Gleason metric. If Garnett's Problem has an affirmative answer, it implies that a continuous function (the Blaschke product) that vanishes on a trivial part can be uniformly approximated by functions that never vanish on trivial parts. This creates a severe topological mismatch. 

Analytically, the obstacle manifests via the Schwarz-Pick Lemma. If $\|B - b\|_\infty < \epsilon$, then $|b(z)|$ must be small wherever $B(z)$ is zero. For interpolating Blaschke products, being small implies being pseudohyperbolically close to a zero. If $B(z)$ has zeros that cluster violently (failing the Carleson separation condition $\delta > 0$), $b(z)$ is forced to place its own zeros nearby to maintain the uniform bound. But $b(z)$ is strictly forbidden from clustering by the definition of an interpolating sequence. Balancing this extreme tension using multi-zero cancellations without destroying the uniform norm elsewhere on the boundary has proven impossible with current techniques.

## 6. The Gap

The precise mathematical gap is the transition from linear approximation to non-linear/multiplicative approximation. Marshall's theorem shows that for any $B \in \mathcal{B}$, one can find finite sequences of interpolating Blaschke products $b_i$ and coefficients $c_i$ such that:
$$ \left\| B - \sum_{i=1}^N c_i b_i \right\|_\infty < \epsilon. $$
In this linear sum, the zeros of the individual $b_i$ can cluster independently, and their algebraic sum smooths out the boundary singularities. However, Garnett's Problem requires a single $b \in \mathcal{I}$. The gap requires either developing a non-linear averaging operator that maps convex combinations of interpolating inner functions back into the interpolating class without blowing up the uniform norm, or constructing an explicit topological obstruction (a continuous linear functional on $H^\infty$) that separates a specific pathological Blaschke product from the closed set $\overline{\mathcal{I}}$.

## 7. Current Research (as of June 2026)

Current research approaches Garnett's Problem through two primary, highly technical avenues:

1. **Aleksandrov-Clark (AC) Measures:** Every inner function is uniquely characterized by its family of AC measures on $\partial\mathbb{D}$. The zeros of interpolating Blaschke products correspond to highly structured, discrete AC measures with specific mass distributions. Researchers are attempting to determine if the weak-* closure of the AC measures associated with interpolating Blaschke products can capture the AC measures of all Blaschke products.
2. **Quasiconformal Surgery:** Another active school of thought involves applying the $\bar{\partial}$-equation and quasiconformal deformations to perform "micro-surgery" on the zero set of a general Blaschke product. By locally dilating the pseudohyperbolic metric around highly clustered zeros, one can create a separated sequence. However, correcting the resulting non-analytic function back to $H^\infty(\mathbb{D})$ via the Beltrami equation alters the boundary values, currently breaking the $\epsilon$-uniform approximation bound. 
3. *Frontier — verify:* Recent preprints have circulated claiming the construction of a "rigid" Blaschke product—one whose zeros approach $\partial\mathbb{D}$ so rapidly and tangentially that its Clark measures are strictly isolated from the Clark measures of any Carleson sequence, potentially providing a negative answer to the conjecture. These claims are currently undergoing rigorous peer review.

## 8. Future Work

Leading mathematicians working in function theory and operator algebras suggest the following pathways to resolve the conjecture:
- **Refining Frostman's Theorem:** Establishing a sharp, quantitative version of Frostman's theorem that dictates the exact Carleson separation constant $\delta$ of the shift $\theta_\alpha$ as a function of the capacity of $\alpha$.
- **Douglas Algebras:** Investigating the problem through the lens of Douglas algebras. Since $H^\infty[\bar{b}]$ (where $b \in \mathcal{I}$) generates all Douglas algebras, characterizing the exact uniform closure $\overline{\mathcal{I}}$ might be achieved by studying the essential spectra of Toeplitz operators with symbols in $H^\infty + C$.
- **Trivial Gleason Parts:** Constructing an explicit constructive approximation for the specific Blaschke products known to vanish on the trivial Gleason parts of $\mathcal{M}(H^\infty)$. If this barrier can be crossed, the general topological obstruction falls.

## 9. Key References

- **[Foundational]** Garnett, J. B. *Bounded Analytic Functions.* Academic Press, 1981. 
- **[Foundational]** Marshall, D. E. *Blaschke products generate $H^\infty$.* Bulletin of the American Mathematical Society, 82(3), 494-496, 1976.
- **[Foundational]** Hoffman, K. *Banach Spaces of Analytic Functions.* Prentice-Hall, 1962. (Reprinted by Dover Publications, 2007).
- **[SOTA / Recent]** Garnett, J. B., and Nicolau, A. *Interpolating Blaschke products generate $H^\infty$.* Pacific Journal of Mathematics, 173(2), 501-510, 1996.
- **[Survey]** Garcia, S. R., Mashreghi, J., and Ross, W. T. *Finite Blaschke Products and Their Connections.* Springer, 2018. [DOI](https://doi.org/10.1007/978-3-319-78247-8)

## 10. Worked Example / Concrete Special Case

To ground the abstract tension of this problem, consider the specific Blaschke sequence $z_n = 1 - \frac{1}{n^2}$ on the real axis in $\mathbb{D}$. 

First, we verify the Blaschke condition:
$$ \sum_{n=1}^\infty (1 - |z_n|) = \sum_{n=1}^\infty \frac{1}{n^2} = \frac{\pi^2}{6} < \infty. $$
Thus, this sequence defines a valid Blaschke product $B(z)$. 

Next, we check the Carleson separation condition. We compute the pseudohyperbolic distance between adjacent zeros:
$$ \rho(z_n, z_{n+1}) = \left| \frac{z_{n+1} - z_n}{1 - z_n z_{n+1}} \right|. $$
The numerator is:
$$ z_{n+1} - z_n = \frac{1}{n^2} - \frac{1}{(n+1)^2} = \frac{2n+1}{n^2(n+1)^2} \approx \frac{2}{n^3}. $$
The denominator is:
$$ 1 - z_n z_{n+1} = 1 - \left(1 - \frac{1}{n^2}\right)\left(1 - \frac{1}{(n+1)^2}\right) = \frac{1}{n^2} + \frac{1}{(n+1)^2} - \frac{1}{n^2(n+1)^2} \approx \frac{2}{n^2}. $$
Therefore, as $n \to \infty$, we have:
$$ \rho(z_n, z_{n+1}) \approx \frac{2/n^3}{2/n^2} = \frac{1}{n} \longrightarrow 0. $$
Because $\inf_{n \neq k} \rho(z_n, z_k) = 0$, the sequence violates the Carleson condition, and $B(z)$ is **not** an interpolating Blaschke product. 

To uniformly approximate $B(z)$ by an interpolating Blaschke product $b(z)$ with zeros $\{w_k\}$, we would need $\| B - b \|_\infty < \epsilon$. This implies that at the zeros of $B$, the approximant $b$ must be small: $|b(z_n)| < \epsilon$. 

By the theory of interpolating sequences, if an interpolating Blaschke product with separation constant $\delta$ is uniformly small at a point, it must have a zero nearby in the pseudohyperbolic metric. Specifically, there exists $\eta(\delta, \epsilon)$ such that $\rho(z_n, w_n) < \eta$. By the triangle inequality for the pseudohyperbolic metric:
$$ \rho(w_n, w_{n+1}) \leq \frac{\rho(w_n, z_n) + \rho(z_n, z_{n+1}) + \rho(z_{n+1}, w_{n+1})}{1 + \text{cross terms}}. $$
Because $\rho(z_n, z_{n+1}) \to 0$, if $\eta$ is forced to be small, the zeros $w_n$ and $w_{n+1}$ of the interpolating product $b(z)$ are forced unacceptably close together, inevitably destroying its mandatory separation constant $\delta > 0$. Finding a configuration of $\{w_k\}$ that bypasses this metric collapse while keeping the function globally bounded by $\epsilon$ constitutes the core barrier of Garnett's Problem.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*