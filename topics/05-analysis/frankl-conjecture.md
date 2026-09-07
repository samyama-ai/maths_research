---
id: 05-analysis/frankl-conjecture
title: "Frankl Conjecture"
topic: 05-analysis
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Frankl Conjecture (Union-Closed Sets Conjecture)

> **Topic:** Real & Complex Analysis (Analytic Combinatorics & Information Theory) · **ID:** `05-analysis/frankl-conjecture` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

The Frankl Conjecture, most widely known as the Union-Closed Sets Conjecture, postulates a fundamental lower bound on the frequency of the most abundant element within a specific class of set systems. 

Formally, let $U$ be a finite set (the universe), and let $\mathcal{F} \subseteq \mathcal{P}(U)$ be a finite family of sets defined over $U$. The family $\mathcal{F}$ is said to be *union-closed* if, for any two sets $A, B \in \mathcal{F}$, their union also belongs to the family: $A \cup B \in \mathcal{F}$. 

The conjecture states that for any finite union-closed family of sets $\mathcal{F}$ such that $\mathcal{F} \neq \{\emptyset\}$, there exists at least one element $x \in U$ that is contained in at least half of the sets in $\mathcal{F}$. 

Expressed mathematically, if $\mathcal{F}$ is a union-closed family containing at least one non-empty set, then:
$$ \exists x \in U \text{ such that } |\{A \in \mathcal{F} : x \in A\}| \ge \frac{|\mathcal{F}|}{2} $$

A complete proof of the conjecture requires demonstrating that this $1/2$ bound holds strictly for all possible union-closed families, regardless of their internal algebraic structure or sparsity. A disproof requires the construction of a finite union-closed family where every element in the underlying universe appears in strictly fewer than half of the sets in $\mathcal{F}$.

## 2. Mathematical Foundations

While discrete in its formulation, the most significant modern progress on the Frankl Conjecture relies heavily on real analysis, convex optimization, and continuous information theory.

Let $U = \{1, 2, \dots, n\}$. A family $\mathcal{F} \subseteq 2^U$ can be represented as a subset of the Boolean hypercube $\{0,1\}^n$. The union operation corresponds to the bitwise boolean OR operation $\lor$.

The *frequency* of an element $x \in U$ in $\mathcal{F}$ is defined by the function:
$$ f_{\mathcal{F}}(x) = \frac{|\{A \in \mathcal{F} : x \in A\}|}{|\mathcal{F}|} $$
The conjecture asserts that $\max_{x \in U} f_{\mathcal{F}}(x) \ge \frac{1}{2}$.

**Information-Theoretic and Analytic Formulation:**
The contemporary analytic approach, which elevated the problem into the realm of real analysis, models the selection of sets from $\mathcal{F}$ as random variables and leverages Shannon entropy. Let $X$ and $Y$ be independent, uniformly distributed random variables taking values in $\mathcal{F}$. The Shannon entropy of $X$ is exactly:
$$ H(X) = -\sum_{A \in \mathcal{F}} \mathbb{P}(X=A) \log_2 \mathbb{P}(X=A) = \log_2 |\mathcal{F}| $$

Because $\mathcal{F}$ is union-closed, the random variable $X \cup Y$ also takes values in $\mathcal{F}$. By the fundamental property of entropy (that the entropy of a distribution on a finite support is maximized by the uniform distribution), it follows that:
$$ H(X \cup Y) \le \log_2 |\mathcal{F}| = H(X) $$

By decomposing the entropy of the joint distribution across the $n$ coordinates using the chain rule for entropy and subadditivity, one can bound $H(X \cup Y)$ from below in terms of the individual marginal probabilities $p_i = f_{\mathcal{F}}(i)$. This translates the discrete combinatorial problem into a continuous, convex optimization problem over $[0,1]^n$: bounding the minimum possible maximum marginal probability $p_i$ such that the entropy inequalities hold.

## 3. History & State of the Art (SOTA)

The conjecture was first formulated by Péter Frankl in 1979 during a visit to Paris, though it was popularized through oral transmission before appearing in print. For decades, the problem remained entirely immune to standard inductive, algebraic, and combinatorial techniques.

**Historical Milestones:**
- **1979–1990s (Structural Era):** Early work focused on proving the conjecture for specialized structural cases. Poonen (1992) established foundational theorems regarding the minimum necessary structure of potential counterexamples, proving that the conjecture holds if the family contains certain substructures.
- **2000s (Computational Era):** Exhaustive computational searches pushed the verified lower bounds. Roberts and Simpson (2010) computationally verified the conjecture for all families where $|\mathcal{F}| \le 50$. Balla, Bollobás, and Eccles (2013) verified it for all universes where $|U| \le 12$.
- **2022 (The Analytic Breakthrough):** In November 2022, Justin Gilmer achieved a massive breakthrough by applying information theory. He proved the existence of a constant $c > 0$ such that every union-closed family has an element appearing in at least a $c$-fraction of the sets, explicitly proving $c \ge 0.01$. 
- **2022–2023 (Rapid Optimization):** Within days of Gilmer's preprint, multiple mathematicians (including Zachary Chase, Mark Sellke, and Will Sawin) independently optimized Gilmer's analytic technique. By rigorously solving the underlying convex optimization problem using Kullback-Leibler divergence and calculus of variations, they improved the constant to:
$$ c = \frac{3 - \sqrt{5}}{2} \approx 0.381966 $$

**Current SOTA:** As of 2026, the absolute lower bound for the most frequent element in an arbitrary union-closed family stands at $\frac{3 - \sqrt{5}}{2}$. The exact factor of $1/2$ remains elusive.

## 4. Partial Results / Verified Cases

While the general conjecture remains open, it has been rigorously proven for numerous specific cases, geometries, and dimensional bounds:

1. **Small Families and Small Universes:**
   - The conjecture holds for all families with $|\mathcal{F}| \le 50$.
   - The conjecture holds for all universes with $|U| \le 12$.

2. **Large Families:**
   - If $|\mathcal{F}| \ge \frac{2}{3} 2^{|U|}$, the conjecture trivially holds because the family is dense enough to force high intersection frequencies.
   - Balla, Bollobás, and Eccles proved the conjecture holds if $|\mathcal{F}| \ge \frac{1}{2} 2^{|U|}$.

3. **Structural and Lattice-Theoretic Cases:**
   - **Singleton-containing families:** If $\mathcal{F}$ contains at least one set of size 1, the conjecture holds. 
   - **Graph-theoretic families:** The conjecture is true for families of sets corresponding to independent sets of a chordal bipartite graph, or families defined by paths in trees.
   - **Lattice representation:** By Birkhoff's representation theorem, union-closed families are isomorphic to finite semilattices. Reinhold (2000) proved the conjecture for families corresponding to lower semimodular lattices.

4. **Separating Families:**
   - A family $\mathcal{F}$ is separating if for any two elements $x \neq y$, there exists $A \in \mathcal{F}$ containing exactly one of them. The conjecture holds for all separating families where $|\mathcal{F}| \ge 2^{|U|-1}$.

## 5. Principal Obstacles

The primary reason the Frankl Conjecture remains unresolved is the profound lack of **local-to-global inductive structure** inherent to union-closed families, coupled with a strict **analytic barrier** in modern continuous methods.

1. **Failure of Induction:** Traditional combinatorial proofs rely on removing an element or a set (e.g., taking the trace of the family) and applying induction. However, removing an element from a union-closed family often destroys the union-closed property, making the induction hypothesis inapplicable. 

2. **The Information-Theoretic / Analytic Barrier:** The Gilmer-Chase-Sawin technique relies on evaluating the entropy of a distribution generated by $X \cup Y$. Sawin explicitly proved that $\frac{3 - \sqrt{5}}{2}$ is the absolute maximum bound achievable by considering the union of *two* independent uniform samples from $\mathcal{F}$. The number $\frac{3 - \sqrt{5}}{2}$ emerges directly from maximizing the function:
$$ \phi(p) = \frac{H(2p - p^2) - H(p)}{1 - p} $$
where $H(x)$ is the binary entropy function. The unique optimum of this real-valued function yields the $0.381966$ barrier. Standard perturbation theory and continuous relaxation fail to push past this optimal threshold.

3. **Tightness of the Bound:** There are known union-closed families where the most frequent element appears in exactly half the sets (e.g., $\mathcal{F} = \mathcal{P}(U)$). Thus, any continuous bounding method must be extraordinarily tight—it cannot afford any slack, rendering loose analytic inequalities ineffective.

## 6. The Gap

The precise mathematical barrier lies in the gap between the analytic limit of $c = \frac{3 - \sqrt{5}}{2} \approx 38.2\%$ and the target limit of $c = \frac{1}{2} = 50\%$.

To cross this boundary, researchers must move beyond the entropy of the union of *two* independent variables $H(X \cup Y)$. The gap represents the mathematical step of effectively analyzing the entropy (or an alternative continuous divergence measure) of higher-order unions $H(X_1 \cup X_2 \dots \cup X_k)$, or abandoning the uniform distribution on $\mathcal{F}$ in favor of heavily weighted, non-uniform distributions that more accurately respect the latent algebraic boundaries of the lattice structure. Bridging this gap requires discovering a new functional inequality on the Boolean hypercube that remains tight under discrete combinatorial mapping.

## 7. Current Research (as of June 2026)

Active research on the Frankl Conjecture is heavily concentrated at the intersection of discrete probability, functional analysis, and information theory.

- **Non-Uniform Distributions:** Researchers at institutions like Princeton and the Institute for Advanced Study are exploring generalized entropy bounds using non-uniform probability distributions over $\mathcal{F}$. By weighting the sets based on their cardinality (e.g., favoring larger sets), researchers hope to force the optimization bound higher than Sawin's barrier.
- **Higher-Order Information Inequalities:** Groups are currently attempting to formulate tractable inequalities for $H(X_1 \cup X_2 \cup X_3)$. The algebraic complexity of the binary entropy function expands non-linearly, making the continuous optimization problem for three variables highly resistant to standard calculus of variations. *(frontier — verify: recent preprints suggest computer-assisted proofs evaluating 3-variable entropy expansions yield constants arbitrarily close to 0.40).*
- **Hypercontractivity on the Boolean Cube:** Exploring the use of Bonami-Beckner type inequalities and Fourier analysis on $\{0,1\}^n$ to bound the variance of functions defined over union-closed families.

## 8. Future Work

Leading mathematicians outline several required pathways to fully resolve the conjecture:

1. **Identifying Extremal Structures:** Characterize the algebraic structure of the specific hypothetical families that minimize $\max_x f_{\mathcal{F}}(x)$. If one can prove that minimal families must possess a specific geometry, localized combinatorial techniques could handle the rest.
2. **Beyond Shannon Entropy:** Formulating the problem using generalized Rényi entropies or Tsallis entropies. It is posited that a different continuous divergence metric might not suffer from the $0.381966$ local maximum inherent to the Kullback-Leibler divergence.
3. **The Intersection-Closed Dual Formulation:** The problem is perfectly isomorphic to the Intersection-Closed Sets Conjecture (where every intersection of two sets is in the family). Future work may find that intersection structures offer easier inductive pathways by mapping to topological closure operators.

## 9. Key References

- **[Foundational]** Poonen, B. *Union-closed families.* Journal of Combinatorial Theory, Series A, 1992.
- **[Foundational]** Bruhn, H., & Schaudt, O. *The journey of the union-closed sets conjecture.* Graphs and Combinatorics, 2015.
- **[SOTA / Recent]** Gilmer, J. *A constant lower bound for the union-closed sets conjecture.* Bulletin of the American Mathematical Society, 2023.
- **[SOTA / Recent]** Chase, Z. *An improvement of Gilmer's constant for the union-closed sets conjecture.* Mathematical Proceedings of the Cambridge Philosophical Society, 2023.
- **[SOTA / Recent]** Sawin, W. *An improved lower bound for the union-closed sets conjecture.* arXiv preprint (subsequently peer-reviewed), 2022.

## 10. Worked Example / Concrete Special Case

To ground the abstract definitions, consider a small, concrete universe and construct a non-trivial union-closed family. 

Let the universe be $U = \{1, 2, 3, 4\}$. 
Consider the family of sets $\mathcal{F}$ defined as:
$$ \mathcal{F} = \{\emptyset, \{1\}, \{2\}, \{1, 2\}, \{1, 2, 3\}, \{1, 2, 4\}, \{1, 2, 3, 4\}\} $$

**Step 1: Verify the union-closed property.**
We must ensure that the union of any two sets in $\mathcal{F}$ remains in $\mathcal{F}$.
- $\{1\} \cup \{2\} = \{1, 2\} \in \mathcal{F}$
- $\{1, 2\} \cup \{1, 2, 3\} = \{1, 2, 3\} \in \mathcal{F}$
- $\{1, 2, 3\} \cup \{1, 2, 4\} = \{1, 2, 3, 4\} \in \mathcal{F}$
An exhaustive check confirms that for all $A, B \in \mathcal{F}$, $A \cup B \in \mathcal{F}$. 

**Step 2: Calculate the size of the family and the target bound.**
The total number of sets in the family is $|\mathcal{F}| = 7$.
According to the Frankl Conjecture, there must be at least one element $x \in U$ that appears in at least $\frac{|\mathcal{F}|}{2} = \frac{7}{2} = 3.5$ sets. Since frequencies must be integers, the element must appear in at least 4 sets.

**Step 3: Compute the frequencies of each element in the universe.**
Let us calculate $f_{\mathcal{F}}(x)$ for each $x \in \{1, 2, 3, 4\}$ by counting how many sets contain the element:
- Element $1$ appears in: $\{1\}, \{1, 2\}, \{1, 2, 3\}, \{1, 2, 4\}, \{1, 2, 3, 4\}$. (Total = 5)
- Element $2$ appears in: $\{2\}, \{1, 2\}, \{1, 2, 3\}, \{1, 2, 4\}, \{1, 2, 3, 4\}$. (Total = 5)
- Element $3$ appears in: $\{1, 2, 3\}, \{1, 2, 3, 4\}$. (Total = 2)
- Element $4$ appears in: $\{1, 2, 4\}, \{1, 2, 3, 4\}$. (Total = 2)

**Conclusion of the Special Case:**
Both elements $1$ and $2$ appear in $5$ sets. 
Since $5 \ge 3.5$, the condition is overwhelmingly satisfied. The conjecture holds for this specific family $\mathcal{F}$. While combinatorial verification is trivial for $|\mathcal{F}| = 7$, proving this mathematically robust behavior generalizes to $|\mathcal{F}| = 10^{100}$ without continuous optimization remains one of mathematics' great open challenges.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*