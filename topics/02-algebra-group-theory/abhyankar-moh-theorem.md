---
id: 02-algebra-group-theory/abhyankar-moh-theorem
title: "Abhyankar-Moh Theorem"
topic: 02-algebra-group-theory
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Abhyankar-Moh Theorem

> **Topic:** Algebra & Group Theory · **ID:** `02-algebra-group-theory/abhyankar-moh-theorem` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

Let $k$ be a field and let $f, g \in k[t]$ be non-constant polynomials generating the whole ring:
$$k[f(t), g(t)] = k[t].$$

**Abhyankar–Moh theorem (embedding form).** If $\operatorname{char} k = 0$, then
$$\deg f \mid \deg g \quad \text{or} \quad \deg g \mid \deg f .$$

**Equivalent (epimorphism) form.** Every $k$-algebra epimorphism $\pi: k[x,y] \twoheadrightarrow k[t]$ in characteristic $0$ has kernel $(F)$ where $F$ is a *variable* (coordinate): there is $G \in k[x,y]$ with $k[F,G] = k[x,y]$. Geometrically: **every closed embedding $\mathbb{A}^1_k \hookrightarrow \mathbb{A}^2_k$ is rectifiable** — some polynomial automorphism of $\mathbb{A}^2$ carries the image onto the coordinate line $\{x = 0\}$.

The characteristic-$0$ statement is a theorem (Abhyankar–Moh 1975; Suzuki 1974). What remains open, and what this page tracks, is the residual problem set:

1. **Positive characteristic.** The statement is *false* over $k$ with $\operatorname{char} k = p > 0$ (Segre–Nagata counterexamples). No classification of the non-rectifiable embeddings $\mathbb{A}^1 \hookrightarrow \mathbb{A}^2$ in characteristic $p$ is known.
2. **Abhyankar–Sathaye embedding conjecture.** Every closed embedding $\mathbb{A}^{n-1} \hookrightarrow \mathbb{A}^n$ over a field of characteristic $0$ is rectifiable. Open for $n \ge 4$.
3. **Higher codimension / general curves.** Rectifiability of $\mathbb{A}^1 \hookrightarrow \mathbb{A}^n$ and the "epimorphism problem" for other affine varieties.

A complete resolution of (1) means either a proof under explicit hypotheses on $p$ and the degrees, or a structural description of all counterexamples; of (2), a proof or a counterexample hyperplane.

## 2. Mathematical Foundations

**Setting.** $k$ algebraically closed for geometric statements. A morphism $\varphi: \mathbb{A}^1 \to \mathbb{A}^2$, $t \mapsto (f(t), g(t))$, is a *closed embedding* iff $\varphi^*: k[x,y] \to k[t]$ is surjective, i.e. $k[f,g] = k[t]$.

**Automorphism group.** Write $\operatorname{Aut}_k(\mathbb{A}^2)$ for the group of polynomial automorphisms. Let $A$ be the affine subgroup and $B$ the triangular (de Jonquières) subgroup, $B = \{(x,y) \mapsto (\alpha x + p(y),\, \beta y + \gamma)\}$.

**Jung–van der Kulk theorem.** $\operatorname{Aut}_k(\mathbb{A}^2) = A *_{A \cap B} B$, an amalgamated free product, in every characteristic. Consequently every automorphism is a composite of affine and triangular maps, and a *tame* rectification is the only possible kind in dimension $2$.

**Curves with one place at infinity.** Let $F \in k[x,y]$ be irreducible with $\deg F = n$, and let $\bar{C} \subset \mathbb{P}^2$ be the projective closure of $C = V(F)$. $C$ has *one place at infinity* if $\bar{C}$ meets the line at infinity $L_\infty$ in a single point with a single branch. Any $F$ with $k[x,y]/(F) \cong k[t]$ has this property. Choosing coordinates so $F$ is monic of degree $n$ in $y$, there is a Newton–Puiseux expansion at infinity
$$y(x) = \sum_{i \le m_1} a_i \, x^{i/n}, \qquad a_i \in \bar{k}, \; m_1 < n .$$

**Characteristic sequence and semigroup.** Set $v_0 = n$, let $v_1 > v_2 > \cdots > v_h$ be the successive characteristic exponents of the expansion (rescaled), and $d_i = \gcd(v_0, v_1, \dots, v_{i-1})$, so $d_1 = n$ and $d_{h+1} = 1$. The **Abhyankar–Moh semigroup condition** for one place at infinity is
$$d_i v_i > d_{i+1} v_{i+1} \qquad (1 \le i \le h-1),$$
and the value semigroup at infinity $\Gamma = \langle v_0, v_1, \dots, v_h \rangle \subseteq \mathbb{Z}$ has conductor
$$c(\Gamma) = \sum_{i=1}^{h} (d_i - d_{i+1}) v_i - v_0 .$$

**Approximate roots.** For $d \mid n$, the *$d$-th approximate root* $\operatorname{App}_d(F)$ is the unique monic $P \in k[x][y]$ of $y$-degree $n/d$ with $\deg_y (F - P^d) < n - n/d$. Existence requires $d$ invertible in $k$ — this is where characteristic enters. The *generalized Tschirnhausen transformation* replaces $F$ by successive approximate roots, lowering $h$ by one at each stage.

**Proof skeleton (char $0$).** Since $C \cong \mathbb{A}^1$ is rational and unibranch at infinity, the genus formula forces $c(\Gamma) = (n-1)(n-2)$-type equality, which with the semigroup condition forces $h = 1$ and $v_1 \equiv 0 \pmod{\gcd}$; the Tschirnhausen step then produces a coordinate change strictly reducing $\max(\deg f, \deg g)$. Induction terminates at $(t, 0)$, proving both rectifiability and the divisibility $\deg f \mid \deg g$ or conversely.

## 3. History & State of the Art (SOTA)

- **1942 / 1953.** Jung, then van der Kulk, determine $\operatorname{Aut}_k(\mathbb{A}^2)$ — the structural prerequisite.
- **1957 / 1972.** Segre, and later Nagata, exhibit polynomial parametrizations in characteristic $p$ with non-divisible degrees, showing any proof must be characteristic-sensitive.
- **1973.** Abhyankar and Moh publish *Newton–Puiseux expansion and generalized Tschirnhausen transformation* I and II (J. reine angew. Math. 260, 261), building the valuation-theoretic engine.
- **1974.** M. Suzuki gives an independent, transcendental proof over $\mathbb{C}$ using topology of polynomial maps $\mathbb{C}^2 \to \mathbb{C}$ and the structure of $\operatorname{Aut}(\mathbb{C}^2)$.
- **1975.** Abhyankar–Moh, *Embeddings of the line in the plane*, J. reine angew. Math. 276, 148–166: the algebraic proof, valid over any field of characteristic $0$.
- **1979.** Ganong reproves and extends the result via *plane curves with one place at infinity*, isolating exactly which steps need $p \nmid$ (something).
- **1982.** Rudolph gives a purely topological/knot-theoretic proof over $\mathbb{C}$ (links of the curve at infinity).
- **1987–1991.** Jelonek, Craighero, and then Kaliman prove rectifiability of $\mathbb{A}^1 \hookrightarrow \mathbb{A}^3$ over $\mathbb{C}$ — the codimension-$2$ analogue.
- **1976.** Sathaye proves the embedding conjecture for *linear planes* $\mathbb{A}^2 \hookrightarrow \mathbb{A}^3$ under a fibration hypothesis; the general $n=3$ hyperplane case remains tied to the Abhyankar–Sathaye conjecture.
- **1983.** Moh applies the machinery to the two-dimensional Jacobian conjecture, verifying it for $\deg \le 100$.

## 4. Partial Results / Verified Cases

| Case | Status |
|---|---|
| $\operatorname{char} k = 0$, $n = 2$ in $\mathbb{A}^2$ | **Theorem** (Abhyankar–Moh 1975; Suzuki 1974) |
| $k = \mathbb{C}$, topological proof | **Theorem** (Rudolph 1982) |
| $\mathbb{A}^1 \hookrightarrow \mathbb{A}^3$, $\operatorname{char} 0$ | **Theorem** (Kaliman 1991; earlier cases Craighero, Jelonek) |
| $\mathbb{A}^1 \hookrightarrow \mathbb{A}^n$, $n \ge 4$, $\operatorname{char} 0$ | Rectifiable (Jelonek 1987, via general extension theorems for $n \ge 4$) |
| $\operatorname{char} k = p$, $p \nmid \gcd(\deg f, \deg g)$ | Conclusion holds — the approximate-root/Tschirnhausen induction survives (Abhyankar–Moh 1975; Ganong 1979) |
| $\operatorname{char} k = p$, $\min(\deg f,\deg g) < p$ | Holds, degrees are prime to $p$ |
| $\operatorname{char} k = p$, $p \mid \gcd$ | **False in general** (Segre 1957, Nagata 1972) |
| $\mathbb{A}^2 \hookrightarrow \mathbb{A}^3$, $\operatorname{char} 0$ | Open (Abhyankar–Sathaye); proved for linear planes with an $\mathbb{A}^1$-fibration (Sathaye 1976) |
| $\mathbb{A}^{n-1} \hookrightarrow \mathbb{A}^n$, $n \ge 4$ | Open |

## 5. Principal Obstacles

- **Failure of approximate roots in characteristic $p$.** $\operatorname{App}_d(F)$ is constructed by a division algorithm requiring $d$ to be a unit in $k$. When $p \mid d_i$, the Tschirnhausen step cannot be performed and the degree induction halts. This is not a technical inconvenience: genuine counterexamples live exactly there.
- **Wild ramification at infinity.** In characteristic $p$ the Newton–Puiseux expansion may need Artin–Schreier terms; the value semigroup no longer determines the singularity, so the numerical genus/conductor bookkeeping that drives the char-$0$ proof loses its rigidity.
- **No amalgamated-product structure above dimension $2$.** The char-$0$ proof ultimately rectifies by composing elementary automorphisms. $\operatorname{Aut}(\mathbb{A}^3)$ contains the Nagata automorphism, which is wild (Shestakov–Umirbaev 2004), so "reduce degree by an elementary move" has no analogue for $n \ge 3$; Kaliman's $\mathbb{A}^1 \hookrightarrow \mathbb{A}^3$ proof instead uses topological/analytic input special to codimension $2$ over $\mathbb{C}$.
- **Cancellation-type difficulties.** The Abhyankar–Sathaye conjecture for a hypersurface $H \subset \mathbb{A}^n$ with $H \cong \mathbb{A}^{n-1}$ presupposes $\mathbb{A}^n \cong H \times \mathbb{A}^1$ and asks that the isomorphism be polynomial — precisely the kind of "abstract iso $\Rightarrow$ coordinate" step that fails for the Danielewski and Russell-cubic style examples.
- **No topological handle in char $p$.** Rudolph's and Suzuki's proofs use links at infinity and $\pi_1$ of the complement; there is no substitute over $\overline{\mathbb{F}}_p$ (étale $\pi_1$ is not finitely presented in the needed way).

## 6. The Gap

The proven statement (Section 4) is: *char $0$, or char $p$ with $p \nmid \gcd(\deg f, \deg g)$.* The general statement to be crossed is a description of what happens when $p \mid \gcd(\deg f,\deg g)$. Concretely:

> Given $\operatorname{char} k = p$ and $k[f,g] = k[t]$ with $p \mid \gcd(\deg f, \deg g)$, does every such pair arise from a coordinate line by composing automorphisms of $\mathbb{A}^2$ with Frobenius-type substitutions $t \mapsto t + (\text{additive polynomial})$? No classification is known, and no invariant separating rectifiable from non-rectifiable embeddings has been produced.

For the Abhyankar–Sathaye conjecture the gap is different: even in char $0$, no method converts the abstract isomorphism $k[x,y,z]/(F) \cong k^{[2]}$ into a variable-ness statement for $F$ when $F$ has no $\mathbb{A}^1$-fibration hypothesis attached.

## 7. Current Research (as of June 2026)

- **Affine algebraic geometry school** (Miyanishi–Masuda tradition in Japan; Dubouloz, Poloni and collaborators in France; Gupta, Dutta and the ISI Kolkata group in India). N. Gupta's disproof of the Zariski cancellation problem in positive characteristic (Invent. Math. 2014; Adv. Math. 2014) is the model result: it shows characteristic-$p$ affine geometry admits genuinely new phenomena and has redirected attention to char-$p$ embedding questions.
- **Epimorphism problem for non-linear targets.** Ongoing work asks which plane curves $\{F = 0\}$ with $F$ having one place at infinity are variables; the "$\delta$-invariant" and Abhyankar–Moh inequality remain the sharpest tools.
- **Derivation-theoretic methods.** Locally nilpotent derivations (char $0$) and exponential maps / $\mathbb{G}_a$-actions (char $p$) are used to detect rectifiability; the char-$p$ theory of $\mathbb{G}_a$-actions is much richer and is the main current lever. *(frontier — verify)*
- **Computational search** for characteristic-$p$ counterexamples of small degree beyond the Segre–Nagata family, via Gröbner-basis membership tests for $k[f,g] = k[t]$. *(frontier — verify)*

## 8. Future Work

- Classify all embeddings $\mathbb{A}^1 \hookrightarrow \mathbb{A}^2_{\overline{\mathbb{F}}_p}$ up to $\operatorname{Aut}(\mathbb{A}^2)$; conjecturally they are all obtained from the line by $\mathbb{G}_a$-actions and additive-polynomial substitutions.
- Settle Abhyankar–Sathaye for $n = 3$ in char $0$; this is widely regarded as the next decisive step and is entangled with the Jacobian conjecture in dimension $3$.
- Extend Kaliman's rectification of $\mathbb{A}^1 \hookrightarrow \mathbb{A}^3$ to non-algebraically-closed and to char-$p$ base fields.
- Develop a characteristic-free replacement for approximate roots — e.g. via Hamburger–Noether expansions, which exist in all characteristics.

## 9. Key References

- **[Foundational]** S. S. Abhyankar and T. T. Moh. *Embeddings of the line in the plane.* Journal für die reine und angewandte Mathematik **276** (1975), 148–166.
- **[Foundational]** S. S. Abhyankar and T. T. Moh. *Newton–Puiseux expansion and generalized Tschirnhausen transformation I, II.* J. reine angew. Math. **260** (1973), 47–83; **261** (1973), 29–54.
- **[Foundational]** M. Suzuki. *Propriétés topologiques des polynômes de deux variables complexes et automorphismes algébriques de l'espace $\mathbb{C}^2$.* Journal of the Mathematical Society of Japan **26** (1974), 241–257.
- **[Foundational]** H. W. E. Jung. *Über ganze birationale Transformationen der Ebene.* J. reine angew. Math. **184** (1942), 161–174.
- **[Foundational]** W. van der Kulk. *On polynomial rings in two variables.* Nieuw Archief voor Wiskunde (3) **1** (1953), 33–41.
- **[Structural]** M. Nagata. *On Automorphism Group of $k[x,y]$.* Lectures in Mathematics 5, Kyoto University, Kinokuniya, 1972.
- **[SOTA / Recent]** R. Ganong. *On plane curves with one place at infinity.* J. reine angew. Math. **307/308** (1979), 173–193.
- **[SOTA / Recent]** L. Rudolph. *Embeddings of the line in the plane.* J. reine angew. Math. **337** (1982), 113–118.
- **[SOTA / Recent]** S. Kaliman. *Extensions of isomorphisms between affine algebraic subvarieties of $k^n$ to automorphisms of $k^n$.* Proceedings of the American Mathematical Society **113** (1991), 325–334.
- **[SOTA / Recent]** Z. Jelonek. *The extension of regular and rational embeddings.* Mathematische Annalen **277** (1987), 113–120.
- **[SOTA / Recent]** A. Sathaye. *On linear planes.* Proceedings of the American Mathematical Society **56** (1976), 1–7.
- **[SOTA / Recent]** I. P. Shestakov and U. U. Umirbaev. *The tame and the wild automorphisms of polynomial rings in three variables.* Journal of the AMS **17** (2004), 197–227.
- **[SOTA / Recent]** N. Gupta. *On the cancellation problem for the affine space $\mathbb{A}^3$ in characteristic $p$.* Inventiones Mathematicae **195** (2014), 279–288.
- **[Survey]** A. van den Essen. *Polynomial Automorphisms and the Jacobian Conjecture.* Progress in Mathematics 190, Birkhäuser, 2000.
- **[Survey]** R. Ganong. *The pencil of translates of a line in the plane.* In *Affine Algebraic Geometry*, CRM Proceedings and Lecture Notes **54**, AMS, 2011, 57–71.
- **[Survey]** M. Miyanishi. *Open Algebraic Surfaces.* CRM Monograph Series 12, AMS, 2001.

## 10. Worked Example / Concrete Special Case

**(a) A char-$0$ instance: rectifying a cuspidal parametrization.**
Take $f(t) = t^2$, $g(t) = t^3 + t$ over $\mathbb{Q}$. Then
$$g(t)^2 - f(t)^3 = (t^3+t)^2 - t^6 = 2t^4 + t^2, \qquad 2t^4 + t^2 - 2f(t)^2 = t^2 = f(t),$$
so no new element yet; instead note $g(t) - t\cdot f(t) = t$, and $t \cdot f(t) = t^3$ is not obviously in $k[f,g]$. Direct check: $g^2 = t^6 + 2t^4 + t^2 = f^3 + 2f^2 + f$, so $g^2 - f^3 - 2f^2 - f = 0$ — the pair satisfies an algebraic relation and $k[f,g] \subsetneq k[t]$ (it misses $t$). This map is **not** an embedding, consistent with $\deg f = 2 \nmid 3 = \deg g$: Abhyankar–Moh forbids it. Contrast $f = t^2$, $g = t^5 + t^2$: again $2 \nmid 5$, so no embedding. The only embeddings with $\deg f = 2$ are, up to affine changes, $(t^2, t^{2m} + \cdots)$ with $2 \mid \deg g$, plus the degenerate rectifiable ones — exactly the divisibility constraint.

**(b) The characteristic-$p$ counterexample (Segre–Nagata type).**
Let $\operatorname{char} k = p > 0$ and set
$$f(t) = t^{p^2}, \qquad g(t) = t^{p^2+p} + t .$$
*Claim: $k[f,g] = k[t]$.* Since the $p$-th power map is additive,
$$g^p = t^{p^3 + p^2} + t^p, \qquad f^{p+1} = t^{p^2(p+1)} = t^{p^3+p^2},$$
hence
$$g^p - f^{\,p+1} = t^p \in k[f,g].$$
Then $\big(t^p\big)^{p+1} = t^{p^2+p}$ lies in $k[f,g]$, and therefore
$$t = g - t^{p^2+p} \in k[f,g].$$
So $k[f,g] = k[t]$ and $t \mapsto (f(t), g(t))$ is a closed embedding $\mathbb{A}^1 \hookrightarrow \mathbb{A}^2$.

*But the degrees are $\deg f = p^2$ and $\deg g = p^2 + p$.* Neither divides the other for any prime $p$: $p^2 \mid p^2 + p$ would force $p^2 \mid p$, and $p^2 + p > p^2$ rules out the reverse. Hence the Abhyankar–Moh conclusion fails, and the embedded line is **not rectifiable** — no automorphism of $\mathbb{A}^2$ takes it to a coordinate axis, since the axis would give divisible degrees.

Note $\gcd(p^2, p^2+p) = p$, so $p \mid \gcd(\deg f, \deg g)$: the example sits exactly in the regime the char-$0$ proof cannot reach, and the failure is traceable to the non-existence of the $p$-th approximate root. This single family is the whole of what is known in characteristic $p$; whether it generates all counterexamples under $\operatorname{Aut}(\mathbb{A}^2)$ and additive substitutions is the open question of Section 6.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*