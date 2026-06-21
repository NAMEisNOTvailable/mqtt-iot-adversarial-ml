# Reproduction Notes

## Original Work

This repository is a reproduction/adaptation of the MIT-licensed code repository:

- `HenryCWong/adversarialBERTMessages`
- https://github.com/HenryCWong/adversarialBERTMessages

The original paper studied MQTT-based IoT MITM scenarios and adversarial message generation using a BERT-based approach inspired by GANs.

## What Was Reproduced

- Sample telemetry data loading.
- Adversarial message generation for numeric and text-like MQTT fields.
- BERT/DistilBERT feature extraction workflow.
- Evaluation of generated messages with multiple anomaly-detection classifiers.
- Comparison of accuracy and false-negative behaviour across perturbation settings.

## Adaptations in This Public Repo

- The notebook was cleaned for public review and has its execution outputs cleared.
- The original Colab-style install cell was replaced with `requirements.txt` instructions.
- The sample dataset is bundled under `data/` with attribution.
- The WordNet alias issue identified during reproduction was fixed by defining both `wn` and `wordnet`.
- The original hardware MITM setup was not reproduced.
- Full assignment report files were not included because the public repo should present the project cleanly and avoid unnecessary personal/course metadata.

## Known Limitations

- This is a software-only reproduction, not a live network attack implementation.
- Results may vary across Python, package and model versions.
- Transformer model downloads can make first runs slow.
- The dataset is small and synthetic relative to real IoT deployments.
- The reproduction does not prove deployability in resource-constrained IoT devices.
- The experiment should be interpreted as defensive evaluation of model robustness, not operational attack guidance.

## Ethical Scope

Run this project only in a local, controlled environment. Do not use it to test, intercept or manipulate traffic on systems you do not own or have explicit permission to assess.
