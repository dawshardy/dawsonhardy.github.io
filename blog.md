---
layout: default
title: Blog
---

# Blog

{% raw %}
{% for post in site.posts %}
- [{{ post.title }}]({{ post.url }}) — {{ post.date | date: "%b %d, %Y" }}
{% endfor %}
{% endraw %}
