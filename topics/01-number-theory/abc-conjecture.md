---
id: 01-number-theory/abc-conjecture
title: "abc Conjecture"
topic: 01-number-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# abc Conjecture

> **Topic:** Number Theory · **ID:** `01-number-theory/abc-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

The $abc$ conjecture, formulated independently by David Masser (1985) and Joseph Oesterlé (1988), proposes a deep and profound relationship between the additive and multiplicative properties of integers. 

A precise statement of the conjecture is as follows: for every real number $\epsilon > 0$, there exists a constant $K_\epsilon > 0$ such that for all triples $(a, b, c)$ of coprime positive integers satisfying $a + b = c$, the following inequality holds:

$$ c < K_\epsilon \cdot \text{rad}(abc)^{1+\epsilon} $$

where $\text{rad}(n)$ denotes the **radical** of $n$, defined as the product of the distinct prime factors of $n$. 

An equivalent formulation states that for any $\epsilon > 0$, there are only finitely many triples $(a, b, c)$ of coprime positive integers with $a + b = c$ such that:

$$ c > \text{rad}(abc)^{1+\epsilon} $$

A complete proof of the $abc$ conjecture would require rigorously establishing this asymptotic upper bound for all possible coprime triples, either via unconditional analytic bounds or by establishing a deep equivalence with arithmetic geometry (e.g., through a proven formulation of the Szpiro conjecture).

## 2. Mathematical Foundations

The fundamental mathematical object underlying the conjecture is the **radical** of an integer. Let $n$ be a positive integer with prime factorization $n = p_1^{e_1} p_2^{e_2} \cdots p_k^{e_k}$. The radical of $n$ is the square-free integer defined by:

$$ \text{rad}(n) = \prod_{p \mid n} p = p_1 p_2 \cdots p_k $$

We conventionally set $\text{rad}(1) = 1$. The radical acts as a measure of the "prime footprint" of an integer, ignoring the exponents of its prime factors.

To quantitatively measure how strongly a specific triple $(a, b, c)$ violates the naive expectation that $c < \text{rad}(abc)$, mathematicians define the **quality** of a triple, denoted $q(a,b,c)$, as:

$$ q(a,b,c) = \frac{\log c}{\log \text{rad}(abc)} $$

The $abc$ conjecture essentially posits that $\limsup_{c \to \infty} q(a,b,c) \le 1$. That is, while $c$ can occasionally exceed $\text{rad}(abc)$, it cannot exceed it by a polynomial power strictly greater than 1 for infinitely many triples.

The conjecture has deep roots in arithmetic geometry. It implies a bound on the discriminant of elliptic curves over $\mathbb{Q}$. Let $E$ be an elliptic curve over $\mathbb{Q}$ with minimal discriminant $\Delta_E$ and conductor $N_E$. The **Szpiro conjecture** states that for every $\epsilon > 0$, there exists a constant $C_\epsilon$ such that:

$$ |\Delta_E| \le C_\epsilon \cdot N_E^{6+\epsilon} $$

The $abc$ conjecture implies the modified Szpiro conjecture, establishing a profound bridge between prime factorizations and the moduli space of elliptic curves.

## 3. History & State of the Art (SOTA)

The $abc$ conjecture was inspired by a polynomial analogue. In 1984, Richard Mason proved the Mason-Stothers theorem, which bounds the degree of polynomials $A, B, C \in k[t]$ (where $k$ is a field and $A+B=C$) strictly by the number of distinct roots of $ABC$. Masser and Oesterlé independently translated this geometric/polynomial truth to the ring of integers $\mathbb{Z}$.

Over the decades, mathematicians extracted vast consequences from the conjecture, proving that its truth would resolve Roth's theorem, the Mordell conjecture (Faltings's theorem), and provide a near-trivial proof of Fermat's Last Theorem for sufficiently large exponents.

The state of the art shifted dramatically in 2012 when Shinichi Mochizuki of Kyoto University's Research Institute for Mathematical Sciences (RIMS) released a massive, 500-page series of preprints outlining Inter-universal Teichmüller theory (IUTT) and claiming a full proof of the $abc$ conjecture. Despite years of intense scrutiny and workshops, the global mathematical community remained largely unconvinced. 

In 2018, Fields Medalist Peter Scholze and Jakob Stix published a report identifying what they termed a "severe, unfixable gap" in Corollary 3.12 of Mochizuki's third IUTT paper. Mochizuki and his collaborators at RIMS dispute this critique and published the papers in *Publications of the Research Institute for Mathematical Sciences* in 2021. Nonetheless, outside of a specific circle of researchers, the conjecture is overwhelmingly considered to remain **open**.

## 4. Partial Results / Verified Cases

While the full $abc$ conjecture remains open, substantial partial results have been achieved:

- **Polynomial Analogue:** The Mason-Stothers theorem is fully proven and acts as the $abc$ conjecture for the polynomial ring $k[t]$.
- **Unconditional Upper Bounds:** While the conjecture demands a polynomial bound $c \ll \text{rad}(abc)^{1+\epsilon}$, the best unconditional bounds are exponential. C. L. Stewart and Kunrui Yu (2001), building on baker's method of linear forms in logarithms, proved that there exists an effectively computable constant $K$ such that:
  $$ c < \exp\left( K \cdot \text{rad}(abc)^{1/3} (\log \text{rad}(abc))^3 \right) $$
- **Computational Verifications (ABC@Home):** Massive distributed computing projects have exhaustively searched for triples with high quality ($q > 1$). The highest quality triple ever discovered was found by Eric Reyssat in 1987 (and remains the maximum known):
  $$ a = 2, \quad b = 3^{10} \cdot 109, \quad c = 23^5 $$
  This yields a quality of $q \approx 1.6299$. Extensive computational searches up to $c < 10^{18}$ confirm that triples with $q > 1$ become exceedingly rare, heavily supporting the empirical truth of the conjecture.

## 5. Principal Obstacles

The central obstacle in proving the $abc$ conjecture is the profound incompatibility between the additive structure of the integers (the equation $a+b=c$) and their multiplicative structure (the prime factorizations that define the radical). 

Traditional techniques in analytic number theory—such as the Hardy-Littlewood circle method or sieve methods—are excellent at capturing additive properties but fail to strongly constrain the multiplicative structures simultaneously. Conversely, tools from algebraic geometry (like Arakelov geometry and Faltings's height) can track multiplicative information via divisors and line bundles, but the bounds obtained on the arithmetic intersection numbers are not sharp enough to yield the required $(1+\epsilon)$ exponent. 

Mochizuki's IUTT attempted to overcome this by effectively dismantling and reconstructing the ring structure of $\mathbb{Z}$ across a "theater" of different Hodge theaters, mapping multiplicative structures while isolating additive deformations. However, the geometric and category-theoretic abstractions introduced (anabelian geometry applied across distinct universes) lack a clear translation to classical intersection theory, leaving classical number theorists unable to verify the crucial bounding steps (Corollary 3.12).

## 6. The Gap

The precise mathematical gap currently stands at bridging the effectively computable, exponential bounds of Stewart and Yu to the sharp, polynomial bound posited by Masser and Oesterlé. 

Specifically, to resolve the conjecture unconditionally, mathematicians must either:
1. Develop an entirely new bound for linear forms in $p$-adic logarithms that vastly improves upon Baker's theory.
2. Formulate a fully rigorous, classical arithmetic-geometric framework that bounds the Arakelov height of points on curves in terms of the log-discriminant without the purported logical leaps of IUTT.

The immediate social and epistemological gap involves resolving the IUTT controversy—whether by finding a way to successfully translate Mochizuki's anabelian insights into classical arithmetic geometry, or by conclusively proving that the bounds in IUTT cannot be achieved.

## 7. Current Research (as of June 2026)

Active research continues along several distinct fronts:

- **Refinement of Arithmetic Heights:** Groups working in Arakelov geometry are attempting to bound the Faltings height of elliptic curves to produce weaker, but unconditional, polynomial variants of the $abc$ bound.
- **Analysis of IUTT:** A subset of researchers continues to study IUTT, either to repair the widely perceived gaps in Corollary 3.12 or to extract weaker, verifiable algebraic lemmas that could be applied to Diophantine equations.
- **Algorithmic Searches:** Computational number theorists continue to search for triples with $q > 1.63$ utilizing lattice basis reduction algorithms (like LLL) and advanced sieving techniques to better map the empirical distribution of $abc$ hits.
- *(frontier — verify)* **Perfectoid Spaces:** Inspired by Scholze's work, there are nascent, highly speculative attempts to leverage the geometry of perfectoid spaces to study the $p$-adic behavior of elliptic curves and extract bounds on the discriminant, though a direct pathway to the $abc$ conjecture remains elusive.

## 8. Future Work

Leading mathematicians suggest that proving the full $abc$ conjecture may require an entirely new branch of mathematics that naturally unifies additive combinatorics with algebraic geometry over $\mathbb{Z}$. 

Short-term future work is focused on establishing an "effective $abc$ conjecture" for specific powers—for example, proving unconditionally that $c \ll \text{rad}(abc)^2$. Even this weaker bound would be sufficient to reprove Fermat's Last Theorem for large exponents and solve numerous open Diophantine equations. Additionally, finding new computational methods to exhaustively check for high-quality triples up to $c \approx 10^{30}$ could provide new heuristic data regarding the behavior of the $K_\epsilon$ constant.

## 9. Key References

- **[Foundational]** Masser, D. W. *Open problems.* Proceedings of the Symposium on Analytic Number Theory, 1985.
- **[Foundational]** Oesterlé, J. *Nouvelles approches du "théorème" de Fermat.* Séminaire Bourbaki, 1988.
- **[SOTA / Recent]** Stewart, C. L., & Yu, K. *On the abc conjecture.* Mathematische Annalen, 2001.
- **[Survey]** Granville, A., & Tucker, T. J. *It's as easy as abc.* Notices of the American Mathematical Society, 2002.
- **[SOTA / Recent]** Scholze, P., & Stix, J. *Why abc is still a conjecture.* Manuscript / RIMS proceedings debate, 2018.

## 10. Worked Example / Concrete Special Case

To ground the abstract formulation of the $abc$ conjecture, let us construct and verify one of the most famous special cases: the Reyssat triple, which yields the highest known quality.

Consider the following three coprime positive integers:
$$ a = 2 $$
$$ b = 3^{10} \cdot 109 = 6,436,341 $$
$$ c = 23^5 = 6,436,343 $$

**Step 1: Verify the additive property.**
We can easily check that $a + b = c$:
$$ 2 + 6,436,341 = 6,436,343 $$

**Step 2: Calculate the radicals.**
The prime factorization of each number is already given. We strip away the exponents to find the radical:
- $\text{rad}(a) = \text{rad}(2) = 2$
- $\text{rad}(b) = \text{rad}(3^{10} \cdot 109) = 3 \cdot 109 = 327$
- $\text{rad}(c) = \text{rad}(23^5) = 23$

Because $a, b,$ and $c$ are coprime, the radical of their product is the product of their radicals:
$$ \text{rad}(abc) = 2 \cdot 327 \cdot 23 = 15,042 $$

**Step 3: Compare $c$ to $\text{rad}(abc)$.**
We observe an extreme violation of the naive expectation that $c < \text{rad}(abc)$. Here:
$$ 6,436,343 > 15,042 $$
The number $c$ is vastly larger than the radical of the product.

**Step 4: Calculate the quality of the triple.**
To see exactly how anomalous this is, we calculate the quality $q(a,b,c)$:
$$ q = \frac{\log c}{\log \text{rad}(abc)} = \frac{\log(6436343)}{\log(15042)} \approx \frac{15.6774}{9.6186} \approx 1.6299 $$

This demonstrates a specific case where $c \approx \text{rad}(abc)^{1.6299}$. The $abc$ conjecture asserts that while we can find specific triples where $q > 1$ (like this one), for any bound $1 + \epsilon$ (say, $1.01$), the number of triples exceeding that power is strictly finite.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*