---
id: 09-probability/chvatal-sankoff-constant
title: "Longest Common Subsequence Chvatal–Sankoff Constant"
topic: 09-probability
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Longest Common Subsequence Chvátal–Sankoff Constant

> **Topic:** Probability & Stochastic Processes · **ID:** `09-probability/chvatal-sankoff-constant` · **Status:** open

## 1. Problem Statement / Conjecture

Let $X = X_1\ldots X_n$ and $Y = Y_1\ldots Y_n$ be independent strings of i.i.d. letters drawn uniformly from an alphabet $\Sigma_k$ of size $k$. Let $L_n^{(k)}$ be the length of a longest common subsequence (LCS) of $X$ and $Y$. Chvátal and Sankoff (1975) proved that

$$\gamma_k \;=\; \lim_{n\to\infty} \frac{\mathbb{E}[L_n^{(k)}]}{n}$$

exists. **The problem: determine $\gamma_k$.** No value of $\gamma_k$ is known for any $k \ge 2$ — not in closed form, and not even known to be rational or irrational. The binary case $\gamma_2$ is the canonical target.

A complete resolution would supply either an exact expression for $\gamma_k$ (or for $\gamma_2$ specifically), or a proof that no such expression exists in a specified class. Subsidiary open questions, all part of the standard problem cluster:

- Is $k \mapsto \gamma_k\sqrt{k}$ monotone? Is $\gamma_k \sqrt k$ increasing to $2$?
- Is $\mathrm{Var}(L_n^{(k)}) = \Theta(n)$ for uniform letters? (Chvátal–Sankoff conjectured $\mathrm{Var} = o(n^{2/3})$; Waterman conjectured sublinear variance.)
- Does $L_n$ obey a Tracy–Widom-type or Gaussian fluctuation law after centering and scaling?

The **Steele/Arratia conjecture** $\gamma_k = 2/(1+\sqrt{k})$ is *false* for $k = 2$: it predicts $0.828427\ldots$, above Lueker's rigorous upper bound $0.826280$.

## 2. Mathematical Foundations

**Subsequences.** For $x \in \Sigma_k^n$, a subsequence is $x_{i_1}x_{i_2}\cdots x_{i_m}$ with $1 \le i_1 < \cdots < i_m \le n$. Then
$$L(x,y) = \max\{ m : \exists\, \text{common subsequence of } x,y \text{ of length } m\}.$$

**Dynamic program.** With $D_{i,j} = L(x_1\ldots x_i,\, y_1\ldots y_j)$,
$$D_{i,j} = \begin{cases} D_{i-1,j-1} + 1, & x_i = y_j,\\ \max(D_{i-1,j},\, D_{i,j-1}), & x_i \ne y_j,\end{cases} \qquad D_{0,j}=D_{i,0}=0 .$$
This is the Wagner–Fischer recursion, computable in $O(n^2)$ time.

**Existence of the limit.** For independent blocks, $L_{m+n} \ge L_m + L_n'$ where $L_n'$ is the LCS of the second blocks, so $a_n := \mathbb{E}[L_n]$ is superadditive: $a_{m+n} \ge a_m + a_n$. Fekete's lemma gives
$$\gamma_k = \lim_{n\to\infty}\frac{a_n}{n} = \sup_{n\ge 1}\frac{a_n}{n},$$
so **every finite $n$ yields a rigorous lower bound** $\gamma_k \ge \mathbb{E}[L_n]/n$. Kingman's subadditive ergodic theorem upgrades this to $L_n/n \to \gamma_k$ almost surely and in $L^1$.

**Concentration.** $L_n$ changes by at most $1$ when a single letter is changed, so the bounded-differences (Azuma–Hoeffding / McDiarmid) inequality gives
$$\mathbb{P}\big(|L_n - \mathbb{E}L_n| \ge t\big) \;\le\; 2\exp\!\left(-\frac{t^2}{4n}\right).$$

**Rate of convergence.** Alexander (1994), via his approximate-subadditivity machinery, proved
$$\gamma_k - \frac{\mathbb{E}[L_n]}{n} \;\le\; C\sqrt{\frac{\log n}{n}} ,$$
so the Fekete lower bounds converge at rate $\tilde O(n^{-1/2})$ — the key quantitative tool making finite-$n$ computation useful.

**Large-alphabet asymptotics.** Sankoff and Mainville conjectured $\lim_{k\to\infty}\gamma_k\sqrt{k} = 2$, the constant $2$ echoing the Vershik–Kerov / Logan–Shepp constant for the longest increasing subsequence of a random permutation ($\mathbb{E}[\mathrm{LIS}_n]\sim 2\sqrt n$). Kiwi, Loebl and Matoušek (2005) proved it.

## 3. History & State of the Art

- **1975.** Chvátal and Sankoff, *J. Appl. Probab.* 12, introduce the problem, prove existence of $\gamma_k$ by superadditivity, and give first bounds ($0.727 \le \gamma_2 \le 0.866$).
- **1978–79.** Deken sharpens to $0.7615 \le \gamma_2 \le 0.8575$ using a first-moment/counting upper bound over "canonical" alignments.
- **1982.** Steele connects LCS to proximity of random strings and popularizes the $2/(1+\sqrt k)$ speculation.
- **1994.** Alexander's convergence-rate theorem. Dančík and Paterson (MFCS 1994; Dančík's Warwick thesis) introduce automaton/dominance methods: $0.77391 \le \gamma_2 \le 0.83763$.
- **1999.** Baeza-Yates, Gavaldá, Navarro, Scheihing give bounds for $k \ge 3$; Boutet de Monvel's large-scale simulations estimate $\gamma_2 \approx 0.8122$.
- **2005.** Kiwi–Loebl–Matoušek prove $\gamma_k\sqrt k \to 2$ (*Adv. Math.* 197).
- **2009.** **Lueker** (*JACM* 56(3)) obtains the still-standing rigorous binary bounds
 $$0.788071 \;\le\; \gamma_2 \;\le\; 0.826280,$$
 disproving $\gamma_2 = 2/(1+\sqrt2)$.
- **2009.** Lember and Matzinger prove $\mathrm{Var}(L_n) = \Theta(n)$ for a biased binary model (*Ann. Probab.* 37), contradicting sublinear-variance folklore in that regime.
- **2022.** Bukh and Cox, *Periodic words, common subsequences and frogs* (*Ann. Appl. Probab.*), refine the large-$k$ expansion beyond the leading $2/\sqrt k$ term.

## 4. Partial Results / Verified Cases

**Rigorous numeric intervals.** Lueker's automaton-plus-power-iteration method certifies $\gamma_2 \in [0.788071, 0.826280]$, an interval of width $0.038$. For larger alphabets the published rigorous ranges (Dančík–Paterson; Baeza-Yates et al.; Lueker's framework) include roughly
$\gamma_3 \in [0.671, 0.765]$, $\gamma_4 \in [0.599, 0.709]$, $\gamma_{10} \in [0.40, 0.49]$ — every interval is nonempty and no endpoint is tight.

**Asymptotic regime $k \to \infty$ — solved to leading order.** Kiwi–Loebl–Matoušek: $\gamma_k = \frac{2}{\sqrt k}(1+o(1))$. Bukh–Cox sharpen the second-order term, giving $\gamma_k \le \frac{2}{\sqrt k} - \frac{c}{k}$ for an explicit $c>0$ and matching-order lower bounds; so the *shape* $2/\sqrt{k} - \Theta(1/k)$ is established, while the coefficient of $1/k$ is not.

**Structural theorems proved unconditionally.**
- Existence and a.s. convergence (Chvátal–Sankoff; Kingman).
- $\gamma_k = \sup_n \mathbb{E}[L_n]/n$, so any exact finite-$n$ computation is a certified lower bound.
- Alexander's $O(\sqrt{\log n/n})$ convergence rate.
- $\gamma_k$ is strictly decreasing in $k$; $\gamma_1 = 1$ trivially (single-letter alphabet, $L_n = n$).
- Linear variance for asymmetric binary letter distributions (Lember–Matzinger).
- Non-uniform letter distributions: the limit $\gamma$ still exists by the same superadditivity, and depends continuously on the letter law.

**Exact small-$n$ values.** $\mathbb{E}[L_n^{(2)}]$ is computable exactly by summing over all $4^n$ string pairs (or by transfer matrix) for $n$ into the hundreds using the DP-state compression; see Section 10 for $n \le 2$.

## 5. Principal Obstacles

- **No integrable structure.** The longest *increasing* subsequence problem was solved (Vershik–Kerov, Logan–Shepp; Baik–Deift–Johansson) because RSK correspondence maps it to random Young tableaux and a determinantal point process. LCS of two random strings has no known RSK-type bijection, no determinantal or Pfaffian representation, and no exactly solvable last-passage analogue. Every attempt to embed LCS into a solvable model loses the "match only on equal letters" constraint.
- **Superadditivity is one-sided and slow.** Fekete gives lower bounds only, and Alexander's $\sqrt{\log n / n}$ rate means closing a gap of $0.038$ by brute force needs $n$ of order $10^{4}$–$10^{5}$ with exact expectations — combinatorially out of reach, since exact $\mathbb{E}[L_n]$ requires tracking the DP wavefront's full state distribution.
- **Upper bounds are first-moment bounds.** All known upper bounds count alignments: bound $\mathbb{P}(L_n \ge \alpha n)$ by (number of candidate common subsequences) × (probability one is realized). The count overshoots badly because near-optimal alignments are highly correlated. A second-moment or cluster-expansion correction has never been made to work: the correlation structure among overlapping alignments is not summable.
- **Wavefront state space explodes.** Lueker's method encodes the difference vector of a DP row as a state in a finite chain and bounds $\gamma_2$ by the chain's growth rate. Accuracy improves with window width $w$, but the state count grows like $k^{w}\cdot 2^{w}$; the $0.038$ gap is essentially a computational wall, not a conceptual one — yet no argument shows the limit of the hierarchy is $\gamma_2$ at any computable rate.
- **Fluctuation theory is unsettled.** Without knowing whether $\mathrm{Var}(L_n)$ is $\Theta(n)$ or $\Theta(n^{2/3})$, one cannot decide between a Gaussian (mean-field) and a KPZ/Tracy–Widom universality picture, which in turn would dictate which analytic machinery is even appropriate.

## 6. The Gap

Proven: $\gamma_2$ exists and lies in $[0.788071, 0.826280]$; $\gamma_k\sqrt k \to 2$ with a $-\Theta(1/k)$ correction. Wanted: the number $\gamma_2$ itself.

The precise missing step is an **upper bound mechanism that is not a union bound over alignments**. Lower bounds are effectively solved in principle (compute $\mathbb{E}[L_n]/n$ for large $n$); upper bounds require controlling the *entropy of near-optimal alignments*, i.e. showing that the exponentially many alignments achieving $\ge (\gamma+\epsilon)n$ matches are so strongly correlated that their expected count overstates the probability by a factor $e^{\Theta(n)}$. Equivalently: prove a large-deviation rate function $I(\alpha) = \lim -\frac1n \log\mathbb{P}(L_n \ge \alpha n)$ exists and identify its zero. Nothing in the current toolkit produces $I$.

## 7. Current Research (as of June 2026)

- **Refined automaton bounds.** Extensions of Lueker's power-iteration scheme with wider windows and interval arithmetic, aiming to shave the binary gap below $0.03$. Progress is incremental and compute-bound. *(frontier — verify)*
- **Combinatorics of periodic words.** The Bukh school (Bukh, Cox, Zhou) continues the "frogs"/periodic-word technique, which converts LCS upper bounds into questions about common subsequences of highly structured words; the same machinery drives progress on twins in words and LCS of random permutations. Active at Carnegie Mellon.
- **Variance and fluctuation program.** Houdré, Matzinger, Lember and collaborators (Georgia Tech, Tartu) push linear-variance results toward the symmetric uniform case, the sharpest remaining structural target. *(frontier — verify)*
- **Chilean/Czech line.** Kiwi, Soto, Loebl and coauthors on relations between $\gamma_k$ for several sequences and on monotonicity of $\gamma_k\sqrt k$.
- **Algorithmic side.** SETH-based conditional lower bounds for LCS computation (Abboud–Backurs–Williams; Bringmann–Künnemann) explain why no subquadratic exact algorithm is expected, which bounds how far exact finite-$n$ computation can be pushed.

## 8. Future Work

- Prove or disprove $\mathrm{Var}(L_n^{(2)}) = \Theta(n)$ for the uniform binary model — the most tractable named subproblem.
- Establish a large-deviation principle for $L_n/n$ with an identified rate function; this is the recognized route to a genuinely new upper bound.
- Prove monotonicity of $k \mapsto \gamma_k \sqrt k$, which would let large-$k$ asymptotics constrain small $k$.
- Pin the $1/k$ coefficient in $\gamma_k = 2/\sqrt k - c_1/k + o(1/k)$; a clean $c_1$ would be strong evidence for or against any proposed closed form.
- Search for an RSK-like bijection or a solvable deformation (e.g. a $q$-deformed matching model) that degenerates to LCS.
- Determine whether $\gamma_2$ is algebraic, or prove it is not a root of any low-degree polynomial with small integer coefficients.

## 9. Key References

- **[Foundational]** V. Chvátal and D. Sankoff. *Longest common subsequences of two random sequences.* Journal of Applied Probability 12(2), 306–315, 1975.
- **[Foundational]** J. G. Deken. *Some limit results for longest common subsequences.* Discrete Mathematics 26(1), 17–31, 1979.
- **[Foundational]** J. M. Steele. *Long common subsequences and the proximity of two random strings.* SIAM Journal on Applied Mathematics 42(4), 731–737, 1982.
- **[Foundational]** D. Sankoff and S. Mainville. *Common subsequences and monotone subsequences.* In *Time Warps, String Edits, and Macromolecules* (D. Sankoff, J. Kruskal, eds.), Addison-Wesley, 1983.
- **[Key tool]** K. S. Alexander. *The rate of convergence of the mean length of the longest common subsequence.* Annals of Applied Probability 4(4), 1074–1082, 1994.
- **[SOTA]** G. S. Lueker. *Improved bounds on the average length of longest common subsequences.* Journal of the ACM 56(3), Article 17, 2009.
- **[SOTA]** M. Kiwi, M. Loebl, J. Matoušek. *Expected length of the longest common subsequence for large alphabets.* Advances in Mathematics 197(2), 480–498, 2005.
- **[SOTA / Recent]** B. Bukh and C. Cox. *Periodic words, common subsequences and frogs.* Annals of Applied Probability 32(2), 2022.
- **[Variance]** J. Lember and H. Matzinger. *Standard deviation of the longest common subsequence.* Annals of Probability 37(3), 1192–1235, 2009.
- **[Bounds, larger $k$]** R. Baeza-Yates, R. Gavaldá, G. Navarro, R. Scheihing. *Bounding the expected length of longest common subsequences and forests.* Theory of Computing Systems 32(4), 435–452, 1999.
- **[Automaton method]** V. Dančík and M. Paterson. *Upper bounds for the expected length of a longest common subsequence of two binary sequences.* Random Structures & Algorithms 6(4), 449–458, 1995.
- **[Numerics]** J. Boutet de Monvel. *Extensive simulations for longest common subsequences.* European Physical Journal B 7, 293–308, 1999.
- **[Survey]** M. Kiwi and J. Soto. *On a speculated relation between Chvátal–Sankoff constants of several sequences.* Combinatorics, Probability and Computing 18(4), 517–532, 2009.

## 10. Worked Example: exact $\mathbb{E}[L_n^{(2)}]$ for $n = 1, 2$

Take $\Sigma_2 = \{0,1\}$, uniform i.i.d. letters.

**$n=1$.** $L_1 = \mathbf{1}\{X_1 = Y_1\}$, so $\mathbb{E}[L_1] = 1/2$ and the Fekete bound is $\gamma_2 \ge 0.5$.

**$n=2$.** Enumerate all $4 \times 4 = 16$ equally likely pairs from $\{00,01,10,11\}$. The LCS table:

| $x \backslash y$ | 00 | 01 | 10 | 11 |
|---|---|---|---|---|
| **00** | 2 | 1 | 1 | 0 |
| **01** | 1 | 2 | 1 | 1 |
| **10** | 1 | 1 | 2 | 1 |
| **11** | 0 | 1 | 1 | 2 |

Check two entries by the DP of Section 2. For $x=01$, $y=10$: $D_{1,1}=0$ ($0\ne1$), $D_{1,2}=1$ (match $x_1=0$ with $y_2=0$), $D_{2,1}=1$ (match $x_2=1$ with $y_1=1$), $D_{2,2}=\max(D_{1,2},D_{2,1})=1$ since $x_2=1\ne y_2=0$. So $L=1$: the strings share `0` and share `1` but not in a common order. For $x=00$, $y=11$ no letter is shared, $L=0$.

Row sums: $4, 5, 5, 4$, total $18$. Hence
$$\mathbb{E}[L_2] = \frac{18}{16} = 1.125, \qquad \frac{\mathbb{E}[L_2]}{2} = 0.5625 .$$

Since $\gamma_2 = \sup_n \mathbb{E}[L_n]/n$, this certifies $\gamma_2 \ge 0.5625$, already better than $n=1$. The sequence $\mathbb{E}[L_n]/n$ climbs slowly: $0.5,\ 0.5625,\ \ldots$, and Alexander's theorem says it is still $O(\sqrt{\log n/n})$ short of $\gamma_2$ at every finite $n$. Pushing $n$ into the thousands by exact wavefront enumeration — plus Lueker's automaton refinement — is exactly what produces the current record $0.788071$. The upper bound $0.826280$ comes from a different mechanism (counting alignments), which is why the two ends of the interval do not meet, and why the gap of $0.038$ has not moved since 2009.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*