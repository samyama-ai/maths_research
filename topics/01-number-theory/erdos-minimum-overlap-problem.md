---
id: 01-number-theory/erdos-minimum-overlap-problem
title: "Erdos Minimum Overlap Problem"
topic: 01-number-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Erdős Minimum Overlap Problem

> **Topic:** Number Theory · **ID:** `01-number-theory/erdos-minimum-overlap-problem` · **Status:** open

## 1. Problem Statement / Conjecture

Split the first $2n$ positive integers into two blocks of equal size. However you do it, some translate of one block must overlap the other block a lot. The problem is to determine exactly how little overlap is forced.

Formally: let $A \subseteq \{1,2,\dots,2n\}$ with $|A| = n$ and $B = \{1,\dots,2n\} \setminus A$, so $|B| = n$. For $k \in \mathbb{Z}$ define the **overlap function**

$$M_k(A) \;=\; \\#\{(a,b) \in A \times B \;:\; a - b = k\} \;=\; \\#\big( A \cap (B+k) \big).$$

Set

$$M(n) \;=\; \min_{\substack{A \subseteq \{1,\dots,2n\} \\ |A| = n}} \; \max_{k \in \mathbb{Z}} \; M_k(A).$$

Erdős (1955) asked for the asymptotic behaviour of $M(n)$. It is known that

$$c \;=\; \lim_{n \to \infty} \frac{M(n)}{n}$$

exists (Haugland, 1996). **The open problem is to determine $c$** — ideally in closed form, and at minimum to decide whether $c$ is rational, algebraic, or has a description as the value of an explicit extremal variational problem. A complete solution is an exact evaluation of $c$ with proof, together with a description of the (asymptotically) extremal splittings.

Current status: $0.379005 < c < 0.380927$ (Haugland, 2016). No closed form is known or conjectured.

## 2. Mathematical Foundations

**Counting identity.** Since every pair $(a,b) \in A \times B$ has exactly one difference,

$$\sum_{k \in \mathbb{Z}} M_k(A) \;=\; |A|\,|B| \;=\; n^2 ,$$

and $M_k = 0$ unless $|k| \le 2n-1$, so $k$ ranges over $4n-1$ values.

**Support bound.** For fixed $k$, a contributing pair is $(b+k, b)$ with $b, b+k \in \{1,\dots,2n\}$, hence

$$M_k(A) \;\le\; 2n - |k| .$$

**Convolution form.** Write $f = \mathbf{1}_A$, $g = \mathbf{1}_B = \mathbf{1}_{[1,2n]} - f$. Then

$$M_k \;=\; \sum_{j \in \mathbb{Z}} f(j)\,g(j-k) \;=\; (f \star g)(k),$$

so the problem is: **minimise the sup-norm of the cross-correlation of a $\{0,1\}$-function with its complement, subject to a balance constraint.** Equivalently, with $h = f - g \in \{\pm 1\}^{2n}$ and $r_k = \sum_j h(j)h(j-k)$ the autocorrelation, one has $2M_k = (2n - |k|) - r_k$ for $k \ge 0$ when $\sum_j h(j) = 0$; minimising $\max_k M_k$ means forcing all autocorrelations $r_k$ to stay **uniformly high** relative to $2n-|k|$ — the opposite of the low-autocorrelation regime of Barker/Turyn-type problems.

**Continuous relaxation.** Rescaling $\{1,\dots,2n\}$ to $[0,1]$ and passing to the limit, define for measurable $S \subseteq [0,1]$ with Lebesgue measure $\lambda(S) = \tfrac12$ and $S^{c} = [0,1]\setminus S$:

$$\gamma \;=\; \inf_{\substack{S \subseteq [0,1] \\ \lambda(S) = 1/2}} \; \sup_{t \in \mathbb{R}} \; \lambda\big(S \cap (S^{c} + t)\big), \qquad c \;=\; 2\gamma .$$

Subadditivity of $n \mapsto M(n)$-type quantities (via concatenation of near-optimal blocks) gives existence of the limit by Fekete's lemma; Haugland's 1996 paper establishes the limit and identifies it with the continuous variational value. Relaxing $\mathbf{1}_S$ to measurable $\varphi : [0,1] \to [0,1]$ with $\int \varphi = \tfrac12$ does **not** change the value, because the objective $\sup_t \int \varphi(x)(1-\varphi(x+t))\,dx$ admits extreme-point (bang-bang) optimisers.

## 3. History & State of the Art (SOTA)

- **1955.** Erdős poses the problem in *Some remarks on number theory* (Hebrew, Riveon Lematematika) and in his problem collections; he proves $c \ge 1/4$ by the pigeonhole identity of §2, and records an upper bound of $2-\sqrt{2} \approx 0.5857$.
- **1955.** P. Scherk improves the lower bound to $1 - 1/\sqrt{2} \approx 0.2929$ by exploiting the support bound $M_k \le 2n-|k|$.
- **1956.** T. S. Motzkin, K. Ralston and J. L. Selfridge give the upper bound $c < 0.4$ via an explicit block construction.
- **1958.** S. Świerczkowski pushes the lower bound to roughly $0.354$ with a refined averaging/weighting argument.
- **1960s–1980s.** Successive small improvements (Guy's *Unsolved Problems in Number Theory* tracks the table); Erdős repeatedly advertises the problem, e.g. in Erdős–Graham (1980).
- **1996.** J. K. Haugland, *Advances in the minimum overlap problem* (J. Number Theory): proves the limit $c$ exists, reduces the question to the continuous extremal problem, and computes rigorous numerical bounds, giving $c < 0.385694$.
- **2016.** J. K. Haugland, *The minimum overlap problem revisited*: substantially larger discretisation with certified arithmetic yields

$$0.379005 \;<\; c \;<\; 0.380927 .$$

This remains the state of the art. The interval has width $< 2\times10^{-3}$ but no exact value is known, and there is no conjectured closed form.

## 4. Partial Results / Verified Cases

- **Exact small values.** $M(n)$ is computable by exhaustive or branch-and-bound search over $\binom{2n}{n}$ splittings (reduced by the symmetries $A \mapsto B$ and $j \mapsto 2n+1-j$). Values are known for $n$ into the low hundreds; e.g. $M(1)=1$, $M(2)=1$, $M(3)=2$, $M(4)=2$. The ratio $M(n)/n$ decreases slowly and non-monotonically toward $c$.
- **Existence of the limit.** Proven unconditionally (Haugland 1996). This is a genuine theorem, not a numerical observation: the sequence is essentially subadditive under concatenation of blocks.
- **Rigorous two-sided bounds.** $0.379005 < c < 0.380927$, with the lower bound obtained from a finite certified relaxation of the continuous problem and the upper bound from an explicit near-optimal step function on a fine grid.
- **Structure of near-optimal sets.** Optimal-to-numerical-precision $S$ are finite unions of intervals with a self-similar, non-periodic block pattern; purely periodic $S$ (e.g. $A$ = residues in an arithmetic progression) are provably far from optimal, giving $\max_k M_k \sim n$.
- **Degenerate/relaxed variants solved.** If $\max_k$ is replaced by an $L^2$-average, the problem is exactly solvable by Fourier/Parseval, and the extremiser is the interval split; if $|A| = \alpha \cdot 2n$ with $\alpha$ fixed, the same limit theory applies and gives a function $c(\alpha)$, again known only numerically.

## 5. Principal Obstacles

- **No algebraic structure to exploit.** The constraint is only a cardinality constraint on a set of integers. There is no group action, multiplicative structure, or arithmetic function to bring standard analytic number theory to bear.
- **Fourier analysis loses the sup.** $\max_k M_k$ is an $L^\infty$ quantity on the physical side. Parseval controls $\sum_k M_k^2$, which is minimised by configurations that are *not* near-optimal for the sup, and the gap between $L^2$ and $L^\infty$ is $\Theta(1)$ here, not $o(1)$. Uncertainty-principle arguments give nothing sharp because the extremal $S$ is spread across all scales.
- **The extremiser is not explicit.** Numerically optimal sets appear to be aperiodic unions of intervals with no evident closed description, so there is no candidate object whose value could be computed exactly. Without a conjectured extremiser, one cannot run the usual "guess-and-verify-by-duality" pattern.
- **Duality is only approximately certified.** Lower bounds come from finite-dimensional relaxations (LP/measure-theoretic duality on a grid). Each refinement improves the bound but the dual optimal measure has no recognisable limit, so refinements yield digits, not a formula.
- **Discretisation cost.** The continuous problem is an infinite-dimensional minimax; grid size $N$ gives $O(N)$ variables and $O(N)$ sup constraints, and the achievable accuracy in the bound scales roughly like $1/N$, so brute-force refinement gives diminishing returns.
- **No known transfer to a solved model.** The problem does not reduce to a Turán-type extremal problem or to a flag-algebra-friendly setting, because the objective is a supremum over an unbounded translation parameter rather than a fixed-arity density.

## 6. The Gap

Proven: the limit exists and lies in $(0.379005,\, 0.380927)$. Wanted: the exact value.

The precise barrier is the absence of a **matching primal–dual pair** for the continuous problem
$$c/2 \;=\; \inf_{\lambda(S)=1/2} \ \sup_{t} \ \lambda\big(S \cap (S^c+t)\big).$$
Current lower bounds come from finite relaxations (a dual certificate supported on finitely many translations $t_1,\dots,t_m$), and current upper bounds from finite step-function constructions. Both converge to $c$ but from different finite families, and neither family is closed under the operation that would let one identify the fixed point. Closing the gap requires either (i) proving that the optimal $S$ lies in a structured family (e.g. self-similar unions of intervals with a prescribed recursion) so that $c$ becomes the root of an explicit equation, or (ii) a compactness/rigidity theorem showing the dual optimiser is finitely supported, which would make the exact value computable in finitely many steps.

## 7. Current Research (as of June 2026)

- **No published improvement on $0.379005 < c < 0.380927$ since 2016.** The 2016 bounds remain the reference values in the literature and in Guy's problem catalog and Bloom's *Erdős Problems* database. *(frontier — verify: any claim of a sharper interval should be checked against Haugland's own updates, which he has posted on his personal pages rather than in journals.)*
- **Certified numerics.** The natural next step, pursued sporadically, is a large-scale LP/SDP relaxation with interval-arithmetic or exact-rational certificates, in the style of modern verified extremal computations (sphere packing, Keller's conjecture SAT certificates). *(frontier — verify)*
- **Structure of extremisers.** Analysts interested in translation-invariant extremal problems (Fourier optimisation, sign-uncertainty problems) have noted the formal similarity of the objective to Fourier-optimisation programs; whether the Cohn–Elkies-style dual framework applies is unresolved. *(frontier — verify)*
- **Communities.** The problem circulates in additive combinatorics and in the Erdős-problems curation effort (T. Bloom and collaborators), which maintains status pages and prize records for Erdős's problems.

## 8. Future Work

1. **Prove a rigidity theorem** for the optimal $S$: show that any optimiser is a finite or self-similar union of intervals. This is the single step most likely to convert numerics into a closed form.
2. **Finite dual support.** Show that the supremum over $t$ is attained on a finite set determined by the breakpoints of $S$; then the minimax becomes a finite semialgebraic problem and $c$ is algebraic.
3. **Rule out rationality.** Even a proof that $c \notin \mathbb{Q}$, or that $c$ is not a root of a low-degree polynomial, would be a genuine advance and is plausibly within reach of the existing certified bounds combined with a separation argument.
4. **Sharper lower bounds by weighted averaging.** Generalise the Scherk/Świerczkowski weighting (weights $w_k$ against the identity $\sum_k M_k = n^2$ and $M_k \le 2n-|k|$) to weights derived from the numerically observed dual measure.
5. **The full curve $c(\alpha)$** for unbalanced splittings, $|A| = 2\alpha n$: computing its shape may reveal structure invisible at $\alpha = 1/2$.

## 9. Key References

- **[Foundational]** P. Erdős. *Some remarks on number theory* (Hebrew, English summary). Riveon Lematematika 9 (1955), 45–48. — Original statement; $c \ge 1/4$.
- **[Foundational]** P. Erdős and R. L. Graham. *Old and New Problems and Results in Combinatorial Number Theory.* Monographies de L'Enseignement Mathématique 28, Genève, 1980. — Problem restated with the history of bounds.
- **[Foundational]** S. Świerczkowski. *On the intersection of a linear set with the translation of its complement.* Colloquium Mathematicum 5 (1958), 185–197. — Lower bound $\approx 0.354$; the continuous formulation.
- **[SOTA / Recent]** J. K. Haugland. *Advances in the minimum overlap problem.* Journal of Number Theory 58 (1996), no. 1, 71–78. — Existence of $\lim M(n)/n$; upper bound $c < 0.385694$.
- **[SOTA / Recent]** J. K. Haugland. *The minimum overlap problem revisited.* arXiv preprint, 2016. — Certified bounds $0.379005 < c < 0.380927$.
- **[Survey]** R. K. Guy. *Unsolved Problems in Number Theory.* 3rd edition, Springer, 2004. — Section C on additive number theory; tabulates the history of bounds for the minimum overlap problem.
- **[Survey]** T. Bloom. *Erdős Problems* (online database of Erdős's problems, with status and references), ongoing.

## 10. Worked Example / Concrete Special Case

**(a) A small exact case: $n = 3$, so $\{1,\dots,6\}$.** Take $A = \{1,4,5\}$, $B = \{2,3,6\}$. Compute $M_k = \\#\{(a,b) : a-b=k\}$:

| $k$ | $-5$ | $-2$ | $-1$ | $1$ | $2$ | $3$ |
|---|---|---|---|---|---|---|
| pairs | $(1,6)$ | $(1,3),(4,6)$ | $(1,2),(5,6)$ | $(4,3)$ | $(4,2),(5,3)$ | $(5,2)$ |
| $M_k$ | 1 | 2 | 2 | 1 | 2 | 1 |

Total $= 9 = n^2$. ✓ Here $\max_k M_k = 2$. No splitting of $\{1,\dots,6\}$ achieves $\max_k M_k = 1$: that would force $\sum_k M_k \le 11$ over the $11$ admissible $k \in \{-5,\dots,5\}$ nonzero and zero — but $M_0 = 0$ always (a number cannot be in both $A$ and $B$), leaving $10$ values of $k$ and $\sum M_k \le 10 < 9$… which is not immediately contradictory, so check directly: $M_1 = M_{-1} = 1$ forces exactly one adjacent $A$-then-$B$ pattern in each direction, impossible for a $3+3$ split of six consecutive integers. Hence $M(3) = 2$ and $M(3)/3 = 0.667$.

**(b) The two lower bounds, derived.** By the counting identity and $M_k = 0$ for $|k| \ge 2n$,
$$n^2 = \sum_{|k| \le 2n-1} M_k \;\le\; (4n-1)\max_k M_k \quad\Longrightarrow\quad \frac{M(n)}{n} \;>\; \frac14 ,$$
which is Erdős's bound $c \ge 1/4$.

Refine using $M_k \le 2n - |k|$. Suppose $\max_k M_k = \beta n$. Then $M_k \le \min(\beta n,\, 2n-|k|)$, and the second bound is the binding one exactly when $|k| > (2-\beta)n$. Summing,
$$n^2 \;\le\; \underbrace{2(2-\beta)n \cdot \beta n}_{|k| \le (2-\beta)n} \;+\; \underbrace{2 \cdot \tfrac12 (\beta n)^2}_{|k| > (2-\beta)n} \;=\; \big(4\beta - 2\beta^2 + \beta^2\big) n^2 = (4\beta - \beta^2)\,n^2 .$$
So $\beta^2 - 4\beta + 1 \le 0$, giving $\beta \ge 2 - \sqrt{3} \approx 0.2679$. Scherk's sharper handling of the same two inputs gives $1 - 1/\sqrt{2} \approx 0.2929$.

**(c) Why the true value is larger.** Both arguments above pretend $M_k$ can sit at its cap for every $k$ simultaneously. It cannot: the profile $k \mapsto M_k$ of an actual set is a cross-correlation and is therefore constrained by positive-definiteness of the autocorrelation $r_k$. Haugland's certified computations exploit exactly these extra constraints, pushing the lower bound from $0.29$ to $0.379005$, while explicit step-function constructions cap it at $0.380927$. The remaining $0.0019$ is the whole of the open problem.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*