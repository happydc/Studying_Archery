# 진단기 index.html에 홈 화면 설치용 태그를 넣는다 (GitHub Pages용)
import sys
p = sys.argv[1] if len(sys.argv) > 1 else 'index.html'
t = open(p, encoding='utf-8').read()
if 'manifest.webmanifest' not in t:
    head = ('<link rel="manifest" href="manifest.webmanifest">\n'
            '<meta name="theme-color" content="#2e5a4d">\n'
            '<link rel="icon" href="icons/icon-192.png">\n'
            '<link rel="apple-touch-icon" href="icons/apple-touch-icon.png">\n'
            '<meta name="apple-mobile-web-app-capable" content="yes">\n'
            '<meta name="mobile-web-app-capable" content="yes">\n'
            '<meta name="apple-mobile-web-app-title" content="사법 진단기">\n</head>')
    t = t.replace('</head>', head, 1)
    sw = ("<script>if('serviceWorker' in navigator && location.protocol==='https:'){"
          "window.addEventListener('load',()=>navigator.serviceWorker.register('sw.js').catch(()=>{}));}</script>\n</body>")
    t = t.replace('</body>', sw, 1)
    open(p, 'w', encoding='utf-8').write(t)
print('ok')
