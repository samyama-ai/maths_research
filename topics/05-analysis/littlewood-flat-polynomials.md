---
id: 05-analysis/littlewood-flat-polynomials
title: "Littlewood's Flat Polynomials Problem"
topic: 05-analysis
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Littlewood's Flat Polynomials Problem

> **Topic:** Real & Complex Analysis · **ID:** `05-analysis/littlewood-flat-polynomials` · **Status:** partially-solved (existence settled 2019; quantitative/"ultraflat" form open)

## 1. Problem Statement / Conjecture

A **Littlewood polynomial** of degree $n$ is
$$P(z)=\sum_{k=0}^{n}\varepsilon_k z^k,\qquad \varepsilon_k\in\{-1,+1\}.$$
On the unit circle $\|P\|_2 = \sqrt{n+1}$, so $\sqrt{n+1}$ is the natural normalisation.

**Littlewood's problem (1966).** Do there exist absolute constants $0<\delta\le\Delta$ and, for every $n$, a Littlewood polynomial $P_n$ of degree $n$ with
$$\delta\sqrt{n+1}\ \le\ |P_n(z)|\ \le\ \Delta\sqrt{n+1}\qquad\text{for all }|z|=1\ ?$$
**Answer: yes** — Balister, Bollobás, Morris, Sahasrabudhe and Tiba (*Annals of Mathematics*, 2020).

The problem as a live open question is now its quantitative refinement.

**Erdős's flatness conjecture (1957).** There is an absolute $c>0$ such that every Littlewood polynomial of degree $n$ satisfies
$$\|P\|_\infty:=\max_{|z|=1}|P(z)|\ \ge\ (1+c)\sqrt{n+1}.$$
Equivalently: **no ultraflat sequence of Littlewood polynomials exists**, where ultraflat means $\|P_n\|_\infty/\sqrt{n+1}\to 1$. A complete resolution is either a proof of such a $c$, or an explicit construction of $\pm1$ coefficient sequences whose sup-norm ratio tends to $1$.

**Erdős's $L^4$ conjecture.** There is $c'>0$ with $\|P\|_4\ge(1+c')\|P\|_2$ for all Littlewood $P$; equivalently the *merit factor* (§2) is bounded above by an absolute constant. This is implied by no known result and implies the $L^\infty$ statement.

## 2. Mathematical Foundations

Write $z=e^{i\theta}$ and $\|P\|_q^q=\frac{1}{2\pi}\int_0^{2\pi}|P(e^{i\theta})|^q\,d\theta$.

**Autocorrelations.** For $\varepsilon=(\varepsilon_0,\dots,\varepsilon_n)\in\{\pm1\}^{n+1}$ set
$$c_k=\sum_{j=0}^{n-k}\varepsilon_j\varepsilon_{j+k},\qquad 1\le k\le n .$$
Then
$$|P(e^{i\theta})|^2=(n+1)+2\sum_{k=1}^{n}c_k\cos k\theta,$$
and by Parseval applied to $|P|^2$,
$$\|P\|_4^4=(n+1)^2+2\sum_{k=1}^{n}c_k^2 .$$
The **merit factor** is
$$F(P)=\frac{\|P\|_2^4}{\|P\|_4^4-\|P\|_2^4}=\frac{(n+1)^2}{2\sum_{k\ge1}c_k^2}.$$
So "$F$ bounded" $\iff$ "$\|P\|_4\ge(1+c')\|P\|_2$", and by $\|P\|_\infty\ge\|P\|_4$ this dominates the $L^\infty$ conjecture. Flatness in the strong Littlewood sense is the two-sided statement $\delta\le|P|/\sqrt{n+1}\le\Delta$, which is *not* an $L^q$ statement: no $L^q$ norm controls the minimum modulus.

**Unimodular relaxation.** Replace $\varepsilon_k\in\{\pm1\}$ by $|a_k|=1$, $a_k\in\mathbb{C}$. Kahane's theorem: there exist unimodular $P_n$ with
$$\bigl|\,|P_n(e^{i\theta})|-\sqrt{n+1}\,\bigr| = o\bigl(\sqrt{n+1}\bigr)\quad\text{uniformly in }\theta,$$
so ultraflat unimodular polynomials exist. The $\pm1$ constraint is therefore the entire difficulty.

**Rudin–Shapiro pairs.** Define $P_0=Q_0=1$ and
$$P_{k+1}(z)=P_k(z)+z^{2^k}Q_k(z),\qquad Q_{k+1}(z)=P_k(z)-z^{2^k}Q_k(z).$$
Then $|P_{k+1}|^2+|Q_{k+1}|^2=2(|P_k|^2+|Q_k|^2)$, giving $|P_k(z)|^2+|Q_k(z)|^2=2^{k+1}$ and hence the upper bound
$$\|P_k\|_\infty\le\sqrt{2}\,\sqrt{n+1},\qquad n+1=2^k .$$

**Discrepancy input.** The BBMST proof is combinatorial: it selects signs by an iterated *partial colouring* argument in the spirit of Spencer's "six standard deviations suffice" and Beck's entropy method, controlling all the linear functionals $\theta\mapsto\sum_k\varepsilon_k e^{ik\theta}$ simultaneously on a net of $\theta$'s.

## 3. History & State of the Art (SOTA)

- **1951/1959 — Shapiro, Rudin.** The Rudin–Shapiro polynomials give $\|P\|_\infty\le\sqrt2\,\sqrt{n+1}$: the upper half of Littlewood's problem, with $\Delta=\sqrt2$.
- **1957 — Erdős.** Poses the flatness conjecture in *Some unsolved problems*; conjectures $\|P\|_\infty\ge(1+c)\sqrt{n+1}$.
- **1966/1968 — Littlewood.** States the two-sided problem in *J. London Math. Soc.* and in *Some Problems in Real and Complex Analysis*; notes the lower bound is the hard side.
- **1980 — Kahane.** Ultraflat *unimodular* polynomials exist; refutes the Erdős conjecture in the unimodular category. Körner, following Byrnes, gives a related construction.
- **1990 — Newman & Byrnes.** For $\varepsilon$ uniform on $\{\pm1\}^{n+1}$, $\mathbb{E}\|P\|_4^4 = 2(n+1)^2-(n+1)$, so the *typical* merit factor is $\approx 1$. Random signs are not flat below.
- **1991 — Beck.** Coefficients restricted to $400$-th roots of unity admit flat polynomials, $\delta,\Delta$ absolute — the first flatness result with finitely many allowed coefficients.
- **2009 — Bombieri & Bourgain.** Sharp analysis of Kahane's construction; error term $O(n^{1/3}\log n)$ for ultraflat unimodular polynomials.
- **2019/2020 — Balister, Bollobás, Morris, Sahasrabudhe, Tiba.** *Flat Littlewood polynomials exist.* For every $n\ge2$ there is a Littlewood $P$ of degree $n$ with $\delta\sqrt{n}\le|P(z)|\le\Delta\sqrt{n}$ on $|z|=1$, with explicit (unoptimised) absolute constants. Littlewood's question is answered affirmatively.
- **Merit factor track.** Turyn's rotated Legendre-symbol sequences give asymptotic $F=6$; Jedwab, Katz and Schmidt (2013) push the record asymptotic merit factor above $6.34$. No construction beats $\approx 6.34$; no *upper* bound on $\limsup F$ is proven at all.

## 4. Partial Results / Verified Cases

- **Upper bound, all $n$:** $\Delta=\sqrt2$ for $n+1=2^k$ (Rudin–Shapiro), extended to all $n$ by truncation with $\Delta$ absolute.
- **Two-sided flatness, all $n\ge2$:** BBMST (2020), absolute $\delta,\Delta$. The published constants are far from $1$ and not claimed optimal.
- **Coefficients in $\mu_{400}$ (400-th roots of unity):** Beck (1991), flat for all degrees.
- **Unimodular coefficients:** Kahane (1980), ultraflat; Bombieri–Bourgain (2009) with error $O(n^{1/3}\log n)$ — so Erdős's conjecture is *false* one relaxation away.
- **Conjugate-reciprocal unimodular polynomials:** Erdélyi proved no such family can be ultraflat, and established the structure ("Saffari's phase conjecture") of Kahane-type ultraflat families. This is the only broad class in which an Erdős-type lower bound is known.
- **Merit factor, explicit families:** Rudin–Shapiro $F\to3$; shifted Legendre $F\to6$; Jedwab–Katz–Schmidt $F>6.34$. Exhaustive computation confirms optimal merit factors for all $n+1\lesssim 60$ and heuristic search far beyond; no example with $F>10$ is known.
- **Small $n$:** Barker sequences (all $|c_k|\le1$) exist for lengths $2,3,4,5,7,11,13$, giving the largest possible merit factors at those lengths ($F=14.08$ at length $13$). None exist for odd length $>13$; the even case is open above $10^{22}$.

## 5. Principal Obstacles

- **No lower-bound method for $|P|$.** All flatness upper bounds come from $L^2$-type identities ($|P_k|^2+|Q_k|^2$ constant), which are blind to zeros. Nothing in classical Fourier analysis forces $\pm1$ coefficient polynomials away from $0$; the Rudin–Shapiro polynomials themselves get small on the circle (Erdélyi's Mahler-measure estimates show their geometric mean is strictly below $\sqrt{n+1}$).
- **The $\pm1$ constraint destroys perturbation.** Kahane's construction tunes phases continuously (a random phase $\theta_k\approx \pi k^2/n$ plus corrections). With only two symbols there is no continuum to correct in; every fix is a discrete flip of size comparable to the error being fixed.
- **Erdős's lower-bound direction has no known mechanism.** A proof would need to exhibit an obstruction that distinguishes $\{\pm1\}$ from $\mu_{400}$ — but Beck showed $400$ symbols already suffice for flatness, so any argument must be genuinely sensitive to the alphabet size, not merely to discreteness.
- **Autocorrelation lower bounds are false individually.** One cannot bound $\sum_k c_k^2$ from below term-by-term: Barker-type sequences make every $|c_k|\le1$ for the lengths where they exist. Any proof of the $L^4$ conjecture must show that $|c_k|\le O(1)$ *for all $k$ simultaneously* is impossible for large $n$ — precisely the (also open) Barker sequence conjecture, strengthened.
- **Discrepancy machinery is one-sided.** The partial-colouring/entropy method used by BBMST controls deviations of many linear forms but produces constants that degrade multiplicatively at every round, so it cannot approach ratio $1$.

## 6. The Gap

Proven: existence of $\delta,\Delta$ with $\delta\sqrt n\le|P|\le\Delta\sqrt n$, $\delta$ small and $\Delta$ large. Conjectured: that the *upper* ratio can never be driven to $1$, i.e. $\|P\|_\infty\ge(1+c)\sqrt{n+1}$.

The gap is a change of quantifier and of direction:

1. **From "some flat $P$ exists" to "every $P$ is non-flat above."** BBMST is a construction; Erdős's conjecture is a universal lower bound over $2^{n+1}$ sequences. No technique currently converts one into the other.
2. **From $L^2$ to $L^4$.** Proving $\sum_{k\ge1}c_k^2\ge \eta\,n^2$ for all $\pm1$ sequences would settle the $L^4$ conjecture and hence the $L^\infty$ one. Current knowledge gives only the *average* $\sum c_k^2\sim n^2/2$; the infimum is bounded below by nothing better than $O(n)$-type trivialities.
3. **The alphabet barrier.** Kahane (infinite alphabet) and Beck ($400$ symbols) both give flatness; the conjecture asserts $2$ symbols do not. No proof strategy is known that is quantitatively sensitive to this.

## 7. Current Research (as of June 2026)

- **Constant optimisation in BBMST.** Cambridge/IMPA-linked groups (Sahasrabudhe, Tiba, Morris) continue to press the explicit $\delta,\Delta$ downward/upward; the announced constants remain far from $\sqrt2$ on the upper side. *(frontier — verify)*
- **Merit-factor asymptotics.** Jedwab, Katz and Schmidt's framework (appending and rotating Legendre sequences) remains the SOTA engine; work continues on whether $6.34\ldots$ is a genuine barrier or an artefact of character-sum families. *(frontier — verify)*
- **Erdélyi's programme** on ultraflat unimodular polynomials: derivative bounds, Mahler measures, and structural constraints ("the ultraflat family is essentially unique in phase"), aimed at showing $\pm1$ coefficients are incompatible with that structure.
- **Barker/circulant Hadamard interplay.** Number-theoretic exclusion of long Barker sequences (Leung–Schmidt), since Barker-like sequences are the only known candidate route to small $\sum c_k^2$.
- **Computational search.** Branch-and-bound and stochastic search for high merit factor at lengths in the hundreds; consistently fails to exceed $\approx 6.4$, supporting boundedness of $F$.

## 8. Future Work

- Prove $\sum_{k\ge1}c_k^2\ge \eta n^2$ for all $\pm1$ sequences — the $L^4$ conjecture — perhaps via an entropy/counting argument showing that near-Barker autocorrelation profiles are rare enough to be excluded.
- Determine the true infimum of $\limsup\|P_n\|_\infty/\sqrt{n+1}$ over Littlewood families: is it $\sqrt2$ (Rudin–Shapiro optimal) or strictly between $1$ and $\sqrt2$?
- Determine the minimal alphabet size admitting *ultraflat* polynomials; Beck's $400$ gives flat, Kahane's $\infty$ gives ultraflat. Locating the threshold would isolate exactly what fails at $2$.
- Make the BBMST partial-colouring argument quantitative enough to output near-optimal $\delta$, or replace it by an algebraic construction.
- Settle the even-length Barker conjecture, removing the main candidate counterexample family for the $L^4$ conjecture.

## 9. Key References

- **[Foundational]** J. E. Littlewood. *On polynomials $\sum^n \pm z^m$, $\sum^n e^{\alpha_m i}z^m$, $z=e^{\theta i}$.* Journal of the London Mathematical Society **41** (1966), 367–376.
- **[Foundational]** J. E. Littlewood. *Some Problems in Real and Complex Analysis.* D. C. Heath, Lexington MA, 1968.
- **[Foundational]** P. Erdős. *Some unsolved problems.* Michigan Mathematical Journal **4** (1957), 291–300.
- **[Foundational]** W. Rudin. *Some theorems on Fourier coefficients.* Proceedings of the American Mathematical Society **10** (1959), 855–859. [DOI](https://doi.org/10.1090/s0002-9939-1959-0116184-5)
- **[Foundational]** J.-P. Kahane. *Sur les polynômes à coefficients unimodulaires.* Bulletin of the London Mathematical Society **12** (1980), 321–342.
- **[SOTA]** P. Balister, B. Bollobás, R. Morris, J. Sahasrabudhe, M. Tiba. *Flat Littlewood polynomials exist.* Annals of Mathematics **192** (2020), 977–1004. [DOI](https://doi.org/10.4007/annals.2020.192.3.6)
- **[Key]** J. Beck. *Flat polynomials on the unit circle — note on a problem of Littlewood.* Bulletin of the London Mathematical Society **23** (1991), 269–277. [DOI](https://doi.org/10.1112/blms/23.3.269)
- **[Key]** E. Bombieri, J. Bourgain. *On Kahane's ultraflat polynomials.* Journal of the European Mathematical Society **11** (2009), 627–703. [DOI](https://doi.org/10.4171/jems/163)
- **[Key]** D. J. Newman, J. S. Byrnes. *The $L^4$ norm of a polynomial with coefficients $\pm1$.* American Mathematical Monthly **97** (1990), 42–45. [DOI](https://doi.org/10.2307/2324003)
- **[Key]** T. W. Körner. *On a polynomial of Byrnes.* Bulletin of the London Mathematical Society **12** (1980), 219–224. [DOI](https://doi.org/10.1112/blms/12.3.219)
- **[SOTA / Recent]** J. Jedwab, D. J. Katz, K.-U. Schmidt. *Advances in the merit factor problem for binary sequences.* Journal of Combinatorial Theory, Series A **120** (2013), 882–906. [DOI](https://doi.org/10.1016/j.jcta.2013.01.010)
- **[Key]** T. Erdélyi. *The phase problem of ultraflat unimodular polynomials: the resolution of the conjecture of Saffari.* Mathematische Nachrichten **248–249** (2003), 89–107.
- **[Survey]** P. Borwein. *Computational Excursions in Analysis and Number Theory.* CMS Books in Mathematics, Springer, 2002. [DOI](https://doi.org/10.1007/978-0-387-21652-2)
- **[Survey]** J. Spencer. *Six standard deviations suffice.* Transactions of the American Mathematical Society **289** (1985), 679–706. [DOI](https://doi.org/10.1090/s0002-9947-1985-0784009-0)

## 10. Worked Example / Concrete Special Case

Take $n=3$ and the Rudin–Shapiro polynomial $P_2(z)=1+z+z^2-z^3$, i.e. $\varepsilon=(1,1,1,-1)$. Here $\|P\|_2=\sqrt{4}=2$.

**Autocorrelations.**
$$c_1=\varepsilon_0\varepsilon_1+\varepsilon_1\varepsilon_2+\varepsilon_2\varepsilon_3=1+1-1=1,\quad
c_2=\varepsilon_0\varepsilon_2+\varepsilon_1\varepsilon_3=1-1=0,\quad
c_3=\varepsilon_0\varepsilon_3=-1 .$$

**Modulus on the circle.** With $c=\cos\theta$ and $\cos3\theta=4c^3-3c$,
$$|P(e^{i\theta})|^2=4+2\bigl(\cos\theta-\cos3\theta\bigr)=4+8c-8c^3 .$$
Setting the derivative $8-24c^2=0$ gives $c=\pm1/\sqrt3$:
$$\max|P|^2=4+\tfrac{16}{3\sqrt3}\approx7.0792,\qquad \min|P|^2=4-\tfrac{16}{3\sqrt3}\approx0.9208 .$$
Hence
$$\frac{\|P\|_\infty}{\sqrt{n+1}}=\frac{2.6607}{2}\approx1.330,\qquad \frac{\min_{|z|=1}|P|}{\sqrt{n+1}}=\frac{0.9596}{2}\approx0.480 .$$
Both sides of Littlewood's inequality hold with $\delta=0.48$, $\Delta=1.33$, and $\Delta\le\sqrt2$ as the Rudin–Shapiro identity predicts.

**$L^4$ norm and merit factor.**
$$\|P\|_4^4=(n+1)^2+2\sum_{k\ge1}c_k^2=16+2(1+0+1)=20,\qquad F=\frac{16}{20-16}=4 .$$
This is optimal for length $4$: $(1,1,1,-1)$ is a Barker sequence, so $|c_k|\le1$ for every $k$, minimising $\sum c_k^2$. Note $\|P\|_4=20^{1/4}\approx2.1147=1.057\,\|P\|_2$ — the $L^4$ excess Erdős conjectures to persist.

**Why this does not scale.** For $n+1=2^k$ the Rudin–Shapiro upper ratio stays $\le\sqrt2$, but its merit factor tends to $3$, i.e. $\|P\|_4/\|P\|_2\to(4/3)^{1/4}\approx1.075$: a *fixed* excess, consistent with Erdős. The obstacle is the lower side: as $k$ grows the minimum modulus of $P_k$ is no longer bounded below by a constant times $\sqrt{n+1}$ — this length-4 example's $\delta=0.48$ degrades — and recovering a uniform $\delta$ for every $n$ is exactly what required the discrepancy-theoretic construction of BBMST.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*