---
id: 02-algebra-group-theory/alperins-weight-conjecture
title: "Alperin's Weight Conjecture"
topic: 02-algebra-group-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Alperin's Weight Conjecture

> **Topic:** Algebra & Group Theory · **ID:** `02-algebra-group-theory/alperins-weight-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Alperin's Weight Conjecture (AWC) is a profound numerical postulate in the modular representation theory of finite groups. It asserts that the number of absolutely simple modules of a finite group algebra over a field of prime characteristic is determined purely by the local structure of the group (i.e., the normalizers of its $p$-subgroups). 

Let $G$ be a finite group, $p$ a prime dividing the order of $G$, and $k$ an algebraically closed field of characteristic $p$. A *weight* for $G$ is defined as a pair $(Q, S)$, where $Q$ is a $p$-subgroup of $G$, and $S$ is a simple $k[N_G(Q)]$-module that is projective when viewed as a module over the quotient group algebra $k[N_G(Q)/Q]$. Two weights $(Q, S)$ and $(Q', S')$ are conjugate if there exists $g \in G$ such that $Q^g = Q'$ and $S^g \cong S'$.

**Conjecture:** The number of isomorphism classes of simple $kG$-modules is precisely equal to the number of $G$-conjugacy classes of weights for $G$. 

Equivalently, the conjecture can be formulated block-by-block. For any $p$-block $B$ of $G$, the number of simple $kG$-modules belonging to $B$, typically denoted $l(B)$, equals the number of conjugacy classes of $B$-weights. A complete proof requires establishing this numerical equality universally for all finite groups.

## 2. Mathematical Foundations

The conjecture sits at the intersection of group theory and representation theory, specifically analyzing group algebras in positive characteristic.

**Group Algebras and Blocks:**
The group algebra $kG$ decomposes into a direct sum of indecomposable two-sided ideals called *blocks*:
$$ kG = B_1 \oplus B_2 \oplus \dots \oplus B_n $$
Every indecomposable $kG$-module belongs to a unique block. Each block $B_i$ is associated with a conjugacy class of $p$-subgroups of $G$, called its *defect groups*. 

**Weights and Projectivity:**
Given a $p$-subgroup $Q \le G$, the normalizer is $N_G(Q)$. Since $Q$ is a normal $p$-subgroup of $N_G(Q)$, any simple $k[N_G(Q)]$-module $S$ must be annihilated by the augmentation ideal of $kQ$, meaning $Q$ acts trivially on $S$. Thus, $S$ naturally inflates from a module of the quotient $N_G(Q)/Q$.
The module $S$ is projective over $k[N_G(Q)/Q]$ if it appears as a direct summand of a free module:
$$ (k[N_G(Q)/Q])^{\oplus m} \cong S \oplus M $$
for some integer $m$ and module $M$. If $(Q, S)$ is a weight, $S$ belongs to a block $b$ of $N_G(Q)$. The weight $(Q,S)$ is assigned to a block $B$ of $G$ if $b^G = B$ in the sense of Brauer induction.

## 3. History & State of the Art (SOTA)

Jonathan Alperin presented this conjecture at the Arcata Conference on Representations of Finite Groups in 1986. At the time, representation theorists were discovering striking, deep connections between the global representation theory of $G$ and the local representation theories of its $p$-subgroups (the "local-global principle").

In 1989, Knörr and Robinson reformulated the conjecture using the Brown complex of $p$-subgroups, expressing it as an alternating sum of ordinary irreducible characters. This inspired Richard Dade in 1992 to formulate his far-reaching "Dade's Ordinary Conjecture" and its projective variants, which express the number of characters of a given defect as an alternating sum over chains of $p$-subgroups. If Dade's conjectures are true, Alperin's Weight Conjecture easily follows.

A monumental turning point occurred in 2011 when G. Navarro and P. H. Tiep reduced the conjecture to the Classification of Finite Simple Groups (CFSG). B. Späth subsequently refined this in 2013, proving that AWC holds for all finite groups if every finite non-abelian simple group satisfies a specific, stronger set of criteria known as the *inductive Alperin weight condition* (iAWC). The state of the art is now entirely focused on verifying iAWC for the remaining families of finite simple groups.

## 4. Partial Results / Verified Cases

Because of the local-global reduction theorems, mathematicians have sought to classify and verify AWC and iAWC for vast families of groups. The conjecture is proven to be true for:
- Finite $p$-solvable groups (proved implicitly by Okuyama, explicitly noted by Alperin).
- Symmetric and alternating groups (verified by Alperin and Fong, 1990; iAWC verified by Späth).
- Groups of Lie type in their defining characteristic (proved by Cabanes).
- Sporadic simple groups (verified theoretically and computationally by various authors).
- Groups with cyclic defect groups (a consequence of Dade's earlier theorems).
- Many classical groups of Lie type in cross characteristic (e.g., General Linear and Unitary groups, verified by Broué, Malle, and Michel).

Therefore, the remaining unverified terrain is strictly confined to certain classes of finite simple groups of Lie type in non-defining characteristic, particularly the exceptional groups (e.g., $E_6, E_7, E_8$).

## 5. Principal Obstacles

The fundamental bottleneck in proving Alperin's Weight Conjecture is that it is a *numerical* equality lacking a natural canonical bijection. While both sides of the equation yield the same integer, standard categorical, homological, or character-theoretic techniques fail to construct an explicit, functorial one-to-one correspondence between the set of simple modules and the set of weights. 

Furthermore, Späth’s reduction to the inductive Alperin weight condition (iAWC) introduces heavy technical burdens. For a simple group $S$, one cannot merely count the modules and weights; one must construct bijections that are highly equivariant with respect to the automorphism group $\operatorname{Aut}(S)$ and extend to central extensions (Schur covers) of $S$. For exceptional groups of Lie type, the Lusztig character theory and generic character tables are incredibly dense, and ensuring that specific cross-characteristic representations extend compatibly under graph, field, and diagonal automorphisms breaks down standard inductive approaches. 

## 6. The Gap

The exact boundary separating the partially solved cases from a complete resolution of the conjecture is verifying the inductive Alperin weight condition (iAWC) for the remaining exceptional groups of Lie type in cross characteristic (such as the Chevalley groups $F_4, E_6, E_7, E_8$, and their twisted analogues). Crossing this boundary requires either a breakthrough in the invariant theory of Lusztig representations to globally establish the automorphism-equivariant bijections required by Späth's theorem, or a completely new categorical approach that establishes a derived equivalence implying the bijections functorially.

## 7. Current Research (as of June 2026)

Current research is bifurcated into two dominant methodologies:
1. **The CFSG Reduction Program:** Led by researchers such as B. Späth, G. Navarro, P. H. Tiep, and C. Vallejo. This program painstakingly analyzes the character sheaves and Deligne-Lusztig theory of the remaining exceptional groups to build the required equivariant maps. 
2. **Categorification and Derived Equivalences:** Following Broué's Abelian Defect Group Conjecture, some algebraic geometers and topologists look for derived equivalences between the principal block of $G$ and the principal block of its normalizer. 
*(frontier — verify)*: Recent preprints attempt to embed the category of $kG$-modules into stable module $\infty$-categories, conjecturing that AWC is simply the decategorified Euler characteristic of a local-global equivalence of specific exact functors.

## 8. Future Work

Leading modular representation theorists suggest the following pathways:
- Complete the case-by-case verification of iAWC for the exceptional groups of Lie type, which would formally conclude the proof of Alperin's Weight Conjecture.
- Develop a "canonical" weight bijection. Even if AWC is proven via Späth's reduction, finding a natural mathematical map—perhaps through the lens of perverse equivalences or homotopical algebra—remains a Holy Grail in the field.
- Resolve Dade's Projective Conjecture, which subsumes AWC and provides a more comprehensive topological framework for local-global counting principles.

## 9. Key References

- **[Foundational]** Alperin, J. L. *Weights for finite groups.* The Arcata Conference on Representations of Finite Groups (Arcata, Calif., 1986), Proc. Sympos. Pure Math., 47, Part 1, Amer. Math. Soc., 1987. [DOI](https://doi.org/10.1090/pspum/047.1/933373)
- **[Foundational]** Knörr, R., and Robinson, G. R. *Some remarks on a conjecture of Alperin.* Journal of the London Mathematical Society, 39(1), 1989. [DOI](https://doi.org/10.1112/jlms/s2-39.1.48)
- **[SOTA / Recent]** Navarro, G., and Tiep, P. H. *A reduction theorem for the Alperin weight conjecture.* Inventiones mathematicae, 184(3), 2011. [DOI](https://doi.org/10.1007/s00222-010-0295-2)
- **[SOTA / Recent]** Späth, B. *A reduction theorem for the Alperin weight conjecture.* Inventiones mathematicae, 192(3), 2013. [DOI](https://doi.org/10.1515/jgt-2012-0032)
- **[Survey]** Linckelmann, M. *The Block Theory of Finite Group Algebras.* Cambridge University Press, 2018.

## 10. Worked Example / Concrete Special Case

Let us verify Alperin's Weight Conjecture for the symmetric group $G = S_3$ over a field $k$ of prime characteristic $p = 2$.

The order of $S_3$ is $6$. Since $p=2$, the $p$-regular conjugacy classes (elements of odd order) are the identity $e$ and the 3-cycles $(123), (132)$, which form two classes. A standard theorem of Brauer states that the number of simple $kG$-modules equals the number of $p$-regular classes. 
Thus, there are **2 simple $kS_3$-modules**: the trivial module $k$, and a 2-dimensional simple module $M$.

Now we calculate the weights. A weight is a pair $(Q, S)$ up to conjugacy. The 2-subgroups of $S_3$ are the trivial subgroup $1$, and the three conjugate subgroups of order 2: $P_1 = \langle (12) \rangle, P_2 = \langle (13) \rangle, P_3 = \langle (23) \rangle$.

**Case 1:** $Q = 1$. 
The normalizer is $N_G(1) = S_3$. We require a simple $k[S_3/1] \cong kS_3$-module $S$ that is projective. A $kS_3$-module is projective if and only if its dimension is divisible by the $p$-part of $|G|$, which is $2$. Of our two simple modules, $k$ has dimension 1, and $M$ has dimension 2. 
Therefore, $M$ is projective. 
This yields the weight $(1, M)$.

**Case 2:** $Q = P_1 = \langle (12) \rangle$.
The normalizer is $N_G(P_1) = P_1$. We require a simple $k[P_1/P_1] \cong k$-module $S$ that is projective. The only simple $k$-module is the trivial module $k$, which is trivially projective over the field $k$.
This yields the weight $(P_1, k)$. 

Because $P_1, P_2, P_3$ are conjugate in $S_3$, the weights $(P_1, k), (P_2, k),$ and $(P_3, k)$ all fall into a single $G$-conjugacy class. 

Summarizing the conjugacy classes of weights, we have exactly two:
1. $[(1, M)]$
2. $[(P_1, k)]$

The number of simple modules is $2$. The number of weight conjugacy classes is $2$. 
$$ 2 = 2 $$
This provides a concrete, finite verification of Alperin's Weight Conjecture for $S_3$ at $p=2$.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*