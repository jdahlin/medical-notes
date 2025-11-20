
```
#!/Users/johandahlin/Library/Application Support/AnkiProgramFiles/.venv/bin/python
from anki.collection import Collection
c = Collection("/Users/johandahlin/Library/Application Support/Anki2/User 1/collection.anki2")
for deck_name in c.decks.all_names():
    if not deck_name.startswith("Biokemi::Johan D"):
         continue
    deck_name = deck_name.replace("Johan D::", "")
    deck_name = deck_name.replace("::", "_")
    deck_id = c.decks.id_for_name(d)
    c.export_anki_package(
        out_path=f"/tmp/{deck_name}.apkg", 
        options=ExportAnkiPackageOptions(with_media=True), 
        limit=DeckIdLimit(deck_id),
    )
```

TODO
- Update script to run rsync to moln
	- Update Caddyfile to [serve static files](https://caddyserver.com/docs/caddyfile/directives/file_server), perhaps with index
- Generate obsidian page with links to anki that can be downloaded
	- how do we insert dynamic content?
- low prio: run it automatically (do we want to?)