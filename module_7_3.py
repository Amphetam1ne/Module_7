class WordsFinder:

    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as f:
                content = f.read().lower()
                for i in punctuation:
                    content.replace(i, '')
                words = content.split()
                all_words[file_name] = words
        return all_words


    def find(self, word):
        word = word.lower()
        all_words = self.get_all_words()
        result = {}
        for file, words in all_words.items():
            if word in words:
                result[file] = words.index(word) + 1
        return result

    def count(self, word):
        word = word.lower()
        all_words = self.get_all_words()
        result = {}

        for file_name, words in all_words.items():
            result[file_name] = words.count(word)

        return result


file_name = 'test_file.txt'

content = '''It's a text for task Найти везде,
Используйте его для самопроверки.
Успехов в решении задачи!
text text text'''

with open(file_name, 'w', encoding='utf-8') as file:
    file.write(content)


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
