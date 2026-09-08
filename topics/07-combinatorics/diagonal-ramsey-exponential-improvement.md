---
id: 07-combinatorics/diagonal-ramsey-exponential-improvement
title: "Exponential Improvement for Diagonal Ramsey Numbers"
topic: 07-combinatorics
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Exponential Improvement for Diagonal Ramsey Numbers

> **Topic:** Combinatorics & Graph Theory · **ID:** `07-combinatorics/diagonal-ramsey-exponential-improvement` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

The diagonal Ramsey number $R(k)=R(k,k)$ is the least $n$ such that every red/blue colouring of the edges of the complete graph $K_n$ contains a monochromatic $K_k$. The classical bounds are
$$\sqrt{2}^{\,k} \;\lesssim\; R(k) \;\lesssim\; 4^{k},$$
and the central open problem is to determine the **exponential growth constant**
$$c \;=\; \lim_{k\to\infty} R(k)^{1/k},$$
whose existence is itself unproven. Known: $\sqrt2 \le \liminf R(k)^{1/k}$ and $\limsup R(k)^{1/k} \le 4$.

Two concrete targets:

1. **Erdős's $\$100$ problem.** Prove that $\lim R(k)^{1/k}$ exists.
2. **Erdős's $\$250$ problem.** Determine its value, if it exists.

The named "exponential improvement" problem is the demand for constants strictly inside the classical window — an upper bound $R(k)\le (4-\varepsilon)^k$ and a lower bound $R(k)\ge(\sqrt2+\delta)^k$ for fixed $\varepsilon,\delta>0$. The first was achieved in 2023; the second is the subject of very recent work. A complete resolution requires matching exponential constants, i.e. proving $R(k)=c^{k+o(k)}$ with $c$ identified.

## 2. Mathematical Foundations

**Ramsey's theorem (1930).** For all $k$ there is $n$ with $n \to (k)^2_2$: every $2$-colouring $\chi:E(K_n)\to\{\text{red},\text{blue}\}$ admits $S\subseteq V$, $|S|=k$, with $\chi$ constant on $\binom S2$.

**Erdős–Szekeres bound.** From $R(s,t)\le R(s-1,t)+R(s,t-1)$,
$$R(s,t)\le\binom{s+t-2}{s-1},\qquad R(k)\le\binom{2k-2}{k-1}\sim \frac{4^{k}}{4\sqrt{\pi k}}.$$

**Erdős's probabilistic bound.** Colour $E(K_n)$ uniformly at random. The expected number of monochromatic $K_k$ is $\binom nk 2^{1-\binom k2}<1$ when $n\le 2^{k/2}$, so
$$R(k) > (1+o(1))\,\frac{k}{e\sqrt2}\,2^{k/2}.$$
Spencer's Local Lemma refinement gains a factor $2$: $R(k)>(1+o(1))\frac{\sqrt2}{e}k\,2^{k/2}$.

**Book graphs.** $B^{(t)}_s = K_t + \overline{K_s}$: a set $T$ of $t$ vertices forming a clique (the *spine*), each joined to all of an $s$-set (the *pages*). Books are the engine of the modern upper bound: a large red book yields either a red $K_k$ by induction on the spine, or a dense blue-biased page set.

**Book Ramsey.** Conlon (2019) proved a quasirandomness-flavoured bound for book Ramsey numbers, giving $R(k)\le 4^{k-c\,k/\log\log k}$ — subexponential savings only.

**The 2023 theorem (Campos–Griffiths–Morris–Sahasrabudhe).**
$$R(k)\;\le\;(4-\varepsilon)^{k}\quad\text{with } \varepsilon = 2^{-7}.$$
More precisely they prove an off-diagonal book statement: for $\ell\le k$,
$$R(k,\ell)\le e^{-\delta \ell + o(k)}\binom{k+\ell}{\ell},\qquad \delta>0 .$$
The proof runs a **book algorithm** maintaining a pair $(X,Y)$ with red density $p$ between them, cycling through four step types — *degree-regularisation*, *big-blue* (Ramsey-type extraction of a blue book), *red step*, and *density-boost* — and tracks the potential
$$\Phi \;=\; \text{(red spine size)}\cdot\log\tfrac1{p} \;+\; \text{entropy-like corrections},$$
so that each red step is "paid for" and every density boost banks a surplus $\Omega(p)$ that cannot be repaid, forcing termination before the Erdős–Szekeres budget is exhausted.

## 3. History & State of the Art (SOTA)

- **1930.** Ramsey proves the finite theorem in *On a problem of formal logic*.
- **1935.** Erdős and Szekeres give $R(k)\le\binom{2k-2}{k-1}$ (the "Happy Ending" paper).
- **1947.** Erdős's two-page probabilistic proof of $R(k)>2^{k/2}$ — the founding paper of the probabilistic method.
- **1975.** Spencer improves the lower bound constant by a factor $2$ via the Lovász Local Lemma.
- **1977–1988.** Polynomial-factor upper-bound gains: Rödl; Thomason (1988) obtains $R(k)\le k^{-1/2+c/\sqrt{\log k}}\binom{2k}{k}$.
- **2009.** Conlon: the first *superpolynomial* saving, $R(k)\le k^{-c\log k/\log\log k}\binom{2k}{k}$ (*Annals of Mathematics*), using a quasirandomness/book argument.
- **2020.** Sah sharpens Conlon's method to $R(k)\le e^{-c\log^2 k}\binom{2k}{k}$ — the limit of that framework.
- **March 2023.** Campos, Griffiths, Morris and Sahasrabudhe post *An exponential improvement for diagonal Ramsey*: $R(k)\le 3.993^k$. This is the first constant-factor-in-the-exponent gain since 1935.
- **2024.** Gupta, Ndiaye, Norin and Wei optimise the CGMS algorithm's parameters and analysis to $R(k)\le 3.8^{k}$ for large $k$.
- **2025.** Campos, Jenssen, Michelen and Sahasrabudhe announce an exponential improvement on the *lower* bound, $R(k)\ge(\sqrt2+\delta)^k$ *(frontier — verify)*, adapting the "algorithmic/free-energy" techniques they used for their 2023 sphere-packing lower bound.

## 4. Partial Results / Verified Cases

**Exactly known diagonal values.** Only $R(1)=1$, $R(2)=2$, $R(3)=6$ (Greenwood–Gleason 1955), $R(4)=18$ (Greenwood–Gleason 1955). $R(5)$ is unknown: $43\le R(5)\le 46$, the lower bound from Exoo (1989) and the upper from Angeltveit–McKay (2024, improving their own $48$ from 2017). For $R(6)$: $102\le R(6)\le 160$.

**Off-diagonal.** $R(3,t)=\Theta\!\left(t^2/\log t\right)$ is settled: upper bound Ajtai–Komlós–Szemerédi (1980), lower bound Kim (1995), constants pinned to a factor $4$ by Fiz Pontiveros–Griffiths–Morris and Bohman–Keevash (triangle-free process, 2020) giving $R(3,t)=\left(\tfrac14+o(1)\right)t^2/\log t$. $R(4,t)=\Theta(t^3/\log^4 t)$ was resolved by Mattheus and Verstraëte (*Annals*, 2024).

**Exponential regimes where improvement is proven.**
- Upper: $R(k)\le 3.8^k$ for all sufficiently large $k$ (Gupta–Ndiaye–Norin–Wei 2024), unconditional, with explicit though astronomically large threshold.
- Off-diagonal upper: $R(k,\ell)\le e^{-\delta\ell+o(k)}\binom{k+\ell}\ell$ for all $\ell\le k$, so the saving persists across the whole off-diagonal range, degrading gracefully as $\ell/k\to0$.
- Multicolour: Conlon–Ferber (2021) and Wigderson (2021) give exponential improvements to lower bounds for $R(k;r)$ with $r\ge3$ colours, e.g. $R(k;3)\ge 2^{7k/8-o(k)}$ — notably these algebraic constructions do **not** help at $r=2$.

## 5. Principal Obstacles

- **The lower bound is a pure existence statement.** Random colourings give $\sqrt2^{\,k}$ and are conjecturally near-optimal in density but no explicit or semi-explicit construction beats them at $r=2$. The Conlon–Ferber algebraic construction gains only when $r\ge3$ because its $\mathbb F_2$-quadratic-form colouring needs a third colour to absorb the "diagonal" degeneracy.
- **Quasirandomness saturates.** Conlon's and Sah's method extracts savings from *deviation* from quasirandomness; a perfectly quasirandom colouring gives zero saving. Sah's $e^{-c\log^2k}$ is provably the ceiling of that argument, so any exponential gain must exploit structure *within* the quasirandom regime — exactly what the book algorithm's density-boost step does.
- **Bookkeeping fragility.** The CGMS potential must be monotone across four interleaved step types with parameters coupled through $p$, $k$ and $\ell$. Pushing $\varepsilon$ up forces the density-boost surplus and the red-step cost into direct competition; the optimisation is not convex and Gupta et al.'s $3.8$ appears close to the method's ceiling.
- **No structural characterisation of extremal colourings.** Unlike triangle-free or $K_4$-free off-diagonal problems, where the $H$-free process supplies a plausible extremal object, nothing predicts what a near-optimal $K_k$-free-in-both-colours colouring looks like.
- **Computation is hopeless.** Deciding $R(5)$ exactly requires searching colourings of $K_{42}$ up to isomorphism, roughly $2^{861}$ raw colourings; even highly pruned SAT/isomorph-free generation has only reduced the upper bound by $2$ in seven years.

## 6. The Gap

Proven: $(\sqrt2)^{k(1+o(1))} \le R(k) \le 3.8^{k}$ (with the lower constant possibly now $\sqrt2+\delta$). Wanted: a single constant $c$ with $R(k)=c^{k+o(k)}$.

The gap is a factor of about $2.69^k$ — still exponential. The specific missing steps:

1. **Existence of the limit.** No supermultiplicativity or submultiplicativity relation is known for $R(k)^{1/k}$; $R(k+1)\le 4R(k)$ is available but $R(a+b)\ge R(a)R(b)$-type inequalities are not, so even $\lim R(k)^{1/k}$ existing is open.
2. **Which end moves.** Erdős himself was reportedly undecided whether the truth is nearer $\sqrt2$ or $4$; there is no consensus conjecture. Most modern opinion leans toward the lower bound being closer to the truth, which would require driving $\varepsilon$ in $(4-\varepsilon)^k$ from $0.2$ to $2.6$ — a qualitative, not quantitative, leap.
3. **A construction barrier.** Producing any explicit family of colourings of $K_n$, $n=(\sqrt2+\delta)^k$, with no monochromatic $K_k$ would be the first genuinely new source of Ramsey lower bounds at two colours.

## 7. Current Research (as of June 2026)

- **Cambridge / IMPA / Birmingham (Campos, Griffiths, Morris, Sahasrabudhe).** Refinement of the book algorithm; the same team's *(frontier — verify)* 2025 lower-bound preprint claims $R(k)\ge(\sqrt2+\delta)^k$ via a Rödl-nibble-like/algorithmic construction analogous to their sphere-packing result.
- **McGill (Norin, Wei, Gupta, Ndiaye).** Systematic parameter optimisation of CGMS; a stated goal is to determine the exact infimum constant the book-algorithm framework can reach.
- **MIT / Stanford (Sah, Sawhney, Conlon).** Entropy and container methods for Ramsey-type counting; sharp thresholds for Ramsey properties of random graphs.
- **UCSD / Vienna (Verstraëte, Mattheus).** Algebraic-geometric constructions (pseudorandom hypergraph covers, generalized quadrangles) for off-diagonal $R(s,t)$, $s\ge5$, with the hope of eventually reaching the diagonal.
- **Computational (McKay, Angeltveit, Exoo, Radziszowski).** Incremental exact bounds; Radziszowski's *Small Ramsey Numbers* dynamic survey (revision \#18, 2024) is the reference ledger.

## 8. Future Work

- Push the CGMS analysis to its true optimum and prove a *lower bound on the method*: show no book algorithm of this form can beat some $c_0^k$, thereby forcing a new idea.
- Develop pseudorandom algebraic constructions at two colours; understand precisely why the Conlon–Ferber quadratic-form colouring degenerates at $r=2$ and whether a twisted or higher-degree variant repairs it.
- Prove existence of $\lim R(k)^{1/k}$ by finding an approximate supermultiplicativity via product/blow-up colourings.
- Transfer the density-boost idea to hypergraph Ramsey numbers, where the tower-height question $r_3(k)$ (Erdős–Hajnal–Rado) has an analogous exponential gap.
- Determine $R(5)$; even $R(5)\le 45$ would be a meaningful test of new SAT-based isomorph-free generation.

## 9. Key References

- **[Foundational]** F. P. Ramsey. *On a Problem of Formal Logic.* Proceedings of the London Mathematical Society, 30:264–286, 1930.
- **[Foundational]** P. Erdős and G. Szekeres. *A combinatorial problem in geometry.* Compositio Mathematica, 2:463–470, 1935.
- **[Foundational]** P. Erdős. *Some remarks on the theory of graphs.* Bulletin of the American Mathematical Society, 53:292–294, 1947.
- **[Foundational]** R. E. Greenwood and A. M. Gleason. *Combinatorial relations and chromatic graphs.* Canadian Journal of Mathematics, 7:1–7, 1955.
- **[Classical]** J. Spencer. *Ramsey's theorem — a new lower bound.* Journal of Combinatorial Theory, Series A, 18:108–115, 1975.
- **[Classical]** A. Thomason. *An upper bound for some Ramsey numbers.* Journal of Graph Theory, 12:509–517, 1988.
- **[Milestone]** D. Conlon. *A new upper bound for diagonal Ramsey numbers.* Annals of Mathematics, 170(2):941–960, 2009.
- **[SOTA]** M. Campos, S. Griffiths, R. Morris and J. Sahasrabudhe. *An exponential improvement for diagonal Ramsey.* arXiv:2303.09521, 2023.
- **[SOTA]** P. Gupta, N. Ndiaye, S. Norin and L. Wei. *Optimizing the CGMS upper bound on Ramsey numbers.* arXiv:2407.19026, 2024.
- **[SOTA]** S. Mattheus and J. Verstraëte. *The asymptotics of $r(4,t)$.* Annals of Mathematics, 199(2):919–941, 2024.
- **[Related]** D. Conlon and A. Ferber. *Lower bounds for multicolor Ramsey numbers.* Advances in Mathematics, 378:107528, 2021.
- **[Related]** V. Angeltveit and B. D. McKay. *$R(5,5)\le 46$.* Journal of Graph Theory, 2024.
- **[Survey]** S. Radziszowski. *Small Ramsey Numbers.* Electronic Journal of Combinatorics, Dynamic Survey DS1, revision \#18, 2024.
- **[Book]** R. Graham, B. Rothschild and J. Spencer. *Ramsey Theory*, 2nd ed. Wiley, 1990.
- **[Book]** N. Alon and J. Spencer. *The Probabilistic Method*, 4th ed. Wiley, 2016.

## 10. Worked Example / Concrete Special Case

**Both classical bounds at $k=4$, then the shape of the saving.**

*Upper bound.* Erdős–Szekeres gives $R(4)\le\binom{6}{3}=20$. The refinement "if $R(s-1,t)$ and $R(s,t-1)$ are both even then the sum may be decreased by $1$" applies since $R(3,4)=9$ is odd — but the standard argument uses $R(4,4)\le R(3,4)+R(4,3)=18$. So $R(4)\le18$.

*Lower bound.* The Paley graph on $\mathbb F_{17}$: vertices $\mathbb Z_{17}$, edge $\{i,j\}$ red iff $i-j$ is a quadratic residue, i.e. $i-j\in\{\pm1,\pm2,\pm4,\pm8\}$. This graph is self-complementary and $K_4$-free in both colours, certifying $R(4)\ge18$. Hence $R(4)=18$.

*Erdős's counting bound at $k=4$.* $\binom n4 2^{1-\binom42}=\binom n4 2^{-5}<1$ needs $\binom n4<32$, i.e. $n\le 6$. So the probabilistic method alone yields only $R(4)\ge7$ — far below $18$. This is the small-$k$ shadow of the exponential gap: random colourings are lossy, structured ones are better, and no one knows how much better asymptotically.

*Where the CGMS saving lives.* The Erdős–Szekeres recursion charges the full "cost" of each red step by shrinking the target from $(k,\ell)$ to $(k,\ell-1)$ at the price of halving nothing. CGMS instead maintain a set pair $(X,Y)$ with red density $p\approx \ell/(k+\ell)$. When the colouring on $(X,Y)$ is quasirandom, a red step costs exactly the $\binom{k+\ell}{\ell}$ budget — no gain. When it is not, a density-boost step raises $p\mapsto p+\Omega(p^2)$ while consuming *no* clique budget. Since $p\le1$, only $O(1/p)$ boosts can occur before $p$ would exceed $1$; each banked boost is worth a factor $e^{\Omega(1)}$ against the budget, and summing over the $\Theta(\ell)$ rounds yields the $e^{-\delta\ell}$ factor. Setting $\ell=k$ and unwinding the constant $\delta$ gives $4e^{-\delta}\le3.993$ in the original paper and $\le3.8$ after Gupta–Ndiaye–Norin–Wei's re-optimisation.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*