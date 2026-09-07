---
id: 03-geometry/campana-conjecture
title: "Campana Conjecture"
topic: 03-geometry
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Campana Conjecture

> **Topic:** Algebraic & Differential Geometry · **ID:** `03-geometry/campana-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Campana introduced a birational class of varieties called **special**, defined by the absence of any fibration whose *orbifold base* is of general type. His conjecture asserts that specialness is the exact geometric characterisation of three a priori unrelated "non-hyperbolic" behaviours.

Let $X$ be a smooth projective variety over a number field $k$ (or a compact Kähler manifold in the analytic statements). Campana conjectures:

1. **(Arithmetic)** $X$ is special $\iff$ rational points are *potentially dense*: there is a finite extension $k'/k$ with $X(k')$ Zariski dense.
2. **(Analytic)** $X$ is special $\iff$ the Kobayashi pseudodistance $d_X$ vanishes identically $\iff$ (conjecturally) entire curves $\mathbb{C}\to X$ are Zariski dense.
3. **(Topological)** If $X$ is special then $\pi_1(X)$ is almost abelian (abelian up to finite index).

The conjecture has a relative, and strictly stronger, **orbifold form**: for a pair $(X,\Delta)$ of general type, the set of *Campana points* (integral points satisfying prescribed divisibility along $\Delta$) is not Zariski dense. Combined with the **core map** $c: X \dashrightarrow C(X)$, this decomposes any $X$ into a special part (density) and a general-type orbifold base (Lang-type degeneracy).

A complete proof requires both implications in each equivalence, for all dimensions; a disproof requires one special variety with non-dense points over every finite extension, or one non-special variety with potentially dense points.

## 2. Mathematical Foundations

**Orbifold pair.** A pair $(X,\Delta)$ with $X$ normal projective and
$$\Delta \;=\; \sum_{i} \Bigl(1-\tfrac{1}{m_i}\Bigr) D_i, \qquad m_i \in \{2,3,\dots\}\cup\{\infty\},$$
the $D_i$ distinct prime divisors. Its canonical bundle is $K_{(X,\Delta)} = K_X + \Delta$ and its Kodaira dimension is
$$\kappa(X,\Delta) \;=\; \limsup_{N\to\infty} \frac{\log h^0\bigl(X, \lfloor N(K_X+\Delta)\rfloor\bigr)}{\log N}.$$
$(X,\Delta)$ is **of general type** if $\kappa(X,\Delta)=\dim X$.

**Orbifold base of a fibration.** Let $f: X \dashrightarrow Y$ be a dominant fibration with connected fibres, $Y$ of dimension $\ge 1$. For a prime divisor $D\subset Y$ write $f^*D = \sum_j t_j E_j + (\text{$f$-exceptional})$. Set the *classical (inf) multiplicity* $m_f(D) = \min_j t_j$ and
$$\Delta_f \;=\; \sum_{D\subset Y}\Bigl(1-\tfrac{1}{m_f(D)}\Bigr) D .$$
The pair $(Y,\Delta_f)$ is the **orbifold base**; it is taken on a suitable birational model (a "neat" model), and $\kappa(Y,\Delta_f)$ is a birational invariant of $f$.

**Special variety.** $X$ is **special** if for *every* dominant fibration $f: X\dashrightarrow Y$ with $\dim Y \ge 1$,
$$\kappa(Y,\Delta_f) \;<\; \dim Y .$$
Equivalently (Campana 2004): $X$ is special iff it carries no **Bogomolov sheaf**, i.e. no rank-one saturated subsheaf $\mathcal{L}\subset \Omega_X^p$ with $\kappa(X,\mathcal{L}) = p$ for some $1\le p\le \dim X$.

**Core map.** For every $X$ there is a functorial fibration $c_X: X \dashrightarrow C(X)$, unique up to birational equivalence, whose general fibres are special and whose orbifold base $(C(X), \Delta_{c_X})$ is of general type. Rationally connected varieties and those with $\kappa(X)=0$ are special ($C(X)$ = point); varieties of general type with $\dim X\ge 1$ are non-special ($c_X = \mathrm{id}$).

**Campana points.** Fix a model $\mathcal{X}\to \mathrm{Spec}\,\mathcal{O}_{k,S}$ and horizontal $\mathcal{D}_i$. A point $P\in X(k)\setminus \bigcup D_i$ is a **Campana point** for $(X,\Delta)$ if for each $i$ and each place $v\notin S$,
$$\mathrm{ord}_v\bigl(\mathcal{D}_i \cdot \overline{P}\bigr) \;=\; 0 \quad\text{or}\quad \mathrm{ord}_v\bigl(\mathcal{D}_i\cdot \overline{P}\bigr) \;\ge\; m_i .$$
**Orbifold Lang–Vojta conjecture:** if $(X,\Delta)$ is of general type, Campana points are not Zariski dense (and are finite when $\dim X = 1$).

## 3. History & State of the Art (SOTA)

- **1970s–1990s.** Bombieri–Lang: a variety of general type has non-dense rational points. Faltings (1983, 1991) proves the curve and subvariety-of-abelian-variety cases. Kobayashi's hyperbolicity conjectures give the analytic counterpart. The dichotomy "general type vs. everything else" was known to be too coarse: Campana's multiple-fibre examples show a variety with $\kappa(X)=1$ can behave like one of general type.
- **2004.** Campana, *Orbifolds, special varieties and classification theory* (Ann. Inst. Fourier **54**, 499–630) introduces orbifold bases, the class of special varieties, the core map, and states the full conjecture.
- **2005.** Campana, *Fibres multiples sur les surfaces* (Manuscripta Math. **117**) develops the surface case and links orbifold Mordell on $\mathbb{P}^1$ to the $abc$ conjecture.
- **2011.** Campana extends the theory to compact Kähler manifolds (J. Inst. Math. Jussieu **10**, 809–934), together with a survey in the EMS volume *Classification of Algebraic Varieties*.
- **2019.** Campana–Păun (Publ. IHÉS **129**) prove birational stability of orbifold cotangent sheaves: if $K_X+\Delta$ is pseudoeffective, then every quotient of $\Omega^1_{(X,\Delta)}$ has pseudoeffective determinant. This supplies the positivity input the classification programme needs.
- **2021–present.** A quantitative arithmetic branch opens: Pieropan–Smeets–Tanimoto–Várilly-Alvarado (Proc. LMS **123**, 2021) formulate a Manin-type asymptotic for Campana points of bounded height and prove it for vector group compactifications.

## 4. Partial Results / Verified Cases

- **Curves.** $X$ special $\iff$ $g(X)\le 1$. Faltings' theorem gives the arithmetic equivalence; genus $\le 1$ gives potential density. Fully proven.
- **Orbifold curves over $\mathbb{Q}$, conditionally.** For $(\mathbb{P}^1,\Delta)$ with $\deg(K+\Delta)>0$, the $abc$ conjecture implies finiteness of Campana points (Campana 2005). Unconditional in the function-field case by Vojta/Mason-type height inequalities.
- **Rationally connected varieties and $\kappa = 0$.** Both are special; potential density is a theorem for rationally connected varieties (Graber–Harris–Starr plus Hassett–Tschinkel arguments) and for abelian varieties, but is **open** for general $\kappa=0$ varieties, notably simply connected Calabi–Yau threefolds.
- **K3 surfaces.** Potential density holds for elliptic K3s and K3s with infinite automorphism group (Bogomolov–Tschinkel, *Density of rational points on elliptic K3 surfaces*, GAFA 2000); all K3s are special. The remaining cases (generic K3 of Picard rank 1) are open.
- **Surfaces.** The classification of special surfaces is complete: $S$ is special iff $\kappa(S)\le 1$ and the orbifold base of the Iitaka fibration is not of general type. Half of the arithmetic conjecture (special $\Rightarrow$ potential density) is known except for some $\kappa=1$ and $\kappa=0$ cases; the converse depends on Bombieri–Lang.
- **Fundamental group.** $\pi_1$ almost abelian is known for special surfaces, for $\kappa(X)=0$ Kähler manifolds up to the abundance conjecture, and for linear representations via Campana–Claudon–Eyssidieux (Compositio **151**, 2015).
- **Special orbifold cases of orbifold Lang–Vojta.** Corvaja–Zannier, Levin, and Autissier prove degeneracy of integral points on many surface pairs $(\mathbb{P}^2, D)$ with $D$ a union of $\ge 4$ lines/conics; Smeets and Streeter prove orbifold-Mordell statements for powerful values of norm forms.
- **Non-special hyperbolicity.** Rousseau–Turchet–Wang (Forum Math. Sigma **9**, 2021) verify the hyperbolic and arithmetic predictions for explicit families of non-special varieties, e.g. complements and fibred threefolds.

## 5. Principal Obstacles

- **No mechanism for producing rational points.** Density statements require a construction (elliptic fibrations, automorphisms, group actions). For a simply connected Calabi–Yau threefold with no fibration and finite automorphism group, no known technique produces a Zariski-dense orbit. Specialness is a *negative* condition — it says which fibrations do not exist — so it gives nothing to iterate.
- **Bombieri–Lang is itself open.** The "non-special $\Rightarrow$ non-dense" direction contains Lang's conjecture as the case $c_X=\mathrm{id}$, and is therefore at least as hard as Faltings in higher dimension.
- **Orbifold multiplicities break Diophantine approximation.** Schmidt subspace/Schmidt–Vojta methods (Corvaja–Zannier, Levin) need many divisor components in general position; a general-type orbifold may have $\deg(K+\Delta)>0$ with only 3 components and small multiplicities, exactly where the approximation inequalities have no slack. The $abc$ dependence in the $\mathbb{P}^1$ case is not an artefact — it is the true difficulty.
- **Positivity is not enough.** Campana–Păun give pseudoeffectivity of orbifold cotangent quotients, but hyperbolicity arguments (Demailly jets, Nevanlinna) need *bigness* of $\Omega^1$ or of jet bundles, which fails for most general-type orbifolds.
- **Abundance.** Deciding whether $\kappa(Y,\Delta_f)=\dim Y$ for all fibrations requires control of $\kappa$ versus numerical positivity — i.e. the abundance conjecture for pairs, itself open from dimension 4 upward in the Kähler setting.
- **Non-classical multiplicities.** The theory is sensitive to $\min$ versus $\mathrm{gcd}$ multiplicities; the two definitions give different classes in dimension $\ge 3$, and it is not settled which is the arithmetically correct one.

## 6. The Gap

Proven: dimension 1 in full; both directions in dimension 2 modulo Bombieri–Lang and modulo potential density for specific $\kappa\in\{0,1\}$ surfaces; the orbifold-curve case *conditional on $abc$*.

Missing, precisely:

1. **A source of dense points for special varieties with no fibration and no automorphisms.** Concretely: exhibit a number field $k'$ with $X(k')$ dense for a generic quintic-section Calabi–Yau threefold.
2. **Degeneracy for orbifold pairs of general type**, unconditionally, already for $(\mathbb{P}^1,\Delta)$ over $\mathbb{Q}$ — an $abc$-strength input.
3. **Stability of specialness under fibration**: it is known that special is preserved under smooth morphisms with special fibres in many cases, but the general "special fibres + special base $\Rightarrow$ special total space" statement (the $C_{n,m}$-type orbifold additivity $\kappa(X,\Delta)\ge \kappa(F,\Delta_F)+\kappa(Y,\Delta_f)$) is open in the orbifold category and is the technical hinge of the whole programme.

## 7. Current Research (as of June 2026)

- **Quantitative Campana points.** Manin-type counting for Campana points, following Pieropan–Smeets–Tanimoto–Várilly-Alvarado; extensions to toric varieties (Pieropan–Schindler, hyperbola method), norm-form orbifolds (Streeter), and equivariant compactifications. Nakahara–Streeter study weak approximation and the Hilbert property in this setting. Groups: Hannover, Bath/Bristol, Osaka, Leiden.
- **Orbifold hyperbolicity.** Cadorel, Deng, Rousseau, Brotbek and collaborators develop orbifold jet differentials and Viehweg–Zuo sheaves to prove hyperbolicity of base spaces of maximal-variation families — a direct analytic case of the conjecture. *(frontier — verify)*
- **Positivity and the core.** Continuation of Campana–Păun: orbifold foliation theory, orbifold $C_{n,m}$, and the MMP for pairs with non-reduced boundary (Nancy, Strasbourg, Freiburg, Bonn).
- **Function-field and $p$-adic analogues.** Isotriviality statements over function fields, where Vojta-type inequalities are theorems, giving unconditional evidence for the arithmetic conjecture. *(frontier — verify)*
- **Potential density experiments.** Explicit search for dense orbits on Calabi–Yau and hyperkähler varieties via rational curves and dynamics (Hassett–Tschinkel style constructions).

## 8. Future Work

- Prove orbifold additivity $C^{\mathrm{orb}}_{n,m}$ in full; this would make the core map behave functorially in all dimensions.
- Establish potential density for one simply connected Calabi–Yau threefold; leading proposals use rational curves of large degree, or families of elliptic curves with non-torsion sections.
- Reduce the orbifold Lang–Vojta conjecture for surfaces to a finite list of divisor configurations amenable to the Schmidt subspace theorem.
- Deduce from $abc$ (or from a partial $abc$ with small exponent) the full orbifold-curve case over all number fields.
- Settle the $\min$-versus-$\gcd$ multiplicity question by finding an arithmetic example separating the two classes.
- Prove "special $\Rightarrow$ $\pi_1$ almost abelian" for threefolds, where the abundance conjecture is available.

## 9. Key References

- **[Foundational]** F. Campana. *Orbifolds, special varieties and classification theory.* Annales de l'Institut Fourier **54** (2004), 499–630.
- **[Foundational]** F. Campana. *Fibres multiples sur les surfaces: aspects géométriques, hyperboliques et arithmétiques.* Manuscripta Mathematica **117** (2005), 429–461.
- **[Foundational]** F. Campana. *Orbifoldes géométriques spéciales et classification biméromorphe des variétés kählériennes compactes.* Journal of the Institute of Mathematics of Jussieu **10** (2011), 809–934.
- **[SOTA]** F. Campana, M. Păun. *Foliations with positive slopes and birational stability of orbifold cotangent bundles.* Publications Mathématiques de l'IHÉS **129** (2019), 1–49.
- **[SOTA]** M. Pieropan, A. Smeets, S. Tanimoto, A. Várilly-Alvarado. *Campana points of bounded height on vector group compactifications.* Proceedings of the London Mathematical Society **123** (2021), 57–101.
- **[SOTA]** E. Rousseau, A. Turchet, J. T.-Y. Wang. *Nonspecial varieties and generalised Lang–Vojta conjectures.* Forum of Mathematics, Sigma **9** (2021), e11.
- **[SOTA]** S. Streeter. *Campana points and powerful values of norm forms.* Mathematische Zeitschrift **301** (2022), 627–664.
- **[Related]** F. Bogomolov, Y. Tschinkel. *Density of rational points on elliptic K3 surfaces.* Geometric and Functional Analysis **10** (2000), 1101–1133.
- **[Related]** F. Campana, B. Claudon, P. Eyssidieux. *Représentations linéaires des groupes kählériens: factorisations et conjecture de Shafarevich linéaire.* Compositio Mathematica **151** (2015), 351–376.
- **[Survey]** D. Abramovich. *Birational geometry for number theorists.* In *Arithmetic Geometry*, Clay Mathematics Proceedings **8**, AMS, 2009, 335–373.
- **[Survey]** F. Campana. *Special orbifolds and birational classification: a survey.* In *Classification of Algebraic Varieties*, EMS Series of Congress Reports, 2011, 123–170.

## 10. Worked Example / Concrete Special Case

Take $X=\mathbb{P}^1_{\mathbb{Q}}$ with the orbifold divisor
$$\Delta \;=\; \tfrac12\,[0] \;+\; \tfrac23\,[1] \;+\; \tfrac67\,[\infty],$$
i.e. multiplicities $(m_0,m_1,m_\infty)=(2,3,7)$. Then
$$\deg(K_{\mathbb{P}^1}+\Delta) \;=\; -2 + \Bigl(1-\tfrac12\Bigr)+\Bigl(1-\tfrac13\Bigr)+\Bigl(1-\tfrac17\Bigr) \;=\; -2+\tfrac{41}{42} \cdot \tfrac{42}{41}\cdot\ldots \;=\; \tfrac{1}{42} \;>\;0,$$
computed directly as $\tfrac12+\tfrac23+\tfrac67 = \tfrac{21+28+36}{42}=\tfrac{85}{42}$, so the degree is $\tfrac{85}{42}-2=\tfrac{1}{42}$. The pair is of general type, so $\mathbb{P}^1$ with this structure is **non-special** and Campana's conjecture predicts **finitely many** Campana points.

**Translation to Diophantine language.** Write a rational point as $x=a/b$ with $\gcd(a,b)=1$. The three orbifold points pull back to the integers $a$ (at $0$), $a-b$ (at $1$), $b$ (at $\infty$). A Campana point is a coprime pair with
$$a \text{ squarefull},\qquad a-b \text{ cubefull},\qquad b \text{ } 7\text{-full},$$
where $n$ is $m$-full if $p\mid n \Rightarrow p^m\mid n$.

**A solution exists.** $(a,b)=(9,1)$: $a=3^2$ is squarefull, $b=1$ is $7$-full, $a-b=8=2^3$ is cubefull, and $\gcd(9,1)=1$. So $x=9$ is a Campana point. The conjecture asserts the list of such $x$ terminates.

**Why $abc$ suffices.** Put $H=\max(|a|,|b|)$, so $|a-b|\le 2H$. If $n$ is $m$-full then $\mathrm{rad}(n)\le |n|^{1/m}$. Hence
$$\mathrm{rad}\bigl(a\,b\,(a-b)\bigr) \;\le\; |a|^{1/2}\,|b|^{1/7}\,|a-b|^{1/3} \;\le\; 2^{1/3}\,H^{\frac12+\frac17+\frac13} \;=\; 2^{1/3}H^{\frac{41}{42}}.$$
The $abc$ conjecture applied to $a=(a-b)+b$ gives $H \ll_\varepsilon \mathrm{rad}(ab(a-b))^{1+\varepsilon}$, so
$$H \;\ll_\varepsilon\; H^{\frac{41}{42}(1+\varepsilon)} .$$
For $\varepsilon<\tfrac{1}{41}$ the exponent is $<1$, forcing $H$ bounded: finitely many Campana points, as predicted.

**Contrast.** Replace $\Delta$ by multiplicity $2$ at four points: $\deg(K+\Delta)=-2+4\cdot\tfrac12=0$. The pair is log-Calabi–Yau, hence special; it is uniformised by an elliptic curve via a double cover, and Campana points are potentially dense — matching the conjecture on the other side of the dichotomy. The whole content of the conjecture is that this degree-$0$/degree-$>0$ threshold, read through orbifold bases of all fibrations, governs arithmetic and hyperbolic behaviour in every dimension.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*