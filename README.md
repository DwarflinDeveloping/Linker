In other languages: [Deutsch](https://gist.github.com/DwarflinDeveloping/3dd8f1a76e0c99f61179dab993728a0b)

# About Linker
Linker is a Discord Bot written in [Python](https://www.python.org/), which makes it possible to send links in a very short time.

# General functions
By bracketing a word with "{" and "}", the bot automatically generates a link from the URL specified by the guild.

<img src="https://cdn.discordapp.com/attachments/822481246097113118/824293121964900372/Usage1.png" width="350px" />

By adding a "$" in front of the word it is possible to display some information from the website.

<img src="https://cdn.discordapp.com/attachments/822481246097113118/824295598433501195/Usage3.png" width="350px" />

It is also possible to use a different url than the default url for a search. The search term and the URL must be separated by a ":".

<img src="https://cdn.discordapp.com/attachments/822481246097113118/824301631247482900/Usage4.png" width="350px" />

# Commands

**%guildfamily**<br>
```%guildfamily get``` – Outputs the default url from this guild<br>
```%guildfamily set <url>``` – Sets the guild's default url to the given url<br>
```%guildfamily clear``` – Deletes the default url of the guild

**%userfamily**<br>
```%userfamily get``` – Outputs your default url<br>
```%userfamily set <url>``` – Sets your default url to the given url<br>
```%userfamily clear``` – Deletes your default url

# Command usage

**%guildfamily set**<br>
This command allows to set the guild's default url. This url is used as a base to define the link by appending `%ARTICLE%`.<br>
When searching, `%ARTICLE%` is replaced by the search term.

At the english Wikipedia it would look like this: ```%guildfamily set https://en.wikipedia.org/wiki/%ARTICLE%```<br>
For the English Minecraft Wiki it would look like this: ```%guildfamily set https://minecraft.fandom.com/wiki/%ARTICLE%```

This principle can be applied to almost every wiki or forum.
