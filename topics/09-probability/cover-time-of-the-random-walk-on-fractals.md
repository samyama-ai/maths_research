---
id: 09-probability/cover-time-of-the-random-walk-on-fractals
title: "Cover Time of the Random Walk on Fractals"
topic: 09-probability
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Cover Time of the Random Walk on Fractals

> **Topic:** Probability & Stochastic Processes · **ID:** `09-probability/cover-time-of-the-random-walk-on-fractals` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Let $(G_n)_{n\ge 0}$ be the natural graph approximation sequence of a self-similar fractal (Sierpiński gasket, nested fractals, Sierpiński carpets, Vicsek trees, critical percolation clusters), and let $X$ be the discrete-time simple random walk on $G_n=(V_n,E_n)$. The **cover time** is

$$\tau_{\mathrm{cov}}^{(n)}=\max_{v\in V_n}\ \inf\{t\ge 0: X_t=v\},\qquad t_{\mathrm{cov}}(G_n)=\max_{x\in V_n}\mathbb{E}_x\big[\tau_{\mathrm{cov}}^{(n)}\big].$$

**Problem.** Determine the exact first-order asymptotics of $t_{\mathrm{cov}}(G_n)$, and the limit law of $\tau_{\mathrm{cov}}^{(n)}$ after centering and scaling.

**Conjecture (sharp constant).** For the level-$n$ Sierpiński gasket graph, with $N=|V_n|$, Hausdorff dimension $d_f=\log 3/\log 2$ and walk dimension $d_w=\log 5/\log 2$,

$$t_{\mathrm{cov}}(G_n)=\big(c^\ast+o(1)\big)\,n\,5^{\,n}=\big(c^\ast+o(1)\big)\,N^{d_w/d_f}\log_3 N ,\qquad d_w/d_f=\tfrac{\log 5}{\log 3}\approx 1.4650,$$

for an explicit constant $c^\ast\in(0,\infty)$, and $\tau_{\mathrm{cov}}^{(n)}$ centered by $t_{\mathrm{cov}}(G_n)$ and scaled by $5^n$ converges in law to a randomly shifted Gumbel-type limit.

A complete solution must (i) establish the two-sided constant $c^\ast$ (currently only $\asymp$ is known), (ii) identify the second-order term, and (iii) extend to fractals with no closed-form $d_w$ (carpets) and to random fractals. A disproof would exhibit a self-similar sequence where $t_{\mathrm{cov}}/(N^{d_w/d_f}\log N)$ oscillates without limit — a live possibility, since lattice-type log-periodic oscillation is endemic on fractals.

## 2. Mathematical Foundations

**Resistance form.** Assign unit conductance to each edge. Effective resistance $R_{\mathrm{eff}}(u,v)$ is the resistance metric of the Dirichlet form $\mathcal{E}(f,f)=\sum_{\{u,v\}\in E}(f(u)-f(v))^2$. Fractal graphs satisfy a *resistance scaling* relation: on the gasket, $R_{\mathrm{eff}}$ between two corners of a level-$n$ cell is $(5/3)^n$.

**Sub-Gaussian heat kernel.** Nested fractal graphs satisfy, for $d_s=2d_f/d_w$ (spectral dimension) and constants $c_i>0$,

$$p_t(x,y)\asymp t^{-d_s/2}\exp\!\left(-c\Big(\tfrac{d(x,y)^{d_w}}{t}\Big)^{\frac{1}{d_w-1}}\right),$$

with $d_s=2\log 3/\log 5\approx 1.365<2$: the walk is **strongly recurrent**, i.e. $R_{\mathrm{eff}}(x,y)\asymp d(x,y)^{d_w-d_f}$ and $\mathrm{diam}_R(V_n)\cdot|E_n|\asymp t_{\mathrm{hit}}^{\max}$.

**Commute-time identity.** $\mathbb{E}_u[\tau_v]+\mathbb{E}_v[\tau_u]=2|E|\,R_{\mathrm{eff}}(u,v)$.

**Gaussian free field.** Pin $v_0\in V_n$ and let $\eta=(\eta_v)$ be the centered Gaussian field with covariance $\mathbb{E}[\eta_u\eta_v]=G_{v_0}(u,v)/\deg(v)$, the Green function killed at $v_0$; equivalently $\mathbb{E}[(\eta_u-\eta_v)^2]=R_{\mathrm{eff}}(u,v)$.

**Theorem (Ding–Lee–Peres 2012).** For every finite connected graph,

$$t_{\mathrm{cov}}(G)\ \asymp\ |E|\,\Big(\mathbb{E}\sup_{v\in V}\eta_v\Big)^{2},$$

with universal implicit constants. **Theorem (Ding 2014).** For bounded-degree graphs with $t_{\mathrm{hit}}^{\max}=o(t_{\mathrm{cov}})$,

$$\sqrt{t_{\mathrm{cov}}(G)}=\big(1+o(1)\big)\sqrt{2|E|}\;\mathbb{E}\sup_{v\in V}\eta_v .$$

The proofs go through the Dynkin/Eisenbaum isomorphism theorems, which couple the local time field of the walk run to a fixed level with $\tfrac12(\eta+\sqrt{2s})^2$.

The problem is therefore *equivalent*, at first order, to computing the expected maximum of the GFF on the fractal graph — a field whose increments have variance $R_{\mathrm{eff}}(u,v)\asymp d(u,v)^{d_w-d_f}$, i.e. a **power-law-correlated, not log-correlated**, hierarchical field.

## 3. History & State of the Art (SOTA)

- **1988–1989.** Barlow–Perkins construct Brownian motion on the Sierpiński gasket with $d_w=\log 5/\log 2$ and sub-Gaussian bounds; Barlow–Bass construct it on the Sierpiński carpet. Uniqueness on carpets is settled only in Barlow–Bass–Kumagai–Teplyaev (2010).
- **1991.** Aldous determines cover-time asymptotics for $b$-ary trees and gives the general "$t_{\mathrm{cov}}\sim t_{\mathrm{hit}}\log|V|$ when hitting times are nearly homogeneous" heuristic.
- **1993–2001.** Kumagai and Fitzsimmons–Hambly–Kumagai obtain heat-kernel and resistance estimates for nested fractals; Kigami's *Analysis on Fractals* supplies the resistance-form framework.
- **2004.** Dembo–Peres–Rosen–Zeitouni prove $t_{\mathrm{cov}}(\mathbb{Z}_n^2)\sim \tfrac{4}{\pi}(n\log n)^2$ — the first sharp constant for a non-tree, the borderline case $d_s=2$.
- **2012.** Ding–Lee–Peres reduce cover times to GFF maxima up to universal constants, proving the Winkler–Zuckerman blanket-time conjecture. Combined with fractal resistance estimates this yields $t_{\mathrm{cov}}\asymp N^{d_w/d_f}\log N$ for nested fractal graphs — the current SOTA for fractals.
- **2014–2021.** Ding removes the constant for bounded-degree graphs and general trees; Zhai proves exponential concentration; Belius–Kistler give the subleading term in $\mathbb{Z}^2$; Cortines–Louidor–Saglietti and Dembo–Rosen–Zeitouni obtain the full limit law on the binary tree.
- **Status on genuine fractals.** Order of magnitude known; leading constant, second-order term, and limit law open for every fractal that is not a tree.

## 4. Partial Results / Verified Cases

- **Trees (solved completely).** $b$-ary tree of depth $n$: $\sqrt{\tau_{\mathrm{cov}}}$ has a randomly shifted Gumbel limit after centering by $\sqrt{2|E|}\,(m_n)$ with $m_n = \sqrt{2\log b}\,n-\tfrac{3}{2\sqrt{2\log b}}\log n$ — the branching-random-walk correction (Cortines–Louidor–Saglietti 2018; Dembo–Rosen–Zeitouni 2021). Vicsek-type fractals, being trees, fall inside this class.
- **$\mathbb{Z}^2$ torus, $d_s=2$.** $t_{\mathrm{cov}}\sim\frac4\pi (n\log n)^2$ (DPRZ 2004); second-order term $-\frac{4}{\pi}\cdot\frac{?}{}$ in the form $\sqrt{t_{\mathrm{cov}}/(2|E|)} = \sqrt{2/\pi}\,(\log n - \tfrac{3}{4}\log\log n)+O(1)$ (Belius–Kistler 2017); tightness on the sphere (Belius–Rosen–Zeitouni 2020).
- **All nested fractals (order of magnitude).** For gasket-type graphs with $d_s<2$: $t_{\mathrm{cov}}(G_n)\asymp |E_n|\cdot \mathrm{diam}_R(V_n)\cdot \log|V_n| \asymp N^{d_w/d_f}\log N$, with universal two-sided constants, by DLP 2012 plus Kumagai's resistance estimates. Gasket: $\asymp n5^n$; $d$-dimensional gasket: $\asymp (d+3)^n n$ with $d_w=\log(d+3)/\log 2$.
- **Maximum of the GFF.** On the level-$n$ gasket, $\mathbb{E}\sup_v\eta_v\asymp \sqrt{n}\,(5/3)^{n/2}$; the $\sqrt{n}$ entropic factor is proven two-sidedly by Fernique/Talagrand majorizing-measure bounds on the resistance metric.
- **Random fractals.** For the incipient infinite cluster on trees and high-dimensional lattices, and for critical Galton–Watson trees conditioned to survive, $d_w=3d_f/2$-type "Alexander–Orbach" behaviour gives $t_{\mathrm{cov}}\asymp N^{3/2}\log N$ (up to constants, quenched, in the tree case).
- **Blanket time.** $t_{\mathrm{bl}}\asymp t_{\mathrm{cov}}$ holds on all fractal graph sequences as a consequence of DLP.

## 5. Principal Obstacles

- **The GFF on a fractal is not log-correlated.** The whole machinery that gives sharp constants in $\mathbb{Z}^2$ and on trees — Gaussian multiplicative chaos, BRW-type second-moment truncation, the Bramson $-\frac{3}{2\theta}\log n$ correction — is calibrated to increments of variance $\log$. On the gasket the increment variance $(5/3)^{k}$ across scale $k$ grows geometrically, so the extremal process is dominated by the coarsest scales while the $\sqrt n$ entropy factor is generated by all scales at once. Neither the tree nor the $\mathbb{Z}^2$ normalization applies.
- **No exact recursion for the maximum.** Decimation gives a distributional recursion $M_n \stackrel{d}{=}$ (function of three dependent copies of $M_{n-1}$ plus a boundary-harmonic Gaussian), but the three copies are correlated through their common boundary triple, so the fixed-point equation is not of a solvable smoothing-transform type.
- **Log-periodic oscillation.** Fractal scaling is discrete ($2^{-n}$ dilations only). Quantities like $t_{\mathrm{cov}}/(N^{d_w/d_f}\log N)$ are expected to be asymptotically multiplicatively periodic in $n$, so the limit may fail to exist. Ruling this in or out requires control finer than any current renewal argument.
- **No spectral formula.** Sharp constants in $\mathbb{Z}^2$ come from explicit Green function asymptotics $G(x,y)=\frac{2}{\pi}\log|x-y|+\kappa+o(1)$. On fractals the Green function has no closed form; the additive constant analogue is a nonexplicit periodic function.
- **Carpets have no explicit $d_w$.** Even the exponent $d_w/d_f$ in the conjecture is a non-explicit real number for Sierpiński carpets; only $d_f<d_w<d_f+1$-type bounds and numerics exist.
- **Late points.** The multifractal geometry of $\alpha$-late points, understood in $\mathbb{Z}^2$ (DPRZ), lacks a fractal analogue because the required exact Green-function decomposition is unavailable.

## 6. The Gap

Proven: $t_{\mathrm{cov}}(G_n)=\Theta(n5^n)$ on the gasket, with the reduction $\sqrt{t_{\mathrm{cov}}}=(1+o(1))\sqrt{2|E_n|}\,\mathbb{E}\sup\eta$ valid because $t_{\mathrm{hit}}^{\max}\asymp 5^n=o(n5^n)$.

Conjectured: existence of $\lim_n \mathbb{E}\sup_v\eta_v \big/ \big(\sqrt n\,(5/3)^{n/2}\big)=a^\ast$, whence $c^\ast=6(a^\ast)^2$ via $2|E_n|=6\cdot 3^n$.

**The gap is exactly one statement:** does the rescaled GFF maximum on the gasket converge, and to what? Everything else in the first-order problem is already a theorem. The second-order problem — a Bramson-type logarithmic correction and a decorated-Poisson extremal process for $\eta$ on a power-law-correlated hierarchical field — has no precedent in the literature.

## 7. Current Research (as of June 2026)

- **Kyoto / Kobe (Kumagai, Croydon, Nakajima, Kajino).** Resistance-form scaling limits and heat-kernel fluctuation; Kajino's work on log-periodicity and on the exact short-time behaviour of fractal heat kernels bears directly on whether the cover-time constant oscillates. *(frontier — verify)*
- **Extrema of hierarchical Gaussian fields (Kistler, Biskup, Louidor, Schweiger).** Programs extending the multiscale refinement of the second-moment method beyond log-correlation; Schweiger's work on membrane-model and non-log-correlated maxima is the closest technical template. *(frontier — verify)*
- **Abe and collaborators** continue the "cover times via GFF / late points" line begun for trees and $\mathbb{Z}^2$; late points at multiples of the cover time on strongly recurrent graphs is an active thread. *(frontier — verify)*
- **Random-media cover times.** Cover times of critical clusters, random recursive/hierarchical graphs and random conductance models on fractals, where quenched constants are expected to be random. *(frontier — verify)*
- **Numerics.** Physics-literature estimates of cover-time distributions on gaskets and carpets (Chupeau–Bénichou–Voituriez-type universality of cover-time distributions) suggest a Gumbel limit and provide numerical targets for $c^\ast$.

## 8. Future Work

1. **Prove convergence of $\mathbb{E}\sup\eta/(\sqrt n (5/3)^{n/2})$** on the gasket, or exhibit oscillation. Route: a multiscale refinement of the second-moment method adapted to geometric variance increments.
2. **Isolate the second-order term.** Determine whether the correction is $\Theta(\log n)$ (BRW-like) or $\Theta(1)$-oscillatory.
3. **Limit law.** Show tightness of $\tau_{\mathrm{cov}}^{(n)}/5^n$ around its mean, then identify the law using Zhai-type exponential concentration plus a decorated point-process limit.
4. **Uniform theory for resistance metrics.** Formulate a general theorem: for graph sequences with $R_{\mathrm{eff}}(u,v)\asymp d^{\beta}$, $\beta>0$, the cover time constant depends only on the scaling limit of the resistance form — a resistance-metric analogue of DLP with sharp constants.
5. **Carpets.** Transfer results to Sierpiński carpets using BBKT uniqueness, where $d_w$ itself remains non-explicit.
6. **Late-point multifractality** on fractals: compute $\dim_H$ of $\alpha$-late points in the fractal metric.

## 9. Key References

- **[Foundational]** M. T. Barlow, E. A. Perkins. *Brownian motion on the Sierpinski gasket.* Probability Theory and Related Fields **79** (1988), 543–623.
- **[Foundational]** M. T. Barlow, R. F. Bass. *The construction of Brownian motion on the Sierpinski carpet.* Annales de l'IHP Probabilités et Statistiques **25** (1989), 225–257.
- **[Foundational]** D. Aldous. *Threshold limits for cover times.* Journal of Theoretical Probability **4** (1991), 197–211.
- **[Foundational]** J. Kigami. *Analysis on Fractals.* Cambridge University Press, 2001.
- **[SOTA]** J. Ding, J. R. Lee, Y. Peres. *Cover times, blanket times, and majorizing measures.* Annals of Mathematics **175** (2012), 1409–1471.
- **[SOTA]** J. Ding. *Asymptotics of cover times via Gaussian free fields: bounded-degree graphs and general trees.* Annals of Probability **42** (2014), 464–496.
- **[SOTA]** A. Dembo, Y. Peres, J. Rosen, O. Zeitouni. *Cover times for Brownian motion and random walks in two dimensions.* Annals of Mathematics **160** (2004), 433–464.
- **[SOTA]** D. Belius, N. Kistler. *The subleading order of two dimensional cover times.* Probability Theory and Related Fields **167** (2017), 461–552.
- **[SOTA]** A. Cortines, O. Louidor, S. Saglietti. *A scaling limit for the cover time of the binary tree.* Advances in Mathematics **391** (2021), 107974.
- **[SOTA]** A. Dembo, J. Rosen, O. Zeitouni. *Limit law for the cover time of a random walk on a binary tree.* Annales de l'IHP Probabilités et Statistiques **57** (2021), 830–855.
- **[SOTA]** A. Zhai. *Exponential concentration of cover times.* Electronic Journal of Probability **23** (2018), paper 32.
- **[SOTA]** M. T. Barlow, R. F. Bass, T. Kumagai, A. Teplyaev. *Uniqueness of Brownian motion on Sierpiński carpets.* Journal of the European Mathematical Society **12** (2010), 655–701.
- **[Survey]** T. Kumagai. *Random Walks on Disordered Media and their Scaling Limits.* Lecture Notes in Mathematics 2101, Springer, 2014.
- **[Survey]** M. T. Barlow. *Diffusions on fractals.* Lectures on Probability Theory and Statistics (Saint-Flour XXV, 1995), Lecture Notes in Mathematics 1690, Springer, 1998.
- **[Survey]** A. Telcs. *The Art of Random Walks.* Lecture Notes in Mathematics 1885, Springer, 2006.
- **[Reference]** M. B. Marcus, J. Rosen. *Markov Processes, Gaussian Processes, and Local Times.* Cambridge University Press, 2006.

## 10. Worked Example / Concrete Special Case

**Level-$n$ Sierpiński gasket graph $G_n$.** Vertices $|V_n|=\tfrac{3(3^n+1)}{2}$, edges $|E_n|=3^{n+1}$, all degrees $2$ or $4$.

*Step 1 — resistance.* Replacing each level-$1$ cell by a star (Y–$\Delta$) multiplies unit resistance by $5/3$ per level, so the corner-to-corner resistance is

$$R_n=R_{\mathrm{eff}}(a,b)=(5/3)^n .$$

*Step 2 — commute time.* The identity gives exactly

$$\mathbb{E}_a[\tau_b]+\mathbb{E}_b[\tau_a]=2|E_n|R_n=2\cdot 3^{n+1}\cdot (5/3)^n=6\cdot 5^{\,n}.$$

By symmetry $\mathbb{E}_a[\tau_b]=3\cdot 5^n$. For $n=3$: $|V_3|=42$, $|E_3|=81$, $R_3=125/27\approx 4.63$, commute time $=750$, $\mathbb{E}_a[\tau_b]=375$. This also recovers $d_w$: hitting time across a cell of diameter $2^n$ is $\asymp 5^n=(2^n)^{\log 5/\log 2}$.

*Step 3 — maximal hitting time.* Strong recurrence gives $t_{\mathrm{hit}}^{\max}=\max_{u,v}\mathbb{E}_u[\tau_v]\asymp |E_n|\,\mathrm{diam}_R \asymp 5^n$.

*Step 4 — cover time upper bound (Matthews).* $t_{\mathrm{cov}}\le t_{\mathrm{hit}}^{\max}\big(1+\tfrac12+\cdots+\tfrac1{|V_n|}\big)\le C 5^n\log|V_n| \le C' n\,5^n .$

*Step 5 — matching lower bound.* Take the $3^k$ corner-vertices of level-$k$ cells, $k=n$. Their pairwise resistances are $\asymp (5/3)^{n}$ at the top scale, so the GFF restricted to them has $\mathbb{E}\sup \gtrsim \sqrt{n}\,(5/3)^{n/2}$ by a Sudakov/majorizing-measure estimate down the hierarchy. DLP then gives

$$t_{\mathrm{cov}}(G_n)\ \gtrsim\ |E_n|\big(\sqrt n (5/3)^{n/2}\big)^2 = 3^{n+1}\cdot n\cdot (5/3)^n = 3n\,5^{\,n}.$$

*Conclusion.* $t_{\mathrm{cov}}(G_n)=\Theta(n5^n)$, i.e. $\Theta\!\left(N^{\log 5/\log 3}\log N\right)$ with $\log 5/\log 3\approx1.4650$. Ding's theorem then makes the sharp constant *equal* to $6\lim_n \big(\mathbb{E}\sup\eta\big)^2/\big(n(5/3)^n\big)$ — and it is precisely this limit whose existence is unproven.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*