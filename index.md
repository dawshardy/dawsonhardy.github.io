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
      <a class="btn" href="./blog">Read posts</a>
      <a class="btn" href="./projects">See projects</a>
    </div>
  </div>

  <div class="card">
    <h3>Links</h3>
    <p>Stuff I’m watching, reading, and listening to.</p>
    <div class="btnrow">
      <a class="btn" href="https://musicboard.app/dawshardy" target="_blank">Musicboard</a>
      <a class="btn" href="https://letterboxd.com/dawshardy/" target="_blank">Letterboxd</a>
      <a class="btn" href="https://www.goodreads.com/user/show/24054980-dawson-hardy" target="_blank">Goodreads</a>
      <a class="btn" href="https://www.linkedin.com/in/dawson-hardy-87aa9a13b/" target="_blank">LinkedIn</a>
      <a class="btn" href="./links">All links</a>
    </div>
  </div>

</div>

<hr>

## Latest posts

{% raw %}
{% for post in site.posts limit: 5 %}
- [{{ post.title }}]({{ post.url }}) — {{ post.date | date: "%b %d, %Y" }}
{% endfor %}
{% endraw %}

<hr>

## What I’m building

- 20G UniFi network testing
- Proxmox homelab stack
- SMB network templates
