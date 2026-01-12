---
title: "Hey everyone. Before finishing up  our discussion on quantum operators, I want to discuss one more v..."
video_id: "dD-oYfhSKhg"
video_url: "https://www.youtube.com/watch?v=dD-oYfhSKhg"
speaker: "Unknown"
channel: "Unknown"
date: ""
duration: ""
tags:
  - "AI"
topics:
  - "Product Development"
summary: |
  Hey everyone. Before finishing up 
  our discussion on quantum operators,
  I want to discuss one more very important 
key_points:
  - "Hey everyone. Before finishing up"
  - "our discussion on quantum operators,"
  - "I want to discuss one more very important"
  - "These operators are fairly intuitive, and"
  - "Here’s what I want to know: is there an operator U"
  - "which is equal to the product of the"
  - "with this alternative formula, we can see that"
  - "we are intuitively asking if we have an operator"
category: "AI & Technology"
confidence_level: "high"
---

# Transcript: dD-oYfhSKhg

- URL: https://www.youtube.com/watch?v=dD-oYfhSKhg
- Retrieved at: 2025-12-30T11:43:06+09:00

## Text

- [00:19] Hey everyone. Before finishing up 
our discussion on quantum operators,
- [00:23] I want to discuss one more very important 
class of operators: unitary operators.
- [00:29] These operators are fairly intuitive, and 
they’ll become foundational to the notion
- [00:33] of change in quantum mechanics. 
With that, let’s get into it!
- [00:39] Like we did when introducing Hermitian operators, 
let’s start with the inner product of two vectors.
- [00:45] Here’s what I want to know: is there an operator U
- [00:48] such that when I transform both vectors 
by U, the inner product stays the same?
- [00:54] Remember that the inner product 
is a generalized dot product,
- [00:56] so let’s use that for some intuition and look 
at the alternate formula for the dot product,
- [01:01] which is equal to the product of the 
lengths times the cosine of the angle. Well,
- [01:06] with this alternative formula, we can see that 
we are intuitively asking if we have an operator
- [01:10] U such that after transforming both vectors, the 
lengths and the angle between them stays the same.
- [01:17] When we frame the question this way, it’s clear 
that one transformation that satisfies this
- [01:21] is a simple rotation! The lengths stay the 
same, and the relative angle is preserved.
- [01:30] Now, rotations are just one type of 
operation that preserve the inner product,
- [01:34] and in general we call operators that 
preserve the inner product unitary operators.
- [01:40] A unitary operator is defined as any operator 
that satisfies the following property,
- [01:45] its hermitian conjugate is equal to 
its inverse. Now, it isn’t immediately
- [01:50] clear that this property implies inner 
product preservation, so let’s prove it.
- [01:55] Let’s start with an inner product 
and apply U to both vectors.
- [01:59] Let’s then pull out the right operator. If we want 
to switch the left operator to act on the right,
- [02:04] remember that we just use the hermitian conjugate. 
The hermitian conjugate is equal to the inverse,
- [02:10] hence, we get U times its inverse, which 
by definition must equal the identity.
- [02:15] Hence, the inner product is 
equal to its original value!
- [02:20] Although unitary operators are an abstract 
concept, I think you should always keep
- [02:24] the intuition that these operators are just 
‘generalized rotations’. They move vectors all
- [02:30] over the place, but they always intuitively keep 
the lengths and corresponding angles the same.
- [02:39] Before connecting this to quantum mechanics, 
let’s lay down one more fundamental property
- [02:43] of unitary operators. Let’s say omega is a 
normalized eigenvector of unitary operator U.
- [02:50] Since omega is normalized, its inner 
product with itself must be equal to one.
- [02:55] Now, let’s act U on omega, and 
take its inner product again.
- [03:00] Since omega is an eigenvector, U will 
simply return the corresponding eigenvalue.
- [03:06] The right slot of the inner product is linear, so 
we can just pull out lambda, and the left slot is
- [03:10] antilinear, so we pull out the complex conjugate 
of lambda. This inner product is then equal to
- [03:16] one, and remember that a complex number times 
its conjugate is equal to its magnitude squared.
- [03:22] Now, U preserves the inner product, 
so we have that this must be equal
- [03:26] to the inner product without 
U, which is just equal to one.
- [03:30] So we have just derived one of the 
fundamental properties of unitary operators:
- [03:34] the eigenvalues of a unitary operator must have 
magnitude one, also known as unit complex numbers.
- [03:42] This is where the ‘unitary’ name comes 
from, all the eigenvalues have unit length.
- [03:47] This property should also make intuitive 
sense! Eigenvalues tell you how much the
- [03:52] operator scales its eigenvector. So if we think 
of unitary operators as generalized rotations,
- [03:58] they intuitively shouldn’t change 
the length of their eigenvectors.
- [04:01] Therefore, it makes sense that the 
eigenvalues have to have unit length.
- [04:09] Great, so why do we care about unitary operators 
in quantum mechanics? Well what do inner products
- [04:15] represent in quantum mechanics? 99 percent of 
the time, inner products are used to calculate
- [04:20] probabilities! So, since unitary operators 
preserve the inner product, if we act a
- [04:26] unitary operator on every vector in our space, the 
probability of getting a particular measurement
- [04:31] wouldn’t change. Likewise, the total probability 
of our state would still be equal to one. So,
- [04:38] the big realization is that unitary operators 
conserve probability in quantum mechanics!
- [04:48] Hopefully I don’t have to convince you that 
conserving probability is a big deal. I mean,
- [04:53] think about all the things we want to do to a 
particle, shown in white, and its system, shown
- [04:57] in blue, while still having its total probability 
be conserved: We may want to take our particle
- [05:03] and its system, and rotate it; or, we may want to 
take our particle and its system and move it over;
- [05:11] or, most importantly, we may want to 
study how our particle evolves in time.
- [05:16] In all of these processes, we would hope 
that total probability is always equal to 1.
- [05:22] Hence, you may expect that things like the 
rotation operator, translation operator,
- [05:26] and time evolution operator will have to 
be unitary, since these transformations
- [05:31] should all conserve probability. In two 
episodes, we’ll flesh this idea out when
- [05:37] we derive the schrodinger equation, and 
prove that time evolution must be unitary.
- [05:45] With that, we’ve covered everything we 
need to know about unitary operators.
- [05:49] There’s a lot more to say about them, 
but we’ve covered the fundamentals that
- [05:53] we need to derive the schrodinger equation. 
They’re fairly simple and intuitive, right?
- [05:59] Next episode, we’ll take a quick pit stop 
into generators in classical physics,
- [06:03] using the lagrangian framework. Generators are 
always brought up when deriving the schrodinger
- [06:08] equation and the momentum operator, but I haven’t 
seen anyone actually take the time to talk about
- [06:13] what they intuitively are in classical 
physics. Once we have that, we’ll finally
- [06:18] see how generators and unitary evolution 
come together into the infamous equation.
- [06:24] With that, thank you so much 
for watching. As always,
- [06:27] let me know if you have any questions. 
Hope to see you in the rest of the series!
