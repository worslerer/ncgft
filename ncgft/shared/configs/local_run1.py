from pathlib import Path
from ncgft.shared.cfg.config import (
    ConfigLocalRun,
    ConfigLocal,
    ConfigModel,
    ConfigQuantization,
    ConfigTokenizer
)


CONFIG = ConfigLocalRun(

    config_local=ConfigLocal(
        enabled=True, 
        path_models=Path("/home/test/caise-ner/ncgft/models"),
        device="cuda",
    ),
    config_model=ConfigModel(
        name_model="Qwen2.5-7B-Instruct",
        max_new_tokens=2048,
        temperature=0.5,
        top_p=0.9,
        use_safe_tensors=True,
    ),
    config_quant=ConfigQuantization(
        quantization_type="nf4",
    ),
    config_tokenizer=ConfigTokenizer(
        local_files_only=True,
        trust_remote_code=False,
    ),
)
