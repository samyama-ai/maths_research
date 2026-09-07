---
id: 06-pdes/mean-curvature-flow-singularities
title: "Mean Curvature Flow Singularities"
topic: 06-pdes
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Mean Curvature Flow Singularities

> **Topic:** Partial Differential Equations · **ID:** `06-pdes/mean-curvature-flow-singularities` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Mean curvature flow (MCF) is the $L^2$-gradient flow of area: a family of hypersurfaces $M_t \subset \mathbb{R}^{n+1}$ evolving by $\partial_t x = \vec{H}$. Closed hypersurfaces always become singular in finite time. The problem is to **classify those singularities and continue the flow through them**.

Three linked statements drive the field.

- **Ilmanen's genericity conjecture.** For a generic (open dense, or at least dense) set of smooth closed initial hypersurfaces $M_0 \subset \mathbb{R}^{n+1}$, every singularity of the flow is *cylindrical*: each tangent flow is a multiplicity-one shrinking $S^k \times \mathbb{R}^{n-k}$, $0 \le k \le n$.
- **Ilmanen's multiplicity-one conjecture.** For flows of smooth closed hypersurfaces, every tangent flow at a singular point has multiplicity one.
- **Uniqueness of blowups.** The tangent flow at a given space-time singular point is independent of the rescaling sequence.

A complete resolution means: prove or disprove each in every dimension $n$, and derive from it a canonical weak flow past singularities that is unique for generic data. A disproof would exhibit a non-perturbable singularity model — e.g. an open set of initial data all of whose flows develop a degenerate neckpinch, or a multiplicity-two tangent plane arising from smooth embedded data.

## 2. Mathematical Foundations

Let $M^n \subset \mathbb{R}^{n+1}$ be smooth, closed, embedded, with unit normal $\nu$, second fundamental form $A_{ij}$, and mean curvature $H = g^{ij}A_{ij}$. A one-parameter family $x(\cdot,t)$ solves MCF if
$$\partial_t x = -H\nu = \Delta_{M_t} x .$$
This is a quasilinear degenerate-parabolic system. Evolution equations:
$$\partial_t H = \Delta H + |A|^2 H, \qquad \partial_t |A|^2 = \Delta |A|^2 - 2|\nabla A|^2 + 2|A|^4 .$$
The maximum principle gives finite extinction time $T \le \frac{\operatorname{diam}(M_0)^2}{2n}$-scale bounds, and **Huisken's blowup rate**
$$\max_{M_t}|A|^2 \ \ge\ \frac{1}{2(T-t)} .$$

**Huisken's monotonicity formula.** With the backward heat kernel centred at $(x_0,t_0)$,
$$\rho_{x_0,t_0}(x,t) = \big(4\pi(t_0-t)\big)^{-n/2} \exp\!\Big(-\frac{|x-x_0|^2}{4(t_0-t)}\Big),$$
one has
$$\frac{d}{dt}\int_{M_t}\rho_{x_0,t_0}\,d\mu = -\int_{M_t}\Big|\vec H + \frac{(x-x_0)^{\perp}}{2(t_0-t)}\Big|^2 \rho_{x_0,t_0}\,d\mu \ \le 0 .$$
The limit $\Theta(x_0,t_0)=\lim_{t\uparrow t_0}\int \rho\,d\mu$ is the **Gaussian density**.

**Self-shrinkers.** Parabolic rescaling $M^s_t = \lambda(M_{t_0+\lambda^{-2}t} - x_0)$ produces, along subsequences, a **tangent flow** that is self-similar: $\Sigma_t = \sqrt{-t}\,\Sigma$ with $\Sigma$ satisfying
$$H = \frac{\langle x,\nu\rangle}{2}.$$
Examples: hyperplanes, $S^n(\sqrt{2n})$, cylinders $S^k(\sqrt{2k})\times\mathbb{R}^{n-k}$, and the Angenent torus in $\mathbb{R}^3$.

**Entropy** (Colding–Minicozzi): $\lambda(M) = \sup_{x_0,t_0} \int_M \rho_{x_0,t_0}\,d\mu$, monotone nonincreasing under MCF and invariant under dilation and translation. Values: $\lambda(S^1)=\sqrt{2\pi/e}\approx 1.5203$, $\lambda(S^2)=4/e\approx 1.4715$, and $\lambda(S^k\times\mathbb{R}^{n-k})=\lambda(S^k)$.

**Type I / Type II.** A singularity is Type I if $|A|^2 \le C/(T-t)$; otherwise Type II. Type I blowups are self-shrinkers; Type II blowups (after suitable rescaling) are eternal **translating solitons** $H = \langle v,\nu\rangle$, e.g. the rotationally symmetric bowl soliton.

**Weak formulations.** Brakke flows (varifold, 1978), level-set/viscosity flows (Evans–Spruck; Chen–Giga–Goto, 1991), and $(\epsilon,R)$-canonical neighborhood/Bamler–Kleiner-style flows with surgery.

## 3. History & State of the Art (SOTA)

- **1978** — Brakke introduces varifold MCF and proves a partial regularity theorem.
- **1984** — Huisken: a closed convex $M_0^n$, $n\ge2$, shrinks to a round point. Gage–Hamilton (1986) and Grayson (1987) settle $n=1$: any embedded closed curve becomes convex and shrinks to a round point, so for curves *all* singularities are circles.
- **1990** — Huisken proves the monotonicity formula; classifies Type I shrinkers with $H\ge0$ as spheres, cylinders, planes.
- **1995** — Ilmanen: elliptic regularization; tangent flows of surface flows ($n=2$) are *smooth* self-shrinkers, possibly with multiplicity. He states the genericity and multiplicity-one conjectures.
- **1994–2003** — White's local regularity theorem: $\Theta \le 1+\epsilon$ implies smoothness; and stratification of the singular set of mean-convex flows.
- **2012** — Colding–Minicozzi, *Generic mean curvature flow I* (Annals): the only entropy-stable self-shrinkers with polynomial volume growth are the generalized cylinders $S^k\times\mathbb{R}^{n-k}$; all others can be perturbed away.
- **2015** — Colding–Minicozzi (Annals): uniqueness of cylindrical tangent flows via a Łojasiewicz–Simon inequality.
- **2019–2023** — Choi–Haslhofer–Hershkovits: mean-convex neighborhood theorem in $\mathbb{R}^3$; with White, extension to $\mathbb{R}^{n+1}$ for cylindrical singularities. Bamler–Kleiner prove the multiplicity-one conjecture for $n=2$.
- **2024** — Chodosh–Choi–Mantoulidis–Schulze: generic MCF in $\mathbb{R}^3$ has only spherical and cylindrical singularities.

## 4. Partial Results / Verified Cases

| Setting | Result |
|---|---|
| $n=1$ (curves in $\mathbb{R}^2$) | Fully solved: Gage–Hamilton 1986, Grayson 1987 — round point. |
| Convex $M_0^n$, any $n$ | Huisken 1984: single spherical singularity. |
| Mean convex ($H>0$), any $n$ | Huisken–Sinestrari, White: all blowups are convex; singular set has parabolic Hausdorff dimension $\le n-1$; surgery exists for $n\ge2$ (Huisken–Sinestrari 2009 for $n\ge3$ with 2-convexity; Brendle–Huisken 2016 for $n=2$; Haslhofer–Kleiner 2017). |
| $n=2$, $\mathbb{R}^3$, generic $M_0$ | CCMS 2024: all singularities are multiplicity-one $S^2$ or $S^1\times\mathbb{R}$; flow is unique after perturbation. |
| $n=2$, multiplicity one | Bamler–Kleiner 2023: proved for closed embedded surfaces. |
| $n=3$, low entropy | Chodosh–Choi–Mantoulidis–Schulze: generic low-entropy flows in $\mathbb{R}^4$ ($\lambda(M_0)\le \lambda(S^2\times\mathbb{R})$) have only spherical/cylindrical singularities. |
| Genus-zero shrinkers, $n=2$ | Brendle 2016 (Annals): an embedded genus-zero self-shrinker in $\mathbb{R}^3$ is a plane, sphere, or cylinder. |
| Entropy lower bound | Bernstein–Wang (JAMS 2016) for $n\le 6$; J. Zhu (JDG) all $n$: $\lambda(M)\ge\lambda(S^n)$ for closed $M^n$, equality iff round. |
| Cylindrical tangent flows | Colding–Minicozzi 2015: uniqueness of blowup; Colding–Minicozzi 2016: singular set is contained in finitely many Lipschitz submanifolds plus a countable set. |
| Type I, any $n$ | Blowups are shrinkers (Huisken 1990); Le–Sesum, Colding–Minicozzi: $\Theta$-gap theorems. |

## 5. Principal Obstacles

- **Non-compactness of the shrinker moduli space.** Self-shrinkers in $\mathbb{R}^{n+1}$ for $n\ge3$ are not classified; even the list of entropy-stable ones is only known under polynomial volume growth. Any classification scheme must handle non-compact, high-genus, and singular ($C^{1,\alpha}$ conical) shrinkers, which exist (Kapouleas–Kleene–Møller, Nguyen: infinitely many complete embedded shrinkers in $\mathbb{R}^3$).
- **Multiplicity in dimension $\ge3$.** Compactness of Brakke flows is only in the varifold sense; a sequence of smooth rescalings can converge to a *higher-multiplicity plane*, where White's local regularity and standard Allard-type theory give no information. Bamler–Kleiner's proof is intrinsically 2-dimensional (it uses the topology of surfaces and continuity/Gauss–Bonnet arguments); no substitute exists for $n\ge3$.
- **Degenerate neckpinches.** Angenent–Velázquez constructed Type II singularities modelled on translating solitons. They are believed non-generic, but proving that requires a perturbation theory for *unstable, non-self-similar* asymptotics; Łojasiewicz inequalities are only available near cylinders.
- **Genericity is not a transversality argument.** MCF is not a smooth flow on a Banach manifold past $T$; "perturb the initial data" must be executed through singular times, so one needs uniqueness/continuity of the weak flow — precisely what the singularity classification is supposed to yield. CCMS break this circularity in $\mathbb{R}^3$ using ancient one-sided flows; the construction relies on mean-convex neighborhoods, again $n=2$-specific.
- **High-dimension phenomena.** Velázquez's example of a flow developing a singularity modelled on the Simons cone in $\mathbb{R}^8$ (and Stolarski's asymptotically conical singularities) shows non-cylindrical singularities really occur; ruling them out generically requires understanding the instability index of singular shrinkers.

## 6. The Gap

Proven: complete classification for $n=1$; for $n=2$ in $\mathbb{R}^3$, generic singularities are spheres and cylinders with multiplicity one; for mean-convex data in all $n$, convexity of blowups and a surgery theory; uniqueness of blowups *given* a cylindrical tangent flow.

Missing: for $n\ge3$ and general (non-mean-convex) initial data, (i) multiplicity one, (ii) a proof that every non-cylindrical shrinker — including compact ones of positive genus, non-compact ones with conical ends, and singular shrinkers — is dynamically unstable in a sense strong enough to be perturbed away through the singular time, and (iii) uniqueness of blowups at non-cylindrical singularities. The single sharpest step is: **rule out multiplicity-$\ge2$ tangent flows for flows of closed embedded hypersurfaces in $\mathbb{R}^{n+1}$, $n\ge3$**, since almost all subsequent machinery (local regularity, sheeting, one-sided perturbation) is unlocked by it.

## 7. Current Research (as of June 2026)

- **Bamler–Kleiner program** (NYU/Berkeley): extending multiplicity-one and the structure theory of singular sets beyond surfaces; their $\mathbb{R}^3$ results give a canonical weak flow through singularities that is unique for generic data. *(frontier — verify: claimed extensions to $n\ge3$ under entropy bounds.)*
- **Chodosh–Choi–Mantoulidis–Schulze** (Stanford/Cornell/UCL and collaborators): generic flows in $\mathbb{R}^4$ under low-entropy hypotheses; ancient one-sided flows as the technical engine.
- **Haslhofer–Choi–Hershkovits** (Toronto/Hebrew University): ancient noncollapsed flows classification in $\mathbb{R}^4$ (Choi–Haslhofer–Hershkovits–White), and canonical neighborhoods.
- **Shrinker classification**: Brendle-style Codazzi/Simons arguments, Bernstein–Wang's topological approach in low entropy, and numerical constructions (Chopp; Kapouleas–Kleene–Møller desingularization).
- **Łojasiewicz methods**: Colding–Minicozzi's rate-of-convergence machinery being adapted to conical and asymptotically conical shrinkers (Chodosh–Schulze; Zhu).
- **Networks and higher codimension**: analogous singularity questions for MCF of networks (Mantegazza–Novaga–Tortorelli) and Lagrangian MCF (Neves; Joyce's conjecture) are active parallel tracks.

## 8. Future Work

- Prove multiplicity one under a bounded-entropy assumption in $\mathbb{R}^{n+1}$, $n\ge3$, using quantitative stratification (Cheeger–Haslhofer–Naber) plus sheeting estimates.
- Establish a general instability/Łojasiewicz theory at *conical* shrinkers, converting Colding–Minicozzi entropy instability into genuine dynamical perturbation.
- Classify self-shrinkers in $\mathbb{R}^4$ with entropy below $\lambda(S^1)$, closing the gap in the low-entropy program.
- Determine whether the set of initial data with only generic singularities is *open* (currently only density is targeted).
- Build a surgery theory without mean convexity, using the generic-singularity classification as the canonical-neighborhood input.

## 9. Key References

- **[Foundational]** G. Huisken. *Flow by mean curvature of convex surfaces into spheres.* Journal of Differential Geometry 20 (1984), 237–266.
- **[Foundational]** G. Huisken. *Asymptotic behavior for singularities of the mean curvature flow.* Journal of Differential Geometry 31 (1990), 285–299.
- **[Foundational]** K. Brakke. *The Motion of a Surface by its Mean Curvature.* Princeton University Press, 1978.
- **[Foundational]** M. Grayson. *The heat equation shrinks embedded plane curves to round points.* Journal of Differential Geometry 26 (1987), 285–314.
- **[Foundational]** T. Ilmanen. *Singularities of Mean Curvature Flow of Surfaces.* Preprint, 1995.
- **[Foundational]** B. White. *A local regularity theorem for mean curvature flow.* Annals of Mathematics 161 (2005), 1487–1519.
- **[SOTA]** T. H. Colding, W. P. Minicozzi II. *Generic mean curvature flow I: generic singularities.* Annals of Mathematics 175 (2012), 755–833.
- **[SOTA]** T. H. Colding, W. P. Minicozzi II. *Uniqueness of blowups and Łojasiewicz inequalities.* Annals of Mathematics 182 (2015), 221–285.
- **[SOTA]** S. Brendle. *Embedded self-similar shrinkers of genus 0.* Annals of Mathematics 183 (2016), 715–728.
- **[SOTA]** J. Bernstein, L. Wang. *A sharp lower bound for the entropy of closed hypersurfaces up to dimension six.* Inventiones Mathematicae 206 (2016), 601–627.
- **[SOTA]** K. Choi, R. Haslhofer, O. Hershkovits. *Ancient low entropy flows, mean-convex neighborhoods, and uniqueness.* Acta Mathematica 228 (2022), 217–301.
- **[SOTA]** R. Bamler, B. Kleiner. *On the multiplicity one conjecture for mean curvature flows of surfaces.* arXiv:2312.02106, 2023.
- **[SOTA]** O. Chodosh, K. Choi, C. Mantoulidis, F. Schulze. *Mean curvature flow with generic initial data.* Inventiones Mathematicae 237 (2024), 121–220.
- **[Survey]** C. Mantegazza. *Lecture Notes on Mean Curvature Flow.* Progress in Mathematics 290, Birkhäuser, 2011.
- **[Survey]** T. H. Colding, W. P. Minicozzi II, E. K. Pedersen. *Mean curvature flow.* Bulletin of the AMS 52 (2015), 297–333.
- **[Survey]** R. Haslhofer. *Lectures on curve shortening flow / mean curvature flow.* Lecture notes, University of Toronto.

## 10. Worked Example / Concrete Special Case

**Round sphere.** Take $M_0 = S^n(R_0)\subset\mathbb{R}^{n+1}$. By symmetry $M_t = S^n(R(t))$, with $\nu$ outward and $H = n/R$, so $\dot R = -n/R$, giving
$$R(t) = \sqrt{R_0^2 - 2nt}, \qquad T = \frac{R_0^2}{2n}.$$
Then $|A|^2 = n/R^2 = \frac{1}{2(T-t)}$, saturating Huisken's blowup rate — a Type I singularity. Rescaling: $\frac{1}{\sqrt{2(T-t)}}M_t = S^n(\sqrt{n/2}\cdot\sqrt{2})$… more usefully, $\frac{M_t}{\sqrt{T-t}} = S^n(\sqrt{2n})$ for all $t$, which satisfies $H=\langle x,\nu\rangle/2$ since $H = n/\sqrt{2n}$ and $\langle x,\nu\rangle/2 = \sqrt{2n}/2$; both equal $\sqrt{n/2}$. The tangent flow is the shrinking sphere, and $\Theta = \lambda(S^n)$ ($=4/e\approx1.4715$ for $n=2$).

**Dumbbell (neckpinch).** Let $M_0\subset\mathbb{R}^3$ be a rotationally symmetric surface: two spheres of radius $1$ centred at $(\pm 3,0,0)$ joined by a thin cylindrical neck of radius $r_0 = 0.1$ and length $4$. Writing the profile as $u(x,t)$ (neck radius over the axis), the flow is
$$\partial_t u = \frac{u_{xx}}{1+u_x^2} - \frac{1}{u}.$$
On the neck, $u_x\approx0$, so $\partial_t u \approx -1/u$ and $u(t)\approx\sqrt{r_0^2-2t}$, pinching at $t\approx 0.005$. The bells, of radius $1$, would need $t = 1/4$ to vanish. So the neck closes first, while the surface stays smooth elsewhere: the singularity is *local*.

Blowing up at the pinch point gives the shrinking cylinder $S^1(\sqrt2)\times\mathbb{R}$, with density $\Theta = \lambda(S^1) = \sqrt{2\pi/e}\approx 1.5203 > \lambda(S^2)\approx1.4715$. This is the model generic singularity.

**Where the difficulty is.** Tune the neck: as $r_0$ increases toward the bell radius there is a critical parameter $r_0^\*$ at which the neck and the bells vanish simultaneously. Angenent–Velázquez showed such a *degenerate* neckpinch produces a Type II singularity whose blowup is the translating bowl soliton, not a cylinder. Because that behaviour occurs only on a codimension-$\ge1$ set of parameters, it should disappear under generic perturbation — for $n=2$ this is now a theorem (CCMS 2024), and for $n\ge3$ it remains the open problem.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*