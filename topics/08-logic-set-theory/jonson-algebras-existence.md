---
id: 08-logic-set-theory/jonson-algebras-existence
title: "Jonson Algebras Existence"
topic: 08-logic-set-theory
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Existence of Jónsson Algebras (Jónsson Cardinals)

> **Topic:** Mathematical Logic & Set Theory · **ID:** `08-logic-set-theory/jonson-algebras-existence` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

A **Jónsson algebra on $\kappa$** is an algebraic structure $\mathfrak{A}=\langle \kappa; f_n \rangle_{n<\omega}$ with countably many finitary operations on the set $\kappa$ such that every subalgebra $B \subsetneq \kappa$ satisfies $|B| < \kappa$. A cardinal $\kappa$ is **Jónsson** exactly when no such algebra exists.

Central question, open since Jónsson's 1956 paper:

> **For which cardinals $\kappa$ does a Jónsson algebra on $\kappa$ exist in ZFC?**

The problem is "partially solved": ZFC decides the question for a large class of $\kappa$ (all successors of regulars, all successors of singulars of uncountable cofinality, everything below $\aleph_\omega$), and large-cardinal hypotheses show some $\kappa$ can consistently fail to carry one. The two sharpest surviving instances are:

1. **Does $\aleph_{\omega+1}$ carry a Jónsson algebra?** (More generally $\lambda^+$ for $\lambda$ singular with $\mathrm{cf}(\lambda)=\omega$.)
2. **Is "$\aleph_\omega$ is Jónsson" consistent?**

A complete solution is either a ZFC construction of the algebra, or a forcing/inner-model construction of a model in which the cardinal is Jónsson (necessarily from large cardinals, since the hypothesis has strength beyond ZFC).

## 2. Mathematical Foundations

**Algebras and subalgebras.** For $\mathfrak{A}=\langle A; f_n\rangle_{n<\omega}$ with $f_n : A^{k_n}\to A$, a set $B\subseteq A$ is a subalgebra if $f_n[B^{k_n}]\subseteq B$ for all $n$. Write $\mathrm{cl}_{\mathfrak A}(X)$ for the closure of $X$.

**Partition formulation.** $\kappa$ is Jónsson iff
$$\kappa \longrightarrow [\kappa]^{<\omega}_{\kappa},$$
i.e. for every $F:[\kappa]^{<\omega}\to\kappa$ there is $H\in[\kappa]^{\kappa}$ with $F[[H]^{<\omega}]\neq\kappa$. Existence of a Jónsson algebra on $\kappa$, written $J[\kappa]$, is the negation $\kappa \nrightarrow [\kappa]^{<\omega}_\kappa$.

**Model-theoretic formulation.** $\kappa$ is Jónsson iff every structure $\mathfrak{M}$ in a countable language with $|M|=\kappa$ has a proper elementary substructure $\mathfrak{N}\prec\mathfrak{M}$ with $|N|=\kappa$. (Skolem functions convert $\prec$ into subalgebra closure; countability of the language is essential — with $\kappa$ many operations every $\kappa$ carries a "Jónsson algebra" trivially.)

**Reduction to two operations.** Countably many finitary operations can be coded into a single binary operation using a pairing bijection $\kappa\times\kappa\to\kappa$ (for infinite $\kappa$), so $J[\kappa]$ is equivalent to the existence of $f:[\kappa]^2\to\kappa$ with no $H\in[\kappa]^\kappa$ whose closure is a proper subset.

**Relatives.** $\kappa$ is **Rowbottom** if for $\lambda<\kappa$ every $F:[\kappa]^{<\omega}\to\lambda$ has $H\in[\kappa]^\kappa$ with $|F[[H]^{<\omega}]|\le\aleph_0$; $\kappa$ is **Ramsey** if $\kappa\to(\kappa)^{<\omega}_2$. Implications:
$$\text{measurable} \Rightarrow \text{Ramsey} \Rightarrow \text{Rowbottom} \Rightarrow \text{Jónsson}.$$

**Combinatorial hypotheses used in constructions.** $\square_\lambda$ (Jensen square), weak square $\square^*_\lambda$, the approachability ideal $I[\lambda^+]$, club-guessing sequences $\langle C_\delta : \delta \in S\rangle$, and pcf scales $\langle f_\alpha : \alpha<\lambda^+\rangle$ in $\prod_n \lambda_n / J^{\mathrm{bd}}$ for $\lambda = \sup_n\lambda_n$. Each supplies a canonical way to "decode" an unbounded set back to all of $\lambda^+$.

## 3. History & State of the Art (SOTA)

- **1956/1960.** Bjarni Jónsson, studying universal and homogeneous relational systems (*Math. Scand.* 4 and 8), isolates the algebras whose every proper subalgebra is small.
- **1966.** Erdős and Hajnal, *On a problem of B. Jónsson*, establish the first ZFC constructions, including a Jónsson algebra on $\aleph_1$ and on $\lambda^+$ under cardinal-arithmetic hypotheses; they also show Jónsson cardinals are large.
- **1970–1971.** Kunen (iterated ultrapowers) and Rowbottom (*Some strong axioms of infinity incompatible with $V=L$*) place Jónsson cardinals in the large-cardinal hierarchy: in $L$ every Jónsson cardinal is Ramsey, so a Jónsson cardinal implies $0^{\sharp}$ exists.
- **1983.** Donder and Koepke: an *accessible* Jónsson cardinal (e.g. $\aleph_\omega$ or $\aleph_{\omega+1}$) implies an inner model with a measurable cardinal; they tie this to the weak Chang conjecture.
- **1984.** Tryba, and independently Shelah, prove $J[\lambda^+]$ for every **regular** $\lambda$ — killing all successors of regulars at once.
- **1990s.** Shelah's pcf theory (*Cardinal Arithmetic*, Ch. III) gives $J[\lambda^+]$ for every singular $\lambda$ of **uncountable** cofinality, via club guessing, and for many $\mathrm{cf}(\lambda)=\omega$ cases under extra pcf/square hypotheses.
- **1999.** Mitchell analyses Jónsson cardinals in the core model $K$, sharpening the Mitchell-order lower bounds on consistency strength.
- **2005–2010.** Eisworth and Shelah's colouring theorems for successors of singulars, and Eisworth's Handbook chapter, present the $\mathrm{cf}(\lambda)=\omega$ case as the residual open problem.

State of the art: **no cardinal is known to be consistently Jónsson without large cardinals, and no ZFC proof of $J[\aleph_{\omega+1}]$ exists.**

## 4. Partial Results / Verified Cases

ZFC proves $J[\kappa]$ (no Jónsson cardinal) in all of the following cases.

| Class of $\kappa$ | Result | Source |
|---|---|---|
| $\kappa=\aleph_1$ | explicit algebra from injections $e_\alpha:\alpha\to\omega$ | Erdős–Hajnal 1966 |
| $\kappa=\lambda^+$, $\lambda$ regular (so all $\aleph_n$, $n\ge 1$, and $\aleph_{\alpha+1}$ for $\alpha$ successor) | $J[\lambda^+]$ | Tryba 1984; Shelah |
| $\kappa=\lambda^+$, $\lambda$ singular, $\mathrm{cf}(\lambda)>\omega$ (e.g. $\aleph_{\omega_1+1}$) | $J[\lambda^+]$ via club guessing | Shelah, *Cardinal Arithmetic* III |
| $\kappa=\lambda^+$ with $\square_\lambda$, or $\square^*_\lambda$, or $\lambda\in I[\lambda^+]$ (approachability) | $J[\lambda^+]$ | Shelah; standard in $L$ and in $K$ |
| $\kappa$ regular but not weakly inaccessible | $J[\kappa]$ (immediate from the successor cases) | — |
| any $\kappa < \aleph_\omega$ | $J[\kappa]$ | combined above |
| all $\kappa$ under $V=L$ (or in fine-structural $K$) | $J[\kappa]$ for accessible $\kappa$ | Jensen; Donder–Koepke |

Conversely, consistency of Jónsson cardinals is known: every Ramsey cardinal is Jónsson, and Prikry forcing over a measurable $\kappa$ yields a model where $\mathrm{cf}(\kappa)=\omega$ and $\kappa$ is still Jónsson. So the theorem list above cannot be extended to *all* $\kappa$ in ZFC.

## 5. Principal Obstacles

- **The uncountable-cofinality proof breaks at $\mathrm{cf}(\lambda)=\omega$.** Shelah's argument for $J[\lambda^+]$ picks a club-guessing sequence and uses that the guessing clubs $C_\delta\subseteq\delta$ of order type $\mathrm{cf}(\lambda)>\omega$ have their own club structure to run a Fodor-style pressing-down argument. When $\mathrm{cf}(\lambda)=\omega$ the guessing clubs are $\omega$-sequences, there is no stationarity inside them, and the pressing-down step evaporates.
- **Self-reference at singular limits.** The successor construction reduces "recover $\lambda^+$ from $H$" to "recover $\lambda$ from a subset of $\lambda$ of size $\lambda$" — that is, to a Jónsson algebra on the singular $\lambda$ itself, uniformly in the pieces. Jónsson algebras do **not** combine at singular limits: knowing $J[\lambda_n]$ for all $n$ with $\sup_n \lambda_n=\lambda$ does not give $J[\lambda]$, and Prikry models show no such implication can hold.
- **Large-cardinal barrier from below.** Any proof of consistency of "$\aleph_{\omega+1}$ is Jónsson" must fail in $K$; by Donder–Koepke and Mitchell it needs at least an inner model with measurables of substantial Mitchell order. Conversely, any ZFC proof of $J[\aleph_{\omega+1}]$ must avoid squares and approachability, since those are exactly the hypotheses that large cardinals destroy.
- **Colouring machinery saturates.** Walks on ordinals (Todorcevic) produce strong colourings $\rho:[\lambda^+]^2\to\lambda$ that give $J[\lambda^+]$ when $\lambda$ is regular; at singular $\lambda$ of countable cofinality the oscillation and $\rho$-functions are only known to yield weaker relations such as $\mathrm{Pr}_1$ variants, not the required onto-ness on every unbounded closed set.

## 6. The Gap

Proved (§4): $J[\lambda^+]$ whenever $\lambda$ is regular, or singular with $\mathrm{cf}(\lambda)>\omega$, or carries approachability/square. Wanted (§1): $J[\lambda^+]$ for **all** $\lambda$, in particular $\lambda=\aleph_\omega$ with $\neg\mathrm{AP}_{\aleph_\omega}$ and every scale bad.

The exact missing step: given $H\subseteq\lambda^+$ unbounded with $|H|=\lambda^+$ and $\mathrm{cf}(\lambda)=\omega$, produce from finitely many parameters in $H$ a uniformly definable surjection onto $\lambda^+$ *without* assuming a coherent sequence $\langle C_\alpha:\alpha<\lambda^+\rangle$. Equivalently: replace stationarity-based club guessing at $\mathrm{cf}(\lambda)=\omega$ by a pcf-scale device that is provably present in ZFC.

## 7. Current Research (as of June 2026)

- **pcf and scales.** Continuing work in the Shelah–Eisworth line on better scales, very good points, and the ideal $I[\lambda^+]$, aiming to extract Jónsson algebras from any ZFC-provable scale structure at $\aleph_\omega$.
- **Strong colourings.** Rinot, Todorcevic and collaborators develop rectangular and transformation-based colourings on successors of singulars; the target is upgrading $\mathrm{Pr}_1(\lambda^+,\lambda^+,\lambda^+,\mathrm{cf}\lambda)$-type statements to the onto-ness required for $J[\lambda^+]$. *(frontier — verify)*
- **Inner-model side.** Core-model induction arguments push the consistency-strength lower bound for accessible Jónsson cardinals upward, aiming for a level where the corresponding upper bound (a forcing construction) becomes plausible. *(frontier — verify)*
- **Chang-conjecture analogy.** Levinski–Magidor–Shelah obtained $\mathrm{Con}((\aleph_{\omega+1},\aleph_\omega)\twoheadrightarrow(\aleph_1,\aleph_0))$ from a huge-type hypothesis. That result does *not* imply $\aleph_{\omega+1}$ is Jónsson (its substructure has size $\aleph_1<\aleph_{\omega+1}$), but its supercompact-style forcing is the main template people try to adapt.

Groups active: set theory at Jerusalem (Shelah school), Bar-Ilan (Rinot), Ohio University (Eisworth), Toronto/CNRS (Todorcevic), Münster/Vienna/Bonn (inner-model theory).

## 8. Future Work

- Prove $J[\lambda^+]$ for $\mathrm{cf}(\lambda)=\omega$ under weak hypotheses that are ZFC-provable at $\aleph_\omega$, e.g. from the existence of *some* scale with stationarily many good points.
- Determine the exact consistency strength of "$\aleph_{\omega+1}$ is Jónsson"; a natural conjecture is that it is at least as strong as a measurable of high Mitchell order and at most a large-cardinal hypothesis in the supercompact range.
- Settle whether $\aleph_\omega$ can be Jónsson; a Prikry-style construction at a measurable followed by a Jónsson-preserving collapse of the interval $(\omega,\kappa)$ is the obvious route, and the obstruction is that known collapses add squares.
- Clarify whether $J[\kappa]$ can consistently fail for a *regular* accessible $\kappa$ — no such cardinal is known to be consistent.

## 9. Key References

- **[Foundational]** B. Jónsson. *Universal relational systems.* Mathematica Scandinavica 4 (1956), 193–208.
- **[Foundational]** P. Erdős, A. Hajnal. *On a problem of B. Jónsson.* Bulletin de l'Académie Polonaise des Sciences, Sér. Sci. Math. Astronom. Phys. 14 (1966), 19–23.
- **[Foundational]** F. Rowbottom. *Some strong axioms of infinity incompatible with the axiom of constructibility.* Annals of Mathematical Logic 3 (1971), 1–44.
- **[Foundational]** K. Kunen. *Some applications of iterated ultrapowers in set theory.* Annals of Mathematical Logic 1 (1970), 179–227.
- **[SOTA]** S. Shelah. *Cardinal Arithmetic.* Oxford Logic Guides 29, Oxford University Press, 1994 (Chapter III on Jónsson algebras).
- **[SOTA]** J. Tryba. *On Jónsson cardinals with uncountable cofinality.* Israel Journal of Mathematics 49 (1984), 315–324.
- **[SOTA]** H.-D. Donder, P. Koepke. *On the consistency strength of 'accessible' Jónsson cardinals and of the weak Chang conjecture.* Annals of Pure and Applied Logic 25 (1983), 233–261.
- **[SOTA]** W. J. Mitchell. *Jónsson cardinals, Erdős cardinals, and the core model.* Journal of Symbolic Logic 64 (1999), 1065–1086.
- **[SOTA]** J.-P. Levinski, M. Magidor, S. Shelah. *Chang's conjecture for $\aleph_\omega$.* Israel Journal of Mathematics 69 (1990), 161–172.
- **[SOTA]** T. Eisworth, S. Shelah. *Successors of singular cardinals and coloring theorems I.* Archive for Mathematical Logic 44 (2005), 597–618.
- **[Survey]** T. Eisworth. *Successors of singular cardinals.* In: Handbook of Set Theory (M. Foreman, A. Kanamori, eds.), Springer, 2010, 1229–1350.
- **[Survey]** A. Kanamori. *The Higher Infinite.* Springer, 2nd edition, 2003 (Jónsson and Rowbottom cardinals).
- **[Survey]** S. Todorcevic. *Walks on Ordinals and Their Characteristics.* Progress in Mathematics 263, Birkhäuser, 2007.

## 10. Worked Example / Concrete Special Case

**(a) $\aleph_0$ is not Jónsson.** Take $\mathfrak{A}=\langle \omega; 0, S\rangle$ with $S(n)=n+1$. A subalgebra contains $0$ and is closed under $S$, hence equals $\omega$. There is no proper subalgebra at all, so certainly none of size $\aleph_0$.

**(b) $\aleph_1$ is not Jónsson (Erdős–Hajnal).** For each infinite $\alpha<\omega_1$ fix an injection $e_\alpha:\alpha\to\omega$. Define unary operations $g_n:\omega_1\to\omega_1$ for $n<\omega$:
$$g_n(\beta)=\begin{cases} e_\beta^{-1}(n) & \text{if } \beta \ge \omega \text{ and } n\in\mathrm{ran}(e_\beta),\\ \beta & \text{otherwise.}\end{cases}$$
Let $\mathfrak{A}=\langle\omega_1; g_n\rangle_{n<\omega}$ and let $B\subseteq\omega_1$ be a subalgebra with $|B|=\aleph_1$.

*Step 1.* Since $|B|=\aleph_1$ and every proper initial segment of $\omega_1$ is countable, $B$ is unbounded in $\omega_1$.

*Step 2.* Fix $\beta\in B$ with $\beta\ge\omega$. Because $e_\beta:\beta\to\omega$ is injective, for every $\alpha<\beta$ there is a unique $n=e_\beta(\alpha)$, and then $g_n(\beta)=\alpha$. Closure gives $\beta\subseteq B$.

*Step 3.* By Step 1 such $\beta$ exist cofinally, so $B=\bigcup\{\beta : \beta\in B\}=\omega_1$.

Hence every subalgebra of size $\aleph_1$ is all of $\omega_1$: $\mathfrak{A}$ is a Jónsson algebra on $\aleph_1$, and $\omega_1 \nrightarrow[\omega_1]^{<\omega}_{\omega_1}$.

**(c) Why the same recipe stalls at $\aleph_{\omega+1}$.** Repeat with $\lambda=\aleph_\omega$ and injections $e_\alpha:\alpha\to\lambda$ for $\alpha<\lambda^+$. Steps 1 and 2 still work: an unbounded $B$ of size $\lambda^+$ picks up $\beta\subseteq \mathrm{cl}(B)$ once the "decoder" indices used lie in $B$. But the decoder now needs $\lambda=\aleph_\omega$ many unary operations, while a Jónsson algebra may use only countably many. Coding $\lambda$ indices into finitely many operations requires recovering all of $\lambda$ from the set $B\cap\lambda$ of size $\lambda$ — precisely a Jónsson algebra on the singular cardinal $\aleph_\omega$, uniform across the cofinal sequence $\langle\aleph_n\rangle_{n<\omega}$. Since $\mathrm{cf}(\aleph_\omega)=\omega$, no club-guessing sequence supplies that uniformity, and this is exactly the gap of §6.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*