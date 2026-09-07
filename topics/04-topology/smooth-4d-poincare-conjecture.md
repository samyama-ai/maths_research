---
id: 04-topology/smooth-4d-poincare-conjecture
title: "Smooth 4D Poincare Conjecture"
topic: 04-topology
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Smooth 4D Poincaré Conjecture

> **Topic:** Topology & Knot Theory · **ID:** `04-topology/smooth-4d-poincare-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

**Conjecture (SPC4).** Every smooth closed 4-manifold $\Sigma$ homotopy equivalent to $S^4$ is diffeomorphic to $S^4$ with its standard smooth structure.

By Freedman's theorem such a $\Sigma$ is automatically *homeomorphic* to $S^4$, so the conjecture asks whether the 4-sphere admits an **exotic** smooth structure: a smooth manifold homeomorphic but not diffeomorphic to $S^4$.

- A **proof** requires showing that every homotopy 4-sphere is standard — equivalently, that the set $\Theta_4^{\mathrm{sm}}$ of smooth homotopy 4-spheres up to diffeomorphism is a single point.
- A **disproof** requires exhibiting one $\Sigma$ together with a computable invariant separating it from $S^4$. No such invariant is currently known to be nontrivial in this setting; producing the invariant is as hard as producing the manifold.

SPC4 is the last open case of the generalized Poincaré conjecture in the smooth category. It is stated as Problem 4.1 in Kirby's problem list.

## 2. Mathematical Foundations

**Homotopy spheres.** $\Sigma^n$ is a homotopy $n$-sphere if it is closed, smooth and homotopy equivalent to $S^n$. For $n=4$ this is equivalent to $\pi_1(\Sigma)=1$ and $H_*(\Sigma;\mathbb{Z}) \cong H_*(S^4;\mathbb{Z})$, i.e.
$$H_i(\Sigma;\mathbb{Z}) = \begin{cases}\mathbb{Z} & i = 0,4\\ 0 & \text{otherwise.}\end{cases}$$
The intersection form $Q_\Sigma$ on $H_2$ is trivial, and the signature and Euler characteristic are $\sigma(\Sigma)=0$, $\chi(\Sigma)=2$.

**Kervaire–Milnor groups.** For $n \ge 5$ the set $\Theta_n$ of homotopy $n$-spheres modulo $h$-cobordism forms a finite abelian group under connected sum, computed from stable homotopy of spheres; e.g. $\Theta_7 \cong \mathbb{Z}/28$. Smale's $h$-cobordism theorem gives $\Theta_n \cong \{\text{homotopy }n\text{-spheres}\}/\mathrm{diffeo}$ for $n\ge 5$. In dimension 4 the $h$-cobordism theorem is unavailable smoothly, so $\Theta_4$ is only a *set* with a monoid structure under $\\#$; SPC4 says $|\Theta_4|=1$.

**Freedman's classification.** A simply connected closed topological 4-manifold is determined up to homeomorphism by $(Q, ks)$, its intersection form and Kirby–Siebenmann invariant $ks \in \mathbb{Z}/2$ (with $ks$ determined by $\sigma/8$ when $Q$ is even). For $Q = 0$ this forces $\Sigma \cong_{\mathrm{homeo}} S^4$.

**Handle/Morse model.** Any homotopy 4-sphere admits a handle decomposition
$$\Sigma = h^0 \cup \big(\textstyle\bigcup_{i=1}^{k} h^1_i\big) \cup \big(\bigcup_{j=1}^{k} h^2_j\big) \cup h^4,$$
which can be arranged with no 3-handles and equal numbers of 1- and 2-handles. The attaching data is a balanced presentation $\langle x_1,\dots,x_k \mid r_1,\dots,r_k\rangle$ of the trivial group, linking SPC4 to the **Andrews–Curtis conjecture**.

**Stabilization.** Wall (1964): if $\Sigma$ is a homotopy 4-sphere, then for some $n$,
$$\Sigma \,\\#\, n(S^2\times S^2) \;\cong_{\mathrm{diffeo}}\; S^4 \,\\#\, n(S^2\times S^2) = \\\\#\, n(S^2\times S^2).$$
So all exoticity is destroyed by stabilization; the open question is whether it exists before stabilizing.

**Two production machines.**
1. *Gluck twist.* For a smoothly embedded 2-sphere $K \subset S^4$ with tubular neighborhood $\nu K \cong S^2\times D^2$, set
$$\Sigma_K = (S^4 \setminus \mathring{\nu}K) \cup_\tau (S^2\times D^2), \qquad \tau(x,\theta) = (\rho_\theta(x),\theta),$$
where $\rho_\theta$ is rotation by $\theta$. Since $\pi_1(SO(3))=\mathbb{Z}/2$, $\tau$ is the unique nontrivial gluing; $\Sigma_K$ is always a homotopy 4-sphere.
2. *Cappell–Shaneson spheres.* For $A \in SL(3,\mathbb{Z})$ with $\det(A-I)=\pm 1$, the mapping torus $M_A = T^3 \times [0,1]/(x,1)\sim(Ax,0)$ is a homology $S^1\times S^3$; surgery on the section circle with a chosen framing yields a homotopy 4-sphere $\Sigma_{A,\epsilon}$.

## 3. History & State of the Art (SOTA)

- **1904.** Poincaré poses the 3-dimensional question.
- **1961.** Smale proves the generalized Poincaré conjecture for $n\ge 5$ (PL/smooth $h$-cobordism); Stallings and Zeeman give independent PL/TOP arguments.
- **1963.** Kervaire–Milnor show the smooth conjecture is **false** for $n=7$ ($\Theta_7 = \mathbb{Z}/28$, Milnor's exotic spheres, 1956).
- **1982.** Freedman proves the topological 4-dimensional Poincaré conjecture via Casson handles and infinite towers.
- **1983–87.** Donaldson's gauge theory shows the smooth and topological worlds diverge sharply in dimension 4; the smooth $h$-cobordism theorem fails (Donaldson; Akbulut corks).
- **1976–2010.** Cappell–Shaneson spheres, Akbulut–Kirby's exotic involution, and Gompf's handle calculus repeatedly produce candidate counterexamples — every one eventually shown standard.
- **2003.** Perelman settles $n=3$.
- **2010.** Freedman–Gompf–Morrison–Walker propose testing candidates with Rasmussen's $s$-invariant; all tested candidates return $s = 0$, giving no obstruction.
- **2021–2023.** Manolescu–Piccirillo convert zero-surgery homeomorphisms into candidate exotic $S^4$'s and definite 4-manifolds; Nakamura and Manolescu–Marengon–Sarkar–Willis eliminate the candidates.

Consensus among experts is split: Freedman and Gompf have publicly leaned toward exotic 4-spheres existing; others (notably in the trisection and Andrews–Curtis communities) toward SPC4 being true.

## 4. Partial Results / Verified Cases

- **All dimensions $n\ne 4$ resolved:** true for $n=1,2,3$ and $n=5,6$; false for $n=7,\dots$ wherever $\Theta_n \ne 0$.
- **Topological case ($n=4$) true** (Freedman 1982), and the PL case is equivalent to the smooth case in dimension 4.
- **Cappell–Shaneson spheres:** Akbulut (2010) proved the $\det(A-I)=+1$ family standard; Gompf (2010) proved standard an infinite family covering the $\det(A-I)=-1$ cases including the Akbulut–Kirby sphere and Gompf's earlier list. Essentially all classically studied $\Sigma_{A,\epsilon}$ are now standard.
- **Gluck twists:** standard for ribbon 2-knots, for 2-knots with a "1-handle unknotted" or unknotted-cross-section presentation, for twist-spun knots (Gluck twists on $n$-twist-spun knots), and — via Gabai's 4-dimensional light bulb theorem (2020) — for 2-spheres admitting a transverse sphere after suitable stabilization arguments.
- **Trisection genus:** every homotopy 4-sphere of trisection genus $\le 2$ is standard (Meier–Zupan 2017); genus 3 is the first unknown case.
- **Stably standard:** every homotopy 4-sphere becomes standard after finitely many $\\#(S^2\times S^2)$ (Wall 1964), and after connected sum with a single $\mathbb{CP}^2$ or $\overline{\mathbb{CP}^2}$ in many families.
- **Invariant-theoretic:** all Seiberg–Witten and Donaldson invariants of a homotopy 4-sphere are trivial (no $b_2^+ > 1$); the $s$-invariant test of Freedman–Gompf–Morrison–Walker returns $0$ on every candidate tested to date.

## 5. Principal Obstacles

- **No gauge theory to apply.** Seiberg–Witten and Donaldson invariants require $b_2^+ \ge 1$ (better, $\ge 2$) to be defined and deformation-invariant. A homotopy 4-sphere has $b_2 = 0$: the moduli spaces are empty or unstable, so the only tools that have ever detected exotic smooth structures in dimension 4 are silent here.
- **Failure of the smooth $h$-cobordism theorem.** In dimension 4 the Whitney trick fails smoothly: Whitney disks can be immersed but not embedded. Freedman replaces them with Casson handles, which are topologically but not smoothly standard. Any homotopy 4-sphere gives an $h$-cobordism from $S^4$ to itself that is topologically but not provably smoothly a product.
- **Relative invariants degenerate.** The $s$-invariant obstruction reduces to slice-genus bounds for knots in $\Sigma \setminus B^4$; Manolescu–Marengon–Sarkar–Willis showed the generalized $s$-invariant cannot obstruct sliceness in the relevant homology-ball settings, closing that route for a broad family.
- **Combinatorial explosion.** Handle presentations reduce SPC4 to Andrews–Curtis moves on balanced trivial presentations. The move set is unbounded and the search space grows super-exponentially; known potential AC-counterexamples (e.g. $\langle x,y \mid x^{n}=y^{n+1},\, xyx=yxy\rangle$) resist both proof and machine search.
- **Constructions are too flexible.** Every known family (Gluck, Cappell–Shaneson, trisection, plumbing) has eventually admitted a handle-cancellation argument, but only after ad hoc discoveries. There is no structural reason known why this should always succeed.

## 6. The Gap

Proven: every homotopy 4-sphere is homeomorphic to $S^4$; is standard after stabilization; and is standard in each finite family so far analyzed (trisection genus $\le 2$; all known Cappell–Shaneson spheres; large classes of Gluck twists). The general statement asserts standardness with **zero** stabilizations and no genus bound.

The precise barrier is a **de-stabilization step**: given a diffeomorphism
$$\Sigma \,\\#\, n(S^2\times S^2) \;\cong\; \\\\#\, n(S^2\times S^2),$$
show that $n$ can be reduced to $0$. Equivalently, find an embedded (not merely immersed) Whitney disk realizing the algebraic cancellation of a 2-handle against a 1-handle. In the disproof direction, the gap is the absence of any smooth invariant of closed 4-manifolds that is nonzero when $b_2 = 0$ — one must invent a new invariant, not merely find a new manifold.

## 7. Current Research (as of June 2026)

- **Zero-surgery / trace-embedding program.** Manolescu–Piccirillo's method — knots $K, K'$ with orientation-preserving homeomorphic zero-surgeries yield candidate exotic definite manifolds and homotopy 4-spheres. Nakamura's trace-embedding criterion eliminated their explicit candidates. The machinery remains the most active source of new candidates. *(frontier — verify)*
- **Trisections.** Gay–Kirby trisection theory, pushed by Meier, Zupan, Kirby and collaborators, is attacking genus-3 homotopy 4-spheres via Heegaard-triple and bridge-trisection combinatorics.
- **Khovanov-theoretic obstructions.** Extensions of Rasmussen's $s$ to knots in punctured homotopy 4-spheres (Manolescu–Marengon–Sarkar–Willis; Ren–Willis work on the Khovanov skein lemma and exotic surfaces) are the leading candidate for a $b_2 = 0$ obstruction. *(frontier — verify)*
- **Exotic surfaces and corks.** Hayden's exotically knotted surfaces in $B^4$ and cork-twisting techniques (Akbulut, Hayden, Piccirillo) probe whether relative exoticity can be closed up.
- **Machine search.** Reinforcement-learning and SAT-based searches for Andrews–Curtis trivializations (following Freedman–Gompf–Morrison–Walker's computational program) have trivialized several long-standing candidate presentations. *(frontier — verify)*

Active groups: Stanford/Berkeley (Manolescu, Gabai's students), MIT (Piccirillo), UT Austin (Gompf), Michigan State/Brigham Young (Meier, Zupan), Max Planck Bonn, Rényi Institute (Stipsicz).

## 8. Future Work

- Construct a diffeomorphism invariant of closed simply connected 4-manifolds sensitive when $b_2 = 0$: candidates include family Bauer–Furuta invariants, $Pin(2)$-equivariant refinements, and skein-lasagna modules from $\mathfrak{gl}_2$ Khovanov homology.
- Settle trisection genus 3: classify genus-3 trisection diagrams of homotopy 4-spheres up to handle slides, the direct analogue of Meier–Zupan's genus-2 result.
- Decide the Andrews–Curtis conjecture for the standard candidate presentations; a counterexample there would not disprove SPC4 but would explain the difficulty.
- Prove or disprove **one-stabilization**: is $\Sigma \\# (S^2\times S^2) \cong \\\\# (S^2\times S^2)$ always, and does one stabilization always suffice? A negative answer would immediately give an exotic $S^4$-like phenomenon.
- Systematize Gluck twists: prove $\Sigma_K \cong S^4$ for all 2-knots $K$, which would remove one entire production machine.

## 9. Key References

- **[Foundational]** M. Freedman. *The topology of four-dimensional manifolds.* Journal of Differential Geometry 17 (1982), 357–453.
- **[Foundational]** S. Smale. *Generalized Poincaré's conjecture in dimensions greater than four.* Annals of Mathematics 74 (1961), 391–406.
- **[Foundational]** M. Kervaire, J. Milnor. *Groups of homotopy spheres: I.* Annals of Mathematics 77 (1963), 504–537.
- **[Foundational]** H. Gluck. *The embedding of two-spheres in the four-sphere.* Transactions of the AMS 104 (1962), 308–333.
- **[Foundational]** S. Cappell, J. Shaneson. *Some new four-manifolds.* Annals of Mathematics 104 (1976), 61–72.
- **[Foundational]** C. T. C. Wall. *On simply-connected 4-manifolds.* Journal of the London Mathematical Society 39 (1964), 141–149.
- **[Key]** S. Akbulut, R. Kirby. *An exotic involution of $S^4$.* Topology 18 (1979), 75–81.
- **[Key]** R. Gompf. *Killing the Akbulut–Kirby 4-sphere, with relevance to the Andrews–Curtis and Schoenflies problems.* Topology 30 (1991), 97–115.
- **[SOTA]** S. Akbulut. *Cappell–Shaneson homotopy spheres are standard.* Annals of Mathematics 171 (2010), 2171–2175.
- **[SOTA]** R. Gompf. *More Cappell–Shaneson spheres are standard.* Algebraic & Geometric Topology 10 (2010), 1665–1681.
- **[SOTA]** M. Freedman, R. Gompf, S. Morrison, K. Walker. *Man and machine thinking about the smooth 4-dimensional Poincaré conjecture.* Quantum Topology 1 (2010), 171–208.
- **[SOTA]** J. Rasmussen. *Khovanov homology and the slice genus.* Inventiones Mathematicae 182 (2010), 419–447.
- **[SOTA]** C. Manolescu, L. Piccirillo. *From zero surgeries to candidates for exotic definite four-manifolds.* arXiv:2102.04391 (2021).
- **[SOTA]** K. Nakamura. *Trace embeddings from zero surgery homeomorphisms.* arXiv:2009.03053 (2020).
- **[SOTA]** C. Manolescu, M. Marengon, S. Sarkar, M. Willis. *A generalization of Rasmussen's invariant, with applications to surfaces in some four-manifolds.* Duke Mathematical Journal 172 (2023).
- **[SOTA]** D. Gabai. *The 4-dimensional light bulb theorem.* Journal of the AMS 33 (2020), 609–652.
- **[SOTA]** J. Meier, A. Zupan. *Genus-two trisections are standard.* Geometry & Topology 21 (2017), 1583–1630.
- **[Survey]** R. Kirby. *Problems in low-dimensional topology.* In *Geometric Topology* (AMS/IP Studies in Advanced Mathematics 2.2), 1997.
- **[Survey]** R. Gompf, A. Stipsicz. *4-Manifolds and Kirby Calculus.* Graduate Studies in Mathematics 20, AMS, 1999.
- **[Survey]** A. Scorpan. *The Wild World of 4-Manifolds.* AMS, 2005.
- **[Survey]** D. Gay, R. Kirby. *Trisecting 4-manifolds.* Geometry & Topology 20 (2016), 3097–3132.

## 10. Worked Example / Concrete Special Case

**A Cappell–Shaneson sphere from the companion matrix of $t^3 - t - 1$.**

Take
$$A = \begin{pmatrix} 0 & 0 & 1\\ 1 & 0 & 1\\ 0 & 1 & 0\end{pmatrix} \in SL(3,\mathbb{Z}), \qquad \chi_A(t) = \det(tI - A) = t^3 - t - 1.$$

*Step 1 — check the surgery condition.* Since $\chi_A(1) = \det(I-A) = (-1)^3\det(A-I)$,
$$\det(A - I) = -\chi_A(1) = -(1 - 1 - 1) = 1.$$
So $A - I$ is invertible over $\mathbb{Z}$, and $\det A = 1$ confirms $A \in SL(3,\mathbb{Z})$.

*Step 2 — the mapping torus.* $A$ induces a diffeomorphism $\varphi_A$ of $T^3 = \mathbb{R}^3/\mathbb{Z}^3$. Its mapping torus $M_A$ is a closed 4-manifold fibering over $S^1$ with fiber $T^3$. By Wang exact sequence,
$$H_1(M_A;\mathbb{Z}) \cong \mathbb{Z} \oplus \operatorname{coker}(A - I) = \mathbb{Z} \oplus \mathbb{Z}^3/(A-I)\mathbb{Z}^3 = \mathbb{Z} \oplus 0 = \mathbb{Z},$$
because $\det(A-I) = 1$ makes $A-I$ surjective. Similarly $H_2(M_A)=0$ and $H_3(M_A)\cong\mathbb{Z}$: $M_A$ is a homology $S^1\times S^3$.

*Step 3 — surgery.* Let $\gamma \subset M_A$ be the section circle $\{pt\}\times S^1$, generating $\pi_1(M_A) \twoheadrightarrow \mathbb{Z}$. Remove $\nu\gamma \cong S^1 \times D^3$ and glue back $D^2 \times S^2$:
$$\Sigma_{A,\epsilon} = (M_A \setminus \mathring{\nu}\gamma) \cup_{\epsilon} (D^2\times S^2),$$
with $\epsilon \in \mathbb{Z}/2$ the framing choice. The surgery kills the $\mathbb{Z}$ in $\pi_1$; since $\pi_1(M_A)$ is normally generated by $[\gamma]$, the result is simply connected. Homology becomes $H_*(\Sigma_{A,\epsilon}) = H_*(S^4)$, and $\chi = 2$, $\sigma = 0$. Hence $\Sigma_{A,\epsilon}$ is a homotopy 4-sphere, and by Freedman it is homeomorphic to $S^4$.

*Step 4 — the hard part.* Akbulut–Kirby (1979) drew a handle diagram for the $\epsilon$-twisted sphere of a matrix in this family: one 1-handle and two 2-handles, whose attaching curves give the balanced presentation
$$\langle x, y \mid xyx = yxy,\; x^5 = y^4 \rangle$$
of the trivial group. Proving $\Sigma \cong S^4$ amounts to cancelling these handles, i.e. trivializing the presentation by Andrews–Curtis moves. Gompf (1991) found such a trivialization after a long sequence of handle slides, and Akbulut (2010) and Gompf (2010) extended this to the full families with $\det(A-I) = \pm 1$.

*What the example shows.* Every algebraic invariant available ($\pi_1$, $H_*$, $Q$, $\sigma$, $\chi$, all Seiberg–Witten invariants) is identical to that of $S^4$ by construction. The only surviving distinction is the handle presentation, and deciding it is a hard combinatorial group-theory problem with no known algorithm. That is exactly the shape of the obstruction described in Sections 5 and 6.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*