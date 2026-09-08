---
id: 01-number-theory/infinitude-of-regular-primes
title: "Infinitude of Regular Primes"
topic: 01-number-theory
status: empirically-supported
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Infinitude of Regular Primes

> **Topic:** Number Theory · **ID:** `01-number-theory/infinitude-of-regular-primes` · **Status:** empirically-supported

## 1. Problem Statement / Conjecture

The conjecture states that there exist infinitely many regular primes. 

A prime $p$ is defined as **regular** if it does not divide the class number of the $p$-th cyclotomic field. Equivalently (by Kummer's criterion), an odd prime $p$ is regular if and only if it does not divide the numerator of any of the Bernoulli numbers $B_k$ for even integers $k$ in the range $2 \le k \le p-3$. 

While it has been proven that there are infinitely many *irregular* primes, the infinitude of regular primes remains one of the most famous open questions in algebraic number theory. It is universally conjectured to be true; in fact, heuristic arguments suggest that the asymptotic density of regular primes among all primes is precisely $e^{-1/2} \approx 0.6065$. A complete proof would mathematically guarantee that this set is unbounded.

## 2. Mathematical Foundations

Let $p$ be an odd prime and $\zeta_p = e^{2\pi i / p}$ be a primitive $p$-th root of unity. We define the $p$-th cyclotomic field as $K = \mathbb{Q}(\zeta_p)$, which has the ring of integers $\mathcal{O}_K = \mathbb{Z}[\zeta_p]$. 

The **ideal class group** of $K$, denoted $Cl(K)$, is the quotient group of fractional ideals of $\mathcal{O}_K$ by its principal fractional ideals. Its order is the **class number** $h_p = |Cl(K)|$. 
An odd prime $p$ is **regular** if $p \nmid h_p$ and **irregular** if $p \mid h_p$.

Kummer's seminal contribution was linking this algebraic definition to the **Bernoulli numbers** $B_k$, which are rational numbers defined via the exponential generating function:
$$ \frac{x}{e^x - 1} = \sum_{k=0}^{\infty} B_k \frac{x^k}{k!} $$
The first few non-zero Bernoulli numbers with even indices are $B_2 = \frac{1}{6}, B_4 = -\frac{1}{30}, B_6 = \frac{1}{42}, B_8 = -\frac{1}{30}, B_{10} = \frac{5}{66}$, etc. We say a prime $p$ divides $B_k$ (or more accurately, its numerator) if $p$ divides the numerator of $B_k$ when expressed as a fraction in lowest terms. 

**Kummer's Criterion:** An odd prime $p$ is regular if and only if $p$ does not divide the numerator of $B_k$ for any even index $k \in \{2, 4, 6, \dots, p-3\}$.

## 3. History & State of the Art (SOTA)

The history of regular primes is intrinsically tied to Fermat's Last Theorem (FLT). In 1847, Ernst Kummer achieved a massive breakthrough by proving that the equation $x^p + y^p = z^p$ has no non-trivial integer solutions for all regular primes $p$. He later explicitly identified the first irregular primes: $37, 59,$ and $67$. 

Because proving FLT using Kummer's approach required demonstrating that there were infinitely many regular primes, the distribution of regular primes became a central focus. However, the first infinitude result went in the opposite direction: in 1915, K. L. Jensen proved unconditionally that there are infinitely many *irregular* primes of the form $4n + 3$. The result for all irregular primes was expanded by various mathematicians over the 20th century.

In 1964, Carl Ludwig Siegel formalized a probabilistic heuristic. Assuming that the numerators of the Bernoulli numbers $B_k$ modulo $p$ behave like independent uniformly distributed random variables, the probability that $p$ does not divide any of the $(p-3)/2$ numerators should approach:
$$ \lim_{p \to \infty} \left(1 - \frac{1}{p}\right)^{\frac{p-3}{2}} = e^{-1/2} $$
This suggests that roughly $60.65\%$ of all primes are regular. The state of the art largely consists of ever-expanding computational evidence strongly confirming Siegel's asymptotic limit, but theoretical progress on the infinitude remains non-existent.

## 4. Partial Results / Verified Cases

There are no theoretically proven infinite families of regular primes. All partial results take the form of vast computational verifications:
- By 2001, Buhler et al. computed the regularity of all primes up to 12 million, finding that the ratio of regular primes perfectly aligned with $e^{-1/2}$.
- By 2011, Buhler and Harvey developed multimodular algorithms and Fast Fourier Transforms (FFTs) to compute irregular primes up to $163 \times 10^6$. 
- More recent distributed computing projects have pushed this boundary into the billions. 
- In every computational bound established so far, the proportion of regular primes converges tightly to $0.6065...$, strongly supporting Siegel's density heuristic and the general infinitude conjecture.

## 5. Principal Obstacles

The fundamental bottleneck in proving the infinitude of regular primes is the inherent asymmetry in proving divisibility versus non-divisibility. 

To prove that a prime is *irregular* (as Jensen did), one only needs to find a *single* index $k$ such that $p \mid B_k$. Jensen succeeded by constructing a carefully crafted sequence of indices using Kummer's congruences, forcing a prime factor to appear in the numerators.

To prove that a prime is *regular*, one must prove that $p$ avoids dividing the numerators of $B_k$ for an entire expanding set of $(p-3)/2$ indices. Standard tools of analytic number theory, such as sieve methods, fail because the target values (the Bernoulli numerators) grow exponentially and do not exhibit sufficient local constraints or structured algebraic periodicity that a sieve can leverage. Furthermore, traditional algebraic geometry and Iwasawa theory describe the structures of class groups where primes *do* divide the class number, but offer few unconditional tools to force a class number to be coprime to $p$.

## 6. The Gap

The exact boundary between what is known and the conjecture is the transition from probabilistic models of ideal class groups to deterministic primes. The Cohen-Lenstra heuristics heavily support the notion that class groups of number fields behave like random abelian groups equipped with certain automorphisms, which organically leads to Siegel's $e^{-1/2}$ density. The "gap" is the complete lack of a deterministic bounding mechanism capable of proving that this probabilistic non-divisibility condition manifests infinitely often in the actual integers.

## 7. Current Research (as of June 2026)

Current research approaches the problem from three main angles:
1. **Algorithmic advances:** Pushing computational limits to larger values of $p$ using optimized arithmetic in $\mathbb{Z}[x]$ and improvements in FFTs over finite fields.
2. **Function Field Analogues:** Exploring the geometric analogues of regular primes over function fields $\mathbb{F}_q(T)$. Through Weil's conjectures and étale cohomology, counting class groups in function fields translates to studying random matrices in symplectic groups (e.g., the work of Ellenberg, Venkatesh, and Westerland). *(frontier — verify)* Extending these density bounds in characteristic $p$ could inspire new approaches in characteristic 0.
3. **Iwasawa Theory and Vandiver's Conjecture:** Much of the modern study of irregular primes revolves around the deeper Vandiver Conjecture (that $p$ does not divide the class number of the maximal real subfield $K^+ = \mathbb{Q}(\zeta_p + \zeta_p^{-1})$). Progress on the structural invariants (the $\lambda$ and $\mu$ invariants of Iwasawa theory) continues to clarify the algebraic structure of irregular primes, even if it does not readily produce a regular prime.

## 8. Future Work

Leading number theorists have suggested several intermediate milestones:
- Establishing *any* lower bound on the counting function for regular primes, such as proving unconditionally that $\pi_{reg}(x) \gg \log\log x$.
- Proving statistical independence between the events $p \mid B_{k_1}$ and $p \mid B_{k_2}$ for $k_1 \neq k_2$.
- Resolving the infinitude of regular primes for specific generalized Bernoulli numbers associated with quadratic characters, where the arithmetic might offer a slightly different angle of attack.

## 9. Key References

- **[Foundational]** Kummer, E. E. *Allgemeiner Beweis des Fermat'schen Satzes, dass die Gleichung $x^\lambda + y^\lambda = z^\lambda$ durch ganze Zahlen unlösbar ist...* Journal für die reine und angewandte Mathematik, 1850.
- **[Foundational]** Jensen, K. L. *Om talteoretiske Egenskaber ved de Bernoulliske Tal.* Nyt Tidsskrift for Matematik B, 1915.
- **[Foundational]** Siegel, C. L. *Zu zwei Bemerkungen Kummers.* Nachrichten der Akademie der Wissenschaften in Göttingen, 1964.
- **[Survey]** Washington, L. C. *Introduction to Cyclotomic Fields (2nd Edition).* Springer, 1997.
- **[SOTA / Recent]** Buhler, J., Harvey, D. *Irregular primes to 163 million.* Mathematics of Computation, 2011. [DOI](https://doi.org/10.1090/s0025-5718-2011-02461-0)

## 10. Worked Example / Concrete Special Case

To understand Kummer's Criterion in practice, let us verify the regularity of $p=5$ and the irregularity of $p=37$.

**Case 1: $p=5$**
We must check the even integers $k$ such that $2 \le k \le 5-3$. 
The only integer in this range is $k=2$.
The Bernoulli number is $B_2 = \frac{1}{6}$. The numerator is $1$.
Since $5 \nmid 1$, Kummer's criterion is satisfied. The prime $5$ is **regular**.

**Case 2: $p=37$**
We must check the even integers $k$ such that $2 \le k \le 34$.
Let us examine the specific index $k = 32$. The Bernoulli number $B_{32}$ is a massive fraction:
$$ B_{32} = -\frac{7709321041217}{5100} $$
We look at the numerator: $7709321041217$. 
We test if it is divisible by $37$:
$$ 7709321041217 = 37 \times 208360028141 $$
Because $37$ divides the numerator of $B_{32}$, Kummer's criterion fails. The prime $37$ is **irregular**. 

*(Historical note: $37$ is the very first irregular prime, which is why Kummer had to single it out when attempting to prove Fermat's Last Theorem).*

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*