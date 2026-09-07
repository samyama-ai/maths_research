---
id: 09-probability/cutoff-for-the-simple-random-walk-on-random-regular-graphs
title: "Cutoff for the Simple Random Walk on Random Regular Graphs"
topic: 09-probability
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

id: 09-probability/cutoff-for-the-simple-random-walk-on-random-regular-graphs
title: "Cutoff for the Simple Random Walk on Random Regular Graphs"
topic: 09-probability
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
```

# Cutoff for the Simple Random Walk on Random Regular Graphs

> **Topic:** Probability & Stochastic Processes · **ID:** `09-probability/cutoff-for-the-simple-random-walk-on-random-regular-graphs` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

The problem asks whether the Simple Random Walk (SRW) on a sequence of random $d$-regular graphs exhibits the **cutoff phenomenon**—an abrupt transition in the Total Variation (TV) distance from the walk's distribution to the stationary distribution—and, if so, to determine the exact asymptotic cutoff time and the width of the cutoff window. 

Specifically, let $\mathcal{G}(n,d)$ denote the probability space of uniformly chosen random $d$-regular graphs on $n$ vertices (where $n d$ is even). Let $P_n$ be the transition matrix of the SRW on a graph $G_n \sim \mathcal{G}(n,d)$, and let $t_{\text{mix}}^{(n)}(\varepsilon)$ denote its $\varepsilon$-mixing time. For $d \ge 3$, the conjecture (now a proven theorem) states that with high probability (w.h.p.) as $n \to \infty$, the SRW exhibits cutoff at time 
$$ t_{\text{cutoff}} = \frac{d}{d-2} \log_{d-1} n $$
meaning that for any $\varepsilon \in (0,1)$,
$$ \lim_{n \to \infty} \frac{t_{\text{mix}}^{(n)}(\varepsilon)}{t_{\text{cutoff}}} = 1. $$
Furthermore, the problem requires establishing the scaling window (or cutoff window) $w_n$, such that the drop in TV distance from $1-\varepsilon$ to $\varepsilon$ occurs within an interval of time $t_{\text{cutoff}} \pm O(w_n)$. The full resolution requires proving $w_n = \sqrt{\log n}$.

## 2. Mathematical Foundations

Let $G = (V,E)$ be a connected, non-bipartite $d$-regular graph on $n = |V|$ vertices. The **Simple Random Walk** on $G$ is a discrete-time Markov chain $(X_t)_{t \ge 0}$ on state space $V$ with transition matrix $P$ defined by $P(x,y) = \frac{1}{d}$ if $\{x,y\} \in E$, and $0$ otherwise. 

Because $G$ is $d$-regular, the unique stationary distribution $\pi$ is uniform: $\pi(x) = \frac{1}{n}$ for all $x \in V$. The convergence of the SRW to equilibrium is measured via the **Total Variation (TV) distance**. For distributions $\mu, \nu$ on $V$, the TV distance is:
$$ \|\mu - \nu\|_{\text{TV}} = \max_{A \subset V} |\mu(A) - \nu(A)| = \frac{1}{2} \sum_{x \in V} |\mu(x) - \nu(x)|. $$
Let $P^t(x, \cdot)$ denote the distribution of the walk at time $t$ starting from $X_0 = x$. The worst-case TV distance at time $t$ is:
$$ d_{\text{TV}}(t) = \max_{x \in V} \|P^t(x, \cdot) - \pi\|_{\text{TV}}. $$
The **$\varepsilon$-mixing time** is defined as:
$$ t_{\text{mix}}(\varepsilon) = \min \{ t \ge 0 : d_{\text{TV}}(t) \le \varepsilon \}. $$

A sequence of Markov chains $(X_t^{(n)})_{t \ge 0}$ exhibits a **cutoff** if, for every $\varepsilon \in (0, 1)$,
$$ \lim_{n \to \infty} \frac{t_{\text{mix}}^{(n)}(\varepsilon)}{t_{\text{mix}}^{(n)}(1-\varepsilon)} = 1. $$
The sequence is said to have a **cutoff window** of order $w_n = o(t_{\text{mix}}^{(n)})$ if, for any $\varepsilon \in (0, 1)$, there exists a constant $C_\varepsilon > 0$ such that:
$$ t_{\text{mix}}^{(n)}(\varepsilon) - t_{\text{mix}}^{(n)}(1-\varepsilon) \le C_\varepsilon w_n. $$

To formalize the random graph ensemble $\mathcal{G}(n,d)$, mathematicians utilize the **Configuration Model** (Bollobás, 1980): each of the $n$ vertices is assigned $d$ half-edges, and a uniform random perfect matching is chosen among the $nd$ half-edges. Conditional on the resulting multigraph containing no self-loops or multiple edges, it is uniformly distributed over the space of simple $d$-regular graphs.

## 3. History & State of the Art (SOTA)

The concept of a cutoff was introduced in the 1980s by David Aldous and Persi Diaconis in the context of card shuffling (e.g., the riffle shuffle). Throughout the 1990s and 2000s, proving cutoff for random walks on graphs became a major focus, as cutoff represents the optimal structural phenomenon of discrete Markov chains.

For random $d$-regular graphs, which are known to be near-optimal expanders with high probability, proving cutoff was historically arduous. A significant milestone was Friedman's proof (2008) of Alon's Second Eigenvalue Conjecture. Friedman showed that for $G \sim \mathcal{G}(n,d)$, the second largest absolute eigenvalue of the transition matrix, $\lambda$, satisfies:
$$ \lambda \le \frac{2\sqrt{d-1}}{d} + o(1) $$
w.h.p. Graphs strictly bounded by $\frac{2\sqrt{d-1}}{d}$ are Ramanujan graphs. While Friedman's result established the optimal spectral gap, standard spectral bounds on mixing times were insufficiently sharp to prove cutoff. 

The breakthrough resolution was achieved by Eyal Lubetzky and Allan Sly in 2010 (published 2011/2012). They successfully proved that the SRW on $\mathcal{G}(n,d)$ exhibits cutoff at $t = \frac{d}{d-2} \log_{d-1} n$ with a window of $\Theta(\sqrt{\log n})$. Their approach bypassed spectral limitations by undertaking a multi-scale geometric analysis of the graph, tracking the exact entropic decay of the walk.

Since their breakthrough, researchers have expanded the SOTA to determine the exact universal profile function (which converges to a Gaussian error function) and extended the proof techniques to the non-backtracking random walk, which mixes strictly faster at time $\log_{d-1} n$.

## 4. Partial Results / Verified Cases

Prior to the full resolution, several restricted or alternative formulations of the problem were solved:
- **Spectral Upper Bounds:** Using Friedman's theorem, an $L^2$ bound (Poincaré inequality) immediately gave $t_{\text{mix}} = O(\log n)$. Specifically, $t_{\text{mix}} \le \frac{d}{d-2\sqrt{d-1}} \log_{d-1} n$, which captures the order but misses the exact constant.
- **Tree-like Lower Bounds:** The local structure of $\mathcal{G}(n,d)$ is a $d$-regular tree up to depth $\approx \frac{1}{2} \log_{d-1} n$. An entropy argument on this tree easily proved that $t_{\text{mix}} \ge \frac{d}{d-2} \log_{d-1} n$, establishing a rigorous lower bound.
- **Non-Backtracking Walk:** A random walk that is forbidden from traversing the edge it just arrived on (i.e., $X_{t+1} \neq X_{t-1}$). It was proven earlier that this walk lacks the "local stalling" of the SRW and exhibits cutoff at precisely $\log_{d-1} n$.
- **Bipartite Configurations:** If the chosen graph is bipartite, the SRW is periodic and does not converge to the uniform distribution. However, replacing the SRW with a lazy random walk (probability $1/2$ of remaining in place) resolved this issue, yielding a scaled cutoff time.

## 5. Principal Obstacles

The fundamental reason this problem remained unsolved for decades is the intrinsic inadequacy of **$L^2$ (spectral) techniques** to capture $L^1$ (Total Variation) concentration in expanders.

The standard bound linking TV distance to the spectral gap $\gamma = 1 - \lambda_{\max}$ relies on the Cauchy-Schwarz inequality:
$$ d_{\text{TV}}(t) \le \frac{1}{2} \sqrt{n \sum_{x} (P^t(x,y) - \pi(x))^2} = \frac{\sqrt{n}}{2} (1 - \gamma)^t. $$
For $G \sim \mathcal{G}(n,d)$, Friedman's theorem yields $\gamma \approx 1 - \frac{2\sqrt{d-1}}{d}$. To make the right-hand side of the inequality less than $\varepsilon$, one requires:
$$ t \ge \frac{\log n + 2 \log(1/(2\varepsilon))}{2 \gamma} \approx \frac{d}{2(d - 2\sqrt{d-1})} \log n. $$
This spectral upper bound is strictly greater than the true mixing time $\frac{d}{d-2} \log_{d-1} n$. The $L^2$ norm is overwhelmingly dominated by "worst-case" highly localized eigenvectors. The Total Variation distance, however, measures average mass transport and is unaffected by these localized $L^2$ pathologies once the walk escapes the immediate vicinity of its starting point. Thus, conventional algebraic graph theory inherently overestimates the mixing time, forcing mathematicians to adopt direct probabilistic tools to track the walker's path geometry.

## 6. The Gap

The "gap" that needed crossing was the divide between the geometric lower bound (derived from the volume expansion of balls in a tree) and the spectral upper bound (derived from eigenvalue analysis). 

The barrier was demonstrating that the random walk does not get localized or slowed down by the logarithmic-length cycles that inevitably appear beyond the tree-like neighborhood of the starting vertex. To close this gap, Lubetzky and Sly had to dynamically reveal the edges of the random graph (using the Configuration Model) simultaneously as the random walk explored the graph. This coupling prevented the walk's history from biasing the unrevealed portions of the graph, showing that the walk behaves like it is on an infinite tree until the very instant it completely uniformly covers the graph.

## 7. Current Research (as of June 2026)

With the baseline problem resolved, the active frontier has shifted to complex graph topologies and perturbed dynamical systems:
- **Erdős-Rényi and Sparse Graphs:** Examining cutoff on the giant component of the sparse Erdős-Rényi graph $G(n, p)$ where $p = c/n$. The variance in degree distribution heavily distorts the tree-like local structures. Results show a cutoff still occurs but at times dependent on the stationary measure biases.
- **Directed Regular Graphs:** Proving cutoff for the random directed walk on random directed graphs. Recent preprints are tackling the asymmetric spectrum of transition matrices where reversible Markov chain techniques fundamentally fail. `*(frontier — verify)*`
- **Cutoff Profile Universality:** Deep structural analysis into the shape of the cutoff window. While the profile for random regular graphs is asymptotically a Gaussian error function, research actively searches for graph sequences where the profile takes a fundamentally different continuous limit.
- **Interacting Particle Systems:** Studying the cutoff of the simple exclusion process and the Glauber dynamics for the Ising model on $\mathcal{G}(n,d)$. The spatial mixing is highly correlated, rendering the single-particle random walk techniques inadequate.

## 8. Future Work

Leading probabilists indicate several major open pathways stemming from this resolution:
1. **Deterministic Expanders:** Does the SRW exhibit cutoff on *all* deterministic sequence of Ramanujan graphs? Currently, cutoff is proven for random graphs, but explicit constructions of Ramanujan graphs (like the Lubotzky-Phillips-Sarnak construction) possess rigid algebraic cycles that could theoretically obstruct cutoff. This is one of the most significant open problems in spectral graph theory.
2. **Adversarial Initial States:** Investigating the precise variance of the mixing time based on the starting vertex. Does an adversary choosing a specific starting node in a pseudo-random graph sequence shift the cutoff time beyond the $O(\sqrt{\log n})$ window?
3. **Heavy-tailed degree distributions:** Extending the proof methodology to scale-free random graphs (e.g., Preferential Attachment models), where degrees follow a power law and the graph lacks uniform expansion.

## 9. Key References

- **[Foundational]** Aldous, D., & Diaconis, P. *Shuffling cards and stopping times.* The American Mathematical Monthly, 93(5), 333-348, 1986.
- **[Foundational]** Friedman, J. *A proof of Alon’s second eigenvalue conjecture and related problems.* Memoirs of the American Mathematical Society, 195(910), 2008.
- **[SOTA / Recent]** Lubetzky, E., & Sly, A. *Cutoff phenomena for random walks on random regular graphs.* Duke Mathematical Journal, 153(3), 475-510, 2010.
- **[SOTA / Recent]** Bordenave, C., Lelarge, M., & Massoulié, L. *Non-backtracking spectrum of random graphs: community detection and non-regular Ramanujan graphs.* IEEE 56th Annual Symposium on Foundations of Computer Science (FOCS), 2015.
- **[Survey]** Berestycki, N., Lubetzky, E., Peres, Y., & Sly, A. *Random walks on the giant component of the Erdős-Rényi graph.* Annals of Probability, 46(1), 143-161, 2018.

## 10. Worked Example / Concrete Special Case

To ground the cutoff time $t_{\text{cutoff}} = \frac{d}{d-2} \log_{d-1} n$, we can look at a simplified, concrete model: tracking the random walk's distance from its starting vertex on a perfect $d$-regular tree (the local geometry of $\mathcal{G}(n,d)$).

Consider $d = 3$. The asymptotic cutoff time formula gives:
$$ t_{\text{cutoff}} = \frac{3}{3-2} \log_{3-1} n = 3 \log_2 n. $$

Let's derive this heuristically. We want to know when the random walk has traversed far enough to have had the *possibility* of reaching all $n$ vertices. 
On a 3-regular tree, the number of vertices exactly at distance $r$ from the origin is $3 \cdot 2^{r-1}$ (for $r \ge 1$). The volume of a ball of radius $R$ is approximately:
$$ |B(R)| = 1 + \sum_{r=1}^{R} 3 \cdot 2^{r-1} = 1 + 3(2^R - 1). $$
For the ball to encompass the entire graph, we need $|B(R)| \approx n$. Thus,
$$ 3 \cdot 2^R \approx n \implies 2^R \approx \frac{n}{3} \implies R \approx \log_2 n. $$
Therefore, the graph has a diameter of roughly $\log_2 n$.

Now, let $X_t$ be the distance of the Simple Random Walk from the starting vertex on this tree. 
At any vertex (other than the root), there is $1$ edge leading back toward the root, and $2$ edges pointing outward. 
Because the walk chooses an edge uniformly at random (probability $1/3$ each), the distance $X_t$ behaves as a biased random walk on the non-negative integers $\mathbb{Z}_{\ge 0}$:
- $P(X_{t+1} = X_t + 1) = \frac{2}{3}$ (moves away from root)
- $P(X_{t+1} = X_t - 1) = \frac{1}{3}$ (moves toward root)

The expected change in distance (the "drift" or speed) per step is:
$$ \mathbb{E}[X_{t+1} - X_t] = (+1)\left(\frac{2}{3}\right) + (-1)\left(\frac{1}{3}\right) = \frac{1}{3}. $$
By the Law of Large Numbers, after $t$ steps, the walk is highly concentrated at a distance of:
$$ X_t \approx \frac{t}{3}. $$
To achieve mixing, the walk must reach the "boundary" of the graph, traversing a distance equal to the graph's radius $R \approx \log_2 n$. Equating the walk's expected distance to the radius gives the required time $t$:
$$ \frac{t}{3} = \log_2 n \implies t = 3 \log_2 n. $$
This elementary calculation perfectly yields the established cutoff time $\frac{d}{d-2}\log_{d-1}n$ for $d=3$. The proof of the Lubetzky-Sly theorem essentially demonstrates that this local tree-like expansion tightly dictates the global mixing time on the random regular graph.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*