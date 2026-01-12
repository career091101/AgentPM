---
title: "YouTube Video: A7yDvA8VQC8"
video_id: "A7yDvA8VQC8"
video_url: "https://www.youtube.com/watch?v=A7yDvA8VQC8"
speaker: "Unknown"
channel: "Unknown"
date: ""
duration: ""
tags:
  - "YouTube"
  - "Transcript"
  - "Startup"
topics:
  - "Startup"
summary: |
  Hi everyone! In the last episode, we derived the schrodinger energy operator, also called the Hamiltonian. So to begin working with the schrodinger equation, operator, which can be written as the mome...
key_points:
  - "watching Chapter 13 first, if you haven’t"
category: "General"
confidence_level: "medium"
transcript_type: "YouTube Auto-generated"
language: "en-ja-mixed"
source: "Founder_Agent_Videos"
---


# Transcript: A7yDvA8VQC8

- URL: https://www.youtube.com/watch?v=A7yDvA8VQC8
- Retrieved at: 2025-12-30T09:55:41+09:00

## Text

- [00:23] Hi everyone!
- [00:24] In the last episode, we derived the schrodinger
equation, and found that it depended on the
- [00:28] energy operator, also called the Hamiltonian.
- [00:32] So to begin working with the schrodinger equation,
we need to dig into the details of the energy
- [00:37] operator, which can be written as the momentum
squared divided by 2m plus the potential energy.
- [00:44] Since the momentum operator shows up in the
hamiltonian, I want to spend this episode
- [00:48] really digging into how the momentum operator
works in quantum mechanics, and why it acts
- [00:52] as a derivative on our wavefunction.
- [00:54] We’re going to be using a ton of the results
we derived last episode, so I highly recommend
- [01:00] watching Chapter 13 first, if you haven’t
already.
- [01:03] With that, let’s dive into it.
- [01:08] To start, let’s begin like we did last episode,
but instead of looking at the time evolution
- [01:12] operator, we now want to analyze the translation
operator.
- [01:16] What does the translation operator do?
- [01:18] Well, when acting on a position eigenstate,
it simply translates it to the position eigenstate
- [01:23] corresponding to x plus a.
- [01:27] Given this definition here, it’s pretty
easy to see how the translation operator acts
- [01:31] on an arbitrary quantum state.
- [01:34] We can always expand the quantum state in
the position basis, and if this continuous
- [01:38] linear combination is unfamiliar to you, I
recommend you refresh with chapter 2 of the
- [01:43] series.
- [01:44] We can then move the translation operator
in, then act it on the ket, which will just
- [01:49] translate them all over by a.
- [01:50] Now, looking at what we have here, we can
see that the translation operator has a pretty
- [01:58] intuitive interpretation.
- [02:01] Since this operator shifts all the position
kets of our quantum state over, this operator
- [02:05] intuitively takes our quantum state and shifts
it over by distance a.
- [02:09] Now, with this intuition, we can already extract
something incredibly important: since we’re
- [02:17] doing nothing else to the particle, just moving
it over by distance a, we should expect that
- [02:22] the total probability of our particle should
still be equal to one.
- [02:26] In other words, spatial translations should
conserve total probability.
- [02:30] I mean all we’re doing is moving stuff over!
- [02:34] It’d be weird if the total probability were
no longer one for some reason.
- [02:38] Since we calculate the total probability using
the inner product of our state with itself,
- [02:43] this gives us the following equation which
must hold true.
- [02:47] Now, note that this is the same equation we
had for the time evolution operator last episode!
- [02:53] And if you remember, we painstakingly showed
that this condition here, along with the intuition
- [02:58] that translations should be reversible, imply
that this operator must be unitary.
- [03:05] We went through the full proof back then,
and it would be 100% identical to the situation
- [03:09] we have here.
- [03:11] Thus, spatial translations must be unitary
in quantum mechanics!
- [03:21] With that, we now want to find out how this
translation operator actually works.
- [03:26] Let’s just follow our lead from last episode,
and surmise that it would be much simpler
- [03:30] to look at the action of the operator over
some infinitesimally small translation dx.
- [03:37] Exactly like last episode, we could then taylor
expand this operator, using our intuition
- [03:41] that the translation operator for a = 0 is
just the identity, since it keeps our particle
- [03:47] in place.
- [03:49] Then we apply both sides to some initial position
ket.
- [03:54] On the left, the translation operator acting
on the ket x will just give us the ket x plus
- [03:59] dx.
- [04:00] So, after moving things around and dividing
by dx, we would get the following equation.
- [04:14] Then taking dx to zero, we have the definition
of the derivative on the left, and the higher
- [04:18] order terms vanish, so we get the following
equation.
- [04:23] Remember that this is exactly what we did
in more detail last episode.
- [04:28] Now, this still doesn’t look like much,
but we haven’t yet input the information
- [04:33] that T is unitary!
- [04:36] Just like for the time evolution operator,
this is done by applying the unitary condition
- [04:40] over a tiny displacement dx, and if we do
exactly what we did last episode where we
- [04:46] taylor expand both operators, this allows
us to conclude that the derivative of T is
- [04:51] antihermitian, which means that it satisfies
this property here.
- [05:01] Since the derivative of T is antihermitian,
then if we multiply Tdot by i, then take the
- [05:07] hermitian conjugate, we will get a negative
sign from both i and Tdot, which will cancel
- [05:12] out, giving us the exact same thing back.
- [05:16] In other words, this must be equal to some
hermitian operator.
- [05:21] Moving the i over, we get the following equation
for the derivative of T, where H is some yet
- [05:25] to be determined hermitian operator.
- [05:32] Now let’s plug this into our differential
equation, and move the i over.
- [05:38] So, what hermitian operator do we expect on
the right hand side here?
- [05:43] Well, here is where we need to use our classical
physics intuition.
- [05:47] We can call back to episode 12, where we found
that in classical physics, if we wanted to
- [05:51] generate a change in the position of the lagrangian,
which was like a classical state, we look
- [05:56] to changes in momentum.
- [05:58] In other words, momentum is the generator
of spatial change.
- [06:01] Thus, it seems that if we want to generate
a change in the position of a quantum state,
- [06:06] we should also look to momentum.
- [06:08] Hence, we use our physics intuition to assert
that this hermitian operator on the right
- [06:13] must be the momentum operator.
- [06:15] Again, I know this can feel like a leap of
faith, but in a moment, we’ll see that all
- [06:20] this generator business is an established
pattern in quantum mechanics, and not as much
- [06:25] of a leap as it seems – just keep in mind
that it’s uncannily similar to the leap
- [06:30] we made for the schrodinger equation.
- [06:32] Let’s do one last thing before revealing
this mystical pattern.
- [06:38] Like last episode, we need to make sure the
units are consistent.
- [06:41] On the left, the derivative gives us units
of inverse meters, and on the right, we have
- [06:46] units of momentum, which you can show can
be written as joule seconds per meter.
- [06:51] So to match the units on both sides, we just
have to add a constant with units of energy
- [06:55] times seconds, or Joule seconds.
- [06:58] Like with the schrodinger equation, this constant
is measured experimentally, and is again the
- [07:02] reduced planck constant.
- [07:06] So, we’ve found an equation showing how
the momentum operator acts on a position ket!
- [07:15] Again, notice how similar this equation is
to the schrodinger equation we derived last
- [07:20] episode, and all the terms in the momentum
equation come from the same fundamental principles.
- [07:26] So, what are we to make of this?
- [07:29] I really want you to notice that there is
a pattern here, and one of the biggest gifts
- [07:34] of being a physicist is discovering patterns
in math and nature.
- [07:39] So what is this pattern?
- [07:41] Well, we first start with a transformation
operator that depends on some parameter, like
- [07:46] time evolution or spatial translation.
- [07:50] We then reason that this transformation must
preserve total probability, which we proved
- [07:55] must imply that the transformation is unitary.
- [08:01] We then look at how the operator acts over
a differential value for the parameter.
- [08:06] Doing this and using the unitary property,
we get an equation of the following form:
- [08:11] i times the derivative with respect to our
parameter equals the action of some hermitian
- [08:15] operator.
- [08:17] We then use our intuition from classical physics
to find what the generator of this transformation
- [08:22] is, and state that this hermitian operator
must be whatever that generator is, so for
- [08:28] time evolution, this generator was energy,
and for spatial translations, the generator
- [08:33] was momentum.
- [08:35] We then insert a factor of hbar to match the
units on both sides.
- [08:41] So following this pattern, we found that time
evolution gave us the schrodinger equation,
- [08:49] spatial translations gave us the action of
the momentum operator, and by following this
- [08:54] same pattern, momentum translations would
give us the action of the negative position
- [08:58] operator, and rotational changes would give
us the action of the angular momentum operator.
- [09:06] Note that the negative that shows up in front
of the position operator is necessary to keep
- [09:09] our quantum theory consistent – if it weren’t
there, then it would actually contradict the
- [09:14] momentum operator equation.
- [09:17] Now, most textbooks don’t note this pattern,
so I want to take a moment to appreciate how
- [09:22] beautiful this is.
- [09:24] We see that the Schrodinger equation is actually
a special case of a much more general pattern
- [09:29] involving transformations and generators in
physics.
- [09:33] Many of you have asked what observables actually
do in our quantum vector space; well, you’re
- [09:37] looking at it: the action of your favorite
observable is to generate some differential
- [09:42] change in your quantum state.
- [09:44] So, hopefully you see why I really like the
generator approach to deriving the Schrodinger
- [09:48] equation – it’s based on a very general
and powerful pattern in physics.
- [09:55] Generators and symmetries form the foundation
of how we understand modern physics, and the
- [09:59] pattern you see here only scratches the surface.
- [10:04] Last thing, notice the similar structure between
these equations and the classical generator
- [10:08] equations we derived in chapter 12.
- [10:11] I mentioned in that chapter that the lagrangian
is somewhat like a classical state, analogous
- [10:16] to the quantum state.
- [10:18] Hopefully seeing these equations adds some
credence to that claim.
- [10:23] Now, although we could dedicate time to each
individual generator equation, I want to spend
- [10:30] the rest of this episode discussing the momentum
operator.
- [10:34] First, note that we found the action of the
momentum operator on a position ket, but I
- [10:39] want to know what it does to the position
wavefunction.
- [10:43] To do this, let’s act the momentum operator
on a quantum state, and then expand that quantum
- [10:49] state in the position eigenbasis.
- [10:53] We can move the momentum operator into the
integral, and since the wavefunction is just
- [10:57] the scalar coefficient in this infinite linear
combination, we can pass the momentum operator
- [11:02] on to the position ket.
- [11:04] Using what we just derived, we know that the
action of the momentum operator on a position
- [11:08] ket is equal to i hbar times the position
derivative.
- [11:13] Now, here is where we need to be a little
clever.
- [11:18] We are going to use integration by parts to
move the derivative from the ket to the wavefunction.
- [11:24] When integrating by parts, we first get a
boundary term evaluated at plus minus infinity,
- [11:30] then we subtract the integral where we’ve
switched the derivative.
- [11:34] If our wavefunction is to be normalizable,
then our wavefunction psi must vanish at plus
- [11:39] minus infinity, therefore the boundary term
must equal zero.
- [11:43] So, in all, we’ve found the following.
- [11:48] So, what does this say?
- [11:52] This says that when acting the momentum operator
on our quantum state, what it does is change
- [11:56] the wavefunction in front of the position
ket by taking its derivative and multiplying
- [12:00] by -ihbar.
- [12:02] So, we have found that the momentum operator
acts on the position wavefunction as follows.
- [12:09] This is something that’s usually introduced
in the first few chapters of every quantum
- [12:13] textbook, but rarely do they show where it
comes from.
- [12:17] Hopefully you now understand how we got to
this point, from start to finish.
- [12:25] Really quick, note that sometimes you see
expressions like the following.
- [12:30] This is technically an abuse of notation,
since remember that operators act on kets,
- [12:35] not scalar wavefunctions.
- [12:38] If you want an expression like this, then
you need to write the following.
- [12:44] In other words, when you act the momentum
operator on your state, and then project onto
- [12:48] the position basis with the position bra,
you get the right hand side.
- [12:53] More simply, the action of the momentum operator
in the position basis is -i hbar times the
- [12:58] derivative.
- [13:00] This keeps all our bra-ket formalism consistent.
- [13:05] So, now that we have this, let’s go back
to the schrodinger equation and finally see
- [13:12] what it looks like in the position basis.
- [13:15] First we write the hamiltonian as kinetic
energy plus potential energy.
- [13:21] Let’s now take the inner product with a
position ket on both sides which projects
- [13:27] everything onto the position basis.
- [13:31] On the left, the position bra doesn’t depend
on time, so we can move it inside the derivative,
- [13:36] which becomes a partial derivative since we
now also have position as a variable.
- [13:41] The inner product of x and psi just gives
us the coefficient in the position basis,
- [13:45] in other words, we get the wavefunction.
- [13:50] On the right, we can use the result we derived
for how the momentum operator acts in the
- [13:54] position basis.
- [13:56] Doing this for each p gives us the following.
- [13:59] Finally, for the potential energy term, since
the position state is an eigenstate of the
- [14:05] position operator, the potential energy operator
will return the same thing, except with x
- [14:10] hat replaced by the eigenvalue x.
- [14:16] And there it is, we’ve derived the equation
we all saw in our introductory quantum classes,
- [14:21] the position-basis Schrodinger equation.
- [14:25] I really want to emphasize that this equation
is specific to the position basis.
- [14:35] We can also ask how the schrodinger equation
looks in the momentum basis.
- [14:39] To do this, we would do basically the same
thing, except we would now project both sides
- [14:43] of the schrodinger equation onto the momentum
basis by taking the inner product with a momentum
- [14:47] ket as shown.
- [14:50] Like before, on the left the momentum bra
moves into the derivative, and we get the
- [14:54] partial time derivative of the inner product
of p and psi, which is just the momentum wavefunction.
- [15:01] In the kinetic energy term on the right, the
momentum state is an eigenstate of the momentum
- [15:05] operator, so this will just give us the momentum
eigenvalue squared.
- [15:10] Now, in the potential energy term on the right,
we are asking about the action of the position
- [15:16] operator after projecting onto the momentum
basis.
- [15:20] If you were to follow our logic from this
episode, but now on the position operator,
- [15:24] you would find that the action of the position
operator in the momentum basis is as follows.
- [15:31] So in the potential energy term, we would
replace x-hat with the following derivative.
- [15:41] And here it is, the momentum-basis schrodinger
equation.
- [15:45] It’s used much less than the position basis
schrodinger equation, but it’s still handy
- [15:49] to have in your back pocket.
- [15:54] Lastly, if you take the schrodinger equation
and project into the energy eigenbasis by
- [16:01] taking an inner product with an energy eigenvector,
it’s easy to show that you get the following
- [16:05] equation, where c_i is the basis coefficient
corresponding to the i^th energy eigenstate,
- [16:11] and we’ve assumed the hamiltonian was time
independent.
- [16:18] This is the energy-basis schrodinger equation.
- [16:22] So, here are some of the different basis-representations
of the schrodinger equation.
- [16:29] Again, this isn’t something that you see
in many textbooks, they usually just throw
- [16:33] the first one at you and call it a day.
- [16:36] I want to stress that these all represent
the same equation!
- [16:40] Each one tells you how the coefficients in
a particular basis evolve in time, and no
- [16:44] one equation carries any more information
than the others.
- [16:56] With that, I think we can wrap up this episode.
- [16:59] This also wraps up the fundamentals that I
wanted to cover in this series.
- [17:03] There’s still a ton of aspects of quantum
math that I hope to cover in future episodes.
- [17:08] For example, I plan to release an episode
on the quantum path integral as well as an
- [17:13] explanation of Bell’s theorem and Bell inequalities,
whose experimental verification was the subject
- [17:19] of the 2022 Nobel Prize in physics.
- [17:22] These videos would be released at an unspecified
date, alongside other video ideas I had for
- [17:27] the channel.
- [17:29] Until then, thank you again for watching through
this series!
- [17:32] I hope you’ve enjoyed learning about quantum
mechanics as much as I’ve enjoyed making
- [17:35] videos on it.
- [17:37] See you all in the next video!