---
layout: default
title: Home
---

<div class="hero">
  <h1>Dawson Hardy</h1>
  <p>Networking, homelab, and the stuff I’m into — with notes I can actually find later.</p>

  <div class="badges">
    <span class="badge"><span class="dot"></span> Network Engineering</span>
    <span class="badge green"><span class="dot"></span> Homelab / Proxmox</span>
    <span class="badge"><span class="dot"></span> UniFi / Fiber / Routing</span>
  </div>
</div>

<div class="grid">

  <div class="card">
    <h3>Blog</h3>
    <p>Writeups on troubleshooting, configs, and lessons learned.</p>
    <div class="btnrow">
      <a class="btn primary" href="./blog">Read posts</a>
      <a class="btn" href="./projects">See projects</a>
    </div>
  </div>

  <div class="card">
    <h3>Links</h3>
    <p>Stuff I’m watching, reading, and listening to.</p>
    <div class="btnrow">
      <a class="btn" href="https://musicboard.app/dawshardy" target="_blank" rel="noopener">Musicboard</a>
      <a class="btn" href="https://open.spotify.com/user/the_wanderlust" target="_blank" rel="noopener">Spotify</a>
      <a class="btn" href="https://letterboxd.com/dawshardy/" target="_blank" rel="noopener">Letterboxd</a>
      <a class="btn" href="https://www.goodreads.com/user/show/24054980-dawson-hardy" target="_blank" rel="noopener">Goodreads</a>
      <a class="btn" href="https://www.linkedin.com/in/dawson-hardy-87aa9a13b/" target="_blank" rel="noopener">LinkedIn</a>
      <a class="btn" href="./links">All links</a>
    </div>
  </div>

</div>

<hr>

## Latest posts
{% for post in site.posts limit: 5 %}
- [{{ post.title }}]({{ post.url }}) <span class="post-meta">— {{ post.date | date: "%b %d, %Y" }}</span>
{% endfor %}

<hr>

## What I’m building
- 20G UniFi network testing (repeatable test method + bottlenecks)
- Proxmox homelab stack (DNS, monitoring, logging, backups)
- Clean SMB VLAN + firewall templates that stay maintainable
