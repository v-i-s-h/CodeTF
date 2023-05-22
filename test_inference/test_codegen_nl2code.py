import sys
from pathlib import Path
sys.path.append(str(Path(".").absolute().parent))
# sys.path.append("../")
import torch
from codetf.models import load_model_pipeline

model = load_model_pipeline(model_name="causal-lm", task="pretrained",
                model_type="codegen-350M-mono",
                quantize="int8", quantize_algo="bitsandbyte")

prompts = "# check if a string is in valid format"
code_snippets = model.predict([prompts])

print(code_snippets)