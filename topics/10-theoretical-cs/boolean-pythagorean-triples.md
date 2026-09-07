---
id: 10-theoretical-cs/boolean-pythagorean-triples
title: "Boolean Pythagorean Triples"
topic: 10-theoretical-cs
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Boolean Pythagorean Triples

> **Topic:** Theoretical Computer Science · **ID:** `10-theoretical-cs/boolean-pythagorean-triples` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

Can the positive integers $\{1,2,\dots,n\}$ be partitioned into two parts so that neither part contains a Pythagorean triple $(a,b,c)$ with $a^2+b^2=c^2$?

Ronald Graham asked this in the 1980s and offered \$100 for a solution. The two-colour case was settled in 2016 by Heule, Kullmann and Marek: a valid colouring exists for $n=7824$ and none exists for $n=7825$. A complete resolution required (i) an explicit bipartition of $[1,7824]$ and (ii) a machine-checkable refutation showing that every one of the $2^{7825}$ colourings of $[1,7825]$ has a monochromatic triple. Both were delivered, the second as a 200 TB proof certificate.

The general question — does every $k$-colouring of $\mathbb{N}$ admit a monochromatic Pythagorean triple, i.e. is $x^2+y^2=z^2$ partition regular? — is **open for all $k\ge 3$**. The catalogued status `solved-recently` refers to $k=2$; the page tracks the open $k\ge 3$ frontier.

## 2. Mathematical Foundations

**Triples.** $T = \{(a,b,c) \in \mathbb{Z}_{>0}^3 : a<b<c,\ a^2+b^2=c^2\}$. Every element is $(a,b,c)=d\,(m^2-n^2,\,2mn,\,m^2+n^2)$ for coprime $m>n\ge 1$ of opposite parity and $d\ge 1$ (Euclid's parametrisation).

**Colouring.** A $k$-colouring is $\chi:[1,n]\to[k]$. It is *valid* if no $(a,b,c)\in T$ with $c\le n$ has $\chi(a)=\chi(b)=\chi(c)$. Define
$$
P_k \;=\; \min\{\,n : \text{no valid }k\text{-colouring of }[1,n]\text{ exists}\,\},
$$
with $P_k=\infty$ if the equation is not $k$-regular.

**Partition regularity.** $x^2+y^2=z^2$ is *partition regular* iff $P_k<\infty$ for all $k$. Rado's theorem characterises partition regularity for **linear** systems $A\mathbf{x}=\mathbf{0}$ by the columns condition (a nonempty subset of columns summing to zero, with the rest in its rational span); it says nothing here, since the equation is quadratic. Compactness (König's lemma) gives: $P_k<\infty$ iff every $k$-colouring of $\mathbb{N}$ has a monochromatic triple.

**Boolean encoding ($k=2$).** Variables $x_1,\dots,x_n$ with $x_i=1$ meaning colour "red". Each triple contributes two clauses:
$$
(x_a \vee x_b \vee x_c) \wedge (\bar{x}_a \vee \bar{x}_b \vee \bar{x}_c).
$$
For $n=7825$ there are $4{,}736$ triples, hence a 3-CNF formula $F_{7825}$ with $7{,}825$ variables and $9{,}472$ clauses. $F_n$ is satisfiable iff a valid 2-colouring of $[1,n]$ exists. The theorem is:
$$
F_{7824}\ \text{SAT},\qquad F_{7825}\ \text{UNSAT}\quad\Longrightarrow\quad P_2=7825 .
$$

**Proof system.** Refutations are certified in **DRAT** (Deletion Resolution Asymmetric Tautology). A clause $C$ has the RAT property on literal $\ell\in C$ w.r.t. $F$ if for every $D\in F$ with $\bar{\ell}\in D$, unit propagation on $F \wedge \neg(C\cup(D\setminus\{\bar\ell\}))$ derives conflict. DRAT is closed under the inference rules used by CDCL solvers with inprocessing, and a derivation of the empty clause is verifiable in time polynomial in the certificate length.

**Symmetries.** $F_n$ is invariant under swapping the two colours, and admits many "free" variables: any $i$ occurring in no triple with $c\le n$ (e.g. $i$ with no representation) can be fixed arbitrarily. Multiplicative scaling $i \mapsto di$ maps triples to triples but not $[1,n]$ to itself, so it is only a partial symmetry.

## 3. History & State of the Art (SOTA)

- **1917 / 1927 / 1933.** Schur's theorem ($x+y=z$ is partition regular), van der Waerden's theorem, and Rado's characterisation set the Ramsey-theoretic frame — all for linear equations.
- **1980s.** Graham popularised the Pythagorean-triple question and offered \$100, conjecturing partition regularity for every $k$ (see his *Integers* problem survey, 2007).
- **2010.** Cooper and Poirel studied Pythagorean partition regularity and reported computational colourings for $[1,n]$ into two parts up to $n$ in the hundreds, plus structural results on ordered triple systems.
- **2015.** Cooper and Overstreet, and independently Myers' Rutgers thesis, pushed exhaustive/heuristic searches and SAT encodings; Myers established that no valid 2-colouring exists for $n$ beyond a computationally reached threshold well under $10^4$ only after heavy search, without closing the gap.
- **2016.** Heule, Kullmann and Marek settled $k=2$: $P_2=7825$. The refutation used **cube-and-conquer** — a lookahead solver splits $F_{7825}$ into nearly $10^6$ cubes (partial assignments), each refuted by a CDCL solver. Runtime: about 2 days on 800 cores of the Stampede cluster (≈35,000 CPU hours). The DRAT certificate is ≈200 TB, compressed to 68 GB; independent verification with `drat-trim` cost ≈16,000 CPU hours. The paper won best paper at SAT 2016; the proof was widely reported as the largest ever produced.
- **2017.** The checking pipeline was hardened: verified DRAT/resolution checkers in Coq/ACL2 (Cruz-Filipe et al.; Heule–Hunt–Kaufmann–Wetzler), so the result rests on a formally verified checker rather than a hand-written C program.
- **2018.** Heule applied the same machinery to Schur number five ($S(5)=160$), a 2 PB proof — the current scale record for this method.
- **2019–2026.** No published finite bound for $k=3$. The state of the art remains: $P_2 = 7825$, $P_k$ unknown and not known finite for $k\ge3$.

## 4. Partial Results / Verified Cases

- **$k=2$: complete.** $P_2 = 7825$. A valid colouring of $[1,7824]$ is explicit and hand-checkable in seconds by a script; the impossibility at $7825$ is machine-verified twice (unverified `drat-trim`, then formally verified checkers).
- **Structure at the boundary.** $7825 = 5^2\cdot 313$; multiples of 5 are pivotal because $(3,4,5)$-type triples propagate through them. Removing a single well-chosen integer from $[1,7825]$ restores satisfiability, so the obstruction is tight, not robust.
- **$k=3$: only lower bounds.** Valid 3-colourings of $[1,n]$ have been constructed by local search for $n$ far beyond $10^5$, giving $P_3 > 10^5$ *(frontier — verify the current record; no peer-reviewed record value is established)*. No upper bound of any kind is known.
- **Restricted variants.** For the *primitive* triples only, or for triples with $c \le n$ and $a,b$ in a fixed congruence class, colourings avoiding monochromatic triples exist for all $n$ in several families — e.g. the odd integers contain no Pythagorean triple at all, since $a^2+b^2\equiv 2 \pmod 4$ is never a square.
- **Related equations settled.** $x+y=z$ (Schur, $S(5)=160$), $x+y=z$ with coefficients (Rado numbers, many computed), and $x\cdot y=z$ (multiplicative Schur) are all resolved or bounded; the mixed quadratic case is not.

## 5. Principal Obstacles

- **No density version to exploit.** The odd numbers have density $1/2$ and contain no Pythagorean triple; more generally $\{n \equiv 1 \bmod M\}$ contains none, because $a,b,c\equiv 1$ forces $1+1\equiv 1 \pmod M$. So any proof must use *all* colour classes simultaneously — the standard "one dense class suffices" reduction that drives Szemerédi-type arguments is unavailable.
- **Not translation invariant.** Fourier/density-increment methods for $x+y=2z$ rely on invariance under $x\mapsto x+t$. The Pythagorean equation is only dilation invariant, and dilation-invariant configurations are exactly the ones density arguments cannot force.
- **Rado's theorem does not extend.** There is no known columns-condition analogue for nonlinear Diophantine equations; deciding partition regularity of a general quadratic is not known to be decidable.
- **The $k=2$ proof carries no insight.** The refutation is a case split over $\sim 10^6$ cubes with no human-comprehensible core; the minimal unsatisfiable subformula still involves thousands of variables. It provides no lemma reusable for $k=3$.
- **Search space explodes.** $k=3$ multiplies the state space to $3^n$ and the encoding to $3n$ variables with $3\cdot|T|$ clauses. If $P_3$ has the same relative growth as Schur numbers ($S(4)=44 \to S(5)=160$), plausible values are $10^6$–$10^9$, well past what cube-and-conquer plus DRAT storage can reach: the certificate size would exceed exabytes.
- **Lower-bound constructions are opaque.** Good 3-colourings come from simulated annealing, not from a periodic or algebraic pattern, so there is no candidate infinite construction to prove non-regularity either.

## 6. The Gap

Proved: $P_2 = 7825$ — a *finite* statement, decidable in principle by brute force, made feasible by SAT technology. Conjectured: $P_k<\infty$ for every $k$ — an infinitary statement about $\mathbb{N}$.

The barrier is that finite verification cannot climb to a general theorem. Two crossings are conceivable:

1. **A finite certificate for $k=3$**: compute $P_3$, as was done for $S(5)$. This is an engineering-plus-theory problem (better symmetry breaking, streamlining, compressed proof formats), not a conceptual one — but current bounds put it out of reach by several orders of magnitude.
2. **A structural theorem**: an arithmetic-combinatorics argument, presumably via multiplicative structure (Euclid's parametrisation turns triples into a statement about Gaussian integers $m+ni$), showing directly that $x^2+y^2=z^2$ is partition regular. Nothing in the literature currently constrains $P_3$ from above at all — even a proof that $P_3 < \infty$ without a value would be a first.

## 7. Current Research (as of June 2026)

- **CMU (Heule's group).** Continued scaling of cube-and-conquer plus DRAT/LRAT, with recent focus on *proof compression* and on verified checkers so that petabyte-scale results remain trustworthy. Targets include Schur-like and Rado-type numbers rather than $P_3$ directly.
- **Swansea (Kullmann).** Theory of hardness measures for CNF and of "good splittings" — quantifying when cube-and-conquer beats plain CDCL, which is the limiting factor for any $k=3$ attempt.
- **Arithmetic combinatorics.** Groups working on nonlinear partition regularity (Moreira's $\{x, x+y, xy\}$ theorem, 2017; Bowen–Sabok's results on $x+y=uv$-type equations) provide the only genuinely non-computational handle on quadratic Ramsey statements *(frontier — none of these methods yet touches $x^2+y^2=z^2$)*.
- **Local-search records.** Improved 3-colouring constructions circulate as preprints and code repositories; published, refereed lower bounds for $P_3$ remain scarce *(frontier — verify any quoted record)*.

## 8. Future Work

- Compute $P_3$, or prove a conditional bound assuming a structural pattern in optimal 3-colourings.
- Find a periodic or algebraically defined 3-colouring valid for all $n$ — this would *disprove* partition regularity and is the cheapest possible refutation.
- Extract a human-readable core from $F_{7825}$: identify a small sub-hypergraph of triples whose 2-colourability fails for a stated reason, then attempt to iterate the construction for $k=3$.
- Attack via Euclid's parametrisation: colourings of $[1,n]$ pull back to colourings of coprime pairs $(m,n)$; a Ramsey statement on that lattice may be more tractable.
- Extend the verified-checker stack to handle proofs that never fit on disk (streaming/on-the-fly verification), the prerequisite for anything at $k=3$ scale.

## 9. Key References

- **[Foundational]** R. Rado. *Studien zur Kombinatorik.* Mathematische Zeitschrift 36, 424–470, 1933.
- **[Foundational]** I. Schur. *Über die Kongruenz $x^m+y^m\equiv z^m \pmod p$.* Jahresbericht der DMV 25, 114–117, 1917.
- **[Foundational]** R. L. Graham. *Some of my favorite problems in Ramsey theory.* INTEGERS: Electronic Journal of Combinatorial Number Theory 7(2), \#A15, 2007.
- **[SOTA]** M. J. H. Heule, O. Kullmann, V. W. Marek. *Solving and Verifying the Boolean Pythagorean Triples Problem via Cube-and-Conquer.* SAT 2016, LNCS 9710, Springer, 228–245, 2016. arXiv:1605.00723.
- **[Survey]** M. J. H. Heule, O. Kullmann. *The Science of Brute Force.* Communications of the ACM 60(8), 70–79, 2017.
- **[Method]** M. J. H. Heule, O. Kullmann, S. Wieringa, A. Biere. *Cube and Conquer: Guiding CDCL SAT Solvers by Lookaheads.* HVC 2011, LNCS 7261, Springer, 50–65, 2012.
- **[Verification]** L. Cruz-Filipe, M. J. H. Heule, W. A. Hunt Jr., M. Kaufmann, P. Schneider-Kamp. *Efficient Certified RAT Verification.* CADE-26, LNCS 10395, Springer, 220–236, 2017.
- **[Verification]** L. Cruz-Filipe, J. Marques-Silva, P. Schneider-Kamp. *Efficient Certified Resolution Proof Checking.* TACAS 2017, LNCS 10205, Springer, 118–135, 2017.
- **[Scaling]** M. J. H. Heule. *Schur Number Five.* AAAI-18, 6598–6606, 2018.
- **[Related]** J. Cooper, C. Poirel. *Pythagorean Partition-Regularity and Ordered Triple Systems with the Sum Property.* arXiv preprint, 2010.
- **[Related]** J. Moreira. *Monochromatic sums and products in $\mathbb{N}$.* Annals of Mathematics 185(3), 1069–1090, 2017.

## 10. Worked Example / Concrete Special Case

**Instance: $n=25$.** Triples with $c\le 25$:
$$(3,4,5),\ (6,8,10),\ (5,12,13),\ (9,12,15),\ (8,15,17),\ (12,16,20),\ (7,24,25),\ (15,20,25).$$
Eight triples, so $F_{25}$ has 25 variables and 16 clauses.

**A valid 2-colouring.** Put $R=\{3,5,6,7,9,10,12,17,20,24\}$ red and everything else blue. Check each triple:

| triple | colours | monochromatic? |
|---|---|---|
| $(3,4,5)$ | R, B, R | no |
| $(6,8,10)$ | R, B, R | no |
| $(5,12,13)$ | R, R, B | no |
| $(9,12,15)$ | R, R, B | no |
| $(8,15,17)$ | B, B, R | no |
| $(12,16,20)$ | R, B, R | no |
| $(7,24,25)$ | R, R, B | no |
| $(15,20,25)$ | B, R, B | no |

So $F_{25}$ is satisfiable, and $P_2 > 25$.

**How propagation forces structure.** Suppose $\chi(3)=\chi(4)=$ red is attempted. Clause $(\bar x_3\vee\bar x_4\vee\bar x_5)$ immediately forces $5$ blue. Then $(5,12,13)$ with $5$ blue leaves the clause $(x_5\vee x_{12}\vee x_{13})$ satisfied but $(\bar x_5\vee\bar x_{12}\vee\bar x_{13})$ free — no unit propagation. This is exactly the behaviour that makes the problem hard: at $n=7825$ almost every decision propagates only one or two steps, so the search tree does not collapse and the solver must enumerate $\sim 10^6$ cubes.

**Scaling to the real instance.** Repeating this by hand is hopeless: $F_{7825}$ has $2^{7825}\approx 10^{2355}$ assignments, versus $\approx 10^{80}$ atoms in the observable universe. Cube-and-conquer replaces enumeration by a lookahead split into $\sim 10^6$ subproblems, each closed by CDCL in seconds to minutes, with every inference logged as a DRAT line. The concatenated log is the 200 TB certificate; checking it is a linear scan verifying that each added clause has the RAT property, and the final line is the empty clause — hence no colouring survives, and $P_2 = 7825$.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*