# pip install ollama    (ya tienes Qwen3 corriendo)
import ollama
r = ollama.chat(model="qwen3:8b", messages=[{"role":"user","content":"Di hola en una línea."}])
print(r["message"]["content"])