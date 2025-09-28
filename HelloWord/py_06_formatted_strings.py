# formatted_strings -> dynamically generate some texts with your variables.
# let's say the  two parts of name we have
name = 'acheson'
first_name = 'dan'
# not a good method
message = name + ' [' + first_name +'] is a coder'
# prefixed with f, formatted string, use curly braces to dynamically insert values into your strings.
# mes = f'{}'
mes = f'{name} [{first_name}] is a coder!!!'
print(message)
print(mes)
