---
hide: 
    - toc
    - navigation
---

<style> .md-footer__inner:not([hidden]) { display: none } </style>
<!-- <style> .md-footer__link--prev:not([hidden]) { display: none } </style> -->
<!-- <style> .md-footer__link--next:not([hidden]) { display: none } </style> -->

# TinySpark

 Teaching Tiny Machine Learning

---

Welcome to **TinySpark**, the online learning platform that teaches you how to create smart machine learning applications on tiny devices. 

TinyML is an emerging field of technology that combines deep learning and embedded systems to enable artificial intelligence on resource-constrained hardware. It has many applications in various domains, such as agriculture, environmental sensing, speech recognition, healthcare and more.

On the platform, you will interactively learn the basics of neural networks, how to train them, and how to use libraries and tools such as [Tensorflow] to compress and optimize them for TinyML. You will learn how to fully develop and deploy machine learning networks.

To follow along with the projects and examples, you will need a TinySpark development board, which is a tiny device that packs enough processing power and sensors to start your TinyML journey!

![TinyML development baord](assets/images/devboard.png)

[Go to the TinySpark kit Introduction](../docs/kit/introduction.md){ .md-button .md-button--primary }
[Go to Chapter 1](/docs/chapter1/introduction.md){ .md-button .md-button--primary }
[Go to About](/docs/chapter1/introduction.md){ .md-button .md-button--primary }

<!-- sources -->
[Tensorflow]: https://www.tensorflow.org/overview

<!-- Last updated timestamp -->
<script>fetch("https://api.github.com/repos/j-siderius/TinySpark/actions/runs?per_page=10").then((e=>e.json())).then((e=>{for(let t of e.workflow_runs)if("pages build and deployment"==t.name&&"success"==t.conclusion){datetime=new Date(t.updated_at),document.getElementById("lastupdate").innerHTML=datetime.toLocaleString("en-GB",{timeZone:"CET"});break}}));</script>
<i>Last updated: <span id=lastupdate></span></i>