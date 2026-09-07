---
id: 01-number-theory/halls-conjecture
title: "Hall's Conjecture"
topic: 01-number-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Hall's Conjecture

> **Topic:** Number Theory · **ID:** `01-number-theory/halls-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Hall's Conjecture, proposed by Marshall Hall Jr. in 1971, is a precise statement regarding the minimum possible distance between a perfect square and a perfect cube in the integers.

**Strong Hall's Conjecture (Original Form):**
There exists an absolute constant $C > 0$ such that for all integers $x, y$ satisfying $y^2 \neq x^3$, the following inequality holds:
$$ |y^2 - x^3| > C \sqrt{|x|} $$

**Weak Hall's Conjecture (Generalized Form):**
For every $\epsilon > 0$, there exists a constant $C(\epsilon) > 0$ such that for all integers $x, y$ with $y^2 \neq x^3$:
$$ |y^2 - x^3| > C(\epsilon) |x|^{\frac{1}{2} - \epsilon} $$

A complete resolution of the conjecture requires either proving the existence of the bounding constants or providing an infinite family of integer pairs $(x,y)$ that violates the bound for all chosen constants, which would disprove the conjecture.

## 2. Mathematical Foundations

The problem lies at the intersection of Diophantine approximation, elliptic curves, and the theory of heights. 
Let us define the polynomial $P(x, y) = y^2 - x^3$. The roots of this polynomial define a singular cubic curve (the cuspidal cubic). Integer solutions near this curve are precisely pairs of integers where $y^2$ is very close to $x^3$.

The conjecture can be framed algebraically using the **ABC Conjecture**. For coprime integers $A, B, C$ such that $A + B = C$, we define the radical $\text{rad}(n)$ as the product of the distinct prime factors of $n$. The ABC conjecture states that for any $\epsilon > 0$, there exists a constant $K(\epsilon)$ such that:
$$ \max(|A|, |B|, |C|) \leq K(\epsilon) \text{rad}(ABC)^{1+\epsilon} $$

By setting $A = x^3$, $C = y^2$, and $B = y^2 - x^3 = k$, and assuming without loss of generality that $\gcd(x,y)=1$, we find:
$$ \text{rad}(x^3 k y^2) = \text{rad}(x k y) \leq |x k y| $$

Because $y^2 = x^3 + k$, for small $k$ we have $y \approx x^{3/2}$. Therefore, $|x k y| \approx k x^{5/2}$.
Applying the ABC conjecture bound:
$$ x^3 \approx y^2 \leq K(\epsilon) (k x^{5/2})^{1+\epsilon} = K(\epsilon) k^{1+\epsilon} x^{\frac{5}{2}(1+\epsilon)} $$

Rearranging the exponents yields:
$$ k^{1+\epsilon} \gg x^{3 - \frac{5}{2}(1+\epsilon)} = x^{\frac{1}{2} - \frac{5}{2}\epsilon} $$

This implies $|k| \gg x^{\frac{1}{2} - \delta}$ for a correspondingly small $\delta$. Thus, the Weak Hall's Conjecture is a direct corollary of the ABC Conjecture.

## 3. History & State of the Art (SOTA)

- **1965 (Davenport's Theorem):** Harold Davenport proved a polynomial analogue. For complex polynomials $f(t), g(t) \in \mathbb{C}[t]$ such that $g(t)^2 \neq f(t)^3$, $\deg(g^2 - f^3) \geq \frac{1}{2}\deg(f) + 1$. This structural insight deeply inspired Hall.
- **1971 (Original Formulation):** Marshall Hall Jr. formulated the integer version of the conjecture after noticing the paucity of squares and cubes close to one another in integer sequences.
- **1982 (Danilov's Bound):** L. V. Danilov found an infinite family of solutions utilizing the Pell equation $t^2 - 5u^2 = -4$, proving that if the absolute constant $C$ exists in the strong conjecture, it must satisfy $C < \frac{54}{25\sqrt{5}} \approx 0.966$. 
- **1998 (Elkies' Computations):** Noam Elkies used lattice reduction (the LLL algorithm) over rational points on curves to find the current record-holding integer pair $x = 5853886516781223$, $y = 447884928428402042307918$, yielding $x^3 - y^2 = -1641843$. This gives a ratio of $|y^2 - x^3| / \sqrt{x} \approx 0.0214$.
- **Current Status:** Most experts in arithmetic geometry suspect that the Strong Hall's Conjecture is false (meaning $\liminf |y^2 - x^3|/\sqrt{x} = 0$), while the Weak Hall's Conjecture remains highly believed but fiercely open, pending an accepted proof of the ABC Conjecture.

## 4. Partial Results / Verified Cases

- **Polynomial Rings:** Davenport's theorem completely resolves the exact analogue for polynomials in $\mathbb{C}[t]$. This was later generalized by R. C. Mason (the Mason-Stothers theorem) which directly formed the genesis of the ABC conjecture.
- **Unconditional Lower Bounds:** Using Alan Baker's theory of linear forms in logarithms, mathematicians have obtained unconditional lower bounds on the difference. Current state-of-the-art bounds prove that for $y^2 \neq x^3$:
  $$ |y^2 - x^3| \geq c (\log x)^\kappa $$
  for small absolute constants $c, \kappa > 0$. While theoretically significant, this logarithmic bound is exponentially weaker than the $O(x^{1/2})$ bound demanded by Hall's Conjecture.
- **Computational Verification:** Exhaustive computational searches have verified the sequence of minimal differences up to $x \approx 10^{20}$. In all bounded intervals tested computationally, the lower envelope of differences rigorously adheres to the weak Hall bound.

## 5. Principal Obstacles

The primary obstacle is that integers lack the continuous geometric structure that makes the polynomial analogue solvable. In $\mathbb{C}[t]$, one can differentiate polynomials and analyze the roots of their derivatives (a technique Davenport and Mason used extensively). There is no "derivative" in $\mathbb{Z}$ that preserves additive and multiplicative structures in the same way.

Secondly, standard Diophantine approximation techniques (like Roth's theorem or the Schmidt subspace theorem) are generally ill-equipped to bound differences between highly specific sparse sequences like $x^3$ and $y^2$. They work well for bounding rational approximations to fixed algebraic numbers, but here, the algebraic geometry of the curve $y^2 = x^3 + k$ shifts dynamically as $k$ varies. 

Finally, linear forms in logarithms natively produce logarithmic, rather than polynomial, bounds because they measure linear independence in the multiplicative group of algebraic numbers, mapping back to the additive group via logarithms. They cannot cross the threshold to polynomial bounds without a fundamental paradigm shift.

## 6. The Gap

The central gap lies between the analytic geometry of complex polynomials and the discrete arithmetic of integer rings. Specifically:
1. **The Exponent Gap:** The gap between the unconditional Baker-type bounds ($O(\log^\kappa x)$) and the conjectured Hall bounds ($O(x^{1/2 - \epsilon})$) is enormous. There is currently no mathematical machinery capable of crossing this exponential divide.
2. **The Constant Gap:** Even if we assume the weak form is true, it remains entirely unknown whether the specific exponent $\frac{1}{2}$ supports a strictly positive constant $C$ (Strong Hall), or if the constant can be driven to zero. This represents a subtle boundary in Diophantine approximation for which there is no viable theoretical framework.

## 7. Current Research (as of June 2026)

Research continues actively along several parallel tracks:
- **Lattice Reduction Searches:** Algorithmic number theorists employ advanced lattice reduction (LLL and BKZ algorithms) coupled with high-performance computing clusters to find sparse solutions to $x^3 - y^2 = k$ that might drive the constant $C$ lower than Elkies' $0.0214$, attempting to empirically falsify the Strong form.
- **Explicit ABC and Szpiro:** Researchers studying effective versions of Szpiro's Conjecture on elliptic curves often generate new theoretical heuristics for Hall's Conjecture. *(frontier — verify)* Recent preprints attempt to leverage rigid analytic geometry and perfectoid spaces to bridge the gap between function fields and number fields, although these have not yet yielded unconditional bounds for Hall's.
- **Mochizuki's IUT:** Inter-universal Teichmüller (IUT) theory remains a controversial backdrop. While claimed by Shinichi Mochizuki to prove the ABC conjecture (and thus Weak Hall), the broad consensus of the arithmetic geometry community remains that the proof contains a critical, unresolved gap. Therefore, independent, conventional approaches to Hall's are still heavily prioritized.

## 8. Future Work

Leading experts suggest several potential pathways to break the deadlock:
- **Refining Linear Forms:** Attempting to construct $p$-adic analogues or non-archimedean extensions of Baker's method that might capture sub-polynomial, but super-logarithmic bounds, such as $\exp(\sqrt{\log x})$.
- **Falsifying the Strong Form:** Finding a mechanism to systematically construct solutions that push $|y^2 - x^3| / \sqrt{x} \to 0$. This would likely involve finding higher-genus modular curves that parametrically map onto the cuspidal cubic with extremely dense integral points.
- **Connections to Belyi Maps:** Further exploring Belyi maps and Grothendieck's *dessins d'enfants* to transport the rigid Davenport bounds from the Riemann sphere directly to the integers via Arakelov geometry.

## 9. Key References

- **[Foundational]** Hall, M. *The Diophantine Equation $x^3 - y^2 = k$.* Computers in Number Theory, Academic Press, 1971.
- **[Foundational]** Davenport, H. *On $f^3(t) - g^2(t)$.* Norske Vid. Selsk. Forh. (Trondheim), 1965.
- **[SOTA / Recent]** Elkies, N. D. *Rational points near curves and small nonzero $|x^3 - y^2|$ via lattice reduction.* Lecture Notes in Computer Science (ANTS-IV), Springer, 2000.
- **[Survey]** Lang, S. *Old and new conjectured Diophantine inequalities.* Bulletin of the American Mathematical Society, 1990.
- **[Survey]** Nitaj, A. *The ABC conjecture homepage.* (Maintained comprehensive survey of ABC and Hall's conjecture literature).

## 10. Worked Example / Concrete Special Case

Let us examine a concrete, famously small difference between a square and a cube to illustrate the sparse phenomenon Hall was studying.

Consider the integers $x = 5234$ and $y = 378661$.
Let us calculate their respective cube and square:
$$ x^3 = 5234^3 = 143,384,152,904 $$
$$ y^2 = 378661^2 = 143,384,153,321 $$

Despite these numbers being on the order of 143 billion, their absolute difference is astonishingly small:
$$ |y^2 - x^3| = |143,384,153,321 - 143,384,152,904| = 417 $$

To see how this relates to Hall's Conjecture, we compare this difference to the square root of $x$:
$$ \sqrt{x} = \sqrt{5234} \approx 72.346 $$

The ratio of the difference to the square root of $x$ is:
$$ \frac{|y^2 - x^3|}{\sqrt{x}} \approx \frac{417}{72.346} \approx 5.76 $$

For $x$ this large, a typical random choice would yield an expected distance between a square and a cube on the order of $\sqrt{x^3} \approx x^{1.5} \approx 378,000$. Finding a difference of just $417$ is an exceptionally rare event in the integers. Yet, the ratio $5.76$ respects the theoretical lower bound proposed by Hall, remaining strictly bounded away from zero.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*