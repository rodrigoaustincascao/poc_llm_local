# POCs sobre LLM

Os testes consistem em executar os LLMs localmente utilizando ferramentas open-sources. Os primeiros testes foram executados utilizando o ChatGPT, caso queira testá-los é necessário gerar a chave no site da [OpenAI](https://platform.openai.com/login?launch).

Caso não possua uma placa NVIDIA é necessário comentar esse trecho no `./docker/docker-compose.yaml`
```
  # deploy:
    #   resources:
    #     reservations:
    #       devices:
    #         - driver: nvidia
    #           count: 1
    #           capabilities: [gpu]
```

## Tecnologias utilizadas nas POCs
- [Docker](https://www.docker.com/)
- [DevContainer](https://code.visualstudio.com/docs/devcontainers/containers)
- [Ollama](https://ollama.com/)
- [Langchain](https://www.langchain.com/)
- [Unstructured](https://unstructured.io/)
- [PandasAI](https://pandas-ai.com/)
- [Gradio](https://www.gradio.app/)
- [Streamlit](https://streamlit.io/)
- [Flask](https://flask.palletsprojects.com)


## Execução

### Requisitos
- Docker
- Docker Compose
- VSCode
- Extensões do VSCode:
    - DevContainer => `ms-vscode-remote.remote-containers`
    - Docker => `ms-azuretools.vscode-docker`

### Execução
Abrir o projeto no VSCode e selecionar a opção `Open a Remote Window`     