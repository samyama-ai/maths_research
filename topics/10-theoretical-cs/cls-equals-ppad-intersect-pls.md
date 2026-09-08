---
id: 10-theoretical-cs/cls-equals-ppad-intersect-pls
title: "Continuous Local Search Hardness (CLS = PPAD ∩ PLS)"
topic: 10-theoretical-cs
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Continuous Local Search Hardness (CLS = PPAD ∩ PLS)

> **Topic:** Theoretical Computer Science · **ID:** `10-theoretical-cs/cls-equals-ppad-intersect-pls` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

$\mathrm{CLS}$ (Continuous Local Search) was introduced by Daskalakis and Papadimitriou (SODA 2011) as the total search class capturing "gradient-descent-like" problems: those solvable by continuous local improvement on a bounded domain. It sits inside $\mathrm{PPAD} \cap \mathrm{PLS}$ by definition, and the founding conjecture was that the containment is **strict** — that $\mathrm{CLS}$ is a genuinely smaller, "very low" class, since no complete problem for $\mathrm{PPAD}\cap\mathrm{PLS}$ was known and the two parent classes' existence arguments (parity of degrees vs. monotone potential decrease) appeared incombinable.

The central question:

> Is $\mathrm{CLS} = \mathrm{PPAD} \cap \mathrm{PLS}$, and does the intersection admit natural complete problems?

**Resolved (2021).** Fearnley, Goldberg, Hollender and Savani proved $\mathrm{CLS} = \mathrm{PPAD}\cap\mathrm{PLS}$, exhibiting *finding a fixed point of gradient descent* on a bounded domain as a complete problem. Concurrently Babichenko and Rubinstein proved mixed Nash equilibrium in congestion games is $\mathrm{PPAD}\cap\mathrm{PLS}$-complete. Göös et al. (2022) then collapsed $\mathrm{EOPL}$ into the same class.

**What remains open**, and what this page tracks: (i) whether $\mathrm{UEOPL} = \mathrm{EOPL} = \mathrm{PPAD}\cap\mathrm{PLS}$; (ii) whether $\mathrm{PPAD}\cap\mathrm{PLS} \subsetneq \mathrm{PPAD}$ and $\subsetneq \mathrm{PLS}$ unconditionally (only oracle separations are known); (iii) whether $\mathrm{PPAD}\cap\mathrm{PLS}$-hardness can be based on standard cryptographic assumptions, as $\mathrm{PPAD}$-hardness now is.

## 2. Mathematical Foundations

**TFNP.** A search problem is a relation $R \subseteq \{0,1\}^* \times \{0,1\}^*$ that is polynomially balanced and polynomial-time decidable. It lies in $\mathrm{TFNP}$ if $\forall x\, \exists y : (x,y)\in R$. Reductions are many-one (Karp-style) between search problems.

**PLS** (Johnson–Papadimitriou–Yannakakis, 1988). Complete problem $\textsc{Localopt}$: given circuits $S:\{0,1\}^n \to \{0,1\}^n$ (neighbourhood) and $\Phi:\{0,1\}^n \to \mathbb{Z}$ (potential), find
$$v \in \{0,1\}^n \quad\text{with}\quad \Phi(S(v)) \ge \Phi(v).$$

**PPAD** (Papadimitriou, 1994). Complete problem $\textsc{EndOfLine}$: given $S,P:\{0,1\}^n\to\{0,1\}^n$ with $P(0^n)=0^n \ne S(0^n)$, find $v$ with $P(S(v))\ne v$ or $S(P(v))\ne v \ne 0^n$.

**CLS** (Daskalakis–Papadimitriou, 2011). Complete problem $\textsc{ContinuousLocalopt}$: given $\varepsilon>0$, $\lambda$-Lipschitz arithmetic circuits $f:[0,1]^n\to[0,1]$ and $g:[0,1]^n\to[0,1]^n$, find $x$ with
$$f(g(x)) \ge f(x) - \varepsilon,$$
or two points witnessing violation of the Lipschitz bound.

**Gradient descent as a search problem.** For $f:[0,1]^n\to\mathbb{R}$ given by an arithmetic circuit with $\nabla f$ also given by a circuit, $L$-smooth ($\|\nabla f(x)-\nabla f(y)\|\le L\|x-y\|$), step size $\eta$, define the projected step
$$g_\eta(x) = \Pi_{[0,1]^n}\big(x - \eta \nabla f(x)\big).$$
$\textsc{GD-Local-Search}$: find $x$ with $f(g_\eta(x)) \ge f(x)-\varepsilon$. $\textsc{GD-Fixed-Point}$: find $x$ with $\|g_\eta(x)-x\|\le\varepsilon$.

**KKT.** For $f$ on $[0,1]^n$, an $\varepsilon$-KKT point satisfies: there exist multipliers $\mu_i^-,\mu_i^+\ge 0$ with
$$\big\|\nabla f(x) - \textstyle\sum_i (\mu_i^- - \mu_i^+) e_i \big\| \le \varepsilon, \qquad \mu_i^- x_i = \mu_i^+(1-x_i) = 0 .$$

**Main theorem (Fearnley–Goldberg–Hollender–Savani, STOC 2021; JACM 2023).**
$$\mathrm{CLS} = \mathrm{PPAD}\cap\mathrm{PLS},$$
and $\textsc{GD-Local-Search}$, $\textsc{GD-Fixed-Point}$ and $\textsc{KKT}$ are complete for it, already for $n=2$ (2D domain) and constant $\eta$.

**Line/potential classes.** $\textsc{EndOfPotentialLine}$ combines both: an $\textsc{EndOfLine}$ graph together with a potential $\Phi$ that strictly increases along the line. $\mathrm{EOPL}$ is the class of problems reducible to it; $\mathrm{UEOPL}$ adds a promise of a *unique* line. Fearnley–Gordon–Mehta–Savani (2019) showed $\mathrm{UEOPL}\subseteq\mathrm{EOPL}\subseteq \mathrm{CLS}$. Göös et al. (CCC 2022) proved
$$\mathrm{EOPL} = \mathrm{PLS}\cap\mathrm{PPAD}, \qquad \mathrm{SOPL} = \mathrm{PLS}\cap\mathrm{PPADS},$$
so all four descriptions coincide: $\mathrm{CLS}=\mathrm{EOPL}=\mathrm{PPAD}\cap\mathrm{PLS}$.

## 3. History & State of the Art (SOTA)

- **1988** Johnson, Papadimitriou, Yannakakis define $\mathrm{PLS}$.
- **1991** Megiddo–Papadimitriou define $\mathrm{TFNP}$; **1994** Papadimitriou defines $\mathrm{PPAD}$, $\mathrm{PPA}$, $\mathrm{PPP}$.
- **2011** Daskalakis–Papadimitriou define $\mathrm{CLS}$, conjecture strictness in $\mathrm{PPAD}\cap\mathrm{PLS}$, and place $P$-matrix LCP, Nash for congestion/network-coordination games, and Contraction in it.
- **2017** Hubáček–Yogev: $\mathrm{CLS}$ has query complexity $\tilde\Omega(n^{1.5})$ in the black-box model, and $\mathrm{CLS}$-hardness follows from indistinguishability obfuscation plus one-way functions.
- **2018** Daskalakis–Tzamos–Zampetakis: Banach fixed point with a general metric (the "converse Banach" problem) is $\mathrm{CLS}$-complete — the first natural $\mathrm{CLS}$-complete problem.
- **2019** Fearnley–Gordon–Mehta–Savani introduce $\mathrm{EOPL}$/$\mathrm{UEOPL}$; Unique Sink Orientation, P-LCP and simple stochastic games land in $\mathrm{UEOPL}$.
- **2021** *The collapse.* Fearnley–Goldberg–Hollender–Savani: $\mathrm{CLS}=\mathrm{PPAD}\cap\mathrm{PLS}$ via gradient descent. Babichenko–Rubinstein: mixed Nash in congestion games is $\mathrm{PPAD}\cap\mathrm{PLS}$-complete. Daskalakis–Skoulakis–Zampetakis: approximate first-order local min-max on a bounded domain is $\mathrm{PPAD}\cap\mathrm{PLS}$-complete.
- **2022** Göös–Hollender–Jain–Maystre–Pires–Robere–Tao: $\mathrm{EOPL}=\mathrm{PLS}\cap\mathrm{PPAD}$, $\mathrm{SOPL}=\mathrm{PLS}\cap\mathrm{PPADS}$, with matching black-box separations.
- **2024** Fearnley–Goldberg–Hollender–Savani: computing an $\varepsilon$-KKT point of a *quadratic* program over a polytope is $\mathrm{PPAD}\cap\mathrm{PLS}$-complete — hardness survives degree-2 objectives.

## 4. Partial Results / Verified Cases

Concrete parameter regimes where completeness (i.e. $\mathrm{PPAD}\cap\mathrm{PLS}$-hardness) is established:

- **Dimension $n=2$.** $\textsc{GD-Local-Search}$ on $[0,1]^2$ with an explicitly given $O(1)$-smooth $f$, step size $\eta$ constant, $\varepsilon$ inverse-polynomial: hard (FGHS 2021). In dimension $n=1$ the problem is in $\mathrm{FP}$ by binary search on $f'$.
- **Degree 2.** $\varepsilon$-KKT for $f(x)=\tfrac12 x^\top Q x + b^\top x$ over $\{Ax\le c\}$, $Q$ indefinite: complete (FGHS 2024). For $Q\succeq 0$ (convex QP) the problem is in $\mathrm{FP}$ (ellipsoid/interior point).
- **Games.** Mixed Nash in congestion games with $n$ players; $\varepsilon$-Nash in network-coordination games; both complete.
- **Min-max.** $\varepsilon$-first-order local min-max for $\min_x\max_y f(x,y)$ on $[0,1]^{n}\times[0,1]^{m}$ with $\varepsilon = 1/\mathrm{poly}$: complete (DSZ 2021).
- **Fixed points.** Contraction maps in arbitrary (circuit-given) metrics: complete; contraction in $\ell_\infty$ or $\ell_2$ with known modulus: in $\mathrm{FP}$ (Shellman–Sikorski style bisection for $\ell_\infty$).
- **Inside the class, still not known complete:** P-matrix LCP, simple stochastic games, unique sink orientation, parity games — all in $\mathrm{UEOPL}$, none $\mathrm{PPAD}\cap\mathrm{PLS}$-hard.
- **Black-box separations verified:** relative to an oracle, $\mathrm{PLS}\not\subseteq\mathrm{PPAD}$, $\mathrm{PPAD}\not\subseteq\mathrm{PLS}$ (Beame et al. 1998), and $\mathrm{SOPL}\subsetneq\mathrm{EOPL}$ (Göös et al. 2022).

## 5. Principal Obstacles

- **Why strictness was believed, and why intuition failed.** The parity argument of $\mathrm{PPAD}$ is non-monotone; the potential argument of $\mathrm{PLS}$ is monotone but non-local. Combining them was thought to require a single object carrying both, which appeared to over-constrain the instance. FGHS defeated this by encoding an $\textsc{EndOfLine}$ line *geometrically* in $[0,1]^2$ and using the surrounding potential landscape to make gradient descent trace it — a construction with no analogue in higher-level classes.
- **No unconditional separations.** Every $\mathrm{TFNP}$ subclass separation known is *relativized* or *proof-complexity-theoretic*. An unconditional $\mathrm{PPAD}\cap\mathrm{PLS}\ne\mathrm{PLS}$ would imply $\mathrm{P}\ne\mathrm{NP}$, so the entire landscape is conditional. Black-box lower bounds (query/communication, via the Göös et al. lifting from Nullstellensatz/resolution degree) cannot transfer to the white-box setting.
- **Cryptographic hardness is one-sided.** $\mathrm{PPAD}$-hardness now follows from sub-exponential LWE via Fiat–Shamir/SNARGs (Choudhuri et al. 2019; Jawale–Kalai–Khurana–Zhang 2021). No such route exists for $\mathrm{PLS}$ — the potential's monotonicity has no known cryptographic instantiation — so $\mathrm{PPAD}\cap\mathrm{PLS}$-hardness rests on obfuscation-strength assumptions (Hubáček–Yogev), not standard ones.
- **The uniqueness promise.** $\mathrm{UEOPL}$'s promise of a unique line kills the standard "many lines" gadgets used in $\mathrm{PPAD}$ hardness. No technique produces hardness for a promise class of this shape without either breaking the promise or assuming worst-case-to-promise transfer.

## 6. The Gap

Proven: $\mathrm{CLS}=\mathrm{EOPL}=\mathrm{PPAD}\cap\mathrm{PLS}$, with 2D gradient descent and indefinite-QP KKT complete. The gap has three precise components.

1. **$\mathrm{UEOPL}$ vs. $\mathrm{EOPL}$.** Is the uniqueness promise strictly weakening? Equivalently: is $\textsc{EndOfPotentialLine}$ reducible to its unique-line variant? A positive answer would make P-LCP, simple stochastic games and parity games $\mathrm{PPAD}\cap\mathrm{PLS}$-complete, effectively ruling out polynomial-time algorithms for them under standard $\mathrm{TFNP}$ beliefs. Currently only an oracle separation of $\mathrm{UEOPL}$ from $\mathrm{EOPL}$ is sought and unresolved.
2. **Hardness from standard assumptions.** Bridge the gap between "PPAD-hard from sub-exponential LWE" and "PPAD∩PLS-hard from iO". Missing ingredient: a cryptographic object whose security reduces to finding a local optimum of a monotone potential.
3. **Structure above the collapse.** Is $\mathrm{PPAD}\cap\mathrm{PLS}$ closed under Turing reductions? Does it equal its own "unique-solution" variant? These are open even relative to oracles.

## 7. Current Research (as of June 2026)

- **Oxford / EPFL / Liverpool (Hollender, Goldberg, Savani, Fearnley).** Extending the gradient-descent completeness programme to structured objectives: after the 2024 quadratic-program result, the target is KKT hardness under *sparsity* or *low-rank* restrictions on $Q$, and hardness for second-order stationary points. *(frontier — verify)*
- **Proof complexity route (Göös, Robere, Pitassi, and collaborators).** Characterizing $\mathrm{TFNP}$ subclasses by propositional proof systems: $\mathrm{PLS} \leftrightarrow$ resolution, $\mathrm{PPADS} \leftrightarrow$ unary Nullstellensatz, $\mathrm{EOPL} \leftrightarrow$ "reversible resolution". Separating $\mathrm{UEOPL}$ would follow from an appropriate proof-system separation. *(frontier — verify)*
- **MIT / Berkeley (Daskalakis, Rubinstein, Zampetakis).** $\mathrm{PPAD}\cap\mathrm{PLS}$ as the right home for min-max and GAN-style equilibrium computation; extending completeness to constrained min-max with smoothness and to online learning dynamics.
- **Cryptography-meets-TFNP.** Post-2021 work on SNARGs for $\mathrm{P}$ has made $\mathrm{PPAD}$-hardness standard-assumption-based; several groups are attempting the $\mathrm{PLS}$ analogue via incrementally verifiable computation over monotone tapes. *(frontier — verify)*

## 8. Future Work

- Settle $\mathrm{UEOPL}$ vs. $\mathrm{EOPL}$ in the black-box model first; a query separation would be strong evidence and is the stated next step in Fearnley–Gordon–Mehta–Savani and Göös et al.
- Find a *natural* $\mathrm{UEOPL}$-complete problem other than $\textsc{UniqueEOPL}$ itself; P-LCP is the prime candidate.
- Determine the exact dimension/smoothness threshold: gradient descent is in $\mathrm{FP}$ for $n=1$ and hard for $n=2$; what happens for $n=2$ with $\eta$ super-polynomially small, or with $f$ given by a polynomial of bounded degree and bounded coefficient size?
- Base $\mathrm{PLS}$-hardness on a falsifiable assumption, thereby making $\mathrm{PPAD}\cap\mathrm{PLS}$-hardness cryptographically standard.
- Map the classes above: is $\mathrm{PPAD}\cap\mathrm{PPP}$ or $\mathrm{PLS}\cap\mathrm{PPP}$ also equal to a natural "line-plus-potential" class?

## 9. Key References

- **[Foundational]** D. Johnson, C. Papadimitriou, M. Yannakakis. *How easy is local search?* Journal of Computer and System Sciences, 37(1):79–100, 1988.
- **[Foundational]** C. Papadimitriou. *On the complexity of the parity argument and other inefficient proofs of existence.* JCSS, 48(3):498–532, 1994.
- **[Foundational]** N. Megiddo, C. Papadimitriou. *On total functions, existence theorems and computational complexity.* Theoretical Computer Science, 81(2):317–324, 1991.
- **[Foundational]** C. Daskalakis, C. Papadimitriou. *Continuous Local Search.* SODA 2011, pp. 790–804.
- **[SOTA]** J. Fearnley, P. Goldberg, A. Hollender, R. Savani. *The Complexity of Gradient Descent: CLS = PPAD ∩ PLS.* STOC 2021; Journal of the ACM, 70(1), Article 7, 2023.
- **[SOTA]** Y. Babichenko, A. Rubinstein. *Settling the complexity of Nash equilibrium in congestion games.* STOC 2021.
- **[SOTA]** M. Göös, A. Hollender, S. Jain, G. Maystre, W. Pires, R. Robere, R. Tao. *Further Collapses in TFNP.* CCC 2022.
- **[SOTA]** J. Fearnley, P. Goldberg, A. Hollender, R. Savani. *The Complexity of Computing KKT Solutions of Quadratic Programs.* STOC 2024.
- **[Recent]** C. Daskalakis, S. Skoulakis, M. Zampetakis. *The complexity of constrained min-max optimization.* STOC 2021.
- **[Recent]** C. Daskalakis, C. Tzamos, M. Zampetakis. *A converse to Banach's fixed point theorem and its CLS completeness.* STOC 2018.
- **[Recent]** J. Fearnley, S. Gordon, R. Mehta, R. Savani. *Unique End of Potential Line.* ICALP 2019; JCSS, 114:1–35, 2020.
- **[Recent]** P. Hubáček, E. Yogev. *Hardness of continuous local search: query complexity and cryptographic lower bounds.* SODA 2017; SIAM Journal on Computing, 49(6):1128–1172, 2020.
- **[Recent]** A. R. Choudhuri, P. Hubáček, C. Kamath, K. Pietrzak, A. Rosen, G. Rothblum. *Finding a Nash equilibrium is no easier than breaking Fiat-Shamir.* STOC 2019.
- **[Separations]** P. Beame, S. Cook, J. Edmonds, R. Impagliazzo, T. Pitassi. *The relative complexity of NP search problems.* JCSS, 57(1):3–19, 1998.
- **[Survey]** A. Hollender. *Structural Results for Total Search Complexity Classes with Applications to Game Theory and Optimization.* PhD thesis, University of Oxford, 2021.

## 10. Worked Example / Concrete Special Case

**A 3-bit $\textsc{EndOfPotentialLine}$ instance.** Vertices $V=\{0,\dots,7\}$ encoded in 3 bits. Define successor $S$ and predecessor $P$ by:

| $v$ | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|---|
| $S(v)$ | 1 | 3 | 2 | 4 | 4 | 6 | 6 | 7 |
| $P(v)$ | 0 | 0 | 2 | 1 | 3 | 5 | 5 | 7 |
| $\Phi(v)$ | 0 | 1 | 0 | 2 | 3 | 5 | 6 | 0 |

Edges are the pairs with $S(u)=v$ **and** $P(v)=u$: $0\to1\to3\to4$ and $5\to6$. Self-loops at $2$ and $7$ are isolated vertices.

*PPAD view.* The standard source is $0$ (with $P(0)=0\ne S(0)$). Following the line: $0\to1\to3\to4$, and $S(4)=4$, so $4$ is a sink — a valid $\textsc{EndOfLine}$ solution. The vertex $6$ is also a sink but of a *second* line whose source is $5$; both are $\textsc{EndOfPotentialLine}$ solutions.

*PLS view.* $\Phi$ strictly increases along each edge: $0<1<2<3$ on the main line, $5<6$ on the second. A vertex with $\Phi(S(v))\le\Phi(v)$ is a local optimum: $v=4$ gives $\Phi(S(4))=\Phi(4)=3$. ✔

So the *same* witness $v=4$ certifies both the parity argument and the potential argument. That coincidence is the whole content of $\mathrm{EOPL}$, and Göös et al. proved it is not a loss of generality: any problem in $\mathrm{PPAD}\cap\mathrm{PLS}$ — a problem with two *independent* proofs of totality — can be re-encoded so that a single line-with-potential carries both.

**The continuous shadow.** FGHS realize this line inside $[0,1]^2$. Take $\eta=\varepsilon=1/100$ and a smooth $f:[0,1]^2\to\mathbb{R}$ that is a "valley" whose floor follows the polyline $0\to1\to3\to4$ drawn as a path in the square, with $f$ decreasing by a fixed $\delta>0$ per unit length along the floor and steeply increasing transversally. Starting at the point encoding vertex $0$, projected gradient descent $x_{t+1}=\Pi_{[0,1]^2}(x_t-\eta\nabla f(x_t))$ slides down the valley and can only stall where the floor stops — the image of vertex $4$. Concretely, at an interior floor point $x$ with $\nabla f(x)=(-\delta,0)$ and $\delta=1$, one step gives $f(g_\eta(x))-f(x)\approx -\eta\|\nabla f\|^2=-10^{-2} < -\varepsilon$, so $x$ is *not* a solution; at the endpoint $\nabla f\approx 0$ and $f(g_\eta(x))\ge f(x)-\varepsilon$ holds. Hence any $\varepsilon$-approximate stall point of gradient descent decodes to an end-of-potential-line solution, and $\textsc{EndOfPotentialLine} \le_p \textsc{GD-Local-Search}$ — the reduction underlying $\mathrm{CLS}=\mathrm{PPAD}\cap\mathrm{PLS}$.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*