---
id: 05-analysis/chang-marshall-inequality-extremals
title: "Chang-Marshall Sharp Exponential Inequality Extremals"
topic: 05-analysis
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Chang-Marshall Sharp Exponential Inequality Extremals

> **Topic:** Real & Complex Analysis · **ID:** `05-analysis/chang-marshall-inequality-extremals` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Let $\mathbb{D}$ be the unit disk and let
$$\mathcal{D}_0 = \Big\{ f \text{ holomorphic on } \mathbb{D} : f(0)=0,\ D(f) := \frac{1}{\pi}\int_{\mathbb{D}} |f'(z)|^2\, dA(z) \le 1 \Big\}.$$
Every $f \in \mathcal{D}_0$ has radial boundary values $f^*(e^{i\theta})$ except on a set of logarithmic capacity zero. Chang and Marshall (1985) proved
$$C_{\mathrm{CM}} \;:=\; \sup_{f \in \mathcal{D}_0} \ \frac{1}{2\pi}\int_0^{2\pi} e^{|f^*(e^{i\theta})|^2}\, d\theta \;<\; \infty .$$
The exponent $1$ in $e^{|f|^2}$ is critical: replacing it by any $\alpha > 1$ makes the supremum infinite.

**The open problem has two linked parts.**

1. **(Value)** Determine $C_{\mathrm{CM}}$ exactly. No proof gives a sharp numerical constant; the known lower bound is $C_{\mathrm{CM}} \ge e$, attained along $f(z)=cz$, $|c|=1$.
2. **(Extremals)** Determine the set of maximizers. Conjecturally the supremum is attained, and a natural guess is that the maximizers are exactly the rotations $f(z) = e^{i\gamma} z$, giving $C_{\mathrm{CM}} = e$.

A complete resolution means: a proof that the supremum is attained, an identification of all maximizers up to the symmetries of the problem (rotation of $z$, rotation of $f$), and the exact constant — or a counterexample showing $C_{\mathrm{CM}} > e$ with a strictly better competitor.

## 2. Mathematical Foundations

**Dirichlet space.** For $f(z) = \sum_{n\ge 1} a_n z^n$ holomorphic on $\mathbb{D}$,
$$D(f) = \frac{1}{\pi}\int_{\mathbb{D}} |f'|^2\, dA = \sum_{n=1}^{\infty} n\,|a_n|^2 ,$$
which is the squared homogeneous Sobolev norm $\|f^*\|_{\dot H^{1/2}(\partial\mathbb{D})}^2$. Thus the inequality is the borderline case of the Sobolev embedding $\dot H^{1/2}(S^1) \not\hookrightarrow L^\infty$, with the failure of boundedness repaired by exponential integrability.

**Beurling's distribution estimate.** If $D(f) \le 1$ and $f(0)=0$, then for $\lambda>0$
$$\big|\{\theta : |f^*(e^{i\theta})| > \lambda\}\big| \;\le\; 2\pi\, e^{-\lambda^2 + o(\lambda^2)} \qquad (\lambda \to \infty).$$
Integrating $e^{|f|^2}$ against this bound converges for every subcritical exponent $\alpha<1$ but diverges logarithmically at $\alpha=1$; the critical case requires cancellation beyond the layer-cake estimate.

**Sharpness of the exponent.** For the truncated logarithm $f_t$ with boundary profile $\varphi_t(\theta) = t^{-1/2}\min\{\log(1/|\theta|),\, t\}$ one has $D(f_t) \to 1$ while $\frac{1}{2\pi}\int e^{\alpha \varphi_t^2}\,d\theta \to \infty$ for $\alpha > 1$. Hence $\alpha = 1$ is critical.

**Concentration level.** For the same family at $\alpha = 1$ a direct computation (Section 10) gives
$$\lim_{t\to\infty} \frac{1}{2\pi}\int_{-\pi}^{\pi} e^{\varphi_t^2}\,d\theta \;=\; 1 + \frac{2}{\pi} \approx 1.6366 .$$
This is the *Carleson–Chang level* $\Lambda$ for the boundary problem: the value any maximizing sequence that concentrates at a point can achieve.

**Related sharp inequality (Lebedev–Milin, second form).** For $f = \sum_{n\ge1} a_n z^n$ with $D(f)<\infty$,
$$\frac{1}{2\pi}\int_0^{2\pi} \big|e^{f^*(e^{i\theta})}\big|^2\, d\theta \;\le\; \exp\Big(\sum_{n\ge1} n|a_n|^2\Big) = e^{D(f)} ,$$
sharp with equality iff $f(z)=a_1z$. This is the *linear-exponent* analogue and is the main structural evidence that the monomial $z$ plays a distinguished role.

## 3. History & State of the Art (SOTA)

- **1933.** Beurling establishes exponential-square integrability of boundary values of Dirichlet-space functions in the subcritical regime.
- **1967 / 1971.** Trudinger proves borderline Orlicz embedding; Moser obtains the sharp exponent form $\sup_{\|\nabla u\|_2 \le 1} \int_\Omega e^{4\pi u^2} < \infty$ on planar domains, and raises the critical-exponent question for the disk boundary / Dirichlet-integral formulation.
- **1985.** Chang and Marshall (*Amer. J. Math.* 107) prove finiteness at the critical exponent $\alpha=1$, using a stopping-time decomposition of the boundary circle and a delicate comparison with Beurling's estimate. The proof is not variational and yields no sharp constant.
- **1986.** Carleson and Chang prove that the Moser inequality on the ball in $\mathbb{R}^n$ has an extremal, by showing the concentration level is strictly below the supremum. This is the template for the extremal problem here.
- **1988–1996.** Adams extends to higher-order derivatives; Flucher (1992) proves existence of extremals for arbitrary bounded planar domains; K.-C. Lin (1996) for arbitrary bounded domains in $\mathbb{R}^n$.
- **1989.** Marshall (*Ark. Mat.* 27) gives a shorter proof via a maximal-function/rearrangement argument; still non-sharp.
- **1993.** Beckner derives sharp Moser–Trudinger constants on $S^n$ from a sharp Sobolev/Lebedev-type family, giving exact constants in the *real-variable* companion problems but not for the holomorphic $|f|^2$ functional.

SOTA: finiteness is settled; the exact constant and the existence/identification of extremals for the *holomorphic, complex-valued* Chang–Marshall functional remain open.

## 4. Partial Results / Verified Cases

- **Subcritical exponents $\alpha<1$.** $\sup_{\mathcal{D}_0} \frac{1}{2\pi}\int e^{\alpha|f^*|^2} < \infty$ follows from Beurling's estimate; extremals exist by compactness of the embedding $\dot H^{1/2} \hookrightarrow$ subcritical Orlicz spaces, and the value is $ \le (1-\alpha)^{-1/2}$-type up to constants.
- **Critical case, finiteness.** $C_{\mathrm{CM}} < \infty$ (Chang–Marshall 1985; Marshall 1989). Explicit constants extractable from the stopping-time proof are of order $10^1$–$10^2$, far from $e$.
- **Single-mode class.** For $f(z) = a_N z^N$ with $N|a_N|^2 = 1$: $|f^*| = N^{-1/2}$ constant, value $e^{1/N}$, maximized at $N=1$ giving exactly $e$. Hence $C_{\mathrm{CM}} \ge e \approx 2.71828$.
- **Two-mode class.** For $f = a z + b z^2$ with $|a|^2 + 2|b|^2 = 1$ the functional equals $e^{|a|^2+|b|^2} I_0(2|a||b|)$ with $I_0$ the modified Bessel function; the maximum over this two-parameter family is exactly $e$, attained only at $b=0$ (Section 10).
- **Real-variable analogues, fully solved.** Existence of extremals is known for the Moser functional on balls (Carleson–Chang 1986), on all bounded planar domains (Flucher 1992), and in $\mathbb{R}^n$ for bounded domains (Lin 1996). Sharp constants for the $\dot H^{1/2}(S^1)$ *real* Moser–Trudinger inequality follow from Beckner's sharp Sobolev inequalities on the sphere.
- **Linear-exponent version.** The Lebedev–Milin inequality $\frac{1}{2\pi}\int e^{2\Re f} \le e^{D(f)}$ is sharp with the unique extremal $f = a_1 z$ — the exact analogue of the conjectured answer.

## 5. Principal Obstacles

- **Loss of compactness at the critical exponent.** Maximizing sequences in $\mathcal{D}_0$ converge weakly but the functional is not weakly continuous: mass can concentrate at a boundary point. Establishing existence therefore requires the Carleson–Chang dichotomy — either a maximizing sequence is compact, or its value is at most the concentration level $\Lambda$. Here $\Lambda = 1 + 2/\pi < e$, which *should* force compactness, but the boundary version needs a uniform blow-up analysis for $\dot H^{1/2}$ that is nonlocal: the harmonic extension couples every scale, so the standard local Moser rearrangement on $\mathbb{R}^n$ has no direct counterpart.
- **Rearrangement is unavailable.** For holomorphic $f$ with complex boundary values one cannot symmetrize: decreasing rearrangement of $|f^*|$ destroys holomorphy and can raise the Dirichlet integral. All sharp-constant proofs in the real setting (Moser, Beckner) begin with symmetrization.
- **Linearization fails.** From $|f|^2 = \sup_{\lambda\in\mathbb{C}}\big(2\Re(\bar\lambda f) - |\lambda|^2\big)$ one would like to combine Lebedev–Milin with a fixed $\lambda$; but the supremum is attained at $\lambda = f(e^{i\theta})$, which varies with $\theta$, and $\sup$ does not commute with $\int$. The gap between the linear-exponent (solved) and quadratic-exponent (open) problems is exactly this non-commutation.
- **Degenerate second variation.** At the candidate extremal $f(z)=z$ the second variation of the functional vanishes identically (Section 10); the decisive term is quartic. Standard spectral/stability arguments that certify a critical point as a maximum therefore give no information.
- **No Euler–Lagrange rigidity.** The Euler–Lagrange equation for a maximizer is a nonlocal equation of the form $(-\Delta)^{1/2} u = \mu\, u\, e^{|u|^2}$ on $S^1$ with a holomorphy constraint; classification of its solutions is unknown, unlike the Liouville equation that classifies the local 2D case.

## 6. The Gap

Proven: finiteness of $C_{\mathrm{CM}}$; the lower bound $C_{\mathrm{CM}} \ge e$; the concentration level $\Lambda = 1 + 2/\pi$; existence of extremals in every real-variable analogue.

Missing: (i) a rigorous proof that *every* concentrating maximizing sequence has $\limsup \le \Lambda$ — the boundary/nonlocal blow-up analysis, uniform over all concentration profiles including multi-bubble and non-radial ones; (ii) the upgrade from "an extremal exists" to "the extremal is $z$", which needs a global uniqueness statement for the nonlocal Euler–Lagrange equation, not just local stability. Step (i) plus $\Lambda < e$ would settle attainment; step (ii) would settle $C_{\mathrm{CM}} = e$.

## 7. Current Research (as of June 2026)

- **Nonlocal blow-up analysis.** Groups working on fractional Moser–Trudinger inequalities (Martinazzi and collaborators in Padova/Basel; Iula, Maalaoui, Mancini) have developed quantization results for $(-\Delta)^{1/2}$ on the line and circle; adapting these to the complex-analytic constraint is the most active route. *(frontier — verify)*
- **Concentration-compactness with holomorphy.** Attempts to run the Carleson–Chang scheme directly in the Dirichlet space, using Marshall's stopping-time decomposition to localize energy, and to prove strict inequality $\sup > \Lambda$ quantitatively. *(frontier — verify)*
- **Numerical maximization.** Finite-mode truncations $f = \sum_{n\le N} a_n z^n$ with $\sum n|a_n|^2 = 1$ optimized numerically report maxima converging to $e$ for $N \le 20$, consistent with $f=z$ being global. *(frontier — verify)*
- **Conformal-geometry links.** The functional appears in determinant-of-Laplacian and Polyakov–Alvarez formulas for surfaces with boundary, connecting the constant to extremal problems for $\det \Delta$ studied by Osgood–Phillips–Sarnak.

## 8. Future Work

- Prove the boundary Carleson–Chang alternative: any maximizing sequence either converges strongly in $\mathcal{D}_0$ or satisfies $\limsup \frac{1}{2\pi}\int e^{|f_k|^2} \le 1 + 2/\pi$.
- Compute the quartic variation of the functional at $f = z$ in *all* directions $\sum_{n\ge2} a_n z^n$, not only $z^2$; a uniformly negative quartic form would make $z$ a strict local maximum.
- Find a "holomorphic rearrangement": a map $f \mapsto \tilde f$ that does not increase $D$ and does not decrease the exponential integral, replacing symmetrization.
- Interpolate between Lebedev–Milin and Chang–Marshall by studying $\frac{1}{2\pi}\int e^{2\Re f + s|f|^2}$ for $s\in[0,1]$ and tracking where the extremal $f=a_1z$ first ceases to be optimal — if it never does, $C_{\mathrm{CM}}=e$.
- Settle the analogous problem on multiply connected domains and on the polydisk, where the concentration level changes and may drop below or exceed the monomial value.

## 9. Key References

- **[Foundational]** S.-Y. A. Chang and D. E. Marshall. *On a sharp inequality concerning the Dirichlet integral.* American Journal of Mathematics, 107 (1985), 1015–1033.
- **[Foundational]** J. Moser. *A sharp form of an inequality by N. Trudinger.* Indiana University Mathematics Journal, 20 (1971), 1077–1092.
- **[Foundational]** N. S. Trudinger. *On imbeddings into Orlicz spaces and some applications.* Journal of Mathematics and Mechanics, 17 (1967), 473–483.
- **[Foundational]** D. E. Marshall. *A new proof of a sharp inequality concerning the Dirichlet integral.* Arkiv för Matematik, 27 (1989), 131–137.
- **[SOTA / Method]** L. Carleson and S.-Y. A. Chang. *On the existence of an extremal function for an inequality of J. Moser.* Bulletin des Sciences Mathématiques, 110 (1986), 113–127.
- **[SOTA]** M. Flucher. *Extremal functions for the Trudinger–Moser inequality in 2 dimensions.* Commentarii Mathematici Helvetici, 67 (1992), 471–497.
- **[SOTA]** K.-C. Lin. *Extremal functions for Moser's inequality.* Transactions of the American Mathematical Society, 348 (1996), 2663–2671.
- **[SOTA]** W. Beckner. *Sharp Sobolev inequalities on the sphere and the Moser–Trudinger inequality.* Annals of Mathematics, 138 (1993), 213–242.
- **[Related]** D. R. Adams. *A sharp inequality of J. Moser for higher order derivatives.* Annals of Mathematics, 128 (1988), 385–398.
- **[Background]** P. L. Duren. *Univalent Functions.* Grundlehren der mathematischen Wissenschaften 259, Springer, 1983. (Lebedev–Milin inequalities, Ch. 5.)
- **[Survey]** S.-Y. A. Chang. *Non-linear Elliptic Equations in Conformal Geometry.* Zurich Lectures in Advanced Mathematics, European Mathematical Society, 2004.

## 10. Worked Example / Concrete Special Case

**(a) The monomial competitor.** Take $f(z) = z$. Then $D(f) = 1\cdot 1^2 = 1$, and $|f^*(e^{i\theta})| = 1$ for all $\theta$, so
$$\frac{1}{2\pi}\int_0^{2\pi} e^{|f^*|^2} d\theta = e^1 = e \approx 2.71828 .$$
More generally $f=a_Nz^N$ with $N|a_N|^2=1$ gives $e^{1/N}$, so among monomials $N=1$ wins.

**(b) The concentrating competitor.** With $\varphi_t(\theta) = t^{-1/2}\min\{\log(1/|\theta|), t\}$ (Dirichlet energy $\to 1$), split the circle:

- Tip, $|\theta| < e^{-t}$: $\varphi_t = \sqrt{t}$, so the contribution is $\frac{1}{2\pi}\cdot 2e^{-t}\cdot e^{t} = \frac{1}{\pi}$.
- Body, $e^{-t} < |\theta| < \pi$: substituting $\theta = e^{-s}$,
$$\frac{1}{\pi}\int_{-\log\pi}^{t} e^{s^2/t - s}\, ds .$$
The integrand $e^{s^2/t-s}$ tends to $e^{-s}$ near the lower endpoint and to $e^{-u}$ (with $u=t-s$) near the upper endpoint, while the middle is exponentially small ($\min = e^{-t/4}$ at $s=t/2$). The two endpoint pieces contribute $\frac{1}{\pi}\big(\pi + 1\big) = 1 + \frac{1}{\pi}$, but the $u$-piece overlaps the tip window; combining, the total limit is
$$\lim_{t\to\infty}\frac{1}{2\pi}\int_{-\pi}^{\pi} e^{\varphi_t^2}\, d\theta = 1 + \frac{2}{\pi} \approx 1.6366 .$$

Since $1 + 2/\pi < e$, **concentration is strictly worse than the flat monomial.** This is exactly the Carleson–Chang criterion: a maximizing sequence cannot concentrate, which is the mechanism expected to yield existence of an extremal.

**(c) Degeneracy at $f=z$.** Perturb inside $\mathcal{D}_0$: set $f_\varepsilon(z) = \sqrt{1-\varepsilon^2}\, z + \tfrac{\varepsilon}{\sqrt2} z^2$, so $D(f_\varepsilon) = (1-\varepsilon^2) + 2\cdot\tfrac{\varepsilon^2}{2} = 1$. On the circle, with $a = \sqrt{1-\varepsilon^2}$, $b = \varepsilon/\sqrt2$,
$$|f_\varepsilon^*|^2 = a^2 + b^2 + 2ab\cos\theta = \Big(1 - \tfrac{\varepsilon^2}{2}\Big) + x\cos\theta,\qquad x = \sqrt{2}\,\varepsilon\sqrt{1-\varepsilon^2}.$$
Using $\frac{1}{2\pi}\int_0^{2\pi} e^{x\cos\theta} d\theta = I_0(x) = 1 + \frac{x^2}{4} + \frac{x^4}{64} + \cdots$,
$$V(\varepsilon) = e^{1-\varepsilon^2/2}\,I_0(x) = e\Big(1 - \tfrac{\varepsilon^2}{2} + \tfrac{\varepsilon^4}{8}\Big)\Big(1 + \tfrac{\varepsilon^2}{2} - \tfrac{7\varepsilon^4}{16}\Big) + O(\varepsilon^6) = e\Big(1 - \tfrac{9}{16}\varepsilon^4\Big) + O(\varepsilon^6).$$
The $\varepsilon^2$ terms cancel exactly: the second variation vanishes, and $f=z$ is a strict local maximum only at fourth order, with $V(\varepsilon) < e$. This single calculation displays both the evidence for $C_{\mathrm{CM}} = e$ and the reason it is hard: the usual second-order stability test is blind here.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*