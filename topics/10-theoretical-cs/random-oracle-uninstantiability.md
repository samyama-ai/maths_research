---
id: 10-theoretical-cs/random-oracle-uninstantiability
title: "Random Oracle Uninstantiability"
topic: 10-theoretical-cs
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Random Oracle Uninstantiability

> **Topic:** Theoretical Computer Science · **ID:** `10-theoretical-cs/random-oracle-uninstantiability` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

The random oracle model (ROM) grants all parties oracle access to a uniformly random function $H:\{0,1\}^* \to \{0,1\}^n$. A scheme proved secure in the ROM is deployed by replacing $H$ with a concrete hash function (SHA-3, SHAKE). The **random oracle methodology** is the heuristic that this replacement preserves security.

The methodology is *false as a general principle*: Canetti, Goldreich and Halevi (STOC 1998) exhibit schemes secure in the ROM whose every concrete instantiation is insecure. The open problem is to characterise the boundary.

> **Central question.** Find a nontrivial, efficiently checkable property $P$ of cryptographic schemes such that (i) all "natural" deployed ROM constructions (FDH-RSA, RSA-OAEP, Fiat–Shamir transforms of standard protocols) satisfy $P$, and (ii) $P$ implies: if $\Pi^H$ is secure in the ROM, then there is a hash family $\mathcal{H} = \{h_s\}$, keyed by a public seed $s$, under standard assumptions, with $\Pi^{h_s}$ secure in the standard model.

A resolution in the positive direction is an explicit $P$ with a proof of the implication. A resolution in the negative direction is a proof that no such $P$ exists — e.g. an uninstantiability result for a scheme in actual deployment, or a proof that Fiat–Shamir applied to some *specific* deployed identification scheme has no sound instantiation.

## 2. Mathematical Foundations

**ROM security.** For a scheme $\Pi$ and game $G$, security means: for all oracle PPT $A$ making $q(n)$ queries,
$$\mathrm{Adv}^{G}_{\Pi}(A,n) \;=\; \Big|\Pr_{H \leftarrow \mathcal{F}_n}\big[G^{H}(\Pi^H, A^H, 1^n) = 1\big] - \tfrac12\Big| \;=\; \mathrm{negl}(n),$$
where $\mathcal{F}_n$ is the uniform distribution on functions $\{0,1\}^*\to\{0,1\}^n$.

**Instantiation.** A hash ensemble $\mathcal{H}=\{h_s : \{0,1\}^*\to\{0,1\}^n\}_{s\in\{0,1\}^{\kappa(n)}}$ with $h_s$ evaluable in time $\mathrm{poly}(n)$ and $s$ public. $\Pi^{\mathcal{H}}$ is the scheme with $H$ replaced by $h_s$, $s$ sampled at setup.

**Definition (uninstantiable).** $\Pi$ is *uninstantiable* if $\Pi^H$ is secure in the ROM but for every ensemble $\mathcal{H}$ there is a PPT $A$ with $\mathrm{Adv}^{G}_{\Pi^{\mathcal H}}(A,n) \ge 1/\mathrm{poly}(n)$ for infinitely many $n$.

**Correlation intractability (CI).** For a relation $R \subseteq \{0,1\}^* \times \{0,1\}^n$, $\mathcal{H}$ is $R$-correlation intractable if for all PPT $A$,
$$\Pr_{s,\;x \leftarrow A(s)}\big[(x,h_s(x)) \in R\big] = \mathrm{negl}(n).$$
$R$ is *sparse* if $\Pr_{y}[(x,y)\in R] = \mathrm{negl}(n)$ for all $x$. A random oracle is CI for every sparse $R$; CGH prove **no** ensemble is CI for all sparse relations, since $R^* = \{(x,y) : x = \langle \Pi\rangle,\ \Pi(x)=y\}$ (the "evasive fixed-point" relation) is sparse yet broken by $x = \langle h_s\rangle$.

**Indifferentiability** (Maurer–Renner–Holenstein). A construction $C^{f}$ from an ideal primitive $f$ is indifferentiable from $\mathcal{F}$ if there is a PPT simulator $S$ with
$$\big|\Pr[D^{C^f,\,f}=1] - \Pr[D^{\mathcal F,\,S^{\mathcal F}}=1]\big| = \mathrm{negl}(n)$$
for all distinguishers $D$. This licenses replacing $\mathcal{F}$ by $C^f$ in single-stage games — it *relocates* the idealisation rather than removing it.

**Fiat–Shamir.** For a public-coin protocol with prover messages $\alpha_i$ and verifier challenges $\beta_i$, set $\beta_i := h_s(x,\alpha_1,\dots,\alpha_i)$. Soundness of the compiled argument follows from CI for the "bad-challenge" relation $R_{\mathrm{BAD}} = \{((x,\alpha),\beta) : \beta = \mathsf{BAD}(x,\alpha)\}$, where $\mathsf{BAD}$ maps a partial transcript to the unique challenge continuable to acceptance.

## 3. History & State of the Art (SOTA)

- **1993.** Bellare and Rogaway (ACM CCS) formalise the ROM as a design paradigm; FDH and OAEP follow.
- **1997–98.** Canetti ("hash functions that hide all partial information", CRYPTO 1997) attempts partial instantiation; Canetti, Goldreich, Halevi (STOC 1998; JACM 51(4), 2004) give the diagonalisation separation — a signature scheme and an encryption scheme, secure in the ROM, insecure under every instantiation.
- **2002.** Nielsen (CRYPTO 2002): non-committing encryption with non-interactive communication exists in the ROM but is *impossible* in the standard model — an unconditional separation not relying on diagonalisation.
- **2003.** Goldwasser and Kalai (FOCS 2003): a 3-round public-coin identification scheme, secure against passive attack, whose Fiat–Shamir signature scheme is insecure under every instantiation.
- **2004.** Maurer–Renner–Holenstein (TCC) introduce indifferentiability; Bellare–Boldyreva–Palacio (EUROCRYPT) give an uninstantiable *natural-looking* hybrid-encryption/IND-CCA scheme; CGH (TCC 2004) extend to length-restricted signatures.
- **2005.** Coron–Dodis–Malinaud–Puniya (CRYPTO) fix Merkle–Damgård to be indifferentiable; Dodis–Oliveira–Pietrzak (CRYPTO) show generic full-domain hash cannot be proven secure by black-box reduction from claw-freeness.
- **2011–2014.** Ristenpart–Shacham–Shrimpton (EUROCRYPT 2011) show indifferentiability fails for multi-stage games; UCE (Bellare–Hoang–Keelveedhi, CRYPTO 2013) proposes an instantiable substitute, partially refuted by Brzuska–Farshim–Mittelbach (CRYPTO 2014) using indistinguishability obfuscation.
- **2018–2021.** Positive turn: CI for *searchable/efficiently computable* relations from LWE (Canetti–Chen–Reyzin–Rothblum 2018; Peikert–Shiehian 2019; Canetti et al., STOC 2019) yields sound Fiat–Shamir for sumcheck, GKR, and NIZK for NP in the plain model.

## 4. Partial Results / Verified Cases

**Negative (uninstantiable), fully proven:**
- CGH signatures/encryption over unrestricted messages; and (TCC 2004) with messages of length $\ge n^{\epsilon}$ for the length-restricted variant.
- Fiat–Shamir on 3-round public-coin protocols (Goldwasser–Kalai 2003), assuming an "excellent" hash-independent CRHF-type primitive; unconditional variant for interactive-proof-based FS with $2^{o(n)}$-secure primitives.
- Non-interactive non-committing encryption (Nielsen 2002) — unconditional, no diagonalisation.
- Every ensemble fails CI for the sparse relation $R^*$ above.

**Positive (instantiable), fully proven:**
- CI for all *efficiently searchable* relations of bounded size (single $y$ per $x$, computable by circuits of a priori bounded depth) from LWE with polynomial modulus-to-noise ratio (Peikert–Shiehian, CRYPTO 2019); from sub-exponential DDH (Jain–Jin, EUROCRYPT 2021).
- Consequently: NIZK for NP in the CRS model, plain-model Fiat–Shamir for the sumcheck protocol and GKR $\Rightarrow$ SNARGs for bounded-depth $\mathsf{P}$ (Choudhuri–Jain–Jin, FOCS 2021); FS for repeated squaring (Lombardi–Vaikuntanathan, CRYPTO 2020).
- Indifferentiability from a random oracle for the sponge construction with random permutation (Bertoni–Daemen–Peeters–Van Assche, EUROCRYPT 2008) and for prefix-free/HMAC/chop Merkle–Damgård (Coron et al. 2005), in single-stage games.
- CI for product relations from strong one-way product functions (Holmgren–Lombardi, FOCS 2018).

## 5. Principal Obstacles

- **Diagonalisation is unavoidable in generality.** Any candidate $\mathcal{H}$ has a short description $s$; a scheme can read $s$ and self-reference. No property of $h_s$ as a function defeats this — only a syntactic restriction on schemes (barring them from reading $s$) does, and no such restriction is known that survives composition.
- **Falsifiability barrier.** Bitansky, Dachman-Soled, Garg, Jain, Kalai, López-Alt, Wichs (TCC 2013) prove that black-box reductions cannot base Fiat–Shamir soundness for *arguments* on any falsifiable assumption, given indistinguishability obfuscation. So the natural proof route is closed for the deployed case.
- **CI for non-searchable relations is the wall.** All known CI constructions need a way to *predict* the bad output $y$ from $x$ so the hash can be programmed. For interactive arguments $\mathsf{BAD}$ is not efficiently computable, and for proofs of super-constant round complexity it is only computable in super-polynomial time. Techniques (KDM-secure encryption, FHE-based "encrypt the bad function" tricks) all break here.
- **Indifferentiability does not close the gap.** It reduces "hash is a random oracle" to "compression function/permutation is ideal"; the ideal-primitive assumption is itself uninstantiable by the same diagonalisation, and the composition theorem fails for multi-stage games (Ristenpart et al. 2011), which include deduplication, key-dependent messages, and leakage settings.
- **Assumption-side obfuscation.** iO simultaneously enables positive instantiations (UCE-style) and refutes them (Brzuska et al. 2014) — the same tool sits on both sides, so no monotone progress.

## 6. The Gap

Proven: (a) *some* ROM-secure schemes have no instantiation; (b) *some* CI classes (searchable, bounded) are instantiable from LWE/DDH. Unproven, and the exact boundary:

1. **No deployed scheme has been shown uninstantiable.** RSA-FDH, RSA-OAEP, Fiat–Shamir–Schnorr, ECDSA-style hashing: no uninstantiability proof, and no plain-model proof. The gap is whether the Goldwasser–Kalai construction can be pushed onto a scheme that does not embed a self-referential trapdoor.
2. **CI for sparse, non-searchable relations** — the precise step needed for FS on general constant-round public-coin *arguments*. Known impossible for *all* sparse relations, known possible for searchable ones; the intermediate class is open.
3. **No syntactic $P$.** There is no accepted formal notion of "natural scheme" separating CGH-style constructions from FDH.

## 7. Current Research (as of June 2026)

- **CI from lattices** (MIT, Weizmann, Berkeley, NTT Research): extending Peikert–Shiehian to relations searchable in bounded *non-uniform* time, aiming at FS for super-constant-round proofs and unbounded-depth SNARGs. Circular-security-flavoured assumptions remain the crutch. *(frontier — verify)*
- **Quantum ROM (QROM).** Boneh et al. (ASIACRYPT 2011) raise the model; Zhandry's compressed-oracle technique (CRYPTO 2019) makes QROM proofs tractable; Yamakawa–Zhandry (EUROCRYPT 2021) separate classical from quantum ROM. Whether uninstantiability is *strictly harder* in QROM is open. *(frontier — verify)*
- **Post-quantum standards.** NIST ML-DSA/SLH-DSA/ML-KEM all rest on ROM/QROM arguments, sharpening the practical stakes; ongoing work replaces ROM steps with indifferentiability-from-permutation arguments for Keccak.
- **UCE refinement.** Split-source and strongly-unpredictable UCE families survive the iO attack; the search continues for a standard-model-instantiable UCE variant strong enough for OAEP.
- **Post-quantum-secure iO** results feed both sides of the barrier; the falsifiability barrier of Bitansky et al. now holds unconditionally under known iO constructions from well-founded assumptions.

## 8. Future Work

- Identify a *cleanly stated* class $P$ — candidate: schemes whose security game does not give the adversary the hash seed as an input to a scheme-controlled circuit evaluation — and prove instantiability for it.
- Build CI hash families for the class of relations with $\mathsf{BAD}$ computable in time $2^{n^{\epsilon}}$; this would settle FS for constant-round proofs unconditionally.
- Prove or refute a *deployed* uninstantiability: exhibit an attack on FS–Schnorr for every hash instantiation, or prove FS–Schnorr sound under a falsifiable assumption.
- Extend indifferentiability to multi-stage games via "resource-restricted" simulators or reset-indifferentiability, and measure the loss.
- Settle whether the ROM is *conservative* for a restricted syntax (e.g. schemes using $H$ only as a PRF/MAC/KDF), where positive instantiation results already exist piecemeal.

## 9. Key References

- **[Foundational]** M. Bellare, P. Rogaway. *Random Oracles are Practical: A Paradigm for Designing Efficient Protocols.* ACM CCS, 1993.
- **[Foundational]** R. Canetti, O. Goldreich, S. Halevi. *The Random Oracle Methodology, Revisited.* STOC 1998; Journal of the ACM 51(4):557–594, 2004.
- **[Foundational]** J. B. Nielsen. *Separating Random Oracle Proofs from Complexity Theoretic Proofs: The Non-Committing Encryption Case.* CRYPTO 2002.
- **[Foundational]** S. Goldwasser, Y. Tauman Kalai. *On the (In)security of the Fiat-Shamir Paradigm.* FOCS 2003.
- **[Foundational]** U. Maurer, R. Renner, C. Holenstein. *Indifferentiability, Impossibility Results on Reductions, and Applications to the Random Oracle Methodology.* TCC 2004.
- **[Foundational]** M. Bellare, A. Boldyreva, A. Palacio. *An Uninstantiable Random-Oracle-Model Scheme for a Hybrid-Encryption Problem.* EUROCRYPT 2004.
- **[SOTA / Recent]** C. Peikert, S. Shiehian. *Noninteractive Zero Knowledge for NP from (Plain) Learning With Errors.* CRYPTO 2019.
- **[SOTA / Recent]** R. Canetti, Y. Chen, J. Holmgren, A. Lombardi, G. N. Rothblum, R. D. Rothblum, D. Wichs. *Fiat-Shamir: From Practice to Theory.* STOC 2019.
- **[SOTA / Recent]** N. Bitansky, D. Dachman-Soled, S. Garg, A. Jain, Y. T. Kalai, A. López-Alt, D. Wichs. *Why "Fiat-Shamir for Proofs" Lacks a Proof.* TCC 2013.
- **[SOTA / Recent]** A. Jain, Z. Jin. *Non-interactive Zero Knowledge from Sub-exponential DDH.* EUROCRYPT 2021.
- **[SOTA / Recent]** M. Zhandry. *How to Record Quantum Queries, and Applications to Quantum Indifferentiability.* CRYPTO 2019.
- **[Survey]** N. Koblitz, A. J. Menezes. *The Random Oracle Model: A Twenty-Year Retrospective.* Designs, Codes and Cryptography 77(2–3):587–610, 2015.
- **[Survey]** T. Ristenpart, H. Shacham, T. Shrimpton. *Careful with Composition: Limitations of the Indifferentiability Framework.* EUROCRYPT 2011.

## 10. Worked Example / Concrete Special Case

**The CGH diagonalisation, in full.** Start from any signature scheme $\Sigma = (\mathsf{Gen},\mathsf{Sign},\mathsf{Ver})$ that is EUF-CMA secure in the standard model. Define $\Sigma^H$ with the same $\mathsf{Gen}$, and

$$\mathsf{Sign}'^{H}_{sk}(m) \;=\;
\begin{cases}
(sk,\ \mathsf{Sign}_{sk}(m)) & \text{if } m = \langle \Pi \rangle \text{ and } \Pi(\langle\Pi\rangle) = H(\langle\Pi\rangle),\\[2pt]
(\bot,\ \mathsf{Sign}_{sk}(m)) & \text{otherwise,}
\end{cases}$$

where $\langle\Pi\rangle$ is the description of a circuit, and $\Pi(\langle\Pi\rangle)$ is evaluated with a $\mathrm{poly}(|m|)$ step bound (halting truncated to $\bot$). $\mathsf{Ver}'$ ignores the first component.

*Security in the ROM.* Fix an adversary $A$ making $q$ queries in total. For a fixed circuit $\Pi$, the value $H(\langle\Pi\rangle)$ is uniform in $\{0,1\}^n$ and independent of $\langle\Pi\rangle$, so
$$\Pr_H\big[\Pi(\langle\Pi\rangle) = H(\langle\Pi\rangle)\big] = 2^{-n}.$$
The trapdoor fires only on messages the adversary actually submits. Union bound over the $\le q$ distinct signing queries:
$$\Pr[\text{$sk$ leaked}] \le q\,2^{-n} = \mathrm{negl}(n).$$
Conditioned on no leak, $\Sigma'^H$ is exactly $\Sigma$, so $\mathrm{Adv}^{\mathrm{EUF\text{-}CMA}}_{\Sigma'^H}(A) \le \mathrm{Adv}^{\mathrm{EUF\text{-}CMA}}_{\Sigma}(B) + q2^{-n} = \mathrm{negl}(n)$.

*Insecurity under every instantiation.* Fix any ensemble $\mathcal{H}=\{h_s\}$ and let the public seed be $s$. The adversary computes the circuit $\Pi_s$ that on input $x$ outputs $h_s(x)$ — this circuit exists and has size $\mathrm{poly}(n)$ because $h_s$ is poly-time evaluable, and its description is computable from $s$ in polynomial time. Submit the single signing query
$$m^{*} \;=\; \langle \Pi_s \rangle .$$
Then $\Pi_s(\langle\Pi_s\rangle) = h_s(\langle\Pi_s\rangle)$ holds *identically*, so the trapdoor condition is met with probability $1$ and the signer returns $sk$. The adversary now signs any $m \ne m^*$ itself: total break with one query, advantage $1$.

*The wrinkle and its fix.* $\Pi_s$ must accept inputs as long as its own description, and $\mathsf{Sign}'$ must accept messages of that length. CGH (TCC 2004) remove the unbounded-length requirement by hashing the circuit description down and using a $\mathrm{poly}$-size interactive "proof of self-reference", yielding uninstantiability for signature schemes restricted to messages of length $n^{\epsilon}$.

*What it does and does not show.* The gap of Section 6 is visible here: $\mathsf{Sign}'$ **reads the seed implicitly** through the message and evaluates an adversary-supplied circuit. FDH-RSA, $\sigma = H(m)^d \bmod N$, does neither — yet no theorem separates the two, which is exactly the missing property $P$.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*