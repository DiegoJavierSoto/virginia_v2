import re

def update_html():
    with open('c:\\Proyectos\\virginia_2\\index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    colors_replacement = '''"colors": {
                        "primary": "#93452a",
                        "primary-container": "#b15d40",
                        "primary-fixed": "#ffdbd0",
                        "on-primary": "#ffffff",
                        "surface": "#fcf9f4",
                        "surface-container-low": "#f6f3ee",
                        "surface-container": "#f0ede8",
                        "surface-container-highest": "#e5e2dd",
                        "surface-container-lowest": "#ffffff",
                        "on-surface": "#1c1c19",
                        "secondary-container": "#f4ded2",
                        "on-secondary-container": "#716158",
                        "secondary-fixed-dim": "#d7c3b7",
                        "outline-variant": "#dac1ba",
                        "on-surface-variant": "#53433f",
                        "outline": "#85736e",
                        "surface-variant": "#f4ded2",
                        "primary-fixed-dim": "#ffb59f",
                        "background": "#fcf9f4",
                        "secondary": "#716158"
                    }'''
    
    content = re.sub(r'"colors":\s*\{[^}]+\}', colors_replacement, content)

    if '"boxShadow"' not in content:
        content = content.replace('"colors":', '"boxShadow": {\n                        "ambient": "0px 12px 32px rgba(28, 28, 25, 0.06)"\n                    },\n                    "colors":')

    br_replacement = '''"borderRadius": {
                        "DEFAULT": "0.125rem",
                        "lg": "0.5rem",
                        "xl": "0.75rem",
                        "full": "9999px"
                    }'''
    content = re.sub(r'"borderRadius":\s*\{[^}]+\}', br_replacement, content)

    content = content.replace('bg-[#fcf9f4]/80', 'bg-surface/80')
    content = content.replace('text-[#4d614f]', 'text-primary')
    content = content.replace('dark:text-[#b7ccb6]', 'dark:text-primary-fixed')
    content = content.replace('hover:text-[#4d614f]', 'hover:text-primary')
    content = content.replace('bg-[#f6f3ee]', 'bg-surface-container-low')

    content = content.replace('bg-primary text-on-primary px-6 py-2.5 rounded-md', 'bg-gradient-to-br from-primary to-primary-container text-on-primary px-6 py-2.5 rounded-xl')
    content = content.replace('bg-primary text-on-primary px-8 py-4 rounded-md', 'bg-gradient-to-br from-primary to-primary-container text-on-primary px-8 py-4 rounded-xl')
    content = content.replace('bg-surface-container-lowest text-primary px-8 py-3 rounded-md', 'bg-surface-container-lowest text-primary px-8 py-3 rounded-xl')
    content = content.replace('class="bg-primary text-on-primary p-12 rounded-xl relative', 'class="bg-gradient-to-br from-primary to-primary-container text-on-primary p-12 rounded-xl relative')

    content = content.replace('shadow-2xl', 'shadow-ambient')
    content = content.replace('shadow-xl', 'shadow-ambient')
    content = content.replace('shadow-lg', 'shadow-ambient')
    content = content.replace('border border-outline-variant/10', '')
    content = content.replace('border-t border-outline-variant/20', '')

    with open('c:\\Proyectos\\virginia_2\\index.html', 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    update_html()
    print("HTML updated successfully.")
