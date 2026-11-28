import os
import markdown

os.makedirs('blog_content', exist_ok=True)
os.makedirs('blog', exist_ok=True)

with open('blog_template.html', 'r', encoding='utf-8') as f:
    template = f.read()

GPLAY_BUTTON_HTML = """
<div style="margin: 32px 0;">
  <a href="https://play.google.com/store/apps/details?id=com.scutarilabs.travelsafeai" target="_blank" rel="noopener noreferrer" aria-label="Get Travel Safe AI on Google Play" style="display: inline-flex; align-items: center; gap: 12px; padding: 10px 24px; background-color: #181818; border-radius: 9999px; text-decoration: none; transition: background-color 0.2s ease;" onmouseover="this.style.backgroundColor='#2a2a2a'" onmouseout="this.style.backgroundColor='#181818'">
    <svg width="22" height="22" viewBox="0 0 24 24" fill="#ffffff" style="display: block; flex-shrink: 0;">
      <path d="M6 4l15 8-15 8V4z"/>
    </svg>
    <span style="display: flex; flex-direction: column; text-align: left; line-height: 1.1;">
      <span style="font-size: 11px; color: #cccccc; letter-spacing: 0.05em; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; text-transform: uppercase;">GET IT ON</span>
      <span style="font-size: 19px; color: #ffffff; font-weight: 700; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; line-height: 1.15;">Google Play</span>
    </span>
  </a>
</div>
"""

post_links = []

for filename in os.listdir('blog_content'):
    if filename.endswith('.md'):
        with open(f'blog_content/{filename}', 'r', encoding='utf-8') as f:
            text = f.read()

        parts = text.split('---')
        title = "Untitled"
        date = ""
        if len(parts) >= 3:
            frontmatter = parts[1]
            md_content = '---'.join(parts[2:])
            for line in frontmatter.split('\n'):
                if line.startswith('title:'):
                    title = line.replace('title:', '').strip().strip('"').strip("'")
                if line.startswith('date:'):
                    date = line.replace('date:', '').strip().strip('"').strip("'")
        else:
            md_content = text

        html_content = markdown.markdown(md_content)
        final_html = template.replace('{{TITLE}}', title).replace('{{DATE}}', date).replace('{{CONTENT}}', html_content + GPLAY_BUTTON_HTML)

        out_name = filename.replace('.md', '.html')
        with open(f'blog/{out_name}', 'w', encoding='utf-8') as f:
            f.write(final_html)

        post_links.append({'title': title, 'date': date, 'url': f'/blog/{out_name}'})
        print(f"Built: blog/{out_name}")

post_links.sort(key=lambda x: x['date'], reverse=True)

index_html = template.replace('{{TITLE}}', 'Research & Engineering Publications').replace('{{DATE}}', 'All Articles')
cards_html = '<div style="display: flex; flex-direction: column; gap: 20px; margin-top: 24px;">'
for post in post_links:
    cards_html += f'''<a href="{post["url"]}" class="bento-card" style="padding: 24px 28px; text-decoration: none; color: inherit; background: #FFFFFF;">
      <div style="font-size: 0.85rem; color: #0066CC; font-weight: 600; margin-bottom: 6px;">{post["date"]}</div>
      <h2 style="font-size: 1.35rem; color: #1D1D1F; margin-bottom: 8px;">{post["title"]}</h2>
      <div style="color: #6E6E73; font-size: 0.95rem; font-weight: 500;">Read publication &rarr;</div>
    </a>'''
cards_html += '</div>'

index_html = index_html.replace('{{CONTENT}}', cards_html)

with open('blog.html', 'w', encoding='utf-8') as f:
    f.write(index_html)

print("Built: blog.html (Apple Card Index page)")
