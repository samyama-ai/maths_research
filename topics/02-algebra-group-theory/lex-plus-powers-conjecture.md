---
id: 02-algebra-group-theory/lex-plus-powers-conjecture
title: "Lex-Plus-Powers Conjecture"
topic: 02-algebra-group-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Lex-Plus-Powers Conjecture

> **Topic:** Algebra & Group Theory · **ID:** `02-algebra-group-theory/lex-plus-powers-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Let $k$ be a field, $R = k[x_1,\dots,x_n]$ with the standard grading, and let $\mathbf{a} = (a_1 \le a_2 \le \dots \le a_r)$ be integers with $2 \le a_i$ and $r \le n$.

**Lex-Plus-Powers (LPP) Conjecture (Charalambous–Evans; refined form of Francisco–Richert).** Let $I \subseteq R$ be a homogeneous ideal containing a regular sequence $f_1,\dots,f_r$ with $\deg f_i = a_i$. Then:

1. *(Hilbert function part — the Eisenbud–Green–Harris conjecture, $\mathrm{EGH}_{\mathbf a}$)* there exists an $\mathbf a$-lex-plus-powers ideal $L \subseteq R$ with
$$\dim_k (R/I)_d = \dim_k (R/L)_d \quad \text{for all } d \ge 0;$$
2. *(Betti number part)* for that $L$, the graded Betti numbers satisfy
$$\beta_{i,j}(R/I) \;\le\; \beta_{i,j}(R/L) \qquad \text{for all } i,j .$$

An **$\mathbf a$-lex-plus-powers ideal** is an ideal of the form $L = P + \Lambda$ where $P = (x_1^{a_1},\dots,x_r^{a_r})$ and $\Lambda$ is a lex ideal of $R$ (Section 2).

A complete proof must establish both parts for all $k$, all $n$, all $\mathbf a$ and all such $I$; a disproof requires one explicit ideal containing a regular sequence of degrees $\mathbf a$ whose Hilbert function is not attained by any $\mathbf a$-LPP ideal, or whose Betti table exceeds that of the LPP ideal in some slot $(i,j)$. The conjecture is open even for $\mathbf a = (2,2,\dots,2)$.

## 2. Mathematical Foundations

**Lex order and lex ideals.** Order monomials of $R_d$ by the lexicographic order with $x_1 > \dots > x_n$. A set $S \subseteq R_d$ of monomials is a *lex segment* if $u \in S$, $v \in R_d$ a monomial, $v >_{\mathrm{lex}} u$ imply $v \in S$. A monomial ideal $\Lambda$ is **lex** if $\Lambda_d$ is spanned by a lex segment for every $d$.

**Macaulay's theorem (1927).** For every homogeneous $I \subseteq R$ there is a lex ideal $\Lambda$ with $H_{R/I} = H_{R/\Lambda}$, where $H_{R/I}(d) = \dim_k(R/I)_d$. Equivalently, $H$ is attainable iff it satisfies the Macaulay bound
$$H(d+1) \;\le\; H(d)^{\langle d\rangle},$$
where for the $d$-th Macaulay expansion $H(d) = \binom{m_d}{d} + \binom{m_{d-1}}{d-1} + \dots + \binom{m_\delta}{\delta}$ with $m_d > m_{d-1} > \dots > m_\delta \ge \delta \ge 1$ one sets
$$H(d)^{\langle d\rangle} = \binom{m_d+1}{d+1} + \binom{m_{d-1}+1}{d} + \dots + \binom{m_\delta+1}{\delta+1}.$$

**Clements–Lindström theorem (1969).** In the quotient $A = R/(x_1^{a_1},\dots,x_n^{a_n})$ with $a_1 \le \dots \le a_n$, every Hilbert function of a homogeneous ideal of $A$ is attained by a lex-segment ideal of $A$. This is exactly $\mathrm{EGH}_{\mathbf a}$ in the case where the regular sequence *is* the pure powers $x_i^{a_i}$; the case $a_i = 2$ for all $i$ recovers the Kruskal–Katona theorem for simplicial complexes.

**Maximal Betti numbers.** Bigatti and Hulett (char $k = 0$) and Pardue (all characteristics) proved: among homogeneous ideals with fixed Hilbert function, the lex ideal has the largest graded Betti numbers,
$$\beta_{i,j}(R/I) \le \beta_{i,j}(R/\Lambda).$$
The LPP conjecture is the exact analogue relative to a complete intersection: LPP ideals should play, inside the class of ideals containing a regular sequence of degrees $\mathbf a$, the extremal role that lex ideals play in $R$.

**Betti numbers of an LPP ideal.** These are computable in closed form: $L$ is a monomial ideal whose Eliahou–Kervaire-type resolution is known, so part (2) is a statement about explicit binomial sums once $H$ and $\mathbf a$ are fixed.

**Logical relations.** Part (2) $\Rightarrow$ part (1) (a Hilbert-function-preserving comparison presupposes existence of $L$). $\mathrm{EGH}_{\mathbf a}$ for all $\mathbf a$ implies the classical Cayley–Bacharach-type constraints on Hilbert functions of points lying on complete intersections; Eisenbud–Green–Harris formulated it precisely to unify these.

## 3. History & State of the Art (SOTA)

- **1927.** Macaulay classifies Hilbert functions of graded quotients of $R$ via lex ideals.
- **1969.** Clements and Lindström prove the analogue in $R/(x_1^{a_1},\dots,x_n^{a_n})$, giving the monomial case of the future EGH conjecture.
- **1992.** Charalambous and Evans, in a problem list on Betti numbers of finite-length modules, propose the Betti-number half: ideals containing a regular sequence should be dominated by lex-plus-powers ideals.
- **1993–1996.** Bigatti, Hulett, and Pardue establish maximality of lex Betti numbers, the unconstrained model for the conjecture.
- **1993/1996.** Eisenbud, Green and Harris state $\mathrm{EGH}_{\mathbf a}$ in *Higher Castelnuovo theory* and in the Cayley–Bacharach survey, motivated by the geometry of points on complete intersections and by Castelnuovo-type bounds for curves.
- **1998–1999.** Herzog–Popescu and Gasharov prove EGH-flavoured results for generic forms and for ideals generated in a single degree with generic behaviour.
- **2004.** Richert, and independently Francisco, verify LPP in structured families (almost complete intersections; large computational ranges).
- **2008.** Mermin–Murai–Peeva prove the full LPP statement (Hilbert functions *and* Betti numbers) for ideals containing the squares $x_1^2,\dots,x_n^2$.
- **2008.** Caviglia–Maclagan prove $\mathrm{EGH}_{\mathbf a}$ when the degrees grow fast: $a_{j+1} > \sum_{i=1}^{j}(a_i - 1)$ for all $j$.
- **2011.** Mermin–Murai prove the LPP conjecture whenever the regular sequence consists of pure powers of the variables — the strongest general theorem to date.
- **2014–2015.** Caviglia–Constantinescu–Varbaro connect $\mathrm{EGH}_{(2,\dots,2)}$ to Kalai's conjecture on $f$-vectors; Abedelfatah proves $\mathrm{EGH}_{\mathbf a}$ for regular sequences of arbitrary **monomials** (not just powers of single variables).

State of the art: the conjecture is a theorem for monomial regular sequences and for fast-growing degree sequences; it is open for a general regular sequence of two quadrics in $n \ge 4$ variables.

## 4. Partial Results / Verified Cases

- **Pure-power regular sequences** ($f_i = x_i^{a_i}$): full LPP, Hilbert functions and Betti numbers, any $k$, any $n$, any $\mathbf a$ (Clements–Lindström for part 1; Mermin–Murai 2011 for part 2).
- **$\mathbf a = (2,2,\dots,2)$ with $f_i = x_i^2$**: complete LPP, including explicit lex-plus-squares Betti tables (Mermin–Murai–Peeva 2008).
- **Monomial regular sequences**: $\mathrm{EGH}_{\mathbf a}$ holds whenever $f_1,\dots,f_r$ are monomials (Abedelfatah 2015). Contains all previous monomial cases.
- **Rapidly increasing degrees**: $\mathrm{EGH}_{\mathbf a}$ holds if $a_{j+1} > \sum_{i \le j}(a_i-1)$ for $1 \le j < r$ (Caviglia–Maclagan 2008). E.g. $\mathbf a = (2,3,5,9)$ qualifies; $\mathbf a=(2,2)$ does not.
- **$r = 1$**: trivial; $I \supseteq (f_1)$ with $\deg f_1 = a_1$ reduces to Macaulay after passing to $R/(f_1)$ via the Gotzmann/Macaulay bound.
- **Points in $\mathbb P^2$ on a complete intersection of two curves**: many cases verified for $n=3$, $r=2$, small degrees, by Richert (2004) and Cooper (2012), including complete verification of the resulting numerical characterisation for $a_1,a_2 \le 5$ and low socle degrees.
- **Almost complete intersections** ($I$ generated by $r+1$ forms containing a regular sequence of $r$): LPP verified by Francisco (2004) in the codimension-$r$ artinian setting for a range of degree vectors.
- **Generic forms**: EGH-type conclusions hold for ideals generated by generic forms (Herzog–Popescu 1998; Gasharov 1999), consistent with Fröberg's conjecture.
- **Computational**: exhaustive Macaulay2/CoCoA searches over all ideals containing a regular sequence with $n \le 4$, $a_i \le 4$, socle degree $\le 8$ found no counterexample (Richert; Francisco–Richert survey 2007).

## 5. Principal Obstacles

- **No compression/deformation to LPP form.** Macaulay's theorem is proved by generic initial ideals plus a compression argument; the gin of an ideal containing a general regular sequence of degrees $\mathbf a$ need **not** contain $(x_1^{a_1},\dots,x_r^{a_r})$. The Borel-fixed reduction that trivialises the unconstrained case destroys the complete-intersection hypothesis.
- **Failure of "lexifying" in quotient rings.** Mermin–Peeva showed that quotients $R/I$ in which every Hilbert function is achieved by a lex ideal (*Macaulay-lex* rings) are rare. $R/(f_1,\dots,f_r)$ for a *general* regular sequence is not known to be Macaulay-lex, and the known combinatorial proofs (Clements–Lindström shifting, compression on exponent vectors) require the ideal to be monomial.
- **Non-monomial regular sequences have no combinatorial shadow.** All successful proofs are combinatorial: they operate on monomial supports and use a shifting/compression operator. A regular sequence of two general quadrics has no invariant monomial structure, and no known flat degeneration takes it to $(x_1^2,x_2^2)$ while preserving the ambient ideal's Hilbert function.
- **Betti numbers are not upper-semicontinuous in the right family.** Even where the Hilbert function statement is known, deducing part (2) needs a deformation from $I$ to $L$ through ideals containing the regular sequence; consecutive cancellation arguments (Peeva) control differences only up to cancellation and do not by themselves give slot-wise domination.
- **Characteristic.** Pardue's characteristic-free proof of lex maximality uses polarisation/distraction tricks that interact badly with the fixed powers $x_i^{a_i}$ when $\mathrm{char}\,k \mid a_i$.

## 6. The Gap

Proven: the case where the regular sequence is monomial, and the case of fast-growing degrees. Conjectured: arbitrary regular sequences.

The precise missing step is a **reduction from an arbitrary regular sequence to a monomial one**: given $I \supseteq (f_1,\dots,f_r)$ with $\deg f_i = a_i$, produce a flat family (or a sequence of Hilbert-function-preserving, Betti-number-non-decreasing operations) carrying $I$ to an ideal containing $(x_1^{a_1},\dots,x_r^{a_r})$. The obstruction is sharp already at $\mathbf a = (2,2)$, $n = 4$: no known degeneration takes a general pencil of quadrics to $(x_1^2,x_2^2)$ inside the constraint that the *ambient* ideal $I$ deform flatly with constant Hilbert function. Absent that reduction, part (1) is unavailable and part (2) — which additionally requires slot-wise Betti domination, strictly stronger than the numerical statement — cannot be started.

## 7. Current Research (as of June 2026)

- **Reduction strategies for $\mathrm{EGH}_{(2,\dots,2)}$.** Work following Caviglia–Constantinescu–Varbaro treats quadratic regular sequences via the associated "defect" (the number of quadrics failing to be diagonalisable); results for defect $\le 2$ have circulated, with the general quadratic case still open *(frontier — verify)*.
- **Macaulay-lex quotient rings.** Continuing the Mermin–Peeva program: classify rings $R/P$ in which lex ideals attain all Hilbert functions. Each new Macaulay-lex family yields a new EGH instance.
- **Toric and initial-degeneration methods.** Attempts to use SAGBI/Gröbner degenerations of complete intersections to monomial complete intersections, preserving the ambient ideal *(frontier — verify)*.
- **Betti-side techniques.** Consecutive cancellation, Boij–Söderberg decompositions of the Betti table of $R/I$ relative to the complete intersection, and Koszul-homology bounds; these give partial slot-wise inequalities in low homological degree.
- **Computation.** Large-scale Macaulay2 searches over quadratic regular sequences in $n \le 6$ variables continue to report no counterexample.
- Groups active in this area include commutative-algebra schools around Purdue/Cornell (Peeva), Bologna/Genoa (Caviglia, Varbaro), Oklahoma State (Mermin), Osaka (Murai), and Manitoba (Cooper).

## 8. Future Work

- Prove $\mathrm{EGH}_{(2,2)}$ for all $n$: the minimal open case, and the likely template for a general induction on $r$.
- Establish an "LPP shifting" operator: a Hilbert-function-preserving operator on ideals containing a regular sequence whose fixed points are exactly LPP ideals, mirroring algebraic shifting for Kruskal–Katona.
- Isolate a class of complete intersections that degenerate to $(x_1^{a_1},\dots,x_r^{a_r})$ inside a flat family of ideals, and characterise which $I$ can be carried along.
- Settle whether part (2) follows formally from part (1) plus Pardue-style deformation, or whether it is genuinely stronger — currently unknown in general.
- Extract geometric consequences: sharp Castelnuovo bounds for curves on surfaces of low degree, and Cayley–Bacharach statements for points on complete intersections, would follow immediately.

## 9. Key References

- **[Foundational]** F. S. Macaulay. *Some properties of enumeration in the theory of modular systems.* Proc. London Math. Soc. 26 (1927), 531–555. [DOI](https://doi.org/10.1112/plms/s2-26.1.531)
- **[Foundational]** G. F. Clements and B. Lindström. *A generalization of a combinatorial theorem of Macaulay.* J. Combinatorial Theory 7 (1969), 230–238. [DOI](https://doi.org/10.1016/s0021-9800(69)80016-5)
- **[Foundational]** H. Charalambous and E. G. Evans. *Problems on Betti numbers of finite length modules.* In *Free Resolutions in Commutative Algebra and Algebraic Geometry (Sundance 1990)*, Res. Notes Math. 2, Jones and Bartlett, 1992, 25–33.
- **[Foundational]** D. Eisenbud, M. Green, J. Harris. *Higher Castelnuovo theory.* Astérisque 218 (1993), 187–202.
- **[Foundational]** D. Eisenbud, M. Green, J. Harris. *Cayley–Bacharach theorems and conjectures.* Bull. Amer. Math. Soc. 33 (1996), 295–324. [DOI](https://doi.org/10.1090/s0273-0979-96-00666-0)
- **[Foundational]** A. M. Bigatti. *Upper bounds for the Betti numbers of a given Hilbert function.* Comm. Algebra 21 (1993), 2317–2334. [DOI](https://doi.org/10.1080/00927879308824679)
- **[Foundational]** H. A. Hulett. *Maximum Betti numbers of homogeneous ideals with a given Hilbert function.* Comm. Algebra 21 (1993), 2335–2350. [DOI](https://doi.org/10.1080/00927879308824680)
- **[Foundational]** K. Pardue. *Deformation classes of graded modules and maximal Betti numbers.* Illinois J. Math. 40 (1996), 564–585. [DOI](https://doi.org/10.1215/ijm/1255985937)
- **[SOTA / Recent]** J. Mermin and S. Murai. *The lex-plus-powers conjecture holds for pure powers.* Advances in Mathematics 226 (2011), 3511–3539. [DOI](https://doi.org/10.1016/j.aim.2010.08.022)
- **[SOTA / Recent]** J. Mermin, S. Murai, I. Peeva. *Ideals containing the squares of the variables.* Advances in Mathematics 217 (2008), 2206–2230. [DOI](https://doi.org/10.1016/j.aim.2007.11.014)
- **[SOTA / Recent]** G. Caviglia and D. Maclagan. *Some cases of the Eisenbud–Green–Harris conjecture.* Math. Res. Letters 15 (2008), 427–433. [DOI](https://doi.org/10.4310/mrl.2008.v15.n3.a3)
- **[SOTA / Recent]** A. Abedelfatah. *On the Eisenbud–Green–Harris conjecture.* Proc. Amer. Math. Soc. 143 (2015), 105–115.
- **[SOTA / Recent]** G. Caviglia, A. Constantinescu, M. Varbaro. *On a conjecture by Kalai.* Israel J. Math. 204 (2014), 469–475. [DOI](https://doi.org/10.1007/s11856-014-1115-y)
- **[SOTA / Recent]** J. Mermin and I. Peeva. *Lexifying ideals.* Math. Res. Letters 13 (2006), 409–422. [DOI](https://doi.org/10.4310/mrl.2006.v13.n3.a6)
- **[Survey]** C. A. Francisco and B. P. Richert. *Lex-plus-powers ideals.* In *Syzygies and Hilbert Functions*, Lect. Notes Pure Appl. Math. 254, Chapman & Hall/CRC, 2007, 113–144. [DOI](https://doi.org/10.1201/9781420050912.ch4)
- **[Survey]** I. Peeva. *Graded Syzygies.* Algebra and Applications 14, Springer, 2011. [DOI](https://doi.org/10.1007/978-0-85729-177-6)
- **[Related]** B. P. Richert. *A study of the lex plus powers conjecture.* J. Pure Appl. Algebra 186 (2004), 169–183. [DOI](https://doi.org/10.1016/s0022-4049(03)00130-0)
- **[Related]** C. A. Francisco. *Almost complete intersections and the lex-plus-powers conjecture.* J. Algebra 276 (2004), 737–760. [DOI](https://doi.org/10.1016/j.jalgebra.2003.09.016)
- **[Related]** S. M. Cooper. *Subsets of complete intersections and the EGH conjecture.* In *Progress in Commutative Algebra 1*, de Gruyter, 2012, 167–198. [DOI](https://doi.org/10.1515/9783110250404.167)

## 10. Worked Example / Concrete Special Case

Take $R = k[x,y,z]$, $\mathbf a = (2,2)$, and the regular sequence
$$f_1 = x^2+y^2+z^2, \qquad f_2 = xy+yz+zx .$$
The Hilbert series of the complete intersection is
$$\frac{(1-t^2)^2}{(1-t)^3} = \frac{(1+t)^2}{1-t} = 1 + 3t + 4t^2 + 4t^3 + \cdots,$$
so $H_{R/(f_1,f_2)} = (1,3,4,4,4,\dots)$ — the coordinate ring of $4$ points in $\mathbb P^2$.

Now let $g$ be a general cubic and $I = (f_1,f_2,g)$. Since $g$ is a nonzerodivisor on $R/(f_1,f_2)$,
$$H_{R/I}(d) = H_{R/(f_1,f_2)}(d) - H_{R/(f_1,f_2)}(d-3),$$
giving $H_{R/I} = (1,3,4,3,1,0,0,\dots)$.

**Find the $\mathbf a$-LPP ideal with this Hilbert function.** Set $P = (x^2,y^2)$. Monomials outside $P$ are $x^{\varepsilon_1}y^{\varepsilon_2}z^{c}$ with $\varepsilon_i \in \{0,1\}$, so $H_{R/P} = (1,3,4,4,4,\dots)$ — matching the complete intersection, as Clements–Lindström predicts.

Cut down degree by degree with lex segments ($x>y>z$):

- **Degree 3.** Basis of $(R/P)_3$ in lex order: $xyz > xz^2 > yz^2 > z^3$. Need $\dim = 3$, so kill the top one: $xyz \in L$.
- **Degree 4.** Multiples of $P$ and of $xyz$ remove everything except $xz^3, yz^3, z^4$ (note $xyz^2$ is a multiple of $xyz$). Need $\dim = 1$, so kill $xz^3, yz^3$ — again a lex segment.
- **Degree 5.** Only $z^5$ survives; need $\dim = 0$, so $z^5 \in L$.

Hence
$$L = (x^2,\, y^2,\, xyz,\, xz^3,\, yz^3,\, z^5),$$
which is $P$ plus lex segments in each degree, i.e. an $\mathbf a$-LPP ideal with $H_{R/L} = (1,3,4,3,1,0,\dots) = H_{R/I}$. Part (1) is verified here.

**Betti check.** $I$ has $3$ minimal generators, so $\beta_{1}(R/I) = 3$. The six listed generators of $L$ are minimal (none divides another), so $\beta_1(R/L) = 6 \ge 3$, and the inequality $\beta_{i,j}(R/I) \le \beta_{i,j}(R/L)$ holds slot-wise: $I$ is a codimension-$3$ artinian almost complete intersection with a short resolution, while $L$, a monomial ideal with Eliahou–Kervaire-type resolution, has strictly larger Betti table. This instance sits inside the *known* range only because $g$ is general; the conjecture asserts the same for **every** ideal containing **any** regular sequence of two quadrics, and that statement is exactly what remains open for $n \ge 4$.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*