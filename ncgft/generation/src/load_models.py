import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
from ncgft.shared.cfg.config import ConfigLocalRun 
from pathlib import Path


#print(CONFIG.config_model)


def load_local_model(cfg: ConfigLocalRun):

    path_model = cfg.config_local.path_models / cfg.config_model.name_model

    if not path_model.exists():
        raise FileNotFoundError(f"Working directory: {Path.cwd()}\nSpecified model path: {path_model} DOES NOT EXISTS! \nCheck either: {cfg.config_local.path_models} or: {cfg.config_model.name_model} ")
    
    quant_config = None
    tokenizer = None
    model = None
    
    quant_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_use_double_quant=True,
        bnb_4bit_compute_dtype = torch.float16,
    )


    tokenizer = AutoTokenizer.from_pretrained(
        str(path_model),
        local_files_only = True,
        trust_remote_code = False,
        use_fast = False,
    )

    if tokenizer.pad_token is None and tokenizer.eos_token is not None:
        tokenizer.pad_token = tokenizer.eos_token

    model = AutoModelForCausalLM.from_pretrained(
        str(path_model),
        local_files_only = True,
        trust_remote_code = False,
        quantization_config = quant_config,
        device_map = "auto",
        dtype = torch.float16,
        low_cpu_mem_usage=True,
    )

    if tokenizer.pad_token_id is not None:
        model.config.pad_token_id = tokenizer.pad_token_id

    model.eval()
    return tokenizer, model
    
    
    



def load_api_model():
    return None





#local
#api ->groq, mistral, 
