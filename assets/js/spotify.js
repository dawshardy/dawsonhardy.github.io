async function loadSpotify() {
  const el = document.getElementById("spotify-now");
  if (!el) return;

  try {
    const res = await fetch("/assets/data/spotify.json", { cache: "no-store" });
    const data = await res.json();

    if (!data || !data.title) {
      el.innerHTML = `<span style="opacity:.75">Nothing playing right now.</span>`;
      return;
    }

    const status = data.is_playing ? "Listening now" : "Recently played";
    const img = data.image
      ? `<img src="${data.image}" alt="" style="width:56px;height:56px;border-radius:12px;border:1px solid rgba(255,255,255,.12);object-fit:cover;margin-right:12px;">`
      : "";

    const inner = `
      <div style="display:flex;align-items:center;">
        ${img}
        <div>
          <div style="font-weight:900;">${status}: ${data.title}</div>
          <div style="opacity:.75;">${data.artist}${data.album ? " — " + data.album : ""}</div>
        </div>
      </div>
    `;

    el.innerHTML = data.track_url
      ? `<a href="${data.track_url}" target="_blank" rel="noopener" style="text-decoration:none;color:inherit;">${inner}</a>`
      : inner;

  } catch (e) {
    el.innerHTML = `<span style="opacity:.75">Spotify widget failed to load.</span>`;
  }
}
loadSpotify();
