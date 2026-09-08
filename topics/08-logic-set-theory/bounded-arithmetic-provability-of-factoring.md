---
id: 08-logic-set-theory/bounded-arithmetic-provability-of-factoring
title: "Wilkie's Problem on Models of Bounded Arithmetic and Factoring"
topic: 08-logic-set-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Wilkie's Problem on Models of Bounded Arithmetic and Factoring

> **Topic:** Mathematical Logic & Set Theory · **ID:** `08-logic-set-theory/bounded-arithmetic-provability-of-factoring` · **Status:** open

## 1. Problem Statement / Conjecture

Does a weak fragment of arithmetic prove that every integer greater than $1$ is a product of primes?

Concretely, let $\mathrm{FACT}$ be the formal sentence "for every $x > 1$ there is a finite sequence of primes whose product is $x$." The problem, attributed to A. J. Wilkie and recorded in the standard open-problem lists of the field, asks:

- **(a)** Does $I\Delta_0$ (induction for bounded formulas in the language $0,S,+,\cdot,\le$) prove $\mathrm{FACT}$?
- **(b)** Does Buss's theory $S^1_2$ — the arithmetic counterpart of polynomial-time reasoning — prove $\mathrm{FACT}$?

Equivalently, in model-theoretic form: is there a model $M \models I\Delta_0$ (or $M \models S^1_2$) and an element $a \in M$, $a > 1$, such that $a$ has **no** factorization into primes coded inside $M$? Such an $a$ is necessarily nonstandard, is divisible by primes of $M$, but the *sequence* of its prime divisors with multiplicity fails to exist as an object of $M$.

A resolution requires either (i) a proof of $\mathrm{FACT}$ inside the named theory, or (ii) a model construction producing $a$ as above. By Buss's witnessing theorem, (b) is not complexity-neutral: a positive answer for $S^1_2$ yields a **deterministic polynomial-time factoring algorithm**. The problem is therefore a formal-provability shadow of the hardness of factoring, and is open in the direction where it is not.

## 2. Mathematical Foundations

**Languages and theories.** The language of bounded arithmetic $L_2$ extends $\{0,S,+,\cdot,\le\}$ by $|x| = \lceil \log_2(x+1)\rceil$ (bit length), $\lfloor x/2 \rfloor$, and the smash function $x \\# y = 2^{|x|\cdot|y|}$. Bounded quantifiers are $\forall x \le t$, $\exists x \le t$; *sharply bounded* ones are $\forall x \le |t|$. The hierarchy $\Sigma^b_i, \Pi^b_i$ counts alternations of non-sharply-bounded quantifiers and matches the polynomial hierarchy: $\Sigma^b_i$-formulas define exactly the $\Sigma^p_i$ predicates.

$$S^i_2 = \mathrm{BASIC} + \Sigma^b_i\text{-LIND}, \qquad T^i_2 = \mathrm{BASIC} + \Sigma^b_i\text{-IND},$$

where LIND is induction up to $|a|$ and IND up to $a$. One has $S^i_2 \subseteq T^i_2 \subseteq S^{i+1}_2$. $\mathrm{PV}$ is Cook's equational theory of polynomial-time functions; $\mathrm{PV}_1$ is its first-order version, and $S^1_2$ is $\forall\Sigma^b_1$-conservative over $\mathrm{PV}_1$.

**Witnessing (Buss, 1986).** If $S^1_2 \vdash \forall x\,\exists y \le t(x)\,\varphi(x,y)$ with $\varphi \in \Sigma^b_1$, then there is a polynomial-time function $f$ with $\mathrm{PV}_1 \vdash \varphi(x,f(x))$. For $T^1_2$ the witnessing class is $\mathrm{PLS}$ (Buss–Krajíček, 1994); for $S^{i+1}_2$ it is $\mathrm{FP}^{\Sigma^p_i}[\text{wit},O(\log)]$.

**The statement.** Primality is made $\Sigma^b_1$ by Pratt certificates: $\mathrm{Pr}(p) \equiv \exists c \le p\\#p\ \mathrm{PrattCert}(c,p)$, where $c$ lists a generator $g$ of $(\mathbb{Z}/p\mathbb{Z})^\times$, the factorization $p-1 = \prod q_j^{e_j}$, and recursively certificates for each $q_j$, checked by
$$g^{p-1} \equiv 1 \pmod p \ \wedge\ \bigwedge_j g^{(p-1)/q_j} \not\equiv 1 \pmod p .$$
Then
$$\mathrm{FACT}:\quad \forall x>1\ \exists w \le x\\#x\ \Big(\mathrm{Seq}(w)\wedge \prod_{i<\mathrm{lh}(w)} (w)_i = x \wedge \forall i<\mathrm{lh}(w)\ \mathrm{Pr}\big((w)_i\big)\Big),$$
a $\forall\Sigma^b_1$ sentence. The bound $x\\#x = 2^{|x|^2}$ is exactly what is needed to code a sequence of $\le |x|$ numbers each $\le x$; its totality is the axiom $\Omega_1$. Iterated product of such a sequence is polynomial-time, so the matrix is $\Delta^b_1$ relative to the certificates.

**Related principles.** $\Delta_0\text{-PHP}$ and the dual weak pigeonhole principle $\mathrm{dWPHP}(\mathrm{PV})$: no polynomial-time $f$ maps $\{0,\dots,x\}$ onto $\{0,\dots,2x\}$. $\mathrm{PV}_1+\mathrm{dWPHP}(\mathrm{PV})$ is the standard arena for formalizing randomized polynomial-time arguments.

## 3. History & State of the Art (SOTA)

- **1971–1986.** Parikh's theorem on bounded theories; Paris–Wilkie's programme on $I\Delta_0$; Buss's thesis *Bounded Arithmetic* (1986) introduces $S^i_2/T^i_2$ and witnessing, making "which arithmetic theory proves what" a complexity question.
- **1981.** A. Woods's Manchester thesis links the $\Delta_0$-pigeonhole principle to the infinitude of primes.
- **1988.** Paris, Wilkie and Woods prove that $I\Delta_0 + \Omega_1$ (indeed $I\Delta_0 + \Delta_0\text{-WPHP}$) proves there are unboundedly many primes. Whether $I\Delta_0$ alone does is still open, and is the closest neighbour of Wilkie's factoring question.
- **1992–1994.** D'Aquino formalizes local Chebyshev-type bounds in models of $I\Delta_0$; Cornaros and Dimitracopoulos give a proof of the prime number theorem in a weak fragment above $I\Delta_0$.
- **1993–1995.** The question is listed among the open problems of the area in Clote–Krajíček's volume and in Krajíček's monograph, in both the provability and the model-theoretic phrasing.
- **1998–2007.** Krajíček–Pudlák and Cook–Krajíček show that cryptographic hardness assumptions have direct unprovability consequences for $S^1_2$ and for Extended Frege, giving *conditional* negative answers.
- **2016.** Jeřábek, *Integer factoring and modular square roots*, formalizes the classical randomized reduction between factoring and square-root extraction modulo $n$ inside $\mathrm{PV}_1 + \mathrm{dWPHP}(\mathrm{PV})$ and extracts from it that factoring lies in $\mathrm{PPA} \cap \mathrm{PPP}$ under randomized reductions. This is the strongest structural progress: it pins the provability of $\mathrm{FACT}$ to theories corresponding to parity- and counting-based $\mathrm{TFNP}$ classes.

## 4. Partial Results / Verified Cases

- **Prime divisor, not factorization.** $I\Delta_0$ proves every $x>1$ has a least divisor $d>1$ and that $d$ is prime — the $\Delta_0$ least number principle applied to "$d \mid x \wedge d>1$" suffices. So the *existence of a prime factor* is settled at the very bottom of the hierarchy; only the *sequence* is problematic.
- **Coding threshold.** $\mathrm{FACT}$ as stated needs $x\\#x$, hence is naturally posed over $I\Delta_0 + \Omega_1$ or over $S^i_2$ (whose language contains $\\#$). Over $I\Delta_0$ alone the witness may not exist for coding reasons independent of number theory.
- **Provable at level 2 of the hierarchy.** $S^2_2 \vdash \mathrm{FACT}$: apply $\Pi^b_2$-LIND (available in $S^2_2$) to $\Theta(i) \equiv \forall y \le x\,(|y| \le i \to \exists\,\text{factorization of } y)$, using $y = p\cdot y'$ with $p \ge 2$, hence $|y'| \le |y|-1$. Consistent with witnessing: factoring is in $\mathrm{FP}^{\mathrm{NP}}$ by binary search on "$\exists$ divisor in $[a,b]$".
- **Conditional negative answers.** If factoring $\notin \mathrm{FP}$, then $S^1_2 \nvdash \mathrm{FACT}$ (Buss witnessing). If factoring $\notin \mathrm{FP}^{\mathrm{PLS}}$, then $T^1_2 \nvdash \mathrm{FACT}$.
- **Upper bounds via weak theories.** Jeřábek (2016): factoring $\in \mathrm{PPA}\cap\mathrm{PPP}$; equivalently $\mathrm{FACT}$ is provable in the $\mathrm{PV}_1$-extension axiomatized by the corresponding counting principles plus $\mathrm{dWPHP}$.
- **Numerical range.** For every *standard* $n$, $\mathrm{FACT}(n)$ is a true $\Sigma^b_1$ instance verified by exhibiting the factorization; all instances up to the current general-purpose factoring frontier (RSA-250, $829$ bits, 2020) are literally witnessed. The problem is entirely about nonstandard $a$.

## 5. Principal Obstacles

- **Descent is not length induction.** The natural proof recurses $x \mapsto x/p$ for an *arbitrary* prime divisor $p$. $\Sigma^b_1$-LIND (i.e. $S^1_2$) only allows the step from $\lfloor x/2\rfloor$ to $x$, a *fixed* predecessor. Converting a general descent into induction requires the $\Pi^b_2$ statement $\Theta(i)$ above; induction for it is not available below $S^2_2$. Every attempt to lower the induction complexity produces an implicit polynomial-time algorithm — which is the point of the problem.
- **Witnessing is a hard wall.** Any $S^1_2$-proof mechanically yields a polynomial-time factoring algorithm. So a positive answer at that level is at least as hard as a breakthrough in computational number theory; a negative answer is an *unconditional* separation of a natural $\forall\Sigma^b_1$ sentence from $S^1_2$, of which none are known.
- **Pratt certificates are circular.** Making primality $\Sigma^b_1$ via certificates presupposes factoring $p-1$; making it $\Delta^b_1$ via AKS requires formalizing the AKS correctness proof (cyclotomic polynomial arithmetic, Chebyshev-type estimates) in $\mathrm{PV}_1$, which is not known to be possible.
- **No unprovability technique reaches here.** The available tools — witnessing, forcing with random variables, model-theoretic cut constructions — deliver unprovability only relative to complexity assumptions. Building a model of $S^1_2$ with an unfactorable element would give an unconditional lower bound flavour that current forcing constructions cannot produce.
- **Missing number theory below $\Omega_1$.** In $I\Delta_0$ even the infinitude of primes is open, so the number-theoretic infrastructure (Chebyshev bounds, counting arguments) needed for a syntactic proof is absent.

## 6. The Gap

Proven: $I\Delta_0 \vdash$ "every $x>1$ has a prime divisor"; $S^2_2 \vdash \mathrm{FACT}$; $\mathrm{PV}_1+\mathrm{dWPHP}+\text{counting} \vdash \mathrm{FACT}$ in Jeřábek's sense. Unresolved: everything strictly between — $\mathrm{PV}_1$, $S^1_2$, $T^1_2$, $S^2_2$'s lower cousins, and $I\Delta_0$ without $\Omega_1$.

The precise barrier is the **quantifier complexity of the induction formula**. One must either (i) replace $\Pi^b_2$-LIND on $\Theta(i)$ by a $\Sigma^b_1$-LIND argument — which by witnessing *is* a polynomial-time factoring algorithm — or (ii) construct $M \models S^1_2$ and $a \in M$ with no coded factorization, which requires showing that no polynomial-time function is provably a factoring algorithm, an unconditional statement currently out of reach.

## 7. Current Research (as of June 2026)

- **Prague school** (Krajíček, Pudlák, Jeřábek, Thapen; Czech Academy of Sciences and Charles University): forcing with random variables, and the classification of $\forall\Sigma^b_1$ consequences of weak theories by $\mathrm{TFNP}$ subclasses. The factoring sentence is a benchmark in this classification.
- **TFNP–proof-complexity correspondence** (Göös, Kamath, Robere, Sokolov and collaborators; Buss and students at UCSD): each $\mathrm{TFNP}$ subclass is matched to a proof system, so locating factoring precisely inside $\mathrm{PPA}\cap\mathrm{PPP}$ localizes which theory proves $\mathrm{FACT}$. *(frontier — verify)*
- **Warsaw group** (Kołodziejczyk, Nguyen and collaborators): conservativity and model-theoretic separations for $S^i_2/T^i_2$, plus the formalization strength of elementary number theory in $I\Delta_0+\Omega_1$.
- **Meta-complexity and unprovability** (Oliveira, Santhanam, Li): unprovability of complexity lower bounds in bounded arithmetic; the same technology is being probed for unprovability of algorithmic *upper* bounds such as $\mathrm{FACT}$. *(frontier — verify)*
- **Formalizing AKS.** Ongoing effort to show $\mathrm{PV}_1$ or $S^1_2 + \mathrm{dWPHP}$ proves the AKS primality criterion correct, which would remove the Pratt-certificate circularity. *(frontier — verify)*

## 8. Future Work

- Determine whether $\mathrm{PV}_1 + \mathrm{dWPHP}(\mathrm{PV})$ alone proves $\mathrm{FACT}$, sharpening Jeřábek's $\mathrm{PPA}\cap\mathrm{PPP}$ placement to a single principle.
- Settle the intermediate levels: is $\mathrm{FACT}$ provable in $T^1_2$? A positive answer would put factoring in $\mathrm{FP}^{\mathrm{PLS}}$, a notable complexity consequence.
- Resolve the $I\Delta_0$ companion problem — infinitude of primes without $\Omega_1$ — as a proving ground for the coding-free techniques the factoring question needs.
- Build models of $\mathrm{PV}_1$ with elements lacking coded factorizations, even under strong cryptographic hypotheses, to map what such models must look like.
- Formalize AKS, or find a $\Delta^b_1$ primality predicate with a $\mathrm{PV}_1$-provable correctness proof.

## 9. Key References

- **[Foundational]** S. R. Buss. *Bounded Arithmetic.* Bibliopolis, Naples, 1986.
- **[Foundational]** J. B. Paris, A. J. Wilkie, A. R. Woods. *Provability of the pigeonhole principle and the existence of infinitely many primes.* The Journal of Symbolic Logic, 53(4):1235–1244, 1988.
- **[Foundational]** A. R. Woods. *Some problems in logic and number theory, and their connections.* PhD thesis, University of Manchester, 1981.
- **[Monograph]** J. Krajíček. *Bounded Arithmetic, Propositional Logic, and Complexity Theory.* Cambridge University Press, 1995.
- **[Monograph]** J. Krajíček. *Proof Complexity.* Cambridge University Press, 2019.
- **[Monograph]** S. A. Cook, P. Nguyen. *Logical Foundations of Proof Complexity.* Cambridge University Press, 2010.
- **[SOTA / Recent]** E. Jeřábek. *Integer factoring and modular square roots.* Journal of Computer and System Sciences, 82(2):380–394, 2016.
- **[SOTA]** E. Jeřábek. *Dual weak pigeonhole principle, Boolean complexity, and derandomization.* Annals of Pure and Applied Logic, 129(1–3):1–37, 2004.
- **[SOTA]** J. Krajíček, P. Pudlák. *Some consequences of cryptographical conjectures for $S^1_2$ and EF.* Information and Computation, 140(1):82–94, 1998.
- **[Related]** S. R. Buss, J. Krajíček. *An application of Boolean complexity to separation problems in bounded arithmetic.* Proceedings of the London Mathematical Society, 69(3):1–21, 1994.
- **[Related]** P. D'Aquino. *Local behaviour of Chebyshev's theorem in models of $I\Delta_0$.* The Journal of Symbolic Logic, 57(1):12–27, 1992.
- **[Related]** C. Cornaros, C. Dimitracopoulos. *The prime number theorem and fragments of PA.* Archive for Mathematical Logic, 33(4):265–281, 1994.
- **[Related]** A. Berarducci, B. Intrigila. *Combinatorial principles in elementary number theory.* Annals of Pure and Applied Logic, 55(1):35–50, 1991.
- **[Survey]** P. Clote, J. Krajíček (eds.). *Arithmetic, Proof Theory, and Computational Complexity.* Oxford University Press, 1993.
- **[Related]** M. Agrawal, N. Kayal, N. Saxena. *PRIMES is in P.* Annals of Mathematics, 160(2):781–793, 2004.

## 10. Worked Example / Concrete Special Case

Take $x = 5893$, so $|x| = 13$. The claimed witness is $w = \langle 71, 83, c_{71}, c_{83}\rangle$ with $71 \cdot 83 = 5893$.

**Verifying the certificate for $p = 71$.** The certificate supplies $g = 7$ and the factorization $70 = 2\cdot 5\cdot 7$. Compute modulo $71$: $7^2 = 49$, $7^4 = 49^2 = 2401 = 33\cdot 71 + 58 \equiv 58$, $7^8 \equiv 58^2 = 3364 = 47\cdot 71 + 27 \equiv 27$. Then
$$7^{10} \equiv 27\cdot 49 = 1323 = 18\cdot 71 + 45 \equiv 45 \ne 1,$$
$$7^{14} \equiv 27\cdot 58\cdot 49 \equiv 4\cdot 49 = 196 \equiv 54 \ne 1,$$
and $7^{35} \equiv -1$ since $\left(\tfrac{7}{71}\right) = -1$ by reciprocity ($71 \equiv 1 \bmod 7$, and $(-1)^{3\cdot 35} = -1$). Since $7^{70} \equiv 1$ and $7^{70/q} \ne 1$ for $q \in \{2,5,7\}$, the order of $7$ is exactly $70$, so $71$ is prime. Every step is a polynomial-time modular exponentiation — $\mathrm{PV}_1$ verifies the check.

**Where the theory stalls.** The certificate for $71$ needed the factorization of $70$; the certificate for $83$ needs the factorization of $82 = 2\cdot 41$, which needs one for $40 = 2^3\cdot 5$, and so on. Each recursion step reduces the bit length by at least one, so the whole object $w$ has size $O(|x|^2)$ and lives below $x\\#x$. **Existence** of $w$ is what is unproved. The descent $5893 \to 83 \to 1$ uses the divisor $71$, not $\lfloor 5893/2\rfloor = 2946$, so $\Sigma^b_1$-LIND does not apply. Formalizing the descent uniformly requires induction on
$$\Theta(i)\equiv \forall y \le x\,\big(|y|\le i \rightarrow \exists w \le x\\#x\ \mathrm{FactSeq}(w,y)\big),$$
a $\Pi^b_2$ formula — available in $S^2_2$, not in $S^1_2$. In a model $M \models S^1_2$ with a nonstandard $a$, the descent $a \to a/p_1 \to a/(p_1p_2) \to \cdots$ is a legitimate *external* sequence of length $\le |a|$, but nothing in $S^1_2$ asserts that this sequence is coded by an element of $M$. That single coding step is the whole of Wilkie's problem.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*