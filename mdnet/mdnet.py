import os
import markdown
from jinja2 import Environment, FileSystemLoader
import argparse
import frontmatter

def convert_md_to_html(md):
    html = markdown.markdown(md)
    return html

def render_template(template_path, metadata, content):
    template_dir = os.path.dirname(template_path)
    env = Environment(loader=FileSystemLoader(template_dir))
    template = env.get_template(os.path.basename(template_path))
    return template.render(title=metadata['title'], date=metadata['date'], content=content)

def render_index(template_path, posts):
    template_dir = os.path.dirname(template_path)
    env = Environment(loader=FileSystemLoader(template_dir))
    template = env.get_template(os.path.basename(template_path))
    return template.render(posts=posts)

def generate_site(input_dir, output_dir, template_path, index_path):
    posts = []
    for md_file in os.listdir(input_dir):
        if md_file.endswith(".md"):
            with open(os.path.join(input_dir, md_file), "r") as file:
                post = frontmatter.load(file)
            
            with open(os.path.join(output_dir, post.metadata['title'] + ".html"), "w") as file:
                file.write(render_template(template_path, post.metadata, convert_md_to_html(post.content)))
                
            posts.append({'title' : post.metadata['title'], 
                          'date' : post.metadata['date'],
                          'tldr' : post.metadata['tldr'],
                          'file' : post.metadata['title'] + '.html'})
    
    with open(os.path.join(output_dir, 'index.html'), 'w') as file:
        file.write(render_index(index_path, posts))

def main():
    parser = argparse.ArgumentParser(description = "Generate a static site from Markdown files.")
    parser.add_argument("input_dir", help = "The directory containing the Markdown files.")
    parser.add_argument("output_dir", help = "The directrory to output the HTML files to.")
    parser.add_argument("template_path", help = "The path to the HTML template.")
    parser.add_argument("index_template_path", help = "The path to the index HTML template.")
    args = parser.parse_args()

    generate_site(args.input_dir, args.output_dir, args.template_path, args.index_template_path)

if __name__ == "__main__":
    main()
