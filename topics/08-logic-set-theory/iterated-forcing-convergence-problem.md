---
id: 08-logic-set-theory/iterated-forcing-convergence-problem
title: "Iterated Forcing Convergence Problem"
topic: 08-logic-set-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Iterated Forcing Convergence Problem

> **Topic:** Mathematical Logic & Set Theory · **ID:** `08-logic-set-theory/iterated-forcing-convergence-problem` · **Status:** open

## 1. Problem Statement / Conjecture

Forcing iterations are built by transfinite recursion; the content of any construction lies at the **limit stages**, where a *support* must be chosen and where the defining property of the iterands may fail to survive. Call a class $\Gamma$ of forcing notions **convergent** if there is a support notion $\mathcal{S}$ such that every $\mathcal{S}$-iteration whose iterands are forced to lie in $\Gamma$ is itself in $\Gamma$, at every limit stage, for iterations of arbitrary length.

**The Iterated Forcing Convergence Problem.** Characterize the convergent classes. Concretely, the two standing open instances are:

1. **(SSP iteration problem, Foreman–Magidor–Shelah.)** Is the class $\mathrm{SSP}$ of forcings preserving stationary subsets of $\omega_1$ convergent? Equivalently, is there an iteration theorem for $\mathrm{SSP}$ not routed through semiproperness — one that does not require the large-cardinal-flavoured hypothesis "every $\mathrm{SSP}$ forcing is semiproper"?
2. **(NNR iteration problem, Shelah.)** Is the class of proper forcings adding no new reals convergent under countable support, in a form with a complete, independently verified proof? Shelah's Chapter XVIII apparatus (D-completeness, $\aleph_2$-p.i.c.) is the only known route and has never been fully absorbed.

A complete solution to an instance is either an iteration theorem with proof, or a model in which a length-$\omega_1$ (resp. length-$\omega_2$) iteration of $\Gamma$-forcings, under every support notion, leaves $\Gamma$.

## 2. Mathematical Foundations

Let $\langle \mathbb{P}_\alpha, \dot{\mathbb{Q}}_\alpha : \alpha < \delta\rangle$ be an iteration: $\mathbb{P}_0 = \{1\}$, $\mathbb{P}_{\alpha+1} = \mathbb{P}_\alpha * \dot{\mathbb{Q}}_\alpha$ with $\Vdash_{\mathbb{P}_\alpha} \dot{\mathbb{Q}}_\alpha$ is a poset. Conditions are functions $p$ with $\mathrm{dom}(p) \subseteq \delta$ and $p\restriction\alpha \Vdash p(\alpha) \in \dot{\mathbb{Q}}_\alpha$; at limits one fixes
$$\mathrm{supp}(p) = \{\alpha : p\restriction\alpha \not\Vdash p(\alpha) = \dot{1}_{\alpha}\},$$
and takes **finite support** ($|\mathrm{supp}(p)|<\omega$), **countable support** ($|\mathrm{supp}(p)|\le\omega$), **revised countable support (RCS)**, or a symmetric/side-condition system.

**Properness.** $\mathbb{Q}$ is proper iff for all large regular $\lambda$ and all countable $M \prec H_\lambda$ with $\mathbb{Q}\in M$, every $p \in \mathbb{Q}\cap M$ has an $(M,\mathbb{Q})$-generic extension $q$:
$$\forall D \in M \ (D \text{ dense in } \mathbb{Q} \ \Rightarrow\ q \Vdash \dot{G}\cap D\cap M \neq \emptyset).$$

**Semiproperness.** Weaken genericity to $q \Vdash M[\dot G]\cap \omega_1 = M \cap \omega_1$.

**SSP.** $\mathbb{Q}\in\mathrm{SSP}$ iff for every stationary $S\subseteq\omega_1$, $\Vdash_{\mathbb{Q}} S$ is stationary. The inclusions
$$\text{ccc} \cup \sigma\text{-closed} \subseteq \text{proper} \subseteq \text{semiproper} \subseteq \mathrm{SSP}$$
are all strict; e.g. Namba forcing $\mathrm{Nm}$ is semiproper under CH but never proper (it changes $\mathrm{cf}(\omega_2)$ to $\omega$).

**Convergence, formally.** $\Gamma$ is $\mathcal{S}$-convergent iff for every limit $\delta$ and every $\mathcal{S}$-iteration with $\Vdash_\alpha \dot{\mathbb{Q}}_\alpha\in\Gamma$ for all $\alpha<\delta$, one has $\mathbb{P}_\delta\in\Gamma$. The known positive results:

- $\Gamma=\text{ccc}$, $\mathcal{S}=$ finite support (Solovay–Tennenbaum 1971).
- $\Gamma=\sigma$-closed, $\mathcal{S}=$ countable support (elementary).
- $\Gamma=$ proper, $\mathcal{S}=$ countable support (Shelah 1978).
- $\Gamma=$ semiproper, $\mathcal{S}=$ RCS (Shelah 1987), assuming each iterand is semiproper *in the intermediate model*.

**Forcing axioms as fixed points.** If $\Gamma$ is convergent and admits a length-$\kappa$ bookkeeping with $\kappa$ supercompact, one gets a model of
$$\mathrm{FA}_{\aleph_1}(\Gamma):\quad \forall \mathbb{Q}\in\Gamma\ \forall \{D_\xi\}_{\xi<\omega_1} \text{ dense } \ \exists \text{ filter } G \ \forall \xi\, (G\cap D_\xi\neq\emptyset).$$
$\mathrm{FA}_{\aleph_1}(\text{ccc})=\mathrm{MA}_{\aleph_1}$, $\mathrm{FA}_{\aleph_1}(\text{proper})=\mathrm{PFA}$, $\mathrm{FA}_{\aleph_1}(\mathrm{SSP})=\mathrm{MM}$. Convergence is thus the engine behind every forcing axiom.

## 3. History & State of the Art (SOTA)

- **1971.** Solovay and Tennenbaum invent iterated forcing to refute Souslin's hypothesis' negation; the ccc finite-support iteration theorem is the first convergence result, proved by a $\Delta$-system argument at limits.
- **1978–1982.** Shelah isolates properness precisely as the largest natural class provably convergent under countable support, and proves the countable support iteration theorem. Baumgartner's 1983 survey *Iterated forcing* standardizes the machinery.
- **1987.** Shelah's RCS iteration theorem for semiproper forcing; SPFA is shown to imply MM.
- **1988.** Foreman, Magidor and Shelah prove Con(supercompact) $\Rightarrow$ Con(MM), by showing that under the iteration hypothesis every SSP forcing is semiproper, and that MM itself implies $\mathrm{SSP}=$ semiproper. The *direct* SSP iteration theorem is left open — the "convergence" question in its sharpest form.
- **1993–2010.** Goldstern's preservation-of-properties framework ("tools for your forcing construction"); Schlindwein's simplified RCS; Zapletal's idealized-forcing account of definable convergence.
- **2014–2015.** Neeman's two-type side-condition iterations and Asperó–Mota's finitely-proper symmetric systems break the $2^{\aleph_0}\le\aleph_2$ ceiling for some fragments, i.e. give *new supports* where countable support cannot converge.
- **2021.** Asperó–Schindler prove $\mathrm{MM}^{++}\Rightarrow(*)$, making the exact strength of the SSP fixed point a central object.

## 4. Partial Results / Verified Cases

| Class $\Gamma$ | Support | Convergent? |
|---|---|---|
| ccc | finite | Yes, all lengths (Solovay–Tennenbaum) |
| $\sigma$-closed | countable | Yes, all lengths |
| proper | countable | Yes, all lengths; forces $2^{\aleph_0}\le\aleph_2$ |
| proper $+$ $\omega^\omega$-bounding | countable | Yes (Shelah; preservation of "$\sqsubseteq$-properness") |
| proper $+$ preserving Lebesgue-null/meager-null bases | countable | Yes (Goldstern's preservation theorems) |
| semiproper | RCS | Yes, lengths $<$ first inaccessible-limit obstruction |
| Souslin ccc, definable proper forcings | finite/countable | Yes (Judah–Shelah; Zapletal for $\sigma$-ideal quotients) |
| proper $+$ adds no reals | countable | Only via Shelah XVIII (D-completeness $+$ $\aleph_2$-p.i.c.); status contested |
| SSP | any known | **Open**; yes under "every SSP is semiproper", which follows from MM |
| ccc, length $\ge\omega_1$, countable support | countable | **No** (see §10) |
| proper, forcing $2^{\aleph_0}=\aleph_3$ | countable | **No**; possible for restricted fragments (Neeman; Asperó–Mota) |

Parameter thresholds: countable support iterations of nontrivial proper forcings of length $\ge\omega_2$ collapse cardinals unless one stops at $\omega_2$; hence PFA gives $2^{\aleph_0}=\aleph_2$, and every attempt to obtain $\mathrm{FA}_{\aleph_1}(\Gamma)$ with $\mathfrak{c}>\aleph_2$ requires a support outside the finite/countable dichotomy.

## 5. Principal Obstacles

- **Limit stages are not local.** Properness is preserved because $(M,\mathbb{P}_\delta)$-generic conditions can be built by a *fusion* along an $\omega$-chain of models, using that each iterand is proper in the intermediate extension. For SSP there is no known way to build the generic condition: SSP is a statement about stationary sets in $V$, and the induction hypothesis at stage $\alpha$ concerns stationary sets of $V^{\mathbb{P}_\alpha}$ that did not exist in $V$. The induction has no stable invariant.
- **Cofinality $\omega$ collapse.** At limits of cofinality $\omega$, RCS must allow conditions with support of order type $\omega$ that becomes bounded after forcing; the "revision" is exactly what makes Namba-like iterands survive. No analogous revision is known for arbitrary SSP forcings, which may change $\mathrm{cf}(\lambda)$ for many $\lambda$ simultaneously.
- **Countable support forces $\mathfrak{c}\le\aleph_2$.** A CS iteration of length $\omega_2$ over a model of CH is $\aleph_2$-cc and adds $\aleph_2$ reals; longer iterations collapse. So the support notion caps the continuum, and any convergence theorem yielding $\mathfrak{c}>\aleph_2$ must use combinatorially new supports — where the $\Delta$-system and fusion tools both fail.
- **Verification barrier.** Shelah's NNR chapter is famously dense; the "adds no reals" property is not preserved by two-step composition in general, so the iteration theorem needs an artificial strengthening (D-completeness relative to a simple $\aleph_1$-completeness system) whose limit-stage bookkeeping has resisted independent reconstruction.

## 6. The Gap

Everything proven sits inside classes with a **local, model-relative generic condition criterion**: proper, semiproper, and their preservation-augmented refinements each say "for countable $M\prec H_\lambda$, every $p\in \mathbb{Q}\cap M$ extends to a condition generic in a specified sense". Convergence is then a fusion argument. SSP has no such criterion: it is a $\Pi_1$ statement over $H_{\mathfrak{c}^+}$ quantifying over stationary sets, with no known localization to countable elementary submodels.

The precise step to cross: either (a) find a first-order, $M$-local reformulation $\Phi(M,\mathbb{Q},p,q)$ equivalent to SSP in ZFC and closed under two-step iteration, or (b) construct, in ZFC or from a modest hypothesis, a sequence $\langle\dot{\mathbb{Q}}_\alpha:\alpha<\omega_1\rangle$ of SSP iterands whose limit under *every* support kills a stationary set. Result (b) would show the FMS large-cardinal detour is unavoidable.

## 7. Current Research (as of June 2026)

- **Side-condition iterations.** Neeman-style two-type sequences of models, and Asperó–Mota symmetric systems, are being pushed toward SSP fragments and toward $\mathrm{FA}$ variants with $\mathfrak{c}=\aleph_3$. Groups at Vienna (KGRC), Barcelona, UC Irvine and Bonn are the main centres. *(frontier — verify)*
- **Virtual/generic large-cardinal reformulations** of the SSP iteration hypothesis, aiming to calibrate exactly which fragment of "SSP = semiproper" is needed. *(frontier — verify)*
- **$(*)$-axiom route.** After Asperó–Schindler, work on $\mathbb{P}_{\max}$ presentations of the SSP fixed point asks whether the fixed point can be reached by a *non-iterative* construction, bypassing convergence entirely.
- **Machine-checked forcing.** Formalizations of the ccc and proper iteration theorems (Lean/Isabelle set-theory libraries) are being extended; a formal check of Shelah's NNR chapter is an announced target. *(frontier — verify)*

## 8. Future Work

1. Isolate a "local SSP" property closed under two-step composition; test it against Namba forcing and against the $\mathrm{SSP}$ forcings that shoot clubs through complements of stationary sets.
2. Develop convergence for iterations of length $>\omega_2$ under supports with $\aleph_2$-sized conditions, targeting $\mathrm{PFA}$-like axioms with $\mathfrak{c}=\aleph_3$.
3. Produce a complete, refereed, ideally formalized exposition of the NNR iteration theorem, with an explicit statement of the composition lemma.
4. Determine whether "every SSP forcing is semiproper" is equiconsistent with a supercompact, or strictly weaker.

## 9. Key References

- **[Foundational]** R. M. Solovay, S. Tennenbaum. *Iterated Cohen extensions and Souslin's problem.* Annals of Mathematics 94 (1971), 201–245.
- **[Foundational]** J. E. Baumgartner. *Iterated forcing.* In: Surveys in Set Theory (A. R. D. Mathias, ed.), LMS Lecture Note Series 87, Cambridge University Press, 1983.
- **[Foundational]** S. Shelah. *Proper and Improper Forcing*, 2nd edition. Perspectives in Mathematical Logic, Springer, 1998.
- **[Foundational]** M. Foreman, M. Magidor, S. Shelah. *Martin's Maximum, saturated ideals, and non-regular ultrafilters. Part I.* Annals of Mathematics 127 (1988), 1–47.
- **[Foundational]** S. Shelah. *Semiproper forcing axiom implies Martin maximum but not $\mathrm{PFA}^+$.* Journal of Symbolic Logic 52 (1987), 360–367.
- **[Survey]** U. Abraham. *Proper forcing.* In: Handbook of Set Theory (M. Foreman, A. Kanamori, eds.), Springer, 2010, 333–394.
- **[Survey]** J. Cummings. *Iterated forcing and elementary embeddings.* In: Handbook of Set Theory, Springer, 2010, 775–883.
- **[Survey]** T. Jech. *Set Theory*, 3rd millennium edition. Springer Monographs in Mathematics, 2003 (Part III).
- **[SOTA]** M. Goldstern. *Tools for your forcing construction.* In: Set Theory of the Reals, Israel Mathematical Conference Proceedings 6 (1993), 305–360.
- **[SOTA]** C. Schlindwein. *Simplified RCS iterations.* Archive for Mathematical Logic 32 (1993), 341–349.
- **[SOTA]** I. Neeman. *Forcing with sequences of models of two types.* Notre Dame Journal of Formal Logic 55 (2014), 265–298.
- **[SOTA]** D. Asperó, M. A. Mota. *Forcing consequences of PFA together with the continuum large.* Transactions of the AMS 367 (2015), 6103–6129.
- **[SOTA]** D. Asperó, R. Schindler. *Martin's Maximum$^{++}$ implies Woodin's axiom $(*)$.* Annals of Mathematics 193 (2021), 793–835.
- **[SOTA]** J. Zapletal. *Forcing Idealized.* Cambridge Tracts in Mathematics 174, Cambridge University Press, 2008.

## 10. Worked Example / Concrete Special Case

**Convergence of ccc at a finite-support limit.** Let $\delta$ be a limit and $\mathbb{P}_\delta$ the FS limit of ccc iterands. Suppose $A=\{p_\xi:\xi<\omega_1\}\subseteq\mathbb{P}_\delta$ is an antichain. Each $\mathrm{supp}(p_\xi)$ is finite, so by the $\Delta$-system lemma there is $S\in[\omega_1]^{\aleph_1}$ and a finite root $r\subseteq\delta$ with $\mathrm{supp}(p_\xi)\cap\mathrm{supp}(p_\eta)=r$ for distinct $\xi,\eta\in S$. Let $\alpha=\max(r)+1<\delta$. Then $\{p_\xi\restriction\alpha : \xi\in S\}$ is an antichain in $\mathbb{P}_\alpha$ of size $\aleph_1$ — because $p_\xi,p_\eta$ are incompatible only through coordinates in the root, the rest having disjoint supports and hence being freely amalgamable. This contradicts the inductive hypothesis that $\mathbb{P}_\alpha$ is ccc. Note where the argument dies: it uses **finiteness** of supports to get a bounded root.

**Divergence of ccc at a countable-support limit.** Start in $V\models 2^{\aleph_0}=\aleph_2$, and let $\mathbb{P}_{\omega_1}$ be the *countable support* iteration of Cohen forcing $\mathbb{C}=2^{<\omega}$, length $\omega_1$. Each iterand is ccc (indeed countable). But a countable support iteration of length $\omega_1$ of nontrivial real-adding forcings collapses $\mathfrak{c}$ to $\aleph_1$: for a condition $p$ at a limit $\gamma$ of uncountable cofinality one may prescribe behaviour on a countable set of coordinates simultaneously, and a fusion along $\omega_1$ yields a surjection $\omega_1\to(2^\omega)^V$ built from the generic reals $\langle c_\alpha:\alpha<\omega_1\rangle$. So $\mathbb{P}_{\omega_1}$ collapses $\aleph_2^V$ and is not ccc. Hence:
$$\text{ccc is FS-convergent, but not CS-convergent.}$$

**Why this is the whole problem in miniature.** Two supports, one class, opposite answers. The known theory consists of exactly four matched pairs $(\Gamma,\mathcal{S})$. For $\Gamma=\mathrm{SSP}$ no matching $\mathcal{S}$ is known, and FMS's workaround is to *first* force enough (a supercompact-based iteration) that $\mathrm{SSP}$ collapses onto semiproper, where RCS applies. A direct SSP convergence theorem would remove the large cardinal from the middle of the argument — and, by the above table, would be the fifth such pair discovered in fifty-five years.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*