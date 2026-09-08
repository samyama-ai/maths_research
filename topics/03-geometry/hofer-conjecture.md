---
id: 03-geometry/hofer-conjecture
title: "Hofer Conjecture"
topic: 03-geometry
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Hofer Conjecture (Infinite Diameter of the Hofer Metric)

> **Topic:** Algebraic & Differential Geometry · **ID:** `03-geometry/hofer-conjecture` · **Status:** partially-solved (open in general)

## 1. Problem Statement / Conjecture

Let $(M,\omega)$ be a closed connected symplectic manifold and let $\mathrm{Ham}(M,\omega)$ be its group of Hamiltonian diffeomorphisms, equipped with Hofer's bi-invariant metric $d_H$.

**Hofer diameter conjecture.** For every closed symplectic manifold,
$$\mathrm{diam}\big(\mathrm{Ham}(M,\omega),\,d_H\big) \;=\; \sup_{\phi,\psi}\, d_H(\phi,\psi) \;=\; +\infty .$$

Equivalently: the Hofer norm $\|\cdot\|_H$ is unbounded on $\mathrm{Ham}(M,\omega)$.

A complete solution means either (i) a proof valid for all closed $(M,\omega)$, or (ii) an explicit closed symplectic manifold with a uniform bound $\|\phi\|_H \le C$ for all $\phi \in \mathrm{Ham}(M,\omega)$. Note the contrast with $C^0$-type invariants: $\mathrm{Ham}$ is a simple group (Banyaga), so no algebraic obstruction to boundedness exists; unboundedness must come from symplectic rigidity. The conjecture is open in general and proved for large classes of manifolds (Section 4).

## 2. Mathematical Foundations

**Hamiltonian flows.** For $H \in C^\infty(S^1\times M,\mathbb{R})$, the vector field $X_{H_t}$ is defined by $\omega(X_{H_t},\cdot) = -dH_t$. Its time-1 map $\phi_H^1$ lies in $\mathrm{Ham}(M,\omega)$, and every element arises this way.

**Hofer length and norm.** The length of the path $\{\phi^t_H\}$ is
$$\mathrm{length}(\{\phi^t_H\}) = \int_0^1 \mathrm{osc}\,(H_t)\, dt = \int_0^1\Big(\max_{x\in M} H_t(x) - \min_{x\in M} H_t(x)\Big) dt ,$$
and
$$\|\phi\|_H = \inf\{\, \mathrm{length}(\{\phi^t_H\}) \;:\; \phi_H^1 = \phi \,\},\qquad d_H(\phi,\psi) = \|\phi\psi^{-1}\|_H .$$
Symmetry, the triangle inequality and bi-invariance ($\|\theta\phi\theta^{-1}\|_H = \|\phi\|_H$ for $\theta \in \mathrm{Symp}$) are elementary. **Nondegeneracy** ($\|\phi\|_H = 0 \Rightarrow \phi = \mathrm{id}$) is a deep theorem: Hofer (1990) for $\mathbb{R}^{2n}$, Polterovich for tame manifolds, Lalonde–McDuff (1995) in full generality via the energy–capacity inequality
$$e(A) \;\ge\; c(A) \quad\text{for displaceable } A\subset M .$$

**Spectral invariants.** For $\alpha \in QH_*(M)$ nonzero, Hamiltonian Floer theory gives $c(\alpha,H) \in \mathrm{Spec}(H)$ with
$$\int_0^1 \min_M (H_t-K_t)\,dt \;\le\; c(\alpha,H)-c(\alpha,K)\;\le\;\int_0^1 \max_M(H_t-K_t)\,dt ,$$
so $c$ is $1$-Lipschitz for $\|\cdot\|_H$. Homogenization $\mu(\phi) = \mathrm{Vol}(M)\cdot\lim_{n\to\infty} c(\alpha,\phi^n)/n$ produces, when $QH_*(M)$ has a field factor, a **Calabi quasimorphism** $\mu:\widetilde{\mathrm{Ham}}\to\mathbb{R}$: homogeneous, with defect $D(\mu)=\sup|\mu(\phi\psi)-\mu(\phi)-\mu(\psi)|<\infty$, Hofer-Lipschitz, and restricting to the **Calabi homomorphism**
$$\mathrm{Cal}_U(\phi_H^1) = \int_0^1\!\!\int_M H_t\,\omega^n\,dt$$
on Hamiltonians supported in a displaceable open $U$.

**The unboundedness mechanism.** If $\nu$ is any homogeneous quasimorphism that is Lipschitz for $\|\cdot\|_H$ ($|\nu(\phi)|\le C\|\phi\|_H$) and is nonzero somewhere, then $\|\phi^n\|_H \ge |\nu(\phi^n)|/C = n|\nu(\phi)|/C \to \infty$. Every known proof of the conjecture instantiates this scheme, or the weaker one via **boundary depth** $\beta(H)$ (the longest finite bar in the Floer barcode), which is also $\|\cdot\|_H$-Lipschitz but is *not* a quasimorphism.

## 3. History & State of the Art (SOTA)

- **1990.** Hofer introduces the metric in *On the topological properties of symplectic maps* and proves nondegeneracy on $\mathbb{R}^{2n}$; the diameter question is posed there and in Hofer–Zehnder (1994).
- **1995.** Lalonde–McDuff prove nondegeneracy on all symplectic manifolds, making $d_H$ a genuine metric and the diameter question meaningful everywhere.
- **1998.** Polterovich proves infinite diameter for closed surfaces of genus $\ge 1$ using Lagrangian intersections and the fundamental-group action.
- **2000.** Schwarz's action spectrum machinery settles all closed **symplectically aspherical** manifolds ($\omega|_{\pi_2}=0=c_1|_{\pi_2}$).
- **2003.** Entov–Polterovich construct Calabi quasimorphisms from semisimple quantum homology, covering $S^2$, $\mathbb{CP}^n$, and products of these — the first genuinely non-aspherical cases.
- **2011–2013.** Usher's boundary-depth technique gives lower bounds on $\|\cdot\|_H$ without quasimorphisms, extending unboundedness to further classes, including cases with non-semisimple quantum homology *(frontier — verify exact class)*.
- **2021.** Kislev–Shelukhin make the barcode bounds quantitative and uniform for closed monotone manifolds.
- **2020–2024.** Periodic Floer homology spectral invariants (Cristofaro-Gardiner–Humilière–Seyfaddini) give quasimorphisms on $\mathrm{Ham}_c$ of surfaces with boundary, resolving adjacent questions (simplicity conjecture).

No closed symplectic manifold is known, or seriously conjectured, to have bounded Hofer diameter.

## 4. Partial Results / Verified Cases

Infinite Hofer diameter is **proved** for:

1. **All closed symplectically aspherical $(M,\omega)$** — Schwarz (2000). Includes all closed surfaces of genus $\ge 1$, tori $\mathbb{T}^{2n}$, and all closed manifolds with $\pi_2(M)=0$.
2. **$S^2$ and $\mathbb{CP}^n$ for all $n\ge1$**, and finite products $\prod_i \mathbb{CP}^{n_i}$ — Entov–Polterovich (2003), via semisimplicity of $QH_*$.
3. **Closed monotone manifolds whose quantum homology has a field summand** (e.g. many coadjoint orbits, flag manifolds, monotone toric Fanos with semisimple $QH$).
4. **Non-compact / relative cases:** $\mathrm{Ham}_c(\mathbb{R}^{2n},\omega_0)$, $\mathrm{Ham}_c(D^2)$ rel boundary, and $\mathrm{Ham}_c(U)$ for $U$ displaceable in a closed $M$, where $\mathrm{Cal}$ itself is an unbounded Hofer-Lipschitz homomorphism.
5. **Surfaces of any genus, including $S^2$, for the group of area-preserving maps**, with quantitative $n$-fold growth $\|\phi^n\|_H \asymp n$.
6. **Classes reachable by boundary depth** — Usher (2013), including manifolds admitting suitable incompressible or displaceable Lagrangian-type configurations, covering some negative-monotone and non-monotone examples outside 1–3.

Additionally, **stronger structure** is known in these cases: $\mathrm{Ham}$ contains quasi-isometrically embedded copies of $\mathbb{R}^n$ for all $n$ (and of infinite-dimensional normed spaces in several settings), so the diameter is not merely infinite but the geometry is "large".

## 5. Principal Obstacles

- **Every proof needs a Floer-theoretic invariant with a $\|\cdot\|_H$-Lipschitz property.** Ordinary algebraic topology of $\mathrm{Ham}$ (e.g. $\pi_1$, $H^*$) sees nothing of the metric: bi-invariance kills naive length arguments, and $\mathrm{Ham}$ is simple and perfect, so homomorphisms to $\mathbb{R}$ do not exist for closed $M$.
- **Quantum homology need not be semisimple.** The Entov–Polterovich construction requires a field factor in $QH_*(M;\Lambda)$. For a general closed $(M,\omega)$ — e.g. blow-ups, high-genus fibrations, non-monotone symplectic $6$-manifolds — $QH_*$ can be a local ring with nilpotents and the homogenization $\lim c(\alpha,\phi^n)/n$ fails to be a quasimorphism.
- **Novikov-field subtleties.** Nontrivial $\omega|_{\pi_2}$ makes the action functional multivalued; the spectrum $\mathrm{Spec}(H)$ is a $\Gamma$-torsor and can be dense in $\mathbb{R}$, destroying the continuity/locality arguments used in the aspherical case.
- **No lower-bound technique is "local".** Displacement energy bounds only see displaceable subsets; if $M$ has few displaceable open sets relative to its symplectic volume (e.g. after normalizing the class of $\omega$), the Calabi-type input vanishes.
- **Perturbative/geodesic methods are insufficient.** Length-minimizing criteria (Bialy–Polterovich, Oh, McDuff) identify short geodesics but yield only $\|\phi\|_H \ge \mathrm{osc}$-type bounds for special autonomous $\phi$; they do not produce sequences with unbounded norm.
- **Transversality/virtual chains.** For general closed $(M,\omega)$ the relevant Floer packages require virtual techniques (Kuranishi, polyfolds), and the *quantitative* structures (product formulas, quasimorphism defect estimates) are technically harder to establish there than the qualitative ones.

## 6. The Gap

Proven: unboundedness whenever the Floer package supplies either (a) a Calabi quasimorphism (semisimple $QH_*$ factor) or (b) a boundary-depth sequence $\beta(H_k)\to\infty$ with controlled oscillation, plus the aspherical case where $c(\alpha,\cdot)$ behaves like a genuine homomorphism on suitable subgroups.

Missing: a *uniform* construction of an unbounded Hofer-Lipschitz function on $\mathrm{Ham}(M,\omega)$ for arbitrary closed $(M,\omega)$. Precisely, one needs either
$$\exists\,\nu:\widetilde{\mathrm{Ham}}\to\mathbb{R} \text{ homogeneous quasimorphism, } |\nu|\le C\|\cdot\|_H,\ \nu\not\equiv 0,$$
for every closed $(M,\omega)$ (this is itself open, and would follow from semisimplicity-free spectral techniques), or a non-quasimorphism substitute — e.g. showing that the barcode of $\phi^n$ contains a bar of length growing in $n$ for some $\phi$ — valid without hypotheses on $QH_*$. The precise barrier is the passage from *semisimple* to *arbitrary* quantum homology.

## 7. Current Research (as of June 2026)

- **Barcode / persistence methods.** Kislev–Shelukhin-style quantitative bounds on spectral norms and boundary depth are being pushed to non-monotone and virtually-defined settings; the aim is a lower bound on $\|\phi^n\|_H$ that needs no ring-theoretic hypothesis *(frontier — verify)*.
- **Quantitative sheaf theory / microlocal methods.** Guillermou–Viterbo-type sheaf quantization gives Hofer-type bounds without $J$-holomorphic curves; extensions from cotangent bundles to closed manifolds are actively pursued (groups in Paris, Kyoto, Tel Aviv) *(frontier — verify)*.
- **PFH/ECH and surface dynamics.** The Cristofaro-Gardiner–Humilière–Seyfaddini program yields Hofer-continuous quasimorphisms on $\mathrm{Ham}_c(D^2)$ and $\mathrm{Ham}(S^2)$; whether analogues exist in dimension $\ge 4$ is a major question.
- **Deformed/bulk quantum homology.** Fukaya–Oh–Ohta–Ono bulk deformations restore semisimplicity for some manifolds where the undeformed $QH_*$ fails, enlarging the Entov–Polterovich class (toric and toric-degeneration examples).
- **Schools.** Tel Aviv (Polterovich, Shelukhin, Entov at Technion), Michigan State (Usher), IAS/Paris (Humilière, Seyfaddini), Kyoto (Ono, Kawamoto).

## 8. Future Work

- Prove that **boundary depth is unbounded** on $\{\phi^n\}$ for a suitable autonomous $\phi$ on any closed $(M,\omega)$; this would settle the conjecture without quasimorphisms.
- Develop **partial quasimorphisms** (Entov–Polterovich) into a tool that works for local Artinian $QH_*$, using nilpotents rather than field factors.
- Determine whether every closed $(M,\omega)$ has a **displaceable open subset of positive "Calabi capacity"** — a purely geometric statement that would feed the standard mechanism.
- Settle the finer questions: is $\mathrm{Ham}(M,\omega)$ always quasi-isometric to a space containing $\mathbb{R}^\infty$? Is the **Hofer geometry of $\mathrm{Ham}(S^2)$** quasi-isometric to a Banach space (Ostrover's program)?
- Extend to $C^0$-closures: does the Hofer norm extend unboundedly to the group of **hameomorphisms** (Oh–Müller)?

## 9. Key References

- **[Foundational]** H. Hofer. *On the topological properties of symplectic maps.* Proc. Roy. Soc. Edinburgh Sect. A **115** (1990), 25–38. [DOI](https://doi.org/10.1017/s0308210500024549)
- **[Foundational]** H. Hofer, E. Zehnder. *Symplectic Invariants and Hamiltonian Dynamics.* Birkhäuser, 1994. [DOI](https://doi.org/10.1007/978-3-0348-8540-9)
- **[Foundational]** F. Lalonde, D. McDuff. *The geometry of symplectic energy.* Annals of Mathematics **141** (1995), 349–371.
- **[Key result]** L. Polterovich. *Hofer's diameter and Lagrangian intersections.* International Mathematics Research Notices **1998**, no. 4, 217–223.
- **[Key result]** M. Schwarz. *On the action spectrum for closed symplectically aspherical manifolds.* Pacific Journal of Mathematics **193** (2000), 419–461. [DOI](https://doi.org/10.2140/pjm.2000.193.419)
- **[Key result]** M. Entov, L. Polterovich. *Calabi quasimorphism and quantum homology.* International Mathematics Research Notices **2003**, no. 30, 1635–1676.
- **[Key result]** Y. Ostrover. *A comparison of Hofer's metrics on Hamiltonian diffeomorphisms and Lagrangian submanifolds.* Communications in Contemporary Mathematics **5** (2003), 803–811. [DOI](https://doi.org/10.1142/s0219199703001154)
- **[SOTA]** M. Usher. *Hofer's metrics and boundary depth.* Annales Scientifiques de l'École Normale Supérieure **46** (2013), 57–128. [DOI](https://doi.org/10.24033/asens.2185)
- **[SOTA]** A. Kislev, E. Shelukhin. *Bounds on spectral norms and barcodes.* Geometry & Topology **25** (2021), 3257–3350. [DOI](https://doi.org/10.2140/gt.2021.25.3257)
- **[SOTA]** D. Cristofaro-Gardiner, V. Humilière, S. Seyfaddini. *Proof of the simplicity conjecture.* Annals of Mathematics **199** (2024), 181–257. [DOI](https://doi.org/10.4007/annals.2024.199.1.3)
- **[Survey]** L. Polterovich. *The Geometry of the Group of Symplectic Diffeomorphisms.* Lectures in Mathematics ETH Zürich, Birkhäuser, 2001.
- **[Survey]** Y. Ostrover. *When symplectic topology meets Banach space geometry.* Proceedings of the ICM, Seoul, 2014.
- **[Background]** Y.-G. Oh. *Spectral invariants and the length minimizing property of Hamiltonian paths.* Asian Journal of Mathematics **9** (2005), 1–18. [DOI](https://doi.org/10.4310/ajm.2005.v9.n1.a1)

## 10. Worked Example / Concrete Special Case

**Claim.** $\mathrm{diam}(\mathrm{Ham}(S^2,\omega)) = \infty$, with an explicit linearly growing sequence.

Normalize $\int_{S^2}\omega = 1$. By Entov–Polterovich, $QH_*(S^2;\Lambda)\cong \Lambda[u]/(u^2 = q)$ splits as a product of two fields, so the homogenized spectral invariant
$$\mu(\phi) \;=\; \lim_{n\to\infty}\frac{c(e_+,\phi^n)}{n}$$
is a homogeneous quasimorphism on $\widetilde{\mathrm{Ham}}(S^2)$ satisfying $|\mu(\phi)| \le \|\phi\|_H$ and $\mu = \mathrm{Cal}_U$ on Hamiltonians supported in a displaceable $U$.

**Construction.** A disk $D\subset S^2$ of area $a<\tfrac12$ is displaceable (rotate it past the equator). Use the area coordinate $A\in[0,a]$ on $D$ (Darboux: $\omega = dA\wedge d\theta$). Take
$$H(A) = a - A \quad (0\le A\le a), \qquad H \equiv 0 \text{ outside } D,$$
smoothed near $A=a$ so that $H\in C^\infty$. The flow rotates each circle $\{A = \text{const}\}$ at angular speed $-H'(A) = 1$; it is autonomous, supported in $D$.

**Calabi invariant.**
$$\mathrm{Cal}_D(\phi_H) = \int_D H\,\omega = \int_0^a (a-A)\,dA = \frac{a^2}{2}.$$

**Lower bound.** Since $\mu$ is homogeneous and equals $\mathrm{Cal}_D$ here,
$$\|\phi_H^{\,n}\|_H \;\ge\; |\mu(\phi_H^{\,n})| \;=\; n\,|\mu(\phi_H)| \;=\; \frac{n a^2}{2}\ \xrightarrow[n\to\infty]{}\ \infty .$$

**Upper bound (sharpness of the growth rate).** $\phi_H^{\,n} = \phi_{nH}^1$ and $\mathrm{osc}(nH) = na$, so $\|\phi_H^{\,n}\|_H \le n a$. Hence
$$\frac{a^2}{2}\;\le\;\liminf_{n\to\infty}\frac{\|\phi_H^{\,n}\|_H}{n}\;\le\; a,$$
i.e. the Hofer norm grows exactly linearly in $n$, and $d_H(\mathrm{id},\phi_H^{\,n})\to\infty$.

**What breaks in general.** Replace $S^2$ by a closed $(M,\omega)$ whose quantum homology is a local ring with nilpotents: the limit $\lim_n c(\alpha,\phi^n)/n$ still exists but the defect $\sup|\mu(\phi\psi)-\mu(\phi)-\mu(\psi)|$ need not be finite, so $\mu(\phi^n) = n\mu(\phi)$ is unavailable and the chain of inequalities above collapses at its first step. That single failure is the whole content of Section 6.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*