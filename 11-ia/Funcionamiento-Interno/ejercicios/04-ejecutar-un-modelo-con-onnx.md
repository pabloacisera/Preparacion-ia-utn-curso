# Ejercicio 04 — Ejecutar un modelo con ONNX Runtime

**Objetivo:** entender la separación entre el **archivo del modelo** (ONNX) y el **motor que lo ejecuta** (ONNX Runtime). Vamos a construir un modelo diminuto y correrlo.

## Requisitos

```bash
pip install onnx onnxruntime numpy
```

## Código

```python
import numpy as np
import onnx
import onnxruntime as ort
from onnx import TensorProto, helper, numpy_helper

# 1) Construimos un "modelo" mínimo: una tabla de embeddings (V x D)
#    y una sola operación, Gather = "buscar la fila de cada ID".
V, D = 5, 3
tabla = np.arange(V * D, dtype=np.float32).reshape(V, D)

entrada = helper.make_tensor_value_info("input_ids", TensorProto.INT64, ["tokens"])
salida = helper.make_tensor_value_info("vectores", TensorProto.FLOAT, ["tokens", D])
nodo = helper.make_node("Gather", ["tabla", "input_ids"], ["vectores"], axis=0)
grafo = helper.make_graph([nodo], "mini_modelo", [entrada], [salida],
                          initializer=[numpy_helper.from_array(tabla, "tabla")])
modelo = helper.make_model(grafo, opset_imports=[helper.make_opsetid("", 17)])
modelo.ir_version = 9
onnx.checker.check_model(modelo)
onnx.save(modelo, "mini_modelo.onnx")
print("Modelo guardado: mini_modelo.onnx")

# 2) Lo ejecutamos con ONNX Runtime (el motor)
sesion = ort.InferenceSession("mini_modelo.onnx", providers=["CPUExecutionProvider"])
ids = np.array([0, 2, 4], dtype=np.int64)
vectores = sesion.run(None, {"input_ids": ids})[0]
print("IDs:", ids)
print("Vectores:\n", vectores)
```

## Qué deberías observar

- El archivo `.onnx` es **un solo modelo** que cualquiera puede ejecutar, sin Python ni frameworks pesados.
- La operación `Gather` busca la fila de cada ID: es la idea de "tabla de embeddings" que usan los modelos reales.
- El **motor** (ONNX Runtime) no entrena nada: solo ejecuta.

## Experimentos

1. Cambiá los IDs de entrada por `[1, 1, 3]` y verificá que devuelve las filas correspondientes.
2. Mirá el tamaño del archivo: `du -h mini_modelo.onnx`. ¿Por qué un modelo real ocupa muchísimo más?
3. Averiguá qué *execution providers* ofrece tu instalación: `print(ort.get_available_providers())`.

[Volver al módulo](../readme.md)
