---
id: 10-theoretical-cs/security-of-fiat-shamir-in-qrom
title: "Security of Fiat-Shamir in QROM"
topic: 10-theoretical-cs
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Security of Fiat-Shamir in the Quantum Random Oracle Model

> **Topic:** Theoretical Computer Science · **ID:** `10-theoretical-cs/security-of-fiat-shamir-in-qrom` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

The Fiat–Shamir (FS) transformation turns a public-coin interactive proof into a non-interactive one by replacing the verifier's challenges with hash values of the transcript so far. Its classical security proof in the random oracle model (ROM) relies on *rewinding*: the reduction reruns the prover with a reprogrammed oracle and forks two accepting transcripts sharing a prefix.

A quantum adversary queries the hash in superposition, so the ROM is replaced by the **quantum random oracle model (QROM)**, in which the adversary gets the unitary $\ket{x}\ket{y}\mapsto\ket{x}\ket{y\oplus H(x)}$. The open problem has three layers:

1. **Quantitative.** For a $\Sigma$-protocol with challenge space $\mathcal{C}$ and a $q$-query quantum adversary, what is the true reduction loss $L(q,n)$ in
 $$\mathrm{Adv}^{\mathrm{FS}}(\mathcal{A}) \;\le\; L(q,n)\cdot \mathrm{Adv}^{\Sigma}(\mathcal{B}) \;+\; \varepsilon ?$$
 Known: $L=O(q^2)$ for $3$-round ($n=1$) and $L=(2q+1)^{2n}$ for $(2n+1)$-round protocols. **Is the exponential-in-$n$ loss necessary, or does a $\mathrm{poly}(q,n)$ reduction exist for all constant-round public-coin protocols?**
2. **Qualitative.** Is FS applied to *any* computationally-sound, constant-round, public-coin **argument** with a "quantum-friendly" special-soundness property secure in the QROM without additional structure (collapsing, commit-and-open, lossiness)?
3. **Tightness for deployed schemes.** For Fiat–Shamir-with-aborts lattice signatures (Dilithium/ML-DSA), does a QROM proof exist that is *tight* — loss $O(1)$ or $O(q)$ rather than $O(q^2)$ — under a standard assumption (MLWE/MSIS) rather than a non-standard one?

A complete resolution is either a reduction meeting the conjectured optimum, or an oracle separation exhibiting a protocol sound against quantum provers whose FS compilation is broken by a $\mathrm{poly}(q)$-query quantum attacker.

## 2. Mathematical Foundations

**$\Sigma$-protocol.** For relation $R\subseteq\mathcal{X}\times\mathcal{W}$, a three-move protocol $\Pi=(P_1,P_2,V)$ produces transcripts $(a,c,z)$ with $c\leftarrow\mathcal{C}$ uniform. It has *$k$-special soundness* if from any $k$ accepting transcripts $(a,c_1,z_1),\dots,(a,c_k,z_k)$ with distinct $c_i$ one extracts $w$ with $(x,w)\in R$. Its soundness error is $\kappa=(k-1)/|\mathcal{C}|$.

**Fiat–Shamir.** $\mathrm{FS}[\Pi]$ has prover output $(a,z)$ with $c=H(x,a)$; the verifier accepts iff $V(x,a,H(x,a),z)=1$.

**QROM.** $H:\{0,1\}^m\to\{0,1\}^\ell$ is drawn uniformly and accessed as
$$ O_H:\ \ket{x}\ket{y}\ \longmapsto\ \ket{x}\ket{y\oplus H(x)} . $$
Zhandry's **compressed oracle** replaces $H$ by a purification: the oracle register holds a superposition over databases $D\in(\{0,1\}^\ell\cup\{\bot\})^{2^m}$, and $O_H$ becomes a unitary $\mathrm{cO}$ acting on $\mathcal{H}_{\mathcal{A}}\otimes\mathcal{H}_D$ that is perfectly indistinguishable from the random $H$ while permitting *recording* — the reduction may measure $D$ to learn the adversary's queries.

**Measure-and-reprogram (Don–Fehr–Majenz–Schaffner, CRYPTO 2019).** Let $\mathcal{A}^H$ be a $q$-query algorithm outputting $(x,z)$. Define the simulator $\mathcal{S}$: pick $i\leftarrow\{1,\dots,q\}$ and $b\leftarrow\{0,1\}$, run $\mathcal{A}$ with a uniformly random $H$, measure the input register of the $i$-th query to get $\hat{x}$, then reprogram $H(\hat{x}):=\Theta$ for an externally supplied $\Theta$ and continue. Then for every $x_0$ and predicate $V$,
$$ \Pr_{\Theta}\big[x=x_0\wedge V(x_0,\Theta,z)\big] \;\ge\; \frac{1}{O(q^2)}\ \Pr_{H}\big[x=x_0\wedge V(x_0,H(x_0),z)\big], $$
with the explicit constant $1/(2q+1)^2$. Iterating over $n$ reprogrammed rounds gives loss $(2q+1)^{2n}$.

**Collapsing (Unruh, EUROCRYPT 2016).** A hash/commitment $C$ is *collapsing* if no efficient quantum adversary distinguishes (i) measuring the message register of a superposition of valid openings from (ii) not measuring it. Collapsing is the quantum surrogate for collision-resistance and is what makes a $\Sigma$-protocol's first message "classically pinned down" under superposition access.

**Adaptive reprogramming (Grilo–Hövelmanns–Hülsing–Majenz, ASIACRYPT 2021).** If a reduction reprograms $H$ at $R$ points whose min-entropy is at least $\alpha$ from the adversary's view, the distinguishing advantage of a $q$-query adversary is at most
$$ \tfrac{3}{2}\,R\,\sqrt{q}\,\cdot 2^{-\alpha/2}. $$
This yields *tight* zero-knowledge in the QROM, in contrast to soundness.

## 3. History & State of the Art (SOTA)

- **1986.** Fiat and Shamir introduce the transformation for identification-to-signature conversion; Pointcheval–Stern (1996) give the classical forking-lemma proof with loss $O(q)$.
- **2011.** Boneh, Dagdelen, Fischlin, Lehmann, Schaffner, Zhandry define the QROM and observe that the ROM proof techniques (query recording, lazy sampling, rewinding) all break.
- **2014.** Ambainis, Rosmanis, Unruh (FOCS) prove a *quantum rewinding barrier*: relative to an oracle, there is a $\Sigma$-protocol that is sound against quantum provers but whose FS/rewinding-based reductions fail; extraction by rewinding a quantum prover with a collapsing measurement can destroy the state.
- **2015–2017.** Unruh's transform gives a QROM-secure alternative to FS at the price of larger proofs. Unruh (ASIACRYPT 2017) shows FS is secure in the QROM when the $\Sigma$-protocol has *quantum proofs of knowledge* / dual-mode structure.
- **2018.** Kiltz, Lyubashevsky, Schaffner (EUROCRYPT) give the first QROM proof for FS signatures from *lossy* identification schemes, with loss $O(q^2)$ — the template later used for Dilithium.
- **2019 (breakthrough).** Don–Fehr–Majenz–Schaffner and, independently, Liu–Zhandry (both CRYPTO 2019) prove FS soundness in the QROM for any $\Sigma$-protocol with a $1/O(q^2)$ reduction, using measure-and-reprogram and Zhandry's compressed oracle respectively. This is the current SOTA for $3$-round.
- **2021–2022.** Chiesa, Ma, Spooner, Zhandry (FOCS 2021) break the rewinding barrier for *succinct* arguments via state-repair on the compressed oracle; Don–Fehr–Majenz–Schaffner (EUROCRYPT 2022) obtain **online extractability** for commit-and-open protocols, removing rewinding entirely and giving simulation-extractable NIZKs.
- **2023.** Barbosa et al. (CRYPTO 2023) find and repair a gap in the published QROM proof of Dilithium (Fiat–Shamir with aborts) and machine-check the corrected proof in EasyCrypt.

## 4. Partial Results / Verified Cases

| Class | Result | Loss |
|---|---|---|
| Any $3$-round $\Sigma$-protocol, static soundness | DFMS'19 / Liu–Zhandry'19 | $(2q+1)^2$ |
| $(2n+1)$-round public-coin, constant $n$ | DFMS multi-round measure-and-reprogram | $(2q+1)^{2n}$ |
| Commit-and-open (Picnic/MPC-in-the-head, GMW 3-colouring) with collapsing commitments | DFMS'22 online extraction | additive $O(q^3/2^{\ell})$-type terms, no rewinding |
| Lossy identification (Dilithium, qTESLA templates) | KLS'18, Barbosa et al.'23 | $O(q^2)$ from MLWE/MSIS |
| Zero-knowledge / adaptive reprogramming | GHHM'21 | tight, $\tfrac32 R\sqrt{q}\,2^{-\alpha/2}$ |
| Succinct arguments (Kilian + FS, IOP-based) | CMSZ'21, Lombardi–Ma–Spooner'22 | $\mathrm{poly}(q)$, non-explicit degree |
| Optimality of $q^2$ | DFMS'19 give an instance forcing $\Omega(q^2)$ loss for the *generic* reduction | — |

Verified concretely: for $|\mathcal{C}|=2^{256}$ and $q=2^{60}$, the $q^2$ loss consumes $120$ bits, leaving $\approx 136$ bits — enough for NIST level-5 targets, which is why deployed schemes tolerate it.

## 5. Principal Obstacles

- **No-cloning kills forking.** The classical forking lemma copies the prover's state after query $i$ and continues twice. A quantum prover's state cannot be copied; measuring the query register to learn $\hat x$ disturbs the state by an amount bounded only by the gentle-measurement lemma, $\|\rho-\rho'\|_1\le 2\sqrt{\varepsilon}$, injecting the square-root losses that compound to $q^2$.
- **Query recording is not free.** The compressed oracle records queries, but reading the database is itself a measurement; "state repair" (CMSZ) restores the adversary only approximately, and the repair cost multiplies per round — the source of the $q^{2n}$ blow-up.
- **Superposition over first messages.** A quantum prover may hold a superposition of first messages $a$. Special soundness presumes a *fixed* $a$ across the extracted transcripts. Without collapsing, there is no proof that measuring $a$ leaves a prover that still succeeds; this is exactly the Ambainis–Rosmanis–Unruh obstruction.
- **Adaptivity across rounds.** For multi-round protocols, the tree-of-transcripts extractor needs $k^n$ leaves; each quantum extraction is lossy and the losses are not independent, so no union/martingale argument currently composes them subexponentially.
- **Assumption mismatch.** Lossy-identification proofs need the "lossy key" indistinguishability, a decisional variant not implied by the search assumption used classically.

## 6. The Gap

Proven: FS is sound in the QROM for $3$-round protocols with loss $\Theta(q^2)$, and for $(2n+1)$-round with loss $q^{2n}$. Conjectured: loss $\mathrm{poly}(q)\cdot 2^{O(n)}$, or even $O(q^2)$ independent of $n$, for all constant-round public-coin protocols with $k$-special soundness.

The precise missing step is a **round-composable extraction lemma**: a statement that a measure-and-reprogram step applied at round $j$ degrades the prover's success on rounds $j+1,\dots,n$ by an *additive* $\mathrm{poly}(q)$ term rather than a *multiplicative* $1/q^2$ factor. Equivalently, one needs an efficient quantum analogue of "the prover's transcript prefix is classical information already fixed in the oracle database" for non-collapsing first messages. All current proofs obtain this only when the first message is a collapsing commitment.

## 7. Current Research (as of June 2026)

- **CWI Amsterdam / QuSoft (Fehr, Majenz, Schaffner, Don)** continue the measure-and-reprogram programme; the target is a multi-round bound with loss $\mathrm{poly}(q)\cdot C^n$ for absolute constant $C$. *(frontier — verify)*
- **Chiesa (EPFL), Spooner (Cornell), Zhandry (NTT Research)** work on post-quantum security of IOP-based SNARKs; the live question is whether FS-compiled IOPs are *knowledge-sound* with explicit polynomial degree, not just sound.
- **Lombardi (Princeton), Ma, Spooner** develop general quantum rewinding via "state repair with commitments", aiming at post-quantum simulation-extractability for constant-round protocols. *(frontier — verify)*
- **Formal-methods school (Radboud/Nijmegen, Hülsing; Inria/MPI, Barthe, Grégoire)** machine-check QROM proofs in EasyCrypt; the mechanised Dilithium proof is being extended to Falcon-style and to FS-with-aborts in general.
- **NIST-adjacent concrete-security work** on whether the $q^2$ loss can be dropped for ML-DSA under MSIS alone, which would shrink recommended parameters.

## 8. Future Work

- Prove or refute a $q^{O(1)}$-loss reduction for $5$-round protocols ($n=2$); this is the smallest open case and would signal whether $q^{2n}$ is intrinsic.
- Find an oracle separation: a quantum-sound $5$-round public-coin argument whose FS compilation admits a $\mathrm{poly}(q)$-query quantum attack. A quantum analogue of the Goldwasser–Kalai counterexample.
- Extend online extractability beyond commit-and-open to *any* collapsing-first-message protocol, eliminating rewinding from the general theorem.
- Develop lower-bound technique for QROM reductions themselves (a "meta-reduction" in the QROM), currently absent because rewinding a *reduction* is as hard as rewinding a prover.
- Tight QROM proofs for FS-with-aborts without lossiness.

## 9. Key References

- **[Foundational]** A. Fiat, A. Shamir. *How to Prove Yourself: Practical Solutions to Identification and Signature Problems.* CRYPTO 1986.
- **[Foundational]** D. Boneh, Ö. Dagdelen, M. Fischlin, A. Lehmann, C. Schaffner, M. Zhandry. *Random Oracles in a Quantum World.* ASIACRYPT 2011.
- **[Foundational]** A. Ambainis, A. Rosmanis, D. Unruh. *Quantum Attacks on Classical Proof Systems: The Hardness of Quantum Rewinding.* FOCS 2014.
- **[Foundational]** M. Zhandry. *How to Record Quantum Queries, and Applications to Quantum Indifferentiability.* CRYPTO 2019.
- **[SOTA]** J. Don, S. Fehr, C. Majenz, C. Schaffner. *Security of the Fiat-Shamir Transformation in the Quantum Random-Oracle Model.* CRYPTO 2019.
- **[SOTA]** Q. Liu, M. Zhandry. *Revisiting Post-Quantum Fiat-Shamir.* CRYPTO 2019.
- **[SOTA]** J. Don, S. Fehr, C. Majenz, C. Schaffner. *Online-Extractability in the Quantum Random-Oracle Model.* EUROCRYPT 2022.
- **[SOTA]** A. Chiesa, F. Ma, N. Spooner, M. Zhandry. *Post-Quantum Succinct Arguments: Breaking the Quantum Rewinding Barrier.* FOCS 2021.
- **[SOTA]** E. Kiltz, V. Lyubashevsky, C. Schaffner. *A Concrete Treatment of Fiat-Shamir Signatures in the Quantum Random-Oracle Model.* EUROCRYPT 2018.
- **[SOTA]** A. B. Grilo, K. Hövelmanns, A. Hülsing, C. Majenz. *Tight Adaptive Reprogramming in the QROM.* ASIACRYPT 2021.
- **[SOTA]** M. Barbosa, G. Barthe, C. Doczkal, J. Don, S. Fehr, B. Grégoire, Y.-H. Huang, A. Hülsing, Y. Lee, X. Wu. *Fixing and Mechanizing the Security Proof of Fiat-Shamir with Aborts and Dilithium.* CRYPTO 2023.
- **[Survey]** D. Unruh. *Post-Quantum Security of Fiat-Shamir.* ASIACRYPT 2017.
- **[Survey]** A. Hülsing, K. Hövelmanns et al. *A Tutorial on the Quantum Random Oracle Model.* (lecture notes / IACR ePrint), 2023.

## 10. Worked Example / Concrete Special Case

Take the **GMW 3-colouring $\Sigma$-protocol** on a graph $G=(V,E)$ with $|E|=m$, repeated in parallel $t$ times, with commitments from a collapsing hash.

- First message: $a=\big(\mathrm{com}(\pi_j(\phi(v)))\big)_{v\in V,\,j\le t}$.
- Challenge: $c=(e_1,\dots,e_t)\in E^t$, so $|\mathcal{C}|=m^t$.
- Response: openings of the two endpoints of each $e_j$.
- Soundness error per repetition: $1-1/m$; overall $\kappa=(1-1/m)^t$.

For $m=1000$ and $t=6905$: $\kappa=(1-10^{-3})^{6905}\approx e^{-6.905}\approx 10^{-3}$.

**Classical FS.** A $q$-query cheating prover succeeds with probability $\le q\kappa$. With $q=2^{60}$, $q\kappa \approx 2^{60}\cdot 2^{-9.97}$ — one must instead take $t$ large enough that $\kappa\le 2^{-128-60}$, i.e. $t \ge 188\ln 2 / 10^{-3}\cdot\log_2 e^{-1}$; numerically $t\approx 1.30\times10^{5}$.

**Quantum FS via DFMS.** The bound becomes
$$ \mathrm{Adv}^{\mathrm{FS}}(\mathcal{A}) \;\le\; (2q+1)^2\,\kappa \;+\; \mathrm{Adv}^{\mathrm{collapse}} . $$
To reach $2^{-128}$ with $q=2^{60}$ one needs $\kappa \le 2^{-128}/2^{122}=2^{-250}$, i.e.
$$ t \;\ge\; \frac{250\ln 2}{-\ln(1-10^{-3})} \;\approx\; \frac{173.3}{1.0005\times10^{-3}} \;\approx\; 1.73\times 10^{5}. $$
So the quantum proof forces $\approx 33\%$ more repetitions than the classical one purely because of the $q^2$ versus $q$ loss — a direct, measurable cost of the open problem.

**Where the loss enters.** The reduction runs $\mathcal{A}$, picks $i\leftarrow\{1,\dots,q\}$ and $b\leftarrow\{0,1\}$, measures query $i$ to obtain $\hat{x}=(x,a)$, and reprograms $H(\hat x)$ to a fresh challenge. The guess of $i$ costs $1/q$; the disturbance from measuring costs another $1/q$ through the gentle-measurement step — jointly $1/(2q+1)^2$. Classically only the guess of $i$ costs anything, giving $1/q$. Closing the gap means showing the measurement disturbance can be amortised over the $q$ queries instead of paid per-query; no technique currently does this.

Now switch to the **5-round** variant (commit, challenge, commit, challenge, open). Two reprogramming steps are needed, and the loss becomes $(2q+1)^4 = 2^{244}$ at $q=2^{60}$, exceeding the $2^{256}$ challenge space and rendering the bound vacuous for any practical parameter set. This is the smallest instance where the open problem bites.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*