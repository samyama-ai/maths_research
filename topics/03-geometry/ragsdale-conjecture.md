---
id: 03-geometry/ragsdale-conjecture
title: "Ragsdale Conjecture"
topic: 03-geometry
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Ragsdale Conjecture

> **Topic:** Algebraic & Differential Geometry · **ID:** `03-geometry/ragsdale-conjecture` · **Status:** solved-recently (disproved 1993; the underlying extremal problem remains open)

## 1. Problem Statement / Conjecture

Let $C \subset \mathbb{RP}^2$ be a nonsingular real plane algebraic curve of even degree $d = 2k$, i.e. the real point set of a curve defined by a real homogeneous polynomial $f$ of degree $2k$ with no real or complex singular points. Every connected component of $C$ is then an *oval*: a circle in $\mathbb{RP}^2$ bounding a disc. An oval is **even** if it lies inside an even number of other ovals, **odd** otherwise. Write $p$ for the number of even ovals and $n$ for the number of odd ovals.

**Ragsdale's conjecture (1906).** For every nonsingular curve of degree $2k$,
$$p \le \tfrac{3k^2 - 3k + 2}{2}, \qquad n \le \tfrac{3k^2 - 3k}{2}.$$

A disproof requires exhibiting a nonsingular real curve of some even degree violating one of the two inequalities; a proof requires deriving them from the degree alone. Ragsdale's bounds are exactly the values attained by the curves produced by Harnack's and Hilbert's classical constructions, and she verified them for those families.

**Status.** The first inequality is **false**: Itenberg (1993) built nonsingular curves of degree $2k$, $k \ge 5$, with
$$p = \tfrac{3k^2-3k+2}{2} + \left\lfloor \tfrac{(k-3)^2}{4} \right\rfloor,$$
the smallest case being a degree-$10$ curve with $p = 32 > 31$. The *Ragsdale problem* — determining $\max p$ and $\max n$ as functions of $k$, a sub-question of the first part of Hilbert's 16th problem — remains open beyond the leading asymptotic term.

## 2. Mathematical Foundations

Let $f$ be a real homogeneous form of degree $2k$; since $2k$ is even, the sign of $f$ is well defined on $\mathbb{RP}^2$. Put
$$B_+ = \{x \in \mathbb{RP}^2 : f(x) \ge 0\}, \qquad B_- = \{x : f(x) \le 0\},$$
choosing the sign so that $B_+$ does not contain the "outer" non-orientable part. Then $B_+$ is a compact surface with boundary $C$, and the even/odd counts compute its Euler characteristic:
$$\chi(B_+) = p - n .$$
Both $p$ and $n$ are invariants of the *real scheme* of $C$ — the isotopy type of $C \subset \mathbb{RP}^2$, encoded in Viro's bracket notation, e.g. $\langle 5 \amalg 1\langle 5\rangle\rangle$ for five empty ovals plus one oval containing five.

Three classical constraints frame the problem.

- **Harnack's inequality (1876).** The number of connected components satisfies
  $$p + n \le \frac{(d-1)(d-2)}{2} + 1 = 2k^2 - 3k + 2,$$
  with equality for *M-curves*.
- **Petrovskii's inequalities (1938).** For nonsingular curves of degree $2k$,
  $$p - n \le \tfrac{3}{2}k(k-1) + 1, \qquad n - p \le \tfrac{3}{2}k(k-1).$$
  These are the correct "half" of Ragsdale's guesses: Ragsdale's conjecture asserts the same bounds for $p$ and $n$ separately.
- **Combined upper bound.** Adding Harnack and Petrovskii:
  $$p \le \tfrac{7}{4}k^2 - \tfrac{9}{4}k + \tfrac{3}{2}, \qquad n \le \tfrac{7}{4}k^2 - \tfrac{9}{4}k + 1 .$$

The main construction tool is **Viro's patchworking**. Given a convex lattice triangulation $\tau$ of the Newton triangle $T_d = \{(i,j) : i,j \ge 0,\ i+j \le d\}$ — convex meaning induced by a piecewise-linear convex function $\nu : T_d \to \mathbb{R}$ — and a sign distribution $\varepsilon : \tau^{(0)} \to \{\pm\}$ on vertices, one forms
$$f_t(x,y) = \sum_{(i,j)} \varepsilon_{ij}\, t^{\nu(i,j)} x^i y^j .$$
**Viro's theorem:** for small $t>0$ the curve $\{f_t = 0\}$ is nonsingular and isotopic in $\mathbb{RP}^2$ to the piecewise-linear curve assembled from the sign-changing edges in the four reflected copies of $T_d$. When $\tau$ is *primitive* (all triangles of area $1/2$), the result is a **T-curve**, and its topology is pure combinatorics.

## 3. History & State of the Art (SOTA)

- **1876** — Harnack proves the component bound and constructs curves attaining it.
- **1891** — Hilbert constructs M-sextics with a different scheme; the classification of degree-6 schemes becomes the seed of Hilbert's 16th problem (1900).
- **1906** — Virginia Ragsdale, in *On the arrangement of the real branches of plane algebraic curves* (Amer. J. Math. 28), isolates $p$ and $n$ as the right invariants, proves her bounds for Harnack- and Hilbert-type curves, and asks whether they hold in general.
- **1938** — Petrovskii proves $p - n \le \frac32 k(k-1)+1$ via Morse theory on $B_+$ and an index/Euler-characteristic count, the first general theorem in this direction.
- **1970s** — Arnold, Rokhlin, Gudkov, Kharlamov: congruences and complex-orientation formulas complete degree 6 and restrict degree 7–8. Ragsdale's conjecture is not touched by these methods.
- **1979–1984** — Viro develops patchworking and settles degree 7; constructions violating natural strengthenings of Ragsdale's inequalities appear, casting doubt on the conjecture *(frontier — verify attribution of the specific pre-1993 strengthenings)*.
- **1993** — Itenberg, *Contre-exemples à la conjecture de Ragsdale* (C. R. Acad. Sci. Paris 317), disproves the $p$-inequality using primitive convex triangulations of $T_{2k}$.
- **1995** — Haas gives a second family ("multilucarnes"); Itenberg extends the T-curve analysis in *Counter-examples to Ragsdale conjecture and T-curves*.
- **1996** — Itenberg & Viro publish the expository account in *The Mathematical Intelligencer*.
- **2000s–present** — the constructions are absorbed into tropical geometry (Itenberg–Mikhalkin–Shustin); asymptotically maximal families in toric varieties (Bertrand; Itenberg–Viro) push on the remaining gap.

## 4. Partial Results / Verified Cases

- **$k \le 4$ (degrees 2, 4, 6, 8).** Both Ragsdale inequalities hold. For $d \le 6$ this follows from the complete classification of real schemes (Gudkov); for $d = 8$ from Harnack plus the Petrovskii and Gudkov–Rokhlin congruence constraints. Degree $8$ gives $p \le 25$, $n \le 24$, which no known octic exceeds.
- **The difference form is a theorem.** $p - n \le \frac32 k(k-1)+1$ and $n - p \le \frac32 k(k-1)$ hold for all $k$ (Petrovskii 1938). So Ragsdale's bounds fail only "jointly with" many odd ovals.
- **Sharpness at small $k$.** For $k = 3$ (sextics) both bounds are attained: Harnack's M-sextic has $(p,n) = (10,1)$; Hilbert's has $(2,9)$.
- **Counterexample range.** $p > \frac{3k^2-3k+2}{2}$ is realized for every $k \ge 5$, with excess $\lfloor (k-3)^2/4 \rfloor$: excess $1$ at $k=5$ (degree 10, $p=32$), $2$ at $k=6$, $4$ at $k=7$, growing like $k^2/4$.
- **Asymptotics of the $p$-part.** The counterexamples give $\max p \ge \frac74 k^2 + O(k)$, matching the Harnack+Petrovskii upper bound $\frac74 k^2 + O(k)$. The leading constant $7/4$ is therefore settled; only the $O(k)$ term is open.
- **Odd ovals.** The $n$-inequality is much more resistant; T-curve methods yield curves with large $n$ but the classical bound has not been broken by the same margin *(frontier — verify current best)*.

## 5. Principal Obstacles

- **Topology sees only $\chi$.** Morse theory on $B_+$, the engine of Petrovskii's proof, controls $\chi(B_+) = p - n$ and nothing finer. Adding the $\mathbb{Z}/2$-Betti numbers back in requires a bound on $b_0(B_+)$ alone, and no complex-geometric quantity is known to dominate it.
- **Congruences constrain only M- and $(M{-}1)$-curves.** Gudkov–Rokhlin ($p - n \equiv k^2 \bmod 8$ for M-curves) and Rokhlin's complex orientation formula are strong precisely where the extremal examples are *not*: Itenberg's counterexamples are far from maximal in total oval count.
- **Bézout is too coarse for nests of depth 1.** The standard technique — intersect with auxiliary curves and bound intersection numbers — bites on deep nests. Counterexamples pile up shallow even ovals, where Bézout gives nothing better than Harnack.
- **Construction outruns obstruction.** Patchworking translates the problem to convex lattice triangulations, so lower bounds are combinatorics; upper bounds still require complex algebraic geometry (Hodge theory, Rokhlin's way). The two languages do not currently meet, so no matching second-order term is available on either side.
- **Non-realizability is hard.** Proving that a given real scheme is *not* algebraic remains a case-by-case art with no general algorithm.

## 6. The Gap

Proven: $p \le \frac74 k^2 - \frac94 k + \frac32$ (Harnack + Petrovskii), and $p \ge \frac74 k^2 + O(k)$ by construction. Conjectured (falsely): $p \le \frac32 k^2 + O(k)$.

The residual gap is the linear term. Define $P(k) = \max\{p(C) : C$ nonsingular of degree $2k\}$. Then
$$\tfrac{3k^2-3k+2}{2} + \left\lfloor \tfrac{(k-3)^2}{4}\right\rfloor \le P(k) \le \tfrac{7}{4}k^2 - \tfrac94 k + \tfrac32 .$$
At $k = 5$ this reads $32 \le P(5) \le 34$. Closing it requires either (i) a patchwork or tropical construction whose even-oval count matches the Petrovskii–Harnack bound term by term, or (ii) a non-realizability theorem for the schemes between the two values — an obstruction stronger than Petrovskii's, sensitive to $p$ rather than $p-n$. The analogous question for $n$ is wider still: no counterexample of comparable strength to the $n$-inequality is known.

## 7. Current Research (as of June 2026)

- **Tropical/patchworking school** (Itenberg, Mikhalkin, Shustin, Brugallé, Bertrand; Paris–Jussieu, Genève, Tel Aviv). Extends combinatorial patchworking to hypersurfaces in toric varieties and to real enumerative invariants; asymptotically maximal families are the main output.
- **"Rokhlin's way"** (Degtyarev, Kharlamov, Orevkov; Bilkent, Strasbourg, Steklov St. Petersburg). Complex-orientation formulas, Hodge-theoretic congruences, and braid-monodromy non-realizability arguments — the source of any future improvement on the upper side. Orevkov's braid techniques give the sharpest degree-8 and degree-9 prohibitions.
- **Computational realizability.** Enumeration of convex primitive triangulations of $T_{2k}$ for $k \le 7$, and SAT/SMT-assisted searches over sign distributions, to test whether $P(5) = 33$ or $34$ *(frontier — verify; no published resolution known)*.
- **Higher dimensions.** Ragsdale-type bounds for $\dim \ge 3$ real hypersurfaces, where Viro-style constructions again beat naive expectations.

## 8. Future Work

- Prove or refute $P(5) = 32$; a single degree-10 answer would calibrate the linear term.
- Find an upper bound on $p$ that uses more than $\chi(B_+)$ — e.g. a bound on $b_0$ of $B_+$ from the Hodge structure of the double cover of $\mathbb{CP}^2$ branched along $C$.
- Determine whether the $n$-inequality $n \le \frac32 k(k-1)$ is false, and if so, at what degree.
- Characterize which "excess" real schemes are T-realizable versus algebraically realizable but not T-realizable; the gap between the two classes is itself unmapped.
- Transfer the counterexample mechanism to real hypersurfaces in $\mathbb{RP}^m$ and to Hilbert's 16th problem for limit cycles, where analogous Ragsdale-type heuristics remain untested.

## 9. Key References

- **[Foundational]** V. Ragsdale. *On the arrangement of the real branches of plane algebraic curves.* American Journal of Mathematics **28** (1906), 377–404.
- **[Foundational]** I. G. Petrovskii. *On the topology of real plane algebraic curves.* Annals of Mathematics **39** (1938), 189–209.
- **[Foundational]** D. Hilbert. *Mathematische Probleme.* Nachrichten der Gesellschaft der Wissenschaften zu Göttingen, 1900 (Problem 16).
- **[Key construction]** O. Ya. Viro. *Gluing of plane real algebraic curves and constructions of curves of degrees 6 and 7.* In *Topology (Leningrad 1982)*, Lecture Notes in Mathematics **1060**, Springer, 1984, 187–200.
- **[Disproof]** I. Itenberg. *Contre-exemples à la conjecture de Ragsdale.* Comptes Rendus de l'Académie des Sciences Paris, Série I **317** (1993), 277–282.
- **[SOTA]** I. Itenberg. *Counter-examples to Ragsdale conjecture and T-curves.* Contemporary Mathematics **182**, American Mathematical Society, 1995, 55–72.
- **[SOTA]** B. Haas. *Les multilucarnes: nouveaux contre-exemples à la conjecture de Ragsdale.* Comptes Rendus de l'Académie des Sciences Paris, Série I **320** (1995), 1507–1512.
- **[Survey]** I. Itenberg and O. Viro. *Patchworking algebraic curves disproves the Ragsdale conjecture.* The Mathematical Intelligencer **18** (1996), no. 4, 19–28.
- **[Survey]** G. Wilson. *Hilbert's sixteenth problem.* Topology **17** (1978), 53–73.
- **[Survey]** A. Degtyarev and V. Kharlamov. *Topological properties of real algebraic varieties: Rokhlin's way.* Russian Mathematical Surveys **55** (2000), 735–814.
- **[Survey]** O. Ya. Viro. *Progress in the topology of real algebraic varieties over the last six years.* Russian Mathematical Surveys **41** (1986), 55–82.
- **[Book]** I. Itenberg, G. Mikhalkin, E. Shustin. *Tropical Algebraic Geometry.* Oberwolfach Seminars **35**, Birkhäuser, 2007.

## 10. Worked Example / Concrete Special Case

**Sextics, $k = 3$ — the bounds are sharp and consistent.**

Ragsdale's bounds give $p \le \frac{27-9+2}{2} = 10$ and $n \le \frac{27-9}{2} = 9$. Harnack's bound gives $p + n \le 2\cdot 9 - 9 + 2 = 11$; Petrovskii gives $p - n \le 10$ and $n - p \le 9$.

Gudkov's classification says a nonsingular sextic with 11 ovals has one of exactly three real schemes:

| scheme | ovals outside all others | ovals inside one | $p$ | $n$ | $p-n$ |
|---|---|---|---|---|---|
| Harnack $\langle 9 \amalg 1\langle 1\rangle\rangle$ | 10 | 1 | 10 | 1 | 9 |
| Gudkov $\langle 5 \amalg 1\langle 5\rangle\rangle$ | 6 | 5 | 6 | 5 | 1 |
| Hilbert $\langle 1 \amalg 1\langle 9\rangle\rangle$ | 2 | 9 | 2 | 9 | $-7$ |

Checks: each row has $p + n = 11$ (Harnack, equality); $p-n \in \{9,1,-7\}$ all satisfy $-9 \le p-n \le 10$ (Petrovskii); $p \le 10$ and $n \le 9$ hold, with Harnack's curve attaining the $p$-bound and Hilbert's the $n$-bound. The Gudkov–Rokhlin congruence $p - n \equiv k^2 = 9 \equiv 1 \pmod 8$ is satisfied by all three ($9 \equiv 1$, $1 \equiv 1$, $-7 \equiv 1$) — this is what rules out the fourth candidate $\langle 5\amalg 1\langle 5\rangle\rangle$-variants with $p-n \equiv 5$.

**Why degree 10 breaks.** For $k = 5$ the same arithmetic gives Ragsdale $p \le 31$, Harnack $p+n \le 37$, Petrovskii $p-n \le 31$, hence $p \le 34$. Itenberg's construction takes a primitive convex triangulation of the Newton triangle $T_{10}$ (which has $\binom{12}{2} = 66$ lattice points and $100$ triangles of area $1/2$) built from a "staircase" of $\lfloor (k-3)^2/4 \rfloor = 1$ modified block, with signs chosen so each interior lattice point of a distinguished sub-region becomes an isolated even oval. Patchworking the four reflected copies of $T_{10}$ yields a nonsingular real decic with
$$p = 32, \qquad n = 2, \qquad p - n = 30 \le 31 .$$
Petrovskii's inequality is satisfied with room to spare; Harnack's is far from tight ($34 \le 37$); only Ragsdale's guess fails. The example shows exactly where the conjecture's reasoning broke down: bounding $p - n$ says nothing about $p$ when $n$ is small.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*