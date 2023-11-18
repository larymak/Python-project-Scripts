class JSONLexer:
    def __init__(self, json_string):
        self.json_string = json_string
        self.tokens = []
        self.current_position = 0

    def tokenize(self):
        if len(self.json_string) > 0:
            while self.current_position < len(self.json_string):
                current_char = self.json_string[self.current_position]

                if current_char.isspace():
                    self.current_position += 1
                elif current_char == "{":
                    self.tokens.append(("LBRACE", "{"))
                    self.current_position += 1
                elif current_char == "}":
                    self.tokens.append(("RBRACE", "}"))
                    self.current_position += 1
                elif current_char == "[":
                    self.tokens.append(("LBRACKET", "["))
                    self.current_position += 1
                elif current_char == "]":
                    self.tokens.append(("RBRACKET", "]"))
                    self.current_position += 1
                elif current_char == ",":
                    self.tokens.append(("COMMA", ","))
                    self.current_position += 1
                elif current_char == ":":
                    self.tokens.append(("COLON", ":"))
                    self.current_position += 1
                elif current_char.isdigit() or current_char == "-":
                    number, success, consumed = self.lex_number()
                    if success:
                        self.tokens.append(("NUMBER", number))
                        self.current_position += consumed
                    else:
                        print(f"Error Tokenizing: {number}")
                        return 1
                elif current_char == '"':
                    str, success, consumed = self.lex_string()
                    if success:
                        self.tokens.append(("STRING", str))
                        self.current_position += consumed
                    else:
                        print(f"Error Tokenizing: {str}")
                        return 1
                elif self.json_string.startswith("true", self.current_position):
                    self.tokens.append(("TRUE", "true"))
                    self.current_position += 4
                elif self.json_string.startswith("false", self.current_position):
                    self.tokens.append(("FALSE", "false"))
                    self.current_position += 5
                elif self.json_string.startswith("null", self.current_position):
                    self.tokens.append(("NULL", "null"))
                    self.current_position += 4
                else:
                    print(f"Unexpected character: {current_char}")
                    return 1

            return self.tokens
        else:
            return 1

    def lex_string(self):
        start_index = self.current_position + 1
        chars_count = 2  # Includes the opening and closing quotes
        str_ = ""
        escaped = False

        for char in self.json_string[start_index:]:
            if char == "\\" and not escaped:
                escaped = True
            elif char == '"' and not escaped:
                return str_, True, chars_count
            elif escaped and char not in ["\\", '"', "b", "f", "n", "r", "t", "u", "/"]:
                break
            elif char in ["\t", "\n"]:
                break
            else:
                escaped = False

            str_ = str_ + char
            chars_count += 1

        return str_, False, chars_count

    def lex_number(self):
        start_index = self.current_position
        chars_count = 0
        num_string = ""

        # Check for number starting with 0 which is not a float
        if len(self.json_string[start_index:]) > 1:
            if self.json_string[start_index] == "0" and self.json_string[
                start_index + 1
            ] not in [".", ","]:
                return num_string, False, chars_count

        for char in self.json_string[start_index:]:
            if not char.isdigit() and char not in ["-", ".", "e", "E", "+"]:
                break
            num_string = num_string + char
            chars_count += 1

        try:
            num = (
                int(num_string)
                if "." not in num_string and "e" not in num_string.lower()
                else float(num_string)
            )
            return num, True, chars_count
        except ValueError:
            return num_string, False, chars_count


class JSONParser:
    def __init__(self, json_string):
        self.tokens = JSONLexer(json_string).tokenize()
        self.current_token = None
        self.current_index = 0

    def parse(self):
        if self.tokens == 1:
            print(f"Error Parsing: Token: {self.current_token} Err: Not JSON")
            return 1
        else:
            self.current_token = self.tokens[0]

            if self.current_token[0] not in ["LBRACE", "LBRACKET"]:
                print(f"Error Parsing: Token: {self.current_token} Err: Not JSON")
                return 1
            else:
                result = self.parse_value()

                # Check if values exist after closing brace or bracket
                if self.current_index + 1 != len(self.tokens):
                    return 1
                else:
                    return result

    def parse_value(self):
        if self.current_token[0] == "STRING":
            return 0
        elif self.current_token[0] == "FALSE":
            return 0
        elif self.current_token[0] == "TRUE":
            return 0
        elif self.current_token[0] == "NULL":
            return 0
        elif self.current_token[0] == "NUMBER":
            return 0
        elif self.current_token[0] == "LBRACE":
            return self.parse_object()
        elif self.current_token[0] == "LBRACKET":
            return self.parse_array()
        else:
            return 1

    def parse_object(self):
        self.next_token()  # Move past the brace token

        while self.current_token != None and self.current_token[0] != "RBRACE":
            if self.current_token[0] == "STRING":
                self.next_token()
            else:
                print(f"Error Parsing: Token: {self.current_token} Err: Key Error")
                return 1

            if self.current_token[0] == "COLON":
                self.next_token()
            else:
                print(f"Error Parsing: Token: {self.current_token} Err: Colon Error")
                return 1

            if self.parse_value() == 0:
                self.next_token()
            else:
                print(f"Error Parsing: Token: {self.current_token} Err: Value Error")
                return 1

            res = self.parse_comma()
            if res == 1:
                print(f"Error Parsing: Token: {self.current_token} Err: Extra Comma")
                return 1

        if (
            "COMMA" not in self.tokens[self.current_index - 1]
            and self.current_token != None
        ):
            return 0
        else:
            print(f"Error Parsing: Token: {self.current_token} Err: Missing Values")
            return 1

    def parse_array(self):
        self.next_token()  # Move past the bracket token

        while self.current_token != None and self.current_token[0] != "RBRACKET":
            if self.parse_value() == 0:
                self.next_token()
            else:
                print(f"Error Parsing: Token: {self.current_token} Err: Value Error")
                return 1

            res = self.parse_comma()
            if res == 1:
                print(f"Error Parsing: Token: {self.current_token} Err: Extra Comma")
                return 1

        if (
            "COMMA" not in self.tokens[self.current_index - 1]
            and self.current_token != None
        ):
            return 0
        else:
            print(f"Error Parsing: Token: {self.current_token} Err: Missing Values")
            return 1

    def parse_comma(self):
        if self.current_token != None:
            if self.current_token[0] == "COMMA":
                self.next_token()

            return 0
        else:
            return 1

    # Move to next token
    def next_token(self):
        self.current_index += 1
        if self.current_index < len(self.tokens):
            self.current_token = self.tokens[self.current_index]
        else:
            self.current_token = None
