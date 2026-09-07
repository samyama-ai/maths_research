---
id: 04-topology/hauptvermutung
title: "Hauptvermutung"
topic: 04-topology
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Hauptvermutung

> **Topic:** Topology & Knot Theory · **ID:** `04-topology/hauptvermutung` · **Status:** solved-recently (disproved; residual dimension-4 questions open)

## 1. Problem Statement / Conjecture

The *Hauptvermutung der kombinatorischen Topologie* ("main conjecture of combinatorial topology") asserts:

> **(H)** If two finite simplicial complexes $K$ and $L$ have homeomorphic polyhedra, $|K| \cong |L|$, then $K$ and $L$ admit a **common subdivision**: there exist subdivisions $K'$ of $K$ and $L'$ of $L$ that are simplicially isomorphic.

Equivalently: a topological space carries at most one piecewise-linear (PL) structure, so combinatorially defined quantities (Whitehead torsion, Reidemeister torsion, simplicial chain-level invariants) are automatically topological invariants.

Two specialisations are tracked separately:

- **(H-cx)** the statement above for arbitrary finite complexes;
- **(H-mfd)** the *manifold Hauptvermutung*: if $M, N$ are compact PL manifolds and $h : M \to N$ is a homeomorphism, is $h$ homotopic (or isotopic) to a PL homeomorphism?

A disproof requires exhibiting homeomorphic polyhedra with provably distinct PL structures, detected by an invariant of the PL structure that is not a homotopy or topological invariant. The conjecture is **false** in both forms: (H-cx) by Milnor (1961), (H-mfd) by Kirby–Siebenmann (1969), with the obstruction theory of Sullivan and Casson giving the exact conditions under which it does hold.

## 2. Mathematical Foundations

**Simplicial and PL categories.** A finite simplicial complex $K$ has polyhedron $|K| \subset \mathbb{R}^N$. A map $f : |K| \to |L|$ is *PL* if it is simplicial for some subdivisions. A *combinatorial triangulation* of a topological manifold $M^n$ is a homeomorphism $|K| \to M$ with every vertex link PL homeomorphic to $S^{n-1}$; equivalently $|K|$ is a PL manifold.

**Whitehead torsion.** For a group $\pi$, let
$$\operatorname{Wh}(\pi) \;=\; K_1(\mathbb{Z}[\pi]) \big/ \{\pm g : g \in \pi\}.$$
A homotopy equivalence $f : K \to L$ of finite complexes has torsion $\tau(f) \in \operatorname{Wh}(\pi_1 L)$, computed from the acyclic based chain complex of the mapping cylinder pair $(M_f, K)$ over $\mathbb{Z}[\pi_1 L]$. Whitehead's theorem: $\tau(f) = 0$ iff $f$ is a *simple* homotopy equivalence, i.e. deformable to $L$ by elementary collapses and expansions. Torsion is invariant under **subdivision**, hence under PL homeomorphism, so
$$K \cong_{\mathrm{PL}} L \;\Longrightarrow\; \tau(\mathrm{id}) = 0 .$$
The whole point of (H) is whether a mere homeomorphism forces $\tau = 0$.

**Casson–Sullivan obstruction.** For a homeomorphism $h : M \to N$ of compact PL manifolds with $\dim \ge 5$, there is an invariant
$$\kappa(h) \in H^3(M; \mathbb{Z}/2)$$
whose vanishing is necessary and sufficient (in the simply connected case) for $h$ to be homotopic to a PL homeomorphism. It is the restriction of the Kirby–Siebenmann class: the forgetful map $\mathrm{TOP}/\mathrm{PL}$ satisfies
$$\mathrm{TOP}/\mathrm{PL} \simeq K(\mathbb{Z}/2, 3),$$
so PL structures on a topological manifold $M^n$ ($n \ge 5$) form a set in bijection with $[M, \mathrm{TOP}/\mathrm{PL}] = H^3(M; \mathbb{Z}/2)$ once nonempty, and $M$ is PL-triangulable iff the obstruction $ks(M) \in H^4(M; \mathbb{Z}/2)$ vanishes.

**Simplicial (non-combinatorial) triangulations.** Galewski–Stern and Matumoto reduced existence of *any* simplicial triangulation of $M^n$, $n \ge 5$, to the splitting of
$$0 \to \ker \mu \to \Theta_3^H \xrightarrow{\ \mu\ } \mathbb{Z}/2 \to 0,$$
where $\Theta_3^H$ is the homology-cobordism group of oriented homology 3-spheres and $\mu$ the Rokhlin invariant: $M$ is triangulable iff $\delta(ks(M)) = 0$ in $H^5(M; \ker\mu)$.

## 3. History & State of the Art (SOTA)

- **1908.** Formulated independently by **Steinitz** and **Tietze**; it underwrote the entire program of defining homology combinatorially and proving topological invariance.
- **1925 / 1952.** True in low dimensions: **Radó** for 2-manifolds, **Moise** (with Bing) for 3-manifolds, where triangulation exists and is unique up to subdivision.
- **1961. Milnor** disproves (H-cx): homeomorphic finite complexes of dimension $6$ built from the homotopy-equivalent lens spaces $L(7,1)$, $L(7,2)$ that are not PL homeomorphic, detected by Whitehead torsion.
- **1967. Sullivan** proves (H-mfd) *holds* for simply connected closed PL manifolds of dimension $\ge 5$ with $H^3(M;\mathbb{Z}/2) = 0$ (and $H_3(M)$ 2-torsion-free), via surgery and the structure of $G/\mathrm{PL}$.
- **1969. Kirby–Siebenmann** settle the general manifold case using the torus trick: $\mathrm{TOP}/\mathrm{PL} \simeq K(\mathbb{Z}/2,3)$, giving both non-triangulable topological manifolds ($\dim \ge 5$) and homeomorphic PL manifolds that are not PL homeomorphic. (H-mfd) is false.
- **1980s.** In dimension 4, PL $=$ smooth (Cerf, Hirsch–Mazur), so **Donaldson**'s exotic phenomena (homeomorphic, non-diffeomorphic simply connected elliptic surfaces) disprove (H-mfd) in dimension 4 as well.
- **2016. Manolescu** shows $\mu$ does not split, using $\mathrm{Pin}(2)$-equivariant Seiberg–Witten Floer homology: non-triangulable topological manifolds exist in every dimension $\ge 5$.

## 4. Partial Results / Verified Cases

Cases where the Hauptvermutung is a **theorem**:

| Class | Result |
|---|---|
| Complexes of dim $\le 3$ | True (Papakyriakopoulos, Moise, Bing) |
| Topological $n$-manifolds, $n \le 3$ | Triangulation exists and is unique up to subdivision (Radó 1925; Moise 1952) |
| Simply connected closed PL $M^n$, $n \ge 5$, $H^3(M;\mathbb{Z}/2) = 0$ | Sullivan 1967: every homeomorphism is homotopic to a PL homeomorphism; e.g. $M = S^n$, $\mathbb{CP}^k$ ($2k \ge 6$), $S^p \times S^q$ with $p+q \ge 5$, $p,q \neq 3$ |
| Homotopy spheres $\Sigma^n$, $n \ge 5$ | PL structure unique: $\Theta_n^{\mathrm{PL}} = 0$ for $n\ge5$ (Kervaire–Milnor + generalized Poincaré) |
| $M^n$ with $H^3(M;\mathbb{Z}/2)=0$, $n \ge 5$ (non-simply-connected) | PL structures unique up to concordance |

Cases where it **fails**, with explicit witnesses:

- **Complexes, $\dim \ge 6$**: Milnor's lens-space joins ($p = 7$, $q = 1, 2$).
- **Manifolds, $\dim \ge 5$**: the $n$-torus $T^n$, $n \ge 5$, has $H^3(T^n;\mathbb{Z}/2) \cong (\mathbb{Z}/2)^{\binom{n}{3}} \ne 0$; each nonzero class realises a self-homeomorphism not homotopic to a PL homeomorphism, and homotopy tori that are homeomorphic but not PL homeomorphic.
- **Manifolds, $\dim 4$**: Donaldson's pairs, e.g. the Dolgachev surface $E(1)_{2,3}$ and $\mathbb{CP}^2 \\# 9\overline{\mathbb{CP}^2}$ — homeomorphic (Freedman), not diffeomorphic, hence not PL homeomorphic.

## 5. Principal Obstacles

The historical obstacle was that every technique available before 1960 was *combinatorial by construction*, so it could not see the difference between a homeomorphism and a PL homeomorphism.

- **Simplicial approximation is not enough.** It replaces a continuous map by a PL one only up to homotopy; homotopy destroys exactly the torsion information that (H) is about.
- **Homotopy invariants are blind.** Homology, cohomology, homotopy groups, and characteristic classes cannot separate $L(7,1)$ from $L(7,2)$; only *simple* homotopy type does, and Whitehead torsion lives in $\operatorname{Wh}(\mathbb{Z}/7) \cong \mathbb{Z}^2$, a group with no homotopy-theoretic definition.
- **Wild topology.** A topological homeomorphism can be nowhere locally PL; there is no local model, so no obstruction can be built by naïve induction over skeleta. Kirby–Siebenmann's torus trick (immerse a punctured torus in $\mathbb{R}^n$, pass to a finite cover, use surgery on homotopy tori) was needed precisely to manufacture local PL structure out of nothing.
- **Dimension 4 is doubly blocked.** Surgery and the $s$-cobordism theorem require the Whitney trick, which fails topologically only in dimension 4 for smooth/PL categories; gauge theory shows the failure is genuine, not a technical gap.
- **The residual open case is a Floer-theoretic problem.** Whether every topological 4-manifold is simplicially triangulable is not reducible to $\Theta_3^H$ by the Galewski–Stern–Matumoto machinery, which needs $n \ge 5$.

## 6. The Gap

The classical conjecture is closed. The precise remaining boundary:

1. **Dimension 4 triangulation.** Does every closed topological 4-manifold admit *some* simplicial triangulation? Casson's invariant shows Freedman's $E_8$-manifold admits no *combinatorial* triangulation; whether it admits a non-combinatorial one is open, and the $n \ge 5$ obstruction theory does not apply because a 4-dimensional vertex link is a homology 3-sphere for which no surgery-theoretic resolution exists in the ambient dimension.
2. **Effective control of $\ker \mu \subset \Theta_3^H$.** Manolescu's $\beta$ shows $\mu$ does not split, but the structure of $\Theta_3^H$ (e.g. whether it contains $\mathbb{Z}/n$ torsion at all) is unknown, so the Galewski–Stern obstruction $\delta(ks(M))$ is not computable in general.
3. **Isotopy vs. homotopy.** Sullivan/Casson give homotopy through PL homeomorphisms; upgrading to isotopy involves $\pi_0 \mathrm{TOP}(M)/\pi_0 \mathrm{PL}(M)$, which is only partially known for non-simply-connected $M$.

## 7. Current Research (as of June 2026)

- **Homology cobordism.** Involutive Heegaard Floer homology (Hendricks–Manolescu) and the $\Theta_3^H$ program (Dai–Hom–Stoffregen–Truong: $\Theta_3^H$ contains a $\mathbb{Z}^\infty$ summand) sharpen what is known about $\ker\mu$. Groups at Princeton, Stanford, Georgia Tech, UT Austin.
- **Dimension-4 triangulation.** Attempts to obstruct or construct non-combinatorial triangulations of the $E_8$-manifold using Seiberg–Witten and $\mathrm{Pin}(2)$ techniques remain the only credible route *(frontier — verify)*.
- **Quantitative / computational PL topology.** Bounds on the number of subdivisions needed to realise a PL homeomorphism, and complexity of deciding PL homeomorphism (undecidable for $\dim \ge 5$ by Markov-type arguments) — active in computational topology groups (TU Berlin, IST Austria).
- **Homotopy-theoretic reformulation.** $\mathrm{TOP}/\mathrm{PL} \simeq K(\mathbb{Z}/2,3)$ is being revisited through $\infty$-categorical surgery and Poincaré-duality-space methods (Lurie-style; the Hermitian $K$-theory program of Calmès–Dotto–Harpaz–Land–Nardin–Nikolaus–Steimle) *(frontier — verify)*.

## 8. Future Work

- Decide the 4-dimensional triangulation conjecture; Manolescu has identified this as the outstanding descendant of the Hauptvermutung.
- Compute or bound the torsion subgroup of $\Theta_3^H$; any element of order 2 with Rokhlin invariant 1 would immediately split $\mu$ and reverse the 2016 conclusion in the $n\ge5$ setting.
- Extend Sullivan-type positive results to non-simply-connected manifolds with controlled $H^3(M;\mathbb{Z}/2)$ and known $\operatorname{Wh}(\pi_1)$, e.g. aspherical manifolds satisfying the Farrell–Jones conjecture (where $\operatorname{Wh}(\pi)=0$).
- Develop algorithmic certificates: given two triangulations, produce a common subdivision or a torsion obstruction, in cases where the ambient decision problem is decidable.

## 9. Key References

- **[Foundational]** H. Tietze. *Über die topologischen Invarianten mehrdimensionaler Mannigfaltigkeiten.* Monatshefte für Mathematik und Physik **19** (1908), 1–118.
- **[Foundational]** E. Steinitz. *Beiträge zur Analysis situs.* Sitzungsberichte der Berliner Mathematischen Gesellschaft **7** (1908), 29–49.
- **[Foundational]** T. Radó. *Über den Begriff der Riemannschen Fläche.* Acta Litterarum ac Scientiarum Szeged **2** (1925), 101–121.
- **[Foundational]** E. E. Moise. *Affine structures in 3-manifolds V: The triangulation theorem and Hauptvermutung.* Annals of Mathematics **56** (1952), 96–114.
- **[Foundational]** J. H. C. Whitehead. *Simple homotopy types.* American Journal of Mathematics **72** (1950), 1–57.
- **[Counterexample]** J. Milnor. *Two complexes which are homeomorphic but combinatorially distinct.* Annals of Mathematics **74** (1961), 575–590.
- **[Counterexample]** D. Sullivan. *On the Hauptvermutung for manifolds.* Bulletin of the AMS **73** (1967), 598–600.
- **[Counterexample]** R. C. Kirby, L. C. Siebenmann. *On the triangulation of manifolds and the Hauptvermutung.* Bulletin of the AMS **75** (1969), 742–749.
- **[Foundational]** R. C. Kirby, L. C. Siebenmann. *Foundational Essays on Topological Manifolds, Smoothings, and Triangulations.* Annals of Mathematics Studies 88, Princeton University Press, 1977.
- **[Structural]** D. E. Galewski, R. J. Stern. *Classification of simplicial triangulations of topological manifolds.* Annals of Mathematics **111** (1980), 1–34.
- **[SOTA]** C. Manolescu. *Pin(2)-equivariant Seiberg–Witten Floer homology and the triangulation conjecture.* Journal of the AMS **29** (2016), 147–176.
- **[SOTA]** I. Dai, J. Hom, M. Stoffregen, L. Truong. *An infinite-rank summand of the homology cobordism group.* Duke Mathematical Journal **170** (2021), 3255–3340.
- **[Survey]** A. A. Ranicki (ed.). *The Hauptvermutung Book.* K-Monographs in Mathematics 1, Kluwer, 1996.
- **[Survey]** C. Manolescu. *Lectures on the triangulation conjecture.* Proceedings of the Gökova Geometry–Topology Conference 2015, 1–38.
- **[Textbook]** M. M. Cohen. *A Course in Simple-Homotopy Theory.* Graduate Texts in Mathematics 10, Springer, 1973.
- **[Textbook]** S. Donaldson. *Irrationality and the h-cobordism conjecture.* Journal of Differential Geometry **26** (1987), 141–168.

## 10. Worked Example / Concrete Special Case

**The lens spaces behind Milnor's counterexample.** For $p$ odd and $\gcd(p,q)=1$, $L(p,q) = S^3 / \sim$ with $(z_1,z_2) \sim (\zeta z_1, \zeta^q z_2)$, $\zeta = e^{2\pi i/p}$. Two classification facts:

- **Homotopy:** $L(p,q) \simeq L(p,q')$ iff $q q' \equiv \pm n^2 \pmod p$ for some $n$.
- **Homeomorphism:** $L(p,q) \cong L(p,q')$ iff $q' \equiv \pm q^{\pm 1} \pmod p$ (Reidemeister).

Take $p = 7$, $q = 1$, $q' = 2$. Squares mod 7 are $\{1,2,4\}$, and $1 \cdot 2 = 2 = 3^2 \bmod 7$, so
$$L(7,1) \simeq L(7,2) \quad \text{(homotopy equivalent).}$$
But $q^{\pm1} = 1$ and $\pm 1 \not\equiv 2 \pmod 7$, so
$$L(7,1) \not\cong L(7,2) \quad \text{(not homeomorphic).}$$

The separating invariant is Reidemeister torsion: for a character $\rho(\zeta) = \zeta^{k}$,
$$\Delta_\rho\big(L(7,q)\big) = (\zeta^{k} - 1)(\zeta^{k q^{*}} - 1), \qquad q q^{*} \equiv 1 \ (\mathrm{mod}\ 7),$$
taken up to units $\pm\zeta^{j}$. For $q=1$ this is $(\zeta^k-1)^2$; for $q=2$, $q^*=4$, giving $(\zeta^k-1)(\zeta^{4k}-1)$. These differ in $\mathbb{Z}[\zeta_7]^\times$-classes, so the homotopy equivalence $f : L(7,1) \to L(7,2)$ has
$$\tau(f) \neq 0 \in \operatorname{Wh}(\mathbb{Z}/7) \cong \mathbb{Z}^{2}.$$

**Milnor's step.** Joining each lens space with a sphere kills the homotopy-theoretic difference: $L(7,1) * S^2$ and $L(7,2) * S^2$ are simply connected 6-dimensional polyhedra, and Milnor showed they are **homeomorphic**. If the Hauptvermutung held, they would share a common subdivision, and the induced equivalence would be *simple*, forcing the torsion contribution of $\tau(f)$ to vanish. It does not: the torsion of the join is computed from $\tau(f)$ weighted by $\chi(S^2)=2$, and $2\tau(f) \ne 0$ in the torsion-free group $\mathbb{Z}^2$. Hence no common subdivision exists, and (H-cx) is false in every dimension $\ge 6$.

**Manifold analogue.** For $M = T^5$, $H^3(T^5;\mathbb{Z}/2) \cong (\mathbb{Z}/2)^{10}$. Each of the $2^{10}-1$ nonzero classes $\kappa$ is realised by a self-homeomorphism of $T^5$ that is not homotopic to a PL homeomorphism — the manifold-level failure, in the smallest dimension where it occurs.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*