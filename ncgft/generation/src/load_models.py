import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
from ncgft.shared.cfg.config import ConfigLocalRun 
from pathlib import Path


#print(CONFIG.config_model)


def load_local_model(cfg: ConfigLocalRun):

    path_model = cfg.config_local.path_models / cfg.config_model.name_model
    
    
    
    
    return path_model


def load_api_model():
    return None





#local
#api ->groq, mistral, 
