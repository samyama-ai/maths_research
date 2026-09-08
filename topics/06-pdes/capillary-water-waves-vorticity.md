---
id: 06-pdes/capillary-water-waves-vorticity
title: "Global Existence for the Two-Dimensional Water Wave Problem with Surface Tension and Vorticity"
topic: 06-pdes
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Global Existence for the Two-Dimensional Water Wave Problem with Surface Tension and Vorticity

> **Topic:** Partial Differential Equations · **ID:** `06-pdes/capillary-water-waves-vorticity` · **Status:** open

## 1. Problem Statement / Conjecture

Consider a two-dimensional incompressible, inviscid fluid of infinite depth with a free upper boundary, acted on by gravity $g \ge 0$ and surface tension $\sigma > 0$, and with **non-zero vorticity**. The unknowns are the interface $\eta(t,x)$ and the velocity field $u(t,\cdot)$ in the fluid domain.

**Conjecture (global regularity, small rotational data).** There exist $N$ large and $\varepsilon_0 > 0$ such that for every initial state with
$$\|\eta_0\|_{H^{N+1/2}} + \|u_0\|_{H^N} + \|x\partial_x(\eta_0,u_0)\|_{L^2} \le \varepsilon \le \varepsilon_0,$$
satisfying the Rayleigh–Taylor sign condition and a non-self-intersection condition, and with vorticity $\mathrm{curl}\,u_0 = \gamma \not\equiv 0$ (small and smooth, or constant $\gamma \ne 0$), the solution exists for all $t \in \mathbb{R}$, remains smooth, and decays at the linear rate $\|\partial_x \eta(t)\|_{L^\infty} \lesssim \varepsilon t^{-1/2}$ with (possibly modified) scattering as $t \to \pm\infty$.

A complete resolution requires either a proof of the above, or a construction of small rotational data whose solution loses regularity, self-intersects, or violates the Rayleigh–Taylor condition in finite time. The **irrotational** case with pure surface tension is a theorem (Ionescu–Pusateri 2018); the conjecture asserts that vorticity does not destroy it. Two sub-cases are separately open: (a) $g = 0$, $\sigma > 0$, constant vorticity; (b) $g > 0$, $\sigma > 0$, any vorticity — open even for $\gamma = 0$.

## 2. Mathematical Foundations

Let $\Omega(t) = \{(x,y) : y < \eta(t,x)\}$ with free surface $\Sigma(t) = \{(x,\eta(t,x))\}$. The incompressible Euler equations are
$$\partial_t u + (u\cdot\nabla)u = -\nabla p - g e_2 \quad \text{in } \Omega(t), \qquad \nabla\cdot u = 0,$$
with the kinematic condition $\partial_t + u\cdot\nabla$ tangent to $\bigcup_t \Sigma(t)$, i.e.
$$\partial_t \eta = u_2 - u_1 \partial_x \eta \quad \text{on } \Sigma(t),$$
and the **Young–Laplace** dynamic boundary condition
$$p\big|_{\Sigma(t)} = -\sigma \mathcal{H}(\eta), \qquad \mathcal{H}(\eta) = \partial_x\!\left(\frac{\partial_x \eta}{\sqrt{1+(\partial_x\eta)^2}}\right).$$

**Irrotational reduction (Zakharov–Craig–Sulem).** If $\mathrm{curl}\,u \equiv 0$, set $u = \nabla\phi$, $\psi = \phi|_{\Sigma}$, and let $G(\eta)$ be the Dirichlet–Neumann operator, $G(\eta)\psi = \sqrt{1+(\partial_x\eta)^2}\,\partial_n\phi|_\Sigma$. The system is Hamiltonian, $\partial_t\eta = \delta_\psi H$, $\partial_t\psi = -\delta_\eta H$, with
$$H(\eta,\psi) = \tfrac12\int_{\mathbb R} \psi\, G(\eta)\psi\,dx + \tfrac g2\int_{\mathbb R}\eta^2\,dx + \sigma\!\int_{\mathbb R}\!\left(\sqrt{1+(\partial_x\eta)^2}-1\right)dx .$$

**Vorticity.** Vorticity $\omega = \mathrm{curl}\,u$ is transported: $\partial_t \omega + u\cdot\nabla\omega = 0$ in 2D. It obstructs the reduction: $u$ is no longer a gradient, and the state must carry the interior field. Two tractable regimes:

- **Constant vorticity** $\omega \equiv \gamma$. Then $u = \nabla\phi + \gamma(-y,0)$ (Wahlén 2007, Constantin–Ivanov–Prodanov 2008), and the system remains a two-unknown system with a *modified*, non-canonical Poisson structure
 $$J_\gamma = \begin{pmatrix} 0 & 1 \\ -1 & -\gamma\,\partial_x^{-1}\end{pmatrix}.$$
- **General vorticity**: the state is $(\eta, \psi, \omega)$ with a div-curl elliptic problem coupling them.

**Linearization and dispersion.** Linearizing at $(\eta,\psi)=(0,0)$ in infinite depth with constant vorticity gives the two branches
$$\omega_\pm(\xi) = -\frac{\gamma}{2}\,\mathrm{sgn}\,\xi \;\pm\; \sqrt{\,g|\xi| + \sigma|\xi|^3 + \frac{\gamma^2}{4}\,}.$$
For $\gamma = 0$ this is the classical $\omega(\xi) = \sqrt{g|\xi|+\sigma|\xi|^3}$. The symbol is **even** when $\gamma=0$ and **not even** when $\gamma \ne 0$; the $\mathrm{sgn}\,\xi$ term is discontinuous at $\xi=0$, and $\omega_\pm(0^\pm)$ has a spectral gap of size $|\gamma|$.

**Rayleigh–Taylor condition.** With $a = -\partial_n p|_{\Sigma}$, local well-posedness for $\sigma > 0$ does *not* require $a>0$, but the coercivity of the natural energy and the sign of the Taylor coefficient control the transition to Kelvin–Helmholtz-type instability in the two-fluid problem.

## 3. History & State of the Art (SOTA)

- **1968.** Zakharov identifies the Hamiltonian structure of the irrotational water wave problem.
- **1993.** Craig–Sulem give the Dirichlet–Neumann formulation and its analytic expansion.
- **1997–99.** Wu proves local well-posedness for 2D and 3D irrotational gravity waves ($\sigma=0$) under the Taylor sign condition.
- **1998–2011.** Local theory *with* surface tension and vorticity: Beyer–Günther (1998), Ogawa–Tani (2002), Coutand–Shkoller (JAMS 2007), Shatah–Zeng (CPAM 2008; ARMA 2011), Alazard–Burq–Zuily (Duke 2011, low regularity, $\sigma>0$). These give existence on a time interval $T(\varepsilon)$ with no smallness-dependent lower bound better than $T \gtrsim \varepsilon^{-1}$.
- **2009–2015.** Global theory for **small irrotational** data: Wu (3D gravity, almost global then global), Germain–Masmoudi–Shatah (3D gravity; 3D capillary, CPAM 2015), Ionescu–Pusateri and Alazard–Delort independently (2D gravity, 2015), Deng–Ionescu–Pausader–Pusateri (3D gravity-capillary, Acta Math. 2017).
- **2017–2018.** 2D capillary: Ifrim–Tataru prove lifespan $T \gtrsim \varepsilon^{-2}$ (cubic lifespan, ARMA 2017); Ionescu–Pusateri prove **global regularity and modified scattering** for 2D pure capillary waves (Mem. AMS 2018). This is the sharp irrotational benchmark the conjecture aims to extend.
- **2019–present.** Vorticity enters the long-time picture: Ifrim–Tataru prove $T \gtrsim \varepsilon^{-2}$ for 2D **gravity** waves with constant vorticity (Anal. PDE 2019); Berti–Franzoi–Maspero construct traveling quasi-periodic gravity-capillary waves with constant vorticity (ARMA 2021); Su studies 2D waves with interior point vortices (CMP 2020).

**Status summary.** Global existence is known for $\sigma>0$, $g=0$, $\gamma=0$ in 2D. It is open for every case with $\gamma \ne 0$, and open in 2D for $g>0,\sigma>0$ even irrotationally.

## 4. Partial Results / Verified Cases

| Regime | Best result | Source |
|---|---|---|
| 2D, $\sigma>0$, $g=0$, irrotational | Global, modified scattering | Ionescu–Pusateri, Mem. AMS 2018 |
| 2D, $\sigma>0$, $g=0$, irrotational | $T \gtrsim \varepsilon^{-2}$, holomorphic coordinates | Ifrim–Tataru, ARMA 2017 |
| 3D, $\sigma>0$, $g=0$, irrotational | Global + scattering | Germain–Masmoudi–Shatah, CPAM 2015 |
| 3D, $g>0,\sigma>0$, irrotational | Global + scattering | Deng–Ionescu–Pausader–Pusateri, Acta 2017 |
| 2D, $g>0$, $\sigma=0$, $\omega\equiv\gamma$ | $T\gtrsim \varepsilon^{-2}$ | Ifrim–Tataru, Anal. PDE 2019 |
| 2D/3D, $\sigma>0$, general $\omega$ | Local well-posedness only, $T\gtrsim\varepsilon^{-1}$ | Coutand–Shkoller 2007; Shatah–Zeng 2011 |
| Periodic 2D, $g>0,\sigma>0$, $\omega\equiv\gamma$ | Quasi-periodic traveling waves (KAM), positive-measure parameter set | Berti–Franzoi–Maspero, ARMA 2021 |
| Periodic 2D gravity, irrotational | $T\gtrsim\varepsilon^{-3}$ via Birkhoff normal form | Berti–Feola–Pusateri, CPAM 2023 |

Also verified: **finite-time splash singularities exist with surface tension** for large (self-approaching) data (Castro–Córdoba–Fefferman–Gancedo–Gómez-Serrano, J. Math. Phys. 2012), so any global statement must be a small-data statement.

## 5. Principal Obstacles

- **Loss of the Zakharov reduction.** With general $\omega$, the state space is $(\eta,\psi,\omega)$ and the div-curl problem couples interior transport to the boundary evolution. The dispersive machinery (space-time resonances, testing by wave packets) is built for a two-unknown boundary system; there is no known dispersive framework for the coupled boundary-plus-transport system.
- **No decay for the vorticity.** The transported $\omega$ does not disperse. Any bilinear estimate mixing a dispersive factor ($t^{-1/2}$) with a non-decaying transported factor loses all time-integrability, so quadratic terms cannot be normal-formed away.
- **Broken parity of the symbol.** For $\gamma\ne0$, $\omega_\pm(\xi)$ contains $-\tfrac{\gamma}{2}\mathrm{sgn}\,\xi$, which is discontinuous at $\xi=0$ and destroys the evenness used in every 2D global proof. Counter-propagating quadratic interactions that are non-resonant when $\gamma=0$ become resonant for suitable $\gamma$.
- **Low-frequency spectral gap.** $\omega_\pm(0^\pm)\ne 0$ means the linear group is not homogeneous; the scaling and Klainerman-type vector field $S = t\partial_t + \tfrac{2}{3}x\partial_x$ adapted to $|\xi|^{3/2}$ is no longer a symmetry, removing the main commuting vector field.
- **Quasilinearity plus slow decay.** In 1D interface dimension the sharp decay is only $t^{-1/2}$; quadratic normal forms lose derivatives and must be paralinearized. Combining paradifferential energy estimates with vorticity transport at high regularity has not been done.
- **Wilton-ripple resonances.** When $g>0$ and $\sigma>0$ simultaneously, genuine three-wave resonances exist (Section 10); no normal form removes them.

## 6. The Gap

Proven: global regularity for 2D **pure capillary, irrotational, infinite depth, small localized** data. Conjectured: the same with $\gamma\ne0$ and/or $g>0$.

The precise missing step is a **long-time bilinear/trilinear estimate for the rotational system**. Concretely, one needs an energy-plus-weighted-norm bootstrap
$$\sup_{t}\Big(\|(\eta,\psi)(t)\|_{H^N} + \langle t\rangle^{-\delta}\|\mathcal{Z}(\eta,\psi)(t)\|_{L^2}\Big) \lesssim \varepsilon,$$
where $\mathcal{Z}$ is a weighted vector field adapted to the *non-even, gapped* symbol $\omega_\pm$, together with a proof that all quadratic interactions involving the transported vorticity are either non-resonant or contribute only to a phase correction. No candidate $\mathcal{Z}$ compatible with $\mathrm{sgn}\,\xi$ is known; and even for $\gamma$ constant, the passage from $T\gtrsim\varepsilon^{-2}$ to $T=\infty$ requires controlling the cubic resonant set of $\omega_\pm$, which has not been computed.

## 7. Current Research (as of June 2026)

- **Holomorphic-coordinate school (Ifrim, Tataru, Hunter, Harrop-Griffiths; Berkeley/UCLA).** Conformal-variable formulation of 2D water waves; cubic lifespan results for constant vorticity, ongoing attempts to reach $\varepsilon^{-3}$ and beyond with surface tension. *(frontier — verify)*
- **Space-time resonance school (Ionescu, Pusateri, Pausader, Deng; Princeton/Toronto/Brown).** Extension of the Mem. AMS 2018 modified-scattering argument to $g>0$ in 2D, where Wilton resonances are the obstruction.
- **Paradifferential Birkhoff normal form (Berti, Feola, Maspero, Murgante, Franzoi; SISSA).** Hamiltonian paradifferential normal forms giving $\varepsilon^{-3}$-type lifespans on the torus; extension to constant vorticity is announced in preprint form. *(frontier — verify)*
- **KAM / quasi-periodic solutions with vorticity.** Berti–Franzoi–Maspero and successors construct time-quasi-periodic traveling gravity-capillary waves with constant vorticity, giving *global* but non-generic solutions.
- **Vortex-patch and point-vortex interiors (Su, Zhang).** Global-in-time or long-time behavior when the vorticity is concentrated, isolating the wave-vortex interaction. *(frontier — verify)*

## 8. Future Work

1. Compute the full quadratic and cubic resonance varieties of $\omega_\pm(\xi) = -\tfrac\gamma2\mathrm{sgn}\,\xi \pm \sqrt{g|\xi|+\sigma|\xi|^3+\gamma^2/4}$ and classify the degenerate values of $(g,\sigma,\gamma)$.
2. Build a weighted-norm/vector-field calculus adapted to a non-even, non-homogeneous symbol with a low-frequency gap.
3. Prove $\varepsilon^{-3}$ or almost-global lifespan for $g=0,\sigma>0,\gamma\ne0$ as a stepping stone; this is the case with the fewest resonances.
4. Treat small non-constant vorticity perturbatively: split $u$ into a dispersive irrotational part and a transported rotational remainder and close estimates in different norms for each.
5. Settle 2D gravity-capillary irrotational global existence — resolving Wilton resonances there is a prerequisite for any rotational extension.
6. Search numerically for small rotational data exhibiting growth of $\|\partial_x\eta\|_{L^\infty}$, which would falsify the conjecture.

## 9. Key References

- **[Foundational]** V. E. Zakharov. *Stability of periodic waves of finite amplitude on the surface of a deep fluid.* Journal of Applied Mechanics and Technical Physics, 9 (1968), 190–194.
- **[Foundational]** D. Coutand, S. Shkoller. *Well-posedness of the free-surface incompressible Euler equations with or without surface tension.* Journal of the AMS, 20 (2007), 829–930.
- **[Foundational]** J. Shatah, C. Zeng. *Geometry and a priori estimates for free boundary problems of the Euler equation.* Communications on Pure and Applied Mathematics, 61 (2008), 698–744.
- **[Foundational]** J. Shatah, C. Zeng. *Local well-posedness for fluid interface problems.* Archive for Rational Mechanics and Analysis, 199 (2011), 653–705.
- **[Foundational]** T. Alazard, N. Burq, C. Zuily. *On the water-wave equations with surface tension.* Duke Mathematical Journal, 158 (2011), 413–499.
- **[SOTA]** A. D. Ionescu, F. Pusateri. *Global regularity for 2D water waves with surface tension.* Memoirs of the American Mathematical Society, 256 (2018), no. 1227.
- **[SOTA]** M. Ifrim, D. Tataru. *The lifespan of small data solutions in two dimensional capillary water waves.* Archive for Rational Mechanics and Analysis, 225 (2017), 1279–1346.
- **[SOTA]** M. Ifrim, D. Tataru. *Two-dimensional gravity water waves with constant vorticity I: cubic lifespan.* Analysis & PDE, 12 (2019), 903–967.
- **[SOTA]** P. Germain, N. Masmoudi, J. Shatah. *Global existence for capillary water waves.* Communications on Pure and Applied Mathematics, 68 (2015), 625–687.
- **[SOTA]** Y. Deng, A. D. Ionescu, B. Pausader, F. Pusateri. *Global solutions of the gravity-capillary water-wave system in three dimensions.* Acta Mathematica, 219 (2017), 213–402.
- **[SOTA]** M. Berti, L. Franzoi, A. Maspero. *Traveling quasi-periodic water waves with constant vorticity.* Archive for Rational Mechanics and Analysis, 240 (2021), 99–202.
- **[SOTA]** M. Berti, R. Feola, F. Pusateri. *Birkhoff normal form and long time existence for periodic gravity water waves.* Communications on Pure and Applied Mathematics, 76 (2023), 1416–1494.
- **[Structure]** E. Wahlén. *A Hamiltonian formulation of water waves with constant vorticity.* Letters in Mathematical Physics, 79 (2007), 303–315.
- **[Structure]** A. Constantin, R. I. Ivanov, E. M. Prodanov. *Nearly-Hamiltonian structure for water waves with constant vorticity.* Journal of Mathematical Fluid Mechanics, 10 (2008), 224–237.
- **[Blow-up]** A. Castro, D. Córdoba, C. Fefferman, F. Gancedo, J. Gómez-Serrano. *Finite time singularities for water waves with surface tension.* Journal of Mathematical Physics, 53 (2012), 115622.
- **[Survey]** D. Lannes. *The Water Waves Problem: Mathematical Analysis and Asymptotics.* AMS Mathematical Surveys and Monographs 188, 2013.
- **[Survey]** Q. Su. *Long time behavior of 2D water waves with point vortices.* Communications in Mathematical Physics, 380 (2020), 1173–1266.

## 10. Worked Example / Concrete Special Case

**Why $\sigma>0$ and $g>0$ together create a resonance (Wilton ripples), and why $\gamma\ne0$ makes it worse.**

*Step 1 — no quadratic resonance for pure capillary.* With $g=\gamma=0$, $\omega(\xi)=\sqrt{\sigma}|\xi|^{3/2}$. A three-wave resonance requires $\xi=\eta+\zeta$ with $|\xi|^{3/2}=|\eta|^{3/2}+|\zeta|^{3/2}$. If $\eta,\zeta$ have the same sign, $|\xi|=|\eta|+|\zeta|$ and strict superadditivity of $s\mapsto s^{3/2}$ gives $(|\eta|+|\zeta|)^{3/2} > |\eta|^{3/2}+|\zeta|^{3/2}$. If they have opposite signs, $|\xi| < \max(|\eta|,|\zeta|)$, so the left side is smaller. **No solutions.** This absence is exactly what lets Ionescu–Pusateri normal-form the quadratic terms and reach $t=\infty$.

*Step 2 — resonance reappears when $g>0$.* Take $\omega(\xi)=\sqrt{g|\xi|+\sigma|\xi|^3}$ and look for a second-harmonic resonance $2\omega(\xi_0)=\omega(2\xi_0)$, $\xi_0>0$. Squaring:
$$4\big(g\xi_0+\sigma\xi_0^3\big) = 2g\xi_0 + 8\sigma\xi_0^3 \;\Longrightarrow\; 2g\xi_0 = 4\sigma\xi_0^3 \;\Longrightarrow\; \boxed{\;\xi_0=\sqrt{g/(2\sigma)}\;}$$
For water, $g = 9.8\ \mathrm{m\,s^{-2}}$ and $\sigma/\rho = 7.3\times10^{-5}\ \mathrm{m^3 s^{-2}}$:
$$\xi_0=\sqrt{9.8/(1.46\times10^{-4})}\approx 259\ \mathrm{rad/m}, \qquad \lambda_0 = 2\pi/\xi_0 \approx 2.4\ \mathrm{cm}.$$
This is the classical Wilton ripple wavelength. At $\xi_0$ the quadratic normal-form denominator $\omega(2\xi)-2\omega(\xi)$ vanishes, so the transformation removing quadratic terms is singular. This single point is why 2D gravity-capillary global existence is still open even without vorticity.

*Step 3 — constant vorticity.* Set $g=0$, $\sigma=1$, $\gamma=2$, and take the branch $\omega_+(\xi)=-\mathrm{sgn}(\xi)+\sqrt{|\xi|^3+1}$. For $\xi>0$, $F(\xi):=\sqrt{\xi^3+1}-1$ satisfies $F(0)=0$ and
$$F''(\xi)=\frac{3\xi\,(1+\xi^3/4)}{(\xi^3+1)^{3/2}}>0,$$
so $F$ is strictly convex with $F(0)=0$, hence strictly superadditive: co-propagating triples are still non-resonant. But for $\xi<0$ the branch is $\omega_+(\xi)=1+\sqrt{|\xi|^3+1}\ge 2$, while $F(\xi)\to 0$ as $\xi\to 0^+$. The symbol is therefore **not even**, and mixed-sign triples $\xi_1>0>\xi_2$ now satisfy $\omega_+(\xi_1+\xi_2)=\omega_+(\xi_1)+\omega_+(\xi_2)$ on a nonempty set for suitable $\gamma$ — the low-frequency gap $|\gamma|$ supplies the frequency budget that the homogeneous symbol $|\xi|^{3/2}$ could never supply.

**Conclusion of the example.** The clean superadditivity argument of Step 1, which underwrites the only complete 2D global result, is destroyed by adding either gravity (Step 2, a single resonant wavenumber) or constant vorticity (Step 3, a whole resonant curve). Bridging that is precisely the gap in Section 6.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*