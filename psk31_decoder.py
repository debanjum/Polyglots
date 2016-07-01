# Code from [1] integrated with this project's varicode decoder
# [1]: https://sdradventure.wordpress.com/2011/10/15/gnuradio-psk31-decoder-part-1/#comment-23

# Importing Modules
import re
import sys
import numpy as np
from varicode import varicode
from scikits.audiolab import Sndfile
from scipy.signal import butter, lfilter


# Butterworth Low Pass Filter
def butter_lowpass_filter(data, cutoff, fs, order):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return lfilter(b, a, data)

# Initialise Variables
SOURCE = sys.argv[1] if len(sys.argv) > 1 else 'psk31.wav'
SYMBOL_RATE = 31.25
varicode = varicode()

f = Sndfile(SOURCE)
samples_per_symbol = int(round(f.samplerate / SYMBOL_RATE))
half = samples_per_symbol // 2

sig = f.read_frames(f.nframes)
delay = f.samplerate / SYMBOL_RATE
delayed = np.hstack((np.zeros(delay, dtype='float64'), sig))
transitions = delayed[:len(sig)]*sig

filtered = butter_lowpass_filter(transitions, cutoff=600, fs=f.samplerate, order=3)
digital = np.where(filtered > 0, 1, 0)

# Sample the stream at half intervals, using the transition points as anchors
bit_stream = []
indices, = np.diff(digital).nonzero()

for i in range(len(indices)-1):
    if indices[i+1] - indices[i] >= half:
        for index in range(indices[i]+half, indices[i+1], samples_per_symbol):
            bit_stream.append('%d' % digital[index])

bit_stream = ''.join(bit_stream)
char_list = re.split('00+', bit_stream)

# Decode the characters
output = [varicode.varichar[char] for char in char_list if char in varicode.varichar]
print 'Message:', ''.join(output)
