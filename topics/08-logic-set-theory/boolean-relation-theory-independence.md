---
id: 08-logic-set-theory/boolean-relation-theory-independence
title: "Friedman's Conjecture on Boolean Relation Theory"
topic: 08-logic-set-theory
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Friedman's Conjecture on Boolean Relation Theory

> **Topic:** Mathematical Logic & Set Theory · **ID:** `08-logic-set-theory/boolean-relation-theory-independence` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Boolean Relation Theory (BRT) is Harvey Friedman's programme for classifying, over a fixed class of functions and a fixed class of sets, **all** Boolean relations that can hold between finitely many sets and their forward images under finitely many functions. Friedman's conjecture, in the form tracked here, has two coupled parts.

**(a) The exotic proposition.** Let $\mathrm{ELG}$ be the class of functions of *expansive linear growth* on $\mathbb{N}$ and let $fA$ denote the forward image of $A^k$ under a $k$-ary $f$. Then:

> **Proposition A.** For all $f,g \in \mathrm{ELG}$ there exist infinite sets $A \subseteq B \subseteq C \subseteq \mathbb{N}$ with
> $$A \cup fA \subseteq C \cup gB, \qquad A \cup fB \subseteq C \cup gC .$$

Friedman proved that Proposition A is provable in $\mathrm{SMAH}^{+}$ but not in $\mathrm{ZFC}$ (assuming $\mathrm{SMAH}$ is consistent), where $\mathrm{SMAH} = \mathrm{ZFC} + \{$"there is a strongly $n$-Mahlo cardinal"$\}_{n<\omega}$ and $\mathrm{SMAH}^{+} = \mathrm{ZFC} + $ "for every $n$ there is a strongly $n$-Mahlo cardinal". More precisely, Proposition A is provably equivalent to $\mathrm{Con}(\mathrm{SMAH})$ over a weak base theory.

**(b) The classification conjecture (open).** The full classification of *Inclusion BRT* in the nine terms $A,B,C,fA,fB,fC,gA,gB,gC$ over the setting $(\mathrm{ELG},\mathrm{INF})$ — deciding, for every candidate Boolean relation, whether it is realizable for all $f,g \in \mathrm{ELG}$ — is conjectured to be (i) effectively decidable, and (ii) *not* decidable within $\mathrm{ZFC}$: some of its instances provably require large cardinals. A complete resolution means a proof (or refutation) that the classification is computable together with an exact calibration of the consistency strength needed to carry it out.

## 2. Mathematical Foundations

**Forward images.** For $f:\mathbb{N}^{k}\to\mathbb{N}$ and $A\subseteq\mathbb{N}$ write
$$fA \;=\; f[A^{k}] \;=\; \{ f(x_1,\dots,x_k) : x_1,\dots,x_k \in A \}.$$

**Expansive linear growth.** With $|x| = \max(x_1,\dots,x_k)$, put
$$\mathrm{ELG} = \Big\{ f:\mathbb{N}^{k}\to\mathbb{N} \;:\; \exists\, c,d>1 \ \forall^{\infty} x \in \mathbb{N}^{k}\ \ c|x| \le f(x) \le d|x| \Big\},$$
where $\forall^{\infty}$ means "for all but finitely many". $\mathrm{INF}$ is the family of infinite subsets of $\mathbb{N}$. $\mathrm{SD}$ is the class of *strictly dominating* functions: $f(x) > |x|$ for all $x$.

**A BRT setting** is a pair $(V,K)$ with $V$ a set of multivariate functions on a domain and $K$ a family of subsets. For a signature of $n$ set variables and $m$ function symbols, the $n(m+1)$ terms $A_i, f_jA_i$ generate a free Boolean algebra with $2^{\,n(m+1)}$ atoms. A **BRT statement** asserts
$$\forall f_1,\dots,f_m \in V\ \exists A_1,\dots,A_n \in K \ \big(\textstyle\bigwedge_{\alpha \in S} \alpha = \emptyset\big)$$
for a chosen set $S$ of atoms. With $n=3$, $m=2$ there are $2^{9}=512$ atoms, hence $2^{512}$ candidate statements — the raw classification target.

**Two seed theorems.**

*Thin Set Theorem (TS).* For every $f:\mathbb{N}^{k}\to\mathbb{N}$ there is an infinite $A$ with $fA \ne \mathbb{N}$. Provable in $\mathrm{ACA}_0$ by Ramsey's theorem for $k$-tuples.

*Complementation Theorem.* For every $f \in \mathrm{SD}$ of arity $k$ there is a **unique** $A \subseteq \mathbb{N}$ with
$$fA \;=\; \mathbb{N}\setminus A, \quad\text{equivalently}\quad A \cup fA = \mathbb{N} \ \wedge\ A \cap fA = \emptyset .$$

**The $\cup$-format.** Friedman restricts attention to statements
$$\forall f,g\in\mathrm{ELG}\ \exists A,B,C \in \mathrm{INF}\ \big( X_1 \cup fX_2 \subseteq X_3 \cup gX_4 \ \wedge\ X_5 \cup fX_6 \subseteq X_7 \cup gX_8 \big),\quad X_i \in \{A,B,C\},$$
giving exactly $3^{8} = 6561$ statements. This is the tractable fragment on which the programme's flagship result was obtained.

## 3. History & State of the Art (SOTA)

- **1970s–80s.** Friedman's incompleteness programme opens with finite Kruskal-type statements and the graph minor theorem (Friedman–Robertson–Seymour, 1987), giving natural combinatorial statements unprovable in $\Pi^1_1\text{-}\mathrm{CA}_0$.
- **1998.** *Finite functions and the necessary use of large cardinals* (Annals of Mathematics) delivers finite $\Pi^0_2$ statements equivalent to $\mathrm{Con}$ of $\mathrm{ZFC}$ + subtle/$n$-Mahlo-type hypotheses. This supplies the reduction machinery later reused in BRT.
- **~1998–2011.** Friedman isolates BRT as an autonomous subject, develops the Complementation and Thin Set seeds, and circulates the book manuscript *Boolean Relation Theory and Incompleteness* through drafts and the FOM mailing list.
- **SOTA.** The $6561$-statement $\cup$-format classification is complete: all but a single symmetry class are settled in weak subsystems of second-order arithmetic, and the residual class — the **Principal Exotic Case**, Proposition A — is equivalent to $\mathrm{Con}(\mathrm{SMAH})$. Reverse-mathematical study of the seed theorems (thin set, free set, rainbow Ramsey) has become an independent industry (Cholak–Giusto–Hirst–Jockusch 2005; Dorais et al. 2016; Cholak–Patey 2020). Friedman has since pivoted much of the incompleteness programme to *emulation theory*, which he presents as a cleaner successor framework.

## 4. Partial Results / Verified Cases

- **$n=1,2$ sets, one function.** Full classification for $(\mathrm{SD},\mathrm{INF})$ and $(\mathrm{ELG},\mathrm{INF})$ in $A,fA$ and $A,B,fA,fB$: finitely many cases, all decided in $\mathrm{RCA}_0$ or $\mathrm{ACA}_0$. The Complementation Theorem settles the $\mathrm{SD}$ case outright and is provable in $\mathrm{ACA}_0$.
- **The $3^8 = 6561$ $\cup$-format statements over $(\mathrm{ELG},\mathrm{INF})$.** Every one is proved or refuted, with exactly one equivalence class of **12** statements (the orbit of Proposition A under the evident symmetries) left over.
- **Proposition A itself.** Provable in $\mathrm{SMAH}^{+}$; not provable in $\mathrm{SMAH}$ (hence not in $\mathrm{ZFC}$) if $\mathrm{SMAH}$ is consistent; provably equivalent to $\mathrm{Con}(\mathrm{SMAH})$ over $\mathrm{ACA}'$. Its $\Pi^0_1$ finite-approximation forms are equivalent to $\mathrm{Con}(\mathrm{SMAH})$ over $\mathrm{EFA}$.
- **Degenerate parameter ranges.** Statements in which both consequents are $C \cup gC$ are trivially true (take $C=\mathbb{N}$); statements whose antecedents force $fA \subseteq A$ for infinite $A$ are refutable outright from $c>1$ in the $\mathrm{ELG}$ bound.
- **Seed-theorem strength.** For $k \ge 2$, $\mathrm{TS}^k$ is strictly weaker than $\mathrm{ACA}_0$ and does not imply $\mathrm{RT}^2_2$; cone-avoidance holds for all $\mathrm{TS}^k$ (Cholak–Patey).

## 5. Principal Obstacles

- **Combinatorial explosion.** The unrestricted three-set, two-function classification has $2^{512}$ candidate statements. No symmetry reduction currently brings this into computational range; the $6561$ figure was obtained only by hard-coding the $\cup$-format.
- **No uniform decision procedure.** Each residual case is settled by a bespoke argument. There is no known "master theorem" converting a Boolean relation into a normal form whose truth value is read off syntactically, so the decidability half of the conjecture has no candidate algorithm.
- **Large-cardinal proofs are non-constructive in the wrong direction.** The forward proof of Proposition A runs through a tower of strongly $n$-Mahlo cardinals and indiscernibles in a transfinite hierarchy; it yields the infinite sets $A\subseteq B\subseteq C$ only as an existence statement, giving no combinatorial control usable in neighbouring cases.
- **Ramsey-theoretic methods cap out at $\mathrm{ACA}_0$.** Every standard tool (Ramsey's theorem for $k$-tuples, Hindman-type arguments, greedy diagonal constructions) is provable in $\mathrm{ACA}_0$ or below, so by conservation none of them can prove a statement equivalent to $\mathrm{Con}(\mathrm{SMAH})$. New techniques of genuinely higher proof-theoretic strength would be required, and none are known that are natural for images $fA$.
- **Reversal is delicate.** Deriving $\mathrm{Con}(\mathrm{SMAH})$ *from* Proposition A requires coding a Mahlo-cardinal hierarchy into infinite subsets of $\mathbb{N}$ closed under $\mathrm{ELG}$ images; the coding is tightly bound to the specific inclusion pattern and does not transfer to variants.
- **Verification burden.** The main results live in a long unrefereed book manuscript. Independent checking of the $6561$-case analysis has not been completed in the literature.

## 6. The Gap

Proven: the $\cup$-format fragment ($3^8$ statements, two functions, three sets, one specific syntactic shape), plus the exact strength of its single exotic residue.

Conjectured: the same for the full Inclusion BRT of $A,B,C,fA,fB,fC,gA,gB,gC$ over $(\mathrm{ELG},\mathrm{INF})$ — $2^{512}$ statements — and, beyond that, for arbitrary BRT settings $(V,K)$.

The precise barrier is a **normal-form-plus-strength dichotomy**: one needs a theorem saying that every BRT statement in a given setting is either (i) provable in $\mathrm{ACA}_0$, (ii) refutable in $\mathrm{RCA}_0$, or (iii) equivalent to $\mathrm{Con}(T)$ for a $T$ read off effectively from the statement's syntax — together with an algorithm producing the trichotomy label. Nothing in the current proofs suggests such a trichotomy holds; the exotic case might be one of infinitely many strength levels, or the classification might itself be undecidable.

## 7. Current Research (as of June 2026)

- **Ohio State / Friedman's own programme.** Continued revision of the BRT manuscript alongside *emulation theory*, which Friedman presents as a more robust vehicle for the same $\mathrm{SMAH}$-level phenomena with far smaller classification tables. *(frontier — verify)*
- **Reverse mathematics of thin/free set theorems.** Groups around Patey (CNRS/Lyon), Dzhafarov (Connecticut), Hirschfeldt and Monin: computability-theoretic separations, cone avoidance, and Weihrauch-degree calibration of $\mathrm{TS}^k$ and $\mathrm{FS}^k$ — the BRT seeds, studied for their own sake.
- **Independent verification.** No published, refereed, third-party confirmation of the full $6561$-case classification. This remains the single largest gap between claim and community-checked result. *(frontier — verify)*
- **Formalization.** Interest in Lean/Isabelle formalization of at least the Complementation Theorem and the decidable portion of the $\cup$-format table has been voiced but no substantial artefact is public. *(frontier — verify)*

## 8. Future Work

1. **Machine-assisted classification.** Encode BRT statements over $(\mathrm{ELG},\mathrm{INF})$ as SAT/SMT instances with the known provable relations as axioms, and mechanically reduce the $2^{512}$ space modulo symmetry; report the surviving cases.
2. **Formalize the exotic case.** A proof assistant development of "Proposition A $\Rightarrow \mathrm{Con}(\mathrm{SMAH})$" would settle the verification question permanently.
3. **Search for a second strength level.** Find a BRT statement in some setting equivalent to $\mathrm{Con}$ of a theory *strictly between* $\mathrm{ZFC}$ and $\mathrm{SMAH}$, or above $\mathrm{SMAH}$. Its existence or non-existence discriminates sharply between the trichotomy and non-trichotomy pictures.
4. **New settings.** BRT over $\mathbb{Q}$, over abelian groups, or with $K$ = sets of positive upper density, to test whether the exotic phenomenon is an artefact of $(\mathrm{ELG},\mathrm{INF})$.
5. **Compare with emulation theory.** Establish a formal translation between BRT statements and emulation-theoretic propositions; a strength-preserving translation would let one classification inherit the other's results.

## 9. Key References

- **[Foundational]** Harvey M. Friedman. *Finite functions and the necessary use of large cardinals.* Annals of Mathematics, 148(3):803–893, 1998.
- **[Foundational]** Harvey M. Friedman, Neil Robertson, Paul Seymour. *The metamathematics of the graph minor theorem.* In *Logic and Combinatorics*, Contemporary Mathematics 65, American Mathematical Society, 1987, pp. 229–261.
- **[Foundational / SOTA]** Harvey M. Friedman. *Boolean Relation Theory and Incompleteness.* Book manuscript, Ohio State University; drafts circulated 2007–2011 (Association for Symbolic Logic, Lecture Notes in Logic series, announced).
- **[Survey]** Stephen G. Simpson. *Subsystems of Second Order Arithmetic.* 2nd edition, Perspectives in Logic, Cambridge University Press / ASL, 2009.
- **[Survey]** Harvey M. Friedman, Stephen G. Simpson. *Issues and problems in reverse mathematics.* In *Computability Theory and Its Applications*, Contemporary Mathematics 257, AMS, 2000, pp. 127–144.
- **[SOTA / Recent]** Peter A. Cholak, Mariagnese Giusto, Jeffry L. Hirst, Carl G. Jockusch, Jr. *Free sets and reverse mathematics.* In *Reverse Mathematics 2001*, Lecture Notes in Logic 21, ASL, 2005, pp. 104–119.
- **[SOTA / Recent]** Peter A. Cholak, Ludovic Patey. *Thin set theorems and cone avoidance.* Transactions of the American Mathematical Society, 373(4):2743–2773, 2020.
- **[SOTA / Recent]** François G. Dorais, Damir D. Dzhafarov, Jeffry L. Hirst, Joseph R. Mileti, Paul Shafer. *On uniform relationships between combinatorial problems.* Transactions of the American Mathematical Society, 368(2):1321–1359, 2016.
- **[Recent]** Harvey M. Friedman. *Concrete mathematical incompleteness: basic emulation theory.* In *Hilary Putnam on Logic and Mathematics* (G. Hellman, R. Cook, eds.), Outstanding Contributions to Logic, Springer, 2018.
- **[Background]** Akihiro Kanamori. *The Higher Infinite: Large Cardinals in Set Theory from Their Beginnings.* 2nd edition, Springer, 2003. (Mahlo and $n$-Mahlo cardinals.)

## 10. Worked Example / Concrete Special Case

**Complementation for $f(x,y) = x+y+1$.** This $f$ is strictly dominating on $\mathbb{N}=\{0,1,2,\dots\}$ since $x+y+1 > \max(x,y)$. The theorem asserts a unique $A$ with $fA = \mathbb{N}\setminus A$. Build $A$ by recursion on $n$: put $n \notin A$ iff $n \in f[(A\cap[0,n))^2]$.

| $n$ | $A\cap[0,n)$ | $f$-values available | $n \in A$? |
|---|---|---|---|
| 0 | $\emptyset$ | — | yes |
| 1 | $\{0\}$ | $1$ | no |
| 2 | $\{0\}$ | $1$ | yes |
| 3 | $\{0,2\}$ | $1,3,5$ | no |
| 4 | $\{0,2\}$ | $1,3,5$ | yes |
| 5 | $\{0,2,4\}$ | $1,3,5,7,9$ | no |
| 6 | $\{0,2,4\}$ | $1,3,5,7,9$ | yes |

So $A = 2\mathbb{N}$ and $fA = \{x+y+1 : x,y \text{ even}\} = 2\mathbb{N}+1 = \mathbb{N}\setminus A$. Both Boolean relations hold: $A\cup fA=\mathbb{N}$ and $A\cap fA=\emptyset$. Uniqueness follows because the recursion had no free choices.

**Why the exotic case is not reachable this way.** Consider the $\cup$-format instance with all four consequent slots equal to $C$:
$$A \cup fA \subseteq C \cup gC \ \wedge\ A \cup fB \subseteq C \cup gC .$$
Take $C = \mathbb{N}$ and $A=B=\mathbb{N}$: both inclusions hold trivially. Every one of the $3^4 = 81$ statements whose two consequents are $C\cup gC$ is provable in $\mathrm{RCA}_0$ by this one line.

Proposition A blocks exactly this move. Its first consequent is $C \cup gB$, so $B$ appears both as a *source* of $f$-images in the second antecedent ($fB$) and as the *only* $g$-source available in the first. Setting $C = \mathbb{N}$ does not help, because $A \cup fA \subseteq \mathbb{N} \cup gB$ is then free but the surviving constraint still couples $A$, $B$ through $\mathrm{ELG}$ growth: with $c>1$, $fB$ contains elements of size $\ge c|b|$ for $b\in B$, which must be absorbed by $C \cup gC$, and $gC$ omits a positive-density set of levels. Chasing this coupling upward through all scales is precisely what the Mahlo hierarchy is used to organize — and by conservation of $\mathrm{ACA}_0$ over $\mathrm{PA}$, no greedy or Ramsey-style construction of the kind used above can replace it.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*