---
id: 01-number-theory/duffin-schaeffer-conjecture
title: "Duffin-Schaeffer Conjecture"
topic: 01-number-theory
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Duffin-Schaeffer Conjecture

> **Topic:** Number Theory · **ID:** `01-number-theory/duffin-schaeffer-conjecture` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

The Duffin-Schaeffer Conjecture (now a theorem) is a profound statement in metric number theory concerning how well real numbers can be approximated by rational numbers. 

Let $f: \mathbb{N} \to \mathbb{R}_{\geq 0}$ be any non-negative function. For a real number $\alpha$, consider the Diophantine inequality:
$$ \left| \alpha - \frac{p}{q} \right| < \frac{f(q)}{q} $$
where $p$ and $q$ are integers, $q > 0$, and they are strictly coprime, meaning $\gcd(p, q) = 1$. 

Let $W(f)$ denote the set of all real numbers $\alpha$ for which there exist infinitely many such rational solutions $p/q$. The conjecture states that the Lebesgue measure of $W(f)$ is full (i.e., almost all real numbers belong to $W(f)$) if and only if the following series diverges:
$$ \sum_{q=1}^{\infty} f(q) \frac{\varphi(q)}{q} = \infty $$
where $\varphi(q)$ is Euler's totient function. If the series converges, the Lebesgue measure of $W(f)$ is exactly $0$.

## 2. Mathematical Foundations

The conjecture naturally sits at the intersection of measure theory, Diophantine approximation, and analytic number theory. 

Let $\lambda$ denote the standard Lebesgue measure on the real line. Since the property of approximation by fractions is invariant under integer translation ($\alpha \mapsto \alpha + 1$), it suffices to study the problem on the unit interval $[0, 1]$.

For each denominator $q \in \mathbb{N}$, define the approximation set $E_q \subset [0,1]$ as the union of intervals around reduced fractions:
$$ E_q = \bigcup_{\substack{1 \leq p \leq q \\ \gcd(p,q)=1}} \left( \frac{p}{q} - \frac{f(q)}{q}, \frac{p}{q} + \frac{f(q)}{q} \right) \pmod 1 $$
Assuming $f(q) < 1/2$ (without loss of generality, as larger $f(q)$ trivially covers the interval), these intervals are disjoint. The Lebesgue measure of $E_q$ is simply the number of intervals multiplied by their length:
$$ \lambda(E_q) = \varphi(q) \frac{2f(q)}{q} $$
The set $W(f) \cap [0,1]$ is precisely the limit superior of these sets:
$$ W(f) = \limsup_{q \to \infty} E_q = \bigcap_{N=1}^{\infty} \bigcup_{q=N}^{\infty} E_q $$

The convergence half of the conjecture follows immediately from the First Borel-Cantelli Lemma: if $\sum \lambda(E_q) < \infty$, then $\lambda(\limsup E_q) = 0$. The divergence half requires establishing a form of the Second Borel-Cantelli Lemma, which demands showing that the sets $E_q$ are "sufficiently independent" of one another.

## 3. History & State of the Art (SOTA)

The history of the problem originates with Khinchin's Theorem (1924), which provided a similar divergence/convergence criterion but required the approximation function $f(q)$ to be monotonically decreasing. Khinchin's formulation also did not enforce the coprimality condition $\gcd(p,q)=1$.

In 1941, Richard J. Duffin and Albert C. Schaeffer demonstrated that if the monotonicity condition on $f$ is dropped, Khinchin's original theorem fails. They constructed a counterexample using highly composite denominators to create massive overlaps between approximation sets, leading to a divergent sum but a measure-zero approximation set. To fix this, they introduced the coprimality constraint to prune redundant fractions, formulating the Duffin-Schaeffer conjecture.

For nearly 80 years, the conjecture remained one of the most prominent open problems in metric number theory. In July 2019, Dimitris Koukoulopoulos and James Maynard announced a complete proof of the conjecture, which was subsequently published in the *Annals of Mathematics* in 2020. 

## 4. Partial Results / Verified Cases

Prior to the full resolution in 2019, several significant partial results constrained the behavior of the problem:

1. **Erdős (1970):** Proven for the case where $f(q)$ is restricted to take the form $c/q$ (for some constant $c > 0$) or when $f(q)$ is supported entirely on a sequence of integers where either $q_k \mid q_{k+1}$ or the sequence elements are pairwise coprime.
2. **Vaaler (1978):** Proven for any function satisfying $f(q) = O(q^{-1})$, effectively handling functions bounded by the standard Dirichlet approximation rate.
3. **Extra Divergence (Gallagher 1961):** If the weaker sum $\sum f(q) = \infty$ diverges, and additionally $f(q)$ satisfies certain regularity bounds, the conjecture holds. Gallagher also proved the higher-dimensional analogue of the conjecture.
4. **Pollington and Vaughan (1990):** Solved higher-dimensional analogues comprehensively, showing that in dimensions $k \geq 2$, the equivalent conjecture is unequivocally true.
5. **Aistleitner et al. (2014):** Reduced the divergence half of the conjecture to bounding the structural properties of "GCD graphs", effectively transforming the analytic problem into a combinatorial one.

## 5. Principal Obstacles

The primary barrier to proving the conjecture was the failure of classical independence heuristics. To use the Second Borel-Cantelli Lemma or its variants (such as the Chung-Erdős inequality), one must prove that the pairwise intersections of the sets $E_q$ and $E_r$ are not substantially larger than they would be if the sets were perfectly independent. 

Specifically, one needs to bound the overlap integral:
$$ \lambda(E_q \cap E_r) \approx \lambda(E_q)\lambda(E_r) \prod_{p \mid \frac{qr}{\gcd(q,r)^2}} \left(1 - \frac{1}{p}\right)^{-1} $$
When $q$ and $r$ share a large greatest common divisor (GCD) and have many prime factors in common, the sets $E_q$ and $E_r$ can exhibit intense pathological correlation. Analytic tools like Fourier analysis, the Hardy-Littlewood circle method, and traditional sieve theory all struggle to capture the arithmetic resonance occurring uniformly over *arbitrary* support sets for the function $f$. 

## 6. The Gap

Before Koukoulopoulos and Maynard's proof, the precise mathematical barrier was proving a uniform upper bound on the mass of "GCD graphs"—graphs where vertices are integers from the support of $f$, and edges encode the property that the vertices share a large GCD. 

The gap was bridged by departing from traditional number theory and employing structural graph theory. Koukoulopoulos and Maynard mapped the arithmetic structure of prime factors to a network flow problem. They developed a novel iterative compression algorithm to show that if a GCD graph were to violate the required bounds, it would contain a highly structured "bottleneck." They then used the fundamental arithmetic properties of primes to prove that such a strictly localized bottleneck cannot exist globally in the integers.

## 7. Current Research (as of June 2026)

With the primary conjecture solved, the frontier of metric number theory has shifted to generalized paradigms:

- **Manifold Intersections:** Formulating and proving Duffin-Schaeffer analogues for dependent quantities, where $\alpha$ is restricted to a smooth manifold (e.g., curves like $(x, x^2)$ in $\mathbb{R}^2$ or fractal measures). *(frontier — verify)*
- **$p$-adic and Function Fields:** While some function field analogues were resolved concurrently or shortly after, sharp bounds on local fields ($\mathbb{Q}_p$) remain a highly active area of refinement. 
- **Dynamical Systems:** Reinterpreting the Koukoulopoulos-Maynard network flow method to study the "shrinking target problem" on homogeneous spaces and unipotent flows.
- **Quantitative Bounds:** Establishing effective rates of convergence; knowing *how many* coprime solutions $p/q$ exist up to a height $Q$, with precise error terms.

## 8. Future Work

Leading researchers emphasize several open pathways built on the ashes of the Duffin-Schaeffer Conjecture:
- **The Littlewood Conjecture:** Though distinct, the structural insights regarding prime factorization and network flows are being adapted in attempts to address the Littlewood conjecture in simultaneous Diophantine approximation.
- **Higher-order Correlations:** The techniques introduced by Koukoulopoulos and Maynard currently bound pairwise overlaps ($\lambda(E_q \cap E_r)$). Future work aims to generalize these graph-theoretic tools to hypergraphs to handle $k$-wise intersections, which is critical for understanding the fine-scale distribution and variance of the error terms in Diophantine counting problems.

## 9. Key References

- **[Foundational]** R. J. Duffin, A. C. Schaeffer. *Khintchine's problem in metric Diophantine approximation.* Duke Mathematical Journal, 1941.
- **[Foundational]** A. Khinchin. *Einige Sätze über Kettenbrüche, mit Anwendungen auf die Theorie der Diophantischen Approximationen.* Mathematische Annalen, 1924. [DOI](https://doi.org/10.1007/bf01448437)
- **[SOTA / Recent]** D. Koukoulopoulos, J. Maynard. *On the Duffin-Schaeffer conjecture.* Annals of Mathematics, 2020. [DOI](https://doi.org/10.4007/annals.2020.192.1.5)
- **[Survey]** G. Harman. *Metric Number Theory.* LMS Monographs, 1998. [DOI](https://doi.org/10.1093/oso/9780198500834.001.0001)
- **[Survey]** A. Pollington, R. C. Vaughan. *The k-dimensional Duffin and Schaeffer conjecture.* Journal de Théorie des Nombres de Bordeaux, 1990. [DOI](https://doi.org/10.1112/s0025579300012900)

## 10. Worked Example / Concrete Special Case

To understand the core geometric objects of the conjecture, we can explicitly compute an approximation set $E_q$ and see how the Euler totient function $\varphi(q)$ dictates its measure.

Let us fix the denominator $q = 6$. The prime factors of $6$ are $2$ and $3$. The positive integers less than $6$ that are strictly coprime to $6$ are $p=1$ and $p=5$. Therefore, $\varphi(6) = 2$.

Suppose our target function evaluates to $f(6) = \frac{1}{4}$ at $q=6$. The inequality $|\alpha - p/6| < \frac{1/4}{6} = \frac{1}{24}$ dictates the valid intervals. 
We construct $E_6$ by taking the union of intervals of radius $\frac{1}{24}$ centered at the reduced fractions $\frac{1}{6}$ and $\frac{5}{6}$:
$$ E_6 = \left( \frac{1}{6} - \frac{1}{24}, \frac{1}{6} + \frac{1}{24} \right) \cup \left( \frac{5}{6} - \frac{1}{24}, \frac{5}{6} + \frac{1}{24} \right) $$
Converting to common denominators:
$$ E_6 = \left( \frac{3}{24}, \frac{5}{24} \right) \cup \left( \frac{19}{24}, \frac{21}{24} \right) $$
Because $f(6) = \frac{1}{4} < \frac{1}{2}$, these intervals are strictly disjoint. The Lebesgue measure (length) of each interval is $\frac{2}{24} = \frac{1}{12}$. 

The total Lebesgue measure is the number of intervals multiplied by the length of each interval:
$$ \lambda(E_6) = 2 \times \frac{1}{12} = \frac{1}{6} $$
We can verify this perfectly matches the theoretical formula from Section 2:
$$ \lambda(E_q) = 2 f(q) \frac{\varphi(q)}{q} \implies \lambda(E_6) = 2 \left(\frac{1}{4}\right) \frac{2}{6} = \frac{1}{6} $$
The Duffin-Schaeffer conjecture states that if you take an infinite sum of these exact measures $\lambda(E_q)$ across all $q$, and the sum diverges to infinity, then almost every real number $\alpha$ will fall into infinitely many such intervals.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*