# NHDNUG.org

Welcome to the repository home for North Houston .NET User Group's website.

We allow contribution to our site... In fact, we encourage it!!!

If you'd like to make a change, please, make a pull request.

There's a couple things you should probably read though - especially if you're developing on Windows:
* [Run Jekyll on Windows](http://jekyll-windows.juthilo.com/) - This will get you up and running with the GitHub Pages framework. Very Helpful.
* [Jeckyll Docs](http://jekyllrb.com/) All the info you need to get productive in jekyll
* [GitHub Flavored Markdown Cheatsheat](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) - As nice as MD is, GFM is even nicer. This'll give you the syntax cheats.
* [Kramdown](http://kramdown.gettalong.org/quickref.html) - There are a few minor things that Kramdown makes easier - mostly code blocks. Don't know that they'll ever be needed, but if they are, it's nice to have a link here.

If you at least skim the cheat sheet - and follow along with what's going on in the rest of the source - you should be good to go. If you have any big changes you want to make, just make a pull request. Chances are, it'll be fine!

If you just want to give clone and run it, give it a try! That first site will get all the pre-reqs moving, all you have to do is hit the "servesite.bat" file, and you can see your changes as you make them. Have fun!

## Important when working with this Repo

Gh-pages (what hosts this site) is case-sensitive. As such, make sure your local git repo is set to be case sensitive.

```
git config core.ignorecase false
```

## Authoring Guide

### Adding a Speaker

1. Add a picture of the speaker (if not already present) to the images/persons directory.
2. Resize the picture of the speaker to **350x350** pixels.
3. Copy last month's speaker file from the _persons directory and paste it back into the _persons directory.
4. Rename this pasted file in the format {first}-{last}.md (lower case)
5. Adjust the metadata in the file as appropriate.

### Adding a Sponsor

1. Add the sponsor's logo (if not already present) to the images/sponsors directory.
2. Resize the sponsor log to a size with a **width of 350px** (height can be taller or shorter)
3. Copy an existing sponsor file from the _sponsors directory and paste it back into the _sponsors directory.
4. Rename this pasted file in the format {sponsor-name}.md (lower case)
5. Adjust the metadata in the file as appropriate.

## New Meetings

1. Copy last's month's meeting file from _posts and paste it back into the same directory.
2. Rename this pasted file in the format {year}-{month}-{day}-{Title-Here}.md
3. Adjust the metadata in the file as appropriate.


### Copyright and license

This repo's source code is licensed under the [MIT license](/LICENSE).

