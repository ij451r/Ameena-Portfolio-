# Ameena PK portfolio: update guide

Run locally: `python3 -m http.server 8000`, open http://localhost:8000 (fetch() needs a server, not file://).
Deploy: push to GitHub, Settings > Pages > Deploy from branch (main, root).

## Add content
- **Videos:** set `drive` (public "Anyone with the link" Drive URL), `title`, `desc` in `work/videos/videos.json`. Save the poster in `work/videos/posters/` and point `poster` at it. `aspect` is "16 / 9" or "9 / 16".
- **School posters:** put 6 images in `work/school-posters/`.
- **Brand posts:** drop images in `work/brands/<brand>/`. New brand = new folder + one line in `work/brands/brands.json`.
- **Writing:** edit `work/writing/writing.json`. To self-host the image, save it in `work/writing/` and set `image` to that path.
- After adding images run `python3 scripts/build-manifests.py` (or push: the GitHub Action does it). Name files `01-name.jpg` to control order; avoid spaces. Export web-sized images (about 1200px wide, under 300 KB).
