---
id: 02-algebra-group-theory/bass-conjecture
title: "Bass Conjecture"
topic: 02-algebra-group-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Bass Conjecture

> **Topic:** Algebra & Group Theory · **ID:** `02-algebra-group-theory/bass-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Let $G$ be a discrete group and $R$ a commutative ring. For a finitely generated projective $RG$-module $P$, the **Hattori–Stallings rank** $r_P$ is an element of $HH_0(RG) = RG/[RG,RG]$, a free $R$-module on the set $[G]$ of conjugacy classes:

$$r_P \;=\; \sum_{[g]\in[G]} r_P(g)\,[g], \qquad r_P(g)\in R,$$

with only finitely many nonzero coefficients.

**Strong Bass Conjecture (SBC), integral form.** For every group $G$ and every finitely generated projective $\mathbb{Z}G$-module $P$,
$$r_P(g) = 0 \quad\text{for all } g \neq 1 .$$
Equivalently, $r_P = n\,[1]$ for some $n \in \mathbb{Z}_{\geq 0}$.

**Bass Conjecture over $\mathbb{C}G$ (BC).** For every finitely generated projective $\mathbb{C}G$-module $P$ (equivalently, every idempotent matrix $e \in M_n(\mathbb{C}G)$),
$$r_P(g) = 0 \quad\text{for all } g \in G \text{ of infinite order.}$$

The restriction to infinite order is necessary over $\mathbb{C}$: if $H \leq G$ is finite of order $m$, then $e = \tfrac{1}{m}\sum_{h \in H} h$ is idempotent and $r_e = \tfrac{1}{m}\sum_{h\in H}[h] \neq \tfrac1m[1]$ whenever $m>1$. Integrality is what makes the torsion coefficients vanish in the $\mathbb{Z}G$ statement.

A complete resolution requires either a proof valid for all discrete groups, or an explicit group $G$ together with an idempotent matrix over $\mathbb{C}G$ (resp. a projective $\mathbb{Z}G$-module) whose rank has a nonzero coefficient at a conjugacy class of an infinite-order (resp. nontrivial) element.

*Disambiguation:* "Bass conjecture" also names Bass's finite-generation conjecture for $K_n$ of finitely generated $\mathbb{Z}$-algebras. This page treats the trace/rank conjecture for group rings.

## 2. Mathematical Foundations

**Hattori–Stallings rank.** For $P$ f.g. projective over a ring $\Lambda$, choose $P \oplus Q \cong \Lambda^n$ and let $e \in M_n(\Lambda)$ be the corresponding idempotent. Define $r_P := \overline{\operatorname{tr}(e)} \in \Lambda/[\Lambda,\Lambda]$. This is independent of choices (Hattori 1965; Stallings 1965) and additive: $r_{P\oplus P'} = r_P + r_{P'}$, $r_{\Lambda} = \overline{1}$.

For $\Lambda = RG$ one has $RG/[RG,RG] \cong \bigoplus_{[g]\in[G]} R$, since $[RG,RG]$ is spanned by $xg x^{-1} - g$. Explicitly, for $e = (e_{ij})$ with $e_{ii} = \sum_{g} a^{(i)}_g g$,
$$r_P(g) \;=\; \sum_{i=1}^{n} \ \sum_{h \in [g]} a^{(i)}_{h}.$$

**Weak Bass Conjecture (WBC).** $r_P(1) = \operatorname{rk}_{\mathbb{Z}}\big(\mathbb{Z}\otimes_{\mathbb{Z}G} P\big)$, where $\mathbb{Z}$ carries the trivial action. SBC $\Rightarrow$ WBC. For $G$ of type $FP$ over $\mathbb{Z}$ with finite projective resolution $0\to P_k \to \dots \to P_0 \to \mathbb{Z}\to 0$, SBC implies $\sum_i (-1)^i r_{P_i} = \chi(G)\,[1]$, i.e. the "complete Euler characteristic" of Bass is concentrated at the identity class.

**Classical constraints on the identity coefficient.** Kaplansky: for $0 \neq e = e^2 \in \mathbb{C}G$, $r_e(1)$ is real and $0 < r_e(1) \le 1$, with equality only for $e=1$; the proof uses positivity of the canonical trace $\tau$ on the group von Neumann algebra $\mathcal{N}(G)$, since $r_e(1) = \tau(e)$. Zalesskii: $r_e(1) \in \mathbb{Q}$ for idempotents over $KG$ with $\operatorname{char}K = 0$.

**Cyclic-homology formulation (Burghelea).** There is a decomposition
$$HH_*(\mathbb{C}G) \;\cong\; \bigoplus_{[g]\in[G]} H_*\big(C_G(g);\mathbb{C}\big), \qquad
HC_*(\mathbb{C}G) \;\cong\; \Big(\bigoplus_{[g]\ \text{elliptic}} HC_*(\mathbb{C})\otimes H_*(C_G(g))\Big)\oplus\Big(\bigoplus_{[g]\ \text{hyperbolic}} H_*\big(C_G(g)/\langle g\rangle\big)\Big),$$
where *elliptic* means $g$ of finite order and *hyperbolic* means $g$ of infinite order. The rank $r_P$ is the degree-$0$ Chern character $\mathrm{ch}_0: K_0(\mathbb{C}G) \to HH_0(\mathbb{C}G)$, and BC is the vanishing of its hyperbolic components.

**Analytic formulation.** BC follows from surjectivity-type statements for assembly maps: the Baum–Connes assembly $\mu: K^G_0(\underline{E}G) \to K_0(C^*_r G)$ and the Bost assembly $\mu_{\ell^1}: K^G_0(\underline{E}G) \to K_0(\ell^1(G))$. Classes induced from finite subgroups have Hattori–Stallings ranks supported on torsion conjugacy classes; surjectivity of $\mu_{\ell^1}$ therefore forces vanishing at infinite-order elements.

## 3. History & State of the Art (SOTA)

- **1960.** Swan proves that for $G$ finite and $P$ f.g. projective over $\mathbb{Z}G$, $\mathbb{Q}\otimes P$ is free over $\mathbb{Q}G$ — the finite-group case of SBC.
- **1965.** Hattori and Stallings independently introduce the rank invariant.
- **1976.** Bass, *Euler characteristics and characters of discrete groups*, formulates the conjecture in the course of studying complete Euler characteristics, proves it for linear groups, and establishes the reduction machinery (induction, integrality, Galois descent over cyclotomic fields) still in use.
- **1985–1998.** The cyclic-homology attack: Marciniak, Eckmann, Ji, Emmanouil use Burghelea's decomposition and the nilpotency of Connes' periodicity operator $S$ to kill hyperbolic components under homological finiteness hypotheses on centralizers.
- **2002.** Lück relates Baum–Connes to the trace conjecture: BC$_{\mathrm{BC}}$ implies $\tau\big(K_0(C^*_rG)\big) = \Lambda^G$, the additive subgroup of $\mathbb{Q}$ generated by $1/|H|$ over finite subgroups $H \le G$.
- **2004.** Berrick, Chatterji and Mislin prove that the **Bost conjecture implies the Bass conjecture**, giving BC for all amenable groups (Bost is known there by Lafforgue's work) and, more generally, for a-T-menable groups.
- **2006.** Emmanouil's monograph consolidates the algebraic and analytic threads.

No counterexample is known, and no group has been identified as a plausible test case. The conjecture is regarded as true.

## 4. Partial Results / Verified Cases

| Class of groups | Status | Source |
|---|---|---|
| Finite groups | SBC proved | Swan (1960) |
| Linear groups (subgroups of $GL_n(F)$, $F$ a field) | SBC proved | Bass (1976) |
| Amenable groups | BC over $\mathbb{C}G$ proved | Berrick–Chatterji–Mislin (2004), via Lafforgue |
| a-T-menable (Haagerup) groups: free groups, $SL_2(\mathbb{R})$-lattices, Coxeter groups, groups acting properly on trees or CAT(0) cube complexes | BC proved | same, via Bost/Higson–Kasparov methods |
| Groups where $C_G(g)/\langle g\rangle$ has finite homological dimension over $\mathbb{Q}$ for every infinite-order $g$ | BC proved | Eckmann (1986), Marciniak (1986) |
| Groups of finite homological dimension; classes closed under directed unions and extensions built from these | proved | Emmanouil (1998) |
| Torsion-free groups with a finite-dimensional $BG$ and suitable centralizer control | WBC proved | Eckmann (1996) |
| Coefficient $r_P(1)$: rationality, and $0 < r_e(1) \le 1$ | theorem, all $G$ | Kaplansky (1969), Zalesskii (1972) |
| Torsion coefficients over $\mathbb{Z}G$ | controlled by integrality/Brauer-induction arguments; the residual difficulty is the hyperbolic part | Bass (1976) |

## 5. Principal Obstacles

- **No structure theory for general projective $\mathbb{C}G$-modules.** For infinite $G$ there is no classification of idempotents in $M_n(\mathbb{C}G)$; one only has traces. Every known proof therefore computes a trace through an external theory (representation theory, cyclic homology, or $K$-theory of a completion) rather than manipulating $e$ directly.
- **Cyclic homology stalls on infinite centralizers.** The hyperbolic summand $H_*\big(C_G(g)/\langle g\rangle\big)$ must be shown to receive no $\mathrm{ch}_0$-image. The available mechanism — nilpotency of Connes' $S$-operator, equivalently finite homological dimension of $C_G(g)/\langle g\rangle$ — fails badly when centralizers are large (e.g. groups with infinite torsion, Tarski monsters, Higman-type groups), and there is no substitute in infinite homological dimension.
- **Analytic transfer is lossy.** Passing from $\mathbb{C}G$ to $C^*_rG$ destroys the delocalized traces $\tau_g$, $g \neq 1$: they are unbounded and do not extend continuously to the reduced $C^*$-algebra. This forces the use of $\ell^1(G)$ and the Bost conjecture, but Bost is unknown precisely where Baum–Connes is hardest — property (T) groups, and groups without a proper action on a Hilbert space or a bolic space.
- **Assembly-map methods give only a one-sided statement.** BC needs surjectivity of the assembly map; the strongest general theorems (Yu, Kasparov–Skandalis, coarse embedding into Hilbert space) give injectivity/Novikov-type conclusions, which say nothing about $r_P(g)$.
- **Integrality does not reach the hyperbolic part.** Congruence and Galois-descent arguments that control coefficients at torsion elements over $\mathbb{Z}G$ have no analogue at infinite-order classes, where no finite-order symmetry acts on the coefficient.

## 6. The Gap

Everything proved rests on one of two hypotheses: (i) homological finiteness of $C_G(g)/\langle g\rangle$, or (ii) surjectivity of the Bost assembly map $\mu_{\ell^1}$. The gap is exactly the class of groups meeting neither: groups with infinite-dimensional centralizer quotients that also have property (T) or otherwise resist all known geometric proofs of Bost — random groups with property (T), Gromov monster groups, lattices in higher-rank $p$-adic Lie groups outside Lafforgue's reach, and groups of infinite homological dimension with exotic torsion. The single missing step is a **purely algebraic vanishing theorem for the delocalized trace**: a proof that $\tau_g(e) = 0$ for $g$ of infinite order and $e = e^2 \in M_n(\mathbb{C}G)$, using no geometry of $G$ and no finiteness of $BG$.

## 7. Current Research (as of June 2026)

- **Extending Bost/Baum–Connes.** Work on the Bost conjecture for groups acting on buildings, on higher-rank lattices, and via Banach-algebraic $KK$-theory (Lafforgue's school, Paris; Münster; Göttingen) directly widens the class of groups satisfying BC. Any new Bost theorem is automatically a new Bass theorem.
- **Delocalized traces and $\ell^1$-methods.** Refinements of relative/bounded cohomology and $\ell^1$-homology to produce trace-vanishing statements for hyperbolic conjugacy classes (Ji–Ogle–Ramsey-type $B$-bounded cohomology). *(frontier — verify)*
- **Interaction with the Atiyah and Kaplansky circles.** The failure of the strong Atiyah conjecture (Grigorchuk–Linnell–Schick–Żuk; Austin; Grabowski) sharpened attention to which trace-type conjectures survive; the Bass conjecture is the one with no known counterexample mechanism.
- **Homotopy-theoretic/assembly reformulations.** Berrick–Chatterji–Mislin's acyclic-group technique — embedding an arbitrary group into an acyclic group to trivialize obstruction classes — remains the most flexible algebraic device and is being reused in $K$-theoretic settings. *(frontier — verify)*

## 8. Future Work

1. Prove BC for one property (T) group not covered by Bost — e.g. a cocompact lattice in $Sp(n,1)$ — by an argument that isolates the delocalized trace rather than the whole assembly map.
2. Develop a version of the cyclic-homology argument that needs only finite *rational* homological dimension in degree $0$ of $C_G(g)/\langle g\rangle$, replacing global finiteness by a degreewise condition.
3. Settle SBC over $\mathbb{Z}G$ for all groups with torsion under the assumption of BC over $\mathbb{C}G$, making explicit the integrality input at elliptic classes.
4. Search computationally for anomalous idempotents in $\mathbb{C}G$ for candidate groups (Burnside-type quotients, Tarski monsters) using linear algebra over finitely supported subspaces — a negative search adds evidence, a positive one is a counterexample.
5. Clarify the exact implication chain BC $+$ trace conjecture $\Rightarrow$ Kaplansky idempotent conjecture for torsion-free groups, and whether the converse direction carries information.

## 9. Key References

- **[Foundational]** H. Bass. *Euler characteristics and characters of discrete groups.* Inventiones Mathematicae 35 (1976), 155–196. [DOI](https://doi.org/10.1007/bf01390137)
- **[Foundational]** A. Hattori. *Rank element of a projective module.* Nagoya Mathematical Journal 25 (1965), 113–120. [DOI](https://doi.org/10.1017/s002776300001148x)
- **[Foundational]** J. Stallings. *Centerless groups — an algebraic formulation of Gottlieb's theorem.* Topology 4 (1965), 129–134. [DOI](https://doi.org/10.1016/0040-9383(65)90060-1)
- **[Foundational]** R. G. Swan. *Induced representations and projective modules.* Annals of Mathematics 71 (1960), 552–578. [DOI](https://doi.org/10.2307/1969944)
- **[Foundational]** I. Kaplansky. *Fields and Rings.* University of Chicago Press, 1969.
- **[Classical]** A. E. Zalesskii. *On a problem of Kaplansky.* Soviet Mathematics Doklady 13 (1972), 449–452. [DOI](https://doi.org/10.1070/im1973v007n03abeh001952)
- **[Structural]** B. Eckmann. *Cyclic homology of groups and the Bass conjecture.* Commentarii Mathematici Helvetici 61 (1986), 193–202. [DOI](https://doi.org/10.1007/978-3-642-61708-9_64)
- **[Structural]** Z. Marciniak. *Cyclic homology and idempotents in group rings.* In: Transformation Groups (Poznań 1985), Lecture Notes in Mathematics 1217, Springer, 1986. [DOI](https://doi.org/10.1007/bfb0072827)
- **[Structural]** R. Ji. *Nilpotency of Connes' periodicity operator and the idempotent conjectures.* K-Theory 9 (1995), 59–76. [DOI](https://doi.org/10.1007/bf00965459)
- **[SOTA]** I. Emmanouil. *On a class of groups satisfying Bass' conjecture.* Inventiones Mathematicae 132 (1998), 307–330. [DOI](https://doi.org/10.1007/s002220050225)
- **[SOTA]** W. Lück. *The relation between the Baum–Connes conjecture and the trace conjecture.* Inventiones Mathematicae 149 (2002), 123–152. [DOI](https://doi.org/10.1007/s002220200215)
- **[SOTA]** A. J. Berrick, I. Chatterji, G. Mislin. *From acyclic groups to the Bass conjecture for amenable groups.* Mathematische Annalen 329 (2004), 597–621. [DOI](https://doi.org/10.1007/s00208-004-0521-6)
- **[Survey]** I. Emmanouil. *Idempotent Matrices over Complex Group Algebras.* Universitext, Springer, 2006. [DOI](https://doi.org/10.1007/3-540-27991-1)
- **[Survey]** W. Lück. *L²-Invariants: Theory and Applications to Geometry and K-Theory.* Ergebnisse der Mathematik 44, Springer, 2002.
- **[Survey]** B. Eckmann. *Projective and Hilbert modules over group algebras, and finitely dominated spaces.* Commentarii Mathematici Helvetici 71 (1996), 453–462. [DOI](https://doi.org/10.1007/bf02566430)

## 10. Worked Example / Concrete Special Case

**(a) $G = \mathbb{Z}/3 = \langle t \mid t^3 = 1\rangle$, over $\mathbb{C}$.** Put $e = \tfrac13(1 + t + t^2)$. Then $e^2 = \tfrac19(3 + 3t + 3t^2) = e$, so $e$ is an idempotent, and since $G$ is abelian each conjugacy class is a singleton:
$$r_e = \tfrac13[1] + \tfrac13[t] + \tfrac13[t^2].$$
The coefficients at $t, t^2 \neq 1$ are nonzero. This is not a counterexample: $t$ has finite order, and BC over $\mathbb{C}G$ asserts vanishing only at infinite-order elements. It shows why the naive statement "$r_P(g)=0$ for all $g\neq1$" cannot hold over $\mathbb{C}$.

**(b) The same group over $\mathbb{Z}$.** The idempotent above does not lie in $\mathbb{Z}G$: $\tfrac13 \notin \mathbb{Z}$. By Swan's theorem, for any f.g. projective $\mathbb{Z}[\mathbb{Z}/3]$-module $P$ the module $\mathbb{Q}\otimes P$ is free over $\mathbb{Q}[\mathbb{Z}/3]$, say of rank $n$. Ranks are computed after $\mathbb{Q}$-extension and are additive, so
$$r_P = r_{(\mathbb{Q}G)^n} = n[1], \qquad r_P(t) = r_P(t^2) = 0,$$
confirming SBC. Concretely, the projective ideal $I = (1-t)\mathbb{Z}G$ satisfies $\mathbb{Z}G \cong \mathbb{Z} \oplus I$ as $\mathbb{Z}G$-modules only after $\otimes\mathbb{Q}$; there $r_{\mathbb{Q}\otimes I} = 1\cdot[1] - r_{\mathbb{Q}} $, and the augmentation module $\mathbb{Q}$ contributes $\tfrac13([1]+[t]+[t^2])$ — the torsion coefficients cancel exactly because $\mathbb{Q}\otimes I \oplus \mathbb{Q} \cong \mathbb{Q}G$ and $\mathbb{Q}$ is not projective over $\mathbb{Z}G$.

**(c) $G = \mathbb{Z} = \langle t \rangle$, an infinite-order test.** $\mathbb{C}G = \mathbb{C}[t,t^{-1}]$ is an integral domain, so its only idempotents are $0$ and $1$; more generally $K_0(\mathbb{C}[t,t^{-1}]) = \mathbb{Z}$ by the Bass–Heller–Swan theorem, generated by the free module. Hence every f.g. projective module is free, $r_P = n[1]$, and $r_P(t^k) = 0$ for all $k \neq 0$. BC holds for $\mathbb{Z}$ — the smallest nontrivial instance of the hyperbolic vanishing that the general conjecture asserts for every infinite-order element of every group.

**(d) Why (c) is hard to scale.** For $G = F_2$ free of rank $2$ and $g$ a primitive word, no elementary argument computes $\tau_g(e)$; the known proof routes through the Haagerup property of $F_2$, the Bost assembly map, and Berrick–Chatterji–Mislin's theorem. Replacing $F_2$ by a property (T) group removes that route entirely, and the coefficient $r_e(g)$ becomes uncontrolled by any present technique.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*