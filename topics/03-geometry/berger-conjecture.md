---
id: 03-geometry/berger-conjecture
title: "Berger Conjecture"
topic: 03-geometry
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Berger Conjecture (Manifolds All of Whose Geodesics Are Closed)

> **Topic:** Algebraic & Differential Geometry · **ID:** `03-geometry/berger-conjecture` · **Status:** partially-solved (open in general; settled for $S^n$, $n\ge 4$, and $n=2$)

## 1. Problem Statement / Conjecture

Let $(M,g)$ be a closed, connected Riemannian manifold all of whose unit-speed geodesics are closed (a **Besse manifold**). By Wadsley's theorem the geodesic flow is then periodic, so there is a common period $\ell>0$: every unit-speed geodesic $\gamma$ satisfies $\gamma(t+\ell)=\gamma(t)$ for all $t$. The *least* period of $\gamma$ is $\ell/k(\gamma)$ for some integer $k(\gamma)\ge 1$, and geodesics with $k(\gamma)\ge 2$ are called **exceptional**.

**Berger Conjecture.** *If $M$ is simply connected and all geodesics of $g$ are closed, then all geodesics have the same least period; i.e. every $P_\ell$-metric on a simply connected manifold is a $C_\ell$-metric, so no exceptional geodesics exist.*

A complete proof requires showing $k(\gamma)=1$ for every geodesic, for every simply connected Besse manifold of every dimension (equivalently: the exceptional set $\Sigma\subset UM$ of unit vectors tangent to short geodesics is empty). A disproof requires a single simply connected $(M,g)$ with all geodesics closed and two geodesics of different least periods. Simple connectivity is essential: $P_\ell$ metrics that are not $C_\ell$ exist on non–simply connected spaces (lens-space quotients; Besse, Ch. 7).

## 2. Mathematical Foundations

**Besse's notation.** $(M,g)$ is a $P_\ell$-manifold if every unit-speed geodesic is $\ell$-periodic; a $C_\ell$-manifold if every unit-speed geodesic is closed with *least* period exactly $\ell$. Trivially $C_\ell\Rightarrow P_\ell$; the conjecture asserts the converse under $\pi_1(M)=1$.

**Geodesic flow.** On the unit tangent bundle $UM$ with the geodesic flow $\phi_t:UM\to UM$, "all geodesics closed" means every orbit is periodic.

> **Wadsley (1975).** A foliation of a compact manifold by circles whose leaves are the orbits of a flow that is geodesible has a uniform period. Hence a Besse manifold admits a common period $\ell$, the flow defines a smooth $S^1$-action on $UM$, and the **space of geodesics**
> $$\mathcal{C}(M)\;=\;UM/S^1$$
> is a compact orbifold of dimension $2n-2$, $n=\dim M$. Exceptional geodesics are exactly the points with nontrivial isotropy $\mathbb{Z}_{k}$, $k\ge2$; they form a closed, nowhere dense set $\Sigma$.

**Bott–Samelson theorem.** If all geodesics of $M$ are closed and $M$ is simply connected, then $H^*(M;\mathbb{Z})$ is a truncated polynomial ring on one generator; $M$ has the integral cohomology of a compact rank-one symmetric space (CROSS): $S^n$, $\mathbb{CP}^n$, $\mathbb{HP}^n$, $\mathbb{CaP}^2$. So the topological candidates are strongly constrained before any metric analysis.

**Model metrics.** The CROSSes with their canonical metrics are $C_\ell$: all geodesics of the round $S^n$ (radius 1) close with length $2\pi$; all geodesics of $\mathbb{CP}^n$ with Fubini–Study metric normalized to sectional curvature in $[1,4]$ close with length $\pi$.

**Zoll deformations.** On $S^2$ there is an infinite-dimensional family of non-round $C_{2\pi}$ metrics (Zoll 1903); Guillemin (1976) showed that every infinitesimal $C_{2\pi}$-deformation of the round $S^2$, given by a symmetric 2-tensor whose "Radon transform" over great circles vanishes, integrates to a genuine Zoll metric. So the conjecture is not a rigidity statement forcing $g$ to be symmetric — only forcing equality of periods.

**Index machinery.** For a closed geodesic $\gamma$ of least period $\tau$, Bott's iteration formula expresses the Morse index $\mathrm{ind}(\gamma^m)$ of the $m$-fold iterate through the $\Omega$-index function on $S^1$:
$$\mathrm{ind}(\gamma^m)\;=\;\sum_{z^m=1}\Lambda_\gamma(z),\qquad \overline{\mathrm{ind}}(\gamma)=\lim_{m\to\infty}\frac{\mathrm{ind}(\gamma^m)}{m}\in[0,\infty),$$
the mean index. On a $P_\ell$ manifold, the energy functional on the free loop space $\Lambda M$ is perfectly Morse–Bott: critical manifolds at level $E=\ell^2/2$ are the geodesic space $\mathcal{C}(M)$ and its exceptional strata.

**Weinstein–Yang volume identity.** If $(M^n,g)$ is $C_{2\pi}$, then $\mathrm{vol}(M,g)=\mathrm{vol}(S^n_{\mathrm{round}})$ (Weinstein 1974 for $n$ even; extended by C. T. Yang in odd dimensions). This rigid invariant is available only once equality of periods is known — one reason the Berger conjecture is a gateway result.

## 3. History & State of the Art (SOTA)

- **1903.** Zoll constructs non-round rotationally symmetric metrics on $S^2$ with all geodesics closed of length $2\pi$.
- **1954/1963.** Bott, and Samelson, prove the cohomological restriction (CROSS-like cohomology ring).
- **1963.** Green proves the two-dimensional Blaschke conjecture: a Wiedersehen metric on $S^2$ is round.
- **1965–1976.** Berger, in his TIFR *Lectures on Geodesics*, and later in Besse's book, formulates the conjecture and proves the basic structure: on a simply connected $P_\ell$ manifold, exceptional geodesics form a closed nowhere-dense set and all periods are $\ell/k$, $k\in\mathbb{N}$.
- **1975.** Wadsley: uniform period, hence the $S^1$-action and the geodesic orbifold.
- **1978.** Besse's monograph *Manifolds all of whose Geodesics are Closed* becomes the canonical reference; the conjecture is Problem 7.x there.
- **1981.** Gromoll–Grove settle $S^2$: any Besse metric on $S^2$ is $C_\ell$ (in fact Zoll).
- **2017.** Radeschi–Wilking prove the conjecture for all $M$ homeomorphic to $S^n$ with $n\ge 4$ — the current SOTA and the only high-dimensional case known.
- **2017–2025.** Transfer of the question to Reeb dynamics ("Besse contact forms"), where periodic Reeb flows are studied with contact homology and embedded contact homology.

## 4. Partial Results / Verified Cases

| Case | Result | Source |
|---|---|---|
| $\dim M=2$, $M\cong S^2$ | Conjecture true; every Besse metric is Zoll, all geodesics of one length | Gromoll–Grove 1981 |
| $M\cong S^n$, $n\ge 4$ | Conjecture true: all geodesics have the same least period | Radeschi–Wilking 2017 |
| $M\cong S^3$ | **Open** | — |
| $M\cong\mathbb{CP}^n,\mathbb{HP}^n,\mathbb{CaP}^2$ | **Open** in all dimensions | — |
| Wiedersehen metrics ($\mathrm{inj}=\mathrm{diam}$) on $S^n$ | Round, hence $C_\ell$ (Blaschke conjecture for spheres: Green $n=2$; Berger, Kazdan; Yang odd $n$) | Green 1963; Yang 1980 |
| Homogeneous / symmetric Besse metrics | $C_\ell$ by direct computation on CROSSes | Besse 1978, Ch. 3 |
| Zoll deformations of round $S^2$ | Explicit infinite-dimensional $C_{2\pi}$ family; period preserved | Zoll 1903; Guillemin 1976 |
| Non–simply connected | Conjecture **false**: $P_\ell$-but-not-$C_\ell$ metrics on lens spaces | Besse 1978, Ch. 7 |

Radeschi–Wilking also give dimension bounds on the exceptional set for general simply connected Besse manifolds: exceptional geodesics are confined to strata of high codimension in $\mathcal{C}(M)$, which is what forces $\Sigma=\emptyset$ once $n\ge4$ and $M\cong S^n$.

## 5. Principal Obstacles

- **No curvature hypothesis.** "All geodesics closed" is a global dynamical condition, not a curvature bound. Comparison geometry (Toponogov, Bishop–Gromov, Rauch) has no input; Besse metrics can have curvature of both signs and arbitrarily bad pinching.
- **Zoll flexibility defeats rigidity arguments.** Any strategy attempting to prove $g$ is symmetric must fail: the Zoll family and Guillemin's deformation theorem show the $C_\ell$ condition is infinitely flexible. The proof must isolate the *period* and nothing else.
- **Morse theory on $\Lambda M$ is degenerate.** The critical sets are whole $(2n-2)$-orbifolds, not isolated points; index computations must be done in families, and the Bott iteration formula for exceptional geodesics gives inequalities that become vacuous when the exceptional stratum is large relative to $n$.
- **Low dimension leaves no codimension room.** In the Radeschi–Wilking argument the exceptional stratum must be squeezed by a codimension count; for $n=3$ the geodesic space has dimension 4 and a 2-dimensional family of Hopf-type exceptional circles is not excluded by the counting alone. This is exactly why $S^3$ resists.
- **Non-sphere topologies break the loop-space input.** For $\mathbb{CP}^n$, $\mathbb{HP}^n$, $\mathbb{CaP}^2$ the rational homotopy and the $S^1$-equivariant homology of $\Lambda M$ (Ziller's computations for the symmetric models) differ, and the index parity arguments calibrated to $S^n$ do not port over.
- **Simple connectivity is used non-locally.** Since the statement is false without it, any proof must consume $\pi_1(M)=1$ globally — ruling out purely local or purely infinitesimal methods.

## 6. The Gap

Proved: $\Sigma=\emptyset$ for $M\cong S^n$, $n=2$ and $n\ge 4$. Conjectured: $\Sigma=\emptyset$ for every simply connected Besse manifold.

The precise unresolved step is the exclusion of an exceptional stratum $\Sigma_k\subset\mathcal{C}(M)$ ($k\ge2$) when either (i) $\dim M=3$, where the potential stratum is a 2-dimensional family of short circles inside the 4-dimensional geodesic space, or (ii) $M$ has $\mathbb{CP}^n$-, $\mathbb{HP}^n$- or $\mathbb{CaP}^2$-type cohomology, where the equivariant Morse theory of $\Lambda M$ at the level $E=\ell^2/2$ has not been made to produce a contradiction. Bridging the gap requires an index/codimension inequality of the form
$$\mathrm{codim}\,\Sigma_k \;>\; f(n,k)\quad\text{with}\quad f \text{ valid for } n=3 \text{ and for non-spherical cohomology rings},$$
which current Bott-iteration bounds do not deliver.

## 7. Current Research (as of June 2026)

- **Münster school (Wilking, Radeschi and collaborators).** Extending the 2017 method to $\mathbb{CP}^n$ by replacing the sphere's loop-space input with equivariant data of the Fubini–Study model. *(frontier — verify)*
- **Contact-dynamical route.** "Besse Reeb flows" — Reeb flows all of whose orbits are periodic. Ginzburg–Gürel–Mazzucchelli (spectral characterization of Besse and Zoll Reeb flows) and Mazzucchelli–Radeschi (structure of Besse convex contact spheres) give orbifold structure theorems for the orbit space and action-spectrum criteria. Applying embedded contact homology to Besse contact forms on $S^3$ is the most direct current attack on the missing dimension-3 Riemannian case. *(frontier — verify)*
- **Zoll characterizations.** Mazzucchelli–Suhr's characterization of Zoll Riemannian metrics on $S^2$ by the length spectrum feeds back into the higher-dimensional problem via systolic-type inequalities. *(frontier — verify)*
- **Blaschke-adjacent programs.** Progress on the Blaschke conjecture for $\mathbb{CP}^n$ (still open) is generally viewed as coupled to Berger's conjecture for the same topologies.

## 8. Future Work

1. **Settle $S^3$.** Either produce a Besse metric on $S^3$ with a shorter exceptional geodesic (a Hopf-fiber-type circle in a Berger-sphere-like metric), or close the codimension gap with a 3-dimensional-specific tool (ECH capacities, Hopf-fibration rigidity).
2. **Do $\mathbb{CP}^n$.** Recompute the $S^1$-equivariant homology of $\Lambda \mathbb{CP}^n$ in the $P_\ell$ setting and search for the parity obstruction analogous to the sphere case.
3. **Quantify the exceptional set.** Prove a general bound $k(\gamma)\le K(n)$ on exceptional multiplicities for simply connected Besse manifolds — weaker than the conjecture, still unknown.
4. **Sub-Riemannian and magnetic analogues.** Test the conjecture for magnetic flows and Finsler metrics, where Katok's examples already show that Finsler Zoll-type behaviour is more flexible.
5. **Couple to the Blaschke conjecture** and to the Weinstein–Yang volume identity to get quantitative consequences (volume and systolic rigidity) once periods are shown equal.

## 9. Key References

- **[Foundational]** R. Bott. *On manifolds all of whose geodesics are closed.* Annals of Mathematics **60** (1954), 375–382.
- **[Foundational]** H. Samelson. *On manifolds with many closed geodesics.* Portugaliae Mathematica **22** (1963), 193–196.
- **[Foundational]** L. W. Green. *Auf Wiedersehensflächen.* Annals of Mathematics **78** (1963), 289–299.
- **[Foundational]** M. Berger. *Lectures on Geodesics in Riemannian Geometry.* Tata Institute of Fundamental Research, Bombay, 1965.
- **[Foundational]** A. W. Wadsley. *Geodesic foliations by circles.* Journal of Differential Geometry **10** (1975), 541–549. [DOI](https://doi.org/10.4310/jdg/1214433160)
- **[Foundational]** A. Weinstein. *On the volume of manifolds all of whose geodesics are closed.* Journal of Differential Geometry **9** (1974), 513–517.
- **[Survey / canonical]** A. L. Besse. *Manifolds all of whose Geodesics are Closed.* Ergebnisse der Mathematik und ihrer Grenzgebiete 93, Springer, 1978. [DOI](https://doi.org/10.1007/978-3-642-61876-5)
- **[Partial result]** D. Gromoll, K. Grove. *On metrics on $S^2$ all of whose geodesics are closed.* Inventiones Mathematicae **65** (1981), 175–177. [DOI](https://doi.org/10.1007/bf01389300)
- **[SOTA]** M. Radeschi, B. Wilking. *On the Berger conjecture for manifolds all of whose geodesics are closed.* Inventiones Mathematicae **210** (2017), 911–962. [DOI](https://doi.org/10.1007/s00222-017-0742-4)
- **[Technique]** V. Guillemin. *The Radon transform on Zoll surfaces.* Advances in Mathematics **22** (1976), 85–119. [DOI](https://doi.org/10.1016/0001-8708(76)90139-0)
- **[Technique]** W. Ziller. *The free loop space of globally symmetric spaces.* Inventiones Mathematicae **41** (1977), 1–22. [DOI](https://doi.org/10.1007/bf01390161)
- **[Related]** C. T. Yang. *Odd-dimensional Wiedersehen manifolds are spheres.* Journal of Differential Geometry **15** (1980), 91–96. [DOI](https://doi.org/10.4310/jdg/1214435386)
- **[Recent / adjacent]** V. Ginzburg, B. Gürel, M. Mazzucchelli. *On the spectral characterization of Besse and Zoll Reeb flows.* Annales de l'Institut Henri Poincaré C — Analyse Non Linéaire **38** (2021). [DOI](https://doi.org/10.1016/j.anihpc.2020.08.004)
- **[Survey]** M. Berger. *A Panoramic View of Riemannian Geometry.* Springer, 2003 (Ch. 10 on manifolds with closed geodesics). [DOI](https://doi.org/10.1007/978-3-642-18245-7)

## 10. Worked Example / Concrete Special Case

**Zoll surfaces: verifying the conjecture explicitly on $S^2$.**

Write the round sphere in Clairaut coordinates $x=\cos\theta\in[-1,1]$, $\varphi\in[0,2\pi)$:
$$g_{\mathrm{round}}=\frac{dx^2}{1-x^2}+(1-x^2)\,d\varphi^2 .$$
Zoll's family (Besse, Ch. 4) is
$$g_h=\frac{(1+h(x))^2}{1-x^2}\,dx^2+(1-x^2)\,d\varphi^2,\qquad h:[-1,1]\to(-1,1)\ \text{smooth, odd},\ h(\pm1)=0 .$$

Take a unit-speed geodesic with Clairaut constant $c=(1-x^2)\dot\varphi$, $|c|\le 1$. The unit-speed condition gives
$$\frac{(1+h)^2}{1-x^2}\dot x^2+\frac{c^2}{1-x^2}=1 \quad\Longrightarrow\quad \dot x^2=\frac{a^2-x^2}{(1+h(x))^2},\qquad a:=\sqrt{1-c^2},$$
so the geodesic oscillates between the turning latitudes $x=\pm a$.

**Arclength between consecutive turning points.**
$$L=\int_{-a}^{a}\frac{dx}{|\dot x|}\,|\dot x|\cdot\frac{1}{|\dot x|}\;=\;\int_{-a}^{a}\frac{(1+h(x))}{\sqrt{a^2-x^2}}\,dx=\int_{-a}^{a}\frac{dx}{\sqrt{a^2-x^2}}+\int_{-a}^{a}\frac{h(x)}{\sqrt{a^2-x^2}}\,dx .$$
The first integral is $\pi$. The second vanishes: $h$ is odd and $(a^2-x^2)^{-1/2}$ is even, so the integrand is odd on a symmetric interval. Hence $L=\pi$ for **every** $c$.

**Longitude increment over the same arc.**
$$\Delta\varphi=\int_{-a}^{a}\frac{c\,(1+h(x))}{(1-x^2)\sqrt{a^2-x^2}}\,dx=\underbrace{\int_{-a}^{a}\frac{c\,dx}{(1-x^2)\sqrt{a^2-x^2}}}_{=\ \pi\ \text{(round value)}}+\underbrace{\int_{-a}^{a}\frac{c\,h(x)\,dx}{(1-x^2)\sqrt{a^2-x^2}}}_{=\ 0\ \text{(odd integrand)}}=\pi .$$

After two arcs the geodesic has returned to its initial point and direction ($\Delta\varphi=2\pi$), with total length $2\pi$. Checks: $c=0$ (meridian) gives $2\int_{-1}^{1}(1+h)\,dx/\sqrt{1-x^2}=2\pi$; $c=1$ (the equator $x=0$) gives $ds=d\varphi$, length $2\pi$.

So every $g_h$ is a $C_{2\pi}$ metric: all geodesics closed, **all with the same least period $2\pi$**, even though $g_h$ is not round for $h\not\equiv0$. This is the conjecture's assertion realized concretely, and it shows what an obstruction proof must contend with — the equality of periods survives an infinite-dimensional deformation with no curvature control. The unsolved cases ask for the same conclusion on $S^3$ and on $\mathbb{CP}^n$, where no Clairaut-type first integral is available to force the two integrals above to cancel.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*