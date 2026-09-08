---
id: 10-theoretical-cs/formula-size-lower-bound-cubic-barrier
title: "Sunflower-Based Formula Size Lower Bounds for Andreev's Function"
topic: 10-theoretical-cs
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Sunflower-Based Formula Size Lower Bounds for Andreev's Function

> **Topic:** Theoretical Computer Science · **ID:** `10-theoretical-cs/formula-size-lower-bound-cubic-barrier` · **Status:** open

## 1. Problem Statement / Conjecture

De Morgan formula size $L(f)$ — the number of leaves in the smallest binary tree over $\{\wedge,\vee\}$ with literal leaves computing $f$ — is stuck at cubic. The record explicit lower bound is $L(A_n) \ge n^3 / (\log n)^{2+o(1)}$ for Andreev's function $A_n$ (Tal 2014), and no explicit function is known with $L(f) = \omega(n^3)$.

**The problem.** Every cubic bound to date routes through *shrinkage under random restrictions*, whose exponent is provably exactly $2$, capping the method at $n^{2+1} = n^3$. The question is whether **sunflower-type structural extraction** — Erdős–Rado sunflowers, robust/quasi-sunflowers, and the post-Alweiss–Lovett–Wu–Zhang bounds — can replace or augment restriction-based shrinkage and break the cubic barrier.

Two concrete targets:

- **(A) Sunflower shrinkage.** Show that any De Morgan formula $F$ of size $L$ computing $A_n$ has a minterm system containing a robust sunflower with $\text{poly}(\log L)$ petals, and that plucking such a sunflower yields an amortized size reduction strictly better than the restriction bound $\mathbb{E}[L(F|_R)] = O(p^2 L)$ — giving effective exponent $\Gamma > 2$ *for formulas computing $A_n$* (not for all formulas, where $\Gamma = 2$ is tight).
- **(B) Superpolynomial consequence.** Derive $L(A_n) \ge n^{3+\varepsilon}$ for some fixed $\varepsilon > 0$, or refute (A) by exhibiting an $A_n$-computing formula family whose minterm hypergraph is sunflower-free at all relevant petal counts.

A complete resolution is either an unconditional bound $\omega(n^3)$ for an explicit function, or a formal barrier showing sunflower extraction cannot beat $\Gamma = 2$.

## 2. Mathematical Foundations

**Formulas.** $L(f)$ = leaf count of a minimum De Morgan formula. Depth $D(f) = \Theta(\log L(f))$ up to constants (Spira). $\mathbf{NC^1} \ne \mathbf{P}$ would follow from $L(f) = n^{\omega(1)}$ for an explicit $f$.

**Andreev's function.** Let $n$ be even, $k = \log_2(n/2)$, $b = (n/2)/k$. Split the input into $y \in \{0,1\}^{n/2} = \{0,1\}^{2^k}$ (the truth table of $f_y : \{0,1\}^k \to \{0,1\}$) and $x = (x^{(1)},\dots,x^{(k)})$ with $x^{(i)} \in \{0,1\}^{b}$. Then
$$A_n(y,x) \;=\; f_y\!\left(\bigoplus_{j} x^{(1)}_j,\ \bigoplus_j x^{(2)}_j,\ \dots,\ \bigoplus_j x^{(k)}_j\right).$$
Upper bound: $L(A_n) = O(n^3/\log^2 n)$ via Lupanov-style formulas for $f_y$ composed with parities.

**Random restrictions.** $R_p$ keeps each variable free with probability $p$ and sets it to $0/1$ uniformly otherwise. The *shrinkage exponent* is
$$\Gamma \;=\; \sup\Big\{\gamma : \mathbb{E}_{R_p}\big[L(f|_{R_p})\big] = O\big(p^{\gamma} L(f)\big) + O(1) \ \ \forall f\Big\}.$$
Subbotovskaya (1961): $\Gamma \ge 3/2$. Håstad (1998): $\Gamma = 2$, with $\mathbb{E}[L(f|_{R_p})] = O(p^2 L + p\sqrt{L})$ after Tal's (2014) removal of the $o(1)$ loss. The value $2$ is tight (witnessed by parity: $L(\oplus_n) = n^2$, $L(\oplus_n|_{R_p}) \approx (pn)^2$).

**The Andreev argument.** Restrict with $p = \Theta(k/n)$; whp each block $x^{(i)}$ retains a live variable, so the parities remain surjective onto $\{0,1\}^k$; choose $y$ to be the truth table of the hardest $k$-bit function, which needs $L \ge 2^k/\log k = \Omega(n/\log n \cdot 1/\log\log n)$ leaves (Shannon/Lupanov counting). Then
$$L(A_n) \;\ge\; \Omega\!\left(p^{-2}\cdot \frac{2^k}{\log k}\right) \;=\; \frac{n^3}{(\log n)^{2+o(1)}}.$$

**Sunflowers.** A family $\mathcal{S} = \{S_1,\dots,S_r\}$ of sets is a *sunflower with $r$ petals and core $Y$* if $S_i \cap S_j = Y$ for all $i \ne j$. Erdős–Rado: any family of more than $r!\,(r-1)^{w}$ sets of size $\le w$ contains one. Alweiss–Lovett–Wu–Zhang (2021): $(\log r)^{w(1+o(1))} \cdot r^{O(1)}$ suffices; Rao and Bell–Chueluecha–Warnke give clean variants. A family $\mathcal{S}$ of $w$-sets is a *robust ($\kappa$-satisfying) sunflower with core $Y$* if for a $p$-random set $W$, $\Pr[\exists S \in \mathcal{S}: S \setminus Y \subseteq W] \ge 1-\kappa$. Robust sunflowers are exactly the object driving Rossman's monotone $k$-clique lower bounds and DNF-compression arguments.

**Bridge to formulas.** For a formula $F$ of size $L$, let $\mathcal{M}(F)$ be its minterm system. Sunflower extraction on $\mathcal{M}(F)$ produces a core $Y$; conditioning on $Y$ acts like a *correlated* restriction that kills $\ge \Omega(r)$ leaves per unit of entropy spent — the hoped-for improvement over the $\Gamma=2$ i.i.d. restriction accounting.

## 3. History & State of the Art (SOTA)

- **1961** Subbotovskaya introduces random restrictions and proves $L(\oplus_n) = \Omega(n^{3/2})$, exponent $3/2$.
- **1966** Nechiporuk: $\Omega(n^2/\log n)$ over the *full* binary basis — still the record there.
- **1971** Khrapchenko: $L(\oplus_n) \ge n^2$, tight for De Morgan.
- **1987** Andreev defines $A_n$ and obtains $n^{2.5-o(1)}$.
- **1993–94** Impagliazzo–Nisan ($\Gamma \ge 1.55$), Paterson–Zwick ($\Gamma \ge 1.63$).
- **1998** Håstad: $\Gamma = 2$, hence $L(A_n) \ge n^{3-o(1)}$.
- **2013** Komargodski–Raz–Tal: average-case $n^{3-o(1)}$ — no size-$n^{3-o(1)}$ formula computes $A_n$ on more than $1/2 + 2^{-n^{\Omega(1)}}$ of inputs.
- **2014** Tal: $n^3/(\log n)^{2+o(1)}$, tight up to $(\log\log n)^{O(1)}$ against the $O(n^3/\log^2 n)$ upper bound. **This is the SOTA.**
- **2016–18** Dinur–Meir reprove cubic bounds via KRW-style communication complexity — a genuinely restriction-free route, but it also halts at $n^3$.
- **2020–21** Alweiss–Lovett–Wu–Zhang / Rao / Bell–Chueluecha–Warnke revolutionize sunflower bounds, prompting the present question.
- **2021** Filmus–Meir–Tal: shrinkage under *random projections* gives $n^{3-o(1)}$ formula lower bounds for a function in $\mathbf{AC^0}$.

## 4. Partial Results / Verified Cases

- **Cubic is achieved, not exceeded.** $n^3/(\log n)^{2+o(1)}$ for $A_n$ (Tal 2014); $n^{3-o(1)}$ average-case (KRT 2013); $n^{3-o(1)}$ for an $\mathbf{AC^0}$ function (Filmus–Meir–Tal 2021).
- **Restricted formula classes.** For *read-once* formulas, exponential separations and exact size characterizations are known. For *regular* formulas (balanced fan-in structure), Rossman (2019) proves criticality bounds $\lambda = O(\log L)^{d-1}$-type statements that are strictly stronger than generic shrinkage — a proof-of-concept that structure beats $\Gamma = 2$ for a subclass.
- **Monotone setting, sunflowers succeed.** Razborov's approximation method plus Erdős–Rado gives $n^{\Omega(k)}$ monotone circuit bounds for $k$-clique; Rossman's robust-sunflower refinement gives $n^{\Omega(k)}$ on random graphs for $k \le n^{o(1)}$. So sunflower extraction *does* break polynomial barriers — in the monotone world.
- **Depth-$d$ small $d$.** For $d = 2$ (DNF/CNF) and $d = 3$, sunflower-based DNF compression (Lovett–Solomon–Zhang 2019) yields near-optimal quantitative statements.
- **Full basis.** No improvement on $n^2/\log n$ since 1966; the Nechiporuk method provably cannot exceed $n^2/\log n$.

## 5. Principal Obstacles

- **$\Gamma = 2$ is a theorem, not a limitation of analysis.** Parity witnesses tightness. Any restriction-based argument that treats the formula as a black box is capped at $p^{-2} \cdot (\text{hardness of the inner function})$, and the inner function on $k = \log n$ bits has complexity at most $O(n/\log n)$. The product is $n^3$ by arithmetic, not by weakness of technique.
- **Sunflowers need a set system; formulas are not monotone.** Minterms of a De Morgan formula involve negated literals and are not upward-closed, so the cancellation that makes Razborov's approximator error small has no analogue. Extracting a sunflower from $\mathcal{M}(F)$ yields a core, but no guarantee that fixing the core simplifies $F$ — the petals may be spread across $\Omega(L)$ distinct subformulas.
- **Width blowup.** Sunflower lemmas require bounded set size $w$; minterms of an $n^3$-size formula can have width $\Theta(n)$, where even AWLZ needs $(\log r)^{\Theta(n)}$ sets — more than the $\binom{2n}{n}$ available. Reducing width demands a restriction, which reintroduces $\Gamma = 2$.
- **Correlated restrictions lose independence.** Sunflower-conditioning is precisely a *correlated* restriction; the martingale/entropy accounting behind Håstad's proof (and Tal's spectral proof) uses independence across coordinates and does not survive.
- **Natural proofs.** Any argument that is constructive and large on random functions runs into Razborov–Rudich; sunflower arguments are typically both.

## 6. The Gap

Proven: $n^3/(\log n)^{2+o(1)}$, via $\Gamma = 2$ plus $\Omega(2^k/k)$ hardness of a random $k$-bit function. Wanted: $n^{3+\varepsilon}$.

The exact missing step is an **amortized shrinkage inequality conditioned on structure**: a statement of the form
$$\mathbb{E}_{Y \sim \text{sunflower core}}\big[L(F|_Y)\big] \;\le\; O\!\big(p^{2+\varepsilon} L(F)\big) \quad \text{for every } F \text{ computing } A_n,$$
where $p$ measures the fraction of variables left free. Because $\Gamma = 2$ is tight in general, such an inequality must *use* a property of $A_n$-computing formulas — e.g. that the top-level structure must implement a $2^k$-way selector, forcing many disjoint minterm families and hence a large sunflower. No one has shown that selector structure forces sunflower structure. That implication is the gap.

## 7. Current Research (as of June 2026)

- **KRW program.** Composition-based depth lower bounds (Karchmer–Raz–Wigderson 1995) remain the main non-restriction route: Gavinsky–Meir–Weinstein–Wigderson (universal relation composition), Dinur–Meir, Mihajlin–Smal's XOR-KRW conjecture (CCC 2021), and lifting-based approaches from the Simons/KTH/Toronto proof-complexity community.
- **Criticality and projections.** Rossman's criticality framework and Filmus–Meir–Tal's random projections are the two live candidates for going past i.i.d. restrictions; projections already reach cubic for $\mathbf{AC^0}$ and are conjectured to extend. *(frontier — verify)*
- **Post-AWLZ sunflower toolkit.** Groups at UCSD (Lovett), Washington (Rao), Georgia Tech/Warwick (Warnke) continue sharpening robust-sunflower thresholds; applications so far are to DNF compression, $\mathbf{AC^0}$-Frege, and monotone complexity rather than De Morgan formulas.
- **Hardness magnification.** Results of Oliveira–Pich–Santhanam suggest weak formula bounds for sparse problems (MCSP variants) would already imply major separations, redirecting effort away from raw $n^3$ improvements. *(frontier — verify)*
- No preprint as of mid-2026 claims $\omega(n^3)$ for an explicit function. *(frontier — verify)*

## 8. Future Work

1. **Prove a structure theorem for selector formulas:** any $F$ computing $A_n$ contains $\Omega(2^k)$ pairwise-far minterm families, then apply AWLZ to extract a $\text{poly}(k)$-petal robust sunflower.
2. **Bound width first, sunflower second.** Use a $p$-restriction only to push minterm width to $O(\log L)$ (a regime where AWLZ is efficient), then charge the remaining reduction to sunflower plucking; a rigorous version would compose to an exponent $2 + \varepsilon$.
3. **Non-monotone robust sunflowers.** Define a sunflower notion for signed (literal) set systems with a matching extraction lemma. Open even to state cleanly.
4. **Nechiporuk over the full basis.** Any bound beating $n^2/\log n$ there would be a bigger conceptual event than beating $n^3$ over De Morgan.
5. **Barrier formalization.** Show any "sunflower-plucking" proof system yields at most $n^{3+o(1)}$, i.e. an analogue of the $\Gamma=2$ tightness theorem for the sunflower method.

## 9. Key References

- **[Foundational]** A. E. Andreev. *On a method for obtaining more than quadratic effective lower bounds for the complexity of $\pi$-schemes.* Moscow University Mathematics Bulletin, 42(1):63–66, 1987.
- **[Foundational]** B. A. Subbotovskaya. *Realization of linear functions by formulas using $\vee$, $\&$, $^-$.* Soviet Mathematics Doklady, 2:110–112, 1961.
- **[Foundational]** V. M. Khrapchenko. *A method of determining lower bounds for the complexity of $\Pi$-schemes.* Mathematical Notes of the Academy of Sciences of the USSR, 10:474–479, 1971.
- **[Foundational]** È. I. Nechiporuk. *On a Boolean function.* Soviet Mathematics Doklady, 7:999–1000, 1966.
- **[Foundational]** P. Erdős and R. Rado. *Intersection theorems for systems of sets.* Journal of the London Mathematical Society, 35:85–90, 1960.
- **[Foundational]** J. Håstad. *The shrinkage exponent of De Morgan formulas is 2.* SIAM Journal on Computing, 27(1):48–64, 1998.
- **[SOTA / Recent]** A. Tal. *Shrinkage of De Morgan formulae by spectral techniques.* FOCS 2014, pp. 551–560.
- **[SOTA / Recent]** I. Komargodski, R. Raz, A. Tal. *Improved average-case lower bounds for De Morgan formula size.* FOCS 2013; SIAM Journal on Computing, 46(1):37–57, 2017.
- **[SOTA / Recent]** R. Alweiss, S. Lovett, K. Wu, J. Zhang. *Improved bounds for the sunflower lemma.* STOC 2020; Annals of Mathematics, 194(3):795–815, 2021.
- **[SOTA / Recent]** A. Rao. *Coding for sunflowers.* Discrete Analysis, 2020:2.
- **[SOTA / Recent]** B. Rossman. *The monotone complexity of $k$-clique on random graphs.* SIAM Journal on Computing, 43(1):256–279, 2014.
- **[SOTA / Recent]** B. Rossman. *Criticality of regular formulas.* CCC 2019, LIPIcs vol. 137.
- **[SOTA / Recent]** I. Dinur, O. Meir. *Toward the KRW conjecture: cubic lower bounds via communication complexity.* CCC 2016; Computational Complexity, 27(3):375–462, 2018.
- **[SOTA / Recent]** Y. Filmus, O. Meir, A. Tal. *Shrinkage under random projections, and cubic formula lower bounds for $\mathbf{AC^0}$.* ITCS 2021, LIPIcs vol. 185.
- **[SOTA / Recent]** S. Lovett, N. Solomon, J. Zhang. *From DNF compression to sunflower theorems via regularity.* CCC 2019, LIPIcs vol. 137.
- **[SOTA / Recent]** I. Mihajlin, A. Smal. *Toward better depth lower bounds: the XOR-KRW conjecture.* CCC 2021, LIPIcs vol. 200.
- **[Survey]** S. Jukna. *Boolean Function Complexity: Advances and Frontiers.* Springer, Algorithms and Combinatorics vol. 27, 2012.
- **[Survey]** M. Karchmer, R. Raz, A. Wigderson. *Super-logarithmic depth lower bounds via the direct sum in communication complexity.* Computational Complexity, 5(3/4):191–204, 1995.

## 10. Worked Example / Concrete Special Case

**Andreev's function at $n = 8$.** Here $n/2 = 4$, $k = \log_2 4 = 2$, block size $b = 2$. Input $y = y_0y_1y_2y_3$ (truth table of $f_y : \{0,1\}^2 \to \{0,1\}$) and $x = (x_1x_2, x_3x_4)$:
$$A_8(y,x) = y_{\,2(x_1 \oplus x_2) + (x_3 \oplus x_4)}.$$
Take $y = 0110$ (so $f_y = \mathrm{XOR}$) and $x = 1011$. Then $x_1 \oplus x_2 = 1$, $x_3 \oplus x_4 = 1$, index $= 2\cdot 1 + 1 = 3$, output $y_3 = 0$. Consistent with $\mathrm{XOR}(1,1) = 0$. ✓

**Why the argument gives $p^{-2}$ and no more.** Restrict with $p = k/(n/2) = 1/2$ here, keeping $y$ free. Whp each of the two blocks keeps one live variable, say $x_2$ and $x_3$ with $x_1 = 0, x_4 = 1$. The restricted function is $A_8|_R(y, x_2, x_3) = y_{2x_2 + \bar{x}_3}$ — a 4-to-1 multiplexer on the free $y$'s. Choosing $y$ adversarially, the hardest $2$-bit function needs $L \ge 3$ leaves (e.g. $\mathrm{XOR}$ on two variables: $(u \vee v)\wedge(\bar u \vee \bar v)$, 4 leaves; parity of 2 bits has $L = 4 = 2^2$ by Khrapchenko). Shrinkage then gives
$$L(A_8) \;\ge\; \Omega\!\left(p^{-2}\cdot 4\right) = \Omega(16),$$
the toy analogue of $n^3/\log^{2}n$.

**Where a sunflower would enter.** The minterms of the selector part are $\{y_i\} \cup T_i$ where $T_i$ is the length-$k$ literal pattern selecting index $i$: for $i=3$, $T_3 = \{x_2, x_3\}$ (in the restricted picture). Across all $2^k$ indices these sets are pairwise intersecting only in $x$-literals and are *disjoint* in the $y$-coordinate — the canonical shape of a sunflower with empty core and $2^k$ petals. **Target (A)** asks: does every formula computing $A_n$ — not merely the canonical one — have to expose $2^{\Omega(k)}$ such petals, and does plucking them cost the formula $\omega(p^2 L)$ leaves? At $n = 8$ the counts are too small to distinguish $p^{-2}$ from $p^{-2-\varepsilon}$; the phenomenon, if it exists, is asymptotic in $k = \log n$, which is exactly why brute-force verification at small $n$ has produced no evidence either way.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*