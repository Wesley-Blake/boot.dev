import argparse
from book_bot import BookBot

def main():
    parser = argparse.ArgumentParser(
        prog='Book Bot',
        description=\
        '''
        Book Bot takes in plain text and returns a small analysis of the text.
        Count of words,
        Count of each letter.
        ''',
        epilog='This program was based on what you will find on boot.dev.'
    )

    parser.add_argument('filename')
    args = parser.parse_args()

    bot = BookBot(args.filename)
    print("="*10 + " BOOKBOT " + "="*10)
    print(f"From file: {args.filename}")
    print("-"*10 + " Word Count " + "-"*6)
    print(f"Found words: {bot.num_words()}")
    print(f"Found unique words: {bot.num_unique_words()}")
    print("="*10 + " Character Count " + "="*3)
    bot.print_characters()


if __name__ == '__main__':
    main()
