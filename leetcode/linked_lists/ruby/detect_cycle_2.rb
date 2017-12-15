require_relative 'linked_list'

# use hash, O(n) extra space
def detect_cycle(head)
  hash_map = {}

  while head
    if hash_map.keys.include?(head)
      return head
    end

    hash_map[head] = 0
    head = head.next
  end

  nil
end


def detect_cycle(head)
  return nil if head.nil?

  fast = slow = head

  while fast
    slow slow.next
    fast = fast.next

    return nil if fast.nil?

    fast = fast.next

    if fast == slow
      slow = head

      while slow != fast
        fast = fast.next
        slow = slow.next
      end

      return fast
    end
  end

  nil
end
