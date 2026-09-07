---
id: 02-algebra-group-theory/hilberts-fourteenth-problem
title: "Hilbert's Fourteenth Problem"
topic: 02-algebra-group-theory
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Hilbert's Fourteenth Problem

> **Topic:** Algebra & Group Theory · **ID:** `02-algebra-group-theory/hilberts-fourteenth-problem` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

Let $k$ be a field and $k[x_1,\dots,x_n]$ the polynomial ring, with fraction field $k(x_1,\dots,x_n)$.

**Hilbert's 14th Problem (Zariski's formulation).** Let $L$ be a subfield with $k \subseteq L \subseteq k(x_1,\dots,x_n)$. Is the ring
$$A \;=\; L \cap k[x_1,\dots,x_n]$$
finitely generated as a $k$-algebra?

Hilbert (1900) asked the question in the narrower setting of invariants: if a linear algebraic group $G \subseteq GL_n(k)$ acts on $k[x_1,\dots,x_n]$, is the invariant ring $k[x_1,\dots,x_n]^G$ finitely generated? Because $k[\mathbf{x}]^G = k(\mathbf{x})^G \cap k[\mathbf{x}]$ for a connected group, the invariant version is a special case of the field-theoretic one.

**Resolution status.** The answer is **no** in general. Nagata (1958) constructed a linear action of $\mathbb{G}_a^{13}$ on $k[x_1,\dots,x_{32}]$ with non-finitely-generated invariant ring. What remains active is the *boundary*: for which $n$, which classes of groups, and which classes of derivations does finite generation hold. The minimal $n$ for the field version was settled by Kuroda (2005): $n=3$ admits a counterexample, and $n \le 2$ never does (Zariski). A complete resolution of the residual problem would mean a characterization of finite generation for all $\mathbb{G}_a$-actions (equivalently, kernels of locally nilpotent derivations), where dimension $4$ is still open.

## 2. Mathematical Foundations

**Derivations and $\mathbb{G}_a$-actions.** A $k$-derivation $D$ of $B = k[x_1,\dots,x_n]$ is $k$-linear with $D(fg)=fD(g)+gD(f)$. $D$ is *locally nilpotent* (an LND) if for every $f \in B$ there is $m$ with $D^m(f)=0$. In characteristic $0$, LNDs correspond bijectively to algebraic actions of the additive group $\mathbb{G}_a = (k,+)$ via
$$\varphi_t(f) \;=\; \exp(tD)(f) \;=\; \sum_{i\ge 0} \frac{t^i}{i!}D^i(f),$$
and the invariant ring is the kernel: $B^{\mathbb{G}_a} = \ker D$. Kernels are *factorially closed*: $fg \in \ker D$, $fg \neq 0$ $\Rightarrow$ $f,g \in \ker D$. Hence $\ker D$ is algebraically closed in $B$ and $\operatorname{trdeg}_k \ker D = n-1$.

**Symbolic Rees algebras.** For a prime $\mathfrak{p}$ in a normal domain $R$, the $m$-th symbolic power is $\mathfrak{p}^{(m)} = \mathfrak{p}^m R_\mathfrak{p} \cap R$. The symbolic blow-up $\bigoplus_{m \ge 0} \mathfrak{p}^{(m)} t^m$ is finitely generated iff a corresponding invariant ring is — the bridge Roberts and Nagata exploited.

**Nagata's construction.** Fix $r=16$ general points $p_i=(p_{i1}:p_{i2}:p_{i3}) \in \mathbb{P}^2$. Let
$$G \;=\; \Big\{ (a_1,\dots,a_{16}) \in \mathbb{G}_a^{16} \;:\; \sum_{i=1}^{16} p_{ij}\,a_i = 0,\; j=1,2,3 \Big\} \;\cong\; \mathbb{G}_a^{13},$$
acting on $k[x_1,\dots,x_{16},y_1,\dots,y_{16}]$ by
$$x_i \mapsto x_i, \qquad y_i \mapsto y_i + a_i x_i .$$
Then $k[\mathbf{x},\mathbf{y}]^G$ is not finitely generated.

**Positive theorems the problem sits against.**
- *Noether (1926):* $B^G$ is finite over $k$ for any finite group $G$, in every characteristic.
- *Hilbert (1890, 1893) / Nagata (1964) / Haboush (1975):* if $G$ is reductive (linearly reductive in char $0$; geometrically reductive in char $p$, by Haboush's theorem), then $B^G$ is finitely generated.
- *Weitzenböck (1932), rigorous proof Seshadri (1962):* in characteristic $0$, a *linear* $\mathbb{G}_a$-action on $k[x_1,\dots,x_n]$ has finitely generated invariants for every $n$.
- *Zariski (1954):* if $\operatorname{trdeg}_k L \le 2$, then $L \cap k[x_1,\dots,x_n]$ is finitely generated, for every $n$.

The failure is therefore confined to non-reductive groups (essentially unipotent ones) with non-linear or high-dimensional actions.

## 3. History & State of the Art (SOTA)

- **1900** — Hilbert states the problem in his Paris ICM address, motivated by his own finiteness theorem for $SL_n$ invariants.
- **1954** — Zariski reformulates it for arbitrary intermediate fields and proves the $\operatorname{trdeg} \le 2$ case.
- **1958–59** — Nagata announces the counterexample at the Edinburgh ICM; full version in *Amer. J. Math.* 81 (1959). The proof rests on his own results about linear systems of plane curves through $r=16$ general points with prescribed multiplicities.
- **1963–75** — Nagata proves finite generation for geometrically reductive groups; Haboush proves reductive $\Rightarrow$ geometrically reductive, closing Mumford's conjecture and the positive side of the problem.
- **1990** — P. Roberts: counterexample in $n=7$ variables, as the kernel of an explicit derivation, and simultaneously an infinitely generated symbolic blow-up.
- **1999–2000** — Daigle–Freudenburg: $n=5$ (a triangular $\mathbb{G}_a$-action on $\mathbb{A}^5$); Freudenburg: $n=6$.
- **2001–06** — Mukai reinterprets Nagata's example via Cox rings of blow-ups of $\mathbb{P}^n$; Castravet–Tevelev connect it to Mori dream spaces.
- **2004–05** — Kuroda: counterexamples in dimension $4$ and then $3$ for the field version, hitting Zariski's bound exactly.
- **2008** — Totaro links the finite-field version to conjectures on cones of curves.

## 4. Partial Results / Verified Cases

**Finite generation holds (proved):**

| Setting | Result |
|---|---|
| $G$ finite, any char | Noether, 1926 |
| $G$ reductive, char $0$ | Hilbert 1890/1893 |
| $G$ reductive, char $p$ | Nagata 1964 + Haboush 1975 |
| $\operatorname{trdeg}_k L \le 2$, any $n$ | Zariski 1954 |
| $n \le 2$ (field version) | Zariski 1954 |
| Linear $\mathbb{G}_a$-action, char $0$, any $n$ | Weitzenböck 1932; Seshadri 1962 |
| $\ker D$ for any LND $D$ of $k[x_1,x_2,x_3]$ | Miyanishi 1985; kernel is a polynomial ring in 2 variables |
| Triangular derivations of $k[x_1,\dots,x_4]$ | Daigle–Freudenburg, *J. Algebra* 204 (1998) |
| LNDs of $R[X,Y,Z]$, $R$ a Dedekind/PID base | Bhatwadekar–Daigle, *J. Algebra* 322 (2009) |
| Nagata-type invariants for $r \le 8$ general points in $\mathbb{P}^2$ (A-D-E cases) | Mukai; Cox ring finitely generated (del Pezzo) |

**Counterexamples (finite generation fails):**

| $n$ | Group / object | Author |
|---|---|---|
| $32$ | $\mathbb{G}_a^{13}$, linear-fibered | Nagata 1959 |
| $18$ | $\mathbb{G}_a^{3}$ | Mukai 2001 |
| $7$ | single LND, symbolic blow-up | Roberts 1990 |
| $6$ | single $\mathbb{G}_a$-action | Freudenburg 2000 |
| $5$ | triangular $\mathbb{G}_a$-action | Daigle–Freudenburg 1999 |
| $4,\,3$ | subfield $L \subset k(x_1,\dots,x_n)$ | Kuroda 2004, 2005 |

Mukai's criterion: for the blow-up of $\mathbb{P}^{n-1}$ at $r$ general points, the Cox ring (equivalently the relevant $\mathbb{G}_a^{r-n}$-invariant ring) is **not** finitely generated when
$$\frac{1}{2} + \frac{1}{n} + \frac{1}{r-n} \;\le\; 1 ,$$
which for $n=3$ gives $r \ge 9$ — a sharp improvement on Nagata's $r=16$.

## 5. Principal Obstacles

- **No reductive averaging.** For linearly reductive $G$ the Reynolds operator $R: B \to B^G$ is a $B^G$-module projection, so $B^G$ inherits Noetherianity of $B$ through $I B \cap B^G = I$. Unipotent groups have no Reynolds operator, and this single tool — the entire classical proof — evaporates.
- **Quotients are only quasi-affine.** For $\mathbb{G}_a$-actions the geometric quotient is typically a quasi-affine variety $U$, and $B^G = \mathcal{O}(U)$. Rings of global functions on quasi-affine varieties are notoriously non-Noetherian (Winkelmann, 2003, characterizes exactly which arise). There is no dimension bound forcing them to be affine.
- **Failure is a linear-systems phenomenon.** Nagata's counterexample is equivalent to a statement about the degrees $d$ and multiplicities $m$ of plane curves through $r$ general points: infinitely many extremal curves are needed. Testing finite generation therefore requires controlling the Mori cone of a blow-up of $\mathbb{P}^2$ — Nagata's conjecture ($d > m\sqrt{r}$ for $r \ge 10$ general points) is itself open, and known only for $r$ a perfect square.
- **No effective degree bounds.** For reductive $G$ there are Derksen-type bounds on generator degrees. For unipotent $G$ no such bound can exist, so Gröbner-basis computation of $\ker D$ terminates only if the kernel happens to be finitely generated — the algorithm cannot certify the negative case.
- **Low dimensions are structurally rigid, not conceptually easy.** The positive results in dimension $3$ use classification of surfaces / $\mathbb{A}^1$-fibrations (Miyanishi), which have no analogue in dimension $4$.

## 6. The Gap

Precisely:

1. **Dimension 4 for $\mathbb{G}_a$.** Is $\ker D$ finitely generated for every locally nilpotent derivation $D$ of $k[x_1,x_2,x_3,x_4]$, $\operatorname{char} k = 0$? Known for triangular $D$; open in general. Since counterexamples exist in $n=5$ and finite generation holds in $n=3$, this single case is the exact frontier.
2. **A structural criterion.** No intrinsic test decides finite generation of $\ker D$ from $D$. The gap is between case-by-case constructions (each counterexample is a bespoke derivation) and a theorem of the form "$\ker D$ is f.g. iff [computable condition on $D$]".
3. **Nagata's conjecture.** Sharpening the Mukai bound and understanding Cox rings of $\mathbb{P}^2$ blown up at $r \ge 10$ general points requires proving Nagata's conjecture for non-square $r$.

## 7. Current Research (as of June 2026)

- **Cox rings and Mori dream spaces.** The dominant modern framing: finite generation of $\operatorname{Cox}(X)$ for blow-ups. Groups at Tübingen (Hausen and collaborators, with the `Cox` / `Macaulay2` toolchains), Kyoto (RIMS, following Mukai), and Bonn continue producing new non-Mori-dream examples, including for $\overline{M}_{0,n}$ following Castravet–Tevelev and later work of González–Karu and Hausen–Keicher–Laface. *(frontier — verify: sharpest current $n$ for $\overline{M}_{0,n}$ non-MDS.)*
- **Locally nilpotent derivations.** Freudenburg (Western Michigan), Daigle (Ottawa), Kuroda (Tokyo Metropolitan) continue the dimension-$4$ program, classifying LNDs of $k[x_1,\dots,x_4]$ by rank and degree.
- **Positive characteristic.** Exponential/Frobenius-twisted $\mathbb{G}_a$-actions behave differently; Totaro's programme relating the finite-field case to the cone of curves is still being pursued.
- **Computational invariant theory.** Derksen–Kemper-style algorithms extended to unipotent groups by Kohls, Kraft, and others: algorithms that succeed when the invariant ring *is* finitely generated, with no termination guarantee otherwise.

## 8. Future Work

- Settle dimension $4$: either produce an LND of $k^{[4]}$ with infinitely generated kernel, or extend Miyanishi's surface-classification argument via $\mathbb{A}^1$-fibrations on threefolds.
- Prove Nagata's conjecture for non-square $r \ge 10$, which would sharpen every Nagata-type counterexample and pin the exact threshold in Mukai's inequality.
- Develop a valuation-theoretic criterion: express $\ker D$ as $\mathcal{O}(U)$ and characterize finite generation through the divisorial valuations on the boundary $X \setminus U$.
- Find the minimal dimension for the *invariant-ring* (as opposed to field) version — currently $5$ from above, $4$ from below.
- Classify which non-reductive groups always give finitely generated invariants (parabolic-type observations of Grosshans; Grosshans subgroups).

## 9. Key References

- **[Foundational]** D. Hilbert. *Mathematische Probleme.* Nachrichten der Königl. Gesellschaft der Wissenschaften zu Göttingen, 1900; expanded in *Archiv der Mathematik und Physik* (3) **1** (1901), 44–63, 213–237.
- **[Foundational]** O. Zariski. *Interprétations algébrico-géométriques du quatorzième problème de Hilbert.* Bulletin des Sciences Mathématiques (2) **78** (1954), 155–168.
- **[Foundational]** M. Nagata. *On the 14-th problem of Hilbert.* American Journal of Mathematics **81** (1959), 766–772.
- **[Foundational]** M. Nagata. *Lectures on the Fourteenth Problem of Hilbert.* Tata Institute of Fundamental Research, Bombay, 1965.
- **[Foundational]** M. Nagata. *Invariants of a group in an affine ring.* Journal of Mathematics of Kyoto University **3** (1964), 369–377.
- **[Foundational]** W. Haboush. *Reductive groups are geometrically reductive.* Annals of Mathematics **102** (1975), 67–83.
- **[Foundational]** R. Weitzenböck. *Über die Invarianten von linearen Gruppen.* Acta Mathematica **58** (1932), 231–293.
- **[Foundational]** C. S. Seshadri. *On a theorem of Weitzenböck in invariant theory.* Journal of Mathematics of Kyoto University **1** (1962), 403–409.
- **[SOTA / Recent]** P. Roberts. *An infinitely generated symbolic blow-up in a power series ring and a new counterexample to Hilbert's fourteenth problem.* Journal of Algebra **132** (1990), 461–473.
- **[SOTA / Recent]** D. Daigle and G. Freudenburg. *A counterexample to Hilbert's fourteenth problem in dimension 5.* Journal of Algebra **221** (1999), 528–535.
- **[SOTA / Recent]** G. Freudenburg. *A counterexample to Hilbert's fourteenth problem in dimension six.* Transformation Groups **5** (2000), 61–71.
- **[SOTA / Recent]** S. Kuroda. *A counterexample to the fourteenth problem of Hilbert in dimension four.* Journal of Algebra **279** (2004), 126–134.
- **[SOTA / Recent]** S. Kuroda. *A counterexample to the fourteenth problem of Hilbert in dimension three.* Michigan Mathematical Journal **53** (2005), 123–132.
- **[SOTA / Recent]** A.-M. Castravet and J. Tevelev. *Hilbert's 14th problem and Cox rings.* Compositio Mathematica **142** (2006), 1479–1498.
- **[SOTA / Recent]** B. Totaro. *Hilbert's 14th problem over finite fields and a conjecture on the cone of curves.* Compositio Mathematica **144** (2008), 1176–1198.
- **[SOTA / Recent]** S. M. Bhatwadekar and D. Daigle. *On finite generation of kernels of locally nilpotent $R$-derivations of $R[X,Y,Z]$.* Journal of Algebra **322** (2009), 2915–2926.
- **[Survey]** G. Freudenburg. *Algebraic Theory of Locally Nilpotent Derivations.* Encyclopaedia of Mathematical Sciences **136**, Springer, 2nd edition, 2017.
- **[Survey]** H. Derksen and G. Kemper. *Computational Invariant Theory.* Encyclopaedia of Mathematical Sciences **130**, Springer, 2nd edition, 2015.
- **[Survey]** A. van den Essen. *Polynomial Automorphisms and the Jacobian Conjecture.* Progress in Mathematics **190**, Birkhäuser, 2000.
- **[Survey]** J. Winkelmann. *Invariant rings and quasiaffine quotients.* Mathematische Zeitschrift **244** (2003), 163–174.

## 10. Worked Example / Concrete Special Case

**A positive case computed in full.** Let $k$ have characteristic $0$, $B=k[x,y,z]$, and
$$D \;=\; x\frac{\partial}{\partial y} + y\frac{\partial}{\partial z}.$$
$D$ is linear and locally nilpotent: $D(x)=0$, $D(y)=x$, $D(z)=y$, so $D^3=0$ on generators. The associated $\mathbb{G}_a$-action is $\exp(tD): (x,y,z)\mapsto (x,\;y+tx,\;z+ty+\tfrac{t^2}{2}x)$.

*Claim:* $\ker D = k[x,\,f]$ where $f = y^2 - 2xz$.

*Check $f \in \ker D$:* $D(f) = 2yD(y) - 2zD(x) - 2xD(z) = 2yx - 0 - 2xy = 0$.

*Proof of equality.* $D(y)=x$, so $y$ is a *local slice* with $x \in \ker D$. Localize: in $B_x = k[x,x^{-1}][y,z]$, set $\tilde z = z - \frac{y^2}{2x}$. Then $D(\tilde z) = y - \frac{2y\cdot x}{2x} = 0$, and $B_x = (\ker D)_x[y]$ with $D = x\,\partial/\partial y$ on it. Hence $(\ker D)_x = k[x,x^{-1}][\tilde z] = k[x,x^{-1}][f]$, since $\tilde z = -f/(2x)$. So any $h \in \ker D$ satisfies $x^N h \in k[x,f]$ for some $N$. Because $k[x,f]$ is a polynomial ring in two variables and $x$ is prime in it with $k[x,f]/(x) \cong k[\bar f]$ a domain, $k[x,f]$ is factorially closed in itself under division by $x$, giving $h \in k[x,f]$. Thus $\ker D = k[x,f]$: **two generators, finitely generated**, consistent with Weitzenböck.

**Where the argument breaks.** The proof used two things: a slice $y$ with $D(y)=x$ a *single* prime, and a clean fibration $B_x = (\ker D)_x[y]$. In Nagata's example the group is $\mathbb{G}_a^{13}$ acting on $k[x_1,\dots,x_{16},y_1,\dots,y_{16}]$ by $y_i \mapsto y_i + a_ix_i$; grading by $\deg y_i = 1$, the degree-$d$ invariants of weight $m$ correspond to plane curves of degree $d$ passing through the $16$ general points $p_i$ with multiplicity $\ge m$. Nagata proved that for $r=16$ such curves exist only when $d > m\sqrt{16} = 4m$, and that the extremal cases produce, for each $d$, a new invariant not expressible in the previously found ones. There is no single localization $x_i$ that trivializes all $13$ directions at once — infinitely many extremal linear systems are needed, and the invariant ring is not finitely generated.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*