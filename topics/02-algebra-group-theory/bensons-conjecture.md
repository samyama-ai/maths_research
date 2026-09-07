---
id: 02-algebra-group-theory/bensons-conjecture
title: "Benson's Conjecture"
topic: 02-algebra-group-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Benson's Conjecture

> **Topic:** Algebra & Group Theory · **ID:** `02-algebra-group-theory/bensons-conjecture` · **Status:** open (in its general form; the finite-group case is a theorem of Symonds, 2010)

## 1. Problem Statement / Conjecture

Benson's Conjecture — the **regularity conjecture for group cohomology** — asserts that the Castelnuovo–Mumford regularity of the mod-$p$ cohomology ring of a finite group vanishes:

$$\operatorname{Reg} H^*(G;k) = 0,$$

where $G$ is a finite group and $k$ a field of characteristic $p>0$, and regularity is computed by local cohomology with respect to the maximal ideal of positive-degree elements.

Status of the claim, stated flatly:

- **Finite groups: proved.** Symonds (2010) established $\operatorname{Reg} H^*(G;k)=0$ for every finite group $G$ and every field $k$ of positive characteristic.
- **Open in the generality Benson posed the question.** The same statement for **finite group schemes** (equivalently, finite-dimensional cocommutative Hopf algebras), for **compact Lie groups and $p$-compact groups**, and for **profinite / virtual-duality groups** with Noetherian cohomology, is not known. Nor is the module-level strengthening $\operatorname{Reg} H^*(G;M)\le 0$ known uniformly in $M$, nor the sharp form of the resulting degree bound on generators (Symonds' bound $|G|$ is believed to be far from optimal).

A complete resolution of the open part requires either a proof of $\operatorname{Reg}\, H^*(\mathcal{G};k)=0$ for an arbitrary finite group scheme $\mathcal{G}$ over $k$, or a counterexample: a $\mathcal{G}$ and an index $i$ with $a_i\big(H^*(\mathcal{G};k)\big)+i>0$.

## 2. Mathematical Foundations

Let $k$ be a field of characteristic $p$, $G$ a finite group, and
$$H^*(G;k)=\operatorname{Ext}^*_{kG}(k,k),$$
a graded-commutative $k$-algebra (strictly commutative for $p=2$). By **Venkov (1959)** and **Evens (1961)**, $H^*(G;k)$ is a finitely generated $k$-algebra; by **Quillen (1971)**,
$$\dim H^*(G;k) \;=\; r_p(G) \;=\; \max\{\, r : (\mathbb{Z}/p)^r \hookrightarrow G \,\},$$
the $p$-rank. Write $\mathfrak{m}=H^{>0}(G;k)$ and let $H^i_{\mathfrak m}(-)$ denote local cohomology at $\mathfrak m$. For a graded module $M$ set
$$a_i(M)=\max\{\, n : H^i_{\mathfrak m}(M)^n\neq 0 \,\}\quad(-\infty \text{ if } H^i_{\mathfrak m}(M)=0),$$
$$\operatorname{Reg}(M)=\max_i\{\, a_i(M)+i \,\}.$$
Here the grading convention is cohomological, so $a_i$ is a **top** degree, not a bottom one; the inequality $\operatorname{Reg} H^*(G;k)\ge 0$ is elementary, and the content of the conjecture is $\operatorname{Reg}\le 0$.

**Cohen–Macaulay reformulation.** Let $\zeta_1,\dots,\zeta_r$ be a homogeneous system of parameters (hsop) with $\deg\zeta_i=d_i$. If $H^*(G;k)$ is Cohen–Macaulay, it is free over $k[\zeta_1,\dots,\zeta_r]$, local cohomology is concentrated in degree $r$, and
$$\operatorname{Reg}=0 \iff \max\{\, n : \big(H^*(G;k)/(\zeta_1,\dots,\zeta_r)\big)^n\neq 0 \,\}=\sum_{i=1}^{r}(d_i-1).$$
Equivalently, the Hilbert series factors as
$$\sum_{n\ge 0}\dim_k H^n(G;k)\,t^n=\frac{f(t)}{\prod_{i=1}^r (1-t^{d_i})},\qquad \deg f=\sum_i (d_i-1).$$
This is the Benson–Carlson duality picture: for Cohen–Macaulay cohomology, $f$ additionally satisfies $t^{\deg f}f(1/t)=f(t)$.

**Depth input.** **Duflot (1981)**: $\operatorname{depth} H^*(G;\mathbb{F}_p)\ \ge\ r_p\big(Z(S)\big)$ for $S\in\operatorname{Syl}_p(G)$. The gap $r_p(G)-\operatorname{depth}$ measures how far the ring is from Cohen–Macaulay and controls how many local cohomology modules $H^i_{\mathfrak m}$ can be nonzero.

**Computational bridge.** Greenlees' local cohomology spectral sequence
$$E_2^{i,j}=H^i_{\mathfrak m}\big(H^*(G;k)\big)^j \Longrightarrow H_{-i-j}(G;k)$$
converts regularity statements into statements about group homology in low degrees; it is the standard tool for extracting $a_i$ in worked cases, but it does not degenerate in general.

**Consequence of the conjecture.** Regularity $0$ forces degree bounds: Symonds deduced that $H^*(G;k)$ is generated as a $k$-algebra in degrees $\le |G|$, and that a system of parameters may be chosen in degrees $\le |G|$.

## 3. History & State of the Art (SOTA)

- **1959–1971.** Venkov and Evens prove finite generation; Quillen computes the Krull dimension and stratifies $\operatorname{Spec} H^*(G;\mathbb{F}_p)$ by elementary abelian subgroups. Finite generation gives no effective degree bounds.
- **1981.** Duflot's depth theorem supplies the only general lower bound on depth, hence the only general constraint on which $H^i_{\mathfrak m}$ vanish.
- **1990s.** Benson–Carlson duality for Cohen–Macaulay cohomology rings; Greenlees introduces local cohomology as the systematic language ("Commutative algebra in group cohomology", 1995), making "regularity $0$" the right uniform formulation of the observed duality.
- **2004–2008.** Benson states the conjecture explicitly in his MSRI survey and proves substantial cases in *On the regularity conjecture for the cohomology of finite groups* (Proc. Edinb. Math. Soc., 2008), notably under hypotheses limiting the codepth $r_p(G)-\operatorname{depth}$.
- **2010.** **Symonds** proves the conjecture for all finite groups (J. Amer. Math. Soc.), combining Quillen stratification, Duflot regular sequences, and regularity bounds for rings of invariants from Karagueuzian–Symonds. Corollary: generation in degrees $\le |G|$.
- **2010–present.** The research frontier moves to (i) finite group schemes and Hopf algebras, where Friedlander–Suslin finite generation is known but non-effective; (ii) sharpening $|G|$; (iii) module and triangulated-category versions in the Benson–Iyengar–Krause local-cohomology framework.

## 4. Partial Results / Verified Cases

- **All finite groups, all $p$ (Symonds 2010).** $\operatorname{Reg} H^*(G;k)=0$ unconditionally. This is the settled core.
- **Cohen–Macaulay cohomology.** Whenever $\operatorname{depth}=r_p(G)$ (e.g. $G$ with $p$-rank $1$: cyclic and, for $p=2$, generalized quaternion; abelian $p$-groups; $\mathbb{Z}/p\wr\mathbb{Z}/p$ cases), regularity $0$ is the classical Benson–Carlson duality and is checkable directly from the Hilbert series.
- **Codepth $\le 2$.** Benson (2008) proved $\operatorname{Reg}\le 0$ when $r_p(G)-\operatorname{depth} H^*(G;k)$ is small, using explicit analysis of the two or three possibly nonzero local cohomology modules.
- **Exhaustive computation.** Regularity $0$ was verified numerically for all groups of order dividing $64$ (Carlson–Townsley–Valeri-Elizondo–Zhang, 2003) and for all $2$-groups of order $128$ and all groups of order $\le 255$ via the Green–King computations (J. Algebra, 2011); regularity in those tables is always exactly $0$, never negative.
- **Elementary abelian and polynomial cases.** For $E=(\mathbb{Z}/p)^r$, $H^*(E;\mathbb{F}_p)$ is a (tensor of exterior and) polynomial ring and $\operatorname{Reg}=0$ by direct computation; likewise for groups whose cohomology is polynomial (Adem–Milgram classification of such $2$-groups).
- **Restricted Lie algebras of small rank.** For $\mathfrak{g}$ abelian restricted with $u(\mathfrak{g})=k[x_i]/(x_i^p)$, $H^*(u(\mathfrak g),k)$ is a tensor of a polynomial and an exterior algebra and regularity $0$ holds — the smallest group-scheme evidence.

## 5. Principal Obstacles

- **Finite generation is non-effective.** For finite group schemes, Friedlander–Suslin (1997) prove $H^*(\mathcal{G};k)$ Noetherian via strict polynomial functors and universal classes in $H^*(GL_n)$; the argument produces no bound on generator degrees, so it cannot even show $\operatorname{Reg}<\infty$ in an explicit form.
- **No classifying space.** Symonds' proof is geometric: it uses $BG$, Quillen's stratification by elementary abelian subgroups, and equivariant arguments on the associated Duflot free actions. A finite group scheme is not reduced; the correct "elementary abelian" analogues are $\pi$-points and infinitesimal one-parameter subgroups (Suslin–Friedlander–Bendel, Friedlander–Pevtsova), and these do not carry the degree-controlled Duflot regular sequences that the proof consumes.
- **The invariant-theoretic input does not transfer.** Karagueuzian–Symonds' bound on the module structure of a finite group acting on a polynomial ring is a statement about *finite groups* acting on $\operatorname{Sym}(V)$; there is no known counterpart for a finite group scheme acting on a graded algebra.
- **The local cohomology spectral sequence does not degenerate.** Greenlees' spectral sequence relates $a_i$ to low-degree homology, but differentials are uncontrolled once codepth exceeds $2$; this is exactly where hand computation stalls.
- **Sharpness is invisible to the method.** The bound "generated in degrees $\le|G|$" comes from combining $\operatorname{Reg}=0$ with a crude bound on parameter degrees. Known examples need degrees far below $|G|$, but no technique currently produces a bound polynomial in the order.

## 6. The Gap

The proven statement is: *for $G$ finite, $a_i(H^*(G;k))+i\le 0$ for all $i$*, proved by exhibiting, for each irreducible component of $\operatorname{Spec}H^*(G;k)$ (indexed by conjugacy classes of elementary abelian subgroups $E$), a Duflot regular sequence in bounded degree and controlling the resulting filtration by $H^*(E;k)^{W_G(E)}$-invariant-theory bounds.

The gap is precisely the step "*elementary abelian subgroups $\to$ degree-bounded Noether normalization*". For a finite group scheme $\mathcal{G}$, one has the stratification of $\operatorname{Spec}H^*(\mathcal{G};k)$ by $\pi$-points, but:

1. no analogue of Duflot's theorem giving a regular sequence in *bounded* degree;
2. no numerical invariant playing the role of $|G|$ against which to bound generator degrees;
3. no proof that the strata's invariant rings satisfy $\operatorname{Reg}\le 0$.

Closing any one of (1)–(3) in the group-scheme setting would likely close the conjecture there; a counterexample would have to be a $\mathcal{G}$ whose cohomology fails Benson–Carlson-type duality in an unbounded way.

## 7. Current Research (as of June 2026)

- **Group schemes and Hopf algebras.** Work in the Friedlander–Pevtsova school on $\pi$-support and the Balmer spectrum of $\operatorname{stmod}(k\mathcal{G})$ is the natural home of the open case; the aim is effective bounds on generator degrees for $\mathcal{G}$ infinitesimal of height $1$, i.e. for restricted enveloping algebras $u(\mathfrak g)$ — the case where a full proof of $\operatorname{Reg}=0$ looks nearest. *(frontier — verify)*
- **Triangulated local duality.** The Benson–Iyengar–Krause machinery (local cohomology and support for triangulated categories) reformulates regularity as a statement about the Gorenstein/duality behaviour of the stable module category; making "$\operatorname{Reg}=0$" a consequence of a category-level Gorenstein property is an active programme. *(frontier — verify)*
- **Sharpening the degree bound.** Aberdeen/Manchester-style work following Symonds asks for the true growth of the maximal generator degree of $H^*(G;\mathbb{F}_p)$ as a function of $|G|$; the conjectural answer is polynomial, and no superpolynomial family is known. *(frontier — verify)*
- **Computation.** Green–King's cohomology database and its successors continue to supply regularity data for $p$-groups of order $128$–$512$; all recorded values are $0$.

## 8. Future Work

- Prove a Duflot-type theorem for finite group schemes: exhibit a regular sequence on $H^*(\mathcal{G};k)$ of degrees bounded in terms of $\dim_k k\mathcal{G}$.
- Establish $\operatorname{Reg} H^*(u(\mathfrak g),k)=0$ for all restricted Lie algebras $\mathfrak g$, starting with $\mathfrak{gl}_n$ and its parabolic subalgebras.
- Settle the module version: is $\operatorname{Reg} H^*(G;M)\le 0$ for every finitely generated $kG$-module $M$, with bounds independent of $M$?
- Replace $|G|$ by a polynomial bound on generator degrees, or produce a family with generator degree growing faster than any polynomial in $|G|$.
- Extend to compact Lie groups and $p$-compact groups, where $H^*(BG;\mathbb{F}_p)$ is Noetherian and Duflot's theorem has an equivariant analogue.

## 9. Key References

- **[Foundational]** B. B. Venkov. *Cohomology algebras for some classifying spaces.* Doklady Akad. Nauk SSSR 127 (1959), 943–944.
- **[Foundational]** L. Evens. *The cohomology ring of a finite group.* Trans. Amer. Math. Soc. 101 (1961), 224–239.
- **[Foundational]** D. Quillen. *The spectrum of an equivariant cohomology ring, I & II.* Ann. of Math. 94 (1971), 549–572 and 573–602.
- **[Foundational]** J. Duflot. *Depth and equivariant cohomology.* Comment. Math. Helv. 56 (1981), 627–637.
- **[Foundational]** J. P. C. Greenlees. *Commutative algebra in group cohomology.* J. Pure Appl. Algebra 98 (1995), 151–162.
- **[Conjecture / Survey]** D. J. Benson. *Commutative algebra in the cohomology of groups.* In: Trends in Commutative Algebra, MSRI Publications 51, Cambridge Univ. Press, 2004, 1–50.
- **[Partial results]** D. J. Benson. *On the regularity conjecture for the cohomology of finite groups.* Proc. Edinburgh Math. Soc. 51 (2008), 273–284.
- **[SOTA]** P. Symonds. *On the Castelnuovo–Mumford regularity of the cohomology ring of a group.* J. Amer. Math. Soc. 23 (2010), 1159–1173.
- **[SOTA / invariant theory]** D. B. Karagueuzian and P. Symonds. *The module structure of a group action on a polynomial ring: a finiteness theorem.* J. Amer. Math. Soc. 20 (2007), 931–967.
- **[Group schemes]** E. M. Friedlander and A. Suslin. *Cohomology of finite group schemes over a field.* Invent. Math. 127 (1997), 209–270.
- **[Framework]** D. J. Benson, S. B. Iyengar, H. Krause. *Local cohomology and support for triangulated categories.* Ann. Sci. École Norm. Sup. 41 (2008), 573–619.
- **[Computation]** J. F. Carlson, L. Townsley, L. Valeri-Elizondo, M. Zhang. *Cohomology Rings of Finite Groups.* Kluwer, 2003.
- **[Computation]** D. J. Green and S. A. King. *The computation of the cohomology rings of all groups of order 128.* J. Algebra 325 (2011), 352–363.
- **[Background]** D. J. Benson. *Representations and Cohomology II: Cohomology of Groups and Modules.* Cambridge Univ. Press, 1991.

## 10. Worked Example / Concrete Special Case

**$G=Q_8$, $k=\mathbb{F}_2$.** The mod-$2$ cohomology is
$$H^*(Q_8;\mathbb{F}_2)=\mathbb{F}_2[x,y,e]\big/\big(x^2+xy+y^2,\ x^2y+xy^2\big),\qquad |x|=|y|=1,\ |e|=4 .$$
The $2$-rank of $Q_8$ is $1$ (the unique involution $-1$ generates the only elementary abelian subgroup), so by Quillen $\dim H^*=1$. Duflot gives $\operatorname{depth}\ge r_2(Z(Q_8))=1$, hence $\operatorname{depth}=\dim=1$: the ring is Cohen–Macaulay, and $H^*_{\mathfrak m}$ is concentrated in degree $1$.

Take the hsop $\zeta_1=e$, so $r=1$, $d_1=4$. Then
$$H^*(Q_8;\mathbb{F}_2)/(e)\;=\;\mathbb{F}_2[x,y]/(x^2+xy+y^2,\ x^2y+xy^2),$$
with $\mathbb{F}_2$-basis $\{1;\ x,y;\ x^2,xy;\ x^3\}$, i.e. Hilbert series
$$f(t)=1+2t+2t^2+t^3 .$$
The top nonzero degree is $3$, and $\sum_i (d_i-1)=4-1=3$. So the Cohen–Macaulay criterion of §2 is met exactly:
$$\operatorname{Reg}H^*(Q_8;\mathbb{F}_2)=a_1+1=(-4+3)+1=0 .$$
Equivalently, the full Hilbert series is
$$\sum_n \dim_{\mathbb{F}_2}H^n(Q_8;\mathbb{F}_2)\,t^n=\frac{1+2t+2t^2+t^3}{1-t^4},$$
and $f$ is palindromic, $t^3f(1/t)=f(t)$ — Benson–Carlson duality in the smallest interesting case.

**Where the difficulty starts.** Replace $Q_8$ by a group with $r_p(G)-\operatorname{depth}=3$: then $H^i_{\mathfrak m}$ can be nonzero for four values of $i$, the Hilbert series no longer determines the $a_i$, and one must control every differential in Greenlees' spectral sequence. That is the regime Symonds' geometric argument handles for finite groups and where no argument at all is available for finite group schemes.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*