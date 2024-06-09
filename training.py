#!/usr/bin/env python3

import mne
from mne.io import read_raw_fif
from mne.datasets import sample
from mne import Epochs, pick_types, create_info
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
from mne.time_frequency import psd_array_welch
import numpy as np


data_path = sample.data_path() # neuroimaging data
raw_file = data_path / 'MEG/sample/sample_audvis_raw.fif'
raw = mne.io.read_raw_fif(str(raw_file), preload=True)

raw.filter(l_freq=8., h_freq=40.)
events = mne.find_events(raw, stim_channel='STI 014')
unique_event_ids = np.unique(events[:, 2])
print(unique_event_ids)
event_id = {'auditory/left': 1, 'auditory/right': 2}
epochs = mne.Epochs(raw, events, event_id, tmin=-0.2, tmax=0.5, preload=True)
picks = pick_types(epochs.info, meg=False, eeg=True, eog=False)
psds, freqs = psd_array_welch(epochs.get_data(), sfreq=raw.info['sfreq'], fmin=1., fmax=40., n_fft=256)
psd_mean = psds.mean(axis=-1)