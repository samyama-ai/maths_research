---
id: 09-probability/connectivity-of-the-random-telegraph-noise
title: "Connectivity of the Random Telegraph Noise"
topic: 09-probability
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Connectivity of the Random Telegraph Noise

> **Topic:** Probability & Stochastic Processes · **ID:** `09-probability/connectivity-of-the-random-telegraph-noise` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Attach to every edge (or site) $x$ of a lattice an independent **random telegraph signal**: a stationary two-state continuous-time Markov chain $\omega_x(t) \in \{0,1\}$ that flips at rate $1$ and has marginal $\mathbb{P}(\omega_x = 1) = p$. The resulting process $t \mapsto \omega(t)$ is a stationary Markov process on $\{0,1\}^{E}$ whose one-time law is Bernoulli($p$) product measure — this is **dynamical percolation** in the sense of Häggström, Peres and Steif (1997).

The problem is to determine the **connectivity structure of the whole trajectory**, not of a single snapshot. Fix $p = p_c$, the critical point, and assume $\theta(p_c) = \mathbb{P}_{p_c}(0 \leftrightarrow \infty) = 0$, so that for each *fixed* $t$ there is a.s. no infinite cluster. Fubini gives that Lebesgue-a.e. $t$ has no infinite cluster. The questions are:

1. **(Existence)** Is the exceptional set $\mathcal{E} = \{t \in [0,\infty) : \omega(t) \text{ has an infinite cluster}\}$ nonempty a.s.?
2. **(Dimension)** If so, what is $\dim_H \mathcal{E}$, and what is $\dim_H \mathcal{E}_0 = \dim_H\{t : 0 \leftrightarrow \infty \text{ in } \omega(t)\}$?
3. **(Quantitative sensitivity)** For the finite-volume crossing event $f_R$ of an $R \times R$ box, at what decorrelation time $t = t(R) \to 0$ does $\mathbb{P}(f_R(\omega(0)) = f_R(\omega(t)) ) $ cease to be $1 - o(1)$ — i.e. what is the exact noise-sensitivity exponent?

A complete solution answers (1)–(3) for $\mathbb{Z}^d$ in every dimension $d \ge 2$ with sharp exponents. The problem is **partially solved**: it is settled with exact constants in two dimensions on the triangular lattice, and open in $d \ge 3$.

## 2. Mathematical Foundations

**The telegraph semigroup.** For a single coordinate at density $p$ with flip rate $1$,
$$\mathbb{P}(\omega_x(t) = 1 \mid \omega_x(0) = 1) = p + (1-p)e^{-t}, \qquad \mathrm{Cov}(\omega_x(0),\omega_x(t)) = p(1-p)e^{-t}.$$
The product process is reversible with respect to $\pi_p = \mathrm{Ber}(p)^{\otimes E}$ and has generator $\mathcal{L}f = \sum_x (\mathbb{E}_x f - f)$.

**Fourier–Walsh diagonalisation.** At $p=1/2$, write $\chi_S(\omega) = \prod_{x \in S}(-1)^{\omega_x}$ and $f = \sum_{S} \hat f(S)\chi_S$. The telegraph semigroup acts diagonally:
$$\mathbb{E}\big[f(\omega(0))\,f(\omega(t))\big] = \sum_{S \subseteq E} \hat f(S)^2 e^{-t|S|}.$$
Equivalently, with resampling parameter $\varepsilon = 1 - e^{-t}$, this is the classical noise operator $T_{1-\varepsilon}$. A sequence $f_n$ of $\{-1,1\}$-valued functions is **noise sensitive** at scale $\varepsilon_n$ if $\sum_{S \ne \emptyset} \hat f_n(S)^2 (1-\varepsilon_n)^{|S|} \to 0$. The **spectral sample** $\mathscr{S}_f$ is the random set with $\mathbb{P}(\mathscr{S}_f = S) = \hat f(S)^2/\|f\|_2^2$; sensitivity at scale $\varepsilon$ is exactly the statement $\mathbb{P}(0 < |\mathscr{S}_f| < 1/\varepsilon) \to 0$ together with $\hat f(\emptyset)^2 \to 0$.

**Arm exponents.** Let $\alpha_1(r) = \mathbb{P}_{p_c}(0 \leftrightarrow \partial B_r)$ and $\alpha_4(r)$ the probability of four alternating arms from $0$ to $\partial B_r$. On the triangular lattice (Smirnov–Werner 2001, Lawler–Schramm–Werner):
$$\alpha_1(r) = r^{-5/48 + o(1)}, \qquad \alpha_4(r) = r^{-5/4 + o(1)}.$$
Since $\alpha_4$ is the probability that a pivotal switch matters, the influence sum for the crossing event satisfies $\sum_x \mathrm{Inf}_x(f_R) \asymp R^2\alpha_4(R) = R^{3/4 + o(1)}$, which is $\mathbb{E}|\mathscr{S}_{f_R}|$.

**Second-moment criterion.** For $X_R = \int_0^1 \mathbf 1\{0 \leftrightarrow \partial B_R \text{ in } \omega(t)\}\,dt$, existence of exceptional times reduces to controlling
$$\mathbb{E}[X_R^2] \;\asymp\; \int_0^1 \mathbb{P}\big(0\leftrightarrow \partial B_R \text{ at times } 0 \text{ and } t\big)\,dt$$
against $\mathbb{E}[X_R]^2 = \alpha_1(R)^2$, then applying Paley–Zygmund and letting $R \to \infty$. Häggström–Peres–Steif also gave the negative criterion: if $\int_0^1 \varepsilon^{-2}\theta(p_c+\varepsilon)\,d\varepsilon < \infty$ then $\mathcal{E} = \emptyset$ a.s.

## 3. History & State of the Art (SOTA)

- **1983.** Aldous, and independently Steif's later formulation, note that dynamic versions of static a.s. events can fail at exceptional times.
- **1997.** Häggström, Peres, Steif, *Dynamical percolation* (Ann. IHP): introduce the model, prove $\mathcal{E} = \emptyset$ for $p \ne p_c$ (by a Fubini/quasi-monotonicity argument), prove exceptional times exist at criticality on spherically symmetric trees with the right branching profile, and give the integral test above.
- **1998.** Peres–Steif: on trees the number of infinite clusters at exceptional times is determined; $\dim_H \mathcal{E}$ computed for a class of trees.
- **1999.** Benjamini–Kalai–Schramm: percolation crossings are noise sensitive at *any* fixed $\varepsilon > 0$, via the hypercontractive influence bound $\sum_x \mathrm{Inf}_x^2$; too weak to reach $\varepsilon \to 0$.
- **2010.** Schramm–Steif (Ann. of Math.): randomised-algorithm bound on the spectrum gives sensitivity at $\varepsilon = R^{-\delta}$, and hence **exceptional times exist on the triangular lattice**, with $\dim_H\mathcal{E} \in [1/6, 31/36]$.
- **2010.** Garban–Pete–Schramm (Acta Math.): full multi-scale analysis of the spectral sample; $\mathbb{E}|\mathscr{S}_{f_R}| \asymp R^2\alpha_4(R)$ is the correct sensitivity scale; **exceptional times also exist for bond percolation on $\mathbb{Z}^2$**, and on the triangular lattice $\dim_H \mathcal{E} = 31/36$, $\dim_H\mathcal{E}_0 = 2/3$.
- **2015.** Hammond–Pete–Schramm: construction of the local time / natural measure on $\mathcal{E}_0$ and identification of the configuration at a "typical" exceptional time with the incipient infinite cluster.
- **$d \ge 3$:** no dimension is settled; even existence of exceptional times is open.

## 4. Partial Results / Verified Cases

- **Off-critical, all $d$, all lattices:** for $p \neq p_c$ the connectivity of $\omega(t)$ is a.s. constant in $t$ (no exceptional times) — HPS 1997.
- **Triangular lattice site percolation, $d = 2$, $p_c = 1/2$:** $\mathcal{E} \ne \emptyset$ a.s.; $\dim_H\mathcal{E} = 31/36$, $\dim_H\mathcal{E}_0 = 2/3$ (GPS 2010). Crossing events are sensitive for $\varepsilon \gg R^{-3/4+o(1)}$ and stable for $\varepsilon \ll R^{-3/4 - o(1)}$.
- **Bond percolation on $\mathbb{Z}^2$, $p_c = 1/2$:** exceptional times exist (GPS 2010); the dimension is only known up to the unproven values of the $\mathbb{Z}^2$ arm exponents.
- **Trees:** for spherically symmetric trees with level sizes $Z_n$, exceptional times at $p_c$ exist iff $\sum_n \frac{1}{n^2 Z_n p_c^{\,n}} < \infty$-type criteria hold (HPS 1997, Peres–Steif 1998); dimension formulas are exact here.
- **Half-plane / one-arm variants, $d=2$:** exceptional times for the half-plane one-arm event have dimension $2/3$-type formulas derived from $\alpha_4^{\mathbb H}$.
- **Dynamical Erdős–Rényi graph $G(n,1/n)$:** Roberts–Şengül (2018) show exceptional times exist at which the largest component is atypically large, of order $n^{2/3}\log^{1/3} n$.
- **Continuum (Poisson Boolean) percolation, $d=2$:** crossing events are noise sensitive (Ahlberg–Broman–Griffiths–Morris 2014).
- **Interacting dynamics:** for exclusion-type and Glauber-type dynamics on the edges, stability/instability results in the supercritical regime are known (Broman–Steif 2006).

## 5. Principal Obstacles

- **No conformal invariance off the triangular lattice or above $d = 2$.** The exact exponents $5/48$ and $5/4$ come from SLE$_6$ and Smirnov's theorem, available only for site percolation on $\mathbb{T}$. Every dimension computation is exponent-driven, so $\mathbb{Z}^2$ and all $d\ge 3$ inherit an unknown.
- **The spectral sample is not a percolation configuration.** GPS's method controls $\mathscr{S}_{f_R}$ by comparing it to a multi-scale fractal with a "clustering" estimate $\mathbb{P}(\mathscr{S} \cap B \neq \emptyset,\ |\mathscr{S}| \text{ small})$. The proof leans on planar duality (RSW crossings in all four directions) to bound the number of pivotals in an annulus. In $d \ge 3$ there is no dual, no RSW, and no proof that $\sum_x \mathrm{Inf}_x(f_R) \to \infty$ polynomially.
- **The high-dimensional regime is a genuine dichotomy, not a technical gap.** For $d$ large the mean-field bound $\theta(p_c+\varepsilon) = \Theta(\varepsilon)$ (Barsky–Aizenman; Hara–Slade lace expansion) makes the HPS integral $\int_0^1 \varepsilon^{-2}\theta(p_c+\varepsilon)d\varepsilon$ diverge logarithmically, so the negative criterion is *exactly* inconclusive; deciding it requires a genuinely sharper second-moment input than any current correlation estimate.
- **Two-time correlation estimates.** The key quantity $\mathbb{P}(0\leftrightarrow\partial B_R \text{ at } 0 \text{ and } t)$ requires knowing how much of the cluster survives a rate-$t$ resampling. In $d=2$ this is done by "the pivotal switches happen at scale $r(t)$ where $r^2\alpha_4(r) \approx 1/t$". No analogue of the pivotal-counting identity is proven in $d\ge3$.
- **Hypercontractivity saturates.** BKS-type bounds only give sensitivity for $\varepsilon$ bounded away from $0$; they cannot see $\varepsilon = R^{-3/4}$, and no soft argument closes the polynomial gap.

## 6. The Gap

The proven statements are: existence and (on $\mathbb{T}$) exact dimension in $d=2$; nonexistence off criticality in all $d$. The general statement asks for the same in every $d \ge 2$.

The precise missing step in $d \ge 3$ is a two-sided estimate
$$\mathbb{P}\big(0 \leftrightarrow \partial B_R \text{ at times } 0 \text{ and } t\big) \;\asymp\; \alpha_1(R)^2 \cdot \Psi_d(t)$$
with $\Psi_d(t) = t^{-\gamma_d + o(1)}$ for an explicit $\gamma_d$, together with the matching statement $\gamma_d > 0$ iff exceptional times exist. Producing $\Psi_d$ requires (i) a pivotal-density estimate replacing $R^d\alpha_4^{(d)}(R)$, and (ii) a quasi-multiplicativity property for $d$-dimensional arm events, neither of which is available. In the mean-field regime the gap is the sharper question of whether $\theta(p_c + \varepsilon)/\varepsilon$ carries a logarithmic correction, which decides the HPS integral test outright.

## 7. Current Research (as of June 2026)

- **Sharp high-dimensional two-time estimates.** Groups working with the lace expansion (van der Hofstad and collaborators, Eindhoven; Slade, UBC) are pushing towards two-time connection probabilities for spread-out models in $d > 6$, where the triangle condition holds. *(frontier — verify)*
- **Noise sensitivity beyond planarity.** Extending the GPS spectral machinery to models with a Markov-type spatial decomposition — FK-percolation, Voronoi, Poisson–Boolean — is active (Geneva/Paris school around Duminil-Copin, Tassion; Ahlberg in Stockholm).
- **Natural measures and scaling limits of $\mathcal{E}$.** Following Hammond–Pete–Schramm, work on convergence of the local-time measure on $\mathcal{E}_0$ and on the dynamical scaling limit as a Markov process on continuum percolation configurations. *(frontier — verify)*
- **Random graph analogues.** Dynamical Erdős–Rényi at criticality, dynamical configuration models, and dynamical percolation on expanders/hyperbolic graphs (where $p_c < p_u$ makes uniqueness itself dynamical).
- **Algorithmic bounds.** Refinements of the Schramm–Steif randomised-algorithm bound and of OSSS-type inequalities as a dimension-free route to noise sensitivity.

## 8. Future Work

- Prove or disprove existence of exceptional times for $\mathbb{Z}^3$; even a non-quantitative existence proof would be a major advance.
- Establish quasi-multiplicativity of arm events in $d = 3$, the standard prerequisite for any multi-scale pivotal analysis.
- Determine whether the HPS integral test is sharp: is $\int_0^1 \varepsilon^{-2}\theta(p_c+\varepsilon)d\varepsilon = \infty$ sufficient for $\mathcal{E} \ne \emptyset$ on transitive graphs?
- Compute $\dim_H\mathcal{E}$ for $\mathbb{Z}^2$ bond percolation conditional on the (conjectured, unproven) universality of the planar arm exponents.
- Extend the theory to non-reversible or non-independent telegraph dynamics (exclusion, Glauber at low temperature), where the semigroup is no longer diagonal in the Fourier–Walsh basis.

## 9. Key References

- **[Foundational]** O. Häggström, Y. Peres, J. E. Steif. *Dynamical percolation.* Annales de l'IHP Probabilités et Statistiques 33 (1997), 497–528.
- **[Foundational]** I. Benjamini, G. Kalai, O. Schramm. *Noise sensitivity of Boolean functions and applications to percolation.* Publications Mathématiques de l'IHÉS 90 (1999), 5–43.
- **[Foundational]** Y. Peres, J. E. Steif. *The number of infinite clusters in dynamical percolation.* Probability Theory and Related Fields 111 (1998), 141–165.
- **[SOTA]** O. Schramm, J. E. Steif. *Quantitative noise sensitivity and exceptional times for percolation.* Annals of Mathematics 171 (2010), 619–672.
- **[SOTA]** C. Garban, G. Pete, O. Schramm. *The Fourier spectrum of critical percolation.* Acta Mathematica 205 (2010), 19–104.
- **[SOTA]** A. Hammond, G. Pete, O. Schramm. *Local time on the exceptional set of dynamical percolation and the incipient infinite cluster.* Annals of Probability 43 (2015), 2949–3005.
- **[Recent]** M. Roberts, B. Şengül. *Exceptional times of the critical dynamical Erdős–Rényi graph.* Annals of Applied Probability 28 (2018), 2275–2308.
- **[Recent]** D. Ahlberg, E. Broman, S. Griffiths, R. Morris. *Noise sensitivity in continuum percolation.* Israel Journal of Mathematics 201 (2014), 847–899.
- **[Related]** E. Broman, J. E. Steif. *Dynamical stability of percolation for some interacting particle systems and $\varepsilon$-movability.* Annals of Probability 34 (2006), 539–576.
- **[Survey]** C. Garban, J. E. Steif. *Noise Sensitivity of Boolean Functions and Percolation.* Cambridge University Press, 2014.
- **[Survey]** J. E. Steif. *A survey of dynamical percolation.* In *Fractal Geometry and Stochastics IV*, Progress in Probability 61, Birkhäuser, 2009, 145–174.
- **[Background]** S. Smirnov, W. Werner. *Critical exponents for two-dimensional percolation.* Mathematical Research Letters 8 (2001), 729–744.
- **[Background]** T. Hara, G. Slade. *Mean-field critical behaviour for percolation in high dimensions.* Communications in Mathematical Physics 128 (1990), 333–391.

## 10. Worked Example / Concrete Special Case

**Setting.** Take $n$ independent rate-$1$ telegraph bits $\omega_1(t),\dots,\omega_n(t)$ with $\mathbb{P}(\omega_i = 1) = p$, and let $A_t = \{\omega_1(t) = \cdots = \omega_n(t) = 1\}$ — the "all-open" event, the toy version of a crossing that needs every edge on a path. Statically, $\mathbb{P}(A_0) = p^n$, exponentially small. The question: does $A_t$ occur at some $t \in [0,1]$?

**First moment.** $X = \int_0^1 \mathbf 1_{A_t}\,dt$, so $\mathbb{E}[X] = p^n$.

**Second moment.** Using the telegraph transition kernel $\mathbb{P}(\omega_i(t)=1\mid \omega_i(0)=1) = p + (1-p)e^{-t}$ and independence across $i$,
$$\mathbb{P}(A_0 \cap A_t) = \big[p\,(p + (1-p)e^{-t})\big]^n = p^{2n}\Big(1 + \tfrac{1-p}{p}e^{-t}\Big)^n .$$
Hence
$$\mathbb{E}[X^2] = 2\int_0^1 (1-t)\,\mathbb{P}(A_0\cap A_t)\,dt \;\le\; 2p^{2n}\int_0^1\Big(1+\tfrac{q}{p}e^{-t}\Big)^n dt, \qquad q = 1-p.$$
Substituting $u = e^{-t}$ gives $\int_{e^{-1}}^{1}(1+\tfrac qp u)^n \tfrac{du}{u} \le e\cdot \frac{p}{q(n+1)}\big[(1+\tfrac qp)^n - 1\big] \asymp \frac{1}{n}\,p^{-n}\cdot\frac{p}{q}$, since $1 + q/p = 1/p$. So
$$\frac{\mathbb{E}[X^2]}{\mathbb{E}[X]^2} \;\asymp\; \frac{p^{2n}\cdot n^{-1}p^{-n}}{p^{2n}}\cdot\frac{p}{q} \;\asymp\; \frac{p^{1-n}}{qn}.$$
Paley–Zygmund then yields $\mathbb{P}(X > 0) \gtrsim n\,q\,p^{\,n-1}$: **the dynamics multiplies the static probability by a factor of order $n$**, the number of coordinates that can be pivotal. Concretely, at $p = 1/2$, $n = 20$: static probability $\approx 9.5\times 10^{-7}$, whereas $\mathbb{P}(\exists t\in[0,1]: A_t) \approx 2\times 10^{-5}$ — a twenty-fold gain, and matching the direct count of "all-open windows", which appear at rate $\asymp n q p^{n-1}$.

**Bridge to percolation.** The same computation is the engine of the real theorem, with "number of coordinates" replaced by "number of pivotals". For the one-arm event $\{0 \leftrightarrow \partial B_R\}$ on the triangular lattice, resampling for time $t$ changes only the pivotals up to the scale $r = r(t)$ with $r^2\alpha_4(r) \asymp 1/t$, i.e. $r(t) = t^{-4/3+o(1)}$ from $\alpha_4(r) = r^{-5/4}$. Plugging this into $\mathbb{P}(0\leftrightarrow\partial B_R \text{ at }0,\,t) \asymp \alpha_1(R)^2/\alpha_1(r(t))$ makes $\int_0^1 \cdot\,dt$ comparable to $\alpha_1(R)^2 \cdot R^{o(1)}$, so the second moment stays bounded as $R\to\infty$ and $\mathcal{E}_0 \neq \emptyset$; the exponent bookkeeping $1 - \tfrac{4}{3}\cdot\tfrac{5}{48}\cdot 2 = \tfrac 23$ is exactly the Hausdorff dimension $\dim_H \mathcal{E}_0 = 2/3$ proved by Garban–Pete–Schramm. In $d\ge 3$ every ingredient of this chain — $\alpha_1$, $\alpha_4$, the pivotal-scale identity — is unavailable, which is precisely the gap of Section 6.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*