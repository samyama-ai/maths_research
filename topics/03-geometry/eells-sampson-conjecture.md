---
id: 03-geometry/eells-sampson-conjecture
title: "Eells-Sampson Conjecture"
topic: 03-geometry
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Eells–Sampson Conjecture (Biharmonic Maps into Non-Positively Curved Targets)

> **Topic:** Algebraic & Differential Geometry · **ID:** `03-geometry/eells-sampson-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Let $(M^m,g)$ and $(N^n,h)$ be Riemannian manifolds and let $\phi:M\to N$ be a smooth map. $\phi$ is **biharmonic** if it is a critical point of the bienergy $E_2(\phi)=\tfrac12\int_M|\tau(\phi)|^2\,v_g$, where $\tau(\phi)=\operatorname{trace}_g\nabla d\phi$ is the tension field. Harmonic maps ($\tau(\phi)=0$) are trivially biharmonic; a biharmonic map that is not harmonic is called **proper biharmonic**.

**Eells–Sampson Conjecture.** *If $(M,g)$ is complete and $(N,h)$ has non-positive sectional curvature, then every biharmonic map $\phi:M\to N$ is harmonic.*

The submanifold specialisation — every biharmonic isometric immersion into a non-positively curved manifold is minimal — is the **generalised Chen conjecture**; the case $N=\mathbb{R}^n$ is **Chen's conjecture** (1988).

Status of the general statement: **false as stated**. Ou–Tang (2012) built proper biharmonic hypersurfaces inside a 5-dimensional conformally flat manifold of *strictly negative* sectional curvature. What remains open, and what "the conjecture" now means in practice, is:

- **(ES-1)** $N$ a space form of non-positive constant curvature: $N=\mathbb{R}^n$ (Chen) or $N=\mathbb{H}^n$, $M$ complete. Open in every dimension $n\ge 6$.
- **(ES-2)** $M$ complete, $\operatorname{Riem}^N\le 0$, with *no* auxiliary finiteness hypothesis on $E(\phi)$, $E_2(\phi)$ or $\int|\tau|^p$.

A complete resolution requires either a proof of (ES-1)/(ES-2) or a proper biharmonic example with complete domain and constant-curvature non-positive target.

## 2. Mathematical Foundations

**Tension and bitension.** For $\phi:(M,g)\to(N,h)$, with $\nabla^\phi$ the pullback connection on $\phi^{-1}TN$ and $\{e_i\}$ a local orthonormal frame,
$$\tau(\phi)=\sum_{i=1}^m\big(\nabla^\phi_{e_i}d\phi(e_i)-d\phi(\nabla_{e_i}e_i)\big).$$
The first variation of $E_2$ (Jiang, 1986) gives the Euler–Lagrange operator
$$\tau_2(\phi)\;=\;-\Delta^\phi\tau(\phi)\;-\;\sum_{i=1}^m R^N\!\big(d\phi(e_i),\tau(\phi)\big)d\phi(e_i)\;=\;0,$$
where $\Delta^\phi=-\sum_i\big(\nabla^\phi_{e_i}\nabla^\phi_{e_i}-\nabla^\phi_{\nabla_{e_i}e_i}\big)$ is the (non-negative) rough Laplacian and $R^N(X,Y)=\nabla_X\nabla_Y-\nabla_Y\nabla_X-\nabla_{[X,Y]}$. This is a fourth-order, quasilinear, *non-uniformly-coercive* elliptic system.

**The Bochner identity.** Writing $\Delta=\operatorname{div}\operatorname{grad}$ on $M$, biharmonicity gives
$$\tfrac12\Delta|\tau(\phi)|^2=|\nabla^\phi\tau(\phi)|^2-\sum_{i=1}^m\big\langle R^N\!\big(d\phi(e_i),\tau(\phi)\big)d\phi(e_i),\,\tau(\phi)\big\rangle .$$
If $\operatorname{Riem}^N\le0$ the curvature term is $\ge0$, so $|\tau(\phi)|^2$ is **subharmonic**. This single inequality drives essentially all positive results.

**Hypersurface reduction.** For an isometric immersion $M^m\hookrightarrow N^{m+1}(c)$ into a space form of constant curvature $c$, with unit normal $\eta$, shape operator $A$ and mean curvature $H=\tfrac1m\operatorname{trace}A$, biharmonicity is equivalent to the system (Ou, 2010)
$$\Delta H \;=\; H\big(|A|^2-mc\big),\qquad\quad A(\operatorname{grad}H)\;=\;-\tfrac{m}{2}\,H\operatorname{grad}H .$$
For $c\le 0$ and $H$ constant the first equation forces $H(|A|^2-mc)=0$, hence $H=0$; the difficulty is entirely in the non-CMC case.

## 3. History & State of the Art (SOTA)

- **1964.** Eells and Sampson introduce harmonic maps and prove the heat-flow existence theorem for $\operatorname{Riem}^N\le0$ (*Amer. J. Math.* **86**). In the same circle of ideas they propose *polyharmonic* maps and observe that on a **compact** domain with $\operatorname{Riem}^N\le0$ biharmonic $\Rightarrow$ harmonic.
- **1983.** Eells–Lemaire's CBMS report lists the study of $k$-polyharmonic maps as Problem (4.4), fixing the problem in the literature.
- **1986.** G.Y. Jiang computes the first and second variation of $E_2$ and writes $\tau_2$ explicitly; the modern theory starts here.
- **1988–91.** B.-Y. Chen, from finite-type submanifold theory, conjectures that biharmonic submanifolds of $\mathbb{R}^n$ ($\Delta \vec H=0$) are minimal.
- **2001–2010.** Caddeo–Montaldo–Oniciuc settle low-dimensional space-form cases; Balmuş–Montaldo–Oniciuc settle 4-dimensional space forms; Ou derives the hypersurface system above.
- **2012.** Ou–Tang produce proper biharmonic hypersurfaces in a negatively curved 5-manifold — the generalised conjecture is false.
- **2011–2014.** Nakauchi–Urakawa, Baird–Fardoun–Ouakkas, Maeta, Alías–García-Martínez–Rigoli prove the conjecture for complete domains **under integrability or curvature side conditions**.
- **2021.** Fu–Hong–Zhan prove Chen's conjecture for hypersurfaces of $\mathbb{R}^5$ (*Adv. Math.*), the current dimensional frontier.

## 4. Partial Results / Verified Cases

**Compact domain.** $M$ compact, $\operatorname{Riem}^N\le0$: biharmonic $\Rightarrow$ harmonic (Eells–Sampson 1964; Jiang 1986). Also true if $M$ is complete and $\operatorname{Vol}(M)=\infty$ with $\int_M|\tau(\phi)|^2<\infty$ (Nakauchi–Urakawa–Gudmundsson, 2014).

**Finiteness hypotheses (complete $M$, $\operatorname{Riem}^N\le0$).**
- $E(\phi)<\infty$ and $E_2(\phi)<\infty$ $\Rightarrow$ harmonic (Nakauchi–Urakawa–Gudmundsson, *Geom. Dedicata* 2014).
- $\operatorname{Ric}^M\ge0$ and $E_2(\phi)<\infty$ $\Rightarrow$ harmonic (Baird–Fardoun–Ouakkas, 2008).
- $\int_M|\tau(\phi)|^p\,v_g<\infty$ for some $1<p<\infty$, plus $E(\phi)<\infty$ $\Rightarrow$ harmonic (Maeta, *Ann. Global Anal. Geom.* 2014).

**Chen's conjecture ($N=\mathbb{R}^n$), confirmed classes.**
- Curves in $\mathbb{R}^n$ and, more generally, submanifolds of finite type (Dimitrić, 1992).
- Surfaces in $\mathbb{R}^3$ (Chen; Jiang, 1987).
- Hypersurfaces with at most two distinct principal curvatures, any dimension (Dimitrić, 1992).
- Hypersurfaces in $\mathbb{R}^4$ (Hasanis–Vlachos, 1995; Defever, 1998).
- Hypersurfaces in $\mathbb{R}^5$ (Fu, three principal curvatures, 2015; Fu–Hong–Zhan, full case, *Adv. Math.* 2021).
- Pseudo-umbilical $M^m\subset\mathbb{R}^n$ with $m\ne4$ (Dimitrić).
- $\varepsilon$-superbiharmonic submanifolds (Wheeler, 2013).

**Hyperbolic ambient.** Biharmonic surfaces in $\mathbb{H}^3$ are minimal (Caddeo–Montaldo–Oniciuc, 2001); hypersurfaces in 4-dimensional space forms with $c\le0$ are minimal (Balmuş–Montaldo–Oniciuc, 2010). CMC biharmonic hypersurfaces in $\mathbb{H}^{n}$ are minimal for all $n$ (immediate from §2). Weakly convex ($A\ge0$) complete biharmonic hypersurfaces in $\mathbb{R}^n,\mathbb{H}^n$ are minimal (Luo, 2014).

**Negative result.** Ou–Tang (2012): $\big(\mathbb{R}^5_{+},\,x_5^{-2\alpha}\delta\big)$-type conformally flat metrics with negative sectional curvature carry proper biharmonic hypersurfaces — no constant-curvature counterexample is known.

## 5. Principal Obstacles

- **No maximum principle without volume/energy control.** Subharmonicity of $|\tau|^2$ closes the argument only when a Liouville-type theorem applies. On a complete non-compact $M$ with unbounded geometry, $|\tau|^2$ may be subharmonic, positive and non-constant; Yau-type $L^p$ Liouville theorems need exactly the finiteness assumptions one wants to remove. This is the whole content of gap (ES-2).
- **Fourth order kills the standard toolkit.** $\tau_2$ has no maximum principle in the second-order sense, no comparison principle, and the associated flow has no known monotonicity formula strong enough for classification. Second-order methods (Bochner, Simons-type identities) apply only after $|\tau|^2$ is already controlled.
- **Non-CMC hypersurfaces.** The system in §2 forces $\operatorname{grad}H$ to be a principal direction with eigenvalue $-\tfrac m2 H$. Classification proceeds by counting distinct principal curvatures and running a Codazzi-based ODE analysis on the level sets of $H$. The combinatorial complexity of the resulting connection coefficients grows sharply with the number of distinct principal curvatures — the reason $\mathbb{R}^5$ (up to four curvatures) took until 2021 and $\mathbb{R}^6$ is out of reach.
- **Curvature rigidity is not exploited.** Ou–Tang's counterexample shows that $\operatorname{Riem}^N\le0$ alone is insufficient. Any proof of (ES-1) must use *constancy* of the curvature (i.e. the ambient Codazzi/Gauss equations), yet no current technique isolates the difference between $\operatorname{Riem}\le0$ and $\operatorname{Riem}\equiv c\le0$ in the fourth-order setting.
- **No known variational characterisation.** Proper biharmonic maps are saddle points of $E_2$; there is no index or stability theory that rules them out on non-compact domains.

## 6. The Gap

Proven: compactness of $M$, or completeness plus one of $\{E<\infty,\;E_2<\infty,\;\|\tau\|_{L^p}<\infty,\;\operatorname{Ric}^M\ge0,\;A\ge0\}$, or low ambient dimension ($\le5$ for $\mathbb{R}^n$, $\le4$ for $\mathbb{H}^n$).

Missing, precisely:

1. **A Liouville theorem for subharmonic $|\tau|^2$ on a complete manifold with no volume growth or energy hypothesis.** Equivalently: rule out a complete biharmonic $\phi$ with $|\tau(\phi)|$ unbounded and infinite bienergy.
2. **A classification of non-CMC biharmonic hypersurfaces in $\mathbb{R}^n$, $\mathbb{H}^n$ for $n\ge6$**, i.e. a dimension-free argument replacing the principal-curvature case analysis. Every proof to date is dimension-specific.

Crossing either barrier for space forms settles (ES-1); crossing (1) in general curvature would contradict Ou–Tang, so (1) must itself be constant-curvature-specific.

## 7. Current Research (as of June 2026)

- **Hypersurface classification in $\mathbb{R}^6$ and $\mathbb{H}^6$** — the direct continuation of Fu–Hong–Zhan, pursued by Y. Fu (Dalian) and collaborators, and by Ou (Texas A&M–Commerce). Progress is reported under extra hypotheses (constant scalar curvature, constant $|A|^2$, three or four distinct principal curvatures). *(frontier — verify)*
- **Integrability-condition removal.** Groups around Urakawa/Nakauchi (Japan) and Maeta continue to weaken the $L^p$ hypotheses toward polynomial-volume-growth conditions. *(frontier — verify)*
- **Omori–Yau / Ekeland methods.** Alías, García-Martínez and Rigoli's approach — replacing compactness by a weak maximum principle on complete manifolds with controlled curvature — remains the most promising route to (ES-2) under geometric rather than analytic side conditions.
- **Biconservative geometry.** Studying the weaker condition $\langle\tau_2,d\phi\rangle=0$ (biconservative submanifolds; Montaldo–Oniciuc–Ratto, Nistor) as an intermediate classification problem.
- **Broader counterexample search.** Deforming Ou–Tang's conformally flat metrics toward constant curvature to locate the exact curvature threshold at which proper biharmonic examples disappear. *(frontier — verify)*

## 8. Future Work

- Prove a Liouville theorem: on a complete $M$ with $\operatorname{Vol}(B_r)\le Ce^{ar}$, a non-negative subharmonic $|\tau|^2$ satisfying the *biharmonic* system (not merely $\Delta|\tau|^2\ge0$) is constant. Using the full fourth-order structure, rather than just the Bochner inequality, is the recommended step.
- Develop a curvature-flow or blow-up analysis for $E_2$ on non-compact domains with an $\varepsilon$-regularity theorem, giving compactness independent of dimension.
- Find a dimension-free integral (Simons-type) identity for the shape operator of a biharmonic hypersurface in a space form that closes without enumerating principal curvatures.
- Determine sharp curvature-pinching: for which $-b^2\le K_N\le -a^2$ do proper biharmonic immersions exist? Ou–Tang gives existence for some non-constant $K_N<0$; a threshold theorem would delimit the true conjecture.

## 9. Key References

- **[Foundational]** J. Eells, J. H. Sampson. *Harmonic Mappings of Riemannian Manifolds.* American Journal of Mathematics **86** (1964), 109–160.
- **[Foundational]** J. Eells, L. Lemaire. *Selected Topics in Harmonic Maps.* CBMS Regional Conference Series in Mathematics 50, American Mathematical Society, 1983.
- **[Foundational]** G. Y. Jiang. *2-harmonic maps and their first and second variational formulas.* Chinese Annals of Mathematics Ser. A **7** (1986), 389–402.
- **[Foundational]** B.-Y. Chen. *Some open problems and conjectures on submanifolds of finite type.* Soochow Journal of Mathematics **17** (1991), 169–188.
- **[Key case]** T. Hasanis, T. Vlachos. *Hypersurfaces in $E^4$ with harmonic mean curvature vector field.* Mathematische Nachrichten **172** (1995), 145–169.
- **[Key case]** R. Caddeo, S. Montaldo, C. Oniciuc. *Biharmonic submanifolds of $\mathbb{S}^3$.* International Journal of Mathematics **12** (2001), 867–876.
- **[Key case]** A. Balmuş, S. Montaldo, C. Oniciuc. *Classification results for biharmonic submanifolds in spheres.* Israel Journal of Mathematics **168** (2008), 201–220.
- **[Structure]** Y.-L. Ou. *Biharmonic hypersurfaces in Riemannian manifolds.* Pacific Journal of Mathematics **248** (2010), 217–232.
- **[Counterexample]** Y.-L. Ou, L. Tang. *On the generalized Chen's conjecture on biharmonic submanifolds.* Michigan Mathematical Journal **61** (2012), 531–542.
- **[SOTA]** N. Nakauchi, H. Urakawa, S. Gudmundsson. *Biharmonic maps into a Riemannian manifold of non-positive curvature.* Geometriae Dedicata **169** (2014), 263–272.
- **[SOTA]** S. Maeta. *Biharmonic maps from a complete Riemannian manifold into a non-positively curved manifold.* Annals of Global Analysis and Geometry **46** (2014), 75–85.
- **[SOTA]** L. J. Alías, S. C. García-Martínez, M. Rigoli. *Biharmonic hypersurfaces in complete Riemannian manifolds.* Pacific Journal of Mathematics **263** (2013), 1–12.
- **[SOTA]** Y. Fu, M.-C. Hong, X. Zhan. *On Chen's biharmonic conjecture for hypersurfaces in $\mathbb{R}^5$.* Advances in Mathematics **383** (2021), 107697.
- **[Survey]** S. Montaldo, C. Oniciuc. *A short survey on differential geometry of biharmonic maps.* Revista de la Unión Matemática Argentina **47** (2006), 1–22.
- **[Survey / Book]** Y.-L. Ou, B.-Y. Chen. *Biharmonic Submanifolds and Biharmonic Maps in Riemannian Geometry.* World Scientific, 2020.

## 10. Worked Example / Concrete Special Case

**(a) The compact case, in full.** Let $M$ be compact, $\operatorname{Riem}^N\le0$, $\tau_2(\phi)=0$. By the Bochner identity of §2, $\tfrac12\Delta|\tau|^2\ge|\nabla^\phi\tau|^2\ge0$. Integrating over the closed manifold $M$, $\int_M\Delta|\tau|^2=0$, hence
$$\int_M|\nabla^\phi\tau(\phi)|^2\,v_g\le0\quad\Longrightarrow\quad \nabla^\phi\tau(\phi)\equiv0 .$$
Now define the vector field $X$ on $M$ by $\langle X,Y\rangle_g=\langle d\phi(Y),\tau(\phi)\rangle_h$. Then
$$\operatorname{div}X=\sum_i\big\langle \nabla^\phi_{e_i}d\phi(e_i)-d\phi(\nabla_{e_i}e_i),\tau\big\rangle+\sum_i\big\langle d\phi(e_i),\nabla^\phi_{e_i}\tau\big\rangle=|\tau(\phi)|^2+0 .$$
The divergence theorem gives $\int_M|\tau(\phi)|^2=0$, so $\tau(\phi)=0$: $\phi$ is harmonic. **Both steps use compactness**, and this is exactly what fails in general.

**(b) A concrete hypersurface computation.** Take the circular cylinder $C=S^1(r)\times\mathbb{R}\subset\mathbb{R}^3$, so $m=2$, $c=0$. Principal curvatures are $\kappa_1=1/r$, $\kappa_2=0$; thus
$$H=\tfrac12\left(\tfrac1r+0\right)=\tfrac1{2r},\qquad |A|^2=\tfrac1{r^2}.$$
Since $H$ is constant, $\Delta H=0$, while the right-hand side of the hypersurface equation is
$$H\big(|A|^2-mc\big)=\tfrac1{2r}\cdot\tfrac1{r^2}=\tfrac1{2r^3}\neq0 .$$
So the cylinder is not biharmonic — consistent with the conjecture. The same one-line argument proves the **CMC case of Chen's conjecture in every dimension**: if $H$ is constant and $c\le0$, then $0=\Delta H=H(|A|^2-mc)$ with $|A|^2-mc\ge|A|^2\ge0$, forcing $H=0$ unless $|A|\equiv0$ and $c=0$ — in either case the immersion is minimal.

**Contrast (sharpness of the sign of $c$).** In $\mathbb{S}^{m+1}$ ($c=1$) the small hypersphere $S^m\!\big(1/\sqrt2\big)$ has $|A|^2=m=mc$, so $\Delta H=0=H(|A|^2-mc)$ holds with $H=1\neq0$: a proper biharmonic hypersurface. Positive curvature genuinely produces examples; the conjecture asserts that non-positive constant curvature never does. The open problem is what happens when $H$ is **not** constant and $n\ge6$.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*