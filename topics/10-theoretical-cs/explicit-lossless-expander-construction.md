---
id: 10-theoretical-cs/explicit-lossless-expander-construction
title: "Explicit Constructions of Optimal Lossless Expanders"
topic: 10-theoretical-cs
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Explicit Constructions of Optimal Lossless Expanders

> **Topic:** Theoretical Computer Science · **ID:** `10-theoretical-cs/explicit-lossless-expander-construction` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

A bipartite graph with left vertex set $[N]$, right vertex set $[M]$, and left-degree $D$ is a **$(K,(1-\epsilon)D)$-lossless expander** if every left set $S$ with $|S| \le K$ satisfies
$$|\Gamma(S)| \ge (1-\epsilon)\,D\,|S|,$$
where $\Gamma(S)$ is the neighbourhood of $S$. "Lossless" means the expansion factor is within $(1-\epsilon)$ of the trivial maximum $D|S|$.

The probabilistic method gives such graphs with
$$D = O\!\left(\frac{\log(N/K)}{\epsilon}\right), \qquad M = O\!\left(\frac{KD}{\epsilon}\right),$$
and both are optimal up to constants (Radhakrishnan–Ta-Shma).

**The problem.** Give a *fully explicit* construction — a deterministic algorithm computing the $i$-th neighbour of a left vertex in time $\mathrm{poly}(\log N, \log M)$ — matching those parameters simultaneously, for all $N$, all $K \le N$, and all $\epsilon > 0$.

Two headline special cases remain open:

1. **Optimal unbalanced regime.** Achieve $D = O(\log(N/K)/\epsilon)$ *and* $M = O(KD/\epsilon)$. Known explicit constructions pay $D = \mathrm{poly}(\log N, 1/\epsilon)$ with exponent $>1$, or $M = K^{1+\alpha}\mathrm{poly}$.
2. **Constant-degree, arbitrarily small $\epsilon$.** For $D = O(1)$ and $M = \Theta(N)$, obtain expansion $(1-\epsilon)D$ for every constant $\epsilon > 0$, with $K = \Omega(\epsilon M/D)$ — and, in the non-bipartite setting, for *unbalanced-free* $d$-regular graphs.

A complete resolution is an explicit family attaining the random bound up to constant factors; a disproof would be an explicitness barrier (e.g. showing a natural class of algebraic constructions cannot do it).

## 2. Mathematical Foundations

**Neighbourhood and unique neighbours.** For $S \subseteq [N]$, $\Gamma(S) = \bigcup_{v\in S}\Gamma(v)$. A right vertex $u$ is a *unique neighbour* of $S$ if $|\Gamma(u)\cap S| = 1$. Counting edges,
$$|\Gamma(S)| \ge (1-\epsilon)D|S| \;\Longrightarrow\; \\#\{\text{unique nbrs of } S\} \ge (1-2\epsilon)D|S|,$$
since the $\epsilon D|S|$ "lost" edges can destroy at most that many unique neighbours. Lossless expansion with $\epsilon < 1/2$ therefore implies a *linear* number of unique neighbours — the property that drives Sipser–Spielman expander codes and their linear-time decoders.

**Spectral vs. vertex expansion.** For a $d$-regular graph $G$ with adjacency eigenvalues $d = \lambda_1 \ge \dots \ge \lambda_n$ and $\lambda = \max(|\lambda_2|,|\lambda_n|)$, the expander mixing lemma gives, for $|S| = \alpha n$,
$$\frac{|\Gamma(S)|}{|S|} \;\ge\; \frac{d^2}{\lambda^2 + \alpha(d^2-\lambda^2)} \xrightarrow[\alpha \to 0]{} \frac{d^2}{\lambda^2}.$$
Even for Ramanujan graphs ($\lambda = 2\sqrt{d-1}$) this yields only $d/4$, and Kahale (1995) sharpened the spectral consequence to $d/2$ while showing $d/2$ is *tight* for some Ramanujan families. So no eigenvalue bound can certify expansion beyond $d/2$, let alone $(1-\epsilon)d$.

**Condenser formulation.** Identify the graph with $\Gamma : [N] \times [D] \to [M]$. It is lossless iff $\Gamma$ is a **lossless condenser**: for every distribution $X$ on $[N]$ with min-entropy $H_\infty(X) \ge \log K$, and $U_D$ uniform on $[D]$,
$$\big(\Gamma(X,U_D)\big) \text{ is } \epsilon'\text{-close to a distribution of min-entropy } \log K + \log D .$$
Entropy is preserved rather than extracted; the entropy *loss* $\log(KD) - H_\infty$ is $O(\log(1/\epsilon))$. This is the lens of Ta-Shma–Umans–Zuckerman (2007) and Guruswami–Umans–Vadhan (2009).

**Algebraic engine.** GUV build $\Gamma$ from Parvaresh–Vardy codes: over $\mathbb{F}_q$ with an irreducible $E(Y)$ of degree $n$, a message $f \in \mathbb{F}_q[Y]/E$ is mapped to
$$\Gamma(f, x) = \big(x,\; f(x),\; f^{h}(x) \bmod E, \dots, f^{h^{m-1}}(x)\big),$$
and expansion follows from the list-decodability of the code (list size $\le h^m$).

## 3. History & State of the Art (SOTA)

- **1988–1996.** Expanders enter coding and derandomization; Sipser–Spielman (1996) show vertex expansion $>3d/4$ gives linear-time decodable codes, making *lossless* expansion the target rather than a curiosity.
- **1995.** Kahale proves the $d/2$ spectral barrier — the structural reason lossless expansion is hard to certify.
- **2000.** Radhakrishnan–Ta-Shma give the matching lower bounds $D = \Omega(\log(N/K)/\epsilon)$ and $M = \Omega(KD/\epsilon)$ for dispersers/extractors, fixing the optimum.
- **2002.** Capalbo–Reingold–Vadhan–Wigderson (STOC 2002) give the first explicit **constant-degree** lossless expanders, via "randomness conductors" and a zig-zag-style composition. Parameters: constant $D = D(\epsilon)$, $M = \Omega(N)$, expansion $(1-\epsilon)D$ for $|S| \le \Omega(M/D)$.
- **2002.** Alon–Capalbo give explicit unique-neighbour expanders by combinatorial means.
- **2007/2009.** Ta-Shma–Umans–Zuckerman, then GUV, give the best **unbalanced** constructions: for any $\alpha>0$,
  $$D = O\!\left(\left(\tfrac{\log N \cdot \log K}{\epsilon}\right)^{1+1/\alpha}\right), \qquad M \le D^2 \cdot K^{1+\alpha}.$$
- **2024.** Golowich (SODA 2024) gives a *new* explicit constant-degree lossless expander family, the first fundamentally different route since CRVW.
- **2024–2025.** Hsieh–McKenzie–Mohanty–Paredes (STOC 2024) construct explicit two-sided unique-neighbour expanders; Hsieh–Lin–Mohanty–O'Donnell–Zhang (STOC 2025) announce explicit *lossless vertex expanders* in the non-bipartite $d$-regular setting *(frontier — verify)*.

## 4. Partial Results / Verified Cases

| Regime | Parameters achieved | Source |
|---|---|---|
| Constant degree, balanced $M=\Omega(N)$ | $(1-\epsilon)D$ for $|S|\le \Omega(\epsilon M/D)$, $D = D(\epsilon) = \mathrm{poly}(1/\epsilon)$ tower-free but large | CRVW 2002 |
| Constant degree, alternative construction | comparable, new proof route, smaller/cleaner degree dependence | Golowich 2024 |
| Highly unbalanced, $K = N^{\Omega(1)}$ | $D = \mathrm{poly}(\log N/\epsilon)$, $M = K^{1+\alpha}\mathrm{poly}(D)$; e.g. $\alpha=1$ gives $D = O((\log N \log K/\epsilon)^2)$ | GUV 2009 |
| $K \le \mathrm{poly}\log N$ | $M = O(K D /\epsilon)$ attainable, since $K^{\alpha}$ overhead is negligible | GUV 2009 |
| Reed–Solomon direct construction | $N = q^k$, $D = q$, $M = q^2$, lossless for $K \le \epsilon q/(k-1)$ | folklore; §10 |
| Spectral certificates | expansion $\ge d/2$ for Ramanujan graphs; $d/2$ tight | Kahale 1995 |
| Non-bipartite $d$-regular vertex expansion $(1-\epsilon)d$ | claimed explicit for $|S|\le \delta(\epsilon) n$ | HLMOZ 2025 *(frontier — verify)* |

Randomized/Monte-Carlo constructions meeting the optimum are routine; the whole difficulty is explicitness.

## 5. Principal Obstacles

- **Spectral methods are provably insufficient.** Kahale's theorem caps eigenvalue-derived vertex expansion at $d/2$, i.e. $\epsilon = 1/2$. Every technique that certifies expansion through $\lambda_2$ — Alon–Boppana-optimal graphs, Cayley graphs of quasirandom groups, Ramanujan lifts — is blocked short of the goal by a factor $2$ in the lossy direction. Lossless expansion is not a spectral property.
- **No local certificate.** Lossless expansion is a statement about *all* $\binom{N}{\le K}$ small sets, and unlike $\lambda_2$ it admits no known polynomial-size witness. There is no analogue of "compute the second eigenvalue" for verifying a candidate.
- **Composition loses constants.** Zig-zag/conductor recursions multiply error terms; keeping the loss at $(1-\epsilon)$ across $\Theta(\log^* N)$ or $\Theta(\log N)$ levels forces the base object's error to shrink, blowing up the degree. CRVW succeed only because their conductors compose with additive entropy loss, and the surviving degree $D(\epsilon)$ is far from $O(1/\epsilon)$.
- **List-decoding barrier in the algebraic route.** GUV's expansion factor is $1 - (\text{list size})/(\text{something})$; the Parvaresh–Vardy list bound $h^m$ forces $M \ge K^{1+\alpha}$ with $\alpha \approx 1/m$ and $D$ growing like $D^{1+1/\alpha}$. Reducing $\alpha \to 0$ (optimal $M$) blows up $D$ polynomially; the trade-off is intrinsic to current list-decoding parameters, not an artifact.
- **High-dimensional expanders give the wrong regime.** HDX-based codes and expanders control *spectral* and *coboundary* quantities, which again saturate before losslessness.

## 6. The Gap

Write the two known frontiers against the optimum:

$$\text{Optimum: } D = \Theta\!\left(\tfrac{\log(N/K)}{\epsilon}\right),\; M = \Theta\!\left(\tfrac{KD}{\epsilon}\right).$$

- GUV: $M = K^{1+\alpha}\cdot \mathrm{poly}$ — a **polynomial** overhead $K^{\alpha}$ in the right-hand side, with degree exponent $1+1/\alpha$ blowing up as $\alpha \to 0$. The gap is the entire *joint* optimization: no construction is simultaneously within $\mathrm{polylog}$ of both bounds.
- CRVW/Golowich: degree $D(\epsilon)$ is a large polynomial (or worse) in $1/\epsilon$ rather than $O(1/\epsilon)$, and $K$ is $\Omega(M/D)$ only up to unspecified constants.

The precise missing step: a *composition or algebraic mechanism whose expansion loss is additive in $\epsilon$ rather than multiplicative across levels*, or a list-decodable code family with list size $O(1/\epsilon)$ at rate matching the optimal condenser output length. Equivalently: derandomize the union bound over $\binom{N}{K}$ sets using $O(\log(N/K)/\epsilon)$ bits of "seed" per vertex.

## 7. Current Research (as of June 2026)

- **New combinatorial routes.** Golowich's SODA 2024 construction is being extended toward smaller $\epsilon$-dependence and to the two-sided setting; groups at MIT, Berkeley/Simons, and CMU are active *(frontier — verify)*.
- **Lossless vertex expanders in the regular setting.** Hsieh–Lin–Mohanty–O'Donnell–Zhang (2025) report explicit $d$-regular graphs with vertex expansion $(1-\epsilon)d$ on small sets, using free-group/tensoring constructions with non-spectral analysis; this is the first credible circumvention of the Kahale barrier for explicit families *(frontier — verify)*.
- **Quantum LDPC feedback.** Good qLDPC codes (Panteleev–Kalachev, Dinur–Evra–Livne–Lubotzky–Mohanty) have imported product/HDX tools; researchers are testing whether the same products yield losslessness.
- **Condenser side.** Improved seeded condensers with entropy loss $O(\log(1/\epsilon))$ and near-optimal output length remain the cleanest formulation of the open problem in the pseudorandomness community (Vadhan's monograph, Open Problem list).

## 8. Future Work

- Design a code family whose list-decoding radius/list-size trade-off is *lossless-optimal*, then push it through the GUV condenser framework to remove the $K^{\alpha}$ overhead.
- Prove or refute a barrier: is there a class of "algebraic degree-$d$" constructions that provably cannot be lossless with optimal $M$?
- Find a polynomial-time *certifier* for $(1-\epsilon)D$ expansion on sets of size $\le K$ (even for $K = N^{o(1)}$); a sum-of-squares certificate would immediately enable search-based explicit constructions.
- Extend two-sided unique-neighbour results to full two-sided losslessness, which is what unique-decoding of expander codes at optimal rate needs.
- Reduce the constant-degree $D(\epsilon)$ toward the information-theoretic $\Theta(1/\epsilon)$.

## 9. Key References

- **[Foundational]** M. Capalbo, O. Reingold, S. Vadhan, A. Wigderson. *Randomness Conductors and Constant-Degree Lossless Expanders.* STOC 2002, pp. 659–668.
- **[Foundational]** N. Kahale. *Eigenvalues and Expansion of Regular Graphs.* Journal of the ACM 42(5):1091–1106, 1995.
- **[Foundational]** M. Sipser, D. Spielman. *Expander Codes.* IEEE Transactions on Information Theory 42(6):1710–1722, 1996.
- **[Foundational]** J. Radhakrishnan, A. Ta-Shma. *Bounds for Dispersers, Extractors, and Depth-Two Superconcentrators.* SIAM Journal on Discrete Mathematics 13(1):2–24, 2000.
- **[SOTA]** V. Guruswami, C. Umans, S. Vadhan. *Unbalanced Expanders and Randomness Extractors from Parvaresh–Vardy Codes.* Journal of the ACM 56(4):20, 2009.
- **[SOTA]** A. Ta-Shma, C. Umans, D. Zuckerman. *Lossless Condensers, Unbalanced Expanders, and Extractors.* Combinatorica 27(2):213–240, 2007.
- **[SOTA / Recent]** L. Golowich. *New Explicit Constant-Degree Lossless Expanders.* SODA 2024.
- **[SOTA / Recent]** J.-T. Hsieh, T. McKenzie, S. Mohanty, P. Paredes. *Explicit Two-Sided Unique-Neighbor Expanders.* STOC 2024.
- **[Recent]** N. Alon, M. Capalbo. *Explicit Unique-Neighbor Expanders.* FOCS 2002.
- **[Survey]** S. Hoory, N. Linial, A. Wigderson. *Expander Graphs and Their Applications.* Bulletin of the AMS 43(4):439–561, 2006.
- **[Survey]** S. Vadhan. *Pseudorandomness.* Foundations and Trends in Theoretical Computer Science, 2012.
- **[Context]** O. Reingold, S. Vadhan, A. Wigderson. *Entropy Waves, the Zig-Zag Graph Product, and New Constant-Degree Expanders.* Annals of Mathematics 155(1):157–187, 2002.

## 10. Worked Example / Concrete Special Case

**The Reed–Solomon expander.** Fix a prime power $q$ and $k \ge 2$. Left vertices are polynomials $f \in \mathbb{F}_q[X]$ of degree $< k$, so $N = q^k$. Right vertices are $\mathbb{F}_q^2$, so $M = q^2$. Degree $D = q$, with
$$\Gamma(f, x) = (x, f(x)), \qquad x \in \mathbb{F}_q .$$

**Claim.** This is a $(K, (1-\epsilon)q)$-expander for $K = \lceil \epsilon q/(k-1)\rceil$.

*Proof.* Suppose $S$ with $|S| = s \le K$ has $T = \Gamma(S)$ of size $|T| < (1-\epsilon)qs$. Set $d_Y = s-1$ and $d_X = \lfloor |T|/s \rfloor$. The space of polynomials $Q(X,Y)$ with $\deg_X \le d_X$, $\deg_Y \le d_Y$ has dimension $(d_X+1)(d_Y+1) = (d_X+1)s > |T|$, so a nonzero $Q$ vanishing on all of $T$ exists.

For each $f \in S$, the univariate $Q(X,f(X))$ vanishes at all $q$ points $x \in \mathbb{F}_q$ and has degree at most
$$d_X + d_Y (k-1) \le \frac{(1-\epsilon)qs}{s} + (s-1)(k-1) = (1-\epsilon)q + (s-1)(k-1).$$
Since $s \le \epsilon q/(k-1)$, this is $\le (1-\epsilon)q + \epsilon q = q$, and in fact $< q$ when the inequality on $s$ is strict, so $Q(X,f(X)) \equiv 0$, hence $(Y - f(X)) \mid Q$. That holds for all $s$ distinct $f \in S$, forcing $\deg_Y Q \ge s > d_Y$ — a contradiction. $\square$

**Numbers.** Take $q = 101$, $k = 3$, $\epsilon = 0.1$. Then
$$N = 101^3 = 1{,}030{,}301,\quad D = 101,\quad M = 10{,}201,\quad K = \lceil 0.1\cdot 101/2\rceil = 6 .$$
So every set of $\le 6$ polynomials has $\ge 0.9 \cdot 101 \cdot |S|$ distinct neighbours.

**Where it falls short.** The optimum for $N \approx 10^6$, $K = 6$, $\epsilon = 0.1$ is $D = O(\log(N/K)/\epsilon) \approx 10 \cdot 17 = 170$ — comparable — but $M = O(KD/\epsilon) \approx 6\cdot 101/0.1 \approx 6{,}060$ against the achieved $10{,}201$: only a factor $1.7$ here. The failure appears when $K$ grows: this construction caps $K$ at $\epsilon q/(k-1) = \epsilon D/(k-1)$, whereas the random bound allows $K = \Omega(\epsilon M/D) = \Omega(\epsilon q)$ *independently of $k$*, i.e. of $\log N$. Pushing $K$ up forces $k \to$ small, i.e. $N \to q^{O(1)}$, destroying the unbalance. GUV's substitution of Parvaresh–Vardy for Reed–Solomon buys back a $K^{1+\alpha}$-sized right side for arbitrary $N$; closing the remaining $K^{\alpha}$ is exactly the open problem of §6.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*