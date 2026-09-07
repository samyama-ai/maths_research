---
id: 09-probability/mixing-time-of-the-glauber-dynamics-for-the-ising-model
title: "Mixing Time of the Glauber Dynamics for the Ising Model"
topic: 09-probability
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Mixing Time of the Glauber Dynamics for the Ising Model

> **Topic:** Probability & Stochastic Processes · **ID:** `09-probability/mixing-time-of-the-glauber-dynamics-for-the-ising-model` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Determine, as a function of the underlying graph and the inverse temperature $\beta$, the total-variation mixing time $t_{\mathrm{mix}}$ of the single-site heat-bath (Glauber) dynamics for the ferromagnetic Ising model.

Three claims organize the field, all open in their general form.

- **(C1) Uniqueness ⇒ optimal mixing.** For every sequence of graphs $G_n$ of maximum degree $\Delta$ and every $\beta$ strictly inside the tree-uniqueness regime $\tanh\beta < 1/(\Delta-1)$, $t_{\mathrm{mix}} = \Theta(n\log n)$, and the dynamics exhibits **cutoff** with an $O(n)$-window.
- **(C2) Critical lattice exponent.** On the box $\Lambda_L = [1,L]^d \cap \mathbb{Z}^d$ at $\beta = \beta_c(d)$, $t_{\mathrm{mix}} = L^{z+o(1)}$ for a universal dynamical critical exponent $z = z(d)$, with $z(2) \approx 2.1665$. Existence of $z$ is not proven in any dimension.
- **(C3) Low-temperature boundary dependence.** On $\Lambda_L \subset \mathbb{Z}^2$ at $\beta > \beta_c$ with all-plus boundary, $t_{\mathrm{mix}} = L^{O(1)}$ (polynomial), whereas with free boundary $t_{\mathrm{mix}} = e^{\Theta(L)}$.

A complete resolution means matching upper and lower bounds up to the stated order, with the transition located exactly at the static phase-transition point.

## 2. Mathematical Foundations

Let $G=(V,E)$ be finite, $|V|=n$, configuration space $\Omega=\{-1,+1\}^V$. The Ising Gibbs measure at inverse temperature $\beta\ge 0$ with external field $h$ and boundary condition $\eta$ is
$$\pi(\sigma) = \frac{1}{Z}\exp\Big(\beta\sum_{\{u,v\}\in E}\sigma_u\sigma_v + h\sum_{v\in V}\sigma_v\Big),\qquad Z=\sum_{\sigma\in\Omega} e^{-H(\sigma)} .$$

**Glauber dynamics.** Continuous-time: each site carries a rate-1 Poisson clock; on ringing at $v$, resample $\sigma_v$ from $\pi(\cdot\mid \sigma_{V\setminus\{v\}})$, i.e. set $\sigma_v=+1$ with probability
$$p_v(\sigma) = \frac{1}{2}\Big(1+\tanh\big(\beta S_v(\sigma)+h\big)\Big),\qquad S_v(\sigma)=\sum_{u\sim v}\sigma_u .$$
This chain is reversible with respect to $\pi$ and irreducible, so $\pi$ is its unique stationary law.

**Mixing and relaxation.** With $d(t)=\max_{\sigma_0}\|\mathbb{P}_{\sigma_0}(\sigma_t\in\cdot)-\pi\|_{\mathrm{TV}}$, set $t_{\mathrm{mix}}(\varepsilon)=\inf\{t: d(t)\le\varepsilon\}$ and $t_{\mathrm{mix}}=t_{\mathrm{mix}}(1/4)$. The generator $\mathcal{L}$ has Dirichlet form
$$\mathcal{E}(f,f)=\sum_{v\in V}\mathbb{E}_\pi\big[\operatorname{Var}_{\pi}(f\mid \sigma_{V\setminus\{v\}})\big],\qquad \mathrm{gap}=\inf_{\operatorname{Var}_\pi f>0}\frac{\mathcal{E}(f,f)}{\operatorname{Var}_\pi f},$$
and $t_{\mathrm{rel}}=\mathrm{gap}^{-1}$ satisfies $(t_{\mathrm{rel}}-1)\log 2 \le t_{\mathrm{mix}}\le t_{\mathrm{rel}}\log(4/\pi_{\min})$. A log-Sobolev constant $\alpha$ gives the sharper $t_{\mathrm{mix}} = O(\alpha^{-1}\log\log \pi_{\min}^{-1})$.

**Cutoff.** A sequence has cutoff with window $w_n = o(t_{\mathrm{mix}}^{(n)})$ if $t_{\mathrm{mix}}^{(n)}(\varepsilon)-t_{\mathrm{mix}}^{(n)}(1-\varepsilon)=O(w_n)$ for every $\varepsilon$.

**Spatial mixing.** *Weak spatial mixing* (WSM): correlations between $\sigma_v$ and boundary conditions decay exponentially in $\mathrm{dist}(v,\partial\Lambda)$. *Strong spatial mixing* (SSM): the same decay holds uniformly over arbitrary subregions and boundary conditions. **Martinelli–Olivieri**: on $\mathbb{Z}^d$, SSM in all boxes is equivalent to a uniform (volume-independent) log-Sobolev constant, hence to $t_{\mathrm{mix}} = \Theta(n\log n)$.

**Tree uniqueness.** On the $\Delta$-regular tree with $h=0$, the Gibbs measure is unique iff $(\Delta-1)\tanh\beta \le 1$; on $\mathbb{Z}^d$ the static threshold is $\beta_c(d)$, with $\beta_c(2)=\tfrac12\log(1+\sqrt2)$.

**Spectral independence.** Writing $\Psi$ for the pairwise influence matrix $\Psi_{u,v}=\mathbb{P}(\sigma_v=+\mid \sigma_u=+)-\mathbb{P}(\sigma_v=+\mid\sigma_u=-)$, $\eta$-spectral independence means $\lambda_{\max}(\Psi)\le\eta$ uniformly over pinnings; combined with entropy factorization this yields $O(n\log n)$ mixing.

## 3. History & State of the Art (SOTA)

Glauber (1963) introduced the dynamics as a physically natural relaxation of the Ising model. The 1980s–90s produced the functional-analytic framework: Holley–Stroock, Zegarliński, Stroock–Zegarliński, and Schonmann–Shlosman established log-Sobolev and spatial-mixing equivalences; Martinelli–Olivieri (1994) proved the definitive statement that SSM in cubes ⟺ uniform spectral gap and log-Sobolev on $\mathbb{Z}^d$, and Martinelli–Olivieri–Schonmann proved WSM ⟹ SSM in $d=2$, so the fast-mixing regime on $\mathbb{Z}^2$ is exactly $\beta<\beta_c$.

Mean-field results came next: Levin–Łuczak–Peres (2010) gave cutoff at $\big(\tfrac{1}{2(1-\beta)}\big)n\log n$ for the Curie–Weiss model at $\beta<1$ and $e^{\Theta(n)}$ for $\beta>1$; Ding–Lubetzky–Peres (2009) resolved the critical window, $t_{\mathrm{mix}}\asymp n^{3/2}$ at $\beta=1$.

The lattice cutoff problem was settled by Lubetzky–Sly: cutoff at $\big(\tfrac{d}{2\lambda_\infty}\big)\log n$ within the SSM regime (*Inventiones*, 2013), then re-proved and extended by the *information percolation* method (*JAMS*, 2016), which also handles small external fields and gives an $O(1)$ window. Lubetzky–Sly (2012) proved polynomial mixing at criticality on $\mathbb{Z}^2$: $L^{c}$ for an unspecified universal $c$.

Since 2020 the combinatorial side has been transformed by **spectral independence**, introduced by Anari–Liu–Oveis Gharan (2020) and pushed to entropy factorization by Chen–Liu–Vigoda (2021): $O(n\log n)$ mixing on *every* graph of max degree $\Delta$ throughout the tree-uniqueness regime, with no geometric assumption. In parallel, Eldan–Koehler–Zeitouni (2022) and Chen–Eldan (2022) gave spectral-gap criteria from the interaction matrix spectrum, e.g. $\|J\|_{\mathrm{op}}<1$ suffices for general (not necessarily ferromagnetic) Ising models.

## 4. Partial Results / Verified Cases

- **$\mathbb{Z}^2$, $\beta<\beta_c$, free/periodic boundary:** $t_{\mathrm{mix}}=\Theta(n\log n)$ with cutoff and $O(1)$ window (Martinelli–Olivieri; Lubetzky–Sly).
- **$\mathbb{Z}^d$, $d\ge3$, $\beta$ small or SSM assumed:** same conclusion; the full interval $\beta<\beta_c(d)$ is *not* covered.
- **Bounded-degree graphs, $\tanh\beta<1/(\Delta-1)$:** $t_{\mathrm{mix}}=O(n\log n)$, optimal (Chen–Liu–Vigoda 2021); Mossel–Sly (2013) had earlier obtained this for the tree-uniqueness threshold on general graphs with a weaker constant, and matching $e^{\Omega(n)}$ slow mixing on random $\Delta$-regular graphs above the threshold.
- **Curie–Weiss ($J_{uv}=\beta/n$):** $\beta<1$: cutoff at $\frac{n\log n}{2(1-\beta)}$, window $n$; $\beta=1$: $t_{\mathrm{mix}}\asymp n^{3/2}$; $\beta>1$: $t_{\mathrm{mix}}=e^{\Theta(n)}$ (magnetization-restricted chain is $\Theta(n\log n)$).
- **$\mathbb{Z}^2$ at $\beta=\beta_c$:** $t_{\mathrm{mix}}\le L^{c}$ for a universal constant $c$ (Lubetzky–Sly 2012); extended to critical FK/Potts with $q\le4$ by Gheissari–Lubetzky (2018).
- **$\mathbb{Z}^2$, $\beta>\beta_c$, plus boundary:** $t_{\mathrm{mix}} \le L^{O(\log L)}$ (quasi-polynomial) up to criticality, Lubetzky–Martinelli–Sly–Toninelli (2013); genuinely polynomial only for $\beta$ large.
- **$\mathbb{Z}^d$, $\beta>\beta_c$, free boundary:** $t_{\mathrm{mix}} = \exp\big(\Theta(L^{d-1})\big)$ — surface-order bottleneck, matching upper bound from Thomas' cluster-expansion argument.
- **Trees and general $\|J\|_{\mathrm{op}}<1$:** $O(n\log n)$ / spectral gap $\Omega(1)$, by localization schemes.
- **Any graph, any $\beta$, sampling (not Glauber):** Jerrum–Sinclair (1993) give an FPRAS for the ferromagnetic partition function via the even-subgraphs chain, so hardness of *sampling* is not the obstruction; slow Glauber mixing is dynamical.

## 5. Principal Obstacles

- **WSM ⇏ SSM for $d\ge3$.** The $d=2$ implication uses planar duality and the fact that a subcritical percolation-type argument controls arbitrary domain shapes. In $d\ge 3$, exponential decay of truncated correlations in $\mathbb{Z}^d$ for $\beta<\beta_c$ is known, but SSM uniform over *all* subregions and boundary conditions is not — irregular domains (slabs, thin tubes, fractal boundaries) can host boundary-driven long-range order that the full-space estimate does not exclude. Every functional-inequality route runs through SSM, so the gap is structural, not technical.
- **No renormalization-group control at criticality.** The conjectured exponent $z$ is a dynamical scaling exponent; there is no rigorous dynamical scaling limit for Ising Glauber in any $d\ge2$. Even with the full static CFT/SLE picture in $d=2$, the time parametrization is not controlled: existence of the limit $\lim_L \log t_{\mathrm{mix}}/\log L$ is unproven.
- **Spectral independence saturates at the uniqueness threshold.** The influence-matrix bound $\lambda_{\max}(\Psi)=O(1)$ degenerates exactly at $\tanh\beta=1/(\Delta-1)$; it is intrinsically a worst-case (tree-recursion) bound and cannot exploit lattice geometry, so it says nothing about $\mathbb{Z}^d$ for $1/(2d-1)<\tanh\beta<\tanh\beta_c(d)$.
- **Metastability blocks coupling.** Below $\beta_c$ path coupling contracts; above it, the two phases make any one-step contraction fail, and canonical-path/conductance arguments only yield the exponential lower bound, not the sharp polynomial *upper* bound with plus boundary, where the mechanism is monotone shrinkage of a droplet — a moving-interface estimate with no general theory.

## 6. The Gap

Three explicit boundaries.

1. **The $[\,\beta_{\mathrm{SI}},\beta_c\,)$ window in $d\ge3$**, where $\tanh\beta_{\mathrm{SI}}=1/(2d-1)$. Closing it requires either SSM in arbitrary $\mathbb{Z}^d$ subregions for all $\beta<\beta_c$, or a lattice-aware strengthening of entropy factorization. Proven: $\beta<\beta_{\mathrm{SI}}$. Claimed: $\beta<\beta_c$.
2. **From "$t_{\mathrm{mix}}\le L^c$ for some $c$" to "$t_{\mathrm{mix}}=L^{z+o(1)}$"** at $\beta_c$ in $d=2$: no lower bound better than $L^{2}$ (times logarithms) is proven, and no upper bound with an identified exponent. Even $c$ in Lubetzky–Sly is not extracted.
3. **From quasi-polynomial $L^{O(\log L)}$ to polynomial $L^{O(1)}$** for the plus-boundary low-temperature $2$D model, at all $\beta>\beta_c$.

## 7. Current Research (as of June 2026)

- **High-dimensional expander / localization program** (Anari, Liu, Oveis Gharan; Chen, Liu, Vigoda; Chen–Eldan; Koehler): pushing spectral independence and stochastic localization to non-product and continuous settings, and to $O(n\log n)$ under weaker-than-uniqueness conditions. *(frontier — verify)* Efforts to certify spectral independence directly from lattice correlation decay rather than tree recursions.
- **Critical dynamics** (Gheissari, Lubetzky, and collaborators): mixing of critical FK-Ising and Swendsen–Wang; extending polynomial bounds to arbitrary boundary conditions and to the $3$D critical point.
- **Information percolation** (Lubetzky–Sly and successors): cutoff for Ising with random external fields, on random graphs, and in the presence of disorder.
- **Random-graph Ising:** critical mixing on Erdős–Rényi and random regular graphs near the Bethe threshold; interplay with the replica-symmetric/reconstruction picture.
- **Institutions:** Courant (NYU), UC Berkeley/Simons, Weizmann, Georgia Tech, Bocconi/Roma Tre (Martinelli school), Cambridge/IHES.

## 8. Future Work

- Prove SSM in arbitrary $\mathbb{Z}^d$ subregions for $\beta<\beta_c(d)$, $d\ge3$ — probably via a sharp-threshold/randomized-algorithm argument in the spirit of Duminil-Copin–Raoufi–Tassion.
- Establish existence of the dynamical exponent $z(2)$ even without identifying its value; a subadditivity or scaling-limit argument for the spectral gap of critical Glauber.
- Construct a lattice version of spectral independence whose threshold coincides with $\beta_c$ rather than the tree threshold.
- Sharpen droplet-shrinkage estimates to convert $L^{O(\log L)}$ into $L^{O(1)}$ for the plus phase.
- Extend cutoff universality: does every bounded-degree family in the uniqueness phase have cutoff, with window $O(n)$?

## 9. Key References

- **[Foundational]** R. J. Glauber. *Time-Dependent Statistics of the Ising Model.* Journal of Mathematical Physics 4 (1963), 294–307.
- **[Foundational]** F. Martinelli, E. Olivieri. *Approach to Equilibrium of Glauber Dynamics in the One Phase Region I & II.* Communications in Mathematical Physics 161 (1994), 447–486 and 487–514.
- **[Survey]** F. Martinelli. *Lectures on Glauber Dynamics for Discrete Spin Models.* Lectures on Probability Theory and Statistics (Saint-Flour 1997), Lecture Notes in Mathematics 1717, Springer, 1999.
- **[Survey]** D. A. Levin, Y. Peres, E. L. Wilmer. *Markov Chains and Mixing Times*, 2nd edition. American Mathematical Society, 2017.
- **[SOTA]** E. Lubetzky, A. Sly. *Cutoff for the Ising model on the lattice.* Inventiones Mathematicae 191 (2013), 719–755.
- **[SOTA]** E. Lubetzky, A. Sly. *Information percolation and cutoff for the stochastic Ising model.* Journal of the AMS 29 (2016), 729–774.
- **[SOTA]** E. Lubetzky, A. Sly. *Critical Ising on the square lattice mixes in polynomial time.* Communications in Mathematical Physics 313 (2012), 815–836.
- **[SOTA]** E. Mossel, A. Sly. *Exact thresholds for Ising–Gibbs samplers on general graphs.* Annals of Probability 41 (2013), 294–328.
- **[SOTA / Recent]** Z. Chen, K. Liu, E. Vigoda. *Optimal mixing of Glauber dynamics: entropy factorization via high-dimensional expansion.* STOC 2021, 1537–1550.
- **[SOTA / Recent]** N. Anari, K. Liu, S. Oveis Gharan. *Spectral independence in high-dimensional expanders and applications to the hardcore model.* FOCS 2020.
- **[SOTA / Recent]** R. Eldan, F. Koehler, O. Zeitouni. *A spectral condition for spectral gap: fast mixing in high-temperature Ising models.* Probability Theory and Related Fields 182 (2022), 1035–1051.
- **[SOTA / Recent]** Y. Chen, R. Eldan. *Localization schemes: A framework for proving mixing bounds for Markov chains.* FOCS 2022.
- **[Foundational]** D. A. Levin, M. J. Łuczak, Y. Peres. *Glauber dynamics for the mean-field Ising model: cut-off, critical power law, and metastability.* Probability Theory and Related Fields 146 (2010), 223–265.
- **[Foundational]** J. Ding, E. Lubetzky, Y. Peres. *The mixing time evolution of Glauber dynamics for the mean-field Ising model.* Communications in Mathematical Physics 289 (2009), 725–764.
- **[SOTA]** E. Lubetzky, F. Martinelli, A. Sly, F. L. Toninelli. *Quasi-polynomial mixing of the 2D stochastic Ising model with "plus" boundary up to criticality.* Journal of the European Mathematical Society 15 (2013), 339–386.
- **[SOTA]** R. Gheissari, E. Lubetzky. *Mixing times of critical two-dimensional Potts models.* Communications on Pure and Applied Mathematics 71 (2018), 994–1046.
- **[Foundational]** M. Jerrum, A. Sinclair. *Polynomial-time approximation algorithms for the Ising model.* SIAM Journal on Computing 22 (1993), 1087–1116.
- **[Computational]** M. P. Nightingale, H. W. J. Blöte. *Monte Carlo computation of correlation times of independent relaxation modes at criticality.* Physical Review B 62 (2000), 1089–1101.

## 10. Worked Example / Concrete Special Case

**Two sites, one edge.** Take $V=\{1,2\}$, $E=\{\{1,2\}\}$, $h=0$, so $\pi(\sigma)\propto e^{\beta\sigma_1\sigma_2}$. Write $\theta=\tanh\beta$. Then
$$\pi(++)=\pi(--)=\frac{e^\beta}{2e^\beta+2e^{-\beta}},\qquad \pi(+-)=\pi(-+)=\frac{e^{-\beta}}{2e^\beta+2e^{-\beta}},$$
and $\mathbb{E}_\pi[\sigma_1\sigma_2]=\theta$.

Use discrete-time Glauber: pick a site uniformly and resample. The functions $\{1,\sigma_1,\sigma_2,\sigma_1\sigma_2\}$ span $L^2(\pi)$. Compute the action of the transition operator $P$:
$$P\sigma_1 = \tfrac12\,\mathbb{E}[\sigma_1'\mid\sigma_2] + \tfrac12\,\sigma_1 = \tfrac12(\sigma_1+\theta\sigma_2),$$
and symmetrically $P\sigma_2 = \tfrac12(\sigma_2+\theta\sigma_1)$. On $\mathrm{span}\{\sigma_1,\sigma_2\}$, $P$ is $\tfrac12\begin{pmatrix}1&\theta\\ \theta&1\end{pmatrix}$, with eigenvalues $\tfrac{1+\theta}{2}$ (eigenvector $\sigma_1+\sigma_2$) and $\tfrac{1-\theta}{2}$ (eigenvector $\sigma_1-\sigma_2$). For the product,
$$P(\sigma_1\sigma_2)=\tfrac12\,\theta\sigma_2\cdot\sigma_2+\tfrac12\,\sigma_1\cdot\theta\sigma_1=\theta,$$
so $g=\sigma_1\sigma_2-\theta$ satisfies $Pg=0$. The spectrum is $\{1,\tfrac{1+\theta}{2},\tfrac{1-\theta}{2},0\}$ and
$$\mathrm{gap}=1-\frac{1+\tanh\beta}{2}=\frac{1-\tanh\beta}{2},\qquad t_{\mathrm{rel}}=\frac{2}{1-\tanh\beta}\;\sim\;e^{2\beta}\ \ (\beta\to\infty).$$

**What this exhibits.** The slow mode is the *even* (magnetization) direction $\sigma_1+\sigma_2$; the odd direction relaxes faster. As $\beta$ grows, $t_{\mathrm{rel}}$ blows up like $e^{2\beta}$ — the two-site version of the metastability that becomes $e^{\Theta(L^{d-1})}$ on $\Lambda_L\subset\mathbb{Z}^d$ with free boundary: there the bottleneck is a domain wall of surface area $L^{d-1}$, whose Gibbs cost is $e^{-2\beta L^{d-1}}$, and the conductance bound gives $t_{\mathrm{mix}}\ge e^{c\beta L^{d-1}}$.

**Contrast at criticality.** On the complete graph with $J_{uv}=\beta/n$, the same magnetization mode is the slow one, but the drift $\mathbb{E}[\Delta m]\approx \frac{1}{n}(\tanh(\beta m)-m)$ vanishes to first order at $\beta=1$; the residual cubic drift $-\beta^3m^3/3$ against diffusivity $n^{-2}$ yields $t_{\mathrm{mix}}\asymp n^{3/2}$ rather than $n\log n$. Conjecture (C2) asks for the lattice analogue of exactly this exponent computation — and there, unlike the mean-field case, no one knows how to do it.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*