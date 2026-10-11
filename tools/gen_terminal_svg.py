#!/usr/bin/env python3
"""Generate a self-contained animated terminal SVG for the GitHub profile header.

Realistic shell model: the `$ ` prompt is printed instantly, the command is
typed character-by-character, and on "enter" the command's output prints all at
once (not typed). A readable pause separates commands, and a trailing prompt
waits with a blinking cursor at the end.

Vector + SMIL, so it is crisp at any width and animates in <img>-loaded SVGs on
GitHub (the mechanism behind every README typing-SVG).
"""

PROMPT = "#50fa7b"   # green
CMD    = "#f8f8f2"   # foreground
ACCENT = "#bd93f9"   # purple
COMMENT= "#6272a4"   # muted
OUT    = "#f8f8f2"
LABEL  = "#ffb86c"   # orange
DIR    = "#8be9fd"   # cyan
BG     = "#282a36"
BAR    = "#21222c"
CURSOR = "#f8f8f2"

FS = 15.0
CW = 9.7             # advance for viewBox/clip sizing (generous: keeps lines off the edge)
CWR = 9.12           # closer-to-real advance for positioning the typing cursor/clip start
LH = 27.0
PADX = 28.0
Y0 = 86.0            # first baseline
BARH = 46.0

# Timing (seconds)
START = 0.6
TYPE = 0.085         # per typed character
ENTER = 0.4          # after typing, before output prints
FADE = 0.18          # output print-in
READ = 0.95          # pause after output, before next command

# A block = a typed command plus the output it prints.
BLOCKS = [
    {
        "cmd": "whoami",
        "out": [[("owen", ACCENT), ("  security engineer @ Ally", OUT)]],
    },
    {
        "cmd": "cat ~/.history",
        "out": [
            [("sre", LABEL), ("       -> ", COMMENT), ("ran production AWS with Terraform and CI/CD", OUT)],
            [("soc", LABEL), ("       -> ", COMMENT), ("worked the queue as the team's AWS SME", OUT)],
            [("sec eng", LABEL), ("   -> ", COMMENT), ("cloud and pipeline security, internal offensive testing", OUT)],
        ],
    },
    {
        "cmd": "ls ~/focus",
        "out": [
            [("ai-security/     ", DIR), ("devsecops/               ", DIR), ("pipeline-security/", DIR)],
            [("cloud-security/  ", DIR), ("infrastructure-as-code/  ", DIR), ("offsec/", DIR)],
        ],
    },
]
PROMPT_STR = "$ "


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def seglen(segs):
    return sum(len(t) for t, _ in segs)


# Lay rows out: one cmd row + its out rows per block, a blank row between blocks,
# then a trailing prompt row.
rows = []  # (kind, payload)
for bi, b in enumerate(BLOCKS):
    if bi:
        rows.append(("blank", None))
    rows.append(("cmd", (bi, b["cmd"])))
    for o in b["out"]:
        rows.append(("out", (bi, o)))
rows.append(("prompt", None))

max_chars = max(
    [len(PROMPT_STR) + len(b["cmd"]) for b in BLOCKS]
    + [seglen(o) for b in BLOCKS for o in b["out"]]
)
width = round(PADX * 2 + max_chars * CW)
height = round(Y0 + (len(rows) - 1) * LH + 24)

defs, body = [], []
body.append(f'<rect x="0" y="0" width="{width}" height="{height}" rx="12" fill="{BG}"/>')
body.append(f'<path d="M0 12 Q0 0 12 0 H{width-12} Q{width} 0 {width} 12 V{BARH} H0 Z" fill="{BAR}"/>')
for i, c in enumerate(("#ff5f56", "#ffbd2e", "#27c93f")):
    body.append(f'<circle cx="{26 + i*22}" cy="{BARH/2:.0f}" r="6.5" fill="{c}"/>')
body.append(
    f'<text x="{width/2:.0f}" y="{BARH/2 + 5:.0f}" text-anchor="middle" '
    f'font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace" '
    f'font-size="13" fill="#6272a4">owen@github: ~</text>'
)

mono = ("font-family=\"ui-monospace, SFMono-Regular, 'JetBrains Mono', "
        "Menlo, Consolas, monospace\"")

# begin-time expressions, chained per block
cmd_begin = {}   # bi -> begin expr for the command typing
out_begin = {}   # bi -> begin expr for the output print
for bi in range(len(BLOCKS)):
    if bi == 0:
        cmd_begin[bi] = f"{START}s"
    else:
        cmd_begin[bi] = f"of{bi-1}.end+{READ}s"
    out_begin[bi] = f"tc{bi}.end+{ENTER}s"

for ri, (kind, payload) in enumerate(rows):
    y = Y0 + ri * LH

    if kind == "blank":
        continue

    if kind == "cmd":
        bi, cmd = payload
        begin = cmd_begin[bi]
        prompt_w = len(PROMPT_STR) * CWR
        cur_end = PADX + (len(PROMPT_STR) + len(cmd)) * CWR
        dur = len(cmd) * TYPE
        # Typing via per-character opacity reveals (no clip-path -- the GitHub
        # mobile app ignores animated clips but honors opacity). The cursor
        # x-animate carries id tc{bi} so output chaining can anchor on its .end.
        tspans = [f'<tspan fill="{PROMPT}" xml:space="preserve" opacity="0">{esc(PROMPT_STR)}'
                  f'<set attributeName="opacity" to="1" begin="tc{bi}.begin" fill="freeze"/></tspan>']
        for i, ch in enumerate(cmd):
            tspans.append(
                f'<tspan fill="{CMD}" xml:space="preserve" opacity="0">{esc(ch)}'
                f'<set attributeName="opacity" to="1" begin="tc{bi}.begin+{i*TYPE:.3f}s" fill="freeze"/></tspan>'
            )
        body.append(
            f'<text x="{PADX:.0f}" y="{y:.0f}" {mono} font-size="{FS:.0f}">' + "".join(tspans) + '</text>'
        )
        # cursor rides the typed edge, then disappears on "enter"
        body.append(
            f'<rect y="{y-FS+2:.1f}" width="8.5" height="{FS+2:.0f}" fill="{CURSOR}" opacity="0" '
            f'x="{PADX+prompt_w:.1f}">'
            f'<animate id="tc{bi}" attributeName="x" from="{PADX+prompt_w:.1f}" to="{cur_end:.1f}" '
            f'begin="{begin}" dur="{dur:.2f}s" fill="freeze"/>'
            f'<set attributeName="opacity" to="0.9" begin="tc{bi}.begin"/>'
            f'<set attributeName="opacity" to="0" begin="tc{bi}.end"/></rect>'
        )

    elif kind == "out":
        bi, segs = payload
        begin = out_begin[bi]
        tspans = "".join(
            f'<tspan fill="{c}" xml:space="preserve">{esc(t)}</tspan>' for t, c in segs
        )
        # first output row of the block carries the id other blocks chain from
        is_first = rows[ri - 1][0] == "cmd"
        anim_id = f' id="of{bi}"' if is_first else ""
        body.append(
            f'<text x="{PADX:.0f}" y="{y:.0f}" {mono} font-size="{FS:.0f}" opacity="0">{tspans}'
            f'<animate{anim_id} attributeName="opacity" from="0" to="1" begin="{begin}" '
            f'dur="{FADE:.2f}s" fill="freeze"/></text>'
        )

    elif kind == "prompt":
        begin = f"of{len(BLOCKS)-1}.end+{READ}s"
        body.append(
            f'<text x="{PADX:.0f}" y="{y:.0f}" {mono} font-size="{FS:.0f}" fill="{PROMPT}" '
            f'opacity="0" xml:space="preserve">{esc(PROMPT_STR)}'
            f'<animate attributeName="opacity" from="0" to="1" begin="{begin}" dur="0.12s" fill="freeze"/></text>'
        )
        cur_x = PADX + len(PROMPT_STR) * CWR
        body.append(
            f'<rect x="{cur_x:.1f}" y="{y-FS+2:.1f}" width="8.5" height="{FS+2:.0f}" fill="{CURSOR}" opacity="0">'
            f'<set attributeName="opacity" to="1" begin="{begin}"/>'
            f'<animate attributeName="opacity" values="1;1;0;0" dur="1.06s" begin="{begin}" repeatCount="indefinite"/></rect>'
        )

svg = (
    f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
    f'width="{width}" height="{height}" role="img" '
    f'aria-label="Terminal: owen, security engineer at Ally; career history and focus areas">\n'
    f'<defs>\n' + "\n".join(defs) + "\n</defs>\n" + "\n".join(body) + "\n</svg>\n"
)
with open("terminal.svg", "w") as f:
    f.write(svg)
print(f"wrote terminal.svg  {width}x{height}  rows={len(rows)}")
