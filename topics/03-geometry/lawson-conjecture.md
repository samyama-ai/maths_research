---
id: 03-geometry/lawson-conjecture
title: "Lawson Conjecture"
topic: 03-geometry
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Lawson Conjecture

> **Topic:** Algebraic & Differential Geometry · **ID:** `03-geometry/lawson-conjecture` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

**Conjecture (Lawson, 1970).** The only embedded minimal torus in the round $3$-sphere $S^3$ is the Clifford torus, up to ambient isometry.

Precisely: let $F : \Sigma \to S^3 \subset \mathbb{R}^4$ be a smooth **embedding** of a closed orientable surface of genus $1$ whose image is a **minimal** surface (mean curvature $H \equiv 0$). Then $F(\Sigma)$ is congruent, under an element of $O(4)$, to
$$
\mathcal{C} \;=\; \Big\{ (x_1,x_2,x_3,x_4)\in S^3 \;:\; x_1^2+x_2^2 = x_3^2+x_4^2 = \tfrac12 \Big\} \;=\; S^1\!\big(\tfrac{1}{\sqrt2}\big)\times S^1\!\big(\tfrac{1}{\sqrt2}\big).
$$

Embeddedness is essential: **immersed** minimal tori in $S^3$ form an infinite family (Hsiang–Lawson tori, and the integrable-systems families of Pinkall–Sterling and Hitchin), so the conjecture is a statement about how the global no-self-intersection condition rigidifies a local PDE constraint. Genus is also essential: Lawson himself constructed embedded minimal surfaces $\xi_{g,1}$ of every genus $g \geq 1$, and for $g \geq 2$ uniqueness fails (Karcher–Pinkall–Sterling and Kapouleas–Yang produce further embedded examples).

**Status: solved.** Simon Brendle proved the conjecture in 2012 (published *Acta Mathematica*, 2013). A complete proof required showing $|A|^2 \equiv 2$ and then invoking the Chern–do Carmo–Kobayashi rigidity theorem. The page is retained because the natural generalizations — free-boundary (critical catenoid) and higher-genus versions — remain open.

## 2. Mathematical Foundations

Let $\Sigma \subset S^3$ be a closed immersed surface with unit normal $\nu$. The **second fundamental form** is $h_{ij} = \langle \nabla_{e_i} \nu, e_j\rangle$ with principal curvatures $\lambda_1,\lambda_2$; minimality means $H = \lambda_1 + \lambda_2 = 0$, so $\lambda_1 = -\lambda_2 =: \lambda \geq 0$ and $|A|^2 = 2\lambda^2$.

**Gauss equation** in $S^3$ (sectional curvature $1$):
$$
K \;=\; 1 + \lambda_1\lambda_2 \;=\; 1 - \tfrac12 |A|^2 .
$$
**Simons' identity** for minimal surfaces in $S^3$:
$$
\Delta_\Sigma |A|^2 \;=\; 2|\nabla A|^2 + 2|A|^2\big(2 - |A|^2\big).
$$
**Gauss–Bonnet** for a minimal torus ($\chi = 0$) then gives $\int_\Sigma \big(1 - \tfrac12|A|^2\big)\,d\mu = 0$, i.e. $\int_\Sigma |A|^2 = 2\,\mathrm{Area}(\Sigma)$.

**Umbilics and holomorphicity.** The Hopf differential $\Phi = \big(h_{11} - h_{22} - 2i h_{12}\big)\,(dz)^2$ is holomorphic for minimal surfaces in a space form. On a torus, a holomorphic quadratic differential has zero total zero-count, so either $\Phi \equiv 0$ (totally umbilic — impossible for genus $1$, since totally geodesic surfaces in $S^3$ are great spheres) or $\Phi$ is nowhere zero. **Hence every minimal torus in $S^3$ is umbilic-free: $\lambda > 0$ everywhere**, and $\Sigma$ carries a flat conformal structure with global principal coordinates.

**Chern–do Carmo–Kobayashi rigidity (1970).** If $\Sigma \subset S^3$ is a closed minimal surface with $|A|^2$ constant, then $|A|^2 \in \{0, 2\}$; $|A|^2 = 0$ gives the equatorial sphere and $|A|^2 = 2$ gives the Clifford torus. Thus Lawson's conjecture reduces to proving $\lambda$ is **constant**.

**Clifford torus data.** With $F(u,v) = \tfrac{1}{\sqrt2}(\cos u, \sin u, \cos v, \sin v)$: induced metric $\tfrac12(du^2+dv^2)$, $\lambda = 1$, $|A|^2 = 2$, $K \equiv 0$, $\mathrm{Area} = 2\pi^2$, first Laplace eigenvalue $\lambda_1 = 2$, Morse index $5$.

**Two-point functions.** Brendle's method studies, for $\kappa > 0$, the function on $\Sigma \times \Sigma$
$$
Z_\kappa(x,y) \;=\; \kappa\,\lambda(x)\,\big(1 - \langle F(x), F(y)\rangle\big) \;-\; \big\langle \nu(x),\, F(y)\big\rangle ,
$$
a *chord–arc* quantity that is nonnegative exactly when the surface satisfies a quantitative non-collapsing (interior-ball) condition; embeddedness is what makes $Z_\kappa \geq 0$ possible for large $\kappa$.

## 3. History & State of the Art (SOTA)

- **1966.** Almgren proves any minimal immersion of $S^2$ into $S^3$ is a totally geodesic equator (genus-$0$ case).
- **1970.** H. Blaine Lawson Jr., *Complete minimal surfaces in $S^3$* (Annals of Math.), constructs embedded minimal surfaces $\xi_{m,k}$ of every genus and, in the accompanying problem list, conjectures uniqueness in genus $1$. In the same year he proves the **unknottedness** theorem: an embedded minimal surface in $S^3$ is unknotted.
- **1970.** Chern–do Carmo–Kobayashi supply the rigidity statement that makes "$|A|^2$ constant" sufficient.
- **1985–1989.** Pinkall–Sterling and Hitchin classify all *immersed* minimal (resp. CMC) tori by integrable-systems / spectral-curve methods, confirming an infinite family and showing embeddedness cannot be dropped.
- **1990.** Urbano: a minimal torus in $S^3$ of Morse index $\leq 5$ is the Clifford torus (index exactly $5$).
- **1995.** Ros proves the conjecture for surfaces invariant under the antipodal map.
- **2012/2013.** **Brendle** proves the conjecture in full, *Embedded minimal tori in $S^3$ and the Lawson conjecture*, Acta Mathematica 211 (2013).
- **2013/2015.** Andrews–Li extend the method to the **Pinkall–Sterling conjecture**: embedded CMC tori in $S^3$ are rotationally symmetric (the Hsiang–Lawson family).
- **2014.** Marques–Neves prove the Willmore conjecture by min-max, a companion rigidity statement for the Clifford torus ($\mathcal{W} \geq 2\pi^2$).

## 4. Partial Results / Verified Cases

Cases settled before 2012, all now subsumed:

- **Genus $0$:** Almgren (1966) — only the equator. Extended by Calabi and Barbosa to minimal $S^2$ in $S^n$.
- **Constant $|A|^2$:** Chern–do Carmo–Kobayashi (1970) — $|A|^2 = 2$ forces $\mathcal{C}$.
- **Low index:** Urbano (1990) — index $\leq 5$. Combined with the fact that a non-totally-geodesic closed minimal surface has index $\geq 5$, this makes "index $=5$" a characterization.
- **Symmetry hypotheses:** Ros (1995), antipodally invariant embeddings; Hsiang's rotationally symmetric classification.
- **Spectral hypothesis:** Montiel–Ros (1986) — for each conformal class of the torus there is at most one minimal immersion into $S^3$ with $\lambda_1 = 2$; combined with Yau's conjecture ($\lambda_1 = 2$ for embedded minimal surfaces in $S^3$, still open in general) this would imply Lawson.
- **Area bounds:** any embedded minimal torus has $2\pi^2 \leq \mathrm{Area} \le 8\pi$ regimes studied by Choe–Soret; and $\int |A|^2 = 2\,\mathrm{Area}$.
- **Full theorem:** Brendle (2013) — all embedded minimal tori, no symmetry, index or curvature assumption.

## 5. Principal Obstacles

Why the problem resisted for 42 years:

- **Failure of purely local PDE methods.** Simons' identity gives $\Delta|A|^2 \geq 2|A|^2(2 - |A|^2)$ only where $|A|^2 \leq 2$; there is no pointwise curvature pinching available, since $\lambda$ can a priori oscillate. Local analysis cannot see embeddedness at all — the infinite immersed family satisfies every local identity.
- **Integrable systems stop at spectral genus.** Pinkall–Sterling/Hitchin reduce minimal tori to spectral curves, but embeddedness is not a condition expressible on the spectral data in any tractable way; ruling out all higher spectral genera is an infinite family of unsolved transcendental conditions.
- **Min-max and variational methods give existence, not uniqueness.** Almgren–Pitts theory produces minimal surfaces; it does not classify them. Index-$5$ characterizations require knowing the index, which is not controlled a priori.
- **Yau's $\lambda_1$ conjecture is itself open.** The Montiel–Ros route needs $\lambda_1 = 2$ for embedded minimal surfaces in $S^3$ — still unproven for general genus.
- **Standard maximum principles are one-point.** The decisive obstacle was that the relevant object is *global separation of sheets*, a two-point quantity; the classical strong maximum principle applies to functions on $\Sigma$, not $\Sigma \times \Sigma$.

Brendle's breakthrough was exactly to move to $\Sigma \times \Sigma$: he shows the set $\Omega = \{\kappa > 0 : Z_\kappa \geq 0\}$ is nonempty (by embeddedness and compactness), open, and closed in $(0,\infty)$, using at the boundary case an interior touching point $(x_0,y_0)$ with $x_0 \neq y_0$ and a strong maximum principle for the degenerate-elliptic operator satisfied by $Z_\kappa$ in the two-point variables. Openness–closedness forces $\Omega = (0,\infty)$, which is incompatible with $\lambda$ non-constant; hence $|A|^2 \equiv 2$ and Chern–do Carmo–Kobayashi concludes.

## 6. The Gap

For the original statement there is no gap: Brendle's proof is complete and independently verified. The frontier has shifted to the family of statements that Brendle's noncollapsing/two-point technique has *not* yet reached:

1. **Critical catenoid conjecture (open).** Is the critical catenoid the unique embedded free-boundary minimal annulus in the unit ball $B^3 \subset \mathbb{R}^3$? This is the free-boundary analogue of Lawson; Fraser–Schoen posed it, and Brendle-type two-point functions do not obviously survive the boundary condition.
2. **Higher genus.** Classify embedded minimal surfaces of genus $g \geq 2$ in $S^3$; uniqueness is false, but the moduli space is unknown even for $g = 2$.
3. **Yau's $\lambda_1 = 2$ conjecture** for embedded minimal surfaces in $S^3$ of arbitrary genus.
4. **Other ambient spaces.** Lawson-type uniqueness in Berger spheres, lens spaces, and for CMC tori in $\mathbb{R}^3/\Lambda$.

## 7. Current Research (as of June 2026)

- **Free-boundary rigidity.** Groups around Fraser and Schoen (Stanford/UBC) and Kapouleas' school (Brown) pursue the critical catenoid; partial results assume symmetry, low index, or $\lambda_1$ hypotheses.
- **High-genus Lawson surfaces.** Heller–Heller–Traizet apply DPW (loop-group / Dorfmeister–Pedit–Wu) methods to obtain sharp area asymptotics for the Lawson surfaces $\xi_{g,1}$, confirming $\mathrm{Area}(\xi_{g,1}) \to 8\pi$ from below and giving an asymptotic expansion in $1/g$. *(frontier — verify current published version.)*
- **Index and spectral data.** Kapouleas–Wiygul computed the Morse index of $\xi_{g,1}$; extensions of index computations to doublings of the Clifford torus are active.
- **Noncollapsing beyond minimal surfaces.** Andrews' school (ANU) continues to develop two-point maximum principles for curvature flows and for CMC rigidity; the Andrews–Li resolution of Pinkall–Sterling is the template.
- **Min-max.** Marques–Neves (Princeton) and collaborators use Almgren–Pitts theory and the Weyl law for the volume spectrum to produce and count minimal surfaces of prescribed genus.

## 8. Future Work

- Adapt $Z_\kappa$-type two-point functions to manifolds with boundary, to attack the critical catenoid; the obstruction is that the touching point may migrate to $\partial B^3$.
- Prove Yau's $\lambda_1$ conjecture; a positive answer plus Montiel–Ros would give a second, spectral proof of Lawson's conjecture and would generalize to higher genus.
- Determine whether Brendle's noncollapsing estimate has a quantitative form: an explicit lower bound on $\inf \Omega$ in terms of $\mathrm{Area}$, yielding effective uniqueness/stability ("almost-minimal embedded tori are close to $\mathcal{C}$").
- Classify the moduli space of embedded minimal genus-$2$ surfaces in $S^3$, combining DPW deformations with min-max existence.

## 9. Key References

- **[Foundational]** H. B. Lawson Jr. *Complete minimal surfaces in $S^3$.* Annals of Mathematics 92 (1970), 335–374.
- **[Foundational]** H. B. Lawson Jr. *The unknottedness of minimal embeddings.* Inventiones Mathematicae 11 (1970), 183–187.
- **[Foundational]** S. S. Chern, M. do Carmo, S. Kobayashi. *Minimal submanifolds of a sphere with second fundamental form of constant length.* In *Functional Analysis and Related Fields*, Springer, 1970, 59–75.
- **[SOTA]** S. Brendle. *Embedded minimal tori in $S^3$ and the Lawson conjecture.* Acta Mathematica 211 (2013), 177–190.
- **[SOTA]** B. Andrews, H. Li. *Embedded constant mean curvature tori in the three-sphere.* Journal of Differential Geometry 99 (2015), 169–189.
- **[Survey]** S. Brendle. *Minimal surfaces in $S^3$: a survey of recent results.* Bulletin of Mathematical Sciences 3 (2013), 133–171.
- **[Related]** F. C. Marques, A. Neves. *Min-max theory and the Willmore conjecture.* Annals of Mathematics 179 (2014), 683–782.
- **[Related]** F. Urbano. *Minimal surfaces with low index in the three-dimensional sphere.* Proceedings of the AMS 108 (1990), 989–992.
- **[Related]** A. Ros. *A two-piece property for compact minimal surfaces in a three-sphere.* Indiana University Mathematics Journal 44 (1995), 841–849.
- **[Related]** U. Pinkall, I. Sterling. *On the classification of constant mean curvature tori.* Annals of Mathematics 130 (1989), 407–451.
- **[Related]** S. Montiel, A. Ros. *Minimal immersions of surfaces by the first eigenfunctions and conformal area.* Inventiones Mathematicae 83 (1986), 153–166.

## 10. Worked Example / Concrete Special Case

**Verifying the Clifford torus and the reduction step.**

Parametrize $F(u,v) = \tfrac{1}{\sqrt2}\big(\cos u, \sin u, \cos v, \sin v\big)$, $(u,v)\in[0,2\pi)^2$. Then
$$
F_u = \tfrac{1}{\sqrt2}(-\sin u,\cos u,0,0), \qquad F_v = \tfrac{1}{\sqrt2}(0,0,-\sin v,\cos v),
$$
so the induced metric is $g = \tfrac12(du^2 + dv^2)$ — flat, as required for a torus.

A unit normal inside $T_F S^3$ is $\nu = \tfrac{1}{\sqrt2}(\cos u,\sin u,-\cos v,-\sin v)$: check $\langle \nu, F\rangle = \tfrac12 - \tfrac12 = 0$, $\langle \nu, F_u\rangle = \langle \nu, F_v\rangle = 0$, $|\nu| = 1$.

Second fundamental form via $h_{ij} = -\langle F_{ij}, \nu\rangle$ (ambient $\mathbb{R}^4$, tangential part):
$$
F_{uu} = \tfrac{1}{\sqrt2}(-\cos u,-\sin u,0,0), \quad \langle F_{uu},\nu\rangle = -\tfrac12 \;\Rightarrow\; h_{uu} = \tfrac12,
$$
$$
F_{vv} = \tfrac{1}{\sqrt2}(0,0,-\cos v,-\sin v), \quad \langle F_{vv},\nu\rangle = +\tfrac12 \;\Rightarrow\; h_{vv} = -\tfrac12, \qquad h_{uv} = 0.
$$
Principal curvatures are $h_{ii}/g_{ii} = (\tfrac12)/(\tfrac12) = 1$ and $-1$. Hence
$$
H = \lambda_1 + \lambda_2 = 0 \quad(\text{minimal}), \qquad |A|^2 = \lambda_1^2 + \lambda_2^2 = 2 .
$$
Gauss equation: $K = 1 + \lambda_1\lambda_2 = 1 - 1 = 0$, consistent with the flat metric and with Gauss–Bonnet on a torus. Area $= \int_0^{2\pi}\!\!\int_0^{2\pi} \tfrac12\,du\,dv = 2\pi^2$, matching $\int|A|^2 = 2\cdot 2\pi^2 = 4\pi^2$.

**Why this is the only possibility.** Suppose $\Sigma\subset S^3$ is *any* embedded minimal torus. Holomorphicity of the Hopf differential on a genus-$1$ surface forces $\lambda>0$ everywhere. Brendle's argument produces $\lambda \equiv \mathrm{const} = c$, so $|A|^2 = 2c^2$ is constant; Chern–do Carmo–Kobayashi then forces $2c^2 \in \{0,2\}$, and $c>0$ leaves only $|A|^2 = 2$, i.e. $\Sigma \cong \mathcal{C}$.

**Contrast — an immersed non-example.** The Hsiang–Lawson tori
$$
F_{p,q}(u,v) = \big(\cos\alpha\,\cos pu,\ \cos\alpha\,\sin pu,\ \sin\alpha\,\cos qv,\ \sin\alpha\,\sin qv\big), \quad \tan^2\alpha = q/p,
$$
are minimal tori in $S^3$ for coprime $p \neq q$, with $|A|^2 = 2$ but a nontrivial $\mathbb{Z}$-fold self-covering of the $\mathcal{C}$-like configuration: for $(p,q)\neq(1,1)$ the map is immersed but **not embedded**. This is the precise sense in which embeddedness, not minimality, carries the rigidity.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*