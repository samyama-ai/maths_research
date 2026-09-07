---
id: 04-topology/hoste-conjecture
title: "Hoste Conjecture"
topic: 04-topology
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Hoste Conjecture

> **Topic:** Topology & Knot Theory · **ID:** `04-topology/hoste-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

**Conjecture (Hoste, c. 2002).** Let $K \subset S^3$ be a knot and let $\Delta_K(t) \in \mathbb{Z}[t^{\pm 1}]$ be its Alexander polynomial. Then every complex root $z$ of $\Delta_K$ satisfies
$$\operatorname{Re}(z) > -1 .$$

Equivalently: the roots of $\Delta_K$ all lie strictly to the right of the vertical line $\operatorname{Re}(z) = -1$ in $\mathbb{C}$.

The statement is about **knots** (one component) in $S^3$. It is false as stated for links: the multivariable-to-one-variable specialization for links loses the normalization $\Delta(1) = \pm 1$, which is the arithmetic input the conjecture depends on. No orientation, fiberedness, or alternation hypothesis is assumed.

A complete resolution requires either (i) a proof valid for all knots, or (ii) an explicit knot $K$ together with a certified root $z$ of $\Delta_K$ with $\operatorname{Re}(z) \le -1$. Because $\Delta_K$ is a concrete integer polynomial, a counterexample would be finitely checkable by exact arithmetic (Sturm sequences / resultants), so the conjecture is falsifiable in a strong sense. It is empirically supported: Hoste checked all $1{,}701{,}936$ prime knots of at most $16$ crossings.

## 2. Mathematical Foundations

**Alexander polynomial via a Seifert matrix.** Let $F$ be a Seifert surface for $K$ of genus $g$, so $H_1(F;\mathbb{Z}) \cong \mathbb{Z}^{2g}$. Let $V$ be the Seifert linking matrix, $V_{ij} = \operatorname{lk}(x_i, x_j^{+})$. Then
$$\Delta_K(t) \;\doteq\; \det\!\left(V - t\,V^{T}\right),$$
where $\doteq$ means equality up to $\pm t^{k}$. Normalize so that $\Delta_K(t) = \sum_{i=0}^{2n} a_i t^{i}$ with $a_0 \ne 0$, $a_{2n} \neq 0$.

**Structural constraints.** For every knot:

1. **Reciprocity (symmetry):** $\Delta_K(t^{-1}) \doteq \Delta_K(t)$, i.e. $a_i = a_{2n-i}$ after normalization. Hence $\deg \Delta_K$ is even and roots occur in pairs $\{z, z^{-1}\}$; with real coefficients they occur in quadruples $\{z, \bar z, z^{-1}, \bar z^{-1}\}$.
2. **Normalization:** $\Delta_K(1) = \pm 1$ (the infinite cyclic cover of a knot complement has $H_1$ of the Alexander module with trivial $t=1$ specialization).
3. **Determinant:** $|\Delta_K(-1)| = \det(K) = |H_1(\Sigma_2(K))|$ is a positive odd integer; in particular $z = -1$ is **never** a root, and $z=0$ is never a root.

**Seifert realization.** Conversely (Seifert, 1934), every $f \in \mathbb{Z}[t^{\pm1}]$ with $f(t^{-1}) \doteq f(t)$ and $f(1) = \pm 1$ is the Alexander polynomial of some knot. So Hoste's conjecture is *exactly equivalent* to the purely arithmetic statement:

> **(H′)** If $f \in \mathbb{Z}[t]$ is reciprocal of even degree with $f(1) = \pm 1$, then every root of $f$ has real part $> -1$.

**Reduction to the unit disk.** Since roots come in pairs $z \leftrightarrow z^{-1}$, and the Möbius map $z \mapsto z^{-1}$ carries the closed half-plane $\{\operatorname{Re} z \le -1\}$ onto the punctured closed disk
$$D \;=\; \Big\{\, z : \big|z + \tfrac12\big| \le \tfrac12 \,\Big\} \setminus \{0\},$$
Hoste's conjecture is equivalent to: **$\Delta_K$ has no root in the disk $D$ of radius $\tfrac12$ centred at $-\tfrac12$** (the disk tangent to the imaginary axis at $0$ and passing through $-1$).

**Factorization reduction.** If $\Delta_K = \prod_i p_i$ with $p_i \in \mathbb{Z}[t]$ irreducible, then $\prod_i p_i(1) = \pm 1$ with each $p_i(1) \in \mathbb{Z}$, so $p_i(1) = \pm 1$ for **every** factor. Thus it suffices to prove (H′) for irreducible reciprocal $f$ with $f(1) = \pm 1$.

## 3. History & State of the Art (SOTA)

- **1928–1934.** Alexander introduces $\Delta_K$; Seifert gives the surface/matrix construction and the realization theorem.
- **1958–1959.** Murasugi and Crowell prove that for an alternating knot the coefficients of $\Delta_K$ are non-zero and **alternate in sign**, and $\deg \Delta_K = 2g(K)$. This is the single most useful structural input for the conjecture.
- **1962.** Fox's trapezoidal conjecture (coefficients of alternating knots are trapezoidal) sets the template of "coefficient shape $\Rightarrow$ root location" questions that Hoste's conjecture sits beside.
- **1998.** Hoste, Thistlethwaite and Weeks tabulate all $1{,}701{,}936$ prime knots up to $16$ crossings, making large-scale root computation possible.
- **c. 2002.** Hoste formulates the conjecture after computing all roots in that table. It circulated as an unpublished observation and was recorded in print by later authors.
- **2000s.** Root-location questions gain independent motivation from Mahler measure and homology growth (Silver–Williams; Hironaka's identification of Lehmer's polynomial with $\Delta$ of the $(-2,3,7)$-pretzel knot).
- **2012–2015.** Lyubich–Murasugi prove the conjecture for large classes of alternating knots via Eneström–Kakeya-type coefficient conditions; Hirasawa–Murasugi develop a systematic "stability" framework for Alexander polynomials; Stoimenow analyses roots of link polynomials in relation to Hoste's conjecture.

**SOTA summary.** No unconditional bound of the form $\operatorname{Re}(z) > -C$ for a universal constant $C$ is known for all knots. What is known are (a) full proofs on explicit infinite families, and (b) coefficient-driven criteria that certify individual polynomials.

## 4. Partial Results / Verified Cases

- **Computational verification:** all prime knots with $\le 16$ crossings ($1{,}701{,}936$ knots, Hoste–Thistlethwaite–Weeks census). No root with $\operatorname{Re}(z) \le -1$ appears.
- **Genus one ($\deg \Delta = 2$):** completely settled — see Section 10. Every root has $\operatorname{Re}(z) \ge \tfrac12$ or is a positive real. This covers all twist knots and all doubled knots.
- **Quadratic factors:** by the factorization reduction, any reciprocal quadratic factor $at^2+bt+a$ of $\Delta_K$ satisfies $2a+b = \pm1$ and hence has roots with $\operatorname{Re}(z) \in \{1 \mp \frac{1}{2a}\} \subset [\tfrac12,\tfrac32]$ or two positive real roots. So knots whose Alexander polynomial splits over $\mathbb{Z}$ into quadratics satisfy the conjecture.
- **Torus knots $T(p,q)$:** $\Delta(t) = \dfrac{(t^{pq}-1)(t-1)}{(t^{p}-1)(t^{q}-1)}$ is a product of cyclotomic polynomials; all roots are roots of unity, $|z| = 1$, and $z = -1$ is excluded since $\det(T(p,q)) \ne 0$. Conjecture holds, with $\operatorname{Re}(z) > -1$ but values accumulating toward $-1$ as $pq \to \infty$ — showing the constant $-1$ cannot be improved to any $-1+\varepsilon$.
- **Alternating knots, real axis:** by Murasugi–Crowell, $\Delta_K(-t)$ has all coefficients of one sign, so $\Delta_K$ has **no negative real root at all**. Hoste's conjecture is therefore automatic on $\mathbb{R}$ for alternating knots; only complex roots are at issue.
- **Alternating families with coefficient control:** Lyubich–Murasugi (2012) prove the conjecture for classes of alternating knots whose sign-normalized coefficient sequences satisfy Eneström–Kakeya-type ratio/dominance conditions (e.g. suitable monotonicity of $a_i/a_{i+1}$), covering infinite families including many two-bridge knots.
- **Stability classes:** Hirasawa–Murasugi identify families (certain two-bridge and pretzel knots, and Alexander polynomials of specific periodic constructions) whose roots lie entirely on $|z| = 1$ or in the open right half-plane $\operatorname{Re}(z) > 0$ — strictly stronger than Hoste's bound.

## 5. Principal Obstacles

- **The only global input is a single evaluation.** The conjecture must be extracted from $\Delta_K(1) = \pm1$ plus reciprocity (statement (H′)). One equation at one point is extremely weak leverage on the location of $2n$ roots; classical root-location machinery (Eneström–Kakeya, Schur–Cohn, Routh–Hurwitz) requires knowledge of *all* coefficients or of a definite sign pattern, which arbitrary knots do not provide.
- **Coefficients are unbounded and unstructured.** For general (non-alternating) knots the $a_i$ can have arbitrary signs and grow arbitrarily; there is no known a priori bound like $|a_i| \le C(n)$. Any argument by coefficient inequalities therefore has no starting point.
- **The bound is sharp, so no slack exists.** Torus knots put roots arbitrarily close to $-1$. Any proof strategy that loses even an $\varepsilon$ (as perturbation, continuity, or compactness arguments typically do) cannot conclude.
- **Topology does not see root location.** Roots of $\Delta_K$ are not known to correspond to a geometric or homological quantity that is monotone under standard operations (crossing change, cabling, satellite, Dehn filling). Twisted Alexander and Heegaard Floer refinements control $\deg \Delta$, leading coefficients, and fiberedness — not the argument of a root.
- **Alternating techniques do not transfer.** The Murasugi–Crowell sign-alternation theorem is the workhorse in all proved cases, and it is false outside the alternating class; even inside it, sign alternation alone kills only real roots, not complex roots near $-1$.

## 6. The Gap

Proved: the conjecture for polynomials with a controlled coefficient shape (alternating signs plus ratio conditions), for degree $2$, for cyclotomic $\Delta$, and computationally to $16$ crossings. Conjectured: all knots.

The exact missing step is a mechanism that converts the arithmetic normalization $f(1) = \pm 1$ into a root-free region. Concretely, the open problem is:

> Show that no reciprocal $f \in \mathbb{Z}[t]$, irreducible, with $f(1) = \pm1$, has a root in the closed disk $\big|z+\tfrac12\big| \le \tfrac12$.

Even the weaker statement "there exists a universal $C > 0$ with $\operatorname{Re}(z) > -C$ for all knot Alexander polynomial roots" is open. Nothing currently rules out a high-degree irreducible reciprocal integer polynomial that takes value $\pm1$ at $t=1$ while placing a conjugate pair deep inside $D$; the obstruction, if real, must come from the interaction of integrality with reciprocity across *all* conjugates simultaneously — an equidistribution/height phenomenon of the same flavour as Lehmer's problem, and no such tool is currently available at the needed precision.

## 7. Current Research (as of June 2026)

- **Coefficient-criteria school (Murasugi lineage; Toronto, Meijo).** Extending the Lyubich–Murasugi and Hirasawa–Murasugi "stability" hierarchy — *stable* (all roots in a half-plane), *bi-stable*, *quasi-stable* — to broader alternating and Montesinos families, and to non-alternating knots with controlled Seifert matrices.
- **Arithmetic-dynamics viewpoint.** Treating (H′) as a height/Mahler-measure question: the set of reciprocal integer polynomials with $f(1)=\pm1$ and bounded Mahler measure is where the extreme root behaviour concentrates (Lehmer's polynomial, $\Delta$ of the $(-2,3,7)$-pretzel knot, has $\Delta(-1)=1$ and eight unimodular roots). Whether small Mahler measure forces roots away from $D$ is open. *(frontier — verify)*
- **Enumeration beyond 16 crossings.** Root scans over $17$–$19$ crossing tabulations and over random braid-closure samples, searching for near-counterexamples with $\operatorname{Re}(z)$ close to $-1$ that are not torus-like. *(frontier — verify)*
- **Twisted and categorified refinements.** Whether twisted Alexander polynomials or the Alexander grading of knot Floer homology impose additional root constraints; so far these control degree and fiberedness rather than root position.

## 8. Future Work

1. **Prove a universal constant.** Establish $\operatorname{Re}(z) > -C$ for some explicit $C$ (even $C = 10^{6}$) for all knots. This would be the first unconditional global result and would isolate whether $C = 1$ is arithmetic or accidental.
2. **Settle the alternating case.** Remove the coefficient-ratio hypotheses from Lyubich–Murasugi, using only Murasugi–Crowell sign alternation plus trapezoidal-type constraints. A proof of Fox's trapezoidal conjecture may feed directly into this.
3. **Attack (H′) directly.** Study the discrete set $\{f : f \text{ reciprocal}, f(1) = \pm1\}$ as a lattice slice and ask for the minimal $\operatorname{Re}$ of a root at each degree $2n$; compute this extremal function exactly for $n \le 6$ by exact optimization.
4. **Test genus-2 completely.** Classify degree-$4$ reciprocal integer polynomials with $f(1) = \pm1$ and verify (H′) exhaustively — a finite two-parameter family, likely tractable by hand.
5. **Search for structure at the boundary.** Characterize which knots realize roots with $\operatorname{Re}(z)$ within $10^{-3}$ of $-1$; if torus knots and cables are the only ones, a rigidity theorem may be within reach.

## 9. Key References

- **[Foundational]** H. Seifert. *Über das Geschlecht von Knoten.* Mathematische Annalen 110 (1934), 571–592.
- **[Foundational]** R. H. Crowell. *Genus of alternating link types.* Annals of Mathematics 69 (1959), 258–275.
- **[Foundational]** K. Murasugi. *On the genus of the alternating knot, I & II.* Journal of the Mathematical Society of Japan 10 (1958), 94–105 and 235–248.
- **[Foundational]** R. H. Fox. *Some problems in knot theory.* In: Topology of 3-Manifolds and Related Topics, Prentice-Hall, 1962, 168–176.
- **[Computational]** J. Hoste, M. Thistlethwaite, J. Weeks. *The First 1,701,936 Knots.* The Mathematical Intelligencer 20 (1998), no. 4, 33–48.
- **[SOTA / Recent]** L. Lyubich, K. Murasugi. *On zeros of the Alexander polynomial of an alternating knot.* Topology and its Applications 159 (2012), 290–303.
- **[SOTA / Recent]** M. Hirasawa, K. Murasugi. *Various stabilities of the Alexander polynomials of knots and links.* arXiv preprint arXiv:1307.1578, 2013.
- **[SOTA / Recent]** A. Stoimenow. *Hoste's conjecture and roots of link polynomials.* Annales mathématiques Blaise Pascal, 2015.
- **[Related]** E. Hironaka. *The Lehmer polynomial and pretzel links.* Canadian Mathematical Bulletin 44 (2001), 440–451.
- **[Related]** D. Silver, S. Williams. *Mahler measure, links and homology growth.* Topology 41 (2002), 979–991.
- **[Tool]** N. Anderson, E. B. Saff, R. S. Varga. *On the Eneström–Kakeya theorem and its sharpness.* Linear Algebra and its Applications 28 (1979), 5–16.
- **[Survey / Textbook]** W. B. R. Lickorish. *An Introduction to Knot Theory.* Graduate Texts in Mathematics 175, Springer, 1997.

## 10. Worked Example / Concrete Special Case

**Claim: Hoste's conjecture holds for every genus-one knot, with an explicit sharp margin.**

Let $K$ have a genus-one Seifert surface. Then $H_1(F) = \mathbb{Z}^2$ and, in a symplectic basis, the Seifert matrix can be taken as
$$V = \begin{pmatrix} a & 1 \\ 0 & b \end{pmatrix}, \qquad a,b \in \mathbb{Z},$$
since $V - V^{T} = \begin{pmatrix} 0 & 1 \\ -1 & 0\end{pmatrix}$ has determinant $1$. Then
$$\Delta_K(t) = \det(V - tV^{T}) = \det \begin{pmatrix} a(1-t) & 1 \\ -t & b(1-t)\end{pmatrix} = ab(1-t)^2 + t .$$
Writing $n = ab \in \mathbb{Z}$,
$$\Delta_K(t) = n t^2 - (2n-1)t + n, \qquad \Delta_K(1) = 1 \ \checkmark, \qquad \Delta_K(-1) = 4n-1 \ (\text{odd}) .$$
Examples: $n=1$ gives the trefoil $t^2-t+1$; $n=-1$ gives the figure-eight $-t^2+3t-1 \doteq t^2-3t+1$.

**Roots.** For $n \ne 0$,
$$z_{\pm} = \frac{(2n-1) \pm \sqrt{(2n-1)^2 - 4n^2}}{2n} = \frac{(2n-1) \pm \sqrt{1-4n}}{2n}.$$

*Case $n \ge 1$ (discriminant $1-4n < 0$).* The roots are a complex conjugate pair with
$$\operatorname{Re}(z_\pm) = \frac{2n-1}{2n} = 1 - \frac{1}{2n} \in \Big[\tfrac12, 1\Big), \qquad z_+ z_- = \frac{n}{n} = 1 \Rightarrow |z_\pm| = 1 .$$
The roots lie on the unit circle with real part at least $\tfrac12$; the minimum $\tfrac12$ is attained by the trefoil ($n=1$, roots $e^{\pm i\pi/3}$).

*Case $n \le -1$ (discriminant $1-4n \ge 5 > 0$).* The roots are real, with
$$z_+ + z_- = \frac{2n-1}{n} = 2 - \frac1n \in (2,3], \qquad z_+ z_- = 1 .$$
Positive sum and positive product force **both roots positive real**. For the figure-eight ($n=-1$): $z_\pm = \frac{3\pm\sqrt5}{2} \approx 2.618,\ 0.382$.

In every case $\operatorname{Re}(z) \ge \tfrac12 > -1$, so Hoste's conjecture holds for all genus-one knots, with a margin of $\tfrac32$.

**Why this does not generalize.** The proof used only that $2n-1$ and $n$ are linked by $\Delta_K(1)=1$ — i.e. one linear relation among two unknown coefficients. At genus $g$, $\Delta_K$ has $g+1$ free coefficients $a_0,\dots,a_g$ (the rest fixed by reciprocity) constrained by the single equation
$$a_g + 2\sum_{i=0}^{g-1} a_i = \pm 1 .$$
For $g=1$ this determines the polynomial up to one integer parameter and the roots can be written down. For $g \ge 2$ the solution set is a lattice of dimension $g$, and no known argument shows that the disk $|z+\tfrac12| \le \tfrac12$ stays root-free across it. That is precisely the gap of Section 6.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*