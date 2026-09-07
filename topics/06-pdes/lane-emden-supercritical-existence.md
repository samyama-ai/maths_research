---
id: 06-pdes/lane-emden-supercritical-existence
title: "Super-critical Lane-Emden Equation Existence"
topic: 06-pdes
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Super-critical Lane-Emden Equation Existence

> **Topic:** Partial Differential Equations · **ID:** `06-pdes/lane-emden-supercritical-existence` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Let $\Omega \subset \mathbb{R}^n$, $n \ge 3$, be a bounded domain with smooth boundary, and let $p > 1$. Consider the Lane–Emden (Lane–Emden–Fowler) Dirichlet problem

$$-\Delta u = u^p \quad \text{in } \Omega, \qquad u > 0 \ \text{ in } \Omega, \qquad u = 0 \ \text{ on } \partial\Omega. \tag{$P_p$}$$

For subcritical $p < p_S := \frac{n+2}{n-2}$, a solution exists for **every** bounded $\Omega$ (mountain pass + compact Sobolev embedding). For $p \ge p_S$ the answer depends on $\Omega$ in a way that is still not understood.

**Open problem.** Characterize the pairs $(\Omega, p)$ with $p > p_S$ for which $(P_p)$ has a positive classical solution.

Two sharper formulations are the standing targets:

- **(A) Topological threshold.** Is there a topological/geometric invariant $\kappa(\Omega) \in \{0,1,\dots,n-3\}$ — morally the largest dimension of a "hole" carried by $\Omega$ — such that $(P_p)$ is solvable for all $p < \frac{n-\kappa+2}{n-\kappa-2}$ and unsolvable for all $p$ above that value? The exponents $p^*_{n,k} := \frac{n-k+2}{n-k-2}$ are Passaseo's *second critical exponents*.
- **(B) Bahri–Coron failure.** Bahri–Coron's theorem (nontrivial reduced homology $\Rightarrow$ existence) holds at $p = p_S$ but is false for $p > p_S$. What replaces it?

A complete resolution means either a proof of a necessary-and-sufficient criterion, or a counterexample family showing no such criterion of finite type exists.

## 2. Mathematical Foundations

**Energy functional and criticality.** Weak solutions of $(P_p)$ are critical points of
$$J_p(u) = \tfrac12 \int_\Omega |\nabla u|^2\,dx - \tfrac{1}{p+1}\int_\Omega (u^+)^{p+1}\,dx, \qquad u \in H_0^1(\Omega).$$
The embedding $H^1_0(\Omega) \hookrightarrow L^{p+1}(\Omega)$ is compact for $p+1 < 2^* = \frac{2n}{n-2}$, continuous but non-compact at $p+1 = 2^*$, and **fails entirely** for $p+1 > 2^*$. Hence for $p > p_S$ the variational framework in $H^1_0$ is unavailable: $J_p$ is not even well defined on $H^1_0(\Omega)$.

**Scaling.** The equation is invariant under $u_\lambda(x) = \lambda^{2/(p-1)} u(\lambda x)$. The exponent $p_S$ is precisely where $\frac{2}{p-1} = \frac{n-2}{2}$, i.e. where scaling preserves the Dirichlet energy.

**Pohozaev identity.** If $u \in C^2(\overline\Omega)$ solves $(P_p)$, testing with $x\cdot\nabla u$ gives
$$\Big(\frac{n-2}{2} - \frac{n}{p+1}\Big)\int_\Omega u^{p+1}\,dx \;=\; -\frac12 \int_{\partial\Omega} \Big|\frac{\partial u}{\partial\nu}\Big|^2 (x\cdot\nu)\,d\sigma. \tag{2.1}$$

**Entire problem.** On $\mathbb{R}^n$: Gidas–Spruck (1981) — no positive solution of $-\Delta u = u^p$ for $1<p<p_S$; for $p \ge p_S$ the radial singular solution is
$$u_\infty(x) = c_p |x|^{-2/(p-1)}, \qquad c_p = \Big[\tfrac{2}{p-1}\Big(n-2-\tfrac{2}{p-1}\Big)\Big]^{1/(p-1)},$$
and a smooth radial family $U_\lambda$ exists for all $p \ge p_S$. The **Joseph–Lundgren exponent**
$$p_{JL} = \begin{cases}+\infty, & 3\le n \le 10,\\[2pt] \dfrac{(n-2)^2-4n+8\sqrt{n-1}}{(n-2)(n-10)}, & n \ge 11,\end{cases}$$
separates oscillatory from monotone convergence of $U_\lambda \to u_\infty$ and governs stability (Farina, 2007: a stable solution on $\mathbb{R}^n$ is trivial iff $p < p_{JL}$).

**Second critical exponents.** For $\mathcal{T}_k^\varepsilon$, an $\varepsilon$-tubular neighbourhood of an embedded $k$-sphere in $\mathbb{R}^n$ ($0\le k \le n-3$), the $k$ "flat" directions act as parameters and the effective dimension is $n-k$, giving the threshold $p^*_{n,k} = \frac{n-k+2}{n-k-2}$, equivalently $2^*_{n,k} = \frac{2(n-k)}{n-k-2}$ in the $p+1$ variable. Note $p^*_{n,0} = p_S$.

## 3. History & State of the Art (SOTA)

- **1870s–1930s.** Lane, Emden and Fowler study $\Delta u + u^p = 0$ as a model for polytropic self-gravitating gas spheres; the radial ODE $u'' + \frac{n-1}{r}u' + u^p = 0$ is classical.
- **1965.** Pohozaev's identity (2.1): for $p \ge p_S$ and $\Omega$ star-shaped, $(P_p)$ has **no** solution. This is the first proof that domain shape, not just $p$, controls solvability.
- **1975.** Kazdan–Warner: in a radial annulus, $(P_p)$ has a radial solution for **every** $p>1$. Star-shapedness is therefore not a technical artifact.
- **1983.** Brezis–Nirenberg analyze $-\Delta u = u^{p_S} + \lambda u$, opening the systematic study of critical-exponent loss of compactness.
- **1984–1988.** Coron: existence at $p=p_S$ in a domain with a small hole. Bahri–Coron: $\tilde H_d(\Omega;\mathbb{Z}_2)\ne 0$ for some $d$ $\Rightarrow$ existence at $p = p_S$.
- **1989–1994.** Ding, and Passaseo, construct **contractible** domains admitting critical-exponent solutions — topology is sufficient but not necessary at $p=p_S$.
- **1993–1995.** Passaseo: for solid-torus-type domains in $\mathbb{R}^n$, $n\ge4$, there is **no** solution once $p \ge \frac{n+1}{n-3} = p^*_{n,1}$, while solutions do exist for $p_S \le p < p^*_{n,1}$. The Bahri–Coron mechanism dies at the second critical exponent.
- **2003–2010.** Lyapunov–Schmidt / singular-perturbation era: del Pino–Felmer–Musso (two-bubble solutions for $p = p_S+\varepsilon$), Ge–Jing–Pacard (bubble towers), del Pino–Wei (small holes, supercritical), del Pino–Musso–Pacard (concentration on boundary geodesics near $p^*_{n,1}$).
- **2006–2015.** Molle–Passaseo obtain existence for arbitrarily large $p$ in suitably shaped domains; Clapp–Faya–Pistoia use symmetry reduction to push existence past $p_S$ for domains invariant under group actions.

## 4. Partial Results / Verified Cases

| Setting | Result |
|---|---|
| $\Omega$ star-shaped, $p \ge p_S$ | No solution (Pohozaev 1965). Includes balls, convex domains. |
| Annulus $\{a<|x|<b\}$, any $n\ge2$, any $p>1$ | Radial solution exists (Kazdan–Warner 1975). |
| $\Omega$ with $\tilde H_*(\Omega;\mathbb{Z}_2)\ne0$, $p=p_S$ | Solution exists (Bahri–Coron 1988). |
| $\Omega$ contractible, $p=p_S$, $n\ge4$ | Solutions exist for suitable dumbbell/thin-tube domains (Ding 1989; Passaseo 1994). |
| Solid-torus type $\Omega\subset\mathbb{R}^n$, $n\ge4$ | Existence for $p_S \le p < \frac{n+1}{n-3}$; nonexistence for $p\ge\frac{n+1}{n-3}$ (Passaseo 1993, 1995). |
| $\Omega_\varepsilon = \Omega \setminus \overline{B_\varepsilon(q)}$, $p = p_S + \sigma$ | Solution exists for $\varepsilon,\sigma$ small; concentration at the hole (del Pino–Wei 2007). |
| $\varepsilon$-tube around a $k$-sphere, $p < p^*_{n,k}$ | Solution exists by reduction to effective dimension $n-k$. |
| $p = p_S + \varepsilon$, $\varepsilon \downarrow 0$, $\Omega$ with a hole | Multi-bubble and bubble-tower solutions (del Pino–Felmer–Musso 2003; Ge–Jing–Pacard 2005). |
| $\Omega$ with $O(m)$-symmetry, $p$ below the symmetric critical exponent | Existence and multiplicity (Clapp–Faya–Pistoia 2013). |
| $\Omega = \mathbb{R}^n$, $1<p<p_S$ | No positive solution (Gidas–Spruck 1981). |
| $\Omega = \mathbb{R}^n$, stable solutions, $p<p_{JL}$ | Only $u\equiv0$ (Farina 2007). |

## 5. Principal Obstacles

- **No variational structure.** For $p>p_S$, $\int_\Omega u^{p+1}$ is infinite on generic $H^1_0$ functions. Mountain-pass, Nehari-manifold, and min–max arguments — the entire toolkit that solves the subcritical case — do not even start. Working in $C^{2,\alpha}$ or $W^{2,q}$ restores the functional but destroys the Hilbert-space geometry and the Palais–Smale machinery.
- **Topological invariants stop predicting.** Passaseo's counterexamples show that $\tilde H_*(\Omega)\ne0$ is compatible with nonexistence when $p$ is large. So the correct invariant must be metric/geometric (curvature, thickness, dimension of the collapsing set), not homotopy-theoretic — and no such invariant has been isolated.
- **Perturbative methods are local in $p$.** Lyapunov–Schmidt reductions build solutions for $p = p^*_{n,k} \pm \varepsilon$ using explicit bubbles $U_\lambda$ as approximate solutions. They give no information for $p$ far from a critical exponent, where no ansatz is known.
- **Degenerate linearized operator.** The linearization $-\Delta - pU_\lambda^{p-1}$ around a bubble has a kernel from translations and dilations whose decay worsens as $p$ grows; invertibility estimates in weighted spaces degenerate, and for $p > p_{JL}$ the Hardy-type constant $p\,c_p^{p-1}$ crosses $\frac{(n-2)^2}{4}$, flipping the sign structure of the associated quadratic form.
- **A priori bounds are missing.** For $p>p_S$ there is no Gidas–Spruck blow-up analysis: rescaling limits may be the singular solution $u_\infty$ rather than a smooth bubble, so continuation/degree arguments in $p$ cannot be closed.

## 6. The Gap

Proven: nonexistence for star-shaped $\Omega$ (all $p\ge p_S$), and a two-sided answer for **model domains** — round annuli, tubes around $k$-spheres, domains with one small hole — near the discrete ladder $p^*_{n,k}$. Conjectured: the same ladder governs **all** smooth bounded domains, via an invariant $\kappa(\Omega)$.

The precise missing step is a **nonexistence theorem for general domains above a geometric threshold**: a Pohozaev-type or blow-up argument showing that if every "hole" of $\Omega$ has dimension $\le k$ (in a sense to be made intrinsic), then $(P_p)$ has no solution for $p \ge p^*_{n,k}$. Only the $k=0$ case (star-shaped $\Rightarrow$ no solution for $p\ge p_S$) and Passaseo's $k=1$ model case are known. Symmetrically, no existence theorem covers $p$ far above $p_S$ in a domain not built by hand.

## 7. Current Research (as of June 2026)

- **Geometric reduction / concentration on submanifolds.** Groups around del Pino (Bath), Musso (Bath), Pacard (École polytechnique), Wei (UBC/Chinese University of Hong Kong) refine gluing methods that produce solutions concentrating on $k$-dimensional sets as $p \uparrow p^*_{n,k}$. The programme aims at a converse: concentration sets must exist, forcing nonexistence when the domain has none. *(frontier — verify)*
- **Symmetry and equivariant reduction.** Clapp (UNAM) and Pistoia (Sapienza Roma) exploit group actions to convert supercritical problems into critical or subcritical ones on quotients, yielding existence for exponents far above $p_S$ in symmetric domains.
- **Stability, Morse index and $p_{JL}$.** Farina-type classification is being pushed to bounded domains: bounding the Morse index of solutions of $(P_p)$ uniformly in $p$ would give the missing a priori estimates. *(frontier — verify)*
- **Singular and weak solutions.** Relaxing to $H^1$ distributional solutions with possible singular sets (Dávila's programme) changes the answer: singular solutions can exist where classical ones do not, and the classification of admissible singular sets is active.
- **Numerical continuation.** Path-following in $p$ on dumbbell and torus domains provides evidence for the sharpness of $p^*_{n,k}$ but no proofs.

## 8. Future Work

1. **Intrinsic definition of $\kappa(\Omega)$.** Find a metric invariant (e.g. the largest $k$ such that $\Omega$ admits a $k$-dimensional "core" with uniformly bounded normal injectivity radius) reproducing the known model cases.
2. **Supercritical Pohozaev.** Seek vector fields $X$ replacing $x$ in (2.1) whose deformation tensor detects $k$-dimensional holes, generalizing star-shapedness.
3. **Blow-up analysis above $p_S$.** Classify possible rescaling limits, including $u_\infty$, and prove compactness of solution sets on compact $p$-ranges.
4. **Non-perturbative existence.** Develop degree theory in weighted Hölder spaces where the linearization is Fredholm for all $p$, decoupling existence from proximity to $p^*_{n,k}$.
5. **Sharpness at the threshold.** Decide existence exactly **at** $p = p^*_{n,k}$ for tube domains — the analogue of the delicate $p=p_S$ case.

## 9. Key References

- **[Foundational]** S. I. Pohozaev. *Eigenfunctions of the equation $\Delta u + \lambda f(u) = 0$.* Soviet Mathematics Doklady, 6 (1965), 1408–1411.
- **[Foundational]** J. L. Kazdan, F. W. Warner. *Remarks on some quasilinear elliptic equations.* Communications on Pure and Applied Mathematics, 28 (1975), 567–597.
- **[Foundational]** D. D. Joseph, T. S. Lundgren. *Quasilinear Dirichlet problems driven by positive sources.* Archive for Rational Mechanics and Analysis, 49 (1973), 241–269.
- **[Foundational]** B. Gidas, J. Spruck. *Global and local behavior of positive solutions of nonlinear elliptic equations.* Communications on Pure and Applied Mathematics, 34 (1981), 525–598.
- **[Foundational]** H. Brezis, L. Nirenberg. *Positive solutions of nonlinear elliptic equations involving critical Sobolev exponents.* Communications on Pure and Applied Mathematics, 36 (1983), 437–477.
- **[Foundational]** A. Bahri, J.-M. Coron. *On a nonlinear elliptic equation involving the critical Sobolev exponent: the effect of the topology of the domain.* Communications on Pure and Applied Mathematics, 41 (1988), 253–294.
- **[Foundational]** J.-M. Coron. *Topologie et cas limite des injections de Sobolev.* Comptes Rendus de l'Académie des Sciences Paris, Série I, 299 (1984), 209–212.
- **[Key]** D. Passaseo. *Nonexistence results for elliptic problems with supercritical nonlinearity in nontrivial domains.* Journal of Functional Analysis, 114 (1993), 97–105.
- **[Key]** D. Passaseo. *New nonexistence results for elliptic equations with supercritical nonlinearity.* Differential and Integral Equations, 8 (1995), 577–586.
- **[Key]** W.-Y. Ding. *Positive solutions of $\Delta u + u^{(n+2)/(n-2)} = 0$ on contractible domains.* Journal of Partial Differential Equations, 2 (1989), 83–88.
- **[SOTA / Recent]** M. del Pino, P. Felmer, M. Musso. *Two-bubble solutions in the super-critical Bahri–Coron's problem.* Calculus of Variations and Partial Differential Equations, 16 (2003), 113–145.
- **[SOTA / Recent]** Y. Ge, R. Jing, F. Pacard. *Bubble towers for supercritical semilinear elliptic equations.* Journal of Functional Analysis, 221 (2005), 251–302.
- **[SOTA / Recent]** M. del Pino, J. Wei. *Supercritical elliptic problems in domains with small holes.* Annales de l'Institut Henri Poincaré, Analyse Non Linéaire, 24 (2007), 507–520.
- **[SOTA / Recent]** M. del Pino, M. Musso, F. Pacard. *Bubbling along boundary geodesics near the second critical exponent.* Journal of the European Mathematical Society, 12 (2010), 1553–1605.
- **[SOTA / Recent]** R. Molle, D. Passaseo. *Nonlinear elliptic equations with large supercritical exponents.* Calculus of Variations and Partial Differential Equations, 26 (2006), 201–225.
- **[SOTA / Recent]** M. Clapp, J. Faya, A. Pistoia. *Nonexistence and multiplicity of solutions to elliptic problems with supercritical exponents.* Calculus of Variations and Partial Differential Equations, 48 (2013), 611–623.
- **[SOTA / Recent]** A. Farina. *On the classification of solutions of the Lane–Emden equation on unbounded domains of $\mathbb{R}^N$.* Journal de Mathématiques Pures et Appliquées, 87 (2007), 537–561.
- **[Survey]** M. del Pino. *Supercritical elliptic problems from a perturbation viewpoint.* Discrete and Continuous Dynamical Systems, 21 (2008), 69–89.
- **[Survey]** J. Dávila. *Singular solutions of semi-linear elliptic problems.* In Handbook of Differential Equations: Stationary Partial Differential Equations, Vol. 6, Elsevier, 2008, 83–176.

## 10. Worked Example / Concrete Special Case

**The dichotomy in $n=4$: ball versus annulus, at $p = 5 > p_S = 3$.**

*Nonexistence in the ball $B_1 \subset \mathbb{R}^4$.* Suppose $u$ solves $-\Delta u = u^5$, $u>0$ in $B_1$, $u=0$ on $\partial B_1$. Multiply by $x\cdot\nabla u$ and integrate; with $n=4$, $p+1=6$, identity (2.1) reads
$$\Big(\frac{4-2}{2} - \frac{4}{6}\Big)\int_{B_1} u^6 = \Big(1 - \frac23\Big)\int_{B_1} u^6 = \frac13\int_{B_1}u^6 = -\frac12\int_{\partial B_1}|\partial_\nu u|^2 (x\cdot\nu)\,d\sigma.$$
On $\partial B_1$, $x\cdot\nu = 1$, so the right side is $-\frac12\int_{\partial B_1}|\partial_\nu u|^2 \le 0$ while the left side is $>0$ unless $u\equiv0$. Contradiction. The same computation kills every star-shaped domain and every $p\ge3$.

*Existence in the annulus $A = \{1<|x|<2\}\subset\mathbb{R}^4$.* Restrict to radial functions. Writing $u=u(r)$, the equation is $u'' + \frac{3}{r}u' + u^5 = 0$ on $(1,2)$, $u(1)=u(2)=0$. Set
$$H = \{u \in H_0^1(A) : u \text{ radial}\}, \qquad \|u\|^2 = \int_A |\nabla u|^2 = \omega_3\int_1^2 |u'(r)|^2 r^3\,dr,$$
with $\omega_3 = 2\pi^2$. Since $r \in [1,2]$ is bounded away from $0$, the weight $r^3 \in [1,8]$ is comparable to $1$, so $\|\cdot\|$ is equivalent to the one-dimensional $H_0^1(1,2)$ norm. By the 1-D Sobolev embedding $H^1_0(1,2)\hookrightarrow C^{0,1/2}([1,2])$,
$$\|u\|_{L^\infty} \le \Big(\int_1^2 |u'|^2\,dr\Big)^{1/2} \le \|u\|/\sqrt{\omega_3},$$
and the embedding $H \hookrightarrow L^q(A)$ is **compact for every $q<\infty$** — the supercritical obstruction has vanished on the radial subspace.

Now minimize on the Nehari manifold
$$c = \inf\Big\{ \tfrac12\|u\|^2 - \tfrac16\int_A u^6 \;:\; u\in H\setminus\{0\},\ \|u\|^2 = \int_A |u|^6 \Big\} = \tfrac13 \inf_{\|u\|^2=\int u^6} \|u\|^2 > 0.$$
Equivalently $c = \frac13 S_A^{3/2}$ with $S_A = \inf_{u\in H\setminus\{0\}} \|u\|^2 / \|u\|_{L^6}^{2}$. Compactness gives a minimizer $u_0 \ge 0$, $u_0 \not\equiv 0$; the Euler–Lagrange equation plus a scaling normalization yields $-\Delta u_0 = u_0^5$ in $A$. Radial symmetry of $A$ means the Palais principle of symmetric criticality applies, so $u_0$ solves the full problem, and the strong maximum principle gives $u_0>0$. Elliptic regularity ($u_0\in L^\infty \Rightarrow u_0 \in C^{2,\alpha}$) makes it classical.

*Reading the example.* Both domains are smooth, bounded, and $4$-dimensional; they differ only in that $A$ is not star-shaped and carries a $2$-sphere. Here $\kappa(A)$ behaves like $n-3=1$ in the ladder — but for a solid torus in $\mathbb{R}^4$, i.e. a tube around $S^1$, Passaseo's threshold is $p^*_{4,1}=\frac{4-1+2}{4-1-2}=5$, and $p=5$ is exactly where solutions disappear. The annulus (a tube around a point set of the *radial* variable, effective dimension $1$) admits solutions for every $p$; the torus does not. Producing an invariant that predicts both outcomes for an arbitrary domain is the open problem.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*