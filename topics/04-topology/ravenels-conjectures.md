---
id: 04-topology/ravenels-conjectures
title: "Ravenel's Conjectures"
topic: 04-topology
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Ravenel's Conjectures

> **Topic:** Topology & Knot Theory · **ID:** `04-topology/ravenels-conjectures` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

In Section 10 of *Localization with respect to certain periodic homology theories* (1984), Douglas Ravenel stated seven conjectures organizing the $p$-local stable homotopy category by "chromatic" height. Informally: all large-scale periodicity in stable homotopy is governed by the Morava $K$-theories $K(n)$, and everything not detected by them is nilpotent.

The seven statements, in the numbering that became standard:

1. **Nilpotence.** If $f\colon F \to X$ is a map of spectra with $F$ finite and $MU_*(f)=0$, then $f$ is smash-nilpotent. Equivalently, for a connective ring spectrum $R$, elements of $\pi_*R$ killed by the Hurewicz map to $MU_*R$ are nilpotent.
2. **Class invariance.** The Bousfield class of a $p$-local finite spectrum $X$ of type $n$ is $\langle X\rangle=\bigl\langle\bigvee_{m\ge n}K(m)\bigr\rangle$; in particular $\langle X\rangle$ depends only on the type.
3. **Thick subcategory.** Every thick subcategory of finite $p$-local spectra is one of the $\mathcal C_n=\{X: K(n-1)_*X=0\}$, giving the chain $\mathcal C_0\supset\mathcal C_1\supset\cdots$.
4. **Periodicity.** Every finite $p$-local $X$ of type $n$ admits a $v_n$-self map $v\colon \Sigma^d X\to X$ inducing an isomorphism on $K(n)_*$ and zero on $K(m)_*$ for $m\ne n$; such maps are asymptotically unique.
5. **Smashing.** The localization functor $L_n = L_{E(n)}$ is smashing: $L_nX \simeq X\wedge L_nS^0$; equivalently $L_n$ agrees with the finite localization $L_n^f$.
6. **Chromatic convergence.** For finite $p$-local $X$, the tower $\cdots\to L_nX\to L_{n-1}X\to\cdots$ converges: $X\to \operatorname{holim}_n L_nX$ is an equivalence.
7. **Telescope.** For $X$ finite of type $n$ with $v_n$-self map $v$, the telescope $T(n)=v^{-1}X=\operatorname{colim}(X\xrightarrow{v}\Sigma^{-d}X\to\cdots)$ satisfies $\langle T(n)\rangle=\langle K(n)\rangle$; equivalently $L_{T(n)}=L_{K(n)}$ and $L_n^f=L_n$ on all spectra.

Conjectures 1–6 are theorems. Conjecture 7 is **true for $n=0,1$ at all primes and false for all $n\ge 2$ at all primes** (Burklund–Hahn–Levy–Schlank, 2023). What remains open is not the truth value but the structure of the $T(n)$-local category that the failure exposes.

## 2. Mathematical Foundations

Work in the stable homotopy category $\mathrm{Sp}$, localized at a prime $p$.

**Complex cobordism and formal groups.** $MU_*\cong\mathbb Z[x_1,x_2,\dots]$, $|x_i|=2i$, carries the universal formal group law (Quillen). $p$-locally $MU_{(p)}$ splits into copies of Brown–Peterson theory with
$$BP_*=\mathbb Z_{(p)}[v_1,v_2,\dots],\qquad |v_n|=2(p^n-1).$$
The invariant prime ideals of $BP_*$ are exactly $I_n=(p,v_1,\dots,v_{n-1})$, $0\le n\le\infty$ (Landweber), which is the algebraic source of the height filtration.

**Morava $K$-theories.** For $0<n<\infty$, $K(n)$ is the complex-orientable ring spectrum with
$$K(n)_*=\mathbb F_p[v_n^{\pm1}],$$
whose formal group is the Honda formal group of height $n$. Conventions: $K(0)=H\mathbb Q$, $K(\infty)=H\mathbb F_p$. Each $K(n)$ is a field object: every module splits as a wedge of suspensions, so $K(n)_*(X\wedge Y)\cong K(n)_*X\otimes_{K(n)_*}K(n)_*Y$. Also $E(n)_*=\mathbb Z_{(p)}[v_1,\dots,v_n][v_n^{-1}]$ with $L_n:=L_{E(n)}$.

**Bousfield classes.** $\langle E\rangle=\langle F\rangle$ iff $E_*X=0\Leftrightarrow F_*X=0$ for all $X$; $L_E$ is localization at $E$ (Bousfield, 1979). Ravenel's picture asserts $\langle E(n)\rangle=\bigvee_{m\le n}\langle K(m)\rangle$ and that the $\langle K(n)\rangle$ are the minimal nonzero classes below finite spectra.

**Type and thickness.** $X$ has *type* $n$ if $K(m)_*X=0$ for $m<n$ and $K(n)_*X\ne0$. A full subcategory of finite spectra is *thick* if closed under cofibers, retracts and suspension.

**Chromatic fracture.** Conjectures 5–7 combine into the pullback square
$$L_nX\longrightarrow L_{K(n)}X,\qquad L_{n-1}X\longrightarrow L_{n-1}L_{K(n)}X,$$
so that a finite spectrum is assembled from its $K(n)$-local pieces. The telescope conjecture asks whether the *computable* $T(n)$-local piece (a filtered colimit of finite objects) coincides with the *structured* $K(n)$-local piece (governed by Morava $E$-theory and the Morava stabilizer group $\mathbb G_n=\mathbb S_n\rtimes\mathrm{Gal}$, via $\pi_*L_{K(n)}S^0=H^*_c(\mathbb G_n;(E_n)_*)$).

## 3. History & State of the Art (SOTA)

- **1970s.** Morava's unpublished work on formal groups and $\mathrm{Ext}_{BP_*BP}$; Miller–Ravenel–Wilson (1977) compute the chromatic spectral sequence and the Greek-letter families, exhibiting height-$n$ periodicity in $\pi_*S^0$.
- **1979.** Bousfield's localization machinery makes "$\langle E\rangle$" a usable invariant.
- **1984.** Ravenel's *Amer. J. Math.* paper states the conjectures and proves several implications among them, plus the $n=1$ case of the telescope conjecture in outline.
- **1988.** Devinatz–Hopkins–Smith prove the Nilpotence Theorem (Conjecture 1), *Annals of Mathematics* 128.
- **1992–98.** Hopkins–Smith (*Annals* 148, 1998) deduce the thick subcategory and periodicity theorems (Conjectures 2–4). Hopkins–Ravenel prove the smashing theorem and chromatic convergence (Conjectures 5–6), written up in Ravenel's *Nilpotence and Periodicity* (Annals Studies 128, 1992).
- **2001.** Mahowald–Ravenel–Shick give strong computational evidence *against* the telescope conjecture at $n=2$, $p\ge 5$, via the "triple loop space" / parametrized Adams spectral sequence.
- **2023.** Burklund–Hahn–Levy–Schlank disprove Conjecture 7 for all $n\ge2$ and all $p$, using algebraic $K$-theory and redshift.

## 4. Partial Results / Verified Cases

- **Conjectures 1–6: complete theorems**, no dimension or prime restriction.
- **Telescope, $n=0$:** trivial; $L_{T(0)}=L_{K(0)}=$ rationalization.
- **Telescope, $n=1$, $p$ odd:** Miller (1981), by comparing the Adams and Adams–Novikov spectral sequences for $v_1^{-1}\pi_*(S/p)$.
- **Telescope, $n=1$, $p=2$:** Mahowald (1982), via the $bo$-resolution and the image-of-$J$ computation of $v_1^{-1}\pi_*(S/2)$.
- **Telescope, $n\ge2$: false.** BHLS produce, for every $n\ge 2$ and every prime, spectra with $L_{T(n)}X\not\simeq L_{K(n)}X$; equivalently $L_n^f\ne L_n$ and $\langle T(n)\rangle\ne\langle K(n)\rangle$.
- **Quantitative consequence (BHLS).** $\pi_*L_{T(n)}S^0$ is strictly larger than $\pi_*L_{K(n)}S^0$; the telescopic homotopy of the sphere contains infinite families invisible to $K(n)$, and $\pi_*L_{T(n)}S^0$ fails to be finitely generated over $\mathbb Z_p$ in the way the $K(n)$-local answer is. *(frontier — verify precise formulations against the published version.)*
- **Algebraic analogues:** the telescope conjecture holds in the derived category of a commutative noetherian ring (Neeman, 1992) and for the stable module category of many finite groups — the failure is specific to topology.

## 5. Principal Obstacles

- **No finite-model handle on $K(n)$-local objects.** $L_{K(n)}$ is not smashing for $n\ge1$; it is a limit-type construction ($L_{K(n)}X=\operatorname{holim} L_n(X\wedge M_I)$). Comparing it to the colimit-type $L_{T(n)}$ pits a limit against a colimit, and no finiteness argument bridges them.
- **Localized Adams spectral sequences do not converge visibly.** For $v_n^{-1}\pi_*X$ the localized Adams $E_2$-term at $n\ge2$ has an unbounded "parasitic" region; distinguishing genuine homotopy from a differential-collapsing artifact defeated direct computation for two decades (Mahowald–Ravenel–Shick).
- **The Morava stabilizer group is too rigid.** $K(n)$-local answers are cohomology of the profinite group $\mathbb G_n$; the telescopic category has no comparable descent-theoretic model, so all $\mathbb G_n$-equivariant technology is unavailable on the $T(n)$ side.
- **Height 1 is misleading.** At $n=1$ the relevant object is $K$-theory, where Adams operations give complete control; at $n\ge2$ there is no analogous cohomology theory with computable homotopy and a self map to leverage.
- **Even now, the failure is non-constructive at the level of $\pi_*S^0$.** BHLS detect the discrepancy through algebraic $K$-theory; no explicit element of $\pi_*L_{T(n)}S^0$ outside the $K(n)$-local part has been named for general $n$.

## 6. The Gap

The proven boundary is exact: Conjectures 1–6 hold universally; Conjecture 7 holds for $n\le1$ and fails for $n\ge2$. The residual mathematical problem is *descriptive*: the chromatic filtration of finite spectra now has two inequivalent refinements, the *K-theoretic* one ($L_{K(n)}$) and the *telescopic* one ($L_{T(n)}$), and there is no known description of the fiber
$$\mathrm{fib}\bigl(L_{T(n)}S^0\longrightarrow L_{K(n)}S^0\bigr)$$
for any $n\ge2$. Crossing the gap means: compute $\pi_*L_{T(2)}S^0$ at some prime, classify the localizing subcategories of $T(n)$-local spectra (the Balmer spectrum of the telescopic category), and determine whether telescopic convergence — $X\to\operatorname{holim}_nL_n^fX$ — still holds for finite $X$.

## 7. Current Research (as of June 2026)

- **BHLS program (Harvard/MIT/Copenhagen/Jerusalem).** The counterexample rests on: Hahn–Wilson's Lichtenbaum–Quillen property for truncated Brown–Peterson spectra $BP\langle n\rangle$ (*Annals*, 2022); Land–Mathew–Meier–Tamme's purity results for chromatically localized $K$-theory; and Burklund–Schlank–Yuan's chromatic Nullstellensatz. Current work extends these to compute $T(n)$-local $K$-theory of further ring spectra. *(frontier — verify)*
- **Telescopic Balmer spectrum.** Barthel, Heard, Sanders and collaborators study prismatic/telescopic refinements of the Balmer spectrum of finite spectra; the disproof does *not* alter the classification of thick subcategories of finite spectra (Conjecture 3 stands), but it does change the lattice of localizing subcategories.
- **Redshift as a computational engine.** $K(\text{height }n)\rightsquigarrow \text{height }n+1$ is now a production method: telescopic invariants of $\mathbb F_p$-algebras and of $\mathbb{S}$-algebras give access to height $n+1$ phenomena unreachable by $E$-theory.
- **Ambidexterity and semiadditivity.** Carmeli–Schlank–Yanovski's $\infty$-semiadditivity of $T(n)$-local spectra is the main structural theorem available on the telescopic side and is the current substitute for Galois descent.
- **Recomputation of MRS.** Renewed attention to the $n=2$, $p\ge5$ parametrized Adams spectral sequence, now with the knowledge that the extra classes are real. *(frontier — verify)*

## 8. Future Work

- Compute $\pi_*L_{T(2)}S^0$ at a large prime, at least in a range, and identify the non-$K(2)$-local classes explicitly.
- Decide whether *telescopic chromatic convergence* $X\simeq\operatorname{holim}_nL_n^fX$ holds for finite $p$-local $X$; Ravenel's Conjecture 6 gives only the $L_n$ version.
- Classify localizing subcategories of $\mathrm{Sp}_{T(n)}$ and determine whether $\langle T(n)\rangle$ decomposes further — i.e., whether there are Bousfield classes strictly between $\langle T(n)\rangle$ and $\langle K(n)\rangle$.
- Determine whether the failure is "small" (a bounded-height correction term) or "large" (unbounded new families) as $n$ grows.
- Transport the disproof to motivic and equivariant settings, where the telescope conjecture remains formally open.

## 9. Key References

- **[Foundational]** D. C. Ravenel. *Localization with respect to certain periodic homology theories.* American Journal of Mathematics **106** (1984), 351–414. [DOI](https://doi.org/10.2307/2374308)
- **[Foundational]** E. S. Devinatz, M. J. Hopkins, J. H. Smith. *Nilpotence and stable homotopy theory I.* Annals of Mathematics **128** (1988), 207–241.
- **[Foundational]** M. J. Hopkins, J. H. Smith. *Nilpotence and stable homotopy theory II.* Annals of Mathematics **148** (1998), 1–49.
- **[Foundational]** A. K. Bousfield. *The localization of spectra with respect to homology.* Topology **18** (1979), 257–281. [DOI](https://doi.org/10.1016/0040-9383(79)90018-1)
- **[Survey / Book]** D. C. Ravenel. *Nilpotence and Periodicity in Stable Homotopy Theory.* Annals of Mathematics Studies 128, Princeton University Press, 1992.
- **[Foundational]** H. R. Miller. *On relations between Adams spectral sequences, with an application to the stable homotopy of a Moore space.* Journal of Pure and Applied Algebra **20** (1981), 287–312. [DOI](https://doi.org/10.1016/0022-4049(81)90064-5)
- **[Foundational]** M. Mahowald. *The image of $J$ in the EHP sequence.* Annals of Mathematics **116** (1982), 65–112. [DOI](https://doi.org/10.2307/2007048)
- **[Foundational]** H. R. Miller, D. C. Ravenel, W. S. Wilson. *Periodic phenomena in the Adams–Novikov spectral sequence.* Annals of Mathematics **106** (1977), 469–516. [DOI](https://doi.org/10.2307/1971064)
- **[SOTA]** R. Burklund, J. Hahn, I. Levy, T. M. Schlank. *K-theoretic counterexamples to Ravenel's telescope conjecture.* arXiv:2310.17459, 2023.
- **[SOTA]** J. Hahn, D. Wilson. *Redshift and multiplication for truncated Brown–Peterson spectra.* Annals of Mathematics **196** (2022), 1277–1351. [DOI](https://doi.org/10.4007/annals.2022.196.3.6)
- **[SOTA]** M. Land, A. Mathew, L. Meier, G. Tamme. *Purity in chromatically localized algebraic K-theory.* Journal of the AMS (2024). [DOI](https://doi.org/10.1090/jams/1043)
- **[Evidence]** M. Mahowald, D. C. Ravenel, P. Shick. *The triple loop space approach to the telescope conjecture.* In *Homotopy Methods in Algebraic Topology*, Contemporary Mathematics 271, AMS, 2001, 217–284. [DOI](https://doi.org/10.1090/conm/271/04358)
- **[Structural]** M. Hovey, N. P. Strickland. *Morava K-theories and localisation.* Memoirs of the AMS **139** (1999), no. 666.
- **[Algebraic analogue]** A. Neeman. *The chromatic tower for $D(R)$.* Topology **31** (1992), 519–532. [DOI](https://doi.org/10.1016/0040-9383(92)90047-l)

## 10. Worked Example / Concrete Special Case

**Height 1 at an odd prime: the telescope conjecture verified.**

Let $p$ be odd and $M=S/p$ the mod-$p$ Moore spectrum, cofiber of $p\colon S^0\to S^0$. Then $K(0)_*M=\pi_*(M)\otimes\mathbb Q=0$ and $K(1)_*M\ne0$, so $M$ has type 1. Adams constructed a self map
$$v_1\colon \Sigma^{2p-2}M\longrightarrow M$$
inducing multiplication by $v_1$ on $K(1)_*M=\mathbb F_p[v_1^{\pm1}]\otimes\Lambda$, and zero on $K(m)_*$ for $m\ne1$. The telescope is
$$T(1)=v_1^{-1}M=\operatorname{colim}\bigl(M\xrightarrow{\;v_1\;}\Sigma^{-(2p-2)}M\xrightarrow{\;v_1\;}\Sigma^{-2(2p-2)}M\to\cdots\bigr).$$

*The $K(1)$-local answer.* $K(1)$ is a summand of mod-$p$ complex $K$-theory, and
$$\pi_*L_{K(1)}(S/p)\;\cong\;\mathbb F_p[v_1^{\pm1}]\otimes E(\zeta),\qquad |v_1|=2p-2,\;|\zeta|=-1,$$
a free module of rank 2 over $\mathbb F_p[v_1^{\pm1}]$, so exactly two $\mathbb F_p$'s in every $(2p-2)$-periodic block.

*The telescopic answer.* Miller runs the localized Adams spectral sequence for $v_1^{-1}\pi_*(S/p)$ and shows the $E_2$-term $v_1^{-1}\mathrm{Ext}_{A}(\mathbb F_p, H^*M)$ collapses onto the same rank-2 $\mathbb F_p[v_1^{\pm1}]$-module, with no extra classes surviving. Hence
$$\pi_*T(1)\;\xrightarrow{\;\cong\;}\;\pi_*L_{K(1)}(S/p),$$
so $\langle T(1)\rangle=\langle K(1)\rangle$: Conjecture 7 holds at $n=1$. Assembling with the cofiber sequence $S^0\xrightarrow{p}S^0\to M$ recovers the classical
$$\pi_iL_1S^0_{(p)}=\begin{cases}\mathbb Z_{(p)} & i=0,\\ \mathbb Z/p^{k+1} & i=(2p-2)k-1,\;k\ge1,\\ \mathbb Q_p/\mathbb Z_p & i=-2,\\ 0&\text{else,}\end{cases}$$
i.e. the image of $J$.

**Why $n=2$ breaks.** Repeat with a type 2 complex, e.g. $V(1)=S/(p,v_1)$ for $p\ge5$, and its $v_2$-self map $v_2\colon\Sigma^{2p^2-2}V(1)\to V(1)$. The $K(2)$-local homotopy $\pi_*L_{K(2)}V(1)$ is finite-rank over $\mathbb F_p[v_2^{\pm1}]$ and computable from $H^*_c(\mathbb G_2;\cdot)$. Mahowald–Ravenel–Shick predicted, and BHLS proved, that $\pi_*v_2^{-1}V(1)$ is strictly larger: the localized Adams $E_2$-term contains an infinite family of classes with no $K(2)$-local counterpart, and they survive. The rank-2-per-period rigidity of height 1 has no height-2 analogue, and that is precisely the content of the disproof.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*