---
id: 01-number-theory/lindelof-hypothesis
title: "Lindelof Hypothesis"
topic: 01-number-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Lindelöf Hypothesis

> **Topic:** Number Theory · **ID:** `01-number-theory/lindelof-hypothesis` · **Status:** open

## 1. Problem Statement / Conjecture

The Lindelöf Hypothesis concerns the asymptotic growth rate of the Riemann zeta function, $\zeta(s)$, along the "critical line" in the complex plane, where the real part of the variable $s = \sigma + it$ is exactly $1/2$. The hypothesis conjectures that for any arbitrarily small $\epsilon > 0$, the Riemann zeta function satisfies the asymptotic bound:

$$ \zeta\left(\frac{1}{2} + it\right) = O(|t|^\epsilon) \quad \text{as } |t| \to \infty $$

In other words, the amplitude of the Riemann zeta function on the critical line grows slower than any positive polynomial power of $|t|$. A complete proof requires establishing this bound unconditionally for all sufficiently large $|t|$.

## 2. Mathematical Foundations

The Riemann zeta function is defined for complex numbers $s = \sigma + it$ with $\sigma > 1$ by the absolutely convergent Dirichlet series:

$$ \zeta(s) = \sum_{n=1}^\infty \frac{1}{n^s} $$

Through its functional equation, $\zeta(s)$ can be analytically continued to a meromorphic function on the entire complex plane, with a single simple pole at $s = 1$. The functional equation is given by:

$$ \zeta(s) = 2^s \pi^{s-1} \sin\left(\frac{\pi s}{2}\right) \Gamma(1-s) \zeta(1-s) $$

To formalize the Lindelöf Hypothesis, mathematicians study the growth exponent $\mu(\sigma)$, defined as the infimum of all real numbers $c \ge 0$ such that:

$$ \zeta(\sigma + it) = O(|t|^c) \quad \text{as } |t| \to \infty $$

From standard bounds, we know that for $\sigma > 1$, $\mu(\sigma) = 0$. By the functional equation and Stirling's approximation for the Gamma function $\Gamma(1-s)$, the growth rate in the region $\sigma < 0$ is governed by $\mu(\sigma) = \frac{1}{2} - \sigma$. 

The Phragmén-Lindelöf principle from complex analysis dictates that the function $\mu(\sigma)$ must be continuous and convex. Drawing a straight line between $\mu(0) = 1/2$ and $\mu(1) = 0$ yields the "convexity bound" in the critical strip $0 \le \sigma \le 1$:

$$ \mu(\sigma) \le \frac{1 - \sigma}{2} $$

Specifically, at $\sigma = 1/2$, the convexity bound provides $\mu(1/2) \le 1/4$. The Lindelöf Hypothesis posits a vastly stronger constraint: it asserts that $\mu(1/2) = 0$, which by convexity would force $\mu(\sigma) = 0$ for all $\sigma \ge 1/2$, and $\mu(\sigma) = 1/2 - \sigma$ for all $\sigma \le 1/2$.

## 3. History & State of the Art (SOTA)

- **1908**: Ernst Lindelöf formally proposed the conjecture while studying the growth rate of analytic functions and their bounds in vertical strips.
- **1921**: G. H. Hardy and J. E. Littlewood established the first "subconvexity" bound by breaking the $1/4$ barrier, proving $\mu(1/2) \le 1/6 \approx 0.16667$. They achieved this using Weyl's method for estimating exponential sums.
- **1920s–2000s**: A long lineage of improvements utilized increasingly sophisticated variations of the Hardy-Littlewood circle method and Vinogradov's mean value theorem. Key milestones include Walfisz (1924), Titchmarsh (1931), Kolesnik (1982), Iwaniec and Mozzochi (1988), and M. N. Huxley, who achieved $\mu(1/2) \le 32/205 \approx 0.15610$ in 2005.
- **2017 (Current SOTA)**: Jean Bourgain achieved a breakthrough by adapting the newly developed theory of $\ell^2$-decoupling in harmonic analysis. Bourgain established the current state-of-the-art exponent:

$$ \mu\left(\frac{1}{2}\right) \le \frac{13}{84} \approx 0.15476 $$

## 4. Partial Results / Verified Cases

While the general continuous hypothesis $\mu(1/2) = 0$ remains unproven, substantial partial results and structurally related cases have been verified:

1. **Computational Verification:** The hypothesis is heavily supported by numerical evidence. High-precision computations of the zeros of the zeta function (e.g., Xavier Gourdon's 2004 computation evaluating heights up to $t \approx 10^{13}$) demonstrate that the amplitude of $\zeta(1/2 + it)$ remains extraordinarily small and entirely consistent with logarithmic or $O(|t|^\epsilon)$ growth.
2. **Implication by the Riemann Hypothesis (RH):** It is a classic theorem (proven by Littlewood in 1912) that the Riemann Hypothesis strictly implies the Lindelöf Hypothesis. If $\zeta(s) \neq 0$ for all $\sigma > 1/2$, bounding the logarithmic derivative $\frac{\zeta'(s)}{\zeta(s)}$ rigorously forces $\zeta(1/2+it) = O(|t|^\epsilon)$. The converse, however, is false: Lindelöf does not imply RH.
3. **Integral Moments:** The Lindelöf hypothesis is equivalent to proving that the $2k$-th continuous moments of the zeta function satisfy:
$$ \int_0^T \left|\zeta\left(\frac{1}{2} + it\right)\right|^{2k} dt = O(T^{1+\epsilon}) $$
for all integers $k \ge 1$. This has been proven unconditionally for the specific dimensions $k=1$ (Hardy-Littlewood, 1918) and $k=2$ (A.E. Ingham, 1926). 

## 5. Principal Obstacles

The central bottleneck in improving the bound on $\mu(1/2)$ lies in the extreme difficulty of demonstrating perfect algebraic cancellation within short exponential sums of the form:

$$ S(N, t) = \sum_{N < n \le 2N} n^{it} = \sum_{N < n \le 2N} e^{i t \log n} $$

Traditional analytic methods operate by approximating these discrete sums with continuous highly oscillatory integrals (the stationary phase method) or by lifting the sum into higher dimensions to extract mean-value cancellations. 
However, these techniques suffer from two major structural constraints:
- **The Square Root Barrier:** Unconditional estimation techniques hit a natural combinatorial limit where the error terms (e.g., from Fourier approximations) become as large as the primary extraction of cancellation, colloquially acting as a barrier that prevents the exponent $\mu$ from approaching zero.
- **Failure of Standard Decoupling:** While Bourgain's $\ell^2$-decoupling theory successfully resolved the main conjecture in Vinogradov's Mean Value Theorem (which involves curves of the pure algebraic form $(x, x^2, \dots, x^k)$), it stalls when applied to the zeta function. The phase function $\phi(x) = t \log x$ does not possess the strict polynomial algebraic structure required for perfect decoupling, capping the maximum theoretical improvements at exactly $13/84$.

## 6. The Gap

The precise mathematical gap lies between the analytic geometry of subconvexity—which provides the $13/84$ bound—and the theoretical limit of exactly $0$. Current subconvexity estimates rely on bounding integrals where the phase function inherently forces some local constructive interference. This establishes an artificial "floor" on the exponent.

To cross this boundary and fully resolve the conjecture, mathematics requires a fundamentally new framework that bypasses local stationary phase limitations. Either a breakthrough in continuous harmonic analysis is needed to model transcendental non-algebraic curves without loss, or a structural insight must be found that maps the discrete exponential sum into an entirely different geometric context (such as motives or the Langlands program) where the cancellation is enforced by rigid global symmetries rather than local analytic approximations.

## 7. Current Research (as of June 2026)

Active research aiming toward the Lindelöf Hypothesis primarily targets generalized frameworks and probabilistic heuristics:

- **Random Matrix Theory (RMT):** Researchers use RMT models (e.g., the Fyodorov-Hiary-Keating conjectures) to predict the exact maximum values of $|\zeta(1/2+it)|$ in short intervals. *(frontier — verify)*: While RMT gives incredibly accurate distributional heuristics, finding a rigorous theoretical bridge to map probabilistic independence back to deterministic exponential sums remains a profound open challenge.
- **Higher Moments:** Research groups at Oxford (including Jon Keating's collaborators) and the Institute for Advanced Study are actively focused on deriving asymptotic formulas for the 6th ($k=3$) and 8th ($k=4$) moments of the Riemann zeta function. Breakthroughs in resolving the off-diagonal terms for $k \ge 3$ would unilaterally shatter the current $13/84$ barrier.
- **Subconvexity for Higher $L$-functions:** Proving unconditional subconvexity bounds for higher-degree $L$-functions over number fields (such as $\text{GL}_2$ and $\text{GL}_3$ automorphic $L$-functions) is heavily active (e.g., the work of Munshi, Nelson, and Michel-Venkatesh). 

## 8. Future Work

Leading mathematicians suggest that attacking the Lindelöf Hypothesis directly via traditional exponential sums is likely exhausted. Wide open pathways include:
1. **The Moment Problem:** Fully solving the exact asymptotic formula for $\int_0^T |\zeta(1/2+it)|^6 dt$. Even establishing the exact leading constant for the sixth moment would require revolutionary new ideas in bounding shifted convolution sums of divisor functions.
2. **Generalization through the Langlands Program:** The belief that a universal, geometric understanding of subconvexity for the broader Selberg class of $L$-functions will eventually yield the Lindelöf hypothesis as a trivial base case. Future strategies involve exploring trace formulas in automorphic representations where the necessary exponential cancellation is an inherent feature of the underlying representation theory.

## 9. Key References

- **[Foundational]** Lindelöf, E. *Quelques remarques sur la croissance de la fonction $\zeta(s)$.* Bulletin des Sciences Mathématiques, 32, 341-356, 1908.
- **[Foundational]** Titchmarsh, E. C., and Heath-Brown, D. R. *The Theory of the Riemann Zeta-Function.* Oxford University Press, 1986.
- **[SOTA / Recent]** Bourgain, J. *Decoupling, exponential sums and the Riemann zeta function.* Journal of the American Mathematical Society, 30(1), 205-224, 2017.
- **[Survey]** Ivić, A. *The Riemann Zeta-Function: Theory and Applications.* Dover Publications, 2003.

## 10. Worked Example / Concrete Special Case

To ground this problem, we can walk through a concrete calculation that demonstrates the standard "convexity bound"—the baseline that the Lindelöf Hypothesis explicitly seeks to improve—by evaluating the asymptotic growth of the zeta function at the boundaries of the critical strip.

Let $s = \sigma + it$ for large positive $t$. 

**Step 1: The Right Boundary ($\sigma = 1$)**
For $\sigma > 1$, the Dirichlet series converges. Directly on the boundary at $\sigma = 1$, using partial summation bounds on the sum $\sum (1/n^{1+it})$, a standard result dictates that the growth is at most logarithmic:
$$ \zeta(1 + it) = O(\log t) = O(t^0) $$
Therefore, the growth exponent on this boundary is exactly $\mu(1) = 0$.

**Step 2: The Left Boundary ($\sigma = 0$)**
To find the behavior at $\sigma = 0$, we rely on the functional equation:
$$ \zeta(s) = 2^s \pi^{s-1} \sin\left(\frac{\pi s}{2}\right) \Gamma(1-s) \zeta(1-s) $$
We evaluate this at $s = it$. 
The absolute value of the trigonometric part grows exponentially: 
$$ \left|\sin\left(i\frac{\pi t}{2}\right)\right| \sim \frac{1}{2} e^{\pi t / 2} $$
By Stirling's approximation for the Gamma function, we have: 
$$ |\Gamma(1 - it)| \sim \sqrt{2\pi} e^{-\pi t / 2} t^{1/2} $$
The remaining term $\zeta(1 - it)$ is evaluated at real part $1$, which we know from Step 1 behaves like $O(\log t)$.
Multiplying these asymptotic magnitudes together yields massive cancellations in the exponential terms:
$$ |\zeta(it)| \sim \left( e^{\pi t / 2} \right) \left( e^{-\pi t / 2} t^{1/2} \right) \log t \approx t^{1/2} \log t $$
Ignoring the logarithmic factor (which is absorbed by arbitrarily small powers of $t$), the growth exponent on this boundary is exactly $\mu(0) = 1/2$.

**Step 3: Interpolation and Convexity**
By the Phragmén-Lindelöf principle, the maximum modulus of an analytic function in a vertical strip is bounded by the strict interpolation of its boundary values. Thus, $\mu(\sigma)$ must be a convex function connecting the points $(0, 1/2)$ and $(1, 0)$.
The straight line connecting these points is given by:
$$ \mu(\sigma) = \frac{1-\sigma}{2} $$
Plugging in $\sigma = 1/2$, we obtain the baseline convexity bound:
$$ \mu\left(\frac{1}{2}\right) \le \frac{1}{4} $$
This shows that unconditionally $\zeta(1/2 + it) = O(t^{1/4 + \epsilon})$. The Lindelöf Hypothesis states that this straight-line interpolation is a drastic overestimation at the center, and the true value should drop to exactly $0$.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*