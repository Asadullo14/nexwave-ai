import numpy as np
from src.rf_analyzer import generate_iq_signal, calculate_psd


def test_signal_and_psd_shapes():
    fs = 1_000_000
    _, iq = generate_iq_signal(sample_rate_hz=fs, duration_s=0.01)
    freq, psd = calculate_psd(iq, fs)
    assert iq.ndim == 1
    assert freq.shape == psd.shape
    assert len(freq) == len(iq)
    assert np.all(np.diff(freq) > 0)
