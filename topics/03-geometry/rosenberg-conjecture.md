---
id: 03-geometry/rosenberg-conjecture
title: "Rosenberg Conjecture"
topic: 03-geometry
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Rosenberg Conjecture

> **Topic:** Algebraic & Differential Geometry · **ID:** `03-geometry/rosenberg-conjecture` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Also called the **Gromov–Lawson–Rosenberg (GLR) conjecture**. Let $M$ be a closed connected spin manifold of dimension $n \ge 5$, let $\pi = \pi_1(M)$, and let $u \colon M \to B\pi$ classify the universal cover. Rosenberg's index

$$\alpha(M,u) \;\in\; KO_n\!\left(C^*_r \pi ; \mathbb{R}\right)$$

is the $KO$-valued index of the Dirac operator of $M$ twisted by the Mishchenko–Fomenko bundle over the real reduced group $C^*$-algebra.

**Conjecture (Rosenberg, 1983/86).** $M$ admits a Riemannian metric of positive scalar curvature (psc) **if and only if** $\alpha(M,u) = 0$.

The "only if" direction is a theorem (Rosenberg 1983), a $C^*$-algebraic upgrade of Lichnerowicz's vanishing argument. The conjectural content is **sufficiency**: vanishing of the index is the *only* obstruction. A disproof means exhibiting one pair $(M,u)$ with $\alpha(M,u)=0$ and no psc metric; a proof means a construction producing a psc metric from index-theoretic vanishing, for every group $\pi$.

Current status: the unstable statement above is **false in general** (Schick 1998), true for large classes of $\pi$, and its Bott-stabilised form (the Stolz conjecture) remains open and is the live problem.

## 2. Mathematical Foundations

**Scalar curvature.** For $(M,g)$, $\mathrm{scal}_g = \sum_{i,j} \langle R(e_i,e_j)e_j, e_i\rangle$; psc means $\mathrm{scal}_g > 0$ pointwise.

**Lichnerowicz formula.** On a spin manifold with spinor bundle $S$ and Dirac operator $D$,
$$D^2 \;=\; \nabla^*\nabla \;+\; \tfrac{1}{4}\,\mathrm{scal}_g .$$
If $\mathrm{scal}_g>0$ then $\ker D = 0$, so every index of $D$ vanishes.

**The $\alpha$-invariant.** Real Clifford-linear index theory (Atiyah–Bott–Shapiro) gives a ring homomorphism
$$\alpha \colon \Omega^{\mathrm{spin}}_n \longrightarrow KO_n(\mathrm{pt}) = KO_{-n}(\mathbb{R}),\qquad
KO_n(\mathbb{R}) \cong \mathbb{Z},\,\mathbb{Z}/2,\,\mathbb{Z}/2,\,0,\,\mathbb{Z},\,0,\,0,\,0$$
for $n \equiv 0,1,\dots,7 \bmod 8$. For $n \equiv 0 \bmod 4$, $\alpha(M) = \hat{A}(M)$ up to a factor of $2$ in dimensions $\equiv 4 \bmod 8$.

**Rosenberg index.** Let $\mathcal{L} = \widetilde{M} \times_\pi C^*_r\pi$ be the flat bundle of finitely generated projective $C^*_r\pi$-modules. Then $D_{\mathcal{L}}$ is $C^*_r\pi$-linear elliptic, with Mishchenko–Fomenko index $\alpha(M,u) \in KO_n(C^*_r\pi)$. It is a spin-bordism invariant, so factors through
$$\Omega^{\mathrm{spin}}_n(B\pi) \xrightarrow{\;D\;} ko_n(B\pi) \xrightarrow{\;\text{per}\;} KO_n(B\pi) \xrightarrow{\;\mu\;} KO_n(C^*_r\pi),$$
where $\mu$ is the real Baum–Connes assembly map. The Lichnerowicz argument, applied to $D_\mathcal{L}$, gives $\mathrm{psc} \Rightarrow \alpha(M,u)=0$.

**Surgery input.** Gromov–Lawson and Schoen–Yau: psc is preserved under surgeries of codimension $\ge 3$. Hence psc is a property of the class $[M,u] \in \Omega^{\mathrm{spin}}_n(B\pi)$ modulo the subgroup $\Omega^{\mathrm{spin},+}_n(B\pi)$ of classes represented by psc manifolds, for $n\ge 5$. The conjecture is therefore equivalent to
$$\Omega^{\mathrm{spin},+}_n(B\pi) \;=\; \ker\!\left(\Omega^{\mathrm{spin}}_n(B\pi) \xrightarrow{\ \alpha\ } KO_n(C^*_r\pi)\right).$$

**Bott stabilisation.** Fix a Bott manifold $B^8$: a simply connected spin $8$-manifold with $\hat{A}(B)=1$. The **stable (Stolz) conjecture** asserts $M$ admits psc after taking a product with sufficiently many copies of $B$ iff $\alpha(M,u)=0$.

## 3. History & State of the Art (SOTA)

- **1963.** Lichnerowicz: $\mathrm{scal}>0$ and spin $\Rightarrow \hat{A}(M)=0$.
- **1974.** Hitchin (*Harmonic spinors*): refines the obstruction to $KO$, producing exotic spheres in dimensions $8k+1, 8k+2$ with no psc metric.
- **1979–1980.** Schoen–Yau (minimal hypersurface method) and Gromov–Lawson (surgery) establish the two rival technologies; the $n$-torus $T^n$ carries no psc metric.
- **1983–1986.** Rosenberg, *$C^*$-algebras, positive scalar curvature and the Novikov conjecture* (I, II, III): defines $\alpha(M,u)$ and formulates the conjecture, linking psc to the Novikov and Baum–Connes conjectures.
- **1992.** Stolz proves the simply connected case in dimensions $\ge 5$: psc $\iff \alpha(M)=0$.
- **1995–1997.** Rosenberg–Stolz reduce the stable version to Baum–Connes; Botvinnik–Gilkey–Stolz prove GLR for finite groups with periodic cohomology.
- **1998.** Schick disproves the unstable conjecture with $\pi = \mathbb{Z}/3 \times \mathbb{Z}^4$ in dimension $5$.
- **2003.** Dwyer–Schick–Stolz produce further counterexamples, including totally non-spin ones, in higher dimensions.
- **2015–2024.** Codimension-two and submanifold obstructions (Hanke–Pape–Schick; Zeidler); minimal-surface and $\mu$-bubble methods (Chodosh–Li; Brendle–Hirsch–Johne) settle the aspherical (Schoen–Yau/Gromov) case in dimensions $\le 5$ (and to $7$ under hypotheses) — results consistent with, but not proving, the index-theoretic picture.

## 4. Partial Results / Verified Cases

Cases where the (unstable) conjecture is **proved**:

- **$\pi = 1$, $n \ge 5$** — Stolz (1992). Combined with Hitchin: psc $\iff \alpha=0$ exactly.
- **Finite groups with periodic cohomology** (cyclic groups, generalized quaternion, spherical space form groups), $n \ge 5$ — Botvinnik–Gilkey–Stolz (1997).
- **$\pi = \mathbb{Z}^n$**, free groups, and surface groups — Rosenberg–Stolz; here $\mu$ is injective and $ko_*(B\pi) \to KO_*(B\pi)$ is understood.
- **Totally non-spin manifolds** (non-spin universal cover) with $\pi$ in the classes above: $\alpha$ is trivially zero and psc always exists, $n\ge5$.
- **Elementary abelian $2$-groups and some small $p$-groups** — Botvinnik–Gilkey and Joachim–Schick (2000), case-by-case $ko_*(B\pi)$ computations.
- **Stable version**: holds for every $\pi$ for which the real Baum–Connes assembly map is injective (Rosenberg–Stolz 1995; Stolz). That covers a-T-menable groups, hyperbolic groups, and many others.

Cases where it **fails**:

- $\pi = \mathbb{Z}/3 \times \mathbb{Z}^4$, $n = 5$ (Schick 1998).
- Infinitely many further groups and dimensions $n \ge 5$ (Dwyer–Schick–Stolz 2003).
- Dimension $4$ is outside the conjecture's scope: Seiberg–Witten invariants obstruct psc on spin $4$-manifolds with $\alpha = 0$ (e.g. suitable minimal surfaces of general type).

## 5. Principal Obstacles

- **Bordism-to-geometry gap.** Surgery only shows psc is a bordism-invariant property in $\Omega^{\mathrm{spin}}_*(B\pi)$; deciding whether a given class contains a psc representative needs the full computation of $\Omega^{\mathrm{spin}}_*(B\pi)$ and of the image of $\alpha$. For most infinite groups $ko_*(B\pi)$ is not computable.
- **Failure of $ko \to KO \to C^*$.** The composite loses information: classes in $\ker\alpha$ can survive as genuine obstructions coming from the non-connective/assembly gap. Schick's counterexample is exactly a $ko$-theory class in $\ker\mu$ that is not psc-representable — the reason "index theory sees everything" fails.
- **No non-index obstruction theory.** All known obstructions in dimensions $\ge 5$ are index-theoretic (Dirac, Callias, codimension-2 descent) or minimal-surface based. The Schoen–Yau method needs regularity of minimal hypersurfaces and historically stalled above dimension $7$; $\mu$-bubbles have pushed it but not to arbitrary dimension.
- **Torsion.** Counterexamples require torsion in $\pi$ interacting with a free part: $\mathbb{Z}/3$ alone is fine, $\mathbb{Z}^4$ alone is fine, the product is not. No structural criterion separates the good products from the bad ones.
- **Baum–Connes dependence.** The stable statement is only as strong as the injectivity of $\mu$, itself an open problem for general groups; and counterexamples to Baum–Connes surjectivity (Higson–Lafforgue–Skandalis) show the frame is delicate.

## 6. The Gap

Proven: sufficiency of $\alpha$ for $\pi=1$ and for a list of groups with computable $ko_*(B\pi)$; necessity for all $\pi$; the stable statement modulo Baum–Connes injectivity.

Not proven, and the precise boundary:

1. **Identify the correct invariant.** Since $\alpha$ is incomplete, one must find a functor $\mathcal{O}(M,u)$, refining the Rosenberg index, whose vanishing is equivalent to psc. Candidates live in the homotopy of the Stolz positive-scalar-curvature spectrum, but no computable model exists.
2. **Bridge $ko$ vs $KO$.** Schick-type counterexamples live in the kernel of periodicity $ko_n(B\pi) \to KO_n(B\pi)$ composed with assembly. Determining exactly which of these kernel elements are psc-representable — i.e. computing $\Omega^{\mathrm{spin},+}_*(B\pi)$ as a functor of $\pi$ — is the open step.
3. **Stable conjecture for all $\pi$.** Prove (or refute) that $M \times B^{8k}$ carries psc when $\alpha(M,u)=0$, without assuming Baum–Connes.

## 7. Current Research (as of June 2026)

- **Secondary and higher index invariants.** $\rho$-invariants, the Higson–Roe surgery exact sequence, and index maps into $K_*(D^*\pi)$ are used to distinguish psc metrics and to obstruct psc where $\alpha$ vanishes (Zeidler; Xie–Yu; Weinberger–Yu). Groups at Münster, Göttingen, Texas A&M, Fudan.
- **Codimension-2 and submanifold obstructions.** Hanke–Pape–Schick and successors: an incompressible codimension-2 submanifold with nonzero index obstructs psc on the ambient manifold — obstructions genuinely not captured by $\alpha(M,u)$. This is the most direct attack on the incompleteness identified in §6. *(frontier — verify: full classification of which counterexamples are explained this way.)*
- **$\mu$-bubbles and geometric methods.** Chodosh–Li, Brendle–Hirsch–Johne, Gromov's school: aspherical manifolds in low dimensions admit no psc metric, independent of index theory; extension beyond dimension $7$ is active. *(frontier — verify)*
- **Spectra and moduli.** Botvinnik–Ebert–Randal-Williams and successors compute homotopy of $\mathcal{R}^+(M)$, the space of psc metrics, giving structural input to the existence question.

## 8. Future Work

- Determine whether the **stable/Stolz conjecture** holds unconditionally; a counterexample would sever psc from Baum–Connes entirely.
- Compute $\Omega^{\mathrm{spin},+}_*(B\pi)$ for one infinite family of "bad" groups (e.g. $\mathbb{Z}/p \times \mathbb{Z}^k$) to give a complete answer in dimension $5$.
- Formulate GLR for the **Stolz spectrum** so that all known obstructions (Rosenberg index, codimension-2, $\rho$) are values of a single natural transformation.
- Extend $\mu$-bubble techniques to all dimensions, giving a non-spin, non-index route to obstructions.
- Settle dimension $4$ separately: classify spin $4$-manifolds with $\alpha=0$ and no psc.

## 9. Key References

- **[Foundational]** A. Lichnerowicz. *Spineurs harmoniques.* C. R. Acad. Sci. Paris 257 (1963), 7–9.
- **[Foundational]** N. Hitchin. *Harmonic spinors.* Advances in Mathematics 14 (1974), 1–55.
- **[Foundational]** M. Gromov, H. B. Lawson. *The classification of simply connected manifolds of positive scalar curvature.* Annals of Mathematics 111 (1980), 423–434.
- **[Foundational]** R. Schoen, S.-T. Yau. *On the structure of manifolds with positive scalar curvature.* Manuscripta Mathematica 28 (1979), 159–183.
- **[Foundational]** J. Rosenberg. *$C^*$-algebras, positive scalar curvature, and the Novikov conjecture.* Publications Mathématiques de l'IHÉS 58 (1983), 197–212. (Parts II and III: Geometric Methods in Operator Algebras, 1986; Topology 25 (1986), 319–336.)
- **[SOTA]** S. Stolz. *Simply connected manifolds of positive scalar curvature.* Annals of Mathematics 136 (1992), 511–540.
- **[SOTA]** J. Rosenberg, S. Stolz. *A "stable" version of the Gromov–Lawson conjecture.* Contemporary Mathematics 181 (1995), 405–418.
- **[SOTA]** B. Botvinnik, P. Gilkey, S. Stolz. *The Gromov–Lawson–Rosenberg conjecture for groups with periodic cohomology.* Journal of Differential Geometry 46 (1997), 374–405.
- **[SOTA]** T. Schick. *A counterexample to the (unstable) Gromov–Lawson–Rosenberg conjecture.* Topology 37 (1998), 1165–1168.
- **[SOTA]** W. Dwyer, T. Schick, S. Stolz. *Remarks on a conjecture of Gromov and Lawson.* In: High-Dimensional Manifold Topology, World Scientific, 2003, 159–176.
- **[SOTA]** B. Hanke, D. Pape, T. Schick. *Codimension two index obstructions to positive scalar curvature.* Annales de l'Institut Fourier 65 (2015), 2681–2710.
- **[SOTA]** O. Chodosh, C. Li. *Generalized soap bubbles and the topology of manifolds with positive scalar curvature.* Annals of Mathematics 199 (2024), 707–740.
- **[Survey]** J. Rosenberg. *Manifolds of positive scalar curvature: a progress report.* Surveys in Differential Geometry 11 (2007), 259–294.
- **[Survey]** J. Rosenberg, S. Stolz. *Metrics of positive scalar curvature and connections with surgery.* In: Surveys on Surgery Theory, Vol. 2, Annals of Mathematics Studies 149, Princeton University Press, 2001.
- **[Survey]** T. Schick. *The topology of positive scalar curvature.* Proceedings of the ICM, Seoul, 2014, Vol. II, 1285–1307.

## 10. Worked Example / Concrete Special Case

**Simply connected case in dimension $9$ — the conjecture verified, with a nontrivial obstruction.**

Take $\pi = 1$, so $C^*_r\pi = \mathbb{R}$ and $\alpha(M,u)$ reduces to the classical $\alpha$-invariant with values in
$$KO_9(\mathbb{R}) \cong \mathbb{Z}/2 \qquad (9 \equiv 1 \bmod 8).$$

*Step 1 — the obstruction is nonzero on some homotopy sphere.* Hitchin (1974) showed the composite $\Theta_9 \to \Omega^{\mathrm{spin}}_9 \xrightarrow{\alpha} \mathbb{Z}/2$ is surjective: there is an exotic $9$-sphere $\Sigma^9$ with $\alpha(\Sigma^9) = 1$. Concretely, the generator of $KO_1(\mathbb{R})=\mathbb{Z}/2$ is detected by the mod-2 dimension of the kernel of the Clifford-linear Dirac operator, $\dim_{\mathbb{R}} \ker D \bmod 2$. Since $\Sigma^9$ is a homotopy sphere all Pontryagin numbers vanish and $\hat{A}$ gives nothing; the $KO$ refinement is essential.

*Step 2 — apply Lichnerowicz.* If $g$ were a psc metric on $\Sigma^9$, then $D^2 = \nabla^*\nabla + \tfrac14\mathrm{scal}_g$ forces $\ker D = 0$, hence $\alpha(\Sigma^9) = 0$. Contradiction: $\Sigma^9$ carries no psc metric, even though it is homeomorphic to $S^9$, which carries the round metric with $\mathrm{scal} = 72$.

*Step 3 — converse via Stolz.* For $M$ simply connected spin of dimension $9$ with $\alpha(M)=0$, Stolz's theorem gives a psc metric. The proof: $\ker \alpha \subset \Omega^{\mathrm{spin}}_9$ is generated by total spaces of $\mathbb{HP}^2$-bundles; such total spaces carry psc metrics by a fibrewise argument, and the Gromov–Lawson surgery theorem transports psc across the bordism (all surgeries have codimension $\ge 3$ since $9 \ge 5$ and $M$ is simply connected).

*Conclusion for this case.* In dimension $9$ with $\pi = 1$:
$$\Sigma^9 \text{ admits psc} \iff \alpha(\Sigma^9) = 0 \in \mathbb{Z}/2 .$$
Among the $\Theta_9 \cong (\mathbb{Z}/2)^3$ homotopy $9$-spheres, exactly the index-two subgroup $\ker\alpha$ (four spheres, including $S^9$) admits psc; the other four do not.

*Where this breaks.* Replace $\pi = 1$ by $\pi = \mathbb{Z}/3\times\mathbb{Z}^4$ and $n=9$ by $n=5$. Schick's construction produces $(M,u)$ with $\alpha(M,u)=0$ in $KO_5(C^*_r\pi)$ — the class dies under $ko_5(B\pi)\to KO_5(B\pi)\xrightarrow{\mu}KO_5(C^*_r\pi)$ — yet $M$ carries no psc metric, obstructed by a codimension-two/Toda-bracket argument invisible to $\alpha$. Step 3 has no analogue: $\Omega^{\mathrm{spin},+}_5(B\pi)$ is strictly smaller than $\ker\alpha$.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*