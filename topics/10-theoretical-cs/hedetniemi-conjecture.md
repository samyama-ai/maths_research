---
id: 10-theoretical-cs/hedetniemi-conjecture
title: "Hedetniemi Conjecture"
topic: 10-theoretical-cs
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Hedetniemi Conjecture

> **Topic:** Theoretical Computer Science · **ID:** `10-theoretical-cs/hedetniemi-conjecture` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

For finite simple graphs $G$ and $H$, let $G \times H$ denote the **categorical (tensor) product**. Hedetniemi (1966) conjectured

$$\chi(G \times H) \;=\; \min\bigl(\chi(G),\, \chi(H)\bigr).$$

The inequality $\chi(G\times H) \le \min(\chi(G),\chi(H))$ is immediate (pull back a colouring along a projection). The conjecture is the reverse inequality: the product of two graphs, each needing $n$ colours, still needs $n$ colours.

**Resolution.** The conjecture is **false**. Shitov (*Annals of Mathematics*, 2019) constructed graphs $G, H$ with $\chi(G), \chi(H) > c$ and $\chi(G\times H) \le c$. A complete disproof requires exhibiting (or proving the existence of) such a pair; Shitov's is non-explicit in size but fully constructive in method.

**What remains open** is the quantitative refinement. Define the **Poljak–Rödl function**

$$f(n) \;=\; \min\{\chi(G\times H) \;:\; \chi(G)=\chi(H)=n\}.$$

Hedetniemi's conjecture is exactly $f(n)=n$ for all $n$. It is known that $f(n)=n$ for $n\le 4$ and $f(n)<n$ for $n \ge 14$. **Open:** is $f$ bounded? Is $f(5)=5$?

## 2. Mathematical Foundations

**Categorical product.** $V(G\times H)=V(G)\times V(H)$ and

$$(u,v)\,(u',v') \in E(G\times H) \iff uu'\in E(G) \ \text{ and }\ vv'\in E(H).$$

The projections $\pi_G, \pi_H$ are graph homomorphisms, and $G\times H$ is the product in the category of graphs and homomorphisms: $\mathrm{Hom}(K, G\times H)\cong \mathrm{Hom}(K,G)\times \mathrm{Hom}(K,H)$.

**Chromatic number as homomorphism.** $\chi(G)\le n \iff G \to K_n$. Hence $\chi(G\times H)\le \min(\chi(G),\chi(H))$ by composing with a projection.

**Multiplicativity.** A graph $K$ is *multiplicative* if for all $G,H$: $G\times H \to K$ implies $G\to K$ or $H\to K$. Hedetniemi's conjecture $\iff$ $K_n$ is multiplicative for every $n$.

**Exponential graph.** For a graph $G$ and integer $c$, define $K_c^{\,G}$ by

$$V(K_c^{\,G}) = \{\,f : V(G)\to [c]\,\},\qquad f \sim f' \iff \forall\, uv\in E(G):\ f(u)\neq f'(v).$$

Two facts drive everything:

1. **Always** $\chi\bigl(G\times K_c^{\,G}\bigr)\le c$, via the *evaluation colouring* $(v,f)\mapsto f(v)$. If $(v,f)\sim(v',f')$ then $vv'\in E(G)$ and $f\sim f'$, so $f(v)\neq f'(v')$.
2. **(El-Zahar–Sauer, 1985)** $K_c$ is multiplicative $\iff$ for every $G$ with $\chi(G)>c$ one has $\chi(K_c^{\,G})\le c$.

So a counterexample is precisely a graph $G$ with

$$\chi(G) > c \quad\text{and}\quad \chi\bigl(K_c^{\,G}\bigr) > c,$$

taking $H = K_c^{\,G}$.

**Fractional relaxation.** With $\chi_f$ the fractional chromatic number, $\chi_f(G\times H)=\min(\chi_f(G),\chi_f(H))$ holds unconditionally (Zhu, 2011).

## 3. History & State of the Art (SOTA)

- **1966.** Stephen T. Hedetniemi states the conjecture in his University of Michigan doctoral work *Homomorphisms of graphs and automata* (Technical Report 03105-44-T).
- **1981.** Poljak and Rödl introduce $f(n)$ and prove a dichotomy: either $f(n)\le 4$ for all $n$, or $f(n)\to\infty$.
- **1985.** El-Zahar and Sauer prove $K_3$ multiplicative: the product of two $4$-chromatic graphs is $4$-chromatic, i.e. $f(4)=4$. This is still the deepest positive case.
- **1998–2008.** Surveys by Zhu (*Taiwanese J. Math.*) and Sauer (*Discrete Math.*, 2001); Tardif's "40 years later" (2008) collects the exponential-graph machinery and the circular-chromatic variants.
- **2011.** Zhu proves the fractional version.
- **2019.** Shitov disproves the conjecture, using graphs of large girth and large chromatic number ("wide" graphs) and a counting argument bounding the colourings of $K_c^{\,G}$. The parameters are astronomically large ($c$ on the order of $10^{3}$–$10^{4}$ and $|V(G)|$ far larger).
- **2019–2023, quantitative phase.** Tardif–Zhu shrink the parameters via Stahl's conjecture on Kneser graphs; He and Wigderson prove $f(n)\le\bigl(\tfrac12+o(1)\bigr)n$; Zhu brings counterexamples down to $c=125$; Tardif reaches **$f(14)\le 13$**, the current record.

## 4. Partial Results / Verified Cases

- **$n \le 4$: conjecture true.** $f(1)=1$, $f(2)=2$ (odd-cycle argument, Section 10), $f(3)=3$ (Burr–Erdős–Lovász–type / Sauer), and $f(4)=4$ by El-Zahar–Sauer (1985).
- **$n \ge 14$: conjecture false.** Tardif (2022), *The chromatic number of the product of 14-chromatic graphs can be 13*.
- **$n \ge 125$:** Zhu (2021), explicit counterexample families with $\chi(G)=\chi(H)=125$, $\chi(G\times H)\le 124$.
- **Asymptotics.** $f(n)\le \bigl(\tfrac12 + o(1)\bigr)n$ (He–Wigderson, 2021). Combined with Poljak–Rödl monotonicity-type arguments this gives failure for all large $n$.
- **Fractional version: true** for all graphs (Zhu, 2011).
- **Circular cliques.** Tardif proved $K_{p/q}$ is multiplicative for $2\le p/q < 4$; the circular analogue of Hedetniemi thus holds below circular chromatic number $4$.
- **Structured factors.** Multiplicativity holds when one factor is a tree, a cycle, or more generally when $H$ admits enough structure (Häggkvist–Hell–Miller–Neumann-Lara for cycles; Hell–Nešetřil for various homomorphism dualities).
- **Digraphs.** The directed analogue was known false long before 1966-style optimism faded (Poljak–Rödl), which was already a warning sign.

## 5. Principal Obstacles

The residual open questions resist current tools for structural reasons.

- **No local certificate for $\chi \ge n$.** Chromatic number is not characterised by any finite family of forbidden local configurations. Every positive proof for $n \le 4$ exploits an ad-hoc structural fact — El-Zahar–Sauer's proof is a long case analysis of $4$-critical graphs — and no such analysis is known for $5$-critical graphs.
- **Topological lower bounds are too weak.** Borsuk–Ulam / neighbourhood-complex methods give $\chi(G)\ge \mathrm{conn}(\mathcal N(G))+3$, but the box complex of a product does not behave multiplicatively in a way that transfers these bounds; the topological lower bound of $G\times H$ collapses.
- **Fractional relaxation is not tight.** The fractional statement is true, so any proof of a false integral statement must exploit integrality gaps; conversely, any proof of a positive case cannot go through LP relaxation. The gap between $\chi_f$ and $\chi$ can be logarithmic, exactly the regime the counterexamples inhabit.
- **Exponential graphs are unmanageable.** $K_c^{\,G}$ has $c^{|V(G)|}$ vertices. Deciding $\chi(K_c^{\,G})\le c$ is not amenable to computer search even for tiny $G$, so the $5\le n\le 13$ window cannot be attacked computationally.
- **Counterexamples need large girth.** Shitov's method requires $G$ with large girth and large chromatic number (probabilistic or Kneser-based), which forces $|V(G)|$ up; small $n$ leaves no room for the counting slack.

## 6. The Gap

Proven: $f(n)=n$ for $n\le 4$; $f(n)\le n-1$ for $n\ge 14$; $f(n)\le(\tfrac12+o(1))n$ asymptotically.

Unproven, and the exact frontier:

1. **The window $5\le n\le 13$.** Is $f(5)=5$, i.e. is $K_4$ multiplicative? Crossing this needs either a structural theory of $5$-critical graphs under products (extending El-Zahar–Sauer) or a counterexample construction whose overhead is $O(1)$ rather than requiring girth-driven blowup.
2. **Boundedness.** Poljak–Rödl: either $f\le 4$ everywhere or $f\to\infty$. Since $f(4)=4$, the live question is whether $f$ is bounded by a constant (necessarily $\le 4$ in the strong dichotomy sense, hence essentially whether $f(n)\le 4$ for large $n$) or grows. He–Wigderson shows $f(n)=O(n)$ with constant $<1$; no super-constant lower bound beyond $f(n)\ge 4$ is known. **The gap is between the lower bound $4$ and the upper bound $(\tfrac12+o(1))n$ — a constant versus a linear function.**

## 7. Current Research (as of June 2026)

- **Shrinking $n$.** Tardif (Royal Military College of Canada) and Zhu (Zhejiang Normal University) continue the descent from $14$ toward $5$; the bottleneck is the girth requirement in the wide-graph input.
- **Simplified proofs.** Wrochna's *Smaller counterexamples to Hedetniemi's conjecture* (arXiv, 2020) reworks Shitov's argument through fractional/topological covering language and reduces the parameters *(frontier — verify the precise chromatic numbers claimed)*.
- **The Poljak–Rödl function.** He (Stanford/Caltech circle) and Wigderson: whether $f(n)=\Omega(n)$ or $f$ is bounded; current belief among specialists is split, with recent evidence leaning toward $f$ unbounded but sublinear behaviour not excluded.
- **Kneser-graph inputs.** Stahl's conjecture on multichromatic numbers of Kneser graphs enters through Tardif–Zhu; progress on Stahl mechanically improves the counterexample parameters.
- **Constraint-satisfaction angle.** Multiplicativity of general targets $K$ links to the algebraic CSP dichotomy programme (Hell–Nešetřil, Barto–Kozik school in Prague/Kraków); multiplicativity of $K$ is a statement about $\mathrm{Hom}(-,K)$ preserving products.

## 8. Future Work

- Prove or disprove $f(5)=5$ — the single most-cited remaining target; a positive proof would likely require a computer-assisted analysis of $5$-critical structure analogous to El-Zahar–Sauer.
- Determine whether $f$ is bounded (Poljak–Rödl, open since 1981). A super-constant lower bound $f(n)\ge 5$ for all $n$ would already be a breakthrough.
- Improve the asymptotic constant below $\tfrac12$, or prove a matching lower bound $f(n)\ge cn$.
- Classify multiplicative graphs beyond circular cliques; Tardif's programme asks which targets $K$ satisfy the product property.
- Transfer the counterexample technique to hypergraph and digraph colouring, and to the circular chromatic number above $4$.

## 9. Key References

- **[Foundational]** Hedetniemi, S. T. *Homomorphisms of graphs and automata.* University of Michigan Technical Report 03105-44-T, 1966.
- **[Foundational]** El-Zahar, M., Sauer, N. *The chromatic number of the product of two 4-chromatic graphs is 4.* Combinatorica **5** (1985), 121–126.
- **[Foundational]** Poljak, S., Rödl, V. *On the arc-chromatic number of a digraph.* Journal of Combinatorial Theory, Series B **31** (1981), 190–198.
- **[SOTA]** Shitov, Y. *Counterexamples to Hedetniemi's conjecture.* Annals of Mathematics **190** (2019), no. 2, 663–667.
- **[SOTA]** He, X., Wigderson, Y. *Hedetniemi's conjecture is asymptotically false.* Journal of Combinatorial Theory, Series B **146** (2021), 485–494.
- **[SOTA]** Zhu, X. *Relatively small counterexamples to Hedetniemi's conjecture.* Journal of Combinatorial Theory, Series B **146** (2021), 141–150.
- **[SOTA]** Tardif, C. *The chromatic number of the product of 14-chromatic graphs can be 13.* Combinatorica **42** (2022).
- **[Recent]** Tardif, C., Zhu, X. *A note on Hedetniemi's conjecture, Stahl's conjecture and the Poljak–Rödl function.* Electronic Journal of Combinatorics **26** (2019), \#P4.32.
- **[Recent]** Zhu, X. *The fractional version of Hedetniemi's conjecture is true.* European Journal of Combinatorics **32** (2011), 1168–1175.
- **[Survey]** Zhu, X. *A survey on Hedetniemi's conjecture.* Taiwanese Journal of Mathematics **2** (1998), 1–24.
- **[Survey]** Sauer, N. *Hedetniemi's conjecture — a survey.* Discrete Mathematics **229** (2001), 261–292.
- **[Survey]** Tardif, C. *Hedetniemi's conjecture, 40 years later.* Graph Theory Notes of New York **54** (2008), 46–57.
- **[Book]** Hell, P., Nešetřil, J. *Graphs and Homomorphisms.* Oxford University Press, 2004.

## 10. Worked Example / Concrete Special Case

**(a) The easy direction.** Let $c:V(G)\to[k]$ be proper with $k=\chi(G)$. Define $\tilde c(u,v)=c(u)$ on $G\times H$. If $(u,v)\sim(u',v')$ then $uu'\in E(G)$, so $c(u)\neq c(u')$. Hence $\chi(G\times H)\le\chi(G)$, and symmetrically $\le \chi(H)$.

**(b) The case $n=2$ is true: $f(2)=2$.** Suppose $\chi(G),\chi(H)\ge 3$. Then $G$ has a closed walk of odd length $a$ and $H$ one of odd length $b$. Traversing the first walk $b$ times and the second $a$ times in lockstep gives a closed walk of odd length $ab$ in $G\times H$, so $G\times H$ is not bipartite and $\chi(G\times H)\ge 3$.

*Concrete instance.* $G=C_5$, $H=C_3$. Then $G\times H$ has $15$ vertices and is connected; the lockstep walk has length $15$, odd. So $\chi(C_5\times C_3)\ge 3$, and by (a) $\chi \le \min(3,3)=3$. Thus $\chi(C_5\times C_3)=3=\min(\chi(C_5),\chi(C_3))$. ✓

**(c) Where the conjecture breaks — the exponential-graph mechanism.** Fix $c$ and any $G$. Put $H=K_c^{\,G}$, the graph of maps $f:V(G)\to[c]$ with $f\sim f'$ iff $f(u)\neq f'(v)$ for every edge $uv\in E(G)$. Colour $G\times H$ by

$$\Phi(v,f) = f(v)\in[c].$$

*Check:* an edge $(v,f)\sim(v',f')$ means $vv'\in E(G)$ and $f\sim f'$; the definition of $\sim$ applied to the edge $vv'$ gives $f(v)\neq f'(v')$, i.e. $\Phi(v,f)\neq\Phi(v',f')$. So **$\chi(G\times K_c^{\,G})\le c$ for every $G$, unconditionally.**

Therefore Hedetniemi fails as soon as one finds a single $G$ with

$$\chi(G) > c \qquad\text{and}\qquad \chi\bigl(K_c^{\,G}\bigr) > c .$$

*Sanity check that this is not vacuous for small $c$.* For $c=2$ and $G$ non-bipartite, $K_2^{\,G}$ turns out to be $2$-colourable (consistent with $f(2)=2$), so no counterexample. Shitov's contribution is to produce, for large $c$, a graph $G$ of large girth with $\chi(G)>c$ for which every $c$-colouring of $K_c^{\,G}$ is obstructed by a counting argument on the "almost constant" maps $f$ — forcing $\chi(K_c^{\,G})>c$ and hence $\chi(G\times K_c^{\,G})\le c<\min(\chi(G),\chi(K_c^{\,G}))$. Zhu and Tardif then optimise this to $c=124$ and $c=13$ respectively.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*