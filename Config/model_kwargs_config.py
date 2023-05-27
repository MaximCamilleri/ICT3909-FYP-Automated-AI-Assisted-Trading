A2C_KWARGS = {
    'gamma': 0.9999,
    'normalize_advantage': False,
    'max_grad_norm': 1,
    'use_rms_prop': True,
    'gae_lambda': 0.95,
    'n_steps': 128,
    'learning_rate': 0.000178696,
    'ent_coef': 0.000638231,
    'vf_coef': 0.571503041
}

PPO_KWARGS = {
    'gamma': 0.95,
    'batch_size': 256,
    'n_steps': 8,
    'learning_rate': 0.000210185,
    'ent_coef': 0.004309815,
    'clip_range': 0.4,
    'n_epochs': 1,
    'gae_lambda': 0.8,
    'max_grad_norm': 0.8,
    'vf_coef': 0.640960538
}

DDPG_KWARGS = {
    'gamma': 0.95,
    'action_noise': 'normal',
    'batch_size': 1024,
    'buffer_size': 1000000,
    'train_freq': 256,
    'tau': 0.005,
    'learning_rate': 4.080859069673294e-05
}

TD3_KWARGS = {
    'gamma': 0.98,
    'learning_rate': 0.010268730,
    'batch_size': 2048,
    'buffer_size': 1000,
    'tau': 0.005,
    'train_freq': 128,
    'action_noise': 'ornstein_uhlenbeck'
}

SAC_KWARGS = {
    'gamma': 0.9999,
    'learning_rate': 0.000024623,
    'batch_size': 256,
    'buffer_size': 1000000,
    'learning_starts': 0,
    'train_freq': 1,
    'tau': 0.001
}

TIMESTEPS_DICT = {
    'a2c' : 2_000, 
    'ppo' : 2_000, 
    'ddpg' : 2_000,
    'sac' : 2_000,
    'td3' : 2_000
}
