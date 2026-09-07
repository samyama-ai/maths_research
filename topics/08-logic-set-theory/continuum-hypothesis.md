---
id: 08-logic-set-theory/continuum-hypothesis
title: "Continuum Hypothesis"
topic: 08-logic-set-theory
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Continuum Hypothesis

> **Topic:** Mathematical Logic & Set Theory · **ID:** `08-logic-set-theory/continuum-hypothesis` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

The **Continuum Hypothesis (CH)** asserts that there is no set whose cardinality lies strictly between that of the integers and that of the real numbers:

$$\text{CH} \iff 2^{\aleph_0} = \aleph_1 .$$

Equivalently: every uncountable set $A \subseteq \mathbb{R}$ satisfies $|A| = |\mathbb{R}|$.

The **Generalized Continuum Hypothesis (GCH)** asserts $2^{\aleph_\alpha} = \aleph_{\alpha+1}$ for every ordinal $\alpha$.

Hilbert's first problem (1900) asked for a proof of CH. The problem is *formally settled* relative to the standard axiom system: Gödel (1938) proved $\mathrm{Con}(\mathrm{ZF}) \Rightarrow \mathrm{Con}(\mathrm{ZFC} + \mathrm{GCH})$, and Cohen (1963) proved $\mathrm{Con}(\mathrm{ZF}) \Rightarrow \mathrm{Con}(\mathrm{ZFC} + \neg\mathrm{CH})$. Hence CH is independent of ZFC.

What remains open — and is the live mathematical problem — is the **question of truth**: is there a principled extension of ZFC, justified by intrinsic (reflection, maximality) or extrinsic (fruitfulness, structural coherence) evidence, that decides CH? A "solution" in the modern sense means either:

1. exhibiting a canonical axiom system, with a compelling justification, that settles the value of $2^{\aleph_0}$; or
2. showing that no such system can exist without arbitrary choice, i.e. establishing a multiverse position on principled grounds.

## 2. Mathematical Foundations

**Cardinals.** A cardinal is an ordinal not in bijection with any smaller ordinal. The alephs enumerate infinite cardinals: $\aleph_0 = |\mathbb{N}|$, and $\aleph_{\alpha+1} = \aleph_\alpha^+$ is the least cardinal greater than $\aleph_\alpha$. Cantor's theorem gives $|A| < |\mathcal{P}(A)|$, so
$$2^{\aleph_0} = |\mathcal{P}(\mathbb{N})| = |\mathbb{R}| > \aleph_0 .$$
Under AC, $2^{\aleph_0} = \aleph_\gamma$ for some $\gamma \ge 1$; CH is $\gamma = 1$.

**Continuum function constraints.** The only ZFC-provable restrictions on $\kappa \mapsto 2^\kappa$ for regular $\kappa$ are monotonicity and König's theorem:
$$\operatorname{cf}(2^{\kappa}) > \kappa, \qquad \text{so } 2^{\aleph_0} \neq \aleph_\omega .$$
**Easton's theorem** (1970): for any monotone class function $F$ on regular cardinals with $\operatorname{cf}(F(\kappa)) > \kappa$, there is a forcing extension where $2^\kappa = F(\kappa)$ for all regular $\kappa$. So $2^{\aleph_0}$ may consistently be $\aleph_1, \aleph_2, \aleph_{17}, \aleph_{\omega_1}, \dots$

**Constructible universe.** $L = \bigcup_{\alpha \in \mathrm{Ord}} L_\alpha$, where $L_{\alpha+1} = \mathrm{Def}(L_\alpha)$ is the set of first-order definable subsets of $L_\alpha$ with parameters, and $L_\lambda = \bigcup_{\alpha<\lambda} L_\alpha$ at limits. Gödel: $L \models \mathrm{ZFC} + V{=}L$, and $V{=}L \Rightarrow \mathrm{GCH}$, via the condensation lemma: if $X \prec L_\alpha$ then the transitive collapse of $X$ is some $L_\beta$, forcing $\mathcal{P}(\omega)\cap L \subseteq L_{\omega_1}$.

**Forcing.** Given a countable transitive $M \models \mathrm{ZFC}$ and a poset $\mathbb{P} \in M$, a filter $G \subseteq \mathbb{P}$ generic over $M$ yields $M[G] \models \mathrm{ZFC}$ with $M \subseteq M[G]$, $\mathrm{Ord}^M = \mathrm{Ord}^{M[G]}$. Taking $\mathbb{P} = \mathrm{Fn}(\omega_2^M \times \omega, 2)$ — finite partial functions, ordered by reverse inclusion — the countable chain condition preserves cardinals, and
$$M[G] \models 2^{\aleph_0} \ge \aleph_2 ,$$
so CH fails. This is Cohen's construction and it earned him the 1966 Fields Medal.

**Cardinal characteristics.** Cardinals between $\aleph_1$ and $2^{\aleph_0}$ measuring combinatorial properties of $\mathbb{R}$: $\mathfrak{b}$ (unbounded families in $(\omega^\omega, \le^*)$), $\mathfrak{d}$ (dominating), $\mathfrak{p}$, $\mathfrak{t}$, $\mathfrak{a}$, $\mathrm{non}(\mathcal{N})$, $\mathrm{cov}(\mathcal{M})$. CH collapses all of them to $\aleph_1$; $\neg$CH lets them separate.

**$\Omega$-logic.** Woodin's semantic consequence relation: $T \models_\Omega \varphi$ iff for every ordinal $\alpha$ and set-forcing $\mathbb{P}$, $V_\alpha^{\mathbb{P}} \models T$ implies $V_\alpha^{\mathbb{P}} \models \varphi$. Under large cardinals this relation is generically invariant. The **$\Omega$-conjecture** states that $\Omega$-validity equals $\Omega$-provability (soundness plus completeness for the $\Omega$-proof relation).

## 3. History & State of the Art (SOTA)

- **1878.** Cantor states CH in *Ein Beitrag zur Mannigfaltigkeitslehre*; he attempts a proof repeatedly for two decades.
- **1883.** Cantor proves CH for closed sets: every uncountable closed $A \subseteq \mathbb{R}$ contains a perfect set, hence $|A| = 2^{\aleph_0}$ (Cantor–Bendixson).
- **1900.** Hilbert's Problem 1.
- **1938–40.** Gödel constructs $L$; GCH and AC are consistent with ZF.
- **1963.** Cohen invents forcing; $\neg$CH consistent. Independence established.
- **1970.** Easton's theorem: the continuum function on regular cardinals is nearly arbitrary.
- **1970s–80s.** Martin's Axiom (Martin–Solovay 1970) gives a workable "$\neg$CH universe"; the Proper Forcing Axiom (PFA, Baumgartner–Shelah) emerges.
- **1988.** Todorcevic and Veličković: PFA $\Rightarrow 2^{\aleph_0} = \aleph_2$. Independently Todorcevic's $\theta$-principles.
- **1994.** Shelah's pcf theory yields the striking ZFC bound $2^{\aleph_\omega} < \aleph_{\omega_4}$ when $\aleph_\omega$ is a strong limit.
- **1999–2001.** Woodin's $\Omega$-logic program: assuming the $\Omega$-conjecture and large cardinals, any "$\Omega$-complete" theory for $H(\omega_2)$ implies $\neg$CH, and $2^{\aleph_0} = \aleph_2$ under Woodin's maximality axiom $(*)$.
- **2010s.** Woodin shifts toward the **Ultimate-$L$** program, which, if it succeeds, would favour CH (Ultimate-$L$ satisfies GCH).
- **2021.** **Asperó–Schindler** prove $\mathrm{MM}^{++} \Rightarrow (*)$ (*Annals of Mathematics* 193), unifying the two leading $\neg$CH axioms and yielding $2^{\aleph_0} = \aleph_2$ from Martin's Maximum$^{++}$.

## 4. Partial Results / Verified Cases

CH is **provable in ZFC** when restricted to definable classes of sets — this is the substantive positive content.

| Class of $A \subseteq \mathbb{R}$ | CH status | Source |
|---|---|---|
| Closed / $F_\sigma$ | Provable (perfect set property) | Cantor–Bendixson 1883 |
| Analytic ($\mathbf{\Sigma}^1_1$) | Provable in ZFC | Suslin 1917 |
| $\mathbf{\Sigma}^1_2$ | Provable from "$\forall x\, x^\sharp$ exists" | Solovay |
| All projective sets | Provable from PD (infinitely many Woodin cardinals) | Martin–Steel 1989, Woodin |
| All sets in $L(\mathbb{R})$ | Provable from AD$^{L(\mathbb{R})}$ | Woodin |
| Arbitrary sets | Independent of ZFC | Gödel 1938, Cohen 1963 |

Other verified points:
- **GCH holds in $L$** and in the canonical inner models $L[U]$, $M_n$, and (conjecturally) Ultimate-$L$.
- **$\mathfrak{p} = \mathfrak{t}$** (Malliaris–Shelah, *JAMS* 2016) — settled a 50-year-old cardinal characteristic problem; a rare ZFC theorem in this landscape.
- **Shelah 1994:** if $\aleph_\omega$ is a strong limit then $2^{\aleph_\omega} < \aleph_{\omega_4}$; singular cardinals *do* obey nontrivial ZFC constraints, unlike regular ones.
- **Silver 1975:** if GCH holds below a singular $\kappa$ of uncountable cofinality, GCH holds at $\kappa$.
- **Under PFA / MM$^{++}$:** $2^{\aleph_0} = \aleph_2$ exactly.
- **Foreman–Magidor–Shelah 1988:** Martin's Maximum is consistent from a supercompact cardinal.

## 5. Principal Obstacles

- **Forcing kills everything.** Any statement about $H(\omega_2)$ not decided by a canonical theory can be flipped by set forcing. Cohen forcing changes $2^{\aleph_0}$ while preserving all large cardinals — the standard hierarchy of consistency strength is therefore *blind* to CH. Levy–Solovay (1967): large cardinals below $|\mathbb{P}|$ survive $\mathbb{P}$-forcing.
- **No absoluteness at the right level.** Shoenfield absoluteness pins down $\Sigma^1_2$ statements between $V$ and $L$; CH is $\Sigma^2_1$, one quantifier too high. Determinacy axioms give a complete theory of $L(\mathbb{R})$ but say nothing about $\mathcal{P}(\omega_1)$.
- **Competing maximality intuitions.** "Maximise the universe" pulls two ways. Forcing axioms (maximise generic objects) give $2^{\aleph_0} = \aleph_2$; inner-model maximality (a canonical fine-structural $L$-like model absorbing all large cardinals) gives CH. Neither intuition is formally privileged.
- **Ultimate-$L$ is unfinished.** Its existence rests on the unproven **Ultimate-$L$ conjecture** and comparison theory at the level of supercompact cardinals; the HOD dichotomy and $\Sigma_2$-reflection arguments are not yet a proof.
- **The $\Omega$-conjecture is open**, so the $\Omega$-logic argument against CH is conditional on an unproved statement about generically invariant logic.
- **Meta-mathematical ambiguity.** Even a full solution requires agreement on what counts as evidence for a new axiom — a philosophical criterion that no theorem can supply.

## 6. The Gap

Section 4 proves CH only for sets with a *definable, wellfounded* construction: sets built by countably many operations from open sets, or sets in models satisfying determinacy. The general statement quantifies over *all* subsets of $\mathbb{R}$, including sets produced by AC-driven transfinite recursion with no definition.

The precise barrier: **$\mathcal{P}(\omega_1)$ has no canonical structure theory.** The projective sets and $L(\mathbb{R})$ are pinned down (up to generic invariance) by large cardinals, but $H(\omega_2)$ — the smallest level where CH is expressible — is not. Crossing the gap requires either:

- proving the Ultimate-$L$ conjecture, giving a canonical inner model that is generically absolute *and* satisfies CH and all large cardinals; or
- proving the $\Omega$-conjecture and showing every $\Omega$-complete theory of $H(\omega_2)$ entails $\neg$CH; or
- a fundamentally new absoluteness theorem at the $\Sigma^2_1$ level.

## 7. Current Research (as of June 2026)

- **Ultimate-$L$ program (Woodin, Berkeley).** Iteration and comparison theory at supercompact level; the HOD dichotomy and the "$V = $ Ultimate-$L$" axiom, which implies CH. *(frontier — verify current status of the comparison lemma.)*
- **Forcing axioms after Asperó–Schindler.** MM$^{++} \Rightarrow (*)$ (Annals 2021) is now the anchor; work on $(*)$-variants, higher analogues ($(*)_{\omega_2}$), and whether MM$^{++}$ and $(*)^{++}$ coincide (Asperó, Schindler, Larson, Viale). *(frontier — verify.)*
- **Viale's "Category forcing" / MM$^{+++}$** (Torino): generic absoluteness for $H(\omega_2)$ under forcing axioms, arguing $\neg$CH is the "complete" theory.
- **Cardinal characteristics beyond the Cichoń diagram** (Goldstern–Kellner–Shelah, Vienna/Jerusalem): simultaneous separation of many characteristics via creature forcing and ultrafilter-limit methods — "Cichoń's maximum".
- **Higher descriptive set theory / generalised Baire spaces** $\kappa^\kappa$ (Helsinki, Bonn, Vienna): transferring CH-adjacent structure theory to uncountable $\kappa$.
- **Inner model theory below one supercompact** (Sargsyan, Steel, Schindler): descriptive inner model theory, hod mice, and the core model induction.

## 8. Future Work

- Settle the **Ultimate-$L$ conjecture** — the single highest-value target; success would give a strong extrinsic case for CH.
- Prove or refute the **$\Omega$-conjecture**; refutation would collapse the main formal argument against CH.
- Find further **ZFC theorems** in the mould of $\mathfrak{p}=\mathfrak{t}$ and Shelah's pcf bounds — genuine constraints reduce the space of admissible axioms.
- Develop **extrinsic criteria**: which of PFA/MM$^{++}$ or $V=$Ultimate-$L$ yields more resolved mathematics outside set theory (Banach spaces, C*-algebras — cf. Farah's work on automorphisms of the Calkin algebra, where CH and OCA give opposite answers).
- Formalise the **multiverse** position (Hamkins) rigorously enough to be tested against the singular-universe programmes.

## 9. Key References

- **[Foundational]** Georg Cantor. *Ein Beitrag zur Mannigfaltigkeitslehre.* Journal für die reine und angewandte Mathematik 84, 1878.
- **[Foundational]** Kurt Gödel. *The Consistency of the Axiom of Choice and of the Generalized Continuum-Hypothesis with the Axioms of Set Theory.* Annals of Mathematics Studies 3, Princeton University Press, 1940.
- **[Foundational]** Paul J. Cohen. *The Independence of the Continuum Hypothesis.* Proceedings of the National Academy of Sciences 50(6), 1143–1148, 1963; Part II, 51(1), 105–110, 1964.
- **[Foundational]** William B. Easton. *Powers of regular cardinals.* Annals of Mathematical Logic 1, 139–178, 1970.
- **[Foundational]** Kurt Gödel. *What is Cantor's Continuum Problem?* American Mathematical Monthly 54, 515–525, 1947 (revised 1964).
- **[SOTA / Recent]** David Asperó and Ralf Schindler. *Martin's Maximum$^{++}$ implies Woodin's Axiom $(*)$.* Annals of Mathematics 193(3), 793–835, 2021.
- **[SOTA / Recent]** Maryanthe Malliaris and Saharon Shelah. *Cofinality spectrum theorems in model theory, set theory, and general topology.* Journal of the AMS 29, 237–297, 2016.
- **[SOTA / Recent]** W. Hugh Woodin. *In search of Ultimate-L: The 19th Midrasha Mathematicae Lectures.* Bulletin of Symbolic Logic 23(1), 1–109, 2017.
- **[SOTA / Recent]** Saharon Shelah. *Cardinal Arithmetic.* Oxford Logic Guides 29, Oxford University Press, 1994.
- **[SOTA / Recent]** M. Foreman, M. Magidor, S. Shelah. *Martin's Maximum, saturated ideals, and non-regular ultrafilters. Part I.* Annals of Mathematics 127(1), 1–47, 1988.
- **[Survey]** W. Hugh Woodin. *The Continuum Hypothesis, Part I & Part II.* Notices of the AMS 48(6), 567–576 and 48(7), 681–690, 2001.
- **[Survey]** Thomas Jech. *Set Theory, 3rd Millennium Edition.* Springer Monographs in Mathematics, 2003.
- **[Survey]** Akihiro Kanamori. *The Higher Infinite: Large Cardinals in Set Theory from Their Beginnings.* 2nd ed., Springer, 2003.
- **[Survey]** Joel David Hamkins. *The set-theoretic multiverse.* Review of Symbolic Logic 5(3), 416–449, 2012.
- **[Survey]** Andrés Eduardo Caicedo, James Cummings, Peter Koellner, Paul B. Larson (eds.). *Foundations of Mathematics: Logic at Harvard — Essays in Honor of W. Hugh Woodin.* Contemporary Mathematics 690, AMS, 2017.

## 10. Worked Example / Concrete Special Case

**CH for closed sets, proved in ZFC.**

Let $A \subseteq \mathbb{R}$ be closed and uncountable. Define the **Cantor–Bendixson derivative** $A' = \{x \in A : x \text{ is a limit point of } A\}$, and iterate:
$$A^{(0)} = A,\quad A^{(\alpha+1)} = (A^{(\alpha)})',\quad A^{(\lambda)} = \bigcap_{\alpha<\lambda} A^{(\alpha)} .$$
Each $A^{(\alpha)}$ is closed and the sequence is decreasing. Since $\mathbb{R}$ is second countable with a countable basis $\{B_n\}$, each step $A^{(\alpha)} \setminus A^{(\alpha+1)}$ removes points that are isolated in $A^{(\alpha)}$, and each such point is witnessed by a distinct basic open $B_n$. So the sequence stabilises at some countable ordinal $\alpha_0 < \omega_1$, and
$$A = P \;\sqcup\; C, \qquad P = A^{(\alpha_0)} \text{ perfect}, \quad C = \bigcup_{\alpha < \alpha_0} \big(A^{(\alpha)} \setminus A^{(\alpha+1)}\big) \text{ countable}.$$
$C$ is a countable union of countable sets, hence countable. If $A$ is uncountable then $P \neq \emptyset$.

Now embed the Cantor set into $P$: build a binary tree of nonempty closed balls $\{I_s : s \in 2^{<\omega}\}$ with $I_{s0}, I_{s1} \subseteq I_s$ disjoint, $\operatorname{diam}(I_s) \le 2^{-|s|}$, and $I_s \cap P \neq \emptyset$. Possible because every point of $P$ is a limit point, so every ball meeting $P$ contains two disjoint sub-balls meeting $P$. Each branch $x \in 2^\omega$ gives $\bigcap_n I_{x\restriction n} \cap P$ a single point, and distinct branches give distinct points. Hence
$$|A| \ge |P| \ge 2^{\aleph_0}, \quad\text{and } |A| \le |\mathbb{R}| = 2^{\aleph_0} \Rightarrow |A| = 2^{\aleph_0}.$$

**Why this does not generalise.** The argument uses that $A$ is closed to guarantee the derivative operation is well defined and that the process halts below $\omega_1$. Suslin (1917) pushed it to analytic sets; Gödel showed that in $L$ there is a $\mathbf{\Pi}^1_1$ set of reals of size $\aleph_1$ with no perfect subset. Beyond the projective hierarchy, AC produces a **Bernstein set** $B$ — built by transfinite recursion of length $2^{\aleph_0}$ picking, for each perfect set $P_\alpha$, one point into $B$ and one into $\mathbb{R}\setminus B$ — such that neither $B$ nor its complement contains a perfect set. $B$ is uncountable, but no ZFC argument computes $|B|$. That is exactly the gap of Section 6.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*