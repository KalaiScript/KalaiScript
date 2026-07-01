import datetime
import os

# List of high-quality coding quotes
QUOTES = [
    {
        "text": "First, solve the problem. Then, write the code.",
        "author": "John Johnson"
    },
    {
        "text": "Clean code always looks like it was written by someone who cares.",
        "author": "Michael Feathers"
    },
    {
        "text": "Simplicity is the soul of efficiency.",
        "author": "Austin Freeman"
    },
    {
        "text": "Make it work, make it right, make it fast.",
        "author": "Kent Beck"
    },
    {
        "text": "One of my most productive days was throwing away 1000 lines of code.",
        "author": "Ken Thompson"
    },
    {
        "text": "Talk is cheap. Show me the code.",
        "author": "Linus Torvalds"
    },
    {
        "text": "Software is a great combination between artistry and engineering.",
        "author": "Bill Gates"
    },
    {
        "text": "Before software can be reusable it first has to be usable.",
        "author": "Ralph Johnson"
    },
    {
        "text": "Programs must be written for people to read, and only incidentally for machines to execute.",
        "author": "Harold Abelson"
    },
    {
        "text": "The best way to predict the future is to invent it.",
        "author": "Alan Kay"
    },
    {
        "text": "Computers are good at following instructions, but not at reading your mind.",
        "author": "Donald Knuth"
    },
    {
        "text": "Any fool can write code that a computer can understand. Good programmers write code that humans can understand.",
        "author": "Martin Fowler"
    }
]

def wrap_text(text, max_chars=65):
    words = text.split(' ')
    lines = []
    current_line = []
    current_length = 0
    for word in words:
        if current_length + len(word) + 1 > max_chars:
            lines.append(' '.join(current_line))
            current_line = [word]
            current_length = len(word)
        else:
            current_line.append(word)
            current_length += len(word) + 1
    if current_line:
        lines.append(' '.join(current_line))
    return lines

def generate_svg():
    # Pick a quote based on the day of the year to keep it daily-changing and stable
    day_of_year = datetime.datetime.now().timetuple().tm_yday
    quote = QUOTES[day_of_year % len(QUOTES)]
    
    wrapped_lines = wrap_text(quote["text"])
    
    # Calculate SVG layout based on lines
    if len(wrapped_lines) == 1:
        text_elements = f'<text x="0" y="55" fill="#a9b1d6" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-style="italic">“{wrapped_lines[0]}”</text>'
        author_y = 85
    else:
        text_elements = (
            f'<text x="0" y="45" fill="#a9b1d6" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-style="italic">“{wrapped_lines[0]}”</text>'
            f'<text x="0" y="68" fill="#a9b1d6" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-style="italic">{wrapped_lines[1]}”</text>'
        )
        author_y = 95
        
    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 120" width="100%" height="120">
  <style>
    .quote-box {{
      animation: pulse 4s ease-in-out infinite alternate;
    }}
    @keyframes pulse {{
      0% {{ stroke: #7aa2f7; stroke-width: 1px; }}
      100% {{ stroke: #bb9af7; stroke-width: 1px; }}
    }}
  </style>

  <!-- Card Background -->
  <rect width="598" height="118" x="1" y="1" rx="8" fill="#1a1b26" class="quote-box" />
  
  <!-- Left Side Decorative Icon -->
  <g transform="translate(25, 42)">
    <path d="M0 0h6v6H0zm10 0h6v6h-6zm10 0h6v6h-6zM0 10h6v6H0zm10 0h6v6h-6zm10 0h6v6h-6z" fill="#7aa2f7" opacity="0.6"/>
  </g>
  
  <!-- Text content -->
  <g transform="translate(65, 0)">
    {text_elements}
    <text x="0" y="{author_y}" fill="#ff9e64" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="13" font-weight="bold">
      — {quote["author"]}
    </text>
  </g>
</svg>
"""
    # Ensure assets folder exists
    os.makedirs("assets", exist_ok=True)
    with open("assets/developer-quote.svg", "w", encoding="utf-8") as f:
        f.write(svg_content)
    print("Successfully generated assets/developer-quote.svg")

if __name__ == "__main__":
    generate_svg()
