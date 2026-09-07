---
id: 04-topology/smales-paradox
title: "Smale's Paradox"
topic: 04-topology
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Smale's Paradox (Sphere Eversion)

> **Topic:** Topology & Knot Theory · **ID:** `04-topology/smales-paradox` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

**Statement.** Let $f_0 : S^2 \to \mathbb{R}^3$ be the standard inclusion and $f_1 = -f_0$ its composition with the antipodal map of $\mathbb{R}^3$ (the "inside-out" sphere). Smale's paradox is the assertion that there exists a smooth homotopy
$$F : S^2 \times [0,1] \to \mathbb{R}^3, \qquad F(\cdot,0)=f_0,\quad F(\cdot,1)=f_1,$$
such that every intermediate map $f_t = F(\cdot,t)$ is an **immersion**: $df_t$ has rank $2$ at every point. Self-intersections are permitted at all times; creases, corners, and pinch points are not.

The result is a theorem, not an open conjecture: it follows from Smale's 1957 classification of immersions of $S^2$ in $\mathbb{R}^3$. It is called a paradox because the conclusion contradicts strong geometric intuition and because Smale's proof is a pure obstruction computation that exhibits no eversion. The residual research problems are (i) constructing explicit, low-complexity, or geometrically optimal eversions, (ii) determining the minimal invariants any eversion must realise, and (iii) machine-verifiable proof.

**What counts as a resolution of the remaining questions.** For the optimality problems, a resolution means a proof that a stated lower bound (number of quadruple points, number of topological events, maximum Willmore energy) is attained by an explicit regular homotopy and cannot be beaten.

## 2. Mathematical Foundations

Let $M^n$ be a smooth manifold and $\mathrm{Imm}(M,\mathbb{R}^q)$ the space of immersions with the $C^\infty$ topology. A **regular homotopy** is a path in this space. Immersions $f_0, f_1$ are regularly homotopic iff they lie in the same path component.

**Smale–Hirsch theorem.** For $q > n$ the differential map
$$d : \mathrm{Imm}(M^n,\mathbb{R}^q) \longrightarrow \mathrm{Mon}(TM, T\mathbb{R}^q)$$
into the space of fibrewise-injective bundle maps is a weak homotopy equivalence. This is the archetypal **h-principle**: a differential-topological problem reduces to a homotopy-theoretic one.

For $M=S^n$, $q=n+1$, the space of monomorphisms $T S^n \to \mathbb{R}^{n+1}$ deformation retracts to maps into the Stiefel manifold $V_{n+1,n} \cong SO(n+1)$, so
$$\pi_0\,\mathrm{Imm}(S^n,\mathbb{R}^{n+1}) \;\cong\; \pi_n\big(V_{n+1,n}\big) \;\cong\; \pi_n\big(SO(n+1)\big)\big/\!\sim,$$
the quotient identifying classes under the action of $\pi_0$-symmetries. For $n=2$:
$$\pi_2(SO(3)) = \pi_2(\mathbb{RP}^3) = \pi_2(S^3) = 0 .$$
Hence $\mathrm{Imm}(S^2,\mathbb{R}^3)$ is connected and *every* immersion of $S^2$ in $\mathbb{R}^3$ is regularly homotopic to every other — in particular $f_0 \simeq -f_0$.

Contrast $n=1$: $V_{2,1}\cong S^1$, $\pi_1(S^1)=\mathbb{Z}$, giving the **Whitney–Graustein theorem** — regular homotopy classes of immersed circles in $\mathbb{R}^2$ are classified by the turning number
$$\mathrm{tn}(\gamma)=\frac{1}{2\pi}\oint_\gamma \kappa\,ds \in \mathbb{Z}.$$

In general the obstruction to everting $S^n \subset \mathbb{R}^{n+1}$ is the class of the antipodal map in $\pi_n(SO(n+1))$; it vanishes exactly for $n \in \{0,2,6\}$, tied to the parallelisability of $S^1,S^3,S^7$ (Bott–Milnor, Adams).

**Generic eversions.** For a generic regular homotopy the image is stratified by double curves, triple points, and isolated quadruple points, with codimension-one *topological events* in time: births/deaths of double curves, triple-point passages, quadruple points, and Whitney-umbrella (pinch) crossings of the double-point set.

**Willmore energy.** For an immersed surface $f$ with mean curvature $H$,
$$\mathcal{W}(f)=\int_{S^2} H^2\, dA, \qquad \mathcal{W}(\text{round sphere})=4\pi .$$
Bryant's theorem: Willmore spheres have $\mathcal{W}=4\pi k$, $k\in\mathbb{Z}_{\ge 1}$, $k\ne 2,3$.

## 3. History & State of the Art (SOTA)

- **1957–59.** Stephen Smale, then a graduate student of Raoul Bott, proved the classification of immersions of $S^2$; Bott initially believed the eversion corollary was false. Published as *A classification of immersions of the two-sphere*, Trans. AMS **90** (1959).
- **1959.** Morris Hirsch generalised to arbitrary manifolds (*Immersions of manifolds*, Trans. AMS **93**).
- **c. 1960.** Arnold Shapiro described the first (unpublished) explicit eversion, routed through Boy's surface, an immersed $\mathbb{RP}^2$ in $\mathbb{R}^3$.
- **1966.** Anthony Phillips popularised a visualisable eversion in *Scientific American* ("Turning a surface inside out").
- **1967–78.** Bernard Morin and collaborators (Froissart, Petit, Apéry) produced the *Morin eversion*, built around a halfway model with a $\mathbb{Z}/4$ symmetry; Charles Pugh built wire models; Nelson Max produced the first computer animation (1977).
- **1973–74.** Gromov's convex integration and Thurston's corrugation technique gave general machinery from which eversion falls out; Thurston's version was rendered in the film *Outside In* (Levy–Maxwell–Munzner, 1994).
- **1981.** Banchoff–Max: every generic sphere eversion has a quadruple point (in fact an odd number).
- **1995–98.** Kusner's minimax eversion — a gradient flow of Willmore energy through a halfway model of energy $16\pi$ — computed by Francis, Sullivan, Brakke et al. and rendered as *The Optiverse*.
- **2019.** Bednorz–Bednorz gave an eversion built entirely from ruled surfaces with closed-form analytic parametrisation.
- **2023.** Massot, van Doorn and Nash formalised the $h$-principle for ample differential relations in Lean/mathlib and derived a machine-checked sphere eversion — the sense in which this entry is tagged *solved-recently*.

## 4. Partial Results / Verified Cases

- **Dimension $n=2$, codimension 1.** Fully solved: eversion exists (Smale 1959), with explicit constructions in at least five families — Shapiro–Phillips, Morin/Froissart, Thurston corrugations, Kusner minimax, Bednorz ruled.
- **Other $n$.** $S^n \subset \mathbb{R}^{n+1}$ is evertible precisely for $n=0,2,6$; for all other $n$ the antipodal class in $\pi_n(SO(n+1))$ is nontrivial and eversion is impossible. $n=1$ is the sharpest obstruction: turning number $+1 \ne -1$.
- **High codimension.** $S^n \to \mathbb{R}^q$ with $q \ge n+2$: $\pi_n(V_{q,n}) = 0$ in this range for the relevant cases, so eversion is unobstructed and routine.
- **Quadruple points.** Banchoff–Max (1981): the count is odd, hence $\ge 1$; realised by the Morin eversion, which has exactly one. Nowik (2000) extended quadruple-point parity to regular homotopies of surfaces in general $3$-manifolds.
- **Topological events.** Francis–Morin conjectured $14$ as the minimum for a generic eversion; Hughes and Aitchison analysed minimal-event families. Lower bounds below $14$ remain unproven.
- **Energy.** The minimax eversion attains maximum Willmore energy exactly $16\pi$; no eversion with maximum energy $<16\pi$ is known.
- **Formal verification.** The Lean proof covers the full Smale–Hirsch chain via convex integration, for $S^2 \subset \mathbb{R}^3$.

## 5. Principal Obstacles

- **Non-constructive $h$-principle.** Smale's argument is a homotopy-group computation; it certifies a path in $\mathrm{Imm}(S^2,\mathbb{R}^3)$ without producing one. Convex integration is constructive in principle but the iterated high-frequency corrugations blow up derivative bounds, producing surfaces with curvature far beyond anything renderable or minimal.
- **No handle on optimality.** Regular homotopy is a $\pi_0$-invariant; it says nothing about the *length*, *complexity* or *energy* of a path. Algebraic topology detects components, not metrics on them, so no cohomological invariant is known that bounds the number of topological events from below.
- **Singularity theory scales badly.** Counting events means classifying codimension-one degeneracies of a $1$-parameter family of maps $S^2\to\mathbb{R}^3$; the double-point set is a curve in $S^2$ whose evolution has no finite normal-form list once event counts grow.
- **Willmore flow is not a proof technique.** Kusner's $16\pi$ bound rests on a minimax over paths; establishing that the minimax value equals $16\pi$ requires a Palais–Smale condition for $\mathcal{W}$ on immersions that is known to fail (energy concentrates and bubbles off spheres in multiples of $4\pi$).
- **Verification cost.** Even the Lean formalisation required roughly a year of work and bespoke API for corrugations; extending it to explicit optimal eversions is out of reach with present tooling.

## 6. The Gap

Existence is closed. The gap is quantitative. Precisely:

1. **Event minimality.** Proven: $\ge 1$ quadruple point (Banchoff–Max). Constructed: eversions with $14$ topological events. Missing: any proof that $13$ or fewer is impossible. No invariant currently separates event counts.
2. **Energy minimality.** Proven: an eversion exists with $\max_t \mathcal{W}(f_t)=16\pi$. Missing: a proof that every eversion satisfies $\max_t \mathcal{W}(f_t) \ge 16\pi$ (Kusner's conjecture). The barrier is compactness failure for the Willmore functional on non-embedded spheres.
3. **Effective bounds from $h$-principle.** Missing: a version of convex integration whose output carries explicit $C^2$ bounds, which would connect the abstract theorem to the geometric optimisation problems.

## 7. Current Research (as of June 2026)

- **Formalisation.** The Lean `sphere-eversion` project (Massot, van Doorn, Nash) is being extended toward general ample relations and to open manifolds in mathlib. *(frontier — verify)*
- **Quantitative convex integration.** Groups working on Nash–Kuiper regularity and Onsager-type problems (De Lellis, Székelyhidi, Isett school) supply techniques for controlled corrugation that have not yet been imported into the eversion setting.
- **Willmore analysis.** Rivière, Kuwert–Schätzle and Marques–Neves-style minimax methods continue to sharpen sphere-eversion energy estimates; the $16\pi$ conjecture is the standing target. *(frontier — verify)*
- **Visualisation and geometry processing.** Discrete-differential-geometry groups (Illinois, Berlin, CMU) use eversions as benchmarks for regular-homotopy-preserving mesh flows.
- **Singularity theory.** Continued work on quadruple-point and triple-point invariants for immersed surfaces in $3$-manifolds, following Nowik and Goryunov.

## 8. Future Work

- Define a numerical invariant of a regular homotopy class of *paths* (not maps) that bounds event count from below — the analogue for paths of the turning number for loops.
- Prove a compactness/bubbling dichotomy for the Willmore minimax over eversion paths, isolating the $4\pi k$ energy quantisation to force $16\pi$.
- Extract explicit curvature bounds from convex integration; compare against the $16\pi$ minimax surface.
- Push formal verification from existence to a verified explicit parametrised eversion, e.g. the Bednorz ruled construction, whose closed form is amenable to symbolic checking.
- Settle the Francis–Morin $14$-event question, at minimum by exhaustive classification of eversions with $\le 13$ events.

## 9. Key References

- **[Foundational]** Stephen Smale. *A classification of immersions of the two-sphere.* Transactions of the American Mathematical Society **90** (1959), 281–290.
- **[Foundational]** Morris W. Hirsch. *Immersions of manifolds.* Transactions of the American Mathematical Society **93** (1959), 242–276.
- **[Foundational]** Hassler Whitney. *On regular closed curves in the plane.* Compositio Mathematica **4** (1937), 276–284.
- **[Foundational]** Mikhael Gromov. *Partial Differential Relations.* Springer, Ergebnisse der Mathematik, 1986.
- **[Structural]** Nelson Max and Tom Banchoff. *Every sphere eversion has a quadruple point.* In *Contributions to Analysis and Geometry*, Johns Hopkins University Press, 1981, 191–209.
- **[Structural]** Tahl Nowik. *Quadruple points of regular homotopies of surfaces in 3-manifolds.* Topology **39** (2000), 1069–1088.
- **[SOTA]** George Francis, John M. Sullivan, Rob Kusner, Ken Brakke, Chris Hartman, Glenn Chappell. *The minimax sphere eversion.* In *Visualization and Mathematics*, Springer, 1997, 3–20.
- **[SOTA]** Adam Bednorz and Witold Bednorz. *Analytic sphere eversion using ruled surfaces.* Differential Geometry and its Applications **64** (2019), 59–79.
- **[SOTA]** Patrick Massot, Floris van Doorn, Oliver Nash. *Formalising the h-principle and sphere eversion.* Proceedings of CPP 2023 (ACM), 2023.
- **[Survey]** Y. Eliashberg and N. Mishachev. *Introduction to the h-Principle.* Graduate Studies in Mathematics 48, American Mathematical Society, 2002.
- **[Survey]** George K. Francis. *A Topological Picturebook.* Springer, 1987.
- **[Expository]** Anthony Phillips. *Turning a surface inside out.* Scientific American **214** (May 1966), 112–120.
- **[Related]** Robert Bryant. *A duality theorem for Willmore surfaces.* Journal of Differential Geometry **20** (1984), 23–53.

## 10. Worked Example / Concrete Special Case

**The one-dimensional case: why the circle cannot be everted.**

This is the computation that makes Smale's theorem feel paradoxical, because the analogous statement one dimension down is *false*, and provably so.

Let $\gamma : S^1 \to \mathbb{R}^2$ be an immersion, i.e. $\gamma'(\theta)\neq 0$ for all $\theta$. Define the unit tangent (Gauss) map
$$T:S^1 \to S^1, \qquad T(\theta)=\frac{\gamma'(\theta)}{\|\gamma'(\theta)\|}.$$
The **turning number** is $\mathrm{tn}(\gamma) := \deg(T) \in \mathbb{Z}$.

*Invariance.* If $\gamma_s$ is a regular homotopy, then $T_s$ is a continuous family of maps $S^1\to S^1$, and degree is a homotopy invariant of maps between circles, so $s\mapsto \mathrm{tn}(\gamma_s)$ is a continuous integer-valued function, hence constant.

*Computation for the two candidates.* Take the standard circle
$$\gamma_0(\theta)=(\cos\theta,\sin\theta),\quad \gamma_0'(\theta)=(-\sin\theta,\cos\theta),\quad T_0(\theta)=\theta+\tfrac{\pi}{2},$$
so $\deg T_0 = +1$. Its reverse-orientation "everted" version is $\gamma_1(\theta)=(\cos\theta,-\sin\theta)$, with $\gamma_1'(\theta)=(-\sin\theta,-\cos\theta)$, giving $T_1(\theta) = -\theta - \tfrac{\pi}{2}$ and $\deg T_1 = -1$.

Equivalently, by the total-curvature formula, $\mathrm{tn} = \frac{1}{2\pi}\oint \kappa\, ds = \frac{1}{2\pi}(2\pi) = 1$ versus $-1$.

Since $+1 \neq -1$, **no regular homotopy turns a circle inside out in the plane.** A figure-eight immersion, by contrast, has $T$ of degree $0$ and is regularly homotopic to its own reverse.

*The jump to $n=2$.* The identical scheme in one dimension higher replaces $\deg : \pi_1(S^1)=\mathbb{Z}$ with the obstruction group $\pi_2(SO(3))$. Because $SO(3)\cong\mathbb{RP}^3$ is covered by $S^3$ and $\pi_2(S^3)=0$, we get
$$\pi_2(SO(3)) \cong \pi_2(S^3) = 0,$$
so the invariant that blocked eversion of the circle simply does not exist for the sphere. Every immersion of $S^2$ in $\mathbb{R}^3$ — the round sphere, the inside-out sphere, any crumpled self-intersecting variant — sits in one single path component. The paradox is exactly the collapse of a $\mathbb{Z}$-valued obstruction to the trivial group.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*