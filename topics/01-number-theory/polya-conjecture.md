---
id: 01-number-theory/polya-conjecture
title: "Polya Conjecture"
topic: 01-number-theory
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Pólya Conjecture

> **Topic:** Number Theory · **ID:** `01-number-theory/polya-conjecture` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

The Pólya conjecture states that for any integer $n > 1$, the number of integers less than or equal to $n$ with an odd number of prime factors (counted with multiplicity) is greater than or equal to the number of integers less than or equal to $n$ with an even number of prime factors. 

Equivalently, it claims that the summatory Liouville function $L(n)$ is non-positive for all $n \ge 2$. In mathematical notation, the conjecture asserts:
$$L(n) \le 0 \quad \text{for all } n > 1.$$
Although historically proposed as a plausible truth, the conjecture has been proven false. Modern work on the problem shifts the focus to understanding the rare intervals where $L(n) > 0$ and investigating the density and distribution of these counterexamples.

## 2. Mathematical Foundations

The conjecture relies on the fundamental theorem of arithmetic and relies heavily on the study of multiplicative functions.

- Let $\Omega(n)$ denote the total number of prime factors of an integer $n$, counted with multiplicity. For example, if $n = p_1^{a_1} p_2^{a_2} \dots p_k^{a_k}$, then $\Omega(n) = a_1 + a_2 + \dots + a_k$.
- The **Liouville function** $\lambda(n)$ is a completely multiplicative arithmetic function defined as:
  $$\lambda(n) = (-1)^{\Omega(n)}$$
  By convention, $\Omega(1) = 0$, so $\lambda(1) = 1$.
- The **summatory Liouville function** $L(n)$ is defined as the partial sum of the Liouville function up to $n$:
  $$L(n) = \sum_{k=1}^n \lambda(k)$$

The behavior of $L(n)$ is intimately connected to the Riemann zeta function $\zeta(s)$ through the Dirichlet series:
$$\sum_{n=1}^\infty \frac{\lambda(n)}{n^s} = \frac{\zeta(2s)}{\zeta(s)}$$
which is absolutely convergent for $\Re(s) > 1$. The non-vanishing of $\zeta(s)$ on the line $\Re(s) = 1$ gives the Prime Number Theorem, which implies that $L(n) = o(n)$.

## 3. History & State of the Art (SOTA)

The conjecture was famously proposed by the Hungarian mathematician George Pólya in 1919. At the time, the conjecture was computationally verified up to $n = 1500$, and the heavy bias towards negative values of $L(n)$ made it a highly plausible hypothesis.

- **1958:** Colin Brian Haselgrove achieved a theoretical breakthrough by proving the conjecture false. He did this not by providing a specific counterexample, but by showing that $L(n)$ changes sign infinitely often. His proof relied on the assumption that there are no zeros of the Riemann zeta function off the critical line (though the argument can be modified if the Riemann Hypothesis fails) and utilized the linear independence of the imaginary parts of the non-trivial zeros over the rational numbers.
- **1960:** R. Sherman Lehman found the first explicit counterexample, $n = 906,150,257$.
- **1980:** Minoru Tanaka computationally determined the absolute smallest counterexample: $n = 906,150,256$.
- **SOTA (Recent Progress):** While the original conjecture is settled, modern high-performance computational number theory continues to probe the "Pólya regions" (ranges where $L(n) > 0$). Recent state-of-the-art algorithms evaluate the logarithmic density of these counterexamples and explore bounds on the fluctuations of $L(x) / \sqrt{x}$. 

## 4. Partial Results / Verified Cases

The conjecture actually holds true for the vast majority of small integers. 
- The inequality $L(n) \le 0$ is completely verified and true for all $2 \le n \le 906,150,255$.
- After the first counterexample at $n = 906,150,256$, $L(n)$ reaches a local maximum of $L(n) = 71$ at $n = 906,180,359$.
- The function eventually becomes negative again and oscillates. The regions where $L(n) > 0$ are extremely sparse; subsequent intervals of counterexamples have been verified to occur around $n \approx 1.7 \times 10^{10}$, $n \approx 4.3 \times 10^{10}$, and $n \approx 7.7 \times 10^{10}$.

## 5. Principal Obstacles

The initial obstacle in the 20th century was computational limitations. The strong negative bias in $L(n)$ known as "Chebyshev's bias" is caused by the behavior of the first non-trivial zero of the Riemann zeta function. 

Mathematically, the oscillation of $L(x)$ is roughly modeled by an explicit formula over the non-trivial zeros $\rho = \beta + i\gamma$ of $\zeta(s)$:
$$L(x) \approx \frac{\sqrt{x}}{\zeta(1/2)} + \sqrt{x} \sum_{\rho} \frac{x^{i\gamma}}{\rho \zeta'(\rho)}$$
Because the first zero $\gamma_1 \approx 14.13$ yields a large negative contribution, standard asymptotic limits and perturbation theory fail to reveal the sign change until $x$ is exponentially large. Exploring this interplay computationally requires calculating $\lambda(n)$ up to $10^{10}$ and beyond, which was impossible for early mathematicians using hand calculations or rudimentary computers.

## 6. The Gap

Because the main Pólya Conjecture was disproved, "the gap" today refers to our incomplete understanding of the distribution of sign changes for $L(n)$. The exact mathematical barrier to fully resolving the behavior of $L(n)$ is a rigorous, unconditional determination of the logarithmic density of the set $\mathcal{P} = \{n \in \mathbb{N} \mid L(n) > 0\}$. 

While Rubinstein and Sarnak established the framework for Chebyshev's bias in prime counting, calculating the exact probability measure for Liouville summatory function sign changes relies on the Grand Simplicity Hypothesis (the assumption that the imaginary parts of the zeros of $\zeta(s)$ are linearly independent over $\mathbb{Q}$), which remains completely out of reach of current analytic techniques.

## 7. Current Research (as of June 2026)

Current research directions focus on:
1. **The Logarithmic Density of Counterexamples:** Estimating the exact logarithmic density of the sets of integers for which the conjecture fails. 
2. **Generalizations to Arithmetic Progressions:** Investigating Pólya-type biases for Liouville functions restricted to arithmetic progressions $a \pmod q$.
3. **Mertens-Pólya Analogues:** Studying summatory functions of strictly multiplicative functions on polynomials over finite fields $\mathbb{F}_q[x]$.

*Research flag: *(frontier — verify)* Active computations are currently seeking to definitively establish whether the set of integers where $L(n)>0$ admits an asymptotic or natural density, or strictly only a logarithmic density.*

## 8. Future Work

Leading mathematicians working in prime bias suggest the following open pathways:
- Proving the Grand Simplicity Hypothesis for the Riemann zeta function, which would unconditionally clarify the limiting distribution of $L(n)/\sqrt{n}$.
- Applying advanced spectral methods and random matrix theory to model the fluctuations of $L(n)$ at limits exceeding $10^{20}$.
- Developing faster deterministic algorithms for evaluating $L(n)$ and $M(n)$ (the Mertens function) in sub-linear time, e.g., $\tilde{O}(n^{2/3})$, to expand empirical evidence of Pólya regions.

## 9. Key References

- **[Foundational]** Pólya, G. *Verschiedene Bemerkungen zur Zahlentheorie.* Jahresbericht der Deutschen Mathematiker-Vereinigung, 1919.
- **[Foundational]** Haselgrove, C. B. *A disproof of a conjecture of Pólya.* Mathematika, 1958. [DOI](https://doi.org/10.1112/s0025579300001480)
- **[Foundational]** Lehman, R. S. *On Liouville's function.* Mathematics of Computation, 1960.
- **[SOTA / Recent]** Tanaka, M. *A Numerical Investigation on Cumulative Sum of the Liouville Function.* Tokyo Journal of Mathematics, 1980. [DOI](https://doi.org/10.3836/tjm/1270216093)
- **[SOTA / Recent]** Borwein, P., Ferguson, R., & Mossinghoff, M. *Sign changes in sums of the Liouville function.* Mathematics of Computation, 2008. [DOI](https://doi.org/10.1090/s0025-5718-08-02036-x)
- **[Survey]** Rubinstein, M., & Sarnak, P. *Chebyshev's bias.* Experimental Mathematics, 1994.

## 10. Worked Example / Concrete Special Case

To understand the conjecture, we can manually compute $L(n)$ for the first 6 integers. Recall that $\Omega(n)$ is the count of prime factors, $\lambda(n) = (-1)^{\Omega(n)}$, and $L(n) = \sum_{k=1}^n \lambda(k)$.

1. $n=1$: By definition, $\Omega(1)=0$ (even). So $\lambda(1) = 1$. 
   $L(1) = 1$.
2. $n=2$: Prime, $\Omega(2)=1$ (odd). So $\lambda(2) = -1$. 
   $L(2) = 1 + (-1) = 0$.
3. $n=3$: Prime, $\Omega(3)=1$ (odd). So $\lambda(3) = -1$. 
   $L(3) = 0 + (-1) = -1$.
4. $n=4$: $4 = 2 \times 2$, so $\Omega(4)=2$ (even). So $\lambda(4) = 1$. 
   $L(4) = -1 + 1 = 0$.
5. $n=5$: Prime, $\Omega(5)=1$ (odd). So $\lambda(5) = -1$. 
   $L(5) = 0 + (-1) = -1$.
6. $n=6$: $6 = 2 \times 3$, so $\Omega(6)=2$ (even). So $\lambda(6) = 1$. 
   $L(6) = -1 + 1 = 0$.

Looking at the cumulative sums for $n \ge 2$, we have $L(2)=0$, $L(3)=-1$, $L(4)=0$, $L(5)=-1$, $L(6)=0$. For all these initial steps, $L(n) \le 0$. The number of odd-prime-factor integers clearly meets or exceeds the even-prime-factor integers early on, providing the empirical foundation that originally misled Pólya.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*