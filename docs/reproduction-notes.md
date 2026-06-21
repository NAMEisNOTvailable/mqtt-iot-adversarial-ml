# Reproduction Notes

## Source

This repo is based on the MIT-licensed code from:

- `HenryCWong/adversarialBERTMessages`
- https://github.com/HenryCWong/adversarialBERTMessages

The paper behind that code studied MQTT-based IoT MITM scenarios and a BERT-based adversarial message generator inspired by GANs.

## Reproduced Workflow

- Sample telemetry data loading.
- Adversarial message generation for numeric and text-like MQTT fields.
- BERT/DistilBERT feature extraction workflow.
- Evaluation of generated messages with multiple anomaly-detection classifiers.
- Comparison of accuracy and false-negative behaviour across perturbation settings.

## Repo Adjustments

- Notebook outputs were removed for readability.
- The Colab install cell was replaced with `requirements.txt`.
- The sample dataset is bundled locally with attribution.
- The WordNet alias issue was fixed by defining both `wn` and `wordnet`.
- Report-level findings are summarized in [results-summary.md](results-summary.md).

## Limits

- This is a software-only reproduction, not a live network attack implementation.
- Results may vary across Python, package and model versions.
- Transformer model downloads can make first runs slow.
- The dataset is small and synthetic relative to real IoT deployments.
- Deployment on resource-constrained IoT devices was not evaluated.
- The original hardware MITM setup is outside this repo's scope.

## Ethical Scope

Run this only in a local, controlled environment. Do not use it to test, intercept or manipulate traffic on systems you do not own or have explicit permission to assess.
