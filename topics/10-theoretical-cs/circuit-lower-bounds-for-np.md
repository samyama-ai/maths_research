---
id: 10-theoretical-cs/circuit-lower-bounds-for-np
title: "Circuit Lower Bounds for NP"
topic: 10-theoretical-cs
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Circuit Lower Bounds for NP

> **Topic:** Theoretical Computer Science · **ID:** `10-theoretical-cs/circuit-lower-bounds-for-np` · **Status:** open

## 1. Problem Statement / Conjecture

Prove that some language in $\mathsf{NP}$ requires Boolean circuits of superpolynomial size. Formally:

$$\mathsf{NP} \not\subseteq \mathsf{P/poly}.$$

Equivalently: exhibit an explicit family $\{f_n\}$, $f_n:\{0,1\}^n\to\{0,1\}$, decidable in nondeterministic polynomial time, such that its circuit complexity $C(f_n)$ over the full binary basis is not bounded by any polynomial.

A complete solution requires either (i) a proof of the separation, or (ii) a proof that $\mathsf{NP}\subseteq \mathsf{P/poly}$ — which by Karp–Lipton would collapse the polynomial hierarchy to $\Sigma_2^p$ (sharpened to $\mathsf{S}_2^p$ by Cai). The conjecture is strictly stronger than $\mathsf{P}\neq\mathsf{NP}$: nonuniform circuits may decide undecidable unary languages, so $\mathsf{P}\neq\mathsf{NP}$ does not formally imply it.

The catalog status is **open**, and dramatically so: the best unconditional lower bound for any explicit function is *linear*, roughly $3.01n$.

## 2. Mathematical Foundations

**Circuits.** A Boolean circuit over basis $\Omega$ is a finite DAG whose sources are labelled $x_1,\dots,x_n$ (or constants), whose internal nodes (gates) are labelled by functions in $\Omega$ with fan-in matching arity, and with one designated output. Size $|C|$ = number of gates; depth = longest source-to-sink path. Standard bases:

- $B_2$ = all $16$ binary functions;
- $U_2 = B_2\setminus\{\oplus,\equiv\}$ (De Morgan basis with free negations);
- monotone basis $\{\wedge,\vee\}$.

Write $C_\Omega(f)$ for the minimum size. Define
$$\mathsf{SIZE}(s(n)) = \{L : \exists\ \text{circuits } C_n,\ |C_n|\le s(n),\ C_n(x)=[x\in L]\},\qquad \mathsf{P/poly}=\bigcup_{k}\mathsf{SIZE}(n^k).$$

**Counting bound (Shannon 1949; Lupanov 1958).** Almost every $f:\{0,1\}^n\to\{0,1\}$ satisfies
$$C_{B_2}(f) \ge \frac{2^n}{n}(1+o(1)), \qquad \text{and every } f \text{ satisfies } C_{B_2}(f)\le \frac{2^n}{n}\Big(1+\frac{3\log n}{n}\Big).$$
So hard functions are abundant; the difficulty is *explicitness*.

**Bounded depth.** $\mathsf{AC}^0$ = poly-size, constant-depth, unbounded fan-in $\{\wedge,\vee,\neg\}$; $\mathsf{AC}^0[m]$ adds $\mathrm{MOD}_m$ gates; $\mathsf{ACC}^0=\bigcup_m \mathsf{AC}^0[m]$; $\mathsf{NC}^1$ = log-depth fan-in-2, equivalently poly-size formulas.

**Karp–Lipton (1980).**
$$\mathsf{NP}\subseteq\mathsf{P/poly}\ \Longrightarrow\ \mathsf{PH}=\Sigma_2^p.$$

**Natural proofs (Razborov–Rudich).** A combinatorial property $\mathcal{P}_n\subseteq\{f:\{0,1\}^n\to\{0,1\}\}$ is *natural* against $\mathsf{SIZE}(s)$ if it is
- *constructive*: membership decidable in time $2^{O(n)}$ in the truth table;
- *large*: $\Pr_f[f\in\mathcal{P}_n]\ge 2^{-O(n)}$;
- *useful*: $f\in\mathcal{P}_n\Rightarrow C(f)>s(n)$.

**Theorem.** If subexponentially strong pseudorandom generators exist, no natural property is useful against $\mathsf{SIZE}(2^{n^{\varepsilon}})$.

## 3. History & State of the Art (SOTA)

- **1949.** Shannon's counting argument establishes $2^n/n$ hardness for random functions.
- **1966.** Nečiporuk's method yields $\Omega(n^2/\log n)$ formula size over $B_2$ — still the record for general formulas.
- **1984.** Blum: $3n-o(n)$ circuit size over $B_2$ for an explicit function, by *gate elimination*.
- **1985–87.** Razborov: superpolynomial monotone lower bound for CLIQUE via the approximation method; Alon–Boppana strengthen it to exponential. Razborov shows monotone lower bounds do **not** transfer: matching, in $\mathsf{P}$, needs $n^{\Omega(\log n)}$ monotone size.
- **1986–87.** Håstad's switching lemma gives $2^{\Omega(n^{1/(d-1)})}$ for parity in depth-$d$ $\mathsf{AC}^0$; Razborov and Smolensky give the polynomial method for $\mathsf{AC}^0[p]$, $p$ prime.
- **1994.** Razborov–Rudich: the natural proofs barrier explains why progress stalled at $\mathsf{AC}^0[p]$.
- **2002–2016.** $U_2$ bound pushed to $5n-o(n)$ (Iwama–Morizumi); $B_2$ bound to $(3+\tfrac{1}{86})n-o(n)$ (Find–Golovnev–Hirsch–Kulikov), for affine dispersers.
- **2011.** Williams: $\mathsf{NEXP}\not\subseteq\mathsf{ACC}^0$ via the *algorithmic method* — a $2^{n-n^{\delta}}$-time $\\#\mathsf{SAT}$ algorithm for $\mathsf{ACC}^0$ circuits (Beigel–Tarui normal form) plus the easy witness lemma.
- **2018.** Murray–Williams push this to $\mathsf{NQP}=\mathsf{NTIME}[n^{\mathrm{polylog}\,n}]\not\subseteq\mathsf{ACC}^0$.
- **2024.** Li (and concurrently Chen–Hirahara–Ren) show $\mathsf{S}_2\mathsf{E}$ requires circuits of size $2^n/n$ — near-maximum hardness for a class just above $\mathsf{NP}$-like levels, but far above $\mathsf{NP}$ itself.

## 4. Partial Results / Verified Cases

| Setting | Bound | Source |
|---|---|---|
| General $B_2$, explicit $f\in\mathsf{P}$ | $(3+\tfrac{1}{86})n - o(n)$ | Find–Golovnev–Hirsch–Kulikov 2016 |
| $U_2$ basis | $5n - o(n)$ | Iwama–Morizumi 2002 |
| De Morgan formulas | $n^{3-o(1)}$, precisely $\Omega(n^3/(\log^2 n\log\log n))$ for Andreev's function | Håstad 1998; Tal 2014 |
| Formulas over $B_2$ | $\Omega(n^2/\log n)$ | Nečiporuk 1966 |
| Monotone circuits, $\mathrm{CLIQUE}_{k,n}\in\mathsf{NP}$ | $n^{\Omega(\sqrt{k})}$; $2^{\Omega(\sqrt{k})}$ for $k\le n^{2/3}$ | Razborov 1985; Alon–Boppana 1987 |
| Depth-$d$ $\mathsf{AC}^0$, parity | $2^{\Omega(n^{1/(d-1)})}$ | Håstad 1986 |
| $\mathsf{AC}^0[p]$, $p$ prime: $\mathrm{MOD}_q$, $q\neq p^k$ | $2^{\Omega(n^{1/2d})}$ | Razborov 1987; Smolensky 1987 |
| $\mathsf{ACC}^0$ | $\mathsf{NQP}\not\subseteq\mathsf{ACC}^0$ | Williams 2011; Murray–Williams 2018 |
| $k$-clique in $\mathsf{AC}^0$ | $n^{\Omega(k)}$ monotone depth-$d$ | Rossman 2008 |
| $\mathsf{S}_2\mathsf{E}$ | $2^n/n$ | Li 2024 |

For $\mathsf{NP}$ specifically: $\mathsf{NP}\not\subseteq\mathsf{mSIZE}(\mathrm{poly})$ is *proved* (CLIQUE, monotone), and $\mathsf{NP}\not\subseteq\mathsf{ACC}^0$ is **not** — even $\mathsf{NP}\not\subseteq\mathsf{AC}^0[6]$ is open.

## 5. Principal Obstacles

- **Gate elimination saturates.** The technique restricts a variable, argues that $\ge c$ gates die, and recurses. Because each restriction destroys one variable and only a bounded number of gates, it cannot beat $O(n)$; a $5n$-type case analysis already runs to hundreds of cases and yields $+\tfrac{1}{86}$ per improvement. There is a formal obstruction: gate elimination arguments are captured by simple "measure" frameworks whose value is $O(n)$.
- **Natural proofs.** Restriction/approximation/polynomial arguments all give properties that are constructive and large. Under standard cryptographic assumptions (subexponential hardness of factoring or discrete log) no such property can prove superpolynomial bounds. Any proof must be non-constructive (like diagonalization/algorithmic method) or non-large (a property shared by almost no random function).
- **Relativization** (Baker–Gill–Solovay 1975): there exist oracles $A,B$ with $\mathsf{P}^A=\mathsf{NP}^A$ and $\mathsf{P}^B\ne\mathsf{NP}^B$; purely simulation-based arguments cannot separate.
- **Algebrization** (Aaronson–Wigderson 2009): even arithmetization-based techniques (IP=PSPACE, Williams-style algebraic tricks) fail; separating $\mathsf{NP}$ from $\mathsf{P/poly}$ requires non-algebrizing methods.
- **Monotone $\ne$ general.** Razborov's own matching bound shows monotone hardness has no implication for general circuits, so the one superpolynomial $\mathsf{NP}$ bound we own is a dead end for the general question.
- **Algebraic degree collapse.** The Razborov–Smolensky polynomial method needs a field over which the gate set has low-degree approximants; $\mathrm{MOD}_6$ gates have no such representation over any single field, blocking the extension to $\mathsf{ACC}^0$ and beyond.

## 6. The Gap

Proved: $C_{B_2}(f)\ge 3.01n$ for explicit $f$. Wanted: $C_{B_2}(f)\ge n^{\omega(1)}$. The gap is not quantitative refinement — it is the absence of any technique that produces a *superlinear* bound for general circuits, for any explicit function whatsoever, including functions in $\mathsf{EXP}$ or $\mathsf{PSPACE}$.

The nearest crossing point is the algorithmic method. Williams' theorem states: if $\mathsf{CircuitSAT}$ for general fan-in-2 circuits of size $2^{o(n)}$ can be solved in time $2^n/n^{\omega(1)}$, then $\mathsf{NEXP}\not\subseteq\mathsf{P/poly}$. So a *nontrivially faster-than-brute-force satisfiability algorithm* for unrestricted circuits is a sufficient step — but even $\mathsf{NEXP}$ is far above $\mathsf{NP}$, and scaling the conclusion down to $\mathsf{NP}$ requires much stronger, currently unavailable, "witness compression" machinery.

## 7. Current Research (as of June 2026)

- **Algorithmic method scaling.** Chen, Ren, Williams, Murray and collaborators (MIT, Oxford, Berkeley, Tsinghua) continue to trade circuit class for complexity class: almost-everywhere lower bounds, lower bounds against $\mathsf{ACC}^0\circ\mathsf{THR}$, and against $\mathsf{ACC}^0$ for classes below $\mathsf{NQP}$.
- **Range avoidance / Remote Point.** The $\mathsf{Avoid}$ problem (given a circuit $C:\{0,1\}^n\to\{0,1\}^{n+1}$, output a non-image string) drove the 2024 $\mathsf{S}_2\mathsf{E}$ near-maximum bounds; extending the technique downward toward $\Sigma_2\mathsf{P}$/$\mathsf{NP}$ is the most active frontier. *(frontier — verify)*
- **Hardness magnification.** Oliveira–Santhanam, Chen–Jin–Williams: an $n^{1+\varepsilon}$ lower bound for gap-MCSP or sparse $\mathsf{NP}$ languages on formulas/branching programs would imply $\mathsf{NP}\not\subseteq\mathsf{NC}^1$ or worse. This relocates the problem to *barely superlinear* bounds — but such bounds themselves seem to hit a "locality barrier".
- **Proof complexity of lower bounds.** Pich, Müller, Krajíček (Oxford, Prague): whether bounded arithmetic theories such as $\mathsf{APC}_1$ can prove $\mathsf{NP}\not\subseteq\mathsf{P/poly}$; several unprovability results are known for weak theories.
- **Meta-complexity.** MCSP/Kolmogorov-complexity-based reformulations (Hirahara, Santhanam, Ilango) connect average-case $\mathsf{NP}$-hardness to lower bounds.

## 8. Future Work

- Construct a *non-natural* useful property: one violating largeness (holds for a $2^{-\omega(n)}$ fraction of functions), e.g. a property tied to a specific algebraic invariant of $\mathsf{SAT}$.
- Find a $2^n/n^{\omega(1)}$ algorithm for general $\mathsf{CircuitSAT}$, or prove such an algorithm impossible (SETH-style).
- Push range-avoidance results from $\mathsf{S}_2\mathsf{E}$ down to $\Sigma_2\mathsf{E}$ and then to subexponential-time analogues.
- Break the $n^{1+\varepsilon}$ magnification threshold for a sparse $\mathsf{NP}$ language, evading the locality barrier.
- Develop non-algebrizing arithmetization, e.g. via multilinear or tensor-rank invariants (a $\Omega(n^{1+\varepsilon})$ tensor rank bound would already be a breakthrough).

## 9. Key References

- **[Foundational]** C. E. Shannon. *The Synthesis of Two-Terminal Switching Circuits.* Bell System Technical Journal 28(1), 1949.
- **[Foundational]** R. M. Karp, R. J. Lipton. *Some Connections Between Nonuniform and Uniform Complexity Classes.* STOC 1980.
- **[Foundational]** N. Blum. *A Boolean Function Requiring 3n Network Size.* Theoretical Computer Science 28, 1984.
- **[Foundational]** A. A. Razborov. *Lower Bounds on the Monotone Complexity of Some Boolean Functions.* Soviet Mathematics Doklady 31, 1985.
- **[Foundational]** N. Alon, R. B. Boppana. *The Monotone Circuit Complexity of Boolean Functions.* Combinatorica 7(1), 1987.
- **[Foundational]** J. Håstad. *Almost Optimal Lower Bounds for Small Depth Circuits.* STOC 1986.
- **[Foundational]** R. Smolensky. *Algebraic Methods in the Theory of Lower Bounds for Boolean Circuit Complexity.* STOC 1987.
- **[Barrier]** T. Baker, J. Gill, R. Solovay. *Relativizations of the P =? NP Question.* SIAM Journal on Computing 4(4), 1975.
- **[Barrier]** A. A. Razborov, S. Rudich. *Natural Proofs.* Journal of Computer and System Sciences 55(1), 1997.
- **[Barrier]** S. Aaronson, A. Wigderson. *Algebrization: A New Barrier in Complexity Theory.* ACM Transactions on Computation Theory 1(1), 2009.
- **[SOTA]** R. Williams. *Nonuniform ACC Circuit Lower Bounds.* Journal of the ACM 61(1), 2014.
- **[SOTA]** C. D. Murray, R. R. Williams. *Circuit Lower Bounds for Nondeterministic Quasi-Polytime: An Easy Witness Lemma for NP and NQP.* STOC 2018.
- **[SOTA]** M. Find, A. Golovnev, E. A. Hirsch, A. S. Kulikov. *A Better-than-3n Lower Bound for the Circuit Complexity of an Explicit Function.* FOCS 2016.
- **[SOTA]** A. Tal. *Shrinkage of De Morgan Formulae by Spectral Techniques.* FOCS 2014.
- **[SOTA]** Z. Li. *Symmetric Exponential Time Requires Near-Maximum Circuit Complexity.* STOC 2024.
- **[SOTA]** I. C. Oliveira, R. Santhanam. *Hardness Magnification for Natural Problems.* FOCS 2018.
- **[Survey]** S. Jukna. *Boolean Function Complexity: Advances and Frontiers.* Springer, 2012.
- **[Survey]** S. Arora, B. Barak. *Computational Complexity: A Modern Approach.* Cambridge University Press, 2009.

## 10. Worked Example / Concrete Special Case

**Claim.** $C_{U_2}(\oplus_n) = 3(n-1)$ for $n\ge 1$, where $\oplus_n(x)=x_1\oplus\cdots\oplus x_n$ and $U_2=B_2\setminus\{\oplus,\equiv\}$.

*Upper bound.* One XOR from two $U_2$ gates plus an OR: $a\oplus b=(a\wedge\bar b)\vee(\bar a\wedge b)$ costs 3 gates. Chaining $n-1$ XORs gives $3(n-1)$. For $n=2$: 3 gates.

*Lower bound (gate elimination).* Induct on $n$. Base $n=1$: $0$ gates. Let $C$ be an optimal $U_2$-circuit for $\oplus_n$, $n\ge 2$.

1. $\oplus_n$ depends on all variables, so $C$ has a gate $g$ both of whose inputs are (possibly negated) variables $x_i,x_j$, $i\ne j$. Since $g\in U_2$, $g = (x_i^{a}\wedge x_j^{b})$ up to output negation, for constants $a,b\in\{0,1\}$ where $x^1=x, x^0=\bar x$.
2. Substitute $x_i := \bar a$ (i.e. the value making the first literal $0$). Then $g$ becomes constant.
3. Every gate $h$ fed by $g$ becomes a function of one remaining input, so $h$ is a constant or a literal — $h$ is eliminated too.
4. Key point: $g$ must have out-degree $\ge 2$. If $g$ had out-degree 1 with successor $h$, then after setting $x_j$ to a suitable constant the subcircuit on $\{x_i\}$ would make $C|_{x_j=c}$ independent of $x_i$ — contradicting that $\oplus_{n-1}$ depends on $x_i$. Hence steps 2–3 kill $g$ plus at least 2 successors: **3 gates**.
5. The restricted circuit computes $\oplus_{n-1}$ (up to negation) on $n-1$ variables, so
$$|C| \ge 3 + C_{U_2}(\oplus_{n-1}) \ge 3 + 3(n-2) = 3(n-1).$$

**Why this is the whole difficulty.** The recursion removes one variable and charges exactly 3 gates, so the method is capped at $3n$ — and refinements with heavier measures reach only $(3+\tfrac{1}{86})n$. Parity is in $\mathsf{P}$ and is *easy* ($3n$ gates suffice); yet no technique proves more than a constant times $n$ for any $\mathsf{NP}$ function either. The distance from this $3(n-1)$ calculation to $n^{\omega(1)}$ is the entire open problem.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*