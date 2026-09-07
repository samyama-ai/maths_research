---
id: 03-geometry/schoen-yau-conjecture
title: "Schoen-Yau Conjecture"
topic: 03-geometry
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Schoen-Yau Conjecture

> **Topic:** Algebraic & Differential Geometry · **ID:** `03-geometry/schoen-yau-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

**Conjecture (Schoen–Yau; also attributed to Gromov–Lawson).** Let $M^n$ be a closed, connected, smooth aspherical manifold, i.e. $\pi_k(M) = 0$ for all $k \ge 2$, equivalently the universal cover $\widetilde{M}$ is contractible. Then $M$ admits **no** Riemannian metric $g$ of positive scalar curvature (PSC), $R_g > 0$ everywhere.

A complete proof must either (a) produce, for every closed aspherical $M^n$ and every metric $g$ on $M$, a point where $R_g \le 0$; or (b) exhibit a single closed aspherical manifold carrying a PSC metric. By Kazdan–Warner's trichotomy, "admits $R_g>0$" is a diffeomorphism invariant, so the statement is topological.

The conjecture is **open for $n \ge 6$** and proved for $n \le 5$.

*Disambiguation.* The name "Schoen–Yau conjecture" is also attached to the assertion that no harmonic diffeomorphism exists from $\mathbb{C}$ onto the hyperbolic plane $\mathbb{H}^2$. That statement was **disproved** by Collin and Rosenberg (*Ann. of Math.* 172 (2010)). This page treats the scalar-curvature conjecture, which is the one still open.

## 2. Mathematical Foundations

Let $(M^n,g)$ be closed and oriented. The **scalar curvature** is the double trace of the Riemann tensor,
$$R_g = g^{ik}g^{jl}R_{ijkl} = \sum_{i,j} \langle R(e_i,e_j)e_j, e_i\rangle,$$
with the geometric meaning
$$\frac{\mathrm{vol}\big(B_r^{(M,g)}(p)\big)}{\mathrm{vol}\big(B_r^{\mathbb{R}^n}\big)} = 1 - \frac{R_g(p)}{6(n+2)}r^2 + O(r^4).$$

**Aspherical.** $M$ is aspherical iff $M \simeq B\pi$ for $\pi = \pi_1(M)$; then $H_*(M;\mathbb{Z}) \cong H_*(B\pi;\mathbb{Z})$ and the fundamental class $[M] \in H_n(B\pi;\mathbb{Z})$ is nonzero. Examples: $T^n$, closed hyperbolic and nonpositively curved manifolds, closed locally symmetric spaces of noncompact type, nilmanifolds, solvmanifolds, closed surfaces of genus $\ge 1$.

**Second variation / stability.** For a two-sided closed minimal hypersurface $\Sigma^{n-1} \subset M^n$ with unit normal $\nu$ and second fundamental form $A$, stability means
$$Q(f,f) = \int_\Sigma |\nabla f|^2 - \big(\mathrm{Ric}(\nu,\nu) + |A|^2\big)f^2 \, d\mu \ \ge\ 0 \qquad \forall f \in C^\infty(\Sigma).$$

**Traced Gauss equation** for a minimal ($H=0$) hypersurface:
$$R_\Sigma = R_M - 2\,\mathrm{Ric}(\nu,\nu) - |A|^2 .$$
Combining the two and using $|A|^2 \ge \tfrac{1}{n-1}H^2 = 0$ gives the **Schoen–Yau descent inequality**: for all $f$,
$$\int_\Sigma \Big(|\nabla f|^2 + \tfrac{1}{2}R_\Sigma f^2\Big) \ \ge\ \int_\Sigma \Big(\tfrac{1}{2}R_M + \tfrac{1}{2}|A|^2 + \tfrac12|\nabla_\Sigma \log \cdot|^2\text{-terms}\Big) f^2,$$
so a stable minimal hypersurface in a PSC manifold carries a metric with $\lambda_1(-\Delta + \tfrac12 R_\Sigma) > 0$, hence (after conformal change, $n-1 \ge 3$) a PSC metric. This is the **codimension-one induction**.

**Dirac operator route.** If $M$ is spin with $\hat{S}$ the spinor bundle, the Lichnerowicz formula reads
$$D^2 = \nabla^*\nabla + \tfrac{1}{4}R_g .$$
$R_g>0$ forces $\ker D = 0$, hence $\hat{A}(M)=0$; twisting by flat/almost-flat bundles yields the index-theoretic obstructions (enlargeability, Rosenberg index $\alpha(M) \in KO_n(C^*_r\pi)$).

**Geroch conjecture** (the $M=T^n$ case) is the model special case.

## 3. History & State of the Art (SOTA)

- **1979.** Schoen and Yau introduce the minimal-hypersurface descent and prove $T^n$ admits no PSC metric for $n \le 7$ (*Manuscripta Math.* 28; *Ann. of Math.* 110 for the 3-dimensional topology). The dimension cap comes from regularity of area-minimizing integral currents, which can be singular for $n \ge 8$.
- **1980–83.** Gromov and Lawson develop the spin/Dirac obstruction: **enlargeable** manifolds (including all closed manifolds admitting nonpositively curved metrics) carry no PSC metric in the spin case. Rosenberg (1983) formulates the $C^*$-index obstruction and shows the Strong Novikov Conjecture for $\pi$ implies no PSC for spin aspherical $M$ with $\pi_1=\pi$.
- **1998.** Schick's counterexample to the unstable Gromov–Lawson–Rosenberg conjecture shows the index obstruction is not complete in general, though not for aspherical manifolds.
- **2017–2022.** Schoen–Yau remove the dimensional restriction for the *torus* by minimizing in a weighted/slicing scheme that tolerates codimension-$\ge 3$ singular sets, and by a dimension-reduction argument on the singular strata; the Geroch conjecture is thereby settled in all dimensions.
- **2020–2024.** Gromov's $\mu$-bubbles (prescribed-mean-curvature soap bubbles) become the central tool. **Chodosh–Li** prove the aspherical conjecture in $n=4$ and $n=5$ (*Ann. of Math.* 199 (2024)).
- **Current SOTA:** true for $n \le 5$ unconditionally; true in all dimensions for spin $M$ whose $\pi_1$ satisfies the Strong Novikov Conjecture; open for non-spin or Novikov-unknown fundamental groups in $n \ge 6$.

## 4. Partial Results / Verified Cases

| Class | Result | Source |
|---|---|---|
| $n \le 3$ | No PSC on aspherical $M^3$ | Schoen–Yau 1979; Gromov–Lawson 1983; geometrization |
| $n = 4, 5$ | No PSC on any closed aspherical $M^n$ | Chodosh–Li 2024 |
| $M = T^n$, all $n$ | Geroch conjecture | Schoen–Yau 1979 ($n\le7$); Schoen–Yau 2017/2022 (all $n$) |
| Spin, $\pi_1$ satisfies Strong Novikov | No PSC | Rosenberg 1983 |
| $\pi_1$ Gromov-hyperbolic, CAT(0)-cubulated, a-T-menable, or a discrete subgroup of a Lie group, spin | No PSC (Novikov known) | Connes–Moscovici 1990; Kasparov–Skandalis 2003; Higson–Kasparov 2001 |
| Nonpositively curved (any $n$), spin | Enlargeable $\Rightarrow$ no PSC | Gromov–Lawson 1983 |
| Enlargeable, non-spin | No PSC | Schoen–Yau 2017; Cecchini–Schick 2021 |
| $M^n = N^{n-m}\times T^m$-type with $\pi_1$-nonzero degree maps, $n\le 7$ | Generalized Geroch | Brendle–Hirsch–Johne 2024 |
| Sufficiently connected (not nec. aspherical) $n=4,5$ | Classification of PSC | Chodosh–Li–Liokumovich 2023 |

## 5. Principal Obstacles

- **Asphericity is not inherited by slices.** The descent replaces $M^n$ by a stable minimal hypersurface $\Sigma^{n-1}$ Poincaré-dual to a class in $H^1(M;\mathbb{Z})$. For the torus, $\Sigma$ inherits a torus-like homological structure. For a general aspherical $M$, $\Sigma$ need not be aspherical and need not even be $\pi_1$-injective, so the induction hypothesis evaporates after one step. This is the core failure.
- **Dimension cap of the slicing argument.** Chodosh–Li's proof works by descending until the residual pieces are $2$- or $3$-dimensional, where surface topology closes the argument. Starting at $n=6$, the descent leaves $3$-dimensional pieces whose "sufficient connectedness" cannot be controlled by the available homotopy input.
- **Minimal surface regularity.** Area-minimizing hypersurfaces have singular sets of dimension $n-8$; Schoen–Yau's 2017 workaround is delicate and adapted to $T^n$-type slicings. A general stable Bernstein theorem in $\mathbb{R}^{n}$ for $n \ge 6$ — needed to control blowups — is unavailable.
- **Non-spin.** The Dirac/index machinery requires a spin structure (or spin$^c$ with a curvature condition). Aspherical manifolds are frequently non-spin, and $KO$-theoretic obstructions have no known non-spin analogue.
- **Novikov is itself open.** The index route reduces the conjecture (in the spin case) to the Strong Novikov Conjecture, which is unproved for general groups; this is a lateral transfer of difficulty, not a solution.

## 6. The Gap

Proven: aspherical $\Rightarrow$ no PSC for $n\le 5$; and for all $n$ when either (i) $M$ is enlargeable, or (ii) $M$ is spin with $\pi_1$ satisfying Strong Novikov. The general statement asserts it for **every** closed aspherical $M^n$, $n\ge 6$.

The precise missing step: find a *homotopy-invariant* quantity, defined for all closed aspherical $M$ and stable under codimension-one minimal descent, which is nonzero for $[M]\in H_n(B\pi)$ and vanishes under PSC. Equivalently — construct a slicing $\Sigma^{n-1}\subset M^n$ for which the inherited structure still forbids PSC, without assuming $\Sigma$ aspherical. Every current proof supplies such a quantity only under one of the two extra hypotheses.

## 7. Current Research (as of June 2026)

- **$\mu$-bubbles and warped slicings** (Gromov; Chodosh, Li, Liokumovich at Stanford/MIT/UCSB): pushing the $n=5$ argument to $n=6$ by replacing "aspherical" with a filling-radius or macroscopic-dimension hypothesis. Gromov's conjecture that PSC $\Rightarrow$ macroscopic dimension $\le n-2$ is the natural intermediate target *(frontier — verify)*.
- **Stable Bernstein theorems.** Chodosh–Li–Minter–Stryker's classification of stable minimal hypersurfaces in $\mathbb{R}^5$ (2024) is the type of input needed for blowup control at $n=6$ *(frontier — verify)*.
- **Spacetime harmonic functions / level-set methods** (Bray, Hirsch, Kazaras, Khuri): substitutes for minimal surfaces avoiding regularity issues, successful in $n=3,4$.
- **Coarse index theory** (Schick, Cecchini, Zeidler, Göttingen/Münster): quantitative index and band-width estimates, and non-spin transfer via Schoen–Yau slicing.
- **Brendle–Hirsch–Johne torical band/Geroch generalizations**, and Brendle's work on scalar curvature rigidity, extending the $n\le 7$ range.

## 8. Future Work

- Prove Gromov's macroscopic-dimension conjecture; it implies the aspherical conjecture in the cases of interest.
- Establish Strong Novikov for wider group classes (e.g. all groups of finite asymptotic dimension is known — Yu; extend beyond).
- Build a non-spin index theory, or a systematic non-spin$\to$spin transfer via slicing, that reproduces the Rosenberg obstruction.
- Settle $n=6$: identify the correct "3-dimensional residue" invariant surviving two rounds of descent.
- Prove or refute a *smoothing* statement: does every closed aspherical $M^6$ admit a $\pi_1$-injective codimension-one slicing with controlled topology?

## 9. Key References

- **[Foundational]** R. Schoen, S.-T. Yau. *On the structure of manifolds with positive scalar curvature.* Manuscripta Mathematica 28 (1979), 159–183.
- **[Foundational]** R. Schoen, S.-T. Yau. *Existence of incompressible minimal surfaces and the topology of three dimensional manifolds with non-negative scalar curvature.* Annals of Mathematics 110 (1979), 127–142.
- **[Foundational]** M. Gromov, H. B. Lawson Jr. *Positive scalar curvature and the Dirac operator on complete Riemannian manifolds.* Publ. Math. IHÉS 58 (1983), 83–196.
- **[Foundational]** J. Rosenberg. *$C^*$-algebras, positive scalar curvature, and the Novikov conjecture.* Publ. Math. IHÉS 58 (1983), 197–212.
- **[SOTA]** O. Chodosh, C. Li. *Generalized soap bubbles and the topology of manifolds with positive scalar curvature.* Annals of Mathematics 199 (2024), 707–740.
- **[SOTA]** R. Schoen, S.-T. Yau. *Positive scalar curvature and minimal hypersurface singularities.* Surveys in Differential Geometry 24 (2019/2022), 441–480.
- **[SOTA]** S. Brendle, S. Hirsch, F. Johne. *A generalization of Geroch's conjecture.* Comm. Pure Appl. Math. 77 (2024), 441–456.
- **[SOTA]** O. Chodosh, C. Li, Y. Liokumovich. *Classifying sufficiently connected PSC manifolds in 4 and 5 dimensions.* Geometry & Topology 27 (2023), 1635–1655.
- **[Related]** S. Cecchini, T. Schick. *Enlargeable metrics on nonspin manifolds.* Proc. Amer. Math. Soc. 149 (2021), 2199–2211.
- **[Counterexample, related conjecture]** T. Schick. *A counterexample to the (unstable) Gromov–Lawson–Rosenberg conjecture.* Topology 37 (1998), 1165–1168.
- **[Survey]** M. Gromov. *Four lectures on scalar curvature.* arXiv:1908.10612; in *Perspectives in Scalar Curvature*, World Scientific, 2023.
- **[Survey]** J. Rosenberg, S. Stolz. *Metrics of positive scalar curvature and connections with surgery.* In *Surveys on Surgery Theory* vol. 2, Annals of Math. Studies 149, Princeton, 2001.
- **[Disambiguation]** P. Collin, H. Rosenberg. *Construction of harmonic diffeomorphisms and minimal graphs.* Annals of Mathematics 172 (2010), 1879–1906.

## 10. Worked Example / Concrete Special Case

**Claim.** $T^3$ admits no metric with $R_g > 0$.

Assume $g$ on $T^3$ with $R_g > 0$. Pick a nonzero class $\sigma \in H_2(T^3;\mathbb{Z})$, say $\sigma = [T^2 \times \{pt\}]$. Geometric measure theory gives an area-minimizing embedded closed surface $\Sigma \subset T^3$ with $[\Sigma] = \sigma$ (regularity is automatic in ambient dimension $3$). $\Sigma$ is minimal ($H=0$) and stable.

**Step 1 — stability with test function $f\equiv 1$:**
$$0 \le Q(1,1) = -\int_\Sigma \big(\mathrm{Ric}(\nu,\nu) + |A|^2\big)\,d\mu \implies \int_\Sigma \mathrm{Ric}(\nu,\nu)\,d\mu \le -\int_\Sigma |A|^2\,d\mu .$$

**Step 2 — Gauss equation** ($H=0$, $R_\Sigma = 2K_\Sigma$):
$$2K_\Sigma = R_g - 2\,\mathrm{Ric}(\nu,\nu) - |A|^2 .$$

**Step 3 — integrate and substitute:**
$$2\int_\Sigma K_\Sigma = \int_\Sigma R_g - 2\int_\Sigma \mathrm{Ric}(\nu,\nu) - \int_\Sigma |A|^2 \ \ge\ \int_\Sigma R_g + 2\int_\Sigma|A|^2 - \int_\Sigma |A|^2 \ \ge\ \int_\Sigma R_g \ >\ 0 .$$

**Step 4 — Gauss–Bonnet:** $\int_\Sigma K_\Sigma = 2\pi\chi(\Sigma)$, so $4\pi\chi(\Sigma) > 0$, giving $\chi(\Sigma)>0$, i.e. $\Sigma \cong S^2$ (orientable case).

**Step 5 — contradiction with asphericity:** $T^3$ is aspherical, so $\pi_2(T^3)=0$ and every map $S^2 \to T^3$ is null-homotopic, hence $[\Sigma]=0$ in $H_2(T^3;\mathbb{Z})$, contradicting $[\Sigma]=\sigma \neq 0$. $\square$

**Where the general case breaks.** For $n=4$ the same descent produces a stable minimal $\Sigma^3 \subset M^4$ carrying PSC (after conformal change), and one would like to iterate. But for a general aspherical $M^4$, $\Sigma^3$ need not be aspherical: it may be a connected sum containing $S^2\times S^1$ or spherical space-form factors, exactly the PSC-admitting $3$-manifolds. Chodosh–Li repair this by replacing minimal $\Sigma$ with a $\mu$-bubble (prescribed mean curvature $H = h$, minimizing $\mathcal{A}(\Omega)=\mathcal{H}^{n-1}(\partial\Omega) - \int_\Omega h$) and tracking $\pi_1$-injective incompressible pieces through the prime decomposition. In $n \ge 6$ the corresponding bookkeeping has no known termination — that is the open gap of Section 6.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*