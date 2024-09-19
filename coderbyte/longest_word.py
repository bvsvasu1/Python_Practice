def LongestWord(sen):

  sen_list = sen.split(" ")
  word = ''
  max_size = 0
  for i in sen_list:
    #temp_word = "".join([char for char in i if char.isalpha()])
    temp_word = "".join([char for char in i if char.isalpha()])
    if len(temp_word)> max_size:
      max_size = len(temp_word)
      word = temp_word
  return word
  

# keep this function call here 
print(LongestWord("fun!!% time"))