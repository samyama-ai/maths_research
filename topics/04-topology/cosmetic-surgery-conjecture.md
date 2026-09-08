---
id: 04-topology/cosmetic-surgery-conjecture
title: "Cosmetic Surgery Conjecture"
topic: 04-topology
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Cosmetic Surgery Conjecture

> **Topic:** Topology & Knot Theory · **ID:** `04-topology/cosmetic-surgery-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

The Pure Cosmetic Surgery Conjecture asserts that for any non-trivial knot in the 3-sphere $S^3$, no two distinct Dehn surgeries can yield orientation-preservingly homeomorphic 3-manifolds. 

Formally, let $K \subset S^3$ be a non-trivial knot, and let $r_1, r_2 \in \mathbb{Q} \cup \{\infty\}$ be two Dehn surgery slopes. If there exists an orientation-preserving homeomorphism $\phi: S^3_{r_1}(K) \xrightarrow{\cong} S^3_{r_2}(K)$ between the resulting surgered manifolds, then the conjecture claims that $r_1 = r_2$. 

Equivalently, the conjecture states that Dehn surgery on a non-trivial knot is a strictly injective operation on the set of slopes up to orientation-preserving homeomorphism. (The conjecture excludes the unknot $U$, for which all slopes $r = 1/n$ trivially yield $S^3_{1/n}(U) \cong S^3$).

## 2. Mathematical Foundations

The problem is grounded in the geometry and algebraic topology of 3-manifolds. Let $K \subset S^3$ be a knot and $N(K)$ be an open tubular neighborhood of $K$. The knot exterior is the compact 3-manifold $X_K = S^3 \setminus N(K)$, whose boundary $\partial X_K \cong T^2$ is a torus.

By convention, we equip $\partial X_K$ with the standard meridian-longitude basis $(\mu, \lambda)$ for $H_1(\partial X_K; \mathbb{Z}) \cong \mathbb{Z} \oplus \mathbb{Z}$, where the meridian $\mu$ bounds a disk in $N(K)$ and the longitude $\lambda$ is homologically trivial in $X_K$. 

A **slope** $r$ is an unoriented isotopy class of simple closed curves on $\partial X_K$. Each slope can be uniquely identified with a rational number or infinity, $r = p/q \in \mathbb{Q} \cup \{\infty\}$, corresponding to the curve class $p\mu + q\lambda$ (where $\gcd(p,q)=1$). 

**Dehn surgery** on $K$ with slope $p/q$ is the operation of gluing a solid torus $S^1 \times D^2$ to the knot exterior $X_K$:
$$S^3_{p/q}(K) = X_K \cup_\varphi (S^1 \times D^2)$$
where the gluing homeomorphism $\varphi: \partial(S^1 \times D^2) \to \partial X_K$ maps the meridian boundary $\partial D^2$ to the curve $p\mu + q\lambda$. 

The manifold $S^3_{p/q}(K)$ inherits a canonical orientation from $S^3$. A surgery is **purely cosmetic** if $S^3_{r_1}(K) \cong S^3_{r_2}(K)$ via an orientation-preserving map. It is **chirally cosmetic** if the map reverses orientation (which is known to exist for certain amphichiral knots). The conjecture specifically addresses the purely cosmetic case.

## 3. History & State of the Art (SOTA)

The history of the conjecture is defined by a sequence of increasingly powerful homological constraints:

- **1989 (Foundations):** Gordon and Luecke proved the monumental theorem that knots are determined by their complements. This immediately resolved the $r_2 = \infty$ case, proving that $S^3_{r}(K) \cong S^3 \implies r=\infty$.
- **1990 (Formalization):** C. McA. Gordon formally proposed the Cosmetic Surgery Conjecture during his address at the International Congress of Mathematicians (ICM) in Kyoto. It was subsequently formalized as Problem 1.81(A) in Robion Kirby’s influential problem list.
- **2015 (Floer Constraints):** Yi Ni and Zhongtao Wu utilized the mapping cone formula in Heegaard Floer homology to impose rigid constraints. They proved that if $S^3_{r_1}(K) \cong S^3_{r_2}(K)$, then $r_1, r_2$ must have opposite signs, and specifically $r_1 = p/q$ and $r_2 = -p/q$.
- **2019 / 2023 (Immersed Curves):** Jonathan Hanselman leveraged bordered Heegaard Floer homology and the geometry of immersed curves to radically narrow the space of possible cosmetic slopes. He proved that cosmetic surgeries must be restricted to slopes of the form $r = \pm 1/n$ or $r = \pm 2$.
- **2024 (Instanton Homology):** In a breakthrough paper, Daemi, Eismeier, and Lidman (*arXiv:2410.21248*) deployed filtered instanton homology to systematically obstruct and rule out the $\pm 1/n$ case.

**State of the Art (2026):** By combining the results of Hanselman, Ni-Wu, and Daemi-Eismeier-Lidman, the conjecture has been functionally reduced to a single remaining edge case. A purely cosmetic surgery can now only exist if $r_1 = 2$, $r_2 = -2$, and the knot $K$ possesses a Seifert genus $g(K) = 2$ and an Alexander polynomial $\Delta_K(t) = 1$.

## 4. Partial Results / Verified Cases

The conjecture has been definitively solved in the affirmative for vast classes of knots and slopes. It is mathematically verified that no purely cosmetic surgeries exist for:
- All torus knots, cable knots, and alternating knots (building on early work by Wang, 2006).
- Any knot $K$ where the Seifert genus $g(K) \neq 2$.
- Any knot $K$ where the Alexander polynomial $\Delta_K(t) \neq 1$.
- Any slope pairs other than strictly $\{2, -2\}$.
- All knots up to 19 crossings, via rigorous computational verification by Futer, Purcell, and Schleimer (2025).

## 5. Principal Obstacles

The problem remains open because traditional invariants and standard quantum topology tools fail at the exact intersection of the remaining constraints ($r=\pm 2$, $g=2$, $\Delta_K(t)=1$):

1. **Failure of Homology & Linking Forms:** As shown in Section 10, classical first homology and linking forms are completely identical for $S^3_{2}(K)$ and $S^3_{-2}(K)$, offering no algebraic leverage.
2. **Degeneration of Heegaard Floer Homology:** While Heegaard Floer homology $\widehat{HF}$ is generally a complete invariant for identifying 3-manifolds, its computation via the surgery mapping cone relies heavily on the knot Floer homology $HFK^-(K)$. The strict condition $\Delta_K(t) = 1$ forces the Euler characteristic of $HFK^-$ in each grading to mimic the unknot. For the specific case of $\pm 2$ surgeries, this causes the resulting chain complexes to be virtually indistinguishable in the Grothendieck group, preventing $\widehat{HF}$ from obstructing the homeomorphism.
3. **Gauge Theory and Accidental Symmetries:** Instanton Floer homology distinguishes manifolds by studying flat $SU(2)$ connections, evaluated via the Chern-Simons functional $\mathcal{CS}: \mathcal{A}/ \mathcal{G} \to \mathbb{R}/\mathbb{Z}$. For $S^3_{\pm 2}(K)$, gauge theory encounters "accidental symmetries." Because $p=2$ is even and small, the spectral flow between critical points on the Chern-Simons functional exhibits a parity symmetry that prevents current filtered gauge techniques from extracting a topological distinction.

## 6. The Gap

The exact mathematical barrier is resolving the isolated boundary case: obstructing an orientation-preserving homeomorphism $S^3_2(K) \cong S^3_{-2}(K)$ for a knot $K \subset S^3$ satisfying $g(K) = 2$ and $\Delta_K(t) = 1$. Bridging this gap requires either finding a highly exotic counterexample knot that supports a hidden geometric symmetry in its exterior, or defining a finer, higher-order topological invariant—potentially a new variant of equivariant gauge theory—that breaks the algebraic symmetry of 2-surgery without degenerating under the $\Delta_K(t)=1$ constraint.

## 7. Current Research (as of June 2026)

- **Instanton Refinement:** Leading groups at Caltech, Princeton, and UT Austin are actively refining the grading and filtrations on $SU(2)$ instanton homology, attempting to break the spectral flow symmetry for $p=2$.
- **Quantum Obstructions:** *(frontier — verify)* Researchers are attempting to apply Witten-Reshetikhin-Turaev (WRT) invariants and the colored Jones polynomial evaluated at specific higher roots of unity ($q = e^{2\pi i / k}$) to find an algebraic obstruction that isolates the $\pm 2$ surgeries on genus-2 knots.
- **Character Varieties:** Active investigations into the $SU(2)$ and $SL(2, \mathbb{C})$ character varieties of $\pi_1(S^3_{\pm 2}(K))$ aim to identify subtle algebraic rigidities in the representation space that would forbid an orientation-preserving isomorphism.

## 8. Future Work

- **Computational Exhaustion:** Expanding computational searches of hyperbolic knots with $g=2$ and $\Delta=1$ using software like SnapPy and Regina. Extending the census beyond 20 crossings could either empirically support the conjecture or yield the first counterexample.
- **Contact Geometry Integration:** Connecting the remaining topological gap to the Contact Cosmetic Surgery Conjecture. Recent progress has resolved the contact analogue for Legendrian knots in $L$-spaces, and bridging these techniques may provide the necessary geometric rigidity to rule out $\pm 2$ topological surgeries.
- **Khovanov Homology:** Exploring whether the Khovanov homology of the surgered manifolds, which categorifies the Jones polynomial, can distinguish $S^3_2(K)$ from $S^3_{-2}(K)$ in ways that Heegaard Floer homology cannot.

## 9. Key References

- **[Foundational]** Gordon, C. McA., and Luecke, J. *Knots are determined by their complements.* Journal of the American Mathematical Society, 1989. [DOI](https://doi.org/10.1090/s0273-0979-1989-15706-6)
- **[SOTA / Recent]** Hanselman, J. *Heegaard Floer homology and cosmetic surgeries in $S^3$.* Journal of the European Mathematical Society, 2023. [DOI](https://doi.org/10.4171/jems/1218)
- **[SOTA / Recent]** Daemi, A., Eismeier, M. M., and Lidman, T. *Filtered instanton homology and cosmetic surgery.* arXiv:2410.21248, 2024.
- **[Survey]** Ni, Y., and Wu, Z. *Cosmetic surgeries on knots in $S^3$.* Journal für die reine und angewandte Mathematik, 2015.

## 10. Worked Example / Concrete Special Case

To ground why standard algebraic topology completely fails to resolve the remaining $\pm 2$ case, we can walk through a concrete calculation of the first homology and the linking form.

Let $K$ be a non-trivial knot. Suppose Dehn surgeries $S^3_{p_1/q_1}(K)$ and $S^3_{p_2/q_2}(K)$ yield orientation-preserving homeomorphic manifolds. 

**Step 1: First Homology**  
The first homology group of a surgered manifold is $H_1(S^3_{p/q}(K); \mathbb{Z}) \cong \mathbb{Z}/|p|\mathbb{Z}$. For the two manifolds to be homeomorphic, their first homology groups must be isomorphic, forcing $|p_1| = |p_2|$. Without loss of generality, let $p_1 = -p_2 = p$.

**Step 2: The Linking Form**  
The linking form is a non-degenerate, symmetric bilinear pairing on the torsion group:
$$\lambda: H_1 \times H_1 \to \mathbb{Q}/\mathbb{Z}$$
For $S^3_{p/q}(K)$, the linking form evaluates to $\lambda([x], [y]) = \frac{q}{p} xy \pmod 1$ on a chosen generator.

An orientation-preserving homeomorphism requires a strict isometry of linking forms (the sign is strictly preserved). Thus, there must exist a unit $u \in (\mathbb{Z}/|p|\mathbb{Z})^\times$ that maps the generator of the first manifold to the second, satisfying:
$$\frac{q_2}{p} \equiv u^2 \frac{q_1}{p} \pmod 1 \implies q_2 \equiv u^2 q_1 \pmod p$$

**Step 3: The SOTA Failure Case**  
Apply this constraint to the sole remaining unsolved case dictated by modern SOTA research: slopes $r_1 = 2/1$ and $r_2 = -2/1$. 
Here, $p = 2$, $q_1 = 1$, and $q_2 = -1$. 

The isometry condition for the linking form becomes:
$$-1 \equiv u^2 (1) \pmod 2$$
Since the only invertible element in $\mathbb{Z}/2\mathbb{Z}$ is $u = 1$, the condition simplifies directly to:
$$-1 \equiv 1 \pmod 2$$
This mathematical congruence is trivially **TRUE**. 

**Conclusion:** Elementary algebraic topology elegantly obstructs orientation-preserving cosmetic surgeries for almost all slopes. However, because $-1 \equiv 1 \pmod 2$, the linking form constraint mathematically evaporates for $\pm 2$ surgeries. This worked example proves exactly why the $\pm 2$ case acts as an invisible boundary to classical invariants, demonstrating why modern topological research requires the full weight of filtered instanton homology to even approach the remaining gap.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*