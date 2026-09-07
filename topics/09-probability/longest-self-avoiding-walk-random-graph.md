---
id: 09-probability/longest-self-avoiding-walk-random-graph
title: "Longest Self-Avoiding Walk on Sparse Random Graphs"
topic: 09-probability
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Longest Self-Avoiding Walk on Sparse Random Graphs

> **Topic:** Probability & Stochastic Processes · **ID:** `09-probability/longest-self-avoiding-walk-random-graph` · **Status:** open

## 1. Problem Statement / Conjecture

A *self-avoiding walk* (SAW) on a graph $G$ is a walk that visits no vertex twice, i.e. a path. Let

$$L(G) \;=\; \max\{\,k : G \text{ contains a path with } k \text{ vertices}\,\}, \qquad C(G) \;=\; \text{circumference of } G .$$

Take $G \sim G(n, c/n)$, the Erdős–Rényi graph with $c > 1$ fixed. It is classical that $L(G) = \Theta(n)$ whp. The problem is to determine the constant.

**Conjecture (scaling limit and its formula).** There is a function $f : (1,\infty) \to (0,1)$, real-analytic on $(1,\infty)$, such that

$$\frac{L(G(n,c/n))}{n} \;\xrightarrow[n\to\infty]{\mathbb{P}}\; f(c) \qquad \text{for every } c > 1,$$

with the same limit for $C(G)/n$ up to the degree-$1$ correction, and $f$ is given by the replica-symmetry-breaking (cavity) fixed-point equations for the maximum-path problem on the Poisson Galton–Watson tree.

**Sub-conjecture (critical scaling).** Writing $c = 1+\varepsilon$ with $\varepsilon \to 0$,

$$f(1+\varepsilon) \;=\; (\kappa + o(1))\,\varepsilon^{2}, \qquad \kappa \in (0,\infty) \text{ a universal constant},$$

i.e. the $\Theta(\varepsilon^2 n)$ order is known and the constant $\kappa$ is not.

A complete resolution means: (i) proving the limit exists for *all* $c>1$ (not merely large $c$), (ii) identifying $f$ in closed or variational form, and (iii) computing $\kappa$. A disproof would exhibit non-convergence, a non-analytic point of $f$, or a formula contradicting the cavity prediction.

## 2. Mathematical Foundations

**Model.** $G(n,p)$ has vertex set $[n]$ and each of the $\binom{n}{2}$ edges present independently with probability $p = c/n$. Degrees converge to $\mathrm{Poisson}(c)$; the local weak limit is the Poisson Galton–Watson tree $\mathrm{PGW}(c)$ (Benjamini–Schramm convergence).

**Giant component.** Let $\theta = \theta(c)$ be the largest root of

$$\theta \;=\; 1 - e^{-c\theta}.$$

Then $|C_{\max}|/n \to \theta$ whp; all other components have size $O(\log n)$.

**$k$-core / $2$-core.** Let $\mu = \mu(c)$ solve $\mu = c\,(1-e^{-\mu})$, $\mu>0$. The $2$-core of $G(n,c/n)$ has

$$\frac{|{\rm core}_2|}{n} \;\longrightarrow\; \gamma_2(c) := 1 - (1+\mu)e^{-\mu}, \qquad \frac{e({\rm core}_2)}{n} \to \tfrac{\mu^2}{2c}.$$

**Elementary upper bounds.** A path uses a vertex of degree $\le 1$ only as an endpoint, and a cycle not at all. Hence whp

$$L(G) \;\le\; \big(1 - (1+c)e^{-c} + o(1)\big)n, \qquad C(G) \;\le\; \big(\gamma_2(c)+o(1)\big)n,$$

and $C(G) \le L(G) \le C(G) + 2$ up to lower-order corrections on the giant.

**Subadditivity.** $L$ is not additive across a vertex split, so the standard superadditive-ergodic route used for SAW on $\mathbb{Z}^d$ (where $c_{n+m} \le c_n c_m$ gives the connective constant $\mu = \lim c_n^{1/n}$, Hammersley–Welsh) has no direct analogue: on $G(n,c/n)$ the object is a *maximum*, not a *count*, and the graph sequence is not nested.

**Variational (cavity) formulation.** The longest path is the optimum of a constraint-satisfaction problem: assign $x_e \in \{0,1\}$ to edges, require $\sum_{e \ni v} x_e \le 2$ for all $v$ and global connectivity/acyclicity of the selected set. Dropping the global constraint gives the *maximum $2$-matching* relaxation, whose value is computable by belief propagation on $\mathrm{PGW}(c)$ and gives an upper bound $f(c) \le f_{2\text{-match}}(c)$. The gap between the relaxation and the true optimum is exactly the cost of contracting short cycles into one long one.

**Local limit / Aldous objective method.** For maximum matchings, $\lim \nu(G_n)/n$ equals a functional of $\mathrm{PGW}(c)$ (Karp–Sipser; Bordenave–Lelarge–Salez). For longest paths no such local formula is proved, because the objective is not local.

## 3. History & State of the Art (SOTA)

- **1976–1981.** Erdős asked for the order of the longest path in sparse random graphs. **Ajtai, Komlós and Szemerédi** (*The longest path in a random graph*, Combinatorica 1, 1981) proved that for $c>1$ the longest path has $\Omega_c(n)$ vertices — the first linear lower bound, via a depth-first-search / rotation argument.
- **1982.** **Bollobás** (*Long paths in sparse random graphs*, Combinatorica 2) sharpened this to $L \ge (1 - \alpha(c))n$ with $\alpha(c) \to 0$ as $c \to \infty$.
- **1986.** **Frieze** (*On large matchings and cycles in sparse random graphs*, Discrete Math. 59) proved the benchmark bound: whp
  $$C(G(n,c/n)) \;\ge\; \big(1 - (1+\epsilon(c))\,c\,e^{-c}\big)n, \qquad \epsilon(c)\to 0 \text{ as } c \to \infty,$$
  matching the trivial upper bound $1-(1+c)e^{-c}$ to leading exponential order. This is still the sharpest general statement for large $c$ in elementary form.
- **1983–1994.** For denser or regular models the answer is complete: $G(n,p)$ is Hamiltonian exactly at the moment the minimum degree reaches $2$ (Komlós–Szemerédi 1983; Bollobás 1984), and random $d$-regular graphs are Hamiltonian whp for every $d \ge 3$ (Robinson–Wormald 1992, 1994), so $f \equiv 1$ there.
- **1991.** **Łuczak** (*Cycles in a random graph near the critical point*, RSA 2) established the critical-window behaviour; combined with the giant-component anatomy this gives circumference $\Theta(\varepsilon^2 n)$ at $c = 1+\varepsilon$.
- **2011.** **Ding, Lubetzky and Peres** (*Anatomy of a young giant component in the random graph*, RSA 39) gave the contiguous kernel description of the giant for $c = 1+\varepsilon$: $2$-core of size $\sim 2\varepsilon^2 n$, kernel of $\sim \tfrac{4}{3}\varepsilon^3 n$ vertices, all of degree $3$ whp — reducing the constant $\kappa$ to a question about longest cycles in a random cubic multigraph with weighted edges.
- **2013.** **Kemkes and Wormald** improved the upper bound on the circumference of the supercritical random graph by small-subgraph conditioning.
- **2021.** **Anastos and Frieze** (*A scaling limit for the length of the longest cycle in a sparse random graph*, JCTB 148) proved existence of the limit $C/n \to f(c)$ for $c$ above a large absolute constant, with $f$ given by a computable expansion and $1-f(c) = \Theta(ce^{-c})$. This is the current SOTA and the first proof that a limit exists at all.

## 4. Partial Results / Verified Cases

- **$c = \infty$ regime (dense / minimum-degree threshold).** $p \ge (\log n + \log\log n + \omega)/n$: Hamiltonian whp, $f = 1$ (Komlós–Szemerédi 1983; Bollobás 1984). Complete.
- **Random $d$-regular, $d \ge 3$:** Hamiltonian whp, $L = n$ (Robinson–Wormald). Complete. Random $2$-regular: $L$ equals the largest cycle, distributed by the Poisson–Dirichlet(1) law, mean $\approx 0.6243\,n$ (Golomb–Dickman constant).
- **Large constant $c$:** limit $f(c)$ exists and is computable to arbitrary accuracy (Anastos–Frieze 2021), for $c \ge c_0$ with $c_0$ a large explicit constant; subsequent work has pushed $c_0$ down into the low tens *(frontier — verify)*.
- **Asymptotics as $c \to \infty$:** $1 - f(c) = (1+o(1))\,c\,e^{-c}$ — matching upper and lower bounds (Frieze 1986 plus the degree count).
- **Critical window and barely supercritical:** for $c = 1+\varepsilon$, $\varepsilon \to 0$ with $\varepsilon^3 n \to \infty$, $C = \Theta(\varepsilon^2 n)$ (Łuczak 1991; Ding–Lubetzky–Peres 2011). Inside the window $p = (1+\lambda n^{-1/3})/n$, $C = \Theta_P(n^{1/3})$.
- **Digraphs:** Krivelevich, Lubetzky and Sudakov (*Longest cycles in sparse random digraphs*, RSA 43, 2013) proved the analogous $(1-O(ce^{-c}))n$ bound for $D(n,c/n)$.
- **Small $n$:** exhaustive computation of $L$ is feasible only to $n \approx 40$–$50$ (longest path is NP-hard); Monte Carlo estimates of $f(c)$ for $c \in [1.2, 6]$ exist in the statistical-physics literature but carry no rigorous error bars.

## 5. Principal Obstacles

- **Non-locality of the objective.** Maximum matchings, independent sets and $k$-cores admit local (Benjamini–Schramm) limits, so the objective method and belief propagation apply. A longest path is a *global* object: no finite-radius neighbourhood statistic certifies it. The Aldous–Steele objective method therefore does not transfer.
- **NP-hardness and the algorithmic barrier.** Longest path is NP-hard; all rigorous lower bounds are constructive (DFS, rotation–extension, Pósa rotations, colour coding) and hence inherit the limits of polynomial-time algorithms on sparse instances. There is no known certificate scheme for near-optimal paths that is tight in the regime $1 < c < 20$.
- **Failure of the $2$-matching relaxation.** The relaxation is exactly solvable but strictly loose: its optimum decomposes into many short cycles, and patching them into one path costs an unknown $\Theta(n)$ number of vertices. Bounding the patching cost requires control on the joint cycle-length spectrum, which is not available.
- **No subadditivity / no connective constant.** For SAW on $\mathbb{Z}^d$ the whole theory rests on $c_{n+m}\le c_n c_m$. On $G(n,c/n)$ the graph changes with $n$, the maximum is not submultiplicative, and Azuma-type concentration gives concentration around the mean without identifying it.
- **Replica symmetry breaking.** The cavity prediction for the longest path is believed to require one-step RSB (the space of near-optimal paths shatters into exponentially many clusters). Rigorous RSB technology — Guerra interpolation, Aizenman–Sims–Starr — is developed for spin glasses with soft constraints; the hard degree-$\le 2$ plus connectivity constraint has no interpolation scheme.
- **Second-moment blow-up.** Counting paths of length $an$ has $\mathbb{E}[X^2]/(\mathbb{E}X)^2$ exponentially large, because two long paths overlapping in many segments dominate. Small-subgraph conditioning fixes this only in the regular case.

## 6. The Gap

Proven: $C/n \to f(c)$ exists for $c \ge c_0$ (large), with $1-f(c) \sim ce^{-c}$; and $C = \Theta(\varepsilon^2 n)$ at $c = 1+\varepsilon$.

Not proven: (i) existence of the limit for $1 < c < c_0$ — no argument currently rules out that $L/n$ oscillates or has different $\liminf$/$\limsup$ in the moderate regime; (ii) any closed form for $f$ at moderate $c$, e.g. $f(2)$ is known only to lie in a wide interval; (iii) the constant $\kappa$ in $f(1+\varepsilon) \sim \kappa\varepsilon^2$.

The precise step to cross: convert the local (PGW-tree) cavity fixed point into a rigorous upper bound on $L$ by exhibiting an interpolation or a certifiable dual object for a global connectivity constraint. Equivalently, prove that the loss from merging the optimal $2$-matching's cycles into a single path is asymptotically given by the RSB complexity functional.

## 7. Current Research (as of June 2026)

- **Anastos (Freie Universität Berlin) and Frieze (Carnegie Mellon)** continue to lower the threshold $c_0$ at which the scaling limit is proved, via multi-round rotation–extension coupled to a fluid-limit analysis of a greedy path-growing process *(frontier — verify)*.
- **Krivelevich's group (Tel Aviv)** develops DFS-based arguments giving explicit, non-asymptotic constants for $L$ at small $c$, and extends the analysis to random subgraphs of expanders and of graphs with large minimum degree.
- **Statistical-physics community (Semerjian, Monasson, Marinari, Zdeborová/Ricci-Tersenghi).** Cavity computations for circuits and long loops in sparse random graphs give numerical predictions for $f(c)$; the 1RSB prediction for the longest cycle is available numerically but unpublished in a form matched to the rigorous bounds *(frontier — verify)*.
- **Kernel-based attack on $\kappa$.** Following Ding–Lubetzky–Peres, the barely-supercritical constant reduces to the circumference of a random cubic multigraph whose edges carry i.i.d. geometric path lengths; groups in Cambridge and Warwick have been analysing this weighted-Hamiltonicity question *(frontier — verify)*.
- **Algorithmic/lower-bound side.** Colour-coding and treewidth-based exact solvers now certify longest paths on sparse instances up to $n \approx 10^3$ for $c \le 3$, sharpening numerics for $f(c)$.

## 8. Future Work

- Prove existence of $\lim L/n$ for all $c>1$ by a sub-/super-additivity substitute — e.g. an interpolation between $G(n,c/n)$ and $G(n_1,\cdot)\cup G(n_2,\cdot)$ with a controlled error, as done by Bayati–Gamarnik–Tetali for independent sets and matchings. This is the most likely next theorem.
- Extend the Bordenave–Lelarge–Salez local-limit framework from matchings to $2$-matchings, then quantify the cycle-merging deficit.
- Determine $\kappa$ exactly via the cubic kernel with geometric edge weights; a matching upper bound would settle the barely-supercritical case.
- Transfer results to the configuration model with general degree distribution $D$: conjecturally $f$ depends on $D$ only through $\mathbb{P}(D\le1)$ and the $2$-core profile.
- Establish concentration beyond Azuma: is $L$ concentrated on an interval of width $O(n^{1/2})$, or $O(n^{1/3})$ with Tracy–Widom-type fluctuations?
- Study the SAW *measure* (uniform long path) rather than the extremal length: mixing, endpoint displacement, and whether the uniform long path is delocalised over the giant.

## 9. Key References

- **[Foundational]** M. Ajtai, J. Komlós, E. Szemerédi. *The longest path in a random graph.* Combinatorica 1(1), 1–12, 1981.
- **[Foundational]** B. Bollobás. *Long paths in sparse random graphs.* Combinatorica 2(3), 223–228, 1982.
- **[Foundational]** A. M. Frieze. *On large matchings and cycles in sparse random graphs.* Discrete Mathematics 59(3), 243–256, 1986.
- **[Foundational]** J. Komlós, E. Szemerédi. *Limit distribution for the existence of Hamiltonian cycles in a random graph.* Discrete Mathematics 43(1), 55–63, 1983.
- **[Foundational]** T. Łuczak. *Cycles in a random graph near the critical point.* Random Structures & Algorithms 2(4), 421–439, 1991.
- **[SOTA / Recent]** M. Anastos, A. M. Frieze. *A scaling limit for the length of the longest cycle in a sparse random graph.* Journal of Combinatorial Theory, Series B 148, 184–208, 2021.
- **[SOTA / Recent]** J. Ding, E. Lubetzky, Y. Peres. *Anatomy of a young giant component in the random graph.* Random Structures & Algorithms 39(2), 139–178, 2011.
- **[SOTA / Recent]** G. Kemkes, N. Wormald. *An improved upper bound on the length of the longest cycle of a supercritical random graph.* SIAM Journal on Discrete Mathematics 27(1), 342–362, 2013.
- **[SOTA / Recent]** M. Krivelevich, E. Lubetzky, B. Sudakov. *Longest cycles in sparse random digraphs.* Random Structures & Algorithms 43(1), 1–15, 2013.
- **[Related]** R. W. Robinson, N. C. Wormald. *Almost all cubic graphs are Hamiltonian.* Random Structures & Algorithms 3(2), 117–125, 1992; *Almost all regular graphs are Hamiltonian.* RSA 5(2), 363–374, 1994.
- **[Related]** C. Bordenave, M. Lelarge, J. Salez. *Matchings on infinite graphs.* Probability Theory and Related Fields 157, 183–208, 2013.
- **[Related]** E. Marinari, G. Semerjian. *On the number of circuits in random graphs.* Journal of Statistical Mechanics: Theory and Experiment, P06019, 2006.
- **[Survey]** A. M. Frieze, M. Karoński. *Introduction to Random Graphs.* Cambridge University Press, 2016.
- **[Survey]** S. Janson, T. Łuczak, A. Ruciński. *Random Graphs.* Wiley, 2000.
- **[Survey]** A. M. Frieze. *Hamilton cycles in random graphs: a bibliography.* arXiv:1901.07139, 2019.
- **[Survey]** N. Madras, G. Slade. *The Self-Avoiding Walk.* Birkhäuser, 1993.

## 10. Worked Example / Concrete Special Case

**Case $c = 2$: how far apart are the bounds?**

*Giant component.* Solve $\theta = 1 - e^{-2\theta}$. Iterating from $\theta_0=0.8$: $1-e^{-1.6}=0.7981$, $1-e^{-1.5962}=0.7973$, converging to $\theta \approx 0.7968$. So the giant holds $\approx 79.7\%$ of vertices, and trivially $L \le 0.7968\,n$.

*Degree bound.* $\mathbb{P}(\mathrm{Poisson}(2) \le 1) = e^{-2}(1+2) = 3e^{-2} = 0.4060$. Every such vertex is excluded from any path except the two endpoints, so whp

$$L(G) \;\le\; (1 - 0.4060 + o(1))\,n \;=\; 0.5940\,n .$$

*$2$-core bound for cycles.* $\mu = c\theta = 1.5936$ (check: $2(1-e^{-1.5936}) = 2(1-0.2032) = 1.5936$ ✓). Then

$$\gamma_2(2) = 1 - (1+\mu)e^{-\mu} = 1 - 2.5936 \times 0.2032 = 0.4730,$$

so the circumference satisfies $C \le 0.4730\,n$ — a bound $0.121\,n$ stronger than the degree bound, and the sharpest simple upper bound available.

*Lower bound.* Frieze's theorem gives $C \ge (1 - (1+\epsilon(c))ce^{-c})n$; at $c=2$ this reads $1 - (1+\epsilon(2))\cdot 0.2707$, and $\epsilon(2)$ is not small, so the statement is vacuous here. Anastos–Frieze's scaling limit needs $c \ge c_0 \gg 2$. What survives at $c=2$ is only Ajtai–Komlós–Szemerédi's qualitative $L = \Omega(n)$ together with explicit DFS constants of order $0.1$–$0.2\,n$.

**Conclusion of the example.** At $c=2$ the true value $f(2)$ is pinned only to roughly $[0.2, 0.473]$ — a factor better than two of uncertainty in a completely explicit model. Contrast with the matching number, where Karp–Sipser gives the exact limit for every $c$:

$$\frac{\nu(G(n,c/n))}{n} \to 1 - \frac{\gamma_* + \gamma_{**} + \gamma_*\gamma_{**}}{2c}, \qquad \gamma_* = c e^{-\gamma_{**}},\ \gamma_{**} = c e^{-\gamma_*},$$

giving $\approx 0.3854$ at $c=2$. The contrast — an exact local formula for matchings, a factor-of-two window for paths — is precisely the non-locality obstacle of Section 5.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*