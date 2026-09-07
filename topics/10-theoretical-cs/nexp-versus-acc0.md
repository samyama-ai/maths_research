---
id: 10-theoretical-cs/nexp-versus-acc0
title: "NEXP versus ACC0"
topic: 10-theoretical-cs
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# NEXP versus ACC0

> **Topic:** Theoretical Computer Science · **ID:** `10-theoretical-cs/nexp-versus-acc0` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

$\mathsf{ACC}^0$ is the class of languages decided by families of constant-depth, polynomial-size Boolean circuits with unbounded fan-in $\mathsf{AND}$, $\mathsf{OR}$, $\mathsf{NOT}$, and $\mathsf{MOD}_m$ gates for some fixed integer $m > 1$. The question is how much computational power lies above it.

Williams (2011) proved $\mathsf{NEXP} \not\subseteq \mathsf{ACC}^0$, so the original separation is *settled*. What remains open, and is the live content of the problem, is the strength of the separation:

1. **Scaling down the hard class.** Is $\mathsf{NP} \not\subseteq \mathsf{ACC}^0$? Is $\mathsf{EXP} \not\subseteq \mathsf{ACC}^0$ (deterministic, no nondeterminism)? Currently the best is $\mathsf{NQP} = \mathsf{NTIME}[n^{\mathrm{polylog}\, n}] \not\subseteq \mathsf{ACC}^0$ (Murray–Williams 2018).
2. **Explicitness.** Exhibit a *single explicit* function — e.g. $\mathsf{SAT}$, $\mathsf{MAJORITY}$, or an $\mathsf{NP}$-complete language — not in $\mathsf{ACC}^0$. None is known. In particular whether $\mathsf{ACC}^0 = \mathsf{TC}^0$ is open.
3. **Scaling up the circuit class.** Extend to $\mathsf{ACC}^0 \circ \mathsf{THR}$, $\mathsf{TC}^0$, $\mathsf{NC}^1$, $\mathsf{P/poly}$.

A complete resolution of (2) at the level of $\mathsf{NP}$ would mean: a language $L \in \mathsf{NP}$ and a proof that for every $m, d, c$ and all large $n$, no depth-$d$ size-$n^c$ circuit over $\{\mathsf{AND},\mathsf{OR},\mathsf{NOT},\mathsf{MOD}_m\}$ decides $L \cap \{0,1\}^n$.

## 2. Mathematical Foundations

**Circuit classes.** $\mathsf{AC}^0[m]$: depth-$O(1)$, size-$n^{O(1)}$ circuits over $\{\mathsf{AND},\mathsf{OR},\mathsf{NOT},\mathsf{MOD}_m\}$, where
$$\mathsf{MOD}_m(y_1,\dots,y_k) = 1 \iff \sum_{i=1}^k y_i \equiv 0 \pmod m .$$
Then $\mathsf{ACC}^0 = \bigcup_{m \ge 2} \mathsf{AC}^0[m]$, and
$$\mathsf{AC}^0 \subsetneq \mathsf{ACC}^0 \subseteq \mathsf{TC}^0 \subseteq \mathsf{NC}^1 \subseteq \mathsf{P/poly}.$$
All inclusions after the first are open.

**Algebraic characterization (Razborov–Smolensky).** For prime $p$, any depth-$d$ size-$s$ $\mathsf{AC}^0[p]$ circuit is approximated on a $1-\varepsilon$ fraction of inputs by a polynomial over $\mathbb{F}_p$ of degree $O\!\left((\log(s/\varepsilon))^d\right)$. Since $\mathsf{MOD}_q$ for $q \neq p$ requires degree $\Omega(\sqrt{n})$ for constant-error approximation, $\mathsf{MOD}_q \notin \mathsf{AC}^0[p]$ when $p$ is prime and $q$ has a prime factor $\ne p$. This argument collapses for composite $m$: $\mathbb{Z}/m\mathbb{Z}$ is not a field, low-degree polynomials over it can compute $\mathsf{OR}$ exactly, and no degree lower bound survives.

**Depth reduction (Yao 1990; Beigel–Tarui 1994).** Every depth-$d$, size-$s$ $\mathsf{ACC}^0$ circuit is equivalent to a depth-2 circuit
$$C(x) = g\!\left(\sum_{j=1}^{S} \bigwedge_{i \in T_j} x_i^{(\pm)}\right), \qquad S \le 2^{(\log s)^{O(d)}},$$
where $g : \{0,\dots,S\} \to \{0,1\}$ is an arbitrary symmetric function given by a table. This is the $\mathsf{SYM} \circ \mathsf{AND}$ normal form; the $\mathsf{AND}$s have fan-in $(\log s)^{O(d)}$. Chen–Papakonstantinou (2016) improved the transformation to $S \le 2^{O(\log^{2d} s)}$ with quasi-linear-time constructibility.

**The algorithmic method (Williams 2010).** If for some $\varepsilon>0$ the satisfiability of $\mathcal{C}$-circuits with $n$ inputs and $2^{n^{o(1)}}$ size can be decided in time $2^{n}/n^{\omega(1)}$, then $\mathsf{NEXP} \not\subseteq \mathcal{C}$. The proof combines: (i) the Impagliazzo–Kabanets–Wigderson easy-witness lemma — $\mathsf{NEXP} \subseteq \mathsf{P/poly}$ implies $\mathsf{NEXP} = \mathsf{MA}$ and every $\mathsf{NEXP}$ verifier has succinct (circuit-encoded) witnesses; (ii) succinct reductions to $\mathsf{SUCCINCT}\text{-}\mathsf{3SAT}$, which is $\mathsf{NEXP}$-complete; (iii) a nondeterministic speedup contradicting the nondeterministic time hierarchy $\mathsf{NTIME}[2^n] \not\subseteq \mathsf{NTIME}[2^n/n]$.

**The $\mathsf{ACC}^0$-SAT algorithm.** Combining the normal form with fast rectangular matrix multiplication (Coppersmith), Williams evaluates the $\mathsf{SYM}\circ\mathsf{AND}$ form on all $2^{k}$ assignments to a suffix of variables in near-optimal time, yielding a satisfiability algorithm for depth-$d$ size-$s$ $\mathsf{ACC}^0$ circuits running in time
$$2^{\,n - \Omega(n^{\delta})}, \qquad \delta = \delta(d,m) > 0 .$$

## 3. History & State of the Art (SOTA)

- **1987.** Razborov and Smolensky independently prove $\mathsf{PARITY} \notin \mathsf{AC}^0[p]$ for prime $p$; progress on composite $m$ halts for 24 years.
- **1990.** Yao shows $\mathsf{ACC}^0 \subseteq \mathsf{SYM}\circ\mathsf{AND}$ of quasipolynomial size (probabilistic construction); Beigel–Tarui (1994) derandomize and simplify it.
- **1997.** Razborov–Rudich formalize the *natural proofs* barrier: the Razborov–Smolensky method is natural, so it cannot extend to classes computing pseudorandom functions.
- **2010.** Williams: "improving exhaustive search implies superpolynomial lower bounds" — the algorithmic method.
- **2011.** Williams: $\mathsf{NEXP} \not\subseteq \mathsf{ACC}^0$, indeed against $\mathsf{ACC}^0$ circuits of size $2^{n^{o(1)}}$ and any constant depth; also $\mathsf{E}^{\mathsf{NP}}$ requires $\mathsf{ACC}^0$ circuits of size $2^{n^{\Omega(1)}}$.
- **2014.** Williams extends to $\mathsf{ACC}^0 \circ \mathsf{THR}$ (one layer of linear threshold gates at the bottom).
- **2018.** Murray–Williams prove an easy-witness lemma for $\mathsf{NQP}$ and $\mathsf{NP}$, giving $\mathsf{NQP} \not\subseteq \mathsf{ACC}^0$ and $\mathsf{NTIME}[n^{\mathrm{polylog}\,n}] \not\subseteq \mathsf{ACC}^0 \circ \mathsf{THR}$.
- **2020.** Chen–Ren: strong *average-case* lower bounds — no $\mathsf{ACC}^0$ circuit computes the $\mathsf{NQP}$ language on more than a $1/2 + 1/\mathrm{polylog}(n)$ fraction of inputs. Chen–Lyu–Williams: *almost-everywhere* lower bounds (hard on all but finitely many input lengths, not just infinitely many).
- **2023.** Vyas–Williams identify oracle settings where the algorithmic method itself fails, delimiting its reach.

## 4. Partial Results / Verified Cases

- **Prime moduli, exact:** $\mathsf{MOD}_q \notin \mathsf{AC}^0[p]$ for distinct primes $p,q$; $\mathsf{MAJORITY} \notin \mathsf{AC}^0[p]$; correlation with $\mathsf{MOD}_p$ circuits is $\exp(-\Omega(n/4^d))$ (Razborov 1987, Smolensky 1987).
- **Nondeterministic classes:** $\mathsf{NEXP} \not\subseteq \mathsf{ACC}^0[2^{n^{o(1)}}]$; $\mathsf{NQP} \not\subseteq \mathsf{ACC}^0$ of size $n^{\log^c n}$ for every $c$; $\mathsf{NQP} \not\subseteq \mathsf{ACC}^0 \circ \mathsf{THR}$.
- **Deterministic with an oracle:** $\mathsf{E}^{\mathsf{NP}} = \mathsf{DTIME}[2^{O(n)}]^{\mathsf{NP}}$ requires $\mathsf{ACC}^0$ circuits of size $2^{n^{\delta}}$ for some $\delta>0$ depending on the depth $d$ and modulus $m$.
- **Depth 2 and 3, restricted:** exponential lower bounds are known for $\mathsf{MOD}_m \circ \mathsf{MOD}_p$ and for $\mathsf{AND} \circ \mathsf{MOD}_m$ circuits with small bottom fan-in; sub-exponential bounds for $\mathsf{CC}^0[m]$ (pure $\mathsf{MOD}$ circuits) of depth 2.
- **Algorithmic side:** $\mathsf{ACC}^0$-SAT in $2^{n-n^{\delta}}$; $\mathsf{ACC}^0 \circ \mathsf{THR}$-SAT in $2^{n-n^{\delta}}$ for circuits of size $2^{n^{\delta}}$; $\\#\mathsf{ACC}^0$-SAT (counting) in the same time.

## 5. Principal Obstacles

- **Composite moduli break algebra.** Over $\mathbb{Z}/6\mathbb{Z}$ there are degree-$O(\sqrt{n})$ "$\mathsf{MOD}_6$-representing" polynomials for $\mathsf{OR}_n$ (Barrington–Beigel–Rudich), so no rank/degree argument of Smolensky type can separate. The multiplicative structure of $\mathbb{Z}/m\mathbb{Z}$ for composite $m$ admits zero divisors and no useful notion of "few roots".
- **Natural proofs.** If $\mathsf{ACC}^0$ contains pseudorandom function families secure against $2^{n^{\varepsilon}}$-time adversaries, no *constructive + large* combinatorial property can prove the lower bound. This is not known for $\mathsf{ACC}^0$, but it is known for $\mathsf{TC}^0$ under standard assumptions, which blocks the natural route upward.
- **The algorithmic method is non-constructive.** Williams' proof yields no explicit hard function: it argues by contradiction with the nondeterministic time hierarchy. Extracting an explicit witness would need a constructive easy-witness lemma.
- **Speedup budget.** The method needs SAT algorithms saving a superpolynomial factor over $2^n$ for circuits of size $2^{n^{o(1)}}$. For $\mathsf{TC}^0$ or general $\mathsf{P/poly}$, no such algorithm is known; for $\mathsf{ACC}^0$ the saving $2^{n-n^\delta}$ has $\delta \to 0$ as depth grows, which is exactly why the result does not scale down to $\mathsf{NP}$.
- **Relativization of the method.** Vyas–Williams exhibit oracles under which the algorithmic-method implication (nontrivial SAT algorithm $\Rightarrow$ lower bound) fails in certain formalizations, showing the framework needs non-relativizing ingredients beyond those already used.

## 6. The Gap

Proven (Section 4): a *nondeterministic* class with quasipolynomial or larger time is not in $\mathsf{ACC}^0$, non-constructively. Wanted (Section 1): an explicit function in $\mathsf{NP}$, or even a deterministic class like $\mathsf{EXP}$, outside $\mathsf{ACC}^0$.

The exact step is quantitative. To get $\mathsf{NP} \not\subseteq \mathsf{ACC}^0$ from the algorithmic method one needs $\mathsf{ACC}^0$-SAT (or a suitable gap-UNSAT/derandomization task) in time $2^{n}/2^{n^{\Omega(1)}}$ *uniformly in the depth $d$* — i.e. a saving $\delta$ that does not degrade as $d$ grows — together with an easy-witness lemma for $\mathsf{NTIME}[n^k]$ with $k$ fixed. Present depth reduction costs $2^{(\log s)^{O(d)}}$, and this tower-in-$d$ blowup is the barrier: it forces $\delta = \delta(d) \to 0$. Removing nondeterminism entirely (getting $\mathsf{EXP} \not\subseteq \mathsf{ACC}^0$) requires replacing the nondeterministic hierarchy step, for which no substitute is known.

## 7. Current Research (as of June 2026)

- **Derandomization-to-lower-bounds pipeline (MIT, Tsinghua/IIIS, Berkeley).** Chen, Ren, Lyu, Williams: nontrivial derandomization of $\mathsf{CAPP}$ (circuit acceptance probability problem) for a class $\mathcal{C}$ yields average-case and almost-everywhere lower bounds against $\mathcal{C}$. Current frontier: strengthening the $1/2 + 1/\mathrm{polylog}$ correlation bound for $\mathsf{ACC}^0$ toward $1/2 + 2^{-n^{\Omega(1)}}$ *(frontier — verify)*.
- **Improved depth reduction.** Attempts to replace the $2^{\log^{O(d)} s}$ blowup with $2^{\tilde O(\log s \cdot d)}$; a depth-independent reduction would immediately push the lower bound toward $\mathsf{NP}$ *(frontier — verify)*.
- **Beyond $\mathsf{ACC}^0$.** Lower bounds against $\mathsf{ACC}^0 \circ \mathsf{THR}$ and small-depth threshold circuits; connections to matrix rigidity (Alman–Chen; Chen–Lyu) where $\mathsf{ACC}^0$-flavored techniques produce explicit rigid matrices.
- **Barriers.** Vyas–Williams-style oracle separations for algorithmic methods; ongoing work on whether $\mathsf{ACC}^0$ supports pseudorandom functions, which would impose a natural-proofs barrier where none is currently proven.
- **Constructivity.** Search for a constructive easy-witness lemma that would name an explicit hard function rather than argue by hierarchy contradiction.

## 8. Future Work

- Prove $\mathsf{EXP} \not\subseteq \mathsf{ACC}^0$ by finding a deterministic substitute for the nondeterministic-hierarchy step (Williams' stated target).
- Obtain a depth-uniform $\mathsf{ACC}^0$-SAT algorithm with saving $2^{n^{\delta}}$, $\delta$ independent of $d$.
- Settle $\mathsf{ACC}^0$ vs $\mathsf{TC}^0$: either place $\mathsf{MAJORITY}$ in $\mathsf{ACC}^0$ (which would be a major upper-bound surprise) or separate.
- Design a nontrivial $\\#\mathsf{SAT}$ or $\mathsf{CAPP}$ algorithm for depth-2 threshold circuits $\mathsf{THR}\circ\mathsf{THR}$, the smallest class where the method currently stalls.
- Determine whether pseudorandom functions exist in $\mathsf{ACC}^0$, resolving whether a natural-proofs barrier applies here at all.

## 9. Key References

- **[Foundational]** A. A. Razborov. *Lower bounds on the size of bounded depth circuits over a complete basis with logical addition.* Matematicheskie Zametki 41(4):598–607, 1987.
- **[Foundational]** R. Smolensky. *Algebraic methods in the theory of lower bounds for Boolean circuit complexity.* STOC 1987, 77–82.
- **[Foundational]** A. C.-C. Yao. *On ACC and threshold circuits.* FOCS 1990, 619–627.
- **[Foundational]** R. Beigel, J. Tarui. *On ACC.* Computational Complexity 4(4):350–366, 1994.
- **[Foundational]** R. Impagliazzo, V. Kabanets, A. Wigderson. *In search of an easy witness: exponential time vs. probabilistic polynomial time.* Journal of Computer and System Sciences 65(4):672–694, 2002.
- **[Foundational]** A. A. Razborov, S. Rudich. *Natural proofs.* Journal of Computer and System Sciences 55(1):24–35, 1997.
- **[SOTA]** R. Williams. *Improving exhaustive search implies superpolynomial lower bounds.* STOC 2010; SIAM Journal on Computing 42(3):1218–1244, 2013.
- **[SOTA]** R. Williams. *Non-uniform ACC circuit lower bounds.* CCC 2011; Journal of the ACM 61(1), Article 2, 2014.
- **[SOTA]** R. Williams. *New algorithms and lower bounds for circuits with linear threshold gates.* STOC 2014; Theory of Computing 14(17), 2018.
- **[SOTA]** S. Chen, P. A. Papakonstantinou. *Depth reduction for composites.* FOCS 2016; SIAM Journal on Computing 48(2), 2019.
- **[SOTA]** C. D. Murray, R. R. Williams. *Circuit lower bounds for nondeterministic quasi-polytime: an easy witness lemma for NP and NQP.* STOC 2018; SIAM Journal on Computing 49(5), 2020.
- **[SOTA]** L. Chen, H. Ren. *Strong average-case circuit lower bounds from nontrivial derandomization.* STOC 2020.
- **[SOTA]** L. Chen, X. Lyu, R. R. Williams. *Almost-everywhere circuit lower bounds from non-trivial derandomization.* FOCS 2020.
- **[Recent]** N. Vyas, R. Williams. *On oracles and algorithmic methods for proving lower bounds.* ITCS 2023.
- **[Survey]** I. C. Oliveira. *Algorithms versus circuit lower bounds.* ECCC Technical Report TR13-117, 2013.
- **[Survey]** D. A. M. Barrington. *Bounded-width polynomial-size branching programs recognize exactly those languages in NC¹.* Journal of Computer and System Sciences 38(1):150–164, 1989.

## 10. Worked Example / Concrete Special Case

**Goal:** convert a small $\mathsf{ACC}^0$ circuit into $\mathsf{SYM}\circ\mathsf{AND}$ form and count its satisfying assignments — the two moves at the heart of Williams' SAT algorithm.

Take $n=4$ and $C(x) = \mathsf{MOD}_3(x_1,x_2,x_3,x_4)$, i.e. $C(x)=1 \iff s \equiv 0 \pmod 3$ where $s=\sum_i x_i$.

*Step 1 — arithmetize over $\mathbb{F}_3$.* Since $a^2 = 0$ in $\mathbb{F}_3$ iff $a=0$, set
$$p(x) = 1 - \left(\sum_{i=1}^{4} x_i\right)^{2} \pmod 3 .$$
Check: $s=0 \Rightarrow p=1$; $s=1 \Rightarrow 1-1=0$; $s=2 \Rightarrow 1-4=1-1=0$; $s=3 \Rightarrow 1-9=1-0=1$; $s=4 \Rightarrow 1-16=1-1=0$. So $p = C$ exactly.

*Step 2 — expand to $\mathsf{SYM}\circ\mathsf{AND}$.* With $x_i^2 = x_i$ over Booleans,
$$\left(\sum_i x_i\right)^2 = \sum_i x_i + 2\sum_{i<j} x_i x_j,$$
hence over $\mathbb{F}_3$
$$p(x) = 1 + 2\sum_{i=1}^{4} x_i + \sum_{1 \le i < j \le 4} x_i x_j .$$
The right-hand side is a sum of $4 + \binom{4}{2} = 10$ $\mathsf{AND}$ gates of fan-in $\le 2$, fed into a top gate that depends only on the integer sum of its inputs and outputs $1$ exactly when that sum $\equiv -1 \equiv 2 \pmod 3$ (so that $1+\text{sum}\equiv 0$... precisely: the top table $g(t)=1 \iff 1 + t \equiv 1 \pmod 3$, taking the weighted sum $t = 2e_1 + e_2$ formed by duplicating the four fan-in-1 gates). This is the Beigel–Tarui normal form, here with $S=10$ instead of $2^{(\log s)^{O(d)}}$.

*Step 3 — count satisfying assignments symmetrically.* Because $g$ sees only $t$, and $t$ is determined by $s$, we need only the weight distribution:
$$\\#\{x : C(x)=1\} = \binom{4}{0} + \binom{4}{3} = 1 + 4 = 5,$$
computed in $O(n)$ arithmetic operations rather than $2^4=16$ evaluations.

*What this illustrates.* For a general depth-$d$ $\mathsf{ACC}^0$ circuit, Step 2 produces $S = 2^{(\log s)^{O(d)}}$ terms rather than $10$, and Step 3 is replaced by evaluating the $\mathsf{SYM}\circ\mathsf{AND}$ form at all $2^{k}$ settings of $k = n^{\delta}$ variables at once via fast rectangular matrix multiplication, giving total time $2^{n-\Omega(n^{\delta})}$. That saving, fed into the algorithmic method, yields $\mathsf{NEXP}\not\subseteq\mathsf{ACC}^0$. The $O(d)$ in the exponent of $S$ is precisely what forces $\delta = \delta(d) \to 0$ and blocks the descent to $\mathsf{NP}$.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*