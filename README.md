# NEXWAVE AI — Starter Repository

**MVP v0.1: RF Spectrum Analyzer + anomaly detection demo**

This starter project demonstrates a software-first RF workflow using synthetic data:
1. Generate a simulated RF signal (no SDR hardware required).
2. Calculate its FFT and power spectral density (PSD).
3. Extract simple spectrum features.
4. Train an Isolation Forest model to flag unusual observations.
5. Visualize results in Google Colab.

> Safety and interpretation: this demo uses synthetic signals. An anomaly score is not proof of unauthorized transmission, interference, or a legal violation. Real-world conclusions require calibrated measurements, trusted frequency-allocation data, and human review.

## Quick start — Google Colab

1. Upload `notebooks/NEXWAVE_RF_Analyzer_v0_1.ipynb` to Google Colab, or open it from your GitHub repository.
2. Run the cells from top to bottom.
3. The notebook installs the small set of required packages automatically.
4. It generates synthetic measurements and displays a spectrum chart and anomaly results.

## Run locally (optional)

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt
python -m src.run_demo
```

## Repository structure

```text
nexwave-ai-starter/
├── README.md
├── requirements.txt
├── .gitignore
├── notebooks/
│   └── NEXWAVE_RF_Analyzer_v0_1.ipynb
├── data/
│   └── sample/
│       └── README.md
├── src/
│   ├── __init__.py
│   ├── rf_analyzer.py
│   └── run_demo.py
└── tests/
    └── test_rf_analyzer.py
```

## Current scope

- Synthetic IQ signal generation
- FFT / PSD visualization
- Simple feature extraction
- Isolation Forest anomaly detection
- CSV export of generated observations

## Not included yet

- Live SDR capture
- Real frequency assignment registry integration
- Signal legality classification
- Direction finding / geolocation
- Production authentication, database, or multi-user dashboard

## Suggested next milestone

Replace synthetic IQ data with a lawful, documented sample recording or a permitted SDR capture. Preserve measurement metadata such as sample rate, center frequency, gain, antenna, timestamp, sensor ID, and calibration details.
