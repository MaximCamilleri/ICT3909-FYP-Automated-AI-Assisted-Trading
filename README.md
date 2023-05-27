# Automated AI Asisted Trading
Trading on the stock market is a risky endeavour, with most inexperienced traders making a loss on their investment. A good trading strategy plays a critical role when investing. This dissertation focuses on the application of Reinforcement Learning (RL) combined with other machine learning techniques to produce a profitable trading strategy. Five state-of-the-art actor-critic algorithms were utilized throughout this project. These are Advantage Actor-Critic (A2C), Soft Actor-Critic (SAC), Deep Deterministic Policy Gradient (DDPG), Twin Delayed Deep Deterministic Policy Gradient (TD3), and Proximal Policy Optimization (PPO).

The development of these algorithms follows a continuous environment, whereby an action space consisting of 29 values indicates the magnitude and direction of actions on the stock market. Each index in the action space refers to an individual ticker part of the DOW30 Index. Additionally, each ticker also consisted of 18 technical indicators on which Principal Component Analysis (PCA) is applied. This reduces the dimensionality of the input parameters. Furthermore, the Optune Python package was used for hyperparameter optimization. Finally, each of these algorithms where combined into a regime switching approach, whereby all the algorithms would be retrained and reevaluated every 63 days. As the algorithms are evaluated, there Sharpe ratios are calculated over the validation window. This is utilized to select the algorithm to be used over the next trading period. 

The strategy developed in this dissertation utilizes various industry standard metrics and benchmarks to evaluate its performance. The implementation of this system over the years 2017-2020 produces a Sharpe ratio of 1.058 and a cumulative return of 96.7\%, outperforming the use of the individual components incorporated into the strategy.

## Dependences 
This project is depended on the FinRL Git repository. For instructions on installation please refer to https://github.com/AI4Finance-Foundation/FinRL

## File Structure
```bash
│
├───Config
│       alpacha_config.py
│       local_config.py
│       model_kwargs_config.py
│
├───Data
│   │   data_preparation.ipynb
│   │
│   ├───Datasets
│   │   └───PCA_datasets
│   │           Dow_no_Pca.csv
│   │           Dow_Pca_0.7.csv
│   │           Dow_Pca_0.75.csv
│   │           Dow_Pca_0.8.csv
│   │           Dow_Pca_0.85.csv
│   │           Dow_Pca_0.85_current.csv
│   │           Dow_Pca_0.9.csv
│   │           Dow_Pca_0.95.csv
│   │           Dow_Pca_0.99.csv
│   │           Dow_Pca_0.99_current.csv
│   │
│   └───PCA_Algorithms
│           PCA_Model_0.7.pickle
│           PCA_Model_0.75.pickle
│           PCA_Model_0.8.pickle
│           PCA_Model_0.85.pickle
│           PCA_Model_0.9.pickle
│           PCA_Model_0.95.pickle
│           PCA_Model_0.99.pickle
│
├───Hyperparameter Tuning
│   │   optimization.ipynb
│   │
│   ├───Best Trials
│   │       A2C_trial_73.pth
│   │       DDPG_trial_44.pth
│   │       PPO_trial_23.pth
│   │       SAC_trial_32.pth
│   │       TD3_trial_41.pth
│   │
│   ├───Results
│   │   ├───A2C
│   │   │       Comparison Between Tuned and Base A2C Models.png
│   │   │       emp_dist_func.png
│   │   │       opt_hist.png
│   │   │       params_importances.png
│   │   │
│   │   ├───DDPG
│   │   │       emp_dist_func.png
│   │   │       opt_hist.png
│   │   │       params_importances.png
│   │   │
│   │   ├───PPO
│   │   │       Comparison Between Tuned and Base PPO Models.png
│   │   │       emp_dist_func.png
│   │   │       opt_hist.png
│   │   │       params_importances.png
│   │   │
│   │   ├───SAC
│   │   │       Comparison Between Tuned and Base SAC Models.png
│   │   │       emp_dist_func.png
│   │   │       opt_hist.png
│   │   │       params_importances.png
│   │   │
│   │   └───TD3
│   │           Comparison Between Tuned and Base TD3 Models.png
│   │           emp_dist_func.png
│   │           opt_hist.png
│   │           params_importances.png
│   │
│   └───Studies
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
│   │   PCA_Testing.ipynb
│   │
│   └───Results
│           In sample cumulative reuturns for PCA tests on A2C.png
│           In sample cumulative reuturns for PCA tests on PPO.png
│           In sample cumulative reuturns for PCA tests on TD3.png
│           Out of sample cumulative reuturns for PCA tests on A2C Test2.png
│           Out of sample cumulative reuturns for PCA tests on A2C.png
│           Out of sample cumulative reuturns for PCA tests on PPO Test2.png
│           Out of sample cumulative reuturns for PCA tests on PPO.png
│           Out of sample cumulative reuturns for PCA tests on TD3 Test2.png
│           Out of sample cumulative reuturns for PCA tests on TD3.png
│
└───Regime Switching
    │   ensemble_strategy.ipynb
    │
    └───Results
        │   AllAlgorithmVariationResults.png
        │   DrawdownPeriods.png
        │   MonthlyReturnsDOW.png
        │   MonthlyReturnsRegimeSwitching.png
        │   RegimeSwithcingVSDow.png
        │
        └───CSV
                account_value.csv
                account_value3.csv
                actions.csv
                actions3.csv
                summery.csv
                summery3.csv
```
