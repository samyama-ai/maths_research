---
id: 02-algebra-group-theory/kronecker-coefficients-positivity
title: "Kronecker Coefficients Positivity"
topic: 02-algebra-group-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Kronecker Coefficients Positivity

> **Topic:** Algebra & Group Theory · **ID:** `02-algebra-group-theory/kronecker-coefficients-positivity` · **Status:** open

## 1. Problem Statement / Conjecture

For partitions $\lambda,\mu,\nu \vdash n$, the **Kronecker coefficient** $g(\lambda,\mu,\nu)$ is the multiplicity of the irreducible $S_n$-representation $S^\lambda$ in the tensor product $S^\mu \otimes S^\nu$. These are non-negative integers defined by a character computation with signs, and the central problem is:

**Problem (Murnaghan 1938; Stanley's Problem 10, 2000).** Find a *combinatorial interpretation* of $g(\lambda,\mu,\nu)$: an explicit family of combinatorial objects $\mathcal{O}(\lambda,\mu,\nu)$, together with a polynomial-time-checkable membership test, such that
$$g(\lambda,\mu,\nu) = \\#\,\mathcal{O}(\lambda,\mu,\nu).$$

Equivalently, in complexity terms: is the function $g$ in the counting class $\\#\mathrm{P}$? A complete solution is either (i) such a family plus a proof that it counts $g$, or (ii) a proof that no $\\#\mathrm{P}$ formula exists (necessarily conditional, since $\\#\mathrm{P} \ne \mathrm{FP}$-type separations are open).

The associated **positivity problem** is the decision version: given $\lambda,\mu,\nu$ in binary, decide whether $g(\lambda,\mu,\nu) > 0$. Mulmuley conjectured this to be in $\mathrm{P}$, by analogy with Littlewood–Richardson coefficients. It is now known to be $\mathrm{NP}$-hard, so the conjecture is false unless $\mathrm{P} = \mathrm{NP}$. What remains open is a structural characterization of the support $\{(\lambda,\mu,\nu) : g > 0\}$, and the combinatorial-interpretation problem above.

## 2. Mathematical Foundations

Let $\chi^\lambda$ denote the irreducible character of $S_n$ indexed by $\lambda \vdash n$, and let $z_\rho = \prod_i i^{m_i} m_i!$ for a cycle type $\rho$ with $m_i$ parts equal to $i$. Then
$$g(\lambda,\mu,\nu) \;=\; \langle \chi^\lambda \chi^\mu, \chi^\nu\rangle \;=\; \sum_{\rho \vdash n} \frac{1}{z_\rho}\,\chi^\lambda_\rho\,\chi^\mu_\rho\,\chi^\nu_\rho .$$
The expression is symmetric in $\lambda,\mu,\nu$ and invariant under conjugating any two of them: $g(\lambda,\mu,\nu) = g(\lambda',\mu',\nu)$.

**Symmetric function form.** With $*$ the internal (Kronecker) product on degree-$n$ symmetric functions, $s_\mu * s_\nu = \sum_\lambda g(\lambda,\mu,\nu)\, s_\lambda$.

**$GL$ form (Schur–Weyl).** For $\ell(\mu)\le a$, $\ell(\nu)\le b$, $\ell(\lambda) \le ab$,
$$s_\lambda(xy) \;=\; \sum_{\mu,\nu} g(\lambda,\mu,\nu)\, s_\mu(x)\, s_\nu(y),$$
so $g$ is the multiplicity of $V^{\mu}_{GL_a}\otimes V^{\nu}_{GL_b}$ in the restriction of $V^\lambda_{GL_{ab}}$ along $GL_a \times GL_b \hookrightarrow GL_{ab}$.

**Contrast with Littlewood–Richardson.** The LR coefficients $c^\lambda_{\mu\nu}$ have the LR-tableau interpretation, satisfy the Horn/Klyachko inequalities, obey **saturation** ($c^{N\lambda}_{N\mu\,N\nu}>0 \Rightarrow c^\lambda_{\mu\nu}>0$, Knutson–Tao 1999), and positivity is decidable in polynomial time (Mulmuley–Narayanan–Sohoni). Kronecker coefficients generalize them: $c^\lambda_{\mu\nu}$ is a special case of the **reduced Kronecker coefficient**
$$\bar g(\bar\lambda,\bar\mu,\bar\nu) \;=\; \lim_{n\to\infty} g\big(\,(n-|\bar\lambda|,\bar\lambda),\,(n-|\bar\mu|,\bar\mu),\,(n-|\bar\nu|,\bar\nu)\,\big),$$
the limit existing by **Murnaghan's stability theorem** (proved with effective bounds by Vallejo 1999 and Briand–Orellana–Rosas 2011: the sequence stabilizes once $n \ge |\bar\lambda|+|\bar\mu|+|\bar\nu| + \bar\lambda_1$-type thresholds).

**Asymptotic/moment-polytope form.** The set $\{(\lambda,\mu,\nu) : g(N\lambda,N\mu,N\nu)>0 \text{ for some } N\ge 1\}$ is, after normalization, a rational convex polytope — the moment (Kirwan) polytope of $\mathbb{P}(\mathbb{C}^a\otimes\mathbb{C}^b\otimes\mathbb{C}^c)$ — and the Kronecker semigroup is finitely generated (Christandl–Harrow–Mitchison 2007; Klyachko). This is exactly the one-body **quantum marginal problem** for three parties.

## 3. History & State of the Art (SOTA)

- **1938.** Murnaghan introduces the problem and proves stability of $g$ under lengthening first rows.
- **1958.** Littlewood computes special cases; the Kronecker product resists the machinery that settles the outer product.
- **1994–2005.** Explicit rules in low-complexity families: Remmel–Whitehead (two rows), Rosas (two-row and hook shapes), Ballantine–Orellana (one two-row factor under a first-part condition).
- **2000.** Stanley lists the combinatorial interpretation as Problem 10 in *Positivity problems and conjectures in algebraic combinatorics* — still open.
- **2001–2008.** Geometric complexity theory (Mulmuley–Sohoni) makes Kronecker positivity a load-bearing question: the GCT program proposed separating $\mathrm{VP}$ from $\mathrm{VNP}$ using representation-theoretic *occurrence obstructions*, requiring efficient control over multiplicities.
- **2009–2017.** The complexity picture inverts the optimistic GCT expectation. Bürgisser–Ikenmeyer: computing $g$ is $\\#\mathrm{P}$-hard. Pak–Panova: $\\#\mathrm{P}$-hardness persists even for **two-row** $\lambda$ (bounded number of rows). Ikenmeyer–Mulmuley–Walter: deciding $g(\lambda,\mu,\nu)>0$ is $\mathrm{NP}$-hard, and $g$ is not in $\\#\mathrm{P}$ unless $\mathrm{NP} = \mathrm{coNP}$-type collapses; Briand–Orellana–Rosas refute Mulmuley's strong saturation conjecture SH.
- **2019.** Bürgisser–Ikenmeyer–Panova prove *no occurrence obstructions* exist for permanent-vs-determinant, ending that GCT route and shifting attention to multiplicity (not occurrence) obstructions.
- **State of the art.** Positivity is understood asymptotically (polytope/semigroup level), completely in a handful of shape families, and is provably hard in general. No general combinatorial rule exists.

## 4. Partial Results / Verified Cases

Cases with proven combinatorial rules or complete positivity criteria:

| Family | Result | Source |
|---|---|---|
| $\lambda$ a hook or two-row, $\mu$ arbitrary | explicit signed-free rule via $\lambda$-restricted tableaux | Rosas (2001) |
| both $\mu,\nu$ two-row shapes | closed formula for $g$ | Remmel–Whitehead (1994) |
| $\mu = (n-p,p)$, $\lambda$ arbitrary with $\lambda_1 \ge 2p-1$ | positive rule | Ballantine–Orellana (2005) |
| one of $\lambda,\mu,\nu$ a hook | combinatorial interpretation via colored Yamanouchi words / noncommutative super Schur functions | Blasiak (2017); Blasiak–Liu (2018) |
| $\lambda,\mu,\nu$ all rectangles | nonvanishing criteria; $g>0$ for large classes | Bürgisser–Christandl–Ikenmeyer (2011) |
| multiplicity-free products $\chi^\mu\chi^\nu$ | full classification | Bessenrodt–Bowman (2017) |
| $\mu=\nu$, $\lambda$ near-trivial; $g(\lambda,\mu,\nu)=1$ cases | classification of multiplicity-one triples | Pak–Panova and others |
| stable range | $\bar g$ well-defined and $\ge c^{\bar\lambda}_{\bar\mu\bar\nu}$; stability thresholds explicit | Murnaghan; Vallejo (1999); Briand–Orellana–Rosas (2011); Sam–Snowden (2016) |
| $\ell(\mu),\ell(\nu) \le k$ fixed, $N$-stretched | $g(N\lambda,N\mu,N\nu)$ is a quasi-polynomial in $N$ | Baldoni–Vergne–Walter; Manivel (2015) |

Computationally, $g(\lambda,\mu,\nu)$ has been tabulated exhaustively for all $n \le 30$-ish and for structured families far beyond, via character-theoretic and Barvinok-style lattice-point algorithms; no counterexample to any of the standing positivity conjectures (e.g. Saxl's conjecture that $\chi^{\delta_k}\otimes\chi^{\delta_k}$ with $\delta_k=(k,k-1,\dots,1)$ contains every irreducible) has appeared in these ranges.

## 5. Principal Obstacles

- **Sign cancellation in the defining formula.** The character sum $\sum_\rho z_\rho^{-1}\chi^\lambda_\rho\chi^\mu_\rho\chi^\nu_\rho$ has terms of both signs and exponentially many summands; no bijective cancellation scheme is known. Every family where a rule exists is one where the signs can be tamed by a plethystic or crystal-theoretic device.
- **Failure of saturation.** $g(\lambda,\mu,\nu)=0$ does *not* imply $g(N\lambda,N\mu,N\nu)=0$ (see §10). Hence the polytope/moment-map description controls only the asymptotic support, and no Horn-type recursion transfers from the LR setting.
- **No crystal or cluster structure.** Littlewood–Richardson positivity follows from a $\mathfrak{gl}$-crystal on tableaux; the internal product corresponds to restriction along a non-Levi subgroup $GL_a\times GL_b \subset GL_{ab}$, for which no crystal-theoretic branching rule is known.
- **Hardness is a genuine barrier, not a gap in ingenuity.** Deciding $g>0$ is $\mathrm{NP}$-hard (Ikenmeyer–Mulmuley–Walter 2017), so any "efficient" positivity criterion is impossible under $\mathrm{P}\ne\mathrm{NP}$. Consequently a combinatorial interpretation, if it exists, must have a membership test whose *nonemptiness* is itself $\mathrm{NP}$-hard — ruling out the tableau-style rules that succeed elsewhere.
- **Geometry does not localize.** The GCT approach needed vanishing/nonvanishing of specific multiplicities; Bürgisser–Ikenmeyer–Panova showed the relevant occurrences all fail to vanish, so the geometry provides no shortcut.

## 6. The Gap

Proven (§4) is: rules for triples where at least one partition is combinatorially degenerate (hook, two rows, rectangle) or where one passes to the stable limit $\bar g$; plus an asymptotic, polytopal description of the support of $g$ under dilation. The general statement (§1) asks for a uniform, cancellation-free count for arbitrary $\lambda,\mu,\nu$ with unbounded row and column counts.

The precise barrier: convert the *asymptotic* positivity criterion (membership in the Kronecker polytope, decidable but only for the dilated family) into a *finite-level* criterion at $N=1$. Saturation is exactly the bridge that does this for LR coefficients and exactly what fails here. Absent saturation, one needs either (a) a new invariant certifying $g(\lambda,\mu,\nu)=0$ inside the polytope, or (b) a $\\#\mathrm{P}$ formula compatible with $\mathrm{NP}$-hard nonemptiness — a shape of answer with no precedent in algebraic combinatorics.

## 7. Current Research (as of June 2026)

- **Complexity-first school (Panova, Pak, Ikenmeyer, Bürgisser).** Sharpening what "combinatorial interpretation" can mean: whether $g \in \\#\mathrm{P}$, whether differences of Kronecker coefficients lie in $\\#\mathrm{P}$, and hardness for restricted shape classes. Panova's survey *Complexity and asymptotics of structure constants* is the current reference frame. Institutions: USC, UCLA, Warwick, Paderborn.
- **Algebraic-combinatorics school (Blasiak, Liu, Orellana, Zabrocki).** Extending the one-hook rule; the Orellana–Zabrocki basis of symmetric functions whose structure constants are Kronecker coefficients converts the problem into a manageable change-of-basis question and is an active line. *(frontier — verify)* claims of rules for "one shape with two rows plus arbitrary" continue to appear.
- **Quantum information / moment polytopes (Christandl, Walter, Vergne).** Kronecker positivity as the three-party marginal problem; algorithms for membership in moment polytopes via scaling algorithms (operator/tensor scaling) give randomized decision procedures in the stretched regime.
- **Saxl's conjecture and staircase products (Pak, Panova, Vallejo, Bessenrodt, Luo–Sellke).** Large explicit families of constituents proven; the full conjecture remains open and is a testbed for positivity techniques.
- **Stability and $\mathrm{FI}$-module methods (Sam, Snowden).** Categorical explanations of Murnaghan stability, extended to secondary stability phenomena.

## 8. Future Work

- Prove or disprove $g \in \\#\mathrm{P}$ unconditionally, or establish it under a standard hypothesis; the community consensus (Pak, Panova) is that a clean tableau rule likely does not exist and the right target is a rule for a "positive part" of $g$.
- Find a *finite* obstruction theory explaining the failure of saturation — e.g. torsion-type invariants that vanish exactly on the saturated locus.
- Develop crystal-like structures for the restriction $GL_{ab}\downarrow GL_a\times GL_b$, possibly via super or quantum deformations, extending Blasiak–Liu's noncommutative super Schur function calculus beyond one hook.
- Push explicit rules to three-row shapes; this is the smallest open case not covered by Rosas/Remmel–Whitehead.
- Settle Saxl's conjecture; more generally characterize triples with $g=1$ and triples with $\mu=\nu$ covering all $\lambda$.

## 9. Key References

- **[Foundational]** F. D. Murnaghan. *The analysis of the Kronecker product of irreducible representations of the symmetric group.* American Journal of Mathematics 60 (1938), 761–784.
- **[Foundational]** R. P. Stanley. *Positivity problems and conjectures in algebraic combinatorics.* In: Mathematics: Frontiers and Perspectives, AMS, 2000, 295–319.
- **[Partial rules]** M. H. Rosas. *The Kronecker product of Schur functions indexed by two-row shapes or hook shapes.* Journal of Algebraic Combinatorics 14 (2001), 153–173.
- **[Partial rules]** J. B. Remmel, T. Whitehead. *On the Kronecker product of Schur functions of two row shapes.* Bulletin of the Belgian Mathematical Society 1 (1994), 649–683.
- **[Partial rules]** C. Ballantine, R. Orellana. *On the Kronecker product $s_{(n-p,p)} * s_\lambda$.* Electronic Journal of Combinatorics 12 (2005), R28.
- **[Partial rules]** J. Blasiak. *Kronecker coefficients for one hook shape.* Séminaire Lotharingien de Combinatoire 77 (2017), Art. B77c.
- **[SOTA]** J. Blasiak, R. I. Liu. *Kronecker coefficients and noncommutative super Schur functions.* Journal of Combinatorial Theory Series A 158 (2018), 315–361.
- **[Stability]** E. Briand, R. Orellana, M. Rosas. *The stability of the Kronecker product of Schur functions.* Journal of Algebra 331 (2011), 11–27.
- **[Stability]** S. Sam, A. Snowden. *Proof of Stembridge's conjecture on stability of Kronecker coefficients.* Journal of Algebraic Combinatorics 43 (2016), 1–10.
- **[Complexity]** E. Briand, R. Orellana, M. Rosas. *Reduced Kronecker coefficients and counter-examples to Mulmuley's strong saturation conjecture SH.* Computational Complexity 18 (2009), 577–600.
- **[Complexity]** I. Pak, G. Panova. *On the complexity of computing Kronecker coefficients.* Computational Complexity 26 (2017), 1–36.
- **[Complexity / SOTA]** C. Ikenmeyer, K. D. Mulmuley, M. Walter. *On vanishing of Kronecker coefficients.* Computational Complexity 26 (2017), 949–992.
- **[GCT]** K. D. Mulmuley, M. Sohoni. *Geometric Complexity Theory II: Towards explicit obstructions for embeddings among class varieties.* SIAM Journal on Computing 38 (2008), 1175–1206.
- **[SOTA]** P. Bürgisser, C. Ikenmeyer, G. Panova. *No occurrence obstructions in geometric complexity theory.* Journal of the American Mathematical Society 32 (2019), 163–193.
- **[Quantum marginals]** M. Christandl, A. W. Harrow, G. Mitchison. *Nonzero Kronecker coefficients and what they tell us about spectra.* Communications in Mathematical Physics 270 (2007), 575–585.
- **[Rectangles]** P. Bürgisser, M. Christandl, C. Ikenmeyer. *Nonvanishing of Kronecker coefficients for rectangular shapes.* Advances in Mathematics 227 (2011), 2082–2091.
- **[Asymptotics]** L. Manivel. *On the asymptotics of Kronecker coefficients.* Journal of Algebraic Combinatorics 42 (2015), 999–1025.
- **[Survey]** G. Panova. *Complexity and asymptotics of structure constants.* arXiv:2305.02553, 2023.

## 10. Worked Example / Concrete Special Case

**Saturation fails at the smallest possible size.**

*Step 1: $g((1,1),(1,1),(1,1)) = 0$.* In $S_2$ the two classes are $1^2$ and $2$, each of size $1$, with $z_{1^2}=2$, $z_{2}=2$. The sign character $\chi^{(1,1)}$ takes values $(1,-1)$. So
$$g = \frac{1^3}{2} + \frac{(-1)^3}{2} = \frac{1}{2}-\frac{1}{2} = 0 .$$
Representation-theoretically: $\mathrm{sgn}\otimes\mathrm{sgn} = \mathbf{1}$, which contains no copy of $\mathrm{sgn}$.

*Step 2: $g((2,2),(2,2),(2,2)) = 1$.* In $S_4$ the classes $1^4, 2\,1^2, 2^2, 3\,1, 4$ have sizes $1,6,3,8,6$. The two-dimensional irreducible $S^{(2,2)}$ has character values
$$\chi^{(2,2)} = (2,\,0,\,2,\,-1,\,0).$$
Then
$$g = \frac{1}{24}\Big[1\cdot 2^3 + 6\cdot 0^3 + 3\cdot 2^3 + 8\cdot(-1)^3 + 6\cdot 0^3\Big] = \frac{8 + 24 - 8}{24} = \frac{24}{24} = 1 .$$

*Conclusion.* With $\lambda=\mu=\nu=(1,1)$ and $N=2$ we have $g(N\lambda,N\mu,N\nu) = 1 > 0$ but $g(\lambda,\mu,\nu)=0$. The saturation property that makes Littlewood–Richardson positivity polynomial-time decidable (Knutson–Tao) is therefore false for Kronecker coefficients, even at $n=2$. This single $2\times 2$ example is the reason the moment-polytope description of §2 — which sees only the dilated family — cannot decide positivity at $N=1$, and it is the precise content of the gap in §6.

*Contrast.* A positive case with a known rule: for $\lambda$ a hook, Blasiak's rule counts colored Yamanouchi tableaux. E.g. $g((3,1),(3,1),(3,1)) = 1$: with $\chi^{(3,1)} = (3,1,-1,0,-1)$,
$$g = \frac{1}{24}\big[1\cdot 27 + 6\cdot 1 + 3\cdot(-1) + 8\cdot 0 + 6\cdot(-1)\big] = \frac{27+6-3-6}{24} = 1 .$$
Here a cancellation-free count exists; for a generic triple of partitions of $n=40$ with four or more rows each, no such count is known.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*