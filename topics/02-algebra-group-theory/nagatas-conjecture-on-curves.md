---
id: 02-algebra-group-theory/nagatas-conjecture-on-curves
title: "Nagata's Conjecture on Curves"
topic: 02-algebra-group-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Nagata's Conjecture on Curves

> **Topic:** Algebra & Group Theory · **ID:** `02-algebra-group-theory/nagatas-conjecture-on-curves` · **Status:** open

## 1. Problem Statement / Conjecture

Let $k$ be an algebraically closed field of characteristic $0$ and let $p_1,\dots,p_n \in \mathbb{P}^2_k$ be points in *very general* position (outside a countable union of proper closed subvarieties of $(\mathbb{P}^2)^n$).

**Conjecture (Nagata, 1959).** If $n > 9$ and $C \subset \mathbb{P}^2$ is a curve of degree $d$ with $\operatorname{mult}_{p_i} C \ge m_i$ for $i = 1,\dots,n$, then

$$d\sqrt{n} \;>\; \sum_{i=1}^{n} m_i .$$

The hypothesis $n > 9$ is necessary: for $n = 9$ the cubic through $9$ general points gives $d = 3$, $\sum m_i = 9$, so $d\sqrt{n} = \sum m_i$ and the strict inequality fails; for $n < 9$ the Del Pezzo geometry makes the correct bound a different (rational) number.

A complete proof must establish the inequality for **all** $n \ge 10$, all degrees $d$, and all multiplicity vectors $(m_1,\dots,m_n)$. A disproof requires exhibiting one $n \ge 10$ and one curve with $d\sqrt n \le \sum m_i$ over very general points. Nagata proved the conjecture when $n$ is a perfect square; every non-square $n \ge 10$ is open, including $n = 10$.

## 2. Mathematical Foundations

**Linear systems of fat points.** Write $\mathcal{L}(d; m_1,\dots,m_n)$ for the linear system of degree-$d$ plane curves with multiplicity $\ge m_i$ at $p_i$. Each multiplicity condition imposes $\binom{m_i+1}{2}$ linear conditions on the $\binom{d+2}{2}$ coefficients, so the **virtual dimension** is

$$v(d;\mathbf m) \;=\; \binom{d+2}{2} - 1 - \sum_{i=1}^n \binom{m_i+1}{2},\qquad \dim \mathcal{L} \ge \max\{v, -1\}.$$

The system is **special** if $\dim\mathcal L > \max\{v,-1\}$.

**Blow-up model.** Let $\pi : X_n \to \mathbb{P}^2$ be the blow-up at $p_1,\dots,p_n$, with exceptional divisors $E_i$ and $H = \pi^*\mathcal{O}(1)$. Then $\operatorname{Pic}(X_n) = \mathbb{Z}H \oplus \bigoplus \mathbb{Z}E_i$ with intersection form $H^2 = 1$, $E_i^2 = -1$, $H\cdot E_i = 0$. Setting $D = dH - \sum m_i E_i$,

$$D^2 = d^2 - \sum m_i^2, \qquad D\cdot K_{X_n} = -3d + \sum m_i,\qquad K_{X_n} = -3H + \sum E_i .$$

Nagata's inequality is equivalent to: the class $\sqrt{n}\,H - \sum_i E_i$ lies in the closure of the nef cone of $X_n$ for $n \ge 10$ (a statement with irrational coefficients when $n$ is not a square — hence the difficulty).

**Seshadri constant formulation.** The multi-point Seshadri constant of $\mathcal{O}_{\mathbb{P}^2}(1)$ at $n$ very general points is

$$\varepsilon(n) \;=\; \inf_{C} \frac{\deg C}{\sum_{i=1}^n \operatorname{mult}_{p_i} C}.$$

A parameter count gives $\varepsilon(n) \le 1/\sqrt{n}$ for all $n$ (systems with $v \ge 0$ are nonempty). Nagata's conjecture is exactly the reverse bound:

$$\varepsilon(n) = \frac{1}{\sqrt n}\quad (n \ge 10).$$

**Homogeneous case.** With $m_1=\dots=m_n=m$, the conjecture reads $d > m\sqrt n$; by a standard averaging/specialization argument the homogeneous case for all $n$ implies the general case.

**SHGH.** The Segre–Harbourne–Gimigliano–Hirschowitz conjecture states that $\mathcal{L}(d;\mathbf m)$ is special only if it contains a multiple $(-1)$-curve in its base locus. SHGH $\Rightarrow$ Nagata: non-speciality forces $v(d;\mathbf m) \ge 0$ for nonempty systems, and for $n \ge 10$, $d^2 + 3d \ge \sum(m_i^2+m_i)$ together with Cauchy–Schwarz yields $d\sqrt n > \sum m_i$.

## 3. History & State of the Art (SOTA)

- **1959.** Masayoshi Nagata, constructing his counterexample to **Hilbert's 14th problem** (*On the 14-th problem of Hilbert*, Amer. J. Math. 81), needed to control curves through $n = 16$ very general points. He proved the inequality for $n = k^2$, $k \ge 4$, and conjectured it for all $n > 9$.
- **1960.** *On rational surfaces II* develops the blow-up/nef-cone framework and the "$(-1)$-curve" combinatorics still used today.
- **1980s–90s.** Segre, Harbourne, Gimigliano and Hirschowitz independently formulate SHGH, subsuming Nagata into a classification of special systems.
- **1994–95.** Geng Xu's degeneration lemma yields the first uniform lower bound $\varepsilon(n) \ge 1/\sqrt{n+1}$ for $n\ge 10$ — asymptotically sharp in ratio but never sufficient.
- **1994.** McDuff–Polterovich link the statement to symplectic packing of $\mathbb{CP}^2$ by $n$ equal balls; Biran (1999) reproves packing stability using algebraic degenerations.
- **1998–2011.** Ciliberto and Miranda's degeneration of the plane to unions of surfaces proves large families of cases and, for $n = 10$, pushes the emptiness threshold to $d/m \ge 117/37 = 3.16216\ldots$ against $\sqrt{10} = 3.16227\ldots$.
- **2005.** Evain gives a new proof for $n = 4^h$ points by collision-of-fat-points techniques.
- **2007–2017.** Dumnicki, Jarnicki, Harbourne, Roé, Küronya, Szemberg develop combinatorial/computational certificates (monomial specializations, cluster algorithms) verifying broad ranges and formulating Nagata-type statements for monomial valuations.

## 4. Partial Results / Verified Cases

| Case | Status | Source |
|---|---|---|
| $n = k^2$, $k \ge 4$ (all $16, 25, 36, \dots$) | **Proved** | Nagata (1959) |
| $n = 4^h$ | Proved (independent method) | Evain (2005) |
| $n \le 9$ | Settled, but conjecture is *false as stated*; $\varepsilon(n)$ is rational and known exactly | Del Pezzo/Cremona theory |
| Homogeneous $m \le 12$, all $n$, $d$ | SHGH proved $\Rightarrow$ Nagata for these multiplicities | Ciliberto–Miranda, Trans. AMS 352 (2000) |
| Homogeneous $m \le 42$ | SHGH verified computationally | Dumnicki–Jarnicki (2007) |
| $n = 10$ | $\varepsilon(10) \ge 37/117$; gap to $1/\sqrt{10}$ is $< 1.2\times10^{-5}$ | Ciliberto–Miranda (2011) |
| General $n \ge 10$ | $\varepsilon(n) \ge 1/\sqrt{n+1}$ | Xu (1995) |
| Specific small non-squares ($n = 11,\dots$) | Improved numerical bounds via monomial specialization; none reach $1/\sqrt n$ | Dumnicki, Harbourne–Roé |
| $n \ge 10$, $\mathbf m$ with $m_i$ bounded relative to $d$ by Bézout against $(-1)$-curves | Proved | classical |

Nagata's square case also follows from a clean specialization: degenerate the $k^2$ points to the grid $\{\ell_1,\dots,\ell_k\}\cap\{\ell'_1,\dots,\ell'_k\}$ and apply Bézout against the $2k$ lines.

## 5. Principal Obstacles

- **Irrationality.** For non-square $n$, $\sqrt n \notin \mathbb{Q}$, so the conjectured extremal class $\sqrt n H - \sum E_i$ is not the class of any effective divisor and lies on the *boundary* of the nef cone at an irrational point. Standard tools — Bézout against an explicit curve, Riemann–Roch, vanishing theorems — all produce **rational** bounds and can therefore only approach $1/\sqrt n$, never reach it. Every known method is off by a positive amount.
- **No extremal curve.** For $n = k^2$ the union of $k$ lines through a grid realises equality asymptotically and anchors the proof. For $n = 10$ there is no candidate curve attaining the bound, so there is nothing to induct on or degenerate to.
- **Speciality is unclassified.** Nagata follows from SHGH, but SHGH is itself open; the base-locus analysis of $\mathcal{L}(d;m^n)$ for $n \ge 10$ is genuinely infinite — $X_n$ has infinitely many $(-1)$-curves and its effective cone is not finitely generated.
- **Degenerations lose too much.** Ciliberto–Miranda's flat degenerations of $\mathbb{P}^2$ into unions of surfaces convert the problem into a combinatorial transversality problem whose bookkeeping error grows with the number of components; the residual loss is exactly what stops $117/37$ from becoming $\sqrt{10}$.
- **Characteristic and field issues.** Some arguments (Xu's lemma, generic smoothness) use characteristic $0$; the conjecture over $\overline{\mathbb{F}_p}$ has additional pathologies for points defined over small fields.

## 6. The Gap

Proved (Section 4) is either: (a) the exact statement for perfect-square $n$, where a grid degeneration supplies an equality configuration; or (b) rational approximations $\varepsilon(n) \ge r_n$ with $r_n < 1/\sqrt n$ strictly ($r_{10} = 37/117$, and $1/\sqrt{n+1}$ in general).

Wanted (Section 1) is the irrational bound $\varepsilon(n) \ge 1/\sqrt n$ for every $n \ge 10$. The precise missing step: **an argument producing a bound not of the form $d/\!\sum m_i \ge p/q$ from a single auxiliary curve.** Concretely, one needs either

1. an infinite family of auxiliary curves $C_j$ on $X_n$ whose Bézout bounds $r_n^{(j)}$ converge to $1/\sqrt n$ (a "limit-of-$(-1)$-curves" mechanism), or
2. a proof that $\mathcal L(d;m^n)$ is non-special whenever $v(d;m^n) < 0$ for $n \ge 10$, i.e. the emptiness half of SHGH.

Closing the numerical gap $\sqrt{10} - 117/37 \approx 1.2 \times 10^{-5}$ by a *finite* computation is impossible: any finite certificate gives a rational threshold.

## 7. Current Research (as of June 2026)

- **Degeneration schools (Rome/Tor Vergata, Colorado State).** Ciliberto and Miranda's toric and semistable degeneration machinery continues to be refined for $n = 10, 11$; the aim is a self-improving degeneration whose thresholds form a sequence converging to $\sqrt n$. *(frontier — verify)*
- **Valuative / Okounkov-body methods (Kraków, Budapest).** Dumnicki, Küronya, Roé, Szemberg study Nagata-type statements for very general **monomial valuations**, replacing points by quasi-monomial valuations; the conjectural bound $\hat\mu(v) \le \sqrt{\text{vol}}$ interpolates the point case and admits continuity arguments that discrete point configurations lack.
- **Newton–Okounkov bodies and Zariski decomposition** on $X_n$: the shape of the body of $\sqrt n H - \sum E_i$ encodes the conjecture; irrational vertices are the target of current asymptotic estimates.
- **Symplectic side.** Packing-stability results for $\mathbb{CP}^2$ and ball-packing obstructions (Biran, McDuff, Hutchings' ECH capacities) give an alternative language; embedded contact homology has so far reproduced but not improved the algebraic bounds. *(frontier — verify)*
- **Computer-assisted certificates.** Dumnicki's specialization-to-monomial-ideal algorithms extend SHGH verification to larger homogeneous multiplicities and to bounded $n$; these strengthen confidence but cannot terminate the problem.

## 8. Future Work

- **Prove SHGH for uniform multiplicities.** Leading opinion (Harbourne, Ciliberto, Miranda, Roé, *Variations on Nagata's conjecture*, 2013) is that the homogeneous case of SHGH is the realistic target, and that Nagata should be attacked through the classification of special systems rather than directly.
- **Interpolate through $n$ continuously.** Treat $n$ as a real parameter via monomial or divisorial valuations; if $\varepsilon$ is continuous in the valuation and known at squares, a density/continuity argument may transfer $n = k^2$ to all $n$.
- **Find the limiting curve family.** Search on $X_{10}$ for infinite sequences of irreducible curves with $d_j/m_j \downarrow \sqrt{10}$ — their existence is predicted by the conjectured nef boundary and would be strong evidence and a proof template.
- **Higher-dimensional Nagata.** Formulate and test the analogue for $\mathbb{P}^r$, $r \ge 3$ ($\varepsilon(n) = n^{-1/r}$ asymptotically), where extra room may make degenerations cheaper.
- **Positive characteristic.** Determine whether the conjecture can fail over $\overline{\mathbb{F}_p}$ for Frobenius-special configurations; a counterexample there would sharply localise the role of characteristic $0$.

## 9. Key References

- **[Foundational]** M. Nagata. *On the 14-th problem of Hilbert.* American Journal of Mathematics **81** (1959), 766–772.
- **[Foundational]** M. Nagata. *On rational surfaces II.* Memoirs of the College of Science, University of Kyoto, Ser. A **33** (1960), 271–293.
- **[Foundational]** G. Xu. *Ample line bundles on smooth surfaces.* Journal für die reine und angewandte Mathematik **469** (1995), 199–209.
- **[SOTA]** C. Ciliberto, R. Miranda. *Degenerations of planar linear systems.* J. reine angew. Math. **501** (1998), 191–220.
- **[SOTA]** C. Ciliberto, R. Miranda. *Linear systems of plane curves with base points of equal multiplicity.* Transactions of the AMS **352** (2000), 4037–4050.
- **[SOTA]** C. Ciliberto, R. Miranda. *Homogeneous interpolation on ten points.* Journal of Algebraic Geometry **20** (2011), 685–726.
- **[SOTA]** L. Evain. *On the postulation of $s^d$ fat points in $\mathbb{P}^d$.* Journal of Algebra **285** (2005), 516–530.
- **[SOTA]** M. Dumnicki, W. Jarnicki. *New effective bounds on the dimension of a linear system in $\mathbb{P}^2$.* Journal of Symbolic Computation **42** (2007), 621–635.
- **[SOTA]** M. Dumnicki, B. Harbourne, A. Küronya, J. Roé, T. Szemberg. *Very general monomial valuations of $\mathbb{P}^2$ and a Nagata type conjecture.* Communications in Analysis and Geometry **25** (2017), 125–161.
- **[Survey]** C. Ciliberto, B. Harbourne, R. Miranda, J. Roé. *Variations on Nagata's conjecture.* In *A Celebration of Algebraic Geometry*, Clay Mathematics Proceedings **18**, AMS, 2013, 185–203.
- **[Survey]** T. Bauer, S. Di Rocco, B. Harbourne, M. Kapustka, A. Knutsen, W. Syzdek, T. Szemberg. *A primer on Seshadri constants.* In *Interactions of Classical and Numerical Algebraic Geometry*, Contemporary Mathematics **496**, AMS, 2009, 33–70.
- **[Background]** R. Lazarsfeld. *Positivity in Algebraic Geometry I.* Ergebnisse der Mathematik 48, Springer, 2004.
- **[Related]** D. McDuff, L. Polterovich. *Symplectic packings and algebraic geometry.* Inventiones Mathematicae **115** (1994), 405–429.
- **[Related]** B. Harbourne, J. Roé. *Discrete behavior of Seshadri constants on surfaces.* Journal of Pure and Applied Algebra **212** (2008), 616–627.

## 10. Worked Example / Concrete Special Case

**Goal: the elementary bound for $n = 10$, and how far it falls short.**

Take $p_1,\dots,p_{10}$ very general and let $C$ have degree $d$ and multiplicity $\ge m$ at each. Nagata predicts $d > m\sqrt{10} = 3.16227\ldots m$.

*Step 1 — auxiliary curve.* The system $\mathcal L(3;1^9)$ has virtual dimension $\binom{5}{2}-1-9 = 0$, so there is a unique cubic $E$ through $p_1,\dots,p_9$, and for general points $E$ is smooth and irreducible.

*Step 2 — Bézout.* Assume $E \not\subset C$. Then $E \cdot C = 3d$ counted with multiplicity, and each $p_i$ ($i \le 9$) contributes at least $\operatorname{mult}_{p_i}E \cdot \operatorname{mult}_{p_i}C = m$:

$$3d \;=\; E\cdot C \;\ge\; \sum_{i=1}^{9} m \;=\; 9m \quad\Longrightarrow\quad d \ge 3m .$$

*Step 3 — the containment case.* If $E \subset C$, write $C = E + C'$ with $\deg C' = d-3$ and $\operatorname{mult}_{p_i}C' \ge m-1$ for $i \le 9$. Induction on $m$ gives $d-3 \ge 3(m-1)$, i.e. $d \ge 3m$ again. Hence $\varepsilon(10) \ge 1/3$ unconditionally, from one cubic.

*Step 4 — the residual gap.* The elementary bound gives $d/(10m) \ge 3/(10) = 0.3$, i.e. $\varepsilon(10)\ge 0.3$, while the conjecture asserts $\varepsilon(10) = 1/\sqrt{10} = 0.316227\ldots$ Ciliberto–Miranda's ten-point degeneration replaces the ratio $3$ by $117/37 = 3.162162\ldots$, leaving

$$\sqrt{10} - \frac{117}{37} \;=\; 3.1622776\ldots - 3.1621621\ldots \;\approx\; 1.15\times 10^{-4}.$$

*Step 5 — why no rational curve closes it.* Suppose some irreducible curve $B$ of degree $\delta$ with multiplicity $\mu$ at each $p_i$ gave the sharp bound by Bézout: one would get $d/m \ge 10\mu/\delta \ge \sqrt{10}$, forcing $\delta/\mu \le \sqrt{10}$, i.e. $B$ itself violates the conjecture. So **no single auxiliary curve can prove Nagata for $n = 10$** — the bound must come from an infinite process. This is the content of Section 6.

*Contrast — the square case $n = 16$.* Specialize the $16$ points to the grid $\ell_i \cap \ell'_j$, $1\le i,j\le 4$. For a curve $C$ of degree $d$ with multiplicity $\ge m$ at all $16$ nodes, Bézout against each of the $4$ lines $\ell_i$ gives $d \ge 4m$ (each $\ell_i$ meets $C$ with multiplicity $\ge m$ at $4$ points), and $4 = \sqrt{16}$ exactly. Semicontinuity transfers the bound to very general points. The rationality of $\sqrt{16}$ is precisely what makes the grid work — and precisely what is unavailable for $n = 10$.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*