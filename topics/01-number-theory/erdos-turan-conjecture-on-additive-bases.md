---
id: 01-number-theory/erdos-turan-conjecture-on-additive-bases
title: "Erdos-Turan Conjecture on Additive Bases"
topic: 01-number-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Erdős–Turán Conjecture on Additive Bases

> **Topic:** Number Theory · **ID:** `01-number-theory/erdos-turan-conjecture-on-additive-bases` · **Status:** open

## 1. Problem Statement / Conjecture

Let $A \subseteq \mathbb{N}_0 = \{0,1,2,\dots\}$ be infinite, and let
$$r_A(n) \;=\; \\#\{(a,a') \in A\times A : a + a' = n,\ a \le a'\}$$
be its (unordered) representation function. Call $A$ an **additive basis of order 2** if $r_A(n) \ge 1$ for all sufficiently large $n$.

**Conjecture (Erdős–Turán, 1941).** If $A$ is an additive basis of order 2, then
$$\limsup_{n \to \infty} r_A(n) = \infty .$$

Equivalently: no set can cover every large integer as a sum of two of its elements while keeping the number of representations uniformly bounded. A disproof requires an explicit or probabilistic construction of $A$ and a constant $C$ with $1 \le r_A(n) \le C$ for all $n \ge n_0$. A proof requires showing that $r_A(n) \le C$ for all $n$ forces $r_A(n) = 0$ infinitely often. Erdős offered \$500 for a resolution; the problem is open in both directions.

Two structural caveats fix the scope. The statement is **false** if $\mathbb{N}_0$ is replaced by $\mathbb{Z}$, and **false** in the cyclic groups $\mathbb{Z}_m$ (Section 4). Any proof must therefore use the order and positivity of $\mathbb{N}_0$, not just its group structure.

## 2. Mathematical Foundations

**Counting function.** Write $A(x) = \\#\{a \in A : a \le x\}$.

**Generating function.** With $f_A(z) = \sum_{a\in A} z^a$ on $|z|<1$,
$$f_A(z)^2 \;=\; \sum_{n\ge 0} \tilde r_A(n)\, z^n, \qquad \tilde r_A(n) = \\#\{(a,a'): a+a'=n\},$$
where $\tilde r_A(n) = 2 r_A(n) - \mathbb{1}[n/2 \in A]$. On the circle $z = e(\theta)$, Parseval gives
$$\sum_{n} \tilde r_A(n)^2 \ \text{(truncated)} \ \longleftrightarrow \ \int_0^1 |f_A(e(\theta))|^4 \, d\theta,$$
the $L^4$ norm that all Fourier-analytic attacks target.

**First moment.** Every pair $(a,a')$ with $a,a' \le x$ contributes to some $n \le 2x$, so
$$\sum_{n \le 2x} r_A(n) \;\ge\; \binom{A(x)}{2} \;=\; \frac{A(x)^2 - A(x)}{2}. \tag{2.1}$$
Conversely, a basis needs $\sum_{n\le N} r_A(n) \ge N + O(1)$, hence
$$A(N) \;\ge\; \sqrt{2N} \,(1+o(1)). \tag{2.2}$$

**Sidon sets ($B_2$ sets).** $A$ is *Sidon* if all pairwise sums $a+a'$ ($a\le a'$) are distinct, i.e. $r_A(n) \le 1$ for every $n$. **Erdős–Turán (1941):** a Sidon set satisfies
$$A(x) \;\le\; x^{1/2} + x^{1/4} + 1. \tag{2.3}$$

**Erdős–Fuchs theorem (1956).** For any $A \subseteq \mathbb{N}_0$ and any $c>0$,
$$\sum_{n \le N} r_A(n) \;=\; cN + o\!\left( N^{1/4} (\log N)^{-1/2} \right)$$
is impossible. So the counting of representations by a basis can never be as regular as that of a "continuous" set of density $\sqrt{c}$.

**Erdős's probabilistic basis (1956).** There exists $A$ with
$$r_A(n) \;\asymp\; \log n \qquad (n \ \text{large}),$$
obtained by including $n$ independently with probability $p_n \asymp \sqrt{\log n / n}$. This is the thinnest known basis in terms of representation growth, and $\log n$ is conjecturally the true minimum order of $\max_{m\le n} r_A(m)$.

## 3. History & State of the Art (SOTA)

- **1941.** Erdős and Turán, *On a problem of Sidon in additive number theory, and on some related problems* (J. London Math. Soc. 16), prove the Sidon bound (2.3) and pose the conjecture.
- **1955–56.** Erdős's random construction gives bases with $r_A(n) \asymp \log n$, showing the conjecture — if true — is sharp only up to the question of how slowly $\limsup r_A$ may grow.
- **1956.** Erdős and Fuchs prove the regularity obstruction above; it remains the deepest general theorem about $\sum_{n\le N} r_A(n)$ and has been refined many times (Jurkat, Montgomery–Vaughan, Hayashi) but never to the point of forcing $\limsup r_A = \infty$.
- **1990.** Ruzsa, *A just basis*, constructs a basis $A$ of order 2 with $\sum_{n \le N} r_A(n)^2 = O(N)$ — i.e. bounded *mean square*. This is the single most important negative signal: all $L^2$/$L^4$ methods are blind to the conjecture.
- **2003.** Nathanson constructs **unique representation bases for $\mathbb{Z}$**: $A\subseteq\mathbb{Z}$ with $r_A(n) = 1$ for *every* $n \in \mathbb{Z}$. The conjecture is thus false over $\mathbb{Z}$.
- **2003.** Grekos, Haddad, Helou, Pihko: if $r_A(n)\ge 1$ for all large $n$ then $\limsup r_A(n) \ge 6$.
- **2006.** Borwein, Choi, Chu improve this to $\limsup r_A(n) \ge 36$, by a large combinatorial optimization over finite blocks combined with computer search.
- **2008.** Chen Yong-Gao settles the cyclic analogue negatively: for every $m$ there is $A \subseteq \mathbb{Z}_m$ with $1 \le r_A(n) \le 768$ for all $n \in \mathbb{Z}_m$, with the constant uniform in $m$.

**SOTA summary.** Proven: $\limsup r_A(n) \ge 36$ for any basis of order 2. Conjectured: $\infty$. The gap between a finite constant and $\infty$ has not narrowed qualitatively since 1941.

## 4. Partial Results / Verified Cases

- **Bounded case $C \le 2$ (Sidon-type).** If $r_A(n)\le 1$ for all $n$, then (2.3) gives $A(x) \le x^{1/2}+x^{1/4}+1$, while (2.2) forces $A(x)\ge \sqrt{2x}(1+o(1))$. For $x$ large these contradict, so **no Sidon set is a basis of order 2**. This is the conjecture verified at its smallest parameter.
- **Thick sets.** If $\limsup_{x} A(x)/\sqrt{x} = \infty$, then by (2.1) the average of $r_A$ over $[1,2x]$ is unbounded, so $\limsup r_A = \infty$. Hence any counterexample must be *exactly* of order $A(x) \asymp \sqrt{x}$ — a razor-thin regime.
- **Explicit numerical lower bounds.** $\limsup r_A(n) \ge 5$ (Dowd-type block arguments), $\ge 6$ (Grekos–Haddad–Helou–Pihko 2003), $\ge 36$ (Borwein–Choi–Chu 2006, verified by finite computation over representation patterns on intervals).
- **Regularity case.** By Erdős–Fuchs, no basis has $\sum_{n\le N} r_A(n) = cN + o(N^{1/4}(\log N)^{-1/2})$; in particular $r_A(n)$ cannot be eventually equal to a constant $c$ for all $n$, nor "essentially constant" in this strong averaged sense.
- **Where it is false.** Order $h=2$ over $\mathbb{Z}$: Nathanson (2003), $r_A \equiv 1$. Over $\mathbb{Z}_m$ for every modulus $m$: Chen (2008), $1 \le r_A \le 768$. Finite perfect difference sets (Singer, $m = q^2+q+1$) give explicit small-modulus examples.
- **Higher orders.** The analogous conjecture for bases of order $h \ge 3$ (with $r_{A,h}(n)\ge 1$) is open, with the same $\mathbb{Z}$- and $\mathbb{Z}_m$-counterexamples available.

## 5. Principal Obstacles

- **Second-moment methods are provably insufficient.** Ruzsa's 1990 basis has $\sum_{n\le N} r_A(n)^2 \ll N$, matching the trivial lower bound. Any argument that only controls $\|f_A\|_{L^4}^4 = \int |f_A|^4$ cannot distinguish a genuine bounded-representation basis from Ruzsa's set. Fourier analysis on $\mathbb{Z}$ naturally produces exactly $L^2$ and $L^4$ information.
- **No group-theoretic proof can exist.** Nathanson's $\mathbb{Z}$-basis and Chen's $\mathbb{Z}_m$-bases mean that any valid proof must invoke the *ordering* of $\mathbb{N}_0$ — the fact that sums of positive elements grow. Circle-method, character-sum, and Fourier-transform arguments are translation-invariant and lose precisely this information.
- **The extremal regime is a knife-edge.** A counterexample must have $A(x) = \Theta(\sqrt{x})$: thick enough to cover all $n$, thin enough to avoid coincidences. Both known extremes are ruled out (Section 4), but no method interpolates. Density arguments give one inequality, Sidon-type arguments the other, and they meet only at the constant.
- **Finite-block methods saturate.** The route to $\limsup \ge 36$ analyses representation patterns on intervals $[0,N]$ and optimizes; the achievable bound grows roughly like the search depth allows, with combinatorial explosion. There is no known mechanism by which such finite certificates could ever yield $\infty$.
- **Erdős–Fuchs does not scale.** It obstructs *smoothness* of the summatory function, not boundedness of $r_A$ itself; a bounded but erratic $r_A$ passes every known Erdős–Fuchs-type test.

## 6. The Gap

Proven (Section 4): for a basis of order 2, $\limsup r_A(n) \ge 36$, $A(x) \asymp \sqrt{x}$, and $r_A \not\le 1$. Conjectured (Section 1): $\limsup r_A(n) = \infty$.

The precise missing step is a *self-improving* mechanism: an argument showing that if $r_A(n) \le C$ for all $n$, then a contradiction arises for **every** $C$, not just $C < 36$. Concretely, one needs either

1. an inequality of the form $\max_{n\le N} r_A(n) \ge \varphi(N)$ with $\varphi \to \infty$, valid for all order-2 bases — plausibly $\varphi(N) \asymp \log N$ by Erdős's construction; or
2. a higher-moment or non-translation-invariant functional $\Phi(A)$ that is bounded on $\mathbb{Z}$-bases but forced to diverge on $\mathbb{N}_0$-bases, thereby using positivity.

No candidate for either is known.

## 7. Current Research (as of June 2026)

- **Refined finite-block optimization.** Continuation of Borwein–Choi–Chu with SAT/ILP certificate search for $\limsup \ge C$ at larger $C$; reported improvements past 36 remain incremental and constant-bound in nature *(frontier — verify)*.
- **Representation functions in general abelian groups.** Chinese schools around Chen Yong-Gao and Tang Min (Nanjing Normal University) continue mapping which groups and which $h$ admit bounded-representation bases, sharpening Chen's constant 768 and studying $r_{A,h}$ in $\mathbb{Z}_m$ *(frontier — verify)*.
- **Nathanson's programme on unique-representation bases** for $\mathbb{Z}$ and for arbitrary countable abelian groups, aimed at isolating exactly which axiom fails when passing to $\mathbb{N}_0$ (CUNY Graduate Center).
- **Probabilistic/thin-basis side.** Refinements of Erdős's random model and of Vu-style concentration methods to construct bases with $\max_{m \le n} r_A(m)$ as small as possible; the target is to determine whether $\log n$ is optimal.
- **Erdős-problem databases.** The problem is actively tracked with a live status page in Thomas Bloom's *erdosproblems.com* collection, which aggregates partial results and prize history.

## 8. Future Work

- **Prove a growth lower bound, not a constant.** Erdős repeatedly emphasized that the real content is $\limsup r_A(n) = \infty$; a first genuine step would be any bound $\limsup r_A(n) \ge \varphi(N)$ growing with $N$, however slowly.
- **Formalize the positivity obstruction.** Isolate a functional inequality valid on $\mathbb{N}_0$ and violated in $\mathbb{Z}$/$\mathbb{Z}_m$; this would be the first tool immune to Nathanson's and Chen's counterexamples.
- **Beat $L^4$.** Develop $L^6$ or higher-moment estimates for $f_A$, or entropy/additive-energy arguments in the spirit of Tao–Vu, that Ruzsa's just basis does not defeat.
- **Determine the extremal order.** Decide whether every basis satisfies $\max_{m\le n} r_A(m) \gg \log n$, which would simultaneously prove the conjecture and show Erdős's random construction is optimal.
- **Order $h\ge 3$.** Solve the $h$-fold analogue, where the larger combinatorial freedom may permit averaging methods unavailable at $h=2$.

## 9. Key References

- **[Foundational]** P. Erdős, P. Turán. *On a problem of Sidon in additive number theory, and on some related problems.* Journal of the London Mathematical Society **16** (1941), 212–215.
- **[Foundational]** P. Erdős, W. H. J. Fuchs. *On a problem of additive number theory.* Journal of the London Mathematical Society **31** (1956), 67–73.
- **[Foundational]** P. Erdős. *Problems and results in additive number theory.* Colloque sur la Théorie des Nombres, Bruxelles, 1955; Georges Thone / Masson, 1956, 127–137.
- **[Structural]** I. Z. Ruzsa. *A just basis.* Monatshefte für Mathematik **109** (1990), 145–151.
- **[Counterexample / $\mathbb{Z}$]** M. B. Nathanson. *Unique representation bases for the integers.* Acta Arithmetica **108** (2003), 1–8.
- **[Counterexample / $\mathbb{Z}_m$]** Y.-G. Chen. *The analogue of Erdős–Turán conjecture in $\mathbb{Z}_m$.* Journal of Number Theory **128** (2008), 2573–2581.
- **[SOTA]** G. Grekos, L. Haddad, C. Helou, J. Pihko. *On the Erdős–Turán conjecture.* Journal of Number Theory **102** (2003), 339–352.
- **[SOTA]** P. Borwein, S. Choi, F. Chu. *An old conjecture of Erdős–Turán on additive bases.* Mathematics of Computation **75** (2006), 475–484.
- **[Survey]** A. Sárközy, V. T. Sós. *On additive representation functions.* In: *The Mathematics of Paul Erdős I*, Springer, 1997, 129–150.
- **[Book]** H. Halberstam, K. F. Roth. *Sequences.* Oxford University Press, 1966.
- **[Book]** M. B. Nathanson. *Additive Number Theory: The Classical Bases.* Graduate Texts in Mathematics 164, Springer, 1996.
- **[Book]** T. Tao, V. H. Vu. *Additive Combinatorics.* Cambridge Studies in Advanced Mathematics 105, Cambridge University Press, 2006.

## 10. Worked Example / Concrete Special Case

**(a) The conjecture fails in $\mathbb{Z}_7$.** Take the Singer perfect difference set $D = \{1,2,4\} \subseteq \mathbb{Z}_7$ (parameters $q=2$, $m = q^2+q+1 = 7$) and adjoin $0$: let $A = \{0,1,2,4\}$. List all unordered sums mod 7:

| pair | 0+0 | 0+1 | 0+2 | 0+4 | 1+1 | 1+2 | 1+4 | 2+2 | 2+4 | 4+4 |
|---|---|---|---|---|---|---|---|---|---|---|
| sum | 0 | 1 | 2 | 4 | 2 | 3 | 5 | 4 | 6 | 1 |

Hence $r_A(0)=1$, $r_A(1)=2$, $r_A(2)=2$, $r_A(3)=1$, $r_A(4)=2$, $r_A(5)=1$, $r_A(6)=1$. So $1 \le r_A(n) \le 2$ for **every** $n \in \mathbb{Z}_7$: a basis of order 2 with representation function bounded by 2. This is the finite shadow of Chen's theorem, and shows that no argument using only the additive group structure can prove the conjecture.

**(b) The conjecture holds for $C=1$ over $\mathbb{N}_0$.** Suppose $A \subseteq \mathbb{N}_0$ satisfies $r_A(n) \le 1$ for all $n$ (a Sidon set) and is a basis of order 2. Take $N = 10^4$.

- Erdős–Turán (2.3): $A(N) \le N^{1/2} + N^{1/4} + 1 = 100 + 10 + 1 = 111$.
- Basis requirement: all $n \le N$ are represented, and each pair from $A \cap [0,N]$ represents at most one $n$, so $\binom{A(N)+1}{2} \ge N$, giving $A(N) \ge \sqrt{2N} - 1 \approx 141.4 - 1 = 140.4$, i.e. $A(N) \ge 141$.

Since $141 > 111$, no such $A$ exists. The contradiction is not asymptotic sleight of hand: it bites already at $N = 10^4$, and the ratio $\sqrt{2N}/(\sqrt{N}+N^{1/4})$ tends to $\sqrt 2 > 1$, so it persists for all larger $N$.

**(c) Why this does not generalize.** For $r_A(n) \le C$ with $C \ge 2$, the Sidon bound (2.3) becomes $A(x) \le \sqrt{2Cx}(1+o(1))$ by a $B_2[C]$-type count, while the basis requirement gives only $A(x) \ge \sqrt{2x}(1+o(1))$. For $C \ge 2$ the two are compatible — the window $\sqrt{2x} \le A(x) \le \sqrt{2Cx}$ is nonempty. Closing that window for every $C$ is precisely the open problem.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*