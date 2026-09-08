---
id: 03-geometry/effective-manin-mumford
title: "Coleman-Gross Conjecture on Torsion Points and Higher Genus Curves (Manin-Mumford Effectivity)"
topic: 03-geometry
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Coleman-Gross Conjecture on Torsion Points and Higher Genus Curves (Manin-Mumford Effectivity)

> **Topic:** Algebraic & Differential Geometry · **ID:** `03-geometry/effective-manin-mumford` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Let $C$ be a smooth projective curve of genus $g \ge 2$ over an algebraically closed field $k$ of characteristic $0$, let $J = \operatorname{Jac}(C)$, and fix a base point $b \in C(k)$. The Abel–Jacobi embedding is
$$\iota_b : C \hookrightarrow J, \qquad P \mapsto [P - b].$$
The **torsion packet** of $C$ at $b$ is $T_b(C) = \iota_b^{-1}(J_{\mathrm{tors}}) = \{P \in C(k) : [P-b] \text{ has finite order}\}$.

The **Manin–Mumford conjecture** — that $T_b(C)$ is finite — is a theorem (Raynaud, 1983). The problem catalogued here is the *effective and uniform* refinement, in the form pushed by Coleman and by the $p$-adic height circle of Coleman–Gross:

> **(EMM-1, effectivity.)** Give an algorithm that, on input a curve $C/\overline{\mathbb{Q}}$ of genus $g \ge 2$ and a base point $b$, outputs the finite set $T_b(C)$ *together with a proof of completeness*, with a complexity bound explicit in $g$, the height of $C$, and $[\,\mathbb{Q}(C,b):\mathbb{Q}\,]$.
>
> **(EMM-2, uniformity with an explicit constant.)** Produce an explicit function $c(g)$ with $\\#T_b(C) \le c(g)$ for every $C$ of genus $g$ and every $b$; conjecturally $c(g)$ is polynomial in $g$.

Finiteness of $c(g)$ is now a theorem (Kühne 2021; Gao–Ge–Kühne 2021), but the constant produced is **ineffective**, and no general algorithm certifying $T_b(C)$ is known. A complete solution to EMM-1 is a decision procedure with a proof of termination and correctness; a solution to EMM-2 is an explicit numerical bound.

## 2. Mathematical Foundations

**Torsion packets and the Weierstrass locus.** $P \in T_b(C)$ iff $n(P-b) = \operatorname{div}(f)$ for some $n \ge 1$, $f \in k(C)^\times$. If $b$ is a Weierstrass point of a hyperelliptic curve, every Weierstrass point $w$ satisfies $2(w-b) \sim 0$, so $\\#T_b(C) \ge 2g+2$.

**Coleman's $p$-adic integration.** Let $C/\mathbb{Q}_p$ have good reduction with special fibre $\overline{C}/\mathbb{F}_p$, and let $\omega \in H^0(C, \Omega^1)$. Coleman integration supplies a locally analytic primitive
$$\lambda_\omega(P) = \int_b^P \omega, \qquad \lambda_\omega : J(\mathbb{C}_p) \to \mathbb{C}_p \ \text{ a homomorphism on divisor classes},$$
so $J_{\mathrm{tors}} \subseteq \ker \lambda_\omega$ for every $\omega$. Hence
$$T_b(C) \subseteq \Big\{ P \in C(\mathbb{C}_p) : \int_b^P \omega = 0 \ \ \forall\, \omega \in H^0(C,\Omega^1) \Big\}.$$
On a residue disc $D_{\bar{x}} = \operatorname{red}^{-1}(\bar x)$ with parameter $t$, $\omega = \big(\sum_{i \ge 0} a_i t^i\big) dt$ and the primitive is a power series whose Newton polygon bounds the number of zeros. When $p > 2g$ the ramification of $\log$ is controlled and the count in each disc is governed by $\operatorname{ord}_{\bar x}(\bar\omega) \le 2g-2$; summing over discs gives Coleman's finiteness with an explicit, $p$-dependent bound.

**Jet-space / Buium bound.** Using $p$-derivations and arithmetic jet spaces, Buium (1992) proved: if $C$ has good reduction at $p > 2g$, then
$$\\#\,T_b(C) \;\le\; p^{4g}\,3^g\, g! .$$

**Coleman–Gross $p$-adic height.** For $C/K$ with $K$ a number field, a choice of idèle class character $\chi$ and of subspaces $W_v \subset H^1_{\mathrm{dR}}(C_{K_v})$ complementary to $H^0(\Omega^1)$ yields a symmetric bilinear global height on degree-zero divisors,
$$h(D_1, D_2) = \sum_v \chi_v\big(h_v(D_1,D_2)\big), \qquad h_p(D_1,D_2) = \int_{D_2} \omega_{D_1},$$
where $\omega_{D_1}$ is the differential of the third kind with residue divisor $D_1$, normalised by $W_p$. Torsion classes have $h \equiv 0$; this quadratic-form vanishing is the input to quadratic Chabauty and to the sharpest current cut-outs of torsion packets.

**Galois-theoretic input.** For $A/K$ abelian, Serre's image-of-Galois theorems and Hindry's argument show that a torsion coset $Z \subseteq A$ with $Z \cap A_{\mathrm{tors}}$ Zariski dense must be a translate of an abelian subvariety by a torsion point; for $C \hookrightarrow J$ with $g \ge 2$, $\iota_b(C)$ generates $J$ and is not a coset, giving finiteness.

## 3. History & State of the Art (SOTA)

- **1963–65:** Manin and Mumford independently pose the finiteness question for $C \cap J_{\mathrm{tors}}$.
- **1983:** Raynaud proves it, first for curves (*Invent. Math.* 71), then for arbitrary subvarieties of abelian varieties, by reduction mod $p^2$ and formal-group arguments. The proof is not effective.
- **1985–87:** Coleman gives a $p$-adic-analytic proof for curves with good reduction at $p > 2g$ (*Annals* 121) and analyses ramified torsion points (*Duke* 54). This is the first genuinely *quantitative* route.
- **1988:** Hindry proves the Manin–Mumford statement for semiabelian varieties using Galois representations.
- **1989:** Coleman–Gross construct $p$-adic heights on curves, the tool that later powers quadratic Chabauty.
- **1992:** Buium's jet-space bound $p^{4g}3^g g!$ — the standard explicit bound to this day.
- **1999–2001:** Coleman–Kaskel–Ribet determine the torsion packet of $X_0(N)$; Baker extends to composite $N$; Baker–Poonen bound packets for curves with special automorphisms; Hrushovski gives a model-theoretic (difference-field) proof yielding bounds of the shape $c(g)\cdot p^{\dim}$.
- **2000:** Rémond gives quantitative Mordell–Lang/Manin–Mumford counts with constants depending on degrees in a fixed projective embedding.
- **2008:** Pila–Zannier reprove Manin–Mumford via o-minimality and the Pila–Wilkie counting theorem — conceptually decisive, but Pila–Wilkie constants are ineffective.
- **2020–21:** DeMarco–Krieger–Ye prove uniform Manin–Mumford for an explicit family of genus-2 curves using arithmetic-dynamical equidistribution; Kühne proves uniform Bogomolov in families, and Gao–Ge–Kühne deduce **uniform Manin–Mumford**: $\\#T_b(C) \le c(g)$ for all genus-$g$ curves. The constants are ineffective.

**SOTA summary.** Finiteness: complete. Uniform boundedness: complete but ineffective. Explicit bounds: only $p$-dependent (Buium/Coleman), only under good reduction at $p > 2g$. Algorithmic determination: only for special curves.

## 4. Partial Results / Verified Cases

| Class | Result |
|---|---|
| Good reduction at $p > 2g$ | $\\#T_b(C) \le p^{4g} 3^g g!$ (Buium 1992); Coleman's residue-disc count when $p > 2g$ |
| Genus $2$, $b$ a Weierstrass point | Boxall–Grant (2000): explicit bounds, at most $22$ torsion points in the Weierstrass-embedded case, with worked examples |
| $X_0(N)$, $N$ prime $\ge 23$, $b = \infty$ | Coleman–Kaskel–Ribet (1999): the packet is exactly the cusps together with the hyperelliptic branch points |
| $X_0(N)$, general $N$ | Baker (2000), *Invent. Math.* 140 |
| Curves with large automorphism group / CM Jacobians | Baker–Poonen (2001): packets computed or bounded via the $\mathbb{Z}[\zeta_n]$-action |
| Fermat curves $x^n + y^n = z^n$ | Coleman and successors: torsion packets at cusps/rational points determined for many $n$ |
| Genus $2$ family $y^2 = x^6 + ax^4 + bx^2 + 1$-type | DeMarco–Krieger–Ye (2020): uniform bound, ineffective in the constant only for degenerate members |
| All genus $g \ge 2$ over $\mathbb{C}$ | Kühne (2021), Gao–Ge–Kühne (2021): $\\#T_b(C) \le c(g)$, $c(g)$ not computed |

## 5. Principal Obstacles

- **Ineffectivity of Pila–Wilkie.** The o-minimal counting theorem gives $N(\Gamma, T) \ll_\epsilon T^\epsilon$ with a constant that is not computable from the defining formula; every Pila–Zannier-style proof inherits this. Making it effective requires effective transcendence/height lower bounds for periods that are not available.
- **Bad reduction destroys $p$-adic counting.** Coleman's and Buium's arguments need good reduction at $p > 2g$. For a curve over a number field, the smallest such prime can be exponentially large in the height and degree of $C$, so $p^{4g}$ is not a bound in terms of $g$ alone. On semistable but bad reduction, the residue-disc decomposition is replaced by Berkovich skeleta and tropical Abel–Jacobi maps, where zero-counting for Coleman integrals is far weaker.
- **No lower bound on $p$-adic heights of non-torsion points.** Certifying that a candidate list is complete needs a gap: any $P \notin T_b(C)$ must have $h(P-b, P-b)$ bounded away from $0$. Effective $p$-adic Bogomolov-type lower bounds of that shape are open.
- **Equidistribution constants.** The Kühne / Gao–Ge–Kühne machinery uses adelic equidistribution and non-degeneracy in families; extracting a constant would require effective height inequalities on the moduli side (an effective version of the Bogomolov conjecture in families), which is precisely the missing ingredient.
- **Galois image bounds.** Hindry's route needs an effective open-image theorem for $\operatorname{Gal}(\overline{K}/K) \to \operatorname{GSp}_{2g}(\hat{\mathbb{Z}})$ uniform in $g$; unavailable beyond $g \le 3$ and CM cases.

## 6. The Gap

Proven: (i) finiteness for all $C$; (ii) $\\#T_b(C) \le c(g)$ with $c(g)$ existing but uncomputed; (iii) $\\#T_b(C) \le p^{4g}3^g g!$ *given* a good prime $p > 2g$; (iv) exact packets for named families ($X_0(N)$, Fermat, CM genus 2).

Missing: the bridge from "an unspecified $c(g)$ exists" to a written-down $c(g)$, and from "$p$ exists" to "$p$ is bounded in terms of $g$ alone". The precise crossing point is an **effective height gap**: a computable $\epsilon(g) > 0$ such that every non-torsion $P \in C(\overline{\mathbb{Q}})$ satisfies $\hat h(\iota_b(P)) \ge \epsilon(g)$ relative to a normalised theta divisor — an effective, uniform Bogomolov inequality for the Abel–Jacobi image. Everything else in EMM-2 follows from that by a standard covering/counting argument.

## 7. Current Research (as of June 2026)

- **Quadratic Chabauty and Coleman–Gross heights.** Balakrishnan–Dogra and collaborators (Oxford, Boston University, MIT) compute $p$-adic heights to cut out rational and torsion points; the same local expansions certify packet completeness on individual curves. Software: `SageMath`/`Magma` Coleman-integration packages.
- **Tropical and Berkovich Chabauty.** Katz–Rabinoff–Zureick-Brown-style methods extend $p$-adic zero-counting to bad reduction via metric graphs; extending torsion-packet counts to arbitrary semistable models is the active frontier *(frontier — verify)*.
- **Explicating $c(g)$.** Groups around Gao (Sorbonne/Peking), Kühne (Basel), and Habegger (Basel) are examining which steps of the uniform Bogomolov proof can be made effective; partial effectivity in the non-degenerate range has been announced *(frontier — verify)*.
- **Arithmetic dynamics.** DeMarco–Krieger–Ye's equidistribution techniques yield explicit bounds for families where the relevant dynamical systems are computable (Lattès-type, bielliptic genus 2).
- **Model-theoretic effectivity.** Refinements of Hrushovski's difference-field proof aiming at bounds polynomial in $g$ and the degree of a good reduction datum.

## 8. Future Work

1. **Effective uniform Bogomolov.** Produce a computable $\epsilon(g)$ as in §6; this is the consensus bottleneck.
2. **A bad-reduction Coleman bound.** Prove $\\#T_b(C) \le F(g, \text{combinatorics of the special fibre})$ for semistable models, removing the $p > 2g$ good-reduction hypothesis.
3. **A certified algorithm.** Combine Coleman integration on all residue discs at a single prime with a Coleman–Gross height gap to output $T_b(C)$ with a machine-checkable completeness proof; target: all genus 2 and 3 curves of small conductor.
4. **Sharp constants.** Determine $\max_{C,b} \\#T_b(C)$ for $g = 2$ (is $22$ optimal?) and $g = 3$.
5. **Function-field and positive-characteristic analogues**, where Hrushovski's methods already give better effectivity.

## 9. Key References

- **[Foundational]** M. Raynaud. *Courbes sur une variété abélienne et points de torsion.* Inventiones Mathematicae 71 (1983), 207–233.
- **[Foundational]** M. Raynaud. *Sous-variétés d'une variété abélienne et points de torsion.* In *Arithmetic and Geometry*, Vol. I, Progress in Mathematics 35, Birkhäuser, 1983, 327–352.
- **[Foundational]** R. F. Coleman. *Torsion points on curves and $p$-adic abelian integrals.* Annals of Mathematics 121 (1985), 111–168.
- **[Foundational]** R. F. Coleman. *Ramified torsion points on curves.* Duke Mathematical Journal 54 (1987), 615–640.
- **[Foundational]** R. F. Coleman and B. H. Gross. *$p$-adic heights on curves.* In *Algebraic Number Theory*, Advanced Studies in Pure Mathematics 17, 1989, 73–81.
- **[Foundational]** M. Hindry. *Autour d'une conjecture de Serge Lang.* Inventiones Mathematicae 94 (1988), 575–603.
- **[Effective bound]** A. Buium. *Intersections in jet spaces and a conjecture of S. Lang.* Annals of Mathematics 136 (1992), 557–567.
- **[Structural]** E. Hrushovski. *The Manin–Mumford conjecture and the model theory of difference fields.* Annals of Pure and Applied Logic 112 (2001), 43–115.
- **[Structural]** J. Pila and U. Zannier. *Rational points in periodic analytic sets and the Manin–Mumford conjecture.* Rendiconti Lincei — Matematica e Applicazioni 19 (2008), 149–162.
- **[Computed cases]** R. Coleman, B. Kaskel, K. Ribet. *Torsion points on $X_0(N)$.* Proceedings of Symposia in Pure Mathematics 66, Part 1, AMS, 1999.
- **[Computed cases]** M. Baker. *Torsion points on modular curves.* Inventiones Mathematicae 140 (2000), 487–509.
- **[Computed cases]** M. Baker and B. Poonen. *Torsion packets on curves.* Compositio Mathematica 127 (2001), 109–116.
- **[Computed cases]** J. Boxall and D. Grant. *Examples of torsion points on genus two curves.* Transactions of the AMS 352 (2000), 4533–4555.
- **[Quantitative]** G. Rémond. *Décompte dans une conjecture de Lang.* Inventiones Mathematicae 142 (2000), 513–545.
- **[SOTA / Recent]** L. DeMarco, H. Krieger, H. Ye. *Uniform Manin–Mumford for a family of genus 2 curves.* Annals of Mathematics 191 (2020), 949–1001.
- **[SOTA / Recent]** L. Kühne. *Equidistribution in families of abelian varieties and uniformity.* arXiv:2101.10272, 2021.
- **[SOTA / Recent]** Z. Gao, T. Ge, L. Kühne. *The uniform Mordell–Lang conjecture.* arXiv:2105.15085, 2021.
- **[SOTA / Recent]** V. Dimitrov, Z. Gao, P. Habegger. *Uniformity in Mordell–Lang for curves.* Annals of Mathematics 194 (2021), 237–298.
- **[Method]** J. S. Balakrishnan and N. Dogra. *Quadratic Chabauty and rational points I: $p$-adic heights.* Duke Mathematical Journal 167 (2018), 1981–2038.
- **[Method]** E. Katz, J. Rabinoff, D. Zureick-Brown. *Uniform bounds for the number of rational points on curves of small Mordell–Weil rank.* Duke Mathematical Journal 165 (2016), 3189–3240.
- **[Survey]** P. Tzermias. *The Manin–Mumford conjecture: a brief survey.* Bulletin of the London Mathematical Society 32 (2000), 641–652.
- **[Survey]** U. Zannier. *Some Problems of Unlikely Intersections in Arithmetic and Geometry.* Annals of Mathematics Studies 181, Princeton University Press, 2012.

## 10. Worked Example / Concrete Special Case

Take the genus-2 curve
$$C: y^2 = x^5 - 1 \quad \text{over } \mathbb{Q}, \qquad b = \infty \ (\text{the unique point at infinity, a Weierstrass point}).$$
$J = \operatorname{Jac}(C)$ has CM by $\mathbb{Z}[\zeta_5]$ via the automorphism $\sigma(x,y) = (\zeta_5 x, y)$.

**Step 1 — Weierstrass points give 2-torsion.** For $w_i = (\zeta_5^i, 0)$, $i = 0,\dots,4$:
$$\operatorname{div}(x - \zeta_5^i) = 2\,w_i - 2\infty \ \Longrightarrow\ 2[w_i - \infty] = 0 .$$
Each class is nonzero ($w_i \ne \infty$ and $g \ge 2$ makes $\iota_\infty$ injective). That is $6$ points of $T_\infty(C)$: $\infty$ and the five $w_i$. Also $\operatorname{div}(y) = \sum_i w_i - 5\infty$, so $\sum_{i} [w_i - \infty] = 0$: the five classes span a $(\mathbb{Z}/2)^4$ inside $J[2] \cong (\mathbb{Z}/2)^4$.

**Step 2 — the CM action produces 5-torsion.** Let $P = (0, \mathrm{i})$ with $\mathrm{i}^2 = -1$. Then $\sigma(P) = P$, so $(\sigma - 1)[P - \infty] = 0$. Since $\sigma$ acts as $\zeta_5$ and $\zeta_5 - 1$ has norm $N_{\mathbb{Q}(\zeta_5)/\mathbb{Q}}(\zeta_5 - 1) = 5$, the endomorphism $\sigma - 1$ is an isogeny of degree $25$. Hence $[P - \infty] \in \ker(\sigma - 1)$ is torsion, of order dividing $5$; being nonzero, it has order exactly $5$. Likewise for $\bar P = (0,-\mathrm{i})$, and $\operatorname{div}(x) = P + \bar P - 2\infty$ shows $[\bar P - \infty] = -[P-\infty]$.

So $\\#T_\infty(C) \ge 8$: $\ \infty,\ (\zeta_5^i,0)_{i=0}^{4},\ (0,\pm \mathrm{i})$.

**Step 3 — what the effective bounds give.** $\operatorname{disc}(x^5-1) = 5^5$, so $C$ has good reduction away from $2$ and $5$. Take $p = 11 > 2g = 4$. Buium's bound reads
$$\\#T_\infty(C) \le p^{4g} 3^g g! = 11^{8} \cdot 9 \cdot 2 = 214\,358\,881 \cdot 18 = 3\,858\,459\,858 .$$
Boxall–Grant's genus-2 Weierstrass analysis brings this to $\le 22$. The truth is $8$.

**The gap in one line.** $8 \le \\#T_\infty(C) \le 22$ from the best structural bound, $\le 3.86 \times 10^9$ from the best general effective bound, and $\le c(2)$ with $c(2)$ unknown from the uniform theorem — while a Coleman-integration computation at $p=11$ (zeros of $\int_\infty^P \omega$, $\omega \in \{dx/y,\ x\,dx/y\}$, on each of the $\\#\overline{C}(\mathbb{F}_{11})$ residue discs) is the only route that actually pins the packet down, and it does not generalise to a curve whose smallest good prime is large.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*