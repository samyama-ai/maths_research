---
id: 02-algebra-group-theory/linnells-conjecture
title: "Linnell's Conjecture"
topic: 02-algebra-group-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Linnell's Conjecture

> **Topic:** Algebra & Group Theory · **ID:** `02-algebra-group-theory/linnells-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Let $G$ be a discrete group whose finite subgroups have bounded order, and write
$$\operatorname{lcm}(G)=\operatorname{lcm}\{\,|H| : H\le G,\ |H|<\infty\,\}<\infty .$$

**Linnell's Conjecture (division-closure form).** The division closure $\mathcal{D}(G)$ of $\mathbb{C}G$ inside the algebra $\mathcal{U}(G)$ of operators affiliated to the group von Neumann algebra $\mathcal{N}(G)$ is semisimple Artinian. In particular, if $G$ is **torsion-free**, $\mathcal{D}(G)$ is a **division ring**.

**Equivalent analytic form (strong Atiyah conjecture).** For every $A\in M_{m\times n}(\overline{\mathbb{Q}}G)$, the von Neumann dimension of the kernel of right multiplication $r_A:\ell^2(G)^m\to\ell^2(G)^n$ satisfies
$$\dim_{\mathcal{N}(G)}\ker(r_A)\ \in\ \tfrac{1}{\operatorname{lcm}(G)}\,\mathbb{Z}.$$

A complete solution is either a proof for all such $G$, or a single group $G$ with $\operatorname{lcm}(G)<\infty$ and a matrix $A$ over $\overline{\mathbb{Q}}G$ whose kernel dimension has denominator not dividing $\operatorname{lcm}(G)$. The torsion-free case ($\operatorname{lcm}(G)=1$, kernel dimensions are integers) implies **Kaplansky's zero-divisor conjecture**: $\mathbb{C}G$ has no zero divisors. The hypothesis $\operatorname{lcm}(G)<\infty$ is essential — without it the statement is false (§3).

## 2. Mathematical Foundations

**Group von Neumann algebra.** $G$ acts on $\ell^2(G)$ by left and right translation. Set $\mathcal{N}(G)=\mathcal{B}(\ell^2(G))^{G}$, the commutant of the left regular representation; equivalently the weak closure of $\mathbb{C}G$ acting by right convolution. It carries the faithful normal trace
$$\operatorname{tr}_{\mathcal{N}(G)}(a)=\langle a\,\delta_e,\ \delta_e\rangle .$$

**Von Neumann dimension.** For a $G$-invariant closed subspace $V\subseteq\ell^2(G)^m$ with orthogonal projection $p_V\in M_m(\mathcal{N}(G))$,
$$\dim_{\mathcal{N}(G)}V=\sum_{i=1}^m \operatorname{tr}_{\mathcal{N}(G)}\big((p_V)_{ii}\big)\in[0,m],$$
a real-valued, additive, continuous dimension. $L^2$-Betti numbers of a $G$-CW complex $X$ are $b_k^{(2)}(X;\mathcal{N}(G))=\dim_{\mathcal{N}(G)}\mathcal{H}_k^{(2)}(X)$; for a cocompact free action they are exactly kernel dimensions of matrices over $\mathbb{Z}G$.

**Affiliated operators and division closure.** $\mathcal{U}(G)$ is the ring of closed densely defined operators affiliated to $\mathcal{N}(G)$; it is the Ore localization of $\mathcal{N}(G)$ at its non-zero-divisors and is von Neumann regular. The **division closure** $\mathcal{D}(G)\subseteq\mathcal{U}(G)$ is the smallest subring containing $\mathbb{C}G$ that is closed under inversion of its own units in $\mathcal{U}(G)$.

**Spectral reformulation.** For $a\in\mathbb{C}G$ let $E_{a^*a}$ be the spectral measure of the positive operator $a^*a$. Then
$$\dim_{\mathcal{N}(G)}\ker(r_a)=\operatorname{tr}_{\mathcal{N}(G)}\big(E_{a^*a}(\{0\})\big),$$
so the conjecture asserts that the **atom of the spectral measure at $0$** has trace in $\tfrac{1}{\operatorname{lcm}(G)}\mathbb{Z}$.

**Why the denominator.** If $H\le G$ is finite of order $h$, the idempotent $e_H=\tfrac1h\sum_{g\in H}g\in\mathbb{Q}G$ has $\operatorname{tr}(e_H)=1/h$, and $\ker(r_{1-e_H})$ has dimension $1/h$. So $\tfrac{1}{\operatorname{lcm}(G)}\mathbb{Z}$ is the smallest group of values compatible with the finite subgroups of $G$.

**Algebraic link.** If $\mathcal{D}(G)$ is a division ring then, $\mathcal{D}(G)$ being flat over $\mathbb{C}G$ and dimension being multiplicative, every kernel dimension is an integer; conversely integrality forces the division-closure statement (Linnell 1993; Lück 2002, Ch. 10). For torsion-free $G$, an embedding $\mathbb{C}G\hookrightarrow\mathcal{D}(G)$ into a division ring immediately kills zero divisors.

## 3. History & State of the Art

- **1976.** Atiyah asks, in *Elliptic operators, discrete groups and von Neumann algebras* (Astérisque 32–33), whether $L^2$-Betti numbers of cocompact free actions are rational. The "strong" integrality refinement grew out of this question.
- **1974.** Lewin proves $\mathbb{C}F$ for $F$ free embeds in a division ring, using Cohn's theory of free ideal rings (firs) — the seed of every later proof.
- **1993.** **Linnell**, *Division rings and group von Neumann algebras* (Forum Math. 5), proves the conjecture for the class $\mathcal{C}$: the smallest class containing free groups, closed under directed unions and under extensions with elementary amenable quotient, assuming bounded torsion. This is the paper in which the division-ring statement is isolated as a conjecture.
- **2000.** Grigorchuk–Linnell–Schick–Żuk and Grigorchuk–Żuk compute the spectrum of the lamplighter $\mathbb{Z}/2\wr\mathbb{Z}$, producing kernel dimension $1/3$ in a group whose finite subgroups are $2$-groups. This refutes the strong Atiyah statement **without** the bounded-torsion hypothesis.
- **2013–2015.** Austin produces irrational kernel dimensions; Grabowski (Invent. Math. 198) encodes Turing machines into group ring operators and realizes arbitrary computable numbers; Pichot–Schick–Żuk build closed manifolds with transcendental $L^2$-Betti numbers. Atiyah's original rationality question is definitively answered *no*.
- **2007–2021.** Linnell–Schick handle finite extensions; Linnell–Okun–Schick settle RAAGs and right-angled Coxeter groups; Jaikin-Zapirain and Jaikin-Zapirain–López-Álvarez reduce large parts of the problem to the existence and universality of **Hughes-free** division rings of fractions, settling all torsion-free one-relator groups.

**Status:** open, and now viewed as *the* remaining case — bounded torsion — after the unbounded-torsion version was demolished.

## 4. Partial Results / Verified Cases

Proved for:

- **Free groups** $F_n$, $n\le\infty$ (Lewin 1974; Linnell 1993). $\mathcal{D}(F_n)$ is the universal field of fractions of the fir $\mathbb{C}F_n$.
- **Elementary amenable groups with $\operatorname{lcm}(G)<\infty$** (Linnell 1993) — includes all virtually abelian, virtually polycyclic, and virtually solvable groups of bounded torsion.
- **Linnell's class $\mathcal{C}$** with bounded torsion: free-by-elementary-amenable and iterated directed unions thereof. Contains pure braid groups $P_n$ (iterated free-by-free semidirect with free quotients handled by extension arguments) and all free-by-cyclic groups.
- **Schick's enlargement $\mathcal{D}$** (Math. Ann. 317, 2000): closure under direct/inverse limits, amalgamated free products over the trivial group, and residually-$\mathcal{C}$ approximation.
- **Right-angled Artin and right-angled Coxeter groups** (Linnell–Okun–Schick, Geom. Dedicata 158, 2012) — here $\operatorname{lcm}$ is the lcm of orders of finite special subgroups.
- **Fundamental groups of compact $3$-manifolds.** By Agol's virtual fibering theorem, closed hyperbolic $3$-manifold groups are virtually free-by-cyclic, hence virtually in $\mathcal{C}$; Linnell–Schick (JAMS 20, 2007) transfer along the finite extension.
- **Torsion-free one-relator groups** (Jaikin-Zapirain–López-Álvarez, Math. Ann. 376, 2020): $\mathbb{Q}G$ embeds in a Hughes-free division ring, and the strong Atiyah conjecture holds.
- **Approximation transfer** (Dodziuk–Linnell–Mathai–Schick–Yates, CPAM 56, 2003): if $G$ is residually a group in a class satisfying the conjecture, with a uniform torsion bound, $G$ satisfies it.

Known **false** without the torsion bound: $\mathbb{Z}/2\wr\mathbb{Z}$ (value $1/3$), Grabowski's groups $(\mathbb{Z}/p)^{(\mathbb{Z})}\rtimes\Gamma$ (any computable value in $[0,1]$).

## 5. Principal Obstacles

- **The only genuine input is Cohn–Lewin fir theory.** Every proof ultimately rests on $\mathbb{C}F$ being a free ideal ring with a universal field of fractions. For a general torsion-free group $\mathbb{C}G$ is not a fir, has no known Sylvester matrix rank function of algebraic origin, and no substitute is available.
- **Closure operations are exhausted.** Linnell's class is generated by extension-with-elementary-amenable-quotient and directed unions. Groups with property (T) or with no normal subgroup structure — torsion-free congruence subgroups of $SL_3(\mathbb{Z})$, Thompson's group $F$, generic hyperbolic groups — lie outside every known closure and admit no induction.
- **Von Neumann dimension is analytically soft.** $\dim_{\mathcal{N}(G)}$ is continuous, not quantized by anything intrinsic; there is no integrality theorem (no index theorem, no $K$-theoretic positivity) forcing the atom at $0$ to be an integer. Standard tools — Fourier analysis on abelian groups, Ore localization on amenable groups, perturbation of the spectrum — all fail precisely because $\mathbb{C}G$ is noncommutative and non-Noetherian for nonelementary $G$.
- **Hard counterexamples in the neighbouring regime.** Grabowski's Turing-machine constructions show that arbitrary computable reals occur once torsion is unbounded. Any proof must therefore *use* the torsion bound in an essential, non-formal way — no soft functional-analytic argument can work.
- **The algebra is genuinely delicate.** Gardam's 2021 disproof of Kaplansky's unit conjecture over $\mathbb{F}_2$ for the Promislow group (a torsion-free crystallographic group) shows that structural intuition about torsion-free group rings can be wrong.
- **Base change.** Passing between $\mathbb{Q}$, $\overline{\mathbb{Q}}$, $\mathbb{C}$ and positive characteristic is nontrivial; Jaikin-Zapirain (GAFA 29, 2019) settled parts of it, but the characteristic-$p$ analogue remains a separate open problem.

## 6. The Gap

Proven: groups assembled from **free** and **elementary amenable** pieces by extensions, directed unions and finite-index passage, plus one-relator and right-angled families — all cases where a Hughes-free or fir-theoretic division ring of fractions can be constructed by hand.

Conjectured: **all** groups with $\operatorname{lcm}(G)<\infty$.

The exact missing step: given an arbitrary torsion-free $G$, construct a division ring $D$ with $\mathbb{C}G\hookrightarrow D\subseteq\mathcal{U}(G)$, or equivalently show that the Sylvester matrix rank function on $M(\mathbb{C}G)$ induced by $\dim_{\mathcal{N}(G)}$ takes only integer values. For **locally indicable** $G$ this reduces (Jaikin-Zapirain, Selecta Math. 27, 2021) to the existence of a Hughes-free division $\mathbb{Q}G$-ring, which is itself open. For groups that are not locally indicable — e.g. torsion-free hyperbolic groups with property (T) — even the reduction is unavailable.

## 7. Current Research (as of June 2026)

- **Hughes-free programme (Madrid; Jaikin-Zapirain and collaborators).** Uniqueness/universality of Hughes-free division rings is settled; the drive is existence for all locally indicable groups, which would give the conjecture for that class. Existence is known for free-by-cyclic, one-relator, and locally indicable groups that are residually (torsion-free amenable).
- **Sylvester rank functions and approximation (Bonn/Madrid/Warwick).** Continuity of rank functions under Lück approximation, positive-characteristic analogues, and $\ell^2$-torsion; Kielak's RFRS/agrarian techniques provide a second route to division rings via Malcev–Neumann series over ordered groups. *(frontier — verify current scope)*
- **Agrarian invariants.** Henneke–Kielak and successors formalize embeddings $\mathbb{Z}G\hookrightarrow D$ as "agrarian maps"; the aim is to derive integrality from existence of *any* such $D$ compatible with the trace. *(frontier — verify)*
- **Sofic/hyperlinear angle.** Elek–Szabó-style arguments and Lück approximation over sofic approximations, seeking uniform spectral gap estimates that would force atom quantization.
- **Computational spectral work.** High-precision numerical spectral measures for hyperbolic and Coxeter-type groups, used to search for a bounded-torsion counterexample; no candidate has emerged.

## 8. Future Work

- Prove existence of Hughes-free division rings of fractions for all locally indicable groups — this is the single highest-value target, explicitly proposed by Jaikin-Zapirain.
- Extend Linnell's class by a new closure operation: amalgamated products and HNN extensions over infinite subgroups, which currently break the induction.
- Settle a decisive test case: a torsion-free cocompact lattice in $SL_3(\mathbb{R})$, or Thompson's group $F$.
- Develop a genuine index-theoretic mechanism forcing integrality — an analogue of the Atiyah–Singer $L^2$-index theorem valid for non-elliptic group-ring operators.
- Resolve the positive-characteristic version, where $\mathcal{U}(G)$ has no analytic substitute and only rank functions are available.
- Look for a counterexample using Grabowski-style encodings constrained to bounded torsion; understanding *why* this fails would itself be a proof strategy.

## 9. Key References

- **[Foundational]** P. A. Linnell. *Division rings and group von Neumann algebras.* Forum Mathematicum **5** (1993), 561–576.
- **[Foundational]** M. F. Atiyah. *Elliptic operators, discrete groups and von Neumann algebras.* Astérisque **32–33** (1976), 43–72.
- **[Foundational]** J. Lewin. *Fields of fractions for group algebras of free groups.* Transactions of the AMS **192** (1974), 339–346.
- **[Foundational]** I. Hughes. *Division rings of fractions for group rings.* Communications on Pure and Applied Mathematics **23** (1970), 181–188.
- **[Survey]** W. Lück. *$L^2$-Invariants: Theory and Applications to Geometry and K-Theory.* Ergebnisse der Mathematik 44, Springer, 2002 (Chapter 10).
- **[Survey]** A. Jaikin-Zapirain. *$L^2$-Betti numbers and their analogues in positive characteristic.* In *Groups St Andrews 2017*, LMS Lecture Note Series 455, Cambridge Univ. Press, 2019.
- **[Partial results]** T. Schick. *Integrality of $L^2$-Betti numbers.* Mathematische Annalen **317** (2000), 727–750.
- **[Partial results]** J. Dodziuk, P. Linnell, V. Mathai, T. Schick, S. Yates. *Approximating $L^2$-invariants and the Atiyah conjecture.* Comm. Pure Appl. Math. **56** (2003), 839–873.
- **[Partial results]** P. Linnell, T. Schick. *Finite group extensions and the Atiyah conjecture.* Journal of the AMS **20** (2007), 1003–1051.
- **[Partial results]** P. Linnell, B. Okun, T. Schick. *The strong Atiyah conjecture for right-angled Artin and Coxeter groups.* Geometriae Dedicata **158** (2012), 261–266.
- **[SOTA / Recent]** A. Jaikin-Zapirain, D. López-Álvarez. *The strong Atiyah and Lück approximation conjectures for one-relator groups.* Mathematische Annalen **376** (2020), 1741–1793.
- **[SOTA / Recent]** A. Jaikin-Zapirain. *The universality of Hughes-free division rings.* Selecta Mathematica **27** (2021), article 74.
- **[SOTA / Recent]** A. Jaikin-Zapirain. *The base change in the Atiyah and the Lück approximation conjectures.* Geometric and Functional Analysis **29** (2019), 464–538.
- **[Counterexamples]** Ł. Grabowski. *On Turing dynamical systems and the Atiyah problem.* Inventiones Mathematicae **198** (2014), 27–69.
- **[Counterexamples]** T. Austin. *Rational group ring elements with kernels having irrational dimension.* Proc. London Math. Soc. **107** (2013), 1424–1448.
- **[Counterexamples]** R. Grigorchuk, P. Linnell, T. Schick, A. Żuk. *On a question of Atiyah.* C. R. Acad. Sci. Paris **331** (2000), 663–668.
- **[Context]** G. Gardam. *A counterexample to the unit conjecture for group rings.* Annals of Mathematics **194** (2021), 967–979.
- **[Context]** I. Agol. *The virtual Haken conjecture.* Documenta Mathematica **18** (2013), 1045–1087.

## 10. Worked Example / Concrete Special Case

**(a) $G=\mathbb{Z}$: the conjecture holds, by Fourier analysis.**
$\mathbb{C}[\mathbb{Z}]\cong\mathbb{C}[t,t^{-1}]$, and the Fourier transform is a unitary $\ell^2(\mathbb{Z})\to L^2(S^1,\lambda)$ ($\lambda$ = normalized Haar measure) carrying right convolution by $p(t)=\sum_k c_kt^k$ to multiplication by $p(z)$. Hence
$$\dim_{\mathcal{N}(\mathbb{Z})}\ker(r_p)=\lambda\big(\{z\in S^1:p(z)=0\}\big).$$
A nonzero Laurent polynomial has finitely many roots, so the measure is $0$. Thus every nonzero $p$ is injective: $\operatorname{lcm}(\mathbb{Z})=1$ and the value $0\in\mathbb{Z}$. Concretely, for $p=2-t-t^{-1}$, $p(z)=2-2\cos\theta$ vanishes only at $\theta=0$, a single point, measure $0$. Here $\mathcal{D}(\mathbb{Z})=\mathbb{C}(t)$, a field.

**(b) $G=\mathbb{Z}\times C_2$ with $C_2=\langle s\mid s^2\rangle$: a half-integer appears, as predicted.**
$\operatorname{lcm}(G)=2$. Take $a=1-s\in\mathbb{Z}G$. Fourier transform in the $\mathbb{Z}$-direction gives $\ell^2(G)\cong L^2(S^1)\otimes\mathbb{C}[C_2]$, and $a$ acts as $1\otimes(1-s)$. On $\mathbb{C}[C_2]$, $1-s$ has kernel spanned by $1+s$, of complex dimension $1$ out of $2$. So
$$\dim_{\mathcal{N}(G)}\ker(r_a)=\lambda(S^1)\cdot\tfrac12=\tfrac12\in\tfrac12\mathbb{Z}. \checkmark$$
Equivalently $e=\tfrac12(1+s)$ is an idempotent with $\operatorname{tr}_{\mathcal{N}(G)}(e)=\tfrac12$, and $\mathcal{D}(G)\cong\mathbb{C}(t)\times\mathbb{C}(t)$ — semisimple Artinian, not a division ring, exactly as the conjecture allows for groups with torsion.

**(c) The lamplighter $\Gamma=\mathbb{Z}/2\wr\mathbb{Z}$: why bounded torsion is not optional.**
$\Gamma=\big(\bigoplus_{\mathbb{Z}}\mathbb{Z}/2\big)\rtimes\mathbb{Z}$ contains finite $2$-groups of every order $2^k$, so $\operatorname{lcm}(\Gamma)=\infty$. Grigorchuk–Żuk computed the spectral measure of the Markov operator $M$ of the standard generating set explicitly: its point spectrum is supported on $\{\cos(p\pi/q)\}$ with atom masses summing over Euler-$\varphi$ counts, and Grigorchuk–Linnell–Schick–Żuk extracted an element $a\in\mathbb{Q}\Gamma$ with
$$\dim_{\mathcal{N}(\Gamma)}\ker(r_a)=\tfrac13 .$$
Since $\tfrac13\notin\tfrac{1}{2^k}\mathbb{Z}$ for any $k$, no finite-subgroup denominator can account for it. This single computation forces the hypothesis $\operatorname{lcm}(G)<\infty$ in Section 1 and marks the exact frontier of the open problem.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*