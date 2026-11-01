---
name: hackernews
description: Busca lo que está sonando en Hacker News. Úsala cuando pida noticias de tech, qué hay en HN o temas para un video.
---

Busca las historias de portada en `https://hn.algolia.com/api/v1/search?tags=front_page` con curl.
Si te doy un tema, usa `https://hn.algolia.com/api/v1/search?query=<tema>&tags=story`.

Dame las 5 más interesantes: título, puntos y link. Una línea por noticia, en español, sin relleno.
