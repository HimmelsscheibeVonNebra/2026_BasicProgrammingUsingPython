"""Pure HTML formatting. Escape all external text before interpolation."""
from html import escape


def render_html(rows, summary, market, snapshot_date):
    """Return a complete HTML page; round percentages only when displaying."""
    body = []
    for q in rows:
        change = q["change_pct"]
        direction = "up" if change > 0 else "down" if change < 0 else "flat"
        body.append(f'<tr><td>{escape(q["code"])}</td>'
                    f'<td>{escape(q["name"])}</td><td>{escape(q["market"])}</td>'
                    f'<td>{q["close"]:,}</td><td class="{direction}">{change:+.2f}%</td>'
                    f'<td>{q["volume"]:,}</td></tr>')
    mean = "N/A" if summary["mean"] is None else f'{summary["mean"]:+.2f}%'
    table_body = "".join(body) or '<tr><td colspan="6">표시할 종목이 없습니다.</td></tr>'
    return f'''<!doctype html>
<html lang="ko"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>한국 주식시장 분석 실습</title>
<style>
body {{font-family:system-ui,sans-serif;background:#f3f5f9;color:#17243c;margin:0}}
main {{max-width:1040px;margin:48px auto;padding:24px}}
h1 {{font-size:2rem}} .meta {{color:#53627b}} .summary {{background:#17243c;color:white;padding:24px;border-radius:12px}}
.scroll {{overflow-x:auto}} table {{border-collapse:collapse;width:100%;background:white;margin-top:24px}}
caption {{text-align:left;padding:12px 0;font-weight:bold}}
th,td {{padding:14px;text-align:right;border-bottom:1px solid #dde3ec;white-space:nowrap}}
th:nth-child(-n+3),td:nth-child(-n+3) {{text-align:left}}
.up {{color:#b12a38}} .down {{color:#245bbb}} .flat {{color:#53627b}}
footer {{margin-top:24px;color:#53627b;line-height:1.6}}
</style></head><body><main>
<p class="meta">PYTHON / WEEK 11 / CLASSROOM DATA</p>
<h1>한국 주식시장 분석</h1>
<p>기준일: {escape(snapshot_date)} · 시장: {escape(market)} · 출처: 수업용 가상 CSV</p>
<section class="summary" aria-label="표본 요약">
종목 {summary["count"]}개 · 상승 {summary["up"]} · 하락 {summary["down"]} · 보합 {summary["flat"]}
<p>표본 단순평균 등락률 <strong>{mean}</strong></p></section>
<div class="scroll"><table><caption>일간 등락률 내림차순 / 동률은 종목코드 오름차순</caption>
<thead><tr><th scope="col">코드</th><th scope="col">종목</th><th scope="col">시장</th>
<th scope="col">종가 (원)</th><th scope="col">등락률</th><th scope="col">거래량 (주)</th></tr></thead>
<tbody>{table_body}</tbody></table></div>
<footer>교육용 가상 데이터입니다. 실제 시세 또는 현재 상장 종목 목록이 아닙니다.<br>
표본의 단순평균이며 KOSPI/KOSDAQ 지수 수익률이 아닙니다. 투자 판단용 정보가 아닙니다.</footer>
</main></body></html>'''
