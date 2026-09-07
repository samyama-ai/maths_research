---
id: 08-logic-set-theory/ramsey-cardinals-existence
title: "Ramsey Cardinals Existence"
topic: 08-logic-set-theory
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Ramsey Cardinals Existence

> **Topic:** Mathematical Logic & Set Theory · **ID:** `08-logic-set-theory/ramsey-cardinals-existence` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

An uncountable cardinal $\kappa$ is **Ramsey** if it satisfies the partition relation
$$\kappa \longrightarrow (\kappa)^{<\omega}_2 ,$$
i.e. for every colouring $f : [\kappa]^{<\omega} \to 2$ there is $H \subseteq \kappa$ with $|H| = \kappa$ that is *homogeneous*: $f \restriction [H]^n$ is constant for each $n < \omega$.

The problem has three parts.

1. **Existence.** Does a Ramsey cardinal exist? This is not decided by ZFC. ZFC cannot prove existence (a Ramsey cardinal is inaccessible, so $V_\kappa \models \mathrm{ZFC}$ and existence yields $\mathrm{Con}(\mathrm{ZFC})$, blocked by Gödel's second incompleteness theorem). ZFC cannot refute existence unless a much weaker large-cardinal hypothesis is already inconsistent. So "existence" is an *axiom candidate*, and the mathematical content of the problem is: **where exactly does the Ramsey property sit in the consistency-strength hierarchy, and what does it decide?**
2. **Calibration.** Pin down the strength of "there is a Ramsey cardinal" between $0^\sharp$ and a measurable cardinal, in the inner-model-theoretic sense: characterise Ramseyness in canonical core models and identify a canonical inner model for it.
3. **Structure.** Determine which combinatorial, model-theoretic and forcing-theoretic properties are equivalent to, or strictly stronger/weaker than, Ramseyness, and which are indestructible.

A complete resolution of (1) in the negative would be an inconsistency proof for a modest large-cardinal axiom; a positive resolution is impossible in ZFC alone. Progress therefore means resolutions of (2) and (3).

## 2. Mathematical Foundations

**Partition notation.** For a set $X$, $[X]^n = \{ s \subseteq X : |s| = n\}$ and $[X]^{<\omega} = \bigcup_{n<\omega} [X]^n$. Write
$$\kappa \to (\lambda)^n_\mu \iff \forall f : [\kappa]^n \to \mu \ \exists H \in [\kappa]^{\lambda} \ \big( |f''[H]^n| = 1 \big),$$
and $\kappa \to (\lambda)^{<\omega}_\mu$ when a single $H$ of order type $\lambda$ is homogeneous simultaneously for all exponents $n$.

**Erdős cardinals.** $\kappa(\alpha)$ is the least $\kappa$ with $\kappa \to (\alpha)^{<\omega}_2$; it exists for suitable $\alpha$ only under large-cardinal assumptions. Ramsey $\iff \kappa \to (\kappa)^{<\omega}_2 \iff \kappa = \kappa(\kappa)$ is $\kappa$-Erdős.

**Indiscernibles form.** $\kappa \to (\kappa)^{<\omega}_2$ is equivalent to: for every structure $\mathfrak{A} = \langle \kappa, \dots\rangle$ in a countable (indeed $<\kappa$-sized) language there is $I \subseteq \kappa$, $|I| = \kappa$, of *good indiscernibles* for $\mathfrak{A}$ — any two increasing tuples from $I$ of the same length satisfy the same formulas with parameters below $\min$ of the tuples.

**Ultrafilter (Dodd–Jensen) characterisation.** A *weak $\kappa$-model* is a transitive $M \models \mathrm{ZFC}^-$ with $\kappa \in M$, $|M| = \kappa$. An $M$-ultrafilter $U$ on $\kappa$ is *weakly amenable* if $\langle A_\xi : \xi<\kappa\rangle \in M$ implies $\{\xi : A_\xi \in U\} \in M$, and *countably complete* ($\omega_1$-iterable) if every $\omega$-sequence from $U$ has infinite intersection. Then
$$\kappa \text{ is Ramsey} \iff \forall A \subseteq \kappa \ \exists\, (M,U):\ A \in M,\ U \text{ a weakly amenable, countably complete } M\text{-ultrafilter on } \kappa .$$
Weak amenability makes the ultrapower embedding $j : M \to N$ iterable through all ordinals; countable completeness makes the iterates wellfounded. This is the working definition in modern papers.

**Position in the hierarchy.** Every measurable cardinal is Ramsey (a $\kappa$-complete nonprincipal ultrafilter gives homogeneous sets in the ultrafilter). Every Ramsey cardinal is inaccessible, Mahlo, weakly compact, and $\Pi^1_2$-indescribable, and the weakly compact cardinals below it are stationary. Ramseyness implies $\kappa \to (\kappa)^n_\lambda$ for all $n<\omega$, $\lambda<\kappa$.

**Anti-constructibility.** If $\kappa$ is Ramsey then $\kappa \to (\omega_1)^{<\omega}_2$ relativises to $L[x]$ for every $x \subseteq \omega$, so $x^\sharp$ exists for all reals $x$; hence $V \neq L$, $\mathbb{R} \cap L$ is countable, every uncountable cardinal is inaccessible in $L$, and (Martin–Harrington) analytic determinacy holds.

## 3. History & State of the Art (SOTA)

- **1956–1958.** Erdős and Hajnal study partition relations with infinite exponent; the cardinals $\kappa(\alpha)$ emerge from work on set mappings (Erdős–Hajnal, *On the structure of set-mappings*, 1958).
- **1965.** Erdős–Hajnal–Rado's *Partition relations for cardinal numbers* systematises $\kappa \to (\lambda)^n_\mu$ and fixes the notation; $\kappa \to (\kappa)^{<\omega}_2$ is isolated as a genuinely large hypothesis, since $\omega$ fails it.
- **1970–1971.** Rowbottom and Silver connect infinite-exponent partitions with indiscernibles and $L$: a Ramsey cardinal makes $\mathbb{R}\cap L$ countable and yields $0^\sharp$. The name "Ramsey cardinal" stabilises here.
- **1979.** W. Mitchell, *Ramsey cardinals and constructibility*: Ramseyness is downward absolute to $L[U]$-style inner models and cannot be destroyed by passing to canonical models with a measure.
- **1981–1982.** Dodd–Jensen core model theory gives the weakly amenable $\omega_1$-iterable $M$-ultrafilter characterisation and shows Ramseyness is downward absolute to $K^{DJ}$: if $\kappa$ is Ramsey in $V$, it is Ramsey in the core model.
- **1990.** Feng's $\Pi_\alpha$-Ramsey hierarchy, topped by *completely Ramsey* cardinals, all strictly below a measurable.
- **2011–2019.** The "Ramsey-like" programme (Gitman; Gitman–Welch; Sharpe–Welch; Holy–Schlicht; Nielsen–Welch) builds a fine hierarchy — strongly Ramsey, super Ramsey, $\alpha$-iterable, $\alpha$-Ramsey, and filter-game characterisations — filling the interval between weakly compact and measurable with a linear-in-strength scale.

**SOTA summary.** Existence remains an axiom. Its strength is strictly between "$\forall x\, x^\sharp$ exists" and "there is a measurable cardinal", both separations being theorems, and Ramseyness has a robust inner-model and game-theoretic characterisation.

## 4. Partial Results / Verified Cases

- **Consistency from above (verified).** If $\kappa$ is measurable then $\kappa$ is Ramsey; in $L[U]$, $\kappa$ is Ramsey and GCH holds. So $\mathrm{Con}(\text{measurable}) \Rightarrow \mathrm{Con}(\text{Ramsey} + \mathrm{GCH})$.
- **Strict separation below.** A Ramsey cardinal implies $\forall x \subseteq \omega\ (x^\sharp$ exists$)$, hence $\mathrm{Con}(\text{Ramsey}) \Rightarrow \mathrm{Con}(0^\sharp)$ but not conversely: in $L[0^\sharp]$ there is no Ramsey cardinal.
- **Strict separation above.** If $\kappa$ is measurable, $\{\alpha<\kappa : \alpha$ Ramsey$\}$ is stationary in $\kappa$ (indeed in the normal measure's dual ideal complement), so $\kappa$ is the $\kappa$-th Ramsey cardinal; Ramsey $\not\Rightarrow$ measurable.
- **Exponent ranges (computed).** $\omega \to (\omega)^n_k$ for all $n,k<\omega$ (finite-exponent Ramsey theorem), but $\omega \not\to (\omega)^{<\omega}_2$; and for uncountable $\kappa$, $\kappa\to(\kappa)^{<\omega}_2$ forces inaccessibility. For $\alpha < \omega_1$, the Erdős cardinals $\kappa(\alpha)$ are consistent from far weaker hypotheses than Ramsey; $\kappa(\omega_1)$ already gives $0^\sharp$.
- **Forcing (verified).** Ramseyness is preserved by forcing of size $<\kappa$ (Levy–Solovay), and by suitable $\kappa$-closed/${<}\kappa$-directed-closed forcings; Gitman–Johnstone obtain indestructibility of Ramsey and Ramsey-like cardinals under classes of $\kappa^+$-c.c. and directed-closed posets.
- **Core-model absoluteness.** Ramsey is downward absolute to $K^{DJ}$ (Dodd–Jensen) and, under anti-large-cardinal hypotheses, to Mitchell-style $K$.
- **Hierarchy placements.** Strongly Ramsey $\Rightarrow$ Ramsey $\Rightarrow$ completely ineffable $\Rightarrow$ weakly compact, each implication strict in consistency strength; $\alpha$-Ramsey for $\alpha<\kappa$ interpolates (Holy–Schlicht), and Nielsen–Welch characterise the levels by filter games $G^\theta_\gamma(\kappa)$.

## 5. Principal Obstacles

- **Incompleteness barrier.** No consistency proof is available in principle: existence implies $\mathrm{Con}(\mathrm{ZFC})$, so ZFC-provable existence is impossible. Only relative consistency and *evidence of coherence* are attainable.
- **No canonical inner model at exactly this level.** For measurables, $L[U]$ gives a fine-structural model with a full comparison theory. Ramseyness is a *local* $\Sigma$-property of $\kappa$-many $M$-ultrafilters on weak $\kappa$-models, not a single global measure, so there is no known model of the form $L[\vec{U}]$ whose canonical objects code exactly "Ramsey and no more". Fine structure handles the strength below and above but not tightly at this point.
- **Filters are external and non-amenable to $V$.** The witnessing ultrafilters $U$ live outside $M$ and cannot be assembled into a $\kappa$-complete filter on $\kappa$ in $V$ — otherwise $\kappa$ would be measurable. Every attempt to upgrade the local witnesses to a global measure collides with the strict separation in Section 4.
- **Iterability is delicate.** Countable completeness is exactly what makes iterated ultrapowers wellfounded; weakening it to $\alpha$-iterability yields strictly weaker cardinals (Gitman), so the standard technique of "just iterate" degrades discontinuously.
- **Reflection is weak.** Ramseyness is $\Pi^1_2$-expressible over $V_\kappa$ but not $\Sigma^1_2$-describable in a way that supports the usual elementary-embedding arguments; the absence of a $j : V \to M$ formulation blocks lifting arguments used for measurable and above.

## 6. The Gap

Proven: exact upper bound (measurable), exact lower bounds ($\forall x\, x^\sharp$, completely ineffable, $\Pi^1_2$-indescribable), downward absoluteness to $K^{DJ}$, and a graded hierarchy $\alpha$-Ramsey with game characterisations.

Not proven: (i) a canonical inner model $K^{\mathrm{Ramsey}}$ with fine structure and a comparison lemma whose minimal model contains exactly one Ramsey cardinal; (ii) an equiconsistency of "there is a Ramsey cardinal" with a purely combinatorial statement about $\omega_1$ or about $\mathbb{R}$ (as $0^\sharp$ is equiconsistent with analytic determinacy); (iii) any consistency-strength argument that would *refute* existence. The precise step needed for (i) is a comparison theory for premice carrying $\kappa$-many weakly amenable, countably complete filters on $\kappa$ that are not internally measures — the standard coherent-sequence indexing has no slot for such objects.

## 7. Current Research (as of June 2026)

- **Ramsey-like hierarchy and games.** Holy, Schlicht, Nielsen and Welch continue the filter-game programme: characterising $\alpha$-Ramsey and $\Pi_\alpha$-Ramsey cardinals by determinacy of games $G^\theta_\gamma(\kappa)$ of length $\gamma$, and separating the levels by consistency strength. Bristol, Bonn/Münster and the CUNY set theory group are the main nodes.
- **Ramsey cardinals in generic/virtual form.** "Virtual" and generically Ramsey variants (Gitman, Schindler, Bagaria) — where embeddings exist in forcing extensions — have strength compatible with $V = L$ in some cases, giving a low-strength shadow of the theory.
- **Indestructibility and forcing axioms.** Determining the optimal class of posets preserving Ramseyness, and whether a Ramsey cardinal can be made indestructible by all $<\kappa$-directed-closed forcing (Laver-style preparation) *(frontier — verify)*.
- **Ideal-theoretic reformulations.** The Ramsey ideal and its saturation properties; whether the Ramsey ideal can be precipitous/normal-saturated at the least Ramsey cardinal *(frontier — verify)*.
- **Inner model theory at the Ramsey level.** Attempts to extract mice from Ramsey-like filters, connected to Welch's greatly Erdős cardinals and stationary reflection *(frontier — verify)*.

## 8. Future Work

- Build a fine-structural model for a Ramsey cardinal by indexing weakly amenable countably complete filters rather than measures; a comparison lemma is the crux.
- Find a combinatorial or descriptive-set-theoretic statement equiconsistent with a Ramsey cardinal, in the style of "analytic determinacy $\equiv$ sharps".
- Settle whether every $\alpha$-Ramsey level for $\alpha \le \kappa$ is strictly increasing in consistency strength, and where completely Ramsey sits relative to $\kappa$-Ramsey.
- Determine the exact reflection strength: is every Ramsey cardinal $\Pi^1_2$-indescribable but consistently not $\Sigma^1_2$-indescribable, and can the least Ramsey be the least of many such?
- Clarify preservation: which iterations of length $\ge \kappa^+$ preserve Ramseyness, and whether Ramseyness can coexist with strong forcing axioms at small cardinals.

## 9. Key References

- **[Foundational]** P. Erdős, A. Hajnal, R. Rado. *Partition relations for cardinal numbers.* Acta Mathematica Academiae Scientiarum Hungaricae 16 (1965), 93–196.
- **[Foundational]** P. Erdős, A. Hajnal. *On the structure of set-mappings.* Acta Mathematica Academiae Scientiarum Hungaricae 9 (1958), 111–131.
- **[Foundational]** F. Rowbottom. *Some strong axioms of infinity incompatible with the axiom of constructibility.* Annals of Mathematical Logic 3 (1971), 1–44.
- **[Foundational]** J. Silver. *Some applications of model theory in set theory.* Annals of Mathematical Logic 3 (1971), 45–110.
- **[Foundational]** A. Dodd, R. Jensen. *The core model.* Annals of Mathematical Logic 20 (1981), 43–75.
- **[Structural]** W. Mitchell. *Ramsey cardinals and constructibility.* Journal of Symbolic Logic 44 (1979), 260–266.
- **[Structural]** Q. Feng. *A hierarchy of Ramsey cardinals.* Annals of Pure and Applied Logic 49 (1990), 257–277.
- **[SOTA / Recent]** V. Gitman. *Ramsey-like cardinals.* Journal of Symbolic Logic 76 (2011), 519–540.
- **[SOTA / Recent]** V. Gitman, P. D. Welch. *Ramsey-like cardinals II.* Journal of Symbolic Logic 76 (2011), 541–560.
- **[SOTA / Recent]** P. Holy, P. Schlicht. *A hierarchy of Ramsey-like cardinals.* Fundamenta Mathematicae 242 (2018), 49–74.
- **[SOTA / Recent]** D. S. Nielsen, P. D. Welch. *Games and Ramsey-like cardinals.* Journal of Symbolic Logic 84 (2019), 408–437.
- **[SOTA / Recent]** I. Sharpe, P. D. Welch. *Greatly Erdős cardinals with some generalizations to the Chang and Ramsey properties.* Annals of Pure and Applied Logic 162 (2011), 863–902.
- **[SOTA / Recent]** V. Gitman, T. A. Johnstone. *Indestructibility for Ramsey and Ramsey-like cardinals.* Annals of Pure and Applied Logic (2019).
- **[Survey]** A. Kanamori. *The Higher Infinite: Large Cardinals in Set Theory from Their Beginnings.* 2nd ed., Springer, 2003 (§7–8).
- **[Survey]** T. Jech. *Set Theory,* 3rd millennium edition. Springer, 2003 (Chs. 9, 17–18).
- **[Related]** A. Levy, R. Solovay. *Measurable cardinals and the continuum hypothesis.* Israel Journal of Mathematics 5 (1967), 234–248.
- **[Related]** L. Harrington. *Analytic determinacy and $0^\sharp$.* Journal of Symbolic Logic 43 (1978), 685–693.

## 10. Worked Example / Concrete Special Case

**Why the exponent $<\omega$ is a genuine strengthening: $\omega \to (\omega)^n_2$ for all $n$, yet $\omega \not\to (\omega)^{<\omega}_2$.**

*Finite exponent (holds).* Ramsey's theorem: any $f : [\omega]^n \to 2$ has an infinite homogeneous $H$. For $n=2$: build $x_0 < x_1 < \cdots$ and infinite sets $A_0 \supseteq A_1 \supseteq \cdots$ with $x_i = \min A_i$ and $f(\{x_i, y\}) = c_i$ constant for all $y \in A_{i+1}$. Some colour $c \in \{0,1\}$ occurs for infinitely many $i$; $H = \{x_i : c_i = c\}$ is homogeneous.

*Infinite exponent (fails).* Define $f : [\omega]^{<\omega} \to 2$ by
$$f(s) = \begin{cases} 0 & \text{if } |s| \le \min(s), \\ 1 & \text{otherwise.}\end{cases}$$
Let $H \subseteq \omega$ be infinite, $m = \min(H)$. Take $s \subseteq H$ with $|s| = m$ and $\min(s)=m$: then $f(s)=0$. Take $t \subseteq H$ with $|t| = m+2$ and $\min(t)=m$: then $|t| > \min(t)$, so $f(t)=1$. Both colours appear on subsets of $H$, of sizes $m$ and $m+2$ respectively — so no infinite $H$ is homogeneous for all exponents simultaneously. Hence $\omega \not\to (\omega)^{<\omega}_2$.

**Consequence for uncountable $\kappa$.** Suppose $\kappa \to (\kappa)^{<\omega}_2$. If $\kappa$ were singular, say $\kappa = \sup_{i<\mathrm{cf}(\kappa)} \kappa_i$, then even $\kappa \to (\kappa)^2_2$ fails by a Sierpiński-type colouring, so $\kappa$ is regular. If $2^\lambda \ge \kappa$ for some $\lambda < \kappa$, fix an injection $\alpha \mapsto A_\alpha \subseteq \lambda$ and colour $\{\alpha<\beta\}$ by whether $\min(A_\alpha \triangle A_\beta) \in A_\alpha$; a homogeneous set of size $\lambda^+$ would give a monotone $\lambda^+$-chain in the lexicographic order on $2^\lambda$, which is impossible for $\lambda^+ > \lambda$ in the standard argument, so $2^\lambda < \kappa$ for all $\lambda<\kappa$. Thus $\kappa$ is inaccessible, $V_\kappa \models \mathrm{ZFC}$, and existence of a Ramsey cardinal yields $\mathrm{Con}(\mathrm{ZFC})$ — the incompleteness barrier of Section 1, obtained from the two-line colouring above.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*