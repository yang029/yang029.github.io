---
layout: post
title:  "Update log"
date:   2020-02-13 00:33:00 
categories: log
---

* At the beginning, I just want to share my complicated feelings on my blog. The initial theme is ~~very~~ kind of ugly, so I design my own genre based on that theme. The inspiration mainly comes from several my favorite blogs. ~~like liuli.in~~ 
* GitHub pages mainly adopt jekyll as its theme, which is based on Ruby language and is a site generator for liquid, Markdown and YAML. Liquid is a template language which can largely reduce the effort to write new websites. YAML is a configuration file storing the configuration(theme, author, contack...) for the website. It really takes me some time to figure out the structure and relations bewteen these languages.(I never heard even one of them before!)
* The refactor of the old theme maybe the hardest part for my new blog. The relations are really complicated among all the HTML templates. Different attribute share the same class name so when I try to change one small feature I always screw up all the pages.
Just like this gif.
![bug-fix](../../../../assets/pic/bug-fix.gif)
*  Anyway, compared to my awesome blog pages, all the effort and hardships are trivial.   



### &ensp;&ensp;&ensp;&ensp;  update log
- **Config.yml** Add header_pages --which is the list to show on home page 
* **Footer.html** delete the footer for site heading to save space
- **home.html** I remove all the YAMI headers and set my own HTML pages. I refer to my own stylesheet and reschedule the structure of the page. But this also lost the adaption on mobile devices. 
* **Content.html** add a new content HTML for the content of the post which is removed from the main page 
- **minima-classic.scss** To better fit the background image, I changed the default background-color, text-color, etc. to their oppisite. 
* **_layout.scss** remove the lines on the header, slightly modify the **font-size** and **font-family** of the title, add style for two links at home, and shrink the space where the footer occupy.
- **home.scss** the new css file for the home page. Adopt minima-classic skin and include the styles for the home page
* **style.scss** add the fixed background picture for other pages except the home pages so that when scroll down the background won't change.
 > **important notes**: the background image on the home page is a lot different from that on other pages. I try to make the background on home page kind of opaque so that the text will be clearer. However, I indeed don't find obvious change and I am considering to roll back the changes.
- bg1.jpg - bg16.jpg beautiful background images
 


