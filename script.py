from translate import Translator


translator = Translator(to_lang="french")


try:
    with open('./test.txt', mode='r') as my_file:
        text = (my_file.read())
        translation = translator.translate(text)
        with open('./translated.txt', mode='w') as my_file2:
            my_file2.write(translation)

except FileNotFoundError as err:
    print('file does not exsit')
