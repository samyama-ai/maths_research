---
id: 08-logic-set-theory/i1-cardinals-existence
title: "I1 Cardinals Existence"
topic: 08-logic-set-theory
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# I1 Cardinals Existence

> **Topic:** Mathematical Logic & Set Theory · **ID:** `08-logic-set-theory/i1-cardinals-existence` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

The axiom **I1** asserts:

$$\exists \lambda \ \exists j \ \big( j : V_{\lambda+1} \prec V_{\lambda+1},\ j \neq \mathrm{id} \big).$$

Here $V_\alpha$ is the $\alpha$-th level of the cumulative hierarchy and $j$ is elementary for the full first-order language of $\langle V_{\lambda+1}, \in\rangle$. A cardinal $\lambda$ witnessing this is an **I1 cardinal**.

The problem has three parts, only the third being genuinely open in the usual sense:

1. **Is I1 consistent with ZFC?** No proof of $\mathrm{Con}(\mathrm{ZFC}) \Rightarrow \mathrm{Con}(\mathrm{ZFC} + \mathrm{I1})$ is possible (Gödel), so the operative question is whether a contradiction can be derived. None is known after 55 years.
2. **Where does I1 sit?** Locate I1 exactly in the consistency-strength order between I2, I3 below and I0 above, and against Kunen's inconsistency ceiling. *Largely settled* — see §4.
3. **How far can the Kunen barrier be pushed?** Kunen (1971) refuted $j : V_{\lambda+2} \prec V_{\lambda+2}$ **using AC**. Whether ZF alone refutes it is open, and is the sharpest formulation of "how close to inconsistency is I1?"

A complete resolution would be either (a) a ZFC-proof of $\neg\mathrm{I1}$ — which would collapse the top of the large-cardinal hierarchy — or (b) an inner-model / fine-structural analysis certifying I1 as a coherent, canonically-analysable axiom in the way $L[\mu]$ certifies measurability.

## 2. Mathematical Foundations

**Elementary embedding.** $j : M \prec N$ means $M \models \varphi(a_1,\dots,a_n) \iff N \models \varphi(j a_1,\dots,j a_n)$ for all formulas $\varphi$. Nontrivial $j$ has a **critical point** $\mathrm{crit}(j) = \min\{\alpha : j(\alpha) > \alpha\}$.

**Critical sequence.** Given $\kappa_0 = \mathrm{crit}(j)$, set $\kappa_{n+1} = j(\kappa_n)$ and
$$\lambda_j := \sup_{n<\omega} \kappa_n .$$
For $j : V_\lambda \prec V_\lambda$ one always has $\lambda = \lambda_j$, hence $\mathrm{cf}(\lambda) = \omega$ and $\lambda$ is a strong limit fixed point of the $\beth$-function.

**The rank-into-rank hierarchy** (Kanamori, *The Higher Infinite*, §24), in decreasing consistency strength:

- **I0($\lambda$)**: $\exists\, j : L(V_{\lambda+1}) \prec L(V_{\lambda+1})$ with $\mathrm{crit}(j) < \lambda$.
- **I1($\lambda$)**: $\exists\, j : V_{\lambda+1} \prec V_{\lambda+1}$, $j\neq\mathrm{id}$. Equivalently, $\exists\, j: V_\lambda \prec V_\lambda$ which is $\Sigma^1_n$-elementary for every $n<\omega$.
- **I2($\lambda$)**: $\exists\, j : V \prec M$ with $V_\lambda \subseteq M$ and $\lambda = \lambda_j$.
- **I3($\lambda$)**: $\exists\, j : V_\lambda \prec V_\lambda$, $j \neq \mathrm{id}$ (first-order elementarity only; $= \Sigma^1_0$).

Since $V_{\lambda+1} = \mathcal{P}(V_\lambda)$, elementarity at level $\lambda+1$ is second-order over $V_\lambda$; this gives the **$E_n$-hierarchy**: $j \in E_n$ iff $j : V_\lambda \prec_{\Sigma^1_n} V_\lambda$, with
$$\mathrm{I3} = E_0 \supsetneq E_1 \supsetneq E_2 \supsetneq \cdots, \qquad \mathrm{I1} = \bigcap_{n<\omega} E_n .$$

**Kunen's Theorem (ZFC, 1971).** There is no nontrivial $j : V \prec V$. Equivalently, there is no $j : V_{\lambda+2} \prec V_{\lambda+2}$ for $\lambda = \lambda_j$. The proof: fix $\lambda = \lambda_j$; by Erdős–Hajnal there is an $\omega$-Jónsson function $f : [\lambda]^\omega \to \lambda$, i.e.
$$\forall X \in [\lambda]^{\lambda} \quad f\,''[X]^\omega = \lambda .$$
$f \in V_{\lambda+1}$, and applying $j$ to $f$ against the club $C = \{\alpha<\lambda : j''\alpha \subseteq \alpha\}$ and the set $j''\lambda \in V_{\lambda+2}$ yields a contradiction. Existence of $\omega$-Jónsson functions uses AC.

**Embedding algebra.** $\mathcal{E}_\lambda = \{ j : V_\lambda \prec V_\lambda \}$ carries the **application** operation
$$ j \cdot k \;=\; \bigcup_{\alpha<\lambda} j(k \cap V_\alpha), $$
which satisfies the **left-distributive law**
$$ j\cdot(k\cdot l) = (j\cdot k)\cdot(j\cdot l). $$

## 3. History & State of the Art (SOTA)

- **1971** — Kunen proves no $j : V \prec V$ (JSL 36), fixing the ceiling. Reinhardt's proposal of $j:V\prec V$ dies; the rank-into-rank axioms are the surviving remnant.
- **1970s–80s** — Gaifman, Solovay, Reinhardt, Kanamori isolate I0–I3 and prove the strength ordering; Martin uses $I1$-type hypotheses for $\Pi^1_2$ determinacy (superseded by Woodin cardinals).
- **1989–1992** — Laver proves that if I3 holds, the free left-distributive algebra on one generator embeds into $\mathcal{E}_\lambda$, and the word problem for one-generator LD-algebras is decidable (*Adv. Math.* 91, 1992). Dehornoy later removed the large-cardinal hypothesis via braid groups — the first case where an I3-proof was replaced by a ZFC-proof.
- **1993–1997** — Dougherty and Jech analyse **Laver tables** $A_{2^n}$; growth of the first-row period is Ackermannian.
- **1997** — Laver, *Implications between strong large cardinal axioms* (APAL 90): $E_{n+1} \subsetneq E_n$ is strict in consistency strength; $\mathrm{I1} \Rightarrow \mathrm{Con}(E_n)$ for all $n$.
- **2000s–2010s** — Woodin isolates **I0** and shows $L(V_{\lambda+1})$ under I0 mirrors $L(\mathbb{R})$ under AD: $\lambda^+$ is measurable in $L(V_{\lambda+1})$, coding/perfect-set/Baire-property analogues hold.
- **2015** — Cramer's *inverse limit reflection* gives a structure theory for $L(V_{\lambda+1})$ (*J. Math. Log.* 15). Shi develops higher degree theory under I0 (*JSL* 80, 2015).
- **2018** — Dimonte's survey *I0 and rank-into-rank axioms* consolidates the field.
- **2020s** — Schlutzenberg and Goldberg attack the choiceless frontier: how much of Kunen's argument survives without AC.

**Current SOTA:** I1 is consistent relative to I0, refuted at $V_{\lambda+2}$ under AC, and not refuted anywhere in ZFC. No inner model for I3 or above exists.

## 4. Partial Results / Verified Cases

Concrete, established facts:

- **Strict hierarchy, indexed by $n$.** For each $n<\omega$, $\mathrm{Con}(\mathrm{ZFC}+E_{n+1}) \Rightarrow \mathrm{Con}(\mathrm{ZFC}+E_n)$ and not conversely (Laver 1997). So the I3–I1 gap contains an $\omega$-chain of strictly increasing strengths, and $\mathrm{I1} \Rightarrow \mathrm{Con}(\mathrm{I2}) \Rightarrow \mathrm{Con}(\mathrm{I3})$.
- **Ceiling verified at level $\lambda+2$.** ZFC proves $\neg\exists j : V_{\lambda+2}\prec V_{\lambda+2}$; also $\neg\exists j:V\prec M$ with $\lambda^+{}$-sequences of $M$ ($\,{}^{\lambda}M \subseteq M$ for $\lambda = \lambda_j$).
- **Structural consequences of I1 at $\lambda$.** $\kappa_0$ is $\lambda$-supercompact-like: each $\kappa_n$ is measurable, $\lambda$-strong, and there are $\kappa_0$-complete normal measures on $V_\lambda$; $\lambda$ is a limit of measurables of Mitchell order $\geq \lambda$.
- **Combinatorial extraction.** From I3 one gets: (i) the LD word problem is decidable; (ii) Laver-table periods $\mathrm{per}(n) \to \infty$. Item (i) was later re-proved in ZFC (Dehornoy); item (ii) is **still only known from I3**.
- **Small-parameter computations.** Laver tables $A_{2^n}$ are explicitly computed for $n \le 48$; the first-row period takes values $1,1,2,4,4,8,8,8,8,16,\dots$, and remains $16$ throughout the computed range.
- **Generic/choiceless variants.** I0-style embeddings have been forced to hold at $\aleph_\omega$ in generic extensions (Dimonte–Shi), showing the axioms are compatible with small-cardinal combinatorics after collapse.

## 5. Principal Obstacles

- **No inner model theory.** Every large cardinal certified as "safe" — measurable, strong, Woodin — has a canonical inner model with fine structure and a comparison theory. Iteration trees and the current descriptive-inner-model machinery break down well below a supercompact; rank-into-rank is far above. Without an $L$-like model for I3, there is no way to check coherence internally.
- **The Kunen argument is AC-driven and saturated.** Kunen's contradiction needs an $\omega$-Jónsson function $f:[\lambda]^\omega\to\lambda$, whose existence is a theorem of AC (Erdős–Hajnal). Every known refutation at $V_{\lambda+2}$ routes through some choice-based coding of $j''\lambda$. Level $\lambda+1$ simply does not contain enough sets to carry out the coding: $j''\lambda \notin V_{\lambda+1}$ because $j''\lambda$ is a *subset of $\lambda$* only after coding, and the coding needs $\mathcal{P}(V_{\lambda+1})$.
- **Reflection cuts both ways.** I1 reflects downward strongly, so no ordinal-level counting argument distinguishes it from consistent axioms below. Any inconsistency proof must be "one level up", exactly where Kunen's method already stops.
- **Combinatorial statements are Ackermann-hard.** Dougherty showed the Laver-table statement "$\mathrm{per}(n)=32$ for some $n$" holds only for $n$ beyond $\mathrm{Ack}(9,\mathrm{Ack}(8,\mathrm{Ack}(8,254)))$, so numerical evidence for or against I3-derived consequences is unreachable by computation.

## 6. The Gap

Proven: no $j : V_{\lambda+2} \prec V_{\lambda+2}$ (ZFC). Asserted: $j : V_{\lambda+1} \prec V_{\lambda+1}$ exists. The gap is **exactly one level of the cumulative hierarchy** — a single application of the power set operation. Formally, all known refutations require a witness object living in $V_{\lambda+2}\setminus V_{\lambda+1}$ (a function $[\lambda]^\omega\to\lambda$ coded as a subset of $V_{\lambda+1}$). The precise open step:

> Produce a Kunen-style diagonalisation using only parameters from $V_{\lambda+1}$ — or prove that no such parameter exists, by exhibiting a model of $\mathrm{ZFC}+\mathrm{I1}$ relative to a weaker hypothesis or by an inner-model construction.

Secondarily: does **ZF alone** refute $j : V_{\lambda+2}\prec V_{\lambda+2}$? This is the choiceless half of the same one-level gap.

## 7. Current Research (as of June 2026)

- **Choiceless set theory (Schlutzenberg, Goldberg; Münster, Berkeley/Oxford).** Schlutzenberg has shown that $\mathrm{ZF} + \exists j:V_{\lambda+2}\prec V_{\lambda+2}$ is not refuted by the known arguments and analysed its consequences; Goldberg's *even ordinals* method derives Kunen-type contradictions from weak fragments of choice. *(frontier — verify)*
- **Structure of $L(V_{\lambda+1})$ under I0 (Dimonte, Cramer, Shi; Udine, NYU, Beijing Normal).** Transfer of AD-theoretic facts ($\Theta$-analysis, perfect set property, Wadge-type hierarchies) from $L(\mathbb{R})$ to $L(V_{\lambda+1})$, with I1 as the "$V_{\lambda+1}$ shadow" of the theory.
- **Generic embeddings at $\aleph_\omega$.** Forcing rank-into-rank-like embeddings onto small cardinals to obtain singular-cardinal combinatorics (failures of SCH, tree properties) from I0-strength hypotheses.
- **Very large cardinals and HOD.** Woodin's suitable extender models and the HOD Dichotomy give a program in which I1-type axioms would sit inside an ultimate $L$; whether such a model can hold an I1 embedding is a leading open test question. *(frontier — verify)*
- **Laver tables and LD-algebras (Dehornoy school, Paris).** Continued search for a ZFC proof that $\mathrm{per}(n)\to\infty$, which would remove the last purely-combinatorial dependence on I3.

## 8. Future Work

- Prove or refute $\mathrm{per}(n)\to\infty$ in ZFC (Dehornoy's stated challenge). A ZFC proof removes an I3 consequence; an independence proof strengthens the case that I3 has real arithmetic content.
- Settle the ZF status of $j:V_{\lambda+2}\prec V_{\lambda+2}$; a ZF refutation would show Kunen's ceiling is choice-free and sharpen the barrier.
- Extend inner-model theory past a supercompact — the prerequisite for any canonical model containing an I1 embedding.
- Develop a systematic "reverse mathematics of rank-into-rank": catalogue arithmetic ($\Pi^0_1$/$\Pi^0_2$) consequences of I1 not provable from I3, giving falsifiable numeric predictions.
- Determine whether $\mathrm{I1}(\lambda)$ can consistently hold at the *least* $\lambda$ of cofinality $\omega$ above a supercompact, clarifying interaction with $\mathrm{HOD}$.

## 9. Key References

- **[Foundational]** Kenneth Kunen. *Elementary embeddings and infinitary combinatorics.* Journal of Symbolic Logic 36(3), 407–413, 1971.
- **[Foundational]** Akihiro Kanamori. *The Higher Infinite: Large Cardinals in Set Theory from Their Beginnings.* Springer, 2nd ed., 2003. (Chapter 24: rank-into-rank axioms.)
- **[Foundational]** Richard Laver. *The left distributive law and the freeness of an algebra of elementary embeddings.* Advances in Mathematics 91(2), 209–231, 1992.
- **[SOTA]** Richard Laver. *Implications between strong large cardinal axioms.* Annals of Pure and Applied Logic 90(1–3), 79–90, 1997.
- **[SOTA]** Randall Dougherty and Thomas Jech. *Finite left-distributive algebras and embedding algebras.* Advances in Mathematics 130(2), 201–241, 1997.
- **[SOTA]** Scott Cramer. *Inverse limit reflection and the structure of $L(V_{\lambda+1})$.* Journal of Mathematical Logic 15(1), 2015.
- **[SOTA]** Xianghui Shi. *Axiom I0 and higher degree theory.* Journal of Symbolic Logic 80(3), 970–1021, 2015.
- **[SOTA]** W. Hugh Woodin. *Suitable extender models I.* Journal of Mathematical Logic 10(1–2), 101–339, 2010.
- **[Survey]** Vincenzo Dimonte. *I0 and rank-into-rank axioms.* Bollettino dell'Unione Matematica Italiana 11, 315–361, 2018.
- **[Survey]** Patrick Dehornoy. *Braids and Self-Distributivity.* Progress in Mathematics 192, Birkhäuser, 2000.

## 10. Worked Example / Concrete Special Case

**Laver tables from a single embedding.** Assume I3 at $\lambda$ with $j : V_\lambda \prec V_\lambda$, $\mathrm{crit}(j) = \kappa_0$. Let $\mathcal{A}_j$ be the closure of $\{j\}$ under $\cdot$. Laver proved $\mathcal{A}_j$ is the *free* left-distributive algebra on one generator. Its finite quotients are the **Laver tables** $A_{2^n}$ on $\{1,\dots,2^n\}$, defined by
$$ p \cdot 1 = p+1 \ (\mathrm{mod}\ 2^n), \qquad p\cdot(q+1) = (p\cdot q)\cdot(p+1). $$

Compute $A_4$ ($n=2$, elements $1,2,3,4$):

- $p\cdot 1$: $1\cdot1=2,\ 2\cdot1=3,\ 3\cdot1=4,\ 4\cdot1=4$ (since $4\equiv 0 \mapsto 4$).
- $1\cdot 2 = (1\cdot1)\cdot(1+1) = 2\cdot 2$. And $2\cdot2=(2\cdot1)\cdot3=3\cdot3$; $3\cdot3=(3\cdot2)\cdot4$ with $3\cdot2=(3\cdot1)\cdot4=4\cdot4=4$, so $3\cdot3=4\cdot4=4$. Hence $1\cdot 2 = 4$.
- Continuing: $1\cdot3=(1\cdot2)\cdot2=4\cdot2=4$, $1\cdot4=(1\cdot3)\cdot2=4$.

| $\cdot$ | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| **1** | 2 | 4 | 2 | 4 |
| **2** | 3 | 4 | 3 | 4 |
| **3** | 4 | 4 | 4 | 4 |
| **4** | 1 | 2 | 3 | 4 |

(Row 1 recomputed with the full recursion gives $2,4,2,4$ — period $2$.)

**The point.** The first row of $A_{2^n}$ is periodic with period $\mathrm{per}(n)$ a power of $2$: $\mathrm{per}(0..9) = 1,1,2,4,4,8,8,8,8,16$. Under I3, the critical points $\kappa_i$ of elements of $\mathcal{A}_j$ are cofinal in $\lambda$, which forces $\mathrm{per}(n)\to\infty$. In ZFC alone this is **unknown**. Dougherty's bound shows $\mathrm{per}(n)=32$ first occurs at some
$$ n > \mathrm{Ack}\big(9,\mathrm{Ack}(8,\mathrm{Ack}(8,254))\big), $$
so no computation can decide it. This is the cleanest concrete instance of the situation: a finite, fully explicit arithmetic statement about $4\times4$-style multiplication tables whose only known proof runs through the existence of $j : V_\lambda\prec V_\lambda$ — and I1 is the strengthening of that hypothesis to one further level, $V_{\lambda+1}$, right up against Kunen's wall at $V_{\lambda+2}$.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*