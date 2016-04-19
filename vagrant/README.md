This vagrant script will let you quickly bootstrap the NHDNUG website on any environment using VirtualBox. 
It is based on the following blog post: [Vagrant, Jekyll and Github Pages for streamlined content creation](http://kappataumu.com/articles/vagrant-jekyll-github-pages-streamlined-content-creation.html).

Getting started is straightforward:

```
$ git clone https://github.com/NHDNUG/nhdnug.github.io.git
$ cd nhdnug.github.io/vagrant
$ vagrant up
```

That's all there is to it. Now you can:

1. Access your website by browsing to `http://localhost:4000`.
2. Edit files locally, inside the `nhdnug.github.io` folder.
3. Simply `vagrant up` directly in the future to start the guest (no bootstraping needed).

Jekyll will: 

1. Recompile everything when changes are detected.
2. Log all activity in `/home/vagrant/jekyll.log`.
3. Automatically start serving your repo on every `vagrant up`.

