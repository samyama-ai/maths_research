---
id: 10-theoretical-cs/fourier-entropy-influence
title: "Fourier Entropy Influence"
topic: 10-theoretical-cs
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Fourier Entropy-Influence Conjecture

> **Topic:** Theoretical Computer Science · **ID:** `10-theoretical-cs/fourier-entropy-influence` · **Status:** open

## 1. Problem Statement / Conjecture

The Fourier Entropy-Influence (FEI) conjecture posits a fundamental structural limitation on the Fourier spectrum of Boolean functions. It states that for any Boolean function, the Shannon entropy of its Fourier power spectrum is bounded from above by a universal constant multiplied by its total influence.

Formally, the conjecture asserts that there exists an absolute universal constant $C > 0$ such that for any integer $n \ge 1$ and any Boolean function $f: \{-1, 1\}^n \to \{-1, 1\}$, the following inequality holds:
$$H(f) \le C \cdot I(f)$$
where $H(f)$ is the spectral entropy of $f$ and $I(f)$ is the total influence of $f$.

A complete proof of the conjecture requires demonstrating that this linear bound holds over all Boolean functions without the constant $C$ depending on the dimension $n$ or any other parameter of the function. Conversely, a disproof would necessitate constructing a family of Boolean functions $\{f_n\}$ for which the ratio $H(f_n) / I(f_n)$ diverges to infinity as $n \to \infty$.

## 2. Mathematical Foundations

The problem is embedded in the harmonic analysis of Boolean functions defined over the hypercube. We model the space of functions as $V = \{f: \{-1, 1\}^n \to \mathbb{R}\}$, equipped with the uniform probability measure over $\{-1, 1\}^n$. The inner product for two functions $f, g$ is defined as:
$$\langle f, g \rangle = \mathbb{E}_{x \sim \{-1, 1\}^n} [f(x)g(x)]$$

The characters of this space are the parity functions over subsets $S \subseteq [n] = \{1, 2, \dots, n\}$:
$$\chi_S(x) = \prod_{i \in S} x_i$$
These form an orthonormal basis, implying any $f$ can be uniquely expressed by its Fourier expansion:
$$f(x) = \sum_{S \subseteq [n]} \hat{f}(S) \chi_S(x)$$
where $\hat{f}(S) = \langle f, \chi_S \rangle$. By Parseval's theorem, for a Boolean function taking values in $\{-1, 1\}$, we have:
$$\sum_{S \subseteq [n]} \hat{f}(S)^2 = \mathbb{E}[f^2] = 1$$
Thus, the squared Fourier coefficients $\{\hat{f}(S)^2\}_{S \subseteq [n]}$ form a valid probability distribution over the subsets of $[n]$.

**Spectral Entropy:** The Shannon entropy of this Fourier distribution is:
$$H(f) = \sum_{S \subseteq [n]} \hat{f}(S)^2 \log_2 \left(\frac{1}{\hat{f}(S)^2}\right)$$
with the standard convention that $0 \log_2(1/0) = 0$.

**Influence:** The influence of the $i$-th coordinate on $f$ is the probability that flipping the $i$-th bit flips the output of the function. Via the Fourier expansion, it can be written as:
$$I_i(f) = \sum_{S \subseteq [n], \, i \in S} \hat{f}(S)^2$$
The total influence $I(f)$ is the sum of individual influences, which simplifies to the expected size of a subset drawn from the Fourier distribution:
$$I(f) = \sum_{i=1}^n I_i(f) = \sum_{S \subseteq [n]} |S| \hat{f}(S)^2$$

Therefore, the FEI conjecture claims that the Shannon entropy of the Fourier distribution is bounded by its mean subset size up to a multiplicative constant.

## 3. History & State of the Art (SOTA)

The FEI conjecture was formally proposed by Ehud Friedgut and Gil Kalai in their seminal 1996 paper, "Every monotone graph property has a sharp threshold." It emerged from the study of sharp thresholds in random graphs, specifically building on the KKL (Kahn-Kalai-Linial, 1988) theorem, which utilized Bonami-Beckner hypercontractivity to analyze the influence of Boolean variables.

Historically, the FEI conjecture rapidly gained prominence due to its profound implications for computational learning theory. In 1994, Yishay Mansour conjectured that any Boolean function computable by a polynomial-size Disjunctive Normal Form (DNF) formula has its Fourier mass highly concentrated on a polynomial number of coefficients. A positive resolution to the FEI conjecture would directly imply Mansour's conjecture, thereby demonstrating that poly-size DNF formulas can be efficiently PAC-learned under the uniform distribution in polynomial time via the Low-Degree Algorithm.

While the general bound $H(f) \le C \cdot I(f)$ remains unresolved, the state of the art has progressed by establishing alternative upper bounds. Recent results demonstrate that Fourier entropy can be bounded by the sum of individual influences with logarithmic penalties:
$$H(f) \le O\left(I(f) + \sum_{k=1}^n I_k(f) \log \left(\frac{1}{I_k(f)}\right)\right)$$
Additionally, active computational search efforts have pushed the lower bound for the universal constant to $C \ge 6.5218$ for $n=18$ variables, disproving early hypotheses that $C$ might be smaller than 5.

## 4. Partial Results / Verified Cases

Although the general FEI conjecture is open, it has been rigorously verified for several important, highly structured classes of Boolean functions:

- **Symmetric Functions:** Proven by O'Donnell, Wright, and Zhao (2011). A Boolean function is symmetric if its output depends only on the Hamming weight of the input.
- **Read-Once Decision Trees:** O'Donnell and Wright (2012) proved the conjecture for read-$k$ decision trees, with the bounding constant $C$ scaling as a function of $k$.
- **Random Functions:** The conjecture holds with high probability for random Boolean functions, where the total influence is large ($\sim n/2$) and the entropy is tightly concentrated near $n$.
- **Random Linear Threshold Functions (LTFs):** Klivans et al. and subsequent authors verified the conjecture for random LTFs.
- **Functions with Bounded Depth/Sparsity:** The conjecture is known to hold when $f$ can be represented as a bounded-depth circuit ($AC^0$) or has a highly sparse Fourier spectrum.

## 5. Principal Obstacles

The primary bottleneck in resolving the FEI conjecture is the inability of classical hypercontractivity to finely control the "tail" of the Fourier spectrum. 

Standard techniques, such as the Bonami-Beckner inequality (or the logarithmic Sobolev inequality on the Boolean cube), are exceptional at bounding the $L_p$ norms (e.g., $L_4$) of the Fourier transform. Bounding $\sum \hat{f}(S)^4$ effectively controls the collision probability of the Fourier distribution (Rényi entropy of order 2). However, transitioning from Rényi entropy bounds to Shannon entropy is highly non-trivial because Shannon entropy is exceptionally sensitive to a long, flat tail of exponentially many extremely small, non-zero Fourier coefficients. 

To prove FEI, one must demonstrate that if a function has small total influence (meaning the Fourier mass is largely concentrated on small sets), it cannot simultaneously spread its remaining probability mass over so many subsets that the Shannon entropy becomes abnormally large. Current mathematical techniques lack a structural theorem that precludes this pathological distribution of "Fourier dust."

## 6. The Gap

The precise boundary distinguishing solved and unsolved instances lies between heavily structured functions and arbitrary Boolean mappings.

1. **What is Proven:** For structured classes (symmetric functions, decision trees, read-once formulas), mathematicians can explicitly map their combinatorial constraints directly to constraints on their Fourier coefficients. Furthermore, upper bounds are known in terms of other, larger complexity measures: $H(f) \le O(C(f))$, where $C(f)$ is the unambiguous certificate complexity or decision tree depth.
2. **What is Required:** To cross the gap, we must bound $H(f)$ unconditionally using *only* $I(f)$. The mathematical barrier lies in eliminating the $\log(1/I_k(f))$ penalties in current best-known upper bounds, or proving a "Min-Entropy / Shannon Entropy" equivalence for Fourier spectra that works globally across the Boolean cube without structural assumptions.

## 7. Current Research (as of June 2026)

Active research on the FEI conjecture currently bifurcates into two main tracks:

- **Structural Upper Bounds:** Leading groups at Carnegie Mellon University and the Weizmann Institute are exploring the Fractional FEI conjecture and Min-FEI variants. Recent preprints have focused on bounding $H(f)$ using the polynomial approximate degree or quantum query complexity as intermediaries. There is also active work connecting the conjecture to modified log-Sobolev inequalities on specialized random walks over the hypercube.
- **Computational Lower Bounds *(frontier — verify)*:** Projects like *Numaro* use heavy distributed computing to search the space of Boolean functions for counterexamples or to strictly push the minimal constant $C$ upward. By exhaustively evaluating specific sub-classes up to $n=18$, the lowest known valid upper bound for $C$ has been raised to approximately 6.5218, achieved by highly asymmetric functions.

## 8. Future Work

Leading mathematicians suggest several stepping stones toward a full resolution:
1. **Resolve Mansour's Conjecture Directly:** Prove that poly-size DNF formulas have concentrated Fourier mass without relying on FEI. This might provide new analytical tools for bounding Fourier tails that could translate back to the general FEI problem.
2. **Polynomial Threshold Functions (PTFs):** Prove the FEI conjecture for PTFs of degree $d \ge 2$. While random LTFs (degree 1) are verified, arbitrary LTFs and low-degree PTFs remain a formidable open challenge that bridges structure and randomness.
3. **Improved Intermediary Bounds:** Establish an unconditional upper bound of $H(f) \le O(I(f) \log I(f))$. While weaker than the true conjecture, this would represent a massive theoretical breakthrough in bounding Shannon entropy solely as a function of total influence, independent of $n$.

## 9. Key References

- **[Foundational]** Friedgut, E., and Kalai, G. *Every monotone graph property has a sharp threshold.* Proceedings of the American Mathematical Society, 1996. (Introduces the FEI conjecture).
- **[Foundational]** Mansour, Y. *Learning Boolean functions via the Fourier transform.* Theoretical Computer Science, 1994.
- **[SOTA / Recent]** O'Donnell, R., Wright, J., and Zhao, C. *The Fourier Entropy-Influence Conjecture for certain classes of Boolean functions.* ICALP, 2011.
- **[SOTA / Recent]** Keller, N., Mossel, E., and Sen, A. *Geometric influences.* Annals of Probability, 2012.
- **[Survey]** O'Donnell, R. *Analysis of Boolean Functions.* Cambridge University Press, 2014. (Comprehensive textbook containing dedicated discussion on FEI and partial results).

## 10. Worked Example / Concrete Special Case

To ground the conjecture in a tangible example, consider the classical logical **AND function** on two variables, mapped to the $\{-1, 1\}$ basis.
Define $f: \{-1, 1\}^2 \to \{-1, 1\}$, where $-1$ represents `True` and $1$ represents `False`. The AND function outputs `True` (-1) only if both inputs are `True` (-1, -1). Its algebraic representation is given by:
$$f(x_1, x_2) = \frac{1 + x_1 + x_2 - x_1 x_2}{2}$$

**Fourier Coefficients:**
We can extract the coefficients $\hat{f}(S)$ directly from the polynomial expansion:
- $\hat{f}(\emptyset) = 1/2$
- $\hat{f}(\{1\}) = 1/2$
- $\hat{f}(\{2\}) = 1/2$
- $\hat{f}(\{1, 2\}) = -1/2$

*Check Parseval's identity:*
$$(1/2)^2 + (1/2)^2 + (1/2)^2 + (-1/2)^2 = 1/4 + 1/4 + 1/4 + 1/4 = 1$$
The Fourier distribution is perfectly uniform over all 4 subsets, each occurring with probability $1/4$.

**Total Influence:**
$$I(f) = \sum_{S} |S| \hat{f}(S)^2 = 0 \cdot \left(\frac{1}{4}\right) + 1 \cdot \left(\frac{1}{4}\right) + 1 \cdot \left(\frac{1}{4}\right) + 2 \cdot \left(\frac{1}{4}\right) = 1$$

**Spectral Entropy:**
$$H(f) = \sum_{S} \hat{f}(S)^2 \log_2 \left(\frac{1}{\hat{f}(S)^2}\right) = 4 \times \left( \frac{1}{4} \log_2(4) \right) = 4 \times \left( \frac{2}{4} \right) = 2$$

**The FEI Bound:**
We compare the entropy to the total influence to establish a lower limit on $C$ for this function:
$$H(f) \le C \cdot I(f) \implies 2 \le C \cdot 1 \implies C \ge 2$$
For this specific function, the inequality holds easily for any constant $C \ge 2$. Current computational lower bounds (e.g., $C \ge 6.5218$) far exceed this local requirement, illustrating that the global maximum of the ratio $H(f) / I(f)$ across the hypercube occurs in much larger dimensions with highly asymmetric functions that pack influence inefficiently relative to their entropy.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*