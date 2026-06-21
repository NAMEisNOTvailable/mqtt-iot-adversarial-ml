# Results Summary

## What I Was Checking

I treated this as a reproduction check, not a claim that I had built a new attack method.

The question was simple: if MQTT-like telemetry messages are modified by the adversarial generator, how do standard anomaly-detection models respond? I focused on the software workflow from the original study, not the hardware MITM testbed.

## Models

- Logistic Regression
- Random Forest
- K Nearest Neighbor
- Multi-Layer Perceptron
- Support Vector Classification

## Results I Would Cite

From the saved notebook run:

- Gamma values ran from about `1.1` to `4.0`.
- Discriminator accuracy ranged from `0.508` to `0.832`.
- False negatives ranged from `15/250` to `72/250`.
- The largest saved false-negative count appeared around gamma `2.1`.
- Different models reacted differently, so the result does not support one clean "best gamma" across every classifier.

## How I Read It

The useful result is not that one number is impressive. The useful result is that false negatives and accuracy move as the generated messages change, and the pattern depends on the model. That makes this a good reproduction/evaluation project, but it should not be overstated as a complete IoT attack implementation.

## Short CV Version

Reproduced a software-only MQTT adversarial-message study, benchmarking five anomaly-detection classifiers against BERT/GAN-inspired messages and analysing accuracy, false negatives, gamma sensitivity and deployment limitations.
