"""
KepAIx Public API Example

This example calls the free public KepAIx market-regime endpoint.

KepAIx is educational only.
Nothing returned by this API is financial advice.
"""

import json
import urllib.request


API_URL = "https://kepaix.com/api/market-regime.php"


def fetch_kepaix_market_regime():
    with urllib.request.urlopen(API_URL, timeout=20) as response:
        data = response.read().decode("utf-8")
        return json.loads(data)


def main():
    regime = fetch_kepaix_market_regime()

    print("KepAIx Market Regime")
    print("--------------------")
    print("Market Mode:", regime.get("market_mode"))
    print("Market State:", regime.get("market_state"))
    print("Confidence:", regime.get("confidence"))
    print("Risk Score:", regime.get("risk_score"))
    print("Summary:", regime.get("summary"))
    print()
    print("Educational only. Not financial advice.")


if __name__ == "__main__":
    main()
