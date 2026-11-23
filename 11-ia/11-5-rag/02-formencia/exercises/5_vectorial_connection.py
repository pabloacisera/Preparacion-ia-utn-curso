# /*
#   * Luego de la segmentación (chunking) del texto largo,
#   * se procede a generar el embedding y empaquetar
#   * cada segmento para pasarlo por la función de creación de puntos.
# */

import os
import hashlib
from datetime import datetime
from dotenv import load_dotenv, find_dotenv
from qdrant_client import QdrantClient, models
from qdrant_client.http.models import PointStruct, Document

# Cargar variables de entorno
load_dotenv(find_dotenv())

qdrant_url = os.getenv("QDRANT_ENDPOINT")
qdrant_api_key = os.getenv("QDRANT_API_KEY")

# Inicializar el cliente con inferencia en la nube
qdrant_client = QdrantClient(
    url=qdrant_url, api_key=qdrant_api_key, cloud_inference=True
)

COLLECTION_NAME = "scalar_collection"

# Texto de prueba sobre la fotosíntesis
text_to_save = (
    "Photosynthesis is the vital biological process used by green plants, algae, "
    "and certain bacteria to convert light energy from the sun into chemical energy. "
    "Inside specialized cell structures called chloroplasts, chlorophyll absorbs "
    "sunlight to transform water and carbon dioxide into glucose, a sugar that "
    "fuels the organism's growth and metabolism. As a crucial byproduct of this "
    "reaction, oxygen is released back into the atmosphere, sustaining almost "
    "all aerobic life on Earth and regulating global carbon cycles."
)


def fn_create_collection():
    if not qdrant_client.collection_exists(collection_name=COLLECTION_NAME):
        qdrant_client.create_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=models.VectorParams(
                size=384, distance=models.Distance.COSINE, on_disk=True
            ),
            quantization_config=models.ScalarQuantization(
                scalar=models.ScalarQuantizationConfig(
                    type=models.ScalarType.INT8,
                    quantile=0.99,  # excluye el 1% de los vecinos
                    always_ram=True,  # vectores cuantizados
                )
            ),
        )
        print("\n[✔] Colección creada y configurada exitosamente.")
    else:
        print("\n[ℹ] La colección ya existe.")


def fn_get_collections():
    # Lista todas las colecciones del clúster
    colls = qdrant_client.get_collections()
    print(f"\nColecciones en el clúster: {colls}")


def fn_get_one_collection():
    # Obtiene detalles de la colección en específico
    try:
        info = qdrant_client.get_collection(collection_name=COLLECTION_NAME)
        print(f"\n--- Detalles de '{COLLECTION_NAME}' ---")
        print(info)
    except Exception as e:
        print(f"\n[❌] Error: La colección probablemente no existe todavía. ({e})")


def fn_create_point():
    # Generamos un ID fijo basado en el contenido (Evita duplicados si se ejecuta muchas veces)
    point_id = hashlib.md5(text_to_save.encode("utf-8")).hexdigest()

    points = [
        PointStruct(
            id=point_id,
            payload={
                "topic": "natural science",
                "date": datetime.now().isoformat(),
                "text": text_to_save,  # ¡Guardamos el texto plano en el payload!
            },
            vector=Document(
                text=text_to_save, model="sentence-transformers/all-minilm-l6-v2"
            ),
        )
    ]

    # Upsert: Inserta si no existe, o actualiza si el ID ya está registrado
    qdrant_client.upsert(collection_name=COLLECTION_NAME, points=points)
    print(f"\n[✔] Punto guardado/actualizado con ID determinista: {point_id}")
    fn_get_one_collection()


def fn_execute_query(q: str):
    print(f"\nBuscando similitud para: '{q}'...")
    response = qdrant_client.query_points(
        collection_name=COLLECTION_NAME,
        query=Document(text=q, model="sentence-transformers/all-minilm-l6-v2"),
    )

    if not response.points:
        print("\n[❌] No se han encontrado vectores o la colección está vacía.")
        return

    print(f"\n--- Resultados encontrados ({len(response.points)}) ---")
    for scored_point in response.points:
        print(f"ID del punto: {scored_point.id}")
        print(f"Score de similitud (Cosine): {scored_point.score:.4f}")

        # Validación segura por si el payload viene vacío o None
        if scored_point.payload:
            topic = scored_point.payload.get("topic", "Sin tema")
            text = scored_point.payload.get("text", "Sin texto")
            print(f"Tema: {topic}")
            print(f"Texto recuperado: {text}")
        else:
            print("Payload: (Vacío / None)")

        print("-" * 60)


def fn_delete_collection():
    if qdrant_client.collection_exists(collection_name=COLLECTION_NAME):
        qdrant_client.delete_collection(collection_name=COLLECTION_NAME)
        print("\n[✔] Colección borrada exitosamente.")
    else:
        print("\n[ℹ] La colección no existe, no hay nada que borrar.")


if __name__ == "__main__":
    while True:
        print("\n==============================")
        print("     MENÚ QDRANT - RAG     ")
        print("==============================\n")
        print("1. Listar todas las colecciones")
        print("2. Crear colección")
        print("3. Crear / Actualizar punto (con texto)")
        print("4. Ejecutar consulta semántica")
        print("5. Borrar colección")
        print("6. Consultar detalles de la colección")
        print("Presiona Enter para salir.")

        option = input("\nElija una opción: ").strip()

        if not option:
            print("Saliendo del programa. ¡Hasta luego!")
            break

        match option:
            case "1":
                fn_get_collections()
            case "2":
                fn_create_collection()
            case "3":
                fn_create_point()
            case "4":
                query_text = input(
                    "Ingrese su pregunta (o presione Enter para usar la consulta por defecto): "
                ).strip()
                if not query_text:
                    query_text = (
                        "Biological process that sustains aerobic life on Earth."
                    )
                fn_execute_query(query_text)
            case "5":
                fn_delete_collection()
            case "6":
                fn_get_one_collection()
            case _:
                print("\n[⚠️] Opción no válida. Intente de nuevo.")


"""
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct, PayloadSchemaType

client = QdrantClient(url="http://localhost:6333")

client.create_collection(
    collection_name="politicas_internas",
    vectors_config=VectorParams(size=384, distance=Distance.COSINE),  # dimensión de MiniLM
)
client.create_payload_index("politicas_internas", "source", PayloadSchemaType.KEYWORD)
client.create_payload_index("politicas_internas", "articulo", PayloadSchemaType.KEYWORD)

point = PointStruct(
    id=uuid_from_content_hash,          # determinista -> idempotente
    vector=embedding,                   # lista de floats, dimensión 384
    payload={
        "text": chunk_text,             # imprescindible: el vector no es reversible
        "source": "politica_vacaciones_v3.pdf",
        "articulo": "7.2",
        "seccion": "Vacaciones y ausencias",
        "chunk_index": 14,
        "doc_id": "pol-vac-2026",
        "fecha_vigencia": "2026-01-01",
        "fecha_epoch": 1767225600,      # para filtros de rango
        "idioma": "es",
    },
)
"""


"""Sobre grandes volumenes de datos para ser procesados(ingesta)"""
"""
Sobre la herramienta, con X desconocido: Redis + RQ, con N workers configurables. La razón es que puedes escalar añadiendo procesos consumidores sin tocar el código, y ves la profundidad de la cola para saber si necesitas más. Redis aguanta bien miles de jobs al día; el cuello de botella real va a ser la CPU de los embeddings, no el broker.

Un cálculo que te conviene hacer antes de elegir: cuánto tarda un documento medio en pasar por el pipeline completo. Si son 15 segundos y llegan 100 al día, un solo worker va sobrado. Si llegan 100 en una hora punta, necesitas concurrencia. Ese número —documentos por hora en el pico, no por día— es el que dimensiona.

Y la contrapartida que no se puede ignorar: con X variable y workers concurrentes, dos procesos pueden intentar escribir sobre el mismo doc_id a la vez. Si un cliente reenvía un documento mientras el primero aún se está indexando, acabas con chunks mezclados de dos versiones. Se resuelve con un lock por doc_id (Redis SET NX con TTL) o con una restricción de unicidad en la tabla de jobs que impida dos jobs activos para el mismo documento.

Un último punto de arquitectura: si el volumen puede crecer de forma imprevisible, el almacenamiento de los ficheros originales va aparte (S3 o disco compartido), no en el contenedor del worker. Los workers deben ser efímeros y reemplazables; si el PDF vive en su disco local, no puedes escalar horizontalmente y pierdes el original al reiniciar.
"""

"""
Si necesitamos una decisión como paso previa a la llamada real
router = ChatOpenAI(model="modelo-ligero", temperature=0).with_structured_output(
    Literal["simple", "complejo"]
)
tipo = router.invoke(f"Clasifica esta consulta: {query}")

por ejemplo, necesita saber si a consulta que hizo una enfermera es de baja, media o alta complejidad y la salida de esta primero consulta decidira que modelo ejecutara la consulta principal
"""
