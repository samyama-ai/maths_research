---
id: 05-analysis/kato-root-problem
title: "Kato's Root Problem"
topic: 05-analysis
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Kato's Root Problem

> **Topic:** Real & Complex Analysis · **ID:** `05-analysis/kato-root-problem` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

Let $A \in L^\infty(\mathbb{R}^n; \mathcal{M}_n(\mathbb{C}))$ satisfy the Gårding (uniform ellipticity) condition
$$\operatorname{Re}\int_{\mathbb{R}^n}\langle A(x)\nabla u(x), \nabla u(x)\rangle\,dx \;\ge\; \lambda\,\|\nabla u\|_2^2,\qquad u\in H^1(\mathbb{R}^n),$$
with $\lambda>0$ and $\|A\|_\infty = \Lambda<\infty$. Let $L = -\operatorname{div}(A\nabla)$ be the maximal accretive operator defined from the associated sesquilinear form, and let $L^{1/2}$ be its accretive square root.

**Kato's square root problem.** Is $\mathcal{D}(L^{1/2}) = H^1(\mathbb{R}^n)$, with
$$\|L^{1/2}u\|_{L^2} \;\simeq\; \|\nabla u\|_{L^2},\qquad u\in H^1(\mathbb{R}^n),$$
the implicit constants depending only on $n,\lambda,\Lambda$?

No smoothness whatsoever is assumed on $A$ — merely bounded measurable, possibly complex, non-symmetric. A complete solution requires the two-sided estimate; a disproof requires a single elliptic $A$ for which the domain of $L^{1/2}$ differs from $H^1$.

**Status.** The $L^2$ problem on $\mathbb{R}^n$ was **solved affirmatively** in 2002 by Auscher, Hofmann, Lacey, McIntosh and Tchamitchian. The *abstract* form of Kato's conjecture (for general maximal accretive operators) is **false**. Substantial descendants — the $L^p$ range, degenerate weights, rough domains, non-smooth manifolds, dimension-free constants — remain open.

## 2. Mathematical Foundations

**Form definition.** Set $J[u,v] = \int_{\mathbb{R}^n}\langle A\nabla u,\nabla v\rangle$ on $V=H^1(\mathbb{R}^n)\subset H=L^2$. By Lax–Milgram there is a closed, densely defined operator $L$ with $\mathcal{D}(L)\subset H^1$ and $\langle Lu,v\rangle = J[u,v]$. Its numerical range lies in the sector $S_\omega = \{z : |\arg z|\le \omega\}$, $\omega = \arctan(\Lambda/\lambda) < \pi/2$, so $L$ is $\omega$-sectorial and $-L$ generates an analytic semigroup $e^{-tL}$ on $L^2$.

**Square root.** For sectorial $L$,
$$L^{1/2} = \frac{1}{\pi}\int_0^\infty \lambda^{-1/2}(\lambda+L)^{-1}L\,\frac{d\lambda}{1}, \qquad\text{equivalently}\qquad L^{1/2}u = \frac{2}{\sqrt{\pi}}\int_0^\infty e^{-t^2 L}Lu\,dt .$$
$L^{1/2}$ is again maximal accretive and $(L^{1/2})^* = (L^*)^{1/2}$ with $L^* = -\operatorname{div}(A^*\nabla)$.

**The easy inclusion and duality.** The estimate $\|\nabla u\|_2 \lesssim \|L^{1/2}u\|_2$ follows from $\operatorname{Re}\langle Lu,u\rangle \ge \lambda\|\nabla u\|_2^2$ together with the Kato–Lions identity $\langle Lu,u\rangle = \|L^{1/2}u\|_2^2$ for symmetric $L$ (and a sectorial variant in general). The **hard direction** is
$$\|L^{1/2}u\|_2 \;\lesssim\; \|\nabla u\|_2 . \tag{K}$$
Since $(L^{1/2})^* = (L^*)^{1/2}$ and $A^*$ is elliptic with the same constants, (K) for the whole class self-improves to the two-sided equivalence.

**Quadratic reformulation.** Because $L$ has a bounded $H^\infty$ functional calculus on $L^2$ whenever square-function bounds hold, (K) is equivalent to the square-function estimate
$$\int_0^\infty \big\|\,t L e^{-t^2 L} u \,\big\|_2^2\,\frac{dt}{t} \;\lesssim\; \|\nabla u\|_2^2 .$$
Writing $\theta_t u := tLe^{-t^2L}u = -\operatorname{div}\!\big(t A\nabla e^{-t^2L}u\big)$ and $\theta_t f := t\operatorname{div}(A\,\cdot)$ acting on the vector field $f=\nabla u$, one must prove that $\theta_t$ is an $L^2$-bounded "square-function operator" with kernel bounds but **no cancellation** $\theta_t 1 = 0$. The remedy is a $T(b)$ theorem: construct test fields $f^\varepsilon_Q$ adapted to each dyadic cube $Q$ with $\fint_Q f^\varepsilon_Q \approx e$ and show that
$$d\mu(x,t) = |\theta_t \mathcal{A}_t \mathbf{1}(x)|^2\,\frac{dx\,dt}{t}$$
is a Carleson measure, where $\mathcal{A}_t$ is a dyadic averaging operator (the *principal part approximation*).

**Counterexample to the abstract conjecture.** Kato asked whether $\mathcal{D}(T^{1/2})=\mathcal{D}(T^{*1/2})$ for every maximal accretive $T$. McIntosh (1972) produced a maximal accretive $T$ with $\mathcal{D}(T^{1/2})\neq\mathcal{D}(T^{*1/2})$; Lions (1962) had already shown $\mathcal{D}(T^{1/2})\neq[H,\mathcal{D}(T)]_{1/2}$ in general. Thus the divergence-form structure is essential, not incidental.

## 3. History & State of the Art

- **1961–62.** Kato, *Fractional powers of dissipative operators*, proves $\mathcal{D}(T^\alpha)=[H,\mathcal{D}(T)]_\alpha$ for $\alpha<1/2$ and isolates $\alpha=1/2$ as the critical exponent. Lions (1962) shows the endpoint can fail abstractly.
- **1972.** McIntosh's counterexample kills the abstract version; the conjecture is thereafter restricted to elliptic divergence-form operators — the form later called *the Kato square root problem*.
- **1982.** Coifman–McIntosh–Meyer prove $L^2$-boundedness of the Cauchy integral on Lipschitz curves; Coifman–Deng–Meyer and Kenig deduce the **one-dimensional Kato problem** ($n=1$, complex $a\in L^\infty$ accretive).
- **1985.** Fabes–Jerison–Kenig: multilinear expansions give the result for $\|A-I\|_\infty$ small (perturbative regime).
- **1998.** Auscher–Tchamitchian, *Astérisque* 249, surveys the field and settles many structured cases.
- **2001.** Auscher–Hofmann–Lewis–Tchamitchian (Acta Math.) prove Carleson-measure extrapolation, giving $n=1$ systems and analyticity of $A\mapsto L_A^{1/2}$ on a maximal region.
- **2001–02.** Hofmann–McIntosh solve $n=2$; Hofmann–Lacey–McIntosh solve all $n$ under pointwise Gaussian heat-kernel bounds (Ann. of Math. 156).
- **2002.** **Auscher–Hofmann–Lacey–McIntosh–Tchamitchian**, *The solution of the Kato square root problem for second order elliptic operators on $\mathbb{R}^n$*, Ann. of Math. 156, 633–654: full solution, all $n$, all complex bounded measurable elliptic $A$.
- **2006.** Axelsson–Keith–McIntosh recast the proof via perturbed Dirac operators $\Pi_B = \Gamma + B_1\Gamma^*B_2$, giving a shorter, far more portable framework ("first-order approach").

## 4. Partial Results / Verified Cases

| Class | Result | Source |
|---|---|---|
| $\|A-I\|_\infty \le \varepsilon(n,\lambda)$ | Kato estimate; $A\mapsto L^{1/2}$ analytic | Fabes–Jerison–Kenig 1985 |
| $n=1$, scalar $a\in L^\infty$ accretive | Solved via Cauchy integral | Coifman–Deng–Meyer 1983; Kenig |
| $n=1$, systems; $A$ in a ball of $L^\infty$ around real symmetric | Solved | Auscher–Hofmann–Lewis–Tchamitchian 2001 |
| $n=2$, all complex $A$ | Solved | Hofmann–McIntosh 2002 |
| Any $n$, $e^{-tL}$ with pointwise Gaussian bounds (e.g. real $A$) | Solved | Hofmann–Lacey–McIntosh 2002 |
| **Any $n$, all complex elliptic $A$** | **Solved** | AHLMcT 2002 |
| Order-$2m$ operators and systems on $\mathbb{R}^n$: $\mathcal{D}(L^{1/2})=H^m$ | Solved | Auscher–Hofmann–McIntosh–Tchamitchian 2001 |
| Mixed Dirichlet/Neumann conditions on rough domains (Ahlfors-regular Dirichlet part, local bi-Lipschitz collar) | Solved | Egert–Haller-Dintelmann–Tolksdorf 2014 |
| Degenerate operators $-w^{-1}\operatorname{div}(w A\nabla)$, $w\in A_2$, with Gaussian bounds | Solved | Cruz-Uribe–Rios 2012 |
| Submanifolds of $\mathbb{R}^n$; vector bundles of generalised bounded geometry | Solved | Morris 2012; Bandara–McIntosh 2016 |
| $L^p$ estimates $\|L^{1/2}u\|_p\simeq\|\nabla u\|_p$ | Holds on an open interval $(p_-(L), p_+(L))\ni 2$, sharp in general | Auscher, Mem. AMS 186 (2007) |

## 5. Principal Obstacles

- **No smoothness, no kernel.** For complex $A$ in $n\ge3$ the heat kernel of $e^{-tL}$ need not be pointwise bounded (Mazya–Nazarov–Plamenevskii type examples); Calderón–Zygmund theory is unavailable, so the operator must be handled by off-diagonal ($L^2$ Gaffney–Davies) estimates only.
- **Failure of $T(1)$.** $\theta_t \mathbf{1}\neq 0$: the natural square-function operator has no cancellation against constants, so the classical $T1$ theorem gives nothing. One must build accretive test functions, and the naive choice $b_Q = e^{-\ell(Q)^2L}(x\cdot e)$ can degenerate.
- **Non-self-adjointness.** Spectral theorem, form-domain interpolation and Kato's $\alpha<1/2$ theorem all stop exactly at $\alpha=1/2$; McIntosh's counterexample shows no abstract operator-theoretic route can close the endpoint.
- **The stopping-time is not free.** The $T(b)$ argument requires a *sector* condition $\operatorname{Re}\langle f^\varepsilon_Q, e\rangle \gtrsim 1$ on a large subset of $Q$, obtained by a delicate $\varepsilon$-parameter stopping-time plus John–Nirenberg-type Carleson extrapolation (AHLT). This machinery is what fails immediately for degenerate ellipticity, unbounded coefficients, or $p\ne 2$.
- **$p\neq2$ genuinely breaks.** Auscher's memoir shows the interval of good $p$ is bounded above by $2n/(n-2)$-type thresholds and no argument extends to all $p$, because the relevant Riesz transform $\nabla L^{-1/2}$ is unbounded on $L^p$ outside $(p_-,p_+)$.

## 6. The Gap

For the classical statement of Section 1 there is **no gap**: the theorem is proven for every bounded measurable complex elliptic $A$ on $\mathbb{R}^n$, all $n\ge1$. The live gaps are downstream:

1. **Constants.** All proofs yield constants of the form $C(n)(\Lambda/\lambda)^{c(n)}$ with $c(n)$ growing in $n$ (buried in the Carleson extrapolation). Whether a **dimension-free** bound $\|L^{1/2}u\|_2\le C(\Lambda/\lambda)\|\nabla u\|_2$ holds is open.
2. **Sharp $p$-range.** The exact endpoints $p_\pm(L)$ in terms of $A$ are unknown outside special classes; the $p$-elliptic condition of Carbonaro–Dragičević gives sufficient but not necessary criteria.
3. **Degenerate and unbounded coefficients.** Kato-type equivalences for $A_2$ weights *without* heat-kernel bounds, and for coefficients with critical-space lower-order terms, are unresolved.
4. **Rough geometry.** The problem on arbitrary open sets with pure Neumann conditions, and on metric-measure spaces without doubling, is open.

## 7. Current Research (as of June 2026)

- **First-order / Dirac framework.** Axelsson–Keith–McIntosh quadratic estimates for $\Pi_B$ remain the transport mechanism; groups at ANU (Bandara), Delft/TU Darmstadt (Egert, Tolksdorf, Haller-Dintelmann) and Bordeaux/Paris-Saclay (Auscher, Bortz, Hofmann's collaborators in the US) push it to bundles, boundary value problems and parabolic analogues.
- **$p$-ellipticity.** Carbonaro–Dragičević's bilinear embedding gives sharp holomorphic-calculus angles and improved $L^p$ Kato ranges; extending it to Riesz transforms with sharp constants is active. *(frontier — verify)*
- **Kato for parabolic and non-autonomous problems** ($\partial_t - \operatorname{div}(A(t,x)\nabla)$, maximal $L^p$-regularity via the square root) is a growing thread following Auscher–Egert–Nyström's work on the parabolic Dirichlet problem. *(frontier — verify)*
- **Dimension-free constants** via heat-flow/Bellman methods: reported partial progress for real symmetric $A$ only. *(frontier — verify)*
- **Applications.** The Kato theorem is the engine behind well-posedness of boundary value problems for $L$ on the half-space (Auscher–Axelsson, Hofmann–Kenig–Mayboroda–Pipher) and remains the standard reduction for $L^2$ solvability results.

## 8. Future Work

- Prove or disprove a $\Lambda/\lambda$-only, dimension-free version of (K).
- Characterise $p_\pm(L)$ intrinsically (conjecturally by the $p$-ellipticity constant of $A$).
- Remove Gaussian-bound hypotheses in the degenerate ($A_2$-weighted) setting.
- Establish the Kato equivalence on general open sets with Neumann boundary conditions, where no extension operator exists.
- Extract quantitative Carleson-measure constants from the $T(b)$ stopping-time argument, which is currently the only non-constructive step.

## 9. Key References

- **[Foundational]** T. Kato. *Fractional powers of dissipative operators.* J. Math. Soc. Japan 13 (1961), 246–274.
- **[Foundational]** J.-L. Lions. *Espaces d'interpolation et domaines de puissances fractionnaires d'opérateurs.* J. Math. Soc. Japan 14 (1962), 233–241.
- **[Foundational]** A. McIntosh. *On the comparability of $A^{1/2}$ and $A^{*1/2}$.* Proc. Amer. Math. Soc. 32 (1972), 430–434.
- **[Foundational]** R. Coifman, A. McIntosh, Y. Meyer. *L'intégrale de Cauchy définit un opérateur borné sur $L^2$ pour les courbes lipschitziennes.* Ann. of Math. 116 (1982), 361–387.
- **[Foundational]** E. Fabes, D. Jerison, C. Kenig. *Multilinear square functions and partial differential equations.* Amer. J. Math. 107 (1985), 1325–1368.
- **[SOTA]** P. Auscher, S. Hofmann, M. Lacey, A. McIntosh, Ph. Tchamitchian. *The solution of the Kato square root problem for second order elliptic operators on $\mathbb{R}^n$.* Ann. of Math. 156 (2002), 633–654.
- **[SOTA]** S. Hofmann, M. Lacey, A. McIntosh. *The solution of the Kato problem for divergence form elliptic operators with Gaussian heat kernel bounds.* Ann. of Math. 156 (2002), 623–631.
- **[SOTA]** P. Auscher, S. Hofmann, J. Lewis, Ph. Tchamitchian. *Extrapolation of Carleson measures and the analyticity of Kato's square-root operators.* Acta Math. 187 (2001), 161–190.
- **[SOTA]** A. Axelsson, S. Keith, A. McIntosh. *Quadratic estimates and functional calculi of perturbed Dirac operators.* Invent. Math. 163 (2006), 455–497.
- **[SOTA]** P. Auscher, S. Hofmann, A. McIntosh, Ph. Tchamitchian. *The Kato square root problem for higher-order elliptic operators and systems on $\mathbb{R}^n$.* J. Evol. Equ. 1 (2001), 361–385.
- **[Recent]** M. Egert, R. Haller-Dintelmann, P. Tolksdorf. *The Kato square root problem for mixed boundary conditions.* J. Funct. Anal. 267 (2014), 1419–1461.
- **[Recent]** D. Cruz-Uribe, C. Rios. *The solution of the Kato problem for degenerate elliptic operators with Gaussian bounds.* Trans. Amer. Math. Soc. 364 (2012), 3449–3478.
- **[Recent]** A. Morris. *The Kato square root problem on submanifolds.* J. London Math. Soc. 86 (2012), 879–910.
- **[Recent]** A. Carbonaro, O. Dragičević. *Convexity of power functions and bilinear embedding for divergence-form operators with complex coefficients.* J. Eur. Math. Soc. 22 (2020), 3175–3221.
- **[Survey]** P. Auscher, Ph. Tchamitchian. *Square root problem for divergence operators and related topics.* Astérisque 249, Soc. Math. France, 1998.
- **[Survey]** S. Hofmann. *A short course on the Kato problem.* Contemp. Math. 289 (2001), 61–77.
- **[Survey]** P. Auscher. *On necessary and sufficient conditions for $L^p$ estimates of Riesz transforms associated to elliptic operators on $\mathbb{R}^n$ and related estimates.* Mem. Amer. Math. Soc. 186 (2007), no. 871.
- **[Book]** T. Kato. *Perturbation Theory for Linear Operators.* Springer, 1966.

## 10. Worked Example / Concrete Special Case

**(a) Constant coefficients — why the statement is plausible.** Let $A\in \mathcal{M}_n(\mathbb{C})$ be constant with $\operatorname{Re}\langle A\xi,\xi\rangle \ge \lambda|\xi|^2$. Then $L$ is the Fourier multiplier $m(\xi)=\langle A\xi,\xi\rangle$, and $L^{1/2}$ has symbol $m(\xi)^{1/2}$ (principal branch). Since
$$\lambda|\xi|^2 \le |\langle A\xi,\xi\rangle| \le \Lambda|\xi|^2 ,$$
we get $\lambda^{1/2}|\xi| \le |m(\xi)^{1/2}| \le \Lambda^{1/2}|\xi|$, and Plancherel gives
$$\lambda^{1/2}\|\nabla u\|_2 \;\le\; \|L^{1/2}u\|_2 \;\le\; \Lambda^{1/2}\|\nabla u\|_2 .$$
The Kato estimate is here a one-line multiplier computation. All difficulty in the general case comes from $A$ varying measurably in $x$, which destroys the multiplier structure entirely.

**(b) $n=1$: the Kato estimate is the Cauchy integral.** Take $L=-\frac{d}{dx}\big(a(x)\frac{d}{dx}\big)$ on $\mathbb{R}$, with $a\in L^\infty$, $\operatorname{Re}a\ge\lambda>0$. Multiplying out,
$$\|L^{1/2}u\|_2^2 \simeq \int_0^\infty \big\| tLe^{-t^2L}u\big\|_2^2 \frac{dt}{t},\qquad tLe^{-t^2L}u = -\partial_x\big(t\,a\,\partial_x e^{-t^2L}u\big).$$
Set $f = a\,u'$. The resolvent family $(I+t^2L)^{-1}$ can be written explicitly through the Cauchy kernel on the Lipschitz graph $\Gamma = \{x + i\!\int_0^x \operatorname{Im}(1/a)\}$ after the change of variable $y(x)=\int_0^x a(s)^{-1}ds$, which is bi-Lipschitz with constants controlled by $\lambda,\Lambda$. Under this substitution $L$ becomes $-\frac{d}{dy}\frac{1}{a\circ x(y)}\frac{d}{dy}$ and the square-function bound reduces exactly to the $L^2$-boundedness of the Cauchy integral
$$C_\Gamma f(z) = \mathrm{p.v.}\int_\Gamma \frac{f(w)}{w-z}\,dw ,$$
proven by Coifman–McIntosh–Meyer (1982). This closes $n=1$.

**(c) Where the $T(b)$ enters.** Test the operator $\theta_t f = t\operatorname{div}(A f)\,$ composed with $\nabla e^{-t^2L}$ on the linear function $\ell_e(x)=x\cdot e$, $|e|=1$. One computes
$$\theta_t\mathbf{1}\cdot e = t\,\nabla e^{-t^2L}\ell_e ,$$
which is *not* zero, so no cancellation is available. Replacing $\ell_e$ by $f^\varepsilon_{Q,e} = \nabla\!\big(I+\varepsilon^2\ell(Q)^2 L\big)^{-1}\ell_e$ restores near-accretivity: on a subset $E\subset Q$ with $|E|\ge(1-\varepsilon)|Q|$ one has $\operatorname{Re}\big\langle \fint_Q f^\varepsilon_{Q,e},e\big\rangle \ge c(\lambda,\Lambda)>0$, and the Carleson packing of the exceptional sets over dyadic scales is exactly the extrapolation lemma of AHLT (2001). This is the pivot on which the 2002 solution turns.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*