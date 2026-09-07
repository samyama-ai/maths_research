---
id: 03-geometry/oort-conjecture
title: "Oort Conjecture"
topic: 03-geometry
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Oort Conjecture

> **Topic:** Algebraic & Differential Geometry · **ID:** `03-geometry/oort-conjecture` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

Let $k$ be an algebraically closed field of characteristic $p > 0$ and let $Y$ be a smooth projective connected curve over $k$ equipped with a faithful action of a **cyclic** group $G$. The Oort conjecture asserts:

> The pair $(Y, G)$ lifts to characteristic zero: there is a complete local domain $R$ of characteristic $0$ with residue field $k$, and a smooth relative curve $\mathcal{Y} \to \operatorname{Spec} R$ with a faithful $R$-linear $G$-action, whose special fibre is $G$-equivariantly isomorphic to $(Y, G)$.

By the local–global principle (Section 2) this is equivalent to the **local Oort conjecture**: every cyclic subgroup $G \subseteq \operatorname{Aut}_k(k[[t]])$ lifts to a $G$-action on $R[[T]]$ over some such $R$.

A complete proof must handle wild ramification, i.e. $p \mid |G|$; the prime-to-$p$ case is classical (Grothendieck). A disproof would exhibit a single cyclic $G$ and a single wildly ramified point where no lift exists over any $R$.

**Status:** proved. Obus–Wewers (Annals, 2014) settled a large ramification range; Pop (Annals, 2014) reduced the general case to it. The conjecture is now the **Oort theorem**; the open residue is the classification of *all* liftable groups (Section 7).

## 2. Mathematical Foundations

**Local–global principle.** For $(Y,G)$ over $k$, the deformation functor of the global $G$-curve decomposes: obstruction to lifting is concentrated at the wildly ramified points. Formally (Bertin–Mézard 2000, building on Garuti 1996), if $y_1,\dots,y_r$ are the ramification points with stabilizers $G_i = G_{y_i}$, then $(Y,G)$ lifts over $R$ as soon as each local action $G_i \hookrightarrow \operatorname{Aut}_k(\widehat{\mathcal{O}}_{Y,y_i}) \cong \operatorname{Aut}_k(k[[t]])$ lifts over $R$. Conversely, a global lift induces local lifts.

**Definition (local Oort group).** A finite group $G$ is a *local Oort group for $k$* if every faithful action of $G$ on $k[[t]]$ lifts to characteristic $0$.

**Ramification filtration.** For $G \subseteq \operatorname{Aut}_k(k[[t]])$ with $|G| = p^n$, put
$$ i_G(\sigma) = v_t\big(\sigma(t) - t\big), \qquad G_j = \{\sigma : i_G(\sigma) \ge j+1\}, $$
giving lower jumps $\lambda_1 < \lambda_2 < \cdots < \lambda_n$ (all prime to $p$ except possibly forced equalities) and the different
$$ d \;=\; \sum_{j \ge 0}\big(|G_j| - 1\big) \;=\; \sum_{i=1}^{n} \big(p^{\,n-i+1} - 1\big)\,(\lambda_i - \lambda_{i-1}), \qquad \lambda_0 := -1 . $$
Upper jumps $u_i$ are obtained by the Herbrand transform $\psi$; the Hasse–Arf theorem gives $u_i \in \mathbb{Z}$, and in characteristic $p$ one has $u_i \ge p\,u_{i-1}$.

**Artin–Schreier–Witt theory.** With $K = k((t))$, cyclic $\mathbb{Z}/p^n$-extensions are classified by
$$ H^1(K, \mathbb{Z}/p^n) \;\cong\; W_n(K)\big/(F-1)W_n(K), $$
$W_n$ the Witt vectors of length $n$, $F$ the Witt Frobenius. For $n=1$ this is $y^p - y = f(t)$, $f \in K$, with upper break $u_1 = -v_t(f)$ after reduction.

**Characteristic-zero side.** A lift is an action of $G$ on the open $p$-adic disc $\operatorname{Spec} R[[T]]$. Since $|G|$ is invertible on the generic fibre only up to $p$-torsion issues, the quotient map on the generic fibre is a $G$-cover of the disc branched at $\ge 2$ points; the *different criterion* (Green–Matignon) forces
$$ d \;=\; \sum_{\text{branch pts } x} d_x , $$
i.e. the special-fibre different must equal the total contribution of the branch points that coalesce in the reduction. Encoding these coalescence patterns yields the **Hurwitz tree** of the lift (Henrio; Brewis–Wewers), a metric tree with a differential form (*deformation datum*) at each vertex satisfying a residue/degree relation
$$ \sum_{\text{poles}} \operatorname{res} \;=\; -\,\chi\text{-type quantity}, $$
so lifting becomes: construct a Hurwitz tree with prescribed different and solve the associated differential data.

**Obstructions.** Bertin's obstruction (1998) and the refined **KGB obstruction** (Chinburg–Guralnick–Harbater) are computable invariants vanishing only for restricted $G$: a local Oort group must be cyclic, dihedral of order $2p^n$, or $A_4$ with $p=2$.

## 3. History & State of the Art (SOTA)

- **Grothendieck (SGA 1, 1961).** Tame covers lift; $\gcd(|G|,p)=1$ case complete.
- **Oort (1987, 1995).** Formulated the lifting question for curves with automorphisms in *Lifting algebraic curves, abelian varieties, and their endomorphisms to characteristic zero* (PSPM 46) and posed the cyclic case as a conjecture in his problem lists.
- **Sekiguchi–Oort–Suwa (1989).** Constructed the group scheme deformations interpolating $\mu_p$ (Kummer) and $\mathbb{Z}/p$ (Artin–Schreier); settles $G = \mathbb{Z}/p$.
- **Green–Matignon (1998, 1999).** Proved $G = \mathbb{Z}/p^2$; introduced the different/branch-point criterion and the theory of order-$p$ automorphisms of the $p$-adic open disc.
- **Bertin–Mézard (2000).** Local–global principle and equicharacteristic deformation theory.
- **Bouw–Wewers (2006).** Dihedral $D_p$ is a local Oort group; deformation data method.
- **Chinburg–Guralnick–Harbater (2008, 2011).** KGB obstruction; classification of candidate local Oort groups.
- **Obus–Wewers (Annals 180, 2014).** Cyclic $\mathbb{Z}/p^n$ liftable under "no essential ramification".
- **Pop (Annals 180, 2014).** Removed the ramification hypothesis; the Oort conjecture is a theorem.
- **Obus (2016, 2017).** $A_4$ in characteristic $2$; generalization of the Oort theorem to $\mathbb{Z}/p^n \rtimes \mathbb{Z}/m$.

## 4. Partial Results / Verified Cases

| Case | Result | Source |
|---|---|---|
| $\gcd(|G|,p)=1$ | Always lifts | Grothendieck, SGA 1 |
| $G=\mathbb{Z}/p$, any break $u_1$ | Lifts | Oort–Sekiguchi–Suwa 1989; Green–Matignon 1999 |
| $G=\mathbb{Z}/p^2$ | Lifts | Green–Matignon 1998 |
| $G=\mathbb{Z}/p^3$, $p$ odd, small breaks | Lifts | Matignon; Brewis–Wewers |
| $G=\mathbb{Z}/p^n$, "no essential ramification" (each upper jump $u_i$ minimal given $u_{i-1}$) | Lifts | Obus–Wewers 2014 |
| $G=\mathbb{Z}/p^n$, arbitrary breaks | Lifts | Pop 2014 |
| $G=D_p$ (order $2p$), $p$ odd | Local Oort group | Bouw–Wewers 2006 |
| $G=A_4$, $p=2$ | Local Oort group | Obus 2016 |
| $G=\mathbb{Z}/p^n\rtimes\mathbb{Z}/m$, $m \mid p-1$, mild conditions | Lifts | Obus 2017 |
| $G$ with non-cyclic Sylow $p$-subgroup, $|G_1|>1$ | **Does not lift** (KGB) | Chinburg–Guralnick–Harbater 2008/2011 |

Concretely, for genus-$g$ curves this settles all $\mathbb{Z}/p^n$-actions for every $n \ge 1$, every $p$, and every admissible jump sequence $(\lambda_1,\dots,\lambda_n)$ with $p \nmid \lambda_i$.

## 5. Principal Obstacles

Why the cyclic case resisted for 25 years:

- **No équivariant deformation-theoretic vanishing.** The obstruction space $H^2$ for the equivariant deformation functor is generally nonzero; formal smoothness fails, so one cannot lift step-by-step along $R/\mathfrak{m}^n$.
- **Wild ramification is not rigid.** The different $d$ grows like $p^n \lambda_n$, so a lift must produce many branch points in the generic fibre; their configuration is a nontrivial combinatorial problem (the Hurwitz tree), not an infinitesimal one.
- **Induction on $n$ breaks down.** A $\mathbb{Z}/p^n$-extension is built from a $\mathbb{Z}/p^{n-1}$-quotient, but a lift of the quotient need not extend: the extension class in $W_n(K)/(F-1)$ can force upper jumps $u_n \gg p\,u_{n-1}$ ("essential ramification"), which makes the residual differential equation on the tree have poles with no admissible residue solution.
- **Deformation data are overdetermined.** The residue conditions on each vertex of the Hurwitz tree form a system whose solvability is a nonlinear condition on the tree metric; for large jumps no *a priori* argument gives a solution.
- **Characteristic-zero rigidity of $\mu_{p^n}$.** Kummer theory gives $\mu_{p^n}$-covers, but the specialization $\mu_{p^n} \rightsquigarrow \mathbb{Z}/p^n$ requires the Sekiguchi–Suwa group schemes, whose deformation parameters are hard to control for $n \ge 3$.

## 6. The Gap

Before 2012 the gap was exactly this: Obus–Wewers solved the local lifting problem for $\mathbb{Z}/p^n$ **when the upper jumps are as small as they can be**, by explicitly constructing the required deformation data on a Hurwitz tree. The general jump sequence produced "essential ramification", where the differential data acquire extra poles and the construction fails.

Pop closed the gap not by solving those cases directly, but by a **degeneration/specialization argument**: any $\mathbb{Z}/p^n$-extension of $k[[t]]$ can be realized as a specialization of an extension defined over a larger (non-algebraically-closed, "generic") base for which the ramification is of no-essential type, and liftability propagates from the generic member of such a family to its specializations. Combined with the Katz–Gabber canonical globalization of a local extension, this yields the full local Oort conjecture, hence the global one.

## 7. Current Research (as of June 2026)

- **Classification of local Oort groups.** The remaining question is: is every group on the KGB list (cyclic, $D_{p^n}$, $A_4$ for $p=2$) actually a local Oort group? Cyclic — yes; $D_p$ — yes; $A_4$, $p=2$ — yes (Obus 2016). Higher dihedral $D_{p^n}$, $n \ge 2$, is largely open. Dang–Das–Karemaker–Obus–Thatte introduced the *isolated differential data criterion* and settled further small dihedral cases in characteristic $2$ *(frontier — verify)*.
- **Generalized/weak Oort groups.** Groups that lift for *some* but not all actions; Obus's "generalization of the Oort conjecture" (2017) covers $\mathbb{Z}/p^n\rtimes\mathbb{Z}/m$ and is being pushed to metacyclic $G$ *(frontier — verify)*.
- **Effective and arithmetic refinements.** Determining the minimal ring $R$ (ramification of $R/W(k)$) needed for a given jump sequence; expected to relate to the Hurwitz-tree metric.
- **Moduli interpretation.** Lifting statements as smoothness/irreducibility statements for the moduli stack of $G$-covers over $\mathbb{Z}_p$, connected to work on the special fibres of Hurwitz spaces.
- **Groups/centres.** Obus (Baruch College/CUNY), Wewers (Ulm), Pop (Penn), Matignon (Bordeaux), Karemaker (Utrecht), Dang (Virginia/Versailles).

## 8. Future Work

- Prove or disprove that $D_{p^n}$ is a local Oort group for all $n$ — the last structural item on the KGB list.
- Develop a *uniform* proof of the cyclic case that avoids Pop's degeneration step, giving explicit equations for the lift over an explicit $R$ (Matignon's program).
- Extend the Hurwitz-tree formalism to non-cyclic $p$-groups to make the KGB obstruction sharp, i.e. show it is the *only* obstruction.
- Lifting with prescribed extra structure (level structure, marked points, semistable degenerations), aimed at comparing $\overline{\mathcal{M}}_g$ in mixed characteristic.
- Analogues for higher-dimensional varieties and for $\mathbb{Z}_p$-actions on formal schemes.

## 9. Key References

- **[Foundational]** A. Grothendieck. *Revêtements étales et groupe fondamental (SGA 1).* Lecture Notes in Math. 224, Springer, 1971.
- **[Foundational]** F. Oort. *Lifting algebraic curves, abelian varieties, and their endomorphisms to characteristic zero.* Proc. Sympos. Pure Math. 46, Part 2, AMS, 1987, 165–195.
- **[Foundational]** T. Sekiguchi, F. Oort, N. Suwa. *On the deformation of Artin–Schreier to Kummer.* Ann. Sci. École Norm. Sup. (4) 22 (1989), 345–375.
- **[Foundational]** B. Green, M. Matignon. *Liftings of Galois covers of smooth curves.* Compositio Math. 113 (1998), 237–272.
- **[Foundational]** B. Green, M. Matignon. *Order $p$ automorphisms of the open disc of a $p$-adic field.* J. Amer. Math. Soc. 12 (1999), 269–303.
- **[Foundational]** J. Bertin, A. Mézard. *Déformations formelles des revêtements sauvagement ramifiés de courbes algébriques.* Invent. Math. 141 (2000), 195–238.
- **[SOTA]** A. Obus, S. Wewers. *Cyclic extensions and the local lifting problem.* Annals of Mathematics 180 (2014), 233–284.
- **[SOTA]** F. Pop. *The Oort conjecture on lifting covers of curves.* Annals of Mathematics 180 (2014), 285–322.
- **[SOTA]** A. Obus. *The local lifting problem for $A_4$.* Algebra & Number Theory 10 (2016), 1683–1693.
- **[SOTA]** A. Obus. *A generalization of the Oort conjecture.* Comment. Math. Helv. 92 (2017), 551–620.
- **[Structural]** T. Chinburg, R. Guralnick, D. Harbater. *Oort groups and lifting problems.* Compositio Math. 144 (2008), 849–866.
- **[Structural]** T. Chinburg, R. Guralnick, D. Harbater. *The local lifting problem for actions of finite groups on curves.* Ann. Sci. Éc. Norm. Supér. (4) 44 (2011), 537–605.
- **[Structural]** I. Bouw, S. Wewers. *The local lifting problem for dihedral groups.* Duke Math. J. 134 (2006), 421–452.
- **[Structural]** L. Brewis, S. Wewers. *Artin characters, Hurwitz trees and the lifting problem.* Math. Ann. 345 (2009), 711–730.
- **[Survey]** A. Obus. *The (local) lifting problem.* Survey, arXiv:1105.1530, 2011.

## 10. Worked Example / Concrete Special Case

**Setting.** $p = 2$, $k = \overline{\mathbb{F}}_2$, $G = \mathbb{Z}/2 = \langle \sigma \rangle$ acting on $k[[t]]$ by
$$ \sigma(t) \;=\; \frac{t}{1+t}. $$

*Order check.* $\sigma^2(t) = \dfrac{t/(1+t)}{1 + t/(1+t)} = \dfrac{t}{1+2t} = t$ in characteristic $2$. So $\sigma$ has order $2$ and the action is faithful.

*Ramification.* $\sigma(t) - t = \dfrac{t - t(1+t)}{1+t} = \dfrac{-t^2}{1+t}$, so $i_G(\sigma) = v_t(\sigma(t)-t) = 2$, the lower jump is $\lambda_1 = i_G(\sigma) - 1 = 1$, and the different is
$$ d = (|G_0| - 1) + (|G_1| - 1) = 1 + 1 = 2 = (p-1)(\lambda_1+1). $$
Equivalently the extension $k[[t]]/k[[t]]^{G}$ is Artin–Schreier of conductor $2$.

**The lift.** Take $R = \mathbb{Z}_2 = W(k')$-flavoured base $W(k)$ (here $\mathbb{Z}_2$ suffices for the formulas) and define on $R[[T]]$
$$ \tilde{\sigma}(T) \;=\; \frac{-T}{1+T}. $$

*It is an involution:*
$$ \tilde{\sigma}^2(T) = \frac{-\big(-T/(1+T)\big)}{1 - T/(1+T)} = \frac{T/(1+T)}{1/(1+T)} = T . $$

*It reduces correctly:* modulo $2$, $-1 \equiv 1$, so $\tilde\sigma(T) \bmod 2 = T/(1+T) = \sigma(t)$.

*Fixed points on the generic fibre:*
$$ T = \frac{-T}{1+T} \iff T(1+T) = -T \iff T^2 + 2T = 0 \iff T \in \{0,\,-2\}. $$
Both lie in the open unit disc ($|0| = 0$, $|-2|_2 = 1/2 < 1$), so the lifted involution of the disc has **two** fixed points, which collide modulo $2$ into the single fixed point $t = 0$ of $\sigma$.

*Different check.* Each fixed point of an order-$2$ automorphism of the disc in characteristic $0$ contributes $1$ to the different of $R[[T]]/R[[T]]^{G}$, giving total $1 + 1 = 2$, exactly the special-fibre different $d = 2$ computed above. The Green–Matignon criterion is satisfied, and the Hurwitz tree here is the trivial tree with one vertex carrying two leaves at distance $v_2(2) = 1$.

**What the general conjecture adds.** For $\mathbb{Z}/p^n$ with jumps $\lambda_1 < \cdots < \lambda_n$, the different $\sum_i (p^{n-i+1}-1)(\lambda_i - \lambda_{i-1})$ must be distributed over a *tree* of coalescing branch points, and the residue conditions on the deformation data at each vertex must be solvable. The $p=2$, $n=1$, $\lambda_1=1$ case above is solvable by a single Möbius transformation; Obus–Wewers and Pop show solutions exist for every $n$ and every jump sequence.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*