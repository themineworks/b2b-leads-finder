# B2B Leads Finder: Emails & Contacts, Any Company, Live

Python client for **[B2B Leads Finder: Emails & Contacts, Any Company, Live](https://apify.com/themineworks/b2b-leads-finder)** — find B2B leads with emails and contacts for any company, searched live.

> ⚡ No login, no cookies, no ban risk · runs in the cloud on [Apify](https://apify.com/themineworks/b2b-leads-finder)
>
> 💸 From **$3.0 per 1,000 results** (volume discounts on paid Apify plans). You are only charged for delivered results — empty searches and failed pages are never billed.

## Quick start

```bash
pip install apify-client
python3 b2b_leads_finder.py --token YOUR_APIFY_TOKEN --companies "stripe.com,notion.so"
```

Get a free API token: [console.apify.com/sign-up](https://console.apify.com/sign-up) — then find it under **Settings → API & Integrations**.

## Options

| Flag | Type | Description |
|---|---|---|
| `--token` | string | Apify API token (or `APIFY_TOKEN` env var) |
| `--out` | string | Output basename — writes `results.json` + `results.csv` |
| `--companies` | array | List of company names or domains to find leads for (e.g. 'stripe.com', 'notion.so', 'Strip |
| `--job-titles` | array | Filter leads by job title keyword (e.g. 'CEO', 'Head of Marketing', 'VP Sales'). Leave emp |
| `--max-leads-per-company` | integer | Maximum number of leads to find per company across all job title filters. |
| `--scrape-website` | boolean | Visit the company's /team, /about, and /contact pages to find directly-listed emails and n |

Flags map 1:1 to the actor's input schema — full reference and a live output sample on the [Store listing](https://apify.com/themineworks/b2b-leads-finder).

## Output

One row per result, saved as both JSON and CSV with every field the actor returns. Preview the exact fields on the [listing's output tab](https://apify.com/themineworks/b2b-leads-finder).

## Why this actor

- **HTTP-native** — fast, stable, no headless-browser overhead
- **No account risk** — never asks for your login or cookies
- **Fair billing** — pay per delivered result only

MIT © [The Mine Works](https://apify.com/themineworks) — part of a 69-scraper suite trusted by 450+ developers.
