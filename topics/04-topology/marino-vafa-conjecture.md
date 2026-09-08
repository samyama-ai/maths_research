---
id: 04-topology/marino-vafa-conjecture
title: "Marino-Vafa Conjecture"
topic: 04-topology
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Mariño-Vafa Conjecture

> **Topic:** Topology & Knot Theory · **ID:** `04-topology/marino-vafa-conjecture` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

The Mariño–Vafa conjecture (2001) asserts a closed-form identity between two objects with no obvious relation:

- **Geometry side.** A generating function of *triple Hodge integrals* over the Deligne–Mumford moduli space $\overline{\mathcal M}_{g,n}$ of stable curves, depending on a partition $\mu$ and a framing parameter $\tau \in \mathbb{Q}$.
- **Combinatorics/physics side.** A finite sum of Chern–Simons quantum dimensions of $U(N)$ representations — the large-$N$ Chern–Simons invariant of the **unknot in $S^3$ with framing $\tau$**.

The conjecture arises from the Gopakumar–Vafa large-$N$ duality: $U(N)$ Chern–Simons theory on $S^3$ is equivalent to open topological string theory on the resolved conifold $\mathcal{O}(-1)^{\oplus 2}\to\mathbb{P}^1$ with a Lagrangian brane. Mariño and Vafa computed the brane amplitude in both frameworks and conjectured equality of the two answers.

A complete proof must establish the identity of formal power series in $\lambda$ and $p_1,p_2,\dots$ for **all** genera $g\ge 0$, **all** partitions $\mu$, and the framing parameter $\tau$ as a free variable. The conjecture is now a **theorem**: proved independently by Liu–Liu–Zhou (2003) and by Okounkov–Pandharipande (2004). What remains open is the surrounding program — the general-knot (LMOV) integrality statements it was a first instance of.

## 2. Mathematical Foundations

**Hodge and $\psi$ classes.** Let $\overline{\mathcal M}_{g,n}$ be the moduli stack of stable genus-$g$ curves with $n$ marked points, $\dim_{\mathbb C}=3g-3+n$. Let $\mathbb{E}\to\overline{\mathcal M}_{g,n}$ be the rank-$g$ Hodge bundle with Chern roots giving $\lambda_i=c_i(\mathbb{E})$, and $\psi_i=c_1(L_i)$ the cotangent class at the $i$-th point. Set the Chern polynomial

$$\Lambda_g^\vee(t)\;=\;t^g-\lambda_1 t^{g-1}+\lambda_2 t^{g-2}-\cdots+(-1)^g\lambda_g .$$

**Geometry side.** For a partition $\mu=(\mu_1\ge\cdots\ge\mu_{\ell})$ with $\ell=\ell(\mu)$, define

$$
\mathcal G_{g,\mu}(\tau)=-\frac{\sqrt{-1}^{\,|\mu|+\ell(\mu)}}{|\operatorname{Aut}(\mu)|}\,\big[\tau(\tau+1)\big]^{\ell(\mu)-1}
\prod_{i=1}^{\ell}\frac{\prod_{a=1}^{\mu_i-1}(\mu_i\tau+a)}{(\mu_i-1)!}
\int_{\overline{\mathcal M}_{g,\ell}}\frac{\Lambda_g^\vee(1)\,\Lambda_g^\vee(\tau)\,\Lambda_g^\vee(-\tau-1)}{\prod_{i=1}^{\ell}(1-\mu_i\psi_i)} ,
$$

with the unstable cases $(g,\ell)=(0,1),(0,2)$ fixed by the standard conventions $\mathcal G_{0,(\mu_1)}$ and $\mathcal G_{0,(\mu_1,\mu_2)}$ from localization. The generating function is

$$\mathcal G(\lambda;\tau;p)=\sum_{|\mu|\ge 1}\sum_{g\ge 0}\lambda^{2g-2+\ell(\mu)}\,\mathcal G_{g,\mu}(\tau)\,p_\mu,\qquad p_\mu=p_{\mu_1}\cdots p_{\mu_\ell},$$

and $\mathcal G^\bullet=\exp(\mathcal G)$ is the disconnected version.

**Representation-theory side.** Put $q=e^{\sqrt{-1}\lambda}$ and $[m]=q^{m/2}-q^{-m/2}$. For a partition $\nu$ let $\kappa_\nu=\sum_i \nu_i(\nu_i-2i+1)$ and let

$$\mathcal W_\nu(\lambda)=q^{\kappa_\nu/4}\prod_{x\in\nu}\frac{1}{[h(x)]}$$

be the Chern–Simons quantum dimension ($h(x)$ = hook length). Define

$$\mathcal R^\bullet(\lambda;\tau;p)=\sum_{\mu}\ \sum_{|\nu|=|\mu|}\frac{\sqrt{-1}^{\,\ell(\mu)}\chi_\nu(\mu)}{z_\mu}\,
e^{\sqrt{-1}\,(\tau+\frac12)\kappa_\nu\lambda/2}\,\mathcal W_\nu(\lambda)\,p_\mu ,$$

where $\chi_\nu$ is the irreducible $S_{|\mu|}$-character and $z_\mu=\prod_j j^{m_j}m_j!$.

**Mariño–Vafa formula.**
$$\boxed{\ \mathcal G^\bullet(\lambda;\tau;p)\;=\;\mathcal R^\bullet(\lambda;\tau;p)\ }$$

**Key structural tool.** Both sides satisfy the same *cut-and-join* equation in $\tau$:

$$\frac{\partial F^\bullet}{\partial\tau}=\frac{\sqrt{-1}\lambda}{2}\sum_{i,j\ge1}\Big[(i+j)\,p_ip_j\frac{\partial F^\bullet}{\partial p_{i+j}}+ij\,p_{i+j}\Big(\frac{\partial^2F^\bullet}{\partial p_i\partial p_j}+\frac{\partial F^\bullet}{\partial p_i}\frac{\partial F^\bullet}{\partial p_j}\Big)\Big].$$

Since this is a first-order ODE system in $\tau$ with polynomial coefficients, matching at one value of $\tau$ (plus a regularity/uniqueness argument) forces equality for all $\tau$.

## 3. History & State of the Art

- **1998–2000.** Faber–Pandharipande, *Hodge integrals and Gromov–Witten theory*, compute $\int \lambda_{g-1}$-type series via $\mathbb{C}^*$-localization on maps to $\mathbb{P}^1$; the $\lambda_g$ conjecture is stated.
- **2001.** ELSV formula relates single Hodge integrals $\Lambda_g^\vee(1)$ to Hurwitz numbers.
- **2000.** Ooguri–Vafa formulate knot invariants as open topological string amplitudes.
- **2001–2002.** M. Mariño and C. Vafa, *Framed knots at large $N$*, state the conjecture; framing $\tau$ enters as the integer/rational framing of the unknot, analytically continued.
- **2003.** C.-C. M. Liu, K. Liu, J. Zhou prove it by virtual localization on moduli of relative stable maps to a formal $\mathbb{P}^1$-geometry, deriving cut-and-join on both sides and matching initial data at $\tau=0$.
- **2004.** Okounkov–Pandharipande give a second proof via the GW/Hurwitz correspondence and the $\mathbb{C}^*$-equivariant theory of $\mathbb{P}^1$ relative to a point.
- **2006–2009.** Two-partition (Liu–Liu–Zhou, *JAMS*) and three-partition generalizations culminate in the proof of the **topological vertex** (Li–Liu–Liu–Zhou, *Geom. Topol.* 2009), the local-curve/local-surface engine of all-genus toric Calabi–Yau computations.

## 4. Partial Results / Verified Cases

- **$\mu=(1)$, all $g$.** Reduces to $\sum_{g\ge0}\lambda^{2g-1}\int_{\overline{\mathcal M}_{g,1}}\frac{\Lambda^\vee_g(1)\Lambda^\vee_g(\tau)\Lambda^\vee_g(-\tau-1)}{1-\psi_1}=\frac{1}{2\sin(\lambda/2)}$ — $\tau$-independent, proved by Faber–Pandharipande (2000) before the conjecture was stated. See §10.
- **$\tau=0$.** The formula degenerates to the **ELSV formula** ($\Lambda_g^\vee(1)$ integrals $=$ simple Hurwitz numbers), Ekedahl–Lando–Shapiro–Vainshtein 2001.
- **$\ell(\mu)=1$, arbitrary $\mu_1$ and $\tau$.** The one-hole amplitude; checked directly against $\mathcal W_{(\mu_1)}$ and $\mathcal W_{(1^{\mu_1})}$.
- **$g\le 2$, $|\mu|\le 4$.** Verified by explicit intersection numbers on $\overline{\mathcal M}_{g,n}$ (Zhou, 2003) before the general proof.
- **Corollaries proved as consequences.** The $\lambda_g$ conjecture,
$$\int_{\overline{\mathcal M}_{g,n}}\psi_1^{a_1}\cdots\psi_n^{a_n}\lambda_g=\binom{2g-3+n}{a_1,\dots,a_n}\frac{2^{2g-1}-1}{2^{2g-1}}\frac{|B_{2g}|}{(2g)!},\qquad \textstyle\sum a_i=2g-3+n,$$
and the $\lambda_g\lambda_{g-1}$ (Faber intersection) identities, both recovered as $\tau$-degree extremes of the Mariño–Vafa formula.
- **Generalizations proved.** Two-partition (2006) and three-partition/topological-vertex (2009) versions; the vertex gives all-genus GW invariants of every smooth toric Calabi–Yau threefold.

## 5. Principal Obstacles

The obstacles are why the conjecture resisted direct attack for two years, and why the surrounding program is still open.

- **Triple Hodge integrals are not determined by Mumford relations alone.** $\mathrm{ch}(\mathbb{E})$ relations give $\Lambda_g^\vee(t)\Lambda_g^\vee(-t)=(-1)^g t^{2g}$, which handles *pairs* of $\Lambda^\vee$ factors. The product $\Lambda_g^\vee(1)\Lambda_g^\vee(\tau)\Lambda_g^\vee(-\tau-1)$ has three factors with $1+\tau+(-\tau-1)=0$; this Calabi–Yau condition is exactly what localization on a threefold produces, but no purely tautological-ring argument evaluates it.
- **No compact target.** The physical geometry is a Lagrangian brane in $T^*S^3$ / the resolved conifold — an *open* string background. Open Gromov–Witten invariants with Lagrangian boundary have no general algebraic definition; one must invent a torus-equivariant *formal* relative geometry whose localization contributions reproduce the desired integrals.
- **Framing is not a geometric parameter.** $\tau$ appears in Chern–Simons theory as an integer framing shift, but the Hodge-integral side needs it as a formal variable. Any proof must analytically continue in $\tau$, which rules out naive term-by-term matching at integer values.
- **Infinitely many unknowns at each order.** Both sides mix all genera and all partition lengths; there is no finiteness making the identity a check on finitely many numbers. The resolution — that both sides solve the same cut-and-join ODE — required recognizing an $S_n$-symmetric-function structure not visible in either original formulation.

## 6. The Gap

For the conjecture itself, the gap is closed: the ODE argument plus the $\tau=0$ initial condition is a complete proof. The residual gap is in the program the conjecture opened:

- **From the unknot to general knots.** The Mariño–Vafa formula is the framed *unknot* case. The **LMOV (Labastida–Mariño–Ooguri–Vafa) integrality conjecture** — that reformulated colored HOMFLY-PT invariants of an arbitrary knot $K$ have integer BPS expansion coefficients $N_{\nu,g,Q}\in\mathbb{Z}$ — is open in general. Proved: integrality of the *first* reformulated invariants (Kontsevich–Schwarz–Vologodsky-type arguments; Liu–Peng 2010 for a large class), torus knots (Kucharski–Sułkowski and others).
- **Geometric interpretation.** No construction assigns to a general knot $K\subset S^3$ a Lagrangian $L_K\subset T^*S^3$ together with a rigorously defined open GW theory whose invariants are the HOMFLY-PT colored polynomials. Ekholm–Shende's skein-valued curve counting (2019–2023) is the most advanced attempt.

## 7. Current Research (as of June 2026)

- **Skein-valued open GW.** Ekholm–Shende's *skein-valued curve counting* and the "HOMFLY skein of the brane" program give a rigorous framework in which the Mariño–Vafa amplitude is a skein-module element; the framed-unknot case is recovered and general knots are being pushed through. *(frontier — verify)*
- **Topological recursion.** Eynard–Orantin recursion applied to the mirror curve $e^u+e^v=1$ reproduces the Mariño–Vafa amplitudes; the Bouchard–Klemm–Mariño–Pasquetti "remodeling conjecture" was proved for toric CY3 by Fang–Liu–Zong (2020), placing the framed-vertex amplitudes in a spectral-curve framework.
- **Knots-quivers correspondence.** Kucharski–Reineke–Stošić–Sułkowski relate LMOV integrality to Donaldson–Thomas invariants of symmetric quivers; active at IFT Warsaw, Caltech, Uppsala. *(frontier — verify)*
- **Groups.** Columbia (C.-C. M. Liu), Tsinghua/YMSC (K. Liu, J. Zhou circle), Caltech/Uppsala (Ekholm, Shende, Sułkowski), IHES/Saclay (Eynard).

## 8. Future Work

- Prove LMOV integrality for all knots by constructing the BPS counting as an honest moduli-theoretic Euler characteristic.
- Extend the formula to **orbifold** and **open crepant resolution** settings ($[\mathbb{C}^3/\mathbb{Z}_n]$ vertices with framing).
- Find a purely algebro-geometric derivation of the triple-Hodge evaluation that does not route through cut-and-join, which would likely generalize to $\Lambda^\vee$-products with $k>3$ factors.
- Categorify: match the $\tau$-framing dependence with the grading shifts in HOMFLY-PT homology.

## 9. Key References

- **[Foundational]** M. Mariño, C. Vafa. *Framed knots at large $N$.* In *Orbifolds in Mathematics and Physics*, Contemp. Math. **310**, AMS, 2002, pp. 185–204.
- **[Foundational]** C. Faber, R. Pandharipande. *Hodge integrals and Gromov–Witten theory.* Inventiones Mathematicae **139** (2000), 173–199. [DOI](https://doi.org/10.1007/s002229900028)
- **[Foundational]** T. Ekedahl, S. Lando, M. Shapiro, A. Vainshtein. *Hodge integrals and Hurwitz numbers.* Inventiones Mathematicae **146** (2001), 297–327.
- **[Proof]** C.-C. M. Liu, K. Liu, J. Zhou. *A proof of a conjecture of Mariño–Vafa on Hodge integrals.* Journal of Differential Geometry **65** (2003), no. 2, 289–340. [DOI](https://doi.org/10.4310/jdg/1090511689)
- **[Proof]** A. Okounkov, R. Pandharipande. *Hodge integrals and invariants of the unknot.* Geometry & Topology **8** (2004), 675–699. [DOI](https://doi.org/10.2140/gt.2004.8.675)
- **[SOTA]** J. Li, C.-C. M. Liu, K. Liu, J. Zhou. *A mathematical theory of the topological vertex.* Geometry & Topology **13** (2009), 527–621. [DOI](https://doi.org/10.2140/gt.2009.13.527)
- **[SOTA]** C.-C. M. Liu, K. Liu, J. Zhou. *A formula of two-partition Hodge integrals.* Journal of the AMS **20** (2007), 149–184. [DOI](https://doi.org/10.1090/s0894-0347-06-00541-8)
- **[Physics origin]** H. Ooguri, C. Vafa. *Knot invariants and topological strings.* Nuclear Physics B **577** (2000), 419–438. [DOI](https://doi.org/10.1016/s0550-3213(00)00118-8)
- **[Physics origin]** M. Aganagic, A. Klemm, M. Mariño, C. Vafa. *The topological vertex.* Communications in Mathematical Physics **254** (2005), 425–478. [DOI](https://doi.org/10.1093/acprof:oso/9780198568490.003.0009)
- **[Survey]** C.-C. M. Liu, K. Liu, J. Zhou. *Mariño–Vafa formula and Hodge integral identities.* Journal of Algebraic Geometry **15** (2006), 379–398. [DOI](https://doi.org/10.1090/s1056-3911-05-00419-4)
- **[Survey]** M. Mariño. *Chern–Simons Theory, Matrix Models, and Topological Strings.* Oxford University Press, 2005.

## 10. Worked Example / Concrete Special Case

Take $\mu=(1)$, so $|\mu|=1$, $\ell(\mu)=1$, $\operatorname{Aut}(\mu)$ trivial. All prefactors collapse: $\sqrt{-1}^{\,|\mu|+\ell(\mu)}=\sqrt{-1}^{\,2}=-1$, $[\tau(\tau+1)]^{0}=1$, the product $\prod_{a=1}^{0}$ is empty, $(\mu_1-1)!=1$. Hence

$$\mathcal G_{g,(1)}(\tau)=\int_{\overline{\mathcal M}_{g,1}}\frac{\Lambda_g^\vee(1)\Lambda_g^\vee(\tau)\Lambda_g^\vee(-\tau-1)}{1-\psi_1}.$$

**Genus 1.** $\overline{\mathcal M}_{1,1}$ has dimension $1$ and $\Lambda_1^\vee(t)=t-\lambda_1$. Expand the numerator, keeping only degrees $0$ and $1$:

$$(1-\lambda_1)(\tau-\lambda_1)(-\tau-1-\lambda_1)=\underbrace{-\tau(\tau+1)}_{\deg 0}+\underbrace{\lambda_1(\tau^2+\tau+1)}_{\deg 1}+O(\lambda_1^2).$$

Since $\frac{1}{1-\psi_1}=1+\psi_1+\cdots$, the degree-$1$ part of the integrand is $-\tau(\tau+1)\psi_1+(\tau^2+\tau+1)\lambda_1$. Using $\int_{\overline{\mathcal M}_{1,1}}\psi_1=\int_{\overline{\mathcal M}_{1,1}}\lambda_1=\tfrac1{24}$:

$$\mathcal G_{1,(1)}(\tau)=\tfrac{1}{24}\big(-\tau^2-\tau\big)+\tfrac1{24}\big(\tau^2+\tau+1\big)=\tfrac{1}{24}.$$

The framing dependence cancels exactly — a nontrivial consistency check.

**The right-hand side.** For $|\mu|=1$ the only $\nu$ with $|\nu|=1$ is $\nu=(1)$: $\chi_{(1)}((1))=1$, $z_{(1)}=1$, $\kappa_{(1)}=0$ (so the framing exponential is $1$, matching the cancellation above), and $\mathcal W_{(1)}(\lambda)=1/[1]=1/(q^{1/2}-q^{-1/2})$. With $q=e^{\sqrt{-1}\lambda}$,

$$\sqrt{-1}\,\mathcal W_{(1)}(\lambda)=\frac{\sqrt{-1}}{2\sqrt{-1}\sin(\lambda/2)}=\frac{1}{2\sin(\lambda/2)} .$$

**Matching.** The conjecture at order $p_1$ reads $\sum_{g\ge0}\lambda^{2g-1}\mathcal G_{g,(1)}(\tau)=\dfrac{1}{2\sin(\lambda/2)}$. Expanding,

$$\frac{1}{2\sin(\lambda/2)}=\frac1\lambda+\frac{\lambda}{24}+\frac{7\lambda^3}{5760}+\frac{31\lambda^5}{967680}+\cdots$$

The $\lambda^{-1}$ coefficient is $\mathcal G_{0,(1)}=1$ (the unstable convention), and the $\lambda^{1}$ coefficient is $\tfrac1{24}$ — exactly the genus-1 computation above. The formula further predicts

$$\int_{\overline{\mathcal M}_{2,1}}\frac{\Lambda_2^\vee(1)\Lambda_2^\vee(\tau)\Lambda_2^\vee(-\tau-1)}{1-\psi_1}=\frac{7}{5760}\quad\text{for every }\tau,$$

which agrees with the Faber–Pandharipande evaluation using $\int_{\overline{\mathcal M}_{2,1}}\psi_1\lambda_2 = \tfrac{1}{5760}$ and $\int_{\overline{\mathcal M}_2}\lambda_1^3=\tfrac{1}{2880}$. This one-hole case is the seed initial condition from which the cut-and-join equation propagates the full identity.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*