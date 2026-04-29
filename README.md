Language: 　**English**　|　[日本語](./README_jp.md)

# FBAC Locale Data Repository

This repository contains the locale data (translations used for messages and UI) used by the [Figura Blue Archive Crafters (FBAC)](https://github.com/Gakuto1112/FiguraBlueArchiveCrafters) avatars.
FBAC avatars access the resources in this repository from the runtime environment to display localized texts in the game.

## Repository Data Structure

The data stored in this repository is broadly divided into three main parts.

### index.json

This file contains information such as the "locale data version" and "supported languages".
FBAC avatars first fetch this file to determine whether to use the cache or download new locale data.

In the `localeVersion` field, the version of the locale data is described using Semantic Versioning.
Be sure to prefix it with a "v".
FBAC avatars compare the version of the cached translation data with this field. If the version here (remote) is newer, it discards the cache and reloads from the remote.

In the `availableLocales` field, the supported languages are stored in a Key-Value format, with the in-game language ID as the key and the language's display name as the value.
The in-game language ID can be obtained by installing [Figura](https://modrinth.com/mod/figura) and executing the following command for your current language:

```mcfunction
/figura run print(client:getActiveLang())
```

The value represents the display name in the game's language settings page.
However, this value is currently unused.

![Game language settings page](./readme_images/locale_settings.jpg)

### src/core/

Contains the locale data related to the core parts of the FBAC avatar.
The file name will be "${inGameLanguageID}.json".
The in-game language ID is the same as the one used in "[index.json](#indexjson)".

Inside the json file, data is stored in a Key-Value format, with the translation key (message ID) as the key and the translated text as the value.

### src/avatars/

Contains the locale data related to the avatar-specific parts of the FBAC avatar.
Translations for character names and [Ex Skill](https://github.com/Gakuto1112/FiguraBlueArchiveCrafters/blob/main/README.md#ex-skill) names are also stored here.
Within this directory, there are subdirectories named after character IDs, and inside those exist locale data json files just like in "[src/core/](#srccore)".
The naming convention for character subdirectories is identical to [FBAC's character-specific resources](https://github.com/Gakuto1112/FiguraBlueArchiveCrafters/tree/main/build_scripts#character-specific-part).
Furthermore, the naming convention for the json files and their internal structure are the same as in "[src/core/](#srccore)".
