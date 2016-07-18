#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Polyglot
# Author: Debanjum Singh Solanky
# Description: RTTY45, PSK31 Polyglot Signal Transmitter
# Generated: Mon Jul 18 09:18:53 2016
##################################################

from PyQt4 import Qt
from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import sip
import sys

class polyglot(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Polyglot")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Polyglot")
        try:
             self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
             pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "polyglot")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.sps = sps = 8
        self.rtty_samp_rate = rtty_samp_rate = 8000
        self.psk_samp_rate = psk_samp_rate = 31.25
        self.out_samp_rate = out_samp_rate = 8000

        ##################################################
        # Blocks
        ##################################################
        self.rational_resampler_xxx_0_0 = filter.rational_resampler_ccc(
                interpolation=out_samp_rate/rtty_samp_rate,
                decimation=1,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=int(out_samp_rate/(sps*psk_samp_rate)),
                decimation=1,
                taps=None,
                fractional_bw=None,
        )
        self.qtgui_sink_x_0 = qtgui.sink_c(
        	256, #fftsize
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	psk_samp_rate*sps, #bw
        	"RTTY45_PSK31_POLYGLOT", #name
        	True, #plotfreq
        	True, #plotwaterfall
        	True, #plottime
        	True, #plotconst
        )
        self.qtgui_sink_x_0.set_update_time(1.0/50)
        self._qtgui_sink_x_0_win = sip.wrapinstance(self.qtgui_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_sink_x_0_win)
        
        
        self.digital_psk_mod_0 = digital.psk.psk_mod(
          constellation_points=2,
          mod_code="none",
          differential=True,
          samples_per_symbol=sps,
          excess_bw=1,
          verbose=False,
          log=False,
          )
        self.blocks_wavfile_source_0 = blocks.wavfile_source("/home/linux/Scripts/GnuRadio/polyglot/.rtty45.wav", True)
        self.blocks_multiply_xx_1 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_const_vxx_0_0_0 = blocks.multiply_const_vcc((0.9, ))
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vcc((0.900, ))
        self.blocks_float_to_complex_0_0 = blocks.float_to_complex(1)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_char*1, "/home/linux/Scripts/GnuRadio/polyglot/.pskquickfox.bin", True)
        self.blocks_complex_to_float_0 = blocks.complex_to_float(1)
        self.blocks_add_const_vxx_0_0 = blocks.add_const_vcc((0.3, ))
        self.audio_sink_0 = audio.sink(out_samp_rate, "", True)
        self.analog_sig_source_x_0 = analog.sig_source_c(out_samp_rate, analog.GR_SIN_WAVE, 500, 1, 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_float_to_complex_0_0, 0), (self.blocks_add_const_vxx_0_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.qtgui_sink_x_0, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.blocks_multiply_xx_1, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.rational_resampler_xxx_0_0, 0), (self.blocks_multiply_xx_1, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.blocks_multiply_xx_1, 1))
        self.connect((self.blocks_multiply_const_vxx_0_0_0, 0), (self.rational_resampler_xxx_0_0, 0))
        self.connect((self.blocks_add_const_vxx_0_0, 0), (self.blocks_multiply_const_vxx_0_0_0, 0))
        self.connect((self.blocks_wavfile_source_0, 0), (self.blocks_float_to_complex_0_0, 0))
        self.connect((self.blocks_file_source_0, 0), (self.digital_psk_mod_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.digital_psk_mod_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_complex_to_float_0, 0), (self.audio_sink_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_complex_to_float_0, 0))


# QT sink close method reimplementation
    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "polyglot")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.qtgui_sink_x_0.set_frequency_range(0, self.psk_samp_rate*self.sps)

    def get_rtty_samp_rate(self):
        return self.rtty_samp_rate

    def set_rtty_samp_rate(self, rtty_samp_rate):
        self.rtty_samp_rate = rtty_samp_rate

    def get_psk_samp_rate(self):
        return self.psk_samp_rate

    def set_psk_samp_rate(self, psk_samp_rate):
        self.psk_samp_rate = psk_samp_rate
        self.qtgui_sink_x_0.set_frequency_range(0, self.psk_samp_rate*self.sps)

    def get_out_samp_rate(self):
        return self.out_samp_rate

    def set_out_samp_rate(self, out_samp_rate):
        self.out_samp_rate = out_samp_rate
        self.analog_sig_source_x_0.set_sampling_freq(self.out_samp_rate)

if __name__ == '__main__':
    import ctypes
    import os
    if os.name == 'posix':
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    qapp = Qt.QApplication(sys.argv)
    tb = polyglot()
    tb.start()
    tb.show()
    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()
    tb = None #to clean up Qt widgets

