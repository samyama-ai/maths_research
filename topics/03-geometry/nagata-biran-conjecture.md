---
id: 03-geometry/nagata-biran-conjecture
title: "Nagata-Biran Conjecture"
topic: 03-geometry
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Nagata-Biran Conjecture

> **Topic:** Algebraic & Differential Geometry · **ID:** `03-geometry/nagata-biran-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Let $X$ be a smooth complex projective surface and $L$ an ample line bundle on $X$. For $r \geq 1$ very general points $p_1,\dots,p_r \in X$, the **multi-point Seshadri constant** is

$$\varepsilon(X,L;r) \;=\; \inf_{C} \frac{L\cdot C}{\sum_{i=1}^{r}\operatorname{mult}_{p_i} C},$$

the infimum over irreducible curves $C \subset X$ meeting at least one $p_i$. A volume/degree count gives the universal upper bound $\varepsilon(X,L;r) \le \sqrt{L^2/r}$.

**Conjecture (Nagata–Biran).** For every smooth projective surface $X$ and ample $L$ there is an $r_0 = r_0(X,L)$ such that

$$\varepsilon(X,L;r) \;=\; \sqrt{\frac{L^2}{r}} \qquad \text{for all } r \ge r_0 .$$

Biran's explicit form takes $r_0 = 9L^2$ (with $L$ a line bundle, so $L^2 \in \mathbb{Z}_{>0}$). The case $X = \mathbb{P}^2$, $L = \mathcal{O}(1)$, $L^2 = 1$, $r_0 = 9$ is **Nagata's conjecture**: for $r \ge 10$ very general points and any plane curve of degree $d$ with multiplicities $m_i$ at them,

$$d \;>\; \frac{1}{\sqrt{r}}\sum_{i=1}^{r} m_i .$$

A proof must exclude *all* curves violating the bound, for every $r \ge r_0$; a disproof needs one surface, one ample $L$, and an infinite family (or arbitrarily large $r$) of "unexpected" curves with $L\cdot C \le \sqrt{L^2/r}\sum_i \operatorname{mult}_{p_i}C$ beyond the conjectured range.

## 2. Mathematical Foundations

Let $\pi: \widetilde{X} \to X$ be the blow-up at $p_1,\dots,p_r$ with exceptional divisors $E_1,\dots,E_r$. Then

$$\varepsilon(X,L;r) \;=\; \sup\bigl\{\,t \in \mathbb{R}_{>0} \;:\; \pi^*L - t\textstyle\sum_i E_i \ \text{is nef}\,\bigr\}.$$

Since $(\pi^*L - t\sum E_i)^2 = L^2 - r t^2 \ge 0$ is necessary for a nef class, $\varepsilon \le \sqrt{L^2/r}$. The conjecture therefore says: **for $r \gg 0$ the nef cone of $\widetilde X$ is cut out along the symmetric ray exactly by the quadratic form**, i.e. the Zariski chamber structure degenerates to the "round" bound and no Seshadri-exceptional curve intervenes.

Equivalently, on $\mathbb{P}^2$, in terms of linear systems: let $\mathcal{L}_r(d;m)$ be plane curves of degree $d$ with multiplicity $\ge m$ at $r$ general points. The naive count

$$\operatorname{vdim}\mathcal{L}_r(d;m) = \binom{d+2}{2} - r\binom{m+1}{2} - 1$$

is nonnegative roughly when $d \gtrsim m\sqrt{r}$; Nagata asserts that no curve exists below the threshold $d = m\sqrt{r}$, i.e. that the only obstruction is the expected one, sharpened to a strict inequality. The related **Waldschmidt constant** $\widehat{\alpha}(r) = \lim_{k} \alpha(I^{(k)})/k$ of the ideal of $r$ general points satisfies $\widehat{\alpha}(r) = 1/\varepsilon(\mathcal{O}(1);r)$, so Nagata reads $\widehat\alpha(r) = \sqrt{r}$ for $r \ge 9$.

Nagata's original motivation: the counterexample to **Hilbert's 14th problem**. For $r = s^2 \ge 16$ points, the ring of invariants of a suitable linear action fails to be finitely generated, and the proof rests exactly on $\varepsilon(\mathcal{O}(1); s^2) = 1/s$.

**Symplectic dictionary.** $\varepsilon(X,L;r) \ge t$ relates to embedding $r$ disjoint equal symplectic balls of capacity $\propto t^2$ into $(X,\omega_L)$; the packing is *full* when the total volume is attained. The Nagata–Biran statement is the algebraic strengthening of **packing stability**.

## 3. History & State of the Art (SOTA)

- **1959.** Nagata (*On the 14-th problem of Hilbert*, Amer. J. Math. 81) proves the inequality $d > m\sqrt{r}$ for $r = s^2$ a perfect square, $s \ge 4$, and conjectures it for all $r \ge 10$. His method: a specialization/induction using the Cremona group, which is genuinely square-specific.
- **1994–95.** Xu (*Curves in $\mathbb{P}^2$ and symplectic packings*, Math. Ann. 299; *Ample line bundles on smooth surfaces*, J. Reine Angew. Math. 469) proves the key differentiation lemma $C^2 \ge m(m-1)$ for irreducible curves with multiplicity $m$ at general points, giving the first uniform bounds $\varepsilon(\mathcal{O}(1);r) \ge 1/(\sqrt r + 1)$-type estimates.
- **1994.** McDuff–Polterovich (*Symplectic packings and algebraic geometry*, Invent. Math. 115) translate the packing problem into Kähler-cone language, computing packing numbers of $\mathbb{P}^2$ for $k \le 9$.
- **1999.** Biran proves **packing stability** (*A stability property of symplectic packing*, Invent. Math. 136): every closed symplectic 4-manifold with rational symplectic class admits full packings by $k$ equal balls for all $k \ge k_0$; for $\mathbb{P}^2$, $k_0 = 9$. In *Constructing new ample divisors out of old ones* (Duke Math. J. 98) he builds the algebraic counterparts and formulates the general surface conjecture, later surveyed in his ECM 2000 lecture.
- **1998–2007.** Ciliberto–Miranda's degeneration technique and Dumnicki's cutting-diagram/linear-programming methods verify the inequality for bounded multiplicities.
- **2008–2019.** Harbourne–Roé (discreteness of Seshadri constants), Dumnicki–Küronya–Maclean–Szemberg (Newton–Okounkov reformulation), and the containment/resurgence literature give equivalent formulations without resolving any new $r$.

**SOTA summary:** the conjecture is open for every non-square $r \ge 10$ on $\mathbb{P}^2$, and the best general lower bounds at $r=10$ sit just under the conjectural $1/\sqrt{10}\approx 0.316228$ (numerically around $0.3161$).

## 4. Partial Results / Verified Cases

- **$X = \mathbb{P}^2$, $r \le 9$:** completely known and classical: $\varepsilon(\mathcal O(1);r) = 1,\ \tfrac12,\ \tfrac12,\ \tfrac12,\ \tfrac25,\ \tfrac25,\ \tfrac38,\ \tfrac6{17},\ \tfrac13$ for $r=1,\dots,9$. At $r=9$ the cubic through the points gives $3/9 = \sqrt{1/9}$, so the conjectured equality already holds at $r_0 = 9$.
- **Perfect squares:** Nagata's theorem gives $\varepsilon(\mathcal O(1); s^2) = 1/s$ for all $s \ge 4$, hence $\varepsilon(\mathcal O(k); s^2) = k/s = \sqrt{k^2/s^2}$; equality holds for every $L=\mathcal O(k)$ whenever $r$ is a square.
- **Bounded multiplicity:** for equal multiplicities $m$ at $r \ge 10$ general points, the inequality $d > m\sqrt r$ is verified for all $m$ up to roughly $m \le 42$ by the degeneration method of Ciliberto–Miranda and the algorithmic methods of Dumnicki and Dumnicki–Jarnicki. Each new $m$ is a finite but rapidly growing computation.
- **Implication from SHGH:** the Segre–Harbourne–Gimigliano–Hirschowitz conjecture (only $(-1)$-curves cause speciality) implies Nagata; SHGH is itself known for $r \le 9$ and for bounded multiplicities.
- **Symplectic version (proved):** Biran's packing stability gives full packings of $\mathbb{P}^2$ by $k$ equal balls for all $k \ge 9$, and of rational ruled surfaces for $k \gg 0$ (Buse–Pinsonnault; Opshtein for maximal packings of $\mathbb{P}^2$). This is the transcendental shadow of the conjecture and is *not* equivalent to it.
- **Other surfaces:** the conjecture is known for $(X,L)$ where $L^2 \cdot r$ is a square and a Nagata-type transfer applies (e.g. $\mathbb{P}^1\times\mathbb{P}^1$ with $L = \mathcal O(1,1)$ at $r = 2s^2$ points), and trivially for $r$ small enough that an explicit curve attains $\sqrt{L^2/r}$.

## 5. Principal Obstacles

- **Irrationality barrier.** If $L^2 r$ is not a perfect square, the conjecture forces $\varepsilon = \sqrt{L^2/r} \notin \mathbb{Q}$. **No irrational Seshadri constant is known to exist on any variety.** Proving Nagata for a single non-square $r$ would produce the first one, so every technique that certifies nef-ness by exhibiting a rational curve class or a finite computation is structurally incapable of closing the case.
- **Infinitely many curves must be excluded.** For non-square $r$ the infimum is not attained; one must rule out an infinite family of potential Seshadri-exceptional curves whose degrees $d$ approach $m\sqrt r$ from above. Finite algorithms (Dumnicki's linear programming, degeneration to bounded $m$) handle one $m$ at a time and do not stabilize.
- **Cremona fails off the squares.** Nagata's induction uses quadratic transformations that permute a square array of points; the group action has no analogue for general $r$, and no other group acting on $\mathbb{P}^2$ blown up at $r \ge 10$ general points is known to be large enough (the Weyl group $W_{E_r}$ is infinite but does not act on the *general* point configuration in the needed way).
- **Positivity methods are volume-blind.** Vanishing theorems, multiplier ideals, and Newton–Okounkov bodies all reproduce the quadratic bound $L^2 - rt^2 \ge 0$ but cannot distinguish nef from "numerically not obviously non-nef" at the boundary; the conjecture is precisely the statement that the boundary is achieved, so these techniques give the upper bound for free and no lower bound.
- **Symplectic input is too coarse.** Full symplectic packing certifies that a class lies in the *symplectic cone*, which is open and cut out by finitely many exceptional-sphere inequalities. The algebraic nef cone can be strictly smaller because effective algebraic curves of high degree impose extra conditions. So Biran's theorem, though it settles the packing analogue for $\mathbb{P}^2$ and $k\ge 9$, leaves Nagata untouched.

## 6. The Gap

Proved: equality at $r \le 9$ on $\mathbb{P}^2$; equality for all perfect-square $r$; the inequality restricted to curves of multiplicity $m \lesssim 42$; the symplectic (Kähler-cone) analogue for $k \ge 9$.

Open: for a single non-square $r \ge 10$, exclude curves of unbounded multiplicity. The precise missing step is an **effective, multiplicity-uniform lower bound** on $\deg C$ for irreducible curves singular at $r$ very general points — a bound of the form $d \ge m\sqrt r$ valid for all $m$, rather than $d \ge m\sqrt{r}\,(1 - c/m)$ which is what Xu-type differentiation currently yields. Equivalently: upgrade the symplectic-cone statement to a statement about the closure of the effective cone of $\widetilde X$, i.e. show that the symmetric nef ray is not chopped off by any algebraic curve.

## 7. Current Research (as of June 2026)

- **Newton–Okounkov and infinitesimal flag valuations.** Küronya, Szemberg, Dumnicki, Maclean and collaborators (Kraków, Essen) reformulate $\varepsilon$ via concave functions on Okounkov bodies; the aim is to convert Nagata into a convex-geometry statement about a single body. Progress remains structural.
- **Symbolic powers, containment and resurgence.** Harbourne, Bauer, Nagel, Seceleanu and others study $\widehat\alpha(r)$ and $I^{(m)} \subseteq I^{r}$ containments; sharp Waldschmidt-constant bounds for general points feed directly into Nagata. *(frontier — verify)*
- **Computational certification.** Dumnicki-school linear-programming and specialization codes push verified multiplicity ranges upward for $r = 10, 11, 12$; each increment is incremental in $m$ only.
- **Symplectic packing beyond stability.** Buse–Pinsonnault, Opshtein, and the ball-packing/ECH-capacity community (Cornell, Paris) compute packing numbers for ruled and rational surfaces, sharpening $k_0$ and testing whether $9L^2$ is optimal in Biran's form. *(frontier — verify)*
- **Higher-dimensional analogues.** Multi-point Seshadri constants on $\mathbb{P}^n$ and abelian varieties, where even the square cases are largely open.

## 8. Future Work

- Prove existence of *some* irrational Seshadri constant, by any construction; this would remove the psychological and technical barrier flagged in §5.
- Find a substitute for the Cremona induction: a degeneration of $\mathbb{P}^2$ (Ciliberto–Miranda style) whose central fibre encodes non-square $r$, with a matching semicontinuity argument for arbitrarily large $m$.
- Establish Nagata for a single non-square value, most plausibly $r = 10$, where the numerical gap is $\lesssim 5\times10^{-4}$.
- Determine whether Biran's bound $r_0 = 9L^2$ is sharp for surfaces other than $\mathbb{P}^2$, e.g. K3 surfaces and abelian surfaces where $L^2$ can be large and Picard lattices are computable.
- Settle SHGH for equal multiplicities, which implies Nagata outright.

## 9. Key References

- **[Foundational]** M. Nagata. *On the 14-th problem of Hilbert.* American Journal of Mathematics **81** (1959), 766–772. [DOI](https://doi.org/10.2307/2372927)
- **[Foundational]** P. Biran. *A stability property of symplectic packing.* Inventiones Mathematicae **136** (1999), 123–155. [DOI](https://doi.org/10.1007/s002220050306)
- **[Foundational]** P. Biran. *Constructing new ample divisors out of old ones.* Duke Mathematical Journal **98** (1999), 113–135. [DOI](https://doi.org/10.1215/s0012-7094-99-09803-4)
- **[Foundational]** D. McDuff, L. Polterovich. *Symplectic packings and algebraic geometry.* Inventiones Mathematicae **115** (1994), 405–429. [DOI](https://doi.org/10.1007/bf01231766)
- **[Foundational]** G. Xu. *Curves in $\mathbb{P}^2$ and symplectic packings.* Mathematische Annalen **299** (1994), 609–613.
- **[Foundational]** G. Xu. *Ample line bundles on smooth surfaces.* Journal für die reine und angewandte Mathematik **469** (1995), 199–209. [DOI](https://doi.org/10.1515/crll.1995.469.199)
- **[Survey]** T. Bauer, S. Di Rocco, B. Harbourne, M. Kapustka, A. Knutsen, W. Syzdek, T. Szemberg. *A primer on Seshadri constants.* Contemporary Mathematics **496**, AMS (2009), 33–70. [DOI](https://doi.org/10.1090/conm/496/09718)
- **[Survey]** R. Lazarsfeld. *Positivity in Algebraic Geometry I.* Ergebnisse der Mathematik 48, Springer, 2004 (Chapter 5). [DOI](https://doi.org/10.1007/978-3-642-18808-4)
- **[Survey]** P. Biran. *From symplectic packing to algebraic geometry and back.* European Congress of Mathematics, Vol. II (Barcelona, 2000), Progress in Mathematics 202, Birkhäuser (2001), 507–524. [DOI](https://doi.org/10.1007/978-3-0348-8266-8_44)
- **[SOTA / Recent]** C. Ciliberto, R. Miranda. *Linear systems of plane curves with base points of equal multiplicity.* Transactions of the AMS **352** (2000), 4037–4050. [DOI](https://doi.org/10.1090/s0002-9947-00-02416-8)
- **[SOTA / Recent]** M. Dumnicki, W. Jarnicki. *New effective bounds on the dimension of a linear system in $\mathbb{P}^2$.* Journal of Symbolic Computation **42** (2007), 621–635.
- **[SOTA / Recent]** B. Harbourne, J. Roé. *Discrete behavior of Seshadri constants on surfaces.* Journal of Pure and Applied Algebra **212** (2008), 616–627. [DOI](https://doi.org/10.1016/j.jpaa.2007.06.018)
- **[SOTA / Recent]** O. Buse, M. Pinsonnault. *Packing numbers of rational ruled four-manifolds.* Journal of Symplectic Geometry **11** (2013), 269–316. [DOI](https://doi.org/10.4310/jsg.2013.v11.n2.a5)

## 10. Worked Example / Concrete Special Case

Take $X = \mathbb{P}^1 \times \mathbb{P}^1$, $L = \mathcal O(1,1)$, so $L^2 = 2$ and curves of bidegree $(a,b)$ satisfy $L\cdot C = a+b$.

**Case $r = 8$ (equality, provable).** The bound is $\sqrt{L^2/r} = \sqrt{2/8} = 1/2$. Since $h^0(\mathcal O(2,2)) = 9$, passing through $8$ general points imposes $8$ conditions and leaves a nonzero section: there is a curve $C$ of bidegree $(2,2)$ through all eight points, irreducible for a general configuration. Then

$$\frac{L\cdot C}{\sum_i \operatorname{mult}_{p_i} C} = \frac{2+2}{8} = \frac12 = \sqrt{\frac{L^2}{8}} .$$

Combined with the universal upper bound, $\varepsilon(L;8) = 1/2$ exactly. The conjecture holds, and the infimum is attained by one curve because $L^2 r = 16$ is a square.

**Case $r = 9$ (open, irrational).** Now $\sqrt{L^2/r} = \sqrt{2}/3 \approx 0.4714$, which is **irrational**, so no single curve can attain it: the conjecture asserts an infinite sequence $C_k$ with $(L\cdot C_k)/\sum_i m_i(C_k) \downarrow \sqrt2/3$ and nothing below.

Check the naive count. A curve of bidegree $(a,a)$ with multiplicity $m$ at $9$ general points is expected to exist when

$$h^0(\mathcal O(a,a)) - 9\binom{m+1}{2} = (a+1)^2 - \frac{9m(m+1)}{2} > 0 ,$$

i.e. asymptotically $a > m\sqrt{9/2} = 2.1213\,m$. Such a curve gives ratio

$$\frac{2a}{9m} > \frac{2 \cdot 2.1213\,m}{9m} = 0.4714 = \frac{\sqrt2}{3}.$$

The expected-dimension threshold reproduces the conjectural value **exactly**. So the conjecture at $r=9$ says precisely: *no unexpected (superabundant) curve of bidegree below the count exists.* Concretely, at $m = 7$ one needs $a \ge 15$ for the count to be positive ($(15+1)^2 = 256 > 9\cdot 28 = 252$), and $2\cdot 15/(9\cdot 7) = 30/63 = 0.47619 > \sqrt2/3$; the conjecture forbids any $(14,14)$ curve with a $7$-fold point at nine general points, whose ratio would be $28/63 = 0.4444 < \sqrt2/3$. Ruling out this one curve is a finite check; ruling out all $m$ simultaneously is the open problem.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*