import gpt_2_simple as gpt2
import os

#Download model
model_name = os.environ['GPT2_MODEL_NAME']
if not os.path.isdir(os.path.join("models", model_name)):
    print(f"Downloading {model_name} model...")
    gpt2.download_gpt2(model_name=model_name)  # model is saved into current directory under /models/124M/
