---
id: 10-theoretical-cs/skolem-problem
title: "Skolem Problem"
topic: 10-theoretical-cs
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Skolem Problem

> **Topic:** Theoretical Computer Science · **ID:** `10-theoretical-cs/skolem-problem` · **Status:** open

## 1. Problem Statement / Conjecture

**Skolem Problem.** Given an integer linear recurrence sequence (LRS) $(u_n)_{n\ge 0}$ specified by its order $k$, integer coefficients $a_1,\dots,a_k$ and integer initial values $u_0,\dots,u_{k-1}$, with
$$u_{n+k} = a_1 u_{n+k-1} + a_2 u_{n+k-2} + \cdots + a_k u_n \qquad (n \ge 0),$$
decide whether there exists $n \in \mathbb{N}$ with $u_n = 0$.

The decision procedure must be *uniform and effective*: an algorithm taking the finite data $(a_1,\dots,a_k,u_0,\dots,u_{k-1})$ in binary and halting with a correct yes/no answer. It is **not known whether such an algorithm exists**; the problem has been open since the 1930s. Terence Tao and others describe it as the outstanding effectivity gap left by the Skolem–Mahler–Lech theorem.

A resolution requires either (a) an algorithm with a proof of total correctness and termination, or (b) a reduction from a problem already known to be undecidable (e.g. Hilbert's tenth problem or the halting problem). Closely related and equally open are the **Positivity Problem** ($u_n \ge 0$ for all $n$?) and the **Ultimate Positivity Problem** ($u_n \ge 0$ for all sufficiently large $n$?).

## 2. Mathematical Foundations

**Exponential polynomial form.** Let $\chi(x) = x^k - a_1x^{k-1} - \cdots - a_k$ be the characteristic polynomial, with distinct roots $\lambda_1,\dots,\lambda_m \in \overline{\mathbb{Q}}^\times$ (assume $a_k \ne 0$) of multiplicities $m_1,\dots,m_m$. Then there are polynomials $P_j \in \overline{\mathbb{Q}}[x]$, $\deg P_j < m_j$, with
$$u_n = \sum_{j=1}^{m} P_j(n)\,\lambda_j^{\,n}.$$
The LRS is **simple** if all $\lambda_j$ are simple ($m_j = 1$), so $u_n = \sum_j c_j \lambda_j^n$. It is **non-degenerate** if no ratio $\lambda_i/\lambda_j$ ($i\ne j$) is a root of unity.

**Zero set.** Write $\mathcal{Z}(u) = \{n \in \mathbb{N} : u_n = 0\}$.

**Theorem (Skolem 1934; Mahler 1935; Lech 1953).** For an LRS over a field of characteristic $0$, $\mathcal{Z}(u)$ is the union of a finite set and finitely many infinite arithmetic progressions. Equivalently, if $(u_n)$ is non-degenerate and not identically zero, $\mathcal{Z}(u)$ is finite.

The proof is $p$-adic: for a suitable prime $p$ of good reduction and suitable $r$, each root satisfies $\lambda_j^{\,r} \in 1 + p\mathbb{Z}_p$, so on the residue class $n \equiv \ell \pmod r$ the map
$$t \;\longmapsto\; u_{rt+\ell} \;=\; \sum_j c_j \lambda_j^{\ell}\exp_p\!\big(t \log_p \lambda_j^{\,r}\big)$$
extends to an analytic function $\mathbb{Z}_p \to \mathbb{Q}_p$. By Strassmann's theorem such a function is either identically zero or has finitely many zeros in $\mathbb{Z}_p$ — bounded by the number of coefficients of small valuation.

**Why this is ineffective.** Strassmann bounds the *number* of zeros, not their *magnitude*. Nothing in the argument bounds $\max \mathcal{Z}(u)$ in terms of the input, so one cannot turn "finitely many zeros" into a search that terminates.

**Skolem Conjecture (exponential local–global principle, Skolem 1937).** If an exponential Diophantine equation $\sum_j c_j\lambda_j^n = 0$ has no solution $n\in\mathbb{Z}$, then it has no solution modulo $m$ for some modulus $m$. Under this conjecture the naive semi-algorithm — search for a zero, and in parallel search for a modulus $m$ with $u_n \not\equiv 0 \pmod m$ for all $n$ — terminates.

**Matrix form.** Equivalently: given $M \in \mathbb{Z}^{k\times k}$ and $u,v\in\mathbb{Z}^k$, decide whether $u^{\mathsf T}M^n v = 0$ for some $n$. This is the entry-reachability form used in verification.

## 3. History & State of the Art (SOTA)

- **1934–1953.** Skolem proves the finiteness result over $\mathbb{Q}$; Mahler extends it to algebraic number fields (1935) and to fields of characteristic $0$ (1956); Lech (1953) gives the general characteristic-zero statement. All proofs are ineffective.
- **1976.** Berstel and Mignotte show the *arithmetic-progression* part of $\mathcal{Z}(u)$ is effectively computable: one can compute $L \le 2^k\,k!\,\cdot$(explicit bound) such that the degenerate structure is exposed by splitting $n$ into residues mod $L$. This reduces the Skolem Problem to the non-degenerate case.
- **1984–1985.** Mignotte–Shorey–Tijdeman (via Baker's theorem on linear forms in logarithms) and independently Vereshchagin settle **order $k \le 4$**.
- **2002.** Blondel and Portier prove the Skolem Problem is **NP-hard**, by encoding subset-sum in the zeros of an LRS built from products of cyclotomic-like factors. No decidability upper bound is known, so the problem is not known to lie in any complexity class.
- **2007–2012.** Derksen gives a Skolem–Mahler–Lech theorem in positive characteristic (the zero set is $p$-automatic); Derksen and Masser make it **effective** in characteristic $p$ — a sharp contrast with characteristic $0$.
- **2012–2014.** Ouaknine and Worrell reframe the area for verification: Positivity for order $\ge 6$ would yield major new results in Diophantine approximation (computing the homogeneous approximation type of a vector of algebraic numbers), and Ultimate Positivity is decidable for simple LRS.
- **2021–2024.** The "Universal Skolem set" programme (Luca–Ouaknine–Worrell) and the conditional-decidability programme (*Skolem meets Schanuel*; *On the Skolem Problem and the Skolem Conjecture*) give algorithms that are correct assuming standard number-theoretic conjectures, plus the practical **Skolem tool**, which decides most instances arising in practice.

## 4. Partial Results / Verified Cases

| Class | Status |
|---|---|
| Order $k \le 3$ | Decidable (Mignotte–Shorey–Tijdeman 1984) |
| Order $k = 4$ | Decidable (Vereshchagin 1985; MST 1984 for the main subcases) |
| Order $k \ge 5$ | **Open**, including simple LRS of order $5$ |
| Degenerate part of $\mathcal{Z}(u)$, any $k$ | Effectively computable (Berstel–Mignotte 1976) |
| LRS with a *dominant* root ($|\lambda_1| > |\lambda_j|$ for $j\ge2$) | Decidable: $|u_n| \ge \tfrac12|c_1||\lambda_1|^n$ for $n$ past an effective threshold from Baker's theorem |
| Simple LRS whose roots have pairwise distinct moduli | Decidable by the same dominance/Baker argument applied inductively |
| "Reversible" LRS (characteristic polynomial with unit constant term, roots algebraic units) of low order | Decidable subject to the Skolem Conjecture (Lipton–Luca–Nieuwveld–Ouaknine–Purser–Worrell, LICS 2022) |
| Simple LRS, arbitrary order | Decidable **conditionally** on the Skolem Conjecture and the $p$-adic Schanuel conjecture (Bilu–Luca–Nieuwveld–Ouaknine–Purser–Worrell, MFCS 2022) |
| Positive characteristic $p$ | Fully effective (Derksen 2007; Derksen–Masser 2012) |
| Universal Skolem sets | There is an effectively computable $\mathcal{S}\subseteq\mathbb{N}$ of positive lower density such that for every non-degenerate LRS, $\mathcal{Z}(u)\cap\mathcal{S}$ is effectively computable (Luca–Maynard–Noubissie–Ouaknine–Worrell, MFCS 2022) |

Computationally, the Skolem tool resolves essentially all randomly generated and benchmark instances of order up to roughly $20$ *(frontier — verify)*, but its termination proof is conditional.

## 5. Principal Obstacles

- **Ineffectivity of the $p$-adic method.** Strassmann's theorem counts zeros of a $p$-adic analytic function but gives no bound on where they lie in $\mathbb{Z}_p$, and the archimedean size of a zero is invisible to the $p$-adic argument. There is no known mechanism converting a $p$-adic count into an archimedean search bound.
- **Baker's theorem stops at equal moduli.** The effective route bounds $|u_n|$ from below by isolating a dominant term; linear forms in logarithms give $\big|\,n\log|\lambda_1| - n\log|\lambda_2|\,\big|$-type lower bounds only when the logarithms are non-trivially independent. When two or more root moduli **coincide**, the dominant terms oscillate: $u_n$ behaves like $\rho^n\big(A\cos(n\theta_1+\varphi_1)+B\cos(n\theta_2+\varphi_2)\big)$, and a zero is a solution of a *simultaneous inhomogeneous* Diophantine approximation problem in the angles $\theta_1,\theta_2$. Baker's theorem yields no effective lower bound for such forms.
- **Hardness transfer.** Ouaknine and Worrell showed that deciding Positivity at order $\ge 6$ entails computing homogeneous Diophantine approximation types for vectors of algebraic numbers — a task considered out of reach. This is a *mathematical* hardness barrier, not a complexity-theoretic one: it says a decision procedure would carry new number theory with it.
- **No undecidability leverage.** The Skolem–Mahler–Lech structure theorem forces $\mathcal{Z}(u)$ to be extremely simple (finite $\cup$ finitely many progressions), so no rich computation can be encoded in the zero set. Standard undecidability reductions therefore fail; only NP-hardness is available.
- **Multiplicities.** For non-simple LRS the polynomial factors $P_j(n)$ break the clean $S$-unit-equation formulation on which the conjectural approaches rest, so even the conditional results do not cover general LRS.

## 6. The Gap

Everything hinges on one missing ingredient: an **effective archimedean bound** $N(a_1,\dots,a_k,u_0,\dots,u_{k-1})$ such that a non-degenerate LRS has no zeros beyond $N$. Given such a bound, brute-force search decides the problem. Section 4 supplies this bound exactly when a *single* term dominates the exponential polynomial for large $n$ — order $\le 4$, or distinct root moduli. The gap opens at order $5$, the first order at which two conjugate pairs of roots may share a modulus while remaining non-degenerate:
$$u_n = c\lambda^n + \big(a\rho^n e^{in\theta_1} + \bar a \rho^n e^{-in\theta_1}\big) + \big(b\rho^n e^{in\theta_2} + \bar b \rho^n e^{-in\theta_2}\big).$$
Deciding $u_n=0$ here needs effective lower bounds on $\|n\theta_1/2\pi - \alpha\|$ and $\|n\theta_2/2\pi - \beta\|$ simultaneously, with $\alpha,\beta$ determined by the phases — precisely the inhomogeneous simultaneous approximation problem for which no effective theory exists. Bridging the gap means either (i) proving the Skolem Conjecture (or enough of it) to certify zero-freeness by congruences, or (ii) an effective inhomogeneous multidimensional Baker-type theorem.

## 7. Current Research (as of June 2026)

- **Max Planck Institute for Software Systems (Saarbrücken) — Ouaknine's group**, with Worrell (Oxford), Luca (Wits/Ostrava), Purser, Nieuwveld. Two active threads: conditional decidability under the Skolem and $p$-adic Schanuel conjectures, and the **Skolem tool**, an implementation combining the Skolem–Mahler–Lech decomposition, modular sieving for certificates of zero-freeness, and Baker-based bounds where applicable *(frontier — verify current version and benchmark scope)*.
- **Universal Skolem sets.** Extending sets of positive density on which zeros are computable toward density $1$; the Bateman–Horn-based constructions of Luca–Maynard–Noubissie use analytic prime-tuple heuristics *(frontier — verify)*.
- **Number-theoretic side.** Work on the exponential local–global principle (Bartolome–Bilu–Luca) targets the Skolem Conjecture for restricted classes of algebraic units.
- **Verification side.** Reductions of program-termination, probabilistic-model-checking and weighted-automata equivalence questions to Skolem/Positivity, motivating the tool work; Positivity remains the harder of the pair, open at order $\ge 6$.

## 8. Future Work

1. **Prove the Skolem Conjecture for algebraic units** of small degree — this alone unconditionally settles reversible LRS of moderate order.
2. **Effective inhomogeneous simultaneous approximation.** Any effective version of Kronecker-type density statements for $\{(n\theta_1, n\theta_2)\}$ with algebraic $\theta_i$ would break order $5$.
3. **Order 5 as a focused target.** Ouaknine and Worrell have repeatedly flagged order $5$ (simple, two equal-modulus conjugate pairs plus one real root) as the smallest genuinely open instance; a complete treatment there is the natural next milestone.
4. **Import the positive-characteristic method.** Derksen's automata-theoretic proof is effective in characteristic $p$; understanding what fails on lifting to characteristic $0$ may isolate the exact obstruction.
5. **Hardness beyond NP.** Establish a stronger lower bound (e.g. PSPACE-hardness) or an unconditional reduction showing Skolem is at least as hard as a known open Diophantine problem.

## 9. Key References

- **[Foundational]** Th. Skolem. *Ein Verfahren zur Behandlung gewisser exponentialer Gleichungen und diophantischer Gleichungen.* 8. Skandinaviske Matematikerkongress, Stockholm, 1934, 163–188.
- **[Foundational]** K. Mahler. *Eine arithmetische Eigenschaft der Taylor-Koeffizienten rationaler Funktionen.* Proc. Akad. Wetensch. Amsterdam 38 (1935), 50–60.
- **[Foundational]** C. Lech. *A note on recurring series.* Arkiv för Matematik 2 (1953), 417–421.
- **[Foundational]** J. Berstel, M. Mignotte. *Deux propriétés décidables des suites récurrentes linéaires.* Bulletin de la Société Mathématique de France 104 (1976), 175–184.
- **[Partial result]** M. Mignotte, T. N. Shorey, R. Tijdeman. *The distance between terms of an algebraic recurrence sequence.* Journal für die reine und angewandte Mathematik 349 (1984), 63–76.
- **[Partial result]** N. K. Vereshchagin. *Occurrence of zero in a linear recursive sequence.* Matematicheskie Zametki 38 (1985), 609–615.
- **[Hardness]** V. D. Blondel, N. Portier. *The presence of a zero in an integer linear recurrent sequence is NP-hard to decide.* Linear Algebra and its Applications 351–352 (2002), 91–98.
- **[Positive characteristic]** H. Derksen. *A Skolem–Mahler–Lech theorem in positive characteristic and finite automata.* Inventiones Mathematicae 168 (2007), 175–224.
- **[Positive characteristic]** H. Derksen, D. Masser. *Linear equations over multiplicative groups, recurrences, and mixing I.* Proceedings of the London Mathematical Society 104 (2012), 1045–1083.
- **[SOTA / Recent]** J. Ouaknine, J. Worrell. *Positivity problems for low-order linear recurrence sequences.* SODA 2014, 366–379.
- **[SOTA / Recent]** J. Ouaknine, J. Worrell. *Ultimate positivity is decidable for simple linear recurrence sequences.* ICALP 2014, LNCS 8573, 330–341.
- **[SOTA / Recent]** F. Luca, J. Ouaknine, J. Worrell. *Universal Skolem sets.* LICS 2021.
- **[SOTA / Recent]** F. Luca, J. Maynard, A. Noubissie, J. Ouaknine, J. Worrell. *A universal Skolem set of positive lower density.* MFCS 2022, LIPIcs 241.
- **[SOTA / Recent]** Y. Bilu, F. Luca, J. Nieuwveld, J. Ouaknine, D. Purser, J. Worrell. *Skolem meets Schanuel.* MFCS 2022, LIPIcs 241.
- **[SOTA / Recent]** R. Lipton, F. Luca, J. Nieuwveld, J. Ouaknine, D. Purser, J. Worrell. *On the Skolem problem and the Skolem conjecture.* LICS 2022.
- **[Related]** M. Bartolome, Y. Bilu, F. Luca. *On the exponential local–global principle.* Acta Arithmetica 159 (2013), 101–111.
- **[Survey]** J. Ouaknine, J. Worrell. *Decision problems for linear recurrence sequences.* Reachability Problems (RP) 2012, LNCS 7550, 21–28.
- **[Survey / Book]** G. Everest, A. van der Poorten, I. Shparlinski, T. Ward. *Recurrence Sequences.* Mathematical Surveys and Monographs 104, American Mathematical Society, 2003.
- **[Survey / Book]** T. Tao. *Structure and Randomness: Pages from Year One of a Mathematical Blog.* American Mathematical Society, 2008 (§ on the effective Skolem–Mahler–Lech problem).

## 10. Worked Example / Concrete Special Case

**A solvable instance (order 3, dominant root).** Take
$$u_n = 2^n - 3n - 1 .$$
Its characteristic roots are $2, 1, 1$, i.e. $\chi(x) = (x-2)(x-1)^2 = x^3 - 4x^2 + 5x - 2$, so
$$u_{n+3} = 4u_{n+2} - 5u_{n+1} + 2u_n,\qquad u_0 = 0,\ u_1 = -2,\ u_2 = -3 .$$
Check: $u_3 = 4(-3) - 5(-2) + 2(0) = -2$ and indeed $2^3 - 10 = -2$; $u_4 = 4(-2) - 5(-3) + 2(-2) = 3 = 16 - 13$. ✓

Decide $\mathcal{Z}(u)$:
- The root ratio $2/1 = 2$ is not a root of unity, so the LRS is non-degenerate — no infinite progressions of zeros.
- $\lambda_1 = 2$ strictly dominates, so an *effective* bound is available directly: for $n \ge 4$, induction gives $2^n > 3n+1$ (base $2^4 = 16 > 13$; step $2^{n+1} = 2\cdot 2^n > 2(3n+1) = 6n+2 > 3n+4$).
- Finite search over $n \in \{0,1,2,3\}$: $u_0 = 0$, $u_1 = -2$, $u_2 = -3$, $u_3 = -2$.

Hence $\mathcal{Z}(u) = \{0\}$, decided with a certified bound $N = 4$. This is exactly the dominant-root case of Section 4.

**The instance that breaks the method (order 5).** Let $\rho e^{\pm i\theta_1}, \rho e^{\pm i\theta_2}$ be two conjugate pairs of algebraic numbers of the same modulus $\rho$ with $\theta_1/\pi$, $\theta_2/\pi$ and $\theta_1/\theta_2$ all irrational, and let $\lambda \in \mathbb{R}$ with $|\lambda| < \rho$. For an LRS
$$u_n = c\lambda^n + 2|a|\rho^n\cos(n\theta_1 + \varphi_1) + 2|b|\rho^n\cos(n\theta_2 + \varphi_2),$$
dividing by $\rho^n$ makes the first term vanish in the limit, and $u_n = 0$ becomes, up to $o(1)$,
$$|a|\cos(n\theta_1 + \varphi_1) + |b|\cos(n\theta_2 + \varphi_2) = 0 .$$
By Weyl equidistribution the pair $(n\theta_1, n\theta_2) \bmod 2\pi$ is dense in the torus, so the left side comes arbitrarily close to $0$ infinitely often. Whether it ever *equals* $0$ (before the $o(1)$ correction) depends on how fast $(n\theta_1,n\theta_2)$ approaches the zero curve — an effective simultaneous inhomogeneous approximation question with no known answer. No dominant term exists, Baker's theorem gives nothing, and the $p$-adic argument still only says "finitely many". This is the open frontier at $k = 5$.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*