---
id: 02-algebra-group-theory/buchsbaum-eisenbud-horrocks-conjecture
title: "Buchsbaum-Eisenbud-Horrocks Conjecture"
topic: 02-algebra-group-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Buchsbaum-Eisenbud-Horrocks Conjecture

> **Topic:** Algebra & Group Theory · **ID:** `02-algebra-group-theory/buchsbaum-eisenbud-horrocks-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Let $(R,\mathfrak m,k)$ be a commutative Noetherian local ring and let $M \neq 0$ be a finitely generated $R$-module of finite projective dimension whose support has codimension $c$ (the case of interest: $R$ regular local of dimension $n$, $M$ of finite length, so $c = n$). Let

$$\beta_i(M) \;=\; \dim_k \operatorname{Tor}^R_i(M,k)$$

be the $i$-th Betti number, i.e. the rank of $F_i$ in the minimal free resolution $F_\bullet \to M$.

**Conjecture (Buchsbaum–Eisenbud 1977; Horrocks).**
$$\beta_i(M) \;\ge\; \binom{c}{i} \qquad \text{for all } 0 \le i \le c .$$

**Weak / total rank form.** $\displaystyle\sum_{i\ge 0}\beta_i(M) \ge 2^{c}$.

A complete proof must establish the binomial bound for every such $(R,M)$; a disproof needs one finitely generated module of finite projective dimension and finite length over a regular local ring with $\beta_i < \binom{n}{i}$ for some $i$. The Koszul complex on a regular sequence $x_1,\dots,x_c$ shows the bound is sharp: $M = R/(x_1,\dots,x_c)$ has $\beta_i = \binom{c}{i}$ and total rank exactly $2^c$.

## 2. Mathematical Foundations

**Minimal free resolution.** Over local $(R,\mathfrak m,k)$, every finitely generated $M$ admits a resolution
$$0 \to F_p \xrightarrow{\ d_p\ } \cdots \to F_1 \xrightarrow{\ d_1\ } F_0 \to M \to 0,\qquad d_i(F_i)\subseteq \mathfrak m F_{i-1},$$
unique up to isomorphism; $F_i \cong R^{\beta_i(M)}$ and $p = \operatorname{pd}_R M$. By the Auslander–Buchsbaum formula, $\operatorname{pd}_R M + \operatorname{depth} M = \operatorname{depth} R$, so for $R$ regular of dimension $n$ and $M$ of finite length, $\operatorname{pd}_R M = n$.

**Koszul complex.** For $\underline x = x_1,\dots,x_c$ a regular sequence, $K_\bullet(\underline x) = \bigwedge^\bullet R^c$ with $\partial(e_{j_1}\wedge\cdots\wedge e_{j_i}) = \sum_t (-1)^{t-1}x_{j_t}\, e_{j_1}\wedge\cdots\widehat{e_{j_t}}\cdots\wedge e_{j_i}$ resolves $R/(\underline x)$ and has $\operatorname{rank} K_i = \binom{c}{i}$. The conjecture asserts the Koszul complex is *minimal* among all finite free resolutions with finite-length homology, rank by rank.

**Herzog–Kühl equations.** If a finite-length graded module over $S=k[x_1,\dots,x_n]$ has a *pure* resolution of type $d_0<d_1<\cdots<d_n$ (each $F_i$ generated in the single degree $d_i$), then
$$\frac{\beta_i}{\beta_0} \;=\; \prod_{j\neq i}\left|\frac{d_j-d_0}{d_j-d_i}\right| ,$$
and this quantity is $\ge \binom{n}{i}$, with equality exactly for $d_j = d_0+j$ (Koszul).

**Complex-level version (false in general).** Replacing "$M$ with finite projective dimension" by "a bounded complex $F_\bullet$ of finite free modules with $H_\bullet(F)$ nonzero of finite length" and asking $\operatorname{rank} F_i \ge \binom{c}{i}$ gives a strictly stronger statement, disproved in characteristic $2$ (Section 5).

**Topological avatar.** Carlsson's conjecture: if $(\mathbb Z/p)^r$ acts freely on a finite CW complex $X$, then $\sum_i \dim_{\mathbb F_p} H_i(X;\mathbb F_p) \ge 2^r$. Chain complexes of such $X$ are finite free complexes over $\mathbb F_p[(\mathbb Z/p)^r]$, linking it to the total rank form.

## 3. History & State of the Art (SOTA)

- **1977.** Buchsbaum and Eisenbud state the rank inequality in *Algebra structures for finite free resolutions, and some structure theorems for ideals of codimension 3* (Amer. J. Math. **99**), while classifying codimension-3 Gorenstein ideals.
- **1979.** Hartshorne's problem list (*Topology* **18**) records Horrocks' independent question about syzygies of finite-length modules over regular local rings, in the context of vector bundles on $\mathbb P^n$; the attribution "Buchsbaum–Eisenbud–Horrocks" dates from here.
- **1981–85.** Evans and Griffith prove the Syzygy Theorem and obtain $\beta_1 \ge c$ and $\beta_{c-1}\ge c$; their monograph *Syzygies* (LMS Lecture Notes 106, 1985) is the standard account.
- **1990–92.** Charalambous, Santoni, Evans and Miller settle the multigraded and monomial cases and produce the first survey of the problem.
- **2010.** Erman applies Boij–Söderberg theory to a special case in the graded setting.
- **2017.** Walker proves the **total rank conjecture** when $2$ is invertible: $\sum_i \beta_i(M) \ge 2^c$ (Ann. of Math. **186**). This is the single largest advance; prior general bounds were only linear in $c$.
- **2018.** Iyengar and Walker construct characteristic-2 finite free complexes violating the complex-level binomial bounds (Acta Math. **221**), showing why Walker's odd-characteristic hypothesis is not an artifact.

Status: the binomial (rank-by-rank) conjecture is open for $c \ge 5$; the total rank form is open only in residue characteristic $2$.

## 4. Partial Results / Verified Cases

- **Small codimension.** The full binomial bounds hold for $c \le 4$. The extreme positions $\beta_0\ge 1$, $\beta_c\ge 1$ are trivial; $\beta_1 \ge c$ and $\beta_{c-1}\ge c$ are Evans–Griffith; combined with the total rank bound this closes $c\le 4$.
- **Total rank, odd characteristic.** Walker (2017): $R$ local, containing a field of odd characteristic or more generally with $2$ invertible in $R$; $M\ne 0$ finitely generated of finite projective dimension and codimension $c$ $\Rightarrow$ $\sum_i\beta_i(M)\ge 2^c$. Proof uses Adams operations on the Grothendieck group of perfect complexes with finite-length homology, producing eigenvalue constraints on $\sum(-1)^i\operatorname{rank}F_i$-type invariants.
- **Multigraded modules.** Charalambous (1991): if $M$ is a $\mathbb Z^n$-graded finite-length module over $S=k[x_1,\dots,x_n]$, then $\beta_i(M)\ge\binom{n}{i}$ for all $i$. Covers all Artinian monomial quotients $S/I$.
- **Pure resolutions.** Any finite-length graded module with a pure resolution satisfies the bounds, directly from the Herzog–Kühl equations (Section 2).
- **Complete intersections and quotients by regular sequences.** $M=R/(x_1,\dots,x_c)$ attains equality; modules whose resolutions are tensor products of Koszul-type complexes satisfy the bounds by multiplicativity of $\binom{\cdot}{\cdot}$ under the Vandermonde identity.
- **Consequence.** Walker's theorem yields Carlsson's conjecture for free $(\mathbb Z/p)^r$-actions on finite complexes for odd primes $p$.
- **Special graded families.** Erman (2010) verifies the rank conjecture for a class of graded finite-length modules via Boij–Söderberg decompositions with controlled degree spread.

## 5. Principal Obstacles

- **No induction on codimension.** There is no operation that reduces a finite-length module over an $n$-dimensional regular ring to one over an $(n-1)$-dimensional ring while controlling all $\beta_i$; quotienting by a general linear form destroys finite projective dimension or inflates Betti numbers unpredictably.
- **Characteristic 2 breaks the K-theoretic machine.** Walker's Adams-operation argument divides by $2$: the eigenvalue decomposition of $\psi^k$ on $K$-theory of perfect complexes needs $2$ invertible. Iyengar–Walker's characteristic-2 examples (finite free complexes with finite-length homology and total rank $< 2^c$) show that no purely complex-theoretic argument can succeed there; a proof in characteristic 2 must use that the homology is concentrated in one degree.
- **Total rank $\ne$ individual ranks.** Even where $\sum_i\beta_i\ge 2^c$ is known, the mass can in principle concentrate; nothing in the $K$-theoretic method distributes it as $\binom{c}{i}$. The Adams operations see only Euler-characteristic-type data, not the position of ranks.
- **Boij–Söderberg is scale-blind.** Betti tables decompose as *positive rational* combinations of pure diagrams. The target inequality $\beta_i\ge\binom{c}{i}$ is not invariant under this rational scaling, so decomposition arguments recover the bound only after an integrality input that is not available.
- **No structure theory beyond codimension 3.** Buchsbaum–Eisenbud's classification of resolutions stops at length 3 (with Gorenstein codimension 4 only partially understood), so explicit multiplicative structure on $F_\bullet$ — the tool that produced the original conjecture — cannot be exploited for $c \ge 5$.

## 6. The Gap

Two distinct gaps remain.

1. **Distribution gap.** For $2$ invertible, $\sum_i\beta_i\ge 2^c$ is a theorem, but the per-degree bound $\beta_i\ge\binom{c}{i}$ is not. Closing it needs an invariant refining the total rank — e.g. a filtration or grading on $K$-theory whose graded pieces detect homological degree — such that the extremal object is forced to be the Koszul complex, not merely to have its total rank.
2. **Characteristic gap.** In residue characteristic 2 even $\sum_i\beta_i\ge 2^c$ is open, and the natural complex-level strengthening is false there. The missing step is a mechanism that distinguishes modules (homology in a single degree) from general perfect complexes, since only the former can still satisfy the bound.

## 7. Current Research (as of June 2026)

- **Walker's school (Nebraska–Lincoln), with M. Brown (Auburn) and K. VandeBogert.** Refinements of Adams operations on matrix factorizations, Hermitian and Grothendieck–Witt $K$-theory, aimed at both the characteristic-2 case and degree-wise bounds. *(frontier — verify)*
- **Differential-module analogues.** Bounds on ranks of "free flags" and differential modules with finite-length homology (Brown, Erman, and coauthors) as a flexible replacement for complexes. *(frontier — verify)*
- **Boij–Söderberg refinements.** Attempts to combine the rational cone of Betti tables with integrality/multiplicity constraints (Erman, Eisenbud, Schreyer circle).
- **Toric and equivariant methods.** Extension of Charalambous' multigraded theorem to modules with reductive or torus actions, and to $\mathbb Z^r$-gradings with $r<n$.
- **Topological side.** Halperin–Carlsson conjecture activity (free torus actions, elliptic spaces) at Bochum, Southampton and Ohio State, exchanging techniques with the algebraic problem.

## 8. Future Work

- Find a $K$-theoretic or motivic invariant refining $\psi^k$ that is sensitive to homological degree, converting the total bound into the binomial bounds.
- Settle characteristic 2 for modules, exploiting single-degree homology; a positive answer would complete Carlsson's conjecture for $(\mathbb Z/2)^r$.
- Prove $\beta_2 \ge \binom{c}{2}$ in general — the first genuinely unknown middle case, and the natural next step after Evans–Griffith's $\beta_1\ge c$.
- Push the Buchsbaum–Eisenbud structure theory (algebra structures on $F_\bullet$) past codimension 3–4.
- Systematic computer search (Macaulay2, Singular) for near-extremal Artinian modules with small $\beta_i$, especially over $\mathbb F_2$.

## 9. Key References

- **[Foundational]** D. A. Buchsbaum, D. Eisenbud. *Algebra structures for finite free resolutions, and some structure theorems for ideals of codimension 3.* American Journal of Mathematics **99** (1977), 447–485.
- **[Foundational]** R. Hartshorne. *Algebraic vector bundles on projective spaces: a problem list.* Topology **18** (1979), 117–128.
- **[Foundational]** E. G. Evans, P. Griffith. *Syzygies.* London Mathematical Society Lecture Note Series **106**, Cambridge University Press, 1985.
- **[SOTA / Recent]** M. E. Walker. *Total Betti numbers of modules of finite projective dimension.* Annals of Mathematics **186** (2017), 641–646.
- **[SOTA / Recent]** S. B. Iyengar, M. E. Walker. *Examples of finite free complexes of small rank and small homology.* Acta Mathematica **221** (2018), 143–158.
- **[Partial results]** H. Charalambous. *Lower bounds for Betti numbers of multigraded modules.* Journal of Algebra **137** (1991), 491–500.
- **[Partial results]** D. Erman. *A special case of the Buchsbaum–Eisenbud–Horrocks rank conjecture.* Mathematical Research Letters **17** (2010), 1079–1089.
- **[Survey]** H. Charalambous, E. G. Evans. *Problems on Betti numbers of finite length modules.* In *Free Resolutions in Commutative Algebra and Algebraic Geometry* (Sundance 1990), Research Notes in Mathematics **2**, Jones and Bartlett, 1992.
- **[Survey]** L. L. Avramov. *Infinite free resolutions.* In *Six Lectures on Commutative Algebra*, Progress in Mathematics **166**, Birkhäuser, 1998.
- **[Background]** J. Herzog, M. Kühl. *On the Betti numbers of finite pure and linear resolutions.* Communications in Algebra **12** (1984), 1627–1646.

## 10. Worked Example / Concrete Special Case

Take $R = k[x,y]_{(x,y)}$, regular local of dimension $n=2$; predicted bounds $(\beta_0,\beta_1,\beta_2)\ge(1,2,1)$, total $\ge 4$.

**Extremal case.** $M = R/(x,y) = k$. Koszul complex:
$$0\to R \xrightarrow{\binom{-y}{x}} R^2 \xrightarrow{(x\ \ y)} R \to k \to 0,$$
Betti numbers $(1,2,1)$, total $4 = 2^2$. Equality throughout.

**A second finite-length module.** $M = R/I$ with $I=(x^2,xy,y^2)=\mathfrak m^2$. The syzygies among $x^2, xy, y^2$ are $y\cdot x^2 - x\cdot xy = 0$ and $y\cdot xy - x\cdot y^2 = 0$, giving
$$0 \to R^2 \xrightarrow{\ A\ } R^3 \xrightarrow{(x^2\ \ xy\ \ y^2)} R \to M \to 0, \qquad A=\begin{pmatrix} y & 0\\ -x & y\\ 0 & -x\end{pmatrix}.$$
Minimality holds since all entries lie in $\mathfrak m$. The signed maximal minors of $A$ are $y^2,\ -(-xy)=xy,\ x^2$ — exactly the generators of $I$, so the Hilbert–Burch theorem confirms exactness. Betti numbers $(1,3,2)$: $1\ge\binom20=1$, $3\ge\binom21=2$, $2\ge\binom22=1$, total $6\ge 4$. Conjecture verified, with slack.

**Why $\beta_1\ge 2$ cannot fail here.** If $\beta_1 = 1$ then $\operatorname{pd} M=1$ and $M \cong R/(f)$ for a nonzerodivisor $f$; but $R/(f)$ has dimension $1$, not finite length. If $\beta_1=0$ then $M$ is free, again not of finite length. So $\beta_1\ge2=\binom21$. This is the $c=2$ instance of Evans–Griffith's $\beta_1\ge c$; already at $c=5$, the analogous statement for $\beta_2\ge\binom52=10$ has no such elementary argument, and only $\sum_i\beta_i\ge 32$ (Walker, $\operatorname{char} k \ne 2$) is available.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*