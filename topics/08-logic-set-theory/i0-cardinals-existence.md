---
id: 08-logic-set-theory/i0-cardinals-existence
title: "I0 Cardinals Existence"
topic: 08-logic-set-theory
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# I0 Cardinals Existence

> **Topic:** Mathematical Logic & Set Theory · **ID:** `08-logic-set-theory/i0-cardinals-existence` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

The axiom **I0** asserts:

> There exist an ordinal $\lambda$ and a nontrivial elementary embedding
> $$ j : L(V_{\lambda+1}) \longrightarrow L(V_{\lambda+1}) \quad\text{with}\quad \mathrm{crit}(j) < \lambda . $$

I0 is the strongest large-cardinal axiom in the standard hierarchy not known to be refutable from $\mathrm{ZFC}$. The open problem has two faces:

1. **Consistency.** Is $\mathrm{ZFC} + \mathrm{I0}$ consistent? By Gödel's second incompleteness theorem this cannot be proved in $\mathrm{ZFC}$, nor in $\mathrm{ZFC}+\mathrm{I0}$; the realistic question is whether a $\mathrm{ZFC}$ *refutation* exists — i.e. whether Kunen's inconsistency argument, or a new combinatorial obstruction, extends downward from $V_{\lambda+2}$ to $L(V_{\lambda+1})$.
2. **Structure.** Assuming I0, determine the theory of $L(V_{\lambda+1})$ in full — specifically, how far the analogy $L(V_{\lambda+1}) \leftrightarrow L(\mathbb{R})$ under $\mathrm{AD}$ (with $\lambda$ playing the role of $\omega$ and $\lambda^+$ of $\omega_1$) can be pushed.

A **resolution** would be either (a) a $\mathrm{ZFC}$ proof that no such $j$ exists, or (b) a proof that I0 is consistent relative to some axiom whose consistency is independently secured — which, given the reverse-mathematical picture, effectively means a proof in a stronger theory plus a coherent inner-model-theoretic account of why I0 is not refutable. Status is *partially-solved* because the exact upper boundary (Kunen's theorem) and a rich body of consequences of I0 are theorems, while consistency and the full theory of $L(V_{\lambda+1})$ are open.

## 2. Mathematical Foundations

Let $V_\alpha$ be the cumulative hierarchy. For a transitive class $M$, $j : M \to M$ is *elementary* if $M \models \varphi[a_1,\dots,a_n] \iff M \models \varphi[j(a_1),\dots,j(a_n)]$ for all first-order $\varphi$; *nontrivial* means $j \neq \mathrm{id}$, in which case there is a least ordinal moved, the **critical point** $\kappa = \mathrm{crit}(j)$.

**Critical sequence.** Set $\kappa_0 = \mathrm{crit}(j)$, $\kappa_{n+1} = j(\kappa_n)$, and $\lambda_j = \sup_n \kappa_n$. For all rank-into-rank axioms, $\lambda = \lambda_j$.

**The rank-into-rank hierarchy** (in decreasing strength; $\lambda$ is always $\lambda_j$):

$$
\begin{aligned}
\mathrm{I0}(\lambda) &: \ \exists j: L(V_{\lambda+1}) \to L(V_{\lambda+1}),\ \mathrm{crit}(j)<\lambda,\\
\mathrm{I1}(\lambda) &: \ \exists j: V_{\lambda+1} \to V_{\lambda+1},\\
\mathrm{I2}(\lambda) &: \ \exists j: V \to M \text{ with } V_\lambda \subseteq M,\ \lambda=\lambda_j,\\
\mathrm{I3}(\lambda) &: \ \exists j: V_{\lambda} \to V_{\lambda}.
\end{aligned}
$$

Equivalently, $\mathrm{I1}$ says $j:V_\lambda \to V_\lambda$ extends to $\Sigma^1_n$-elementarity on $V_{\lambda+1}$ for all $n$; $\mathrm{I3}$ is $\Sigma^1_0$-elementarity.

**Kunen's inconsistency (1971).** In $\mathrm{ZFC}$ there is no nontrivial elementary $j : V \to V$. The sharp local form: for every $\lambda$ there is no nontrivial elementary
$$ j : V_{\lambda+2} \longrightarrow V_{\lambda+2}. $$
So the entire hierarchy sits in the two-step window between $V_{\lambda+1}$ and $V_{\lambda+2}$, and $L(V_{\lambda+1}) \subseteq V_{\lambda+2}$ is the natural largest structure not directly hit.

**Why $\mathrm{AC}$ must fail inside.** I0 implies $L(V_{\lambda+1}) \models \mathrm{ZF} + \neg\mathrm{AC}$; indeed $V_{\lambda+1}$ has no well-ordering in $L(V_{\lambda+1})$, since one would let Kunen's argument run inside $L(V_{\lambda+1})$. This is exactly parallel to $L(\mathbb{R}) \models \mathrm{AD}$ under large cardinals.

**Woodin's structural theorems (from I0).** Writing $N = L(V_{\lambda+1})$ and $\Theta = \Theta^{L(V_{\lambda+1})}_{V_{\lambda+1}}$ (the sup of ordinals that are surjective images of $V_{\lambda+1}$ in $N$):
- $\lambda^+$ is measurable in $N$, and the club filter on $\lambda^+$ is an ultrafilter there;
- $N$ satisfies a coding/reflection theorem making $\Theta$ behave like $\Theta^{L(\mathbb{R})}$ under $\mathrm{AD}$;
- $\mathrm{I0}(\lambda)$ implies $\mathrm{I1}(\lambda)$, and moreover $\mathrm{I1}(\bar\lambda)$ holds for a stationary set of $\bar\lambda<\lambda$, so $\mathrm{Con}(\mathrm{I0}) \Rightarrow \mathrm{Con}(\mathrm{I1})$ strictly.

**Laver's algebra.** If $j,k : V_\lambda \to V_\lambda$ are elementary, so is the *application*
$$ j \cdot k \;=\; \bigcup_{\alpha<\lambda} j(k \restriction V_\alpha), $$
and $\cdot$ satisfies the **left-distributive law** $a\cdot(b\cdot c) = (a\cdot b)\cdot(a\cdot c)$.

## 3. History & State of the Art (SOTA)

- **1967–1970.** Reinhardt proposes $j: V \to V$ (the "Reinhardt cardinal"). Kunen (1971) refutes it in $\mathrm{ZFC}$ via an $\omega$-Jónsson-function argument using Erdős–Hajnal.
- **1978.** Solovay, Reinhardt and Kanamori codify I1–I3 in *Strong axioms of infinity and elementary embeddings*, fixing the modern naming.
- **1980.** Martin derives $\Pi^1_2$-determinacy from an iterable I3-type embedding — the first serious application.
- **1980s–1992.** Laver shows the free left-distributive algebra on one generator embeds into the algebra of elementary embeddings under $\cdot$ assuming I3, solving the word problem for LD-algebras; Dehornoy converts this into the (later choice-free) left-orderability of braid groups.
- **1993.** Dougherty and Dougherty–Jech analyse the finite **Laver tables** $A_n$ and show the growth of the relevant period function is not primitive recursive — Ackermannian.
- **1990s–2010s.** Woodin develops the $L(V_{\lambda+1})$/$L(\mathbb{R})$ analogy, and in *Suitable extender models I–II* (2010–2011) places I0 and its strengthenings ($\mathrm{I0}^\sharp$, the $E_\alpha$ and "Icarus" hierarchies) at the top of the Ultimate-$L$ program.
- **2012–2018.** Dimonte, Cramer, Shi and Wu produce the current SOTA: inverse-limit reflection, forcing technology preserving I1/I0, and degree-theoretic consequences. Dimonte's 2018 survey is the standard reference.
- **2019–2023.** Bagaria–Koellner–Woodin and Goldberg map the *choiceless* region above Kunen's bound ($\mathrm{ZF}$ + Reinhardt, Berkeley cardinals), and Schlutzenberg studies $\mathrm{ZF} + \exists j: V_{\lambda+2}\to V_{\lambda+2}$.

## 4. Partial Results / Verified Cases

- **Upper boundary is exact.** $j : V_{\lambda+2} \to V_{\lambda+2}$ is refuted in $\mathrm{ZFC}$ (Kunen). $j: V_{\lambda+1}\to V_{\lambda+1}$ is not. So the open region has width exactly one power set.
- **Strict hierarchy.** $\mathrm{I0} \Rightarrow \mathrm{I1} \Rightarrow \mathrm{I2} \Rightarrow \mathrm{I3}$, each with strictly larger consistency strength; each implies the existence of $n$-huge cardinals for all $n$ below $\lambda$.
- **Definable embeddings are impossible.** Suzuki (1999): no $j : V \to V$ is definable from parameters — so any witness to I0 must be a genuinely external class object.
- **$\mathrm{AC}$ fails in $L(V_{\lambda+1})$** under I0 (theorem, not conjecture), and $\lambda^+$ is measurable there (Woodin).
- **Reflection.** Cramer's inverse-limit reflection (2015) yields, from I0, a perfect-set-style dichotomy and generic-absoluteness results for subsets of $V_{\lambda+1}$ definable in $L(V_{\lambda+1})$ from parameters in $V_{\lambda+1}\cup\{V_{\lambda+1}\}$.
- **Forcing robustness.** Dimonte–Wu (2016) give a general iteration tool showing I1 (and variants of I0) can be forced to coexist with $\mathrm{GCH}$ failures at $\lambda$, e.g. $2^\lambda$ large while $\mathrm{I1}(\lambda)$ persists.
- **Combinatorial corollaries with no known $\mathrm{ZFC}$ proof.** From I3: the free one-generator LD-algebra is $\cong$ the algebra of embeddings; and the period of the first row of the Laver table $A_n$ tends to $\infty$. Both were theorems from I3 long before (and, for the LD word problem, superseded by) choice-free proofs.
- **Small-$n$ verification.** The Laver-table periods for $A_n$, $n=0,\dots,9$, are computed outright: $1,1,2,4,4,8,8,8,8,16$.

## 5. Principal Obstacles

- **Kunen's proof does not descend.** Kunen needs an $\omega$-Jónsson function $f : [\lambda]^\omega \to \lambda$, whose existence uses $\mathrm{AC}$ on $\lambda^\omega$, and needs $f \in \mathrm{dom}(j)$ — i.e. a set of rank $\lambda+2$. Inside $L(V_{\lambda+1})$, $\mathrm{AC}$ fails and no such $f$ is available. Every known refutation technique bottoms out at this single missing choice function.
- **No inner-model theory reaches here.** Fine-structural models exist only up to (roughly) finitely many Woodin cardinals plus a bit more; there is no comparison/iterability machinery at the level of superstrong, let alone rank-into-rank. Without a canonical model one cannot even state a plausible "$L$-like" consistency proof.
- **Nonlinearity of extenders.** Above a superstrong cardinal the extender embeddings are no longer "linearly iterable" in the usual sense; the critical sequence $\kappa_n$ makes the target $\lambda$ a limit of critical points, so ultrapower-by-$U$ arguments (Gabriel Goldberg's Ultrapower Axiom included) lose traction.
- **Second-order quantification.** I1 and I0 quantify over subsets of $V_\lambda$; reflection arguments that work for $\Sigma_n$-correctness break because $V_{\lambda+1}$ is not $\Sigma_1$-definable over any level below.
- **Choiceless analogues give no signal.** $\mathrm{ZF}$ + Reinhardt is not known inconsistent either, so the failure to refute I0 may reflect the weakness of our tools rather than truth.

## 6. The Gap

Proven: no elementary $j:V_{\lambda+2}\to V_{\lambda+2}$; and, granting I0, a substantial fragment of $\mathrm{Th}(L(V_{\lambda+1}))$.

Sought: a decision on $\exists j : L(V_{\lambda+1}) \to L(V_{\lambda+1})$.

The precise barrier is a **one-rank gap plus a choice gap**. A refutation must produce, inside $L(V_{\lambda+1})$ and without $\mathrm{AC}$, an object playing the role of Kunen's $\omega$-Jónsson function — equivalently, a definable "coding" of $[\lambda]^\omega$ into $\lambda$ that $j$ must respect. Woodin's structure theory says such coding *does* partially exist (e.g. $\Theta$-analysis, measurability of $\lambda^+$), which is why the problem is live: if the analogy with $\mathrm{AD}$ is exact, I0 is consistent; if the coding can be pushed one step further than the $\mathrm{AD}$ analogy allows, I0 dies. Nobody has an argument for which side wins.

## 7. Current Research (as of June 2026)

- **Ultimate-$L$ program (Woodin, Berkeley/Harvard-adjacent groups).** I0 and its strengthenings are the test cases for whether the $\mathrm{HOD}$ Dichotomy and suitable extender models survive at the top of the hierarchy. The key open technical statement remains whether I0 can hold in an Ultimate-$L$-like model. *(frontier — verify)*
- **$L(V_{\lambda+1})$ descriptive set theory (Cramer, Dimonte, Shi, Wu; Vienna/Udine, Beijing Normal, Rutgers lineage).** Extending perfect-set property, uniformization and Wadge-style hierarchy results from $L(\mathbb{R})$ under $\mathrm{AD}$ to $L(V_{\lambda+1})$ under I0.
- **Choiceless large cardinals (Bagaria, Koellner, Woodin, Goldberg, Schlutzenberg).** Goldberg's "even ordinals" technique (2023) sharpened where $\mathrm{ZF}$-only Kunen-type arguments fail; the hope is that a refinement reaches $L(V_{\lambda+1})$. *(frontier — verify)*
- **Forcing and preservation.** Continued development of Dimonte–Wu style iterations to separate I0 variants and to compute $\mathrm{Con}$-strength distinctions between $\mathrm{I0}(\lambda)$, $\mathrm{I0}^\sharp$, and Icarus-set axioms.
- **Algebraic shadows.** Ongoing work on Laver tables, LD-monoids and braid-group orderings continues to be the only place where rank-into-rank axioms have concrete finite-combinatorial consequences.

## 8. Future Work

- Build any fine-structural or "self-iterable" model at the level of a superstrong cardinal; without this, no consistency-flavoured evidence for I0 is obtainable.
- Complete the $\mathrm{AD}/L(V_{\lambda+1})$ dictionary: identify the exact analogue of the Solovay hierarchy and of $\mathrm{AD}^+$ for $L(V_{\lambda+1})$; a failure of the dictionary would be the first real evidence *against* I0.
- Determine whether the period function of Laver tables provably tends to $\infty$ in $\mathrm{PA}$ or $\mathrm{ZFC}$ alone — a genuinely finitary question whose only current proof uses I3.
- Push Kunen's argument into $\mathrm{ZF}$: characterize precisely which fragment of choice is needed, then test whether $L(V_{\lambda+1})$ satisfies it.
- Search for new consequences of I0 in "ordinary" mathematics (as Laver's work did), which would raise the stakes on consistency.

## 9. Key References

- **[Foundational]** Kenneth Kunen. *Elementary Embeddings and Infinitary Combinatorics.* The Journal of Symbolic Logic, 36(3), 407–413, 1971.
- **[Foundational]** Robert Solovay, William Reinhardt, Akihiro Kanamori. *Strong Axioms of Infinity and Elementary Embeddings.* Annals of Mathematical Logic, 13(1), 73–116, 1978.
- **[Foundational]** Richard Laver. *The Left Distributive Law and the Freeness of an Algebra of Elementary Embeddings.* Advances in Mathematics, 91(2), 209–231, 1992.
- **[Foundational]** Richard Laver. *Implications Between Strong Large Cardinal Axioms.* Annals of Pure and Applied Logic, 90(1–3), 79–90, 1997.
- **[Reference]** Akihiro Kanamori. *The Higher Infinite: Large Cardinals in Set Theory from Their Beginnings.* 2nd edition, Springer, 2003. (Chapter 24 covers I0–I3.)
- **[SOTA]** W. Hugh Woodin. *Suitable Extender Models I.* Journal of Mathematical Logic, 10(1–2), 101–339, 2010; *Suitable Extender Models II: Beyond $\omega$-huge.* Journal of Mathematical Logic, 11(2), 115–436, 2011.
- **[SOTA]** Scott S. Cramer. *Inverse Limit Reflection and the Structure of $L(V_{\lambda+1})$.* Journal of Mathematical Logic, 15(1), 2015.
- **[SOTA]** Vincenzo Dimonte, Liuzhen Wu. *A General Tool for Consistency Results Related to I1.* European Journal of Mathematics, 2(2), 474–492, 2016.
- **[SOTA]** Xianghui Shi. *Axiom I0 and Higher Degree Theory.* The Journal of Symbolic Logic, 80(3), 970–1021, 2015.
- **[Survey]** Vincenzo Dimonte. *I0 and Rank-into-Rank Axioms.* Bollettino dell'Unione Matematica Italiana, 11, 315–361, 2018.
- **[Recent]** Joan Bagaria, Peter Koellner, W. Hugh Woodin. *Large Cardinals Beyond Choice.* The Bulletin of Symbolic Logic, 25(3), 283–318, 2019.
- **[Recent]** Gabriel Goldberg. *Even Ordinals and the Kunen Inconsistency.* The Journal of Symbolic Logic, 2023.
- **[Related]** Akira Suzuki. *No Elementary Embedding from $V$ into $V$ is Definable from Parameters.* The Journal of Symbolic Logic, 64(4), 1591–1594, 1999.
- **[Related]** Randall Dougherty, Thomas Jech. *Finite Left-Distributive Algebras and Embedding Algebras.* Advances in Mathematics, 130(2), 201–241, 1997.

## 10. Worked Example / Concrete Special Case

**Laver tables: a finite shadow of I3.**

Fix $N=2^n$. The Laver table $A_n$ is the unique left-distributive operation on $\{1,\dots,N\}$ with $a * 1 = a+1 \pmod N$ (residue taken in $\{1,\dots,N\}$).

For $n=1$, $A_1$ on $\{1,2\}$:

$$
\begin{array}{c|cc}
* & 1 & 2\\\hline
1 & 2 & 2\\
2 & 1 & 2
\end{array}
$$

Row of $1$ is $(2,2)$: **period $1$**.

For $n=2$, $A_2$ on $\{1,2,3,4\}$:

$$
\begin{array}{c|cccc}
* & 1 & 2 & 3 & 4\\\hline
1 & 2 & 4 & 2 & 4\\
2 & 3 & 4 & 3 & 4\\
3 & 4 & 4 & 4 & 4\\
4 & 1 & 2 & 3 & 4
\end{array}
$$

Check left-distributivity on one triple: $1*(2*3) = 1*3 = 2$, while $(1*2)*(1*3) = 4*2 = 2$. ✓

Row of $1$ is $(2,4,2,4)$: **period $2$**.

Continuing, the period $p(n)$ of the first row of $A_n$ is
$$ p(0),\dots,p(9) = 1,1,2,4,4,8,8,8,8,16 . $$

**The connection to I0/I3.** Assume $\mathrm{I3}(\lambda)$ with witness $j$, and let $\mathcal{A}_j$ be the closure of $\{j\}$ under the application $k \cdot l = \bigcup_\alpha k(l\restriction V_\alpha)$. Laver proved $(\mathcal{A}_j,\cdot)$ is the free left-distributive algebra on one generator, and that the map "critical point modulo the $n$-th level of the critical sequence" sends $\mathcal{A}_j$ onto $A_n$. Since the $\kappa_i$ are strictly increasing and $j$ is nontrivial, no finite bound on the critical points survives, which forces

$$ \lim_{n\to\infty} p(n) = \infty . $$

That statement is about finite multiplication tables — completely arithmetic — yet **the only known proof passes through a rank-into-rank embedding**. Dougherty and Jech showed the first $n$ with $p(n)\ge 32$ exceeds an Ackermann-type tower, so brute-force verification is hopeless.

This is the problem in miniature: I3 (and above it I0) is not refutable by any technique we possess, it implies concrete finite facts we cannot otherwise prove, and the *only* known upper wall is Kunen's one-rank-higher inconsistency at $V_{\lambda+2}$.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*