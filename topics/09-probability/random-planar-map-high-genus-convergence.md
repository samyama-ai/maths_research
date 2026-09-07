---
id: 09-probability/random-planar-map-high-genus-convergence
title: "Convergence of Random Maps in High Genus"
topic: 09-probability
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Convergence of Random Maps in High Genus

> **Topic:** Probability & Stochastic Processes · **ID:** `09-probability/random-planar-map-high-genus-convergence` · **Status:** open

## 1. Problem Statement / Conjecture

Let $\mathcal{T}_{n,g}$ be the set of rooted triangulations with $2n$ faces of the compact orientable surface of genus $g$, and let $T_{n,g}$ be uniform on $\mathcal{T}_{n,g}$. Fix $\theta\in[0,1/2)$ and take $g=g_n$ with $g_n/n\to\theta$.

- **Local regime (settled).** $T_{n,g_n}$ converges in distribution for the local topology to the Planar Stochastic Hyperbolic Triangulation $\mathbb{T}_{\lambda(\theta)}$ of Curien.
- **Conjecture A (global/hyperbolic limit; open).** After rescaling graph distances by a constant $c(\theta)>0$ and uniformizing, $T_{n,g_n}$ converges — in the sense of local-global (Benjamini–Schramm plus mesoscopic) convergence of metric measure surfaces — to a Weil–Petersson random hyperbolic surface of genus $g_n$. Concretely: all Poisson short-cycle statistics, the systole law, the diameter $\mathrm{diam}(T_{n,g_n})=(c'(\theta)+o(1))\log n$, and the spectral gap of the map should match those of $\mathrm{WP}_{g_n}$ under the same normalization.
- **Conjecture B (critical genus; open).** For $g_n/n\to 1/2$ (maximal genus), identify the local limit; it should degenerate to a tree-like object as $\lambda(\theta)\to 0$.
- **Conjecture C (universality; open).** The limits in A and B depend on the face-degree distribution only through one scalar parameter, for all (not necessarily bipartite) face-degree profiles with a finite second moment.

A complete resolution of A means a proof or refutation of the coupling between uniform high-genus maps and Weil–Petersson random surfaces at scales beyond bounded balls.

## 2. Mathematical Foundations

**Maps.** A *map* of genus $g$ is a connected multigraph $G$ embedded in the compact orientable surface $\Sigma_g$ so that $\Sigma_g\setminus G$ is a disjoint union of open discs (the *faces*). Euler's relation is
$$V-E+F=2-2g .$$
Maps are *rooted*: one oriented edge is distinguished, killing automorphisms, so $|\mathcal{T}_{n,g}|<\infty$.

For a triangulation with $F=2n$ faces one has $E=3n$ and hence
$$V=3n-2n+2-2g=n+2-2g,\qquad \bar d=\frac{2E}{V}=\frac{6n}{n+2-2g}\xrightarrow[g/n\to\theta]{}\frac{6}{1-2\theta}.$$
So $\theta>0$ forces mean degree strictly above $6$: the map is *hyperbolic* on average.

**Local topology.** For rooted maps $m,m'$ set $d_{\mathrm{loc}}(m,m')=(1+\sup\{r: B_r(m)\simeq B_r(m')\})^{-1}$, where $B_r$ is the ball of radius $r$ around the root vertex. Benjamini–Schramm convergence is convergence in law for $d_{\mathrm{loc}}$ after re-rooting uniformly.

**PSHT.** For $\lambda\in(0,\tfrac1{12}]$, Curien's $\mathbb{T}_\lambda$ is the unique random infinite type-II triangulation of the plane with the spatial Markov property: for every finite triangulation $t$ with one hole of perimeter $p$,
$$\mathbb{P}\big(t\subset \mathbb{T}_\lambda\big)=C_p(\lambda)\,\lambda^{|t|},$$
$|t|$ = number of inner vertices, $(C_p(\lambda))_{p\ge2}$ an explicit $\lambda$-determined sequence. At $\lambda_c=1/12$ this is the UIPT of Angel–Schramm, with $\mathbb{E}|B_r|\asymp r^4$; for $\lambda<\lambda_c$,
$$|B_r(\mathbb{T}_\lambda)|\,e^{-\kappa(\lambda) r}\to W>0\quad\text{a.s.},\qquad \kappa(\lambda)>0,$$
and $\mathbb{T}_\lambda$ is a.s. nonamenable with positive anchored expansion. There is an explicit decreasing bijection $\theta\mapsto\lambda(\theta)$ from $[0,1/2)$ onto $(0,1/12]$, with $\lambda(0)=1/12$.

**Weil–Petersson surfaces.** $\mathcal{M}_g$ carries the WP volume form; $\mathrm{WP}_g$ is the normalized probability measure, with $V_g=\mathrm{Vol}_{WP}(\mathcal{M}_g)$ computed by Mirzakhani's recursion. Mirzakhani–Petri: for $X\sim \mathrm{WP}_g$, the number $N_{[a,b]}(X)$ of primitive closed geodesics of length in $[a,b]$ converges as $g\to\infty$ to a Poisson variable of mean
$$\int_a^b \frac{e^t+e^{-t}-2}{2t}\,dt,$$
and $X$ converges Benjamini–Schramm to the hyperbolic plane $\mathbb{H}^2$. Conjecture A asserts that uniform high-genus maps sit in the same universality class, with $\mathbb{T}_{\lambda(\theta)}$ playing the role of $\mathbb{H}^2$ at discrete curvature $\kappa(\lambda(\theta))$.

**Enumeration.** Bender–Canfield: for fixed $g$, the number of rooted maps with $n$ edges is $\sim t_g\, n^{5(g-1)/2}\,12^{n}$. This is non-uniform in $g$; the high-genus regime needs ratio estimates $|\mathcal{T}_{n+1,g}|/|\mathcal{T}_{n,g}|$ valid uniformly, which is the analytic engine of all known results.

## 3. History & State of the Art (SOTA)

- 1986: Bender–Canfield give fixed-genus asymptotics; Bender–Gao–Richmond extend to families. Genus is treated as a fixed parameter throughout.
- 2003: Angel–Schramm construct the UIPT ($\theta=0$, planar).
- 2006–2013: Chapuy–Marcus–Schaeffer bijection between genus-$g$ unicellular maps and labelled objects (2009); Le Gall and Miermont prove the Brownian map is the scaling limit at $g=0$ with scaling $n^{-1/4}$ (2013); Bettinelli obtains subsequential Brownian surfaces at fixed $g\ge1$ (2010), completed by Bettinelli–Miermont for compact Brownian surfaces.
- 2013: Angel–Chapuy–Curien–Ray identify the local limit of unicellular maps in high genus as a supercritical Galton–Watson tree conditioned to survive.
- 2016: Curien constructs the PSHT family $\mathbb{T}_\lambda$, the candidate hyperbolic local limits.
- 2019: Budzinski–Curien–Petri prove that random gluings of polygons with unconstrained genus converge locally to $\mathbb{H}^2$, matching Mirzakhani–Petri.
- **2021 (SOTA):** Budzinski–Louf prove $T_{n,g_n}\to\mathbb{T}_{\lambda(\theta)}$ locally for every $\theta\in[0,1/2)$ (Invent. Math.), extended in 2022 to bipartite maps with prescribed face degrees (Ann. Probab.).
- 2021–2022: Janson–Louf match short-cycle Poisson statistics of high-genus unicellular maps with Mirzakhani–Petri intensities.
- 2015–2021: Mirzakhani–Zograf and Aggarwal supply the large-genus volume asymptotics that make the surface side quantitative.

## 4. Partial Results / Verified Cases

| Regime | Result | Reference |
|---|---|---|
| $\theta=0$, $g=0$ | Full local limit (UIPT) **and** scaling limit (Brownian map, $n^{-1/4}$) | Angel–Schramm 2003; Le Gall 2013, Miermont 2013 |
| $g$ fixed $\ge 1$, $n\to\infty$ | Scaling limit: Brownian surface of genus $g$ | Bettinelli 2010; Bettinelli–Miermont |
| $\theta\in[0,1/2)$, triangulations | Local limit $=\mathbb{T}_{\lambda(\theta)}$ | Budzinski–Louf 2021 |
| $\theta\in[0,1/2)$, bipartite, prescribed face degrees, finite exponential moment | Local limit in the PSHT-type family | Budzinski–Louf 2022 |
| Unicellular maps ($F=1$), $g/n\to\theta\in(0,1/2)$ | Local limit is a GW tree conditioned to survive; degenerates to the $3$-regular tree as $\theta\to1/2$ | Angel–Chapuy–Curien–Ray 2013 |
| Unicellular maps, high genus | Short cycles $\to$ Poisson with Mirzakhani–Petri intensity; geometric comparison with $\mathrm{WP}_g$ | Janson–Louf 2021, 2022 |
| Unconstrained genus ($2p$-gon gluings, $p\to\infty$) | Local limit $\mathbb{H}^2$; systole and pants statistics as in $\mathrm{WP}_g$ | Budzinski–Curien–Petri 2019; Guth–Parlier–Young 2011 |
| Non-bipartite, general degrees, $\theta>0$ | Open | — |
| $\theta=1/2$ for triangulations | Open | — |
| Any global (diameter, systole, spectrum) statement at $\theta>0$ | Open except upper bounds | — |

## 5. Principal Obstacles

- **Genus is not a local quantity.** The spatial Markov property that drives peeling in the plane fails at fixed genus: cutting along an explored region can change the genus of the unexplored part in an uncontrolled way. Peeling therefore only controls balls of bounded radius, which is exactly the local regime already solved.
- **Non-uniform enumeration.** The fixed-genus asymptotics $t_g n^{5(g-1)/2}12^n$ have $t_g$ growing super-exponentially and error terms not uniform in $g$; the whole high-genus program rests on two-term ratio estimates $\beta_{n,g}=|\mathcal{T}_{n+1,g}|/|\mathcal{T}_{n,g}|$, which are known to converge but with no quantitative rate strong enough to control $n^{\varepsilon}$-size regions.
- **Bijections lose the metric.** Chapuy–Marcus–Schaeffer and Chapuy–Dołęga bijections encode distances *to a single vertex* by a label process. In high genus the injectivity radius is $O(1)$ and the map is nonamenable, so a single label field is not enough to reconstruct the metric: geodesics between two points are not read off from labels.
- **No compact limit object.** As $g\to\infty$ the surfaces leave any Gromov–Hausdorff-precompact family; diameters are $\Theta(\log n)$, not $n^{1/4}$, so the Brownian-surface machinery has no target. One must work in a local-global (Benjamini–Schramm plus mesoscopic) topology for which no uniqueness/rigidity theory exists.
- **Nonamenability blocks concentration.** Standard subadditivity and Efron–Stein arguments that give concentration for $n^{1/4}$-scale planar quantities degrade exponentially in exponentially growing balls.
- **The surface side is not discrete.** Mirzakhani's integration formula has no combinatorial analogue: there is no formula counting genus-$g$ maps with a prescribed pants decomposition with error uniform in $g$.

## 6. The Gap

Proven: convergence of the law of $B_r(T_{n,g_n})$ for every **fixed** $r$, for $\theta\in[0,1/2)$. Conjectured: convergence of statistics at scale $r\sim\varepsilon\log n$ and of global functionals.

The precise missing step is a **transfer from local to mesoscopic scales**. Since $|B_r(\mathbb{T}_\lambda)|\approx e^{\kappa r}$, matching $|B_r|$ with the total volume $n$ requires $r\approx \kappa^{-1}\log n$, so the exchange of limits $\lim_{n}\lim_{r}$ vs $\lim_{r}\lim_{n}$ is not justified by any current tightness estimate. Two concrete sub-gaps:

1. **Cycle-counting for maps with faces.** Janson–Louf's Poisson short-cycle theorem is proved only for unicellular maps ($F=1$), where the CMS bijection reduces the problem to trees. For $F=2n$ there is no such reduction.
2. **Uniformization.** Even with matched cycle statistics, no theorem converts a discrete map with mean degree $6/(1-2\theta)$ into a hyperbolic metric with controlled distortion, uniformly in $g$.

## 7. Current Research (as of June 2026)

- **Paris school (Curien, Budzinski, Louf, Marzouk).** Extending the ratio-estimate method to non-bipartite maps and to $\theta\to1/2$; quantitative peeling with genus-tracking. *(frontier — verify)* Preprints claiming $O(\log n)$ two-sided diameter bounds at $\theta>0$ circulate but the lower bound remains the harder half.
- **Uppsala/Paris (Janson, Louf).** Poisson-cycle statistics beyond unicellular maps, via mixed-face-count interpolation.
- **Random hyperbolic surfaces (Mirzakhani school: Petri, Wu, Xue, Lipnowski, Wright, Anantharaman, Monk).** Spectral gap of $\mathrm{WP}_g$: $\lambda_1>3/16-\varepsilon$ (Wu–Xue; Lipnowski–Wright), with subsequent work pushing towards $1/4-\varepsilon$ *(frontier — verify)*. A discrete analogue — spectral gap of high-genus maps — is the natural test of Conjecture A.
- **Enumerative geometry (Aggarwal, Delecroix–Goujard–Zograf–Zorich).** Large-genus asymptotics of intersection numbers and strata volumes, supplying uniform-in-$g$ constants that the map side lacks.
- **Topological recursion / matrix models.** The $1/N$ expansion of one-matrix models resums to a "double-scaling in genus" regime that physicists identify with JT gravity; making this rigorous is an active line. *(frontier — verify)*

## 8. Future Work

- Prove a **local-global convergence theorem**: show that for $r_n=\varepsilon\log n$, $B_{r_n}(T_{n,g_n})$ is close in total variation to $B_{r_n}(\mathbb{T}_{\lambda(\theta)})$ conditioned on volume. This alone would give the diameter asymptotics.
- Develop a **discrete Mirzakhani integration formula**: count genus-$g$ maps with a marked separating cycle of length $\ell$, uniformly in $g$, and derive Poisson limits for cycles in maps with many faces.
- Settle **$\theta=1/2$**: identify the limit as $\lambda\to0$ and prove it is the tree-like object predicted by the unicellular case.
- Prove **universality (Conjecture C)** for non-bipartite face-degree profiles with only a second-moment assumption.
- Establish a **spectral gap** for $T_{n,g_n}$ and compare with $\mathrm{WP}_g$.

## 9. Key References

- **[Foundational]** O. Angel, O. Schramm. *Uniform infinite planar triangulations.* Communications in Mathematical Physics 241 (2003), 191–213.
- **[Foundational]** E. A. Bender, E. R. Canfield. *The asymptotic number of rooted maps on a surface.* Journal of Combinatorial Theory, Series A 43 (1986), 244–257.
- **[Foundational]** G. Chapuy, M. Marcus, G. Schaeffer. *A bijection for rooted maps on orientable surfaces.* SIAM Journal on Discrete Mathematics 23 (2009), 1587–1611.
- **[Foundational]** N. Curien. *Planar stochastic hyperbolic triangulations.* Probability Theory and Related Fields 165 (2016), 509–540.
- **[SOTA]** T. Budzinski, B. Louf. *Local limits of uniform triangulations in high genus.* Inventiones Mathematicae 223 (2021), 1–47.
- **[SOTA]** T. Budzinski, B. Louf. *Local limits of bipartite maps with prescribed face degrees in high genus.* Annals of Probability 50 (2022), 1059–1126.
- **[SOTA]** S. Janson, B. Louf. *Unicellular maps vs. hyperbolic surfaces in large genus: simple closed curves.* Annals of Probability 50 (2022), 1322–1349.
- **[SOTA]** S. Janson, B. Louf. *Short cycles in high genus unicellular maps.* Annales de l'IHP Probabilités et Statistiques 57 (2021), 1547–1564.
- **[SOTA]** O. Angel, G. Chapuy, N. Curien, G. Ray. *The local limit of unicellular maps in high genus.* Electronic Communications in Probability 18 (2013), no. 86.
- **[SOTA]** T. Budzinski, N. Curien, B. Petri. *Universality for random surfaces in unconstrained genus.* Electronic Journal of Combinatorics 26 (2019), \#P4.2.
- **[SOTA]** M. Mirzakhani, B. Petri. *Lengths of closed geodesics on random surfaces of large genus.* Commentarii Mathematici Helvetici 94 (2019), 869–889.
- **[SOTA]** M. Mirzakhani, P. Zograf. *Towards large genus asymptotics of intersection numbers on moduli spaces of curves.* GAFA 25 (2015), 1258–1289.
- **[SOTA]** A. Aggarwal. *Large genus asymptotics for intersection numbers and principal strata volumes.* Inventiones Mathematicae 226 (2021), 897–1010.
- **[SOTA]** Y. Wu, Y. Xue. *Random hyperbolic surfaces of large genus have first eigenvalues greater than $\frac{3}{16}-\epsilon$.* GAFA 32 (2022), 340–410.
- **[Related]** J. Bettinelli. *Scaling limits for random quadrangulations of positive genus.* Electronic Journal of Probability 15 (2010), 1594–1644.
- **[Related]** L. Guth, H. Parlier, R. Young. *Pants decompositions of random surfaces.* GAFA 21 (2011), 1069–1090.
- **[Survey]** N. Curien. *Peeling Random Planar Maps.* École d'Été de Probabilités de Saint-Flour, Lecture Notes in Mathematics 2335, Springer, 2023.
- **[Survey]** G. Miermont. *Aspects of random maps.* Saint-Flour lecture notes, 2014.

## 10. Worked Example / Concrete Special Case

Take $\theta=1/4$, i.e. $g_n=\lfloor n/4\rfloor$, and $T_n$ uniform on triangulations of $\Sigma_{g_n}$ with $2n$ faces.

**Step 1 — Euler count.** $F=2n$, $E=3n$, so
$$V=n+2-2g_n=n+2-\tfrac{n}{2}+O(1)=\tfrac{n}{2}+O(1).$$

**Step 2 — mean degree.** $\bar d=2E/V=6n/(n/2)=12$. Compare $\bar d=6$ for planar triangulations ($\theta=0$). Discrete Gauss–Bonnet: the average angle defect per vertex is $2\pi(1-\bar d/6)=-2\pi$, uniformly negative — the map is uniformly hyperbolic, unlike the flat planar case.

**Step 3 — local limit.** Budzinski–Louf give $T_n\to\mathbb{T}_{\lambda(1/4)}$ with $\lambda(1/4)\in(0,1/12)$ strictly subcritical, so $\mathbb{E}|B_r(\mathbb{T}_{\lambda})|\asymp e^{\kappa r}$ with $\kappa=\kappa(\lambda(1/4))>0$. The root degree of $\mathbb{T}_\lambda$ has mean $12$, consistent with Step 2 (a nontrivial consistency check: the local limit must reproduce the global degree average, which holds because uniform re-rooting makes the root vertex size-biased-free).

**Step 4 — what is proved and what is not.** For each fixed $r$, $\mathbb{P}(B_r(T_n)=b)\to\mathbb{P}(B_r(\mathbb{T}_\lambda)=b)$. Now set $r_n=\kappa^{-1}\log n$. Then $\mathbb{E}|B_{r_n}(\mathbb{T}_\lambda)|\asymp n$, i.e. balls of this radius already exhaust the map. Conjecture A predicts
$$\frac{\mathrm{diam}(T_n)}{\log n}\longrightarrow \frac{2}{\kappa}\quad\text{in probability},$$
the factor $2$ coming from the fact that a typical pair of vertices is at distance twice the "radius" in an exponentially growing nonamenable graph. **Nothing in the proof of Step 3 gives this**: the local convergence is not quantitative in $r$, and no tail bound rules out $o(n)$ vertices sitting at distance $\gg 2\kappa^{-1}\log n$.

**Step 5 — the surface comparison.** On the hyperbolic side, a $\mathrm{WP}_{g}$ surface has area $4\pi(g-1)$ and diameter $(2+o(1))\log g$, with the number of geodesics of length $\le L$ Poisson of mean $\int_0^L \frac{e^t+e^{-t}-2}{2t}dt\sim \frac{e^L}{2L}$. Matching areas, $4\pi(g_n-1)\leftrightarrow c\,n$, and matching exponential growth rates fixes the single constant $c(\theta)$ in Conjecture A. For unicellular maps ($F=1$) Janson–Louf verified exactly this matching of Poisson intensities; for $F=2n$ with $\theta=1/4$ it is open.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*