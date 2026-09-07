---
id: 01-number-theory/pillais-conjecture
title: "Pillai's Conjecture"
topic: 01-number-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Pillai's Conjecture

> **Topic:** Number Theory · **ID:** `01-number-theory/pillais-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Pillai's Conjecture posits that in the sequence of perfect powers of integers, the gap between consecutive terms tends to infinity.

Formally, for any given positive integer $c$, the exponential Diophantine equation
$$A^x - B^y = c$$
has only finitely many solutions in positive integers $A, B, x, y$ where $x \ge 2$ and $y \ge 2$.

An equivalent formulation states that if $P = \{1, 4, 8, 9, 16, 25, 27, 32, \dots\}$ denotes the set of perfect powers (integers of the form $a^b$ with $a \ge 1, b \ge 2$) and $p_n$ is the $n$-th term of this sequence in strictly increasing order, then:
$$\lim_{n \to \infty} (p_{n+1} - p_n) = \infty$$

A complete proof of the conjecture would demonstrate that every integer gap $c$ occurs at most a finite number of times, establishing a fundamental property about the asymptotic distribution of perfect powers.

## 2. Mathematical Foundations

Let $\mathbb{Z}^+$ denote the set of positive integers. We define the set of perfect powers $S$ as:
$$S = \{ x^m \in \mathbb{Z}^+ \mid x \ge 2, m \ge 2 \}$$

Let $\{s_n\}_{n=1}^{\infty}$ be the sequence of elements of $S$ ordered such that $s_1 < s_2 < s_3 < \dots$. Pillai's conjecture claims that for any constant $C > 0$, there exists an index $N$ such that for all $n > N$:
$$s_{n+1} - s_n > C$$
which is mathematically equivalent to stating that:
$$\liminf_{n \to \infty} (s_{n+1} - s_n) = \infty$$

The problem is intimately tied to Diophantine approximation, heights on algebraic varieties, and Baker's theory of linear forms in logarithms. For an algebraic number $\alpha$, its logarithmic height $h(\alpha)$ is a measure of its arithmetic complexity. The fundamental inequality from Baker's theory states that for non-zero algebraic numbers $\alpha_1, \dots, \alpha_k$ and integers $b_1, \dots, b_k$, the linear form $\Lambda = b_1 \log \alpha_1 + \dots + b_k \log \alpha_k$, if non-zero, is bounded away from zero:
$$|\Lambda| > \exp(-C \max_i \log |b_i|)$$
where $C$ depends on $k$ and the heights of the $\alpha_i$. In Pillai's equation, setting $\Lambda = x \log A - y \log B$, the conjecture hinges on understanding the strict lower bounds of $|\Lambda|$ relative to the unfixed variables $A, B, x, y$.

## 3. History & State of the Art (SOTA)

The conjecture was formulated by the Indian mathematician Subbayya Sivasankaranarayana Pillai in 1931, during his investigations into the distribution of perfect powers and Waring's problem.

Historically, the most famous special case of this conjecture is Catalan's Conjecture, proposed by Eugène Charles Catalan in 1844, which claims that the only solution for $c=1$ is $3^2 - 2^3 = 1$. This was famously proven unconditionally by Preda Mihăilescu in 2002 using the theory of cyclotomic fields and Galois modules.

With the advent of Alan Baker's theory of linear forms in logarithms in the late 1960s, it became possible to give effective upper bounds for the solutions of exponential Diophantine equations when certain parameters (like the bases $A$ and $B$) are fixed. 

A major theoretical milestone is the widely accepted understanding that the ABC conjecture implies Pillai's conjecture. Given that the ABC conjecture provides deep uniform bounds on the heights of solutions to $A+B=C$ in coprime integers, it naturally limits the frequency of perfect powers occurring close to one another.

## 4. Partial Results / Verified Cases

While the general statement remains open, significant partial results and specific verifications have been achieved:
- **Catalan's Equation ($c=1$):** Proven completely by P. Mihăilescu (2002). The only non-trivial solution in positive integers is $3^2 - 2^3 = 1$.
- **Fixed Bases:** If $A$ and $B$ are fixed positive integers, the equation $A^x - B^y = c$ has only finitely many solutions. This follows from Polya's theorem (1918) and can be solved effectively using linear forms in $p$-adic and Archimedean logarithms. For example, Herschfeld (1936) proved that $2^x - 3^y = c$ has at most one solution for sufficiently large $|c|$.
- **Fixed Exponents:** If $x$ and $y$ are fixed integers $\ge 2$ (not both 2), the equation $A^x - B^y = c$ reduces to finding integral points on hyperelliptic or superelliptic curves. By Siegel's theorem on integral points (1929), this is known to have finitely many solutions.
- **Verified Differences ($c \le 100$):** Using combinations of Baker's method and the LLL lattice basis reduction algorithm, all solutions to $A^x - B^y = c$ for $c \le 100$ (with varying specific fixed bases $A, B \le 100$) have been computationally verified by groups like Stroeker and Tijdeman (1982).
- **Specific primes:** Equations of the form $A^p - B^q = c$ for fixed specific small primes $p, q$ have been systematically solved by researchers like Bugeaud, Mignotte, and Siksek using the modular approach.

## 5. Principal Obstacles

The primary theoretical bottleneck lies in the inability to uniformly bound all four variables $(A, B, x, y)$ simultaneously using existing mathematical machinery.

1. **Failure of Baker's Method for Four Variables:** Baker's theory of linear forms in logarithms provides highly effective bounds for the exponents $x$ and $y$ when the bases $A$ and $B$ are fixed. However, when $A$ and $B$ are treated as completely free variables, the resulting theoretical bounds on the linear form $\Lambda = x \log A - y \log B$ become circular. The height of the algebraic numbers involved grows faster than the logarithmic bounds can constrain, rendering the method ineffective without additional a priori constraints.
2. **Limitations of the Modular Approach:** The Wiles-Ribet modular approach (utilizing Frey curves and Galois representations) is extremely powerful for fixed-exponent equations, most notably Fermat's Last Theorem ($A^p + B^p = C^p$). However, to apply this to Pillai's fully variable equation $A^x - B^y = c$, one must construct Frey varieties of higher dimensions (Abelian varieties) because the exponents $x$ and $y$ differ and vary freely. The necessary generalizations of Ribet's Level Lowering Theorem and modularity lifting theorems over these higher-dimensional spaces are severely lacking in current arithmetic geometry.

## 6. The Gap

The precise mathematical gap separating the proven cases from the fully general conjecture is the transition from "fixed parameter" bounds to "absolute uniform" bounds. 

Currently, analytical techniques can prove inequalities of the form:
$$ |A^x - B^y| \ge K(A, B, x, y) $$
where the effectiveness of the constant $K$ heavily depends on holding either the bases or the exponents constant. To bridge the gap and resolve the conjecture, one must establish an absolute lower bound for the distance between two arbitrary perfect powers that grows monotonically as a function of the powers themselves, independent of their specific bases or exponents. Essentially, we lack a functional tool that bounds the error term of rational approximations of $\frac{\log A}{\log B}$ uniformly across all $A, B \in \mathbb{Z}^+$.

## 7. Current Research (as of June 2026)

Active research heavily centers on conditional results, explicit algorithms, and generalized geometry:
- **ABC Conjecture Implications:** A dominant school of thought considers Pillai's conjecture solved conditionally upon the ABC conjecture. Shinichi Mochizuki's Inter-Universal Teichmüller Theory (IUTT) claims a proof of the ABC conjecture. However, since the broader mathematical community remains fractured on the validity of IUTT, researchers continue to treat Pillai's conjecture as unconditionally open and pursue alternative methods. *(frontier — verify)*
- **Explicit Baker-Feldman Bounds:** Improvements to the explicit constants in linear forms in logarithms are continually pursued by the Strasbourg and Bordeaux groups, aimed at making larger specific cases computationally tractable.
- **Computational Verification:** Ongoing distributed computing projects are extending the verified ranges of $c$ using the LLL algorithm, sieve methods, and $p$-adic linear forms, pushing the empirical lower bounds for general counter-examples significantly higher.

## 8. Future Work

Leading mathematicians suggest the following open pathways for future resolution:
- **Archimedean and $p$-adic Synthesis:** Combining Archimedean bounds from linear forms in logarithms with $p$-adic bounds from the modular method to simultaneously and tightly constrain all four variables.
- **Higher-Dimensional Diophantine Geometry:** Generalizing the theory of heights on algebraic curves to varieties of general type. Specifically, advancing Vojta's conjectures (which natively generalize the ABC conjecture to higher dimensions) would provide a natural geometric framework for bounding solutions to generalized Pillai-type equations.
- **Thue-Mahler Reductions:** Finding novel ways to reduce specific infinite families of Pillai equations into generalized Thue-Mahler equations, where recent algorithmic advances in computational number theory could yield explicit finite solution sets.

## 9. Key References

- **[Foundational]** Pillai, S. S. "On the inequality $0 < a^x - b^y \le n$". *Journal of the Indian Mathematical Society*, 19, 1-11, 1931.
- **[Foundational]** Mihăilescu, P. "Primary Cyclotomic Units and a Proof of Catalan's Conjecture". *Journal für die reine und angewandte Mathematik (Crelles Journal)*, 572, 167-195, 2004.
- **[SOTA / Recent]** Bennett, M. A., & Bugeaud, Y. "The equation $x^a - y^b = c$ in integers $x, y, a, b$". *Journal of the London Mathematical Society*, 85(1), 173-196, 2012.
- **[Survey]** Waldschmidt, M. "Open Diophantine Problems". *Moscow Mathematical Journal*, 4(1), 245-305, 2004.

## 10. Worked Example / Concrete Special Case

Let us explicitly examine the specific gap $c = 5$ for the fixed bases $A=2$ and $B=3$. The generalized Pillai equation collapses to the specific equation:
$$2^x - 3^y = 5$$
We seek all solutions in integers $x \ge 2, y \ge 1$.

**Step 1: Modular constraints (Congruences)**
Consider the equation modulo 8. Since we are looking for non-trivial powers, assume $x \ge 3$, so $2^x \equiv 0 \pmod 8$.
$$-3^y \equiv 5 \pmod 8 \implies 3^y \equiv -5 \equiv 3 \pmod 8$$
The sequence of $3^y \pmod 8$ for $y=1, 2, 3, \dots$ is exactly $3, 1, 3, 1, \dots$
Thus, $y$ must be an odd integer.

Next, consider the equation modulo 3:
$$2^x \equiv 5 \equiv 2 \pmod 3$$
The sequence of $2^x \pmod 3$ for $x=1, 2, 3, \dots$ is exactly $2, 1, 2, 1, \dots$
Thus, $x$ must also be an odd integer.

**Step 2: Identifying small solutions**
Let's check small odd values for $x$ and $y$:
- If $x=3$, $2^3 - 3^y = 5 \implies 8 - 3^y = 5 \implies 3^y = 3 \implies y=1$. Solution: $(x, y) = (3, 1)$.
- If $x=5$, $2^5 - 3^y = 5 \implies 32 - 3^y = 5 \implies 3^y = 27 \implies y=3$. Solution: $(x, y) = (5, 3)$.

**Step 3: Bounding larger solutions**
Suppose there exists a larger solution. Using linear forms in logarithms, one analyzes the linear form:
$$ \Lambda = x \log 2 - y \log 3 $$
From the equation $2^x - 3^y = 5$, we can factor to write $2^x = 3^y(1 + 5 \cdot 3^{-y})$. Taking logarithms yields:
$$ x \log 2 - y \log 3 = \log(1 + 5 \cdot 3^{-y}) \approx 5 \cdot 3^{-y} $$
Baker's theory provides a deterministic lower bound for $|\Lambda|$ algebraically in terms of $\log x$ and $\log y$. By comparing the exponentially small upper bound ($5 \cdot 3^{-y}$) with Baker's polynomial lower bound, one extracts an absolute maximum bound for $y$ (historically around $10^{15}$). Using the LLL algorithm to find the rational approximation of $\frac{\log 2}{\log 3}$, one can rapidly compress this massive theoretical bound down to computationally trivial numbers, proving rigorously that $(3, 1)$ and $(5, 3)$ are the **only** solutions for $2^x - 3^y = 5$.

This example demonstrates how fixing the bases makes the problem highly tractable via Baker's bounds and modular arithmetic, highlighting the stark contrast with the fully general conjecture where $A$ and $B$ are unknown and such bounds become circular.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*