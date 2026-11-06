# Conteúdo dos 6 carrosséis storytelling do lote 02 (2026-11-05)
# Uso: STORY_DATA=story_data_lote02 python3 render_story.py <pasta_saida> [id_do_post]
REV = {
 "GCS": dict(ini="G.C.S.", date="30/09/2026", local="C.O.T. - Centro Ortopédico e Traumatológico", text="Excelente atendimento e estrutura perfeita. Médico e equipe estão de parabéns!"),
 "A": dict(ini="A.", date="22/09/2026", local="CIDOR · Consulta especialista em dor", text="Secretaria atenciosa, médico atencioso me explicou tudo certinho passou exames para eu retornar"),
 "P": dict(ini="P.", date="09/09/2026", local="CIDOR · Consulta especialista em dor", text="Excelente profissional, dedicado e atencioso. Super recomendo"),
 "VS": dict(ini="V.S.", date="09/09/2026", local="C.O.T. - Centro Ortopédico e Traumatológico", text="Dr. Bernardo é muito envolvido para gerar a solução do paciente e muito sincero na avaliação. Ótimo profissional!"),
 "AC": dict(ini="A.C.", date="12/08/2026", local="C.O.T. · Infiltração do joelho", text="Médico maravilhoso, paciente e muito educado. Ótimo profissional"),
 "LCF": dict(ini="L.C.F.", date="01/09/2026", local="CIDOR · Consulta especialista em dor", text="Profissional muito competente e atencioso. Não atrasa o horário. Excelente médico!"),
}
POSTS = [
 dict(id="ST07_joelho_incha_caminhada", tema="JOELHO", photo="bernardo_24_jaleco_mesa_sorrindo.jpg", pos="40% 25%",
  slides=[
   dict(t="cover", pre="Seu joelho ", hi="incha depois da caminhada?", sub="Isso pode ser um alerta."),
   dict(t="card", pre="Inchaço que aparece depois de caminhar, treinar ou ficar muito tempo em pé", hi="é o joelho avisando que algo não vai bem."),
   dict(t="card", pre="Ele pode indicar", hi="inflamação, desgaste da cartilagem ou lesão no menisco."),
   dict(t="card", pre="A boa notícia é que, com exame físico e ultrassom no consultório,", hi="dá para entender a causa e tratar cedo.", post="Em muitos casos, sem cirurgia."),
   dict(t="review", r="GCS"),
   dict(t="cta", q="Seu joelho incha depois do esforço?", hi='Comente "JOELHO"', post=" e veja como eu posso te ajudar."),
  ],
  caption="""Joelho inchado depois da caminhada não é só cansaço.

O inchaço é um sinal de que a articulação está sofrendo, seja por inflamação, desgaste ou lesão no menisco. Descobrir a causa cedo abre mais opções de tratamento.

👉 Comente "JOELHO" e veja como eu posso te ajudar."""),
 dict(id="ST08_coluna_ciatico_5_problemas", tema="COLUNA", photo="bernardo_41_jaleco_recepcao_cidor.jpg", pos="20% 30%",
  slides=[
   dict(t="cover", pre="Só quem tem ", hi="dor ciática", post=" vai entender esses 5 problemas aqui"),
   dict(t="item", title="Choque na perna:", body="A dor sai da lombar ou da nádega e desce pela perna como um choque."),
   dict(t="item", title="Não aguentar ficar sentado:", body="Reunião, trânsito ou cinema viram um teste de resistência."),
   dict(t="item", title="Perna dormente:", body="Formigamento ou dormência na perna ou no pé que vai e volta."),
   dict(t="item", title="Andar torto:", body="Você muda o jeito de andar para fugir da dor, e outras partes começam a doer."),
   dict(t="item", title="Medo de piorar:", body="Cada movimento vira uma dúvida: \"será que isso vai travar de novo?\""),
   dict(t="review", r="A"),
   dict(t="cta", q="Você se identificou com algum desses?", hi='Comente "COLUNA"', post=" e eu te mostro os caminhos de tratamento."),
  ],
  caption="""Dor ciática não é só uma dor na perna.

Ela muda o jeito de sentar, de andar e até de dormir. Na maioria das vezes ela vem de um nervo irritado na coluna, e existem tratamentos que podem aliviar a dor sem cirurgia.

Qual desses você mais sente?

👉 Comente "COLUNA" e eu te mostro os caminhos de tratamento."""),
 dict(id="ST09_joelho_historia_ricardo", tema="JOELHO", photo="bernardo_36_jaleco_ultrassom.jpg", pos="22% 25%",
  slides=[
   dict(t="cover", pre="Ricardo achava que o joelho travado era só uma pancada do futebol... ", hi="até que não conseguiu mais esticar a perna."),
   dict(t="card", hi="Jogou mais três finais de semana com dor.", post="Gelo, pomada e \"semana que vem passa\"..."),
   dict(t="card", pre="Até que", hi="o joelho travou no meio do jogo", post="e ele saiu de campo mancando."),
   dict(t="card", pre="Com exame físico, ultrassom no consultório e ressonância,", hi="identificamos uma lesão no menisco."),
   dict(t="card", pre="Tratamos com o procedimento indicado para o caso dele e reabilitação,", hi="e ele voltou ao futebol com segurança.", foot="Caso ilustrativo. Os resultados variam de pessoa para pessoa."),
   dict(t="card", pre="Hoje ele sabe:", hi="joelho que trava não é pancada. É sinal para avaliar."),
   dict(t="review", r="P"),
   dict(t="cta", q="Seu joelho já travou depois do futebol?", hi='Comente "JOELHO"', post=" que eu posso te ajudar."),
  ],
  caption="""Joelho que trava não é "só uma pancada".

Travamento, dor para esticar a perna e sensação de falseio podem indicar lesão no menisco. Quanto antes vem o diagnóstico, mais opções de tratamento existem e mais seguro é o retorno ao esporte.

👉 Comente "JOELHO" que eu posso te ajudar.

*Caso ilustrativo. Os resultados variam de pessoa para pessoa."""),
 dict(id="ST10_coluna_endoscopia_5_duvidas", tema="COLUNA", photo="bernardo_61_terno_mesa_modelos.jpg", pos="66% 30%",
  slides=[
   dict(t="cover", pre="Cirurgia de coluna por endoscopia: ", hi="5 dúvidas que todo mundo tem"),
   dict(t="item", title="O que é?", body="Uma cirurgia feita por um corte de poucos milímetros, com uma câmera que mostra a coluna por dentro."),
   dict(t="item", title="Para quem serve?", body="Para casos selecionados, como algumas hérnias de disco e estreitamentos do canal, quando o tratamento sem cirurgia não bastou."),
   dict(t="item", title="Precisa de anestesia geral?", body="Em muitos casos, não. Pode ser feita com sedação e anestesia local, conforme a avaliação."),
   dict(t="item", title="A recuperação é mais rápida?", body="Por ser menos invasiva, a alta costuma ser rápida. O tempo de volta à rotina depende de cada caso."),
   dict(t="item", title="Todo mundo pode fazer?", body="Não. A indicação vem do exame físico e dos exames de imagem. Cada coluna tem a sua resposta."),
   dict(t="review", r="VS"),
   dict(t="cta", q="Ficou com alguma dúvida sobre a sua coluna?", hi='Comente "COLUNA"', post=" e eu te explico as opções para o seu caso."),
  ],
  caption="""Cirurgia de coluna não precisa significar corte grande e meses de recuperação.

A endoscopia de coluna usa um corte de poucos milímetros e uma câmera para tratar casos selecionados, como algumas hérnias de disco. Mas ela não é para todo mundo: a indicação vem de uma avaliação cuidadosa, e muitos casos melhoram sem cirurgia nenhuma.

👉 Comente "COLUNA" e eu te explico as opções para o seu caso."""),
 dict(id="ST11_joelho_prp", tema="JOELHO", photo="bernardo_28_jaleco_mesa_modelos.jpg", pos="64% 30%",
  slides=[
   dict(t="cover", pre="Tratar o joelho ", hi="com o próprio sangue?", sub="Existe, e tem nome: PRP."),
   dict(t="card", pre="O PRP (plasma rico em plaquetas) é preparado a partir de uma pequena amostra do seu sangue", hi="e aplicado no joelho de forma guiada."),
   dict(t="card", pre="Ele pode ser indicado em alguns casos de", hi="artrose no joelho, tendinites e lesões do esporte."),
   dict(t="card", pre="Não é para todo mundo e não faz milagre.", hi="A indicação depende da avaliação e faz parte de um plano com fortalecimento."),
   dict(t="review", r="AC"),
   dict(t="cta", q="Quer saber se o PRP serve para o seu joelho?", hi='Comente "JOELHO"', post=" e veja como eu posso te ajudar."),
  ],
  caption="""Você já ouviu falar em tratar o joelho com o próprio sangue?

O PRP (plasma rico em plaquetas) é um dos chamados ortobiológicos e pode ser indicado em alguns casos de artrose, tendinite e lesões do esporte. Ele não substitui avaliação nem fortalecimento, e a indicação é sempre individual.

👉 Comente "JOELHO" e veja como eu posso te ajudar."""),
 dict(id="ST12_coluna_historia_sandra", tema="COLUNA", photo="bernardo_52_terno_fundo_neutro.jpg", pos="40% 25%",
  slides=[
   dict(t="cover", pre="Sandra achava que a dor nas costas era o preço de trabalhar e cuidar da casa... ", hi="até que não conseguia mais levantar da cama sem ajuda."),
   dict(t="card", hi="Conviveu com a dor por anos.", post="Analgésico, bolsa quente e \"não tenho tempo para médico\"..."),
   dict(t="card", pre="Até que", hi="levantar de manhã virou a pior parte do dia", post="e ela começou a faltar no trabalho."),
   dict(t="card", pre="Com exame físico e exames de imagem,", hi="identificamos desgaste nas pequenas articulações da coluna."),
   dict(t="card", pre="Tratamos com bloqueio guiado por imagem e reabilitação,", hi="e ela voltou à rotina com muito menos dor.", foot="Caso ilustrativo. Os resultados variam de pessoa para pessoa."),
   dict(t="card", pre="Hoje ela sabe:", hi="cuidar da coluna também é cuidar de quem depende dela."),
   dict(t="review", r="LCF"),
   dict(t="cta", q="Você também deixa sua dor nas costas para depois?", hi='Comente "COLUNA"', post=" que eu posso te ajudar."),
  ],
  caption="""Dor nas costas não precisa ser o preço da rotina.

Mulheres sofrem mais com dor crônica na coluna e, muitas vezes, são as que mais adiam o cuidado. Com o diagnóstico certo, existem tratamentos minimamente invasivos que podem aliviar a dor e devolver a rotina.

👉 Comente "COLUNA" que eu posso te ajudar.

*Caso ilustrativo. Os resultados variam de pessoa para pessoa."""),
]
