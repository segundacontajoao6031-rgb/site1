# Origem das fotos dos produtos

Levantamento feito em 14/10/2026 via navegador real a partir dos links de afiliado.
A página de cada anúncio (`shop.tiktok.com/br/pdp/...`) exibe apenas **“Security Check” (captcha)**
para acesso automatizado, então a galeria completa não é acessível sem login manual.
O que foi acessível: a **foto de capa oficial** embutida nos parâmetros `og_info`
da URL de compartilhamento (título + imagem do próprio anúncio).

Como usar: `baixar_fotos.py` baixa novamente as 12 capas para
`public/images/products/<slug>/cover.jpg`.

| Produto | Título no anúncio | Imagem original (capa oficial) | Arquivo local | Formato/dim. | Validada |
|---|---|---|---|---|---|
| body-splash-ayra | Body Splash Árabe Ayra 100ml by Primacial - Perfume Floral Gourmand | `https://p16-oec-sg.ibyteimg.com/.../031440efc76d4396971d4f85b5d4ba76~tplv-aphluv4xwc-resize-jpeg:800:800.jpeg?dr=15584&t=555f072d&ps=933b5bde&shp=2408c917&shcp=32ce9e9e&idc=my2&from=604555543` | `public/images/products/body-splash-ayra/cover.jpg` | JPEG 800x800 | sim, confere frasco Primacial Ayra |
| vestido-suplex | Vestido Feminino De Alcinha Liso Suplex | `https://p16-oec-sg.ibyteimg.com/.../733dbf7bcc6e4ab196bd8bf38fbb48b0~tplv-aphluv4xwc-resize-jpeg:800:800.jpeg?...` (mesmos parâmetros) | `public/images/products/vestido-suplex/cover.jpg` | JPEG 800x800 | sim, vestido alcinha em modelo |
| perfume-attrative | Perfume Feminino Attrative 20ml \| Aroma Doce Floral Frutado para Ocasiões Especiais | `https://p16-oec-sg.ibyteimg.com/.../6a266919572044bc85f1d3bce2e4c20a~tplv-aphluv4xwc-resize-jpeg:800:800.jpeg?...` | `public/images/products/perfume-attrative/cover.jpg` | JPEG 800x800 | sim, frasco coração 20ML |
| hidrabene-fps70 | Hidrabene Protetor solar facial fps 70 Uniformizador | `https://p16-oec-sg.ibyteimg.com/.../7ebce5ad4d614c519a4e64d0529a9a2a~tplv-aphluv4xwc-resize-jpeg:800:800.jpeg?...` | `public/images/products/hidrabene-fps70/cover.jpg` | JPEG 600x800 | sim |
| cinta-modeladora | Cinta Modeladora Feminina Redutora Abdominal/Afina a Cintura/Fitness | `https://p16-oec-va.ibyteimg.com/.../a734cfcd190449f4bfc45773f19bae64~tplv-o3syd03w52-resize-jpeg:800:800.jpeg?...` | `public/images/products/cinta-modeladora/cover.jpg` | JPEG 800x800 | sim, cinta preta de colchetes |
| depilador-sobrancelha | Depilador Indolor Caneta Sobrancelha Removedor Instantâneo A Pilha(lolibiju) | `https://p16-oec-va.ibyteimg.com/.../f5f40438e72143ba9348287a12c7a4c6~tplv-o3syd03w52-resize-jpeg:800:800.jpeg?...` | `public/images/products/depilador-sobrancelha/cover.jpg` | JPEG 739x739 | sim |
| sutias-canelados | Kit Até 5 Sutiã Canelado Confort Com Bojo e Alça de Regulagem Cores Neutras | `https://p16-oec-sg.ibyteimg.com/.../a5fb3ed197014be4b04bf20f540a2682~tplv-aphluv4xwc-resize-jpeg:800:800.jpeg?...` | `public/images/products/sutias-canelados/cover.jpg` | JPEG 600x800 | sim |
| calcinhas-mirela | Kit 5 Calcinhas Mirela Algodão Cintura Reforçada Alta Compressão em Vários Cores para Mulheres | `https://p16-oec-sg.ibyteimg.com/.../71e3683106194041a6a247e24b514000~tplv-aphluv4xwc-resize-jpeg:800:800.jpeg?...` | `public/images/products/calcinhas-mirela/cover.jpg` | JPEG 800x800 | sim |
| jogo-toalhas | Jogo Toalha de Banho Super Luxo 4Pçs ... | `https://p16-oec-va.ibyteimg.com/.../de8b169255ff40e4bb27fb2cda5dccc2~tplv-o3syd03w52-resize-jpeg:800:800.jpeg?...` | `public/images/products/jogo-toalhas/cover.jpg` | JPEG 800x800 | sim, 4 toalhas empilhadas |
| blusa-gola-boba | Blusa Feminina Gola Boba Suplex Casual Versatil Social Drapeada Forrada Elegante Moda Tendencia | `https://p16-oec-sg.ibyteimg.com/.../37c92749f79e45fdb337fee5f5ce08e5~tplv-aphluv4xwc-resize-jpeg:800:800.jpeg?...` | `public/images/products/blusa-gola-boba/cover.jpg` | JPEG 800x800 | sim |
| bolsas-baguete | Kit 2 Bolsas Femininas Baguetes Lisas Pequenas Correntes de Ombro e de Mão | `https://p16-oec-sg.ibyteimg.com/.../2e7de48ba0884ff4ab371495d91c7233~tplv-aphluv4xwc-resize-jpeg:800:800.jpeg?...` | `public/images/products/bolsas-baguete/cover.jpg` | JPEG 800x800 | sim |
| baby-doll | Conjunto Baby Doll Feminino Canelado de Coração - Tamanho do 36 ao 44 | `https://p16-oec-va.ibyteimg.com/.../8b14b694f4f24877bf7c98e9b3385632~tplv-o3syd03w52-resize-jpeg:800:800.jpeg?...` | `public/images/products/baby-doll/cover.jpg` | JPEG 800x800 | sim, conjunto branco de corações |
| skincare-dermachem | — (link resolve direto p/ `shop.tiktok.com/br/pdp/1734238399161796437` sem `og_info`) | nenhuma acessível | — | — | **bloqueada**: sem capa nos metadados + página com captcha. Abrir o link no celular e salvar a capa manualmente em `public/images/products/skincare-dermachem/` |
| combo-cachos | — (link resolve direto p/ `shop.tiktok.com/br/pdp/1731409904436807166` sem `og_info`) | nenhuma acessível | — | — | **bloqueada**: idem. Salvar manualmente em `public/images/products/combo-cachos/` |

URLs acima abreviadas com `...` — as URLs completas estão em `baixar_fotos.py`
e em `data/product-images.json`. Todas são fotos originais do anúncio
(`original listing`), nenhuma é banco de imagens.

Limitação geral: as demais fotos da galeria (variações, embalagem, detalhes)
exigem sessão logada / captcha resolvido manualmente; nenhum método legítimo
automatizado as expôs. Não foram inventadas URLs nem usadas fotos aproximadas.
