---
id: 02-algebra-group-theory/adams-barbasch-vogan-conjecture
title: "Adams-Barbasch-Vogan Conjecture"
topic: 02-algebra-group-theory
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Adams-Barbasch-Vogan Conjecture

> **Topic:** Algebra & Group Theory · **ID:** `02-algebra-group-theory/adams-barbasch-vogan-conjecture` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Arthur's conjectures attach to each *Arthur parameter* $\psi$ of a reductive group $G$ over a local field a finite set $\Pi_\psi$ of irreducible admissible representations — an **Arthur packet** — characterized globally, by the trace formula. Adams, Barbasch and Vogan (ABV) gave a purely local, geometric construction of a candidate packet $\Pi^{\mathrm{ABV}}_\psi$ using characteristic cycles of equivariant perverse sheaves on a space of Langlands parameters.

**Conjecture (ABV, 1992; Conj. 1.19 and Ch. 22 of their book).** For a real reductive group $G(\mathbb{R})$, a strong real form of a connected reductive $\mathbb{C}$-group, and every Arthur parameter $\psi$,
$$\Pi^{\mathrm{ABV}}_\psi \;=\; \Pi^{\mathrm{Arthur}}_\psi ,$$
with matching pairings $\langle \cdot,\pi\rangle$ of the packet against the component group $A_\psi$, so that the ABV-defined virtual character
$$\eta^{\mathrm{mic}}_\psi \;=\; \sum_{\pi \in \Pi^{\mathrm{ABV}}_\psi} (-1)^{d(\pi)-d(\psi)}\,\langle 1,\pi\rangle\,\Theta_\pi$$
is the stable distribution predicted by Arthur, and the twisted characters $\eta^{\mathrm{mic}}_\psi(s)$ for $s \in A_\psi$ are the endoscopic transfers.

A complete resolution requires, for every real form and every $\psi$: (i) equality of the two finite sets of representations, (ii) equality of the associated pairings with $A_\psi$, and (iii) compatibility with endoscopic transfer. The analogous statement over $p$-adic fields is **Vogan's conjecture**, and is now proved in some families.

## 2. Mathematical Foundations

Let $G$ be connected reductive over $\mathbb{R}$ with complex dual group ${}^\vee G$ and $L$-group ${}^\vee G^\Gamma = {}^\vee G \rtimes \Gamma$, $\Gamma = \mathrm{Gal}(\mathbb{C}/\mathbb{R})$.

**Geometric parameter space.** Fix a semisimple infinitesimal character $\lambda \in {}^\vee\mathfrak{g}$. ABV replace Langlands parameters $\phi: W_\mathbb{R} \to {}^\vee G^\Gamma$ by *geometric parameters*: the smooth complex variety
$$X = X(\lambda, {}^\vee G^\Gamma) = \{\, y \in {}^\vee G^\Gamma \setminus {}^\vee G \;:\; y^2 = \exp(2\pi i \lambda),\ \mathrm{Ad}(y)\lambda = \lambda \,\}\big/\!\sim ,$$
carried with an algebraic action of the centralizer $H = {}^\vee G(\lambda)$, having **finitely many orbits**. A *complete geometric parameter* is a pair $\xi = (S, \mathcal{V})$: an $H$-orbit $S \subset X$ and an irreducible $H$-equivariant local system $\mathcal{V}$ on $S$. The Local Langlands Correspondence in this form:
$$\{\text{complete geometric parameters at }\lambda\} \;\longleftrightarrow\; \{\text{irreducible reps of infinitesimal character }\lambda \text{ over all strong real forms}\}, \qquad \xi \mapsto \pi(\xi),$$
with standard modules $M(\xi)$ dual to the standard perverse extensions and irreducibles $\pi(\xi)$ dual to $P(\xi) = IC(S,\mathcal{V})$.

**Microlocal multiplicities.** For a perverse sheaf $P$ on $X$ the characteristic cycle is
$$CC(P) \;=\; \sum_{S} \chi^{\mathrm{mic}}_{S}(P)\,\big[\overline{T^*_S X}\big] \in H^{BM}_{2\dim X}(T^*X), \qquad \chi^{\mathrm{mic}}_S(P) \in \mathbb{Z}_{\ge 0},$$
the sum over $H$-orbits, $\overline{T^*_S X}$ the closure of the conormal bundle. Kashiwara's index theorem makes $\chi^{\mathrm{mic}}$ computable as a local Euler characteristic of vanishing cycles at a generic covector.

**Arthur parameters and micropackets.** An Arthur parameter is a homomorphism
$$\psi : W_\mathbb{R} \times \mathrm{SL}(2,\mathbb{C}) \longrightarrow {}^\vee G^\Gamma$$
with $\psi|_{W_\mathbb{R}}$ bounded and $\psi|_{\mathrm{SL}_2}$ algebraic; its Langlands parameter is $\phi_\psi(w) = \psi\!\left(w, \begin{pmatrix} |w|^{1/2} & 0\\ 0 & |w|^{-1/2}\end{pmatrix}\right)$, with component group $A_\psi = \pi_0\!\big(Z_{{}^\vee G}(\psi)\big)$. Let $S_\psi \subset X$ be the orbit of $\phi_\psi$. ABV define
$$\Pi^{\mathrm{ABV}}_\psi \;=\; \big\{\, \pi(\xi) \;:\; \chi^{\mathrm{mic}}_{S_\psi}\big(P(\xi)\big) \neq 0 \,\big\},$$
the **micropacket** attached to $S_\psi$: the set of irreducibles whose IC sheaf has the conormal variety of $S_\psi$ in its singular support. The pairing with $A_\psi$ is read off from the microlocal multiplicity as an $A_\psi$-equivariant local system on $T^*_{S_\psi}X$. Since $\chi^{\mathrm{mic}}_{S_\psi}(P(\xi_\psi)) = 1$, always $\Pi_{\phi_\psi} \cap \Pi^{\mathrm{ABV}}_\psi \ni \pi(\xi_\psi)$, and $\Pi^{\mathrm{ABV}}_\psi \supseteq \Pi_{\phi_\psi}$ is expected but not automatic.

## 3. History & State of the Art (SOTA)

- **1983–89.** Arthur formulates the conjectures on unipotent automorphic representations (*Astérisque* 171–172, 1989), predicting non-tempered packets and a stable distribution attached to each $\psi$.
- **1985.** Barbasch–Vogan compute unipotent representations of complex groups and identify associated varieties/wavefront sets as the right invariants.
- **1987.** Adams–Johnson construct packets for a restricted class of real $\psi$ out of cohomologically induced modules $A_{\mathfrak{q}}(\lambda)$, and verify endoscopic character identities for them.
- **1992.** ABV's book supplies the geometric parametrization, defines micropackets, and *proves* on the geometric side: the stability of $\eta^{\mathrm{mic}}_\psi$ and the endoscopic lifting identities for these microlocally defined virtual characters. What is left open is the identification with Arthur's packets.
- **2013.** Arthur's endoscopic classification for quasisplit symplectic/orthogonal groups gives $\Pi_\psi$ its trace-formula existence for classical groups over all local fields, making the comparison a well-posed problem.
- **2018–2022.** Arancibia–Moeglin–Renard identify Adams–Johnson packets with Arthur packets and with ABV packets for real classical groups; Cunningham–Fiori–Moussaoui–Mracek–Xu port the whole microlocal construction to $p$-adic groups (Vogan's conjecture); Cunningham–Ray prove it for irreducible parameters of $p$-adic $\mathrm{GL}_n$.
- **Computation.** The Atlas of Lie Groups software computes characteristic cycles and ABV packets for arbitrary real forms at given infinitesimal character; this is the main empirical instrument.

## 4. Partial Results / Verified Cases

- **Tempered $\psi$** ($\psi|_{\mathrm{SL}_2}$ trivial): $S_\psi$ is open in its closure component and $\Pi^{\mathrm{ABV}}_\psi = \Pi_{\phi_\psi}$, the tempered $L$-packet. Proved in ABV (1992), consistent with Shelstad's real endoscopy.
- **Adams–Johnson parameters** (real classical groups; $\psi|_{W_\mathbb{R}}$ with image in a torus, $\phi_\psi$ of regular integral infinitesimal character, packet built from $A_{\mathfrak{q}}(\lambda)$'s attached to $\theta$-stable parabolics): $\Pi^{\mathrm{AJ}}_\psi = \Pi^{\mathrm{ABV}}_\psi = \Pi^{\mathrm{Arthur}}_\psi$ — Arancibia–Moeglin–Renard (2018) for $\mathrm{Sp}(2n,\mathbb{R})$, quasisplit $\mathrm{SO}(p,q)$, $U(p,q)$; extended by Adams–Arancibia–Mezo (arXiv:2108.05788) to all real classical groups with matching $A_\psi$-pairings.
- **Complex groups viewed as real groups:** Arthur packets for $\mathrm{Res}_{\mathbb{C}/\mathbb{R}}G$ are singletons or explicitly known (Barbasch–Vogan 1985; Moeglin–Renard, *Contemp. Math.* 691, 2017), and agree with micropackets.
- **$\mathrm{GL}(n,\mathbb{R})$, $\mathrm{GL}(n,\mathbb{C})$:** all packets are singletons; equality is immediate. Over $p$-adic fields, Cunningham–Ray prove $\Pi^{\mathrm{ABV}}_\psi = \Pi_\psi$ for $\mathrm{GL}_n$ when $\phi_\psi$ is irreducible.
- **Low rank:** $\mathrm{SL}(2,\mathbb{R})$, $\mathrm{PGL}(2,\mathbb{R})$, $\mathrm{Sp}(4,\mathbb{R})$, $\mathrm{SO}(3,2)$, $U(2,1)$, $U(2,2)$ verified by explicit character computation; $p$-adic $G_2$ unipotent packets computed by Cunningham–Fiori–Xu (*Adv. Math.* 395, 2022).
- **Endoscopic side:** Mezo (*Memoirs AMS* 222, 2013) proves the twisted character identities for real groups needed to compare $\eta^{\mathrm{mic}}_\psi$ with the twisted transfer from $\mathrm{GL}_N$.

## 5. Principal Obstacles

- **Two incompatible definitions.** $\Pi_\psi$ is defined by a *global* mechanism (twisted trace formula, stabilization, spectral transfer from $\mathrm{GL}_N$), $\Pi^{\mathrm{ABV}}_\psi$ by *local* sheaf geometry. There is no dictionary translating one into the other directly; all proofs proceed by computing both sides in a family and comparing.
- **Characteristic cycles are not computable in closed form.** $\chi^{\mathrm{mic}}_S(IC(\overline{S'}))$ is not determined by Kazhdan–Lusztig polynomials: for singular orbit closures the cycles can acquire unexpected components (the Kashiwara–Saito phenomenon in type $A_7$), and no combinatorial rule is known in general. Algorithms exist but are exponential; Atlas computations stall well below the ranks where new behaviour is expected.
- **Failure of Adams–Johnson methods outside regular integral $\lambda$.** Cohomological induction produces packets only when $\phi_\psi$ has regular infinitesimal character; genuinely unipotent $\psi$ (singular $\lambda$, non-special nilpotent orbits) fall outside, and the corresponding representations are not $A_{\mathfrak{q}}(\lambda)$-modules.
- **Non-quasisplit forms.** Arthur's classification is stated for quasisplit groups; over inner forms the packets are only defined conditionally, whereas $\Pi^{\mathrm{ABV}}_\psi$ is defined uniformly over all strong real forms at once. The comparison then has no fixed target.
- **Sign and normalization bookkeeping.** The pairing $\langle s,\pi\rangle$ depends on Whittaker normalizations, choices of splittings and transfer factors; even where both sets coincide, matching pairings has required substantial extra work.

## 6. The Gap

Proved: equality for tempered parameters, for Adams–Johnson parameters over real classical groups, for complex groups, for $\mathrm{GL}_n$, and in explicitly computed low-rank cases. Unproved: parameters $\psi$ whose $\mathrm{SL}(2)$-part is non-trivial and for which $\phi_\psi$ has **singular or non-integral infinitesimal character**, exceptional groups $G_2, F_4, E_{6,7,8}$ over $\mathbb{R}$, and non-quasisplit inner forms. The precise missing step is a **local characterization theorem**: a proof that the stable virtual character $\eta^{\mathrm{mic}}_\psi$ constructed microlocally is *the* stable distribution whose twisted transfer to $\mathrm{GL}_N$ is the character of the Speh-type representation attached to $\psi$ — without passing through a global argument. Equivalently, one needs to show the microlocal multiplicity matrix $\big(\chi^{\mathrm{mic}}_{S_\psi}(P(\xi))\big)$ is computed by the same unitriangular matrix that governs Arthur's spectral transfer.

## 7. Current Research (as of June 2026)

- **The Cunningham school (Calgary/Voganish project).** Systematic development of ABV packets for $p$-adic groups: vanishing-cycle functors on Vogan varieties, "open" and "unipotent" parameter families, and software (`Voganish`) for computing microlocal multiplicities. Recent output includes ABV packets for $p$-adic $\mathrm{Sp}(4)$, $G_2$ and classification of parameters for which packets are singletons. *(frontier — verify)*
- **Adams–Arancibia–Mezo–Vogan circle.** Comparison for real classical groups beyond AJ parameters, and packets at singular infinitesimal character via translation functors and the Atlas software.
- **Moeglin–Renard.** Explicit constructions of real Arthur packets from Moeglin's $p$-adic construction, and irreducibility/multiplicity-one statements for the constituents.
- **Unipotent representations.** Work of Barbasch, Ma, Sun, Vogan and Losev–Mason-Brown–Matvieievskyi on unipotent representations attached to nilpotent orbits with the expected associated varieties gives independent access to the constituents of unipotent $\Pi_\psi$. *(frontier — verify)*
- **Local Arthur packets as local objects.** Attempts to characterize $\Pi_\psi$ by twisted endoscopic character relations alone (Mezo; Xu for classical groups) — this is the route that would close the gap in Section 6.

## 8. Future Work

1. Prove a local, purely character-theoretic characterization of Arthur packets for real groups; combine with ABV's proven stability/endoscopy statements to conclude equality.
2. Develop a combinatorial calculus for $\chi^{\mathrm{mic}}$ on geometric parameter spaces — a microlocal analogue of Kazhdan–Lusztig theory — bypassing exponential cycle computations.
3. Settle the singular-infinitesimal-character case via translation-functor arguments, where $A_\psi$-pairings can degenerate.
4. Complete the exceptional real groups by Atlas-driven computation, targeting split $G_2(\mathbb{R})$ and $F_4$ unipotent packets first.
5. Extend the comparison to non-quasisplit inner forms, where ABV packets are defined but Arthur's are not, thereby *defining* Arthur packets microlocally.

## 9. Key References

- **[Foundational]** J. Adams, D. Barbasch, D. A. Vogan Jr. *The Langlands Classification and Irreducible Characters for Real Reductive Groups.* Progress in Mathematics 104, Birkhäuser, 1992.
- **[Foundational]** J. Arthur. *Unipotent automorphic representations: conjectures.* Astérisque 171–172 (1989), 13–71.
- **[Foundational]** J. Adams, J. Johnson. *Endoscopic groups and packets of non-tempered representations.* Compositio Mathematica 64 (1987), 271–309.
- **[Foundational]** D. Barbasch, D. A. Vogan Jr. *Unipotent representations of complex semisimple groups.* Annals of Mathematics 121 (1985), 41–110.
- **[Foundational]** M. Kashiwara. *Index theorem for constructible sheaves.* Astérisque 130 (1985), 193–209.
- **[SOTA]** J. Arthur. *The Endoscopic Classification of Representations: Orthogonal and Symplectic Groups.* AMS Colloquium Publications 61, 2013.
- **[SOTA]** N. Arancibia, C. Moeglin, D. Renard. *Paquets d'Arthur des groupes classiques et unitaires.* Annales de la Faculté des Sciences de Toulouse 27 (2018), 1023–1105.
- **[SOTA]** J. Adams, N. Arancibia Robert, P. Mezo. *Equivalent definitions of Arthur packets for real classical groups.* arXiv:2108.05788, 2021.
- **[SOTA]** C. Cunningham, A. Fiori, A. Moussaoui, J. Mracek, B. Xu. *Arthur packets for $p$-adic groups by way of microlocal vanishing cycles of perverse sheaves, with examples.* Memoirs of the AMS 276 (2022), no. 1353.
- **[SOTA]** C. Cunningham, M. Ray. *Proof of Vogan's conjecture on Arthur packets: irreducible parameters of $p$-adic general linear groups.* arXiv:2206.01027, 2022.
- **[SOTA]** C. Cunningham, A. Fiori, B. Xu. *Arthur packets for $G_2$ and perverse sheaves on cubics.* Advances in Mathematics 395 (2022), 108074.
- **[Survey]** D. A. Vogan Jr. *The local Langlands conjecture.* In *Representation Theory of Groups and Algebras*, Contemporary Mathematics 145, AMS, 1993, 305–379.
- **[Survey]** P. Mezo. *Character identities in the twisted endoscopy of real reductive groups.* Memoirs of the AMS 222 (2013), no. 1042.
- **[Computational]** J. Adams, M. van Leeuwen, P. Trapa, D. A. Vogan Jr. *Unitary representations of real reductive groups.* Astérisque 417 (2020).

## 10. Worked Example / Concrete Special Case

**How a micropacket becomes larger than an $L$-packet.** The mechanism is entirely local geometry: a singular orbit closure whose IC sheaf has a reducible characteristic cycle.

Take the model geometry of a flag variety $X = \mathcal{B}$ for $\mathrm{SL}(4,\mathbb{C})$ with the Bruhat stratification by $B$-orbits $C_w$, $w \in S_4$ ($\dim C_w = \ell(w)$). Let $w = s_2 s_1 s_3 s_2$, $\ell(w) = 4$. The Schubert variety $\overline{C_w}$ is singular exactly along the point stratum $C_e$, and the Kazhdan–Lusztig polynomial is
$$P_{e,w}(q) = 1 + q .$$
The corresponding characteristic cycle is
$$CC\big(IC(\overline{C_w})\big) = \big[\overline{T^*_{C_w} X}\big] \;+\; \big[\overline{T^*_{C_e} X}\big],$$
so $\chi^{\mathrm{mic}}_{C_e}\big(IC(\overline{C_w})\big) = 1 \neq 0$, while trivially $\chi^{\mathrm{mic}}_{C_e}\big(IC(\overline{C_e})\big) = 1$.

Transporting this to a geometric parameter space $X(\lambda,{}^\vee G^\Gamma)$ with orbits $S_\psi$ (closed, playing the role of $C_e$) and $S'$ (playing the role of $C_w$), the micropacket is
$$\Pi^{\mathrm{ABV}}_\psi = \{\pi(\xi_\psi),\ \pi(\xi')\},$$
two elements, whereas the $L$-packet $\Pi_{\phi_\psi} = \{\pi(\xi_\psi)\}$ has one. The virtual character
$$\eta^{\mathrm{mic}}_\psi = \Theta_{\pi(\xi_\psi)} + (-1)^{\dim S' - \dim S_\psi}\,\Theta_{\pi(\xi')}$$
is stable, while the individual characters are not: the two summands' unstable parts cancel.

This is exactly the shape of the smallest genuine real-group instance, the Saito–Kurokawa parameter for $\mathrm{Sp}(4,\mathbb{R})$ (equivalently $\mathrm{SO}(3,2)$): $\psi = \phi_\tau \oplus (\mathbf{1}\boxtimes S_2)$ into ${}^\vee G = \mathrm{SO}(5,\mathbb{C})$, with $\phi_\tau$ a $2$-dimensional discrete parameter. Here $A_\psi \cong \mathbb{Z}/2$ and $|\Pi_\psi| = 2$: one non-tempered Langlands quotient (the $\langle 1,\cdot\rangle = +1$ member, which alone lies in $\Pi_{\phi_\psi}$) and one limit of discrete series contributed by the extra conormal component (pairing $-1$). The Howe–Piatetski-Shapiro non-tempered cusp forms realize this packet automorphically, and ABV's construction reproduces it microlocally — the case verified by hand and by Atlas, and the template for the general conjecture.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*