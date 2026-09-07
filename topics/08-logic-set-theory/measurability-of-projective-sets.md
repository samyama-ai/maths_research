---
id: 08-logic-set-theory/measurability-of-projective-sets
title: "Measurability of Projective Sets"
topic: 08-logic-set-theory
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Measurability of Projective Sets

> **Topic:** Mathematical Logic & Set Theory · **ID:** `08-logic-set-theory/measurability-of-projective-sets` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Let $\mathbb{R}$ (or Baire space $\omega^\omega$) carry Lebesgue measure $\lambda$. A set $A \subseteq \mathbb{R}$ is **projective** if it is obtained from a Borel set by finitely many alternations of continuous projection and complementation. The problem:

> **Is every projective set Lebesgue measurable?**

The answer is not decidable in $\mathsf{ZFC}$. The live problem has three components:

1. **Level-by-level calibration.** For each $n$, determine the exact consistency strength and the exact combinatorial characterization of "every $\mathbf{\Sigma}^1_n$ set is Lebesgue measurable" (abbreviated $\mathbf{\Sigma}^1_n(\lambda)$).
2. **The axiomatic question.** Identify axioms that decide measurability at *all* projective levels and are independently justified. Projective Determinacy ($\mathsf{PD}$) does this; the open part is whether $\mathsf{PD}$ can be grounded on hypotheses weaker or more evident than large cardinals, and whether the inner-model program can reach the cardinals that imply it.
3. **Uniformity across regularity properties.** Determine which regularity properties (measurability, Baire property, perfect set property, Ramsey property, $\sigma$-ideal regularity for arbitrary definable proper forcings) imply which others at each projective level.

A complete resolution of (1) means: for every $n$, a large-cardinal or transcendence statement $T_n$ with $\mathsf{ZFC} \vdash \mathbf{\Sigma}^1_n(\lambda) \leftrightarrow T_n$, plus matching consistency-strength bounds. Components (2) and (3) remain open in the senses given in §6.

## 2. Mathematical Foundations

**Projective hierarchy.** For $A \subseteq (\omega^\omega)^k$:
$$\mathbf{\Sigma}^1_1 = \{\,\exists y\, B : B \text{ closed}\,\},\qquad \mathbf{\Pi}^1_n = \neg\,\mathbf{\Sigma}^1_n,\qquad \mathbf{\Sigma}^1_{n+1} = \exists^{\omega^\omega} \mathbf{\Pi}^1_n,\qquad \mathbf{\Delta}^1_n = \mathbf{\Sigma}^1_n \cap \mathbf{\Pi}^1_n.$$
Boldface classes allow a real parameter; lightface $\Sigma^1_n$ do not. The projective sets are $\bigcup_n \mathbf{\Sigma}^1_n$; $\mathbf{\Delta}^1_1 = $ Borel (Suslin).

**Measurability.** $A$ is $\lambda$-measurable iff there is a Borel $B$ with $A \triangle B \in \mathcal{N}$, the $\sigma$-ideal of null sets. Write $\mathbf{\Sigma}^1_n(\lambda)$ for "all $\mathbf{\Sigma}^1_n$ sets are measurable". Note $\mathbf{\Sigma}^1_n(\lambda) \Rightarrow \mathbf{\Pi}^1_n(\lambda) \Rightarrow \mathbf{\Delta}^1_{n+1}(\lambda)$ (complements and the fact that $\mathbf{\Delta}^1_{n+1}$ sets are $\omega_1$-unions of $\mathbf{\Pi}^1_n$-ish pieces via Shoenfield-type analysis).

**Random and Cohen reals.** $x$ is **random over** $M$ iff $x$ avoids every null Borel set coded in $M$; **Cohen over** $M$ iff it avoids every meager Borel set coded in $M$. These are the generics for measure algebra forcing $\mathbb{B}$ and Cohen forcing $\mathbb{C}$.

**Determinacy.** For $A \subseteq \omega^\omega$, $G(A)$ is the infinite two-player game with payoff $A$; $\mathrm{Det}(\Gamma)$ says every $A \in \Gamma$ gives a determined game. $\mathsf{PD} = \mathrm{Det}(\bigcup_n \mathbf{\Sigma}^1_n)$.

**Key theorems the problem rests on.**

- *(Mycielski–Świerczkowski 1964)* $\mathrm{Det}(\Gamma)$ for a reasonably closed $\Gamma$ implies every set in $\Gamma$ is $\lambda$-measurable, via the covering game. Hence $\mathsf{PD} \Rightarrow$ all projective sets measurable.
- *(Solovay 1969)* $\mathbf{\Sigma}^1_2(\lambda) \iff$ for every real $r$, $\{x : x \text{ random over } L[r]\}$ has measure one. Dually $\mathbf{\Delta}^1_2(\lambda) \iff \forall r\,\exists x$ random over $L[r]$ (Judah–Shelah).
- *(Gödel 1938–40)* In $L$ there is a $\Sigma^1_2$ good wellordering of $\mathbb{R}$; hence a $\mathbf{\Delta}^1_2$ non-measurable set (§10).
- *(Shoenfield)* $\mathbf{\Sigma}^1_2$ statements are absolute between $V$ and inner models containing $\omega_1$ — which is exactly why the hierarchy is rigid at level 2 and wild above.

## 3. History & State of the Art

- **1917.** Lusin proves analytic ($\mathbf{\Sigma}^1_1$) sets are Lebesgue measurable, from the Suslin operation $\mathcal{A}$ preserving measurability (Lusin–Sierpiński). Hence $\mathbf{\Pi}^1_1$ too. Lusin declares he "does not know and will never know" whether $\mathbf{\Sigma}^1_2$ sets are measurable.
- **1938–40.** Gödel's $L$ gives a $\mathbf{\Delta}^1_2$ non-measurable set: Lusin's question is not positively answerable in $\mathsf{ZFC}$.
- **1964.** Mycielski–Świerczkowski: $\mathsf{AD}$ implies all sets are measurable, linking determinacy to regularity.
- **1969.** Solovay: a measurable cardinal implies $\mathbf{\Sigma}^1_2(\lambda)$ (and $\mathbf{\Sigma}^1_2$ sets have the perfect set property).
- **1970.** Solovay's model: from an inaccessible $\kappa$, the Lévy collapse $\mathrm{Coll}(\omega,{<}\kappa)$ yields $L(\mathbb{R})\models \mathsf{ZF+DC}+$ "every set of reals is measurable"; in the $\mathsf{ZFC}$ extension itself, every set definable from a real and an ordinal — in particular every projective set — is measurable.
- **1984.** Shelah: the inaccessible is necessary. $\mathbf{\Sigma}^1_3(\lambda)$ implies $\aleph_1$ is inaccessible in $L[r]$ for all reals $r$. Raisonnier gave a streamlined proof (rapid filters). By contrast the Baire property needs no inaccessible: Shelah built a model of $\mathsf{ZF+DC}$ + "all sets have the Baire property" from $\mathsf{ZFC}$ alone.
- **1985–88.** Martin–Steel: $n$ Woodin cardinals with a measurable above imply $\mathbf{\Pi}^1_{n+1}$ determinacy; infinitely many Woodins imply $\mathsf{PD}$. Woodin: a supercompact implies $\mathsf{AD}^{L(\mathbb{R})}$, later reduced to $\omega$ Woodins with a measurable above.
- **1988–95.** Woodin's converse via core model theory: $\mathsf{PD}$ is equiconsistent with "there are infinitely many Woodin cardinals". Neeman and Woodin obtain optimal level-by-level equivalences ($\mathbf{\Pi}^1_{n+1}$-determinacy $\iff$ closure under the sharp-like operator $M_n^{\\#}$).
- **1989.** Judah–Shelah separate $\mathbf{\Delta}^1_2(\lambda)$ from $\mathbf{\Sigma}^1_2(\lambda)$ and from Baire-property analogues by forcing.
- **2005–present.** Steel: $\mathsf{PFA} \Rightarrow \mathsf{AD}^{L(\mathbb{R})}$ by core model induction, so strong forcing axioms also deliver projective measurability. Sargsyan's descriptive inner model theory pushes the inductive machinery well past $\mathsf{AD}^{L(\mathbb{R})}$.

## 4. Partial Results / Verified Cases

| Level | Status in $\mathsf{ZFC}$ | Exact characterization |
|---|---|---|
| Borel, $\mathbf{\Sigma}^1_1$, $\mathbf{\Pi}^1_1$ | **Provable** (Lusin 1917) | — |
| $\mathbf{\Delta}^1_2$ | Independent | $\iff \forall r\ \exists x$ random over $L[r]$ (Judah–Shelah 1989) |
| $\mathbf{\Sigma}^1_2$ | Independent; follows from a measurable cardinal | $\iff \forall r\ \lambda(\{x:\text{random over }L[r]\}) = 1$ (Solovay 1969) |
| $\mathbf{\Sigma}^1_3$ | Independent | Implies $\forall r\ (\aleph_1 \text{ inaccessible in } L[r])$ (Shelah 1984) |
| $\mathbf{\Sigma}^1_{n+2}$ | Follows from $n$ Woodins + measurable above (Martin–Steel) | — |
| All projective | Independent | Equiconsistent with $\mathsf{ZFC} + $ "there is an inaccessible cardinal" (Solovay 1970 upper, Shelah 1984 lower) |

Concrete verified consistency facts:

- Adding $\aleph_2$ random reals over $L$ by a measure algebra gives $\mathbf{\Sigma}^1_2(\lambda)$ while $\aleph_1 = \aleph_1^L$, so the $\mathbf{\Pi}^1_1$ perfect set property fails. Measurability does **not** imply the perfect set property at level 2.
- Adding $\aleph_1$ Cohen reals over $L$ gives $\mathbf{\Delta}^1_2$ Baire property but a non-measurable $\mathbf{\Delta}^1_2$ set (Cohen forcing makes ground-model reals null but not meager). The two regularity properties are genuinely independent of each other.
- Under $\mathsf{PD}$, every projective set is measurable, has the Baire property, the perfect set property and the Ramsey property, and $\mathbf{\Sigma}^1_{2n}$, $\mathbf{\Pi}^1_{2n+1}$ have the scale and uniformization properties (periodicity theorems, Moschovakis).

## 5. Principal Obstacles

- **Absoluteness collapses above level 2.** Shoenfield absoluteness pins $\mathbf{\Sigma}^1_2$ truth to $L[r]$, which is why level 2 admits a clean transcendence characterization. From $\mathbf{\Sigma}^1_3$ upward there is no comparably canonical inner model in $\mathsf{ZFC}$: the correct analogue of $L[r]$ is $M_n^{\\#}(r)$, whose existence is itself the large-cardinal hypothesis. Forcing arguments and classical descriptive set theory cannot manufacture it.
- **Classical tools are level-1 tools.** The Suslin operation $\mathcal{A}$ preserves measurability, which handles $\mathbf{\Sigma}^1_1$ and stops there; $\mathbf{\Sigma}^1_2$ sets are $\omega_1$-unions of Borel sets, and $\sigma$-additivity of $\lambda$ gives nothing for $\omega_1$-unions when $\mathsf{CH}$-like configurations occur. Fourier/harmonic-analytic and Baire-category methods are $\sigma$-ideal-specific and do not transfer across ideals (measure vs. category behave asymmetrically, per Shelah's inaccessible-free Baire theorem).
- **Choice manufactures counterexamples.** $\mathsf{AC}$ gives Vitali and Bernstein sets; the only question is complexity, and complexity is controlled by *definable wellorderings*, i.e. by which inner model computes $\mathbb{R}$. So the problem is inseparable from inner model theory.
- **Inner model theory stalls.** Deriving $\mathsf{PD}$-strength from a hypothesis requires a core model at Woodin-cardinal strength (Mitchell–Steel) plus iterability; iterability at and beyond long extenders (superstrong, supercompact) is not established. Core model induction is delicate and does not currently reach a full "inner model for a supercompact".
- **No canonical justification for $\mathsf{PD}$.** $\mathsf{PD}$ is equiconsistent with infinitely many Woodins, so it cannot be proved from anything of lower consistency strength. Any "evidential" argument (Woodin's $\Omega$-logic, generic absoluteness) is philosophical as much as mathematical.

## 6. The Gap

Proven: measurability at levels $\le \mathbf{\Pi}^1_1$; full level-2 characterizations; full projective measurability from an inaccessible (Solovay) or from $\mathsf{PD}$; the exact consistency strength (one inaccessible) of "all projective sets are measurable".

The gap has two precise edges.

1. **Characterization gap, $n \ge 3$.** There is no known statement $T_n$, expressible without assuming large cardinals exist, with $\mathsf{ZFC} \vdash \mathbf{\Sigma}^1_n(\lambda) \leftrightarrow T_n$ for $n \ge 3$. The natural candidate — "$\forall r$, the reals random over $M_{n-2}^{\\#}(r)$ have measure one" — presupposes $M_{n-2}^{\\#}$ exists, i.e. presupposes the hypothesis it is meant to calibrate. Bridging requires a core model induction that produces $M_n^{\\#}$ from $\mathbf{\Sigma}^1_{n+2}(\lambda)$ alone; this is known only in weak forms.
2. **Justification gap.** $\mathsf{PD}$ delivers a complete, structurally coherent theory of projective sets, but its adoption rests on large cardinals whose existence is unprovable and whose canonical inner models are unconstructed past Woodin-limit-of-Woodins level. Woodin's $\Omega$-conjecture and the HOD conjecture are the current formal attempts to close it; both are open.

## 7. Current Research (as of June 2026)

- **Descriptive inner model theory / core model induction.** Sargsyan, Steel, Trang, Schindler and collaborators continue to push hybrid mice ($\mathsf{HOD}$-mice, hod pairs) past $\mathsf{AD}^{L(\mathbb{R})}$ toward $\mathsf{AD}_{\mathbb{R}} + \Theta$ regular and beyond. Centres: UC Berkeley, Münster (Schindler), IMPAN Warsaw (Sargsyan), UC Irvine (Trang, Zeman).
- **Regularity for arbitrary definable forcings.** Ikegami's framework ("$\mathbb{P}$-measurability" for arithmetically definable proper forcings) yields uniform level-2 characterizations: $\mathbf{\Delta}^1_2$-$\mathbb{P}$-regularity $\iff$ $\forall r\,\exists$ $\mathbb{P}$-generic over $L[r]$. Extending the schema to level 3 with matching lower bounds is active. *(frontier — verify)*
- **Forcing axioms as a route to $\mathsf{PD}$.** Following Steel's $\mathsf{PFA} \Rightarrow \mathsf{AD}^{L(\mathbb{R})}$, work on $\mathsf{MM}^{++}$, Woodin's $(\ast)$-axiom and their consequences for projective regularity continues; Asperó–Schindler's proof that $\mathsf{MM}^{++} \Rightarrow (\ast)$ (Annals, 2021) reshaped the landscape.
- **Reverse mathematics / effective descriptive set theory.** Calibrating measurability of $\Sigma^1_n$ sets in subsystems of second-order and third-order arithmetic (Yokoyama, Sato, Simpson school). *(frontier — verify)*
- **Ultimate-$L$.** Woodin's program aims at a canonical inner model absorbing supercompacts; success would settle the justification gap in one direction. *(frontier — verify)*

## 8. Future Work

- Prove $\mathbf{\Sigma}^1_3(\lambda) \Rightarrow \forall r\ M_1^{\\#}(r)$ exists (or refute), giving the first genuine level-3 large-cardinal characterization.
- Extend Ikegami's uniform $\sigma$-ideal framework to all projective levels, so measurability, Baire property and Ramsey property are calibrated by a single template rather than case-by-case forcing.
- Resolve the $\Omega$-conjecture and the HOD conjecture; either settles whether $\mathsf{PD}$ is "forced" on us by generic absoluteness.
- Build iterable inner models at superstrong/supercompact strength (Ultimate-$L$), or prove an obstruction.
- Determine the exact strength of "every projective set is universally Baire", intermediate between measurability and $\mathsf{PD}$.

## 9. Key References

- **[Foundational]** N. Lusin. *Sur la classification de M. Baire.* C. R. Acad. Sci. Paris **164** (1917), 91–94.
- **[Foundational]** K. Gödel. *The Consistency of the Continuum Hypothesis.* Annals of Mathematics Studies 3, Princeton University Press, 1940.
- **[Foundational]** J. Mycielski, S. Świerczkowski. *On the Lebesgue measurability and the axiom of determinateness.* Fundamenta Mathematicae **54** (1964), 67–71.
- **[Foundational]** R. M. Solovay. *On the cardinality of $\Sigma^1_2$ sets of reals.* In: Foundations of Mathematics (Bulloff, Holyoke, Hahn, eds.), Springer, 1969, 58–73.
- **[Foundational]** R. M. Solovay. *A model of set-theory in which every set of reals is Lebesgue measurable.* Annals of Mathematics **92** (1970), 1–56.
- **[SOTA]** S. Shelah. *Can you take Solovay's inaccessible away?* Israel Journal of Mathematics **48** (1984), 1–47.
- **[SOTA]** J. Raisonnier. *A mathematical proof of S. Shelah's theorem on the measure problem and related results.* Israel Journal of Mathematics **48** (1984), 48–56.
- **[SOTA]** D. A. Martin, J. R. Steel. *A proof of projective determinacy.* Journal of the American Mathematical Society **2** (1989), 71–125.
- **[SOTA]** W. H. Woodin. *Supercompact cardinals, sets of reals, and weakly homogeneous trees.* Proceedings of the National Academy of Sciences USA **85** (1988), 6587–6591.
- **[SOTA]** J. Ihoda (Judah), S. Shelah. *$\Delta^1_2$-sets of reals.* Annals of Pure and Applied Logic **42** (1989), 207–223.
- **[SOTA]** J. R. Steel. *PFA implies $\mathsf{AD}^{L(\mathbb{R})}$.* Journal of Symbolic Logic **70** (2005), 1255–1296.
- **[SOTA]** D. Ikegami. *Forcing absoluteness and regularity properties.* Annals of Pure and Applied Logic **161** (2010), 879–894.
- **[Survey]** A. S. Kechris. *Classical Descriptive Set Theory.* Springer GTM 156, 1995.
- **[Survey]** Y. N. Moschovakis. *Descriptive Set Theory.* 2nd ed., Mathematical Surveys and Monographs 155, AMS, 2009.
- **[Survey]** A. Kanamori. *The Higher Infinite.* 2nd ed., Springer, 2003.
- **[Survey]** T. Bartoszyński, H. Judah. *Set Theory: On the Structure of the Real Line.* A K Peters, 1995.
- **[Survey]** G. Sargsyan. *Descriptive inner model theory.* Bulletin of Symbolic Logic **19** (2013), 1–55.

## 10. Worked Example: a $\mathbf{\Delta}^1_2$ non-measurable set in $L$

Assume $V = L$. We construct a Bernstein set of complexity $\Delta^1_2$ (lightface), witnessing failure of measurability at the lowest possible projective level.

**Step 1 — the wellordering.** Gödel's canonical wellordering $<_L$ restricted to $\mathbb{R}$ has a $\Sigma^1_2$ definition:
$$x <_L y \iff \exists \text{ a countable well-founded model } M \models V{=}L \text{ with } x,y \in M \text{ and } M \models x <_L y .$$
"There is a countable well-founded model coding $\ldots$" is $\Sigma^1_2$ (existential real quantifier over a $\Pi^1_1$ well-foundedness condition), and by condensation this is correct. Under $V=L$, $<_L\restriction\mathbb{R}$ has order type $\omega_1$ and every real appears at a countable $L$-level.

**Step 2 — the transfinite construction.** Perfect subsets of $\mathbb{R}$ are coded by reals; let $\langle P_\alpha : \alpha < \omega_1\rangle$ enumerate them in $<_L$-order of their codes. Recursively pick, for each $\alpha < \omega_1$,
$$x_\alpha = \text{the } <_L\text{-least element of } P_\alpha \setminus \{x_\beta, y_\beta : \beta<\alpha\}, \qquad y_\alpha = \text{the } <_L\text{-least element of } P_\alpha \setminus \{x_\beta,y_\beta:\beta\le\alpha\}\cup\{x_\alpha\}.$$
Each $P_\alpha$ has size $2^{\aleph_0}$ while fewer than $\aleph_1$ points are excluded, so both choices exist. Set $B = \{x_\alpha : \alpha < \omega_1\}$.

**Step 3 — complexity.** $x \in B$ iff there exists a countable well-founded model $M \models V{=}L$ containing $x$ such that $M$ computes an initial segment of the construction and $M \models$ "$x = x_\alpha$ for some $\alpha$". This is $\Sigma^1_2$. The same form works for $x \notin B$ (a witnessing $M$ computes that $x$ is never chosen as some $x_\alpha$, since the construction is absolute to sufficiently large countable $L$-levels). Hence $B$ is $\Delta^1_2$.

**Step 4 — non-measurability.** $B$ meets every perfect set (it contains $x_\alpha \in P_\alpha$) and so does $\mathbb{R}\setminus B$ (it contains $y_\alpha \in P_\alpha$). Suppose $B$ were measurable. If $\lambda(B) > 0$, by inner regularity $B$ contains a closed set of positive measure, which contains a perfect set $P$; but $P = P_\alpha$ for some $\alpha$ and $y_\alpha \in P_\alpha \setminus B$ — contradiction. So $\lambda(B) = 0$; symmetrically $\lambda(\mathbb{R}\setminus B) = 0$; then $\lambda(\mathbb{R}) = 0$, contradiction. Hence $B$ is not Lebesgue measurable.

**Reading the example.** The construction uses exactly one non-classical ingredient: a $\Sigma^1_2$ wellordering of $\mathbb{R}$. Solovay's characterization says the obstruction is precisely that $\mathbb{R}^{L}$ is not null — no real is random over $L$. Force with the measure algebra to add $\aleph_2$ random reals over $L$ and the set of reals random over $L[r]$ acquires measure one for each $r$; then $\mathbf{\Sigma}^1_2(\lambda)$ holds and the above $B$ ceases to be $\mathbf{\Delta}^1_2$. Pushing the same transcendence one projective level up is the open gap of §6.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*