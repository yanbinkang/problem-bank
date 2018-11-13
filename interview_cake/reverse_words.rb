def reverse_words(message)
  reverse_characters(message, 0, message.length-1)

  current_word_start_index = 0

  for i in 0..message.length do
    if (message[i] == ' ' or (i == message.length))
      reverse_characters(message, current_word_start_index, i-1)
      current_word_start_index = i + 1
    end
  end

  return message
end

def reverse_characters(message, front_index, back_index)
  while front_index < back_index
    message[front_index], message[back_index] = \
        message[back_index], message[front_index]

    front_index += 1
    back_index -= 1
  end

  message
end

# puts reverse_words('the eagle has landed')
p reverse_words('boys love girls')
p reverse_words('')
p reverse_words('a')

