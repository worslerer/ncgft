from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path



@dataclass(frozen=True)
class ConfigAPI:
    enabled: bool 
    url_api: str 
    token: str 
    name_model: str

@dataclass(frozen = True)
class ConfigLocal:
    enabled: bool
    path_models: Path 
    device: str = "cuda"
    
@dataclass(frozen = True)
class ConfigModel:
    name_model: str 
    max_new_tokens: int 
    temperature: float 
    top_p: float 
    use_safe_tensors: bool 
    
    

@dataclass(frozen=True)
class ConfigQuantization:
    quantization_type: str = "nf4"


@dataclass(frozen=True)
class ConfigTokenizer:
    path_tokenizer: str 
    local_files_only: bool = True
    trust_remote_code: bool = False


@dataclass(frozen=True)
class ConfigLocalRun:

    config_local:       ConfigLocal =    field(default_factory=ConfigLocal)
    config_model:       ConfigModel =       field(default_factory=ConfigModel)
    config_quant:       ConfigQuantization =field(default_factory=ConfigQuantization)
    config_tokenizer:   ConfigTokenizer =   field(default_factory=ConfigTokenizer)


@dataclass(frozen=True)
class ConfigAPIRun:

    config_api:         ConfigAPI =         field(default_factory=ConfigAPI)
    config_model:       ConfigModel =       field(default_factory=ConfigModel)
    config_quant:       ConfigQuantization =field(default_factory=ConfigQuantization)
    config_tokenizer:   ConfigTokenizer =   field(default_factory=ConfigTokenizer)

    

