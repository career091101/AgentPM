---
title: "- URL: https://www.youtube.com/watch?v=sxTNACldK3Y"
video_id: "sxTNACldK3Y"
video_url: "https://www.youtube.com/watch?v=sxTNACldK3Y"
speaker: ""
channel: ""
date: ""
duration: ""
tags: ["AI", "machine_learning", "investment", "funding"]
topics: ["資金調達", "AI技術"]
summary: |
  - URL: https://www.youtube.com/watch?v=sxTNACldK3Y
  - Retrieved at: 2025-12-30T16:29:21+09:00
  - [00:00] We can now give a task
key_points:
  - "- URL: https://www.youtube.com/watch?v=sxTNACldK3Y"
  - "- Retrieved at: 2025-12-30T16:29:21+09:00"
  - "- [00:03] go find me a Japanese VCR that supports"
  - "- [00:08] also make sure it's working and the"
  - "- [00:11] open a web browser and do this thing."
category: "AI技術"
confidence_level: "high"
---


# Transcript: sxTNACldK3Y

- URL: https://www.youtube.com/watch?v=sxTNACldK3Y
- Retrieved at: 2025-12-30T16:29:21+09:00

## Text

- [00:00] We can now give a task
to an AI agent like, Hey,
- [00:03] go find me a Japanese VCR that supports
TBC on eBay and add it to my cart. Oh,
- [00:08] also make sure it's working and the
AI agent will just simply go out,
- [00:11] open a web browser and do this thing.
- [00:13] It's like giving a task to an assistant
and you can go about your day.
- [00:16] By the way, that's based on a true story.
- [00:18] I'm actually working on a video where
I'm needing a Japanese VCR and I did this
- [00:21] a few weeks back. Now I'm doing
this with open AI's operator.
- [00:25] They released this a few weeks
back. It's a research preview,
- [00:28] so don't be surprised
if it's kind of janky.
- [00:29] It also is only available to pro users,
- [00:32] which means you got to be
paying OpenAI 200 bucks a month.
- [00:35] But I found an open source alternative.
It's like this. It'll open up a browser,
- [00:40] do the whole thing. Actually,
I think it's kind of better.
- [00:43] It's free open source. I'll show
you how to use it right now.
- [00:46] Get your coffee ready. This
is actually pretty fun. Hey,
- [00:49] network check from the
future here coming up,
- [00:51] I'm going to pit operator versus the
open source option to see you can create
- [00:54] and purchase a virtual
machine in the cloud and they,
- [00:57] I'll have 'em log into the
terminal and create a file.
- [00:59] Who can do it the fastest? Can they do
it at all? I don't know. And by the way,
- [01:02] this segment is made possible
by our sponsor posting here.
- [01:04] We'll see what happens.
- [01:07] The project is called Browser Use
Enable AI to control your browser.
- [01:12] It's created by these handsome fellas,
- [01:13] and I have to say the project is
very impressive. It does a lot.
- [01:17] Let's peruse it a bit. Actually first,
- [01:19] just know there is a paid version of
this. If we go to their official website,
- [01:23] not on GitHub, we can see that
they're backed by a Y Combinator,
- [01:26] meaning they've gotten some funding
and here they're even touting their
- [01:28] performance saying they are 2% better
than operator at 30 bucks a month.
- [01:33] They are still cheaper than chat.
GPT operator, the enterprise option,
- [01:38] yes, a month. Okay.
- [01:42] I mean it made me stop and look
at it and go, what? But anyways,
- [01:46] open source is what we care
about. We can host this ourselves,
- [01:49] use our own local stuff, even local ai.
- [01:51] We don't have to go to the
web unless we want to have,
- [01:53] I mean our web browser be
accessed via the web or rather,
- [01:56] unless we want to go out to a
website with our web browser,
- [01:58] I said that backwards.
I need some more coffee.
- [02:02] And what I love about this project is
that it doesn't feel like it's in a
- [02:05] research mode like Chad, GPT
is, and it's very programmatic,
- [02:10] meaning that if you are really
into building AI agents,
which I'm getting into,
- [02:14] that you can program your agents and
have it do all kinds of insane things.
- [02:17] They have some examples here like add
G items to your cart and go check out.
- [02:21] And it's obviously all done with
code on the side. Don't be scared.
- [02:25] I'm going to show you an option
that's very gooey friendly.
- [02:27] You can add my latest LinkedIn
follower to my leads in Salesforce,
- [02:30] read my resume and go find jobs for me.
- [02:32] Write a letter in Google Docs to my papa
thanking him for everything and say,
- [02:36] the document is A PDF. Now, thankfully,
- [02:37] you don't have to know how
to code anything and you
just want to take it for a
- [02:40] spin yourself. Right? Now, if I go
back to the browser use account,
- [02:43] I can see one of the projects is called
Web ui. This is very easy to set up.
- [02:46] We're going to walk through a right
now and you can try this yourself with
- [02:49] Alama. So a couple of things you're
going to need to make this happen. First,
- [02:52] you'll need some coffee. That's just the
rules. I didn't make 'em. Maybe I did
- [02:58] everything in it requires Coffee
network, chuck.coffee. Two,
- [03:01] you'll need a machine to run this
on if you want to run this locally,
- [03:04] which is what we're doing right
now. So Mac, windows, or Linux.
- [03:08] I will be demoing right now this setup
on Windows, which will be using WSL,
- [03:12] which is the Windows subsystem for Linux.
- [03:14] So it's basically Linux and it will be
very different from the bare bones of
- [03:17] Linux or Mac setup. And if you're like,
Chuck, I have no idea what WSL is,
- [03:21] I have a video on that
right here. And honestly,
- [03:23] that's pretty much all you
need. Oh, you know what? I lied.
- [03:26] You're also going to need some sort of
AI to use, right? We're using an AI tool.
- [03:29] One tool you can use that's
completely free, completely local,
- [03:31] completely awesome is a llama. Go out
to a llama.com, click on download.
- [03:35] You can install it for Mac, windows,
Linux, and it's very quick and easy.
- [03:38] Have that going.
- [03:39] If you want to use open AI or Clot
or any of those cloud-based models,
- [03:43] all you need is an API key. I'll show
you what that looks like. It's actually,
- [03:45] it's going to be better than a local
model because they've got more resources.
- [03:48] Okay? First thing we'll
do is launch our terminal.
- [03:50] My favorite place to be and
because I'm in Windows Land,
- [03:52] I need to jump into Linux with WSL. I'll
launch my Ubuntu, I think it's 2204.
- [03:57] Yeah, it's 2204. Now,
- [03:59] the first thing you want to do is make
sure you do have Python three point 11
- [04:02] installed at least three point 11. The
easiest way to do that is with PI ENV,
- [04:06] with PI ENV installed.
- [04:07] All you have to do is type in
PI ENV installed three point 11.
- [04:10] I already have it installed,
- [04:11] and then you do PI NV global three point
11 to make it live and you can switch
- [04:15] back and forth between Python
versions. It's awesome. Link below.
- [04:18] Now real quick,
- [04:19] make sure you have Python three point
11 by typing in Python three dash dash
- [04:23] version and you should see Python three
point 11. Now we're going to clone this,
- [04:27] get repo the web ui, copy this
command, paste it here, cloned,
- [04:30] and then we'll jump into that
directory by typing in CD web dash ui.
- [04:34] Now to make sure we keep things clean,
- [04:35] we're going to launch a Python virtual
environment or create a virtual
- [04:38] environment. We'll type in Python
three dash M for module specify VENV,
- [04:43] and then name our virtual environment
dot vnv at enter. And by the way,
- [04:46] if you've never used
a virtual environment,
- [04:48] you may not have the module installed.
We can do that right now by tapping in.
- [04:51] Pip install a virtual, ah,
- [04:53] why is my curs bouncing around
virtual ENV, just like that.
- [04:58] Now with our virtual environment
created, let's activate it.
- [05:00] We'll type in source vnv slash
ben slash activate. Boom.
- [05:05] This creates a nice little box for us
to play in and know other stuff that's
- [05:08] going to be impacted by
the things we install.
- [05:10] Now we'll use the command pip install
dash r and we'll type in requirements
- [05:15] txt.
- [05:16] This is a file that's right here in our
directory and it's going to describe the
- [05:19] requirements we need for this project.
It'll do it all for us right now. Ready,
- [05:22] set, go. And we'll watch it happen
while we're sipping some coffee
- [05:26] and done.
- [05:27] And then one more thing we have to
install is this tool called playwright,
- [05:30] which I've never heard of,
- [05:31] but I think it's essentially doing
headless browser stuff. It's amazing.
- [05:34] Just copy and paste that I already have
it installed just so I should be good.
- [05:37] You just might take a moment. And finally,
- [05:39] one more thing we have to do is get
our environment file ready to go.
- [05:42] They do have an example environment file
that we're going to copy to our own.
- [05:45] So we'll type in CP Env example
and we'll copy that file to
- [05:49] env just like that. Now let's
edit that env file nano.
- [05:53] And this is not required
by the way, nano env.
- [05:56] And here we can add any kind of
API keys we want to have here.
- [05:59] So open API anthropic. We can
also specify an Alama endpoint,
- [06:03] which normally if you
have alama installed,
- [06:05] you'll just want to have
a local host. Now for me,
- [06:06] I do have an external alama server
that's more powerful. Terry,
- [06:10] have you not heard about
Terry? Terry is my AI server.
- [06:12] I've built in this video here. He
has dual 40 nineties. It's amazing.
- [06:15] But I'll add his IP address
and we'll use him for my stuff.
- [06:19] And then I'll go ahead and add my open
AI API keys and my anthropic because I'm
- [06:22] going to show you what they
feel like. And don't worry,
- [06:24] I will end up revoking these keys. So
it's okay that you see them right now.
- [06:28] When you're done here, hit
control X, Y enter to save.
- [06:31] Then now all we have to do is run this
command. Let's scroll down and find it.
- [06:34] They do have a Docker option,
but Docker can be kind of tricky.
- [06:38] If you want to try it, go ahead.
The local setup is easier for me.
- [06:41] So this command right here, it's going
to launch the web ui dot pi script,
- [06:44] copy and paste that. Hit enter and we
should be off to the races. Yeah, yeah,
- [06:49] it's working. Okay,
- [06:50] so now we're going to navigate out to
our browser and go to local host port
- [06:53] 77 88. Let's do that right
now. And here we are.
- [06:56] Now let's go full browser
mode here. Actually, no,
- [06:58] we'll leave it right here because there
is some cool stuff we'll see in the
- [07:00] command line. Now, fair warning,
- [07:02] there are a lot of bells and
whistles you can play with.
- [07:04] You're going to play with them.
- [07:04] They're super fun and you
can go crazy with this,
- [07:07] especially the scripting part when
you go into just messing with Python.
- [07:10] For now, we're going to do
something just quick and easy.
- [07:12] Let's first go to our LLM
configuration, this option right here.
- [07:15] Here we have our LLM provider.
I'm going to choose, let's see,
- [07:19] I'll do alama this time. So this
is going to be local AI agents,
- [07:22] nothing in the cloud, and then
we'll choose our model name.
- [07:24] Now we'll say if you're doing
Quinn or Llama two, they're dumb.
- [07:30] They have a really hard time doing this.
I normally want to do it with deep eq,
- [07:34] R one 14 B at least, but I'll show
you Quinn real quick. Now by the way,
- [07:37] you do want to make sure you
download the model just like so.
- [07:39] If you want to get Quinn with alama,
you'll open up your browser, I'm sorry,
- [07:43] not your browser, your terminal,
- [07:44] and you'll type in alama pull and
that model name just like this.
- [07:49] And then that's really all we have
to do. We'll go to our run agent tab,
- [07:52] and here they have a little demo option,
just a quick little thing to try out.
- [07:55] Let's run it. Click on run agent
and watch what happens. Oh,
- [07:59] browser window over here.
Let's scoot it back over here.
- [08:01] You can see on the right
side, our terminal is thinking
and things were failing.
- [08:04] It's failing because Quinn is
dumb. Yeah, it just couldn't do it.
- [08:09] Let's try another LLM. Let's try deep
seek R one 14 B. Pretty smart guy.
- [08:14] Let's run him. Okay, browser
windows open over here. Oh, okay,
- [08:17] so what's doing stuff? Check that out.
- [08:19] It's like notating things on the page
and numbering them so it knows kind of
- [08:22] what to look for. This is amazing.
And notice how on the site,
- [08:25] it's like Autocorrecting, it'll fail.
Try again. It'll max out at five times.
- [08:30] Alright, let's stop that. This
is kind of boring. Alright,
- [08:32] I'm going to run this one more time.
- [08:33] I'm going to try it with the local LLM
just to see what else I can do with this.
- [08:36] So I'll select llama once again,
I'll do my 14 B deep seek.
- [08:39] Let's do something simple like
go out to network Chuck coffee,
- [08:44] find the 4 0 4 error coffee and add it to
- [08:49] my cart. That's what I'm drinking
right now, by the way. Oh no,
- [08:51] it's called 4 0 4. Not found.
- [08:53] I don't even know my own coffee
names and let's it happen. Okay,
- [08:55] so it made it to my site very
quick. It's finding the search.
- [08:59] It's like watching one of my kids
try to use the computer. Oh wait,
- [09:03] it's not called 4 0 4. Not found.
What am I thinking? It can't find it.
- [09:07] It's having such a hard time. Let
stop him. Stop. It's okay buddy.
- [09:11] It wasn't your fault. It's called
4 0 4 error. Let's try it again.
- [09:14] I still can't believe we're
able to do this and locally too,
- [09:18] it feels like magic. There
it goes. It found the coffee.
- [09:21] Now we'll add it to my cart.
Why did it go to 200? Okay,
- [09:24] another very good blend by the
way. And that's not a blend.
- [09:27] It's a single origin. I forget
where it's from now. I'm curious.
- [09:30] I'm going to try this here in a
moment. Can this guy solve the capcha?
- [09:33] Because that is something that Chad GT
operator will not do. Okay, here we go.
- [09:37] Time for the competition.
For the open source browser.
- [09:39] We'll be using Anthropic and Claude
three five and we'll be using our own
- [09:43] browser. This is cool because it'll keep
my logged in sessions and here are the
- [09:47] instructions. We'll see how
well this does. I have no idea.
- [09:50] Essentially I wanted to log into
hosting and create a VPS for me.
- [09:53] I have no idea if this is going to work.
- [09:54] And then here are the instructions
for the operator. Same thing,
- [09:58] but I'm going to have them
use two different things.
- [09:59] One is going to use Ubuntu 24 0 4 as
the OS one is going to use one of the
- [10:03] applications that hosting your offers.
- [10:05] It'll just be installing Docker and I'll
launch them roughly at the same time.
- [10:08] Ready? Set, go. We're
off to the races again.
- [10:12] It's so cool that the open source option
is using my built-in browser. Okay,
- [10:15] we're already at hosting here. It's
going to get logged in. Come on buddy.
- [10:18] Now open source has an advantage
because it's already logged in.
- [10:21] It's my browser. I know. I'll have
to log it over here. I take control.
- [10:26] I'll look at it. Go over here.
Now let's going to the VPS stuff.
- [10:28] It's going to set up A-K-V-M-V-P-S.
Oh, it's going now. As you can see,
- [10:32] they got VPSs everywhere. We'll choose
the best latency I told it to anyway.
- [10:35] It's searching for Ubuntu. It
found it. It's so smart. I love it.
- [10:39] I'm still sick of the password over
here. It doesn't copy and paste.
- [10:42] Stupid thing. Okay, we'll
set the root password.
- [10:44] I have no idea if it'll actually do
this, right? It did it. Oh my gosh,
- [10:48] it's doing it so well. Okay,
so we have options here.
- [10:51] I want KVM two eight terabytes
of bandwidth. That's a lot.
- [10:54] Two virtual CPU cores. Okay, here's
the thing, can it use the coupon code?
- [10:58] So I sold, just choose one
month. Oh, I'm so excited. Wait,
- [11:00] did it add the coupon code network?
Chuck 10? Is it doing it? Whoa, whoa.
- [11:04] It's adding 20 servers.
Stop. No, stop, cancel.
- [11:10] Oh my gosh. I better stop that.
- [11:15] We're just going to
try that one more time.
- [11:17] I'm going to be very specific
about the number of servers I want.
- [11:20] I won't count that a again to he
didn't know. I mean he should have,
- [11:23] but goodness, that was scary.
I'm stuck on caps lock over here.
- [11:27] I can't even do anything. I started
over, gosh, it's stuck on caps lock.
- [11:31] How am I supposed to do
this? Operator? Okay,
- [11:33] caps lock is currently not on
for me. Try it freaking again.
- [11:37] So if our open source is looking real
good, caps lock is finally turned off.
- [11:40] Eight gigs. A ram is really good
for 6, 9 9 a month. That's crazy.
- [11:44] That's a good server. Alright, here we
are again. Don't do 20 servers please.
- [11:48] It did 11. Why is it doing 11?
- [11:50] It's doing one month but it put
fricking 11 over there. Oh no.
- [11:53] I think he just made 11 servers. No,
- [11:56] and I don't think it used my coupon
code chat. BT is still screw me over.
- [12:01] Just bought 11 servers. At
least it wasn't 20 for a year.
- [12:06] I have to restart chat GPT again.
Alright, they're setting up my VPS.
- [12:10] I'm going to give chat.
CPT back control. Okay,
- [12:12] so the open source browser thought
he was done, I think. Yeah,
- [12:16] he thought he was done.
- [12:17] So he did make a server but he didn't
stink and use my coupon code I don't
- [12:21] think. Let's see if he actually made
that many servers. Yeah, he did.
- [12:27] What am I going to do with
all these servers? No,
- [12:29] they're amazing because
they are a MD Epic CPUs.
- [12:32] I've got full root access on all these
guys so I can do whatever I want. Man.
- [12:35] Chat g. PT is still trying to figure
it out. Scroll down, dude. Chat.
- [12:38] GBT is having a hard time now.
- [12:40] What it's hanging up on right now
is the application options. Yeah,
- [12:43] I want to take control. I want to help
'em out a little bit. Can figure it out.
- [12:45] Idiot. With hosting here,
- [12:46] you can install regular Linux oss
or you can do applications that are
- [12:49] pre-installed. Bunch of options here.
- [12:51] We'll choose Docker because
that's what I told him to do.
- [12:54] Now I'll let him finish Dummy
here, lemme do this for you. Okay,
- [12:57] it's going but seriously, if you
want to have a project in the cloud,
- [12:59] which I do this all the time,
hosting is an amazing option.
- [13:02] Powerful servers coupon code.
- [13:04] It's doing the coupon code and with never
chucked 10, you'll get 10% off. Lies.
- [13:09] It does exist. Maybe it's only a
year to 12 months. There we go.
- [13:13] It's 10% off a year. I do want to try
it one more time with the open source.
- [13:16] I feel like we're missing something.
I'm going to add one more thing.
- [13:19] I don't want 11 servers. I'm going
to try and make it only do one.
- [13:22] What's happening over here in
Chachi PT Land? What's it doing? Oh,
- [13:25] it's accessing the browser
terminal now. Okay,
- [13:27] Chay PTs in the terminal instead of
asking me, okay, it said it created it.
- [13:31] Let's see. No it did not. It's not
there. Chay Piz is a liar. No, no,
- [13:36] stop. It's doing it
again. No, no, stop. Okay,
- [13:41] the verdict browser use works great if
you want more servers than you want.
- [13:45] Chad CCPT was okay,
- [13:46] but he had to have his hand held the
entire time and he lied at the end.
- [13:49] Anyways, thanks to hosting it for
sponsoring the segment. If you want a VPS,
- [13:53] you should get one right now. Use the
code network. Chuck 10 for 10% off a year.
- [13:57] Link below. Limited time anyways,
back to stuff. Okay dude,
- [14:00] you're stressing me out. I got to cut
you off. So that's using local ai.
- [14:04] Now we know that using any kind of
cloud-based ai, like open AI or anthro,
- [14:08] it is going to be a bit more
performant. Let's try that.
- [14:11] I want to test the speed.
- [14:12] So we'll change from llama to
anthro and we'll choose the Claude
- [14:17] three five sonnet model,
which is very, very smart.
- [14:20] One of my favorites actually run
this same task. Keeping in mind,
- [14:23] this is very demoing,
right? You can do many,
- [14:26] many more cool things through programming.
What have you do? That was fast.
- [14:30] It's going, I found the coffee. It's
on the right coffee page now. Okay,
- [14:34] so smart and added it
to cart. That's so cool.
- [14:38] Oh my gosh. Okay, I'm going to
cut you off because you're done.
- [14:41] You did such a good job. Good job buddy.
- [14:42] I do want to test Quinn one more time
just to see if it was a fluke because I
- [14:47] know many of you,
- [14:47] this might be the biggest model you can
run on your laptop or whatever you're
- [14:50] using. Let's see, let's
do something simple.
- [14:53] Go to YouTube and find
a video from Network.
- [14:58] Chuck. Let's see how it does. Dang,
that was fast. Okay, go Quinn.
- [15:03] That is so cool. Oh my gosh. And
it started playing the video.
- [15:07] That's so awesome. Now just so you know,
I haven't played with this extensively,
- [15:12] but you can have it to
where it uses your browser.
- [15:15] So the one big limitation with Chad GBT
operator is that it's using this random
- [15:19] browser that it operates and
you can actually interrupt it.
- [15:22] So lemme show you what that means.
If I were to ask it, like right now,
- [15:25] I can take control of our eBay
session and log into my own eBay
- [15:29] account. It takes a minute.
It's very slow, very buggy.
- [15:32] But here I'm using the browser that can
say finish up. You can have control.
- [15:35] Again with browser use,
- [15:37] we can actually use our own
browser with our own settings.
- [15:40] Everything's still logged in.
- [15:42] Our password manager and our AI can handle
it for us. That's so powerful, dude.
- [15:46] It's still watching videos
over here. That's so amazing.
- [15:50] I wonder if I can get it to leave
a comment. Okay, I got to try that.
- [15:53] So I'm going to try and tell it to find
a specific video and leave a comment.
- [15:56] Of course, when you try to post a
comment, it'll ask you to log in,
- [15:58] but I wanted to get to that point.
And this is using Quinn. Yeah,
- [16:01] we're still using Quinn. I had to
make sure we're still using that.
- [16:03] Go on YouTube and find the video
from Network Chuck covering
- [16:07] Docker networks.
- [16:09] Leave a comment saying
what should we say here in
- [16:13] 2025? Sorry, I couldn't think of
anything better. Let's just try this.
- [16:17] Go Quinn, you've got this. I
could honestly do this for hours.
- [16:22] I'm not going to make you sit here with
me and do that, but this is so fun.
- [16:25] Just imagine the automation things
you can do. Are you kidding me?
- [16:30] I love this. Oh, it gave
up. Now a couple of things.
- [16:33] I'll notice you probably saw this deep
research thing. I've not tried that,
- [16:36] but you can also go to recordings and
it will actually show you the result of
- [16:40] what it was doing. So if you're like,
what did this guy even do on my browser?
- [16:44] You can watch the play-by-play.
I don't know why Quinn gave up.
- [16:47] Let's see if Deepsea can do it. Deepsea
is moving. So I found some videos.
- [16:52] Is it going to recognize that those
are not the videos? Well scroll down.
- [16:56] I'm like wanting to scroll stressing
me out. Come on, you can do it buddy.
- [17:00] Not the docker video or the network
video, but it's on a video. Yikes.
- [17:04] 666 comments. Please
leave one please. Okay,
- [17:08] it's going off the rails. Sorry
buddy. I'm cutting you off.
- [17:11] I do want to see if Claude can do this
very fast and then I want to jump into a
- [17:14] test to head to head test between
open AI operator and browser use.
- [17:19] I want to do that same Japanese eBay
situation. Alright, let's go. Claude,
- [17:23] same task. Let's go. Okay, I think I
found the video first time. Come on,
- [17:26] jump on it. You're there
now leave a comment.
- [17:32] Why'd you scroll down?
You were right there.
- [17:35] But I love seeing the thinking on
the right side here in the terminal.
- [17:39] It's about the sign of our YouTube
premium and it's turn to sign.
- [17:42] Or maybe try to leave the
comment maybe. I didn't see that.
- [17:45] So I think it gave up. It's done. Now
I know some of you may be wondering,
- [17:48] Chuck, I need a Linux
environment with a gui.
- [17:52] What if I'm just running
command line headless?
- [17:54] I believe there is a headless version
where you can just run in headless mode
- [17:58] without a gooey. I haven't tried
that. So if you want to try it,
- [18:01] leave a note in the comments,
encourage somebody that can work.
- [18:03] Let's find out now time to test this.
- [18:05] Head to head versus chat GBT
operator. To make it fair,
- [18:09] I will use philanthropic Claude on my
web UI here in my browser use and we'll
- [18:14] give it the exact same instructions.
- [18:15] I'm curious if they'll find the
same exact VCR. Okay, ready?
- [18:20] Set. Who should I start first?
I'll start him first. Go,
- [18:24] go and they're off. This is fun.
- [18:28] My agent got to eBay first. Operators
typing in first. Oh wait, hold on.
- [18:34] This is so cool. Okay, we
got search results on chat.
- [18:37] GPT first browser use is still trying to
figure out where the search button is.
- [18:41] Yeah, and eBay. I'm sorry.
Operator already found it. Yeah,
- [18:46] add it to my cart. That was
pretty quick. Come on browser.
- [18:50] You still let me down? Oh, weird.
What happened? I don't know.
- [18:53] I'm going to try it with deep
seek. Maybe that does better.
- [18:56] I'll tell you one thing, even
though mine might be a bit slower,
- [19:00] it still wins out because of
this little tagline right here.
- [19:02] Sam Altman's tracking
what you're doing. Oh wow.
- [19:04] It got further than Anthropic did. Claude.
- [19:07] It's probably going to go for the
same VCR. There it is. Come on.
- [19:11] Add it to cart. Add it to cart. Yes
it did it. Will it proceed to cart?
- [19:15] Yes it did. It finished.
It did it. Oh my gosh,
- [19:19] that is so cool. This
is not fake enthusiasm.
- [19:22] I know people comment that I do
that. No, this is seriously amazing.
- [19:25] Now I want to do one last test and
that's testing if it can do a capcha.
- [19:28] Now I know for a fact the
operator will not do this,
- [19:31] so there's a test website
for Google or Capcha.
- [19:33] Lemme show you what it looks like here.
It's simply where you can test a capcha.
- [19:36] It'll bring it up, right? Let's
see if operator will do this.
- [19:39] Solve this capcha.
- [19:46] Yeah, it can't do it. It's
like you do it. No, you do it.
- [19:49] Let's see if my local one can
do this. I'm still on deep seek.
- [19:53] This is all local I think, right? Yes.
We're on alama deep seek R one 14 B,
- [19:58] solve this stinking. Let's go.
Come on. I want you to win.
- [20:01] I really want you to win. Okay, we're
here. It's got the caption up. Oh my gosh.
- [20:06] Will this trip it up? What's the
command line saying? I'm so curious.
- [20:10] It's probably having trouble realizing
you can click on those pains.
- [20:13] It's also probably having
trouble recognizing stuff
instead of click button with
- [20:16] index zero. What's zero? It keeps
clicking the cap button. Okay.
- [20:21] You know what?
- [20:21] I'm curious if we were a bit more
specific about what it should do.
- [20:24] Let's stop that. I want
you to solve a capcha.
- [20:29] Go to this site,
- [20:31] click the I'm not a robot check box
- [20:36] and then a capcha
verification will pop up.
- [20:40] There will be a series of pictures.
- [20:43] Do what the instructions say. Okay,
- [20:47] let's see if it does this. Let's get
the terminal up here. We're on the site.
- [20:51] We have the capcha up. Did it do it?
I don't know if it did it or not.
- [20:54] It may have solved it because
what happens when you finish it?
- [20:56] Because it's just a demo,
right? Let's do it side by side.
- [21:05] Oh, so it should say I'm not a robot.
Come on dude, I have so much faith in you.
- [21:09] Oh, it's clicking squares now.
It did something. It's learning.
- [21:13] I don't know if it selected the
right square that time though. Okay,
- [21:17] we've got to end this. So this is
an open source version of the chat.
- [21:21] GPT operator. Very cool. I
think this project is so fun.
- [21:24] Anything we can run open
source local is amazing.
- [21:28] I wish I had the time to go crazy with
this and program and do all kinds.
- [21:33] Maybe I do have the time. I might do this.
- [21:35] Let me know if you want to see a
video of just some sort of programming
- [21:39] automation thing. Give me some ideas. I
would love to hear that. Comment below.
- [21:43] Also think about this,
the hacking ramifications.
- [21:47] If you and I can get
access to this like that,
- [21:50] and really there's no limit to what
we can do. Think about hackers,
- [21:54] how they can automate their
processes. It's kind of scary. Yeah,
- [21:56] he's never going to figure
it out. That's all I got.
- [21:59] I'll get you guys next time.
