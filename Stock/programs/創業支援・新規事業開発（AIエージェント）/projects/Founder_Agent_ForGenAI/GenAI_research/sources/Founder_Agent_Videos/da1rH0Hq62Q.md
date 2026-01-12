---
title: "Hello everyone. In the last couple of episodes, we’ve been working with observables and their repres..."
video_id: "da1rH0Hq62Q"
video_url: "https://www.youtube.com/watch?v=da1rH0Hq62Q"
speaker: "Unknown"
channel: "Unknown"
date: ""
duration: ""
tags:
  - "AI"
  - "Tutorial"
topics:
  - "Product Development"
summary: |
  In the last couple of episodes, we’ve been
  working with observables and their representation
  as linear operators within our vector space.
key_points:
  - "In the last couple of episodes, we’ve been"
  - "In this episode, I want to introduce Hermitian"
  - "chapter 7 on observables, since we will be"
  - "This is just acting the operator M on the"
  - "we also commonly write this as follows."
  - "This is just a ket representing the vector"
  - "that looks like this, it’s sometimes convenient"
  - "Remember that this is just the inner product"
category: "Technical Tutorial"
confidence_level: "high"
---

# Transcript: da1rH0Hq62Q

- URL: https://www.youtube.com/watch?v=da1rH0Hq62Q
- Retrieved at: 2025-12-30T11:44:29+09:00

## Text

- [00:01] Hello everyone.
- [00:14] In the last couple of episodes, we’ve been
working with observables and their representation
- [00:25] as linear operators within our vector space.
- [00:28] In this episode, I want to introduce Hermitian
operators, and show you how they connect to
- [00:32] our physical observables.
- [00:34] As a heads up, make sure you’ve watched
chapter 7 on observables, since we will be
- [00:38] using results derived in that chapter!
- [00:43] To begin, I want to introduce some slightly
new notation.
- [00:47] We have worked with the following expression
a lot.
- [00:51] This is just acting the operator M on the
ket phi.
- [00:54] Because M acting on phi returns another vector,
we also commonly write this as follows.
- [01:01] This is just a ket representing the vector
we would get when we act M on phi.
- [01:08] So when we have an inner product expression
that looks like this, it’s sometimes convenient
- [01:12] to write it like this.
- [01:14] Remember that this is just the inner product
with psi and M phi.
- [01:22] So with that, here’s the set up and geometric
intuition.
- [01:25] Say we have this inner product.
- [01:28] Remember that the inner product is basically
the dot product, so let’s rely on that for
- [01:32] some intuition.
- [01:34] Remember that we have the following equivalent
expression for the dot product.
- [01:37] So geometrically, this inner product basically
says “act M on phi, and then measure the
- [01:44] new angle between the new vector and psi,
scaled by their lengths.”
- [01:52] Now here’s what we want to investigate:
do we have an operator N that we can apply
- [01:56] to psi instead, and give an equal inner product?
- [01:59] Geometrically, we’re asking if we have an
operator that allows us to instead move psi,
- [02:05] and still give us the same magnitudes times
angle of the two vectors?
- [02:09] And this must be true for any two vectors
phi and psi that we choose.
- [02:15] It turns out, there is such an operator!
- [02:17] This operator is called the hermitian adjoint.
- [02:20] We designate the hermitian adjoint by taking
our operator and adding a dagger to the front
- [02:24] of it.
- [02:25] The fundamental property of the hermitian
adjoint is that it satisfies the following
- [02:29] property for any vector phi and psi.
- [02:34] Now, there are few properties of the hermitian
adjoint that I want to show you, but their
- [02:40] proof is not very enlightening; however, I
encourage you to practice bra-ket notation
- [02:45] and try proving them yourself – they’re
fairly easy proofs.
- [02:49] First, the hermitian adjoint of the hermitian
adjoint is the operator itself.
- [02:55] Second, the hermitian adjoint of a sum is
the sum of the hermitian adjoints.
- [03:02] Lastly, and often most importantly, the hermitian
adjoint of a product of operators is calculated
- [03:09] by switching their order and taking the individual
hermitian adjoints.
- [03:13] If you’re going to prove any one of these,
this last one is the one to try.
- [03:22] Before moving on to the connection to quantum
mechanics: I want to discuss some common hermitian
- [03:26] adjoints that you’ll encounter.
- [03:28] First, say we have a scalar number.
- [03:32] What is the hermitian adjoint of this?
- [03:34] Well, we can set up an inner product with
the scalar number as the operator.
- [03:39] We want to know how to move this scalar to
the other side of the inner product.
- [03:42] Well, we can pull the scalar out of the right
side of the inner product since the right
- [03:47] side is linear.
- [03:48] Then, we can remember that the left side of
the inner product is antilinear, so we have
- [03:53] to complex conjugate the scalar to move it
into the left side.
- [03:56] Therefore, we have that the hermitian adjoint
of a scalar is just the complex conjugate!
- [04:02] This is an important fact that you should
remember.
- [04:07] Second, what is the hermitian adjoint of a
ket?
- [04:13] Now this might seem like a weird question,
since we’ve been considering a ket as a
- [04:17] vector, not an operator – but bear with
me as we try to make sense of it.
- [04:22] Instead of working with the ket by itself,
let’s work with it within an inner product.
- [04:27] So what is the hermitian adjoint of an inner
product?
- [04:31] Well an inner product is just a number, so
we get the complex conjugate, which just flips
- [04:36] the inner product.
- [04:39] But, we can also evaluate the hermitian adjoint
of the inner product by first breaking up
- [04:45] our inner product, and using our rule for
adjoint products: we switch the positions,
- [04:51] and then take the individual hermitian adjoints.
- [04:55] This expression and the one we previously
found must both be equal.
- [04:59] Since phi and psi are both completely arbitrary,
this seems to point to the fact that the hermitian
- [05:04] adjoint of a ket is a bra, and the hermitian
adjoint of a bra is a ket.
- [05:11] Now this is more of a justification rather
than a rigorous proof.
- [05:14] But this really is true; in the description
I’ve linked a stack exchange post that goes
- [05:18] more in-depth into how we can consider a ket
as an operator to prove this.
- [05:25] So, how do these hermitian adjoints connect
with quantum physics?
- [05:31] Well we can ask ourselves, “what is the
hermitian adjoint of an observable?”
- [05:36] To answer this, let’s go over what we know
about observables so far.
- [05:41] Remember that we found that physical observables
are represented by linear operators whose
- [05:45] eigenvectors represent definite states and
eigenvalues represent the corresponding measured
- [05:50] value.
- [05:52] Observables must also follow rules from our
physical intuition.
- [05:55] Let’s recap the rules we derived in chapter
7:
- [05:59] First, the eigenvalues must be real, since
measured quantities are obviously real.
- [06:06] Second, the eigenvectors must span the whole
space, since each quantum state must carry
- [06:12] some value for the observable.
- [06:14] Last, the eigenvectors must be orthogonal,
otherwise, they wouldn’t be definite states.
- [06:20] These last two allow us to conclude that observables
have an orthonormal eigenbasis.
- [06:29] Given these properties of observables, I want
to show you an incredibly useful way to express
- [06:34] observables that will be helpful in finding
the adjoint.
- [06:37] First, let’s consider our observable acting
on an arbitrary quantum state.
- [06:43] Since this operator has an orthonormal eigenbasis,
we can expand our quantum state in this eigenbasis,
- [06:48] and move the operator into the sum.
- [06:53] Since these are eigenvectors, the operator
will just give us the corresponding eigenvalue.
- [06:59] Now what about the coefficients, c_i?
- [07:02] Remember that we previously derived the following
expression for the coefficients (and if you
- [07:06] don’t remember, it’s really easy to verify).
- [07:09] So we can substitute this in.
- [07:15] Then we can move the inner product over to
the right.
- [07:18] Now using the power of bra-ket notation, we
can break up this inner product.
- [07:24] Since psi is the same for every term of the
sum, we can pull it out.
- [07:28] So, we found that the action of the observable
on any psi is the same as the action of this
- [07:34] sum of operators.
- [07:35] In other words, they are equal!
- [07:38] So we’ve found that observables can be written
as a sum involving their eigenstates and real
- [07:42] eigenvalues.
- [07:45] If we have an observable with a continuous
eigenbasis, we can follow the same logic to
- [07:50] derive the following analogous expression.
- [07:53] So, why is this useful?
- [07:56] Well, let’s use this form for observables
to see what their hermitian adjoints are.
- [08:01] We’ll do the discrete case here, but note
that the logic is the same in the continuous
- [08:05] case.
- [08:06] First, let’s use the property that the hermitian
adjoint of a sum is the sum of the hermitian
- [08:11] adjoints.
- [08:13] Next, let’s use our product rule for the
hermitian adjoint – we flip the order and
- [08:20] then distribute the dagger.
- [08:24] The hermitian adjoint of a bra is a ket, the
adjoint of the ket is a bra, and the adjoint
- [08:29] of a scalar is the complex conjugate.
- [08:34] Remember that the eigenvalues have to be real,
since these represent the outcome values that
- [08:38] we can measure.
- [08:40] So this just gives us the same eigenvalue,
and we can move it back to the left since
- [08:44] it’s a scalar.
- [08:46] And check it out, we get the exact same operator
back!
- [08:50] So we’ve just proved that the hermitian
adjoint of a physical observable is itself!
- [08:55] We have a special name for operators that
are their own hermitian adjoints; we call
- [08:59] them hermitian operators, which I agree is
sort of a confusing name, but it’s what
- [09:03] we call them.
- [09:05] So we have found that all observables are
hermitian operators, and therefore they satisfy
- [09:10] the following inner product property.
- [09:13] Since we deal with observables all the time
in quantum mechanics, this property is really
- [09:18] handy, so it’s worth remembering.
- [09:21] I want to take a step back and review how
we got to this conclusion.
- [09:25] In almost all quantum mechanics textbooks,
observables are simply declared to be hermitian.
- [09:29] From this declaration, they usually then use
some statement of the spectral theorem to
- [09:34] conclude that hermitian operators have an
orthonormal eigenbasis with real eigenvalues.
- [09:40] This usually ends with some statement like,
“these properties conveniently model physical
- [09:45] observables!”
- [09:47] What I wanted to show you is that you can
instead use physical intuition to come to
- [09:50] the conclusion that observables must be hermitian
operators.
- [09:55] We did this by first finding that observables
should be represented by linear operators.
- [09:59] Then, we derived that if they were to model
real physical quantities, they need to satisfy
- [10:04] three properties.
- [10:06] Finally, we found that this leads to the fact
that observables must be hermitian operators.
- [10:14] I find this approach much more satisfying,
since we use our physical intuition to develop
- [10:18] the math, rather than the other way around.
- [10:21] Although the spectral theorem is incredibly
important, I thought it would be useful to
- [10:25] show you how the universe’s intuition drops
the hermiticity of observables in our lap.
- [10:32] So, hopefully you see that there’s a good
amount of intuition behind why observables
- [10:39] are hermitian in quantum mechanics.
- [10:41] Now that we know this fact, we can finally
start digging into some of the neat properties
- [10:45] that observables have.
- [10:47] Starting with the next episode, we’ll go
over the ubiquitous commutator and how it
- [10:52] relates to the infamous uncertainty principle,
which hopefully won’t be so mysterious after
- [10:56] we’ve attacked it.
- [10:59] With that, thank you so much for watching.
- [11:02] As always, let me know if you have any questions.
- [11:04] Hope to see you in the rest of the series!
