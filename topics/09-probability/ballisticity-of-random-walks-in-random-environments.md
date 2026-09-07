---
id: 09-probability/ballisticity-of-random-walks-in-random-environments
title: "Ballisticity of Random Walks in Random Environments"
topic: 09-probability
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Ballisticity of Random Walks in Random Environments

> **Topic:** Probability & Stochastic Processes · **ID:** `09-probability/ballisticity-of-random-walks-in-random-environments` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Let $\omega = (\omega(x,\cdot))_{x \in \mathbb{Z}^d}$ be an i.i.d. uniformly elliptic random environment on $\mathbb{Z}^d$, and let $(X_n)_{n \ge 0}$ be the random walk that, from $x$, jumps to $x+e$ with probability $\omega(x,e)$. Fix a direction $\ell \in S^{d-1}$.

**Ballisticity conjecture (Kalikow; Sznitman–Zerner).** For $d \ge 2$, if the walk is transient in direction $\ell$, i.e.
$$P_0\big[A_\ell\big] = 1, \qquad A_\ell := \{X_n \cdot \ell \to +\infty\},$$
then the walk is *ballistic*: there is a deterministic $v \ne 0$ with
$$\lim_{n \to \infty} \frac{X_n}{n} = v \quad P_0\text{-a.s.}, \qquad v \cdot \ell > 0 .$$

Equivalently, in $d\ge2$ the zero-speed transient regime that exists in $d = 1$ should be empty under uniform ellipticity. A complete proof must rule out **all** trapping mechanisms producing $\lim X_n \cdot \ell / n = 0$ on $A_\ell$; a disproof requires an explicit i.i.d. uniformly elliptic environment in some $d \ge 2$ that is directionally transient with zero speed.

Two companion problems are standard:

* **Sznitman's conjecture (now essentially settled, §4):** the ballisticity conditions $(T)_\gamma$, $\gamma \in (0,1)$, are all equivalent to $(T')$.
* **Directional 0–1 law:** for $d \ge 3$, is $P_0[A_\ell] \in \{0,1\}$?

## 2. Mathematical Foundations

**Environment space.** $\Omega = \mathcal{P}^{\mathbb{Z}^d}$ where $\mathcal{P} = \{(p_e)_{|e|=1} : p_e \ge 0,\ \sum_e p_e = 1\}$, with product measure $\mathbb{P} = \mu^{\otimes \mathbb{Z}^d}$. *Uniform ellipticity*: there is $\kappa > 0$ with $\mu[\omega(0,e) \ge \kappa] = 1$ for all $2d$ unit vectors $e$. *Ellipticity* only requires $\omega(0,e) > 0$ a.s.

**Quenched and annealed laws.** For fixed $\omega$, $P_{x,\omega}$ is the Markov law with $P_{x,\omega}[X_{n+1} = X_n + e \mid X_n] = \omega(X_n,e)$. The annealed (averaged) law is $P_x[\cdot] = \int P_{x,\omega}[\cdot]\, \mathbb{P}(d\omega)$; it is not Markovian.

**Regeneration structure (Sznitman–Zerner 1999).** Under transience in $\ell$ define $\tau_1$, the first time the walk reaches a new maximum of $X_\cdot \cdot \ell$ and never backtracks below it. Iterating gives $\tau_1 < \tau_2 < \cdots$ such that $(X_{\tau_{k+1}} - X_{\tau_k}, \tau_{k+1} - \tau_k)_{k \ge 1}$ are i.i.d. under $P_0[\,\cdot \mid A_\ell]$. Renewal theory then gives
$$\frac{X_n}{n} \longrightarrow v = \frac{E_0[X_{\tau_2} - X_{\tau_1} \mid A_\ell]}{E_0[\tau_2 - \tau_1 \mid A_\ell]} \quad \text{a.s.},$$
with $v \neq 0$ **iff** $E_0[\tau_2 - \tau_1 \mid A_\ell] < \infty$. The conjecture is therefore exactly the integrability of the regeneration time.

**Ballisticity conditions.** For $L > 0$ let $U_{L,\ell} = \{x : -bL < x\cdot\ell < L\}$ be a slab and $T_{U}$ its exit time. Sznitman's condition
$$(T)_\gamma \mid \ell: \quad \limsup_{L \to \infty} L^{-\gamma} \log P_0\big[X_{T_{U_{L,\ell}}} \cdot \ell < 0\big] < 0, \qquad \gamma \in (0,1],$$
with $(T) := (T)_1$ and $(T') := \bigcap_{\gamma < 1} (T)_\gamma$. The polynomial condition $(P)_M \mid \ell$ requires, for one large $L$,
$$P_0\big[X_{T_{U_{L,\ell}}}\cdot \ell < 0\big] \le L^{-M}.$$

**Kalikow's condition.** With the Kalikow auxiliary walk drift $\hat d_U(x) = \sum_e e \, \hat\omega_U(x,e)$, where $\hat\omega_U$ is built from Green's-function averages $E[G_{U,\omega}(0,x)\omega(x,e)]/E[G_{U,\omega}(0,x)]$, Kalikow's condition is $\inf_{U,x} \hat d_U(x) \cdot \ell > 0$. It implies $(T)$, hence ballisticity.

**One-dimensional benchmark.** For $d = 1$ with $\rho_x = \frac{1-\omega(x,1)}{\omega(x,1)}$ (Solomon 1975):
$$\text{transient to } +\infty \iff \mathbb{E}[\log \rho] < 0, \qquad v = \frac{1 - \mathbb{E}[\rho]}{1 + \mathbb{E}[\rho]} \ \text{ if } \mathbb{E}[\rho] < 1, \quad v = 0 \ \text{ if } \mathbb{E}[\rho] \ge 1 .$$

## 3. History & State of the Art (SOTA)

* **1975.** Solomon gives the complete $d=1$ picture, including the zero-speed transient phase. Kesten–Kozlov–Spitzer identify the limit laws via the index $s$ with $\mathbb{E}[\rho^s] = 1$.
* **1982.** Sinai: the recurrent $d=1$ walk is $(\log n)^2$-subdiffusive — dimension one is dominated by traps.
* **1981.** Kalikow introduces the auxiliary-walk condition and the 0–1 law $P_0[A_\ell] + P_0[A_{-\ell}] \in \{0,1\}$, and conjectures no zero-speed transience for $d \ge 2$.
* **1999.** Sznitman–Zerner build the renewal structure and prove the LLN under Kalikow's condition, reducing ballisticity to $E_0[\tau_2 - \tau_1] < \infty$.
* **2001–2003.** Sznitman introduces $(T)$, $(T')$ and the *effective criterion* — a finite-box, checkable condition implying $(T')$ and hence ballisticity plus an annealed CLT, together with new examples of ballistic walks.
* **2001.** Zerner–Merkl prove the directional 0–1 law in $d = 2$.
* **2014.** Berger–Drewitz–Ramírez: the *polynomial condition* $(P)_M$ with $M \ge 15d+5$, verifiable in a single finite box, implies $(T')$. This is the current practical criterion.
* **2020.** Guerra–Ramírez prove Sznitman's conjecture: $(T)_\gamma \Leftrightarrow (T')$ for all $\gamma \in (0,1)$, collapsing the hierarchy of ballisticity conditions.

The main conjecture — transience $\Rightarrow$ ballisticity for $d \ge 2$ under uniform ellipticity — remains open in every dimension $d \ge 2$.

## 4. Partial Results / Verified Cases

* **$d = 1$:** fully solved and *false* as stated: $\mathbb{E}[\log\rho] < 0 \le \log \mathbb{E}[\rho]$ gives transience with $v = 0$ and $X_n \asymp n^s$, $s \in (0,1)$ (Solomon 1975; Kesten–Kozlov–Spitzer 1975). This is why the conjecture is posed for $d \ge 2$.
* **Under $(T')$, any $d \ge 2$:** ballisticity holds, with annealed CLT (Sznitman 2002), quenched CLT for $d \ge 4$ (Berger–Zeitouni 2008; Rassoul-Agha–Seppäläinen 2009).
* **Checkable criteria:** Kalikow's condition; Sznitman's effective criterion; $(P)_M$ for $M \ge 15d+5$ (Berger–Drewitz–Ramírez 2014) — all imply ballisticity and are decidable from a single finite box.
* **Small perturbations of simple random walk:** for $d \ge 3$ and environments within $\varepsilon(d)$ of uniform in $L^\infty$, ballisticity plus diffusive corrections hold (Sznitman 2003; Bolthausen–Sznitman perturbative expansions).
* **Non-nestling walks** (a.s. drift $d(x)\cdot\ell \ge \delta > 0$): Kalikow's condition holds trivially, so ballistic in all $d$.
* **Dirichlet environments, $d \ge 3$:** complete answer. With parameters $(\alpha_e)$ and $\kappa = 2\sum_e \alpha_e - \max_e(\alpha_e + \alpha_{-e})$, the walk is ballistic iff $\kappa > 1$; for $\kappa \le 1$ it is transient with zero speed and $X_n \approx n^{\kappa}$ (Sabot 2013; Bouchet 2013; Sabot–Tournier). These environments are elliptic but **not uniformly** elliptic.
* **Counterexample without uniform ellipticity:** Bramson–Zeitouni–Zerner (2006) construct an i.i.d. elliptic environment in $d = 2$ that is transient with zero speed — so uniform ellipticity is not a removable hypothesis.
* **Ellipticity thresholds:** Campos–Ramírez (2014) give explicit moment conditions on $\omega(0,e)^{-1}$ under which $(T')$-type criteria still force ballisticity, quantifying how weak ellipticity may be.

## 5. Principal Obstacles

* **Traps are not excluded by transience.** A finite region where the environment locally pushes backwards costs $\mathbb{P}$-probability $e^{-c|B|}$ but can hold the walk for time $e^{c'|B|}$. Uniform ellipticity should force cost to beat reward for $d\ge2$, but no entropy-versus-energy comparison is known that is uniform over trap shapes. Both quantities are exponential with unmatched constants.
* **Loss of the Markov property.** Under the annealed law the walk is self-interacting through re-visits; regeneration times repair this only *after* transience is assumed, and they carry no a priori tail control.
* **Renormalisation needs a seed estimate.** All successful arguments (effective criterion, $(P)_M$, $(T)_\gamma \Rightarrow (T')$) are multiscale schemes that propagate an atypical-backtracking estimate from scale $L$ to $L^{3/2}$ or $L^{1+\varepsilon}$. Each requires an initial finite-box input. Directional transience alone provides only $P_0[\text{backtrack}] = o(1)$ with no rate, and no known argument upgrades $o(1)$ to $L^{-M}$.
* **No harmonic-analytic or homogenisation route.** The environment seen from the particle has no explicit invariant measure absolutely continuous w.r.t. $\mathbb{P}$ in the ballistic regime (unlike balanced or Dirichlet cases), so the standard "environment viewed from the particle + ergodic theorem" machinery is unavailable.
* **$d = 2$ recurrence of the underlying lattice** makes re-visits frequent, defeating perturbative expansions that work for $d \ge 3$.
* **Missing 0–1 law for $d \ge 3$** means one cannot even reduce to a clean dichotomy; $P_0[A_\ell] \in (0,1)$ is not excluded.

## 6. The Gap

Everything proven passes through some quantitative decay of the backtracking probability:
$$P_0\big[X_{T_{U_{L,\ell}}} \cdot \ell < 0\big] \le L^{-M} \ \ (\text{one } L) \quad \Longrightarrow \quad (T') \quad \Longrightarrow \quad v \ne 0 .$$
What is *assumed* in the conjecture is only
$$P_0\big[X_{T_{U_{L,\ell}}} \cdot \ell < 0\big] \xrightarrow[L\to\infty]{} 0 \quad\text{with no rate.}$$
The gap is exactly the implication
$$\text{transience in } \ell \ \Longrightarrow \ (P)_M \mid \ell \ \text{ for some } M \ge 15d+5 .$$
Equivalently: prove $E_0[\tau_2 - \tau_1 \mid A_\ell] < \infty$, or exclude environments in which the annealed backtracking probability decays slower than any power of $L$ while still vanishing.

## 7. Current Research (as of June 2026)

* **Post-Guerra–Ramírez consolidation.** With $(T)_\gamma \equiv (T')$ settled, effort has shifted to whether $(T')$ itself is *equivalent* to directional transience under uniform ellipticity — i.e. whether the condition hierarchy is not merely internally collapsed but complete. Groups at PUC Chile / NYU Shanghai (Ramírez and collaborators) drive this line.
* **Trap geometry and ellipticity thresholds.** Fribergh, Kious and coauthors quantify local trapping for elliptic (non-uniformly elliptic) walks, mapping the exact ellipticity moment at which zero-speed transience appears — narrowing where a counterexample could live. *(frontier — verify)*
* **Dirichlet and random-conductance models** remain the testing ground: exactly solvable ballisticity thresholds ($\kappa = 1$) give the sharp shape of the trapping mechanism the conjecture must exclude.
* **Renormalisation with fewer inputs.** Attempts to run the Berger–Drewitz–Ramírez scheme starting from purely qualitative transience, using entropy bounds on trap configurations instead of a seed polynomial estimate. No success reported. *(frontier — verify)*
* **Quenched CLT in $d = 2, 3$ under $(T')$** is still incomplete and is pursued in parallel.

## 8. Future Work

1. **Prove a "no rate needed" renormalisation:** show that $P_0[\text{backtrack past } -L] \to 0$ forces polynomial decay, perhaps by a sprinkling/decoupling argument on the environment.
2. **Establish the directional 0–1 law for $d \ge 3$**, which Zerner–Merkl obtained in $d=2$ by planar-topology arguments unavailable in higher dimensions.
3. **Classify traps by entropy:** develop a large-deviation cost functional for finite trap configurations and prove cost $>$ holding-time reward for $d \ge 2$ under uniform ellipticity $\kappa$.
4. **Interpolate ellipticity:** find the sharp function $\kappa \mapsto$ (ballistic / zero-speed) for i.i.d. environments, unifying the Dirichlet threshold with the Bramson–Zeitouni–Zerner counterexample.
5. **Counterexample search:** systematic computational search in $d=2$ for uniformly elliptic laws with anomalously slow backtracking decay.

## 9. Key References

- **[Foundational]** F. Solomon. *Random walks in a random environment.* Annals of Probability 3(1), 1–31, 1975.
- **[Foundational]** H. Kesten, M. Kozlov, F. Spitzer. *A limit law for random walk in a random environment.* Compositio Mathematica 30, 145–168, 1975.
- **[Foundational]** S. Kalikow. *Generalized random walk in a random environment.* Annals of Probability 9(5), 753–768, 1981.
- **[Foundational]** Ya. G. Sinai. *The limiting behavior of a one-dimensional random walk in a random medium.* Theory of Probability and Its Applications 27(2), 256–268, 1982.
- **[Foundational]** A.-S. Sznitman, M. Zerner. *A law of large numbers for random walks in random environment.* Annals of Probability 27(4), 1851–1869, 1999.
- **[Foundational]** A.-S. Sznitman. *On a class of transient random walks in random environment.* Annals of Probability 29(2), 724–765, 2001.
- **[Foundational]** A.-S. Sznitman. *An effective criterion for ballistic behavior of random walks in random environment.* Probability Theory and Related Fields 122(4), 509–544, 2002.
- **[Foundational]** M. Zerner, F. Merkl. *A zero-one law for planar random walks in random environment.* Annals of Probability 29(4), 1716–1732, 2001.
- **[SOTA / Recent]** N. Berger, A. Drewitz, A. F. Ramírez. *Effective polynomial ballisticity conditions for random walk in random environment.* Communications on Pure and Applied Mathematics 67(12), 1947–1973, 2014.
- **[SOTA / Recent]** E. Guerra, A. F. Ramírez. *A proof of Sznitman's conjecture about ballistic random walks in random environments.* Journal of the London Mathematical Society, 2020.
- **[SOTA / Recent]** C. Sabot. *Random Dirichlet environment viewed from the particle in dimension $d \ge 3$.* Annals of Probability 41(2), 722–743, 2013.
- **[SOTA / Recent]** É. Bouchet. *Sub-ballistic random walk in Dirichlet environment.* Electronic Journal of Probability 18, paper 58, 2013.
- **[SOTA / Recent]** M. Bramson, O. Zeitouni, M. Zerner. *Shortest spanning trees and a counterexample for random walks in random environments.* Annals of Probability 34(3), 821–856, 2006.
- **[SOTA / Recent]** D. Campos, A. F. Ramírez. *Ellipticity criteria for ballistic behavior of random walks in random environment.* Probability Theory and Related Fields 160(1–2), 189–251, 2014.
- **[Survey]** O. Zeitouni. *Random walks in random environment.* Lectures on Probability Theory and Statistics, École d'Été de Probabilités de Saint-Flour XXXI, Lecture Notes in Mathematics 1837, Springer, 2004.
- **[Survey]** A. Drewitz, A. F. Ramírez. *Selected topics in random walks in random environment.* In *Topics in Percolative and Disordered Systems*, Springer Proceedings in Mathematics & Statistics 69, 23–83, 2014.
- **[Survey]** C. Sabot, L. Tournier. *Random walks in Dirichlet environment: an overview.* Annales de la Faculté des Sciences de Toulouse 26(2), 463–509, 2017.

## 10. Worked Example / Concrete Special Case

**A $d = 1$ walk that is transient with zero speed.** Let $\omega(x,1)$ be i.i.d. with
$$\omega(x,1) = \tfrac{9}{10} \ \text{ w.p. } \tfrac12, \qquad \omega(x,1) = \tfrac14 \ \text{ w.p. } \tfrac12 .$$
This is uniformly elliptic with $\kappa = 1/10$. Then $\rho = (1-\omega)/\omega$ takes values $1/9$ and $3$, each w.p. $1/2$.

*Transience.* $\mathbb{E}[\log \rho] = \tfrac12\log\tfrac19 + \tfrac12 \log 3 = \tfrac12 \log \tfrac13 < 0$, so by Solomon $X_n \to +\infty$ a.s.

*Speed.* $\mathbb{E}[\rho] = \tfrac12(\tfrac19 + 3) = \tfrac{14}{9} \approx 1.556 > 1$, so $v = 0$: the walk escapes to $+\infty$ but sublinearly.

*Rate of escape.* The Kesten–Kozlov–Spitzer index solves $\mathbb{E}[\rho^s] = 1$. Writing $x = 3^s$,
$$\tfrac12\big(x^{-2} + x\big) = 1 \iff x^3 - 2x^2 + 1 = 0 \iff (x-1)(x^2 - x - 1) = 0 ,$$
so $x = \varphi = \frac{1+\sqrt5}{2}$ and
$$s = \frac{\log \varphi}{\log 3} = \frac{0.4812}{1.0986} \approx 0.438 \in (0,1).$$
Hence $X_n \approx n^{0.438}$, and $\tau_n / n^{1/s}$ converges to a stable law of index $s$; the regeneration time has infinite mean, $E_0[\tau_2 - \tau_1] = \infty$.

*Mechanism.* The environment contains stretches of $k$ consecutive sites with $\rho = 3$ (probability $2^{-k}$) that act as backward-drift traps; the expected exit time from such a stretch is of order $3^k$. Since $3^k \cdot 2^{-k} = 1.5^k \to \infty$, rare traps dominate the mean holding time and kill the speed.

*Why $d \ge 2$ should differ.* In $d \ge 2$ the walk can go **around** a backward-drift block: escaping a trap of diameter $k$ requires only a transversal excursion, so the quenched exit time is expected to be polynomial in $k$ rather than $e^{ck}$, while the probability of the trap remains $e^{-ck^d}$. The conjecture asserts this heuristic is exact under uniform ellipticity — but no proof converts it into the seed estimate $P_0[X_{T_{U_{L,\ell}}}\cdot\ell < 0] \le L^{-(15d+5)}$ demanded by §6. The Bramson–Zeitouni–Zerner $d=2$ counterexample shows that when $\omega(0,e)$ may approach $0$, "going around" can itself be blocked, and the $d=1$ trapping picture is restored.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*