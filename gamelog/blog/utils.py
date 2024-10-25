import markdown
from django.utils.safestring import mark_safe

def get_markdown(content):
    md = markdown.Markdown(
        extensions=[
            'fenced_code',           # For code blocks with ```
            'tables',                # For tables
            'nl2br',                 # Convert newlines to <br>
            'toc',                   # Table of contents
            'mdx_math',              # For math equations
            'pymdownx.highlight',    # Code highlighting
            'pymdownx.superfences',  # Nested code blocks
            'pymdownx.emoji',        # Emoji support
        ]
    )
    return mark_safe(md.convert(content))