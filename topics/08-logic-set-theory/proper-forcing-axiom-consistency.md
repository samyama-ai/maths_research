---
id: 08-logic-set-theory/proper-forcing-axiom-consistency
title: "Proper Forcing Axiom Consistency"
topic: 08-logic-set-theory
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Proper Forcing Axiom Consistency

> **Topic:** Mathematical Logic & Set Theory · **ID:** `08-logic-set-theory/proper-forcing-axiom-consistency` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

The Proper Forcing Axiom (PFA) is known to be consistent relative to a supercompact cardinal (Baumgartner, from Shelah's proper forcing iteration theory). No lower bound anywhere near that strength is known. The open problem:

> **Determine the exact consistency strength of PFA.** Specifically: is $\mathrm{Con}(\mathrm{ZFC} + \text{“there is a supercompact cardinal”})$ equivalent to $\mathrm{Con}(\mathrm{ZFC} + \mathrm{PFA})$?

A complete solution requires either
1. a **lower-bound** construction — a core-model-theoretic argument producing, from $\mathrm{ZFC}+\mathrm{PFA}$, an inner model with a supercompact cardinal (or whatever the true strength turns out to be); or
2. a **new upper bound** — a forcing construction producing a model of PFA from a hypothesis strictly weaker than supercompactness in consistency strength.

The folklore conjecture is that PFA is equiconsistent with a supercompact cardinal. It is the flagship open problem of the *inner model program*, since a lower bound of supercompact strength would require an inner model theory at the supercompact level, which does not yet exist.

## 2. Mathematical Foundations

**Properness.** For a poset $\mathbb{P}$ and a regular $\theta$ with $\mathbb{P}\in H_\theta$, let $N\prec (H_\theta,\in)$ be countable with $\mathbb{P}\in N$. A condition $q\in\mathbb{P}$ is *$(N,\mathbb{P})$-generic* if for every maximal antichain $A\in N$ of $\mathbb{P}$,
$$q \Vdash \dot G \cap A \cap N \neq \emptyset .$$
$\mathbb{P}$ is **proper** iff for club many countable $N\prec H_\theta$ and every $p\in \mathbb{P}\cap N$ there is $q\le p$ that is $(N,\mathbb{P})$-generic. Equivalently, $\mathbb{P}$ preserves stationarity of every stationary $S\subseteq[X]^{\omega}$. Properness implies preservation of $\omega_1$ and contains all ccc and all countably closed posets.

**PFA.** For every proper $\mathbb{P}$ and every family $\{D_\alpha : \alpha<\omega_1\}$ of dense subsets of $\mathbb{P}$ there is a filter $G\subseteq\mathbb{P}$ with $G\cap D_\alpha\neq\emptyset$ for all $\alpha<\omega_1$.

**Bounded PFA (BPFA).** The restriction to $\mathbb P$ proper and $|D_\alpha|\le\aleph_1$; equivalently (Bagaria) $\Sigma_1$-elementarity
$$H_{\aleph_2} \prec_{\Sigma_1} V^{\mathbb{P}} \text{'s } H_{\aleph_2}\quad\text{for all proper }\mathbb{P}.$$

**Supercompactness.** $\kappa$ is supercompact iff for every $\lambda\ge\kappa$ there is an elementary $j:V\to M$ with $\mathrm{crit}(j)=\kappa$, $j(\kappa)>\lambda$, and ${}^{\lambda}M\subseteq M$.

**Upper bound (Baumgartner).** If $\kappa$ is supercompact, let $f:\kappa\to V_\kappa$ be a Laver function. The countable-support iteration $\langle \mathbb{P}_\alpha,\dot{\mathbb{Q}}_\alpha : \alpha<\kappa\rangle$ with $\dot{\mathbb{Q}}_\alpha = f(\alpha)$ when $f(\alpha)$ is (forced to be) proper, and trivial otherwise, is proper by Shelah's iteration theorem, has the $\kappa$-cc, collapses $\kappa$ to $\omega_2$, and forces PFA.

**Square.** $\square_\kappa$: a sequence $\langle C_\alpha : \alpha\in\mathrm{Lim}\cap\kappa^+\rangle$ with $C_\alpha$ club in $\alpha$, $\mathrm{ot}(C_\alpha)\le\kappa$, and $C_\beta = C_\alpha\cap\beta$ for $\beta\in\mathrm{Lim}(C_\alpha)$.

**Consequences fixing the landscape.** PFA implies $2^{\aleph_0}=\aleph_2$ (Veličković; Todorcevic; and via Moore's Mapping Reflection Principle from BPFA), $\neg\square_\kappa$ for all uncountable $\kappa$ (Todorcevic), the Singular Cardinal Hypothesis (Viale), and $\mathrm{AD}^{L(\mathbb{R})}$ (Steel).

## 3. History & State of the Art (SOTA)

- **1978–1982.** Shelah isolates properness and proves the countable-support iteration theorem (*Proper Forcing*, Springer LNM 940, 1982). Baumgartner forces PFA from a supercompact.
- **1984.** Baumgartner's Handbook chapter collects the first wave of applications (all $\aleph_1$-dense sets of reals are isomorphic; every Aronszajn tree is special).
- **1988.** Foreman–Magidor–Shelah prove Martin's Maximum ($\mathrm{MM}$, the axiom for stationary-set-preserving posets) consistent from a supercompact — MM is the provably maximal such axiom and implies PFA.
- **1995.** Goldstern–Shelah pin BPFA exactly: equiconsistent with a *reflecting* ($\Sigma_2$-reflecting) cardinal — far below a Mahlo, and much weaker than PFA.
- **2005.** Steel: PFA implies $\mathrm{AD}^{L(\mathbb{R})}$, hence PFA has strength beyond $\omega$ Woodin cardinals, via core model induction.
- **2009.** Jensen–Schimmerling–Schindler–Steel ("Stacking mice") derive inner models with Woodin cardinals from BPFA-type hypotheses.
- **2011.** Viale–Weiss: any *forcing* proof of PFA of the Baumgartner type must use a supercompact — the upper bound is optimal *as a method*.
- **2014.** Neeman reproves PFA from a supercompact using finite side conditions (sequences of models of two types), giving a genuinely different iteration technology.
- **2021.** Asperó–Schindler: $\mathrm{MM}^{++}$ implies Woodin's $(*)$, tying the maximal forcing axiom to $\mathbb{P}_{\max}$ and $\mathrm{AD}^+$ machinery.

Current SOTA: **lower bound** $\approx$ "$\mathrm{AD}^{L(\mathbb{R})}$ plus much more" (core model induction, well below a Woodin limit of Woodins in the published record); **upper bound** = one supercompact. The gap is enormous.

## 4. Partial Results / Verified Cases

Exact strengths are known for fragments and for weakenings:

- **BPFA:** equiconsistent with a $\Sigma_2$-reflecting cardinal (Goldstern–Shelah 1995).
- **$\mathrm{BPFA}$ + "$\omega_1$ is not remarkable in $L$" / $\mathrm{BMM}$:** calibrated near remarkable cardinals (Schindler).
- **$\mathrm{MA}_{\aleph_1}$** (the ccc fragment): equiconsistent with ZFC — no large cardinal needed (Solovay–Tennenbaum 1971).
- **Poset-size fragments:** PFA restricted to proper posets of size $\aleph_1$, and hierarchies indexed by $\aleph_2$-linkedness or by $\Sigma^2_1$-absoluteness, are calibrated by Neeman–Schimmerling (*Hierarchies of forcing axioms I, II*, JSL 2008) at levels far below supercompact (around $\Sigma^2_1$-reflection / Woodin-type hypotheses).
- **PFA$^{++}$, MM, MM$^{++}$:** all forced from a supercompact; none separated from PFA in consistency strength.
- **Method-optimality (Viale–Weiss 2011):** if $\mathbb{P}$ is a proper poset of size $\kappa$ forcing PFA and collapsing $\kappa$ to $\omega_2$ in the standard way, then $\kappa$ is strongly compact; under the stronger internal-approachability hypotheses satisfied by all known iterations, $\kappa$ is supercompact. This is proved through $\mathrm{ISP}$ and *guessing models*: PFA implies $\mathrm{ISP}(\omega_2)$, i.e. stationarily many $M\in[H_\theta]^{\aleph_1}$ are $\aleph_1$-guessing.
- **Lower-bound consequences of PFA verified:** $\neg\square_\kappa$ all $\kappa\ge\omega_1$; SCH; $\mathrm{AD}^{L(\mathbb{R})}$; failure of covering for all current core models $K$ that have been constructed (i.e. every $K$ built so far is incompatible with PFA).

## 5. Principal Obstacles

- **No inner model theory at the supercompact level.** The core model induction derives $\mathrm{AD}^{L(\mathbb{R})}$ and beyond by contradiction against $K$-existence dichotomies. Constructing $K$ requires an *anti-large-cardinal hypothesis* (currently: no model with a Woodin limit of Woodins, or Jensen–Steel's "no $M_1^{\\#}$"-style thresholds). Above that, the comparison process — the engine of all fine structure — is not known to terminate: iteration trees at superstrong/supercompact levels lack a proven *iterability* theory. So the standard "contradiction with covering" route stalls.
- **Squares are exhausted as a tool.** PFA kills $\square_\kappa$ and even weak squares, which is exactly what forces $K$ to fail. But $\square$-failure only certifies strength up to the level where $\square$ is known to hold in canonical models — currently subcompact-cardinal-level (Schimmerling–Zeman). Beyond that, one has no combinatorial *witness* in $K$ to contradict.
- **The upper bound cannot be lowered by iteration.** Viale–Weiss shows any Baumgartner-style construction forces the ground-model cardinal to be strongly compact. Lowering the upper bound demands a fundamentally non-iterative construction (e.g. $\mathbb{P}_{\max}$-style or symmetric-extension methods), and no such construction is known to produce full PFA.
- **Reflection is $\aleph_2$-local, strength is global.** PFA's direct consequences all live in $H_{\aleph_2}$, whereas supercompactness is a statement about arbitrarily large $\lambda$. Guessing models bridge some of this ($\mathrm{ISP}$ is a genuine reflection at every $\lambda$), but $\mathrm{ISP}(\omega_2)$ alone is consistent from much less than a supercompact.

## 6. The Gap

Proven: $\mathrm{Con}(\text{supercompact}) \Rightarrow \mathrm{Con}(\mathrm{PFA}) \Rightarrow \mathrm{Con}(\mathrm{AD}^{L(\mathbb{R})} + \dots)$.

The gap is the region between "$\omega$ Woodins / $\mathrm{AD}^+$-level determinacy" and "one supercompact". Crossing it in the lower-bound direction requires exactly one missing ingredient: **a fine-structural inner model $K^{\text{sc}}$ with a supercompact cardinal, together with a covering/weak-covering lemma for it**, so that PFA's failure of covering can be converted into a supercompact. In the upper-bound direction the gap would close if one exhibited a model of PFA obtained from, say, a Woodin limit of Woodins — which would refute the equiconsistency conjecture and is regarded as unlikely but is not excluded.

## 7. Current Research (as of June 2026)

- **Woodin's Ultimate-$L$ program.** The $\mathrm{HOD}$ dichotomy and the $\Sigma_2$-definable "Ultimate-$L$" candidate aim to produce a canonical model with a supercompact; if $V=\text{Ultimate-}L$ is proved consistent with a supercompact and comes with covering, the PFA lower bound follows. *(frontier — verify)*
- **Hod mice and the Sargsyan school** (Sargsyan, Steel, Trang): core model induction past $\mathrm{AD}_{\mathbb{R}}+\Theta$-regular, pushing PFA's lower bound upward within the determinacy hierarchy. Recent work targets "$\mathrm{LSA}$-over-uB" as the next milestone. *(frontier — verify)*
- **Guessing models and $\mathrm{ISP}$** (Viale, Weiss, Krueger, Cox, Fuchino): identifying which PFA consequences are equivalent to supercompactness-flavoured reflection; $\mathrm{ISP}$, $\mathrm{GMP}$, and the "$\mathrm{SGM}$" hierarchies.
- **Neeman-style side conditions** (Neeman, Asperó–Mota, Veličković, Gilton, Krueger): finite/mixed side-condition iterations giving forcing axioms with the continuum $>\aleph_2$, and new fragments whose exact strength is computable.
- **$\mathbb{P}_{\max}$ and $(*)$** (Asperó–Schindler, Larson, Woodin): $\mathrm{MM}^{++}\Rightarrow(*)$ reframes maximality; whether $(*)$-style axioms can be leveraged to reduce upper bounds is under study.
- Institutions: UC Irvine (Neeman), Münster (Schindler), Torino (Viale), Berkeley/Rutgers (Steel, Sargsyan), Barcelona (Bagaria, Asperó/Mota network), UEA.

## 8. Future Work

- Prove weak covering for the current best candidate $K$ under "there is no inner model with a supercompact"; combine with PFA's $\square$-failure and $\mathrm{ISP}$ to get a supercompact.
- Extract a combinatorial principle from PFA that provably fails in *all* fine-structural models below supercompactness — a "$\square$ at the supercompact level" (candidates: variants of $\mathrm{ISP}$, or non-existence of $(\kappa,1)$-morasses-with-square).
- Separate PFA from MM in consistency strength, or prove they are equiconsistent (open).
- Determine the exact strength of PFA restricted to posets of size $\mathfrak{c}$, of $\mathrm{PFA}(\aleph_2\text{-cc})$, and of $\mathrm{ISP}(\omega_2)$ alone.
- Investigate whether a supercompact is *necessary* for MM$^{++}$ via the $(*)$-connection and $\mathrm{AD}^+$ inner models.

## 9. Key References

- **[Foundational]** Saharon Shelah. *Proper and Improper Forcing*, 2nd edition. Perspectives in Mathematical Logic, Springer, 1998. (1st ed.: *Proper Forcing*, LNM 940, 1982.)
- **[Foundational]** James E. Baumgartner. *Applications of the Proper Forcing Axiom.* In: Handbook of Set-Theoretic Topology (Kunen & Vaughan, eds.), North-Holland, 1984, 913–959.
- **[Foundational]** Matthew Foreman, Menachem Magidor, Saharon Shelah. *Martin's Maximum, saturated ideals, and non-regular ultrafilters. Part I.* Annals of Mathematics 127 (1988), 1–47.
- **[Foundational]** Stevo Todorcevic. *A note on the proper forcing axiom.* Contemporary Mathematics 31 (1984), 209–218.
- **[SOTA]** Matteo Viale, Christoph Weiss. *On the consistency strength of the proper forcing axiom.* Advances in Mathematics 228 (2011), 2672–2687.
- **[SOTA]** John R. Steel. *PFA implies $\mathrm{AD}^{L(\mathbb{R})}$.* Journal of Symbolic Logic 70 (2005), 1255–1296.
- **[SOTA]** Itay Neeman. *Forcing with sequences of models of two types.* Notre Dame Journal of Formal Logic 55 (2014), 265–298.
- **[SOTA]** David Asperó, Ralf Schindler. *Martin's Maximum$^{++}$ implies Woodin's Axiom $(*)$.* Annals of Mathematics 193 (2021), 793–835.
- **[SOTA]** Ronald Jensen, Ernest Schimmerling, Ralf Schindler, John Steel. *Stacking mice.* Journal of Symbolic Logic 74 (2009), 315–335.
- **[SOTA]** Martin Goldstern, Saharon Shelah. *The bounded proper forcing axiom.* Journal of Symbolic Logic 60 (1995), 58–73.
- **[SOTA]** Itay Neeman, Ernest Schimmerling. *Hierarchies of forcing axioms I;* Itay Neeman, *Hierarchies of forcing axioms II.* Journal of Symbolic Logic 73 (2008).
- **[SOTA]** Matteo Viale. *The proper forcing axiom and the singular cardinal hypothesis.* Journal of Symbolic Logic 71 (2006), 473–479.
- **[SOTA]** David Asperó, Miguel Angel Mota. *Forcing consequences of PFA together with the continuum large.* Transactions of the AMS 367 (2015), 6103–6129.
- **[Survey]** Justin Tatch Moore. *The proper forcing axiom.* Proceedings of the International Congress of Mathematicians, Hyderabad 2010, Vol. II, 3–29.
- **[Survey]** Boban Veličković. *Forcing axioms and stationary sets.* Advances in Mathematics 94 (1992), 256–284.
- **[Survey]** Justin Tatch Moore. *Set mapping reflection.* Journal of Mathematical Logic 5 (2005), 87–97.

## 10. Worked Example / Concrete Special Case

**Claim.** $\mathrm{PFA}\Rightarrow 0^{\\#}$ exists. This is the first rung of the lower-bound ladder, and it exhibits the exact argument pattern (kill $\square$, contradict covering) that stalls higher up.

*Step 1 (PFA side).* By Todorcevic's theorem, PFA implies $\neg\square_\kappa$ for every uncountable cardinal $\kappa$. Fix $\kappa=\aleph_\omega$.

*Step 2 (assume the negation).* Suppose $0^{\\#}$ does not exist. By Jensen's Covering Lemma, for every uncountable $X\subseteq \mathrm{Ord}$ there is $Y\in L$ with $X\subseteq Y$ and $|Y|=|X|$. Two consequences: every $V$-cardinal is an $L$-cardinal, and successor cardinals are computed correctly, so
$$(\aleph_\omega^+)^L = \aleph_{\omega+1}^V .$$

*Step 3 (inside $L$).* Jensen proved $L\models \square_\lambda$ for every $\lambda$. Let $\vec{C}=\langle C_\alpha : \alpha \in \mathrm{Lim}\cap(\aleph_\omega^+)^L\rangle \in L$ be a $\square_{\aleph_\omega}$-sequence there.

*Step 4 (transfer to $V$).* The index set is all of $\mathrm{Lim}\cap\aleph_{\omega+1}^V$ by Step 2. Each $C_\alpha$ is club in $\alpha$ — "club in $\alpha$" is absolute between $L$ and $V$ for a fixed $\alpha$ (unboundedness and closure are $\Delta_0$ in $C_\alpha,\alpha$). Coherence $C_\beta = C_\alpha\cap\beta$ for $\beta\in\mathrm{Lim}(C_\alpha)$ and $\mathrm{ot}(C_\alpha)\le\aleph_\omega$ are likewise absolute. So $\vec C$ witnesses $\square_{\aleph_\omega}$ in $V$.

*Step 5 (contradiction).* Steps 1 and 4 conflict. Hence $0^{\\#}$ exists. $\blacksquare$

**Where it breaks down.** Replace $L$ by the core model $K$ for a stronger mouse operator. Steps 2 and 3 both survive only while (i) $K$ can be constructed — which needs an anti-large-cardinal hypothesis such as "no inner model with a Woodin limit of Woodins" — and (ii) $K\models\square_\kappa$ — known through subcompact-level extenders (Schimmerling–Zeman). At the supercompact level neither holds: there is no $K$, and no $\square$-like witness. That single missing pair is the whole content of Section 6.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*