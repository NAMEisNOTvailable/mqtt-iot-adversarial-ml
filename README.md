# MQTT IoT Adversarial ML Reproduction

Reproduction of an MQTT IoT security study on adversarial message generation and anomaly-detection evaluation.

The workflow generates MQTT-like adversarial messages from sample telemetry data, runs five classifiers, and compares accuracy and false negatives across perturbation settings.

## Start Here

- Notebook: [notebooks/mqtt_adversarial_ml_reproduction.ipynb](notebooks/mqtt_adversarial_ml_reproduction.ipynb)
- Results summary: [docs/results-summary.md](docs/results-summary.md)
- Reproduction notes: [docs/reproduction-notes.md](docs/reproduction-notes.md)

## What It Covers

- Uses sample weather telemetry data from the original code repository.
- Generates adversarial MQTT-like messages from numeric and text-like fields.
- Evaluates Logistic Regression, Random Forest, KNN, MLP and SVC.
- Compares accuracy and false negatives across changing gamma values.
- Documents dependency fixes and reproduction limits.

## Main Takeaway

In the saved run, discriminator accuracy ranged from `0.508` to `0.832`, and false negatives ranged from `15/250` to `72/250`. These numbers are specific to the software workflow and sample dataset used here.

## Files

| Path | Purpose |
| --- | --- |
| `notebooks/mqtt_adversarial_ml_reproduction.ipynb` | Notebook with outputs removed. |
| `data/weather_sample_data.csv` | Sample data from the original MIT-licensed repo. |
| `docs/results-summary.md` | Result numbers and interpretation. |
| `docs/reproduction-notes.md` | Reproduction scope, changes and limitations. |
| `scripts/check_repo.py` | Small check to catch missing files or accidental course/private markers. |

## Run Locally

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
jupyter notebook notebooks/mqtt_adversarial_ml_reproduction.ipynb
```

The notebook can take time to run because it loads transformer models and repeatedly evaluates generated message sets.

## Scope

This is a controlled reproduction for defensive security research and model-evaluation practice. It does not include a live MQTT broker, Raspberry Pi devices, WiFi Pineapple hardware, or instructions for attacking real systems.

## Attribution

The notebook adapts code and sample data from [HenryCWong/adversarialBERTMessages](https://github.com/HenryCWong/adversarialBERTMessages), which is released under the MIT License. See [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).

Original paper: Henry Wong and Tie Luo, *Man-in-the-Middle Attacks on MQTT-based IoT Using BERT Based Adversarial Message Generation*.
