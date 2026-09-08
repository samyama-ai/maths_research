---
id: 03-geometry/fujita-conjecture
title: "Fujita Conjecture"
topic: 03-geometry
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Fujita Conjecture

> **Topic:** Algebraic & Differential Geometry · **ID:** `03-geometry/fujita-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Let $X$ be a smooth complex projective variety of dimension $n$, let $K_X$ be its canonical bundle, and let $L$ be an ample line bundle on $X$. Fujita conjectured:

- **(Freeness)** $K_X + mL$ is globally generated (base-point free) for every $m \ge n+1$.
- **(Very ampleness)** $K_X + mL$ is very ample for every $m \ge n+2$.

"Globally generated" means the evaluation map $H^0(X, K_X+mL)\otimes \mathcal{O}_X \to K_X+mL$ is surjective, i.e. the linear system has no base points. "Very ample" means the induced map to $\mathbb{P}H^0(X,K_X+mL)^\vee$ is a closed embedding.

A complete proof must handle arbitrary $n$, arbitrary $X$, and arbitrary ample $L$, with **no** dependence on numerical invariants of $L$ (such as $L^n$) — that uniformity is the whole content. A disproof requires one explicit $(X,L,m)$ with $m\ge n+1$ and a base point of $|K_X+mL|$ (or $m \ge n+2$ and failure of embedding). Both bounds are sharp: $X=\mathbb{P}^n$, $L=\mathcal{O}(1)$ gives $K_X+mL=\mathcal{O}(m-n-1)$, free exactly for $m\ge n+1$ and very ample exactly for $m\ge n+2$.

## 2. Mathematical Foundations

Write $\mathcal{O}_X(D)$ for the line bundle of a divisor $D$; $\equiv$ denotes numerical equivalence. $L$ is **nef** if $L\cdot C\ge 0$ for all curves $C$, **ample** if $L^{\dim V}\cdot V>0$ for all subvarieties $V$ (Nakai–Moishezon).

**Multiplier ideals.** For an effective $\mathbb{Q}$-divisor $D$ and a log resolution $\mu: X'\to X$ with $K_{X'} = \mu^*(K_X+D) + \sum a_i E_i$,
$$\mathcal{J}(X,D) \;=\; \mu_*\mathcal{O}_{X'}\!\left(\textstyle\sum_i \lceil a_i \rceil E_i\right)\subseteq \mathcal{O}_X .$$
The **log canonical threshold** at $x$ is $\mathrm{lct}_x(D)=\sup\{c>0: \mathcal{J}(X,cD)_x=\mathcal{O}_{X,x}\}$.

**Nadel vanishing.** If $N$ is a line bundle with $N - D$ nef and big, then
$$H^i\!\left(X,\; K_X+N \otimes \mathcal{J}(X,D)\right)=0 \quad \text{for } i>0 .$$

The standard strategy: to free a point $x$, build $D \equiv cL$ with $c<m$ such that $\mathcal{J}(X,D)$ cuts out exactly $\{x\}$ near $x$ (an *isolated log canonical centre*). Then $0\to K_X+mL\otimes\mathcal{J} \to K_X+mL \to \mathbb{C}_x\to 0$ plus Nadel vanishing gives surjectivity of $H^0(K_X+mL)\to\mathbb{C}_x$, i.e. $x$ is not a base point.

**Producing $D$.** By Riemann–Roch and asymptotic vanishing, $h^0(X,kL)\sim \frac{L^n}{n!}k^n$, so one can find $D_k\in|kL|$ with $\mathrm{mult}_x D_k > kn(L^n)^{-1/n}$-type bounds; hence $c\approx n/ (L^n)^{1/n}$. When $L^n=1$ this gives $c \approx n$, which is why the conjectural threshold $m=n+1$ is exactly at the edge and why singularity-of-the-generic-divisor arguments alone do not close the gap.

**Kawamata–Viehweg vanishing.** $H^i(X,K_X+N)=0$ for $i>0$ if $N$ is nef and big; the multiplier-ideal version above is its refinement, and the whole subject is an application of the minimal model program's vanishing package.

**Fujita's numerical version (weaker, also open in general):** $K_X+mL$ free for $m\ge n+1$ should follow from any statement bounding $\mathrm{lct}$ of divisors in $|kL|$ uniformly in $L$.

## 3. History & State of the Art (SOTA)

Takao Fujita posed the conjecture in *On polarized manifolds whose adjoint bundles are not semipositive* (Algebraic Geometry, Sendai 1985; Adv. Stud. Pure Math. 10, 1987), where he classified pairs with $K_X+(n+1)L$ not nef. The prototype is the classical fact that on a curve ($n=1$) $K_X+2L$ is free and $K_X+3L$ very ample, by Riemann–Roch.

Milestones:

- **1988** — Reider's Bogomolov-instability method settles $n=2$ completely.
- **1993** — Ein–Lazarsfeld prove freeness for $n=3$ ($m\ge 4$), introducing the multiplier-ideal/lct machinery that has dominated since.
- **1993** — Kollár gives the first *effective* bound in all dimensions: $K_X+mL$ free for $m\ge 2(n+2)!$ (roughly factorial).
- **1993** — Demailly proves $2K_X+12n^nL$ very ample, an analytic (Monge–Ampère / $L^2$-estimate) route.
- **1995** — Angehrn–Siu reduce the bound to the quadratic $m\ge \tfrac12(n^2+n)+1$ via analytic cutting-down of log canonical centres. This remains the standard general theorem.
- **1997** — Kawamata proves $n=4$ freeness ($m\ge 5$); Helmke gives an independent inductive treatment.
- **2002** — Heier obtains sub-quadratic effective bounds (order $n^{4/3}$ up to constants) using Siu's effective Matsusaka theorem.
- **2015–2020** — Ye–Zhu prove $n=5$ freeness ($m\ge 6$).

Very ampleness is proven only for $n\le 2$; for $n \ge 3$ even $n=3$ very ampleness ($m\ge5$) is open in full generality.

## 4. Partial Results / Verified Cases

| Case | Result | Source |
|---|---|---|
| $n=1$ | Free $m\ge2$, very ample $m\ge3$ | Riemann–Roch |
| $n=2$ | Free $m\ge3$, very ample $m\ge4$ | Reider (1988) |
| $n=3$ | Free $m\ge4$; very ampleness open | Ein–Lazarsfeld (1993) |
| $n=4$ | Free $m\ge5$ | Kawamata (1997), Helmke (1999) |
| $n=5$ | Free $m\ge6$ | Ye–Zhu (2015/2020) |
| $n\ge6$ | Free for $m\ge \tfrac12(n^2+n)+1$ | Angehrn–Siu (1995) |
| $n\ge6$, asymptotic | Free for $m = O(n^{4/3})$ | Heier (2002) |
| Toric $X$ (any $n$) | Full conjecture, freeness and very ampleness, including singular toric with $\mathbb{Q}$-Gorenstein hypotheses | Fujino (2003), Payne (2006), Mustață |
| Abelian varieties | $K_X=\mathcal{O}_X$; $mL$ free for $m\ge2$, very ample for $m\ge3$ | Lefschetz |
| $L^n$ large | Freeness for $m\ge n+1$ holds once $L^n \gg 0$ relative to $n$ (Ein–Lazarsfeld–Nakamaye type separation) | Ein–Lazarsfeld (1993) |
| $L$ very ample already | $K_X+mL$ free for $m\ge n+1$ by Castelnuovo–Mumford regularity | classical |
| Log/klt pairs | $K_X+\Delta+mL$ free for $m\ge\tfrac12(n^2+n)+1$ (Angehrn–Siu extends); dimension-$\le3$ log versions by Fujino | Kollár, Fujino |

Computationally: on toric varieties the conjecture reduces to a lattice-polytope statement checkable by integer programming, and has been machine-verified for large families of reflexive polytopes in $n\le 4$.

## 5. Principal Obstacles

- **The lct deficit.** Constructing $D\equiv cL$ singular enough at $x$ costs $c\sim n/(L^n)^{1/n}$; when $L^n=1$ (e.g. $\mathcal{O}(1)$ on $\mathbb{P}^n$) this consumes essentially the whole budget $m-1=n$, leaving no slack for the *positivity* needed in Nadel vanishing. The method is critical exactly at the conjectural bound.
- **Cutting down log canonical centres.** Angehrn–Siu's induction lowers the dimension of the minimal lc centre $Z$ one step at a time, and each step spends a multiplicative factor $\sim \dim Z$ of $L$. Summing $1+2+\dots+n$ produces the quadratic bound. Making each step cost $O(1)$ requires a *uniform* volume lower bound $ (L|_Z)^{\dim Z}\ge 1$ for subvarieties $Z$ — true for the top-dimensional case but not controllable inductively because $Z$ is singular and $L|_Z$'s sections do not extend.
- **Extension failure.** The step from $H^0(Z,\cdot)$ back to $H^0(X,\cdot)$ needs a surjectivity (Ohsawa–Takegoshi / Kawamata subadjunction) statement on a possibly non-normal, non-reduced centre. Subadjunction ($K_Z+\Delta_Z \le (K_X+D)|_Z$ with $\Delta_Z$ effective) exists (Kawamata 1998) but loses effectivity.
- **Very ampleness is strictly harder.** Separating tangent vectors requires an lc centre of multiplicity $\ge2$ at a point plus separation of two moving points, and the two constructions interact; no analogue of Reider's rank-2 Bogomolov instability exists in dimension $\ge3$, since Bogomolov's inequality is a surface phenomenon.
- **No characteristic-$p$ or numerical shortcut.** Frobenius/test-ideal methods give freeness bounds but with worse constants; positivity-of-direct-image (Viehweg, Popa–Schnell) arguments give asymptotic statements, not the sharp linear bound.

## 6. The Gap

Proven: freeness for $n\le5$ and for $m\gtrsim \tfrac12 n^2$ (or $O(n^{4/3})$) in general. Conjectured: freeness at $m=n+1$ for all $n$.

The precise missing step is an **effective inductive subadjunction with $O(1)$ loss**: given a minimal log canonical centre $Z\subseteq X$ of the pair $(X,cL)$ at $x$, produce a divisor on $Z$ isolating $x$ using only $(\dim Z + \varepsilon)$-many copies of $L|_Z$, *and* lift the resulting section to $X$. Present technology loses a factor per dimension step. Equivalently: prove the uniform bound
$$\mathrm{lct}_x\big(|kL|\big)\;\le\; \frac{n}{k}\cdot\frac{1}{(L^n)^{1/n}} \quad\text{for suitable }D_k,$$
together with vanishing that tolerates the residual positivity $ (m-c)L$ being merely nef rather than ample-with-slack. For very ampleness, the gap is total in $n\ge3$: no dimension beyond 2 is known.

## 7. Current Research (as of June 2026)

- **Effective non-vanishing and lc centres.** Continuation of the Kawamata–Helmke–Ye–Zhu line, pushing the case-by-case analysis toward $n=6$; the combinatorics of possible minimal lc centre configurations grows sharply and is the current bottleneck *(frontier — verify)*.
- **Positivity of direct images.** Groups working on Hodge-module positivity (Popa, Schnell, and collaborators) supply generic global generation for pushforwards $f_*\omega^{\otimes m}$, giving Fujita-type statements for fibred and irregular varieties.
- **Generic vanishing / irregular varieties.** For $X$ with maximal Albanese dimension, generic-vanishing methods (Pareschi–Popa) recover the conjectural linear bound; extending to arbitrary $X$ is open.
- **Analytic school.** Ohsawa–Takegoshi extension with optimal constants (Guan–Zhou, Błocki) is being applied to make the Angehrn–Siu induction lossless; the difficulty is the singular metric on the centre *(frontier — verify)*.
- **Singular and log settings.** Fujino's programme extends freeness statements to log canonical and semi-log-canonical pairs, relevant to moduli compactifications.
- **Positive characteristic.** Test-ideal analogues of multiplier ideals give freeness statements in dimension $\le3$ over $\overline{\mathbb{F}_p}$ (Cascini, Tanaka, Witaszek), but with non-sharp bounds.

## 8. Future Work

- Prove an $O(1)$-loss version of Kawamata subadjunction for minimal lc centres; this alone would give a linear bound $m \ge Cn$ and plausibly $n+1$.
- Establish a lower bound $\mathrm{vol}(L|_Z)\ge 1$ for all lc centres $Z$ of $(X,cL)$ with $c<n$ — a Fano-type boundedness statement.
- Settle very ampleness for $n=3$ ($K_X+5L$), the smallest genuinely open very-ampleness case, likely via Reider-type methods for rank-3 sheaves.
- Develop a purely toric-degeneration proof: the toric case is fully known, so a degeneration argument preserving base-point freeness would be decisive.
- Search for counterexamples among varieties with $L^n=1$ and $\mathrm{Pic}=\mathbb{Z}L$ (the numerically tightest configurations), including weighted hypersurfaces.

## 9. Key References

- **[Foundational]** T. Fujita. *On polarized manifolds whose adjoint bundles are not semipositive.* In: Algebraic Geometry, Sendai 1985, Advanced Studies in Pure Mathematics 10, North-Holland, 1987, pp. 167–178.
- **[Foundational]** I. Reider. *Vector bundles of rank 2 and linear systems on algebraic surfaces.* Annals of Mathematics 127 (1988), 309–316. [DOI](https://doi.org/10.2307/2007055)
- **[Foundational]** L. Ein, R. Lazarsfeld. *Global generation of pluricanonical and adjoint linear series on smooth projective threefolds.* Journal of the American Mathematical Society 6 (1993), 875–903. [DOI](https://doi.org/10.1090/s0894-0347-1993-1207013-5)
- **[Foundational]** J. Kollár. *Effective base point freeness.* Mathematische Annalen 296 (1993), 595–605. [DOI](https://doi.org/10.1007/bf01445123)
- **[Foundational]** J.-P. Demailly. *A numerical criterion for very ample line bundles.* Journal of Differential Geometry 37 (1993), 323–374. [DOI](https://doi.org/10.4310/jdg/1214453680)
- **[SOTA]** U. Angehrn, Y.-T. Siu. *Effective freeness and point separation for adjoint bundles.* Inventiones Mathematicae 122 (1995), 291–308. [DOI](https://doi.org/10.1007/bf01231446)
- **[SOTA]** Y. Kawamata. *On Fujita's freeness conjecture for 3-folds and 4-folds.* Mathematische Annalen 308 (1997), 491–505. [DOI](https://doi.org/10.1007/s002080050085)
- **[SOTA]** S. Helmke. *On Fujita's conjecture.* Duke Mathematical Journal 88 (1997), 201–216.
- **[SOTA]** G. Heier. *Effective freeness of adjoint line bundles.* Documenta Mathematica 7 (2002), 31–42. [DOI](https://doi.org/10.4171/dm/116)
- **[SOTA / Recent]** F. Ye, Z. Zhu. *On Fujita's freeness conjecture in dimension 5.* (arXiv:1511.06126; published version in Advances in Mathematics, 2020.). [DOI](https://doi.org/10.1016/j.aim.2020.107210)
- **[Special case]** O. Fujino. *Notes on toric varieties from Mori theoretic viewpoint.* Tohoku Mathematical Journal 55 (2003), 551–564. [DOI](https://doi.org/10.2748/tmj/1113247130)
- **[Special case]** S. Payne. *Fujita's very ampleness conjecture for singular toric varieties.* Tohoku Mathematical Journal 58 (2006), 447–459. [DOI](https://doi.org/10.2748/tmj/1163775140)
- **[Survey]** R. Lazarsfeld. *Positivity in Algebraic Geometry I & II.* Ergebnisse der Mathematik 48–49, Springer, 2004. (Chapters 9–11 cover multiplier ideals and Fujita-type results.). [DOI](https://doi.org/10.1007/978-3-642-18810-7)
- **[Survey]** Y. Kawamata. *On effective non-vanishing and base-point-freeness.* Asian Journal of Mathematics 4 (2000), 173–181. [DOI](https://doi.org/10.4310/ajm.2000.v4.n1.a11)

## 10. Worked Example / Concrete Special Case

**(a) Sharpness on $\mathbb{P}^n$.** Take $X=\mathbb{P}^n$, $L=\mathcal{O}(1)$, $K_X=\mathcal{O}(-n-1)$. Then
$$K_X+mL=\mathcal{O}(m-n-1).$$
$\mathcal{O}(d)$ is globally generated iff $d\ge0$ and very ample iff $d\ge1$. So freeness holds exactly for $m\ge n+1$ and very ampleness exactly for $m\ge n+2$: the conjectured constants cannot be lowered by $1$.

**(b) Reider's proof of the surface case $n=2$.** Let $S$ be a smooth projective surface, $L$ ample, and set $L'=3L$; we show $|K_S+L'|$ is base-point free.

Reider's theorem: if $L'$ is nef with $L'^2\ge5$ and $x\in S$ is a base point of $|K_S+L'|$, then there exists an effective divisor $D\ni x$ with
$$L'\cdot D=0,\; D^2\in\{-1,-2\}\qquad\text{or}\qquad L'\cdot D=1,\; D^2\in\{0,-1\}.$$

Check the hypothesis: $L$ ample on a surface gives $L^2\ge1$ (integer, positive by Nakai–Moishezon), so
$$L'^2=(3L)^2=9L^2\ge 9\ge5. \checkmark$$

Now suppose such a $D$ exists. $D$ is a nonzero effective divisor and $L$ is ample, so $L\cdot D\ge1$, hence
$$L'\cdot D = 3\,(L\cdot D)\ \ge\ 3 .$$
But Reider forces $L'\cdot D\in\{0,1\}$ — contradiction. Therefore $|K_S+3L|$ has no base point, which is exactly Fujita freeness for $n=2$.

The same argument with $L'=4L$ gives $L'\cdot D=4(L\cdot D)\ge4$, while Reider's separation criterion for very ampleness allows only $L'\cdot D\le 2$; hence $K_S+4L$ is very ample, the $n=2$ very-ampleness statement.

**(c) Why this does not generalize.** The engine is Bogomolov's inequality $c_1^2\le 4c_2$ for unstable rank-2 bundles, which produces the divisor $D$ from a Cayley–Bacharach extension. In dimension $\ge3$ the analogous destabilizing object is a rank-$n$ reflexive sheaf whose instability yields a subsheaf of arbitrary rank, and no numerical inequality pins down the resulting subvariety's degree against $L$ — precisely the obstacle described in Section 5. Substituting multiplier ideals for Reider recovers $m\ge4$ when $n=3$ (Ein–Lazarsfeld) but degrades to $\tfrac12(n^2+n)+1$ as $n$ grows.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*