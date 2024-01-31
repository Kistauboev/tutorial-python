Messi={'lambo', 'pagani', 'tesla'}
Ronaldo={'chiron', '911 gts', 'regera'}  # SET-{}
Messi.update(Ronaldo)
print(Messi)

Messi={'lambo', 'pagani', 'tesla'}
Ronaldo=['chiron', '911 gts', 'regera']  # LIST-[]
Messi.update(Ronaldo)
print(Messi)


Messi={'lambo', 'pagani', 'tesla'}
Ronaldo=['chiron', '911 gts', 'regera']
Neymar=('maybach', 'huracan', 'zonda')  # TUPLE-()
Messi.update(Ronaldo)
Messi.update(Neymar)
print(Messi)
