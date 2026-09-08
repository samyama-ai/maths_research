---
id: 02-algebra-group-theory/cherlin-zilber-conjecture
title: "Cherlin-Zilber Conjecture"
topic: 02-algebra-group-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Cherlin-Zilber Conjecture

> **Topic:** Algebra & Group Theory · **ID:** `02-algebra-group-theory/cherlin-zilber-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

**Conjecture (Cherlin 1979, Zilber 1977–84; the "algebraicity conjecture").**
Every infinite simple group of finite Morley rank is isomorphic, as an abstract group, to the group of $K$-rational points $\mathbb{G}(K)$ of a simple algebraic group $\mathbb{G}$ over an algebraically closed field $K$.

Constraints and conventions:

- "Group of finite Morley rank" means a group $G$ whose first-order theory in the language $\{\cdot,{}^{-1},1\}$ (possibly with extra structure) is totally transcendental with $\mathrm{RM}(G)<\omega$. Extra definable structure is *allowed*: the conclusion must hold even if $G$ is equipped with additional predicates.
- "Simple" means simple as an abstract group, with no definability hypothesis on the (absent) normal subgroups.
- The isomorphism is required only abstractly; it then follows (Poizat) that the field $K$ is interpretable in $G$ and the isomorphism is definable.

A **proof** requires: for each such $G$, the interpretation of an algebraically closed field $K$ in $G$ and an abstract isomorphism onto a simple algebraic group over $K$. A **disproof** requires the construction of one infinite simple group of finite Morley rank not of this form — e.g. a *bad group* (Section 2), or a simple group of degenerate type.

## 2. Mathematical Foundations

**Morley rank.** For a structure $M$ with monster model $\mathfrak{C}$, $\mathrm{RM}$ is defined on definable sets $X$ by: $\mathrm{RM}(X)\ge 0$ iff $X\neq\emptyset$; $\mathrm{RM}(X)\ge \alpha+1$ iff there are pairwise disjoint definable $X_i\subseteq X$ ($i<\omega$) with $\mathrm{RM}(X_i)\ge\alpha$; limit stages by supremum. If $\mathrm{RM}(X)=\alpha<\infty$, the **degree** $\deg(X)$ is the maximal $d$ with $X$ a disjoint union of $d$ definable sets of rank $\alpha$.

Equivalently (Borovik–Poizat) a **ranked group** is a group with a rank function on definable sets satisfying:

1. *(Monotonicity)* $\mathrm{RM}(X)\ge n+1$ iff $X$ contains infinitely many disjoint definable subsets of rank $\ge n$.
2. *(Definability)* for a definable family $\{X_a\}_{a\in A}$, $\{a: \mathrm{RM}(X_a)=n\}$ is definable.
3. *(Additivity)* for a definable surjection $f:X\to Y$ with all fibres of rank $n$, $\mathrm{RM}(X)=\mathrm{RM}(Y)+n$.
4. *(Elimination of infinite quantifiers)* uniform finiteness of fibres in definable families.

Consequences used throughout:

$$\mathrm{RM}(G)=\mathrm{RM}(H)+\mathrm{RM}(G/H)\quad\text{for }H\trianglelefteq G\text{ definable},$$
$$\mathrm{RM}(g^{G})=\mathrm{RM}(G)-\mathrm{RM}(C_G(g)).$$

**Descending chain condition (Macintyre).** A group of finite Morley rank has no infinite strictly descending chain of definable subgroups. Hence every $X\subseteq G$ has a definable hull, arbitrary intersections of definable subgroups are definable, and $G$ has a unique smallest definable subgroup of finite index, the **connected component** $G^{\circ}$. $G$ is **connected** iff $G=G^{\circ}$ iff $\deg(G)=1$.

**Model of the conjecture.** For $\mathbb{G}$ simple algebraic over $K=\bar{K}$, the group $\mathbb{G}(K)$ has finite Morley rank equal to $\dim_K \mathbb{G}$, with $\mathrm{RM}$ = Zariski dimension and $\deg$ = number of top-dimensional irreducible components. Thus $\mathrm{RM}(\mathrm{PSL}_2(K))=3$, $\mathrm{RM}(\mathrm{PSL}_n(K))=n^2-1$.

**Anchoring theorems.**

- *Macintyre (1971):* every infinite field of finite Morley rank (indeed every $\omega$-stable field) is algebraically closed.
- *Zilber (1977):* an $\aleph_1$-categorical group is abelian-by-finite or interprets an algebraically closed field; solvable non-nilpotent connected groups interpret a field (**Zilber's field theorem**).
- *Reineke (1975):* a connected group of Morley rank $1$ is abelian.
- *Nesin, Zilber:* connected solvable groups of finite Morley rank are nilpotent-by-abelian; a connected nilpotent group splits as $D\ast B$, $D$ divisible and $B$ of bounded exponent.

**Bad group.** A connected non-solvable group of finite Morley rank all of whose proper definable connected subgroups are nilpotent. **Bad field.** A structure $(K,\bar K^{\ast}\supseteq T)$ of finite Morley rank with $K$ algebraically closed and $T$ a proper infinite definable multiplicative subgroup. Both are the principal conjectured non-existent obstructions.

**Borovik's 2-type trichotomy.** Let $S$ be a Sylow $2$-subgroup of $G$ (all conjugate; Borovik–Poizat). Then $S^{\circ}=U\ast T$ with $U$ of bounded exponent ("unipotent") and $T$ a $2$-torus $\cong(\mathbb{Z}_{2^{\infty}})^{r}$; $r$ is the **Prüfer $2$-rank**. Types: **even** ($T=1\neq U$), **odd** ($U=1\neq T$), **mixed** ($U\neq1\neq T$), **degenerate** ($S^{\circ}=1$, i.e. $S$ finite).

## 3. History & State of the Art (SOTA)

- **1971.** Macintyre proves $\omega$-stable fields are algebraically closed — the template result the conjecture generalizes to groups.
- **1977–84.** Zilber, studying uncountably categorical structures, isolates the ladder theorem and the field theorem; conjectures algebraicity in the categorical setting.
- **1979.** Cherlin, *Groups of small Morley rank*, states the conjecture in the finite-Morley-rank setting, classifies rank $\le 2$ connected groups (solvable), reduces rank $3$ to "$\mathrm{PSL}_2(K)$ or a bad group", and introduces bad groups.
- **1987–94.** Poizat's *Groupes stables* and the Borovik–Nesin monograph fix the toolkit: Sylow theory, generic elements, generation by connected subgroups, Zilber's indecomposability theorem.
- **Late 1980s onward.** The **Borovik programme**: import the classification of finite simple groups' local-analysis machinery (Sylow $2$-theory, signalizer functors, amalgam and identification theorems) into the ranked category, splitting by $2$-type.
- **1997.** Altınel–Borovik–Cherlin eliminate **mixed type**.
- **2008.** The same authors complete **even type** (monograph, AMS Surveys 145): a simple group of finite Morley rank of even type is a Chevalley group over an algebraically closed field of characteristic $2$. This is the largest solved block.
- **2007.** Borovik–Burdges–Cherlin: a connected group of **degenerate type** has no involutions at all.
- **2018.** Frécon: **no bad group of Morley rank $3$ exists**; hence a simple group of Morley rank $3$ is $\mathrm{PSL}_2(K)$.

## 4. Partial Results / Verified Cases

| Case | Status | Source |
|---|---|---|
| $\mathrm{RM}(G)\le 2$, connected | Solvable; no simple examples | Cherlin 1979 |
| $\mathrm{RM}(G)=3$, simple | $\cong \mathrm{PSL}_2(K)$ | Cherlin 1979 + Frécon 2018 |
| $\mathrm{RM}(G)=4$, simple | No such group (reduced to rank-3 bad groups) | Wiscons 2016 + Frécon 2018 |
| $\mathrm{RM}(G)=5$, simple | Must be a bad group; hence non-algebraic if it exists | Deloro–Wiscons 2018 |
| Even type | Fully classified: Chevalley groups over $\bar{\mathbb{F}}_2$-like fields | Altınel–Borovik–Cherlin 2008 |
| Mixed type | Non-existent | Altınel–Borovik–Cherlin 1997 |
| Degenerate type | No involutions; conjecturally no simple groups | Borovik–Burdges–Cherlin 2007 |
| Odd type, Prüfer $2$-rank $\ge 3$ | Identified as Chevalley groups in the $L^{\ast}$-inductive setting | Berkman–Borovik–Burdges–Cherlin 2008 |
| Tame minimal simple groups | Classified: $\mathrm{PSL}_2(K)$ | Cherlin–Jaligot 2004 |
| Fields of char $p>0$, finite MR | Algebraically closed; no bad fields of char $p$ modulo a number-theoretic hypothesis | Wagner 2001 |
| Simple groups with a definable generic action of rank $\le 3$ on a set | Classified via permutation-group methods | Borovik–Cherlin 2008 |

## 5. Principal Obstacles

- **No underlying geometry is given.** In algebraic group theory one starts with a variety; here only a rank function and the DCC. Every argument must *manufacture* a field via Zilber's field theorem, which needs a definable solvable non-nilpotent section — exactly what a bad group refuses to supply.
- **Degenerate type has no involutions.** The entire finite-group local-analysis machinery is driven by centralizers of involutions. Borovik–Burdges–Cherlin removed involutions from degenerate type, which is a strong structural theorem but also destroys the only known handle. Replacement "unipotence parameters" (Burdges' $U_{0,r}$ theory) give a graded Sylow-like theory but no analogue of the Feit–Thompson odd-order theorem.
- **No Feit–Thompson.** It is open whether a connected group of finite Morley rank without involutions is solvable. In the finite case this took 255 pages of character theory; characters are unavailable (no finite conjugacy classes, no Brauer theory).
- **Hrushovski constructions.** Ab initio amalgamation with predimension $\delta(A)=\dim(A)-\epsilon\cdot|R(A)|$ produces strongly minimal sets not locally modular and not field-like, and — crucially — Baudisch–Hils–Martin-Pizarro–Wagner (2009) produced a **bad field of characteristic $0$** by a red-field collapse. So the analogous non-existence statement one wants for groups is *false* one level down, in the field setting. There is no soft reason forbidding a bad group.
- **Non-uniform induction.** Even/odd type proofs are inductive over "$L^{\ast}$-groups" (all proper simple definable sections already known). Degenerate sections break the induction, since they are not classified.
- **Small Prüfer rank.** Odd-type identification needs enough $2$-tori to build amalgams; Prüfer rank $1$ and $2$ configurations (e.g. $\mathrm{PSL}_2$, $\mathrm{PSL}_3$, $\mathrm{SL}_2$-like) resist generic identification.

## 6. The Gap

The conjecture reduces, modulo the completed even and mixed cases, to two irreducible cores:

1. **Degenerate type:** show no infinite simple group of finite Morley rank has a finite Sylow $2$-subgroup. Since such a group has no involutions at all, this is equivalent to a ranked Feit–Thompson theorem: *is a connected group of finite Morley rank with no involutions solvable?* Nothing weaker than a full replacement for character theory is known to suffice.
2. **Odd type of small Prüfer rank:** identify $G$ from $C(i)$ for $i$ an involution when the $2$-torus has rank $1$ or $2$, without assuming tameness (no bad fields) and without assuming proper definable simple sections are algebraic.

Orthogonally, the rank-graded attack stalls at **rank $5$**: Deloro–Wiscons show a simple group of Morley rank $5$ must be bad, so ruling out rank-$5$ bad groups (Frécon's rank-$3$ argument does not lift) is the next concrete step. Frécon's method exploited a rank-$2$ "pseudoplane" of Borel cosets; in rank $5$ the corresponding geometry has rank $3$ or $4$ and the combinatorial identity that forced the contradiction has no known analogue.

## 7. Current Research (as of June 2026)

- **Manchester / Lyon / Rutgers axis.** Borovik, Cherlin, Deloro, Frécon and Wiscons continue the rank-by-rank and permutation-group approach: bounding $\mathrm{RM}(G)$ for a group acting definably and faithfully on a set of rank $n$ (the conjectured bound is $\mathrm{RM}(G)\le n(n+2)$, attained by $\mathrm{PGL}_{n+1}$).
- **Frécon-style geometric arguments.** Attempts to axiomatize the rank-$3$ contradiction as a statement about definable "generic planes" in ranked groups, aiming at all bad groups. *(frontier — verify)*
- **Burdges' unipotence theory** ($U_{0,r}$-groups, torsion-free unipotence in characteristic $0$) is the standing substitute for $p$-local analysis in degenerate type; recent work targets a signalizer-functor theorem valid without involutions. *(frontier — verify)*
- **Group actions and representations.** Deloro's programme on minimal ranked representations ($\mathrm{SL}_2$-modules of small rank) supplies identification tools for odd type of small Prüfer rank.
- **Model-theoretic side.** Study of groups definable in $o$-minimal, geometric and NIP structures continues to sharpen what "field-like" means; Hrushovski-construction experts (Hils, Martin-Pizarro, Baudisch, Wagner) probe whether a *bad group* can be built by collapse, which would refute the conjecture.

## 8. Future Work

- Prove the **ranked Feit–Thompson theorem**, or find a genuine analogue of the Brauer/Bender method usable with generic elements and rank additivity.
- Eliminate **bad groups of all ranks**, generalizing Frécon's rank-$3$ geometric contradiction; a plausible intermediate target is rank $5$ (Deloro–Wiscons).
- Settle the existence of **bad fields of characteristic $p>0$** unconditionally (currently tied to a hypothesis on the density of Mersenne-type primes, Wagner 2001); their non-existence removes the tameness hypothesis from odd-type arguments.
- Complete **odd type of Prüfer $2$-rank $1$ and $2$** without the $L^{\ast}$ inductive assumption.
- Push the **permutation-group programme**: prove the $\mathrm{RM}(G)\le n(n+2)$ bound for faithful definable actions, which would give an independent route to identification.
- Test the conjecture's boundary by attempting a **Hrushovski-style counterexample**: an explicit amalgamation class whose generic is a simple non-algebraic ranked group.

## 9. Key References

- **[Foundational]** B. Zilber. *Groups and rings whose theory is categorical.* Fundamenta Mathematicae 95 (1977), 173–188.
- **[Foundational]** G. Cherlin. *Groups of small Morley rank.* Annals of Mathematical Logic 17 (1979), 1–28. [DOI](https://doi.org/10.1016/0003-4843(79)90019-6)
- **[Foundational]** A. Macintyre. *On $\omega_1$-categorical theories of fields.* Fundamenta Mathematicae 71 (1971), 1–25. [DOI](https://doi.org/10.4064/fm-71-1-1-25)
- **[Monograph]** A. Borovik, A. Nesin. *Groups of Finite Morley Rank.* Oxford Logic Guides 26, Oxford University Press, 1994.
- **[Monograph]** B. Poizat. *Stable Groups.* Mathematical Surveys and Monographs 87, American Mathematical Society, 2001 (French original *Groupes stables*, 1987).
- **[SOTA]** T. Altınel, A. Borovik, G. Cherlin. *Simple Groups of Finite Morley Rank.* Mathematical Surveys and Monographs 145, American Mathematical Society, 2008. [DOI](https://doi.org/10.1017/cbo9780511546464.007)
- **[SOTA]** T. Altınel, A. Borovik, G. Cherlin. *Groups of mixed type.* Journal of Algebra 192 (1997), 524–571. [DOI](https://doi.org/10.1006/jabr.1996.6950)
- **[SOTA]** A. Borovik, J. Burdges, G. Cherlin. *Involutions in groups of finite Morley rank of degenerate type.* Inventiones Mathematicae 167 (2007), 155–220. [DOI](https://doi.org/10.1007/s00029-007-0030-z)
- **[SOTA]** O. Frécon. *Simple groups of Morley rank 3 are algebraic.* Journal of the American Mathematical Society 31 (2018), 643–659. [DOI](https://doi.org/10.1090/jams/892)
- **[SOTA]** J. Wiscons. *Groups of Morley rank 4.* Journal of Symbolic Logic 81 (2016), 65–79.
- **[SOTA]** A. Deloro, J. Wiscons. *Simple groups of Morley rank 5 are bad.* Journal of Symbolic Logic 83 (2018), 1217–1229. [DOI](https://doi.org/10.1017/jsl.2017.86)
- **[SOTA]** J. Burdges. *A signalizer functor theorem for groups of finite Morley rank.* Journal of Algebra 274 (2004), 215–229. [DOI](https://doi.org/10.1016/j.jalgebra.2003.08.015)
- **[SOTA]** G. Cherlin, E. Jaligot. *Tame minimal simple groups of finite Morley rank.* Journal of Algebra 276 (2004), 13–79. [DOI](https://doi.org/10.1016/j.jalgebra.2003.12.027)
- **[SOTA]** A. Baudisch, M. Hils, A. Martin-Pizarro, F. O. Wagner. *Die böse Farbe.* Journal of the Institute of Mathematics of Jussieu 8 (2009), 415–443.
- **[Related]** E. Hrushovski. *A new strongly minimal set.* Annals of Pure and Applied Logic 62 (1993), 147–166. [DOI](https://doi.org/10.1016/0168-0072(93)90171-9)
- **[Related]** F. O. Wagner. *Fields of finite Morley rank.* Journal of Symbolic Logic 66 (2001), 703–706. [DOI](https://doi.org/10.2307/2695038)
- **[Survey]** A. Borovik, G. Cherlin. *Permutation groups of finite Morley rank.* In *Model Theory with Applications to Algebra and Analysis, Vol. 2*, LMS Lecture Note Series 350, Cambridge University Press, 2008, 59–124. [DOI](https://doi.org/10.1017/cbo9780511735219.003)

## 10. Worked Example / Concrete Special Case

**Rank 3: the dichotomy and its resolution.**

*Step 1 — the algebraic model.* Let $K=\bar K$ and $G=\mathrm{PSL}_2(K)$. Then $\mathrm{RM}(G)=\dim G=3$. A Borel subgroup $B=\{\begin{psmallmatrix}a&b\\0&a^{-1}\end{psmallmatrix}\}/\{\pm1\}$ has $\dim B=2$, with unipotent radical $U\cong (K,+)$ of rank $1$ and torus $T\cong K^{\ast}$ of rank $1$. Then $B=U\rtimes T$ is connected, solvable, **non-nilpotent**, and $N_G(B)=B$. Rank additivity on the coset space:
$$\mathrm{RM}(G/B)=\mathrm{RM}(G)-\mathrm{RM}(B)=3-2=1,$$
matching $\mathbb{P}^1(K)$. Zilber's field theorem applied to $U\rtimes T$ recovers $K$ from $G$ alone.

*Step 2 — Cherlin's dichotomy.* Let $G$ be simple, connected, $\mathrm{RM}(G)=3$. Definable connected proper subgroups have rank $1$ or $2$. If $G$ has a definable connected non-nilpotent subgroup $H$ with $\mathrm{RM}(H)=2$, then $H$ is solvable (rank $\le2$ connected groups are solvable), so Zilber's field theorem interprets an algebraically closed $K$ in $G$, and an identification argument yields $G\cong\mathrm{PSL}_2(K)$. Otherwise every proper definable connected subgroup is nilpotent: $G$ is a **bad group of rank 3**.

*Step 3 — anatomy of the hypothetical bad group.* In a bad group $G$ of rank $3$, the maximal proper definable connected subgroups (Borels) $B$ are nilpotent of rank $1$, hence abelian (Reineke), self-normalizing, and pairwise intersect trivially: $B_1\cap B_2=1$ for $B_1\neq B_2$. Count generically. The family of Borels is $\{B^{g}: g\in G\}$, parametrized by $G/N_G(B)=G/B$, so
$$\mathrm{RM}(\{B^{g}\})=3-1=2 .$$
The union $\bigcup_g B^{g}$ of these $2$-dimensional-many pairwise-almost-disjoint rank-$1$ subgroups has rank $2+1=3=\mathrm{RM}(G)$ — generically covering $G$ — yet a bad group has **no involutions and no unipotent-like torsion available to build a field**, and $\bigcup_g B^g$ can be shown to have degree issues. Cherlin proved this configuration forces $G$ to act on the rank-$2$ "pseudoplane" of Borel cosets, with points $G/B$ ($\mathrm{RM}=2$) and lines the conjugates of $B$; no algebraic group has such a geometry.

*Step 4 — the resolution.* Frécon (2018) showed this geometry is contradictory: analysing generic pairs $(x,y)\in G^2$ and the rank of the definable set of Borels meeting a generic "line", he derives a rank equation with no solution, so no bad group of rank $3$ exists. Consequently every simple group of Morley rank $3$ is $\mathrm{PSL}_2(K)$ — the smallest genuinely non-trivial confirmed instance of the Cherlin–Zilber conjecture. The identical bookkeeping in rank $5$ (Borels of rank $1$ or $2$, coset spaces of rank $3$ or $4$) gives no contradiction with present methods; that is precisely where the open problem now sits.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*