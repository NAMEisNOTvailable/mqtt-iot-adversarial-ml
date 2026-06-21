# Results Summary

## Reproduction Question

The study asked whether adversarial MQTT-like messages could affect anomaly-detection models by increasing false negatives or reducing detection accuracy.

The reproduction focused on the software and algorithmic part of the original work rather than the original hardware MITM testbed.

## Models Benchmarked

- Logistic Regression
- Random Forest
- K Nearest Neighbor
- Multi-Layer Perceptron
- Support Vector Classification

## Supported Findings

The saved notebook and report support these claims:

- The experiment generated adversarial MQTT-like messages from sample telemetry data and evaluated model behaviour under changing gamma values.
- The discriminator run covered gamma values from approximately `1.1` to `4.0`.
- In the saved discriminator run, accuracy ranged from `0.508` to `0.832`.
- False negatives ranged from `15/250` to `72/250`, with the largest saved value occurring around gamma `2.1`.
- The report found that false-negative behaviour and accuracy were sensitive to perturbation settings, but model responses were not uniform.
- The reproduction did not establish one stable gamma value that generalises cleanly across every model.

## Interpretation

The project is strongest as a reproduction and evaluation exercise, not as a claim of a new attack method. Its value is in showing how generated adversarial messages can be tested against multiple anomaly-detection models, how false negatives can be tracked, and how reproduction limitations should be documented.

## Resume-Ready Summary

Reproduced a software-only MQTT adversarial-message study, benchmarking five anomaly-detection classifiers against BERT/GAN-inspired messages and analysing accuracy, false negatives, gamma sensitivity and deployment limitations.
