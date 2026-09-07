---
id: 05-analysis/lusin-return-times
title: "Lusin's Return Times Theorem"
topic: 05-analysis
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Lusin's Return Times Theorem

> **Topic:** Real & Complex Analysis · **ID:** `05-analysis/lusin-return-times` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

"Lusin's Return Times Theorem" is the maximal, Lusin-conjecture-strength form of Bourgain's return times theorem: the demand that the return-times averages converge not merely pointwise for bounded data, but with a maximal-function bound strong enough to contain Carleson's theorem (Lusin's conjecture on a.e. convergence of Fourier series) as the special case of a circle rotation.

Let $(X,\mathcal{X},\mu,T)$ be an invertible measure-preserving system on a probability space. Fix $f \in L^p(X)$.

**(RT$_{p,q}$)** *There is a set $X_0 \subseteq X$ with $\mu(X_0)=1$ such that for every $x \in X_0$, every other measure-preserving system $(Y,\mathcal{Y},\nu,S)$, and every $g \in L^q(Y)$, the averages*
$$A_N(x,y) \;=\; \frac{1}{N}\sum_{n=1}^{N} f(T^n x)\, g(S^n y)$$
*converge for $\nu$-a.e. $y \in Y$.*

The two questions on the table:

1. **Range.** For which pairs $(p,q)$ does (RT$_{p,q}$) hold? Bourgain proved $(\infty,\infty)$; the target is the full range $p,q>1$.
2. **Lusin form.** Does the sampled maximal operator
$$\mathcal{C}f(x) \;=\; \sup_{(Y,S,g):\,\|g\|_{L^q}\le 1}\ \Big\|\sup_{N}\big|A_N(x,\cdot)\big|\Big\|_{L^{q,\infty}(Y)}$$
satisfy a weak-type bound $\mu\{\mathcal{C}f > \lambda\} \lesssim (\|f\|_p/\lambda)^p$? Equivalently (Lusin/Egorov form): for every $\varepsilon>0$ is there $E\subseteq X$ with $\mu(X\setminus E)<\varepsilon$ on which the convergence in (RT) is uniform over the whole class of admissible $(Y,S,g)$ with $\|g\|_q\le 1$?

A complete resolution means a proof of the weak-type bound for the claimed range, together with counterexamples pinning the boundary. Question 1 is settled in the region $1/p+1/q<3/2$ (Demeter–Lacey–Tao–Thiele, 2008) and known to fail at $p=q=1$ (Assani–Buczolich–Mauldin, 2005); the residual strip $1/p+1/q\ge 3/2$, $p,q>1$ is open.

## 2. Mathematical Foundations

**Good universal weights.** A sequence $a=(a_n)$ of complex numbers is a *good universal weight for the pointwise ergodic theorem in $L^q$* if for every measure-preserving system $(Y,\nu,S)$ and every $g\in L^q(\nu)$,
$$\lim_{N\to\infty}\frac1N\sum_{n=1}^N a_n\, g(S^n y)\quad\text{exists for }\nu\text{-a.e. }y.$$
Bourgain's return times theorem says: for $f\in L^\infty(X)$, the orbit sequence $a_n(x)=f(T^nx)$ is a good universal weight for $\mu$-a.e. $x$.

**Wiener–Wintner.** Taking $Y=\mathbb{T}=\mathbb{R}/\mathbb{Z}$, $S y = y+\theta$, $g(y)=e^{2\pi i y}$ reduces (RT) to the Wiener–Wintner theorem: for a.e. $x$,
$$\lim_{N\to\infty}\frac1N\sum_{n=1}^N f(T^nx)\,e^{2\pi i n\theta}\ \text{ exists for every }\theta\in\mathbb{T}.$$
The quantifier order — one null set, all $\theta$ — is what makes the statement nontrivial.

**Carleson operator.** The maximal form of the display above,
$$\mathcal{C}_{WW}f(x)=\sup_{\theta\in\mathbb{T}}\ \sup_{N}\ \Big|\frac1N\sum_{n=1}^N f(T^nx)e^{2\pi i n\theta}\Big|,$$
is the ergodic Carleson operator. By the Calderón transference principle its $L^p$ boundedness for $1<p<\infty$ is equivalent to the Carleson–Hunt theorem for the modulation-invariant maximal partial-sum operator
$$\mathcal{C}F(\xi)=\sup_{N}\Big|\int_{|\eta|\le N}\hat F(\eta)e^{2\pi i \xi\eta}\,d\eta\Big|,\qquad \|\mathcal{C}F\|_p\lesssim_p\|F\|_p .$$
This is the sense in which the maximal return-times problem *contains* Lusin's conjecture.

**Duality obstruction.** Bourgain's original argument, and Rudolph's joinings proof, both use $f\in L^\infty$ to control $\sup_N|A_N|$ by $\|f\|_\infty\cdot(\text{maximal ergodic average of }|g|)$. For $f\in L^p$ with $p<\infty$ one needs a genuinely bilinear estimate: the operator
$$(f,g)\mapsto \sup_N|A_N|$$
must map $L^p\times L^q\to L^r$-type spaces with $1/r=1/p+1/q$, *without* using the pairing $\langle f,g\rangle$ — hence "breaking the duality".

**Time–frequency structure.** The relevant model operator is a bilinear sum over tiles $P=I_P\times \omega_P$ of unit area in phase space,
$$\sum_{P}\frac{\langle f,\phi_P\rangle\langle g,\phi_{P'}\rangle}{|I_P|^{1/2}}\,\phi_{P''},$$
with an outer supremum over modulation parameters. Modulation invariance forbids any Littlewood–Paley decomposition that fixes a frequency scale.

## 3. History & State of the Art (SOTA)

- **1941.** Wiener and Wintner prove the uniform-in-$\theta$ ergodic theorem for $f\in L^1$ (their proof had a gap later repaired; the modern statement is due to Bourgain and to Assani).
- **1966–68.** Carleson proves Lusin's conjecture for $L^2$; Hunt extends to $L^p$, $p>1$. Kolmogorov's 1926 example rules out $p=1$.
- **1988–89.** Bourgain announces the return times theorem in *C. R. Acad. Sci. Paris*; the full proof appears as an appendix (with Furstenberg, Katznelson, Ornstein) to his IHÉS paper on pointwise ergodic theorems for arithmetic sets. Case $f,g\in L^\infty$.
- **1994.** Rudolph gives a joinings proof, replacing harmonic analysis with a structural Furstenberg-tower argument; extends to $f\in L^\infty$, $g\in L^1$.
- **1998.** Rudolph proves the multi-term return times theorem: orbit sequences of $k$ bounded functions from $k$ systems weight each other simultaneously.
- **2000.** Lacey–Thiele give the time–frequency proof of Carleson's theorem, supplying the tool set later used for return times.
- **2005.** Assani–Buczolich–Mauldin construct a counterexample showing (RT$_{1,1}$) is false.
- **2008.** Demeter, Lacey, Tao, Thiele prove (RT$_{p,q}$) for $p,q>1$ with $1/p+1/q<3/2$, together with the corresponding maximal (Lusin-type) weak-type estimates. This is the "solved-recently" component.
- **2010s–2020s.** Zorin-Kranich and others recast the multi-term theorem via cube spaces / Host–Kra structure theory, giving $L^\infty$ multi-term results in the nilpotent setting.

## 4. Partial Results / Verified Cases

| Case | Status | Source |
|---|---|---|
| $f,g\in L^\infty$ | Proved | Bourgain (1988/89); Rudolph (1994) |
| $f\in L^\infty$, $g\in L^1$ | Proved | Rudolph (1994), joinings |
| $p,q>1$, $1/p+1/q<3/2$ | Proved, with maximal bound | Demeter–Lacey–Tao–Thiele (2008) |
| $p=q=2$ | Proved (special case of above, $1/2+1/2=1<3/2$) | DLTT (2008) |
| $Y=\mathbb{T}$, $S$ a rotation, $g$ a character | Proved for $f\in L^p$, $p>1$ (Carleson–Hunt via transference); $f\in L^1$ fails | Carleson (1966), Hunt (1968), Kolmogorov (1926) |
| $Y$ with quasi-discrete spectrum; polynomial weights $e^{2\pi i P(n)}$ | Proved | Lesigne (1993) |
| $k$-term version, all $f_i\in L^\infty$ | Proved | Rudolph (1998); Zorin-Kranich (nilpotent reformulation) |
| $p=q=1$ | **False** | Assani–Buczolich–Mauldin (2005) |
| $p,q>1$, $1/p+1/q\ge 3/2$ (e.g. $p=q=4/3$) | **Open** | — |

Ergodic-theoretic reductions are also complete for systems with **discrete spectrum** (Kronecker systems), where $A_N$ can be computed by Fourier expansion and convergence is elementary, and for **weakly mixing** systems, where the limit is $\big(\int f\big)\big(\int g\big)$ off a null set.

## 5. Principal Obstacles

- **Modulation invariance.** The operator commutes with $f\mapsto e^{2\pi i n\theta}f$, so no square-function or Littlewood–Paley argument that privileges a frequency scale can work. Every known proof must organise phase space into tiles and run a Carleson-type selection/tree argument — expensive and lossy at exponents near $1$.
- **Loss of duality.** For $f\in L^\infty$ one bounds $|A_N|\le\|f\|_\infty M g$. Once $f\in L^p$, $p<\infty$, the natural estimate is bilinear; the Bessel/tree-counting inequalities available for tiles give an $L^p\times L^q\to L^r$ bound only when the total "energy budget" $1/p+1/q$ stays below $3/2$. The number $3/2$ is an artefact of the counting, not of any known example.
- **No transference to a single Euclidean model.** Unlike Wiener–Wintner, the general (RT) quantifies over *all* systems $(Y,S)$; there is no single operator on $\mathbb{R}$ whose boundedness transfers back. The DLTT proof handles this by proving a uniform estimate for a family of model operators.
- **Failure of the joinings method below $L^\infty$.** Rudolph's Furstenberg-tower argument needs uniform control of conditional expectations along the tower; for $f\in L^p$ the tower approximations are not uniformly integrable in the required sense.
- **$L^1$ genuinely breaks.** The ABM counterexample shows the obstruction is not merely technical at the endpoint: the exceptional set of $x$ for which the orbit sequence fails to be a good universal weight can have full measure.

## 6. The Gap

Proved: (RT$_{p,q}$) plus maximal bounds on the open region $\{p,q>1,\ 1/p+1/q<3/2\}$. Claimed: the whole region $\{p,q>1\}$. The gap is the closed strip
$$\tfrac32 \;\le\; \tfrac1p+\tfrac1q \;<\; 2,\qquad p,q>1,$$
containing e.g. $p=q=4/3$ and all pairs with $p$ close to $1$.

The exact step to be crossed is a **tile-counting inequality below the $3/2$ threshold**: current arguments bound the number of trees carrying a given energy by a quantity that becomes summable only when $1/p+1/q<3/2$. One needs either (i) a sharper size/energy interpolation for bilinear tile sums with an outer supremum, or (ii) a counterexample showing $3/2$ is real. No candidate counterexample exists in the strip; the ABM construction is intrinsically an $L^1$ phenomenon.

## 7. Current Research (as of June 2026)

- **Outer-measure time–frequency analysis.** The Do–Thiele outer $L^p$ framework repackages the DLTT tree estimates as embedding theorems into outer measure spaces; work continues on whether outer-Hölder can be run at exponents past $3/2$. *(frontier — verify)*
- **Sparse domination.** Efforts to dominate the modulation-invariant return-times operator by sparse forms $\sum_Q \langle f\rangle_{p,Q}\langle g\rangle_{q,Q}|Q|$ have produced Carleson-operator sparse bounds (Culiuc–Di Plinio–Ou); extending these to the bilinear return-times form is active. *(frontier — verify)*
- **Ergodic bilinear Hilbert transform.** Demeter's and Krause–Mirek–Tao's programme on non-conventional pointwise averages shares the modulation-invariance obstacle; techniques migrate between the two problems.
- **Structural / nilsystem route.** Zorin-Kranich, Host–Kra-style cube-space methods give clean $L^\infty$ multi-term results; the question is whether structure theory can be made quantitative enough to reach $L^p$.
- **Groups:** UCLA / Georgia Tech / Bonn (time–frequency school around Thiele's students), Indiana (Demeter), UNC (Assani, return times survey lineage), Rutgers/Bonn (Mirek).

## 8. Future Work

- Decide the strip $1/p+1/q\in[3/2,2)$: either improve the bilinear tree-counting or construct a counterexample built from a Kakeya/Besicovitch-type arrangement of tiles.
- Establish a genuine **Lusin–Egorov formulation**: for each $\varepsilon$, a set $E$ of measure $>1-\varepsilon$ on which convergence is uniform over the class of all $(Y,S,g)$, with quantitative dependence of the rate on $\varepsilon$.
- Multi-term return times for $L^p$ data ($k\ge 3$), where even the DLTT range is unavailable.
- Return times along **sparse subsequences** ($n^2$, primes), combining Bourgain's arithmetic maximal theorem with the return-times structure.
- Variational and jump-counting strengthenings: replace $\sup_N$ by the $r$-variation $V_r(A_N)$, which would give convergence rates rather than mere convergence.

## 9. Key References

- **[Foundational]** N. Wiener and A. Wintner. *Harmonic analysis and ergodic theory.* American Journal of Mathematics 63 (1941), 415–426.
- **[Foundational]** L. Carleson. *On convergence and growth of partial sums of Fourier series.* Acta Mathematica 116 (1966), 135–157.
- **[Foundational]** R. A. Hunt. *On the convergence of Fourier series.* In: Orthogonal Expansions and their Continuous Analogues, Southern Illinois Univ. Press, 1968, 235–255.
- **[Foundational]** J. Bourgain. *Temps de retour pour les systèmes dynamiques.* C. R. Acad. Sci. Paris Sér. I Math. 306 (1988), 483–485.
- **[Foundational]** J. Bourgain. *Pointwise ergodic theorems for arithmetic sets*, with an appendix *On the return time sequence* by J. Bourgain, H. Furstenberg, Y. Katznelson and D. Ornstein. Publications Mathématiques de l'IHÉS 69 (1989), 5–45.
- **[Structural]** D. J. Rudolph. *A joinings proof of Bourgain's return time theorem.* Ergodic Theory and Dynamical Systems 14 (1994), 197–203.
- **[Structural]** D. J. Rudolph. *Fully generic sequences and a multiple-term return-times theorem.* Inventiones Mathematicae 131 (1998), 199–228.
- **[Technique]** M. Lacey and C. Thiele. *A proof of boundedness of the Carleson operator.* Mathematical Research Letters 7 (2000), 361–370.
- **[SOTA / Recent]** C. Demeter, M. Lacey, T. Tao and C. Thiele. *Breaking the duality in the return times theorem.* Duke Mathematical Journal 143 (2008), 281–355.
- **[Counterexample]** I. Assani, Z. Buczolich and R. D. Mauldin. *An $L^1$ counting problem in ergodic theory.* Journal d'Analyse Mathématique 95 (2005), 221–241.
- **[Survey]** I. Assani and K. Presser. *A survey of the return times theorem.* In: Ergodic Theory and Dynamical Systems, de Gruyter Proceedings in Mathematics, 2014. (arXiv:1209.0856)
- **[Monograph]** I. Assani. *Wiener Wintner Ergodic Theorems.* World Scientific, 2003.
- **[Related]** E. Lesigne. *Spectre quasi-discret et théorème ergodique de Wiener–Wintner pour les polynômes.* Ergodic Theory and Dynamical Systems 13 (1993), 767–784.

## 10. Worked Example / Concrete Special Case

Take both systems to be circle rotations. Let $X=Y=\mathbb{T}$ with Lebesgue measure, $Tx=x+\alpha$, $Sy=y+\beta$, with $\alpha$ irrational. Let $f(x)=e^{2\pi i x}$ and let $g\in L^2(\mathbb{T})$ with Fourier expansion $g(y)=\sum_{k\in\mathbb{Z}}\hat g(k)e^{2\pi i k y}$.

Then $f(T^nx)=e^{2\pi i x}e^{2\pi i n\alpha}$ and
$$A_N(x,y)=\frac1N\sum_{n=1}^N f(T^nx)g(S^ny)
= e^{2\pi i x}\sum_{k}\hat g(k)e^{2\pi i k y}\cdot \frac1N\sum_{n=1}^N e^{2\pi i n(\alpha+k\beta)} .$$

The inner geometric average is
$$\frac1N\sum_{n=1}^N e^{2\pi i n\gamma_k}=\begin{cases}1,& \gamma_k:=\alpha+k\beta\in\mathbb{Z},\\[2pt] O\!\left(\dfrac{1}{N\,\|\gamma_k\|}\right),&\text{otherwise,}\end{cases}$$
where $\|\cdot\|$ is distance to the nearest integer.

*Case A ($1,\alpha,\beta$ rationally independent).* No $k$ gives $\gamma_k\in\mathbb{Z}$, so every term tends to $0$ and $A_N(x,y)\to 0$ for every $x$ and a.e. $y$. Consistent with $\int f=0$.

*Case B ($\beta=-\alpha$).* Then $\gamma_k\in\mathbb{Z}$ exactly for $k=1$, and
$$\lim_{N\to\infty}A_N(x,y)=\hat g(1)\,e^{2\pi i (x+y)}\neq 0 \ \text{ in general.}$$
So the orbit of $f$ is a nontrivial universal weight, and the limit depends on the joining of the two systems.

*Where the difficulty enters.* Convergence above was proved for one fixed $\beta$. The return-times statement requires a **single** null set of $x$ valid for all $(Y,S,g)$ simultaneously — here, all $\beta$ at once. Interchanging "for a.e. $x$" and "for all $\beta$" requires controlling
$$\mathcal{C}_{WW}f(x)=\sup_{\theta}\sup_N\Big|\frac1N\sum_{n\le N} f(T^nx)e^{2\pi i n\theta}\Big|,$$
whose $L^p$ boundedness for $1<p<\infty$ is exactly the Carleson–Hunt theorem transferred to $(X,T)$. Kolmogorov's a.e.-divergent $L^1$ Fourier series shows the bound fails at $p=1$ — the same wall the Assani–Buczolich–Mauldin counterexample hits from the ergodic side. Replacing the characters $e^{2\pi i n\theta}$ by orbit sequences $g(S^ny)$ from an arbitrary system is what upgrades Carleson's argument to the DLTT time–frequency proof, and what still costs the constraint $1/p+1/q<3/2$.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*