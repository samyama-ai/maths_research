---
id: 08-logic-set-theory/perfect-set-property-for-projective-sets
title: "Perfect Set Property for Projective Sets"
topic: 08-logic-set-theory
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Perfect Set Property for Projective Sets

> **Topic:** Mathematical Logic & Set Theory · **ID:** `08-logic-set-theory/perfect-set-property-for-projective-sets` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

A set $A \subseteq \omega^\omega$ has the **perfect set property** (PSP) if $A$ is countable or contains a homeomorphic copy of Cantor space $2^\omega$. PSP implies the continuum hypothesis holds for $A$: $|A| \in \{\aleph_0, 2^{\aleph_0}\}$.

The problem: **for which pointclasses of the projective hierarchy does ZFC prove PSP, and what is the exact consistency strength of PSP at each level?**

Settled endpoints: ZFC proves PSP for $\mathbf{\Sigma}^1_1$ (Suslin) and refutes it for $\mathbf{\Pi}^1_1$ under $V=L$ (Gödel). "Every projective set has PSP" is equiconsistent with an inaccessible cardinal. What remains open is a cluster of finer questions:

- The exact large-cardinal strength of $\mathbf{\Sigma}^1_n$-PSP for $n \ge 3$ *level by level*, matched to inner-model-theoretic hypotheses rather than to the single inaccessible that suffices for the whole hierarchy at once.
- Whether PSP for definable sets in **generalized Baire space** $\kappa^\kappa$ ($\kappa$ uncountable regular) has any consistency strength beyond the known bounds.
- Optimal separations: which implications between PSP, Lebesgue measurability (LM) and the Baire property (BP) hold levelwise, and which reverse.

A resolution means: for each $n$, a statement $\Phi_n$ in the language of inner model theory such that ZFC $\vdash$ ($\mathbf{\Sigma}^1_n$-PSP $\leftrightarrow$ $\Phi_n$), or an equiconsistency with an explicitly named large cardinal.

## 2. Mathematical Foundations

**Polish spaces and the projective hierarchy.** Work in $\mathcal{N} = \omega^\omega$ with the product topology. Define
$$\mathbf{\Sigma}^1_1 = \{\,\exists y\,\in\omega^\omega\ (x,y)\in C : C \text{ closed in } \mathcal{N}^2\,\},\quad \mathbf{\Pi}^1_n = \neg\mathbf{\Sigma}^1_n,\quad \mathbf{\Sigma}^1_{n+1} = \exists^{\omega^\omega}\mathbf{\Pi}^1_n,$$
$\mathbf{\Delta}^1_n = \mathbf{\Sigma}^1_n \cap \mathbf{\Pi}^1_n$. Boldface classes allow real parameters; lightface $\Sigma^1_n$ does not. The projective sets are $\bigcup_n \mathbf{\Sigma}^1_n$.

**Perfect sets.** $P \subseteq \mathcal{N}$ is perfect if it is nonempty, closed, and has no isolated points; every such $P$ satisfies $|P| = 2^{\aleph_0}$. A set is **thin** if it contains no perfect subset.

$$\mathrm{PSP}(\Gamma) :\iff \forall A \in \Gamma\ \big(|A| \le \aleph_0 \ \vee\ \exists P \subseteq A \text{ perfect}\big).$$

**Cantor–Bendixson.** For closed $F$, $F = P \cup S$ with $P$ perfect and $S$ countable open-in-$F$ scattered part; the derivative $F^{(\alpha+1)} = \{x \in F^{(\alpha)} : x \text{ not isolated in } F^{(\alpha)}\}$ stabilizes at a countable ordinal.

**Relative constructibility.** $L[a]$ is the constructible hierarchy relative to a real $a$; $\omega_1^{L[a]}$ is the least ordinal that $L[a]$ believes is $\aleph_1$. Write
$$\mathrm{IR} :\iff \forall a \in \omega^\omega\ \ \omega_1^{L[a]} < \omega_1 \qquad (\text{"}\omega_1 \text{ is inaccessible to reals"}).$$

**Key theorems relied on.**

1. **Suslin (1917).** Every $\mathbf{\Sigma}^1_1$ set has PSP. Proof by the Cantor scheme: a Suslin representation $A = p[T]$ yields either a rank-analysis making $A$ countable or a perfect embedding of $2^{<\omega}$ into $T$.
2. **Mansfield–Solovay.** If $A$ is $\mathbf{\Sigma}^1_2(a)$ and $A \not\subseteq L[a]$, then $A$ contains a perfect subset. Equivalently, $A = p[T]$ for a tree $T \in L[a]$ on $\omega \times \omega_1$, and $p[T] \subseteq L[a]$ unless $T$ has a perfect splitting subtree.
3. **Solovay.** $\mathrm{PSP}(\mathbf{\Pi}^1_1) \iff \mathrm{PSP}(\mathbf{\Sigma}^1_2) \iff \mathrm{IR}$.
4. **Davis (1964), perfect set game.** For $A \subseteq 2^\omega$, in $G^*_A$ player I plays finite binary strings $s_i$, II plays bits $\varepsilon_i$; the run produces $x = s_0^{\frown}\!\langle\varepsilon_0\rangle^{\frown} s_1 \cdots$ and II wins iff $x \in A$. Then: II has a winning strategy $\iff A$ contains a perfect set; I has one $\iff A$ is countable. Hence $\mathrm{Det}(\Gamma) \Rightarrow \mathrm{PSP}(\Gamma)$ for reasonable $\Gamma$ closed under the game's continuous preimages.

## 3. History & State of the Art (SOTA)

- **1884.** Cantor proves closed subsets of $\mathbb{R}$ satisfy the CH dichotomy, verifying CH for closed sets.
- **1916.** Alexandrov and Hausdorff independently extend PSP to Borel sets.
- **1917.** Suslin extends it to analytic sets; Luzin asks whether it extends to co-analytic sets. Luzin's later verdict on the projective regularity questions — that one "will never know" — was prophetic.
- **1938–40.** Gödel's $L$ gives a $\Sigma^1_2$ good wellordering of the reals and an uncountable thin $\Pi^1_1$ set, so $\mathrm{PSP}(\mathbf{\Pi}^1_1)$ is not provable.
- **1957.** Specker: if every uncountable set of reals has a perfect subset then $\omega_1$ is inaccessible in $L$; so PSP has genuine large-cardinal strength.
- **1964–70.** Mycielski–Świerczkowski and Davis link determinacy to regularity; Solovay's Levy-collapse model over an inaccessible gives $\mathrm{ZF}+\mathrm{DC}+$"all sets of reals have PSP".
- **1970.** Mansfield's perfect-set theorem for $\Sigma^1_2$; Solovay's cardinality analysis of $\Sigma^1_2$ sets.
- **1975.** Kechris and Guaspari–Sacks: there is a **largest thin $\Pi^1_1$ set** $C_1$, and $C_1 = \{x : x \in L_{\omega_1^x}[x]\}$; likewise a largest thin $\Sigma^1_2$ set $C_2 = \mathbb{R} \cap L$ under suitable hypotheses.
- **1984.** Shelah shows the inaccessible is *necessary* for measurability-type statements but not for BP, isolating PSP and LM as the strength-carrying properties.
- **1985–89.** Martin–Steel and Woodin: $n$ Woodin cardinals with a measurable above give $\mathbf{\Pi}^1_{n+1}$-determinacy, hence PSP throughout the projective hierarchy under $\omega$ Woodins; all sets in $L(\mathbb{R})$ have PSP under $\mathrm{AD}^{L(\mathbb{R})}$.
- **1999–2010.** Brendle–Löwe and Ikegami give a uniform "Solovay-type" template characterizing $\mathbf{\Delta}^1_2$/$\mathbf{\Sigma}^1_2$ regularity for arbitrary arboreal forcings; PSP is the instance for Sacks forcing, where the $\mathbf{\Delta}^1_2$ and $\mathbf{\Sigma}^1_2$ levels coincide.
- **2010s–2020s.** Transfer to $\kappa^\kappa$ (Schlicht; Lücke–Motto Ros–Schlicht) and optimal-strength determinacy work (Müller–Schindler–Woodin).

## 4. Partial Results / Verified Cases

| Class | Status | Hypothesis |
|---|---|---|
| Closed, $F_\sigma$, Borel | PSP holds | ZF + DC |
| $\mathbf{\Sigma}^1_1$ (analytic) | PSP holds | ZF + DC (Suslin) |
| $\mathbf{\Pi}^1_1$, $\mathbf{\Sigma}^1_2$, $\mathbf{\Delta}^1_2$ | PSP $\iff \mathrm{IR}$ | independent of ZFC |
| $\mathbf{\Pi}^1_1$ | PSP holds | any measurable cardinal; or $\forall x\,(x^\sharp$ exists$)$ |
| $\mathbf{\Sigma}^1_{n+1}$ | PSP holds | $\mathbf{\Delta}^1_n$-determinacy; $n-1$ Woodins + measurable above |
| all projective | PSP holds | one inaccessible (Levy collapse), or PD |
| all sets in $L(\mathbb{R})$ | PSP holds | one inaccessible (Solovay 1970) |
| all sets of reals | PSP holds | ZF + DC + AD; equiconsistent with an inaccessible |

Concrete parameters: $\mathrm{PSP}(\mathbf{\Sigma}^1_2)$ already implies $\omega_1$ is inaccessible in $L[a]$ for every real $a$, so the level-2 statement alone carries the full inaccessible strength; nothing weaker than an inaccessible suffices at *any* projective level $\ge 2$, and nothing stronger is needed at *any* level. In $L$, $C_1 = \mathbb{R}$ is an uncountable thin $\Pi^1_1$ set of size $2^{\aleph_0} = \aleph_1$. Harrington (1977) shows one can have a thin $\Pi^1_1$ set of size $\aleph_1$ together with $2^{\aleph_0}$ arbitrarily large.

## 5. Principal Obstacles

- **No absoluteness beyond level 2.** Shoenfield absoluteness pins $\Sigma^1_2$ truth between $V$ and $L[a]$, which is exactly why Mansfield–Solovay closes level 2. At $\Sigma^1_3$ the tree representations are not in $L[a]$, and only sharps/Woodin cardinals restore the needed homogeneously Suslin representations. Classical tree analysis therefore stops at 2.
- **Consistency-strength ceiling collapses information.** Because one inaccessible suffices for *all* projective levels, consistency strength cannot separate levels; a levelwise theory needs finer invariants (e.g. "for all $x$, $M_n^\sharp(x)$ exists" versus mere closure properties of $\omega_1$), and no candidate $\Phi_n$ is known to be both necessary and sufficient for $n\ge 3$.
- **Core model induction is lossy.** Lower-bound arguments from $\mathbf{\Sigma}^1_3$-regularity produce inner models with Woodin cardinals only under extra hypotheses; the PSP statement is $\Sigma$-weak — it says a set is countable *or* large — and does not by itself yield the iterability needed to run $K$-constructions.
- **PSP is a "one-sided" property.** Unlike LM and BP, which are $\sigma$-ideal quotients with a forcing-algebra (null/meager) attached, PSP corresponds to Sacks forcing, whose ideal (countable-supported perfect sets) is not $\sigma$-generated in the same way. This breaks the Solovay-style characterization machinery above level 2.
- **Generalized Baire space.** For uncountable $\kappa$, $\kappa^\kappa$ is not $\sigma$-compact, the Cantor–Bendixson analysis fails for closed sets in ZFC, and $\mathbf{\Sigma}^1_1(\kappa)$-PSP outright fails (e.g. the club filter yields a thin non-small $\Sigma^1_1$ set). Everything must be rebuilt from long games.

## 6. The Gap

Proven (§4): a complete equivalence at levels $\mathbf{\Pi}^1_1$/$\mathbf{\Sigma}^1_2$ ($\mathrm{PSP} \iff \mathrm{IR}$), and matching upper/lower consistency bounds (one inaccessible) for the entire projective hierarchy.

Not proven (§1): a *characterization* of $\mathrm{PSP}(\mathbf{\Sigma}^1_n)$ for $n \ge 3$ in the style of Solovay's, i.e. a statement of the form "for all reals $x$ and all $n$-small mice $M$ containing $x$, $\omega_1^M < \omega_1$". The precise step to be crossed: produce, from $\mathrm{PSP}(\mathbf{\Sigma}^1_3)$ alone, a $\Sigma^1_3$-correct iterable inner model in which the third-level thin set can be computed — the analogue of "$\mathbf{\Sigma}^1_2$ sets are $\omega_1$-Suslin in $L[a]$" one level up. Equivalently: identify the canonical largest thin $\mathbf{\Pi}^1_3$ set $C_3$ and prove it is $\mathbb{R} \cap M_1$-like without assuming $\mathbf{\Delta}^1_2$-determinacy.

## 7. Current Research (as of June 2026)

- **Optimal-strength descriptive set theory** (Münster: Schindler; Vienna: Müller; Bonn/Barcelona: Schlicht, Aguilera). Programme: match each projective regularity property with the existence of mice $M_n^\sharp$. Aguilera–Müller-type results deriving determinacy from optimal hypotheses are the technical engine. *(frontier — verify)*
- **Generalized Baire spaces.** Schlicht's long-game perfect set property for $\kappa^\kappa$, and the Hurewicz-dichotomy programme of Lücke–Motto Ros–Schlicht, aim at a $\kappa$-analogue of "all definable sets have PSP" from an inaccessible or a $\kappa$-superstrong hypothesis. Open: the exact strength of "all $\kappa$-projective subsets of $\kappa^\kappa$ have the $\kappa$-PSP". *(frontier — verify)*
- **Idealized forcing / Solovay templates.** Continuations of Ikegami's framework, relating $\mathbf{\Sigma}^1_2(\mathbb{P})$-regularity to $\mathbb{P}$-absoluteness, being pushed to $\mathbf{\Sigma}^1_3$ under $M_1^\sharp$ closure.
- **Choiceless contexts.** PSP under $\mathrm{ZF}+\mathrm{DC}+$"all sets are Suslin", and PSP in Woodin's $\mathrm{AD}^+$ framework; the question of PSP for sets beyond $L(\mathbb{R})$ in the derived model.

## 8. Future Work

1. Compute the largest thin $\mathbf{\Pi}^1_3$ set outright, without determinacy hypotheses, as a set of reals of an $M_1$-like mouse; this is the recognized route to a Solovay-style level-3 characterization.
2. Prove or refute: $\mathrm{PSP}(\mathbf{\Sigma}^1_3)$ implies $\forall x\,(M_1^\sharp(x)$ exists$)$. A negative answer would show PSP is strictly weaker than LM at level 3.
3. Settle the levelwise implication structure among $\{\mathrm{PSP}, \mathrm{LM}, \mathrm{BP}\}$ at $n \ge 3$, extending Shelah's level-2 separations.
4. Develop Cantor–Bendixson analysis for closed subsets of $\kappa^\kappa$ under $\kappa$-perfect-set games, and determine whether the $\kappa$-PSP for $\kappa$-analytic sets is consistent at a successor $\kappa$.
5. Explore effective/lightface versions: strength of "every lightface $\Sigma^1_2$ set has PSP" (which is strictly weaker: it needs only $\omega_1^L < \omega_1$).

## 9. Key References

- **[Foundational]** M. Suslin. *Sur une définition des ensembles mesurables B sans nombres transfinis.* C. R. Acad. Sci. Paris 164, 1917.
- **[Foundational]** K. Gödel. *The Consistency of the Continuum Hypothesis.* Princeton University Press, 1940.
- **[Foundational]** E. Specker. *Zur Axiomatik der Mengenlehre (Fundierungsaxiom und Auswahlaxiom).* Zeitschrift für mathematische Logik und Grundlagen der Mathematik 3, 1957, 173–210.
- **[Foundational]** M. Davis. *Infinite games of perfect information.* In: Advances in Game Theory, Annals of Mathematics Studies 52, Princeton University Press, 1964, 85–101.
- **[Foundational]** R. M. Solovay. *A model of set-theory in which every set of reals is Lebesgue measurable.* Annals of Mathematics 92, 1970, 1–56.
- **[Foundational]** R. Mansfield. *Perfect subsets of definable sets of real numbers.* Pacific Journal of Mathematics 35, 1970, 451–457.
- **[SOTA / Recent]** A. S. Kechris. *The theory of countable analytical sets.* Transactions of the AMS 202, 1975, 259–297.
- **[SOTA / Recent]** L. Harrington. *Long projective wellorderings.* Annals of Mathematical Logic 12, 1977, 1–24.
- **[SOTA / Recent]** S. Shelah. *Can you take Solovay's inaccessible away?* Israel Journal of Mathematics 48, 1984, 1–47.
- **[SOTA / Recent]** D. A. Martin, J. R. Steel. *A proof of projective determinacy.* Journal of the AMS 2, 1989, 71–125.
- **[SOTA / Recent]** J. Brendle, B. Löwe. *Solovay-type characterizations for forcing-algebras.* Journal of Symbolic Logic 64, 1999, 1307–1323.
- **[SOTA / Recent]** D. Ikegami. *Forcing absoluteness and regularity properties.* Annals of Pure and Applied Logic 161, 2010, 879–894.
- **[SOTA / Recent]** P. Schlicht. *Perfect subsets of generalized Baire spaces and long games.* Journal of Symbolic Logic 82, 2017, 1317–1355.
- **[Survey]** A. Kanamori. *The Higher Infinite.* 2nd ed., Springer, 2003.
- **[Survey]** A. S. Kechris. *Classical Descriptive Set Theory.* Graduate Texts in Mathematics 156, Springer, 1995.
- **[Survey]** Y. N. Moschovakis. *Descriptive Set Theory.* 2nd ed., Mathematical Surveys and Monographs 155, AMS, 2009.
- **[Survey]** T. Jech. *Set Theory.* 3rd millennium edition, Springer, 2003 (Ch. 25: perfect set property and the projective hierarchy).

## 10. Worked Example / Concrete Special Case

**The level-2 dichotomy, computed both ways.**

*Failure side ($V=L$).* Let
$$C_1 = \{\, x \in 2^\omega : x \in L_{\omega_1^x}[x] \,\},$$
where $\omega_1^x$ is the least $x$-admissible ordinal. ZFC proves $C_1$ is $\Pi^1_1$ and thin (Guaspari–Kechris–Sacks): if $P \subseteq C_1$ were perfect, pick $x \in P$ Cohen-generic over a countable elementary submodel coding $P$; then $x \notin L_{\omega_1^x}[x]$ by genericity, contradiction. Now assume $V=L$. Every real is constructible and appears in $L_{\omega_1^x}[x]$, so $C_1 = 2^\omega$, which has size $\aleph_1 = 2^{\aleph_0}$. Thus $C_1$ is an uncountable $\Pi^1_1$ set with no perfect subset: $\mathrm{PSP}(\mathbf{\Pi}^1_1)$ fails in $L$.

*Success side (Levy collapse).* Let $\kappa$ be inaccessible and force with $\mathrm{Coll}(\omega, <\kappa)$, the finite-support product collapsing every $\alpha < \kappa$ to $\omega$. In $V[G]$, $\kappa = \omega_1$. Fix a real $a \in V[G]$. By the $\kappa$-cc and a nice-name argument, $a \in V[G \restriction \alpha]$ for some $\alpha < \kappa$; the tail forcing $\mathrm{Coll}(\omega,[\alpha,\kappa))$ collapses $\alpha^+$, so
$$\omega_1^{L[a]} \le \big(|\alpha|^+\big)^{V[G\restriction\alpha]} < \kappa = \omega_1^{V[G]},$$
i.e. $\mathrm{IR}$ holds. Now take any $\mathbf{\Sigma}^1_2(a)$ set $A$. Since $\omega_1^{L[a]}$ is countable, $L[a]$ satisfies CH, so $|\mathbb{R} \cap L[a]|^{L[a]} = \omega_1^{L[a]}$, and in $V[G]$ that set is countable. Mansfield–Solovay gives the dichotomy: either $A \subseteq L[a]$ — hence $A$ is countable — or $A$ contains a perfect subset. So every $\mathbf{\Sigma}^1_2$ set in $V[G]$ has PSP.

*The counting that drives it.* $\aleph_0 \le |\mathbb{R} \cap L[a]| \le |\omega_1^{L[a]}|$. Under $V=L$ this is $\aleph_1$ and PSP dies; after the collapse it is $\aleph_0$ and PSP lives. The single number $\omega_1^{L[a]}$ decides level 2 completely — and the open problem of §6 is precisely that no such single number is known to decide level 3.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*