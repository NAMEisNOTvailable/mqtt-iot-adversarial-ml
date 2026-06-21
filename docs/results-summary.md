# Results Summary

## Question

Can generated MQTT-like messages change anomaly-detection behaviour in the reproduced software workflow?

The experiment modifies sample telemetry messages, runs several classifiers, and compares accuracy and false negatives as the perturbation setting changes.

## Models

- Logistic Regression
- Random Forest
- K Nearest Neighbor
- Multi-Layer Perceptron
- Support Vector Classification

## Results

From the saved notebook run:

- Gamma values covered about `1.1` to `4.0`.
- Discriminator accuracy ranged from `0.508` to `0.832`.
- False negatives ranged from `15/250` to `72/250`.
- The largest saved false-negative count appeared around gamma `2.1`.
- Different models reacted differently, so the result does not support one clean "best gamma" across every classifier.

## Interpretation

The result is useful for comparing classifier sensitivity to generated MQTT-like messages. Accuracy and false negatives moved as the generated messages changed, and the pattern differed by classifier.
