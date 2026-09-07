---
id: 03-geometry/andre-oort-conjecture
title: "Andre-Oort Conjecture"
topic: 03-geometry
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# André–Oort Conjecture

> **Topic:** Algebraic & Differential Geometry · **ID:** `03-geometry/andre-oort-conjecture` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

Let $S$ be a Shimura variety over $\mathbb{C}$ and let $\Sigma \subseteq S(\mathbb{C})$ be a set of **special points** (CM points). The conjecture asserts:

> Every irreducible component of the Zariski closure $\overline{\Sigma}^{\mathrm{Zar}}$ is a **special subvariety** of $S$.

Equivalently: if an irreducible closed subvariety $V \subseteq S$ contains a Zariski-dense set of special points, then $V$ is special (i.e. an irreducible component of the image of a Shimura sub-datum under a Hecke correspondence).

The conjecture is a **theorem**. It was proved unconditionally by Pila, Shankar and Tsimerman, with an appendix by Esnault and Groechenig (arXiv:2109.08788, 2021), building on Binyamini–Schmidt–Yafaev and on Tsimerman's earlier resolution for $\mathcal{A}_g$. What remains open is the **effective** form (explicit bounds on the special points off the special locus) and the wider **Zilber–Pink** generalisation, of which André–Oort is the codimension-extreme case.

A complete disproof would have required exhibiting a non-special $V$ with dense CM locus; a complete proof required, and obtained, unconditional Galois-orbit lower bounds for special points on all Shimura varieties.

## 2. Mathematical Foundations

**Shimura datum.** A pair $(G, X)$ with $G$ a connected reductive $\mathbb{Q}$-group and $X$ a $G(\mathbb{R})$-conjugacy class of morphisms $h : \mathbb{S} \to G_{\mathbb{R}}$ ($\mathbb{S} = \mathrm{Res}_{\mathbb{C}/\mathbb{R}}\mathbb{G}_m$) satisfying Deligne's axioms. For a compact open $K \subseteq G(\mathbb{A}_f)$,
$$\mathrm{Sh}_K(G,X)(\mathbb{C}) \;=\; G(\mathbb{Q}) \backslash \bigl( X \times G(\mathbb{A}_f)/K \bigr),$$
a quasi-projective variety with a canonical model over a number field $E(G,X)$ (Deligne, Borovoi, Milne).

**Special points.** $x \in X$ is special if its Mumford–Tate group $\mathrm{MT}(x) \subseteq G$ is a torus. Its image in $\mathrm{Sh}_K$ is a special point, algebraic over $E(G,X)$ by Shimura reciprocity.

**Special subvarieties.** Images of $\mathrm{Sh}_{K'}(H, X_H) \to \mathrm{Sh}_K(G,X)$ for sub-data $(H, X_H) \subseteq (G,X)$, translated by Hecke operators.

**Model case.** $G = \mathrm{GSp}_{2g}$, $X = \mathfrak{H}_g$ (Siegel upper half space), $S = \mathcal{A}_g$; special points $=$ CM abelian varieties. For $g=1$, $S = Y(1) \cong \mathbb{A}^1_j$, special points are the singular moduli $j(\tau)$, $\tau$ imaginary quadratic. Special subvarieties of $Y(1)^n$ are cut out by conditions "$x_i$ is a fixed singular modulus" and "$\Phi_N(x_i, x_j) = 0$" (modular polynomials).

**The three pillars of the proof.**

1. **Pila–Wilkie counting.** For $Z \subseteq \mathbb{R}^n$ definable in an o-minimal structure and $\varepsilon > 0$,
$$\\#\{ q \in Z^{\mathrm{trans}} \cap \mathbb{Q}^n : H(q) \le T \} \;\ll_{Z,\varepsilon}\; T^{\varepsilon},$$
where $Z^{\mathrm{trans}}$ removes all connected positive-dimensional semialgebraic subsets.
2. **Definability of uniformisation.** $\pi : X \to S$ restricted to a Siegel fundamental set $\mathfrak{F}$ is definable in $\mathbb{R}_{\mathrm{an},\exp}$ (Peterzil–Starchenko for $\mathcal{A}_g$; Klingler–Ullmo–Yafaev in general).
3. **Arithmetic lower bound.** For a special point $s$ with CM order of discriminant $\mathrm{disc}(s)$, one needs $\delta > 0$ with
$$[\,\mathbb{Q}(s) : \mathbb{Q}\,] \;=\; \\#\,\mathrm{Gal}(\overline{\mathbb{Q}}/E)\cdot s \;\gg_\varepsilon\; |\mathrm{disc}(s)|^{\delta},$$
against the polynomial height bound $H(\tilde s) \ll |\mathrm{disc}(s)|^{C}$ for a preimage $\tilde s \in \mathfrak{F}$. The two bounds combined make the Galois orbit too large for Pila–Wilkie unless positive-dimensional semialgebraic blocks occur; **Ax–Lindemann–Weierstrass** then converts those blocks into special subvarieties.

For $g=1$ the Galois bound is Siegel's ineffective $h(d) \gg_\varepsilon |d|^{1/2 - \varepsilon}$.

## 3. History & State of the Art (SOTA)

- **1989** — Yves André poses the case of curves in his book *G-Functions and Geometry* (Problem, Ch. X.4).
- **1997** — Frans Oort independently states the $\mathcal{A}_g$ case in "Canonical liftings and dense sets of CM-points"; the joint name dates from this period.
- **1998** — Moonen proves cases in $\mathcal{A}_g$ via canonical lifts and $p$-adic methods.
- **2003** — Edixhoven–Yafaev: curves whose CM points lie in one Hecke orbit (*Annals* 157).
- **2006–2009** — Klingler, Ullmo, Yafaev develop the ergodic/equidistribution route; full conjecture proved **assuming GRH for CM fields** (published *Annals* 180, 2014).
- **2011** — Pila proves the conjecture unconditionally for $Y(1)^n \cong \mathbb{C}^n$ via the Pila–Zannier o-minimal strategy (*Annals* 173).
- **2014** — Pila–Tsimerman prove Ax–Lindemann for $\mathcal{A}_g$ (*Annals* 179).
- **2018** — Tsimerman proves André–Oort for $\mathcal{A}_g$, all $g$, unconditionally (*Annals* 187), using the averaged Colmez conjecture (Andreatta–Goren–Howard–Madapusi Pera; Yuan–Zhang) to get $h_{\mathrm{Fal}} \ll_\varepsilon |\mathrm{disc}|^{\varepsilon}$ for CM abelian varieties.
- **2021** — Pila–Shankar–Tsimerman (appendix Esnault–Groechenig) prove the **general case**: a canonical height on Shimura varieties bounds the heights of special points, feeding the Binyamini–Schmidt–Yafaev reduction.
- **2023** — Binyamini–Schmidt–Yafaev publish the point-counting derivation of Galois lower bounds from height bounds (*Math. Annalen*).

## 4. Partial Results / Verified Cases

| Class | Result | Reference |
|---|---|---|
| Curves in $Y(1)^2$, CM points in one Hecke orbit | proved | Edixhoven 1998; Edixhoven–Yafaev 2003 |
| $Y(1)^n$, all $n$ | proved unconditionally | Pila 2011 |
| $\mathcal{A}_2$ (abelian surfaces) | proved | Pila–Tsimerman, *Compositio* 149 (2013) |
| $\mathcal{A}_g$, all $g$ | proved unconditionally | Tsimerman 2018 |
| Arbitrary Shimura variety, under GRH for CM fields | proved | Klingler–Ullmo–Yafaev 2014 |
| Arbitrary Shimura variety, unconditional | proved | Pila–Shankar–Tsimerman 2021 |
| **Effective** case: lines $ax+by=c$ in $Y(1)^2$ | proved with explicit bounds | Kühne 2012; Bilu–Masser–Zannier 2013; Allombert–Bilu–Pizarro-Madariaga 2015 |
| Zilber–Pink for $Y(1)^n$ | open in general; partial (Habegger–Pila 2016, Daw–Orr) | — |

Effective results reach only very low complexity: Kühne's method handles specific plane curves of small degree; there is no effective statement for a general curve in $\mathcal{A}_2$.

## 5. Principal Obstacles

The obstacles that held the problem open for three decades, and those that persist:

- **Ineffectivity of the class-number input.** Siegel's bound $h(d) \gg_\varepsilon |d|^{1/2-\varepsilon}$ has an ineffective implied constant (a putative Siegel zero). Every proof using it inherits ineffectivity: one knows the exceptional set is finite but cannot list it.
- **Galois orbits beyond $\mathcal{A}_g$.** For $\mathcal{A}_g$ the Faltings height gives a handle on the arithmetic of a CM point via the Colmez conjecture. A general Shimura variety of abelian type has no moduli interpretation and no Faltings height; PST's fix is a *canonical* height built from an integral model plus a rigidity/integrality statement for local systems (Esnault–Groechenig appendix), a genuinely new mechanism rather than a generalisation of the old one.
- **Pila–Wilkie's $T^{\varepsilon}$ is not polynomial.** The counting theorem gives no explicit constant, so it cannot yield explicit bounds. Sharpening to $\log$-power counts requires point-counting in *sharply o-minimal* / Pfaffian settings (Binyamini–Novikov), still incomplete for general $\pi$.
- **Ax–Lindemann is not enough for Zilber–Pink.** Passing from André–Oort to intersections with special subvarieties of *positive* dimension needs uniform Galois bounds over families and functional transcendence in the "Ax–Schanuel" form, where the arithmetic input (heights of intersection points) remains unavailable.
- **Equidistribution fails at the boundary.** The ergodic approach (Clozel–Ullmo, Ullmo–Yafaev) loses control when the sequence of special subvarieties escapes to the boundary of the Baily–Borel compactification; this was the reason GRH was needed.

## 6. The Gap

For the conjecture itself there is no gap: Section 4's last unconditional row is Section 1's full statement. The residual gaps are:

1. **Effectivity.** Proven: finiteness of maximal special subvarieties in $\overline{\Sigma}^{\mathrm{Zar}}$. Not proven: any computable bound on $|\mathrm{disc}(s)|$ for $s \in \Sigma \setminus (\text{special locus})$ except in explicit small cases. Crossing this requires either an effective lower bound for $L(1,\chi_d)$ or a proof route avoiding Siegel entirely.
2. **Zilber–Pink.** Replace "special points" by "special subvarieties of complementary dimension". The missing step is a height bound for atypical intersection points that is uniform in the parameter of the intersecting special subvariety.
3. **Uniformity in the level and the group.** Bounds in the current proof depend on $K$ and $(G,X)$ non-explicitly.

## 7. Current Research (as of June 2026)

- **Effective André–Oort via sharply o-minimal structures.** Binyamini and Novikov's programme replaces Pila–Wilkie with polynomial-in-$\log$ counting; Binyamini–Schmidt–Yafaev use it for Galois bounds. Effective statements for $Y(1)^n$ with explicit constants are being pushed. *(frontier — verify)*
- **Zilber–Pink.** Daw–Orr (UCL / Manchester / Reading) on unlikely intersections in $\mathcal{A}_2$ and quantitative reduction theory; Habegger–Pila on large Galois orbits.
- **Heights and integral models.** Follow-ups to the PST canonical height, connecting to $p$-adic Hodge theory and to Esnault–Groechenig's integrality of rigid local systems; groups at Oxford, Toronto, Duke, IAS.
- **Non-archimedean and function-field analogues.** André–Oort for Drinfeld modular varieties (Breuer and successors) and for $\mathcal{A}_g$ in positive characteristic (Moonen's $p$-adic canonical lifting circle).
- **André–Oort for mixed Shimura varieties and variations of Hodge structure**, via Bakker–Klingler–Tsimerman's definability of period maps and the resulting algebraicity theorems.

## 8. Future Work

- Prove an effective version of Siegel's theorem, or design a Galois lower bound bypassing $L(1,\chi_d)$ — the single highest-value target, explicitly named by Pila and by Kühne.
- Establish Ax–Schanuel with quantitative height control on all Shimura varieties, the stated route to Zilber–Pink (Klingler–Ullmo–Yafaev's bi-algebraic programme).
- Extend the canonical-height machinery to mixed Shimura varieties, giving André–Oort for families of semiabelian varieties.
- Develop algorithms that, given an explicit curve in $Y(1)^2$ or $\mathcal{A}_2$, decide whether it is special and enumerate its CM points.

## 9. Key References

- **[Foundational]** Y. André. *G-Functions and Geometry*. Aspects of Mathematics E13, Vieweg, 1989.
- **[Foundational]** F. Oort. *Canonical liftings and dense sets of CM-points*, in "Arithmetic and Geometry" (F. Catanese, ed.), Cambridge University Press, 1997.
- **[Foundational]** J. Pila, A. J. Wilkie. *The rational points of a definable set*. Duke Math. J. 133 (2006), 591–616.
- **[Foundational]** J. Pila, U. Zannier. *Rational points in periodic analytic sets and the Manin–Mumford conjecture*. Rend. Lincei Mat. Appl. 19 (2008), 149–162.
- **[Milestone]** B. Edixhoven, A. Yafaev. *Subvarieties of Shimura varieties*. Ann. of Math. 157 (2003), 621–645.
- **[Milestone]** J. Pila. *O-minimality and the André–Oort conjecture for $\mathbb{C}^n$*. Ann. of Math. 173 (2011), 1779–1840.
- **[Milestone]** L. Kühne. *An effective result of André–Oort type*. Ann. of Math. 176 (2012), 651–671.
- **[Milestone]** B. Klingler, A. Yafaev. *The André–Oort conjecture*. Ann. of Math. 180 (2014), 867–925; E. Ullmo, A. Yafaev. *Galois orbits and equidistribution of special subvarieties: towards the André–Oort conjecture*. Ann. of Math. 180 (2014), 823–865.
- **[Milestone]** J. Pila, J. Tsimerman. *Ax–Lindemann for $\mathcal{A}_g$*. Ann. of Math. 179 (2014), 659–681.
- **[SOTA]** J. Tsimerman. *The André–Oort conjecture for $\mathcal{A}_g$*. Ann. of Math. 187 (2018), 379–390.
- **[SOTA]** F. Andreatta, E. Z. Goren, B. Howard, K. Madapusi Pera. *Faltings heights of abelian varieties with complex multiplication*. Ann. of Math. 187 (2018), 391–531; X. Yuan, S.-W. Zhang. *On the averaged Colmez conjecture*. Ann. of Math. 187 (2018), 533–638.
- **[SOTA]** J. Pila, A. N. Shankar, J. Tsimerman, with an appendix by H. Esnault and M. Groechenig. *Canonical heights on Shimura varieties and the André–Oort conjecture*. arXiv:2109.08788, 2021.
- **[SOTA]** G. Binyamini, H. Schmidt, A. Yafaev. *Lower bounds for Galois orbits of special points on Shimura varieties: a point-counting approach*. Math. Ann. 385 (2023), 961–973.
- **[Survey]** T. Scanlon. *O-minimality as an approach to the André–Oort conjecture*. Panoramas et Synthèses 52, SMF, 2017.
- **[Survey]** C. Daw. *The André–Oort conjecture via o-minimality*, in "O-minimality and Diophantine Geometry", LMS Lecture Note Series 421, Cambridge University Press, 2015.
- **[Survey]** Y. Peterzil, S. Starchenko. *Definability of restricted theta functions and families of abelian varieties*. Duke Math. J. 162 (2013), 731–765.

## 10. Worked Example / Concrete Special Case

**Setting.** $S = Y(1)^2 = \mathbb{A}^2$ with coordinates $(j_1, j_2)$. Special points are pairs of singular moduli, e.g.
$$j(i) = 1728,\qquad j\!\left(\tfrac{1+\sqrt{-3}}{2}\right) = 0,\qquad j\!\left(\tfrac{1+\sqrt{-163}}{2}\right) = -640320^3 .$$
Special curves are exactly the vertical/horizontal lines through a singular modulus and the modular curves $Y_0(N) : \Phi_N(j_1,j_2)=0$.

**A special curve.** $\Phi_2(X,Y) = X^3 + Y^3 - X^2Y^2 + 1488XY(X+Y) - 162000(X^2+Y^2) + 40773375XY + 8748000000(X+Y) - 157464000000000$. Its points $(j(\tau), j(2\tau))$ include infinitely many CM pairs: whenever $\tau$ is imaginary quadratic, so is $2\tau$. Consistent with the conjecture — the curve is special.

**A non-special curve.** Take the line $L : j_1 + j_2 = 1$. Kühne (2012) proves $L$ contains **no** CM points at all. Sketch of why the general mechanism forces finiteness: suppose $(j(\tau_1), j(\tau_2)) \in L$ with $\tau_k$ of discriminant $d_k$, $|d_1| \ge |d_2|$. Then

1. *Galois.* Conjugating over $\mathbb{Q}$, the whole Galois orbit of $j(\tau_1)$ — of size $h(d_1) \gg_\varepsilon |d_1|^{1/2-\varepsilon}$ — produces distinct points of $L$, so $L$ carries $\gg |d_1|^{1/2-\varepsilon}$ CM points.
2. *Height.* Each such point has a preimage $(\tilde\tau_1, \tilde\tau_2)$ in the standard fundamental domain $\mathfrak{F}$ with $\tilde\tau_k = \frac{-b_k + \sqrt{d_k}}{2a_k}$, $|b_k| \le a_k \le \sqrt{|d_k|/3}$; hence $H(\tilde\tau_k) \ll |d_k| \ll |d_1|$ as a rational point of $\mathbb{Q}^2$ after clearing $\sqrt{d_k}$.
3. *Counting.* The set $Z = \{ (\tilde\tau_1,\tilde\tau_2) \in \mathfrak{F}^2 : (j(\tilde\tau_1), j(\tilde\tau_2)) \in L \}$ is definable in $\mathbb{R}_{\mathrm{an},\exp}$. Steps 1–2 give $\gg T^{1/2-\varepsilon}$ rational points of height $\le T = C|d_1|$ on $Z$, contradicting Pila–Wilkie's $\ll T^{\varepsilon}$ — unless $Z$ contains a positive-dimensional semialgebraic arc.
4. *Ax–Lindemann.* Such an arc forces $L$ to be the image of a semialgebraic curve in $\mathfrak{H}^2$, hence $L$ is special. But $L$ is a line of slope $-1$ not through a singular modulus and $\Phi_N \ne$ linear for any $N$, so $L$ is not special. Contradiction; only finitely many CM points can lie on $L$, and Kühne's explicit version shows the count is zero.

The example shows both the shape of the argument and its ineffectivity: step 1's implied constant is Siegel's.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*