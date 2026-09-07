---
id: 10-theoretical-cs/sliding-scale-conjecture
title: "Sliding Scale Conjecture"
topic: 10-theoretical-cs
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Sliding Scale Conjecture

> **Topic:** Theoretical Computer Science · **ID:** `10-theoretical-cs/sliding-scale-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

The Sliding Scale Conjecture (SSC) asks whether the soundness error of a probabilistically checkable proof can be driven down to $1/\mathrm{poly}(n)$ while keeping the proof of polynomial size, a constant number of queries, and an answer alphabet only polynomially larger than the reciprocal of the error.

**Conjecture (Bellare–Goldwasser–Lund–Russell, 1993).** There is a constant $c \ge 1$ such that for every $\varepsilon = \varepsilon(n)$ with $1/n^{c'} \le \varepsilon \le 1/2$ (some $c' > 0$), every language in $\mathsf{NP}$ has a PCP verifier that

* uses $r = O(\log n)$ random bits,
* makes $2$ queries into a proof over alphabet $\Sigma$ with $|\Sigma| \le (1/\varepsilon)^{c}$,
* has perfect completeness, and
* has soundness error at most $\varepsilon$.

Equivalently: gap **Label Cover** (equivalently, gap $2$-CSP with projection constraints) on instances of size $\mathrm{poly}(n)$ with alphabet $|\Sigma| = \mathrm{poly}(1/\varepsilon)$ and soundness $\varepsilon$ is $\mathsf{NP}$-hard for $\varepsilon$ as small as $1/\mathrm{poly}(n)$.

A proof requires exhibiting such a verifier (or reduction) for all of $\mathsf{NP}$; a disproof requires showing that $\mathsf{NP} \not\subseteq \mathsf{PCP}_{1,\varepsilon}[O(\log n), 2]$ over alphabets of size $\mathrm{poly}(1/\varepsilon)$ for some $\varepsilon = n^{-\Omega(1)}$, which — since the containment is not known to fail even unconditionally — would itself be a major complexity separation.

## 2. Mathematical Foundations

**Two-prover games / Label Cover.** A projection game is $G = (U, V, E, \Sigma_U, \Sigma_V, \{\pi_e\}_{e \in E})$, a bipartite graph with edge maps $\pi_e : \Sigma_U \to \Sigma_V$. The value is
$$
\mathrm{val}(G) \;=\; \max_{\substack{f: U \to \Sigma_U \\ g: V \to \Sigma_V}} \; \Pr_{e = (u,v) \sim E}\big[\, \pi_e(f(u)) = g(v) \,\big].
$$
Gap Label Cover $\mathrm{LC}(1, \varepsilon)$ is the promise problem of distinguishing $\mathrm{val}(G) = 1$ from $\mathrm{val}(G) \le \varepsilon$. The SSC states that $\mathrm{LC}(1,\varepsilon)$ is $\mathsf{NP}$-hard for $\varepsilon = |G|^{-\Omega(1)}$ with $|\Sigma_U| = \mathrm{poly}(1/\varepsilon)$.

**PCP notation.** $L \in \mathsf{PCP}_{c,s}[r, q]_{\Sigma}$ if a verifier reading $r$ random bits and $q$ symbols of a proof $\pi \in \Sigma^{2^{O(r)}}$ accepts $x \in L$ with probability $\ge c$ for some $\pi$, and accepts $x \notin L$ with probability $\le s$ for every $\pi$. The PCP theorem (Arora–Safra; Arora–Lund–Motwani–Sudan–Szegedy) gives
$$
\mathsf{NP} = \mathsf{PCP}_{1,\,1/2}[O(\log n),\, O(1)]_{\{0,1\}} .
$$

**Trivial limits.** Soundness $\varepsilon$ with $q$ queries forces $|\Sigma|^{q} \ge 1/\varepsilon$: a random proof already passes with probability $\approx |\Sigma|^{-q}$ on a fixed test. So $|\Sigma| = \mathrm{poly}(1/\varepsilon)$ is optimal up to the exponent, which is why the tradeoff is called a *sliding scale*: as $\varepsilon$ slides from $\Omega(1)$ down to $1/\mathrm{poly}(n)$, $|\Sigma|$ slides up polynomially, and $r$ stays at $O(\log n)$.

**Parallel repetition.** For $G^{\otimes t}$ (the $t$-fold parallel product), Raz's theorem gives
$$
\mathrm{val}(G^{\otimes t}) \;\le\; (1-\delta)^{\Omega\!\left(t / \log |\Sigma|\right)}, \qquad \delta = \delta(1-\mathrm{val}(G)) > 0,
$$
so $t = \Theta(\log n)$ repetitions of a constant-gap game reach $\varepsilon = 1/\mathrm{poly}(n)$ with $|\Sigma^t| = \mathrm{poly}(n) = \mathrm{poly}(1/\varepsilon)$ — the correct alphabet — but randomness $t \cdot O(\log n) = O(\log^2 n)$, hence proof size $n^{\Theta(\log n)}$. The whole conjecture is thus the *randomness* clause.

## 3. History & State of the Art (SOTA)

* **1993.** Bellare, Goldwasser, Lund and Russell (STOC 1993) formulate the tradeoff between error and answer size and pose the conjecture, motivated by hardness of approximation with polynomial factors.
* **1997.** Raz and Safra give a sub-constant error low-degree test and a PCP with error $n^{-\Omega(1)}$ but a *constant* number of queries only after composition, with alphabet larger than $\mathrm{poly}(1/\varepsilon)$ in the relevant regime. Arora–Sudan independently give improved low-degree testing.
* **1999.** Dinur, Fischer, Kindler, Raz and Safra ("PCP characterizations of NP: towards a polynomially-small error-probability") obtain $O(1)$-query PCPs of polynomial size with error $2^{-(\log n)^{1-o(1)}}$ and alphabet $2^{(\log n)^{1-o(1)}}$ — the sliding-scale relation $\varepsilon = |\Sigma|^{-\Omega(1)}$ holding up to *quasi-polynomially small* error.
* **2008–2010.** Moshkovitz and Raz achieve the same error regime with exactly **two** queries and nearly-linear proof size: $\mathsf{NP} \subseteq \mathsf{PCP}_{1,\varepsilon}[\log n + O(\log^{1-o(1)} n), 2]$ with $\varepsilon = 2^{-(\log n)^{1-o(1)}}$.
* **2009–2013.** Dinur and Harsha isolate *decodable PCPs* as the right composition primitive in the low-error regime, simplifying and modularizing DFKRS.
* **2024–2026.** High-dimensional expander (HDX) based agreement testing (Bafna–Minzer; Bafna–Minzer–Vyas) yields quasi-linear-size 2-query PCPs with small soundness, reopening the randomness-efficiency question with combinatorial rather than algebraic tools.

Status: the conjecture is proven for every error down to $2^{-(\log n)^{1-o(1)}}$ and open for every $\varepsilon \le 2^{-(\log n)^{1-o(1)}}$, in particular for the target $\varepsilon = n^{-\delta}$.

## 4. Partial Results / Verified Cases

* **Constant $\varepsilon$.** True for every fixed $\varepsilon > 0$: apply Raz's parallel repetition $t = O_\varepsilon(1)$ times to the ALMSS PCP. Alphabet $\mathrm{poly}(1/\varepsilon)$, randomness $O(\log n)$.
* **$\varepsilon \ge 2^{-(\log n)^{1-o(1)}}$, i.e. alphabet up to $2^{(\log n)^{1-o(1)}}$.** True, by DFKRS (constant queries) and Moshkovitz–Raz (two queries, near-linear size). This covers all $\varepsilon = 1/\mathrm{polylog}(n)$ and $\varepsilon = 2^{-\log n/\log\log n}$.
* **Quasi-polynomial proof size.** True in full for $\varepsilon = n^{-\delta}$ if the size bound is relaxed to $n^{O(\log n)}$ (Raz repetition, $t = \Theta(\log n)$, $|\Sigma| = \mathrm{poly}(n)$). Consequently the SSC statements are known *under quasi-$\mathsf{NP}$-hardness*, e.g. $2^{(\log n)^{1-o(1)}}$-factor results become $n^{\Omega(1)}$-factor results.
* **Algebraic components.** Sub-constant-error low-degree testing is fully resolved: for degree-$d$ polynomials over $\mathbb{F}_q^m$, the plane-vs-plane test has error $\mathrm{poly}(d/q)$ (Raz–Safra), and direct-product/agreement tests achieve error $\exp(-\Omega(k))$ for $k$-wise direct products (Dinur–Livni Navon; Bafna–Minzer). These are the SSC bound *for the test itself*.
* **Special instance families.** For *free* games (complete bipartite constraint graph) and for smooth/fortified projection games, low-error reductions with the right alphabet exist, but the size blow-up remains quasi-polynomial for free games.

## 5. Principal Obstacles

* **Randomness-efficient repetition is provably not black-box.** The natural route — replace the $t$ independent edges of $G^{\otimes t}$ by a random walk on an expander, reusing randomness so that $r = O(\log n)$ — fails. Feige and Kilian (STOC 1995) construct two-prover systems where recycling randomness in this way does *not* decrease the error at the required rate; the provers can correlate answers across correlated coordinates. No derandomized parallel repetition theorem is known for general games at any nontrivial rate.
* **Parallel repetition is tight, not lossy-in-our-favor.** Raz's counterexample to strong parallel repetition shows $\mathrm{val}(G^{\otimes t})$ can be as large as $(1-\Theta(\delta^2))^{t}$ for odd-cycle games, ruling out the $(1-\delta)^{\Theta(t)}$ rate that would let $t = o(\log n)$ repetitions suffice.
* **Composition costs alphabet.** Low-error PCP composition (Dinur–Harsha) needs an inner verifier that is *list-decodable* with list size $L$; the soundness one can prove degrades like $L \cdot \varepsilon_{\text{inner}}$, and known inner objects have $L$ growing with $1/\varepsilon$, so each composition level loses a $(\log n)^{o(1)}$ factor in the exponent. Iterating $\omega(1)$ levels — needed to reach $\varepsilon = n^{-\delta}$ — accumulates exactly the $2^{-(\log n)^{1-o(1)}}$ barrier.
* **Algebraic tests hit a field-size wall.** Low-degree tests over $\mathbb{F}_q$ have error $\Omega(d/q)$ and the encoding length is $q^m$ with $d \cdot m \approx \log n$; pushing $q$ to $n^{\delta}$ to get error $n^{-\delta}$ forces $m = O(1)$ and destroys the arity needed for efficient encoding.
* **No lower-bound technique.** Nothing rules out the conjecture either. Any refutation would give a nontrivial upper bound on $\mathsf{NP}$'s PCP power, a regime with no known techniques.

## 6. The Gap

Known: soundness $\varepsilon$ with alphabet $\mathrm{poly}(1/\varepsilon)$ and $O(\log n)$ randomness for all
$$
\varepsilon \;\ge\; 2^{-(\log n)^{1-o(1)}} .
$$
Wanted: the same for $\varepsilon = 2^{-\Omega(\log n)} = n^{-\Omega(1)}$. The gap is the multiplicative $(\log n)^{o(1)}$ in the exponent — equivalently, the step from $\mathrm{polylog}$-many effective repetitions to $\Theta(\log n)$ of them without spending $\Theta(\log^2 n)$ random bits.

Precisely, the missing object is a **randomness-efficient repetition or amplification step**: a transformation $G \mapsto G'$ with $|G'| = \mathrm{poly}(|G|)$, $|\Sigma'| = |\Sigma|^{O(t)}$, and
$$
\mathrm{val}(G) \le 1-\delta \;\Longrightarrow\; \mathrm{val}(G') \le 2^{-\Omega(t)}, \qquad t = \Theta(\log |G|),
$$
where $G'$ uses only $O(\log |G|)$ random bits. Every known construction achieving the soundness pays $\Omega(t \log |G|)$ randomness.

## 7. Current Research (as of June 2026)

* **HDX-based agreement testing.** Bafna and Minzer's characterization of direct-product testing via coboundary expansion, and Bafna–Minzer–Vyas's quasi-linear-size 2-query PCPs with small soundness, replace the algebraic low-degree test by sparse complexes. Sparsity is exactly randomness-efficiency, making this the most direct current attack on the SSC randomness bottleneck. *(frontier — verify the precise soundness/alphabet tradeoff achieved.)*
* **Projection Games Conjecture (PGC).** Moshkovitz's weaker statement — near-linear-size projection games with soundness $\varepsilon$ and alphabet $\mathrm{poly}(1/\varepsilon)$ for *constant* $\varepsilon$ — is the size-efficient sibling of SSC and is a proving ground for the same composition machinery.
* **Derandomized/decoupled repetition.** Work on parallel repetition with correlated questions (expander-walk repetition for *specific* game families, e.g. games with structured or "fortified" constraint graphs) seeks the missing amplification step on restricted instances.
* **Groups.** Weizmann (Dinur, Minzer, Safra), MIT/Tel Aviv (Bafna, Moshkovitz), IISc/TIFR (Harsha, Bhangale), and the broader PCP/hardness community.

## 8. Future Work

* Prove derandomized parallel repetition for projection games whose constraint graph is a good expander, even at rate $2^{-\Omega(t/\mathrm{polylog})}$; that alone would break the $(\log n)^{1-o(1)}$ exponent barrier.
* Build a decodable PCP with list size $L = \mathrm{poly}(1/\varepsilon)$ *independent of the composition depth*, allowing $\omega(1)$ composition levels without exponent loss.
* Push HDX agreement tests to soundness $\varepsilon = |\Sigma|^{-\Omega(1)}$ on complexes of size $\mathrm{poly}(n)$ with $\Sigma$ of size $n^{\delta}$.
* Explore refutation: identify a natural family of games for which $\mathrm{val}$ is approximable in polynomial time at the sliding-scale parameters, hinting at an unconditional barrier.
* Catalog consequences: SSC would upgrade $2^{(\log n)^{1-o(1)}}$-factor $\mathsf{NP}$-hardness to $n^{\Omega(1)}$ for Label Cover, Min-Rep, Directed Steiner problems, and would strengthen Dinur–Kindler–Raz–Safra's $n^{\Omega(1/\log\log n)}$ hardness for the Closest Vector Problem.

## 9. Key References

- **[Foundational]** M. Bellare, S. Goldwasser, C. Lund, A. Russell. *Efficient Probabilistically Checkable Proofs and Applications to Approximation.* STOC 1993, pp. 294–304.
- **[Foundational]** S. Arora, C. Lund, R. Motwani, M. Sudan, M. Szegedy. *Proof Verification and the Hardness of Approximation Problems.* Journal of the ACM 45(3):501–555, 1998.
- **[Foundational]** R. Raz. *A Parallel Repetition Theorem.* SIAM Journal on Computing 27(3):763–803, 1998.
- **[Foundational]** R. Raz, S. Safra. *A Sub-Constant Error-Probability Low-Degree Test, and a Sub-Constant Error-Probability PCP Characterization of NP.* STOC 1997, pp. 475–484.
- **[SOTA]** I. Dinur, E. Fischer, G. Kindler, R. Raz, S. Safra. *PCP Characterizations of NP: Toward a Polynomially-Small Error-Probability.* STOC 1999; journal version, Computational Complexity 20(3):413–504, 2011.
- **[SOTA]** D. Moshkovitz, R. Raz. *Two-Query PCP with Subconstant Error.* Journal of the ACM 57(5), Article 29, 2010.
- **[SOTA]** I. Dinur, P. Harsha. *Composition of Low-Error 2-Query PCPs Using Decodable PCPs.* SIAM Journal on Computing 42(6):2452–2486, 2013 (FOCS 2009).
- **[Obstacle]** U. Feige, J. Kilian. *Impossibility Results for Recycling Random Bits in Two-Prover Proof Systems.* STOC 1995, pp. 457–468.
- **[Obstacle]** R. Raz. *A Counterexample to Strong Parallel Repetition.* SIAM Journal on Computing 40(3):771–777, 2011.
- **[Related]** S. Arora, M. Sudan. *Improved Low-Degree Testing and its Applications.* Combinatorica 23(3):365–426, 2003.
- **[Related]** I. Dinur, G. Kindler, R. Raz, S. Safra. *Approximating CVP to Within Almost-Polynomial Factors is NP-Hard.* Combinatorica 23(2):205–243, 2003.
- **[Related]** D. Moshkovitz. *The Projection Games Conjecture and the NP-Hardness of $\ln n$-Approximating Set-Cover.* Theory of Computing 11:221–235, 2015.
- **[Frontier]** M. Bafna, D. Minzer. *Characterizing Direct Product Testing via Coboundary Expansion.* STOC 2024.
- **[Survey]** O. Goldreich. *Computational Complexity: A Conceptual Perspective.* Cambridge University Press, 2008 (Ch. 9, PCP).

## 10. Worked Example / Concrete Special Case

Take 3SAT instance $\varphi$ with $m$ clauses and $n$ variables, and form the **clause-vs-variable game** $G$: $U$ = clauses with $\Sigma_U$ = the $7$ satisfying assignments to the clause's three variables; $V$ = variables with $\Sigma_V = \{0,1\}$; edges pick a clause $u$ uniformly and one of its three variables $v$ uniformly; $\pi_{(u,v)}$ restricts the clause assignment to $v$.

If $\varphi$ is satisfiable, $\mathrm{val}(G) = 1$. If $\varphi$ is at most $(1-\eta)$-satisfiable (as guaranteed by the PCP theorem applied to the instance), then any variable assignment falsifies $\ge \eta m$ clauses, and for each such clause the prover's clause-answer disagrees on at least one of three variables, so
$$
\mathrm{val}(G) \;\le\; 1 - \eta/3 .
$$
Concretely with $\eta = 1/8$: $\mathrm{val}(G) \le 1 - 1/24$, $|\Sigma_U| = 7$, randomness $r = \log_2(3m)$.

Now amplify. With $t$-fold parallel repetition, Raz gives
$$
\mathrm{val}(G^{\otimes t}) \le (1 - 1/24)^{\Omega(t/\log 7)} = 2^{-ct}
$$
for an absolute constant $c > 0$. To hit target error $\varepsilon = 1/N$ where $N = \mathrm{poly}(m)$ is the final instance size, set $t = \frac{1}{c}\log_2 N$. Then:

| quantity | value | SSC requirement | verdict |
|---|---|---|---|
| alphabet $|\Sigma_U^t| = 7^{t}$ | $N^{\log_2 7 / c} = \mathrm{poly}(1/\varepsilon)$ | $\mathrm{poly}(1/\varepsilon)$ | ✅ |
| soundness | $2^{-ct} = 1/N$ | $\le \varepsilon$ | ✅ |
| randomness $t \cdot \log_2(3m)$ | $\Theta(\log^2 m)$ | $O(\log m)$ | ❌ |
| proof size | $m^{\Theta(\log m)}$ | $\mathrm{poly}(m)$ | ❌ |

Every entry meets the conjecture except the randomness, which overshoots by exactly a factor $\Theta(\log m)$. Contrast the resolved regime: choosing $t = (\log m)^{1-o(1)} / c$ gives randomness $(\log m)^{2-o(1)}$ — still too much — which is why Moshkovitz–Raz do *not* proceed by repetition but by a manifold-vs-point low-degree test composed with itself; their route reaches $\varepsilon = 2^{-(\log m)^{1-o(1)}}$ with randomness $\log m + O((\log m)^{1-o(1)})$, and the residual $(\log m)^{1-o(1)}$ additive term is precisely the Gap of Section 6.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*