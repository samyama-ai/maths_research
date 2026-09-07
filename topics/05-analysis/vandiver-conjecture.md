---
id: 05-analysis/vandiver-conjecture
title: "Vandiver Conjecture"
topic: 05-analysis
status: empirically-supported
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Vandiver Conjecture

> **Topic:** Real & Complex Analysis · **ID:** `05-analysis/vandiver-conjecture` · **Status:** empirically-supported

## 1. Problem Statement / Conjecture

Let $p$ be an odd prime, $\zeta_p = e^{2\pi i/p}$, and let $\mathbb{Q}(\zeta_p)^+ = \mathbb{Q}(\zeta_p + \zeta_p^{-1})$ be the maximal real subfield of the $p$-th cyclotomic field. Write $h_p^+$ for its class number.

**Conjecture (Vandiver).** For every odd prime $p$,
$$p \nmid h_p^+ .$$

Equivalently: the $p$-Sylow subgroup of the ideal class group of $\mathbb{Q}(\zeta_p)^+$ is trivial. A complete proof must establish this for all odd primes; a disproof requires exhibiting a single prime $p$ with $p \mid h_p^+$ (necessarily an irregular prime, and necessarily $p > 2^{31}$ by current computation).

The conjecture is *not* a theorem and there is no consensus that it is true: Washington's heuristic predicts roughly $\tfrac12 \log\log X$ counterexamples below $X$, i.e. about one counterexample in the first $10^{10^{9}}$ primes. The label "empirically-supported" reflects verification for all $p < 2\cdot 10^9$ with no failure, against a heuristic that predicts failures too rarely to observe.

## 2. Mathematical Foundations

Let $K = \mathbb{Q}(\zeta_p)$, $G = \mathrm{Gal}(K/\mathbb{Q}) \cong (\mathbb{Z}/p)^\times$, cyclic of order $p-1$. Let $A$ be the $p$-Sylow subgroup of the class group $\mathrm{Cl}(K)$, and let $J \in G$ denote complex conjugation. Since $p \nmid \\#G$, the group ring $\mathbb{Z}_p[G]$ is a product of local rings and $A$ decomposes into eigenspaces under the Teichmüller character $\omega : G \to \mathbb{Z}_p^\times$:
$$A = \bigoplus_{i=0}^{p-2} A^{(i)}, \qquad A^{(i)} = \varepsilon_i A, \quad \varepsilon_i = \frac{1}{p-1}\sum_{a=1}^{p-1} \omega(a)^{-i}\sigma_a^{-1}.$$
Set $A^+ = (1+J)A/2$ and $A^- = (1-J)A/2$, so $A^+ = \bigoplus_{i \text{ even}} A^{(i)}$. Because $\mathrm{Cl}(\mathbb{Q}(\zeta_p)^+) \hookrightarrow \mathrm{Cl}(K)^+$ with index a power of $2$, Vandiver's conjecture is equivalent to
$$A^+ = 0 \iff A^{(i)} = 0 \text{ for all even } i.$$

**Class number factorization.** $h_p = h_p^- h_p^+$ with $h_p^+ = h(\mathbb{Q}(\zeta_p)^+)$ and the relative class number given analytically by
$$h_p^- = 2p \prod_{\chi \text{ odd}} \left( -\tfrac{1}{2} B_{1,\chi} \right), \qquad B_{1,\chi} = \frac{1}{p}\sum_{a=1}^{p-1} \chi(a)\, a .$$

**Kummer's criterion.** $p \mid h_p$ iff $p$ divides the numerator of some Bernoulli number $B_{2k}$, $1 \le k \le (p-3)/2$, where $\frac{t}{e^t-1} = \sum_{n\ge0} B_n \frac{t^n}{n!}$. Such $p$ are *irregular*; the pairs $(p,2k)$ are the *irregular pairs* and their number is the index of irregularity $i_p$.

**Herbrand–Ribet.** For even $k$ with $2 \le k \le p-3$: $A^{(p-k)} \neq 0 \iff p \mid \mathrm{num}(B_k)$. This controls the *odd* eigenspaces $A^{(p-k)}$ only; Vandiver concerns the complementary *even* ones and is not decided by Bernoulli divisibility.

**Iwasawa theory.** Let $K_\infty = \bigcup_n \mathbb{Q}(\zeta_{p^{n+1}})$, $\Gamma = \mathrm{Gal}(K_\infty/K) \cong \mathbb{Z}_p$, $\Lambda = \mathbb{Z}_p[[T]]$, and $X_\infty = \varprojlim A_n$. Then $|A_n| = p^{\mu p^n + \lambda n + \nu}$ for $n \gg 0$. Ferrero–Washington gives $\mu = 0$ for abelian fields. The Mazur–Wiles theorem (Iwasawa Main Conjecture) identifies the characteristic ideal of $X_\infty^{(i)}$ for odd $i$ with the Kubota–Leopoldt $p$-adic $L$-function $L_p(s,\omega^{1-i})$; the even part is *not* determined by an $L$-function, which is precisely the source of the difficulty.

**Equivalent formulations.**
- $A^+ = 0$ iff $A^-$ is cyclic over $\mathbb{Z}_p[G]$ (Iwasawa).
- Vandiver for $p$ implies $A^{(p-k)}$ is cyclic of order $p^{\,v_p(B_k \text{-related } L\text{-value})}$ and $\lambda^-$ equals $i_p$-type counts.
- Kurihara: Vandiver for $p$ is equivalent to $K_{4n}(\mathbb{Z}) \otimes \mathbb{Z}_p = 0$ for all $n$ (given Quillen–Lichtenbaum, now a theorem via Voevodsky–Rost).
- Vandiver implies the first case of Fermat's Last Theorem for $p$ (Vandiver's original motivation) and implies $\mathbb{Z}[\zeta_p]$ has "no unexpected $p$-units": the cyclotomic units generate the full unit group up to index prime to $p$ in the relevant eigenspaces.

## 3. History & State of the Art (SOTA)

- **1847–1857 — Kummer.** Introduced regular primes, proved FLT for them, and verified $p \nmid h_p^+$ for $p < 100$. The statement "$p \nmid h_p^+$" appears implicitly in Kummer's work; the conjecture is sometimes called the Kummer–Vandiver conjecture.
- **1929, 1946 — Vandiver.** H. S. Vandiver isolated the hypothesis and proved the first case of FLT under it, publishing systematic criteria in *Fermat's last theorem: its history and the nature of the known results concerning it* (Amer. Math. Monthly, 1946).
- **1954 — Vandiver, Lehmer, Lehmer.** First machine (SWAC) verification, to $p < 2000$.
- **1976 — Ferrero–Washington.** $\mu = 0$ for abelian fields, removing one structural unknown.
- **1976 — Ribet.** Converse to Herbrand, completing Herbrand–Ribet.
- **1984 — Mazur–Wiles.** Main Conjecture over $\mathbb{Q}$; determines $A^-$ eigenspace orders exactly, leaves $A^+$ untouched.
- **1993–2001 — Buhler, Crandall, Ernvall, Metsänkylä, Shokrollahi.** Verification to $p < 12{,}000{,}000$ using fast Bernoulli-number computation mod $p$.
- **2011 — Buhler–Harvey.** Irregular primes and Vandiver to $163{,}577{,}856$.
- **2017 — Hart, Harvey, Ong.** Verification to $2\cdot 10^9$ — the current record. No counterexample.
- **2003 — Schoof.** Heuristic computation of the "plus" class numbers $h_p^+$ for $p < 10000$, giving conjectural values (all small, mostly $1$).

## 4. Partial Results / Verified Cases

- **Regular primes.** Trivially true: $p \nmid h_p$ implies $p \nmid h_p^+$. Regular primes have density conjecturally $e^{-1/2} \approx 60.65\%$.
- **Computational range.** True for all odd $p < 2^{31} \approx 2.15\cdot10^9$ (Hart–Harvey–Ong 2017), covering every irregular prime in that range, including all $\approx 7.6\times10^7$ irregular primes found there. The verification uses the criterion: if for each irregular pair $(p,2k)$ there exists $t$ with $2 \le t \le p-2$ such that $q_t = \frac{t^{p-1}-1}{p}$ satisfies $\sum$-conditions on $B_{2k}$-related Voronoi congruences, then Vandiver holds for $p$.
- **Small index of irregularity.** Explicit criteria (Vandiver, Washington Thm 8.14 ff.) verify $p \nmid h_p^+$ whenever a single Kummer-type congruence involving $B_{2k}$ and the $p$-adic logarithm of a cyclotomic unit is nonzero mod $p$; this succeeds unconditionally for all known $p$.
- **Structural consequences proven under Vandiver.** For every $p$ in the verified range: $A^-$ is cyclic as $\mathbb{Z}_p[G]$-module; $\lambda^+ = 0$ (Greenberg's conjecture holds for $\mathbb{Q}(\zeta_p)^+$ in that range); $K_{4n}(\mathbb{Z})\otimes\mathbb{Z}_p = 0$ for those $p$.
- **Small $p$ table.** $h_p^+ = 1$ for all $p < 100$ except conjecturally $p = 163$ ($h^+ = 4$), $p=191$ ($h^+=11$); in all computed cases $\gcd(p, h_p^+) = 1$.
- **Function-field analogue.** The analogue over $\mathbb{F}_q(t)$ with cyclotomic function fields (Carlitz modules) is **false**: counterexamples were exhibited by Hayes-type constructions and by explicit computation, showing the conjecture is not formal.

## 5. Principal Obstacles

- **No $L$-function for the plus part.** Mazur–Wiles computes $\mathrm{char}_\Lambda(X_\infty^{(i)})$ for *odd* $i$ via $L_p(s,\omega^{1-i})$. For even $i$ the corresponding $p$-adic $L$-function is (up to the trivial-zero factor) attached to the *unit* side, and the Main Conjecture in that range degenerates to a statement about $A^+$ itself. The analytic input simply is not there.
- **Euler systems produce only annihilators of $A^-$.** The cyclotomic-unit Euler system bounds $A^-$ from above by an analytic quantity. Applying Kolyvagin/Rubin machinery to the plus part requires a global unit or Stark-type element whose existence is equivalent to what one wants to prove — a circularity.
- **Class field theory gives no lower-bound obstruction.** Vandiver's is a *vanishing* statement; there is no known cohomological obstruction whose triviality forces $A^+ = 0$. Genus theory and reflection (Leopoldt's Spiegelungssatz) give only $\dim A^{(i)} \le \dim A^{(1-i)} + 1$, transferring information from minus to plus with a slack of one dimension that is never eliminated.
- **Heuristics predict failure.** Washington's Cohen–Lenstra-style count says $\\#\{p \le X : p \mid h_p^+\} \approx \tfrac12 \log\log X$. So any proof must exploit a rigid arithmetic mechanism, not a probabilistic one — yet no such mechanism is visible, and the function-field analogue shows none can be purely formal.
- **Computation is only linear in reach.** Verification cost per prime is $\tilde O(p)$ for Bernoulli numbers mod $p$; extending from $2\cdot10^9$ to $10^{11}$ is a ~50× compute increase and provides essentially zero additional evidence on a $\log\log$ scale.

## 6. The Gap

Proven: $A^-$ is completely described by $p$-adic $L$-values (Mazur–Wiles), $\mu=0$ (Ferrero–Washington), and $A^+ = 0$ for $p < 2\cdot10^9$ by direct congruence checks. Unproven: any statement about $A^{(i)}$ for even $i$ valid for *all* $p$.

The exact barrier: one needs to show that the map
$$\mathcal{C}_\infty \hookrightarrow \mathcal{U}_\infty \quad (\text{cyclotomic units into local units})$$
has cokernel with trivial $\Gamma$-coinvariants in even eigenspaces — equivalently that the "index of cyclotomic units" $[\mathcal{E}:\mathcal{C}] = h_p^+$ is prime to $p$. Every known route computes this index only *as* $h_p^+$, so the statement is a tautology rather than a derivation. Crossing the gap requires an independent handle on $\mathcal{E}/\mathcal{C}$ — e.g. an unconditional construction of $p$-units in real cyclotomic fields (Stark units), or a new Euler system whose derived classes annihilate $A^+$.

## 7. Current Research (as of June 2026)

- **Mihăilescu's programme.** Preda Mihăilescu (Göttingen) has circulated several preprints since 2010 attacking Vandiver via "Stickelberger and the eigenspace decomposition of $A^+$" and $p$-adic transcendence-style arguments (Baker–Brumer linear forms in $p$-adic logarithms of cyclotomic units). Substantial partial statements — e.g. bounds on $\mathrm{rank}\,A^+$ in terms of $i_p$ — have been claimed. *(frontier — verify)*: no full proof has been refereed and accepted.
- **Iwasawa-theoretic / Greenberg's conjecture.** Groups at Keio (Kurihara), Tokyo, and Bordeaux study $\lambda^+ = 0$ for real abelian fields; Greenberg's conjecture and Vandiver are logically independent but share the same missing analytic input.
- **Motivic / K-theoretic route.** Following Kurihara (1992) and Weibel's exposition of Quillen–Lichtenbaum, the equivalence with $K_{4n}(\mathbb{Z})_{(p)} = 0$ has redirected effort toward computing motivic cohomology $H^2_{\mathcal{M}}(\mathbb{Z},\mathbb{Z}(2n+1))$ directly. No independent computation of these groups exists.
- **Higher-rank Euler/Kolyvagin systems.** Work of Burns, Sano, Sakamoto and collaborators on the equivariant Tamagawa number conjecture and Rubin–Stark elements gives conditional descriptions of $A^+$ assuming Rubin–Stark; the Rubin–Stark conjecture for real cyclotomic fields is itself open. *(frontier — verify)*
- **Extended computation.** Follow-ups to Hart–Harvey–Ong using GPU Bernoulli arithmetic have been discussed for reaching $10^{10}$. *(frontier — verify)*

## 8. Future Work

- Prove Rubin–Stark for $\mathbb{Q}(\zeta_p)^+$ unconditionally; this would give explicit $p$-units and a genuine upper bound on $[\mathcal{E}:\mathcal{C}]$ independent of $h^+$.
- Sharpen Leopoldt reflection to remove the $+1$ slack, or find a second reflection relation coupling $A^{(i)}$ and $A^{(1-i)}$ with strict inequality.
- Determine whether the function-field counterexamples have a characteristic-$0$ shadow: identify precisely which archimedean/unit-theoretic input is unavailable in the Carlitz setting, and whether it is strong enough to force $A^+=0$.
- Compute $h_p^+$ unconditionally (not just heuristically) for $p$ up to $10^4$, extending Schoof's work; each such value gives one hard data point rather than a congruence check.
- Replace verification-per-prime by verification of a *density* statement: prove $\\#\{p\le X: p\mid h_p^+\} = o(\pi(X))$, currently unknown even in that weak form.

## 9. Key References

- **[Foundational]** E. E. Kummer. *Über die Zerlegung der aus Wurzeln der Einheit gebildeten complexen Zahlen in ihre Primfactoren.* J. reine angew. Math. 35 (1847), 327–367.
- **[Foundational]** H. S. Vandiver. *Fermat's last theorem: its history and the nature of the known results concerning it.* American Mathematical Monthly 53 (1946), 555–578.
- **[Foundational]** H. S. Vandiver, D. H. Lehmer, E. Lehmer. *An application of high-speed computing to Fermat's last theorem.* Proc. Nat. Acad. Sci. USA 40 (1954), 25–33.
- **[Textbook]** L. C. Washington. *Introduction to Cyclotomic Fields.* 2nd ed., Graduate Texts in Mathematics 83, Springer, 1997. (Chapters 8, 10, 13; Washington's heuristic on counterexample density.)
- **[Foundational]** B. Ferrero, L. C. Washington. *The Iwasawa invariant $\mu_p$ vanishes for abelian number fields.* Annals of Mathematics 109 (1979), 377–395.
- **[Foundational]** K. Ribet. *A modular construction of unramified $p$-extensions of $\mathbb{Q}(\mu_p)$.* Inventiones Mathematicae 34 (1976), 151–162.
- **[Foundational]** B. Mazur, A. Wiles. *Class fields of abelian extensions of $\mathbb{Q}$.* Inventiones Mathematicae 76 (1984), 179–330.
- **[Structural]** M. Kurihara. *Some remarks on conjectures about cyclotomic fields and K-groups of $\mathbb{Z}$.* Compositio Mathematica 81 (1992), 223–236.
- **[Computational]** J. Buhler, R. Crandall, R. Ernvall, T. Metsänkylä, M. A. Shokrollahi. *Irregular primes and cyclotomic invariants to 12 million.* Journal of Symbolic Computation 31 (2001), 89–96.
- **[Computational]** J. Buhler, D. Harvey. *Irregular primes to 163 million.* Mathematics of Computation 80 (2011), 2435–2444.
- **[SOTA / Recent]** W. Hart, D. Harvey, W. Ong. *Irregular primes to two billion.* Mathematics of Computation 86 (2017), 3031–3049.
- **[Computational]** R. Schoof. *Class numbers of real cyclotomic fields of prime conductor.* Mathematics of Computation 72 (2003), 913–937.
- **[Survey]** C. Weibel. *Algebraic K-theory of rings of integers in local and global fields.* In: Handbook of K-Theory, Springer, 2005.

## 10. Worked Example / Concrete Special Case

Take $p = 37$, the third irregular prime.

**Step 1 — irregularity.** Kummer's criterion requires checking $B_{2k}$ for $1 \le k \le 17$. The relevant one is $B_{32}$:
$$B_{32} = -\frac{7709321041217}{510}.$$
Reduce the numerator mod $37$: $7709321041217 = 37 \cdot 208360028141 + 0$, so $37 \mid \mathrm{num}(B_{32})$. Hence $(37,32)$ is an irregular pair and $i_{37}=1$ (no other even index works). So $37 \mid h_{37}$.

**Step 2 — locate the divisibility.** Herbrand–Ribet with $k=32$ gives
$$A^{(37-32)} = A^{(5)} \neq 0,$$
and $5$ is **odd**, so the nontrivial eigenspace sits in $A^-$. Indeed the relative class number is $h_{37}^- = 37$, and $A \cong \mathbb{Z}/37$ concentrated in $A^{(5)}$.

**Step 3 — the Vandiver check.** Vandiver asserts $A^{(i)} = 0$ for the even indices $i = 0,2,4,\dots,34$. Since $i_{37}=1$, the only even index that could conceivably be nonzero by reflection is $i = 1-5 \equiv 32 \pmod{36}$: Leopoldt's Spiegelungssatz gives
$$\dim_{\mathbb{F}_{37}} A^{(32)} \le \dim_{\mathbb{F}_{37}} A^{(5)} + 1 .$$
This alone permits $A^{(32)}$ to be nonzero — the slack the general proof cannot close. One therefore runs the explicit criterion: pick $t=2$ and compute the Fermat quotient
$$q_2 = \frac{2^{36}-1}{37} \bmod 37 .$$
Since $2^{36} - 1 = 68719476735 = 37 \cdot 1857283155$, and $1857283155 \equiv 22 \pmod{37}$, we get $q_2 \equiv 22 \not\equiv 0$. Vandiver's criterion (Washington, Cor. 8.19 form) states that if for the irregular pair $(p,2k)$ some $t$ gives a nonvanishing associated congruence, then $p \nmid h_p^+$. Here the check succeeds, so $A^{(32)} = 0$.

**Step 4 — conclusion.** $A^+ = 0$, so $37 \nmid h_{37}^+$. Independently, $h_{37}^+ = 1$, and $h_{37} = h_{37}^- \cdot h_{37}^+ = 37 \cdot 1 = 37$, matching Step 2.

**What this shows.** The whole content of Vandiver's conjecture is that Step 3 never fails. For $37$ it is one Fermat-quotient computation. For a general $p$ it is $i_p$ such computations, each of which succeeds "by luck" — with heuristic failure probability $\approx 1/p$ per irregular pair, summing to $\sum_p i_p/p \sim \tfrac12\log\log X$ expected failures. The verification to $2\cdot10^9$ is $7.6\times10^7$ consecutive lucky outcomes; the conjecture is the claim that the luck is not luck at all.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*