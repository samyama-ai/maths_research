---
id: 09-probability/conformal-invariance-of-the-2d-ising-model
title: "Conformal Invariance of the 2D Ising Model"
topic: 09-probability
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Conformal Invariance of the 2D Ising Model

> **Topic:** Probability & Stochastic Processes · **ID:** `09-probability/conformal-invariance-of-the-2d-ising-model` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

Let $\Omega \subset \mathbb{C}$ be a bounded simply connected domain and let $\Omega_\delta$ be its discretization by the square lattice $\delta\mathbb{Z}^2$. Run the Ising model on $\Omega_\delta$ at the critical temperature. The conjecture, in the form stated by physicists since the 1980s, is:

**(CI)** All scaling limits ($\delta \to 0$) of critical Ising observables — spin correlations, energy densities, interfaces, loop ensembles, and the magnetization field — exist, are **universal** (independent of the lattice and of the local weights, given criticality), and are **conformally covariant**: for a conformal bijection $\varphi:\Omega \to \Omega'$ and a primary field $\mathcal{O}$ of scaling dimension $\Delta$,
$$\langle \mathcal{O}(z_1)\cdots \mathcal{O}(z_n)\rangle_\Omega = \prod_{j=1}^n |\varphi'(z_j)|^{\Delta}\,\langle \mathcal{O}(\varphi(z_1))\cdots \mathcal{O}(\varphi(z_n))\rangle_{\Omega'} .$$
The limits are those predicted by the unitary minimal conformal field theory $\mathcal{M}(4,3)$ of central charge $c = 1/2$, with $\Delta_\sigma = 1/8$ and $\Delta_\varepsilon = 1$; interfaces converge to $\mathrm{SLE}_3$ and loop ensembles to $\mathrm{CLE}_3$ (FK-Ising: $\mathrm{SLE}_{16/3}$, $\mathrm{CLE}_{16/3}$).

A complete resolution requires proofs of existence, conformal covariance, and universality for the full family of correlation functions, together with the identification of the limiting objects with the $c=1/2$ CFT. Large parts of this program are now theorems; the residual open part is universality beyond a restricted class of graphs and the construction of the full CFT (all fields, all boundary conditions, operator product expansions) as a probabilistic limit.

## 2. Mathematical Foundations

**The model.** On a finite graph $G=(V,E)$ with configurations $\sigma \in \{\pm 1\}^V$,
$$\mu_\beta(\sigma) = \frac{1}{Z_\beta}\exp\Big(\beta \sum_{\{u,v\}\in E} J_{uv}\,\sigma_u\sigma_v\Big).$$
On $\mathbb{Z}^2$ with $J\equiv 1$, Kramers–Wannier duality fixes the self-dual point, and criticality is
$$\sinh(2\beta_c)=1, \qquad \beta_c = \tfrac{1}{2}\log(1+\sqrt{2}) .$$

**FK representation.** The random-cluster measure with $q=2$ on configurations $\omega \subset E$,
$$\phi_{p,2}(\omega) \propto p^{|\omega|}(1-p)^{|E\setminus\omega|}\,2^{k(\omega)},$$
is coupled to the Ising model via the Edwards–Sokal coupling; $p_c = \sqrt{2}/(1+\sqrt{2})$.

**Smirnov's fermionic observable.** On the medial lattice, for a Dobrushin domain $(\Omega_\delta,a,b)$ with the exploration path $\gamma$, set
$$F_\delta(z) = \mathbb{E}\big[\mathbf{1}_{z \in \gamma}\, e^{-\frac{i}{2}\,\mathrm{wind}(\gamma, z\to b)}\big],$$
where $\mathrm{wind}$ is the total turning of the path. The half-integer $1/2$ is the fermionic spin. $F_\delta$ is **s-holomorphic**: for every edge $(z,z')$ of the medial lattice with prescribed direction $\eta$,
$$\mathrm{Pr}_{\eta}\big[F_\delta(z)\big] = \mathrm{Pr}_{\eta}\big[F_\delta(z')\big],$$
where $\mathrm{Pr}_\eta$ is orthogonal projection onto $\eta\,\mathbb{R} \subset \mathbb{C}$. S-holomorphicity implies the discrete Cauchy–Riemann equations and, crucially, that $\mathrm{Im}\!\int^z F_\delta^2$ is a well-defined discrete function which is sub-/super-harmonic depending on the sublattice.

**The limit.** Smirnov's theorem: $\delta^{-1/2}F_\delta \to \sqrt{\varphi'}$, where $\varphi:\Omega\to\mathbb{R}\times(0,1)$ is the conformal map sending $a,b$ to $\mp\infty$. Convergence of the observable, plus a precompactness/Loewner argument, yields interface convergence.

**Isoradial graphs.** A planar graph is isoradial if every face is inscribed in a circle of common radius $\delta$; the *critical* (Z-invariant) Ising weights are $\sinh(2\beta_e J_e) = \tan(\theta_e/2)^{\pm1}$ in terms of the half-angle $\theta_e$ of the rhombus of $e$. This is the class in which universality is proved.

## 3. History & State of the Art (SOTA)

- **1944.** Onsager computes the free energy of the square-lattice Ising model; Yang (1952) obtains the spontaneous magnetization $(1-\sinh^{-4} 2\beta)^{1/8}$, fixing the exponent $1/8$.
- **1966.** Kadanoff's block-spin renormalization; Polyakov (1970) argues scale invariance upgrades to conformal invariance.
- **1984.** Belavin, Polyakov, Zamolodchikov construct 2D CFT; the Ising model is identified with the $c=1/2$ minimal model, giving exact correlation formulas.
- **1999–2001.** Schramm invents SLE; Smirnov proves conformal invariance of critical site percolation on the triangular lattice (Cardy's formula), setting the template.
- **2006–2010.** Smirnov introduces the discrete fermionic observable and proves conformal invariance of the FK-Ising and Ising interface observables (announced ICM 2006; *Ann. of Math.* 2010). Fields Medal 2010.
- **2012.** Chelkak–Smirnov prove universality on isoradial graphs.
- **2013–2015.** Hongler–Smirnov (energy density), Chelkak–Hongler–Izyurov (spin correlations), Camia–Garban–Newman (magnetization field), Benoist–Hongler (CLE$_3$).

The problem's status has therefore moved from "open conjecture" to "solved for a large and canonical family of observables on a restricted graph class".

## 4. Partial Results / Verified Cases

| Object | Result | Reference |
|---|---|---|
| FK-Ising interface, Dobrushin b.c. | $\to \mathrm{SLE}_{16/3}$; observable $\to\sqrt{\varphi'}$ | Smirnov 2010; Chelkak–Duminil-Copin–Hongler–Kemppainen–Smirnov 2014 |
| Ising spin interface | $\to \mathrm{SLE}_3$ | CDCHKS 2014 |
| Energy density $\varepsilon = \sigma_u\sigma_v - \tfrac{\sqrt2}{2}$ | $\delta^{-1}\mathbb{E}[\varepsilon]$ converges, covariance exponent $\Delta_\varepsilon=1$ | Hongler–Smirnov, *Acta Math.* 2013 |
| $n$-point spin correlations | $\delta^{-n/8}\mathbb{E}[\sigma_{a_1}\!\cdots\sigma_{a_n}] \to \mathcal{C}^n\langle\sigma\cdots\sigma\rangle_\Omega$, plus/free b.c. | Chelkak–Hongler–Izyurov, *Ann. of Math.* 2015 |
| Magnetization field $\delta^{15/8}\sum\sigma_x$ | unique conformally covariant limit, non-Gaussian | Camia–Garban–Newman, *Ann. Probab.* 2015 |
| Full collection of spin interfaces | $\to \mathrm{CLE}_3$ | Benoist–Hongler, *Ann. Probab.* 2019 |
| Universality class | isoradial graphs with Z-invariant critical weights, any rhombus angles bounded away from $0,\pi$ | Chelkak–Smirnov 2012; Chelkak–Izyurov–Mahfouf 2023 |
| Boundary conditions | free, plus/minus, and Dobrushin-type mixtures with finitely many changes | Izyurov 2015; Hongler–Kytölä 2013 |
| Near-critical / massive regime | massive SLE$_3$ and massive observables on $\mathbb{Z}^2$ | Makarov–Smirnov 2010; Park 2018–2021 |

## 5. Principal Obstacles

- **Exact solvability is the engine.** Every proof rests on a discrete holomorphic (free-fermion) structure that is a lattice-level miracle. It exists for $q=2$ random-cluster and for dimer models, and it degenerates for $q\neq 2$. There is no perturbative or soft-analytic replacement.
- **S-holomorphicity is fragile.** The local relation defining s-holomorphic functions needs the rhombic/isoradial geometry to close. On a generic weighted planar graph at criticality, the natural observable satisfies no exact discrete Cauchy–Riemann system, so the whole convergence machinery collapses at step one.
- **Boundary regularity.** Convergence estimates near the boundary require uniform discrete Beurling-type bounds; rough boundaries, cusps, and multiply connected domains (where a modulus enters, breaking the reduction to a single conformal map) need new input.
- **No renormalization-group proof.** RG explains universality heuristically but has never been made rigorous here; conversely the integrable proofs give universality only inside the class where integrability survives.
- **Fields beyond $\sigma$ and $\varepsilon$.** Descendants, the stress-energy tensor $T$, and OPE structure constants require joint control of correlations at coinciding points, i.e. uniform multi-scale estimates that current observable-by-observable methods do not deliver.

## 6. The Gap

Precisely:

1. **Universality off isoradiality.** Section 4's results hold for isoradial graphs with Z-invariant weights. The conjecture asserts the same limits for *any* critical planar Ising model — e.g. periodic lattices with generic anisotropic couplings, doubly periodic graphs, or random planar environments. The missing step is a substitute for s-holomorphicity. Chelkak's **s-embeddings** are the leading candidate: they re-embed an arbitrary weighted planar graph so that the propagation equation becomes discrete-holomorphic, but the required convergence of s-embeddings to a "nice" (Lorentz-minimal-surface) limit is proved only under hypotheses that are hard to verify in examples.
2. **Full CFT.** Proved: individual correlation families converge to explicit $c=1/2$ formulas. Not proved: that the limit carries a Virasoro action of central charge $1/2$, or that all $\mathcal{M}(4,3)$ fields and their OPEs arise probabilistically as a single coherent scaling limit.
3. **Dimension three.** No conformal invariance statement in $d=3$ is proven; the conformal bootstrap gives high-precision numerics ($\Delta_\sigma \approx 0.5181489$) but the assumption of conformal invariance itself is unproven.

## 7. Current Research (as of June 2026)

- **S-embeddings and t-embeddings** (Chelkak; Chelkak–Laslier–Russkikh; Chelkak–Ramassamy). The programme extends discrete complex analysis to general weighted planar graphs and to bipartite dimers, with the Lorentz-minimal-surface geometry as the continuum object. *(frontier — verify)* claims of universality for genuinely non-isoradial doubly periodic Ising models remain hypothesis-dependent.
- **Ising CFT as a probabilistic object** (Hongler, Kytölä, Viklund, Peltola, Zurich/Aalto/Helsinki schools): discrete stress-energy tensor, discrete Virasoro representations, and convergence of discrete correlation kernels.
- **Massive and off-critical scaling limits** (Park, Chelkak–Park): massive SLE$_3$, near-critical magnetization fields.
- **Multiple SLEs and partition functions** (Peltola–Wu, Izyurov, Beffara–Peltola–Wu): pure partition functions for $\mathrm{SLE}_3$ with $2N$ boundary points, matching Ising boundary-condition-changing operators.
- **Bootstrap–probability interface**: reconciling the rigorous $d=2$ limits with the numerical $d=3$ bootstrap; no rigorous bridge yet.
- **Random geometry**: Ising on random planar maps and its coupling to Liouville quantum gravity with $\gamma=\sqrt{3}$ via mating-of-trees (Gwynne–Miller, Chen–Curien and successors).

## 8. Future Work

- Prove that s-embeddings of a general critical planar Ising model converge, removing the isoradiality hypothesis — the single highest-value open step.
- Construct the Virasoro action on the scaling limit directly, and prove OPE relations probabilistically, thereby deriving BPZ equations rather than importing them.
- Extend to multiply connected domains and to Riemann surfaces, where moduli dependence must be handled.
- Develop a rigorous renormalization-group argument for universality that does not use integrability; this is the only route with plausible relevance to $d=3$.
- Understand mixed correlations $\langle \sigma\cdots\sigma\,\varepsilon\cdots\varepsilon\rangle$ and boundary-operator fusion uniformly in the separation of points.

## 9. Key References

- **[Foundational]** L. Onsager. *Crystal Statistics. I. A Two-Dimensional Model with an Order-Disorder Transition.* Physical Review 65, 117–149, 1944.
- **[Foundational]** A. A. Belavin, A. M. Polyakov, A. B. Zamolodchikov. *Infinite conformal symmetry in two-dimensional quantum field theory.* Nuclear Physics B 241, 333–380, 1984.
- **[Foundational]** O. Schramm. *Scaling limits of loop-erased random walks and uniform spanning trees.* Israel Journal of Mathematics 118, 221–288, 2000.
- **[SOTA]** S. Smirnov. *Conformal invariance in random cluster models. I. Holomorphic fermions in the Ising model.* Annals of Mathematics 172, 1435–1467, 2010.
- **[SOTA]** D. Chelkak, S. Smirnov. *Universality in the 2D Ising model and conformal invariance of fermionic observables.* Inventiones Mathematicae 189, 515–580, 2012.
- **[SOTA]** D. Chelkak, H. Duminil-Copin, C. Hongler, A. Kemppainen, S. Smirnov. *Convergence of Ising interfaces to Schramm's SLE curves.* Comptes Rendus Mathématique 352, 157–161, 2014.
- **[SOTA]** C. Hongler, S. Smirnov. *The energy density of the critical Ising model.* Acta Mathematica 211, 191–225, 2013.
- **[SOTA]** D. Chelkak, C. Hongler, K. Izyurov. *Conformal invariance of spin correlations in the planar Ising model.* Annals of Mathematics 181, 1087–1138, 2015.
- **[SOTA]** F. Camia, C. Garban, C. M. Newman. *Planar Ising magnetization field I. Uniqueness of the critical scaling limit.* Annals of Probability 43, 528–571, 2015.
- **[SOTA]** S. Benoist, C. Hongler. *The scaling limit of critical Ising interfaces is CLE(3).* Annals of Probability 47, 2049–2086, 2019.
- **[Recent]** D. Chelkak, K. Izyurov, R. Mahfouf. *Universality of spin correlations in the Ising model on isoradial graphs.* Annals of Probability 51, 840–898, 2023.
- **[Survey]** H. Duminil-Copin, S. Smirnov. *Conformal invariance of lattice models.* In: Probability and Statistical Physics in Two and More Dimensions, Clay Mathematics Proceedings 15, AMS, 2012.
- **[Survey]** D. Chelkak. *Planar Ising model at criticality: state-of-the-art and perspectives.* Proceedings of the ICM 2018, Vol. IV, 2801–2828.
- **[Survey]** A. Kemppainen, S. Smirnov. *Random curves, scaling limits and Loewner evolutions.* Annals of Probability 45, 698–779, 2017.

## 10. Worked Example / Concrete Special Case

**Conformal covariance of the one-point magnetization, checked explicitly.**

Take $\Omega=\mathbb{H}$ (upper half-plane) with $+$ boundary conditions. The theorem of Chelkak–Hongler–Izyurov gives, for $a_\delta \to z \in \Omega$,
$$\delta^{-1/8}\,\mathbb{E}^{+}_{\Omega_\delta}[\sigma_{a_\delta}] \longrightarrow \mathcal{C}\cdot\langle \sigma(z)\rangle^{+}_{\Omega},$$
with a lattice-dependent constant $\mathcal{C}$ (for $\mathbb{Z}^2$, $\mathcal{C}=2^{5/48}e^{-\frac{3}{2}\zeta'(-1)}$) and the universal profile
$$\langle \sigma(z)\rangle^{+}_{\mathbb{H}} = (2\,\mathrm{Im}\,z)^{-1/8}.$$
The exponent $1/8=\Delta_\sigma$ is exactly Yang's magnetization exponent — the lattice input that fixes the CFT.

Now transport this to the unit disk $\mathbb{D}$ using
$$\varphi(w) = i\,\frac{1-w}{1+w}, \qquad \varphi:\mathbb{D}\xrightarrow{\ \sim\ }\mathbb{H}.$$
Compute the two ingredients:
$$\varphi'(w) = \frac{-2i}{(1+w)^2} \ \Longrightarrow\ |\varphi'(w)| = \frac{2}{|1+w|^2},$$
$$\mathrm{Im}\,\varphi(w) = \mathrm{Re}\!\left[\frac{(1-w)(1+\bar w)}{|1+w|^2}\right] = \frac{1-|w|^2}{|1+w|^2}.$$
The covariance rule with $\Delta_\sigma = 1/8$ gives
$$\langle\sigma(w)\rangle^{+}_{\mathbb{D}} = |\varphi'(w)|^{1/8}\,\langle\sigma(\varphi(w))\rangle^{+}_{\mathbb{H}} = \left(\frac{2}{|1+w|^2}\right)^{1/8}\left(\frac{2(1-|w|^2)}{|1+w|^2}\right)^{-1/8} = \big(1-|w|^2\big)^{-1/8}.$$

Three checks fall out.

1. **Consistency.** The answer depends on $w$ only through $|w|$, as rotational symmetry of $\mathbb{D}$ demands — although the map $\varphi$ used to derive it was not rotation-equivariant. Any other conformal map $\mathbb{D}\to\mathbb{H}$ (i.e. $\varphi$ post-composed with a Möbius automorphism of $\mathbb{H}$) gives the same result, because the automorphism contributes $|\psi'|^{1/8}$ which cancels against the change in $\mathrm{Im}$.
2. **Normalization.** At the center, $\langle\sigma(0)\rangle^{+}_{\mathbb{D}} = 1$, so the disk of radius $1$ is the natural unit of scale: on the lattice, $\mathbb{E}^+[\sigma_0] \approx \mathcal{C}\,\delta^{1/8}$ in a disk of radius $1$.
3. **Boundary blow-up.** As $|w|\to 1$, $\langle\sigma(w)\rangle \sim (2\,\mathrm{dist}(w,\partial\mathbb{D}))^{-1/8}$, matching the half-plane formula locally — the boundary magnetization diverges with the same exponent $1/8$. On the lattice nothing diverges: $\mathbb{E}^+[\sigma_a]\le 1$ always. The divergence is the price of the $\delta^{-1/8}$ renormalization, and it says that the spin field is a distribution of negative regularity, not a function — which is precisely why the magnetization field must be built as a random generalized function (Camia–Garban–Newman) rather than pointwise.

The same computation with $n$ points reproduces the $\mathcal{M}(4,3)$ answer; e.g. in the full plane $\langle\sigma(z_1)\sigma(z_2)\rangle = |z_1-z_2|^{-1/4}$, so the critical two-point function decays with exponent $\eta = 1/4$, Onsager–Kaufman's lattice result.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*