---
id: 04-topology/hofers-conjecture
title: "Hofer's Conjecture"
topic: 04-topology
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Hofer's Conjecture

> **Topic:** Topology & Knot Theory · **ID:** `04-topology/hofers-conjecture` · **Status:** partially-solved (open in general)

## 1. Problem Statement / Conjecture

**Hofer's conjecture (the Hofer diameter conjecture).** For every closed connected symplectic manifold $(M,\omega)$, the group $\mathrm{Ham}(M,\omega)$ of Hamiltonian diffeomorphisms has infinite diameter with respect to the Hofer metric:

$$\mathrm{diam}\big(\mathrm{Ham}(M,\omega),\, d_H\big) \;=\; \sup_{\varphi,\psi}\, d_H(\varphi,\psi) \;=\; +\infty .$$

Equivalently: the Hofer norm $\|\cdot\|_H$ is an unbounded function on $\mathrm{Ham}(M,\omega)$.

A proof must exhibit, for each closed $(M,\omega)$, a sequence $\varphi_n \in \mathrm{Ham}(M,\omega)$ with $\|\varphi_n\|_H \to \infty$ — in practice, a Hofer-continuous unbounded functional (spectral invariant, quasimorphism, or filtered-Floer quantity). A disproof requires a single closed $(M,\omega)$ with $\sup_\varphi\|\varphi\|_H<\infty$, i.e. a uniform constant $C$ such that every Hamiltonian isotopy can be regenerated with total oscillation $\le C$.

The name "Hofer's conjecture" is also used for the distinct **Hofer–Zehnder conjecture** on periodic points (a Hamiltonian diffeomorphism with more than the homologically minimal number of fixed points has infinitely many periodic points); that problem is discussed in §3 and §7 but is not the subject of this page.

## 2. Mathematical Foundations

Let $(M,\omega)$ be a closed symplectic manifold, $\dim M = 2n$. A smooth $H \colon [0,1]\times M \to \mathbb{R}$ defines the time-dependent vector field $X_{H_t}$ by
$$\iota_{X_{H_t}}\omega = -\,dH_t ,$$
whose time-1 map $\varphi_H^1$ is a *Hamiltonian diffeomorphism*. These form the group $\mathrm{Ham}(M,\omega)$, a normal subgroup of $\mathrm{Symp}_0(M,\omega)$, which is simple for closed $M$ (Banyaga).

**Hofer norm.** With the oscillation
$$\|H\| \;=\; \int_0^1 \Big( \max_{x\in M} H_t(x) - \min_{x\in M} H_t(x)\Big)\, dt ,$$
set
$$\|\varphi\|_H \;=\; \inf\{\, \|H\| \;:\; \varphi_H^1=\varphi \,\}, \qquad d_H(\varphi,\psi)=\|\varphi\psi^{-1}\|_H .$$
$d_H$ is bi-invariant, symmetric, satisfies the triangle inequality, and — the hard part — is **nondegenerate**: $\|\varphi\|_H=0 \Rightarrow \varphi=\mathrm{id}$ (Hofer 1990 for $\mathbb{R}^{2n}$; Polterovich 1993 for rational/tame $M$; Lalonde–McDuff 1995 in full generality).

**Displacement energy.** For $U\subset M$ open,
$$e(U)=\inf\{\|\varphi\|_H : \varphi(U)\cap U=\emptyset\}.$$
The energy–capacity inequality $c(U)\le e(U)$ ties $d_H$ to symplectic capacities.

**Spectral invariants.** For $\tilde\varphi \in \widetilde{\mathrm{Ham}}$ and $a\in QH_*(M)$, filtered Hamiltonian Floer homology yields $c(a,\tilde\varphi)\in\mathbb{R}$, with the *spectral norm*
$$\gamma(\varphi)=c([M],\tilde\varphi)+c([M],\tilde\varphi^{-1}) \le \|\varphi\|_H .$$
**Calabi quasimorphisms.** A homogeneous quasimorphism $\mu\colon \widetilde{\mathrm{Ham}}\to\mathbb{R}$ ($|\mu(fg)-\mu(f)-\mu(g)|\le D$, $\mu(f^n)=n\mu(f)$) that is Hofer-Lipschitz, $|\mu(\varphi)|\le C\|\varphi\|_H$, forces $\|\varphi^n\|_H \ge n|\mu(\varphi)|/C$ — immediate infinite diameter whenever $\mu\not\equiv 0$.
**Boundary depth.** $\beta(H)$ = the largest length of a finite bar in the Floer barcode of $H$; $\beta$ is Hofer-Lipschitz and is the second main unboundedness detector (Usher).

## 3. History & State of the Art (SOTA)

- **1990.** Hofer introduces $d_H$ in *On the topological properties of symplectic maps* and proves nondegeneracy on $\mathbb{R}^{2n}$, with $e(B^{2n}(r))=\pi r^2$; the compactly supported group $\mathrm{Ham}_c(\mathbb{R}^{2n})$ has infinite diameter immediately.
- **1993–95.** Polterovich, then Lalonde–McDuff (*The geometry of symplectic energy*, Annals 141), establish nondegeneracy for all symplectic manifolds; Bialy–Polterovich analyse geodesics and length-minimising paths.
- **1997–2000.** Schwarz constructs spectral invariants for symplectically aspherical $M$ and deduces infinite Hofer diameter there — the first large closed-manifold class.
- **2003.** Entov–Polterovich build Calabi quasimorphisms from the quantum homology of monotone manifolds with semisimple $QH_*$, settling $S^2$, $\mathbb{CP}^n$, and products of these. Ostrover proves infinite diameter for further classes, including negative monotone manifolds.
- **2010–2013.** McDuff (*Monodromy in Hamiltonian Floer theory*) and Usher (*Hofer's metrics and boundary depth*) widen the class dramatically, Usher also producing quasi-isometric embeddings of $\mathbb{R}^k$ (flats) into $\mathrm{Ham}$.
- **2021–2024.** Kislev–Shelukhin sharpen barcode-based Hofer bounds; PFH/Heegaard-Floer spectral invariants (Cristofaro-Gardiner–Humilière–Mak–Seyfaddini–Smith) give unboundedness results at the $C^0$/homeomorphism level on surfaces.

The conjecture is **open in general**; no closed symplectic manifold is known or suspected to have bounded Hofer diameter.

## 4. Partial Results / Verified Cases

Infinite Hofer diameter is proven for:

1. **Open manifolds / $\mathrm{Ham}_c(\mathbb{R}^{2n})$, $n\ge1$** (Hofer 1990), via $e(B(r))=\pi r^2$.
2. **Symplectically aspherical closed manifolds** ($\omega|_{\pi_2(M)}=0=c_1|_{\pi_2(M)}$): tori $\mathbb{T}^{2n}$, surfaces of genus $\ge 1$ and their products, all closed aspherical Kähler examples (Schwarz 2000). Here $\gamma$ itself is unbounded.
3. **Monotone manifolds with semisimple quantum homology**: $S^2$, $\mathbb{CP}^n$ for all $n$, $S^2\times\cdots\times S^2$, monotone toric Fano varieties whose $QH$ splits into fields (Entov–Polterovich 2003) — via nonzero Calabi quasimorphisms.
4. **Negative monotone closed manifolds** and further rational classes (Ostrover 2003).
5. **Broad Floer-theoretic classes with nonvanishing boundary depth**, including many non-monotone and non-semisimple cases, plus quasi-isometrically embedded $\mathbb{R}^k$ for every $k$ (Usher 2013).
6. **All closed surfaces** $\Sigma_g$, $g\ge 0$, in every case; also the $C^0$-analogues: $\overline{\mathrm{Ham}}$ and the group of area-preserving homeomorphisms of $S^2$ and $D^2$ carry unbounded Hofer-type/Calabi invariants (2020–2022 PFH work).
7. **Relative and subgroup versions**: the Hofer metric on Lagrangian orbits (Chekanov, Ostrover) is unbounded in many of the same settings.

## 5. Principal Obstacles

- **Bounded spectral norm.** On $\mathbb{CP}^n$ (and monotone manifolds whose quantum homology is a field) the spectral norm $\gamma$ is *bounded*, so the strongest general lower bound $\|\varphi\|_H\ge\gamma(\varphi)$ carries no information about unboundedness. Any proof there must use a strictly finer invariant.
- **Semisimplicity is not generic.** The Entov–Polterovich quasimorphism requires a field factor in $QH_*(M;\Lambda)$. For manifolds with non-semisimple quantum homology (many blow-ups, higher-degree hypersurfaces, most non-monotone rational manifolds) no Calabi quasimorphism is known, and $\mathrm{Ham}$ may in principle be uniformly perfect — bi-invariant boundedness is a real phenomenon in other transformation groups.
- **Boundary depth can vanish.** $\beta$ is identically bounded (indeed often $0$) precisely on manifolds with strong quantum-homological simplicity, so Usher's mechanism degenerates exactly where quasimorphisms also fail.
- **No non-Floer lower bounds.** Every known lower bound for $\|\cdot\|_H$ on a closed manifold factors through filtered Floer theory. Geometric or hard-analysis methods (energy–capacity, Gromov width, geodesic criteria) give only *local* bounds — they cannot exclude a uniform constant $C$ because capacities of $M$ itself are finite.
- **Bi-invariance kills coarse geometry.** $d_H$ is conjugation-invariant, so word-metric/quasi-isometry techniques from geometric group theory (which handle $\mathrm{Diff}$ via fragmentation) do not apply; fragmentation norms on $\mathrm{Ham}$ are typically bounded.

## 6. The Gap

Proven: unboundedness whenever the Floer package supplies an unbounded Hofer-Lipschitz functional — unbounded $\gamma$ (aspherical case), a nonzero Calabi quasimorphism (semisimple $QH$), or unbounded boundary depth. Conjectured: unboundedness for *every* closed $(M,\omega)$.

The exact gap is the class of closed symplectic manifolds on which **simultaneously** (i) $\gamma$ is bounded, (ii) $QH_*(M;\Lambda)$ admits no field factor supporting a Calabi quasimorphism, and (iii) boundary depth is bounded. For such $M$ the whole existing toolkit is silent. Crossing the gap requires either a new Hofer-Lipschitz invariant not built from the persistence module of $HF_*$ — a genuinely new source of unbounded conjugation-invariant functions on $\mathrm{Ham}$ — or a structural theorem showing that boundedness of $\gamma$ and $\beta$ forces a contradiction with, say, the nondegeneracy of $d_H$ or the simplicity of $\mathrm{Ham}$.

## 7. Current Research (as of June 2026)

- **Persistence/barcode quantitative symplectic topology** (Shelukhin, Kislev, Polterovich, Usher, Zhang): sharpening Hofer bounds from Floer barcodes; the same technology drove Shelukhin's proof of the Hofer–Zehnder conjecture for $\mathbb{CP}^n$ and monotone targets (Annals 2022).
- **$C^0$ symplectic topology and PFH** (Cristofaro-Gardiner, Humilière, Seyfaddini, Mak, Smith; MIT/Sorbonne/Cambridge): periodic Floer homology spectral invariants have produced unbounded quasimorphisms on surface homeomorphism groups and the proof of the simplicity conjecture. Extending PFH-type invariants beyond dimension 4 is the main frontier lead for the diameter conjecture *(frontier — verify)*.
- **Quasimorphism existence without semisimplicity**: attempts to build Calabi quasimorphisms from Lagrangian Floer theory / Fukaya-categorical idempotents (Entov–Polterovich, Fukaya–Oh–Ohta–Ono, Borman) — the operational question is whether every closed $M$ has *some* "heavy" subset supporting a partial quasi-state *(frontier — verify)*.
- **Symplectic cohomology and deformed invariants** for non-monotone and negative-monotone manifolds; equivariant and family Floer refinements.
- **Groups**: Tel Aviv (Polterovich, Ostrover, Entov), Montréal (Shelukhin), Georgia (Usher), IHES/Sorbonne, Stony Brook.

## 8. Future Work

- Identify a **candidate counterexample class** — a closed $M$ with $QH$ a field and vanishing boundary depth — and compute whether $\|\cdot\|_H$ is bounded there; even a conditional answer would decide the shape of the conjecture.
- Develop **invariants of the full Floer persistence module** beyond $\gamma$ and $\beta$ (e.g. total bar-length asymptotics, torsion-type invariants) that survive when $QH$ is a field.
- Push **higher-dimensional analogues of PFH / embedded contact homology**, the only recent tool that gave unbounded invariants where spectral norms were bounded.
- Settle the closely related **boundedness questions**: is $\gamma$ bounded exactly when $QH$ is a field? Is $\mathrm{Ham}(M,\omega)$ ever uniformly perfect for closed $M$?
- Relative programme: prove infinite diameter of Hofer metrics on **Lagrangian submanifold spaces** and deduce the ambient statement.

## 9. Key References

- **[Foundational]** H. Hofer. *On the topological properties of symplectic maps.* Proceedings of the Royal Society of Edinburgh Sect. A, 115 (1990), 25–38.
- **[Foundational]** F. Lalonde, D. McDuff. *The geometry of symplectic energy.* Annals of Mathematics, 141 (1995), 349–371.
- **[Foundational]** M. Bialy, L. Polterovich. *Geodesics of Hofer's metric on the group of Hamiltonian diffeomorphisms.* Duke Mathematical Journal, 76 (1994), 273–292.
- **[Foundational]** H. Hofer, E. Zehnder. *Symplectic Invariants and Hamiltonian Dynamics.* Birkhäuser, 1994.
- **[SOTA]** M. Schwarz. *On the action spectrum for closed symplectically aspherical manifolds.* Pacific Journal of Mathematics, 193 (2000), 419–461.
- **[SOTA]** M. Entov, L. Polterovich. *Calabi quasimorphism and quantum homology.* International Mathematics Research Notices, 2003, no. 30, 1635–1676.
- **[SOTA]** Y. Ostrover. *A comparison of Hofer's metrics on Hamiltonian diffeomorphisms and Lagrangian submanifolds.* Communications in Contemporary Mathematics, 5 (2003), 803–811.
- **[SOTA]** M. Usher. *Hofer's metrics and boundary depth.* Annales Scientifiques de l'École Normale Supérieure, 46 (2013), 57–128.
- **[SOTA]** D. McDuff. *Monodromy in Hamiltonian Floer theory.* Compositio Mathematica, 146 (2010), 1002–1028.
- **[Recent]** A. Kislev, E. Shelukhin. *Bounds on spectral norms and barcodes.* Geometry & Topology, 25 (2021), 3257–3350.
- **[Recent]** E. Shelukhin. *On the Hofer–Zehnder conjecture.* Annals of Mathematics, 195 (2022), 775–839.
- **[Recent]** D. Cristofaro-Gardiner, V. Humilière, C. Y. Mak, S. Seyfaddini, I. Smith. *Quantitative Heegaard Floer cohomology and the Calabi invariant.* Forum of Mathematics, Pi, 10 (2022), e27.
- **[Survey]** L. Polterovich. *The Geometry of the Group of Symplectic Diffeomorphisms.* Lectures in Mathematics ETH Zürich, Birkhäuser, 2001.
- **[Survey]** D. McDuff, D. Salamon. *Introduction to Symplectic Topology.* 3rd edition, Oxford University Press, 2017.
- **[Survey]** L. Polterovich, D. Rosen. *Function Theory on Symplectic Manifolds.* CRM Monograph Series 34, AMS, 2014.

## 10. Worked Example / Concrete Special Case

**(a) The open case, computed.** In $(\mathbb{R}^{2n},\omega_0)$ let $B(r)$ be the ball of radius $r$. Hofer's theorem gives $e(B(r))=\pi r^2$. Pick $\varphi_k$ displacing $B(k)$ inside $B(2k)$ (a translation cut off by a bump function). Then
$$\|\varphi_k\|_H \;\ge\; e(B(k)) \;=\; \pi k^2 \;\xrightarrow[k\to\infty]{}\;\infty .$$
So $\mathrm{diam}\,\mathrm{Ham}_c(\mathbb{R}^{2n})=\infty$. The argument dies on a closed $M$: all capacities of $M$ are finite, so displacement energy is bounded by a constant depending only on $(M,\omega)$.

**(b) The closed case: $S^2$ via the Calabi quasimorphism.** Take $(S^2,\omega)$ with total area $1$. $QH_*(S^2;\Lambda)\cong \Lambda[u]/(u^2=q)$ splits into two fields, so Entov–Polterovich give a homogeneous quasimorphism $\mu\colon\widetilde{\mathrm{Ham}}(S^2)\to\mathbb{R}$ with
$$|\mu(\varphi)| \le \|\varphi\|_H, \qquad \mu(\varphi^k)=k\,\mu(\varphi),$$
and $\mu$ restricts to the Calabi homomorphism on Hamiltonians supported in a *displaceable* disc: if $\mathrm{supp}(H_t)\subset D$ with $\mathrm{Area}(D)<1/2$, then
$$\mu(\varphi_H)\;=\;-\int_0^1\!\!\int_{S^2} H_t\,\omega\,dt .$$
Concretely, let $D$ have area $1/4$ and let $H$ be a time-independent bump with $H\equiv 1$ on the middle of $D$ and $\int_{S^2} H\,\omega = 0.2$. Then $\mu(\varphi_H)=-0.2$ and
$$\|\varphi_H^{\,k}\|_H \;\ge\; |\mu(\varphi_H^{\,k})| \;=\; 0.2\,k .$$
The Hofer norm grows at least linearly in $k$ although $\varphi_H$ is supported in a disc of area $1/4$ and the spectral norm $\gamma(\varphi_H^k)\le 1$ stays bounded. This is the exact mechanism the conjecture needs in general — and precisely what is missing when $QH_*(M)$ admits no such field factor.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*