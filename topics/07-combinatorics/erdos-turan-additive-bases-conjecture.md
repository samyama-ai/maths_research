---
id: 07-combinatorics/erdos-turan-additive-bases-conjecture
title: "Erdős-Turán Conjecture on Additive Bases"
topic: 07-combinatorics
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Erdős-Turán Conjecture on Additive Bases

> **Topic:** Combinatorics & Graph Theory · **ID:** `07-combinatorics/erdos-turan-additive-bases-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Let $A \subseteq \mathbb{N}_0 = \{0,1,2,\dots\}$ be infinite, and let

$$r_A(n) \;=\; \\#\{(a,b) \in A \times A \;:\; a+b = n\}$$

be its (ordered) representation function. Call $A$ an **additive basis of order 2** (an *asymptotic basis*) if $r_A(n) \ge 1$ for all sufficiently large $n$.

> **Conjecture (Erdős–Turán, 1941).** If $A$ is an asymptotic basis of order 2, then
> $$\limsup_{n \to \infty} r_A(n) = \infty .$$

Equivalently: no set of non-negative integers can represent every large integer while keeping the number of representations uniformly bounded. A proof must handle *every* basis; a disproof requires an explicit or probabilistic construction of $A \subseteq \mathbb{N}_0$ and a constant $C$ with $1 \le r_A(n) \le C$ for all large $n$. Erdős attached a \$500 prize; the problem is listed as \\#30 in the Erdős problem catalogue.

The natural generalisation replaces 2 by $h \ge 2$: if $r_{A,h}(n) = \\#\{(a_1,\dots,a_h) \in A^h : a_1+\cdots+a_h = n\} \ge 1$ for large $n$, is $\limsup_n r_{A,h}(n) = \infty$? This is open for every $h \ge 2$.

## 2. Mathematical Foundations

**Counting function and the square-root barrier.** Write $A(x) = \\#\left(A \cap [0,x]\right)$. Since every $n \le N$ has a representation using elements of $A \cap [0,N]$,

$$N + O(1) \;\le\; \sum_{n \le N} r_A(n) \;\le\; A(N)^2 ,
\qquad\text{hence}\qquad A(N) \;\ge\; (1+o(1))\sqrt{N}. \tag{2.1}$$

Conversely, if $A$ is a basis with $r_A(n) \le C$, then $A(N)^2 \le \sum_{n\le 2N} r_A(n) \le 2CN$, so $A(N) \ll_C \sqrt{N}$. **Any counterexample must satisfy $A(N) \asymp \sqrt{N}$** — it is a *thin* basis. This is the single most important structural constraint.

**Generating function formulation.** Put $f(z) = \sum_{a \in A} z^a$ for $|z| < 1$. Then

$$f(z)^2 \;=\; \sum_{n \ge 0} r_A(n) z^n, \qquad \frac{f(z)^2}{1-z} \;=\; \sum_{N \ge 0} R_A(N) z^N, \quad R_A(N) := \sum_{n \le N} r_A(n).$$

The conjecture asserts that $f(z)^2$ cannot have coefficients confined to a bounded interval $[1,C]$ from some point on. Since $\sum_{n\le N} z^n$-type comparison gives $R_A(N) \sim cN$ for a hypothetical counterexample with $c \in [1,C]$ in the Cesàro sense, the problem lives at the interface of Tauberian theory and $L^2$ methods on the circle.

**Circle-method / $L^2$ view.** With $f_N(\theta) = \sum_{a \in A, a \le N} e(a\theta)$, Parseval gives

$$\int_0^1 |f_N(\theta)|^4 \, d\theta \;=\; \sum_{n} r_{A \cap [0,N]}(n)^2 .$$

A bounded representation function forces $\sum_n r_A(n)^2 \ll N$, i.e. $\|f_N\|_4^4 \ll \|f_N\|_2^4 / 1$ — the fourth moment is as small as it can be for a set of size $\asymp \sqrt N$. Such sets are *near-perfect-difference-set-like*; they exist in finite settings, which is why no purely $L^2$ argument can succeed.

**Erdős–Fuchs theorem (1956).** For every infinite $A$ and every $c > 0$,

$$\sum_{n \le N} r_A(n) \;=\; cN + o\!\left(N^{1/4} (\log N)^{-1/2}\right) \tag{2.2}$$

is impossible. Montgomery–Vaughan (1990) showed the exponent $1/4$ and the $\log$ power are both optimal. Thus $R_A(N)$ must oscillate around any linear trend by at least $N^{1/4}(\log N)^{-1/2}$ — but oscillation of the *partial sums* is fully compatible with $r_A(n) \in \{1,2,\dots,C\}$, which is exactly why (2.2) does not settle the conjecture.

## 3. History & State of the Art (SOTA)

- **1941.** P. Erdős and P. Turán, *On a problem of Sidon in additive number theory, and on some related problems* (J. London Math. Soc. **16**, 212–215), state the conjecture alongside their celebrated $B_2$-set bound $|A| \le x^{1/2} + O(x^{1/4})$ for Sidon sets in $[1,x]$.
- **1956.** Erdős–Fuchs prove (2.2), the first genuine general obstruction to "almost constant" representation counts.
- **1956.** Erdős, by a random-greedy construction, exhibits a basis of order 2 with $r_A(n) = \Theta(\log n)$ — the sparsest known representation behaviour, and the conjectured true minimum growth rate for "generic" bases.
- **1990.** Erdős–Tetali extend the probabilistic construction to all orders $h$: there is a basis of order $h$ with $r_{A,h}(n) \asymp \log n$.
- **1990.** Ruzsa (*A just basis*) constructs a basis of order 2 whose representation function is bounded **in mean square**: $\sum_{n \le N} r_A(n)^2 = O(N)$. This kills every second-moment approach.
- **2003.** Nathanson constructs *unique representation bases* for $\mathbb{Z}$: $A \subseteq \mathbb{Z}$ with $r_A(n) = 1$ for **all** $n \in \mathbb{Z}$. The conjecture is therefore false over $\mathbb{Z}$ — it depends essentially on one-sidedness of $\mathbb{N}$.
- **2003–2006.** Quantitative attack on the $\limsup$: Grekos–Haddad–Helou–Pihko prove $\limsup r_A(n) \ge 5$; Borwein–Choi–Chu improve this to $\ge 6$, combining an extremal analysis with exhaustive computation over finite bases.
- **2008.** Chen Yong-Gao settles the $\mathbb{Z}_m$ analogue negatively, constructing for every $m$ a subset of $\mathbb{Z}_m$ that is a basis with uniformly bounded representation function.
- **2013.** Konstantoulas obtains lower bounds on representation functions for bases with prescribed density, showing $\limsup r_A(n)$ grows if $A$ is denser than the critical $\sqrt{N}$ scale by a fixed factor.

**SOTA summary:** the best unconditional statement is $\limsup_n r_A(n) \ge 6$; the conjectured truth is $\infty$.

## 4. Partial Results / Verified Cases

1. **Dense bases (fully solved).** If $\limsup_{N} A(N)/\sqrt{N} = \infty$, the conjecture holds: by (2.1), $\frac{1}{N}\sum_{n\le N} r_A(n) \ge A(\sqrt{N})^2/N \to \infty$ along a subsequence, so the maximum is unbounded. More sharply, $A(N) \ge K\sqrt{N}$ for large $N$ forces $\limsup r_A(n) \ge K^2$. Only bases with $A(N) \asymp \sqrt N$ survive.
2. **Quantitative $\limsup$ bounds.** $\limsup r_A(n) \ge 6$ (Borwein–Choi–Chu 2006), improving $\ge 5$ (Grekos et al. 2003). The finite ingredient is: any $A$ with $r_A(n)\ge 1$ for all $n \le N$ has $\max_{n \le N} r_A(n) \ge 6$ once $N$ exceeds an explicit, computer-verified threshold.
3. **Regularity-type cases.** By Erdős–Fuchs, no basis satisfies $R_A(N) = cN + o(N^{1/4}\log^{-1/2}N)$; hence bases whose representation function is *asymptotically constant* ($r_A(n) \to c$) or constant on a density-1 set with small variance are excluded.
4. **Bases of positive lower density in structured families.** For $A$ a union of finitely many arithmetic progressions, or $A$ the value set of a polynomial of degree $\ge 2$ (Waring-type bases), $r_A(n)$ is unbounded by classical circle-method asymptotics — e.g. for squares, $r(n)$ is $\Theta(n^{o(1)})$ but unbounded along $n$ with many prime factors $\equiv 1 \bmod 4$.
5. **Counterexamples in relaxed settings (negative verified cases).** $\mathbb{Z}$: Nathanson (2003), $r_A(n) = 1$ for all $n$. $\mathbb{Z}_m$: Chen (2008). Mean-square over $\mathbb{N}$: Ruzsa (1990). These delimit exactly which hypotheses are load-bearing: well-ordering of $\mathbb{N}$ and control of the *supremum*, not the average.

## 5. Principal Obstacles

- **Every averaged statistic is achievable.** Ruzsa's just basis has $\sum_{n\le N} r_A(n)^2 = O(N)$, matching what a bounded representation function would give. Any proof strategy that only controls $L^2$ norms of $f_N$ — Parseval, large sieve, standard circle method — is provably incapable of reaching a contradiction. One would need a genuinely $L^\infty$ statement.
- **The obstruction is not local.** The $\mathbb{Z}_m$ and $\mathbb{Z}$ counterexamples show there is no congruence obstruction and no "algebraic" reason. Whatever forces unboundedness must use the order structure of $\mathbb{N}$ (positivity: $a+b = n$ with $0 \le a,b \le n$), which Fourier analysis on $\mathbb{Z}$ discards.
- **Extremal finite configurations exist.** Perfect difference sets (Singer, from $PG(2,q)$) give $A \subseteq \mathbb{Z}_{q^2+q+1}$ of size $q+1$ with every non-zero residue represented exactly once as a difference. Analogous finite additive designs let one build $A \cap [0,N]$ with $A(N) \sim c\sqrt N$ and $\max_{n \le N} r_A(n)$ small (growing very slowly). The conjecture asserts these cannot be glued coherently across all scales, but no invariant is known that is monotone under such gluing.
- **Erdős–Fuchs is sharp and too weak.** The $N^{1/4}$ oscillation it forces is compatible with $r_A(n)$ taking values in $\{1,\dots,C\}$ in a suitably irregular pattern; strengthening the error term is impossible (Montgomery–Vaughan).
- **No transfer from Sidon theory.** A counterexample would be a "near-Sidon basis": simultaneously as sparse as a Sidon set and as covering as a basis. The Erdős–Turán Sidon bound $|A \cap [1,x]| \le x^{1/2}+O(x^{1/4})$ shows these two demands are *nearly* compatible; the gap between $x^{1/2}$ and $x^{1/2}+O(x^{1/4})$ is precisely where the problem sits, and no method resolves quantities at that resolution.

## 6. The Gap

Proven: $\limsup r_A(n) \ge 6$, and unboundedness whenever $A(N)/\sqrt N \to \infty$. Conjectured: $\limsup r_A(n) = \infty$ for the remaining class $A(N) \asymp \sqrt N$.

The exact missing step is a **scale-coupling argument**: current lower bounds on $\limsup r_A(n)$ come from finite extremal combinatorics inside a single window $[0,N]$, and each such argument saturates at an absolute constant, because a *finite* window genuinely admits bases with small maximum representation count (see §10). To reach $\infty$ one must show that a basis achieving max-representation $\le C$ on $[0,N]$ imposes a structure on $A \cap [0,N]$ that is incompatible with extending to $[0, N^{1+\delta}]$ at the same cost — i.e. an induction on scales with a strictly increasing cost functional. No candidate functional is known that is (i) computable from $A \cap [0,N]$, (ii) monotone under extension, and (iii) unbounded. Closing the gap is equivalent to converting the $L^2$-tight information of Ruzsa's construction into an $L^\infty$ contradiction using positivity of $\mathbb{N}$.

## 7. Current Research (as of June 2026)

- **Quantitative $\limsup$ improvements.** The value 6 has stood since 2006. Groups in Hungary (Rényi Institute — Sándor, Kiss and coauthors on representation functions and their maxima) and in China (Chen Yong-Gao's school, Nanjing Normal) continue to push extremal and finite-window analyses; incremental gains to 7 or beyond are the realistic near-term target. *(frontier — verify: no published improvement past 6 has been confirmed.)*
- **Probabilistic and entropy methods.** Refinements of the Erdős–Tetali random construction ask for the minimal possible growth of $\max_{n \le N} r_A(n)$: is $\log N$ optimal, i.e. is there a basis with $r_A(n) = O(\log n / \log\log n)$? Entropy-compression and container-method arguments are being applied to the space of bases. *(frontier — verify.)*
- **Relaxations and analogues.** Bases of $\mathbb{Z}$, $\mathbb{Z}_m$, function fields $\mathbb{F}_q[t]$, and bases of order $h$ where the representation function is restricted (e.g. counting only representations with $a < b$). Each analogue that *fails* sharpens the list of properties of $\mathbb{N}$ a proof must use.
- **Computational search.** Exhaustive and SAT/ILP-driven searches for finite bases of $[0,N]$ minimising $\max_n r_A(n)$, extending the Borwein–Choi–Chu tables; the growth rate of this finite extremal quantity as $N \to \infty$ is the direct finite proxy for the conjecture.
- **Catalogue activity.** The problem is tracked as \#30 on Thomas Bloom's *erdosproblems.com*, which aggregates current partial results and prize status.

## 8. Future Work

- **Find a scale-monotone invariant.** Leading suggestion (Erdős, Ruzsa, Tao): identify an entropy- or energy-type functional $\Phi(A \cap [0,N])$ that is bounded below in terms of $\max_{n\le N} r_A(n)$ and grows with $\log N$ for any set extendable to a basis.
- **Prove the finite version quantitatively.** Show that $m(N) := \min \{ \max_{n \le N} r_A(n) : A \subseteq [0,N],\, r_A(n)\ge 1 \ \forall n \le N \}$ satisfies $m(N) \to \infty$. This is formally weaker in appearance but is essentially equivalent to the conjecture and is amenable to computation.
- **Exploit positivity.** Develop analytic tools on the half-line — Tauberian arguments with one-sided kernels, or Hardy-space methods for $f(z)^2$ — that do not survive passage to $\mathbb{Z}$, thereby avoiding Nathanson's counterexample automatically.
- **Sharpen the Sidon connection.** Determine whether a basis with $A(N) \le (1+\epsilon)\sqrt N$ for all large $N$ must have unbounded $r_A$; this "critically thin" case may be tractable and would isolate the difficulty in the constant.
- **Higher orders.** Even a proof for a single $h \ge 3$ would be a breakthrough, and the extra degrees of freedom in $h$-fold sums may allow a counting argument unavailable at $h=2$.

## 9. Key References

- **[Foundational]** P. Erdős, P. Turán. *On a problem of Sidon in additive number theory, and on some related problems.* Journal of the London Mathematical Society **16** (1941), 212–215.
- **[Foundational]** P. Erdős, W. H. J. Fuchs. *On a problem of additive number theory.* Journal of the London Mathematical Society **31** (1956), 67–73.
- **[Foundational]** P. Erdős. *Problems and results in additive number theory.* Colloque sur la Théorie des Nombres (Bruxelles, 1955), Georges Thone / Masson, 1956, 127–137.
- **[Key construction]** I. Z. Ruzsa. *A just basis.* Monatshefte für Mathematik **109** (1990), 145–151.
- **[Key construction]** P. Erdős, P. Tetali. *Representation of integers as the sum of $k$ terms.* Random Structures & Algorithms **1** (1990), 245–261.
- **[Key construction]** M. B. Nathanson. *Unique representation bases for the integers.* Acta Arithmetica **108** (2003), 1–8.
- **[SOTA]** G. Grekos, L. Haddad, C. Helou, J. Pihko. *On the Erdős–Turán conjecture.* Journal of Number Theory **102** (2003), 339–352.
- **[SOTA]** P. Borwein, S. Choi, F. Chu. *An old conjecture of Erdős–Turán on additive bases.* Mathematics of Computation **75** (2006), 475–484.
- **[SOTA]** Y.-G. Chen. *The analogue of Erdős–Turán conjecture in $\mathbb{Z}_m$.* Journal of Number Theory **128** (2008), 2573–2581.
- **[SOTA]** I. Konstantoulas. *Lower bounds for a conjecture of Erdős and Turán.* Acta Arithmetica **159** (2013), 301–313.
- **[Sharpness]** H. L. Montgomery, R. C. Vaughan. *On the Erdős–Fuchs theorems.* In *A Tribute to Paul Erdős*, Cambridge University Press, 1990, 331–338.
- **[Survey / Book]** H. Halberstam, K. F. Roth. *Sequences.* Oxford University Press, 1966 (2nd ed., Springer, 1983).
- **[Survey / Book]** M. B. Nathanson. *Additive Number Theory: The Classical Bases.* Graduate Texts in Mathematics 164, Springer, 1996.
- **[Survey / Book]** T. Tao, V. H. Vu. *Additive Combinatorics.* Cambridge Studies in Advanced Mathematics 105, Cambridge University Press, 2006.

## 10. Worked Example / Concrete Special Case

**A finite basis of $[0,99]$ with small representation counts.** Take

$$A \;=\; \{0,1,2,\dots,9\} \;\cup\; \{10,20,30,\dots,90\}, \qquad |A| = 19 .$$

Every $n \in [0,99]$ writes as $n = 10q + r$ with $0 \le q,r \le 9$, and $10q \in A$, $r \in A$. So $r_A(n) \ge 1$ on all of $[0,99]$: $A$ is a basis of the window.

Check the lower bound (2.1): $A(99)^2 = 361 \ge 100$, and indeed $|A| = 19 \approx 1.9\sqrt{100}$ — within a factor 1.9 of the theoretical floor $\sqrt{N} = 10$.

Representation counts (ordered pairs):

| $n$ | representations $a+b=n$, $a,b\in A$ | $r_A(n)$ |
|---|---|---|
| $47$ | $7+40,\;40+7$ | $2$ |
| $55$ | $5+50,\;50+5$ | $2$ |
| $30$ | $0+30,\;30+0,\;10+20,\;20+10$ | $4$ |
| $90$ | $0+90,\,90+0,\,10+80,\,80+10,\,20+70,\,70+20,\,30+60,\,60+30,\,40+50,\,50+40$ | $10$ |

So $\max_{n \le 99} r_A(n) = 10$, attained at the "structured" point $n = 90$, while a typical $n$ has $r_A(n) = 2$. The average is $\tfrac{1}{100}\sum_{n \le 99} r_A(n) \le |A|^2/100 = 3.61$.

**What this illustrates.**

1. *Average versus supremum.* The density factor $1.9$ forces average multiplicity $\approx 1.9^2 = 3.6$ — this is the whole content of the trivial bound in §4.1. It says nothing about the supremum growing with $N$.
2. *Spikes are structural, not statistical.* The excess at $n = 90$ comes from the arithmetic-progression structure of the second block. A cleverer block (a Sidon set of multiples of 10) would flatten it — but the quotients must cover $\{0,\dots,9\}$ entirely, so the second block is forced to be $\{0,10,\dots,90\}$ and the spike is unavoidable *for this construction*.
3. *Why finite windows do not decide the problem.* Iterating the base-$b$ idea, $A_k = \bigcup_{j<k}\{ i\cdot b^{j} : 0 \le i < b \}$ covers $[0, b^k)$ with $|A_k| = k(b-1)+1$ elements — far below $\sqrt{b^k}$, so this cannot be a basis of order 2 for large $k$; the genuinely economical windows need $\asymp \sqrt N$ elements, and their maxima grow only very slowly in the known examples. The Erdős–Turán conjecture is precisely the claim that this slow growth is nevertheless unbounded — a statement no single window can witness.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*