require_relative 'linked_list'
# https://leetcode.com/problems/intersection-of-two-linked-lists/

def get_intersection(headA, headB)
  current_a, current_b = headA, headB
  len_a, len_b = 0, 0

  while current_a
    len_a += 1
    current_a = current_a.next
  end

  while current_b
    len_b += 1
    current_b = current_b.next
  end

  if len_a > len_b
    (len_a - len_b).times do
      current_a = current_a.next
    end
  elsif len_b > len_a
    (len_b - len_a).times do
      current_b = current_b.next
    end
  end

  while current_b != current_a
    current_b = current_b.next
    current_a = current_a.next
  end

  current_a
end
