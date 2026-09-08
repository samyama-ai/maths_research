---
id: 02-algebra-group-theory/broues-abelian-defect-group-conjecture
title: "Broue's Abelian Defect Group Conjecture"
topic: 02-algebra-group-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Broué's Abelian Defect Group Conjecture

> **Topic:** Algebra & Group Theory · **ID:** `02-algebra-group-theory/broues-abelian-defect-group-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Let $p$ be a prime, $G$ a finite group, and $(K,\mathcal{O},k)$ a $p$-modular system large enough for $G$. Let $B$ be a block of $\mathcal{O}G$ with defect group $D$, and let $b$ be the Brauer correspondent of $B$, a block of $\mathcal{O}N_G(D)$ with the same defect group.

**Conjecture (Broué, 1990).** If $D$ is *abelian*, then $B$ and $b$ are derived equivalent:
$$D^b(B\text{-mod}) \;\simeq\; D^b(b\text{-mod})$$
as triangulated categories.

Equivalently (Rickard's theorem), there exists a two-sided tilting complex $X$ of $(B,b)$-bimodules with $X \otimes^{\mathbf{L}}_{b} X^\vee \cong B$ and $X^\vee \otimes^{\mathbf{L}}_{B} X \cong b$ in the respective homotopy categories.

A proof must supply such an equivalence for *every* prime $p$, every finite group $G$, and every block with abelian defect group. A disproof requires one block $B$ with abelian $D$ for which $B$ and $b$ have non-equivalent derived module categories — for instance by exhibiting a derived invariant (number of ordinary irreducible characters, number of simple modules, elementary divisors of the Cartan matrix, Hochschild cohomology ring, centre) that differs.

Two strengthenings are usually studied alongside it:

- **Splendid (Rickard) version:** the tilting complex may be chosen with components that are $p$-permutation $\mathcal{O}[G\times N_G(D)]$-modules with vertices in $\Delta D$. This forces compatibility with Brauer constructions at every $p$-subgroup, hence induces derived equivalences of all local blocks.
- **Geometric version (for groups of Lie type):** for $G$ finite reductive in non-defining characteristic, the complex should be realized by the $\ell$-adic cohomology of a Deligne–Lusztig variety.

Abelianness is essential: the conclusion is false for non-abelian $D$ (e.g. $G = $ a $p$-group of maximal class, or $B$ the principal $2$-block of $A_6$ versus its correspondent), where $k(B) \ne k(b)$ in general.

## 2. Mathematical Foundations

**Blocks.** $\mathcal{O}G = \bigoplus_i B_i$ with $B_i = \mathcal{O}Ge_i$ for primitive orthogonal idempotents $e_i$ of $Z(\mathcal{O}G)$. Each $B$ is a symmetric $\mathcal{O}$-algebra via the trace form $\lambda(\sum a_g g) = a_1$.

**Defect groups.** $B$ is a direct summand of the $\mathcal{O}[G\times G]$-module $\mathcal{O}G$; its vertex is $\Delta D = \{(d,d): d\in D\}$ for a $p$-subgroup $D \le G$ unique up to $G$-conjugacy. Equivalently, $D$ is minimal such that the relative trace map $\mathrm{Tr}^G_D : (\mathcal{O}G)^D \to (\mathcal{O}G)^G$ hits $e_B$. The defect $d$ satisfies $|D| = p^d$, and $\nu_p(\chi(1)) \ge \nu_p(|G|) - d$ for all $\chi \in \mathrm{Irr}(B)$, with equality defining the *height-zero* characters.

**Brauer correspondence.** For $P \le G$ a $p$-subgroup, the Brauer homomorphism
$$\mathrm{Br}_P : (kG)^P \longrightarrow kC_G(P), \qquad \sum_{g} a_g g \;\longmapsto\; \sum_{g \in C_G(P)} a_g g$$
is a surjective algebra map. If $D$ is a defect group of $B$, then $\mathrm{Br}_D(e_B)$ is a block idempotent sum, and the Brauer correspondent $b$ of $B$ is the unique block of $\mathcal{O}N_G(D)$ with $b^G = B$.

**Local structure.** When $D$ is abelian, $D \le C_G(D)$, the fusion system $\mathcal{F} = \mathcal{F}_D(G,B)$ is controlled by $N_G(D)$ (Burnside), and the *inertial quotient* is $E = N_G(D,e_D)/DC_G(D)$, a $p'$-group acting faithfully on $D$. If moreover $C_G(D) = D \times (\text{$p'$-part})$ and $b$ is nilpotent-covered, Külshammer–Puig theory gives
$$b \;\cong\; \mathrm{Mat}_n\!\left(\mathcal{O}_\alpha[D \rtimes E]\right)$$
for a $2$-cocycle $\alpha \in H^2(E,\mathcal{O}^\times)$. So the conjecture asserts that an arbitrary abelian-defect block is derived equivalent to an explicitly presented twisted group algebra.

**Derived invariants forced by the conjecture.**
$$k(B) = k(b),\quad l(B) = l(b),\quad \mathrm{Cartan}(B) \sim \mathrm{Cartan}(b),\quad HH^*(B) \cong HH^*(b),\quad Z(B)\cong Z(b).$$
It implies **Alperin's weight conjecture** and the **Alperin–McKay conjecture** for abelian-defect blocks, and Broué showed a derived equivalence induces a *perfect isometry* $I : \mathbb{Z}\mathrm{Irr}(b) \to \mathbb{Z}\mathrm{Irr}(B)$, i.e. a bijection with signs whose character $\mu(g,h) = \sum \pm \chi(g)\overline{\chi'(h)}$ satisfies the integrality and separation conditions
$$\frac{\mu(g,h)}{|C_G(g)|} \in \mathcal{O}, \qquad \mu(g,h) = 0 \text{ unless } g,h \text{ are both } p\text{-singular or both } p\text{-regular.}$$

## 3. History & State of the Art

- **1990.** Michel Broué states the conjecture in *Isométries parfaites, types de blocs, catégories dérivées* (Astérisque 181–182), motivated by perfect isometries observed between $\mathrm{Irr}(B)$ and $\mathrm{Irr}(b)$ in cyclic-defect and generic-block computations, and by Broué–Malle–Michel's generic block theory for finite reductive groups.
- **1989–1991.** Rickard's Morita theory for derived categories (*Morita theory for derived categories*, J. LMS 39, 1989) makes "derived equivalent" a workable notion; Rickard and Linckelmann settle blocks with **cyclic** defect groups (Brauer tree algebras are derived equivalent to the corresponding star).
- **1996.** Rickard introduces **splendid** equivalences (Proc. LMS 72), giving descent from $k$ to $\mathcal{O}$ and compatibility with local subgroups.
- **1996.** Marcus reduces the splendid conjecture, via Fong–Reynolds and Clifford theory, to blocks of quasi-simple groups — so the conjecture is in principle checkable against the classification of finite simple groups.
- **2008.** Chuang–Rouquier prove it for **all blocks of symmetric groups with abelian defect**, using $\mathfrak{sl}_2$-categorification and perverse/derived self-equivalences (Annals of Math. 167).
- **2013.** Craven–Rouquier develop **perverse equivalences** as the systematic mechanism, with algorithmic predictions for $\mathrm{Irr}$-bijections.
- **2017.** Bonnafé–Dat–Rouquier prove Jordan decomposition of blocks in the strong form (Annals 185), removing the connected-centre hypothesis from Bonnafé–Rouquier and reducing many Lie-type cases to quasi-isolated blocks.
- **2020s.** Case-by-case verification continues for sporadic and Lie-type quasi-simple groups (Koshitani, Kunugi, Müller, Dudas, Ruhstorfer, Livesey). No counterexample and no general proof.

## 4. Partial Results / Verified Cases

- **Cyclic defect groups** ($D \cong C_{p^n}$): fully proved (Rickard 1989; Linckelmann 1991 over $\mathcal{O}$; Rouquier 1998 for the splendid/geometric refinements).
- **$p$-solvable groups:** true — an abelian-defect block of a $p$-solvable group is Morita (not merely derived) equivalent to its correspondent up to the Fong–Reynolds reduction (Dade; Harris–Linckelmann, 1997).
- **Klein four defect group** $D \cong C_2\times C_2$: proved. Every such block is derived equivalent to exactly one of $k[C_2\times C_2]$, $kA_4$, $B_0(kA_5)$ (Erdmann's classification of tame algebras plus Rickard; structure completed by Craven–Eaton–Kessar–Linckelmann, Math. Z. 268, 2011).
- **Elementary abelian defect of order 8** ($D \cong C_2^3$): Alperin's and Broué's conjectures verified by Kessar–Koshitani–Linckelmann (J. reine angew. Math. 671, 2012).
- **Symmetric and alternating groups, and their double covers (partially):** all abelian-defect blocks of $S_n$ (Chuang–Rouquier 2008); wreath-product reductions in Chuang–Kessar (Bull. LMS 34, 2002) handle defect $C_p \wr$-type situations, and blocks of $S_n$ of $p$-weight $w < p$ are Morita equivalent to $B_0 \wr S_w$.
- **$\mathrm{GL}_n(q)$ in non-defining characteristic** with abelian defect: proved via $\mathfrak{sl}_2$/$\mathfrak{gl}_\infty$-categorification and Bonnafé–Rouquier Morita equivalences.
- **Principal $3$-blocks with $D \cong C_3\times C_3$:** verified for large families of quasi-simple groups (Koshitani–Kunugi and collaborators, from ~2000 onward), including $\mathrm{PSU}_3(q)$, $\mathrm{Sp}_4(q)$, $\mathrm{PSL}_3(q)$, and all sporadic groups with such defect.
- **Coxeter-element case for finite reductive groups:** Bonnafé–Rouquier (Nagoya Math. J. 183, 2006) and Dudas construct the equivalence from the cohomology of the Deligne–Lusztig variety attached to a Coxeter element, for $\ell \mid \Phi_h(q)$ with $h$ the Coxeter number.
- **Numerical consequences:** for abelian-defect blocks, the height-zero half of Brauer's height zero conjecture (all $\chi\in\mathrm{Irr}(B)$ have height $0$) is a theorem (Kessar–Malle, Annals 178, 2013), consistent with and predicted by Broué.

## 5. Principal Obstacles

- **Non-constructive existence.** Rickard's criterion converts the problem into finding a tilting complex, but there is no general recipe. Known constructions (Okuyama's iterated stable-equivalence method, Rouquier's perverse equivalences, Deligne–Lusztig cohomology) are all input-specific.
- **Stable equivalence does not lift for free.** In many cases one can build a stable equivalence of Morita type $B \simeq b$ from Broué's "gluing" of local data, but promoting a stable equivalence to a derived equivalence requires finding a suitable set of "$B$-simple images", which is an unstructured search. This is the single most common stopping point.
- **Character-theoretic techniques are too coarse.** Perfect isometries and isotypies are consequences, not causes; a perfect isometry carries no information about $\mathrm{Ext}$-groups, so it cannot produce the complex.
- **No functorial mechanism outside categorification.** The successes for $S_n$ and $\mathrm{GL}_n(q)$ come from a Kac–Moody $2$-representation acting on the union of blocks. Most groups carry no such action; sporadic groups and exceptional Lie types have no known categorified symmetry to exploit.
- **Bad primes in Lie type.** For $p \in \{2,3,5\}$ and exceptional groups, quasi-isolated blocks resist the Jordan-decomposition reduction; Bonnafé–Dat–Rouquier leaves these as genuine residual cases.
- **Cohomology of Deligne–Lusztig varieties is not known.** The geometric approach needs the full $\Lambda$-cohomology complex $R\Gamma_c(X(w),\Lambda)$ to be a tilting complex; even the ordinary $\ell$-adic cohomology of $X(w)$ for general $w$ is open, and torsion-freeness (the "disjointness/torsion" conjectures) is unproven.
- **CFSG-dependence.** Marcus's reduction makes the conjecture a statement about quasi-simple groups, but the resulting programme is an infinite family-by-family verification with no uniform argument in sight.

## 6. The Gap

The proven cases share one of three features: (i) the block algebra is *tame* or otherwise classified up to Morita equivalence ($D$ cyclic, $|D| \le 8$ for $p = 2$); (ii) the block sits inside a categorified family with an $\mathfrak{sl}_2$-action ($S_n$, $\mathrm{GL}_n(q)$); or (iii) a geometric model produces the complex directly (Coxeter case).

The general statement has none of these. The precise missing step is:

> Given an abelian-defect block $B$ and a stable equivalence of Morita type $B \simeq_{\mathrm{st}} b$ obtained by gluing local Morita equivalences over $\mathcal{F}$, decide in general whether it lifts to a derived equivalence — equivalently, produce a *canonical* tilting complex from the fusion system $\mathcal{F}_D(G,B)$ and the Külshammer–Puig class $\alpha$ alone.

Broué's conjecture would follow from a positive answer plus the (also open) claim that the local gluing always yields the stable equivalence. Currently there is no proof even that $k(B) = k(b)$ for abelian $D$ in general.

## 7. Current Research (as of June 2026)

- **Perverse-equivalence programme** (Rouquier, Craven, Dudas): compute the predicted $\mathrm{Irr}$-bijection combinatorially from a perversity function, then realize it; used to settle individual quasi-isolated blocks in exceptional Lie types. *(frontier — verify for $E_7$, $E_8$ at $p=3,5$.)*
- **Deligne–Lusztig geometry** (Dudas, Michel, Bonnafé, Rouquier): explicit computation of $R\Gamma_c$ for varieties beyond Coxeter type, and of the Hecke-algebra action on it.
- **Morita classification of abelian-defect blocks** (Eaton, Kessar, Külshammer, Livesey, Sambale): complete lists of Morita equivalence classes for small abelian $D$ — a route to Donovan's conjecture that simultaneously certifies Broué in those cases. Recent extensions cover $2$-blocks with abelian defect groups of rank $\le 4$. *(frontier — verify.)*
- **Inductive conditions and Lie-type reductions** (Ruhstorfer, Brough, Schaeffer Fry, Malle): the machinery built for the McKay and height-zero conjectures — the latter completed by Malle–Navarro–Schaeffer Fry–Tiep (Annals 200, 2024) — is being redirected at block equivalences.
- **Computational verification** (Koshitani, Kunugi, Müller, Noeske): GAP/MAGMA-driven confirmation for sporadic groups and small Lie-type groups; essentially all sporadic-group blocks with abelian defect are now handled.

## 8. Future Work

- Prove the **gluing conjecture**: that Broué's local Morita equivalences assemble into a stable equivalence of Morita type for every abelian-defect block; this is the natural first half.
- Find a **fusion-system-theoretic construction** of the tilting complex, depending only on $(\mathcal{F},\alpha)$, which would also imply Donovan's finiteness conjecture in the abelian case.
- Extend $2$-Kac–Moody categorification beyond type $A$: an $\mathfrak{sl}_2$-action on unions of blocks of classical groups in non-defining characteristic.
- Settle the **torsion-freeness** of $H^*_c(X(w),\mathbb{Z}_\ell)$ for regular $w$, which would give the geometric version uniformly for finite reductive groups.
- Complete the quasi-isolated exceptional-type cases at bad primes, finishing the CFSG-based programme.

## 9. Key References

- **[Foundational]** M. Broué. *Isométries parfaites, types de blocs, catégories dérivées.* Astérisque 181–182 (1990), 61–92.
- **[Foundational]** J. Rickard. *Morita theory for derived categories.* Journal of the London Mathematical Society 39 (1989), 436–456. [DOI](https://doi.org/10.1112/jlms/s2-39.3.436)
- **[Foundational]** J. Rickard. *Splendid equivalences: derived categories and permutation modules.* Proceedings of the London Mathematical Society 72 (1996), 331–358. [DOI](https://doi.org/10.1112/plms/s3-72.2.331)
- **[Foundational]** M. Linckelmann. *Derived equivalence for cyclic blocks over a $P$-adic ring.* Mathematische Zeitschrift 207 (1991), 293–304.
- **[Reduction]** A. Marcus. *On equivalences between blocks of group algebras: reduction to the simple components.* Journal of Algebra 184 (1996), 372–396. [DOI](https://doi.org/10.1006/jabr.1996.0265)
- **[SOTA]** J. Chuang, R. Rouquier. *Derived equivalences for symmetric groups and $\mathfrak{sl}_2$-categorification.* Annals of Mathematics 167 (2008), 245–298.
- **[SOTA]** C. Bonnafé, J.-F. Dat, R. Rouquier. *Derived categories and Deligne–Lusztig varieties II.* Annals of Mathematics 185 (2017), 609–670.
- **[SOTA]** C. Bonnafé, R. Rouquier. *Coxeter orbits and modular representations.* Nagoya Mathematical Journal 183 (2006), 1–34. [DOI](https://doi.org/10.1017/s0027763000009259)
- **[SOTA]** D. Craven, R. Rouquier. *Perverse equivalences and Broué's conjecture.* Advances in Mathematics 248 (2013), 1–58. [DOI](https://doi.org/10.1016/j.aim.2013.07.010)
- **[SOTA]** R. Kessar, S. Koshitani, M. Linckelmann. *Conjectures of Alperin and Broué for $2$-blocks with elementary abelian defect groups of order $8$.* Journal für die reine und angewandte Mathematik 671 (2012), 101–130. [DOI](https://doi.org/10.1515/crelle.2011.162)
- **[SOTA]** C. Eaton, R. Kessar, B. Külshammer, B. Sambale. *$2$-blocks with abelian defect groups.* Advances in Mathematics 254 (2014), 706–735.
- **[SOTA]** R. Kessar, G. Malle. *Quasi-isolated blocks and Brauer's height zero conjecture.* Annals of Mathematics 178 (2013), 321–384. [DOI](https://doi.org/10.4007/annals.2013.178.1.6)
- **[Related]** D. Craven, C. Eaton, R. Kessar, M. Linckelmann. *The structure of blocks with a Klein four defect group.* Mathematische Zeitschrift 268 (2011), 441–476. [DOI](https://doi.org/10.1007/s00209-010-0679-4)
- **[Survey]** M. Linckelmann. *The Block Theory of Finite Group Algebras*, Vols. I–II. London Mathematical Society Student Texts 91–92, Cambridge University Press, 2018.
- **[Survey]** R. Rouquier. *Derived equivalences and finite dimensional algebras.* Proceedings of the International Congress of Mathematicians, Madrid 2006, Vol. II, EMS, 191–221. [DOI](https://doi.org/10.4171/022-2/9)
- **[Survey]** J. Chuang, R. Kessar. *Symmetric groups, wreath products, Morita equivalences, and Broué's abelian defect group conjecture.* Bulletin of the London Mathematical Society 34 (2002), 174–184. [DOI](https://doi.org/10.1112/s0024609301008839)

## 10. Worked Example / Concrete Special Case

**Setup.** $p = 2$, $G = A_5$, $k$ algebraically closed of characteristic $2$. Then $|G| = 60 = 2^2\cdot 15$, a Sylow $2$-subgroup is $D = \langle (12)(34),(13)(24)\rangle \cong C_2\times C_2$ — abelian — and
$$N_G(D) = D \rtimes C_3 \cong A_4 .$$

**The two blocks.** $\mathrm{Irr}(A_5) = \{1, 3, 3', 4, 5\}$ (by degree). Since $2^2 \mid 4$, the degree-$4$ character lies in a block of defect $0$. Hence the principal block $B = B_0(kA_5)$ has
$$\mathrm{Irr}(B) = \{\chi_1,\chi_3,\chi_{3'},\chi_5\},\quad k(B) = 4,\qquad \mathrm{IBr}(B) = \{k, 2a, 2b\},\quad l(B) = 3 .$$
For $N_G(D) = A_4$: $\mathrm{Irr}(A_4) = \{1,\omega,\omega^2, 3\}$ and $|A_4| = 12 = 2^2\cdot 3$, so no character has degree divisible by $4$ and there is a single block $b = kA_4$ with $k(b) = 4$, $l(b) = 3$ (the three linear characters of $A_4/D \cong C_3$ reduce to the three simple modules).

**Numerical check.** Both blocks have Cartan matrix
$$C \;=\; \begin{pmatrix} 2 & 1 & 1\\ 1 & 2 & 1\\ 1 & 1 & 2\end{pmatrix}, \qquad \det C = 4 = |D|,$$
with elementary divisors $1,1,4$ — as required for a derived equivalence, which preserves the Cartan matrix up to $\mathbb{Z}$-congruence $C \mapsto P^{T}CP$, $P \in \mathrm{GL}_3(\mathbb{Z})$.

**Induced perfect isometry.** Broué's theory forces a sign-bijection $\mathrm{Irr}(B) \to \mathrm{Irr}(b)$ with degrees matching modulo $|D| = 4$ after signs. One valid choice:
$$\chi_1 \mapsto 1,\qquad \chi_5 \mapsto \omega,\qquad \chi_3 \mapsto -\omega^2,\qquad \chi_{3'}\mapsto \chi_3^{A_4},$$
checking degrees mod $4$: $1\equiv 1$, $5\equiv 1$, $-3 \equiv 1$... reading each side, $1\equiv1$, $5\equiv 1\equiv \omega(1)$, $3 \equiv 3 \equiv -1 \equiv -\omega^2(1)$, $3'\equiv 3 \equiv \chi_3^{A_4}(1)$. All consistent, and all four characters have height $0$, as Kessar–Malle guarantees for abelian defect.

**The equivalence.** $B$ and $b$ are **not** Morita equivalent — $kA_4$ is a twisted group algebra of $D\rtimes C_3$ while $B_0(kA_5)$ is not, and they have non-isomorphic Ext-quivers with relations. They *are* derived equivalent: Rickard produced a splendid tilting complex, and since $A_5 \cong \mathrm{SL}_2(4)$, the complex is realized geometrically by the cohomology of the Drinfeld curve
$$X : \; xy^{q} - x^{q}y = 1 \quad (q = 4),$$
the Deligne–Lusztig variety for the Coxeter element of $\mathrm{SL}_2(4)$, with $R\Gamma_c(X,\mathcal{O})e_B$ serving as the tilting complex between $B$ and $b$. This is the smallest complete illustration of the conjecture: derived-equivalent but Morita-inequivalent blocks, with the equivalence coming from geometry rather than from any algebra isomorphism.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*