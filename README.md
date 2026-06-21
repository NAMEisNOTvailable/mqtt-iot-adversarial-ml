# MQTT IoT Adversarial ML Reproduction

This is a software-only reproduction project on MQTT IoT security and adversarial machine learning.

I reproduced the software side of a published study that generated MQTT-like adversarial messages and tested how several anomaly-detection models responded. I did not reproduce the original Raspberry Pi / WiFi Pineapple MITM setup. The useful part here is the evaluation workflow: generate modified messages, run classifiers, compare accuracy and false negatives, and write down where the reproduction has limits.

## Start Here

- Notebook: [notebooks/mqtt_adversarial_ml_reproduction.ipynb](notebooks/mqtt_adversarial_ml_reproduction.ipynb)
- Results summary: [docs/results-summary.md](docs/results-summary.md)
- Reproduction notes: [docs/reproduction-notes.md](docs/reproduction-notes.md)

## What I Did

- Adapted the original MIT-licensed notebook into a cleaner local reproduction.
- Used the sample weather telemetry data from the original code repository.
- Generated adversarial MQTT-like messages from numeric and text-like fields.
- Benchmarked Logistic Regression, Random Forest, KNN, MLP and SVC.
- Compared accuracy and false negatives across changing gamma values.
- Recorded the dependency issue I had to fix and the parts of the original experiment I did not reproduce.

## Main Takeaway

The saved run showed that model behaviour changed noticeably as the generated messages were perturbed. Discriminator accuracy ranged from `0.508` to `0.832`, while false negatives ranged from `15/250` to `72/250`.

I would not present this as a new attack method. It is better read as a reproduction and evaluation exercise: a small study of how adversarially generated IoT-style messages can affect anomaly-detection results, and what has to be treated carefully when reproducing that kind of paper.

## Files

| Path | Purpose |
| --- | --- |
| `notebooks/mqtt_adversarial_ml_reproduction.ipynb` | Cleaned notebook with outputs removed. |
| `data/weather_sample_data.csv` | Sample data from the original MIT-licensed repo. |
| `docs/results-summary.md` | The result numbers I would actually cite. |
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
