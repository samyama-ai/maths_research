---
id: 06-pdes/inviscid-damping
title: "Inviscid Damping"
topic: 06-pdes
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Inviscid Damping

> **Topic:** Partial Differential Equations · **ID:** `06-pdes/inviscid-damping` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

Consider the 2D incompressible Euler equations near a shear flow $(b(y),0)$ on $\mathbb{T}\times\mathbb{R}$ or the channel $\mathbb{T}\times[0,1]$. **Inviscid damping** is the claim that, although Euler has no dissipation and conserves all $L^p$ norms of vorticity, the *velocity* field of a perturbation converges as $t\to\infty$:
$$u(t)\longrightarrow (b_\infty(y),0),\qquad \|u^1(t)-b_\infty\|_{L^2}\lesssim \langle t\rangle^{-1},\qquad \|u^2(t)\|_{L^2}\lesssim \langle t\rangle^{-2}.$$
The energy is not lost; it is transferred to high vorticity frequencies by the shear (filamentation), so the velocity decays by the Riemann–Lebesgue lemma. This is the hydrodynamic analogue of Landau damping in the Vlasov–Poisson system.

The open problem, as posed after the linear theory of Case (1960), is **nonlinear** inviscid damping: for which spectrally stable shear flows $b$, and in which regularity class $X$, does there exist $\varepsilon_0>0$ such that every perturbation with $\|\omega_0\|_X<\varepsilon_0$ scatters to a nearby shear flow at the above rates? A complete resolution must specify (i) the class of admissible $b$, (ii) the sharp regularity threshold separating damping from instability, and (iii) the asymptotic profile $b_\infty$.

Status: **solved-recently** for Couette flow $b(y)=y$ and for stable strictly monotone flows in Gevrey-$1/s$ regularity with $s>1/2$; **open** in Sobolev regularity and for general non-monotone flows.

## 2. Mathematical Foundations

The 2D Euler equation in vorticity form, $\omega=\partial_x u^2-\partial_y u^1$:
$$\partial_t\omega+u\cdot\nabla\omega=0,\qquad u=\nabla^\perp\Delta^{-1}\omega=(-\partial_y,\partial_x)\Delta^{-1}\omega .$$
Write $u=(b(y)+u^1,u^2)$, $\omega=-b'(y)+\theta$. The linearization about the shear is
$$\partial_t\theta+b(y)\partial_x\theta-b''(y)\partial_x\Delta^{-1}\theta=0 .$$

**Rayleigh equation.** Modal solutions $\theta=e^{ik(x-ct)}\phi(y)$ with $\psi$ the stream function give
$$(b(y)-c)\left(\phi''-k^2\phi\right)-b''(y)\phi=0,\qquad \phi(\partial\Omega)=0 .$$
*Rayleigh's criterion* (1880): a necessary condition for an unstable eigenvalue ($\operatorname{Im}c>0$) is that $b''$ vanishes somewhere; *Fjørtoft's criterion* strengthens this. A flow with no unstable or embedded neutral modes is called **spectrally stable**; the linearized operator then has purely continuous spectrum $=b(\text{range})$, and damping is a statement about the absence of point spectrum plus regularity of the spectral density.

**The Orr mechanism.** For Couette flow $b(y)=y$ set $z=x-ty$, $f(t,z,y)=\theta(t,z+ty,y)$. Then $\partial_tf=0$ at the linear level and
$$\widehat{\psi}(t,k,\eta)=-\frac{\widehat{f}(k,\eta)}{k^2+(\eta-kt)^2},\qquad \widehat{u^2}=ik\widehat\psi,\quad \widehat{u^1}=-i(\eta-kt)\widehat\psi .$$
The multiplier decays like $t^{-2}$ for $k\neq0$, giving the rates in §1. The transient growth at the **critical time** $t\approx \eta/k$ (Orr, 1907) — where the multiplier is $O(1)$ instead of $O(t^{-2})$ — is the source of all difficulty.

**Nonlinear echoes.** In the nonlinear problem, the quadratic term couples mode $(k,\eta)$ near its critical time to modes $(k\pm1,\cdot)$, producing a cascade of **echoes** with cumulative amplification $\sim e^{C\sqrt{|\eta|}}$ over the whole chain. This is exactly the loss compensated by Gevrey-$2$ regularity.

**Gevrey classes.** For $s\in(0,1]$, $\lambda>0$,
$$\mathcal{G}^{\lambda,s}=\Big\{f:\ \|f\|_{\mathcal G^{\lambda,s}}^2=\sum_k\int e^{2\lambda(|k|+|\eta|)^{s}}|\widehat f(k,\eta)|^2\,d\eta<\infty\Big\},$$
i.e. Gevrey class $1/s$; $s=1$ is analytic, $s\to0$ approaches Sobolev. The echo amplification $e^{C\sqrt{|\eta|}}$ is absorbable precisely when $s>1/2$ (Gevrey-$2$).

**Vorticity depletion.** For non-monotone $b$ with critical points $y_c$ ($b'(y_c)=0$), the limiting vorticity of the linearized flow vanishes at $y_c$ — the "depletion" phenomenon of Bouchet–Morita (2010) — which restores $t^{-1},t^{-2}$ decay despite the degeneracy.

## 3. History & State of the Art (SOTA)

- **1880** Rayleigh: inflection-point criterion.
- **1907** Orr: explicit non-modal transient growth and decay for Couette; the "Orr mechanism".
- **1960** Case: linear damping for Couette by Laplace transform, the first rigorous statement.
- **1960s–90s** Physics literature (Briggs–Daugherty–Levy 1970; Lundgren) on 2D vortex relaxation.
- **2010** Bouchet–Morita: vorticity depletion for general stable shear flows.
- **2011** Lin–Zeng (ARMA): nontrivial steady states (Kelvin–Stuart cat's-eyes) arbitrarily close to Couette in $H^s$ for $s<3/2$ — nonlinear damping is *false* in low Sobolev spaces.
- **2015** Bedrossian–Masmoudi (*Publ. IHES*): **nonlinear inviscid damping for Couette flow in Gevrey-$1/s$, $s>1/2$**, on $\mathbb T\times\mathbb R$. Landmark result.
- **2017–20** Wei–Zhang–Zhao; Zillinger; Jia: linear damping in Sobolev/Gevrey for monotone and non-monotone flows, with depletion.
- **2020** Deng–Masmoudi (*CPAM*): **sharpness** — instability of Couette in Gevrey-$1/s$ for $s<1/2$.
- **2020–23** Ionescu–Jia (*Acta Math.*) and Masmoudi–Zhao: **nonlinear inviscid damping near stable monotone shear flows in a finite channel**, Gevrey-$2$. These essentially close the monotone case.
- **2022** Ionescu–Jia; Bedrossian–Coti Zelati–Vicol: axisymmetrization and damping near point vortices.

## 4. Partial Results / Verified Cases

| Setting | Regularity | Result |
|---|---|---|
| Couette $b=y$, $\mathbb T\times\mathbb R$ | Gevrey-$1/s$, $s>1/2$ | Nonlinear damping, $t^{-1}/t^{-2}$ (Bedrossian–Masmoudi 2015) |
| Couette, finite channel $\mathbb T\times[0,1]$ | Gevrey-$2$ | Nonlinear damping (Ionescu–Jia 2020) |
| Couette | Gevrey-$1/s$, $s<1/2$ | **Instability**: damping fails (Deng–Masmoudi 2020) |
| Couette | $H^s$, $s<3/2$ | Nontrivial nearby steady states; damping fails (Lin–Zeng 2011) |
| Strictly monotone, spectrally stable $b$, channel | Gevrey-$2$ | Nonlinear damping (Ionescu–Jia 2023; Masmoudi–Zhao) |
| Monotone $b$ with $b''\ne0$ allowed | $H^{-1}\times H^1$-type Sobolev | **Linear** damping (Wei–Zhang–Zhao, *CPAM* 2018) |
| Non-monotone (e.g. Kolmogorov $b=\sin y$, Poiseuille $b=y^2$) | Sobolev | **Linear** damping + vorticity depletion at critical points (Wei–Zhang–Zhao, *Ann. PDE* 2019) |
| Point vortex $\omega=\delta$-like radial profiles | Gevrey | Axisymmetrization + damping (Bedrossian–Coti Zelati–Vicol 2019; Ionescu–Jia 2022) |
| 3D Couette, Navier–Stokes | $H^\sigma$, $\sigma>9/2$ | Stability threshold $\varepsilon\lesssim \nu^{1/2}$-type (Bedrossian–Germain–Masmoudi, *Ann. Math.* 2017) |

Damping rates are sharp: $u^2$ cannot decay faster than $t^{-2}$ for generic data, and $u^1-b_\infty$ decays exactly like $t^{-1}$.

## 5. Principal Obstacles

- **Echo cascades.** The nonlinearity resonates at the sequence of critical times $t_n\approx\eta/n$. Each echo costs a factor $\sim e^{c\sqrt{\eta}/N}$ over $N$ steps; summing gives $e^{c\sqrt\eta}$. Sobolev norms cannot absorb a stretched-exponential loss, so **no Sobolev-based energy method can close** — and by Deng–Masmoudi the loss is real, not an artifact.
- **No dissipation.** Unlike Navier–Stokes there is no $\nu|\nabla|^2$ term to beat the growth; all control must come from the time-dependent Fourier multiplier $(k^2+(\eta-kt)^2)^{-1}$, which is $O(1)$ during the critical interval.
- **Nonlinear change of coordinates.** For general $b$ one must construct the asymptotic profile $b_\infty$ and the associated straightening map simultaneously with the solution; the map is only as regular as the solution, creating a quasilinear loss-of-derivative loop. Ionescu–Jia and Masmoudi–Zhao resolve this with elaborate paradifferential/wave-operator constructions tied to $b$.
- **Critical points and endpoints.** When $b'(y_c)=0$ the Orr multiplier degenerates; the Rayleigh equation has a genuine singularity and the associated spectral projection loses regularity. Boundary points of a channel produce $y$-boundary terms with only algebraic decay ($t^{-1}$ in $u^1$ but weaker vorticity control).
- **Embedded neutral modes.** Spectral stability is a hypothesis, not a checkable structural property, for most non-monotone profiles.

## 6. The Gap

Three precise gaps remain between §4 and §1.

1. **The Sobolev window $3/2\le s$.** Lin–Zeng rule out damping for $H^s$, $s<3/2$; Deng–Masmoudi rule out Gevrey-$1/s$ with $s<1/2$. Nothing is known for $H^s$ with $s>3/2$, nor for Gevrey exactly at $s=1/2$. Whether the true threshold is Gevrey-$2$ or some intermediate class (e.g. $e^{\lambda|\eta|^{1/2}/\log|\eta|}$) is open. Deng–Masmoudi's instability is a *norm-growth* statement, not a construction of a non-damping solution in $H^{3/2+}$.
2. **Non-monotone profiles nonlinearly.** Linear damping with depletion is proven for Kolmogorov and Poiseuille flows; **no nonlinear result exists** in any regularity for a flow with an interior critical point. The obstruction is that depletion is a statement about the limit, not a uniform-in-time coercive quantity.
3. **Large data / vortex relaxation.** Damping near a *general* steady state, or the conjectured relaxation of generic 2D Euler data to a shear/vortex (the "2D turbulence relaxation" picture), is entirely open; even the correct asymptotic class is unclear given Šverák–Choi's results on the rigidity and non-uniqueness of $\omega$-limit sets.

## 7. Current Research (as of June 2026)

- **Ionescu–Jia (Princeton/UMN)** and **Masmoudi–Zhao (NYU–Abu Dhabi / Peking)** continue the monotone-flow programme, extending to boundary-layer profiles and to Euler–Boussinesq stratified shear. *(frontier — verify)*
- **Wei–Zhang and collaborators (Peking)** push toward nonlinear damping for non-monotone flows via depletion-adapted energies, and study the Kolmogorov flow's transition threshold in Navier–Stokes.
- **Bedrossian, Coti Zelati, Vicol** (UCLA / SISSA / NYU) study enhanced dissipation, vortex axisymmetrization, and the interpolation between $\nu>0$ and $\nu=0$ regimes.
- **Deng, Zillinger, Jia**: sharper echo analysis aiming to pin the exact critical regularity; toy "echo chain" models (Deng–Masmoudi; Bedrossian's Vlasov analogue) are the main testing ground. *(frontier — verify)*
- Interaction with **Landau damping** literature (Mouhot–Villani; Bedrossian–Masmoudi–Mouhot) remains the main source of technique transfer.

## 8. Future Work

- Determine the sharp regularity threshold for Couette: is it exactly Gevrey-$2$, and is there a solution in $H^\infty\setminus\mathcal G^{\lambda,1/2}$ that fails to damp?
- Prove nonlinear inviscid damping for one non-monotone spectrally stable profile — Kolmogorov $\sin y$ is the canonical target.
- Handle channel boundaries without loss: obtain the full $t^{-2}$ decay for $u^2$ up to $\partial\Omega$.
- Quantify the vanishing-viscosity limit: make the Gevrey-$2$ inviscid statement and the Sobolev Navier–Stokes threshold $\varepsilon\lesssim\nu^{\alpha}$ two ends of one uniform theorem.
- Extend to compressible/stratified/MHD shear, where damping competes with wave radiation.

## 9. Key References

- **[Foundational]** Lord Rayleigh. *On the stability, or instability, of certain fluid motions.* Proc. London Math. Soc. 11, 1880.
- **[Foundational]** W. M'F. Orr. *The stability or instability of the steady motions of a perfect liquid and of a viscous liquid.* Proc. Royal Irish Academy 27, 1907.
- **[Foundational]** K. M. Case. *Stability of inviscid plane Couette flow.* Physics of Fluids 3, 1960.
- **[Foundational]** F. Bouchet, H. Morita. *Large time behavior and asymptotic stability of the 2D Euler and linearized Euler equations.* Physica D 239, 2010.
- **[Foundational]** Z. Lin, C. Zeng. *Inviscid dynamical structures near Couette flow.* Archive for Rational Mechanics and Analysis 200, 2011.
- **[SOTA]** J. Bedrossian, N. Masmoudi. *Inviscid damping and the asymptotic stability of planar shear flows in the 2D Euler equations.* Publications mathématiques de l'IHÉS 122, 2015.
- **[SOTA]** D. Wei, Z. Zhang, W. Zhao. *Linear inviscid damping for a class of monotone shear flow in Sobolev spaces.* Communications on Pure and Applied Mathematics 71, 2018.
- **[SOTA]** D. Wei, Z. Zhang, W. Zhao. *Linear inviscid damping and vorticity depletion for shear flows.* Annals of PDE 5, 2019.
- **[SOTA]** Y. Deng, N. Masmoudi. *Long-time instability of the Couette flow in low Gevrey spaces.* Communications on Pure and Applied Mathematics 76, 2023 (arXiv:1803.01246).
- **[SOTA]** A. D. Ionescu, H. Jia. *Inviscid damping near the Couette flow in a channel.* Communications in Mathematical Physics 374, 2020.
- **[SOTA]** A. D. Ionescu, H. Jia. *Nonlinear inviscid damping near monotonic shear flows.* Acta Mathematica 230, 2023.
- **[SOTA]** N. Masmoudi, W. Zhao. *Nonlinear inviscid damping for a class of monotone shear flows in a finite channel.* arXiv:2001.08564, 2020.
- **[SOTA]** J. Bedrossian, M. Coti Zelati, V. Vicol. *Vortex axisymmetrization, inviscid damping, and vorticity depletion in the linearized 2D Euler equations.* Annals of PDE 5, 2019.
- **[SOTA]** J. Bedrossian, P. Germain, N. Masmoudi. *On the stability threshold for the 3D Couette flow in Sobolev regularity.* Annals of Mathematics 185, 2017.
- **[Survey]** J. Bedrossian, P. Germain, N. Masmoudi. *Stability of the Couette flow at high Reynolds numbers in two dimensions and three dimensions.* Bulletin of the AMS 56, 2019.
- **[Survey]** C. Mouhot, C. Villani. *On Landau damping.* Acta Mathematica 207, 2011. (Methodological ancestor.)

## 10. Worked Example / Concrete Special Case

**Linear damping for Couette on $\mathbb T\times\mathbb R$, explicit rates.**

Take $b(y)=y$, perturbation vorticity $\theta$, linearized equation $\partial_t\theta+y\partial_x\theta=0$ (here $b''=0$, so no stretching term). Pass to moving coordinates $z=x-ty$, $f(t,z,y)=\theta(t,z+ty,y)$; then $\partial_tf=0$, so $\widehat f(t,k,\eta)=\widehat{\theta_0}(k,\eta)$ for all $t$. In the original variables $\widehat\theta(t,k,\eta)=\widehat{\theta_0}(k,\eta+kt)$ — pure frequency transport, $\|\theta(t)\|_{L^2}$ constant. **No vorticity decays.**

Stream function: $\widehat\psi(t,k,\eta)=-\widehat f(k,\eta)\big/\big(k^2+(\eta-kt)^2\big)$, hence
$$\widehat{u^2}(t,k,\eta)=\frac{-ik\,\widehat{\theta_0}(k,\eta)}{k^2+(\eta-kt)^2}.$$

Take a single mode $k=1$ and Gaussian data $\widehat{\theta_0}(1,\eta)=e^{-\eta^2/2}$. Then
$$\|u^2(t)\|_{L^2_{x,y}}^2 = c\int_{\mathbb R}\frac{e^{-\eta^2}}{\big(1+(\eta-t)^2\big)^2}\,d\eta .$$
For large $t$, the Gaussian concentrates near $\eta=O(1)$ while the denominator is $\approx t^4$ there, so the integral is $\sim C t^{-4}$ and $\|u^2(t)\|_{L^2}\sim C t^{-2}$. Similarly $\widehat{u^1}=-i(\eta-t)\widehat\psi$ gives $\|u^1(t)\|_{L^2}\sim Ct^{-1}$. This is the sharp rate.

**Where the nonlinearity bites.** Take instead data concentrated at high frequency, $\widehat{\theta_0}(1,\eta)$ peaked at $\eta=\eta_0\gg1$. Then $\|u^2\|$ is *not* small until the **critical time** $t=\eta_0$, at which $k^2+(\eta_0-kt)^2=1$: the velocity transiently returns to full size, of order $|\widehat{\theta_0}|$, before resuming decay. In the nonlinear problem this $O(1)$ velocity burst at $t=\eta_0$ drives the mode $k=2$ at frequency $\approx2\eta_0$, which has its own critical time $t=\eta_0$… and iterating over $k=1,\dots,N$ with $N\approx\sqrt{\eta_0}$ optimally chosen yields a total amplification of order
$$\prod_{n=1}^{N}\big(1+c\,\varepsilon\,\eta_0/n^2\big)\ \approx\ \exp\!\big(c\sqrt{\eta_0}\big)\quad\text{for }\varepsilon\sim\eta_0^{-1/2}.$$
A Gevrey-$1/s$ norm supplies a factor $e^{-\lambda\eta_0^{s}}$, which beats $e^{c\sqrt{\eta_0}}$ exactly when $s>1/2$. That single inequality is the whole reason the theorem is stated in Gevrey-$2$, and Deng–Masmoudi show the mechanism genuinely fails below it.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*