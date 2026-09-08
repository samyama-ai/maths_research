---
id: 02-algebra-group-theory/inverse-galois-problem
title: "Inverse Galois Problem"
topic: 02-algebra-group-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Inverse Galois Problem

> **Topic:** Algebra & Group Theory · **ID:** `02-algebra-group-theory/inverse-galois-problem` · **Status:** open

## 1. Problem Statement / Conjecture

**Question (Inverse Galois Problem, IGP).** Is every finite group $G$ isomorphic to $\mathrm{Gal}(L/\mathbb{Q})$ for some finite Galois extension $L/\mathbb{Q}$?

A complete positive solution requires, for each finite group $G$, a construction of a number field $L$ with $L/\mathbb{Q}$ normal and separable and $\mathrm{Aut}(L/\mathbb{Q}) \cong G$. A disproof requires exhibiting a single finite group $G$ that is provably not a quotient of the absolute Galois group $G_{\mathbb{Q}} = \mathrm{Gal}(\overline{\mathbb{Q}}/\mathbb{Q})$.

Equivalently: is $G_\mathbb{Q}$ **surjective onto every finite group**, i.e. does every finite group occur as a continuous quotient of the profinite group $G_\mathbb{Q}$? Note $G_\mathbb{Q}$ has cardinality $2^{\aleph_0}$, so no cardinality obstruction exists; and no known invariant of $G_\mathbb{Q}$ (its cohomological dimension, its cyclotomic character, its decomposition groups) rules out any finite group. The problem is open even though not a single candidate counterexample is known.

Two standard strengthenings:

- **Regular IGP.** Realize $G$ as $\mathrm{Gal}(L/\mathbb{Q}(t))$ with $L/\mathbb{Q}(t)$ *regular*, i.e. $L \cap \overline{\mathbb{Q}} = \mathbb{Q}$. By Hilbert irreducibility this implies the IGP for $G$ over $\mathbb{Q}$ and over every number field.
- **Shafarevich's conjecture.** $\mathrm{Gal}(\overline{\mathbb{Q}}/\mathbb{Q}^{\mathrm{ab}})$ is a free profinite group of countably infinite rank. This implies IGP over $\mathbb{Q}^{\mathrm{ab}}$ but not over $\mathbb{Q}$.

## 2. Mathematical Foundations

Let $K$ be a field, $\overline{K}$ a separable closure, $G_K=\mathrm{Gal}(\overline{K}/\overline{K}\cap K^{\mathrm{sep}})$ the absolute Galois group with the Krull topology. The Galois correspondence gives an inclusion-reversing bijection between closed subgroups of $G_K$ and subextensions of $K^{\mathrm{sep}}/K$; finite quotients of $G_K$ correspond to finite Galois extensions.

**Hilbert Irreducibility Theorem (1892).** If $f(t,X)\in\mathbb{Q}(t)[X]$ is irreducible, the set of $t_0\in\mathbb{Q}$ with $f(t_0,X)$ irreducible is Zariski-dense (indeed has density $1$ in a suitable counting). Consequently, if $\mathrm{Gal}(f/\mathbb{Q}(t)) \cong G$ with $\mathbb{Q}$ algebraically closed in the splitting field, then $\mathrm{Gal}(f(t_0,X)/\mathbb{Q}) \cong G$ for infinitely many $t_0$.

**Riemann existence theorem / geometric monodromy.** For $r$ branch points $P_1,\dots,P_r \in \mathbb{P}^1(\mathbb{C})$,
$$\pi_1^{\mathrm{top}}\!\left(\mathbb{P}^1(\mathbb{C})\setminus\{P_1,\dots,P_r\}\right) = \left\langle \gamma_1,\dots,\gamma_r \;\middle|\; \gamma_1\gamma_2\cdots\gamma_r = 1\right\rangle,$$
a free group of rank $r-1$. Hence $G$ is a Galois group over $\mathbb{C}(t)$ for every finite $G$: choose generators $g_1,\dots,g_r$ with $\prod g_i = 1$. Grothendieck's specialization gives $\pi_1^{\mathrm{alg}}(\mathbb{P}^1_{\overline{\mathbb{F}}_p}\setminus S)$ as the prime-to-$p$ completion. The whole difficulty of the IGP is **descent of the field of definition** from $\mathbb{C}$ (or $\overline{\mathbb{Q}}$) to $\mathbb{Q}$.

**Rigidity criterion (Belyi–Fried–Matzat–Thompson).** Let $\mathbf{C}=(C_1,\dots,C_r)$ be conjugacy classes of $G$ with $Z(G)=1$. Set
$$\Sigma(\mathbf{C}) = \{(g_1,\dots,g_r)\in C_1\times\cdots\times C_r : g_1\cdots g_r = 1,\ \langle g_1,\dots,g_r\rangle = G\}.$$
$\mathbf{C}$ is **rigid** if $G$ acts simply transitively on $\Sigma(\mathbf{C})$ by simultaneous conjugation, i.e. $|\Sigma(\mathbf{C})| = |G|$. $\mathbf{C}$ is **rational** if for every $m$ coprime to $|G|$ the class multiset $(C_1^m,\dots,C_r^m)$ equals $(C_1,\dots,C_r)$ up to permutation. 

> **Theorem.** If $\mathbf{C}$ is rigid and rational and $Z(G)=1$, then $G$ occurs regularly as $\mathrm{Gal}(L/\mathbb{Q}(t))$, branched over $r$ rational points; hence $G$ is a Galois group over $\mathbb{Q}$.

The class number $|\Sigma(\mathbf{C})|$ is computable from the character table by Frobenius' formula: for $r=3$,
$$\left|\{(g_1,g_2,g_3)\in C_1\times C_2\times C_3: g_1g_2g_3=1\}\right| = \frac{|C_1||C_2||C_3|}{|G|}\sum_{\chi \in \mathrm{Irr}(G)} \frac{\chi(c_1)\chi(c_2)\chi(c_3)}{\chi(1)}.$$

**Embedding problems.** Given a surjection $\alpha: G_\mathbb{Q}\twoheadrightarrow Q$ and $\pi: G \twoheadrightarrow Q$, does $\alpha$ lift to $\tilde\alpha: G_\mathbb{Q}\to G$? For central $\ker\pi$ the obstruction lies in $H^2(G_\mathbb{Q},\ker\pi)$; the IGP for solvable groups is solved by iterating solvable embedding problems.

## 3. History & State of the Art (SOTA)

- **1771/1830s.** Lagrange and Galois pose the direct problem; the inverse question is implicit in Hilbert's work.
- **1892.** Hilbert proves irreducibility and realizes $S_n$ and $A_n$ over $\mathbb{Q}$ for all $n$.
- **1937.** Scholz and Reichardt realize all $p$-groups of odd order $p$.
- **1954.** Shafarevich: every finite **solvable** group is a Galois group over every number field (the original argument had a gap at the prime $2$, later repaired; see Ishkhanov–Lur'e–Faddeev's exposition).
- **1974.** Shih realizes $\mathrm{PSL}_2(\mathbb{F}_p)$ over $\mathbb{Q}$ for $p$ with $\left(\frac{q}{p}\right)=-1$ for some $q\in\{2,3,7\}$, using modular curves.
- **1979.** Belyi realizes most finite simple groups of Lie type over $\mathbb{Q}^{\mathrm{ab}}$; his three-point-cover theorem seeds rigidity.
- **1984.** Thompson realizes the Monster $\mathbb{M}$ over $\mathbb{Q}$ via a rigid triple of classes $(2A,3B,29A)$.
- **1994–95.** Harbater, Raynaud (Abhyankar's conjecture), and Pop settle the geometric case: every finite group is a Galois group over $K(t)$ for $K$ complete with respect to a nontrivial discrete valuation (e.g. $\mathbb{Q}_p(t)$, $\overline{\mathbb{F}}_p((u))(t)$) — patching methods.
- **2001–present.** Klüners–Malle's database realizes every transitive group of degree $\le 15$ over $\mathbb{Q}$; automorphic methods (Khare–Larsen–Savin; Dieulefait–Wiese) produce large families of classical groups over finite fields.

## 4. Partial Results / Verified Cases

| Class | Status over $\mathbb{Q}$ | Source |
|---|---|---|
| Abelian $G$ | Solved (Kronecker–Weber: subfields of $\mathbb{Q}(\zeta_n)$) | classical |
| Solvable $G$ | Solved, all number fields | Shafarevich 1954 |
| $S_n$, $A_n$, all $n$ | Solved, regularly over $\mathbb{Q}(t)$ | Hilbert 1892 |
| 25 of the 26 sporadic simple groups | Solved; **$M_{23}$ open** | Matzat, Thompson, Hoyden-Siedersleben, Pahlings |
| Monster $\mathbb{M}$ (order $\approx 8\times10^{53}$) | Solved via rigid triple | Thompson 1984 |
| Transitive groups of degree $\le 15$ | All realized, explicit polynomials | Klüners–Malle 2001 |
| $\mathrm{PSL}_2(\mathbb{F}_p)$ | Known for $p \le 11$ and all $p$ in explicit congruence families; general $p$ open | Shih 1974; Zywina 2013 |
| $\mathrm{PSp}_{2n}(\mathbb{F}_{\ell^k})$, $\mathrm{PGL}_2$ | Infinitely many $\ell$ for each $n$, via modular/automorphic Galois representations | Dieulefait–Wiese 2011; Khare–Larsen–Savin 2008 |
| Every finite $G$ over $\mathbb{C}(t)$, $\overline{\mathbb{Q}}(t)$ | Solved (Riemann existence) | classical |
| Every finite $G$ over $K(t)$, $K$ complete discretely valued | Solved | Harbater 1994, Pop 1995, Haran–Völklein 1996 |
| Every finite $G$ over $\mathbb{Q}^{\mathrm{ab}}$? | Open; implied by Shafarevich's freeness conjecture | — |

## 5. Principal Obstacles

- **Rigidity is a finite resource.** The rigidity/rationality criterion succeeds only when $|\Sigma(\mathbf{C})| = |G|$ exactly. For most groups the character-theoretic count exceeds $|G|$ (there are "too many" generating tuples), and the braid group $B_r$ acts on $\Sigma(\mathbf{C})/G$ with several orbits, none of them necessarily $\mathbb{Q}$-rational. Weakenings (weak rigidity, Fried's braid-orbit criterion, the "GAR" and "GAP" realizations of Matzat) enlarge the reach but do not remove the finiteness.
- **Rational points on Hurwitz spaces.** Fried–Völklein recast regular realizations as $\mathbb{Q}$-points on the Hurwitz moduli space $\mathcal{H}_r(G,\mathbf{C})$. These spaces have large genus and dimension $r-3$ (after normalizing three branch points); no general machinery produces rational points on high-genus varieties. Faltings' theorem in fact *forbids* many points once genus $\ge 2$.
- **Patching does not descend.** Harbater–Pop–Raynaud formal/rigid patching works because $K$ complete gives a "local–global" gluing on the formal fibre. $\mathbb{Q}$ has no such completeness; the local realizations over each $\mathbb{Q}_p$ exist but a global one need not, and there is no adelic patching theorem for $\mathbb{Q}$.
- **Non-split embedding problems.** Building $G$ from a realized quotient $Q$ requires solving an embedding problem with kernel $N$. When $N$ is nonabelian the obstruction is not cohomological in a usable sense, and even for abelian $N$ the class $\in H^2(G_\mathbb{Q},N)$ is only computable when $N$ is a trivial or cyclotomic module.
- **No conjectural counterexample mechanism.** Absent any invariant that could obstruct a group, there is no target for a disproof either, so the problem admits no known "hard direction" to attack.

## 6. The Gap

Proven: all solvable groups; all symmetric/alternating groups; all groups admitting a rigid rational class vector; all groups over $\mathbb{C}(t)$ and over complete discretely valued base fields; every transitive group of degree $\le 15$.

Missing: a mechanism that produces a $\mathbb{Q}$-rational point on $\mathcal{H}_r(G,\mathbf{C})$ for an *arbitrary* finite simple group $G$ — equivalently, a way to descend the Riemann-existence cover from $\mathbb{C}$ to $\mathbb{Q}$ without the accidental uniqueness that rigidity supplies. Concretely: by the classification of finite simple groups plus solvability of embedding problems in favourable cases, it would suffice to realize (regularly, with GAR property) every finite simple group. The smallest sharp instance of the gap is $M_{23}$: a sporadic group of order $10{,}200{,}960$ whose character table admits no rigid rational triple, and for which no realization over $\mathbb{Q}$ is known.

## 7. Current Research (as of June 2026)

- **Hurwitz-space homological stability.** Ellenberg–Venkatesh–Westerland's stability theorem for Hurwitz spaces over $\mathbb{F}_q(t)$ has been extended by Landesman–Levy to non-splitting components, giving counts of $G$-extensions of $\mathbb{F}_q(t)$ for $q$ large. *(frontier — verify)* Transfer of these function-field counts to $\mathbb{Q}$ remains conjectural.
- **Automorphic and modular constructions.** Groups $\mathrm{PSp}_{2n}(\mathbb{F}_\ell)$, $\mathrm{G}_2(\mathbb{F}_\ell)$, and other Lie-type groups are realized by proving large-image results for residual Galois representations attached to automorphic forms (Wiese, Dieulefait, Arias-de-Reyna, and collaborators, Barcelona/Luxembourg).
- **Explicit descent and $M_{23}$.** Computational group theory groups (Kassel/Malle school; Klüners at Paderborn) continue to search braid orbits and higher-genus Hurwitz components for $M_{23}$; no accepted realization exists.
- **Counting and Malle's conjecture.** Malle's asymptotic $N(\mathbb{Q},G;X) \sim c\,X^{a(G)}(\log X)^{b(G)-1}$ is a quantitative refinement; Klüners' 2005 counterexample ($G = C_3\wr C_2$) shows the $\log$ exponent needs correction. Work of Bhargava-school authors on $S_n$ for $n\le 5$ (and recent $n=6$ progress) *(frontier — verify)* bears on the density side.
- **Field arithmetic.** Shafarevich's conjecture on $\mathrm{Gal}(\overline{\mathbb{Q}}/\mathbb{Q}^{\mathrm{ab}})$ and Fried–Jarden's theory of PAC fields continue as the structural route (Jarden, Haran, Pop).

## 8. Future Work

- Prove regular realizability with the **GAR property** for all finite simple groups; combined with Shafarevich-type embedding arguments this yields the full IGP.
- Develop a descent theory for Hurwitz components with non-rational braid orbits — e.g. using the cyclotomic action and the Fried "Modular Tower" program to detect obstructions at each level.
- Settle $M_{23}$, either by an explicit cover of genus $>0$ with a rational point or by a new obstruction.
- Prove Shafarevich's freeness conjecture for $\mathrm{Gal}(\overline{\mathbb{Q}}/\mathbb{Q}^{\mathrm{ab}})$, then attack the descent from $\mathbb{Q}^{\mathrm{ab}}$ to $\mathbb{Q}$ (this last step is itself an embedding problem with abelian quotient and is not known to be tractable).
- Import function-field statistics (EVW-type stability) into number-field heuristics to at least predict which groups should have small-discriminant realizations.

## 9. Key References

- **[Foundational]** D. Hilbert. *Ueber die Irreducibilität ganzer rationaler Functionen mit ganzzahligen Coefficienten.* Journal für die reine und angewandte Mathematik **110** (1892), 104–129. [DOI](https://doi.org/10.1515/crll.1892.110.104)
- **[Foundational]** I. R. Shafarevich. *Construction of fields of algebraic numbers with given solvable Galois group.* Izvestiya Akad. Nauk SSSR Ser. Mat. **18** (1954), 525–578.
- **[Foundational]** G. V. Belyi. *On Galois extensions of a maximal cyclotomic field.* Izvestiya Akad. Nauk SSSR Ser. Mat. **43** (1979), 267–276. [DOI](https://doi.org/10.1070/im1980v014n02abeh001096)
- **[Foundational]** J. G. Thompson. *Some finite groups which appear as $\mathrm{Gal}(L/K)$, where $K \subseteq \mathbb{Q}(\mu_n)$.* Journal of Algebra **89** (1984), 437–499.
- **[Foundational]** K.-y. Shih. *On the construction of Galois extensions of function fields and number fields.* Mathematische Annalen **207** (1974), 99–120. [DOI](https://doi.org/10.1007/bf01362150)
- **[Survey]** J.-P. Serre. *Topics in Galois Theory.* Jones and Bartlett, 1992 (2nd ed., A K Peters, 2008).
- **[Survey]** G. Malle and B. H. Matzat. *Inverse Galois Theory.* Springer Monographs in Mathematics, 1999; 2nd edition, Springer, 2018. [DOI](https://doi.org/10.1007/978-3-662-12123-8)
- **[Survey]** H. Völklein. *Groups as Galois Groups: An Introduction.* Cambridge Studies in Advanced Mathematics 53, Cambridge University Press, 1996.
- **[Survey]** M. D. Fried and M. Jarden. *Field Arithmetic.* Ergebnisse der Mathematik, 3rd edition, Springer, 2008.
- **[SOTA]** M. Raynaud. *Revêtements de la droite affine en caractéristique $p>0$ et conjecture d'Abhyankar.* Inventiones Mathematicae **116** (1994), 425–462.
- **[SOTA]** D. Harbater. *Abhyankar's conjecture on Galois groups over curves.* Inventiones Mathematicae **117** (1994), 1–25. [DOI](https://doi.org/10.1007/bf01232232)
- **[SOTA]** F. Pop. *Étale Galois covers of affine smooth curves.* Inventiones Mathematicae **120** (1995), 555–578. [DOI](https://doi.org/10.1007/bf01241142)
- **[SOTA]** M. D. Fried and H. Völklein. *The inverse Galois problem and rational points on moduli spaces.* Mathematische Annalen **290** (1991), 771–800. [DOI](https://doi.org/10.1007/bf01459271)
- **[SOTA]** C. Khare, M. Larsen and G. Savin. *Functoriality and the inverse Galois problem.* Compositio Mathematica **144** (2008), 541–564. [DOI](https://doi.org/10.1112/s0010437x07003284)
- **[SOTA]** L. Dieulefait and G. Wiese. *On modular forms and the inverse Galois problem.* Transactions of the American Mathematical Society **363** (2011), 4569–4584.
- **[SOTA]** J. S. Ellenberg, A. Venkatesh and C. Westerland. *Homological stability for Hurwitz spaces and the Cohen–Lenstra conjecture over function fields.* Annals of Mathematics **183** (2016), 729–786. [DOI](https://doi.org/10.4007/annals.2016.183.3.1)
- **[Computational]** J. Klüners and G. Malle. *A database for field extensions of the rationals.* LMS Journal of Computation and Mathematics **4** (2001), 182–196. [DOI](https://doi.org/10.1112/s1461157000000851)
- **[Computational]** J. Klüners. *A counterexample to Malle's conjecture on the asymptotics of discriminants.* Comptes Rendus Mathématique, Académie des Sciences Paris **340** (2005), 411–414.

## 10. Worked Example / Concrete Special Case

**Goal:** realize $G = S_3$ regularly over $\mathbb{Q}(t)$ by rigidity, then descend to $\mathbb{Q}$.

**Step 1 — rigidity count.** Take $r=3$ and $\mathbf{C} = (C_2, C_2, C_3)$ where $C_2$ is the class of transpositions ($|C_2|=3$) and $C_3$ the class of $3$-cycles ($|C_3|=2$). Count triples with $g_1g_2g_3=1$: pick $g_1,g_2$ transpositions with $g_1 \ne g_2$ (so that $g_3=(g_1g_2)^{-1}$ is a $3$-cycle), giving $3\cdot 2 = 6$ triples, each generating $S_3$. Thus
$$|\Sigma(\mathbf{C})| = 6 = |S_3|,$$
so $S_3$ acts simply transitively: $\mathbf{C}$ is **rigid**. Also $Z(S_3)=1$, and every class of $S_3$ is rational (character table is integral), so $\mathbf{C}$ is **rational**. The rigidity theorem predicts a regular $S_3$-extension of $\mathbb{Q}(t)$ branched over three $\mathbb{Q}$-points.

**Step 2 — explicit cover.** Take $\beta(x) = x^2(3-2x) = 3x^2 - 2x^3$, a degree-$3$ map $\mathbb{P}^1\to\mathbb{P}^1$. Then $\beta'(x)=6x(1-x)$, so the critical points are $x=0$ with $\beta(0)=0$ and $x=1$ with $\beta(1)=1$; also $x=\infty$ is totally ramified over $\infty$. Ramification data:
$$\text{over } 0:\ (2,1),\qquad \text{over } 1:\ (2,1),\qquad \text{over } \infty:\ (3).$$
This is exactly the branch cycle description $(C_2, C_2, C_3)$ — a Belyi map, with monodromy group $S_3$.

**Step 3 — the field extension.** Set $t = 3x^2 - 2x^3$, so $\mathbb{Q}(x)/\mathbb{Q}(t)$ is degree $3$, cut out by
$$f(t,X) = 2X^3 - 3X^2 + t = 0 .$$
Its discriminant is $\mathrm{disc}(f) = -108\,t(t-1)$ up to squares, i.e. $\mathrm{disc}(f)\equiv -3\,t(t-1) \pmod{(\mathbb{Q}(t)^\times)^2}$. Since $-3t(t-1)$ is not a square in $\mathbb{Q}(t)$, the Galois group of the splitting field $L$ is $S_3$, not $A_3$. Moreover $\mathbb{Q}$ is algebraically closed in $L$ (the cover has a $\mathbb{Q}$-rational totally ramified point at $\infty$), so $L/\mathbb{Q}(t)$ is **regular** with group $S_3$.

**Step 4 — specialize (Hilbert).** Put $t=2$: $\;f(2,X) = 2X^3-3X^2+2$. Candidate rational roots $\pm1,\pm2,\pm\tfrac12$ give values $1,-3,6,-24,\tfrac32$ — none vanish, so $f(2,X)$ is irreducible over $\mathbb{Q}$. Its discriminant is $-3\cdot 2\cdot 1 = -6$ times a square, and $-6$ is not a square in $\mathbb{Q}$. Hence
$$\mathrm{Gal}\big(f(2,X)/\mathbb{Q}\big) \cong S_3,$$
realized by the splitting field of $2X^3-3X^2+2$, a degree-$6$ field containing $\mathbb{Q}(\sqrt{-6})$.

This is the complete pipeline — character-table count $\Rightarrow$ rigid triple $\Rightarrow$ three-point cover $\Rightarrow$ regular extension of $\mathbb{Q}(t)$ $\Rightarrow$ specialization — and it is precisely this pipeline that fails at Step 1 for groups such as $M_{23}$, where no rigid rational class vector exists.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*