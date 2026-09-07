---
id: 03-geometry/section-conjecture
title: "Section Conjecture"
topic: 03-geometry
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Section Conjecture

> **Topic:** Algebraic & Differential Geometry · **ID:** `03-geometry/section-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Let $k$ be a field finitely generated over $\mathbb{Q}$ (the core case: $k$ a number field), with absolute Galois group $G_k = \mathrm{Gal}(\bar k/k)$, and let $X/k$ be a smooth, geometrically connected **hyperbolic curve**: $2g-2+n>0$, where $g$ is the genus of the smooth compactification and $n$ the number of punctures. Étale homotopy theory gives the *fundamental exact sequence*

$$1 \longrightarrow \pi_1(X_{\bar k}) \longrightarrow \pi_1(X) \xrightarrow{\ \mathrm{pr}\ } G_k \longrightarrow 1 .$$

A rational point $x \in X(k)$ is a section $\mathrm{Spec}\,k \to X$ of the structure map, hence induces a group-theoretic section $s_x : G_k \to \pi_1(X)$, well defined up to conjugation by $\pi_1(X_{\bar k})$ (the ambiguity being the choice of a path to the base point).

**Conjecture (Grothendieck, 1983).** For $X/k$ projective hyperbolic, the map

$$\kappa : X(k) \longrightarrow \mathcal{S}_{\pi_1(X)/G_k} := \{\text{sections of } \mathrm{pr}\}/\!\sim_{\pi_1(X_{\bar k})}, \qquad x \mapsto [s_x],$$

is a **bijection**. For $X$ affine hyperbolic the same map, extended by *cuspidal (tangential) sections* at the punctures, is conjectured to be a bijection onto all sections; equivalently every section is either geometric or cuspidal.

A complete proof must show both **injectivity** (distinct points give non-conjugate sections) and **surjectivity** (every abstract section is geometric). A disproof would exhibit one hyperbolic curve over a finitely generated field of characteristic $0$ carrying a non-geometric, non-cuspidal section — for instance a curve with $X(k)=\emptyset$ but $\mathcal{S}\neq\emptyset$.

## 2. Mathematical Foundations

**Fundamental group.** $\pi_1(X_{\bar k})$ is the profinite completion of the topological surface group: for $X$ projective of genus $g$,

$$\pi_1(X_{\bar k}) \cong \widehat{\Big\langle a_1,b_1,\dots,a_g,b_g \ \Big|\ \prod_{i=1}^{g}[a_i,b_i]=1 \Big\rangle},$$

and for the $n$-punctured genus-$g$ curve, the profinite completion of a free group of rank $2g+n-1$. Hyperbolicity $2g-2+n>0$ is exactly the condition that this group is non-abelian and has trivial center, which makes $\pi_1(X) \to \mathrm{Out}(\pi_1(X_{\bar k}))$ the natural carrier of arithmetic information.

**Outer Galois representation.** Centerlessness gives an exact sequence-free reformulation: the extension class lives in

$$\rho_X : G_k \longrightarrow \mathrm{Out}\big(\pi_1(X_{\bar k})\big),$$

and sections of $\mathrm{pr}$ up to conjugacy form a torsor-like set whose obstruction theory is nonabelian $H^1$. Concretely, if $\pi_1(X_{\bar k})^{\mathrm{ab}} = T := \varprojlim_N J[N](\bar k)$ (the full Tate module of the Jacobian $J$), the abelianized sections are classified by

$$\mathcal{S}^{\mathrm{ab}} \ \longleftrightarrow\ H^1(G_k, T), \qquad \kappa^{\mathrm{ab}}:X(k)\to H^1(G_k,T)$$

the Kummer map, whose image lies in $\varprojlim_N J(k)/N J(k) \hookrightarrow H^1(G_k,T)$.

**Cuspidal sections.** For $X = \bar X \setminus S$, each $\bar k$-point $y \in S$ has a decomposition group $D_y \subset \pi_1(X)$ with $D_y \cap \pi_1(X_{\bar k}) = I_y \cong \hat{\mathbb{Z}}(1)$ and $D_y/I_y \cong G_{k(y)}$. If $y\in S(k)$, sections of $D_y \to G_k$ exist and are classified by $H^1(G_k,\hat{\mathbb{Z}}(1)) = \varprojlim_N k^\times/(k^\times)^N$; they correspond to nonzero tangent vectors at $y$ up to $N$-th powers. These *tangential sections* are not geometric but must be included in the affine statement.

**Local–global.** For a number field $k$ and place $v$, restriction gives $\mathcal{S}(X/k) \to \prod_v \mathcal{S}(X_{k_v}/k_v)$. The image of $\kappa$ lands in the subset cut out by the *finite descent obstruction*; the section conjecture predicts $X(k) = \mathcal{S}$, and hence (Stoll) that finite descent is the only obstruction for curves.

## 3. History & State of the Art (SOTA)

- **1983.** Grothendieck states the conjecture in his letter to Faltings (3 June 1983) and in *Esquisse d'un Programme*; both appear in *Geometric Galois Actions 1*, LMS Lecture Note Series 242 (1997). The section conjecture is the "$\mathrm{Spec}\,k \to X$" case of his general Hom-form anabelian philosophy.
- **1990.** Nakamura proves Galois rigidity for punctured projective lines, launching the isomorphism-form program.
- **1996–1999.** Tamagawa proves the Grothendieck conjecture for affine hyperbolic curves over finite and $p$-adic fields (Compositio 109, 1997); Mochizuki proves the isomorphism and Hom-forms for hyperbolic curves over **sub-$p$-adic** fields (Invent. Math. 138, 1999). These settle "isomorphisms of $\pi_1$ come from isomorphisms of curves" — but not the section conjecture, since a section is a morphism *from a point*, not from a hyperbolic curve.
- **2003–2011.** The **real** section conjecture ($k=\mathbb{R}$) becomes a theorem (Mochizuki; a homotopy-theoretic proof by Pál, 2011): conjugacy classes of sections biject with connected components of $X(\mathbb{R})$.
- **2005–2010.** The **birational** section conjecture over $p$-adic fields is proved by Koenigsmann (Crelle 588, 2005), extended to higher dimension and to "large"/pro-$p$ settings by Pop (Compositio 146, 2010).
- **2010.** Stix derives unconditional non-existence results: a section forces index $1$; Hoshi constructs counterexamples to the **pro-$p$** section conjecture over number fields, showing the profinite hypothesis is essential.

**Status.** Open in every case of the original statement: no hyperbolic curve over a number field with $X(k)\neq\emptyset$ is known to satisfy surjectivity of $\kappa$.

## 4. Partial Results / Verified Cases

- **Injectivity of $\kappa$:** known for all hyperbolic curves over finitely generated fields of characteristic $0$ (via the Mordell–Weil theorem and the Kummer map on the Jacobian; $\bigcap_N N J(k) = 0$).
- **$k=\mathbb{R}$ (and real closed fields):** full conjecture proved. $\mathcal{S} \leftrightarrow \pi_0(X(\mathbb{R}))$, with $\mathcal{S}=\emptyset$ iff $X(\mathbb{R})=\emptyset$ (Mochizuki; Pál).
- **Birational version over $p$-adic $k$:** sections of $\mathrm{Gal}(k(X)) \to G_k$ come from $k$-rational points of $X$ or from tangential data (Koenigsmann 2005; Pop 2010 in dimension $\geq 1$ and over henselian/large fields).
- **Empty-case verification:** if $X(k_v) = \emptyset$ for some place $v$, then $\mathcal{S}(X/k)=\emptyset$ and the conjecture holds trivially. Stix (Amer. J. Math. 132, 2010) upgraded this: if $X/k$ over a number field admits a section then the **index** of $X$ equals $1$; hence every curve of index $>1$ (e.g. suitable genus-$1$-index-$2$ constructions, or Stix's explicit hyperelliptic families) satisfies the conjecture vacuously.
- **Abelianized / nilpotent quotients:** Esnault–Wittenberg (JAMS 23, 2010) prove that under finiteness of $Ш(J)$ the abelian birational sections are controlled by $\varprojlim J(k)/N$; Harari–Szamuely (Math. Ann. 344, 2009) analyze $\kappa^{\mathrm{ab}}$ and show that the abelianized section conjecture is *false* in general, so the nonabelian input is indispensable. Wickelgren (Math. Ann. 358, 2014) proves the $2$-nilpotent real section conjecture for $\mathbb{P}^1\setminus\{0,1,\infty\}$.
- **Failure of variants:** the pro-$p$ section conjecture fails over number fields (Hoshi, Publ. RIMS 46, 2010): explicit hyperbolic curves with non-geometric pro-$p$ sections.

## 5. Principal Obstacles

- **No reconstruction target.** Mochizuki's and Tamagawa's methods reconstruct a curve from $\pi_1$ by recovering its function field / decomposition groups from group theory. A section $s:G_k\to\pi_1(X)$ gives a subgroup isomorphic to $G_k$; there is no known group-theoretic criterion certifying that $s(G_k)$ is a **decomposition group** of a closed point rather than an accidental copy of $G_k$.
- **Cuspidalization gap.** The birational statement (Koenigsmann, Pop) works with $\mathrm{Gal}(k(X))$, which contains all decomposition groups by construction. Passing from $\pi_1(k(X))$ down to $\pi_1(X)$ requires a *cuspidalization* — lifting a section of $\pi_1(X)$ to the birational fundamental group — and this is exactly the step no technique performs over number fields.
- **Failure of local-to-global.** Over $p$-adic fields sections are plentiful and poorly understood; there is no $p$-adic section conjecture theorem to feed a local–global argument, unlike in Faltings-style Diophantine geometry.
- **Non-abelian cohomology is not finite-dimensional.** Descent-obstruction computations control $\kappa^{\mathrm{ab}}$ and finite nilpotent quotients, but the counterexamples of Harari–Szamuely and Hoshi show every truncated (abelian, pro-$p$, $n$-nilpotent) approximation can admit spurious sections; the conjecture is genuinely about the full profinite object, where no finiteness or rigidity theorem applies.
- **No effectivity.** Even granting the conjecture, no algorithm computes $\mathcal{S}$; the space of sections is a profinite set with no known finiteness theorem, so one cannot verify surjectivity on a single example by computation.

## 6. The Gap

Proven: injectivity everywhere; the full statement over $\mathbb{R}$; the birational statement over $p$-adic and large fields; vacuous cases where $\mathcal{S}=\emptyset$ is forced by index or local obstructions.

Missing: a single implication of the form

$$s \in \mathcal{S}(X/k),\ X(k)\ \text{unconstrained} \ \Longrightarrow\ s(G_k) \ \text{is contained in a decomposition group } D_x,\ x \in X(k).$$

The precise barrier is the **cuspidalization step over global fields**: given a section of $\pi_1(X)\to G_k$, produce a compatible system of sections of $\pi_1(U)\to G_k$ for all open $U\subset X$, whose intersection of images is a decomposition group. Over $p$-adic fields the henselian valuation-theoretic machinery (Koenigsmann's use of $p$-adic rigidity and Pop's local theory) supplies this; over $\mathbb{Q}$ no substitute exists.

## 7. Current Research (as of June 2026)

- **Anabelian schools.** RIMS Kyoto (Mochizuki, Hoshi, Tsujimura, Minamide) pursues combinatorial/absolute anabelian geometry and the "resolution of nonsingularities" program, which would give a $p$-adic cuspidalization tool. *(frontier — verify)*
- **Exeter/Nottingham (Saïdi), Bonn (Stix), Penn (Pop)** work on section conjectures over function fields and finitely generated fields, and on the "good sections" formalism isolating which sections can be lifted birationally.
- **Homotopy-theoretic approaches.** Motivic and $\mathbb{A}^1$-homotopy methods (Wickelgren, Pál, Schmidt–Stix) reinterpret sections as points of an étale homotopy fixed-point space, giving obstruction towers whose first stages recover descent obstructions.
- **Computational descent.** Explicit verification that $\mathcal{S}=\emptyset$ for curves violating finite descent, connecting to quadratic Chabauty computations on modular curves. *(frontier — verify)*

## 8. Future Work

1. **Prove the $p$-adic section conjecture** for a nonempty class of hyperbolic curves; this is widely regarded as the necessary intermediate step (Stix's book devotes its final part to it).
2. **Cuspidalization theory:** develop a mechanism converting $\pi_1(X)$-sections into $\pi_1(k(X))$-sections, perhaps via the theory of decomposition groups of divisorial valuations.
3. **Test $\mathbb{P}^1\setminus\{0,1,\infty\}$** over $\mathbb{Q}$: the smallest hyperbolic curve, with $X(\mathbb{Q}) = \emptyset$ after removing $\{-1,2,1/2\}$-type solutions of the unit equation; a proof here would be decisive.
4. **Sharpen the descent link:** prove that the section-conjecture prediction implies Stoll's conjecture that finite descent is the only obstruction for curves, and look for a numerical counterexample to either.

## 9. Key References

- **[Foundational]** A. Grothendieck. *Letter to G. Faltings (1983)* and *Esquisse d'un Programme*, in L. Schneps, P. Lochak (eds.), **Geometric Galois Actions 1**, LMS Lecture Note Series 242, Cambridge University Press, 1997.
- **[Foundational]** H. Nakamura. *Galois rigidity of the étale fundamental groups of punctured projective lines.* J. reine angew. Math. **411** (1990), 205–216.
- **[Foundational]** A. Tamagawa. *The Grothendieck conjecture for affine curves.* Compositio Mathematica **109** (1997), 135–194.
- **[Foundational]** S. Mochizuki. *The local pro-$p$ anabelian geometry of curves.* Inventiones Mathematicae **138** (1999), 319–423.
- **[SOTA]** J. Koenigsmann. *On the section conjecture in anabelian geometry.* J. reine angew. Math. **588** (2005), 221–235.
- **[SOTA]** F. Pop. *On the birational $p$-adic section conjecture.* Compositio Mathematica **146** (2010), 621–637.
- **[SOTA]** H. Esnault, O. Wittenberg. *On abelian birational sections.* Journal of the AMS **23** (2010), 713–724.
- **[SOTA]** J. Stix. *On the period-index problem in light of the section conjecture.* American Journal of Mathematics **132** (2010), 157–180.
- **[SOTA]** Y. Hoshi. *Existence of nongeometric pro-$p$ Galois sections of hyperbolic curves.* Publ. RIMS **46** (2010), 829–848.
- **[SOTA]** D. Harari, T. Szamuely. *Galois sections for abelianized fundamental groups* (with an appendix by E. Demarche). Mathematische Annalen **344** (2009), 779–800.
- **[SOTA]** A. Pál. *The real section conjecture and Smith's fixed point theorem for pro-spaces.* J. London Math. Soc. **83** (2011), 353–367.
- **[SOTA]** K. Wickelgren. *2-nilpotent real section conjecture.* Mathematische Annalen **358** (2014), 361–387.
- **[Survey]** J. Stix. **Rational Points and Arithmetic of Fundamental Groups: Evidence for the Section Conjecture.** Lecture Notes in Mathematics 2054, Springer, 2013.
- **[Survey]** T. Szamuely. **Galois Groups and Fundamental Groups.** Cambridge Studies in Advanced Mathematics 117, Cambridge University Press, 2009.
- **[Related]** M. Stoll. *Finite descent obstructions and rational points on curves.* Algebra & Number Theory **1** (2007), 349–391.

## 10. Worked Example / Concrete Special Case

**Why hyperbolicity is not optional: $X = \mathbb{G}_m = \mathbb{P}^1\setminus\{0,\infty\}$ over $k=\mathbb{Q}$.**

Here $2g-2+n = -2+2 = 0$, so $X$ is *not* hyperbolic. The geometric fundamental group is abelian:

$$\pi_1(\mathbb{G}_{m,\bar{\mathbb{Q}}}) \cong \hat{\mathbb{Z}}(1) = \varprojlim_N \mu_N(\bar{\mathbb{Q}}).$$

Since the coefficient module is abelian and the extension $1 \to \hat{\mathbb{Z}}(1)\to \pi_1(\mathbb{G}_m)\to G_\mathbb{Q}\to 1$ is split (the point $1 \in \mathbb{G}_m(\mathbb{Q})$ splits it), conjugacy classes of sections form a **group**:

$$\mathcal{S} \ \cong\ H^1\big(G_\mathbb{Q}, \hat{\mathbb{Z}}(1)\big) \ =\ \varprojlim_N H^1(G_\mathbb{Q},\mu_N) \ =\ \varprojlim_N \mathbb{Q}^\times/(\mathbb{Q}^\times)^N \ =\ \widehat{\mathbb{Q}^\times},$$

by Hilbert 90 and Kummer theory. The map $\kappa$ is the Kummer map: for $a \in \mathbb{Q}^\times = X(\mathbb{Q})$, the associated cocycle is

$$c_a(\sigma) \ = \ \Big( \frac{\sigma(a^{1/N})}{a^{1/N}} \Big)_{N} \ \in \ \varprojlim_N \mu_N .$$

Now compute. $\mathbb{Q}^\times \cong \{\pm 1\}\times \bigoplus_{p} \mathbb{Z}$, a free abelian group of countable rank times $\mathbb{Z}/2$. Its profinite completion is

$$\widehat{\mathbb{Q}^\times} \ \cong\ \mathbb{Z}/2 \times \prod_{p \ \text{prime}}' \hat{\mathbb{Z}} \quad (\text{completion of the direct sum}),$$

which is **uncountable**, while $X(\mathbb{Q}) = \mathbb{Q}^\times$ is countable. So $\kappa$ is injective (as $\bigcap_N (\mathbb{Q}^\times)^N = \{1\}$) with dense image but is massively non-surjective: take $\alpha = (\ldots) \in \widehat{\mathbb{Q}^\times}$ whose $p$-adic exponent vector $(v_p(\alpha))_p \in \hat{\mathbb{Z}}^{\text{(completed)}}$ has infinitely many nonzero entries — e.g. $v_p(\alpha)=1$ for all $p$. No rational number has infinitely many prime factors, so $\alpha \notin \mathrm{im}\,\kappa$, yet $\alpha$ defines a perfectly good conjugacy class of sections of $\pi_1(\mathbb{G}_m)\to G_\mathbb{Q}$.

**Reading.** For genus $0$ with $n=2$, non-geometric sections are abundant and completely explicit. The section conjecture asserts that the moment one adds a third puncture ($X=\mathbb{P}^1\setminus\{0,1,\infty\}$, $2g-2+n=1>0$), the fundamental group becomes a free profinite group of rank $2$ with trivial center, the abelian Kummer-theoretic slack collapses under the non-abelian braid-like relations, and $\kappa$ becomes bijective onto geometric-plus-cuspidal sections. Proving that collapse — even for this single curve over $\mathbb{Q}$ — remains open; only its $2$-nilpotent and real shadows are known (Wickelgren 2014).

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*