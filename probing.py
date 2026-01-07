
# Let's scan the context for clues using keyword searches and show snippets around matches def find._snippets(keyword, windo-200, mox_hits=10):
hits = O
for i, chunk in enumerate(context):
start = 0
while True:
idx = chunk.lower().find(keyword.lower(), start)if idx =- -1:
break
s - max(0, idx - window)
e = min(len(chunk), idx + len(keyword) + window)
hits.append((i,chunk[s:e]))if len(hits)>= max_hits:
retunn hits
start = idx + 1
return hits
keywords - ["dinengdeng", "pinakbet", "bagoong", "Agoo", "La Union", "festival", "beauty pageant", "Miss", “Dinengdeng Festival"门
results = ff
for kw in keywords:
results[ki] - find_snippets(km, windo-400, mox.hits=5)
for kw, hits in results.items):
print(f"ee= Keyword:fkwr =e-")if not hits:
print("No hits")for i, snip in hits:
print(f"[Chunk fi]...fsnipl...In")
