---
id: 03-geometry/abundance-conjecture
title: "Abundance Conjecture"
topic: 03-geometry
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Abundance Conjecture

> **Topic:** Algebraic & Differential Geometry · **ID:** `03-geometry/abundance-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

**Conjecture (Abundance).** Let $(X,\Delta)$ be a projective klt (Kawamata log terminal) pair over $\mathbb{C}$ with $\Delta$ an effective $\mathbb{Q}$-divisor. If the log canonical divisor $K_X+\Delta$ is **nef**, then it is **semi-ample**: some multiple $m(K_X+\Delta)$ with $m\in\mathbb{Z}_{>0}$ is base-point free.

Equivalently, in numerical form: for a nef $K_X+\Delta$ the Kodaira dimension equals the numerical dimension,
$$\kappa(X,K_X+\Delta)\;=\;\nu(X,K_X+\Delta).$$

The conjecture is expected in the wider **log canonical (lc)** and **semi-log-canonical (slc)** settings, where semi-ampleness is the statement needed to build moduli of stable varieties. A complete proof must handle all dimensions $n=\dim X\ge 4$ and all $\nu\in\{0,1,\dots,n\}$; a disproof would exhibit a klt pair with $K_X+\Delta$ nef and $\kappa<\nu$, i.e. a minimal model with no Iitaka fibration realizing its numerical positivity.

Abundance is the last missing pillar of the Minimal Model Program (MMP). With existence of minimal models (known for klt pairs of general type, Birkar–Cascini–Hacon–McKernan 2010) it would give: every non-uniruled projective variety is birational to a variety with a canonical **Iitaka fibration** of relative dimension $n-\kappa$, completing the birational classification in all dimensions.

## 2. Mathematical Foundations

Let $X$ be a normal projective variety with $K_X+\Delta$ $\mathbb{Q}$-Cartier, and $f:Y\to X$ a log resolution with
$$K_Y \;=\; f^*(K_X+\Delta)\;+\;\sum_i a_i E_i .$$
The pair is **klt** if $a_i>-1$ for all $i$ (all $f$), **lc** if $a_i\ge -1$.

**Nef:** $D\cdot C\ge 0$ for every irreducible curve $C\subset X$.
**Semi-ample:** $|mD|$ base-point free for some $m>0$; equivalently $D=g^*A$ for a morphism $g:X\to Z$ with $A$ ample on $Z$.

**Kodaira dimension.**
$$\kappa(X,D)\;=\;\limsup_{m\to\infty}\frac{\log h^0(X,\mathcal{O}_X(\lfloor mD\rfloor))}{\log m}\in\{-\infty,0,1,\dots,n\}.$$

**Numerical dimension** (for $D$ nef): the largest $k$ with $D^{k}\cdot H^{\,n-k}>0$ for an ample $H$,
$$\nu(X,D)\;=\;\max\{k: D^{k}\cdot H^{n-k}\neq 0\}.$$
Nakayama's $\sigma$-decomposition extends $\nu$ to pseudo-effective $D$ via $\kappa_\sigma$, and gives the general inequality
$$\kappa(X,D)\;\le\;\nu(X,D)\qquad(D\ \text{nef}).$$
Abundance asserts equality for $D=K_X+\Delta$. Semi-ampleness for nef $D$ implies $\kappa=\nu$, and conversely for log canonical divisors the equality $\kappa=\nu$ plus the basepoint-free theorem machinery yields semi-ampleness (Nakayama; Fujino).

**Inputs the conjecture relies on.**
- *Basepoint-free theorem* (Kawamata–Shokurov): if $D$ is nef and $aD-(K_X+\Delta)$ is nef and big for some $a>0$, then $D$ is semi-ample. This settles $\nu=n$ (big case).
- *Cone theorem* and existence of flips/minimal models (BCHM, *J. Amer. Math. Soc.* 23 (2010)).
- *Nonvanishing Conjecture*: if $K_X+\Delta$ is pseudo-effective then $\kappa(X,K_X+\Delta)\ge 0$. Abundance $\Leftrightarrow$ Nonvanishing + "$\kappa\ge 0 \Rightarrow \kappa=\nu$" in each dimension.
- *Extension theorems* / multiplier ideals (Siu, Hacon–McKernan, Demailly–Hacon–Păun) for lifting sections from divisors.

## 3. History & State of the Art (SOTA)

- **1970s.** Iitaka's fibration and the classification of surfaces (Enriques–Kodaira) implicitly contain abundance for $n=2$: a minimal surface with $K_X$ nef has $|mK_X|$ base-point free for $m=12$ (Enriques' theorem on elliptic and properly elliptic surfaces).
- **1980s.** Mori's bend-and-break, Kawamata–Shokurov basepoint-free and rationality theorems build the MMP; abundance is isolated by Kawamata and Reid as the remaining conjecture beyond termination.
- **1988.** Miyaoka proves the $\nu=1$ case for threefolds using generic semipositivity of $\Omega^1_X$ and foliations in characteristic $p$.
- **1992.** Kawamata completes abundance for minimal projective threefolds, combining Miyaoka's results with the theory of the Albanese map and Viehweg's weak positivity.
- **1994.** Keel–Matsuki–McKernan prove the **log** abundance theorem for threefolds (with a 2004 erratum fixing the $\nu=2$ argument).
- **2000–2004.** Fujino proves abundance for semi-log-canonical threefolds; Nakayama's monograph *Zariski-decomposition and Abundance* establishes the $\kappa_\sigma=0$ case in all dimensions and the general framework.
- **2010s.** Analytic approaches (Siu, Păun, Demailly–Hacon–Păun) attack nonvanishing via $L^2$ methods; Campana–Koziarz–Păun and Fujino settle the maximal-Albanese-dimension case; Gongyo–Lehmann and Lazić–Peternell prove sweeping *conditional* reductions.

Status: **proved for $n\le 3$ (klt, lc, slc); open for every $n\ge 4$** except the special classes below.

## 4. Partial Results / Verified Cases

- **Dimension $\le 2$:** classical (Enriques–Kodaira); $12K_X$ is base-point free for minimal surfaces of nonnegative Kodaira dimension.
- **Dimension $3$:** Miyaoka (1987–88, $\nu=1$ and $\kappa\ge 0$), Kawamata (*Invent. Math.* 108, 1992) for minimal threefolds; Keel–Matsuki–McKernan (*Duke Math. J.* 75, 1994) for log pairs; Fujino (*Duke Math. J.* 102, 2000) for semi-log-canonical threefolds.
- **$\nu = n$ (big case), any $n$:** immediate from the Kawamata–Shokurov basepoint-free theorem.
- **$\nu = 0$, any $n$:** Nakayama (2004) for klt; Kawamata (*Amer. J. Math.* 135, 2013) and Gongyo for log canonical pairs — $K_X+\Delta\sim_{\mathbb{Q}}0$ effectively.
- **Maximal Albanese dimension, any $n$:** if the Albanese map $a:X\to \mathrm{Alb}(X)$ is generically finite onto its image, abundance holds — Campana–Koziarz–Păun (*Bull. SMF* 140, 2012), Fujino (*Proc. Japan Acad.* 89, 2013).
- **Uniruled / $\kappa=-\infty$ direction:** if $X$ is uniruled, $K_X$ is not pseudo-effective (Boucksom–Demailly–Păun–Peternell, *J. Algebraic Geom.* 22, 2013), so no minimal model exists — abundance is vacuous there.
- **Reduction results:** Hacon–Xu (*Ann. of Math.* 177, 2013) reduce slc abundance to the lc case in the same dimension; Fujino–Gongyo reduce lc to klt; Gongyo–Lehmann (*Compositio* 149, 2013) reduce abundance in dimension $n$ to nonvanishing plus abundance for the fibers of the Iitaka-type reduction map.
- **Fourfolds:** known for $\nu\in\{0,4\}$; the log canonical case reduces to the klt case, and the remaining open range is $\nu\in\{1,2,3\}$.
- **Extra structure:** varieties with a nonzero holomorphic form / large $\pi_1$-type hypotheses (Lazić–Peternell, "Abundance for varieties with many differential forms", *Algebr. Geom.* 5, 2018).

## 5. Principal Obstacles

- **Nonvanishing has no cohomological handle.** For $0<\nu<n$ the divisor $K_X+\Delta$ is not big, so Kawamata–Viehweg vanishing $H^i(X,K_X+\lceil D\rceil)=0$ ($D$ nef and big) does not apply. Every standard proof of effectivity — Riemann–Roch plus vanishing — collapses.
- **No induction on dimension.** Restricting to a divisor $S$ changes $\nu$ unpredictably; the adjoint $(K_X+\Delta+S)|_S$ need not be nef, and extension theorems require a big component that is absent when $\nu<n$.
- **Numerical vs. effective gap.** $\nu$ is an intersection-theoretic invariant, $\kappa$ a cohomological one. Bridging them requires producing sections from purely numerical data — exactly what fails for general nef line bundles: the Atiyah ruled surface (Section 10) carries a nef $D$ with $\nu(D)=1$, $\kappa(D)=0$. Only the *adjoint* nature of $K_X+\Delta$ can rule this out, and no current technique uses it in the non-big range.
- **Positive characteristic tools do not lift.** Miyaoka's threefold proof used Frobenius and foliation techniques on $\Omega^1_X$; the resulting generic semipositivity statements are too weak in dimension $\ge 4$, where the Bogomolov-type inequalities give no control on the Iitaka fibration.
- **Analytic route stalls on regularity.** Singular metrics with semipositive curvature exist on nef $K_X$ by definition, but converting a metric with vanishing Lelong numbers into holomorphic sections requires an $L^2$ extension across a nonalgebraic locus; the closedness/openness arguments of Demailly–Hacon–Păun require positivity that $\nu<n$ denies.

## 6. The Gap

Everything proved lives at the two ends of the range or under extra structure. The precise boundary:

- **Proved:** $n\le 3$ (all $\nu$); $\nu\in\{0,n\}$ (all $n$); maximal Albanese dimension; slc/lc $\Rightarrow$ klt reductions.
- **Open:** klt pairs with $n\ge 4$ and $0<\nu<n$.

The single step to be crossed is **Nonvanishing in the intermediate range**: given a klt pair with $K_X+\Delta$ nef and $0<\nu<n$, produce one effective divisor $D\sim_{\mathbb{Q}} m(K_X+\Delta)$. Gongyo–Lehmann and Lazić–Peternell show that once $\kappa\ge 0$ is known in all dimensions $\le n$, the passage from $\kappa\ge0$ to $\kappa=\nu$ and then to semi-ampleness follows by induction on the Iitaka fibration. So abundance is, modulo established machinery, exactly the nonvanishing conjecture.

## 7. Current Research (as of June 2026)

- **Generalised abundance (Lazić–Peternell).** The programme "On generalised abundance, I–II" (*Publ. RIMS* 56, 2020; *Peking Math. J.* 3, 2020) studies $K_X+\Delta+tL$ for nef $L$ and proves abundance under a generalised nonvanishing hypothesis; the technique replaces induction on $n$ by induction on $t$-thresholds. Continued in work with Han, Liu and Tsakanikas on generalised pairs. *(frontier — verify current dimension-4 claims)*
- **Generalised pairs and boundedness (Birkar's school).** Boundedness of complements and generalised log canonical thresholds give effective statements ("$m$ bounded") that could turn abundance into a finite check on bounded families. Cambridge/Warwick/Tsinghua groups.
- **Analytic MMP.** Demailly's programme via singular Kähler–Einstein metrics and transcendental MMP (Cao–Höring, Das–Hacon in the Kähler category); abundance for compact Kähler threefolds is now known (Campana–Höring–Peternell, *Ann. Sci. ENS*, 2016 and later work).
- **Foliated abundance.** Cascini–Spicer and Spicer–Svaldi have proved abundance for rank-one and rank-two foliations on threefolds; the foliated case feeds back into the classical one via the algebraic-integrability results of Ascher–Braun–Druel–Höring et al. *(frontier — verify)*
- **Characteristic $p$ and mixed characteristic.** Bernasconi, Hacon, Patakfalvi, Witaszek prove abundance for threefolds over $\overline{\mathbb{F}_p}$ ($p>3$); the techniques (Frobenius trace, $F$-singularities) are being tested in dimension 4.

## 8. Future Work

- Prove **Nonvanishing** for klt pairs in dimension 4 with $\nu\in\{1,2,3\}$; this is the field's stated first target (Kawamata, Fujino, Lazić–Peternell all isolate it).
- Develop **canonical bundle formulae with moduli parts** strong enough that positivity of the moduli $\mathbf{M}$-part on the base of the Iitaka fibration is semi-ample (the "Prokhorov–Shokurov b-semi-ampleness conjecture"), which would complete the induction step.
- Push **generalised nonvanishing** for $K_X+\Delta+L$: Lazić–Peternell argue this weaker-looking statement is more amenable because $L$ supplies positivity absent from $K_X+\Delta$.
- Use **hyperbolicity/Albanese methods** beyond maximal Albanese dimension: prove abundance when the Albanese fibers have small dimension, then induct.
- Combine **analytic** $L^2$-extension with **boundedness of complements** to get effectivity of $m$ in $|m(K_X+\Delta)|$, converting the conjecture into a bounded-family verification.

## 9. Key References

- **[Foundational]** Y. Kawamata, K. Matsuda, K. Matsuki. *Introduction to the Minimal Model Problem.* In: Algebraic Geometry, Sendai 1985, Adv. Stud. Pure Math. 10, North-Holland, 1987.
- **[Foundational]** Y. Miyaoka. *Abundance conjecture for 3-folds: case $\nu=1$.* Compositio Mathematica 68 (1988), 203–220.
- **[Foundational]** Y. Kawamata. *Abundance theorem for minimal threefolds.* Inventiones Mathematicae 108 (1992), 229–246. [DOI](https://doi.org/10.1007/bf02100604)
- **[Foundational]** S. Keel, K. Matsuki, J. McKernan. *Log abundance theorem for threefolds.* Duke Mathematical Journal 75 (1994), 99–119; Correction, Duke Math. J. 122 (2004), 625–630. [DOI](https://doi.org/10.1215/s0012-7094-94-07504-2)
- **[Foundational]** N. Nakayama. *Zariski-decomposition and Abundance.* MSJ Memoirs 14, Mathematical Society of Japan, 2004. [DOI](https://doi.org/10.2969/msjmemoirs/014010000)
- **[SOTA]** C. Birkar, P. Cascini, C. D. Hacon, J. McKernan. *Existence of minimal models for varieties of log general type.* Journal of the AMS 23 (2010), 405–468. [DOI](https://doi.org/10.1090/s0894-0347-09-00649-3)
- **[SOTA]** C. D. Hacon, C. Xu. *Existence of log canonical closures.* Inventiones Mathematicae 192 (2013), 161–195. [DOI](https://doi.org/10.1007/s00222-012-0409-0)
- **[SOTA]** F. Campana, V. Koziarz, M. Păun. *Numerical character of the effectivity of adjoint line bundles.* Annales de l'Institut Fourier 62 (2012), 107–119. [DOI](https://doi.org/10.5802/aif.2701)
- **[SOTA]** Y. Gongyo, B. Lehmann. *Reduction maps and minimal model theory.* Compositio Mathematica 149 (2013), 295–308. [DOI](https://doi.org/10.1112/s0010437x12000553)
- **[SOTA]** V. Lazić, T. Peternell. *On generalised abundance, I.* Publications of RIMS 56 (2020), 353–389.
- **[SOTA]** F. Campana, A. Höring, T. Peternell. *Abundance for Kähler threefolds.* Annales Scientifiques de l'ÉNS 49 (2016), 971–1025. [DOI](https://doi.org/10.24033/asens.2301)
- **[Survey]** O. Fujino. *Foundations of the Minimal Model Program.* MSJ Memoirs 35, Mathematical Society of Japan, 2017. [DOI](https://doi.org/10.2969/msjmemoirs/035010000)
- **[Survey]** J. Kollár, S. Mori. *Birational Geometry of Algebraic Varieties.* Cambridge Tracts in Mathematics 134, Cambridge University Press, 1998.
- **[Survey]** C. D. Hacon, J. McKernan. *Flips and flops.* Proceedings of the ICM, Hyderabad, 2010. [DOI](https://doi.org/10.1142/9789814324359_0062)

## 10. Worked Example / Concrete Special Case

**(a) Why "nef" alone is not enough.** Let $E$ be an elliptic curve and $\mathcal{E}$ the unique nonsplit extension
$$0\to\mathcal{O}_E\to\mathcal{E}\to\mathcal{O}_E\to 0$$
(Atiyah). Put $X=\mathbb{P}(\mathcal{E})\xrightarrow{\pi}E$, a ruled surface, and let $C_0$ be the section with $\mathcal{O}_X(C_0)=\mathcal{O}_{\mathbb{P}(\mathcal{E})}(1)$. Then
$$C_0^2=\deg\mathcal{E}=0,\qquad C_0\cdot f=1\ (f=\text{fiber}),$$
and $C_0$ is nef (Atiyah: $\mathcal{E}$ is semistable with no quotient of negative degree). So
$$\nu(X,C_0)=1\quad\text{since } C_0\cdot f>0,$$
but $h^0(X,mC_0)=h^0(E,\mathrm{Sym}^m\mathcal{E})=1$ for all $m\ge0$, because $\mathrm{Sym}^m\mathcal{E}$ is again an iterated nonsplit self-extension of $\mathcal{O}_E$. Hence $\kappa(X,C_0)=0<1=\nu$, and $C_0$ is **not semi-ample**: the only member of $|mC_0|$ is $mC_0$ itself, so the base locus contains $C_0$ forever.

This is the exact failure mode abundance forbids for log canonical divisors. Note $X$ is a ruled surface, so $K_X$ is *not* pseudo-effective ($-K_X = 2C_0 + \pi^*(\det\mathcal{E})^{-1} \equiv 2C_0$ is nef here) — consistent with the conjecture.

**(b) A case where abundance holds, explicitly.** Let $S\to\mathbb{P}^1$ be a minimal properly elliptic surface with a relatively minimal elliptic fibration $g$ and no multiple fibers, with generic fiber $F$. The canonical bundle formula gives
$$K_S \;=\; g^*\!\left(K_{\mathbb{P}^1}+\det\, g_*\omega_{S/\mathbb{P}^1}\right)\;=\;g^*L,\qquad \deg L = -2+\chi(\mathcal{O}_S).$$
If $\chi(\mathcal{O}_S)\ge 3$ then $\deg L>0$, so $L$ is ample on $\mathbb{P}^1$ and $K_S=g^*L$ is semi-ample by construction. Numerically, $K_S^2=0$ and $K_S\cdot H>0$ for ample $H$, so $\nu(S,K_S)=1$; and $h^0(mK_S)=h^0(\mathbb{P}^1,mL)=m\deg L+1$ grows linearly, so $\kappa=1=\nu$. Abundance holds, and the Iitaka fibration is $g$ itself.

The contrast between (a) and (b) is the whole content of the conjecture: a nef divisor may have $\kappa<\nu$, but a nef *log canonical* divisor is predicted never to — and in dimension $\ge 4$ with $0<\nu<n$ nobody knows how to produce the fibration $g$ of case (b).

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*