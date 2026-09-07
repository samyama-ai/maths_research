---
id: 10-theoretical-cs/fast-fourier-transform-lower-bound
title: "Fast Fourier Transform Lower Bound"
topic: 10-theoretical-cs
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Fast Fourier Transform Lower Bound

> **Topic:** Theoretical Computer Science · **ID:** `10-theoretical-cs/fast-fourier-transform-lower-bound` · **Status:** open

## 1. Problem Statement / Conjecture

The Fast Fourier Transform (FFT) lower bound problem is one of the most prominent open questions in theoretical computer science and algebraic complexity theory. The problem asks for the optimal asymptotic number of arithmetic operations required to compute the Discrete Fourier Transform (DFT) of an $N$-dimensional vector.

Specifically, given an input vector $x \in \mathbb{C}^N$, the unnormalized DFT is the linear transformation $y = F_N x$, where $F_N \in \mathbb{C}^{N \times N}$ is the Fourier matrix. The Cooley-Tukey algorithm establishes that $x \mapsto F_N x$ can be computed using $O(N \log N)$ operations in the arithmetic circuit model. The fundamental open question is whether this $O(N \log N)$ upper bound is tight.

**The Conjecture:** Any linear straight-line program (or linear arithmetic circuit) with arbitrary constants from $\mathbb{C}$ that computes the map $x \mapsto F_N x$ requires $\Omega(N \log N)$ arithmetic operations. 

In other words, it is conjectured that the algebraic complexity $L(F_N)$ scales as $\Theta(N \log N)$. Currently, the best known unconditional lower bound for general, unrestricted linear circuits over $\mathbb{C}$ computing the DFT is merely the trivial $\Omega(N)$, established by simple dimension-counting arguments. Proving a super-linear lower bound for this explicit, universally applied linear transformation remains entirely open.

## 2. Mathematical Foundations

Let $\mathbb{C}$ be the field of complex numbers. The Discrete Fourier Transform of order $N$ is the linear map defined by the symmetric matrix $F_N \in \mathbb{C}^{N \times N}$, where the entry in the $j$-th row and $k$-th column is given by:

$$ (F_N)_{j,k} = \omega_N^{j k} $$

for $0 \le j, k \le N-1$, where $\omega_N = \exp(-2\pi i / N)$ is a primitive $N$-th root of unity.

The computational model is the Linear Straight-Line Program (LSLP) over $\mathbb{C}$. An LSLP computing the map $F_N: \mathbb{C}^N \to \mathbb{C}^N$ is a sequence of variables (or nodes in a directed acyclic graph) $v_1, v_2, \dots, v_S$ such that:
1. $v_k = x_{k-1}$ for $1 \le k \le N$ (the input variables).
2. For $k > N$, each node computes a linear combination of previously computed nodes: 
   $$ v_k = \alpha_k v_a + \beta_k v_b $$ 
   where $a, b < k$ and the scalar constants $\alpha_k, \beta_k \in \mathbb{C}$.
3. There exists a subset of indices $i_1, \dots, i_N$ such that $v_{i_m} = y_{m-1}$ for all $1 \le m \le N$, where $y = F_N x$.

The algebraic complexity, or size, of the LSLP is the number of internal computation nodes, $S - N$. This exactly corresponds to the number of binary algebraic operations (additions, subtractions, and scalar multiplications) performed. The linear complexity $L(F_N)$ is defined as the minimum size over all valid LSLPs computing $F_N$.

A critical foundational result in this model is **Morgenstern’s Theorem (1973)**. It states that if we restrict the LSLP such that all scalar constants are bounded by some real number $c > 1$ (i.e., $|\alpha_k| + |\beta_k| \le c$ for all $k$), then the required number of operations $L_c$ is bounded from below by the determinant of the transformation:

$$ L_c(F_N) \ge \log_c |\det(F_N)| $$

Because $|\det(F_N)| = N^{N/2}$, Morgenstern's bounded-coefficient model successfully yields the conjectured lower bound: $L_c(F_N) = \Omega(N \log N)$. The central problem is generalizing this to circuits where the constants $\alpha_k, \beta_k$ are unbounded.

## 3. History & State of the Art (SOTA)

The history of the DFT's complexity is deeply intertwined with the development of modern computing. While Carl Friedrich Gauss independently discovered an $O(N \log N)$ technique in 1805, the upper bound was broadly popularized by James Cooley and John Tukey in 1965. Their divide-and-conquer algorithm fundamentally shaped digital signal processing.

Following the establishment of the $O(N \log N)$ upper bound, theoreticians sought to prove its optimality. In 1973, Morgenstern proved his seminal $\Omega(N \log N)$ lower bound for circuits with bounded coefficients. However, efforts to extend this to general LSLPs immediately hit a wall. In 1977, Leslie Valiant introduced the concept of **Matrix Rigidity** as a structural approach to prove super-linear lower bounds for linear circuits of logarithmic depth (which includes the FFT graph). Valiant hoped that proving the Fourier matrix was highly rigid would immediately yield the desired $\Omega(N \log N)$ bounds. 

Despite decades of effort by the theoretical computer science community, proving sufficient matrix rigidity for explicit matrices like $F_N$ has remained intractable. In a major shock to the field, Alman and Williams (2017) proved that the Walsh-Hadamard matrix (a close cousin of the Fourier matrix over $\mathbb{F}_2$) is actually *not* highly rigid, casting deep suspicion on the viability of the rigidity approach for proving the FFT lower bound. 

As of the current state of the art, the best unconditional lower bound for computing the DFT with unrestricted linear circuits remains $O(N)$. Specifically, simple fan-in/fan-out dimension counting guarantees a lower bound of slightly less than $3N$ operations. The $\Omega(N \log N)$ barrier has not been breached for general LSLPs.

## 4. Partial Results / Verified Cases

While the general conjecture remains open, the $\Omega(N \log N)$ lower bound has been verified in several restricted models of computation:

1. **Bounded Constants:** As previously noted, Morgenstern proved the conjecture for circuits where the absolute sum of scalar multipliers in any single addition is bounded by a constant $c$. The Cooley-Tukey algorithm naturally satisfies this bound (typically with $c=2$), proving that Cooley-Tukey is structurally optimal among all bounded-coefficient algorithms.
2. **Boolean Circuit Model (Finite Fields):** When computing the Number Theoretic Transform (the DFT over a finite field $\mathbb{F}_q$) using standard Boolean gates (AND, OR, NOT) instead of arithmetic nodes, achieving an $\Omega(N \log N)$ bound is trivial because simply writing the output requires $\Omega(N \log q)$ wire complexity. However, bounding the *algebraic* steps remains stuck at $\Omega(N)$.
3. **Multiplicative Complexity:** A celebrated result by Shmuel Winograd (1978) proved that the exact number of non-rational multiplications required to compute $F_N$ for prime $N$ is precisely $2N - O(1)$. This isolates the bottleneck: the $\Omega(N \log N)$ asymptotic complexity of the FFT is entirely derived from the structural additions (linear combinations), not from the multiplication gates. 
4. **Sparse Outputs:** If the output vector $y = F_N x$ is known a priori to be $k$-sparse (having at most $k$ non-zero frequencies), algorithms developed by Hassanieh, Indyk, Katabi, and Price (2012) can compute the Sparse FFT in $O(k \log N)$ or $O(k \log(N/k))$ operations. This proves that any general lower bound must depend heavily on the density of the output manifold.

## 5. Principal Obstacles

The primary barrier to resolving the FFT lower bound is the phenomenon of **large scalar cancellations** in unbounded arithmetic circuits. 

In linear algebra, invariants like volume and the determinant are strictly tied to scalar multiplication. If an LSLP is allowed to use arbitrarily large constants (e.g., multiplying intermediate nodes by $10^{100}$ and later dividing by $10^{100}$), it can artificially inflate intermediate determinants or compress geometric spaces in ways that bypass traditional topological lower bounds. Morgenstern’s proof exploits the determinant, but the determinant is homogeneous of degree $N$: $\det(\lambda A) = \lambda^N \det(A)$. A circuit can trivially scale its computation by a massive $\lambda$ to satisfy the determinant inequality without performing any extra structural additions.

Furthermore, traditional algebraic complexity measures—such as the Baur-Strassen theorem, Betti numbers, or degree bounds from algebraic geometry—are designed for *non-linear* polynomials. Because the DFT simply computes a set of linear forms (polynomials of degree 1), their geometric degree is trivial, rendering these heavy-duty algebraic techniques entirely useless.

Finally, the **Matrix Rigidity** obstacle is severe. A matrix $A$ is $(r, d)$-rigid if one cannot reduce its rank to $r$ by altering at most $d$ entries in each row. Valiant proved that depth-$O(\log N)$ linear circuits require super-linear size if the target matrix is $(O(N/\log \log N), O(N^\epsilon))$-rigid. The parameter space of low-rank matrices is highly non-convex, making evasion sets difficult to construct. The Alman-Williams result suggests that Fourier-like matrices might inherently possess hidden, non-intuitive low-rank approximations via polynomial factorizations, meaning $F_N$ might completely evade the rigidity property altogether.

## 6. The Gap

The mathematical gap lies between the known $\Omega(N \log N)$ complexity for bounded circuits and the $\Omega(N)$ complexity for unbounded circuits. 

To cross this gap, complexity theorists must discover a novel algebraic invariant measure, $\mu: \mathbb{C}^{N \times N} \to \mathbb{R}$, that satisfies four strict properties:
1. **Subadditivity under graph composition:** $\mu(A B) \le \mu(A) + \mu(B)$.
2. **Lower bounded on the Fourier matrix:** $\mu(F_N) = \Omega(N \log N)$.
3. **Upper bounded by base operations:** For any elementary arithmetic operation matrix $E$, $\mu(E) \le O(1)$.
4. **Scale Invariance:** $\mu(\lambda A) \approx \mu(A)$ for any arbitrary scalar $\lambda \in \mathbb{C}$.

Morgenstern’s $\mu(A) = \log |\det A|$ elegantly satisfies the first three properties but fatally fails the fourth. Bridging this gap requires defining a robust information-theoretic or graph-theoretic invariant that measures the "entanglement" or necessary data-routing topology of a matrix, independent of scalar magnitudes.

## 7. Current Research (as of June 2026)

Active research on the FFT lower bound is generally split into two distinct methodologies:

- **Fine-Grained Matrix Rigidity:** Researchers at IAS and MIT continue to probe the exact rigidity parameters of $F_N$ over $\mathbb{C}$. While the Walsh-Hadamard matrix was shown to be non-rigid, the continuous nature of roots of unity in $\mathbb{C}$ (unlike the $\pm 1$ limits of Walsh-Hadamard) leaves a narrow window where $F_N$ might still possess the necessary rigidity to trigger Valiant's bound.
- **Depth-Restricted Lower Bounds:** A secondary track focuses on proving super-linear lower bounds for highly restricted depth-3 or depth-4 linear circuits over $\mathbb{C}$. By utilizing shifting techniques and partial derivatives on restricted linear graphs, researchers aim to incrementally build up to the $O(\log N)$ depth of the FFT.
- *(frontier — verify)* Recent preprints leveraging fast multipole methods and Chebyshev polynomial approximations suggest that $F_N$ over $\mathbb{C}$ can indeed be approximated by highly sparse, low-rank factorizations, implying that $F_N$ is definitively non-rigid. If verified, this would force the complete abandonment of the Valiant rigidity program for the DFT, requiring entirely new lower-bound architectures.

## 8. Future Work

Leading mathematicians and complexity theorists suggest several open pathways:

- **Information Flow in Linear DAGs:** Developing a theory of "linear network coding" complexity that can track the forced routing of linearly independent variables through a bottleneck, completely disregarding the scalar values attached to the edges.
- **Geometric Complexity Theory (GCT):** While GCT is traditionally applied to the Permanent vs. Determinant problem via tensor rank, finding an analogous representation-theoretic approach for linear circuit size (which corresponds to highly restricted matrix factorizations) remains a compelling, albeit highly abstract, frontier.
- **Unbounded Depth:** Even if rigidity succeeds, it only applies to circuits of depth $O(\log N)$. Finding techniques that apply to linear circuits of arbitrary depth $O(N)$ is an ultimate, long-term requirement for fully resolving the conjecture.

## 9. Key References

- **[Foundational]** Cooley, J. W., & Tukey, J. W. *An algorithm for the machine calculation of complex Fourier series.* Mathematics of Computation, 1965.
- **[Foundational]** Morgenstern, J. *Note on a lower bound of the linear complexity of the fast Fourier transform.* Journal of the ACM (JACM), 1973.
- **[Foundational]** Valiant, L. G. *Graph-Theoretic Arguments in Low-Level Complexity.* Mathematical Foundations of Computer Science (MFCS), 1977.
- **[Foundational]** Winograd, S. *On computing the discrete Fourier transform.* Mathematics of Computation, 1978.
- **[SOTA / Recent]** Alman, J., & Williams, R. *Probabilistic Polynomials and Hamming Weight Queries.* 58th IEEE Annual Symposium on Foundations of Computer Science (FOCS), 2017.
- **[Survey]** Lokam, S. V. *Complexity Lower Bounds using Linear Algebra.* Foundations and Trends in Theoretical Computer Science, 2009.
- **[Survey]** Bürgisser, P., Clausen, M., & Shokrollahi, M. A. *Algebraic Complexity Theory.* Springer, 1997.

## 10. Worked Example / Concrete Special Case

To ground the abstract lower bound, consider the computation of the DFT for a small vector $x \in \mathbb{C}^4$, where $N=4$. The primitive 4th root of unity is $\omega_4 = \exp(-2\pi i / 4) = -i$.

The Fourier matrix $F_4$ is explicitly constructed as:
$$ 
F_4 = \begin{pmatrix}
1 & 1 & 1 & 1 \\
1 & -i & -1 & i \\
1 & -1 & 1 & -1 \\
1 & i & -1 & -i
\end{pmatrix}
$$

We can apply Morgenstern's bounded-coefficient theorem to find the minimum number of operations $L$ required to compute $y = F_4 x$. Assume an LSLP where every binary operation $v_k = \alpha v_a + \beta v_b$ strictly satisfies $|\alpha| + |\beta| \le 2$. Let $c=2$.

First, we calculate the determinant of $F_4$. Because the columns of the unnormalized DFT matrix are orthogonal and each column has a squared norm of $N=4$, we have:
$$ F_4 F_4^* = 4 I_4 $$
where $I_4$ is the identity matrix and $F_4^*$ is the conjugate transpose. Taking the determinant of both sides:
$$ \det(F_4) \det(F_4^*) = \det(4 I_4) = 4^4 = 256 $$
Since $|\det(F_4)| = |\det(F_4^*)|$, we find $|\det(F_4)|^2 = 256$, which gives $|\det(F_4)| = 16$.

Applying Morgenstern’s bound:
$$ L_2(F_4) \ge \log_2(16) = 4 $$

Thus, any bounded arithmetic circuit requires at least $4$ operations to compute $F_4 x$. 

In practice, the Cooley-Tukey Radix-2 Decimation-in-Time algorithm computes $F_4 x$ in exactly $\frac{N}{2} \log_2 N$ butterfly stages. For $N=4$, this results in $2$ butterfly stages, each containing $2$ butterfly operations. A standard butterfly operation $(a, b) \mapsto (a+Wb, a-Wb)$ executes $2$ additions/subtractions (which are combinations bounded by $1+1=2 \le c$). 

Thus, the Cooley-Tukey algorithm computes $F_4 x$ utilizing exactly $4 \log_2 4 = 8$ structural additions. This demonstrates that for bounded coefficients, the algorithmic upper bound of $8$ operations is tightly constrained by the theoretical information-theoretic lower bound of $4$, separated only by a small constant factor.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*