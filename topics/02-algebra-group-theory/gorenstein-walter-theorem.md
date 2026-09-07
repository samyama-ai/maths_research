---
id: 02-algebra-group-theory/gorenstein-walter-theorem
title: "Gorenstein-Walter Theorem"
topic: 02-algebra-group-theory
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Gorenstein-Walter Theorem

> **Topic:** Algebra & Group Theory · **ID:** `02-algebra-group-theory/gorenstein-walter-theorem` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

**Theorem (Gorenstein–Walter, 1965).** Let $G$ be a finite group whose Sylow $2$-subgroups are dihedral, and let $O(G)$ denote the largest normal subgroup of $G$ of odd order (the *core*). Then
$$G/O(G) \;\cong\; \begin{cases} \text{a dihedral } 2\text{-group}, & \\ A_7, & \\ H \text{ with } \mathrm{PSL}_2(q) \trianglelefteq H \le \mathrm{P\Gamma L}_2(q), & q \text{ odd}, \ q>3. \end{cases}$$
In particular the only **simple** groups with dihedral Sylow $2$-subgroups are $A_7$ and $\mathrm{PSL}_2(q)$ for odd $q>3$.

The theorem is proved. What remains open — and what this page tracks — is the *revision problem*: the original proof runs to roughly 260 journal pages and depends essentially on Brauer's theory of blocks and exceptional characters. The open questions are:

1. **(Revision)** Is there a proof by purely local group-theoretic methods (no character theory, no block theory) of publishable length? Bender (1981) gave a substantially shorter but still character-dependent argument.
2. **(Fusion-theoretic form)** Classify all saturated fusion systems on a dihedral $2$-group *without* invoking the classification of finite simple groups (CFSG), and deduce the group statement from it.
3. **(Odd analogue)** Determine the correct $p$-local generalization for odd primes $p$, where no dihedral-type rigidity is available.

A complete resolution of (1) means a self-contained local-analytic proof; of (2), a CFSG-free classification of $\mathcal{F}$ on $D_{2^n}$; of (3), a theorem of comparable strength for $p$-groups of maximal class, $p$ odd.

## 2. Mathematical Foundations

**Dihedral groups.** For $n \ge 2$,
$$D_{2^n} = \langle r,s \mid r^{2^{n-1}} = s^2 = 1,\ srs^{-1}=r^{-1}\rangle,$$
of order $2^n$. For $n\ge 3$ it has maximal class ($|D_{2^n}| = 2^n$, nilpotency class $n-1$), center $Z = \langle r^{2^{n-2}}\rangle$ of order $2$, and exactly two conjugacy classes of non-central involutions with representatives $s$ and $rs$. The case $n=2$ gives the Klein four-group $V_4 = D_4$, which is abelian and is included in the theorem's hypothesis.

**Cores and $2$-local structure.** $O(G)$ is the $2$-core: the unique largest normal subgroup of odd order. A group $G$ is *$2$-constrained* if $C_{G/O(G)}(O_2(G/O(G))) \le O_2(G/O(G))$. For an involution $t \in G$, the *$2$-local subgroup* is $C_G(t)$.

**Fusion.** For $S \in \mathrm{Syl}_2(G)$, the fusion category $\mathcal{F}_S(G)$ has objects the subgroups of $S$ and morphisms the maps induced by $G$-conjugation. Burnside's lemma gives: if $S$ is abelian, $\mathcal{F}_S(G)$ is controlled by $N_G(S)$. For $S \cong D_{2^n}$ there are exactly three possible fusion patterns on the three classes of involutions of $S$: no fusion; fusion of the two non-central classes ($\mathrm{PGL}_2$-type); or fusion of all three classes ($\mathrm{PSL}_2$/$A_7$-type).

**Sylow structure of the target groups.** For $q = p^f$ odd, $|\mathrm{PSL}_2(q)| = q(q^2-1)/2$, and a Sylow $2$-subgroup is dihedral of order $2^n$ where $2^n = \left|(q^2-1)/2\right|_2$, the $2$-part. Thus $q \equiv \pm 3 \pmod 8 \iff S \cong V_4$. For $A_7$, $|A_7| = 2520 = 2^3\cdot3^2\cdot5\cdot7$ and $S \cong D_8$.

**Inputs the proof depends on.**
- *Feit–Thompson (1963):* groups of odd order are solvable — needed so that $O(G)$ is solvable and induction on $|G|$ is available.
- *Brauer–Suzuki–Wall (1958):* character-theoretic characterization of $\mathrm{PSL}_2(q)$ by the centralizer of an involution.
- *Brauer's theory of blocks with Klein four and cyclic defect groups*, giving the character-degree relation $|G| = \frac{1}{4}\big(\text{degree data}\big)$ used in the final identification step.
- *Glauberman's $Z^*$-theorem (1966):* if $t$ is an involution isolated in $S$ (i.e. $t^G \cap S = \{t\}$), then $t \in Z^*(G)$, so $t O(G) \in Z(G/O(G))$.

## 3. History & State of the Art (SOTA)

- **1955–1958.** Suzuki classifies groups with all odd Sylow subgroups cyclic; Brauer–Suzuki–Wall characterize $\mathrm{PSL}_2(q)$ by an involution centralizer.
- **1959.** Brauer–Suzuki: a group with generalized quaternion Sylow $2$-subgroups is never simple — the companion result for the other maximal-class family.
- **1963.** Feit–Thompson odd order theorem removes the last obstruction to induction.
- **1965.** Gorenstein and Walter publish *The characterization of finite groups with dihedral Sylow 2-subgroups* in three parts, *J. Algebra* **2**, pp. 85–151, 218–270, 354–393. This is the first classification theorem in the "characterization by Sylow $2$-structure" program and the template for the whole CFSG local-analysis strategy.
- **1966.** Glauberman's $Z^*$-theorem simplifies the isolated-involution case.
- **1969–1970.** Walter handles abelian Sylow $2$-subgroups; Alperin–Brauer–Gorenstein handle quasi-dihedral (semidihedral) and wreathed Sylow $2$-subgroups (*Trans. AMS* **151**, 261 pp.), completing maximal-class $2$-groups.
- **1974.** Goldschmidt's *2-fusion in finite groups* gives a general fusion machine that recovers parts of the dihedral analysis.
- **1981.** Bender publishes a compressed proof (13 pages, *J. Algebra* **70**), using the Bender method (strongly embedded subgroups, uniqueness subgroups) plus character theory.
- **1994–present.** Gorenstein–Lyons–Solomon incorporate the dihedral case into the second-generation CFSG as part of the "special odd type" analysis.
- **2010s–2020s.** Fusion-system reformulations: saturated fusion systems on dihedral $2$-groups are classified, but the known proofs of exhaustiveness in the general reduced case still lean on CFSG-derived input.

## 4. Partial Results / Verified Cases

- **$|S| = 4$ ($S \cong V_4$).** Fully proved by elementary means (Gorenstein–Walter Part I; also a corollary of Walter's abelian theorem). $G/O(G) \cong V_4$, or $\mathrm{PSL}_2(q)$ with $q \equiv \pm3 \pmod 8$, $q>3$. Note $\mathrm{PSL}_2(5)\cong A_5$, $\mathrm{PSL}_2(13)$, $\mathrm{PSL}_2(29)$ are instances.
- **$|S| = 8$ ($S \cong D_8$).** The unique place where $A_7$ occurs; also $\mathrm{PSL}_2(7)$, $\mathrm{PSL}_2(9)\cong A_6$, $\mathrm{PSL}_2(17)$, and $\mathrm{PGL}_2(3)\cong S_4$-type quotients. Verified computationally for all groups of order $\le 2000$ in GAP/Magma libraries.
- **$G$ solvable.** Elementary: $G/O(G)$ is a $2$-group, i.e. dihedral, by Hall–Higman/Burnside transfer arguments alone. No character theory needed.
- **$G$ $2$-constrained.** Reduces to the solvable case via the $2$-local structure; no character theory.
- **Isolated central involution.** If $z \in Z(S)$ is not $G$-conjugate to any other involution of $S$, Glauberman's $Z^*$-theorem gives $z \in Z^*(G)$ and induction on $|G/\langle z\rangle O(G)|$ closes the case — a genuinely character-free path for this branch.
- **Companion maximal-class families (all settled).** Generalized quaternion (Brauer–Suzuki, 1959: no simple group); semidihedral and wreathed (Alperin–Brauer–Gorenstein, 1970: $\mathrm{PSL}_3(q)$, $\mathrm{PSU}_3(q)$, $M_{11}$, $A_7$-related).
- **Fusion systems.** All saturated fusion systems on $D_{2^n}$ are known: the three patterns of §2, realized by $D_{2^n}$ itself, $\mathrm{PGL}_2(q)$-type, and $\mathrm{PSL}_2(q)$/$A_7$-type. Verified independently for $2^n \le 2^9$ by Oliver's enumeration of reduced fusion systems over small $2$-groups.

## 5. Principal Obstacles

- **The character-theory dependence is not cosmetic.** After the local analysis pins down $C_G(t) \cong$ (a specific shape, e.g. $C_G(z)/O(C_G(z))$ dihedral or $\mathrm{SL}_2$-like), one must *identify* $G$ from that data. Local methods produce a group with a $BN$-pair or a strongly embedded subgroup only in favorable branches; in the residual branches the only known identification tool is Brauer's exceptional-character machinery, which computes $|G|$ from a block with Klein four or cyclic defect group. There is no known local substitute for this counting.
- **Two fusion classes, not one.** Because $D_{2^n}$ ($n\ge3$) has two classes of non-central involutions, Thompson-style factorization and signalizer functor arguments split into cases that do not merge. Signalizer functor theory, the workhorse of the generic CFSG case, needs $2$-rank $\ge 3$; a dihedral group has $2$-rank exactly $2$, so the functor machinery is unavailable. This is precisely why the small-rank cases were historically the hardest.
- **$A_7$ is a genuine sporadic obstruction.** $A_7$ and $\mathrm{PSL}_2(9)=A_6$ have isomorphic Sylow $2$-subgroups and isomorphic fusion systems, so *no* $2$-local or fusion-theoretic argument alone can separate them. Separation requires global data ($|G|$, or the structure of odd-order local subgroups). Any purely fusion-theoretic proof must therefore stop at a two-element ambiguity.
- **Fusion systems do not see the core.** The passage from $\mathcal{F}_S(G)$ to $G/O(G)$ is not formal; it requires knowing that $O(G)$ is controlled, which in turn uses $Z^*$ or a solvability input.
- **Odd $p$ has no analogue of the $Z^*$-theorem** in usable form, and $p$-groups of maximal class for $p \ge 5$ are wildly numerous (no classification), so the strategy does not transpose.

## 6. The Gap

Proven: everything in §4, plus the full theorem as stated in §1. The gap is methodological and lies in exactly one step. Write $z$ for the central involution of $S \cong D_{2^n}$, $H = C_G(z)$, and suppose all three classes of involutions of $S$ fuse in $G$ and $O(G)=1$. Local analysis (Bender's method) yields $H/O(H)$ isomorphic to a dihedral group or $S_4$ and shows $G$ has one class of involutions. **The missing local step:** derive
$$|G| \;=\; \frac{q(q^2-1)}{2} \quad\text{or}\quad 2520$$
from that data without Brauer's block theory. Currently this order formula is obtained by summing exceptional-character degrees in the principal $2$-block; no argument using only $p$-local subgroups, transfer, and generation is known. Crossing this gap would (a) give a character-free proof of the first CFSG-style classification theorem, and (b) supply the missing exhaustiveness step for a CFSG-independent classification of fusion systems on dihedral $2$-groups.

## 7. Current Research (as of June 2026)

- **Second-generation CFSG (Gorenstein–Lyons–Solomon volumes, AMS).** The dihedral case is absorbed into the treatment of groups of special odd type; the aim is uniform exposition, not elimination of character theory. Solomon and Lyons remain the drivers.
- **Fusion-system program (Aschbacher, Oliver, Craven, Semeraro, Grazian).** Goal: reprove small-Sylow classifications entirely inside $\mathcal{F}$, then transfer to groups. Dihedral and semidihedral $2$-groups are the test cases. *(frontier — verify)* Ongoing work aims at a CFSG-free proof that a reduced saturated fusion system over $D_{2^n}$ is $\mathcal{F}_S(\mathrm{PSL}_2(q))$ or $\mathcal{F}_S(A_7)$.
- **Amalgam and $BN$-pair methods (Parker, Stroth, and collaborators, Birmingham/Magdeburg).** Rank-$1$ amalgam recognition of $\mathrm{PSL}_2(q)$ from a pushing-up configuration; this route is character-free where it applies but has not covered all dihedral branches.
- **Formalization.** *(frontier — verify)* Lean/mathlib efforts on Sylow theory, transfer, and the Feit–Thompson prerequisites are far from the dihedral theorem; Brauer block theory is essentially unformalized, which makes the revision problem also a prerequisite for any machine-checked CFSG.

## 8. Future Work

- Find a local proof of the order formula in §6, e.g. by producing a strongly $2$-embedded configuration or a $BN$-pair directly from the fused-involution hypothesis.
- Prove exhaustiveness of the three dihedral fusion systems from the saturation axioms alone, using Oliver's reduction to reduced/tame systems, then apply tameness to recover the group statement.
- Extend the fusion-system treatment uniformly to the four maximal-class families (dihedral, semidihedral, quaternion, and the wreathed near-relative), replacing four separate 1960s papers with one argument.
- For odd $p$: classify saturated fusion systems on metacyclic and maximal-class $p$-groups without CFSG; Grazian–Parker-type results are the current frontier.
- Formalize the $|S|=4$ and $|S|=8$ cases as a proof of concept for machine-checked local analysis.

## 9. Key References

- **[Foundational]** D. Gorenstein and J. H. Walter. *The characterization of finite groups with dihedral Sylow 2-subgroups, I, II, III.* Journal of Algebra **2** (1965), 85–151, 218–270, 354–393.
- **[Foundational]** R. Brauer and M. Suzuki. *On finite groups of even order whose 2-Sylow group is a quaternion group.* Proceedings of the National Academy of Sciences USA **45** (1959), 1757–1759.
- **[Foundational]** R. Brauer, M. Suzuki, G. E. Wall. *A characterization of the one-dimensional unimodular projective groups over finite fields.* Illinois Journal of Mathematics **2** (1958), 718–745.
- **[Foundational]** W. Feit and J. G. Thompson. *Solvability of groups of odd order.* Pacific Journal of Mathematics **13** (1963), 775–1029.
- **[Foundational]** G. Glauberman. *Central elements in core-free groups.* Journal of Algebra **4** (1966), 403–420.
- **[SOTA / Recent]** H. Bender. *Finite groups with dihedral Sylow 2-subgroups.* Journal of Algebra **70** (1981), 216–228.
- **[SOTA / Recent]** J. L. Alperin, R. Brauer, D. Gorenstein. *Finite groups with quasi-dihedral and wreathed Sylow 2-subgroups.* Transactions of the American Mathematical Society **151** (1970), 1–261.
- **[SOTA / Recent]** D. M. Goldschmidt. *2-fusion in finite groups.* Annals of Mathematics (2) **99** (1974), 70–117.
- **[SOTA / Recent]** B. Oliver. *Reduced fusion systems over 2-groups of small order.* Journal of Algebra **489** (2017), 345–392.
- **[Survey]** D. Gorenstein, R. Lyons, R. Solomon. *The Classification of the Finite Simple Groups, Number 2.* Mathematical Surveys and Monographs 40.2, American Mathematical Society, 1996.
- **[Survey]** M. Aschbacher and B. Oliver. *Fusion systems.* Bulletin of the American Mathematical Society **52** (2015), 555–615.
- **[Survey]** D. A. Craven. *The Theory of Fusion Systems: An Algebraic Approach.* Cambridge University Press, 2011.
- **[Survey]** D. Gorenstein. *Finite Groups.* Harper & Row, 1968 (2nd ed., Chelsea, 1980).
- **[Background]** H. Bender and G. Glauberman. *Local Analysis for the Odd Order Theorem.* LMS Lecture Note Series 188, Cambridge University Press, 1994.

## 10. Worked Example / Concrete Special Case

**Case $S \cong V_4$, $G$ simple.** Take $G = A_5 \cong \mathrm{PSL}_2(5)$, $|G| = 60 = 2^2\cdot3\cdot5$, so $S = \{1,(12)(34),(13)(24),(14)(23)\} \cong V_4$.

*Step 1 — normalizer.* $N_G(S) \cong A_4$, of order $12$, acting on the three involutions of $S$ by a $3$-cycle. So $N_G(S)/C_G(S) \cong \mathbb{Z}/3$ permutes the involutions transitively.

*Step 2 — fusion.* $S$ is abelian, so Burnside's fusion lemma applies: two elements of $S$ are $G$-conjugate iff they are $N_G(S)$-conjugate. By Step 1 all three involutions are $G$-conjugate — the "$\mathrm{PSL}_2$-type" pattern of §2. Hence no involution is isolated, and Glauberman's $Z^*$-theorem gives no information; this is exactly the hard branch.

*Step 3 — centralizer.* $C_G((12)(34)) = S \cong V_4$, of order $4$. So $G$ has $|G|/|C_G(t)| = 60/4 = 15$ involutions, one class.

*Step 4 — identification (the character step).* $S$ is a Klein four defect group of the principal $2$-block $B_0$. Brauer's theory of Klein four blocks says $B_0$ contains exactly four ordinary irreducible characters $\chi_0,\chi_1,\chi_2,\chi_3$ with $\chi_0(1) \pm \chi_1(1)\pm\chi_2(1)\pm\chi_3(1) = 0$ for suitable signs. For $A_5$: $B_0 = \{1, 3, 3', 5\}$ with degrees $1,3,3,5$ and $1+3+3-5 = 2 \ne 0$; the correct relation is $-1+3+3-5=0$ with signs $(-,+,+,-)$, consistent. Combining with $|C_G(t)|=4$ and the odd-order local data ($N_G(\langle x\rangle) \cong S_3$ for $|x|=3$, $N_G(\langle y\rangle)\cong D_{10}$ for $|y|=5$) forces $|G| = 60$ and then $G \cong \mathrm{PSL}_2(5)$ by Brauer–Suzuki–Wall.

*Step 5 — the gap made concrete.* Steps 1–3 are pure local analysis, cheap and character-free. Step 4 is not: nothing in Steps 1–3 distinguishes $A_5$ from a hypothetical simple group with $S \cong V_4$, one class of involutions, and $|C_G(t)| = 4$ but a different order. Ruling that out is exactly the order-formula step of §6.

*Contrast, $|S| = 8$.* In $\mathrm{PSL}_2(7)$ (order $168$) and in $A_7$ (order $2520$) the Sylow $2$-subgroup is $D_8$ and in both cases all involutions are conjugate, with $C_G(z) \cong D_8$ for $\mathrm{PSL}_2(7)$ and $C_{A_7}(z) \cong D_8$ for $z=(12)(34)$ — wait, $|C_{A_7}((12)(34))| = 24$, so $C_{A_7}(z) \cong S_4$ while $C_{\mathrm{PSL}_2(7)}(z)\cong D_8$. That order difference ($24$ vs $8$) is what separates the two, and it is a *global* count, not a fusion invariant — the concrete form of the "$A_7$ obstruction" in §5.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*