---
id: 04-topology/lichtenbaum-quillen-conjecture
title: "Lichtenbaum-Quillen Conjecture"
topic: 04-topology
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Lichtenbaum-Quillen Conjecture

> **Topic:** Topology & Knot Theory · **ID:** `04-topology/lichtenbaum-quillen-conjecture` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

The Lichtenbaum–Quillen conjecture (LQC) asserts that algebraic $K$-theory with finite coefficients is computed by étale cohomology in high degrees.

Let $\ell$ be a prime, $X$ a nice scheme with $1/\ell \in \mathcal{O}_X$ and finite $\ell$-cohomological dimension $d = \mathrm{cd}_\ell(X)$. The conjecture states that the natural comparison map from algebraic to étale $K$-theory
$$\rho_n \colon K_n(X;\mathbb{Z}/\ell^\nu) \longrightarrow K_n^{\text{ét}}(X;\mathbb{Z}/\ell^\nu)$$
is an isomorphism for $n \geq d - 1$ and injective for $n = d - 2$. Equivalently, the descent spectral sequence
$$E_2^{s,t} = H^s_{\text{ét}}\big(X; \mathbb{Z}/\ell^\nu(t/2)\big) \Longrightarrow K_{t-s}(X;\mathbb{Z}/\ell^\nu)$$
converges to algebraic (not merely étale) $K$-theory in the range $t - s \geq d - 1$.

The canonical arithmetic case is $X = \operatorname{Spec}\mathcal{O}_F[1/\ell]$ for a number field $F$, where $d = 2$ for $\ell$ odd: then $K_n(\mathcal{O}_F[1/\ell];\mathbb{Z}/\ell^\nu)$ should be étale for all $n \geq 1$.

**Status.** Resolved. The conjecture follows from the Bloch–Kato/norm residue isomorphism, proved at $\ell = 2$ by Voevodsky (2003) and for all $\ell$ by Voevodsky (2011) using Rost's norm varieties, with the patching arguments completed by Haesemeyer–Weibel (2019). The reductions were supplied by Suslin–Voevodsky, Levine, Geisser–Levine and Thomason. The entry is retained because the *effective* and *integral* forms, and the higher chromatic analogues, remain open.

## 2. Mathematical Foundations

**Algebraic $K$-theory.** For a scheme $X$, Quillen's $K$-theory space is $K(X) = \Omega BQ\mathcal{P}(X)$; mod-$\ell^\nu$ groups are $K_n(X;\mathbb{Z}/\ell^\nu) = \pi_n(K(X)/\ell^\nu)$, homotopy of the cofiber of $\ell^\nu$.

**Étale $K$-theory.** Following Dwyer–Friedlander, $K^{\text{ét}}(X;\mathbb{Z}/\ell^\nu)$ is the homotopy limit of $K/\ell^\nu$ over the étale site — equivalently (Thomason) the Bott-inverted theory
$$K^{\text{ét}}(X;\mathbb{Z}/\ell^\nu) \simeq K(X;\mathbb{Z}/\ell^\nu)[\beta^{-1}],$$
where $\beta \in K_2(X;\mathbb{Z}/\ell^\nu)$ is the Bott element (for $\ell^\nu > 2$, after adjoining $\mu_{\ell^\nu}$). Thomason's theorem makes the "high degrees" clause precise: inverting $\beta$ only discards information below the cohomological dimension.

**Motivic reformulation (Beilinson–Lichtenbaum).** Let $H^{p,q}_{\mathcal{M}}(X;\mathbb{Z}/\ell)$ denote motivic cohomology. The Beilinson–Lichtenbaum conjecture $\mathrm{BL}(\ell)$ says
$$H^{p,q}_{\mathcal{M}}(X;\mathbb{Z}/\ell) \xrightarrow{\ \sim\ } H^p_{\text{ét}}\big(X;\mu_\ell^{\otimes q}\big) \quad \text{for } p \leq q,$$
with injectivity at $p = q+1$. Combined with the motivic Atiyah–Hirzebruch spectral sequence
$$E_2^{p,q} = H^{p-q}_{\mathcal{M}}\big(X;\mathbb{Z}/\ell(-q)\big) \Longrightarrow K_{-p-q}(X;\mathbb{Z}/\ell),$$
$\mathrm{BL}(\ell)$ implies LQC.

**Norm residue (Bloch–Kato).** For a field $F$ with $1/\ell \in F$, the Galois symbol
$$K^M_n(F)/\ell \xrightarrow{\ \sim\ } H^n_{\text{ét}}\big(F;\mu_\ell^{\otimes n}\big)$$
is an isomorphism for all $n \geq 0$. Suslin–Voevodsky (2000) proved $\mathrm{BK}(\ell) \Rightarrow \mathrm{BL}(\ell)$ (under resolution of singularities), with Geisser–Levine and Levine removing that hypothesis. Hence
$$\mathrm{BK}(\ell) \;\Longrightarrow\; \mathrm{BL}(\ell) \;\Longrightarrow\; \mathrm{LQC}(\ell).$$

**Arithmetic input.** For $R = \mathcal{O}_F[1/\ell]$, $\ell$ odd: $\mathrm{cd}_\ell(R) = 2$, $H^0(R;\mathbb{Z}_\ell(i)) = 0$ for $i \neq 0$, $H^1$ is finitely generated of rank $r_1 + r_2$ or $r_2$ (by parity of $i$), and $H^2$ is finite. Hence LQC predicts a two-column spectral sequence yielding
$$K_{2i-1}(R;\mathbb{Z}_\ell) \cong H^1(R;\mathbb{Z}_\ell(i)), \qquad K_{2i-2}(R;\mathbb{Z}_\ell) \cong H^2(R;\mathbb{Z}_\ell(i)), \quad i \geq 2.$$

## 3. History & State of the Art (SOTA)

- **1973.** Lichtenbaum, in *Values of zeta-functions, étale cohomology, and algebraic $K$-theory*, conjectures that special values $\zeta_F(1-i)$ are expressible via $K$-groups of $\mathcal{O}_F$, forcing a cohomological description of those groups.
- **1974/75.** Quillen, in his Vancouver ICM address, formulates the descent statement: a spectral sequence from étale cohomology converging to $K$-theory above the cohomological dimension. Quillen's computation $K_{2i-1}(\mathbb{F}_q) = \mathbb{Z}/(q^i-1)$ is the motivating example.
- **1983–85.** Suslin proves algebraic $K$-theory of algebraically closed fields with finite coefficients agrees with topological $K$-theory — the "base case" of descent. Dwyer–Friedlander construct $K^{\text{ét}}$ and verify LQC for local fields and for $\mathcal{O}_F[1/\ell]$ in special cases.
- **1985.** Thomason proves the Bott-inverted descent theorem: $K/\ell^\nu[\beta^{-1}] \simeq K^{\text{ét}}$. This converts LQC into the assertion "$\beta$ acts injectively/surjectively in high degrees".
- **1996–2003.** Voevodsky's motivic homotopy theory; proof of the Milnor conjecture ($\ell = 2$ Bloch–Kato), published in Publ. IHÉS 2003.
- **2000.** Rognes–Weibel compute the $2$-primary $K$-theory of $\mathcal{O}_F$ for totally real and other number fields, establishing LQC at $\ell = 2$ over number rings; this also settles the $2$-part of the Birch–Tate conjecture for abelian $F$ (with Mazur–Wiles and Kolster).
- **2003–2011.** Rost's norm varieties and chain lemma; Voevodsky's *On motivic cohomology with $\mathbb{Z}/\ell$-coefficients* (Annals, 2011) completes Bloch–Kato for all $\ell$. Haesemeyer–Weibel's 2019 monograph gives a complete, axiomatized account.
- **2020–21.** Clausen–Mathew reprove and vastly generalize étale descent (*Hyperdescent and étale $K$-theory*) using condensed/pro-étale methods, giving a proof independent of much of the motivic machinery in the finite-dimensionality setting.

## 4. Partial Results / Verified Cases

Cases established before, or independently of, the full Bloch–Kato proof:

- **Finite fields $\mathbb{F}_q$** ($\mathrm{cd}_\ell = 1$): Quillen (1972), $K_{2i-1}(\mathbb{F}_q) = \mathbb{Z}/(q^i-1)$, $K_{2i}(\mathbb{F}_q) = 0$; matches étale cohomology of $\operatorname{Spec}\mathbb{F}_q$ exactly.
- **Algebraically closed fields**: Suslin (1983, 1984), $K_*(\bar{F};\mathbb{Z}/\ell) \cong \pi_*(KU/\ell)$.
- **Local fields** and $\mathcal{O}_F[1/\ell]$ for $F$ abelian over $\mathbb{Q}$: Dwyer–Friedlander (1985); also Kahn's low-degree results ($n \le 3$, via $K_3^{\mathrm{ind}}$ and $H^3$).
- **$\ell = 2$, number rings**: Rognes–Weibel (JAMS 2000), all number fields $F$, all $n \geq 1$; Rognes–Østvær for two-regular fields with explicit group tables.
- **Characteristic $p$, $\ell = p$**: Geisser–Levine (2000), via Bloch–Kato–Gabber and de Rham–Witt; $K_n(F;\mathbb{Z}/p) \cong$ logarithmic de Rham–Witt cohomology.
- **Degree $n \leq 2$** of the norm residue map: Merkurjev–Suslin (1982) proved $\mathrm{BK}$ in weight $2$, giving LQC in low degrees for all $\ell$ and all fields.
- **Full statement, all $\ell$, all schemes of finite $\ell$-cohomological dimension over a field or a Dedekind domain**: consequence of Voevodsky (2011) + Rost + Suslin–Voevodsky + Levine + Thomason.

## 5. Principal Obstacles

Historically the barriers were, and for the remaining open forms still are:

- **No geometric model for descent.** $K$-theory is not a cohomology theory represented by a sheaf; étale descent fails outright in low degrees (e.g. $K_0(\mathbb{R}) = \mathbb{Z}$ vs. étale $K_0$ of $\operatorname{Spec}\mathbb{R}$ which sees $\mathbb{Z}/2$-Galois cohomology in all degrees). Any proof must locate the exact degree where failure stops, which classical spectral-sequence comparison cannot see.
- **Non-vanishing of higher Milnor $K$-theory.** Bloch–Kato in weight $n$ requires producing, for each nontrivial symbol, a *norm variety* — a smooth projective $X$ splitting the symbol with $\ell$-divisible degree-zero cycles. Rost's construction is an intricate induction on $n$ with no closed formula; each weight needs new geometry.
- **Failure of standard algebraic topology.** Adams-operation and Bott-periodicity arguments compute $K^{\text{ét}}$ but say nothing about $\rho_n$ being injective: they cannot detect the "non-Bott-torsion" classes that would obstruct descent.
- **Effectivity.** Even now, the proof gives no bound on the size of $H^2(\mathcal{O}_F[1/\ell];\mathbb{Z}_\ell(i))$, so $K_{4k+2}(\mathbb{Z})$ at odd primes is still tied to Vandiver's conjecture — which is verified computationally only for $\ell < 2^{31}$.
- **Higher chromatic analogues.** For $K(n)$-local or $\mathbb{E}_\infty$-ring-level statements (Ausoni–Rognes redshift), there is no analogue of étale cohomology to descend along; the "Galois theory" of ring spectra (Rognes) is only partially developed.

## 6. The Gap

The gap that was closed: Thomason reduced LQC to injectivity of the Bott map $\beta$ in high degrees; Suslin–Voevodsky reduced that to the Beilinson–Lichtenbaum comparison; Voevodsky reduced that to Bloch–Kato; and Bloch–Kato reduced to the existence of Rost varieties with prescribed characteristic numbers. The last step — Rost's degree formula and chain lemma, plus Voevodsky's motivic Margolis-homology argument on the symmetric-power motive $\check{C}(X)$ — is where the actual mathematical content sits.

The gaps that remain:
1. **Integral LQC.** With $\mathbb{Z}$-coefficients, the comparison $K_n(X) \to K_n^{\text{ét}}(X)$ is not an isomorphism (rationally it detects only Borel classes). No clean statement is known integrally.
2. **Effective bounds.** Converting the isomorphism into computable $K$-groups of $\mathbb{Z}$ at odd $\ell$ still requires Vandiver, i.e. $H^2(\mathbb{Z}[1/\ell];\mathbb{Z}_\ell(i)) = 0$ for $i$ even.
3. **Redshift/chromatic LQC.** Whether $K(R)$ for $R$ of telescopic complexity $n$ has telescopic complexity $n+1$ with an étale-type descent statement one chromatic level up.

## 7. Current Research (as of June 2026)

- **Descent via condensed and prismatic methods.** Clausen–Mathew (Invent. Math. 2021) prove étale hyperdescent for $K/\ell$ on qcqs schemes of finite valuative dimension, subsuming LQC; Bhatt–Clausen–Mathew (Selecta 2020) give a short $K(1)$-local proof. Groups at Copenhagen (Nikolaus), Bonn (Morrow, Scholze), Northwestern (Antieau) and Harvard/MIT (Mathew, Bhatt) drive this.
- **New motivic cohomology for singular and mixed-characteristic schemes.** Elmanto–Morrow and Bachmann–Elmanto–Morrow construct motivic cohomology for arbitrary qcqs schemes with an Atiyah–Hirzebruch spectral sequence into $K$-theory, extending the Beilinson–Lichtenbaum comparison outside the smooth case *(frontier — verify)*.
- **Syntomic cohomology at $\ell = p$.** Bhatt–Morrow–Scholze and Antieau–Mathew–Morrow–Nikolaus compute $K_*(\mathbb{Z}/p^n)$ and $p$-adic $K$-theory of $p$-adic rings, the characteristic-$p$-coefficient analogue of LQC.
- **Redshift.** Hahn–Wilson (Annals 2022) prove the Ausoni–Rognes redshift for $\mathrm{BP}\langle n\rangle$; Burklund–Schlank–Yuan's chromatic Nullstellensatz (arXiv:2207.09929) supplies the Galois-descent input. This is the current "higher LQC" frontier *(frontier — verify)*.
- **Trace methods.** Cyclotomic-trace comparisons ($K \to \mathrm{TC}$) of Dundas–Goodwillie–McCarthy type, refined by Clausen–Mathew–Morrow for henselian pairs, now give independent routes to the $\ell$-adic statements.

## 8. Future Work

- Make LQC effective: prove $H^2(\mathbb{Z}[1/\ell];\mathbb{Z}_\ell(2k)) = 0$, i.e. Vandiver, or find an unconditional bound on its order, to pin down $K_{4k+2}(\mathbb{Z})$.
- Extend Beilinson–Lichtenbaum to singular and mixed-characteristic schemes using the new motivic filtration (Elmanto–Morrow programme).
- Formulate and prove a $K(n)$-local Lichtenbaum–Quillen statement: identify the correct "étale site" for higher chromatic heights (Rognes' Galois theory of ring spectra).
- Reprove Bloch–Kato without Rost's norm varieties — a proof by pure descent/condensed methods would be a major simplification, as advocated by Weibel.
- Push the Lichtenbaum/Quillen zeta-value programme: unconditional special-value formulas for $\zeta_F(1-i)$ in terms of $\\#K_{2i-2}(\mathcal{O}_F)/\\#K_{2i-1}(\mathcal{O}_F)$ for non-abelian $F$.

## 9. Key References

- **[Foundational]** S. Lichtenbaum. *Values of zeta-functions, étale cohomology, and algebraic $K$-theory.* In Algebraic $K$-theory II, Lecture Notes in Math. 342, Springer, 1973, pp. 489–501. [DOI](https://doi.org/10.1007/bfb0073737)
- **[Foundational]** D. Quillen. *Higher algebraic $K$-theory.* Proc. Int. Congress of Mathematicians (Vancouver, 1974), Vol. 1, Canad. Math. Congress, 1975, pp. 171–176.
- **[Foundational]** R. W. Thomason. *Algebraic $K$-theory and étale cohomology.* Ann. Sci. École Norm. Sup. (4) 18 (1985), 437–552.
- **[Foundational]** W. Dwyer, E. Friedlander. *Algebraic and etale $K$-theory.* Trans. Amer. Math. Soc. 292 (1985), 247–280.
- **[Foundational]** A. Suslin. *On the $K$-theory of algebraically closed fields.* Invent. Math. 73 (1983), 241–245.
- **[Key step]** A. Suslin, V. Voevodsky. *Bloch–Kato conjecture and motivic cohomology with finite coefficients.* In The Arithmetic and Geometry of Algebraic Cycles, NATO Sci. Ser. C 548, Kluwer, 2000, pp. 117–189. [DOI](https://doi.org/10.1007/978-94-011-4098-0_5)
- **[Key step]** M. Levine. *Inverting the motivic Bott element.* $K$-Theory 19 (2000), 1–28. [DOI](https://doi.org/10.1023/a:1007874218371)
- **[Key step]** T. Geisser, M. Levine. *The Bloch–Kato conjecture and a theorem of Suslin–Voevodsky.* J. Reine Angew. Math. 530 (2001), 55–103. [DOI](https://doi.org/10.1515/crll.2001.006)
- **[SOTA]** V. Voevodsky. *Motivic cohomology with $\mathbb{Z}/2$-coefficients.* Publ. Math. Inst. Hautes Études Sci. 98 (2003), 59–104.
- **[SOTA]** V. Voevodsky. *On motivic cohomology with $\mathbb{Z}/l$-coefficients.* Ann. of Math. (2) 174 (2011), 401–438. [DOI](https://doi.org/10.4007/annals.2011.174.1.11)
- **[SOTA]** J. Rognes, C. Weibel. *Two-primary algebraic $K$-theory of rings of integers in number fields* (with an appendix by M. Kolster). J. Amer. Math. Soc. 13 (2000), 1–54. [DOI](https://doi.org/10.1090/s0894-0347-99-00317-3)
- **[SOTA / Recent]** D. Clausen, A. Mathew. *Hyperdescent and étale $K$-theory.* Invent. Math. 225 (2021), 981–1076. [DOI](https://doi.org/10.1007/s00222-021-01043-3)
- **[SOTA / Recent]** B. Bhatt, D. Clausen, A. Mathew. *Remarks on $K(1)$-local $K$-theory.* Selecta Math. (N.S.) 26 (2020), article 39.
- **[SOTA / Recent]** J. Hahn, D. Wilson. *Redshift and multiplication for truncated Brown–Peterson spectra.* Ann. of Math. (2) 196 (2022), 1277–1351. [DOI](https://doi.org/10.4007/annals.2022.196.3.6)
- **[Survey / Book]** C. Haesemeyer, C. Weibel. *The Norm Residue Theorem in Motivic Cohomology.* Annals of Mathematics Studies 200, Princeton Univ. Press, 2019. [DOI](https://doi.org/10.23943/princeton/9780691191041.001.0001)
- **[Survey]** C. Weibel. *Algebraic $K$-theory of rings of integers in local and global fields.* Handbook of $K$-theory, Vol. 1, Springer, 2005, pp. 139–190. [DOI](https://doi.org/10.1007/978-3-540-27855-9_5)
- **[Related]** B. Mazur, A. Wiles. *Class fields of abelian extensions of $\mathbb{Q}$.* Invent. Math. 76 (1984), 179–330. [DOI](https://doi.org/10.1007/bf01388599)

## 10. Worked Example / Concrete Special Case

**Goal:** compute the $3$-primary part of $K_3(\mathbb{Z})$ from étale cohomology, and check it against the classical answer $K_3(\mathbb{Z}) = \mathbb{Z}/48$.

Take $\ell = 3$ (a regular prime) and $R = \mathbb{Z}[1/3]$. Localization gives $K_n(\mathbb{Z};\mathbb{Z}_3) \cong K_n(R;\mathbb{Z}_3)$ for $n \geq 2$, since $K_*(\mathbb{F}_3)$ has no $3$-torsion.

**Step 1 — cohomological dimension.** $\mathrm{cd}_3(R) = 2$, so the descent spectral sequence has only columns $s = 0,1,2$:
$$E_2^{s,t} = H^s_{\text{ét}}\big(R;\mathbb{Z}_3(i)\big) \Longrightarrow K_{2i-s}(R;\mathbb{Z}_3), \qquad t = 2i.$$

**Step 2 — the columns.** $H^0(R;\mathbb{Z}_3(i)) = 0$ for $i \neq 0$ (no nontrivial invariants). Since $3$ is regular, Iwasawa theory (Mazur–Wiles) gives $H^2(R;\mathbb{Z}_3(i)) = 0$ for all $i$. So only $s = 1$ survives and LQC predicts
$$K_{2i-1}(\mathbb{Z};\mathbb{Z}_3) \cong H^1\big(\mathbb{Z}[1/3];\mathbb{Z}_3(i)\big), \qquad K_{2i-2}(\mathbb{Z};\mathbb{Z}_3) = 0 \ \ (i \ge 2).$$

**Step 3 — evaluate $H^1$ at $i = 2$.** For $i$ even, $H^1(\mathbb{Z}[1/\ell];\mathbb{Z}_\ell(i))$ is finite cyclic of order the $\ell$-part of
$$w_i(\mathbb{Q}) = \max\{ N : \operatorname{Gal}(\mathbb{Q}(\mu_N)/\mathbb{Q}) \text{ has exponent dividing } i \}.$$
Here $\ell \mid w_i$ iff $(\ell - 1) \mid i$, and then $v_\ell(w_i) = 1 + v_\ell(i)$. With $\ell = 3$, $i = 2$: $(3-1) \mid 2$ ✓ and $v_3(2) = 0$, so the $3$-part of $w_2$ is $3^1 = 3$. Indeed $w_2(\mathbb{Q}) = 24 = 2^3 \cdot 3$. Hence
$$H^1\big(\mathbb{Z}[1/3];\mathbb{Z}_3(2)\big) \cong \mathbb{Z}/3.$$

**Step 4 — read off the $K$-group.** With $2i - 1 = 3$:
$$K_3(\mathbb{Z};\mathbb{Z}_3) \cong \mathbb{Z}/3.$$

**Step 5 — check.** Lee–Szczarba computed $K_3(\mathbb{Z}) = \mathbb{Z}/48 = \mathbb{Z}/16 \oplus \mathbb{Z}/3$. The $3$-primary part is $\mathbb{Z}/3$. ✓ The $2$-primary part $\mathbb{Z}/16$ is likewise recovered by the $\ell = 2$ descent spectral sequence, where $\mathrm{cd}_2(\mathbb{Z}[1/2]) = 2$ is replaced by a real-place correction (Rognes–Weibel).

**What this illustrates.** The whole computation used only Galois cohomology of $\mathbb{Q}$ — no manifold, simplicial set, or general linear group. LQC is exactly the licence to make that substitution; before Voevodsky it was the missing justification, and Step 2's use of regularity is precisely the point where the *effective* form of the conjecture (Vandiver at general $\ell$) is still unresolved.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*