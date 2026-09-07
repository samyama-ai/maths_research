---
id: 08-logic-set-theory/jonsson-cardinals-existence
title: "Jonsson Cardinals Existence"
topic: 08-logic-set-theory
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Jónsson Cardinals Existence

> **Topic:** Mathematical Logic & Set Theory · **ID:** `08-logic-set-theory/jonsson-cardinals-existence` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

A cardinal $\kappa$ is **Jónsson** if every algebra with universe of size $\kappa$ and countably many finitary operations has a proper subalgebra of size $\kappa$. The cluster of open problems is:

1. **Consistency strength.** Determine the exact strength of "there exists a Jónsson cardinal". Known bracket: below a Ramsey cardinal, above an inner model with many measurables. Is $\mathrm{Con}(\exists$ Ramsey$)$ strictly stronger than $\mathrm{Con}(\exists$ Jónsson$)$? Equivalently: is every Jónsson cardinal Ramsey in some canonical inner model, and can the two notions be separated by consistency strength at all?
2. **Jónsson successors of singulars.** Can $\lambda^{+}$ be Jónsson for $\lambda$ singular? The first open instance is $\aleph_{\omega+1}$. ZFC rules out every other kind of successor.
3. **Smallness.** Must a Jónsson cardinal be a limit cardinal? Must the least Jónsson cardinal be inaccessible, or even be a limit of measurables in an inner model?

A complete solution to (1) is an equiconsistency proof or a strict-strength separation; to (2) a ZFC proof that $\lambda^{+}$ is never Jónsson, or a forcing/large-cardinal model where some $\lambda^{+}$ is.

## 2. Mathematical Foundations

**Algebras.** An *algebra* is a structure $\mathfrak{A}=\langle A, f_n\rangle_{n<\omega}$ where each $f_n : A^{k_n}\to A$ is finitary. A *subalgebra* is a subset closed under all $f_n$. Write $\mathrm{cl}^{\mathfrak A}(X)$ for the closure of $X$.

**Definition (Jónsson).**
$$\kappa \text{ is Jónsson} \iff \forall \mathfrak{A}\ \big(|A|=\kappa \Rightarrow \exists B\subsetneq A,\ |B|=\kappa,\ B \text{ a subalgebra}\big).$$
A **Jónsson algebra** on $\kappa$ is a counterexample: an algebra of size $\kappa$ all of whose proper subalgebras have size $<\kappa$. So $\kappa$ is Jónsson iff no Jónsson algebra on $\kappa$ exists.

**Partition characterization (Erdős–Hajnal).** Writing $\kappa\to[\kappa]^{<\omega}_{\kappa}$ for: for every $F:[\kappa]^{<\omega}\to\kappa$ there is $H\in[\kappa]^{\kappa}$ with $F''[H]^{<\omega}\neq\kappa$,
$$\kappa \text{ is Jónsson} \iff \kappa\to[\kappa]^{<\omega}_{\kappa}.$$
The reduction is Skolem-function bookkeeping: the $F$-closure of $H$ is a subalgebra, and missing one value forces properness.

**Comparison notions.**
- $\kappa$ is **Ramsey** if $\kappa\to(\kappa)^{<\omega}_2$.
- $\kappa$ is **Rowbottom** if every $\mathfrak A$ of size $\kappa$ with a distinguished $\omega_1$-small predicate has an elementary substructure of size $\kappa$ meeting the predicate in a set of size $<\omega_1$; formally $\kappa\to[\kappa]^{<\omega}_{\lambda,\omega_1}$ for all $\lambda<\kappa$.
- Implications: measurable $\Rightarrow$ Ramsey $\Rightarrow$ Rowbottom $\Rightarrow$ Jónsson, all strict in strength except possibly the last.

**Square principle.** $\square_\lambda$: a sequence $\langle C_\alpha : \alpha\in \mathrm{Lim}(\lambda^{+})\rangle$ with $C_\alpha$ club in $\alpha$, $\mathrm{otp}(C_\alpha)\le\lambda$, and $C_\alpha\cap\beta = C_\beta$ for $\beta\in\mathrm{Lim}(C_\alpha)$. $\square_\lambda$ yields a Jónsson algebra on $\lambda^{+}$.

**PCF apparatus.** For $\lambda$ singular with $\mathrm{cf}(\lambda)=\mu$ and an increasing sequence $\langle\lambda_i : i<\mu\rangle$ cofinal in $\lambda$, a *scale* is $\langle f_\alpha : \alpha<\lambda^{+}\rangle \subseteq \prod_i\lambda_i$ increasing and cofinal modulo the bounded ideal. Shelah's theorem $\mathrm{cf}(\prod_i\lambda_i/J^{bd})=\lambda^{+}$ guarantees such scales exist; good and better scales are the engine of all ZFC non-Jónsson results at successors of singulars.

## 3. History & State of the Art (SOTA)

- **1956.** Bjarni Jónsson asks, in the context of universal relational systems, whether every infinite algebra of size $\kappa$ has a proper subalgebra of the same size. $\omega$ answers no immediately; the question becomes a large-cardinal question.
- **1965.** Keisler and Rowbottom show that a Jónsson cardinal implies $V\neq L$ — the first proof that Jónssonness is a genuine large-cardinal property, not a combinatorial accident.
- **1966.** Erdős and Hajnal, *On a problem of B. Jónsson*, prove the partition characterization $\kappa\to[\kappa]^{<\omega}_\kappa$ and establish the basic closure facts.
- **1970s.** Rowbottom and Kunen situate Jónsson between Ramsey and $0^{\\#}$-type hypotheses. Devlin–Jensen covering ("Marginalia to a theorem of Silver") gives: if $0^{\\#}$ does not exist there are no Jónsson cardinals.
- **1978.** Shelah, *Jónsson algebras in successor cardinals*: if $\lambda$ is regular then $\lambda^{+}$ carries a Jónsson algebra. Kills $\aleph_1,\aleph_2,\dots,\aleph_n$ outright.
- **1983.** Donder–Koepke: an "accessible" Jónsson cardinal (e.g. one $\le 2^{\aleph_0}$) implies an inner model with a measurable; same for weak Chang conjecture.
- **1984.** Tryba (and independently Woodin) push non-existence at successors of singulars of uncountable cofinality; completed by Shelah's club-guessing machinery in *Cardinal Arithmetic* (1994): $\lambda$ singular with $\mathrm{cf}(\lambda)>\omega$ $\Rightarrow$ $\lambda^{+}$ not Jónsson.
- **1999.** Mitchell, *Jónsson cardinals, Erdős cardinals, and the core model*: below an inner model with a Woodin cardinal, every Jónsson cardinal is Ramsey in $K$. This is the sharpest lower bound known and the reason most set theorists expect Jónsson and Ramsey to be equiconsistent.
- **2010.** Eisworth's Handbook chapter *Successors of Singular Cardinals* consolidates the PCF attack on the $\mathrm{cf}(\lambda)=\omega$ case.

## 4. Partial Results / Verified Cases

Cases where the question is fully settled:

- **$\kappa=\omega$:** not Jónsson. Explicit Jónsson algebra in §10.
- **$\kappa=\lambda^{+}$, $\lambda$ regular:** not Jónsson (Shelah 1978). Covers all $\aleph_n$, $1\le n<\omega$, and $\lambda^{+}$ for every regular $\lambda$ in ZFC alone.
- **$\kappa=\lambda^{+}$, $\lambda$ singular with $\mathrm{cf}(\lambda)>\omega$:** not Jónsson (Tryba 1984; Shelah, club guessing). So $\aleph_{\omega_1+1}$ is never Jónsson.
- **$\kappa=\lambda^{+}$ with $\square_\lambda$:** not Jónsson. Hence no successor Jónsson cardinals in $L$, or in any $\square$-satisfying core model.
- **$\kappa = \omega_1$:** strongly non-Jónsson — Todorcevic's $\omega_1\not\to[\omega_1]^{2}_{\omega_1}$ (1987) gives a two-place Jónsson algebra.
- **Upper bound:** Ramsey $\Rightarrow$ Rowbottom $\Rightarrow$ Jónsson. So $\mathrm{Con}(\text{ZFC}+\exists\text{ Ramsey})\Rightarrow \mathrm{Con}(\text{ZFC}+\exists\text{ Jónsson})$; measurable cardinals are Jónsson.
- **Lower bounds:** no Jónsson cardinal if $0^{\\#}$ fails (Devlin–Jensen); an inner model with a measurable from an accessible Jónsson (Donder–Koepke 1983); Ramsey in $K$ below a Woodin (Mitchell 1999).
- **Successors of singulars of cofinality $\omega$, restricted:** if $\lambda$ is a strong-limit singular of cofinality $\omega$ carrying a *very good scale*, or if $\lambda^{+}$ carries a suitable club-guessing ideal, $\lambda^{+}$ is not Jónsson.
- **Without choice:** under $\mathrm{AD}$, $\aleph_1$ is measurable hence Jónsson (Kleinberg 1977). The problem is a ZFC problem.

## 5. Principal Obstacles

- **Core-model induction saturates.** Mitchell's argument computes $K$ under an anti-large-cardinal hypothesis (no inner model with a Woodin). Above a Woodin, $K$ is not available in usable form, so no lower bound beyond that region has been extracted. The technique is bounded by the state of inner model theory, not by anything about Jónsson algebras.
- **No known separating forcing.** Every model of "$\exists$ Jónsson" ever produced is a model of "$\exists$ Ramsey" (or built by collapsing above one). There is no forcing that destroys Ramseyness while preserving the $\kappa\to[\kappa]^{<\omega}_\kappa$ relation, because that relation is preserved by so few extensions: it fails after adding $\kappa$ Cohen reals, but the failure kills both properties at once.
- **PCF gives colorings only when scales are good.** The ZFC constructions of Jónsson algebras on $\lambda^{+}$ all run through a scale plus a guessing device (club guessing at $\mathrm{cf}>\omega$, approachability, better scales). At $\mathrm{cf}(\lambda)=\omega$ every such device is consistently absent — Gitik–Sharon-style models kill approachability and good scales at $\aleph_\omega$ from supercompactness. So the standard toolkit provably cannot settle $\aleph_{\omega+1}$.
- **$\omega$-cofinality defeats club guessing.** Club guessing needs $S\subseteq\lambda^{+}$ stationary with $\mathrm{cf}(\alpha)$ uncountable to build the coherent guessing sequence; at $\mathrm{cf}(\lambda)=\omega$ the relevant points have cofinality $\omega$ and the guessing sequences are not ZFC-provable in the form required.
- **Non-elementary closure.** Jónssonness is about arbitrary algebras, not elementary substructures of $H_\theta$; the usual "take an elementary submodel and reflect" argument gives only a subalgebra of the same size that may equal the whole, so the properness step needs a *specific* omitted value, which is exactly where the combinatorics is hard.

## 6. The Gap

Two crisp boundaries.

- **Strength.** Proved: Jónsson $\Rightarrow$ Ramsey in $K$, assuming no inner model with a Woodin cardinal. Wanted: either (a) remove the anti-large-cardinal hypothesis, giving a full equiconsistency Jónsson $\equiv$ Ramsey; or (b) produce a model of ZFC with a Jónsson cardinal but no inner model with a Ramsey. The missing step in (a) is a core model $K$ at and above a Woodin cardinal with the covering properties Mitchell's argument uses. No candidate construction exists for (b).
- **Successors.** Proved: $\lambda^{+}$ not Jónsson for $\lambda$ regular, for $\lambda$ singular of uncountable cofinality, and for $\lambda$ singular of cofinality $\omega$ *when* a good/better scale or approachability-style guessing exists at $\lambda$. The gap is exactly: $\lambda$ singular, $\mathrm{cf}(\lambda)=\omega$, no good scale, no approachable-set guessing. Crossing it means constructing a coloring $F:[\lambda^{+}]^{<\omega}\to\lambda^{+}$ onto every $\lambda^{+}$-sized closure, from PCF data alone with no guessing sequence — or forcing $\aleph_{\omega+1}$ Jónsson from a supercompact.

## 7. Current Research (as of June 2026)

- **PCF / successors of singulars.** Eisworth (Ohio) and Rinot (Bar-Ilan) continue the "getting more colors" program: strengthening $\lambda^{+}\not\to[\lambda^{+}]^{2}_{\lambda^{+}}$-type results and locating the minimal guessing hypothesis needed for a Jónsson algebra on $\lambda^{+}$. Rinot's parameterized walks-on-ordinals principles ($\mathrm{U}(\kappa,\mu,\theta,\chi)$) have absorbed several previously separate constructions. *(frontier — verify)* Recent work reduces the $\mathrm{cf}(\lambda)=\omega$ case to a single instance of a club-guessing ideal on $\lambda^{+}$.
- **Inner model theory.** Groups around Schindler (Münster), Steel (Berkeley, emeritus), Sargsyan (IMPAN) work on core models at the Woodin level; a $K$ past one Woodin would immediately upgrade Mitchell's theorem. *(frontier — verify)*
- **Generalized Erdős/Ramsey hierarchy.** Sharpe–Welch-style "greatly Erdős" cardinals and virtual large cardinals (Gitman, Schindler) are used to calibrate where Jónssonness sits among the Ramsey-like properties; the reflection is that Jónsson is a *consequence* rather than a member of that hierarchy.
- **Determinacy side.** Under $\mathrm{AD}^{+}$, which $\aleph_n$ and $\aleph_{\omega\cdot n+1}$ are Jónsson is an active computation, but it does not bear on the ZFC problem.

## 8. Future Work

- Prove in ZFC that $\aleph_{\omega+1}$ is not Jónsson, or show consistency from a supercompact via Prikry-type forcing with a Radin-style preservation of $\kappa\to[\kappa]^{<\omega}_\kappa$ across the collapse.
- Isolate a "Jónsson ideal" on $\lambda^{+}$ whose non-triviality is equivalent to Jónssonness, and compute its saturation from PCF.
- Extend Mitchell's core-model computation to the region of finitely many Woodins.
- Settle whether the least Jónsson cardinal can be singular of cofinality $\omega$ while not being a limit of Ramsey cardinals in $K$.
- Determine whether Jónsson is preserved by $\kappa$-c.c. forcing in general; a preservation theorem would give the first separation candidate.

## 9. Key References

- **[Foundational]** B. Jónsson. *Universal relational systems.* Mathematica Scandinavica 4 (1956), 193–208.
- **[Foundational]** P. Erdős and A. Hajnal. *On a problem of B. Jónsson.* Bulletin de l'Académie Polonaise des Sciences, Sér. Sci. Math. Astronom. Phys. 14 (1966), 19–23.
- **[Foundational]** H. J. Keisler and F. Rowbottom. *Constructible sets and weakly compact cardinals.* Notices of the American Mathematical Society 12 (1965), 373–374.
- **[Foundational]** S. Shelah. *Jónsson algebras in successor cardinals.* Israel Journal of Mathematics 30 (1978), 57–64.
- **[Foundational]** K. Devlin and R. B. Jensen. *Marginalia to a theorem of Silver.* In: Logic Conference Kiel 1974, Lecture Notes in Mathematics 499, Springer, 1975.
- **[SOTA]** W. J. Mitchell. *Jónsson cardinals, Erdős cardinals, and the core model.* Journal of Symbolic Logic 64 (1999), 1065–1086.
- **[SOTA]** H.-D. Donder and P. Koepke. *On the consistency strength of 'accessible' Jónsson cardinals and of the weak Chang conjecture.* Annals of Pure and Applied Logic 25 (1983), 233–261.
- **[SOTA]** J. Tryba. *On Jónsson cardinals with uncountable cofinality.* Israel Journal of Mathematics 49 (1984), 315–324.
- **[SOTA]** S. Shelah. *Cardinal Arithmetic.* Oxford Logic Guides 29, Oxford University Press, 1994.
- **[SOTA]** S. Todorcevic. *Partitioning pairs of countable ordinals.* Acta Mathematica 159 (1987), 261–294.
- **[Survey]** T. Eisworth. *Successors of Singular Cardinals.* In: Handbook of Set Theory (M. Foreman and A. Kanamori, eds.), Springer, 2010, 1229–1350.
- **[Survey]** A. Kanamori. *The Higher Infinite: Large Cardinals in Set Theory from Their Beginnings.* 2nd ed., Springer, 2003.
- **[Survey]** T. Jech. *Set Theory,* The Third Millennium Edition. Springer, 2003.
- **[Related]** E. M. Kleinberg. *Infinitary Combinatorics and the Axiom of Determinateness.* Lecture Notes in Mathematics 612, Springer, 1977.

## 10. Worked Example / Concrete Special Case

**A Jónsson algebra on $\omega$.** Let $\mathfrak{A}=\langle \omega, p\rangle$ with the single unary operation
$$p(n)=\begin{cases}n-1 & n>0\\ 0 & n=0.\end{cases}$$
Let $B\subseteq\omega$ be a subalgebra with $|B|=\aleph_0$. $B$ is infinite, so it is unbounded in $\omega$. Take any $m\in\omega$ and pick $b\in B$ with $b\ge m$. Closure under $p$ gives $b, b-1,\dots, m \in B$. Hence $B=\omega$. No proper subalgebra of size $\aleph_0$ exists: $\omega$ is not Jónsson. In partition form, $F(\{n\})=p(n)$ witnesses $\omega\not\to[\omega]^{<\omega}_{\omega}$.

**Why $\lambda^{+}$ resists for $\lambda$ regular (sketch of Shelah's mechanism).** Fix injections $e_\alpha:\alpha\to\lambda$ for $\lambda\le\alpha<\lambda^{+}$. Define $d:[\lambda^{+}]^{2}\to\lambda$ by $d(\alpha,\beta)=e_\beta(\alpha)$ for $\alpha<\beta$. If $X\subseteq\lambda^{+}$ has size $\lambda^{+}$, then for each $\beta$ above $\sup$ of a $\lambda$-sized initial piece $X_0\subseteq X$, the map $e_\beta\restriction X_0$ is injective into $\lambda$, so $d''(X_0\times\{\beta\})$ has size $\lambda$. Adding a pairing operation that decodes $(\xi,\beta)\mapsto$ the $\xi$-th element above $\beta$ turns this "large fibre" property into surjectivity of the closure onto $\lambda^{+}$, so every $\lambda^{+}$-sized subalgebra is everything. Regularity of $\lambda$ is used to guarantee $|X_0|=\lambda$ below a single $\beta$.

**Where it breaks at $\aleph_{\omega+1}$.** Here $\lambda=\aleph_\omega$ is singular of cofinality $\omega$: $e_\beta$ maps $\beta$ injectively into $\aleph_\omega=\sup_n\aleph_n$, and a $\lambda$-sized $X_0$ can have $e_\beta''X_0$ spread across all $\aleph_n$ with no single $\aleph_n$ capturing a large piece. Recovering surjectivity requires a scale $\langle f_\alpha\rangle\subseteq\prod_n\aleph_n$ that is *good* at enough points; and good scales at $\aleph_\omega$ can be forced to fail (Gitik–Sharon) from a supercompact. That is exactly the open case.

**Positive direction.** If $\kappa$ is Ramsey and $F:[\kappa]^{<\omega}\to\kappa$, apply $\kappa\to(\kappa)^{<\omega}_{2}$ to the colorings induced by $F$ to obtain $H\in[\kappa]^{\kappa}$ of good indiscernibles; the closure $\mathrm{cl}^{F}(H)$ has order type $<\kappa$ in each initial segment and omits a value, so $\kappa\to[\kappa]^{<\omega}_{\kappa}$ and $\kappa$ is Jónsson.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*