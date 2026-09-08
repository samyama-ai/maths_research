---
id: 10-theoretical-cs/border-rank-versus-rank-gap
title: "Border Rank versus Rank Gap Conjecture"
topic: 10-theoretical-cs
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Border Rank versus Rank Gap Conjecture

> **Topic:** Theoretical Computer Science · **ID:** `10-theoretical-cs/border-rank-versus-rank-gap` · **Status:** open

## 1. Problem Statement / Conjecture

Let $T \in A \otimes B \otimes C$ be a tensor over $\mathbb{C}$, with rank $R(T)$ and border rank $\underline{R}(T)$. Always $\underline{R}(T) \le R(T)$, and the inequality can be strict. Define the **gap function**

$$g(r) \;=\; \max\{\, R(T) \;:\; T \text{ a tensor of order } 3 \text{ over } \mathbb{C},\ \underline{R}(T) \le r \,\}.$$

$g(r)$ is finite for every $r$ (Lehmkuhl–Lickteig 1989), but no polynomial upper bound is known.

**Conjecture (linear gap).** There is an absolute constant $C$ with $g(r) \le C\,r$ for all $r$; the sharp form conjectures $g(r) = 2r - O(1)$.

**Weak form (polynomial gap).** $g(r) \le \mathrm{poly}(r)$.

A proof must either exhibit, for every $T$ of border rank $r$, an exact decomposition into $O(r)$ (resp. $\mathrm{poly}(r)$) rank-one terms, or produce a family $T_r$ with $\underline{R}(T_r) \le r$ and $R(T_r)/r \to \infty$. The question is open even for order-3 tensors over $\mathbb{C}$; the field matters ($\mathbb{R}$ behaves differently), and the order-$d$ analogue is open for every $d \ge 3$.

## 2. Mathematical Foundations

Let $A,B,C$ be finite-dimensional $\mathbb{C}$-vector spaces. A tensor $T \in A\otimes B\otimes C$ has

$$R(T) \;=\; \min\Big\{\, r : T = \sum_{i=1}^{r} a_i \otimes b_i \otimes c_i,\ a_i \in A,\ b_i \in B,\ c_i \in C \,\Big\}.$$

Border rank is the rank needed in the limit:

$$\underline{R}(T) \;=\; \min\Big\{\, r : T \in \overline{\{\,S : R(S) \le r\,\}} \,\Big\},$$

closure in the Euclidean (equivalently Zariski) topology. Equivalently, $\underline{R}(T)\le r$ iff there exist curves $a_i(\varepsilon), b_i(\varepsilon), c_i(\varepsilon)$ with entries Laurent polynomials in $\varepsilon$ such that

$$T \;=\; \lim_{\varepsilon \to 0} \sum_{i=1}^{r} a_i(\varepsilon)\otimes b_i(\varepsilon)\otimes c_i(\varepsilon),$$

i.e. $\sum_i a_i(\varepsilon)\otimes b_i(\varepsilon)\otimes c_i(\varepsilon) = T + \varepsilon\,E_1 + \cdots + \varepsilon^{q} E_q$ for some error terms $E_j$. The smallest such $q$ is the **error degree** $\deg_\varepsilon(T,r)$.

Geometrically, $\underline{R}(T)\le r$ says $[T] \in \sigma_r(\mathrm{Seg}(\mathbb{P}A\times\mathbb{P}B\times\mathbb{P}C))$, the $r$-th secant variety of the Segre variety. $R$ is the rank with respect to the Segre itself; $\underline{R}$ is the rank with respect to its closure. $R$ is not lower semicontinuous, $\underline{R}$ is; hence the gap.

**Key bridging theorem (Bini 1980).** Interpolation on $\varepsilon$ converts an approximate decomposition into an exact one at multiplicative cost in the error degree:

$$R(T) \;\le\; \underline{R}(T)\cdot\big(\deg_\varepsilon(T,\underline{R}(T)) + 1\big).$$

Thus the whole conjecture is equivalent to bounding the error degree: $g(r) = O(r)$ iff every border-rank-$r$ tensor admits an approximate decomposition of bounded error degree.

**Degeneration.** $\underline{R}(T)\le r$ iff $T$ is a degeneration of the unit tensor $\langle r\rangle = \sum_{i=1}^r e_i\otimes e_i\otimes e_i$, i.e. $T \in \overline{GL(A)\times GL(B)\times GL(C)\cdot \langle r\rangle}$ after padding. Finiteness of $g(r)$ follows because the degeneration can be realized by a curve of bounded degree in a space whose dimension depends only on $r$ (a concise tensor of border rank $r$ lives in a format of size at most $r\times r\times r$).

For matrix multiplication $\langle m,n,p\rangle \in \mathbb{C}^{mn}\otimes\mathbb{C}^{np}\otimes\mathbb{C}^{pm}$, both quantities control the exponent $\omega$: $\omega = \inf\{\tau : \underline{R}(\langle n,n,n\rangle) = O(n^\tau)\}$, which is *why* border rank was introduced.

## 3. History & State of the Art (SOTA)

- **1969.** Strassen shows $R(\langle 2,2,2\rangle)\le 7$, opening bilinear complexity.
- **1979–80.** Bini, Capovani, Lotti, Romani give an *approximate* algorithm for the $2\times2$ product with one zero entry using 5 multiplications, where 6 are needed exactly — the first explicit rank/border-rank separation for a natural tensor. Bini (1980) proves the interpolation theorem above, making border rank a legitimate complexity measure.
- **1989.** Lehmkuhl and Lickteig prove that the error degree of a border-rank-$r$ tensor is bounded by a function of $r$ alone, so $g(r) < \infty$. The bound extracted from their argument is at least exponential in $r$; no better general bound is known today.
- **2008.** de Silva and Lim connect the gap to the ill-posedness of best low-rank tensor approximation: the infimum in the least-squares problem need not be attained precisely when the target has $\underline{R} < R$.
- **2013–14.** Buczyński and Landsberg classify tensors of border rank $\le 3$ and compute the maximal rank on the third secant variety, giving $g(3)=5$.
- **2016.** Bläser and Lysikov study degeneration degree for tensors and algebras, giving explicit (still exponential) error-degree bounds in structured cases.
- **2017–18.** Zuiddam constructs explicit tensor families with rank exceeding border rank by a constant factor, giving $g(r) \ge cr$ with $c>1$; Christandl, Jensen and Zuiddam show $R(W^{\otimes 2}) = 7 < 9$, disproving multiplicativity of rank and simultaneously exhibiting a $7/4$ ratio against $\underline{R}(W^{\otimes 2}) = 4$.
- **2018–2021.** Landsberg–Michałek prove $\underline{R}(\langle n,n,n\rangle) \ge 2n^2 - \lceil\log_2 n\rceil - 1$; Conner–Harper–Landsberg push $\underline{R}(\langle 3,3,3\rangle) \ge 17$, against $R(\langle 3,3,3\rangle)\le 23$ (Smirnov, Laderman) and $\underline{R}(\langle 3,3,3\rangle)\le 20$ (Smirnov).

**SOTA summary.** Lower bound $g(r) \ge \tfrac{7}{4}r - O(1)$; upper bound $g(r) \le \exp(O(r\log r))$-type from error-degree arguments. The gap between these is the problem.

## 4. Partial Results / Verified Cases

- $g(1) = 1$: border rank 1 implies rank 1 (the Segre is closed).
- $g(2) = 3$: a concise tensor of border rank $2$ lives in $\mathbb{C}^2\otimes\mathbb{C}^2\otimes\mathbb{C}^2$, where maximal rank is $3$; the W-state attains it.
- $g(3) = 5$ (Buczyński–Landsberg, *On the third secant variety*, 2014): full classification of points of $\sigma_3(\mathrm{Seg})$ and their ranks.
- **Matrix pencils** ($2\times n\times n$ tensors): Kronecker normal form gives closed formulas for both $R$ and $\underline{R}$ (Grigoriev; JaJa; see Landsberg 2012, §10). Here $R(T) - \underline{R}(T)$ equals the number of nontrivial Jordan blocks, so $R \le 2\underline{R}$ — the linear conjecture holds with $C=2$ for all $2$-slice tensors.
- **Symmetric border rank $\le 3$ and binary forms:** Sylvester's algorithm gives exact rank/border rank for $\mathbb{C}^2$-forms; for a degree-$d$ binary form, $R \le d+1-\underline{R}$, again linear.
- **Small formats:** in $\mathbb{C}^2\otimes\mathbb{C}^2\otimes\mathbb{C}^2$ max rank $3$, max border rank $2$; in $\mathbb{C}^3\otimes\mathbb{C}^3\otimes\mathbb{C}^3$ max rank $5$, max border rank $5$; in $\mathbb{C}^n\otimes\mathbb{C}^n\otimes\mathbb{C}^2$ everything is decided by Kronecker theory.
- **Bounded error degree:** for any $T$ with $\deg_\varepsilon \le q$, Bini interpolation yields $R(T)\le (q+1)\underline{R}(T)$. All known families satisfy $q \le 2$; no example with $q$ growing is known.
- **Matrix multiplication:** $R(\langle 2,2,2\rangle) = \underline{R}(\langle 2,2,2\rangle) = 7$ (Winograd; Landsberg 2006), so the gap is $0$ there.

## 5. Principal Obstacles

- **Degeneration curves are uncontrolled.** Finiteness of $g(r)$ comes from a compactness/constructibility argument (Lehmkuhl–Lickteig), which bounds the degree of an approximating curve by elimination-theoretic degree bounds. These are exponential in the number of variables ($\sim r^2$ parameters), and elimination theory offers no leverage to make them linear.
- **No lower-bound technique separates rank from border rank by more than a constant.** All robust rank lower bounds — substitution method, Strassen's commutator equations, laser-method-style arguments, slice rank, the barrier results of Christandl–Vrana–Zuiddam — are either border-rank lower bounds (hence useless for the gap) or lose exactly the constant factor one needs. The substitution method, the main tool giving $R$ strictly above $\underline{R}$, yields $R(T)\ge 2\dim A - O(\log)$-type bounds and cannot exceed a factor $\approx 2$.
- **Rank is not semicontinuous, so geometry fights back.** Every algebro-geometric invariant of $[T]$ (Hilbert function, apolarity, singularities of the annihilator scheme) is continuous or semicontinuous, hence detects $\underline{R}$; capturing $R$ requires non-closed data.
- **Rank is not multiplicative or additive in a usable way.** Christandl–Jensen–Zuiddam killed multiplicativity ($R(W^{\otimes 2})=7<9$); Shitov refuted Strassen's additivity conjecture. The natural amplification route — tensor a constant-factor gap with itself to get a super-constant gap — therefore fails: border rank *is* multiplicative, rank is not, and the ratio can shrink under $\otimes$.
- **Cactus/smoothable rank do not interpolate.** The intermediate notions (cactus rank, smoothable rank) that make apolarity work sit *below* rank and above border rank only sometimes, so they do not give an upper bound ladder toward $R$.

## 6. The Gap

Proven: $g(r) = r$ for $r\le 1$, $g(2)=3$, $g(3)=5$, linear behaviour for pencils and binary forms, and $g(r) \ge \tfrac74 r - O(1)$ in general. General upper bound: only $g(r) < \infty$ with an exponential-type explicit bound.

The exact missing step is a **uniform bound on the error degree**. Concretely: show there is a constant $q_0$ (or $q(r)=O(\log r)$) such that every $T$ with $\underline{R}(T)\le r$ admits

$$\sum_{i=1}^{r} a_i(\varepsilon)\otimes b_i(\varepsilon)\otimes c_i(\varepsilon) \;=\; T + O(\varepsilon^{\,q_0+1}),$$

after which Bini interpolation closes the conjecture with $C = q_0+1$. Equivalently: bound the degree of an optimal curve in $\sigma_r(\mathrm{Seg})$ through $[T]$ transverse to the rank stratification. Every known instance has $q_0 \le 2$; nobody can rule out $q_0$ growing with $r$, and nobody can construct such a tensor. Related, and equally open: Strassen's asymptotic rank conjecture would force the *asymptotic* ratio $\lim_n R(T^{\otimes n})^{1/n} / \underline{R}(T)$ to collapse for tight tensors, i.e. the gap disappears in the limit even where it is nonzero at $n=1$.

## 7. Current Research (as of June 2026)

- **Border apolarity** (Buczyńska–Buczyński, Duke 2021) is the dominant new machinery: multigraded Hilbert schemes give border rank lower bounds and, applied at Texas A&M (Landsberg's group) and IMPAN Warsaw (Buczyński, Michałek — now MPI/Konstanz), have produced the current border ranks of small matrix multiplication and determinant tensors. Extending apolarity to *exact* rank is an active and unresolved direction. *(frontier — verify)*
- **Error-degree computations** for structured families (Bläser's group, Saarbrücken; Lysikov) aim at explicit small-$q$ certificates for classes such as tensors of minimal border rank and $1_*$-generic tensors.
- **Minimal border rank tensors** ($\underline{R}(T)=\dim A$) are now classified up to $\dim A = 5$ via the Hilbert scheme of points and Quot schemes (Jelisiejew, Landsberg, Pal); the rank of such tensors is bounded linearly in these cases, supporting the conjecture. *(frontier — verify)*
- **Asymptotic spectrum of tensors** (Strassen; Christandl–Vrana–Zuiddam; CWI Amsterdam) reframes the gap asymptotically: support functionals and quantum functionals bound asymptotic subrank/border rank but are provably blind to the rank/border-rank gap at finite $n$.
- **Computer search** for tensors of border rank $r$ with rank $> 2r$ in formats up to $6\times6\times6$, using numerical homotopy continuation and SAT/Gröbner certificates; no example found. *(frontier — verify)*

## 8. Future Work

1. **Prove $g(4)$ and $g(5)$.** Extending the Buczyński–Landsberg classification to the fourth and fifth secant varieties would give the first data points beyond the trivially-classified range and test $g(r)=2r-1$.
2. **Bound error degree for minimal border rank tensors.** These have the richest structure (they correspond to commuting-matrix / smoothable algebra data); a linear bound here would be the first infinite family beyond pencils.
3. **Find a super-constant separation.** Search among tensors with high error degree by construction — e.g. degenerations along curves of high tangency order, or tensors built from non-smoothable algebras of small length (the length-8 non-smoothable Gorenstein algebras are the natural candidates).
4. **Adapt substitution beyond factor 2.** Any rank lower bound above $2\dim A$ for a concise tensor would be new and would immediately improve $g(r)$'s lower bound.
5. **Settle the asymptotic version.** Decide whether $\tilde{R}(T) = \underline{\tilde{R}}(T)$ for all tensors, which is implied by Strassen's asymptotic rank conjecture.

## 9. Key References

- **[Foundational]** V. Strassen. *Gaussian elimination is not optimal.* Numerische Mathematik 13 (1969), 354–356.
- **[Foundational]** D. Bini, M. Capovani, F. Romani, G. Lotti. *$O(n^{2.7799})$ complexity for $n\times n$ approximate matrix multiplication.* Information Processing Letters 8 (1979), 234–235.
- **[Foundational]** D. Bini. *Relations between exact and approximate bilinear algorithms. Applications.* Calcolo 17 (1980), 87–97.
- **[Foundational]** T. Lehmkuhl, T. Lickteig. *On the order of approximation in approximative triadic decompositions of tensors.* Theoretical Computer Science 66 (1989), 1–14.
- **[Book]** P. Bürgisser, M. Clausen, M. A. Shokrollahi. *Algebraic Complexity Theory.* Grundlehren der mathematischen Wissenschaften 315, Springer, 1997.
- **[Book]** J. M. Landsberg. *Tensors: Geometry and Applications.* Graduate Studies in Mathematics 128, AMS, 2012.
- **[Book]** J. M. Landsberg. *Geometry and Complexity Theory.* Cambridge Studies in Advanced Mathematics 169, Cambridge University Press, 2017.
- **[Partial result]** J. Buczyński, J. M. Landsberg. *Ranks of tensors and a generalization of secant varieties.* Linear Algebra and its Applications 438 (2013), 668–689.
- **[Partial result]** J. Buczyński, J. M. Landsberg. *On the third secant variety.* Journal of Algebraic Combinatorics 40 (2014), 475–502.
- **[SOTA / Recent]** J. Zuiddam. *A note on the gap between rank and border rank.* Linear Algebra and its Applications 525 (2017), 33–44.
- **[SOTA / Recent]** M. Christandl, A. K. Jensen, J. Zuiddam. *Tensor rank is not multiplicative under the tensor product.* Linear Algebra and its Applications 543 (2018), 125–139.
- **[SOTA / Recent]** M. Bläser, V. Lysikov. *On degeneration of tensors and algebras.* Proc. MFCS 2016, LIPIcs 58, 19:1–19:11.
- **[SOTA / Recent]** J. M. Landsberg, M. Michałek. *A $2n^2-\log_2(n)-1$ lower bound for the border rank of matrix multiplication.* International Mathematics Research Notices 2018(15), 4722–4733.
- **[SOTA / Recent]** A. Conner, A. Harper, J. M. Landsberg. *New lower bounds for matrix multiplication and $\det_3$.* Forum of Mathematics, Sigma 9 (2021), e35.
- **[SOTA / Recent]** W. Buczyńska, J. Buczyński. *Apolarity, border rank, and multigraded Hilbert scheme.* Duke Mathematical Journal 170 (2021), 3659–3702.
- **[Applications]** V. de Silva, L.-H. Lim. *Tensor rank and the ill-posedness of the best low-rank approximation problem.* SIAM Journal on Matrix Analysis and Applications 30 (2008), 1084–1127.
- **[Survey]** M. Bläser. *Fast Matrix Multiplication.* Theory of Computing Graduate Surveys 5 (2013), 1–60.
- **[Computational]** A. V. Smirnov. *Bilinear complexity and practical algorithms for matrix multiplication.* Computational Mathematics and Mathematical Physics 53 (2013), 1781–1795.

## 10. Worked Example / Concrete Special Case

Take $A=B=C=\mathbb{C}^2$ with bases $\{a_1,a_2\}$, $\{b_1,b_2\}$, $\{c_1,c_2\}$, and the **W-state**

$$W \;=\; a_1\otimes b_1\otimes c_2 \;+\; a_1\otimes b_2\otimes c_1 \;+\; a_2\otimes b_1\otimes c_1 .$$

**Border rank $\le 2$.** Set

$$S(\varepsilon) \;=\; \tfrac{1}{\varepsilon}\Big[(a_1+\varepsilon a_2)\otimes(b_1+\varepsilon b_2)\otimes(c_1+\varepsilon c_2) \;-\; a_1\otimes b_1\otimes c_1\Big].$$

Expanding, the $\varepsilon^0$ terms cancel, and

$$S(\varepsilon) \;=\; W \;+\; \varepsilon\big(a_1\otimes b_2\otimes c_2 + a_2\otimes b_1\otimes c_2 + a_2\otimes b_2\otimes c_1\big) \;+\; \varepsilon^{2}\, a_2\otimes b_2\otimes c_2 .$$

So $R(S(\varepsilon))\le 2$ for all $\varepsilon\neq 0$ and $\lim_{\varepsilon\to0}S(\varepsilon)=W$, giving $\underline{R}(W)\le 2$. Since $W\neq 0$ is not a product tensor, $\underline{R}(W)=2$. The error degree here is $q=2$.

**Rank $=3$.** Write $W$ as a pencil of $C$-slices: the coefficient of $c_1$ is $M_1 = a_1b_2 + a_2b_1 \cong \begin{pmatrix}0&1\\1&0\end{pmatrix}$, and of $c_2$ is $M_2 = a_1b_1 \cong \begin{pmatrix}1&0\\0&0\end{pmatrix}$. A $2\times2\times2$ tensor has rank $2$ iff its pencil is simultaneously diagonalizable, iff Cayley's hyperdeterminant $\det(\lambda M_1 + \mu M_2)$ has two distinct roots. Here

$$\det(\lambda M_1 + \mu M_2) \;=\; \det\begin{pmatrix}\mu & \lambda\\ \lambda & 0\end{pmatrix} \;=\; -\lambda^{2},$$

a double root at $\lambda=0$: the pencil is not diagonalizable (it is a single Jordan block), so $R(W) \ge 3$. The displayed expression for $W$ has three terms, so $R(W)=3$.

**Bini check.** $\underline{R}(W)\cdot(q+1) = 2\cdot 3 = 6 \ge 3 = R(W)$: the interpolation bound is valid but loose.

**Scaling up.** For the direct sum $W^{\oplus k}$ one has $\underline{R}=2k$ and $R=3k$ (rank is additive on these), so $g(2k)\ge 3k$, i.e. $g(r)\ge \tfrac32 r$. Using $W^{\otimes 2}$ instead — with $\underline{R}(W^{\otimes 2}) = \underline{R}(W)^2 = 4$ but $R(W^{\otimes 2}) = 7 < 9$ (Christandl–Jensen–Zuiddam 2018) — direct sums give $g(4k)\ge 7k$, i.e. $g(r)\ge \tfrac74 r$, the best ratio known. Note what happened: squaring made border rank multiply exactly while rank fell short of $3^2$. That is precisely the amplification failure described in Section 5, and it is why no example with ratio above $2$ has ever been produced.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*