Den här repositoriet är organiserat för en länkad wiki‑känsla som fungerar med Obsidian/Anki‑stilens wikilänkar `[[fil|etikett]]`. Varje struktur/organ har en egen fil i singular. Använd alias/etikett för plural i texten: `[[muskel|muskler]]`.

## Mappstruktur
- `anatomi/` – strukturer i makroanatomi
  - `muskler/`, `ben/`, `leder/`, `kärl/`, `nerver/`, `organ/`, `regioner/`
- `histologi/` – vävnader, mikroskopiska strukturer, preparat
- `bok/histologi/` – kapitelstubbar som pekar till uppladdade kapitel (PDF/HTML)
- `mallar/` – återanvändbara mallar för nya sidor
- `index.md` – startsida och snabblänkar

## Namngivning
- Filnamn i singular, liten bokstav, bindestreck: `biceps-brachii.md`, `humerus.md`.
- En sida per begrepp. Flera synonymer/översättningar nämns i sidans front matter eller i ”AKA”.
- Länka med wikilänk och alias för böjningar, t.ex. `[[biceps-brachii|biceps brachii]]`, `[[muskel|muskler]]`.

## Länk‑konventioner
- Intern: `[[Anatomi/Muskler/Biceps Brachii|biceps brachii]]`
- Kapitel i histologiboken: `[[bok/histologi/Kap 05 Bindväv|Kapitel 5 – Bindväv]]`
- Senare, när kapitel‑PDF:er finns i `bok/histologi/pdf/`, uppdatera kapitelstubben med filväg.

## Snabbstart
1) Kopiera en mall från `mallar/` till relevant mapp.
2) Döp filen i singular (svenska/latin), fyll i sektionerna.
3) Lägg till ”Relaterat”‑länkar till närliggande sidor.
4) Länka till relevanta bokkapitel via `bok/histologi/…` stubbarna.

## Anki och webbläsare
- Obsidian/Anki: Wikilänkar `[[...]]` fungerar utmärkt direkt.
- Ren webbläsare: Vi kan senare lägga till enkel renderare eller konverteringsscript som gör `[[...]]` → vanliga Markdown‑länkar/HTML.

