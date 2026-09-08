---
id: 08-logic-set-theory/control-measure-problem
title: "Fremlin's Problem on Measure Extension and the Control Measure Problem"
topic: 08-logic-set-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Fremlin's Problem on Measure Extension and the Control Measure Problem

> **Topic:** Mathematical Logic & Set Theory · **ID:** `08-logic-set-theory/control-measure-problem` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

The **Control Measure Problem (CMP)** asks: if $\nu : \Sigma \to X$ is a countably additive vector measure on a $\sigma$-algebra $\Sigma$ with values in a complete metrizable topological vector space (an $F$-space) $X$, must there exist a finite nonnegative countably additive measure $\mu$ on $\Sigma$ — a *control measure* — with
$$\lim_{\mu(A)\to 0}\nu(A)=0 \quad\text{and}\quad \big(\mu(A)=0 \iff \nu(B)=0 \ \forall B\subseteq A,\ B\in\Sigma\big)?$$

For $X$ locally convex the answer is yes (Bartle–Dunford–Schwartz / Rybakov). Fremlin showed in *Measure Theory* vol. 3, §393 that CMP is equivalent to a purely Boolean question, **Maharam's problem**: *is every exhaustive submeasure equivalent to a countably additive measure?* — equivalently, *is every Maharam algebra a measure algebra?*

**Resolved part.** Talagrand (2008) constructed an exhaustive submeasure not equivalent to any measure. CMP therefore has a **negative** answer in ZFC.

**Open core (the surviving problem).** The cluster of measure-extension questions that Fremlin isolated around §393 remains open:

1. Is there a **pathological exhaustive** submeasure — one that dominates no nonzero finitely additive measure? *(Fremlin's problem; Talagrand's example is not known to be pathological.)*
2. Does ZFC decide whether every ccc weakly $(\sigma,\infty)$-distributive complete Boolean algebra is a Maharam algebra (von Neumann's problem in its residual form)?
3. Is there a **Maharam-type classification** of Maharam algebras, i.e. a structural invariant playing the role Maharam's 1947 homogeneity theorem plays for measure algebras?
4. Which pairs (subalgebra $\mathfrak{B}\le\mathfrak{A}$, measure $\mu$ on $\mathfrak{B}$) admit a countably additive extension to $\mathfrak{A}$, when $\mathfrak{A}$ carries only a continuous submeasure?

A complete solution to (1)–(3) means a ZFC proof or a consistency proof (forcing / large-cardinal) for each.

## 2. Mathematical Foundations

Let $\mathfrak{A}$ be a Boolean algebra. A function $\varphi:\mathfrak{A}\to[0,\infty)$ is a **submeasure** if
$$\varphi(0)=0,\qquad a\le b\Rightarrow \varphi(a)\le\varphi(b),\qquad \varphi(a\vee b)\le\varphi(a)+\varphi(b).$$

- $\varphi$ is **exhaustive** if $\lim_{n}\varphi(a_n)=0$ for every disjoint sequence $(a_n)$ in $\mathfrak{A}$.
- $\varphi$ is **uniformly exhaustive** if for every $\varepsilon>0$ there is $n$ such that no disjoint family $a_1,\dots,a_n$ has $\varphi(a_i)>\varepsilon$ for all $i$.
- $\varphi$ is a **Maharam submeasure** (continuous) if $a_n\downarrow 0 \Rightarrow \varphi(a_n)\to 0$.
- $\varphi$ is **equivalent to a measure** if there is a finitely additive $\mu\ge0$ with the same null sets and the same "small" sets; on a finite algebra this is the two-sided bound $K^{-1}\mu\le\varphi\le K\mu$ for some $K<\infty$.
- $\varphi$ is **pathological** if the only finitely additive $\mu\ge 0$ with $\mu\le\varphi$ is $\mu=0$.

Every measure is uniformly exhaustive; uniform exhaustivity $\Rightarrow$ exhaustivity. A **Maharam algebra** is a complete Boolean algebra carrying a strictly positive continuous submeasure; a **measure algebra** is one carrying a strictly positive $\sigma$-additive measure.

Submeasure $\to$ topology: $\varphi$ induces the metric $d(a,b)=\varphi(a\,\triangle\,b)$, and on measurable functions the $F$-norm
$$\|f\|_{\varphi}=\inf\{\varepsilon>0:\ \varphi(\{|f|>\varepsilon\})\le\varepsilon\},$$
making $L^0(\varphi)$ an $F$-space. The vector measure $\nu(A)=\chi_A\in L^0(\varphi)$ is countably additive iff $\varphi$ is continuous, and has a control measure iff $\varphi$ is equivalent to a measure. This is the bridge between CMP and submeasures.

**Anchor theorems.**

- *(Maharam 1947)* A measure algebra is characterized algebraically; every homogeneous measure algebra is isomorphic to the measure algebra of $\{0,1\}^\kappa$.
- *(Kalton–Roberts 1983)* Every uniformly exhaustive submeasure is equivalent to a measure. Proof via a combinatorial lemma with an absolute constant on balancing weights in finite set systems.
- *(Talagrand 2008)* There is an exhaustive, continuous submeasure on the clopen algebra of $\{0,1\}^{\mathbb N}$ that is **not** uniformly exhaustive, hence not equivalent to a measure.
- *(Todorcevic 2004)* Every Maharam algebra is ccc, weakly $(\sigma,\infty)$-distributive, and satisfies the $\sigma$-finite chain condition.

## 3. History & State of the Art (SOTA)

- **1947.** Maharam, *An algebraic characterization of measure algebras*, isolates the question: is every continuous exhaustive submeasure a measure?
- **1950s–70s.** CMP is posed for $F$-space-valued vector measures (Dieudonné; see Diestel–Uhl, *Vector Measures*, 1977). Positive for locally convex $X$ (Rybakov: some $|x^*\nu|$ is a control measure).
- **1975.** Herer–Christensen construct pathological submeasures (non-exhaustive), yielding exotic monothetic groups with no nontrivial characters.
- **1980.** Talagrand, *A simple example of pathological submeasure*, simplifies the Herer–Christensen object.
- **1983.** Kalton–Roberts prove uniformly exhaustive $\Rightarrow$ measure, reducing Maharam's problem exactly to the gap "exhaustive vs. uniformly exhaustive".
- **1991.** Roberts gives a candidate combinatorial scheme (nested partitions with degrading uniformity constants) that later becomes the skeleton of Talagrand's construction.
- **2004–2005.** Todorcevic proves the chain-condition properties of Maharam algebras; Balcar–Jech–Pazák and (independently) Veličković show that under the P-ideal dichotomy (a consequence of PFA), every ccc weakly distributive complete Boolean algebra is a Maharam algebra.
- **2008.** Talagrand, *Maharam's problem*, Ann. of Math. 168, 981–1009: negative solution. Combined with 2005 results, von Neumann's problem is settled negatively (consistently there is a ccc weakly distributive complete algebra that is not a measure algebra — Talagrand's).
- **2008 onward.** Farah–Veličković, *Maharam algebras*, study Maharam algebras as forcing notions (adding Cohen/random reals, weak distributivity, absoluteness). The structural theory of Maharam algebras — the residual open problem — is now the active front.

## 4. Partial Results / Verified Cases

- **Locally convex $F$-spaces**: CMP true (Bartle–Dunford–Schwartz 1955; Rybakov 1970).
- **Uniformly exhaustive submeasures**: equivalent to measures (Kalton–Roberts 1983). Covers all submeasures on **finite** algebras and all submeasures with $\varphi$ dominated by a measure up to a constant.
- **Finite algebras**: every submeasure on a finite algebra is trivially uniformly exhaustive; the phenomenon is asymptotic, in the sense that the equivalence constant $K$ must blow up along a sequence of finite stages.
- **$\sigma$-finite chain condition**: every Maharam algebra has it (Todorcevic 2004), so Maharam algebras cannot be Suslin algebras.
- **Under PID / PFA**: ccc + weakly $(\sigma,\infty)$-distributive $\Rightarrow$ Maharam algebra (Balcar–Jech–Pazák 2005; Veličković 2005). Under MA$_{\aleph_1}$ some weaker forms hold.
- **Atomic and $\sigma$-finite cases**: a continuous submeasure on a purely atomic algebra with summable atom values is a measure up to equivalence.
- **Talagrand's example**: exhaustive, continuous, defined on the clopen algebra of $\{0,1\}^{\mathbb N}$, with uniform-exhaustivity constant along level $n$ degrading like a slowly divergent sequence; explicitly not equivalent to any measure.

## 5. Principal Obstacles

- **No local convexity, no duality.** The positive theory for locally convex $X$ runs through functionals $x^*$ and Hahn–Banach. In $L^0(\varphi)$ with $\varphi$ pathological the dual can be trivial, so every duality-based argument evaporates.
- **Exhaustivity is not quantitative.** Exhaustivity is a statement about each disjoint sequence separately; uniform exhaustivity is a single uniform bound. Compactness arguments that would upgrade one to the other fail because the algebra is not compact in the submeasure metric.
- **Kalton–Roberts is intrinsically finitary.** Its combinatorial lemma has an absolute constant that is useless once uniformity degrades; the extension of a measure from level $n$ to level $n+1$ loses a factor, and nothing prevents the product from diverging.
- **No Maharam-type invariant.** Maharam's 1947 classification uses the additivity of $\mu$ in an essential way (homogeneous pieces, metric density). For submeasures there is no known homogeneity decomposition, so structural questions (2)–(3) of §1 have no algebraic handle.
- **Set-theoretic sensitivity.** The residual von Neumann question is not a ZFC question of the usual kind: its answer changes with forcing axioms, so any attempted ZFC proof must fail, and any consistency proof needs new forcing technology preserving weak distributivity.

## 6. The Gap

Proven: uniformly exhaustive $\Rightarrow$ measure; exhaustive $\not\Rightarrow$ measure. The gap is now **not** the original CMP but the fine structure of the counterexample class:

- Talagrand's submeasure fails uniform exhaustivity, but it is not known whether it (or any exhaustive submeasure) is **pathological**. Between "not equivalent to a measure" and "dominates no nonzero measure" lies an entire unexplored spectrum: the family of measures $\mu\le\varphi$ can be nonempty but degenerate.
- Between "Maharam algebra" and "measure algebra" lies the class of ccc weakly distributive algebras. PID collapses part of the picture; ZFC alone does not decide the rest. The missing step is a ZFC construction (or a consistency proof of nonexistence) of a ccc weakly distributive complete algebra that is not Maharam.

## 7. Current Research (as of June 2026)

- **Descriptive set theory of Maharam algebras.** Farah–Veličković's programme continues: which forcing-theoretic properties of measure algebras (no Cohen reals, weak distributivity, $\sigma$-finite cc) characterize Maharam algebras? Groups at Toronto/York (Farah), Paris (Veličković), Prague (Balcar school legacy, Pazák). *(frontier — verify)*
- **Quantitative reworking of Talagrand's construction**, aiming to compute the exact decay rate of the equivalence constant and thereby decide pathologicity. *(frontier — verify)*
- **Banach-space side**: twisted sums and non-locally-convex $F$-spaces built from exhaustive submeasures; Kalton's programme continued by Castillo and coauthors.
- **Combinatorics of submeasures**: connections between exhaustive submeasures and concentration / Ramsey-type partition calculus, following Todorcevic.

## 8. Future Work

- Determine whether an exhaustive pathological submeasure exists; this would give an exotic Polish group with trivial dual and an $L^0$-space with no nonzero continuous linear functionals arising from a *continuous* submeasure.
- Develop a homogeneity/decomposition theory for Maharam algebras — a "Maharam type" for continuous submeasures.
- Decide the ZFC status of "ccc + weakly distributive $\Rightarrow$ Maharam", ideally by a forcing construction preserving weak distributivity.
- Reverse-mathematics / effective content: locate the strength of Kalton–Roberts and of Talagrand's construction in subsystems of second-order arithmetic.
- Extend Fremlin's extension analysis: characterize the subalgebra pairs for which a measure on $\mathfrak{B}$ extends countably additively to a submeasure algebra $\mathfrak{A}$.

## 9. Key References

- **[Foundational]** D. Maharam. *An algebraic characterization of measure algebras.* Annals of Mathematics 48 (1947), 154–167.
- **[Foundational]** W. Herer, J. P. R. Christensen. *On the existence of pathological submeasures and the construction of exotic topological groups.* Mathematische Annalen 213 (1975), 203–210.
- **[Foundational]** J. Diestel, J. J. Uhl Jr. *Vector Measures.* Mathematical Surveys 15, American Mathematical Society, 1977.
- **[Foundational]** N. J. Kalton, J. W. Roberts. *Uniformly exhaustive submeasures and nearly additive set functions.* Transactions of the American Mathematical Society 278 (1983), 803–816.
- **[Foundational]** M. Talagrand. *A simple example of a pathological submeasure.* Mathematische Annalen 252 (1980), 97–102.
- **[SOTA / Recent]** M. Talagrand. *Maharam's problem.* Annals of Mathematics 168 (2008), 981–1009.
- **[SOTA / Recent]** S. Todorcevic. *A problem of von Neumann and Maharam about algebras supporting continuous submeasures.* Fundamenta Mathematicae 183 (2004), 169–183.
- **[SOTA / Recent]** B. Balcar, T. Jech, T. Pazák. *Complete ccc Boolean algebras, the order sequential topology, and a problem of von Neumann.* Bulletin of the London Mathematical Society 37 (2005), 885–898.
- **[SOTA / Recent]** B. Veličković. *ccc forcing and splitting reals.* Israel Journal of Mathematics 147 (2005), 209–220.
- **[SOTA / Recent]** I. Farah, B. Veličković. *Maharam algebras and Cohen reals.* Proceedings of the American Mathematical Society 135 (2007), 2283–2290.
- **[Survey]** D. H. Fremlin. *Measure Theory, Volume 3: Measure Algebras.* Torres Fremlin, 2002 — §393, "The control measure problem".
- **[Survey]** B. Balcar, T. Jech. *Weak distributivity, a problem of von Neumann and the mystery of measurability.* Bulletin of Symbolic Logic 12 (2006), 241–266.
- **[Survey]** J. W. Roberts. *Maharam's problem.* In: Proceedings of the Orlicz Memorial Conference (P. Kranz, I. Labuda, eds.), University of Mississippi, 1991.

## 10. Worked Example / Concrete Special Case

**(a) A finite partition submeasure, with its equivalence constant computed.**
Let $\Omega=\{1,\dots,6\}$ and $\mathcal{P}=\{\{1,2\},\{3,4\},\{5,6\}\}$. Define
$$\varphi(A)=\tfrac13\,\\#\{P\in\mathcal{P}: P\cap A\neq\emptyset\}.$$
$\varphi$ is monotone and subadditive (a cover of $A\cup B$ meets at most the union of the two hit-sets), so it is a submeasure, with $\varphi(\Omega)=1$. It is badly non-additive: $\varphi(\{1\})=\varphi(\{1,2\})=\tfrac13$, so $\varphi(\{1\})+\varphi(\{2\})=\tfrac23>\varphi(\{1,2\})$. Yet with counting measure $\mu(A)=|A|/6$ one checks all $2^6$ sets and gets
$$\mu(A)\ \le\ \varphi(A)\ \le\ 2\,\mu(A)\quad (A\neq\emptyset),$$
the upper bound being tight at $A=\{1,3,5\}$ where $\mu=\tfrac12$, $\varphi=1$. So $\varphi$ is equivalent to a measure with constant $K=2$ — as Kalton–Roberts guarantees for every finite algebra.

**(b) Where the problem lives.** Stack such partition submeasures over levels $n=1,2,\dots$ on $\{0,1\}^{\mathbb N}$, taking at level $n$ a family of $m_n$ partitions and forming
$$\varphi(A)=\inf\Big\{\sum_{i} \varphi_{n_i}(A_i)\ :\ A\subseteq\bigcup_i A_i\Big\}.$$
Talagrand chooses $m_n$ so that (i) every disjoint sequence still has $\varphi(a_k)\to0$ (exhaustivity survives, because each single set is eventually witnessed at deep levels), while (ii) the best constant $K_n$ in $K_n^{-1}\mu\le\varphi\le K_n\mu$ at level $n$ satisfies $K_n\to\infty$. Since a global measure equivalent to $\varphi$ would give a uniform $K$, no such measure exists.

**(c) Back to control measures.** With $\varphi$ as in (b), form $L^0(\varphi)$ under $\|f\|_\varphi=\inf\{\varepsilon:\varphi(|f|>\varepsilon)\le\varepsilon\}$ and set $\nu(A)=\chi_A$. Continuity of $\varphi$ gives $\nu$ countably additive; a control measure $\mu$ for $\nu$ would satisfy $\mu(A)\to0\iff\varphi(A)\to0$, i.e. exactly the equivalence ruled out in (b). Contrast the classical case $\varphi=\lambda$ (Lebesgue): $L^0[0,1]$ with convergence in measure, $\nu(A)=\chi_A$, control measure $\mu=\lambda$ — CMP holds. The difference between the two lines is the entire content of the problem.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*