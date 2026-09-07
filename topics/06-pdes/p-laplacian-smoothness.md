---
id: 06-pdes/p-laplacian-smoothness
title: "P Laplacian Smoothness"
topic: 06-pdes
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Optimal Regularity for the p-Laplacian (the $C^{p'}$-Conjecture)

> **Topic:** Partial Differential Equations · **ID:** `06-pdes/p-laplacian-smoothness` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Let $\Omega \subset \mathbb{R}^n$ be open, $p > 2$, and let $u \in W^{1,p}_{\mathrm{loc}}(\Omega)$ be a weak solution of the $p$-Poisson equation
$$-\Delta_p u := -\operatorname{div}\big(|\nabla u|^{p-2}\nabla u\big) = f \quad \text{in } \Omega, \qquad f \in L^\infty_{\mathrm{loc}}(\Omega).$$

**Conjecture ($C^{p'}$-regularity).** $u \in C^{1,\frac{1}{p-1}}_{\mathrm{loc}}(\Omega)$, with the estimate
$$\|u\|_{C^{1,\frac{1}{p-1}}(B_{1/2})} \le C(n,p)\Big(\|u\|_{L^\infty(B_1)} + \|f\|_{L^\infty(B_1)}^{\frac{1}{p-1}}\Big).$$

Here $p' = p/(p-1)$ is the conjugate exponent and $1/(p-1) = p'-1$, so the assertion is that $u$ has the regularity of the model function $|x_1|^{p'}$ — hence the name. A complete resolution requires either a proof valid for all $n \ge 3$ and all $p > 2$, or a counterexample: a solution with $f \in L^\infty$ whose gradient fails to be $\frac{1}{p-1}$-Hölder.

A companion, strictly harder question is the **optimal interior regularity of $p$-harmonic functions** ($f \equiv 0$): determine the largest $\alpha = \alpha(n,p)$ with $\nabla u \in C^{0,\alpha}_{\mathrm{loc}}$. This is settled in $n=2$ and open for every $n \ge 3$ and every $p \ne 2$.

## 2. Mathematical Foundations

**Weak formulation.** $u$ solves $-\Delta_p u = f$ weakly if
$$\int_\Omega |\nabla u|^{p-2}\nabla u \cdot \nabla \varphi \,dx = \int_\Omega f\varphi\,dx \qquad \forall \varphi \in C_c^\infty(\Omega).$$
It is the Euler–Lagrange equation of the $p$-Dirichlet energy $\mathcal{E}[u]=\int_\Omega \big(\tfrac{1}{p}|\nabla u|^p - fu\big)dx$, strictly convex for $1<p<\infty$, so minimizers over $u_0 + W^{1,p}_0(\Omega)$ exist and are unique.

**Degeneracy.** In non-divergence form (where $\nabla u\ne0$),
$$\Delta_p u = |\nabla u|^{p-2}\Big(\Delta u + (p-2)\,\Delta_\infty^N u\Big), \qquad \Delta_\infty^N u = \frac{\nabla u^{\top} D^2u\,\nabla u}{|\nabla u|^2}.$$
The coefficient matrix $A(\xi) = |\xi|^{p-2}\big(I + (p-2)\tfrac{\xi\otimes\xi}{|\xi|^2}\big)$ has eigenvalues $|\xi|^{p-2}$ (multiplicity $n-1$) and $(p-1)|\xi|^{p-2}$; the ellipticity ratio is the constant $p-1$, but both eigenvalues **degenerate to $0$** as $\xi\to0$ when $p>2$ (and blow up when $1<p<2$, the *singular* case). The whole difficulty lives on the critical set $\{\nabla u = 0\}$.

**Monotonicity.** For $p\ge2$ there is $c(p)>0$ with
$$\big(|\xi|^{p-2}\xi - |\eta|^{p-2}\eta\big)\cdot(\xi-\eta) \ \ge\ c(p)\,|\xi-\eta|^{p},$$
and for $1<p<2$, $\ \ge c(p)|\xi-\eta|^2(|\xi|+|\eta|)^{p-2}$. These drive uniqueness and the Caccioppoli estimates.

**Known baseline (Uraltseva; Uhlenbeck; Evans; Lewis; DiBenedetto; Tolksdorf).** For $f\in L^\infty_{\mathrm{loc}}$ and $1<p<\infty$ there exists $\alpha_0 = \alpha_0(n,p)\in(0,1)$, **not explicit**, with $u\in C^{1,\alpha_0}_{\mathrm{loc}}(\Omega)$. The conjecture asks for the sharp value in the $f\in L^\infty$ regime.

**Stress field.** The natural regular object is $V := |\nabla u|^{\frac{p-2}{2}}\nabla u$ or $W := |\nabla u|^{p-2}\nabla u$; these are smoother than $\nabla u$ itself and satisfy $V\in W^{1,2}_{\mathrm{loc}}$.

## 3. History & State of the Art (SOTA)

- **1968.** Uraltseva proves interior $C^{1,\alpha}$ regularity for $p$-harmonic functions, $p\ge2$.
- **1977.** Uhlenbeck extends $C^{1,\alpha}$ to degenerate elliptic *systems* with $|\nabla u|^{p-2}$ structure (*Acta Math.*).
- **1982–1984.** Evans, Lewis, DiBenedetto and Tolksdorf give independent proofs covering $1<p<\infty$, general right-hand sides and lower-order terms.
- **1988–1989.** Iwaniec–Manfredi and Bojarski–Iwaniec use complex-analytic/hodograph methods to compute the **exact** planar exponent.
- **1998.** Lindqvist's *Notes on the p-Laplace equation* consolidates the field; the sharp exponent in $n\ge3$ is stated as open.
- **2014–2017.** Teixeira, Araújo, Ricarte develop geometric tangential methods giving $C^{1,\alpha}$ with $\alpha \to \frac{1}{p-1}$ in suitable asymptotic regimes; the $C^{p'}$-conjecture is formulated explicitly in this form.
- **2017.** Araújo–Teixeira–Urbano prove the $C^{p'}$-conjecture in the plane, $n=2$, $p>2$.
- **2018–2020.** Cianchi–Maz'ya (second-order estimates for $W=|\nabla u|^{p-2}\nabla u$, including global/convex-domain versions) and Dong–Peng–Zhang–Zhou (Hessian estimates via a fundamental pointwise inequality) sharpen the Sobolev-side theory.

**SOTA summary.** Sharp $C^{1,\alpha}$ exponent known: $n=2$ only. $C^{p'}$-conjecture: proven $n=2$; open $n\ge3$.

## 4. Partial Results / Verified Cases

- **$p=2$:** trivial — $u$ is harmonic (or $f\in L^\infty \Rightarrow u \in C^{1,\alpha}$ for all $\alpha<1$, and $\frac{1}{p-1}=1$ is the known-false endpoint, so the conjecture is stated for $p>2$).
- **$n=2$, all $p>2$, $f\in L^\infty$:** $u\in C^{1,\frac{1}{p-1}}_{\mathrm{loc}}$ — Araújo–Teixeira–Urbano (*Adv. Math.* 316, 2017).
- **$n=2$, $f\equiv0$:** exact regularity of $p$-harmonic functions (Iwaniec–Manfredi 1989): $u\in C^{k,\beta}_{\mathrm{loc}}$ where
$$k+\beta = \frac{1}{6}\left(7 + \frac{1}{p-1} + \sqrt{1+\frac{14}{p-1}+\frac{1}{(p-1)^2}}\right),$$
which $\to \frac{4}{3}$ as $p\to\infty$, matching the $C^{1,1/3}$ regularity of planar $\infty$-harmonic functions (Savin 2005; Evans–Savin 2008).
- **$n\ge3$, $f\equiv0$:** $C^{1,\alpha_0}$ for a non-explicit $\alpha_0(n,p)$; no sharp value, no counterexample below $\frac{1}{p-1}$.
- **Second-order regularity, all $n$, all $p>1$:** $|\nabla u|^{p-2}\nabla u \in W^{1,2}_{\mathrm{loc}}$ when $f\in L^2_{\mathrm{loc}}$ (Cianchi–Maz'ya, *ARMA* 2018); and $|\nabla u|^{\frac{p-2}{2}}\nabla u\in W^{1,2}_{\mathrm{loc}}$ (Damascelli–Sciunzi 2004; Dong–Peng–Zhang–Zhou 2020).
- **Asymptotic regimes:** $C^{1,\alpha}$ with $\alpha \to \frac{1}{p-1}$ as $p\to\infty$, and improved exponents when $f$ vanishes on $\{\nabla u=0\}$ or $f\in L^q$, $q>n$, with $\alpha = \min\{\alpha_0^-,\ \tfrac{1}{p-1}(1-\tfrac{n}{q})\}$ (Teixeira, *Nonlinearity* 2017).
- **Radial / one-dimensional solutions:** the conjecture is elementary and sharp (Section 10).
- **$1<p<2$ (singular case), $f\in L^\infty$:** $u\in C^{1,\alpha}$ for all $\alpha<1$ is known; the conjectured $\frac{1}{p-1}>1$ is not the right scaling, so the $C^{p'}$ statement is specific to $p>2$.

## 5. Principal Obstacles

- **No uniform ellipticity.** Linear Schauder and Calderón–Zygmund theory require $\lambda I \le A \le \Lambda I$ with $\lambda>0$. On $\{\nabla u=0\}$ the modulus $|\nabla u|^{p-2}$ vanishes; every perturbative argument must be run on a scale where $|\nabla u|$ is bounded below, then patched.
- **Failure of intrinsic scaling to close.** The equation is invariant under $u\mapsto \lambda^{-1}u(\lambda x)$ only for $f=0$; with $f\ne0$ the natural rescaling $u_r(x)=\frac{u(x_0+rx)}{r^{1+\frac{1}{p-1}}}$ produces $\|f\|$ terms that are exactly borderline — this is why $\frac{1}{p-1}$ is the critical exponent and why no room is left for an $\varepsilon$-loss.
- **The plane is special.** The $n=2$ proofs (Iwaniec–Manfredi, and the hodograph/quasiregular-map route of Bojarski–Iwaniec) use that $\nabla u$ can be identified with a quasiregular map $\mathbb{C}\to\mathbb{C}$, giving unique continuation and isolated critical points with integer-like local degrees. In $n\ge3$ the critical set $\{\nabla u=0\}$ can be large (Krol'–Maz'ya-type examples show non-smoothness phenomena) and no such structure theory exists.
- **Linearization is degenerate.** Differentiating the equation gives $\operatorname{div}(A(\nabla u)\nabla u_{x_i}) = f_{x_i}$; with $f$ only in $L^\infty$ the right-hand side is a distribution of negative order, and $A(\nabla u)$ is a *non-explicit* $C^{0,\alpha_0}$ matrix. Bootstrapping stalls immediately.
- **Compactness arguments lose the exponent.** Geometric tangential methods transfer regularity from the $f\equiv0$ limit profile. Since the sharp exponent for $p$-harmonic functions in $n\ge3$ is itself unknown, the method can only deliver $\min\{\alpha_0,\frac{1}{p-1}\}$ — and $\alpha_0$ is the unknown.

## 6. The Gap

Proven: $n=2$ (all $p>2$), plus $n\ge3$ with the non-explicit exponent $\alpha_0(n,p)$ and the $q>n$ integrability trade-off. Conjectured: $\alpha = \frac{1}{p-1}$ for all $n\ge2$, $p>2$, $f\in L^\infty$.

The precise missing step is a **dimension-free lower bound $\alpha_0(n,p)\ge \frac{1}{p-1}$ for $p$-harmonic functions in $n\ge3$**. Equivalently: show that at a critical point $x_0$ of a $p$-harmonic function, the oscillation of $\nabla u$ on $B_r(x_0)$ is $O(r^{1/(p-1)})$. Every known route to this needs either (a) a quantitative estimate on the size/structure of $\{\nabla u=0\}$ in $n\ge3$, or (b) a monotonicity formula for $\int_{\partial B_r}|\nabla u|^p$ with the correct homogeneity — neither exists. Note the barrier is one-sided: no counterexample with $\alpha<\frac{1}{p-1}$ is known either, so the conjecture may fail only via a sharper-than-expected obstruction on a fractal critical set.

## 7. Current Research (as of June 2026)

- **Geometric tangential analysis** (Teixeira, Araújo, Urbano, Ricarte; UFC Fortaleza, Coimbra, Central Florida): pushing the $n=2$ proof to $n\ge3$ by improved flatness/approximation lemmas. Partial dimension-dependent gains reported. *(frontier — verify)*
- **Nonlinear potential theory** (Kuusi–Mingione, Aalto/Turin/Parma): Wolff-potential pointwise bounds $|\nabla u(x)| \lesssim \mathbf{W}^{f}_{1/p,p}(x,r) + \fint_{B_r}|\nabla u|$, giving sharp gradient continuity criteria under Lorentz $L(n,1)$ data — the correct scale-invariant substitute for $L^\infty$.
- **Second-order/Sobolev route** (Cianchi–Maz'ya, Balci–Diening–Weimar): upgrading $W\in W^{1,2}$ to fractional $W^{1+s,q}$ estimates on $\nabla u$, aiming to reach $\frac{1}{p-1}$ via embedding.
- **Viscosity-solution and $\infty$-Laplacian techniques** (Savin, Crandall, Peres–Schramm–Sheffield–Wilson tug-of-war): the $p\to\infty$ endpoint $C^{1,1/3}$ in the plane remains open in $n\ge3$ and is regarded as the same barrier in disguise.
- **Numerical probing**: adaptive FEM computations of $p$-harmonic functions with prescribed singular boundary data have not produced any candidate counterexample beating $\frac{1}{p-1}$ in $n=3$. *(frontier — verify)*

## 8. Future Work

- Establish a **Federer–Almgren-type frequency function** for $\Delta_p$ that is monotone in $r$; this is the single most-cited missing tool.
- Prove the conjecture for **$p$ large** ($p\gg n$), where the equation is close to $\Delta_\infty$ and the $\frac{1}{p-1}\to0$ target is weakest.
- Settle the **$n=3$, $f\equiv0$** sharp exponent, even non-constructively.
- Extend to **anisotropic and $p(x)$-Laplacians** and to the **fractional $p$-Laplacian**, where the analogous sharp exponent is open for every $s\in(0,1)$.
- Construct a $p$-harmonic function in $\mathbb{R}^3$ with critical set of positive $\mathcal{H}^{n-2}$-measure and controlled gradient decay — a disproof strategy.

## 9. Key References

- **[Foundational]** N. N. Uraltseva. *Degenerate quasilinear elliptic systems.* Zap. Nauchn. Sem. LOMI 7 (1968), 184–222.
- **[Foundational]** K. Uhlenbeck. *Regularity for a class of non-linear elliptic systems.* Acta Mathematica 138 (1977), 219–240.
- **[Foundational]** L. C. Evans. *A new proof of local $C^{1,\alpha}$ regularity for solutions of certain degenerate elliptic P.D.E.* Journal of Differential Equations 45 (1982), 356–373.
- **[Foundational]** E. DiBenedetto. *$C^{1+\alpha}$ local regularity of weak solutions of degenerate elliptic equations.* Nonlinear Analysis 7 (1983), 827–850.
- **[Foundational]** P. Tolksdorf. *Regularity for a more general class of quasilinear elliptic equations.* Journal of Differential Equations 51 (1984), 126–150.
- **[Foundational]** J. L. Lewis. *Regularity of the derivatives of solutions to certain degenerate elliptic equations.* Indiana University Mathematics Journal 32 (1983), 849–858.
- **[Sharp planar case]** T. Iwaniec, J. J. Manfredi. *Regularity of p-harmonic functions on the plane.* Revista Matemática Iberoamericana 5 (1989), 1–19.
- **[SOTA]** D. J. Araújo, E. V. Teixeira, J. M. Urbano. *A proof of the $C^{p'}$-regularity conjecture in the plane.* Advances in Mathematics 316 (2017), 541–553.
- **[SOTA]** E. V. Teixeira. *Regularity for the fully nonlinear dead-core problem* and *Sharp regularity for general Poisson equations with borderline sources.* J. Math. Pures Appl. 99 (2013), 150–164.
- **[SOTA]** A. Cianchi, V. G. Maz'ya. *Second-order two-sided estimates in nonlinear elliptic problems.* Archive for Rational Mechanics and Analysis 229 (2018), 569–599.
- **[SOTA]** H. Dong, F. Peng, Y. Zhang, Y. Zhou. *Hessian estimates for equations involving p-Laplacian via a fundamental inequality.* Advances in Mathematics 370 (2020), 107212.
- **[Potential theory]** T. Kuusi, G. Mingione. *Guide to nonlinear potential estimates.* Bulletin of Mathematical Sciences 4 (2014), 1–82.
- **[Survey]** P. Lindqvist. *Notes on the Stationary p-Laplace Equation.* SpringerBriefs in Mathematics, Springer, 2019.
- **[Survey]** J. M. Urbano. *The method of intrinsic scaling.* Lecture Notes in Mathematics 1930, Springer, 2008.

## 10. Worked Example / Concrete Special Case

**Sharpness of the exponent $\frac{1}{p-1}$, with $p=4$, $n$ arbitrary.**

Take $u(x) = c\,|x_1|^{4/3}$ on $\mathbb{R}^n$, $c>0$. Then $\nabla u = \tfrac{4}{3}c\,|x_1|^{1/3}\operatorname{sgn}(x_1)\,e_1$, so $|\nabla u| = \tfrac43 c|x_1|^{1/3}$ and
$$|\nabla u|^{2}\nabla u = \Big(\tfrac43 c\Big)^{3}|x_1|^{2/3}\cdot|x_1|^{1/3}\operatorname{sgn}(x_1)\,e_1 = \tfrac{64}{27}c^3\,x_1\,e_1 .$$
Hence
$$\Delta_4 u = \partial_{x_1}\Big(\tfrac{64}{27}c^3 x_1\Big) = \tfrac{64}{27}c^3 = \text{const}.$$
Choosing $c = \tfrac34$ gives $\Delta_4 u \equiv 1$, i.e. $-\Delta_4 u = f$ with $f \equiv -1 \in L^\infty$. Note the identity $|\nabla u|^{p-2}\nabla u$ is *smooth* (linear) even though $\nabla u$ is not — this is exactly the phenomenon behind the Cianchi–Maz'ya second-order theory.

Now measure $\nabla u$: for $x_1 = t > 0$,
$$|\nabla u(t e_1) - \nabla u(0)| = \tfrac{4}{3}\cdot\tfrac34\, t^{1/3} = t^{1/3}.$$
So $\nabla u \in C^{0,1/3}$ and **not** $C^{0,\beta}$ for any $\beta > 1/3$. Since $\frac{1}{p-1} = \frac13$ for $p=4$, the conjectured exponent is attained with equality: the conjecture is optimal and admits no $\varepsilon$-improvement.

**Contrast with $f\equiv0$.** The same profile is not $4$-harmonic ($\Delta_4 u = 1 \ne 0$). For $f\equiv0$ in the plane, Iwaniec–Manfredi give $k+\beta = \tfrac16\big(7+\tfrac13+\sqrt{1+\tfrac{14}{3}+\tfrac19}\big) = \tfrac16\big(\tfrac{22}{3}+\tfrac{\sqrt{52}}{3}\big) \approx 1.622$, i.e. $\nabla u \in C^{0,0.622}$ — far better than $1/3$. The gap between $0.622$ (source-free, $n=2$) and $1/3$ (bounded source, any $n$) is precisely the content of Sections 4–6: the source term, not the degeneracy alone, caps the regularity at $\frac{1}{p-1}$, and proving that cap is achieved for $n\ge3$ is the open problem.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*