
# %%
import base64
import json
from io import BytesIO
import os
from dotenv import load_dotenv, find_dotenv
from groq import Groq
from pdf2image import convert_from_path

def get_agnostic_pdf_classes(pdf_path: str) -> list:
    """
    Converts PDF pages into images and uses Groq's active production vision model
    to extract and classify content chunks into text, table, or code.
    """
    # 1. Load environment and initialize Groq client
    load_dotenv(find_dotenv())
    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        raise ValueError("GROQ_API_KEY not found in the environment variables.")

    client = Groq(api_key=api_key)

    # 2. Render PDF pages into PIL images
    pdf_pages = convert_from_path(pdf_path)
    classified_chunks = []

    # 3. Vision prompt tailored for RAG structural classification
    vision_prompt = """
    Visually analyze this document page. Extract 100% of its content and strictly classify it into a list using the following valid JSON format. Do not include any conversational introduction, preamble, or markdown code blocks (such as ```json):

    [
      {"class": "text" or "table" or "code", "content": "exact extracted text content"}
    ]

    Rules:
    1. Transcribe the document text exactly as it is written in its original language (Spanish).
    2. Maintain all original indentation and spacing for code segments ("code").
    3. Format table contents line-by-line so that rows and fields remain structurally legible.
    """

    # 4. Iterate over each rendered page
    for page in pdf_pages:
        # Convert PIL Image object to JPEG bytes in memory
        memory_buffer = BytesIO()
        page.save(memory_buffer, format="JPEG")

        # Encode bytes to Base64 string
        base64_image = base64.b64encode(memory_buffer.getvalue()).decode('utf-8')

        # 5. Execute Groq Vision API call using the official active vision endpoint
        api_response = client.chat.completions.create(
            model="qwen/qwen3.8-27b",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": vision_prompt},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{base64_image}"
                            }
                        }
                    ]
                }
            ],
            temperature=0.0,
            response_format={"type": "json_object"}
        )

        # 6. FIX: Correctly access the string content through choices[0].message.content
        string_payload = api_response.choices[0].message.content
        raw_json_content = json.loads(string_payload)

        if isinstance(raw_json_content, list):
            classified_chunks.extend(raw_json_content)
        elif isinstance(raw_json_content, dict):
            # Extract internal list if the model wraps the array in a root key
            first_root_value = next(iter(raw_json_content.values()))
            if isinstance(first_root_value, list):
                classified_chunks.extend(first_root_value)
            else:
                classified_chunks.append(raw_json_content)

    return classified_chunks

# Execution block
document_chunks = get_agnostic_pdf_classes("../_documentos/documento_complejo.pdf")
print(document_chunks)


# %%
from langchain_text_splitters import RecursiveCharacterTextSplitter

# =====================================================================
# MODULE 2: SEMANTIC TEXT PROCESSING (Conceptual Semantic Chunking)
# =====================================================================
def group_chunks_semantically(structural_chunks: list) -> list:
    """
    Groups plain text chunks by meaning using basic transitional connectors.
    Tables and code blocks are preserved intact and bypass semantic merging.
    """
    semantic_chunks = []
    text_accumulator = []

    # Universal semantic topic-change indicators
    topic_transition_keywords = ("Por otro lado,", "En cuanto a", "Además,", "Sin embargo,")

    for chunk in structural_chunks:
        chunk_class = chunk["class"]
        chunk_content = chunk["content"]

        if chunk_class == "text":
            # Check if the text starts with a semantic topic change indicator
            has_topic_changed = any(chunk_content.startswith(keyword) for keyword in topic_transition_keywords)

            if has_topic_changed and text_accumulator:
                semantic_chunks.append({
                    "type": "text_semantic",
                    "content": " ".join(text_accumulator)
                })
                text_accumulator = [chunk_content]
            else:
                text_accumulator.append(chunk_content)
        else:
            # If we encounter a non-text block, flush the accumulated text first
            if text_accumulator:
                semantic_chunks.append({
                    "type": "text_semantic",
                    "content": " ".join(text_accumulator)
                })
                text_accumulator = []

            # Append tables or code preserving their distinct structures
            semantic_chunks.append({
                "type": chunk_class,
                "content": chunk_content
            })

    # Flush any remaining text at the end of the loop
    if text_accumulator:
        semantic_chunks.append({
            "type": "text_semantic",
            "content": " ".join(text_accumulator)
        })

    return semantic_chunks

group_chunks_semantically(document_chunks)

# %%
# =====================================================================
# MODULE 3: TOKEN COUNTING UTILITY (OpenAI tiktoken integration)
# =====================================================================
import tiktoken


def count_tokens_with_tiktoken(text: str) -> int:
    """
    Calculates the exact token length of a given text using OpenAI's standard encoding.
    """
    token_encoder = tiktoken.get_encoding("cl100k_base")
    return len(token_encoder.encode(text))


# Execution and verification block for Module 3
# Catching the output from your exact Block 2 function call
semantic_pipeline_output = group_chunks_semantically(document_chunks)

print("[MODULE 3 INFO] Token counting utility initialized.")
print(f"Total semantic blocks to process from Block 2: {len(semantic_pipeline_output)}")
print("-" * 50)

for idx, chunk in enumerate(semantic_pipeline_output):
    tokens = count_tokens_with_tiktoken(chunk["content"])
    print(f"Block {idx + 1} ({chunk['type']}) -> Total Tokens: {tokens}")

# %%
# =====================================================================
# MODULE 4: RECURSIVE REFINEMENT BY TOKENS (LangChain Integration)
# =====================================================================
from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_chunks_by_tokens(semantic_chunks: list, max_tokens: int = 30) -> list:
    """
    Uses LangChain's RecursiveCharacterTextSplitter measured by real tokens.
    Only breaks down semantic text blocks that exceed the max token limit.
    """
    final_rag_chunks = []

    # Initialize LangChain splitter powered by our tiktoken counter function
    langchain_splitter = RecursiveCharacterTextSplitter(
        chunk_size=max_tokens,
        chunk_overlap=5,
        length_function=count_tokens_with_tiktoken,
        separators=["\n\n", "\n", " ", ""],
    )

    for chunk in semantic_chunks:
        chunk_type = chunk["type"]
        chunk_content = chunk["content"]

        # Only split text blocks if they exceed our token limit ceiling
        if (
            chunk_type == "text_semantic"
            and count_tokens_with_tiktoken(chunk_content) > max_tokens
        ):
            sub_token_chunks = langchain_splitter.split_text(chunk_content)
            for sub_chunk in sub_token_chunks:
                final_rag_chunks.append(
                    {"chunk_type": "text_recursive_tokens", "content": sub_chunk}
                )
        else:
            # Code segments and Tables preserve their integral structures completely
            final_rag_chunks.append(
                {"chunk_type": f"{chunk_type}_integral", "content": chunk_content}
            )

    return final_rag_chunks


# Execution block for Module 4 (Setting safe token baseline size to 30)
final_embedding_payload = split_chunks_by_tokens(
    semantic_pipeline_output, max_tokens=30
)

print(f"[MODULE 4 INFO] Fixed token threshold pipeline complete.")
print(
    f"Final total chunks ready for the embedding model: {len(final_embedding_payload)}\n"
)
print("=" * 60)

for idx, final_chunk in enumerate(final_embedding_payload):
    token_count = count_tokens_with_tiktoken(final_chunk["content"])
    print(
        f"--- RAG CHUNK {idx + 1} [{final_chunk['chunk_type'].upper()} | TOKENS: {token_count}] ---"
    )
    print(final_chunk["content"])
    print("=" * 60)

# %%
%pip install fastembed

# %%
# =====================================================================
# MODULE 5 (ALTERNATIVA LIVIANA): EMBEDDINGS CON FASTEMBED
# =====================================================================
from fastembed import TextEmbedding

def generate_embeddings_with_fastembed(final_rag_chunks: list) -> list:
    """
    Genera vectores de embedding de forma liviana usando ONNX Runtime (sin PyTorch).
    """
    print("[MODULE 5 INFO] Cargando modelo liviano con FastEmbed...")

    # Usamos un modelo estándar equivalente y muy eficiente (All-MiniLM-L6-v2)
    embedding_model = TextEmbedding(model_name="BAAI/bge-small-en-v1.5") # o puedes usar el modelo por defecto

    # Extraemos solo el contenido de texto de los chunks para enviarlos en lote
    texts_to_embed = [chunk["content"] for chunk in final_rag_chunks]

    print(f"[MODULE 5 INFO] Generando vectores para {len(texts_to_embed)} chunks...")

    # FastEmbed procesa los textos de forma eficiente en lotes (batching)
    embeddings_generator = embedding_model.embed(texts_to_embed)
    embeddings_list = list(embeddings_generator)

    vector_database_payload = []

    for idx, (chunk, vector) in enumerate(zip(final_rag_chunks, embeddings_list)):
        vector_database_payload.append({
            "id": f"chunk_{idx + 1}",
            "chunk_type": chunk["chunk_type"],
            "content": chunk["content"],
            "embedding": vector.tolist(), # Convertimos el array de numpy a lista estándar
            "metadata": {
                "length_tokens": count_tokens_with_tiktoken(chunk["content"])
            }
        })
        print(f"Vectorizado Chunk {idx + 1} [{chunk['chunk_type'].upper()}] -> Dimensión: {len(vector)}")

    return vector_database_payload

# Ejecución del Módulo 5 optimizado
vector_database_ready = generate_embeddings_with_fastembed(final_embedding_payload)

print("=" * 60)
print(f"[MODULE 5 INFO] ¡Pipeline RAG completado sin sobrecargar el disco!")
print(f"Total de registros listos: {len(vector_database_ready)}")


