---
id: 09-probability/contextual-bandit-minimax-regret-gap
title: "Bandit Regret Lower Bounds for Adversarial Contextual Settings"
topic: 09-probability
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Bandit Regret Lower Bounds for Adversarial Contextual Settings

> **Topic:** Probability & Stochastic Processes · **ID:** `09-probability/contextual-bandit-minimax-regret-gap` · **Status:** open

## 1. Problem Statement / Conjecture

Fix $K \ge 2$ arms, a horizon $T$, a context space $\mathcal{X}$, and a finite policy class $\Pi \subseteq [K]^{\mathcal{X}}$ with $|\Pi| = N$. In the adversarial contextual bandit protocol (also called *bandits with expert advice*), an oblivious adversary fixes contexts $x_1,\dots,x_T$ and loss vectors $\ell_1,\dots,\ell_T \in [0,1]^K$ in advance; at round $t$ the learner sees $x_t$, plays $A_t \in [K]$, and observes only $\ell_t(A_t)$.

The minimax regret is
$$\mathcal{R}^\star(T,K,\Pi) \;=\; \inf_{\text{alg}} \; \sup_{\text{adv}} \; \mathbb{E}\Big[\sum_{t=1}^T \ell_t(A_t) \;-\; \min_{\pi \in \Pi} \sum_{t=1}^T \ell_t(\pi(x_t))\Big].$$

**Open problem (information-theoretic form).** Determine $\mathcal{R}^\star(T,K,\Pi)$ up to universal constants as a function of $(T,K,N)$. The two known bounds are
$$c\,\sqrt{\frac{KT\log N}{\log K}} \;\le\; \mathcal{R}^\star(T,K,\Pi) \;\le\; \sqrt{2KT\log N},$$
the upper bound from Exp4 (Auer–Cesa-Bianchi–Freund–Schapire 2002) and the lower bound from Seldin–Lugosi (2016), valid in the regime $K \le N$, $\log N \lesssim T/K$ and $N$ not too large. **Conjecture (Seldin–Lugosi):** the lower bound is tight, i.e. $\mathcal{R}^\star \asymp \sqrt{KT\log N/\log K}$ for all $N \ge K$ in this regime. A complete resolution is either an algorithm matching $\sqrt{KT\log N/\log K}$ for *every* class of size $N$, or a class $\Pi$ on which $\Omega(\sqrt{KT\log N})$ is forced.

**Open problem (infinite classes).** For $\Pi$ of Natarajan / Littlestone dimension $d$, is $\mathcal{R}^\star \asymp \sqrt{KTd}$, or is an extra $\mathrm{polylog}(T)$ (or a $\sqrt{\log K}$-type) factor necessary? Covering plus Exp4 gives only $\tilde O(\sqrt{KTd\log T})$.

**Open problem (computational form).** Is there an algorithm with $\mathrm{poly}(T)$ oracle calls to an offline ERM oracle for $\Pi$ achieving $\tilde O(\sqrt{KT\log N})$ against adversarial contexts? Current oracle-efficient methods stall at $T^{2/3}$.

## 2. Mathematical Foundations

**Protocol and filtration.** Let $\mathcal{F}_t = \sigma(A_1,\ell_1(A_1),\dots,A_t,\ell_t(A_t))$. A policy $\pi$ has cumulative loss $L_T(\pi) = \sum_t \ell_t(\pi(x_t))$; the learner's is $\hat L_T = \sum_t \ell_t(A_t)$, and $\mathcal{R}_T = \mathbb{E}[\hat L_T] - \min_\pi L_T(\pi)$.

**Exp4.** Maintain weights $q_t \in \Delta(\Pi)$, induce the arm distribution
$$p_t(a) \;=\; \sum_{\pi\in\Pi} q_t(\pi)\,\mathbb{1}\{\pi(x_t)=a\},$$
play $A_t \sim p_t$, and form the importance-weighted estimator
$$\hat\ell_t(a) \;=\; \frac{\ell_t(a)}{p_t(a)}\,\mathbb{1}\{A_t=a\}, \qquad \mathbb{E}_t[\hat\ell_t(a)] = \ell_t(a),$$
with per-policy estimate $\hat y_t(\pi) = \hat\ell_t(\pi(x_t))$ and exponential update $q_{t+1}(\pi) \propto q_t(\pi)e^{-\eta \hat y_t(\pi)}$. The standard mirror-descent analysis over the simplex $\Delta(\Pi)$ with negative-entropy potential gives
$$\mathcal{R}_T \;\le\; \frac{\log N}{\eta} \;+\; \frac{\eta}{2}\sum_{t=1}^T \mathbb{E}\!\left[\sum_{\pi} q_t(\pi)\hat y_t(\pi)^2\right] \;\le\; \frac{\log N}{\eta} + \frac{\eta KT}{2},$$
optimized at $\eta = \sqrt{2\log N/(KT)}$ to yield $\sqrt{2KT\log N}$. The variance step uses only $\sum_\pi q_t(\pi)\hat y_t(\pi)^2 \le \sum_a \ell_t(a)^2/p_t(a) \cdot p_t(a)^{\,0}\!\cdot\! \mathbb{1}\{A_t=a\} \Rightarrow \mathbb{E}_t[\cdot] \le K$; it is *exactly this step* that ignores the combinatorial structure of $\Pi$ and is suspected to be loose by $\sqrt{\log K}$.

**Lower-bound machinery.** Regret lower bounds follow from the Bretagnolle–Huber inequality: for measures $P,Q$ on the observation space and an event $E$,
$$P(E) + Q(E^c) \;\ge\; \tfrac12 e^{-\mathrm{KL}(P\|Q)},$$
combined with the bandit divergence decomposition
$$\mathrm{KL}(\mathbb{P}_\nu \| \mathbb{P}_{\nu'}) \;=\; \sum_{a=1}^K \mathbb{E}_\nu[N_a(T)]\,\mathrm{KL}(\nu_a \| \nu'_a),$$
$N_a(T)$ the pull count. For $K$-armed bandits with no contexts this yields $\mathcal{R}^\star \ge \tfrac{1}{27}\sqrt{KT}$ (Auer et al. 2002), matched to constants by INF/Tsallis-INF (Audibert–Bubeck 2009; Zimmert–Seldin 2021), so the pure-bandit case $N=K$ is closed.

**Complexity measures for infinite $\Pi$.** For adversarial contexts, uniform convergence must be *sequential*: the relevant quantity is the sequential Rademacher complexity $\mathfrak{R}^{\mathrm{seq}}_T(\Pi)$ over binary trees $\mathbf{x}:\{\pm1\}^{<T}\to\mathcal{X}$,
$$\mathfrak{R}^{\mathrm{seq}}_T(\mathcal{G}) = \sup_{\mathbf{x}} \mathbb{E}_\epsilon \sup_{g\in\mathcal{G}} \frac1T\sum_{t=1}^T \epsilon_t\, g(\mathbf{x}_t(\epsilon_{<t})),$$
controlled by the Littlestone dimension rather than the VC dimension (Rakhlin–Sridharan–Tewari 2015).

## 3. History & State of the Art (SOTA)

- **1995–2002.** Auer, Cesa-Bianchi, Freund and Schapire introduce Exp3 and Exp4 and prove $O(\sqrt{KT\log N})$ for bandits with expert advice, plus the $\Omega(\sqrt{KT})$ lower bound for $N=K$ (SIAM J. Comput. 32(1), 2002). The $\sqrt{\log N}$ dependence has stood as the upper bound for 24 years.
- **2009–2011.** Audibert–Bubeck remove the $\log K$ from the $K$-armed case ($\Theta(\sqrt{KT})$). Beygelzimer et al. (AISTATS 2011) give Exp4.P with high-probability regret $O(\sqrt{KT\log(N/\delta)})$.
- **2014–2016.** Oracle-efficiency splits from information-theoretic optimality. Agarwal et al. (ICML 2014) attain $\tilde O(\sqrt{KT\log N})$ with $\tilde O(\sqrt{KT/\log N})$ oracle calls, but only for **i.i.d. contexts**. Hazan–Koren (STOC 2016) prove that for *adversarial* contexts, an oracle-efficient algorithm with $\sqrt{T}$ regret would break standard cryptographic assumptions.
- **2016.** Seldin and Lugosi (EWRL 2016) exhibit the first lower bound exceeding $\sqrt{KT}$: $\Omega(\sqrt{KT\log N/\log K})$, opening the $\sqrt{\log K}$ gap and conjecturing their bound is tight.
- **2016–2021.** Rakhlin–Sridharan (BISTRO) and Syrgkanis–Krishnamurthy–Schapire obtain $\tilde O(T^{2/3})$ oracle-efficient regret in transductive/adversarial context models; Foster–Rakhlin (ICML 2020) give optimal regression-oracle rates but under realizability and stochastic contexts.
- **2023–2026.** Log-factor-tight analyses for feedback graphs (Eldowa, Esposito, Cesa-Bianchi et al., NeurIPS 2023) supply the closest available technology for shaving the $\sqrt{\log K}$, since expert advice is a graph-feedback problem in disguise.

## 4. Partial Results / Verified Cases

- **$N=K$ (no contexts):** closed. $\mathcal{R}^\star = \Theta(\sqrt{KT})$; Tsallis-INF with $\alpha=1/2$ gives $2\sqrt{KT}$, matching the constant of the $\sqrt{KT}$ lower bound up to a small factor (Zimmert–Seldin, JMLR 2021).
- **$\log N \asymp \log K$ (i.e. $N \le K^{O(1)}$):** the two bounds coincide up to constants, so $\mathcal{R}^\star = \Theta(\sqrt{KT\log N})$ is settled.
- **Product classes $\Pi = [K]^{[m]}$ over $m$ disjoint contexts:** $\mathcal{R}^\star = \Theta(\sqrt{KTm}) = \Theta(\sqrt{KT\log N/\log K})$ — the conjectured rate is *achieved*, by running $m$ independent Exp3 instances (Section 10).
- **Full-information analogue:** $\Theta(\sqrt{T\log N})$ exactly (Cesa-Bianchi–Lugosi 2006), with no $\log K$ anomaly; the gap is specific to bandit feedback.
- **i.i.d. contexts, adversarial or stochastic losses with realizable regression class:** $\tilde\Theta(\sqrt{KT\log|\mathcal{F}|})$ via SquareCB (Foster–Rakhlin 2020).
- **Bandit multiclass ($\ell_t \in \{0,1\}^K$ induced by a label):** learnability characterized by a bandit Littlestone dimension (Daniely–Helbertal, COLT 2013; Raman–Subedi–Raman–Tewari, ALT 2023), with rates tight up to $\log K$ and $\log T$ factors.
- **$T \lesssim \log N / K$ (small horizon):** trivial linear regret $\Theta(T)$; both bounds degenerate.

## 5. Principal Obstacles

- **The variance term is bounded worst-case, not structurally.** Exp4's second-order term $\mathbb{E}\sum_\pi q_t(\pi)\hat y_t(\pi)^2 \le K$ is attained only if $q_t$ spreads uniformly over arms *and* the policies disagree maximally. Any improvement needs a bound coupling $\log N$ to the *achievable* disagreement pattern of $\Pi$ — a combinatorial quantity for which no potential function is known.
- **Lower bounds cannot exceed information-theoretic budget.** The KL-decomposition argument can only charge the learner for arms actually pulled; with $N$ experts, at most $\log_2 N$ bits per round can be extracted, and any construction forcing $\sqrt{KT\log N}$ must make the experts simultaneously informative and indistinguishable. Seldin–Lugosi's construction saturates at $\log N/\log K$ "effective independent bandits", and every known family of hard instances decomposes similarly.
- **Sequential vs. i.i.d. uniform convergence.** For infinite $\Pi$, adversarial contexts kill VC-based covering: the empirical process is a martingale process, so only sequential Rademacher / Littlestone quantities apply, and these can be infinite for finite-VC classes (e.g. thresholds on $[0,1]$: $\mathrm{VC}=1$, $\mathrm{Ldim}=\infty$).
- **Computational barrier.** Hazan–Koren show adversarial-context oracle-efficiency at $\sqrt{T}$ implies breaking PAC-learnability barriers, so the statistical and algorithmic questions cannot be attacked together by the reductions that succeeded in the i.i.d. case.
- **Log-barrier / OMD alternatives do not help.** Tsallis and log-barrier regularizers, which removed $\log K$ in the $K$-armed case, are defined over $\Delta([K])$; lifting them to $\Delta(\Pi)$ reintroduces an $N$-dependent range in the local norm, giving $\mathrm{poly}(N)$ rather than $\log N$.

## 6. The Gap

The entire open region is $K \ll N \ll \infty$ with $\log N \gg \log K$. There the proven interval is
$$\Big[\,c\sqrt{KT\log N/\log K}\;,\;\sqrt{2KT\log N}\,\Big],$$
a multiplicative gap of exactly $\Theta(\sqrt{\log K})$. Crossing it requires **one** of:

1. an algorithm whose second-order term is $O(K/\log K)$ in an amortized sense for every $\Pi$ — equivalently, an exploration distribution $p_t$ whose induced variance adapts to the "effective number of distinguishable arms" of $\Pi$ at $x_t$; or
2. a class $\Pi$ of size $N$ on which no algorithm can decompose the instance into $\log N/\log K$ independent sub-bandits — a hard instance where the experts overlap in a way that defeats the divergence-decomposition ceiling.

For infinite classes, the gap is between $\sqrt{KTd}$ and $\sqrt{KTd\log T}$: the $\log T$ comes from the discretization scale of the sequential cover, and no chaining argument is known that survives importance weighting.

## 7. Current Research (as of June 2026)

- **Feedback-graph transfer.** The Milan/UCL line (Cesa-Bianchi, Eldowa, Esposito, Colomboni) obtained the exact $\log$-factor dependence for graph-feedback bandits; bandits with expert advice is the "clique cover" instance of that theory, and adapting their FTRL analyses to $\Delta(\Pi)$ is the most active route to the $\sqrt{\log K}$. *(frontier — verify)*
- **Yandex/Copenhagen (Seldin, Zimmert) and INRIA groups** continue on best-of-both-worlds Tsallis-INF extensions to expert advice, where the conjectured $\sqrt{KT\log N/\log K}$ would follow from a suitable local-norm bound. *(frontier — verify)*
- **Microsoft Research NY / Cornell (Foster, Krishnamurthy, Rakhlin, Simchi-Levi)** push the Decision–Estimation Coefficient framework; the DEC gives matching upper/lower bounds for interactive decision making but currently loses $\log$ factors precisely in the adversarial-context regime.
- **Littlestone-dimension characterizations** for bandit multiclass and partial feedback (Tewari's group at Michigan; Hanneke and collaborators) aim at the infinite-class version.
- Reported preprints claiming to close the $\sqrt{\log K}$ for structured $\Pi$ (tree policies, sparse classes) should be treated as *(frontier — verify)*.

## 8. Future Work

- Design an FTRL scheme on $\Delta(\Pi)$ with a hybrid regularizer: negative entropy in the policy coordinates (to pay $\log N$) plus a Tsallis $\tfrac12$-entropy in the induced arm marginals (to pay $\sqrt{K}$ instead of $\sqrt{K\log K}$). The obstruction is that the arm marginal is a linear image of $q_t$, so the two potentials do not compose additively.
- Develop lower bounds via *composite* hypothesis classes rather than product classes — e.g. random codes on $[K]^{\mathcal{X}}$ with prescribed pairwise Hamming distance — and compute whether the KL budget permits $\sqrt{KT\log N}$.
- Settle the infinite-class rate for Littlestone dimension $d$: does adaptive chaining for sequential Rademacher complexity survive importance weighting with $1/p_t(a) \le K/\gamma$ clipping?
- Determine whether the $\sqrt{\log K}$ gap is *algorithmic* or *information-theoretic* by resolving the smallest open case $K=2$, $N=2^m$ exactly, where $\log K = 1$ and both bounds read $\Theta(\sqrt{Tm})$ — a positive resolution here would rule out one family of hard instances.
- Extend to non-oblivious adversaries and to high-probability bounds, where the Exp4.P analysis loses an extra $\log N$.

## 9. Key References

- **[Foundational]** P. Auer, N. Cesa-Bianchi, Y. Freund, R. E. Schapire. *The Nonstochastic Multiarmed Bandit Problem.* SIAM Journal on Computing 32(1):48–77, 2002.
- **[Foundational]** N. Cesa-Bianchi, G. Lugosi. *Prediction, Learning, and Games.* Cambridge University Press, 2006.
- **[Lower bound]** Y. Seldin, G. Lugosi. *A lower bound for multi-armed bandits with expert advice.* European Workshop on Reinforcement Learning (EWRL), 2016.
- **[Minimax, K-armed]** J.-Y. Audibert, S. Bubeck. *Minimax Policies for Adversarial and Stochastic Bandits.* COLT, 2009.
- **[SOTA]** J. Zimmert, Y. Seldin. *Tsallis-INF: An Optimal Algorithm for Stochastic and Adversarial Bandits.* Journal of Machine Learning Research 22(28):1–49, 2021.
- **[High probability]** A. Beygelzimer, J. Langford, L. Li, L. Reyzin, R. E. Schapire. *Contextual Bandit Algorithms with Supervised Learning Guarantees.* AISTATS, 2011.
- **[Oracle efficiency, i.i.d.]** A. Agarwal, D. Hsu, S. Kale, J. Langford, L. Li, R. E. Schapire. *Taming the Monster: A Fast and Simple Algorithm for Contextual Bandits.* ICML, 2014.
- **[Computational barrier]** E. Hazan, T. Koren. *The Computational Power of Optimization in Online Learning.* STOC, 2016.
- **[Adversarial contexts, $T^{2/3}$]** V. Syrgkanis, A. Krishnamurthy, R. E. Schapire. *Efficient Algorithms for Adversarial Contextual Learning.* ICML, 2016.
- **[Regression oracles]** D. J. Foster, A. Rakhlin. *Beyond UCB: Optimal and Efficient Contextual Bandits with Regression Oracles.* ICML, 2020.
- **[Sequential complexity]** A. Rakhlin, K. Sridharan, A. Tewari. *Sequential complexities and uniform martingale laws of large numbers.* Probability Theory and Related Fields 161:111–153, 2015.
- **[Feedback graphs, log factors]** K. Eldowa, E. Esposito, T. Cesarini, N. Cesa-Bianchi. *On the Minimax Regret for Online Learning with Feedback Graphs.* NeurIPS, 2023.
- **[Bandit multiclass]** A. Daniely, T. Helbertal. *The Price of Bandit Information in Multiclass Online Classification.* COLT, 2013.
- **[Survey / textbook]** T. Lattimore, C. Szepesvári. *Bandit Algorithms.* Cambridge University Press, 2020 (Chapter 18, Exp4; Chapter 15, minimax lower bounds).

## 10. Worked Example / Concrete Special Case

**Setup.** Let $\mathcal{X}=[m]$ with each context appearing exactly $T/m$ times, and let $\Pi = [K]^{[m]}$ be *all* maps from context to arm, so $N = K^m$ and $\log N = m\log K$.

**Exp4's bound.** Plugging in,
$$\mathcal{R}_{\mathrm{Exp4}} \le \sqrt{2KT\log N} = \sqrt{2KTm\log K}.$$

**A better algorithm.** Because $\Pi$ is a product class, the problem splits: run an independent Exp3 instance $\mathcal{A}_j$ on each context $j \in [m]$, each seeing $T/m$ rounds of a $K$-armed adversarial bandit. The comparator also splits, $\min_{\pi\in\Pi}L_T(\pi) = \sum_{j=1}^m \min_{a\in[K]} \sum_{t: x_t=j}\ell_t(a)$, so regret is additive:
$$\mathcal{R}_T = \sum_{j=1}^m \mathcal{R}^{(j)}_{T/m} \le m \cdot 2\sqrt{K\,\tfrac{T}{m}} = 2\sqrt{KTm}.$$
Using the minimax-optimal $\sqrt{KT'}$ rate per instance (Audibert–Bubeck) rather than Exp3's $\sqrt{2KT'\log K}$ is what removes the $\log K$.

**Matching lower bound.** Each sub-instance is a genuine $K$-armed adversarial bandit over $T/m$ rounds, so $\mathcal{R}^{(j)} \ge \tfrac{1}{27}\sqrt{K T/m}$, and independence across contexts gives
$$\mathcal{R}^\star \;\ge\; \tfrac{1}{27} m\sqrt{KT/m} \;=\; \tfrac{1}{27}\sqrt{KTm} \;=\; \tfrac{1}{27}\sqrt{\frac{KT\log N}{\log K}}.$$

**Numbers.** Take $K = 1024$, $m = 10$, $T = 10^7$. Then $N = 2^{100}$, $\log N \approx 69.3$, $\log K \approx 6.93$. Exp4 promises $\sqrt{2\cdot 1024 \cdot 10^7 \cdot 69.3} \approx 1.19\times 10^6$; the decomposition achieves $2\sqrt{1024\cdot 10^7\cdot 10} \approx 6.4\times 10^5$ and the lower bound is $\approx 1.2\times 10^4$ — with the conjectured truth at $\Theta(\sqrt{KTm}) \approx 3.2\times10^5$. The Exp4/optimal ratio is $\sqrt{\log K}\approx 2.6$.

**Why this does not settle the conjecture.** The decomposition used that $\Pi$ is a full product, so that no policy couples two contexts. For a general $\Pi$ of the same cardinality — say a random subset of $[K]^{[m']}$ with $m' \gg m$ — the comparator does not split, the $m$ sub-bandits share exploration budget, and no known potential function reproduces the $\sqrt{KTm}$ accounting. Whether such coupling can push regret up to $\sqrt{KT\log N}$, or whether every class admits an implicit decomposition, is exactly the open question.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*