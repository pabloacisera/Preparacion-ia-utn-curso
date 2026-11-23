### Instalación de modelo de texto mediante llampa.cpp

```bash
sudo apt update && sudo apt install -y git build-essential cmake libcurl4-openssl-dev

git clone https://github.com/ggml-org/llama.cpp
cd llama.cpp

cmake -B build
cmake --build build --config Release -j 2

# descarga desde hugging face

# opcion minima
./build/bin/llama-cli -hf LiquidAI/LFM3-1.7B-GGUF:Q4_K_M


# opcion optima para agentes
./build/bin/llama-cli -hf LiquidAI/LFM3-1.7B-GGUF:Q8_0


# ejecución en cli(más liviana)

./build/bin/llama-cli -m ~/Descargas/tu-modelo.gguf -t 2 -c 2048 --conversation

# o en servidor

./build/bin/llama-server -m ~/Descargas/tu-modelo.gguf -t 2 -c 2048

```


