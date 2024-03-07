def snake_to_camel(word):
        import re
        s=word.split("_")
        c=""
        for x in s:
                c+=x.capitalize()
        return c

print(snake_to_camel('python_exercises'))