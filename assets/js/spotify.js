async function loadSpotify() {
  const el = document.getElementById("spotify-now");
  if (!el) return;

  const safe = (s) => (s ?? "").toString().replace(/[&<>"']/g, (c) => ({
    "&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"
  }[c]));

  try {
    const res = await fetch("/assets/data/spotify.json", { cache: "no-store" });
    const data = await res.json();

    if (!data || !data.title) {
      el.innerHTML = `
        <div class="spotify-card">
          <div class="spotify-meta">
            <div class="spotify-status">🎧 Spotify</div>
            <div class="spotify-title">Nothing playing right now</div>
            <div class="spotify-sub">Try again in a bit.</div>
          </div>
        </div>
      `;
      return;
    }

    const status = data.is_playing ? "Listening now" : "Recently played";
    const title = safe(data.title);
    const artist = safe(data.artist);
    const album = safe(data.album);
    const url = data.track_url || "#";
    const image = data.image || "";

    el.innerHTML = `
      <a class="spotify-card" href="${url}" target="_blank" rel="noopener">
        <div class="spotify-art">
          ${image ? `<img src="${image}" alt="Album art for ${title}">` : `<div class="spotify-art-fallback"></div>`}
        </div>
        <div class="spotify-meta">
          <div class="spotify-status">${data.is_playing ? "🟢 " : "🕓 "}${status}</div>
          <div class="spotify-title">${title}</div>
          <div class="spotify-sub">${artist}${album ? ` — ${album}` : ""}</div>
          <div class="spotify-cta">Open in Spotify →</div>
        </div>
      </a>
    `;
  } catch (e) {
    el.innerHTML = `
      <div class="spotify-card">
        <div class="spotify-meta">
          <div class="spotify-status">🎧 Spotify</div>
          <div class="spotify-title">Widget failed to load</div>
          <div class="spotify-sub">Check spotify.json or try refresh.</div>
        </div>
      </div>
    `;
  }
}

loadSpotify();
