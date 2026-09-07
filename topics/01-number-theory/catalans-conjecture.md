---
id: 01-number-theory/catalans-conjecture
title: "Catalan's Conjecture"
topic: 01-number-theory
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Catalan's Conjecture

> **Topic:** Number Theory · **ID:** `01-number-theory/catalans-conjecture` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

Catalan's Conjecture (now known as Mihăilescu's Theorem) states that $8$ and $9$ are the only consecutive powers of natural numbers. 

Formally, the conjecture asserts that the only solution in the natural numbers for $x, y, a, b > 1$ to the exponential Diophantine equation
$$x^a - y^b = 1$$
is $x=3, a=2, y=2, b=3$. 

A complete proof required demonstrating that no other non-trivial integer solutions exist, meaning it is impossible to find two perfect powers (squares, cubes, or higher) that differ by exactly $1$, other than $3^2 = 9$ and $2^3 = 8$.

## 2. Mathematical Foundations

The core mathematical structure revolves around the study of the exponential Diophantine equation:
$$x^p - y^q = 1$$
where $p$ and $q$ are odd primes. If a solution exists for composite exponents $a$ and $b$, it implies a solution for prime exponents, reducing the general problem to primes $p, q \ge 3$ along with the cases where one exponent is $2$.

The resolution of the problem relies deeply on algebraic number theory, specifically the properties of cyclotomic fields. Let $\zeta_p$ be a primitive $p$-th root of unity, and consider the cyclotomic field $K = \mathbb{Q}(\zeta_p)$ with its ring of integers $\mathcal{O}_K = \mathbb{Z}[\zeta_p]$. The equation can be factored over $K$ as:
$$x^p - 1 = (x-1) \prod_{k=1}^{p-1} (x - \zeta_p^k) = y^q$$

The proof leverages the theory of **Galois modules** and the **ideal class group** of $K$. Crucial theorems invoked include Stickelberger's Theorem, which provides elements in the group ring $\mathbb{Z}[G]$ (where $G = \text{Gal}(K/\mathbb{Q})$) that annihilate the ideal class group of $K$, and Thaine's Theorem, which connects the units of $K$ to the annihilators of the class group.

## 3. History & State of the Art (SOTA)

The problem was first explicitly stated by the Belgian mathematician Eugène Charles Catalan in 1844 in a letter to the editor of *Crelle's Journal* (*Journal für die reine und angewandte Mathematik*). However, special cases were studied much earlier. In 1343, Levi ben Gerson proved that the only powers of $2$ and $3$ that differ by $1$ are $8$ and $9$.

A major breakthrough occurred in 1976 when Robert Tijdeman applied Baker's method of linear forms in logarithms (from transcendental number theory) to provide an effective upper bound for $x, y, p,$ and $q$. Tijdeman proved that Catalan's equation has at most a finite number of solutions. 

Despite Tijdeman's finiteness result, the theoretical bounds were astronomically large (initially around $10^{110}$), putting brute-force computational verification entirely out of reach. In 2002, Preda Mihăilescu solved the conjecture completely by abandoning the analytic approach of Baker's method and deploying deep algebraic number theory, specifically properties of cyclotomic units. His proof was officially published in 2004.

## 4. Partial Results / Verified Cases

Prior to Mihăilescu's 2002 proof, several partial cases had been strictly verified:
- **Levi ben Gerson (1343):** Proved the conjecture for equations of the form $2^a - 3^b = \pm 1$.
- **Leonhard Euler (1738):** Solved the case where $a=2, b=3$, proving $x^2 - y^3 = 1$ has only the solution $x=3, y=2$.
- **Victor-Amédée Lebesgue (1850):** Proved there are no solutions for $b=2$, meaning $x^p - y^2 = 1$ has no non-trivial solutions.
- **Ko Chao (1965):** Proved there are no solutions for $a=2$, i.e., $x^2 - y^q = 1$ has no non-trivial solutions (reducing the general problem strictly to odd primes $p, q$).
- **J. W. S. Cassels (1960):** Proved that if $x^p - y^q = 1$ has a solution, then $p \mid y$ and $q \mid x$.
- **Computational Verification:** Using Mignotte's refined analytic bounds and Cassels' relations, computers verified that there are no solutions for $p, q < 10^7$ before the full proof was discovered.

## 5. Principal Obstacles

The main obstacle in Catalan's Conjecture was that the exponents $a$ and $b$ were unknown variables. Traditional algebraic number theory, such as unique factorization over Dedekind domains (used in classical attempts at Fermat's Last Theorem), works well when exponents are fixed. When factoring $x^p - 1$ in $\mathbb{Z}[\zeta_p]$, the non-unique factorization of ideals and the unknown degree of the cyclotomic extension $p$ made parameterizing solutions extremely difficult.

Analytic methods like Baker's theory of linear forms in logarithms could bound the size of the variables, but these bounds were computationally intractable. Perturbation theory and standard Diophantine approximation fail to close the gap because logarithms of integers pack very densely at the scales required, making it impossible to separate the true solutions from "near-misses" computationally.

## 6. The Gap

Before Mihăilescu's work, the precise boundary to be crossed was the gap between Tijdeman's analytic upper bounds (where variables could be as large as $10^{110}$) and the computational lower bounds (checked up to $10^7$). The gap required either thousands of years of supercomputing time, a dramatic improvement in the estimates of linear forms in logarithms, or a completely novel theoretical approach. Mihăilescu crossed this gap by proving that if a solution existed for large primes $p$ and $q$, it would impose contradictory restrictions on the annihilators of the class group of cyclotomic fields, effectively proving the non-existence of solutions algebraically without needing to compute up to the analytic bounds.

## 7. Current Research (as of June 2026)

With Catalan's Conjecture definitively proven, modern research has shifted to its generalizations, most notably the **Pillai Conjecture**. Pillai's Conjecture hypothesizes that for any given integer $c > 0$, the equation $x^a - y^b = c$ has only finitely many solutions. Catalan's Conjecture is simply the case where $c=1$.

Active research groups in Diophantine geometry are studying effective bounds for Pillai's equation. Another active frontier is the **Fermat-Catalan Conjecture** (or Beal's Conjecture), which examines $x^a + y^b = z^c$ where $1/a + 1/b + 1/c < 1$. 

*(frontier — verify)* Recent preprints from researchers utilizing refined $p$-adic linear forms in logarithms claim to have lowered the bounds for specific classes of the generalized Pillai equation $Ax^a - By^b = c$, making small-parameter instances computationally verifiable. Furthermore, deep connections between the abc-conjecture and Catalan-type exponential equations remain an active area of investigation.

## 8. Future Work

Leading mathematicians working in Diophantine equations have articulated the following pathways:
- Finding an unconditionally effective proof of Pillai's Conjecture, bounding the size of $x^a$ and $y^b$ purely in terms of $c$.
- Proving the generalized Fermat-Catalan conjecture.
- Extending Mihăilescu's cyclotomic annihilation techniques to resolve broader classes of Diophantine equations involving unknown prime exponents where the abc-conjecture is not yet rigorously applicable.

## 9. Key References

- **[Foundational]** Catalan, E. *Note extraite d'une lettre adressée à l'éditeur.* Journal für die reine und angewandte Mathematik, 1844. 
- **[Foundational]** Tijdeman, R. *On the equation of Catalan.* Acta Arithmetica, 1976.
- **[SOTA / Recent]** Mihăilescu, P. *Primary Cyclotomic Units and a Proof of Catalan's Conjecture.* Journal für die reine und angewandte Mathematik (Crelles Journal), 2004.
- **[Survey]** Schoof, R. *Catalan's Conjecture.* Universitext, Springer, 2008.
- **[Survey]** Bilu, Y., Bugeaud, Y., Mignotte, M. *The Problem of Catalan.* Springer, 2014.

## 10. Worked Example / Concrete Special Case

Consider Euler's verified case where $a=2$ and $b=3$. We seek integer solutions $x, y > 1$ to:
$$x^2 - y^3 = 1$$
We can rewrite this as:
$$y^3 = x^2 - 1 = (x-1)(x+1)$$
We analyze the greatest common divisor $d = \gcd(x-1, x+1)$. Since $(x+1) - (x-1) = 2$, any common divisor must divide $2$. Thus, $d = 1$ or $d = 2$.

**Case 1: $d=1$**
If $x-1$ and $x+1$ are coprime, and their product is a perfect cube ($y^3$), both factors must themselves be perfect cubes. The only two perfect cubes that differ by exactly $2$ are $1$ and $-1$. Thus:
$$x+1 = 1 \implies x = 0$$
But the problem strictly requires $x > 1$. Therefore, no valid solution exists in this case.

**Case 2: $d=2$**
If the greatest common divisor is $2$, then $x$ must be odd. Let $x = 2k + 1$. Substituting this into the factors gives:
$$y^3 = (2k)(2k+2) = 4k(k+1)$$
Because $x$ is odd, $x^2$ is odd, so $y^3 = x^2 - 1$ must be even, meaning $y$ is even. Let $y = 2m$. Substituting $y$:
$$(2m)^3 = 8m^3 = 4k(k+1) \implies 2m^3 = k(k+1)$$
Since $k$ and $k+1$ are consecutive integers, they are coprime ($\gcd(k, k+1) = 1$). Since their product is twice a cube, one of them must be a perfect cube, and the other must be twice a perfect cube.

Subcase 2a: Let $k = u^3$ and $k+1 = 2v^3$. Then $2v^3 - u^3 = 1$. By inspection, a solution is $u=1, v=1$, yielding $k=1$. 
If $k=1$, then $x = 2(1) + 1 = 3$. 
Using $y^3 = x^2 - 1$, we get $y^3 = 3^2 - 1 = 8$, which gives $y = 2$. This matches the known solution.

Subcase 2b: Let $k = 2v^3$ and $k+1 = u^3$. Then $u^3 - 2v^3 = 1$. The only integer solution is $u=1, v=0$, which yields $k=0$ and $x=1$, failing the condition $x > 1$.

Thus, $x=3, y=2$ is the unique solution to this specific case, demonstrating the Diophantine descent method used before modern cyclotomic field techniques became necessary for the general problem.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*