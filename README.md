<h1>Simple webapp check words anagram</h1>

<h3>Single Page webapp that build with Python Flask and Vue.js</h3>


<h3>Prerequisites</h3>
<ul>
    <li>Python3.9+ installed on the machine </li>
</ul>

<h3>Run webapp without virtual env</h3>
<ul>
    <li>Flask installed on the machine (if not, run "pip install Flask" to install)</li>
    <li>cd anagram_webapp</li>
    <li>run "python app.py"</li>
    <li>server should be running on http://127.0.0.1:5000/</li>
</ul>

<h3>Run webapp with virtual env</h3>
<ul>
    <li>virtualenv installed (if not, run "pip install virtualenv")</li>
    <li>cd anagram_webapp</li>
    <li>run "virtualenv virtual" create virtual env</li>
    <li>run ". virtual/bin/activate" to activate it</li>
    <li>(virtual) run "pip install -r requirement"</li>
    <li>(virtual) run "python app.py"</li>
    <li>server should be running on http://127.0.0.1:5000/</li>
</ul>

<h3>Run unit test</h3>
<ul>
    <li>cd anagram_webapp</li>
    <li>run "python -m unittest"</li>
</ul>