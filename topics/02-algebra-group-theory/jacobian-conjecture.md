---
id: 02-algebra-group-theory/jacobian-conjecture
title: "Jacobian Conjecture"
topic: 02-algebra-group-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Jacobian Conjecture

> **Topic:** Algebra & Group Theory · **ID:** `02-algebra-group-theory/jacobian-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Let $k$ be a field of characteristic $0$ and let
$$F = (F_1,\dots,F_n) : k^n \longrightarrow k^n, \qquad F_i \in k[x_1,\dots,x_n],$$
be a polynomial map. Write $JF = \left(\partial F_i/\partial x_j\right)_{i,j}$ for its Jacobian matrix.

**Conjecture (Keller, 1939).** If $\det JF \in k^{*}$ (a nonzero constant), then $F$ is a polynomial automorphism: there exists $G \in k[x_1,\dots,x_n]^n$ with $F \circ G = G \circ F = \mathrm{id}$.

The converse is elementary: if $F$ is invertible with polynomial inverse $G$, the chain rule gives $JF(x)\cdot JG(F(x)) = I$, so $\det JF$ is a unit in $k[x]$, hence a nonzero constant. A map with $\det JF \in k^*$ is called a **Keller map**. By the Lefschetz principle it suffices to treat $k = \mathbb{C}$; by rescaling one may assume $\det JF = 1$. The statement for fixed $n$ is denoted $\mathrm{JC}_n$.

A complete solution is either a proof of $\mathrm{JC}_n$ for all $n$, or a single explicit Keller map over $\mathbb{C}$ that is not surjective or not injective. Both hypotheses are sharp: in characteristic $p$, $F(x) = x - x^p$ has $F' = 1$ but is not injective on $\overline{\mathbb{F}_p}$; and for real *rational* or non-polynomial smooth maps the analogue fails (Pinchuk, 1994).

## 2. Mathematical Foundations

**Setting.** $\mathrm{GA}_n(k)$ denotes the group of polynomial automorphisms of $\mathbb{A}^n_k$; it contains the affine group $\mathrm{Aff}_n(k)$ and the triangular (de Jonquières) group $\mathrm{BA}_n(k)$. For $n=2$, Jung–van der Kulk gives $\mathrm{GA}_2 = \mathrm{Aff}_2 *_{\mathrm{Aff}_2 \cap \mathrm{BA}_2} \mathrm{BA}_2$ (amalgamated free product); no such structure theorem is known for $n \ge 3$ (Nagata's map is wild in dimension 3, by Shestakov–Umirbaev).

**Injectivity implies bijectivity.** If $F$ is an injective polynomial endomorphism of $\mathbb{A}^n_{\mathbb C}$, then $F$ is an automorphism (Białynicki-Birula–Rosenlicht 1962; also via Ax–Grothendieck). So $\mathrm{JC}_n$ reduces to: *every Keller map is injective*.

**Degree of the inverse.** If a Keller map $F$ of degree $d$ is invertible, then
$$\deg F^{-1} \le d^{\,n-1}$$
(Bass–Connell–Wright 1982; Rusek–Winiarski 1984). This makes $\mathrm{JC}_n$ for fixed $d$ a *decidable* elimination problem: write $G$ with undetermined coefficients of degree $\le d^{n-1}$ and solve $F\circ G = \mathrm{id}$. The system is astronomically large, which is why "just compute" fails.

**Reduction of degree (Bass–Connell–Wright 1982; Yagzhev 1980).** The general conjecture follows from the case
$$F = X + H, \qquad H = (H_1,\dots,H_N) \text{ homogeneous of degree } 3,$$
for all $N$. Equivalently, $JH$ is nilpotent (since $\det(I + JH) = 1$ with $JH$ homogeneous forces nilpotency).

**Drużkowski's cubic-linear form (1983).** One may further take
$$H_i(x) = (a_{i1}x_1 + \cdots + a_{iN}x_N)^3, \qquad A = (a_{ij}),$$
so $\mathrm{JC}$ is equivalent to: for every $N\times N$ matrix $A$ with $(A\,\mathrm{diag}(\ell_1^2,\dots))$ nilpotent — concretely, whenever $A\,D$ is nilpotent for all diagonal $D$ — the map $X + H$ is invertible. This turns the conjecture into a statement about nilpotency of matrix families.

**Symmetric reduction (de Bondt–van den Essen 2005).** It suffices to assume $JH$ is a *symmetric* matrix, i.e. $H = \nabla P$ for a homogeneous $P$ of degree $4$. So $\mathrm{JC}$ becomes: if $\det(I + \mathrm{Hess}\,P) = 1$ then $X + \nabla P$ is invertible.

**Dixmier equivalence.** Let $A_n(\mathbb{C})$ be the Weyl algebra with generators $p_i,q_i$, $[p_i,q_j]=\delta_{ij}$. The Dixmier conjecture $\mathrm{DC}_n$ asserts every endomorphism of $A_n$ is an automorphism. Tsuchimoto (2005) and Belov-Kanel–Kontsevich (2007) proved
$$\mathrm{JC}_{2n} \iff \mathrm{DC}_n,$$
so the two problems are stably equivalent.

**Vanishing/Mathieu–Zhao formulation (Zhao 2007).** $\mathrm{JC}$ is equivalent to: for a homogeneous $P$ of degree $4$ in $N$ variables with $\Delta^m(P^m) = 0$ for all $m\ge 1$ ($\Delta = \sum \partial^2/\partial x_i^2$), one has $\Delta^m(P^{m+1}) = 0$ for all $m \gg 0$.

## 3. History & State of the Art (SOTA)

- **1939.** Ott-Heinrich Keller, *Ganze Cremona-Transformationen*, asks the question for maps over $\mathbb{Z}$ with $\det JF = 1$.
- **1950s–70s.** Repeated false proofs; the problem acquires a reputation. Abhyankar and Moh develop the two-dimensional theory (Abhyankar–Moh embedding theorem, 1975: every embedding $\mathbb{A}^1 \hookrightarrow \mathbb{A}^2$ is rectifiable).
- **1980.** Yagzhev, and independently **1982** Bass–Connell–Wright, prove the reduction to cubic homogeneous maps in all dimensions — the single most-used structural result.
- **1980.** Wang: $\mathrm{JC}_n$ holds for all $n$ when $\deg F \le 2$.
- **1983.** Moh: $\mathrm{JC}_2$ holds for $\deg F \le 100$, by analysis of Newton polygons and approximate roots.
- **1983.** Drużkowski: cubic-linear reduction.
- **1998.** Smale lists it as **Problem 16** of his 18 mathematical problems for the next century.
- **2005–2007.** Tsuchimoto; Belov-Kanel–Kontsevich: stable equivalence with the Dixmier conjecture, linking $\mathrm{JC}$ to noncommutative algebra and to $p$-curvature methods in characteristic $p$.
- **2005.** de Bondt–van den Essen: symmetric reduction.
- **2007–present.** Zhao's Mathieu–Zhao space program recasts $\mathrm{JC}$ as a vanishing statement for the Laplacian, connecting it to the Mathieu conjecture on compact Lie groups.
- **Books.** van den Essen (2000) and van den Essen–Kuroda–Crachiola (2021) are the standard references.

## 4. Partial Results / Verified Cases

| Case | Result | Source |
|---|---|---|
| $\deg F \le 2$, any $n$ | True | Wang 1980 |
| $n = 2$, $\deg F \le 100$ | True | Moh 1983 |
| $n = 2$, $\deg F = p$ or $pq$ ($p,q$ prime) | True | Nagata; Appelgate–Onishi |
| $F$ cubic homogeneous, $n \le 3$ | True; $JH$ linearly triangularizable | Wright 1993 |
| Cubic-linear (Drużkowski), $n \le 4$ | True, by full classification | Hubbers 1994 |
| Cubic homogeneous, $n \le 5$ | True | de Bondt 2009 (thesis) |
| $JH$ symmetric with $\mathrm{rank}\,JH \le 2$ | True | de Bondt–van den Essen |
| $F$ proper / $k[x] $ finite over $k[F]$ | True | classical (Keller maps that are finite are automorphisms) |
| $F$ injective on $\mathbb{C}^n$ | Automorphism | Białynicki-Birula–Rosenlicht 1962 |
| $\deg F^{-1} \le (\deg F)^{n-1}$ | Proven bound | Bass–Connell–Wright 1982 |

Known *failures of neighbouring statements*, which bound what any proof may use: char $p>0$ ($x - x^p$); real polynomial maps $\mathbb{R}^2\to\mathbb{R}^2$ with $\det JF > 0$ everywhere but non-injective (Pinchuk 1994, degree 25 example); and the analytic analogue for entire maps $\mathbb{C}^n\to\mathbb{C}^n$.

## 5. Principal Obstacles

- **No induction on dimension.** $\mathrm{JC}_n$ does not visibly imply or follow from $\mathrm{JC}_{n-1}$; a Keller map does not restrict to Keller maps on hyperplanes. Every reduction (degree, symmetry, cubic-linear) *raises* the dimension $n \to N$ with $N$ uncontrolled, so results proven for small $N$ never accumulate into the general case.
- **Degree explosion.** The elimination approach is decidable for fixed $(n,d)$ but the inverse has degree up to $d^{n-1}$; Gröbner-basis certificates are doubly exponential. Moh's $d\le 100$ in dimension 2 is already near the limit of the Newton-polygon combinatorics.
- **No structure theory above dimension 2.** Jung–van der Kulk makes $\mathrm{GA}_2$ an amalgam, giving normal forms and a degree calculus. Shestakov–Umirbaev (2004) showed Nagata's automorphism is wild, so $\mathrm{GA}_3$ is *not* generated by affine and triangular maps: there is no normal form to induct on.
- **Topological/analytic methods only give local information.** $\det JF \ne 0$ makes $F$ a local biholomorphism and an open map, and $F(\mathbb{C}^n)$ is dense; the obstruction is that $F$ may fail to be proper, i.e. points can escape "to infinity" over a codimension-1 set. Controlling behaviour at infinity is exactly the missing ingredient, and compactifying $\mathbb{A}^n$ introduces indeterminacy loci one cannot resolve uniformly in $n$.
- **Positive-characteristic transfer is lossy.** $p$-curvature techniques (Tsuchimoto) reduce to reductions mod $p$, but the char-$p$ statement is *false*; one must track uniformity in $p$, and the known bounds degrade with degree.
- **Nilpotency does not imply triangularizability.** The cubic reduction asks whether nilpotent $JH$ forces $H$ to be conjugate to a triangular map. This is true for $n\le3$ but **false** in general: de Bondt and others exhibit nilpotent Jacobians that are not linearly triangularizable, killing the most natural strategy.

## 6. The Gap

Proven: $\mathrm{JC}_n$ for $\deg F \le 2$ (all $n$), for $n=2$ up to degree $100$, and for cubic homogeneous/cubic-linear maps in dimensions $\le 5$. Wanted: a statement uniform in *both* $n$ and $d$.

The precise barrier is a single implication:

> For $H$ homogeneous of degree $3$ in $N$ variables with $JH$ nilpotent, show $X+H$ is injective — with an argument whose input is only the nilpotency of $JH$, not a classification of $H$.

Every known proof of a case proceeds by classifying the possible $A$ (or $H$) up to linear conjugacy; the number of orbits grows without bound with $N$, so classification cannot close the gap. Equivalently, in Zhao's formulation, the gap is the step from "$\Delta^m(P^m)=0$ for all $m$" to "$\Delta^m(P^{m+1})=0$ for $m\gg0$" — from a nilpotency condition to an eventual-vanishing condition, with no known mechanism converting one to the other.

## 7. Current Research (as of June 2026)

- **Mathieu–Zhao spaces.** Wenhua Zhao (Illinois State) and collaborators continue to develop MZ-subspaces of associative algebras, the framework in which $\mathrm{JC}$ becomes a vanishing statement; recent work targets the image-of-derivation and idempotency conjectures. *(frontier — verify)*
- **Nijmegen school.** Arno van den Essen, Michiel de Bondt, and co-workers pursue homogeneous and symmetric Keller maps, classifying nilpotent Jacobians in higher dimensions and producing counterexamples to intermediate conjectures (e.g. to linear triangularizability, and to the "$JH$ nilpotent $\Rightarrow$ tame" heuristic).
- **Noncommutative route.** Following Belov-Kanel–Kontsevich, work on automorphisms of the Weyl algebra, the "$\mathrm{Aut}(A_n) \cong \mathrm{Aut}(P_n)$" (Poisson) conjecture, and quantization-based approaches. Kontsevich's proposed canonical correspondence remains unfinished. *(frontier — verify)*
- **Tropical and valuation methods** for $n=2$, extending Moh's degree bound via key polynomials and valuations centred at infinity; incremental degree improvements are reported but no published bound has displaced $d \le 100$ as the standard citation. *(frontier — verify)*
- **Perennial false proofs.** Multiple preprints claiming a full proof appear annually; none has survived refereeing. Treat any such claim as unverified until published with independent confirmation.

## 8. Future Work

- **Find an $N$-uniform invariant.** Something attached to $H$ (a valuation at infinity, a filtration, a degree function on $\mathrm{GA}_N$) that decreases under composition and is bounded below — the amalgam structure supplies exactly this in $n=2$.
- **Properness at infinity.** Prove that a Keller map is proper, or characterize the "asymptotic variety" $S_F$ (the set where $F$ fails to be proper) and show $\det JF$ constant forces $S_F=\emptyset$. Jelonek's theory of the set of non-properness is the main tool.
- **Uniform char-$p$ control.** Exploit $\mathrm{JC}_{2n} \iff \mathrm{DC}_n$: prove the Dixmier conjecture using $p$-curvature with bounds uniform in $p$, avoiding the char-$p$ counterexamples.
- **Settle Zhao's vanishing conjecture** for the Laplacian on quartic forms, even for restricted classes (e.g. $P$ a sum of fourth powers of linear forms — precisely the Drużkowski case).
- **Push $n=2$ beyond degree 100** with computer-assisted Newton-polygon analysis, ideally to an argument independent of the degree.
- **Search for counterexamples** systematically in the cubic-linear family: classify nilpotent $A$ in dimension $6$–$10$, the first range where the classification-based proofs break down.

## 9. Key References

- **[Foundational]** O.-H. Keller. *Ganze Cremona-Transformationen.* Monatshefte für Mathematik und Physik **47** (1939), 299–306. [DOI](https://doi.org/10.1007/bf01695502)
- **[Foundational]** H. Bass, E. H. Connell, D. Wright. *The Jacobian conjecture: reduction of degree and formal expansion of the inverse.* Bulletin of the American Mathematical Society **7** (1982), 287–330. [DOI](https://doi.org/10.1090/s0273-0979-1982-15032-7)
- **[Foundational]** A. Białynicki-Birula, M. Rosenlicht. *Injective morphisms of real algebraic varieties.* Proceedings of the AMS **13** (1962), 200–203. [DOI](https://doi.org/10.2307/2034464)
- S. S.-S. Wang. *A Jacobian criterion for separability.* Journal of Algebra **65** (1980), 453–494. [DOI](https://doi.org/10.1016/0021-8693(80)90233-1)
- A. V. Yagzhev. *On Keller's problem.* Siberian Mathematical Journal **21** (1980), 747–754.
- T.-T. Moh. *On the Jacobian conjecture and the configurations of roots.* Journal für die reine und angewandte Mathematik **340** (1983), 140–212. [DOI](https://doi.org/10.1515/crll.1983.340.140)
- L. M. Drużkowski. *An effective approach to Keller's Jacobian conjecture.* Mathematische Annalen **264** (1983), 303–313. [DOI](https://doi.org/10.1007/bf01459126)
- D. Wright. *The Jacobian conjecture: linear triangularization for cubics in dimension three.* Linear and Multilinear Algebra **34** (1993), 85–97. [DOI](https://doi.org/10.1080/03081089308818214)
- S. Pinchuk. *A counterexample to the strong real Jacobian conjecture.* Mathematische Zeitschrift **217** (1994), 1–4.
- **[Survey / Book]** A. van den Essen. *Polynomial Automorphisms and the Jacobian Conjecture.* Progress in Mathematics **190**, Birkhäuser, 2000. [DOI](https://doi.org/10.2307/3621827)
- **[SOTA]** M. de Bondt, A. van den Essen. *A reduction of the Jacobian conjecture to the symmetric case.* Proceedings of the AMS **133** (2005), 2201–2205. [DOI](https://doi.org/10.1090/s0002-9939-05-07570-2)
- **[SOTA]** Y. Tsuchimoto. *Endomorphisms of Weyl algebra and $p$-curvatures.* Osaka Journal of Mathematics **42** (2005), 435–452.
- **[SOTA]** A. Belov-Kanel, M. Kontsevich. *The Jacobian conjecture is stably equivalent to the Dixmier conjecture.* Moscow Mathematical Journal **7** (2007), 209–218. [DOI](https://doi.org/10.17323/1609-4514-2007-7-2-209-218)
- **[SOTA]** W. Zhao. *A vanishing conjecture on differential operators with constant coefficients.* Acta Mathematica Vietnamica **32** (2007), 259–286.
- I. Shestakov, U. Umirbaev. *The tame and the wild automorphisms of polynomial rings in three variables.* Journal of the AMS **17** (2004), 197–227. [DOI](https://doi.org/10.1090/s0894-0347-03-00440-5)
- S. Smale. *Mathematical problems for the next century.* The Mathematical Intelligencer **20** (1998), 7–15. [DOI](https://doi.org/10.1007/bf03025291)
- **[Survey / Book]** A. van den Essen, S. Kuroda, A. J. Crachiola. *Polynomial Automorphisms and the Jacobian Conjecture: New Results from the Beginning of the 21st Century.* Frontiers in Mathematics, Birkhäuser, 2021.

## 10. Worked Example / Concrete Special Case

**A cubic-linear Keller map in dimension 2, inverted explicitly.**

Let $u = x + y$ and set
$$F(x,y) = \bigl(\,x + u^3,\ \ y - u^3\,\bigr) = \bigl(x + (x+y)^3,\ y - (x+y)^3\bigr).$$
This is exactly Drużkowski's form $X + H$ with $H_i = (a_i\cdot x)^3$, $a_1 = (1,1)$, $a_2 = -(1,1)$ up to sign.

*Step 1 — the Jacobian.* With $\partial u/\partial x = \partial u/\partial y = 1$,
$$JF = \begin{pmatrix} 1 + 3u^2 & 3u^2 \\ -3u^2 & 1 - 3u^2 \end{pmatrix},$$
$$\det JF = (1+3u^2)(1-3u^2) + 9u^4 = 1 - 9u^4 + 9u^4 = 1.$$
So $F$ is a Keller map.

*Step 2 — nilpotency.* Here
$$JH = 3u^2\begin{pmatrix} 1 & 1 \\ -1 & -1\end{pmatrix}, \qquad (JH)^2 = 9u^4\begin{pmatrix}1&1\\-1&-1\end{pmatrix}^2 = 0,$$
confirming the general fact that $\det(I+JH)=1$ with $JH$ homogeneous forces $JH$ nilpotent.

*Step 3 — inversion.* Write $(X,Y) = F(x,y)$. Then
$$X + Y = (x + u^3) + (y - u^3) = x + y = u.$$
The cubic terms cancel: the linear form $u$ is a *first integral* of the map. Hence
$$G(X,Y) = \bigl(X - (X+Y)^3,\ Y + (X+Y)^3\bigr)$$
and $G(F(x,y)) = (x + u^3 - u^3,\ y - u^3 + u^3) = (x,y)$. So $F \in \mathrm{GA}_2(\mathbb{C})$, with $\deg F = \deg F^{-1} = 3$, matching the bound $\deg F^{-1} \le d^{\,n-1} = 3^1 = 3$.

*Step 4 — why this does not generalize.* The proof used one accident: the row vectors $a_1,a_2$ of the linear part of $H$ are proportional, so a single linear form $u$ is invariant and $F$ is linearly conjugate to a triangular map ($u \mapsto u$, $x \mapsto x + u^3$). Wright (1993) showed every nilpotent cubic $JH$ in dimension $\le 3$ is linearly triangularizable this way. In dimension $\ge 4$ there exist nilpotent $JH$ admitting **no** invariant linear form, so no chain of one-variable substitutions inverts them, and the argument above has no analogue. That failure is precisely the content of Section 6.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*