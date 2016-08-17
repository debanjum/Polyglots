#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Polyglot
# Author: Debanjum S. Solanky
# Description: RTTY45, PSK31 Polyglot Signal Transmitter
# Generated: Tue Aug 16 21:11:28 2016
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
        self.samp_rate = samp_rate = 32000
        self.psk_samp_rate = psk_samp_rate = 31.25
        self.fsk_scale = fsk_scale = 1.2
        self.freq = freq = 1000
        self.bw = bw = 75

        ##################################################
        # Blocks
        ##################################################
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=int(samp_rate/(sps*psk_samp_rate)),
                decimation=1,
                taps=None,
                fractional_bw=None,
        )
        self.qtgui_sink_x_0 = qtgui.sink_f(
        	1024, #fftsize
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"QT GUI Plot", #name
        	True, #plotfreq
        	True, #plotwaterfall
        	True, #plottime
        	True, #plotconst
        )
        self.qtgui_sink_x_0.set_update_time(1.0/10)
        self._qtgui_sink_x_0_win = sip.wrapinstance(self.qtgui_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_sink_x_0_win)
        
        
        self.digital_psk_mod_0 = digital.psk.psk_mod(
          constellation_points=2,
          mod_code="none",
          differential=True,
          samples_per_symbol=sps,
          excess_bw=0.01,
          verbose=False,
          log=False,
          )
        self.blocks_not_xx_0 = blocks.not_ii()
        self.blocks_multiply_xx_1_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_1 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vff(1)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vcc((0.9, ))
        self.blocks_int_to_float_0_0 = blocks.int_to_float(1, fsk_scale)
        self.blocks_int_to_float_0 = blocks.int_to_float(1, fsk_scale)
        self.blocks_file_source_0_0_0 = blocks.file_source(gr.sizeof_int*1, "baudotmessage.bin", True)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_char*1, "varicodemessage.bin", True)
        self.blocks_complex_to_float_0 = blocks.complex_to_float(1)
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.band_pass_filter_0_1 = filter.interp_fir_filter_fff(1, firdes.band_pass(
        	1, samp_rate, 500, 1500, 10, firdes.WIN_HAMMING, 6.76))
        self.audio_sink_0 = audio.sink(samp_rate, "", True)
        self.analog_sig_source_x_1 = analog.sig_source_f(samp_rate, analog.GR_SIN_WAVE, freq+bw, 1, 0)
        self.analog_sig_source_x_0 = analog.sig_source_f(samp_rate, analog.GR_SIN_WAVE, freq-bw, 1, 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_int_to_float_0_0, 0), (self.blocks_multiply_xx_0_0, 1))
        self.connect((self.blocks_multiply_xx_1_0, 0), (self.blocks_multiply_xx_0_0, 0))
        self.connect((self.blocks_file_source_0_0_0, 0), (self.blocks_not_xx_0, 0))
        self.connect((self.blocks_multiply_xx_1, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_int_to_float_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.blocks_file_source_0_0_0, 0), (self.blocks_int_to_float_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.band_pass_filter_0_1, 0))
        self.connect((self.band_pass_filter_0_1, 0), (self.qtgui_sink_x_0, 0))
        self.connect((self.band_pass_filter_0_1, 0), (self.audio_sink_0, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_1_0, 0))
        self.connect((self.blocks_not_xx_0, 0), (self.blocks_int_to_float_0_0, 0))
        self.connect((self.digital_psk_mod_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.blocks_complex_to_float_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.blocks_complex_to_float_0, 0), (self.blocks_multiply_xx_1, 1))
        self.connect((self.blocks_complex_to_float_0, 0), (self.blocks_multiply_xx_1_0, 1))
        self.connect((self.blocks_file_source_0, 0), (self.digital_psk_mod_0, 0))
        self.connect((self.analog_sig_source_x_1, 0), (self.blocks_multiply_xx_1, 0))


# QT sink close method reimplementation
    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "polyglot")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.band_pass_filter_0_1.set_taps(firdes.band_pass(1, self.samp_rate, 500, 1500, 10, firdes.WIN_HAMMING, 6.76))
        self.qtgui_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_1.set_sampling_freq(self.samp_rate)

    def get_psk_samp_rate(self):
        return self.psk_samp_rate

    def set_psk_samp_rate(self, psk_samp_rate):
        self.psk_samp_rate = psk_samp_rate

    def get_fsk_scale(self):
        return self.fsk_scale

    def set_fsk_scale(self, fsk_scale):
        self.fsk_scale = fsk_scale
        self.blocks_int_to_float_0_0.set_scale(self.fsk_scale)
        self.blocks_int_to_float_0.set_scale(self.fsk_scale)

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self.analog_sig_source_x_0.set_frequency(self.freq-self.bw)
        self.analog_sig_source_x_1.set_frequency(self.freq+self.bw)

    def get_bw(self):
        return self.bw

    def set_bw(self, bw):
        self.bw = bw
        self.analog_sig_source_x_0.set_frequency(self.freq-self.bw)
        self.analog_sig_source_x_1.set_frequency(self.freq+self.bw)

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

