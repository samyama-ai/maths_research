---
id: 10-theoretical-cs/bqp-versus-ph
title: "BQP versus PH"
topic: 10-theoretical-cs
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# BQP versus PH

> **Topic:** Theoretical Computer Science · **ID:** `10-theoretical-cs/bqp-versus-ph` · **Status:** open

## 1. Problem Statement / Conjecture

Is $\mathsf{BQP} \subseteq \mathsf{PH}$?

$\mathsf{BQP}$ is the class of languages decided by polynomial-time quantum algorithms with bounded error; $\mathsf{PH} = \bigcup_{k\ge 0}\Sigma_k^{\mathrm p}$ is the polynomial hierarchy. The question asks whether every problem efficiently solvable by a quantum computer can be expressed by a constant number of alternating polynomial-length quantifiers over a polynomial-time predicate.

Both containments are open and neither is known to fail:

- $\mathsf{BQP} \subseteq \mathsf{PH}$: unknown. Not even $\mathsf{BQP}\subseteq \Sigma_2^{\mathrm p}$ or $\mathsf{BQP}\subseteq\mathsf{AM}$ is known.
- $\mathsf{PH} \subseteq \mathsf{BQP}$: unknown, but widely disbelieved (it would imply $\mathsf{NP}\subseteq\mathsf{BQP}$).

A resolution in either direction is a non-relativizing result: relative to an oracle, both containments are known to be false (Raz–Tal 2019 for the first; Bennett–Bernstein–Brassard–Vazirani 1997 for the second). A complete solution therefore means either (a) a uniform simulation of quantum computation by a constant-alternation classical machine, or (b) an unconditional separation, which would in particular give $\mathsf{P}\ne\mathsf{PSPACE}$ and hence is beyond current technique. The realistic near-term target is the *conditional* or *structured* version: identify plausible complexity assumptions under which $\mathsf{BQP}\not\subseteq\mathsf{PH}$.

## 2. Mathematical Foundations

**BQP.** $L\in\mathsf{BQP}$ if there is a polynomial-time uniform family of quantum circuits $\{C_n\}$ over a fixed universal gate set, with $C_n$ acting on $p(n)$ qubits, such that
$$
x\in L \Rightarrow \Pr[C_{|x|}(x)=1]\ge \tfrac23,\qquad
x\notin L \Rightarrow \Pr[C_{|x|}(x)=1]\le \tfrac13 ,
$$
where $\Pr[C(x)=1]=\big\|(\,|1\rangle\langle 1|\otimes I)\,U_{C}\,|x\rangle|0^{m}\rangle\big\|^2$. Error amplification by majority is standard, so the constants are immaterial.

**PH.** $L\in\Sigma_k^{\mathrm p}$ iff there is a polynomial-time predicate $R$ and polynomial $q$ with
$$
x\in L \iff \exists y_1\forall y_2\cdots Q_k y_k\ R(x,y_1,\dots,y_k),\qquad |y_i|\le q(|x|).
$$
Equivalently (Furst–Saxe–Sipser), $\mathsf{PH}$ relativizes to the non-uniform class $\mathsf{AC}^0$: a language in $\mathsf{PH}^A$ is decided, for each input length, by a depth-$d$, size-$2^{\mathrm{polylog}}$ (quasipolynomial) unbounded-fan-in circuit reading the oracle string $A$. This is the form used in all oracle separations.

**Known containments.**
$$
\mathsf{BPP}\subseteq\mathsf{BQP}\subseteq\mathsf{AWPP}\subseteq\mathsf{PP}\subseteq\mathsf{P}^{\\#\mathsf P}\subseteq\mathsf{PSPACE}.
$$
$\mathsf{BQP}\subseteq\mathsf{PP}$ is Adleman–DeMarrais–Huang (1997), via writing the final amplitude as a $\mathsf{GapP}$ function
$$
\langle 1 | U_C |x,0^m\rangle=\sum_{\text{paths}}\prod_{t}\langle s_{t+1}|U_t|s_t\rangle ,
$$
a signed sum over exponentially many computational paths. Fortnow–Rogers (1999) sharpened this to $\mathsf{AWPP}$, a "one-sided gap" class, which is why $\mathsf{BQP}$ is *low* for $\mathsf{PP}$: $\mathsf{PP}^{\mathsf{BQP}}=\mathsf{PP}$.

**Why the containment is not free.** Toda's theorem gives $\mathsf{PH}\subseteq\mathsf{P}^{\mathsf{PP}}$, i.e. $\mathsf{PP}$ sits *above* $\mathsf{PH}$; so $\mathsf{BQP}\subseteq\mathsf{PP}$ gives no upper bound inside $\mathsf{PH}$. Indeed $\mathsf{PP}\subseteq\mathsf{PH}$ would collapse the hierarchy.

**Forrelation.** For $f,g:\{0,1\}^n\to\{\pm1\}$ with $N=2^n$, define
$$
\Phi_{f,g}\;=\;\frac{1}{2^{3n/2}}\sum_{x,y\in\{0,1\}^n} f(x)\,(-1)^{x\cdot y}\,g(y)\;=\;\langle \hat f, g\rangle .
$$
$|\Phi_{f,g}|\le 1$. **Forrelation** is the promise problem: decide $|\Phi|\le 1/100$ versus $\Phi\ge 3/5$. One quantum query suffices (Section 10); classically $\tilde\Omega(\sqrt N)$ queries are needed.

**The Aaronson–Ambainis conjecture.** Every bounded degree-$d$ multilinear polynomial $p:\{0,1\}^N\to[-1,1]$ has a variable of influence at least $(\mathrm{Var}(p)/d)^{O(1)}$. This is the main structural conjecture whose truth would obstruct large query separations for total functions.

## 3. History & State of the Art (SOTA)

- **1993/1997.** Bernstein–Vazirani define $\mathsf{BQP}$ and prove $\mathsf{BQP}\subseteq\mathsf{P}^{\\#\mathsf P}$; the question "is $\mathsf{BQP}\subseteq\mathsf{PH}$?" is posed immediately after, since no classical class below $\mathsf{PP}$ was known to contain it.
- **1994.** Shor's factoring algorithm gives no evidence either way: factoring is in $\mathsf{NP}\cap\mathsf{coNP}\subseteq\mathsf{PH}$.
- **1997–1999.** $\mathsf{BQP}\subseteq\mathsf{AWPP}$ (Fortnow–Rogers); $\mathsf{BQP}$ low for $\mathsf{PP}$.
- **2010.** Aaronson, *BQP and the Polynomial Hierarchy* (STOC), proposes Fourier Checking and Forrelation as oracle candidates, and reduces the oracle separation to a "Generalized Linial–Nisan conjecture" about $\mathsf{AC}^0$ fooled by almost $k$-wise independent distributions. He then disproves the generalized form; the weaker Linial–Nisan conjecture is proved by Braverman (2010, polylogarithmic independence fools $\mathsf{AC}^0$).
- **2015/2018.** Aaronson–Ambainis: Forrelation needs $\Omega(\sqrt N/\log N)$ randomized queries against $1$ quantum query, and no $t$-query quantum algorithm beats $O(N^{1-1/2t})$ classical queries — an optimal separation for the query model.
- **2017.** Tal proves tight $L_1$ Fourier bounds for $\mathsf{AC}^0$: a depth-$d$, size-$M$ circuit satisfies $\sum_{|S|=k}|\hat C(S)| \le O(\log M)^{(d-1)k}$.
- **2019.** **Raz–Tal** (STOC; JACM 2022) combine Tal's bound with a stochastic-calculus ("Brownian") argument to show that the Forrelation distribution fools $\mathsf{AC}^0$ with advantage $\mathrm{polylog}(N)^{d}/\sqrt N$, giving an oracle $A$ with $\mathsf{BQP}^A\not\subseteq\mathsf{PH}^A$. This settled the 25-year-old relativized version.
- **2021.** Bansal–Sinha and, independently, Sherstov–Storozhenko–Wu prove the $k$-fold Forrelation conjecture: $R(\mathrm{forr}_k)=\Omega(N^{1-1/k})$ against $\lceil k/2\rceil$ quantum queries.
- **2022.** Aaronson–Ingram–Kretschmer, *The Acrobatics of BQP*, build oracles where $\mathsf{P}=\mathsf{NP}$ yet $\mathsf{BQP}\ne\mathsf{QCMA}$, showing $\mathsf{BQP}$'s relation to classical classes is unusually oracle-fragile.

**State of the art in the unrelativized world: nothing.** No containment better than $\mathsf{AWPP}$, no consequence-bearing separation.

## 4. Partial Results / Verified Cases

- **Query/oracle model (solved).** $\exists A:\ \mathsf{BQP}^A\not\subseteq\mathsf{PH}^A$ (Raz–Tal 2019). The separation holds for a *random* oracle drawn from the Forrelation distribution; the advantage of any depth-$d$ size-$M$ circuit is $O\!\big((\log M)^{2d}/\sqrt N\big)$.
- **Converse direction, oracle model (solved).** $\exists A:\ \mathsf{NP}^A\not\subseteq\mathsf{BQP}^A$; indeed for a random oracle, unstructured search needs $\Theta(\sqrt N)$ quantum queries (BBBV 1997, Grover matching upper bound). Hence $\mathsf{PH}^A\not\subseteq\mathsf{BQP}^A$.
- **Optimal query separations (solved).** $k$-Forrelation: quantum $\lceil k/2\rceil$ queries vs. randomized $\Omega(N^{1-1/k})$, matching the $O(N^{1-1/2t})$ upper bound for $t$-query quantum algorithms up to constants in the exponent — so the query model is closed.
- **Sampling problems (conditional).** If BosonSampling or IQP output distributions could be sampled exactly in classical polynomial time, then $\mathsf{PH}$ collapses to $\Sigma_3^{\mathrm p}$ (Aaronson–Arkhipov 2013; Bremner–Jozsa–Shepherd 2011), via Stockmeyer approximate counting. This is a genuine unrelativized theorem — but about *sampling* classes, not $\mathsf{BQP}$ decision problems.
- **Structured upper bounds.** All known natural $\mathsf{BQP}$ problems (factoring, discrete log, Pell's equation, hidden subgroup for abelian groups, Jones polynomial approximation) lie in $\mathsf{NP}\cap\mathsf{coNP}$ or in low levels of $\mathsf{PH}$ — i.e. every *concrete* case is verified to be inside $\mathsf{PH}$.

## 5. Principal Obstacles

- **Relativization is exhausted, and it cuts both ways.** Raz–Tal shows no relativizing proof of $\mathsf{BQP}\subseteq\mathsf{PH}$ exists; BBBV shows no relativizing proof of the reverse. Any resolution must use non-relativizing tools (arithmetization, PCP-style algebra, interactive proofs), and the only known non-relativizing hammer — Toda / $\mathsf{IP}=\mathsf{PSPACE}$ arithmetization — lands at $\mathsf{PP}$ or $\mathsf{PSPACE}$, far above $\mathsf{PH}$.
- **Interference has no quantifier normal form.** The acceptance probability is a signed sum $\sum_{\text{paths}} \prod_t \langle s_{t+1}|U_t|s_t\rangle$ with cancellation. Existential/universal quantifiers count witnesses monotonically; there is no known way to certify near-total cancellation with $O(1)$ alternations. This is exactly the reason $\mathsf{GapP}$ collapses only to $\mathsf{PP}$.
- **$\mathsf{AC}^0$ lower-bound technology tops out at $\sqrt N$ advantage.** Tal's $L_1$ Fourier bound is tight; the Raz–Tal advantage $\mathrm{polylog}(N)^d/\sqrt N$ cannot be pushed further without new switching-lemma-type results, so even in the oracle world the separation is at the technique's ceiling.
- **The Aaronson–Ambainis conjecture blocks the total-function route.** If true, no *total* Boolean problem gives a superpolynomial quantum query speedup that survives averaging, so any separation must exploit a promise or a distribution — which does not translate to a uniform complexity-class separation.
- **Separation implies major lower bounds.** $\mathsf{BQP}\not\subseteq\mathsf{PH}$ implies $\mathsf{P}\ne\mathsf{PH}$, hence $\mathsf{P}\ne\mathsf{NP}$. Natural-proofs and algebrization barriers apply.

## 6. The Gap

The gap is the passage from **query complexity with a promise** to **uniform computation without one**.

- Proven: there is a *distribution over oracle strings* on which one quantum query and quasipolynomial-size constant-depth circuits disagree by $\Omega(1)$ vs. $o(1)$.
- Needed: a *language*, defined by a uniform polynomial-time description with no oracle and no promise, in $\mathsf{BQP}$ and provably outside $\Sigma_k^{\mathrm p}$ for every $k$.

Concretely, one must (i) instantiate the Forrelation oracle with an explicit pseudorandom object whose Fourier-analytic indistinguishability from the Forrelation distribution can be *proved* against $\mathsf{PH}$, and (ii) do so without an oracle, i.e. prove an unconditional $\mathsf{PH}$ lower bound. Step (ii) alone would resolve $\mathsf{P}\ne\mathsf{NP}$. In the containment direction, the missing step is a quantifier-bounded simulation of amplitude cancellation: a $\Sigma_k^{\mathrm p}$ predicate certifying $|\langle 1|U_C|x,0^m\rangle|^2 \ge 2/3$ for constant $k$, where every known certificate needs approximate counting nested to depth $\mathrm{poly}(n)$.

## 7. Current Research (as of June 2026)

- **Aaronson–Ambainis conjecture.** Progress on special cases: symmetric polynomials, low-degree/block-multilinear forms, and the "one influential variable" version for degree $2$. Full resolution remains open; groups at UT Austin (Aaronson), Waterloo/IQC, and Tel Aviv (Tal) are active. Partial results via hypercontractivity and Fourier-growth machinery continue to appear. *(frontier — verify)*
- **Fourier growth of stronger circuit classes.** Extending Tal-style $L_1$ bounds beyond $\mathsf{AC}^0$ — to $\mathsf{AC}^0[\oplus]$, low-depth decision trees of parities, and branching programs — with the goal of separating $\mathsf{BQP}$ from richer relativized classes. This is the most active technical front. *(frontier — verify)*
- **Oracle "acrobatics."** Following Aaronson–Ingram–Kretschmer, constructing oracles that decouple $\mathsf{BQP}$ from $\mathsf{QCMA}$, $\mathsf{QMA}$, $\mathsf{SZK}$, and $\mathsf{PH}$ simultaneously, mapping which combinations of relativized facts are jointly realizable.
- **Quantum-classical separations from cryptography.** Kretschmer's line on pseudorandom quantum states and oracle-based quantum advantage without $\mathsf{P}\ne\mathsf{NP}$; relatedly, classically-verifiable quantum advantage (Brakerski–Christiano–Mahadev–Vazirani–Vidick) as evidence that $\mathsf{BQP}$ contains problems with no short classical certificates.
- **Sampling-based collapse arguments.** Sharpening Aaronson–Arkhipov to *approximate* sampling under the Permanent-of-Gaussians and anticoncentration conjectures; Fefferman–Umans's Quantum Fourier Sampling gives an alternative route via $\\#\mathsf P$-hardness of a Fourier-coefficient gap.

## 8. Future Work

- Prove or refute the Aaronson–Ambainis conjecture; either outcome sharply reshapes what a separation could look like.
- Push Fourier-growth bounds from $\mathsf{AC}^0$ to $\mathsf{AC}^0[\oplus]$ and to polynomial-size formulas, aiming at $\mathsf{BQP}^A\not\subseteq\mathsf{PH}^A$ variants robust to parity gates.
- Find an explicit ("de-oracled") Forrelation instance — e.g. based on a concrete pseudorandom generator — and reduce $\mathsf{BQP}\not\subseteq\mathsf{PH}$ to a standard cryptographic assumption.
- Determine whether $\mathsf{BQP}\subseteq\mathsf{AM}$ or $\mathsf{BQP}\subseteq\mathsf{S}_2^{\mathrm p}$ holds under derandomization hypotheses; any such containment would be the first evidence for the positive side.
- Clarify the relationship between the sampling collapse theorems and decision-class separation: does approximate hardness of quantum sampling imply anything for $\mathsf{BQP}$ vs. $\mathsf{PH}$?

## 9. Key References

- **[Foundational]** E. Bernstein, U. Vazirani. *Quantum Complexity Theory.* SIAM Journal on Computing 26(5):1411–1473, 1997 (STOC 1993).
- **[Foundational]** L. Adleman, J. DeMarrais, M.-D. Huang. *Quantum Computability.* SIAM Journal on Computing 26(5):1524–1540, 1997.
- **[Foundational]** L. Fortnow, J. Rogers. *Complexity Limitations on Quantum Computation.* Journal of Computer and System Sciences 59(2):240–252, 1999.
- **[Foundational]** S. Toda. *PP is as Hard as the Polynomial-Time Hierarchy.* SIAM Journal on Computing 20(5):865–877, 1991.
- **[Foundational]** C. Bennett, E. Bernstein, G. Brassard, U. Vazirani. *Strengths and Weaknesses of Quantum Computing.* SIAM Journal on Computing 26(5):1510–1523, 1997.
- **[Foundational]** S. Aaronson. *BQP and the Polynomial Hierarchy.* Proc. 42nd ACM Symposium on Theory of Computing (STOC), 141–150, 2010.
- **[SOTA / Recent]** R. Raz, A. Tal. *Oracle Separation of BQP and PH.* Proc. 51st STOC, 13–23, 2019; Journal of the ACM 69(4), Article 30, 2022.
- **[SOTA / Recent]** A. Tal. *Tight Bounds on the Fourier Spectrum of AC0.* Proc. 32nd Computational Complexity Conference (CCC), 15:1–15:31, 2017.
- **[SOTA / Recent]** S. Aaronson, A. Ambainis. *Forrelation: A Problem That Optimally Separates Quantum from Classical Computing.* SIAM Journal on Computing 47(3):982–1038, 2018 (STOC 2015).
- **[SOTA / Recent]** N. Bansal, M. Sinha. *k-Forrelation Optimally Separates Quantum and Classical Query Complexity.* Proc. 53rd STOC, 1303–1316, 2021.
- **[SOTA / Recent]** A. Sherstov, A. Storozhenko, P. Wu. *An Optimal Separation of Randomized and Quantum Query Complexity.* Proc. 53rd STOC, 1289–1302, 2021.
- **[SOTA / Recent]** S. Aaronson, D. Ingram, W. Kretschmer. *The Acrobatics of BQP.* Proc. 37th CCC, 20:1–20:17, 2022.
- **[SOTA / Recent]** S. Aaronson, A. Arkhipov. *The Computational Complexity of Linear Optics.* Theory of Computing 9(4):143–252, 2013.
- **[SOTA / Recent]** B. Fefferman, C. Umans. *The Power of Quantum Fourier Sampling.* Proc. 11th Conference on the Theory of Quantum Computation, Communication and Cryptography (TQC), 2016.
- **[Survey]** S. Aaronson, A. Ambainis. *The Need for Structure in Quantum Speedups.* Theory of Computing 10(6):133–166, 2014.
- **[Survey]** J. Watrous. *Quantum Computational Complexity.* In *Encyclopedia of Complexity and Systems Science*, Springer, 2009.
- **[Survey]** S. Arora, B. Barak. *Computational Complexity: A Modern Approach.* Cambridge University Press, 2009 (Chapters 5, 10, 17).

## 10. Worked Example / Concrete Special Case

**The one-query Forrelation algorithm, and the $n=1$ instance.**

*Algorithm.* Given oracles for $f,g:\{0,1\}^n\to\{\pm1\}$, run on $n$ qubits:
$$
|0^n\rangle \xrightarrow{H^{\otimes n}} \frac{1}{\sqrt N}\sum_x |x\rangle
\xrightarrow{O_f} \frac{1}{\sqrt N}\sum_x f(x)|x\rangle
\xrightarrow{H^{\otimes n}} \frac{1}{N^{3/2}}\!\!\sum_{x,y}\!f(x)(-1)^{x\cdot y}|y\rangle
\xrightarrow{O_g}\ \cdot\ \xrightarrow{H^{\otimes n}}
$$
The amplitude on $|0^n\rangle$ is exactly
$$
\alpha_0=\frac{1}{2^{3n/2}}\sum_{x,y} f(x)(-1)^{x\cdot y} g(y)=\Phi_{f,g},
$$
so measuring gives outcome $0^n$ with probability $\Phi_{f,g}^2$. Two oracle calls (one per function; one "query" in the standard Forrelation convention) suffice to estimate $\Phi$ to constant additive error by repetition.

*Instance $n=1$, $N=2$.* Write $f=(f(0),f(1))$, $g=(g(0),g(1))\in\{\pm1\}^2$. Here $2^{3n/2}=2^{3/2}=2\sqrt2$ and
$$
\Phi_{f,g}=\frac{f(0)g(0)+f(0)g(1)+f(1)g(0)-f(1)g(1)}{2\sqrt2}.
$$

| $f$ | $g$ | numerator | $\Phi$ | $\Pr[0]$ |
|---|---|---|---|---|
| $(1,1)$ | $(1,1)$ | $1+1+1-1=2$ | $1/\sqrt2$ | $1/2$ |
| $(1,1)$ | $(1,-1)$ | $1-1+1+1=2$ | $1/\sqrt2$ | $1/2$ |
| $(1,-1)$ | $(1,-1)$ | $1-1-1-1=-2$ | $-1/\sqrt2$ | $1/2$ |

Every $n=1$ instance has $|\Phi|=1/\sqrt2$: with $N=2$ the Hadamard transform of a $\pm1$ vector is never near-orthogonal to another, so the promise gap $\{|\Phi|\le 1/100\}$ vs. $\{\Phi\ge 3/5\}$ is vacuous at $n=1$. The problem only becomes meaningful once $N$ is large, where a *random* pair $(f,g)$ has $\mathbb E[\Phi]=0$ and $\mathrm{Var}(\Phi)=1/N$, i.e. $|\Phi|\approx N^{-1/2}$, while a Forrelated pair (sample $z\sim\mathcal N(0,\epsilon^2 I_N)$, set $f=\mathrm{sgn}(z)$, $g=\mathrm{sgn}(\hat z)$) has $\Phi=\Omega(1)$.

*Why $\mathsf{PH}$ struggles.* A $\Sigma_k^{\mathrm p}$ machine relativized to the oracle string is a depth-$d$, quasipolynomial-size $\mathsf{AC}^0$ circuit on $2N$ input bits. Tal's bound gives $\sum_{|S|=k}|\hat C(S)|\le O(\log M)^{(d-1)k}$, and Raz–Tal's stochastic-walk argument converts this into
$$
\big|\Pr_{\text{Forrelated}}[C=1]-\Pr_{\text{uniform}}[C=1]\big| \;=\; O\!\left(\frac{(\log M)^{2d}}{\sqrt N}\right)\xrightarrow[N\to\infty]{}0 ,
$$
while the quantum algorithm above distinguishes with constant advantage using one query. That is the entire oracle separation — and the reason it does not de-relativize is that the argument needs the oracle string to be *drawn at random*, a resource unavailable to a uniform machine.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*