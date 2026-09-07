---
id: 03-geometry/halperin-carlsson-conjecture
title: "Halperin-Carlsson Conjecture"
topic: 03-geometry
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Halperin-Carlsson Conjecture

> **Topic:** Algebraic & Differential Geometry · **ID:** `03-geometry/halperin-carlsson-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

**Toral (Halperin) form.** Let $X$ be a finite-dimensional, paracompact space with $\dim_{\mathbb{Q}} H^*(X;\mathbb{Q}) < \infty$ (e.g. a finite CW complex or a closed manifold), and suppose the torus $T^r = (S^1)^r$ acts *almost freely* on $X$ — every isotropy subgroup is finite. Then
$$\dim_{\mathbb{Q}} H^*(X;\mathbb{Q}) \;=\; \sum_{i\ge 0}\dim_{\mathbb{Q}} H^i(X;\mathbb{Q}) \;\ge\; 2^r .$$

**Elementary abelian (Carlsson) form.** Let $G = (\mathbb{Z}/p)^r$ act freely and cellularly on a finite CW complex $X$. Then
$$\dim_{\mathbb{F}_p} H^*(X;\mathbb{F}_p) \;\ge\; 2^r .$$

Equivalently, in terms of the *toral rank* $\operatorname{rk}_0(X) := \max\{ r : T^r \text{ acts almost freely on } X\}$, the conjecture reads $\operatorname{rk}_0(X) \le \log_2 \dim_{\mathbb{Q}} H^*(X;\mathbb{Q})$. The bound $2^r$ is exactly attained by $X = T^r$ acting on itself, so it is sharp for every $r$.

A complete solution means either a proof valid for all $r$ and all finite-dimensional $X$ (resp. all primes $p$), or a single finite complex carrying an almost free $T^r$-action (resp. free $(\mathbb{Z}/p)^r$-action) with total Betti number $< 2^r$.

## 2. Mathematical Foundations

**Borel construction and equivariant cohomology.** For a $G$-space $X$ set $X_G = EG\times_G X$ and $H_G^*(X;k)=H^*(X_G;k)$, a module over $R:=H^*(BG;k)$. For $G=T^r$, $k=\mathbb{Q}$: $R=\mathbb{Q}[t_1,\dots,t_r]$, $|t_i|=2$. For $G=(\mathbb{Z}/p)^r$, $k=\mathbb{F}_p$: $R = \mathbb{F}_p[x_1,\dots,x_r]\otimes \Lambda(y_1,\dots,y_r)$ for $p$ odd, $R=\mathbb{F}_2[x_1,\dots,x_r]$ for $p=2$.

**Localization.** The action is almost free (resp. free) iff $H_G^*(X;k)$ is a *torsion* $R$-module of finite length, so $\dim_k H^*_G(X;k)<\infty$. The Serre spectral sequence of $X_G \to BG$ has $E_2 = H^*(BG)\otimes H^*(X)$ and must collapse the polynomial part entirely, which forces the differentials to consume all of $R$ — the source of the exponential lower bound.

**Minimal-model formulation (Halperin).** For $X$ nilpotent with minimal Sullivan model $(\Lambda V, d)$, an almost free $T^r$-action gives a *relative* model
$$\big(\mathbb{Q}[t_1,\dots,t_r]\otimes \Lambda V,\; D\big), \qquad D t_i = 0,\quad D v \equiv dv \ \ (\mathrm{mod}\ (t_1,\dots,t_r)),$$
with $\dim_{\mathbb{Q}} H^*(\mathbb{Q}[t]\otimes\Lambda V, D) < \infty$. The conjecture asserts $\dim H^*(\Lambda V,d)\ge 2^r$ for every such model.

**Free-module (Carlsson/algebraic) formulation.** Let $E = k[x_1,\dots,x_r]/(x_1^2,\dots,x_r^2)$ (an exterior algebra for $p=2$, or the group algebra $k[(\mathbb{Z}/p)^r]$ up to a filtration). A free $(\mathbb{Z}/p)^r$-action on $X$ makes $C_*(X)$ a finite free DG module over $k[G]$. The algebraic conjecture states: if $F$ is a finite free DG $E$-module (or a perfect complex over $k[x_1,\dots,x_r]$ with finite-length homology), then
$$\sum_i \dim_k H_i(F) \;\ge\; 2^r .$$
This is the exact homological cousin of the **Buchsbaum–Eisenbud–Horrocks rank conjecture**: for a finite-length module $M$ over a regular local ring of dimension $r$, $\sum_i \beta_i(M) \ge 2^r$.

**Toral rank of a nilmanifold.** For $N/\Gamma$ with nilpotent Lie algebra $\mathfrak{g}$, $\operatorname{rk}_0(N/\Gamma) = \dim \mathfrak{z}(\mathfrak{g})$, so the conjecture specializes to the purely Lie-algebraic statement $\dim H^*(\mathfrak{g};\mathbb{Q}) \ge 2^{\dim\mathfrak z(\mathfrak g)}$.

## 3. History & State of the Art (SOTA)

- **1980–1982.** Gunnar Carlsson, studying free $(\mathbb{Z}/p)^r$-actions on products of spheres, proved nonexistence results and formulated the rank conjecture in the $\mathbb{F}_p$ setting (*Amer. J. Math.* 1980; *Invent. Math.* 1982).
- **1985–1987.** Stephen Halperin, in "Rational homotopy and torus actions" (Durham symposium, LMS Lect. Notes 117), stated the toral rank conjecture in rational homotopy language and proved it for large classes of spaces. The two conjectures were recognized as the same phenomenon at $p=0$ and $p>0$; the combined statement is now standard as **Halperin–Carlsson**.
- **1986–1993.** Allday and Puppe developed the localization/Poincaré-series machinery, proved the conjecture for $r\le 3$, and codified the field in *Cohomological Methods in Transformation Groups* (CUP, 1993).
- **1988.** Adem–Browder settled the free-rank-of-symmetry problem for $(S^n)^k$: a free $(\mathbb{Z}/p)^r$-action forces $r\le k$, except possibly $p=2$, $n\in\{1,3,7\}$ (the case $n=1$ is classical; $n=3,7$ were closed later).
- **2011–2012.** Ustinovskiy proved the conjecture for **moment-angle complexes** $\mathcal{Z}_K$ and clarified its link to the Horrocks-type rank conjectures in commutative algebra.
- **2017.** Mark Walker proved the weak Buchsbaum–Eisenbud–Horrocks bound $\sum_i\beta_i(M)\ge 2^c$ for finite-length modules of codimension $c$ over regular local rings containing $\tfrac12$ (*Ann. of Math.* 186), the strongest evidence yet on the commutative-algebra side.
- **2018.** Iyengar–Walker (*Acta Math.* 221) constructed finite free **DG modules** over $k[x_1,\dots,x_r]$, $\operatorname{char} k \ne 2$, with total homology $< 2^r$ for $r \ge 8$ — refuting the naive DG/algebraic strengthening of the conjecture. Their complexes are not chain complexes of spaces, so the topological conjecture survives; but the "purely algebraic proof strategy" is dead.

Status: open for all $r\ge 4$, in both the rational and mod-$p$ forms.

## 4. Partial Results / Verified Cases

- **Small rank:** true for $r\le 3$ in both forms (Allday–Puppe; Carlsson for $(\mathbb{Z}/2)^3$ acting freely on finite complexes).
- **Even cohomology:** if $H^{\mathrm{odd}}(X;\mathbb{Q})=0$ then $\dim H^*(X;\mathbb{Q})\ge 2^r$ (Halperin) — here the Serre spectral sequence argument closes.
- **Elliptic spaces:** $\dim \pi_*(X)\otimes\mathbb{Q}<\infty$ and $\dim H^*(X;\mathbb{Q})<\infty$; then $\operatorname{rk}_0(X)=\dim\pi_{\text{odd}}\otimes\mathbb{Q} - \dim\pi_{\text{even}}\otimes\mathbb{Q}$ and the bound holds.
- **Products of spheres:** free $(\mathbb{Z}/p)^r$-action on $(S^{n_1}\times\cdots\times S^{n_k})$ forces $r \le k$, hence total Betti number $2^k\ge 2^r$ (Adem–Browder, with the exceptional $p=2$, $n\in\{1,3,7\}$ cases settled subsequently).
- **Moment-angle complexes / toric topology:** $\mathcal{Z}_K$ for any simplicial complex $K$ (Ustinovskiy).
- **Nilmanifolds:** verified for 2-step nilpotent Lie algebras with small-dimensional centre and, by classification, for $\mathfrak{g}$ of dimension $\le 7$; general nilpotent case open.
- **Free $T^r$-actions with $X/T^r$ formal**, two-stage spaces, and spaces whose model has $\dim V \le r+2$: known by explicit model computations.
- **Homogeneous spaces $G/H$:** $\operatorname{rk}_0(G/H)=\operatorname{rank} G-\operatorname{rank} H$ and $\dim H^*(G/H;\mathbb{Q})$ satisfies the bound directly.

## 5. Principal Obstacles

- **Spectral sequences lose multiplicativity.** The Serre spectral sequence of $X_G\to BG$ gives strong bounds only when differentials are forced by degree parity. For $r\ge 4$ the pattern of possible differentials on odd classes branches combinatorially, and additive bookkeeping yields only linear-in-$r$ bounds such as $\dim H^*(X)\ge 2r$ or $\ge 3r$, not $2^r$.
- **Localization is insensitive to total rank.** Localizing $H^*_G(X)$ at a prime ideal detects fixed sets, not Betti-number counts; there is no known localization statement whose output is exponential.
- **The algebraic model is false.** The most natural strategy — replace $C_*(X)$ by an arbitrary finite free DG $k[x_1,\dots,x_r]$-module and prove the bound in homological algebra — is refuted by Iyengar–Walker for $\operatorname{char} k\ne2$, $r\ge 8$. Any proof must use structure genuinely present in a cochain algebra (commutativity, Steenrod operations, cup-length constraints) that generic DG modules lack.
- **No Euler-characteristic or index-theoretic handle.** Almost free torus actions force $\chi(X)=0$, which is one linear relation, far weaker than an exponential bound.
- **Rational homotopy models grow.** In the relative model $(\mathbb{Q}[t]\otimes\Lambda V, D)$ the perturbed differential $D$ can be arbitrarily nonlinear in the $t_i$; controlling $\dim H^*(\Lambda V,d)$ from finiteness of $H^*(\mathbb{Q}[t]\otimes\Lambda V,D)$ is an inverse problem with no known normal form.

## 6. The Gap

Proven inputs give: (i) exponential bounds under parity or ellipticity hypotheses, (ii) exponential bounds for $r\le3$, (iii) the commutative-algebra analogue (Walker) for *modules*, i.e. for complexes concentrated in one homology degree. The general statement needs an exponential bound for **complexes with homology spread across many degrees and no parity restriction**. Concretely: the gap is to promote Walker's $2^c$ bound from resolutions of modules to the DG/topological setting while excluding the Iyengar–Walker counterexamples by a property that cochain algebras have and free DG modules do not. Best unconditional general bounds are polynomial or linear in $r$; the missing step is the passage from linear to exponential.

## 7. Current Research (as of June 2026)

- **Commutative-algebra side.** Continuation of Walker's Adams-operations / $K$-theoretic method (Nebraska–Lincoln, Utah) toward characteristic 2 and toward DG rings with extra structure. *(frontier — verify)*
- **Toric topology.** Extending Ustinovskiy's method from moment-angle complexes to polyhedral products and to quotients by general subtori (Moscow/HSE, Manchester, Fudan schools).
- **Rational homotopy.** Ongoing work on the conjecture for hyperelliptic and coformal spaces, and on Hilali-type inequalities relating $\dim H^*$ to $\dim\pi_*\otimes\mathbb{Q}$, which interact with the toral rank bound.
- **Nilpotent Lie algebras.** Computer-assisted verification for classified nilpotent Lie algebras in dimension $\le 9$ and structural results for filiform algebras. *(frontier — verify)*
- **Equivariant stable homotopy.** Attempts to reformulate the mod-$p$ conjecture as a bound on the rank of a $G$-equivariant module spectrum, using the Balmer spectrum of the stable module category.

## 8. Future Work

- Identify the extra structure (Steenrod/Dyer–Lashof operations, $E_\infty$-multiplicativity, or Poincaré duality) that separates cochain complexes of free $G$-spaces from the Iyengar–Walker DG modules, and build it into the bound.
- Settle $r=4$ in either form — the first genuinely open case — since existing $r\le3$ proofs are case analyses that visibly break at $r=4$.
- Prove the Buchsbaum–Eisenbud–Horrocks bound in characteristic 2, closing Walker's remaining case.
- Establish the nilmanifold case $\dim H^*(\mathfrak g)\ge 2^{\dim\mathfrak z(\mathfrak g)}$ in full; it is a self-contained Lie-algebra cohomology problem and would be the first infinite-rank-range confirmation.
- Test sharpness: search for finite complexes with almost free $T^r$-actions and total Betti number close to but above $2^r$ that are not products of tori; near-extremal examples would constrain any proof.

## 9. Key References

- **[Foundational]** S. Halperin. *Rational homotopy and torus actions.* In: Homotopy Theory (Durham 1985), London Math. Soc. Lecture Note Series 117, Cambridge University Press, 1987, pp. 293–306.
- **[Foundational]** G. Carlsson. *On the nonexistence of free actions of elementary abelian groups on products of spheres.* American Journal of Mathematics 102 (1980), 1147–1157.
- **[Foundational]** G. Carlsson. *On the rank of abelian groups acting freely on $(S^n)^k$.* Inventiones Mathematicae 69 (1982), 393–400.
- **[SOTA]** M. E. Walker. *Total Betti numbers of modules of finite projective dimension.* Annals of Mathematics 186 (2017), 641–646.
- **[SOTA]** S. B. Iyengar, M. E. Walker. *Examples of finite free complexes of small rank and small homology.* Acta Mathematica 221 (2018), 143–158.
- **[SOTA]** A. Adem, W. Browder. *The free rank of symmetry of $(S^n)^k$.* Inventiones Mathematicae 92 (1988), 431–440.
- **[SOTA]** Yu. M. Ustinovskiy. *Toral rank conjecture for moment-angle complexes.* Mathematical Notes 90 (2011), 279–283.
- **[Survey]** C. Allday, V. Puppe. *Cohomological Methods in Transformation Groups.* Cambridge Studies in Advanced Mathematics 32, Cambridge University Press, 1993.
- **[Survey]** Y. Félix, S. Halperin, J.-C. Thomas. *Rational Homotopy Theory.* Graduate Texts in Mathematics 205, Springer, 2001.
- **[Survey]** V. Puppe. *Multiplicative aspects of the Halperin–Carlsson conjecture.* Georgian Mathematical Journal 16 (2009), 369–379.

## 10. Worked Example / Concrete Special Case

**Case $r=1$, proved in full.** Let $S^1$ act almost freely on a finite complex $X$ with $\dim_{\mathbb{Q}}H^*(X;\mathbb{Q})<\infty$. Claim: $\dim_{\mathbb{Q}}H^*(X;\mathbb{Q})\ge 2$.

The Borel fibration $X\to X_{S^1}\to BS^1=\mathbb{C}P^\infty$ gives a Gysin sequence over $\mathbb{Q}$ with Euler class $t\in H^2(BS^1)$:
$$\cdots \to H^{n-2}_{S^1}(X)\xrightarrow{\;\cdot t\;} H^{n}_{S^1}(X)\to H^{n}(X)\to H^{n-1}_{S^1}(X)\xrightarrow{\;\cdot t\;}\cdots$$
Almost freeness $\Rightarrow$ $H^*_{S^1}(X;\mathbb{Q})\cong H^*(X/S^1;\mathbb{Q})$ is finite-dimensional, so multiplication by $t$ is nilpotent. If $\dim H^*(X;\mathbb{Q})=1$ then $X$ is $\mathbb{Q}$-acyclic ($H^0=\mathbb{Q}$, $H^{>0}=0$), so $H^*_{S^1}(X;\mathbb{Q})\cong H^*(BS^1;\mathbb{Q})=\mathbb{Q}[t]$, which is infinite-dimensional — contradiction. Hence $\dim H^*(X;\mathbb{Q})\ge 2 = 2^1$. Sharpness: $X=S^1$ acting on itself, $\dim H^*=2$.

**Model computation, $r=2$.** Take $X=T^2$ with minimal model $(\Lambda(v_1,v_2),d=0)$, $|v_i|=1$. The free $T^2$-action corresponds to the relative model
$$\big(\mathbb{Q}[t_1,t_2]\otimes\Lambda(v_1,v_2),\,D\big),\qquad Dv_1=t_1,\ Dv_2=t_2 .$$
Then $H^*(\mathbb{Q}[t_1,t_2]\otimes\Lambda(v_1,v_2),D)=\mathbb{Q}$ (Koszul complex on a regular sequence), finite-dimensional as required, and $\dim H^*(\Lambda(v_1,v_2),0)=4=2^2$: the bound is attained.

**Where the difficulty starts.** Replace $v_2$ by a degree-3 generator with $Dv_2 = t_1^2 + t_2\,\alpha$ for some $\alpha\in\Lambda V$. Finiteness of the Koszul-type homology no longer forces the $D$-image to be a regular sequence in $\mathbb{Q}[t_1,t_2]$; one must instead bound $\dim H^*(\Lambda V,d)$ from the *length* of the torsion module $H^*_{T^r}(X)$. For $r\ge4$ the possible perturbation patterns are not classifiable, which is precisely the obstruction described in Section 5.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*