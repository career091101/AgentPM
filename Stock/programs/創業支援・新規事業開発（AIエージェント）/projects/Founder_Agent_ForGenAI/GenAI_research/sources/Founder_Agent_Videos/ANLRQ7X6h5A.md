---
title: "YouTube Video: ANLRQ7X6h5A"
video_id: "ANLRQ7X6h5A"
video_url: "https://www.youtube.com/watch?v=ANLRQ7X6h5A"
speaker: "Unknown"
channel: "Unknown"
date: ""
duration: ""
tags:
  - "YouTube"
  - "Transcript"
topics:
  - "General"
summary: |
  Hey everyone. In the last few episodes, we have analyzed Hilbert space, and taken a look at some of kets. In this episode, I want to move on to the physical quantities. In the very first episode, we p...
key_points:
  - "In the very first episode, we posited that"
  - "First, we are going to change our language"
  - "First, given an observable operator, how would"
category: "General"
confidence_level: "medium"
transcript_type: "YouTube Auto-generated"
language: "en-ja-mixed"
source: "Founder_Agent_Videos"
---


# Transcript: ANLRQ7X6h5A

- URL: https://www.youtube.com/watch?v=ANLRQ7X6h5A
- Retrieved at: 2025-12-30T09:57:11+09:00

## Text

- [00:02] Hey everyone.
- [00:22] In the last few episodes, we have analyzed
how particles are represented by kets in our
- [00:25] Hilbert space, and taken a look at some of
the mathematics involved in working with these
- [00:29] kets.
- [00:30] In this episode, I want to move on to the
second half of our framework: how we represent
- [00:34] physical quantities.
- [00:36] In the very first episode, we posited that
physical quantities are represented by linear
- [00:41] operators on our Hilbert space.
- [00:43] Now we are going to further develop this idea
and formalize it in mathematics.
- [00:48] First, we are going to change our language
a bit.
- [00:52] We are going to use the word observable for
any physical quantity that we can measure
- [00:56] out of our particle.
- [00:57] This includes position, momentum, energy,
angular momentum, or any combination of those
- [01:02] – basically anything we can measure and
therefore observe from our particle.
- [01:08] Before digging into the nuance of how we represent
these observables as operators, I want to
- [01:12] remind ourselves about the formal definition
of a linear operator, just to make sure we’re
- [01:16] on the same page.
- [01:20] As you might remember, a linear operator is
a map on a vector space that preserves the
- [01:24] linear structure of the space.
- [01:26] In other words, a linear map satisfies the
following properties: addition is still addition
- [01:32] and scalar multiplication is still scalar
multiplication.
- [01:36] Note that a linear operator is an abstract
map, while a matrix is a representation of
- [01:41] a linear operator in a particular basis.
- [01:43] We’ll see in a bit that quantum mechanics
has no standard basis, so that’s why you
- [01:48] will almost always see us working with the
abstract operators themselves.
- [01:55] Moving back into quantum mechanics, we established
that we suspect physical observables are represented
- [02:00] by some linear operator on our space of kets.
- [02:03] Now let’s finally start digging into this
idea.
- [02:06] First, given an observable operator, how would
we get the possible values that we can measure?
- [02:15] To begin solving this problem, let us look
at angular momentum as an example.
- [02:21] Say we have a particle and an apparatus to
measure angular momentum.
- [02:25] We can take a measurement and know that at
this moment the particle has an angular momentum
- [02:29] of 1.41 Nms; therefore, at this very moment,
the particle has to be represented by a particular
- [02:37] quantum state that corresponds to having that
outcome of angular momentum.
- [02:40] I mean, think about it: the measurement told
us what the angular momentum is, so we can’t
- [02:45] be in a superposition of more than one outcome,
our particle has to be in the state representing
- [02:50] this outcome.
- [02:54] If instead our apparatus told us the particle
had an angular momentum of 2.44 Nms, then
- [02:59] the particle would be in a quantum state corresponding
to that outcome.
- [03:03] Hopefully you see that this would be true
for any possible angular momentum we could
- [03:09] measure.
- [03:11] So what we have is a list of possible measured
values and associated kets representing states
- [03:16] that 100% have that value.
- [03:19] We call these special states definite states.
- [03:22] In these special states our particle has a
definite 100% certain value for angular momentum,
- [03:28] no ifs or buts.
- [03:30] Now, how would we get this list from the angular
momentum operator?
- [03:34] Well we have a list of definite angular momentum
kets and associated values...I don’t know
- [03:40] about you, but to me this screams eigenvalues
and eigenvectors, and this is the right direction
- [03:45] to head.
- [03:47] Most textbooks just state this as a fact,
but hopefully you see why it’s incredibly
- [03:50] reasonable that eigenvectors show up.
- [03:54] So, let’s summarize the conclusion.
- [03:59] Every physical observable is represented by
some linear operator in this vector space.
- [04:05] To figure out all the possible values of that
observable, find the eigenvalues.
- [04:12] To figure out which state corresponds to having
that particular value, find the eigenvector
- [04:17] corresponding to that eigenvalue.
- [04:19] These eigenvectors are called eigenstates,
and represent definite states that 100% have
- [04:24] this value for the observable.
- [04:27] This is the fundamental framework for how
we represent observables in quantum mechanics.
- [04:37] Now let’s relate this to our current understanding
of quantum states.
- [04:40] Ever since the start of the series, we’ve
wanted to represent our particle as a superposition
- [04:45] of all possible outcomes of a measurement.
- [04:48] We now finally have the framework and language
to do so.
- [04:51] We now know that these outcome states are
actually the definite states of the observable,
- [04:56] which are its eigenstates.
- [04:58] So mathematically, being in a superposition
of outcomes is done by being in a linear combination
- [05:04] of an observable’s eigenvectors.
- [05:06] Now, note that we haven’t discussed how
the coefficients relate to probability or
- [05:11] what happens when we actually take the measurement.
- [05:13] Don’t worry, we’ll discuss this in depth
next chapter where we derive the Born rule.
- [05:20] Now, with just this, we can already use our
physicist’s intuition to derive the mathematical
- [05:27] properties that physical observables should
have.
- [05:30] First, observables need to have real eigenvalues.
- [05:34] Intuitively, it doesn’t make sense for a
particle to have 2 + 3i energy.
- [05:40] Physical quantities are inherently real.
- [05:43] Next, observables’ eigenstates must span
the entire vector space.
- [05:52] Remember that the span of a set of vectors
is the subspace formed by all possible linear
- [05:56] combinations of those vectors.
- [05:58] So this property says that linear combinations
of an observables’ eigenstates cover the
- [06:03] entire quantum vector space.
- [06:05] Another way to word this is that any quantum
state can be written as a linear combination
- [06:10] of eigenstates.
- [06:16] This property actually isn’t that hard to
prove, see if you can do it by considering
- [06:20] what it physically means for a particle to
lie outside the eigenstates’ span.
- [06:24] Gave it a shot?
- [06:26] The key is to realize that every single particle
has a value for an observable; meaning, every
- [06:32] particle has some value for position, for
momentum, for energy, etc., so, for example,
- [06:38] there aren’t any particles that have a position
of “none”.
- [06:45] Taking that idea, let’s imagine that the
energy eigenvectors didn’t span the entire
- [06:49] space.
- [06:50] This would imply that there was some quantum
state outside the span, and therefore could
- [06:54] not be written as a superposition of the energy
eigenstates.
- [06:58] So, this quantum state has no possible energy
measurement outcomes, since remember that
- [07:03] the eigenstates represent the definite states
you get from a measurement, and this quantum
- [07:07] state can’t be written in terms of any!
- [07:09] But this isn’t possible, the particle has
to have some value of energy when we measure
- [07:14] it.
- [07:15] Thus, it must be in some superposition of
the energy eigenstates.
- [07:19] This must also be true of every other observable
we can measure.
- [07:23] Therefore, the eigenstates of an observable
must span the entire space.
- [07:29] Lastly, we can actually conclude that the
eigenstates must be mutually orthogonal, i.e.
- [07:37] perpendicular.
- [07:38] We can use the arrow analogy to see why this
is true.
- [07:41] Here we have non-orthogonal states L_1 and
L_2.
- [07:45] Since they aren’t orthogonal, we can decompose
L_1 into two components: one component along
- [07:50] L_2 (which we can write as some scalar times
L2), plus some orthogonal component.
- [07:57] Remember that we defined the definite states
to be states where we are 100% sure that the
- [08:02] particle has that value for the observable.
- [08:04] Yet, here we have that the L_1 state contains
a superposition of the L_2 state, meaning
- [08:10] there’s a chance we could get L_2 if we
took a measurement.
- [08:13] This doesn’t make any sense, and goes against
how we defined these definite states.
- [08:18] Therefore, the eigenstates from an observable
must be mutually orthogonal.
- [08:23] A quick note: you may have noticed that we
implicitly assumed that components should
- [08:27] be decided using orthogonal projections; in
the next chapter, we’ll justify this claim.
- [08:33] So, we have found that an observable’s eigenstates
must satisfy two things: 1.
- [08:40] span the entire vector space, and 2.
- [08:42] be mutually orthogonal (and hence linearly
independent).
- [08:46] What do we call a set of linearly independent
vectors that span your space?
- [08:50] A basis!
- [08:51] And because each state can be normalized,
we just showed that an observable’s eigenstates
- [08:56] must form an orthonormal eigenbasis!
- [08:59] We assumed this previously, but now you see
how we use our intuition to prove it!
- [09:08] So let’s summarize a bit: In quantum mechanics,
all physical observables are represented by
- [09:13] a linear operator.
- [09:15] By just considering physical intuition, we
found that this operator must have an orthonormal
- [09:19] eigenbasis, representing the definite states
of this observable.
- [09:24] The corresponding eigenvalues must be real,
because they represent the values that we
- [09:28] would measure in the corresponding eigenstate.
- [09:32] If you’ve taken a quantum mechanics course
in the past, these properties are usually
- [09:36] derived by assuming observables are hermitian
operators…but haven’t you wondered why
- [09:40] we assume them to be hermitian in the first
place?
- [09:44] In this approach, we get these properties
just from physical intuition, and in chapter
- [09:48] 9, we’ll show how these properties actually
imply that observables are hermitian.
- [09:53] Now, there are still open questions; most
importantly, how do we calculate the probability
- [10:02] associated with each measuring each eigenvalue?
- [10:05] We’ll answer this and derive the Born rule
next episode.
- [10:08] There, we’ll connect everything together
and lay out the full prescription for our
- [10:13] mathematical model of quantum physics.
- [10:17] Thank you so much for watching.
- [10:18] If you have any questions, feel free to leave
them below.
- [10:21] Hope to see you in the rest of the series!