# Publicação automática — Dr. Bernardo (@drbernardomercante)

Agenda: **terça e quinta, 18h (horário de Brasília)**, um carrossel por vez, na ordem de `fila.json`.

- `publicar.py status` mostra o que já foi e o que falta. `publicar.py publicar` publica o próximo.
- Conta: Instagram business id `17841401873564284`. O token acessa outras contas de clientes; nunca publicar em outro id.
- A API só aceita JPEG: cada post fica em `posts/<id>/slide_01.jpg...` + `legenda.txt`, e a imagem precisa estar no GitHub antes de publicar.
- Um post conta como publicado quando a 1ª linha da legenda já aparece no perfil. Não repetir a 1ª linha de legenda entre posts.

## Quando faltarem 2 posts

Gerar um lote novo de 12 seguindo os padrões da pasta do projeto (`/mnt/project-files/bernardo/`: `PADRAO_CARROSSEL_HQ.md`, `PADRAO_CARROSSEL_STORYTELLING.md`, `01_briefing.md`) e as regras da memória do projeto (Método DIC, CTA só JOELHO ou COLUNA, sem numerar slides, avaliação 5★ antes do CTA, HQs diversas, pesquisar temas em alta). Depois:

1. Salvar o lote em `/mnt/project-files/bernardo/posts/lote_NN/`.
2. Converter os slides para JPEG 1080×1350 em `bernardo/posts/<id>/`, com `legenda.txt`.
3. Acrescentar os posts no fim de `fila.json`, alternando formato e tema.
4. Commit e push para o mesmo branch usado na publicação.

## Lotes
- Lote 01: 12 posts (07/10 a 12/11/2026). Ilustrações em `ilustracoes/lote_01`.
- Lote 02: 12 posts, gerado em 05/11/2026 (pesquisa em `/mnt/project-files/bernardo/pesquisa/temas_em_alta_2026-11.md`). Ilustrações em `ilustracoes/lote_02` (design Canva DAHaFek1tFY). Textos em `hq_data_lote02.py` e `story_data_lote02.py`.
- Para montar: `HQ_DATA=hq_data_lote02 python3 render_hq.py <artes> <saida>` e `STORY_DATA=story_data_lote02 python3 render_story.py <saida>` (os scripts ficam em `/mnt/project-files/bernardo/automacao/`).
