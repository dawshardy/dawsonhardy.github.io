---
layout: default
title: Blog
---

{% for post in site.posts %}
- [{{ post.title }}]({{ post.url }}) <span class="post-meta">— {{ post.date | date: "%b %d, %Y" }}</span>
{% endfor %}
