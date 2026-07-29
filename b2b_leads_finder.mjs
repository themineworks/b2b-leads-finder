#!/usr/bin/env node
// Find B2B leads with emails and contacts.
// Node.js client for the themineworks/b2b-leads-finder Apify actor: runs it, waits, saves results.json.
// Free Apify account + API token: https://console.apify.com/sign-up
import { ApifyClient } from 'apify-client';
import { writeFileSync } from 'node:fs';

const ACTOR = 'themineworks/b2b-leads-finder';

// Flags map 1:1 to the actor's input schema. Run: node b2b_leads_finder.mjs --token YOUR_TOKEN --companies "stripe.com"
function parseArgs(argv) {
    const out = {};
    for (let i = 0; i < argv.length; i++) {
        if (!argv[i].startsWith('--')) continue;
        const key = argv[i].slice(2);
        const val = (argv[i + 1] && !argv[i + 1].startsWith('--')) ? argv[++i] : true;
        out[key] = val;
    }
    return out;
}

const args = parseArgs(process.argv.slice(2));
const token = args.token || process.env.APIFY_TOKEN;
if (!token) {
    console.error('Provide --token or set APIFY_TOKEN — free token at https://console.apify.com/sign-up');
    process.exit(1);
}

const runInput = {};
if (args['companies'] !== undefined) runInput.companies = String(args['companies']).split(',').map(s => s.trim());
if (args['job-titles'] !== undefined) runInput.jobTitles = String(args['job-titles']).split(',').map(s => s.trim());
if (args['max-leads-per-company'] !== undefined) runInput.maxLeadsPerCompany = parseInt(args['max-leads-per-company'], 10);
if (args['scrape-website'] !== undefined) runInput.scrapeWebsite = args['scrape-website'] === true || args['scrape-website'] === 'true';

const client = new ApifyClient({ token });
console.log(`Running ${ACTOR} ...`);
const run = await client.actor(ACTOR).call(runInput);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
writeFileSync('results.json', JSON.stringify(items, null, 2));
console.log(`Saved ${items.length} results to results.json`);
