# #1
# a
# NUM = input()
#
# if NUM mod 2 = 0 then
#    output "Integer Value = ", NUM / 2, "Remainder Value = ", 0
# else if NUM mod 2 = 1 then
#    NUM = NUM - 1
#    output "Integer Value = ", NUM / 2, "Remainder Value = ", 1
# end if
#
# b
#  NUM = input()
#  zeros = 8
#
#  loop until NUM = 1 OR NUM = 0
#     mod_value = NUM mod 2
#     NUM = (NUM - mod_value) / 2
#     output mod_value
#     zeros = zeros - 1
#  end loop
#
#  output NUM
#
#  loop from 2 to zeros
#     output "0"
#  end loop
#
# c
#   NUM = input()
#   zeros = 8
#   a = new Array()
#   index = 8
#
#   loop until NUM = 1 OR NUM = 0
#      mod_value = NUM mod 2
#      NUM = (NUM - mod_value) / 2
#      output mod_value
#      a[index] = mod_value
#      index = index - 1
#      zeros = zeros - 1
#   end loop
#   a[index] = NUM
#   output NUM
#
#   loop from 2 to zeros
#      output "0"
#   end loop
#
#   loop x from 0 to (index-1)
#      a[x] = 0
#   end loop
#
#   output a
#
# #2
# a
# NUM = input()
#
#  loop until NUM = 1
#      if NUM mod 2 = 0 then
#          NUM2 = NUM / 2
#          NUM = NUM / 2
#          output NUM2
#      else if NUM mod 2 = 1 then
#          NUM1 = (NUM * 3) + 1
#          NUM = (NUM * 3) + 1
#          output NUM1
#      end if
#
#  end loop
#
# b
# NUMS = new Collection()
# NUM = input()
#
#  loop until NUM = 1
#      if NUM mod 2 = 0 then
#          NUM2 = NUM / 2
#          NUM = NUM / 2
#          output NUM2
#          NUMS.addItem(NUM2)
#      else if NUM mod 2 = 1 then
#          NUM1 = (NUM * 3) + 1
#          NUM = (NUM * 3) + 1
#          output NUM1
#          NUMS.addItem(NUM1)
#      end if
#  end loop
#
#  loop while NUMS.hasNext()
#      NUM3 = NUMS.getNext()
#      output NUM3
#  end loop
#
# c
# NUMS = new Collection()
# NUMUM = new Array()
# NUM = input()
# N = 0
#
#  loop until NUM = 1
#      if NUM mod 2 = 0 then
#          NUM2 = NUM / 2
#          NUM = NUM / 2
#          output NUM2
#          NUMS.addItem(NUM2)
#      else if NUM mod 2 = 1 then
#          NUM1 = (NUM * 3) + 1
#          NUM = (NUM * 3) + 1
#          output NUM1
#          NUMS.addItem(NUM1)
#      end if
#  end loop
#
#  loop while NUMS.hasNext()
#      NUM3 = NUMS.getNext()
#          if NUM3 mod 5 = 0 then
#              NUMUM[N] = NUM3
#              N = N + 1
#          end if
#  end loop
#
#  output NUMUM
#
# #3
# a
# NAME = ["Phoebe", "Melody", "Taylor", "Yvonne"]
# NAME1 = ["Adolph", "Darwin", "Holmes", "Renner"]
#
# method firstLetter(s)
#     return s.substring(0, 3)
# end method
#
# method lastLetter(s)
#     return s.substring(3, 6)
# end method
#
# loop I from 0 to 4
#     output firstLetter( NAME[I] ), lastLetter( NAME[I] )
#     output firstLetter( NAME1[I] ), lastLetter( NAME1[I] )
# end loop
#
# b
#  NAME = ["Phoebe", "Melody", "Taylor", "Yvonne"]
#  NAME1 = ["Adolph", "Darwin", "Holmes", "Renner"]
#  STACK = new Stack()
#
#  method firstLetter(s)
#      return s.substring(0, 3)
#  end method
#
#  method lastLetter(s)
#      return s.substring(3, 6)
#  end method
#
#  loop x from 0 to 3
#      STACK.push(firstLetter(NAME[x]))
#      STACK.push(lastLetter( NAME1[x] ))
#      STACK.push(firstLetter( NAME1[x] ))
#      STACK.push(lastLetter( NAME[x] ))
#  end loop
#
# c
#  NAME = ["Phoebe", "Melody", "Taylor", "Yvonne"]
#  NAME1 = ["Adolph", "Darwin", "Holmes", "Renner"]
#  STACK = new Stack()
#  NEW_NAMES = new Collection()
#
#  method firstLetter(s)
#      return s.substring(0, 3)
#  end method
#
#  method lastLetter(s)
#      return s.substring(3, 6)
#  end method
#
#  loop x from 0 to 3
#      STACK.push(lastLetter( NAME[x] ))
#      STACK.push(firstLetter(NAME1[x]))
#      STACK.push(lastLetter( NAME1[x] ))
#      STACK.push(firstLetter( NAME[x] ))
#  end loop
#
#  loop until STACK.isEmpty()
#      NAM1 = STACK.pop()
#      NAM2 = STACK.pop()
#      output NAM1, NAM2
#      NEW_NAMES.addItem(NAM1)
#      NEW_NAMES.addItem(NAM2)
#  end loop