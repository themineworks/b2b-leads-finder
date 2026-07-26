#!/usr/bin/env python3
"""Find B2B leads with emails and contacts for any company, searched live.
CLI for the themineworks/b2b-leads-finder Apify actor: runs it, waits, saves JSON + CSV.
Free Apify account + API token: https://console.apify.com/sign-up
"""
import argparse, csv, json, os, sys
from apify_client import ApifyClient

ACTOR = "themineworks/b2b-leads-finder"

def main():
    ap = argparse.ArgumentParser(description="find B2B leads with emails and contacts for any company, searched live")
    ap.add_argument("--token", default=os.environ.get("APIFY_TOKEN"),
                    help="Apify API token (or set APIFY_TOKEN env var)")
    ap.add_argument("--out", default="results", help="Output basename (.json and .csv)")
    ap.add_argument("--companies", help="Comma-separated. List of company names or domains to find leads for (e.g. 'stripe.com', 'notion.so', 'Stripe') e.g. stripe.com,notion.so")
    ap.add_argument("--job-titles", help="Comma-separated. Filter leads by job title keyword (e.g. 'CEO', 'Head of Marketing', 'VP Sales') e.g. CEO,Head of Marketing")
    ap.add_argument("--max-leads-per-company", type=int, default=10, help="Maximum number of leads to find per company across all job title filters")
    ap.add_argument("--scrape-website", action="store_true", help="Visit the company's /team, /about, and /contact pages to find directly-listed emails and names")
    a = ap.parse_args()
    if not a.token:
        sys.exit("Provide --token or set APIFY_TOKEN — free token at https://console.apify.com/sign-up")

    run_input = {}
    if a.companies is not None: run_input["companies"] = [s.strip() for s in a.companies.split(",") if s.strip()]
    if a.job_titles is not None: run_input["jobTitles"] = [s.strip() for s in a.job_titles.split(",") if s.strip()]
    if a.max_leads_per_company is not None: run_input["maxLeadsPerCompany"] = a.max_leads_per_company
    if a.scrape_website: run_input["scrapeWebsite"] = True

    client = ApifyClient(a.token)
    print(f"Running {ACTOR} ...")
    run = client.actor(ACTOR).call(run_input=run_input)
    items = list(client.dataset(run["defaultDatasetId"]).iterate_items())

    with open(a.out + ".json", "w", encoding="utf-8") as f:
        json.dump(items, f, indent=2, ensure_ascii=False)
    if items:
        keys = []
        for it in items:
            for k in it:
                if k not in keys: keys.append(k)
        with open(a.out + ".csv", "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=keys, extrasaction="ignore")
            w.writeheader()
            for it in items:
                w.writerow({k: ("" if v is None else v) for k, v in it.items()})
    print(f"Done: {len(items)} results -> {a.out}.json / {a.out}.csv")

if __name__ == "__main__":
    main()
