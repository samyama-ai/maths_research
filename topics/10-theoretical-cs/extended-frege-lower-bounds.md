---
id: 10-theoretical-cs/extended-frege-lower-bounds
title: "Extended Frege Lower Bounds"
topic: 10-theoretical-cs
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Extended Frege Lower Bounds

> **Topic:** Theoretical Computer Science · **ID:** `10-theoretical-cs/extended-frege-lower-bounds` · **Status:** open

## 1. Problem Statement / Conjecture

The Extended Frege (EF) lower bound problem asks whether there exists a sequence of propositional tautologies for which the Extended Frege proof system requires super-polynomial proof sizes. 

Formally, a propositional proof system is a polynomial-time computable function $f : \Sigma^* \to \text{TAUT}$, where $\text{TAUT}$ is the set of all propositional tautologies. The size of a proof $\pi$ is its length in symbols, $|\pi|$. The conjecture states that for the Extended Frege system, there exists a family of tautologies $\{\tau_n\}_{n=1}^{\infty}$ of length $|\tau_n| = \Theta(n)$ such that for any valid EF proof $\pi_n$ where $f(\pi_n) = \tau_n$, the size of the proof is bounded below by a super-polynomial function:
$$ |\pi_n| = n^{\omega(1)} $$

Equivalently, proving this conjecture asserts that EF is not a polynomially bounded proof system. By Cook and Reckhow's foundational theorem (1979), demonstrating that *no* propositional proof system is polynomially bounded is unconditionally equivalent to proving $\text{NP} \neq \text{coNP}$. Establishing super-polynomial lower bounds for EF represents one of the highest barriers in structural complexity theory, as EF encapsulates polynomial-time reasoning.

## 2. Mathematical Foundations

Let $\mathcal{F}$ denote a standard **Frege system**. A Frege system is defined over a functionally complete basis of Boolean connectives (e.g., $\{\wedge, \vee, \neg\}$). It consists of a finite set of axiom schemas and inference rules that are implicationally sound and complete. A classic example includes schemas such as $A \rightarrow (B \rightarrow A)$ and the Modus Ponens inference rule:
$$ \frac{A \quad A \rightarrow B}{B} $$

A proof of a formula $\phi$ in $\mathcal{F}$ is a sequence of formulas $\phi_1, \phi_2, \dots, \phi_m = \phi$ where each $\phi_i$ is either an instantiated axiom or derived from previous formulas via an inference rule. The size of the proof is $\sum_{i=1}^m |\phi_i|$, where $|\phi_i|$ is the number of symbols. A Frege system operates intrinsically on Boolean *formulas* (trees).

An **Extended Frege (EF)** system augments $\mathcal{F}$ by introducing the *extension rule*. At any step $k$ in the proof, one may introduce a novel, previously unused extension variable $p_k$ via the defining axiom:
$$ p_k \leftrightarrow \psi $$
where $\psi$ is a formula constructed from original variables and previously defined extension variables $p_j$ ($j < k$). 

The extension rule allows EF to abbreviate complex recurring subformulas, effectively enabling the system to reason over Boolean *circuits* (directed acyclic graphs) rather than just formulas. Consequently, Frege is computationally associated with the complexity class $NC^1$, whereas Extended Frege is associated with general polynomial-size circuits, $P/poly$. EF is polynomially equivalent to Extended Resolution (ER), introduced by Tseitin. 

## 3. History & State of the Art (SOTA)

The formal framework of propositional proof complexity was established by Stephen Cook and Robert Reckhow in 1979. They formulated the "Cook's Program": a step-by-step approach to proving $\text{NP} \neq \text{coNP}$ by proving super-polynomial lower bounds for increasingly powerful proof systems. 

Historically, proof complexity has successfully advanced through weaker systems. In 1985, Haken proved exponential lower bounds for the Resolution system. In 1988, Ajtai broke the barrier for bounded-depth Frege ($AC^0$-Frege), with exponential bounds solidified by Pitassi, Beame, and Impagliazzo (1993), and Krajíček, Pudlák, and Woods (1995). 

However, the State of the Art (SOTA) halts abruptly at systems capable of counting. As of the present, researchers possess **zero** super-polynomial lower bounds for Extended Frege. Remarkably, there are no super-polynomial lower bounds known even for standard Frege systems. The boundary of our ignorance begins at $TC^0$-Frege (Frege with threshold/counting gates) and extends upward to standard Frege, Extended Frege, and quantified propositional calculus.

## 4. Partial Results / Verified Cases

While EF remains completely unassailable, researchers have achieved robust lower bounds for structurally restricted subsystems. These verified cases highlight the exact limits of current mathematical techniques:

- **Resolution and Extended Resolution:** Haken (1985) proved that Resolution requires size $2^{\Omega(n)}$ to prove the Pigeonhole Principle ($PHP_n^{n+1}$). However, Tseitin (1968) and Cook (1976) demonstrated that *Extended* Resolution (and thus EF) can prove $PHP_n^{n+1}$ in polynomial size $O(n^4)$.
- **Bounded-Depth Frege ($AC^0$-Frege):** Using Håstad's Switching Lemma, it has been verified that $AC^0$-Frege requires exponential size to prove the Parity Principle and the weak Pigeonhole Principle.
- **Cutting Planes (CP):** Pudlák (1997) proved exponential lower bounds for CP (which uses linear inequalities) by evaluating the Clique-Coloring tautologies.
- **Monotone Extended Frege:** If the EF extension rule is strictly confined to monotone formulas (restricting negations strictly to the leaves), exponential lower bounds can be rigorously established. Hrubeš (2007) achieved this by leveraging monotone feasible interpolation.
- **Algebraic Systems:** Exponential lower bounds are known for bounded-degree Polynomial Calculus (Razborov, 1998) and fixed-degree Sum-of-Squares / Positivstellensatz algorithms (Grigoriev, 2001) for random 3-SAT instances.

## 5. Principal Obstacles

The mathematical wall defending Extended Frege is grounded in its equivalence to $P/poly$. Proving an EF lower bound is intrinsically coupled with proving boolean circuit lower bounds, inheriting all profound obstacles from computational complexity:

1. **Failure of Feasible Interpolation:** Krajíček and Pudlák introduced the interpolation technique: if a system has a short proof of a tautology $A(x,y) \vee B(x,z)$ (where $A$ and $B$ cannot both be false), one can construct a small circuit separating inputs satisfying $A$ from inputs satisfying $B$. For Resolution, this yields monotone boolean circuits, leading to lower bounds. For EF, the interpolating circuits are general $P/poly$ circuits. Krajíček and Pudlák (1997), alongside Bonet, Pitassi, and Raz, proved that if strong cryptography exists (e.g., integer factoring is hard for $P/poly$), feasible interpolation for EF *must* fail.
2. **The Natural Proofs Barrier:** Razborov and Rudich's Natural Proofs barrier (1997) asserts that standard combinatorial techniques cannot prove strong circuit lower bounds without inadvertently breaking pseudo-random generators (PRGs). Because EF is powerful enough to formalize the reasoning of $P/poly$, it is theoretically capable of "understanding" and internalizing the proofs of cryptographic PRGs. Consequently, bounds against EF must avoid logical formulations of Natural Proofs.
3. **Lack of Structural Bottlenecks:** Weaker systems like Resolution or $AC^0$-Frege restrict the depth or the arity of the clauses. Håstad's Switching Lemma destroys $AC^0$ circuits by hitting them with random restrictions. EF circuits (and formulas in Frege) have unrestricted depth, making random restriction techniques completely ineffective.

## 6. The Gap

The precise mathematical gap is between constant-depth formula logic ($AC^0$-Frege) and logarithmic-depth formula logic (standard Frege / $NC^1$). 

The exact next barrier to cross is **$AC^0[p]$-Frege**: bounded-depth Frege systems augmented with modular counting axioms (e.g., Mod-2 or parity gates). Smolensky and Razborov famously proved in 1987 that $AC^0[p]$ circuits cannot compute the Majority function. Yet, we entirely lack the proof-complexity analogue. We cannot yet prove that an $AC^0[2]$-Frege system requires super-polynomial size to prove the Pigeonhole Principle. Closing the gap requires translating the algebraic Razborov-Smolensky polynomial approximations of boolean circuits into valid syntactic proof deductions.

## 7. Current Research (as of June 2026)

Current research operates along two primary axes aiming to bypass the cryptographic barriers of EF:

- **Algebraic Proof Systems (IPS):** Grochow and Pitassi (2018) formalized the Ideal Proof System (IPS), translating propositional proof lower bounds into algebraic circuit lower bounds (e.g., the permanent polynomial). Research heavily targets proving lower bounds for restricted IPS models (like multi-linear IPS), operating on the hypothesis that algebraic geometry and invariant theory (via the Geometric Complexity Theory program) can circumvent the Natural Proofs barrier. *(frontier — verify: recent preprints claim sub-exponential lower bounds for bounded-depth IPS via shifted partial derivatives).*
- **Proof Complexity Generators (Hard Tautologies):** Krajíček (2011) and Alekhnovich et al. (2004) proposed generating hard tautologies using cryptographic pseudorandom generators. Given a PRG $G : \{0,1\}^n \to \{0,1\}^m$ ($m > n$), the propositional formula $\tau(b)$ asserting "$b \notin \text{Im}(G)$" is a tautology for most strings $b$. Current schools of thought (e.g., at the Institute for Advanced Study and Charles University) study whether Nissan-Wigderson generators based on hard functions can explicitly yield EF lower bounds. 
- **Lifting Theorems:** A prevailing trend uses "lifting" to transfer query/communication complexity lower bounds to proof size lower bounds (e.g., Göös, Pitassi, Watson 2015). Researchers are actively searching for a suitable communication game that perfectly characterizes EF to allow lifting techniques to apply.

## 8. Future Work

Leading theoreticians outline the following pathways to eventually break the Extended Frege lower bound:

1. **Resolution of $AC^0[p]$ and $TC^0$ Frege:** Before attacking standard or Extended Frege, researchers suggest proving lower bounds for threshold logic ($TC^0$-Frege). Identifying tautologies based on expander graph properties or matrix multiplication identities that are hard for $TC^0$ is a critical stepping stone.
2. **Automating Circuit Lower Bounds:** Since EF lower bounds imply $P/poly$ lower bounds, researchers suggest formulating tautologies that encode the statement "$SAT \notin P/poly$". Understanding how EF fails to prove circuit lower bounds about itself (a meta-mathematical approach) could yield structural weaknesses in the extension rule.
3. **Algebraization of Frege:** Transforming the Boolean axioms of standard Frege into completely algebraic identities over finite fields, and attempting to apply degree-bounding arguments to the resulting ideal memberships, heavily bridging proof complexity with algebraic geometry.

## 9. Key References

- **[Foundational]** Cook, S. A., & Reckhow, R. A. *The relative efficiency of propositional proof systems.* Journal of Symbolic Logic, 44(1), 36-50, 1979.
- **[Foundational]** Krajíček, J., & Pudlák, P. *Some consequences of cryptographical conjectures for $S^1_2$ and EF.* Information and Computation, 140(1), 82-94, 1997.
- **[SOTA / Recent]** Grochow, J. A., & Pitassi, T. *Circuit complexity, proof complexity, and polynomial identity testing: The ideal proof system.* Journal of the ACM (JACM), 65(6), 1-59, 2018.
- **[SOTA / Recent]** Göös, M., Pitassi, T., & Watson, T. *Deterministic communication vs. partition number.* In Proceedings of the 56th Annual IEEE Symposium on Foundations of Computer Science (FOCS), 1077-1088, 2015.
- **[Survey]** Krajíček, J. *Proof Complexity.* Encyclopedia of Mathematics and its Applications. Cambridge University Press, 2019.
- **[Survey]** Razborov, A. A. *Lower bounds for propositional proofs and Boolean circuits.* In Proceedings of the International Congress of Mathematicians, Vol. 1, 47-60, 1995.

## 10. Worked Example / Concrete Special Case

To ground the power of the Extended Frege extension rule, consider the **Pigeonhole Principle** ($PHP_n^{n+1}$), stating there is no injective map from $n+1$ pigeons to $n$ holes. 

We formalize $PHP_n^{n+1}$ with boolean variables $x_{i,j}$ (pigeon $i$ is in hole $j$, for $i \in \{1,\dots,n+1\}, j \in \{1,\dots,n\}$). The tautology $\tau_{PHP}$ is the negation of:
$$ \left( \bigwedge_{i=1}^{n+1} \bigvee_{j=1}^n x_{i,j} \right) \wedge \left( \bigwedge_{i \neq i'} \bigwedge_{j=1}^n (\neg x_{i,j} \vee \neg x_{i',j}) \right) $$

Any standard Resolution proof of this requires size $2^{\Omega(n)}$. A Frege system can prove this by creating complex formulas to count pigeons. However, Extended Frege (EF) achieves a highly concise polynomial-size proof ($O(n^4)$) by using the extension rule to natively "build circuits" that compute arithmetic sums.

EF introduces new variables $S_{m,k}$ to represent the proposition: "there are exactly $k$ pigeons residing in the first $m$ holes." EF defines these recursively using the extension rule:
$$ S_{m,k} \leftrightarrow \left( S_{m-1, k} \wedge \text{hole } m \text{ is empty} \right) \vee \left( S_{m-1, k-1} \wedge \text{hole } m \text{ has 1 pigeon} \right) $$
By defining these intermediate nodes, EF evaluates the sum of pigeons exactly like a dynamic programming algorithm or a carry-save adder circuit. The proof then easily derives a contradiction by concluding that $S_{n, n+1}$ must be true (which is structurally impossible since $n$ holes can hold at most $n$ pigeons without collisions). 

This demonstrates how EF's extension rule mimics polynomial-time algorithmic computation, collapsing exponential-sized brute-force search trees into elegant, polynomial-sized arithmetic verifications. Finding a tautology that EF *cannot* compress in this manner remains the grand challenge.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*