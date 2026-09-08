---
id: 07-combinatorics/bh-sidon-sets-growth-problem
title: "Sidon Set Growth in Finite Abelian Groups (Erdős–Turán B_h Problem)"
topic: 07-combinatorics
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Sidon Set Growth in Finite Abelian Groups (Erdős–Turán $B_h$ Problem)

> **Topic:** Combinatorics & Graph Theory · **ID:** `07-combinatorics/bh-sidon-sets-growth-problem` · **Status:** open

## 1. Problem Statement / Conjecture

Let $G$ be a finite abelian group of order $n$ and let $h \ge 2$. A set $A \subseteq G$ is a **$B_h$ set** if every element of $G$ has at most one representation as a sum of $h$ elements of $A$, counted up to reordering. Write
$$F_h(G) \;=\; \max\{|A| : A \subseteq G,\ A \text{ is a } B_h \text{ set}\}, \qquad F_h(n) = F_h(\mathbb{Z}_n).$$

Counting multisets gives $\binom{|A|+h-1}{h} \le n$, hence $F_h(G) \le (h!\,n)^{1/h}(1+o(1))$. The best known constructions (Bose–Chowla) give $F_h(\mathbb{Z}_{q^h-1}) \ge q \sim n^{1/h}$.

**The problem.** Determine
$$\sigma_h \;=\; \limsup_{n\to\infty} \frac{F_h(\mathbb{Z}_n)}{n^{1/h}} \quad\text{and}\quad \underline{\sigma}_h = \liminf_{n\to\infty} \frac{F_h(\mathbb{Z}_n)}{n^{1/h}}.$$
Known: $1 \le \underline\sigma_h \le \sigma_h \le (h!)^{1/h} \approx h/e$. For $h=2$ the answer is $\sigma_2 = \underline\sigma_2 = 1$ (matching Singer's perfect difference sets and the trivial bound). **For every $h \ge 3$ the value of $\sigma_h$ is open**, and even the qualitative question is open:

> Is $\sigma_h > 1$ for some $h \ge 3$? Equivalently, is there any infinite family of finite abelian groups admitting $B_h$ sets of size $(1+\varepsilon)|G|^{1/h}$?

A complete solution means either (a) a construction beating $n^{1/h}$ by a constant factor for some $h\ge 3$, or (b) a proof that $F_h(G) \le (1+o(1))|G|^{1/h}$ for all abelian $G$. A refined form asks for $\sigma_h$ exactly, and for the dependence on the group's structure (cyclic vs. elementary abelian $\mathbb{F}_p^d$).

## 2. Mathematical Foundations

**Definitions.** For $A \subseteq G$ and $x \in G$ let
$$r_h(A,x) = \\#\{(a_1,\dots,a_h) \in A^h : a_1 + \cdots + a_h = x,\ a_1 \preceq \cdots \preceq a_h\}$$
for a fixed linear order $\preceq$ on $G$. Then $A$ is a $B_h$ set iff $r_h(A,x) \le 1$ for all $x$, and a $B_h[g]$ set iff $r_h(A,x) \le g$. $B_2$ sets are **Sidon sets**: equivalently, all nonzero differences $a - a'$ ($a \ne a'$) are distinct.

**The $h=2$ counting bound.** Differences are distinct and nonzero, so
$$|A|(|A|-1) \le n-1 \quad\Longrightarrow\quad |A| \le \tfrac{1}{2}\bigl(1+\sqrt{4n-3}\bigr).$$
Equality holds iff $A$ is a **planar (perfect) difference set**.

**General $h$.** Distinct multisets have distinct sums, so
$$\binom{|A|+h-1}{h} \le n, \qquad |A| \le (h!\,n)^{1/h} + O_h(n^{1/(h-1)\cdot\frac{h-1}{h}\cdot\frac12}) = (h!\,n)^{1/h}(1+o(1)).$$

**Fourier characterization.** With $\widehat{1_A}(\chi) = \sum_{a\in A}\chi(a)$ over characters $\chi \in \widehat G$, the $B_h[g]$ condition is equivalent to an $L^{2h}$ bound:
$$\sum_{\chi \in \widehat{G}} |\widehat{1_A}(\chi)|^{2h} \;=\; n \sum_{x\in G} \tilde r_h(A,x)^2,$$
where $\tilde r_h$ counts ordered representations. For a $B_h$ set this forces
$$\frac{1}{n}\sum_{\chi} |\widehat{1_A}(\chi)|^{2h} \le h!\,|A|^h,$$
i.e. $\|\widehat{1_A}\|_{2h}$ is as small as the Rudin-type extremal allows. Sidon sets are exactly the sets whose $L^4$ Fourier norm is minimal.

**Transference between $\mathbb{Z}_n$ and $[1,n]$.** If $A \subseteq \mathbb{Z}_n$ is $B_h$, its representatives in $[0,n)$ form a $B_h$ set of integers, so $F_h(\mathbb{Z}_n) \le F_h([n])$. Conversely a $B_h$ set in $[1,n]$ is $B_h$ modulo any $m > hn$, so $F_h([n]) \le F_h(\mathbb{Z}_{hn+1})$. Hence the cyclic and integer constants agree up to the factor $h^{1/h} \to 1$; the group problem and the interval problem are asymptotically the same question.

**Bose–Chowla theorem.** Let $q$ be a prime power, $\theta$ a generator of $\mathbb{F}_{q^h}^\times$. Then
$$A_\theta = \{\, a \in [1, q^h-1] : \theta^a - \theta \in \mathbb{F}_q \,\}$$
is a $B_h$ set of size $q$ in $\mathbb{Z}_{q^h-1}$. For $h=2$, Singer's construction gives a $B_2$ set of size $q+1$ in $\mathbb{Z}_{q^2+q+1}$, meeting the counting bound exactly.

## 3. History & State of the Art (SOTA)

- **1932–1941.** Sidon posed the question to Erdős in the context of $L^4$ norms of Fourier series. Erdős and Turán (*J. London Math. Soc.*, 1941) proved $F_2([n]) \le n^{1/2} + O(n^{1/4})$.
- **1938–1942.** Singer's projective-plane difference sets, then Bose's affine analogue, give $F_2(\mathbb{Z}_{q^2+q+1}) = q+1$ — asymptotically optimal, and (by prime gaps) $F_2([n]) \ge n^{1/2} - O(n^{0.263})$.
- **1962.** Bose–Chowla extend the construction to all $h$, giving $\underline\sigma_h \ge 1$.
- **1969.** Lindström sharpens the Sidon bound to $F_2([n]) \le n^{1/2} + n^{1/4} + 1$, and proves $F_4([n]) \le (8n)^{1/4} + O(n^{1/8})$, the first improvement over the trivial constant $(4!\cdot 4)^{1/4}$ for $h=4$.
- **1990s–2001.** Improvements to the $h \ge 3$ constants: Chen (1994) and Jia (1994) for even $h$; Green (*Acta Arithmetica*, 2001) gives the strongest general upper bounds, e.g. $\sigma_3 \le 7^{1/3} \approx 1.913$ against the trivial $18^{1/3} \approx 2.62$, and improved constants for $B_h[g]$.
- **2002–2012.** Cilleruelo, Ruzsa, Trujillo and Vinuesa develop the $B_h[g]$ theory and finite-field methods; Cilleruelo (*Combinatorica*, 2012) links Sidon sets in $\mathbb{F}_p^2$-type settings to point-counting on curves.
- **2023.** Balogh, Füredi and Roy shave the $h=2$ second-order term to $F_2([n]) \le \sqrt n + 0.998\, n^{1/4}$ — the first improvement on Lindström's constant $1$ in over fifty years.

## 4. Partial Results / Verified Cases

- **$h = 2$, cyclic groups: solved asymptotically.** $F_2(\mathbb{Z}_n) = (1+o(1))\sqrt n$; exact equality $F_2(\mathbb{Z}_{q^2+q+1}) = q+1$ for every prime power $q$ (Singer).
- **$h = 2$, elementary abelian:** in $\mathbb{F}_2^d$, Sidon sets of size $2^{\lceil d/2\rceil}$ exist (Bose-type / Kerdock constructions) and $|A| \le 2^{d/2}(1+o(1))$; the exact maximum is known only for small $d$. In $\mathbb{F}_3^d$ the maximum Sidon set size is determined for $d \le 5$ (Huang–Tait–Won, 2019).
- **Upper bounds with constants $<(h!)^{1/h}$:** for $h = 3$, $\sigma_3 \le 7^{1/3}$ (Green); for $h = 4$, $\sigma_4 \le 8^{1/4} \approx 1.682$ (Lindström) versus trivial $24^{1/4}\approx 2.21$; general even $h=2k$ bounds of shape $\sigma_{2k} \le \bigl(k\cdot (k!)^2\bigr)^{1/2k}$-type from Jia/Chen/Green.
- **$B_h[g]$ variants:** for $g$ large the truth is known to differ from the naive counting heuristic — Cilleruelo–Ruzsa–Vinuesa showed the extremal density of $B_2[g]$ sets is *not* asymptotically $\sqrt{g\,n}$, disproving the natural guess, so the "counting bound is tight" intuition provably fails somewhere in this family.
- **Small-parameter verification:** $F_h(\mathbb{Z}_n)$ has been computed exhaustively for small $n$ and $h \in \{2,3,4\}$; the tables (compiled in O'Bryant's dynamic survey) show no example with $F_h(\mathbb{Z}_n) > (1+\varepsilon)n^{1/h}$ persisting as $n$ grows.

## 5. Principal Obstacles

- **Constructions are algebraic and rigid.** Every known $B_h$ set of size $\asymp n^{1/h}$ comes from $\mathbb{F}_{q^h}^\times$ (Bose–Chowla, Singer, Ruzsa's $\mathbb{Z}_{p^2-p}$ construction). These give exactly $q$ or $q+1$ elements; the field structure caps the size at the degree of the extension. There is no known deformation, union, or probabilistic augmentation that adds a constant factor without destroying the $B_h$ property.
- **Random methods lose the exponent.** A random subset of $G$ of size $m$ has $\approx m^{2h}/n$ collisions; deleting one element per collision leaves only $\asymp n^{1/(2h-1)}$, far below $n^{1/h}$. Random-greedy and hypergraph-container refinements improve the count of $B_h$ sets but not the maximum size.
- **Fourier analysis is one-sided.** The $L^{2h}$ identity gives upper bounds by convexity, but a $B_h$ set has *flat* Fourier transform, so there is no large spectral component to exploit — the standard structure-vs-randomness dichotomy has nothing to bite on. Improvements past the counting bound require capturing the *inefficiency* of near-extremal configurations, which for $h\ge3$ is a statement about $2h$-fold additive energy of sets with no structure.
- **The $h=2$ proofs do not generalize.** Lindström's and Erdős–Turán's arguments use that difference sets are *sets* (multiplicity 1) and a clean window/averaging argument over intervals of length $\ell$. For $h\ge 3$ the relevant object is a multiset of $h$-fold sums; the averaging loses a factor that is precisely the $(h!)^{1/h}$ discrepancy in question.
- **Second-moment slack.** All known upper-bound arguments are essentially second-moment counts. A set achieving the counting bound would have to tile the group with $h$-fold sums almost perfectly — a "perfect difference set for $h\ge3$" — and no obstruction theory (design-theoretic, character-sum, or algebraic) is known that rules such objects out beyond isolated small cases.

## 6. The Gap

Proven: $1 \le \underline\sigma_h \le \sigma_h \le c_h$ with $c_3 = 7^{1/3}$, $c_4 = 8^{1/4}$, $c_h \le (h!)^{1/h}$ in general. Conjectured (Erdős): $\sigma_h = 1$ for all $h$.

The gap is the multiplicative interval $[1, c_h]$, of width tending to $\Theta(h)$. Two distinct crossings are needed:

1. **Lower side.** Produce a $B_h$ set of size $(1+\varepsilon)|G|^{1/h}$ in some infinite family, or prove that the algebraic ceiling $q$ in $\mathbb{Z}_{q^h-1}$ is intrinsic. No non-algebraic construction of *any* $B_h$ set of size $\Omega(n^{1/h})$ is known — this is itself a notable gap in method.
2. **Upper side.** Convert the counting bound into a bound sensitive to the *distribution* of $h$-fold sums. Concretely, prove that for a $B_h$ set the sumset $hA$ cannot occupy a $\Theta(1)$ fraction of $G$ unless $A$ has algebraic structure incompatible with the $B_h$ condition. Even the case $h=3$, showing $\sigma_3 < 7^{1/3} - \delta$ for an explicit $\delta$, is an active target.

## 7. Current Research (as of June 2026)

- **Container and counting methods.** Hypergraph containers have given tight bounds on the *number* of $B_h$ sets in $[n]$ and in $\mathbb{Z}_n$, and on Sidon sets in random subsets. Groups in Illinois (Balogh), Cambridge/Oxford (Conlon, Green) and IMPA/Brazil (Kohayakawa, Sampaio) continue in this direction; the transfer to extremal *size* remains blocked. *(frontier — verify)*
- **Finite-field geometry.** Extending Cilleruelo's curve-counting approach to $B_h$ sets in $\mathbb{F}_q^d$, aiming for either better constructions or Weil-type obstructions. *(frontier — verify)*
- **Second-order term for $h=2$.** After Balogh–Füredi–Roy, work continues on pushing the coefficient of $n^{1/4}$ below $0.998$ and toward the conjectured truth (Erdős conjectured that $F_2([n]) - \sqrt n$ is unbounded but $o(n^{1/4})$). *(frontier — verify)*
- **$B_h[g]$ densities.** Following Cilleruelo–Ruzsa–Vinuesa, determining $\lim_g \beta_g/\sqrt g$ for the $B_2[g]$ density constant remains a concrete, tractable-looking open question that probes the same failure of the counting heuristic.
- **Computation.** Exhaustive and SAT/ILP-based searches for optimal $B_3$ and $B_4$ sets in $\mathbb{Z}_n$ extend the verified tables; no counterexample to $\sigma_h = 1$ has emerged.

## 8. Future Work

- Settle whether $\sigma_3 = 1$. Erdős offered prizes for progress on the Sidon-set problems; the $h=3$ constant is the first genuinely unknown case.
- Develop a non-algebraic construction of dense $B_h$ sets, even suboptimal ones with size $n^{1/h}/\log n$, to break the monoculture of $\mathbb{F}_{q^h}$-based examples.
- Prove a stability theorem: any $B_2$ set in $\mathbb{Z}_n$ of size $\ge (1-\varepsilon)\sqrt n$ is close to a Singer set. Such rigidity, if extended to $h=3$, would let counting bounds be improved by ruling out near-perfect configurations.
- Clarify the role of group structure: compare $F_h(\mathbb{Z}_n)$ with $F_h(\mathbb{F}_p^d)$ for $p^d = n$, where the vector-space setting admits linear-algebraic tools unavailable in the cyclic case.
- Connect to the infinite Erdős–Turán problem: whether every infinite Sidon set $A \subseteq \mathbb{N}$ satisfies $\liminf_x |A\cap[1,x]|/\sqrt x = 0$ (Erdős), where Ruzsa's and Cilleruelo's constructions reach counting function $x^{\sqrt2 - 1 + o(1)}$.

## 9. Key References

- **[Foundational]** P. Erdős, P. Turán. *On a problem of Sidon in additive number theory, and on some related problems.* Journal of the London Mathematical Society **16** (1941), 212–215.
- **[Foundational]** J. Singer. *A theorem in finite projective geometry and some applications to number theory.* Transactions of the American Mathematical Society **43** (1938), 377–385.
- **[Foundational]** R. C. Bose. *An affine analogue of Singer's theorem.* Journal of the Indian Mathematical Society **6** (1942), 1–15.
- **[Foundational]** R. C. Bose, S. Chowla. *Theorems in the additive theory of numbers.* Commentarii Mathematici Helvetici **37** (1962/63), 141–147.
- **[Classical]** B. Lindström. *An inequality for $B_2$-sequences.* Journal of Combinatorial Theory **6** (1969), 211–212.
- **[Classical]** B. Lindström. *A remark on $B_4$-sequences.* Journal of Combinatorial Theory **7** (1969), 276–277.
- **[SOTA]** B. Green. *The number of squares and $B_h[g]$ sets.* Acta Arithmetica **100** (2001), 365–390.
- **[SOTA]** J. Cilleruelo, I. Z. Ruzsa, C. Trujillo. *Upper and lower bounds for finite $B_h[g]$ sequences.* Journal of Number Theory **97** (2002), 26–34.
- **[SOTA]** J. Cilleruelo, I. Z. Ruzsa, C. Vinuesa. *Generalized Sidon sets.* Advances in Mathematics **225** (2010), 2786–2807.
- **[SOTA]** J. Cilleruelo. *Combinatorial problems in finite fields and Sidon sets.* Combinatorica **32** (2012), 497–511.
- **[Recent]** J. Balogh, Z. Füredi, S. Roy. *An upper bound on the size of Sidon sets.* American Mathematical Monthly **130** (2023), 437–445.
- **[Recent]** J. Cilleruelo. *Infinite Sidon sequences.* Advances in Mathematics **255** (2014), 474–486.
- **[Recent]** Y. Huang, M. Tait, R. Won. *Sidon sets and 2-caps in $\mathbb{F}_3^n$.* Involve **12** (2019), 995–1003.
- **[Survey]** K. O'Bryant. *A complete annotated bibliography of work related to Sidon sequences.* Electronic Journal of Combinatorics, Dynamic Survey DS11 (2004).
- **[Book]** H. Halberstam, K. F. Roth. *Sequences.* Springer-Verlag, 2nd edition, 1983 (Chapter II).
- **[Classical]** I. Z. Ruzsa. *Solving a linear equation in a set of integers I.* Acta Arithmetica **65** (1993), 259–282.
- **[Classical]** S. Chen. *On the size of finite Sidon sequences.* Proceedings of the American Mathematical Society **121** (1994), 353–356.

## 10. Worked Example / Concrete Special Case

**(a) $h = 2$, $G = \mathbb{Z}_{13}$: the counting bound is attained.**

The bound $|A|(|A|-1) \le 12$ gives $|A| \le 4$. Take the Singer set for $q = 3$ (so $n = q^2+q+1 = 13$):
$$A = \{0,\,1,\,3,\,9\} \subseteq \mathbb{Z}_{13}.$$
The six positive differences are $1-0=1$, $3-0=3$, $9-0=9$, $3-1=2$, $9-1=8$, $9-3=6$; their negatives mod $13$ are $12, 10, 4, 11, 5, 7$. Together: $\{1,2,3,4,5,6,7,8,9,10,11,12\}$ — every nonzero residue exactly once. So $A$ is Sidon, $|A| = 4$, and the bound is tight. This is why $\sigma_2 = 1$: Singer sets exist for every prime power $q$, and prime gaps let one interpolate.

**(b) $h = 3$, $G = \mathbb{Z}_{26}$: the bound is not attained.**

Multiset counting: a $B_3$ set of size $k$ needs $\binom{k+2}{3} \le 26$. Since $\binom{6}{3} = 20 \le 26$ and $\binom{7}{3} = 35 > 26$, the counting bound gives $F_3(\mathbb{Z}_{26}) \le 4$.

Bose–Chowla with $q=3$, $h=3$ produces a $B_3$ set of size $q = 3$ in $\mathbb{Z}_{q^3-1} = \mathbb{Z}_{26}$. So the construction gives $3$ against a bound of $4$.

The Singer set from (a) does **not** work here: in $A = \{0,1,3,9\}$ we have
$$1 + 1 + 1 \;=\; 3 \;=\; 0 + 0 + 3,$$
two different multisets with the same sum. Note this obstruction is purely additive — *any* $B_3$ set containing $0$, $1$ and the element $3 = 1+1+1$ fails, in any abelian group. This illustrates the structural point of Section 5: the $h=2$ extremal objects carry small additive relations ($c = 3a - 2b$ type) that are invisible to the Sidon condition but fatal for $h \ge 3$, and the algebraic constructions that avoid all such relations pay for it by capping at $q$ elements rather than $(h!)^{1/h} q$.

Asymptotically, the same arithmetic runs at every scale: in $\mathbb{Z}_{q^3-1}$ Bose–Chowla gives $q \approx n^{1/3}$ while the bound allows $(6n)^{1/3} \approx 1.817\, n^{1/3}$, and Green's theorem narrows this to $7^{1/3} n^{1/3} \approx 1.913\,n^{1/3}$ in the interval model. Closing the interval $[1, 1.913]$ for $h=3$ is exactly the open problem.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*