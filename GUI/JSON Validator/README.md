# GUI JSON Validator

## Description

The GUI JSON Validator is a simple tool that allows you to validate JSON strings using a graphical user interface. It consists of two components: a JSON lexer and parser and a graphical interface for user interaction.

## Screenshot

**Valid JSON Screenshot**
[![Valid-JSON.png](https://i.postimg.cc/y8ngKCYZ/Valid-JSON.png)](https://postimg.cc/qNhMcYKJ)

**Invalid JSON Screenshot**
[![Invalid-JSON.png](https://i.postimg.cc/9fM4FgrN/Invalid-JSON.png)](https://postimg.cc/XrRNs8Kw)

## How to Use

1. **JSON Lexer and Parser:**
   - The `json_parser` module provides a JSON lexer and parser.
   - It can be used independently for programmatic JSON validation.

2. **GUI JSON Validator:**
   - The `JSONValidator` class provides a graphical user interface for JSON validation.
   - Run the `JSONValidator` class from the provided script to launch the GUI.
   - Input your JSON string in the text box and click the "Validate" button.
   - The result will be displayed in the information label.

## Dependencies

- The `json_parser` module is required for JSON parsing.
