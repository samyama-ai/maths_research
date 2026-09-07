---
id: 04-topology/beilinson-lichtenbaum-conjecture
title: "Beilinson-Lichtenbaum Conjecture"
topic: 04-topology
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Beilinson-Lichtenbaum Conjecture

> **Topic:** Topology & Knot Theory · **ID:** `04-topology/beilinson-lichtenbaum-conjecture` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

Let $X$ be a smooth scheme over a field $k$, and let $m$ be an integer invertible in $k$. Let $\mathbb{Z}(n)$ denote Voevodsky's motivic complex of weight $n$ on the Zariski site of $X$, and let $\pi: X_{\text{ét}} \to X_{\mathrm{Zar}}$ be the change-of-topology morphism. The **Beilinson–Lichtenbaum conjecture** (BL) asserts that the comparison map

$$
H^{p,n}_{\mathcal{M}}(X, \mathbb{Z}/m) \;\longrightarrow\; H^{p}_{\text{ét}}(X, \mu_m^{\otimes n})
$$

is an **isomorphism for $p \le n$** and **injective for $p = n+1$**.

Equivalently, in the derived category of Zariski sheaves,

$$
\mathbb{Z}/m(n) \;\xrightarrow{\ \sim\ }\; \tau^{\le n}\, R\pi_*\, \mu_m^{\otimes n}.
$$

So motivic cohomology with finite coefficients is exactly the *truncation* of étale cohomology below the weight; above the weight the two theories diverge (motivic cohomology of a field vanishes in degrees $p > n$, étale cohomology need not).

A complete proof must establish the isomorphism/injectivity range for all smooth $X/k$, all $n \ge 0$, and all $m$ invertible in $k$. A disproof requires one smooth $X$, one $n$, one $m$, and one degree $p \le n+1$ where the map fails.

**Status.** The conjecture is a **theorem** for smooth varieties over a field, as a consequence of the Bloch–Kato / norm residue isomorphism theorem proved by Rost and Voevodsky (Voevodsky 2003, 2011; write-up completed by Haesemeyer–Weibel 2019). What remains open are the integral, singular, and mixed-characteristic generalizations described in §5–§7.

## 2. Mathematical Foundations

**Motivic complexes.** For $X$ smooth over $k$, $\mathbb{Z}(n) \in D^-(\mathrm{Sh}_{\mathrm{Zar}}(X))$ is Voevodsky's weight-$n$ motivic complex, defined via the Suslin complex of the presheaf with transfers $\mathbb{Z}_{\mathrm{tr}}(\mathbb{G}_m^{\wedge n})[-n]$. Motivic cohomology is bigraded:
$$
H^{p,n}_{\mathcal{M}}(X,\mathbb{Z}) := \mathbb{H}^p_{\mathrm{Zar}}(X, \mathbb{Z}(n)).
$$
Low weights: $\mathbb{Z}(0) = \mathbb{Z}$, $\mathbb{Z}(1) \simeq \mathbb{G}_m[-1]$. For $X = \operatorname{Spec} F$ a field, $H^{n,n}_{\mathcal{M}}(F,\mathbb{Z}) \cong K^M_n(F)$, the Milnor $K$-group, and $H^{p,n}_{\mathcal{M}}(F,\mathbb{Z}) = 0$ for $p > n$ (Nesterenko–Suslin, Totaro).

**Milnor $K$-theory.**
$$
K^M_*(F) = T^*(F^\times)\big/\big\langle a \otimes (1-a) : a \ne 0,1 \big\rangle .
$$

**Norm residue map.** Kummer theory gives $\partial: F^\times/m \xrightarrow{\sim} H^1_{\text{ét}}(F,\mu_m)$. Cup product yields
$$
\chi_{n,m}: K^M_n(F)/m \longrightarrow H^n_{\text{ét}}(F, \mu_m^{\otimes n}), \qquad \{a_1,\dots,a_n\} \mapsto \partial(a_1)\cup\cdots\cup\partial(a_n).
$$

**Bloch–Kato conjecture (BK$(n,\ell)$).** $\chi_{n,m}$ is an isomorphism for every field $F$ with $1/m \in F$.

**Key equivalence.** Suslin–Voevodsky (2000), refined by Geisser–Levine (2001) to include the $p$-torsion and singular-base bookkeeping:
$$
\mathrm{BK}(n,\ell) \iff \mathrm{BL}(n,\ell)\ \text{for all smooth }X/k .
$$
The implication BL $\Rightarrow$ BK is immediate: take $X = \operatorname{Spec} F$, $p = n$, and use $H^{n,n}_{\mathcal{M}}(F,\mathbb{Z}/m) = K^M_n(F)/m$. The converse is a descent/induction argument on weight using the Bloch–Kato–Gabber and Gersten resolutions.

**Motivic spectral sequence.** BL controls the $E_2$-page of
$$
E_2^{p,q} = H^{p-q}_{\mathcal{M}}(X, \mathbb{Z}(-q)) \;\Longrightarrow\; K_{-p-q}(X),
$$
and with $\mathbb{Z}/m$ coefficients its degeneration range gives the **Quillen–Lichtenbaum conjecture**: $K_i(X;\mathbb{Z}/m) \to K^{\text{ét}}_i(X;\mathbb{Z}/m)$ is an isomorphism for $i \ge \operatorname{cd}_m(X) - 1$.

## 3. History & State of the Art (SOTA)

- **1970.** Milnor introduces $K^M_*$ and asks whether $K^M_n(F)/2 \to H^n(F,\mathbb{Z}/2)$ is an isomorphism (the *Milnor conjecture*, $m=2$).
- **1982–1985.** Lichtenbaum ("Values of zeta-functions at non-negative integers") and Beilinson ("Higher regulators and values of $L$-functions") independently postulate complexes $\mathbb{Z}(n)$ computing weight-$n$ motivic cohomology and conjecture the étale truncation property. Bloch and Kato formulate the norm residue statement in their 1986 IHÉS paper.
- **1982.** Merkurjev–Suslin prove $n=2$, all $m$: $K_2(F)/m \cong H^2(F,\mu_m^{\otimes 2})$ — the first deep case, equivalent to the statement that every central simple algebra of exponent $m$ is Brauer-equivalent to a product of cyclic algebras.
- **1985.** Thomason constructs étale $K$-theory and Bott-inverted descent spectral sequences, placing Quillen–Lichtenbaum in a homotopy-theoretic frame.
- **1990.** Merkurjev–Suslin and (independently) Rost settle $n=3$, $m=2$.
- **1996–2003.** Voevodsky proves the Milnor conjecture ($\ell = 2$, all $n$) using the motivic Steenrod algebra, motivic Adams-type arguments, and Rost's Pfister quadric splitting varieties. Published in *Publ. Math. IHÉS* 98 (2003).
- **2000.** Suslin–Voevodsky prove BK $\Leftrightarrow$ BL.
- **2011.** Voevodsky proves BK for all odd primes $\ell$ (*Annals of Mathematics* 174), conditional on Rost's theory of norm varieties and the Rost motive.
- **2019.** Haesemeyer–Weibel publish a complete, self-contained proof (*The Norm Residue Theorem in Motivic Cohomology*, Annals of Math. Studies 200), closing the remaining exposition gaps in Rost's chain-lemma and degree-formula input.

## 4. Partial Results / Verified Cases

| Case | Result | Reference |
|---|---|---|
| $n \le 1$, any $m$ | Kummer theory / Hilbert 90 | classical |
| $n = 2$, any $m$ | Isomorphism | Merkurjev–Suslin 1982 |
| $n = 3$, $\ell = 2$ | Isomorphism | Merkurjev–Suslin 1990; Rost |
| $\ell = 2$, all $n$ | Milnor conjecture | Voevodsky 2003 |
| $\ell$ odd prime, all $n$ | Norm residue theorem | Voevodsky 2011; Rost |
| $X$ smooth over a field, $m$ invertible | **BL holds in full** | Suslin–Voevodsky 2000 + above |
| $\operatorname{char} k = p$, $\ell = p$ | $\mathbb{Z}/p(n) \simeq \nu_n[-n]$ (logarithmic de Rham–Witt); BL holds in the degenerate form $H^{p,n} = 0$ for $p > n$ | Geisser–Levine, *Invent. Math.* 139 (2000) |
| $X = \operatorname{Spec}\mathcal{O}_F$, number ring, $\ell = 2$ | Quillen–Lichtenbaum verified, $K$-groups computed | Rognes–Weibel, *JAMS* 13 (2000) |
| $F$ algebraically closed | $K_*(F;\mathbb{Z}/m) \cong K_*^{\mathrm{top}}(\mathbb{C};\mathbb{Z}/m)$ | Suslin 1983 |

## 5. Principal Obstacles

The *original* statement is proved; the difficulty now sits in its generalizations, and the historical obstacles explain why the proof was 30 years in the making.

- **No induction from within étale cohomology.** BK$(n)$ cannot be deduced from BK$(n-1)$ by any purely cohomological device: one must *construct geometry*. Rost's **norm varieties** $X_a$ for a symbol $a = \{a_1,\dots,a_n\}$ — smooth projective of dimension $\ell^{n-1}-1$ splitting $a$, with $\deg$ of every closed point divisible by $\ell$ — require the chain lemma and degree formulas, the hardest input in the whole program.
- **Motivic Steenrod operations need char 0.** Voevodsky's computation of the motivic Steenrod algebra and the Milnor operations $Q_i$ used resolution of singularities; extending to $\operatorname{char} k = p > 0$ needed later work (Hoyois–Kelly–Østvær, and de Jong alterations) and is still delicate.
- **Integral coefficients fail.** BL with $\mathbb{Z}$ coefficients is false as stated; the correct integral statements — **Beilinson–Soulé vanishing** ($H^{p,n}_{\mathcal{M}}(X,\mathbb{Q}) = 0$ for $p \le 0$, $n>0$) and the Hodge/Tate-type conjectures on cycle class maps — remain open. No known technique produces vanishing in negative degrees; the Gersten/Bloch–Ogus machinery is degree-preserving and gives no leverage there.
- **Singular schemes.** $\mathbb{Z}(n)$ on non-smooth $X$ has no universally accepted definition with the right properties (cdh-descent versions lose the $K$-theory comparison; $K$-theoretic definitions lose $\mathbb{A}^1$-invariance). Weibel's cdh-motivic cohomology satisfies BL only after inverting characteristic.
- **Mixed characteristic and $\ell = p$.** For $X$ over $\mathbb{Z}_p$ and $m = p^r$, étale cohomology must be replaced by syntomic cohomology; the analogue of the BL truncation involves $\mathbb{Z}_p(n)^{\mathrm{syn}}$ and a Nygaard filtration, not $\tau^{\le n}$ of a Galois complex. Establishing the correct comparison range is the current frontier.

## 6. The Gap

For smooth $X$ over a field with $m$ invertible: **there is no gap** — Section 1 is a theorem. The live boundary lies one step out:

1. **Integral BL / Beilinson–Soulé.** Proven: $\mathbb{Z}/m(n) \simeq \tau^{\le n} R\pi_*\mu_m^{\otimes n}$. Open: the vanishing $H^{p,n}_{\mathcal{M}}(X,\mathbb{Q}) = 0$ for $p \le 0$, $n \ge 1$, unknown even for $X = \operatorname{Spec}\mathbb{Z}$ beyond small weights.
2. **$p$-adic BL in mixed characteristic.** Proven: $\ell \ne p$. Open (partially, see §7): $\mathbb{Z}_p(n)$ on $p$-adic schemes, where the comparison target is Bhatt–Morrow–Scholze syntomic cohomology and the truncation degree is not simply $n$.
3. **Singular / non-$\mathbb{A}^1$-invariant BL.** Proven for smooth $X$. Open: a motivic complex for arbitrary qcqs schemes with a BL truncation property and a spectral sequence to non-connective $K$-theory.

The exact step to be crossed for (2): identify a filtration on $p$-adic étale/syntomic cohomology whose graded pieces satisfy a Hilbert-90-type acyclicity in weight $n$, playing the role that Rost's norm varieties played for $\ell \ne p$.

## 7. Current Research (as of June 2026)

- **Syntomic and prismatic motivic cohomology.** Bhatt–Morrow–Scholze's $\mathbb{Z}_p(n)$ and the Antieau–Mathew–Morrow–Nikolaus Beilinson fiber square (*Duke Math. J.* 171, 2022) supply the mixed-characteristic replacement for $\mu_p^{\otimes n}$. Elmanto–Morrow (equicharacteristic) and Bouis (mixed characteristic) have constructed motivic cohomology for general schemes with a BL-style comparison; whether the truncation degree is exactly $n$ in all cases is still being pinned down *(frontier — verify)*.
- **Non-$\mathbb{A}^1$-invariant motivic homotopy.** Annala–Hoyois–Iwasa's $\mathbb{P}^1$-homotopy theory drops $\mathbb{A}^1$-invariance and aims to house a BL theorem for singular schemes *(frontier — verify)*.
- **Consequences and reproofs.** Bhatt–Clausen–Mathew's $K(1)$-local reproof of Quillen–Lichtenbaum, and continued work on the Rost motive in characteristic $p$ (Haesemeyer–Weibel; Hoyois–Kelly–Østvær).
- **Groups.** Institut de Mathématiques de Jussieu; IAS Princeton; Rutgers (Weibel); Bonn/MPIM (Nikolaus, Scholze); Oslo (Østvær); Copenhagen; Northwestern (Antieau).

## 8. Future Work

- Prove a truncation statement for $\mathbb{Z}_p(n)$ in mixed characteristic and derive the $p$-primary Quillen–Lichtenbaum theorem uniformly.
- Extend BL to *singular* schemes with a genuinely motivic (not merely cdh-descent) complex; test against Weibel's negative $K$-theory vanishing.
- Attack Beilinson–Soulé vanishing in weight $n \ge 3$ over number fields, where all current tools (Borel regulators, Goncharov's polylogarithmic complexes) stop.
- Find a "reason" for the norm residue theorem: a proof not requiring Rost's norm varieties. Voevodsky repeatedly flagged this as the structural desideratum.
- Develop BL for motivic cohomology with coefficients in general Galois modules and for stacks / equivariant settings.

## 9. Key References

- **[Foundational]** J. Milnor. *Algebraic $K$-theory and quadratic forms.* Inventiones Mathematicae 9 (1970), 318–344.
- **[Foundational]** S. Lichtenbaum. *Values of zeta-functions at non-negative integers.* In: Number Theory (Noordwijkerhout 1983), Lecture Notes in Math. 1068, Springer, 1984.
- **[Foundational]** A. Beilinson. *Higher regulators and values of $L$-functions.* Journal of Soviet Mathematics 30 (1985), 2036–2070.
- **[Foundational]** S. Bloch, K. Kato. *$p$-adic étale cohomology.* Publications Mathématiques de l'IHÉS 63 (1986), 107–152.
- **[Foundational]** A. Merkurjev, A. Suslin. *$K$-cohomology of Severi–Brauer varieties and the norm residue homomorphism.* Izv. Akad. Nauk SSSR Ser. Mat. 46 (1982), 1011–1046.
- **[Foundational]** R. Thomason. *Algebraic $K$-theory and étale cohomology.* Ann. Sci. École Norm. Sup. 18 (1985), 437–552.
- **[Key equivalence]** A. Suslin, V. Voevodsky. *Bloch–Kato conjecture and motivic cohomology with finite coefficients.* In: The Arithmetic and Geometry of Algebraic Cycles, NATO Sci. Ser. C 548, Kluwer, 2000, 117–189.
- **[SOTA]** V. Voevodsky. *Motivic cohomology with $\mathbb{Z}/2$-coefficients.* Publ. Math. IHÉS 98 (2003), 59–104.
- **[SOTA]** V. Voevodsky. *On motivic cohomology with $\mathbb{Z}/\ell$-coefficients.* Annals of Mathematics 174 (2011), 401–438.
- **[SOTA]** C. Haesemeyer, C. Weibel. *The Norm Residue Theorem in Motivic Cohomology.* Annals of Mathematics Studies 200, Princeton University Press, 2019.
- **[SOTA]** T. Geisser, M. Levine. *The $K$-theory of fields in characteristic $p$.* Inventiones Mathematicae 139 (2000), 459–493.
- **[SOTA]** T. Geisser, M. Levine. *The Bloch–Kato conjecture and a theorem of Suslin–Voevodsky.* J. reine angew. Math. 530 (2001), 55–103.
- **[Recent]** B. Antieau, A. Mathew, M. Morrow, T. Nikolaus. *On the Beilinson fiber square.* Duke Mathematical Journal 171 (2022), 3707–3806.
- **[Recent]** J. Rognes, C. Weibel. *Two-primary algebraic $K$-theory of rings of integers in number fields.* J. Amer. Math. Soc. 13 (2000), 1–54.
- **[Survey]** C. Mazza, V. Voevodsky, C. Weibel. *Lecture Notes on Motivic Cohomology.* Clay Mathematics Monographs 2, AMS, 2006.
- **[Survey]** C. Weibel. *The norm residue isomorphism theorem.* Journal of Topology 2 (2009), 346–372.

## 10. Worked Example / Concrete Special Case

**Weight $n = 1$ over a field $F$, coefficients $\mathbb{Z}/m$, $1/m \in F$.**

Take $X = \operatorname{Spec} F$. The weight-one motivic complex is $\mathbb{Z}(1) \simeq \mathbb{G}_m[-1]$, i.e. the single group $F^\times$ placed in cohomological degree $1$. Tensoring the exact triangle $\mathbb{Z}(1) \xrightarrow{m} \mathbb{Z}(1) \to \mathbb{Z}/m(1)$ gives

$$
H^{0,1}_{\mathcal{M}}(F,\mathbb{Z}/m) = {}_m(F^\times) = \mu_m(F), \qquad
H^{1,1}_{\mathcal{M}}(F,\mathbb{Z}/m) = F^\times/(F^\times)^m,
$$
and $H^{p,1}_{\mathcal{M}}(F,\mathbb{Z}/m) = 0$ for $p \ge 2$ (the complex has only one nonzero term).

The étale side is computed from the Kummer sequence of sheaves on $\operatorname{Spec} F_{\text{ét}}$:
$$
1 \to \mu_m \to \mathbb{G}_m \xrightarrow{\ x \mapsto x^m\ } \mathbb{G}_m \to 1 .
$$
Its long exact sequence, together with Hilbert's Theorem 90 ($H^1_{\text{ét}}(F,\mathbb{G}_m) = H^1(\mathrm{Gal}(F^{\mathrm{sep}}/F), (F^{\mathrm{sep}})^\times) = 0$), yields
$$
H^0_{\text{ét}}(F,\mu_m) = \mu_m(F), \qquad
H^1_{\text{ét}}(F,\mu_m) \cong F^\times/(F^\times)^m, \qquad
H^2_{\text{ét}}(F,\mu_m) \cong \operatorname{Br}(F)[m].
$$

Now check BL degree by degree, with $n=1$:

- $p = 0 \le n$: $\mu_m(F) \to \mu_m(F)$, identity. **Isomorphism ✓**
- $p = 1 \le n$: $F^\times/m \to H^1_{\text{ét}}(F,\mu_m)$, the Kummer map. **Isomorphism ✓** — this *is* Hilbert 90.
- $p = 2 = n+1$: $0 \to \operatorname{Br}(F)[m]$. **Injective ✓**, but not surjective in general.

The failure of surjectivity at $p = n+1$ is not a defect — it is the content of the conjecture. Concretely, for $F = \mathbb{Q}_p$ and $m = 2$: $H^{2,1}_{\mathcal{M}} = 0$ while $\operatorname{Br}(\mathbb{Q}_p)[2] \cong \tfrac{1}{2}\mathbb{Z}/\mathbb{Z} \cong \mathbb{Z}/2$, generated by the quaternion algebra class. Motivic cohomology genuinely sees only the truncation $\tau^{\le 1}$.

Stepping up one weight, $n = 2$, the same comparison at $p = n = 2$ reads
$$
K_2(F)/m \;\xrightarrow{\ \sim\ }\; H^2_{\text{ét}}(F, \mu_m^{\otimes 2}),
$$
which is exactly the Merkurjev–Suslin theorem of 1982. For $F = \mathbb{Q}$, $m = 2$, this identifies $K_2(\mathbb{Q})/2$ with $H^2(\mathbb{Q},\mu_2^{\otimes 2})$, and the Hilbert-symbol reciprocity $\prod_v (a,b)_v = 1$ is the resulting statement that the sum of local invariants of the quaternion algebra $(a,b)$ vanishes. The general case for all $n$ needed Rost's norm varieties and Voevodsky's motivic Steenrod operations.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*