---
id: 08-logic-set-theory/decidability-of-p-adic-exponential
title: "Decidability of p-adic Exponential"
topic: 08-logic-set-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Decidability of the p-adic Exponential

> **Topic:** Mathematical Logic & Set Theory · **ID:** `08-logic-set-theory/decidability-of-p-adic-exponential` · **Status:** open

## 1. Problem Statement / Conjecture

Fix a prime $p$. The field $\mathbb{Q}_p$ has a decidable elementary theory (Ax–Kochen, Ershov, Cohen). The $p$-adic exponential $\exp_p$ converges only on a small ideal, so "adding $\exp$" splits into three questions of increasing strength:

1. **Restricted case.** Is $\operatorname{Th}(\mathbb{Q}_p, +, \cdot, \exp_p\!\restriction_{p\mathbb{Z}_p})$ decidable? — **Yes**, by Denef–van den Dries (1988). Settled.
2. **Exponential ring case.** Is the $p$-adic exponential ring $(\mathbb{Z}_p, +, \cdot, E)$, $E(x) = \exp_p(px)$, decidable *and* is its theory axiomatised by an effective exponential-algebraic scheme? Known **only modulo a $p$-adic Schanuel conjecture**.
3. **Global case.** Is $\operatorname{Th}(\mathbb{Q}_p, +, \cdot, \log_p)$ decidable, where $\log_p:\mathbb{Q}_p^\times \to \mathbb{Q}_p$ is the total Iwasawa logarithm normalised by $\log_p(p)=0$ (equivalently: $\mathbb{Q}_p$ with $p$-adic powers $x^y = \exp_p(y\log_p x)$)? **Open**, even conditionally in full generality.

The catalogued open problem is (2)+(3): **prove unconditionally that the $p$-adic exponential/logarithm expansions of $\mathbb{Q}_p$ have decidable theory, or show that one of them interprets $(\mathbb{Z},+,\cdot)$ and is therefore undecidable.** A complete resolution means either an explicit decision procedure with a correctness proof from ZFC alone, or an interpretation of Peano arithmetic. This is the $p$-adic mirror of Macintyre–Wilkie's theorem that $\operatorname{Th}(\mathbb{R},\exp)$ is decidable modulo Schanuel's conjecture.

## 2. Mathematical Foundations

**Valued field.** $\mathbb{Q}_p$ carries $v:\mathbb{Q}_p^\times \twoheadrightarrow \mathbb{Z}$, $|x|_p = p^{-v(x)}$, valuation ring $\mathbb{Z}_p = \{v \ge 0\}$, maximal ideal $p\mathbb{Z}_p$, residue field $\mathbb{F}_p$.

**Convergence.** For $x \in \mathbb{Q}_p$, $v(n!) = \frac{n - s_p(n)}{p-1}$, so
$$\exp_p(x) = \sum_{n\ge 0} \frac{x^n}{n!} \quad\text{converges}\iff v(x) > \tfrac{1}{p-1},$$
i.e. on $p\mathbb{Z}_p$ for $p$ odd and $4\mathbb{Z}_2$ for $p=2$. On that domain $\exp_p$ is an isometric group isomorphism
$$\exp_p : (p\mathbb{Z}_p, +) \xrightarrow{\ \sim\ } (1+p\mathbb{Z}_p, \times), \qquad \log_p(1+y) = \sum_{n \ge 1} \frac{(-1)^{n-1}y^n}{n}$$
its inverse. Unlike $\mathbb{R}$, there is **no continuous total** $\exp_p : \mathbb{Q}_p \to \mathbb{Q}_p^\times$: $(\mathbb{Q}_p,+)$ has no proper open subgroup of finite index matching $\mathbb{Q}_p^\times$.

**Iwasawa extension.** $\log_p$ extends uniquely to a homomorphism $\mathbb{Q}_p^\times \to (\mathbb{Q}_p,+)$ with $\log_p p = 0$, using $\mathbb{Q}_p^\times \cong p^{\mathbb{Z}} \times \mu_{p-1} \times (1+p\mathbb{Z}_p)$ ($p$ odd) and $\log_p$ killing the first two factors. Hence
$$\{x \in \mathbb{Q}_p^\times : \log_p x = 0\} = p^{\mathbb{Z}}\cdot \mu_{p-1},$$
so the predicate $p^{\mathbb{Z}}$ is definable from $\log_p$ — and $p^{\mathbb{Z}}$ is **not** definable in the pure field $\mathbb{Q}_p$.

**Languages.** $\mathcal{L}_{\mathrm{Mac}} = \{+,-,\cdot,0,1\} \cup \{P_n\}_{n\ge2}$ with $P_n(x) \leftrightarrow \exists y\, (y^n = x)$; Macintyre (1976): $\mathbb{Q}_p$ admits quantifier elimination in $\mathcal{L}_{\mathrm{Mac}}$. $\mathcal{L}^{D}_{\mathrm{an}}$ adds all restricted analytic functions $f:\mathbb{Z}_p^m\to\mathbb{Z}_p$ given by power series in $\mathbb{Z}_p\langle X_1,\dots,X_m\rangle$ (coefficients $\to 0$) together with division $D(x,y)= x/y$ if $v(x)\ge v(y), y \ne 0$, else $0$.

**Key normalisation.** $\exp_p(px) = \sum_n \frac{p^n}{n!}x^n$ has coefficients $p^n/n! \in \mathbb{Z}_p$ with $v(p^n/n!) \ge n(1 - \frac{1}{p-1}) \to \infty$ for $p \ge 3$. So $E(x)=\exp_p(px)$ **is** a restricted analytic function on $\mathbb{Z}_p$ — this is why case (1) is tractable.

**$p$-adic Schanuel conjecture (pSC).** If $x_1,\dots,x_n \in p\mathbb{Z}_p$ are linearly independent over $\mathbb{Q}$, then
$$\operatorname{trdeg}_{\mathbb{Q}} \mathbb{Q}\big(x_1,\dots,x_n,\exp_p x_1,\dots,\exp_p x_n\big) \ \ge\ n .$$

## 3. History & State of the Art (SOTA)

- **1932.** Mahler proves the $p$-adic Hermite–Lindemann theorem: for algebraic $\alpha \ne 1$ with $|\alpha-1|_p<1$, $\log_p\alpha$ is transcendental. This is pSC for $n=1$.
- **1965.** Ax–Kochen and Ershov: $\operatorname{Th}(\mathbb{Q}_p)$ is decidable and complete relative to the value group and residue field.
- **1967.** Brumer proves the $p$-adic analogue of Baker's theorem: $p$-adic logarithms of algebraic numbers that are $\mathbb{Q}$-linearly independent are $\overline{\mathbb{Q}}$-linearly independent. This is the "linear part" of pSC over $\overline{\mathbb{Q}}$.
- **1969 / 1976.** Cohen gives a primitive-recursive decision procedure; Macintyre gives quantifier elimination with power predicates, making definable sets geometrically usable.
- **1988.** Denef–van den Dries: $\mathbb{Q}_p^{\mathrm{an}}$ eliminates quantifiers in $\mathcal{L}^D_{\mathrm{an}}\cup\{P_n\}$, $p$-adic subanalytic sets are well behaved, and the theory is decidable. Consequence: restricted $\exp_p$ is harmless.
- **1990s–2010s.** Lipshitz's rigid subanalytic sets, Lipshitz–Robinson separated power series, and Cluckers–Lipshitz's axiomatic "fields with analytic structure" give uniform-in-$p$ analytic cell decomposition.
- **1996.** Macintyre–Wilkie: $\operatorname{Th}(\mathbb{R},\exp)$ is decidable assuming Schanuel's conjecture — the template every $p$-adic attempt follows.
- **2010s.** Mariaule transports the template: decidability of $\mathbb{Q}_p$ with a predicate for $\alpha^{\mathbb{Z}}$, and of the $p$-adic exponential ring, conditional on pSC; plus effective model-completeness results for $p$-adic analytic structures.

## 4. Partial Results / Verified Cases

- **Restricted exponential, all $p$:** $\operatorname{Th}(\mathbb{Q}_p, \exp_p\!\restriction_{p\mathbb{Z}_p})$ and $\operatorname{Th}(\mathbb{Q}_p, \log_p\!\restriction_{1+p\mathbb{Z}_p})$ are decidable (Denef–van den Dries 1988). Definable sets are exactly the $p$-adic subanalytic sets; cell decomposition and dimension theory hold.
- **$p=2$ caveat:** the same holds with domain $4\mathbb{Z}_2$; the rescaling $x\mapsto \exp_2(4x)$ restores integral coefficients.
- **Exponential ring $(\mathbb{Z}_p,+,\cdot,E)$:** decidable modulo pSC; the argument mirrors Macintyre–Wilkie, replacing o-minimality by $p$-adic analytic cell decomposition *(frontier — verify against Mariaule's published version)*.
- **Powers predicate:** $\operatorname{Th}(\mathbb{Q}_p, +,\cdot, \alpha^{\mathbb{Z}})$ for $\alpha \in \mathbb{Q}^{\times}$ is decidable modulo pSC; unconditionally, model-completeness holds after adding suitable divisibility predicates.
- **Transcendence input, unconditional:** pSC holds for $n=1$ (Mahler 1932); the $\overline{\mathbb{Q}}$-linear case holds by Brumer (1967); effective versions with explicit constants by Yu Kunrui give bounds on linear forms in $p$-adic logarithms, so *specific* existential sentences with algebraic parameters are decidable one at a time.
- **Existential fragment with one exponential:** sentences of the form $\exists x \in p\mathbb{Z}_p\, \big(f(x,\exp_p x)=0\big)$, $f \in \mathbb{Z}[X,Y]$, are decidable by Newton polygon plus Hensel arguments on the restricted analytic function $f(px, E(x))$.

## 5. Principal Obstacles

- **No o-minimality.** $\mathbb{Q}_p$ is totally disconnected; there is no order to tame definable sets. The Wilkie–Macintyre machinery uses intermediate-value arguments and finiteness of connected components. The $p$-adic replacement — $P$-minimality and analytic cell decomposition — gives finiteness statements only for *restricted* analytic families, not for functions with $p^{\mathbb{Z}}$-type unboundedness.
- **Domain mismatch.** $\exp_p$ is not total, so the "exponential" is a partial function; extending it by a total group homomorphism requires the axiom of choice and gives a non-measurable, wildly non-definable object. Every reasonable totalisation ($E(x)=\exp_p(px)$, or Iwasawa $\log_p$) changes the structure's strength discontinuously.
- **The $p^{\mathbb{Z}}$ hazard.** Total $\log_p$ defines $p^{\mathbb{Z}}\mu_{p-1}$. A predicate for a multiplicative cyclic group is exactly the configuration from which $(\mathbb{Z},+,\cdot)$ is often interpretable; avoiding interpretation of arithmetic requires a *Mann property* / $S$-unit finiteness statement, which for $p$-adic exponentials is precisely the transcendence content of pSC.
- **Transcendence is the bottleneck.** Deciding whether an exponential-polynomial system has a solution reduces to bounding the transcendence degree of $\mathbb{Q}(\bar x, \exp \bar x)$. Unconditionally, only $n=1$ (Mahler) and linear-in-logs (Brumer, Yu) are available; nothing gives the full $n$-variable lower bound.
- **No $p$-adic Ax theorem strong enough.** Ax's differential-algebraic proof of Schanuel for power series works in characteristic $0$ differential fields; $\mathbb{Q}_p$ has no non-trivial continuous derivation, so the differential-algebraic route to a "$p$-adic Ax–Schanuel" over $\mathbb{Q}_p$ itself is blocked.

## 6. The Gap

Proven: quantifier elimination and decidability for **restricted** analytic structure; conditional decidability for the exponential ring and for $\alpha^{\mathbb{Z}}$, where "conditional" means the decision procedure's correctness proof invokes pSC exactly once, to bound the dimension of the solution variety of an exponential-polynomial system.

Missing: an **unconditional** transcendence-degree lower bound of Schanuel type over $\mathbb{Q}_p$, or a substitute that yields only the finiteness statement the decision procedure needs (an effective bound on the number of non-degenerate solutions of $\sum_i \alpha_i \exp_p(\lambda_i x) = 0$). Formally the gap is:

$$\text{pSC for all } n \ \Longrightarrow\ \operatorname{Th}(\mathbb{Z}_p,+,\cdot,E) \text{ decidable}; \qquad \text{currently pSC known only for } n=1 .$$

For the **global** structure $(\mathbb{Q}_p,\log_p)$ the gap is wider: even granting pSC, no quantifier-elimination result is known for the interaction of the total logarithm with the value group, and no interpretation of arithmetic has been ruled out.

## 7. Current Research (as of June 2026)

- **Analytic structures school** (Cluckers, Lipshitz, Halupczok; Leuven/Purdue/Münster): uniform-in-$p$ analytic cell decomposition, Hensel minimality as a replacement for o-minimality. Hensel-minimal expansions have Jacobian and dimension theory; the live question is whether $(\mathbb{Q}_p,\log_p^{\mathrm{Iwasawa}})$ is $1$-h-minimal *(frontier — verify)*.
- **Exponential-algebraic closure** (Kirby, Zilber, Bays; Manchester/Oxford): pseudo-exponential axiomatics adapted to valued fields; a $p$-adic "$E$-field" with a Schanuel-type predimension is under construction.
- **Effective model theory of $\mathbb{Q}_p^{\mathrm{an}}$** (Mariaule and collaborators): making the Denef–van den Dries elimination primitive recursive, a prerequisite for any conditional decision procedure to be genuinely algorithmic.
- **Transcendence side** (Yu Kunrui's estimates; Bombieri–Gubler style $p$-adic subspace theorems): explicit lower bounds for $|\Lambda|_p$ where $\Lambda = \sum \beta_i \log_p \alpha_i$, feeding partial Mann properties.
- **Undecidability side**: attempts to define $\mathbb{Z}$ inside $(\mathbb{Q}_p, \log_p)$ via the definable set $p^{\mathbb{Z}}\mu_{p-1}$; so far these produce only a definable copy of $(\mathbb{Z},+,<)$, which is Presburger and harmless.

## 8. Future Work

- Prove pSC for $n=2$ (already open): transcendence of $\log_p\alpha_1 / \log_p\alpha_2$ is essentially the $p$-adic Gelfond problem.
- Isolate a **weak pSC** sufficient for decidability — a finiteness statement about torsion-free ranks, in the spirit of the uniform Schanuel conjecture of Kirby–Zilber — and prove it unconditionally.
- Establish Hensel minimality (or a suitable $P$-minimality) for the Iwasawa-logarithm expansion, which would immediately give cell decomposition and reduce decidability to a residue-field/value-group computation.
- Settle the **existential** theory of $(\mathbb{Q}_p, \exp_p)$: a $p$-adic exponential Hilbert's tenth problem, likely more accessible than the full theory.
- Uniformity in $p$: is there a single algorithm deciding, given $p$ and a sentence, truth in $(\mathbb{Q}_p, \exp_p\!\restriction)$? Ax–Kochen transfer suggests yes for the restricted case.

## 9. Key References

- **[Foundational]** J. Ax and S. Kochen. *Diophantine problems over local fields I.* American Journal of Mathematics 87 (1965), 605–630.
- **[Foundational]** P. J. Cohen. *Decision procedures for real and p-adic fields.* Communications on Pure and Applied Mathematics 22 (1969), 131–151.
- **[Foundational]** A. Macintyre. *On definable subsets of p-adic fields.* Journal of Symbolic Logic 41 (1976), 605–610.
- **[Foundational]** J. Denef and L. van den Dries. *p-adic and real subanalytic sets.* Annals of Mathematics 128 (1988), 79–138.
- **[Transcendence]** K. Mahler. *Ein Beweis der Transzendenz der P-adischen Exponentialfunktion.* Journal für die reine und angewandte Mathematik 169 (1932), 61–66.
- **[Transcendence]** A. Brumer. *On the units of algebraic number fields.* Mathematika 14 (1967), 121–124.
- **[Transcendence]** Kunrui Yu. *p-adic logarithmic forms and group varieties II.* Acta Arithmetica 89 (1999), 337–378.
- **[Template]** A. Macintyre and A. J. Wilkie. *On the decidability of the real exponential field.* In P. Odifreddi (ed.), *Kreiseliana: About and Around Georg Kreisel*, A K Peters, 1996, 441–467.
- **[Template]** A. J. Wilkie. *Model completeness results for expansions of the ordered field of real numbers by restricted Pfaffian functions and the exponential function.* Journal of the American Mathematical Society 9 (1996), 1051–1094.
- **[SOTA / Recent]** R. Cluckers and L. Lipshitz. *Fields with analytic structure.* Journal of the European Mathematical Society 13 (2011), 1147–1223.
- **[SOTA / Recent]** L. Lipshitz and Z. Robinson. *Rings of separated power series and quasi-affinoid geometry.* Astérisque 264, Société Mathématique de France, 2000.
- **[SOTA / Recent]** N. Mariaule. *The field of p-adic numbers with a predicate for the powers of an integer.* Journal of Symbolic Logic, 2017.
- **[Context]** J. Ax. *On Schanuel's conjectures.* Annals of Mathematics 93 (1971), 252–268.
- **[Survey]** L. Bélair. *Panorama of p-adic model theory.* Annales des sciences mathématiques du Québec 36 (2012), 43–75.
- **[Textbook]** N. Koblitz. *p-adic Numbers, p-adic Analysis, and Zeta-Functions.* 2nd ed., Springer GTM 58, 1984.

## 10. Worked Example / Concrete Special Case

Take $p=3$, so $\exp_3$ is a bijection $3\mathbb{Z}_3 \to 1+3\mathbb{Z}_3$. Consider the $\mathcal{L}\cup\{\exp\}$-sentence

$$\sigma:\quad \exists x,y \in 3\mathbb{Z}_3\ \exists m,n \in \mathbb{Z}_{\ne 0}\ \big(\exp_3(x) = 4 \ \wedge\ \exp_3(y)=10 \ \wedge\ mx = ny\big).$$

$\sigma$ says $\log_3 4 / \log_3 10 \in \mathbb{Q}$. Note $4 = 1+3$ and $10 = 1+3^2$ both lie in $1+3\mathbb{Z}_3$, so $x = \log_3 4$ and $y = \log_3 10$ exist and are unique.

**Step 1 — valuations.** $\log_3(1+u) = u - u^2/2 + \dots$, so $v(x) = v(3) = 1$ and $v(y) = v(9) = 2$. Valuation alone does not refute $\sigma$: $x/y$ could have valuation $-1$, e.g. equal $1/3$.

**Step 2 — transfer to the multiplicative side.** $\exp_3$ and $\log_3$ are mutually inverse isomorphisms of $(3\mathbb{Z}_3,+)$ and $(1+3\mathbb{Z}_3,\times)$, so
$$mx = ny \iff \exp_3(mx)=\exp_3(ny) \iff 4^{m} = 10^{n}.$$

**Step 3 — descend to $\mathbb{Q}$.** Both sides are rational numbers, and equality in $\mathbb{Q}_3$ of rationals is equality in $\mathbb{Q}$. Unique factorisation gives $2^{2m} = 2^{n}5^{n}$, hence $n = 0$ and then $m=0$, contradicting $m,n \ne 0$.

**Conclusion:** $\sigma$ is **false**; $\log_3 4/\log_3 10$ is irrational. In fact Mahler's theorem gives more — $\log_3 4$ is transcendental — and Brumer's theorem upgrades the conclusion to $\overline{\mathbb{Q}}$-linear independence of $\log_3 4$ and $\log_3 10$.

**Why this is the whole problem in miniature.** The decision was made by reducing an exponential sentence to a multiplicative Diophantine fact about algebraic parameters. A general sentence produces systems such as
$$\sum_{i=1}^{k} P_i(x_1,\dots,x_n)\,\exp_3\!\big(\lambda_i(x)\big) = 0,\qquad P_i \in \mathbb{Q}[\bar X],\ \lambda_i \text{ linear},$$
and no elementary factorisation argument bounds their solution sets. What is needed is exactly $\operatorname{trdeg}_{\mathbb{Q}}\mathbb{Q}(\bar x, \exp_3 \bar x)\ge n$ for $\mathbb{Q}$-independent $\bar x$ — the $p$-adic Schanuel conjecture, unproved for every $n \ge 2$.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*