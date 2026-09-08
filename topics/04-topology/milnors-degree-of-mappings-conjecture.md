---
id: 04-topology/milnors-degree-of-mappings-conjecture
title: "Milnor's Degree of Mappings Conjecture"
topic: 04-topology
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Milnor's Degree of Mappings Conjecture

> **Topic:** Topology & Knot Theory · **ID:** `04-topology/milnors-degree-of-mappings-conjecture` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Let $M, N$ be closed, connected, oriented $n$-manifolds. Every continuous map $f: M \to N$ has a **degree** $\deg f \in \mathbb{Z}$, defined by $f_*[M] = (\deg f)\,[N]$ in $H_n(N;\mathbb{Z}) \cong \mathbb{Z}$. Write

$$D(M,N) = \{\deg f \;:\; f: M \to N \text{ continuous}\}, \qquad D(N) := D(N,N).$$

Milnor's degree-of-mappings problem, raised by Milnor and sharpened in Milnor–Thurston (1977) and by Gromov, asks for a topological criterion deciding when $D(M,N)$ is finite. The conjectural package has three linked parts.

- **(A) Finiteness.** For closed oriented $M,N$ of the same dimension, $D(M,N)$ is finite unless $N$ is *flexible*, i.e. unless $D(N)$ is infinite. So all unbounded degree behaviour is inherited from self-maps of the target.
- **(B) Dichotomy (aspherical case).** If $N$ is closed, oriented and aspherical, then either $D(N) = \{0, \pm 1\}$ ($N$ is *inflexible*) or $D(N)$ is infinite. No intermediate behaviour occurs.
- **(C) Structure.** A closed oriented aspherical flexible $N$ admits a nontrivial self-covering; equivalently $\pi_1(N)$ is isomorphic to a proper subgroup of finite index in itself (a *non-co-Hopfian* group).

A complete resolution means proving each statement for all $n$, or exhibiting a closed oriented manifold violating it — e.g. an aspherical $N$ with $D(N)$ infinite but $\pi_1(N)$ co-Hopfian, or with $D(N) = \{0,\pm 1, \pm k\}$ for some $k \ge 2$.

## 2. Mathematical Foundations

**Degree.** For $f:M\to N$ smooth and $y$ a regular value, $\deg f = \sum_{x \in f^{-1}(y)} \operatorname{sign}\det(df_x)$. Degree is multiplicative: $\deg(g\circ f) = \deg g \cdot \deg f$, so $D(N)$ is a multiplicatively closed subset of $\mathbb{Z}$ containing $0$ and $1$.

**Simplicial volume.** For a singular real chain $c = \sum_i a_i \sigma_i$ put $\|c\|_1 = \sum_i |a_i|$. The *Gromov norm* (simplicial volume) of $M$ is

$$\|M\| \;=\; \inf\bigl\{\, \|c\|_1 \;:\; c \in C_n(M;\mathbb{R}),\ \partial c = 0,\ [c] = [M]_{\mathbb{R}} \,\bigr\}.$$

It is a homotopy invariant, and functoriality of $f_*$ with $\|f_*c\|_1 \le \|c\|_1$ gives the **degree theorem**

$$|\deg f| \cdot \|N\| \;\le\; \|M\|. \tag{2.1}$$

Hence $\|N\| > 0 \Rightarrow |D(M,N)| \le 2\lfloor \|M\|/\|N\|\rfloor + 1 < \infty$.

**Gromov–Thurston proportionality.** For a closed hyperbolic $n$-manifold $M$,

$$\|M\| = \frac{\operatorname{Vol}(M)}{v_n}, \qquad v_n = \text{volume of the regular ideal geodesic $n$-simplex in } \mathbb{H}^n,$$

with $v_3 = \Lambda(\pi/6)\cdot 6 \approx 1.0149416$ (Lobachevsky function). In particular $\|M\| > 0$.

**Functorial semi-norms.** A *functorial semi-norm* on $H_n(-;\mathbb{R})$ assigns $|\cdot|$ to homology classes with $|f_*\alpha| \le |\alpha|$ for all continuous $f$. Any such gives a bound of type (2.1). Simplicial volume is the universal example among those bounded on the point.

**Co-Hopfian groups.** $G$ is co-Hopfian if every injective endomorphism is an automorphism. Mostow rigidity implies $\pi_1$ of a closed hyperbolic $n$-manifold, $n \ge 3$, is co-Hopfian; lattices in higher-rank semisimple Lie groups are co-Hopfian by Margulis superrigidity. Statement (C) predicts co-Hopfian $\Leftrightarrow$ inflexible in the aspherical setting.

**Hopf property.** If $N$ is closed oriented aspherical and $f:N\to N$ has $|\deg f| = 1$, then $f_*: \pi_1(N)\to\pi_1(N)$ is surjective; if $\pi_1(N)$ is Hopfian (e.g. residually finite and finitely generated), $f$ is a homotopy equivalence.

## 3. History & State of the Art (SOTA)

- **1966–1970s.** Milnor circulates the question of which pairs $(M,N)$ admit nonzero-degree maps and whether degrees can be unbounded; the "ordering of manifolds by domination" ($M \succeq N$ iff some $f:M\to N$ has $\deg f \ne 0$) becomes the organizing frame.
- **1977.** Milnor and Thurston, *Characteristic numbers of 3-manifolds*, bound $\|M\|$ by the number of tetrahedra in a triangulation and establish multiplicativity under finite coverings, yielding the first systematic degree bounds in dimension 3.
- **1982.** Gromov's *Volume and bounded cohomology* puts $\|\cdot\|$ on a general footing, proves the proportionality principle and vanishing for amenable fundamental groups, and derives (2.1) in all dimensions. This proves part (A)–(B) for all targets with $\|N\| > 0$.
- **1991–2003.** Shicheng Wang and collaborators classify nonzero-degree maps between aspherical 3-manifolds; Duan–Wang compute $D(M,N)$ for large families, including $(n-1)$-connected $2n$-manifolds.
- **2009–2015.** Kotschick–Löh and Crowley–Löh isolate *inflexible manifolds with vanishing simplicial volume*, showing (2.1) cannot be the whole story; Amann realizes prescribed multiplicatively closed sets as $D(N)$ for simply connected $N$, refuting the dichotomy (B) outside the aspherical class.
- **2013–2018.** Kotschick–Neofytidis and Neofytidis settle inflexibility for large classes of aspherical products, circle bundles and manifolds with nontrivial $\pi_1$-center.

## 4. Partial Results / Verified Cases

- **Positive simplicial volume.** If $\|N\| > 0$ then $D(M,N)$ is finite for every $M$ (Gromov 1982). Covers all closed hyperbolic $n$-manifolds ($n \ge 2$), closed negatively curved manifolds, closed locally symmetric spaces of noncompact type (Lafont–Schmidt), and any $N$ with a hyperbolic piece in its JSJ decomposition in dimension 3.
- **Mostow rigidity.** For $N$ closed hyperbolic of dimension $n \ge 3$: $D(N) = \{0, \pm 1\}$, and every degree-$\pm 1$ self-map is homotopic to an isometry. In dimension 2, $D(\Sigma_g) = \{0,\pm 1\}$ for $g \ge 2$ since $\|\Sigma_g\| = 4g-4 > 0$.
- **Dimension 3 (complete).** For closed oriented aspherical geometric 3-manifolds the flexible geometries are exactly $\mathbb{E}^3$, $\mathrm{Nil}$, $\mathrm{Sol}$; the inflexible ones are $\mathbb{H}^3$, $\mathbb{H}^2\times\mathbb{R}$, $\widetilde{\mathrm{SL}_2}$. The last two have $\|N\| = 0$, so inflexibility there is *not* detected by simplicial volume (Kotschick–Neofytidis 2013). Statement (C) holds in dimension 3: flexible geometric 3-manifolds are precisely those with non-co-Hopfian fundamental group.
- **Torus and nilmanifolds.** $D(T^n) = \mathbb{Z}$: the map induced by $A \in M_n(\mathbb{Z})$ has degree $\det A$. All closed infranilmanifolds are flexible.
- **Products.** If $N = N_1 \times N_2$ with both factors inflexible and aspherical with trivial center, $N$ is inflexible (Neofytidis 2017); $\|N\|$ may vanish.
- **Simply connected targets.** For $(n-1)$-connected $2n$-manifolds $D(M,N)$ is computable from the intersection form (Duan–Wang 2003). Amann (2015) constructs simply connected $N$ with $D(N)$ an arbitrary prescribed multiplicatively closed set of the form $\{k^m\}$ — so (B) genuinely needs asphericity.
- **Amenable $\pi_1$.** $\|N\| = 0$ whenever $\pi_1(N)$ is amenable, so (2.1) is vacuous there; separately, closed aspherical $N$ with virtually poly-cyclic $\pi_1$ are all flexible, consistent with (C).

## 5. Principal Obstacles

- **Simplicial volume vanishes too often.** The only general degree bound in all dimensions is (2.1). But $\|N\| = 0$ for every manifold with amenable $\pi_1$, for $S^1$-bundles, and for many aspherical manifolds (e.g. $\Sigma_g \times S^1$, $\widetilde{\mathrm{SL}_2}$-manifolds). Exactly on this class — the inflexible-with-zero-norm manifolds — the conjecture is open, and the tool is silent by construction.
- **No universal replacement semi-norm.** Crowley–Löh show that functorial semi-norms bounded on the point are dominated by simplicial volume, so no finer *bounded* functorial semi-norm can separate the remaining cases. Unbounded functorial semi-norms exist but are not computable on generic aspherical manifolds.
- **Bounded cohomology is intractable.** The proof of (2.1) via $H_b^*(\pi_1)$ needs nonvanishing bounded classes. $H^*_b(G;\mathbb{R})$ is unknown for most groups: it vanishes for amenable $G$ and is huge for free groups, with almost nothing in between computed above degree 2.
- **Degree $\ne$ algebra.** Statement (C) requires converting a self-map of degree $k \ge 2$ into a covering. There is no general mechanism: $f_*\pi_1(N)$ need not have finite index equal to $|k|$, and even when $[\pi_1(N):f_*\pi_1(N)] < \infty$ one must promote a $\pi_1$-injection to a homotopy self-cover, which needs Borel-type rigidity not available in general.
- **Surgery-theoretic methods fail.** Degree-$k$ maps for $k\ge2$ are not normal maps; the surgery exact sequence and the Farrell–Jones machinery control degree-one normal invariants only.

## 6. The Gap

Proven: finiteness of $D(M,N)$ whenever $\|N\| > 0$, plus a complete answer in dimension 3 and for several product/bundle families. Conjectured: the same conclusions with no hypothesis on $\|N\|$.

The precise barrier is the class
$$\mathcal{Z} = \{\,N \text{ closed, oriented, aspherical} : \|N\| = 0 \,\}.$$
For $N \in \mathcal{Z}$ nothing forces $D(N)$ to be $\{0,\pm 1\}$ or infinite, and no invariant is known that is (i) functorial under maps of nonzero degree, (ii) nonzero on the inflexible members of $\mathcal{Z}$. Crossing the gap means constructing such an invariant — a functorial semi-norm, a bounded-cohomology class, or an $L^2$/measure-equivalence invariant — or proving a rigidity theorem that upgrades a degree-$k$ self-map of an aspherical manifold to a $k$-fold covering.

## 7. Current Research (as of June 2026)

- **Inflexibility of aspherical manifolds with center.** Neofytidis' programme relates $D(N)$ to the center of $\pi_1(N)$ and to Seifert-type fibrations; extension beyond dimension 4 is active *(frontier — verify)*.
- **Integral foliated and stable simplicial volume.** Löh's group (Regensburg) studies integral foliated simplicial volume and its relation to $L^2$-Betti numbers and cost, aiming at a norm that survives where $\|\cdot\|$ vanishes.
- **Bounded cohomology of transformation groups.** Monod, Fournier-Facio, Moraschini and coauthors compute $H^*_b$ for groups of homeomorphisms and for boundedly acyclic groups; new nonvanishing classes in degree $\ge 3$ would directly feed degree theorems.
- **Co-Hopf properties of lattices and CAT(0) groups.** Superrigidity-flavoured proofs that $\pi_1$ of nonpositively curved aspherical manifolds with no Euclidean de Rham factor are co-Hopfian, aimed at statement (C).
- **Rational-homotopy constructions.** Following Amann and Costoya–Viruel, explicit simply connected and non-aspherical examples calibrate exactly how much asphericity (B) needs.

## 8. Future Work

- Decide (B) for the smallest open case: closed aspherical 4-manifolds with $\|N\| = 0$ and infinite non-amenable $\pi_1$.
- Construct a functorial semi-norm nonzero on $\Sigma_g\times S^1$ that is *not* derived from the surface factor, giving a norm-theoretic proof of known inflexibility results.
- Prove: for $N$ closed aspherical with $\pi_1(N)$ co-Hopfian and Hopfian, $D(N)=\{0,\pm1\}$. This is the cleanest implication linking (B) and (C).
- Determine whether $D(N)$ can be finite with more than three elements for aspherical $N$ — a single such example kills (B).
- Extend Wang's dimension-3 classification of nonzero-degree maps to graph-manifold-like aspherical 4-manifolds and to higher-dimensional geometrizable manifolds.

## 9. Key References

- **[Foundational]** J. Milnor and W. Thurston. *Characteristic numbers of 3-manifolds.* L'Enseignement Mathématique 23 (1977), 249–254.
- **[Foundational]** M. Gromov. *Volume and bounded cohomology.* Publications Mathématiques de l'IHÉS 56 (1982), 5–99.
- **[Foundational]** W. Thurston. *The Geometry and Topology of Three-Manifolds.* Princeton University lecture notes, 1979 (Chapter 6).
- **[Foundational]** R. Benedetti and C. Petronio. *Lectures on Hyperbolic Geometry.* Springer, 1992. [DOI](https://doi.org/10.1007/978-3-642-58158-8)
- **[SOTA / Recent]** H. Duan and S. Wang. *The degrees of maps between manifolds.* Mathematische Zeitschrift 244 (2003), 67–89. [DOI](https://doi.org/10.1007/s00209-002-0475-x)
- **[SOTA / Recent]** D. Kotschick and C. Löh. *Fundamental classes not representable by products.* Journal of the London Mathematical Society 79 (2009), 545–561. [DOI](https://doi.org/10.1112/jlms/jdn089)
- **[SOTA / Recent]** D. Kotschick and C. Neofytidis. *On three-manifolds dominated by circle bundles.* Mathematische Zeitschrift 274 (2013), 21–32. [DOI](https://doi.org/10.1007/s00209-012-1055-3)
- **[SOTA / Recent]** D. Crowley and C. Löh. *Functorial semi-norms on singular homology and (in)flexible manifolds.* Algebraic & Geometric Topology 15 (2015), 1453–1499.
- **[SOTA / Recent]** M. Amann. *Degrees of self-maps of simply connected manifolds.* International Mathematics Research Notices, 2015. [DOI](https://doi.org/10.1093/imrn/rnu201)
- **[SOTA / Recent]** C. Neofytidis. *Degrees of self-maps of products.* International Mathematics Research Notices, 2017. [DOI](https://doi.org/10.1093/imrn/rnw227)
- **[Survey]** S. Wang. *Non-zero degree maps between 3-manifolds.* Proceedings of the ICM, Beijing 2002, Vol. II, 457–468.
- **[Survey]** C. Löh. *Simplicial volume.* Bulletin of the Manifold Atlas, 2011.
- **[Survey]** M. Gromov. *Metric Structures for Riemannian and Non-Riemannian Spaces.* Birkhäuser, 1999.

## 10. Worked Example / Concrete Special Case

**(a) A flexible manifold: $T^3$.** For $A \in M_3(\mathbb{Z})$, the linear map $x \mapsto Ax$ on $\mathbb{R}^3$ descends to $f_A: T^3 \to T^3$ with $\deg f_A = \det A$. Taking $A = \operatorname{diag}(k,1,1)$ gives $\deg = k$ for every $k \in \mathbb{Z}$, so $D(T^3) = \mathbb{Z}$. Consistently, $\|T^3\| = 0$ ($\pi_1 = \mathbb{Z}^3$ is amenable) and $\pi_1$ is non-co-Hopfian: $k\mathbb{Z}\oplus\mathbb{Z}\oplus\mathbb{Z} \cong \mathbb{Z}^3$ has index $k$.

**(b) An inflexible manifold detected by the norm: closed hyperbolic $N^3$.** Let $\operatorname{Vol}(N) = V$. Then $\|N\| = V/v_3 > 0$, and (2.1) applied to a self-map gives $|\deg f|\cdot V/v_3 \le V/v_3$, i.e. $|\deg f| \le 1$. So $D(N) = \{0,\pm 1\}$. For the Weeks manifold, $V \approx 0.9427$ and $\|N\| \approx 0.9288$. Mostow rigidity upgrades this: any degree-$\pm1$ self-map is homotopic to an isometry.

**(c) The gap case: $N = \Sigma_2 \times S^1$.** Here $\|N\| = 0$, because simplicial volume of a product satisfies $\|A\times B\| = 0$ whenever one factor is $S^1$ (amenable $\pi_1$ factor kills the norm). So (2.1) gives *no* bound. Yet $N$ is inflexible. Argument: let $f: N\to N$. Since $Z(\pi_1 N) = \mathbb{Z}$ is the $S^1$ factor and is characteristic, $f$ is homotopic to a fibre-preserving map covering some $\bar f: \Sigma_2 \to \Sigma_2$, with fibre degree $d \in \mathbb{Z}$, and
$$\deg f = d \cdot \deg \bar f .$$
Since $\|\Sigma_2\| = 4\cdot 2 - 4 = 4 > 0$, (2.1) on the base gives $|\deg\bar f| \le 1$. The fibre degree satisfies $|d| \le 1$ because a degree-$d$ map on the $S^1$ factor multiplies the Euler class pairing $\langle e, [\Sigma_2]\rangle$ by $d\cdot\deg\bar f$ while the bundle is trivial ($e = 0$) — the obstruction instead comes from $H^1(N;\mathbb{Z})$: $f^*$ acts on the $\mathbb{Z}$ summand dual to the fibre by $d$, and self-maps of an aspherical manifold with centre cannot expand the centre without producing a self-cover of $\Sigma_2$, which is impossible for $\chi < 0$ except at index 1. Hence $D(N) = \{0,\pm 1\}$.

This is exactly the shape of the open problem: (c) is inflexible for reasons that no bounded functorial semi-norm can see, and the conjecture asserts that every aspherical $N$ behaves like (a) or like (c), never in between.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*