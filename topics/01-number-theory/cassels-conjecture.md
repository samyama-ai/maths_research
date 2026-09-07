---
id: 01-number-theory/cassels-conjecture
title: "Cassels' Conjecture"
topic: 01-number-theory
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Cassels' Conjecture

> **Topic:** Number Theory · **ID:** `01-number-theory/cassels-conjecture` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Cassels' Conjecture concerns the exact algebraic evaluation of higher-order Gauss sums (Kummer sums) and the explicit determination of their complex phases. While the absolute value of a degree-$n$ Gauss sum modulo a prime $p$ is classically known to be $\sqrt{p}$, the exact phase argument is highly non-trivial. 

For the cubic case, J. W. S. Cassels conjectured that the phase of the cubic Gauss sum $G(\pi)$ over the Eisenstein integers can be explicitly expressed as a product of values of the Weierstrass $\wp$-function—associated with a specific elliptic curve with complex multiplication (CM)—evaluated at $\pi$-torsion points. 

In its modern, generalized form, the problem conjectures that the phase of any $n$-th order Gauss sum over a number field can be explicitly and algebraically determined by the periods of an abelian variety (or motivic period) with complex multiplication by the corresponding cyclotomic field. While the original cubic and quartic cases were proven in the late 1970s, establishing the explicit generalized product formulas for degrees $n \ge 5$ remains an open and partially solved mathematical frontier.

## 2. Mathematical Foundations

Let $K = \mathbb{Q}(\omega)$ be the Eisenstein field, where $\omega = e^{2\pi i / 3}$. For a primary prime $\pi \in \mathcal{O}_K$ (satisfying $\pi \equiv 1 \pmod 3$), the cubic residue symbol is defined for any $\alpha \in \mathcal{O}_K$ coprime to $\pi$ by:
$$ \left( \frac{\alpha}{\pi} \right)_3 \equiv \alpha^{(N(\pi)-1)/3} \pmod \pi $$
where $N(\pi)$ is the norm of $\pi$. The associated Kummer sum (cubic Gauss sum) is defined as:
$$ G(\pi) = \sum_{x \pmod \pi} \left( \frac{x}{\pi} \right)_3 e^{2\pi i \text{Tr}_{K/\mathbb{Q}}(x/\pi)} $$

Cassels introduced the elliptic curve $E: y^2 = 4x^3 - 1$, which has complex multiplication by the ring of integers $\mathcal{O}_K$. Let $\wp(z)$ denote the associated Weierstrass $\wp$-function, and $\Omega$ its fundamental real period. Cassels conjectured the exact algebraic identity for the phase:
$$ \frac{G(\pi)}{|G(\pi)|} = \epsilon(\pi) \prod_{k \in S} \wp\left( \frac{k \Omega}{\pi} \right) $$
where $S$ is a specifically chosen "one-third" set of residues modulo $\pi$, and $\epsilon(\pi)$ is an explicitly defined third root of unity depending on the arithmetic of $\pi$. 

## 3. History & State of the Art (SOTA)

The history of the problem begins with Ernst Kummer (1846), who performed statistical calculations on the arguments of cubic Gauss sums, observing a mysterious bias toward the positive real half-plane—a phenomenon known as "Kummer's mystery". In 1956, Tomio Kubota demonstrated that Kummer sums were deeply related to the division values of elliptic functions. 

In 1970, J. W. S. Cassels took Kubota's insights further and formulated the exact product formula for the phase of the cubic Gauss sum, grounding the analytic sum entirely in algebraic geometry. Charles R. Matthews proved Cassels' Conjecture in 1979 for the cubic case, and shortly after, extended the methodology to prove the analogous quartic case (often called the Cassels-Matthews Conjecture). In the same year, S. J. Patterson and D. R. Heath-Brown resolved Kummer's statistical mystery, proving that the phases are asymptotically equidistributed, and that Kummer's observed bias was a small-number artifact. The State of the Art currently focuses on generalizing these exact evaluations to arbitrary higher-degree Gauss sums using the modern framework of exponential motives.

## 4. Partial Results / Verified Cases

The conjecture and its direct lineage are verified in the following specific dimensions and parameters:
- **Cubic Degree ($n=3$):** The original Cassels' Conjecture was proven by C. R. Matthews (1979). 
- **Quartic Degree ($n=4$):** The explicit phase product formula utilizing the lemniscate elliptic curve ($y^2 = x^3 - x$) and complex multiplication by $\mathbb{Q}(i)$ was proven by Matthews (1979).
- **Quadratic Degree ($n=2$):** The classical evaluation of the quadratic Gauss sum was solved by Carl Friedrich Gauss in 1801, representing the trivial $1$-dimensional case of this program.
- For higher general degrees ($n \ge 5$), the explicit geometric product formulas remain unsolved, marking the boundary of current verified cases.

## 5. Principal Obstacles

The primary bottleneck for the generalized Cassels' Conjecture (for arbitrary degree $n \ge 5$) is that elliptic curves only possess complex multiplication by imaginary quadratic fields. Therefore, they can only capture the arithmetic of quadratic, cubic, and quartic Gauss sums (using $\mathbb{Q}(i)$ and $\mathbb{Q}(\omega)$). 

For $n \ge 5$, the cyclotomic field $\mathbb{Q}(\zeta_n)$ has degree $\varphi(n) > 2$. To represent the phase of $n$-th degree Gauss sums, one must utilize abelian varieties of dimension $g \ge 2$ (such as the Jacobian of the Fermat curve $x^n + y^n = 1$). However, the theory of complex multiplication for higher-dimensional abelian varieties lacks a simple, single-variable analytic uniformizer analogous to the Weierstrass $\wp$-function. Consequently, writing down an explicit, computable product formula for the phase using values of generalized theta functions evaluated at torsion points is theoretically complex and currently non-explicit.

## 6. The Gap

The exact mathematical barrier lies between dimension $1$ (degrees 3 and 4) and dimension $g \ge 2$ (degree $n \ge 5$). In dimension $1$, the Weierstrass $\wp$-function provides a globally defined, explicit analytic uniformizer to extract periods and torsion values. To fully resolve the generalized Cassels conjecture, mathematicians must construct an explicit analytic product formula over higher-dimensional Jacobians that yields the exact phase of general cyclotomic Gauss sums, requiring a fully explicit theory of complex multiplication for higher-genus curves.

## 7. Current Research (as of June 2026)

Active research heavily utilizes the theory of **exponential motives**. Schools of thought led by researchers in arithmetic geometry are attempting to lift the Cassels-Matthews product formulas to arbitrary dimensions by identifying Gauss sums as periods of specific exponential motives. 

Recent preprints have focused on hypergeometric motives and establishing exact period relations that bypass the need for explicit theta-function evaluations. Connections to the geometric Langlands program suggest that the phase of generalized Gauss sums can be extracted from the epsilon factors of corresponding Galois representations *(frontier — verify)*. 

## 8. Future Work

Leading mathematicians suggest that future breakthroughs will require a synthesis of Arakelov geometry and the theory of motivic periods. Open pathways involve constructing explicit bases for the de Rham cohomology of Fermat curves such that the intersection pairings yield a generalized analog to the $\wp$-function product. Furthermore, extending these evaluations to non-abelian extensions (non-abelian Gauss sums) remains a long-term goal.

## 9. Key References

- **[Foundational]** Cassels, J.W.S. *On Kummer sums.* Proceedings of the London Mathematical Society, 1970.
- **[Foundational]** Matthews, C.R. *The proof of Cassels' conjecture on Kummer sums.* Inventiones Mathematicae, 1979.
- **[Survey]** Berndt, B.C., and Evans, R.J. *The determination of Gauss sums.* Bulletin of the American Mathematical Society, 1981.
- **[SOTA / Recent]** Fresán, J., & Jossen, P. *Exponential Motives.* Annals of Mathematics Studies, Princeton University Press, 2020.

## 10. Worked Example / Concrete Special Case

Consider the evaluation of the Kummer sum for the prime $p = 7$. In the Eisenstein integers $K = \mathbb{Q}(\omega)$, the prime $7$ splits as $7 = \pi \bar{\pi}$, where we can choose the prime factor $\pi = 2 + 3\omega$. The norm is $N(\pi) = 7$.

The cubic residue symbol $\chi_3(x) = \left(\frac{x}{\pi}\right)_3$ maps the multiplicative group $(\mathbb{Z}/7\mathbb{Z})^\times$ to the cube roots of unity $\{1, \omega, \omega^2\}$. Evaluating the values modulo $\pi$, the generator $3$ gives $\chi_3(3) = \omega$. The character values for $x = 1, 2, 3, 4, 5, 6$ correspond to the sequence $1, \omega^2, \omega, \omega, \omega^2, 1$.

The cubic Gauss sum is:
$$ G(\pi) = \sum_{x=1}^{6} \chi_3(x) e^{2\pi i x / 7} $$

Expanding this, we get:
$$ G(\pi) = e^{2\pi i / 7} + \omega^2 e^{4\pi i / 7} + \omega e^{6\pi i / 7} + \omega e^{8\pi i / 7} + \omega^2 e^{10\pi i / 7} + e^{12\pi i / 7} $$

We analytically know that the magnitude $|G(\pi)| = \sqrt{7}$. According to Cassels' product formula, the phase argument $G(\pi) / \sqrt{7}$ can be computed purely algebraically without expanding the complex exponentials. Let $E$ be $y^2 = 4x^3 - 1$ with fundamental period $\Omega$. 

Cassels' formula predicts that the phase is exactly determined by evaluating the Weierstrass $\wp$-function at specific $7$-torsion points on $E$, corresponding to a third-set $S$ (e.g., $S = \{1, 2\}$):
$$ \frac{G(\pi)}{\sqrt{7}} = \epsilon(\pi) \wp\left(\frac{\Omega}{\pi}\right) \wp\left(\frac{2\Omega}{\pi}\right) $$
By evaluating the $\wp$-function on this CM elliptic curve, the product yields the exact nested radical expression for the phase of $G(\pi)$, beautifully grounding the analytic trigonometric sum in the algebraic geometry of $E$.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*