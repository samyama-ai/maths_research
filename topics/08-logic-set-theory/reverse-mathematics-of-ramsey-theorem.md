---
id: 08-logic-set-theory/reverse-mathematics-of-ramsey-theorem
title: "Reverse Mathematics of Ramsey Theorem"
topic: 08-logic-set-theory
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Reverse Mathematics of Ramsey's Theorem

> **Topic:** Mathematical Logic & Set Theory · **ID:** `08-logic-set-theory/reverse-mathematics-of-ramsey-theorem` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Reverse mathematics calibrates theorems by the set-existence axioms needed to prove them in subsystems of second-order arithmetic. For Ramsey's theorem the calibration is complete for exponent $n \ge 3$ and famously incomplete for $n = 2$.

**Main open problem.** Determine the exact first-order strength of $\mathsf{RT}^2_2$ — Ramsey's theorem for pairs and two colours — over $\mathsf{RCA}_0$. Concretely:

1. **(First-order part.)** Characterise $\mathrm{Th}_{\Pi^1_1}(\mathsf{RCA}_0 + \mathsf{RT}^2_2)$, i.e. the set of first-order (arithmetical) consequences of $\mathsf{RT}^2_2$. Is $\mathsf{RCA}_0 + \mathsf{RT}^2_2$ $\Pi^1_1$-conservative over $\mathsf{RCA}_0 + \mathsf{B}\Sigma^0_2$?
2. **(Conservation ceiling.)** $\mathsf{RT}^2_2$ is known to be $\Pi^0_3$-conservative over $\mathsf{I}\Sigma^0_1$. Is it $\Pi^0_4$-conservative? Where exactly does conservation fail?
3. **(Reducibility.)** Does $\mathsf{SRT}^2_2$ imply $\mathsf{RT}^2_2$ over $\mathsf{RCA}_0$ (i.e. in all models, not merely $\omega$-models)?

A complete solution to (1) means exhibiting a first-order theory $T$ in the language of arithmetic such that $\mathsf{RCA}_0 + \mathsf{RT}^2_2 \vdash \varphi \iff T \vdash \varphi$ for all arithmetical $\varphi$, with both directions proved.

## 2. Mathematical Foundations

Work in the language $L_2$ of second-order arithmetic. For $X \subseteq \mathbb{N}$ let $[X]^n = \{ \{x_1 < \dots < x_n\} : x_i \in X \}$. A **$k$-colouring** of $[\mathbb{N}]^n$ is $c : [\mathbb{N}]^n \to k$; a set $H$ is **homogeneous** for $c$ if $c$ is constant on $[H]^n$.

$$\mathsf{RT}^n_k :\quad \forall c : [\mathbb{N}]^n \to k \;\; \exists H \;(H \text{ infinite} \wedge |c([H]^n)| = 1).$$

$\mathsf{RT}^n_{<\infty} = \forall k\, \mathsf{RT}^n_k$; $\mathsf{RT} = \forall n\, \mathsf{RT}^n_{<\infty}$.

**Base theory.** $\mathsf{RCA}_0$: ordered semiring axioms, $\Sigma^0_1$ induction ($\mathsf{I}\Sigma^0_1$), and $\Delta^0_1$ comprehension. Its minimal $\omega$-model is the computable sets. Stronger systems: $\mathsf{WKL}_0$ (every infinite binary tree has a path), $\mathsf{ACA}_0$ (arithmetical comprehension, equivalent to "the Turing jump exists").

**Induction/bounding hierarchy.** For $n \ge 1$,
$$\mathsf{I}\Sigma^0_{n+1} \Rightarrow \mathsf{B}\Sigma^0_{n+1} \Rightarrow \mathsf{I}\Sigma^0_n,$$
both implications strict (Paris–Kirby). $\mathsf{B}\Sigma^0_2$ is the collection scheme
$$\forall x < a\,\exists y\, \varphi(x,y) \;\rightarrow\; \exists b\,\forall x < a\,\exists y < b\, \varphi(x,y), \qquad \varphi \in \Sigma^0_2 .$$

**Decomposition.** A colouring $c:[\mathbb{N}]^2 \to 2$ is **stable** if $\lim_y c(x,y)$ exists for every $x$. $\mathsf{SRT}^2_2$ is $\mathsf{RT}^2_2$ restricted to stable colourings. $\mathsf{COH}$ states that every sequence $\vec{R} = \langle R_i \rangle_{i\in\mathbb{N}}$ has an infinite **cohesive** set $C$: for each $i$, $C \subseteq^* R_i$ or $C \subseteq^* \overline{R_i}$. Cholak–Jockusch–Slaman:
$$\mathsf{RCA}_0 \vdash \mathsf{RT}^2_2 \leftrightarrow \mathsf{SRT}^2_2 + \mathsf{COH}.$$

**Anchor theorems.**
- $\mathsf{RCA}_0 \vdash \mathsf{RT}^n_k \leftrightarrow \mathsf{ACA}_0$ for all $n \ge 3$, $k \ge 2$ (Simpson, SOSOA III.7.6, from Jockusch 1972).
- $\mathsf{RCA}_0 \vdash \mathsf{RT} \rightarrow \mathsf{ACA}_0'$, and $\mathsf{ACA}_0^+ \vdash \mathsf{RT}$ (McAloon; Simpson III.7.9).
- $\mathsf{RCA}_0 \vdash \mathsf{RT}^1_{<\infty} \leftrightarrow \mathsf{B}\Sigma^0_2$ (Hirst 1987) — the infinite pigeonhole principle is exactly $\Sigma^0_2$-collection.
- Jockusch's bounds: every computable $c:[\mathbb{N}]^n\to 2$ has an infinite $\Pi^0_n$ homogeneous set, and some computable $c$ has no infinite $\Sigma^0_n$ one.

## 3. History & State of the Art (SOTA)

- **1930.** Ramsey proves $\mathsf{RT}$ in *On a problem of formal logic*.
- **1971–72.** Specker gives a computable $2$-colouring of pairs with no computable infinite homogeneous set; Jockusch systematises this, proving the $\Pi^0_n$ upper / $\Sigma^0_n$ lower bounds and the arithmetical strength for $n\ge 3$.
- **1987.** Hirst's thesis: $\mathsf{RT}^1_{<\infty} \equiv \mathsf{B}\Sigma^0_2$; $\mathsf{RT}^2_2 \rightarrow \mathsf{B}\Sigma^0_2$.
- **1995.** Seetapun–Slaman: $\mathsf{RCA}_0 + \mathsf{RT}^2_2 \nvdash \mathsf{ACA}_0$, by cone avoidance — for any non-computable $C$ and computable $c$, there is an infinite homogeneous $H$ with $C \not\le_T H$. This split $\mathsf{RT}^2_2$ off the "Big Five".
- **2001.** Cholak–Jockusch–Slaman: the $\mathsf{SRT}^2_2 + \mathsf{COH}$ decomposition, low$_2$ homogeneous sets, and $\Pi^1_1$-conservativity of $\mathsf{RT}^2_2$ over $\mathsf{RCA}_0 + \mathsf{I}\Sigma^0_2$.
- **2012–15.** Liu Jiayi: $\mathsf{RT}^2_2 \nvdash \mathsf{WKL}_0$, and $\mathsf{RT}^2_2 \nvdash \mathsf{DNR}$ — $\mathsf{RT}^2_2$ and $\mathsf{WKL}_0$ are incomparable.
- **2014, 2017.** Chong–Slaman–Yang: $\mathsf{SRT}^2_2 \nvdash \mathsf{COH}$ (in a non-standard model), and $\mathsf{RT}^2_2 \nvdash \mathsf{I}\Sigma^0_2$. The first-order part sits strictly between $\mathsf{B}\Sigma^0_2$ and $\mathsf{I}\Sigma^0_2$ — or equals $\mathsf{B}\Sigma^0_2$.
- **2018.** Patey–Yokoyama: $\mathsf{RT}^2_2$ is $\Pi^0_3$-conservative over $\mathsf{RCA}_0$; hence its provably total functions are exactly the primitive recursive ones and it has the same $\Sigma^0_1$ theorems as $\mathsf{I}\Sigma^0_1$.
- **2021.** Monin–Patey: $\mathsf{SRT}^2_2 \nvdash \mathsf{RT}^2_2$ over $\omega$-models, via a new "partition genericity" forcing.

## 4. Partial Results / Verified Cases

| Statement | Status over $\mathsf{RCA}_0$ |
|---|---|
| $\mathsf{RT}^n_k$, $n\ge 3$, $k\ge 2$ | **Solved:** $\equiv \mathsf{ACA}_0$ |
| $\mathsf{RT}^1_k$, $k$ fixed standard | **Solved:** provable in $\mathsf{RCA}_0$ |
| $\mathsf{RT}^1_{<\infty}$ | **Solved:** $\equiv \mathsf{B}\Sigma^0_2$ |
| $\mathsf{RT}^2_k$, $k \ge 2$ fixed | Equivalent to $\mathsf{RT}^2_2$; strength unknown |
| $\mathsf{COH}$ | **Solved:** $\Pi^1_1$-conservative over $\mathsf{RCA}_0$; strictly weaker than $\mathsf{RT}^2_2$ |
| $\mathsf{RT}^2_2$ vs $\mathsf{ACA}_0$, $\mathsf{WKL}_0$, $\mathsf{DNR}$ | **Solved (negative):** implies none of them |
| $\mathsf{RT}^2_2 \to \mathsf{B}\Sigma^0_2$ | **Solved (Hirst).** $\mathsf{RT}^2_2 \to \mathsf{I}\Sigma^0_2$: **refuted** (CSY 2017) |
| $\Pi^0_3$-conservation over $\mathsf{I}\Sigma^0_1$ | **Solved (Patey–Yokoyama 2018)** |
| $\Pi^1_1$-conservation over $\mathsf{I}\Sigma^0_2$ | **Solved (CJS 2001)** |
| Proof-theoretic ordinal | **Solved:** $\omega^\omega$, same as $\mathsf{I}\Sigma^0_1$ |
| Effective bound | **Solved:** every computable $c:[\mathbb{N}]^2\to2$ has an infinite low$_2$ homogeneous set (CJS) |

Also settled: the whole zoo below $\mathsf{RT}^2_2$ — $\mathsf{ADS}$, $\mathsf{CAC}$, $\mathsf{EM}$, $\mathsf{SADS}$, $\mathsf{RWKL}$ — has been separated into a largely complete lattice of implications (Hirschfeldt–Shore; Lerman–Solomon–Towsner; Patey).

## 5. Principal Obstacles

- **Computability-theoretic methods only see $\omega$-models.** Cone avoidance, low$_2$ constructions, and preservation properties give $\omega$-model separations. The remaining open questions are first-order: they live in models with non-standard integers, where the effective machinery does not directly apply.
- **Non-standard model constructions are extremely delicate.** The CSY proofs use models of $\mathsf{B}\Sigma^0_2 + \neg\mathsf{I}\Sigma^0_2$ where the "$\Sigma^0_2$-approximation" of a $\Delta^0_2$ set changes cofinally often; the standard limit-lemma reasoning behind $\mathsf{SRT}^2_2 \leftrightarrow \mathsf{D}^2_2$ becomes unstable, and priority arguments require inductive strength the model lacks.
- **Induction and set existence are entangled.** Each iteration of a Ramsey-type construction costs induction; bounding the number of iterations needs $\mathsf{B}\Sigma^0_2$, which is itself a consequence of $\mathsf{RT}^2_2$. Any proof of conservation must simultaneously control both, which is why Patey–Yokoyama had to combine forcing with an indicator/proof-size argument rather than pure recursion theory.
- **No known combinatorial statement is a candidate for the first-order part.** Unlike $\mathsf{WKL}_0$ (conservative over $\mathsf{I}\Sigma^0_1$ by Harrington) there is no clean model-theoretic "closure under low sets" argument for $\mathsf{RT}^2_2$: it is not $\Pi^1_1$-conservative over $\mathsf{RCA}_0$ (it proves $\mathsf{B}\Sigma^0_2$), so the target theory must be pinned down from above and below.

## 6. The Gap

Let $T_1 = \mathsf{RCA}_0 + \mathsf{B}\Sigma^0_2$ and $T_2 = \mathsf{RCA}_0 + \mathsf{I}\Sigma^0_2$. Known:
$$T_1 \subseteq \mathrm{Th}_{\Pi^1_1}(\mathsf{RCA}_0 + \mathsf{RT}^2_2) \subsetneq T_2 .$$
The left inclusion is Hirst; the right non-inclusion is Chong–Slaman–Yang 2017. **The gap is whether the left inclusion is an equality.** Patey–Yokoyama close the gap for $\Pi^0_3$ sentences (equality there). So the open region is exactly $\Pi^0_4$ and higher, together with $\Sigma^0_2$-statements about arbitrary sets. Crossing it requires either (a) a model construction turning any model of $\mathsf{B}\Sigma^0_2$ into one of $\mathsf{RT}^2_2$ with the same first-order part, or (b) a specific $\Pi^0_4$ (or $\Pi^1_1$) sentence provable from $\mathsf{RT}^2_2$ but not from $\mathsf{B}\Sigma^0_2$.

## 7. Current Research (as of June 2026)

- **Proof-size and conservation.** Kołodziejczyk–Wong–Yokoyama analyse how $\mathsf{RT}^2_2$ proofs of collection blow up, giving quantitative limits on conservation and evidence about the $\Pi^0_4$ frontier. *(frontier — verify)* Several 2023–2025 preprints claim sharper characterisations of the first-order part in terms of a "$\Sigma^0_2$-approximation" scheme strictly between $\mathsf{B}\Sigma^0_2$ and $\mathsf{I}\Sigma^0_2$. *(frontier — verify)*
- **Forcing with partition genericity.** Monin and Patey (Créteil / CNRS–Lyon) extend the technique used for $\mathsf{SRT}^2_2 \nvdash_\omega \mathsf{RT}^2_2$ to pigeonhole-type basis theorems, aiming at the non-$\omega$-model version.
- **Non-standard models.** Chong, Slaman, Yang, Wong (NUS, Berkeley) continue the $\alpha$-largeness/indicator programme for $\mathsf{B}\Sigma^0_2$ models.
- **Higher exponents with weak colour bounds.** Free-set, thin-set, and rainbow Ramsey analogues ($\mathsf{FS}^n$, $\mathsf{TS}^n$, $\mathsf{RRT}^n_k$) at $n \ge 3$ remain open in strength; Cholak–Patey and Dzhafarov–Patey are active here.
- **Formalisation.** Partial Lean/Isabelle formalisations of $\mathsf{RT}^n_k \equiv \mathsf{ACA}_0$ for $n\ge3$. *(frontier — verify)*

## 8. Future Work

- Build a model of $\mathsf{B}\Sigma^0_2 + \mathsf{RT}^2_2$ over an arbitrary countable model of $\mathsf{B}\Sigma^0_2$ — the direct route to $\Pi^1_1$-conservation.
- Push Patey–Yokoyama's indicator/forcing hybrid from $\Pi^0_3$ to $\Pi^0_4$, or find the counterexample sentence.
- Settle $\mathsf{SRT}^2_2 \to \mathsf{RT}^2_2$ over $\mathsf{RCA}_0$ (only the $\omega$-model case is done).
- Determine whether $\mathsf{RT}^2_2$'s first-order part is finitely axiomatisable over $\mathsf{I}\Sigma^0_1$.
- Extend the analysis to $\mathsf{RT}^2_{<\infty}$ with non-standard $k$, and to Ramsey theorems on trees and for $\mathbb{Q}$.

## 9. Key References

- **[Foundational]** F. P. Ramsey. *On a problem of formal logic.* Proc. London Math. Soc. (2) 30, 264–286, 1930.
- **[Foundational]** C. G. Jockusch. *Ramsey's theorem and recursion theory.* Journal of Symbolic Logic 37, 268–280, 1972.
- **[Foundational]** J. L. Hirst. *Combinatorics in Subsystems of Second Order Arithmetic.* Ph.D. thesis, Pennsylvania State University, 1987.
- **[Foundational]** D. Seetapun, T. A. Slaman. *On the strength of Ramsey's theorem.* Notre Dame Journal of Formal Logic 36(4), 570–582, 1995.
- **[Foundational]** P. A. Cholak, C. G. Jockusch, T. A. Slaman. *On the strength of Ramsey's theorem for pairs.* Journal of Symbolic Logic 66(1), 1–55, 2001.
- **[SOTA]** J. Liu. *$\mathsf{RT}^2_2$ does not imply $\mathsf{WKL}_0$.* Journal of Symbolic Logic 77(2), 609–620, 2012.
- **[SOTA]** J. Liu. *Cone avoiding closed sets.* Transactions of the AMS 367, 1609–1630, 2015.
- **[SOTA]** C. T. Chong, T. A. Slaman, Y. Yang. *The metamathematics of stable Ramsey's theorem for pairs.* Journal of the AMS 27(3), 863–892, 2014.
- **[SOTA]** C. T. Chong, T. A. Slaman, Y. Yang. *The inductive strength of Ramsey's theorem for pairs.* Advances in Mathematics 308, 121–141, 2017.
- **[SOTA]** L. Patey, K. Yokoyama. *The proof-theoretic strength of Ramsey's theorem for pairs and two colors.* Advances in Mathematics 330, 1034–1070, 2018.
- **[SOTA]** B. Monin, L. Patey. *$\mathsf{SRT}^2_2$ does not imply $\mathsf{RT}^2_2$ in $\omega$-models.* Advances in Mathematics 389, 107903, 2021.
- **[Survey]** S. G. Simpson. *Subsystems of Second Order Arithmetic.* 2nd ed., Cambridge University Press / ASL, 2009.
- **[Survey]** D. R. Hirschfeldt. *Slicing the Truth: On the Computable and Reverse Mathematics of Combinatorial Principles.* World Scientific, IMS Lecture Notes Series 28, 2015.
- **[Survey]** D. D. Dzhafarov, C. Mummert. *Reverse Mathematics: Problems, Reductions, and Proofs.* Springer, 2022.

## 10. Worked Example / Concrete Special Case

**Claim (over $\mathsf{RCA}_0$).** $\mathsf{SRT}^2_2$ is equivalent to $\mathsf{D}^2_2$: every $\Delta^0_2$ set $A$ has an infinite subset in $A$ or in $\overline{A}$. (Proved by CJS assuming $\mathsf{I}\Sigma^0_2$; its status under $\mathsf{B}\Sigma^0_2$ alone is exactly the delicacy CSY exploit.)

*Construction.* Let $A$ be $\Delta^0_2$ with approximation $A(x) = \lim_s g(x,s)$, $g$ computable, $g(x,s)\in\{0,1\}$. Define
$$c(x,y) = g(x,y) \quad \text{for } x < y.$$
For each fixed $x$, $\lim_{y} c(x,y) = A(x)$, so $c$ is **stable**. If $H$ is infinite homogeneous with colour $1$, then each $x \in H$ has $c(x,y)=1$ for all larger $y \in H$; since $H$ is infinite this forces $\lim_y c(x,y)=1$, i.e. $H \subseteq A$. Colour $0$ gives $H \subseteq \overline{A}$. Conversely, from a stable $c$ set $A = \{x : \lim_y c(x,y)=1\}$, a $\Delta^0_2$ set; an infinite $H \subseteq A$ is *limit-homogeneous*, and thinning $H$ to a genuinely homogeneous set needs only $\Delta^0_1$ comprehension relative to $H \oplus c$.

**A concrete instance.** Take $A = \{ x : \varphi_x(x)\!\downarrow \}$, the halting set, with $g(x,s) = 1$ iff $\varphi_x(x)$ halts in $\le s$ steps. Then $c(x,y)=g(x,y)$ is a computable stable colouring. Any infinite homogeneous $H$ satisfies $H \subseteq K$ or $H \subseteq \overline{K}$. The first case is possible with $H$ computable (enumerate elements known to halt). The second is not: an infinite computable subset of $\overline{K}$ exists (e.g. indices of trivially divergent programs), so this particular $c$ does **not** witness non-computability — which is precisely why Specker's and Jockusch's harder colourings are needed. Jockusch's $n=3$ colouring, by contrast, encodes an injection $f$ with range $K$ via
$$c(\{x,y,z\}) = 1 \iff (\exists w \le x)\big(f(w) \in (y,z]\big)\ \text{fails uniformly},$$
and any infinite homogeneous set computes $\emptyset'$, giving $\mathsf{RT}^3_2 \to \mathsf{ACA}_0$. The absence of any such coding at $n=2$ — provably, by Seetapun's cone avoidance — is the source of the entire open problem.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*