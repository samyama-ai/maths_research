---
id: 04-topology/tait-alternating-knot-conjecture
title: "Tait Alternating Knot Conjecture"
topic: 04-topology
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Tait Alternating Knot Conjecture

> **Topic:** Topology & Knot Theory · **ID:** `04-topology/tait-alternating-knot-conjecture` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

Peter Guthrie Tait, compiling knot tables between 1876 and 1885, asserted three properties of alternating diagrams without proof. They are collectively the **Tait conjectures**:

- **(T1) Minimality.** A reduced alternating diagram of a link $L$ has the minimal crossing number among all diagrams of $L$.
- **(T2) Writhe invariance.** Any two reduced alternating diagrams of the same oriented link have the same writhe; consequently an amphichiral alternating knot has even crossing number.
- **(T3) Flyping.** Any two reduced alternating diagrams of the same prime link on $S^2$ are related by a finite sequence of *flypes*.

"Reduced" means the diagram has no *nugatory* crossing — no crossing separated by a simple closed curve meeting the diagram only at that point. A complete resolution requires proofs of all three statements for all links, plus, in the modern reading of Tait's programme, an intrinsic (diagram-free) characterisation of which knots admit an alternating diagram at all.

All three statements are now **theorems**: (T1) and (T2) were proved in 1987 using the Jones polynomial (Kauffman, Murasugi, Thistlethwaite); (T3) was proved by Menasco and Thistlethwaite (1991/1993). The intrinsic characterisation was obtained independently by Greene and by Howie in 2017. What remains open is the extension of these statements beyond the alternating/adequate world — most notably additivity of crossing number under connected sum for arbitrary knots.

## 2. Mathematical Foundations

A **link diagram** $D$ is a 4-valent plane graph with over/under decoration at each vertex. $D$ is **alternating** if, travelling along each component, crossings alternate over–under–over–under. The **crossing number** $c(L)=\min_D c(D)$.

**Kauffman bracket.** $\langle\,\cdot\,\rangle:\{\text{diagrams}\}\to\mathbb{Z}[A^{\pm1}]$ is defined by
$$\langle \emptyset\rangle=1,\qquad \langle D\sqcup\bigcirc\rangle=(-A^{2}-A^{-2})\langle D\rangle,$$
$$\langle D\rangle = A\,\langle D_0\rangle + A^{-1}\langle D_\infty\rangle,$$
where $D_0,D_\infty$ are the two smoothings at a chosen crossing. Summing over all $2^{c}$ states $\sigma$,
$$\langle D\rangle=\sum_{\sigma}A^{\,a(\sigma)-b(\sigma)}\bigl(-A^{2}-A^{-2}\bigr)^{|\sigma|-1},$$
with $a,b$ the numbers of $A$- and $B$-smoothings and $|\sigma|$ the number of state circles. The Jones polynomial of an oriented link is
$$V_L(t)=\bigl(-A^{3}\bigr)^{-w(D)}\langle D\rangle\Big|_{A=t^{-1/4}},\qquad w(D)=\sum_{\text{crossings}}\varepsilon_i\in\mathbb{Z}.$$

**Span.** Write $\operatorname{span}V_L=\max\deg V_L-\min\deg V_L$.

> **Theorem (Kauffman 1987, Murasugi 1987, Thistlethwaite 1987).** For any connected diagram $D$ with $c$ crossings, $\operatorname{span}\langle D\rangle\le 4c$, with equality iff $D$ is reduced alternating (up to connected-sum splitting). Hence for a nonsplit link, $\operatorname{span}V_L\le c(L)$, with equality when $L$ is alternating.

Since $\operatorname{span}V_L$ is an invariant, this proves (T1). The extremal-coefficient argument extends to **adequate** diagrams: $D$ is $A$-adequate if the all-$A$ state has no state circle touching itself at a crossing, $B$-adequate dually, adequate if both. Reduced alternating $\Rightarrow$ adequate.

**Writhe (T2).** Thistlethwaite's proof uses the Kauffman two-variable polynomial $F_L(a,z)$: for a reduced alternating diagram, the $a$-degree spread of $F$ determines $w(D)$, so $w$ is an invariant of the link. Equivalently, via the HOMFLY or via the Jones polynomial of the mirror: $V_{\bar L}(t)=V_L(t^{-1})$, so an amphichiral $L$ has symmetric Jones span, forcing $c(L)$ even by parity of the extremal degrees.

**Flyping (T3).** A **flype** replaces a tangle $T$ inside a diagram by its $180^\circ$ rotation, moving one crossing from one side of $T$ to the other. Menasco–Thistlethwaite work in the link complement $S^{3}\setminus L$, cut along the two checkerboard surfaces, and analyse incompressible spanning surfaces and the induced "cut-and-paste" combinatorics of curves on the diagram sphere.

**Intrinsic characterisation.** Greene: a link $L\subset S^3$ is nonsplit alternating **iff** it bounds a pair of spanning surfaces $S_+,S_-$ with definite intersection forms of opposite sign satisfying $\chi(S_+)+\chi(S_-)=2-c$ combinatorially, i.e. **positive- and negative-definite spanning surfaces**. Howie: $L$ is alternating iff its exterior contains a pair of spanning surfaces $S_1,S_2$ with
$$\chi(S_1)+\chi(S_2)+\tfrac{1}{2}\,i(\partial S_1,\partial S_2)=2 .$$

## 3. History & State of the Art (SOTA)

- **1876–1885.** Tait's *On knots I, II, III* (Trans. Roy. Soc. Edinburgh) tabulate alternating knots to 10 crossings and record the three assertions as working hypotheses. Tait, Kirkman and Little produce tables through 11 crossings by hand.
- **1928–1984.** The Alexander polynomial cannot detect chirality ($\Delta_{\bar K}=\Delta_K$) and gives no crossing-number bound; the conjectures resist all classical machinery for a century.
- **1984.** Jones discovers $V_L(t)$. Within three years the bracket state sum makes (T1) and (T2) accessible.
- **1987.** Kauffman (*Topology* 26), Murasugi (*Topology* 26), Thistlethwaite (*Topology* 26) independently prove (T1); Murasugi (*Math. Proc. Camb. Phil. Soc.* 102) and Thistlethwaite (*Topology* 27, 1988, via the Kauffman polynomial) settle (T2).
- **1988.** Lickorish–Thistlethwaite extend minimality to semi-adequate links: an adequate diagram is minimal and its writhe is an invariant.
- **1991/1993.** Menasco–Thistlethwaite announce (Bull. AMS 25) and publish (Ann. of Math. 138) the flyping theorem, completing Tait's programme and yielding an algorithmic classification of alternating links.
- **1998–2004.** Flyping powers exhaustive tabulation: Hoste–Thistlethwaite–Weeks tabulate all 1,701,936 prime knots to 16 crossings, with alternating knots enumerated directly from flype-equivalence classes.
- **2017.** Greene (*Duke Math. J.* 166) and Howie (*Geom. Topol.* 21) give the diagram-free characterisations, answering a question of Ralph Fox ("what is an alternating knot?").
- **2017–2025.** Consequences fan out: Greene–Howie-type criteria drive results on the Khovanov homology of alternating links (thin, determined by the Jones polynomial and signature — Lee 2005), on quasi-alternating links, and on the relation between the Turaev genus and alternation number.

## 4. Partial Results / Verified Cases

- **Fully proved classes.** All alternating links (T1, T2, T3); all adequate links (T1, T2 — Lickorish–Thistlethwaite 1988); all $A$- or $B$-adequate links get the one-sided bound $\operatorname{span}$ estimate.
- **Crossing-number additivity.** $c(K_1\\#K_2)=c(K_1)+c(K_2)$ holds when both summands are alternating (immediate from T1), and more generally when both are adequate. Open in general; Lackenby (*J. Topology*, 2009) proved $c(K_1\\#\cdots\\# K_n)\ge \frac{1}{152}\sum_i c(K_i)$, later improved to a factor $1/5$ by Lackenby's refinements and to additivity for torus knots and for knots with essential-tangle decompositions.
- **Amphichirality.** No alternating amphichiral knot with odd crossing number exists (T2). Verified by tabulation for all prime knots to 16 crossings.
- **Detection.** Being alternating is decidable from the exterior (Greene/Howie); combined with normal-surface algorithms this gives an algorithm to decide alternation, made explicit by Lackenby's work on alternating-link recognition (2017–2021), which places the problem in $\mathsf{NP}$.
- **Computational range.** Tables of alternating knots complete through 23 crossings (Burton, 2020: 352,152,252 prime knots to 19 crossings; alternating counts extended further by Burton and by Rankin–Flint–Schermann for alternating knots to 23 crossings).

## 5. Principal Obstacles

The historical failure of pre-1984 methods, and the obstacles to generalisation:

- **Classical invariants are degree-blind.** The Alexander polynomial satisfies $\deg\Delta_K\le c(K)-1$ only weakly and is mirror-symmetric, so it can bound neither crossing number sharply nor detect chirality. Fundamental-group presentations from a diagram give no lower bound on $c$, because Tietze moves destroy the crossing count.
- **Crossing number is not geometric.** $c(K)$ is defined by a minimum over infinitely many diagrams, with no known monotone quantity in the complement to bound it. Reidemeister moves can increase crossings arbitrarily before decreasing them (hard unknot diagrams need $\ge c$ extra crossings), so local simplification arguments fail.
- **Adequacy is fragile.** The bracket-extremal argument needs the top and bottom terms to survive without cancellation. For a general diagram, the all-$A$ state has self-touching circles and the extremal coefficient collapses, so $\operatorname{span}V<4c$ with no controlled defect.
- **Flyping arguments are surface-specific.** Menasco–Thistlethwaite exploit the fact that the two checkerboard surfaces of an alternating diagram are essential in the complement; for non-alternating diagrams the checkerboard surfaces compress, and the incompressible-surface bookkeeping breaks down.
- **Additivity resists.** For $c(K_1\\# K_2)$, one must show a minimal diagram of the composite can be split along a curve meeting it twice. The natural tool — an essential annulus/sphere — need not be realised by a simple closed curve on the diagram sphere, and normal-surface bounds only give a linear-loss inequality.

## 6. The Gap

Tait's own three conjectures have no remaining gap. The residual programme is the extension:

1. **Additivity of crossing number.** Proven only when the summands are adequate. The precise missing step: given a minimal diagram $D$ of $K_1\\# K_2$ and the essential swallow-follow annulus in the complement, produce an isotopy making the decomposing sphere meet $D$ in exactly two points. No invariant is known that is simultaneously additive under $\\#$ and a sharp lower bound for $c$.
2. **Beyond adequacy.** For a general knot $\operatorname{span}V_K\le c(K)$, but the deficit $c(K)-\operatorname{span}V_K$ is unbounded (e.g. knots with trivial Jones polynomial are not known to exist, but $(p,q)$-torus knots already have span far below $c$). Bridging requires a lower bound for $c$ from Khovanov or knot-Floer homology with controlled loss; current results (Turaev genus bounds, the Khovanov width inequality $w_{Kh}(K)\le g_T(K)+2$) lose too much.
3. **Effectiveness of Greene–Howie.** The characterisations are existential over spanning surfaces; converting them into a polynomial-time recognition algorithm for alternation is open.

## 7. Current Research (as of June 2026)

- **Definite-surface methods.** Greene's programme (Boston College) continues into lattice-embedding characterisations of alternating and of definite 4-manifolds; extensions to alternating links in thickened surfaces and to *checkerboard-definite* links are active.
- **Alternating distance.** Groups at Boise State, Bryn Mawr and Trinity College Dublin (Lowrance, Kalfagianni, Champanerkar–Kofman) study alternation number, dealternating number and Turaev genus, and the inequalities among them; several remain conjecturally sharp. *(frontier — verify)*
- **Recognition complexity.** Lackenby's line of work (Oxford) on knot-problem complexity — unknot recognition in $\mathsf{NP}\cap\mathsf{co\text{-}NP}$, and alternating-link recognition — is being pushed toward certified polynomial-time recognition of alternating diagrams. *(frontier — verify)*
- **Virtual and surface-alternating links.** Boden, Karimi and collaborators extend Tait-type minimality and flyping to alternating links in thickened surfaces and to virtual knots, where a Kauffman-bracket span theorem holds with genus corrections. *(frontier — verify)*
- **Categorified obstructions to additivity.** Attempts to build an additive lower bound for $c$ from Khovanov homology's thickness or from the HOMFLY homology's Poincaré polynomial remain the main hope for the crossing-number additivity conjecture.

## 8. Future Work

- Prove $c(K_1\\#K_2)=c(K_1)+c(K_2)$ in full generality; a plausible route is an additive homological width invariant $w$ with $w(K)\le c(K)$ and equality on a large class.
- Turn Greene's definite-spanning-surface criterion into an explicit certificate checkable in polynomial time, yielding alternation $\in\mathsf{NP}\cap\mathsf{co\text{-}NP}$.
- Extend flyping to a complete generating set of moves relating minimal diagrams of adequate or of Turaev-genus-one links.
- Sharpen the Kauffman-bracket span deficit: characterise the links with $c(L)-\operatorname{span}V_L=1$, conjecturally exactly the almost-alternating links.
- Quantify Tait's programme in thickened surfaces: is every reduced alternating diagram on a surface of genus $g$ minimal in its own homotopy class?

## 9. Key References

- **[Foundational]** P. G. Tait. *On Knots I, II, III.* Transactions of the Royal Society of Edinburgh, 1877–1885; reprinted in *Scientific Papers*, Vol. I, Cambridge Univ. Press, 1898.
- **[Foundational]** L. H. Kauffman. *State models and the Jones polynomial.* Topology 26 (1987), 395–407.
- **[Foundational]** K. Murasugi. *Jones polynomials and classical conjectures in knot theory.* Topology 26 (1987), 187–194.
- **[Foundational]** M. B. Thistlethwaite. *A spanning tree expansion of the Jones polynomial.* Topology 26 (1987), 297–309.
- **[Foundational]** M. B. Thistlethwaite. *Kauffman's polynomial and alternating links.* Topology 27 (1988), 311–318.
- **[Foundational]** W. B. R. Lickorish, M. B. Thistlethwaite. *Some links with non-trivial polynomials and their crossing-numbers.* Commentarii Mathematici Helvetici 63 (1988), 527–539.
- **[Foundational]** W. W. Menasco, M. B. Thistlethwaite. *The classification of alternating links.* Annals of Mathematics 138 (1993), 113–171. (Announcement: Bulletin of the AMS 25 (1991), 403–412.)
- **[SOTA / Recent]** J. E. Greene. *Alternating links and definite surfaces.* Duke Mathematical Journal 166 (2017), 2133–2151. (With an appendix by A. Juhász and M. Lackenby.)
- **[SOTA / Recent]** J. Howie. *A characterisation of alternating knot exteriors.* Geometry & Topology 21 (2017), 2353–2371.
- **[SOTA / Recent]** M. Lackenby. *The crossing number of composite knots.* Journal of Topology 2 (2009), 747–768.
- **[SOTA / Recent]** J. Hoste, M. Thistlethwaite, J. Weeks. *The first 1,701,936 knots.* The Mathematical Intelligencer 20 (1998), 33–48.
- **[Survey]** W. B. R. Lickorish. *An Introduction to Knot Theory.* Graduate Texts in Mathematics 175, Springer, 1997.
- **[Survey]** C. C. Adams. *The Knot Book.* W. H. Freeman, 1994; reprint AMS, 2004.
- **[Survey]** A. Champanerkar, I. Kofman. *A survey on the Turaev genus of knots.* Acta Mathematica Vietnamica 39 (2014), 497–514.

## 10. Worked Example / Concrete Special Case

**Claim.** The standard 3-crossing diagram $D$ of the trefoil is minimal, and the trefoil is chiral.

*Bracket computation.* $D$ is alternating and reduced with $c=3$. Expanding the state sum over all $2^3=8$ states and setting $\delta=-A^2-A^{-2}$:

| $a(\sigma)$ | states | $|\sigma|$ | contribution |
|---|---|---|---|
| 3 | 1 | 2 | $A^{3}\delta$ |
| 2 | 3 | 1 | $3A^{1}$ |
| 1 | 3 | 2 | $3A^{-1}\delta$ |
| 0 | 1 | 3 | $A^{-3}\delta^{2}$ |

Summing:
$$\langle D\rangle = A^{3}\delta+3A+3A^{-1}\delta+A^{-3}\delta^{2} = -A^{5}-A^{-3}+A^{-7}.$$
Extremal degrees: $\max=5$, $\min=-7$, so $\operatorname{span}\langle D\rangle=12=4c$ — exactly the equality case of the span theorem, as (T1) predicts.

*Jones polynomial.* With writhe $w(D)=-3$ for this orientation,
$$f_D=(-A^{3})^{3}\langle D\rangle\cdot(-A^3)^{-2\cdot 3}\Rightarrow V(t)=-t^{-4}+t^{-3}+t^{-1},$$
after $A=t^{-1/4}$. Then $\operatorname{span}V=(-1)-(-4)=3=c(K)$.

*Minimality.* Any diagram $D'$ of the trefoil satisfies $c(D')\ge\operatorname{span}V=3$. Since $c(D)=3$, $c(3_1)=3$. The trefoil is therefore the unique nontrivial knot of minimal crossing number, and the only diagrams with $c=3$ are the two alternating ones.

*Chirality.* The mirror $\overline{3_1}$ has $V_{\overline{3_1}}(t)=V_{3_1}(t^{-1})=-t^{4}+t^{3}+t\neq V_{3_1}(t)$, so $3_1\not\simeq\overline{3_1}$. Consistently with (T2), the two reduced alternating diagrams of $3_1$ both have writhe $-3$ (respectively $+3$ for the mirror), and $c=3$ is odd — matching the theorem that an amphichiral alternating knot must have even crossing number. The smallest amphichiral alternating knot is the figure-eight $4_1$, with $c=4$ and $V(t)=t^{-2}-t^{-1}+1-t+t^{2}$, palindromic as required.

*Flyping.* $3_1$ has no nontrivial flype: its two reduced alternating diagrams on $S^2$ are related by a plane isotopy alone, the degenerate case of (T3). The smallest knot with a genuinely nontrivial flype orbit is $8_{15}$-type twisted-tangle families, where flyping permutes crossings between the two sides of a 2-string tangle without changing the knot type.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*