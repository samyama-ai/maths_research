---
id: 10-theoretical-cs/orthogonal-vectors-conjecture
title: "Orthogonal Vectors Conjecture"
topic: 10-theoretical-cs
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Orthogonal Vectors Conjecture

> **Topic:** Theoretical Computer Science · **ID:** `10-theoretical-cs/orthogonal-vectors-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

The **Orthogonal Vectors** problem (OV) is: given two sets $A, B \subseteq \{0,1\}^d$ with $|A| = |B| = n$, decide whether there exist $a \in A$, $b \in B$ with
$$\langle a, b\rangle \;=\; \sum_{k=1}^{d} a_k b_k \;=\; 0 \quad \text{(over } \mathbb{Z}\text{)}.$$

Brute force takes $O(n^2 d)$ time.

**Orthogonal Vectors Conjecture (OVC).** For every $\varepsilon > 0$ there is no randomized algorithm solving OV in time
$$O\!\left(n^{2-\varepsilon}\,\mathrm{poly}(d)\right)$$
on instances with $d = n^{o(1)}$.

**Low-dimensional variant (LDOVC).** For every $\varepsilon > 0$ there exists $c = c(\varepsilon)$ such that OV with $d = c\log n$ requires $n^{2-\varepsilon}$ time. LDOVC implies OVC; the converse is not known.

A **disproof** requires an algorithm running in $n^{2-\varepsilon}\mathrm{poly}(d)$ for some fixed $\varepsilon > 0$ and all $d = n^{o(1)}$ (equivalently, by the reduction of Section 2, refuting SETH would be a consequence). A **proof** requires an unconditional $n^{2-o(1)}$ time lower bound in a general model (word RAM with $O(\log n)$-bit words), which would imply $\mathrm{P} \neq \mathrm{NP}$-scale separations far beyond current techniques. The realistic target is therefore *conditional* resolution: proving OVC equivalent to, or strictly weaker than, other fine-grained hypotheses.

## 2. Mathematical Foundations

**Boolean encoding.** For $a,b \in \{0,1\}^d$, $\langle a,b\rangle = 0$ iff $\mathrm{supp}(a) \cap \mathrm{supp}(b) = \emptyset$, so OV is *Set Disjointness search*: is there a disjoint pair between two families of subsets of $[d]$? Equivalently, with $\bar b$ the complement,
$$\exists a,b:\ \prod_{k=1}^{d}\bigl(1 - a_k b_k\bigr) = 1 \iff \exists a, b:\ \mathrm{supp}(a)\subseteq \mathrm{supp}(\bar b).$$

**$k$-OV.** Given $k$ sets $A_1,\dots,A_k \subseteq \{0,1\}^d$ of size $n$, decide whether $\exists a^{(1)},\dots,a^{(k)}$ with $\sum_{j=1}^{d}\prod_{i=1}^{k} a^{(i)}_j = 0$. The $k$-OV conjecture asserts no $O(n^{k-\varepsilon}\mathrm{poly}(d))$ algorithm.

**SETH.** Let $s_k = \inf\{\delta : k\text{-SAT} \in \mathrm{TIME}(2^{\delta n})\}$. The Strong Exponential Time Hypothesis (Impagliazzo–Paturi 2001) states $\lim_{k\to\infty} s_k = 1$.

**Theorem (Williams 2005).** SETH $\Rightarrow$ OVC, and more precisely $\Rightarrow$ LDOVC.

*Proof sketch.* Given a $k$-CNF $\varphi$ on $N$ variables with $m$ clauses, apply the **Sparsification Lemma** (Impagliazzo–Paturi–Zane 2001): for every $\mu > 0$, $\varphi$ is equivalent to an OR of $2^{\mu N}$ $k$-CNFs each with $m' = O(N)$ clauses, computable in $2^{\mu N}\mathrm{poly}(N)$ time. Split the variables into halves $X_1, X_2$ of size $N/2$. For each of the $n = 2^{N/2}$ assignments $\alpha$ to $X_1$, build $a_\alpha \in \{0,1\}^{m'}$ with $(a_\alpha)_j = 1$ iff $\alpha$ does *not* satisfy clause $C_j$; similarly $b_\beta$ for $X_2$. Then $\langle a_\alpha, b_\beta\rangle = 0$ iff every clause is satisfied by $\alpha \cup \beta$. Hence an $O(n^{2-\varepsilon}\mathrm{poly}(d))$ OV algorithm with $d = m' = O(N) = c\log n$ yields $k$-SAT in $2^{(1-\varepsilon/2+\mu)N}$ time for all $k$, refuting SETH. $\square$

**Polynomial method.** Razborov–Smolensky probabilistic polynomials over $\mathbb{F}_2$ compute $\mathrm{OR}_s$ with error $1/3$ in degree $O(\log s)$; composing with the degree-$d$ AND gives, for the "batched" OV predicate on $s$ pairs, a probabilistic polynomial of degree $O(\sqrt{d\log s})$ and sparsity $\binom{O(d)}{O(\sqrt{d \log s})}$. Evaluating it on all $n^2/s^2$ blocks reduces to rectangular matrix multiplication, which by Coppersmith's bound runs in $N^{2+o(1)}$ time when the inner dimension is $N^{0.17}$.

## 3. History & State of the Art

- **2001** — IPZ sparsification lemma and the formalization of SETH provide the two ingredients for fine-grained reductions.
- **2005** — R. Williams isolates OV (as "2-constraint CSP with a sparse structure") and proves SETH $\Rightarrow$ OVC. This is the origin of the conjecture.
- **2013–2015** — OV becomes the central hub of fine-grained complexity. SETH/OV-based quadratic lower bounds are proved for graph diameter (Roditty–Vassilevska Williams, STOC 2013), discrete Fréchet distance (Bringmann, FOCS 2014), edit distance (Backurs–Indyk, STOC 2015), LCS and dynamic time warping (Bringmann–Künnemann, FOCS 2015; Abboud–Backurs–Vassilevska Williams, FOCS 2015), regular expression matching, and many dynamic and streaming problems.
- **2015** — Abboud, Williams and Yu (SODA 2015) give the best known upper bound: OV with $d = c\log n$ in randomized time
  $$n^{2 - 1/O(\log c)}.$$
  This is $n^{2-o(1)}$ for $c = \omega(1)$, hence consistent with OVC, but it rules out any $n^2$-type lower bound proof that ignores dimension.
- **2016** — Chan and Williams (SODA 2016) derandomize Razborov–Smolensky and obtain the same bound deterministically.
- **2017** — Gao, Impagliazzo, Kolokolova and Williams show $k$-OV is *complete* for model-checking first-order properties: every FO property with $k+1$ quantifiers on sparse structures is solvable in $\tilde O(m^k)$ and is $k$-OV-hard.
- **2019** — Chen and Williams (SODA 2019) exhibit a nontrivial **equivalence class** for OV, showing OVC equivalent to subquadratic hardness of e.g. approximate Min-IP/Max-IP and sparse OV.
- **2019** — Kane and Williams prove unconditional near-quadratic lower bounds for OV in restricted models (certain branching programs and formulas), the first "OVC theorems" in any nontrivial model.

## 4. Partial Results / Verified Cases

- **Constant or tiny dimension.** For $d = O(1)$, or more generally $d \le \frac{\log n}{10\log\log n}$, OV is solvable in $O(n\,d + 2^d d)= n^{1+o(1)}$ time by the subset-sum (fast zeta/Möbius) transform of Section 10. So OVC is *false* below the $\Theta(\log n)$ threshold; the conjecture concerns $d = \omega(\log n)$.
- **$d = c\log n$, fixed $c$.** Solved in $n^{2-1/O(\log c)}$ time (Abboud–Williams–Yu 2015; deterministic: Chan–Williams 2016). For any fixed $c$ this is truly subquadratic, so only the $c \to \infty$ limit is open.
- **Sparse vectors.** If every $a \in A$ has $\|a\|_0 \le t$, OV is solvable in $\tilde O(n 2^{t})$ time; more sharply, sparse OV with $m = n\log^{O(1)}n$ total ones is subquadratic-equivalent to general OV (Chen–Williams 2019).
- **Geometric/real analogues.** Over $\mathbb{R}^d$ with $d$ constant, the analogous "is some point below some hyperplane" (Hopcroft's problem) is solvable in $O(n^{4/3})$ time for $d=2$ (Chan), far below quadratic — the hardness is genuinely a $d = \omega(\log n)$ phenomenon.
- **Restricted models.** Kane–Williams (ITCS 2019) prove $n^{2-o(1)}$-type size lower bounds for OV on restricted branching-program and formula models, i.e., OVC holds unconditionally in those models.
- **Conditional status.** OVC is implied by SETH; it is *not known* to imply SETH. Under NSETH (Carmosino et al. 2016), a deterministic fine-grained reduction from OV back to SAT is ruled out for several natural formats.

## 5. Principal Obstacles

- **No unconditional superlinear lower bounds.** Proving OVC outright means an $n^{2-o(1)}$ time lower bound for an explicit problem in $\mathrm{P}$ on a general RAM. No technique gives even $\omega(n\log n)$ for any problem in $\mathrm{NP}$ in that model; this is the same wall as $\mathrm{P}$ vs $\mathrm{NP}$-style separations.
- **Algorithmic barriers to disproof.** The polynomial method already extracts subquadratic savings; the savings decay as $1/\log c$ because the Razborov–Smolensky degree $O(\sqrt{d\log s})$ forces the block size $s$ to shrink exponentially in $d/\log n$. Beating this requires probabilistic polynomials of degree $o(\sqrt{d\log s})$ for $\mathrm{OR}$-of-$\mathrm{AND}$s, which is **impossible**: the degree bound is tight (Aspnes–Beigel–Furst–Rudich / Razborov lower bounds for approximate degree of OR). Any refutation must abandon the polynomial route.
- **Communication-complexity obstruction.** OV is exactly a search version of Set Disjointness, whose randomized communication complexity is $\Theta(d)$ (Kalyanasundaram–Schnitger; Razborov). Every known subquadratic technique (hashing, dimension reduction, LSH, sketching) implicitly compresses $b$ below $\Theta(d)$ bits and therefore cannot certify orthogonality exactly — this kills all metric-embedding and nearest-neighbour approaches, which succeed only for *approximate* inner products.
- **Consequence barrier.** By Abboud–Hansen–Vassilevska Williams–Williams (STOC 2016), sufficiently strong improvements for OV-hard string problems would imply $\mathrm{NEXP} \not\subseteq \mathrm{NC}^1$-type circuit lower bounds. So a disproof of OVC via those routes is at least as hard as an open circuit lower bound.
- **No reduction back.** Because OVC is not known to imply SETH, one cannot transfer intuition or partial progress about $k$-SAT to OV; OVC sits strictly between "obviously true" and "provably equivalent to a studied hypothesis".

## 6. The Gap

Known: OV in dimension $d = c\log n$ takes at most $n^{2-1/O(\log c)}$ time. Conjectured: for every $\varepsilon$ there is $c$ with lower bound $n^{2-\varepsilon}$. The gap is the *rate of decay in $c$*. Both sides are consistent with the truth being $n^{2 - 1/\Theta(\log c)}$; the conjecture only asserts the exponent savings tend to $0$, and the algorithm shows they do so at rate at most $1/\log c$. The concrete open step is either:

1. an algorithm with savings **independent of $c$**, i.e. $n^{2-\varepsilon}$ for $d = n^{o(1)}$ (refutes OVC, and by Section 2 refutes SETH); or
2. a *fine-grained equivalence* OVC $\Leftrightarrow$ SETH, closing the one-directional implication of Williams 2005.

Direction (2) is the live target: Chen–Williams 2019 enlarged OV's equivalence class but did not reach SETH, and NSETH-type results suggest natural deterministic reductions from OV to CNF-SAT would themselves have unlikely consequences.

## 7. Current Research (as of June 2026)

- **Equivalence classes and completeness.** Extending Chen–Williams to pull more problems (Max-IP approximation, bichromatic closest pair, sparse graph diameter) into an OV-equivalent class. Groups: MIT (V. Vassilevska Williams, R. Williams' school), Weizmann/Tel Aviv (Abboud, Rubinstein), MPI-INF Saarbrücken (Bringmann, Künnemann).
- **Distributed PCPs and hardness of approximation in P.** Abboud–Rubinstein–Williams' framework continues to yield OV-based inapproximability, e.g. for Max-IP and closest pair; ongoing work seeks approximation-resistance results matching the exact-OV threshold. *(frontier — verify)*
- **Quantum OV.** Grover-type search gives $\tilde O(n\sqrt{d})$ for the decision version on quantum RAM; the "quantum OVC" — no $n^{1-\varepsilon}$ quantum algorithm — is used to derive quantum fine-grained lower bounds (Aaronson–Chia–Lin–Wang–Zhang, Buhrman–Patro–Speelman). Current work asks whether quantum OVC follows from quantum SETH. *(frontier — verify)*
- **Derandomization and circuit connections.** Chan–Williams-style derandomization is being pushed toward $k$-OV and toward the "shaving logs" regime linked to Formula-SAT algorithms (Abboud–Bringmann).
- **Average-case and structured OV.** Study of OV on random instances with planted orthogonal pairs, and on vectors with bounded VC dimension or low-rank structure, where subquadratic algorithms do exist.

## 8. Future Work

- Prove or refute LDOVC $\Rightarrow$ SETH; a proof would collapse the fine-grained landscape's two main hypotheses into one.
- Establish OVC unconditionally in richer restricted models than Kane–Williams: general branching programs, $\mathrm{AC}^0$ with a few majority gates, or algebraic decision trees of bounded degree.
- Determine the true dependence on $c$: is $n^{2-\Theta(1/\log c)}$ optimal? Even an $n^{2-1/O(\sqrt{\log c})}$ improvement would be structurally new.
- Settle $k$-OV for $k \ge 3$: current algorithms give $n^{k-1/O(\log c)}$; a genuine separation between $k$-OV and $k$-SAT hardness is open.
- Extend the polynomial method past its approximate-degree barrier — e.g. via polynomials over rings $\mathbb{Z}_m$ with composite $m$, where no matching degree lower bounds are known.

## 9. Key References

- **[Foundational]** R. Williams. *A new algorithm for optimal 2-constraint satisfaction and its implications.* Theoretical Computer Science 348(2–3): 357–365, 2005.
- **[Foundational]** R. Impagliazzo, R. Paturi, F. Zane. *Which problems have strongly exponential complexity?* Journal of Computer and System Sciences 63(4): 512–530, 2001.
- **[Foundational]** R. Impagliazzo, R. Paturi. *On the complexity of $k$-SAT.* Journal of Computer and System Sciences 62(2): 367–375, 2001.
- **[SOTA]** A. Abboud, R. Williams, H. Yu. *More applications of the polynomial method to algorithm design.* SODA 2015, pp. 218–230.
- **[SOTA]** T. M. Chan, R. Williams. *Deterministic APSP, orthogonal vectors, and more: quickly derandomizing Razborov–Smolensky.* SODA 2016, pp. 1246–1255.
- **[SOTA]** L. Chen, R. Williams. *An equivalence class for orthogonal vectors.* SODA 2019, pp. 21–40.
- **[SOTA]** D. M. Kane, R. Williams. *The orthogonal vectors conjecture for branching programs and formulas.* ITCS 2019, art. 48.
- **[Applications]** A. Backurs, P. Indyk. *Edit distance cannot be computed in strongly subquadratic time (unless SETH is false).* STOC 2015, pp. 51–58.
- **[Applications]** K. Bringmann. *Why walking the dog takes time: Fréchet distance has no strongly subquadratic algorithms unless SETH fails.* FOCS 2014, pp. 661–670.
- **[Applications]** K. Bringmann, M. Künnemann. *Quadratic conditional lower bounds for string problems and dynamic time warping.* FOCS 2015, pp. 79–97.
- **[Completeness]** J. Gao, R. Impagliazzo, A. Kolokolova, R. Williams. *Completeness for first-order properties on sparse structures with algorithmic applications.* ACM Transactions on Algorithms 15(2), 2019 (prelim. SODA 2017).
- **[Barriers]** M. Carmosino, J. Gao, R. Impagliazzo, I. Mihajlin, R. Paturi, S. Schneider. *Nondeterministic extensions of the strong exponential time hypothesis and consequences for non-reducibility.* ITCS 2016, pp. 261–270.
- **[Barriers]** A. Abboud, T. D. Hansen, V. Vassilevska Williams, R. Williams. *Simulating branching programs with edit distance and friends.* STOC 2016, pp. 375–388.
- **[Survey]** V. Vassilevska Williams. *On some fine-grained questions in algorithms and complexity.* Proceedings of the ICM 2018, Vol. 3, pp. 3447–3487.
- **[Survey]** K. Bringmann. *Fine-grained complexity theory (tutorial).* STACS 2019, art. 4.

## 10. Worked Example / Concrete Special Case

Take $n = 4$, $d = 3$, writing vectors as bit strings $(v_1v_2v_3)$:
$$A = \{110,\; 011,\; 101,\; 111\}, \qquad B = \{001,\; 100,\; 010,\; 111\}.$$

**Brute force ($16$ inner products).** $\langle 110, 001\rangle = 0$ — orthogonal. So the answer is YES, witnessed by $(110, 001)$. Note $\langle 111, b\rangle \ge 1$ for all $b \ne 0$, and $\langle a, 111\rangle \ge 1$ for all $a \neq 0$, so the last elements never participate.

**Subset-sum algorithm ($O(2^d d + nd)$).** Identify $v$ with $\mathrm{supp}(v) \subseteq \{1,2,3\}$. Define
$$f(S) \;=\; \\#\{a \in A : \mathrm{supp}(a) \subseteq S\}.$$
Base counts $g(S) = \\#\{a \in A : \mathrm{supp}(a) = S\}$: $g(\{1,2\}) = g(\{2,3\}) = g(\{1,3\}) = g(\{1,2,3\}) = 1$, all other $g = 0$. The fast zeta transform ($d$ passes, one per coordinate) gives
$$f(\emptyset)=f(\{1\})=f(\{2\})=f(\{3\})=0,\quad f(\{1,2\})=f(\{1,3\})=f(\{2,3\})=1,\quad f(\{1,2,3\})=4.$$
Now for each $b \in B$ evaluate $f\bigl(\overline{\mathrm{supp}(b)}\bigr)$, the number of $a$'s orthogonal to $b$:

| $b$ | $\mathrm{supp}(b)$ | complement | $f(\cdot)$ |
|---|---|---|---|
| $001$ | $\{3\}$ | $\{1,2\}$ | $1$ |
| $100$ | $\{1\}$ | $\{2,3\}$ | $1$ |
| $010$ | $\{2\}$ | $\{1,3\}$ | $1$ |
| $111$ | $\{1,2,3\}$ | $\emptyset$ | $0$ |

Total orthogonal pairs $= 3$, matching direct enumeration: $(110,001), (011,100), (101,010)$. Cost: $O(2^3\cdot 3 + 4\cdot 3) = O(36)$ operations instead of $O(n^2 d) = O(48)$ — and in general $O(2^d d + nd)$, which is $n^{1+o(1)}$ whenever $d \le \frac{\log n}{10\log\log n}$. This is exactly why OVC is a statement about $d = \omega(\log n)$: the $2^d$ table blows past $n^2$ precisely at the threshold where the conjecture begins to bite.

**Link to SAT.** Read the same instance backwards through Section 2: with $d = 3$ clauses and $N/2 = 2$ variables per side, $a_\alpha$ records which clauses $\alpha$ fails. The pair $(110, 001)$ says $\alpha$ satisfies clause $3$ only, $\beta$ satisfies clauses $1,2$ — together they satisfy $\varphi$. A subquadratic OV algorithm at $d = c\log n$ would therefore solve $k$-SAT in $2^{(1-\delta)N}$ time for every $k$, refuting SETH.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*