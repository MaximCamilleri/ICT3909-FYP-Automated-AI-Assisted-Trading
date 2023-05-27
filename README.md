# Automated AI Asisted Trading
Trading on the stock market is a risky endeavour, with most inexperienced traders making a loss on their investment. A good trading strategy plays a critical role when investing. This dissertation focuses on the application of Reinforcement Learning (RL) combined with other machine learning techniques to produce a profitable trading strategy. Five state-of-the-art actor-critic algorithms where utilized throughout this project. These are Deep Deterministic Policy Gradient (DDPG), Advantage Actor Critic (A2C), Soft Actor Critic (SAC), Twin Delayed Deep Deterministic Policy Gradient (TD3), and Proximal Policy Optimization (PPO).

The development of these algorithms follows a continues environment, whereby an action space consisting of 29 values indicate the magnitude and direction of actions on the stock market. Each index in the action space refers to an individual ticker part of the DOW30 Index. Additionally, each ticker also consisted of 18 technical indicators on which Principal Component Analysis (PCA) is applied. This reduces the dimensional of the input parameters. Furthermore, the Optune python package was used for hyperparameter optimization. Finally, each of these algorithms where combined into a regime switching approach, whereby all the algorithms would be retrained and reevaluated every 63 days. As the algorithms are evaluated, there Sharpe ratios are calculated over the validation window. This is utilized to select the algorithm to be used over the next trading period. 

The strategy developed in this dissertation utilizes various industry standard metrics and benchmarks to evaluate its performance. The implementation of this system over the years 2017-2020 produces a Sharpe ratio of 1.091 and a cumulative return of 95\%, outperforming the use of the individual components incorporated into the strategy.

## File Structure
```bash
│
├───Data
│   │   data_preparation.ipynb
│   │
│   └───Datasets
│       └───PCA_datasets
│               Dow_no_Pca.csv
│               Dow_Pca_0.7.csv
│               Dow_Pca_0.75.csv
│               Dow_Pca_0.8.csv
│               Dow_Pca_0.85.csv
│               Dow_Pca_0.85_current.csv
│               Dow_Pca_0.9.csv
│               Dow_Pca_0.95.csv
│               Dow_Pca_0.99.csv
│               Dow_Pca_0.99_current.csv
│
├───Hyperparameter Tuning
│   │   optimization.ipynb
│   │
│   └───studies
│           A2C_study.pkl
│           DDPG_study.pkl
│           PPO_study.pkl
│           SAC_study.pkl
│           TD3_study.pkl
│
├───Live Trading
│   │   alpaca.ipynb
│   │   corn_job.ipynb
│   │
│   ├───Models
│   │       sac_85.zip
│   │
│   └───PCA_Models
│           PCA_Model_0.85.pickle
│           PCA_Model_0.99.pickle
│
├───PCA Testing
└───Regime Switching
```
