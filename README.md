# SQL-Database-Scanner

SQL-Database-Scanner is a lightweight Python script that scans SQL dump files for potentially embedded scripts, such as XSS, web miners, and other malicious scripts. It uses regular expressions to identify suspicious patterns and reports the line numbers where they are found.

**Disclaimer**: This tool is designed for educational and informational purposes only. It is not a comprehensive solution for identifying all embedded scripts or potential security vulnerabilities. For a more robust security analysis, consider using professional tools and methodologies.

## Prerequisites

- Python 3.x

## Usage

1. Run the script using the command line, providing the SQL dump file as an argument:

```bash
python scan.py <sql_dump_file>
```

The tool will output potentially embedded scripts found on the specified lines.

## Limitations

* The script uses simple regular expressions to identify suspicious patterns, which may not cover all embedded scripts or potential security vulnerabilities. It may also produce false positives.
 * The script assumes the SQL dump file is UTF-8 encoded. If the file uses a different encoding, you may need to modify the script to handle it correctly.

## Contributing

Contributions to improve the tool are welcome. Please submit a pull request or open an issue to discuss potential improvements or bug fixes.
