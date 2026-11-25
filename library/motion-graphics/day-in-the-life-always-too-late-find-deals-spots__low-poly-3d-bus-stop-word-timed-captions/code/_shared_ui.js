// ---------- 2D layer: captions, pills, stamps, list, end card
const SAFE = CONFIG.safe, CX = (SAFE.left + SAFE.right) / 2
function pill(text, row, k, kind) {
  if (k <= 0) return
  const fs = 44; g.font = `700 ${fs}px system-ui, -apple-system, BlinkMacSystemFont, Helvetica, Arial, sans-serif`; const mark = kind === 'good' ? '✓' : kind === 'bad' ? '✕' : '', tw = g.measureText(text).width, w = tw + (mark ? 124 : 76), h = 92, y = SAFE.top + 60 + row * 112
  g.save(); g.translate(CX, y); g.scale(k, k); g.shadowColor = 'rgba(0,0,0,.35)'; g.shadowBlur = 30; g.shadowOffsetY = 12
  g.fillStyle = CONFIG.card; g.beginPath(); g.roundRect(-w / 2, -h / 2, w, h, h / 2); g.fill(); g.shadowColor = 'transparent'
  let x = -w / 2 + 38
  if (mark) { g.fillStyle = kind === 'good' ? CONFIG.good : CONFIG.bad; g.beginPath(); g.arc(x + 16, 0, 26, 0, 7); g.fill(); g.fillStyle = '#0b0c10'; g.font = `800 34px system-ui, -apple-system, BlinkMacSystemFont, Helvetica, Arial, sans-serif`; g.textAlign = 'center'; g.textBaseline = 'middle'; g.fillText(mark, x + 16, 2); x += 58 }
  g.fillStyle = CONFIG.bright; g.font = `700 ${fs}px system-ui, -apple-system, BlinkMacSystemFont, Helvetica, Arial, sans-serif`; g.textAlign = 'left'; g.textBaseline = 'middle'; g.fillText(text, x, 2); g.restore()
}
function stamp(text, k, color, rot, yShare) {
  if (k <= 0) return
  const s = lerp(2.6, 1, eo(k)); g.save(); g.translate(CX, H * yShare + SAFE.top); g.rotate(rot); g.scale(s, s); g.globalAlpha = clamp(k * 3)
  g.font = '800 92px system-ui, -apple-system, BlinkMacSystemFont, Helvetica, Arial, sans-serif'; const w = g.measureText(text).width + 90; g.fillStyle = color; g.beginPath(); g.roundRect(-w / 2, -80, w, 160, 26); g.fill()
  g.strokeStyle = '#fff'; g.lineWidth = 8; g.beginPath(); g.roundRect(-w / 2 + 14, -66, w - 28, 132, 16); g.stroke()
  g.fillStyle = '#fff'; g.textAlign = 'center'; g.textBaseline = 'middle'; g.fillText(text, 0, 6); g.restore()
}
function coin(xs, ys, k, t, size = 400) {
  if (k <= 0) return
  const sx = Math.cos(t * 3.2), h = size * k, w = h * 0.8 * Math.abs(sx)
  g.save(); g.translate(W * xs, H * ys); g.shadowColor = 'rgba(255,255,255,.55)'; g.shadowBlur = 70; g.drawImage(G_IMG, -w / 2, -h / 2, Math.max(2, w), h); g.restore()
}
function captions(t) {
  let gi = -1; for (let i = 0; i < GROUPS.length; i++) { if (t >= WORDS[GROUPS[i][0]][1] - 0.04) gi = i }
  if (gi < 0) return
  const [a, b, br, mul] = GROUPS[gi]; const endT = gi + 1 < GROUPS.length ? WORDS[GROUPS[gi + 1][0]][1] - 0.04 : WORDS[b][2] + 0.5
  if (t > Math.min(endT, WORDS[b][2] + 0.9)) return
  const lines = [[]]; for (let i = a; i <= b; i++) { lines[lines.length - 1].push(i); if (i === br) lines.push([]) }
  let fs = 118 * mul; const maxW = SAFE.right - SAFE.left - 20
  const widthOf = (ln) => { g.font = `800 ${fs}px system-ui, -apple-system, BlinkMacSystemFont, Helvetica, Arial, sans-serif`; return g.measureText(ln.map(i => WORDS[i][0].toUpperCase()).join(' ')).width }
  while (Math.max(...lines.map(widthOf)) > maxW && fs > 40) fs -= 4
  g.font = `800 ${fs}px system-ui, -apple-system, BlinkMacSystemFont, Helvetica, Arial, sans-serif`; g.textBaseline = 'middle'; g.textAlign = 'left'; g.lineJoin = 'round'
  const lh = fs * 1.1, y0 = H * CONFIG.capY - (lines.length - 1) * lh / 2, sp = g.measureText(' ').width
  lines.forEach((ln, li) => {
    let x = CX - widthOf(ln) / 2; const y = y0 + li * lh
    for (const i of ln) {
      const txt = WORDS[i][0].toUpperCase(), ww = g.measureText(txt).width, said = t >= WORDS[i][1] - 0.04
      if (said) { const k = back(seg(t, WORDS[i][1] - 0.04, WORDS[i][1] + 0.1)), cur = t < WORDS[i][2] + 0.06 || i === b
        g.save(); g.translate(x + ww / 2, y); g.scale(0.7 + 0.3 * k, 0.7 + 0.3 * k); g.textAlign = 'center'
        g.strokeStyle = '#000'; g.lineWidth = fs * 0.2; g.shadowColor = 'rgba(0,0,0,.45)'; g.shadowBlur = 0; g.shadowOffsetY = fs * 0.07; g.strokeText(txt, 0, 0); g.shadowColor = 'transparent'
        g.fillStyle = cur ? CONFIG.capHi : CONFIG.capBase; g.fillText(txt, 0, 0); g.restore() }
      x += ww + sp
    }
  })
}
function endCard(t) {
  const k = seg(t, T.end, T.end + 0.35); if (k <= 0) return
  g.fillStyle = `rgba(6,6,9,${eo(k)})`; g.fillRect(0, 0, W, H)
  const a = eo(seg(t, T.end + 0.15, T.end + 0.6)), gh = 340, gy = H * 0.3
  g.save(); g.globalAlpha = a; g.translate(W / 2, gy); const s = lerp(1.25, 1, eo(seg(t, T.end + 0.15, T.end + 0.8))); g.scale(s, s); g.shadowColor = 'rgba(255,255,255,.35)'; g.shadowBlur = 90; g.drawImage(G_IMG, -gh * 0.4, -gh / 2, gh * 0.8, gh); g.restore()
  const ww = 540, wh = ww * WORD_IMG.height / WORD_IMG.width, wy = gy + gh / 2 + 10; g.save(); g.globalAlpha = eo(seg(t, T.end + 0.35, T.end + 0.8)); g.drawImage(WORD_IMG, W / 2 - ww / 2, wy, ww, wh); g.restore()
  g.textAlign = 'center'; g.textBaseline = 'middle'; const ly = wy + wh + 90
  CONFIG.endLines.forEach((s, i) => { const kk = eo(seg(t, T.end + 0.7 + i * 0.32, T.end + 1.05 + i * 0.32)); g.globalAlpha = kk; g.fillStyle = i === CONFIG.endLines.length - 1 ? '#fff' : '#d4d4d8'; g.font = '700 78px system-ui, -apple-system, BlinkMacSystemFont, Helvetica, Arial, sans-serif'; g.fillText(s, W / 2, ly + i * 100 + (1 - kk) * 26) })
  const kk = back(seg(t, T.end + 1.9, T.end + 2.2)); if (kk > 0) { g.globalAlpha = 1; g.save(); g.translate(W / 2, ly + CONFIG.endLines.length * 100 + 70); g.scale(kk, kk); g.font = '700 56px system-ui, -apple-system, BlinkMacSystemFont, Helvetica, Arial, sans-serif'; const w = g.measureText(CONFIG.site).width + 110; g.fillStyle = '#fff'; g.beginPath(); g.roundRect(-w / 2, -60, w, 120, 60); g.fill(); g.fillStyle = '#0b0c10'; g.fillText(CONFIG.site, 0, 3); g.restore() }
  g.globalAlpha = 1
}
