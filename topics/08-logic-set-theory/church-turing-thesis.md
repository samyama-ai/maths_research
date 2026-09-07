---
id: 08-logic-set-theory/church-turing-thesis
title: "Church Turing Thesis"
topic: 08-logic-set-theory
status: empirically-supported
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# The Church–Turing Thesis

> **Topic:** Mathematical Logic & Set Theory · **ID:** `08-logic-set-theory/church-turing-thesis` · **Status:** empirically-supported

## 1. Problem Statement / Conjecture

**Thesis (Church 1936, Turing 1936).** Every function on the natural numbers that is *effectively calculable* — computable by a human clerk following a finite, deterministic rule book, with unlimited time and paper but no insight — is computable by a Turing machine, equivalently is a $\lambda$-definable function, equivalently is general recursive.

The thesis is not a theorem in the ordinary sense: one side of the claimed identity, "effectively calculable", is an informal notion. Hence it is **not provable from ZFC as stated**, and the standing problem has three distinguishable forms.

- **(CT-informal)** The original thesis. Resolution would require an accepted formal analysis of "effective procedure" — an *axiomatization of computability* — from which Turing-computability is derived as a theorem. Partial answers exist (Section 4); no consensus that the problem is closed.
- **(CT-physical / Gandy's thesis)** Every function computable by a finite physical device in our universe is Turing-computable. A disproof would be a physically realizable *hypercomputer*; a proof requires a settled final physical theory, so this form is open and arguably empirical, not mathematical.
- **(CT-complexity / Extended CT)** Every physically realizable model of computation can be simulated by a probabilistic Turing machine with **polynomial** overhead. Shor's algorithm (1994) is strong evidence *against* this form; its quantum replacement (every physical device simulable in poly time by a quantum TM) is open.

Status **empirically-supported**: no counterexample in 90 years, every proposed model of effective computation has been proved Turing-equivalent, but no proof exists and none can exist absent a formalization of the informal side.

## 2. Mathematical Foundations

**Turing machines.** A deterministic TM is a tuple $M=(Q,\Gamma,\sqcup,\Sigma,\delta,q_0,F)$ with $\delta:Q\times\Gamma\rightharpoonup Q\times\Gamma\times\{L,R\}$ partial. $M$ computes $f:\mathbb{N}^k\rightharpoonup\mathbb{N}$ if started on $\bar{n}$ it halts with $f(\bar n)$ on tape when $f(\bar n)\!\downarrow$, and diverges otherwise.

**Partial recursive functions.** The least class containing the zero function $Z(n)=0$, successor $S(n)=n+1$, projections $\pi^n_i$, closed under composition, primitive recursion
$$f(\bar x,0)=g(\bar x),\qquad f(\bar x,n+1)=h(\bar x,n,f(\bar x,n)),$$
and unbounded search $f(\bar x)=\mu y\,[\,g(\bar x,y)=0\,]$.

**$\lambda$-calculus.** Terms $M::=x\mid (MN)\mid \lambda x.M$ with $\beta$-reduction $(\lambda x.M)N\to M[x:=N]$. Church numerals $\bar n=\lambda f.\lambda x.f^{n}x$; $f$ is $\lambda$-definable if some closed $F$ satisfies $F\,\bar n\twoheadrightarrow_\beta \overline{f(n)}$.

**Theorem (Church, Kleene, Turing, 1936).** The classes of partial recursive, $\lambda$-definable, and Turing-computable partial functions on $\mathbb{N}$ coincide.

**Kleene Normal Form.** There exist a primitive recursive predicate $T$ and function $U$ with
$$\varphi_e(x)\simeq U\big(\mu y\,T(e,x,y)\big),$$
so one application of $\mu$ suffices for all partial recursive functions.

**Undecidability.** The halting set $K=\{e: \varphi_e(e)\!\downarrow\}$ is computably enumerable, not computable; $\emptyset'\equiv_T K$. **Rice's theorem:** every nontrivial extensional index set is undecidable.

**Gandy machines.** Gandy (1980) formalized "discrete deterministic mechanical device" as a structure on hereditarily finite sets $\mathrm{HF}$ with a state transition $F:S\to S$ satisfying four principles: (I) states are HF-sets closed under a group of permutations; (II) a hierarchy bound $\exists\, k$ on set rank (*form of description*); (III) **local causation** — a bound $\lVert\cdot\rVert$ such that the next value at a region depends only on a bounded neighbourhood; (IV) **unique assembly**. **Gandy's Theorem:** any $F$ satisfying (I)–(IV) has Turing-computable orbits.

**Relativization.** With an oracle $A\subseteq\mathbb{N}$ one gets $\varphi^A_e$ and the Turing degrees $\mathcal{D}=(2^\omega/\equiv_T,\le_T)$, an upper semilattice with jump $\mathbf{a}\mapsto\mathbf{a}'$. Any consistent hypercomputation claim amounts to physical access to a nonzero degree, typically $\mathbf{0}'$.

## 3. History & State of the Art (SOTA)

- **1931–34.** Gödel's incompleteness paper uses a class of "recursive" functions; in Princeton lectures (1934) he defines *general recursive* functions after a suggestion of Herbrand, but explicitly declines to identify them with effective calculability.
- **1936.** Church, *An unsolvable problem of elementary number theory* (Amer. J. Math. 58), proposes the identification with $\lambda$-definability; Kleene proves $\lambda$-definable $=$ general recursive. Turing, *On computable numbers* (Proc. LMS 42), gives the machine model, the universal machine, and the analysis of a human computer — the argument Gödel called "unquestionably adequate".
- **1937.** Turing proves TM-computable $=$ $\lambda$-definable (JSL 2).
- **1943–52.** Post's problem (1944) on degrees between $\mathbf 0$ and $\mathbf 0'$; Kleene's *Introduction to Metamathematics* (1952) fixes the modern presentation and the name "Church's thesis".
- **1956–57.** Friedberg and Muchnik independently solve Post's problem by the priority method.
- **1980.** Gandy's *Church's thesis and principles for mechanisms* — the first genuine theorem in the neighbourhood of the physical thesis.
- **1985.** Deutsch introduces the universal quantum Turing machine and the "Church–Turing principle"; quantum machines compute exactly the classical computable functions.
- **1994.** Shor: integer factoring in quantum polynomial time — evidence against the *extended* thesis.
- **2000–08.** Dershowitz–Gurevich derive the thesis from Gurevich's *sequential ASM postulates* (BSL 2008): the first widely cited axiomatic proof.
- **2010s–2020s.** Analysis of analog and continuous-time models: Bournez–Graça–Pouly prove polynomial-time equivalence between the GPAC / polynomial ODEs and the classical TM (JACM 2017), closing a long-standing gap for analog computation.

## 4. Partial Results / Verified Cases

The thesis is a *theorem* for every model that has been formalized. Confirmed equivalences:

| Model | Equivalence result |
|---|---|
| $\lambda$-calculus, combinatory logic | Church–Kleene 1936; Turing 1937 |
| General recursive / $\mu$-recursive | Kleene 1936 |
| Post canonical systems, Markov algorithms, semi-Thue systems | Post 1943; Markov 1951 |
| Register / counter machines (2 counters) | Minsky 1961–67 |
| Unrestricted grammars, tag systems ($2$-tag) | Minsky 1961; Cocke–Minsky 1964 |
| Cellular automata; Rule 110 | Cook 2004 (universality of Rule 110) |
| Random-access machines, all standard programming languages | Shepherdson–Sturgis 1963 |
| Quantum Turing machines, quantum circuits | Deutsch 1985; Bernstein–Vazirani 1997 (computes exactly the c.e. sets) |
| Gandy machines (finite, local, deterministic physical mechanisms) | Gandy 1980 |
| Sequential algorithms satisfying the ASM postulates | Gurevich 2000; Dershowitz–Gurevich 2008 |
| GPAC / polynomial ODEs over $\mathbb{R}$ | Bournez–Graça–Pouly 2017, with **polynomial-time** equivalence |
| Interactive / parallel algorithms | Blass–Gurevich 2003–2008 (ASM axiomatization extended) |

Also verified: **Kolmogorov complexity is model-independent up to $O(1)$** (invariance theorem), and the class of c.e. sets is robust under all the above. Constructive/intuitionistic versions: **CT$_0$** (every function $\mathbb{N}\to\mathbb{N}$ is recursive) is consistent with HA and realizability models, and is *refuted* in classical set theory — the failure boundary is exactly the law of excluded middle.

## 5. Principal Obstacles

- **Category error at the core.** "Effectively calculable" is not a set-theoretic object. No ZFC proof can quantify over it without a prior definition, and any definition offered can be challenged as smuggling in the conclusion (Kreisel's "squeezing" concern).
- **Axiomatizations are contestable, not wrong.** The Gandy and ASM proofs are valid, but their postulates — bounded local causation, bounded state description, unique assembly, isomorphism-invariance of one step — are precisely what a skeptic denies. A device with unbounded parallelism in bounded time (Gandy's principle III violated) escapes the theorem trivially.
- **Physics is not finished.** CT-physical depends on whether spacetime admits Malament–Hogarth structures (Hogarth 1992: in some relativistic spacetimes an observer can read off the result of an infinite computation), whether measurement can extract non-computable reals, and whether physical constants are computable. General relativity and quantum field theory permit models where $\mathbf{0}'$ is accessible; whether such spacetimes are physically realizable is unresolved (Etesi–Németi 2002).
- **Idealized hypercomputers are mathematically consistent.** Infinite-time Turing machines (Hamkins–Lewis 2000) compute exactly the sets of "writable" reals, well beyond $\Delta^1_1$; real-valued neural nets with irrational weights decide all sets in polynomial time (Siegelmann–Sontag 1994). These are not counterexamples — they violate finiteness of description — but they show that no purely mathematical argument rules hypercomputation out.
- **The extended thesis has already broken once.** Shor's algorithm shows that "polynomial-time robustness" is not a safe abstraction, weakening any inductive argument from robustness alone.

## 6. The Gap

Proved: **model $\Rightarrow$ model.** Every *formal* computational model so far defined is Turing-equivalent, and every model satisfying an explicit finiteness/locality axiom set is provably so (Gandy 1980; Dershowitz–Gurevich 2008).

Unproved: **informal $\Rightarrow$ formal.** The exact missing step is a demonstration that any conceivable effective procedure satisfies the postulates. Concretely, for CT-informal one needs an axiom system $\mathcal{A}$ over "algorithm" such that (i) $\mathcal{A}$ is defensible on conceptual grounds alone, (ii) $\mathcal{A}\vdash$ Turing-computability, and (iii) $\mathcal{A}$ does not presuppose a symbol-manipulation model. Current systems satisfy (ii), arguably (i), and are disputed on (iii).

For CT-physical the gap is sharper and empirical: exhibit or exclude a finite physical process whose input–output relation is a non-computable function — i.e. decide whether $\mathrm{deg}_T(\text{Physics}) = \mathbf{0}$.

## 7. Current Research (as of June 2026)

- **Axiomatic computability.** The Dershowitz–Gurevich ASM program continues, with extensions to interactive, parallel, and effective-over-abstract-structures algorithms (Boker–Dershowitz). Debate on whether the postulates beg the question remains live in *Bulletin of Symbolic Logic* and *Philosophia Mathematica*.
- **Analog and continuous computation.** Post-Bournez–Graça–Pouly work on characterizing $\mathsf{P}$ and $\mathsf{PSPACE}$ by ODE length, giving machine-free definitions of complexity classes *(frontier — verify)*.
- **Physical Church–Turing thesis.** Ongoing work by the Németi school (Rényi Institute) on relativistic hypercomputation in Kerr/Malament–Hogarth spacetimes; Aaronson's line of argument that computational complexity constrains admissible physics.
- **Quantum advantage as evidence on ECT.** Random-circuit-sampling supremacy claims and their classical spoofing (tensor-network simulations) are the live empirical test of the quantum-extended thesis *(frontier — verify)*.
- **Reverse mathematics and constructive CT.** Strength of CT$_0$ and Markov's principle over $\mathsf{RCA}_0$ and in homotopy type theory / cubical settings, where CT is independent of univalent foundations (Swan–Uemura showed CT is consistent with cubical type theory, 2019).
- **Higher-type computability.** Kleene's S1–S9 vs. Kleene–Kreisel functionals; Longley–Normann's program on which higher-type notion is "the" right thesis at type level $\ge 2$, where the analogue of CT genuinely fails to be unique.

## 8. Future Work

- Produce an axiomatization of "effective procedure" independent of state-transition metaphors — e.g. purely in terms of information locality plus finite describability — and prove Turing-equivalence from it.
- Settle the higher-type question: identify a canonical thesis for functionals of type $\ge 2$, or prove that no canonical choice exists (a genuine *failure* of CT above type 1).
- Determine whether Malament–Hogarth spacetimes are excluded by quantum gravity; a theorem "no MH spacetime is stable under semiclassical backreaction" would substantially close CT-physical.
- Formalize the equivalence proofs in a proof assistant end to end (Turing $\leftrightarrow$ $\mu$-recursive $\leftrightarrow$ $\lambda$ is done in Isabelle/Coq; Gandy's theorem is not).
- Clarify what evidence would count against the extended thesis beyond factoring: identify a candidate physical process with conjectured super-polynomial classical simulation cost and rigorous lower bounds.

## 9. Key References

- **[Foundational]** Alonzo Church. *An Unsolvable Problem of Elementary Number Theory.* American Journal of Mathematics, 58(2):345–363, 1936.
- **[Foundational]** Alan M. Turing. *On Computable Numbers, with an Application to the Entscheidungsproblem.* Proceedings of the London Mathematical Society, s2-42:230–265, 1937 (read 1936); correction s2-43:544–546, 1938.
- **[Foundational]** Alan M. Turing. *Computability and $\lambda$-Definability.* Journal of Symbolic Logic, 2(4):153–163, 1937.
- **[Foundational]** Stephen C. Kleene. *General Recursive Functions of Natural Numbers.* Mathematische Annalen, 112:727–742, 1936.
- **[Foundational]** Stephen C. Kleene. *Introduction to Metamathematics.* North-Holland, 1952.
- **[Foundational]** Emil L. Post. *Formal Reductions of the General Combinatorial Decision Problem.* American Journal of Mathematics, 65(2):197–215, 1943.
- **[Key theorem]** Robin Gandy. *Church's Thesis and Principles for Mechanisms.* In *The Kleene Symposium*, North-Holland, 1980, pp. 123–148.
- **[SOTA]** Nachum Dershowitz and Yuri Gurevich. *A Natural Axiomatization of Computability and Proof of Church's Thesis.* Bulletin of Symbolic Logic, 14(3):299–350, 2008.
- **[SOTA]** Yuri Gurevich. *Sequential Abstract-State Machines Capture Sequential Algorithms.* ACM Transactions on Computational Logic, 1(1):77–111, 2000.
- **[SOTA]** Olivier Bournez, Daniel S. Graça, Amaury Pouly. *Polynomial Time Corresponds to Solutions of Polynomial Ordinary Differential Equations of Polynomial Length.* Journal of the ACM, 64(6):38, 2017.
- **[SOTA]** Joel D. Hamkins and Andy Lewis. *Infinite Time Turing Machines.* Journal of Symbolic Logic, 65(2):567–604, 2000.
- **[SOTA]** Peter W. Shor. *Polynomial-Time Algorithms for Prime Factorization and Discrete Logarithms on a Quantum Computer.* SIAM Journal on Computing, 26(5):1484–1509, 1997.
- **[SOTA]** David Deutsch. *Quantum Theory, the Church–Turing Principle and the Universal Quantum Computer.* Proceedings of the Royal Society of London A, 400:97–117, 1985.
- **[Survey]** Robert I. Soare. *Computability and Recursion.* Bulletin of Symbolic Logic, 2(3):284–321, 1996.
- **[Survey]** Wilfried Sieg. *Church Without Dogma: Axioms for Computability.* In *New Computational Paradigms*, Springer, 2008, pp. 139–152.
- **[Survey]** B. Jack Copeland. *The Church–Turing Thesis.* Stanford Encyclopedia of Philosophy (revised edition).
- **[Survey]** Odifreddi, Piergiorgio. *Classical Recursion Theory.* North-Holland, 1989.
- **[Book]** Robert I. Soare. *Turing Computability: Theory and Applications.* Springer, 2016.

## 10. Worked Example / Concrete Special Case

**Goal.** Exhibit the thesis in action on one function, then show where the informal step hides.

Take the predecessor-truncated subtraction $f(n)= n \dot- 1$.

**(a) As a $\mu$-recursive function.** $f(0)=Z(0)=0$; $f(n+1)=h(n,f(n))$ with $h=\pi^2_1$. So $f$ is primitive recursive by one application of the recursion scheme.

**(b) As a $\lambda$-term.** Church's predecessor:
$$P=\lambda n.\lambda f.\lambda x.\; n\,(\lambda g.\lambda h.\,h\,(g\,f))\,(\lambda u.x)\,(\lambda u.u).$$
Check $n=2$: $\bar 2 = \lambda f.\lambda x.f(fx)$, and $P\,\bar 2 \twoheadrightarrow_\beta \lambda f.\lambda x.\,fx=\bar 1$. The inner term builds a chain of $n$ "shifted" applications and discards the first, costing $O(n)$ $\beta$-steps.

**(c) As a Turing machine.** On tape alphabet $\{\sqcup,1\}$ with $n$ encoded in unary: scan right to the first $\sqcup$, move left, if the cell holds $1$ write $\sqcup$ and halt; if the cell is already $\sqcup$ (input $0$) halt unchanged. Four states, $O(n)$ steps.

All three yield the same function — an instance of the 1936–37 equivalence theorems, and the pattern that repeats for **every** model in the Section 4 table.

**Where the thesis is still needed.** Now consider the informal procedure: *"given $e$, output $1$ if $\varphi_e$ is total, else $0$."* This is a perfectly clear *description*, and by Rice-type arguments the set $\mathrm{Tot}=\{e:\varphi_e \text{ total}\}$ is $\Pi^0_2$-complete, hence not computable. The thesis is exactly what licenses the inference

> "$\mathrm{Tot}$ is not Turing-computable" $\;\Longrightarrow\;$ "no effective procedure decides totality."

Without CT, the first statement is a theorem about machines and the second is unsupported. Every undecidability result in mathematics — the halting problem, Hilbert's tenth problem (Matiyasevich 1970), the word problem for groups (Novikov 1955, Boone 1958), the unsolvability of the Entscheidungsproblem — depends on this one step. That is the practical content of the thesis and the reason its unprovability matters.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*