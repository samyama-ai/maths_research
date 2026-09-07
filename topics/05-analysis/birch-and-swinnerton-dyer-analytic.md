---
id: 05-analysis/birch-and-swinnerton-dyer-analytic
title: "Birch and Swinnerton-Dyer Analytic"
topic: 05-analysis
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Birch and Swinnerton-Dyer Analytic

> **Topic:** Real & Complex Analysis · **ID:** `05-analysis/birch-and-swinnerton-dyer-analytic` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Let $E/\mathbb{Q}$ be an elliptic curve with Hasse–Weil $L$-function $L(E,s)$. The **analytic** form of the Birch and Swinnerton-Dyer conjecture makes two claims about the behaviour of this complex-analytic object at the central point $s=1$.

- **(Rank part.)** The order of vanishing of $L(E,s)$ at $s=1$ — the *analytic rank* $r_{\mathrm{an}} = \operatorname{ord}_{s=1} L(E,s)$ — equals the rank $r$ of the finitely generated abelian group $E(\mathbb{Q})$.
- **(Full formula.)** The leading Taylor coefficient is given exactly by
$$\lim_{s\to 1}\frac{L(E,s)}{(s-1)^{r}}=\frac{\Omega_E\cdot \mathrm{Reg}(E/\mathbb{Q})\cdot \prod_{p}c_p\cdot \\#Ш(E/\mathbb{Q})}{\big(\\#E(\mathbb{Q})_{\mathrm{tors}}\big)^{2}}.$$

A complete proof must, for **every** $E/\mathbb{Q}$: (i) establish that $Ш(E/\mathbb{Q})$ is finite (otherwise the right side is undefined), and (ii) prove both equalities without rank restriction. A disproof needs one curve where either equality fails — checkable in principle, since all quantities are computable to arbitrary precision granted finiteness of $Ш$. Over a general number field $K$ the statement is the same, but is conditional on the analytic continuation of $L(E/K,s)$ to $s=1$, itself open.

## 2. Mathematical Foundations

**The $L$-function.** For $E/\mathbb{Q}$ of conductor $N$ in minimal Weierstrass form, set $a_p = p+1-\\#E(\mathbb{F}_p)$ for $p\nmid N$. Then
$$L(E,s)=\prod_{p\mid N}\big(1-a_pp^{-s}\big)^{-1}\prod_{p\nmid N}\big(1-a_pp^{-s}+p^{1-2s}\big)^{-1},$$
with $a_p\in\{0,\pm1\}$ at bad primes. Hasse's bound $|a_p|\le 2\sqrt p$ gives absolute convergence only for $\Re(s)>3/2$, so $s=1$ lies outside the region of definition: **the conjecture is a statement about an analytic continuation.**

**Continuation.** By the modularity theorem (Wiles; Taylor–Wiles; Breuil–Conrad–Diamond–Taylor 2001), $L(E,s)=L(f,s)$ for a weight-$2$ newform $f\in S_2(\Gamma_0(N))$. Hence $\Lambda(E,s)=N^{s/2}(2\pi)^{-s}\Gamma(s)L(E,s)$ is entire and satisfies
$$\Lambda(E,s)=w\,\Lambda(E,2-s),\qquad w=\pm 1,$$
so the parity of $r_{\mathrm{an}}$ is forced: $w=(-1)^{r_{\mathrm{an}}}$.

**Arithmetic side.** Mordell–Weil gives $E(\mathbb{Q})\cong \mathbb{Z}^r\oplus E(\mathbb{Q})_{\mathrm{tors}}$. The regulator is $\mathrm{Reg}(E/\mathbb{Q})=\det\big(\langle P_i,P_j\rangle\big)_{1\le i,j\le r}$ for a basis $P_1,\dots,P_r$ of $E(\mathbb{Q})/\mathrm{tors}$, where $\langle P,Q\rangle = \hat h(P+Q)-\hat h(P)-\hat h(Q)$ is the Néron–Tate height pairing ($\mathrm{Reg}=1$ if $r=0$). The real period is $\Omega_E=\int_{E(\mathbb{R})}|\omega|$ for the Néron differential $\omega$; $c_p=[E(\mathbb{Q}_p):E_0(\mathbb{Q}_p)]$ are the Tamagawa numbers; and
$$Ш(E/\mathbb{Q})=\ker\Big(H^1(\mathbb{Q},E)\to\prod_v H^1(\mathbb{Q}_v,E)\Big)$$
is the Tate–Shafarevich group, conjecturally finite.

**Descent exact sequence.** For each $n$,
$$0\to E(\mathbb{Q})/nE(\mathbb{Q})\to \mathrm{Sel}^{(n)}(E/\mathbb{Q})\to Ш(E/\mathbb{Q})[n]\to 0,$$
which is what makes the Selmer group the effective bridge between $r$ and $\\#Ш$.

## 3. History & State of the Art (SOTA)

- **1958–1965.** Bryan Birch and Peter Swinnerton-Dyer compute $\prod_{p\le X}\\#E(\mathbb{F}_p)/p$ on the EDSAC II at Cambridge, observe growth like $C(\log X)^r$, and formulate the conjecture in "Notes on elliptic curves I, II" (*J. reine angew. Math.*, 1963 and 1965). It is the first conjecture born from machine computation.
- **1965–1977.** Tate reformulates the constants; Cassels proves the invariance of the conjecture under isogeny. **Coates–Wiles (1977)**: for CM curves with $L(E,1)\neq 0$, $E(\mathbb{Q})$ is finite — the first theorem in the direction $r_{\mathrm{an}}=0\Rightarrow r=0$.
- **1986.** **Gross–Zagier** compute $L'(E,1)$ for $L$-functions of curves over imaginary quadratic fields as a multiple of the Néron–Tate height of a Heegner point.
- **1988–1990.** **Kolyvagin**'s Euler system of Heegner points bounds Selmer groups, giving $r_{\mathrm{an}}\le 1\Rightarrow r=r_{\mathrm{an}}$ and $\\#Ш<\infty$.
- **1991–2004.** **Rubin** proves the Iwasawa main conjecture for imaginary quadratic fields; **Kato** constructs an Euler system from Beilinson elements giving one divisibility for all modular forms, hence upper bounds on Selmer ranks.
- **2014.** **Skinner–Urban** prove the other divisibility of the GL$_2$ main conjecture for good ordinary $p$, upgrading rank $0$/$1$ results to exact $p$-part formulae; **Bhargava–Skinner–Zhang** show BSD holds for a positive proportion — at least $66.48\%$ — of curves ordered by naive height.
- **Present.** No single curve of rank $\ge 2$ has BSD proved, and no unconditional proof exists for any curve with $r_{\mathrm{an}}\ge 2$.

## 4. Partial Results / Verified Cases

- **Analytic rank $0$ or $1$ (Gross–Zagier–Kolyvagin).** For $E/\mathbb{Q}$ with $r_{\mathrm{an}}\in\{0,1\}$: $r=r_{\mathrm{an}}$ and $Ш(E/\mathbb{Q})$ is finite. This covers all elliptic curves of analytic rank $\le 1$ over $\mathbb{Q}$ — an infinite family, but nothing above rank $1$.
- **CM curves.** Coates–Wiles (1977) for $K=\mathbb{Q}(\sqrt{-1}),\mathbb{Q}(\sqrt{-3})$ and CM by the full ring of integers; Rubin (1991) gives the $p$-part of the full formula for CM curves and $p$ not dividing the class number, $p>3$.
- **The full formula, $p$-part.** For $r_{\mathrm{an}}=0$ and $p\ge 5$ good ordinary with irreducible, ramified-at-some-$q$ residual representation, Skinner–Urban (2014) prove $\mathrm{ord}_p$ of both sides agree. Extensions to $r_{\mathrm{an}}=1$: Jetchev–Skinner–Wan; supersingular $p$: Castella, Wan.
- **Converse theorems.** W. Zhang (*Cambridge J. Math.* 2014): if $\mathrm{corank}_{\mathbb{Z}_p}\mathrm{Sel}_{p^\infty}=1$ then $r_{\mathrm{an}}=1$, under hypotheses on the mod-$p$ representation.
- **Congruent numbers.** Tunnell (1983) gives an effective criterion for $L(E_n,1)=0$ for $y^2=x^3-n^2x$; the criterion is a theorem of BSD-rank-part for $n$ squarefree only granted BSD in the rank-$0$ direction, which Coates–Wiles supplies for one implication.
- **Statistical.** Bhargava–Skinner–Zhang (2014): $\ge 66.48\%$ of all $E/\mathbb{Q}$ by height satisfy full BSD. A. Smith (2017 preprint, $2^\infty$-Selmer groups): in quadratic twist families of curves with full rational $2$-torsion, $100\%$ have rank $0$ or $1$ as predicted (Goldfeld's conjecture for these families).
- **Numerical verification.** Grigorov–Jorza–Patrikis–Stein–Tarniţă (*Math. Comp.* 78, 2009) verify full BSD, including $\\#Ш$, for all $2\,463$ curves of conductor $\le 1000$ of rank $\le 1$ satisfying their hypotheses; Cremona's tables now cover conductor $\le 500\,000$ with BSD-predicted $\\#Ш$ matching a perfect square in every computed case.

## 5. Principal Obstacles

- **Rank $\ge 2$ has no point-construction.** Every proven case builds a rational point from an $L$-value: Heegner points give one point, and the Gross–Zagier formula relates $L'(E,1)$ to its height. There is no known analytic object producing two independent points, and the Gross–Kudla–Schoen cycle constructions yield classes whose non-triviality is exactly as hard as the statement they should prove.
- **Kolyvagin's Euler system saturates at corank $1$.** The derived cohomology classes $c_n$ vanish identically once the Heegner point is torsion, so the method gives no information when $r_{\mathrm{an}}\ge2$. Kato's Euler system gives only the upper bound $r\le r_{\mathrm{an}}$ direction ($\mathrm{Sel}$ finite when $L(E,1)\neq0$), never lower bounds on $r$.
- **Finiteness of $Ш$ is unknown in general.** Without it, the right-hand side of the formula is not even defined, and descent computes only $\mathrm{Sel}^{(n)}$ — an upper bound for $r$ that need not stabilise.
- **The transcendental/algebraic mismatch.** $L$-values are analytic objects with no a priori algebraicity; heights are real transcendentals defined by an infinite limit $\hat h(P)=\lim_{n}4^{-n}h(2^nP)$. Fourier-analytic and circle-method techniques handle averages over families (moments of $L$-functions) but say nothing pointwise about an individual curve.
- **Continuation over general fields.** For $E$ over a number field that is not totally real (or a suitable soluble base change), $L(E/K,s)$ is not known to extend to $s=1$ at all — the conjecture is not yet a well-posed statement there.

## 6. The Gap

The proven implication is one-directional and rank-truncated:
$$r_{\mathrm{an}}\le 1 \;\Longrightarrow\; r=r_{\mathrm{an}},\ \ \\#Ш<\infty,$$
plus $p$-parts of the leading-coefficient formula under ordinary/irreducibility hypotheses on $p$. The gap has three components.

1. **The rank-$2$ barrier.** Produce, for a curve with $\operatorname{ord}_{s=1}L(E,s)=2$, two $\mathbb{Q}$-independent points in $E(\mathbb{Q})$ from analytic data. Equivalently: a Gross–Zagier formula for the second derivative, expressing $L''(E,1)$ as a $2\times 2$ regulator.
2. **Finiteness of $Ш$ when $r_{\mathrm{an}}\ge2$.** No case is known.
3. **From $p$-parts to the full identity.** Even where the $p$-part is proved for a set of $p$, the hypotheses (good ordinary, $\bar\rho_{E,p}$ irreducible and suitably ramified) exclude infinitely many $p$ per curve; assembling all $p$ plus the archimedean normalisation into the exact rational identity is unfinished.

## 7. Current Research (as of June 2026)

- **$p$-converse theorems and Iwasawa theory.** Burungale, Castella, Skinner, Tian and collaborators continue to relax hypotheses in the anticyclotomic main conjecture, targeting supersingular and additive-reduction primes and residually reducible $\bar\rho$. Full removal of the ordinariness hypothesis is the stated goal *(frontier — verify)*.
- **Diagonal cycles for rank $2$.** Darmon–Rotger's conjectures on Gross–Kudla–Schoen cycles, and the reciprocity laws of Bertolini–Seveso–Venerucci, aim at a rank-$2$ analogue of Gross–Zagier in the $p$-adic setting. Progress remains conditional on non-vanishing of the relevant $p$-adic $L$-values *(frontier — verify)*.
- **Distribution and statistics.** Post-Bhargava work on average Selmer ranks and Smith's $2^\infty$-Selmer machinery push toward Goldfeld's conjecture ($50\%$ rank $0$, $50\%$ rank $1$) beyond full-$2$-torsion families *(frontier — verify)*.
- **Computation.** The LMFDB and Cremona tables extend verified $\\#Ш$ ranges; quadratic Chabauty and $p$-adic height methods (Balakrishnan and collaborators) certify ranks for curves where descent alone is inconclusive.

## 8. Future Work

- Construct a **higher-rank Euler system** whose derived classes remain non-trivial when the Heegner point vanishes; this is the single structural step Kolyvagin's method lacks.
- Prove **finiteness of $Ш(E/\mathbb{Q})$** unconditionally for a curve of analytic rank $2$ — even one example would be a first.
- Establish a **second-derivative height formula**: $L''(E,1)$ as a determinant of Néron–Tate heights of cycle-theoretic points, as suggested by the Beilinson–Bloch framework.
- Prove **analytic continuation of $L(E/K,s)$** for general number fields $K$ via potential modularity, making BSD well-posed outside the totally real case.
- Sharpen the **statistical result** past $66.48\%$ toward $100\%$, which would follow from Goldfeld's conjecture together with the rank $\le 1$ theorems.

## 9. Key References

- **[Foundational]** B. Birch and H. P. F. Swinnerton-Dyer. *Notes on elliptic curves. II.* Journal für die reine und angewandte Mathematik 218 (1965), 79–108.
- **[Foundational]** B. Gross and D. Zagier. *Heegner points and derivatives of $L$-series.* Inventiones Mathematicae 84 (1986), 225–320.
- **[Foundational]** V. A. Kolyvagin. *Finiteness of $E(\mathbb{Q})$ and $Ш(E,\mathbb{Q})$ for a subclass of Weil curves.* Izvestiya Akademii Nauk SSSR, Ser. Mat. 52 (1988), 522–540.
- **[Foundational]** J. Coates and A. Wiles. *On the conjecture of Birch and Swinnerton-Dyer.* Inventiones Mathematicae 39 (1977), 223–251.
- **[SOTA / Recent]** C. Skinner and E. Urban. *The Iwasawa main conjectures for $\mathrm{GL}_2$.* Inventiones Mathematicae 195 (2014), 1–277.
- **[SOTA / Recent]** K. Rubin. *The "main conjectures" of Iwasawa theory for imaginary quadratic fields.* Inventiones Mathematicae 103 (1991), 25–68.
- **[SOTA / Recent]** K. Kato. *$p$-adic Hodge theory and values of zeta functions of modular forms.* Astérisque 295 (2004), 117–290.
- **[SOTA / Recent]** M. Bhargava, C. Skinner and W. Zhang. *A majority of elliptic curves over $\mathbb{Q}$ satisfy the Birch and Swinnerton-Dyer conjecture.* arXiv:1407.1826, 2014.
- **[SOTA / Recent]** W. Zhang. *Selmer groups and the indivisibility of Kolyvagin classes.* Cambridge Journal of Mathematics 2 (2014), 191–253.
- **[SOTA / Recent]** G. Grigorov, A. Jorza, S. Patrikis, W. Stein and C. Tarniţă. *Computational verification of the Birch and Swinnerton-Dyer conjecture for individual elliptic curves.* Mathematics of Computation 78 (2009), 2397–2425.
- **[Survey]** A. Wiles. *The Birch and Swinnerton-Dyer conjecture.* In *The Millennium Prize Problems*, Clay Mathematics Institute / AMS, 2006.
- **[Survey]** J. H. Silverman. *The Arithmetic of Elliptic Curves*, 2nd ed. Graduate Texts in Mathematics 106, Springer, 2009.
- **[Survey]** J. E. Cremona. *Algorithms for Modular Elliptic Curves*, 2nd ed. Cambridge University Press, 1997.
- **[Related]** J. B. Tunnell. *A classical Diophantine problem and modular forms of weight $3/2$.* Inventiones Mathematicae 72 (1983), 323–334.
- **[Related]** C. Breuil, B. Conrad, F. Diamond and R. Taylor. *On the modularity of elliptic curves over $\mathbb{Q}$: wild 3-adic exercises.* Journal of the AMS 14 (2001), 843–939.

## 10. Worked Example / Concrete Special Case

Take the curve of smallest conductor with positive rank, **37a1**:
$$E:\;y^2+y=x^3-x,\qquad N=37,\ \Delta=37.$$

**Analytic side.** $37$ is prime and $E$ has multiplicative reduction there. The sign of the functional equation is $w=-1$, so $r_{\mathrm{an}}$ is odd, hence $L(E,1)=0$ and $r_{\mathrm{an}}\ge 1$. Numerically, using the rapidly convergent series $L(E,1+t)$ from the newform $f=q\prod_{n\ge1}(1-q^n)^2(1-q^{37n})^2$,
$$L'(E,1)=0.3059997738\ldots,\qquad L''(E,1)\neq 0\text{-check gives } r_{\mathrm{an}}=1 .$$

**Arithmetic side.** The point $P=(0,0)$ satisfies $0+0=0-0$; one checks $E(\mathbb{Q})=\mathbb{Z}P$ with $E(\mathbb{Q})_{\mathrm{tors}}=\{\mathcal{O}\}$, so $\\#E(\mathbb{Q})_{\mathrm{tors}}=1$ and $r=1$. Canonical height:
$$\hat h(P)=0.0511114082\ldots,\qquad \mathrm{Reg}(E/\mathbb{Q})=0.0511114082\ldots$$
Real period, from $\Omega_E=\int_{E(\mathbb{R})}\frac{dx}{2y+1}$ evaluated by the AGM:
$$\Omega_E=5.9869172924\ldots$$
Reduction at $37$ is split multiplicative with $\mathrm{ord}_{37}(\Delta)=1$, so $c_{37}=1$; all other $c_p=1$. Kolyvagin's theorem applies (a Heegner point of infinite order exists), giving $\\#Ш(E/\mathbb{Q})<\infty$; descent shows $Ш=0$, so $\\#Ш=1$.

**The check.** The BSD prediction is
$$\frac{\Omega_E\cdot\mathrm{Reg}\cdot\prod_pc_p\cdot\\#Ш}{(\\#E(\mathbb{Q})_{\mathrm{tors}})^2}
=\frac{5.9869172924\times 0.0511114082\times 1\times 1}{1^2}=0.3059997738\ldots,$$
matching $L'(E,1)$ to every computed digit. Here BSD is a **theorem**, because $r_{\mathrm{an}}=1$ places the curve inside the Gross–Zagier–Kolyvagin range.

**Where it breaks.** Replace $E$ by **389a1**, $y^2+y=x^3+x^2-2x$, of conductor $389$ and rank $2$ with generators $(0,0)$ and $(1,0)$. Here $w=+1$ and numerically $L(E,1)=L'(E,1)=0$, $L''(E,1)=0.7593165\ldots$, and the predicted $2\times2$ regulator $\det\big(\langle P_i,P_j\rangle\big)=0.1524601\ldots$ matches to $30$ digits. But every Heegner point on this curve is torsion, Kolyvagin's classes vanish, and **nothing in the above proof survives**: the equality $r=2$, the finiteness of $Ш$, and the leading-coefficient identity are all unproved for this single explicit curve. That is Section 6's gap, in one example.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*