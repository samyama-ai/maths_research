---
id: 06-pdes/degasperis-procesi-global-existence
title: "Degasperis Procesi Global Existence"
topic: 06-pdes
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Global Existence vs. Wave Breaking for the Degasperis–Procesi Equation

> **Topic:** Partial Differential Equations · **ID:** `06-pdes/degasperis-procesi-global-existence` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

The Degasperis–Procesi (DP) equation on the line,
$$u_t - u_{txx} + 4uu_x = 3u_xu_{xx} + uu_{xxx}, \qquad u(0,x)=u_0(x),$$
is locally well posed in $H^s(\mathbb{R})$ for $s>3/2$, and its solutions either exist for all time or break in finite time with $\sup_x u(t,x)$ bounded and $\inf_x u_x(t,x)\to-\infty$ (wave breaking). The open problem has three linked parts.

**(P1) Sharp criterion.** Characterize, in terms of the initial momentum density $y_0=u_0-u_0''$ alone, exactly which data yield global classical solutions. Conjecturally the criterion is of *McKean type*: wave breaking occurs if and only if some positive part of $y_0$ lies strictly to the right of some negative part, i.e. iff there exist $x<z$ with $y_0$ (as a measure) charging $(-\infty,x]$ positively and $[z,\infty)$ negatively in a suitable ordered sense. A complete solution must prove both implications for all $u_0\in H^s$, $s>3/2$ (equivalently $y_0\in\mathcal{M}(\mathbb{R})$ in the weak setting).

**(P2) Weak-solution theory.** Prove or disprove uniqueness of global entropy weak solutions of the conservative form in $L^\infty\cap BV$ and, more sharply, in $L^2(\mathbb{R})$ — the natural energy class — including solutions containing shockpeakons.

**(P3) Uniform bounds.** Decide whether $\|u(t)\|_{L^\infty}$ stays bounded uniformly in $t$ for all $H^s$ data, or whether it can grow without bound; no conserved $H^1$ norm is available to force the former.

A complete proof of (P1) means a necessary-and-sufficient condition; a disproof means an explicit datum violating the conjectured equivalence in either direction.

## 2. Mathematical Foundations

Write $y=u-u_{xx}$. The DP equation is the $b=3$ member of the *b-family*
$$y_t+uy_x+b\,u_xy=0, \qquad y=(1-\partial_x^2)u,$$
of which only $b=2$ (Camassa–Holm, CH) and $b=3$ (DP) are integrable. With $G(x)=\tfrac12e^{-|x|}$, the Green function of $1-\partial_x^2$, DP is equivalent to the nonlocal transport form
$$u_t+uu_x+\partial_x G*\!\left(\tfrac32u^2\right)=0,$$
and to the conservation law $u_t+\partial_x\big(\tfrac12u^2+\tfrac32 G*u^2\big)=0$, which makes sense for $u\in L^2$ and is the basis of the entropy theory.

**Lax pair / integrability.** DP admits the $3\times3$ Lax pair
$$\psi_x-\psi_{xxx}=\lambda y\psi,\qquad \psi_t=\tfrac{1}{\lambda}\psi_{xx}-u\psi_x+\left(u_x+\tfrac{2}{3\lambda}\right)\psi,$$
and a bi-Hamiltonian structure (Degasperis–Holm–Hone 2002).

**Conservation laws.** Unlike CH, DP has *no* conserved $H^1$ energy. Its useful invariants are
$$E_1=\int_{\mathbb R} y\,dx,\qquad E_2=\int_{\mathbb R} y\,v\,dx \ \ \text{with}\ (4-\partial_x^2)v=u,\qquad E_3=\int_{\mathbb R}u^3\,dx,$$
and $E_2$ is equivalent to $\|u\|_{L^2}^2$: $\tfrac14\|u\|_{L^2}^2\le E_2\le \|u\|_{L^2}^2$ up to fixed constants. So the coercive a priori control is $L^2$ only.

**Sign persistence.** Along the flow map $q(t,x)$ defined by $q_t=u(t,q)$, $q(0,x)=x$, one has the exact transport identity
$$y(t,q(t,x))\,q_x(t,x)^3=y_0(x),$$
so $q_x>0$ implies $\operatorname{sign} y$ is preserved. (For CH the exponent is $2$; the cubic weight is the source of DP's stronger nonlinear amplification.)

**Blow-up scenario (Liu–Yin 2006).** The maximal existence time $T$ is finite iff
$$\liminf_{t\uparrow T}\ \inf_{x}u_x(t,x)=-\infty,$$
with $\|u(t)\|_{L^\infty}$ remaining finite: solutions break like a wave, they do not blow up in amplitude.

**Peakons and shockpeakons.** $u(t,x)=c\,e^{-|x-ct|}$ is a weak solution for every $c\in\mathbb{R}$; $N$-peakons $u=\sum_{j}p_je^{-|x-x_j|}$ obey
$$\dot x_j=u(x_j),\qquad \dot p_j=-2p_j\langle u_x\rangle(x_j),$$
where $\langle\cdot\rangle$ is the average of one-sided limits. DP additionally supports *shockpeakons* $u=\sum_j\big(p_j-s_j\operatorname{sgn}(x-x_j)\big)e^{-|x-x_j|}$ with $s_j\ge0$ (Lundmark 2007), which CH does not.

## 3. History & State of the Art (SOTA)

* **1999.** Degasperis and Procesi isolate the equation by asymptotic-integrability classification of $u_t+c_0u_x+\gamma u_{xxx}-\alpha^2u_{txx}=(c_1u^2+c_2u_x^2+c_3uu_{xx})_x$: exactly KdV, CH, and DP survive to third order.
* **2002.** Degasperis, Holm and Hone prove genuine integrability: Lax pair, bi-Hamiltonian structure, infinitely many conservation laws, peakons.
* **2003.** Yin establishes local well-posedness in $H^s$, $s>3/2$, on the line and the circle, plus a first global-existence criterion. Lundmark and Szmigielski solve the $N$-peakon inverse problem by a cubic string / Stieltjes continued-fraction method.
* **2005–2006.** Zhou, Liu and Yin obtain sufficient blow-up conditions and the precise wave-breaking scenario; Escher–Liu–Yin construct global weak solutions and describe the blow-up set. Coclite and Karlsen build the $L^1\cap BV$ entropy theory with uniqueness.
* **2007.** Lundmark shows DP shock formation is *not* the end of the solution: peakon–antipeakon collisions continue as shockpeakons, a mechanism absent from CH.
* **2009.** Lin and Liu prove orbital stability of DP peakons in $L^2$ using $E_2,E_3$ — a different functional pair from CH's $H^1$ argument. Constantin and Lannes place DP inside shallow-water asymptotics as a valid approximation of the free-surface Euler system.
* **2019.** Guo, Liu, Molinet and Yin prove norm inflation / ill-posedness for CH-type equations, including DP, in the critical space $H^{3/2}$, closing the scale from below.

The state of the art is therefore: sharp local theory ($s>3/2$ sharp), sharp blow-up mechanism, sufficient (not necessary) global-existence criteria, and a complete but non-optimal weak theory.

## 4. Partial Results / Verified Cases

* **Sign-definite momentum (global).** If $y_0\in L^1\cap L^\infty$ does not change sign — $y_0\ge0$ or $y_0\le0$ on $\mathbb{R}$ — then $u$ is global, and $u$ has the sign of $y_0$ with $|u_x|\le|u|$ (Yin 2003; Liu–Yin 2006). Same statement on the circle.
* **Ordered sign change (blow-up).** If there is $x_0$ with $y_0(x)\ge0$ for $x\le x_0$ and $y_0(x)\le0$ for $x\ge x_0$, and $y_0\not\equiv0$, then the solution breaks in finite time (Liu–Yin, *Comm. Math. Phys.* 267, 2006). This is the exact mirror image of the global case.
* **Slope/antisymmetry criteria.** Odd data $u_0$ with $u_0'(0)<0$ break; more generally quantitative criteria of the form $\inf_x u_{0,x}<-C\|u_0\|_{L^2}$ (Zhou 2005) give finite-time breaking, with explicit $C$ depending only on the Green function.
* **Peakon sector ($N$-peakons, all $N$).** Global existence and collision behaviour are completely known: solutions with all $p_j>0$ (or all $<0$) are global and asymptotically separate; sign-mixed configurations collide in finite time and continue as shockpeakons. Here the conjectured McKean-type criterion (P1) is a *theorem*, obtained from the explicit inverse-spectral formulas of Lundmark–Szmigielski.
* **Weak solutions.** Global entropy weak solutions exist for $u_0\in L^2$; uniqueness is proved in $L^\infty\cap BV$ with an Oleinik-type entropy condition $u_x\le \mathrm{const}$ (Coclite–Karlsen 2006).
* **Stability.** Peakons are orbitally stable in $L^2$ (Lin–Liu 2009); shockpeakons are stable within the entropy class.
* **Regularity/propagation.** Infinite propagation speed: compactly supported data instantly lose compact support, with $u\sim c_\pm(t)e^{\mp x}$ tails (Henry 2005).

## 5. Principal Obstacles

* **No $H^1$ conservation.** The CH proof of McKean's criterion leans on $\|u\|_{H^1}$ being conserved, which gives $\|u\|_{L^\infty}\le\|u\|_{H^1}/\sqrt2$ and a pointwise bound on the nonlocal term. DP conserves only the $L^2$-equivalent $E_2$, and $L^2(\mathbb{R})\not\hookrightarrow L^\infty$. The best $L^\infty$ estimates are of Grönwall type, growing in $t$, so no argument closes uniformly on long time intervals.
* **Cubic Jacobian weight.** The transport law $y(q)q_x^3=y_0$ amplifies momentum faster than CH's $q_x^2$. Standard Riccati arguments for $m(t)=\inf_xu_x$ produce $m'\le -\tfrac12 m^2 + (\text{nonlocal})$, but the nonlocal remainder is controlled only by $\|u\|_{L^\infty}^2$, which is exactly the uncontrolled quantity.
* **$E_3=\int u^3$ is not coercive.** The only cubic invariant has no sign, so it cannot be used to trap the solution in a bounded set; Lyapunov constructions from $(E_2,E_3)$ work near a single peakon but degenerate for general data.
* **Non-self-adjoint spectral problem.** The DP Lax operator is third order and non-self-adjoint; its spectrum need not be real for sign-changing $y_0$. Inverse-scattering arguments — the tool that makes McKean's CH theorem work — have no completeness theory here outside the discrete peakon sector.
* **Shock formation obstructs continuation uniqueness.** Because DP admits genuine shocks, the blow-up time is not the end of the story; distinguishing "wave breaking then continuation" from "no breaking" requires an entropy selection principle that does not exist in $H^s$.

## 6. The Gap

Proven: sign-definite $y_0$ $\Rightarrow$ global; monotonically ordered sign change $\Rightarrow$ breaking. Conjectured: breaking $\iff$ any positive mass of $y_0$ sits to the right of any negative mass.

The gap is the *unordered sign-changing* class: $y_0$ with two or more sign alternations, e.g. $y_0>0$ on $(-\infty,a)$, $y_0<0$ on $(a,b)$, $y_0>0$ on $(b,\infty)$. Neither theorem applies. The missing step is a monotone quantity that tracks the *relative ordering* of positive and negative momentum along the flow without an $L^\infty$ bound on $u$ — the DP analogue of McKean's "$y_0$ ordering is preserved" lemma. Equivalently: prove a time-uniform bound $\|u(t)\|_{L^\infty}\le C(\|u_0\|_{L^2},\|u_0\|_{L^\infty})$, which would immediately close the Riccati argument and reduce (P1) to a finite computation on the characteristics.

## 7. Current Research (as of June 2026)

* **Sharp criteria via characteristics.** Chinese schools (Sun Yat-sen, Zhejiang, Fudan; Yin, Zhou, and collaborators) continue to push localized blow-up criteria that require only a sign change on a bounded interval, trading generality for quantitative slope hypotheses. *(frontier — verify)*
* **Rough data and critical regularity.** After the $H^{3/2}$ ill-posedness result, work focuses on the critical Besov space $B^{3/2}_{2,1}$, where local well-posedness holds, and on norm-inflation rates just below it (Himonas, Holliman, Guo, Ye). *(frontier — verify)*
* **Shockpeakon dynamics and numerics.** Lundmark, Szmigielski and coauthors extend the cubic-string inverse problem to shockpeakons and to the interlacing/non-interlacing spectral picture for sign-changing measures.
* **Entropy $L^2$ uniqueness.** Extensions of Coclite–Karlsen toward uniqueness in $L^2$ without $BV$, using compensated compactness and Lions–Perthame–Tadmor kinetic formulations.
* **Higher-dimensional and generalized b-family.** Rotation-DP, two-component DP, and $b$-family analogues where the exponent in $q_x^b$ is treated as a parameter, to isolate which structural features control global existence.

## 8. Future Work

1. **Prove a uniform $L^\infty$ bound** for $H^s$ solutions, or construct data with $\|u(t)\|_{L^\infty}\to\infty$. This single question controls (P1) and (P3).
2. **Build a McKean-type ordering lemma** for the cubic weight $q_x^3$, testing it first on three-interval sign patterns and on $N$-peakon data with prescribed sign sequences.
3. **Spectral completeness for the third-order Lax operator** with signed measure potentials, to extend the peakon-sector proof to general $y_0\in\mathcal{M}$.
4. **Numerical scan of the sign-alternation boundary** with entropy-consistent schemes (Coclite–Karlsen–Risebro type), locating the empirical breaking/no-breaking interface in a two-parameter family of three-bump momenta.
5. **Uniqueness in $L^2$** for entropy solutions, closing (P2).

## 9. Key References

- **[Foundational]** A. Degasperis, M. Procesi. *Asymptotic Integrability.* In: Symmetry and Perturbation Theory (A. Degasperis, G. Gaeta, eds.), World Scientific, 1999, pp. 23–37.
- **[Foundational]** A. Degasperis, D. D. Holm, A. N. W. Hone. *A New Integrable Equation with Peakon Solutions.* Theoretical and Mathematical Physics, 133 (2002), 1463–1474.
- **[Foundational]** Z. Yin. *On the Cauchy Problem for an Integrable Equation with Peakon Solutions.* Illinois Journal of Mathematics, 47 (2003), 649–666.
- **[SOTA]** Y. Liu, Z. Yin. *Global Existence and Blow-up Phenomena for the Degasperis–Procesi Equation.* Communications in Mathematical Physics, 267 (2006), 801–820.
- **[SOTA]** J. Escher, Y. Liu, Z. Yin. *Global Weak Solutions and Blow-up Structure for the Degasperis–Procesi Equation.* Journal of Functional Analysis, 241 (2006), 457–485.
- **[SOTA]** G. M. Coclite, K. H. Karlsen. *On the Well-Posedness of the Degasperis–Procesi Equation.* Journal of Functional Analysis, 233 (2006), 60–91.
- **[SOTA]** H. Lundmark. *Formation and Dynamics of Shock Waves in the Degasperis–Procesi Equation.* Journal of Nonlinear Science, 17 (2007), 169–198.
- **[SOTA]** H. Lundmark, J. Szmigielski. *Multi-peakon Solutions of the Degasperis–Procesi Equation.* Inverse Problems, 19 (2003), 1241–1245.
- **[SOTA]** Z. Lin, Y. Liu. *Stability of Peakons for the Degasperis–Procesi Equation.* Communications on Pure and Applied Mathematics, 62 (2009), 125–146.
- **[SOTA]** Y. Guo, X. Liu, L. Molinet, Z. Yin. *Ill-posedness of the Camassa–Holm and Related Equations in the Critical Space.* Journal of Differential Equations, 266 (2019), 1698–1707.
- **[Related]** J. Escher, Z. Yin. *Well-posedness, Blow-up Phenomena, and Global Solutions for the b-equation.* Journal für die reine und angewandte Mathematik, 624 (2008), 51–80.
- **[Related]** Z. Jiang, L. Ni, Y. Zhou. *Wave Breaking of the Camassa–Holm Equation.* Journal of Nonlinear Science, 22 (2012), 235–245. (Proof of McKean's criterion — the CH template for P1.)
- **[Related]** D. Henry. *Infinite Propagation Speed for the Degasperis–Procesi Equation.* Journal of Mathematical Analysis and Applications, 311 (2005), 755–759.
- **[Survey]** A. Constantin, D. Lannes. *The Hydrodynamical Relevance of the Camassa–Holm and Degasperis–Procesi Equations.* Archive for Rational Mechanics and Analysis, 192 (2009), 165–186.
- **[Survey]** A. Constantin. *Nonlinear Water Waves with Applications to Wave-Current Interactions and Tsunamis.* CBMS-NSF Regional Conference Series in Applied Mathematics 81, SIAM, 2011.

## 10. Worked Example / Concrete Special Case

**Symmetric peakon–antipeakon: exact finite-time breaking with bounded amplitude.**

Take $u(t,x)=p\big(e^{-|x+q|}-e^{-|x-q|}\big)$ with $p(t)>0$, $q(t)>0$: a peakon at $-q$ and an antipeakon at $+q$, so $u$ is odd. The DP peakon ODEs $\dot x_j=u(x_j)$, $\dot p_j=-2p_j\langle u_x\rangle(x_j)$ specialize as follows. Put $s=e^{-2q}\in(0,1)$.

At $x=-q$: $u(-q)=p(1-s)$, and $\langle u_x\rangle(-q)=-ps$ (the peakon's own derivative averages to zero; only the antipeakon contributes). Hence
$$\dot q=-p(1-s),\qquad \dot p=2p^2s,\qquad \dot s=-2\dot q\,s=2p(1-s)s.$$
Divide:
$$\frac{dp}{ds}=\frac{2p^2s}{2p(1-s)s}=\frac{p}{1-s}\ \Longrightarrow\ p(t)=\frac{C}{1-s(t)},\quad C>0 \text{ constant}.$$
Substituting back gives the striking identity
$$\dot q=-p(1-s)=-C,$$
so $q(t)=q_0-Ct$ exactly: the peaks approach at constant speed and collide at
$$T=\frac{q_0}{C}.$$
Near collision $1-s=1-e^{-2q}\approx 2q=2C(T-t)$, so
$$p(t)\approx\frac{1}{2(T-t)}\longrightarrow\infty,$$
i.e. the momenta blow up like $(T-t)^{-1}$, and $u_x(t,0)=-2p s\to-\infty$: wave breaking.

**But the amplitude stays bounded.** For fixed $x>0$ and $t\uparrow T$,
$$u(t,x)=p\,e^{-x}\big(e^{-q}-e^{q}\big)=-2p\,e^{-x}\sinh q\approx-2\cdot\frac{1}{2(T-t)}\cdot C(T-t)\,e^{-x}=-Ce^{-x},$$
so $u(T,x)=-C\operatorname{sgn}(x)e^{-|x|}$, and $\|u(t)\|_{L^\infty}\le C$ for all $t<T$. The limit is a **shockpeakon** with zero peak height and jump $-2C$ at the origin — the solution continues past $T$ in the entropy class with $s_1(t)$ decaying, not as a classical solution.

**Why this is the model case for the gap.** Here $y_0=2C'(\delta_{-q_0}-\delta_{q_0})/(1-s_0)$ has its positive mass to the *left* of its negative mass — the *global* configuration in the ordered picture? No: reversing signs matters. Taking $p>0$ at $-q$ means positive momentum on the left and negative on the right, and this datum *breaks*; taking $p<0$ at $-q$ reverses the flow, $\dot q=+|C|>0$, the peaks separate and the solution is global for all $t>0$. The two-peakon family thus realizes both sides of the conjectured McKean criterion exactly, with $T=q_0/C$ computable in closed form. Adding a third peak with an unordered sign pattern $(+,-,+)$ leaves the closed-form structure intact but places the datum outside every proved theorem in Section 4 — this three-peakon family is the smallest concrete instance of the open case.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*