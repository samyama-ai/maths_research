---
id: 07-combinatorics/cayley-graph-isomorphism-problem
title: "Cayley Graph Isomorphism Problem"
topic: 07-combinatorics
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Cayley Graph Isomorphism Problem

> **Topic:** Combinatorics & Graph Theory · **ID:** `07-combinatorics/cayley-graph-isomorphism-problem` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

The Cayley Graph Isomorphism Problem investigates the exact conditions under which the combinatorial equivalence (graph isomorphism) of two Cayley graphs over the same group implies an algebraic equivalence (group automorphism). The problem partitions into two tightly coupled challenges:

1. **The Structural Problem (Classification of CI-Groups):** For which finite groups $G$ is it true that any two Cayley graphs on $G$ are isomorphic if and only if they are mapped to each other by an automorphism of $G$? Such groups are designated as *Cayley Isomorphism groups* (CI-groups). The overarching conjecture is that CI-groups form a highly restricted, completely classifiable family of groups (predominantly cyclic, elementary abelian, or small direct products thereof), and the exact threshold where the CI-property fails for elementary abelian groups $\mathbb{Z}_p^d$ must be explicitly derived.
2. **The Computational Problem (Algorithmic Complexity):** Does there exist a deterministic polynomial-time algorithm, operating in $O(n^c)$ time, to decide whether two given Cayley graphs $X(G, S)$ and $X(G, T)$ are isomorphic? The core conjecture asserts that for any abelian group $G$, isomorphism testing is in the complexity class $\text{P}$, achievable through high-dimensional Weisfeiler-Leman stabilization.

A complete resolution requires both a definitive algebraic taxonomy of all finite CI-groups and a polynomial-time separation protocol for non-CI Cayley graphs.

## 2. Mathematical Foundations

Let $G$ be a finite group and let $S \subseteq G$ be a connection set. For undirected graphs, we require that the identity element is not in the set, $1_G \notin S$, and that the set is symmetric, $S = S^{-1}$. The **Cayley graph** $X = \text{Cay}(G, S)$ is defined by the vertex set $V(X) = G$ and the edge set:
$$E(X) = \{(g, gs) \mid g \in G, s \in S\}$$

The group $G$ acts on $X$ by right multiplication. The right regular representation $R : G \to \text{Sym}(G)$, defined by $R_g(x) = xg$, embeds $G$ as a regular permutation subgroup $G_R \le \text{Sym}(G)$. By construction, $G_R$ is a subgroup of the full automorphism group of the graph, meaning $G_R \le \text{Aut}(X)$.

Two Cayley graphs $X = \text{Cay}(G, S)$ and $Y = \text{Cay}(G, T)$ are isomorphic if there exists a bijection $\sigma \in \text{Sym}(G)$ such that $\sigma(E(X)) = E(Y)$. If such a $\sigma$ can be chosen from the automorphism group of the underlying group, $\sigma \in \text{Aut}(G)$, then $X$ and $Y$ are said to be **Cayley isomorphic**.

A graph $X = \text{Cay}(G, S)$ is defined as a **CI-graph** if, for every $T \subseteq G$, the isomorphism $\text{Cay}(G, S) \cong \text{Cay}(G, T)$ guarantees that the graphs are Cayley isomorphic (i.e., there exists $\alpha \in \text{Aut}(G)$ such that $\alpha(S) = T$). A group $G$ is a **CI-group** if every Cayley graph on $G$ is a CI-graph.

The structural foundation of the problem rests on **Babai's Conjugacy Criterion** (1977): 
A Cayley graph $X = \text{Cay}(G, S)$ is a CI-graph if and only if every regular subgroup $H \le \text{Aut}(X)$ that is isomorphic to $G$ is conjugate to $G_R$ within $\text{Aut}(X)$. Thus, the combinatorial problem of graph isomorphism is exactly translated into a purely algebraic problem of subgroup conjugacy within permutation groups.

To study these permutation groups computationally and algebraically, one utilizes **Schur rings (S-rings)**. A subring $\mathfrak{S}$ of the group algebra $\mathbb{C}[G]$ is an S-ring over $G$ if there exists a partition $\mathcal{T} = \{T_0, T_1, \dots, T_d\}$ of $G$ satisfying:
1. $T_0 = \{1_G\}$.
2. For every $i$, there exists $j$ such that $T_i^{-1} = \{t^{-1} \mid t \in T_i\} = T_j$.
3. The linear span is closed under multiplication: $\underline{T_i} \cdot \underline{T_j} = \sum_{k=0}^d p_{ij}^k \underline{T_k}$, where $\underline{T_i} = \sum_{t \in T_i} t \in \mathbb{C}[G]$, and $p_{ij}^k \in \mathbb{Z}_{\ge 0}$ are intersection numbers.

The equivalence of S-rings forms the primary obstruction and mechanism for algorithmically deciding Cayley graph isomorphism.

## 3. History & State of the Art (SOTA)

The genesis of the problem traces to 1967 when A. Ádám conjectured that all finite cyclic groups are CI-groups. This became known as Ádám's Conjecture and served as the catalyst for algebraic graph theory.

- **1970:** B. Elspas and J. Turner provided the first counterexample to Ádám's conjecture by explicitly constructing non-isomorphic connection sets for $\mathbb{Z}_8$, proving it is not a CI-group.
- **1977:** L. Babai formulated the overarching Cayley Graph Isomorphism Problem and published the foundational theorem equating the CI-property to the conjugacy of regular subgroups in the symmetric group.
- **1987:** P. Pálfy analyzed the CI-property for general relational structures (where the arity of the relation is unrestricted, unlike graphs which are binary relations). He proved a group $G$ is a universal CI-group if and only if $|G| = 4$ or $\gcd(|G|, \phi(|G|)) = 1$, where $\phi$ is Euler's totient function.
- **1995–1997:** M. Muzychuk resolved the remaining open fragments of Ádám's conjecture, fully classifying cyclic CI-groups utilizing S-ring theory.
- **2002:** C. H. Li published a seminal survey summarizing decades of partial results and presenting a presumed asymptotic taxonomy of general CI-groups.
- **2004:** In a major algorithmic breakthrough, S. Evdokimov and I. Ponomarenko (and independently M. Muzychuk) proved that isomorphism of circulant graphs (Cayley graphs of cyclic groups) can be decided in polynomial time.
- **2011:** G. Somlai dramatically shifted the structural landscape. It had been widely hypothesized that elementary abelian $p$-groups $\mathbb{Z}_p^d$ might all be CI-groups. Somlai proved they are strictly *not* CI-groups for $d \ge 2p+3$, reopening a massive gap in the classification taxonomy.
- **2015:** L. Babai established that the general Graph Isomorphism problem is in quasipolynomial time $O(\exp(\log^c n))$. While this subsumes Cayley graphs, pushing the complexity down to polynomial time $O(n^c)$ for abelian and nilpotent groups remains the state of the art objective.

## 4. Partial Results / Verified Cases

While the general problem remains open, several critical boundaries have been permanently established:

- **Cyclic Groups:** A cyclic group $\mathbb{Z}_n$ is a CI-group for graphs if and only if $n = k, 2k$, or $4k$, where $k$ is an odd square-free integer (Muzychuk, 1995).
- **Elementary Abelian Groups:** For $G = \mathbb{Z}_p^d$ (where $p$ is an odd prime), $G$ is verified to be a CI-group for $d \le 4$ (proven across successive papers by Dobson, Hirasaka, and Muzychuk). Conversely, $G$ is known *not* to be a CI-group for $d \ge 2p+3$ (Somlai, 2011).
- **Dihedral Groups:** A dihedral group $D_n$ is a CI-group if and only if $n$ is an odd square-free integer (Babai, 1977).
- **Simple Groups:** Non-abelian simple groups are never CI-groups. In fact, the alternating group $A_n$ and symmetric group $S_n$ fail the CI-property for all $n \ge 5$.
- **Computational Tractability:** Deterministic polynomial-time isomorphism testing has been strictly verified for:
  - Graphs of bounded eigenvalue multiplicity or bounded degree.
  - Circulant graphs (Cayley graphs of $\mathbb{Z}_n$).
  - Cayley graphs of $\mathbb{Z}_p^2$ and $\mathbb{Z}_p^3$.

## 5. Principal Obstacles

The fundamental bottleneck preventing a complete structural classification is the breakdown of Sylow-like conjugacy theorems within arbitrary permutation groups. Sylow's theorems elegantly guarantee that $p$-subgroups of the exact same order are always conjugate within any finite group. However, Babai's criterion requires that two *regular* subgroups of the same isomorphism class be conjugate within $\text{Aut}(X)$. Because $\text{Aut}(X)$ is often a complex primitive permutation group constructed via wreath products or twisted wreath products (dictated by the O'Nan-Scott theorem), regular subgroups can embed in wildly non-conjugate ways. There is no natural algebraic forcing mechanism to guarantee their conjugacy.

Algorithmically, the barrier lies in the combinatorial stabilization of Schur rings. The standard polynomial-time technique for graph isomorphism is the Weisfeiler-Leman (WL) algorithm, which essentially computes the coherent configuration (or S-ring) generated by the graph's adjacency matrix. For Cayley graphs of non-cyclic abelian groups (like $\mathbb{Z}_p^d$), highly distinct and non-isomorphic connection sets can generate algebraically indistinguishable S-rings under 1-dimensional WL stabilization. Resolving these "pseudosymmetries" requires higher-dimensional WL algorithms, but identifying the exact dimension $k$ such that $k$-WL perfectly distinguishes all abelian Cayley graphs is mathematically intractable with current representation theory.

Furthermore, deciding the isomorphism of Cayley graphs of $\mathbb{Z}_p^d$ is polynomially equivalent to the Linear Code Equivalence problem, linking the geometric layout of the connection sets to the rigid subspace intersection geometries of error-correcting codes, a known computational hurdle.

## 6. The Gap

The exact boundary separating the solved cases from the open conjectures manifests in two explicit gaps:

1. **The Structural Gap (The Dimension Threshold):** For elementary abelian groups $\mathbb{Z}_p^d$, we know the CI-property holds for $d \le 4$ and fails for $d \ge 2p+3$. The precise integer threshold $d_{CI}(p)$ where the property collapses lies strictly in the window $5 \le d \le 2p+2$. Closing this gap—specifically determining if $\mathbb{Z}_p^5$ is a CI-group for primes $p \ge 5$—is the most immediate structural hurdle. Furthermore, the complete list of CI-groups among nilpotent groups of class 2 remains completely uncharacterized.
2. **The Algorithmic Gap:** Moving the isomorphism testing of arbitrary abelian Cayley graphs from Babai's quasipolynomial time $O(\exp(\log^c n))$ down to deterministic polynomial time $O(n^c)$. We lack a general polynomial-time S-ring decomposition protocol for direct products like $\mathbb{Z}_{p_1}^{a_1} \times \dots \times \mathbb{Z}_{p_k}^{a_k}$.

## 7. Current Research (as of June 2026)

Active research continues to probe the intersection of algebraic combinatorics and computational group theory. Leading schools of thought are heavily clustered at the Steklov Institute in St. Petersburg, the University of Western Australia, and various Hungarian research groups specializing in permutation groups.

Current methodologies focus on bounding the WL-dimension of abelian Cayley graphs utilizing the representation theory of association schemes. 
- *(frontier — verify)*: Recent preprints claim that the Weisfeiler-Leman dimension for Cayley graphs of elementary abelian $p$-groups is bounded by $O(d)$, mapping the problem to an $n^{O(d)}$ algorithm. 
- *(frontier — verify)*: There are active, highly technical computational searches attempting to explicitly construct non-conjugate regular subgroups in $\text{Sym}(p^5)$ to definitively prove that $\mathbb{Z}_p^5$ is not a CI-group for $p>3$, thereby truncating the Somlai gap.

## 8. Future Work

Prominent mathematicians in algebraic graph theory advocate for the following tactical pathways:
- **Resolve $\mathbb{Z}_p^5$:** Explicitly construct the automorphism group of a theoretical non-CI Cayley graph on $\mathbb{Z}_p^5$ utilizing twisted wreath products to prove the failure of the CI-property at dimension 5.
- **S-Ring Tensor Products:** Develop a rigorous generalized theory of S-ring tensor products that accurately captures the automorphism groups of direct products of Cayley graphs, escaping the linear code equivalence bottleneck.
- **Metacyclic Extensions:** Extend Muzychuk’s polynomial-time isomorphism algorithm from purely cyclic groups to metacyclic groups (groups possessing a normal cyclic subgroup where the resulting quotient is also cyclic).
- **Quantum Complexity:** Investigate the quantum computational complexity of the Cayley Graph Isomorphism Problem by mapping the S-ring intersection data to the Hidden Subgroup Problem (HSP) over non-abelian primitive groups.

## 9. Key References

- **[Foundational]** Babai, L. *Isomorphism problem for a class of point-symmetric structures.* Acta Mathematica Academiae Scientiarum Hungaricae, 1977.
- **[Foundational]** Muzychuk, M. *Ádám's conjecture is true in the square-free case.* Journal of Combinatorial Theory, Series A, 1995.
- **[SOTA / Recent]** Somlai, G. *Elementary abelian $p$-groups of rank $2p+3$ are not CI-groups.* Journal of Algebra, 2011.
- **[SOTA / Recent]** Evdokimov, S., Ponomarenko, I. *Recognizing and isomorphism testing of circulant graphs in polynomial time.* St. Petersburg Mathematical Journal, 2004.
- **[Survey]** Li, C. H. *On isomorphisms of finite Cayley graphs—a survey.* Discrete Mathematics, 2002.

## 10. Worked Example / Concrete Special Case

To concretely illustrate the CI-property, we examine Ádám's conjecture holding true for the cyclic group $G = \mathbb{Z}_5 = \{0, 1, 2, 3, 4\}$. 

Consider two distinct connection sets: 
$S = \{1, 4\}$ and $T = \{2, 3\}$.

We construct the two Cayley graphs, $X = \text{Cay}(\mathbb{Z}_5, S)$ and $Y = \text{Cay}(\mathbb{Z}_5, T)$.
- The edges of $X$ are formed by connecting each vertex $x$ to $x+1 \pmod 5$ and $x+4 \pmod 5$. This yields the edge set:
  $E(X) = \{(0,1), (1,2), (2,3), (3,4), (4,0)\}$
  This is a standard 5-cycle ($C_5$).
- The edges of $Y$ are formed by connecting each vertex $x$ to $x+2 \pmod 5$ and $x+3 \pmod 5$. This yields the edge set:
  $E(Y) = \{(0,2), (2,4), (4,1), (1,3), (3,0)\}$
  This is also a 5-cycle, meaning $X$ and $Y$ are clearly isomorphic as graphs ($X \cong Y$).

The CI-property asks: Does this graph isomorphism stem from an underlying *group automorphism* of $\mathbb{Z}_5$? The automorphisms of $\mathbb{Z}_5$ are given by multiplication by non-zero elements modulo 5. 

Let us test the automorphism $\alpha \in \text{Aut}(\mathbb{Z}_5)$ defined by $\alpha(x) = 2x \pmod 5$.
Apply $\alpha$ to the connection set $S = \{1, 4\}$:
- $\alpha(1) = 2 \times 1 = 2 \pmod 5$
- $\alpha(4) = 2 \times 4 = 8 \equiv 3 \pmod 5$

Thus, $\alpha(S) = \{2, 3\} = T$. Because the connection sets map directly to one another under a group automorphism, the graphs are Cayley isomorphic. The function $\alpha(x) = 2x \pmod 5$ maps every edge $(x, y) \in E(X)$ directly to $(2x, 2y) \in E(Y)$. For example, the edge $(1,2)$ in $X$ maps to $(2,4)$ in $Y$, preserving the adjacency.

Because every graph isomorphism between Cayley graphs of $\mathbb{Z}_5$ can be resolved this way into a group automorphism, $\mathbb{Z}_5$ is verified as a CI-group. (This perfectly aligns with Muzychuk's theorem, as $5 = k$ where $k$ is an odd square-free integer).

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*