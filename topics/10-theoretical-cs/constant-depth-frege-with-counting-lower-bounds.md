---
id: 10-theoretical-cs/constant-depth-frege-with-counting-lower-bounds
title: "Nullstellensatz Degree Lower Bounds for Constant-Depth Frege"
topic: 10-theoretical-cs
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Nullstellensatz Degree Lower Bounds for Constant-Depth Frege

> **Topic:** Theoretical Computer Science · **ID:** `10-theoretical-cs/constant-depth-frege-with-counting-lower-bounds` · **Status:** open

## 1. Problem Statement / Conjecture

Constant-depth Frege with counting, written $\mathrm{AC}^0[p]\text{-Frege}$, is the propositional proof system whose lines are depth-$d$ formulas over $\{\neg,\wedge,\vee,\mathrm{MOD}_p\}$ with unbounded fan-in, for a fixed prime $p$ and fixed $d$. No superpolynomial lower bound on proof size is known for this system, for **any** tautology, any $p$, and any depth $d\ge 2$ beyond the trivial cases. The central question:

> **Problem.** Exhibit an explicit family of tautologies $\{\tau_n\}$ and prove that every $\mathrm{AC}^0[p]$-Frege refutation of $\neg\tau_n$ has size $n^{\omega(1)}$.

The Nullstellensatz route makes this concrete. For an unsatisfiable system of polynomials over $\mathbb{F}_p$, let $\mathrm{NS}_{\mathbb{F}_p}(\mathcal{F})$ denote its Nullstellensatz refutation degree (Section 2). Strong degree lower bounds are known. The conjectured transfer is:

> **Conjecture (degree-to-size transfer).** There are constants $c,\varepsilon>0$ such that for every fixed $d$ and prime $p$, if a CNF family $\mathcal{F}_n$ requires $\mathrm{NS}_{\mathbb{F}_p}$ degree $\ge D(n)$, then every depth-$d$ $\mathrm{AC}^0[p]$-Frege refutation of $\mathcal{F}_n$ has size at least $\exp\!\big(D(n)^{\varepsilon/d^{\,c}}\big)$.

A complete resolution is either (i) a proof of this transfer, or of any weaker statement yielding $n^{\omega(1)}$ size bounds for an explicit family; or (ii) a polynomial-size $\mathrm{AC}^0[p]$-Frege refutation scheme for all the candidate hard families, which would be a major positive result. A conditional or relativized proof does not count: the target is unconditional and explicit.

## 2. Mathematical Foundations

**Nullstellensatz refutations.** Let $F$ be a field and $f_1,\dots,f_m \in F[x_1,\dots,x_n]$ with no common $0/1$ root. Hilbert's Nullstellensatz (with the Boolean axioms $x_i^2-x_i$) guarantees polynomials $g_i,h_i$ with

$$\sum_{i=1}^{m} g_i f_i \;+\; \sum_{j=1}^{n} h_j\,(x_j^2-x_j) \;=\; 1 .$$

The **degree** of the refutation is $\max_i \deg(g_i f_i)$, and $\mathrm{NS}_F(\mathcal{F})$ is the minimum such degree. Polynomial Calculus (PC) is the dynamic version, deriving from $\{f_i\}$ by the rules $\frac{f,\,g}{\alpha f+\beta g}$ and $\frac{f}{x_j f}$ until $1$ is derived; since a degree-$D$ NS certificate unfolds into a degree-$D$ PC derivation,

$$\mathrm{PC}\text{-}\deg_F(\mathcal{F}) \;\le\; \mathrm{NS}_F(\mathcal{F}),$$

so every PC degree lower bound is also an NS degree lower bound.

**Counting principles.** For $q\ge 2$ and $q \nmid n$, the principle $\mathrm{Count}^q_n$ asserts that $[n]$ can be partitioned into blocks of size exactly $q$. Variables $x_e$ range over $q$-subsets $e\subseteq[n]$, with axioms

$$\sum_{e \ni i} x_e = 1 \quad (i \in [n]), \qquad x_e x_{e'} = 0 \ \ (e\cap e' \neq \emptyset,\ e\neq e'), \qquad x_e^2 - x_e = 0 .$$

Counting mod $q$ makes the system unsatisfiable. Over $\mathbb{F}_p$ with $p \mid q$ the refutation is trivial (sum all vertex axioms); the interesting regime is $p \nmid q$. The pigeonhole principle $\mathrm{PHP}^{m}_{n}$ ($m>n$) is the analogous system with $x_{ij}$, $\sum_{j} x_{ij}=1$, $x_{ij}x_{i'j}=0$.

**Designs.** The lower-bound method of Buss–Impagliazzo–Krajíček–Pudlák–Razborov–Sgall assigns to each monomial $M$ of degree $<D$ a value $\mathcal{D}(M) \in F$ such that $\mathcal{D}(1)=1$ and $\mathcal{D}$ annihilates every $f_i$ times any low-degree monomial. A $D$-design is exactly a linear functional witnessing $1 \notin I_{<D}$, hence $\mathrm{NS}_F \ge D$; it is the dual (LP-duality) formulation of degree.

**Simulation direction that is known.** Impagliazzo and Segerlind proved that constant-depth Frege *augmented with counting axioms* polynomially simulates $\mathrm{NS}_{\mathbb{F}_p}$: a degree-$D$ NS refutation converts into a depth-$O(1)$ Frege proof of size $n^{O(D)}$ from $\mathrm{Count}^p$ axioms. The converse — turning degree hardness into size hardness for systems with $\mathrm{MOD}_p$ *connectives* — is what is missing.

## 3. History & State of the Art (SOTA)

- **1988–1994.** Ajtai proved superpolynomial depth-$d$ Frege lower bounds for $\mathrm{PHP}$; Pitassi–Beame–Impagliazzo and Krajíček–Pudlák–Woods independently gave the exponential form $\exp(n^{1/6^{d}})$ via switching lemmas over restrictions matched to the PHP structure.
- **1990–1994.** Ajtai showed that $\mathrm{Count}^p_n$ has no polynomial-size constant-depth Frege proofs, and that $\mathrm{Count}^q$ does not imply $\mathrm{Count}^p$ in constant depth for distinct primes.
- **1996.** Beame–Impagliazzo–Krajíček–Pitassi–Pudlák introduced Nullstellensatz as a propositional proof system with explicit degree lower bounds.
- **1996–97.** BIKPRS ("Proof complexity in algebraic systems and bounded depth Frege systems with modular counting") introduced designs and established the tight link between NS degree over $\mathbb{F}_p$ and small-depth Frege-with-counting size, obtaining unconditional size lower bounds for a *restricted* fragment (essentially depth-$2$/$3$ $\mathrm{MOD}_p$-of-$\mathrm{AND}$ lines).
- **1998–2001.** Razborov's PC degree $\ge n/2$ for $\mathrm{PHP}$; Buss–Grigoriev–Impagliazzo–Pitassi linear degree gaps for Tseitin mod distinct primes; Ben-Sasson–Impagliazzo and Alekhnovich–Razborov linear PC degree for random $k$-CNFs.
- **2016–2021.** Pitassi–Rossman–Servedio–Tan pushed depth-$d$ Frege lower bounds to polylogarithmic depth via an expander switching lemma; Håstad obtained $\exp(n^{\Omega(1/d)})$-type bounds for Tseitin on grids. All of these are for $\mathrm{AC}^0$-Frege, with no $\mathrm{MOD}_p$ connectives.
- **Status today.** Circuit complexity has had $\mathrm{AC}^0[p]$ lower bounds since Razborov–Smolensky (1987). Proof complexity has none — a 39-year gap.

## 4. Partial Results / Verified Cases

- **Degree side (fully solved for many families).** $\mathrm{NS}_{F}(\mathrm{PHP}^{n+1}_n) \ge n/2$ over every field $F$ (via Razborov's PC bound). Tseitin formulas on $n$-vertex $d$-regular expanders require PC (hence NS) degree $\Omega(n)$ over any field of characteristic $\ne 2$. Random $3$-CNFs with $\Delta n$ clauses require degree $\Omega(n)$ with probability $1-o(1)$. $\mathrm{Count}^q_n$ over $\mathbb{F}_p$ with $p\nmid q$ requires degree growing linearly in the relevant parameter, by the design construction of BIKPRS and its extension by Beame–Riis.
- **Upper bounds pinning tightness.** The induction principle has $\mathrm{NS}$ degree $\Theta(\log n)$ (Buss–Pitassi), showing $\Theta(\log n)$ is genuinely attained and that NS degree is not always large.
- **Size side, restricted depth.** BIKPRS give $\exp(n^{\Omega(1)})$ size lower bounds for constant-depth Frege systems with $\mathrm{MOD}_p$ gates when the *depth is $2$ or $3$* and the counting gates appear only at the bottom level.
- **Separations.** Impagliazzo–Segerlind ("Counting axioms do not polynomially simulate counting gates", 2001) separate $F_d(\mathrm{Count}_p)$ from $\mathrm{AC}^0[p]$-Frege, confirming that the counting-axiom results do **not** already settle the connective version.
- **Size–degree trade-offs.** de Rezende–Nordström–Risse–Sokolov (2019) give NS size-degree trade-offs from reversible pebbling, showing degree $D$ can coexist with monomial size $n^{O(1)}$ only in constrained regimes.

## 5. Principal Obstacles

- **No switching lemma for $\mathrm{MOD}_p$.** All $\mathrm{AC}^0$-Frege lower bounds run through Håstad-style switching: a random restriction collapses a depth-$d$ formula to a shallow decision tree. $\mathrm{MOD}_p$ is invariant under restrictions of this kind — parity of a random subcube is still parity — so the depth-reduction engine has no traction.
- **Razborov–Smolensky does not lift.** The circuit method approximates each gate by a low-degree $\mathbb{F}_p$-polynomial with small error, then contradicts via the degree of $\mathrm{MOD}_q$. In a *proof*, errors accumulate along $S$ lines; a union bound needs error $\ll 1/S$, which forces approximating degree $\Omega(\log S)$, and there is no known amplification that keeps the degree below the $\sqrt{n}$ threshold where the argument bites.
- **Degree is not size.** A degree-$D$ NS lower bound bounds the *ideal-membership* complexity, but $\mathrm{AC}^0[p]$-Frege lines are not low-degree polynomials: a depth-$d$ formula with $\mathrm{MOD}_p$ connectives encodes a polynomial of degree up to $n$, and no known normal form reduces its effective degree without an exponential size blow-up.
- **Feasible interpolation fails.** Krajíček-style interpolation yields lower bounds only for systems where lines have small communication complexity; $\mathrm{MOD}_p$ formulas do not, and Bonet–Pitassi–Raz-type results indicate interpolation is unavailable for Frege-strength systems under cryptographic assumptions.
- **The composite barrier is worse.** For composite $m$, even circuit lower bounds against $\mathrm{AC}^0[m]$ are open, so the proof-complexity question for $\mathrm{AC}^0[m]$-Frege has no known upstream analogue at all.

## 6. The Gap

Proven: for every explicit hard family, $\mathrm{NS}_{\mathbb{F}_p}$-degree $\ge \Omega(n)$; and $\mathrm{AC}^0[p]$-Frege-with-counting-*axioms* simulates NS, so degree bounds transfer *downward* into that weaker system. Wanted: the *upward* direction, an inequality of the shape

$$\text{size}_{\mathrm{AC}^0[p]\text{-Frege},\,d}(\mathcal{F}) \;\ge\; \exp\!\big(\mathrm{NS}_{\mathbb{F}_p}(\mathcal{F})^{\varepsilon/d^c}\big).$$

The missing step is a **restriction-plus-approximation normal form**: a random restriction procedure under which any depth-$d$ formula with $\mathrm{MOD}_p$ connectives becomes, with probability $1-o(1/S)$, a polynomial of degree $o(\mathrm{NS}_{\mathbb{F}_p}(\mathcal{F}))$ over $\mathbb{F}_p$. Applying such a normal form line-by-line to a size-$S$ refutation would turn it into a low-degree NS certificate, contradicting the design. Every known restriction either fails to reduce depth (because $\mathrm{MOD}_p$ survives) or incurs error $\Omega(1)$ per line.

## 7. Current Research (as of June 2026)

- **Algebraic proof complexity / IPS.** The Ideal Proof System of Grochow–Pitassi reframes $\mathrm{AC}^0[p]$-Frege lower bounds as algebraic-circuit lower bounds; Forbes–Shpilka–Tzameret–Wigderson and Alekseev–Grigoriev–Hirsch–Tzameret prove lower bounds for structured IPS fragments (multilinear, read-once, low-depth). Groups: Tel Aviv (Tzameret), Toronto (Pitassi), Prague (Krajíček, Pudlák).
- **Sub-systems with $\mathrm{MOD}_p$.** Lower bounds for $\mathrm{Res}(\oplus)$ and $\mathrm{Res}(\mathrm{lin})$ over $\mathbb{F}_p$ — Itsykson–Sokolov and later work — are the closest genuine progress, since these are the depth-$2$ shadow of the target. *(frontier — verify)* Extensions to tree-like $\mathrm{Res}(\mathrm{lin}_{\mathbb{F}_p})$ with polynomially many linear forms per line are the current frontier.
- **Lifting.** Göös–Pitassi–Watson-style query-to-communication lifting has converted degree/width bounds into size bounds for several systems; whether an algebraic lifting theorem exists over $\mathbb{F}_p$ that respects $\mathrm{MOD}_p$ lines is open. *(frontier — verify)*
- **Forcing and model theory.** Krajíček's forcing-with-random-variables programme aims at $\mathrm{AC}^0[p]$-Frege independence via constructions of Boolean-valued models; no unconditional lower bound has emerged.

## 8. Future Work

1. Prove any superpolynomial lower bound for *depth-$3$* $\mathrm{AC}^0[p]$-Frege with unrestricted placement of $\mathrm{MOD}_p$ — the first case beyond BIKPRS.
2. Develop a switching lemma modulo $\mathbb{F}_p$-linear algebra: restrictions that are random affine subspaces rather than random subcubes, adapted to lines containing $\mathrm{MOD}_p$.
3. Strengthen the design method to *robust* designs that tolerate $1/\mathrm{poly}$ error per line, which would make a union bound over $S$ lines viable.
4. Obtain lower bounds for constant-depth IPS over $\mathbb{F}_p$; by Grochow–Pitassi these imply $\mathrm{AC}^0[p]$-Frege bounds.
5. Settle the size complexity of $\mathrm{Count}^q_n$ in $\mathrm{AC}^0[p]$-Frege for $p \nmid q$ — the canonical candidate, with matching degree hardness already in hand.

## 9. Key References

- **[Foundational]** P. Beame, R. Impagliazzo, J. Krajíček, T. Pitassi, P. Pudlák. *Lower bounds on Hilbert's Nullstellensatz and propositional proofs.* Proceedings of the London Mathematical Society, 73(3):1–26, 1996.
- **[Foundational]** S. Buss, R. Impagliazzo, J. Krajíček, P. Pudlák, A. Razborov, J. Sgall. *Proof complexity in algebraic systems and bounded depth Frege systems with modular counting.* Computational Complexity, 6(3):256–298, 1996/97.
- **[Foundational]** M. Ajtai. *The complexity of the pigeonhole principle.* Combinatorica, 14(4):417–433, 1994.
- **[Foundational]** T. Pitassi, P. Beame, R. Impagliazzo. *Exponential lower bounds for the pigeonhole principle.* Computational Complexity, 3:97–140, 1993.
- **[SOTA / Recent]** A. Razborov. *Lower bounds for the polynomial calculus.* Computational Complexity, 7(4):291–324, 1998.
- **[SOTA / Recent]** R. Impagliazzo, N. Segerlind. *Counting axioms do not polynomially simulate counting gates.* FOCS 2001, 200–209.
- **[SOTA / Recent]** R. Impagliazzo, N. Segerlind. *Constant-depth Frege systems with counting axioms polynomially simulate Nullstellensatz refutations.* ACM Transactions on Computational Logic, 2006.
- **[SOTA / Recent]** S. Buss, D. Grigoriev, R. Impagliazzo, T. Pitassi. *Linear gaps between degrees for the polynomial calculus modulo distinct primes.* Journal of Computer and System Sciences, 62(2):267–289, 2001.
- **[SOTA / Recent]** T. Pitassi, B. Rossman, R. Servedio, L.-Y. Tan. *Poly-logarithmic Frege depth lower bounds via an expander switching lemma.* STOC 2016, 644–657.
- **[SOTA / Recent]** J. Håstad. *On small-depth Frege proofs for Tseitin for grids.* Journal of the ACM, 68(1), 2021.
- **[SOTA / Recent]** S. F. de Rezende, J. Nordström, K. Risse, D. Sokolov. *Nullstellensatz size-degree trade-offs from reversible pebbling.* CCC 2019.
- **[Survey]** T. Pitassi, I. Tzameret. *Algebraic proof complexity: progress, frontiers and challenges.* ACM SIGLOG News, 3(3):21–43, 2016.
- **[Survey]** N. Segerlind. *The complexity of propositional proofs.* Bulletin of Symbolic Logic, 13(4):417–481, 2007.
- **[Book]** J. Krajíček. *Proof Complexity.* Cambridge University Press, 2019.

## 10. Worked Example / Concrete Special Case

Take $\mathrm{Count}^2_3$: a perfect matching of $\{1,2,3\}$. Variables $x_{12},x_{13},x_{23}$; axioms

$$A_1: x_{12}+x_{13}-1,\quad A_2: x_{12}+x_{23}-1,\quad A_3: x_{13}+x_{23}-1,$$

plus $x_e^2-x_e$.

**Over $\mathbb{F}_2$ the refutation has degree $0$.** Constant multipliers $g_i=1$ give $A_1+A_2+A_3 = 2(x_{12}+x_{13}+x_{23}) - 3 = -3 = 1 \pmod 2$. This is the collapse the problem is designed to avoid: mod-$2$ counting is free in characteristic $2$.

**Over $\mathbb{F}_3$ constants fail.** Seek $c_1A_1+c_2A_2+c_3A_3 = 1$. Matching coefficients: $c_1+c_2=0$ (for $x_{12}$), $c_1+c_3=0$, $c_2+c_3=0$. Adding all three: $2(c_1+c_2+c_3)=0$, so $c_1+c_2+c_3=0$ in $\mathbb{F}_3$, and each pair-sum being $0$ forces $c_1=c_2=c_3=c$ with $2c=0$, i.e. $c=0$. Then the left side is $0\ne 1$. So $\mathrm{NS}_{\mathbb{F}_3} \ge 1$.

**A degree-$1$ refutation over $\mathbb{F}_3$.** Let $S=x_{12}+x_{13}+x_{23}$. Then $A_1+A_2+A_3 = 2S-3 = 2S$ in $\mathbb{F}_3$, so $S = 2^{-1}(A_1+A_2+A_3) = 2(A_1+A_2+A_3)$ lies in the ideal. Hence $x_{23}+1 = S - A_1 \in I$, i.e. $x_{23} \equiv -1$. Substituting into the Boolean axiom, $x_{23}^2 - x_{23} \equiv (-1)^2-(-1) = 2$, and $2$ is a unit in $\mathbb{F}_3$. Explicitly,

$$2^{-1}\Big[(x_{23}-1)\,(x_{23}^2-x_{23}) \text{-type combination}\Big] \;\Longrightarrow\; 1 \in I,$$

with all multipliers of degree $\le 1$, so $\mathrm{NS}_{\mathbb{F}_3}(\mathrm{Count}^2_3)=1$.

**Why this is the whole problem in miniature.** For general odd $n$, the design construction of BIKPRS shows the required degree grows without bound in $n$ over $\mathbb{F}_p$, $p$ odd. If the degree-to-size transfer of Section 1 held, this would immediately give $\exp(n^{\Omega(1)})$-size lower bounds for $\mathrm{AC}^0[3]$-Frege on $\mathrm{Count}^2_n$. What is missing is not the algebra — it is the reduction from a size-$S$ depth-$d$ proof with $\mathrm{MOD}_3$ connectives to a low-degree $\mathbb{F}_3$ certificate on which the design can be evaluated.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*