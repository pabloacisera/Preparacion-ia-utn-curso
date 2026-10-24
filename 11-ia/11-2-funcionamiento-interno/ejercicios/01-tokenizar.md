# Ejercicio 01 — Tokenizar texto

**Objetivo:** ver con código cómo se corta un texto en tokens, cómo se ven los IDs y por qué un idioma cuesta más tokens que otro.

## Requisitos

```bash
pip install tokenizers
```

## Código

```python
from tokenizers import Tokenizer, models, pre_tokenizers, decoders, trainers

FRASES = [
    "el gato come pescado.",
    "el delfín nada.",
    "el niño juega en el jardín.",
    "la casa es grande.",
]

tok = Tokenizer(models.BPE(unk_token="<unk>"))
tok.pre_tokenizer = pre_tokenizers.ByteLevel(add_prefix_space=False)
tok.decoder = decoders.ByteLevel()
tok.train_from_iterator(
    FRASES,
    trainers.BpeTrainer(vocab_size=330, special_tokens=["<unk>", "<pad>", "<fin>"],
                        initial_alphabet=pre_tokenizers.ByteLevel.alphabet()),
)

for frase in ["el gato come pescado.", "el delfín nada."]:
    enc = tok.encode(frase)
    print(f"Frase : {frase!r}")
    print("Piezas:", enc.tokens)
    print("IDs   :", enc.ids)
    print("Vuelta:", repr(tok.decode(enc.ids)), "\n")
```

## Qué deberías observar

- Cada palabra frecuente tiende a ser una pieza; las palabras con acentos se parten en partes más chicas.
- La **marca `Ġ`** delante de una pieza significa "acá había un espacio".
- La frase se puede reconstruir (`decode`): el tokenizador no pierde información.

## Experimentos

1. Cambiá `vocab_size` a 280 y a 600. ¿Cuántas piezas por frase salen?
2. Agregá frases en inglés y compará cuántos tokens usan frente al mismo contenido en español.
3. Tokenizá una URL y un número largo. ¿Cómo se parten?

[Volver al módulo](../readme.md)
