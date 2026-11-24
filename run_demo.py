"""Run the synthetic NEXWAVE AI RF anomaly demo locally."""
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest

from src.rf_analyzer import generate_iq_signal, calculate_psd, make_synthetic_observations


def main():
    sample_rate = 2_000_000
    _, iq = generate_iq_signal(sample_rate_hz=sample_rate)
    freq_hz, psd_db = calculate_psd(iq, sample_rate)

    plt.figure(figsize=(11, 4))
    plt.plot(freq_hz / 1e3, psd_db, linewidth=0.8)
    plt.title("NEXWAVE AI — Simulated RF Spectrum")
    plt.xlabel("Frequency offset (kHz)")
    plt.ylabel("Relative PSD (dB)")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

    data = make_synthetic_observations()
    features = data.drop(columns=["demo_ground_truth"])
    model = IsolationForest(n_estimators=200, contamination=0.07, random_state=42)
    model.fit(features)
    data["model_prediction"] = (model.predict(features) == -1).astype(int)
    data["anomaly_score"] = -model.score_samples(features)

    print(data.sort_values("anomaly_score", ascending=False).head(10).to_string(index=False))
    data.to_csv("nexwave_demo_results.csv", index=False)
    print("\\nSaved: nexwave_demo_results.csv")


if __name__ == "__main__":
    main()
