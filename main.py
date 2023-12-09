

with open('./Input/Names/invited_names.txt') as names:
    for name in names.readlines():
        with open('./Input/Letters/starting_letter.txt') as file_letter:
            letter = file_letter.read()
            file_name = name.replace('\\n', " ")
            new_letter = letter.replace("[name]", file_name.strip())
            with open(f'./Output/ReadyToSend/letter_for_{file_name.strip()}.txt', mode='w') as new_letters:
                new_letters.write(new_letter.strip())

