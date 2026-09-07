---
id: 02-algebra-group-theory/dades-ordinary-conjecture
title: "Dade's Ordinary Conjecture"
topic: 02-algebra-group-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Dade's Ordinary Conjecture

> **Topic:** Algebra & Group Theory · **ID:** `02-algebra-group-theory/dades-ordinary-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Let $G$ be a finite group and $p$ a prime number. Let $B$ be a $p$-block of $G$. The $p$-defect of an ordinary irreducible character $\chi \in \operatorname{Irr}(G)$ is defined as $d(\chi) = v_p(|G|) - v_p(\chi(1))$, where $v_p$ is the $p$-adic valuation and $\chi(1)$ is the degree of the character.

**Dade's Ordinary Conjecture** asserts that if the $p$-core $O_p(G)$ is trivial, and the block $B$ has strictly positive defect, then for every integer $d \ge 0$, the following alternating sum evaluates to zero:

$$ \sum_{C \in \mathcal{R}_p(G)/G} (-1)^{|C|} k(N_G(C), B, d) = 0 $$

where:
- $\mathcal{R}_p(G)/G$ is the set of $G$-conjugacy classes of $p$-radical chains $C$.
- $|C|$ is the length of the chain $C$.
- $N_G(C)$ is the normalizer of the chain.
- $k(N_G(C), B, d)$ denotes the number of ordinary irreducible characters of $N_G(C)$ that have exact $p$-defect $d$ and belong to a $p$-block of $N_G(C)$ that induces (in the sense of Brauer) to the block $B$.

In essence, the conjecture claims that the number of irreducible characters of fixed defect in a block of a finite group can be completely determined by an alternating sum of character counts over local subgroups (normalizers of $p$-chains).

## 2. Mathematical Foundations

The conjecture bridges global representation theory with local $p$-structure dynamics. The formulation relies on several technical definitions:

**$p$-Blocks and Defect:**
The group algebra $\mathbb{C}[G]$ decomposes into a direct sum of indecomposable two-sided ideals called blocks. This induces a partition on the set of irreducible characters $\operatorname{Irr}(G)$. For a fixed prime $p$, these are the $p$-blocks. A block $B$ is associated with a defect group $D \le G$ (a $p$-subgroup), and the defect of the block is $d(B) = v_p(|D|)$. The conjecture applies only when $d(B) > 0$, meaning the block's defect group is non-trivial. 

**$p$-Radical Chains:**
A $p$-chain $C$ in $G$ is a strictly increasing sequence of $p$-subgroups:
$$ C : P_0 < P_1 < \dots < P_n $$
The length of this chain is $|C| = n$. The normalizer of the chain is the intersection of the normalizers of its components:
$$ N_G(C) = \bigcap_{i=0}^n N_G(P_i) $$
For a general group $G$, Dade defines a chain to be **radical** if $P_0 = O_p(G)$ (the largest normal $p$-subgroup of $G$) and for every $1 \le i \le n$, the subgroup $P_i$ satisfies:
$$ P_i = O_p(N_G(C_i)) $$
where $C_i$ is the truncated chain $P_0 < P_1 < \dots < P_i$. If $O_p(G) = 1$, then every radical chain starts with $P_0 = 1$. We denote the set of all radical $p$-chains by $\mathcal{R}_p(G)$. The group $G$ acts on $\mathcal{R}_p(G)$ by conjugation, resulting in the orbit space $\mathcal{R}_p(G)/G$.

**Block Induction:**
Let $H \le G$ be a subgroup and $b$ a $p$-block of $H$. Block induction, denoted $b^G = B$, is defined via the Brauer homomorphism. If $\omega_b$ is the central character associated with $b$, then $b^G$ is defined if and only if $\omega_b \circ \operatorname{Tr}_H^G$ restricts to a well-defined central character on the center of the group algebra of $G$. In Dade's conjecture, we specifically consider blocks $b$ of $N_G(C)$ that induce to $B$ in $G$.

## 3. History & State of the Art (SOTA)

Everett C. Dade formulated this conjecture in a seminal two-part paper published in 1992 and 1994. The conjecture is part of a broader historical program aiming to link the global representations of a group to its local $p$-subgroup structure:
- **1950s:** R. Brauer's foundational height-zero conjecture and $k(B)$ conjecture.
- **1970s:** The McKay Conjecture, relating characters of $p'$-degree in $G$ to those in $N_G(P)$.
- **1987:** Alperin's Weight Conjecture (AWC), bridging modular representations and $p$-weights.
- **1989:** Knörr and Robinson reformulated AWC into an alternating sum over the simplicial complex of $p$-subgroups (the Bouc complex).

Dade synthesized and radically generalized the Knörr-Robinson formulation, extending it from defect-zero modular weights to ordinary characters of arbitrary defect $d$. Dade proposed his conjecture in a hierarchy of increasing strength: **Ordinary, Projective, Invariant, and Inductive**. 

**State of the Art:** The paramount breakthrough in recent years is the reduction theorem by Britta Späth (2017). Späth proved that Dade's Projective Conjecture (which encompasses the Ordinary Conjecture) can be reduced to verifying a set of "inductive conditions" for finite quasisimple groups (The Character Triple Conjecture). This effectively shifted the entire field's focus away from arbitrary finite groups to the intense, targeted study of simple groups of Lie type, alternating groups, and sporadic groups.

## 4. Partial Results / Verified Cases

Because of Späth’s reduction, the problem is entirely solved for certain vast classes of groups, and verification continues for finite simple groups. It is completely verified for:
- **$p$-solvable groups:** Proven independently by G. Robinson and others shortly after Dade proposed the conjecture.
- **Symmetric and Alternating Groups:** Verified by J. Olsson and K. Uno (1996) for all primes $p$.
- **Groups with Cyclic Defect Groups:** Dade himself proved the ordinary conjecture for this class in a subsequent paper.
- **Finite Simple Groups of Lie Type in Defining Characteristic:** Largely verified due to the favorable behavior of parabolic induction and Borel subgroups.
- **Sporadic Simple Groups:** Verified computationally and theoretically for nearly all 26 sporadic groups and their covering groups by researchers like J. An, C. Eaton, and A.A. Schaeffer Fry.

## 5. Principal Obstacles

The conjecture remains open because verifying the "inductive conditions" for finite simple groups of Lie type in **cross-characteristic** (when the prime $p$ does not divide the characteristic of the underlying field) is extraordinarily demanding.

**The Global Cancellation Phenomenon:**
Dade's conjecture posits a perfect numerical cancellation across a poset of $p$-subgroups. This topological alternating sum (essentially computing an equivariant Euler characteristic of a $p$-subgroup complex) means that characters cannot be counted in isolation; one needs a canonical, global bookkeeping mechanism across multiple layers of normalizers.

**Automorphism Equivariance:**
To fulfill Späth's inductive conditions, one cannot merely prove Dade's conjecture for a simple group $S$. One must construct a specific bijection of characters between $S$ and its local subgroups that is entirely equivariant under the action of the outer automorphism group $\operatorname{Aut}(S)$. Finite groups of Lie type possess complex outer automorphisms (field, graph, and diagonal automorphisms). Constructing character bijections that respect these automorphisms requires extending deep theorems from Deligne-Lusztig theory.

**Lusztig Series and Disconnected Centers:**
In cross-characteristic, the representation theory of a Lie type group $\mathbf{G}^F$ is governed by Lusztig series parameterized by semisimple elements of the dual group $\mathbf{G}^{*F}$. When the dual group has a disconnected center, the parameterizations become non-canonical, severely obstructing the construction of equivariant bijections.

## 6. The Gap

The precise mathematical barrier separating the solved cases from a complete proof of Dade's Ordinary Conjecture is the verification of the **Inductive Dade Condition** for the remaining families of finite simple groups of Lie type in non-defining characteristic. Specifically, while classical groups (Types A, B, C, D) are nearly complete, the exceptional groups of Lie type—most notably $E_6, E_7$, and $E_8$—present a massive computational and theoretical gap. Crossing this boundary requires resolving how outer automorphisms permute the Harish-Chandra series and Lusztig series of these exceptional groups.

## 7. Current Research (as of June 2026)

Research is heavily clustered around fulfilling Späth's reduction framework. 
- **Exceptional Groups of Lie Type:** Researchers such as A. A. Schaeffer Fry and J. Taylor are actively mapping the Galois automorphisms and constructing equivariant character bijections for exceptional Lie groups. *(frontier — verify)*
- **Local-Global Unification:** G. Malle and M. Cabanes are pushing the boundaries of Deligne-Lusztig theory to establish generalized character triple isomorphisms that satisfy both Dade's conditions and the inductive block-wise Alperin-McKay conditions simultaneously.
- **Categorification via Derived Equivalences:** Some schools of thought suggest Dade's numerical coincidence is the shadow of a structural derived equivalence (following Broué's Abelian Defect Group Conjecture). Techniques using perverse equivalences (Chuang-Rouquier) are being explored to lift Dade's sum from the Grothendieck group to the derived category.

## 8. Future Work

Leading mathematicians suggest that future breakthroughs will rely on proving that the cohomology of Deligne-Lusztig varieties behaves predictably under graph and field automorphisms. If a unified, canonical parameterization of cross-characteristic characters can be achieved—one that naturally commutes with both $p$-local normalizers and global outer automorphisms—the inductive conditions for types $E_6, E_7, E_8$ will fall, completing the proof of Dade's Ordinary Conjecture.

## 9. Key References

- **[Foundational]** Dade, E. C. *Counting characters in blocks, I.* Inventiones mathematicae, 1992.
- **[Foundational]** Dade, E. C. *Counting characters in blocks, II.* Journal für die reine und angewandte Mathematik, 1994.
- **[SOTA / Recent]** Späth, B. *A reduction theorem for Dade's projective conjecture.* Journal of the European Mathematical Society, 2017.
- **[Survey]** Navarro, G. *Characters and Blocks of Finite Groups.* Cambridge University Press, 1998.
- **[Survey]** Cabanes, M., Enguehard, M. *Representation Theory of Finite Reductive Groups.* Cambridge University Press, 2004.

## 10. Worked Example / Concrete Special Case

We explicitly calculate the alternating sum for the symmetric group $G = S_4$ at the prime $p = 3$. 
The order of $S_4$ is $24 = 2^3 \cdot 3$, so the maximal power of $3$ dividing $|G|$ is $3^1$, giving $v_3(|G|) = 1$. 
The 3-core $O_3(S_4) = 1$. We evaluate the conjecture for the principal 3-block $B = B_0(S_4)$ at defect $d = 1$.

**1. Global Characters:**
The irreducible characters of $S_4$ have degrees 1, 1, 2, 3, 3.
The defect of a character is $d(\chi) = v_3(24) - v_3(\chi(1)) = 1 - v_3(\chi(1))$.
- Degrees 1, 1, 2 yield $v_3 = 0 \implies d(\chi) = 1$.
- Degrees 3, 3 yield $v_3 = 1 \implies d(\chi) = 0$.
The principal 3-block $B_0(S_4)$ contains exactly the three characters of defect 1 (the two characters of defect 0 constitute their own individual blocks). Thus, the global character count is:
$$ k(S_4, B_0(S_4), 1) = 3 $$

**2. Radical 3-chains:**
Since $O_3(S_4) = 1$, radical chains must begin with $P_0 = 1$. The only non-trivial 3-subgroups of $S_4$ are the four Sylow 3-subgroups (isomorphic to $C_3$). Let $P_1 = \langle (1,2,3) \rangle$. 
The normalizer is $N_G(P_1) = \langle (1,2,3), (1,2) \rangle \cong S_3$.
Because $O_3(S_3) = P_1$, the subgroup $P_1$ is a radical subgroup. As it is a maximal 3-subgroup, the chain cannot be extended. Thus, up to $G$-conjugacy, there are exactly two radical chains:
- $C_0 : 1$, with length $|C_0| = 0$ and $N_G(C_0) = S_4$.
- $C_1 : 1 < P_1$, with length $|C_1| = 1$ and $N_G(C_1) = S_3$.

**3. Local Characters:**
For $C_1$, we compute the characters of $N_G(C_1) \cong S_3$. 
The order of $S_3$ is 6, so $v_3(6) = 1$. The irreducible characters of $S_3$ have degrees 1, 1, 2. 
For all three characters, $v_3(\chi(1)) = 0$, giving a defect of $d(\psi) = 1 - 0 = 1$. 
All three characters belong to the principal block $B_0(S_3)$, and $B_0(S_3)$ induces via the Brauer homomorphism to the principal block $B_0(S_4)$ of the parent group. Therefore:
$$ k(S_3, B_0(S_4), 1) = 3 $$

**4. The Alternating Sum:**
Evaluating Dade's formula for $d=1$:
$$ \sum_{C \in \mathcal{R}_3(S_4)/S_4} (-1)^{|C|} k(N_G(C), B_0(S_4), 1) $$
$$ = (-1)^{|C_0|} k(S_4, B_0(S_4), 1) + (-1)^{|C_1|} k(S_3, B_0(S_4), 1) $$
$$ = (+1)(3) + (-1)(3) = 0 $$
The perfect cancellation confirms Dade's Ordinary Conjecture for this special case.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*