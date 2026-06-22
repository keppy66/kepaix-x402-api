/*
KepAIx Public API Example

Educational use only.
Not financial advice.
*/

const API_URL = "https://kepaix.com/api/market-regime.php";

async function getMarketRegime() {
    try {
        const response = await fetch(API_URL);
        const data = await response.json();

        console.log("KepAIx Market Regime");
        console.log("--------------------");
        console.log("Market Mode:", data.market_mode);
        console.log("Market State:", data.market_state);
        console.log("Confidence:", data.confidence);
        console.log("Risk Score:", data.risk_score);
        console.log("Summary:", data.summary);
        console.log("");
        console.log("Educational only. Not financial advice.");
    } catch (error) {
        console.error("Error:", error);
    }
}

getMarketRegime();
