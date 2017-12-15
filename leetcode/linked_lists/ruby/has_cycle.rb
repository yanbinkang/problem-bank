require_relative 'linked_list'

def has_cycle(head)
  fast = head
  slow = head

  while fast && fast.next
    slow = slow.next
    fast = fast.next.next

    if fast == slow
      return true
    end
  end

  return false
end
