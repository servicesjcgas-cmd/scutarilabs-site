import os
import markdown

os.makedirs('blog_content', exist_ok=True)
os.makedirs('blog', exist_ok=True)

with open('blog_template.html', 'r', encoding='utf-8') as f:
    template = f.read()

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
        final_html = template.replace('{{TITLE}}', title).replace('{{DATE}}', date).replace('{{CONTENT}}', html_content)

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
