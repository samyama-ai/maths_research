---
id: 05-analysis/mandelbrot-local-connectivity
title: "Mandelbrot Local Connectivity"
topic: 05-analysis
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Mandelbrot Local Connectivity (MLC)

> **Topic:** Real & Complex Analysis · **ID:** `05-analysis/mandelbrot-local-connectivity` · **Status:** open

## 1. Problem Statement / Conjecture

Let $p_c(z) = z^2 + c$ and let
$$M \;=\; \{\, c \in \mathbb{C} \;:\; \{p_c^{\circ n}(0)\}_{n \ge 0} \text{ is bounded} \,\}$$
be the Mandelbrot set.

**Conjecture (MLC; Douady–Hubbard, 1982–85).** $M$ is locally connected: every $c \in M$ has a neighbourhood basis $\{U_i\}$ in $M$ with each $U_i$ connected.

Since $M$ is compact, connected, and full, local connectivity is equivalent (Carathéodory) to continuous extension to $\partial\mathbb{D}$ of the Riemann map
$$\Phi:\ \widehat{\mathbb{C}}\setminus\overline{\mathbb{D}} \;\longrightarrow\; \widehat{\mathbb{C}} \setminus M ,\qquad \Phi(w) = w + O(1) \text{ at } \infty ,$$
i.e. to the statement that every parameter ray $R_M(\theta) = \Phi(\{re^{2\pi i\theta} : r>1\})$ lands and the landing map $\theta \mapsto \gamma(\theta)$ is continuous. A complete resolution is either (i) a proof that all impressions of prime ends are singletons, or (ii) exhibition of a parameter $c_0 \in \partial M$ and a sequence of points of $M$ converging to $c_0$ that cannot be joined to $c_0$ inside small connected subsets of $M$.

MLC is not merely a topological curiosity. Douady and Hubbard proved that **MLC $\Rightarrow$ $M$ is homeomorphic to the pinched-disk (abstract Mandelbrot set) model**, and hence **$\Rightarrow$ density of hyperbolicity in the quadratic family** (Fatou's conjecture for $z^2+c$): every $c\in\mathbb{C}$ is approximated by parameters whose critical orbit converges to an attracting cycle.

## 2. Mathematical Foundations

**Filled Julia set and Green's function.** For $c\in\mathbb C$, $K_c = \{z : p_c^{\circ n}(z) \not\to \infty\}$, $J_c = \partial K_c$. The Böttcher coordinate $\varphi_c$ conjugates $p_c$ to $w \mapsto w^2$ near $\infty$, and $G_c(z) = \log|\varphi_c(z)|$ extends to the escape-rate function with $G_c(p_c(z)) = 2G_c(z)$. Fundamental dichotomy: $J_c$ connected $\iff 0\in K_c \iff c\in M$.

**Uniformization of the complement.** Douady–Hubbard: $\Phi^{-1}(c) = \varphi_c(c)$ is a conformal isomorphism $\widehat{\mathbb C}\setminus M \to \widehat{\mathbb C}\setminus\overline{\mathbb D}$; in particular $M$ is connected.

**Multiplier and hyperbolic components.** A cycle $z_0 \mapsto \cdots \mapsto z_{k-1}\mapsto z_0$ has multiplier $\lambda = \prod_{j} 2z_j$. A component $W\subset \operatorname{int}M$ is *hyperbolic* if $p_c$ has an attracting cycle for $c\in W$; then $\lambda_W : W \to \mathbb{D}$ is a conformal isomorphism (Douady–Hubbard, Sullivan).

**External rays and combinatorics.** Dynamical rays $R_c(\theta)$ and parameter rays $R_M(\theta)$ are indexed by $\theta \in \mathbb{R}/\mathbb{Z}$; doubling $\sigma(\theta)=2\theta$ acts on ray angles. The *pinched-disk model* is $\overline{\mathbb D}/\!\sim_{\mathrm{QML}}$, where $\sim_{\mathrm{QML}}$ is Thurston's quadratic minor lamination. MLC $\iff$ the induced map $\overline{\mathbb D}/\!\sim_{\mathrm{QML}} \to M$ is a homeomorphism.

**Renormalization.** $p_c$ is *renormalizable* of period $k>1$ if there are topological disks $0\in U \Subset V$ with $p_c^{\circ k}: U \to V$ a degree-2 proper (quadratic-like) map with connected filled Julia set; by Douady–Hubbard straightening, $p_c^{\circ k}|_U$ is hybrid equivalent to some $z^2+c'$. *A priori bounds* means the moduli $\operatorname{mod}(V_n \setminus U_n)$ of the successive renormalization annuli stay bounded below:
$$\inf_{n} \operatorname{mod}(V_n\setminus U_n) \;>\; 0 .$$

**Yoccoz puzzles.** Cutting $K_c$ (resp. $M$) by equipotentials and the finitely many rays landing at the repelling fixed point $\alpha$ (resp. the corresponding parameter rays) gives nested puzzle pieces $P_n(c)$, $\bigcap_n P_n(c) = \{c\}$ whenever one can prove $\sum_n \operatorname{mod}(P_n\setminus P_{n+1}) = \infty$ (Grötzsch inequality). MLC at $c$ reduces to shrinking of *parapuzzle* pieces.

## 3. History & State of the Art

- **1980–82.** Mandelbrot's computer pictures; Douady and Hubbard prove connectivity of $M$ (C. R. Acad. Sci. Paris, 1982) and develop the theory in the *Orsay notes*, "Étude dynamique des polynômes complexes" (1984–85), where MLC is formulated and its consequence for density of hyperbolicity established.
- **1985–90.** Thurston's lamination theory supplies the conjectural combinatorial model; Tan Lei proves asymptotic similarity between $M$ and $J_c$ at Misiurewicz points (1990); Milnor's "Self-similarity and hairiness in the Mandelbrot set" (1989).
- **1990–95.** **Yoccoz**: MLC holds at every *at most finitely renormalizable* parameter with all periodic orbits repelling — the single largest advance. Exposition in Hubbard (1993).
- **1996–99.** **Lyubich** proves complex a priori bounds and MLC for infinitely renormalizable parameters of *bounded primitive type satisfying a "secondary limbs" condition* (Acta Math. 1997); with Graczyk–Świątek this yields density of hyperbolicity in the **real** quadratic family (Annals 1997).
- **2006–09.** **Kahn**: a priori bounds for bounded primitive combinatorics. **Kahn–Lyubich**: local connectivity of $J_c$ for unicritical maps under a priori bounds (Annals 2009); **Avila–Kahn–Lyubich–Shen**: combinatorial rigidity for unicritical polynomials $z^d+c$, extending Yoccoz's result to $d\ge 3$ (Annals 2009).
- **2012–22.** Buff–Chéritat construct quadratic Julia sets of positive area (Annals 2012); Avila–Lyubich construct Feigenbaum Julia sets of positive measure (Publ. IHÉS / Annals-level results, 2022). These show the measure-theoretic "hairiness" side of $M$ is subtler than expected but do **not** contradict MLC.
- **2018–2023.** **Dudko–Lyubich** develop *pacman renormalization* and prove MLC at *satellite* parameters of bounded type, and at the Feigenbaum point — the first genuinely infinitely-satellite-renormalizable cases.

Computationally, $M$ has been rendered to depths $\sim 10^{-1000}$ with perturbation/series arithmetic; no numerical evidence against MLC exists, but pictures cannot certify local connectivity.

## 4. Partial Results / Verified Cases

MLC is **proven** at:

1. **Every $c \notin M$** and every $c$ in a hyperbolic component's closure with locally connected boundary — trivially, $\partial W$ is a Jordan curve for each hyperbolic $W$ (Douady–Hubbard).
2. **All at most finitely renormalizable parameters with only repelling cycles** (Yoccoz, ~1990). This includes all Misiurewicz (strictly preperiodic critical orbit) parameters, e.g. $c=i$, $c=-2$.
3. **Real parameters**: $M \cap \mathbb{R} = [-2,\ 1/4]$, and MLC holds at every real $c$ (Lyubich 1997; Graczyk–Świątek 1997), giving density of hyperbolicity for the real logistic family.
4. **Infinitely renormalizable, bounded *primitive* type** satisfying the secondary-limbs condition (Lyubich 1997; a priori bounds by Kahn 2006 removed the extra hypothesis in the bounded case).
5. **Infinitely renormalizable *satellite* type of bounded combinatorics**, including the Feigenbaum parameter $c_{\mathrm{Feig}} \approx -1.401155$ (Dudko–Lyubich, pacman renormalization, 2018–2021).
6. **Degree-$d$ analogues**: connectedness loci $\mathcal M_d$ of $z^d+c$ are locally connected at finitely renormalizable parameters (Avila–Kahn–Lyubich–Shen 2009).
7. **Every point of $\partial M$ is the landing point of at least one ray** in the sense that rays with rational angle all land (Douady; Goldberg–Milnor), so the *combinatorial* model surjects onto $M$.

Uncovered: infinitely renormalizable parameters of **unbounded** combinatorics — a set of Hausdorff dimension $2$ in $\partial M$ carrying the hardest behaviour.

## 5. Principal Obstacles

- **Loss of a priori bounds.** All known proofs of parapuzzle shrinking need $\operatorname{mod}(V_n\setminus U_n)\ge \mu>0$. For unbounded combinatorics the return times blow up, the quadratic-like germs degenerate towards parabolic maps, and the moduli are only known to satisfy weak (non-uniform) lower bounds. Without them the Grötzsch sum $\sum \operatorname{mod}$ can converge and puzzle pieces need not shrink to points.
- **Parabolic implosion / near-parabolic renormalization.** In the satellite case the renormalization operator is not hyperbolic in the classical Douady–Hubbard–Sullivan–McMullen sense; the relevant fixed points are parabolic-like, so the standard exponential contraction of the renormalization horseshoe is unavailable. Cheraghi–Shishikura's near-parabolic renormalization controls high-type rotation numbers, but the analytic estimates degrade as the type grows.
- **Failure of transfer from dynamical to parameter plane.** Local connectivity of $J_c$ does not imply MLC at $c$; the Douady "first entry"/parameter-to-dynamics transfer requires uniform geometric bounds along the whole renormalization tower.
- **Genuine non-local-connectivity nearby.** Sørensen and Douady constructed infinitely renormalizable quadratics with non-locally connected $J_c$; Buff–Chéritat produced $J_c$ of positive area. So the dynamical-plane statement is *false* in general, and any proof of MLC must exploit a parameter-plane-only rigidity mechanism.
- **No usable linear theory.** Fourier/harmonic methods do not see $M$: $\partial M$ has Hausdorff dimension $2$ (Shishikura 1998), so quantitative potential theory gives no modulus of continuity for $\Phi$.

## 6. The Gap

Proven: MLC at all $c$ that are at most finitely renormalizable, and at infinitely renormalizable $c$ whose renormalization combinatorics are **bounded** (primitive by Lyubich/Kahn, satellite by Dudko–Lyubich).

Missing: the case of **infinitely renormalizable parameters of unbounded combinatorial type**, in particular unbounded satellite (Siegel-adjacent) towers where renormalization periods $k_n$ and rotation numbers grow arbitrarily fast. The precise step needed is:

> **Uniform complex a priori bounds.** Show that for every infinitely renormalizable $c$ there is $\mu(c)>0$ with $\operatorname{mod}(V_n\setminus U_n)\ge\mu$ for all $n$ — or a substitute rigidity argument that yields $\operatorname{diam}(P_n(c))\to 0$ for parapuzzle pieces without such bounds.

Equivalently: prove *combinatorial rigidity* — two infinitely renormalizable quadratics with the same combinatorics and no invariant line field are conformally conjugate (the "no invariant line fields" conjecture is itself equivalent in strength to MLC-plus-hyperbolicity for quadratics).

## 7. Current Research (as of June 2026)

- **Pacman renormalization** (Dudko, Lyubich, Selinger): extending the hyperbolicity of the pacman renormalization operator from bounded to slowly-growing satellite types. *(frontier — verify)* Attempts to reach "eventually bounded" and Brjuno-type rotation numbers are active.
- **Near-parabolic renormalization** (Cheraghi, Shishikura, Yang, and collaborators at Imperial College London / Kyoto): control of high-type Siegel and satellite parameters; recent work on the trichotomy for the post-critical set and on rigidity of Siegel boundaries.
- **Positive-measure and hairiness phenomena** (Avila, Lyubich, Buff, Chéritat, Dudko): mapping the boundary between measure-theoretic pathology and topological rigidity.
- **Groups/institutions:** Stony Brook (Lyubich, Dudko), IMPA/Zurich (Avila), Kyoto (Shishikura), Toulouse (Chéritat, Buff), Warwick and Imperial (Cheraghi, van Strien), Fudan/Shen Weixiao (higher-degree rigidity).
- **Computer-assisted directions:** rigorous interval-arithmetic verification of a priori bounds for specific deep combinatorial types; validated numerics for the Feigenbaum fixed point. *(frontier — verify)*

## 8. Future Work

- Prove complex a priori bounds for **all** combinatorial types, or classify the exact obstruction (Lyubich's proposed programme).
- Establish hyperbolicity of a *unified* renormalization operator covering primitive and satellite towers, so that Sullivan-style rigidity applies uniformly.
- Attack the equivalent **no invariant line fields** conjecture directly via quasiconformal deformation theory and thermodynamic formalism on $J_c$.
- Extend the Avila–Kahn–Lyubich–Shen rigidity machinery to the bicritical and cubic connectedness loci, where local connectivity is known to **fail** for the cubic locus (Lavaurs) — understanding why $d$-unicritical differs from multicritical may isolate what MLC really needs.
- Develop parameter-plane analogues of Buff–Chéritat's perturbation techniques to search for a *counterexample* at unbounded satellite type — a live minority view.

## 9. Key References

- **[Foundational]** A. Douady and J. H. Hubbard. *Étude dynamique des polynômes complexes* (Publications Mathématiques d'Orsay 84-02, 85-04), Université de Paris-Sud, 1984–85.
- **[Foundational]** A. Douady and J. H. Hubbard. *On the dynamics of polynomial-like mappings.* Annales Scientifiques de l'École Normale Supérieure, 18(2):287–343, 1985. [DOI](https://doi.org/10.24033/asens.1491)
- **[Foundational]** J. H. Hubbard. *Local connectivity of Julia sets and bifurcation loci: three theorems of J.-C. Yoccoz.* In *Topological Methods in Modern Mathematics*, Publish or Perish, 1993, pp. 467–511.
- **[Foundational]** J. Milnor. *Dynamics in One Complex Variable*, 3rd ed., Annals of Mathematics Studies 160, Princeton University Press, 2006.
- **[SOTA]** M. Lyubich. *Dynamics of quadratic polynomials, I–II.* Acta Mathematica, 178:185–247 and 247–297, 1997. [DOI](https://doi.org/10.1007/bf02392694)
- **[SOTA]** J. Graczyk and G. Świątek. *Generic hyperbolicity in the logistic family.* Annals of Mathematics, 146(1):1–52, 1997. [DOI](https://doi.org/10.2307/2951831)
- **[SOTA]** J. Kahn and M. Lyubich. *Local connectivity of Julia sets for unicritical polynomials.* Annals of Mathematics, 170(1):413–426, 2009. [DOI](https://doi.org/10.4007/annals.2009.170.413)
- **[SOTA]** A. Avila, J. Kahn, M. Lyubich, W. Shen. *Combinatorial rigidity for unicritical polynomials.* Annals of Mathematics, 170(2):783–797, 2009. [DOI](https://doi.org/10.4007/annals.2009.170.783)
- **[SOTA / Recent]** D. Dudko and M. Lyubich. *Local connectivity of the Mandelbrot set at some satellite parameters of bounded type.* arXiv:1808.10425 (2018); and *MLC at Feigenbaum points*, arXiv:2101.11834 (2021).
- **[Recent]** X. Buff and A. Chéritat. *Quadratic Julia sets with positive area.* Annals of Mathematics, 176(2):673–746, 2012. [DOI](https://doi.org/10.4007/annals.2012.176.2.1)
- **[Recent]** A. Avila and M. Lyubich. *Lebesgue measure of Feigenbaum Julia sets.* Annals of Mathematics, 195(1):1–88, 2022. [DOI](https://doi.org/10.4007/annals.2022.195.1.1)
- **[Survey]** M. Shishikura. *The Hausdorff dimension of the boundary of the Mandelbrot set and Julia sets.* Annals of Mathematics, 147(2):225–267, 1998. [DOI](https://doi.org/10.2307/121009)
- **[Survey]** J. Milnor. *Local connectivity of Julia sets: expository lectures.* In *The Mandelbrot Set, Theme and Variations* (ed. Tan Lei), LMS Lecture Note Series 274, Cambridge University Press, 2000, pp. 67–116. [DOI](https://doi.org/10.1017/cbo9780511569159.006)
- **[Survey]** C. T. McMullen. *Complex Dynamics and Renormalization*, Annals of Mathematics Studies 135, Princeton University Press, 1994.

## 10. Worked Example / Concrete Special Case

**The $1/2$-wake and the root $c=-3/4$: MLC verified by hand.**

Period-2 cycles of $p_c(z)=z^2+c$ satisfy $p_c^{\circ 2}(z)=z$ but $p_c(z)\ne z$; dividing $z^4+2cz^2 - z + c^2+c$ by $z^2 - z + c$ gives
$$z^2 + z + (c+1) = 0 ,\qquad z_1+z_2=-1,\quad z_1z_2 = c+1 .$$
The multiplier is
$$\lambda = p_c'(z_1)p_c'(z_2) = 4z_1z_2 = 4(c+1).$$
Hence the period-2 hyperbolic component is exactly the disk
$$W_2 = \{\,c : |4(c+1)|<1\,\} = \{\,|c+1|<\tfrac14\,\},$$
a round disk of radius $1/4$ centred at $-1$ (containing the basilica $c=-1$, $\lambda=0$). Its root is $\lambda=1$, i.e. $c=-3/4$, where $W_2$ is internally tangent to the main cardioid $c = \tfrac{\mu}{2}-\tfrac{\mu^2}{4}$ at $\mu = -1$.

Two parameter rays land at $c=-3/4$: $R_M(1/3)$ and $R_M(2/3)$, the angles being the fixed points of the doubling map's $2$-cycle $1/3 \mapsto 2/3 \mapsto 1/3$. They cut $\mathbb{C}$ into two pieces; the one containing $-1$ is the **$1/2$-wake** $\mathcal{W}_{1/2}$.

*Local connectivity at $c=-3/4$.* Take the parapuzzle neighbourhoods
$$P_n \;=\; \{\, c : G_M(c) < 2^{-n} \,\} \cap \big(\mathcal{W}_{1/2}\text{-sector between }R_M(1/3), R_M(2/3)\big) \;\cup\; \{\text{cardioid side}\},$$
where $G_M = \log|\Phi^{-1}|$. Because both rays land at the *same* point $-3/4$ and the parabolic implosion at $c=-3/4$ is understood explicitly (the parabolic fixed point $z=-1/2$ with $p_c'(-1/2)=-1$, $p_c^{\circ 2}$ having a degenerate fixed point), the sets $P_n \cap M$ are connected and $\operatorname{diam}(P_n)\to 0$. So $M$ is locally connected at $-3/4$.

*Where the difficulty starts.* Iterate the construction: inside $W_2$ sit period-4, period-8, … satellite components with roots $c_1=-3/4$, $c_2\approx -1.25$, $c_3\approx -1.3680989$, … accumulating at $c_{\mathrm{Feig}}\approx -1.4011551890$, with $ (c_n - c_{\mathrm{Feig}}) \sim C\,\delta^{-n}$, $\delta = 4.6692\ldots$ At $c_{\mathrm{Feig}}$ the parameter is infinitely renormalizable of period $2^n$; the puzzle pieces $P_n$ are now separated by *renormalization annuli* whose moduli must be bounded below to conclude $\operatorname{diam}(P_n)\to0$. Here the combinatorics are bounded (all periods double), Feigenbaum–Coullet–Tresser universality supplies the bounds, and MLC holds (Lyubich; Dudko–Lyubich). Replace "double every step" by a sequence of rotation numbers $p_n/q_n$ with $q_n\to\infty$ arbitrarily fast, and every known lower bound on $\operatorname{mod}(V_n\setminus U_n)$ degenerates to $0$ — that is exactly the open case of Section 6.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*