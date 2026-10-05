# Technical names: machine learning

These are technical names for machine learning, deep learning, MLOps, and responsible AI.
Use them as nouns, or as modifiers before a noun.
Do not use a technical name as a verb (rule W6).
Use the official spelling and case. Write model IDs, metric names in code, and parameters as inline code.
A name in parentheses is the short name or the acronym. Write the full name at the first use (rule W7).
This list is not complete. Any official name is a technical name (rule W5).

## Core concepts

- machine learning (ML), artificial intelligence (AI), deep learning, model, ML model, machine learning model, algorithm, training, inference, prediction, predictive model, baseline model, champion model, challenger model, model version, model artifact, model weights, weight, bias, hyperparameter, model architecture
- objective function, loss function, cost function, loss, gradient, gradient descent, stochastic gradient descent (SGD), learning rate, learning rate schedule, optimizer, Adam optimizer, AdamW, momentum, batch size, mini-batch, epoch, iteration, convergence, local minimum
- overfitting, underfitting, generalization, bias-variance tradeoff, regularization, L1 regularization, L2 regularization, dropout, early stopping, weight decay, data leakage, target leakage, curse of dimensionality

## Data and features

- training data, training set, validation set, test set, holdout set, evaluation set, train-test split, cross-validation, k-fold cross-validation, stratified sampling, data split, observation, feature, feature vector, feature engineering, feature selection, feature importance
- feature store, online feature store, offline feature store, feature view, feature group, point-in-time join, training-serving skew, label, target variable, ground truth, annotation, data labeling, labeling, labeler, annotator, label noise
- class, class imbalance, imbalanced dataset, oversampling, undersampling, Synthetic Minority Oversampling Technique (SMOTE), data augmentation, synthetic data, one-hot encoding, label encoding, standardization, min-max scaling, feature scaling, missing value, imputation, outlier
- categorical feature, numerical feature, continuous feature, ordinal feature, time series, lag feature, seasonality, trend, stationarity, Data Version Control (DVC)

## Learning types and tasks

- supervised learning, unsupervised learning, semi-supervised learning, self-supervised learning, reinforcement learning (RL), transfer learning, online learning, federated learning, active learning, multi-task learning, few-shot learning, zero-shot learning, contrastive learning
- classification, binary classification, multiclass classification, multi-label classification, regression, linear regression, logistic regression, clustering, recommendation, recommender system, collaborative filtering, content-based filtering, ranking, forecasting, time series forecasting
- natural language processing (NLP), computer vision (CV), object detection, image classification, image segmentation, semantic segmentation, optical character recognition (OCR), speech recognition, automatic speech recognition (ASR), sentiment analysis, named entity recognition (NER), entity extraction, topic modeling, text classification, machine translation, question answering
- policy, reward, reward function, episode, exploration, exploitation

## Algorithms and model types

- decision tree, random forest, gradient boosting, gradient-boosted trees, XGBoost, LightGBM, CatBoost, support vector machine (SVM), naive Bayes, k-means, DBSCAN, hierarchical clustering, Gaussian mixture model (GMM), t-SNE, UMAP
- autoencoder, variational autoencoder (VAE), generative adversarial network (GAN), diffusion model, ARIMA, Prophet, ensemble, ensemble model, bagging, stacking, linear model, tree-based model, isolation forest, Markov chain, hidden Markov model (HMM), Bayesian model, Bayesian optimization

## Neural networks and deep learning

- neural network, artificial neural network, neuron, input layer, hidden layer, output layer, dense layer, fully connected layer, convolutional layer, pooling layer, activation function, ReLU, sigmoid function, softmax function, tanh, GELU
- convolutional neural network (CNN), recurrent neural network (RNN), long short-term memory (LSTM), gated recurrent unit (GRU), transformer, transformer architecture, attention, attention mechanism, self-attention, multi-head attention, encoder, decoder, encoder-decoder model, positional encoding
- residual connection, layer normalization, batch normalization, backpropagation, vanishing gradient, exploding gradient, gradient clipping, weight initialization, pretrained model, pretraining, foundation model, model checkpoint, mixed precision, mixed-precision training
- knowledge distillation, distillation, student model, teacher model, pruning, ResNet, BERT, vision transformer (ViT), U-Net, YOLO, CLIP

## Training

- model training, training job, training run, training pipeline, training loop, distributed training, data parallelism, model parallelism, tensor parallelism, pipeline parallelism, fully sharded data parallel (FSDP), DeepSpeed, gradient accumulation
- hyperparameter tuning, hyperparameter optimization (HPO), grid search, random search, Optuna, Ray Tune, experiment, experiment tracking, learning curve, loss curve, training loss, validation loss, retraining, continual learning, random seed, seed, reproducibility, compute budget, GPU hour

## Evaluation and metrics

- probability, fraud, fraud detection, fraud case, manual review, review, model evaluation, evaluation metric, offline evaluation, online evaluation, accuracy, precision, recall, F1 score, F-beta score, specificity, sensitivity, true positive (TP), true negative (TN), false positive (FP), false negative (FN), false positive rate (FPR), true positive rate (TPR)
- confusion matrix, receiver operating characteristic (ROC) curve, ROC curve, area under the curve (AUC), ROC AUC, precision-recall curve, PR AUC, log loss, cross-entropy, mean absolute error (MAE), mean squared error (MSE), root mean squared error (RMSE), mean absolute percentage error (MAPE), R-squared, coefficient of determination
- mean average precision (mAP), hit rate, top-k accuracy, perplexity, BLEU, ROUGE, word error rate (WER), character error rate (CER), intersection over union (IoU), calibration, calibration curve, confidence score, confidence interval, statistical significance, p-value, decision threshold
- lift, uplift, business metric, guardrail metric, benchmark, leaderboard, error analysis, data slice

## Deployment and serving

- model deployment, model serving, model server, inference endpoint, real-time inference, online inference, batch inference, batch prediction, streaming inference, edge inference, on-device inference, inference latency, inference cost
- model registry, model stage, model promotion, multi-armed bandit, champion-challenger test, model package, model container, ONNX, ONNX Runtime, TorchScript, TensorRT, NVIDIA Triton Inference Server, Triton Inference Server, TorchServe, TensorFlow Serving, KServe, Seldon Core, BentoML, Ray Serve
- model compression, model optimization, GPU instance, inference accelerator, prediction log

## MLOps and monitoring

- MLOps, LLMOps, machine learning operations, ML pipeline, inference pipeline, continuous training (CT), model monitoring, model drift, data drift, concept drift, prediction drift, feature drift, covariate shift, label shift, drift detection
- population stability index (PSI), Kolmogorov-Smirnov test (KS test), Jensen-Shannon divergence, Kullback-Leibler divergence (KL divergence), Wasserstein distance, performance degradation, model decay, retraining trigger, feedback loop
- model lineage, model governance, model risk management, model inventory, model card, intended use, out-of-scope use, limitation, datasheet for datasets, data card, model documentation
- MLflow, MLflow Tracking, MLflow Model Registry, Weights & Biases (W&B), Comet, ClearML, Kubeflow, Kubeflow Pipelines, Metaflow, ZenML, Feast, Tecton, Hopsworks, Evidently, Evidently AI, WhyLabs, Arize AI, Fiddler AI, Label Studio, Labelbox, Scale AI

## Responsible AI

- responsible AI, AI governance, AI risk management, fairness, algorithmic bias, demographic parity, equalized odds, equal opportunity, disparate impact, protected attribute, sensitive attribute
- explainability, interpretability, explainable AI (XAI), SHAP, LIME, feature attribution, counterfactual explanation, partial dependence plot (PDP), model transparency, accountability, human oversight
- differential privacy, membership inference attack, model inversion attack, adversarial example, adversarial attack, data poisoning, model robustness, robustness, AI incident, NIST AI Risk Management Framework (AI RMF), ISO/IEC 42001, high-risk AI system, impact assessment

## Tools and frameworks

- SciPy, scikit-learn, statsmodels, PyTorch, PyTorch Lightning, TensorFlow, Keras, JAX, Flax, Hugging Face, Hugging Face Hub, Hugging Face Transformers, Transformers library, Datasets library, Accelerate
- spaCy, NLTK, Gensim, OpenCV, Matplotlib, seaborn, Plotly, Ray, Dask, RAPIDS, cuDF, CUDA, cuDNN, NCCL, Spark MLlib, H2O.ai, AutoML, Google Colab, Kaggle

## Hardware and performance

- graphics processing unit (GPU), tensor processing unit (TPU), neural processing unit (NPU), NVIDIA, NVIDIA A100, NVIDIA H100, NVIDIA H200, NVIDIA B200, NVIDIA L4, NVIDIA T4, GPU memory, VRAM, high-bandwidth memory (HBM), NVLink, InfiniBand
- FLOPS, TFLOPS, dynamic batching, continuous batching, memory bandwidth, compute-bound, memory-bound
