---
id: 09-probability/random-schrodinger-operators-mobility-edge
title: "Random Schrödinger Operators Mobility Edge"
topic: 09-probability
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Random Schrödinger Operators Mobility Edge

> **Topic:** Probability & Stochastic Processes · **ID:** `09-probability/random-schrodinger-operators-mobility-edge` · **Status:** open

## 1. Problem Statement / Conjecture

For the Anderson model on $\mathbb{Z}^d$ with $d \ge 3$ and small disorder strength $\lambda$, the spectrum is conjectured to split into two regimes separated by a **mobility edge**: energies near the band centre carry absolutely continuous spectrum and diffusive transport, energies near the band edges carry pure point spectrum with exponentially localized eigenfunctions.

Precisely, let $H_\lambda = -\Delta + \lambda V_\omega$ act on $\ell^2(\mathbb{Z}^d)$, with $V_\omega(x)$ i.i.d. with bounded density. **Conjecture (Anderson transition).** For $d \ge 3$ there is $\lambda_0(d) > 0$ such that for $0 < \lambda < \lambda_0$ there exist energies $E_c^\pm(\lambda)$ in the interior of the almost-sure spectrum $\Sigma_\lambda$ with:

1. $H_\lambda$ has purely absolutely continuous spectrum in $(E_c^-, E_c^+)$, a.s.;
2. $H_\lambda$ has pure point spectrum with exponentially decaying eigenfunctions on $\Sigma_\lambda \setminus [E_c^-, E_c^+]$, a.s.;
3. transport is diffusive in the a.c. region and vanishes in the localized region.

A complete resolution requires either a proof of (1) — **no continuum-model or lattice-model proof of a.c. spectrum at weak disorder in any finite dimension $d \ge 2$ exists** — or a disproof, e.g. showing full localization for all $\lambda>0$ in $d\ge 3$. The complementary conjecture, that **no** mobility edge exists for $d = 1, 2$ (complete localization at all energies and all $\lambda > 0$), is proved for $d=1$ and open for $d=2$.

## 2. Mathematical Foundations

**The model.** On $\ell^2(\mathbb{Z}^d)$,
$$ (H_\omega \psi)(x) = \sum_{|x-y|_1 = 1} \big(\psi(x) - \psi(y)\big) + \lambda\, \omega_x \psi(x), $$
with $(\omega_x)_{x\in\mathbb{Z}^d}$ i.i.d., law $\mu$, and $\lambda \ge 0$. $H_\omega$ is $\mathbb{Z}^d$-ergodic, so by the Pastur–Kunz–Souillard theorem the spectrum and its Lebesgue decomposition are deterministic:
$$ \sigma(H_\omega) = \Sigma_\lambda = [0,4d] + \lambda\,\mathrm{supp}\,\mu \quad \text{a.s.} $$
and $\Sigma_{\rm pp}, \Sigma_{\rm ac}, \Sigma_{\rm sc}$ are a.s. non-random sets.

**Continuum version.** $H_\omega = -\Delta + \sum_{j\in\mathbb{Z}^d} \omega_j\, u(x-j)$ on $L^2(\mathbb{R}^d)$, $u$ a compactly supported single-site bump.

**Localization.** *Anderson (spectral) localization* on $I$: a.s. $H_\omega$ has pure point spectrum in $I$ with eigenfunctions obeying $|\psi(x)| \le C_\omega e^{-m|x|}$. *Dynamical localization*: for all $p$,
$$ \mathbb{E}\Big[\sup_{t\in\mathbb{R}} \big\| |X|^{p/2} e^{-itH_\omega} P_I(H_\omega)\delta_0 \big\|^2 \Big] < \infty. $$

**Delocalization criterion.** With $G_\omega(x,y;z) = \langle \delta_x, (H_\omega - z)^{-1}\delta_y\rangle$, a.c. spectrum on $I$ follows if $\liminf_{\varepsilon\downarrow 0}\operatorname{Im} G_\omega(0,0;E+i\varepsilon) > 0$ on a positive-measure subset of $I$.

**Fractional moment (Aizenman–Molchanov) criterion.** For $0<s<1$, exponential decay
$$ \mathbb{E}\big[|G_\omega(x,y;E+i0)|^s\big] \le C e^{-\mu|x-y|} $$
uniformly in $\varepsilon$ implies spectral and dynamical localization at $E$. This holds when $\lambda$ is large or when $E$ lies where the density of states is thin.

**Density of states and Lifshitz tails.** $N(E) = \lim_{L} L^{-d}\,\\#\{\text{eigenvalues of } H_\omega|_{\Lambda_L} \le E\}$. Near the bottom $E_0$ of $\Sigma_\lambda$,
$$ N(E) \sim \exp\!\big(-c (E-E_0)^{-d/2}\big), \qquad E \downarrow E_0, $$
the *Lifshitz tail* — the quantitative source of band-edge localization.

**Transport exponent.** $\beta(p) = \liminf_{T\to\infty} \frac{\log \langle\!\langle |X|^p\rangle\!\rangle_T}{p \log T}$, where $\langle\!\langle\cdot\rangle\!\rangle_T$ is the time-averaged moment. $\beta = 0$ is localization; $\beta = 1/2$ is diffusion. A **dynamical mobility edge** is a jump of $\beta$ from $0$ to a positive value.

**Self-consistency (SCBA / tree approximation).** On the Bethe lattice of degree $K+1$, the Green function satisfies the recursion $\Gamma_x = (\lambda\omega_x - z - \sum_{y \sim x, \,y \text{ forward}} \Gamma_y)^{-1}$, whose stationary distribution is the exact object analyzed by Abou-Chacra–Anderson–Thouless (1973) and rigorously by Klein (1998).

## 3. History & State of the Art (SOTA)

- **1958.** P. W. Anderson, *Absence of diffusion in certain random lattices*, Phys. Rev. **109**, introduces the model and argues for localization at strong disorder. Nobel Prize 1977.
- **1973.** Abou-Chacra, Anderson, Thouless give the self-consistent theory on the Bethe lattice, predicting a genuine mobility edge.
- **1977–1980.** One dimension settled: Gol'dsheid–Molchanov–Pastur prove localization for a continuum 1D model; Kunz–Souillard prove it for the 1D lattice model. Furstenberg's theorem yields positive Lyapunov exponent at all energies.
- **1979.** Abrahams–Anderson–Licciardello–Ramakrishnan "gang of four" scaling theory: $d=2$ is critical, all states localized for $d\le 2$, mobility edge only for $d\ge 3$.
- **1983.** Fröhlich–Spencer invent **multiscale analysis (MSA)**, proving exponential decay of the Green function at large $\lambda$ or extreme energies in all $d$; Fröhlich–Martinelli–Scoppola–Spencer (1985) upgrade to pure point spectrum. Simon–Wolff (1986) give the rank-one/spectral-averaging route.
- **1993.** Aizenman–Molchanov's **fractional moment method** gives a short proof of localization at large disorder and extreme energies, plus exponential decay of eigenfunction correlators.
- **1996.** Minami's estimate ⇒ Poisson eigenvalue statistics in the localized phase.
- **1998.** Klein proves **absolutely continuous spectrum for the Anderson model on the Bethe lattice at small disorder** — the only rigorous delocalization result for a genuine random Schrödinger operator.
- **2005–2013.** Bourgain–Kenig prove localization for the continuum Bernoulli–Anderson model via quantitative unique continuation; Germinet–Klein give a comprehensive localization proof for singular potentials and construct the *dynamical* transition. Aizenman–Warzel (2011–2013) establish resonant delocalization on trees, showing a.c. spectrum extends into the Lifshitz-tail regime.
- **2007.** Germinet–Klein–Schenker prove **dynamical delocalization** for random Landau Hamiltonians in $d=2$ — near each Landau level, some energy has non-trivial transport.
- **2020–2022.** Ding–Smart (2D) and Li–Zhang (3D) prove Anderson–Bernoulli localization near the spectral edge on the lattice, resolving a long-standing discrete-unique-continuation obstruction.

## 4. Partial Results / Verified Cases

| Setting | Result | Source |
|---|---|---|
| $d=1$, lattice/continuum, any $\lambda>0$ | Complete localization, all energies; positive Lyapunov exponent | Gol'dsheid–Molchanov–Pastur 1977; Kunz–Souillard 1980 |
| Strip $\mathbb{Z}\times\{1,\dots,W\}$ | Complete localization | Klein–Lacroix–Speis 1990 |
| All $d$, $\lambda$ large ($\lambda \gtrsim C d$) | Spectral + dynamical localization on all of $\Sigma_\lambda$ | Fröhlich–Spencer 1983; Aizenman–Molchanov 1993 |
| All $d$, any $\lambda>0$, $E$ near band edges (Lifshitz regime) | Localization on $[E_0, E_0+\delta(\lambda)]$ | Fröhlich–Spencer 1983; Klopp 1990s |
| Continuum, Bernoulli single-site, $d \le 3$ near edge | Localization | Bourgain–Kenig 2005; Germinet–Klein 2013 |
| Lattice Bernoulli, $d=2$ and $d=3$, near edge | Localization | Ding–Smart 2020; Li–Zhang 2022 |
| Bethe lattice (degree $K+1 \ge 3$), small $\lambda$ | **Purely a.c. spectrum** in the interior; mobility edge exists | Klein 1998; Aizenman–Warzel 2013 |
| Random Landau Hamiltonian, $d=2$, strong field | Dynamical delocalization near Landau levels | Germinet–Klein–Schenker 2007 |
| Random band matrices, bandwidth $W$, 1D chain of length $N$ | Delocalization for $W \gg N^{1/2}$; localization for $W \ll N^{1/2}$ | Yau–Yin; Bourgade et al.; Dubova–Yang *(frontier — verify)* |

Nothing above proves a.c. spectrum on $\mathbb{Z}^d$ for any finite $d\ge 2$.

## 5. Principal Obstacles

- **No positive lower bound on $\operatorname{Im} G$.** Every rigorous tool (MSA, fractional moments) is *upper-bound* technology: it shows decay. Proving a.c. spectrum needs a stable lower bound on $\operatorname{Im}G_\omega(0,0;E+i0)$ that survives averaging over $\omega$; no perturbative expansion controls this uniformly in the volume.
- **Divergent diagrammatic expansions.** The perturbative series in $\lambda$ for the two-particle Green function has terms growing like $(\lambda^2 t)^n / n!$-free combinatorics; the diffusive resummation (ladder diagrams) is only controlled up to kinetic times $t \ll \lambda^{-2}$ (Erdős–Salmhofer–Yau), far short of the $t\to\infty$ limit that a.c. spectrum requires.
- **Tree vs. lattice.** Klein's Bethe-lattice proof uses the absence of loops: the forward Green function recursion is exactly a distributional fixed-point equation with a contraction property. On $\mathbb{Z}^d$ loops re-inject correlations and the recursion is not closed. Exponential volume growth of the tree also suppresses the return probability that drives localization on $\mathbb{Z}^d$.
- **Criticality is not a perturbation.** At $E_c$ the conjectured behaviour is multifractal with non-trivial exponents; no renormalization-group scheme for random Schrödinger operators is mathematically controlled at a non-Gaussian fixed point.
- **$d=2$ marginality.** Scaling theory predicts localization length $\xi \sim e^{c/\lambda^2}$ in $d=2$ — non-perturbative in $\lambda$, invisible to any finite-order expansion, and beyond the reach of MSA whose initial-scale estimate needs $\lambda$ large or $E$ in a thin-DOS region.
- **Unique continuation.** For singular (e.g. Bernoulli) potentials, spectral averaging fails; progress required quantitative unique continuation inequalities, discrete versions of which are still restricted to $d\le 3$.

## 6. The Gap

Proven: localization holds (i) everywhere in $d=1$, (ii) at large $\lambda$, (iii) at band edges for every $\lambda$, in every $d$. Delocalization is proven only on trees and, dynamically, for magnetic 2D models.

The precise missing step is a **volume-uniform lower bound**: show that for $d\ge 3$, $\lambda$ small and $E$ near $2d$,
$$ \liminf_{\varepsilon \downarrow 0} \ \mathbb{E}\big[\operatorname{Im} G_\omega(0,0;E+i\varepsilon)\big] > 0 \quad\text{with}\quad \mathbb{E}\big[|G_\omega(0,0;E+i\varepsilon)|^s\big] \text{ non-decaying}, $$
equivalently that the diffusion coefficient $D(E) = \lim_{t\to\infty}\frac{1}{t}\mathbb{E}\langle |X(t)|^2\rangle$ is strictly positive. Existing methods produce $D(E) > 0$ only for times up to $\lambda^{-2-\kappa}$, $\kappa < 2/5$ (Erdős–Salmhofer–Yau), not $t = \infty$. Closing the gap means passing from finitely many to infinitely many collisions.

## 7. Current Research (as of June 2026)

- **Random band matrices as a proxy.** The Yau (Harvard/NYU) and Bourgade (NYU) schools have effectively settled the $\mathbb{Z}^1$ band-matrix transition at $W \sim N^{1/2}$ and are pushing to $\mathbb{Z}^2$/$\mathbb{Z}^3$ band models, where the analogue of the mobility edge should appear; Dubova–Yang report delocalization for 1D band matrices down to nearly optimal bandwidth *(frontier — verify)*.
- **Supersymmetric (SUSY) methods.** Disertori–Spencer–Zirnbauer's rigorous SUSY analysis of the $H^{2|2}$ nonlinear sigma model proves a phase transition (localized/extended) in $d\ge 3$ for that effective model; extending it back to genuine Schrödinger operators is active (IHES, Warwick).
- **Trees with loops / finite-cycle graphs.** Aizenman–Warzel-style resonant delocalization on graphs interpolating between trees and $\mathbb{Z}^d$ (Sabri, Anantharaman; École Polytechnique, Strasbourg).
- **Quantum unique continuation.** Ding–Smart–style discrete unique continuation for $d \ge 4$ Bernoulli models remains open; Li, Zhang, and collaborators continue this line.
- **Eigenvector statistics at the edge of localization.** Refinements of Minami's estimate and Poisson-to-GOE crossover in intermediate regimes (Aizenman, Warzel, Klopp, Shirley).
- **Continuum Anderson at low density (Poisson potential).** Klopp and collaborators on the low-density limit where localization can be proved on a widening energy window.

## 8. Future Work

- Prove a.c. spectrum on $\mathbb{Z}^d$, $d \ge 3$, at small $\lambda$ for a *simplified but non-tree* graph (e.g. $\mathbb{Z}^d$ with slowly decaying long-range hopping, or a hierarchical lattice) as a stepping stone.
- Extend the $t \ll \lambda^{-2-\kappa}$ kinetic control to all $\kappa$, then to $t = \infty$, via renormalization of the four-point function.
- Transfer the SUSY sigma-model transition to the true operator by a rigorous mapping with controlled error.
- Establish GOE local eigenvalue statistics as an operational definition of delocalization on finite boxes with $L \gg \xi$ — a target more tractable than a.c. spectrum.
- Settle $d=2$: prove complete localization for all $\lambda>0$, matching the scaling-theory prediction. Even a proof for $\lambda$ small and $E$ in a fixed compact set would be decisive.

## 9. Key References

- **[Foundational]** P. W. Anderson. *Absence of Diffusion in Certain Random Lattices.* Physical Review **109**, 1492–1505, 1958.
- **[Foundational]** J. Fröhlich, T. Spencer. *Absence of diffusion in the Anderson tight binding model for large disorder or low energy.* Communications in Mathematical Physics **88**, 151–184, 1983.
- **[Foundational]** M. Aizenman, S. Molchanov. *Localization at large disorder and at extreme energies: an elementary derivation.* Communications in Mathematical Physics **157**, 245–278, 1993.
- **[Foundational]** H. Kunz, B. Souillard. *Sur le spectre des opérateurs aux différences finies aléatoires.* Communications in Mathematical Physics **78**, 201–246, 1980.
- **[Delocalization]** A. Klein. *Extended States in the Anderson Model on the Bethe Lattice.* Advances in Mathematics **133**, 163–184, 1998.
- **[Delocalization]** M. Aizenman, S. Warzel. *Resonant delocalization for random Schrödinger operators on tree graphs.* Journal of the European Mathematical Society **15**, 1167–1222, 2013.
- **[SOTA / Recent]** F. Germinet, A. Klein, J. Schenker. *Dynamical delocalization in random Landau Hamiltonians.* Annals of Mathematics **166**, 215–244, 2007.
- **[SOTA / Recent]** J. Bourgain, C. Kenig. *On localization in the continuous Anderson–Bernoulli model in higher dimension.* Inventiones Mathematicae **161**, 389–426, 2005.
- **[SOTA / Recent]** J. Ding, C. K. Smart. *Localization near the edge for the Anderson Bernoulli model on the two dimensional lattice.* Inventiones Mathematicae **219**, 467–506, 2020.
- **[SOTA / Recent]** L. Li, L. Zhang. *Anderson–Bernoulli localization on the three-dimensional lattice and discrete unique continuation principle.* Duke Mathematical Journal **171**, 327–415, 2022.
- **[SOTA / Recent]** L. Erdős, M. Salmhofer, H.-T. Yau. *Quantum diffusion of the random Schrödinger evolution in the scaling limit.* Acta Mathematica **200**, 211–277, 2008.
- **[SOTA / Recent]** M. Disertori, T. Spencer, M. Zirnbauer. *Quasi-diffusion in a 3D supersymmetric hyperbolic sigma model.* Communications in Mathematical Physics **300**, 435–486, 2010.
- **[Survey / Book]** M. Aizenman, S. Warzel. *Random Operators: Disorder Effects on Quantum Spectra and Dynamics.* Graduate Studies in Mathematics 168, American Mathematical Society, 2015.
- **[Survey / Book]** R. Carmona, J. Lacroix. *Spectral Theory of Random Schrödinger Operators.* Birkhäuser, 1990.
- **[Survey]** P. Stollmann. *Caught by Disorder: Bound States in Random Media.* Birkhäuser, 2001.
- **[Survey]** F. Evers, A. D. Mirlin. *Anderson transitions.* Reviews of Modern Physics **80**, 1355–1417, 2008.

## 10. Worked Example / Concrete Special Case

**Claim.** In $d=1$ there is no mobility edge: for every $\lambda>0$ and every energy in the band, the Lyapunov exponent is strictly positive.

Take $H_\omega = -\Delta + \lambda V_\omega$ on $\ell^2(\mathbb{Z})$ with $\mathbb{E}\omega = 0$, $\mathbb{E}\omega^2 = 1$. The eigenvalue equation $\psi(n+1)+\psi(n-1) + \lambda\omega_n\psi(n) = E\psi(n)$ is a transfer-matrix product:
$$ \begin{pmatrix}\psi(n+1)\\ \psi(n)\end{pmatrix} = A_n(E)\begin{pmatrix}\psi(n)\\ \psi(n-1)\end{pmatrix}, \qquad A_n(E) = \begin{pmatrix} E - \lambda\omega_n & -1 \\ 1 & 0\end{pmatrix}. $$
Set $\gamma(E) = \lim_{N} \frac{1}{N}\mathbb{E}\log\|A_N \cdots A_1\|$, the Lyapunov exponent (Furstenberg–Kesten).

**Positivity.** For $E \in (-2,2)$ the group generated by $\mathrm{supp}(A_n)$ in $SL(2,\mathbb{R})$ is non-compact and strongly irreducible (the free matrices have no common invariant finite union of directions once $\mathrm{supp}\,\mu$ has two points). Furstenberg's theorem then gives $\gamma(E) > 0$ for **all** $E$, with no exceptional interval.

**Quantitative weak-disorder value.** Write $E = 2\cos k$, $k\in(0,\pi)$. Second-order perturbation in $\lambda$ (Thouless formula / Pastur–Figotin) gives
$$ \gamma(E) \;=\; \frac{\lambda^2}{8\sin^2 k} + O(\lambda^4) \;=\; \frac{\lambda^2}{8\,(1 - E^2/4)} + O(\lambda^4), $$
i.e. localization length $\xi(E) = \gamma(E)^{-1} \approx 8(1-E^2/4)/\lambda^2$. Numerically, at $\lambda = 0.2$ and $E = 0$: $\gamma = 0.04/8 = 5\times10^{-3}$, so $\xi \approx 200$ sites. At $E = 1.8$: $1-E^2/4 = 0.19$, giving $\gamma \approx 2.6\times10^{-2}$, $\xi \approx 38$ sites.

**Interpretation.** $\gamma(E)$ is a smooth, strictly positive function of $E$ across the whole band; it grows towards the band edges but never vanishes inside. By Kotani theory, $\gamma > 0$ on a set of full Lebesgue measure forces $\Sigma_{\rm ac} = \emptyset$. So the $d=1$ picture is "localization everywhere, with an energy-dependent length" — no critical $E_c$.

The conjectured $d\ge 3$ picture is qualitatively different: $\xi(E)$ should **diverge** as $E \to E_c^{\pm}$ like $|E-E_c|^{-\nu}$ with $\nu \approx 1.57$ (numerics for the 3D orthogonal class), and be genuinely infinite inside. Producing a rigorous analogue of the calculation above that yields $\gamma \equiv 0$ on an interval, for any lattice of dimension $\ge 2$, is exactly the open problem.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*