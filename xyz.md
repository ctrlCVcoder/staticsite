Deploy to the Internet
We're so close! We have one last step: to publish our site to the world wide web. (Yes, on a public domain and server)

GitHub Pages
GitHub Pages is a free service from GitHub that allows you to host static websites directly from a GitHub repository. Conveniently, you now have a static site generator!

That said, there are two limitations we're going to need to work around:

GitHub pages serves repo sites from https://ctrlCVcoder.github.io/staticsite/, which means that the "root" of our site will actually be at a subdirectory. We'll have to enhance our generator to handle that.
GitHub Pages needs the code committed to Git (at least by default) to deploy the site. So we'll have to break our "don't commit the generated site" rule.

Assignment
Right now our site always assumes that / is the root path of the site (e.g. http://localhost:8888/. Make it configurable by:
In main.py use the sys.argv to grab the first CLI argument to the program. Save it as the basepath. If one isn't provided, default to /.
Pass the basepath to the generate_pages_recursive and generate_page functions.
In generate_page, after you replace the {{ Title }} and {{ Content }}, replace any instances of:
href="/ with href="{basepath}
src="/ with src="{basepath}
Create a new build.sh script that builds the site for production:
The script is simple: python3 src/main.py "/staticsite/"
Your main.py is also used for local testing, so it will still need the default / baseurl
Run the new build script and ensure that the site is built correctly
Update your main.py to build the site into the docs directory instead of public. GitHub pages serves sites from the docs directory of your main branch by default.
Delete the public directory, and remove it from your .gitignore file.
Rebuild the site into the docs directory.
