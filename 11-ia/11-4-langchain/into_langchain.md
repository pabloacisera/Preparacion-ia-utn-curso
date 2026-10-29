### Langchain Integration

```Markdown
Python Code
     |
     v
run_agent("question for model")
     |
     v
result = agent.invoke({
    "messages": [("user": question)]
})
    |
    v
request to LLM api
```

### Langchain Calls

LangChain envia tanto el mensaje como las tools disponibles, es decir todas aquellas funciones que tienen el decorador `@tool`. Gracias a este ultimo se crea un schema:

```Schema
{
    "messages": [
        {
            "role": "user",
            "content": "all the content"
        },
    ],
    "tools": [
        {
            "type": "function",
            "function: {
                "name": "add",
                "description": "add two numbers...",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "a":  { "type": "number" },
                        "b":  { "type": "number" }
                    }
                }
            }
        },
        ...
    ]
}
```

### Model returns calls

La respuesta del modelo siempre es con `"role":assistant`, y la decisión que tiene es si va a utilizar alguna de las herramientas que tiene a disposición. Esto se llama "Llamada a herramienta estructurada", por ejemplo decide que necesita multiplar o sumar los valores, y para ello tiene que utilizar la función "add", y le pide al agente que invoque esa función y le devuelva el resultado.

Para poder hacer el agente(o en este caso langchain) extrae de la llamada del LLM, el tool_calls, que es la herramienta que se debe ejcutar, tools_args que son los argumentos que hay que pasarle a las funciones , y el id, que es el identificador de la llamada, servira para cuando tenga una respuesta y deba devolverla a la api, debemos decirle que herramienta dio la respuesta.

De todo lo anterior, se agrega a la respuesta al LLM para su posterior razonamiento, todo entra en el schema, es como si al bloque anterior se le agregar la respuesta de la funcion, y se indicar que id de tool ejecuta la llamada. Esto es asi porque no hay memoria de conversación, aun, entonces en cada bucle de razonamiento-peticion-respuesta-razonamiento, se debe enviar todo lo que se hizo.

Luego de lo anterior, cuando el LLM vuelva a recibir la respuesta a llamada estructurada, decidirá si ya tiene la información necesaria para responder la pregunta original, o si debe volver a iterar sobre el proceso anterior, llamando a otras herrmientas, o mcp, o si pregunta o pide aclaración.

