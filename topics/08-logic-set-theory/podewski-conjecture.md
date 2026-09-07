---
id: 08-logic-set-theory/podewski-conjecture
title: "Podewski Conjecture"
topic: 08-logic-set-theory
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Podewski Conjecture

> **Topic:** Mathematical Logic & Set Theory · **ID:** `08-logic-set-theory/podewski-conjecture` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

**Conjecture (Podewski).** Every minimal field is algebraically closed.

Here a *field* $K$ is **minimal** if the structure $(K;+,\cdot,0,1)$ is minimal as a first-order structure: every subset of $K$ definable with parameters from $K$ by a first-order formula in the language of rings is finite or cofinite.

Two points fix the strength of the statement.

- Minimality is imposed on the **single model** $K$, not on its theory. If one instead demands that every model of $\operatorname{Th}(K)$ be minimal — *strong minimality* — the conjecture is a classical theorem (Section 4). Podewski's question is exactly what survives when uniformity across models, and with it all of stability theory's machinery, is removed.
- No cardinality, stability, NIP, or definability-of-a-valuation hypothesis is assumed.

A complete resolution is either (i) a proof that $K=K^{\mathrm{alg}}$ for every minimal $K$, or (ii) an explicit minimal field $K$ with $K \neq K^{\mathrm{alg}}$ — necessarily of characteristic $0$, by Wagner's theorem.

## 2. Mathematical Foundations

**Definable sets.** For $\varphi(x,\bar y)$ a ring formula and $\bar a \in K^{m}$, put $\varphi(K,\bar a)=\{b\in K : K \models \varphi(b,\bar a)\}$. $K$ is minimal iff for all such $\varphi,\bar a$, either $|\varphi(K,\bar a)|<\aleph_0$ or $|K\setminus\varphi(K,\bar a)|<\aleph_0$. $K$ is **strongly minimal** if every $L \equiv K$ is minimal.

**Coset lemma (the engine of the subject).** Let $G$ be an infinite group definable in a minimal structure with $G \subseteq K^{1}$, and $H \leq G$ definable and infinite. Then $H$ is cofinite; if $a \notin H$, the coset $aH$ is infinite and disjoint from $H$, contradicting cofiniteness. Hence

$$H \leq G \text{ definable and infinite} \;\Longrightarrow\; H = G .$$

**Consequences for a minimal field $K$** (all immediate from the coset lemma, since images of definable maps are definable):

1. *Multiplicative divisibility.* For $n\geq 1$, $\pi_n : K^\times \to K^\times,\; x \mapsto x^{n}$ has kernel $\mu_n(K)$ of size $\leq n$, so $(K^\times)^{n}$ is infinite and definable, hence
$$(K^{\times})^{n} = K^{\times} \quad \text{for all } n \geq 1 .$$
In particular $K$ is quadratically closed and therefore **not formally real** (in an ordered field $[K^\times:(K^\times)^2]\geq 2$).
2. *Perfection.* If $\operatorname{char} K = p > 0$, Frobenius $x\mapsto x^{p}$ is an injective endomorphism of $(K,+)$, so $K^{p}$ is an infinite definable additive subgroup, whence $K^{p}=K$: $K$ is perfect.
3. *No Artin–Schreier extensions.* If $\operatorname{char} K = p>0$, the additive map $\wp(x)=x^{p}-x$ has kernel $\mathbb{F}_p$, so $\wp(K)$ is infinite definable, hence
$$\wp(K) = K ,$$
and by Artin–Schreier theory $K$ has no Galois extension of degree $p$.
4. *No proper definable subring or valuation ring.* A subring $R \subsetneq K$ with $|R| = \infty$ is an infinite definable additive subgroup, so $R=K$. Hence no nontrivial **definable** valuation exists on a minimal field.

**Classical inputs.** *Artin–Schreier theorem:* if $1 < [K^{\mathrm{alg}}:K] < \infty$ then $\operatorname{char}K = 0$, $[K^{\mathrm{alg}}:K]=2$, and $K$ is real closed. Combined with (1), a non-algebraically-closed minimal field has **infinite** absolute Galois group $G_K = \operatorname{Gal}(K^{\mathrm{sep}}/K)$. *Kummer theory:* if $\mu_\ell \subseteq K$ and $\ell \neq \operatorname{char}K$, cyclic degree-$\ell$ extensions of $K$ correspond to $K^\times/(K^\times)^\ell$, which is trivial by (1).

## 3. History & State of the Art (SOTA)

- **1971.** Macintyre proves every $\omega$-stable (equivalently, for fields, $\aleph_1$-categorical) field is algebraically closed. This settles the *strongly minimal* case, since a strongly minimal field is $\omega$-stable of Morley rank $1$.
- **1973.** Klaus-Peter Podewski studies minimal rings and raises the conjecture for minimal fields, deliberately dropping any elementary-class hypothesis.
- **1975.** Reineke proves the companion statement for groups: **every minimal group is abelian**. This showed the naked coset argument is genuinely powerful and made the field case look tractable.
- **1980.** Cherlin and Shelah extend Macintyre: superstable fields are algebraically closed; superstable division rings are commutative.
- **1998.** Wagner proves *small* fields (countably many types over finite sets) of characteristic $p>0$ are algebraically closed.
- **2000.** Wagner, *Minimal fields* (JSL 65): **every minimal field of characteristic $p>0$ is algebraically closed.** This is the state of the art; characteristic $0$ remains open after 25 years.
- **2010–2021.** The problem migrates into the "tame fields" programme: Junker–Koenigsmann's *slim fields*, Kaplan–Scanlon–Wagner on Artin–Schreier extensions in NIP fields, Johnson's classification of dp-minimal and dp-finite fields. Each supplies a characteristic-$0$ classification under a *combinatorial tameness* hypothesis that minimality alone does not supply.

## 4. Partial Results / Verified Cases

| Hypothesis added to minimality | Conclusion | Source |
|---|---|---|
| $\operatorname{char} K = p > 0$ | $K = K^{\mathrm{alg}}$ | Wagner 2000 |
| Strong minimality (all models minimal) | $K = K^{\mathrm{alg}}$ | Macintyre 1971 |
| $\omega$-stable / superstable | $K = K^{\mathrm{alg}}$ | Macintyre 1971; Cherlin–Shelah 1980 |
| Small, $\operatorname{char}=p>0$ | $K = K^{\mathrm{alg}}$ | Wagner 1998 |
| dp-minimal | $K = K^{\mathrm{alg}}$ | derived: Johnson's trichotomy (ACF / RCF / henselian) plus §2(1),(4) |
| Superrosy of finite rank | $K = K^{\mathrm{alg}}$ | derived from Krupiński–Pillay 2014 |

Unconditional facts about any minimal $K$: $K^{\times}$ is divisible; $K$ is perfect and quadratically closed; $K$ is not orderable; $K$ admits no definable nontrivial valuation ring and no infinite proper definable subring; $K$ is infinite; $|G_K| = \infty$ if $K \neq K^{\mathrm{alg}}$; $K$ has no cyclic extension of prime degree $\ell$ with $\mu_\ell \subseteq K$; and in characteristic $p$, no degree-$p$ extension.

## 5. Principal Obstacles

- **No transfer to elementary extensions.** Minimality is not preserved by $\equiv$. Compactness, indiscernibles, forking, and Morley rank — every standard tool — is a statement about a theory, not a model, and is unavailable.
- **Minimality controls only $K^{1}$.** Nothing is assumed about definable subsets of $K^{n}$, $n \geq 2$, or of imaginary sorts. There is no elimination of imaginaries, no definable dimension, and no "generic element" to work with.
- **Failure of descent to $K(\zeta_\ell)$.** The natural route in characteristic $0$ is: to kill a degree-$\ell$ extension by Kummer theory one must first adjoin $\zeta_\ell$. But $L=K(\zeta_\ell)$ lives on $K^{d}$, $d = [L:K]$, and minimality of $K$ says nothing about definable subsets of $K^{d}$. So $L^{\times}$ need not be divisible, and the argument stalls at the first step.
- **No characteristic-$0$ analogue of $\wp$.** In characteristic $p$ the map $\wp(x)=x^p-x$ is *additive* with *finite* kernel, so the coset lemma applies directly and kills degree-$p$ extensions without any roots of unity. In characteristic $0$ the additive group is torsion-free divisible and carries no definable finite-kernel endomorphism whose surjectivity encodes Galois data. Cyclic extensions of degree $\ell$ with $\mu_\ell \not\subseteq K$ are simply invisible to the multiplicative group of $K$.
- **Hrushovski's warning.** The 1993 construction of a new strongly minimal set shows minimal geometries need not be classical; there is no a priori reason a minimal structure carries an algebraic-geometry-like dimension theory that one could import.

## 6. The Gap

Proven: a minimal field $K$ has divisible $K^{\times}$, is perfect and quadratically closed, is not real closed, and — in characteristic $p$ — has trivial $G_K$.

Open: characteristic $0$. Reduced to a sharp statement:

> Let $K$ be a minimal field of characteristic $0$ and $\ell$ an odd prime with $\zeta_\ell \notin K$. Show that $K$ has no Galois extension of degree $\ell$.

Equivalently: exclude the possibility that $G_K$ is an infinite profinite group all of whose finite quotients are realized by extensions generated over $K(\zeta_\ell)$ rather than over $K$. The missing step is a **descent principle**: some mechanism transporting the minimality of $K$ to finite algebraic extensions $L/K$, or an interpretation of $L^\times/(L^\times)^\ell$ inside a definable subset of $K^{1}$ where the coset lemma bites. No such mechanism is known without a rank or a tameness hypothesis.

## 7. Current Research (as of June 2026)

- **Lyon (Institut Camille Jordan, Wagner's school).** Continued work on fields with restricted definable subgroup lattices; the characteristic-$p$ proof is treated as the template, with attempts to substitute a definable-Galois-cohomology argument for $\wp$.
- **Wrocław (Krupiński and collaborators).** Rosy/small-field techniques and definable topological-dynamics methods, aimed at supplying the missing dimension theory. *(frontier — verify)*
- **Fudan / Berkeley lineage (Johnson).** The dp-finite classification programme continues to sharpen "no definable valuation $\Rightarrow$ algebraically closed" statements; the open task is to remove finiteness-of-dp-rank. *(frontier — verify)*
- **NIP fields programme (Halevi–Hasson–Jahnke and others).** Under the conjectural classification of strongly dependent fields, minimality plus NIP forces algebraic closure. Whether *every* minimal field is NIP is itself open and is currently the most-discussed intermediate target. *(frontier — verify)*
- **Quasi-minimal analogues.** Zilber-style quasi-minimal classes (pseudo-exponentiation) supply characteristic-$0$ minimal-like fields that *are* algebraically closed, taken as weak evidence for the conjecture.

## 8. Future Work

1. **Prove or refute "minimal $\Rightarrow$ NIP".** A positive answer, plus the NIP-fields classification, would close the conjecture.
2. **Find a definable substitute for $K(\zeta_\ell)$.** Represent degree-$\ell$ cyclic extensions by a *one-variable* definable family over $K$ (e.g. via norm forms or Brauer-group torsors coded on $K^1$), so the coset lemma applies.
3. **Analyse $(K,+)$ in characteristic $0$.** Classify definable additive endomorphisms; show that minimality forces $K$ to be the fixed field of nothing, or extract a contradiction from an infinite $G_K$ acting on divisible $K^\times$.
4. **Attempt a construction.** Build, by transfinite induction, a characteristic-$0$ field of size $\aleph_1$ that is minimal but not algebraically closed — the Hrushovski-amalgamation route. No serious obstruction to such a construction has been published, and no construction has succeeded.
5. **Settle the ring case.** Podewski's original setting: classify all minimal rings, not just fields.

## 9. Key References

- **[Foundational]** K.-P. Podewski. *Minimale Ringe.* Mathematisch-Physikalische Semesterberichte, 1973. (Origin of the conjecture.)
- **[Foundational]** J. Reineke. *Minimale Gruppen.* Zeitschrift für Mathematische Logik und Grundlagen der Mathematik 21 (1975), 357–359.
- **[Foundational]** A. Macintyre. *On $\omega_1$-categorical theories of fields.* Fundamenta Mathematicae 71 (1971), 1–25.
- **[Foundational]** G. Cherlin, S. Shelah. *Superstable fields and groups.* Annals of Mathematical Logic 18 (1980), 227–270.
- **[SOTA]** F. O. Wagner. *Minimal fields.* The Journal of Symbolic Logic 65 (2000), 1833–1835.
- **[SOTA]** F. O. Wagner. *Small fields.* The Journal of Symbolic Logic 63 (1998), 995–1002.
- **[Recent]** M. Junker, J. Koenigsmann. *Schlanke Körper (Slim fields).* The Journal of Symbolic Logic 75 (2010), 481–500.
- **[Recent]** I. Kaplan, T. Scanlon, F. O. Wagner. *Artin–Schreier extensions in NIP and simple fields.* Israel Journal of Mathematics 185 (2011), 141–153.
- **[Recent]** W. Johnson. *Fun with Fields.* PhD thesis, University of California, Berkeley, 2016.
- **[Recent]** K. Krupiński, A. Pillay. *Superrosy fields and valuations.* Annals of Pure and Applied Logic 165 (2014), 1256–1273.
- **[Recent]** Y. Halevi, A. Hasson, F. Jahnke. *A conjectural classification of strongly dependent fields.* The Bulletin of Symbolic Logic 25 (2019), 182–195.
- **[Survey]** F. O. Wagner. *Simple Theories.* Kluwer Academic Publishers, 2000.
- **[Survey]** D. Marker. *Model Theory: An Introduction.* Springer GTM 217, 2002. (Minimality, strong minimality, ACF.)
- **[Context]** E. Hrushovski. *A new strongly minimal set.* Annals of Pure and Applied Logic 62 (1993), 147–166.

## 10. Worked Example / Concrete Special Case

**Claim.** A minimal field $K$ with $\operatorname{char} K = 3$ has no Galois extension of degree $3$, and no quadratic extension.

*Step 1 — $K$ is infinite.* A finite field $\mathbb{F}_q$ is minimal vacuously but is excluded: every element is definable, and the conjecture is stated for infinite fields (a finite field is not algebraically closed, so the convention matters). Assume $|K|=\infty$.

*Step 2 — kill degree $3$.* Define $\wp: K \to K$, $\wp(x)=x^{3}-x$. It is additive:
$$\wp(x+y)=(x+y)^{3}-(x+y)=x^{3}+y^{3}-x-y=\wp(x)+\wp(y),$$
using $(x+y)^3 = x^3+y^3$ in characteristic $3$. Its kernel is $\{x: x^3=x\}=\mathbb{F}_3$, of size $3$. So the image $\wp(K)$ is a subgroup of $(K,+)$, definable by $\exists x\,(x^{3}-x=y)$, and infinite (it is $K/\mathbb{F}_3$ in bijection, so $|\wp(K)|=|K|$). By minimality $\wp(K)$ is cofinite. If some $a \notin \wp(K)$, then the coset $a+\wp(K)$ is infinite and disjoint from $\wp(K)$, contradicting cofiniteness. Hence $\wp(K)=K$. Artin–Schreier theory: degree-$3$ Galois extensions of $K$ are exactly $K(\alpha)$ with $\alpha^{3}-\alpha = a$ and $a \notin \wp(K)$. There are none.

*Step 3 — kill degree $2$.* The set of squares $S=\{y : \exists x\; x^{2}=y\}$ is definable. The map $x \mapsto x^2$ on $K^\times$ has kernel $\mu_2(K) = \{1\}$ (characteristic $3 \neq 2$ gives $\mu_2=\{\pm 1\}$, size $2$), so $(K^\times)^2$ is infinite, hence cofinite in $K$, hence — by the same coset argument inside $K^\times$ — equal to $K^\times$. Every element of $K$ is a square, so $X^{2}-a$ is reducible for all $a$: no quadratic extension.

*Step 4 — the sanity check.* $K=\overline{\mathbb{F}_3}$ satisfies all of this: by quantifier elimination in ACF, every definable subset of $\overline{\mathbb{F}_3}$ is a finite Boolean combination of zero sets of one-variable polynomials, hence finite or cofinite. So $\overline{\mathbb{F}_3}$ is minimal, consistent with Wagner's theorem.

*Where characteristic $0$ breaks.* Repeat Step 2 over a hypothetical minimal $K$ of characteristic $0$ and $\ell=5$. There is no additive $\wp$; instead one needs $K^{\times}/(K^{\times})^{5}$ to classify degree-$5$ cyclic extensions, which requires $\zeta_5 \in K$. If $\zeta_5 \notin K$, one passes to $L=K(\zeta_5)$ with $[L:K] \mid 4$. Now $L^{\times}$ is a group definable in $K$ **on the sort $K^{4}$**, and minimality gives no control over definable subsets of $K^{4}$: $(L^\times)^5$ may be a proper infinite subgroup of infinite index for all minimality knows. The proof stops precisely there — this is the gap of Section 6.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*