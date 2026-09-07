---
id: 03-geometry/bombieri-lang-conjecture
title: "Bombieri-Lang Conjecture"
topic: 03-geometry
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Bombieri-Lang Conjecture

> **Topic:** Algebraic & Differential Geometry · **ID:** `03-geometry/bombieri-lang-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Let $X$ be a smooth projective variety of general type defined over a number field $K$. The Bombieri–Lang conjecture asserts that the $K$-rational points of $X$ are **not Zariski dense**:
$$\overline{X(K)}^{\mathrm{Zar}} \neq X .$$

The strong (Lang) form asserts more: there is a proper closed subvariety $\mathrm{Sp}(X) \subsetneq X$, the **special locus**, independent of the field, such that for every number field $L \supseteq K$ the set $X(L) \setminus \mathrm{Sp}(X)$ is **finite**. Lang further conjectured that $\mathrm{Sp}(X)$ equals the Zariski closure of the union of all images of non-constant rational maps $A \dashrightarrow X$ from abelian varieties, and equals the algebraic-hyperbolicity exceptional locus (the closure of the union of all non-constant holomorphic images $\mathbb{C} \to X(\mathbb{C})$).

A complete proof must produce, for arbitrary $X$ of general type and arbitrary number field, a proper closed subset containing all but finitely many rational points. A disproof would exhibit one smooth projective variety of general type over some number field with a Zariski-dense set of rational points. The case $\dim X = 1$ is Faltings' theorem (Mordell's conjecture); every case with $\dim X \geq 2$ that is not reducible to abelian varieties is open.

## 2. Mathematical Foundations

**General type.** For $X$ smooth projective of dimension $n$ over a field of characteristic $0$, with canonical bundle $\omega_X = \wedge^n \Omega^1_X$, the Kodaira dimension is
$$\kappa(X) = \limsup_{m \to \infty} \frac{\log \dim H^0(X, \omega_X^{\otimes m})}{\log m} \in \{-\infty, 0, 1, \dots, n\},$$
and $X$ is of **general type** iff $\kappa(X) = n$, equivalently $h^0(\omega_X^{\otimes m}) \sim c\, m^n$ with $c>0$, equivalently $\omega_X$ is big. For curves this is $g \geq 2$; for surfaces it is the last class of the Enriques–Kodaira classification.

**Heights.** Fix an ample $L$ on $X$ and a Weil height $h_L : X(\overline{\mathbb{Q}}) \to \mathbb{R}$, well defined up to $O(1)$ by
$$h_L(x) = \frac{1}{[K:\mathbb{Q}]}\sum_{v \in M_K} n_v \log \max_i \|s_i(x)\|_v .$$
Northcott: $\{x \in X(K) : h_L(x) \leq B\}$ is finite. So finiteness statements reduce to height upper bounds.

**Vojta's conjecture** (the analytic/arithmetic engine). For $X$ smooth projective over $K$, $D$ a normal crossings divisor, $A$ ample, $S$ a finite set of places, $\varepsilon > 0$: there is a proper closed $Z \subsetneq X$ with
$$m_S(x, D) + h_{K_X}(x) \leq \varepsilon\, h_A(x) + O(1) \qquad \text{for all } x \in X(K)\setminus Z,$$
where $m_S$ is the proximity function. Taking $D = 0$ and $X$ of general type ($h_{K_X} \geq c\, h_A - O(1)$ off a closed set) yields a bounded height on $X(K)\setminus Z$, hence Bombieri–Lang by Northcott. Vojta's conjecture is the function-field/Nevanlinna analogue of the Second Main Theorem, $T_f(r) + N^{(1)}_f(r,D) \le_{\mathrm{exc}} N_f(r,D) + O(\log r)$.

**Green–Griffiths–Lang (analytic counterpart).** If $X/\mathbb{C}$ is of general type, all entire curves $f : \mathbb{C} \to X$ lie in a proper closed subset; if $X$ is moreover Brody hyperbolic (no non-constant $f$), then $\mathrm{Sp}(X)=\emptyset$ and $X(K)$ should be finite.

**Geometric (function-field) form.** For $K = k(B)$, $k$ algebraically closed of characteristic $0$, $B$ a smooth curve, and $X/K$ smooth projective of general type: either $X(K)$ is non-dense, or $X$ descends (after base change) to a variety over $k$ — the isotriviality escape clause.

## 3. History & State of the Art (SOTA)

- **1974.** Bombieri raised the surface case ($\kappa(X)=2 \Rightarrow X(K)$ non-dense) in a seminar at the University of Chicago; the statement circulated unpublished.
- **1974–1986.** Lang, independently and in a much wider frame, formulated the conjecture together with its hyperbolic and Mordell–Lang siblings; the definitive exposition is *Hyperbolic and Diophantine analysis*, Bull. AMS **14** (1986), which sets out the trichotomy "general type $\Leftrightarrow$ non-dense rational points $\Leftrightarrow$ degeneracy of entire curves".
- **1983.** Faltings proves the Mordell conjecture — the $n=1$ case — via the Shafarevich conjecture and Arakelov/Tate isogeny arguments.
- **1987/1991.** Vojta's thesis reframes Diophantine approximation as value distribution and states the master inequality; Vojta then gives a second proof of Mordell by Arakelov-theoretic Thue–Siegel–Roth methods.
- **1991–1994.** Faltings proves the Mordell–Lang conjecture for subvarieties of abelian varieties; Vojta (1996) extends to semiabelian varieties; McQuillan (1995) generalizes further.
- **1997.** Caporaso, Harris and Mazur show that the weak Bombieri–Lang conjecture implies **uniform** bounds $N(g,K)$ on $|C(K)|$ for all curves of genus $g$ over $K$ — a startling consequence that made the conjecture a load-bearing hypothesis.
- **2000s–2020s.** Progress is concentrated in the geometric (function-field) setting and in cases with ample or positive cotangent bundle.

No case of the conjecture over a number field is known outside varieties mapping to (semi)abelian varieties.

## 4. Partial Results / Verified Cases

| Case | Result |
|---|---|
| $\dim X = 1$, $g \ge 2$ | Faltings (1983): $X(K)$ finite. Complete. |
| $X \subseteq A$ closed subvariety of an abelian variety | Faltings (1991, 1994): $X(K)$ is a finite union of translates of subgroups; if $X$ contains no translate of a positive-dimensional abelian subvariety then $X(K)$ is finite. Gives BL for all $X$ of general type admitting a finite map to an abelian variety. |
| $X \subseteq G$ semiabelian | Vojta (1996), McQuillan (1995): same structure theorem, with $S$-integral points. |
| $\Omega^1_X$ ample and globally generated | Moriwaki (1995): $X(K)$ finite for any number field $K$ — the only unconditional non-abelian number-field case. |
| $\Omega^1_X$ ample, function fields | Noguchi (1985) and Martin-Deschamps (1984): non-density / rigidity results over $k(B)$. |
| Geometric BL, subvarieties of abelian varieties | Raynaud, Hrushovski, Buium (Mordell–Lang over function fields, incl. char $p$). |
| Geometric BL, general | Xie–Yuan, *Partial heights, entire curves, and the geometric Bombieri–Lang conjecture* (arXiv 2107.02185): proves geometric BL for varieties of general type whose Albanese-type / partial-height geometry is controlled — notably for $X$ with a finite map to a semiabelian variety, and gives new non-density criteria *(frontier — verify)*. |
| Characteristic $p$ | The geometric conjecture is **false**: unirational surfaces of general type (e.g. certain Fermat and Zariski surfaces) carry dense rational points. |
| Bogomolov-type height statement | Ullmo (1998) and Zhang (1998) prove the Bogomolov conjecture: points of small canonical height on a curve of genus $\geq 2$ in its Jacobian are finite — a metric shadow of BL. |

## 5. Principal Obstacles

- **No height machine for non-abelian $X$.** Faltings' method needs the group law of $A$: it uses multiplication-by-$m$ to amplify, Mumford's gap principle, and the product/Vojta divisor on $A^m$ with an explicit Néron–Tate quadratic height. A general variety of general type has no such $\mathbb{Z}$-action and no quadratic height; the amplification step has no substitute.
- **$K_X$ is big, not ample or nef.** General type only guarantees $K_X^{\otimes m} = A + E$ for large $m$; the effective part $E$ can be arbitrarily complicated. Vojta's inequality then holds only outside an unknown $Z$, and no known argument makes $Z$ effective or even proves it proper.
- **Failure of jet/Green–Griffiths machinery in dimension $\ge 3$.** Demailly's holomorphic Morse inequalities produce jet differentials only when $c_1^n$-type numerical inequalities hold; for generic hypersurfaces degree bounds (Diverio–Merker–Rousseau, Siu, Brotbek, Riedl–Yang) are astronomically large or require high degree, and jet differentials give *analytic* degeneracy without any arithmetic transfer.
- **No arithmetic Nevanlinna dictionary.** The analogy Second Main Theorem $\leftrightarrow$ Vojta's inequality is heuristic. The known "unit equation"-style inputs (Schmidt subspace theorem, Corvaja–Zannier) apply only when the divisor has many components, which a general type variety with $\rho = 1$ does not supply.
- **Positive-characteristic counterexamples** show any proof must use characteristic-zero-specific input (resolution, Hodge theory, Kobayashi metrics), ruling out purely formal or model-theoretic arguments that work uniformly.
- **Uniformity consequences.** Since BL implies uniform bounds on $|C(K)|$ for all genus-$g$ curves (Caporaso–Harris–Mazur), any proof is at least as strong as a result no current method approaches; conversely a counterexample to uniformity would disprove BL.

## 6. The Gap

Proven: non-density (indeed finiteness off the special locus) whenever the variety embeds in a commutative algebraic group, or when $\Omega^1_X$ is ample and globally generated. General statement: arbitrary $X$ with $\kappa(X)=\dim X$.

The exact missing step is a **height inequality on a variety with no group structure**: given $X$ of general type over $K$, produce an effective proper closed $Z \subsetneq X$ and constants $c>0$, $C$ with
$$h_A(x) \leq C \quad\text{for all } x \in X(K) \setminus Z,$$
equivalently establish Vojta's conjecture with $D=0$. Even the weakest unresolved instance — a simply connected smooth surface $S \subset \mathbb{P}^3$ of degree $\ge 5$ over $\mathbb{Q}$, where $\pi_1 = 0$ kills every map from an abelian variety and $\Omega^1_S$ is not ample (it contains lines) — is completely open: nobody can rule out a Zariski-dense set of rational points on $x^5+y^5+z^5+w^5=0$.

## 7. Current Research (as of June 2026)

- **Function-field breakthroughs.** Xie and Yuan's partial-height technique (arXiv 2107.02185, and follow-ups on the geometric Bombieri–Lang and geometric Lang conjectures) is the most active thread: it builds height functions attached to non-ample partial polarizations and bootstraps non-density; extensions to more general fibrations are being pursued *(frontier — verify)*.
- **Hyperbolicity of hypersurfaces.** Brotbek's Wronskian method, Demailly's jet-metric estimates, and the Riedl–Yang degeneracy bounds continue to sharpen degree thresholds for Kobayashi hyperbolicity of generic hypersurfaces in $\mathbb{P}^n$ (Grenoble, Northwestern, IHES circles).
- **Uniform Mordell.** Dimitrov–Gao–Habegger and Kühne's uniform Bogomolov theorem give uniform bounds $|C(K)| \le c(g)^{1+\mathrm{rk}\,J(K)}$ for curves — the first unconditional realization of a CHM-style consequence, driving hope that similar equidistribution/Betti-rank arguments extend to higher-dimensional subvarieties of abelian schemes.
- **$p$-adic and Chabauty–Kim.** Kim's non-abelian Chabauty and quadratic Chabauty (Balakrishnan–Dogra–Müller–Tuitman–Vonk) give effective results for curves; higher-dimensional analogues over $\mathbb{Q}_p$ for surfaces of general type are being explored.
- **Model theory / o-minimality.** Pila–Wilkie counting and the Zilber–Pink programme (Gao, Klingler, Ullmo–Yafaev) supply unlikely-intersection tools that reprove Mordell–Lang cases and may be adaptable when $X$ maps to a Shimura variety.

## 8. Future Work

- Prove Vojta's height inequality for a single class of simply connected surfaces of general type — e.g. surfaces with $c_1^2 > 2c_2$, where Bogomolov's theorem gives symmetric differentials.
- Extend the partial-height method from function fields to number fields by replacing degrees on curves with Arakelov intersection numbers.
- Make the special locus $\mathrm{Sp}(X)$ effective for concrete families (Fermat surfaces, complete intersections), where the union of rational and elliptic curves can be enumerated.
- Establish the Green–Griffiths–Lang conjecture in dimension $3$ unconditionally, then look for an arithmetic transfer principle.
- Test uniformity numerically: search for genus-$2$ curves over $\mathbb{Q}$ with very many rational points; a sequence with $|C(\mathbb{Q})| \to \infty$ would disprove BL.

## 9. Key References

- **[Foundational]** S. Lang. *Hyperbolic and Diophantine analysis.* Bulletin of the American Mathematical Society **14** (1986), 159–205.
- **[Foundational]** G. Faltings. *Endlichkeitssätze für abelsche Varietäten über Zahlkörpern.* Inventiones Mathematicae **73** (1983), 349–366.
- **[Foundational]** G. Faltings. *Diophantine approximation on abelian varieties.* Annals of Mathematics **133** (1991), 549–576; and *The general case of S. Lang's conjecture*, in Barsotti Symposium in Algebraic Geometry, Academic Press, 1994.
- **[Foundational]** P. Vojta. *Diophantine Approximations and Value Distribution Theory.* Lecture Notes in Mathematics 1239, Springer, 1987.
- **[SOTA]** P. Vojta. *Integral points on subvarieties of semiabelian varieties, I.* Inventiones Mathematicae **126** (1996), 133–181.
- **[SOTA]** L. Caporaso, J. Harris, B. Mazur. *Uniformity of rational points.* Journal of the AMS **10** (1997), 1–35.
- **[SOTA]** A. Moriwaki. *Remarks on rational points of varieties whose cotangent bundles are generated by global sections.* Mathematical Research Letters **2** (1995), 113–118.
- **[SOTA / Recent]** J. Xie, X. Yuan. *Partial heights, entire curves, and the geometric Bombieri–Lang conjecture.* arXiv:2107.02185.
- **[SOTA / Recent]** V. Dimitrov, Z. Gao, P. Habegger. *Uniformity in Mordell–Lang for curves.* Annals of Mathematics **194** (2021), 237–298.
- **[Survey]** E. Bombieri, W. Gubler. *Heights in Diophantine Geometry.* Cambridge University Press, 2006.
- **[Survey]** M. Hindry, J. Silverman. *Diophantine Geometry: An Introduction.* Graduate Texts in Mathematics 201, Springer, 2000.
- **[Survey]** J.-P. Demailly. *Hyperbolic algebraic varieties and holomorphic differential equations.* Acta Mathematica Vietnamica **37** (2012), 441–512.

## 10. Worked Example / Concrete Special Case

Take the Fermat quintic surface
$$S : x^5 + y^5 + z^5 + w^5 = 0 \subset \mathbb{P}^3_{\mathbb{Q}} .$$

**Step 1 — general type.** For a smooth surface of degree $d$ in $\mathbb{P}^3$, adjunction gives $\omega_S = \mathcal{O}_S(d-4)$. With $d=5$, $\omega_S = \mathcal{O}_S(1)$ is ample, so $\kappa(S)=2$: $S$ is of general type. Its invariants: $K_S^2 = d(d-4)^2 = 5$, $p_g = \binom{d-1}{3} = 4$, $\chi(\mathcal{O}_S) = 5$, and $\pi_1(S) = 1$ by Lefschetz. Simple connectivity means there is **no** non-constant map from an abelian variety into $S$ that factors through an Albanese — Faltings' theorem gives nothing here.

**Step 2 — the special locus.** $S$ contains lines. Writing the equation as $(x^5+y^5) + (z^5+w^5) = 0$, take $\zeta,\xi$ with $\zeta^5 = \xi^5 = -1$; then
$$L_{\zeta,\xi} : \{ x = \zeta y,\ z = \xi w \}$$
lies on $S$. There are $3$ ways to pair up the four coordinates and $5 \times 5$ choices of $(\zeta,\xi)$, giving $3d^2 = 75$ lines. Each $L \cong \mathbb{P}^1$ has infinitely many points over its field of definition.

**Step 3 — rational points.** For $d=5$ odd, $\zeta = \xi = -1$ is rational, so
$$L_0 = \{ x = -y,\ z = -w \} = \{ [t : -t : s : -s] \} \subset S(\mathbb{Q}),$$
an infinite set: $|\{P \in L_0(\mathbb{Q}) : h(P) \le B\}| \asymp e^{2B}$ by Schanuel. Three such rational lines exist (one per pairing).

**Step 4 — what BL predicts.** $\mathrm{Sp}(S)$ contains the $75$ lines. The conjecture asserts $S(\mathbb{Q}) \setminus \mathrm{Sp}(S)$ is **finite**: all but finitely many rational solutions of $x^5+y^5+z^5+w^5=0$ lie on one of the three rational lines. Numerical searches up to height $10^5$ have found only the line solutions plus sporadic points, consistent with the prediction, but nothing is proved: no method today rules out a Zariski-dense set of rational points on $S$. This single surface is a minimal open instance of the conjecture.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*