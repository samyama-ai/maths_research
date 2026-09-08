---
id: 03-geometry/s-duality-conjecture
title: "S-Duality Conjecture"
topic: 03-geometry
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# S-Duality Conjecture (Vafa–Witten Modularity of Instanton Partition Functions)

> **Topic:** Algebraic & Differential Geometry · **ID:** `03-geometry/s-duality-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Let $X$ be a smooth closed oriented 4-manifold (in the algebro-geometric setting, a smooth complex projective surface with $b_1 = 0$). For a compact gauge group $G$ and fixed first Chern class $c_1$, form the generating function of Euler characteristics of moduli spaces $M_{c_1,c_2}$ of instantons (equivalently, of stable sheaves of rank $r$):

$$Z_{G,c_1}(\tau) \;=\; \sum_{c_2} \chi\big(M_{c_1,c_2}\big)\, q^{\,c_2 - \frac{r-1}{2r}c_1^2 - \frac{r\,\chi(X)}{24}}, \qquad q = e^{2\pi i \tau},\ \ \tau \in \mathbb{H}.$$

**Conjecture (Vafa–Witten, 1994).** $Z_{G,c_1}(\tau)$ is (the $q$-expansion of) a modular form of weight $-\tfrac{1}{2}\chi(X)$ for a congruence subgroup of $SL(2,\mathbb{Z})$ determined by $r$ and $c_1$, and the collection $\{Z_{G,c_1}\}$ is permuted by $SL(2,\mathbb{Z})$ in a way exchanging $G$ with its Langlands dual ${}^L G$. For $G = SU(2)$ versus $SO(3)$ the expected transformation is

$$Z_{SU(2)}(-1/\tau) \;=\; \pm\, 2^{-b_2(X)/2}\left(\frac{\tau}{2i}\right)^{-\chi(X)/2} \sum_{c_1 \in H^2(X;\mathbb{Z}/2)} Z_{SO(3),c_1}(\tau),$$

with $T:\tau \mapsto \tau+1$ acting on the $SO(3)$ sectors by the phase $e^{2\pi i (c_1^2/4 - \chi/24)}$ (conventions as in [Vafa–Witten 1994, §3–4]).

A complete resolution requires: (i) a definition of $\chi(M_{c_1,c_2})$ that is deformation-invariant and finite for all $c_2$ (the virtual Vafa–Witten invariant), and (ii) a proof of the modular transformation law for all $X$ in a stated class and all $r$. A disproof would exhibit a surface and rank for which the completed generating series is provably not modular of the predicted weight and level.

## 2. Mathematical Foundations

**Moduli.** Let $(X,H)$ be a polarized smooth projective surface, $\mathcal{M} = \mathcal{M}_H(r,c_1,c_2)$ the moduli space of Gieseker $H$-semistable torsion-free sheaves with Chern character $(r,c_1,c_2)$. Its expected dimension is
$$\operatorname{vd} = 2rc_2 - (r-1)c_1^2 - (r^2-1)\chi(\mathcal{O}_X).$$

**Vafa–Witten moduli space.** The relevant space is not $\mathcal{M}$ but the moduli of *Higgs pairs* $(E,\phi)$ with $\phi \in \operatorname{Hom}(E, E \otimes K_X)$, i.e. compactly supported sheaves on the total space of $K_X$:
$$\mathcal{N} = \mathcal{M}_H^{\,\perp}\big(\text{Tot}(K_X)\big),$$
which carries a symmetric obstruction-theory-like structure. Tanaka–Thomas define a $\mathbb{C}^*$-equivariant perfect obstruction theory of virtual dimension $0$ and set
$$\mathsf{VW}_{r,c_1,c_2}(X) \;=\; \int_{[\mathcal{N}^{\mathbb{C}^*}]^{\mathrm{vir}}} \frac{1}{e(N^{\mathrm{vir}})} \ \in \ \mathbb{Q},$$
localization being forced because $\mathcal{N}$ is noncompact. The fixed locus splits into the **instanton branch** ($\phi = 0$, giving $\mathcal{M}$ itself, contributing a signed virtual Euler characteristic $e^{\mathrm{vir}}(\mathcal{M})$ in the sense of Fantechi–Göttsche) and **monopole branches** (nilpotent $\phi$, supported on nested Hilbert schemes and Seiberg–Witten-type data).

**Modular objects.** With $\eta(\tau) = q^{1/24}\prod_{n\ge 1}(1-q^n)$, a holomorphic $f$ on $\mathbb{H}$ has weight $k$ for $\Gamma \le SL(2,\mathbb{Z})$ if $f\!\left(\frac{a\tau+b}{c\tau+d}\right) = (c\tau+d)^k f(\tau)$ for all $\begin{psmallmatrix} a & b \\ c & d\end{psmallmatrix} \in \Gamma$. **Mock modular forms** of weight $k$ are holomorphic $f$ admitting a shadow $g$ of weight $2-k$ such that $\hat f = f + g^*$ (with $g^*$ the non-holomorphic Eichler integral of $g$) transforms with weight $k$; these appear whenever $b_2^+(X) = 1$ or $p_g(X) = 0$, where wall-crossing and noncompactness of the space of anti-self-dual metrics break exact modularity.

**Refinement.** Replacing $\chi$ by $\chi_{-y}$ or by Poincaré/Hodge polynomials gives **refined** invariants $\mathsf{VW}(q,y)$, conjecturally Jacobi-like forms; the $y \to 1$ limit recovers the numerical case.

## 3. History & State of the Art (SOTA)

- **1977** — Montonen and Olive conjecture electric–magnetic duality of gauge theories with $G \leftrightarrow {}^L G$; Osborn (1979) notes $\mathcal{N}=4$ super-Yang–Mills as the natural home.
- **1994** — Vafa and Witten, *A strong coupling test of S-duality*, give the topologically twisted $\mathcal{N}=4$ theory on $X$ and the modularity prediction; they compute $K3$, $\mathbb{P}^2$, ALE spaces and rational elliptic surfaces at rank 2.
- **1990s** — Göttsche's formula for Hilbert schemes of points confirms the rank-1 case; Yoshioka, Klyachko and Göttsche compute rank-2 Betti numbers on rational and ruled surfaces, producing the predicted (mock) modular series.
- **2007** — Kapustin and Witten reinterpret S-duality as the geometric Langlands correspondence via compactification on a Riemann surface, relating Hitchin systems for $G$ and ${}^LG$.
- **2017–2020** — Tanaka and Thomas give the first mathematically rigorous definition of $\mathsf{VW}$ invariants for projective surfaces (stable and semistable cases), turning the physics prediction into a precise conjecture in algebraic geometry.
- **2019–2020** — Göttsche–Kool propose explicit closed formulas for rank 2 and 3 refined invariants in terms of Seiberg–Witten invariants and universal modular functions, verified in large ranges of $c_2$ by Segre/Nekrasov-style computations.

## 4. Partial Results / Verified Cases

- **Rank 1, all surfaces.** Göttsche's formula gives $\sum_n \chi(X^{[n]}) q^{n - \chi(X)/24} = \eta(\tau)^{-\chi(X)}$, exactly modular of weight $-\chi(X)/2$. The conjecture is a theorem here.
- **$K3$, rank 2.** Vafa–Witten's computation, made rigorous by Yoshioka's and Göttsche's Betti-number results and by Tanaka–Thomas for the virtual theory, yields a weight $-12$ form assembled from $\eta(\tau/2)^{-24}$, $\eta(2\tau)^{-24}$ and $\eta((\tau+1)/2)^{-24}$, matching the predicted $\Gamma_0(4)$-type transformation.
- **Minimal surfaces of general type, ranks 2 and 3.** Tanaka–Thomas and Laarakker compute all instanton and monopole contributions when $K_X$ has connected smooth canonical divisors; the answers agree with the Vafa–Witten/Dijkgraaf–Park–Schroers formulas expressed through Seiberg–Witten invariants.
- **$\mathbb{P}^2$ and Hirzebruch surfaces, ranks 2 and 3.** Klyachko, Yoshioka and Manschot compute the series; they are *mock* modular of the right weight, with shadow determined by wall-crossing — Bringmann–Manschot and Dabholkar–Putrov–Witten make the completion explicit.
- **Elliptic surfaces $E(n)$, rank 2.** Minahan–Nemeschansky–Vafa–Warner and later Göttsche–Kool verify modularity for $\pi: X \to \mathbb{P}^1$ elliptic with section.
- **Computational ranges.** Göttsche–Kool verify their rank-2 and rank-3 conjectural formulas for many surfaces with $p_g > 0$ up to $c_2$ of order $10$–$20$ using virtual localization on Quot/nested Hilbert schemes.
- **Hitchin-system shadow.** Hausel–Thaddeus (2003) prove $SL_n$/$PGL_n$ Hitchin systems on a curve are SYZ-mirror partners for $n=2,3$; Donagi–Pantev (2012) prove the duality of Hitchin systems for general reductive $G$ — the dimensional reduction of S-duality.

## 5. Principal Obstacles

- **Noncompactness.** $\mathcal{N}$ (Higgs pairs on $K_X$) is noncompact, so the invariant exists only via $\mathbb{C}^*$-localization; there is no compact virtual class whose deformation invariance would immediately give modularity.
- **Strictly semistable sheaves.** For $c_1$ not coprime to $r$, $\mathcal{M}$ has singular strictly semistable loci; defining the invariant needs Joyce–Song-style stack-theoretic or Mochizuki-style corrections, and the correct generating function is only conjectural.
- **Wall-crossing.** For $b_2^+(X)=1$ the moduli space depends on the polarization $H$; the resulting metaplectic anomaly turns exact modularity into mock modularity, and the shadow must be computed independently. No general framework produces the shadow from geometry alone.
- **Modularity is not local.** Every known proof technique (localization, wall-crossing, universality) produces the coefficients $\mathsf{VW}_{r,c_1,c_2}$ one $c_2$ at a time. Modularity is a statement about the *whole* series; there is no geometric operation on $\mathcal{M}$ implementing $\tau \mapsto -1/\tau$.
- **No known geometric realization of $S$.** Unlike wall-crossing (Kontsevich–Soibelman, Joyce–Song) which is now algebraic, the $SL(2,\mathbb{Z})$ action has no established derived-categorical or motivic incarnation on $D^b(\text{Tot}(K_X))$.
- **Rank growth.** Monopole contributions proliferate combinatorially with $r$ (partitions of $r$ indexing nested Hilbert schemes); explicit formulas exist only for $r \le 5$ in special cases.

## 6. The Gap

Proven: rank 1 for all $X$; ranks 2–3 for restricted classes (minimal general type with nice canonical divisor, $K3$, elliptic, toric/rational surfaces), and only as *verification* of a closed formula that happens to be modular, not as a derivation of modularity. Conjectured: a uniform statement for all $r$ and all $X$.

The precise barrier: one must produce a structural reason — not a case-by-case computation — for why $\sum_{c_2} \mathsf{VW}_{r,c_1,c_2} q^{c_2 - \cdots}$ lies in a finite-dimensional space of (mock) modular forms of weight $-\chi(X)/2$. Equivalently: find a geometric or categorical symmetry of the moduli problem realizing $S: \tau \mapsto -1/\tau$ and exchanging rank with degree data, and control the semistable/wall-crossing corrections uniformly in $r$.

## 7. Current Research (as of June 2026)

- **Tanaka–Thomas / Thomas school (Imperial College London).** Extending virtual VW invariants beyond the stable case; Thomas's $K$-theoretic refinement and its conjectural Jacobi-form structure.
- **Göttsche–Kool–Laarakker (ICTP, Utrecht).** Universal formulas for refined and $K$-theoretic invariants in ranks 2–5 via Segre and Verlinde series; the *Segre–Verlinde correspondence* is a modular-flavoured duality now proven in several cases. *(frontier — verify)*
- **Feyzbakhsh–Thomas.** Bridgeland-stability wall-crossing relating rank-$r$ sheaf counts to Pandharipande–Thomas / Gopakumar–Vafa invariants — the first technique that moves *between* ranks, and the most promising route to an inductive proof of modularity. *(frontier — verify)*
- **Mock modularity school (Manschot, Dabholkar, Pioline, Alexandrov).** Indefinite theta functions and holomorphic anomaly equations governing the non-modular completion for $b_2^+ = 1$; higher-depth mock modularity for $r \ge 3$.
- **Geometric Langlands side (Ben-Zvi, Gaitsgory, Nadler, Donagi–Pantev).** With the categorical geometric Langlands equivalence announced for de Rham setting, attention shifts to whether the 4-dimensional S-duality statement can be recovered from a categorified 2-dimensional one. *(frontier — verify)*

## 8. Future Work

- Prove modularity for rank 2 on *all* surfaces with $p_g > 0$ by combining Mochizuki's wall-crossing formula with the Seiberg–Witten expressions — regarded as the nearest fully attainable target.
- Develop a motivic/categorical $SL(2,\mathbb{Z})$ action on $D^b(\mathrm{Tot}(K_X))$, possibly through Bridgeland stability on the local surface, giving $S$ a geometric meaning.
- Establish the higher-depth mock modularity of $\mathbb{P}^2$ series for all ranks $r$, generalizing Bringmann–Manschot beyond $r=3$.
- Formulate and prove the orbifold/stacky and open (with boundary/surface-defect) versions to test the framework in more computable settings.
- Connect the refined invariants to vertex-algebra characters (W-algebras, Vertex Operator Algebras attached to 4-manifolds), where modularity would follow from Zhu-type theorems rather than by computation.

## 9. Key References

- **[Foundational]** C. Montonen, D. Olive. *Magnetic Monopoles as Gauge Particles?* Physics Letters B 72(1), 117–120, 1977. [DOI](https://doi.org/10.1016/0370-2693(77)90076-4)
- **[Foundational]** C. Vafa, E. Witten. *A Strong Coupling Test of S-Duality.* Nuclear Physics B 431, 3–77, 1994. (arXiv:hep-th/9408074). [DOI](https://doi.org/10.1016/0550-3213(94)90097-3)
- **[Foundational]** L. Göttsche. *The Betti Numbers of the Hilbert Scheme of Points on a Smooth Projective Surface.* Mathematische Annalen 286, 193–207, 1990. [DOI](https://doi.org/10.1007/bf01453572)
- **[SOTA]** Y. Tanaka, R. P. Thomas. *Vafa–Witten Invariants for Projective Surfaces I: Stable Case.* Journal of Algebraic Geometry 29, 603–668, 2020. [DOI](https://doi.org/10.1090/jag/738)
- **[SOTA]** Y. Tanaka, R. P. Thomas. *Vafa–Witten Invariants for Projective Surfaces II: Semistable Case.* Pure and Applied Mathematics Quarterly 13(3), 517–562, 2017. [DOI](https://doi.org/10.4310/pamq.2017.v13.n3.a6)
- **[SOTA]** L. Göttsche, M. Kool. *Virtual Refinements of the Vafa–Witten Formula.* Communications in Mathematical Physics 376, 1–49, 2020. [DOI](https://doi.org/10.1007/s00220-020-03748-7)
- **[SOTA]** T. Laarakker. *Monopole Contributions to Refined Vafa–Witten Invariants.* Geometry & Topology 24(6), 2781–2828, 2020. [DOI](https://doi.org/10.2140/gt.2020.24.2781)
- **[Related]** A. Kapustin, E. Witten. *Electric-Magnetic Duality and the Geometric Langlands Program.* Communications in Number Theory and Physics 1(1), 1–236, 2007. [DOI](https://doi.org/10.4310/cntp.2007.v1.n1.a1)
- **[Related]** T. Hausel, M. Thaddeus. *Mirror Symmetry, Langlands Duality, and the Hitchin System.* Inventiones Mathematicae 153, 197–229, 2003. [DOI](https://doi.org/10.1007/s00222-003-0286-7)
- **[Related]** R. Donagi, T. Pantev. *Langlands Duality for Hitchin Systems.* Inventiones Mathematicae 189, 653–735, 2012. [DOI](https://doi.org/10.1007/s00222-012-0373-8)
- **[Mock modularity]** K. Bringmann, J. Manschot. *From Sheaves on $\mathbb{P}^2$ to a Generalization of the Rademacher Expansion.* American Journal of Mathematics 133(4), 1039–1065, 2011.
- **[Mock modularity]** A. Dabholkar, P. Putrov, E. Witten. *Duality and Mock Modularity.* SciPost Physics 9, 072, 2020. [DOI](https://doi.org/10.21468/scipostphys.9.5.072)
- **[Survey]** R. P. Thomas. *Equivariant K-theory and Refined Vafa–Witten Invariants.* Communications in Mathematical Physics 378, 1451–1500, 2020. [DOI](https://doi.org/10.1007/s00220-020-03821-1)
- **[Survey]** K. Yoshioka. *The Betti Numbers of the Moduli Space of Stable Sheaves of Rank 2 on a Ruled Surface.* Mathematische Annalen 302, 519–540, 1995. [DOI](https://doi.org/10.1007/bf01444506)

## 10. Worked Example / Concrete Special Case

**Rank 1 on a $K3$ surface.** Take $X$ a $K3$ surface, $r=1$, $c_1 = 0$. A rank-1 torsion-free sheaf with trivial determinant is $I_Z$ for a length-$n$ subscheme $Z$, so $\mathcal{M}_{0,n} \cong X^{[n]}$, the Hilbert scheme of $n$ points, smooth of dimension $2n$. Göttsche's formula gives
$$\sum_{n\ge 0} \chi(X^{[n]})\, q^n \;=\; \prod_{m \ge 1} (1-q^m)^{-\chi(X)} \;=\; \prod_{m\ge1}(1-q^m)^{-24}.$$

Insert the Vafa–Witten normalization $q^{\,n - \chi(X)/24} = q^{\,n-1}$:
$$Z_{1,0}(\tau) \;=\; q^{-1}\prod_{m\ge1}(1-q^m)^{-24} \;=\; \frac{1}{\eta(\tau)^{24}} \;=\; \frac{1}{\Delta(\tau)}.$$

Check the first coefficients: $\chi(X^{[0]})=1$, $\chi(X^{[1]}) = \chi(K3) = 24$, $\chi(X^{[2]}) = 324$, and indeed
$$\frac{1}{\Delta(\tau)} = q^{-1} + 24 + 324\,q + 3200\,q^2 + \cdots.$$

Now verify the predicted weight. Since $\eta(-1/\tau) = \sqrt{-i\tau}\ \eta(\tau)$,
$$Z_{1,0}(-1/\tau) = \eta(-1/\tau)^{-24} = (-i\tau)^{-12}\eta(\tau)^{-24} = \left(\frac{\tau}{i}\right)^{-12} Z_{1,0}(\tau),$$
so $Z_{1,0}$ is modular of weight $-12$ for the full $SL(2,\mathbb{Z})$. The conjecture predicts weight $-\chi(X)/2 = -24/2 = -12$. Exact match, with $\Gamma = SL(2,\mathbb{Z})$ as expected since $U(1)$ is self-dual and $c_1=0$ gives no level structure.

**What breaks at rank 2.** Repeating the computation for $r=2$, $c_1=0$ on $K3$, $\mathcal{M}_{0,c_2}$ contains strictly semistable sheaves ($E = I_{Z_1} \oplus I_{Z_2}$), so $\chi$ must be replaced by a virtual/stack-theoretic count; the resulting series is no longer a single $\eta$-power but a $\Gamma_0(4)$-combination of $\eta(\tau/2)^{-24}$, $\eta(2\tau)^{-24}$, $\eta((\tau+1)/2)^{-24}$, and the $SU(2) \leftrightarrow SO(3)$ exchange is needed to close the $SL(2,\mathbb{Z})$ orbit. This is precisely where the general proof stops.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*