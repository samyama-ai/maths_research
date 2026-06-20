---
id: 10-theoretical-cs/p-vs-np
title: "P vs NP"
topic: 10-theoretical-cs
status: open
first_added: 2026-06
last_reviewed: 2026-06
last_substantive_update: 2026-06
stale_since: ""
provenance: synthesized
---

# P vs NP

> **Topic:** Theoretical Computer Science · **ID:** `10-theoretical-cs/p-vs-np` · **Status:** open

## 1. Problem Statement / Conjecture

The $\mathbf{P}$ vs $\mathbf{NP}$ problem asks whether every language that can be decided in polynomial time by a non-deterministic Turing machine can also be decided in polynomial time by a deterministic Turing machine.

Formally:
$$\mathbf{P} \stackrel{?}{=} \mathbf{NP}$$

## 2. Mathematical Foundations

Let $\Sigma$ be a finite alphabet. A language $L \subseteq \Sigma^*$ is in $\mathbf{P}$ if there exists a deterministic Turing machine $M$ and a polynomial $p(n)$ such that:
1. $M$ runs for at most $p(|x|)$ steps on input $x$.
2. $M(x) = 1 \iff x \in L$.

A language $L$ is in $\mathbf{NP}$ if there exists a deterministic Turing machine $V$ (the verifier) and a polynomial $p(n)$ such that:
1. $V$ runs for at most $p(|x|)$ steps on input $(x, y)$.
2. $x \in L \iff \exists y \in \Sigma^*$ with $|y| \leq p(|x|)$ such that $V(x, y) = 1$.

The string $y$ is called a *certificate* or *witness*.

A language $L$ is $\mathbf{NP}$-complete if:
1. $L \in \mathbf{NP}$.
2. For every $L' \in \mathbf{NP}$, there is a polynomial-time mapping reduction $L' \leq_p L$.

## 3. History & State of the Art (SOTA)

* **1971**: Stephen Cook published *The Complexity of Theorem-Proving Procedures*, showing that the Boolean Satisfiability problem (SAT) is $\mathbf{NP}$-complete.
* **1972**: Richard Karp published a paper proving 21 diverse combinatorial problems are $\mathbf{NP}$-complete.
* **1973**: Leonid Levin independently proved that SAT and several other problems are $\mathbf{NP}$-complete (the Cook-Levin theorem).
* **Conjecture**: The overwhelming consensus in theoretical computer science is that $\mathbf{P} \neq \mathbf{NP}$.

## 4. Partial Results / Verified Cases

* **Relativization Barrier (1975)**: Baker, Gill, and Solovay showed that there exist oracles $A$ and $B$ such that $\mathbf{P}^A = \mathbf{NP}^A$ and $\mathbf{P}^B \neq \mathbf{NP}^B$. This implies that any proof resolving $\mathbf{P}$ vs $\mathbf{NP}$ must not "relativize" (i.e., it cannot rely on methods that remain valid when oracle access is introduced).
* **Natural Proofs Barrier (1997)**: Razborov and Rudich proved that a wide class of circuit lower bound techniques (called "natural proofs") cannot prove $\mathbf{P} \neq \mathbf{NP}$, assuming that strong pseudorandom generators exist.
* **Algebrization Barrier (2008)**: Aaronson and Wigderson extended relativization to show that proof techniques must also not algebrize.

## 5. Principal Obstacles

The three barriers (Relativization, Natural Proofs, Algebrization) rule out almost all standard techniques in computability and complexity theory. Diagnonalization, circuit complexity lower bounds, and simple arithmetization are insufficient to separate the classes.

## 6. The Gap

The gap is between the best known upper bounds for solving $\mathbf{NP}$-complete problems (typically exponential time, e.g., $2^{O(n)}$ for SAT) and the best known unconditional lower bounds for these problems on general computation models (which are only linear, e.g., $O(n)$).

## 7. Current Research (as of June 2026)

* **Geometric Complexity Theory (GCT)**: An algebraic geometry program proposed by Ketan Mulmuley and Milind Sohoni that aims to show $\mathbf{P} \neq \mathbf{NP}$ by showing that certain group-theoretic representations do not occur as sub-representations of others.
* **Fine-Grained Complexity**: Studying the exact exponents of polynomial-time algorithms to find tight relationships under assumptions like the Strong Exponential Time Hypothesis (SETH).

## 8. Future Work

* Developing non-relativizing and non-natural proof techniques.
* Formulating concrete representation-theoretic obstructions in GCT.

## 9. Key References

- **[Foundational]** Cook, Stephen. *The complexity of theorem-proving procedures.* Proceedings of the third annual ACM symposium on Theory of computing, 1971.
- **[Foundational]** Karp, Richard M. *Reducibility among combinatorial problems.* Complexity of Computer Computations, 1972.
- **[Survey]** Aaronson, Scott. *P =? NP.* Open Problems in Mathematics, Springer, 2016.

## 10. Worked Example / Concrete Special Case

Consider the difference between **2-SAT** and **3-SAT**.

A Boolean formula in Conjunctive Normal Form (CNF) consists of clauses joined by $\land$ (AND), where each clause is a disjunction ($\lor$, OR) of literals.

* **2-SAT**: Every clause contains exactly 2 literals (e.g., $(x_1 \lor \bar{x_2}) \land (x_2 \lor x_3)$).
  * 2-SAT is solvable in polynomial time: we can construct an implication graph where each clause $(a \lor b)$ is represented by directed edges $\bar{a} \to b$ and $\bar{b} \to a$. Finding strongly connected components using Tarjan's algorithm takes $O(V + E)$ time. Thus, **2-SAT $\in \mathbf{P}$**.
  
* **3-SAT**: Every clause contains exactly 3 literals (e.g., $(x_1 \lor \bar{x_2} \lor x_3)$).
  * **3-SAT is $\mathbf{NP}$-complete**. Despite only increasing the clause size by 1 literal, no polynomial-time algorithm is known, and any instance can encode any NP computation.

This illustrates how a minor structural shift transitions a problem from deterministic polynomial-time solvability ($\mathbf{P}$) to universal verification difficulty ($\mathbf{NP}$-complete).

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*
