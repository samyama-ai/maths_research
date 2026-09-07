---
id: 10-theoretical-cs/existence-of-one-way-functions
title: "Existence of One-Way Functions"
topic: 10-theoretical-cs
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Existence of One-Way Functions

> **Topic:** Theoretical Computer Science · **ID:** `10-theoretical-cs/existence-of-one-way-functions` · **Status:** open

## 1. Problem Statement / Conjecture

The conjecture stating the existence of one-way functions (OWFs) is the foundational assumption of modern cryptography. Informally, a one-way function is a mathematical function that is easy to compute on every input, but hard to invert given the image of a random input.

Formally, the open problem asks: **Does there exist a function $f: \{0,1\}^* \to \{0,1\}^*$ such that:**
1. **Easy to compute:** There exists a deterministic polynomial-time algorithm that computes $f(x)$ for all $x \in \{0,1\}^*$.
2. **Hard to invert:** For every probabilistic polynomial-time (PPT) algorithm $\mathcal{A}$, every positive polynomial $p(\cdot)$, and all sufficiently large $n$, the probability that $\mathcal{A}$ succeeds in finding a pre-image of $f(x)$ when $x$ is chosen uniformly at random from $\{0,1\}^n$ is strictly less than $1/p(n)$.

The existence of one-way functions implies that $\text{P} \neq \text{NP}$. It is, in fact, a strictly stronger claim than $\text{P} \neq \text{NP}$ because it requires average-case computational hardness over a specific distribution, whereas $\text{P} \neq \text{NP}$ only requires worst-case hardness. If one-way functions exist, then secure pseudorandom generators, digital signatures, and private-key cryptography are possible. If they do not, much of modern cryptographic infrastructure is fundamentally insecure against computationally bounded adversaries.

## 2. Mathematical Foundations

The formalization of the problem relies on the theory of computation, probability theory, and asymptotic complexity. 

Let $\{0,1\}^*$ denote the set of all finite binary strings. Let $|x|$ denote the length of a string $x \in \{0,1\}^*$. A function $\mu: \mathbb{N} \to \mathbb{R}$ is called **negligible** if for every positive polynomial $p(n)$, there exists an integer $N_0$ such that for all $n > N_0$, $|\mu(n)| < 1/p(n)$. We denote a negligible function as $\text{negl}(n)$.

A function $f: \{0,1\}^* \to \{0,1\}^*$ is a **strong one-way function** if it satisfies the following two conditions:
1. **Polynomial-time Computability:** There exists a deterministic Turing machine $M$ and a polynomial $q(\cdot)$ such that for all $x \in \{0,1\}^*$, $M(x) = f(x)$ and $M$ halts in at most $q(|x|)$ steps.
2. **Average-case Hardness to Invert:** For every probabilistic polynomial-time (PPT) Turing machine $\mathcal{A}$, the success probability of $\mathcal{A}$ in finding any valid pre-image is negligible. Formally:
   $$ \Pr_{x \xleftarrow{\$} \{0,1\}^n, r} \left[ \mathcal{A}(1^n, f(x); r) \in f^{-1}(f(x)) \right] \le \text{negl}(n) $$
   where $x \xleftarrow{\$} \{0,1\}^n$ denotes choosing $x$ uniformly at random from the set of strings of length $n$, and $r$ represents the internal random coin tosses of the adversary $\mathcal{A}$.

A **weak one-way function** is defined similarly, except the inversion probability is only bounded away from $1$. That is, for every PPT $\mathcal{A}$, there exists a polynomial $q(n)$ such that for all sufficiently large $n$:
$$ \Pr_{x \xleftarrow{\$} \{0,1\}^n} \left[ \mathcal{A}(1^n, f(x)) \in f^{-1}(f(x)) \right] \le 1 - \frac{1}{q(n)} $$

**Yao's Hardness Amplification Theorem** establishes that weak one-way functions exist if and only if strong one-way functions exist. The construction $F(x_1, \dots, x_k) = (f(x_1), \dots, f(x_k))$ for $k = \text{poly}(n)$ converts a weak OWF into a strong OWF.

## 3. History & State of the Art (SOTA)

The concept of computational asymmetry (functions easy to evaluate but hard to invert) was introduced conceptually by Diffie and Hellman (1976) in their seminal paper "New Directions in Cryptography." The formal definition of one-way functions as cryptographic primitives was crystallized in the 1980s through the work of Goldwasser, Micali, Yao, and Levin.

Major theoretical milestones include:
- **Impagliazzo's Worlds (1995):** Impagliazzo defined five distinct possible universes of computational complexity. The existence of OWFs places us in "Minicrypt" (where private-key cryptography exists) or "Cryptomania" (where public-key cryptography exists), while their non-existence places us in "Pessiland", "Heuristica", or "Algorithmica".
- **HILL Theorem (1999):** Håstad, Impagliazzo, Levin, and Luby proved that the existence of one-way functions is strictly equivalent to the existence of Pseudorandom Generators (PRGs). The construction is highly non-trivial, bridging unpredictability and pseudorandomness.
- **Rompel's Theorem (1990):** Rompel proved that one-way functions exist if and only if secure Digital Signatures exist, closing the loop on the minimal assumptions required for authentication.
- **Universal One-Way Function (Levin, 1987):** Levin constructed a specific function $f_{\text{univ}}$ that is one-way if *any* one-way function exists. It operates by simulating all Turing machines for bounded steps, leveraging a time-bounded Kolmogorov complexity framework.
- **Liu-Pass Equivalence (2020):** Liu and Pass proved that the existence of one-way functions is equivalent to the average-case hardness of approximating time-bounded Kolmogorov complexity ($K^t$), providing the first natural, non-cryptographic problem characterizing OWFs.

Currently, while unconditionally proving the existence of OWFs remains out of reach, SOTA cryptography builds upon extensively tested candidates.

## 4. Partial Results / Verified Cases

Because unconditionally proving the existence of OWFs implies proving $\text{P} \neq \text{NP}$, there are no verified cases of one-way functions in the absolute sense. However, there are many "candidate" one-way functions that have resisted decades of concerted cryptanalytic attacks:

1. **Integer Factorization:** Let $f(p, q) = p \cdot q$, where $p$ and $q$ are $n$-bit primes. The best known classical algorithm, the General Number Field Sieve (GNFS), runs in sub-exponential time $O(\exp(c \cdot n^{1/3} (\log n)^{2/3}))$. This makes $f$ a widely presumed one-way function, though it is vulnerable to Shor's algorithm on a quantum computer.
2. **Discrete Logarithm:** For a cyclic group $G$ of order $q$ with generator $g$, the function $f(x) = g^x \pmod p$ is assumed one-way.
3. **Lattice-Based Candidates (Post-Quantum):** 
   - **Learning with Errors (LWE):** Introduced by Regev (2005). The problem of finding a secret vector $s \in \mathbb{Z}_q^n$ given samples $(a, \langle a, s \rangle + e \pmod q)$, where $e$ is small noise. LWE is known to be as hard as worst-case lattice problems (like GapSVP).
   - **Short Integer Solution (SIS):** Finding a non-zero short vector $x$ such that $Ax \equiv 0 \pmod q$ for a random matrix $A$.
4. **Subset Sum:** Given numbers $a_1, \dots, a_n \in \mathbb{Z}$ and a target $T$, finding a subset summing to $T$. Certain density regimes of this problem yield strong OWF candidates.

Theoretical verified cases also include relative results: OWFs are proven to exist relative to a random oracle (by probability 1), demonstrating that structural, relativizing proofs cannot disprove their existence.

## 5. Principal Obstacles

Proving the existence of one-way functions is strictly harder than resolving the $\text{P} \neq \text{NP}$ problem. The primary obstacles are the fundamental barriers of complexity theory:

1. **The Relativization Barrier (Baker-Gill-Solovay, 1975):** There exist oracles $A$ and $B$ such that $\text{P}^A = \text{NP}^A$ (so OWFs do not exist relative to $A$) and $\text{P}^B \neq \text{NP}^B$ where OWFs *do* exist relative to $B$. Any proof of the existence of OWFs must use non-relativizing techniques (methods that do not treat the computation as a black box).
2. **The Natural Proofs Barrier (Razborov-Rudich, 1995):** Most known techniques for proving lower bounds in circuit complexity are "natural," meaning they identify a "largeness" condition (satisfied by most functions) and a "constructivity" condition (evaluable in polynomial time) that separate a complexity class. Razborov and Rudich proved that if one-way functions exist, natural proofs *cannot* separate $\text{P}$ from $\text{NP}$ or $\text{P/poly}$. Thus, a proof of the existence of OWFs must inherently be "unnatural" (e.g., highly specific to the algebraic structure of the function, rather than generic properties of boolean functions).
3. **The Algebrization Barrier (Aaronson-Wigderson, 2008):** Algebraic techniques (like arithmetization used in $\text{IP} = \text{PSPACE}$) fail to resolve questions about the existence of one-way functions because these questions remain open even when algorithms are given algebraic access to the underlying fields.
4. **Worst-case to Average-case Hardness:** While $\text{NP}$-complete problems are hard in the worst case (assuming $\text{P} \neq \text{NP}$), OWFs require a problem in $\text{NP}$ to be hard on *average* over a highly specific, samplable distribution (the uniform distribution of inputs). Feigenbaum, Fortnow, and others have shown that standard non-adaptive reductions cannot convert worst-case $\text{NP}$-hardness into average-case hardness unless the Polynomial Hierarchy collapses.

## 6. The Gap

The exact boundary between current knowledge and the full resolution of the conjecture lies in the chasm between worst-case complexity and average-case complexity within the class $\text{NP}$.

Currently, we can prove:
- Unconditional lower bounds for restricted computational models (e.g., $\text{AC}^0$, monotone circuits).
- Worst-case to average-case reductions for high-complexity classes like $\text{EXP}$ or $\text{PSPACE}$ (using random self-reducibility and error-correcting codes).
- Worst-case to average-case reductions within $\text{NP}$ for specific algebraic problems (e.g., LWE, which reduces worst-case lattice problems to average-case LWE).

However, we cannot establish that the worst-case hardness of a generic $\text{NP}$-complete problem (like 3-SAT) implies the existence of a one-way function. The gap requires a novel mathematical framework for extracting samplable, average-case hardness from worst-case hardness in a regime where verification is efficient ($\text{NP}$) but the computation is weak (bounded depth/time). The Liu-Pass equivalence isolates this gap to exactly the average-case hardness of computing $K^t$, shifting the gap from cryptography to the foundations of meta-complexity.

## 7. Current Research (as of June 2026)

The search for the resolution to the existence of OWFs currently centers heavily around **Meta-complexity** and **Fine-Grained Cryptography**.

1. **Meta-Complexity:** Following the breakthrough of Liu and Pass (2020), which proved that OWFs exist if and only if time-bounded Kolmogorov complexity ($K^t$) is hard to compute on average, the field of meta-complexity has seen explosive growth. Recent work focuses on whether the worst-case hardness of $K^t$ implies its average-case hardness. *$\text{*(frontier — verify)*}$ Researchers at Cornell and MIT are currently exploring reductions establishing that worst-case $\text{NP}$-hardness of Minimum Circuit Size Problem (MCSP) might imply average-case hardness of $K^t$, which would yield OWFs from worst-case assumptions.*
2. **Quantum One-Way Functions (QOWFs):** With classical OWFs vulnerable to quantum algorithms (if they rely on factoring/discrete log), the study of QOWFs (functions computable by polynomial-time quantum circuits but hard to invert by quantum adversaries) has become critical. A major research vector is whether QOWFs exist relative to a classical oracle where classical OWFs do not.
3. **Fine-Grained Cryptography:** Instead of demanding super-polynomial hardness, researchers are building cryptographic primitives that are computable in $O(n)$ time but require $O(n^2)$ time to invert. Recent bounds derived from the Strong Exponential Time Hypothesis (SETH) have established unconditional "fine-grained" OWFs against restricted adversaries, providing a sandbox for analyzing structural requirements of asymmetry.

## 8. Future Work

Leading theoretical computer scientists suggest the following pathways to bridge the gap:

1. **Studying the Minimum Circuit Size Problem (MCSP):** MCSP is a prominent candidate for bridging worst-case to average-case complexity. A major open path is proving whether MCSP is $\text{NP}$-complete under randomized reductions. If MCSP is $\text{NP}$-complete, and its worst-case to average-case reduction holds, one-way functions would exist assuming $\text{P} \neq \text{NP}$.
2. **Bypassing Black-Box Separations:** Because standard $\text{NP}$-complete problems cannot be reduced to average-case hardness via black-box reductions (as shown by Bogdanov-Trevisan and others), future proofs must leverage non-black-box techniques, such as those used in Barak's protocol. Utilizing the code of the adversary rather than just its input-output behavior is a widely cited prerequisite for future breakthroughs.
3. **Pseudorandomness from Derandomization:** Another vector connects the existence of OWFs to the derandomization of $\text{BPP}$. Establishing exactly what level of circuit lower bounds yields both derandomization and average-case hardness remains a fertile area, guided by the algorithmic method and the study of expander graphs.

## 9. Key References

- **[Foundational]** Diffie, W., & Hellman, M. *New directions in cryptography.* IEEE Transactions on Information Theory, 1976.
- **[Foundational]** Levin, L. A. *One-way functions and pseudorandom generators.* Combinatorica, 1987.
- **[Foundational]** Håstad, J., Impagliazzo, R., Levin, L. A., & Luby, M. *A pseudorandom generator from any one-way function.* SIAM Journal on Computing, 1999.
- **[SOTA / Recent]** Liu, Y., & Pass, R. *On One-way Functions and Kolmogorov Complexity.* IEEE 61st Annual Symposium on Foundations of Computer Science (FOCS), 2020.
- **[SOTA / Recent]** Hirahara, S. *Unexpected connections between routing algorithms and minimum circuit size problem.* Proceedings of the 53rd Annual ACM SIGACT Symposium on Theory of Computing (STOC), 2021.
- **[Survey]** Goldreich, O. *Foundations of Cryptography: Volume 1, Basic Tools.* Cambridge University Press, 2001.
- **[Survey]** Impagliazzo, R. *A Personal View of Average-Case Complexity.* Proceedings of the 10th Annual Structure in Complexity Theory Conference, 1995.

## 10. Worked Example / Concrete Special Case

To ground the concept, consider the most famous candidate for a one-way function: integer multiplication, whose inversion is integer factorization.

Let $f: \mathbb{N} \times \mathbb{N} \to \mathbb{N}$ be defined as:
$$ f(p, q) = p \times q $$
where $p$ and $q$ are required to be prime numbers of exactly $n$ bits in length.

**Forward Computation (Easy):**
Suppose $n = 4$ bits. We randomly select two prime numbers, $p = 11$ (binary `1011`) and $q = 13$ (binary `1101`).
Computing $f(11, 13) = 11 \times 13 = 143$. 
The standard multiplication algorithm (grade-school multiplication) computes this in time $O(n^2)$. Here, it requires just a few bitwise shifts and additions. The output is $143$ (binary `10001111`).

**Inversion (Hard):**
The adversary is given $N = 143$ and the parameter $n = 4$, and must find $p, q$ such that $p \times q = 143$.
For $n=4$, the adversary can simply use trial division up to $\sqrt{143} \approx 11$. They will quickly find $143 / 11 = 13$, fully inverting the function.

However, consider the asymptotic scaling when $n = 2048$ bits (typical in modern RSA cryptography).
- The forward computation $f(p, q)$ takes $O(2048^2)$ bit operations, which executes in microseconds on a standard CPU.
- To invert the function, the adversary is given a 4096-bit number $N$. The best known classical algorithm, the General Number Field Sieve (GNFS), has a heuristic time complexity of:
  $$ L_N\left[\frac{1}{3}, \sqrt[3]{\frac{64}{9}}\right] = \exp\left( \left(\sqrt[3]{\frac{64}{9}} + o(1)\right) (\ln N)^{1/3} (\ln \ln N)^{2/3} \right) $$
For $N \approx 2^{4096}$, this requires a number of operations vastly exceeding the estimated number of atoms in the observable universe. Thus, while $\mathcal{A}$ has a non-zero probability of guessing $p$ and $q$ completely at random, that probability is $1 / 2^{2048} \ll \text{negl}(n)$. 

Because there is no known polynomial-time algorithm $O(n^k)$ to compute the prime factors for arbitrary $N$, this specific mathematical instance perfectly models the asymmetry demanded by the conjecture, even if we cannot formally prove the lower bound of the inversion complexity.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*