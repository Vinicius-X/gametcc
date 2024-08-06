# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define d = Character("Dinah Moraes")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene cenario

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show Dinah normal

    # These display lines of dialogue.

    d "A francisquinha pega o penico e joga mijo na filomena."

    d "E o gepeto com a chiquinha só leva chifre e não aprende"

    d "O matozão deve pensão tem que vender os garrafão."

    # This ends the game.

    return
