---
id: 05-analysis/nevanlinna-theory-extensions
title: "Nevanlinna Theory Extensions"
topic: 05-analysis
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Nevanlinna Theory Extensions

> **Topic:** Real & Complex Analysis · **ID:** `05-analysis/nevanlinna-theory-extensions` · **Status:** open

## 1. Problem Statement / Conjecture

Nevanlinna's Second Main Theorem (SMT) gives, for a nonconstant meromorphic $f:\mathbb{C}\to\mathbb{P}^1$ and distinct points $a_1,\dots,a_q$,
$$(q-2)\,T(r,f)\le \sum_{j=1}^q N^{(1)}(r,a_j) + S(r,f),$$
with truncation at multiplicity $1$. The **extension problem** is to establish the analogous inequality for holomorphic maps into higher-dimensional varieties. The central open statement is the **Griffiths–Lang conjecture** in its truncated form (Vojta's "$1+\varepsilon$" analogue):

> Let $X$ be a smooth complex projective variety, $D\subset X$ a normal crossings divisor, $A$ an ample divisor, and $f:\mathbb{C}\to X$ a holomorphic curve with Zariski-dense image. Then for every $\varepsilon>0$,
> $$T_{K_X+D}(r,f)\ \le\ N^{(1)}_D(r,f)\ +\ \varepsilon\,T_A(r,f)\ +\ O(1)$$
> for all $r$ outside a set of finite Lebesgue measure.

Two subordinate open statements are tracked here: (i) the **Green–Griffiths–Lang conjecture** — if $X$ is of general type, all entire curves $f:\mathbb{C}\to X$ lie in a proper algebraic subvariety $Y\subsetneq X$ independent of $f$; and (ii) the **Kobayashi conjecture** — a *very general* hypersurface $X\subset\mathbb{P}^{n+1}$ of degree $d\ge 2n+1$ is Kobayashi hyperbolic, and $\mathbb{P}^n\setminus X$ is hyperbolic for $d\ge 2n+1$.

A complete solution means a proof (or a counterexample with an explicit Zariski-dense entire curve) of the truncated SMT above for arbitrary $(X,D)$; untruncated versions, or versions with an unspecified exceptional set depending on $f$, do not suffice.

## 2. Mathematical Foundations

For $f:\mathbb{C}\to\mathbb{P}^1$ meromorphic, the **proximity**, **counting** and **characteristic** functions are
$$m(r,a)=\int_0^{2\pi}\log^+\frac{1}{|f(re^{i\theta})-a|}\frac{d\theta}{2\pi},\qquad N(r,a)=\int_0^r\frac{n(t,a)-n(0,a)}{t}\,dt+n(0,a)\log r,$$
$$T(r,f)=m(r,\infty)+N(r,\infty),$$
where $n(t,a)$ counts $a$-points in $|z|\le t$ with multiplicity. The **First Main Theorem** states $m(r,a)+N(r,a)=T(r,f)+O(1)$ for all $a\in\mathbb{P}^1$. The **truncated** counting function $N^{(k)}(r,a)$ replaces each multiplicity $\mu$ by $\min(\mu,k)$. The **defect** is
$$\delta(a)=\liminf_{r\to\infty}\frac{m(r,a)}{T(r,f)}=1-\limsup_{r\to\infty}\frac{N(r,a)}{T(r,f)},$$
and the SMT yields the **defect relation** $\sum_{a\in\mathbb{P}^1}\delta(a)\le 2$.

For a holomorphic curve $f:\mathbb{C}\to X$ into a projective variety and a line bundle $L$ with smooth metric of Chern form $\omega$, the **order function** is
$$T_L(r,f)=\int_1^r\frac{dt}{t}\int_{|z|<t} f^*\omega ,$$
and for $D\in|L|$ with $f(\mathbb{C})\not\subset\mathrm{supp}\,D$, $m_D(r,f)+N_D(r,f)=T_L(r,f)+O(1)$.

**Cartan's Second Main Theorem** (1933): if $f:\mathbb{C}\to\mathbb{P}^n$ is linearly nondegenerate and $H_1,\dots,H_q$ are hyperplanes in general position, then
$$(q-n-1)\,T(r,f)\ \le\ \sum_{j=1}^q N^{(n)}_{H_j}(r,f)\ +\ S(r,f),$$
truncation level exactly $n$; $S(r,f)=O(\log T(r,f)+\log r)$ off a finite-measure set.

**Jet differentials.** Let $E_{k,m}T^*_X$ denote the Green–Griffiths bundle of jet differentials of order $k$ and weighted degree $m$, i.e. polynomials $P(f',f'',\dots,f^{(k)})$ of weight $m$ under $f^{(j)}\mapsto \lambda^j f^{(j)}$. The **fundamental vanishing theorem** (Green–Griffiths; Siu–Yeung; Demailly): if $P\in H^0(X,E_{k,m}T^*_X\otimes A^{-1})$ with $A$ ample, then every entire $f:\mathbb{C}\to X$ satisfies $P(j_k f)\equiv 0$. This converts hyperbolicity into a problem of producing enough global jet differentials, controlled by the algebraic Morse-type inequalities of Demailly.

**Vojta's dictionary** identifies $T$ with logarithmic height, $N^{(1)}$ with the truncated counting of primes, and the truncated SMT above with Vojta's conjecture on integral points — which implies the $abc$ conjecture. Hence the analytic statement in §1 is the function-theoretic shadow of $abc$.

## 3. History & State of the Art

- **1925.** R. Nevanlinna proves the First and Second Main Theorems and the defect relation, superseding Picard (1879) and Borel (1897).
- **1933.** H. Cartan establishes the SMT for linearly nondegenerate curves in $\mathbb{P}^n$ against hyperplanes with truncation $n$, and conjectures the moving-target and defect refinements.
- **1970s.** Griffiths, King and Carlson develop equidimensional and higher-dimensional value distribution (Acta Math. 1973); Bloch's 1926 theorem on abelian varieties is completed by Ochiai and Kawamata (Bloch–Ochiai theorem: entire curves in a complex torus have degenerate Zariski closure, a translate of a subtorus).
- **1977.** Drasin solves Nevanlinna's inverse problem: any admissible pair of deficiency/branching data on a countable set is realized by a meromorphic function.
- **1979–1987.** Green–Griffiths formulate the algebraic-degeneracy conjecture; Vojta constructs the arithmetic–analytic dictionary (LNM 1239, 1987), making the truncated SMT the analytic analogue of the $abc$/Vojta conjecture.
- **1998.** McQuillan proves Green–Griffiths for surfaces of general type with $c_1^2>c_2$, via Ahlfors currents and Diophantine approximation on foliations.
- **2004.** Yamanoi proves the SMT for small (moving) targets with the sharp constant $2$, closing a problem open since Chuang and Osgood.
- **2009–2020.** Ru proves the SMT for holomorphic curves into $\mathbb{P}^n$ (and general $X$) against hypersurfaces in general position; Ru–Vojta introduce the birational Nevanlinna constant $\mathrm{Nev}_{\mathrm{bir}}$, unifying most known SMTs (Amer. J. Math. 2020).
- **2015–2019.** Siu proves hyperbolicity of generic high-degree hypersurfaces in $\mathbb{P}^n$; Brotbek gives a self-contained Wronskian proof; Demailly and Deng make the degree bound effective ($d\ge (5n)^2 n^n$ order of magnitude), and Brotbek–Deng handle complements.

## 4. Partial Results / Verified Cases

- **Dimension 1 targets:** complete (Nevanlinna 1925), with truncation level $1$ and sharp constant $2$; small-function targets settled by Yamanoi (2004), and Gol'dberg's conjecture on zeros of higher derivatives by Yamanoi (2013).
- **$X=\mathbb{P}^n$, hyperplanes in general position:** Cartan (1933), truncation $n$, sharp. Moving hyperplanes: Ru–Stoll (1991), truncation established by Ru–Wang.
- **$X=\mathbb{P}^n$, $q$ hypersurfaces of degree $d_j$ in general position:** Ru (Ann. of Math. 169, 2009) proves $\sum_j d_j^{-1} m_{D_j}(r,f)\le (n+1+\varepsilon)T(r,f)$ for Zariski-dense $f$ — but **untruncated**.
- **Semi-abelian varieties:** Noguchi–Winkelmann–Yamanoi prove the SMT with truncation level $1$ for holomorphic curves into semi-abelian $A$ with a compactification, plus the general-position defect relation — the strongest complete case in dimension $\ge 2$.
- **Varieties of maximal Albanese dimension:** Yamanoi (2015) proves Green–Griffiths–Lang: entire curves are algebraically degenerate.
- **Surfaces of general type with $c_1^2>c_2$:** McQuillan (1998); Demailly–El Goul prove hyperbolicity for very general surfaces in $\mathbb{P}^3$ of degree $d\ge 21$.
- **Generic hypersurfaces $X\subset\mathbb{P}^{n+1}$:** hyperbolic for $d\ge (5n)^2n^n$ (Demailly) and $d\ge (n+1)^{n+2}(n+2)^{2n+3}$ ranges in Brotbek–Deng; complements $\mathbb{P}^n\setminus X$ hyperbolic for $d\ge (n+1)^{n+2}(n+2)^{2n+3}$. The conjectural sharp bound $d\ge 2n+1$ is verified only for $n=1$ (trivially) and partially for $n=2$.
- **Non-archimedean analogue:** the $p$-adic SMT holds with truncation level $1$ and no error term (Boutabaa; An–Escassut; Ru), because $p$-adic entire functions have no ramification loss.

## 5. Principal Obstacles

1. **Truncation.** Every known higher-dimensional SMT beyond semi-abelian varieties (Ru 2009; Ru–Vojta 2020) is proved by Schmidt-subspace-style filtration or by the Ahlfors–Schwarz lemma, both of which lose control of multiplicities. There is no analogue of the logarithmic derivative lemma applied to a Wronskian that keeps multiplicity $\le \dim$ once the target is not a linear system on $\mathbb{P}^n$. Since truncated SMT $\Rightarrow$ $abc$-type arithmetic statements, the barrier is expected to be genuine.
2. **Absence of a Wronskian.** Cartan's proof uses the Wronskian $W(f_0,\dots,f_n)$, an object tied to linear nondegeneracy in $\mathbb{P}^n$. For a general $X$ no canonical differential operator of order $n$ exists; jet differentials replace it but exist only in high weighted degree.
3. **Negativity of jet bundles.** Demailly's Morse inequalities give sections of $E_{k,m}T^*_X\otimes A^{-1}$ only when $k$ and $m$ grow like $n^{O(n)}$, producing degree bounds far above $2n+1$. The base locus of these sections is uncontrolled, so degeneracy is proved but the *exceptional locus* is not identified.
4. **From degeneracy to hyperbolicity.** Green–Griffiths gives an entire curve inside some subvariety $Y$; hyperbolicity requires induction on $\dim Y$, and $Y$ is typically singular with no known control on its canonical bundle. This "descent" step fails uniformly.
5. **Error term and exceptional sets.** $S(r,f)$ is only controlled outside a set of finite measure; no method removes this for curves of infinite lower order, blocking uniform statements.

## 6. The Gap

Proven (§4): untruncated SMT for $\mathbb{P}^n$ and hypersurfaces (Ru), truncation level $1$ only for semi-abelian targets, algebraic degeneracy for maximal Albanese dimension and for generic very-high-degree hypersurfaces. Conjectured (§1): truncation level $1$ (or any level bounded independently of $f$) for arbitrary $(X,D)$ of log-general type, with a $\varepsilon T_A$ error.

The precise missing step is a **multiplicity-preserving replacement for the Wronskian on an arbitrary projective variety**: a canonical section, of order $k$ bounded in terms of $\dim X$, whose vanishing divisor along $f$ dominates $\sum_j (N_{D_j}-N^{(1)}_{D_j})$. Equivalently: upgrade Ru–Vojta's $\mathrm{Nev}_{\mathrm{bir}}(D)$ inequality to a truncated form. In the arithmetic dictionary this is exactly the step from Schmidt's subspace theorem to $abc$, which is also open.

## 7. Current Research (as of June 2026)

- **Ru–Vojta programme.** Ongoing refinement of the birational Nevanlinna constant to handle non-general-position divisors and subvarieties; extensions to the "Cartan-type" setting and to moving targets. Groups: Houston (Ru), Berkeley (Vojta), and collaborators in Shanghai and Taipei.
- **Effective Kobayashi bounds.** Demailly's school (Grenoble), Brotbek (Strasbourg), Deng (Wuhan/CAS), Diverio (Rome), Merker (Orsay) push the degree threshold for hyperbolic generic hypersurfaces downward; current published thresholds remain super-exponential in $n$, and reaching a polynomial bound in $n$ is the stated near-term target *(frontier — verify)*.
- **Foliation and Ahlfors-current methods.** McQuillan-style tautological inequalities applied to higher-dimensional foliations, with recent attention to singular holomorphic foliations on threefolds *(frontier — verify)*.
- **Nevanlinna theory over non-archimedean and adelic bases**, and over Kähler and parabolic Riemann surfaces (Păun–Sibony's theory of currents on parabolic leaves), aiming at SMTs for maps from covers of $\mathbb{C}$.
- **Higher-dimensional sources.** SMT for $f:\mathbb{C}^m\to X$ with $m>1$ and for meromorphic maps of finite growth index; degeneracy statements for such maps into semi-abelian varieties.

## 8. Future Work

- Prove truncation level $1$ for holomorphic curves into **abelian varieties with non-general-position divisors**, then attempt the general-type case by Albanese fibration (Yamanoi's suggested route).
- Construct **jet differentials on general-type varieties with controlled base locus**, e.g. via Brotbek's Wronskian sections for complete intersections, to identify the Green–Griffiths exceptional locus rather than just its existence.
- Establish the **Kobayashi conjecture for surfaces in $\mathbb{P}^3$** at the sharp degree $d\ge 5$, currently only known for $d\ge 18$–$21$ ranges (Demailly–El Goul; later refinements).
- Develop a **direct analytic proof of the truncated SMT for $\mathbb{P}^2$ and three or more curves** of high degree, which would already yield a function-field $abc$-type statement not obtainable from Ru's theorem.
- Transfer Yamanoi's small-function techniques from $\mathbb{P}^1$ to $\mathbb{P}^n$, closing Cartan's moving-target defect conjecture with truncation.

## 9. Key References

- **[Foundational]** R. Nevanlinna. *Zur Theorie der meromorphen Funktionen.* Acta Mathematica 46 (1925), 1–99.
- **[Foundational]** H. Cartan. *Sur les zéros des combinaisons linéaires de $p$ fonctions holomorphes données.* Mathematica (Cluj) 7 (1933), 5–31.
- **[Foundational]** P. Griffiths, J. King. *Nevanlinna theory and holomorphic mappings between algebraic varieties.* Acta Mathematica 130 (1973), 145–220.
- **[Foundational]** M. Green, P. Griffiths. *Two applications of algebraic geometry to entire holomorphic mappings.* In: The Chern Symposium 1979, Springer, 1980, 41–74.
- **[Foundational]** P. Vojta. *Diophantine Approximations and Value Distribution Theory.* Lecture Notes in Mathematics 1239, Springer, 1987.
- **[Foundational]** D. Drasin. *The inverse problem of the Nevanlinna theory.* Acta Mathematica 138 (1977), 83–151.
- **[SOTA / Recent]** M. Ru. *Holomorphic curves into algebraic varieties.* Annals of Mathematics 169 (2009), 255–267.
- **[SOTA / Recent]** M. Ru, P. Vojta. *A birational Nevanlinna constant and its consequences.* American Journal of Mathematics 142 (2020), 957–991.
- **[SOTA / Recent]** K. Yamanoi. *The second main theorem for small functions and related problems.* Acta Mathematica 192 (2004), 225–294.
- **[SOTA / Recent]** K. Yamanoi. *Holomorphic curves in algebraic varieties of maximal Albanese dimension.* International Journal of Mathematics 26 (2015), 1541006.
- **[SOTA / Recent]** Y.-T. Siu. *Hyperbolicity of generic high-degree hypersurfaces in complex projective space.* Inventiones Mathematicae 202 (2015), 1069–1166.
- **[SOTA / Recent]** D. Brotbek. *On the hyperbolicity of general hypersurfaces.* Publications Mathématiques de l'IHÉS 126 (2017), 1–34.
- **[SOTA / Recent]** D. Brotbek, Y. Deng. *Kobayashi hyperbolicity of the complements of general hypersurfaces of high degree.* Geometric and Functional Analysis 29 (2019), 690–750.
- **[SOTA / Recent]** M. McQuillan. *Diophantine approximations and foliations.* Publications Mathématiques de l'IHÉS 87 (1998), 121–174.
- **[Survey]** J. Noguchi, J. Winkelmann. *Nevanlinna Theory in Several Complex Variables and Diophantine Approximation.* Grundlehren der mathematischen Wissenschaften 350, Springer, 2014.
- **[Survey]** M. Ru. *Nevanlinna Theory and Its Relation to Diophantine Approximation.* 2nd ed., World Scientific, 2021.
- **[Survey]** J.-P. Demailly. *Algebraic criteria for Kobayashi hyperbolic projective varieties and jet differentials.* Proceedings of Symposia in Pure Mathematics 62, AMS, 1997, 285–360.

## 10. Worked Example / Concrete Special Case

**(a) Sharpness in dimension 1.** Take $f(z)=e^z$. Then $T(r,f)=r/\pi+O(1)$, and $f$ omits $0$ and $\infty$, so $N(r,0)=N(r,\infty)=0$ and $\delta(0)=\delta(\infty)=1$. For any $a\ne 0,\infty$, $N(r,a)=T(r,f)+O(1)$ and $\delta(a)=0$. The defect sum is exactly $2$: the SMT constant $q-2$ cannot be improved.

**(b) Truncation in $\mathbb{P}^2$ gives the entire-function $abc$.** Let $a,b,c$ be entire, without common zeros, not all constant, with
$$a+b=c .$$
Set $f=[a:b:c]:\mathbb{C}\to\mathbb{P}^2$. Because $a+b-c=0$, the image lies on the line $L:\ x_0+x_1-x_2=0\cong\mathbb{P}^1$. Restricting, consider instead $g=[a:b]:\mathbb{C}\to\mathbb{P}^1$ and apply Cartan (equivalently Nevanlinna) with the three points $0,\infty,-1$, corresponding to the divisors $a=0$, $b=0$, $c=a+b=0$. Truncation level is $n=1$, so
$$T(r,g)\ \le\ N^{(1)}(r,1/a)+N^{(1)}(r,1/b)+N^{(1)}(r,1/c)\ +\ S(r,g).$$
Since $a,b,c$ have no common zeros, $T(r,g)=\max\{T(r,a),T(r,b),T(r,c)\}+O(1)$ up to normalization. This is precisely the Mason–Stothers/$abc$ statement in the analytic category: the height is bounded by the number of *distinct* zeros.

Concretely, take $a=z^n$, $b=1$, $c=z^n+1$. Then $N^{(1)}(r,1/a)=\log r$, $N^{(1)}(r,1/b)=0$, and $c$ has $n$ simple zeros, giving $N^{(1)}(r,1/c)=n\log r+O(1)$, while $T(r,g)=n\log r+O(1)$. The inequality reads $n\log r\le (n+1)\log r$ — tight to within one unit, and the truncation is essential: without it the left side could be compared against $N(r,1/a)=n\log r$ alone and the statement carries no arithmetic content.

**(c) What breaks in dimension 2.** Replace the line $L$ by a smooth quartic $C\subset\mathbb{P}^2$ and $D=D_1+D_2+D_3$ three curves of degree $2$ in general position on $X=\mathbb{P}^2$. Ru's theorem gives
$$\tfrac12\sum_{j=1}^3 m_{D_j}(r,f)\ \le\ (3+\varepsilon)\,T(r,f),$$
i.e. an untruncated conclusion. No known argument replaces $N_{D_j}$ by $N^{(1)}_{D_j}$ here, because the filtration of $H^0(\mathbb{P}^2,\mathcal{O}(d))$ used in the proof measures only vanishing order along $D_j$ in bulk, not the multiplicity of individual intersection points of $f(\mathbb{C})$ with $D_j$. That single missing bookkeeping step is the gap of §6.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*