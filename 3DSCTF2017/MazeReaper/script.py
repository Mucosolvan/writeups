from pwn import *

p = connect('maze01.3dsctf.org', 8002)

p.recvline()
p.clean()

p.sendline('start')
sleep(1)

p.recvline()
p.recvline()

for i in range(50):
	print p.recvline().strip()
	n, m, k, d = map(int, p.recvline().split())
	a, b = map(int, p.recvline().split())

	graph = [[] for i in range(n)]
	keys = [[] for i in range(n)]
	doors = [[] for i in range(n)]

	for i in range(m):
		fr, to = map(int, p.recvline().split())
		graph[fr].append(to)
		graph[to].append(fr)

	for i in range(k):
		num, key = p.recvline().split()
		keys[int(num)].append(key)

	for i in range(d):
		num, key = p.recvline().split()
		doors[int(num)].append(key)

	p.recvline()

	state = [0 for i in range(26)]
	states = [[] for i in range(n)]
	states[a].append(state[:])
	q = [(a, 0, state)]
	ans = -1
	while q != []:
		v, dist, state = q[0]
		if v == b:
			ans = dist
			break

		q.pop(0)
		for key in keys[v]:
			state[ord(key) - ord('a')] = 1

		for u in graph[v]:
			cp_state = state[:]
			pom = True

			for door in doors[u]:
				if not cp_state[ord(door) - ord('A')]:
					pom = False
					break

			if pom and not cp_state in states[u]:
				states[u].append(cp_state)
				q.append((u, dist + 1, cp_state))

	p.sendline(str(ans))
	sleep(1)
	print p.recvline().strip()
	print p.recvline()
