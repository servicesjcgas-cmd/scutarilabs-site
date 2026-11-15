import os
import markdown

# Create directories if they don't exist
os.makedirs('blog_content', exist_ok=True)
os.makedirs('blog', exist_ok=True)

# Read your master template
with open('blog_template.html', 'r', encoding='utf-8') as f:
    template = f.read()

post_links = []

# Process every markdown file
for filename in os.listdir('blog_content'):
    if filename.endswith('.md'):
        with open(f'blog_content/{filename}', 'r', encoding='utf-8') as f:
            text = f.read()

        # Parse front matter manually
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

        # Convert markdown to HTML
        html_content = markdown.markdown(md_content)

        # Inject data into template
        final_html = template.replace('{{TITLE}}', title).replace('{{DATE}}', date).replace('{{CONTENT}}', html_content)

        # Save the blog post in the /blog/ folder
        out_name = filename.replace('.md', '.html')
        with open(f'blog/{out_name}', 'w', encoding='utf-8') as f:
            f.write(final_html)
        
        # Store data for the index page
        post_links.append({'title': title, 'date': date, 'url': f'/blog/{out_name}'})
        print(f"Built: blog/{out_name}")

# Generate the main blog.html directory page
post_links.sort(key=lambda x: x['date'], reverse=True)

index_html = template.replace('{{TITLE}}', 'ScutariLabs Blog Directory').replace('{{DATE}}', '')
links_html = "<h2>All Articles</h2><ul>"
for post in post_links:
    links_html += f'<li style="margin-bottom: 15px;"><a href="{post["url"]}" style="font-size: 1.2rem;">{post["title"]}</a><br><span style="color: #A0AAB5;">{post["date"]}</span></li>'
links_html += "</ul>"

index_html = index_html.replace('{{CONTENT}}', links_html)

with open('blog.html', 'w', encoding='utf-8') as f:
    f.write(index_html)

print("Built: blog.html (Index page)")
print("Done! You can now commit the generated HTML to GitHub.")
