---
id: 03-geometry/gudkov-conjecture
title: "Gudkov Conjecture"
topic: 03-geometry
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Gudkov Conjecture

> **Topic:** Algebraic & Differential Geometry · **ID:** `03-geometry/gudkov-conjecture` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

Let $A \subset \mathbb{CP}^2$ be a nonsingular real plane algebraic curve of even degree $m = 2k$, and let $\mathbb{R}A \subset \mathbb{RP}^2$ be its real point set — a disjoint union of $l$ circles ("ovals"), each of which is null-homotopic in $\mathbb{RP}^2$ and hence bounds a disc. An oval is **even** if it lies inside an even number of other ovals, **odd** otherwise. Write $p$ for the number of even ovals and $n$ for the number of odd ovals, $p+n=l$.

By Harnack's inequality $l \le g+1 = \tfrac{(m-1)(m-2)}{2}+1$; a curve attaining this bound is an **$M$-curve**.

**Gudkov's conjecture (1969).** For every nonsingular real $M$-curve of degree $m=2k$,
$$p - n \equiv k^2 \pmod 8 .$$

A complete resolution requires proving this congruence for all $k \ge 1$ and all $M$-curves, or exhibiting a single $M$-curve violating it. **Status: proved.** Arnold (1971) obtained the congruence mod $4$; Rokhlin (1972) proved the full mod $8$ statement. The conjecture is retained in the catalog because it anchors the still-open *Gudkov program*: the isotopy classification of nonsingular real plane curves (Hilbert's 16th problem, first part), open from degree $8$ upward.

## 2. Mathematical Foundations

**Real scheme.** The isotopy type of the pair $(\mathbb{RP}^2, \mathbb{R}A)$ is encoded by a nesting forest, written in Viro's notation: $\langle 1 \rangle$ is one oval, $\langle \alpha \sqcup 1\langle\beta\rangle\rangle$ is $\alpha$ empty outer ovals together with one oval containing $\beta$ empty ovals.

**Euler-characteristic reading of $p-n$.** For $m=2k$ even, $\mathbb{RP}^2 \setminus \mathbb{R}A$ splits into
$$B = \{x : F(x) \le 0\}, \qquad B' = \overline{\{x : F(x) \ge 0\}},$$
for a defining form $F$ of degree $2k$ normalized so that $B$ is the orientable piece (a disjoint union of surfaces with boundary embedded in a disc). Then
$$\chi(B) = p - n .$$
So Gudkov's congruence is a statement $\chi(B)\equiv k^2 \pmod 8$ about the Euler characteristic of one half of the complement.

**Double cover and the topological input.** Let $Y \to \mathbb{CP}^2$ be the double cover branched along $A$, defined in the total space of $\mathcal{O}(k)$ by $w^2 = F(z_0,z_1,z_2)$. Then $Y$ is a nonsingular simply connected complex surface with
$$\chi(Y) = 2\chi(\mathbb{CP}^2) - \chi(A_{\mathbb C}) = 4k^2-6k+6, \qquad \sigma(Y) = -\tfrac{2}{3}k(2k^2-3), $$
and $Y$ carries two commuting involutions: the deck transformation $\tau$ and complex conjugation. Rokhlin's argument compares $\sigma(Y)$ with the fixed-point data of the induced involution on $Y_{\mathbb R}$, invoking two theorems:

- **Rokhlin's theorem.** For a closed smooth spin $4$-manifold, $\sigma \equiv 0 \pmod{16}$.
- **Atiyah–Singer $G$-signature theorem**, giving $\sigma(\tau, Y)$ in terms of the self-intersection of the branch locus.

Combining these with the Guillou–Marin extension of Rokhlin's theorem to characteristic surfaces in non-spin $4$-manifolds yields the congruence.

**Companion invariants.** A curve is of **type I** (dividing) if $A_{\mathbb C} \setminus \mathbb{R}A$ is disconnected; $M$-curves are always of type I. For a type I curve of degree $2k$ with complex orientations, Rokhlin's formula reads
$$2(\Pi^+ - \Pi^-) = l - k^2,$$
where $\Pi^\pm$ count injective pairs of ovals with agreeing/disagreeing induced orientations. Reducing this relation mod $8$ recovers Gudkov's congruence for $M$-curves.

## 3. History & State of the Art (SOTA)

- **1876.** Harnack proves the bound $l \le g+1$ and constructs $M$-curves of every degree.
- **1891.** Hilbert classifies degree-$6$ curves *incorrectly*: he asserts that only $\langle 9 \sqcup 1\langle 1\rangle\rangle$ and $\langle 1 \sqcup 1\langle 9\rangle\rangle$ occur among $M$-sextics, and includes the classification problem in his 16th problem (1900).
- **1969.** D. A. Gudkov, in his doctoral work at Gorky, completes the classification of nonsingular sextics: exactly $56$ real schemes occur, and there are **three** $M$-sextics — Hilbert's two plus $\langle 5 \sqcup 1\langle 5\rangle\rangle$, which Gudkov constructs. Observing $p-n=1\equiv 3^2 \pmod 8$ in all three cases and $p-n=4\equiv 2^2$ for quartics, he conjectures the general congruence.
- **1971.** Arnold proves $p-n \equiv k^2 \pmod 4$ using the intersection form on the double cover, and the mod $8$ statement under extra hypotheses. This paper launches the "topology of $4$-manifolds applied to real algebraic geometry" program.
- **1972.** Rokhlin, *Proof of Gudkov's hypothesis*, settles the conjecture in full.
- **1973.** Gudkov–Krakhnov and, independently, Kharlamov extend it to $(M-1)$-curves: $p-n \equiv k^2 \pm 1 \pmod 8$.
- **1978–1986.** Rokhlin's complex orientation formula; Marin's and Guillou–Marin's reproofs and sharpenings; Kharlamov–Marin congruences; Viro completes degree $7$ and, with patchworking, revolutionizes construction.
- **1996–2002.** Itenberg–Viro disprove the related Ragsdale conjecture by patchworking; Orevkov introduces braid/link-theoretic prohibitions, closing many degree-$8$ cases.

## 4. Partial Results / Verified Cases

- **Full theorem.** The congruence $p-n\equiv k^2 \pmod 8$ holds for all nonsingular real $M$-curves of every even degree $2k$ (Rokhlin 1972). No exception exists.
- **Degree $2$ and $4$** ($k=1,2$): verified directly from the classifications ($1$ oval; $4$ unnested ovals, $p-n=4$).
- **Degree $6$** ($k=3$): all three $M$-schemes give $p-n=1\equiv 9$.
- **Degree $8$** ($k=4$): every constructed $M$-octic ($l=22$) satisfies $p-n\equiv 16 \equiv 0 \pmod 8$; the congruence is used as a *prohibition*, eliminating candidate schemes.
- **$(M-1)$- and $(M-2)$-curves.** $p-n \equiv k^2\pm1 \pmod 8$ (Gudkov–Krakhnov, Kharlamov 1973); refinements for $(M-2)$ under type-I hypotheses (Kharlamov–Marin).
- **Higher dimensions.** Rokhlin's congruence for $M$-surfaces in $\mathbb{RP}^3$: $\chi(X_{\mathbb R}) \equiv \sigma(X_{\mathbb C}) \pmod{16}$ (Rokhlin, Kharlamov, Nikulin), the direct analogue of Gudkov's statement.
- **Open classification.** Degrees $\le 7$ fully classified (Gudkov for $6$, Viro for $7$). Degree $8$ remains incomplete; a small number of $M$-octic schemes are still undecided *(frontier — verify)*.

## 5. Principal Obstacles

The congruence itself is settled; the obstacles concern the surrounding classification program that Gudkov's result opened.

- **Prohibitions are congruences, not inequalities.** Bézout arguments, Gudkov–Rokhlin, Rokhlin's orientation formula and Fiedler alternation each cut down candidate schemes, but none is complete: in degree $8$ they leave a residue of schemes that are neither prohibited nor constructed.
- **The gap between construction and prohibition widens with degree.** Viro patchworking builds curves from combinatorial data but only realizes schemes admitting a suitable convex subdivision; non-patchworkable schemes require ad hoc small-perturbation or Hilbert–Rohn–Gudkov deformation arguments, which do not scale.
- **$4$-manifold topology saturates.** Rokhlin's method extracts one mod-$8$ (or mod-$16$) datum from the double cover. Extra information would need finer invariants (Seiberg–Witten, Heegaard Floer) of the branched covers, which have not yielded new real-algebraic prohibitions.
- **Moduli-space connectivity is unknown.** Even when a scheme is realizable, deciding whether the space of curves with that scheme is connected — the rigid-isotopy classification — is only solved through degree $6$ (Nikulin, Kharlamov) using $K3$ period maps that have no degree-$8$ analogue.
- **Complexity.** The number of candidate schemes grows super-exponentially with degree, so degree $10$ is out of reach of the case-by-case method entirely.

## 6. The Gap

Proven: $p-n \equiv k^2 \pmod 8$ for $M$-curves; $\pm 1$ shifts for $(M-1)$; the complex orientation formula for type I curves; complete isotopy classification for $m \le 7$.

Not proven: a *complete* system of restrictions. The precise missing step is a family of obstructions strong enough that "not prohibited" implies "constructible" in degree $\ge 8$. Concretely, one wants either (i) a new invariant of the branched double cover $Y$ refining $\sigma(Y) \bmod 16$, or (ii) a construction technique strictly stronger than patchworking plus Gudkov deformation. Every currently undecided degree-$8$ $M$-scheme satisfies Gudkov's congruence and all known Bézout and Rokhlin prohibitions, which is exactly why they resist.

## 7. Current Research (as of June 2026)

- **Orevkov's braid-theoretic school** (Toulouse/Steklov): real trigonal and pseudoholomorphic curves encoded as quasipositive braids; the strongest known degree-$8$ and degree-$9$ prohibitions come from this line.
- **Strasbourg / St. Petersburg (Kharlamov, Degtyarev, Itenberg, Viro's students):** lattice-theoretic and Rokhlin-style methods, plus real enumerative invariants (Welschinger numbers) as a source of new obstructions.
- **Tropical and patchworking geometry** (Itenberg, Mikhalkin, Renaudineau, Shaw): $T$-hypersurfaces, real phase structures, and a spectral sequence computing $\mathbb{Z}/2$ Betti numbers of patchworked real hypersurfaces — a genuinely new prohibition mechanism, currently giving Petrovskii/Ragsdale-type bounds rather than mod-$8$ refinements *(frontier — verify)*.
- **Symplectic/pseudoholomorphic relaxation:** deciding whether some undecided degree-$8$ schemes are realizable by flexible (pseudoholomorphic) curves but not algebraic ones — the sharpest place where "algebraic" and "topological" would separate *(frontier — verify)*.

## 8. Future Work

- Complete the isotopy classification of nonsingular octics — the explicitly named successor task in Gudkov's 1974 survey and Viro's problem lists.
- Search for mod-$16$ or mod-$32$ congruences for $M$-curves refining Gudkov's, plausibly via Pin$^-$ structures and the Guillou–Marin form on characteristic surfaces.
- Push the rigid-isotopy classification past degree $6$; degree-$8$ curves relate to lattice-polarized surfaces without the $K3$ period tool.
- Systematize computer-assisted prohibition: encode Bézout, Gudkov–Rokhlin, orientation and Fiedler conditions as constraints and enumerate surviving degree-$8$/$9$ schemes exhaustively.
- Extend the congruence program to real algebraic surfaces in $\mathbb{RP}^3$ of degree $\ge 5$, where the analogue of Gudkov's classification is wide open.

## 9. Key References

- **[Foundational]** A. Harnack. *Über die Vieltheiligkeit der ebenen algebraischen Curven.* Mathematische Annalen 10 (1876), 189–198.
- **[Foundational]** D. Hilbert. *Über die reellen Züge algebraischer Curven.* Mathematische Annalen 38 (1891), 115–138.
- **[Foundational]** D. A. Gudkov. *Complete topological classification of the disposition of ovals of a sixth order curve in the projective plane* (Russian). Gor'kov. Gos. Univ. Uchen. Zap. 87 (1969), 118–153.
- **[Foundational]** V. I. Arnold. *On the arrangement of ovals of real plane algebraic curves, involutions of four-dimensional smooth manifolds, and the arithmetic of integral quadratic forms.* Functional Analysis and Its Applications 5 (1971), 169–176.
- **[Foundational]** V. A. Rokhlin. *Proof of Gudkov's hypothesis.* Functional Analysis and Its Applications 6 (1972), 136–138.
- **[Extension]** D. A. Gudkov, A. D. Krakhnov. *On the periodicity of the Euler characteristic of real algebraic $(M-1)$-manifolds.* Functional Analysis and Its Applications 7 (1973), 98–102.
- **[Extension]** V. M. Kharlamov. *New congruences for the Euler characteristic of real algebraic manifolds.* Functional Analysis and Its Applications 7 (1973), 147–150.
- **[Foundational]** V. A. Rokhlin. *Complex topological characteristics of real algebraic curves.* Russian Mathematical Surveys 33:5 (1978), 85–98.
- **[Survey]** D. A. Gudkov. *The topology of real projective algebraic varieties.* Russian Mathematical Surveys 29:4 (1974), 1–79.
- **[Survey]** G. Wilson. *Hilbert's sixteenth problem.* Topology 17 (1978), 53–73.
- **[Survey]** O. Ya. Viro. *Progress in the topology of real algebraic varieties over the last six years.* Russian Mathematical Surveys 41:3 (1986), 55–82.
- **[Survey]** A. Degtyarev, V. Kharlamov. *Topological properties of real algebraic varieties: Rokhlin's way.* Russian Mathematical Surveys 55:4 (2000), 735–814.
- **[SOTA]** S. Yu. Orevkov. *Link theory and oval arrangements of real algebraic curves.* Topology 38 (1999), 779–810.
- **[SOTA]** I. Itenberg, O. Viro. *Patchworking algebraic curves disproves the Ragsdale conjecture.* The Mathematical Intelligencer 18 (1996), 19–28.
- **[Method]** L. Guillou, A. Marin (eds.). *À la recherche de la topologie perdue.* Progress in Mathematics 62, Birkhäuser, 1986.

## 10. Worked Example / Concrete Special Case

**Degree $4$, $k=2$: constructing an $M$-quartic and checking the congruence.**

Take two ellipses
$$f(x,y) = x^2+2y^2-1, \qquad g(x,y) = 2x^2+y^2-1 .$$
They meet where $x^2+2y^2 = 2x^2+y^2$, i.e. $y^2=x^2$, together with $3x^2=1$: four real nodes at $(\pm\tfrac{1}{\sqrt3}, \pm\tfrac{1}{\sqrt3})$. The union $\{fg=0\}$ is a singular quartic whose real picture is a "flower": one central region (inside both ellipses), four lunes (inside exactly one), and the unbounded region.

Smooth the four nodes by perturbing:
$$C_\delta: \; f(x,y)\,g(x,y) = -\delta, \qquad 0<\delta \ll 1 .$$
The set $\{fg<-\delta\}$ is exactly the four lunes, each shrunk away from the nodes, so $\mathbb{R}C_\delta$ consists of **four pairwise disjoint, unnested ovals**. Since $g=3$ for a quartic, Harnack's bound is $l\le 4$: $C_\delta$ is an $M$-quartic.

Count: all four ovals have depth $0$, so $p=4$, $n=0$, and
$$p-n = 4 = 2^2 = k^2, \qquad 4 \equiv 4 \pmod 8 .\ \checkmark$$

The opposite smoothing $fg = +\delta$ gives $\{fg>\delta\}$ = central region $\sqcup$ outer region, hence two **nested** ovals: $p=1$ (outer, depth $0$), $n=1$ (inner, depth $1$), $p-n=0$. This is an $(M-2)$-curve, so Gudkov's congruence does not apply — and indeed $0 \not\equiv 4 \pmod 8$, showing the maximality hypothesis is essential. Deleting one oval from the four-oval curve by a further small perturbation gives an $(M-1)$-quartic with $p=3,n=0$, and $3 \equiv k^2-1 \pmod 8$, matching Gudkov–Krakhnov–Kharlamov.

For comparison, the three $M$-sextics ($k=3$, $l=11$):

| scheme | $p$ | $n$ | $p-n$ | $k^2 \bmod 8$ |
|---|---|---|---|---|
| $\langle 9 \sqcup 1\langle 1\rangle\rangle$ | $10$ | $1$ | $9$ | $1$ |
| $\langle 1 \sqcup 1\langle 9\rangle\rangle$ | $2$ | $9$ | $-7$ | $1$ |
| $\langle 5 \sqcup 1\langle 5\rangle\rangle$ (Gudkov) | $6$ | $5$ | $1$ | $1$ |

All three reduce to $1 \equiv 9 \pmod 8$. It was precisely Gudkov's discovery of the third row — the scheme Hilbert had declared impossible — that made the pattern visible.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*