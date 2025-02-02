def solution(s):
  answer = False
  s = s.upper()
  p_count = 0
  y_count = 0

  for c in s:
      if(c == 'P'):
          p_count += 1
      if(c == 'Y'):
          y_count += 1

  if(p_count == y_count):
      answer = True
  else:
      answer = False
  return answer