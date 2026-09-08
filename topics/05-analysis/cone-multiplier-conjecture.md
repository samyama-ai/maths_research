---
id: 05-analysis/cone-multiplier-conjecture
title: "Wolff's Conjecture on Cone Multipliers"
topic: 05-analysis
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Wolff's Conjecture on Cone Multipliers

> **Topic:** Real & Complex Analysis · **ID:** `05-analysis/cone-multiplier-conjecture` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Fix $n \ge 3$ and write $\xi = (\xi', \xi_n) \in \mathbb{R}^{n-1} \times \mathbb{R}$. For $\delta > 0$ define the **cone multiplier operator** $T^\delta$ on $\mathbb{R}^n$ by

$$\widehat{T^\delta f}(\xi) \;=\; \Big(1 - \frac{|\xi'|}{\xi_n}\Big)_+^{\delta}\, \psi(\xi_n)\, \hat f(\xi),$$

where $\psi \in C_c^\infty(1/2, 2)$ cuts off the cone to a compact piece and $a_+ = \max(a,0)$.

**Conjecture (cone multiplier / Wolff).** For $2 \le p \le \infty$, $T^\delta$ is bounded on $L^p(\mathbb{R}^n)$ if and only if

$$\delta \;>\; \delta_n(p) \;:=\; \max\Big\{0,\; \frac{n-1}{2} - \frac{n-1}{p} - \frac12\Big\} \;=\; \max\Big\{0,\; (n-1)\Big(\tfrac12 - \tfrac1p\Big) - \tfrac12\Big\}.$$

By duality the same holds for $1 < p \le 2$ with $1/p$ replaced by $1/p'$. The content of the conjecture is the sufficiency; the necessity is known (Section 10). In particular, for $2 \le p \le \frac{2(n-1)}{n-2}$ the claim is that **every** $\delta > 0$ works — for $n = 3$ this means $L^p$-boundedness for all $\delta>0$ in the full range $2 \le p \le 4$, in sharp contrast with the Bochner–Riesz multiplier for the sphere, where positive $\delta$ is needed as soon as $p \ne 2$.

A complete proof must supply, for each $p$ in the conjectured range and each $\delta > \delta_n(p)$, a bound $\|T^\delta f\|_{L^p(\mathbb{R}^n)} \le C_{n,p,\delta}\|f\|_{L^p(\mathbb{R}^n)}$; a disproof requires an $f$ witnessing unboundedness for some $\delta > \delta_n(p)$.

## 2. Mathematical Foundations

**The light cone.** $\Gamma = \{\xi : |\xi'| = \xi_n,\ \xi_n > 0\} \subset \mathbb{R}^n$ is a hypersurface with exactly $n-2$ non-vanishing principal curvatures; the missing direction is the radial generator. Consequently the surface measure satisfies $|\widehat{d\sigma}(x)| \lesssim (1+|x|)^{-(n-2)/2}$ away from the dual cone, one power of $|x|^{-1/2}$ worse than the sphere.

**Slab decomposition.** Write $m_\delta(\xi) = (1-|\xi'|/\xi_n)^\delta_+\psi(\xi_n) = \sum_{j \ge 0} 2^{-j\delta} m_j(\xi)$, where $m_j$ is supported in the slab $\{1-|\xi'|/\xi_n \sim 2^{-j}\}$ and obeys $|\partial^\alpha m_j| \lesssim 2^{j|\alpha_\nu|}$ in the normal direction $\nu$. Boundedness of $T^\delta$ on $L^p$ for all $\delta > \delta_0$ is equivalent to the slab bound
$$\|T_{j}\|_{L^p \to L^p} \lesssim_\varepsilon 2^{j(\delta_0+\varepsilon)} \qquad \text{for all } \varepsilon>0 .$$

**Plates.** For $\epsilon = 2^{-j}$ the $\epsilon$-slab around $\Gamma$ is partitioned into $\sim \epsilon^{-(n-2)/2}$ **plates** $\theta$, each a box of dimensions $\underbrace{\epsilon}_{\text{normal}} \times \underbrace{\epsilon^{1/2} \times \cdots \times \epsilon^{1/2}}_{n-2} \times \underbrace{1}_{\text{generator}}$. Write $f_\theta$ for the Fourier restriction of $f$ to $\theta$.

**Wolff's square function conjecture (cone in $\mathbb{R}^3$).** For $\hat f$ supported in the $\epsilon$-neighbourhood of $\Gamma \subset \mathbb{R}^3$ and $p \ge 4$,
$$\|f\|_{L^p(\mathbb{R}^3)} \;\lesssim_\varepsilon\; \epsilon^{-\varepsilon}\,\Big\|\Big(\sum_\theta |f_\theta|^2\Big)^{1/2}\Big\|_{L^p(\mathbb{R}^3)} .$$

**Local smoothing.** Setting $u(x,t) = e^{it\sqrt{-\Delta}}f(x)$ on $\mathbb{R}^{n-1}\times[1,2]$, the wave propagator's spacetime Fourier support is the cone in $\mathbb{R}^n$. Sogge's local smoothing conjecture asserts
$$\|e^{it\sqrt{-\Delta}}f\|_{L^p(\mathbb{R}^{n-1}\times[1,2])} \lesssim \|f\|_{L^p_s(\mathbb{R}^{n-1})},\qquad s > (n-1)\Big(\tfrac12-\tfrac1p\Big)-\tfrac1p,\quad p \ge \tfrac{2(n-1)}{n-2},$$
a gain of $1/p$ derivatives over the sharp fixed-time bound of Miyachi and Peral. Mockenhaupt–Seeger–Sogge (1993) showed local smoothing at exponent $s$ implies the cone multiplier bound at $\delta = s$; the two conjectures have the same critical index.

## 3. History & State of the Art (SOTA)

- **1970s–80s.** The cone multiplier is singled out as the natural "one-degenerate-direction" analogue of Bochner–Riesz. Fixed-time wave estimates (Miyachi 1980, Peral 1980) give $\delta > (n-1)(\frac12-\frac1p)$ — half a derivative worse than conjectured.
- **1991.** Sogge (*Invent. Math.* 104) proves the first local smoothing gain in 2+1 dimensions, initiating the subject.
- **1993.** Mockenhaupt–Seeger–Sogge (*JAMS* 6) convert Kakeya/Nikodym maximal bounds into local smoothing, and formalize the implication local smoothing $\Rightarrow$ cone multiplier.
- **1995.** Bourgain, *Estimates for cone multipliers*, gives $\epsilon$-improvements over the trivial exponent.
- **2000.** **Wolff** (*GAFA* 10) proves the sharp square function/decoupling-type inequality for the cone in $\mathbb{R}^3$ for $p > 74$, yielding the sharp cone multiplier bound there, and states the square function conjecture for all $p \ge 4$. This is the statement now called *Wolff's conjecture*.
- **2002.** Łaba–Wolff extend the method to $\mathbb{R}^n$, $n\ge 4$, for large $p$.
- **2011.** Heo–Nazarov–Seeger (*Acta Math.* 206) obtain sharp cone multiplier bounds in high dimensions for $p \ge \frac{2(n-1)}{n-3}$, $n \ge 4$.
- **2015.** Bourgain–Demeter's $\ell^2$ decoupling theorem (*Ann. of Math.* 182) gives the sharp result for the cone in $\mathbb{R}^n$ in the full decoupling range $p \ge \frac{2n}{n-2}$ — for $n=3$, all $p \ge 6$.
- **2020.** **Guth–Wang–Zhang** (*Ann. of Math.* 192) prove the sharp $L^4$ square function estimate for the cone in $\mathbb{R}^3$, i.e. Wolff's conjecture and the local smoothing conjecture in 2+1 dimensions. This **settles the cone multiplier conjecture completely for $n=3$**.
- **2020–2026.** Attention shifts to $n \ge 4$ (equivalently local smoothing in $\ge 3$ space dimensions), where the problem remains open.

## 4. Partial Results / Verified Cases

| Case | Range settled | Source |
|---|---|---|
| $n = 3$, $p \ge 6$ | sharp, $\delta > \frac12-\frac2p$ | Bourgain–Demeter $\ell^2$ decoupling (2015) |
| $n = 3$, $2 \le p \le 4$ | sharp, all $\delta>0$ | Guth–Wang–Zhang (2020) |
| $n = 3$, $4 < p < 6$ | sharp | GWZ (2020), by interpolation from $p=4$ |
| $n \ge 4$, $p \ge \frac{2n}{n-2}$ | sharp | Bourgain–Demeter (2015) |
| $n \ge 4$, $p \ge \frac{2(n-1)}{n-3}$ | sharp | Heo–Nazarov–Seeger (2011) |
| $n \ge 4$, $p$ large | sharp | Łaba–Wolff (2002) |
| all $n$, $p = 2$ | trivial, all $\delta > 0$ | Plancherel |

So the conjecture is a **theorem for $n=3$**, and for every $n$ in the tail range $p \ge \frac{2n}{n-2}$. The remaining open window is
$$\frac{2(n-1)}{n-2} \;<\; p \;<\; \frac{2n}{n-2}, \qquad n \ge 4,$$
e.g. $3 < p < 4$ for $n=4$, $\tfrac83 < p < \tfrac{10}{3}$ for $n=5$. Partial (non-sharp) gains inside the window are known: Lee–Vargas, and Garrigós–Seeger's analysis of plate decompositions, which shows the plate square function *characterizes* the cone multiplier only in restricted ranges.

## 5. Principal Obstacles

- **One flat direction.** The cone's null generator kills the $L^2$-based orthogonality that drives spherical Bochner–Riesz arguments. Wave packets over the cone are *plates*, not tubes; two plates over widely separated cone directions can still overlap in a whole $1$-dimensional set, so a naive $TT^*$ argument loses exactly the half-derivative one is trying to save.
- **Kakeya is not enough.** The MSS scheme bounds local smoothing by Nikodym maximal estimates for light rays. Even the *optimal* Kakeya bound gives strictly less than the conjectured $1/p$ gain, because the extremal Kakeya configurations are not realizable by wave packets — the loss is in the passage from a measure-theoretic covering bound to an $L^p$ bound with signs.
- **Decoupling saturates.** $\ell^2$ decoupling is sharp only for $p \ge \frac{2n}{n-2}$; below that exponent the $\ell^2$ inequality is *false* at the conjectured exponent, and the correct object is the square function, which is strictly stronger and has no known induction-on-scales proof in dimensions $n \ge 4$.
- **Polynomial partitioning does not transfer.** The GWZ proof uses the special two-dimensional geometry of $\mathbb{R}^3$: plates over the light cone in $\mathbb{R}^3$ tangent to a common plane form a "cinematic" family, and the induction is run on the degree of a partitioning surface. In $\mathbb{R}^n$, $n\ge4$, the analogous tangency sets have higher-dimensional structure and the key "planebrush"/broad–narrow dichotomy has no established analogue.
- **Non-vanishing curvature is only $n-2$-fold.** Standard stationary-phase decay $|x|^{-(n-2)/2}$ is one half-power short of what a direct kernel estimate would need to reach $\delta_n(p)$.

## 6. The Gap

Proven: sharp bounds for $p$ above $\frac{2n}{n-2}$ (all $n$) and everything for $n=3$. Conjectured: the strip $\frac{2(n-1)}{n-2} < p < \frac{2n}{n-2}$ for $n \ge 4$.

The exact missing step is the **sharp cone square function estimate in dimension $n \ge 4$ at the critical exponent $p = \frac{2(n-1)}{n-2}$**:
$$\|f\|_{L^{p}(\mathbb{R}^n)} \;\lesssim_\varepsilon\; \epsilon^{-\varepsilon}\Big\|\Big(\sum_\theta|f_\theta|^2\Big)^{1/2}\Big\|_{L^{p}(\mathbb{R}^n)},\qquad p=\tfrac{2(n-1)}{n-2},$$
for $\hat f$ in the $\epsilon$-slab. For $n=3$ this is exactly the $L^4$ inequality proved by GWZ. Everything else — interpolation with $L^2$ and with the decoupling range, and the passage from slab bound to multiplier bound — is routine. Equivalently: prove the local smoothing conjecture for the wave equation in $\ge 3$ space dimensions.

## 7. Current Research (as of June 2026)

- **Higher-dimensional square functions.** Gao, Liu, Miao and Xi have pushed square-function and local smoothing estimates for Fourier integral operators past the decoupling exponent in several regimes; the critical exponent in $n\ge4$ is still out of reach. *(frontier — verify)*
- **Variable-coefficient theory.** Beltran–Hickman–Sogge established Wolff-type inequalities for wave equations on manifolds, showing the constant-coefficient cone results are not artifacts of flatness — and, conversely, that Bourgain-type counterexamples limit what can hold in the variable setting.
- **Small cap decoupling.** Demeter–Guth–Wang's small cap decoupling interpolates between $\ell^2$ decoupling and the square function; adapting it to the cone in $\mathbb{R}^n$ is an active line. *(frontier — verify)*
- **Nested polynomial partitioning / Hörmander dichotomies.** Guo–Wang–Zhang's dichotomy for Hörmander-type oscillatory integral operators is being tested as the higher-dimensional replacement for the GWZ planebrush. *(frontier — verify)*
- **Groups.** MIT (Guth and collaborators), Wisconsin (Seeger), Johns Hopkins (Sogge), Bonn/Birmingham (Hickman, Beltran), Chinese Academy of Sciences and Zhejiang (Miao, Xi), KIAS/Seoul (S. Lee).

## 8. Future Work

1. **Prove the $n=4$ square function estimate at $p=3$.** The smallest open case; a proof would likely be templatable to all $n$.
2. **Develop an induction-on-scales that respects signs.** The GWZ argument is not an $\ell^2$ argument; identifying which structural feature (plate tangency to a variety of low degree) generalizes is the stated program.
3. **Sharp Nikodym for light rays in $\mathbb{R}^n$.** Even short of the full conjecture, the sharp Kakeya bound for families of light rays would give new intermediate exponents.
4. **Counterexample search.** Bourgain's variable-coefficient counterexamples suggest testing whether the *constant-coefficient* conjecture could fail in high dimension; no such example is known.
5. **Endpoint and weak-type behaviour at $\delta = \delta_n(p)$**, where even in $\mathbb{R}^3$ the critical case is unresolved.

## 9. Key References

- **[Foundational]** T. Wolff. *Local smoothing type estimates on $L^p$ for large $p$.* Geom. Funct. Anal. **10** (2000), 1237–1288.
- **[Foundational]** G. Mockenhaupt, A. Seeger, C. D. Sogge. *Local smoothing of Fourier integral operators and Carleson–Sjölin estimates.* J. Amer. Math. Soc. **6** (1993), 65–130.
- **[Foundational]** C. D. Sogge. *Propagation of singularities and maximal functions in the plane.* Invent. Math. **104** (1991), 349–376.
- **[Foundational]** J. Bourgain. *Estimates for cone multipliers.* Operator Theory: Advances and Applications **77** (1995), 41–60.
- **[SOTA]** L. Guth, H. Wang, R. Zhang. *A sharp square function estimate for the cone in $\mathbb{R}^3$.* Ann. of Math. (2) **192** (2020), 551–581.
- **[SOTA]** J. Bourgain, C. Demeter. *The proof of the $\ell^2$ decoupling conjecture.* Ann. of Math. (2) **182** (2015), 351–389.
- **[SOTA]** Y. Heo, F. Nazarov, A. Seeger. *Radial Fourier multipliers in high dimensions.* Acta Math. **206** (2011), 55–92.
- **[SOTA]** I. Łaba, T. Wolff. *A local smoothing estimate in higher dimensions.* J. Anal. Math. **88** (2002), 149–171.
- **[SOTA]** D. Beltran, J. Hickman, C. D. Sogge. *Variable coefficient Wolff-type inequalities and sharp local smoothing estimates for wave equations on manifolds.* Anal. PDE **13** (2020), 403–433.
- **[Related]** S. Lee, A. Vargas. *On the cone multiplier in $\mathbb{R}^3$.* J. Funct. Anal. **263** (2012), 925–940.
- **[Related]** G. Garrigós, A. Seeger. *On plate decompositions of cone multipliers.* Proc. Edinburgh Math. Soc. **52** (2009), 631–651.
- **[Related]** C. Demeter, L. Guth, H. Wang. *Small cap decouplings.* Geom. Funct. Anal. **30** (2020), 989–1062.
- **[Survey / Book]** C. D. Sogge. *Fourier Integral Operators in Classical Analysis.* Cambridge University Press, 1993 (2nd ed. 2017).
- **[Survey / Book]** E. M. Stein. *Harmonic Analysis: Real-Variable Methods, Orthogonality, and Oscillatory Integrals.* Princeton University Press, 1993.

## 10. Worked Example / Concrete Special Case

**(a) Necessity of $\delta_n(p)$ via a plate.** Take the slab piece $T_j$, $\epsilon = 2^{-j}$, and let $\hat f = \chi_\theta$ for one plate $\theta$ of dimensions $\epsilon \times \epsilon^{1/2}\times\cdots\times\epsilon^{1/2}\times 1$, so $|\theta| \sim \epsilon^{n/2}$. Then $|f| \gtrsim |\theta|$ on the dual box $\theta^*$ with $|\theta^*| \sim \epsilon^{-n/2}$, giving $\|f\|_p \sim \epsilon^{n/2}\epsilon^{-n/(2p)}$. Summing $\epsilon^{-(n-2)/2}$ such plates with the phases arranged so that all wave packets focus on a common $\epsilon^{-1/2}$-neighbourhood of a light ray, and comparing with the diffuse $L^p$ mass of $f$, yields
$$\|T_j\|_{L^p\to L^p} \gtrsim \epsilon^{-\left[(n-1)(\frac12-\frac1p)-\frac12\right]},$$
which forces $\delta \ge \delta_n(p)$ in the multiplier bound. Numerically, for $n=4,\ p=7/2$: $\delta_4(7/2)=3\left(\tfrac12-\tfrac27\right)-\tfrac12 = \tfrac{9}{14}-\tfrac{7}{14}=\tfrac17$. That case lies in the open window $3<p<4$ — **whether $T^{1/7+}$ is bounded on $L^{7/2}(\mathbb{R}^4)$ is not known.**

**(b) Sufficiency at $p=4$, $n=3$, from the square function.** Here $\delta_3(4)=\tfrac12-\tfrac24=0$, so the claim is boundedness for every $\delta>0$. Fix $\epsilon = 2^{-j}$ and let $f$ have $\hat f$ in the $\epsilon$-slab, decomposed into $N \sim \epsilon^{-1/2}$ plates. Guth–Wang–Zhang give
$$\|f\|_{L^4(\mathbb{R}^3)} \;\lesssim_\varepsilon\; \epsilon^{-\varepsilon}\Big\|\Big(\sum_\theta|f_\theta|^2\Big)^{1/2}\Big\|_{L^4}.$$
Apply this to $T_j f$. Since the multiplier $m_j$ is a smooth symbol adapted to each plate, $\|(\sum_\theta |(T_jf)_\theta|^2)^{1/2}\|_4 \lesssim \|(\sum_\theta|f_\theta|^2)^{1/2}\|_4$, and the reverse square function bound $\|(\sum_\theta|f_\theta|^2)^{1/2}\|_4 \lesssim \epsilon^{-\varepsilon}\|f\|_4$ (Littlewood–Paley for plates, valid since $4\ge 2$) gives
$$\|T_j\|_{L^4 \to L^4} \lesssim_\varepsilon \epsilon^{-\varepsilon} = 2^{j\varepsilon}.$$
Then for $\delta>0$, choosing $\varepsilon = \delta/2$,
$$\|T^\delta f\|_4 \le \sum_{j\ge0} 2^{-j\delta}\|T_j f\|_4 \lesssim \sum_{j\ge0} 2^{-j\delta}2^{j\delta/2}\|f\|_4 = \frac{1}{1-2^{-\delta/2}}\|f\|_4 < \infty .$$
Interpolating this with the trivial $L^2$ bound gives all $2\le p\le4$; interpolating with the $\ell^2$-decoupling result at $p=6$ gives $4<p<6$. This is the complete resolution for $n=3$ — and it is exactly the step (a) sharp square function at the critical exponent that is missing for $n\ge4$.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*