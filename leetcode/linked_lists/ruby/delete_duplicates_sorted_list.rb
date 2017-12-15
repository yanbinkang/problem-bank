require_relative 'linked_list'

def delete_duplicates(head)
  current = head
  previous = nil

  dict = {}

  while current
    if dict.keys.include?(current.val)
      previous.next = current.next
    else
      dict[current.val] = 1
      previous = current
    end

    current = current.next
  end

  return head
end
