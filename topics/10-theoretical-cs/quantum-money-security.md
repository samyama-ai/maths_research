---
id: 10-theoretical-cs/quantum-money-security
title: "Quantum Money Security"
topic: 10-theoretical-cs
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Quantum Money Security

> **Topic:** Theoretical Computer Science · **ID:** `10-theoretical-cs/quantum-money-security` · **Status:** open

## 1. Problem Statement / Conjecture

Quantum money exploits the no-cloning theorem to build banknotes that cannot be duplicated. The private-key case (Wiesner, ~1970) is solved: unconditional security holds when only the mint can verify. The open problem is the **public-key** case.

> **Main open problem.** Does there exist a *publicly verifiable* quantum money scheme — a triple $(\mathrm{Gen}, \mathrm{Ver}, \mathrm{Count})$ where anyone holding a public key can verify a note, no one but the mint can produce new ones, and security rests on a *standard, well-studied* computational assumption?

A complete resolution requires either:

1. **Construction + reduction:** an explicit scheme with a polynomial-time reduction from counterfeiting to a falsifiable assumption believed to hold against quantum polynomial-time (QPT) adversaries (e.g. LWE, isogeny problems, indistinguishability obfuscation with a proven instantiation); or
2. **Impossibility:** a proof that public-key quantum money cannot exist, or cannot be based on such assumptions — necessarily a non-relativizing proof, since Aaronson–Christiano exhibit an oracle relative to which it *does* exist.

Every candidate proposed since 2009 is either broken, or secure only relative to an oracle, or based on a bespoke assumption invented for that scheme.

## 2. Mathematical Foundations

**Definition (quantum money scheme).** A scheme is a tuple of QPT algorithms:
$$\mathrm{Gen}(1^\lambda) \to (\mathrm{sk}, \mathrm{pk}),\qquad \mathrm{Mint}(\mathrm{sk}) \to (s, \rho_s),\qquad \mathrm{Ver}(\mathrm{pk}, s, \rho) \to \{0,1\},$$
with $s$ a classical serial number and $\rho_s$ the quantum note. **Correctness:** $\Pr[\mathrm{Ver}(\mathrm{pk},s,\rho_s)=1] \ge 1-\mathrm{negl}(\lambda)$.

**Security (unforgeability).** For every QPT $\mathcal{A}$,
$$\Pr\Big[ \mathrm{Count}\big(\mathrm{pk}, \mathcal{A}(\mathrm{pk}, s, \rho_s^{\otimes k})\big) \ge k+1 \Big] \le \mathrm{negl}(\lambda),$$
where $\mathrm{Count}$ verifies a purported $(k{+}1)$-note register in the same serial number. Private-key money is the special case $\mathrm{pk} = \bot$ with $\mathcal{A}$ unbounded but given only oracle access to $\mathrm{Ver}(\mathrm{sk},\cdot,\cdot)$.

**Wiesner's scheme.** $\mathrm{sk} = (x, \theta) \in \{0,1\}^n \times \{0,1\}^n$; the note is
$$|\$_{x,\theta}\rangle = \bigotimes_{i=1}^{n} H^{\theta_i}|x_i\rangle,$$
i.e. each qubit is one of the four BB84 states $\{|0\rangle,|1\rangle,|{+}\rangle,|{-}\rangle\}$. Verification measures qubit $i$ in basis $\theta_i$ and checks the outcome equals $x_i$.

**No-cloning.** There is no unitary $U$ on $\mathcal{H}\otimes\mathcal{H}$ with $U(|\psi\rangle\otimes|0\rangle) = |\psi\rangle^{\otimes 2}$ for all $|\psi\rangle$; the inner-product identity $\langle\psi|\phi\rangle = \langle\psi|\phi\rangle^2$ forces $|\psi\rangle,|\phi\rangle$ equal or orthogonal (Wootters–Zurek 1982, Dieks 1982).

**Hidden-subspace money (Aaronson–Christiano).** For a subspace $A \le \mathbb{F}_2^n$ with $\dim A = n/2$, the note is the coset state
$$|A\rangle = \frac{1}{\sqrt{|A|}}\sum_{a\in A} |a\rangle, \qquad H^{\otimes n}|A\rangle = |A^{\perp}\rangle .$$
Verification projects onto $|A\rangle\langle A|$ using membership oracles $U_A, U_{A^\perp}$: measure $\mathbb{1}_A$ in the computational basis, apply $H^{\otimes n}$, measure $\mathbb{1}_{A^\perp}$. In the real scheme the oracles are replaced by public multivariate polynomial systems $\{p_i\}$ over $\mathbb{F}_2$ of degree $d\ge 3$ with $\{x : p_i(x)=0\ \forall i\} = A$.

**Quantum lightning (Zhandry).** A strengthening: a QPT $\mathrm{Gen}$ outputs $(s,\rho_s)$ such that no QPT adversary can produce two states with the *same* serial number, even choosing $s$ itself. Formally, for all QPT $\mathcal{A}$ outputting $(s, \rho_1, \rho_2)$,
$$\Pr[\mathrm{Ver}(s,\rho_1)=\mathrm{Ver}(s,\rho_2)=1] \le \mathrm{negl}(\lambda).$$
Quantum lightning implies public-key money and implies collision-resistant hashing.

## 3. History & State of the Art

- **~1970 / 1983.** Stephen Wiesner writes *Conjugate Coding*; rejected for a decade, published in SIGACT News 15(1), 1983. First proposal of unforgeable quantum banknotes; the same paper seeds BB84.
- **2009.** Aaronson (CCC) formalizes public-key quantum money, shows it exists relative to a quantum oracle, and proves no scheme can be information-theoretically secure in the public-key setting (an unbounded adversary searches for any state accepted by the public verifier).
- **2010.** Lutomirski et al., *Breaking and making quantum money*, propose collision-based and knot-based ideas; Farhi–Gosset–Hassidim–Lutomirski–Shor (ITCS 2012) give **quantum money from knots**, using superpositions over grid diagrams with fixed Alexander polynomial. Still unbroken, but with no reduction to a standard problem.
- **2012.** Molina–Vidick–Watrous compute the *exact* optimal counterfeiting probability for Wiesner's scheme: $(3/4)^n$.
- **2012.** Aaronson–Christiano (STOC), *Quantum money from hidden subspaces*: security proven unconditionally relative to a classical subspace oracle ($2^{\Omega(n)}$ queries needed), plus a concrete instantiation by low-degree polynomials.
- **2016–2019.** The "noisy" Aaronson–Christiano instantiation is broken by Gröbner/algebraic attacks (Conde Pena–Durán Díaz–Faugère–Hernández Encinas–Perret, IET Information Security 2019). Zhandry (EUROCRYPT 2019) shows the oracle can be replaced by indistinguishability obfuscation, and introduces **quantum lightning** with a candidate from multi-collision-resistant hashing.
- **2021.** Roberts (EUROCRYPT 2021) breaks Zhandry's concrete lightning candidate.
- **2022–2023.** Khesin–Lu–Shor propose publicly verifiable money from random lattices; Liu–Montgomery–Zhandry (EUROCRYPT 2023) break it and prove structural barriers for lattice-based money. Shmueli (STOC 2022) constructs public-key money with a *classical* bank from iO + LWE.
- **2024.** Zhandry, *Quantum money from abelian group actions* (ITCS 2024) — currently the most standard-looking assumption base.

**SOTA summary:** public-key quantum money is known (i) relative to oracles, (ii) from indistinguishability obfuscation, (iii) from cryptographic group actions. It is *not* known from any assumption in the standard, long-studied set (factoring, LWE, isogeny path-finding without extra structure).

## 4. Partial Results / Verified Cases

- **Private-key, $\mathrm{Ver}$ oracle used once per note:** Wiesner's scheme is unconditionally secure. Optimal $1\to 2$ counterfeiting success is exactly $(3/4)^n$ (Molina–Vidick–Watrous 2012); the general $k \to k+1$ optimum is also known in closed form.
- **Private-key from one-way functions:** pseudorandom quantum states (Ji–Liu–Song, CRYPTO 2018) yield private-key money with a *reusable* verifier, from any post-quantum OWF. This case is fully solved.
- **Public-key relative to a classical oracle:** hidden-subspace money is secure with $2^{\Omega(n)}$ oracle queries required, for $\dim A = n/2$ (Aaronson–Christiano 2012). Ben-David–Sattath (2023) extend the same oracle to quantum tokens for digital signatures.
- **Public-key from iO:** if indistinguishability obfuscation for classical circuits exists and is post-quantum secure, public-key money exists (Zhandry 2019); Shmueli 2022 upgrades this to a fully classical bank.
- **Public-key from abelian group actions:** secure under a new but structurally clean assumption on cryptographic group actions (Zhandry 2024).
- **Negative results.** No public-key scheme is information-theoretically secure (Aaronson 2009). Wiesner's scheme with a *reusable, answer-returning* verifier is broken: Lutomirski's online attack (2010) and the adaptive attack of Nagaj–Sattath–Brodutch–Unruh (QIC 16, 2016) recover $(x,\theta)$ with polynomially many interactions.
- **Broken candidates.** AC noisy instantiation (degree-$d$ polynomial systems, $d=3,4$) — algebraic attack; Zhandry lightning from multi-collision hashing — Roberts 2021; Khesin–Lu–Shor lattices — Liu–Montgomery–Zhandry 2023.

## 5. Principal Obstacles

- **No-cloning does not survive public verification.** A public verifier is a projector $\Pi_s$ the adversary can implement herself. Given $\Pi_s$, an unbounded adversary can prepare an accepted state by amplitude amplification, so *all* public-key security is computational. Purely information-theoretic tools (fidelity, trace distance, adversary-method bounds) therefore cap out at oracle separations.
- **The verifier leaks its own witness.** Any efficient $\Pi_s$ is a circuit; the natural security reduction must show that this circuit does not help build a second copy. This is exactly the functionality-hiding that obfuscation provides — which is why every known standard-model construction goes through iO or an iO-flavored primitive.
- **Structure invites algebra.** Making $\mathrm{Ver}$ efficient forces algebraic structure (polynomial ideals, lattices, isogeny graphs). That same structure is what Gröbner-basis, lattice-reduction, and isogeny-walk attacks consume. Each break above followed this pattern: the AC polynomials fell to $F_4$-style elimination because $\deg = 3$ ideals over $\mathbb{F}_2$ with $n/2$-dimensional solution spaces are far from generic.
- **No black-box reduction technique.** A reduction must, from a counterfeiter producing $\rho_1 \otimes \rho_2$, extract a classical solution to a hard problem. Rewinding a quantum adversary is constrained by measurement disturbance; the state-repair techniques (Chiesa–Ma–Spooner–Zhandry) apply to proofs, not to two-copy extraction.
- **Barrier results.** Liu–Montgomery–Zhandry show that money built from lattices in the natural "coset state" way collapses, because the dual-lattice structure yields a second copy; this rules out a broad design template rather than a single scheme.

## 6. The Gap

Proven: private-key money unconditionally; public-key money **relative to an oracle** or **from iO / group actions**. Wanted: public-key money from a standard assumption, or an impossibility proof.

The precise missing step is a **de-oraclization** that is not obfuscation. Concretely: replace the subspace membership oracles $U_A, U_{A^\perp}$ in
$$\Pi_A = H^{\otimes n}\,\mathbb{1}_{A^\perp}\, H^{\otimes n}\,\mathbb{1}_{A}$$
by an efficiently evaluable public description $D_A$ such that (i) $D_A$ decides membership in $A$, and (ii) no QPT algorithm given $D_A$ and $|A\rangle$ outputs $|A\rangle^{\otimes 2}$. Every explicit $D_A$ tried so far — polynomial systems, lattice bases, hash-based commitments — has satisfied (i) and failed (ii). iO satisfies both, but is not a standard assumption. On the impossibility side, any proof must be non-relativizing, since the oracle world is a counterexample.

## 7. Current Research (as of June 2026)

- **Group actions and isogenies.** Zhandry's abelian-group-action money (ITCS 2024) is the focus of ongoing cryptanalysis; Montgomery–Sharif and others study class-group actions on supersingular elliptic curves as a money source. Whether these assumptions survive is open *(frontier — verify)*.
- **Quaternion algebras / modular forms.** Kane–Sharif–Silverberg, *Quantum money from quaternion algebras* (Mathematical Cryptology, 2022): notes are superpositions over ideal classes in a quaternion order; the hard problem is finding an isogeny/ideal equivalence. Cryptanalysis remains active *(frontier — verify)*.
- **Knot money.** The 2012 FGHLS scheme is still unbroken after 14 years and is the oldest surviving candidate; the security assumption (hardness of identifying grid diagrams with equal Alexander polynomial) has no reduction to anything standard.
- **Barriers.** Extending the Liu–Montgomery–Zhandry template to rule out further families (e.g. all "coset-state with efficiently checkable dual" schemes) is an active line at MIT, NTT Research, Princeton, and Weizmann.
- **Adjacent primitives.** Unclonable cryptography more broadly — copy-protection, unclonable encryption, one-shot signatures — is being mapped onto the same assumption landscape; one-shot signatures from standard assumptions would imply public-key money.

## 8. Future Work

- Build a scheme whose counterfeiting problem *is* a standard problem (e.g. reduce directly from LWE or isogeny path-finding), rather than one invented alongside the scheme.
- Prove a black-box separation: public-key quantum money cannot be built from collision-resistant hashing, or from one-way functions alone.
- Determine whether **quantum lightning** exists at all under any standard assumption; it currently has no surviving concrete candidate outside iO.
- Sharpen the AC oracle bound and determine whether the $2^{\Omega(n)}$ query lower bound is tight for $\dim A = n/2$, and how it degrades for $\dim A = \alpha n$, $\alpha \ne 1/2$.
- Study whether verification can be made *destructive-but-public* (a weaker notion) with a standard-assumption proof, as a stepping stone.

## 9. Key References

- **[Foundational]** Stephen Wiesner. *Conjugate Coding.* SIGACT News 15(1):78–88, 1983.
- **[Foundational]** W. K. Wootters and W. H. Zurek. *A single quantum cannot be cloned.* Nature 299:802–803, 1982.
- **[Foundational]** Scott Aaronson. *Quantum Copy-Protection and Quantum Money.* IEEE Conference on Computational Complexity (CCC), 2009.
- **[Foundational]** Scott Aaronson and Paul Christiano. *Quantum Money from Hidden Subspaces.* STOC 2012.
- **[SOTA]** Mark Zhandry. *Quantum Lightning Never Strikes the Same State Twice.* EUROCRYPT 2019.
- **[SOTA]** Mark Zhandry. *Quantum Money from Abelian Group Actions.* ITCS 2024.
- **[SOTA]** Jiahui Liu, Hart Montgomery, Mark Zhandry. *Another Round of Breaking and Making Quantum Money: How to Not Build It from Lattices, and More.* EUROCRYPT 2023.
- **[SOTA]** Bhaskar Roberts. *Security Analysis of Quantum Lightning.* EUROCRYPT 2021.
- **[SOTA]** Omri Shmueli. *Public-key Quantum Money with a Classical Bank.* STOC 2022.
- **[Analysis]** Abel Molina, Thomas Vidick, John Watrous. *Optimal counterfeiting attacks and generalizations for Wiesner's quantum money.* TQC 2012, LNCS 7582.
- **[Analysis]** Daniel Nagaj, Or Sattath, Aharon Brodutch, Dominique Unruh. *An adaptive attack on Wiesner's quantum money.* Quantum Information and Computation 16(11–12), 2016.
- **[Construction]** Edward Farhi, David Gosset, Avinatan Hassidim, Andrew Lutomirski, Peter Shor. *Quantum money from knots.* ITCS 2012.
- **[Construction]** Daniel M. Kane, Shahed Sharif, Alice Silverberg. *Quantum money from quaternion algebras.* Mathematical Cryptology, 2022.
- **[Cryptanalysis]** Marta Conde Pena, Raúl Durán Díaz, Jean-Charles Faugère, Luis Hernández Encinas, Ludovic Perret. *Non-quantum cryptanalysis of the noisy version of Aaronson–Christiano's quantum money scheme.* IET Information Security 13(4), 2019.
- **[Survey]** Zhengfeng Ji, Yi-Kai Liu, Fang Song. *Pseudorandom Quantum States.* CRYPTO 2018.

## 10. Worked Example / Concrete Special Case

**Wiesner's scheme with $n=2$: exactly how well can a forger do?**

Bank picks $x=(x_1,x_2)$, $\theta=(\theta_1,\theta_2)$ uniformly; note $|\$\rangle = H^{\theta_1}|x_1\rangle \otimes H^{\theta_2}|x_2\rangle$. Each qubit is uniform over $\{|0\rangle,|1\rangle,|{+}\rangle,|{-}\rangle\}$, so the marginal is $\rho = \mathbb{1}/2$ — the forger learns nothing for free.

*Attack A — measure and re-prepare.* Measure each qubit in the "Breidbart" basis $\{\cos\frac{\pi}{8}|0\rangle + \sin\frac{\pi}{8}|1\rangle,\ -\sin\frac{\pi}{8}|0\rangle+\cos\frac{\pi}{8}|1\rangle\}$, which sits halfway between the two bases. The guess is correct with probability $\cos^2\frac{\pi}{8} = \frac{2+\sqrt2}{4} \approx 0.8536$. Prepare two copies of the guessed state and submit both. Per qubit, both copies pass iff the guess was right *or* the wrong-basis measurement outcomes both happen to match — the clean bound is
$$p_{\text{per qubit}} = \cos^4\tfrac{\pi}{8} \approx 0.7286 .$$
For $n=2$: $0.7286^2 \approx 0.531$.

*Attack B — optimal cloner.* Molina–Vidick–Watrous solve the SDP for the optimal $1\to 2$ counterfeiter and obtain exactly $3/4$ per qubit, beating Attack A. Since qubits are independent and verification is a product measurement, the optimum for the whole note is
$$p_{\text{success}}(n) = \left(\tfrac34\right)^{n}, \qquad p_{\text{success}}(2) = \tfrac{9}{16} = 0.5625 .$$
For $n=100$, $(3/4)^{100} \approx 3.2\times10^{-13}$ — exponentially small, hence secure.

*Why this does not extend to public keys.* Publishing enough information for a merchant to run the verification means publishing the projector $\Pi = |\$\rangle\langle\$|$, i.e. revealing $(x,\theta)$ — and then anyone mints. Replace the product state by the coset state $|A\rangle$ with $n=4$, $A = \mathrm{span}\{1100, 0011\}$, $A^\perp = A$:
$$|A\rangle = \tfrac12\big(|0000\rangle+|1100\rangle+|0011\rangle+|1111\rangle\big).$$
Verification is $\mathbb{1}_A$, then $H^{\otimes4}$, then $\mathbb{1}_{A^{\perp}}$. Given only *oracle* access to $\mathbb{1}_A,\mathbb{1}_{A^\perp}$, producing $|A\rangle^{\otimes2}$ needs $2^{\Omega(n)}$ queries. But if the oracle is published as the explicit generator matrix — or as the polynomial system $p_1 = x_1+x_2$, $p_2 = x_3+x_4$ — then $A$ is read off by linear algebra and the note is cloned in $O(n^3)$ time. The whole open problem lives in that gap: an efficiently evaluable description of $\mathbb{1}_A$ that does not reveal $A$.

*(Note: the $\\#$-free presentation above is deliberate; where counts appear, write $\\#$ inside math.)*

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*