---
id: 09-probability/extinction-time-of-the-contact-process-on-finite-graphs
title: "Extinction Time of the Contact Process on Finite Graphs"
topic: 09-probability
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Extinction Time of the Contact Process on Finite Graphs

> **Topic:** Probability & Stochastic Processes · **ID:** `09-probability/extinction-time-of-the-contact-process-on-finite-graphs` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

On any finite graph the contact process (SIS epidemic) dies out almost surely: the empty configuration is the unique absorbing state of an irreducible finite-state Markov chain. The mathematical content is entirely in the **rate** of extinction.

Let $G_n = (V_n, E_n)$ be a sequence of finite connected graphs with $|V_n| = n$, and let $\tau_n$ be the extinction time of the contact process with infection rate $\lambda > 0$ started from all sites infected. The problem is to determine the growth of $\tau_n$ as a function of $\lambda$ and the geometry of $G_n$, and specifically:

1. **Dichotomy.** For which $(\lambda, G_n)$ is $\log \mathbb{E}[\tau_n] = \Theta(n)$ (metastable/supercritical regime) versus $\mathbb{E}[\tau_n] = O(\log n)$ (subcritical regime)? Is the intermediate behaviour always confined to a critical value $\lambda_c(G_\bullet)$?
2. **Sharp constant.** Does $\frac{1}{|V_n|}\log \mathbb{E}[\tau_n]$ converge to a finite positive limit $c(\lambda)$, and is $\lambda \mapsto c(\lambda)$ continuous / analytic on $(\lambda_c,\infty)$?
3. **Critical case.** At $\lambda = \lambda_c$, what is the exact order of $\tau_n$? The prevailing conjecture is a **polynomial law** $\tau_n = n^{\alpha + o(1)}$ with $\alpha$ expressible through the critical exponents of the infinite-volume process.
4. **Exponential law.** Under what generality does $\tau_n / \mathbb{E}[\tau_n] \Rightarrow \mathrm{Exp}(1)$?

A complete resolution means: for a stated class of graph sequences, matching upper and lower bounds on $\log \mathbb{E}[\tau_n]$ up to $1+o(1)$, plus identification of the critical-case exponent.

## 2. Mathematical Foundations

The contact process $(\xi_t)_{t\ge 0}$ on $G=(V,E)$ is the continuous-time Markov process on $\{0,1\}^V$ (equivalently on subsets $\xi_t \subseteq V$ of infected sites) with generator

$$
(\mathcal{L}f)(\xi) \;=\; \sum_{x \in V} \Big[ \mathbf{1}\{x\in\xi\}\big(f(\xi\setminus\{x\}) - f(\xi)\big) \;+\; \lambda\,\mathbf{1}\{x\notin\xi\}\,n_\xi(x)\,\big(f(\xi\cup\{x\}) - f(\xi)\big)\Big],
$$

where $n_\xi(x) = \\#\{y : \{x,y\}\in E,\ y \in \xi\}$. Recovery rate is normalised to $1$; $\lambda>0$ is the infection rate.

**Graphical construction.** Place independent Poisson processes: rate-$1$ "recovery" marks on each $\{x\}\times\mathbb{R}_+$ and rate-$\lambda$ "infection" arrows on each ordered pair $(x,y)$ with $\{x,y\}\in E$. Then $x \in \xi_t^A$ iff there is an *active path* from $A\times\{0\}$ to $(x,t)$ moving up in time, crossing arrows, avoiding recovery marks. This yields **monotonicity** (attractiveness) in $\lambda$ and in the initial set, **self-duality**
$$\mathbb{P}(\xi^A_t \cap B \neq \emptyset) = \mathbb{P}(\xi^B_t \cap A \neq \emptyset),$$
and a **subadditivity** structure used for all large-deviation arguments.

**Extinction time.** $\tau_n^A := \inf\{t\ge 0 : \xi_t^A = \emptyset\}$, with $\tau_n := \tau_n^{V_n}$.

**Infinite-volume critical values.** On $\mathbb{Z}^d$, $\lambda_c(\mathbb{Z}^d) = \sup\{\lambda: \mathbb{P}(\xi_t^{\{0\}} \neq \emptyset\ \forall t) = 0\}$; $\lambda_c(\mathbb{Z}) \approx 1.6494$ numerically. On the $d$-regular tree $\mathbb{T}_d$ there are two critical values $\lambda_1(\mathbb{T}_d) < \lambda_2(\mathbb{T}_d)$ separating extinction, global (weak) survival, and local (strong) survival (Pemantle 1992).

**Metastability.** A sequence $(G_n)$ exhibits metastability at $\lambda$ if there are $0<c\le C<\infty$ with
$$ e^{cn} \le \mathbb{E}[\tau_n] \le e^{Cn} \quad\text{for large } n, \qquad \frac{\tau_n}{\mathbb{E}[\tau_n]} \xrightarrow{d} \mathrm{Exp}(1). $$
The exponential law follows from an asymptotic loss-of-memory estimate: $\sup_{A\neq\emptyset}\big|\mathbb{P}(\tau^A_n > t + s) - \mathbb{P}(\tau^A_n>t)\mathbb{P}(\tau^{V_n}_n>s)\big| \to 0$ on the metastable time scale.

## 3. History & State of the Art (SOTA)

- **1974.** Harris introduces the contact process; the graphical representation and the basic subcritical/supercritical dichotomy on $\mathbb{Z}^d$.
- **1984–85.** Cassandro–Galves–Olivieri–Vares give the pathwise approach to metastability; Schonmann proves the exponential limit law for the contact process on finite intervals of $\mathbb{Z}$.
- **1988–89.** Durrett–Liu, Durrett–Schonmann and Durrett–Schonmann–Tanaka ("The contact process on a finite set", I–III) establish the trichotomy on $[1,n]\cap\mathbb{Z}$: $\tau_n \asymp \log n$ for $\lambda<\lambda_c$, $\log\tau_n \asymp n$ for $\lambda>\lambda_c$, and a genuinely intermediate critical behaviour at $\lambda=\lambda_c$.
- **1993, 1999.** Mountford proves metastability for boxes $[1,n]^d\subset\mathbb{Z}^d$ with $\log \mathbb{E}[\tau] \asymp n^d$, and later the **existence of the constant** $\lim n^{-d}\log\mathbb{E}[\tau_n] = c(\lambda)\in(0,\infty)$ for $\lambda>\lambda_c(\mathbb{Z}^d)$.
- **2005–2009.** Berger–Borgs–Chayes–Saberi and Chatterjee–Durrett shift attention to random graphs: on power-law configuration models with exponent $\beta > 2$, $\lambda_c = 0$ — hubs (star subgraphs) sustain the infection for every $\lambda>0$, refuting the mean-field "epidemic threshold $\propto 1/\langle d^2\rangle$" heuristic from the physics literature.
- **2013–2016.** Mountford–Valesin–Yao obtain metastable densities on power-law graphs; Mountford–Mourrat–Valesin–Yao prove the **universal lower bound**: for *every* connected $G_n$ on $n$ vertices and every $\lambda>\lambda_c(\mathbb{Z})$, $\mathbb{E}[\tau_n]\ge e^{cn}$.
- **2016–2017.** Mourrat–Valesin and Lalley–Su settle random $d$-regular graphs: $\tau_n = O(\log n)$ for $\lambda<\lambda_c(\mathbb{T}_d)$ and $\log\tau_n \asymp n$ for $\lambda>\lambda_c(\mathbb{T}_d)$, with the exponential law.
- **2021–2022.** Bhamidi–Nam–Nguyen–Sly treat general degree distributions on the configuration model; Nam–Nguyen–Sly give sharp small-$\lambda$/large-degree asymptotics for critical values on random graphs and Galton–Watson trees.

**SOTA summary:** the *dichotomy* is settled for lattices, random regular graphs, and broad configuration-model classes. The *sharp constant* is known to exist only in restricted settings; the *critical exponent* is open even for $[1,n]\cap\mathbb{Z}$.

## 4. Partial Results / Verified Cases

| Setting | Regime | Result |
|---|---|---|
| $[1,n]\cap\mathbb{Z}$ | $\lambda<\lambda_c(\mathbb{Z})$ | $\tau_n/\log n \to 1/\gamma(\lambda)$, exponential decay rate $\gamma$ (Durrett–Liu 1988) |
| $[1,n]^d\cap\mathbb{Z}^d$ | $\lambda>\lambda_c(\mathbb{Z}^d)$ | $n^{-d}\log\mathbb{E}[\tau_n]\to c(\lambda)\in(0,\infty)$; $\tau_n/\mathbb{E}\tau_n\Rightarrow\mathrm{Exp}(1)$ (Mountford 1993, 1999) |
| Arbitrary connected $G_n$, $|V_n|=n$ | $\lambda>\lambda_c(\mathbb{Z})\approx1.6494$ | $\mathbb{E}[\tau_n]\ge e^{c(\lambda)n}$, universally (MMVY 2016) |
| Random $d$-regular, $d\ge3$ | $\lambda<\lambda_1(\mathbb{T}_d)$ | $\tau_n = O(\log n)$ w.h.p. (Mourrat–Valesin 2016; Lalley–Su 2017) |
| Random $d$-regular, $d\ge3$ | $\lambda>\lambda_1(\mathbb{T}_d)$ | $\log\tau_n \asymp n$, exponential law |
| Configuration model, power law $\mathbb{P}(D=k)\sim k^{-\beta}$, $\beta>2$ | all $\lambda>0$ | $\lambda_c=0$; $\log\mathbb{E}[\tau_n]\asymp n$ (Chatterjee–Durrett 2009; MVY 2013) |
| Configuration model, $\mathbb{E}[D]=\infty$ | all $\lambda>0$ | metastability, density asymptotics (Can–Schapira 2015) |
| Star $K_{1,n}$ | $\lambda^2 n \gg 1$ | $\log\mathbb{E}[\tau_n] \ge c\lambda^2 n$ (BBCS 2005; Chatterjee–Durrett 2009) |
| General degree configuration model | $\lambda$ small | survival/extinction criterion via local weak limit (Bhamidi–Nam–Nguyen–Sly 2021) |
| $[1,n]\cap\mathbb{Z}$, $\lambda=\lambda_c$ | critical | $\tau_n$ superlinear and sub-exponential (Durrett–Schonmann–Tanaka 1989); exponent unknown |

## 5. Principal Obstacles

- **No explicit stationary measure.** The contact process is non-reversible and has no product or Gibbs stationary law. Standard metastability machinery for reversible dynamics (Dirichlet-form capacity, potential theory of Bovier–den Hollander) gives sharp prefactors for Glauber dynamics but has no analogue here; there is no energy landscape whose saddle governs the escape.
- **Constants come from subadditivity.** Lower bounds on $\log\mathbb{E}[\tau_n]$ come from block/renormalisation arguments: build a supercritical oriented percolation on coarse-grained blocks, then bound extinction by a large-deviation event for that percolation. The constant produced is an unquantified renormalisation constant, so upper and lower bounds never match.
- **Graph-dependence of the exponent.** On $\mathbb{Z}^d$ the exponent scales with volume $n^d$; on expanders with volume $n$; on power-law graphs with $n$ but driven by a sparse set of hubs. There is no single geometric functional (isoperimetry, spectral gap, degree moments) known to determine $c(\lambda)$, so results are proved graph class by graph class.
- **Criticality.** At $\lambda_c$ the process is neither dominated by a supercritical percolation nor by a subcritical branching random walk. Determining $\alpha$ requires the critical exponents of the infinite-volume contact process, which are themselves unknown rigorously in $d=1,2$ (the process is conjectured to be in the **directed percolation** universality class, with $d=1$ exponents only known numerically).
- **Hubs versus bulk.** On heavy-tailed graphs the surviving infection lives on stars connected by long paths; the metastable density is governed by an infinite-dimensional fixed-point equation whose uniqueness/regularity in $\lambda$ is not established.

## 6. The Gap

Proven: two-sided *exponential-order* bounds $e^{cn}\le \mathbb{E}[\tau_n]\le e^{Cn}$ with $c<C$ for wide graph classes, plus existence of the limiting constant on lattice boxes.

Missing:

1. **$c = C$ in general.** Show $\lim n^{-1}\log \mathbb{E}[\tau_n]$ exists for random regular graphs / configuration models. Existing proofs of existence use the near-exact translation invariance and Fekete subadditivity of $\mathbb{Z}^d$ boxes, which random graphs lack (they are only asymptotically homogeneous, and gluing two graphs is not a subadditive operation on the exponent).
2. **The critical exponent.** Prove $\tau_n = n^{\alpha+o(1)}$ at $\lambda_c$ on $[1,n]$ and identify $\alpha$ in terms of the directed-percolation exponents $(\nu_\parallel, \nu_\perp, \delta)$; the conjectured relation $\alpha = \nu_\parallel/\nu_\perp \approx 1.58$ *(frontier — verify)* is unproven in both directions.
3. **Universal upper bound.** MMVY's universal lower bound $e^{cn}$ has no companion: no geometric condition is known that is *necessary and sufficient* for $\log \mathbb{E}[\tau_n] = O(n)$ rather than $\omega(n)$ (e.g. $\log \mathbb{E}[\tau_n] \asymp n^d$ on boxes shows the exponent can exceed the vertex count only via volume-vs-diameter mismatch — a full classification is absent).

## 7. Current Research (as of June 2026)

- **Sly's group (Berkeley/Princeton) and coauthors (Nam, Nguyen, Bhamidi).** Sharp asymptotics of $\lambda_c$ for sparse random graphs and Galton–Watson trees; the small-$\lambda$ expansion $\lambda_c(\mathbb{T}_d)$ as $d\to\infty$ and its transfer to finite graphs.
- **Valesin (Groningen) with Mountford, Mourrat, Can, Schapira.** Metastable densities, contact process in random environment (random rates), and extinction times on evolving/dynamic graphs where edges refresh at rate $\kappa$ — the interplay of $\kappa$ and $\lambda$ produces a two-parameter phase diagram whose extinction-time exponent is largely open *(frontier — verify)*.
- **Contact process on preferential-attachment and inhomogeneous graphs** (Jacob, Mörters, Linker, Remenik): quantifying how a power-law tail exponent $\beta$ controls $\log \mathbb{E}[\tau_n]$ and the density of infection at hubs.
- **Critical-case analysis** via lace-expansion and mean-field results above the upper critical dimension $d_c = 4$: for $d>4$ one expects $\alpha=2$ at criticality, and partial results exist for the spread-out/long-range contact process, which is the most likely place a rigorous critical extinction exponent lands first *(frontier — verify)*.
- **Computational.** High-precision Monte Carlo and transfer-matrix estimates of $c(\lambda)$ on $[1,n]$ for $n\le 40$, and DP-exponent estimates $\nu_\parallel = 1.7338$, $\nu_\perp = 1.0968$ in $d=1$ from the statistical-physics literature.

## 8. Future Work

- Develop a **non-reversible potential theory** for attractive interacting particle systems, aiming at prefactor-sharp escape rates rather than exponential order.
- Replace Fekete subadditivity with a **local-weak-convergence** argument: show $n^{-1}\log\mathbb{E}[\tau_n]$ is continuous with respect to Benjamini–Schramm convergence of $(G_n)$ plus an expansion assumption; this would give existence of the constant for random regular graphs from the tree limit.
- Prove **finite-size scaling** at $\lambda_c$: establish that the extinction time under the scaling window $|\lambda - \lambda_c| \asymp n^{-1/\nu_\perp}$ has a nondegenerate scaling limit, which would pin $\alpha$ once critical exponents are known.
- Extend the universal lower bound of MMVY down from $\lambda_c(\mathbb{Z})$ to a graph-dependent threshold, e.g. show $\mathbb{E}[\tau_n]\ge e^{cn}$ for all $\lambda > \lambda_1(\mathbb{T}_{d})$ on any graph with max degree $d$.

## 9. Key References

- **[Foundational]** T. E. Harris. *Contact interactions on a lattice.* Annals of Probability 2(6):969–988, 1974.
- **[Foundational]** T. M. Liggett. *Stochastic Interacting Systems: Contact, Voter and Exclusion Processes.* Springer, Grundlehren 324, 1999.
- **[Foundational]** R. Durrett, X.-F. Liu. *The contact process on a finite set.* Annals of Probability 16(3):1158–1173, 1988.
- **[Foundational]** R. Durrett, R. H. Schonmann. *The contact process on a finite set II.* Annals of Probability 16(4):1570–1583, 1988.
- **[Foundational]** R. Durrett, R. H. Schonmann, N. Tanaka. *The contact process on a finite set III: The critical case.* Annals of Probability 17(4):1303–1321, 1989.
- **[Foundational]** M. Cassandro, A. Galves, E. Olivieri, M. E. Vares. *Metastable behavior of stochastic dynamics: a pathwise approach.* Journal of Statistical Physics 35:603–634, 1984.
- **[Foundational]** R. H. Schonmann. *Metastability for the contact process.* Journal of Statistical Physics 41:445–464, 1985.
- **[Foundational]** T. Mountford. *A metastable result for the finite multidimensional contact process.* Canadian Mathematical Bulletin 36(2):216–226, 1993.
- **[Foundational]** T. Mountford. *Existence of a constant for finite system extinction.* Journal of Statistical Physics 96:1331–1341, 1999.
- **[Foundational]** R. Pemantle. *The contact process on trees.* Annals of Probability 20(4):2089–2116, 1992.
- **[SOTA / Recent]** N. Berger, C. Borgs, J. T. Chayes, A. Saberi. *On the spread of viruses on the internet.* Proc. 16th ACM–SIAM Symposium on Discrete Algorithms (SODA), 301–310, 2005.
- **[SOTA / Recent]** S. Chatterjee, R. Durrett. *Contact processes on random graphs with power law degree distributions have critical value 0.* Annals of Probability 37(6):2332–2356, 2009.
- **[SOTA / Recent]** T. Mountford, D. Valesin, Q. Yao. *Metastable densities for the contact process on power law random graphs.* Electronic Journal of Probability 18, paper 103, 2013.
- **[SOTA / Recent]** T. Mountford, J.-C. Mourrat, D. Valesin, Q. Yao. *Exponential extinction time of the contact process on finite graphs.* Stochastic Processes and their Applications 126(7):1974–2013, 2016.
- **[SOTA / Recent]** J.-C. Mourrat, D. Valesin. *Phase transition of the contact process on random regular graphs.* Electronic Journal of Probability 21, paper 31, 2016.
- **[SOTA / Recent]** S. Lalley, W. Su. *Contact processes on random regular graphs.* Annals of Applied Probability 27(4):2061–2097, 2017.
- **[SOTA / Recent]** V. H. Can, B. Schapira. *Metastability for the contact process on the configuration model with infinite mean degree.* Electronic Journal of Probability 20, paper 26, 2015.
- **[SOTA / Recent]** S. Bhamidi, D. Nam, O. Nguyen, A. Sly. *Survival and extinction of epidemics on random graphs with general degree.* Annals of Probability 49(1):244–286, 2021.
- **[SOTA / Recent]** D. Nam, O. Nguyen, A. Sly. *Critical value asymptotics for the contact process on random graphs.* Transactions of the American Mathematical Society 375:3565–3602, 2022.
- **[Survey]** R. Durrett. *Some features of the spread of epidemics and information on a random graph.* PNAS 107(10):4491–4498, 2010.
- **[Survey]** X. Huang, R. Durrett. *The contact process on random graphs and Galton–Watson trees.* ALEA, Latin American Journal of Probability and Mathematical Statistics 17:159–182, 2020.

## 10. Worked Example / Concrete Special Case

**The star $K_{1,n}$: why $\lambda_c = 0$ on power-law graphs.**

Take $G = K_{1,n}$: one centre $o$ and $n$ leaves. Fix small $\lambda>0$ with $\lambda^2 n \gg 1$. Write $k_t$ for the number of infected leaves.

*Quasi-equilibrium.* Given $k$ infected leaves, the centre is infected at rate $\lambda k$ and heals at rate $1$, so on the fast time scale it is infected a fraction
$$ p(k) = \frac{\lambda k}{1 + \lambda k} $$
of the time. Leaves become infected at rate $\lambda (n-k)p(k)$ and heal at total rate $k$. For $k \gg 1/\lambda$ we have $p(k)\approx 1$, so the drift balances at
$$ \lambda(n-k^\ast) = k^\ast \quad\Longrightarrow\quad k^\ast = \frac{\lambda n}{1+\lambda} \approx \lambda n .$$
The consistency condition $k^\ast \gg 1/\lambda$ is exactly $\lambda^2 n \gg 1$.

*Cost of extinction.* Extinction requires the centre to be healthy long enough for every infected leaf to recover without re-infecting it. Suppose the centre heals at time $0$ with $k$ infected leaves and stays healthy. Leaves then decay deterministically to first order, $k(t) \approx k e^{-t}$, and the centre is re-infected at rate $\lambda k(t)$. The probability of no re-infection over the whole decay is
$$ \exp\!\Big(-\int_0^\infty \lambda k e^{-t}\,dt\Big) = e^{-\lambda k}. $$
At $k = k^\ast \approx \lambda n$ this is $e^{-\lambda^2 n}$. Attempts to extinguish occur at rate $O(1)$ (the centre heals at rate 1), so
$$ \mathbb{E}[\tau] \;\gtrsim\; e^{c\lambda^2 n}, \qquad \text{i.e.}\quad \log \mathbb{E}[\tau] \;\ge\; c\,\lambda^2 n .$$
Rigorous versions appear in Berger–Borgs–Chayes–Saberi (2005) and Chatterjee–Durrett (2009, Lemma 5.2); the matching upper bound is known only up to a $\log(1/\lambda)$ factor, $\log\mathbb{E}[\tau]\le C\lambda^2 n\log(1/\lambda)$ *(frontier — verify)*.

*Consequence.* In a configuration model with $\mathbb{P}(D=k)\sim k^{-\beta}$, $\beta>2$, the maximum degree is $d_{\max}\asymp n^{1/(\beta-1)}$, so a star of size $\lambda^{-2}$ exists w.h.p. for every fixed $\lambda>0$ once $n$ is large. That star holds the infection for time $e^{\Theta(1)}\cdot$(super-polynomial in its size), and the infection is passed between hubs along short paths. Hence $\lambda_c = 0$ and $\log\mathbb{E}[\tau_n]\asymp n$ for every $\lambda>0$ — the qualitative point that separates the finite-graph theory from the $\mathbb{Z}^d$ picture, where $\lambda$ must exceed $\lambda_c(\mathbb{Z}^d)>0$.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*