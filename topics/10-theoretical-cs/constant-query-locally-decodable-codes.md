---
id: 10-theoretical-cs/constant-query-locally-decodable-codes
title: "Locally Decodable Codes with Constant Queries"
topic: 10-theoretical-cs
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Locally Decodable Codes with Constant Queries

> **Topic:** Theoretical Computer Science · **ID:** `10-theoretical-cs/constant-query-locally-decodable-codes` · **Status:** open

## 1. Problem Statement / Conjecture

Fix a constant number of queries $q \ge 3$. A $q$-query locally decodable code (LDC) encodes $k$ message symbols into $n$ codeword symbols so that any single message symbol can be recovered, with probability $\ge 2/3$, by a randomized decoder that reads only $q$ codeword positions — even when a constant fraction $\delta$ of the codeword has been adversarially corrupted.

**The open problem.** Determine the asymptotics of
$$N_q(k) \;=\; \min\{\, n : \text{a } (q,\delta,\varepsilon)\text{-LDC } C:\Sigma^k \to \Sigma^n \text{ exists}\,\}$$
for each constant $q \ge 3$ and constant $\delta,\varepsilon > 0$.

The headline question: **is $N_3(k)$ polynomial in $k$?** More sharply, the widely believed conjecture is that constant-query LDCs must be *superpolynomially* long:

> **Conjecture (folklore, attributed to the Katz–Trevisan / Goldreich school).** For every constant $q$, $N_q(k) \ge k^{\omega(1)}$; and for $q = 3$, $N_3(k) \ge 2^{k^{\Omega(1)}}$.

A complete resolution requires either (a) a construction of a $q$-query LDC of length $\mathrm{poly}(k)$ for some constant $q$, or (b) a proof that no such code exists, for all alphabets $\Sigma$ and all decoders (including nonlinear codes and adaptive decoders). The problem is open even for $q=3$ over $\Sigma = \mathbb{F}_2$.

## 2. Mathematical Foundations

Let $\Sigma$ be a finite alphabet and $\Delta(y,y')$ the relative Hamming distance.

**Definition (LDC).** $C : \Sigma^k \to \Sigma^n$ is a $(q,\delta,\varepsilon)$-LDC if there is a randomized oracle machine $\mathcal{D}$ such that for all $x \in \Sigma^k$, all $i \in [k]$, and all $y \in \Sigma^n$ with $\Delta(y, C(x)) \le \delta$,
$$\Pr[\mathcal{D}^{y}(i) = x_i] \;\ge\; \tfrac{1}{|\Sigma|} + \varepsilon,$$
and $\mathcal{D}$ makes at most $q$ queries to $y$. A **locally correctable code (LCC)** instead recovers $C(x)_j$ for any $j \in [n]$.

**Smooth / normal form.** Katz–Trevisan show that any $(q,\delta,\varepsilon)$-LDC yields a *smooth* decoder that never queries any fixed index with probability more than $\frac{q}{\delta n}$, and (for linear codes over $\mathbb{F}_2$) a *normal form*: for each $i$ there is a set $\mathcal{M}_i$ of at least $\varepsilon\delta n / q$ pairwise-disjoint $q$-subsets $S \subseteq [n]$ with
$$\sum_{j \in S} C(x)_j \;=\; x_i \quad \text{for all } x \in \mathbb{F}_2^k .$$
Each $\mathcal{M}_i$ is a **matching**; the union $\bigcup_i \mathcal{M}_i$ is a $q$-uniform hypergraph with $\Omega(kn)$ edges. Lower bounds are proved by showing such hypergraph systems are impossible when $n$ is small.

**Dual formulation.** For a linear code with generator columns $c_1,\dots,c_n \in \mathbb{F}_2^k$, a normal-form matching for $i$ is a set of disjoint triples (for $q=3$) with $c_a + c_b + c_c = e_i$. So the question becomes: *how many vectors in $\mathbb{F}_2^k$ are needed so that every standard basis vector has $\Omega(n)$ disjoint $3$-term representations?*

**Matching vector codes.** Let $m$ be a composite modulus and $S \subseteq \mathbb{Z}_m \setminus \{0\}$. A *matching vector family* is $(u_1,\dots,u_k), (v_1,\dots,v_k) \in \mathbb{Z}_m^h$ with
$$\langle u_i, v_i \rangle = 0 \ \ \forall i, \qquad \langle u_i, v_j \rangle \in S \ \ \forall i \ne j .$$
Grolmusz's construction from the Barrington–Beigel–Rudich low-degree $\mathrm{OR}$-representation modulo $m=p_1p_2$ gives families of size $k = \exp\!\big(\Omega(\tfrac{\log^2 h}{\log\log h})\big)$ — superpolynomial in $h$. Efremenko's decoder turns such a family, with $|S| = 2^r - 1$, into a $2^r$-query LDC of length $n = m^h$ by evaluating on the group $\mathbb{Z}_m^h$ and interpolating along the "line" $\{g^{t v_i}\}$.

**Known upper bounds.** Reed–Muller codes of degree $d = q-1$ over $\mathbb{F}_{\ge q+1}$ give $q$-query LDCs with $n = \exp\!\big(O(k^{1/(q-1)})\big)$. The Hadamard code is a $2$-query LDC with $n = 2^k$.

## 3. History & State of the Art (SOTA)

- **1990–1992.** Local decoding appears implicitly in program self-testing/correcting (Blum–Luby–Rubinfeld), IP $=$ PSPACE and PCP machinery, and random self-reducibility of low-degree polynomials.
- **1995.** Chor–Goldreich–Kushilevitz–Sudan introduce *private information retrieval* (PIR); the PIR/LDC equivalence (Katz–Trevisan) means every improvement transfers between the two.
- **2000.** Katz and Trevisan (STOC) give the first formal LDC definition and the first lower bounds: $n \ge \Omega\big(k^{1+1/(q-1)}\big)$ for $q$-query LDCs.
- **2002.** Goldreich–Karloff–Schulman–Trevisan prove $n \ge 2^{\Omega(k)}$ for *linear* 2-query LDCs over $\mathbb{F}_2$, and $n \ge \Omega(k^2/\log k)$ for linear 3-query.
- **2004.** Kerenidis and de Wolf, using a quantum information argument, settle $q=2$ completely: $n \ge 2^{\Omega(k)}$ for all (even nonlinear, adaptive) 2-query LDCs. This is tight against Hadamard.
- **2007.** Woodruff extends the combinatorial bounds: $\tilde{\Omega}(k^2)$ for $q=3$ and $\Omega\!\big(k^{1+1/(\lceil q/2\rceil - 1)}/\log k\big)$ for general $q$ — still the shape of the best bounds for large $q$.
- **2008.** Yekhanin (JACM) breaks the Reed–Muller barrier for $q=3$: conditional on infinitely many Mersenne primes, $n = \exp(k^{1/\log\log k})$; unconditionally $\exp(k^{1/32{,}582{,}657})$ from the then-largest known Mersenne prime.
- **2009.** Efremenko (STOC) gives unconditional $3$-query LDCs of length $n = \exp\!\big(\exp(O(\sqrt{\log k \log\log k}))\big) = \exp(k^{o(1)})$, via Grolmusz matching vectors mod $511 = 7 \cdot 73$. Dvir–Gopalan–Yekhanin systematize these as *matching vector codes*.
- **2023.** Alrabiah–Guruswami–Kothari–Manohar (STOC) prove $n \ge \tilde{\Omega}(k^3)$ for *linear* 3-query LDCs, importing semirandom CSP-refutation and Kikuchi-matrix spectral machinery.
- **2024.** Kothari–Manohar (STOC) prove an **exponential** lower bound $n \ge 2^{k^{\Omega(1)}}$ for *linear* 3-query locally **correctable** codes, and (FOCS, with sharp design bounds) superpolynomial lower bounds for smooth 3-LDCs.

**Current SOTA gap for $q=3$, linear, over $\mathbb{F}_2$:** lower bound $\tilde{\Omega}(k^3)$ (LDC) vs. upper bound $\exp(k^{o(1)})$.

## 4. Partial Results / Verified Cases

| Regime | Status |
|---|---|
| $q = 1$ | Impossible for $k \ge 2$ (trivial averaging argument). |
| $q = 2$, any alphabet, nonlinear, adaptive | **Solved.** $n = 2^{\Theta(k)}$; Kerenidis–de Wolf lower bound matches Hadamard. |
| $q=2$, large alphabet $\Sigma$, LCC | Bhattacharyya–Gopi–Tal: $n \ge 2^{\Omega(k/|\Sigma|^{?})}$-type exponential bounds; essentially settled. |
| $q = 3$, **linear** LCC over $\mathbb{F}_2$ | **Solved up to the exponent:** $n \ge 2^{k^{\Omega(1)}}$ (Kothari–Manohar 2024) vs. $\exp(k^{o(1)})$ — matching *shape*. |
| $q = 3$, **linear** LDC | $\tilde{\Omega}(k^3)$ lower bound; conjecture open. |
| $q = 3$, LCC over $\mathbb{R}$ or $\mathbb{C}$ | Dvir–Saraf–Wigderson: $n \ge \Omega(k^3)$ (superquadratic barrier broken over the reals). |
| $q$ even | $n \ge \Omega\big(k^{1+1/(\lceil q/2\rceil-1)}/\log k\big)$ (Woodruff). |
| **Matching vector codes**, all $q$ | Ben-Aroya–Efremenko–Ta-Shma: any $3$-query MV code has $n \ge \tilde{\Omega}(k^3)$; the whole MV family cannot be polynomial. |
| Smooth $3$-LDC, design-like structure | Kothari–Manohar (FOCS 2024): superpolynomial $n \ge k^{\omega(1)}$. |
| Constant *rate* with $n^{\varepsilon}$ queries | **Solved (positively):** Kopparty–Saraf–Yekhanin multiplicity codes achieve rate $1-\alpha$ with $n^{\varepsilon}$ queries — but $q$ is not constant. |

## 5. Principal Obstacles

- **Nonlinearity.** Every strong bound past $\tilde\Omega(k^2)$ (AGKM, Kothari–Manohar) uses linearity to get a normal form: $\sum_{j\in S} y_j = x_i$. For nonlinear codes the decoder is an arbitrary function of $q$ symbols; no hypergraph/matrix object is available to spectrally analyze.
- **The quantum argument stops at $q=2$.** Kerenidis–de Wolf convert a 2-query LDC into a 1-query *quantum* random access code and apply Nayak's bound $n \ge \Omega(k)$ qubits. For $q \ge 3$ the reduction produces $\lceil q/2 \rceil$-query quantum codes, and no matching quantum information bound is known — this is exactly the source of Woodruff's $\lceil q/2 \rceil$ exponent.
- **Fourier analysis is too coarse.** Over $\mathbb{F}_2$ the natural approach — bounding the number of characters supported by a matching — collapses because the matchings are *disjoint* and the constraint graph is sparse ($O(kn)$ edges out of $\binom{n}{3}$), so Fourier mass is spread and no character-level obstruction appears.
- **Kikuchi lifting has an inherent exponent loss.** The recent breakthroughs lift a 3-uniform hypergraph to a Kikuchi graph on $\binom{n}{\ell}$ vertices and compare its spectral norm to its edge count. The trace-moment bounds degrade with $\ell$, and pushing $\ell$ high enough to reach exponential bounds for *decodable* (rather than correctable) codes is not currently controlled.
- **Constructions are stuck at group algebras.** All known subexponential constructions are matching vector codes, and BET proves this route cannot reach $\mathrm{poly}(k)$. Any polynomial-length construction must abandon the $\mathbb{Z}_m^h$ / Grolmusz template entirely.
- **Barriers by consequence.** Strong LDC lower bounds imply progress on matrix rigidity (Dvir) and on explicit rigid matrices, an area with its own long-standing barriers — evidence that the problem is not merely technical.

## 6. The Gap

For $q=3$ over $\mathbb{F}_2$ the interval between proven and conjectured is:
$$\underbrace{\tilde{\Omega}(k^3)}_{\text{AGKM 2023, linear LDC}} \;\le\; N_3(k) \;\le\; \underbrace{\exp\!\big(\exp(O(\sqrt{\log k \log\log k}))\big)}_{\text{Efremenko 2009}} .$$
Two distinct steps must be crossed.

1. **From LCC to LDC.** Kothari–Manohar's exponential bound uses that *every* codeword coordinate is locally correctable, giving $n$ matchings rather than $k$. An LDC supplies only $k$ matchings, and there is no known reduction from LDC to LCC at constant query count. Closing this is the single most concrete open step.
2. **From linear to nonlinear.** No technique currently converts an arbitrary $q$-local decoder into a linear-algebraic constraint system without losing the query count.

For $q \ge 4$ the gap is far wider: lower bound $\tilde\Omega(k^{1+1/(\lceil q/2\rceil-1)})$ versus upper bound $\exp(k^{o(1)})$, and even *super-quadratic* bounds are unknown for $q = 5$.

## 7. Current Research (as of June 2026)

- **Kikuchi-matrix / CSP-refutation school** (Kothari, Manohar, Guruswami, Alrabiah, Hsieh, Tulsiani). The dominant program: encode the local-decoding hypergraph as a Kikuchi matrix and bound its spectral norm. Active target is extending the $2^{k^{\Omega(1)}}$ LCC bound to LDCs and to $q = 4,5$. *(frontier — verify)* Preprints since 2025 report exponential bounds for 3-LDCs over large alphabets and for "design 3-LDCs"; the general nonlinear $q=3$ case is reported still open.
- **Quantum-information approaches.** Renewed attempts to find a $\lceil q/2 \rceil$-query quantum RAC bound strong enough to give super-quadratic bounds for $q=4$ (de Wolf and collaborators).
- **Algebraic geometry / lifted codes.** Guo–Kopparty–Sudan lifted Reed–Solomon codes and Hermitian-curve variants continue to be probed for constant-query behavior; no construction has beaten Efremenko.
- **Approximate and relaxed variants.** Relaxed LDCs (Ben-Sasson–Goldreich–Harsha–Sudan–Vadhan; Asadi–Shinkar; Cohen–Yankovitz) achieve $n = k^{1+o(1)}$ with constant queries under a weakened "reject $\perp$" guarantee — the strongest evidence that the difficulty lies in the *always-correct* requirement.
- **Institutions.** CMU, Berkeley/Simons, UT Austin, Weizmann, Tel Aviv, CWI, Princeton/IAS.

## 8. Future Work

- **Prove an LDC$\to$LCC-style amplification** at constant $q$, or show a formal separation between $N_q^{\mathrm{LDC}}$ and $N_q^{\mathrm{LCC}}$.
- **Handle nonlinearity** via a "local linearization" lemma: show any constant-query decoder can be replaced by an affine one with polynomial loss in $n$, or exhibit a nonlinear code that provably beats every linear one.
- **Settle $q=4$:** obtain $n \ge k^{2+\Omega(1)}$, which Woodruff's method cannot give.
- **Beat Efremenko or prove MV-optimality.** Either construct a 3-query LDC of length $\exp(k^{o(1)})$ outside the matching-vector paradigm, or prove all 3-query LDCs are essentially matching vector codes.
- **Harvest consequences:** exponential 3-LDC bounds would give explicit rigid matrices and new arithmetic-circuit lower bounds; conversely, polynomial-length 3-query LDCs would yield $\mathrm{poly}(k)$-communication 3-server PIR with $k^{o(1)}$ per-server cost.

## 9. Key References

- **[Foundational]** J. Katz and L. Trevisan. *On the efficiency of local decoding procedures for error-correcting codes.* STOC 2000, pp. 80–86.
- **[Foundational]** O. Goldreich, H. Karloff, L. J. Schulman, L. Trevisan. *Lower bounds for linear locally decodable codes and private information retrieval.* Computational Complexity, 15(3):263–296, 2006 (CCC 2002).
- **[Foundational]** I. Kerenidis and R. de Wolf. *Exponential lower bound for 2-query locally decodable codes via a quantum argument.* Journal of Computer and System Sciences, 69(3):395–420, 2004.
- **[Foundational]** B. Chor, O. Goldreich, E. Kushilevitz, M. Sudan. *Private information retrieval.* Journal of the ACM, 45(6):965–981, 1998 (FOCS 1995).
- **[Construction]** S. Yekhanin. *Towards 3-query locally decodable codes of subexponential length.* Journal of the ACM, 55(1):1–16, 2008.
- **[Construction]** K. Efremenko. *3-query locally decodable codes of subexponential length.* SIAM Journal on Computing, 41(6):1694–1703, 2012 (STOC 2009).
- **[Construction]** Z. Dvir, P. Gopalan, S. Yekhanin. *Matching vector codes.* SIAM Journal on Computing, 40(4):1154–1178, 2011.
- **[Lower bound]** D. Woodruff. *New lower bounds for general locally decodable codes.* ECCC TR07-006, 2007.
- **[Lower bound]** A. Ben-Aroya, K. Efremenko, A. Ta-Shma. *A note on amplifying the error-tolerance of locally decodable codes.* / *Local list decoding with a constant number of queries.* FOCS 2010. (See also Ben-Aroya–Efremenko–Ta-Shma, *A note on matching vector codes*, ECCC TR10-088, 2010.)
- **[SOTA]** O. Alrabiah, V. Guruswami, P. K. Kothari, P. Manohar. *A near-cubic lower bound for 3-query locally decodable codes from semirandom CSP refutation.* STOC 2023, pp. 1438–1448.
- **[SOTA]** P. K. Kothari and P. Manohar. *An exponential lower bound for linear 3-query locally correctable codes.* STOC 2024.
- **[SOTA]** P. K. Kothari and P. Manohar. *Superpolynomial lower bounds for smooth 3-LCCs and sharp bounds for designs.* FOCS 2024.
- **[Related]** Z. Dvir, S. Saraf, A. Wigderson. *Superquadratic lower bound for 3-query locally correctable codes over the reals.* Theory of Computing, 13(11):1–36, 2017.
- **[Related]** S. Kopparty, S. Saraf, S. Yekhanin. *High-rate codes with sublinear-time decoding.* Journal of the ACM, 61(5):28, 2014.
- **[Survey]** S. Yekhanin. *Locally Decodable Codes.* Foundations and Trends in Theoretical Computer Science, 6(3):139–255, 2012.
- **[Survey]** L. Trevisan. *Some applications of coding theory in computational complexity.* Quaderni di Matematica, 13:347–424, 2004.

## 10. Worked Example / Concrete Special Case

**The Hadamard code with $k=3$, and why $q=2$ forces $n = 2^k$.**

Let $C : \mathbb{F}_2^3 \to \mathbb{F}_2^8$ be $C(x)_a = \langle a, x\rangle \bmod 2$, indexing coordinates by $a \in \mathbb{F}_2^3$. For $x = (1,0,1)$:

| $a$ | 000 | 001 | 010 | 011 | 100 | 101 | 110 | 111 |
|---|---|---|---|---|---|---|---|---|
| $C(x)_a$ | 0 | 1 | 0 | 1 | 1 | 0 | 1 | 0 |

**Decoding $x_2$ with 2 queries.** Pick $a \in \mathbb{F}_2^3$ uniformly; query positions $a$ and $a \oplus e_2$ where $e_2 = 010$. Output $y_a \oplus y_{a \oplus e_2}$. On the uncorrupted word this equals $\langle a,x\rangle + \langle a + e_2, x\rangle = \langle e_2, x\rangle = x_2$. Check with $a = 101$: $y_{101} \oplus y_{111} = 0 \oplus 0 = 0 = x_2$. ✓

**Error tolerance.** Both queries are individually uniform over the 8 positions ("perfectly smooth"). If $y$ differs from $C(x)$ in a $\delta$-fraction of positions, a union bound gives
$$\Pr[\text{decoder errs}] \;\le\; \Pr[a \text{ corrupt}] + \Pr[a\oplus e_2 \text{ corrupt}] \;\le\; 2\delta,$$
so for $\delta < 1/6$ success is $\ge 2/3$. This works for every $k$: $n = 2^k$, $q=2$, $\varepsilon = 1/2 - 2\delta$.

**Why this length is forced.** Kerenidis–de Wolf convert the decoder into the single quantum query $\frac{1}{\sqrt{2}}(|a\rangle + |a \oplus e_i\rangle)$ applied to the state $\frac{1}{\sqrt n}\sum_a (-1)^{y_a}|a\rangle$ ($\log n$ qubits). Measuring in the basis $\{|a\rangle \pm |a\oplus e_i\rangle\}$ recovers $x_i$ with probability $\ge 2/3$ for every $i$ *from one state*. Nayak's random-access-code bound then forces $\log n \ge \Omega(k)$, i.e. $n \ge 2^{\Omega(k)}$. Hadamard is optimal.

**Where $q=3$ diverges.** Adding a third query lets the decoder use *triples* $\{a,b,c\}$ with $c_a + c_b + c_c = e_i$ instead of *pairs*, and Reed–Muller already exploits this: degree-$2$ polynomials over $\mathbb{F}_5$ restricted to a random line through the evaluation point give a 3-query LDC with $n = \exp(O(\sqrt{k}))$ — a square-root saving over $2^k$. Efremenko's matching-vector code pushes the same idea to $n = \exp(k^{o(1)})$. The quantum argument, however, only yields a *2-query quantum* code from a 3-query classical one, and no exponential bound is known there — which is precisely why $2^k$ is proven for $q=2$ and only $\tilde\Omega(k^3)$ is proven for $q = 3$.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*