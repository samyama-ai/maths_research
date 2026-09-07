---
id: 10-theoretical-cs/meyniel-conjecture
title: "Meyniel Conjecture"
topic: 10-theoretical-cs
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Meyniel Conjecture

> **Topic:** Theoretical Computer Science · **ID:** `10-theoretical-cs/meyniel-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

**Conjecture (Meyniel, 1985).** There is a constant $C$ such that every connected graph $G$ on $n$ vertices satisfies
$$c(G) \le C\sqrt{n},$$
where $c(G)$ is the *cop number* of $G$ — the least number of cops needed to catch a robber in the Nowakowski–Winkler–Quilliot pursuit game.

The conjecture is an asymptotic upper bound on the worst case over all connected graphs; it is not about any particular family. A proof requires exhibiting a cop strategy (or a non-constructive argument) using $O(\sqrt n)$ cops on **every** connected graph. A disproof requires an infinite family $G_1, G_2, \dots$ with $|V(G_i)| = n_i \to \infty$ and $c(G_i)/\sqrt{n_i} \to \infty$.

Two weakenings are also standard and also open:

- **Soft Meyniel:** $c(G) = O(n^{1-\varepsilon})$ for some fixed $\varepsilon > 0$.
- **Meyniel for a class $\mathcal{C}$:** $c(G) = O(\sqrt n)$ for all $G \in \mathcal{C}$.

The matching lower bound is known: incidence graphs of projective planes have $c(G) \sim \sqrt{n/2}$, so the exponent $1/2$ cannot be lowered.

## 2. Mathematical Foundations

**The game.** Let $G=(V,E)$ be finite, simple, connected. Fix $k \ge 1$. Player *cop* places $k$ tokens on vertices $c_1,\dots,c_k \in V$; player *robber* then places one token on $r \in V$. Play alternates, cops first. On a move each player may keep a token where it is or slide it along an edge; formally, positions move within the closed neighbourhood $N[v] = \{v\} \cup \{u : uv \in E\}$. Both players see the whole board (perfect information). The cops win if at some finite time $c_i = r$ for some $i$.

**Cop number.**
$$c(G) = \min\{\, k \in \mathbb{N} : k \text{ cops have a winning strategy on } G \,\}.$$
Since the state space $V^k \times V \times \{0,1\}$ is finite and the game is a reachability game, it is determined; $c(G) \le n$ always, and $c$ is well defined. For disconnected $G$, $c(G)=\sum_i c(G_i)$ over components, which is why Section 1 assumes connectivity.

**Retracts and cop-win graphs.** A vertex $u$ is *dominated* (a corner) if $N[u] \subseteq N[v]$ for some $v \ne u$. $G$ is *dismantlable* if repeatedly deleting corners reduces $G$ to a single vertex.

> **Theorem (Nowakowski–Winkler 1983; Quilliot 1978).** $c(G)=1$ iff $G$ is dismantlable.

**Retract bound.** If $H$ is a retract of $G$ (there is $f:V(G)\to V(H)$ with $f|_H = \mathrm{id}$ and $f$ edge-or-vertex preserving), then $c(G) \le \max\{c(H),\, c(G\setminus H)+1\}$ — the engine behind the planar bound.

**Girth lower bound (Aigner–Fromme; Frankl).** If $\operatorname{girth}(G)\ge 5$ then
$$c(G) \ge \delta(G),$$
where $\delta$ is the minimum degree. More generally (Frankl 1987), if $\operatorname{girth}(G) \ge 8t-3$ and $\delta(G) > d$ then $c(G) > d^{\,t}$.

**Why the exponent $\tfrac12$ is right.** For a projective plane $\mathrm{PG}(2,q)$ the incidence graph $I_q$ is bipartite, $(q+1)$-regular, has girth $6$, and $n = 2(q^2+q+1)$ vertices, with
$$c(I_q) = q+1 = \bigl(1+o(1)\bigr)\sqrt{n/2}.$$
Families attaining $\Theta(\sqrt n)$ are called **Meyniel extremal**.

**Complexity context.** Deciding $c(G)\le k$ with $k$ part of the input is EXPTIME-complete (Kinnersley 2015) and NP-hard (Fomin–Golovach–Kratochvíl 2008); for fixed $k$ it is polynomial, in time $n^{O(k)}$.

## 3. History & State of the Art (SOTA)

- **1978–1983.** Quilliot, and independently Nowakowski and Winkler, define the game for one cop and characterise cop-win graphs by dismantlability.
- **1984.** Aigner and Fromme introduce $c(G)$ for $k$ cops, prove the *shortest-path/geodesic guarding* lemma, and show $c(G)\le 3$ for planar $G$.
- **1985/1987.** Meyniel states the $O(\sqrt n)$ bound in private communication; it is first recorded in print by Frankl, *Cops and robbers in graphs with large girth and Cayley graphs* (Discrete Applied Math., 1987), who also proves the first sublinear bound
$$c(G) = O\!\left(\frac{n \log\log n}{\log n}\right).$$
- **2008.** Chiniforooshan removes the $\log\log$: $c(G) = O(n/\log n)$.
- **2011–2012.** Three independent groups — Lu–Peng, Scott–Sudakov, and Frieze–Krivelevich–Loh — reach the current record
$$c(G) \le \frac{n}{2^{(1-o(1))\sqrt{\log_2 n}}}.$$
This is $n^{1-o(1)}$: it does **not** establish soft Meyniel.
- **2013–2019.** Meyniel is settled for random graphs. Bollobás–Kun–Leader (2013) prove $c(G(n,p)) = O(\sqrt{n}\log n)$ for $p \ge 2.1\log n/n$; Prałat–Wormald remove the logarithm and cover all $p$, and settle random $d$-regular graphs.

No improvement on the general upper-bound exponent has been made since 2012.

## 4. Partial Results / Verified Cases

Meyniel's bound (often with an explicit constant) is **proved** for:

| Class | Bound | Source |
|---|---|---|
| Planar graphs | $c \le 3$ | Aigner–Fromme 1984 |
| Genus-$g$ surfaces | $c \le \tfrac{4g}{3}+\tfrac{10}{3}$ | Bowler–Erde–Lehner–Pitz 2021 |
| Treewidth $t$ | $c \le \lfloor t/2\rfloor + 1$ | Joret–Kamiński–Theis 2010 |
| $H$-minor-free | $c \le c_H$ (constant) | Andreae 1986 |
| Diameter $2$ | $c \le 2\sqrt n - 1$ | Lu–Peng 2012 |
| Bipartite, diameter $3$ | $c \le 2\sqrt n - 1$ | Lu–Peng 2012 |
| $G(n,p)$, all $p=p(n)$ | $c = O(\sqrt n)$ a.a.s. | Prałat–Wormald 2016 |
| Random $d$-regular, $d\ge 3$ fixed | $c = \Theta(\sqrt n)$ a.a.s. | Prałat–Wormald 2019 |
| Cayley graphs of abelian groups | $c = O(\sqrt n)$ | Frankl 1987; Bradshaw 2020 |
| Cayley graphs of nilpotent groups of bounded class | $c = O(\sqrt n)$ | Bradshaw 2020 |

Small cases are also fully understood computationally: $c(G)\le 1$ for all $n \le 3$; the minimum order of a graph with $c(G)=3$ is $10$ (the Petersen graph), and the minimum order of a $4$-cop-win graph is known to lie in $\{16,\dots,19\}$ from exhaustive search (Baird–Beveridge–Bonato et al. 2014). For every fixed $k$, $c(G)\le k$ is decidable in $n^{O(k)}$ time, so any fixed-$k$ range is verifiable by machine.

## 5. Principal Obstacles

- **No usable global invariant.** $c(G)$ is not monotone under subgraphs, and only weakly controlled by retracts and minors. There is no known submodular or LP-relaxable quantity whose value certifies $c(G)$, so the standard toolkit for graph parameters (tree-decompositions, flows, entropy) applies only inside restricted classes.
- **Expansion is the enemy of the only known method.** Every general upper-bound proof (Frankl through Lu–Peng/Scott–Sudakov/Frieze–Krivelevich–Loh) is a *covering* argument: park cops so that their balls of some radius $r$ dominate the graph, then shrink the robber's territory. In a graph of degree $d$ a ball of radius $r$ has $\le d^{\,r}$ vertices, so covering $n$ vertices needs $\approx n/d^{\,r}$ cops. To get $\sqrt n$ one needs $r \approx \tfrac12 \log_d n$, but at that radius the cops lose control: the robber can slip through the boundary of a large ball in one move, and the iteration loses a factor per round. The $2^{-\sqrt{\log n}}$ savings is exactly the point where the number of rounds one can afford ($\approx\sqrt{\log n}$) balances the per-round gain.
- **Girth and degree pull in opposite directions.** Frankl's theorem says high girth plus degree $d$ forces large cop number; so any proof must extract a *low-girth* structure from every dense graph and exploit it, but short cycles do not by themselves help the cops — they only help when the robber's escape routes are globally scarce.
- **Extremal examples are algebraic and rare.** All known Meyniel-extremal families come from incidence structures (projective planes, generalized quadrangles, designs). This gives no probabilistic or entropic mechanism to argue that *nothing* can do better, so one cannot reason "either the graph is like a projective plane, or the cops win easily".
- **Adversary-strategy lower bounds are weak.** Robber strategies are analysed by local escape lemmas; there is no known potential function that survives $\omega(1)$ rounds against $\omega(\sqrt n)$ cops, which is why even *soft* Meyniel resists.

## 6. The Gap

Proven: $c(G) \le n\,2^{-(1-o(1))\sqrt{\log_2 n}}$. Conjectured: $c(G) = O(n^{1/2})$. Writing the true worst-case exponent as
$$\alpha^\ast = \limsup_{n\to\infty} \frac{\log \max_{|V(G)|=n} c(G)}{\log n},$$
we know $\alpha^\ast \ge \tfrac12$ (projective planes) and $\alpha^\ast \le 1$ (trivially, and the record bound gives $\alpha^\ast \le 1$ with only a subpolynomial saving). **The entire interval $(\tfrac12, 1]$ is open.** The concrete missing step is a cop strategy whose progress per round is a constant *fraction* of the robber's remaining territory rather than a $2^{-\sqrt{\log n}}$ fraction — equivalently, a covering argument that works at radius $\Theta(\log_d n)$ without losing control of the ball boundary. Even proving $\alpha^\ast < 1$ (soft Meyniel) would be a major advance.

## 7. Current Research (as of June 2026)

- **High-girth constructions.** Bradshaw, Hosseini, Mohar and Turcotte (*On the cop number of graphs of high girth*, J. Graph Theory, 2023) sharpen Frankl's bound to $c(G) \ge \tfrac{1}{e}(\delta-1)^{\lfloor (g-1)/4\rfloor}$ and build graphs of prescribed girth with cop number close to $n^{1/2}$, narrowing the search for non-algebraic Meyniel-extremal families.
- **Algebraic / group-theoretic route.** Following Bradshaw's abelian and nilpotent results, groups of polynomial growth and bounded-doubling Cayley graphs are an active target; the hope is that a Freiman-type structure theorem converts growth control into a covering strategy. *(frontier — verify)*
- **Random and pseudorandom models.** Prałat's Toronto Metropolitan group continues to push cop number for random geometric graphs, hypergraph incidence models, and inhomogeneous random graphs, where Meyniel-type bounds hold with explicit constants.
- **Variants as probes.** Zero-visibility, lazy, surrounding, and containment cops-and-robbers all admit Meyniel analogues; the containment variant is used to test whether the $\sqrt n$ barrier is intrinsic to the covering method or to the game. *(frontier — verify)*
- **Structural classes.** Ongoing work on $H$-free graphs (e.g. $2K_2$-free, $P_5$-free) aims at constant or $O(\sqrt n)$ bounds via forbidden-induced-subgraph arguments rather than covering. *(frontier — verify)*

## 8. Future Work

1. **Attack soft Meyniel first.** Any $c(G)=O(n^{1-\varepsilon})$ bound with fixed $\varepsilon>0$ would be the first exponent improvement in forty years; Scott and Sudakov single this out as the decisive intermediate target.
2. **Bounded-degree case.** Prove Meyniel for graphs of maximum degree $d$ with a constant depending only on $d$ — random $d$-regular graphs are already done, so the obstruction is deterministic expanders.
3. **Diameter induction.** Extend Lu–Peng from diameter $2$ (and bipartite diameter $3$) to diameter $3$ and to bounded diameter generally; a diameter-$k$ result with constant $C(k)$ growing slowly would combine with a diameter-reduction step.
4. **Sharpen the constant.** Determine $\liminf$ and $\limsup$ of $\max_{|V|=n} c(G)/\sqrt n$; projective planes give $\ge 1/\sqrt 2$, and it is open whether this is optimal.
5. **Lower-bound machinery.** Develop a robber potential function robust to $\omega(1)$ rounds; absent one, disproving Meyniel is out of reach.

## 9. Key References

- **[Foundational]** R. Nowakowski, P. Winkler. *Vertex-to-vertex pursuit in a graph.* Discrete Mathematics 43 (1983), 235–239.
- **[Foundational]** A. Quilliot. *Jeux et pointes fixes sur les graphes.* Thèse de 3ème cycle, Université de Paris VI, 1978.
- **[Foundational]** M. Aigner, M. Fromme. *A game of cops and robbers.* Discrete Applied Mathematics 8 (1984), 1–12.
- **[Foundational]** P. Frankl. *Cops and robbers in graphs with large girth and Cayley graphs.* Discrete Applied Mathematics 17 (1987), 301–305.
- **[SOTA]** E. Chiniforooshan. *A better bound for the cop number of general graphs.* Journal of Graph Theory 58 (2008), 45–48.
- **[SOTA]** A. Scott, B. Sudakov. *A bound for the cops and robbers problem.* SIAM Journal on Discrete Mathematics 25 (2011), 1438–1442.
- **[SOTA]** L. Lu, X. Peng. *On Meyniel's conjecture of the cop number.* Journal of Graph Theory 71 (2012), 192–205.
- **[SOTA]** A. Frieze, M. Krivelevich, P. Loh. *Variations on cops and robbers.* Journal of Graph Theory 69 (2012), 383–402.
- **[SOTA]** B. Bollobás, G. Kun, I. Leader. *Cops and robbers in a random graph.* Journal of Combinatorial Theory Series B 103 (2013), 226–236.
- **[SOTA]** P. Prałat, N. Wormald. *Meyniel's conjecture holds for random graphs.* Random Structures & Algorithms 48 (2016), 396–421.
- **[SOTA]** P. Prałat, N. Wormald. *Meyniel's conjecture holds for random $d$-regular graphs.* Random Structures & Algorithms 55 (2019), 719–741.
- **[SOTA]** P. Bradshaw. *A proof of the Meyniel conjecture for abelian Cayley graphs.* Discrete Mathematics 343 (2020), 111546.
- **[SOTA]** N. Bowler, J. Erde, F. Lehner, M. Pitz. *Bounding the cop number of a graph by its genus.* SIAM Journal on Discrete Mathematics 35 (2021), 2459–2489.
- **[SOTA]** W. Kinnersley. *Cops and robbers is EXPTIME-complete.* Journal of Combinatorial Theory Series B 111 (2015), 201–220.
- **[Survey]** W. Baird, A. Bonato. *Meyniel's conjecture on the cop number: a survey.* Journal of Combinatorics 3 (2012), 225–238.
- **[Book]** A. Bonato, R. Nowakowski. *The Game of Cops and Robbers on Graphs.* Student Mathematical Library 61, American Mathematical Society, 2011.

## 10. Worked Example / Concrete Special Case

**The Heawood graph — the smallest Meyniel-extremal instance.**

Take the Fano plane $\mathrm{PG}(2,2)$: $q=2$, so $q^2+q+1 = 7$ points and $7$ lines, each line containing $3$ points, each point on $3$ lines, two points on exactly one common line, two lines meeting in exactly one point. Its incidence graph $I_2$ — the **Heawood graph** — has
$$n = 7 + 7 = 14, \qquad \text{it is } 3\text{-regular}, \qquad \operatorname{girth}(I_2) = 6 .$$
(Girth $6$: a $4$-cycle would need two points on two common lines, contradicting the plane axioms.)

**Lower bound $c(I_2)\ge 3$.** Suppose two cops play, at $x_1,x_2$, and the robber sits at $v$ with $N(v)=\{u_1,u_2,u_3\}$. Because $\operatorname{girth} \ge 5$, any vertex $x \notin N[v]$ has at most one neighbour in $N(v)$: two neighbours would close a $4$-cycle through $v$. So after the cops move, each cop threatens at most one $u_i$ (a cop already inside $N[v]$ would have been caught-adjacent, and the robber never steps next to a cop). With $2$ cops at most $2$ of the $3$ neighbours are threatened, so some $u_i$ is safe and the robber moves there. The robber survives forever, hence $c(I_2)\ge 3 = \delta(I_2)$. This is exactly the Aigner–Fromme/Frankl girth bound $c \ge \delta$.

**Upper bound $c(I_2)\le 3$.** The Heawood graph has treewidth $4$, so Joret–Kamiński–Theis gives $c \le \lfloor 4/2\rfloor + 1 = 3$. Hence $c(I_2)=3$.

**Checking Meyniel.** $\sqrt{n} = \sqrt{14} \approx 3.742$, and
$$\frac{c(I_2)}{\sqrt n} = \frac{3}{3.742} \approx 0.802 .$$
So the constant $C=1$ already suffices here. Running the same computation for general $q$ (a prime power), $c(I_q)=q+1$ and $n=2(q^2+q+1)$, so
$$\frac{c(I_q)}{\sqrt n} = \frac{q+1}{\sqrt{2q^2+2q+2}} \xrightarrow[q\to\infty]{} \frac{1}{\sqrt 2} \approx 0.7071 .$$
Numerically: $q=3 \Rightarrow n=26$, $c=4$, ratio $0.784$; $q=7 \Rightarrow n=114$, $c=8$, ratio $0.749$; $q=31 \Rightarrow n=1986$, $c=32$, ratio $0.718$.

**What this example shows.** The ratio $c/\sqrt n$ decreases monotonically toward $1/\sqrt2$ — projective planes certify that no bound $c(G)=o(\sqrt n)$ can hold, and that $C \ge 1/\sqrt 2$. What no example does is bound the ratio from above: for all anyone can prove, some unknown family has $c(G) = n^{0.9}$. That is the whole content of the conjecture.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*