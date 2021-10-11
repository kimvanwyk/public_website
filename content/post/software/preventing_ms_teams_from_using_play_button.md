---
date: "2021-10-11"
tags: ["msteams", "wth"]
title: "Preventing MS Teams from invoking the calling tone or worse when resuming media playback"
---

Desktop versions of MS Teams has had a jaw-droppingly stupid bug [for more than a year](https://answers.microsoft.com/en-us/msteams/forum/all/teams-and-media-keys/136320bb-7af0-4bdc-8743-56608ff576b2?page=2) - pushing the *play* media key causes Teams to either invoke a call tone without calling anyone (bafflingly stupid) or call back the group or individual you've just been meeting with (embarrassing and aggressively antagonistic towards the poor user). This looks to be because Teams registers itself as a media player through the Electron framework it is built on. Why that means playing an empty call tone makes sense is beyond my understanding. Why it hasn't and likely will never be fixed is a rant for a different day, along with other unflattering and somewhat unprintable opinions I hold about MS Teams and its (sheer lack of) feature set compared to other chat and meeting software.

To fix it, I followed the advice [here](https://microsoftteams.uservoice.com/forums/555103-public/suggestions/39956326-media-keys-affecting-teams-web-app). On my Linux box:

* Open **/usr/share/applications/teams.desktop** as the root user
* Modify the *Exec=teams %U* entry in the **[Desktop Entry]** section to be *Exec=teams -disable-features=HardwareMediaKeyHandling %U*
* Restart Teams
* Optionally, shake head sadly

I also have a suspicion that Teams overwrote my above change in an update, so I've also taken this step. As of 11 Oct '21 I don't know if it's helped yet:

```bash
chmod ugo-w /usr/share/applications/teams.desktop
```


