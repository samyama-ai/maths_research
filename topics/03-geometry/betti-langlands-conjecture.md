---
id: 03-geometry/betti-langlands-conjecture
title: "Betti Langlands Conjecture"
topic: 03-geometry
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Betti Langlands Conjecture

> **Topic:** Algebraic & Differential Geometry · **ID:** `03-geometry/betti-langlands-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Let $X$ be a smooth projective connected curve over $\mathbb{C}$ (equivalently, a compact Riemann surface of genus $g$), let $G$ be a connected reductive group over $\mathbb{C}$ with Langlands dual $G^\vee$, and let $k$ be a field of characteristic $0$. The Betti Langlands conjecture of Ben-Zvi and Nadler (2016) asserts an equivalence of $k$-linear stable $\infty$-categories

$$\mathrm{Shv}_{\mathcal{N}}\big(\mathrm{Bun}_G(X); k\big) \;\simeq\; \mathrm{IndCoh}_{\mathcal{N}}\big(\mathrm{Loc}_{G^\vee}(X)\big),$$

where the left side is ind-constructible sheaves on the moduli stack of $G$-bundles with singular support in the global nilpotent cone, and the right side is ind-coherent sheaves with nilpotent singular support on the *Betti* (topological) derived stack of $G^\vee$-local systems, i.e. the derived character stack $\mathrm{Loc}_{G^\vee}(X) = \mathrm{Map}(X_{\mathrm{top}}, BG^\vee)$.

The equivalence is required to be compatible with:

1. the Hecke action of $\mathrm{Rep}(G^\vee)$ at every point $x \in X$, matched with tensoring by tautological bundles;
2. the spectral action of $\mathrm{Perf}(\mathrm{Loc}_{G^\vee}(X))$;
3. Whittaker normalization: the Whittaker sheaf corresponds to the structure sheaf $\mathcal{O}_{\mathrm{Loc}_{G^\vee}(X)}$.

A complete proof must produce such an equivalence for all $g$ and all reductive $G$; a disproof would exhibit a curve and a group for which no functor satisfying (1)–(3) is an equivalence (for instance, by exhibiting mismatched invariants such as Hochschild homology or $t$-structures). The distinguishing feature versus the de Rham conjecture is that the right-hand side depends only on the topological surface, so the conjecture predicts that $\mathrm{Shv}_{\mathcal{N}}(\mathrm{Bun}_G(X))$ is independent of the complex structure on $X$ and carries a mapping class group action.

## 2. Mathematical Foundations

**Automorphic side.** $\mathrm{Bun}_G(X)$ is a smooth Artin stack, locally of finite type, of dimension $(g-1)\dim G$. Its cotangent stack is

$$T^*\mathrm{Bun}_G = \{(E,\varphi) : E \in \mathrm{Bun}_G, \ \varphi \in H^0(X, \mathrm{ad}(E)\otimes \Omega^1_X)\},$$

Higgs bundles. The **global nilpotent cone** $\mathcal{N} \subset T^*\mathrm{Bun}_G$ is the zero fibre of the Hitchin map $h: T^*\mathrm{Bun}_G \to \bigoplus_i H^0(X,\Omega_X^{\otimes d_i})$; Laumon proved $\mathcal{N}$ is Lagrangian. For $\mathcal{F} \in \mathrm{Shv}(\mathrm{Bun}_G;k)$ one takes the Kashiwara–Schapira micro-support $SS(\mathcal{F})$ (defined stratum-wise on quasi-compact opens) and sets

$$\mathrm{Shv}_{\mathcal{N}}(\mathrm{Bun}_G) = \{\mathcal{F} : SS(\mathcal{F}) \subseteq \mathcal{N}\}^{\mathrm{ind}}.$$

**Spectral side.** The Betti local system stack is the derived mapping stack
$$\mathrm{Loc}_{G^\vee}(X) = \mathrm{Map}(X_{\mathrm{top}}, BG^\vee) \;=\; \Big[\{(a_i,b_i)\in (G^\vee)^{2g} : \textstyle\prod_{i=1}^g [a_i,b_i] = e\}^{\mathrm{der}} \big/ G^\vee\Big],$$
a quasi-smooth derived stack: its cotangent complex at $\rho$ has $\mathbb{T}_\rho = H^\bullet(X, \mathrm{ad}\rho)[1]$ concentrated in degrees $[-1,1]$. Quasi-smoothness gives the classical singularity support $\mathrm{Sing}(\mathrm{Loc}_{G^\vee}) = \{(\rho,\eta) : \eta \in H^0(X,\mathrm{ad}\rho)^*\}$, and $\mathcal{N}$ denotes the locus where $\eta$ is a nilpotent element of $\mathfrak{g}^\vee$. The category $\mathrm{IndCoh}_{\mathcal{N}}$ is Arinkin–Gaitsgory's category of ind-coherent sheaves with singular support in $\mathcal{N}$, interpolating
$$\mathrm{QCoh}(\mathrm{Loc}_{G^\vee}) \subsetneq \mathrm{IndCoh}_{\mathcal{N}}(\mathrm{Loc}_{G^\vee}) \subsetneq \mathrm{IndCoh}(\mathrm{Loc}_{G^\vee}).$$
Without the nilpotency condition the equivalence is false already for $G=\mathrm{SL}_2$, $g=1$ (an observation of Arinkin–Gaitsgory in the de Rham setting).

**Hecke structure.** For $x\in X$ the Hecke stack $\mathcal{H}ecke_x$ carries the geometric Satake equivalence $\mathrm{Perv}_{L^+G}(\mathrm{Gr}_G) \simeq \mathrm{Rep}(G^\vee)$ (Mirković–Vilonen), providing the $\mathrm{Rep}(G^\vee)$-action which the conjectured equivalence must intertwine with $V \mapsto \mathcal{V}_x \otimes (-)$, $\mathcal{V}_x$ the tautological bundle at $x$.

## 3. History & State of the Art (SOTA)

- **1987–2007.** Laumon and Beilinson–Drinfeld formulate the de Rham geometric Langlands conjecture via Hecke eigensheaves and construct them for $\mathrm{GL}_n$ and for opers. Kapustin–Witten (2007) reinterpret it as S-duality of the $4$d $\mathcal{N}=4$ gauge theory compactified on $X$; in that framework the *topological* (Betti) character variety, not the de Rham one, is the natural B-model target for the $A$-twist.
- **2015.** Arinkin–Gaitsgory identify nilpotent singular support as the correct spectral condition, making a *categorical* (not merely eigensheaf) statement plausible.
- **2016–2018.** Ben-Zvi and Nadler state the Betti conjecture (*Betti Geometric Langlands*, Proc. Sympos. Pure Math. 97.2, AMS 2018), formulating it as a topological field theory statement: both sides should extend to $2$-dimensional TQFT-type assignments on surfaces, with a $3$d "Betti Langlands" interpretation and a mapping class group symmetry absent on the de Rham side.
- **2019.** Nadler–Yun construct the spectral action of $\mathrm{Perf}(\mathrm{Loc}_{G^\vee}(X))$ on the automorphic category for arbitrary $X$ and $G$ — the single largest structural step towards the conjecture.
- **2024.** Gaitsgory, Raskin and collaborators complete the proof of the **de Rham** geometric Langlands conjecture in a five-paper series. This does *not* imply the Betti statement: no Riemann–Hilbert equivalence is known between the two automorphic categories (see §5).

## 4. Partial Results / Verified Cases

- **$G = T$ a torus, any genus.** Proved. Both sides linearize: $\mathcal{N}$ is the zero section, so the automorphic category is local systems on $\mathrm{Bun}_T(X)$, and the Mellin transform (Gabber–Loeser, *Faisceaux pervers $\ell$-adiques sur un tore*, Duke Math. J. 83, 1996) identifies it with $\mathrm{QCoh}((T^\vee)^{2g} \times BT^\vee)$.
- **Genus $0$, no punctures.** Birkhoff–Grothendieck gives $\mathrm{Bun}_G(\mathbb{P}^1) = \coprod_{\lambda} \mathrm{pt}/\mathrm{Aut}(E_\lambda)$ indexed by dominant coweights, while $\mathrm{Loc}_{G^\vee}(\mathbb{P}^1) = BG^\vee$; the equivalence reduces to a computation with $\mathrm{Rep}(G^\vee)$ and the nilpotent cone of $\mathfrak{g}^\vee$.
- **Genus $0$ with $3$ punctures ("pair of pants"), $G = \mathrm{SL}_2, \mathrm{PGL}_2$.** Proved by Nadler–Yun, *Geometric Langlands correspondence for $\mathrm{SL}(2)$, $\mathrm{PGL}(2)$ over the pair of pants*, Compositio Math. 155 (2019), including the parabolic/tame-ramified refinement.
- **Genus $1$.** Substantial progress: Ben-Zvi–Nadler's elliptic Springer theory (Compositio Math. 151, 2015) and Li–Nadler's uniformization of semistable bundles on elliptic curves give an explicit description of $\mathrm{Shv}_{\mathcal{N}}(\mathrm{Bun}_G(E))$ for $E$ elliptic, matching coherent sheaves on the elliptic character stack in the studied cases *(frontier — the full genus-one statement for all reductive $G$ is not published as a theorem)*.
- **Structural, all $(X,G)$.** The spectral action of $\mathrm{Perf}(\mathrm{Loc}_{G^\vee}(X))$ exists (Nadler–Yun, Israel J. Math. 232, 2019); both sides are modules over the same ring, so the conjecture becomes a statement about a single generating object.
- **Local/Betti gluing.** Ben-Zvi–Nadler's Betti spectral gluing describes $\mathrm{IndCoh}_{\mathcal{N}}$ by Eisenstein-type gluing along parabolics, giving the spectral analogue of the automorphic parabolic induction filtration.

## 5. Principal Obstacles

- **No Betti Whittaker sheaf.** The de Rham proof is organized around the Whittaker (Poincaré) object, built from the exponential $D$-module $e^{f}$ on $\mathbb{A}^1$ / the Artin–Schreier sheaf in the $\ell$-adic case. Neither has a Betti analogue: over $\mathbb{C}$ there is no rank-one constructible sheaf on $\mathbb{A}^1$ with the required irregular monodromy. All known Betti substitutes are non-compact or fail to generate.
- **No Fourier–Deligne transform.** Laumon's Fourier transform on vector bundle stacks — the engine behind Eisenstein series, the Vinberg degeneration and Hecke computations — has only a Mellin (torus) analogue in the Betti world, which is why abelian $G$ is easy and non-abelian $G$ is not.
- **Riemann–Hilbert does not transfer the theorem.** RH gives $\mathrm{Shv}_c(Y) \simeq D_{rh}(Y)$ only for finite-type $Y$ and does not respect the nilpotent singular support condition or the ind-completions in a way compatible with Hecke functors on $\mathrm{Bun}_G$, which is non-quasi-compact. Likewise, $\mathrm{Loc}^{dR}_{G^\vee}$ and $\mathrm{Loc}^{B}_{G^\vee}$ are only analytically, not algebraically, isomorphic (Riemann–Hilbert is transcendental), so coherent sheaf categories differ.
- **Non-abelian Hodge is not an equivalence of categories.** The Simpson correspondence relates de Rham and Betti moduli as real-analytic spaces but is not holomorphic, so it cannot be used to transport $\mathrm{IndCoh}$.
- **Singular support for constructible sheaves on stacks** is technically delicate: functoriality of $SS$ under the Hecke correspondences, and finiteness/compact generation of $\mathrm{Shv}_{\mathcal{N}}(\mathrm{Bun}_G)$, are only partially established.

## 6. The Gap

Proven: the torus case, genus $0$ (unpunctured and the $3$-punctured $\mathrm{SL}_2/\mathrm{PGL}_2$ case), the spectral action for all $(X,G)$, spectral gluing, and the whole de Rham conjecture.

Missing: a Betti object $\mathcal{W} \in \mathrm{Shv}_{\mathcal{N}}(\mathrm{Bun}_G)$ that (i) generates the category under the spectral action and (ii) has endomorphisms $\mathrm{End}(\mathcal{W}) \simeq \mathcal{O}(\mathrm{Loc}_{G^\vee}(X))$. Given Nadler–Yun's action, the conjecture reduces exactly to producing such a $\mathcal{W}$ and proving these two properties. Every known construction of $\mathcal{W}$ imports the exponential sheaf and therefore lives in the de Rham world. Bridging that step — either by a genuinely topological Whittaker model, or by proving a singular-support-compatible Riemann–Hilbert theorem on $\mathrm{Bun}_G$ — is the barrier.

## 7. Current Research (as of June 2026)

- **Austin/Berkeley/MIT (Ben-Zvi, Nadler, Yun).** TQFT formulation: realizing both sides as values of a $3$d/$4$d topological field theory, with the mapping class group action and cutting-and-gluing along pairs of pants as the organizing principle.
- **Skein theory and quantum character varieties** (Gunningham, Jordan, Safronov). The finiteness of skein modules (Gunningham–Jordan–Safronov, Invent. Math. 232, 2023) supplies the quantum/$A$-model side that the Betti conjecture predicts; deformation quantization of $\mathrm{Loc}_{G^\vee}$ is the natural home for the mapping class group symmetry.
- **Transport from de Rham.** Following the 2024 de Rham proof, several groups are attempting a categorical Riemann–Hilbert comparison respecting nilpotent singular support *(frontier — verify)*.
- **Relative and arithmetic analogues.** Ben-Zvi–Sakellaridis–Venkatesh's relative Langlands duality and Zhu's categorical local Langlands programme both use Betti-style spectral stacks; results there feed constraints back into the global Betti statement.
- **Cohomological Hall / Donaldson–Thomas methods** applied to character stacks give independent computations of $\mathrm{IndCoh}_{\mathcal{N}}(\mathrm{Loc}_{G^\vee})$ in low genus *(frontier — verify)*.

## 8. Future Work

1. Construct a topological Whittaker object, e.g. as a limit of nearby-cycle or Radon-transform constructions on $\mathrm{Bun}_N$.
2. Settle genus $1$ for all reductive $G$ using elliptic Springer theory, then bootstrap to $g\ge 2$ by gluing along pairs of pants — the strategy explicitly proposed by Ben-Zvi–Nadler.
3. Prove compact generation and a $t$-structure comparison for $\mathrm{Shv}_{\mathcal{N}}(\mathrm{Bun}_G)$; this alone would remove several technical hypotheses.
4. Verify the predicted mapping class group action as an independent test: it is a falsifiable consequence of the conjecture that has no de Rham counterpart.
5. Compute both sides' Hochschild/trace invariants (character varieties of $3$-manifolds) and check the resulting numerical identities.

## 9. Key References

- **[Foundational]** D. Ben-Zvi, D. Nadler. *Betti Geometric Langlands.* In *Algebraic Geometry: Salt Lake City 2015*, Proc. Sympos. Pure Math. 97.2, American Mathematical Society, 2018.
- **[Foundational]** D. Arinkin, D. Gaitsgory. *Singular support of coherent sheaves and the geometric Langlands conjecture.* Selecta Mathematica 21 (2015), 1–199.
- **[Foundational]** A. Kapustin, E. Witten. *Electric-magnetic duality and the geometric Langlands program.* Communications in Number Theory and Physics 1 (2007), 1–236.
- **[SOTA]** D. Nadler, Z. Yun. *Spectral action in Betti geometric Langlands.* Israel Journal of Mathematics 232 (2019), 299–349.
- **[SOTA]** D. Nadler, Z. Yun. *Geometric Langlands correspondence for $\mathrm{SL}(2)$, $\mathrm{PGL}(2)$ over the pair of pants.* Compositio Mathematica 155 (2019), 324–371.
- **[SOTA]** D. Ben-Zvi, D. Nadler. *Elliptic Springer theory.* Compositio Mathematica 151 (2015), 1568–1584.
- **[SOTA]** P. Li, D. Nadler. *Uniformization of semistable bundles on elliptic curves.* Advances in Mathematics, 2021.
- **[SOTA]** D. Gaitsgory, S. Raskin, et al. *Proof of the geometric Langlands conjecture I–V.* Preprint series, 2024.
- **[Related]** S. Gunningham, D. Jordan, P. Safronov. *The finiteness conjecture for skein modules.* Inventiones mathematicae 232 (2023), 301–363.
- **[Survey]** I. Mirković, K. Vilonen. *Geometric Langlands duality and representations of algebraic groups over commutative rings.* Annals of Mathematics 166 (2007), 95–143.
- **[Survey]** O. Gabber, F. Loeser. *Faisceaux pervers $\ell$-adiques sur un tore.* Duke Mathematical Journal 83 (1996), 501–606.

## 10. Worked Example / Concrete Special Case

Take $X = E$ an elliptic curve ($g=1$) and $G = \mathbb{G}_m$, so $G^\vee = \mathbb{G}_m$.

**Spectral side.** $\pi_1(E) = \mathbb{Z}^2$, so
$$\mathrm{Loc}_{\mathbb{G}_m}(E) = \mathrm{Hom}(\mathbb{Z}^2, \mathbb{G}_m) \times B\mathbb{G}_m = (\mathbb{C}^\times)^2 \times B\mathbb{G}_m .$$
This is smooth (the derived structure is trivial because $\mathbb{G}_m$ is abelian and the commutator equation is vacuous), so $\mathcal{N}$ is the zero section and $\mathrm{IndCoh}_{\mathcal{N}} = \mathrm{QCoh}$. Hence
$$\mathrm{IndCoh}_{\mathcal{N}}(\mathrm{Loc}_{\mathbb{G}_m}(E)) \;=\; \mathrm{QCoh}\big((\mathbb{C}^\times)^2\big) \otimes \mathrm{Rep}(\mathbb{G}_m) \;=\; \mathrm{QCoh}\big((\mathbb{C}^\times)^2\big)^{\oplus \mathbb{Z}} .$$

**Automorphic side.** $\mathrm{Bun}_{\mathbb{G}_m}(E) = \mathrm{Pic}(E) = \coprod_{d\in\mathbb{Z}} \mathrm{Pic}^d(E) \times B\mathbb{G}_m$, and for an elliptic curve $\mathrm{Pic}^d(E) \cong E$ via $L \mapsto$ its Abel–Jacobi class. The nilpotent cone for a torus is the zero section, so
$$\mathrm{Shv}_{\mathcal{N}}(\mathrm{Bun}_{\mathbb{G}_m}(E)) = \mathrm{LocSys}\big(\mathbb{Z} \times E \times B\mathbb{G}_m\big) = \Big(\mathrm{Rep}_{\mathbb{C}}(\pi_1 E)\Big)^{\oplus \mathbb{Z}},$$
the $\mathbb{Z}$ from the degree components, and $B\mathbb{G}_m$ contributing only its trivial gerbe-weight decomposition.

**The matching.** A rank-one local system on $E$ is determined by its two monodromies $(a,b) \in (\mathbb{C}^\times)^2$; the Mellin transform sends a $\pi_1(E)=\mathbb{Z}^2$-representation to a quasi-coherent sheaf on the character torus:
$$\mathrm{LocSys}(E) \simeq \mathrm{Mod}_{\mathbb{C}[\mathbb{Z}^2]} = \mathrm{QCoh}\big(\mathrm{Spec}\,\mathbb{C}[x^{\pm},y^{\pm}]\big) = \mathrm{QCoh}\big((\mathbb{C}^\times)^2\big).$$
Summing over $d\in\mathbb{Z}$ on both sides gives the asserted equivalence. **Hecke check:** at $x\in E$ the Hecke operator for the tautological character is $L \mapsto L(x)$, i.e. translation by $x$ on $\mathrm{Pic}^d \cong E$ combined with the shift $d\mapsto d+1$. Under Mellin, translation by $x$ acts on the local system $\mathcal{L}_{(a,b)}$ by the scalar $\chi_{(a,b)}(x)$ — exactly multiplication by the fibre at $x$ of the tautological line bundle on $(\mathbb{C}^\times)^2 \times E$. So the equivalence intertwines Hecke and tensoring, as required by condition (1) of §1.

For $G = \mathrm{SL}_2$ on the same curve, $\mathrm{Loc}_{\mathrm{PGL}_2}(E)$ acquires genuine derived structure at the reducible locus, $\mathcal{N}$ becomes nontrivial, and no Mellin transform is available — this is precisely where the general problem begins.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*