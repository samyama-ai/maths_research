---
id: 10-theoretical-cs/matrix-multiplication-exponent
title: "Matrix Multiplication Exponent"
topic: 10-theoretical-cs
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Matrix Multiplication Exponent

> **Topic:** Theoretical Computer Science · **ID:** `10-theoretical-cs/matrix-multiplication-exponent` · **Status:** open

## 1. Problem Statement / Conjecture

Let $\omega$ denote the **exponent of matrix multiplication**: the infimum of all real $\tau$ such that two $n \times n$ matrices over an arbitrary field $\mathbb{F}$ can be multiplied using $O(n^{\tau})$ arithmetic operations (additions, subtractions, multiplications, and divisions in $\mathbb{F}$).

**The open problem:** determine $\omega$ exactly. The dominant conjecture is

$$\omega = 2,$$

i.e. for every $\varepsilon > 0$ there is an algorithm running in $O(n^{2+\varepsilon})$ operations. (It is known that no $O(n^2)$ algorithm exists in the arithmetic-circuit model for $n\times n$ multiplication with the standard rank measure, so the $o(1)$ slack is essential; $\omega=2$ is an infimum statement, not an achieved bound.)

A complete resolution requires either (a) a construction, for each $\varepsilon>0$, of a bilinear algorithm family of cost $O(n^{2+\varepsilon})$, or (b) a proof of a lower bound $\omega \ge 2+\delta$ for some $\delta>0$ — which would be the first superquadratic lower bound for any explicit bilinear map and would qualitatively exceed all known algebraic complexity lower-bound technology.

Current status (2025): $2 \le \omega < 2.371339$.

## 2. Mathematical Foundations

**The matrix multiplication tensor.** Multiplication of an $n\times m$ by an $m\times p$ matrix is the bilinear map encoded by the tensor
$$\langle n,m,p\rangle \;=\; \sum_{i=1}^{n}\sum_{j=1}^{m}\sum_{k=1}^{p} x_{ij}\otimes y_{jk}\otimes z_{ki} \;\in\; \mathbb{F}^{nm}\otimes\mathbb{F}^{mp}\otimes\mathbb{F}^{pn}.$$

**Rank.** The *tensor rank* $R(T)$ is the least $r$ with $T=\sum_{\ell=1}^{r} a_\ell\otimes b_\ell\otimes c_\ell$, $a_\ell,b_\ell,c_\ell$ of rank one in their factors. Equivalently, $R(\langle n,n,n\rangle)$ is the minimum number of *non-scalar* multiplications in a bilinear algorithm.

**Definition of $\omega$.**
$$\omega \;=\; \inf\{\tau \in \mathbb{R} : R(\langle n,n,n\rangle) = O(n^{\tau})\}.$$
Strassen's recursion — $\langle n,m,p\rangle \otimes \langle n',m',p'\rangle = \langle nn',mm',pp'\rangle$ — gives submultiplicativity $R(\langle n^k,n^k,n^k\rangle)\le R(\langle n,n,n\rangle)^k$, so a single algorithm with $R(\langle n,n,n\rangle)=r$ yields $\omega \le \log_n r$. Bilinear cost dominates: total arithmetic cost is $\Theta(n^{\omega})$ up to $n^{o(1)}$.

**Border rank.** $\underline{R}(T)$ is the least $r$ such that $T$ is a limit of tensors of rank $\le r$; formally, over $\mathbb{F}[\epsilon]$,
$$\epsilon^{q} T \;=\; \sum_{\ell=1}^{r} a_\ell(\epsilon)\otimes b_\ell(\epsilon)\otimes c_\ell(\epsilon) \;+\; O(\epsilon^{q+1}).$$
**Bini's theorem** (1980): $\omega=\inf\{\tau:\underline{R}(\langle n,n,n\rangle)=O(n^{\tau})\}$ — approximate algorithms suffice, at a cost of only $n^{o(1)}$.

**Schönhage's $\tau$-theorem** (asymptotic sum inequality, 1981): if $\underline{R}\big(\bigoplus_{i=1}^{s}\langle n_i,m_i,p_i\rangle\big) \le r$ with the summands independent, then
$$\sum_{i=1}^{s} (n_i m_i p_i)^{\omega/3} \;\le\; r.$$
This makes *disjoint, unbalanced* products usable, and is the engine of every modern bound.

**Laser method** (Strassen 1986; Coppersmith–Winograd 1990). One takes a "structurally simple" starting tensor of low border rank, e.g. the CW tensor
$$\mathrm{CW}_q=\sum_{i=1}^{q}\big(x_0y_iz_i + x_iy_0z_i + x_iy_iz_0\big) + x_0y_0z_{q+1}+x_0y_{q+1}z_0+x_{q+1}y_0z_0,\qquad \underline{R}(\mathrm{CW}_q)\le q+2,$$
takes a large tensor power, and zeroes out variable blocks so that the surviving blocks form a large set of *disjoint* matrix-multiplication tensors; the $\tau$-theorem then bounds $\omega$. Choosing which blocks to keep is a combinatorial optimization over probability distributions on triples, solved by convex programming.

**Group-theoretic framework** (Cohn–Umans 2003). If a finite group $G$ has subsets $S,T,U$ with the *triple product property* ($s^{-1}s' \, t^{-1}t' \, u^{-1}u' = 1 \Rightarrow s=s',t=t',u=u'$), then $\langle |S|,|T|,|U|\rangle$ embeds in the group algebra $\mathbb{F}[G]$, and Wedderburn's theorem $\mathbb{F}[G]\cong\bigoplus_i \mathbb{F}^{d_i\times d_i}$ reduces it to smaller matrix products, giving $(|S||T||U|)^{\omega/3}\le \sum_i d_i^{\omega}$.

**Related exponents.** The *dual exponent* $\alpha$ is the supremum of $\kappa$ with $\langle n,n,n^{\kappa}\rangle$ computable in $n^{2+o(1)}$; $\omega=2$ iff $\alpha=1$. Strassen's **asymptotic rank conjecture** asserts $\underline{R}(T^{\otimes k})^{1/k}\to \dim$-many for all tight tensors, and implies $\omega=2$.

## 3. History & State of the Art (SOTA)

Until 1969, $2n^3-n^2$ operations (the schoolbook algorithm) was believed optimal. **Volker Strassen** (*Gaussian elimination is not optimal*, Numer. Math. 1969) computed $\langle 2,2,2\rangle$ with 7 multiplications, giving $\omega\le\log_2 7 < 2.8074$.

Milestones in the upper bound:

| Year | Author(s) | Bound on $\omega$ | Method |
|---|---|---|---|
| 1969 | Strassen | 2.8074 | recursion on $\langle 2,2,2\rangle$ |
| 1978 | Pan | 2.795 | trilinear aggregation |
| 1979 | Bini–Capovani–Lotti–Romani | 2.7799 | border rank |
| 1981 | Schönhage | 2.548 | asymptotic sum inequality |
| 1981 | Coppersmith–Winograd | 2.496 | partial matrix products |
| 1986 | Strassen | 2.479 | laser method |
| 1990 | Coppersmith–Winograd | 2.3755 | $\mathrm{CW}_q$ + laser method |
| 2010–12 | Stothers; Vassilevska Williams | 2.3729 | higher powers of $\mathrm{CW}_q$ |
| 2014 | Le Gall | 2.3728639 | 8th/32nd powers, convex programming |
| 2021 | Alman–Vassilevska Williams | 2.3728596 | refined laser method |
| 2023 | Duan–Wu–Zhou | 2.371866 | asymmetric hashing |
| 2024 | Vassilevska Williams–Xu–Xu–Zhou | 2.371552 | refined asymmetric hashing |
| 2025 | Alman–Duan–Vassilevska Williams–Xu–Xu–Zhou | **2.371339** | combination loss compensation |

Lower bounds have moved far less: $R(\langle n,n,n\rangle)\ge 3n^2-o(n^2)$ (Landsberg 2014; earlier $2.5n^2-3n$, Bläser 1999), and $\underline{R}(\langle n,n,n\rangle)\ge 2n^2-\lceil\log_2 n\rceil-1$ (Landsberg–Michałek 2018). All are $O(n^2)$ and hence give nothing beyond $\omega\ge 2$.

## 4. Partial Results / Verified Cases

- **$\langle 2,2,2\rangle$: fully solved.** $R=7$ (Strassen upper; Winograd 1971 and Hopcroft–Kerr 1971 lower). $\underline{R}=7$ as well (Landsberg 2006). All 7-term decompositions are equivalent under the symmetry group (de Groote 1978).
- **$\langle 3,3,3\rangle$: open.** $19 \le R \le 23$; upper bound by Laderman (1976), lower bound $R\ge 19$ by Bläser (2003). Border rank $\underline R\ge 17$ (Landsberg–Michałek). A rank-$\le 22$ algorithm would give $\omega<2.81$… but not beat Strassen ($\log_3 23=2.854$).
- **Small rectangular cases.** $R(\langle 2,2,3\rangle)=11$, $R(\langle 2,2,5\rangle)=18$, $R(\langle 2,3,3\rangle)=15$ (Hopcroft–Kerr; Smirnov; Heule–Kauers–Seidl SAT searches).
- **Machine-found decompositions.** AlphaTensor (Fawzi et al., *Nature* 2022) found rank-47 $\langle 4,4,4\rangle$ over $\mathbb{Z}/2$ (beating $7^2=49$) and rank-76 $\langle 4,5,5\rangle$. Kauers–Moosbauer's *flip graph* search (2022–2023) gave $R(\langle 5,5,5\rangle)\le 93$ and $R(\langle 4,4,5\rangle)\le 76$. AlphaEvolve (2025) reported a rank-48 $\langle4,4,4\rangle$ decomposition over $\mathbb{C}$ *(frontier — verify)*.
- **Restricted models.** Over the *bilinear-with-commutativity* and *tensor-restricted* models exact answers are known for many $\langle n,m,p\rangle$ with $nmp\le 60$.
- **Special structures.** $\omega=2$ is *known* for multiplication of structured families: Toeplitz, circulant, Hankel and Vandermonde matrices all admit $\tilde O(n)$ or $\tilde O(n^2)$ algorithms via FFT; group algebras of abelian groups reduce exactly to the DFT.
- **Dual exponent.** $\alpha \ge 0.321334$ (Duan–Wu–Zhou 2023), improving Le Gall–Urrutia's $0.31389$; i.e. $n\times n$ by $n\times n^{0.32}$ is already in $n^{2+o(1)}$.

## 5. Principal Obstacles

- **No superquadratic lower bound technique exists.** The best general lower bounds on tensor rank for explicit tensors in $\mathbb{F}^{N}\otimes\mathbb{F}^{N}\otimes\mathbb{F}^{N}$ are $\approx 3N$ (substitution method, Bläser; border-rank via Koszul flattenings and Young flattenings, Landsberg–Ottaviani). Flattening-based methods are *provably capped*: a Koszul flattening of $\langle n,n,n\rangle$ has rank at most $\sim 2n^2$, so they cannot exceed $2n^2$, i.e. cannot show $\omega>2$. Since $\dim\langle n,n,n\rangle$'s ambient space is $N=n^2$, $3N=3n^2$ is *quadratic* in $n$ — the lower-bound machinery is a full polynomial factor from relevance.
- **Laser-method barriers.** Ambainis, Filmus and Le Gall (STOC 2015) proved that applying the laser method to any fixed power of $\mathrm{CW}_q$ cannot give $\omega<2.3078$, and that the $k$-th power for $k\le 16$ cannot give below $2.3725$. Alman and Vassilevska Williams (FOCS 2018 / JACM 2021) formalized *universal method* and *galactic* barriers: for large classes of starting tensors — including $\mathrm{CW}_q$ and all Coppersmith–Winograd-type tensors — no choice of degeneration can prove $\omega<2.168$. Recent bounds inch toward these barriers, not past them.
- **Cap-set obstruction to the group-theoretic route.** Blasiak, Church, Cohn, Grochow, Naslund, Sawin and Umans (*Discrete Analysis*, 2017), using the Croot–Lev–Pach/Ellenberg–Gijswijt polynomial method, showed that abelian groups of bounded exponent cannot yield $\omega=2$ via the simultaneous-triple-product-property; the tri-colored sum-free set bound $O(c^n)$, $c<3$, caps the achievable gain. This killed the most concrete proposed route to $\omega=2$.
- **The $o(1)$ is unavoidable and uncontrolled.** All bounds since 1979 are *asymptotic and non-constructive in effect*: the $n^{o(1)}$ factors and the recursion depths make current algorithms galactic (crossover points beyond $10^{20}$), so no computation can test whether the constructions are near-optimal.
- **Degeneration loses too much.** Zeroing out blocks in the laser method destroys a constant fraction of the tensor's "value" at every level; quantifying and recovering that loss ("combination loss compensation", 2025) yields only fourth-decimal improvements.

## 6. The Gap

Proven: $2 \le \omega < 2.371339$. The interval has width $\approx 0.371$ and every improvement since 1990 has been in the third or fourth decimal.

The gap is *structural*, not quantitative:

1. **Upper-bound side.** Every bound since Schönhage flows through the same pipeline — pick a low-border-rank tensor $T$, take $T^{\otimes k}$, degenerate to disjoint matrix products, apply the $\tau$-theorem. The barrier results say this pipeline stops before $2.168$. To reach $\omega=2$ one needs a genuinely new source of tensors, or a way to use $T^{\otimes k}$ *without* zeroing out blocks.
2. **Lower-bound side.** Proving $\omega>2$ needs a lower bound of the form $\underline{R}(\langle n,n,n\rangle)\ge n^{2+\delta}$. Nothing in algebraic geometry currently produces superlinear-in-ambient-dimension border-rank bounds for *any* explicit tensor sequence; this is essentially the tensor analogue of the explicit-obstruction problem in geometric complexity theory.

The single crossing step: exhibit (or rule out) a family of tensors $T_n$ with $\underline{R}(T_n)=n^{2+o(1)}$ that degenerates to $\langle n,n,n\rangle$ *without* asymptotically lossy block-zeroing. Strassen's asymptotic rank conjecture is one precise formulation whose proof would deliver $\omega=2$.

## 7. Current Research (as of June 2026)

- **Asymmetric hashing / loss compensation.** The Duan–Wu–Zhou (FOCS 2023) idea of asymmetric variable-block hashing, refined by Vassilevska Williams, Xu, Xu, Zhou (SODA 2024) and Alman, Duan, Vassilevska Williams, Xu, Xu, Zhou (SODA 2025) to $\omega<2.371339$, remains the active upper-bound line (MIT, Tsinghua/IIIS, Berkeley). Further gains are expected to be $10^{-4}$-scale.
- **Asymptotic spectrum of tensors.** Strassen's programme, continued by Christandl, Vrana, Zuiddam: the asymptotic spectrum $\Delta(\mathcal{T})$ of tensors, quantum functionals, and the support-rank/slice-rank toolkit. Kaski, Michałek and collaborators connect Strassen's asymptotic rank conjecture to faster set-cover and Boolean-tensor algorithms *(frontier — verify)*.
- **Search-based decompositions.** Flip-graph and SAT/SMT search (Kauers–Moosbauer, Heule–Kauers–Seidl), reinforcement learning (AlphaTensor, AlphaEvolve), and Gröbner-basis certification of small ranks. These improve concrete $\langle n,m,p\rangle$ ranks but have not yet moved $\omega$.
- **Geometry and lower bounds.** Landsberg, Michałek, Conner, Huang and Rupniewski study border-rank via border apolarity and $110$-equations, seeking to push border-rank bounds past $2n^2$. Border apolarity has settled several small-tensor cases exactly.
- **Practical side.** Numerical stability of fast algorithms (Demmel, Dumitriu, Holtz; Bini–Lotti), communication-avoiding Strassen, and $\langle 4,4,4\rangle$-level kernels in production BLAS.

## 8. Future Work

- Prove or refute **Strassen's asymptotic rank conjecture** for tight tensors; even partial results would settle $\omega=2$ conditionally in useful cases.
- Find a construction escaping the Alman–Vassilevska Williams universal-method barrier: candidates include non-CW starting tensors with large symmetry groups, tensors from simple Lie algebras, and coherent-configuration constructions.
- Revive the **Cohn–Umans programme** with non-abelian groups of unbounded exponent, or with the *simultaneous triple product property* in group algebras where the cap-set obstruction does not apply; Cohn–Kleinberg–Szegedy–Umans's "strong USP" and "two-family" conjectures each imply $\omega=2$ and remain open.
- Develop border-rank lower bounds beyond flattening: border apolarity, deformation theory of $110$-equations, and representation-theoretic obstructions in the sense of geometric complexity theory.
- Improve $\alpha$: since $\alpha=1 \Leftrightarrow \omega=2$, pushing $\alpha$ past $\tfrac12$ would be a landmark.

## 9. Key References

- **[Foundational]** V. Strassen. *Gaussian elimination is not optimal.* Numerische Mathematik 13(4):354–356, 1969.
- **[Foundational]** D. Coppersmith, S. Winograd. *Matrix multiplication via arithmetic progressions.* Journal of Symbolic Computation 9(3):251–280, 1990.
- **[Foundational]** A. Schönhage. *Partial and total matrix multiplication.* SIAM Journal on Computing 10(3):434–455, 1981.
- **[Foundational]** D. Bini, M. Capovani, F. Romani, G. Lotti. *$O(n^{2.7799})$ complexity for $n\times n$ approximate matrix multiplication.* Information Processing Letters 8(5):234–235, 1979.
- **[Book]** P. Bürgisser, M. Clausen, M. A. Shokrollahi. *Algebraic Complexity Theory.* Grundlehren der mathematischen Wissenschaften 315, Springer, 1997.
- **[Book]** J. M. Landsberg. *Geometry and Complexity Theory.* Cambridge Studies in Advanced Mathematics 169, Cambridge University Press, 2017.
- **[SOTA]** J. Alman, R. Duan, V. Vassilevska Williams, Y. Xu, Z. Xu, R. Zhou. *More Asymmetry Yields Faster Matrix Multiplication.* Proc. SODA 2025.
- **[SOTA]** R. Duan, H. Wu, R. Zhou. *Faster Matrix Multiplication via Asymmetric Hashing.* Proc. FOCS 2023.
- **[SOTA]** J. Alman, V. Vassilevska Williams. *A Refined Laser Method and Faster Matrix Multiplication.* Proc. SODA 2021.
- **[Barrier]** J. Alman, V. Vassilevska Williams. *Limits on All Known (and Some Unknown) Approaches to Matrix Multiplication.* Journal of the ACM 68(1), 2021 (conf. FOCS 2018).
- **[Barrier]** A. Ambainis, Y. Filmus, F. Le Gall. *Fast Matrix Multiplication: Limitations of the Coppersmith–Winograd Method.* Proc. STOC 2015.
- **[Barrier]** J. Blasiak, T. Church, H. Cohn, J. A. Grochow, E. Naslund, W. F. Sawin, C. Umans. *On cap sets and the group-theoretic approach to matrix multiplication.* Discrete Analysis, 2017:3.
- **[Lower bound]** J. M. Landsberg. *New lower bounds for the rank of matrix multiplication.* SIAM Journal on Computing 43(1):144–149, 2014.
- **[Lower bound]** J. M. Landsberg, M. Michałek. *A $2n^2-\log_2(n)-1$ lower bound for the border rank of matrix multiplication.* International Mathematics Research Notices 2018(15):4722–4733.
- **[Framework]** H. Cohn, C. Umans. *A group-theoretic approach to fast matrix multiplication.* Proc. FOCS 2003.
- **[Survey]** F. Le Gall. *Algebraic complexity theory and matrix multiplication.* Tutorial, Proc. ISSAC 2014 (and *Powers of tensors and fast matrix multiplication*, ISSAC 2014, pp. 296–303).
- **[Survey]** M. Bläser. *Fast Matrix Multiplication.* Theory of Computing, Graduate Surveys 5, 2013.
- **[Computational]** A. Fawzi et al. *Discovering faster matrix multiplication algorithms with reinforcement learning.* Nature 610:47–53, 2022.
- **[Computational]** M. Kauers, J. Moosbauer. *Flip graphs for matrix multiplication.* Proc. ISSAC 2023.

## 10. Worked Example / Concrete Special Case

**Strassen's $\langle 2,2,2\rangle$ decomposition and why it forces $\omega\le\log_2 7$.**

Let $A=\begin{pmatrix}a_{11}&a_{12}\\a_{21}&a_{22}\end{pmatrix}$, $B=\begin{pmatrix}b_{11}&b_{12}\\b_{21}&b_{22}\end{pmatrix}$, $C=AB$. Define seven products:

$$
\begin{aligned}
M_1&=(a_{11}+a_{22})(b_{11}+b_{22}), & M_2&=(a_{21}+a_{22})\,b_{11}, & M_3&=a_{11}(b_{12}-b_{22}),\\
M_4&=a_{22}(b_{21}-b_{11}), & M_5&=(a_{11}+a_{12})\,b_{22}, & M_6&=(a_{21}-a_{11})(b_{11}+b_{12}),\\
M_7&=(a_{12}-a_{22})(b_{21}+b_{22}). & & & &
\end{aligned}
$$

Then
$$C_{11}=M_1+M_4-M_5+M_7,\quad C_{12}=M_3+M_5,\quad C_{21}=M_2+M_4,\quad C_{22}=M_1-M_2+M_3+M_6.$$

*Check $C_{11}$:*
$M_1+M_4-M_5+M_7 = (a_{11}b_{11}+a_{11}b_{22}+a_{22}b_{11}+a_{22}b_{22}) + (a_{22}b_{21}-a_{22}b_{11}) - (a_{11}b_{22}+a_{12}b_{22}) + (a_{12}b_{21}+a_{12}b_{22}-a_{22}b_{21}-a_{22}b_{22})$.
The terms $a_{11}b_{22}$, $a_{22}b_{11}$, $a_{22}b_{22}$, $a_{22}b_{21}$, $a_{12}b_{22}$ all cancel, leaving $a_{11}b_{11}+a_{12}b_{21}=C_{11}$. ✓

**Tensor reading.** Each $M_\ell$ is a rank-one term $a_\ell\otimes b_\ell\otimes c_\ell$ in $\mathbb{F}^4\otimes\mathbb{F}^4\otimes\mathbb{F}^4$; e.g. $M_1$ contributes $(x_{11}+x_{22})\otimes(y_{11}+y_{22})\otimes(z_{11}+z_{22})$. Summing gives exactly $\langle 2,2,2\rangle$, so $R(\langle2,2,2\rangle)\le 7$. Since the schoolbook count is 8, the saving is one multiplication — bought with 18 additions instead of 4.

**Recursion.** Apply the identity block-wise to $n\times n$ matrices split into four $(n/2)\times(n/2)$ blocks. The seven $M_\ell$ are recursive multiplications of half-size matrices; the additions cost $\Theta(n^2)$:
$$T(n)=7\,T(n/2)+\Theta(n^2)\;\Longrightarrow\; T(n)=\Theta\!\left(n^{\log_2 7}\right)=\Theta(n^{2.8074}).$$

**Why one more saved multiplication matters so much.** A rank-6 decomposition of $\langle 2,2,2\rangle$ would give $\omega\le\log_2 6=2.585$ — but Winograd (1971) proved $R(\langle2,2,2\rangle)=7$ exactly, and Landsberg (2006) proved even $\underline{R}(\langle2,2,2\rangle)=7$. So $2\times 2$ is closed. Progress must come from larger $n$: e.g. $R(\langle3,3,3\rangle)\le 21$ would give $\omega\le\log_3 21 = 2.771$, and $R(\langle n,n,n\rangle)\le n^{2+o(1)}$ for a *single* growing family would give $\omega=2$. The current record of $2.371339$ comes from no explicit small algorithm at all — it is an asymptotic-sum argument over a degeneration of a high tensor power of $\mathrm{CW}_5$-type tensors, with no realizable implementation.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*