---
id: 03-geometry/minimal-model-program
title: "Minimal Model Program"
topic: 03-geometry
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Minimal Model Program

> **Topic:** Algebraic & Differential Geometry · **ID:** `03-geometry/minimal-model-program` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

The Minimal Model Program (MMP) asks whether every projective variety can be transformed, by a controlled finite sequence of birational surgeries, into a canonical "simplest" model in its birational class.

Precisely, let $(X,\Delta)$ be a projective klt pair over an algebraically closed field of characteristic $0$, with $\Delta$ an effective $\mathbb{Q}$-divisor. The program predicts a finite sequence of divisorial contractions and flips
$$(X,\Delta) = (X_0,\Delta_0) \dashrightarrow (X_1,\Delta_1) \dashrightarrow \cdots \dashrightarrow (X_N,\Delta_N)$$
ending in exactly one of two outcomes:

1. a **minimal model**: $K_{X_N}+\Delta_N$ is nef, i.e. $(K_{X_N}+\Delta_N)\cdot C \ge 0$ for every curve $C \subset X_N$; or
2. a **Mori fiber space**: a morphism $X_N \to Z$ with $\dim Z < \dim X_N$, connected fibers, relative Picard rank $1$, and $-(K_{X_N}+\Delta_N)$ relatively ample.

Three components remain open in general dimension:

- **Existence of flips** for the full log canonical (lc) range and in positive/mixed characteristic beyond dimension $3$.
- **Termination of flips**: no infinite sequence of flips exists. Open for $\dim X \ge 4$ in general.
- **Abundance**: if $K_X+\Delta$ is nef then it is semiample, i.e. $m(K_X+\Delta)$ is basepoint-free for some $m \in \mathbb{Z}_{>0}$. Open for $\dim X \ge 4$.

A complete resolution requires proving all three (or exhibiting a counterexample) for arbitrary dimension, singularity class, and base field.

## 2. Mathematical Foundations

**Singularities.** Let $\pi: Y \to X$ be a log resolution of the pair $(X,\Delta)$, with $K_X+\Delta$ $\mathbb{Q}$-Cartier. Write
$$K_Y = \pi^*(K_X+\Delta) + \sum_i a(E_i; X,\Delta)\, E_i .$$
The pair is **terminal** if all $a>0$, **canonical** if $a\ge 0$, **klt** if $a>-1$, **log canonical** if $a\ge -1$, for all divisors $E_i$ over $X$.

**Cone Theorem** (Mori, Kawamata, Kollár, Reid, Shokurov). For $(X,\Delta)$ klt projective,
$$\overline{NE}(X) = \overline{NE}(X)_{K_X+\Delta \ge 0} + \sum_{j} \mathbb{R}_{\ge 0}[C_j],$$
where the $K_X+\Delta$-negative extremal rays $\mathbb{R}_{\ge 0}[C_j]$ are locally discrete in $\{ (K_X+\Delta)<0 \}$ and each $C_j$ is a rational curve with $0 < -(K_X+\Delta)\cdot C_j \le 2\dim X$.

**Contraction Theorem.** Each such ray $R$ admits a contraction $\mathrm{cont}_R: X \to Y$ with $\mathrm{cont}_{R*}\mathcal{O}_X = \mathcal{O}_Y$, contracting exactly the curves with class in $R$. Three types: fiber type ($\dim Y<\dim X$), divisorial (exceptional locus a prime divisor), and **small** (exceptional locus of codimension $\ge 2$).

**Flip.** For a small contraction $f: X \to Y$ with $-(K_X+\Delta)$ $f$-ample, the flip is $f^+: X^+ \to Y$ small with $K_{X^+}+\Delta^+$ $f^+$-ample. It exists iff the relative canonical algebra
$$\mathcal{R}(X/Y, K_X+\Delta) = \bigoplus_{m\ge 0} f_*\mathcal{O}_X\!\left(\lfloor m(K_X+\Delta)\rfloor\right)$$
is a finitely generated $\mathcal{O}_Y$-algebra; then $X^+ = \mathrm{Proj}_Y \mathcal{R}$.

**Basepoint-free theorem.** If $(X,\Delta)$ is klt, $D$ nef, and $aD-(K_X+\Delta)$ nef and big for some $a>0$, then $|mD|$ is basepoint-free for $m \gg 0$. Abundance is exactly the case $D = K_X+\Delta$, where no such positivity is available.

**Numerical invariants.** The numerical dimension $\nu(K_X+\Delta) = \max\{k : (K_X+\Delta)^k \cdot H^{n-k} > 0\}$ and Kodaira dimension $\kappa(K_X+\Delta)$ always satisfy $\kappa \le \nu$; abundance is equivalent to $\kappa = \nu$ for nef $K_X+\Delta$ plus semiampleness.

## 3. History & State of the Art (SOTA)

- **1890s–1910s.** The Italian school (Castelnuovo, Enriques) established the surface case: contract $(-1)$-curves until none remain.
- **1979–1982.** Mori's bend-and-break produces rational curves and the Cone Theorem (*Ann. of Math.* 1979, 1982), turning the classification into a program.
- **1982–1988.** Reid, Kawamata, Kollár, Shokurov develop vanishing-based contraction and basepoint-free theorems. Mori proves existence of $3$-fold flips for terminal pairs (*JAMS* 1988) by explicit classification of extremal neighbourhoods.
- **1985–1992.** Shokurov proves termination in dimension $3$ using the "difficulty" function; Kawamata (1992) and Miyaoka (1988–1991) prove abundance for $3$-folds; Keel–Matsuki–McKernan (1994) extend to log $3$-folds.
- **2003.** Shokurov's prelimiting flips give existence of $4$-fold flips.
- **2010.** Birkar–Cascini–Hacon–McKernan (*JAMS* 23) prove existence of flips in all dimensions and existence of minimal models for klt pairs of log general type, plus finite generation of the canonical ring. This is the decisive modern result.
- **2012–2015.** Extension to lc pairs (Birkar, Hacon–Xu); MMP for $3$-folds in characteristic $p>5$ (Hacon–Xu, Birkar, Cascini–Tanaka–Xu).
- **2023.** Bhatt–Ma–Patakfalvi–Schwede–Tucker–Waldron–Witaszek establish the $3$-fold MMP in mixed characteristic using $+$-regularity.

## 4. Partial Results / Verified Cases

| Setting | Status |
|---|---|
| Surfaces, $\dim = 2$, any characteristic | Complete (classical) |
| $\dim = 3$, terminal, char $0$ | Complete: flips (Mori 1988), termination (Shokurov 1985), abundance (Miyaoka–Kawamata) |
| $\dim = 3$, log canonical, char $0$ | Complete (Keel–Matsuki–McKernan 1994; Fujino) |
| $\dim = n$, klt, $K_X+\Delta$ big | Minimal models exist; ring $\mathcal{R}(X,K_X+\Delta)$ finitely generated (BCHM 2010) |
| $\dim = n$, existence of flips, klt | Proven (BCHM 2010); lc case by Birkar 2012, Hacon–Xu 2013 |
| $\dim = 4$, termination | Known for terminal pairs (Kawamata–Matsuda–Matsuki 1987), for klt pairs with big boundary (Alexeev–Hacon–Kawamata 2007), and conditionally on ACC (Birkar 2007) |
| $\dim = 5$, termination | Known for pairs with $K_X+\Delta$ effective, klt, via Birkar 2007 + ACC results of Hacon–McKernan–Xu 2014 |
| $\dim = 3$, char $p > 5$ | MMP holds (Hacon–Xu 2015, Birkar 2016, Cascini–Tanaka–Xu) |
| $\dim = 3$, mixed characteristic, residue char $p>5$ | MMP holds (Bhatt et al. 2023) |
| Kähler $\dim = 3$ | Minimal models exist (Höring–Peternell, *Invent. Math.* 2016) |
| Abundance, $\dim \ge 4$ | Open; known if $\nu = 0$ (Nakayama), and under strong hypotheses (Lazić–Peternell) |
| Fano varieties, fixed $\dim$, $\epsilon$-lc | Bounded (Birkar, *Ann. of Math.* 2019, 2021 — BAB conjecture) |

## 5. Principal Obstacles

- **Termination is not a positivity statement.** Existence of flips follows from finite generation, which BCHM derives from extension theorems and multiplier ideals — all positivity-driven. Termination is a *descending chain* statement about discrepancies, and no known positivity input controls it. Shokurov's dimension-$3$ "difficulty" function $d(X,\Delta)=\\#\{E : a(E;X,\Delta)<1\}$ drops at each flip; in dimension $\ge 4$ the analogous set is infinite and no replacement monotone invariant of finite range is known.
- **MMP with scaling is only partially adequate.** BCHM proves termination *of a particular sequence* (with scaling) when $K_X+\Delta$ is big. When $\kappa = -\infty$ or $K_X+\Delta$ is on the boundary of the effective cone, the scaling threshold can converge to a positive limit without terminating; this is exactly the non-vanishing gap.
- **Abundance escapes vanishing theorems.** All basepoint-freeness proofs need $aD - (K_X+\Delta)$ nef and big to run Kawamata–Viehweg vanishing. For $D=K_X+\Delta$ this is vacuous, so the induction has no base. Dimension $3$ used Miyaoka's generic semipositivity of $\Omega^1_X$ plus Riemann–Roch bookkeeping — both genuinely $3$-dimensional.
- **Characteristic $p$ kills the tools.** Kodaira vanishing fails (Raynaud), resolution of singularities is unavailable above dimension $3$, and multiplier ideals must be replaced by test ideals/Frobenius splitting, which do not yet give the required extension theorems in dimension $\ge 4$.
- **Kähler non-projectivity.** Without ample line bundles, $\overline{NE}(X)$ must be replaced by cones of currents; bend-and-break has no direct analogue, so extremal rays are produced only by transcendental methods that currently stop at dimension $3$.

## 6. The Gap

Proven: flips exist in every dimension for klt (and lc) pairs in characteristic $0$; minimal models exist when $K_X+\Delta$ is big.

Conjectured: the same for arbitrary $(X,\Delta)$, together with abundance.

The precise remaining steps are:

1. **Non-vanishing.** If $K_X+\Delta$ is pseudo-effective and $(X,\Delta)$ klt, then $K_X+\Delta \sim_{\mathbb{Q}} D \ge 0$. This is the single implication that would upgrade BCHM from "big" to "pseudo-effective", giving existence of minimal models in full.
2. **Termination.** Rule out an infinite flip sequence $X_0 \dashrightarrow X_1 \dashrightarrow \cdots$ in dimension $\ge 4$ for non-big boundaries. Known reduction: ACC for minimal log discrepancies plus lower-semicontinuity of mlds implies termination in all dimensions (Shokurov). ACC for log canonical thresholds is a theorem (Hacon–McKernan–Xu 2014); ACC for mlds is not.
3. **Abundance.** Upgrade $K_X+\Delta$ nef to semiample. Equivalent formulation: $\kappa(K_X+\Delta) = \nu(K_X+\Delta)$ for nef $K_X+\Delta$ on klt pairs.

## 7. Current Research (as of June 2026)

- **Termination via mlds and complements.** Work at Utah (Hacon, Xu's school at Princeton/MIT, Moraga at UCLA) targets termination for pseudo-effective $4$-folds and ACC for minimal log discrepancies in fixed dimension. *(frontier — verify)* Recent preprints claim termination for large classes of $4$-fold pseudo-effective flips.
- **Kähler MMP in dimension $\ge 4$.** Das–Hacon and Höring–Peternell extend contraction and flip existence to compact Kähler klt spaces; dimension $4$ remains partial. *(frontier — verify)*
- **Mixed and positive characteristic.** After Bhatt–Ma–Patakfalvi–Schwede–Tucker–Waldron–Witaszek (2023), efforts focus on removing the $p>5$ hypothesis and on $4$-folds using $+$-stable sections and perfectoid techniques (Witaszek, Takamatsu, Yoshikawa).
- **Generalized pairs and boundedness.** Birkar's generalized pairs framework underpins the BAB theorem and now drives boundedness of log Calabi–Yau fibrations and of minimal models with bounded invariants.
- **Analytic approaches.** Siu's analytic proof of finite generation and Demailly–Păun-style transcendental Morse inequalities remain an independent route to abundance.
- **Foliated MMP.** Cascini–Spicer establish the MMP for rank-$1$ and rank-$2$ foliations on $3$-folds, with abundance-type statements; extension to higher rank is active.

## 8. Future Work

- Prove ACC for minimal log discrepancies in dimension $n$; combined with lower semicontinuity this settles termination unconditionally.
- Establish non-vanishing in dimension $4$ via Nakayama–Zariski decomposition and the $\sigma$-decomposition, isolating the case $\nu(K_X)=0$ versus $\nu>0$.
- Develop a Frobenius/perfectoid analogue of Hacon–McKernan extension in dimension $\ge 4$, the sole missing input for the positive-characteristic MMP.
- Prove abundance for $3$-folds in characteristic $p$ without the $p>5$ restriction.
- Find a transcendental substitute for bend-and-break to produce extremal rays on Kähler $4$-folds.

## 9. Key References

- **[Foundational]** S. Mori. *Flip theorem and the existence of minimal models for 3-folds.* Journal of the AMS 1 (1988), 117–253. [DOI](https://doi.org/10.2307/1990969)
- **[Foundational]** Y. Kawamata, K. Matsuda, K. Matsuki. *Introduction to the minimal model problem.* Advanced Studies in Pure Mathematics 10 (1987), 283–360.
- **[Foundational]** V. V. Shokurov. *3-fold log flips.* Izvestiya RAN, Ser. Mat. 56 (1992), 105–203. [DOI](https://doi.org/10.1070/im1993v040n01abeh001862)
- **[Foundational]** V. V. Shokurov. *Prelimiting flips.* Proceedings of the Steklov Institute of Mathematics 240 (2003), 75–213.
- **[SOTA]** C. Birkar, P. Cascini, C. D. Hacon, J. McKernan. *Existence of minimal models for varieties of log general type.* Journal of the AMS 23 (2010), 405–468. [DOI](https://doi.org/10.1090/s0894-0347-09-00649-3)
- **[SOTA]** C. Birkar. *Existence of log canonical flips and a special LMMP.* Publications mathématiques de l'IHÉS 115 (2012), 325–368. [DOI](https://doi.org/10.1007/s10240-012-0039-5)
- **[SOTA]** C. D. Hacon, C. Xu. *Existence of log canonical closures.* Inventiones mathematicae 192 (2013), 161–195. [DOI](https://doi.org/10.1007/s00222-012-0409-0)
- **[SOTA]** C. D. Hacon, J. McKernan, C. Xu. *ACC for log canonical thresholds.* Annals of Mathematics 180 (2014), 523–571. [DOI](https://doi.org/10.4007/annals.2014.180.2.3)
- **[SOTA]** C. D. Hacon, C. Xu. *On the three dimensional minimal model program in positive characteristic.* Journal of the AMS 28 (2015), 711–744. [DOI](https://doi.org/10.1090/s0894-0347-2014-00809-2)
- **[SOTA]** B. Bhatt, L. Ma, Zs. Patakfalvi, K. Schwede, K. Tucker, J. Waldron, J. Witaszek. *Globally +-regular varieties and the minimal model program for threefolds in mixed characteristic.* Publications mathématiques de l'IHÉS 138 (2023), 69–227.
- **[SOTA]** A. Höring, T. Peternell. *Minimal models for Kähler threefolds.* Inventiones mathematicae 203 (2016), 217–264. [DOI](https://doi.org/10.1007/s00222-015-0592-x)
- **[SOTA]** C. Birkar. *Singularities of linear systems and boundedness of Fano varieties.* Annals of Mathematics 193 (2021), 347–405. [DOI](https://doi.org/10.4007/annals.2021.193.2.1)
- **[Abundance]** Y. Kawamata. *Abundance theorem for minimal threefolds.* Inventiones mathematicae 108 (1992), 229–246. [DOI](https://doi.org/10.1007/bf02100604)
- **[Abundance]** S. Keel, K. Matsuki, J. McKernan. *Log abundance theorem for threefolds.* Duke Mathematical Journal 75 (1994), 99–119. [DOI](https://doi.org/10.1215/s0012-7094-94-07504-2)
- **[Termination]** V. Alexeev, C. D. Hacon, Y. Kawamata. *Termination of (many) 4-dimensional log flips.* Inventiones mathematicae 168 (2007), 433–448. [DOI](https://doi.org/10.1007/s00222-007-0038-1)
- **[Termination]** C. Birkar. *Ascending chain condition for log canonical thresholds and termination of log flips.* Duke Mathematical Journal 136 (2007), 173–180. [DOI](https://doi.org/10.1215/s0012-7094-07-13615-9)
- **[Survey / Book]** J. Kollár, S. Mori. *Birational Geometry of Algebraic Varieties.* Cambridge University Press, 1998.
- **[Survey / Book]** A. Corti (ed.). *Flips for 3-folds and 4-folds.* Oxford University Press, 2007. [DOI](https://doi.org/10.1093/acprof:oso/9780198570615.001.0001)
- **[Survey / Book]** O. Fujino. *Foundations of the Minimal Model Program.* MSJ Memoirs 35, Mathematical Society of Japan, 2017. [DOI](https://doi.org/10.2969/msjmemoirs/035010000)

## 10. Worked Example / Concrete Special Case

**Surface MMP run on $X = \mathrm{Bl}_p\mathbb{P}^2$.** Let $\pi: X \to \mathbb{P}^2$ be the blow-up at a point $p$, with exceptional curve $E$ and $H = \pi^*\mathcal{O}(1)$. Intersection theory:
$$H^2 = 1,\quad H\cdot E = 0,\quad E^2 = -1,\qquad K_X = \pi^*K_{\mathbb{P}^2}+E = -3H+E .$$

Take $\Delta = 0$. Then
$$K_X \cdot E = (-3H+E)\cdot E = -3(H\cdot E) + E^2 = 0 + (-1) = -1 < 0 .$$
So $\mathbb{R}_{\ge 0}[E]$ is a $K_X$-negative ray. It is extremal: $E^2 = -1 < 0$ forces $[E]$ to span an extremal ray of $\overline{NE}(X) = \mathbb{R}_{\ge 0}[E] + \mathbb{R}_{\ge 0}[\ell]$, where $\ell = H - E$ is the strict transform of a line through $p$ (check $\ell^2 = 1 - 1 = 0$, $K_X\cdot\ell = -3+(-1)\cdot(-1)\cdot$ … explicitly $K_X\cdot \ell = (-3H+E)\cdot(H-E) = -3 - E^2 = -3+1 = -2 < 0$).

Contracting $R=\mathbb{R}_{\ge 0}[E]$ is the *divisorial* contraction $\pi$ itself, since $\dim E = 1 = \dim X - 1$. The output is $\mathbb{P}^2$, on which $K_{\mathbb{P}^2} = -3H$ satisfies $K_{\mathbb{P}^2}\cdot\ell = -3 < 0$ for every line. So $K_{\mathbb{P}^2}$ is not nef: the program continues by contracting $\mathbb{P}^2 \to \mathrm{Spec}\,\mathbb{C}$, a **Mori fiber space** of fiber type with relative Picard rank $\rho(\mathbb{P}^2)=1$ and $-K_{\mathbb{P}^2}$ ample.

Total run: one divisorial contraction, zero flips, terminating in a Mori fiber space. Termination is trivial here because $\rho(X)=2$ drops by $1$ at each step and $\rho \ge 1$.

**Why dimension $3$ is different.** Small contractions first appear in dimension $3$. In the *Francia flip*, $X$ contains a curve $C\cong\mathbb{P}^1$ with $K_X\cdot C = -1/2$ inside a $\frac{1}{2}(1,1,1)$ quotient singularity; contracting $C$ gives $f:X\to Y$ with $\mathrm{Exc}(f)=C$ of codimension $2$, so $Y$ is not $\mathbb{Q}$-Gorenstein-friendly and $K_Y$ is not $\mathbb{Q}$-Cartier. The flip $X^+\to Y$ replaces $C$ by a different curve $C^+$ with $K_{X^+}\cdot C^+ = +1$. Note $\rho(X^+) = \rho(X)$: **the Picard number does not drop**, so the surface termination argument fails outright. Discrepancies do increase strictly at a flip, which is what Shokurov's difficulty function exploits in dimension $3$ — and what has no known analogue in dimension $\ge 4$.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*