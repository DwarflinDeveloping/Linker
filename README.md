In other languages: [Deutsch](https://gist.github.com/DwarflinDeveloping/3dd8f1a76e0c99f61179dab993728a0b)

# About Linker
Linker is a bot programmed in [Python](https://www.python.org/) which makes it possible to send links in a very short time.

# General functions
When a word is bracketed with "{" and "}", the bot generates a link completely automatically and sends it below the message.<br>
This is generated from the default URL set for the Discord server.<br>
A default URL consists of the base URL and the variable `%ARTICLE%`.
The variable is replaced by the search term entered between the curly brackets during a search.
For example, if you set the URL to `https://minecraft.fandom.com/wiki/%ARTICLE%`, all searches will be made on the English Minecraft wiki.

<img src="https://cdn.discordapp.com/attachments/822481246097113118/824293121964900372/Usage1.png" width="350px" />

By adding a "$" at the beginning of a word, it is possible to display quick information from the website.
However, some websites have this feature disabled, so this is usually only possible in wikis and forums.

<img src="https://cdn.discordapp.com/attachments/822481246097113118/824295598433501195/Usage3.png" width="350px" />

It is also possible to use a different URL than the default URL. For this, separate the search word and the base URL with a ":" from each other.
Everything before the colon is the base URL.

<img src="https://cdn.discordapp.com/attachments/822481246097113118/824301631247482900/Usage4.png" width="350px" />

It is also possible to use a template as the base URL. For instance `minecraft-en` refers to the English Minecraft wiki.
Here are all of these templates listed:

## templates

`minecraft-<WIKINAME>` - `https://minecraft.fandom.com/<WIKINAME>/wiki/%ARTICLE%`<br>
`wikipedia-<WIKINAME>` - `https://<WIKINAME>.wikipedia.org/wiki/%ARTICLE%`<br>
`fandom-<WIKINAME>` - `https://<WIKINAME>.fandom.com/wiki/%ARTICLE%`<br>
`gamepedia-<WIKINAME>` - `https://<WIKINAME>.gamepedia.com/%ARTICLE%`

`youtube` - `https://www.youtube.com/%ARTICLE%`<br>
`twitch` - `https://www.twitch.tv/%ARTICLE%`

# commands

**%guildfamily**<br>
`%guildfamily get` - Outputs the default url from this guild<br>
`%guildfamily set <url>` - Sets the guild's default url to the given url<br>
`%guildfamily clear` - Deletes the default url of the guild

**%userfamily**<br>
`%userfamily get` - Outputs your default url<br>
`%userfamily set <url>` - Sets your default url to the given url<br>
`%userfamily clear` - Deletes your default url

# command use

**%guildfamily set**<br>
When using this command it is possible to set the default URL of the server.
It is necessary to include the variable `%ARTICLE%` in this URL. In case of a search, `%ARTICLE%` will be replaced by the search term entered between the curly brackets.
If you do not want to build the URL yourself, you can also use the templates (see **Templates**).

Here the principle will be explained based on the Emglish Minecraft Wiki:<br>.
• If you use a template, the command will look like this: `%guildfamily set minecraft-en`<br>.
• If you want to compose it yourself, however, like this: `%guildfamily set https://en.wikipedia.org/wiki/%ARTICLE`

<img src="https://cdn.discordapp.com/attachments/805136929750122497/824701089164165130/Usage5.png" width="350px" />

This principle can be applied to almost all Wikis, forums and most websites.

**%userfamily set**<br>
This command is practically the same as `%guildfamily` with the difference that the default url of the guild is not set, but that of the user. Templates can be used here as well.

<img src="https://cdn.discordapp.com/attachments/805136929750122497/824704011550326805/Usage6.png" width="350px" />

**%guildwords**<br>
If this command is used, the custom words of the guild can be viewed and managed.<br>
Custom words are words that output a custom url when searched.

<img src="https://cdn.discordapp.com/attachments/805136929750122497/824709866681139250/Usage7.png" width="350px" />
