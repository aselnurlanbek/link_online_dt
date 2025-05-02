# Automatically generated type hinting file for a .ini file
# Generated with config-to-object https://pypi.org/project/config-to-object/1.0.0/
# Run "ini_typefile your_config.ini type_file.py" to create a new type file

from typing import NamedTuple, List, Tuple

class Env(NamedTuple):
    env_name:str
    minari_dataset_name:str
    seed:int
    train_seed:int
    deterministic_torch:bool

class Eval(NamedTuple):
    eval_freq:int
    n_eval_episodes:int
    target_returns:Tuple[float]
    checkpoints_path:str
    eval_rtg:int   #odt
    eval_context_length:int #odt
    ordering:int #odt

class WandbConfig(NamedTuple):
    wandb_group:str
    wandb_name:str
    log_to_tb:bool   #odt
    save_dir: str #odt
    exp_name: str  #odt

class Train(NamedTuple):
    algorithm_name:str
    embedding_dim:int
    num_layers:int
    num_heads:int
    seq_len:int
    episode_len:int
    attention_dropout:float
    residual_dropout:float
    embedding_dropout:float
    learning_rate:float
    beta1:float
    beta2:float
    weight_decay:float
    clip_grad:float
    batch_size:int
    max_update_steps:int
    warmup_steps:int
    print_freq:int
    load_model:str
    init_temperature:float   #odt


    # Pretraining ODT
    max_pretrain_iters: int
    online_rtg:int
    num_online_rollouts:int
    replay_size:int
    num_updates_per_online_iter:int

class Normalize(NamedTuple):
    state_normalization:bool
    return_scale:float

class Config(NamedTuple):
    Env:Env
    Eval:Eval
    WandbConfig:WandbConfig
    Train:Train
    Normalize:Normalize