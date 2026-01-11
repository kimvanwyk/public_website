---
date: "2026-01-11"
tags: ["python"]
title: "Relaying fun in parallel"
---

[This post](https://fosstodon.org/@leoncowle@hachyderm.io/115867547711990878) from Leon Cowle reminded me of one of the weirder and technically pleasing projects of my career. Many details here will be incorrect, not because of an NDA but because my memory is bad.

We had several thousand decoders we could sell to a customer if we changed their config, which required flashing new software. To do that, a signal is sent to the decoder on its RS232 port in the first few seconds of booting to stop the boot sequence and then a series of commands is issued via RS232. I had already previously developed a battle hardened script to do the config change with [TeraTerm](https://teratermproject.github.io/index-en.html), a scriptable terminal program. Doing it one by one would however take weeks and we needed everything done in a single week.

Simon Hoffe, one of the best engineers I have ever had the pleasure of working with and learning from, found and ordered a 16-way RS232 output PCI card (a lot harder before ubiquitous online shopping) and got it to us in time. He then went to a local electronics retailer and bought 16 240V capable relays, various wiring components and 16 cheap lunchboxes (literally, like you'd store last night's leftovers in). We soon had 16 units that could switch on a 240V output when they receive a 12V signal. We also had plenty of these [Agilent 34970 relay devices](https://www.keysight.com/zz/en/support/34970A/34970a-data-acquisition-control-mainframe-modules.html) and the means to instruct them via [VISA](https://en.wikipedia.org/wiki/Virtual_instrument_software_architecture) [GPIB](https://en.wikipedia.org/wiki/GPIB) instructions from a suitably equipped PC.

This cleared me to write a piece of software I'm still both proud of and a little terrified by. For each batch of 16 decoders, we would:
* Connect all decoders to one of COM1 through COM16 from a PC
* Connect the power of each decoder to the lunchbox associated with the COM port, with each lunchbox connected to a relay from the 34970 relay device, connected to the same PC
* Tell the software that the connections are made for the COM port
* Let the software power on the decoder, catch the boot up sequence and flash the decoder
* Indicate to the technician that the decoder has passed or failed the upgrade and can be swapped out

I wanted to use TeraTerm to communicate with each decoder since I had a script already, rather than rewrite it with a threaded [pySerial](https://www.pyserial.com/docs) app. I ended up with a GUI tool which put 16 coloured labels and 16 buttons in a grid and which created 16 TeraTerm scripts on startup, each referencing a different COM port. When any button was pressed:

* [PyVISA](https://pyvisa.readthedocs.io/) commands were issued to the relay card to power up the associated decoder
* A TeraTerm instance was started in a thread with the script for the COM port
* The TeraTerm script was configured to write a file when it exits, either *COMXX_pass.txt* or *COMXX_fail.txt*
* The app monitored for the appearance of these files and updated the correct label
* Rinse, lather and repeat

If I wrote this now it would be in pure Python with threads and asynchronous smarts, but 10ish years ago this got the job done in time and we got all the decoders processed and sold. It serves as a very handy reminder in my career that getting the job done now in a hacky way is often way more important than getting it done later with a reusable pinnacle of software engineering excellence.

