import re
import sys

def find_embedded_scripts(file_path):
    script_patterns = [
        r'<script[^>]*>.*?</script>',
        r'on(click|dblclick|mousedown|mouseup|mouseover|mousemove|mouseout|mouseenter|mouseleave|keydown|keypress|keyup|load|unload|submit|reset|focus|blur|change|select|error)=',
        r'Worker\([^)]*\)',
        r'importScripts\([^)]*\)',
        r'\.postMessage\([^)]*\)',
        r'\b(?:WASM|asm)\.Instance\b',
        r'CryptoJS\.',
        r'\b(?:cryptonight|hashimoto|ethash|scrypt|keccak)\b',
        r'\b(?:coinhive|mineralt|crypto-loot|jsecoin)\b',
    ]
    
    compiled_patterns = [re.compile(pattern, re.IGNORECASE) for pattern in script_patterns]
    suspicious_lines = []

    with open(file_path, 'r', encoding='utf-8', errors='replace') as file:
        for line_number, line in enumerate(file, start=1):
            for pattern in compiled_patterns:
                match = pattern.search(line)
                if match:
                    start = max(match.start() - 100, 0)
                    end = min(match.end() + 100, len(line))
                    context = line[start:end].strip()
                    suspicious_lines.append((line_number, context))
                    break

    return suspicious_lines

def main():
    if len(sys.argv) < 2:
        print('Usage: python script_sniffer.py <sql_dump_file>')
        sys.exit(1)

    file_path = sys.argv[1]
    suspicious_lines = find_embedded_scripts(file_path)

    if suspicious_lines:
        print('Potentially embedded scripts found:')
        for line_number, context in suspicious_lines:
            print(f'  Line {line_number}: {context}')
    else:
        print('No potentially embedded scripts found.')

if __name__ == '__main__':
    main()

