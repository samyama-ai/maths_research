---
id: 07-combinatorics/hedetniemis-conjecture
title: "Hedetniemi's Conjecture"
topic: 07-combinatorics
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Hedetniemi's Conjecture

> **Topic:** Combinatorics & Graph Theory · **ID:** `07-combinatorics/hedetniemis-conjecture` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

Hedetniemi's conjecture (1966) asserts that for all finite simple graphs $G$ and $H$,
$$\chi(G \times H) \;=\; \min\{\chi(G), \chi(H)\},$$
where $G \times H$ is the **categorical** (tensor, Kronecker) product and $\chi$ is the chromatic number.

The inequality $\chi(G\times H) \le \min\{\chi(G),\chi(H)\}$ is immediate; the content is the lower bound. A disproof requires exhibiting graphs $G,H$ with $\chi(G\times H) < \min\{\chi(G),\chi(H)\}$.

**Status.** Disproved by Yaroslav Shitov (*Annals of Mathematics*, 2019). What remains open is the quantitative residue: the Poljak–Rödl function
$$f(n) \;=\; \min\{\chi(G\times H) : \chi(G)=\chi(H)=n\}$$
satisfies $f(n)=n$ for $n\le 4$ and $f(n)<n$ for all large $n$. **Whether $f$ is bounded** — i.e. whether some fixed $c$ has $\chi(G\times H)\le c$ for graphs of arbitrarily large chromatic number — is the principal surviving open problem, together with the exact threshold $n$ at which $f(n)<n$ first occurs.

## 2. Mathematical Foundations

**Categorical product.** For graphs $G=(V_G,E_G)$, $H=(V_H,E_H)$:
$$V(G\times H)=V_G\times V_H,\qquad (g,h)\sim(g',h') \iff gg'\in E_G \text{ and } hh'\in E_H .$$
This is the product in the category of graphs with homomorphisms: a homomorphism $F\to G\times H$ is exactly a pair $(F\to G,\ F\to H)$. The projections $\pi_G,\pi_H$ are homomorphisms, so any proper $n$-colouring of $G$ (a homomorphism $G\to K_n$) pulls back, giving
$$\chi(G\times H)\le\min\{\chi(G),\chi(H)\}.$$

**Homomorphism reformulation.** Since $\chi(G)\le n \iff G\to K_n$, the conjecture states: if $G\times H\to K_n$ then $G\to K_n$ or $H\to K_n$. A graph $K$ with this property (for all $G,H$ with $G\times H\to K$) is called **multiplicative**. Hedetniemi's conjecture $=$ "every complete graph is multiplicative".

**Exponential graph.** For graphs $H,K$, define $K^{H}$ with vertex set all functions $\varphi:V_H\to V_K$ and
$$\varphi\sim\psi \iff \big(\forall\, hh'\in E_H:\ \varphi(h)\psi(h')\in E_K\big).$$
The adjunction $G\times H \to K \iff G\to K^{H}$ holds. Hence $K_n$ is multiplicative iff for every $H$ with $\chi(H)>n$, either $\chi(K_n^{H})>n$ or $H\to K_n$ — the standard El-Zahar–Sauer route.

**Fractional analogue.** With $\chi_f$ the fractional chromatic number, $\chi_f(G\times H)=\min\{\chi_f(G),\chi_f(H)\}$ is a *theorem* (Zhu, 2011).

**Poljak–Rödl function.** $f(n)$ as above is non-decreasing, satisfies $f(n)\le n$, and Poljak–Rödl (1981) proved the dichotomy: either $f$ is bounded, or $f(n)\to\infty$. Moreover $f$ bounded would imply $f(n)\le 9$ for all $n$ (Poljak, 1991) — a strong rigidity constraint.

**Shitov's mechanism.** The construction uses a graph $G$ of large girth and large chromatic number together with $H = G^{c}$-type "wide" auxiliaries and the exponential graph $K_n^{H}$. Shitov's key lemma: if $G$ has girth $>g$ and $q$ is large, then the chromatic number of the *fractional-to-integral gap* graph obtained by blowing up $G$ can be controlled, so that $K_n^{H}$ admits a colouring forced by a probabilistic/entropy count on independent sets. The upshot is a pair with
$$\chi(G\times H)\le n < \min\{\chi(G),\chi(H)\}.$$

## 3. History & State of the Art (SOTA)

- **1966** — Stephen T. Hedetniemi states the conjecture in his University of Michigan technical report *Homomorphisms of graphs and automata*.
- **1971–1981** — Trivial case $n=2$ (a product is bipartite iff a factor is). Burr, Erdős and Lovász study related product colourings; Poljak and Rödl introduce $f(n)$ and prove the bounded/unbounded dichotomy.
- **1985** — El-Zahar and Sauer prove the $n=4$ case: the product of two 4-chromatic graphs is 4-chromatic. This remains the largest verified $n$, forty years on.
- **1991** — Poljak shows $f$ bounded $\Rightarrow$ $f(n)\le 9$ eventually; also links to arc-colourings of digraphs.
- **1998–2011** — Tardif proves circular cliques $K_{p/q}$ with $2\le p/q<4$ are multiplicative; Zhu proves the fractional Hedetniemi conjecture (2011). Häggkvist–Hell–Miller–Neumann-Lara and Duffus–Sands–Woodrow give structural criteria.
- **2019 (May)** — **Shitov** disproves the conjecture; counterexamples have chromatic number astronomically large (roughly of order $10^{10000}$ vertices/colours in the original write-up).
- **2019–2021** — Tardif and Zhu extract quantitative corollaries: $f(n)<n$ for all sufficiently large $n$. Zhu constructs "relatively small" counterexamples with $\chi(G)=\chi(H)=125$.
- **2022–2024** — Tardif shows the product of two 14-chromatic graphs can be 13-chromatic — the current record for the smallest known failure.

**SOTA summary:** $f(n)=n$ for $n\le 4$; $f(n)\le n-1$ for $n\ge 14$; the range $5\le n\le 13$ is entirely open.

## 4. Partial Results / Verified Cases

| Regime | Result | Source |
|---|---|---|
| $n=1,2$ | $\chi(G\times H)=\min$ trivially ($K_2$ multiplicative) | folklore |
| $n=3$ | $K_3$ multiplicative | Hedetniemi/El-Zahar–Sauer |
| $n=4$ | Product of two 4-chromatic graphs is 4-chromatic | El-Zahar & Sauer (1985) |
| $5\le n\le 13$ | **Open** — no proof, no counterexample | — |
| $n=14$ | $f(14)\le 13$: counterexample exists | Tardif (2022–23) |
| $n=125$ | Explicit counterexample pair | Zhu (2021) |
| $n$ huge | $f(n)<n$ | Shitov (2019) |
| Fractional | $\chi_f(G\times H)=\min\{\chi_f,\chi_f\}$ — **true** | Zhu (2011) |
| Circular cliques $2\le p/q<4$ | $K_{p/q}$ multiplicative | Tardif |
| Bounded-treewidth / $H$ with a loop, $H$ a path or cycle power | conjecture holds | various |
| Odd cycles $C_{2k+1}$ | multiplicative | Häggkvist–Hell–Miller–Neumann-Lara |

## 5. Principal Obstacles

- **The proof for $n=4$ does not scale.** El-Zahar–Sauer analyse $K_4^{H}$ by hand, using the fact that a 4-chromatic graph contains structurally rigid subgraphs (odd-girth control plus a case analysis on the neighbourhood structure of the exponential graph). The number of cases grows super-exponentially with $n$, and no inductive scheme is known to pass from $n$ to $n+1$.
- **Fractional relaxation is uninformative.** The fractional statement is true, so any LP/flow-based lower bound on $\chi(G\times H)$ cannot exceed $\min\{\chi_f(G),\chi_f(H)\}$ — and the integrality gap $\chi-\chi_f$ can be unbounded (Kneser graphs). Shitov's counterexamples exploit exactly this gap; LP duality, therefore, is structurally incapable of proving the conjecture and equally incapable of pinning down $f$.
- **Topological methods stall.** Lovász-type lower bounds ($\chi \ge \mathrm{conn}(\mathrm{Hom}(K_2,G))+3$) behave badly under $\times$: box complexes of products are not products of box complexes, so no functorial lower bound transfers.
- **Shitov's construction is non-explicit and lossy.** It uses random/large-girth graphs and probabilistic estimates that only bite once parameters are enormous. Pushing it down to $n=5$ requires replacing asymptotic counting with exact combinatorics on small structures — precisely the regime where the counting estimates are vacuous.
- **The bounded/unbounded dichotomy is a genuine trichotomy-free wall.** Deciding whether $f$ is bounded seems to need either an unconditional lower bound $\chi(G\times H)\to\infty$ (no technique known) or a construction with $\chi(G),\chi(H)$ unbounded and $\chi(G\times H)$ fixed (Shitov's gap grows too slowly to test this).

## 6. The Gap

Proven: $f(n)=n$ for $n\le 4$; $f(n)\le n-1$ for $n\ge 14$. General statement (now known false): $f(n)=n$ for all $n$.

The precise remaining boundary has two components.

1. **The threshold.** Determine the least $n_0$ with $f(n_0)<n_0$. Currently $5\le n_0\le 14$. Closing this needs either an El-Zahar–Sauer-style argument for $K_5$ — i.e. showing $\chi(K_5^{H})\le 5$ forces $H\to K_5$ — or a counterexample construction whose parameters survive at $n=5$.
2. **Boundedness.** Decide whether $\sup_n f(n)<\infty$. By Poljak's theorem the answer is either "$f(n)\le 9$ for all $n$" or "$f(n)\to\infty$"; no method currently distinguishes these. Equivalently: is there a fixed $c$ and graphs $G_k,H_k$ with $\chi(G_k),\chi(H_k)\to\infty$ but $\chi(G_k\times H_k)\le c$?

## 7. Current Research (as of June 2026)

- **Quantitative Shitov programme** (Tardif, Zhu, and collaborators in Canada/Taiwan/China). Systematic reduction of counterexample size: $10^{10000}\to 125\to 14$. Further reductions target $n=10$ and below; each step replaces a probabilistic estimate with an explicit gadget. *(frontier — verify)*
- **Growth rate of $n-f(n)$.** Attempts to show the defect is unbounded, which would rule out $f$ being bounded by a fixed small constant in a strong sense. No unconditional result yet.
- **Multiplicativity beyond cliques.** Classifying multiplicative graphs — circular cliques, Kneser graphs, graphs with loops — remains active; the failure for $K_n$ makes the classification question sharper rather than moot.
- **Directed and fractional analogues.** The digraph version (Poljak–Rödl arc-chromatic connection) and generalisations to constraint-satisfaction/homomorphism dualities are studied by the CSP-complexity community (Wrochna, Brandts, Bulín), where "multiplicativity" corresponds to a promise-CSP hardness gadget property. *(frontier — verify)*

## 8. Future Work

- Attack $K_5$ directly via the exponential graph $K_5^{H}$, mirroring El-Zahar–Sauer but with computer-assisted case enumeration on small $H$ of odd girth $\ge 7$.
- Derandomise Shitov's large-girth ingredient using explicit Ramanujan-type or Kneser-type constructions, to control chromatic parameters exactly at small scale.
- Settle Poljak's dichotomy: either construct a family with unbounded factor chromatic numbers and bounded product chromatic number, or prove a lower bound $f(n)\ge g(n)\to\infty$ (even $f(n)\ge 10$ for all large $n$ would refute boundedness).
- Develop lower-bound machinery for $\chi(G\times H)$ that is not fractionally relaxable — e.g. Hom-complex or entropy-based invariants that are multiplicative under $\times$.

## 9. Key References

- **[Foundational]** S. T. Hedetniemi. *Homomorphisms of graphs and automata.* Technical Report 03105-44-T, University of Michigan, 1966.
- **[Foundational]** M. El-Zahar and N. Sauer. *The chromatic number of the product of two 4-chromatic graphs is 4.* Combinatorica **5** (1985), 121–126.
- **[Foundational]** S. Poljak and V. Rödl. *On the arc-chromatic number of a digraph.* Journal of Combinatorial Theory, Series B **31** (1981), 190–198.
- **[Foundational]** S. Poljak. *Coloring digraphs by iterated antichains.* Commentationes Mathematicae Universitatis Carolinae **32** (1991), 209–212.
- **[SOTA]** Y. Shitov. *Counterexamples to Hedetniemi's conjecture.* Annals of Mathematics **190** (2019), 663–667.
- **[SOTA]** X. Zhu. *Relatively small counterexamples to Hedetniemi's conjecture.* Journal of Combinatorial Theory, Series B **146** (2021), 141–150.
- **[SOTA]** C. Tardif. *The chromatic number of the product of 14-chromatic graphs can be 13.* Combinatorica **43** (2023).
- **[Related]** X. Zhu. *The fractional version of Hedetniemi's conjecture is true.* European Journal of Combinatorics **32** (2011), 1168–1175.
- **[Survey]** N. Sauer. *Hedetniemi's conjecture — a survey.* Discrete Mathematics **229** (2001), 261–292.
- **[Survey]** C. Tardif. *Hedetniemi's conjecture, 40 years later.* Graph Theory Notes of New York **54** (2008), 46–57.
- **[Book]** P. Hell and J. Nešetřil. *Graphs and Homomorphisms.* Oxford University Press, 2004.

## 10. Worked Example / Concrete Special Case

**Claim.** $\chi(C_5\times C_7)=3$, consistent with the conjecture at $n=3$.

*Upper bound.* $\chi(C_5)=\chi(C_7)=3$, and the projection $\pi_1:C_5\times C_7\to C_5$ is a homomorphism, so composing with a proper 3-colouring of $C_5$ gives $\chi(C_5\times C_7)\le 3$.

*Lower bound.* Label $V(C_5)=\mathbb{Z}_5$, $V(C_7)=\mathbb{Z}_7$, with $i\sim i\pm 1$ in each factor. Then $(a,b)\sim(a',b')$ iff $a'-a=\pm1$ and $b'-b=\pm1$. Consider the walk that takes $35$ steps, each of the form $(+1,+1)$. After $35$ steps the first coordinate advances by $35\equiv 0 \pmod 5$ and the second by $35\equiv 0\pmod 7$, so this is a **closed walk of length 35**, which is odd. A graph containing a closed odd walk contains an odd cycle, hence is not bipartite, so $\chi\ge 3$. Therefore $\chi(C_5\times C_7)=3=\min\{3,3\}$. ∎

**Why this generalises to $n=2$ and no further.** The $n=2$ case is exactly the observation above run backwards: $G\times H$ is bipartite iff $G$ or $H$ is, because an odd closed walk in $G\times H$ projects to odd closed walks in both factors, and conversely odd closed walks of lengths $p$ (in $G$) and $q$ (in $H$) combine to one of length $pq$ (odd). This argument is a *parity* argument — it has no analogue for $n\ge 3$ because there is no local certificate for $\chi\ge n$ comparable to an odd closed walk.

**Where the conjecture breaks.** Shitov's counterexamples replace the parity certificate with a *counting* one. Take $G$ of large girth with $\chi(G)$ large but $\chi_f(G)$ comparatively small; then $K_n^{G}$ has many "almost proper" maps that can be stitched into an $n$-colouring of $K_n^{G}$ itself, so $K_n^{G}\to K_n$ while $G\not\to K_n$. Setting $H=K_n^{G}$ and using the adjunction $H\times G\to K_n$, one gets $\chi(H\times G)\le n<\min\{\chi(G),\chi(H)\}$. The integrality gap $\chi-\chi_f$ — invisible at $n\le 4$ where the gap is too small — is exactly what kills the conjecture.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*