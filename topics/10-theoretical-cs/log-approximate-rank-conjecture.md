---
id: 10-theoretical-cs/log-approximate-rank-conjecture
title: "Log-Approximate-Rank Conjecture"
topic: 10-theoretical-cs
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Log-Approximate-Rank Conjecture

> **Topic:** Theoretical Computer Science · **ID:** `10-theoretical-cs/log-approximate-rank-conjecture` · **Status:** open

**Status note.** The conjecture *as originally stated* is **false**: Chattopadhyay, Mande and Sherif (STOC 2019 / JACM 2020) exhibited a total function with $O(\log n)$ log-approximate-rank and $n^{\Omega(1)}$ randomized communication complexity. The `open` tag tracks the surviving program described in §6–§8: the exact log-rank conjecture, the correct upper bound on $R(f)$ in terms of $\mathrm{rank}_\varepsilon$, and the restricted classes on which a polynomial relation still plausibly holds.

## 1. Problem Statement / Conjecture

Let $f:\mathcal{X}\times\mathcal{Y}\to\{0,1\}$ with $\mathcal{X}=\mathcal{Y}=\{0,1\}^n$, and let $M_f$ be its $2^n\times 2^n$ communication matrix. For $\varepsilon\in(0,1/2)$ define the **$\varepsilon$-approximate rank**
$$\mathrm{rank}_\varepsilon(M_f)\;=\;\min\{\,\mathrm{rank}(A)\;:\;A\in\mathbb{R}^{\mathcal{X}\times\mathcal{Y}},\ \|A-M_f\|_\infty\le\varepsilon\,\}.$$

**Log-Approximate-Rank Conjecture (LARC).** There is a constant $c$ such that for every total $f$,
$$R(f)\;=\;O\!\big((\log \mathrm{rank}_{1/3}(M_f))^{c}\big),$$
where $R(f)$ is bounded-error randomized (public-coin) two-party communication complexity.

The inequality in the other direction is elementary: a $c$-bit randomized protocol yields an approximating matrix of rank $\le 2^c$, so $\log\mathrm{rank}_{1/3}(M_f)\le O(R(f))$. LARC therefore asserts that approximate rank is a *polynomially tight* lower bound — the randomized analogue of the Lovász–Saks log-rank conjecture. A disproof requires a total $f$ (partial functions admit easy counterexamples, e.g. Gap-Hamming-type promises) with $\log\mathrm{rank}_{1/3}(M_f)=\mathrm{polylog}(n)$ and $R(f)=n^{\Omega(1)}$.

Two companion statements: the **quantum LARC** ($Q(f)=\mathrm{polylog}\,\mathrm{rank}_{1/3}$), and the **log-approximate-nonnegative-rank conjecture** ($R(f)=\mathrm{polylog}\,\mathrm{rank}^+_{1/3}$, where the approximant is required entrywise nonnegative).

## 2. Mathematical Foundations

**Protocols and measures.** $D(f)$ = deterministic complexity; $R_\varepsilon(f)$ = worst-case cost of a public-coin protocol erring with probability $\le\varepsilon$ on every input; $R(f)=R_{1/3}(f)$; $Q(f)$, $Q^*(f)$ = quantum complexity without / with shared entanglement. Rectangle bound: $\mathrm{rank}(M_f)\le 2^{D(f)}$.

**Approximate rank as a lower bound.** Buhrman and de Wolf proved $Q(f)\ge \tfrac12\log \mathrm{rank}_\varepsilon(M_f)-O(1)$ for constant $\varepsilon$, via the "approximate degree of the acceptance polynomial" argument of Beals–Buhrman–Cleve–Mosca–de Wolf. Since $Q(f)\le R(f)$, approximate rank lower-bounds both models. Equivalent formulations: $\log\mathrm{rank}_\varepsilon$ is, up to constants, the logarithm of the $\gamma_2$-norm's rank-relaxation studied by Linial–Shraibman, and it dominates the discrepancy and margin bounds.

**XOR functions.** For $f:\{0,1\}^n\to\{0,1\}$ set $F(x,y)=f(x\oplus y)$. With the Fourier expansion $f(z)=\sum_{S\subseteq[n]}\hat f(S)\chi_S(z)$, $\chi_S(z)=(-1)^{\sum_{i\in S}z_i}$, one has the spectral decomposition
$$M_F \;=\; \sum_{S\subseteq[n]} \hat f(S)\, v_S v_S^{\!\top},\qquad v_S(x)=\chi_S(x),$$
so $\mathrm{rank}(M_F)=\|\hat f\|_0$ (Fourier sparsity) and
$$\mathrm{rank}_\varepsilon(M_F)\;\le\;\mathrm{sparsity}_\varepsilon(f):=\min\{\|\hat g\|_0 : \|g-f\|_\infty\le\varepsilon\}.$$

**Grolmusz sparsification.** Sampling $T$ characters i.i.d. from the distribution $|\hat f(S)|/\|\hat f\|_1$ and averaging gives, for $T=O(\|\hat f\|_1^2\log(1/\delta)/\varepsilon^2)$, a sparse $\varepsilon$-approximant. Hence
$$\log \mathrm{rank}_{\varepsilon}(M_F)\;=\;O\!\big(\log(\|\hat f\|_1/\varepsilon)\big).$$
So any Boolean $f$ with **polynomially bounded spectral norm** $\|\hat f\|_1=\mathrm{poly}(n)$ automatically has $\log\mathrm{rank}_{1/3}(M_F)=O(\log n)$. LARC restricted to XOR functions therefore predicts: small spectral norm $\Rightarrow$ efficient randomized protocol.

**The SINK function.** Let $m$ be a parameter and $n=\binom{m}{2}$. Read $z\in\{0,1\}^n$ as an orientation of the edges of $K_m$ (a tournament). Define
$$\mathrm{SINK}_m(z)=1 \iff \exists\, i\in[m]\ \text{with every incident edge oriented into } i .$$
The $m$ events are pairwise disjoint (two sinks would conflict on the edge between them), so $\mathrm{SINK}_m$ is a **sum of $m$ disjoint conjunctions**, each on $m-1$ literals. Each conjunction has spectral norm exactly $1$, giving $\|\widehat{\mathrm{SINK}_m}\|_1\le m=O(\sqrt{n})$.

## 3. History & State of the Art (SOTA)

- **1988.** Lovász and Saks pose the log-rank conjecture: $D(f)=\mathrm{polylog}(\mathrm{rank}(M_f))$.
- **1995–2007.** Approximate rank and the related $\gamma_2$/factorization norms enter communication complexity through Buhrman–de Wolf (2001) and Linial–Shraibman (2009); approximate rank becomes the standard "algebraic" lower bound for quantum communication.
- **2009.** Lee and Shraibman, in their survey *Lower bounds in communication complexity*, formulate the log-approximate-rank conjecture as the natural randomized/quantum analogue. It is repeated as a central open problem for a decade, in part because approximate rank subsumes discrepancy, margin and the smooth rectangle bounds.
- **2014–2016.** Lovett proves $D(f)=O(\sqrt{\mathrm{rank}(M_f)}\log \mathrm{rank}(M_f))$; Gavinsky–Lovett give equivalent formulations. Göös–Pitassi–Watson (FOCS 2015) show $D(f)=\tilde\Omega(\log^2 \mathrm{rank})$ is possible, the best known separation for the exact conjecture.
- **2019 — refutation.** Chattopadhyay, Mande and Sherif prove that $F=\mathrm{SINK}_m\circ\mathrm{XOR}$ on $2n$ variables has spectral norm $O(\sqrt n)$, $\mathrm{rank}_{1/3}(M_F)=O(n^2)$, approximate nonnegative rank $O(n^{2.5})$, and $R(F)=\Omega(\sqrt n)$. Because $\log\mathrm{rank}_{1/3}=O(\log n)$, this is an **exponential** refutation of LARC, and simultaneously of the log-approximate-nonnegative-rank conjecture.
- **2019 — quantum.** Sinha and de Wolf (FOCS 2019) and, independently, Anshu, Boddu and Touchette (FOCS 2019) show $Q(F)=\Omega(n^{1/4})$ — the latter even for $Q^*$ with unlimited shared entanglement — refuting the quantum LARC.
- **Since 2020.** Work has shifted to (i) upper bounds of the form $R(f)\le \mathrm{poly}(\mathrm{rank}_\varepsilon)^{1/2}$, (ii) sharper separations, and (iii) whether the *exact* log-rank conjecture survives.

## 4. Partial Results / Verified Cases

- **Low-rank regime.** $\mathrm{rank}_{1/3}(M_f)\le \mathrm{const}$ forces $R(f)=O(1)$; more generally $R(f)=O(\mathrm{rank}_\varepsilon(M_f))$ trivially, and $R(f)=\tilde O(\sqrt{\mathrm{rank}_\varepsilon})$ by the approximate-rank analogue of Lovett's argument (Gál–Syed). So LARC holds up to a *square-root*, not polylogarithmic, loss — and the CMS example shows the square-root form is close to necessary.
- **Small spectral norm, structured $f$.** If $\|\hat f\|_1 = O(1)$ then $F=f\circ\mathrm{XOR}$ has $D(F)=O(1)$; if $f$ has Fourier sparsity $s$ then $D(F)=O(\sqrt{s}\,\mathrm{polylog}\,s)$ (Tsang–Wong–Xie–Zhang and successors), so log-rank holds up to polynomial loss for XOR functions of low sparsity.
- **Symmetric functions.** For $f$ symmetric, $R(f\circ\mathrm{XOR})$ is determined up to constants by the "jump" parameter $r(f)$ (Zhang–Shi); LARC-type polynomial equivalence holds in this class.
- **Small-alphabet / low-degree classes.** For $f$ computed by an $\mathrm{AC}^0$ circuit of constant depth composed with XOR, or for $f$ with $\deg_2(f)=O(1)$ over $\mathbb{F}_2$, log-rank and its approximate variant hold with explicit polynomial exponents.
- **Parameter range of the counterexample.** The refutation is effective for all $m\ge m_0$ with $n=\binom m2$: $\log\mathrm{rank}_{1/3}=\Theta(\log n)$ versus $R=\Theta(\sqrt n)$ (upper bound $O(\sqrt n\log n)$ by having Alice and Bob exchange candidate sink vertices).

## 5. Principal Obstacles

- **Approximate rank is spectrally blind.** Grolmusz sparsification collapses any $\mathrm{poly}(n)$ spectral norm to $\mathrm{polylog}$ log-approximate-rank, but the *protocol* it suggests — sample a character, evaluate $\chi_S(x)\chi_S(y)$ — is a *nondeterministic/one-sided* object. There is no known way to convert a low-rank approximant into a protocol without paying $\sqrt{\mathrm{rank}}$: the rank-based rectangle-finding arguments (Nisan–Wigderson, Lovett) produce a large *almost-monochromatic* rectangle only after a $\sqrt{\mathrm{rank}}$-sized search.
- **Approximation destroys the combinatorial handle.** For exact rank one can use the rank of submatrices, discrepancy of subrectangles, and the fact that rank drops by at least one on a proper restriction. Under $\|\cdot\|_\infty$ perturbation, none of these are monotone: an $\varepsilon$-approximant need not restrict to an $\varepsilon$-approximant of a *subfunction* with controlled rank, so induction on rank fails.
- **Why lower-bound machinery does not see the counterexample.** Discrepancy, corruption, smooth rectangle and $\gamma_2$ bounds are all dominated by $\log \mathrm{rank}_\varepsilon$, hence all $O(\log n)$ for $\mathrm{SINK}\circ\mathrm{XOR}$. Only *information-theoretic* or *query-to-communication lifting* arguments — which are not rank-based — deliver the $\Omega(\sqrt n)$ bound. This is the structural reason the conjecture survived a decade: every technique that could have refuted it was itself bounded by approximate rank.
- **Nonnegative rank offers no repair.** The natural fix — demand a nonnegative approximant, which corresponds to randomized *nondeterministic* protocols — also fails, since $\mathrm{rank}^+_{1/3}(M_F)=O(n^{2.5})$ for the same $F$.

## 6. The Gap

What is proven: $\log\mathrm{rank}_{1/3}(M_f)\le O(R(f))\le \tilde O(\sqrt{\mathrm{rank}_{1/3}(M_f)})$, with an explicit total function achieving $R=\Omega(\sqrt n)$ against $\log\mathrm{rank}_{1/3}=O(\log n)$, i.e. $R(f)=2^{\Omega(\log\mathrm{rank}_{1/3})^{?}}$ — the separation is exponential in the log-rank parameter but only quartic-root in the rank itself ($R\approx \mathrm{rank}_{1/3}^{1/4}$).

The gap is therefore **quantitative, not qualitative**: is $R(f)=\tilde O(\mathrm{rank}_{1/3}(M_f)^{1/4})$ the truth, or can $R(f)=\Theta(\sqrt{\mathrm{rank}_{1/3}})$ be forced? Closing it requires either (i) a communication protocol of cost $\mathrm{rank}_\varepsilon^{1/4+o(1)}$ for all total $f$, or (ii) a family with $R(f)\ge \mathrm{rank}_\varepsilon^{1/2-o(1)}$. Separately, the exact log-rank conjecture is untouched by CMS: $\mathrm{SINK}_m$ has Fourier sparsity $m\cdot 2^{m-1}=2^{\Theta(\sqrt n)}$, so $\log\mathrm{rank}(M_F)=\Theta(\sqrt n)=\Theta(R(F))$ — perfectly consistent with log-rank.

## 7. Current Research (as of June 2026)

- **Optimal approximate-rank-vs-randomized separations.** Groups at Tata Institute (Chattopadhyay), CWI/QuSoft (de Wolf), and Toronto/Simons (Pitassi, Göös at EPFL) are pushing composed-function constructions past the $\mathrm{rank}^{1/4}$ barrier. *(frontier — verify)*
- **Lifting theorems as the replacement paradigm.** Query-to-communication lifting (Raz–McKenzie, Göös–Pitassi–Watson, Chattopadhyay–Koucký–Loff–Mukhopadhyay) is now the default route to lower bounds that rank cannot certify; current work seeks lifting with *constant-size* gadgets, which would sharpen all separations by log factors. *(frontier — verify)*
- **Restricted LARC.** Whether a polynomial relation holds for XOR functions of *low approximate degree*, or for functions with bounded $\mathbb{F}_2$-degree, remains actively studied; the $\mathrm{SINK}$ example has approximate degree $\Theta(\sqrt n)$, so it does not rule these out.
- **Quantum side.** After Anshu–Boddu–Touchette, attention has moved to whether $Q^*(f)$ and $\log\mathrm{rank}_{1/3}$ are polynomially related for *communication-friendly* classes, and to information-cost characterizations of $Q^*$.

## 8. Future Work

- Determine the true exponent $\alpha$ in $R(f)=\tilde\Theta(\mathrm{rank}_{1/3}(M_f)^{\alpha})$; currently $1/4\le\alpha\le 1/2$.
- Identify a *corrected* complexity measure that is polynomially equivalent to $R(f)$ — candidates include relaxed partition bound, information complexity, and $\gamma_2^{\alpha}$-style norms with rectangle-size penalties.
- Resolve the exact log-rank conjecture, or transplant the $\mathrm{SINK}$ construction to exact rank by finding a total $f$ with small Fourier sparsity but large deterministic complexity.
- Settle whether small spectral norm implies efficient *deterministic* protocols for XOR functions (currently open even for $\|\hat f\|_1=\mathrm{poly}\log n$).
- Extend the refutation to number-in-hand multiparty and to nonnegative-rank-based LP/SDP extension-complexity settings.

## 9. Key References

- **[Foundational]** L. Lovász, M. Saks. *Lattices, Möbius functions and communication complexity.* FOCS, 1988.
- **[Foundational]** H. Buhrman, R. de Wolf. *Communication complexity lower bounds by polynomials.* IEEE Conference on Computational Complexity (CCC), 2001.
- **[Foundational / Survey]** T. Lee, A. Shraibman. *Lower Bounds in Communication Complexity.* Foundations and Trends in Theoretical Computer Science, vol. 3, no. 4, 2009. (Statement of the log-approximate-rank conjecture.)
- **[SOTA]** A. Chattopadhyay, N. S. Mande, S. Sherif. *The Log-Approximate-Rank Conjecture is False.* STOC 2019; Journal of the ACM, vol. 67, no. 4, 2020.
- **[SOTA]** M. Sinha, R. de Wolf. *Exponential Separation between Quantum Communication and Logarithm of Approximate Rank.* FOCS, 2019.
- **[SOTA]** A. Anshu, N. G. Boddu, D. Touchette. *Quantum Log-Approximate-Rank Conjecture is Also False.* FOCS, 2019.
- **[SOTA]** S. Lovett. *Communication is bounded by root of rank.* Journal of the ACM, vol. 63, no. 1, 2016.
- **[SOTA]** A. Gál, R. Syed. *Upper bounds on communication in terms of approximate rank.* Theory of Computing Systems, 2022.
- **[Related]** M. Göös, T. Pitassi, T. Watson. *Deterministic Communication vs. Partition Number.* FOCS 2015; SIAM Journal on Computing, vol. 47, no. 6, 2018.
- **[Related]** V. Grolmusz. *On the power of circuits with gates of low L1 norms.* Theoretical Computer Science, vol. 188, 1997.
- **[Survey]** S. Lovett. *Recent advances on the log-rank conjecture in communication complexity.* Bulletin of the EATCS, no. 112, 2014.
- **[Textbook]** A. Rao, A. Yehudayoff. *Communication Complexity and Applications.* Cambridge University Press, 2020.

## 10. Worked Example / Concrete Special Case

Take $m=3$, so $n=\binom32=3$ variables $z_{12},z_{13},z_{23}$, with the convention $z_{ij}=1$ meaning the edge is oriented **into $i$**. Vertex $1$ is a sink iff $z_{12}=z_{13}=1$; vertex $2$ iff $z_{12}=0,z_{23}=1$; vertex $3$ iff $z_{13}=0,z_{23}=0$. Enumerating $(z_{12},z_{13},z_{23})$:

| $z$ | 000 | 001 | 010 | 011 | 100 | 101 | 110 | 111 |
|---|---|---|---|---|---|---|---|---|
| $\mathrm{SINK}_3$ | 1 | 1 | 0 | 1 | 1 | 0 | 1 | 1 |

The two zeros are exactly the two cyclic tournaments on three vertices ($6$ of the $8$ tournaments have a sink). Note $\{010,101\}=\{z: z_{12}\oplus z_{13}=1 \text{ and } z_{13}\oplus z_{23}=1\}$, so the indicator of the zero-set is
$$g=\frac{1-\chi_{\{12,13\}}}{2}\cdot\frac{1-\chi_{\{13,23\}}}{2}=\tfrac14\big(1-\chi_{\{12,13\}}-\chi_{\{13,23\}}+\chi_{\{12,23\}}\big),$$
using $\chi_{\{12,13\}}\chi_{\{13,23\}}=\chi_{\{12,23\}}$. Hence
$$\mathrm{SINK}_3 \;=\; \tfrac34+\tfrac14\chi_{\{12,13\}}+\tfrac14\chi_{\{13,23\}}-\tfrac14\chi_{\{12,23\}},$$
with Fourier sparsity $4$ and spectral norm $\|\hat f\|_1=\tfrac34+3\cdot\tfrac14=\tfrac32\le m=3$, matching the general bound $\|\widehat{\mathrm{SINK}_m}\|_1\le m=O(\sqrt n)$.

Consequently $F(x,y)=\mathrm{SINK}_3(x\oplus y)$ has an $8\times 8$ communication matrix $M_F=\sum_S \hat f(S)v_Sv_S^\top$ of exact rank $4$.

**Scaling up.** For general $m$: (i) $\|\hat f\|_1\le m$ gives, by Grolmusz sparsification, an $\varepsilon$-approximant of sparsity $O(m^2/\varepsilon^2)=O(n/\varepsilon^2)$, so $\mathrm{rank}_{1/3}(M_F)=\mathrm{poly}(n)$ and $\log\mathrm{rank}_{1/3}(M_F)=O(\log n)$; (ii) embedding Set-Disjointness on $\Theta(m)$ coordinates into the "which vertex is the sink" structure, together with the $\Omega(m)$ bound of Kalyanasundaram–Schnitger and Razborov, gives $R(F)=\Omega(m)=\Omega(\sqrt n)$. The two facts are incompatible with LARC.

Finally, contrast with exact rank: the $m$ disjoint conjunctions of $\mathrm{SINK}_m$ have $m\cdot 2^{m-1}=2^{\Theta(\sqrt n)}$ Fourier coefficients, so $\log\mathrm{rank}(M_F)=\Theta(\sqrt n)\approx R(F)$. The same function that kills the approximate conjecture is a *perfect* example for the exact one — the failure is entirely an artifact of approximation.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*