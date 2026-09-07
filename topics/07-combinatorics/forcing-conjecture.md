---
id: 07-combinatorics/forcing-conjecture
title: "Forcing Conjecture"
topic: 07-combinatorics
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Forcing Conjecture

> **Topic:** Combinatorics & Graph Theory · **ID:** `07-combinatorics/forcing-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

A graph $H$ is **forcing** if the single equation "$H$-density equals the random value" already forces quasirandomness: for every sequence of graphs $(G_n)$ with edge density tending to $p \in (0,1)$, if the homomorphism density of $H$ in $G_n$ tends to $p^{e(H)}$, then $(G_n)$ is $p$-quasirandom.

**Forcing Conjecture.** *A graph $H$ is forcing if and only if $H$ is bipartite and contains a cycle.*

The "only if" direction is proved (Section 4). The open content is the "if": every bipartite graph with at least one cycle is forcing. A complete proof must supply, for each such $H$, an inequality of the form $t(H,W) \ge p^{e(H)}$ with equality only at the constant graphon; a disproof must exhibit a bipartite $H$ with a cycle and a non-constant graphon $W$ with $\int W = p$ and $t(H,W) = p^{e(H)}$.

The conjecture is attributed to Skokan and Thoma (2004) and appears in this form in Conlon–Fox–Sudakov (2010) and in Lovász's monograph. It strictly implies **Sidorenko's Conjecture**, its better-known weaker sibling.

## 2. Mathematical Foundations

Work in the graphon space: $\mathcal{W}_0$ is the set of symmetric measurable $W : [0,1]^2 \to [0,1]$. For a finite graph $H = (V,E)$ the **homomorphism density** is
$$t(H,W) \;=\; \int_{[0,1]^{V}} \prod_{\{u,v\}\in E} W(x_u,x_v) \; \prod_{v \in V} dx_v .$$
Write $p = t(K_2,W) = \int W$, the edge density, and $d_W(x) = \int_0^1 W(x,y)\,dy$ the degree function.

**Cut norm.** $\displaystyle \|U\|_\square = \sup_{S,T \subseteq [0,1]} \Big| \int_{S\times T} U(x,y)\,dx\,dy \Big|$. A sequence $(G_n)$ with density $\to p$ is **$p$-quasirandom** iff $\|W_{G_n} - p\|_\square \to 0$, equivalently $G_n \to p$ in the cut metric.

**Forcing.** $H$ is forcing iff for all $W \in \mathcal{W}_0$,
$$t(H,W) \;\ge\; t(K_2,W)^{e(H)} \qquad\text{with equality iff } W \equiv p \text{ a.e.}$$
The inequality alone is **Sidorenko's property**; forcing $=$ Sidorenko $+$ rigidity of the equality case. Hence *forcing $\Rightarrow$ Sidorenko*, and the Forcing Conjecture implies Sidorenko's conjecture (which asserts the inequality for all bipartite $H$).

**Graph norms.** For $H$ with $e(H)$ edges set $\|U\|_H = |t(H,U)|^{1/e(H)}$ for symmetric $U:[0,1]^2\to\mathbb{R}$. $H$ is **norming** if $\|\cdot\|_H$ is a norm, and **weakly norming** if $\|\cdot\|_H$ is a norm on nonnegative $U$. Hatami's theorem: *weakly norming $\Rightarrow$ forcing*. The prototype is $H = C_4$, where $\|U\|_{C_4} = \|U\|_4$ is the Schatten–von-Neumann-type quartic norm and $\|U\|_\square \le \|U\|_4$.

**Chung–Graham–Wilson.** The equivalence of $\|W-p\|_\square\to 0$ with the count condition $t(C_4,W)\to p^4$ (given $t(K_2,W)\to p$) is the founding instance: $\{K_2, C_4\}$ is a *forcing pair*.

## 3. History & State of the Art (SOTA)

- **1989** — Chung, Graham and Wilson, *Quasi-random graphs* (Combinatorica 9), prove seven properties of dense graphs equivalent, among them the $C_4$-count condition. $C_4$ is the first forcing graph.
- **1993** — Sidorenko formulates his correlation inequality (*A correlation inequality for bipartite graphs*, Graphs and Combinatorics 9), earlier appearing in work of Erdős–Simonovits; it isolates the inequality half.
- **2004** — Skokan and Thoma, *Bipartite subgraphs and quasi-randomness* (Graphs and Combinatorics 20), prove $K_{a,b}$ is forcing for $a,b \ge 2$ and pose the conjecture in its present generality.
- **2010** — Hatami, *Graph norms and Sidorenko's conjecture* (Israel J. Math. 175), introduces (weakly) norming graphs, proves weakly norming $\Rightarrow$ forcing, and verifies the property for complete bipartite graphs, even cycles and hypercubes $Q_d$.
- **2010** — Conlon, Fox and Sudakov, *An approximate version of Sidorenko's conjecture* (GAFA 20), prove Sidorenko (and a forcing version) for bipartite $H$ with a vertex joined to all vertices of the other part; they state the Forcing Conjecture explicitly.
- **2012** — Lovász, *Large Networks and Graph Limits*, recasts forcing in graphon language and catalogues forcing families.
- **2016–2018** — Kim–Lee–Lee (Trans. AMS 368) and Conlon–Kim–Lee–Lee (J. London Math. Soc. 98) develop the *tree-arrangeable* / random-walk (Markov chain) method, extending both Sidorenko and forcing to large new classes.
- **2019–2021** — Kráľ–Martins–Pach–Wrochna (JCTA 162) and Grzesik–Kráľ–Lovász Jr. (Proc. LMS) delimit the norming route: $K_{5,5}$ minus a perfect matching is not weakly norming, and "step Sidorenko" fails for edge-transitive graphs, so Hatami's implication cannot reach all bipartite $H$.
- **2021** — Conlon and Lee, *Sidorenko's conjecture for blow-ups* (Discrete Analysis 2021:2), prove that a sufficiently large blow-up of any bipartite graph is Sidorenko; the same machinery yields forcing statements for blow-ups.

## 4. Partial Results / Verified Cases

**Necessity (proved).** If $H$ has an odd cycle, $H$ is not forcing: a suitable perturbation $W = p + U$ with $\int U = 0$ can cancel the positive and negative contributions to $t(H,W)$, so equality occurs at non-constant $W$. If $H$ is a forest with $e(H)=m$, take $W$ the graphon of two disjoint cliques of equal measure and density $p=1/2$; then $t(H,W) = 2\cdot(1/2)^{v(H)} = (1/2)^{m}$ while $\|W-1/2\|_\square = 1/8 \ne 0$. Disconnected $H$ reduces to components. So forcing graphs are bipartite with a cycle.

**Sufficiency, known classes.**
- Even cycles $C_{2k}$, $k \ge 2$ (Chung–Graham–Wilson for $k=2$; general $k$ from Hatami's norming property).
- Complete bipartite graphs $K_{a,b}$, $a,b \ge 2$ (Skokan–Thoma 2004; also norming for even $a$ or $b$).
- Hypercubes $Q_d$, all $d \ge 2$ (Hatami 2010).
- All weakly norming graphs, including the reflection-group families of Conlon–Lee (*Finite reflection groups and graph norms*, Adv. Math. 315, 2017).
- Bipartite $H$ with a vertex complete to the opposite part (Conlon–Fox–Sudakov 2010) — this covers every bipartite graph on at most $5$ vertices containing a cycle, and in particular all bipartite $H$ of one-sided size $\le 2$.
- Tree-arrangeable graphs and graphs built by "tree-like" gluings (Kim–Lee–Lee 2016; Conlon–Kim–Lee–Lee 2018), which include every bipartite $H$ having a part in which some vertex has degree $\le 2$ after suitable reduction, and all bipartite $H$ with $\min$-degree side of bounded size.
- Bipartite $H$ with parts $A,B$ where $|A| \le 4$ or $H$ has at most $6$ vertices: covered by the union of the above.
- Blow-ups $H^{(k)}$ of any bipartite $H$ for $k$ large (Conlon–Lee 2021).

Sidorenko's inequality is verified for all bipartite graphs up to about $8$–$9$ vertices by combinations of these methods plus computer-assisted flag-algebra / SOS certificates; forcing follows whenever the certificate is strict.

## 5. Principal Obstacles

- **Rigidity is harder than positivity.** Entropy/information-theoretic proofs of Sidorenko (Szegedy; Kim–Lee–Lee) produce the inequality $t(H,W)\ge p^{e(H)}$ but lose track of the equality case: the entropy-maximisation step is not strictly concave in the directions that matter, so equality does not immediately force $W$ constant.
- **Cauchy–Schwarz/Hölder chains degenerate.** Every known proof strings together Hölder steps; strictness at each step is needed for forcing, but for graphs without enough symmetry the chain passes through auxiliary quantities whose equality cases are large families.
- **Norming route is provably insufficient.** Kráľ–Martins–Pach–Wrochna showed $K_{5,5}$ minus a perfect matching is not weakly norming, so Hatami's implication cannot be the general mechanism; forcing must be proved without a norm.
- **No positivstellensatz for homomorphism densities.** Hatami–Norine proved that deciding validity of linear inequalities between homomorphism densities is undecidable, and that not every valid inequality has a sum-of-squares proof. So a uniform certificate scheme for all bipartite $H$ may not exist.
- **Local vs global.** Methods that work for "locally dense" hosts (Lee, RSA 2021) control $W$ near the constant graphon but give nothing about graphons far away with the same $H$-count.

## 6. The Gap

Proved: forcing for weakly norming graphs, for graphs with a vertex complete to the other side, for tree-arrangeable graphs, for large blow-ups. Conjectured: all bipartite $H$ with a cycle.

The precise missing step is a **strict** Sidorenko inequality for bipartite graphs that are neither norming nor reducible by a tree/random-walk decomposition. The smallest well-known test cases are $K_{5,5}$ minus a perfect matching (Sidorenko is known by other means; the *equality case* is the residual issue) and the incidence graphs of finite projective planes, e.g. the Heawood graph (bipartite, $3$-regular, girth $6$, $14$ vertices), where no known decomposition applies. Even granting Sidorenko for all bipartite $H$, forcing would remain open: one would still have to show that $t(H,W)=p^{e(H)}$ implies $\|W-p\|_\square = 0$, which no current proof of Sidorenko delivers as a black box.

## 7. Current Research (as of June 2026)

- **Norm theory of graphs** (Conlon, Lee, Kráľ and coauthors): classifying weakly norming graphs via reflection groups, and studying "step Sidorenko" as an intermediate property. The programme now aims at replacing norms by weaker *strict convexity* statements sufficient for forcing. *(frontier — verify)*
- **Entropy and Markov-chain methods** (Szegedy's information-theoretic framework; Kim–Lee–Lee): current work seeks stability versions — quantitative bounds of the form $t(H,W) \ge p^{e(H)} + c_H\|W-p\|_\square^{C}$ — which would give forcing with an explicit rate. Partial rates exist for $C_{2k}$ and $K_{a,b}$.
- **Flag algebras and SDP certificates** (Kráľ's group, Brno/Leipzig; Razborov school): machine-generated strict certificates for individual bipartite graphs up to ~10 vertices. *(frontier — verify)*
- **Blow-up and tensor tricks** (Conlon–Lee): proving properties for $H^{(k)}$ and transferring back to $H$; the transfer step remains lossy for forcing.
- **Analytic/limit-theory groups** at Oxford, Caltech, KAIST, Masaryk and Warwick are the principal centres.

## 8. Future Work

1. Prove a **stability form of Sidorenko** for a class strictly larger than weakly norming graphs — e.g. all bipartite graphs of girth $\ge 6$ — since stability implies forcing directly.
2. Settle forcing for **incidence graphs of generalized polygons** (Heawood graph first): a single new example without a norm would signal a genuinely new mechanism.
3. Determine whether **Sidorenko $\Rightarrow$ forcing** for bipartite graphs with a cycle. No counterexample and no proof is known; a proof would collapse the two conjectures.
4. Develop **finite forcing families** beyond $\{K_2,C_4\}$: characterise which finite sets of graphs jointly force quasirandomness, and relate this to the single-graph conjecture.
5. Explore whether the **undecidability results** of Hatami–Norine obstruct any uniform certificate, and if so, whether forcing admits a non-constructive proof via limit compactness.

## 9. Key References

- **[Foundational]** F. R. K. Chung, R. L. Graham, R. M. Wilson. *Quasi-random graphs.* Combinatorica **9** (1989), 345–362.
- **[Foundational]** A. F. Sidorenko. *A correlation inequality for bipartite graphs.* Graphs and Combinatorics **9** (1993), 201–204.
- **[Foundational]** J. Skokan, L. Thoma. *Bipartite subgraphs and quasi-randomness.* Graphs and Combinatorics **20** (2004), 255–262.
- **[Foundational]** H. Hatami. *Graph norms and Sidorenko's conjecture.* Israel Journal of Mathematics **175** (2010), 125–150.
- **[SOTA]** D. Conlon, J. Fox, B. Sudakov. *An approximate version of Sidorenko's conjecture.* Geometric and Functional Analysis **20** (2010), 1354–1366.
- **[SOTA]** J. H. Kim, C. Lee, J. Lee. *Two approaches to Sidorenko's conjecture.* Transactions of the American Mathematical Society **368** (2016), 5057–5074.
- **[SOTA]** D. Conlon, J. Lee. *Finite reflection groups and graph norms.* Advances in Mathematics **315** (2017), 130–165.
- **[SOTA]** D. Conlon, J. H. Kim, C. Lee, J. Lee. *Some advances on Sidorenko's conjecture.* Journal of the London Mathematical Society **98** (2018), 593–608.
- **[SOTA]** D. Kráľ, T. Martins, P. P. Pach, M. Wrochna. *The step Sidorenko property and non-norming edge-transitive graphs.* Journal of Combinatorial Theory Series A **162** (2019), 34–54.
- **[SOTA]** D. Conlon, J. Lee. *Sidorenko's conjecture for blow-ups.* Discrete Analysis **2021:2**.
- **[Survey]** L. Lovász. *Large Networks and Graph Limits.* AMS Colloquium Publications, vol. 60, 2012.
- **[Survey]** H. Hatami, S. Norine. *Undecidability of linear inequalities in graph homomorphism densities.* Journal of the American Mathematical Society **24** (2011), 547–565.

## 10. Worked Example / Concrete Special Case

**$C_4$ is forcing.** Let $W \in \mathcal{W}_0$, $p = \int W$, and suppose $t(C_4,W) = p^4$. Write $U = W - p$, so $\int U = 0$.

*Step 1 — the Cauchy–Schwarz chain.* With $P_3$ the path on three vertices,
$$t(C_4,W) = \int\!\!\int \Big(\int W(x,y)W(z,y)\,dy\Big)^2 dx\,dz \;\ge\; \Big(\int\!\!\int\!\!\int W(x,y)W(z,y)\Big)^2 = t(P_3,W)^2,$$
and $t(P_3,W) = \int d_W(x)^2 dx \ge \big(\int d_W\big)^2 = p^2$. Hence $t(C_4,W)\ge p^4$.

*Step 2 — equality forces regularity.* Equality throughout requires $\int d_W(x)^2dx = p^2$, i.e. $d_W \equiv p$ a.e., i.e. $d_U \equiv 0$.

*Step 3 — expansion.* Expand $t(C_4, p+U)$ over the $2^4$ choices of $p$ or $U$ on the four edges $xy,yz,zw,wx$:
- one $U$: $4p^3\int U = 0$;
- two adjacent $U$'s: $4p^2\int d_U(y)^2 dy = 0$;
- two opposite $U$'s: $2p^2(\int U)^2 = 0$;
- three $U$'s: $4p\int d_U(y)\,U(y,z)\,d_U(z) = 0$;
- four $U$'s: $t(C_4,U) = \|U\|_4^4$.

So $t(C_4,W) = p^4 + \|U\|_4^4$. Given $t(C_4,W)=p^4$ we get $\|U\|_4 = 0$, and since $\|U\|_\square \le \|U\|_4$, $U = 0$ a.e. Thus $W \equiv p$: $C_4$ is forcing. $\blacksquare$

**Contrast — the path $P_3$ is not forcing.** Take $W(x,y) = 1$ if $x,y$ lie in the same half of $[0,1]$ and $0$ otherwise. Then $p = 1/2$, $d_W \equiv 1/2$, and $t(P_3,W) = \int d_W^2 = 1/4 = p^{2}$: the path count is exactly random. But $t(C_4,W) = 2\cdot(1/2)^4 = 1/8 \ne 1/16$ and $\|W - 1/2\|_\square = 1/8 > 0$. The same $W$ defeats every tree, since $t(T,W) = 2\cdot 2^{-v(T)} = (1/2)^{e(T)}$. This is exactly why the conjecture demands a cycle, and why $C_4$ — the smallest bipartite graph with a cycle — is the model case the general conjecture tries to imitate.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*