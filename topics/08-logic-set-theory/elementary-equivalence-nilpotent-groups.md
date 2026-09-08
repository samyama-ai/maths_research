---
id: 08-logic-set-theory/elementary-equivalence-nilpotent-groups
title: "The Elementary Equivalence Problem for Finitely Generated Nilpotent Groups"
topic: 08-logic-set-theory
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# The Elementary Equivalence Problem for Finitely Generated Nilpotent Groups

> **Topic:** Mathematical Logic & Set Theory · **ID:** `08-logic-set-theory/elementary-equivalence-nilpotent-groups` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Two groups $G, H$ are *elementarily equivalent*, written $G \equiv H$, if they satisfy exactly the same first-order sentences in the language of groups $L = \{\cdot, {}^{-1}, 1\}$.

**The problem.** Classify finitely generated (f.g.) nilpotent groups up to $\equiv$:

1. **(Mal'cev's question, 1960s)** Does $G \equiv H$ imply $G \cong H$ for f.g. nilpotent $G,H$? — **Answered no** (Zilber 1971).
2. **(Structural classification)** Give an explicit algebraic invariant $I(G)$, computable from a presentation, with $G \equiv H \iff I(G) = I(H)$.
3. **(Effectiveness)** Decide $\equiv$ from finite presentations — **answered yes** in principle (Oger 1991 + Grunewald–Segal 1980), but with no elementary complexity bound. Open: is $\equiv$ decidable in primitive recursive, or even elementary, time?
4. **(Models)** Describe *all* models of $\mathrm{Th}(G)$, in particular the non-finitely-generated ones. Open outside specific families.

A complete solution requires: an invariant as in (2) proved to characterise $\equiv$; a complexity-bounded algorithm for (3); and a classification of $\mathrm{Th}(G)$-models for (4).

## 2. Mathematical Foundations

**Nilpotency.** The lower central series is $\gamma_1(G) = G$, $\gamma_{i+1}(G) = [\gamma_i(G), G]$. $G$ is nilpotent of class $c$ if $\gamma_{c+1}(G) = 1 \neq \gamma_c(G)$. Each $\gamma_i$ is definable by the first-order formula
$$\gamma_i(G) = \{g : \exists \text{ product of } i\text{-fold commutators}\},$$
and for f.g. nilpotent $G$ the subgroups $\gamma_i(G)$, $Z(G)$, the isolator $\mathrm{Is}_G(N) = \{g : g^n \in N \text{ for some } n \ge 1\}$, and the torsion subgroup $\tau(G)$ are all $L$-definable without parameters, because nilpotency of fixed class bounds the commutator length uniformly.

**Hirsch length.** For f.g. nilpotent $G$ there is a central series with cyclic factors; $h(G)$ = number of infinite factors. $h$ is a $\equiv$-invariant.

**Mal'cev correspondence.** A torsion-free f.g. nilpotent group $G$ of class $c$ embeds in a uniquely divisible group $G^{\mathbb{Q}}$ (the Mal'cev completion), which corresponds to a nilpotent Lie $\mathbb{Q}$-algebra $L_{\mathbb{Q}}(G)$ via Baker–Campbell–Hausdorff:
$$x \cdot y = x + y + \tfrac12 [x,y] + \tfrac1{12}\big([x,[x,y]] - [y,[x,y]]\big) + \cdots$$

**Class 2 and bilinear maps.** For $G$ nilpotent of class $2$ set $A = G/Z(G)$, $B = G'$. Commutation induces an alternating bilinear map
$$f_G : A \times A \to B, \qquad f_G(\bar x, \bar y) = [x,y],$$
and Myasnikov's theory of definable invariants of bilinear maps reduces $\equiv$ for such groups to equivalence of the pair $(f_G, \text{enrichment by definable ring of scalars})$.

**Oger's criterion (1991).** For f.g. finite-by-nilpotent $G, H$:
$$G \equiv H \iff G \times \mathbb{Z} \cong H \times \mathbb{Z}.$$
So $\equiv$-classes coincide with **genus** (Warfield) classes, which are finite: each f.g. nilpotent $G$ is $\equiv$ to only finitely many f.g. groups up to $\cong$.

**QFA.** $G$ is *quasi-finitely axiomatizable* if a single sentence $\varphi$ satisfies: $H \models \varphi$ and $H$ f.g. $\Rightarrow H \cong G$. Oger–Sabbagh: a f.g. nilpotent $G$ is QFA $\iff Z(G) \subseteq \mathrm{Is}_G(G') \iff G$ has no direct factor isomorphic to $\mathbb{Z}$.

**Undecidability of theories.** By Noskov's theorem, a f.g. solvable group has decidable elementary theory iff it is virtually abelian. Hence $\mathrm{Th}(G)$ is undecidable for every f.g. non-virtually-abelian nilpotent $G$ — the *classification* problem is nonetheless separately tractable.

## 3. History & State of the Art (SOTA)

- **1949–1960.** Mal'cev develops the correspondence between nilpotent groups and Lie rings and raises the question of whether $\equiv$ implies $\cong$ for f.g. nilpotent groups.
- **1971.** Zilber constructs two non-isomorphic, elementarily equivalent f.g. nilpotent groups of class $2$ — a negative answer.
- **1975–76.** Warfield, Hirshon: failure of cancellation, $G \times \mathbb{Z} \cong H \times \mathbb{Z} \not\Rightarrow G \cong H$; genus of a f.g. nilpotent group is finite.
- **1980.** Grunewald–Segal: the isomorphism problem for f.g. nilpotent (indeed polycyclic-by-finite) groups is decidable, via algorithms for arithmetic groups.
- **1991.** Oger: $G \equiv H \iff G \times \mathbb{Z} \cong H \times \mathbb{Z}$ for f.g. finite-by-nilpotent groups. Combined with Grunewald–Segal this makes $\equiv$ **decidable**.
- **1994.** Belegradek: complete model theory of unitriangular groups $UT_n(R)$, including a description of groups $\equiv UT_n(\mathbb{Z})$.
- **2003–2006.** Nies; Oger–Sabbagh: QFA characterisation and separation of nilpotent groups by single sentences.
- **2009–2021.** Myasnikov–Sohrabi: full description of groups (not necessarily f.g.) elementarily equivalent to free nilpotent groups $N_{r,c}$ of finite rank, and bi-interpretability of large classes of f.g. nilpotent groups with the ring $\mathbb{Z}$.

## 4. Partial Results / Verified Cases

| Class | Result |
|---|---|
| f.g. abelian | $\equiv \iff \cong$ (Szmielew invariants; the theory is decidable) |
| f.g. finite-by-nilpotent | $\equiv \iff G\times\mathbb{Z}\cong H\times\mathbb{Z}$ (Oger 1991); decidable |
| $G$ with $Z(G)\subseteq \mathrm{Is}_G(G')$ (no $\mathbb{Z}$ direct factor) | QFA: $\equiv$ determines $\cong$ within f.g. groups (Oger–Sabbagh 2006) |
| Heisenberg $H_3(\mathbb{Z})$, $UT_n(\mathbb{Z})$, $n\ge3$ | bi-interpretable with $(\mathbb{Z},+,\cdot)$; QFA; prime models of their theories |
| Free nilpotent $N_{r,c}$, $r,c$ finite | all models of $\mathrm{Th}(N_{r,c})$ described as $\mathbb{Z}^*$-completions over models of arithmetic (Myasnikov–Sohrabi 2011) |
| Class 2, $G' $ cyclic | $\equiv$ reduces to equivalence of alternating bilinear forms over $\mathbb{Z}$ modulo definable scalars |
| $h(G) \le 4$ | genus is trivial in all recorded cases; $\equiv = \cong$ (smallest known cancellation failures require larger Hirsch length) |
| Any fixed $G$ | $\{H \text{ f.g.} : H \equiv G\}/\cong$ is **finite** (genus finiteness) |

Complementary negative facts: $\mathrm{Th}(G)$ is undecidable for all f.g. non-virtually-abelian nilpotent $G$ (Noskov), and $G \times \mathbb{Z}$ is never QFA.

## 5. Principal Obstacles

- **The invariant is arithmetic, not combinatorial.** Genus classes are indexed by double cosets
$$\mathrm{Aut}(\hat{G}) \backslash \ \hat{?} \ / \ \mathrm{Aut}(G^{\mathbb{Q}}),$$
i.e. by class-number-like data for arithmetic groups. Grunewald–Segal's decision procedure enumerates orbits of arithmetic groups acting on lattices; the search is non-constructively bounded, giving no elementary complexity estimate.
- **Mal'cev correspondence is not first-order over $\mathbb{Z}$.** BCH has denominators divisible by primes $\le c$, so the group$\leftrightarrow$Lie-ring translation is interpretable only after passing to $G^{\mathbb{Q}}$; equivalence of $\mathbb{Z}$-forms of a fixed $\mathbb{Q}$-Lie algebra is exactly the hard arithmetic residue.
- **Bilinear-map methods stall above class 2.** For class $2$ the whole structure is one alternating map $f_G: A\times A \to B$ and Myasnikov's definable-scalar machinery applies. For class $\ge 3$ the group is a tower of extensions whose cohomology classes in $H^2(\cdot,\cdot)$ have no known definable normal form.
- **Undecidable ambient theories.** Since $\mathrm{Th}(G)$ interprets arithmetic, no back-and-forth or quantifier-elimination argument can be run inside the theory; all positive results route through the *external* isomorphism problem instead.
- **Torsion and abelian direct factors.** $\mathbb{Z}$ direct factors destroy bi-interpretability with $\mathbb{Z}$ and QFA, so the sharpest tool (definable coordinates) does not apply to arbitrary $G$ without stripping factors first — and the stripping is not first-order uniform.

## 6. The Gap

Proven: $\equiv$ on f.g. nilpotent groups equals "$\cong$ after $\times\mathbb{Z}$" and is decidable. Missing, in order of increasing strength:

1. **Complexity.** Every known decision procedure inherits Grunewald–Segal's unbounded arithmetic-group search. No primitive-recursive bound is known even for class $2$, Hirsch length $\le 10$.
2. **Explicit invariant.** No presentation-level formula computes the genus; one wants an invariant like a class group or an idele-class quotient, computable in polynomial time from a consistent polycyclic presentation.
3. **Models.** $\mathrm{Th}(G)$ has been fully described only for $N_{r,c}$, $UT_n(\mathbb{Z})$, and near relatives. For a general f.g. nilpotent $G$ — especially with torsion or abelian direct factors — the non-f.g. models are uncharted.
4. **Beyond f.g.** For nilpotent groups of finite Mal'cev rank, or free nilpotent groups of infinite rank, Oger's criterion fails outright; no substitute is known.

## 7. Current Research (as of June 2026)

- **Stevens Institute (Myasnikov, Sohrabi) and collaborators**: first-order rigidity and bi-interpretability with $\mathbb{Z}$ for nilpotent and metabelian groups; extension of the "elementary coordinatization" programme from free nilpotent groups to arbitrary f.g. nilpotent groups with prescribed abelian direct factors. *(frontier — verify)*
- **Paris (Sabbagh school) and Oger's programme**: refinements of QFA to *finitely axiomatizable within f.g. groups of bounded Hirsch length*, and separation of genus classes by explicit sentences of low quantifier rank.
- **Arithmetic-group algorithmics (Oxford/Düsseldorf/Warwick)**: practical genus computation for f.g. nilpotent groups via `GAP`/`Polycyclic`, with the aim of tabulating all $\equiv$-classes of Hirsch length $\le 8$. *(frontier — verify)*
- **Model theory of pro-$p$ and adelic completions**: transferring "$\equiv$ = genus" to profinite settings, where genus is the Grothendieck/Pickel invariant; connections to first-order rigidity results for higher-rank arithmetic groups (Avni–Lubotzky–Meiri).
- **Definable sets and NIP/NTP considerations**: since these theories interpret arithmetic they are maximally complex, so effort focuses on *external* invariants rather than tameness.

## 8. Future Work

- Extract an explicit complexity bound from the Grunewald–Segal orbit algorithm restricted to nilpotent groups of class $2$ — likely the first tractable case.
- Prove or refute: for class-2 f.g. nilpotent $G$, genus is computable in time polynomial in the Hirsch length and the bit size of the structure constants.
- Extend Myasnikov–Sohrabi coordinatization to all f.g. nilpotent $G$ by proving that $G \cong G_0 \times \mathbb{Z}^k$ with $G_0$ bi-interpretable with $\mathbb{Z}$, uniformly and definably.
- Determine whether $\equiv$ for nilpotent groups of finite Mal'cev rank (a class where Oger's cancellation criterion is unavailable) is decidable.
- Classify $\mathrm{Th}(G)$-models for $G$ with nontrivial torsion; the finite-by-nilpotent case is the natural next target after $UT_n$.

## 9. Key References

- **[Foundational]** A. I. Mal'cev. *On a correspondence between rings and groups.* American Mathematical Society Translations, Series 2, vol. 45, 1965 (Russian original 1960).
- **[Foundational]** B. Zilber. *An example of two elementarily equivalent but non-isomorphic finitely generated nilpotent groups of class 2.* Algebra and Logic 10 (1971), 173–188.
- **[Foundational]** F. Grunewald, D. Segal. *Some general algorithms. I: Arithmetic groups.* Annals of Mathematics 112 (1980), 531–583.
- **[Foundational]** R. B. Warfield, Jr. *Genus and cancellation for groups with finite commutator subgroup.* Journal of Pure and Applied Algebra 6 (1975), 125–132.
- **[Key result]** F. Oger. *Cancellation and elementary equivalence of finitely generated finite-by-nilpotent groups.* Journal of the London Mathematical Society (2) 44 (1991), 173–183.
- **[Key result]** F. Oger, G. Sabbagh. *Quasi-finitely axiomatizable nilpotent groups.* Journal of Mathematical Logic 6 (2006), 45–58.
- **[Key result]** O. V. Belegradek. *The model theory of unitriangular groups.* Annals of Pure and Applied Logic 68 (1994), 225–261.
- **[SOTA / Recent]** A. Myasnikov, M. Sohrabi. *Groups elementarily equivalent to a free nilpotent group of finite rank.* Annals of Pure and Applied Logic 162 (2011), 916–933.
- **[SOTA / Recent]** A. Nies. *Separating classes of groups by first-order sentences.* International Journal of Algebra and Computation 13 (2003), 287–302.
- **[Context]** G. A. Noskov. *On the elementary theory of a finitely generated almost solvable group.* Mathematics of the USSR–Izvestiya 22 (1984), 465–482.
- **[Survey / Book]** D. Segal. *Polycyclic Groups.* Cambridge University Press, 1983.
- **[Survey / Book]** W. Hodges. *Model Theory.* Cambridge University Press, 1993.

## 10. Worked Example / Concrete Special Case

**The Heisenberg group $H = H_3(\mathbb{Z}) = \langle a, b \mid [a,b]=c,\ [a,c]=[b,c]=1 \rangle$.**

Normal form: every $g \in H$ is uniquely $a^i b^j c^k$, with
$$(a^{i}b^{j}c^{k})(a^{p}b^{q}c^{r}) = a^{i+p} b^{j+q} c^{\,k+r-jp}, \qquad [a^i b^j c^k,\ a^p b^q c^r] = c^{\,iq-jp}.$$
Here $Z(H) = H' = \langle c\rangle \cong \mathbb{Z}$, $H/Z(H)\cong\mathbb{Z}^2$, $h(H)=3$.

**Step 1 — interpret the ring $\mathbb{Z}$.** Take as domain the definable set $Z(H)=\langle c \rangle$, with addition given by the group operation ($c^m c^n = c^{m+n}$). Define multiplication by the formula
$$\mu(u,v,w) \ :\equiv\ \exists x\,\exists y\ \big([x,b]=u \wedge [x,a]=1 \wedge [a,y]=v \wedge [y,b]=1 \wedge [x,y]=w\big).$$
Check with normal forms: $[x,a]=1$ with $x=a^ib^jc^k$ forces $c^{-j}=1$, so $j=0$; then $[x,b]=c^{i}=u=c^m$ gives $i=m$, i.e. $x=a^m c^k$. Dually $[y,b]=1$ gives $y = b^n c^r$ with $[a,y]=c^{n}=v$. Finally
$$[x,y]=[a^m c^k,\ b^n c^r] = c^{\,m\cdot n - 0\cdot 0} = c^{mn}.$$
So $\mu(c^m,c^n,w) \iff w = c^{mn}$: the ring $(\mathbb{Z},+,\cdot)$ is interpreted in $H$ without parameters. Consequences: $\mathrm{Th}(H)$ is undecidable, and $H$ is bi-interpretable with $\mathbb{Z}$ (the coordinates $i,j,k$ of $g$ are recovered by $[g,b]=c^{i}$, $[g,a]=c^{-j}$, and $g a^{-i} b^{-j} = c^{k}$). Hence $H$ is QFA: one sentence saying "class 2, $Z=H'\cong\mathbb{Z}$ via the above coordinates, generated by two elements $a,b$ with $[a,b]$ generating $Z$" pins $H$ among f.g. groups.

**Step 2 — the criterion at work.** $Z(H)=\langle c\rangle = H' = \mathrm{Is}_H(H')$, so $Z(H)\subseteq \mathrm{Is}_H(H')$ and Oger–Sabbagh confirms QFA. Therefore for f.g. nilpotent $K$: $K \equiv H \Rightarrow K \cong H$. Equivalently, by Oger's theorem, $K \times \mathbb{Z} \cong H \times \mathbb{Z} \Rightarrow K \cong H$ — cancellation holds here.

**Step 3 — where it breaks.** Put $G = H \times \mathbb{Z}$. Now $Z(G) = \langle c \rangle \times \mathbb{Z} \not\subseteq \mathrm{Is}_G(G') = \langle c\rangle$, so $G$ is **not** QFA. Zilber's construction lives exactly in this regime: one builds class-2 groups $G_1 \not\cong G_2$ whose central extensions differ by a unit that becomes trivial after tensoring up, so that $G_1\times\mathbb{Z} \cong G_2\times\mathbb{Z}$ and hence $G_1 \equiv G_2$. Deciding which pairs behave this way is the genus computation of Section 6 — solvable in principle, with no known efficient algorithm.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*