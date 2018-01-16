inp = input()
add = lambda y, z: y + (z ^ 21);
results = {
	False:lambda:print('Almost!!'),
	True:lambda:print('Correct!')
}

revList = [160,155,208,160,190,215,237,134,210,126,212,222,224,238,128,240,164,213,183,192,162,178,163,162][::-1]
results[
 [add(*element)
  for element in zip(list(map(ord,inp)), list(map(ord,inp))[::-1])] == revList
  and 'mo4r' in inp and '34C3_' in inp and inp.split('_')[3] == 'tzzzz']()

