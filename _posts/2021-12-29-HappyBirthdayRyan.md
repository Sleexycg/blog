---
layout:     post
title:      生日快乐瑞阳！
subtitle:   Sleexy's BEST wishes to RYAN
date:       2021-12-29
author:     Sleexycg
header-img: img/birthday.png
catalog: true
tags:                              
    - 文章
---
生日快乐哟瑞阳


中考加油呀！考黄高！


请你吃个蛋糕（）


> 想和你一起看日落，一起看星辰❤


>我要为你摘一颗星，采一朵云，装入思念的信封里 


```
import turtle as t
import math as m
import random as r
def drawX(a, i):
    angle = m.radians(i)
    return a * m.cos(angle)
def drawY(b, i):
    angle = m.radians(i)
    return b * m.sin(angle)
t.bgcolor("#d3dae8")
t.setup(1000, 800)
t.penup()
t.goto(150, 0)
t.pendown()
t.pencolor("white")
t.begin_fill()
for i in range(360):
    x = drawX(150, i)
    y = drawY(60, i)
    t.goto(x, y)
t.fillcolor("#fef5f7")
t.end_fill()
t.begin_fill()
for i in range(180):
    x = drawX(150, -i)
    y = drawY(70, -i)
    t.goto(x, y)
for i in range(180, 360):
    x = drawX(150, i)
    y = drawY(60, i)
    t.goto(x, y)
t.fillcolor("#f2d7dd")
t.end_fill()
t.pu()
t.goto(120, 0)
t.pd()
t.begin_fill()
for i in range(360):
    x = drawX(120, i)
    y = drawY(48, i)
    t.goto(x, y)
t.fillcolor("#cbd9f9")
t.end_fill()
t.begin_fill()
t.pencolor("#fee48c")
for i in range(540):
    x = drawX(120, i)
    y = drawY(48, i) + 70
    t.goto(x, y)
t.goto(-120, 0)
t.fillcolor("#cbd9f9")
t.end_fill()
t.pu()
t.goto(120, 70)
t.pd()
t.pencolor("#fff0f3")
t.begin_fill()
for i in range(360):
    x = drawX(120, i)
    y = drawY(48, i) + 70
    t.goto(x, y)
t.fillcolor("#fff0f3")
t.end_fill()
t.pu()
t.goto(110, 70)
t.pd()
t.pencolor("#fff9fb")
t.begin_fill()
for i in range(360):
    x = drawX(110, i)
    y = drawY(44, i) + 70
    t.goto(x, y)
t.fillcolor("#fff9fb")
t.end_fill()
t.pu()
t.goto(120, 0)
t.pd()
t.begin_fill()
t.pencolor("#ffa79d")
for i in range(180):
    x = drawX(120, -i)
    y = drawY(48, -i) + 10
    t.goto(x, y)
t.goto(-120, 0)
for i in range(180, 360):
    x = drawX(120, i)
    y = drawY(48, i)
    t.goto(x, y)
t.fillcolor("#ffa79d")
t.end_fill()
t.pu()
t.goto(120, 70)
t.pd()
t.begin_fill()
t.pensize(4)
t.pencolor("#fff0f3")
for i in range(1800):
    x = drawX(120, 0.1 * i)
    y = drawY(-18, i) + 10
    t.goto(x, y)
t.goto(-120, 70)
t.pensize(1)
for i in range(180, 360):
    x = drawX(120, i)
    y = drawY(48, i) + 70
    t.goto(x, y)
t.fillcolor("#fff0f3")
t.end_fill()
t.pu()
t.goto(80, 70)
t.pd()
t.begin_fill()
t.pencolor("#6f3732")
t.goto(80, 120)
for i in range(180):
    x = drawX(80, i)
    y = drawY(32, i) + 120
    t.goto(x, y)
t.goto(-80, 70)
for i in range(180, 360):
    x = drawX(80, i)
    y = drawY(32, i) + 70
    t.goto(x, y)
t.fillcolor("#6f3732")
t.end_fill()
t.pu()
t.goto(80, 120)
t.pd()
t.pencolor("#ffaaa0")
t.begin_fill()
for i in range(360):
    x = drawX(80, i)
    y = drawY(32, i) + 120
    t.goto(x, y)
t.fillcolor("#ffaaa0")
t.end_fill()
t.pu()
t.goto(70, 120)
t.pd()
t.pencolor("#ffc3be")
t.begin_fill()
for i in range(360):
    x = drawX(70, i)
    y = drawY(28, i) + 120
    t.goto(x, y)
t.fillcolor("#ffc3be")
t.end_fill()
t.pu()
t.goto(80, 120)
t.pd()
t.begin_fill()
t.pensize(3)
t.pencolor("#ffaaa0")
for i in range(1800):
    x = drawX(80, 0.1 * i)
    y = drawY(-12, i) + 80
    t.goto(x, y)
t.goto(-80, 120)
t.pensize(1)
for i in range(180, 360):
    x = drawX(80, i)
    y = drawY(32, i) + 120
    t.goto(x, y)
t.fillcolor("#ffaaa0")
t.end_fill()
t.pu()
t.goto(64, 120)
t.pd()
t.pencolor("#b1c9e9")
t.begin_fill()
for i in range(360):
    x = drawX(4, i) + 60
    y = drawY(1, i) + 120
    t.goto(x, y)
t.goto(64, 170)
for i in range(540):
    x = drawX(4, i) + 60
    y = drawY(1, i) + 170
    t.goto(x, y)
t.goto(56, 120)
t.fillcolor("#b1c9e9")
t.end_fill()
t.pencolor("white")
t.pensize(2)
for i in range(1, 6):
    t.goto(64, 120 + 10 * i)
    t.pu()
    t.goto(56, 120 + 10 * i)
    t.pd()
t.pu()
t.goto(60, 170)
t.pd()
t.goto(60, 180)
t.pensize(1)
t.pu()
t.goto(64, 190)
t.pd()
t.pencolor("#f1add1")
t.begin_fill()
for i in range(360):
    x = drawX(4, i) + 60
    y = drawY(10, i) + 190
    t.goto(x, y)
t.fillcolor("#f1add1")
t.end_fill()
t.pu()
t.goto(-56, 120)
t.pd()
t.pencolor("#b1c9e9")
t.begin_fill()
for i in range(360):
    x = drawX(4, i) - 60
    y = drawY(1, i) + 120
    t.goto(x, y)
t.goto(-56, 170)
for i in range(540):
    x = drawX(4, i) - 60
    y = drawY(1, i) + 170
    t.goto(x, y)
t.goto(-64, 120)
t.fillcolor("#b1c9e9")
t.end_fill()
t.pencolor("white")
t.pensize(2)
for i in range(1, 6):
    t.goto(-56, 120 + 10 * i)
    t.pu()
    t.goto(-64, 120 + 10 * i)
    t.pd()
t.pu()
t.goto(-60, 170)
t.pd()
t.goto(-60, 180)
t.pensize(1)
t.pu()
t.goto(-56, 190)
t.pd()
t.pencolor("#f1add1")
t.begin_fill()
for i in range(360):
    x = drawX(4, i) - 60
    y = drawY(10, i) + 190
    t.goto(x, y)
t.fillcolor("#f1add1")
t.end_fill()
t.pu()
t.goto(0, 130)
t.pd()
t.pencolor("#b1c9e9")
t.begin_fill()
for i in range(360):
    x = drawX(4, i)
    y = drawY(1, i) + 130
    t.goto(x, y)
t.goto(4, 180)
for i in range(540):
    x = drawX(4, i)
    y = drawY(1, i) + 180
    t.goto(x, y)
t.goto(-4, 130)
t.fillcolor("#b1c9e9")
t.end_fill()
t.pencolor("white")
t.pensize(2)
for i in range(1, 6):
    t.goto(4, 130 + 10 * i)
    t.pu()
    t.goto(-4, 130 + 10 * i)
    t.pd()
t.pu()
t.goto(0, 180)
t.pd()
t.goto(0, 190)
t.pensize(1)
t.pu()
t.goto(4, 200)
t.pd()
t.pencolor("#f1add1")
t.begin_fill()
for i in range(360):
    x = drawX(4, i)
    y = drawY(10, i) + 200
    t.goto(x, y)
t.fillcolor("#f1add1")
t.end_fill()
t.pu()
t.goto(30, 110)
t.pd()
t.pencolor("#b1c9e9")
t.begin_fill()
for i in range(360):
    x = drawX(4, i) + 30
    y = drawY(1, i) + 110
    t.goto(x, y)
t.goto(34, 160)
for i in range(540):
    x = drawX(4, i) + 30
    y = drawY(1, i) + 160
    t.goto(x, y)
t.goto(26, 110)
t.fillcolor("#b1c9e9")
t.end_fill()
t.pencolor("white")
t.pensize(2)
for i in range(1, 6):
    t.goto(34, 110 + 10 * i)
    t.pu()
    t.goto(26, 110 + 10 * i)
    t.pd()
t.pu()
t.goto(30, 160)
t.pd()
t.goto(30, 170)
t.pensize(1)
t.pu()
t.goto(34, 180)
t.pd()
t.pencolor("#f1add1")
t.begin_fill()
for i in range(360):
    x = drawX(4, i) + 30
    y = drawY(10, i) + 180
    t.goto(x, y)
t.fillcolor("#f1add1")
t.end_fill()
t.pu()
t.goto(-30, 110)
t.pd()
t.pencolor("#b1c9e9")
t.begin_fill()
for i in range(360):
    x = drawX(4, i) - 30
    y = drawY(1, i) + 110
    t.goto(x, y)
t.goto(-26, 160)
for i in range(540):
    x = drawX(4, i) - 30
    y = drawY(1, i) + 160
    t.goto(x, y)
t.goto(-34, 110)
t.fillcolor("#b1c9e9")
t.end_fill()
t.pencolor("white")
t.pensize(2)
for i in range(1, 6):
    t.goto(-26, 110 + 10 * i)
    t.pu()
    t.goto(-34, 110 + 10 * i)
    t.pd()
t.pu()
t.goto(-30, 160)
t.pd()
t.goto(-30, 170)
t.pensize(1)
t.pu()
t.goto(-26, 180)
t.pd()
t.pencolor("#f1add1")
t.begin_fill()
for i in range(360):
    x = drawX(4, i) - 30
    y = drawY(10, i) + 180
    t.goto(x, y)
t.fillcolor("#f1add1")
t.end_fill()
color = ["#e28cb9", "#805a8c", "#eaa989", "#6e90b7", "#b8b68f", "#e174b5", "#cf737c", "#7c8782"]
for i in range(80):
    t.pu()
    x = r.randint(-120, 120)
    y = r.randint(-25, 30)
    t.goto(x, y)
    t.pd()
    t.dot(r.randint(2, 5), color[r.randint(0, 7)])
for i in range(40):
    t.pu()
    x = r.randint(-90, 90)
    y = r.randint(-35, 10)
    t.goto(x, y)
    t.pd()
    t.dot(r.randint(2, 5), color[r.randint(0, 7)])
for i in range(40):
    t.pu()
    x = r.randint(-80, 80)
    y = r.randint(60, 90)
    t.goto(x, y)
    t.pd()
    t.dot(r.randint(2, 5), color[r.randint(0, 7)])
for i in range(30):
    t.pu()
    x = r.randint(-50, 50)
    y = r.randint(45, 70)
    t.goto(x, y)
    t.pd()
    t.dot(r.randint(2, 5), color[r.randint(0, 7)])
for i in range(50):
    t.pu()
    x = r.randint(-500, 500)
    y = r.randint(120, 300)
    t.goto(x, y)
    t.pd()
    t.dot(r.randint(3, 5), color[r.randint(0, 7)])
t.seth(90)
t.pu()
t.goto(0, 0)
t.fd(150)
t.left(90)
t.fd(360)
t.pd()
t.write("吴瑞阳生日快乐", font=("Curlz MT", 90))
t.done()

```


<html lang="zh-CN">
<head>
  <meta charset="utf-8" />
    <script src='//unpkg.com/valine/dist/Valine.min.js'></script>
</head>
<body>
 
    <div id="vcomments"></div>
    <script>
        new Valine({
            el: '#vcomments',
            appId: '5gs7mewf1YuWQ9J4atrPemJL-gzGzoHsz',
            appKey: 'PYoScleaKF7S52j1FTDBITXw',
            placeholder: "Tips：昵称填入QQ号自动补全QQ头像和QQ昵称，支持Markdown语法",
            recordIP:true,
            enableQQ:true,
            visitor: true, // 阅读量统计
    // 设置Bilibili表情包地址
    emojiCDN: '//i0.hdslb.com/bfs/emote/', 
    // 表情title和图片映射
    emojiMaps: {
        "tv_doge": "6ea59c827c414b4a2955fe79e0f6fd3dcd515e24.png",
        "tv_亲亲": "a8111ad55953ef5e3be3327ef94eb4a39d535d06.png",
        "tv_偷笑": "bb690d4107620f1c15cff29509db529a73aee261.png",
        "tv_再见": "180129b8ea851044ce71caf55cc8ce44bd4a4fc8.png",
        "tv_冷漠": "b9cbc755c2b3ee43be07ca13de84e5b699a3f101.png",
        "tv_发怒": "34ba3cd204d5b05fec70ce08fa9fa0dd612409ff.png",
        "tv_发财": "34db290afd2963723c6eb3c4560667db7253a21a.png",
        "tv_可爱": "9e55fd9b500ac4b96613539f1ce2f9499e314ed9.png",
        "tv_吐血": "09dd16a7aa59b77baa1155d47484409624470c77.png",
        "tv_呆": "fe1179ebaa191569b0d31cecafe7a2cd1c951c9d.png",
        "tv_呕吐": "9f996894a39e282ccf5e66856af49483f81870f3.png",
        "tv_困": "241ee304e44c0af029adceb294399391e4737ef2.png",
        "tv_坏笑": "1f0b87f731a671079842116e0991c91c2c88645a.png",
        "tv_大佬": "093c1e2c490161aca397afc45573c877cdead616.png",
        "tv_大哭": "23269aeb35f99daee28dda129676f6e9ea87934f.png",
        "tv_委屈": "d04dba7b5465779e9755d2ab6f0a897b9b33bb77.png",
        "tv_害羞": "a37683fb5642fa3ddfc7f4e5525fd13e42a2bdb1.png",
        "tv_尴尬": "7cfa62dafc59798a3d3fb262d421eeeff166cfa4.png",
        "tv_微笑": "70dc5c7b56f93eb61bddba11e28fb1d18fddcd4c.png",
        "tv_思考": "90cf159733e558137ed20aa04d09964436f618a1.png",
        "tv_惊吓": "0d15c7e2ee58e935adc6a7193ee042388adc22af.png",
        // ... 更多表情
    } 
})
    </script>
</body>