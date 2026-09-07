---
id: 04-topology/arnold-chord-conjecture
title: "Arnold Chord Conjecture"
topic: 04-topology
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Arnold Chord Conjecture

> **Topic:** Topology & Knot Theory · **ID:** `04-topology/arnold-chord-conjecture` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Let $(M^{2n+1},\xi)$ be a closed contact manifold with a contact form $\alpha$ (so $\xi=\ker\alpha$ and $\alpha\wedge(d\alpha)^n\neq0$), and let $R_\alpha$ be its Reeb vector field. Let $L\subset M$ be a closed Legendrian submanifold, i.e. $\dim L=n$ and $T_pL\subset\xi_p$ for all $p\in L$.

**Chord conjecture (Arnold, 1986).** There exists a *Reeb chord* of $L$: a non-constant trajectory $c:[0,T]\to M$, $T>0$, with $\dot c(t)=R_\alpha(c(t))$ and $c(0),c(T)\in L$.

**Quantitative form.** The number of Reeb chords is at least $\tfrac12\dim H_*(L;\mathbb{Z}/2)$ when the chords are nondegenerate — the Legendrian analogue of Arnold's Lagrangian intersection conjecture.

A complete resolution means either a proof for all closed $(M,\alpha,L)$ in every dimension, or a counterexample: an explicit closed Legendrian $L$ and contact form $\alpha$ whose Reeb flow admits no chord with both endpoints on $L$. The hypotheses are sharp in the sense that *compactness of $L$* and *$\alpha$ being a genuine contact form* (not merely a stable Hamiltonian structure) cannot be dropped.

## 2. Mathematical Foundations

**Contact data.** On $\mathbb{R}^{2n+1}$ with coordinates $(x_1,y_1,\dots,x_n,y_n,z)$ the standard contact form is
$$\alpha_{\mathrm{std}}=dz-\sum_{i=1}^n y_i\,dx_i,\qquad R_{\alpha_{\mathrm{std}}}=\partial_z .$$
The Reeb field of a general $\alpha$ is determined by $\alpha(R_\alpha)=1$, $\iota_{R_\alpha}d\alpha=0$.

**Legendrian condition and chords.** $L^n\subset M^{2n+1}$ is Legendrian iff $\alpha|_{TL}\equiv 0$; this is the maximal integral dimension for $\xi$. In $(\mathbb{R}^{2n+1},\alpha_{\mathrm{std}})$ the Lagrangian projection $\pi_{\mathbb{C}^n}(x,y,z)=(x,y)$ sends $L$ to an exact immersed Lagrangian, and
$$\{\text{Reeb chords of }L\}\ \longleftrightarrow\ \{\text{double points of }\pi_{\mathbb{C}^n}(L)\},$$
the chord length ("action") of a chord $c$ being $\mathcal{A}(c)=\int_c\alpha=z(c(T))-z(c(0))$.

**Action functional.** Chords are critical points of the Legendrian action functional on paths with endpoints on $L$; nondegeneracy of a chord means $d\phi_T(T_{c(0)}L)\pitchfork T_{c(T)}L$ inside $\xi$, where $\phi_t$ is the Reeb flow.

**Holomorphic curve machinery.** Fix an $\mathbb{R}$-invariant almost complex structure $J$ on the symplectization $(\mathbb{R}\times M,\ d(e^s\alpha))$ with $J(\partial_s)=R_\alpha$ and $J\xi=\xi$. Finite-energy $J$-holomorphic maps $u:(\Sigma,\partial\Sigma)\to(\mathbb{R}\times M,\mathbb{R}\times L)$ have boundary punctures asymptotic to Reeb chords of $L$ and interior punctures asymptotic to closed Reeb orbits (Hofer's asymptotic analysis). Counting rigid such strips defines the Chekanov–Eliashberg DGA $(\mathcal{A}(L),\partial)$, freely generated over $\mathbb{Z}/2$ (or $\mathbb{Z}[H_1(L)]$) by the Reeb chords, with
$$\partial a=\sum_{b_1,\dots,b_k}\\#\mathcal{M}(a;b_1,\dots,b_k)\,b_1\cdots b_k .$$
Its homology (Legendrian contact homology, LCH) is a Legendrian isotopy invariant. **If $L$ had no Reeb chord, $\mathcal{A}(L)$ would be the trivial algebra**, so any nonvanishing/nontrivial LCH computation forces chords to exist.

**Relation to the Weinstein conjecture.** Contact surgery/doubling arguments turn chord existence into closed-orbit existence: the chord conjecture for $L\subset M$ is the "open string" version of the Weinstein conjecture "every closed contact manifold carries a closed Reeb orbit", proved in dimension 3 by Taubes (2007) via Seiberg–Witten theory.

## 3. History & State of the Art (SOTA)

- **1986.** V. I. Arnold, *First steps in symplectic topology* (Russian Math. Surveys **41**), poses the chord conjecture for Legendrian curves in the standard contact $S^3$, motivated by wave-front singularities, the four-vertex theorem, and his Lagrangian intersection conjectures.
- **1993.** Hofer introduces pseudoholomorphic curves in symplectizations, proving the Weinstein conjecture for overtwisted $\xi$ and for $\pi_2(M)\neq0$; the same bubbling analysis yields chords in the overtwisted and "sufficiently non-tight" 3-dimensional settings.
- **1999.** Abbas (*Duke Math. J.* **96**) proves the chord conjecture for Legendrian *unknots* in the tight $S^3$ with contact forms $f\alpha_{\mathrm{std}}$, via finite-energy surfaces and open-book/foliation techniques.
- **2001.** Mohnke (*Ann. of Math.* **154**) proves the conjecture for **every** closed Legendrian in $(\mathbb{R}^{2n+1},\xi_{\mathrm{std}})$ and in subcritically Stein-fillable contact manifolds, all $n$, using punctured holomorphic disks with a Lagrangian boundary and a neck-stretching/degeneration argument.
- **2002–2009.** Chekanov's DGA and its higher-dimensional version (Ekholm–Etnyre–Sullivan) turn chord counting into algebra; Ekholm–Etnyre–Sabloff duality gives the sharp lower bound $\tfrac12\dim H_*(L;\mathbb{Z}/2)$ for Legendrians admitting exact Lagrangian fillings.
- **2011/2013.** **Hutchings–Taubes settle dimension 3 completely**: every Legendrian knot in any closed contact 3-manifold, for any contact form, has a Reeb chord (Part I: nondegenerate forms; Part II: the general case). The proof runs through embedded contact homology (ECH) and Taubes' Seiberg–Witten $\Rightarrow$ ECH isomorphism.
- **2016–present.** Dimitroglou Rizell and collaborators extend existence and counting results to Legendrians in $P\times\mathbb{R}$ for Liouville $P$, and to displaceable settings, via lifted holomorphic polygons and Lagrangian caps.

**SOTA summary:** solved in dimension 3 unconditionally; solved in all dimensions for $\mathbb{R}^{2n+1}$ and subcritically fillable ambients; open for general closed contact manifolds of dimension $\ge5$.

## 4. Partial Results / Verified Cases

| Setting | Result | Source |
|---|---|---|
| $\dim M=3$, any closed $(M,\alpha)$, any Legendrian knot | Chord exists (all cases) | Hutchings–Taubes I (2011), II (2013) |
| $\dim M=3$, overtwisted $\xi$ or $\pi_2(M)\ne0$ | Chord exists | Hofer (1993) |
| Legendrian unknot in tight $S^3$, $\alpha=f\alpha_{\mathrm{std}}$ | Chord exists | Abbas (1999) |
| $(\mathbb{R}^{2n+1},\xi_{\mathrm{std}})$, all $n\ge1$, any closed Legendrian | Chord exists | Mohnke (2001) |
| Subcritically Stein-fillable $(M^{2n+1},\xi)$ | Chord exists | Mohnke (2001) |
| $L\subset J^1(N)=T^*N\times\mathbb{R}$, $L$ the 1-jet lift of a function | Chords $\leftrightarrow$ critical points; $\ge \mathrm{cat}(N)$ chords after perturbation | classical Morse theory |
| $L$ with an exact Lagrangian filling in $\mathbb{R}^{2n+1}$ | $\\#\{\text{chords}\}\ \ge\ \tfrac12\dim H_*(L;\mathbb{Z}/2)$ | Ekholm–Etnyre–Sabloff (2009) |
| $L$ with nonvanishing linearized LCH | $\\#\{\text{chords}\}\ \ge\ \dim LCH_*$ | Chekanov (2002); Ekholm–Etnyre–Sullivan (2005) |
| $L\subset P\times\mathbb{R}$, $P$ Liouville, $L$ displaceable | Chord exists | Dimitroglou Rizell (2016) |

Concrete counts: the Legendrian unknot with $tb=-1$ in $\mathbb{R}^3$ has exactly $1$ chord (sharp, $=\tfrac12\dim H_*(S^1)$); the Chekanov–Eliashberg $m(5_2)$ Legendrian pair has $5$ chords each, distinguished by their DGAs.

## 5. Principal Obstacles

- **Compactness fails in the open string setting.** Chord existence proofs run by contradiction: assume no chords, then a moduli space of holomorphic disks with boundary on $\mathbb{R}\times L$ is compact, and a count gives a contradiction. Without chords there are no boundary punctures to absorb energy, but *interior* bubbling into closed Reeb orbits and multiple-cover degenerations still occur; controlling them requires either dimension-3 ECH index positivity or a subcritical/flexible filling.
- **No transversality in general.** Somewhere-injective genericity fails for multiply covered curves in dimensions $\ge5$; polyfold or Kuranishi virtual perturbation is needed, and the resulting counts are rational, destroying the integrality arguments that make Mohnke's disk count work.
- **Seiberg–Witten theory is 3-dimensional.** The Hutchings–Taubes proof is not soft: it uses ECH $\cong\widehat{HM}$ and the Weinstein-conjecture machinery of Taubes, all of which are special to $\dim 3$ (and $\dim 4$ symplectic cobordisms). There is no gauge-theoretic substitute in higher dimensions.
- **Fillings may not exist.** Mohnke's argument needs a symplectic filling with a subcritical (or at least controlled) Weinstein handle decomposition to cap off the disks. Many contact manifolds — including all overtwisted ones in higher dimensions — admit no such filling, and the relevant $J$-holomorphic disks can escape to infinity in the completion.
- **Algebra can be trivial for reasons other than absence of chords.** LCH-based proofs only work if one can show $\mathcal{A}(L)$ is nontrivial *a priori*; augmentations may fail to exist, and the DGA of a Legendrian with a single "long" chord can have vanishing homology, so the algebraic route gives no unconditional existence statement.

## 6. The Gap

Everything proved rests on one of three inputs: (i) 3-dimensional gauge theory, (ii) a subcritical/Stein filling that lets one cap holomorphic disks, (iii) a displacement or exactness hypothesis in a split ambient $P\times\mathbb{R}$. The open case is exactly the complement:

> A closed contact manifold $(M^{2n+1},\xi)$, $n\ge2$, with **no** symplectic filling and no split structure, carrying a closed Legendrian $L^n$.

The precise missing step is a **compactness-and-count theorem for finite-energy holomorphic disks with boundary on $\mathbb{R}\times L$ in an arbitrary symplectization of dimension $\ge6$**, robust under virtual perturbation, that produces a nonzero rigid count from purely topological input (e.g. $[L]\ne0$ or $H_*(L)\ne0$). Equivalently: a higher-dimensional replacement for the ECH index inequality that makes the "no chords $\Rightarrow$ compact moduli space $\Rightarrow$ contradiction" argument dimension-independent. Even conditional on the higher-dimensional Weinstein conjecture (itself open), no implication to the chord conjecture is known.

## 7. Current Research (as of June 2026)

- **Higher-dimensional ECH substitutes.** Efforts to build an index-positive contact invariant beyond dimension 3 — via Hutchings' embedded-contact-style indices, or via microlocal sheaf-theoretic Legendrian invariants (Nadler, Shende, Treumann, Zaslow) that see chords through singular support. Sheaf methods currently need Weinstein-type ambients. *(frontier — verify)*
- **Uppsala/Cambridge school (Dimitroglou Rizell, Ekholm, Golovko).** Lifting holomorphic polygons, Lagrangian caps and endocobordisms; results on rigidity of chord counts and on Legendrians with prescribed small numbers of chords.
- **Rabinowitz Floer homology for Legendrians** (Cieliebak–Frauenfelder circle, Merry, Albers): a Lagrangian/Legendrian Rabinowitz functional whose critical points are chords, giving existence whenever the associated Floer homology is nonzero — currently restricted to exact contact embeddings into symplectically aspherical fillings.
- **Quantitative refinements in dimension 3.** Sharp bounds on the number of chords, chord actions and systolic-type inequalities via ECH spectral invariants (Hutchings, Cristofaro-Gardiner, Hryniewicz); the "exactly one chord forces unknottedness" phenomenon is being pushed toward classification statements. *(frontier — verify)*
- **Search for counterexamples.** Ginzburg-style $C^2$ constructions that defeated the Hamiltonian Seifert conjecture are being adapted to chordless Legendrian configurations for stable Hamiltonian structures; no genuine contact counterexample is known. *(frontier — verify)*

## 8. Future Work

1. **Prove the conjecture for Weinstein-fillable $(M^{2n+1},\xi)$** with critical handles — the first case beyond Mohnke's subcritical theorem. Strategy: relate the LCH of $L$ to the wrapped Floer cohomology of a Lagrangian in the filling (Ekholm–Lekili surgery formula) and show nonvanishing from $H_*(L)$.
2. **Establish the quantitative bound $\\#\ge\tfrac12\dim H_*(L;\mathbb{Z}/2)$ without a filling hypothesis**, i.e. remove the Ekholm–Etnyre–Sabloff duality assumption.
3. **Overtwisted higher dimensions.** Borman–Eliashberg–Murphy overtwistedness gives an $h$-principle; determine whether chords can be made to vanish for loose Legendrians in overtwisted contact structures, or prove flexibility still forces chords.
4. **Degenerate contact forms.** Extend the Hutchings–Taubes Part II removal of nondegeneracy to whatever higher-dimensional argument emerges; degenerate forms are precisely where naive limiting arguments lose the chord.
5. **Non-compact and singular Legendrians.** Chord existence for Legendrians with conical ends or with singularities (arising from wave fronts), the setting closest to Arnold's original motivation.

## 9. Key References

- **[Foundational]** V. I. Arnold. *First steps in symplectic topology.* Russian Mathematical Surveys **41** (1986), no. 6, 1–21.
- **[Foundational]** H. Hofer. *Pseudoholomorphic curves in symplectizations with applications to the Weinstein conjecture in dimension three.* Inventiones Mathematicae **114** (1993), 515–563.
- **[Foundational]** C. Abbas. *Finite energy surfaces and the chord problem.* Duke Mathematical Journal **96** (1999), 241–316.
- **[SOTA]** K. Mohnke. *Holomorphic disks and the chord conjecture.* Annals of Mathematics (2) **154** (2001), 219–222.
- **[SOTA]** M. Hutchings, C. H. Taubes. *Proof of the Arnold chord conjecture in three dimensions, I.* Geometry & Topology **15** (2011), 901–964.
- **[SOTA]** M. Hutchings, C. H. Taubes. *Proof of the Arnold chord conjecture in three dimensions, II.* Geometry & Topology **17** (2013), 2601–2688.
- **[SOTA]** C. H. Taubes. *The Seiberg–Witten equations and the Weinstein conjecture.* Geometry & Topology **11** (2007), 2117–2202.
- **[Structural]** Yu. Chekanov. *Differential algebra of Legendrian links.* Inventiones Mathematicae **150** (2002), 441–483.
- **[Structural]** T. Ekholm, J. Etnyre, M. Sullivan. *The contact homology of Legendrian submanifolds in $\mathbb{R}^{2n+1}$.* Journal of Differential Geometry **71** (2005), 177–305.
- **[Structural]** T. Ekholm, J. Etnyre, J. Sabloff. *A duality exact sequence for Legendrian contact homology.* Duke Mathematical Journal **150** (2009), 1–75.
- **[Recent]** G. Dimitroglou Rizell. *Lifting pseudo-holomorphic polygons to the symplectisation of $P\times\mathbb{R}$ and applications.* Quantum Topology **7** (2016), 29–105.
- **[Survey]** Y. Eliashberg, A. Givental, H. Hofer. *Introduction to symplectic field theory.* Geometric and Functional Analysis, Special Volume (2000), 560–673.
- **[Survey]** C. Abbas, H. Hofer. *Holomorphic Curves and Global Questions in Contact Geometry.* Birkhäuser, 2019.
- **[Survey]** V. Ginzburg. *The Weinstein conjecture and theorems of nearby and almost existence.* In *The Breadth of Symplectic and Poisson Geometry*, Progress in Mathematics **232**, Birkhäuser, 2005, 139–172.
- **[Background]** K. Cieliebak, Y. Eliashberg. *From Stein to Weinstein and Back: Symplectic Geometry of Affine Complex Manifolds.* AMS Colloquium Publications **59**, 2012.

## 10. Worked Example / Concrete Special Case

**Claim (chord conjecture in $(\mathbb{R}^3,\alpha=dz-y\,dx)$, elementary proof).** Every closed embedded Legendrian curve $L\subset\mathbb{R}^3$ has a Reeb chord.

*Proof.* Here $R_\alpha=\partial_z$, so a Reeb chord is a vertical segment with both endpoints on $L$: exactly a double point of the Lagrangian projection $\gamma=\pi(L)\subset\mathbb{R}^2_{x,y}$. Suppose $L$ has no chord. Then $\gamma$ is an *embedded* closed curve. Since $L$ is Legendrian, $dz=y\,dx$ along $L$, so
$$0=\oint_L dz=\oint_\gamma y\,dx=-\operatorname{Area}(\text{region bounded by }\gamma)\ \ne 0$$
by Green's theorem applied to the embedded curve $\gamma$. Contradiction. $\square$

**Explicit instance.** Take the figure-eight Lagrangian projection
$$\gamma(t)=(x(t),y(t))=(\sin t,\ \sin 2t),\qquad t\in[0,2\pi].$$
It is immersed: $\dot x=\cos t$ and $\dot y=2\cos 2t$ never vanish together ($\cos t=0\Rightarrow\cos2t=-1$). Its unique double point is $\gamma(0)=\gamma(\pi)=(0,0)$. The Legendrian lift is $z(t)=\int_0^t y\,dx$:
$$z(t)=\int_0^t \sin 2s\,\cos s\,ds=\int_0^t 2\sin s\cos^2 s\,ds=\tfrac23\bigl(1-\cos^3 t\bigr).$$
Closedness: $z(2\pi)=0=z(0)$, consistent with zero signed area. The lift $L=\{(\sin t,\sin2t,z(t))\}$ is embedded in $\mathbb{R}^3$ because the two preimages of the double point lift to different heights:
$$z(0)=0,\qquad z(\pi)=\tfrac23\bigl(1-(-1)\bigr)=\tfrac43 .$$
So $L$ has exactly **one** Reeb chord, the vertical segment from $(0,0,0)$ to $(0,0,\tfrac43)$, of action $\mathcal{A}=\tfrac43$.

**Invariants.** $L$ is a Legendrian unknot; $tb(L)=\mathrm{writhe}(\gamma)=-1$ and $r(L)=0$ (the tangent $\dot\gamma$ has winding number $0$). The chord count is sharp:
$$\\#\{\text{chords}\}=1=\tfrac12\dim H_*(S^1;\mathbb{Z}/2)=\tfrac12(1+1).$$
The Chekanov–Eliashberg DGA has a single generator $a$ (Conley–Zehnder grading $|a|=1$) with $\partial a=1+1=0$ over $\mathbb{Z}/2$ counting the two half-disks of the figure eight — the augmentation $\varepsilon(a)=0$ exists and linearized LCH is $\mathbb{Z}/2$ in degree $1$, matching the single chord.

In dimension $\ge5$ the Green's-theorem argument has no analogue: an embedded Lagrangian projection of $L^n\subset\mathbb{R}^{2n+1}$ is an *exact* embedded Lagrangian in $\mathbb{C}^n$, and ruling those out is Gromov's theorem, whose proof is itself the holomorphic-disk argument that Mohnke had to upgrade — and which no one knows how to run in a general closed contact manifold.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*