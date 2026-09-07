---
id: 05-analysis/six-exponentials-theorem
title: "Six Exponentials Theorem"
topic: 05-analysis
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Six Exponentials Theorem

> **Topic:** Real & Complex Analysis · **ID:** `05-analysis/six-exponentials-theorem` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

**Theorem (Six Exponentials).** Let $x_1, x_2, x_3$ be complex numbers linearly independent over $\mathbb{Q}$, and let $y_1, y_2$ be complex numbers linearly independent over $\mathbb{Q}$. Then at least one of the six numbers
$$e^{x_i y_j}, \qquad 1 \le i \le 3,\ 1 \le j \le 2$$
is transcendental.

The theorem is proved. The catalog entry tracks it because its sharp form is **open**: dropping $x_3$ gives the

**Four Exponentials Conjecture (Schneider's Problem 8).** If $x_1, x_2$ are $\mathbb{Q}$-linearly independent and $y_1, y_2$ are $\mathbb{Q}$-linearly independent, then at least one of the four numbers $e^{x_i y_j}$, $1 \le i,j \le 2$, is transcendental.

Equivalent elementary form: *if $t \in \mathbb{R}\setminus\mathbb{Q}$, then at least one of $2^t, 3^t$ is transcendental.* Six exponentials yields only the three-prime version: one of $2^t, 3^t, 5^t$ is transcendental.

A resolution means either a proof of the $2 \times 2$ statement (for all complex $x_i, y_j$, not just real ones), or a construction of $\mathbb{Q}$-linearly independent pairs $(x_1,x_2)$, $(y_1,y_2)$ with all four $e^{x_iy_j}$ algebraic — which would also refute Schanuel's conjecture.

## 2. Mathematical Foundations

Write $\overline{\mathbb{Q}}$ for the algebraic numbers, and let
$$\mathcal{L} = \exp^{-1}(\overline{\mathbb{Q}}^{\times}) = \{\lambda \in \mathbb{C} : e^{\lambda} \in \overline{\mathbb{Q}}\}$$
be the $\mathbb{Q}$-vector space of **logarithms of algebraic numbers**. Roy's enlarged space is
$$\widetilde{\mathcal{L}} = \Big\{ \beta_0 + \sum_{k=1}^{n} \beta_k \lambda_k \ :\ n \ge 0,\ \beta_k \in \overline{\mathbb{Q}},\ \lambda_k \in \mathcal{L} \Big\},$$
the $\overline{\mathbb{Q}}$-span of $\{1\} \cup \mathcal{L}$.

**Matrix reformulation.** For a $d \times \ell$ matrix $M = (x_i y_j)$ of rank $1$, the six exponentials theorem says: if $M$ has entries in $\mathcal{L}$, then $d\ell \le d + \ell$ forces structure. Concretely, a rank-one $3\times 2$ matrix cannot have all six entries in $\mathcal{L}$ unless its rows or columns are $\mathbb{Q}$-dependent. The four exponentials conjecture is the same claim for $2\times 2$, where $d\ell = 4 = d+\ell$ — the boundary case that current transcendence machinery misses.

**Strong Six Exponentials Theorem (Roy, 1992).** With $x_i, y_j$ as in §1, at least one of the six products $x_i y_j$ lies outside $\widetilde{\mathcal{L}}$. **Strong Four Exponentials Conjecture:** the same for $2\times2$; it implies the four exponentials conjecture (take $x_iy_j = \lambda_{ij} \in \mathcal{L} \subset \widetilde{\mathcal L}$).

**Schanuel's Conjecture.** If $z_1,\dots,z_n$ are $\mathbb{Q}$-linearly independent, then
$$\operatorname{trdeg}_{\mathbb{Q}} \mathbb{Q}(z_1,\dots,z_n, e^{z_1},\dots,e^{z_n}) \ge n.$$
Schanuel $\Rightarrow$ four exponentials: if all $e^{x_iy_j}\in\overline{\mathbb{Q}}$, applying Schanuel to $x_1y_1, x_1y_2, x_2y_1, x_2y_2$ (which are $\mathbb{Q}$-linearly independent when $x_iy_j$ are, by rank considerations) forces a contradiction with $\operatorname{trdeg} \le 2$.

**Underlying analytic tool — Schneider–Lang criterion.** Let $K$ be a number field, $f_1,\dots,f_N$ meromorphic functions of finite order $\rho$, at least two algebraically independent, with the ring $K[f_1,\dots,f_N]$ stable under $d/dz$. Then the set of $w \in \mathbb{C}$ at which all $f_i$ are simultaneously defined and take values in $K$ has cardinality at most $C\rho[K:\mathbb{Q}]$. Applied to $f_i(z) = e^{x_i z}$ on the lattice of points $y_1\mathbb{Z} + y_2\mathbb{Z}$, this is the engine of the proof.

## 3. History & State of the Art (SOTA)

- **1934–35.** Gelfond and Schneider independently solve Hilbert's 7th problem: $\alpha^\beta$ is transcendental for $\alpha \in \overline{\mathbb{Q}}\setminus\{0,1\}$, $\beta \in \overline{\mathbb{Q}}\setminus\mathbb{Q}$. This is the $2\times2$ case with an *algebraicity* hypothesis on the ratio $y_2/y_1$.
- **1944.** Alaoglu and Erdős, studying colossally abundant numbers, ask whether $p^t$ and $q^t$ both rational for distinct primes $p,q$ forces $t \in \mathbb{Z}$ — a four exponentials question. They note the three-prime case follows from then-unpublished work.
- **c. 1949.** Siegel possesses a proof of the six exponentials statement but does not publish it.
- **1957.** Schneider lists the four exponentials statement as the eighth of his eight open problems in *Einführung in die transzendenten Zahlen*.
- **1966 / 1968.** Lang (*Introduction to Transcendental Numbers*) and Ramachandra (*Acta Arithmetica* 14) publish independent proofs of the six exponentials theorem; Ramachandra's paper gives the sharpest contemporaneous quantitative form.
- **1981.** Waldschmidt proves the **five exponentials theorem** (*Invent. Math.* 63): for $\mathbb{Q}$-linearly independent pairs $(x_1,x_2)$, $(y_1,y_2)$ and $\gamma \in \overline{\mathbb{Q}}^\times$, at least one of
 $$e^{x_1y_1},\ e^{x_1y_2},\ e^{x_2y_1},\ e^{x_2y_2},\ e^{\gamma x_2/x_1}$$
 is transcendental. This is the closest unconditional approach to the four-exponentials statement.
- **1992.** Roy proves the strong six exponentials theorem and shows the strong four exponentials conjecture is equivalent to a purely algebraic rank conjecture on matrices with entries in $\widetilde{\mathcal{L}}$.
- **1994.** Laurent's interpolation determinants replace Siegel's lemma, giving cleaner and numerically sharper proofs.
- **2000–present.** Waldschmidt's *Diophantine Approximation on Linear Algebraic Groups* is the standard reference; the four exponentials conjecture remains open, with no improvement on the five exponentials barrier.

## 4. Partial Results / Verified Cases

Cases of the **four exponentials conjecture** that are settled:

1. **Six exponentials (three $x$'s, two $y$'s):** fully proved, all complex parameters. Equivalently: for irrational $t$, one of $2^t,3^t,5^t$ is transcendental.
2. **Gelfond–Schneider case:** $y_2/y_1 \in \overline{\mathbb{Q}}$, or $x_2/x_1 \in \overline{\mathbb{Q}}$ — proved 1934.
3. **Five exponentials:** the $2\times2$ case holds provided $e^{\gamma x_2/x_1}$ is algebraic for some $\gamma\in\overline{\mathbb{Q}}^\times$, i.e. $x_2/x_1 \in \overline{\mathbb{Q}}^{\times}\cdot\mathcal{L}$ (Waldschmidt 1981).
4. **Sharp six exponentials / strong six exponentials:** entries allowed in $\widetilde{\mathcal{L}}$ rather than $\mathcal{L}$ (Roy 1992); also quantitative versions with explicit transcendence measures $\ge \exp(-C D^{2} \log^{2} A)$ type lower bounds for $|x_iy_j - \Lambda|$.
5. **Real case with rational exponents:** for distinct primes $p,q$ and $t$ real, $p^t, q^t$ both *rational* forces $t\in\mathbb Z$ when a third prime is available; the two-prime case is still open. (Alaoglu–Erdős 1944.)
6. **Rank $\ge 3$ generalizations:** the $d\times\ell$ statement is known whenever $d\ell > d+\ell$, i.e. $(d,\ell)$ with $\min(d,\ell)\ge 2$ and $(d,\ell)\ne(2,2)$.
7. **Modular analogues:** Diaz (1997) shows the four exponentials conjecture implies, and is linked to, Bertrand's conjectures on the modular function $j$; Nesterenko's 1996 theorem on $\pi, e^\pi, \Gamma(1/4)$ supplies unconditional results in the modular setting.

## 5. Principal Obstacles

- **Counting mismatch.** All proofs build an auxiliary function $F(z) = \sum_{\text{finite}} p(\lambda) e^{\lambda z}$ vanishing to high order on a lattice, then derive a contradiction from a zero-estimate. The number of unknown coefficients grows like $S^{d}$ while the number of vanishing conditions grows like $S^{\ell}$ for parameter $S$; Siegel's lemma needs *strictly more* unknowns than conditions asymptotically, which holds exactly when $d\ell > d+\ell$. For $d=\ell=2$ the two counts balance and the method returns no contradiction.
- **No extra derivative.** The Schneider–Lang criterion trades one derivative for one degree of freedom. In the $2\times2$ case there is no third exponential $e^{x_3z}$ to supply that freedom, and differentiating $e^{x_iz}$ produces no new function.
- **Interpolation determinants do not close the gap.** Laurent's determinant method (1994) improves constants by an order of magnitude but leaves the exponent count untouched; the determinant is of size $S^2 \times S^2$ with rows and columns exhausted simultaneously.
- **No known algebraic obstruction.** Roy's reduction shows the strong four exponentials conjecture is equivalent to: every matrix with entries in $\widetilde{\mathcal{L}}$ whose "structural rank" is $\ge 2$ has rank $\ge 2$. No linear-algebra technique is known that certifies rank over $\widetilde{\mathcal L}$ without transcendence input, so the reduction moves the difficulty rather than dissolving it.
- **Schanuel is strictly harder.** The only known implication chain runs through Schanuel's conjecture, itself far out of reach (it implies algebraic independence of $e$ and $\pi$).

## 6. The Gap

Proved: the $3\times2$ statement (§1), the $2\times2$ statement under an auxiliary algebraicity hypothesis on $x_2/x_1$ (five exponentials), and the strong $3\times2$ statement over $\widetilde{\mathcal L}$.

Open: the bare $2\times2$ statement. The precise missing step is a transcendence argument valid at the **critical exponent $d\ell = d+\ell$**, where the auxiliary-function construction has zero slack. Equivalently: prove that a rank-one $2\times2$ matrix with all four entries in $\mathcal{L}$ must have $\mathbb{Q}$-proportional rows. Any method producing a nontrivial estimate at the balanced count — for instance a zero-estimate on $\mathbb{G}_m^2$ stronger by a factor $\log S$, or a $p$-adic/multiplicity gain — would close the gap.

## 7. Current Research (as of June 2026)

- **Interpolation-determinant refinements.** Continuing work in the Laurent–Mignotte–Nesterenko tradition on linear forms in two logarithms sharpens constants for effective Diophantine equations; no participant claims a route past the $2\times2$ barrier.
- **Roy's rank program.** Damien Roy (Ottawa) and collaborators pursue the matrix-rank reformulation and its links to simultaneous Diophantine approximation and the "small value" conjectures; the strong four exponentials conjecture remains the target. *(frontier — verify)*
- **Model theory and Zilber's exponential fields.** Work on pseudo-exponentiation gives Schanuel-type statements in structures satisfying Zilber's axioms, hence four-exponentials analogues there; transfer to $\mathbb{C}$ is conditional on the unproven quasiminimality/Schanuel package. *(frontier — verify)*
- **Modular and $p$-adic analogues.** Groups in Paris (Sorbonne, IMJ-PRG), Ottawa, TIFR Mumbai, and Moscow (Steklov) work on modular six-exponentials statements following Diaz and on $p$-adic versions where lattice geometry differs.
- **Periods and motivic Galois theory.** The Grothendieck period conjecture implies Schanuel-type consequences; four exponentials is being studied as a test case for motivic formulations. *(frontier — verify)*

## 8. Future Work

- Find a transcendence criterion insensitive to the $d\ell > d+\ell$ inequality — e.g. by using multiplicity estimates on $\mathbb{G}_m^2$ with derivatives in two independent directions simultaneously.
- Attack the **strong four exponentials conjecture** directly via Roy's rank criterion, seeking a purely algebraic proof over $\widetilde{\mathcal{L}}$.
- Extend the five exponentials theorem by weakening the hypothesis on $x_2/x_1$ from $\overline{\mathbb{Q}}^\times \cdot \mathcal{L}$ to $\widetilde{\mathcal L}$, or by replacing the fifth exponential with a weaker auxiliary condition — Waldschmidt's stated intermediate target.
- Settle the Alaoglu–Erdős two-prime case: does $2^t, 3^t \in \mathbb{Q}$ force $t\in\mathbb{Z}$? A proof restricted to *rational* (not merely algebraic) values might be easier.
- Develop unconditional consequences of Zilber-style exponential-field results that survive transfer to $\mathbb{C}$.

## 9. Key References

- **[Foundational]** Lang, S. *Introduction to Transcendental Numbers.* Addison-Wesley, 1966.
- **[Foundational]** Ramachandra, K. *Contributions to the theory of transcendental numbers. I, II.* Acta Arithmetica **14** (1968), 65–72, 73–88.
- **[Foundational]** Schneider, Th. *Einführung in die transzendenten Zahlen.* Springer-Verlag, 1957.
- **[Foundational]** Alaoglu, L. and Erdős, P. *On highly composite and similar numbers.* Transactions of the American Mathematical Society **56** (1944), 448–469.
- **[SOTA]** Waldschmidt, M. *Transcendance et exponentielles en plusieurs variables.* Inventiones Mathematicae **63** (1981), 97–127. (Five exponentials theorem.)
- **[SOTA]** Roy, D. *Matrices whose coefficients are linear forms in logarithms.* Journal of Number Theory **41** (1992), 22–47.
- **[SOTA]** Laurent, M. *Linear forms in two logarithms and interpolation determinants.* Acta Arithmetica **66** (1994), 181–199.
- **[SOTA]** Diaz, G. *La conjecture des quatre exponentielles et les conjectures de D. Bertrand sur la fonction modulaire.* Journal de Théorie des Nombres de Bordeaux **9** (1997), 229–245.
- **[Survey]** Waldschmidt, M. *Diophantine Approximation on Linear Algebraic Groups: Transcendence Properties of the Exponential Function in Several Variables.* Grundlehren der mathematischen Wissenschaften 326, Springer, 2000.
- **[Survey]** Waldschmidt, M. *Open Diophantine problems.* Moscow Mathematical Journal **4** (2004), no. 1, 245–305.
- **[Background]** Baker, A. *Transcendental Number Theory.* Cambridge University Press, 1975.
- **[Background]** Nesterenko, Yu. V. *Modular functions and transcendence problems.* Comptes Rendus de l'Académie des Sciences Paris, Série I, **322** (1996), 909–914.

## 10. Worked Example / Concrete Special Case

**Claim.** If $t \in \mathbb{R}$ is irrational, then at least one of $2^t, 3^t, 5^t$ is transcendental.

*Setup.* Put
$$x_1 = \log 2,\quad x_2 = \log 3,\quad x_3 = \log 5,\qquad y_1 = 1,\quad y_2 = t.$$

*Step 1 — $x_1,x_2,x_3$ are $\mathbb{Q}$-linearly independent.* Suppose $a\log 2 + b\log 3 + c\log 5 = 0$ with $a,b,c \in \mathbb{Z}$ not all zero. Exponentiating gives $2^a 3^b 5^c = 1$, contradicting unique factorization unless $a=b=c=0$.

*Step 2 — $y_1,y_2$ are $\mathbb{Q}$-linearly independent.* $a\cdot 1 + b\cdot t = 0$ with $(a,b)\ne(0,0)$ forces $t = -a/b \in \mathbb{Q}$, excluded.

*Step 3 — the six numbers.* The array $e^{x_iy_j}$ is
$$\begin{pmatrix} e^{x_1y_1} & e^{x_1y_2} \\ e^{x_2y_1} & e^{x_2y_2} \\ e^{x_3y_1} & e^{x_3y_2}\end{pmatrix} = \begin{pmatrix} 2 & 2^{t} \\ 3 & 3^{t} \\ 5 & 5^{t}\end{pmatrix}.$$
The first column is $2,3,5$ — all algebraic. By the six exponentials theorem some entry is transcendental, so it lies in the second column: one of $2^t, 3^t, 5^t$ is transcendental. $\square$

*Where the gap bites.* Drop the third row. The matrix $\begin{pmatrix} 2 & 2^{t} \\ 3 & 3^{t}\end{pmatrix}$ has $x_1=\log2$, $x_2=\log3$ $\mathbb{Q}$-independent and $y_1=1$, $y_2=t$ $\mathbb{Q}$-independent, so the four exponentials conjecture would give "one of $2^t,3^t$ transcendental." No proof is known. Note that Gelfond–Schneider does *not* apply: it needs $t$ algebraic, whereas here $t$ ranges over all irrational reals — e.g. for $t$ a Liouville number, nothing is known about $2^t$ and $3^t$ jointly beyond the three-prime statement above.

*Numerical illustration.* Take $t = \log_2 3 = 1.58496\ldots$, irrational. Then $2^t = 3$ is algebraic. Six exponentials forces one of $3^t = 3^{\log_2 3} = 5.7040\ldots$ and $5^t = 5^{\log_2 3} = 13.8390\ldots$ to be transcendental; four exponentials would already force $3^{\log_2 3}$ itself to be transcendental. Both statements are currently unprovable for this specific number by any other route.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*