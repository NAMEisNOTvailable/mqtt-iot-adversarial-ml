# MQTT IoT Adversarial ML Reproduction

Software-only reproduction of an MQTT IoT security study that uses BERT/GAN-inspired adversarial message generation to test anomaly-detection models.

This repo packages a university reproduction study into a cleaner portfolio artifact: a runnable notebook, sample data, result notes, limitations, and attribution to the original MIT-licensed research code.

## Quick Review Path

1. Read the scope and result summary: [docs/results-summary.md](docs/results-summary.md)
2. Check reproduction decisions and limitations: [docs/reproduction-notes.md](docs/reproduction-notes.md)
3. Open the cleaned notebook: [notebooks/mqtt_adversarial_ml_reproduction.ipynb](notebooks/mqtt_adversarial_ml_reproduction.ipynb)

## What This Demonstrates

- Reproduced a software-only MQTT adversarial-message workflow from a published IoT security study.
- Generated MQTT-like adversarial telemetry messages from a sample weather dataset.
- Benchmarked Logistic Regression, Random Forest, KNN, MLP and SVC anomaly-detection classifiers.
- Compared accuracy and false-negative behaviour across changing perturbation settings.
- Documented reproduction gaps, dependency fixes and deployment limitations instead of overstating the result.

## Repository Contents

| Path | Purpose |
| --- | --- |
| `notebooks/mqtt_adversarial_ml_reproduction.ipynb` | Cleaned public notebook for the reproduction workflow. |
| `data/weather_sample_data.csv` | Sample telemetry dataset from the original MIT-licensed code repository. |
| `docs/results-summary.md` | Main findings, supported metrics and interpretation. |
| `docs/reproduction-notes.md` | Attribution, reproduction scope and known deviations from the original setup. |
| `scripts/check_repo.py` | Lightweight repository hygiene check for the public artifact. |

## Run Locally

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
jupyter notebook notebooks/mqtt_adversarial_ml_reproduction.ipynb
```

The notebook can take time to run because it loads transformer models and repeatedly evaluates generated message sets.

## Scope

This is a controlled reproduction and analysis artifact. It does not include a live MQTT broker, Raspberry Pi devices, WiFi Pineapple hardware, or instructions for attacking real systems. The work is intended for defensive security research, model-evaluation practice and portfolio review.

## Attribution

The notebook adapts code and sample data from [HenryCWong/adversarialBERTMessages](https://github.com/HenryCWong/adversarialBERTMessages), released under the MIT License. See [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).

Original paper: Henry Wong and Tie Luo, *Man-in-the-Middle Attacks on MQTT-based IoT Using BERT Based Adversarial Message Generation*.
