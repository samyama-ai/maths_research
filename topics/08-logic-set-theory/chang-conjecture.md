---
id: 08-logic-set-theory/chang-conjecture
title: "Chang Conjecture"
topic: 08-logic-set-theory
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Chang Conjecture

> **Topic:** Mathematical Logic & Set Theory · **ID:** `08-logic-set-theory/chang-conjecture` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Chang's Conjecture (CC) is the two-cardinal transfer principle

$$(\aleph_2,\aleph_1)\twoheadrightarrow(\aleph_1,\aleph_0).$$

Explicitly: every structure $\mathfrak{A}=(A,U,\dots)$ in a countable first-order language, with $|A|=\aleph_2$ and a distinguished unary predicate $U\subseteq A$ with $|U|=\aleph_1$, has an elementary substructure $\mathfrak{B}\prec\mathfrak{A}$ with $|B|=\aleph_1$ and $|B\cap U|=\aleph_0$.

CC is not a theorem or refutation of ZFC. The settled part: CC is consistent relative to an $\omega_1$-Erdős cardinal, and *equiconsistent* with one. The open part is the pattern problem — which simultaneous families of instances $(\kappa^+,\kappa)\twoheadrightarrow(\mu^+,\mu)$ are consistent, and at what strength. The flagship open question (Foreman): is

$$(\aleph_3,\aleph_2)\twoheadrightarrow(\aleph_2,\aleph_1)\ \wedge\ (\aleph_2,\aleph_1)\twoheadrightarrow(\aleph_1,\aleph_0)$$

consistent with ZFC? A resolution is a forcing construction from a stated large-cardinal hypothesis, or a ZFC refutation (as Shelah gave for the $\aleph_\omega$ analogue).

## 2. Mathematical Foundations

**Two-cardinal notation.** For cardinals $\kappa>\lambda$, $\mu>\nu$, write $(\kappa,\lambda)\twoheadrightarrow(\mu,\nu)$ iff for every structure $\mathfrak{A}=(A,U,\dots)$ in a countable language with $|A|=\kappa$, $|U|=\lambda$, there is $\mathfrak{B}\prec\mathfrak{A}$ with $|B|=\mu$, $|B\cap U|=\nu$. A model with $|A|=\kappa,|U|=\lambda$ has **type** $(\kappa,\lambda)$.

**Skolem-hull reformulation.** By closing under Skolem functions, $(\aleph_2,\aleph_1)\twoheadrightarrow(\aleph_1,\aleph_0)$ is equivalent to: for every $F:[\omega_2]^{<\omega}\to\omega_2$ there is $X\subseteq\omega_2$ with
$$F\,[\,[X]^{<\omega}\,]\subseteq X,\qquad |X|=\aleph_1,\qquad |X\cap\omega_1|=\aleph_0 .$$
Equivalently, $\{X\in[\omega_2]^{\aleph_1} : |X\cap\omega_1|=\aleph_0\}$ is stationary in $[\omega_2]^{\aleph_1}$.

**Erdős cardinals.** $\kappa\to(\alpha)^{<\omega}$ means every $F:[\kappa]^{<\omega}\to 2$ has a set of order type $\alpha$ homogeneous for each $[\,\cdot\,]^n$ separately. $\kappa(\alpha)$ is the least such $\kappa$; $\kappa(\omega_1)$ is the **$\omega_1$-Erdős cardinal**. Already $\kappa(\omega_1)$ implies $0^\sharp$ exists, so it is incompatible with $V=L$.

**Generic-embedding form.** CC follows from the existence of an elementary embedding $j:V\to M$ in a generic extension with $\mathrm{crit}(j)=\omega_1^V$, $j(\omega_1^V)=\omega_2^V$ — the mechanism behind all known consistency proofs, via ideals on $[\omega_2]^{\aleph_1}$ or huge-cardinal Laver-style forcings.

**Weak Chang Conjecture (wCC).** $\forall f:[\omega_2]^{<\omega}\to\omega_2$, for stationarily many $\alpha<\omega_2$ of cofinality $\omega_1$ there are cofinally many $\beta<\omega_1$ with $\sup(\mathrm{cl}_f(X)\cap\omega_1)=\beta$ for some countable $X$ — a strictly weaker principle, strength $\approx$ an "accessible" Jónsson cardinal.

## 3. History & State of the Art (SOTA)

- **1960s, model theory.** Vaught's two-cardinal theorem: if a countable theory has a model of type $(\kappa^+,\kappa)$ for some infinite $\kappa$, it has one of type $(\aleph_1,\aleph_0)$. Chang (1965) proved, under GCH, $(\kappa^+,\kappa)\twoheadrightarrow(\lambda^+,\lambda)$ for $\lambda$ regular with $\lambda^{<\lambda}=\lambda$. The transfer *down to* $\lambda=\aleph_0$ escapes this method — $\aleph_0$ is regular but the hull must have uncountable size while meeting $\omega_1$ countably, so no closure argument applies. Chang asked whether the $\aleph_0$ case holds; it became "Chang's Conjecture".
- **1971 — Silver.** Con(ZFC $+\ \kappa(\omega_1)$ exists) $\Rightarrow$ Con(ZFC + CC + GCH), by Lévy-collapsing an $\omega_1$-Erdős cardinal to $\omega_2$ and using indiscernibles to build the required hulls.
- **1983 — Donder–Koepke.** Lower bounds via core-model theory: wCC implies an inner model with a suitable Jónsson/Erdős cardinal.
- **1988 — Foreman–Magidor–Shelah.** Martin's Maximum implies CC, placing it inside the standard forcing-axiom package.
- **1989 — Donder–Levinski.** CC is *equiconsistent* with an $\omega_1$-Erdős cardinal. This closes the original question.
- **1990 — Levinski–Magidor–Shelah.** Con($(\aleph_{\omega+1},\aleph_\omega)\twoheadrightarrow(\aleph_1,\aleph_0)$) from a huge cardinal — the singular-cardinal instance.
- **1994 — Shelah.** PCF theory refutes $(\aleph_{\omega+1},\aleph_\omega)\twoheadrightarrow(\aleph_{n+1},\aleph_n)$ in ZFC for $n\ge 1$: the first outright ZFC *failure* of a Chang-type transfer.
- **2009–2018 — Foreman; Eskew–Hayut.** Global and simultaneous patterns from huge-cardinal hierarchies, plus new ZFC restrictions on which patterns can coexist.

## 4. Partial Results / Verified Cases

| Instance | Status |
|---|---|
| $(\kappa^+,\kappa)\twoheadrightarrow(\lambda^+,\lambda)$, $\lambda$ regular, $\lambda^{<\lambda}=\lambda$ | **ZFC theorem under GCH** (Chang 1965) |
| $(\kappa^+,\kappa)\twoheadrightarrow(\aleph_1,\aleph_0)$ for *some* $\kappa$ | Vaught: transfer to type $(\aleph_1,\aleph_0)$ always available |
| $(\aleph_2,\aleph_1)\twoheadrightarrow(\aleph_1,\aleph_0)$ | **Equiconsistent with $\kappa(\omega_1)$** (Silver 1971; Donder–Levinski 1989); consistent with CH and with GCH; follows from MM |
| $(\aleph_{n+1},\aleph_n)\twoheadrightarrow(\aleph_1,\aleph_0)$, $n\ge 1$ | Consistent from large cardinals in the huge hierarchy |
| $(\aleph_{\omega+1},\aleph_\omega)\twoheadrightarrow(\aleph_1,\aleph_0)$ | Consistent from a huge cardinal (Levinski–Magidor–Shelah 1990) |
| $(\aleph_{\omega+1},\aleph_\omega)\twoheadrightarrow(\aleph_{n+1},\aleph_n)$, $n\ge1$ | **False in ZFC** (Shelah, *Cardinal Arithmetic*, 1994) |
| $(\aleph_3,\aleph_2)\twoheadrightarrow(\aleph_2,\aleph_1)$ alone | Consistent from huge-type hypotheses (Eskew–Hayut 2018) |
| Global CC: $(\kappa^+,\kappa)\twoheadrightarrow(\mu^+,\mu)$ for all regular $\kappa>\mu$ | Consistent from huge cardinals (Foreman 2009; Eskew–Hayut) |
| CC in $L$, or in any $L[E]$ below $0^\sharp$ | **Fails** (condensation; see §10) |
| $(\aleph_3,\aleph_2)\twoheadrightarrow(\aleph_2,\aleph_1)$ **and** $(\aleph_2,\aleph_1)\twoheadrightarrow(\aleph_1,\aleph_0)$ | **Open** |

## 5. Principal Obstacles

- **Non-transitivity of $\twoheadrightarrow$.** Chang transfers do not compose: $(\aleph_3,\aleph_2)\twoheadrightarrow(\aleph_2,\aleph_1)$ and $(\aleph_2,\aleph_1)\twoheadrightarrow(\aleph_1,\aleph_0)$ give no information about $(\aleph_3,\aleph_2)\twoheadrightarrow(\aleph_1,\aleph_0)$, and there is no known composition of hulls that preserves both size and trace conditions. Standard model-theoretic transfer (Vaught, Chang) is exactly a composition argument, so it stalls.
- **Forcings interfere.** Each instance is naturally forced by a Lévy-collapse or Laver-prepared huge-cardinal forcing that identifies a critical point with $\omega_1$ or $\omega_2$. Two instances demand two embeddings with *different* critical points into the same final model; the collapse producing one typically destroys the stationarity of the $[\,\cdot\,]$-set witnessing the other.
- **Core-model lower bounds saturate.** Donder–Koepke/Donder–Levinski technology computes strength up to Erdős-type cardinals by comparing indiscernibles. Beyond $0^\sharp$-level hypotheses, the inner-model program has no fine-structural models for huge cardinals, so the true consistency strength of the simultaneous patterns is not computable with present methods.
- **PCF gives failures, not successes.** Shelah's scales refute transfers at singulars of countable cofinality but say nothing about successors of regulars, where no canonical scale exists.
- **Square principles.** $\square_{\kappa}$-type coherent sequences are the standard tool for refuting compactness, but the known square-vs-CC implications are one-directional and do not decide the simultaneous case.

## 6. The Gap

Proven: each Chang instance in isolation, at a known or bounded strength; and one family of ZFC refutations at $\aleph_\omega$. Not proven: any statement about *interaction*. The precise missing step is a forcing (or ideal) construction that supports two generic elementary embeddings $j_1,j_2$ with $\mathrm{crit}(j_1)=\omega_1$, $j_1(\omega_1)=\omega_2$ and $\mathrm{crit}(j_2)=\omega_2$, $j_2(\omega_2)=\omega_3$ in a common extension — or a ZFC proof that the stationary sets $\{X\in[\omega_2]^{\aleph_1}:|X\cap\omega_1|=\aleph_0\}$ and $\{Y\in[\omega_3]^{\aleph_2}:|Y\cap\omega_2|=\aleph_1\}$ cannot both be stationary. No current technique produces or forbids the pair.

## 7. Current Research (as of June 2026)

- **Eskew–Hayut programme (Vienna, Jerusalem).** Systematic classification of consistent Chang patterns on successors of regulars and of singulars, using huge-cardinal Prikry- and Radin-style forcings together with ZFC constraints derived from PCF and from ideal-based reflection.
- **Ideal-theoretic route (Foreman school, UC Irvine).** Realizing Chang transfers as consequences of saturated or dense ideals on $[\lambda]^\kappa$; the "smoke and mirrors" framework shows small-cardinal combinatorics equiconsistent with huge cardinals, and is the standard vehicle for global CC.
- **Erdős-hierarchy strength calculus.** Sharpe–Welch's greatly Erdős cardinals give calibrated hypotheses between $\kappa(\omega_1)$ and measurables, used to pin strengths of strengthened CC variants (e.g. CC with additional stationary-reflection clauses).
- **Interaction with forcing axioms.** MM$^{++}$ and its $(*)$-relatives are being examined for which Chang instances they decide beyond the FMS result. *(frontier — verify)*
- **Higher-gap variants** $(\kappa^{+n},\kappa)\twoheadrightarrow(\mu^{+n},\mu)$ for $n\ge2$: partial consistency results announced from 2-huge cardinals. *(frontier — verify)*

## 8. Future Work

1. Settle the simultaneous $(\aleph_3,\aleph_2)\twoheadrightarrow(\aleph_2,\aleph_1)\wedge(\aleph_2,\aleph_1)\twoheadrightarrow(\aleph_1,\aleph_0)$ question — Foreman's stated priority.
2. Determine the exact consistency strength of $(\aleph_3,\aleph_2)\twoheadrightarrow(\aleph_2,\aleph_1)$; current upper bound (huge-type) and lower bound (well below huge) are far apart.
3. Extend PCF-style ZFC refutations from $\aleph_\omega$ to successors of regulars, or prove no such refutation exists.
4. Develop an inner-model theory for huge cardinals adequate to compute Chang-pattern strengths.
5. Classify which sets $S$ of pairs of cardinals admit $\{(\kappa,\lambda)\in S\}$ all holding simultaneously — the "global Chang spectrum".

## 9. Key References

- **[Foundational]** C. C. Chang. *A note on the two cardinal problem.* Proceedings of the American Mathematical Society 16 (1965), 1148–1155.
- **[Foundational]** R. L. Vaught. *The Löwenheim–Skolem theorem.* In: Logic, Methodology and Philosophy of Science (Proc. 1964 Int. Congress), North-Holland, 1965.
- **[Foundational]** J. Silver. *Some applications of model theory in set theory.* Annals of Mathematical Logic 3 (1971), 45–110.
- **[Foundational]** H.-D. Donder, J.-P. Levinski. *Some principles related to Chang's conjecture.* Annals of Pure and Applied Logic 45 (1989), 39–101.
- **[Foundational]** H.-D. Donder, P. Koepke. *On the consistency strength of "accessible" Jónsson cardinals and of the weak Chang conjecture.* Annals of Pure and Applied Logic 25 (1983), 233–261.
- **[SOTA]** J.-P. Levinski, M. Magidor, S. Shelah. *Chang's conjecture for $\aleph_\omega$.* Israel Journal of Mathematics 69 (1990), 161–172.
- **[SOTA]** M. Foreman, M. Magidor, S. Shelah. *Martin's Maximum, saturated ideals, and nonregular ultrafilters. Part I.* Annals of Mathematics 127 (1988), 1–47.
- **[SOTA]** S. Shelah. *Cardinal Arithmetic.* Oxford Logic Guides 29, Oxford University Press, 1994.
- **[SOTA / Recent]** M. Foreman. *Smoke and mirrors: combinatorial properties of small cardinals equiconsistent with huge cardinals.* Advances in Mathematics 222 (2009), 565–595.
- **[SOTA / Recent]** M. Eskew, Y. Hayut. *On the consistency of local and global versions of Chang's conjecture.* Transactions of the American Mathematical Society 370 (2018), 2879–2905.
- **[SOTA / Recent]** B. Sharpe, P. Welch. *Greatly Erdős cardinals with some generalizations to the Chang and Ramsey properties.* Annals of Pure and Applied Logic 162 (2011), 863–902.
- **[Survey]** M. Foreman. *Ideals and generic elementary embeddings.* In: Handbook of Set Theory (Foreman, Kanamori, eds.), Springer, 2010.
- **[Survey]** T. Jech. *Set Theory.* 3rd millennium edition, Springer, 2003 (Chapters 8, 33).

## 10. Worked Example / Concrete Special Case

**Claim.** If $V=L$ then CC fails.

Take $\mathfrak{A}=(L_{\omega_2},\in,\omega_1)$, with $U=\omega_1$. Then $|L_{\omega_2}|=\aleph_2$ and $|U|=\aleph_1$, so $\mathfrak{A}$ is a legitimate structure of type $(\aleph_2,\aleph_1)$. In $L$, $\omega_1=\omega_1^L$ and every set in $L_{\omega_2}$ has $L$-cardinality $\le\aleph_1$, so
$$\mathfrak{A}\models\text{"}\omega_1\text{ is the largest cardinal"}.$$

Suppose CC held and gave $X\prec\mathfrak{A}$ with $|X|=\aleph_1$ and $|X\cap\omega_1|=\aleph_0$. Let $\pi:X\cong L_\gamma$ be the transitive collapse (condensation applies since $X\prec L_{\omega_2}$ and $L_{\omega_2}\models\mathrm{ZF}^-$). Put $\bar\omega_1:=\pi(\omega_1)=\mathrm{ot}(X\cap\omega_1)$, a **countable** ordinal, since $X\cap\omega_1$ is countable.

Elementarity transfers the sentence:
$$L_\gamma\models\text{"}\bar\omega_1\text{ is the largest cardinal"}.$$
Hence for every $a\in L_\gamma$ there is, inside $L_\gamma$, an injection $a\hookrightarrow\bar\omega_1$. Since $L_\gamma=\bigcup_{\xi<\gamma}L_\xi$ and each level is covered, a standard Gödel-pairing surjection $\bar\omega_1\times\bar\omega_1\to\bar\omega_1$ yields a surjection $\bar\omega_1\to\gamma$ in $L_{\gamma+1}$. Computing cardinality in $V$:
$$|L_\gamma|\ \le\ |\bar\omega_1|\cdot\aleph_0\ =\ \aleph_0 .$$

But $\pi$ is a bijection $X\to L_\gamma$, so $|L_\gamma|=|X|=\aleph_1$. Contradiction: $\aleph_1\le\aleph_0$.

So no such $X$ exists and CC fails in $L$. The same argument runs in any fine-structural $L[E]$ with condensation, which is why CC requires $0^\sharp$ — and, sharpened by Donder–Levinski, exactly an $\omega_1$-Erdős cardinal. Note where the argument breaks under an $\omega_1$-Erdős cardinal: with $0^\sharp$ present, $L_{\omega_2}$ has $\omega_1$ Silver indiscernibles, and a hull generated by an uncountable set of indiscernibles below $\omega_2$ can have size $\aleph_1$ while its intersection with $\omega_1$ stays countable — the collapse is no longer countable because $\gamma$ is no longer $\bar\omega_1$-definable.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*