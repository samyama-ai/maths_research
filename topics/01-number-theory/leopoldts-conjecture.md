---
id: 01-number-theory/leopoldts-conjecture
title: "Leopoldt's Conjecture"
topic: 01-number-theory
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Leopoldt's Conjecture

> **Topic:** Number Theory · **ID:** `01-number-theory/leopoldts-conjecture` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Leopoldt's conjecture posits that for any number field $K$ and any prime number $p$, the $p$-adic regulator of $K$ is strictly non-zero. 

Equivalently, if $U_K$ is the group of fundamental units of the ring of integers $\mathcal{O}_K$, and we consider its natural diagonal embedding into the product of the local unit groups for all completions of $K$ above $p$, the topological closure of this image has a $\mathbb{Z}_p$-rank that is precisely equal to the original $\mathbb{Z}$-rank of $U_K$. In fundamental terms, the conjecture claims that the globally multiplicatively independent algebraic units of $K$ remain multiplicatively independent when interpreted locally as $p$-adic numbers; there are no "unexpected" $p$-adic algebraic relations among them. A complete proof would establish this non-vanishing property for all number fields $K$ unconditionally.

## 2. Mathematical Foundations

Let $K$ be a number field of degree $n = [K : \mathbb{Q}]$, with $r_1$ real embeddings and $r_2$ pairs of complex conjugate embeddings. By Dirichlet's Unit Theorem, the group of units $U_K = \mathcal{O}_K^\times$ is a finitely generated abelian group of rank $r = r_1 + r_2 - 1$. 

Let $\epsilon_1, \dots, \epsilon_r$ be a fundamental system of units for $U_K$. For a fixed prime number $p$, let $v_1, \dots, v_g$ be the places of $K$ dividing $p$. We map the tensor product $U_K \otimes_{\mathbb{Z}} \mathbb{Z}_p$ diagonally into the product of local unit groups:
$$ \phi_p: U_K \otimes_{\mathbb{Z}} \mathbb{Z}_p \longrightarrow \prod_{i=1}^g U_{K, v_i} $$
where $U_{K, v_i}$ is the unit group of the $v_i$-adic completion $K_{v_i}$. Using the standard local $p$-adic logarithm map $\log_p: U_{K, v_i} \to K_{v_i}$, one can construct an $r \times r$ matrix whose $(i, j)$-th entry is $\log_p(\sigma_i(\epsilon_j))$, with $\sigma_i$ traversing the $r$ normalized embeddings of $K$ into $\mathbb{C}_p$. The $p$-adic regulator, $R_p(K)$, is the determinant of this matrix (normalized by the valuation of roots of unity).

Leopoldt's conjecture asserts that $R_p(K) \neq 0$. 

This can be rephrased using the Leopoldt defect $\delta_p(K)$, defined as:
$$ \delta_p(K) = r - \text{rank}_{\mathbb{Z}_p}(\text{Im}(\phi_p)) $$
The conjecture directly asserts $\delta_p(K) = 0$. In the framework of Galois cohomology, let $M_p$ be the maximal abelian pro-$p$ extension of $K$ unramified outside $p$. By Global Class Field Theory, the Galois group $X = \text{Gal}(M_p/K)$ is a finitely generated $\mathbb{Z}_p$-module. The conjecture states:
$$ \text{rank}_{\mathbb{Z}_p}(X) = r_2 + 1 $$

## 3. History & State of the Art (SOTA)

- **1962:** Heinrich-Wolfgang Leopoldt proposed the conjecture while defining $p$-adic $L$-functions and evaluating their residues at $s=1$. He proved that the formula for the residue directly contains the $p$-adic regulator, mirroring the classical analytic class number formula.
- **1965:** James Ax demonstrated that the conjecture would be unconditionally true if the $p$-adic analogue of Schanuel's conjecture held, linking the problem deeply to algebraic independence and transcendence theory.
- **1967:** Armand Brumer proved the conjecture for all abelian extensions of $\mathbb{Q}$ and all abelian extensions of imaginary quadratic fields. Brumer achieved this by transferring Alan Baker’s newly developed method of linear forms in logarithms to the $p$-adic domain.
- **SOTA:** The conjecture remains fully open for general number fields, especially non-abelian extensions of $\mathbb{Q}$ of degree $\ge 3$. Computations have relentlessly verified it for many specific fields and primes. Theoretically, it plays a structural cornerstone in Iwasawa theory; its truth guarantees the expected finite generation of various Selmer groups and standardizes the algebraic structure of the unramified Iwasawa module over the cyclotomic $\mathbb{Z}_p$-extension.

## 4. Partial Results / Verified Cases

- **Abelian over $\mathbb{Q}$:** Proven unconditionally by Brumer (1967). This covers all cyclotomic fields and their subfields (e.g., all real quadratic fields).
- **Abelian over Imaginary Quadratic Fields:** Proven unconditionally by Brumer (1967) utilizing elliptic units and complex multiplication.
- **Function Fields:** The strict analogue of Leopoldt's conjecture for function fields over finite fields is completely proven. It translates geometrically to the non-vanishing of certain characteristic polynomials on the Jacobians of curves.
- **Empirical Bounds:** Computationally verified for completely real non-abelian fields of small degrees (cubic, quartic, quintic) for prime numbers $p$ well into the tens of millions using lattice reduction algorithms (LLL) and $p$-adic approximations.

## 5. Principal Obstacles

The fundamental bottleneck is the weakness of general $p$-adic transcendence theory. Proving that the $p$-adic regulator is non-zero demands proving that the $p$-adic logarithms of fundamental units are linearly independent over $\mathbb{Z}_p$. 

In the complex case, standard topology prevents discrete subgroups from concentrating infinitesimally around the identity. In the ultrametric $p$-adic topology, this intuition fails. Baker’s method of linear forms in $p$-adic logarithms successfully handles units constructed via explicit algebraic machinery (e.g., cyclotomic units derived from the exponential map, or elliptic units from the Weierstrass $\wp$-function). For a generic non-abelian number field, no such explicit units exist. Without knowing how units are distributed globally relative to one another, current perturbation limits and transcendence bounds cannot guarantee that a linear combination of their local $p$-adic logarithms does not inadvertently sum to exactly zero. 

## 6. The Gap

The exact boundary of human knowledge on this problem lies exactly at the frontier of explicit class field theory (Kronecker-Weber domains and Complex Multiplication). To cross the gap into general non-abelian fields requires either a massive breakthrough in transcendence theory (such as proving the $p$-adic Schanuel Conjecture) or the discovery of a non-abelian Euler system (like generalized Stark units or Rubin-Stark units) that unconditionally applies to arbitrary number fields, forcing local-global non-vanishing properties.

## 7. Current Research (as of June 2026)

Active research continues in several highly sophisticated directions:
- **Equivariant Tamagawa Number Conjecture (ETNC):** Using broader generalizations of the Stark conjectures to relate the leading coefficients of Artin $L$-functions to regulators, bounding the Leopoldt defect.
- **Iwasawa Theory of Selmer Groups:** Reversing the implication to try and deduce Leopoldt's conjecture from the structure of ideal class groups up the cyclotomic tower.
- *(frontier — verify)* **$p$-adic Hodge Theory and Perfectoid Spaces:** Utilizing Peter Scholze's framework of perfectoid spaces to link $p$-adic regulators geometrically to the étale cohomology of motives over non-abelian fields, bypassing traditional linear forms in logarithms.

## 8. Future Work

- **Proving the $p$-adic Schanuel Conjecture:** This remains the "holy grail" that would simultaneously resolve Leopoldt's conjecture for all number fields.
- **Constructing Non-Abelian Euler Systems:** Building unconditionally verifiable Euler systems that can tightly bind the unit groups of fields lacking Complex Multiplication.
- **Algorithmic Searches:** Expanding computational matrices using high-performance $p$-adic linear algebra to search for potential, albeit highly unexpected, pathological counterexamples in large degree, highly ramified nilpotent extensions.

## 9. Key References

- **[Foundational]** Leopoldt, H. W. *Zur Arithmetik in abelschen Zahlkörpern.* Journal für die reine und angewandte Mathematik 209 (1962): 54-71. [DOI](https://doi.org/10.1515/crll.1962.209.54)
- **[Foundational]** Brumer, A. *On the units of algebraic number fields.* Mathematika 14, no. 2 (1967): 121-124.
- **[SOTA / Recent]** Neukirch, J., Schmidt, A., Wingberg, K. *Cohomology of Number Fields.* 2nd ed., Springer Science & Business Media, 2008.
- **[Survey]** Washington, L. C. *Introduction to Cyclotomic Fields.* 2nd ed., Springer Science & Business Media, 1997.

## 10. Worked Example / Concrete Special Case

Consider the real quadratic field $K = \mathbb{Q}(\sqrt{2})$ and the prime $p = 3$. 

The degree is $[K:\mathbb{Q}] = 2$. It has $r_1 = 2$ real embeddings and $r_2 = 0$ complex embeddings, so the rank of the unit group is $r = 2 + 0 - 1 = 1$. The ring of integers is $\mathcal{O}_K = \mathbb{Z}[\sqrt{2}]$, and a fundamental unit is $\epsilon = 1 + \sqrt{2}$.

Leopoldt's conjecture for this specific case asserts that the $3$-adic regulator is non-zero, which equates simply to showing that the $3$-adic logarithm $\log_3(\epsilon) \neq 0$.

Because $2$ is not a quadratic residue modulo $3$ ($1^2 \equiv 1$, $2^2 \equiv 1$), the prime $3$ is inert in $K$. The local completion is $K_3 = \mathbb{Q}_3(\sqrt{2})$, with residue field $\mathbb{F}_9$. The group of units in $\mathbb{F}_9$ has order $9 - 1 = 8$. To evaluate the $3$-adic logarithm using its Taylor series, we must raise $\epsilon$ to the 8th power to find a unit congruent to $1$ modulo $3$:
$$ \epsilon^2 = (1+\sqrt{2})^2 = 3 + 2\sqrt{2} $$
$$ \epsilon^4 = (3+2\sqrt{2})^2 = 17 + 12\sqrt{2} $$
$$ \epsilon^8 = (17+12\sqrt{2})^2 = 289 + 408\sqrt{2} + 288 = 577 + 408\sqrt{2} $$

We can rewrite $\epsilon^8$ as $1 + x$, where $x = 576 + 408\sqrt{2}$. 
Factoring $3$ out of $x$ gives $x = 3(192 + 136\sqrt{2})$. Since $192 = 3 \cdot 64 \equiv 0 \pmod 3$ and $136 = 3 \cdot 45 + 1 \equiv 1 \pmod 3$, we find that modulo $9$, $x \equiv 3\sqrt{2} \pmod 9$.
This shows that the $3$-adic valuation of $x$ is exactly $v_3(x) = 1$.

The $p$-adic logarithm is defined by the series:
$$ \log_3(1+x) = x - \frac{x^2}{2} + \frac{x^3}{3} - \dots $$
Since $v_3(x) = 1$, the first term $x$ has valuation $1$. The second term $-\frac{x^2}{2}$ has valuation exactly $2$, and all higher terms have valuation $\ge 2$. Therefore, the valuation of the entire sum is dominated by the leading term:
$$ \log_3(\epsilon^8) \equiv x \equiv 3\sqrt{2} \pmod{9} $$
Because $3\sqrt{2} \not\equiv 0 \pmod 9$, the value is not zero. By the linearity of the logarithm:
$$ \log_3(\epsilon) = \frac{1}{8} \log_3(\epsilon^8) \neq 0 $$
Thus, the $3$-adic regulator of $K = \mathbb{Q}(\sqrt{2})$ strictly does not vanish, explicitly confirming Leopoldt's conjecture for this field and prime.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*