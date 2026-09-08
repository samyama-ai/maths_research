---
id: 02-algebra-group-theory/kac-weisfeiler-conjecture
title: "Kac-Weisfeiler Conjecture"
topic: 02-algebra-group-theory
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Kac-Weisfeiler Conjecture

> **Topic:** Algebra & Group Theory · **ID:** `02-algebra-group-theory/kac-weisfeiler-conjecture` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

Let $k$ be an algebraically closed field of characteristic $p > 0$, let $G$ be a connected reductive algebraic group over $k$, and let $\mathfrak{g} = \operatorname{Lie}(G)$, a restricted Lie algebra with $p$-th power map $x \mapsto x^{[p]}$. Every irreducible $\mathfrak{g}$-module is finite-dimensional and carries a **$p$-character** $\chi \in \mathfrak{g}^*$ determined by
$$x^p - x^{[p]} = \chi(x)^p \cdot \mathrm{id}_M \qquad \text{for all } x \in \mathfrak{g}.$$
Set $d(\chi) = \tfrac{1}{2}\big(\dim \mathfrak{g} - \dim \mathfrak{g}_\chi\big)$, half the dimension of the coadjoint $G$-orbit of $\chi$, where $\mathfrak{g}_\chi = \{x : \chi([x,\mathfrak{g}]) = 0\}$.

**KW1 (first Kac–Weisfeiler conjecture, 1971).** $p^{d(\chi)}$ divides $\dim M$ for every irreducible $\mathfrak{g}$-module $M$ with $p$-character $\chi$.

**KW2 (second Kac–Weisfeiler conjecture).** The bound is attained: the reduced enveloping algebra $U_\chi(\mathfrak{g})$ admits an irreducible module of dimension exactly $p^{d(\chi)}$.

A complete proof must handle every $\chi \in \mathfrak{g}^*$ and every $p$ (or state the exact characteristic hypotheses); a disproof exhibits one reductive $\mathfrak{g}$, one $\chi$, and one irreducible module violating the divisibility or the attainment.

## 2. Mathematical Foundations

**Reduced enveloping algebras.** For $\chi \in \mathfrak{g}^*$ put
$$U_\chi(\mathfrak{g}) = U(\mathfrak{g}) \big/ \big\langle x^p - x^{[p]} - \chi(x)^p : x \in \mathfrak{g} \big\rangle .$$
By the PBW theorem $\dim_k U_\chi(\mathfrak{g}) = p^{\dim \mathfrak{g}}$, and $\mathfrak{g}$-modules with $p$-character $\chi$ are exactly $U_\chi(\mathfrak{g})$-modules. Hence $\dim M \le p^{(\dim\mathfrak{g})/2}$ for irreducible $M$, and $d(\chi) \le \tfrac12 \dim\mathfrak g$ always.

**Coadjoint geometry.** $\mathfrak{g}_\chi$ is the Lie algebra of the stabiliser $G_\chi$, and the orbit $G\cdot\chi \subset \mathfrak{g}^*$ carries the Kirillov–Kostant symplectic form, so $\dim G\cdot\chi = 2d(\chi)$ is even. KW1 is the modular analogue of the orbit method: representations "quantise" the orbit, and $p^{d(\chi)}$ is the size of a Lagrangian $p$-lattice in it.

**Jordan decomposition and KW reduction.** Under a nondegenerate $G$-invariant form $\mathfrak{g} \cong \mathfrak{g}^*$, write $\chi = \chi_s + \chi_n$. Weisfeiler–Kac proved a Morita equivalence
$$U_\chi(\mathfrak{g})\text{-mod} \;\simeq\; U_{\chi_n}(\mathfrak{g}_{\chi_s})\text{-mod}, \qquad \mathfrak{g}_{\chi_s} = \text{a Levi subalgebra},$$
with dimensions scaled by $p^{(\dim\mathfrak g - \dim\mathfrak g_{\chi_s})/2}$. This reduces both conjectures to **nilpotent** $\chi$.

**Support varieties.** Friedlander–Parshall attach to $M$ the rank variety inside the restricted nullcone $\mathcal{N}_p(\mathfrak{g}) = \{x : x^{[p]} = 0\}$; $\dim M$ is divisible by $p^{\,\mathrm{codim}}$-type factors controlled by that variety. Premet's proof of KW1 turns a statement about $\dim M$ into a statement about the dimension of $\mathcal N_p(\mathfrak g)$ and its irreducible components.

**Finite W-algebras.** For nilpotent $e \in \mathfrak{g}_{\mathbb C}$ with $\mathfrak{sl}_2$-triple $(e,h,f)$ and Slodowy slice $e + \mathfrak{g}^f$, the W-algebra $U(\mathfrak{g}_{\mathbb C},e)$ is the quantisation of the slice; its modular reduction $U(\mathfrak{g}_k,e)$ satisfies
$$U_\chi(\mathfrak{g}) \;\cong\; \operatorname{Mat}_{p^{d(\chi)}}\big(U(\mathfrak{g}_k,e)\big)$$
(Premet, 2002 — the "Premet Morita equivalence", for $p \gg 0$). KW1 is then immediate, and KW2 becomes: **does $U(\mathfrak{g}_k,e)$ have a $1$-dimensional representation?**

## 3. History & State of the Art (SOTA)

- **1971.** Boris Weisfeiler and Victor Kac, *Irreducible representations of Lie $p$-algebras* (Funkts. Anal. Prilozh. 5), prove the reduction to nilpotent $\chi$, settle the supersolvable/triangulable case, and state the divisibility conjecture.
- **1986–88.** Friedlander–Parshall build support-variety technology for restricted Lie algebras and verify KW1 in low-rank and regular cases.
- **1995.** Alexander Premet proves **KW1** for $\mathfrak{g} = \operatorname{Lie}(G)$, $G$ reductive, under: (A) the derived group of $G$ is simply connected, (B) $\mathfrak{g}$ has a nondegenerate $G$-invariant bilinear form, (C) $p$ is good for the root system. The proof combines support varieties with the Bala–Carter classification and Premet's theorem that $\mathcal{N}_p(\mathfrak{g})$ is irreducible of dimension $\dim\mathfrak g - \operatorname{rk}\mathfrak g$.
- **2002–2007.** Premet's Slodowy-slice enveloping algebras give a second, structural proof of KW1 for $p \gg 0$ and convert KW2 into the $1$-dimensional-representation problem.
- **2008.** Bezrukavnikov–Mirković–Rumynin's localisation in prime characteristic gives an independent derivation of the divisibility for regular $\chi$ and proves Lusztig's conjectures on the geometry of blocks.
- **2010–11.** Losev, Premet, and Goodwin–Röhrle–Ubly establish the existence of $1$-dimensional W-algebra representations in all types, completing **KW2 for $p \gg 0$**.

## 4. Partial Results / Verified Cases

| Class | Result |
|---|---|
| Supersolvable / nilpotent restricted $\mathfrak g$ | Every irreducible has dimension *exactly* $p^{d(\chi)}$ (Weisfeiler–Kac 1971) |
| $\mathfrak{gl}_n,\ \mathfrak{sl}_n$, $p \nmid n$ | KW1 and KW2 hold for all $\chi$, all $p$ (classical; W-algebras of type $A$ are quotients of Yangians and always have $1$-dimensional modules) |
| Reductive $\mathfrak g$, $p$ good, hypotheses (A)–(C) | **KW1 proved** (Premet 1995); covers $p>3$ in types $A,B,C,D$, $p>5$ in $E_8$ |
| Regular $\chi$ (i.e. $\dim\mathfrak g_\chi = \operatorname{rk}\mathfrak g$) | KW1, KW2 hold; $U_\chi$ is Azumaya of rank $p^{2d(\chi)}$ over its centre (Friedlander–Parshall; BMR) |
| Subregular and rigid nilpotent orbits, exceptional types | $1$-dimensional W-algebra modules verified by computer for $G_2, F_4, E_6, E_7$ and all but a handful of $E_8$ orbits (Goodwin–Röhrle–Ubly 2010), remainder settled by Premet |
| Simple $\mathfrak g$, $p \gg 0$ (no effective bound) | **KW2 proved** (Premet 2010 + Losev 2011 + GRU 2010) |
| Basic classical Lie superalgebras | KW1 analogue proved (Wang–Zhao 2009); queer series treated separately |
| Cartan-type $\mathfrak g$ (e.g. Witt algebra $W_1$) | **KW1 is false** — see §5 |

## 5. Principal Obstacles

- **No effective characteristic bound.** The Premet Morita equivalence and the reduction of KW2 to $1$-dimensional W-algebra modules both rest on base change from $\mathbb{C}$ to $\overline{\mathbb{F}_p}$ for $p$ larger than an unspecified constant depending on $\mathfrak g$ and $e$. The constant comes from clearing denominators in $\mathbb{Z}$-forms of Slodowy slices and from Losev's use of Fedosov/deformation quantisation over $\mathbb C$ — analytic input that does not descend. Nothing in the argument yields a number, so KW2 is open for *every* explicit small $p$ outside type $A$.
- **Bad primes break the geometry.** Premet's KW1 proof needs $\mathcal N_p(\mathfrak g) = \mathcal N(\mathfrak g)$ and the Bala–Carter bijection, both of which fail for $p = 2$ (types $B,C,D,F,G$), $p=3$ ($G_2, F_4, E$), $p=5$ ($E_8$). In bad characteristic $\mathcal N_p$ can be reducible and the invariant form degenerate, so orbit dimensions no longer control $p$-divisibility.
- **The conjecture is genuinely reductive-specific.** For the Witt algebra $W_1 = \operatorname{Der}(k[x]/x^p)$, $\dim W_1 = p$, a generic $\chi$ has $\dim (W_1)_\chi = 1$, so $d(\chi) = (p-1)/2$; but every irreducible $U_\chi(W_1)$-module has dimension $\le p$ (Chang 1941). For $p \ge 5$, $p^{(p-1)/2} \nmid p$. So no argument for KW1 can be purely "restricted Lie algebra + orbit dimension" — it must use the reductive group action, which is exactly the ingredient that is fragile at small $p$.
- **Support varieties are too coarse.** Rank varieties give divisibility only up to the codimension of the support, which under-counts for non-regular $\chi$; Premet had to supplement them with the sheets/induction machinery of nilpotent orbits.

## 6. The Gap

Everything proved is asymptotic or type-restricted. The precise residual statement is:

> For a simple, simply connected $G$ with $p$ good (or even $p > h$, the Coxeter number), and *every* nilpotent $\chi \in \mathfrak{g}^*$, the modular finite W-algebra $U(\mathfrak{g}_k, e)$ possesses a $1$-dimensional representation — equivalently $U_\chi(\mathfrak{g})$ has an irreducible module of dimension $p^{d(\chi)}$.

The barrier is the transition from *"for $p \gg 0$"* to *"for all good $p$"*. Concretely: one needs either (i) an explicit $\mathbb{Z}[1/N]$-form of the W-algebra with a controlled $N$, so that Losev's complex-analytic construction of $1$-dimensional modules reduces mod $p$; or (ii) a purely characteristic-$p$ construction of a Whittaker-type module of dimension $p^{d(\chi)}$ that never passes through $\mathbb{C}$. Neither exists in general. KW1 has no analogous gap for good $p$; its own gap is bad characteristic.

## 7. Current Research (as of June 2026)

- **Effective bounds for W-algebras.** Groups at Manchester (Premet, Goodwin's Birmingham collaborators), MIT/Yale (Losev's circle) pursue integral forms of $U(\mathfrak g,e)$ with computable denominators. *(frontier — verify)* Type-by-type explicit bounds for classical $\mathfrak g$ have been circulated but are not uniformly published.
- **Modular Whittaker theory.** Direct construction of $p^{d(\chi)}$-dimensional modules via generalised Gelfand–Graev representations of the finite group $G(\mathbb{F}_q)$ — an approach that bypasses characteristic zero.
- **Bad characteristic.** Systematic study of $\mathcal N_p(\mathfrak g)$ and centralisers when $p$ is bad (work in the Ruhr-Universität Bochum and Birmingham schools), aiming at a corrected KW1 with a modified exponent.
- **Super and quantum analogues.** KW-type divisibility for Lie superalgebras (Shu, Yao, Wang and collaborators in Shanghai/Xiamen) and for restricted quantum groups at roots of unity.
- **Cartan type.** Determining the correct replacement exponent for $W_n$, $S_n$, $H_n$, $K_n$, where the naive KW1 fails.

## 8. Future Work

- Produce a characteristic-free proof of the Premet Morita equivalence valid for all good $p$; this alone would settle KW2 in the stated range.
- Extract an explicit function $N(\mathfrak g)$ such that all results hold for $p > N(\mathfrak g)$, then close the residual finite range by computer algebra (the strategy already successful for exceptional-type W-algebras).
- Extend KW1 to bad primes, possibly with $d(\chi)$ replaced by a smaller invariant read off from the irreducible components of $\mathcal N_p(\mathfrak g)$.
- Classify all restricted Lie algebras satisfying the "KW property" ($\max \dim = p^{d(\chi)}$ for all $\chi$); reductive is sufficient but the exact class is unknown.

## 9. Key References

- **[Foundational]** B. Ju. Weisfeiler, V. G. Kac. *Irreducible representations of Lie $p$-algebras.* Funktsional. Anal. i Prilozhen. **5** (1971), no. 2, 28–36.
- **[Foundational]** H.-J. Chang. *Über Wittsche Lie-Ringe.* Abh. Math. Sem. Univ. Hamburg **14** (1941), 151–184. [DOI](https://doi.org/10.1007/bf02940743)
- **[Foundational]** E. M. Friedlander, B. J. Parshall. *Modular representation theory of Lie algebras.* Amer. J. Math. **110** (1988), 1055–1093.
- **[Key theorem]** A. Premet. *Irreducible representations of Lie algebras of reductive groups and the Kac–Weisfeiler conjecture.* Invent. Math. **121** (1995), 79–117. [DOI](https://doi.org/10.1007/bf01884291)
- **[Key theorem]** A. Premet. *Special transverse slices and their enveloping algebras.* Adv. Math. **170** (2002), 1–55. [DOI](https://doi.org/10.1006/aima.2001.2063)
- **[SOTA]** A. Premet. *Commutative quotients of finite $W$-algebras.* Adv. Math. **225** (2010), 269–306. [DOI](https://doi.org/10.1016/j.aim.2010.02.020)
- **[SOTA]** I. Losev. *1-dimensional representations and parabolic induction for $W$-algebras.* Adv. Math. **226** (2011), 4841–4883. [DOI](https://doi.org/10.1016/j.aim.2010.12.021)
- **[SOTA]** S. M. Goodwin, G. Röhrle, G. Ubly. *On 1-dimensional representations of finite $W$-algebras associated to simple Lie algebras of exceptional type.* LMS J. Comput. Math. **13** (2010), 357–369. [DOI](https://doi.org/10.1112/s1461157009000205)
- **[SOTA]** R. Bezrukavnikov, I. Mirković, D. Rumynin. *Localization of modules for a semisimple Lie algebra in prime characteristic.* Ann. of Math. **167** (2008), 945–991.
- **[Survey]** J. C. Jantzen. *Representations of Lie algebras in prime characteristic.* In *Representation Theories and Algebraic Geometry*, NATO ASI Ser. C **514**, Kluwer, 1998, 185–235. [DOI](https://doi.org/10.1007/978-94-015-9131-7_5)
- **[Survey]** J. E. Humphreys. *Modular representations of simple Lie algebras.* Bull. Amer. Math. Soc. **35** (1998), 105–122.
- **[Extension]** W. Wang, L. Zhao. *Representations of Lie superalgebras in prime characteristic I.* Proc. London Math. Soc. (3) **99** (2009), 145–167. [DOI](https://doi.org/10.1112/plms/pdn057)

## 10. Worked Example / Concrete Special Case

Take $\mathfrak{g} = \mathfrak{sl}_2$ over $k = \overline{\mathbb{F}_p}$, $p \ge 3$, basis $e, h, f$ with $[h,e]=2e$, $[h,f]=-2f$, $[e,f]=h$, and $p$-map $e^{[p]}=f^{[p]}=0$, $h^{[p]}=h$.

**Choice of $\chi$.** Let $\chi(e) = 1$, $\chi(h)=\chi(f)=0$ — a nonzero nilpotent character. Then $\mathfrak{g}_\chi = \operatorname{span}(e)$, so
$$d(\chi) = \tfrac12(3 - 1) = 1, \qquad \text{KW predicts } p \mid \dim M \text{ and } \exists\, M \text{ with } \dim M = p .$$
In $U_\chi(\mathfrak{sl}_2)$ the relations are $e^p = 1$, $f^p = 0$, $h^p = h$, and $\dim U_\chi = p^3$.

**Construction of a $p$-dimensional module.** Fix $a \in \mathbb{F}_p$, let $M_a$ have basis $\{m_i\}_{i \in \mathbb{Z}/p}$ and set
$$e\,m_i = m_{i+1}, \qquad h\,m_i = (2i+a)\,m_i, \qquad f\,m_i = b_i\, m_{i-1}, \quad b_i = -\,i\,(i-1+a).$$
Checks:
- $[h,e]$: $(he-eh)m_i = \big((2i+2+a)-(2i+a)\big)m_{i+1} = 2\,e\,m_i$. ✓
- $[h,f]$: $(hf-fh)m_i = b_i\big((2i-2+a)-(2i+a)\big)m_{i-1} = -2\,f\,m_i$. ✓
- $[e,f]$: $(ef-fe)m_i = (b_i - b_{i+1})m_i$, and $b_i - b_{i+1} = -i(i-1+a) + (i+1)(i+a) = 2i + a$, which is $h\,m_i$. ✓
- $p$-relations: $e^p m_i = m_{i+p} = m_i$, matching $\chi(e)^p = 1$; $h$ acts by $\mathbb F_p$-scalars so $h^p = h$; and $b_0 = 0$ forces $f^p m_i = \big(\prod_{j} b_j\big) m_i = 0$. ✓

**Irreducibility.** For $p$ odd the scalars $2i + a$, $i \in \mathbb{Z}/p$, are pairwise distinct, so any submodule is spanned by a subset of the $m_i$; since $e$ permutes them in a single $p$-cycle, that subset is empty or everything. Hence $M_a$ is irreducible of dimension exactly $p = p^{d(\chi)}$ — **KW2 verified**, and every irreducible here has dimension divisible by $p$, verifying **KW1**.

**Contrast.** For $\chi = 0$, $d(0) = 0$ and the divisibility is vacuous: the trivial module ($\dim 1$) and the Steinberg module ($\dim p$) coexist. For $\chi$ regular semisimple ($\chi \leftrightarrow h$), again $\dim\mathfrak g_\chi = 1$ and $d(\chi)=1$; KW reduction identifies $U_\chi(\mathfrak{sl}_2)$-mod with modules over the torus $U_0(\mathfrak{h})$, $\dim\mathfrak h = 1$, and each of the $p$ irreducibles has dimension $p^1$. The general conjecture asserts this uniform $p^{\frac12\dim G\cdot\chi}$ pattern for every reductive $\mathfrak{g}$ — and, as §5 shows, the Witt algebra proves that the reductive hypothesis is not decoration.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*