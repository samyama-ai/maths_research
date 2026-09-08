---
id: 01-number-theory/dynamical-lehmer-conjecture
title: "Northcott and Lehmer Problems for Dynamical Heights"
topic: 01-number-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Northcott and Lehmer Problems for Dynamical Heights

> **Topic:** Number Theory · **ID:** `01-number-theory/dynamical-lehmer-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Let $\varphi: \mathbb{P}^1 \to \mathbb{P}^1$ be a morphism of degree $d \ge 2$ defined over $\overline{\mathbb{Q}}$, and let $\hat{h}_\varphi$ be its canonical (Call–Silverman) height. Two linked questions:

**(A) Dynamical Lehmer problem.** Is there a constant $C(\varphi) > 0$ such that for every $\alpha \in \overline{\mathbb{Q}}$ that is *not* $\varphi$-preperiodic,
$$\hat{h}_\varphi(\alpha) \;\ge\; \frac{C(\varphi)}{[\mathbb{Q}(\alpha):\mathbb{Q}]}\,?$$
For $\varphi(z) = z^d$ one has $\hat h_\varphi = h$ (the absolute Weil height) and the statement is exactly Lehmer's 1933 problem on Mahler measures. A complete solution requires either a proof valid for all $\varphi$, or a single $\varphi$ together with a sequence $\alpha_i$ of non-preperiodic points with $D_i\hat h_\varphi(\alpha_i) \to 0$, where $D_i = [\mathbb{Q}(\alpha_i):\mathbb{Q}]$.

**(B) Dynamical Northcott problem.** For which fields $L \subseteq \overline{\mathbb{Q}}$ of infinite degree over $\mathbb{Q}$, and which $\varphi$, does $\hat h_\varphi$ have the **Northcott property** on $L$: for every $B$, the set $\{\alpha \in L : \hat h_\varphi(\alpha) \le B\}$ is finite? Equivalently, what is the *Northcott number*
$$\mathcal{N}_\varphi(L) \;=\; \inf\{B > 0 : \\#\{\alpha \in L: \hat h_\varphi(\alpha) \le B\} = \infty\}\,?$$
Over a number field the Northcott property holds unconditionally (Northcott 1950; Call–Silverman 1993); the open problem is the infinite-degree regime, and the *uniformity* of the finiteness in $\varphi$ within a family.

Question (A) is the quantitative refinement of (B) restricted to $L = \overline{\mathbb{Q}}$ graded by degree.

## 2. Mathematical Foundations

**Weil height.** For $\alpha \in \overline{\mathbb{Q}}$ with $[K:\mathbb{Q}] < \infty$, $\alpha \in K$,
$$h(\alpha) \;=\; \frac{1}{[K:\mathbb{Q}]}\sum_{v \in M_K} [K_v:\mathbb{Q}_v]\,\log^{+}|\alpha|_v ,$$
independent of $K$. If $\alpha$ has minimal polynomial $f \in \mathbb{Z}[x]$ of degree $D$ with Mahler measure $M(f) = |a_D|\prod \max(1,|\alpha_i|)$, then $h(\alpha) = \tfrac{1}{D}\log M(f)$.

**Canonical height (Call–Silverman).** For $\varphi$ of degree $d\ge 2$,
$$\hat h_\varphi(\alpha) \;=\; \lim_{n\to\infty} \frac{h(\varphi^n(\alpha))}{d^n},$$
the limit exists, $\hat h_\varphi = h + O(1)$, and it satisfies the functional equation
$$\hat h_\varphi(\varphi(\alpha)) = d\cdot \hat h_\varphi(\alpha).$$
Consequently $\hat h_\varphi(\alpha) = 0$ if and only if $\alpha \in \mathrm{PrePer}(\varphi,\overline{\mathbb{Q}})$.

**Local decomposition.** $\hat h_\varphi(\alpha) = \frac{1}{[K:\mathbb{Q}]}\sum_v [K_v:\mathbb{Q}_v]\,\hat\lambda_{\varphi,v}(\alpha)$, where $\hat\lambda_{\varphi,v}$ is the Green's function of the filled Julia set $K_v \subset \mathbb{A}^1(\mathbb{C}_v)$ (Berkovich analytification at nonarchimedean $v$), normalized by $\hat\lambda_{\varphi,v} = \log^{+}|\cdot|_v + O(1)$ and $\hat\lambda_{\varphi,v}\circ\varphi = d\,\hat\lambda_{\varphi,v}$.

**Equidistribution.** If $\hat h_\varphi(\alpha_i) \to 0$ with $\deg \alpha_i \to \infty$, the Galois orbits $\frac{1}{D_i}\sum_{\sigma}\delta_{\alpha_i^\sigma}$ converge weakly to the invariant measure $\mu_{\varphi,v}$ at every place (Baker–Rumely; Chambert-Loir; Favre–Rivera-Letelier). This is the dynamical analogue of Bilu's theorem.

**Special maps.** $\varphi$ is *exceptional/special* if it is conjugate to $z^{\pm d}$, to $\pm T_d$ (Chebyshev), or is a Lattès map $\varphi\circ\pi = \pi\circ\psi$ for an isogeny-type $\psi$ on an elliptic curve $E$ and $\pi = x$-coordinate map; then $\hat h_\varphi(x(P)) = c\cdot \hat h_E(P)$ with $\hat h_E$ the Néron–Tate height.

**Classical benchmarks.** Lehmer (1933): is $h(\alpha) \ge c/D$ for $\alpha$ not $0$ or a root of unity? Best known unconditional bound (Dobrowolski 1979, with Voutier's explicit constant):
$$h(\alpha) \;\ge\; \frac{c}{D}\left(\frac{\log\log D}{\log D}\right)^{3},\qquad c = \tfrac14 \text{ admissible for } D\ge 2 .$$

## 3. History & State of the Art (SOTA)

- **1933.** Lehmer asks for algebraic integers of small Mahler measure; finds $M = 1.17628\ldots$ from a degree-$10$ polynomial. No smaller value has been found in nearly a century of searching.
- **1950.** Northcott proves finiteness of points of bounded height and degree, and finiteness of periodic points of a morphism over a number field.
- **1971.** Smyth: nonreciprocal $\alpha$ satisfy $h(\alpha) \ge \frac{1}{D}\log\theta_0$, $\theta_0 = 1.3247\ldots$ (plastic number) — Lehmer for a large class.
- **1979–1996.** Dobrowolski's bound; Louboutin, Voutier, Cantor–Straus refinements; Amoroso–David extend to $\mathbb{G}_m^n$.
- **1993.** Call–Silverman construct $\hat h_\varphi$ for polarized dynamical systems, giving Northcott over number fields.
- **2001.** Bombieri–Zannier: Northcott property for $h$ on infinite extensions with bounded local degrees (e.g. $\mathbb{Q}^{(d)}$, the compositum of all degree-$\le d$ fields); Widmer (2011) and Checcoli–Fehm later widen the class.
- **2006–2009.** Baker's Green's-function lower bounds; Baker's function-field finiteness theorem; Benedetto's polynomial function-field bounds; Ingram's explicit bounds for $z^d+c$.
- **2007.** Silverman states the dynamical Lehmer conjecture in *The Arithmetic of Dynamical Systems* (Conjecture 3.25), and asks for a Dobrowolski-type dynamical bound.
- **2019–2021.** Looper obtains $abc$-conditional and unconditional lower bounds for polynomial canonical heights, linking Lehmer-type gaps to uniform boundedness of preperiodic points.

## 4. Partial Results / Verified Cases

- **Number fields, fixed degree.** For any $\varphi$ over a number field $K$, $\hat h_\varphi$ has the Northcott property on $\overline{\mathbb{Q}}$ restricted to bounded degree; explicit $C(\varphi, D)$ follow from Call–Silverman's effective comparison $|\hat h_\varphi - h| \le C_1(\varphi)$.
- **Bad reduction gives a uniform bound.** If $\varphi$ does *not* have potentially good reduction at some place $v$ (so $\mu_{\varphi,v}$ is not the Gauss-point mass), Baker's average-Green's-function estimate yields $\hat h_\varphi(\alpha) \ge C(\varphi) > 0$ for all non-preperiodic $\alpha$, with $C$ **independent of $\deg\alpha$** — far stronger than Lehmer. Lehmer-hard cases are precisely those with everywhere potentially good reduction, which includes $z^d$, $T_d$, and Lattès maps with everywhere-good reduction.
- **Unicritical polynomials.** Ingram (2009): for $\varphi_c(z) = z^d + c$ with $c \in \overline{\mathbb{Q}}$ not an algebraic integer, $\hat h_{\varphi_c}(\alpha) \ge C\,h(c)$ uniformly in $\deg\alpha$; for integral $c$ the problem persists.
- **Lattès maps.** Dynamical Lehmer for a Lattès map is equivalent to elliptic Lehmer for $\hat h_E$. Known: Laurent (1983) proved a Dobrowolski-type bound $\hat h_E(P) \gg D^{-1}(\log\log D/\log D)^{c}$ for CM curves; David–Hindry extended to CM abelian varieties; Masser (1989) gives $\hat h_E(P) \gg_E D^{-3-\varepsilon}$ (roughly) in the general case.
- **Power maps.** Smyth's nonreciprocal case; totally real $\alpha$ (Schinzel: $h(\alpha)\ge \tfrac12\log\frac{1+\sqrt5}{2}$, absolute); $\alpha$ with bounded number of nonzero coefficients; abelian extensions (Amoroso–Dvornicich: $h(\alpha)\ge \frac{\log 5}{12}$ for $\alpha\in\mathbb{Q}^{ab}$, no degree dependence).
- **Function fields.** Baker (2009): over $K = k(C)$, if $\varphi$ of degree $\ge2$ is non-isotrivial, then $\{\alpha : \hat h_\varphi(\alpha) \le B\}$ is finite for all $B$ — full Northcott without any degree restriction. Benedetto (2005) proved the polynomial case with explicit constants.
- **Computation.** For $\varphi = z^2$: Mahler measures verified to have no value in $(1, 1.17628)$ for all $\deg \le 44$ (Mossinghoff, Rhin, Wu, 2008) and for wide structured families beyond.

## 5. Principal Obstacles

- **No auxiliary-polynomial engine.** The Dobrowolski method rests on the Frobenius congruence $f(x)^p \equiv f(x^p) \bmod p$ — a group-theoretic fact special to $z \mapsto z^p$. A general $\varphi$ has no analogue: $\varphi$ and Frobenius do not commute, and there is no "$p$-th power map" in the dynamical category. Constructing a nonvanishing auxiliary function with high-order vanishing along a $\varphi$-orbit fails because orbits are not group-like and admit no interpolation determinant with controllable index.
- **Transcendence machinery has no dynamical target.** Elliptic/abelian Lehmer bounds come from linear forms in logarithms on a commutative group scheme. A general rational map has no algebraic group, so Baker–Wüstholz and Philippon's zero estimates are unavailable.
- **Equidistribution is qualitative.** The arithmetic equidistribution theorems say a small-height sequence equidistributes, but current effective versions (Petsche; Favre–Rivera-Letelier) give error terms of size $O(D^{-1/3}\log D)$-type, weaker than the $C/D$ the conjecture needs; the discrepancy inequality loses exactly the factor being sought.
- **The good-reduction wall.** All robust positive results exploit a place of bad reduction, where the Green's function is bounded below on a set of positive capacity. Everywhere-potentially-good-reduction maps have local Julia sets of capacity $1$ at every finite place, so the local contributions all vanish to first order and the product formula gives no leverage. This is exactly the class containing $z^d$.
- **Uniformity in $\varphi$.** Even where bounds exist, $C(\varphi)$ degenerates as $\varphi$ approaches the boundary of moduli space, obstructing family-uniform statements tied to the Morton–Silverman uniform boundedness conjecture.

## 6. The Gap

Proven: (i) full Northcott over number fields and over non-isotrivial function fields; (ii) degree-independent positive lower bounds whenever $\varphi$ has a place of genuinely bad reduction; (iii) $D^{-1}(\log\log D/\log D)^{3}$ for $\varphi = z^d$ and Dobrowolski-quality bounds for CM Lattès maps.

Conjectured: $C(\varphi)/D$ for *all* $\varphi$, in particular for every everywhere-potentially-good-reduction map.

The gap is a single structural step: producing, for a map with no bad place, a *global* arithmetic obstruction to a full Galois orbit clustering near the Julia set at every place simultaneously. For $z^d$ this obstruction is Frobenius; the missing object is its dynamical replacement — a functorial congruence relating $\varphi$ mod $\mathfrak{p}$ to the Frobenius action on the orbit, strong enough to force $\ge cD/\log D$ conjugates off the unit circle. Closing the gap for Lattès maps alone would already resolve the elliptic Lehmer conjecture in the non-CM case, itself open since Masser (1989).

## 7. Current Research (as of June 2026)

- **Berkovich potential theory.** Groups around Baker, Rumely, Favre, Rivera-Letelier and Fili pursue quantitative energy/mutual-energy estimates on $\mathsf{P}^{1,\mathrm{an}}_{\mathbb{C}_v}$; the aim is an effective equidistribution theorem with $O(D^{-1})$ discrepancy. *(frontier — verify)*
- **$abc$-conditional routes.** Looper's programme derives uniform lower bounds on $\hat h_\varphi$ for polynomials from $abc$ plus a "gap principle" for critical orbits; this also implies uniform boundedness of preperiodic points in families. Active at Cambridge/Brown.
- **Northcott numbers on infinite extensions.** Pazuki, Technau, Widmer, Pottmeyer and Checcoli–Fehm compute or bound $\mathcal{N}(L)$ for the Weil height on $\mathbb{Q}^{(d)}$, totally $p$-adic fields, and fields of bounded local degree; the dynamical analogue $\mathcal{N}_\varphi(L)$ for $z^d+c$ and Lattès maps is being developed. *(frontier — verify)*
- **Unlikely intersections.** Baker–DeMarco, DeMarco–Krieger–Ye and Ghioca–Tucker–Zhang techniques yield rigidity statements for simultaneously small height; these feed height-gap conjectures adjacent to Lehmer.
- **$p$-adic / Berkovich dynamical Dobrowolski.** Attempts to replace Frobenius by good-reduction dynamics on the residue tree, exploiting that $\varphi$ mod $\mathfrak p$ has $O(\mathfrak{p}^n)$-many periodic points. *(frontier — verify)*

## 8. Future Work

- Prove any bound of the shape $\hat h_\varphi(\alpha) \ge C(\varphi) D^{-A}$ with $A$ absolute, for all $\varphi$ of degree $2$ — currently open even for the family $z^2+c$, $c \in \mathbb{Z}$.
- Establish a dynamical Frobenius congruence: for good reduction at $\mathfrak p$ with residue field $\mathbb{F}_q$, control the interaction of $\varphi^n$ with $\sigma_{\mathfrak p}$ on $\mathrm{Gal}$-orbits.
- Settle non-CM elliptic Lehmer, thereby the Lattès case, presumably via improvements to isogeny estimates and Masser–Wüstholz-type bounds.
- Determine whether $\mathcal{N}_\varphi(L) > 0$ for $L$ the maximal totally $p$-adic field and $\varphi$ a non-special map.
- Push Mahler-measure searches past degree $50$ and to structured families (Salem numbers, interval polynomials) to test the $1.17628$ barrier.

## 9. Key References

- **[Foundational]** D. H. Lehmer. *Factorization of certain cyclotomic functions.* Annals of Mathematics 34 (1933), 461–479.
- **[Foundational]** D. G. Northcott. *Periodic points on an algebraic variety.* Annals of Mathematics 51 (1950), 167–177.
- **[Foundational]** G. Call, J. H. Silverman. *Canonical heights on varieties with morphisms.* Compositio Mathematica 89 (1993), 163–205.
- **[Foundational]** E. Dobrowolski. *On a question of Lehmer and the number of irreducible factors of a polynomial.* Acta Arithmetica 34 (1979), 391–401.
- **[Foundational]** C. J. Smyth. *On the product of the conjugates outside the unit circle of an algebraic integer.* Bulletin of the LMS 3 (1971), 169–175.
- **[SOTA]** M. Baker. *A lower bound for average values of dynamical Green's functions.* Mathematical Research Letters 13 (2006), 245–257.
- **[SOTA]** M. Baker. *A finiteness theorem for canonical heights attached to rational maps over function fields.* Journal für die reine und angewandte Mathematik 626 (2009), 205–233.
- **[SOTA]** R. Benedetto. *Heights and preperiodic points of polynomials over function fields.* International Mathematics Research Notices 2005, no. 62, 3855–3866.
- **[SOTA]** P. Ingram. *Lower bounds on the canonical height associated to the morphism $\phi(z)=z^d+c$.* Monatshefte für Mathematik 157 (2009), 69–89.
- **[SOTA]** N. R. Looper. *A lower bound on the canonical height for polynomials.* Mathematische Annalen 373 (2019), 1146–1163.
- **[SOTA]** E. Bombieri, U. Zannier. *A note on heights in certain infinite extensions of $\mathbb{Q}$.* Atti della Accademia Nazionale dei Lincei (Rend. Lincei Mat. Appl.) 12 (2001), 5–14.
- **[SOTA]** M. Widmer. *On certain infinite extensions of the rationals with Northcott property.* Monatshefte für Mathematik 162 (2011), 341–353.
- **[SOTA]** D. Masser. *Counting points of small height on elliptic curves.* Bulletin de la Société Mathématique de France 117 (1989), 247–265.
- **[Survey]** J. H. Silverman. *The Arithmetic of Dynamical Systems.* Graduate Texts in Mathematics 241, Springer, 2007 (Conjecture 3.25).
- **[Survey]** C. Smyth. *The Mahler measure of algebraic numbers: a survey.* In *Number Theory and Polynomials*, LMS Lecture Note Series 352, Cambridge University Press, 2008, 322–349.
- **[Survey]** M. Baker, R. Rumely. *Potential Theory and Dynamics on the Berkovich Projective Line.* AMS Surveys and Monographs 159, 2010.
- **[Computational]** M. Mossinghoff, G. Rhin, Q. Wu. *Minimal Mahler measures.* Experimental Mathematics 17 (2008), 451–458.

## 10. Worked Example / Concrete Special Case

**Case $\varphi(z) = z^2$.** Here $\hat h_\varphi = h$ exactly, and preperiodic points are $0,\infty$ and roots of unity. Take Lehmer's polynomial
$$L(x) = x^{10} + x^{9} - x^{7} - x^{6} - x^{5} - x^{4} - x^{3} + x + 1,$$
irreducible over $\mathbb{Q}$, with a unique root $\alpha_0 = 1.176280818\ldots$ outside the closed unit disc (a Salem number). Then $M(L) = \alpha_0$, $D = 10$, and
$$\hat h_\varphi(\alpha_0) = h(\alpha_0) = \frac{\log \alpha_0}{10} = \frac{0.1623576\ldots}{10} = 0.01623576\ldots$$
so $D\cdot \hat h_\varphi(\alpha_0) = 0.16236$. The conjecture asserts this product stays bounded away from $0$; no example beats $0.16236$ despite exhaustive search to degree $44$. Dobrowolski at $D = 10$ gives only $h \ge \tfrac{1}{4}\cdot 10^{-1}(\log\log 10/\log 10)^3 \approx 6\times 10^{-5}$ — a factor $\approx 270$ weaker than the truth, and the loss grows like $(\log D/\log\log D)^3$.

**Contrast: a bad-reduction map.** Take $\varphi(z) = z^2 + \tfrac{1}{p}$ over $\mathbb{Q}$. At $v = p$ we have $|1/p|_p = p > 1$, so the filled Julia set is $K_p = \{|z|_p \le p^{1/2}\}$-bounded and $\varphi$ has bad reduction. Ingram's theorem applies since $1/p$ is not an algebraic integer: there is $C > 0$ with $\hat h_\varphi(\alpha) \ge C\log p$ for *every* non-preperiodic $\alpha \in \overline{\mathbb{Q}}$, with no dependence on $[\mathbb{Q}(\alpha):\mathbb{Q}]$. The mechanism: at $p$, $\hat\lambda_{\varphi,p}$ is the Green's function of a Cantor Julia set of capacity $< 1$, so a positive proportion of any Galois orbit must escape, and the product formula converts that into a global lower bound.

**Why the hard case is hard.** Move to $c \in \mathbb{Z}$, say $\varphi(z) = z^2 - 1$. Now $\varphi$ has good reduction at every prime, every local Julia set has capacity $1$, every $\hat\lambda_{\varphi,v}$ vanishes on the closed unit disc for $v$ finite, and the entire lower bound must come from the archimedean place alone. There the only known input is potential theory on the Julia set of $z^2-1$ (the basilica), which is qualitative. No bound of the form $\hat h_{\varphi}(\alpha) \ge C/D$ is known for $z^2-1$; the smallest known nonzero values, e.g. from $\alpha$ with $\varphi^3(\alpha)$ small, sit near $10^{-2}$ at degree $8$ — consistent with the conjecture, but unproven.

**Lattès translation.** If $E/\mathbb{Q}$ has good reduction everywhere over some number field and $\varphi$ is the degree-$4$ Lattès map with $\varphi(x(P)) = x(2P)$, then $\hat h_\varphi(x(P)) = 2\hat h_E(P)$, and question (A) becomes: is $\hat h_E(P) \ge c(E)/[\mathbb{Q}(P):\mathbb{Q}]$? For non-CM $E$ the best unconditional bound remains polynomial of degree $> 1$ in $D$ — the same wall, in a different language.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*