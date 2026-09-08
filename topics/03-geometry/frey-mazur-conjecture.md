---
id: 03-geometry/frey-mazur-conjecture
title: "Serre's Uniformity and Frey-Mazur Conjecture on Isogeny of Elliptic Curves"
topic: 03-geometry
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Serre's Uniformity and Frey-Mazur Conjecture on Isogeny of Elliptic Curves

> **Topic:** Algebraic & Differential Geometry · **ID:** `03-geometry/frey-mazur-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Two linked uniformity statements about mod-$p$ Galois representations of elliptic curves over $\mathbb{Q}$.

**(A) Serre's uniformity conjecture.** There is an absolute constant $C$ such that for every elliptic curve $E/\mathbb{Q}$ without complex multiplication and every prime $p > C$, the mod-$p$ representation
$$\rho_{E,p}\colon \mathrm{Gal}(\overline{\mathbb{Q}}/\mathbb{Q}) \longrightarrow \mathrm{Aut}(E[p]) \cong \mathrm{GL}_2(\mathbb{F}_p)$$
is **surjective**. The expected optimal value is $C = 37$.

**(B) Frey–Mazur conjecture.** There is an absolute constant $C'$ such that for all elliptic curves $E, E'/\mathbb{Q}$ and all primes $p > C'$, an isomorphism of $\mathrm{Gal}(\overline{\mathbb{Q}}/\mathbb{Q})$-modules
$$E[p] \;\cong\; E'[p]$$
forces $E$ and $E'$ to be **isogenous over $\mathbb{Q}$**. The expected value is $C' = 17$.

A complete proof of (A) means: determine $X_{\mathrm{ns}}^{+}(p)(\mathbb{Q})$ (rational points of the modular curve for the normalizer of a nonsplit Cartan subgroup) for all $p > 37$ and show every such point is a cusp or CM. A complete proof of (B) means: show that for $p > C'$ the twisted modular curve $X_E(p)$ classifying curves $p$-congruent to $E$ has only the "obvious" rational points, uniformly in $E$. A disproof of either is a single explicit counterexample with $p$ above the stated bound.

## 2. Mathematical Foundations

Let $E/\mathbb{Q}$ be an elliptic curve, $p$ prime, $E[p] \cong (\mathbb{Z}/p)^2$ its $p$-torsion. Galois acts $\mathbb{F}_p$-linearly, giving $\rho_{E,p}$. Two constraints:

- $\det \rho_{E,p} = \chi_p$, the mod-$p$ cyclotomic character, so the image surjects onto $\mathbb{F}_p^\times$ via $\det$.
- Complex conjugation has image conjugate to $\begin{pmatrix} 1 & 0 \\ 0 & -1\end{pmatrix}$ (the representation is *odd*).

**Serre's classification.** If $\rho_{E,p}$ is not surjective and $p \geq 17$ ($p \neq 2,3,5,7,11,13$ handled separately), then $\mathrm{im}\,\rho_{E,p}$ is contained in one of:
1. a **Borel** subgroup $\left\{\begin{pmatrix}*&*\\0&*\end{pmatrix}\right\}$ — equivalently $E$ admits a rational $p$-isogeny;
2. the normalizer $N_s(p)$ of a **split Cartan** $C_s(p) \cong \mathbb{F}_p^\times \times \mathbb{F}_p^\times$;
3. the normalizer $N_{ns}(p)$ of a **nonsplit Cartan** $C_{ns}(p) \cong \mathbb{F}_{p^2}^\times$;
4. a subgroup with projective image $A_4$, $S_4$ or $A_5$ ("exceptional").

The exceptional case is excluded for $p > 13$ by the oddness plus $\det$ surjectivity, since $\mathrm{PGL}_2(\mathbb{F}_p)$ then contains no such subgroup compatible with $\chi_p$ being surjective. Cases 1–3 correspond to rational points on the modular curves $X_0(p)$, $X_s^+(p)$, $X_{ns}^+(p)$, quotients of $X(p)$ by the corresponding subgroups. Degrees over $X(1)$ are $p+1$, $p(p+1)/2$, $p(p-1)/2$; genera grow like $p/12$, $p^2/24$, $p^2/24$.

**Congruences and the Weil pairing.** An isomorphism $\phi\colon E[p] \to E'[p]$ of Galois modules is *symplectic* if $e_p(\phi P, \phi Q) = e_p(P,Q)^{\lambda}$ with $\lambda$ a fixed square in $\mathbb{F}_p^\times$, where $e_p$ is the Weil pairing; Galois-equivariance forces $\lambda \in \mathbb{F}_p^\times$ in general. Fixing $E$, the pairs $(E', \phi)$ are parametrized by the $\mathbb{Q}$-rational points of a twist $X_E(p)$ of the modular curve $X(p)$, a smooth curve of genus
$$g\big(X(p)\big) = 1 + \frac{(p-6)(p^2-1)}{24},$$
so $g = 0$ for $p \le 5$, $g = 3$ for $p = 7$, $g=26$ for $p=11$, $g=50$ for $p=13$, and $g \ge 133$ for $p \ge 17$. Faltings' theorem gives $\\#X_E(p)(\mathbb{Q}) < \infty$ for each fixed $E$ and $p \ge 7$; the conjecture asserts uniformity in $E$.

**Relation to (A).** If $E[p] \cong E'[p]$ then $\mathrm{im}\,\rho_{E,p} = \mathrm{im}\,\rho_{E',p}$, so Frey–Mazur is a statement about the *fibers* of $E \mapsto \rho_{E,p}$, whereas Serre uniformity is about the *image*. Both are instances of the expectation that non-cuspidal, non-CM rational points on modular curves of large level are exhausted by finitely many sporadic examples (a case of the Zilber–Pink / uniform Mordell–Lang philosophy).

## 3. History & State of the Art (SOTA)

- **1972.** Serre (*Propriétés galoisiennes des points d'ordre fini des courbes elliptiques*, Invent. Math. 15) proves the open image theorem: for non-CM $E/\mathbb{Q}$, $\rho_{E,p}$ is surjective for all $p \gg_E 0$, and raises the uniformity question.
- **1977–78.** Mazur settles the Borel case: *Rational points on modular curves* (LNM 601) and *Rational isogenies of prime degree* (Invent. Math. 44). For non-CM $E/\mathbb{Q}$, a rational $p$-isogeny exists only for $p \in \{2,3,5,7,11,13,17,19,37\}$.
- **1980s.** Frey and Mazur formulate (B) in the context of the modular method for Fermat-type equations; it explains why level-lowering arguments need $p$ large.
- **1992.** Kraus–Oesterlé (*Sur une question de B. Mazur*, Math. Ann. 293) prove structural constraints on $p$-congruent pairs, e.g. control of the congruence in terms of conductors and $j$-invariants.
- **2011.** Bilu–Parent, *Serre's uniformity problem in the split Cartan case* (Annals of Math. 173): $X_s^+(p)(\mathbb{Q})$ has only cusps and CM points for $p$ large; extended by Bilu–Parent–Rebolledo (Ann. Inst. Fourier 63, 2013) to all $p \ge 11$, $p \ne 13$.
- **2014.** Baran shows the exceptional isomorphism $X_s(13) \cong X_{ns}^{+}(13)$ (J. Number Theory), making level 13 a single "cursed curve" of genus 3.
- **2019/2023.** Balakrishnan–Dogra–Müller–Tuitman–Vonk determine $X_s(13)(\mathbb{Q})$ by explicit quadratic Chabauty–Kim (Annals 189, 2019) and extend the machinery in *Quadratic Chabauty for modular curves* (Compositio Math. 159, 2023).
- **2016–2022.** Massive computation: Sutherland (Forum Math. Sigma 4, 2016) computes mod-$p$ images for $\sim 10^8$ curves; Zywina classifies possible images; Rouse–Sutherland–Zureick-Brown (Forum Math. Sigma 10, 2022) determine $\ell$-adic images for all $E/\mathbb{Q}$, conditional exactly on the nonsplit Cartan case.

## 4. Partial Results / Verified Cases

**Serre uniformity — proved sub-cases (all for $E/\mathbb{Q}$ non-CM, $p > 37$):**
- Borel/reducible: **completely proved** (Mazur 1978).
- Exceptional projective image $A_4, S_4, A_5$: **impossible** for $p > 13$ (Serre 1972).
- Split Cartan normalizer: **completely proved** for $p \ge 11$, $p\neq13$ (Bilu–Parent 2011; Bilu–Parent–Rebolledo 2013); $p = 13$ by BDMTV 2019.
- Nonsplit Cartan normalizer: proved only for $p \le 13$ (level 13 via Baran's isomorphism). **Open for every $p \ge 17$.**

**Conditional and effective bounds.**
- Under GRH, Serre (Publ. IHÉS 54, 1981) and Larson–Vaintrob (Bull. LMS 46, 2014) give $p \ll \log N_E$ for exceptional primes, $N_E$ the conductor.
- Unconditional effective bounds depending on $E$: Masser–Wüstholz (Bull. LMS 25, 1993), Pellarin (2001), Lombardo (Math. Ann. 2015), Le Fourn — all polynomial in the Faltings height, none uniform.
- Lemos proves surjectivity for $p>37$ whenever $E/\mathbb{Q}$ admits *some* rational cyclic isogeny of degree $> 1$ (Trans. AMS 371, 2019), and further cases in Math. Z. (2019).
- Le Fourn–Lemos (Algebra & Number Theory 15, 2021) rule out large classes of nonsplit-Cartan images, leaving only images equal to the full normalizer for $p$ above an explicit bound.

**Computational verification.** No non-CM $E/\mathbb{Q}$ with non-surjective $\rho_{E,p}$ for $p>37$ occurs among all curves of conductor $\le 10^6$ and the $\sim 2.5\times 10^8$ curves in the LMFDB/Stein–Watkins databases (Sutherland 2016; Zywina).

**Frey–Mazur — verified and falsified ranges.**
- Counterexamples exist for $p \le 17$. For $p = 2,3,5$ the twist $X_E(p)$ has genus $0$ with rational points, so *every* $E$ lies in an infinite family of pairwise non-isogenous $p$-congruent curves (Rubin–Silverberg 1995). For $p=7$, $X_E(7)$ is a plane quartic and infinitely many $E$ admit nontrivial congruences (Halberstadt–Kraus 2003).
- Cremona–Freitas (Rev. Mat. Iberoam. 38, 2022) exhaustively searched LMFDB conductor ranges and determined symplectic type; the largest prime realized by a non-isogenous congruent pair is $p = 17$ *(frontier — verify the specific conductor-3675 example labels)*. No pair with $p \ge 19$ is known.
- **Function-field analogue proved:** Bakker–Tsimerman (Annals of Math. 184, 2016) prove the geometric Frey–Mazur statement over function fields of curves of fixed genus $g$, with $C'$ depending only on $g$.

## 5. Principal Obstacles

- **Genus growth versus rank.** For $X_{ns}^{+}(p)$ the genus is $\approx p^2/24$, and the Jacobian's Mordell–Weil rank over $\mathbb{Q}$ is expected to grow comparably. Classical Chabauty–Coleman requires $\mathrm{rank}\,J(\mathbb{Q}) < g$; this fails systematically here.
- **No winding quotient.** Mazur's Eisenstein-ideal argument and Bilu–Parent's Runge method both exploit structure absent in the nonsplit case: $X_{ns}^{+}(p)$ has a **single cusp**, so Runge's method (which needs at least two cusps in different Galois orbits, or many rational points at infinity) does not apply, and there is no analogue of the rank-zero winding quotient of $J_0(p)$.
- **Quadratic Chabauty scaling.** The BDMTV method needs $\mathrm{rank}\,J(\mathbb{Q}) \le g + \rho(J) - 1$ where $\rho$ is the Néron–Severi rank; it succeeds at $g=3$, $p=13$ but the required explicit $p$-adic heights, Coleman integrals, and models of $X_{ns}^{+}(p)$ become computationally prohibitive already at $p=17$ ($g=6$) and are not a uniform-in-$p$ argument in any case.
- **Uniformity is qualitatively harder.** Faltings/Vojta give finiteness for each fixed curve but no bound uniform in the family $\{X_E(p)\}_E$. Uniform Mordell–Lang results (Dimitrov–Gao–Habegger; Kühne) bound $\\#X(\mathbb{Q})$ in terms of $g$ and the rank, but the rank of $\mathrm{Jac}\,X_E(p)$ is uncontrolled as $E$ varies.
- **Twists have no moduli interpretation over $\mathbb{Q}$.** $X_E(p)$ is a twist of $X(p)$ with no cusps rational in general, blocking the standard toolkit (Eisenstein quotients, $q$-expansions, Hecke correspondences over $\mathbb{Q}$).

## 6. The Gap

For (A): everything reduces to a single family. The precise open statement is

> For all primes $p \ge 17$, every $P \in X_{ns}^{+}(p)(\mathbb{Q})$ is a cusp or has CM $j$-invariant.

Section 4 proves this for $p \le 13$ and for all curves carrying an auxiliary isogeny; the barrier is exhibiting, uniformly in $p$, an obstruction to rational points on a one-cusp curve of genus $\sim p^2/24$ whose Jacobian has no known rank-deficient quotient. Equivalently: find a "nonsplit Runge" or a $p$-uniform Chabauty–Kim.

For (B): what is proved is finiteness for each fixed $(E,p)$ and boundedness in the geometric/function-field setting. The gap is the passage from "finite for each $E$" to "the finite set is the trivial one, for all $E$, once $p > 17$" — i.e. an effective, uniform height bound on $X_E(p)(\mathbb{Q})$ independent of $E$. No current method produces bounds independent of the Faltings height of $E$.

## 7. Current Research (as of June 2026)

- **Quadratic and higher Chabauty–Kim.** Groups at Oxford, Duke, Groningen, and MIT (Balakrishnan, Dogra, Müller, Tuitman, Vonk and collaborators) push explicit nonabelian Chabauty to higher genus and to $X_{ns}^{+}(17)$; the bottleneck is computing a plane model and $p$-adic heights. *(frontier — verify)*
- **Group-theoretic reduction.** Furio and Lombardo have recent work reducing Serre uniformity to images equal to the *full* normalizer $N_{ns}(p)$, eliminating proper subgroups for all but small $p$; combined with Le Fourn–Lemos this narrows the target considerably. *(frontier — verify)*
- **Isogeny and height methods.** Effective Faltings-style bounds (Le Fourn, Lombardo, von Känel–Matschke) and integral-point methods on modular curves aim at conductor-explicit versions of Serre's bound.
- **Uniform Mordell–Lang.** Applications of Dimitrov–Gao–Habegger and Kühne to families of twists $X_E(p)$; the missing input is a uniform rank bound.
- **Databases.** Continued extension of LMFDB isogeny/congruence data and Sutherland's `galrep` computations to larger conductor ranges, testing both conjectures empirically.

## 8. Future Work

- Develop a Runge-type method tolerating a single cusp, e.g. via Siegel units on $X_{ns}^{+}(p)$ over quadratic fields where extra cusps appear.
- Find a rank-deficient quotient of $J_{ns}^{+}(p)$ analogous to Mazur's Eisenstein quotient, perhaps from the nonsplit analogue of the Eisenstein ideal.
- Prove a uniform bound on $\mathrm{rank}\,\mathrm{Jac}(X_E(p))(\mathbb{Q})$ in terms of $p$ alone, feeding into uniform Mordell–Lang to settle Frey–Mazur.
- Transfer the Bakker–Tsimerman function-field proof to the arithmetic setting via degeneration or an arithmetic Hodge-theoretic analogue of their monodromy argument.
- Settle $p = 17$ and $p = 19$ for the nonsplit Cartan case explicitly; these would be the first new cases since 2019.

## 9. Key References

- **[Foundational]** J.-P. Serre. *Propriétés galoisiennes des points d'ordre fini des courbes elliptiques.* Inventiones Mathematicae **15** (1972), 259–331.
- **[Foundational]** B. Mazur. *Rational isogenies of prime degree.* Inventiones Mathematicae **44** (1978), 129–162.
- **[Foundational]** B. Mazur. *Rational points on modular curves.* In: Modular Functions of One Variable V, Lecture Notes in Math. **601**, Springer, 1977.
- **[Foundational]** A. Kraus, J. Oesterlé. *Sur une question de B. Mazur.* Mathematische Annalen **293** (1992), 259–275.
- **[SOTA]** Y. Bilu, P. Parent. *Serre's uniformity problem in the split Cartan case.* Annals of Mathematics **173** (2011), 569–584.
- **[SOTA]** Y. Bilu, P. Parent, M. Rebolledo. *Rational points on $X_0^{+}(p^r)$.* Annales de l'Institut Fourier **63** (2013), 957–984.
- **[SOTA]** J. Balakrishnan, N. Dogra, J. S. Müller, J. Tuitman, J. Vonk. *Explicit Chabauty–Kim for the split Cartan modular curve of level 13.* Annals of Mathematics **189** (2019), 885–944.
- **[SOTA]** J. Balakrishnan, N. Dogra, J. S. Müller, J. Tuitman, J. Vonk. *Quadratic Chabauty for modular curves: algorithms and examples.* Compositio Mathematica **159** (2023), 1111–1152.
- **[SOTA]** T. Bakker, J. Tsimerman. *$p$-torsion monodromy representations of elliptic curves over geometric function fields.* Annals of Mathematics **184** (2016), 709–744.
- **[SOTA]** J. Cremona, N. Freitas. *Global methods for the symplectic type of congruences between elliptic curves.* Revista Matemática Iberoamericana **38** (2022), 1–32.
- **[SOTA]** J. Rouse, A. V. Sutherland, D. Zureick-Brown. *$\ell$-adic images of Galois for elliptic curves over $\mathbb{Q}$.* Forum of Mathematics, Sigma **10** (2022), e62.
- **[Computational]** A. V. Sutherland. *Computing images of Galois representations attached to elliptic curves.* Forum of Mathematics, Sigma **4** (2016), e4.
- **[Partial results]** S. Le Fourn, P. Lemos. *Residual Galois representations of elliptic curves with image contained in the normaliser of a nonsplit Cartan.* Algebra & Number Theory **15** (2021), 747–771.
- **[Partial results]** P. Lemos. *Serre's uniformity conjecture for elliptic curves with rational cyclic isogenies.* Transactions of the AMS **371** (2019), 137–146.
- **[Survey]** K. Rubin, A. Silverberg. *Families of elliptic curves with constant mod $p$ representations.* In: Elliptic Curves, Modular Forms & Fermat's Last Theorem, International Press, 1995.
- **[Survey]** B. Baran. *An exceptional isomorphism between modular curves of level 13.* Journal of Number Theory **145** (2014), 273–300.

## 10. Worked Example / Concrete Special Case

**(a) Why $C = 37$ is the expected constant.** Take $p = 37$. By Mazur, a non-CM $E/\mathbb{Q}$ with a rational $37$-isogeny exists: $X_0(37)$ has non-cuspidal rational points with
$$j = -7 \cdot 11^3 = -9317, \qquad j = -7\cdot 137^3 \cdot 2083^3 .$$
For these curves $\mathrm{im}\,\rho_{E,37}$ lies in a Borel subgroup, so $\rho_{E,37}$ is **not** surjective. Order of $\mathrm{GL}_2(\mathbb{F}_{37})$ is $(37^2-1)(37^2-37) = 1368 \cdot 1332 = 1{,}822{,}176$; a Borel has order $(37-1)^2\cdot 37 = 47{,}952$, index $38$. So the image has index $38$ — a genuine failure of surjectivity at $p=37$, and no non-CM failure is known for any larger $p$. This is exactly why the conjecture is stated for $p > 37$ and not $p > 13$.

**(b) The level-13 case, resolved.** $X_s(13) \cong X_{ns}^{+}(13)$ has genus $g = 3$; its Jacobian has $\mathrm{rank}\,J(\mathbb{Q}) = 3$, so Chabauty–Coleman ($\mathrm{rank} < g$) fails. Quadratic Chabauty uses $\rho(J) = 3$ and the condition $\mathrm{rank} \le g + \rho - 1 = 5$, which holds. BDMTV found exactly $7$ rational points: $1$ cusp and $6$ CM points, with $j$-invariants
$$j \in \{0,\; 54000,\; -12288000,\; 1728,\; 287496,\; -884736\},$$
corresponding to CM by discriminants $-3,-12,-27,-4,-16,-19$. Conclusion: no non-CM $E/\mathbb{Q}$ has mod-$13$ image in a Cartan normalizer. The same computation at $p=17$ needs $g=6$, and no comparable model or height computation is available.

**(c) A Frey–Mazur counterexample at $p=5$.** Fix $E/\mathbb{Q}$. The twist $X_E(5)$ has genus $0$ and possesses a rational point (the pair $(E,\mathrm{id})$), hence $X_E(5) \cong \mathbb{P}^1_{\mathbb{Q}}$ and $X_E(5)(\mathbb{Q})$ is infinite. Each non-cuspidal point gives $E'$ with $E'[5] \cong E[5]$ as Galois modules. Since $E$ has only finitely many curves in its $\mathbb{Q}$-isogeny class (at most $8$, by Mazur), infinitely many of these $E'$ are **non-isogenous** to $E$. Concretely, with $E = 11a1: y^2 + y = x^3 - x^2 - 10x - 20$, the curves $11a1, 11a2, 11a3$ are $5$-isogenous to each other — not counterexamples — but the Rubin–Silverberg family attached to $E$ produces infinitely many further $5$-congruent curves of unbounded conductor outside this class. The same construction dies at $p \ge 7$ because $g(X_E(7)) = 3 > 0$, and Faltings gives finiteness; the conjecture asserts that beyond $p = 17$ the finite set contains nothing new.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*