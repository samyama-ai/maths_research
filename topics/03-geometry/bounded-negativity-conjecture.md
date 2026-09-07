---
id: 03-geometry/bounded-negativity-conjecture
title: "Bounded Negativity Conjecture"
topic: 03-geometry
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Bounded Negativity Conjecture

> **Topic:** Algebraic & Differential Geometry · **ID:** `03-geometry/bounded-negativity-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

**Conjecture (Bounded Negativity, BNC).** Let $X$ be a smooth projective surface over an algebraically closed field of characteristic $0$. Then there is a constant $b(X) \geq 0$ such that
$$C^2 \geq -b(X)$$
for every **reduced** curve $C \subset X$.

The constant may depend on $X$ but not on $C$. Equivalently: the self-intersection numbers of reduced curves on a fixed surface are bounded below.

A complete proof must produce, for every such $X$, an effective or non-effective bound $b(X)$. A disproof must exhibit a single characteristic-$0$ surface $X$ and a sequence of reduced curves $C_n \subset X$ with $C_n^2 \to -\infty$. Two caveats fix the scope:

- **Reduced is essential.** For any curve $D$ with $D^2 > 0$, $(mD)^2 = m^2 D^2 \to +\infty$; for $D^2 < 0$ it tends to $-\infty$. Multiplicities must be excluded.
- **Characteristic $0$ is essential.** The statement is *false* in characteristic $p > 0$ (Section 10).

The variant restricted to *irreducible* reduced curves is formally weaker; it is also open, and no reduction of the reduced case to the irreducible case is known in general, because cross terms $C_i \cdot C_j$ in $C = \sum C_i$ can absorb arbitrarily negative diagonal contributions.

## 2. Mathematical Foundations

Let $X$ be a smooth projective surface over $k = \bar{k}$. The **Néron–Severi group** $\mathrm{NS}(X) = \mathrm{Pic}(X)/\!\equiv$ is a finitely generated abelian group of rank $\rho(X)$, the Picard number. The intersection form
$$\mathrm{NS}(X) \times \mathrm{NS}(X) \to \mathbb{Z}, \qquad (D, D') \mapsto D \cdot D'$$
is a nondegenerate symmetric bilinear form of signature $(1, \rho(X) - 1)$ by the **Hodge Index Theorem**. Negative self-intersection is therefore generic in the lattice; the content of BNC is that *effective, reduced* classes cannot realize arbitrarily negative values.

**Adjunction.** For a reduced irreducible curve $C \subset X$ with arithmetic genus $p_a(C)$,
$$C^2 = 2p_a(C) - 2 - K_X \cdot C .$$
So BNC is equivalent to the upper bound $K_X \cdot C \leq 2p_a(C) - 2 + b(X)$ for all reduced irreducible $C$: the canonical degree of a curve must not exceed its genus by more than a fixed amount.

**Blow-ups and Harbourne constants.** BNC is not known to be stable under blowing up. Let $f : Y \to X$ be the blow-up at $s$ distinct points with exceptional divisors $E_1,\dots,E_s$; for $C \subset X$ reduced of multiplicity $m_i$ at $p_i$, the strict transform satisfies
$$\tilde{C}^2 = C^2 - \sum_{i=1}^{s} m_i^2 .$$
Bauer–Harbourne–Knutsen–Küronya–Müller-Stach–Roulleau–Szemberg (Duke, 2013) encode this by the **global Harbourne constant**
$$H(X) \;=\; \inf_{f, C} \frac{\tilde{C}^2}{s},$$
the infimum over all blow-ups $f$ at $s \geq 1$ distinct points and all reduced curves $C \subset X$. Then BNC holds for *all* blow-ups of $X$ if and only if $H(X) > -\infty$. Restricting $C$ to line arrangements in $X = \mathbb{P}^2$ gives the **linear Harbourne constant** $H_L(\mathbb{P}^2)$; for an arrangement of $d$ lines with singular points of multiplicities $m_1,\dots,m_s$,
$$H_L(\text{arrangement}) = \frac{d^2 - \sum_i m_i^2}{s}.$$

**The main external input** is the logarithmic Bogomolov–Miyaoka–Yau inequality (Miyaoka 1984, Sakai 1980): for a reduced curve $C$ on $X$ with $K_X + C$ big and nef and mild singularities,
$$(K_X + C)^2 \leq 3\, e(X \setminus C),$$
where $e$ is the topological Euler number. Applied to line arrangements this yields **Hirzebruch's inequality**: for $d$ lines in $\mathbb{P}^2$ with $t_r$ points of multiplicity $r$ and $t_d = t_{d-1} = 0$,
$$t_2 + \tfrac{3}{4}\, t_3 \;\geq\; d + \sum_{r \geq 5} (2r - 9)\, t_r .$$

## 3. History & State of the Art (SOTA)

The problem is classically attributed to **Federigo Enriques**, who asked whether the self-intersections of irreducible curves on a fixed surface are bounded below; it circulated as folklore through the Italian school and appears in this form in Harbourne's lecture notes. The modern name and formulation are due to **Brian Harbourne**, who publicized it in connection with Seshadri constants, symbolic powers, and the SHGH conjecture on linear systems of plane curves with imposed multiplicities.

Milestones:

- **1960** — Nagata's conjecture on plane curves through $n \geq 10$ very general points, later recognized as implying BNC for the corresponding blow-ups.
- **1980–1984** — Sakai's and Miyaoka's logarithmic BMY inequalities supply the only general-purpose tool that bounds negativity of curve configurations.
- **1983** — Hirzebruch's inequality for complex line arrangements, later the engine behind all Harbourne-constant bounds.
- **2009–2012** — the problem is placed at the center of the "primer on Seshadri constants" and the Impanga survey *Recent developments and open problems in linear series*, which lists BNC as a principal open problem.
- **2013** — the Duke paper *Negative curves on algebraic surfaces* introduces $H$-constants, reducing BNC-for-all-blow-ups to a single numerical invariant per surface, and proving the first uniform bounds.
- **2015** — $H_L(\mathbb{P}^2) \geq -4$ for arbitrary complex line arrangements (IMRN); $\geq -3$ for real arrangements.
- **2017** — Roulleau extends Miyaoka–Sakai methods to configurations of elliptic curves on abelian and other surfaces.

**SOTA summary.** BNC is proved for large structured classes (Section 4), is known to fail in positive characteristic, and is *open* already for the blow-up of $\mathbb{P}^2$ at $n \geq 10$ very general points and for arbitrary minimal surfaces of general type. Best known bracket for the linear Harbourne constant of the plane: $-4 \leq H_L(\mathbb{P}^2) \leq -9/4$.

## 4. Partial Results / Verified Cases

BNC is a theorem in the following cases.

1. **$\rho(X) = 1$.** If $H$ generates $\mathrm{NS}(X)_{\mathbb{Q}}$ with $H^2 > 0$, every effective $C \equiv aH$ has $a > 0$, so $C^2 = a^2 H^2 > 0$. Bound: $b(X) = 0$.
2. **$-K_X$ is $\mathbb{Q}$-effective.** Write $-K_X \equiv_{\mathbb{Q}} D = \sum a_j D_j$, $a_j > 0$. For irreducible $C \not\subset \mathrm{Supp}(D)$, $K_X \cdot C \leq 0$, so adjunction gives $C^2 \geq -2$. The finitely many components $D_j$ contribute a finite maximum. Covers del Pezzo surfaces, all blow-ups of $\mathbb{P}^2$ at $n \leq 9$ points in *any* position (a cubic passes through any $9$ points), and anticanonical rational surfaces.
3. **$K_X \equiv 0$.** K3, Enriques, abelian, and bielliptic surfaces: $C^2 = 2p_a(C) - 2 \geq -2$, so $b(X) = 2$. On abelian surfaces $C^2 \geq 0$.
4. **Ruled and toric surfaces.** For $X = \mathbb{P}(E) \to B$ the negative sections have $C^2 = -e(E)$, fixed; fibers have $C^2 = 0$. Toric surfaces have finitely many torus-invariant curves and $-K_X$ effective.
5. **Mori dream surfaces** (finitely generated Cox ring). The effective cone is rational polyhedral, every irreducible curve with $C^2 < 0$ is an extremal ray generator, and there are finitely many; $b(X)$ is the maximum over that finite list.
6. **Line arrangements in $\mathbb{P}^2$, uniformly.** For any arrangement of $d \geq 2$ complex lines with $s$ singular points, $d^2 - \sum m_i^2 \geq -4s$; for real arrangements, $\geq -3s$ (BdRHHLPS, IMRN 2015). Hence blow-ups of $\mathbb{P}^2$ at singular loci of line arrangements satisfy a uniform bound.
7. **Elliptic-curve configurations** on surfaces with $K_X$ nef and $c_1^2 \le 3c_2$: Roulleau (IMRN 2017) obtains bounds of Harbourne type via Miyaoka–Sakai.
8. **Conditional case.** SHGH (Segre–Harbourne–Gimigliano–Hirschowitz) implies that on $X_n = \mathrm{Bl}_n \mathbb{P}^2$ at $n \geq 10$ very general points every irreducible curve with $C^2 < 0$ is a $(-1)$-curve, so $b(X_n) = 1$ (with $b = 1$ for irreducible curves).

## 5. Principal Obstacles

- **No structure theory for negative curves on general-type surfaces.** For $K_X$ nef and big, adjunction reads $C^2 = 2p_a(C) - 2 - K_X \cdot C$ with $K_X \cdot C > 0$; nothing prevents $K_X \cdot C$ from outgrowing $2p_a(C)$. Every known proof works by making $K_X \cdot C \leq 0$ (case 2 above) or by fixing a finite list of curves (cases 1, 5). Neither survives on a surface with infinite effective cone and positive canonical class.
- **Instability under blow-up.** BNC for $X$ says nothing about $\mathrm{Bl}_s X$: the drop $\tilde{C}^2 = C^2 - \sum m_i^2$ is unbounded unless one bounds multiplicities against the number of points. This is exactly the unsolved content of $H(X) > -\infty$.
- **Characteristic $0$ is used only globally.** The Frobenius counterexample (Section 10) shows that any proof must invoke a genuinely characteristic-$0$ input — Hodge theory, BMY, or transcendental methods. Purely lattice-theoretic or intersection-theoretic arguments cannot work, since they would transfer to characteristic $p$.
- **BMY has hypotheses that fail asymptotically.** The Miyaoka–Sakai inequality requires $K_X + C$ nef with controlled singularity types, and it degrades as singularities of $C$ get worse. It yields sharp bounds for line and conic arrangements but no statement for curves of unbounded degree with unbounded multiplicities on an arbitrary surface.
- **Cone-of-curves methods stall.** For surfaces with non-polyhedral pseudo-effective cone (e.g. $\mathrm{Bl}_n \mathbb{P}^2$, $n \geq 10$) the negative curves accumulate near the boundary of the nef cone, and Mori theory offers no control over their self-intersections.

## 6. The Gap

Proven: $C^2 \ge -b(X)$ whenever the negative curves either (i) form a finite set determined by cone geometry, (ii) are constrained by $K_X \cdot C \le 0$, or (iii) are configurations of low-degree curves (lines, conics, elliptic curves) reachable by log-BMY.

Conjectured: the same for arbitrary reduced curves on arbitrary characteristic-$0$ surfaces.

The precise missing step is a **uniform upper bound of the form $K_X \cdot C \le 2p_a(C) - 2 + b(X)$ for irreducible curves on surfaces of general type**, together with a mechanism controlling cross terms for reducible reduced curves. Concretely, the sharpest quantitative gap is:
$$-4 \;\leq\; H_L(\mathbb{P}^2) \;\leq\; -\tfrac{9}{4},$$
and even $H(\mathbb{P}^2) > -\infty$ — bounded negativity for *all* blow-ups of the plane at *arbitrary* points with *arbitrary* reduced curves — is open. Closing that single case would settle BNC for every rational surface.

## 7. Current Research (as of June 2026)

- **Harbourne-constant program.** Groups around Szemberg and Tutaj-Gasińska (Kraków), Pokora (Kraków/Bonn), Harbourne (Nebraska), and Bauer (Erlangen) continue to compute $H$-constants for arrangements of conics, cubics, and higher-degree curves, and for arrangements on abelian and K3 surfaces. The unresolved target is whether $H_L(\mathbb{P}^2) = -9/4$, attained by the dual Hesse configuration. *(frontier — verify)*
- **Orbifold BMY refinements.** Work extending Miyaoka's inequality to $\mathbb{Q}$-divisor boundaries with arbitrary coefficients aims to remove the "mild singularities" hypothesis and reach curves of unbounded degree. *(frontier — verify)*
- **Non-Mori-dream constructions.** González-Anaya, González, and Karu study negative curves on blow-ups of weighted projective planes; these produce explicit surfaces with a unique negative curve of very large negativity, testing sharpness of any conjectural $b(X)$.
- **Symbolic powers and containment.** BNC feeds the Harbourne–Huneke containment problem $I^{(3)} \subseteq I^2$ for ideals of points; counterexamples (Dumnicki–Szemberg–Tutaj-Gasińska, based on the dual Hesse configuration) came from the same arrangement geometry, keeping the two problems coupled.
- **Positive characteristic.** Classification of which characteristic-$p$ surfaces *do* satisfy bounded negativity (beyond the Frobenius obstruction) is an active side thread.

## 8. Future Work

- Prove $H(\mathbb{P}^2) > -\infty$: a bound of the form $d^2 - \sum m_i^2 \geq -c\,s$ for *every* reduced plane curve of degree $d$ with $s$ singular points of multiplicities $m_i$, with $c$ absolute. This is the cleanest single statement that would unlock the rational case.
- Establish whether BNC is a birational invariant, i.e. whether BNC for $X$ implies BNC for all blow-ups of $X$. A positive answer reduces the whole conjecture to minimal models.
- Attack surfaces of general type via effective Bogomolov-type inequalities on $\Omega^1_X$ and the Bogomolov–Miyaoka–Yau slope, seeking $K_X \cdot C \le 2p_a(C) + O(1)$.
- Extract from Nagata/SHGH a self-contained proof for $\mathrm{Bl}_n \mathbb{P}^2$, $n \geq 10$ very general, which is currently only conditional.
- Formulate and test a higher-dimensional analogue (bounded negativity for divisors restricted to surfaces in $X$ of dimension $\geq 3$).

## 9. Key References

- **[Foundational]** M. Nagata. *On rational surfaces II.* Memoirs of the College of Science, University of Kyoto, Ser. A, 33 (1960), 271–293.
- **[Foundational]** F. Sakai. *Semistable curves on algebraic surfaces and logarithmic pluricanonical maps.* Mathematische Annalen 254 (1980), 89–120.
- **[Foundational]** Y. Miyaoka. *The maximal number of quotient singularities on surfaces with given numerical invariants.* Mathematische Annalen 268 (1984), 159–171.
- **[Foundational]** F. Hirzebruch. *Arrangements of lines and algebraic surfaces.* In: Arithmetic and Geometry, Vol. II, Progress in Mathematics 36, Birkhäuser, 1983, 113–140.
- **[SOTA]** Th. Bauer, B. Harbourne, A. L. Knutsen, A. Küronya, S. Müller-Stach, X. Roulleau, T. Szemberg. *Negative curves on algebraic surfaces.* Duke Mathematical Journal 162 (2013), no. 10, 1877–1894.
- **[SOTA]** Th. Bauer, S. Di Rocco, B. Harbourne, J. Huizenga, A. Lundman, P. Pokora, T. Szemberg. *Bounded negativity and arrangements of lines.* International Mathematics Research Notices 2015, no. 19, 9456–9471.
- **[SOTA]** X. Roulleau. *Bounded negativity, Miyaoka–Sakai inequality and elliptic curve configurations.* International Mathematics Research Notices 2017, no. 8, 2480–2496.
- **[Survey]** Th. Bauer, C. Bocci, S. Cooper, S. Di Rocco, M. Dumnicki, B. Harbourne, K. Jabbusch, A. L. Knutsen, A. Küronya, R. Miranda, J. Roé, H. Schenck, T. Szemberg, Z. Teitler. *Recent developments and open problems in linear series.* In: Contributions to Algebraic Geometry (Impanga Lecture Notes), EMS Series of Congress Reports, European Mathematical Society, 2012, 93–140.
- **[Survey]** Th. Bauer, S. Di Rocco, B. Harbourne, M. Kapustka, A. L. Knutsen, W. Syzdek, T. Szemberg. *A primer on Seshadri constants.* Contemporary Mathematics 496, American Mathematical Society, 2009, 33–70.
- **[Related]** M. Dumnicki, T. Szemberg, H. Tutaj-Gasińska. *Counterexamples to the $I^{(3)} \subset I^2$ containment.* Journal of Algebra 393 (2013), 24–29.

## 10. Worked Example / Concrete Special Case

**(a) Why characteristic $0$ is necessary.** Let $C$ be a smooth projective curve of genus $g \geq 2$ over $\overline{\mathbb{F}_q}$, defined over $\mathbb{F}_q$, and set $X = C \times C$, a smooth projective surface. For $n \geq 1$ let $F^n : C \to C$ be the $q^n$-power Frobenius and
$$\Gamma_n = \{ (x, F^n(x)) : x \in C \} \subset X,$$
its graph — an irreducible reduced curve isomorphic to $C$, so $p_a(\Gamma_n) = g$.

The projection $\mathrm{pr}_1|_{\Gamma_n}$ has degree $1$ and $\mathrm{pr}_2|_{\Gamma_n}$ has degree $\deg F^n = q^n$. Since $K_X = \mathrm{pr}_1^{*} K_C + \mathrm{pr}_2^{*} K_C$ and $\deg K_C = 2g - 2$,
$$K_X \cdot \Gamma_n = (2g-2)\cdot 1 + (2g-2)\cdot q^n = (2g-2)(1 + q^n).$$
Adjunction gives
$$\Gamma_n^2 = 2p_a(\Gamma_n) - 2 - K_X \cdot \Gamma_n = (2g-2) - (2g-2)(1+q^n) = -(2g-2)\,q^n .$$
With $g = 2$, $q = 2$: $\Gamma_n^2 = -2^{n+1} \to -\infty$. Bounded negativity fails on $C \times C$ in characteristic $p$. Any proof of BNC must therefore use an input unavailable in characteristic $p$.

**(b) The dual Hesse configuration: the current record for $H_L(\mathbb{P}^2)$.** Over $\mathbb{C}$, let $\omega = e^{2\pi i/3}$ and take the $9$ lines dual to the base points of the Hesse pencil:
$$x = 0,\; y = 0,\; z = 0,\quad x + \omega^{j} y + \omega^{k} z = 0 \;\; (j,k \in \{0,1,2\})\ \text{suitably normalized}.$$
This arrangement has $d = 9$ lines and exactly $s = 12$ singular points, all triple ($t_3 = 12$, $t_2 = 0$). Check against Hirzebruch: $t_2 + \tfrac{3}{4} t_3 = 9 \ge d = 9$ — equality, so the configuration is extremal.

Let $f : Y \to \mathbb{P}^2$ blow up the $12$ triple points, and let $\tilde{C}$ be the strict transform of the total arrangement $C$ (degree $9$, so $C^2 = 81$):
$$\tilde{C}^2 = 81 - \sum_{i=1}^{12} 3^2 = 81 - 108 = -27 .$$
Hence
$$H_L(\text{dual Hesse}) = \frac{\tilde{C}^2}{s} = \frac{-27}{12} = -\frac{9}{4} = -2.25 .$$
No line arrangement in $\mathbb{P}^2$ is known with a smaller value, while the Hirzebruch-based theorem only guarantees $H_L(\mathbb{P}^2) \geq -4$. The unclosed interval $[-4, -9/4]$ is the quantitative face of the conjecture in its simplest instance.

**(c) A case where the bound is immediate.** On a smooth quartic surface $X \subset \mathbb{P}^3$ (a K3, $K_X = 0$), any irreducible reduced curve satisfies $C^2 = 2p_a(C) - 2 \geq -2$, with $-2$ attained by lines on $X$ (e.g. the $64$ lines on the Schur quartic). So $b(X) = 2$: BNC holds, sharply.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*