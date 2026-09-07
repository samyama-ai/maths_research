---
id: 02-algebra-group-theory/james-conjecture
title: "James Conjecture"
topic: 02-algebra-group-theory
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# James Conjecture

> **Topic:** Algebra & Group Theory · **ID:** `02-algebra-group-theory/james-conjecture` · **Status:** solved-recently (disproved by Williamson, 2017; weight-restricted forms still open)

## 1. Problem Statement / Conjecture

Let $p$ be a prime and $F$ a field of characteristic $p$. The decomposition numbers of the symmetric group $\mathfrak{S}_n$ over $F$ are the multiplicities
$$d^{(p)}_{\lambda\mu} = [\,S^\lambda_F : D^\mu_F\,], \qquad \lambda \vdash n,\; \mu \text{ $p$-regular},$$
of the simple modules $D^\mu_F$ in the Specht modules $S^\lambda_F$. In parallel, let $\mathcal{H}_n(q)$ be the Iwahori–Hecke algebra of type $A_{n-1}$ over a field of characteristic $0$ with $q$ a primitive $e$-th root of unity, with decomposition numbers $d^{(e)}_{\lambda\mu}$. James and Mathas showed there is a square unitriangular non-negative integer **adjustment matrix** $A$ with
$$D^{(p)} = D^{(e)} A \quad\text{when } e = p .$$

**James's Conjecture (1990).** If a block $B$ of $F\mathfrak{S}_n$ (or of the Schur algebra $S_F(n,n)$) has $p$-weight $w$ with
$$w < p,$$
then the corresponding block of $A$ is the identity matrix; equivalently $d^{(p)}_{\lambda\mu} = d^{(e=p)}_{\lambda\mu}$ for all $\lambda,\mu$ in $B$. In particular the modular decomposition numbers of $\mathfrak{S}_n$ for $n < p^2$ would be computed by the (characteristic-free, algorithmically known) Hecke-algebra numbers.

A disproof requires exhibiting one block with $w<p$ and one off-diagonal adjustment entry $a_{\mu\nu}\neq 0$. A proof would require showing the characteristic-$p$ and root-of-unity categories have identical composition multiplicities in that range.

## 2. Mathematical Foundations

**Blocks and weight.** By the Nakayama conjecture (a theorem), $S^\lambda$ and $S^\nu$ lie in the same $p$-block of $F\mathfrak{S}_n$ iff $\lambda,\nu$ have the same $p$-core. If $\lambda$ has $p$-core $\kappa$ with $|\kappa| = n - pw$, then $w$ is the **$p$-weight**; the defect group has order $p^{\,\lceil \cdot \rceil}$ growing with $w$, and $w=0$ means the block is simple (defect zero).

**Hecke algebra.** $\mathcal{H}_n(q)$ has generators $T_1,\dots,T_{n-1}$ with
$$(T_i-q)(T_i+1)=0,\qquad T_iT_{i+1}T_i=T_{i+1}T_iT_{i+1},\qquad T_iT_j=T_jT_i\ (|i-j|>1).$$
For $q$ a primitive $e$-th root of unity in characteristic $0$, Specht modules $S^\lambda$ and simples $D^\mu$ ($\mu$ $e$-regular) are defined by Dipper–James, and $e$ plays the role of $p$.

**Ariki's theorem / LLT.** Let $\mathcal{F}$ be the level-one Fock space for $U_v(\widehat{\mathfrak{sl}}_e)$ with standard basis $\{|\lambda\rangle\}$. Lascoux–Leclerc–Thibon defined a canonical basis $\{G(\mu)\}$ and Ariki proved
$$G(\mu)\big|_{v=1} = \sum_{\lambda} d^{(e)}_{\lambda\mu}\,|\lambda\rangle ,$$
so $d^{(e)}_{\lambda\mu}$ are computable by the LLT algorithm. The unknown is the passage $d^{(e=p)} \rightsquigarrow d^{(p)}$, i.e. $A$.

**Geometric side.** Via Soergel bimodules and the Riche–Williamson/Elias–Williamson theory, characteristic-$p$ multiplicities for $GL_n$ are governed by the **$p$-canonical basis** ${}^p\!H_x = \sum_y {}^p\!h_{y,x}(v) H_y$ of the Hecke algebra, computed from indecomposable parity/Soergel bimodules over $F$. One has ${}^p\!h_{y,x} = h_{y,x}$ (ordinary Kazhdan–Lusztig) exactly when the local intersection cohomology $IH^\bullet_y(\overline{X_x};\mathbb{Z})$ is $p$-torsion-free. Torsion in $IH^\bullet$ of Schubert varieties is thus the exact obstruction, and James's conjecture asserts a torsion-free range $w<p$.

## 3. History & State of the Art (SOTA)

- **1990.** G. James, computing decomposition matrices of $GL_n(q)$ for $n\le 10$, observes that all discrepancies between characteristic-$p$ and root-of-unity data occur only for $w\ge p$, and formulates the conjecture (Proc. LMS 60 (1990)).
- **1996–97.** LLT conjecture and Ariki's theorem make $d^{(e)}$ effectively computable; James–Mathas formalise the adjustment matrix via a $q$-analogue of the Jantzen–Schaper theorem.
- **1996–2008.** Verification for small weights: Richards ($w=2$), Fayers ($w=3$, $w=4$).
- **2008.** Chuang–Rouquier prove blocks of the same weight are derived equivalent ($\mathfrak{sl}_2$-categorification), proving Broué's abelian defect conjecture for symmetric groups and reducing the conjecture to a statement depending only on $w$ and $p$.
- **2017.** **Williamson, "Schubert calculus and torsion explosion" (JAMS 30, 1023–1046)** disproves the conjecture. Using intersection-cohomology torsion of Schubert varieties for $SL_n$ produced by products of $2\times 2$ elementary matrices, he shows torsion primes grow *exponentially* in $n$, violating the polynomial bounds implicit in Lusztig's conjecture and yielding blocks with $w<p$ and non-trivial adjustment matrix. An appendix by Kontorovich–McNamara–Williamson shows such primes occur with positive density along explicit families.
- **Post-2017.** The correct replacement is not a numerical bound but the $p$-canonical basis: Riche–Williamson's tilting character formula for $GL_n$ (Astérisque 397, 2018) expresses $d^{(p)}$ in terms of ${}^p\!h_{y,x}$, which is computable but not by a closed formula.

## 4. Partial Results / Verified Cases

- **$w=0$:** trivial — simple blocks, $A=I$.
- **$w=1$:** all such blocks are Brauer tree algebras with a line tree and multiplicity 1; decomposition matrices coincide for all $p\ge 2$.
- **$w=2$, $p\ge 3$:** Richards (1996) computed the decomposition numbers explicitly ($0/1$ entries determined by pairs of $p$-hooks) and confirmed $A=I$.
- **$w=3$, $p\ge 5$:** Fayers (Trans. AMS 360 (2008)) — James's conjecture holds.
- **$w=4$, $p\ge 5$:** Fayers (J. Algebra 317 (2007)) — holds for weight-four blocks of Hecke algebras and symmetric groups.
- **All $n\le$ moderate size:** exhaustive computation of decomposition matrices of $\mathfrak{S}_n$ (GAP/Magma, Jantzen–Schaper bounds) shows no counterexample for $n$ in the low hundreds; every documented failure of $A=I$ in that range has $w\ge p$.
- **Rouquier ("RoCK") blocks:** for $w<p$, Chuang–Kessar and Turner's Rock-block theory give explicit Morita/derived models in which the conjecture is verified for these representatives — but the Chuang–Rouquier equivalence transports only *derived*, not decomposition-matrix, data across all blocks of weight $w$ when $w \ge p$ effects intervene.
- **Counterexamples (Williamson 2017):** exist, but only for large parameters — reported torsion primes such as $p=839$ arising from explicit matrix words, with the associated symmetric groups of degree of order $10^6$. No counterexample is known with $n$ small enough for direct computation.

## 5. Principal Obstacles

- **No positivity/torsion-freeness in characteristic $p$.** Ordinary KL combinatorics rests on the decomposition theorem for $\mathbb{Q}$-coefficients. Over $\mathbb{Z}$ or $\mathbb{F}_p$ the decomposition theorem fails; parity sheaves exist but their characters are not given by any known recursion.
- **Torsion explosion.** Williamson shows $IH^\bullet$ of Schubert varieties in $SL_n/B$ contains torsion of order growing like $\vartheta^n$ (Fibonacci-type growth from products $\begin{pmatrix}1&a\\0&1\end{pmatrix}\begin{pmatrix}1&0\\b&1\end{pmatrix}$). Any conjecture bounding bad behaviour by a polynomial in $n$ (or by $w<p$) is therefore doomed; the failure is not an artefact of small primes.
- **Jantzen–Schaper is only an inequality.** The standard tool bounds decomposition numbers from above by weighted sums; for $w\ge 3$ the bounds cease to pin entries down uniquely, so Fayers-type arguments require intricate case analysis that does not scale.
- **Categorification is characteristic-blind at the wrong level.** $\mathfrak{sl}_2$-categorification controls blocks up to derived equivalence, which preserves Cartan matrices but not decomposition matrices with their labelling; it cannot see the adjustment matrix.
- **Effectiveness.** Even with Riche–Williamson, computing ${}^p\!h_{y,x}$ requires Soergel-bimodule computations of size exponential in the Coxeter length.

## 6. The Gap

Proven: $A=I$ for $w\le 4$ (with $p\ge 5$). Disproved: the general claim "$w<p \Rightarrow A=I$". The residual gap is the interval $5\le w<p$: no counterexample is known with small weight, and no proof covers $w\ge 5$. The precise missing step is a criterion for $p$-torsion-freeness of $IH^\bullet_y(\overline{X_x};\mathbb{Z})$ (equivalently ${}^p\!h_{y,x}=h_{y,x}$) in terms of the combinatorial weight $w$ of the corresponding block. Williamson's construction produces torsion only for very long Weyl-group elements; the open question is the *threshold* — the smallest $w$ (as a function of $p$, or absolutely) at which counterexamples begin.

## 7. Current Research (as of June 2026)

- **$p$-canonical basis computation.** Jensen–Williamson's algorithms and the `Soergel`/`IHecke` implementations (Sydney, MPIM Bonn) tabulate ${}^p\!h_{y,x}$ for $S_n$, $n\le 10$–$12$, seeking small-weight anomalies. No small-weight counterexample found *(frontier — verify)*.
- **Weight-5 and weight-6 blocks.** Extensions of Fayers's induction/Jantzen–Schaper methods, and Rock-block reductions (Turner, Chuang, Tan, Kleshchev–Muth Schurian-infinite analysis), aimed at $w=5$ *(frontier — verify)*.
- **Geometric Satake / Smith–Treumann.** Riche–Williamson and Bezrukavnikov–Riche use the Frobenius-twisted Smith theory to relate characteristic-$p$ tilting characters to affine data, giving conceptual replacements for James's statement.
- **Kontorovich-style number theory.** Density of torsion primes in matrix-product families, connecting thin-group counting to representation theory.
- **Groups:** Sydney (Williamson, Mathas), Clermont-Ferrand/Paris (Riche), Bonn (MPIM), QMUL (Fayers), Oregon/Colorado (Kleshchev, Brundan).

## 8. Future Work

- Determine $w_{\min}(p)$: the least weight admitting a non-identity adjustment block. Williamson's examples suggest $w$ grows fast with $p$; a conjectural asymptotic is absent.
- Prove a "$p$-James" statement: identify a modified basis (the $p$-canonical basis restricted to a block) for which unitriangular agreement holds in a genuine range.
- Push explicit verification to $w=5,6$ using RoCK blocks plus derived equivalence, exploiting that only one block per weight need be checked.
- Develop torsion-detection criteria for Schubert varieties (Braden–Williamson style local models) to bound $p$-torsion by combinatorial invariants of the core/quotient.

## 9. Key References

- **[Foundational]** G. D. James. *The decomposition matrices of $GL_n(q)$ for $n\le 10$.* Proc. London Math. Soc. (3) **60** (1990), 225–265.
- **[Foundational]** G. James, A. Mathas. *A $q$-analogue of the Jantzen–Schaper theorem.* Proc. London Math. Soc. (3) **74** (1997), 241–274.
- **[Foundational]** A. Lascoux, B. Leclerc, J.-Y. Thibon. *Hecke algebras at roots of unity and crystal bases of quantum affine algebras.* Comm. Math. Phys. **181** (1996), 205–263.
- **[Foundational]** S. Ariki. *On the decomposition numbers of the Hecke algebra of $G(m,1,n)$.* J. Math. Kyoto Univ. **36** (1996), 789–808.
- **[SOTA]** G. Williamson. *Schubert calculus and torsion explosion.* J. Amer. Math. Soc. **30** (2017), 1023–1046 (with an appendix by A. Kontorovich, P. J. McNamara and G. Williamson).
- **[SOTA]** S. Riche, G. Williamson. *Tilting modules and the $p$-canonical basis.* Astérisque **397**, Soc. Math. France, 2018.
- **[SOTA]** L. T. Jensen, G. Williamson. *The $p$-canonical basis for Hecke algebras.* In *Categorification and Higher Representation Theory*, Contemp. Math. **683**, AMS, 2017, 333–361.
- **[Partial results]** M. J. Richards. *Some decomposition numbers for Hecke algebras of general linear groups.* Math. Proc. Cambridge Philos. Soc. **119** (1996), 383–402.
- **[Partial results]** M. Fayers. *Decomposition numbers for weight three blocks of symmetric groups and Iwahori–Hecke algebras.* Trans. Amer. Math. Soc. **360** (2008), 1341–1376.
- **[Partial results]** M. Fayers. *James's Conjecture holds for weight four blocks of Iwahori–Hecke algebras.* J. Algebra **317** (2007), 593–633.
- **[Structural]** J. Chuang, R. Rouquier. *Derived equivalences for symmetric groups and $\mathfrak{sl}_2$-categorification.* Ann. of Math. (2) **167** (2008), 245–298.
- **[Survey/Book]** A. Mathas. *Iwahori–Hecke Algebras and Schur Algebras of the Symmetric Group.* Univ. Lecture Series **15**, AMS, 1999.
- **[Related]** P. Fiebig. *An upper bound on the exceptional characteristics for Lusztig's character formula.* J. reine angew. Math. **673** (2012), 1–31.

## 10. Worked Example / Concrete Special Case

Take $p = e = 3$, $n = 4$. Partitions of $4$ and their $3$-cores:

| $\lambda$ | $3$-core | weight $w$ |
|---|---|---|
| $(4)$ | $(1)$ | 1 |
| $(3,1)$ | $(3,1)$ | 0 |
| $(2,2)$ | $(1)$ | 1 |
| $(2,1,1)$ | $(2,1,1)$ | 0 |
| $(1^4)$ | $(1)$ | 1 |

So the principal block $B$ contains $\{(4),(2,2),(1^4)\}$ with $w = 1 < p = 3$; $(3,1)$ and $(2,1,1)$ are defect-zero blocks (their hook lengths $\{4,2,1,1\}$ contain no multiple of $3$).

The $3$-regular partitions in $B$ are $(4)$ and $(2,2)$, giving two simples $D^{(4)}, D^{(2,2)}$. A weight-one block is a Brauer tree algebra whose tree is a line with $e=3$ edges and no exceptional vertex, so its decomposition matrix is the $3\times 2$ "staircase":

$$D^{(3)}_B=\begin{array}{c|cc} & (4) & (2,2)\\\hline (4) & 1 & 0\\ (2,2) & 1 & 1\\ (1^4) & 0 & 1\end{array}$$

On the Hecke side, run the LLT algorithm at $e=3$ in the Fock space. Starting from $|(4)\rangle$ and applying $\widehat{\mathfrak{sl}}_3$-operators, the canonical basis elements specialise at $v=1$ to
$$G((4))\mapsto |(4)\rangle+|(2,2)\rangle,\qquad G((2,2))\mapsto |(2,2)\rangle+|(1^4)\rangle,$$
which reproduces exactly the matrix above: $d^{(e=3)}_{(2,2),(4)} = 1 = d^{(3)}_{(2,2),(4)}$, etc. Hence the adjustment matrix of $B$ is $A = I_2$, confirming James's conjecture in this instance.

The conjecture's content is that this coincidence should persist for all $w<p$. It does for $w \le 4$. Williamson's counterexamples show that at the other extreme — where the Weyl group element indexing the block is long enough for $IH^\bullet$ of the corresponding Schubert variety to carry $p$-torsion — an entry of $A$ becomes non-zero even though $w<p$, so the LLT output and the true modular matrix differ by a strictly unitriangular correction.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*