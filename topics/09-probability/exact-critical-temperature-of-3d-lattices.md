---
id: 09-probability/exact-critical-temperature-of-3d-lattices
title: "Exact Critical Temperature of 3D Lattices"
topic: 09-probability
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Exact Critical Temperature of 3D Lattices

> **Topic:** Probability & Stochastic Processes · **ID:** `09-probability/exact-critical-temperature-of-3d-lattices` · **Status:** open

## 1. Problem Statement / Conjecture

For two-dimensional lattices, the critical points of the two canonical models of statistical mechanics are known in closed form: the square-lattice Ising model has $\sinh(2K_c)=1$, i.e. $K_c=\tfrac12\ln(1+\sqrt2)$ (Kramers–Wannier 1941, Onsager 1944), and square-lattice bond percolation has $p_c=\tfrac12$ (Kesten 1980). In three dimensions no such formula is known for any lattice.

**The problem.** Determine, in closed form, the critical parameter of a nearest-neighbour model on a three-dimensional lattice $\mathcal{L}\subset\mathbb{R}^3$ — concretely:

1. the Ising critical coupling $K_c(\mathcal{L}) = J/(k_BT_c)$ on the simple cubic (sc), body-centred cubic (bcc) or face-centred cubic (fcc) lattice;
2. the bond or site percolation threshold $p_c(\mathcal{L})$ on the same lattices.

A complete solution means either (a) an explicit expression for $K_c$ or $p_c$ in terms of standard constants and functions (algebraic number, value of a hypergeometric or elliptic function, root of an explicitly given analytic equation), together with a proof; or (b) a theorem showing no such expression exists in a precisely defined class — e.g. that $p_c(\mathbb{Z}^3,\text{bond})$ is not algebraic, or a formalised version of Fisher's expectation that the 3D Ising model admits no integrable structure. Both directions are open; even irrationality of $p_c(\mathbb{Z}^3)$ is unproven.

## 2. Mathematical Foundations

**Ising model.** On a finite $\Lambda\subset\mathcal{L}$ with configurations $\sigma\in\{-1,+1\}^{\Lambda}$,
$$H_\Lambda(\sigma)=-J\sum_{\{x,y\}\in E(\Lambda)}\sigma_x\sigma_y,\qquad \mu_{\Lambda,\beta}(\sigma)=\frac{e^{-\beta H_\Lambda(\sigma)}}{Z_\Lambda(\beta)},\qquad K=\beta J .$$
Spontaneous magnetisation $m^*(\beta)=\lim_{\Lambda\uparrow\mathcal{L}}\langle\sigma_0\rangle^{+}_{\Lambda,\beta}$ is non-decreasing in $\beta$, and
$$K_c(\mathcal{L})=\inf\{K>0:\ m^*(K)>0\}.$$

**Percolation.** Each edge (resp. vertex) is open independently with probability $p$; $\theta(p)=\mathbb{P}_p(|C_0|=\infty)$ for the cluster $C_0$ of the origin, and
$$p_c(\mathcal{L})=\sup\{p\in[0,1]:\theta(p)=0\}.$$
The two are linked by the FK–random-cluster measure $\phi_{p,q}$ with $q=2$ and $p=1-e^{-2K}$ (Fortuin–Kasteleyn 1972); $\{K_c\}$ and $\{p_c(q=2)\}$ correspond under this map.

**Duality — the 2D mechanism and its 3D failure.** In 2D the high-temperature/low-temperature duality
$$\sinh(2K)\,\sinh(2K^*)=1,\qquad e^{-2K^*}=\tanh K,$$
maps the square lattice to itself; assuming a unique transition, the critical point is the fixed point $\sinh 2K_c=1$. In 3D the same expansion maps the Ising model not to an Ising model but to $\mathbb{Z}_2$ **lattice gauge theory** on the dual lattice (Wegner 1971):
$$Z^{\text{Ising}}_{\mathbb{Z}^3}(K)\ \longleftrightarrow\ Z^{\mathbb{Z}_2\text{-gauge}}_{\mathbb{Z}^3}(K^*),$$
so the duality relation constrains $K_c^{\text{Ising}}$ only in terms of the (independently unknown) gauge-theory critical coupling. Likewise bond percolation on $\mathbb{Z}^3$ is dual to *plaquette* percolation (Aizenman–Chayes–Chayes–Fröhlich–Russo 1983), not to bond percolation. No self-duality survives in $d=3$.

**Integrability.** In 2D the transfer matrices commute via the Yang–Baxter equation; the 3D analogue is Zamolodchikov's tetrahedron equation, whose known solutions (Bazhanov–Baxter 1992) are not the Ising model.

**Numerics (best known values).**
$$K_c^{\text{sc}}=0.221\,654\,626(5),\quad k_BT_c/J = 4.511\,523\,2(17)\ \ \text{(Ferrenberg–Xu–Landau 2018)},$$
$$p_c^{\text{bond}}(\mathbb{Z}^3)=0.248\,811\,82(10),\qquad p_c^{\text{site}}(\mathbb{Z}^3)=0.311\,607\,7(2).$$

## 3. History & State of the Art (SOTA)

- **1941–1944.** Kramers–Wannier locate $T_c$ of the square lattice by duality; Onsager solves the model exactly. The 3D case is immediately singled out as the hard one.
- **1957.** Broadbent–Hammersley define percolation and prove $0<p_c(\mathbb{Z}^d)<1$ for $d\ge2$.
- **1960s–80s.** High-temperature series expansions (Domb, Sykes, Fisher–Gaunt, Nickel) yield $K_c^{\text{sc}}$ to $\sim6$ digits and the large-$d$ expansion $K_c=\frac{1}{2d}+\frac{1}{(2d)^2}+\dots$
- **1980.** Kesten proves $p_c=\tfrac12$ for square-lattice bonds — the last 2D case needing rigour.
- **1982–1990.** Aizenman and Fröhlich prove triviality/mean-field behaviour for Ising in $d\ge5$; Hara–Slade's lace expansion gives mean-field percolation exponents for $d\ge19$.
- **2000.** Istrail proves computing the Ising partition function on non-planar lattices (including sc) is NP-hard, formal evidence against a simple closed form.
- **2007–2008.** Z.-D. Zhang's conjectured 3D solution is refuted by Wu, McCoy, Fisher and Chayes.
- **2012–2016.** Conformal bootstrap pins the 3D Ising *universal* data to extreme precision ($\nu=0.629971(4)$, $\eta=0.0362978(20)$) — but $K_c$ is non-universal and untouched by it.
- **2013–2018.** Monte Carlo with cluster algorithms and GPU hardware reaches 9–10 significant digits for $K_c^{\text{sc}}$ and $p_c$. No digit sequence has matched any proposed closed form.

## 4. Partial Results / Verified Cases

**Exactly solved (closed form known).**
- All planar 2D lattices with Ising: square $\tfrac12\ln(1+\sqrt2)$; triangular $\tfrac14\ln 3$; honeycomb $\tfrac12\,\mathrm{arccosh}\,2$ — via star–triangle.
- 2D percolation: square bond $\tfrac12$; triangular site $\tfrac12$; triangular bond $2\sin(\pi/18)$; honeycomb bond $1-2\sin(\pi/18)$; the Ziff–Scullard family of "exactly solvable" 2D lattices (martini, checkerboard, and self-dual triangular-hypergraph classes), 2006.
- **Bethe lattice / regular tree** of degree $z$: $p_c=1/(z-1)$ and $\tanh K_c=1/(z-1)$ exactly — a "$d=\infty$" surrogate.
- $d=1$: $K_c=\infty$, $p_c=1$.

**Rigorous structural results in $d=3$ (but no formula).**
- Sharpness of the transition: exponential decay for $p<p_c$ (Menshikov 1986; Aizenman–Barsky 1987; new proof Duminil-Copin–Tassion 2016).
- Continuity: $m^*(K_c)=0$ for Ising on $\mathbb{Z}^3$ (Aizenman–Duminil-Copin–Sidoravicius 2015). The percolation analogue $\theta(p_c)=0$ on $\mathbb{Z}^3$ remains **open**.
- Mean-field regime: percolation exponents and the $1/(2d)$-expansion $p_c=\frac{1}{2d}+\frac{1}{(2d)^2}+\frac{7}{2(2d)^3}+O(d^{-4})$ are proven for $d\ge19$ (Hara–Slade 1990, 1995), reduced to $d\ge11$ (Fitzner–van der Hofstad 2017). Ising triviality: $d\ge5$, and marginally $d=4$ (Aizenman–Duminil-Copin 2021). $d=3$ falls in the gap.
- Rigorous numerical bounds: e.g. $p_c^{\text{bond}}(\mathbb{Z}^3)<0.5$ and Balister–Bollobás–Walters-style interval bounds; these are certified enclosures, not closed forms.

## 5. Principal Obstacles

- **No self-duality.** The single mechanism that fixes 2D critical points is absent: Wegner duality sends spins to gauge fields, so the fixed-point argument has no 3D analogue.
- **No integrability.** Transfer matrices in 3D do not form a commuting family; the tetrahedron equation admits no Ising solution, so Baxter-style exact diagonalisation is unavailable.
- **Complexity barrier.** Istrail (2000): exact evaluation of $Z$ on non-planar lattices is NP-hard, and the 3D Ising ground-state problem is NP-complete (Barahona 1982). A closed-form $K_c$ need not contradict this, but any Pfaffian/dimer route — the engine of the 2D solution — is blocked.
- **Non-universality.** The bootstrap, the RG and $\varepsilon$-expansion all compute universal quantities (exponents, amplitude ratios). $K_c$ depends on lattice microstructure and is invisible to every conformal or continuum method.
- **No convergent lattice expansion.** High- and low-temperature series have finite radius of convergence limited by non-physical singularities; extrapolation (Padé, differential approximants) gives digits, never identities.
- **Rigorous PDE/probabilistic tools stop short.** Lace expansion needs $d$ large for the diagrammatic estimates to close; discrete-holomorphicity (Smirnov) is intrinsically two-dimensional.

## 6. The Gap

Proven: existence, uniqueness and sharpness of the transition in 3D, high-dimensional asymptotics, universal critical data, and ~10-digit numerics. Missing: any **algebraic or analytic characterisation** of the 3D critical point.

The precise barrier: in 2D one has an involution $K\mapsto K^*$ on the model's own parameter space plus uniqueness of the transition, which forces $K_c=K^*_c$. In 3D one must either (i) find a self-map of a parameter space containing the 3D Ising/percolation model whose fixed set is the critical manifold — none is known and Wegner duality shows the naive candidate leaves the class — or (ii) prove a transcendence/inexpressibility theorem, for which there is currently no technique: no result exists ruling out even that $p_c(\mathbb{Z}^3)$ is rational.

## 7. Current Research (as of June 2026)

- **Rigorous 3D probability** (Duminil-Copin's group, IHES/Geneva; Hutchcroft, Caltech): $\theta(p_c)=0$ on $\mathbb{Z}^3$, sharp near-critical estimates, and the random-cluster model for $q\ge1$ in $d=3$.
- **High-dimension reduction**: van der Hofstad, Fitzner and collaborators pushing lace-expansion methods below $d=11$; a rigorous route to $d=3$ is not expected but each step tightens the $1/(2d)$ picture. *(frontier — verify)*
- **Bootstrap for non-universal data**: attempts to combine conformal-bootstrap operator data with lattice perturbation theory to predict $K_c$ to high accuracy — an approximation programme, not an exact-solution programme. *(frontier — verify)*
- **Tensor-network/tensor-RG** (Xie–Xiang and successors): coarse-graining estimates of $K_c^{\text{sc}}$ competitive with Monte Carlo, and searches for 3D fixed-point tensors with exact structure. *(frontier — verify)*
- **Exact-threshold combinatorics** (Ziff, Scullard, Grimmett–Manolescu): extending the 2D star–triangle/hypergraph families; no 3D member has been found.

## 8. Future Work

- Search systematically for a 3D generalisation of the star–triangle relation acting on a *larger* family (e.g. anisotropic couplings, decorated lattices) whose fixed manifold is computable.
- Prove $\theta(p_c)=0$ on $\mathbb{Z}^3$ — the consensus next rigorous target, likely a prerequisite for any structural characterisation of $p_c$.
- Develop transcendence tools for lattice constants: even a conditional statement ("$p_c(\mathbb{Z}^3)$ is not a root of any polynomial of degree $\le D$ and height $\le H$") would be a first.
- Certify the numerics: interval-arithmetic enclosures of $K_c^{\text{sc}}$ tight enough to exclude candidate closed forms by inverse symbolic search.
- Explore whether Istrail-style complexity lower bounds can be converted into a formal non-solvability statement for a defined class of expressions.

## 9. Key References

- **[Foundational]** H. A. Kramers, G. H. Wannier. *Statistics of the Two-Dimensional Ferromagnet. Part I.* Physical Review 60, 252–262, 1941.
- **[Foundational]** L. Onsager. *Crystal Statistics. I. A Two-Dimensional Model with an Order-Disorder Transition.* Physical Review 65, 117–149, 1944.
- **[Foundational]** S. R. Broadbent, J. M. Hammersley. *Percolation processes I. Crystals and mazes.* Proc. Cambridge Philos. Soc. 53, 629–641, 1957.
- **[Foundational]** F. J. Wegner. *Duality in Generalized Ising Models and Phase Transitions without Local Order Parameters.* J. Math. Phys. 12, 2259–2272, 1971.
- **[Foundational]** H. Kesten. *The critical probability of bond percolation on the square lattice equals 1/2.* Comm. Math. Phys. 74, 41–59, 1980.
- **[Book]** R. J. Baxter. *Exactly Solved Models in Statistical Mechanics.* Academic Press, 1982.
- **[Book]** G. Grimmett. *Percolation*, 2nd ed. Springer, 1999.
- **[Structural]** T. Hara, G. Slade. *Mean-field critical behaviour for percolation in high dimensions.* Comm. Math. Phys. 128, 333–391, 1990.
- **[Structural]** T. Hara, G. Slade. *The self-avoiding-walk and percolation critical points in high dimensions.* Combin. Probab. Comput. 4, 197–215, 1995.
- **[Structural]** M. Aizenman, H. Duminil-Copin, V. Sidoravicius. *Random currents and continuity of Ising model's spontaneous magnetization.* Comm. Math. Phys. 334, 719–742, 2015.
- **[Structural]** H. Duminil-Copin, V. Tassion. *A new proof of the sharpness of the phase transition for Bernoulli percolation and the Ising model.* Comm. Math. Phys. 343, 725–745, 2016.
- **[Structural]** R. Fitzner, R. van der Hofstad. *Mean-field behavior for nearest-neighbor percolation in $d>10$.* Electron. J. Probab. 22, paper 43, 2017.
- **[Structural]** M. Aizenman, H. Duminil-Copin. *Marginal triviality of the scaling limits of critical 4D Ising and $\phi_4^4$ models.* Annals of Mathematics 194, 163–235, 2021.
- **[Complexity]** S. Istrail. *Statistical mechanics, three-dimensionality and NP-completeness I.* Proc. 32nd ACM STOC, 87–96, 2000.
- **[Refutation]** F. Y. Wu, B. M. McCoy, M. E. Fisher, L. Chayes. *Comment on a recent conjectured solution of the three-dimensional Ising model.* Philosophical Magazine 88, 3093–3095, 2008.
- **[SOTA / Numerics]** A. M. Ferrenberg, J. Xu, D. P. Landau. *Pushing the limits of Monte Carlo simulations for the three-dimensional Ising model.* Phys. Rev. E 97, 043301, 2018.
- **[SOTA / Numerics]** J. Wang, Z. Zhou, W. Zhang, T. M. Garoni, Y. Deng. *Bond and site percolation in three dimensions.* Phys. Rev. E 87, 052107, 2013.
- **[SOTA / Numerics]** X. Xu, J. Wang, J.-P. Lv, Y. Deng. *Simultaneous analysis of three-dimensional percolation models.* Frontiers of Physics 9, 113–119, 2014.
- **[SOTA / Bootstrap]** F. Kos, D. Poland, D. Simmons-Duffin, A. Vichi. *Precision islands in the Ising and O(N) models.* JHEP 08 (2016) 036.
- **[Exact 2D thresholds]** R. M. Ziff, C. R. Scullard. *Exact bond percolation thresholds in two dimensions.* J. Phys. A 39, 15083–15090, 2006.
- **[Survey]** H. Duminil-Copin. *Lectures on the Ising and Potts models on the hypercubic lattice.* In *Random Graphs, Phase Transitions, and the Gaussian Free Field*, Springer PROMS 304, 35–161, 2020.

## 10. Worked Example / Concrete Special Case

**Why the 2D argument gives $K_c$ and why it dies in 3D.**

*Step 1 — high-temperature expansion (square lattice).* Using $e^{K\sigma_x\sigma_y}=\cosh K\,(1+\sigma_x\sigma_y\tanh K)$,
$$Z(K)=(\cosh K)^{|E|}2^{|V|}\sum_{\gamma\in\mathcal{E}}(\tanh K)^{|\gamma|},$$
where $\mathcal{E}$ is the set of even subgraphs (every vertex has even degree), because $\sum_{\sigma_x=\pm1}\sigma_x^k=0$ for odd $k$.

*Step 2 — low-temperature expansion on the dual.* Writing configurations by their domain walls on the dual lattice $\mathcal{L}^*$,
$$Z^*(K^*)=2\,e^{K^*|E^*|}\sum_{\gamma^*\in\mathcal{E}^*}e^{-2K^*|\gamma^*|}.$$
Both sums run over even subgraphs. In 2D, $\mathcal{L}^*=\mathcal{L}$ for the square lattice, so the two series are identical once
$$e^{-2K^*}=\tanh K \iff \sinh(2K)\sinh(2K^*)=1 .$$

*Step 3 — fixed point.* $K\mapsto K^*$ is a decreasing involution on $(0,\infty)$ with the unique fixed point $\sinh 2K=1$, i.e. $K=\tfrac12\ln(1+\sqrt2)=0.4406868\ldots$. If the transition is unique it must sit there. Numerically $k_BT_c/J = 2/\ln(1+\sqrt2)=2.269185\ldots$ — matched to all measured digits.

*Step 4 — the 3D obstruction, explicitly.* On $\mathbb{Z}^3$ the high-temperature objects are still closed loops (1-dimensional), but the low-temperature domain walls are **surfaces** (2-dimensional), living on plaquettes of the dual lattice. The map therefore sends
$$\text{Ising spins on }\mathbb{Z}^3\ \longmapsto\ \mathbb{Z}_2\ \text{gauge variables on plaquettes of }(\mathbb{Z}^3)^*,$$
with the *same* relation $e^{-2K^*}=\tanh K$ but between **two different models**. The self-consistency equation becomes
$$K_c^{\text{Ising}}\ \text{and}\ K_c^{\text{gauge}}\ \text{satisfy}\ \sinh(2K_c^{\text{Ising}})\sinh(2K_c^{\text{gauge}})=1,$$
one equation in two unknowns. Inserting the measured $K_c^{\text{Ising,sc}}=0.221654626$ predicts $K_c^{\text{gauge}}=\tfrac12\,\mathrm{arcsinh}\big(1/\sinh(0.443309252)\big)=0.7614133\ldots$, which agrees with Monte Carlo values of the $\mathbb{Z}_2$ gauge transition — a genuine, verified consequence of duality, and precisely *not* a determination of $K_c$. Closing the system requires one further independent exact relation, which is exactly what is missing.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*