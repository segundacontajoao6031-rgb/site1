# Variados do Dia a Dia — vitrine de afiliada TikTok Shop

Vitrine estática da `@variadosdiaadiadobr` com 14 produtos e fotos oficiais de capa.
Sem build, sem dependências: abra `index.html` ou publique a pasta `site/` na Vercel.

## Arquivos
- `index.html` — catálogo completo (14 produtos, botão **Compre Agora** por produto)
- `styles.css` — visual rosa minimalista, responsivo, com foco visível e `prefers-reduced-motion`
- `public/images/products/<slug>/cover.jpg` — 12 capas oficiais baixadas do anúncio
- `baixar_fotos.py` — baixa novamente as 12 capas (URLs de origem no próprio script)
- `docs/product-image-sources.md` — inventário com origem, dimensões e validação de cada foto
- `data/product-images.json` — mesmo inventário em formato legível por máquina
- `vercel.json` — config mínima da Vercel (site estático)

## Fotos
12 de 14 capas obtidas via metadados oficiais de compartilhamento do anúncio e
validadas (JPEG decodificável, dimensões conferidas, conferência visual por amostragem).
2 produtos (`skincare-dermachem`, `combo-cachos`) exibem “Foto em breve”: os links
resolvem direto sem metadados e a página do anúncio exige captcha/login — ver
`docs/product-image-sources.md`. Para completá-los, abra o link no celular e salve
a capa em `public/images/products/<slug>/cover.jpg`, depois troque o bloco
`.semfoto` por `<img>` seguindo o padrão dos demais cards.

## Publicar
```powershell
cd site
git init -b main
git add .
git commit -m "Complete product catalog and polish affiliate storefront"
git remote add origin https://github.com/segundacontajoao6031-rgb/site1.git
git push -u origin main
```
Vercel: importe o repositório (diretório-raiz `site/`) ou `vercel --prod` dentro de `site/`.
