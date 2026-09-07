---
id: 08-logic-set-theory/invariant-basis-number-problem
title: "Invariant Basis Number Problem"
topic: 08-logic-set-theory
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Invariant Basis Number Problem

> **Topic:** Mathematical Logic & Set Theory · **ID:** `08-logic-set-theory/invariant-basis-number-problem` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

A unital ring $R$ has **invariant basis number** (IBN) if
$$R^m \cong R^n \text{ as left } R\text{-modules} \implies m = n \qquad (m,n \in \mathbb{N}).$$

The Invariant Basis Number Problem is the cluster of questions:

1. **Existence.** Do rings without IBN exist, and which pairs $(m,n)$ with $m<n$ occur as the *module type* of such a ring?
2. **Classification.** Give a checkable criterion deciding IBN for a concrete presented ring.
3. **Logical strength.** How much of the axiom of choice, and how much set-existence strength in second-order arithmetic, is needed for the statement "dimension is well defined"?

A complete answer to (1) requires an explicit ring $R$ with an isomorphism $R^m\cong R^n$, $m\ne n$, together with a proof that no smaller pair occurs. A complete answer to (2) requires an algorithm on presentations. A complete answer to (3) requires ZF-models (or reverse-mathematics separations) pinning the statement between known principles.

Items (1) and (2) are **resolved**: Leavitt (1957, 1962) settled existence and realised every module type; Cohn (1966) settled the universal-ring picture; Kanuni–Özaydın (2019) reduced IBN for Cohn–Leavitt path algebras to rational linear algebra. Residual open pieces are listed in §6.

## 2. Mathematical Foundations

Let $R$ be a ring with $1 \ne 0$. $R^m\cong R^n$ holds iff there exist matrices $X\in M_{m\times n}(R)$, $Y\in M_{n\times m}(R)$ with
$$XY = I_m, \qquad YX = I_n .$$
So IBN is a purely equational, first-order condition on $R$: its failure is witnessed by finitely many ring elements satisfying finitely many equations. Hence **failure of IBN is preserved by ultraproducts and is $\Sigma_1$ over the language of rings**; IBN itself is a $\Pi_1$ (universal) property of the elementary diagram, and is preserved under elementary equivalence.

**Module type.** If $R$ lacks IBN, set $m$ minimal with $R^m\cong R^n$ for some $n>m$, and $n$ minimal for that $m$. Leavitt showed $R^k \cong R^l$ ($k,l \ge m$) iff $k\equiv l \pmod{n-m}$. The pair $(m,n-m)$ is the **module type**.

**The finiteness hierarchy** (Lam, *Lectures on Modules and Rings*, §1):
$$\text{stably finite} \;\Rightarrow\; \text{UGN} \;\Rightarrow\; \text{rank condition} \;\Rightarrow\; \text{IBN},$$
where *stably finite* means $ab=1\Rightarrow ba=1$ in every $M_k(R)$; *UGN* (unbounded generating number) means $R^n$ needs at least $n$ generators; the *rank condition* means a surjection $R^m \twoheadrightarrow R^n$ forces $m\ge n$. All three implications are strict.

**Sufficient conditions.** If there is a ring homomorphism $R\to S$ with $S$ having IBN, then $R$ has IBN (apply $-\otimes_R S$). Consequences: every nonzero commutative ring has IBN (quotient by a maximal ideal gives a field); every group ring $K[G]$ has IBN (augmentation $K[G]\to K$); every ring with a nonzero finite-dimensional representation has IBN. Left-Noetherian rings have IBN via composition-length/Goldie-rank arguments.

**Leavitt algebras.** For a field $K$ and $1\le m<n$, $L_K(m,n)$ is the $K$-algebra with generators $x_{ij}, y_{ji}$ ($1\le i\le m$, $1\le j\le n$) and defining relations exactly $XY=I_m$, $YX=I_n$. It is the universal ring of module type $(m,n-m)$.

**Set-theoretic layer.** For *finite* ranks over a field, invariance of dimension is a theorem of ZF alone (Steinitz exchange is a finite induction). The infinite analogue is not: in ZF one cannot prove that any two bases of a vector space have equal cardinality, and "every vector space has a basis" implies AC (Blass, 1984). Läuchli (1962) built ZF-models with pathological vector spaces. In second-order arithmetic, existence of a basis for a countable vector space over a countable field is equivalent to $\mathsf{ACA}_0$ (Friedman–Simpson–Smith, 1983), while finite-rank invariance is provable in $\mathsf{RCA}_0$.

## 3. History & State of the Art (SOTA)

- **1950–51.** Jacobson and Shepherdson analyse one-sided inverses; Shepherdson shows $R$ Dedekind-finite $\not\Rightarrow$ $M_2(R)$ Dedekind-finite.
- **1957.** W. G. Leavitt, *Modules without invariant basis number* (Proc. AMS 8): first explicit rings with $R^m\cong R^n$, $m\ne n$.
- **1962.** Leavitt, *The module type of a ring* (Trans. AMS 103): the algebras $L_K(m,n)$; module type is well defined and every pair $(m,k)$, $m,k\ge1$, is realised. $L_K(1,n)$ is simple.
- **1966.** P. M. Cohn, *Some remarks on the invariant basis property* (Topology 5): universal constructions, embedding results, and the separation of IBN from the rank condition.
- **1977.** J. Cuntz constructs $\mathcal{O}_n$, the C\*-analogue: $\mathcal{O}_n$ contains a copy of $L_{\mathbb{C}}(1,n)$ as a dense $*$-subalgebra.
- **1983.** Montgomery: von Neumann finiteness is not preserved by tensor products of algebras — a warning for closure properties.
- **2001.** G. Abrams, *Invariant basis number and types for strongly graded rings* (J. Algebra 237): IBN transfer along gradings.
- **2004.** Elek–Szabó: Kaplansky's direct finiteness conjecture holds for sofic groups, giving stable finiteness (hence IBN) for $K[G]$ in a very wide class.
- **2005–2017.** Leavitt path algebras $L_K(E)$ emerge (Abrams–Aranda Pino; Ara–Moreno–Pardo), with $\mathcal{V}(L_K(E))\cong M_E$, the graph monoid.
- **2019.** Kanuni–Özaydın: IBN for Cohn–Leavitt path algebras of finite graphs is decided by a rational linear system; in particular IBN is independent of $K$ and computable in polynomial time. This is the "solved-recently" core of the entry.

## 4. Partial Results / Verified Cases

- **All commutative rings** $R\ne 0$: IBN holds (choice-free for finite ranks).
- **Left- or right-Noetherian rings**, **local rings**, **semilocal rings**, **von Neumann regular rings**, **$C^*$-algebras with a tracial state**: IBN holds.
- **Group rings $K[G]$**, all $G$, all fields $K$: IBN holds via augmentation. Stable finiteness holds for $\mathrm{char}\,K=0$ (Kaplansky) and for all sofic $G$ in any characteristic (Elek–Szabó 2004).
- **Module types realised:** for every $1\le m<n$ and every field $K$, $L_K(m,n)$ has module type $(m,n-m)$ — the full parameter range $\{(m,k): m,k\ge 1\}$ is attained (Leavitt 1962).
- **Graph algebras (finite graph $E$, adjacency matrix $A_E$, regular vertices $\mathrm{Reg}(E)$).** $L_K(E)$ has IBN iff the system
 $$(I - A_E^{t})\,x = \mathbf{1}, \qquad x \in \mathbb{Q}^{\mathrm{Reg}(E)},$$
 has **no** rational solution (Kanuni–Özaydın 2019). Decidable by Gaussian elimination; independent of $K$.
- **Hierarchy strictness:** rings with IBN but failing the rank condition, and rings with the rank condition failing UGN, are known (Cohn 1966; see Lam, GTM 189, §1C for the catalogue).
- **Set theory:** finite-rank invariance is a $\mathsf{RCA}_0$ theorem; infinite-basis cardinality invariance fails in suitable ZF-models (Läuchli 1962; Howard–Rubin 1998, Forms 1–11 table).

## 5. Principal Obstacles

- **No local-to-global principle.** IBN is not local: it is not detected on localisations, completions, or residue rings in any uniform way, because failure is a single equational witness that can be destroyed by any quotient. Standard commutative-algebra machinery (Nakayama, faithfully flat descent) applies only after a map to a "good" ring is found — and constructing such a map is the whole problem.
- **$K$-theory is too coarse.** For $R$ without IBN, $K_0(R) \cong \mathbb{Z}/(n-m)$ collapses the distinction between $R^k$ and $R^{k+(n-m)}$; one must work with the non-cancellative monoid $\mathcal{V}(R)$ of projectives, which is not a group and has no exact sequences.
- **Non-separativity.** Ara–Goodearl–O'Meara–Pardo (1998) reduce many finiteness questions for exchange rings to *separativity* of $\mathcal{V}(R)$; whether every exchange ring is separative is open, and without it the refinement calculus stalls.
- **Word-problem obstruction.** For a general finitely presented ring, deciding whether $XY=I_m,\;YX=I_n$ is consistent with the relations subsumes the word problem for finitely presented monoids, so no algorithm can exist in full generality. The Kanuni–Özaydın criterion works only because graph presentations linearise.
- **Ultraproduct/soficity gap.** For Kaplansky's direct finiteness conjecture, the sofic proof uses approximation by finite permutation matrices; no group is known to be non-sofic, but neither is soficity provable, so the argument cannot be closed.

## 6. The Gap

Resolved: existence, module-type classification, and decidability on the graph-algebra class. The remaining boundary is exactly:

- **(G1)** No criterion for IBN on arbitrary finitely presented rings (provably impossible in full generality; the open part is to demarcate maximal decidable subclasses beyond Cohn–Leavitt algebras).
- **(G2)** **Kaplansky's direct finiteness conjecture**: is $K[G]$ stably finite for every group $G$ and field $K$? Known for sofic $G$; open for arbitrary $G$ and $\mathrm{char}\,K = p>0$. IBN itself holds; the gap is the stronger stable-finiteness rung of the hierarchy.
- **(G3)** Closure under $\otimes_K$: if $R,S$ are $K$-algebras with IBN, must $R\otimes_K S$? Montgomery's example blocks the analogous statement for von Neumann finiteness, so no transfer argument is available.
- **(G4)** Non-unital and infinite-graph settings, where "basis number" must be replaced by local-unit or Morita-theoretic invariants.

## 7. Current Research (as of June 2026)

- **Graph and groupoid algebras.** Extension of the Kanuni–Özaydın criterion to Steinberg algebras of ample groupoids and to weighted/separated graph algebras; the ambition is a monoid-theoretic IBN test valid whenever $\mathcal{V}$ is finitely presented. Centres: Colorado (Abrams), UAB Barcelona (Ara), Western Sydney (Hazrat). *(frontier — verify)*
- **Soficity and direct finiteness.** Continued attack on (G2) via $L^2$-invariants and operator-algebraic approximation; work relating Kaplansky finiteness to the Atiyah conjecture and to Connes-embeddability. *(frontier — verify)*
- **Set-theoretic/reverse-mathematical side.** Ongoing calibration of dimension-invariance statements in ZF and in subsystems of second-order arithmetic, using the Howard–Rubin framework for permutation models.
- **Model theory of rings without IBN.** $L_K(1,n)$ is simple and its first-order theory is being studied as a natural example where a $\Sigma_1$ equational condition destroys all rank invariants.

## 8. Future Work

- Find the maximal class of presentations on which IBN is decidable; conjecturally those whose $\mathcal{V}$-monoid is finitely presented and refinement.
- Settle separativity for exchange rings — this would collapse several finiteness rungs at once (Ara–Goodearl–O'Meara–Pardo programme).
- Prove or refute stable finiteness of $K[G]$ for a non-sofic-candidate group, e.g. via Gromov-style random groups.
- Decide (G3) by constructing $R,S$ with IBN and $R\otimes_K S$ of finite module type.
- Give a ZF-model-theoretic account of what exactly fails for infinite ranks, aligned with the finite-rank equational picture.

## 9. Key References

- **[Foundational]** W. G. Leavitt. *Modules without invariant basis number.* Proc. Amer. Math. Soc. 8 (1957), 322–328.
- **[Foundational]** W. G. Leavitt. *The module type of a ring.* Trans. Amer. Math. Soc. 103 (1962), 113–130.
- **[Foundational]** P. M. Cohn. *Some remarks on the invariant basis property.* Topology 5 (1966), 215–228.
- **[Foundational]** J. C. Shepherdson. *Inverses and zero divisors in matrix rings.* Proc. London Math. Soc. (3) 1 (1951), 71–85.
- **[Survey]** T. Y. Lam. *Lectures on Modules and Rings.* Graduate Texts in Mathematics 189, Springer, 1999. (Ch. 1: IBN, rank condition, stable finiteness.)
- **[Survey]** P. M. Cohn. *Free Rings and Their Relations,* 2nd ed. Academic Press, 1985.
- **[Survey]** G. Abrams, P. Ara, M. Siles Molina. *Leavitt Path Algebras.* Lecture Notes in Mathematics 2191, Springer, 2017.
- **[SOTA / Recent]** M. Kanuni, M. Özaydın. *Cohn–Leavitt path algebras and the invariant basis number property.* Journal of Algebra and Its Applications 18 (2019).
- **[SOTA / Recent]** G. Elek, E. Szabó. *Sofic groups and direct finiteness.* Journal of Algebra 280 (2004), 426–434.
- **[SOTA / Recent]** G. Abrams. *Invariant basis number and types for strongly graded rings.* Journal of Algebra 237 (2001), 32–37.
- **[Related]** P. Ara, K. R. Goodearl, K. C. O'Meara, E. Pardo. *Separative cancellation for projective modules over exchange rings.* Israel J. Math. 105 (1998), 105–137.
- **[Related]** J. Cuntz. *Simple $C^*$-algebras generated by isometries.* Comm. Math. Phys. 57 (1977), 173–185.
- **[Logic]** A. Blass. *Existence of bases implies the axiom of choice.* Contemporary Mathematics 31 (1984), 31–33.
- **[Logic]** H. Läuchli. *Auswahlaxiom in der Algebra.* Comment. Math. Helv. 37 (1962/63), 1–18.
- **[Logic]** H. Friedman, S. G. Simpson, R. L. Smith. *Countable algebra and set existence axioms.* Ann. Pure Appl. Logic 25 (1983), 141–181.
- **[Logic]** P. Howard, J. E. Rubin. *Consequences of the Axiom of Choice.* AMS Math. Surveys and Monographs 59, 1998.

## 10. Worked Example / Concrete Special Case

**The Leavitt algebra $L_K(1,2)$.** Take $K$ a field and $R = L_K(1,2)$: generators $x_1,x_2,y_1,y_2$, relations
$$x_1y_1 + x_2y_2 = 1, \qquad y_ix_j = \delta_{ij}\,1 \;\; (i,j\in\{1,2\}).$$
Set $X = \begin{pmatrix} x_1 & x_2\end{pmatrix}\in M_{1\times2}(R)$ and $Y=\begin{pmatrix} y_1 \\ y_2\end{pmatrix}\in M_{2\times1}(R)$. Then
$$XY = x_1y_1 + x_2y_2 = I_1, \qquad YX = \begin{pmatrix} y_1x_1 & y_1x_2 \\ y_2x_1 & y_2x_2\end{pmatrix} = \begin{pmatrix} 1 & 0\\ 0 & 1\end{pmatrix} = I_2 .$$

Define $\varphi: R \to R^2$, $r\mapsto rX$ (row vector $(rx_1, rx_2)$), and $\psi: R^2\to R$, $(a,b)\mapsto ay_1+by_2$. Both are right $R$-module maps and $\psi\varphi = \mathrm{id}_R$, $\varphi\psi=\mathrm{id}_{R^2}$. Hence
$$R \cong R^2 \implies R^k \cong R^l \text{ for all } k,l\ge 1,$$
so $R$ has module type $(1,1)$ and fails IBN maximally: **every** finitely generated free module of positive rank is isomorphic to $R$ itself. Correspondingly $K_0(R) \cong \mathbb{Z}/1 = 0$.

**Cross-check with the graph criterion.** $L_K(1,2) = L_K(E)$ for $E$ the "rose with two petals": one vertex $v$, two loops. Then $A_E = (2)$, $\mathrm{Reg}(E)=\{v\}$, and
$$(I - A_E^{t})x = \mathbf{1} \iff (1-2)x = 1 \iff x = -1 \in \mathbb{Q}.$$
A rational solution exists, so IBN fails — matching the direct computation.

**Contrast: one petal.** $E$ = one vertex, one loop gives $L_K(E) = K[t,t^{-1}]$, and $(1-1)x=1$ has no solution. IBN holds — as it must, since $K[t,t^{-1}]$ is commutative and nonzero. The single integer $1-n$ therefore separates the commutative Laurent ring from the simple, rank-collapsing Leavitt algebra.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*