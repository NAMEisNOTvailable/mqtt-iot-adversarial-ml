# MQTT IoT Adversarial ML Reproduction

This is a software-only reproduction project on MQTT IoT security and adversarial machine learning.

I reproduced the software workflow from a published study: generating MQTT-like adversarial messages, running several anomaly-detection classifiers, and comparing accuracy and false negatives across perturbation settings.

## Start Here

- Notebook: [notebooks/mqtt_adversarial_ml_reproduction.ipynb](notebooks/mqtt_adversarial_ml_reproduction.ipynb)
- Results summary: [docs/results-summary.md](docs/results-summary.md)
- Reproduction notes: [docs/reproduction-notes.md](docs/reproduction-notes.md)

## What I Did

- Used the sample weather telemetry data from the original code repository.
- Generated adversarial MQTT-like messages from numeric and text-like fields.
- Benchmarked Logistic Regression, Random Forest, KNN, MLP and SVC.
- Compared accuracy and false negatives across changing gamma values.
- Documented dependency fixes and reproduction limits.

## Main Takeaway

The run showed a clear change in model behaviour as generated messages were perturbed: discriminator accuracy ranged from `0.508` to `0.832`, and false negatives ranged from `15/250` to `72/250`. The project is mainly useful as a reproduction record: it checks whether the original software workflow runs, compares how the models respond, and notes what the result does not prove.

## Files

| Path | Purpose |
| --- | --- |
| `notebooks/mqtt_adversarial_ml_reproduction.ipynb` | Notebook with outputs removed. |
| `data/weather_sample_data.csv` | Sample data from the original MIT-licensed repo. |
| `docs/results-summary.md` | Result numbers and interpretation. |
| `docs/reproduction-notes.md` | What changed from the original code and what was not reproduced. |
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

This is a controlled, software-only reproduction for defensive security research and model-evaluation practice. It does not include a live MQTT broker, Raspberry Pi devices, WiFi Pineapple hardware, or instructions for attacking real systems.

## Attribution

The notebook adapts code and sample data from [HenryCWong/adversarialBERTMessages](https://github.com/HenryCWong/adversarialBERTMessages), which is released under the MIT License. See [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).

Original paper: Henry Wong and Tie Luo, *Man-in-the-Middle Attacks on MQTT-based IoT Using BERT Based Adversarial Message Generation*.
