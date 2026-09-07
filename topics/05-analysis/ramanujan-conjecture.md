---
id: 05-analysis/ramanujan-conjecture
title: "Ramanujan Conjecture"
topic: 05-analysis
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Ramanujan Conjecture

> **Topic:** Real & Complex Analysis · **ID:** `05-analysis/ramanujan-conjecture` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

Ramanujan's original conjecture (1916) concerns the coefficients $\tau(n)$ of the discriminant modular form
$$\Delta(z) = q\prod_{n\ge 1}(1-q^n)^{24} = \sum_{n\ge 1}\tau(n)q^n, \qquad q = e^{2\pi i z},\ \ \operatorname{Im} z > 0 .$$
He conjectured $|\tau(p)| \le 2p^{11/2}$ for every prime $p$, equivalently $|\tau(n)| \le d(n)\,n^{11/2}$ for all $n$, where $d(n)$ is the number of divisors. This was proved by **Deligne (1974)** as a consequence of the Weil conjectures. Petersson's extension — that a normalized Hecke eigenform of weight $k$ on a congruence subgroup has $|a_f(p)| \le 2p^{(k-1)/2}$ — follows by the same argument for $k \ge 2$, and for $k=1$ from Deligne–Serre.

What remains **open** is the *generalized Ramanujan–Petersson conjecture* (GRC):

> Let $F$ be a number field, $\pi = \otimes_v \pi_v$ a cuspidal automorphic representation of $\mathrm{GL}_n(\mathbb{A}_F)$ with unitary central character. Then every local component $\pi_v$ is **tempered**: its matrix coefficients lie in $L^{2+\varepsilon}(\mathrm{GL}_n(F_v)/Z)$ for all $\varepsilon>0$.

A complete proof must handle all $n$, all number fields, all places (archimedean and ramified non-archimedean), and all cusp forms — including non-cohomological ones such as Maass forms, which carry no known motive. A disproof requires a single cuspidal $\pi$ on $\mathrm{GL}_n$ with a non-tempered local component. For groups other than $\mathrm{GL}_n$ the naive conjecture is **false** (Howe–Piatetski-Shapiro, 1979).

## 2. Mathematical Foundations

**Modular setting.** $\Delta \in S_{12}(\mathrm{SL}_2(\mathbb{Z}))$ is the unique normalized cusp form of weight $12$ and level $1$. It is an eigenfunction of all Hecke operators $T_p$, so $\tau$ is multiplicative and
$$\sum_{n\ge1}\frac{\tau(n)}{n^{s}} = \prod_p \left(1 - \tau(p)p^{-s} + p^{11-2s}\right)^{-1}.$$
Write $1 - \tau(p)X + p^{11}X^2 = (1-\alpha_p X)(1-\beta_p X)$ with $\alpha_p\beta_p = p^{11}$. Ramanujan's bound is exactly
$$|\alpha_p| = |\beta_p| = p^{11/2},$$
i.e. the two Satake parameters have equal absolute value; equivalently $\tau(p) = 2p^{11/2}\cos\theta_p$ for a real angle $\theta_p \in [0,\pi]$.

**Analytic normalization.** For $a_f(n)$ the coefficients of a weight-$k$ eigenform, set $\lambda_f(n) = a_f(n)n^{-(k-1)/2}$. Ramanujan–Petersson says $|\lambda_f(p)| \le 2$.

**Automorphic setting.** For $\pi$ on $\mathrm{GL}_n(\mathbb{A}_F)$ unramified at $v$, the Satake parameter is a semisimple conjugacy class $\mathrm{diag}(\alpha_{1,v},\dots,\alpha_{n,v}) \in \mathrm{GL}_n(\mathbb{C})$ with
$$L(s,\pi_v) = \prod_{i=1}^n \left(1 - \alpha_{i,v} q_v^{-s}\right)^{-1}.$$
GRC at $v$ asserts $|\alpha_{i,v}| = 1$ for all $i$. Define the exponent
$$\theta_n = \inf\{\theta : |\alpha_{i,v}| \le q_v^{\theta}\ \text{for all such }\pi,v,i\}.$$
GRC is $\theta_n = 0$; the trivial bound from unitarity plus non-existence of poles is $\theta_n < 1/2$.

**Archimedean form.** For a Maass cusp form $u$ on $\mathrm{SL}_2(\mathbb{Z})\backslash\mathbb{H}$ with $\Delta u = \lambda u$, $\lambda = \tfrac14 + r^2$, temperedness at $\infty$ means $r \in \mathbb{R}$, i.e. $\lambda \ge 1/4$. For congruence subgroups $\Gamma_0(N)$ this is **Selberg's eigenvalue conjecture** $\lambda_1 \ge 1/4$.

**Geometric input.** Deligne's proof rests on: (i) Eichler–Shimura/Deligne's construction of $\ell$-adic Galois representations $\rho_{f,\ell}: \mathrm{Gal}(\overline{\mathbb{Q}}/\mathbb{Q}) \to \mathrm{GL}_2(\overline{\mathbb{Q}}_\ell)$ with $\operatorname{tr}\rho_{f,\ell}(\mathrm{Frob}_p) = a_f(p)$, realized in $H^{k-1}_{\text{ét}}$ of the Kuga–Sato variety; (ii) the Riemann hypothesis over finite fields (Weil I): eigenvalues of $\mathrm{Frob}_q$ on $H^i$ of a smooth projective variety over $\mathbb{F}_q$ have absolute value $q^{i/2}$.

## 3. History & State of the Art (SOTA)

- **1916** — Ramanujan, *On certain arithmetical functions*, states multiplicativity and the bound $|\tau(p)| \le 2p^{11/2}$ on numerical evidence.
- **1917** — Mordell proves multiplicativity of $\tau$ using Hecke-type operators avant la lettre.
- **1930s–40s** — Successive analytic bounds on $\tau(n) \ll n^{c}$: Hardy–Littlewood/Kloosterman $c = 47/8$, Salié and Davenport $c = 35/6$, Rankin (1939) $c = 29/5$ via the Rankin–Selberg method. All fall short of $11/2 = 5.5$.
- **1939** — Petersson formulates the general conjecture for weight-$k$ eigenforms.
- **1968–69** — Deligne (Bourbaki 355) shows Ramanujan's conjecture *follows from* the Weil conjectures.
- **1974** — Deligne proves Weil I; the Ramanujan–Petersson conjecture for $k\ge 2$ is a corollary.
- **1974** — Deligne–Serre handle weight $1$ (Artin representations, finite image).
- **1979** — Howe–Piatetski-Shapiro construct cuspidal non-tempered representations of split $\mathrm{Sp}_4$ and $\mathrm{U}(2,2)$: the naive GRC fails outside $\mathrm{GL}_n$.
- **1995** — Luo–Rudnick–Sarnak: $\theta_2 \le 5/28$ for $\mathrm{GL}_2/\mathbb{Q}$ and $\theta_n \le \tfrac12 - \tfrac{1}{n^2+1}$.
- **2002** — L. Lafforgue proves the global Langlands correspondence for $\mathrm{GL}_n$ over **function fields**, giving GRC there in full.
- **2003** — Kim–Sarnak: $\theta_2 \le 7/64$ over $\mathbb{Q}$, i.e. $\lambda_1 \ge \tfrac14 - \left(\tfrac{7}{64}\right)^2 = \tfrac{975}{4096} \approx 0.238$.
- **2011** — Blomer–Brumley extend $7/64$ and $\tfrac12 - \tfrac{1}{n^2+1}$ to arbitrary number fields.

## 4. Partial Results / Verified Cases

| Class | Status |
|---|---|
| Holomorphic eigenforms, $S_k(\Gamma_0(N),\chi)$, $k\ge2$ | **Proved** (Deligne 1974) |
| Weight $k=1$ | **Proved** (Deligne–Serre 1974) |
| Hilbert modular forms of regular weight over totally real $F$ | **Proved** (Brylinski–Labesse; Blasius 2006) |
| Self-dual regular algebraic cuspidal $\pi$ on $\mathrm{GL}_n$ over CM/totally real fields | **Proved** at unramified places (Harris–Taylor 2001; Clozel–Harris–Taylor), and at *all* finite places (Shin 2011; Caraiani 2012) |
| Regular algebraic cuspidal $\pi$ on $\mathrm{GL}_n$ over CM fields, general (non-self-dual) | Proved for $\ell$-adic-cohomological cases via Harris–Lan–Taylor–Thorne / Scholze constructions at good places |
| $\mathrm{GL}_n$ over a **function field** $\mathbb{F}_q(X)$, all $n$ | **Proved** (L. Lafforgue 2002) |
| $\mathrm{GL}_2/\mathbb{Q}$ Maass forms | Open; $\theta_2 \le 7/64$ (Kim–Sarnak 2003) |
| $\mathrm{GL}_n$, general number field | Open; $\theta_n \le \tfrac12 - \tfrac{1}{n^2+1}$ (Blomer–Brumley 2011) |
| Average/density versions | Proved: Sarnak–Xue-type density estimates show exceptional eigenvalues are sparse |

Numerically, $\lambda_1$ for $\mathrm{SL}_2(\mathbb{Z})$ is $\approx 91.14$ (Hejhal, Booker–Strömbergsson–Venkatesh verified rigorously), far above $1/4$; no counterexample to GRC on $\mathrm{GL}_n$ is known at any level of computation.

## 5. Principal Obstacles

- **No motive for Maass forms.** Deligne's argument needs $\pi$ to appear in the étale cohomology of an algebraic variety. Maass forms with $\lambda = \tfrac14+r^2$, $r$ irrational, are not known to be motivic; their Hecke eigenvalues are transcendental-looking real numbers with no Frobenius interpretation. The Weil-conjecture machinery has no entry point.
- **Non-cohomological automorphic forms.** For $\mathrm{GL}_n/F$ with $F$ having a complex place, or with non-regular infinitesimal character, the relevant $(\mathfrak{g},K)$-cohomology vanishes and Shimura-variety methods produce no Galois representation.
- **Analytic methods stall at $1/2$.** Rankin–Selberg, the Kuznetsov formula and functoriality (symmetric powers) give bounds of the shape $\theta \le \tfrac12 - \delta$ with $\delta$ decreasing in $n$; each new symmetric power gains a fixed increment and infinitely many would be needed. Kim–Sarnak's $7/64$ uses $\mathrm{Sym}^4$ functoriality — the highest currently available for $\mathrm{GL}_2$ in the needed generality.
- **Ramified and archimedean places.** Even in cohomological cases, purity at bad primes required the full weight-monodromy analysis (Caraiani 2012); analogous control is unavailable when no geometry is present.
- **The conjecture is false in general.** Since Howe–Piatetski-Shapiro, any proof strategy must use something specific to $\mathrm{GL}_n$ (multiplicity one, no endoscopy), ruling out purely representation-theoretic or trace-formula arguments that treat all reductive groups alike.

## 6. The Gap

Proven: temperedness for automorphic representations that are **motivic** — regular algebraic and cohomological, hence attached to $\ell$-adic Galois representations whose Frobenius eigenvalues are pure by Weil I / weight-monodromy — plus the entire function-field case where Lafforgue's shtuka moduli supply the geometry.

Open: everything **non-motivic**. The precise barrier is:

> Given a cuspidal $\pi$ on $\mathrm{GL}_n(\mathbb{A}_F)$ with *no* known geometric realization (e.g. a Maass form of eigenvalue $\tfrac14+r^2$), produce an object whose $p$-adic or $\ell$-adic weight structure forces $|\alpha_{i,p}| = 1$.

Equivalently, close the numeric gap from $\theta_2 \le 7/64 \approx 0.109$ to $\theta_2 = 0$, and from $\theta_n \le \tfrac12-\tfrac1{n^2+1}$ to $\theta_n = 0$ — a gap that no finite amount of known functoriality can bridge.

## 7. Current Research (as of June 2026)

- **Functoriality via the trace formula.** Arthur's stabilized trace formula and the Langlands "Beyond Endoscopy" programme (Frenkel–Langlands–Ngô; Altuğ; Sarnak's school at IAS/Princeton) aim to construct $\mathrm{Sym}^m$ lifts for all $m$, which would give $\theta_2 = 0$ for $\mathrm{GL}_2$. Progress remains at low $m$. *(frontier — verify)*
- **$p$-adic and torsion cohomology.** Scholze's perfectoid/locally symmetric space methods and their refinements (Caraiani–Scholze on Shimura varieties, Newton–Thorne on symmetric power functoriality for holomorphic forms) extend Galois-representation constructions to torsion classes; extending them to *non-torsion, non-cohomological* Maass classes is the target. *(frontier — verify)*
- **Density theorems as substitutes.** Sarnak–Xue, Blomer–Buttcane and follow-ups prove GRC "on average", enough for many applications (sieve, sup-norms, quantum chaos, Ramanujan graphs); active work sharpens exponents in $\mathrm{GL}_n$ density hypotheses (Blomer, Brumley, Assing–Blomer, Jana).
- **Explicit bounds over number fields.** Continued refinement of $\theta_n$ for $\mathrm{GL}_3,\mathrm{GL}_4$ using Rankin–Selberg and Kuznetsov-type formulas.
- **Applications-driven checks.** Ramanujan graphs (Lubotzky–Phillips–Sarnak) and optimal lifting/golden-gate constructions in quantum computing consume the proved $\mathrm{GL}_2$ holomorphic case directly.

## 8. Future Work

- Prove $\mathrm{Sym}^m$ functoriality for $\mathrm{GL}_2$ for all $m\ge 1$ over number fields; this yields $\theta_2 = 0$ by Langlands' argument that all $L(s,\mathrm{Sym}^m\pi)$ being automorphic forces $|\lambda_\pi(p)|\le 2$.
- Attach $\ell$-adic (or $p$-adic analytic) objects to Maass forms with $r \notin \tfrac{i}{2}\mathbb{Z}$ — Sarnak's stated "hardest open problem" in the circle.
- Formulate and prove the correct **Arthur-parameter** version of GRC for general reductive $G$, which predicts exactly which non-tempered representations occur (CAP forms), converting the Howe–Piatetski-Shapiro counterexamples into a theorem.
- Push weight-monodromy/purity arguments to non-regular weights and to $\mathrm{GL}_n$ over fields with complex places.
- Improve $\theta_n$ below $\tfrac12 - \tfrac{c}{n}$ for large $n$; currently the bound degrades like $n^{-2}$.

## 9. Key References

- **[Foundational]** S. Ramanujan. *On certain arithmetical functions.* Transactions of the Cambridge Philosophical Society, 22 (1916), 159–184.
- **[Foundational]** L. J. Mordell. *On Mr. Ramanujan's empirical expansions of modular functions.* Proceedings of the Cambridge Philosophical Society, 19 (1917), 117–124.
- **[Foundational]** P. Deligne. *Formes modulaires et représentations $\ell$-adiques.* Séminaire Bourbaki, exp. 355, Lecture Notes in Mathematics 179, Springer, 1971.
- **[Foundational]** P. Deligne. *La conjecture de Weil. I.* Publications Mathématiques de l'IHÉS, 43 (1974), 273–307.
- **[Foundational]** P. Deligne, J.-P. Serre. *Formes modulaires de poids 1.* Annales scientifiques de l'ÉNS, 7 (1974), 507–530.
- **[Counterexample]** R. Howe, I. Piatetski-Shapiro. *A counterexample to the "generalized Ramanujan conjecture" for (quasi-)split groups.* Proceedings of Symposia in Pure Mathematics 33, AMS, 1979, 315–322.
- **[SOTA]** W. Luo, Z. Rudnick, P. Sarnak. *On Selberg's eigenvalue conjecture.* Geometric and Functional Analysis, 5 (1995), 387–401.
- **[SOTA]** H. Kim (with appendices by D. Ramakrishnan and by H. Kim and P. Sarnak). *Functoriality for the exterior square of $\mathrm{GL}_4$ and the symmetric fourth of $\mathrm{GL}_2$.* Journal of the AMS, 16 (2003), 139–183.
- **[SOTA]** L. Lafforgue. *Chtoucas de Drinfeld et correspondance de Langlands.* Inventiones Mathematicae, 147 (2002), 1–241.
- **[SOTA]** V. Blomer, F. Brumley. *On the Ramanujan conjecture over number fields.* Annals of Mathematics, 174 (2011), 581–605.
- **[SOTA]** S. W. Shin. *Galois representations arising from some compact Shimura varieties.* Annals of Mathematics, 173 (2011), 1645–1741.
- **[SOTA]** A. Caraiani. *Local-global compatibility and the action of monodromy on nearby cycles.* Duke Mathematical Journal, 161 (2012), 2311–2413.
- **[Survey]** P. Sarnak. *Notes on the generalized Ramanujan conjectures.* In *Harmonic Analysis, the Trace Formula, and Shimura Varieties*, Clay Mathematics Proceedings 4, AMS, 2005, 659–685.
- **[Survey]** V. Blomer, F. Brumley. *The role of the Ramanujan conjecture in analytic number theory.* Bulletin of the AMS, 50 (2013), 267–320.
- **[Book]** H. Iwaniec. *Spectral Methods of Automorphic Forms.* 2nd ed., Graduate Studies in Mathematics 53, AMS, 2002.

## 10. Worked Example / Concrete Special Case

**Checking Ramanujan's bound for $\Delta$ at small primes.**

Expanding $q\prod(1-q^n)^{24}$ gives
$$\tau(2) = -24,\quad \tau(3) = 252,\quad \tau(5) = 4830,\quad \tau(7) = -16744,\quad \tau(11) = 534612 .$$
The predicted bound is $2p^{11/2}$:

| $p$ | $\tau(p)$ | $2p^{11/2}$ | $\lambda(p) = \tau(p)p^{-11/2}$ | $\theta_p = \arccos(\lambda(p)/2)$ |
|---|---|---|---|---|
| 2 | $-24$ | $90.51$ | $-0.5303$ | $1.8355$ |
| 3 | $252$ | $840.7$ | $0.5995$ | $1.2660$ |
| 5 | $4830$ | $6987.7$ | $1.3825$ | $0.8027$ |
| 7 | $-16744$ | $18990.5$ | $-1.7635$ | $2.6607$ |
| 11 | $534612$ | $88\,478\,\!\cdot\!... $ ($\approx 8.85\times10^5$) | $1.2085$ | $0.9051$ |

Every $|\lambda(p)| \le 2$, as Deligne's theorem guarantees.

**Verifying the Satake structure at $p=2$.** The Hecke polynomial is
$$1 + 24X + 2^{11}X^2 = 1 + 24X + 2048X^2 .$$
Its roots satisfy $\alpha_2 + \beta_2 = -24$, $\alpha_2\beta_2 = 2048$. The discriminant is $24^2 - 4\cdot 2048 = 576 - 8192 = -7616 < 0$, so the roots are complex conjugates:
$$\alpha_2, \beta_2 = -12 \pm i\sqrt{2048-144} = -12 \pm i\,\sqrt{1904},$$
giving $|\alpha_2|^2 = 144 + 1904 = 2048 = 2^{11}$, i.e. $|\alpha_2| = 2^{11/2}$ exactly. **Negative discriminant $\iff$ Ramanujan's bound holds at $p$**; a violation would force real roots of unequal modulus, one exceeding $p^{11/2}$.

**Contrast: the open case.** For the first Maass cusp form on $\mathrm{SL}_2(\mathbb{Z})$, $\lambda_1 \approx 91.14$ so $r_1 \approx 9.5335$; its Hecke eigenvalues satisfy $\lambda(2) \approx 1.549$, again inside $[-2,2]$. But no proof covers it: the Hecke polynomial $1 - \lambda(p)X + X^2$ has no known Frobenius interpretation, and the only unconditional guarantee is $|\lambda(p)| \le p^{7/64} + p^{-7/64}$ — at $p=2$ that is $\approx 2.011$, weaker than $2$. That $0.011$ is, in miniature, the entire remaining gap.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*