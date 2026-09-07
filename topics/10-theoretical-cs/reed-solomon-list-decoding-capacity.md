---
id: 10-theoretical-cs/reed-solomon-list-decoding-capacity
title: "Reed-Solomon List Decoding Capacity"
topic: 10-theoretical-cs
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Reed-Solomon List Decoding Capacity

> **Topic:** Theoretical Computer Science · **ID:** `10-theoretical-cs/reed-solomon-list-decoding-capacity` · **Status:** open

## 1. Problem Statement / Conjecture

Reed–Solomon (RS) codes are the canonical MDS codes: encode a message as a low-degree polynomial and evaluate it at $n$ distinct field points. The question is how many errors an RS code can tolerate when the decoder is allowed to output a short *list* of candidates rather than a single codeword.

Two questions, both open in their strong forms.

- **(Q1) Explicit combinatorial capacity.** Is there an explicit (deterministic, polynomial-time constructible) sequence of evaluation sets $S_n \subseteq \mathbb{F}_q$, $|S_n| = n$, $q = \mathrm{poly}(n)$, such that the RS code $\mathrm{RS}_{S_n,k}$ of rate $R = k/n$ is $\big(1 - R - \varepsilon,\, O(1/\varepsilon)\big)$-list-decodable for every $\varepsilon > 0$? All current capacity proofs are probabilistic or generic; no explicit evaluation set is known to beat the Johnson radius $1 - \sqrt{R}$.
- **(Q2) Algorithmic capacity.** Is there a polynomial-time algorithm that, given a received word $y$, outputs all codewords within relative distance $1 - R - \varepsilon$ of $y$, for *any* RS code known to be combinatorially list-decodable at that radius? No polynomial-time RS list-decoder is known past $1 - \sqrt{R}$, for any evaluation set.

A complete resolution of (Q1) means an explicit construction with a proof of the list-size bound; a complete resolution of (Q2) means an algorithm with a running-time and correctness proof, or a hardness result (e.g. under a standard assumption) ruling it out. Secondary open question: the optimal field size $q$ as a function of $n, \varepsilon, L$.

## 2. Mathematical Foundations

Fix a finite field $\mathbb{F}_q$, a set of distinct evaluation points $S = \{\alpha_1,\dots,\alpha_n\} \subseteq \mathbb{F}_q$, and $k \le n$. The Reed–Solomon code is
$$\mathrm{RS}_{S,k} = \big\{ \big(f(\alpha_1),\dots,f(\alpha_n)\big) : f \in \mathbb{F}_q[x],\ \deg f < k \big\} \subseteq \mathbb{F}_q^n .$$
It has rate $R = k/n$ and minimum Hamming distance $d = n-k+1$, meeting the Singleton bound (MDS).

**List decodability.** A code $C \subseteq \mathbb{F}_q^n$ is $(\rho, L)$-list-decodable if for every $y \in \mathbb{F}_q^n$,
$$\big|\{ c \in C : \Delta(y,c) \le \rho n \}\big| \le L,$$
where $\Delta$ is Hamming distance.

**Capacity.** A random code of rate $R$ over a large alphabet is $(1-R-\varepsilon, O(1/\varepsilon))$-list-decodable; conversely no code of rate $R$ is $(1-R+\varepsilon, \mathrm{poly}(n))$-list-decodable. So $\rho^\ast(R) = 1-R$ is the *list-decoding capacity* over large alphabets.

**Johnson bound.** Any code of relative distance $\delta$ is $(1-\sqrt{1-\delta},\, O(n^2))$-list-decodable. For MDS codes $\delta \to 1-R$, giving the *Johnson radius*
$$\rho_J(R) = 1 - \sqrt{R}.$$
This is combinatorial and holds for every evaluation set.

**Guruswami–Sudan.** For all $R$, there is an $O(\mathrm{poly}(n))$ algorithm listing all codewords within relative radius $1-\sqrt{R}$, via bivariate interpolation with multiplicity $m$: find $Q(x,y) \ne 0$ with a zero of multiplicity $m$ at each $(\alpha_i, y_i)$ and weighted degree $< m(n - t)$; every $f$ agreeing with $y$ in $\ge t > \sqrt{kn}$ places satisfies $(y - f(x)) \mid Q$.

**Generalized Singleton bound (Shangguan–Tamo).** If a code of rate $R$ and length $n$ is $(\rho, L)$-list-decodable, then
$$\rho \le \frac{L}{L+1}\left(1 - R + \frac{1}{n}\right),$$
equivalently $\rho n \le \frac{L}{L+1}(n-k+1)$. Setting $L = \lceil 1/\varepsilon \rceil$ recovers capacity: $\rho \to 1-R$ as $L \to \infty$. A code meeting this with equality for all $L$ is said to *achieve list-decoding capacity with optimal list size*.

**Higher-order MDS.** Brakensiek–Gopi–Makam define $\mathrm{MDS}(\ell)$: a code whose generator matrix satisfies, for all $\ell$-tuples of column subsets $\mathcal{I}_1,\dots,\mathcal{I}_\ell$,
$$\dim\Big(\bigcap_{j} \mathrm{span}(\mathcal{I}_j)\Big) = \text{the generic (minimum possible) value}.$$
Their theorem: $C$ is $\mathrm{MDS}(L+1)$ $\iff$ $C$ meets the generalized Singleton bound with list size $L$.

## 3. History & State of the Art (SOTA)

- **1960:** Reed and Solomon introduce the codes.
- **1957/1962:** Johnson's bound, later recognized as the generic list-decoding limit from distance alone. Elias and Wozencraft introduce list decoding (1957–58).
- **1997:** Sudan decodes RS beyond $\tfrac{1}{2}(1-R)$ for $R < 1/3$.
- **1999:** Guruswami–Sudan reach the Johnson radius $1-\sqrt{R}$ for all rates, in polynomial time. This has remained the algorithmic record for plain RS codes for 27 years.
- **2005–2007:** Guruswami–Vardy prove maximum-likelihood decoding of RS is NP-hard; Cheng–Wan link RS list decoding in certain parameter regimes to discrete logarithm.
- **2008:** Guruswami–Rudra show *folded* RS codes achieve capacity explicitly and algorithmically — but folding changes the code, leaving plain RS open.
- **2010:** Ben-Sasson–Kopparty–Radhakrishnan use subspace polynomials to exhibit RS codes (full-length, structured evaluation sets) with superpolynomial list sizes near the Johnson radius: capacity cannot hold for *all* evaluation sets.
- **2014–2015:** Rudra–Wootters show random puncturings of RS codes are list-decodable beyond Johnson.
- **2020–2021:** Shangguan–Tamo state the generalized Singleton bound and prove RS codes attaining it for $L = 2, 3$; Guo–Li–Shangguan–Tamo–Wootters improve list-decodability via tree packings.
- **2023:** Brakensiek–Gopi–Makam prove *generic* RS codes achieve the generalized Singleton bound for every $L$ (exponential field size). Guo–Zhang prove randomly punctured RS codes achieve capacity over fields of size $O_\varepsilon(n^2)$.
- **2024–2025:** Alrabiah–Guruswami–Li reduce the field size to $O_\varepsilon(n)$, which is optimal up to the $\varepsilon$-dependence; Brakensiek–Dhar–Gopi–Zhang show AG codes cannot substitute for RS here; Chen–Zhang and Srivastava sharpen explicit folded-RS list sizes.

## 4. Partial Results / Verified Cases

- **Johnson regime, all parameters.** Every RS code, any $S$, any $q$: $(1-\sqrt{R}, O(n^2))$-list-decodable, decodable in polynomial time (Guruswami–Sudan 1999). Recent work shows the list size in this regime is in fact $O(1/\varepsilon)$-ish for random codes.
- **Small list sizes exactly.** $L = 1$ (unique decoding, radius $\tfrac12(1-R+1/n)$) is classical Berlekamp–Massey. $L = 2, 3$: Shangguan–Tamo construct RS codes meeting the generalized Singleton bound over fields of size $O(n^2)$ / $O(n^3)$.
- **Generic evaluation points.** Brakensiek–Gopi–Makam: RS codes with generic (algebraically independent) evaluation points meet $\rho = \frac{L}{L+1}(1-R+\frac1n)$ for all $L$; field size initially $q = 2^{\Omega(n)}$, improved to $q = n^{O(L)}$ by Brakensiek–Dhar–Gopi.
- **Random evaluation points, linear field size.** Alrabiah–Guruswami–Li (2024): for $q = O_\varepsilon(n)$, a uniformly random $S \subseteq \mathbb{F}_q$ of size $n$ yields, with high probability, an RS code that is $(1-R-\varepsilon, O(1/\varepsilon))$-list-decodable. This settles the *existential/combinatorial* form of the question up to constants.
- **Explicit capacity for modified codes.** Folded RS (Guruswami–Rudra 2008) and univariate multiplicity codes achieve capacity explicitly and algorithmically; Chen–Zhang (2024) and Srivastava (2025) give folded-RS list sizes $O(1/\varepsilon)$, matching the generalized Singleton bound up to constants.
- **Negative case.** Full-length RS codes over $\mathbb{F}_{2^m}$ with subspace-structured evaluation sets fail badly beyond Johnson (Ben-Sasson–Kopparty–Radhakrishnan 2010).

## 5. Principal Obstacles

- **Interpolation is stuck at Johnson.** The Guruswami–Sudan method finds a single low-degree $Q(x,y)$ vanishing at the $n$ points. Parameter counting caps the achievable agreement at $\sqrt{kn}$: past that, the interpolation ideal is either empty or contains spurious factors. Folded RS breaks the barrier only by adding *correlated* symbols (consecutive evaluations $f(\gamma^i x)$) that give extra algebraic constraints; plain RS supplies no such extra structure.
- **Probabilistic proofs are non-constructive by design.** The BGM/Guo–Zhang/AGL proofs bound the probability that a random evaluation set makes some $(L+1) \times (L+1)$-type intersection matrix degenerate. They are union bounds over exponentially many bad configurations — they certify existence but give no efficiently checkable witness for a fixed $S$.
- **No certification.** Deciding whether a *given* RS code is $\mathrm{MDS}(\ell)$ appears to require checking exponentially many subspace intersection conditions; no polynomial-time certificate is known. So even a candidate explicit $S$ cannot currently be verified.
- **Structured sets are provably bad.** Any explicit construction must avoid subfield/subspace structure (BKR), which is exactly the structure that makes evaluation sets explicit and analyzable. This is the same tension as in explicit Ramsey graphs or rigid matrices: the properties are generic, and derandomizing genericity is the hard part.
- **Hardness shadows.** Guruswami–Vardy (NP-hardness of ML decoding) and Cheng–Wan (discrete-log reductions) show that some natural RS decoding tasks past Johnson are computationally hard, so (Q2) may not have a positive answer in full generality — but the hard instances are not the capacity-achieving regime, so they do not settle it.

## 6. The Gap

Proven: random/generic evaluation sets over $q = O_\varepsilon(n)$ give list-decodability at radius $1-R-\varepsilon$ with list size $O(1/\varepsilon)$. Missing, in order of difficulty:

1. **Derandomization.** Turn "a random $S$ works with probability $1-o(1)$" into a specific $S$ described by an $O(\log n)$-space algorithm. The needed step is a pseudorandom generator, or an algebraic invariant, that certifies the higher-order MDS conditions — equivalently, a low-complexity object fooling all $\binom{n}{\le L k}$ intersection tests.
2. **Algorithm.** Even granting a capacity-achieving RS code, produce the list. This requires a decoding principle fundamentally different from bivariate interpolation, since the interpolation lower bound at $\sqrt{kn}$ agreement is tight for the method.
3. **Exact list size and field size.** Determine the optimal constant in $L = \Theta(1/\varepsilon)$ and whether $q = (1+o(1))n$ suffices.

## 7. Current Research (as of June 2026)

- **Field-size optimization for randomly punctured RS.** Following Alrabiah–Guruswami–Li, groups at CMU, Berkeley, and Microsoft Research are pushing the $\varepsilon$-dependence in $q = O_\varepsilon(n)$ toward $q = O(n/\varepsilon)$ and asking whether $q = n + O(1)$ is possible. *(frontier — verify)*
- **Higher-order MDS theory.** Brakensiek, Dhar, Gopi and collaborators continue to map $\mathrm{MDS}(\ell)$, its field-size requirements, and its links to matroid/Schubert-calculus generic intersection conditions — the most promising route to a certifiable explicit construction.
- **Partial derandomization.** Reducing the randomness needed to sample a good $S$ from $n \log q$ bits to $O(\log n)$ bits, e.g. via limited-independence or algebraic-geometry-flavored evaluation sets. *(frontier — verify)*
- **Explicit folded/multiplicity codes.** Chen–Zhang, Srivastava, Tamo and others tighten list sizes to the exact generalized Singleton value; a partial transfer of these ideas back to unfolded RS is being attempted.
- **Barriers for AG codes.** Brakensiek–Dhar–Gopi–Zhang's "no list-decoding friends" result shows AG codes need exponential alphabets to meet the bound exactly, isolating RS as special and refocusing effort on RS-specific tools.
- **List recovery and soft decoding.** Extensions of the capacity results to list recovery (where each position gives a set of candidates) remain harder, with known separations.

## 8. Future Work

- Find an efficiently checkable algebraic invariant of $S$ implying $\mathrm{MDS}(L+1)$ — the analogue of what "MDS" is for $L = 1$.
- Prove or refute: any polynomial-time algorithm list-decoding *some* rate-$R$ RS family beyond $1-\sqrt{R}$ implies a breakthrough for a known hard problem (a formal barrier for (Q2)).
- Extract from folded RS a "virtual folding" of plain RS: identify structure in a generic evaluation set that plays the role of the Frobenius/multiplicative shift.
- Determine the true trade-off curve $L(\rho, R)$ for RS codes over $q = \Theta(n)$, including the constant in $L = \Theta(1/\varepsilon)$.
- Settle whether *every* RS code with $n \le q/2$ and random-like $S$ is list-decodable at capacity, or whether adversarial-but-explicit $S$ can fail.

## 9. Key References

- **[Foundational]** M. Sudan. *Decoding of Reed–Solomon Codes beyond the Error-Correction Bound.* Journal of Complexity, 13(1):180–193, 1997.
- **[Foundational]** V. Guruswami and M. Sudan. *Improved Decoding of Reed–Solomon and Algebraic-Geometry Codes.* IEEE Transactions on Information Theory, 45(6):1757–1767, 1999.
- **[Foundational]** V. Guruswami and A. Rudra. *Explicit Codes Achieving List Decoding Capacity: Error-Correction with Optimal Redundancy.* IEEE Transactions on Information Theory, 54(1):135–150, 2008.
- **[Barrier]** E. Ben-Sasson, S. Kopparty, J. Radhakrishnan. *Subspace Polynomials and Limits to List Decoding of Reed–Solomon Codes.* IEEE Transactions on Information Theory, 56(1):113–120, 2010.
- **[Hardness]** V. Guruswami and A. Vardy. *Maximum-Likelihood Decoding of Reed–Solomon Codes is NP-Hard.* IEEE Transactions on Information Theory, 51(7):2249–2256, 2005.
- **[Hardness]** Q. Cheng and D. Wan. *On the List and Bounded Distance Decodability of Reed–Solomon Codes.* SIAM Journal on Computing, 37(1):195–209, 2007.
- **[Key bound]** C. Shangguan and I. Tamo. *Combinatorial List-Decoding of Reed–Solomon Codes beyond the Johnson Radius.* Proc. STOC 2020, ACM, pp. 538–551.
- **[SOTA]** J. Brakensiek, S. Gopi, V. Makam. *Generic Reed–Solomon Codes Achieve List-Decoding Capacity.* Proc. STOC 2023, ACM.
- **[SOTA]** Z. Guo and Z. Zhang. *Randomly Punctured Reed–Solomon Codes Achieve List-Decoding Capacity over Linear-Sized Fields.* Proc. FOCS 2023, IEEE.
- **[SOTA]** O. Alrabiah, V. Guruswami, R. Li. *Randomly Punctured Reed–Solomon Codes Achieve List-Decoding Capacity over Linear-Sized Fields.* Proc. FOCS 2024, IEEE. (Field size $O_\varepsilon(n)$.)
- **[SOTA]** J. Brakensiek, M. Dhar, S. Gopi, Z. Zhang. *AG Codes Have No List-Decoding Friends: Approaching the Generalized Singleton Bound Requires Exponential Alphabets.* Proc. SODA 2024, SIAM.
- **[Recent]** S. Srivastava. *Improved List Size for Folded Reed–Solomon Codes.* Proc. SODA 2025, SIAM.
- **[Recent]** Y. Chen and Z. Zhang. *Explicit Folded Reed–Solomon and Multiplicity Codes Achieve Relaxed Generalized Singleton Bound.* Proc. STOC 2024, ACM.
- **[Prior]** A. Rudra and M. Wootters. *Every List-Decodable Code for High Noise Has Abundant Near-Optimal Rate Puncturings.* Proc. STOC 2014, ACM.
- **[Survey]** V. Guruswami. *Algorithmic Results in List Decoding.* Foundations and Trends in Theoretical Computer Science, 2(2):107–195, 2007.
- **[Book]** V. Guruswami, A. Rudra, M. Sudan. *Essential Coding Theory.* Draft textbook, 2019.

## 10. Worked Example / Concrete Special Case

Take $q = 7$, $S = \{1,2,3,4,5,6\} \subseteq \mathbb{F}_7$, $n = 6$, $k = 2$. So $R = 1/3$, $d = n-k+1 = 5$, and codewords are evaluations of lines $f(x) = a + bx$.

**Radii.**

| Notion | Formula | Value (errors out of 6) |
|---|---|---|
| Unique decoding | $\lfloor (d-1)/2 \rfloor$ | $2$ |
| Johnson | $(1-\sqrt{R})\,n = (1-0.5774)\cdot 6 = 2.54$ | $2$ |
| Generalized Singleton, $L=2$ | $\frac{2}{3}(n-k+1) = \frac{2}{3}\cdot 5 = 3.33$ | $3$ |
| Capacity $1-R$ | $\frac{2}{3}\cdot 6 = 4$ | $4$ |

**A received word with list size exactly 2 at radius 3.** Let $y = (0,0,0,1,3,5)$, indexed by $\alpha = 1,\dots,6$.

- $f_1(x) = 0$ agrees with $y$ at $\alpha \in \{1,2,3\}$ — distance $3$.
- $f_2(x) = 2x$ gives $(2,4,6,1,3,5)$; it agrees with $y$ at $\alpha \in \{4,5,6\}$ — distance $3$.

Any third line $g$ within distance $3$ must agree with $y$ in at least $3$ of the $6$ positions. Two distinct degree-$<2$ polynomials agree in at most $k-1 = 1$ point, so $g$ agrees with $f_1$ in $\le 1$ position and with $f_2$ in $\le 1$ position. Since the agreement sets of $f_1$ and $f_2$ with $y$ partition all six positions, $g$ can match $y$ in at most $2$ positions. Hence the list at radius $3$ is exactly $\{f_1, f_2\}$, size $2$ — meeting the generalized Singleton bound $\frac{L}{L+1}(n-k+1)$ with $L = 2$.

**Why this is the open problem in miniature.** Radius $3 > 2.54$ is strictly beyond the Johnson radius, so Guruswami–Sudan interpolation, run on this $y$, is not guaranteed to return $\{f_1,f_2\}$: the interpolation constraint needs agreement $t > \sqrt{kn} = \sqrt{12} \approx 3.46$, i.e. $t \ge 4$, and here $t = 3$. The two codewords exist and the list is short — combinatorics is fine — but no known polynomial-time algorithm finds them for a general RS code at this radius.

**Counting at capacity.** At radius $4$ (agreement $2$), every pair of positions determines a line, so up to $\binom{6}{2} = 15$ codewords can lie in the ball. This is why capacity needs list size growing like $1/\varepsilon$: the generalized Singleton bound with $\rho n = 4$ forces $\frac{L}{L+1} \ge 4/5$, i.e. $L \ge 4$.

**The general shape.** The theorems of Brakensiek–Gopi–Makam and Alrabiah–Guruswami–Li say that if the six points $\{1,\dots,6\}$ are replaced by a *random* six-element subset of a field of size $O(n/\varepsilon^{O(1)})$, then the analogue of the argument above holds at every radius up to $1-R-\varepsilon$ with list size $O(1/\varepsilon)$ — whp. Writing down one specific such set, and decoding it, is what remains open.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*