---
id: 04-topology/casson-invariant-homology-cobordism
title: "Casson Invariant and the Homology Cobordism Group Structure"
topic: 04-topology
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Casson Invariant and the Homology Cobordism Group Structure

> **Topic:** Topology & Knot Theory · **ID:** `04-topology/casson-invariant-homology-cobordism` · **Status:** open

## 1. Problem Statement / Conjecture

Let $\Theta^3_{\mathbb{Z}}$ be the group of oriented integral homology 3-spheres modulo integral homology cobordism, with connected sum as the operation. The Casson invariant $\lambda:\{\mathbb{Z}\mathrm{HS}^3\}\to\mathbb{Z}$ is additive under $\\#$ but is **not** a homology cobordism invariant; only its mod 2 reduction, the Rokhlin invariant $\mu$, descends to a surjection $\mu:\Theta^3_{\mathbb{Z}}\to\mathbb{Z}/2$. The problem is to determine the structure of $\Theta^3_{\mathbb{Z}}$ and how far Casson-type (gauge-theoretic) invariants determine it. Precisely:

- **(Q1) Torsion.** Is $\Theta^3_{\mathbb{Z}}$ torsion-free? Equivalently, if $\Sigma \\# \cdots \\# \Sigma$ ($n$ copies, $n \ge 2$) bounds a compact smooth $\mathbb{Z}$-homology 4-ball, must $\Sigma$ bound one?
- **(Q2) Freeness.** Is $\Theta^3_{\mathbb{Z}}\cong\mathbb{Z}^\infty$ (free abelian of countably infinite rank)?
- **(Q3) Casson detection.** Is there an integer-valued homology cobordism *homomorphism* $q:\Theta^3_{\mathbb{Z}}\to\mathbb{Z}$ with $q\equiv\lambda\pmod 2$, i.e. lifting $\mu$? More broadly: does the instanton Floer homology whose Euler characteristic is $2\lambda$ determine the order of $[\Sigma]$?

A complete resolution of (Q1)/(Q2) means an isomorphism $\Theta^3_{\mathbb{Z}}\cong\mathbb{Z}^\infty$ with proof, or the exhibition of a homology sphere of finite order $n>1$. (Q3) has a known negative answer for homomorphisms (Manolescu, 2016); the open form asks for the strongest non-homomorphic lift.

## 2. Mathematical Foundations

**Homology cobordism.** $\Sigma_0\sim\Sigma_1$ iff there is a compact oriented smooth 4-manifold $W$ with $\partial W=\Sigma_0\sqcup(-\Sigma_1)$ and $H_*(W;\mathbb{Z})\cong H_*(\Sigma_0\times[0,1];\mathbb{Z})$. Then $\Theta^3_{\mathbb{Z}}=\{\mathbb{Z}\mathrm{HS}^3\}/\!\sim$, with identity $[S^3]$ and $-[\Sigma]=[-\Sigma]$.

**Casson invariant.** For a Heegaard splitting $\Sigma=H_1\cup_F H_2$ of genus $g$, the $SU(2)$ representation varieties $R(H_i)\subset R(F)$ meet in $R(\Sigma)$. Casson defines
$$\lambda(\Sigma)=\tfrac12\,\big\langle R(H_1),R(H_2)\big\rangle_{R^{\mathrm{irr}}(F)},$$
half the signed count of irreducible $SU(2)$ representations of $\pi_1(\Sigma)$, after perturbation to transversality. It satisfies:

1. **Surgery formula.** For a knot $K\subset S^3$ and $n\in\mathbb{Z}$,
$$\lambda\big(S^3_{1/n}(K)\big)=\frac{n}{2}\,\Delta_K''(1),$$
with $\Delta_K$ the Conway-normalized Alexander polynomial, $\Delta_K(1)=1$.
2. **Additivity.** $\lambda(\Sigma_1\\#\Sigma_2)=\lambda(\Sigma_1)+\lambda(\Sigma_2)$, and $\lambda(-\Sigma)=-\lambda(\Sigma)$.
3. **Rokhlin reduction.** $\lambda(\Sigma)\equiv\mu(\Sigma)\pmod 2$, where $\mu(\Sigma)=\sigma(W)/8 \bmod 2$ for any spin 4-manifold $W$ with $\partial W=\Sigma$.
4. **Casson's theorem.** $\lambda(\Sigma)\neq0\Rightarrow\pi_1(\Sigma)$ admits an irreducible $SU(2)$ representation, hence $\pi_1(\Sigma)\neq1$.

**Gauge-theoretic reformulation (Taubes).** $\lambda(\Sigma)=\tfrac12\chi\big(HF_*^{\mathrm{inst}}(\Sigma)\big)$, the Euler characteristic of Floer's $\mathbb{Z}/8$-graded instanton homology, defined from the Chern–Simons functional $CS(A)=\frac{1}{8\pi^2}\int_\Sigma \mathrm{tr}(A\wedge dA+\tfrac23A^{\wedge3})$.

**Brieskorn spheres.** For pairwise coprime $p,q,r\ge2$, $\Sigma(p,q,r)=\{x^p+y^q+z^r=0\}\cap S^5$ and
$$\lambda\big(\Sigma(p,q,r)\big)=\tfrac18\,\sigma\big(F(p,q,r)\big),$$
$\sigma$ the signature of the Milnor fiber. E.g. $\sigma(F(2,3,5))=-8$ (the $E_8$ form), so $\lambda(\Sigma(2,3,5))=-1$ and $\mu=1$: $\mu$ is surjective.

**Why $\lambda$ fails to descend.** $\lambda$ is a *finite-type* invariant of degree 1 in the Ohtsuki filtration; homology cobordism does not control $\Delta_K''(1)$, as Section 10 shows.

## 3. History & State of the Art (SOTA)

- **1952/1958.** Rokhlin's theorem gives $\mu:\Theta^3_{\mathbb{Z}}\to\mathbb{Z}/2$; $\Theta^3_{\mathbb{Z}}$ appears in Kervaire–Milnor-style surgery.
- **1970s.** Galewski–Stern and Matumoto reduce the triangulation of topological manifolds in dimension $\ge5$ to the question of whether $\mu$ splits: manifolds of dimension $\ge 5$ are triangulable iff there is a homomorphic section of $\mu$.
- **1985.** Casson introduces $\lambda$ in lectures at MSRI; notes published by Akbulut–McCarthy (1990). Fintushel–Stern's pseudofree-orbifold $R$-invariant shows $\Sigma(2,3,7)$ has infinite order, so $\Theta^3_{\mathbb{Z}}$ is infinite.
- **1988–1990.** Floer's instanton homology; Taubes proves $\lambda=\tfrac12\chi(HF^{\mathrm{inst}})$. Fintushel–Stern (1990) and Furuta (1990) prove $\Theta^3_{\mathbb{Z}}$ contains $\mathbb{Z}^\infty$: $\{\Sigma(2,3,6k-1)\}_{k\ge1}$ is independent.
- **1996–2004.** Frøyshov's $h$-invariant, a surjective homomorphism $\Theta^3_{\mathbb{Z}}\to\mathbb{Z}$ from Yang–Mills/Seiberg–Witten Floer theory; Ozsváth–Szabó's $d$-invariant gives another.
- **2013/2016.** Manolescu's $\beta$ from $Pin(2)$-equivariant Seiberg–Witten Floer homology: no $\Sigma$ with $\mu(\Sigma)=1$ satisfies $2[\Sigma]=0$. Hence $\mu$ does not split and non-triangulable manifolds exist in every dimension $\ge5$.
- **2018–2023.** Dai–Hom–Stoffregen–Truong prove $\Theta^3_{\mathbb{Z}}$ contains a $\mathbb{Z}^\infty$ **direct summand**, via involutive Heegaard Floer homology and the knot-concordance homomorphisms $\varphi_j$.
- **2020–2023.** Daemi's $\Gamma$-invariants and Nozaki–Sato–Taniguchi's filtered instanton $r_s$-invariants give new constraints; the subgroup generated by Seifert fibered homology spheres is shown not to be all of $\Theta^3_{\mathbb{Z}}$, and admits infinite-rank complements.

**SOTA summary:** $\mathbb{Z}^\infty\ \oplus\ ? \;\hookrightarrow\;\Theta^3_{\mathbb{Z}}$ with a $\mathbb{Z}^\infty$ summand known; no torsion element known and none excluded in general.

## 4. Partial Results / Verified Cases

- **Infinite rank.** $\Sigma(2,3,6k-1)$, $k\ge1$, generate $\mathbb{Z}^\infty\subset\Theta^3_{\mathbb{Z}}$ (Fintushel–Stern 1990; Furuta 1990).
- **Infinite-rank summand.** $\Theta^3_{\mathbb{Z}}\cong\mathbb{Z}^\infty\oplus G$ for some $G$ (Dai–Hom–Stoffregen–Truong 2023), using $(+1)$-surgeries on twisted Whitehead doubles.
- **No 2-torsion with $\mu=1$.** If $\mu(\Sigma)=1$ then $2[\Sigma]\neq0$ (Manolescu 2016). Torsion classes must have $\mu=0$ and vanishing $d$, $h$, $\beta$, $\bar\mu$.
- **Seifert fibered spaces.** No Seifert fibered $\mathbb{Z}\mathrm{HS}^3$ other than $S^3$ is torsion; the Neumann–Siebenmann invariant $\bar\mu$ is a homology cobordism invariant on this class (Stoffregen 2020, via $Pin(2)$-SWF), and $\bar\mu \equiv \mu \bmod 2$.
- **Casson invariant conjecture (Neumann–Wahl).** For links of complete intersection surface singularities that are $\mathbb{Z}\mathrm{HS}^3$, $\lambda(\Sigma)=\sigma(F)/8$: proven for Brieskorn complete intersections and for splice-quotient singularities (Némethi–Okuma 2009); open in full generality.
- **$\lambda$ is not a cobordism invariant.** Explicit: $\lambda\big(S^3_{+1}(K)\big)=2$ for $K$ the square knot, which is slice, so $[S^3_{+1}(K)]=0$ (Section 10).
- **Homomorphisms known.** $d/2$, $h$, $\beta$, $\varphi_j$, $\Gamma$ and $r_s$-derived maps give surjections onto $\mathbb{Z}$ and onto $\mathbb{Z}^\infty$; none is congruent to $\lambda$ mod 2 as a homomorphism (impossible by Manolescu).

## 5. Principal Obstacles

- **$\lambda$ is a Euler characteristic, not a filtration.** $\lambda=\tfrac12\chi(HF^{\mathrm{inst}})$ is insensitive to cancellation: a nontrivial homology cobordism can kill Floer generators in pairs. Any cobordism-invariant refinement must use the $\mathbb{R}$-filtration by Chern–Simons values or an equivariant structure, not the count itself.
- **Reducibles and the $\mathbb{Z}/8$ grading.** Instanton Floer homology has no $\mathbb{Z}$-grading and no natural absolute correction term; Frøyshov's $h$ requires $S^1$-equivariant enhancements that are hard to compute outside plumbed/Seifert families.
- **Torsion is invisible to $\mathbb{R}$-valued homomorphisms.** Every known invariant ($d$, $h$, $\beta$, $\varphi_j$, $\Gamma$, $r_s$) is either a homomorphism to a torsion-free group or a quasi-morphism, so it vanishes identically on any torsion class. Detecting a hypothetical $\mathbb{Z}/n$ requires a genuinely torsion-sensitive invariant — none exists.
- **No computable model for general $\Sigma$.** Explicit Floer computations are confined to Seifert fibered spaces, surgeries on small knots, and plumbings with at most one bad vertex. Hyperbolic homology spheres are essentially inaccessible.
- **Smooth vs. topological.** In the topological category $\Theta^{3,\mathrm{top}}_{\mathbb{Z}}=0$ (Freedman), so every obstruction must be smooth; gauge theory is the only source, and it does not see $\mathbb{Z}/n$-symmetry of cobordisms.

## 6. The Gap

Proven: $\Theta^3_{\mathbb{Z}}$ contains $\mathbb{Z}^\infty$ as a direct summand and has no 2-torsion of Rokhlin invariant 1. Claimed: $\Theta^3_{\mathbb{Z}}\cong\mathbb{Z}^\infty$. The gap is the complement $G$ in $\Theta^3_{\mathbb{Z}}\cong\mathbb{Z}^\infty\oplus G$: nothing is known about $G$ beyond that it is not detected by any current invariant. Concretely, one must either

- construct an invariant $\tau:\Theta^3_{\mathbb{Z}}\to A$ with $A$ containing torsion and $\tau$ nonzero on some $n$-torsion class — no candidate functional exists — or
- prove a *cancellation theorem*: if $n\Sigma$ bounds a $\mathbb{Z}$-homology ball then $\Sigma$ does. Every known proof of infinite order factors through a real-valued homomorphism and therefore proves nothing about $n$-torsion.

For (Q3), the gap is quantitative: Manolescu rules out homomorphic lifts of $\mu$ from $\lambda$, but whether some *quasi-morphism* or filtered instanton invariant reproduces $\lambda \bmod 2$ with controlled defect remains open.

## 7. Current Research (as of June 2026)

- **Involutive and $Pin(2)$ Heegaard Floer (Hendricks–Manolescu–Zemke; Dai, Hom, Stoffregen, Truong; Princeton/Georgia Tech/Michigan State).** Refining the $\varphi_j$ homomorphisms and local-equivalence groups of $\iota$-complexes to enlarge the known summand. *(frontier — verify)* Recent work aims at showing the local equivalence group of $\iota$-complexes is torsion-free, which would rule out torsion detected by involutive theory.
- **Filtered instanton theory (Daemi, Nozaki, Sato, Taniguchi; Simons Center/RIKEN/Kyoto).** The $r_s$ and $\Gamma$ invariants exploit Chern–Simons filtration levels; used to show $\Theta^3_{\mathbb{Z}}$ is not generated by Seifert spaces and to bound homology-cobordism distance.
- **Equivariant Seiberg–Witten and Bauer–Furuta (Iida, Taniguchi, Lin).** Families and $S^1$-equivariant Bauer–Furuta invariants targeting torsion questions.
- **Singularity theory (Némethi and collaborators).** The Casson invariant conjecture for non-splice-quotient complete intersections, tied to the Seiberg–Witten invariant conjecture for normal surface singularities.
- **Homology concordance of knots in homology spheres (Dai–Hedden–Mallick–Stoffregen).** Satellite operators as a source of new independent families.

## 8. Future Work

- Build a homology cobordism invariant valued in a group with torsion — e.g. from equivariant stable homotopy with finite-cyclic symmetry, or a $\mathbb{Z}/n$-equivariant refinement of the Seiberg–Witten Floer spectrum — since every real-valued invariant is structurally blind to torsion.
- Determine whether the local equivalence group of $\iota$-complexes (or $Pin(2)$ SWF local equivalence) is torsion-free; this bounds what Floer theory can prove.
- Find a canonical lift $\tilde\lambda$ of $\mu$ that is a quasi-morphism with explicit defect, giving quantitative triangulation obstructions.
- Compute instanton and involutive invariants for hyperbolic homology spheres, e.g. surgeries on hyperbolic knots, to escape the Seifert/plumbing regime.
- Settle the Casson invariant conjecture for all complete intersection singularity links.

## 9. Key References

- **[Foundational]** S. Akbulut, J. McCarthy. *Casson's Invariant for Oriented Homology 3-Spheres: An Exposition.* Mathematical Notes 36, Princeton University Press, 1990.
- **[Foundational]** C. H. Taubes. *Casson's invariant and gauge theory.* Journal of Differential Geometry 31 (1990), 547–599.
- **[Foundational]** A. Floer. *An instanton-invariant for 3-manifolds.* Communications in Mathematical Physics 118 (1988), 215–240.
- **[Foundational]** R. Fintushel, R. Stern. *Pseudofree orbifolds.* Annals of Mathematics 122 (1985), 335–364.
- **[Foundational]** M. Furuta. *Homology cobordism group of homology 3-spheres.* Inventiones Mathematicae 100 (1990), 339–355.
- **[Foundational]** R. Fintushel, R. Stern. *Instanton homology of Seifert fibred homology three spheres.* Proceedings of the London Mathematical Society 61 (1990), 109–137.
- **[SOTA]** C. Manolescu. *Pin(2)-equivariant Seiberg–Witten Floer homology and the triangulation conjecture.* Journal of the American Mathematical Society 29 (2016), 147–176.
- **[SOTA]** I. Dai, J. Hom, M. Stoffregen, L. Truong. *An infinite-rank summand of the homology cobordism group.* Duke Mathematical Journal 172 (2023), 2365–2432.
- **[SOTA]** A. Daemi. *Chern–Simons functional and the homology cobordism group.* Duke Mathematical Journal 169 (2020), 2827–2886.
- **[SOTA]** Y. Nozaki, K. Sato, M. Taniguchi. *Filtered instanton Floer homology and the homology cobordism group.* Journal of the European Mathematical Society 25 (2023).
- **[SOTA]** M. Stoffregen. *Pin(2)-equivariant Seiberg–Witten Floer homology of Seifert fibrations.* Compositio Mathematica 156 (2020), 199–250.
- **[SOTA]** K. A. Frøyshov. *An inequality for the h-invariant in instanton Floer theory.* Topology 43 (2004), 407–432.
- **[Related]** W. Neumann, J. Wahl. *Casson invariant of links of singularities.* Commentarii Mathematici Helvetici 65 (1990), 58–78.
- **[Related]** A. Némethi, T. Okuma. *The Seiberg–Witten invariant conjecture for splice-quotients.* Journal of the London Mathematical Society 78 (2008), 143–154.
- **[Survey]** C. Manolescu. *Homology cobordism and triangulations.* Proceedings of the ICM 2018, Vol. II, 1175–1191.
- **[Survey]** N. Saveliev. *Invariants for Homology 3-Spheres.* Encyclopaedia of Mathematical Sciences 140, Springer, 2002.

## 10. Worked Example / Concrete Special Case

**Claim.** $\lambda$ does not descend to $\Theta^3_{\mathbb{Z}}$.

Let $K=T_{2,3}\\#\,\overline{T_{2,3}}$ be the square knot (trefoil connect-sum its mirror). Its Alexander polynomial is
$$\Delta_K(t)=\Delta_{T_{2,3}}(t)^2=\big(t-1+t^{-1}\big)^2 .$$
Write $g(t)=t-1+t^{-1}$, so $\Delta_K=g^2$. Then $g(1)=1$, $g'(t)=1-t^{-2}$ gives $g'(1)=0$, and $g''(t)=2t^{-3}$ gives $g''(1)=2$. Hence
$$\Delta_K''(1)=\big(g^2\big)''(1)=2g'(1)^2+2g(1)g''(1)=0+2\cdot1\cdot2=4 .$$
By the surgery formula with $n=1$,
$$\lambda\big(S^3_{+1}(K)\big)=\tfrac12\Delta_K''(1)=2 .$$

Now $K$ is slice: it is $J\\#\overline{J}$, so it bounds a smoothly embedded disk in $B^4$. Pushing the slice disk in and doing $+1$-surgery along it shows $\Sigma:=S^3_{+1}(K)$ bounds a compact smooth $\mathbb{Z}$-homology 4-ball. Therefore
$$[\Sigma]=0\in\Theta^3_{\mathbb{Z}},\qquad \lambda(\Sigma)=2\neq0=\lambda(S^3).$$

Consistency check with Section 2(3): $\lambda(\Sigma)=2\equiv0\pmod2$, so $\mu(\Sigma)=0$, as Rokhlin's theorem forces for anything bounding a homology ball. Casson's theorem still applies: $\lambda(\Sigma)\neq0$, so $\pi_1(\Sigma)$ has an irreducible $SU(2)$ representation and $\Sigma$ is not $S^3$ — a nontrivial homology sphere that is nevertheless trivial in $\Theta^3_{\mathbb{Z}}$.

**Contrast.** For $\Sigma(2,3,5)=S^3_{-1}(T_{2,3})$, $\lambda=-1$ is odd, so $\mu=1$ and $[\Sigma(2,3,5)]\neq0$. By Manolescu's theorem $2[\Sigma(2,3,5)]\neq0$ as well. This is the whole extent of what $\lambda$ contributes to $\Theta^3_{\mathbb{Z}}$: its parity, and nothing more — the gap of Section 6 in one line.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*