# aiHiringQuizWeb
Files:
- static: folder for pictures used on this web application
- templates: files for pages on ths web application
    - about.html: introduction of this application(informative page)
    - aihiring.html: introduction of ai-hiring(informative page)
    - base.html: UI template for every page(functional page)
    - cases.html: case studies(informative page)
    - dilemmas.html: ethical dilemmas(informative page)
    - index.html: cover page where the maze is(interactive page)
    - solutions.html: solutions of the ethical dilemmas(informative page)
    - sources.html: academic sources for readers(informative page)
- app.py: backend file written with python(flask)

Used languages:
- python
- javascript
- css
- html

Required python libraries: flask

How to run this application(try one of the two):
- click the "RUN" button on VS Code 
    --> search the url(like: http://127.0.0.1:5006) shown in the terminal on your browser
- type "flask run app.py" on your terminal(this may not work on some computer)
    --> search the url(like: http://127.0.0.1:5006) shown in the terminal on your browser

ps: 
- the maze includes more than 50 questions. But for each round, 10 of them are randomly distributed in the game.
- the output of the game is based on users' score for each metric(so it's not the same when you make different choices every round). 
- questions in the maze were designed after reading materials in the "SOURCES" page and careful considerations.
- feel free to ask by emailing 14806762@uva.nl
