---
id: 02-algebra-group-theory/broue-michel-conjecture
title: "Broue-Michel Conjecture"
topic: 02-algebra-group-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Broué–Michel Conjecture

> **Topic:** Algebra & Group Theory · **ID:** `02-algebra-group-theory/broue-michel-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Let $\mathbf{G}$ be a connected reductive group over $\overline{\mathbb{F}_p}$ with Frobenius endomorphism $F$, finite group of Lie type $G = \mathbf{G}^F$, and Weyl group $W$. To each element $\mathbf{w}$ of the braid monoid $B^+(W)$ Deligne and Lusztig attach a variety $\mathbf{X}(\mathbf{w})$ carrying a $G$-action, hence a complex of $\ell$-adic cohomology $R\Gamma_c(\mathbf{X}(\mathbf{w}),\Lambda)$.

**Conjecture (Broué–Michel, 1997).** Let $d \ge 1$, let $w\phi$ be a $d$-regular element of $W\phi$ in Springer's sense, and let $\mathbf{w}$ be its canonical lift, so that $(\mathbf{w}\phi)^d = \boldsymbol{\pi}$, the full twist. Write $W(\zeta_d) = C_W(w\phi)$ for the relative Weyl group, $\mathbf{S}$ for a Sylow $\Phi_d$-torus, $\mathbf{L}=C_{\mathbf{G}}(\mathbf{S})$, $N = N_G(\mathbf{S})$. Then:

- **(BM1)** The centralizer braid group $C_{B(W)}(\mathbf{w}\phi) \cong B(W(\zeta_d))$ acts on $R\Gamma_c(\mathbf{X}(\mathbf{w}),\Lambda)$ in $D^b(\Lambda G)$, and this action factors through a **cyclotomic Hecke algebra** $\mathcal{H}(W(\zeta_d))$, giving $\operatorname{End}_{D^b(\Lambda G)}\big(R\Gamma_c(\mathbf{X}(\mathbf{w}),\Lambda)\big) \cong \mathcal{H}(W(\zeta_d))$.
- **(BM2)** (*Disjointness*) Over $\overline{\mathbb{Q}}_\ell$, $\operatorname{Hom}_{G}\big(H^i_c(\mathbf{X}(\mathbf{w})),H^j_c(\mathbf{X}(\mathbf{w}))\big)=0$ for $i\neq j$; equivalently the eigenvalues of $F^{\delta}$ separate the cohomology degrees.
- **(BM3)** (*Geometric form of Broué's conjecture*) If $\ell \mid \Phi_d(q)$ and $\ell \nmid |W|$, then $R\Gamma_c(\mathbf{Y}(\dot{\mathbf{w}}),\Lambda)b$ induces a **splendid Rickard equivalence** $D^b(\Lambda N b') \xrightarrow{\ \sim\ } D^b(\Lambda G b)$ between the principal blocks.

A complete solution means a proof (or a counterexample) valid for all $\mathbf{G}$, all $d$, and all $\ell \mid \Phi_d(q)$. Only fragments are known.

## 2. Mathematical Foundations

Fix a Borel $\mathbf{B}=\mathbf{T}\mathbf{U}$ and simple reflections $S \subset W = N_\mathbf{G}(\mathbf{T})/\mathbf{T}$. $F$ acts on $X(\mathbf{T})\otimes\mathbb{R}$ as $q\phi$ with $\phi$ of finite order $\delta$. The Deligne–Lusztig varieties are
$$\mathbf{X}(w)=\{g\mathbf{B}\in \mathbf{G}/\mathbf{B}\ :\ g^{-1}F(g)\in \mathbf{B}w\mathbf{B}\},\qquad \dim \mathbf{X}(w)=\ell(w),$$
$$\mathbf{Y}(\dot w)=\{g\mathbf{U}\ :\ g^{-1}F(g)\in \mathbf{U}\dot w\mathbf{U}\},$$
with $\mathbf{Y}(\dot w)\to\mathbf{X}(w)$ a $\mathbf{T}^{wF}$-torsor. The virtual character is $R_w^{\mathbf{G}}(\theta)=\sum_i (-1)^i H^i_c(\mathbf{Y}(\dot w),\overline{\mathbb{Q}}_\ell)_\theta$.

For a word $\mathbf{b}=\mathbf{s}_1\cdots\mathbf{s}_n$ in $B^+(W)$ one sets
$$\mathbf{X}(\mathbf{b})=\{(g_0\mathbf{B},\dots,g_n\mathbf{B}) : g_{i-1}^{-1}g_i\in \mathbf{B}s_i\mathbf{B},\ g_n=F(g_0)\},$$
which depends only on $\mathbf{b}$, not on the chosen word; $\mathbf{X}(\mathbf{b})\cong\mathbf{X}(w)$ when $\mathbf{b}$ is the lift of a reduced $w$.

**Regular elements (Springer).** $w\phi$ is $\zeta_d$-regular if it has an eigenvector in the complement of the reflection hyperplanes with eigenvalue $\zeta_d=e^{2\pi i/d}$. Then $W(\zeta_d)=C_W(w\phi)$ is a complex reflection group acting on the $\zeta_d$-eigenspace, and $|W(\zeta_d)|=\\#\{i : d \mid d_i\}$-many degrees survive: $W(\zeta_d)$ has degrees the $d_i$ divisible by $d$.

**Generic Sylow theory (Broué–Malle).** $|G| = q^{N}\prod_i(q^{d_i}-1)$ factors over cyclotomic polynomials; the Sylow $\Phi_d$-torus $\mathbf{S}$ is unique up to conjugacy, $\mathbf{L}=C_\mathbf{G}(\mathbf{S})$ is a $d$-split Levi, and
$$N_G(\mathbf{S})/\mathbf{L}^F \cong W(\zeta_d).$$

**Cyclotomic Hecke algebra.** For a complex reflection group $V$ with reflections of order $e_j$ in class $j$, $\mathcal{H}(V;\{u_{j,k}\})$ is the quotient of $\Lambda B(V)$ by $\prod_{k=0}^{e_j-1}(\mathbf{s}_j-u_{j,k})$; "cyclotomic" means the $u_{j,k}$ are specialized to $\zeta\, q^{m}$ for roots of unity $\zeta$ and rationals $m$. The BMR freeness statement — $\mathcal{H}$ is free of rank $|V|$ — is now a theorem (Etingof; Marin–Pfeiffer; Losev), removing one hypothesis from (BM1).

**Full twist.** $\boldsymbol{\pi}=(\mathbf{s}_1\cdots\mathbf{s}_n)^{h}$ generates the center of $B(W)$ for $W$ irreducible; $(\mathbf{w}\phi)^d=\boldsymbol{\pi}$ is the braid-theoretic shadow of $d$-regularity (Bessis–Digne–Michel).

## 3. History & State of the Art

- **1976.** Lusztig, *Coxeter orbits and eigenspaces of Frobenius*, computes $H^*_c(\mathbf{X}(c))$ completely for $c$ a Coxeter element: cohomology is disjoint and $F$-eigenvalues are pairwise distinct. This is the empirical seed of (BM2).
- **1989.** Broué–Michel prove that unions $\bigcup_t \mathcal{E}(G,st)$ of Lusztig series over $\ell$-elements $t\in C(s)$ are unions of $\ell$-blocks — the *Broué–Michel theorem*, the block-theoretic backdrop.
- **1990–1993.** Broué's abelian defect group conjecture (Astérisque 181–182); Broué–Malle generic Sylow theory (Math. Ann. 292, 1992); Broué–Malle–Michel, *Generic blocks of finite reductive groups* (Astérisque 212, 1993) organize unipotent characters into $d$-Harish-Chandra series indexed by $\operatorname{Irr}W(\zeta_d)$.
- **1997.** Broué–Michel state the conjectures above in *Sur certains éléments réguliers des groupes de Weyl et les variétés de Deligne–Lusztig associées*.
- **2003–2017.** Bonnafé–Rouquier prove Jordan decomposition as a derived equivalence (Publ. IHÉS 97); Digne–Michel–Rouquier settle the Coxeter case; Bonnafé–Dat–Rouquier (Ann. of Math. 185, 2017) reduce Broué's conjecture for finite reductive groups to quasi-isolated blocks.
- **SOTA.** (BM1) known for $d=1$, $d=h$ (Coxeter), and for many "good" $\mathbf{w}$ up to the braid relations; (BM2) known for Coxeter and low-rank checks; (BM3) known for cyclic defect and for the Coxeter/$\Phi_h$ case in large characteristic.

## 4. Partial Results / Verified Cases

- **Coxeter case $d=h$** ($\mathbf{w}=\mathbf{c}$, $W(\zeta_h)=\mathbb{Z}/h$): (BM1)+(BM2) proved for all $\mathbf{G}$ over $\overline{\mathbb{Q}}_\ell$ by Lusztig (1976) and, integrally, by Digne–Michel–Rouquier (*Adv. Math.* 209, 2007) and Bonnafé–Rouquier (*Nagoya Math. J.* 183, 2006). $H^*_c(\mathbf{X}(c))$ is torsion-free and $\operatorname{End} \cong \Lambda[F]/\prod(F-\lambda_i)$.
- **Brauer trees.** For $\ell \mid \Phi_h(q)$, $\ell \nmid |W|$, Dudas (*Adv. Math.* 229, 2012) and Dudas–Rouquier determined the Brauer trees of unipotent blocks of cyclic defect from $H^*_c(\mathbf{X}(c))$, confirming (BM3) in that range.
- **Cyclic defect / rank 1.** $\mathrm{SL}_2(q)$, $\mathrm{PGL}_2(q)$, $\mathrm{SU}_3(q)$, $^2G_2(q)$: (BM3) fully proved (Rouquier, LNM 1685, 1998).
- **$d=1$.** $\mathbf{X}(\boldsymbol{\pi})$-type statements reduce to ordinary Harish-Chandra theory and the Iwahori–Hecke algebra $\mathcal{H}(W,q)$: (BM1) is classical.
- **Braid-group action.** Digne–Michel (*Nagoya Math. J.* 183, 2006; *Adv. Math.* 257, 2014) construct the $B(W(\zeta_d))$-action on $R\Gamma_c(\mathbf{X}(\mathbf{w}),\Lambda)$ for all regular $\mathbf{w}$, using parabolic Deligne–Lusztig varieties; the *quotient* to $\mathcal{H}$ remains conjectural.
- **Low-rank verification.** $\mathrm{GL}_n(q)$ for $n\le 5$, $\mathrm{Sp}_4(q)$, $G_2(q)$, $^3D_4(q)$, $\mathrm{SU}_n(q)$ for small $n$: cohomology computed and the conjecture verified degree-by-degree (Digne–Michel–Rouquier; Dudas; Dudas–Malle; Craven).
- **Reduction.** Bonnafé–Dat–Rouquier reduce the block-theoretic content of (BM3) to quasi-isolated blocks of simple groups.

## 5. Principal Obstacles

- **No handle on higher-dimensional cohomology.** Beyond $\dim \mathbf{X}(\mathbf{w})=\ell(w)$ small or Coxeter, no method computes $H^i_c$ for all $i$. Lusztig's Coxeter argument uses that the $F$-eigenvalues force a filtration; for general $d$ the eigenvalue multiplicities collide.
- **Affineness is open.** Deligne–Lusztig proved $\mathbf{X}(w)$ affine when $\ell(w)$ exceeds a bound depending on $q$; He and Bonnafé–Rouquier extended this to minimal-length and good-position elements, but affineness (which would give concentration of $H^i_c$ in degrees $\ge \ell(w)$) is unknown in general. Without it, vanishing arguments fail.
- **Singular compactifications.** The natural compactifications $\overline{\mathbf{X}(\mathbf{b})}$ (Deligne–Lusztig, Bott–Samelson type) are singular; weight arguments give inequalities, not equalities.
- **Torsion.** $H^*_c(\mathbf{X}(\mathbf{w}),\mathbb{Z}_\ell)$ may have torsion; splendid Rickard equivalences require integral control, which the $\overline{\mathbb{Q}}_\ell$-level trace formula cannot supply.
- **Non-formality.** $R\Gamma_c$ is not known to split as $\bigoplus H^i_c[-i]$; disjointness (BM2) is exactly what would force formality, so (BM1) and (BM2) are entangled.
- **Hecke relations need eigenvalues.** Proving that the braid action factors through $\mathcal{H}$ requires knowing the Frobenius eigenvalues in advance — precisely the unknown.

## 6. The Gap

Proven: the *existence* of the braid group action (Digne–Michel) and the full picture for $d=h$ and for $\ell(w)\le 2$-type cases. Conjectured: that the action satisfies the degree-$e_j$ polynomial relations of a cyclotomic Hecke algebra, and that cohomology is disjoint.

The precise missing step: **for a $d$-regular $\mathbf{w}$ with $d\neq 1,h$, show that each braid generator $\sigma_j \in B(W(\zeta_d))$ acts on $R\Gamma_c(\mathbf{X}(\mathbf{w}),\Lambda)$ with $\prod_{k}(\sigma_j - \zeta^k q^{m_k}) = 0$**, i.e. that its eigenvalues on $H^*_c$ take exactly $e_j$ values. Equivalently, one must compute the $F^{\delta}$-eigenvalues on $H^*_c(\mathbf{X}(\mathbf{w}))$ — no general algorithm exists. Everything else (BM3 included, given Bonnafé–Dat–Rouquier's reduction) would follow by known machinery.

## 7. Current Research (as of June 2026)

- **Paris (Michel, Digne, Dudas, Broué)**: parabolic Deligne–Lusztig varieties and the "spetsial" framework; extending the $B(W(\zeta_d))$-action to non-regular roots of $\boldsymbol{\pi}$.
- **Bonn / MPIM and Kaiserslautern (Malle, Dudas–Malle)**: decomposition matrices for unipotent blocks used as a consistency test for conjectural cohomology tables.
- **UCLA / Bath (Rouquier, Craven)**: perverse equivalences as a combinatorial model that *predicts* the cohomology degrees; Craven's algorithm produces conjectural $H^*_c$ for rank $\le 4$ groups. *(frontier — verify)*
- **Integral $\ell$-adic methods**: Dudas' work on generic and unitriangular decomposition matrices, and torsion-freeness of $H^*_c$ for minimal-length elements. *(frontier — verify)*
- **Spetses**: Broué–Malle–Michel's *Split spetses for primitive reflection groups* (Astérisque 359, 2014) supplies the expected cyclotomic Hecke parameters for every $(W,d)$, so (BM1) has a fully explicit conjectural target.

## 8. Future Work

- Prove affineness of $\mathbf{X}(w)$ in general, or at least for regular $\mathbf{w}$; this would settle concentration and reduce (BM2) to a multiplicity count.
- Compute $H^*_c(\mathbf{X}(\mathbf{w}))$ for the next open case $d=h/2$ in exceptional types ($E_7$, $E_8$), where relative Weyl groups are $G_{31}$-type primitive groups.
- Establish (BM1) by exhibiting a *geometric* realization of the Hecke relation, e.g. a distinguished triangle from a $\mathbb{P}^1$-fibration on parabolic Deligne–Lusztig varieties (Digne–Michel's stated program).
- Combine Craven–Rouquier perverse equivalences with Bonnafé–Dat–Rouquier's reduction to obtain (BM3) for all quasi-isolated blocks.
- Extend to non-principal blocks and to $\ell \mid |W|$, where the defect group is non-abelian and the statement needs modification.

## 9. Key References

- **[Foundational]** M. Broué, J. Michel. *Blocs et séries de Lusztig dans les groupes réductifs finis.* J. reine angew. Math. **395** (1989), 56–67.
- **[Foundational]** M. Broué, J. Michel. *Sur certains éléments réguliers des groupes de Weyl et les variétés de Deligne–Lusztig associées.* In: Finite Reductive Groups: Related Structures and Representations (M. Cabanes, ed.), Progress in Math. 141, Birkhäuser, 1997, 73–139.
- **[Foundational]** P. Deligne, G. Lusztig. *Representations of reductive groups over finite fields.* Ann. of Math. (2) **103** (1976), 103–161.
- **[Foundational]** G. Lusztig. *Coxeter orbits and eigenspaces of Frobenius.* Invent. Math. **38** (1976/77), 101–159.
- **[Foundational]** M. Broué, G. Malle, J. Michel. *Generic blocks of finite reductive groups.* Astérisque **212** (1993), 7–92.
- **[Foundational]** M. Broué, G. Malle, R. Rouquier. *Complex reflection groups, braid groups, Hecke algebras.* J. reine angew. Math. **500** (1998), 127–190.
- **[SOTA]** F. Digne, J. Michel, R. Rouquier. *Cohomologie des variétés de Deligne–Lusztig.* Adv. Math. **209** (2007), 749–822.
- **[SOTA]** F. Digne, J. Michel. *Parabolic Deligne–Lusztig varieties.* Adv. Math. **257** (2014), 136–218.
- **[SOTA]** C. Bonnafé, J.-F. Dat, R. Rouquier. *Derived categories and Deligne–Lusztig varieties II.* Ann. of Math. (2) **185** (2017), 609–670.
- **[SOTA]** C. Bonnafé, R. Rouquier. *Coxeter orbits and modular representations.* Nagoya Math. J. **183** (2006), 1–34.
- **[SOTA]** O. Dudas. *Coxeter orbits and Brauer trees.* Adv. Math. **229** (2012), 3398–3435.
- **[SOTA]** D. Craven, R. Rouquier. *Perverse equivalences and Broué's conjecture.* Adv. Math. **248** (2013), 1–58.
- **[SOTA]** D. Bessis. *Finite complex reflection arrangements are $K(\pi,1)$.* Ann. of Math. (2) **181** (2015), 809–904.
- **[Survey]** M. Cabanes, M. Enguehard. *Representation Theory of Finite Reductive Groups.* Cambridge Univ. Press, New Math. Monographs 1, 2004.
- **[Survey]** F. Digne, J. Michel. *Representations of Finite Groups of Lie Type.* 2nd ed., LMS Student Texts 95, Cambridge Univ. Press, 2020.
- **[Survey]** M. Broué, G. Malle, J. Michel. *Split spetses for primitive reflection groups.* Astérisque **359** (2014).

## 10. Worked Example: $\mathbf{G}=\mathrm{SL}_2$, $d=2$

Take $\mathbf{G}=\mathrm{SL}_2$, $F$ the standard $q$-Frobenius, $G=\mathrm{SL}_2(q)$, $W=\{1,s\}$, $h=2$, $d=2$. Then $s$ is $\zeta_2$-regular, $\mathbf{s}^2=\boldsymbol{\pi}$, and $W(\zeta_2)=C_W(s)=\mathbb{Z}/2$. The Sylow $\Phi_2$-torus has $\mathbf{S}^F\cong\mu_{q+1}$, $\mathbf{L}=\mathbf{T}_w$, $N=N_G(\mathbf{T}_w)$ of order $2(q+1)$.

**The varieties.** $\mathbf{X}(s)=\mathbb{P}^1\setminus\mathbb{P}^1(\mathbb{F}_q)$ and $\mathbf{Y}(\dot s)$ is the *Drinfeld curve*
$$\mathbf{Y}(\dot s)=\{(x,y)\in\mathbb{A}^2 \ :\ xy^q-x^qy=1\},$$
with $\mu_{q+1}$ acting by scalars and $\mathbf{Y}\to\mathbf{X}$ the quotient.

**Cohomology.** $\chi_c(\mathbf{X}(s))=2-(q+1)=1-q$, and $H^i_c(\mathbf{X}(s),\overline{\mathbb{Q}}_\ell)=0$ for $i\ne 1,2$. Since $H^2_c=\overline{\mathbb{Q}}_\ell$ (trivial module, $F$ acting by $q$), $\dim H^1_c = q$, and it is the Steinberg module $\mathrm{St}$, with $F$ acting by $1$. For $\mathbf{Y}$: $\chi_c=(q+1)(1-q)=1-q^2$, $H^2_c=\overline{\mathbb{Q}}_\ell$, $\dim H^1_c=q^2$, decomposing over $\hat\mu_{q+1}$ as
$$H^1_c(\mathbf{Y})=\mathrm{St}\ \oplus\ \bigoplus_{\theta^2\ne 1}\pi_\theta\ \oplus\ (\pi_{\theta_0}^+\oplus\pi_{\theta_0}^-),$$
dimensions $q + (q-1)(q-1) + 2\cdot\tfrac{q-1}{2} = q^2$. ✓

**(BM2).** $H^1_c$ and $H^2_c$ share no constituent ($\mathrm{St}\ne \mathbf{1}$); the $F$-eigenvalues $1$ and $q$ are distinct. Disjointness holds.

**(BM1).** $\operatorname{End}_{D^b(\Lambda G)}(R\Gamma_c(\mathbf{X}(s),\Lambda))$ is generated by the Frobenius endomorphism $F$, which satisfies
$$(F-1)(F-q)=0,$$
i.e. it is the cyclotomic Hecke algebra $\mathcal{H}(\mathbb{Z}/2;\,u_0=1,\ u_1=q)$ of $W(\zeta_2)=\mathbb{Z}/2$ — exactly as predicted.

**(BM3).** Let $\ell$ be odd, $\ell\mid q+1$, $\ell\nmid q-1$, $\ell^a=(q+1)_\ell$. The principal block $b$ of $\Lambda G$ has cyclic defect group of order $\ell^a$ with $e=|W(\zeta_2)|=2$ edges: the Brauer tree is the line
$$\mathbf{1} \;-\!\!-\; \bullet_{\text{exc}} \;-\!\!-\; \mathrm{St},\qquad m=\frac{\ell^a-1}{2},$$
and the planar embedding is read off from the eigenvalues $1,q$. Rouquier showed $R\Gamma_c(\mathbf{Y}(\dot s),\Lambda)b$ induces a splendid Rickard equivalence $D^b(\Lambda N b')\simeq D^b(\Lambda G b)$. All three parts hold — the difficulty in general is that no analogue of these two dimension counts exists once $\dim\mathbf{X}(\mathbf{w})\ge 3$.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*