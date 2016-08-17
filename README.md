POLYGLOTS
=============
> Experiments in creating polyglot signals

Generate and transmit RTTY, PSK polyglot messages over audio using GnuRadio.<br />
For further details refer to our [paper](https://www.usenix.org/system/files/conference/woot16/woot16-paper-bratus.pdf).


QUICK-START
---------------
1. [Install](http://gnuradio.org/redmine/projects/gnuradio/wiki/InstallingGR) [GnuRadio](http://gnuradio.org/)
2. Setup and run polylgot
```sh
$ git clone https://github.com/debanjum/polyglots.git  # Cloning Repository
$ cd polyglots
$ make           # Compile the baudotmessage.c script
$ make run       # Generate PSK31, RTTY message files and run Polyglot script
```
3. Install [fldigi](http://www.w1hkj.com/) or an equivalent digital modes software
4. Decode polyglot:<br />
   - To decode the PSK-31 transmissions. In the Menu Select: Op_Mode > PSK > BPSK-31
   - To decode the RTTY-45 transmissions. In the Menu Select: Op_Mode > RTTY > RTTY-45
6. Use the fldigi signal browser to locate the decoded message.


WARNING
---------------
1. Listening to the Signal transmission are not the most pleasant audio experience.<br />
   Use an Audio cable to connect up your devices Audio-Out to the Audio-In to avoid abusing your ears.
2. The transmission are **not error-free**! So the decoded messages in the signal browser will have errors.


PLAY
---------------
1. Open [polyglot.grc](./polyglot.grc) in GnuRadio Companion(GRC)
2. Edit the flow:
   - change parameters
   - add debug blocks to figure the working of the flow
   - add wav file sinks to analyse the generated audio signal offline
   - add QT GUI sinks to the PSK, RTTY/FSK to analyse the two signals before they're merged
3. Run:
   - Click the `compile` button in GRC and run the flow with `make polyglot` or `python polyglot.py`
   - Put the absolute path to the .bin message files and run flow directly from GRC
4. Analyse the polyglot:
   - What changes and how does it affect the waterfall, time-series and constellation displays on the transmitter(GRC) ?
   - How do these changes affect what fldigi/baudline/your-tool-of-choice decodes ?


FILES
---------------
1. [baudotmessage.c](./baudotmessage.c): Generates the baudot encoded RTTY message.<br />
   the baudotmessage is currently hardcoded, so you'll need to change it in the c file and then run `make message`
2. [varicodemessage.py](./varicodemessage.py): Generates the varicode encoded PSK message.<br />
   create a new varicode message with `python varicode -f <filename> -m <message>`
3. [polyglot.py](./polyglot.py): Creates and transmits the PSK, RTTY polyglot
4. [polyglot.grc](./polyglot.grc): GnuRadio Companion flow of the polyglot


DEBUGGING
---------------
- The script fails to run from Gnu Radio Companion(GRC).<br />
  To run the flow script from GRC convert the path to message source(.bin) files to their absolute paths


CONTRIBUTING
---------------
Fork, Edit and Submit [pull request](https://github.com/debanjum/polyglots/pulls)


BUGS
---------------
Please file bug reports at [issues](https://github.com/debanjum/polyglots/issues)
