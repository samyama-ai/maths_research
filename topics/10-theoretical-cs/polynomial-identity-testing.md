---
id: 10-theoretical-cs/polynomial-identity-testing
title: "Polynomial Identity Testing"
topic: 10-theoretical-cs
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Polynomial Identity Testing

> **Topic:** Theoretical Computer Science · **ID:** `10-theoretical-cs/polynomial-identity-testing` · **Status:** open

## 1. Problem Statement / Conjecture

**PIT.** Given an arithmetic circuit $C$ over a field $\mathbb{F}$ with $n$ inputs, size $s$ and degree $d$, decide whether the polynomial $C(x_1,\dots,x_n) \in \mathbb{F}[x_1,\dots,x_n]$ is *identically* zero — zero as a formal polynomial, not merely as a function.

The problem is solved in randomized polynomial time: PIT $\in$ coRP (Schwartz–Zippel). The open problem is derandomization.

> **Conjecture (PIT derandomization).** PIT $\in \mathsf{P}$. Equivalently, in the harder *blackbox* setting: for every $n,d,s$ there is an explicit **hitting set** $\mathcal{H} \subseteq \mathbb{F}^n$, constructible in time $\mathrm{poly}(n,d,s)$, such that every nonzero size-$s$ degree-$d$ circuit is nonzero at some point of $\mathcal{H}$.

Two regimes must be distinguished.

- **Whitebox:** the algorithm reads the circuit's wiring.
- **Blackbox:** the algorithm only queries $C$ at points, i.e. must output a hitting set.

A complete resolution means either (a) a deterministic $\mathrm{poly}(n,d,s)$ algorithm for general circuits, or (b) a proof that none exists under a standard hypothesis. Because of Kabanets–Impagliazzo, (a) is known to entail superpolynomial circuit lower bounds, so a proof is expected to be very hard; a *disproof* would have to overturn PIT $\in$ coRP-style heuristics and is not seriously expected.

## 2. Mathematical Foundations

**Arithmetic circuits.** A circuit over $\mathbb{F}$ is a directed acyclic graph whose leaves carry variables $x_i$ or constants, whose internal gates are labelled $+$ or $\times$, with one output gate. *Size* $s$ = number of gates/wires; *depth* = longest leaf-to-root path; *degree* $d$ = formal degree of the computed polynomial. A **formula** is a circuit of fan-out $1$; an **algebraic branching program (ABP)** is a layered DAG with edges labelled by affine forms, computing the sum over $s\to t$ paths of the product of edge labels.

**Complexity classes.** $\mathsf{VP}$ = families $(f_n)$ with $\deg f_n, \mathrm{size}(f_n) = \mathrm{poly}(n)$; $\mathsf{VNP}$ = families with $f_n(x) = \sum_{e \in \{0,1\}^m} g(x,e)$, $g \in \mathsf{VP}$. Valiant's conjecture is $\mathsf{VP} \neq \mathsf{VNP}$, with $\mathrm{per}_n$ the canonical $\mathsf{VNP}$-complete polynomial.

**Schwartz–Zippel lemma.** If $f \in \mathbb{F}[x_1,\dots,x_n]$ is nonzero of total degree $d$ and $S \subseteq \mathbb{F}$ is finite, then
$$\Pr_{a \in_R S^n}\big[f(a) = 0\big] \;\le\; \frac{d}{|S|}.$$
Taking $|S| \ge 2d$ gives a one-sided-error test with error $\le 1/2$; the value $C(a)$ is computed gate-by-gate in time $\mathrm{poly}(s)$ (over $\mathbb{Q}$, modulo a random prime to control bit-length).

**Hitting sets.** $\mathcal{H}$ is a hitting set for a class $\mathcal{C}$ if $\forall f \in \mathcal{C}\setminus\{0\}\ \exists a \in \mathcal{H}: f(a)\neq 0$. A **hitting-set generator** is a map $G:\mathbb{F}^k \to \mathbb{F}^n$ with $f \neq 0 \Rightarrow f\circ G \neq 0$ for all $f \in \mathcal{C}$; small $k$ (seed length) yields a hitting set of size $|S|^k$. By a dimension/counting argument (Heintz–Schnorr 1980), hitting sets of size $\mathrm{poly}(n,d,s)$ *exist* for every class; the content of the conjecture is explicitness.

**Depth-3 ($\Sigma\Pi\Sigma$) circuits.** $C = \sum_{i=1}^{k} \prod_{j=1}^{d_i} \ell_{ij}$ with $\ell_{ij}$ affine forms; $k$ is the top fan-in. Simple-rank machinery: after removing the gcd of each term, if $C \equiv 0$ then $\dim_{\mathbb{F}}\mathrm{span}\{\ell_{ij}\}$ is bounded by a function of $k$ alone (rank bounds).

**Chasm at depth 4/3.** Agrawal–Vinay (2008), sharpened by Koiran and by Gupta–Kamath–Kayal–Saptharishi (2016): any size-$s$ circuit of degree $d=\mathrm{poly}(n)$ has a $\Sigma\Pi\Sigma$ circuit of size $s^{O(\sqrt d)}$. Consequently a $\mathrm{poly}$-time blackbox PIT for depth-4 (even depth-3) circuits of size $s^{O(\sqrt d)}$ derandomizes general PIT in quasipolynomial time.

## 3. History & State of the Art (SOTA)

- **1922 (prehistory).** Ore's lemma bounding roots of a nonzero multivariate polynomial over a finite grid — the ancestor of Schwartz–Zippel.
- **1978–1980.** DeMillo–Lipton, Zippel, and Schwartz independently give the randomized test; Zippel's motivation is sparse interpolation in computer algebra.
- **1979–1987.** Lovász reduces perfect matching to a symbolic determinant; Mulmuley–Vazirani–Vazirani give an RNC matching algorithm via the Isolation Lemma. Matching's parallel derandomization becomes the flagship PIT application.
- **2002–2004.** Agrawal–Kayal–Saxena's PRIMES $\in \mathsf{P}$ is a derandomized identity test of $(X+a)^n \equiv X^n + a \pmod{n, X^r-1}$ — the proof of concept that PIT instances can be derandomized structurally.
- **2003–2004.** Kabanets–Impagliazzo: if PIT $\in$ NSUBEXP then $\mathsf{NEXP} \not\subseteq \mathsf{P}/\mathrm{poly}$ **or** $\mathrm{per}$ has no polynomial-size arithmetic circuits. PIT derandomization is *equivalent in difficulty* to lower bounds, not merely useful for them.
- **2005–2015.** Whitebox and blackbox algorithms for structured classes: noncommutative formulas (Raz–Shpilka), depth-3 bounded top fan-in (Kayal–Saxena; Dvir–Shpilka; Karnin–Shpilka; Saxena–Seshadhri), ROABPs (Forbes–Shpilka; Agrawal–Gurjar–Korwar–Saxena).
- **2018–2019.** Bootstrapping (Agrawal–Ghosh–Saxena; Kumar–Saptharishi–Tengse): a hitting set of size $s^{o(1)}$ for *constant-variate* circuits already gives quasipolynomial hitting sets for all of $\mathsf{VP}$. Hardness-to-randomness in the algebraic setting (Guo–Kumar–Saptharishi–Solomon).
- **2021.** Limaye–Srinivasan–Tavenas prove the first superpolynomial lower bounds against constant-depth algebraic circuits, unlocking quasipolynomial-time blackbox PIT for constant-depth circuits *(via the hardness–randomness route; see §7)*.

**SOTA for general circuits:** no deterministic algorithm better than the trivial $s^{O(n)}$ / brute-force interpolation over a $(d+1)^n$ grid.

## 4. Partial Results / Verified Cases

| Class | Result | Reference |
|---|---|---|
| Sparse polynomials, $m$ monomials | blackbox $\mathrm{poly}(n,d,m)$ | Ben-Or–Tiwari; Klivans–Spielman 2001 |
| Noncommutative formulas / ABPs | whitebox $\mathrm{poly}$ | Raz–Shpilka 2005 |
| ROABP (read-once oblivious ABP, known order) | whitebox $\mathrm{poly}$, blackbox $(nd w)^{O(\log n)}$ | Forbes–Shpilka 2013; AGKS 2015 |
| ROABP, unknown order | blackbox quasipoly | Agrawal–Gurjar–Korwar–Saxena 2015 |
| $\Sigma\Pi\Sigma(k)$, constant top fan-in $k$ | whitebox poly (Kayal–Saxena 2007); blackbox $\mathrm{poly}$ via rank bound $O(k^3\log d)$ | Saxena–Seshadhri 2013 |
| $\Sigma\wedge\Sigma$ (diagonal depth-3) | blackbox quasipoly (duality trick) | Saxena 2008 |
| Read-$k$ oblivious ABPs, $k$ constant | quasipoly blackbox | Anderson–van Melkebeek–Saxena 2015 |
| Bounded top-fanin depth-4, $\Sigma^{[k]}\Pi\Sigma\Pi^{[\delta]}$ | poly-time blackbox for constant $k,\delta$ | Dutta–Dwivedi–Saxena 2021 |
| Bipartite perfect matching (a $\Sigma\Pi$-structured determinant instance) | quasi-$\mathsf{NC}$, i.e. $n^{O(\log n)}$ processors, $\mathrm{polylog}$ depth | Fenner–Gurjar–Thierauf 2016 |
| General graph matching | quasi-$\mathsf{NC}$ | Svensson–Tarnawski 2017 |
| Constant-depth circuits (any fixed depth $\Delta$) | quasipolynomial-time blackbox PIT | Limaye–Srinivasan–Tavenas 2021 + hardness–randomness |

Small parameters are fully settled: for $n = O(1)$ variables and $d = \mathrm{poly}$, brute-force grid interpolation is polynomial — which, by bootstrapping, is exactly the regime where a mild improvement would cascade.

## 5. Principal Obstacles

- **Equivalence with lower bounds.** Kabanets–Impagliazzo shows derandomizing PIT forces a superpolynomial lower bound ($\mathsf{NEXP}\not\subseteq\mathsf{P}/\mathrm{poly}$ or $\mathrm{per}\notin\mathsf{VP}$). No technique currently proves such bounds; the best general arithmetic circuit lower bound remains $\Omega(n\log d)$ (Baur–Strassen). PIT therefore inherits every barrier facing Valiant's conjecture.
- **Exponential monomial blow-up.** A depth-2 formula $\prod_{i=1}^n(x_i+y_i)$ has size $2n$ but $2^n$ monomials. Any technique that manipulates the coefficient vector explicitly — sparse interpolation, Ben-Or–Tiwari, Kronecker substitution — dies immediately for general circuits.
- **Loss of rank/structure at depth 4.** Depth-3 successes rest on Sylvester–Gallai-type rank bounds for *linear* forms. At depth 4 the analogous statements concern radical ideals of quadratics and higher (Sylvester–Gallai for nonlinear polynomials); these are only partially known and degrade fast with degree.
- **Non-relativizing/algebrizing failure is not the issue; naturalness is.** Forbes–Shpilka–Tzameret–Wigderson and Chatterjee–Kumar–Ramya–Saptharishi–Tengse show that "algebraic natural proofs" — the succinct, generic-witness arguments most current lower-bound methods produce — would themselves need PIT-like derandomization to exist, giving a self-referential barrier.
- **Blackbox = variety construction.** A hitting set must intersect the complement of the variety $\mathcal{V}$ of all vanishing circuits. Explicitly constructing points off an implicitly-defined high-codimension variety is exactly Noether normalization, which Mulmuley (GCT V) shows is derandomizable only under strong hardness assumptions.
- **Characteristic and field issues.** Over small finite fields, Schwartz–Zippel needs an extension field; several structural tools (partial derivatives, Wronskians, the duality trick) behave badly in positive characteristic.

## 6. The Gap

What is proven: polynomial-time deterministic PIT for classes whose *structure is read-once, low top fan-in, or non-commutative* — all of which admit a normal form making a nonzero coefficient explicitly locatable. What is asked: the same for arbitrary depth and unbounded reuse of subcomputations.

The precise crossing point is **depth 4 with unbounded top fan-in and degree $d = \Theta(\sqrt{\text{size}})$**: by the chasm results, a blackbox hitting set of size $s^{O(1)}$ for $\Sigma\Pi\Sigma\Pi^{[\sqrt d]}$ circuits of size $s^{O(\sqrt d)}$ yields quasipolynomial-time PIT for all of $\mathsf{VP}$. Equivalently, by bootstrapping (AGS 2018; KST 2019), it suffices to construct, for some constant $k \ge 2$, hitting sets of size $s^{o(1)}$ for $k$-variate degree-$s$ size-$s$ circuits — beating the trivial $s^{k}$ grid by any $s^{\varepsilon}$ factor. The gap is therefore not a matter of scale but of a single super-constant-saving step that no current method delivers.

## 7. Current Research (as of June 2026)

- **Hardness-to-randomness after LST.** Turning the Limaye–Srinivasan–Tavenas constant-depth lower bounds into *polynomial* (not quasipolynomial) hitting sets for constant depth is the most active line, using the Guo–Kumar–Saptharishi–Solomon cone-closed-basis generator and Andrews–Forbes ideal-based lower bounds. *(frontier — verify)* Several 2024–2026 preprints claim improved parameters for $\Sigma\Pi\Sigma\Pi$ set-multilinear PIT.
- **Bootstrapping the constant-variate case.** Groups around Nitin Saxena (IIT Kanpur), Mrinal Kumar (TIFR), and Ramprasad Saptharishi (TIFR) pursue $s^{o(1)}$ hitting sets for few-variate circuits, and the related question of PIT for the *border* class $\overline{\mathsf{VP}}$.
- **Sylvester–Gallai for nonlinear polynomials.** Peleg–Shpilka, Garg–Oliveira–Sengupta and successors have proved radical-ideal SG theorems for quadratics and cubics, giving PIT for $\Sigma^{[k]}\Pi\Sigma\Pi^{[2]}$ and $\Pi^{[3]}$ circuits; extending to degree $\ge 4$ is open. *(frontier — verify)*
- **Closure and factoring.** Dutta–Saxena–Sinhababu's uniform closure of algebraic classes under factoring is being used to show hitting sets are robust under taking factors and roots.
- **Matching / isolation.** Deterministic $\mathsf{NC}$ for perfect matching remains open; work by Gurjar, Thierauf, Svensson continues on derandomizing the Isolation Lemma for polytopes with small face-lattice complexity.
- **Proof complexity.** Ideal Proof System lower bounds (Grochow–Pitassi) are being read back as PIT hardness statements.

## 8. Future Work

- Prove a $\Sigma\Pi\Sigma\Pi$ rank/dimension bound independent of degree — the exact analogue of Saxena–Seshadhri one level up.
- Obtain any explicit hitting set of size $s^{2-\varepsilon}$ for bivariate degree-$s$, size-$s$ circuits; by KST 2019 this bootstraps to quasipolynomial PIT for $\mathsf{VP}$.
- Strengthen LST to $\exp(n^{\Omega(1)})$ lower bounds for constant depth, which under GKSS-style generators would give genuinely polynomial-time constant-depth PIT.
- Settle PIT for the border class $\overline{\mathsf{VP}}$, where limits of circuits break the coefficient-extraction toolbox.
- Determine whether whitebox PIT for general ABPs (not read-once) is in $\mathsf{P}$ — the smallest natural class where nothing beyond Schwartz–Zippel is known.
- Derandomize the Isolation Lemma to place perfect matching in $\mathsf{NC}$.

## 9. Key References

- **[Foundational]** R. A. DeMillo, R. J. Lipton. *A probabilistic remark on algebraic program testing.* Information Processing Letters 7(4), 1978.
- **[Foundational]** J. T. Schwartz. *Fast probabilistic algorithms for verification of polynomial identities.* Journal of the ACM 27(4), 1980.
- **[Foundational]** R. Zippel. *Probabilistic algorithms for sparse polynomials.* EUROSAM 1979, LNCS 72.
- **[Foundational]** J. Heintz, C.-P. Schnorr. *Testing polynomials which are easy to compute.* STOC 1980.
- **[Foundational]** L. Lovász. *On determinants, matchings, and random algorithms.* Fundamentals of Computation Theory (FCT), 1979.
- **[Foundational]** K. Mulmuley, U. V. Vazirani, V. V. Vazirani. *Matching is as easy as matrix inversion.* Combinatorica 7(1), 1987.
- **[Foundational]** V. Kabanets, R. Impagliazzo. *Derandomizing polynomial identity tests means proving circuit lower bounds.* Computational Complexity 13(1–2), 2004.
- **[Foundational]** M. Agrawal, N. Kayal, N. Saxena. *PRIMES is in P.* Annals of Mathematics 160(2), 2004.
- **[SOTA / Recent]** N. Limaye, S. Srinivasan, S. Tavenas. *Superpolynomial lower bounds against low-depth algebraic circuits.* FOCS 2021.
- **[SOTA / Recent]** M. Agrawal, S. Ghosh, N. Saxena. *Bootstrapping variables in algebraic circuits.* STOC 2018; PNAS 116(17), 2019.
- **[SOTA / Recent]** M. Kumar, R. Saptharishi, A. Tengse. *Near-optimal bootstrapping of hitting sets for algebraic circuits.* SODA 2019.
- **[SOTA / Recent]** Z. Guo, M. Kumar, R. Saptharishi, N. Solomon. *Derandomization from algebraic hardness.* FOCS 2019; SIAM J. Computing 51(2), 2022.
- **[SOTA / Recent]** M. A. Forbes, A. Shpilka. *Quasipolynomial-time identity testing of non-commutative and read-once oblivious algebraic branching programs.* FOCS 2013.
- **[SOTA / Recent]** M. Agrawal, R. Gurjar, A. Korwar, N. Saxena. *Hitting-sets for ROABP and sum of set-multilinear polynomials.* SIAM J. Computing 44(3), 2015.
- **[SOTA / Recent]** N. Saxena, C. Seshadhri. *From Sylvester–Gallai configurations to rank bounds: improved blackbox identity test for depth-3 circuits.* Journal of the ACM 60(5), 2013.
- **[SOTA / Recent]** S. Fenner, R. Gurjar, T. Thierauf. *Bipartite perfect matching is in quasi-NC.* STOC 2016.
- **[SOTA / Recent]** A. Gupta, P. Kamath, N. Kayal, R. Saptharishi. *Arithmetic circuits: A chasm at depth 3.* SIAM J. Computing 45(3), 2016.
- **[SOTA / Recent]** M. A. Forbes, A. Shpilka, I. Tzameret, A. Wigderson. *Proof complexity lower bounds from algebraic circuit complexity.* Theory of Computing 17, 2021.
- **[Survey]** A. Shpilka, A. Yehudayoff. *Arithmetic circuits: A survey of recent results and open questions.* Foundations and Trends in TCS 5(3–4), 2010.
- **[Survey]** N. Saxena. *Progress on polynomial identity testing.* Bulletin of the EATCS 99, 2009; and *Progress on polynomial identity testing — II*, in Perspectives in Computational Complexity, Birkhäuser, 2014.
- **[Survey]** R. Saptharishi. *A survey of lower bounds in arithmetic circuit complexity.* Living survey, GitHub, continuously updated.

## 10. Worked Example / Concrete Special Case

**(a) Why the problem is not trivial.** Let
$$C(x_1,\dots,x_n,y_1,\dots,y_n) \;=\; \prod_{i=1}^{n}(x_i+y_i) \;-\; \sum_{S\subseteq[n]}\ \prod_{i\in S}x_i\prod_{i\notin S}y_i .$$
Both sides are equal, so $C \equiv 0$. The first term is a circuit of size $2n$; expanding it produces $2^n$ monomials. Any test that expands the circuit takes $2^n$ time. Schwartz–Zippel with $S=\{0,1,\dots,2n\}$, $d=n$, evaluates $C$ at one random point in $O(n)$ arithmetic operations and errs with probability $\le n/(2n+1) < 1/2$. Derandomizing means naming a *specific* small set of points that works for **every** size-$2n$ circuit, not just this one.

**(b) PIT decides perfect matching.** Take the bipartite graph $G$ on $L=\{1,2\}$, $R=\{1',2'\}$ with edges $\{11', 12', 22'\}$. Its Edmonds matrix is
$$A \;=\; \begin{pmatrix} x_{11} & x_{12} \\ 0 & x_{22}\end{pmatrix},\qquad \det A \;=\; x_{11}x_{22}.$$
$\det A \neq 0$, so $G$ has a perfect matching, namely $\{11', 22'\}$. Remove edge $22'$: then
$$A' = \begin{pmatrix} x_{11} & x_{12} \\ 0 & 0\end{pmatrix},\qquad \det A' = 0,$$
and indeed vertex $2'$... vertex $2$ has only neighbour $2'$ removed, leaving $2$ isolated: no perfect matching. In general $\det A = \sum_{\sigma} \mathrm{sgn}(\sigma)\prod_i x_{i\sigma(i)}$, and terms cannot cancel because each permutation gives a distinct monomial; so $\det A \not\equiv 0 \iff G$ has a perfect matching (Lovász). The determinant has a size-$\mathrm{poly}(n)$ circuit but $n!$ potential monomials — again an instance where evaluation is cheap and expansion is not.

**(c) A depth-3 identity settled by rank.** Consider $\Sigma\Pi\Sigma(3)$ with $d=1$:
$$C = (x+y+z) + (x - y) \cdot(-1) + (-2x + 2y + \dots)$$
More cleanly, the canonical cancellation is
$$C \;=\; (x+y)(x-y) \;-\; (x^2 - y^2) \;\equiv\; 0 .$$
Written as $\Sigma\Pi\Sigma$ with top fan-in $k=2$: $T_1 = (x+y)(x-y)$, $T_2 = -(x+y)(x-y)$. The linear forms $\{x+y, x-y\}$ span a space of dimension $2$. Saxena–Seshadhri's rank bound says a simple, minimal, zero $\Sigma\Pi\Sigma(k)$ circuit of degree $d$ has $\mathrm{rank} = O(k^3 \log d)$; for $k=2$ this is $O(1)$, so it suffices to test the identity on an $O(1)$-dimensional subspace — a hitting set of size $\mathrm{poly}(d)$, computed deterministically. Evaluating $C$ at $(x,y)=(1,0),(0,1),(1,1),(2,1)$ gives $0$ each time, and the rank bound certifies that these few points suffice. **No analogue of this rank certificate is known when the $\ell_{ij}$ are replaced by quadratics of unbounded number** — that missing certificate is precisely the gap of §6.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*