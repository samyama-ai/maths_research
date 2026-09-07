---
id: 09-probability/hypercube-random-walk-mixing-random-conductances
title: "Mixing Time of Random Walks on Randomly Weighted Hypercubes"
topic: 09-probability
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Mixing Time of Random Walks on Randomly Weighted Hypercubes

> **Topic:** Probability & Stochastic Processes · **ID:** `09-probability/hypercube-random-walk-mixing-random-conductances` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Put i.i.d. positive random weights (conductances) on the edges of the $n$-dimensional hypercube and run the associated reversible random walk. Question: does the walk still exhibit the sharp **cutoff** known for the unweighted hypercube, and at what time?

Let $E_n$ be the edge set of $\mathcal{Q}_n=\{0,1\}^n$, $|E_n| = n2^{n-1}$, and let $(c_e)_{e \in E_n}$ be i.i.d. from a law $\mu$ on $(0,\infty)$. Consider the variable-speed random walk (VSRW) $X_t$ which crosses edge $e$ at rate $c_e$.

**Conjecture (annealed cutoff).** If $\mathbb{E}_\mu[c] < \infty$ and $\mu(\{0\})=0$, then for $\mu$-a.e. environment the VSRW started at $\mathbf{0}$ has a total-variation cutoff at time
$$t_n = \frac{1}{4\,\mathbb{E}_\mu[c]}\,\log n,$$
with window $O(1)$: for every $\varepsilon>0$,
$$\lim_{n\to\infty}\ \big\|\,\mathbb{P}_{\mathbf 0}(X_{(1+\varepsilon)t_n}\in\cdot)-U_n\,\big\|_{\mathrm{TV}} = 0,
\qquad
\lim_{n\to\infty}\ \big\|\,\mathbb{P}_{\mathbf 0}(X_{(1-\varepsilon)t_n}\in\cdot)-U_n\,\big\|_{\mathrm{TV}} = 1,$$
where $U_n$ is uniform on $\mathcal{Q}_n$. Equivalently, the discrete-time constant-speed walk with $P(x,y)=c_{xy}/\pi(x)$ has cutoff at $\frac{n}{4}\log n$ steps, **independent of $\mu$** after normalising $\mathbb{E}_\mu[c]=1$.

A complete solution must (i) prove or disprove universality of the constant, (ii) determine the correct statement when $\mathbb{E}_\mu[c]=\infty$ or $\mu$ has an atom / heavy accumulation at $0$, and (iii) explain the discrepancy with the relaxation time, which is *not* universal (Section 10).

## 2. Mathematical Foundations

**Weighted graph and Dirichlet form.** For $x\sim y$ in $\mathcal{Q}_n$ write $c_{xy}=c_{yx}>0$ and $\pi(x)=\sum_{y\sim x}c_{xy}=\sum_{i=1}^n c_{x,\,x\oplus e_i}$. Two canonical walks:

- **CSRW (constant speed / discrete time):** $P(x,y)=c_{xy}/\pi(x)$, reversible w.r.t. $\pi$.
- **VSRW:** generator $\mathcal{L}f(x)=\sum_{y\sim x}c_{xy}\big(f(y)-f(x)\big)$, reversible w.r.t. **counting measure**, so its stationary law is exactly $U_n$.

The Dirichlet form is
$$\mathcal{E}(f,f)=\tfrac12\sum_{x\sim y}c_{xy}\big(f(x)-f(y)\big)^2,\qquad
\mathrm{gap} = \inf\Big\{\tfrac{\mathcal{E}(f,f)}{\mathrm{Var}_\nu(f)} : \mathrm{Var}_\nu(f)>0\Big\},$$
with $\nu$ the relevant stationary measure. Mixing time: $t_{\mathrm{mix}}(\varepsilon)=\inf\{t: \max_x\|\mathbb{P}_x(X_t\in\cdot)-\nu\|_{\mathrm{TV}}\le\varepsilon\}$, and **cutoff** means $t_{\mathrm{mix}}(\varepsilon)/t_{\mathrm{mix}}(1-\varepsilon)\to1$ for all $\varepsilon$.

**Unweighted benchmark.** For $c\equiv1$, Fourier analysis on $\mathbb{Z}_2^n$ diagonalises $\mathcal{L}$: the Walsh characters $\chi_S(x)=(-1)^{\sum_{i\in S}x_i}$, $S\subseteq[n]$, are eigenfunctions with eigenvalues $-2|S|$. Hence
$$\|\mathbb{P}_{\mathbf 0}(X_t\in\cdot)-U_n\|^2_{\mathrm{TV}}\le \tfrac14\sum_{k=1}^n\binom{n}{k}e^{-4kt}=\tfrac14\big[(1+e^{-4t})^n-1\big],$$
giving cutoff at $\frac14\log n$ (continuous time, all coordinates ringing at rate $1$), equivalently $\frac14 n\log n$ for the lazy one-coordinate-per-step walk (Diaconis–Graham–Morrison 1990; Aldous 1983).

**Comparison (Diaconis–Saloff-Coste 1993).** If $0<a\le c_e\le b<\infty$ a.s. (uniform ellipticity), then for all $f$, $a\,\mathcal{E}_1(f,f)\le \mathcal{E}_c(f,f)\le b\,\mathcal{E}_1(f,f)$, so
$$\frac{a}{b}\cdot\frac{1}{C} \le \frac{\mathrm{gap}_c}{\mathrm{gap}_1}\le \frac{b}{a}\cdot C .$$
This yields order but never constants, hence never cutoff.

**Degeneracy scale.** If $\mu([0,\varepsilon])\asymp \varepsilon^{\gamma}$ as $\varepsilon\downarrow0$, then among $n2^{n-1}$ edges the minimum conductance is $c_{\min}\asymp (n2^n)^{-1/\gamma}$ — exponentially small — while a vertex all of whose $n$ edges are weak requires $\varepsilon \gtrsim 2^{-1/\gamma}$, i.e. traps of only $O(1)$ depth. This asymmetry is the crux: local defects destroy the spectral gap but not, conjecturally, TV mixing.

## 3. History & State of the Art (SOTA)

- **1983–1990.** Aldous (*Random walks on finite groups and rapidly mixing Markov chains*, 1983) and Diaconis–Graham–Morrison (1990) establish cutoff at $\frac14 n\log n$ on the unweighted hypercube, one of the founding examples of the cutoff phenomenon.
- **1993–1997.** Diaconis–Saloff-Coste comparison and Nash-inequality machinery give $\Theta(n\log n)$ for any uniformly elliptic weighting; Saloff-Coste's Saint-Flour lectures (1997) codify the toolkit.
- **1982–2017 (percolation degeneration).** Taking $\mu=\mathrm{Bernoulli}(p)$ makes the weighted hypercube a percolation cluster. Ajtai–Komlós–Szemerédi (1982) and Bollobás–Kohayakawa–Łuczak (1992) locate the phase transition at $p_c=1/(n-1)$; van der Hofstad–Nachmias (*Hypercube percolation*, JEMS 2017) give the critical scaling window and giant-component geometry, prerequisites for any mixing statement in that regime.
- **2005–2011 (random conductance model).** On $\mathbb{Z}^d$, Fontes–Mathieu (2006) and Berger–Biskup–Hoffman–Kozma (2008) show anomalous heat-kernel decay for bounded conductances with heavy accumulation at $0$; Biskup's *Probability Surveys* (2011) article is the standard reference. These results show the environment can change the diffusive picture qualitatively even when $c\le 1$.
- **2013.** Ding–Peres, *Sensitivity of mixing times*: there exist bounded-degree graphs where a bounded (factor-2) perturbation of edge weights changes the mixing time by a $\log$ factor. This is the formal reason "uniform ellipticity $\Rightarrow$ same constant" is false in general and must be a hypercube-specific phenomenon if true.
- **2017–2022 (cutoff on random geometries).** Berestycki–Lubetzky–Peres–Sly (*Random walks on the random graph*, Ann. Probab. 2018), Ben-Hamou–Salez (2017), and Hermon–Sly–Sousi (2022) prove cutoff for walks on random sparse graphs by entropy/local-weak-limit methods. These are the templates currently being transplanted to the weighted hypercube.

**SOTA summary:** order $\Theta(n\log n)$ is known under uniform ellipticity; the *constant* and hence cutoff is proven only in structured sub-classes (Section 4).

## 4. Partial Results / Verified Cases

1. **Direction-dependent weights (fully solved).** If $c_{x,x\oplus e_i}=a_i$ depends only on the coordinate $i$, the chain is a product of $n$ two-state chains and
$$4\|\mathbb{P}_{\mathbf 0}(X_t\in\cdot)-U_n\|_{\mathrm{TV}}^2\ \le\ \prod_{i=1}^n\big(1+e^{-4a_i t}\big)-1 .$$
Cutoff holds iff $\sum_i e^{-4a_i t}$ transitions sharply; for $a_i$ i.i.d. with $\mathbb{E}[a]<\infty$ and $\mathbb{P}(a\le\varepsilon)\asymp\varepsilon^\gamma$ the cutoff time is $\frac{1}{4}\max_i a_i^{-1}\log(\cdot)$-driven and is **not** $\frac{1}{4\mathbb{E}[a]}\log n$ — the slowest coordinate dominates. This shows the conjecture genuinely requires the i.i.d.-per-edge (non-product) structure.
2. **Uniform ellipticity, $a\le c\le b$.** $t_{\mathrm{mix}} = \Theta(n\log n)$ for the CSRW, with explicit constants $\frac{a}{4b}n\log n \le t_{\mathrm{mix}} \le C\frac{b}{a}n\log n$ (Diaconis–Saloff-Coste comparison plus the exact spectrum of $\mathcal{Q}_n$). Cutoff open even here.
3. **Small perturbations.** If $c_e = 1+\xi_e$ with $\|\xi\|_\infty \le \delta_n \to 0$, first-order perturbation of the Walsh spectrum gives cutoff at $\frac14 n\log n$ whenever $\delta_n \sqrt{n}\to 0$ *(the regime where eigenvalue clusters do not merge)*.
4. **Stationary measure is asymptotically uniform.** For $\mathbb{E}[c^2]<\infty$, $\pi(x)=\sum_{i}c_{x,x\oplus e_i}$ has relative fluctuation $O(n^{-1/2})$, so $\|\pi - U_n\|_{\mathrm{TV}}\to0$: CSRW and VSRW targets agree asymptotically. Fails when $\mu$ is in the domain of attraction of an $\alpha$-stable law, $\alpha<2$.
5. **Percolation case $\mu=\mathrm{Ber}(p)$, $p = \lambda/n$, $\lambda>1$.** The giant component's diameter and expansion are controlled (van der Hofstad–Nachmias 2017); mixing on it is polynomial in $n$ but the exact exponent and any cutoff remain open.
6. **Relaxation time (negative result).** For $\mu$ with $\mu([0,\varepsilon])\asymp\varepsilon^\gamma$, $t_{\mathrm{rel}} \ge c\,(n2^n)^{1/\gamma}/n$ for the VSRW via a test function supported on the endpoints of the weakest edge — exponentially larger than $t_{\mathrm{mix}}$. So *any* proof must avoid spectral-gap bounds.

## 5. Principal Obstacles

- **Fourier analysis breaks.** The Walsh basis diagonalises the operator only when $c$ is translation-invariant. A generic i.i.d. environment destroys the $\mathbb{Z}_2^n$ symmetry; the generator has no known basis, and the eigenvalue multiplicities $\binom{n}{k}$ split into $\binom nk$ distinct, uncontrolled values.
- **Spectral profile is the wrong tool.** By item 6 above, $t_{\mathrm{rel}}$ can be exponential while $t_{\mathrm{mix}}$ is $\Theta(\log n)$ (VSRW). Every $L^2$ method — Nash inequalities, log-Sobolev, spectral profile, evolving sets (Morris–Peres 2005) — is bounded below by $t_{\mathrm{rel}}$ and therefore cannot see the conjectured answer.
- **Comparison loses constants.** Diaconis–Saloff-Coste bounds are tight only up to $b/a$; Ding–Peres (2013) prove such loss is unavoidable on general graphs, so the required improvement must exploit the hypercube's expansion, not generic reversibility.
- **No local weak limit with the right topology.** The success stories on random regular graphs use convergence to a weighted tree plus entropy concentration. The hypercube's local limit is $\mathbb{Z}^\infty$ with i.i.d. weights, an infinite-dimensional object for which no entropy/speed theory exists.
- **Environment dependence of the walk's own path.** The walk's crossing rate at $x$ in direction $i$ is $c_{x,x\oplus e_i}$, a weight it *re-samples* as it moves, but with correlations along self-intersecting paths. Decoupling these correlations (the analogue of "the walk sees fresh randomness") is unproven beyond $O(\log n)$ time only heuristically.

## 6. The Gap

Proven: order $n\log n$ under ellipticity (4.2), exact answers for degenerate/product weightings (4.1), $\pi\approx U_n$ (4.4).

Missing: a **non-$L^2$ upper bound** matching the coupon-collector lower bound to first order. Concretely, one needs to show that for the VSRW the number of coordinates never flipped by time $t$ concentrates at $n\,\mathbb{E}[e^{-2ct}]$-type expressions and that the *residual* randomness of the environment along the trajectory contributes only $o(\log n)$. The single crossing point: proving
$$\mathbb{E}_{\mathrm{env}}\Big[\big\|\mathbb{P}_{\mathbf 0}(X_{(1+\varepsilon)t_n}\in\cdot)-U_n\big\|_{\mathrm{TV}}\Big]\to0
\quad\text{with } t_n = \tfrac{1}{4\mathbb{E}[c]}\log n,$$
i.e. that rare weak edges (which do kill the spectral gap) are avoided by the walk with probability $1-o(1)$, so they affect $t_{\mathrm{mix}}$ only through a null set of starting points. No current technique separates "bad for the spectrum" from "invisible to typical trajectories" on the hypercube.

## 7. Current Research (as of June 2026)

- **Entropy / non-backtracking transplants.** Groups following Berestycki–Lubetzky–Peres–Sly and Ben-Hamou–Salez are adapting entropic concentration to high-dimensional product graphs; the obstruction is the absence of a tree-like local limit. *(frontier — verify)*
- **Random conductance homogenisation in growing dimension.** Extending Biskup-style quenched invariance principles from $\mathbb{Z}^d$ (fixed $d$) to $d=n\to\infty$, where the relevant scaling is $\log n$ rather than diffusive. Israeli and Cambridge probability groups are active here. *(frontier — verify)*
- **Percolation regime.** Following van der Hofstad–Nachmias, the mixing time of the walk on the supercritical hypercube giant component at $p=(1+\varepsilon)/n$ is being attacked with the "anatomy of the giant" decomposition (2-core plus decorations). *(frontier — verify)*
- **Trap models / spin glasses.** When $\mu$ has an exponential heavy tail, the model becomes Random Energy Model dynamics; Ben Arous–Bovier–Gayrard's ageing analysis (2003) gives the expected non-cutoff, subaging picture, and delimits where the conjecture must fail.
- **Numerics.** Direct diagonalisation is feasible only to $n\approx 24$ ($2^{24}$ states via Lanczos); TV simulation via coupling supports the universal constant for lognormal and Gamma conductances up to $n\approx 40$. *(frontier — verify)*

## 8. Future Work

1. **Prove cutoff for two-valued conductances** $c\in\{a,b\}$, each with probability $1/2$ — the minimal non-product case; even here the constant is unproven.
2. **Develop a hypercube-adapted "escape" estimate:** show the walk crosses an edge of conductance below $\delta$ at most $o(\log n)$ times before $t_n$, giving an effective uniformly elliptic environment on the trajectory.
3. **Quantify the gap/mixing divergence:** characterise exactly which $\mu$ give $t_{\mathrm{rel}}\gg t_{\mathrm{mix}}$, in the spirit of Hermon–Peres's hitting-time characterisation of $L^2$ mixing.
4. **Classify degenerate laws:** determine the phase boundary in $\gamma$ (accumulation at $0$) and in the tail index at $\infty$ separating cutoff, no-cutoff-but-$\Theta(n\log n)$, and trap-dominated ageing.
5. **Bernoulli interpolation:** connect $\mu=\mathrm{Ber}(p)$ with $p$ from $\Theta(1/n)$ to $\Theta(1)$ and track how cutoff appears.

## 9. Key References

- **[Foundational]** D. Aldous. *Random walks on finite groups and rapidly mixing Markov chains.* Séminaire de Probabilités XVII, Lecture Notes in Math. 986, Springer, 1983.
- **[Foundational]** P. Diaconis, R. L. Graham, J. A. Morrison. *Asymptotic analysis of a random walk on a hypercube with many dimensions.* Random Structures & Algorithms 1(1), 51–72, 1990.
- **[Foundational]** P. Diaconis, L. Saloff-Coste. *Comparison theorems for reversible Markov chains.* Annals of Applied Probability 3(3), 696–730, 1993.
- **[Survey]** D. A. Levin, Y. Peres. *Markov Chains and Mixing Times*, 2nd edition. American Mathematical Society, 2017.
- **[Survey]** M. Biskup. *Recent progress on the random conductance model.* Probability Surveys 8, 294–373, 2011.
- **[Survey]** L. Saloff-Coste. *Lectures on finite Markov chains.* Lectures on Probability Theory and Statistics (Saint-Flour 1996), Lecture Notes in Math. 1665, Springer, 1997.
- **[SOTA / Recent]** N. Berestycki, E. Lubetzky, Y. Peres, A. Sly. *Random walks on the random graph.* Annals of Probability 46(1), 456–490, 2018.
- **[SOTA / Recent]** A. Ben-Hamou, J. Salez. *Cutoff for nonbacktracking random walks on sparse random graphs.* Annals of Probability 45(3), 1752–1770, 2017.
- **[SOTA / Recent]** J. Hermon, A. Sly, P. Sousi. *Universality of cutoff for graphs with an added random matching.* Annals of Probability 50(1), 203–240, 2022.
- **[SOTA / Recent]** R. van der Hofstad, A. Nachmias. *Hypercube percolation.* Journal of the European Mathematical Society 19(3), 725–814, 2017.
- **[Technical]** N. Berger, M. Biskup, C. E. Hoffman, G. Kozma. *Anomalous heat-kernel decay for random walk among bounded random conductances.* Annales de l'IHP Probabilités et Statistiques 44(2), 374–392, 2008.
- **[Technical]** L. R. G. Fontes, P. Mathieu. *On symmetric random walks with random conductances on $\mathbb{Z}^d$.* Probability Theory and Related Fields 134(4), 565–602, 2006.
- **[Technical]** J. Ding, Y. Peres. *Sensitivity of mixing times.* Electronic Communications in Probability 18, no. 88, 2013.
- **[Technical]** B. Morris, Y. Peres. *Evolving sets, mixing and heat kernel bounds.* Probability Theory and Related Fields 133(2), 245–266, 2005.
- **[Technical]** G. Ben Arous, A. Bovier, V. Gayrard. *Glauber dynamics of the random energy model I: Metastable motion on the extreme states.* Communications in Mathematical Physics 235, 379–425, 2003.
- **[Historical]** M. Ajtai, J. Komlós, E. Szemerédi. *Largest random component of a $k$-cube.* Combinatorica 2(1), 1–7, 1982.

## 10. Worked Example / Concrete Special Case

**$n=2$: the weighted 4-cycle.** Vertices $00,01,11,10$; set conductances alternating $a,b,a,b$:
$$c_{00,01}=a,\quad c_{01,11}=b,\quad c_{11,10}=a,\quad c_{10,00}=b .$$
Every vertex has $\pi(x)=a+b$. Test the two Walsh characters on the VSRW generator $\mathcal{L}f(x)=\sum_{y\sim x}c_{xy}(f(y)-f(x))$.

Take $\chi_1(x)=(-1)^{x_1}$, i.e. $\chi_1 = (1,1,-1,-1)$ on $(00,01,11,10)$. Then
$$\mathcal{L}\chi_1(00)=a(\chi_1(01)-\chi_1(00))+b(\chi_1(10)-\chi_1(00)) = a\cdot 0 + b\cdot(-2)=-2b = -2b\,\chi_1(00),$$
$$\mathcal{L}\chi_1(11)=b(\chi_1(01)-\chi_1(11))+a(\chi_1(10)-\chi_1(11)) = 2b + 0 = -2b\,\chi_1(11).$$
So $\chi_1$ survives as an eigenfunction with eigenvalue $-2b$; symmetrically $\chi_2=(-1)^{x_2}$ has eigenvalue $-2a$, and $\chi_1\chi_2$ has eigenvalue $-2(a+b)$. Spectrum: $\{0,-2a,-2b,-2(a+b)\}$.

**Consequences.**
- $\mathrm{gap} = 2\min(a,b)$, so $t_{\mathrm{rel}} = \dfrac{1}{2\min(a,b)}$ — governed by the **minimum**, not the mean.
- TV distance from $\mathbf 0=00$: with $\bar c = (a+b)/2$,
$$4\|\mathbb{P}_{00}(X_t\in\cdot)-U_2\|^2_{\mathrm{TV}} \le e^{-4at}+e^{-4bt}+e^{-4(a+b)t}.$$
For $a=1,b=10^{-3}$: $t_{\mathrm{rel}}=500$, but the sum drops below $10^{-2}$ only once $e^{-4bt}\le 10^{-2}$, i.e. $t\ge 1151 \approx 2.3\,t_{\mathrm{rel}}$. Here mixing *is* slaved to the weak edge, because with $n=2$ each coordinate has only one conductance value.

**Why the conjecture is nontrivial.** In the true i.i.d.-per-edge model with $n$ large, coordinate $i$ is crossed at rate $c_{x,x\oplus e_i}$ which is *resampled at every vertex $x$* the walk visits. A vertex sitting next to a weak edge has $n-1$ other edges of typical conductance; the walk leaves in time $\asymp 1/(n\bar c)$ and never needs that edge. The alternating-cycle computation above is exactly the *product* case (4.1), where a weak direction is globally weak and cannot be routed around — and there the answer depends on $\min_i a_i$, not $\mathbb{E}[c]$. The conjecture asserts that as soon as weights vary edge-by-edge, the $n$ available detours homogenise the rate to $\mathbb{E}[c]$ and restore the universal constant $\frac14\log n$. Proving that the walk *routes around* the exponentially weak edges — while the spectrum does not — is precisely the open step of Section 6.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*