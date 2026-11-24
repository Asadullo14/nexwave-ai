"""Small, beginner-friendly RF analysis helpers for the NEXWAVE AI demo."""
from __future__ import annotations

import numpy as np


def generate_iq_signal(
    sample_rate_hz: float = 2_000_000,
    duration_s: float = 0.02,
    tones_hz: tuple[float, ...] = (120_000.0, -260_000.0),
    amplitudes: tuple[float, ...] = (1.0, 0.45),
    noise_std: float = 0.12,
    seed: int = 7,
) -> tuple[np.ndarray, np.ndarray]:
    """Generate complex IQ samples containing tones plus Gaussian noise."""
    if sample_rate_hz <= 0 or duration_s <= 0:
        raise ValueError("sample_rate_hz and duration_s must be positive")
    if len(tones_hz) != len(amplitudes):
        raise ValueError("tones_hz and amplitudes must have equal lengths")

    rng = np.random.default_rng(seed)
    n_samples = int(sample_rate_hz * duration_s)
    if n_samples < 2:
        raise ValueError("duration is too short for the selected sample rate")

    t = np.arange(n_samples) / sample_rate_hz
    iq = noise_std * (
        rng.standard_normal(n_samples) + 1j * rng.standard_normal(n_samples)
    ) / np.sqrt(2)

    for tone, amplitude in zip(tones_hz, amplitudes):
        iq += amplitude * np.exp(1j * 2 * np.pi * tone * t)

    return t, iq


def calculate_psd(
    iq: np.ndarray, sample_rate_hz: float
) -> tuple[np.ndarray, np.ndarray]:
    """Return FFT-shifted frequency axis (Hz) and relative PSD (dB)."""
    iq = np.asarray(iq)
    if iq.ndim != 1 or iq.size < 2:
        raise ValueError("iq must be a one-dimensional array with at least 2 samples")
    if sample_rate_hz <= 0:
        raise ValueError("sample_rate_hz must be positive")

    window = np.hanning(iq.size)
    spectrum = np.fft.fftshift(np.fft.fft(iq * window))
    power = (np.abs(spectrum) ** 2) / max(np.sum(window ** 2), 1e-12)
    psd_db = 10 * np.log10(power + 1e-15)
    frequencies_hz = np.fft.fftshift(np.fft.fftfreq(iq.size, d=1 / sample_rate_hz))
    return frequencies_hz, psd_db


def make_synthetic_observations(n_normal: int = 250, n_anomaly: int = 18, seed: int = 21):
    """Create illustrative spectrum-feature rows for anomaly-detection practice."""
    import pandas as pd

    rng = np.random.default_rng(seed)
    normal = pd.DataFrame({
        "center_frequency_mhz": rng.normal(900, 1.8, n_normal),
        "bandwidth_khz": np.clip(rng.normal(180, 25, n_normal), 60, None),
        "signal_power_dbm": rng.normal(-68, 4, n_normal),
        "noise_floor_dbm": rng.normal(-96, 2, n_normal),
        "spectral_occupancy_pct": np.clip(rng.normal(32, 7, n_normal), 0, 100),
        "signal_duration_ms": np.clip(rng.normal(110, 25, n_normal), 5, None),
    })
    unusual = pd.DataFrame({
        "center_frequency_mhz": rng.choice([875, 925, 960, 840], n_anomaly) + rng.normal(0, 0.3, n_anomaly),
        "bandwidth_khz": rng.normal(520, 90, n_anomaly),
        "signal_power_dbm": rng.normal(-43, 5, n_anomaly),
        "noise_floor_dbm": rng.normal(-91, 3, n_anomaly),
        "spectral_occupancy_pct": np.clip(rng.normal(78, 8, n_anomaly), 0, 100),
        "signal_duration_ms": rng.normal(420, 70, n_anomaly),
    })
    data = pd.concat([normal, unusual], ignore_index=True)
    data["demo_ground_truth"] = [0] * n_normal + [1] * n_anomaly
    return data.sample(frac=1, random_state=seed).reset_index(drop=True)
