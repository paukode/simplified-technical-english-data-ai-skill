# Examples: machine learning

Each example shows text before and after the change to STE.
The rule IDs refer to `references/writing-rules.md`.

## 1. The intended use and the limitations in a model card

Type: mixed

Before:

~~~text
The churn model is great at predicting which customers are likely to cancel, but it shouldn't really be used for anything like credit decisions, and it may not work as well for brand-new customers.
~~~

After:

~~~text
Intended use: The `churn-xgb` model (version 3.2) calculates the probability that a customer cancels the subscription in the next 30 days. The retention team uses the output to select customers for retention actions.

Out-of-scope use: Do not use the model for credit decisions.

Limitations: For customers with less than 30 days of history, the model is less accurate. In the test on 2026-09-01, the AUC was 0.81 for all customers and 0.64 for new customers.
~~~

Changes: the model ID and the version (M3), measured values (M2), and no "should" or "may" (V4).

## 2. Retrain a model

Type: procedure

Before:

~~~text
To retrain, kick off the training pipeline with the latest feature snapshot, and once it's done, compare the new model's AUC against the champion before promoting it.
~~~

After:

~~~text
1. Start the training pipeline with the feature snapshot of the current week.
2. When the training job is complete, find the AUC of the new model on the test set.
3. Compare this AUC with the AUC of the champion model on the same test set.
4. If the new model is better by 0.01 or more, register the new model as the challenger model.
5. If the new model is not better, stop. Do not change the champion model.
~~~

Changes: one instruction in each step (P2), each decision as a condition (P6), and no phrasal verbs (V7).

## 3. Drift alert for a feature

Type: mixed

Before:

~~~text
Heads up, feature drift detected on 'avg_basket_value' - PSI is way over threshold, the model's predictions might be getting less reliable.
~~~

After:

~~~text
The population stability index (PSI) of the feature `avg_basket_value` is 0.31 for the last 7 days. The limit is 0.2.

A PSI of more than 0.2 shows a large change in the distribution of the feature.

Examine the input data. Then compare the accuracy of the model with the baseline.
~~~

Changes: the value and the limit (M6), the full term before the acronym (W14), and no "might" (V4).

## 4. Evaluation results of a new model

Type: description

Before:

~~~text
The new model is way more accurate and basically never misses fraud now.
~~~

After:

~~~text
We did the evaluation of the `fraud-gbm-v7` model on 2026-09-28. The test set contained 120,000 transactions from August 2026, with 1,450 fraud cases.

| Metric | `fraud-gbm-v6` | `fraud-gbm-v7` |
|---|---|---|
| Recall | 0.82 | 0.89 |
| Precision | 0.74 | 0.71 |
| False positive rate | 0.31% | 0.38% |

The new model finds more fraud cases. But it also sends more correct transactions to manual review.
~~~

Changes: measured values with the test set and the date (M2), a table for the values (D4), and the cost of the change (D3).

## 5. The feature store

Type: description

Before:

~~~text
The feature store keeps training and serving consistent by computing features once and serving them both offline (for training) and online (low-latency lookups at inference time).
~~~

After:

~~~text
The feature store calculates each feature one time. It then supplies the same feature values to the training jobs and to the inference endpoints.

- The offline feature store keeps the history of the feature values. The training jobs read from it.
- The online feature store keeps the current value of each feature. The inference endpoints read from it in less than 10 ms.

This prevents training-serving skew.
~~~

Changes: no "-ing" verb forms (V3), a vertical list (S4), and a measured value (M6).

## 6. A canary deployment of a model

Type: procedure

Before:

~~~text
Roll out the new model to 5% of traffic first and keep an eye on latency and error rates for an hour before ramping up.
~~~

After:

~~~text
1. Send 5% of the traffic to the new model.
2. Monitor the p99 latency and the error rate for 1 hour.
3. If the p99 latency is less than 200 ms and the error rate is less than 0.5%, go to step 4. If not, go to step 7.
4. Send 50% of the traffic to the new model.
5. Monitor the p99 latency and the error rate for 1 more hour. If the values are in the limits, go to step 6. If not, go to step 7.
6. Send 100% of the traffic to the new model. The procedure is complete.
7. Send all the traffic to the old model. Then examine the logs of the new model.
~~~

Changes: no phrasal verbs or slang (V7, W9), specific limits (W13), and each decision as a condition (P6).
