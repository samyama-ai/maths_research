---
id: 10-theoretical-cs/discrete-logarithm-in-p
title: "Discrete Logarithm in P"
topic: 10-theoretical-cs
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Discrete Logarithm in P

> **Topic:** Theoretical Computer Science · **ID:** `10-theoretical-cs/discrete-logarithm-in-p` · **Status:** open

## 1. Problem Statement / Conjecture

The Discrete Logarithm Problem (DLP) asks whether, for a given finite cyclic group $G$, a generator $g \in G$, and an element $h \in G$, one can compute the integer $x$ such that $g^x = h$ in deterministic or randomized polynomial time. In the language of complexity theory, the question is whether $\text{DLP} \in \text{P}$ (or $\text{BPP}$) when executed on a classical Turing machine.

Formally, the computational task is defined as: Given the tuple $(G, g, h, N)$, where $N = |G|$ is the order of the group, output an integer $x \in \{0, 1, \dots, N-1\}$ satisfying $g^x = h$ in time $O((\log N)^c)$ for some constant $c > 0$. 

The overarching conjecture—foundational to modern public-key cryptography—is that $\text{DLP} \notin \text{P}$ for general finite cyclic groups, and specifically for cryptographically significant groups such as the multiplicative group of large prime fields $\mathbb{F}_p^*$ and the group of rational points on carefully chosen elliptic curves over finite fields $E(\mathbb{F}_q)$. A complete proof of this conjecture would require demonstrating an unconditional super-polynomial lower bound for these groups, which would famously imply $\text{P} \neq \text{NP}$. Conversely, a disproof would require constructing a purely classical polynomial-time algorithm for the DLP in these structures.

## 2. Mathematical Foundations

Let $(G, \cdot)$ be a finite cyclic group of order $N$. Let $g$ be a generator of $G$, meaning that $G = \langle g \rangle = \{g^0, g^1, \dots, g^{N-1}\}$. The discrete logarithm function to the base $g$, denoted $\log_g : G \to \mathbb{Z}/N\mathbb{Z}$, is a group isomorphism defined by mapping $h \in G$ to the unique equivalence class $x \bmod N$ such that:
$$ g^x = \underbrace{g \cdot g \cdot \ldots \cdot g}_{x \text{ times}} = h $$

The group elements are represented using bit strings of length $n = \lceil \log_2 N \rceil$. The group operation (multiplication) and inversion are assumed to be computable in time polynomial in $n$. The forward operation, modular exponentiation $x \mapsto g^x$, can be computed in $O(n^3)$ operations (or faster) using the binary square-and-multiply algorithm. This asymmetry makes exponentiation a candidate one-way function.

In complexity theory, the decision version of the DLP is formulated as: Given $(G, g, h, N)$ and an integer $k \le N$, is the discrete logarithm $x \le k$? This decision problem lies in $\text{NP} \cap \text{co-NP}$ (assuming the prime factorization of $N$ is provided or can be found in $\text{NP} \cap \text{co-NP}$). It is in $\text{NP}$ because a proposed solution $x$ can be verified in polynomial time. It is in $\text{co-NP}$ because one can supply the prime factorization of $N$ and a primitive root to prove that $x$ is unique and greater than $k$. 

The complexity of DLP heavily depends on the underlying mathematical structure of $G$:
1.  **Multiplicative group of a finite field**: $G = \mathbb{F}_q^*$, where $q = p^k$ for a prime $p$.
2.  **Elliptic curve groups**: $G = E(\mathbb{F}_q)$, the group of points on an elliptic curve forming an abelian algebraic group under chord-and-tangent addition.

## 3. History & State of the Art (SOTA)

The computational difficulty of the DLP was brought to the forefront by Whitfield Diffie and Martin Hellman in their 1976 seminal paper introducing public-key cryptography. 

Historically, algorithms to solve DLP fall into two categories: generic algorithms and index calculus methods.
*   **Generic Algorithms:** In the 1970s, Daniel Shanks introduced the Baby-step Giant-step algorithm running in time $O(\sqrt{N})$ and space $O(\sqrt{N})$. John Pollard subsequently introduced Pollard's rho algorithm (1978), achieving the same time bound $O(\sqrt{N})$ but with $O(1)$ memory by utilizing pseudo-random walks and cycle-finding. 
*   **Index Calculus:** For $G = \mathbb{F}_p^*$, the index calculus method exploits the smoothness of integers over a "factor base." Discovered independently by several researchers in the 1970s, it provided subexponential algorithms. In 1993, Gordon and Schirokauer independently adapted the Number Field Sieve (NFS) to the DLP in $\mathbb{F}_p^*$, achieving a heuristic running time of:
    $$ L_p[1/3, c] = \exp\left(c (\log p)^{1/3} (\log \log p)^{2/3}\right) $$
    where $c \approx 1.923$.

In 1985, Neal Koblitz and Victor Miller independently suggested using the group of points on an elliptic curve (ECDLP), conjecturing that index calculus would fail due to the lack of a suitable smoothness concept, restricting attackers to $O(\sqrt{N})$ generic algorithms.

The most profound theoretical milestone occurred in 1994, when Peter Shor introduced a quantum algorithm that solves the DLP for any finite cyclic group in bounded-error quantum polynomial time ($\text{BQP}$), effectively proving that $\text{DLP} \in \text{BQP}$. Shor's algorithm heavily utilizes the Quantum Fourier Transform to solve the Abelian Hidden Subgroup Problem.

## 4. Partial Results / Verified Cases

While the general case remains open, the DLP has been proven to be in polynomial (or quasi-polynomial) time for several highly specific mathematical instances:

*   **Smooth Group Orders (Pohlig-Hellman):** If the prime factorization of $N$ is $N = \prod p_i^{e_i}$, the Pohlig-Hellman algorithm reduces the DLP in $G$ to the DLP in subgroups of order $p_i$. The complexity is $O(\sum e_i (\log p_i + \sqrt{p_i}))$. Consequently, if $N$ is "smooth" (its largest prime factor is bounded by a polynomial in $\log N$), the DLP is solvable in classical polynomial time.
*   **Anomalous Elliptic Curves:** For an elliptic curve $E$ over $\mathbb{F}_p$ such that the number of points is exactly $p$ (i.e., $|E(\mathbb{F}_p)| = p$), the ECDLP is in $\text{P}$. Smart, Semaev, and Satoh-Araki (1998) independently showed that the $p$-adic elliptic logarithm yields an explicitly computable group isomorphism from $E(\mathbb{F}_p)$ to the additive group $(\mathbb{F}_p, +)$, solving the problem in $O(\log^3 p)$ time.
*   **Small Characteristic Finite Fields:** The most dramatic recent breakthrough occurred for $\mathbb{F}_{q}^*$ where $q = p^k$ and the characteristic $p$ is small ($p = n^{O(1)}$). Following structural insights by Joux, Barbulescu et al. (2014) presented a heuristic algorithm solving the DLP in quasi-polynomial time:
    $$ \exp\left(O((\log \log q)^2)\right) $$
    This fundamentally breaks the $L[1/3]$ barrier for small-characteristic fields, pushing the problem tantalizingly close to $\text{P}$.

## 5. Principal Obstacles

The fundamental bottleneck preventing a universal polynomial-time algorithm is the theoretical constraint of the **Generic Group Model (GGM)**. Victor Shoup (1997) and Valeriy Nechaev (1994) unconditionally proved that any algorithm that treats the group operations as a "black box" (an oracle) must make at least $\Omega(\sqrt{N})$ oracle queries to find a discrete logarithm. Therefore, any polynomial-time algorithm must heavily exploit the specific mathematical representation of the group.

Exploiting this representation has proven notoriously difficult due to the following algebraic obstacles:
*   **Absence of Smoothness in Elliptic Curves:** Standard index calculus requires finding elements that factor cleanly into a small, restricted subset (the factor base). In $\mathbb{F}_p^*$, this is achieved by treating elements as integers. On an elliptic curve $E(\mathbb{F}_q)$, points do not "factor" into a combination of "smaller" points in any way that preserves the group operation over a manageable factor base. Summation polynomials (Semaev polynomials) exist, but they have exponentially growing degrees, rendering algebraic resolution intractable.
*   **The $L[1/3]$ Barrier in Large Characteristic:** For large prime fields $\mathbb{F}_p^*$, the Number Field Sieve relies on constructing two algebraic number fields that share a common root modulo $p$. To push the complexity below $L[1/3]$ (e.g., to $L[1/4]$ or polynomial time), one would need to select defining polynomials of varying, highly optimized degrees that generate sufficient smooth algebraic integers. Current analytic number theory dictates that the probability of an integer being smooth drops off too precipitously, creating an intrinsic mathematical boundary that standard sieve methods cannot cross.

## 6. The Gap

The exact boundary between what is known and the full resolution of the conjecture is defined by the gap between the structure of quantum logic and classical logic, as well as the gap between finite field representations.

First, there is a representation gap. We possess quasi-polynomial algorithms for $\mathbb{F}_{p^k}^*$ when $p$ is small, leveraging the Frobenius automorphism. However, for large prime fields $\mathbb{F}_p^*$, the best classical time remains subexponential. Bridging this requires discovering an entirely new algebraic mechanism in large characteristic fields that mimics the descent procedures used in small characteristics.

Second, there is a complexity-theoretic gap. We know $\text{DLP} \in \text{BQP}$, proving that deep structural invariants exist and can be computed via quantum phase estimation. The classical barrier is extracting the periodicity of the function $f(a,b) = g^a h^{-b}$ without utilizing quantum superposition. Resolving the conjecture entails either finding a classical analogue to the Fourier transform capable of isolating this hidden subgroup efficiently, or proving that classical Turing machines strictly lack the capacity to extract such periodic structures algebraically—which would separate $\text{P}$ from $\text{BQP}$.

## 7. Current Research (as of June 2026)

Research into the DLP is split between aggressive algorithmic improvements (cryptanalysis) and deep structural geometry:
*   **Advanced Number Field Sieves:** Groups are focusing on the Multiple Number Field Sieve (MNFS) and the Tower Number Field Sieve (TNFS) for medium characteristic fields. Recent algorithmic refinements focus on polynomial selection and matrix-solving techniques (Block Wiedemann) deployed on massive supercomputing clusters.
*   **Isogeny-based Reductions:** * (frontier — verify)* Active research is investigating whether the graph of isogenies between elliptic curves can be used to construct a classical subexponential index calculus for general ECDLP by traversing the isogeny graph to map points onto highly specific, vulnerable curves.
*   **Exact Quantum Complexity:** With the advent of noisy intermediate-scale quantum (NISQ) devices, theorists are optimizing the exact T-gate counts and qubit requirements for Shor's algorithm, calculating the precise physical threshold at which 256-bit ECDLP will be broken in practice.

## 8. Future Work

Leading mathematicians and cryptographers highlight several open pathways:
1.  **Subexponential ECDLP:** The holy grail of classical cryptanalysis is discovering a classical algorithm for general elliptic curves that runs in time $L_N[\alpha, c]$ for some $\alpha < 1$. This would likely involve radical new insights into the arithmetic geometry of abelian varieties.
2.  **Rigorous Quasi-Polynomial Time:** The Barbulescu et al. algorithm for small characteristic fields relies on unproven heuristics regarding the existence of irreducible polynomials and smoothness probabilities. Providing a fully rigorous proof of this quasi-polynomial time bound remains a high-priority problem in computational number theory.
3.  **Conditional Lower Bounds:** In the absence of an unconditional $\text{P} \neq \text{NP}$ proof, theorists aim to reduce other standard hard problems (like finding shortest vectors in ideal lattices) directly to the DLP in $\mathbb{F}_p^*$ to establish stronger conditional lower bounds outside the generic group model.

## 9. Key References

- **[Foundational]** Diffie, W., & Hellman, M. E. *New directions in cryptography.* IEEE Transactions on Information Theory, 1976.
- **[Foundational]** Shoup, V. *Lower bounds for discrete logarithms and related problems.* EUROCRYPT 1997.
- **[Foundational]** Shor, P. W. *Polynomial-time algorithms for prime factorization and discrete logarithms on a quantum computer.* SIAM Journal on Computing, 1997.
- **[SOTA / Recent]** Barbulescu, R., Gaudry, P., Joux, A., & Thomé, E. *A heuristic quasi-polynomial algorithm for discrete logarithm in finite fields of small characteristic.* Advances in Cryptology – EUROCRYPT 2014.
- **[SOTA / Recent]** Boudot, F., Gaudry, P., Guillevic, A., Heninger, N., Thomé, E., & Zimmermann, P. *Comparing the difficulty of factorization and discrete logarithm: a 240-digit experiment.* Annual International Cryptology Conference (CRYPTO), 2020.
- **[Survey]** Joux, A., Odlyzko, A., & Pierrot, C. *The past, evolving present, and future of the discrete logarithm.* Open Problems in Mathematics and Computational Science, Springer, 2014.
- **[Survey]** Galbraith, S. D., & Gaudry, P. *Recent progress on the elliptic curve discrete logarithm problem.* Designs, Codes and Cryptography, 2016.

## 10. Worked Example / Concrete Special Case

To ground the problem, consider a small, concrete instance of the DLP in a finite field solved via Shanks' Baby-step Giant-step algorithm, which achieves the optimal generic group complexity of $O(\sqrt{N})$.

Let the group be $G = \mathbb{F}_{11}^*$ under multiplication modulo $11$. The order of the group is $N = 10$. 
Let the generator be $g = 2$. We wish to find $x$ such that:
$$ 2^x \equiv 7 \pmod{11} $$

**Step 1: Setup parameters.**
Let $m = \lceil \sqrt{N} \rceil = \lceil \sqrt{10} \rceil = 4$.
We write $x$ in the form $x = i \cdot m + j$, where $0 \le j < m$ and $0 \le i < m$.
Therefore, $2^{im+j} \equiv 7 \pmod{11}$, which implies:
$$ 2^j \equiv 7 \cdot (2^{-m})^i \pmod{11} $$

**Step 2: Baby Steps (Compute $2^j \pmod{11}$).**
We compute a table of $2^j \pmod{11}$ for $j \in \{0, 1, 2, 3\}$:
*   $j = 0 \implies 2^0 = 1$
*   $j = 1 \implies 2^1 = 2$
*   $j = 2 \implies 2^2 = 4$
*   $j = 3 \implies 2^3 = 8$

**Step 3: Giant Steps (Compute $7 \cdot (2^{-4})^i \pmod{11}$).**
First, we find $2^{-4} \pmod{11}$. 
$2^4 = 16 \equiv 5 \pmod{11}$. 
The modular inverse of $5$ modulo $11$ is $9$ (since $5 \times 9 = 45 \equiv 1 \pmod{11}$). Thus, $2^{-4} \equiv 9 \pmod{11}$.

Now we evaluate the right-hand side, $7 \cdot 9^i \pmod{11}$, for $i \in \{0, 1, 2, 3\}$ until we find a match in our Baby Step table:
*   $i = 0 \implies 7 \cdot 9^0 \equiv 7 \pmod{11}$. (Not in table)
*   $i = 1 \implies 7 \cdot 9^1 = 63 \equiv 8 \pmod{11}$. 

**Step 4: Resolve.**
We have found a collision: $8$ is in the Baby Step table at $j = 3$, and in the Giant Step sequence at $i = 1$.
Equating them:
$$ 2^3 \equiv 7 \cdot 9^1 \equiv 7 \cdot (2^{-4})^1 \pmod{11} $$
Multiplying both sides by $2^4$ gives:
$$ 2^3 \cdot 2^4 \equiv 7 \pmod{11} \implies 2^7 \equiv 7 \pmod{11} $$
Thus, the discrete logarithm is $x = 7$. 

Verification: $2^7 = 128$. And $128 = 11 \times 11 + 7$, so $128 \equiv 7 \pmod{11}$. The result is correct. This deterministic $O(\sqrt{N})$ approach represents the best known generic method, scaling exponentially as bit sizes reach modern cryptographic lengths.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*