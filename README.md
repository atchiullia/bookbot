## 📚 BookBot

BookBot is my first [Boot.dev](https://www.boot.dev) project!

---

**BookBot** is a simple Python program that analyzes a text file (such as a book from [Project Gutenberg](https://www.gutenberg.org/)) and outputs statistics like word count and character frequency.

---

### 🚀 Features

* Word count for the entire document
* Frequency count of each character (case-insensitive)
* Sorted character statistics
* Command-line interface to specify the book to analyze

---

### 🛠 Requirements

* Python 3.x

---

### 📂 Project Structure

```
bookbot/
├── books/
│   ├── frankenstein.txt
│   ├── mobydick.txt
│   └── prideandprejudice.txt
├── main.py
├── stats.py
└── README.md
```

---

### 🧠 Usage

1. Clone this repository:

```bash
git clone https://github.com/your-username/bookbot.git
cd bookbot
```

2. Run the program with a path to a book file:

```bash
python3 main.py books/frankenstein.txt
```

3. Example output:

```
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found 74352 total words
--------- Character Count -------
a: 4621
b: 1230
c: 2119
...
============= END ===============
```

---

### 📝 Add Your Own Books

1. Download books from [Project Gutenberg](https://www.gutenberg.org/).
2. Save them in the `books/` directory.
3. Run the script with the new book:

```bash
python3 main.py books/yourbook.txt
```

---

### 📄 License

MIT License – do whatever you want, just give credit.

