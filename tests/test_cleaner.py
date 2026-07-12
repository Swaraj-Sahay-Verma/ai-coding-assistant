from extractor.dom import create_dom, get_all_nodes
from extractor.cleaner import remove_unwanted_tags

html = """
<html>

<head>

<style>
body { color:red; }
</style>

<script>
alert("Hello");
</script>

</head>

<body>

<nav>
Home
About
</nav>

<main>

<h1>FastAPI</h1>

<p>
FastAPI is a modern Python framework.
</p>

</main>

<footer>
Copyright
</footer>

</body>

</html>
"""

soup = create_dom(html)

print("Before Cleaning:")

for tag in get_all_nodes(soup):
    print(tag.name)

remove_unwanted_tags(soup)

print("\nAfter Cleaning:")

for tag in get_all_nodes(soup):
    print(tag.name)