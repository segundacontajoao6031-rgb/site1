# Variados do Dia a Dia

Vitrine estática de afiliados do TikTok Shop, responsiva para computador e celular.

## Projeto
- `index.html`: catálogo com 14 produtos e links para os anúncios.
- `styles.css`: tema editorial moderno, efeito 3D em CSS e grade responsiva (4 colunas no desktop, 3 em telas intermediárias e 2 no celular).
- `public/images/products/<slug>/cover.jpg`: 12 capas locais.
- Os dois anúncios sem capa local usam as imagens oficiais do CDN do TikTok Shop, documentadas em `docs/product-image-sources.md` e `data/product-images.json`.
- `vercel.json`: configuração estática, sem dependências nem etapa de build.

## Links e imagens
Os links dos cartões são links curtos de afiliada `vt.tiktok.com` que levam ao TikTok Shop. Eles abrem os produtos correspondentes; preços, estoque, variações e comissão podem mudar e precisam ser conferidos na conta de afiliada antes da divulgação.

## Publicação
O repositório é estático: na Vercel, use a raiz do repositório como diretório-raiz, sem framework, sem comando de build e sem diretório de saída personalizado. O domínio de produção é https://variadosdodiaadia.vercel.app/.

