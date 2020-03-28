---
title: Convolution of Gaussians is Gaussian
---

A gaussian is a function of the form $f(x)=Ae^{-(x-\mu)^2/2\sigma^2}$ for some constant $A$ -- when $A$ is chosen
to make the total integral of $f$ equal to $1$, you obtain the probability distribution function for a normally
distributed random variable of mean $\mu$ and variance $\sigma^2$.

In class I mentioned the result that the convolution of two gaussian functions is again a gaussian.
This is usually proved by:

- showing that the Fourier transform $\hat{f}$ of a gaussian $f$ is a gaussian;
- observing that the product $fg$ of gaussians $f$ and $g$ is a gaussian 
- using the convolution theorem to conclude that if $f$ and $g$ are gaussians, then so is

$$
f*g = \widehat{\hat{f}\hat{g}}.
$$

However, one can also simply work out the integral.  If $f=e^{-(x-\mu)^2/\sigma^2}$ and $g=e^{-(x-\nu)^2/\tau^2}$
then

$$
(f*g)(x) = \int e^{-(t-\mu)^2/\sigma^2-(x-t-\nu)^2/\tau^2}\,dt.
$$

**Lemma:** Suppose $Q(x,t)$ is a quadratic function in two variables of the form

$$
Q(x,t) = A(t-r)^2+B(x-t-s)^2
$$

where $A$,$B$,$r$, and $s$ are constants.  Then there are constants $A'$,$B'$, $r'$ and $s'$
so that

$$
Q(x,t) = A'(x-r')^2+B'(t-x-s').
$$

**Proof:** This is an exercise in completing the square.  Write
$$
Q(x,t)=ax^2+bxt+ct^2+dx+et+f.
$$
First complete the square to eliminate the $et$ term.  Let $t_1=t-\frac{e}{2c}$.
Then:

$$
Q(x,t)=ax^2+bx\left(\frac{e}{2c}\right)+dx+ct_1^2-\left(\frac{e}{2c}\right)^2+f+bxt_1
$$

Next complete the square to eliminate the $xt_1$ term by setting $t_2=t_1-\frac{b}{2c}x$ so that

$$
Q(x,t)=ax^2+(b\left(\frac{e}{2c}\right)+d)x+c(t_2-\frac{b}{2c}x)^2-\left(\frac{b}{2c}\right)^2-\left(\frac{e}{2c}\right)^2+f
$$

Finally complete the square on the pure $x$ terms to get the desired form.

**Proposition:** $(f*g)$ is a gaussian.

**Proof:** By the lemma, $(f*g)$ can be written

$$
(f*g)(x)=\int e^{-A(x-r)^2}e^{-B(t-x-s)^2}dt=e^{-A(x-r)^2}\int_{-\infty}^{\infty} e^{-B(t-x-s)^2}dt
$$

Since the integral runs from $-\infty$ to $\infty$ its value is independent of the value of $x$
so the integral yields a constant $C$ leaving

$$
(f*g)(x) = Ce^{-A(x-r)^2}
$$

which is a gaussian.

**Remark:** If you have more patience than I you can get the constants exactly.  The full
result is that if $F$ is the gaussian distribution with mean $\mu$ and variance $\sigma$,
and $G$ is the gaussian distribution with mean $\nu$ and variance $\tau$, then
$F*G$ is the gaussian distribution with mean $\mu+\nu$ and variance $\sigma^2+\tau^2$.

In particular, following up on a question from class,
the $n$-fold repeated convolution with the standard gaussian of mean zero and variance $\sigma^2$
is equivalent to convolution with a gaussian of mean zero and variance $n\sigma^2$.

**Remark 2:** For the probabilists, if $X$ and $Y$ are independent normally distributed random variables
with mean $\mu$ and $\nu$ and variances $\sigma$ and $\tau$ respectively, then the
distribution of $X+Y$ is the convolution of the associated gaussian distribution functions.
From this point of view the fact that the mean and variance of $X+Y$ are $\mu+\nu$ and $\sigma^2+\tau^2$
respectively are natural.



