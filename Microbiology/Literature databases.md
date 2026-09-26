
## PubMed

https://pubmed.ncbi.nlm.nih.gov/

**MeSH** - Medical Subject Heading; standartised keywords the articles are indexed by.
MeSH database - https://www.ncbi.nlm.nih.gov/mesh/
Can find definitions of MeSH terms and more/less specific terms to use.

Operators:
- `"text"` - encases a string of text, just writing text works as well.
- `(text)` - used to group a part of the search.
- `A AND B` - searches for both `A` and `B` at the same time.
- `A OR B` - searches for `A` or `B`.
- `A NOT B` - searches for `A` **and not** `B`; warning: `A AND (NOT B)` is not a thing!

You can add a type of the strings to search by.
- `[mesh]` - MeSH term.
- `[tiab]` - title/abstract; in case the article is new and MeSH terms have not been added yet.

Example search strings:
	`("bacteriophages"[mesh] AND "therapy"[tiab])`
	`("bacteriophages"[mesh] AND "therapy"[tiab] AND "overcoming"[tiab])`

**Systematic review** - critical summary of the research area; based on the articles from several databases.

## Embase

https://www.embase.com/

**Emtree** - subject headings indexing in Embase.

Uses a different format for search queries, but I'm too lazy to explain it.

There's a query translator from the PubMed format to the Embase format.

## Other

**Scopus** - citation database.
**Web of Science** - citation database.
**The library search tool** - books, articles, theses.
