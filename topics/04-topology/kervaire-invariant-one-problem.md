---
id: 04-topology/kervaire-invariant-one-problem
title: "Kervaire Invariant One Problem"
topic: 04-topology
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Kervaire Invariant One Problem

> **Topic:** Topology & Knot Theory · **ID:** `04-topology/kervaire-invariant-one-problem` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

For which $n$ does there exist a smooth closed $n$-manifold with stable framing whose Kervaire invariant equals $1$?

The Kervaire invariant $\Phi$ is a $\mathbb{Z}/2$-valued cobordism invariant defined on framed $(4k+2)$-manifolds. Browder (1969) reduced the question to the dimensions $n = 2^{j+1}-2$ and translated it into stable homotopy theory: an element of Kervaire invariant one exists in dimension $2^{j+1}-2$ if and only if the class
$$h_j^2 \in \mathrm{Ext}_{\mathcal{A}}^{2,\,2^{j+1}}(\mathbb{F}_2,\mathbb{F}_2)$$
is a permanent cycle in the classical Adams spectral sequence for the sphere spectrum. Such a permanent cycle detects an element $\theta_j \in \pi_{2^{j+1}-2}^s(S^0)$.

**Resolution status.** Elements $\theta_j$ exist for $j = 1,\dots,5$ (dimensions $2, 6, 14, 30, 62$). Hill–Hopkins–Ravenel (*Annals*, 2016) proved $\theta_j$ does not exist for $j \ge 7$ (dimensions $\ge 254$). The remaining case $j=6$, dimension $126$, was settled affirmatively by Lin–Wang–Xu (2024–25): $\theta_6$ exists. A complete answer therefore reads: Kervaire invariant one is realized exactly in dimensions $2, 6, 14, 30, 62, 126$.

## 2. Mathematical Foundations

**Arf invariant.** Let $V$ be a finite-dimensional $\mathbb{F}_2$-vector space with a nondegenerate symplectic form $\lambda$ and a quadratic refinement $q: V \to \mathbb{Z}/2$ satisfying
$$q(x+y) = q(x) + q(y) + \lambda(x,y).$$
For a symplectic basis $a_1,b_1,\dots,a_g,b_g$,
$$\mathrm{Arf}(q) = \sum_{i=1}^{g} q(a_i)\, q(b_i) \in \mathbb{Z}/2,$$
independent of the basis. $\mathrm{Arf}(q)=0$ iff $q$ takes value $0$ on a Lagrangian subspace.

**Kervaire invariant.** Let $M^{4k+2}$ be closed, smooth, with stable framing $\varphi$. Set $V = H^{2k+1}(M;\mathbb{F}_2)$ with $\lambda(x,y) = \langle x\smile y,[M]\rangle$. The framing gives a Wu-type refinement $q_\varphi: V \to \mathbb{Z}/2$, defined by embedding a representing sphere $S^{2k+1} \hookrightarrow M^{4k+2}$ and measuring the framing of its normal bundle against the trivialization, i.e. an element of $\pi_{2k+1}(SO/SO_{2k+1}) \cong \mathbb{Z}/2$ for $2k+1 \ne 1,3,7$. Then
$$\Phi(M,\varphi) := \mathrm{Arf}(q_\varphi) \in \mathbb{Z}/2 .$$
$\Phi$ is a framed-cobordism invariant, so by the Pontryagin–Thom isomorphism $\Omega^{fr}_n \cong \pi_n^s(S^0)$ it defines a homomorphism $\Phi: \pi^s_{4k+2}(S^0) \to \mathbb{Z}/2$.

**Browder's theorem (1969).** $\Phi \equiv 0$ unless $4k+2 = 2^{j+1}-2$; and $\Phi \ne 0$ in that dimension iff $h_j^2$ survives the Adams spectral sequence
$$E_2^{s,t} = \mathrm{Ext}^{s,t}_{\mathcal{A}}(\mathbb{F}_2,\mathbb{F}_2) \Longrightarrow \pi_{t-s}^s(S^0)^{\wedge}_2 ,$$
where $\mathcal{A}$ is the mod-2 Steenrod algebra and $h_j \in \mathrm{Ext}^{1,2^j}$ is the Adams class of $Sq^{2^j}$.

**Kervaire–Milnor context.** For $\Theta_n$ the group of homotopy $n$-spheres and $bP_{n+1}$ the subgroup bounding parallelizable manifolds, with $n=4k+2$,
$$bP_{4k+4-2} := bP_{n+1} \cong \begin{cases} 0 & \text{if } \theta \text{ of Kervaire invariant one exists in dim } n,\\ \mathbb{Z}/2 & \text{otherwise.}\end{cases}$$

**HHR detecting spectrum.** Hill–Hopkins–Ravenel construct
$$\Omega = \left(N_{C_2}^{C_8} MU_{\mathbb{R}}\right)^{hC_8},$$
the homotopy fixed points of the $C_8$-norm of real bordism, and prove three properties: (i) *Detection* — if $\theta_j$ exists for $j\ge 7$, its image in $\pi_*\Omega$ is nonzero; (ii) *Gap* — $\pi_{-i}\Omega = 0$ for $0 < i < 4$; (iii) *Periodicity* — $\pi_*\Omega \cong \pi_{*+256}\Omega$. Since $2^{j+1}-2 \equiv -2 \pmod{256}$ for $j\ge 7$, Detection would place a nonzero class in $\pi_{-2}\Omega = 0$.

## 3. History & State of the Art (SOTA)

- **1960.** Kervaire constructs a closed PL $10$-manifold admitting no smooth structure, using the vanishing of $\Phi$ in dimension $10$.
- **1963.** Kervaire–Milnor, *Groups of homotopy spheres I*, tie $bP_{n+1}$ and the classification of exotic spheres to the Kervaire invariant.
- **1969.** Browder proves the $2^{j+1}-2$ restriction and the $h_j^2$ criterion — the definitive reformulation.
- **1967–1984.** Mahowald–Tangora ($\theta_4$, dimension 30, via Adams differentials), Barratt–Mahowald, and Barratt–Jones–Mahowald ($\theta_5$, dimension 62) give the existence results.
- **2009–2016.** Hill–Hopkins–Ravenel announce (2009) and publish (*Annals* 184, 2016) the nonexistence for $j \ge 7$, introducing equivariant slice filtration methods.
- **2016.** Xu gives an independent verification of the strong Kervaire problem in dimension 62.
- **2023.** Isaksen–Wang–Xu compute $\pi_n^s$ for $n \le 90$, establishing the machinery (motivic deformations, Chow $t$-structure, machine-assisted $\mathrm{Ext}$ charts) later applied at $n=126$.
- **2024–25.** Lin–Wang–Xu, *On the last Kervaire invariant problem*, prove $h_6^2$ is a permanent cycle: $\theta_6 \in \pi_{126}^s$ exists.

## 4. Partial Results / Verified Cases

| $j$ | Dimension $2^{j+1}-2$ | $\theta_j$ | Source |
|---|---|---|---|
| 1 | 2 | $\eta^2$ | Classical (Pontryagin); $T^2$ Lie-framed |
| 2 | 6 | $\nu^2$ | Classical |
| 3 | 14 | $\sigma^2$ | Classical |
| 4 | 30 | exists | Barratt–Mahowald; Mahowald–Tangora differentials |
| 5 | 62 | exists | Barratt–Jones–Mahowald (1984); Xu (2016) |
| 6 | 126 | exists | Lin–Wang–Xu (2024–25) |
| $\ge 7$ | $\ge 254$ | **does not exist** | Hill–Hopkins–Ravenel (2016) |

Additional verified structure: Browder's theorem eliminates all $n \not\equiv -2 \bmod$ powers of two outright, i.e. $\Phi = 0$ on $\pi_n^s$ for every $n=4k+2$ other than $2,6,14,30,62,126,254,\dots$. Consequently $bP_{n+1} = 0$ for $n \in \{2,6,14,30,62,126\}$ and $bP_{n+1} \cong \mathbb{Z}/2$ for all other $n \equiv 2 \bmod 4$. The "strong" form (whether $\theta_j$ can be chosen with $\theta_j = \theta_{j-1}^2$, i.e. $\theta_{j-1}^2 \ne 0$) is known to fail at $j=6$: $\theta_5^2 = 0$ in $\pi_{124}^s$, so $\theta_6$ is not a square. *(frontier — verify)*

## 5. Principal Obstacles

- **Adams spectral sequence unreachability.** Deciding whether $h_j^2$ survives requires knowing all differentials $d_r(h_j^2)$ into $\mathrm{Ext}^{2+r,\,2^{j+1}+r-1}$ in a stem of size $2^{j+1}-2$. Direct machine computation of $\mathrm{Ext}_{\mathcal{A}}$ scales badly: charts through stem 90 already require months of computation; stem 126 is far past the reach of naive minimal-resolution algorithms.
- **No small detecting spectrum for finitely many $j$.** HHR's argument is uniformly asymptotic. The periodicity is $256 = 2^8$, so it can only exclude $2^{j+1}-2 \equiv -2 \pmod{256}$, i.e. $j \ge 7$. Dimension $126 \equiv 126 \pmod{256}$ is invisible to $\Omega$; no analogous $C_4$ or $C_8$ construction with a smaller period and a gap has been found.
- **Failure of classical Adams-tower techniques at $j=6$.** The Barratt–Jones–Mahowald method uses $\theta_{j-1}$-squaring and Hopf-invariant relations; it stalls because $\theta_5^2$ vanishes, so no "square root" input is available.
- **Ambiguity of hidden extensions.** Even with $E_\infty$ known, translating $E_\infty$ classes into elements of $\pi_*^s$ requires resolving hidden $2$-, $\eta$-, $\nu$-extensions — the step where the geometric statement lives.
- **Geometry gives nothing directly.** No explicit framed $126$-manifold with $\Phi=1$ is known; the existence proof is purely homotopy-theoretic, so surgery-theoretic constructions do not supply candidates.

## 6. The Gap

Before 2024 the gap was a single integer. Nonexistence was proved for $j\ge 7$ by the Gap Theorem, existence for $j\le 5$ by explicit constructions; $j=6$ sat between two methods, each structurally incapable of reaching it. Closing it required computing the Adams (equivalently, $\mathbb{C}$-motivic Adams) spectral sequence in stems $125$–$127$ at the prime $2$ and proving that every potential differential on $h_6^2$ vanishes.

Residual gaps after the resolution: (a) no explicit geometric model of a framed $126$-manifold with Kervaire invariant one; (b) the *strong* Kervaire problem, i.e. the multiplicative structure of the $\theta_j$'s, is not fully understood; (c) the analogous odd-primary problem — whether $\beta_1^p$ (Ravenel's classes) is a permanent cycle — is open for $p=3,5$ in general.

## 7. Current Research (as of June 2026)

- **Lin–Wang–Xu program** (Chinese Academy of Sciences / Copenhagen; UCLA). The 2024 preprint *On the last Kervaire invariant problem* combines the $\mathbb{C}$-motivic deformation $\mathbb{S}/\tau$, the Chow $t$-structure, and a large machine-verified $\mathrm{Ext}$ computation over the Steenrod algebra; the argument is a Rust/C++-assisted resolution plus by-hand differential analysis. Peer review and independent verification of the computer component are ongoing. *(frontier — verify)*
- **Formal verification.** Efforts to certify the minimal-resolution and $d_r$ bookkeeping in Lean/`Mathlib` and via Isaksen–Bruner's `ext` software are underway. *(frontier — verify)*
- **Equivariant methods after HHR.** Hill, Hopkins, Ravenel and collaborators continue slice-filtration computations of $\pi_* (N_{C_2}^{C_{2^n}} MU_{\mathbb{R}})^{hC_{2^n}}$, with applications to $\mathrm{tmf}$-analogues and Real bordism at odd primes.
- **Odd primes.** Work on Ravenel's $\beta$-family and the odd-primary Kervaire classes continues (Ravenel proved nonexistence for $p\ge 5$, $j\ge 2$, in 1978); $p=3$ remains partly open.

## 8. Future Work

- Produce an explicit framed $126$-manifold, or a surgery-theoretic construction, realizing $\Phi = 1$.
- Reduce the computer-assisted portion of the $126$-proof to a human-checkable argument, ideally via an equivariant or motivic detecting spectrum tailored to period $128$.
- Settle the multiplicative/strong Kervaire structure: which products $\theta_i\theta_j$ are nonzero, and what the $\theta_j$ generate in $\pi_*^s$.
- Extend HHR-style norm-and-gap arguments to odd primes to finish the $p=3$ Kervaire-type problem.
- Push stable stem computations past dimension 100 systematically, using motivic and synthetic spectra, to make dimension-126-scale questions routine.

## 9. Key References

- **[Foundational]** M. Kervaire. *A manifold which does not admit any differentiable structure.* Commentarii Mathematici Helvetici 34 (1960), 257–270. [DOI](https://doi.org/10.1007/bf02565940)
- **[Foundational]** M. Kervaire, J. Milnor. *Groups of homotopy spheres: I.* Annals of Mathematics 77 (1963), 504–537.
- **[Foundational]** W. Browder. *The Kervaire invariant of framed manifolds and its generalization.* Annals of Mathematics 90 (1969), 157–186. [DOI](https://doi.org/10.2307/1970686)
- **[Foundational]** M. Mahowald, M. Tangora. *Some differentials in the Adams spectral sequence.* Topology 6 (1967), 349–369. [DOI](https://doi.org/10.1016/0040-9383(67)90023-7)
- **[Foundational]** M. G. Barratt, J. D. S. Jones, M. E. Mahowald. *Relating the Kervaire invariant and the Hopf invariant.* Algebraic Topology, Aarhus 1982, Lecture Notes in Mathematics 1051, Springer, 1984.
- **[SOTA]** M. A. Hill, M. J. Hopkins, D. C. Ravenel. *On the nonexistence of elements of Kervaire invariant one.* Annals of Mathematics 184 (2016), 1–262. [DOI](https://doi.org/10.4007/annals.2016.184.1.1)
- **[SOTA]** M. A. Hill, M. J. Hopkins, D. C. Ravenel. *Equivariant Stable Homotopy Theory and the Kervaire Invariant Problem.* New Mathematical Monographs 40, Cambridge University Press, 2021.
- **[SOTA / Recent]** Z. Xu. *The strong Kervaire invariant problem in dimension 62.* Geometry & Topology 20 (2016), 1611–1624. [DOI](https://doi.org/10.2140/gt.2016.20.1611)
- **[SOTA / Recent]** D. C. Isaksen, G. Wang, Z. Xu. *Stable homotopy groups of spheres: from dimension 0 to 90.* Publications mathématiques de l'IHÉS 137 (2023), 107–243. [DOI](https://doi.org/10.1007/s10240-023-00139-1)
- **[SOTA / Recent]** W. Lin, G. Wang, Z. Xu. *On the last Kervaire invariant problem.* arXiv:2412.10879, 2024.
- **[Survey]** H. Miller. *Kervaire invariant one (after M. A. Hill, M. J. Hopkins, and D. C. Ravenel).* Séminaire Bourbaki, exp. 1029, Astérisque 348 (2012), 65–98.
- **[Survey]** V. Snaith. *Stable Homotopy Around the Arf–Kervaire Invariant.* Progress in Mathematics 273, Birkhäuser, 2009. [DOI](https://doi.org/10.1007/978-3-7643-9904-7)

## 10. Worked Example / Concrete Special Case

**Dimension 2: the Lie-framed torus has Kervaire invariant one.**

Take $M = T^2 = S^1 \times S^1$ with the framing $\varphi$ coming from the Lie group structure (left-invariant vector fields), and $k=0$, so $4k+2 = 2$ and the middle cohomology is $V = H^1(T^2;\mathbb{F}_2) \cong \mathbb{F}_2\{a,b\}$.

1. **Symplectic form.** $\lambda(a,b) = \langle a \smile b, [T^2]\rangle = 1$, $\lambda(a,a)=\lambda(b,b)=0$. So $(a,b)$ is a symplectic basis, $g=1$.
2. **Quadratic refinement.** Each generator is represented by an embedded circle $S^1 \subset T^2$ with trivial normal bundle. $q_\varphi(x)$ records whether the Lie framing restricted to that circle extends over a disc, i.e. the class in $\pi_1(SO/SO_1)\cong\pi_1(SO)\cong\mathbb{Z}/2$. The Lie framing on each factor circle is the *nonbounding* framing (the one generating $\Omega_1^{fr}\cong\mathbb{Z}/2$, corresponding to $\eta$). Hence
$$q_\varphi(a) = 1, \qquad q_\varphi(b) = 1 .$$
3. **Arf invariant.**
$$\Phi(T^2,\varphi) = \mathrm{Arf}(q_\varphi) = q_\varphi(a)\,q_\varphi(b) = 1\cdot 1 = 1 .$$

So $\theta_1 = [T^2,\varphi] = \eta^2 \ne 0$ in $\pi_2^s(S^0)\cong\mathbb{Z}/2$, matching the Adams picture: $h_1^2 \in \mathrm{Ext}^{2,4}_{\mathcal{A}}$ is a permanent cycle detecting $\eta^2$.

**Contrast, dimension 10.** Here $10 = 4\cdot 2 + 2$ but $10 \ne 2^{j+1}-2$ for any $j$ (the nearest values are $6$ and $14$). Browder's theorem forces $\Phi \equiv 0$ on $\pi_{10}^s$. Hence $bP_{12} \cong \mathbb{Z}/2$, and Kervaire's original $10$-manifold — built by plumbing two copies of the tangent disc bundle of $S^5$ and coning off the boundary homotopy $9$-sphere — carries a PL structure but no smooth one: any smoothing would give a framed $10$-manifold with $\Phi = 1$, contradicting the vanishing.

**Scaling up.** The same computation at $j=6$ would need $\mathrm{Arf}$ on $H^{63}(M^{126};\mathbb{F}_2)$ for an unknown manifold; instead Lin–Wang–Xu work entirely in the Adams $E_2$-page, ruling out $d_r(h_6^2)$ for all $r \ge 2$ by showing the target groups $\mathrm{Ext}^{2+r,\,128+r-1}_{\mathcal{A}}$ contain no class that can receive the differential.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*