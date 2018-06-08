import re

s="""
<html>
    <body style=&#39;background-color:#ffff>
        <h4>Click</h4>
        <a href='http://www.python.org'>Here</a>
        <p>
            To connect to the most powerful tools in the world.
        </p>
    </body>
</html>"""

ans=re.sub('<[^<]+?>','',s)
print(ans)